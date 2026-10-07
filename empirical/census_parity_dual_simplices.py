"""Census parity-dual simplex compounds for small even N.

This script supports `8.parity_dual_simplices.md`.
It computes exact Gram profiles for V_N union W_N, normalized absolute
angle profiles, coherence versus the Welch bound, and stabilizer orders.
"""

from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path


TARGETS = [4, 6, 8, 10, 12]
BRUTE_COORDINATE_TARGETS = {4, 6, 8}


def vec_dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum(x * y for x, y in zip(a, b))


def mat_vec(a: list[list[Fraction]], v: list[Fraction]) -> list[Fraction]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def vec_neg(v: list[Fraction]) -> list[Fraction]:
    return [-x for x in v]


def vec_key(v: list[Fraction]) -> tuple[Fraction, ...]:
    return tuple(v)


def permute_vec(perm: tuple[int, ...], v: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0, 1) for _ in v]
    for i, target in enumerate(perm):
        out[target] = v[i]
    return out


def simplex_vertices(n: int) -> list[list[Fraction]]:
    vertices = []
    for i in range(n):
        v = [Fraction(-1, n) for _ in range(n)]
        v[i] += Fraction(1, 1)
        vertices.append(v)
    return vertices


def parity_vector(n: int) -> list[Fraction]:
    return [Fraction(1 if i % 2 == 0 else -1, 1) for i in range(n)]


def parity_reflection(n: int) -> list[list[Fraction]]:
    s = parity_vector(n)
    return [
        [
            Fraction(1 if i == j else 0, 1) - Fraction(2, n) * s[i] * s[j]
            for j in range(n)
        ]
        for i in range(n)
    ]


def compound_vertices(n: int) -> list[list[Fraction]]:
    v = simplex_vertices(n)
    rho = parity_reflection(n)
    w = [mat_vec(rho, vertex) for vertex in v]
    return v + w


def pair_profile(vertices: list[list[Fraction]]) -> Counter[Fraction]:
    profile: Counter[Fraction] = Counter()
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            profile[vec_dot(vertices[i], vertices[j])] += 1
    return profile


def normalized_abs_profile(n: int, raw_profile: Counter[Fraction]) -> Counter[Fraction]:
    norm_factor = Fraction(n, n - 1)
    profile: Counter[Fraction] = Counter()
    for value, count in raw_profile.items():
        profile[abs(value * norm_factor)] += count
    return profile


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def format_profile(profile: Counter[Fraction]) -> str:
    return "; ".join(
        f"{format_fraction(value)}:{profile[value]}"
        for value in sorted(profile)
    )


def coordinate_stabilizer_order(n: int) -> int:
    if n == 4:
        return math.factorial(4)
    m = n // 2
    return 2 * math.factorial(m) * math.factorial(m)


def full_gram_automorphism_order(n: int) -> int:
    # The closed form is proved in `8.parity_dual_simplices.md`, Theorem 6.1.
    if n == 4:
        return 48
    return 2 * coordinate_stabilizer_order(n)


def central_inversion_preserves_compound(n: int) -> bool:
    compound = compound_vertices(n)
    compound_set = {vec_key(v) for v in compound}
    return {vec_key(vec_neg(v)) for v in compound} == compound_set


def brute_coordinate_stabilizer_order(n: int) -> int:
    compound = compound_vertices(n)
    compound_set = {vec_key(v) for v in compound}
    count = 0
    for perm in permutations(range(n)):
        image = {vec_key(permute_vec(perm, v)) for v in compound}
        if image == compound_set:
            count += 1
    return count


def expected_raw_profile(n: int) -> Counter[Fraction]:
    """Closed form raw off-diagonal profile for V_N union W_N."""
    profile: Counter[Fraction] = Counter()
    profile[Fraction(-1, n)] += n * (n - 1)
    profile[Fraction(n - 3, n)] += n
    profile[Fraction(-3, n)] += n * (n - 2) // 2
    profile[Fraction(1, n)] += n * n // 2
    return profile


def welch_bound(num_vectors: int, dimension: int) -> float:
    return math.sqrt((num_vectors - dimension) / (dimension * (num_vectors - 1)))


def census_row(n: int) -> dict[str, object]:
    compound = compound_vertices(n)
    raw = pair_profile(compound)
    expected = expected_raw_profile(n)
    assert raw == expected, (n, raw, expected)

    abs_profile = normalized_abs_profile(n, raw)
    coherence = max(abs_profile)
    dimension = n - 1
    num_vectors = 2 * n
    welch = welch_bound(num_vectors, dimension)

    coordinate_order = coordinate_stabilizer_order(n)
    if n in BRUTE_COORDINATE_TARGETS:
        brute_order = brute_coordinate_stabilizer_order(n)
        assert brute_order == coordinate_order, (n, brute_order, coordinate_order)
    else:
        brute_order = None

    return {
        "n": n,
        "dimension": dimension,
        "num_vectors": num_vectors,
        "raw_profile": raw,
        "abs_profile": abs_profile,
        "coherence": coherence,
        "welch": welch,
        "coordinate_order": coordinate_order,
        "brute_order": brute_order,
        "full_gram_order": full_gram_automorphism_order(n),
        "central_inversion": central_inversion_preserves_compound(n),
    }


