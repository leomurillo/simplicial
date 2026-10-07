"""Balanced leakage census for saved local-ring Ext_CH rows.

This script reads the finite local-row reports produced by
verify_next_local_row.py and compute_ext_ch_cocycle.py.  It does not
recompute the ring constructors.  For each nonempty conductor packet subset
S, it treats canonical carry orbits with source,middle in S as active and
counts leakage when the target conductor lies outside S.

The reported balanced leakage is the active leaking carry mass divided by
active carry mass, multiplied by the full-block residual survival ratio from
the saved coboundary/Mittag-Leffler reducer.  It is a finite support-level
proxy for the Theorem 14.13 time-average budget.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"

DEFAULT_INPUTS = [
    REPORTS / "ext_ch_cocycle_f4_u2.json",
    REPORTS / "next_local_row_f2_u2.json",
    REPORTS / "next_local_row_f2_u3.json",
    REPORTS / "next_local_row_f2_u4.json",
    REPORTS / "next_local_row_f2_u5.json",
    REPORTS / "next_local_row_f8_u2.json",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def conductor_sort_key(name: str) -> tuple[int, str]:
    if name == "u":
        return (1, name)
    if name.startswith("u^"):
        try:
            return (int(name[2:]), name)
        except ValueError:
            pass
    return (999, name)


def path_parts(path: str) -> tuple[str, str, str]:
    parts = tuple(part.strip() for part in path.split("->"))
    if len(parts) != 3:
        raise ValueError(f"expected source->middle->target path, got {path!r}")
    return parts  # type: ignore[return-value]


def ratio(reduction: dict[str, Any] | None) -> float | None:
    if not reduction or reduction.get("skipped"):
        return None
    raw = int(reduction.get("raw_support", 0))
    if raw == 0:
        return 0.0
    return int(reduction.get("residual_support", 0)) / raw


def extract_payload(path: Path) -> dict[str, Any]:
    payload = load_json(path)
    if "ext_ch" in payload:
        ext = payload["ext_ch"]
        ring = payload["ring"]
        row_key = payload.get("row_key", path.stem)
        packets = sorted(payload.get("packets", {}).keys(), key=conductor_sort_key)
        full = ext.get("full_block_coboundary")
        support = ext.get("support_projection_coboundary")
        pair_orbit_count = ext["canonical_pair_orbit_count"]
    else:
        ext = payload
        ring = payload["ring"]
        row_key = path.stem
        packets = sorted(
            {part for key in ext["raw_path_distribution"] for part in path_parts(key)},
            key=conductor_sort_key,
        )
        full = ext.get("coboundary_reduction")
        support = ext.get("support_projection_coboundary")
        pair_orbit_count = ext["pair_orbit_count"]

    return {
        "source": str(path),
        "ring": ring,
        "row_key": row_key,
        "packets": packets,
        "raw_atom_count": int(ext["raw_atom_count"]),
        "raw_pair_count": int(ext["raw_pair_count"]),
        "pair_orbit_count": int(pair_orbit_count),
        "canonical_pair_orbits": ext["canonical_pair_orbits"],
        "raw_path_distribution": ext["raw_path_distribution"],
        "full_block_residual_weight": ratio(full),
        "support_projection_residual_weight": ratio(support),
        "full_block_reduction": full,
        "support_projection_reduction": support,
    }


def conductor_subsets(packets: list[str]) -> list[tuple[str, ...]]:
    out: list[tuple[str, ...]] = []
    for size in range(1, len(packets) + 1):
        out.extend(tuple(combo) for combo in itertools.combinations(packets, size))
    return out


def orbit_path(row: dict[str, Any]) -> tuple[str, str, str]:
    rep = row.get("representative", {})
    source = rep.get("source")
    middle = rep.get("middle")
    target = rep.get("target")
    if source and middle and target:
        return str(source), str(middle), str(target)
    return path_parts(str(row["path"]))


def summarize_leaf(
    rows: list[dict[str, Any]],
    raw_atom_count: int,
    packets: tuple[str, ...],
    residual_weight: float,
    min_active_mass_fraction: float,
) -> dict[str, Any]:
    packet_set = set(packets)
    active = []
    leaking = []
    internal = []
    generated_targets: dict[str, int] = {}
    for row in rows:
        source, middle, target = orbit_path(row)
        atom_count = int(row["atom_count"])
        if source in packet_set and middle in packet_set:
            active.append(row)
            generated_targets[target] = generated_targets.get(target, 0) + atom_count
            if target in packet_set:
                internal.append(row)
            else:
                leaking.append(row)

    active_mass = sum(int(row["atom_count"]) for row in active)
    leak_mass = sum(int(row["atom_count"]) for row in leaking)
    internal_mass = sum(int(row["atom_count"]) for row in internal)
    active_fraction = active_mass / raw_atom_count if raw_atom_count else 0.0
    support_leakage = leak_mass / active_mass if active_mass else 0.0
    orbit_leakage = len(leaking) / len(active) if active else 0.0
    balanced = residual_weight * support_leakage
    orbit_balanced = residual_weight * orbit_leakage
    return {
        "leaf": "+".join(packets),
        "packets": list(packets),
        "active_orbits": len(active),
        "leaking_orbits": len(leaking),
        "active_atom_mass": active_mass,
        "internal_atom_mass": internal_mass,
        "leaking_atom_mass": leak_mass,
        "active_mass_fraction": active_fraction,
        "support_leakage_fraction": support_leakage,
        "balanced_leakage": balanced,
        "orbit_balanced_leakage": orbit_balanced,
        "is_regular_by_active_mass": active_fraction >= min_active_mass_fraction,
        "is_full_leaf": False,
        "generated_targets": dict(sorted(generated_targets.items(), key=lambda item: conductor_sort_key(item[0]))),
    }


def summarize_row(payload: dict[str, Any], min_active_mass_fraction: float) -> dict[str, Any]:
    packets = list(payload["packets"])
    residual_weight = payload["full_block_residual_weight"]
    if residual_weight is None:
        residual_weight = 1.0
    leaves = [
        summarize_leaf(
            payload["canonical_pair_orbits"],
            payload["raw_atom_count"],
            subset,
            residual_weight,
            min_active_mass_fraction,
        )
        for subset in conductor_subsets(packets)
    ]
    full_name = "+".join(packets)
    for leaf in leaves:
        leaf["is_full_leaf"] = leaf["leaf"] == full_name

    active_leaves = [leaf for leaf in leaves if leaf["active_orbits"] > 0]
    regular_leaves = [leaf for leaf in active_leaves if leaf["is_regular_by_active_mass"]]
    proper_regular = [leaf for leaf in regular_leaves if not leaf["is_full_leaf"]]
    best_regular = min(regular_leaves, key=lambda leaf: leaf["balanced_leakage"]) if regular_leaves else None
    best_proper = min(proper_regular, key=lambda leaf: leaf["balanced_leakage"]) if proper_regular else None

    return {
        "ring": payload["ring"],
        "row_key": payload["row_key"],
        "source": payload["source"],
        "packets": packets,
        "raw_atom_count": payload["raw_atom_count"],
        "raw_pair_count": payload["raw_pair_count"],
        "pair_orbit_count": payload["pair_orbit_count"],
        "full_block_residual_weight": payload["full_block_residual_weight"],
        "support_projection_residual_weight": payload["support_projection_residual_weight"],
        "min_active_mass_fraction": min_active_mass_fraction,
        "best_regular_leaf": best_regular["leaf"] if best_regular else None,
        "best_proper_regular_leaf": best_proper["leaf"] if best_proper else None,
        "leaves": sorted(
            active_leaves,
            key=lambda leaf: (
                leaf["balanced_leakage"],
                -leaf["active_mass_fraction"],
                leaf["leaf"],
            ),
        ),
    }


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        return round(obj, 12)
    if isinstance(obj, list):
        return [json_ready(item) for item in obj]
    if isinstance(obj, dict):
        return {str(key): json_ready(value) for key, value in obj.items()}
    return obj


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def make_report(rows: list[dict[str, Any]], output_json: Path) -> str:
    lines = [
        "# Local Row Balanced-Leakage Census",
        "",
        "## Status",
        "",
        f"- JSON artifact: `{output_json}`",
        "- active leaf rule: canonical carry orbits with source,middle inside the leaf",
        "- leakage rule: active carry orbit whose target lands outside the leaf",
        "- balanced leakage: active leakage fraction weighted by the full-block residual survival ratio",
        "",
        "This is a support-level finite audit over saved Ext_CH rows. It does not replace a leaf-specific full-block coboundary computation.",
        "",
    ]

    for row in rows:
        lines += [
            f"## {row['ring']}",
            "",
            f"- source: `{row['source']}`",
            f"- packets: `{', '.join(row['packets'])}`",
            f"- raw atoms / pairs / pair orbits: `{row['raw_atom_count']}` / `{row['raw_pair_count']}` / `{row['pair_orbit_count']}`",
            f"- full-block residual weight: `{fmt(row['full_block_residual_weight'])}`",
            f"- support-projection residual weight: `{fmt(row['support_projection_residual_weight'])}`",
            f"- best regular leaf: `{row['best_regular_leaf']}`",
            f"- best proper regular leaf: `{row['best_proper_regular_leaf']}`",
            "",
            "| rank | leaf | active mass frac | active orbits | leak orbits | support leakage | balanced leakage | orbit-balanced | flags |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---|",
        ]
        for rank, leaf in enumerate(row["leaves"][:16], start=1):
            flags = []
            if leaf["is_full_leaf"]:
                flags.append("full")
            if leaf["is_regular_by_active_mass"]:
                flags.append("regular")
            if leaf["support_leakage_fraction"] == 0.0:
                flags.append("closed")
            lines.append(
                f"| {rank} | `{leaf['leaf']}` | {fmt(leaf['active_mass_fraction'])} | "
                f"{leaf['active_orbits']} | {leaf['leaking_orbits']} | "
                f"{fmt(leaf['support_leakage_fraction'])} | {fmt(leaf['balanced_leakage'])} | "
                f"{fmt(leaf['orbit_balanced_leakage'])} | {', '.join(flags) if flags else 'thin'} |"
            )
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, action="append", default=None)
    parser.add_argument("--min-active-mass-fraction", type=float, default=0.01)
    parser.add_argument("--report", type=Path, default=REPORTS / "local_row_balanced_leakage.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "local_row_balanced_leakage.json")
    args = parser.parse_args()

    inputs = args.input or [path for path in DEFAULT_INPUTS if path.exists()]
    if not inputs:
        raise SystemExit("No local-row inputs found. Pass --input path/to/report.json.")

    rows = [
        summarize_row(extract_payload(path), args.min_active_mass_fraction)
        for path in inputs
    ]
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(json_ready({"rows": rows}), indent=2), encoding="utf-8")
    args.report.write_text(make_report(rows, args.json), encoding="utf-8")

    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(
        json.dumps(
            json_ready(
                {
                    row["ring"]: {
                        "best_regular_leaf": row["best_regular_leaf"],
                        "best_proper_regular_leaf": row["best_proper_regular_leaf"],
                        "full_block_residual_weight": row["full_block_residual_weight"],
                    }
                    for row in rows
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
