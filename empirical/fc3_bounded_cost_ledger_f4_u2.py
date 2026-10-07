"""Build the first bounded FC3 split-cost ledger for F4[u]/(u^2).

This script is deliberately a ledger, not a new heavy census.  It reads the
FC1 atlas certificate, B3 normalizer audits, B4 transfer audit, B0 frontier
audit, and the per-row PSL carry-vs-depth certificate, then emits the separated
cost fields needed by the bounded FC3 theorem candidate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"

FC1_JSON = REPORTS / "fc1_noether_atlas_certificate_f4_u2.json"
NORMALIZER_JSON = REPORTS / "normalizer_b0_investment.json"
TRANSFER_JSON = REPORTS / "normalizer_transfer_audit.json"
FRONTIER_JSON = REPORTS / "information_investment_frontier.json"
PSL_JSON = REPORTS / "per_row_carry_vs_depth.json"

DEFAULT_JSON = REPORTS / "fc3_bounded_cost_ledger_f4_u2.json"
DEFAULT_REPORT = REPORTS / "fc3_bounded_cost_ledger_f4_u2.md"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def find_row(payload: dict[str, Any] | list[dict[str, Any]], key: str) -> dict[str, Any]:
    rows = payload if isinstance(payload, list) else payload["rows"]
    for row in rows:
        if row.get("key") == key or row.get("row") == "F_4[u]/(u^2)":
            return row
    raise KeyError(f"missing row {key}")


def ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def build_payload() -> dict[str, Any]:
    fc1 = load_json(FC1_JSON)
    normalizer = load_json(NORMALIZER_JSON)
    transfer = load_json(TRANSFER_JSON)
    frontier = load_json(FRONTIER_JSON)
    psl_rows = load_json(PSL_JSON)

    residual = fc1["tuple_level_residual_label"]
    full = residual["full_filtered_residual"]
    support = residual["support_projection_residual"]
    h4 = residual["h4_visible_atoms"]
    h3 = residual["h3_contraction_visible_from_h4_invisible"]
    remaining = residual["remaining_invisible_atoms"]

    normalizer_row = find_row(normalizer, "f4-u2")
    transfer_row = find_row(transfer, "f4-u2")
    frontier_row = find_row(frontier, "f4-u2")
    psl_row = find_row(psl_rows, "f4-u2")

    descent_policy = frontier_row["policies"]["descent_closure"]
    normalizer_policy = frontier_row["policies"]["normalizer_saturation"]
    transfer_summary = transfer_row["transfer_summary"]

    binding_test = None
    for test in psl_row["tests"]:
        if test["target_packet"] == "u^2":
            binding_test = test["by_shallow_depth"][0]
            break
    if binding_test is None:
        raise AssertionError("missing F4[u]/(u^2) u^2 PSL binding test")

    residual_partition_sum = h4 + h3 + remaining
    support_underpricing_gap = full - support
    transfer_break_even_margin = (
        transfer_summary["mean_structural_gain"] - transfer_summary["mean_premium"]
    )

    checks = [
        {
            "name": "fc1_certificate_pass",
            "observed": fc1["certificate_pass"],
            "expected": True,
            "pass": fc1["certificate_pass"] is True,
        },
        {
            "name": "residual_visibility_partition",
            "observed": residual_partition_sum,
            "expected": full,
            "pass": residual_partition_sum == full,
        },
        {
            "name": "support_projection_erases_full_residual",
            "observed": [full, support],
            "expected": [1569, 0],
            "pass": full == 1569 and support == 0,
        },
        {
            "name": "support_only_underpricing_gap_positive",
            "observed": support_underpricing_gap,
            "expected": "> 0",
            "pass": support_underpricing_gap > 0,
        },
        {
            "name": "generated_subgroup_zero_structural_frontier",
            "observed": {
                "fisher": descent_policy["mean_fisher_projection_error"],
                "reciprocal": descent_policy["mean_reciprocal_projection_error"],
                "closure": descent_policy["mean_closure_leakage"],
                "balance": descent_policy["mean_descent_balance_cost"],
            },
            "expected": "all near 0",
            "pass": all(
                abs(descent_policy[field]) < 1e-12
                for field in [
                    "mean_fisher_projection_error",
                    "mean_reciprocal_projection_error",
                    "mean_closure_leakage",
                    "mean_descent_balance_cost",
                ]
            ),
        },
        {
            "name": "normalizer_transfer_break_even",
            "observed": transfer_break_even_margin,
            "expected": "> 0",
            "pass": transfer_break_even_margin > 0,
        },
        {
            "name": "psl_dagger_holds",
            "observed": psl_row["dagger_holds"],
            "expected": True,
            "pass": psl_row["dagger_holds"] is True,
        },
    ]

    return {
        "schema": "fc3_bounded_cost_ledger_f4_u2.v1",
        "status": "first bounded FC3 split-cost ledger for the certified local row",
        "row_key": "f4-u2",
        "ring": fc1["ring"],
        "certificate_pass": all(check["pass"] for check in checks),
        "sources": {
            "fc1_atlas_certificate": source_path(FC1_JSON),
            "normalizer_b0_investment": source_path(NORMALIZER_JSON),
            "normalizer_transfer_audit": source_path(TRANSFER_JSON),
            "information_investment_frontier": source_path(FRONTIER_JSON),
            "per_row_carry_vs_depth": source_path(PSL_JSON),
        },
        "ledger": {
            "generated_subgroup_descent": {
                "policy": "D_G(S) = <S> \\ {0}",
                "mean_J": descent_policy["mean_J"],
                "mean_support_size": descent_policy["mean_support_size"],
                "mean_resource_cost": descent_policy["mean_resource_cost"],
                "zero_structural_cost": True,
            },
            "normalizer_symmetry_premium": {
                "policy": "D_G^Gamma(S) = <Gamma.S> \\ {0}",
                "all_support_mean_symmetry_premium": normalizer_row[
                    "mean_symmetry_premium"
                ],
                "all_support_overbuy_count": normalizer_row["overbuy_count"],
                "all_support_checks": normalizer_row["support_checks"],
                "frontier_mean_J": normalizer_policy["mean_J"],
                "frontier_mean_resource_cost": normalizer_policy[
                    "mean_resource_cost"
                ],
                "transfer_mean_premium": transfer_summary["mean_premium"],
                "transfer_mean_structural_gain": transfer_summary[
                    "mean_structural_gain"
                ],
                "transfer_mean_net_gain": transfer_summary["mean_net_gain"],
                "transfer_break_even_margin": transfer_break_even_margin,
                "normalizer_beats_minimal_rate": transfer_summary[
                    "normalizer_beats_minimal_rate"
                ],
            },
            "psl_depth_or_boundary_carry": {
                "d_max": psl_row["d_max"],
                "row_lambda_psl_crit": psl_row["row_lambda_crit"],
                "binding_target_packet": "u^2",
                "binding_depth": binding_test["depth"],
                "binding_depth_savings": binding_test["depth_savings"],
                "binding_total_carry_squared": binding_test[
                    "total_carry_squared"
                ],
                "binding_lambda_crit": binding_test["lambda_crit"],
            },
            "filtered_carry": {
                "source": residual["kappa_source"],
                "full_filtered_residual": full,
                "support_projection_residual": support,
                "support_underpricing_gap_atoms": support_underpricing_gap,
                "h4_visible_atoms": h4,
                "h3_contraction_visible_atoms": h3,
                "remaining_hidden_atoms": remaining,
                "visibility_partition_sum": residual_partition_sum,
                "fractions_of_full": {
                    "support_projection": ratio(support, full),
                    "h4_visible": ratio(h4, full),
                    "h3_contraction_visible": ratio(h3, full),
                    "remaining_hidden": ratio(remaining, full),
                    "support_underpricing_gap": ratio(support_underpricing_gap, full),
                },
            },
            "resource_skeleton": {
                "seed_coordinates": fc1["bounded_atlas_scope"]["seed_coordinates"],
                "tuple_size": fc1["bounded_atlas_scope"]["tuple_size"],
                "aggregate_tuple_supports": fc1["delivered_layer_summary"][
                    "aggregate_tuple_supports"
                ],
                "size24_orbits": fc1["delivered_layer_summary"]["size24_orbits"],
                "size24_sign_nontrivial": fc1["delivered_layer_summary"][
                    "size24_sign_nontrivial"
                ],
                "carry_pair_chart_orbits_not_simultaneous": fc1[
                    "delivered_layer_summary"
                ]["carry_pair_chart_orbits_not_simultaneous"],
            },
        },
        "unit_weight_carry_scalarizations": {
            "support_only_atoms": support,
            "full_filtered_atoms": full,
            "visible_partition_atoms": residual_partition_sum,
            "support_only_underprices_full_by_atoms": support_underpricing_gap,
        },
        "checks": checks,
        "interpretation": [
            "Generated-subgroup descent is the zero-structural baseline.",
            "Normalizer saturation is a transfer policy, not a free default.",
            "Support residual 0 is not full filtered closure.",
            "H4 and H3 entries are visibility channels modulo kernels, not standalone Ext_CH detectors.",
            "This is an exact finite bookkeeping certificate, not learned-model evidence.",
        ],
    }


def format_float(value: float) -> str:
    return f"{value:.6f}"


def render_markdown(payload: dict[str, Any]) -> str:
    ledger = payload["ledger"]
    filtered = ledger["filtered_carry"]
    normalizer = ledger["normalizer_symmetry_premium"]
    descent = ledger["generated_subgroup_descent"]
    psl = ledger["psl_depth_or_boundary_carry"]
    resource = ledger["resource_skeleton"]

    lines = [
        "# FC3 Bounded Cost Ledger: F4[u]/(u^2)",
        "",
        "This is the first exact split-cost ledger for FC3.  It imports the",
        "bounded FC1 atlas and the B0-B4 information-investment audits without",
        "turning support projection into full filtered closure.",
        "",
        "## Ledger Summary",
        "",
        "| channel | value | reading |",
        "|---|---:|---|",
        (
            "| generated-subgroup descent mean J | "
            f"{format_float(descent['mean_J'])} | zero structural baseline on the held-out frontier |"
        ),
        (
            "| generated-subgroup resource | "
            f"{format_float(descent['mean_resource_cost'])} | mean support/resource paid by D_G(S) |"
        ),
        (
            "| normalizer transfer gain | "
            f"{format_float(normalizer['transfer_mean_structural_gain'])} | expected structural gain on normalizer-transfer audit |"
        ),
        (
            "| normalizer transfer premium | "
            f"{format_float(normalizer['transfer_mean_premium'])} | resource-weighted symmetry premium |"
        ),
        (
            "| normalizer break-even margin | "
            f"{format_float(normalizer['transfer_break_even_margin'])} | positive means B3 pays on this audit distribution |"
        ),
        (
            "| PSL lambda_crit | "
            f"{format_float(psl['row_lambda_psl_crit'])} | row break-even for shallow PSL depth |"
        ),
        f"| full filtered residual | {filtered['full_filtered_residual']} | true [kappa]-sourced local carry mass |",
        f"| support projection residual | {filtered['support_projection_residual']} | support-only pricing channel |",
        f"| H4-visible atoms | {filtered['h4_visible_atoms']} | Fisher-shadow incidence channel |",
        f"| H3-contraction visible atoms | {filtered['h3_contraction_visible_atoms']} | weaker contraction-shadow channel |",
        f"| remaining hidden atoms | {filtered['remaining_hidden_atoms']} | not visible to tested H4/H3 channels |",
        f"| support underpricing gap | {filtered['support_underpricing_gap_atoms']} | full minus support residual |",
        "",
        "## Visibility Fractions",
        "",
        "| field | fraction of full residual |",
        "|---|---:|",
    ]
    for key, value in filtered["fractions_of_full"].items():
        lines.append(f"| {key} | {format_float(value)} |")

    lines += [
        "",
        "## Resource Skeleton",
        "",
        "| field | value |",
        "|---|---:|",
    ]
    for key, value in resource.items():
        lines.append(f"| {key} | {value} |")

    lines += [
        "",
        "## Checks",
        "",
        "| check | observed | expected | pass |",
        "|---|---|---|---|",
    ]
    for check in payload["checks"]:
        observed = json.dumps(check["observed"], sort_keys=True)
        expected = json.dumps(check["expected"], sort_keys=True)
        lines.append(
            f"| {check['name']} | `{observed}` | `{expected}` | {check['pass']} |"
        )

    lines += [
        "",
        "## Reading",
        "",
        "The bounded FC3 theorem should start from the generated-subgroup baseline,",
        "add the normalizer premium only under the transfer break-even rule, and",
        "price local carry through the full filtered residual and its declared",
        "visibility partition.  On this certified row, support-only pricing sees",
        "`0` carry atoms while the full filtered ledger sees `1569`.",
    ]
    return "\n".join(lines) + "\n"


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_report(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(payload), encoding="utf-8")


def check_payload(payload: dict[str, Any], path: Path) -> None:
    recorded = json.loads(path.read_text(encoding="utf-8"))
    if recorded != payload:
        raise AssertionError(f"payload differs from {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=None)
    args = parser.parse_args()

    payload = build_payload()
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return

    write_json(payload, args.json)
    write_report(payload, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
