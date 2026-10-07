"""Census full cyclotomic block-sign compounds.

This script supports Section 8 of `8.parity_dual_simplices.md`.
It uses exact rational arithmetic and the Ramanujan-sum formula for the
orthogonal projectors onto cyclotomic blocks:

    P_d[i,j] = c_d(i-j) / N.

The block-sign group B_N flips arbitrary cyclotomic summands H_N^[d],
d | N, d > 1.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from pathlib import Path


TARGETS = list(range(3, 17))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_factors(n: int) -> list[int]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def mobius(n: int) -> int:
    if n == 1:
        return 1
    factors = prime_factors(n)
    prod_factors = 1
    for p in factors:
        prod_factors *= p
    if prod_factors != n:
        return 0
    return -1 if len(factors) % 2 else 1


def euler_phi(n: int) -> int:
    out = n
    for p in prime_factors(n):
        out = out // p * (p - 1)
    return out


def ramanujan_sum(q: int, k: int) -> int:
    g = gcd(q, k)
    h = q // g
    return mobius(h) * euler_phi(q) // euler_phi(h)


def simplex_vertices(n: int) -> list[list[Fraction]]:
    vertices = []
    for i in range(n):
        v = [Fraction(-1, n) for _ in range(n)]
        v[i] += Fraction(1, 1)
        vertices.append(v)
    return vertices


def block_sign_matrix(n: int, block_divisors: list[int], signs: tuple[int, ...]) -> list[list[Fraction]]:
    sign_by_divisor = dict(zip(block_divisors, signs))
    return [
        [
            Fraction(1, n)
            + sum(
                Fraction(sign_by_divisor[d] * ramanujan_sum(d, i - j), n)
                for d in block_divisors
            )
            for j in range(n)
        ]
        for i in range(n)
    ]


def mat_vec(a: list[list[Fraction]], v: list[Fraction]) -> list[Fraction]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def vec_dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum(x * y for x, y in zip(a, b))


def frame_operator(vertices: list[tuple[Fraction, ...]]) -> list[list[Fraction]]:
    n = len(vertices[0])
    return [
        [sum(vertex[i] * vertex[j] for vertex in vertices) for j in range(n)]
        for i in range(n)
    ]


def expected_projector(n: int) -> list[list[Fraction]]:
    return [
        [Fraction(1 if i == j else 0, 1) - Fraction(1, n) for j in range(n)]
        for i in range(n)
    ]


def vec_key(v: list[Fraction]) -> tuple[Fraction, ...]:
    return tuple(v)


def simplex_image(
    n: int,
    vertices: list[list[Fraction]],
    block_divisors: list[int],
    signs: tuple[int, ...],
) -> tuple[tuple[Fraction, ...], ...]:
    matrix = block_sign_matrix(n, block_divisors, signs)
    image = [vec_key(mat_vec(matrix, v)) for v in vertices]
    return tuple(sorted(image))


def half_turn_signs(n: int, block_divisors: list[int]) -> tuple[int, ...] | None:
    if n % 2:
        return None
    signs = []
    for d in block_divisors:
        signs.append(-1 if (n // d) % 2 else 1)
    return tuple(signs)


def pair_profile(vertices: list[tuple[Fraction, ...]]) -> Counter[Fraction]:
    profile: Counter[Fraction] = Counter()
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            profile[vec_dot(list(vertices[i]), list(vertices[j]))] += 1
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


def format_profile(profile: Counter[Fraction], max_items: int = 8) -> str:
    items = sorted(profile)
    shown = items[:max_items]
    text = "; ".join(f"{format_fraction(value)}:{profile[value]}" for value in shown)
    if len(items) > max_items:
        text += f"; ... ({len(items)} values)"
    return text


def welch_squared(line_count: int, dimension: int) -> Fraction:
    if line_count <= dimension:
        return Fraction(0, 1)
    return Fraction(line_count - dimension, dimension * (line_count - 1))


def levenshtein_second_squared(line_count: int, dimension: int) -> Fraction | None:
    """Second real projective Levenshtein bound, when its range applies."""
    first_threshold = dimension * (dimension + 1) // 2
    second_threshold = dimension * (dimension + 1) * (dimension + 2) // 6
    if not (first_threshold < line_count <= second_threshold):
        return None
    return Fraction(
        3 * line_count - dimension * (dimension + 2),
        (dimension + 2) * (line_count - dimension),
    )


def format_sqrt(value: Fraction) -> str:
    if value == 0:
        return "0"
    numerator_root = isqrt(value.numerator)
    denominator_root = isqrt(value.denominator)
    if numerator_root * numerator_root == value.numerator and denominator_root * denominator_root == value.denominator:
        return format_fraction(Fraction(numerator_root, denominator_root))
    return f"sqrt({format_fraction(value)})"


def census_row(n: int) -> dict[str, object]:
    block_divisors = [d for d in divisors(n) if d > 1]
    vertices = simplex_vertices(n)
    signs_list = list(product([1, -1], repeat=len(block_divisors)))
    image_by_signs = {
        signs: simplex_image(n, vertices, block_divisors, signs)
        for signs in signs_list
    }
    distinct_simplices = sorted(set(image_by_signs.values()))
    simplex_index = {simp: idx for idx, simp in enumerate(distinct_simplices)}
    kernel = [
        signs
        for signs, simplex in image_by_signs.items()
        if simplex_index[simplex] == simplex_index[image_by_signs[tuple([1] * len(block_divisors))]]
    ]

    half_turn = half_turn_signs(n, block_divisors)
    if n % 2 == 0:
        assert half_turn in kernel, (n, half_turn, kernel)
        expected_orbit = 2 ** max(len(block_divisors) - 1, 0)
    else:
        expected_orbit = 2 ** len(block_divisors)
    assert len(distinct_simplices) == expected_orbit, (n, len(distinct_simplices), expected_orbit)

    union_vertices = sorted({vertex for simplex in distinct_simplices for vertex in simplex})
    assert len(union_vertices) == n * len(distinct_simplices), n

    raw_profile = pair_profile(union_vertices)
    abs_profile = normalized_abs_profile(n, raw_profile)
    projective_values = [value for value in abs_profile if value < 1]
    projective_coherence = max(projective_values) if projective_values else Fraction(0, 1)
    frame_bound = Fraction(len(union_vertices), n - 1)
    projective_lines = len(union_vertices) // 2
    dimension = n - 1
    welch_sq = welch_squared(projective_lines, dimension)
    levenshtein_sq = levenshtein_second_squared(projective_lines, dimension)
    packing_bound_sq = levenshtein_sq or welch_sq

    # Unit-normalized frame operator.  The vertices have squared norm (n-1)/n,
    # so unit normalization multiplies the outer-product sum by n/(n-1).
    raw_operator = frame_operator(union_vertices)
    scaled_operator = [
        [Fraction(n, n - 1) * value for value in row]
        for row in raw_operator
    ]
    expected_operator = [
        [frame_bound * value for value in row]
        for row in expected_projector(n)
    ]
    assert scaled_operator == expected_operator, n

    return {
        "n": n,
        "block_divisors": block_divisors,
        "block_count": len(block_divisors),
        "group_order": len(signs_list),
        "kernel_order": len(kernel),
        "distinct_simplices": len(distinct_simplices),
        "vertices": len(union_vertices),
        "projective_lines": projective_lines,
        "dimension": dimension,
        "frame_bound": frame_bound,
        "abs_values": len(abs_profile),
        "projective_abs_values": len(projective_values),
        "abs_profile": abs_profile,
        "coherence": max(abs_profile) if abs_profile else Fraction(0, 1),
        "projective_coherence": projective_coherence,
        "welch_sq": welch_sq,
        "levenshtein_sq": levenshtein_sq,
        "packing_bound_sq": packing_bound_sq,
        "half_turn": half_turn,
    }


def markdown_report(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Cyclotomic Block-Sign Census",
        "",
        "**Script:** `empirical/census_cyclotomic_block_signs.py`",
        "**Companion note:** `8.parity_dual_simplices.md`",
        "**Status:** all checks passed",
        "",
        "For each `N`, the block-sign group",
        "",
        "```text",
        "B_N = <rho_d : d | N, d > 1>",
        "```",
        "",
        "acts on the regular simplex `V_N`.  The census computes the distinct simplex images and the angle profile of the resulting spectral compound.",
        "",
        "The listed frame bound is for the unit-normalized compound in the `(N-1)`-dimensional zero-sum hyperplane.  Since the compound is centrally symmetric, ordinary coherence is always `1`; the non-antipodal/projective coherence is the useful packing statistic.",
        "",
        "| N | block divisors | B_N order | kernel | distinct simplices | vertices | frame bound | projective angle values | coherence | non-antipodal coherence | abs profile preview |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        coherence = row["coherence"]
        projective_coherence = row["projective_coherence"]
        frame_bound = row["frame_bound"]
        assert isinstance(coherence, Fraction)
        assert isinstance(projective_coherence, Fraction)
        assert isinstance(frame_bound, Fraction)
        lines.append(
            "| "
            f"{row['n']} | "
            f"`{row['block_divisors']}` | "
            f"{row['group_order']} | "
            f"{row['kernel_order']} | "
            f"{row['distinct_simplices']} | "
            f"{row['vertices']} | "
            f"{format_fraction(frame_bound)} | "
            f"{row['projective_abs_values']} | "
            f"{format_fraction(coherence)} | "
            f"{format_fraction(projective_coherence)} | "
            f"`{format_profile(row['abs_profile'])}` |"
        )

    lines.extend(
        [
            "",
            "## Consequences",
            "",
            "1. For odd `N`, the block-sign action has no coordinate half-turn kernel in the tested range, so the number of distinct simplices is `2^(tau(N)-1)`.",
            "2. For even `N`, the half-turn `C_N^(N/2)` is itself a block-sign element and fixes `V_N` as a set.  The number of distinct simplices is therefore `2^(tau(N)-2)`.",
            "3. If `M_N` is the number of distinct simplex images, then the unit-normalized compound has `N M_N` vectors and frame bound `N M_N/(N-1)`.  The script verifies the exact frame operator identity for every tested `N`.",
            "4. Because the all-block sign flip is `-I` on `H_N`, the full spectral compound always contains antipodal partners and has ordinary coherence `1`.  The non-antipodal/projective coherence is the meaningful packing statistic.",
            "5. The full spectral compounds are still exact few-angle objects for small `N`, but the number of angle values grows.  This motivates a Ramanujan-sum formula rather than case-by-case tables.",
            "",
            "## Projective Packing Baseline",
            "",
            "The compound is centrally symmetric, so the packing comparison is made after identifying antipodal pairs.  The table below uses the number of projective lines `vertices/2`.  The bound column is the Welch bound except where the second real projective Levenshtein bound applies.",
            "",
            "| N | dimension | vertices | projective lines | projective coherence | Welch bound | Levenshtein bound | excess over bound |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    baseline_targets = {5, 6, 7, 8, 9, 10, 12}
    for row in rows:
        if row["n"] not in baseline_targets:
            continue
        projective_coherence = row["projective_coherence"]
        welch_sq = row["welch_sq"]
        levenshtein_sq = row["levenshtein_sq"]
        packing_bound_sq = row["packing_bound_sq"]
        assert isinstance(projective_coherence, Fraction)
        assert isinstance(welch_sq, Fraction)
        assert isinstance(packing_bound_sq, Fraction)
        active_excess = float(projective_coherence) - float(packing_bound_sq) ** 0.5
        lines.append(
            "| "
            f"{row['n']} | "
            f"{row['dimension']} | "
            f"{row['vertices']} | "
            f"{row['projective_lines']} | "
            f"{format_fraction(projective_coherence)} | "
            f"{format_sqrt(welch_sq)} | "
            f"{format_sqrt(levenshtein_sq) if levenshtein_sq is not None else '-'} | "
            f"{active_excess:.6f} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    rows = [census_row(n) for n in TARGETS]
    report = markdown_report(rows)
    report_path = Path(__file__).parent / "reports" / "cyclotomic_block_signs.md"
    report_path.write_text(report, encoding="utf-8")

    print("=== Cyclotomic block-sign census ===")
    for row in rows:
        coherence = row["coherence"]
        projective_coherence = row["projective_coherence"]
        assert isinstance(coherence, Fraction)
        assert isinstance(projective_coherence, Fraction)
        print(
            "[ok] "
            f"N={row['n']}: blocks={row['block_divisors']}; "
            f"|B|={row['group_order']}; kernel={row['kernel_order']}; "
            f"simplices={row['distinct_simplices']}; vertices={row['vertices']}; "
            f"frame-bound={format_fraction(row['frame_bound'])}; "
            f"projective-values={row['projective_abs_values']}; "
            f"coherence={format_fraction(coherence)}"
            f"; non-antipodal={format_fraction(projective_coherence)}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
