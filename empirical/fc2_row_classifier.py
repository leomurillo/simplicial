"""Row-level FC2 classifier for filtered carry and visible support kernels.

This script starts the post-theorem FC2 atlas phase.  It does not re-prove the
filtered source theorem; it reads or computes finite row certificates and
separates:

1. the full filtered section class diagnostic;
2. the raw-support support projection diagnostic;
3. known Fisher-jet/K_CH shadows where an exact lift certificate exists;
4. normalizer orbit data already certified for each row.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable

from cocycle_reducer import CocycleReducer
from fisher_jet_functor import FisherJet
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import (
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f16_ring,
    make_f2_u4_ring,
    make_f4_u2_ring,
)


REPORT_DIR = Path(__file__).with_name("reports")
DEFAULT_JSON = REPORT_DIR / "fc2_row_classification.json"
DEFAULT_MD = REPORT_DIR / "fc2_row_classification.md"

F4_CONSTRUCTOR_JSON = REPORT_DIR / "local_adjacency_constructor_f4_u2.json"
F4_EXT_JSON = REPORT_DIR / "ext_ch_cocycle_f4_u2.json"
F2_U5_JSON = REPORT_DIR / "next_local_row_f2_u5.json"
F8_U2_JSON = REPORT_DIR / "next_local_row_f8_u2.json"
FC2_CURVATURE_JSON = REPORT_DIR / "fc2_curvature_carry_certificate.json"


CONTROL_FACTORIES: dict[str, Callable[[], FiniteLocalRing]] = {
    "f16-field": make_f16_ring,
    "f2-u4-control": make_f2_u4_ring,
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def counter_json(counter: Counter[object]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter, key=str)}


def compact_coboundary(reduction: dict[str, Any] | None) -> dict[str, Any] | None:
    if reduction is None:
        return None
    if reduction.get("skipped"):
        return dict(reduction)
    keys = [
        "mode",
        "c2_scope",
        "coefficient_field",
        "c1_generators",
        "c2_dimension",
        "coboundary_rank",
        "residual_dimension",
        "raw_support",
        "residual_support",
        "residual_equal_raw",
        "raw_is_coboundary",
        "rational_rank_certified",
        "raw_non_coboundary_over_q_certified",
    ]
    return {key: reduction[key] for key in keys if key in reduction}


def cell_orbit_summary(constructor: LocalAdjacencyConstructor, arity: int) -> dict[str, Any]:
    tower = HyperAdjacencyTower(constructor)
    cells = tower.cells(arity)
    _cell_to_orbit, rows = tower.orbit_maps(arity)
    return {
        "cells": len(cells),
        "orbits": len(rows),
        "family_orbit_counts": dict(
            sorted(Counter(str(row["family"]) for row in rows).items())
        ),
        "orbit_size_distribution": dict(
            sorted(Counter(int(row["size"]) for row in rows).items())
        ),
    }


def fisher_probe(constructor: LocalAdjacencyConstructor) -> dict[str, Any] | None:
    packet_labels = [labels[0] for labels in constructor.packets.values() if labels]
    if not packet_labels:
        return None
    jet = FisherJet(constructor)
    left_mode = packet_labels[0]
    right_mode = packet_labels[min(1, len(packet_labels) - 1)]
    alpha = constructor.ring.nontrivial[0]
    expansion = jet.elementary_expansion(alpha, left_mode, right_mode)
    return {
        "alpha": constructor.ring.label_name(alpha),
        "left_mode": constructor.ring.label_name(left_mode),
        "right_mode": constructor.ring.label_name(right_mode),
        "order0_support": len(expansion.order0),
        "left_order1_support": len(expansion.left_order1),
        "right_order1_support": len(expansion.right_order1),
        "mixed_order2_support": len(expansion.mixed_order2),
    }


def support_erasure_summary(
    *,
    full: dict[str, Any] | None,
    support: dict[str, Any] | None,
) -> dict[str, Any]:
    full_residual = (
        None
        if not full or full.get("skipped")
        else int(full.get("residual_support", 0))
    )
    support_residual = (
        None
        if not support or support.get("skipped")
        else int(support.get("residual_support", 0))
    )
    raw_support = (
        None
        if not full or full.get("skipped")
        else int(full.get("raw_support", full.get("residual_support", 0)))
    )
    erased = None
    erasure_ratio = None
    if full_residual is not None and support_residual is not None:
        erased = full_residual - support_residual
        erasure_ratio = None if full_residual == 0 else erased / full_residual
    if full_residual is None:
        status = "full filtered residual not measured"
    elif full_residual == 0:
        status = "filtered class trivial in measured full-block model"
    elif support_residual == 0:
        status = "nonzero full filtered class erased by raw-support projection"
    elif support_residual is None:
        status = "nonzero full filtered class; support projection not measured"
    else:
        status = "nonzero full filtered class has support-visible residual"
    return {
        "raw_support": raw_support,
        "full_filtered_residual": full_residual,
        "support_projection_residual": support_residual,
        "support_projection_erased_from_full": erased,
        "support_projection_erasure_ratio": erasure_ratio,
        "status": status,
    }


def f4_known_shadow() -> dict[str, Any]:
    payload = load_json(FC2_CURVATURE_JSON)
    h4 = payload["arity4_curvature_shadow"]
    return {
        "status": "complete for the first mixed row",
        "k_ch_commutator_orbits": h4["arity_2_commutator_orbits"],
        "lifted_commutator_orbits": h4["lifted_arity_2_commutator_orbits"],
        "mixed_h4_orbits_hit": h4["mixed_h4_orbits_hit"],
        "mixed_h4_orbits_total": h4["mixed_h4_orbits_total"],
        "pure_h4_orbits_hit": h4["pure_h4_orbits_hit"],
        "pure_h4_orbits_total": h4["pure_h4_orbits_total"],
        "entry_hits_by_family": h4["entry_hits_by_family"],
    }


def f4_row() -> dict[str, Any]:
    constructor_report = load_json(F4_CONSTRUCTOR_JSON)
    ext = load_json(F4_EXT_JSON)
    constructor = LocalAdjacencyConstructor(make_f4_u2_ring())
    support = CocycleReducer(constructor).coboundary_reduction(
        "support",
        c2_scope="raw_support",
    )
    full = ext["coboundary_reduction"]
    return finalize_row(
        {
            "row_key": "f4-u2",
            "row_role": "certified mixed row",
            "ring": ext["ring"],
            "constructor": constructor_report["constructor"],
            "h3": constructor_report["h3"],
            "h4": constructor_report["h4"],
            "ext_ch": {
                "raw_atom_count": ext["raw_atom_count"],
                "raw_pair_count": ext["raw_pair_count"],
                "raw_coefficient_distribution": ext["raw_coefficient_distribution"],
                "raw_path_distribution": ext["raw_path_distribution"],
                "atom_orbit_count": ext["atom_orbit_count"],
                "atom_orbit_size_distribution": ext["atom_orbit_size_distribution"],
                "atom_orbit_missing_total": ext["atom_orbit_missing_total"],
                "pair_orbit_count": ext["pair_orbit_count"],
                "pair_orbit_size_distribution": ext["pair_orbit_size_distribution"],
                "pair_orbit_missing_total": ext["pair_orbit_missing_total"],
                "full_block_coboundary": compact_coboundary(full),
                "support_projection_coboundary": compact_coboundary(support),
            },
            "fisher_jet_shadow": {
                "support_projection": compact_coboundary(support),
                "k_ch": f4_known_shadow(),
                "representative_probe": fisher_probe(constructor),
            },
            "sources": [
                str(F4_CONSTRUCTOR_JSON),
                str(F4_EXT_JSON),
                str(FC2_CURVATURE_JSON),
            ],
        }
    )


def next_row_from_report(row_key: str, path: Path) -> dict[str, Any]:
    report = load_json(path)
    ext = report["ext_ch"]
    return finalize_row(
        {
            "row_key": row_key,
            "row_role": "certified atlas row",
            "ring": report["ring"],
            "constructor": {
                "ring": report["ring"],
                "label_count": report["labels"],
                "nontrivial_label_count": report["nontrivial_labels"],
                "packets": report["packets"],
                "gamma_size": report["gamma_size"],
                "quotient_shift_count": report["quotient_shift_count"],
                "quotient_shift_support_distribution": report[
                    "quotient_shift_support_distribution"
                ],
                "carry_record_count": report["carry_record_count"],
                "carry_path_distribution": report["carry_path_distribution"],
            },
            "h3": compact_hyper(report.get("h3")),
            "h4": compact_hyper(report.get("h4")),
            "ext_ch": {
                "raw_atom_count": ext["raw_atom_count"],
                "raw_pair_count": ext["raw_pair_count"],
                "raw_coefficient_distribution": ext["raw_coefficient_distribution"],
                "raw_path_distribution": ext["raw_path_distribution"],
                "atom_orbit_count": None,
                "atom_orbit_size_distribution": None,
                "atom_orbit_missing_total": None,
                "pair_orbit_count": ext["canonical_pair_orbit_count"],
                "pair_orbit_size_distribution": ext["pair_orbit_size_distribution"],
                "pair_orbit_missing_total": ext["pair_orbit_missing_total"],
                "full_block_coboundary": compact_coboundary(
                    ext.get("full_block_coboundary")
                ),
                "support_projection_coboundary": compact_coboundary(
                    ext.get("support_projection_coboundary")
                ),
            },
            "fisher_jet_shadow": {
                "support_projection": compact_coboundary(
                    ext.get("support_projection_coboundary")
                ),
                "k_ch": {
                    "status": (
                        "not extracted in this first classifier; the row is "
                        "classified at filtered and raw-support projection level"
                    )
                },
                "representative_probe": report.get("fisher_probe"),
            },
            "sources": [str(path)],
        }
    )


def compact_hyper(item: dict[str, Any] | None) -> dict[str, Any] | None:
    if item is None:
        return None
    return {
        "cells": item.get("cells"),
        "orbits": item.get("orbits"),
        "family_orbit_counts": item.get("family_orbit_counts"),
        "orbit_size_distribution": item.get("orbit_size_distribution"),
        "signature_collisions": item.get("signature_collisions"),
    }


def control_row(row_key: str, factory: Callable[[], FiniteLocalRing]) -> dict[str, Any]:
    constructor = LocalAdjacencyConstructor(factory())
    reducer = CocycleReducer(constructor)
    atoms = reducer.raw_atoms()
    atom_orbits = reducer.atom_orbits()
    pair_orbits = reducer.pair_orbits()
    full = reducer.coboundary_reduction("full_block")
    support = reducer.coboundary_reduction("support", c2_scope="raw_support")
    constructor_summary = constructor.summary()
    mixed_packet_count = 0
    packets = list(constructor.packets.values())
    for left_index, left in enumerate(packets):
        for right in packets[left_index + 1 :]:
            mixed_packet_count += len(left) * len(right)

    k_ch_status = (
        "zero conductor-mixed mode pairs; K_CH mixed-conductor shadow is empty"
        if mixed_packet_count == 0
        else "not extracted in this first classifier; use as pure wild control"
    )
    return finalize_row(
        {
            "row_key": row_key,
            "row_role": "computable control",
            "ring": constructor.ring.name,
            "constructor": constructor_summary,
            "h3": cell_orbit_summary(constructor, 3),
            "h4": cell_orbit_summary(constructor, 4),
            "ext_ch": {
                "raw_atom_count": len(atoms),
                "raw_pair_count": len({atom.pair_key for atom in atoms}),
                "raw_coefficient_distribution": counter_json(
                    Counter(atom.coefficient for atom in atoms)
                ),
                "raw_path_distribution": dict(
                    sorted(Counter(atom.path_word for atom in atoms).items())
                ),
                "atom_orbit_count": len(atom_orbits),
                "atom_orbit_size_distribution": dict(
                    sorted(Counter(int(orbit["size"]) for orbit in atom_orbits).items())
                ),
                "atom_orbit_missing_total": sum(
                    int(orbit["missing"]) for orbit in atom_orbits
                ),
                "pair_orbit_count": len(pair_orbits),
                "pair_orbit_size_distribution": dict(
                    sorted(Counter(int(orbit["size"]) for orbit in pair_orbits).items())
                ),
                "pair_orbit_missing_total": sum(
                    int(orbit["missing"]) for orbit in pair_orbits
                ),
                "full_block_coboundary": compact_coboundary(full),
                "support_projection_coboundary": compact_coboundary(support),
            },
            "fisher_jet_shadow": {
                "support_projection": compact_coboundary(support),
                "k_ch": {
                    "status": k_ch_status,
                    "conductor_mixed_mode_pairs": mixed_packet_count,
                },
                "representative_probe": fisher_probe(constructor),
            },
            "sources": ["computed from local_adjacency_constructor.py"],
        }
    )


def finalize_row(row: dict[str, Any]) -> dict[str, Any]:
    ext = row["ext_ch"]
    full = ext.get("full_block_coboundary")
    support = ext.get("support_projection_coboundary")
    row["classification"] = support_erasure_summary(full=full, support=support)
    row["nonzero_filtered_class_certified"] = bool(
        row["classification"]["full_filtered_residual"]
        and row["classification"]["full_filtered_residual"] > 0
    )
    row["support_projection_erases_class"] = bool(
        row["nonzero_filtered_class_certified"]
        and row["classification"]["support_projection_residual"] == 0
    )
    return row


def build_payload(row_keys: list[str]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for row_key in row_keys:
        if row_key == "f4-u2":
            rows.append(f4_row())
        elif row_key == "f2-u5":
            rows.append(next_row_from_report(row_key, F2_U5_JSON))
        elif row_key == "f8-u2":
            rows.append(next_row_from_report(row_key, F8_U2_JSON))
        elif row_key in CONTROL_FACTORIES:
            rows.append(control_row(row_key, CONTROL_FACTORIES[row_key]))
        else:
            raise ValueError(f"unknown row key: {row_key}")

    return {
        "classification_problem": {
            "nonzero_question": "Which finite local rows have [kappa_R] != 0?",
            "criterion": (
                "A measured row is classified nonzero when the full-block "
                "section-change reducer has residual_support > 0."
            ),
            "kernel_question": (
                "For a chosen Fisher/support projection J, which part of the "
                "full filtered residual is erased by ker J?"
            ),
            "visible_support_question": (
                "Record support-projection visibility for every row, and "
                "record K_CH/higher-arity shadows only where the exact "
                "Fisher-jet lift has been extracted."
            ),
        },
        "projection_convention": {
            "support_projection": (
                "raw-support C2 quotient with support section changes; this "
                "is a support-level Fisher-jet quotient, not by itself the "
                "K_CH commutator detector"
            ),
            "k_ch": (
                "antisymmetric cubic Fisher commutator shadow; currently "
                "complete here for F4[u]/(u^2) through the arity-4 lift"
            ),
        },
        "rows": rows,
        "nonzero_rows": [
            row["row_key"] for row in rows if row["nonzero_filtered_class_certified"]
        ],
        "support_projection_kernel_rows": [
            row["row_key"] for row in rows if row["support_projection_erases_class"]
        ],
        "fc1_implications": [
            (
                "Normalizer pair-orbits, carry paths, conductor packet sizes, "
                "and H3/H4 family orbits are natural row invariants for the "
                "FC1 macrovariable census."
            ),
            (
                "Rows with identical visible support residuals can still have "
                "different filtered carry mass and orbit decompositions; FC1 "
                "should include full filtered orbit data, not support closure alone."
            ),
        ],
        "fc3_implications": [
            (
                "The information-investment functional must charge full "
                "filtered residual separately from support-projection closure."
            ),
            (
                "Projection-specific kernels identify which carry residuals "
                "can enter a visible cost term and which remain hidden unless "
                "a richer K_CH or higher-arity Fisher-jet channel is used."
            ),
        ],
    }


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# FC2 Row Classification",
        "",
        "This is the first row-level classifier after the FC2 source theorem.",
        "It treats `[kappa_R]` as the solved filtered section class and classifies",
        "which finite rows are nonzero, what the raw-support projection erases,",
        "and which Fisher-jet shadows are already explicitly extracted.",
        "",
        "## Classification Problem",
        "",
        f"- nonzero criterion: {payload['classification_problem']['criterion']}",
        f"- kernel question: {payload['classification_problem']['kernel_question']}",
        f"- visible support question: {payload['classification_problem']['visible_support_question']}",
        "",
        "The support projection below is not being identified with `K_CH`.",
        "It is a reproducible support-level quotient.  The `K_CH`/arity-4",
        "shadow is separately imported where it has an exact certificate.",
        "",
        "## Row Table",
        "",
        "| row | ring | role | raw atoms | raw pairs | pair orbits | full residual | support residual | erased by support | H3 | H4 | K_CH status |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in payload["rows"]:
        ext = row["ext_ch"]
        cls = row["classification"]
        h3 = row.get("h3") or {}
        h4 = row.get("h4") or {}
        kch = row["fisher_jet_shadow"]["k_ch"]
        if kch.get("k_ch_commutator_orbits") is not None:
            kch_status = (
                f"{kch['k_ch_commutator_orbits']} comm orbits; "
                f"H4 mixed {kch['mixed_h4_orbits_hit']}/{kch['mixed_h4_orbits_total']}"
            )
        else:
            kch_status = kch["status"]
        lines.append(
            "| "
            + " | ".join(
                [
                    row["row_key"],
                    row["ring"],
                    row["row_role"],
                    str(ext["raw_atom_count"]),
                    str(ext["raw_pair_count"]),
                    fmt(ext["pair_orbit_count"]),
                    fmt(cls["full_filtered_residual"]),
                    fmt(cls["support_projection_residual"]),
                    fmt(cls["support_projection_erased_from_full"]),
                    f"{fmt(h3.get('cells'))}/{fmt(h3.get('orbits'))}",
                    f"{fmt(h4.get('cells'))}/{fmt(h4.get('orbits'))}",
                    kch_status,
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Support-Kernel Reading",
        "",
    ]
    for row in payload["rows"]:
        cls = row["classification"]
        ratio = cls["support_projection_erasure_ratio"]
        ratio_text = "n/a" if ratio is None else f"{ratio:.3f}"
        lines.append(
            f"- `{row['row_key']}`: {cls['status']} "
            f"(erasure ratio `{ratio_text}`)."
        )

    lines += [
        "",
        "## Orbit Data",
        "",
        "| row | atom orbits | atom orbit sizes | pair orbit sizes | H3 families | H4 families |",
        "|---|---:|---|---|---|---|",
    ]
    for row in payload["rows"]:
        ext = row["ext_ch"]
        h3 = row.get("h3") or {}
        h4 = row.get("h4") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    row["row_key"],
                    fmt(ext.get("atom_orbit_count")),
                    fmt(ext.get("atom_orbit_size_distribution")),
                    fmt(ext.get("pair_orbit_size_distribution")),
                    fmt(h3.get("family_orbit_counts")),
                    fmt(h4.get("family_orbit_counts")),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Fisher-Jet Shadow Status",
        "",
    ]
    for row in payload["rows"]:
        shadow = row["fisher_jet_shadow"]
        probe = shadow.get("representative_probe")
        lines.append(f"### {row['row_key']}")
        lines.append("")
        lines.append(f"- support projection residual: `{fmt(row['classification']['support_projection_residual'])}`")
        kch = shadow["k_ch"]
        if kch.get("k_ch_commutator_orbits") is not None:
            lines.append(f"- K_CH commutator orbits: `{kch['k_ch_commutator_orbits']}`")
            lines.append(
                f"- lifted arity-4 commutator orbits: `{kch['lifted_commutator_orbits']}`"
            )
            lines.append(
                f"- H4 mixed/pure hit: `{kch['mixed_h4_orbits_hit']} / {kch['mixed_h4_orbits_total']}` mixed, "
                f"`{kch['pure_h4_orbits_hit']} / {kch['pure_h4_orbits_total']}` pure"
            )
        else:
            lines.append(f"- K_CH status: {kch['status']}")
        if probe:
            lines.append(
                "- representative Fisher probe: "
                f"`mixed_order2_support={probe['mixed_order2_support']}` "
                f"for modes `{probe['left_mode']}`, `{probe['right_mode']}`"
            )
        lines.append("")

    lines += [
        "## FC1/FC3 Handoff",
        "",
        "FC1 should now treat conductor packet sizes, carry path distributions,",
        "normalizer pair-orbits, and H3/H4 family orbits as candidate natural",
        "macrovariables.  The table shows why support closure alone is too coarse:",
        "every classified nonzero row can be erased by the raw-support projection.",
        "",
        "FC3 should score the full filtered residual separately from visible",
        "support residuals.  The projection kernel is not a nuisance term; it",
        "is the list of residual mass that a chosen information-investment",
        "functional cannot see unless it pays for a richer K_CH or higher-arity",
        "Fisher-jet channel.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows",
        default="f4-u2,f2-u5,f8-u2,f16-field,f2-u4-control",
        help=(
            "comma-separated row keys: f4-u2, f2-u5, f8-u2, "
            "f16-field, f2-u4-control"
        ),
    )
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    payload = build_payload(row_keys)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"Wrote {args.json}")
    print(f"Wrote {args.report}")


if __name__ == "__main__":
    main()
