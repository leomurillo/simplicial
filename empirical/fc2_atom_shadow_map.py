"""Coefficient-level atom map for the FC2 visible Fisher-shadow phase.

This classifier layer relates full filtered residual representatives to the
visible Fisher-shadow support without treating K_CH itself as an Ext_CH
detector.  For the current row atlas the full-block residual equals the raw
carry cochain, so raw cocycle atoms are valid full filtered residual
representatives.  Each atom is mapped to its closed H4 atom-boundary support

    (left_eta, right_eta, input, output)

and that H4 orbit is compared with the already certified input-side H4 image
of the Fisher commutator.  The result is an incidence table: support-erased
filtered atoms that are incident to a visible H4 Fisher-shadow orbit versus
support-erased atoms invisible to this tested channel.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter
from typing import Any

from cocycle_reducer import CocycleAtom, CocycleReducer
from fc2_visible_fisher_kernel import ROW_FACTORIES, counter_json, load_row_classification
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import Label, LocalAdjacencyConstructor


REPORT_DIR = Path(__file__).with_name("reports")
VISIBLE_JSON = REPORT_DIR / "fc2_visible_fisher_kernel.json"
DEFAULT_JSON = REPORT_DIR / "fc2_atom_shadow_map.json"
DEFAULT_MD = REPORT_DIR / "fc2_atom_shadow_map.md"

DEFAULT_ROWS = ("f4-u2", "f2-u5", "f8-u2", "f16-field", "f2-u4-control")


def load_visible_rows() -> dict[str, dict[str, Any]]:
    if not VISIBLE_JSON.exists():
        return {}
    payload = json.loads(VISIBLE_JSON.read_text(encoding="utf-8"))
    return {row["row_key"]: row for row in payload.get("rows", [])}


def label_text(constructor: LocalAdjacencyConstructor, label: Label) -> str:
    return constructor.ring.label_name(label)


def cell_text(constructor: LocalAdjacencyConstructor, cell: tuple[Label, ...]) -> str:
    return "(" + ", ".join(label_text(constructor, label) for label in cell) + ")"


def atom_text(constructor: LocalAdjacencyConstructor, atom: CocycleAtom) -> dict[str, str | int]:
    return {
        "left_eta": label_text(constructor, atom.left_eta),
        "right_eta": label_text(constructor, atom.right_eta),
        "path": atom.path_word,
        "output": label_text(constructor, atom.output),
        "input": label_text(constructor, atom.input),
        "coefficient": atom.coefficient,
    }


def atom_boundary_cell(atom: CocycleAtom) -> tuple[Label, Label, Label, Label]:
    return (atom.left_eta, atom.right_eta, atom.input, atom.output)


def visibility_ratio(visible: int, total: int) -> str:
    if total == 0:
        return "0/0"
    return f"{visible}/{total}"


def nested_visibility_rows(counter: dict[str, Counter[str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key in sorted(counter):
        counts = counter[key]
        total = int(counts["total"])
        visible = int(counts["visible"])
        rows.append(
            {
                "key": key,
                "total_atoms": total,
                "visible_h4_incident_atoms": visible,
                "h4_invisible_atoms": int(counts["invisible"]),
                "visible_fraction": visibility_ratio(visible, total),
            }
        )
    return rows


def row_projection_summary(row_key: str, row_classification: dict[str, dict[str, Any]]) -> dict[str, Any]:
    row = row_classification.get(row_key, {})
    ext = row.get("ext_ch", {})
    full = ext.get("full_block_coboundary") or {}
    support = ext.get("support_projection_coboundary") or {}
    classification = row.get("classification") or {}
    return {
        "full_filtered_residual": classification.get("full_filtered_residual")
        or full.get("residual_support"),
        "support_projection_residual": classification.get("support_projection_residual")
        or support.get("residual_support"),
        "support_projection_erases_class": row.get("support_projection_erases_class"),
        "full_block_residual_equal_raw": full.get("residual_equal_raw"),
        "raw_atom_count": ext.get("raw_atom_count"),
        "raw_coefficient_distribution": ext.get("raw_coefficient_distribution"),
        "raw_path_distribution": ext.get("raw_path_distribution"),
    }


def visible_h4_image(row_key: str, visible_rows: dict[str, dict[str, Any]]) -> dict[int, dict[str, Any]]:
    row = visible_rows.get(row_key, {})
    shadow = row.get("visible_shadow") or {}
    if shadow.get("status") != "exact":
        return {}
    lift = shadow.get("input_side_h4_lift") or {}
    return {
        int(image["h4_orbit"]): image
        for image in lift.get("h4_orbit_image_table", [])
    }


def representative_samples(
    constructor: LocalAdjacencyConstructor,
    samples: list[tuple[CocycleAtom, int, str]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for atom, h4_orbit, family in samples:
        rows.append(
            {
                **atom_text(constructor, atom),
                "atom_boundary_h4_cell": cell_text(constructor, atom_boundary_cell(atom)),
                "atom_boundary_h4_orbit": h4_orbit,
                "atom_boundary_h4_family": family,
            }
        )
    return rows


def analyze_row(
    row_key: str,
    *,
    row_classification: dict[str, dict[str, Any]],
    visible_rows: dict[str, dict[str, Any]],
    sample_atoms: int,
) -> dict[str, Any]:
    started = perf_counter()
    ring = ROW_FACTORIES[row_key]()
    constructor = LocalAdjacencyConstructor(ring)
    reducer = CocycleReducer(constructor)

    atom_started = perf_counter()
    atoms = reducer.raw_atoms()
    atom_elapsed = perf_counter() - atom_started

    h4_started = perf_counter()
    tower = HyperAdjacencyTower(constructor)
    cell_to_h4_orbit, h4_rows = tower.orbit_maps(4)
    h4_elapsed = perf_counter() - h4_started

    visible_image = visible_h4_image(row_key, visible_rows)
    visible_h4_orbits = set(visible_image)
    projection = row_projection_summary(row_key, row_classification)

    total_atoms = 0
    visible_atoms = 0
    invisible_atoms = 0
    non_h4_atoms = 0
    nonclosed_atoms = 0
    coefficient_visibility: dict[str, Counter[str]] = defaultdict(Counter)
    path_visibility: dict[str, Counter[str]] = defaultdict(Counter)
    family_visibility: dict[str, Counter[str]] = defaultdict(Counter)
    h4_orbit_atom_counts: Counter[int] = Counter()
    visible_h4_orbit_atom_counts: Counter[int] = Counter()
    invisible_h4_orbit_atom_counts: Counter[int] = Counter()
    visible_samples: list[tuple[CocycleAtom, int, str]] = []
    invisible_samples: list[tuple[CocycleAtom, int, str]] = []
    non_h4_samples: list[dict[str, Any]] = []

    for atom in atoms:
        total_atoms += 1
        cell = atom_boundary_cell(atom)
        coefficient_key = str(atom.coefficient)
        path_key = atom.path_word
        if any(label == constructor.ring.zero for label in cell):
            non_h4_atoms += 1
            if len(non_h4_samples) < sample_atoms:
                non_h4_samples.append(
                    {
                        **atom_text(constructor, atom),
                        "atom_boundary_cell": cell_text(constructor, cell),
                        "reason": "zero label in atom-boundary cell",
                    }
                )
            continue
        if constructor.ring.add_many(cell) != constructor.ring.zero:
            nonclosed_atoms += 1
            if len(non_h4_samples) < sample_atoms:
                non_h4_samples.append(
                    {
                        **atom_text(constructor, atom),
                        "atom_boundary_cell": cell_text(constructor, cell),
                        "reason": "atom-boundary cell is not closed",
                    }
                )
            continue

        h4_orbit = cell_to_h4_orbit[cell]
        family = str(h4_rows[h4_orbit]["family"])
        h4_orbit_atom_counts[h4_orbit] += 1
        is_visible = h4_orbit in visible_h4_orbits
        bucket = "visible" if is_visible else "invisible"
        if is_visible:
            visible_atoms += 1
            visible_h4_orbit_atom_counts[h4_orbit] += 1
            if len(visible_samples) < sample_atoms:
                visible_samples.append((atom, h4_orbit, family))
        else:
            invisible_atoms += 1
            invisible_h4_orbit_atom_counts[h4_orbit] += 1
            if len(invisible_samples) < sample_atoms:
                invisible_samples.append((atom, h4_orbit, family))

        for counter in (
            coefficient_visibility[coefficient_key],
            path_visibility[path_key],
            family_visibility[family],
        ):
            counter["total"] += 1
            counter[bucket] += 1

    h4_orbit_rows = []
    for h4_orbit, count in sorted(h4_orbit_atom_counts.items()):
        row = h4_rows[h4_orbit]
        image = visible_image.get(h4_orbit)
        h4_orbit_rows.append(
            {
                "h4_orbit": h4_orbit,
                "family": row["family"],
                "representative": row["representative"],
                "h4_orbit_size": row["size"],
                "atom_count": int(count),
                "visible_h4_incident": image is not None,
                "h2_commutator_orbits": 0 if image is None else image["h2_commutator_orbits"],
                "k_ch_entry_hits": 0 if image is None else image["entry_hits"],
            }
        )

    visible_h4_rows = [row for row in h4_orbit_rows if row["visible_h4_incident"]]
    invisible_h4_rows = [row for row in h4_orbit_rows if not row["visible_h4_incident"]]

    return {
        "row_key": row_key,
        "ring": constructor.ring.name,
        "label_count": len(constructor.ring.labels),
        "gamma_size": len(constructor.ring.normalizer_actions),
        "projection_summary": projection,
        "classification_convention": {
            "residual_representative_basis": (
                "raw cocycle atoms, valid for this row only when "
                "full_block_residual_equal_raw is true"
            ),
            "atom_boundary_h4_cell": "(left_eta, right_eta, input, output)",
            "visible_condition": (
                "atom-boundary H4 orbit belongs to the input-side H4 image of "
                "the exact Fisher K_CH commutator shadow"
            ),
            "non_detection_warning": (
                "visible_h4_incident is an H4-support incidence flag, not an "
                "Ext_CH detection theorem for K_CH"
            ),
        },
        "visible_fisher_shadow": {
            "status": (visible_rows.get(row_key, {}).get("visible_shadow") or {}).get("status"),
            "k_ch_commutator_orbits": (
                (visible_rows.get(row_key, {}).get("visible_shadow") or {}).get(
                    "commutator_orbits"
                )
            ),
            "input_side_h4_orbits_hit": len(visible_h4_orbits),
            "visible_h4_orbits": sorted(visible_h4_orbits),
        },
        "atom_accounting": {
            "raw_residual_atoms": total_atoms,
            "h4_boundary_atoms": total_atoms - non_h4_atoms - nonclosed_atoms,
            "visible_h4_incident_atoms": visible_atoms,
            "h4_invisible_atoms": invisible_atoms,
            "non_h4_boundary_atoms": non_h4_atoms,
            "nonclosed_boundary_atoms": nonclosed_atoms,
            "visible_fraction": visibility_ratio(visible_atoms, total_atoms),
            "support_erased_visible_h4_incident_atoms": (
                visible_atoms if projection.get("support_projection_residual") == 0 else None
            ),
            "support_erased_h4_invisible_atoms": (
                invisible_atoms if projection.get("support_projection_residual") == 0 else None
            ),
        },
        "coefficient_visibility": nested_visibility_rows(coefficient_visibility),
        "path_visibility": nested_visibility_rows(path_visibility),
        "atom_boundary_h4_family_visibility": nested_visibility_rows(family_visibility),
        "visible_h4_orbit_atom_counts": visible_h4_rows,
        "h4_invisible_orbit_atom_counts_sample": sorted(
            invisible_h4_rows,
            key=lambda row: (-int(row["atom_count"]), int(row["h4_orbit"])),
        )[:20],
        "representative_visible_atoms_sample": representative_samples(
            constructor, visible_samples
        ),
        "representative_h4_invisible_atoms_sample": representative_samples(
            constructor, invisible_samples
        ),
        "non_h4_boundary_atoms_sample": non_h4_samples,
        "timing_seconds": {
            "raw_atoms": round(atom_elapsed, 3),
            "h4_orbits": round(h4_elapsed, 3),
            "total": round(perf_counter() - started, 3),
        },
    }


def build_payload(row_keys: tuple[str, ...], sample_atoms: int) -> dict[str, Any]:
    row_classification = load_row_classification()
    visible_rows = load_visible_rows()
    rows = [
        analyze_row(
            row_key,
            row_classification=row_classification,
            visible_rows=visible_rows,
            sample_atoms=sample_atoms,
        )
        for row_key in row_keys
    ]
    return {
        "classification_layer": "FC2 coefficient-level atom to visible Fisher-shadow H4 incidence",
        "source_theorem_status": (
            "FC2 source theorem is treated as solved; this report classifies "
            "how the full filtered residual representatives meet the tested "
            "visible H4 Fisher-shadow channel"
        ),
        "projection_conventions": {
            "full_filtered_residual": (
                "full-block section-change residual from fc2_row_classifier; "
                "for current rows residual_equal_raw=true, so raw atoms are "
                "the coefficient-level residual representatives"
            ),
            "raw_support_projection": (
                "support residual 0 is kernel/erasure in that projection, not "
                "filtered triviality"
            ),
            "k_ch": (
                "K_CH remains a Fisher-jet shadow of [kappa].  The atom map "
                "uses only the input-side H4 image of K_CH as a visible support "
                "incidence channel, not as an Ext_CH detector by itself"
            ),
        },
        "rows": rows,
    }


def format_summary_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| row | full residual atoms | support residual | K_CH orbits | visible H4 orbits | atom-boundary visible | atom-boundary invisible | timing |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        accounting = row["atom_accounting"]
        projection = row["projection_summary"]
        shadow = row["visible_fisher_shadow"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['row_key']}`",
                    str(accounting["raw_residual_atoms"]),
                    str(projection["support_projection_residual"]),
                    str(shadow["k_ch_commutator_orbits"]),
                    str(shadow["input_side_h4_orbits_hit"]),
                    str(accounting["visible_h4_incident_atoms"]),
                    str(accounting["h4_invisible_atoms"]),
                    str(row["timing_seconds"]["total"]),
                ]
            )
            + " |"
        )
    return lines


def format_visibility_table(rows: list[dict[str, Any]], key_header: str) -> list[str]:
    lines = [
        f"| {key_header} | total atoms | visible H4 incident | H4 invisible | visible fraction |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['key']}`",
                    str(row["total_atoms"]),
                    str(row["visible_h4_incident_atoms"]),
                    str(row["h4_invisible_atoms"]),
                    f"`{row['visible_fraction']}`",
                ]
            )
            + " |"
        )
    return lines


def format_h4_orbit_table(rows: list[dict[str, Any]], *, limit: int | None = None) -> list[str]:
    shown = rows if limit is None else rows[:limit]
    lines = [
        "| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |",
        "|---:|---|---:|---:|---:|---|",
    ]
    for row in shown:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["h4_orbit"]),
                    str(row["family"]),
                    str(row["atom_count"]),
                    str(row["h2_commutator_orbits"]),
                    str(row["k_ch_entry_hits"]),
                    "`" + str(row["representative"]) + "`",
                ]
            )
            + " |"
        )
    return lines


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# FC2 Coefficient-Level Atom Shadow Map",
        "",
        "This report maps full filtered residual representatives to the visible",
        "input-side H4 Fisher-shadow support.  It is an incidence classifier:",
        "`visible_h4_incident` means the atom-boundary H4 orbit is in the",
        "already certified H4 image of the `K_CH` commutator shadow.  It does",
        "not make `K_CH` a standalone `Ext_CH` detector.",
        "",
        "Because the current row atlas has `full_block_residual_equal_raw=true`,",
        "the raw carry atoms are used here as coefficient-level representatives",
        "of the full filtered residual.",
        "",
        "## Summary",
        "",
        *format_summary_table(payload["rows"]),
        "",
    ]

    for row in payload["rows"]:
        accounting = row["atom_accounting"]
        projection = row["projection_summary"]
        shadow = row["visible_fisher_shadow"]
        lines += [
            f"## {row['row_key']}",
            "",
            f"- ring: `{row['ring']}`",
            f"- full residual atoms: `{accounting['raw_residual_atoms']}`",
            f"- full residual equals raw cochain: `{projection['full_block_residual_equal_raw']}`",
            f"- support projection residual: `{projection['support_projection_residual']}`",
            f"- K_CH commutator orbits: `{shadow['k_ch_commutator_orbits']}`",
            f"- input-side H4 orbits hit by K_CH: `{shadow['input_side_h4_orbits_hit']}`",
            f"- atom-boundary visible/invisible: `{accounting['visible_h4_incident_atoms']} / {accounting['h4_invisible_atoms']}`",
            f"- non-H4 or nonclosed atom boundaries: `{accounting['non_h4_boundary_atoms']} / {accounting['nonclosed_boundary_atoms']}`",
            "",
            "Path visibility:",
            "",
            *format_visibility_table(row["path_visibility"], "carry path"),
            "",
            "Atom-boundary H4 family visibility:",
            "",
            *format_visibility_table(row["atom_boundary_h4_family_visibility"], "H4 family"),
            "",
            "Visible H4 orbit atom counts:",
            "",
            *format_h4_orbit_table(row["visible_h4_orbit_atom_counts"]),
            "",
        ]
        invisible_sample = row["h4_invisible_orbit_atom_counts_sample"]
        if invisible_sample:
            lines += [
                "Largest H4-invisible atom-boundary orbits under this channel:",
                "",
                *format_h4_orbit_table(invisible_sample, limit=12),
                "",
            ]

    lines += [
        "## FC1/FC3 Implications",
        "",
        "For FC1, the natural row macrovariables now include atom-boundary H4",
        "family incidence, visible H4 orbit atom mass, and the split between",
        "support-erased atoms incident to the Fisher-shadow image and atoms",
        "invisible to the tested Fisher-jet channel.",
        "",
        "For FC3, the cost split is explicit: full filtered residual mass can be",
        "support-erased while still having a nonzero visible H4-shadow incidence",
        "component.  The remaining H4-invisible atoms are the next target for",
        "richer Fisher-jet or coefficient-shadow observables.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rows",
        nargs="+",
        default=list(DEFAULT_ROWS),
        choices=sorted(ROW_FACTORIES),
        help="row keys to analyze",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=DEFAULT_JSON,
        help="JSON report path",
    )
    parser.add_argument(
        "--md",
        type=Path,
        default=DEFAULT_MD,
        help="Markdown report path",
    )
    parser.add_argument(
        "--sample-atoms",
        type=int,
        default=8,
        help="representative atom samples per visible/invisible bucket",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload(tuple(args.rows), args.sample_atoms)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    args.md.write_text(render_markdown(payload), encoding="utf-8")
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
