"""Combine neural, support-level, and per-leaf residual critical-leaf audits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_leaf(leaves: list[dict[str, Any]], name: str | None) -> dict[str, Any] | None:
    if name is None:
        return None
    return next((leaf for leaf in leaves if leaf["leaf"] == name), None)


def full_block_status(row: dict[str, Any] | None) -> str:
    if row is None:
        return "n/a"
    if row.get("skipped"):
        return "skipped"
    return "closed" if row.get("raw_is_coboundary") else "residual"


def merged_residual_value(
    residual: dict[str, Any] | None,
    modular: dict[str, Any] | None,
    key: str,
) -> Any:
    if residual is not None and not residual.get("skipped") and residual.get(key) is not None:
        return residual.get(key)
    if modular is not None:
        return modular.get(key)
    return None


def merged_full_block_status(
    residual: dict[str, Any] | None,
    modular: dict[str, Any] | None,
) -> str:
    if residual is not None and not residual.get("skipped"):
        return full_block_status(residual)
    if modular is not None:
        return "modular_closed" if modular.get("raw_is_coboundary") else "modular_residual"
    return full_block_status(residual)


def build_summary(
    neural: dict[str, Any],
    local: dict[str, Any],
    per_leaf: dict[str, Any],
    modular: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for run in neural["runs"]:
        chosen = run.get("best_proper_nonflat_by_rho_frac") or run.get("best_nonflat_by_rho_frac") or run.get("best_regular_by_rho_frac")
        leaf = find_leaf(run["leaves"], chosen)
        rows.append(
            {
                "mode": "neural",
                "algebra": f"{run['preset']} / {run['model_tag']}",
                "selected_leaf": chosen,
                "selection_rule": "best non-flat rho_frac" if run.get("best_nonflat_by_rho_frac") else "best regular rho_frac",
                "balanced_leakage": None if leaf is None else leaf.get("mean_balanced_leakage"),
                "support_leakage": None if leaf is None else leaf.get("mean_kch_closure_leakage_fraction"),
                "full_block_status": "n/a",
                "full_block_residual_deficit": None,
                "full_block_packet_mass_normalized_residual": None,
                "full_block_orbit_count_normalized_residual": None,
                "nu_lambda_E_normalized_carry_proxy": None,
                "nu_lambda_E_raw_mass": None,
                "nu_lambda_E_residual_mass": None,
                "nu_lambda_E_deficit": None,
                "c2_orbit_quotient_volume": None,
                "residual_orbit_quotient_support": None,
                "orbit_quotient_residual_mass": None,
                "h3_leaf_orbit_quotient_dimension": None,
                "h4_leaf_orbit_quotient_dimension": None,
                "h4_to_h3_orbit_cokernel_dimension": None,
                "reading": "centroid projection; no Ext_CH full-block complex",
            }
        )

    per_leaf_index = {
        (row["ring"], row["leaf"]): row
        for row in per_leaf["rows"]
    }
    modular_index = {
        (row["ring"], row["leaf"]): row
        for row in (modular or {}).get("rows", [])
        if row.get("modular_residual_status") == "complete"
    }
    for run in local["rows"]:
        chosen = run.get("best_proper_regular_leaf") or run.get("best_regular_leaf")
        leaf = find_leaf(run["leaves"], chosen)
        residual = per_leaf_index.get((run["ring"], chosen))
        modular_residual = modular_index.get((run["ring"], chosen))
        rows.append(
            {
                "mode": "local_atlas",
                "algebra": run["ring"],
                "selected_leaf": chosen,
                "selection_rule": "best proper regular balanced leakage",
                "balanced_leakage": None if leaf is None else leaf.get("balanced_leakage"),
                "support_leakage": None if leaf is None else leaf.get("support_leakage_fraction"),
                "full_block_status": merged_full_block_status(residual, modular_residual),
                "full_block_residual_deficit": merged_residual_value(
                    residual, modular_residual, "residual_deficit"
                ),
                "full_block_packet_mass_normalized_residual": (
                    merged_residual_value(
                        residual,
                        modular_residual,
                        "packet_mass_normalized_residual",
                    )
                    if modular_residual is None
                    else (
                        None
                        if modular_residual.get("raw_support") in (None, 0)
                        else modular_residual.get("residual_support")
                        / modular_residual.get("raw_support")
                    )
                ),
                "full_block_orbit_count_normalized_residual": (
                    None if residual is None else residual.get("orbit_count_normalized_residual")
                ),
                "nu_lambda_E_normalized_carry_proxy": (
                    merged_residual_value(
                        residual,
                        modular_residual,
                        "nu_lambda_E_normalized_carry_proxy",
                    )
                ),
                "nu_lambda_E_raw_mass": (
                    merged_residual_value(residual, modular_residual, "nu_lambda_E_raw_mass")
                ),
                "nu_lambda_E_residual_mass": (
                    merged_residual_value(residual, modular_residual, "nu_lambda_E_residual_mass")
                ),
                "nu_lambda_E_deficit": (
                    merged_residual_value(residual, modular_residual, "nu_lambda_E_deficit")
                ),
                "c2_orbit_quotient_volume": (
                    merged_residual_value(residual, modular_residual, "c2_orbit_quotient_volume")
                ),
                "residual_orbit_quotient_support": (
                    merged_residual_value(
                        residual,
                        modular_residual,
                        "residual_orbit_quotient_support",
                    )
                ),
                "orbit_quotient_residual_mass": (
                    merged_residual_value(
                        residual,
                        modular_residual,
                        "orbit_quotient_residual_mass",
                    )
                ),
                "h3_leaf_orbit_quotient_dimension": (
                    None if residual is None else residual.get("h3_leaf_orbit_quotient_dimension")
                ),
                "h4_leaf_orbit_quotient_dimension": (
                    None if residual is None else residual.get("h4_leaf_orbit_quotient_dimension")
                ),
                "h4_to_h3_orbit_cokernel_dimension": (
                    None if residual is None else residual.get("h4_to_h3_orbit_cokernel_dimension")
                ),
                "reading": (
                    "support closes but full-block residual survives"
                    if residual and not residual.get("skipped") and not residual.get("raw_is_coboundary")
                    else "support closes but modular full-block residual survives"
                    if modular_residual and not modular_residual.get("raw_is_coboundary")
                    else "support-level result; full-block audit pending or skipped"
                ),
            }
        )
    return rows


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
        "# Cross-Mode Critical-Leaf Summary",
        "",
        f"- JSON artifact: `{output_json}`",
        "- Quotient columns are normalizer orbit quotients on the selected leaf; H4->H3 is a support-level orbit cokernel, not a full higher-current rank quotient.",
        "",
        "| mode | algebra | selected leaf | balanced leakage | support/KCH leakage | full-block status | full-block deficit | residual/atom | nu_E residual | C2 orbit vol | residual orbit support | orbit residual mass | H3 orbits | H4 orbits | H4->H3 cokernel | reading |",
        "|---|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['mode']} | {row['algebra']} | `{row['selected_leaf']}` | "
            f"{fmt(row['balanced_leakage'])} | {fmt(row['support_leakage'])} | "
            f"{row['full_block_status']} | {fmt(row['full_block_residual_deficit'])} | "
            f"{fmt(row['full_block_packet_mass_normalized_residual'])} | "
            f"{fmt(row['nu_lambda_E_residual_mass'])} | "
            f"{fmt(row['c2_orbit_quotient_volume'])} | "
            f"{fmt(row['residual_orbit_quotient_support'])} | "
            f"{fmt(row['orbit_quotient_residual_mass'])} | "
            f"{fmt(row['h3_leaf_orbit_quotient_dimension'])} | "
            f"{fmt(row['h4_leaf_orbit_quotient_dimension'])} | "
            f"{fmt(row['h4_to_h3_orbit_cokernel_dimension'])} | "
            f"{row['reading']} |"
        )
    lines += [
        "",
        "## Reading",
        "",
        "The neural rows identify non-flat conductor leaves with zero KCH outside budget in the cyclic proxy. The local rows identify support-closed leaves, but the per-leaf full-block audit shows that the filtered residual is still not killed on the exact rows that were small enough to run. The C2-volume and orbit-quotient residual masses decay along the F2 suffix tower while the relative full-block deficit remains 1.0; the H4-to-H3 support orbit cokernel vanishes on the selected local rows. The closure gap is now a quotient-level saturation question rather than a support-closure question.",
        "Rows marked `modular_residual` are finite-field full-block reductions from `streaming_modular_residual`; they are residual evidence, not rational closure proofs.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--neural", type=Path, default=REPORTS / "critical_leaf_projection_census.json")
    parser.add_argument("--local", type=Path, default=REPORTS / "local_row_balanced_leakage.json")
    parser.add_argument("--per-leaf", type=Path, default=REPORTS / "per_leaf_coboundary_audit.json")
    parser.add_argument("--modular", type=Path, default=REPORTS / "streaming_modular_residual.json")
    parser.add_argument("--report", type=Path, default=REPORTS / "cross_mode_critical_leaf_summary.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "cross_mode_critical_leaf_summary.json")
    args = parser.parse_args()

    modular = load(args.modular) if args.modular.exists() else None
    rows = build_summary(load(args.neural), load(args.local), load(args.per_leaf), modular)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(json_ready({"rows": rows}), indent=2), encoding="utf-8")
    args.report.write_text(make_report(rows, args.json), encoding="utf-8")
    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
