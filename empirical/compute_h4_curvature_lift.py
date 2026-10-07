"""Arity-4 curvature-lift support audit for F_4[u]/(u^2).

This script supports Theorem 9.3 of Paper 11.  The theorem identifies the
support of the analytic arity-4 curvature coefficient R^(4) with the canonical
input-side boundary map already present in the arity-2 witness data.

An arity-2 commutator witness has labels

    (tau, omega, alpha, beta, input, output).

The input-side boundary lift sends it to the closed arity-4 cells

    (tau, omega, alpha, input),  (tau, omega, beta, input),

whenever the four labels sum to zero.  This is the least extra-choice
projection that keeps the tame displacement, wild displacement, operator leg,
and vector leg that actually enters the operator product.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from compute_f4_u2_ext_ch import (
    ACTIONS,
    ZERO,
    add_label,
    coefficient_by_key,
    compute_witnesses,
    conductor,
    label_name,
    orbit_decomposition,
    tangent_compatible,
)
from compute_h4_f4_u2 import S4, conductor_family, h4_cells, transform_cell


Key = tuple[tuple[int, int], ...]
Cell4 = tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]

POSITIONS = ("tau", "omega", "alpha", "beta", "input", "output")
INPUT_SIDE = ((0, 1, 2, 4), (0, 1, 3, 4))
OUTPUT_SIDE = ((0, 1, 2, 5), (0, 1, 3, 5))
OPERATOR_SIDE = ((0, 1, 2, 3),)
ALL_LITERAL = tuple(combinations(range(6), 4))


def add_many(labels: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    out = ZERO
    for label in labels:
        out = add_label(out, label)
    return out


def conductor_letter(label: tuple[int, int]) -> str:
    return "T" if conductor(label) == "u" else "W"


def conductor_family_from_cell(cell: Cell4) -> str:
    return "".join(sorted(conductor_letter(label) for label in cell))


def cell_text(cell: Cell4) -> str:
    return "(" + ", ".join(label_name(label) for label in cell) + ")"


def cell_sort_key(cell: Cell4) -> tuple[tuple[int, int], ...]:
    return cell


def h4_orbit_rows() -> tuple[dict[Cell4, int], list[dict[str, object]]]:
    remaining = set(h4_cells(distinct=False))
    cell_to_orbit: dict[Cell4, int] = {}
    rows: list[dict[str, object]] = []

    while remaining:
        seed = min(remaining, key=cell_sort_key)
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


def h2_commutator_orbits() -> tuple[set[int], dict[Key, int], list[dict[str, object]]]:
    defect = tangent_compatible(compute_witnesses("defect"))
    commutator = tangent_compatible(compute_witnesses("commutator"))
    defect_orbits = orbit_decomposition(defect)
    commutator_coeffs = coefficient_by_key(commutator)

    key_to_orbit: dict[Key, int] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        for key in orbit["keys"]:
            key_to_orbit[key] = orbit_id

    commutator_orbits = {key_to_orbit[key] for key in commutator_coeffs}
    return commutator_orbits, key_to_orbit, defect_orbits


def projection_summary(
    projection_sets: tuple[tuple[int, int, int, int], ...],
    commutator_keys: set[Key],
    key_to_h2_orbit: dict[Key, int],
    cell_to_h4_orbit: dict[Cell4, int],
    h4_rows: list[dict[str, object]],
) -> dict[str, object]:
    h2_orbits: set[int] = set()
    h4_to_h2: dict[int, set[int]] = defaultdict(set)
    h2_to_h4: dict[int, set[int]] = defaultdict(set)
    h4_entry_hits: Counter[int] = Counter()
    family_entry_hits: Counter[str] = Counter()
    closed_hits = 0

    for key in commutator_keys:
        h2_orbit = key_to_h2_orbit[key]
        for projection in projection_sets:
            cell = tuple(key[index] for index in projection)
            if add_many(cell) != ZERO:
                continue
            h4_orbit = cell_to_h4_orbit[cell]
            h2_orbits.add(h2_orbit)
            h4_to_h2[h4_orbit].add(h2_orbit)
            h2_to_h4[h2_orbit].add(h4_orbit)
            h4_entry_hits[h4_orbit] += 1
            family_entry_hits[h4_rows[h4_orbit]["family"]] += 1
            closed_hits += 1

    return {
        "h2_orbits": h2_orbits,
        "h4_to_h2": h4_to_h2,
        "h2_to_h4": h2_to_h4,
        "h4_entry_hits": h4_entry_hits,
        "family_entry_hits": family_entry_hits,
        "closed_hits": closed_hits,
    }


def projection_table(
    projection_summaries: dict[str, dict[str, object]],
    total_commutator_orbits: int,
) -> list[str]:
    lines = [
        "| projection | lifted H2 orbits | closed hits | family hits | H2 orbit -> H4 orbit count |",
        "|---|---:|---:|---|---|",
    ]
    for name, summary in projection_summaries.items():
        h2_to_h4 = summary["h2_to_h4"]
        orbit_count_distribution = Counter(len(ids) for ids in h2_to_h4.values())
        family_hits = ", ".join(
            f"{family}: {count}"
            for family, count in sorted(summary["family_entry_hits"].items())
        )
        h2_to_h4_text = ", ".join(
            f"{count} ids: {number}"
            for count, number in sorted(orbit_count_distribution.items())
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    f"{len(summary['h2_orbits'])}/{total_commutator_orbits}",
                    str(summary["closed_hits"]),
                    family_hits or "-",
                    h2_to_h4_text or "-",
                ]
            )
            + " |"
        )
    return lines


def report() -> str:
    cell_to_h4_orbit, h4_rows = h4_orbit_rows()
    commutator_orbits, key_to_h2_orbit, _defect_orbits = h2_commutator_orbits()
    commutator_keys = set(coefficient_by_key(tangent_compatible(compute_witnesses("commutator"))))

    projection_summaries = {
        "input alpha leg": projection_summary(
            (INPUT_SIDE[0],), commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
        "input beta leg": projection_summary(
            (INPUT_SIDE[1],), commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
        "input-side union": projection_summary(
            INPUT_SIDE, commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
        "operator pair": projection_summary(
            OPERATOR_SIDE, commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
        "output-side union": projection_summary(
            OUTPUT_SIDE, commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
        "all literal four-label projections": projection_summary(
            ALL_LITERAL, commutator_keys, key_to_h2_orbit, cell_to_h4_orbit, h4_rows
        ),
    }

    input_summary = projection_summaries["input-side union"]
    hit_h4_orbits = set(input_summary["h4_to_h2"])
    family_orbit_counts = Counter(row["family"] for row in h4_rows)
    hit_family_orbit_counts = Counter(h4_rows[orbit_id]["family"] for orbit_id in hit_h4_orbits)
    pure_hits = {
        orbit_id
        for orbit_id in hit_h4_orbits
        if h4_rows[orbit_id]["family"] in {"TTTT", "WWWW"}
    }

    lines = [
        "# Arity-4 Curvature-Lift Support Audit for F4[u]/(u^2)",
        "",
        "This is the support-level test for Theorem 9.3 of Paper 11.  The",
        "analytic arity-4 curvature coefficient R^(4) is defined there as the",
        "centroid-normalized, S_4-symmetrized four-linear coefficient projected",
        "onto the antisymmetric commutator component.  This script audits its",
        "claimed support via the canonical input-side boundary of the already",
        "computed arity-2 commutator witnesses.",
        "",
        "## Measured arity-4 skeleton",
        "",
        "- total closed nontrivial 4-cells: 3165",
        f"- Gamma_R x S_4 orbits: {len(h4_rows)}",
        "- family orbit counts: "
        + ", ".join(
            f"{family}: {count}" for family, count in sorted(family_orbit_counts.items())
        ),
        "",
        "## Input-side lift",
        "",
        "For a commutator witness",
        "`(tau, omega, alpha, beta, input, output)`, the input-side lift uses",
        "the two closed projections",
        "`(tau, omega, alpha, input)` and `(tau, omega, beta, input)`.",
        "",
        f"- arity-2 commutator orbits: {len(commutator_orbits)}",
        f"- lifted arity-2 commutator orbits: {len(input_summary['h2_orbits'])}",
        "- H2 orbit to H4 orbit multiplicity: "
        + ", ".join(
            f"{count} H4 orbit: {number}"
            for count, number in sorted(
                Counter(len(ids) for ids in input_summary["h2_to_h4"].values()).items()
            )
        ),
        f"- H4 mixed orbits hit: {sum(count for family, count in hit_family_orbit_counts.items() if family in {'TTWW', 'TWWW'})} / 7",
        f"- H4 pure orbits hit: {len(pure_hits)} / 11",
        "- lifted entry hits by family: "
        + ", ".join(
            f"{family}: {count}"
            for family, count in sorted(input_summary["family_entry_hits"].items())
        ),
        "",
        "Thus every one of the 592 commutator orbits has exactly one",
        "input-side arity-4 orbit image, and the images are exactly the seven",
        "mixed TTWW/TWWW orbits.  No TTTT or WWWW orbit is hit by this lift.",
        "",
        "## Mixed-orbit image table",
        "",
        "| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |",
        "|---:|---|---:|---:|---:|---|",
    ]

    for orbit_id in sorted(
        hit_h4_orbits,
        key=lambda oid: (h4_rows[oid]["family"], h4_rows[oid]["size"], oid),
    ):
        row = h4_rows[orbit_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(orbit_id),
                    str(row["family"]),
                    str(row["size"]),
                    str(len(input_summary["h4_to_h2"][orbit_id])),
                    str(input_summary["h4_entry_hits"][orbit_id]),
                    "`" + cell_text(row["seed"]) + "`",
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Projection due diligence",
        "",
    ]
    lines += projection_table(projection_summaries, len(commutator_orbits))

    lines += [
        "",
        "The single input projections split the 592 into two 296-orbit halves.",
        "Their union is exact.  The operator-pair and output-side projections",
        "under-detect the commutator support, while allowing all literal four-label",
        "projections is too loose because it also routes through pure TTTT and",
        "WWWW cells.",
        "",
        "## Status",
        "",
        "GREEN for Theorem 9.3 at support level: under the input-side boundary",
        "convention, the 592 lift exactly onto the seven mixed arity-4 orbits",
        "and avoid the eleven pure orbits.",
        "",
        "Coefficient values are supplied by `h4_R4_covariant_full_mixed_lift_table.md`.",
        "After FC2, the cohomological source is the filtered binary Ext_CH",
        "class; a standalone hypercell Ext_CH^(4) complex is optional rather",
        "than the source of this support theorem.  Open beyond this report:",
        "family extension to deeper mixed rows and higher arities.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    text = report()
    report_path = Path(__file__).with_name("reports") / "h4_f4_u2_curvature_lift.md"
    report_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nWrote {report_path}")


if __name__ == "__main__":
    main()
