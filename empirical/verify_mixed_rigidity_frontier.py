"""Probe the mixed-composite affine-rigidity frontier.

This script answers the first coordinate-layer tests suggested by the
`N=12` rigidity pattern:

* `N=12=4*3` is affine-rigid because `S_3 = Aff(Z/3)`.
* `N=20=4*5` and `N=28=4*7` are not affine-rigid; their coordinate
  stabilizers are `Aff(Z/4) x S_p`.
* `N=60=4*3*5` is not affine-rigid; its coordinate stabilizer is
  `Aff(Z/4) x S_3 x S_5`.

The checks stay at the coordinate-pair/vertex-set layer.  They do not claim
full face-lattice or full orthogonal-stabilizer classifications.
"""

from __future__ import annotations

from itertools import product
from math import factorial, gcd
from pathlib import Path

from census_cyclotomic_block_signs import divisors, euler_phi, ramanujan_sum
from verify_mixed_composite_stabilizers import crt_from_pair, crt_pair


TARGETS = [
    (12, (3,)),
    (20, (5,)),
    (28, (7,)),
    (60, (3, 5)),
]


def block_divisors(n: int) -> list[int]:
    return [d for d in divisors(n) if d > 1]


def ramanujan_table(n: int) -> dict[int, list[int]]:
    return {
        d: [ramanujan_sum(d, k) for k in range(n)]
        for d in block_divisors(n)
    }


def diff_pair_signature(
    n: int,
    delta: int,
    table: dict[int, list[int]],
) -> frozenset[tuple[int, int]]:
    blocks = block_divisors(n)
    values: set[tuple[int, int]] = set()
    for signs in product([1, -1], repeat=len(blocks)):
        for a in range(n):
            left = sum(sign * table[d][(-a) % n] for sign, d in zip(signs, blocks))
            right = sum(sign * table[d][(delta - a) % n] for sign, d in zip(signs, blocks))
            values.add((left, right))
    return frozenset(values)


def pair_color_matrix(n: int) -> tuple[list[list[object]], int, list[int]]:
    table = ramanujan_table(n)
    signature_by_delta = {
        delta: diff_pair_signature(n, delta, table)
        for delta in range(1, n)
    }
    signature_to_gcd: dict[object, int] = {}
    gcd_to_signatures: dict[int, set[object]] = {}
    for delta, signature in signature_by_delta.items():
        divisor = gcd(n, delta)
        signature_to_gcd.setdefault(signature, divisor)
        assert signature_to_gcd[signature] == divisor, (n, delta)
        gcd_to_signatures.setdefault(divisor, set()).add(signature)
    assert all(len(signatures) == 1 for signatures in gcd_to_signatures.values()), n

    matrix: list[list[object]] = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = matrix[j][i] = signature_by_delta[(j - i) % n]
    return matrix, len(set(signature_by_delta.values())), sorted(gcd_to_signatures)


def pair_color_automorphism_count(n: int, matrix: list[list[object]]) -> int:
    candidates = {0: [0]}
    for i in range(1, n):
        candidates[i] = [j for j in range(1, n) if matrix[0][i] == matrix[0][j]]
    order = [0] + sorted(range(1, n), key=lambda i: (len(candidates[i]), i))
    used = [False for _ in range(n)]
    mapping: list[int | None] = [None for _ in range(n)]
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
                if matrix[i][k] != matrix[j][mapped_k]:
                    ok = False
                    break
            if ok:
                mapping[i] = j
                used[j] = True
                search(position + 1)
                used[j] = False
                mapping[i] = None

    search(0)
    return n * count


def scaled_vertices(n: int) -> set[tuple[int, ...]]:
    blocks = block_divisors(n)
    table = ramanujan_table(n)
    vertices: set[tuple[int, ...]] = set()
    for signs in product([1, -1], repeat=len(blocks)):
        for a in range(n):
            vertices.add(
                tuple(
                    sum(sign * table[d][(i - a) % n] for sign, d in zip(signs, blocks))
                    for i in range(n)
                )
            )
    return vertices


def from_crt_tuple(moduli: tuple[int, ...], values: tuple[int, ...]) -> int:
    modulus = 1
    out = 0
    for current_modulus, value in zip(moduli, values):
        if modulus == 1:
            out = value
            modulus = current_modulus
        else:
            out = crt_from_pair(modulus * current_modulus, modulus, current_modulus, out, value)
            modulus *= current_modulus
    return out


def to_crt_tuple(moduli: tuple[int, ...], x: int) -> tuple[int, ...]:
    return tuple(x % modulus for modulus in moduli)


