"""Verify prime-power coordinate stabilizer patterns.

This supports Section 8 of `8.parity_dual_simplices.md`.

The check is deliberately exact and combinatorial:

* coordinate-pair colors are computed from the rational vertex set;
* the colors are checked against the predicted p-adic congruence levels;
* a generating set for the predicted tree automorphism group is checked
  against the full spectral vertex set.
"""

from __future__ import annotations

from math import factorial
from pathlib import Path

from census_cyclotomic_block_polytope import (
    full_spectral_vertices,
    pair_colors,
    permutes_vertex_set,
)


TARGETS = [(8, 2, 3), (9, 3, 2), (16, 2, 4), (25, 5, 2), (27, 3, 3), (32, 2, 5)]


def p_adic_valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        out += 1
        value //= p
    return out


def predicted_pair_key(i: int, j: int, p: int, r: int) -> int:
    valuation = p_adic_valuation(abs(i - j), p)
    if p == 2 and r >= 3:
        return min(valuation, r - 2)
    return valuation


def predicted_order(p: int, r: int) -> int:
    if p == 2 and r == 2:
        return factorial(4)
    if p == 2:
        order = factorial(4) ** (2 ** (r - 2))
        for level in range(r - 2):
            order *= 2 ** (2**level)
        return order

    order = 1
    for level in range(r):
        order *= factorial(p) ** (p**level)
    return order


def predicted_group_name(p: int, r: int) -> str:
    if p == 2 and r == 2:
        return "S_4 (exceptional antipodal-simplex case)"
    if p == 2:
        return f"binary congruence tree with S_4 fibers at level {r - 2}"
    return f"Aut of depth-{r} p-adic congruence tree; iterated S_{p} wreath product"


def swap_digit_permutation(n: int, p: int, level: int, residue: int, digit: int) -> tuple[int, ...]:
    """Swap adjacent child digits inside one congruence node."""

    step = p**level
    modulus = p ** (level + 1)
    out = list(range(n))
    for x in range(n):
        if x % step != residue:
            continue
        current_digit = (x // step) % p
        if current_digit == digit:
            out[x] = x + step
        elif current_digit == digit + 1:
            out[x] = x - step
    return tuple(out)


def swap_positions_permutation(n: int, values: list[int], index: int) -> tuple[int, ...]:
    out = list(range(n))
    out[values[index]], out[values[index + 1]] = out[values[index + 1]], out[values[index]]
    return tuple(out)


def predicted_generators(n: int, p: int, r: int) -> list[tuple[int, ...]]:
    if p == 2 and r == 2:
        return [swap_positions_permutation(n, list(range(n)), i) for i in range(n - 1)]

    generators: list[tuple[int, ...]] = []
    top_tree_level = r - 2 if p == 2 else r - 1
    for level in range(top_tree_level):
        step = p**level
        for residue in range(step):
            for digit in range(p - 1):
                generators.append(swap_digit_permutation(n, p, level, residue, digit))

    leaf_modulus = 2 ** (r - 2) if p == 2 else p ** (r - 1)
    for residue in range(leaf_modulus):
        values = [x for x in range(n) if x % leaf_modulus == residue]
        for index in range(len(values) - 1):
            generators.append(swap_positions_permutation(n, values, index))
    return generators


def verify_pair_colors(n: int, p: int, r: int) -> int:
    vertices = full_spectral_vertices(n)
    colors = pair_colors(n, vertices)
    key_by_color: dict[object, int] = {}
    colors_by_key: dict[int, set[object]] = {}

    for i in range(n):
        for j in range(i + 1, n):
            color = colors[(i, j)]
            key = predicted_pair_key(i, j, p, r)
            key_by_color.setdefault(color, key)
            assert key_by_color[color] == key, (n, i, j, key_by_color[color], key)
            colors_by_key.setdefault(key, set()).add(color)

    assert all(len(values) == 1 for values in colors_by_key.values()), (n, colors_by_key)
    expected_color_count = (r - 1) if p == 2 and r >= 3 else r
    assert len(colors_by_key) == expected_color_count, (n, len(colors_by_key), expected_color_count)
    return len(colors_by_key)


def verify_generators(n: int, p: int, r: int) -> int:
    vertices = full_spectral_vertices(n)
    generators = predicted_generators(n, p, r)
    assert all(permutes_vertex_set(n, vertices, generator) for generator in generators), n
    return len(generators)


def row_for_target(n: int, p: int, r: int) -> dict[str, object]:
    color_count = verify_pair_colors(n, p, r)
    generator_count = verify_generators(n, p, r)
    return {
        "n": n,
        "p": p,
        "r": r,
        "colors": color_count,
        "generators": generator_count,
        "order": predicted_order(p, r),
        "group": predicted_group_name(p, r),
    }


def markdown_report(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Prime-Power Stabilizer Verifier",
        "",
        "**Script:** `empirical/verify_prime_power_stabilizers.py`",
        "**Companion note:** `8.parity_dual_simplices.md`",
        "**Status:** exact pair-color and generator checks passed",
        "",
        "For odd prime powers `N=p^r`, the coordinate-pair colors recover the full p-adic congruence tree.  For powers of two `N=2^r`, `r>=3`, the top two binary layers fuse into four-point fibers; the colors recover congruences only through modulo `2^(r-2)`, and each fiber carries a full `S_4` action.",
        "",
        "| N | p | r | pair-color levels | checked generators | predicted coordinate stabilizer order | group description |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row['n']} | "
            f"{row['p']} | "
            f"{row['r']} | "
            f"{row['colors']} | "
            f"{row['generators']} | "
            f"{row['order']} | "
            f"{row['group']} |"
        )
    lines.extend(
        [
            "",
            "## Consequences",
            "",
            "1. The `N=8` and `N=9` stabilizer rows in the polytope census are the first two prime-power cases of a general p-adic pattern.",
            "2. Odd prime powers have the full rooted p-ary tree automorphism group, equivalently an iterated wreath product with `r` copies of `S_p`.",
            "3. Powers of two are slightly exceptional: the half-turn kernel fuses the last two binary levels, leaving full `S_4` fibers over the residue classes modulo `2^(r-2)`.",
            "4. Mixed composites such as `N=12` are not explained by the prime-power theorem; their stabilizers remain part of the squarefree/mixed-divisor problem.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    rows = [row_for_target(n, p, r) for n, p, r in TARGETS]
    report = markdown_report(rows)
    report_path = Path(__file__).parent / "reports" / "prime_power_stabilizers.md"
    report_path.write_text(report, encoding="utf-8")

    print("=== Prime-power stabilizer verifier ===")
    for row in rows:
        print(
            "[ok] "
            f"N={row['n']}: pair-colors={row['colors']}; "
            f"generators={row['generators']}; "
            f"order={row['order']}; {row['group']}"
        )
    print(f"\nWrote {report_path}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
