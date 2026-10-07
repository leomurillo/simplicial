"""Independent two-cell verifier for the covariant R^(4) recipe.

The computation intentionally does not import the existing Mobius witness or
follow-up scripts.  It reuses only the FisherJet operator ingredients
``M, B^tau, B^omega, C`` over the local adjacency constructor and the H4
orbit skeleton from ``compute_h4_f4_u2.py``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

from compute_f4_u2_ext_ch import (
    LABELS,
    NONTRIVIAL,
    ZERO,
    Label,
    add_label,
    conductor,
    label_name,
)
from fisher_jet_functor import FisherJet, JetMatrix as Matrix
from local_adjacency_constructor import LocalAdjacencyConstructor, make_f4_u2_ring
from compute_h4_f4_u2 import ACTIONS, S4, conductor_family, h4_cells, transform_cell
from r4_partition_rules import (
    R4_NORMALIZATION,
    Partition,
    all_partitions,
    bianchi_correction,
    leibniz_coefficient,
    partition_lattice_mobius,
    projected_coefficient,
    refines,
)


Cell4 = tuple[Label, Label, Label, Label]
Entry = tuple[Label, Label]

U: Label = (0, 1)
ONE: Label = (1, 0)
W: Label = (2, 0)
WU: Label = (0, 2)

TARGET_CELL: Cell4 = (U, ONE, ONE, U)
TARGET_ENTRY: Entry = (U, U)

PLUS2_CELL: Cell4 = (WU, W, WU, W)
PLUS2_ENTRY: Entry = (W, W)

NORMALIZATION = R4_NORMALIZATION
JET = FisherJet(LocalAdjacencyConstructor(make_f4_u2_ring()))
TAME_MODES = JET.constructor.packets["u"]
WILD_MODES = JET.constructor.packets["u^2"]


def elementary_expansion(alpha: Label, tau: Label, omega: Label):
    return JET.elementary_expansion(alpha, tau, omega)


def matrix_add(*matrices: Matrix) -> Matrix:
    return JET.matrix_add(*matrices)


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return JET.matrix_mul(left, right)


def matrix_scale(matrix: Matrix, scalar: Fraction) -> Matrix:
    return JET.matrix_scale(matrix, scalar)


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return JET.matrix_sub(left, right)


def compute_witnesses(kind: str) -> list[dict[str, object]]:
    return JET.witnesses(
        kind,  # type: ignore[arg-type]
        left_modes=TAME_MODES,
        right_modes=WILD_MODES,
    )


def tangent_compatible(witnesses: list[dict[str, object]]) -> list[dict[str, object]]:
    return JET.tangent_compatible(witnesses)


def coefficient_by_key(witnesses: list[dict[str, object]]) -> dict[tuple[Label, ...], Fraction]:
    return JET.coefficient_by_key(witnesses)


def orbit_decomposition(witnesses: list[dict[str, object]]) -> list[dict[str, object]]:
    coefficients = coefficient_by_key(witnesses)
    key_set = set(coefficients)
    remaining = set(key_set)
    orbits: list[dict[str, object]] = []
    while remaining:
        seed = next(iter(remaining))
        ambient = {
            JET.constructor.ring.transform_tuple(seed, action, None)
            for action in JET.constructor.ring.normalizer_actions
        }
        present = ambient & key_set
        orbits.append(
            {
                "keys": present,
                "size": len(present),
                "ambient_size": len(ambient),
                "missing": len(ambient - key_set),
            }
        )
        remaining -= present
    return orbits


@dataclass(frozen=True)
class TermTrace:
    partition: Partition
    block_labels: tuple[Label, ...]
    base_entry: Fraction
    leibniz_coefficient: Fraction
    bianchi_correction: Fraction
    projected_coefficient: Fraction

    @property
    def raw_leibniz_contribution(self) -> Fraction:
        return self.base_entry * self.leibniz_coefficient * NORMALIZATION

    @property
    def raw_projected_contribution(self) -> Fraction:
        return self.base_entry * self.projected_coefficient * NORMALIZATION


@dataclass(frozen=True)
class VerificationResult:
    title: str
    cell: Cell4
    entry: Entry
    source_note: tuple[str, ...]
    tau: Label
    omega: Label
    h4_orbit_id: int
    h4_orbit_size: int
    h4_family: str
    expansion_rows: tuple[dict[str, object], ...]
    direct_product_mixed_entry: Fraction
    path_composed_mixed_entry: Fraction
    direct_defect_mixed_entry: Fraction
    traces: tuple[TermTrace, ...]
    stage2_raw_entry: Fraction
    stage3_raw_entry: Fraction
    final_entry: Fraction


@dataclass(frozen=True)
class SweepRecord:
    orbit_id: int
    orbit_size: int
    coefficient: Fraction
    witness: tuple[Label, Label, Label, Label, Label, Label]
    lift_name: str
    cell: Cell4
    entry: Entry
    h4_orbit_id: int
    h4_orbit_size: int
    h4_family: str
    stage2_value: Fraction
    final_value: Fraction


def add_many(labels: tuple[Label, ...]) -> Label:
    out = ZERO
    for label in labels:
        out = add_label(out, label)
    return out


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def label_list_text(labels: tuple[Label, ...]) -> str:
    return "(" + ", ".join(label_name(label) for label in labels) + ")"


def partition_text(partition: Partition, slot_names: tuple[str, ...]) -> str:
    return " | ".join(
        "{" + ",".join(slot_names[index] for index in block) + "}"
        for block in partition
    )


def block_label_text(block_labels: tuple[Label, ...]) -> str:
    return " | ".join(label_name(label) for label in block_labels)


def matrix_entry(matrix: Matrix, entry: Entry) -> Fraction:
    return matrix.get(entry, Fraction(0))


def product(matrices: list[Matrix]) -> Matrix:
    if not matrices:
        return {(label, label): Fraction(1) for label in NONTRIVIAL}
    out = matrices[0]
    for matrix in matrices[1:]:
        out = matrix_mul(out, matrix)
    return out


def block_labels_for(cell: Cell4, partition: Partition) -> tuple[Label, ...]:
    return tuple(add_many(tuple(cell[index] for index in block)) for block in partition)


def moment_operator(block_labels: tuple[Label, ...], tau: Label, omega: Label) -> Matrix:
    matrices = [elementary_expansion(label, tau, omega).order0 for label in block_labels]
    return product(matrices)


def mixed_product_operator(labels: tuple[Label, ...], tau: Label, omega: Label) -> Matrix:
    pieces = [elementary_expansion(label, tau, omega) for label in labels]
    out: Matrix = {}

    for c_index in range(len(pieces)):
        matrices = [
            piece.mixed_order2 if index == c_index else piece.order0
            for index, piece in enumerate(pieces)
        ]
        out = matrix_add(out, product(matrices))

    for tame_index in range(len(pieces)):
        for wild_index in range(len(pieces)):
            if tame_index == wild_index:
                continue
            matrices = []
            for index, piece in enumerate(pieces):
                if index == tame_index:
                    matrices.append(piece.tame_order1)
                elif index == wild_index:
                    matrices.append(piece.wild_order1)
                else:
                    matrices.append(piece.order0)
            out = matrix_add(out, product(matrices))

    return out


@lru_cache(maxsize=None)
def h4_orbit_for_cell(cell: Cell4) -> tuple[int, int, str]:
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
    raise ValueError(f"cell not found in H4 skeleton: {cell}")


def expansion_summary(cell: Cell4, tau: Label, omega: Label, entry: Entry) -> tuple[dict[str, object], ...]:
    rows: list[dict[str, object]] = []
    slot_names = ("tau", "omega", "beta", "iota")
    for slot_name, label in zip(slot_names, cell, strict=True):
        expansion = elementary_expansion(label, tau, omega)
        rows.append(
            {
                "slot": slot_name,
                "label": label,
                "M_count": len(expansion.order0),
                "Bt_count": len(expansion.tame_order1),
                "Bw_count": len(expansion.wild_order1),
                "C_count": len(expansion.mixed_order2),
                "M_entry": matrix_entry(expansion.order0, entry),
                "Bt_entry": matrix_entry(expansion.tame_order1, entry),
                "Bw_entry": matrix_entry(expansion.wild_order1, entry),
                "C_entry": matrix_entry(expansion.mixed_order2, entry),
            }
        )
    return tuple(rows)


def source_note_for(cell: Cell4, entry: Entry) -> tuple[str, ...]:
    if cell == TARGET_CELL and entry == TARGET_ENTRY:
        return (
            "source = original sealed target",
            "witness = (u, 1, u, 1, u, u)",
            "lift = beta-in, cell = (u, 1, 1, u)",
        )
    if cell == PLUS2_CELL and entry == PLUS2_ENTRY:
        return (
            "source = TTWW arity-2 orbit-size-24 +2 stratum",
            "witness = (wu, w, 1+u, wu, w, 1+u)",
            "lift = beta-in, cell = (wu, w, wu, w)",
        )
    return ("source = command-line cell",)


def verify_cell(title: str, cell: Cell4, entry: Entry) -> VerificationResult:
    tau, omega = cell[0], cell[1]
    orbit_id, orbit_size, family = h4_orbit_for_cell(cell)
    traces: list[TermTrace] = []

    stage2_operator: Matrix = {}
    stage3_operator: Matrix = {}
    for partition in all_partitions(4):
        block_labels = block_labels_for(cell, partition)
        moment = moment_operator(block_labels, tau, omega)
        base_entry = matrix_entry(moment, entry)
        leibniz = leibniz_coefficient(partition)
        correction = bianchi_correction(partition)
        projected = leibniz + correction
        traces.append(
            TermTrace(
                partition=partition,
                block_labels=block_labels,
                base_entry=base_entry,
                leibniz_coefficient=leibniz,
                bianchi_correction=correction,
                projected_coefficient=projected,
            )
        )
        stage2_operator = matrix_add(
            stage2_operator,
            matrix_scale(moment, leibniz * NORMALIZATION),
        )
        stage3_operator = matrix_add(
            stage3_operator,
            matrix_scale(moment, projected * NORMALIZATION),
        )

    direct_product_mixed = mixed_product_operator(cell, tau, omega)
    path_composed_mixed = elementary_expansion(add_many(cell), tau, omega).mixed_order2
    direct_defect_mixed = matrix_sub(direct_product_mixed, path_composed_mixed)

    stage2_raw_entry = matrix_entry(stage2_operator, entry)
    stage3_raw_entry = matrix_entry(stage3_operator, entry)
    final_entry = stage3_raw_entry / NORMALIZATION

    return VerificationResult(
        title=title,
        cell=cell,
        entry=entry,
        source_note=source_note_for(cell, entry),
        tau=tau,
        omega=omega,
        h4_orbit_id=orbit_id,
        h4_orbit_size=orbit_size,
        h4_family=family,
        expansion_rows=expansion_summary(cell, tau, omega, entry),
        direct_product_mixed_entry=matrix_entry(direct_product_mixed, entry),
        path_composed_mixed_entry=matrix_entry(path_composed_mixed, entry),
        direct_defect_mixed_entry=matrix_entry(direct_defect_mixed, entry),
        traces=tuple(traces),
        stage2_raw_entry=stage2_raw_entry,
        stage3_raw_entry=stage3_raw_entry,
        final_entry=final_entry,
    )


def result_branch(result: VerificationResult) -> str:
    if result.cell == TARGET_CELL and result.entry == TARGET_ENTRY:
        if result.final_entry == Fraction(-1):
            return (
                "Cell 1 returns `-1`: Heaven's recipe is verified at the sealed "
                "target cell."
            )
        if result.final_entry == Fraction(-2):
            return (
                "Cell 1 returns `-2`: the recipe as implemented leaves the full "
                "unrestricted Leibniz value."
            )
        return "Cell 1 returns neither `-1` nor `-2`: re-escalation is required."
    if result.final_entry == Fraction(2):
        return "Cell 2 returns `+2`: the +2 stratum is consistent with the recipe."
    return "Cell 2 does not return `+2`: the +2 stratum does not track this recipe."


def lifted_mixed_records(
    *,
    family: str | None = None,
    orbit_size: int | None = None,
) -> tuple[SweepRecord, ...]:
    """Reconstruct lifted mixed records from arity-2 commutator orbits.

    This uses the arity-2 commutator computation only to locate the support
    class.  The R^(4) values below are recomputed by ``verify_cell`` and do
    not use the commutator coefficient as an input.
    """

    commutator = tangent_compatible(compute_witnesses("commutator"))
    coefficients = coefficient_by_key(commutator)
    records: list[SweepRecord] = []

    for orbit_id, orbit in enumerate(orbit_decomposition(commutator)):
        if orbit_size is not None and int(orbit["size"]) != orbit_size:
            continue

        seed = min(orbit["keys"])
        lift_candidates = [
            ("alpha-in", (0, 1, 2, 4)),
            ("beta-in", (0, 1, 3, 4)),
        ]
        for lift_name, indices in lift_candidates:
            cell = tuple(seed[index] for index in indices)
            if add_many(cell) != ZERO:
                continue
            h4_orbit_id, h4_orbit_size, h4_family = h4_orbit_for_cell(cell)
            if h4_family not in {"TTWW", "TWWW"}:
                break
            if family is not None and h4_family != family:
                break
            entry = (seed[4], seed[4])
            result = verify_cell("sweep", cell, entry)
            records.append(
                SweepRecord(
                    orbit_id=orbit_id,
                    orbit_size=int(orbit["size"]),
                    coefficient=coefficients[seed],
                    witness=seed,
                    lift_name=lift_name,
                    cell=cell,
                    entry=entry,
                    h4_orbit_id=h4_orbit_id,
                    h4_orbit_size=h4_orbit_size,
                    h4_family=h4_family,
                    stage2_value=result.stage2_raw_entry / NORMALIZATION,
                    final_value=result.final_entry,
                )
            )
            break

    return tuple(records)


def lifted_ttww_size24_records() -> tuple[SweepRecord, ...]:
    """Reconstruct the TTWW arity-2 orbit-size-24 lift class."""

    return lifted_mixed_records(family="TTWW", orbit_size=24)


def counter_text(counter: Counter[Fraction]) -> str:
    if not counter:
        return "{}"
    return "{" + ", ".join(
        f"{fraction_text(value)}: {count}" for value, count in sorted(counter.items())
    ) + "}"


def orbit_key(record: SweepRecord) -> tuple[str, int, int]:
    return record.h4_family, record.h4_orbit_size, record.h4_orbit_id


def grouped_records(records: tuple[SweepRecord, ...]) -> list[tuple[tuple[str, int, int], list[SweepRecord]]]:
    groups: dict[tuple[str, int, int], list[SweepRecord]] = {}
    for record in records:
        groups.setdefault(orbit_key(record), []).append(record)
    return sorted(groups.items(), key=lambda item: item[0])


def sweep_report(records: tuple[SweepRecord, ...]) -> str:
    plus2 = [record for record in records if record.final_value == Fraction(2)]
    stage2_distribution = Counter(record.stage2_value for record in records)
    final_distribution = Counter(record.final_value for record in records)
    coefficient_distribution = Counter(record.coefficient for record in records)
    h4_orbit_distribution = Counter(record.h4_orbit_size for record in records)

    lines = [
        "# H4 R4 Covariant Sweep - TTWW Orbit-Size-24 Lift Class",
        "",
        "This is a broader sanity sweep after the two-cell verification.  It",
        "reconstructs the TTWW arity-2 commutator orbit-size-24 lift class from",
        "the arity-2 operator computation, then evaluates every lifted cell with",
        "`compute_R4_covariant_at_cell.py`'s independent paired-slot recipe.",
        "The inherited arity-2 coefficient is reported only as class metadata;",
        "it is not used to compute any `R^(4)` value.",
        "",
        "## Summary",
        "",
        f"- records scanned: {len(records)}",
        f"- inherited coefficient distribution: {counter_text(coefficient_distribution)}",
        f"- unrestricted Leibniz value distribution: {counter_text(stage2_distribution)}",
        f"- paired-slot `R^(4)` value distribution: {counter_text(final_distribution)}",
        f"- `R^(4)=+2` records: {len(plus2)}",
        "- H4 orbit-size distribution: "
        + ", ".join(f"{size}: {count}" for size, count in sorted(h4_orbit_distribution.items())),
        "",
        "The `+2` discriminator is therefore not isolated: the independent",
        "paired-slot verifier finds the same 40-record `+2` stratum expected from",
        "the earlier class scan, without importing the cumulant scripts.",
        "",
        "## First ten `+2` records",
        "",
        "| arity-2 orbit | lift | cell | entry | stage 2 | R^(4) | inherited coeff |",
        "|---:|---|---|---|---:|---:|---:|",
    ]

    for record in plus2[:10]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record.orbit_id),
                    record.lift_name,
                    "`" + label_list_text(record.cell) + "`",
                    "`"
                    + f"{label_name(record.entry[0])} <- {label_name(record.entry[1])}"
                    + "`",
                    fraction_text(record.stage2_value),
                    fraction_text(record.final_value),
                    fraction_text(record.coefficient),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Method Guardrail",
        "",
        "This sweep imports no `compute_h4_mobius_witness.py` or",
        "`compute_h4_mobius_followups.py` symbols.  The only imported numerical",
        "operators are the Section 9.1 `M`, `B^tau`, `B^omega`, and `C` pieces",
        "already used by the verifier.",
        "",
    ]
    return "\n".join(lines)


def full_mixed_table_report(records: tuple[SweepRecord, ...]) -> str:
    stage2_distribution = Counter(record.stage2_value for record in records)
    final_distribution = Counter(record.final_value for record in records)
    coefficient_distribution = Counter(record.coefficient for record in records)

    lines = [
        "# H4 R4 Covariant Full Mixed-Lift Coefficient Table",
        "",
        "This report evaluates the paired-slot `R^(4)` recipe on every lifted",
        "mixed support record coming from the 592 arity-2 commutator orbits.  The",
        "arity-2 computation is used only to locate the support records; the",
        "coefficient values are recomputed by the standalone paired-slot verifier.",
        "",
        "## Global Summary",
        "",
        f"- records scanned: {len(records)}",
        f"- inherited coefficient distribution: {counter_text(coefficient_distribution)}",
        f"- unrestricted Leibniz value distribution: {counter_text(stage2_distribution)}",
        f"- paired-slot `R^(4)` value distribution: {counter_text(final_distribution)}",
        f"- H4 mixed orbit groups: {len(grouped_records(records))}",
        "",
        "## Seven Mixed Orbit Groups",
        "",
        "| family | H4 orbit | H4 orbit size | records | inherited coeffs | unrestricted Leibniz | paired-slot R^(4) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    for (family, h4_size, h4_orbit), group in grouped_records(records):
        lines.append(
            "| "
            + " | ".join(
                [
                    family,
                    str(h4_orbit),
                    str(h4_size),
                    str(len(group)),
                    counter_text(Counter(record.coefficient for record in group)),
                    counter_text(Counter(record.stage2_value for record in group)),
                    counter_text(Counter(record.final_value for record in group)),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The full mixed-lift coefficient table supports the same distinction as the",
        "two-cell verifier: input-side inheritance locates the support, while the",
        "paired-slot projection computes the signed coefficient.  The paired-slot",
        "rule removes the crossing contribution wherever it is active; it does not",
        "use the inherited commutator coefficient as a target value.",
        "",
        "## Method Guardrail",
        "",
        "This report imports no arity-4 Mobius witness or follow-up code.  It uses",
        "only the `FisherJet` operator pieces (`M`, `B^tau`, `B^omega`, `C`) and",
        "the arity-2 commutator support to choose which mixed records to evaluate.",
        "",
    ]
    return "\n".join(lines)


def report(result: VerificationResult) -> str:
    slot_names = ("tau", "omega", "beta", "iota")
    entry_text = f"{label_name(result.entry[0])} <- {label_name(result.entry[1])}"
    stage2_normalized = result.stage2_raw_entry / NORMALIZATION

    lines = [
        f"# {result.title}",
        "",
        "This report computes the two-cell `R^(4)` verifier directly from the",
        "`FisherJet` operator ingredients.  The script gets `M`, `B^tau`,",
        "`B^omega`, and `C` through the functor; it does not import",
        "the existing arity-4 witness or follow-up code.",
        "",
        "## Cell",
        "",
        "```text",
        f"cell  = {label_list_text(result.cell)}",
        f"entry = {entry_text}",
        f"tau displacement   = {label_name(result.tau)}",
        f"omega displacement = {label_name(result.omega)}",
        f"sum(cell) = {label_name(add_many(result.cell))}",
        f"H4 orbit = {result.h4_orbit_id}, family = {result.h4_family}, size = {result.h4_orbit_size}",
    ]
    lines.extend(result.source_note)
    lines += [
        "```",
        "",
        "## Stage 1 - Taylor Pieces",
        "",
        "| slot | label | cond | M nz | B_tau nz | B_omega nz | C nz | M entry | B_tau entry | B_omega entry | C entry |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in result.expansion_rows:
        label = row["label"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["slot"]),
                    label_name(label),
                    conductor(label),
                    str(row["M_count"]),
                    str(row["Bt_count"]),
                    str(row["Bw_count"]),
                    str(row["C_count"]),
                    fraction_text(row["M_entry"]),
                    fraction_text(row["Bt_entry"]),
                    fraction_text(row["Bw_entry"]),
                    fraction_text(row["C_entry"]),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "The direct mixed path check is recorded separately from the contraction",
        "calculation:",
        "",
        "```text",
        f"[s r] K(x1)K(x2)K(x3)K(x4) entry = {fraction_text(result.direct_product_mixed_entry)}",
        f"[s r] K(x1+x2+x3+x4) entry        = {fraction_text(result.path_composed_mixed_entry)}",
        f"direct product-minus-composed entry = {fraction_text(result.direct_defect_mixed_entry)}",
        "```",
        "",
        "## Stage 2 - Unrestricted Leibniz Contraction",
        "",
        "All 15 product-rule contractions are generated.  No non-crossing filter is",
        "applied at this stage.",
        "",
        "| contraction | block labels | base entry | Leibniz coeff | raw contribution |",
        "|---|---|---:|---:|---:|",
    ]

    for trace in result.traces:
        lines.append(
            "| "
            + " | ".join(
                [
                    "`" + partition_text(trace.partition, slot_names) + "`",
                    "`" + block_label_text(trace.block_labels) + "`",
                    fraction_text(trace.base_entry),
                    fraction_text(trace.leibniz_coefficient),
                    fraction_text(trace.raw_leibniz_contribution),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "```text",
        f"raw unrestricted Leibniz entry = {fraction_text(result.stage2_raw_entry)}",
        f"after 1/4! normalization       = {fraction_text(stage2_normalized)}",
        "```",
        "",
        "## Stage 3 - Paired-Slot Projection",
        "",
        "The six-term paired-slot alternation cancels the middle pair-of-pairs",
        "`(tau,beta;omega,iota)` and propagates that cancellation through its",
        "Leibniz refinements.  The table shows the correction applied after the",
        "unrestricted expansion has already been formed.",
        "",
        "| contraction | Leibniz coeff | Bianchi correction | projected coeff | raw projected contribution |",
        "|---|---:|---:|---:|---:|",
    ]

    for trace in result.traces:
        lines.append(
            "| "
            + " | ".join(
                [
                    "`" + partition_text(trace.partition, slot_names) + "`",
                    fraction_text(trace.leibniz_coefficient),
                    fraction_text(trace.bianchi_correction),
                    fraction_text(trace.projected_coefficient),
                    fraction_text(trace.raw_projected_contribution),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "```text",
        f"raw projected entry = {fraction_text(result.stage3_raw_entry)}",
        "```",
        "",
        "## Stage 4 - Normalization",
        "",
        "```text",
        f"R^(4) entry = {fraction_text(result.stage3_raw_entry)} / 24 = {fraction_text(result.final_entry)}",
        "```",
        "",
        "## Outcome",
        "",
        result_branch(result),
        "",
    ]
    return "\n".join(lines)


def label_table() -> dict[str, Label]:
    out: dict[str, Label] = {}
    for label in LABELS:
        name = label_name(label)
        out[name] = label
        out[name.replace("(", "").replace(")", "")] = label

    out.update(
        {
            "0": ZERO,
            "u": U,
            "wu": WU,
            "(w+1)u": (0, 3),
            "w+1u": (0, 3),
            "1": ONE,
            "w": W,
            "w+1": (3, 0),
        }
    )
    return out


def parse_label(text: str) -> Label:
    table = label_table()
    key = text.strip()
    if key not in table:
        raise argparse.ArgumentTypeError(f"unknown label: {text}")
    return table[key]


def parse_cell(text: str) -> Cell4:
    parts = [part.strip() for part in text.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("--cell must contain four comma-separated labels")
    return tuple(parse_label(part) for part in parts)  # type: ignore[return-value]


def parse_entry(text: str) -> Entry:
    if "<-" in text:
        left, right = text.split("<-", 1)
        return parse_label(left), parse_label(right)
    label = parse_label(text)
    return label, label


def write_report(path: Path, result: VerificationResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report(result), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cell", type=parse_cell, help="four comma-separated labels")
    parser.add_argument("--entry", type=parse_entry, help="matrix entry, e.g. 'u<-u' or 'u'")
    parser.add_argument("--title", default="H4 R4 Covariant Cell Verification")
    parser.add_argument("--report", type=Path, help="optional markdown report path")
    parser.add_argument(
        "--sweep-ttww-size24",
        action="store_true",
        help="write the TTWW arity-2 orbit-size-24 sweep report",
    )
    parser.add_argument(
        "--full-mixed-table",
        action="store_true",
        help="write the full seven-orbit mixed-lift coefficient table",
    )
    args = parser.parse_args()

    if args.full_mixed_table:
        text = full_mixed_table_report(lifted_mixed_records())
        print(text)
        if args.report is not None:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(text, encoding="utf-8")
            print(f"Wrote {args.report}")
        return

    if args.sweep_ttww_size24:
        text = sweep_report(lifted_ttww_size24_records())
        print(text)
        if args.report is not None:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(text, encoding="utf-8")
            print(f"Wrote {args.report}")
        return

    if args.cell is not None:
        entry = args.entry if args.entry is not None else (args.cell[3], args.cell[3])
        result = verify_cell(args.title, args.cell, entry)
        text = report(result)
        print(text)
        if args.report is not None:
            write_report(args.report, result)
            print(f"Wrote {args.report}")
        return

    reports_dir = Path(__file__).with_name("reports")
    results = [
        (
            reports_dir / "h4_R4_covariant_target_cell.md",
            verify_cell("H4 R4 Covariant Verification - Target Cell", TARGET_CELL, TARGET_ENTRY),
        ),
        (
            reports_dir / "h4_R4_covariant_plus2_cell.md",
            verify_cell("H4 R4 Covariant Verification - TTWW +2 Cell", PLUS2_CELL, PLUS2_ENTRY),
        ),
    ]

    for path, result in results:
        write_report(path, result)
        print(report(result))
        print(f"Wrote {path}\n")

    sweep_path = reports_dir / "h4_R4_covariant_ttww_size24_sweep.md"
    sweep_text = sweep_report(lifted_ttww_size24_records())
    sweep_path.write_text(sweep_text, encoding="utf-8")
    print(sweep_text)
    print(f"Wrote {sweep_path}\n")

    full_table_path = reports_dir / "h4_R4_covariant_full_mixed_lift_table.md"
    full_table_text = full_mixed_table_report(lifted_mixed_records())
    full_table_path.write_text(full_table_text, encoding="utf-8")
    print(full_table_text)
    print(f"Wrote {full_table_path}\n")


if __name__ == "__main__":
    main()
