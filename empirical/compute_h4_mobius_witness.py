"""Single-cell Mobius probe for the arity-4 curvature lift.

This is a small witness computation for the Option A-prime question in the
Paper 11 leader report.  It compares two candidate lower-contraction
cumulants for one size-12 arity-2 commutator orbit:

* classical partitions Pi_4;
* non-crossing partitions NC_4.

The chosen witness is the size-12 commutator key

    (tau, omega, alpha, beta, input, output) = (u, 1, u, 1, u, u),

whose commutator coefficient is -1.  Its closed input-side beta lift is the
arity-4 cell

    (tau, omega, beta, input) = (u, 1, 1, u).

The scalar tested is the diagonal entry at the lifted input line u.  This is
not a full R^(4) coefficient table; it is the first coefficient-point probe of
the lower-contraction formula.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path
from fractions import Fraction

from compute_f4_u2_ext_ch import (
    ACTIONS,
    NONTRIVIAL,
    ZERO,
    add_label,
    coefficient_by_key,
    compute_witnesses,
    conductor,
    label_name,
    matrix_add,
    matrix_mul,
    matrix_scale,
    orbit_decomposition,
    tangent_compatible,
)
from compute_h4_f4_u2 import S4, conductor_family, h4_cells, transform_cell


Label = tuple[int, int]
Matrix = dict[tuple[Label, Label], Fraction]
Partition = tuple[tuple[int, ...], ...]

U: Label = (0, 1)
ONE: Label = (1, 0)
WITNESS: tuple[Label, Label, Label, Label, Label, Label] = (U, ONE, U, ONE, U, U)
CELL_NAMES = ("tau", "omega", "beta", "iota")
CELL: tuple[Label, Label, Label, Label] = (U, ONE, ONE, U)
ENTRY: tuple[Label, Label] = (U, U)
TOP: Partition = ((0, 1, 2, 3),)


def add_many(labels: tuple[Label, ...]) -> Label:
    out = ZERO
    for label in labels:
        out = add_label(out, label)
    return out


def k_centroid(label: Label) -> Matrix:
    """Centroid augmentation-corner shift K(label)."""

    out: Matrix = {}
    for col in NONTRIVIAL:
        row = add_label(label, col)
        if row != ZERO:
            out[(row, col)] = Fraction(1)
    return out


def all_partitions(n: int) -> list[Partition]:
    partitions: list[Partition] = []

    def rec(index: int, blocks: list[list[int]]) -> None:
        if index == n:
            partitions.append(tuple(tuple(block) for block in blocks))
            return
        for block in blocks:
            block.append(index)
            rec(index + 1, blocks)
            block.pop()
        blocks.append([index])
        rec(index + 1, blocks)
        blocks.pop()

    rec(0, [])
    return partitions


def is_crossing(partition: Partition) -> bool:
    blocks = [set(block) for block in partition]
    for left_index in range(len(blocks)):
        for right_index in range(left_index + 1, len(blocks)):
            left = sorted(blocks[left_index])
            right = sorted(blocks[right_index])
            for a, c in combinations(left, 2):
                for b, d in combinations(right, 2):
                    if a < b < c < d or b < a < d < c:
                        return True
    return False


PARTITIONS = all_partitions(4)
NC_PARTITIONS = [partition for partition in PARTITIONS if not is_crossing(partition)]


def refines(left: Partition, right: Partition) -> bool:
    return all(
        any(set(block).issubset(set(target)) for target in right)
        for block in left
    )


def pi_mobius(partition: Partition) -> Fraction:
    block_count = len(partition)
    return Fraction(((-1) ** (block_count - 1)) * factorial(block_count - 1))


@lru_cache(maxsize=None)
def nc_mobius_by_index(left_index: int, right_index: int) -> int:
    left = NC_PARTITIONS[left_index]
    right = NC_PARTITIONS[right_index]
    if left == right:
        return 1
    total = 0
    for mid_index, middle in enumerate(NC_PARTITIONS):
        if mid_index == right_index:
            continue
        if refines(left, middle) and refines(middle, right):
            total += nc_mobius_by_index(left_index, mid_index)
    return -total


def nc_mobius(partition: Partition) -> Fraction | None:
    if partition not in NC_PARTITIONS:
        return None
    return Fraction(nc_mobius_by_index(NC_PARTITIONS.index(partition), NC_PARTITIONS.index(TOP)))


def partition_operator(cell: tuple[Label, Label, Label, Label], partition: Partition) -> Matrix:
    ordered_blocks = sorted(partition, key=lambda block: min(block))
    out: Matrix | None = None
    for block in ordered_blocks:
        block_label = add_many(tuple(cell[index] for index in block))
        block_operator = k_centroid(block_label)
        out = block_operator if out is None else matrix_mul(out, block_operator)
    if out is None:
        raise ValueError("empty partition")
    return out


def cumulant(
    cell: tuple[Label, Label, Label, Label],
    partitions: list[Partition],
    mobius,
) -> Matrix:
    out: Matrix = {}
    for partition in partitions:
        coefficient = mobius(partition)
        if coefficient is None:
            continue
        out = matrix_add(out, matrix_scale(partition_operator(cell, partition), coefficient))
    return out


def partition_text(partition: Partition) -> str:
    return " | ".join(
        "{" + ",".join(CELL_NAMES[index] for index in block) + "}"
        for block in partition
    )


def h4_orbit_for_cell(cell: tuple[Label, Label, Label, Label]) -> tuple[int, int, str]:
    remaining = set(h4_cells(distinct=False))
    orbit_id = 0
    while remaining:
        seed = min(remaining)
        orbit = {
            transform_cell(seed, action, permutation)
            for action in ACTIONS
            for permutation in S4
        }
        if cell in orbit:
            return orbit_id, len(orbit), conductor_family(seed)
        remaining -= orbit
        orbit_id += 1
    raise ValueError("cell not found in H4 skeleton")


def witness_orbit_size_and_coefficient() -> tuple[int, Fraction]:
    commutator = tangent_compatible(compute_witnesses("commutator"))
    coeffs = coefficient_by_key(commutator)
    if WITNESS not in coeffs:
        raise ValueError("chosen witness is not in the commutator support")
    for orbit in orbit_decomposition(commutator):
        if WITNESS in orbit["keys"]:
            return int(orbit["size"]), coeffs[WITNESS]
    raise ValueError("chosen witness orbit not found")


def contribution_rows() -> list[dict[str, object]]:
    rows = []
    for partition in sorted(PARTITIONS, key=lambda item: (len(item), item)):
        base = partition_operator(CELL, partition).get(ENTRY, Fraction(0))
        mu_pi = pi_mobius(partition)
        mu_nc = nc_mobius(partition)
        rows.append(
            {
                "partition": partition_text(partition),
                "crossing": is_crossing(partition),
                "base": base,
                "mu_pi": mu_pi,
                "pi_contribution": base * mu_pi,
                "mu_nc": mu_nc,
                "nc_contribution": None if mu_nc is None else base * mu_nc,
            }
        )
    return rows


def fraction_text(value: Fraction | None) -> str:
    if value is None:
        return "-"
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def counter_text(counter: Counter[Fraction]) -> str:
    return "{" + ", ".join(
        f"{fraction_text(value)}: {count}"
        for value, count in sorted(counter.items())
    ) + "}"


def report() -> str:
    orbit_size, measured_commutator = witness_orbit_size_and_coefficient()
    h4_orbit_id, h4_orbit_size, h4_family = h4_orbit_for_cell(CELL)
    pi_value = cumulant(CELL, PARTITIONS, pi_mobius).get(ENTRY, Fraction(0))
    nc_value = cumulant(CELL, NC_PARTITIONS, nc_mobius).get(ENTRY, Fraction(0))
    pi_operator = cumulant(CELL, PARTITIONS, pi_mobius)
    nc_operator = cumulant(CELL, NC_PARTITIONS, nc_mobius)

    lines = [
        "# H4 Mobius Witness Probe",
        "",
        "This is a one-cell test for the arity-4 lower-contraction formula in",
        "Paper 11.  It compares classical partition Mobius inversion on Pi_4",
        "with non-crossing Mobius inversion on NC_4.",
        "",
        "## Chosen size-12 commutator witness",
        "",
        "```text",
        "witness = (tau, omega, alpha, beta, input, output)",
        "        = (" + ", ".join(label_name(label) for label in WITNESS) + ")",
        f"commutator coefficient = {fraction_text(measured_commutator)}",
        f"commutator orbit size = {orbit_size}",
        "```",
        "",
        "The closed input-side beta lift is",
        "",
        "```text",
        "cell = (tau, omega, beta, input)",
        "     = (" + ", ".join(label_name(label) for label in CELL) + ")",
        "sum(cell) = " + label_name(add_many(CELL)),
        f"H4 orbit = {h4_orbit_id}, family = {h4_family}, orbit size = {h4_orbit_size}",
        "tested matrix entry = input <- input = "
        + f"{label_name(ENTRY[0])} <- {label_name(ENTRY[1])}",
        "```",
        "",
        "The inherited arity-2 commutator coefficient is used as the provisional",
        "single-cell target because the current codebase has no independent",
        "coefficient-level implementation of R^(4).",
        "",
        "## Result",
        "",
        "| candidate | partitions | value at input diagonal | matches inherited coefficient? |",
        "|---|---:|---:|---|",
        f"| Pi_4 classical Mobius | {len(PARTITIONS)} | {fraction_text(pi_value)} | {pi_value == measured_commutator} |",
        f"| NC_4 non-crossing Mobius | {len(NC_PARTITIONS)} | {fraction_text(nc_value)} | {nc_value == measured_commutator} |",
        "",
        "On this witness, NC_4 matches the inherited commutator coefficient and",
        "Pi_4 overshoots by the single crossing partition.",
        "",
        "The full cumulant operators are sparse:",
        "",
        f"- Pi_4 nonzero entries: {len(pi_operator)}, coefficient distribution {counter_text(Counter(pi_operator.values()))}",
        f"- NC_4 nonzero entries: {len(nc_operator)}, coefficient distribution {counter_text(Counter(nc_operator.values()))}",
        "",
        "## Partition contribution table",
        "",
        "| partition | crossing? | base entry | mu_Pi | Pi contribution | mu_NC | NC contribution |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]

    for row in contribution_rows():
        lines.append(
            "| "
            + " | ".join(
                [
                    "`" + str(row["partition"]) + "`",
                    "yes" if row["crossing"] else "no",
                    fraction_text(row["base"]),
                    fraction_text(row["mu_pi"]),
                    fraction_text(row["pi_contribution"]),
                    fraction_text(row["mu_nc"]),
                    fraction_text(row["nc_contribution"]),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "The crossing partition",
        "",
        "```text",
        "{tau,beta} | {omega,iota}",
        "```",
        "",
        "has base entry 1 and classical contribution -1.  It is absent from",
        "NC_4.  Removing exactly this contribution changes the value from -2",
        "to -1.",
        "",
        "## Interpretation",
        "",
        "For this size-12 witness, the non-crossing Mobius contraction is the",
        "candidate compatible with the inherited arity-2 curvature coefficient.",
        "This is not yet a proof of Theorem 9.3's coefficient formula, but it is",
        "strong evidence that Option A-prime should be written with NC_4 lower",
        "contractions rather than all of Pi_4.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    text = report()
    report_path = Path(__file__).with_name("reports") / "h4_mobius_witness.md"
    report_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nWrote {report_path}")


if __name__ == "__main__":
    main()