def expected_generators(n: int, odd_factors: tuple[int, ...]) -> list[tuple[int, ...]]:
    moduli = (4,) + odd_factors
    generators: list[tuple[int, ...]] = []

    # Aff(Z/4).
    generators.append(
        tuple(
            from_crt_tuple(moduli, ((to_crt_tuple(moduli, x)[0] + 1) % 4,) + to_crt_tuple(moduli, x)[1:])
            for x in range(n)
        )
    )
    generators.append(
        tuple(
            from_crt_tuple(moduli, ((-to_crt_tuple(moduli, x)[0]) % 4,) + to_crt_tuple(moduli, x)[1:])
            for x in range(n)
        )
    )

    # Full symmetric group on each odd prime coordinate, generated by adjacent swaps.
    for coordinate_index, size in enumerate(odd_factors, start=1):
        for swap_index in range(size - 1):
            image = []
            for x in range(n):
                values = list(to_crt_tuple(moduli, x))
                if values[coordinate_index] == swap_index:
                    values[coordinate_index] = swap_index + 1
                elif values[coordinate_index] == swap_index + 1:
                    values[coordinate_index] = swap_index
                image.append(from_crt_tuple(moduli, tuple(values)))
            generators.append(tuple(image))

    return generators


def verify_generators_preserve_vertices(n: int, generators: list[tuple[int, ...]]) -> int:
    vertices = scaled_vertices(n)
    for generator in generators:
        assert all(
            tuple(vertex[generator[i]] for i in range(n)) in vertices
            for vertex in vertices
        ), n
    return len(vertices)


def expected_group_order(odd_factors: tuple[int, ...]) -> int:
    order = 8
    for factor in odd_factors:
        order *= factorial(factor)
    return order


def row_for_target(n: int, odd_factors: tuple[int, ...]) -> dict[str, object]:
    matrix, color_count, gcd_classes = pair_color_matrix(n)
    upper = pair_color_automorphism_count(n, matrix)
    expected = expected_group_order(odd_factors)
    assert upper == expected, (n, upper, expected)
    vertex_count = verify_generators_preserve_vertices(n, expected_generators(n, odd_factors))
    affine_order = n * euler_phi(n)
    return {
        "n": n,
        "factors": "4*" + "*".join(str(factor) for factor in odd_factors),
        "vertices": vertex_count,
        "colors": color_count,
        "gcd_classes": ",".join(str(value) for value in gcd_classes),
        "coordinate_order": upper,
        "affine_order": affine_order,
        "rigid": upper == affine_order,
        "description": "Aff(Z/4) x " + " x ".join(f"S_{factor}" for factor in odd_factors),
    }


def markdown_report(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Mixed Rigidity Frontier",
        "",
        "**Script:** `empirical/verify_mixed_rigidity_frontier.py`",
        "**Status:** pair-color upper bounds match checked CRT generator lower bounds",
        "",
        "This report tests the first `4p` and `4pq` rows suggested by the `N=12` rigidity pattern.  The evidence is coordinate-layer evidence only; no face-lattice or full orthogonal-stabilizer classification is claimed.",
        "",
        "| N | factor form | scaled vertices | pair-color classes | gcd classes | coordinate stabilizer order | affine order | affine-rigid? | description |",
        "|---:|---|---:|---:|---|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row['n']} | "
            f"{row['factors']} | "
            f"{row['vertices']} | "
            f"{row['colors']} | "
            f"`{row['gcd_classes']}` | "
            f"{row['coordinate_order']} | "
            f"{row['affine_order']} | "
            f"{'yes' if row['rigid'] else 'no'} | "
            f"{row['description']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "1. `N=12=4*3` is affine-rigid because the odd factor contributes `S_3`, and `S_3 = Aff(Z/3)`.",
            "2. `N=20=4*5` and `N=28=4*7` are not affine-rigid.  The `4` side remains affine, but the odd prime side contributes the full symmetric group.",
            "3. `N=60=4*3*5` is not affine-rigid.  The first `4pq` row has coordinate stabilizer `Aff(Z/4) x S_3 x S_5`, not `Aff(Z/60)`.",
            "4. The refined conjecture should not be stated as `4p` or `4pq` rigidity.  The correct next target is to characterize when odd CRT factors contribute only their affine subgroup and when they enlarge to full symmetric factors.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = [row_for_target(n, odd_factors) for n, odd_factors in TARGETS]
    report = markdown_report(rows)
    report_path = Path(__file__).parent / "reports" / "mixed_rigidity_frontier.md"
    report_path.write_text(report, encoding="utf-8")

    print("=== Mixed rigidity frontier ===")
    for row in rows:
        print(
            "[ok] "
            f"N={row['n']}: colors={row['colors']}; "
            f"coord={row['coordinate_order']}; aff={row['affine_order']}; "
            f"rigid={row['rigid']}; {row['description']}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
