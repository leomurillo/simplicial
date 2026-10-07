"""H4-invisible contraction-shadow classifier for FC2 atom maps.

This experiment refines the coefficient-level atom map without treating K_CH
as an Ext_CH detector.  Starting from the exact input-side H4 image of the
visible Fisher commutator, it contracts those H4 cells to H3 and asks whether
atom-boundary H4 cells that were invisible at H4 become visible after the
H4-to-H3 support projection.

The result is a projection-shadow diagnostic.  H3-contraction visibility is
weaker than H4 incidence and is recorded as additional erasure/refinement,
not as filtered closure and not as Ext_CH detection.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from time import perf_counter
from typing import Any

from cocycle_reducer import CocycleAtom, CocycleReducer
from fc2_atom_shadow_map import atom_boundary_cell, visible_h4_image
from fc2_visible_fisher_kernel import ROW_FACTORIES, counter_json
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import Label, LocalAdjacencyConstructor


REPORT_DIR = Path(__file__).with_name("reports")
VISIBLE_JSON = REPORT_DIR / "fc2_visible_fisher_kernel.json"
DEFAULT_JSON = REPORT_DIR / "fc2_h4_contraction_shadow.json"
DEFAULT_MD = REPORT_DIR / "fc2_h4_contraction_shadow.md"
DEFAULT_ROWS = ("f4-u2", "f2-u5", "f8-u2", "f16-field", "f2-u4-control")
PAIR_POSITIONS = tuple(combinations(range(4), 2))


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


def visibility_rows(counter: dict[str, Counter[str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key in sorted(counter):
        item = counter[key]
        total = int(item["h4_invisible_atoms"])
        h3_visible = int(item["h3_contraction_visible_atoms"])
        rows.append(
            {
                "key": key,
                "h4_invisible_atoms": total,
                "h3_contraction_visible_atoms": h3_visible,
                "remaining_invisible_atoms": int(item["remaining_invisible_atoms"]),
                "h3_contraction_visible_fraction": (
                    "0/0" if total == 0 else f"{h3_visible}/{total}"
                ),
            }
        )
    return rows


def contracted_h3_orbits(
    tower: HyperAdjacencyTower,
    cell: tuple[Label, Label, Label, Label],
    cell_to_h3_orbit: dict[tuple[Label, ...], int],
) -> tuple[tuple[int, str], ...]:
    rows: list[tuple[int, str]] = []
    for left, right in PAIR_POSITIONS:
        contracted = tower.contract_pair(cell, (left, right))
        if contracted is None:
            continue
        rows.append((cell_to_h3_orbit[contracted], f"{left}{right}"))
    return tuple(rows)


def visible_h3_shadow_from_h4_image(
    tower: HyperAdjacencyTower,
    *,
    cell_to_h4_orbit: dict[tuple[Label, ...], int],
    cell_to_h3_orbit: dict[tuple[Label, ...], int],
    visible_h4_orbits: set[int],
) -> tuple[set[int], Counter[str], Counter[int]]:
    h3_orbits: set[int] = set()
    pair_positions: Counter[str] = Counter()
    h3_hits: Counter[int] = Counter()
    for cell, h4_orbit in cell_to_h4_orbit.items():
        if h4_orbit not in visible_h4_orbits:
            continue
        for h3_orbit, pair_position in contracted_h3_orbits(
            tower, cell, cell_to_h3_orbit
        ):
            h3_orbits.add(h3_orbit)
            h3_hits[h3_orbit] += 1
            pair_positions[pair_position] += 1
    return h3_orbits, pair_positions, h3_hits


def representative_samples(
    constructor: LocalAdjacencyConstructor,
    samples: list[tuple[CocycleAtom, int, tuple[int, ...]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for atom, h4_orbit, h3_orbits in samples:
        rows.append(
            {
                **atom_text(constructor, atom),
                "atom_boundary_h4_cell": cell_text(constructor, atom_boundary_cell(atom)),
                "atom_boundary_h4_orbit": h4_orbit,
                "visible_h3_orbits": list(h3_orbits),
            }
        )
    return rows


def analyze_row(
    row_key: str,
    *,
    visible_rows: dict[str, dict[str, Any]],
    sample_atoms: int,
) -> dict[str, Any]:
    started = perf_counter()
    constructor = LocalAdjacencyConstructor(ROW_FACTORIES[row_key]())
    reducer = CocycleReducer(constructor)

    atom_started = perf_counter()
    atoms = reducer.raw_atoms()
    atom_elapsed = perf_counter() - atom_started

    tower = HyperAdjacencyTower(constructor)
    h3_started = perf_counter()
    cell_to_h3_orbit, h3_rows = tower.orbit_maps(3)
    h3_elapsed = perf_counter() - h3_started

    h4_started = perf_counter()
    cell_to_h4_orbit, h4_rows = tower.orbit_maps(4)
    h4_elapsed = perf_counter() - h4_started

    visible_image = visible_h4_image(row_key, visible_rows)
    visible_h4_orbits = set(visible_image)
    visible_h3_orbits, visible_h3_pair_positions, visible_h3_hit_counts = (
        visible_h3_shadow_from_h4_image(
            tower,
            cell_to_h4_orbit=cell_to_h4_orbit,
            cell_to_h3_orbit=cell_to_h3_orbit,
            visible_h4_orbits=visible_h4_orbits,
        )
    )

    h4_visible_atoms = 0
    h4_invisible_atoms = 0
    h3_contraction_visible_atoms = 0
    remaining_invisible_atoms = 0
    atom_pair_positions: Counter[str] = Counter()
    atom_visible_h3_hits: Counter[int] = Counter()
    family_counter: dict[str, Counter[str]] = defaultdict(Counter)
    path_counter: dict[str, Counter[str]] = defaultdict(Counter)
    h3_visible_samples: list[tuple[CocycleAtom, int, tuple[int, ...]]] = []
    remaining_samples: list[tuple[CocycleAtom, int, tuple[int, ...]]] = []

    for atom in atoms:
        cell = atom_boundary_cell(atom)
        h4_orbit = cell_to_h4_orbit[cell]
        if h4_orbit in visible_h4_orbits:
            h4_visible_atoms += 1
            continue

        h4_invisible_atoms += 1
        family = str(h4_rows[h4_orbit]["family"])
        visible_hits: set[int] = set()
        for h3_orbit, pair_position in contracted_h3_orbits(
            tower, cell, cell_to_h3_orbit
        ):
            if h3_orbit not in visible_h3_orbits:
                continue
            visible_hits.add(h3_orbit)
            atom_visible_h3_hits[h3_orbit] += 1
            atom_pair_positions[pair_position] += 1

        bucket = (
            "h3_contraction_visible_atoms"
            if visible_hits
            else "remaining_invisible_atoms"
        )
        if visible_hits:
            h3_contraction_visible_atoms += 1
            if len(h3_visible_samples) < sample_atoms:
                h3_visible_samples.append((atom, h4_orbit, tuple(sorted(visible_hits))))
        else:
            remaining_invisible_atoms += 1
            if len(remaining_samples) < sample_atoms:
                remaining_samples.append((atom, h4_orbit, ()))

        for counter in (family_counter[family], path_counter[atom.path_word]):
            counter["h4_invisible_atoms"] += 1
            counter[bucket] += 1

    visible_h3_table = [
        {
            "h3_orbit": h3_orbit,
            "family": h3_rows[h3_orbit]["family"],
            "representative": h3_rows[h3_orbit]["representative"],
            "h3_orbit_size": h3_rows[h3_orbit]["size"],
            "visible_h4_image_contraction_hits": int(visible_h3_hit_counts[h3_orbit]),
            "h4_invisible_atom_contraction_hits": int(atom_visible_h3_hits[h3_orbit]),
        }
        for h3_orbit in sorted(visible_h3_orbits)
    ]

    return {
        "row_key": row_key,
        "ring": constructor.ring.name,
        "classification_convention": {
            "source": (
                "visible H3 shadow generated by pair-contractions of the exact "
                "input-side H4 image of K_CH"
            ),
            "test": (
                "an H4-invisible residual atom is H3-contraction-visible when "
                "at least one pair contraction of its atom-boundary H4 cell "
                "lands in that generated H3 shadow"
            ),
            "non_detection_warning": (
                "H3-contraction visibility is a support projection, not "
                "filtered closure and not K_CH as an Ext_CH detector"
            ),
        },
        "visible_h4_shadow": {
            "visible_h4_orbits": sorted(visible_h4_orbits),
            "visible_h4_orbit_count": len(visible_h4_orbits),
        },
        "visible_h3_shadow": {
            "visible_h3_orbits": sorted(visible_h3_orbits),
            "visible_h3_orbit_count": len(visible_h3_orbits),
            "pair_position_hits_from_visible_h4_image": counter_json(
                visible_h3_pair_positions
            ),
            "visible_h3_orbit_table": visible_h3_table,
        },
        "atom_accounting": {
            "raw_residual_atoms": len(atoms),
            "h4_visible_atoms": h4_visible_atoms,
            "h4_invisible_atoms": h4_invisible_atoms,
            "h4_invisible_h3_contraction_visible_atoms": h3_contraction_visible_atoms,
            "remaining_invisible_atoms": remaining_invisible_atoms,
            "accounting_check": (
                h4_visible_atoms
                + h3_contraction_visible_atoms
                + remaining_invisible_atoms
            ),
        },
        "h4_invisible_family_visibility": visibility_rows(family_counter),
        "h4_invisible_path_visibility": visibility_rows(path_counter),
        "h3_visible_pair_positions_from_atoms": counter_json(atom_pair_positions),
        "representative_h3_contraction_visible_atoms_sample": representative_samples(
            constructor, h3_visible_samples
        ),
        "representative_remaining_invisible_atoms_sample": representative_samples(
            constructor, remaining_samples
        ),
        "timing_seconds": {
            "raw_atoms": round(atom_elapsed, 3),
            "h3_orbits": round(h3_elapsed, 3),
            "h4_orbits": round(h4_elapsed, 3),
            "total": round(perf_counter() - started, 3),
        },
    }


def build_payload(row_keys: tuple[str, ...], sample_atoms: int) -> dict[str, Any]:
    visible_rows = load_visible_rows()
    rows = [
        analyze_row(row_key, visible_rows=visible_rows, sample_atoms=sample_atoms)
        for row_key in row_keys
    ]
    return {
        "classification_layer": "FC2 H4-invisible atom contraction shadow",
        "source_theorem_status": (
            "FC2 source theorem is treated as solved; this experiment refines "
            "visible support projections of already classified residual atoms"
        ),
        "projection_conventions": {
            "h4_visible": (
                "atom-boundary H4 orbit lies in the input-side H4 image of the "
                "visible K_CH Fisher shadow"
            ),
            "h3_contraction_visible": (
                "atom-boundary H4 orbit is not H4-visible, but at least one "
                "H4-to-H3 contraction lands in the contraction shadow of that "
                "visible H4 image"
            ),
            "warning": (
                "Both channels are support projections.  Neither replaces the "
                "full filtered residual or makes K_CH an Ext_CH detector."
            ),
        },
        "rows": rows,
    }


def format_summary(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| row | raw atoms | H4-visible | H4-invisible | H3-contraction visible from H4-invisible | remaining invisible | visible H3 orbits | timing |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        accounting = row["atom_accounting"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['row_key']}`",
                    str(accounting["raw_residual_atoms"]),
                    str(accounting["h4_visible_atoms"]),
                    str(accounting["h4_invisible_atoms"]),
                    str(accounting["h4_invisible_h3_contraction_visible_atoms"]),
                    str(accounting["remaining_invisible_atoms"]),
                    str(row["visible_h3_shadow"]["visible_h3_orbit_count"]),
                    str(row["timing_seconds"]["total"]),
                ]
            )
            + " |"
        )
    return lines


def format_visibility_table(rows: list[dict[str, Any]], key_header: str) -> list[str]:
    lines = [
        f"| {key_header} | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['key']}`",
                    str(row["h4_invisible_atoms"]),
                    str(row["h3_contraction_visible_atoms"]),
                    str(row["remaining_invisible_atoms"]),
                    f"`{row['h3_contraction_visible_fraction']}`",
                ]
            )
            + " |"
        )
    return lines


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# FC2 H4-Invisible Atom Contraction Shadow",
        "",
        "This experiment starts from the exact input-side H4 Fisher-shadow image",
        "and contracts it to H3.  It then asks which atom-boundary H4 cells that",
        "were invisible at H4 become visible after the same H4-to-H3 support",
        "projection.",
        "",
        "This is a projection-shadow diagnostic only.  It does not claim support",
        "closure, and it does not make `K_CH` an `Ext_CH` detector.",
        "",
        "## Summary",
        "",
        *format_summary(payload["rows"]),
        "",
    ]
    for row in payload["rows"]:
        accounting = row["atom_accounting"]
        lines += [
            f"## {row['row_key']}",
            "",
            f"- ring: `{row['ring']}`",
            f"- H4-visible atoms: `{accounting['h4_visible_atoms']}`",
            f"- H4-invisible atoms entering this refinement: `{accounting['h4_invisible_atoms']}`",
            f"- H3-contraction visible atoms: `{accounting['h4_invisible_h3_contraction_visible_atoms']}`",
            f"- remaining invisible atoms: `{accounting['remaining_invisible_atoms']}`",
            f"- visible H3 orbits generated from K_CH H4 image: `{row['visible_h3_shadow']['visible_h3_orbit_count']}`",
            "",
            "H4-invisible family refinement:",
            "",
            *format_visibility_table(row["h4_invisible_family_visibility"], "H4 family"),
            "",
            "H4-invisible path refinement:",
            "",
            *format_visibility_table(row["h4_invisible_path_visibility"], "carry path"),
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
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    parser.add_argument("--sample-atoms", type=int, default=8)
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