def markdown_report(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Parity-Dual Even-N Census",
        "",
        "**Script:** `empirical/census_parity_dual_simplices.py`",
        "**Companion note:** `8.parity_dual_simplices.md`",
        "**Status:** all checks passed",
        "",
        "This census covers the compound `V_N union W_N` for even `N=4,6,8,10,12`, where `W_N=rho_2(V_N)`.  All Gram profiles are exact rational counts.  Coherence is computed after unit-normalizing the vectors.  The Welch bound is included as a packing baseline for `2N` unit vectors in dimension `N-1`.",
        "",
        "The coordinate stabilizer is the subgroup of ambient coordinate permutations preserving the compound.  For `N=4` this is the full tetrahedral coordinate action `S_4`.  For `N=2m>=6`, Theorem 6.1 of the companion note proves the parity-class wreath product `(S_m x S_m) semidirect C_2`, of order `2(m!)^2`, preserving or swapping the even/odd coordinate classes.  The full Gram automorphism group, equivalently the ambient orthogonal stabilizer, additionally includes the simplex-swap induced by `rho_2`; for `N=4` this is the full cube/stella-octangula order `48`.",
        "",
        "| N | dim | raw off-diagonal Gram profile | normalized absolute profile | coherence | Welch | coordinate stabilizer | full Gram/orthogonal stabilizer | central inversion |",
        "|---:|---:|---|---|---:|---:|---:|---:|---|",
    ]

    for row in rows:
        coherence = row["coherence"]
        assert isinstance(coherence, Fraction)
        lines.append(
            "| "
            f"{row['n']} | "
            f"{row['dimension']} | "
            f"`{format_profile(row['raw_profile'])}` | "
            f"`{format_profile(row['abs_profile'])}` | "
            f"{format_fraction(coherence)} ({float(coherence):.6f}) | "
            f"{row['welch']:.6f} | "
            f"{row['coordinate_order']} | "
            f"{row['full_gram_order']} | "
            f"{'yes' if row['central_inversion'] else 'no'} |"
        )

    lines.extend(
        [
            "",
            "## Brute Coordinate Checks",
            "",
            "The coordinate stabilizer orders for `N=4,6,8` were verified by exhaustive enumeration of all ambient coordinate permutations.  The `N=10,12` entries use the closed-form parity-class stabilizer count, because brute force over `10!` and `12!` permutations is unnecessary for this census.",
            "",
            "| N | brute coordinate stabilizer | formula |",
            "|---:|---:|---:|",
        ]
    )
    for row in rows:
        if row["brute_order"] is not None:
            lines.append(
                f"| {row['n']} | {row['brute_order']} | {row['coordinate_order']} |"
            )

    lines.extend(
        [
            "",
            "## Consequences",
            "",
            "1. The `N=4` case is exceptional: `W_4=-V_4` up to relabeling, central inversion preserves the compound, and the full Gram/orthogonal stabilizer has order `48`.",
            "2. For `N>=6`, central inversion does not preserve the compound.  The coordinate stabilizer is exactly the parity-class wreath product proved in Theorem 6.1.",
            "3. The full compound is not a single ETF in these tested cases.  Each component simplex is an ETF, but the union has multiple normalized absolute inner products and does not meet the Welch bound.",
            "4. The largest cross-angle grows with `N`: the coherence is `(N-3)/(N-1)` for `N>=8`, while the Welch baseline decreases.  This suggests the parity-dual compound is better studied as a structured two-simplex compound than as a Grassmannian packing candidate.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = [census_row(n) for n in TARGETS]
    report = markdown_report(rows)
    report_path = Path(__file__).parent / "reports" / "parity_dual_census.md"
    report_path.write_text(report, encoding="utf-8")

    print("=== Parity-dual even-N census ===")
    for row in rows:
        coherence = row["coherence"]
        assert isinstance(coherence, Fraction)
        brute = (
            f", brute={row['brute_order']}"
            if row["brute_order"] is not None
            else ""
        )
        print(
            "[ok] "
            f"N={row['n']}: abs profile={format_profile(row['abs_profile'])}; "
            f"coherence={format_fraction(coherence)} ({float(coherence):.6f}); "
            f"Welch={row['welch']:.6f}; "
            f"coord={row['coordinate_order']}{brute}; "
            f"full-gram={row['full_gram_order']}; "
            f"central-inversion={'yes' if row['central_inversion'] else 'no'}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
