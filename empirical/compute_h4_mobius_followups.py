"""Follow-up Mobius witness probes for Paper 11 arity 4.

This script writes the two follow-up reports requested by the lead:

* a TWWW mixed-family witness report;
* a TTWW size-24 witness report.

The requested "TWWW size-12" class is empty under the measured input-side lift,
so the TWWW report uses the minimal available TWWW class, which has arity-2
commutator orbit size 24.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from compute_f4_u2_ext_ch import (
    ACTIONS,
    ZERO,
    add_label,
    coefficient_by_key,
    compute_witnesses,
    label_name,
    orbit_decomposition,
    tangent_compatible,
)
from compute_h4_f4_u2 import S4, conductor_family, h4_cells, transform_cell
from compute_h4_mobius_witness import (
    NC_PARTITIONS,
    PARTITIONS,
    add_many,
    cumulant,
    fraction_text,
    is_crossing,
    nc_mobius,
    partition_operator,
    pi_mobius,
)


Label = tuple[int, int]
Partition = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class LiftRecord:
    orbit_id: int
    orbit_size: int
    coefficient: Fraction
    witness: tuple[Label, Label, Label, Label, Label, Label]
    lift_name: str
    cell: tuple[Label, Label, Label, Label]
    cell_names: tuple[str, str, str, str]
    h4_orbit: int
    h4_family: str
    h4_orbit_size: int
    pi_value: Fraction
    nc_value: Fraction


def h4_orbit_map() -> tuple[dict[tuple[Label, Label, Label, Label], int], list[dict[str, object]]]:
    remaining = set(h4_cells(distinct=False))
    cell_to_orbit: dict[tuple[Label, Label, Label, Label], int] = {}
    rows: list[dict[str, object]] = []
    while remaining:
        seed = min(remaining)
        orbit = {
            transform_cell(seed, action, permutation)
            for action in ACTIONS
            for permutation in S4
        }
        orbit_id = len(rows)
        for cell in orbit:
            cell_to_orbit[cell] = orbit_id
        rows.append(
            {
                "id": orbit_id,
                "seed": seed,
                "size": len(orbit),
                "family": conductor_family(seed),
            }
        )
        remaining -= orbit
    return cell_to_orbit, rows


def lifted_records() -> list[LiftRecord]:
    cell_to_orbit, h4_rows = h4_orbit_map()
    commutator = tangent_compatible(compute_witnesses("commutator"))
    commutator_coeffs = coefficient_by_key(commutator)
    commutator_orbits = orbit_decomposition(commutator)
    records: list[LiftRecord] = []

    for orbit_id, orbit in enumerate(commutator_orbits):
        seed = next(iter(orbit["keys"]))
        coefficient = commutator_coeffs[seed]
        lift_candidates = [
            ("alpha-in", (0, 1, 2, 4), ("tau", "omega", "alpha", "iota")),
            ("beta-in", (0, 1, 3, 4), ("tau", "omega", "beta", "iota")),
        ]
        for lift_name, indices, cell_names in lift_candidates:
            cell = tuple(seed[index] for index in indices)
            if add_many(cell) != ZERO:
                continue
            h4_orbit = cell_to_orbit[cell]
            h4_row = h4_rows[h4_orbit]
            entry = (seed[4], seed[4])
            pi_value = cumulant(cell, PARTITIONS, pi_mobius).get(entry, Fraction(0))
            nc_value = cumulant(cell, NC_PARTITIONS, nc_mobius).get(entry, Fraction(0))
            records.append(
                LiftRecord(
                    orbit_id=orbit_id,
                    orbit_size=int(orbit["size"]),
                    coefficient=coefficient,
                    witness=seed,
                    lift_name=lift_name,
                    cell=cell,
                    cell_names=cell_names,
                    h4_orbit=h4_orbit,
                    h4_family=str(h4_row["family"]),
                    h4_orbit_size=int(h4_row["size"]),
                    pi_value=pi_value,
                    nc_value=nc_value,
                )
            )
            break
    return records


def partition_text(partition: Partition, names: tuple[str, str, str, str]) -> str:
    return " | ".join(
        "{" + ",".join(names[index] for index in block) + "}"
        for block in partition
    )


def partition_rows(record: LiftRecord) -> list[str]:
    entry = (record.witness[4], record.witness[4])
    lines = [
        "| partition | crossing? | base entry | mu_Pi | Pi contribution | mu_NC | NC contribution |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for partition in sorted(PARTITIONS, key=lambda item: (len(item), item)):
        base = partition_operator(record.cell, partition).get(entry, Fraction(0))
        mu_pi = pi_mobius(partition)
        mu_nc = nc_mobius(partition)
        lines.append(
            "| "
            + " | ".join(
                [
                    "`" + partition_text(partition, record.cell_names) + "`",
                    "yes" if is_crossing(partition) else "no",
                    fraction_text(base),
                    fraction_text(mu_pi),
                    fraction_text(base * mu_pi),
                    fraction_text(mu_nc),
                    fraction_text(None if mu_nc is None else base * mu_nc),
                ]
            )
            + " |"
        )
    return lines


def counter_text(counter: Counter[object]) -> str:
    return "{" + ", ".join(f"{key}: {value}" for key, value in sorted(counter.items())) + "}"


def summary_for(records: list[LiftRecord], family: str, orbit_size: int) -> list[str]:
    subset = [
        record
        for record in records
        if record.h4_family == family and record.orbit_size == orbit_size
    ]
    return [
        f"- records in class {family}, arity-2 orbit size {orbit_size}: {len(subset)}",
        f"- inherited coefficient distribution: {counter_text(Counter(record.coefficient for record in subset))}",
        f"- Pi_4 value distribution: {counter_text(Counter(record.pi_value for record in subset))}",
        f"- NC_4 value distribution: {counter_text(Counter(record.nc_value for record in subset))}",
        f"- Pi_4 matches inherited coefficient: {sum(record.pi_value == record.coefficient for record in subset)} / {len(subset)}",
        f"- NC_4 matches inherited coefficient: {sum(record.nc_value == record.coefficient for record in subset)} / {len(subset)}",
    ]


def report_for(
    title: str,
    record: LiftRecord,
    records: list[LiftRecord],
    extra_note: list[str],
) -> str:
    entry = (record.witness[4], record.witness[4])
    pi_operator = cumulant(record.cell, PARTITIONS, pi_mobius)
    nc_operator = cumulant(record.cell, NC_PARTITIONS, nc_mobius)

    lines = [
        f"# {title}",
        "",
        "This is a follow-up to `empirical/reports/h4_mobius_witness.md`.",
        "It compares classical Pi_4 Mobius contraction with NC_4 Mobius",
        "contraction on one additional lifted commutator cell.",
        "",
    ]
    lines += extra_note
    lines += [
        "",
        "## Chosen witness",
        "",
        "```text",
        "witness = (tau, omega, alpha, beta, input, output)",
        "        = (" + ", ".join(label_name(label) for label in record.witness) + ")",
        f"commutator coefficient = {fraction_text(record.coefficient)}",
        f"commutator orbit size = {record.orbit_size}",
        "lift = " + record.lift_name,
        "cell = (" + ", ".join(label_name(label) for label in record.cell) + ")",
        "sum(cell) = " + label_name(add_many(record.cell)),
        f"H4 orbit = {record.h4_orbit}, family = {record.h4_family}, orbit size = {record.h4_orbit_size}",
        "tested entry = "
        + f"{label_name(entry[0])} <- {label_name(entry[1])}",
        "```",
        "",
        "## Result",
        "",
        "| candidate | partitions | value at input diagonal | matches inherited coefficient? |",
        "|---|---:|---:|---|",
        f"| Pi_4 classical Mobius | {len(PARTITIONS)} | {fraction_text(record.pi_value)} | {record.pi_value == record.coefficient} |",
        f"| NC_4 non-crossing Mobius | {len(NC_PARTITIONS)} | {fraction_text(record.nc_value)} | {record.nc_value == record.coefficient} |",
        "",
        "Full cumulant operator distributions:",
        "",
        f"- Pi_4 nonzero entries: {len(pi_operator)}, distribution {counter_text(Counter(pi_operator.values()))}",
        f"- NC_4 nonzero entries: {len(nc_operator)}, distribution {counter_text(Counter(nc_operator.values()))}",
        "",
        "## Class scan",
        "",
    ]
    lines += summary_for(records, record.h4_family, record.orbit_size)
    lines += [
        "",
        "## Partition contribution table",
        "",
    ]
    lines += partition_rows(record)
    lines += [""]
    return "\n".join(lines)


def main() -> None:
    records = lifted_records()
    counts = Counter((record.h4_family, record.orbit_size) for record in records)

    twww_records = [
        record
        for record in records
        if record.h4_family == "TWWW" and record.orbit_size == 24 and record.coefficient == 1
    ]
    if not twww_records:
        raise ValueError("no TWWW size-24 positive witness found")
    twww = twww_records[0]

    ttww_size24_records = [
        record
        for record in records
        if (
            record.h4_family == "TTWW"
            and record.orbit_size == 24
            and record.coefficient == -1
            and record.nc_value == record.coefficient
            and record.pi_value != record.coefficient
        )
    ]
    if not ttww_size24_records:
        raise ValueError("no TTWW size-24 NC-only witness found")
    ttww_size24 = ttww_size24_records[0]

    reports_dir = Path(__file__).with_name("reports")
    twww_text = report_for(
        "H4 Mobius Follow-up: TWWW Witness",
        twww,
        records,
        [
            "The requested TWWW size-12 class is empty under the measured",
            "input-side lift:",
            "",
            f"- TWWW size-12 records: {counts.get(('TWWW', 12), 0)}",
            f"- TWWW size-24 records: {counts.get(('TWWW', 24), 0)}",
            "",
            "This report therefore uses a minimal TWWW witness, which has",
            "arity-2 commutator orbit size 24.",
        ],
    )
    size24_text = report_for(
        "H4 Mobius Follow-up: TTWW Size-24 Witness",
        ttww_size24,
        records,
        [
            "This report uses a TTWW witness from an arity-2 commutator orbit",
            "of size 24.  It is chosen so that NC_4 matches the inherited",
            "commutator coefficient while Pi_4 does not.",
        ],
    )

    (reports_dir / "h4_mobius_witness_twww.md").write_text(twww_text, encoding="utf-8")
    (reports_dir / "h4_mobius_witness_size24.md").write_text(size24_text, encoding="utf-8")
    print(twww_text)
    print(f"\nWrote {reports_dir / 'h4_mobius_witness_twww.md'}\n")
    print(size24_text)
    print(f"\nWrote {reports_dir / 'h4_mobius_witness_size24.md'}")


if __name__ == "__main__":
    main()
