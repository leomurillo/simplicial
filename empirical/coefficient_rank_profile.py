"""Coefficient rank-profile probe for CRT Fisher coefficients.

For a two-factor CRT product, the coefficient-rank invariant

    rho_n(h; S, T) = rank_tensor(Q_S C_n(h) Q_T)

is an ordinary matrix rank after vectorizing each local block.  This script
computes that rank exactly over rational numbers for synthetic Fourier
profiles on a product of cyclic character groups.

The default row is C12 ~= C4 x C3.  It is deliberately theory-side: no model
outputs, logits, or empirical centroids are required.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable


GroupElement = tuple[int, ...]
Profile = dict[GroupElement, Fraction]
Pattern = tuple[int, ...]


@dataclass(frozen=True)
class RankRow:
    order: int
    source: Pattern
    target: Pattern
    rank: int
    nonzero_entries: int
    local_row_dimension: int
    local_column_dimension: int


def group_elements(sizes: tuple[int, ...]) -> list[GroupElement]:
    return list(product(*(range(size) for size in sizes)))


def add_group(a: GroupElement, b: GroupElement, sizes: tuple[int, ...]) -> GroupElement:
    return tuple((x + y) % size for x, y, size in zip(a, b, sizes))


def sub_group(a: GroupElement, b: GroupElement, sizes: tuple[int, ...]) -> GroupElement:
    return tuple((x - y) % size for x, y, size in zip(a, b, sizes))


def zero_profile(sizes: tuple[int, ...]) -> Profile:
    return {element: Fraction(0) for element in group_elements(sizes)}


def convolve(left: Profile, right: Profile, sizes: tuple[int, ...]) -> Profile:
    out = zero_profile(sizes)
    elements = group_elements(sizes)
    for x in elements:
        total = Fraction(0)
        for y in elements:
            total += left[y] * right[sub_group(x, y, sizes)]
        out[x] = total
    return out


def powers(profile: Profile, max_order: int, sizes: tuple[int, ...]) -> dict[int, Profile]:
    out = {1: profile}
    for order in range(2, max_order + 1):
        out[order] = convolve(out[order - 1], profile, sizes)
    return out


def tensor_profile(vectors: list[list[Fraction]], sizes: tuple[int, ...]) -> Profile:
    out = zero_profile(sizes)
    for element in group_elements(sizes):
        value = Fraction(1)
        for factor_index, coordinate in enumerate(element):
            value *= vectors[factor_index][coordinate]
        out[element] = value
    return out


def add_profiles(*profiles: Profile) -> Profile:
    if not profiles:
        raise ValueError("at least one profile is required")
    keys = profiles[0].keys()
    return {key: sum(profile[key] for profile in profiles) for key in keys}


def sparse_tensor(
    sizes: tuple[int, ...],
    first: list[Fraction],
    second: list[Fraction],
) -> Profile:
    if len(sizes) != 2:
        raise ValueError("sparse_tensor examples are implemented for two factors")
    return tensor_profile([first, second], sizes)


def example_profiles(sizes: tuple[int, ...]) -> dict[str, Profile]:
    if sizes != (4, 3):
        raise ValueError("built-in examples currently target C4 x C3")

    e4 = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    e3 = [Fraction(1), Fraction(0), Fraction(0)]
    phi = [Fraction(0), Fraction(1), Fraction(-1), Fraction(2)]
    psi = [Fraction(1), Fraction(2), Fraction(-1)]
    phi_a = [Fraction(0), Fraction(1), Fraction(0), Fraction(-1)]
    phi_b = [Fraction(0), Fraction(0), Fraction(2), Fraction(1)]
    psi_a = [Fraction(0), Fraction(1), Fraction(-1)]
    psi_b = [Fraction(0), Fraction(2), Fraction(1)]

    local_sum = add_profiles(
        sparse_tensor(sizes, phi_a, e3),
        sparse_tensor(sizes, e4, psi_a),
    )
    two_summand = add_profiles(
        sparse_tensor(sizes, phi_a, psi_a),
        sparse_tensor(sizes, phi_b, psi_b),
    )
    return {
        "pure_tensor": sparse_tensor(sizes, phi, psi),
        "local_additive_sum": local_sum,
        "two_summand_mixed": two_summand,
    }


def support_patterns(factor_count: int) -> list[Pattern]:
    patterns = []
    for mask in range(1, 1 << factor_count):
        patterns.append(tuple(index for index in range(factor_count) if mask & (1 << index)))
    return patterns


def local_indices(size: int, active: bool) -> list[int]:
    if active:
        return list(range(1, size))
    return [0]


def local_block_basis(size: int, source_active: bool, target_active: bool) -> list[tuple[int, int]]:
    rows = local_indices(size, target_active)
    cols = local_indices(size, source_active)
    return list(product(rows, cols))


def rank_fraction_matrix(matrix: list[list[Fraction]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    work = [row[:] for row in matrix]
    row_count = len(work)
    col_count = len(work[0])
    rank = 0
    for col in range(col_count):
        pivot = None
        for row in range(rank, row_count):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][col]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(row_count):
            if row != rank and work[row][col] != 0:
                factor = work[row][col]
                work[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def block_flatten_matrix(
    coefficient: Profile,
    sizes: tuple[int, int],
    source: Pattern,
    target: Pattern,
) -> list[list[Fraction]]:
    local_0 = local_block_basis(
        sizes[0],
        source_active=0 in source,
        target_active=0 in target,
    )
    local_1 = local_block_basis(
        sizes[1],
        source_active=1 in source,
        target_active=1 in target,
    )
    matrix: list[list[Fraction]] = []
    for row_0, col_0 in local_0:
        row_values = []
        for row_1, col_1 in local_1:
            eta = ((row_0 - col_0) % sizes[0], (row_1 - col_1) % sizes[1])
            row_values.append(coefficient[eta])
        matrix.append(row_values)
    return matrix


def rank_profile(
    profile: Profile,
    sizes: tuple[int, int],
    max_order: int,
) -> list[RankRow]:
    coefficient_powers = powers(profile, max_order, sizes)
    patterns = support_patterns(len(sizes))
    rows = []
    for order in range(1, max_order + 1):
        coefficient = coefficient_powers[order]
        for source in patterns:
            for target in patterns:
                matrix = block_flatten_matrix(coefficient, sizes, source, target)
                nonzero = sum(1 for row in matrix for value in row if value)
                rows.append(
                    RankRow(
                        order=order,
                        source=source,
                        target=target,
                        rank=rank_fraction_matrix(matrix),
                        nonzero_entries=nonzero,
                        local_row_dimension=len(matrix),
                        local_column_dimension=len(matrix[0]) if matrix else 0,
                    )
                )
    return rows


def pattern_text(pattern: Pattern) -> str:
    if not pattern:
        return "{}"
    return "{" + ",".join(str(index + 1) for index in pattern) + "}"


def fraction_json(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


def profile_support_summary(profile: Profile) -> dict[str, int]:
    counts: dict[str, int] = {}
    for element, value in profile.items():
        if not value:
            continue
        pattern = tuple(index for index, coordinate in enumerate(element) if coordinate != 0)
        counts[pattern_text(pattern)] = counts.get(pattern_text(pattern), 0) + 1
    return dict(sorted(counts.items()))


def rank_summary(rows: list[RankRow]) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    for row in rows:
        order_key = str(row.order)
        rank_key = str(row.rank)
        out.setdefault(order_key, {})
        out[order_key][rank_key] = out[order_key].get(rank_key, 0) + 1
    return out


def max_rank_rows(rows: list[RankRow]) -> list[RankRow]:
    by_order: dict[int, int] = {}
    for row in rows:
        by_order[row.order] = max(by_order.get(row.order, 0), row.rank)
    return [row for row in rows if row.rank == by_order[row.order] and row.rank > 0]


def rows_json(rows: Iterable[RankRow]) -> list[dict[str, object]]:
    return [
        {
            "order": row.order,
            "source": pattern_text(row.source),
            "target": pattern_text(row.target),
            "rank": row.rank,
            "nonzero_entries": row.nonzero_entries,
            "local_row_dimension": row.local_row_dimension,
            "local_column_dimension": row.local_column_dimension,
        }
        for row in rows
    ]


def render_report(payload: dict[str, object]) -> str:
    lines = [
        "# Coefficient Rank-Profile Probe",
        "",
        f"- CRT row: `{payload['crt_row']}`",
        f"- max order: `{payload['max_order']}`",
        "",
        "The rank is the two-factor tensor rank of `Q_S C_n(h) Q_T`, computed as an exact rational matrix rank after vectorizing each local source/target block.",
        "",
    ]
    for name, data in payload["examples"].items():  # type: ignore[union-attr]
        lines += [
            f"## {name}",
            "",
            f"- first-order support by CRT pattern: `{data['support_patterns']}`",
            f"- rank-counts by order: `{data['rank_counts_by_order']}`",
            "",
            "| order | source | target | rank | nonzero entries | local shape |",
            "|---:|---|---|---:|---:|---|",
        ]
        for row in data["max_rank_rows"]:  # type: ignore[index]
            lines.append(
                f"| {row['order']} | {row['source']} | {row['target']} | "
                f"{row['rank']} | {row['nonzero_entries']} | "
                f"{row['local_row_dimension']}x{row['local_column_dimension']} |"
            )
        lines.append("")

    lines += [
        "## Interpretation",
        "",
        "- `pure_tensor` is the sanity check: every occupied block has tensor rank 1 through the tested orders.",
        "- `local_additive_sum` has first-order support spread across the two CRT factors; higher orders show where additive cross-factor superposition creates rank greater than 1 inside a support block.",
        "- `two_summand_mixed` is the impurity stress test: rank greater than 1 appears immediately in mixed support blocks and persists under convolution powers.",
        "",
        "This is the paper-facing reason to keep `rho_n(h;S,T)`: scalar conductor support says which CRT corners are occupied, while the rank profile says whether the coefficient inside that corner factors over local components.",
        "",
    ]
    return "\n".join(lines)


def build_payload(sizes: tuple[int, int], max_order: int) -> dict[str, object]:
    examples = {}
    for name, profile in example_profiles(sizes).items():
        rows = rank_profile(profile, sizes, max_order)
        examples[name] = {
            "support_patterns": profile_support_summary(profile),
            "rank_counts_by_order": rank_summary(rows),
            "max_rank_rows": rows_json(max_rank_rows(rows)),
            "rows": rows_json(rows),
            "profile": {
                str(element): fraction_json(value)
                for element, value in profile.items()
                if value
            },
        }
    return {
        "crt_row": " x ".join(f"C{size}" for size in sizes),
        "factor_sizes": list(sizes),
        "max_order": max_order,
        "examples": examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factor-sizes", type=int, nargs=2, default=(4, 3))
    parser.add_argument("--max-order", type=int, default=4)
    parser.add_argument("--report", type=Path, default=Path("empirical/reports/coefficient_rank_profile_c4_c3.md"))
    parser.add_argument("--json", type=Path, default=Path("empirical/reports/coefficient_rank_profile_c4_c3.json"))
    args = parser.parse_args()

    sizes = tuple(args.factor_sizes)
    payload = build_payload(sizes, args.max_order)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(render_report(payload), encoding="utf-8")
    args.json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(render_report(payload))
    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
