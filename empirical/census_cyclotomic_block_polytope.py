"""Round 3 census for full cyclotomic block-sign polytopes.

This script supports Section 8 of `8.parity_dual_simplices.md`.
It keeps the primary reported checks exact.  It uses:

* closed formulas for the prime antipodal-simplex family;
* exact facet enumeration for the first composite case, N=6;
* optional SciPy/Qhull facet seeds for selected larger composite hulls,
  followed by exact rational exposed-face reconstruction;
* a colored-pair upper-bound computation for coordinate stabilizers in
  selected small composite cases.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial, gcd
from pathlib import Path

try:
    import numpy as np
    from scipy.spatial import ConvexHull
except ImportError:  # pragma: no cover - optional local enhancement
    np = None
    ConvexHull = None

from census_cyclotomic_block_signs import (
    divisors,
    euler_phi,
    simplex_image,
    simplex_vertices,
)


TARGETS = [3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 24]
COORD_STABILIZER_TARGETS = [6, 8, 9, 10, 12]
SCIPY_HULL_TARGETS = [8, 9, 10]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


def block_divisors(n: int) -> list[int]:
    return [d for d in divisors(n) if d > 1]


def full_spectral_simplices(n: int) -> list[tuple[tuple[Fraction, ...], ...]]:
    vertices = simplex_vertices(n)
    blocks = block_divisors(n)
    signs_list = list(product([1, -1], repeat=len(blocks)))
    return sorted(set(simplex_image(n, vertices, blocks, signs) for signs in signs_list))


def full_spectral_vertices(n: int) -> list[tuple[Fraction, ...]]:
    return sorted({vertex for simplex in full_spectral_simplices(n) for vertex in simplex})


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivots: list[int] = []
    r = 0
    for c in range(cols):
        pivot_row = None
        for i in range(r, rows):
            if a[i][c] != 0:
                pivot_row = i
                break
        if pivot_row is None:
            continue
        a[r], a[pivot_row] = a[pivot_row], a[r]
        pivot = a[r][c]
        a[r] = [x / pivot for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                factor = a[i][c]
                a[i] = [a[i][j] - factor * a[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return a, pivots


def rank(rows: list[list[Fraction]] | list[tuple[Fraction, ...]]) -> int:
    if not rows:
        return 0
    _, pivots = rref([list(row) for row in rows])
    return len(pivots)


def null_vector(rows: list[list[Fraction]], n: int) -> list[Fraction] | None:
    reduced, pivots = rref(rows)
    free = [c for c in range(n) if c not in pivots]
    if len(free) != 1:
        return None
    free_col = free[0]
    out = [Fraction(0, 1) for _ in range(n)]
    out[free_col] = Fraction(1, 1)
    for row_index, pivot_col in enumerate(pivots):
        out[pivot_col] = -reduced[row_index][free_col]
    return out


def affine_dimension(face: frozenset[int], vertices: list[tuple[Fraction, ...]]) -> int:
    if len(face) <= 1:
        return len(face) - 1
    ids = list(face)
    base = vertices[ids[0]]
    rows = [
        [vertices[i][j] - base[j] for j in range(len(base))]
        for i in ids[1:]
    ]
    return rank(rows)


def exact_facets(vertices: list[tuple[Fraction, ...]]) -> list[frozenset[int]]:
    """Enumerate facets by exact supporting-hyperplane tests.

    This is intended for the first composite case, N=6.  It enumerates
    dimension-sized vertex subsets, constructs the rational normal in
    the zero-sum hyperplane, and deduplicates the resulting exposed
    vertex sets.
    """

    n = len(vertices[0])
    dim = rank(vertices)
    one = [Fraction(1, 1) for _ in range(n)]
    facets: set[frozenset[int]] = set()

    for combo in combinations(range(len(vertices)), dim):
        base = vertices[combo[0]]
        rows = [
            [vertices[idx][j] - base[j] for j in range(n)]
            for idx in combo[1:]
        ]
        rows.append(one)
        normal = null_vector(rows, n)
        if normal is None:
            continue

        values = [
            sum(normal[j] * vertex[j] for j in range(n))
            for vertex in vertices
        ]
        chosen_value = values[combo[0]]
        if chosen_value == 0:
            continue

        high = max(values)
        low = min(values)
        if chosen_value == high:
            facets.add(frozenset(i for i, value in enumerate(values) if value == high))
        elif chosen_value == low:
            facets.add(frozenset(i for i, value in enumerate(values) if value == low))

    return sorted(facets, key=lambda face: (len(face), sorted(face)))


def exact_exposed_face_from_indices(
    vertices: list[tuple[Fraction, ...]],
    indices: tuple[int, ...],
) -> frozenset[int] | None:
    """Recover the full exact exposed face generated by coplanar indices."""

    n = len(vertices[0])
    base = vertices[indices[0]]
    rows = [
        [vertices[idx][j] - base[j] for j in range(n)]
        for idx in indices[1:]
    ]
    rows.append([Fraction(1, 1) for _ in range(n)])
    normal = null_vector(rows, n)
    if normal is None:
        return None

    values = [
        sum(normal[j] * vertex[j] for j in range(n))
        for vertex in vertices
    ]
    chosen_value = values[indices[0]]
    high = max(values)
    low = min(values)
    if chosen_value == high:
        return frozenset(i for i, value in enumerate(values) if value == high)
    if chosen_value == low:
        return frozenset(i for i, value in enumerate(values) if value == low)
    return None


def scipy_seeded_facets(
    vertices: list[tuple[Fraction, ...]],
) -> list[frozenset[int]] | None:
    """Use Qhull facet hyperplanes, then reconstruct exact rational facets.

    The points live in the zero-sum hyperplane, so deleting the final
    coordinate gives an affine chart of dimension N-1.  Qhull may
    triangulate nonsimplicial facets; each reported hyperplane is used
    only to locate candidate coplanar vertices, and those candidates are
    lifted back to the exact coordinate model.
    """

    if np is None or ConvexHull is None:
        return None

    dim = rank(vertices)
    points = np.array(
        [[float(value) for value in vertex[:-1]] for vertex in vertices],
        dtype=float,
    )
    hull = ConvexHull(points, qhull_options="Qx")
    facets: set[frozenset[int]] = set()
    for equation in hull.equations:
        distances = points @ equation[:-1] + equation[-1]
        indices = tuple(
            int(index)
            for index, distance in enumerate(distances)
            if abs(distance) <= 1e-7
        )
        if len(indices) < dim:
            continue
        face = exact_exposed_face_from_indices(
            vertices,
            indices,
        )
        if face is None:
            continue
        if affine_dimension(face, vertices) != dim - 1:
            raise RuntimeError(f"Qhull hyperplane exposed a nonfacet: {sorted(face)}")
        facets.add(face)
    if not facets:
        raise RuntimeError("Qhull did not expose any rational facets")
    return sorted(facets, key=lambda face: (len(face), sorted(face)))


def f_vector_from_facets(
    vertices: list[tuple[Fraction, ...]],
    facets: list[frozenset[int]],
) -> list[int]:
    faces: set[frozenset[int]] = {frozenset(range(len(vertices)))}
    for facet in facets:
        new_faces = set(faces)
        for face in faces:
            intersection = face & facet
            if intersection:
                new_faces.add(intersection)
        faces = new_faces

    dim = rank(vertices)
    return [
        sum(1 for face in faces if affine_dimension(face, vertices) == k)
        for k in range(dim)
    ]


def antipodal_simplex_f_vector(n: int) -> list[int]:
    """F-vector of conv(+/- V_N).

    For r<N, a signed r-subset gives a face exactly when the remaining
    free coordinates can balance the signed sum.  If N is even, the
    facets are the balanced full signed subsets.
    """

    dim = n - 1
    f_vector: list[int] = []
    for k in range(dim):
        if n % 2 == 0 and k == dim - 1:
            f_vector.append(factorial(n) // (factorial(n // 2) ** 2))
            continue
        r = k + 1
        total = 0
        for plus_count in range(r + 1):
            minus_count = r - plus_count
            free_count = n - r
            if abs(plus_count - minus_count) < free_count:
                total += factorial(n) // (
                    factorial(plus_count)
                    * factorial(minus_count)
                    * factorial(free_count)
                )
        f_vector.append(total)
    return f_vector


def pair_colors(
    n: int,
    vertices: list[tuple[Fraction, ...]],
) -> dict[tuple[int, int], tuple[tuple[Fraction, Fraction], ...]]:
    return {
        (i, j): tuple(sorted((vertex[i], vertex[j]) for vertex in vertices))
        for i in range(n)
        for j in range(i + 1, n)
    }


def edge_color(
    colors: dict[tuple[int, int], tuple[tuple[Fraction, Fraction], ...]],
    i: int,
    j: int,
) -> tuple[tuple[Fraction, Fraction], ...]:
    return colors[(i, j)] if i < j else colors[(j, i)]


def colored_pair_automorphism_count(
    n: int,
    vertices: list[tuple[Fraction, ...]],
) -> int:
    """Count automorphisms of the coordinate pair-color invariant.

    This is an exact upper bound for coordinate permutations preserving
    the vertex set.  For the reported targets the count matches an
    explicit lower-bound group, so the coordinate stabilizer is exact.
    """

    colors = pair_colors(n, vertices)
    vertex_colors = [
        tuple(sorted(edge_color(colors, i, j) for j in range(n) if j != i))
        for i in range(n)
    ]
    classes: dict[tuple[object, ...], list[int]] = defaultdict(list)
    for i, color in enumerate(vertex_colors):
        classes[color].append(i)

    order = sorted(range(n), key=lambda i: (len(classes[vertex_colors[i]]), i))
    candidates = {i: classes[vertex_colors[i]][:] for i in range(n)}
    used = [False] * n
    mapping: list[int | None] = [None] * n
    count = 0

    def search(position: int) -> None:
        nonlocal count
        if position == n:
            count += 1
            return
        i = order[position]
        for j in candidates[i]:
            if used[j]:
                continue
            ok = True
            for previous_position in range(position):
                k = order[previous_position]
                mapped_k = mapping[k]
                assert mapped_k is not None
                if edge_color(colors, i, k) != edge_color(colors, j, mapped_k):
                    ok = False
                    break
            if ok:
                mapping[i] = j
                used[j] = True
                search(position + 1)
                used[j] = False
                mapping[i] = None

    search(0)
    return count


def permutes_vertex_set(
    n: int,
    vertices: list[tuple[Fraction, ...]],
    permutation: tuple[int, ...],
) -> bool:
    vertex_set = set(vertices)
    return all(
        tuple(vertex[permutation[i]] for i in range(n)) in vertex_set
        for vertex in vertices
    )


def parity_wreath_permutations(n: int) -> list[tuple[int, ...]]:
    even = list(range(0, n, 2))
    odd = list(range(1, n, 2))
    out: list[tuple[int, ...]] = []
    for even_perm in product_permutations(even):
        for odd_perm in product_permutations(odd):
            preserve = list(range(n))
            for new, old in zip(even, even_perm):
                preserve[new] = old
            for new, old in zip(odd, odd_perm):
                preserve[new] = old
            out.append(tuple(preserve))

            swap = list(range(n))
            for new, old in zip(even, odd_perm):
                swap[new] = old
            for new, old in zip(odd, even_perm):
                swap[new] = old
            out.append(tuple(swap))
    return out


def residue_wreath_permutations(n: int, modulus: int) -> list[tuple[int, ...]]:
    blocks = [[i for i in range(n) if i % modulus == r] for r in range(modulus)]
    out: list[tuple[int, ...]] = []
    for block_perm in product_permutations(list(range(modulus))):
        block_internal_perms = [product_permutations(block) for block in blocks]
        for internal_choices in product(*block_internal_perms):
            p = list(range(n))
            for new_block_index, old_block_index in enumerate(block_perm):
                new_block = blocks[new_block_index]
                old_entries = internal_choices[old_block_index]
                for new, old in zip(new_block, old_entries):
                    p[new] = old
            out.append(tuple(p))
    return out


def affine_permutations(n: int) -> list[tuple[int, ...]]:
    return [
        tuple((a * i + b) % n for i in range(n))
        for a in range(n)
        if gcd(a, n) == 1
        for b in range(n)
    ]


def product_permutations(values: list[int]) -> list[tuple[int, ...]]:
    if not values:
        return [()]
    out: list[tuple[int, ...]] = []
    for i, value in enumerate(values):
        rest = values[:i] + values[i + 1 :]
        for tail in product_permutations(rest):
            out.append((value,) + tail)
    return out


def expected_coordinate_order(n: int) -> tuple[int, str] | None:
    if is_prime(n) or n == 4:
        return factorial(n), "S_N (antipodal simplex compound)"
    if n in {6, 8, 10}:
        m = n // 2
        return 2 * factorial(m) ** 2, f"S_{m} wr S_2"
    if n == 9:
        return factorial(3) ** 4, "S_3 wr S_3"
    if n == 12:
        return n * euler_phi(n), "Aff(Z/12)"
    return None


def expected_coordinate_permutations(n: int) -> list[tuple[int, ...]] | None:
    if is_prime(n) or n == 4:
        return product_permutations(list(range(n)))
    if n in {6, 8, 10}:
        return parity_wreath_permutations(n)
    if n == 9:
        return residue_wreath_permutations(n, 3)
    if n == 12:
        return affine_permutations(n)
    return None


def frontier_coordinate_summary(n: int) -> tuple[int, str] | None:
    return {
        18: (559872, "exact in mixed-composite verifier; S_3^6 semidirect Aff(Z/6)"),
        20: (960, "exact in mixed-composite verifier; Aff(Z/4) x S_5"),
        24: (768, "exact in mixed-composite verifier; full gcd-distance scheme"),
    }.get(n)


def spectral_affine_orthogonal_lower_order(n: int, distinct_simplices: int) -> int:
    return distinct_simplices * n * euler_phi(n)


def format_list(values: list[int] | None) -> str:
    if values is None:
        return "not computed"
    return "(" + ", ".join(str(value) for value in values) + ")"


def row_for_n(n: int) -> dict[str, object]:
    vertices = full_spectral_vertices(n)
    simplices = full_spectral_simplices(n)
    dim = rank(vertices)
    distinct_simplices = len(simplices)

    f_vector: list[int] | None = None
    hull_note = "general polar intersection"
    facet_sizes = "not computed"

    if is_prime(n) or n == 4:
        f_vector = antipodal_simplex_f_vector(n)
        hull_note = "conv(+/- simplex); polar is cube slice"
        facet_sizes = "simplicial" if n % 2 else "balanced nonsimplicial facets"
    elif n == 6:
        facets = exact_facets(vertices)
        scipy_facets = scipy_seeded_facets(vertices)
        if scipy_facets is not None:
            assert set(scipy_facets) == set(facets), n
        f_vector = f_vector_from_facets(vertices, facets)
        facet_sizes = ",".join(str(size) for size in sorted({len(face) for face in facets}))
        hull_note = "exact facet enumeration"
    elif n in SCIPY_HULL_TARGETS:
        facets = scipy_seeded_facets(vertices)
        if facets is not None:
            f_vector = f_vector_from_facets(vertices, facets)
            facet_sizes = ",".join(str(size) for size in sorted({len(face) for face in facets}))
            hull_note = "SciPy/Qhull-seeded exact facet reconstruction"

    coordinate_order: int | None = None
    coordinate_note = "not enumerated"
    expected = expected_coordinate_order(n)
    if expected is not None:
        expected_order, expected_note = expected
        expected_perms = expected_coordinate_permutations(n)
        assert expected_perms is not None
        assert len(set(expected_perms)) == expected_order, (n, len(set(expected_perms)), expected_order)
        assert all(permutes_vertex_set(n, vertices, perm) for perm in expected_perms), n
        if n in COORD_STABILIZER_TARGETS:
            upper_bound = colored_pair_automorphism_count(n, vertices)
            assert upper_bound == expected_order, (n, upper_bound, expected_order)
            coordinate_order = upper_bound
            coordinate_note = f"exact by pair-color upper bound; {expected_note}"
        else:
            coordinate_order = expected_order
            coordinate_note = expected_note
    else:
        frontier = frontier_coordinate_summary(n)
        if frontier is not None:
            coordinate_order, coordinate_note = frontier

    return {
        "n": n,
        "dim": dim,
        "blocks": block_divisors(n),
        "simplices": distinct_simplices,
        "vertices": len(vertices),
        "antipodal_pairs": len(vertices) // 2,
        "f_vector": f_vector,
        "hull_note": hull_note,
        "facet_sizes": facet_sizes,
        "coordinate_order": coordinate_order,
        "coordinate_note": coordinate_note,
        "spectral_affine_orthogonal_lower": spectral_affine_orthogonal_lower_order(n, distinct_simplices),
    }


def markdown_report(rows: list[dict[str, object]]) -> str:
    status = "exact checks passed for the reported rows"
    if any("SciPy/Qhull" in str(row["hull_note"]) for row in rows):
        status = "exact and SciPy/Qhull-seeded checks passed for the reported rows"

    lines = [
        "# Cyclotomic Block-Sign Polytope Census",
        "",
        "**Script:** `empirical/census_cyclotomic_block_polytope.py`",
        "**Companion note:** `8.parity_dual_simplices.md`",
        f"**Status:** {status}",
        "",
        "The full spectral compound is",
        "",
        "```text",
        "X_N^spec = union_{T in B_N/K_N} T(V_N).",
        "```",
        "",
        "Its polar has the exact description",
        "",
        "```text",
        "conv(X_N^spec)^o = intersection_T T([-1,1]^N cap H_N),",
        "```",
        "",
        "where `T` ranges over distinct block-sign simplex images.  This gives a safe all-`N` convex-hull handle even when full facet enumeration is impractical.",
        "",
        "| N | dim | blocks | simplices | vertices | antipodal pairs | f-vector / facet data | coordinate stabilizer | spectral-affine orthogonal lower | notes |",
        "|---:|---:|---|---:|---:|---:|---|---|---:|---|",
    ]

    for row in rows:
        coord_order = row["coordinate_order"]
        coord_text = "not enumerated"
        if isinstance(coord_order, int):
            coord_text = f"{coord_order} ({row['coordinate_note']})"
        lines.append(
            "| "
            f"{row['n']} | "
            f"{row['dim']} | "
            f"`{row['blocks']}` | "
            f"{row['simplices']} | "
            f"{row['vertices']} | "
            f"{row['antipodal_pairs']} | "
            f"`{format_list(row['f_vector'])}`; facets `{row['facet_sizes']}` | "
            f"{coord_text} | "
            f"{row['spectral_affine_orthogonal_lower']} | "
            f"{row['hull_note']} |"
        )

    lines.extend(
        [
            "",
            "## Prime-family formula",
            "",
            "For odd prime `p`, the block-sign group is `{I,-I}` on `H_p`, so",
            "",
            "```text",
            "X_p^spec = V_p union -V_p.",
            "```",
            "",
            "The polar is the central cube slice `[-1,1]^p cap H_p`.  The hull is simplicial, and for `0 <= k <= p-2`,",
            "",
            "```text",
            "f_k = sum_{a+b=k+1, |a-b| < p-k-1} p!/(a! b! (p-a-b)!).",
            "```",
            "",
            "The number of facets is therefore `p * binomial(p-1,(p-1)/2)`.  The full orthogonal stabilizer in this prime family is `C_2 x S_p`; the coordinate stabilizer is `S_p`.",
            "",
            "## Composite cautions",
            "",
            "1. The composite hulls do not yet have a uniform product/free-sum classification analogous to the parity-only prism theorem.",
            "2. The first composite full spectral hull, `N=6`, has analytic decomposition `(hexagon free-sum hexagon) x I`, exact f-vector `(24, 108, 192, 144, 38)`, and facets with 8 or 12 vertices.",
            "3. Prime-power coordinate stabilizers are now separated in `empirical/reports/prime_power_stabilizers.md`: odd prime powers have p-adic congruence-tree wreath products, while powers of two have fused `S_4` fibers.",
            "4. Mixed composite coordinate stabilizers are separated in `empirical/reports/mixed_composite_stabilizers.md`: they range from parity collapse to CRT product actions to divisor-lattice rigidity.",
            "5. The full Gram/orthogonal stabilizers of the composite full spectral hulls are not classified here.  The listed `spectral-affine orthogonal lower` is only the safe subgroup generated by block signs and affine cyclic relabelings.  It is not a coordinate-stabilizer count, so it can be larger than the coordinate stabilizer.",
            "6. The `N=8,9,10` f-vectors are included as SciPy/Qhull-seeded computations: Qhull supplies facet hyperplane hints, and the script expands each candidate to an exact rational exposed facet before counting faces.",
            "7. The frontier rows `N=18,20,24` report safe vertex/block/lower-bound data and cross-reference exact coordinate stabilizer data from `empirical/reports/mixed_composite_stabilizers.md`.  They are included to guide the mixed-composite program, not to claim face-lattice or full orthogonal-stabilizer classifications.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = [row_for_n(n) for n in TARGETS]
    report = markdown_report(rows)
    report_path = Path(__file__).parent / "reports" / "cyclotomic_block_polytope.md"
    report_path.write_text(report, encoding="utf-8")

    print("=== Cyclotomic block-sign polytope census ===")
    for row in rows:
        print(
            "[ok] "
            f"N={row['n']}: dim={row['dim']}; simplices={row['simplices']}; "
            f"vertices={row['vertices']}; f={format_list(row['f_vector'])}; "
            f"coord={row['coordinate_order'] or 'not-enumerated'}; "
            f"spectral-affine-orthogonal-lower={row['spectral_affine_orthogonal_lower']}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
