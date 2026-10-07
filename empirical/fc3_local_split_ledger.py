"""Build the FC3 local split-ledger certificate for current FC2 rows.

This report extends the first F4[u]/(u^2) FC3 ledger from one Noether-atlas row
to the currently certified FC2 local projection rows.  It records only the
cost fields already present in the exact row classifiers: full filtered carry,
support projection, H4-visible incidence, H3-contraction visibility, remaining
hidden mass, optional PSL depth frontier, and optional normalizer premium.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"

ROW_CLASSIFICATION_JSON = REPORTS / "fc2_row_classification.json"
ATOM_SHADOW_JSON = REPORTS / "fc2_atom_shadow_map.json"
H3_CONTRACTION_JSON = REPORTS / "fc2_h4_contraction_shadow.json"
VISIBLE_KERNEL_JSON = REPORTS / "fc2_visible_fisher_kernel.json"
NORMALIZER_JSON = REPORTS / "normalizer_b0_investment.json"
TRANSFER_JSON = REPORTS / "normalizer_transfer_audit.json"
PSL_JSON = REPORTS / "per_row_carry_vs_depth.json"

DEFAULT_JSON = REPORTS / "fc3_local_split_ledger.json"
DEFAULT_REPORT = REPORTS / "fc3_local_split_ledger.md"

NORMALIZER_KEY_MAP = {
    "f4-u2": "f4-u2",
    "f2-u4-control": "f2-u4",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def rows_by_key(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["row_key"]: row for row in payload["rows"]}


def audit_rows_by_key(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["key"]: row for row in payload["rows"]}


def psl_rows_by_ring(payload: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["ring_name"]: row for row in payload}


def ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def find_binding_psl_test(row: dict[str, Any]) -> dict[str, Any] | None:
    target = row["row_lambda_crit"]
    best: dict[str, Any] | None = None
    best_delta = math.inf
    for test in row["tests"]:
        for shallow in test["by_shallow_depth"]:
            value = shallow["lambda_crit"]
            if value <= 0:
                continue
            delta = abs(value - target)
            if delta < best_delta:
                best_delta = delta
                best = {
                    "target_packet": test["target_packet"],
                    "d_star": test["d_star"],
                    "depth": shallow["depth"],
                    "depth_savings": shallow["depth_savings"],
                    "total_carry_squared": shallow["total_carry_squared"],
                    "lambda_crit": value,
                    "missed_boundaries": shallow["missed_boundaries"],
                }
    return best


def optional_normalizer(
    row_key: str,
    normalizer_rows: dict[str, dict[str, Any]],
    transfer_rows: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    audit_key = NORMALIZER_KEY_MAP.get(row_key)
    if audit_key is None:
        return None
    normalizer = normalizer_rows.get(audit_key)
    transfer = transfer_rows.get(audit_key)
    if normalizer is None:
        return None

    result: dict[str, Any] = {
        "audit_key": audit_key,
        "mean_symmetry_premium_all_supports": normalizer["mean_symmetry_premium"],
        "support_checks": normalizer["support_checks"],
        "overbuy_count": normalizer["overbuy_count"],
    }
    if transfer is not None:
        summary = transfer["transfer_summary"]
        result.update(
            {
                "transfer_mean_structural_gain": summary["mean_structural_gain"],
                "transfer_mean_premium": summary["mean_premium"],
                "transfer_mean_net_gain": summary["mean_net_gain"],
                "transfer_break_even_margin": (
                    summary["mean_structural_gain"] - summary["mean_premium"]
                ),
                "normalizer_beats_minimal_rate": summary[
                    "normalizer_beats_minimal_rate"
                ],
            }
        )
    return result


def build_row(
    row_key: str,
    classification: dict[str, Any],
    atom_shadow: dict[str, Any],
    h3_shadow: dict[str, Any],
    visible_kernel: dict[str, Any],
    psl_by_ring: dict[str, dict[str, Any]],
    normalizer_rows: dict[str, dict[str, Any]],
    transfer_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    class_cost = classification["classification"]
    atom_accounting = atom_shadow["atom_accounting"]
    h3_accounting = h3_shadow["atom_accounting"]
    visible = visible_kernel["visible_shadow"]
    lift = visible.get("input_side_h4_lift", {})

    full = class_cost["full_filtered_residual"]
    support = class_cost["support_projection_residual"]
    h4 = h3_accounting["h4_visible_atoms"]
    h3 = h3_accounting["h4_invisible_h3_contraction_visible_atoms"]
    remaining = h3_accounting["remaining_invisible_atoms"]
    h4_invisible = h3_accounting["h4_invisible_atoms"]

    psl_row = psl_by_ring.get(classification["ring"])
    psl = None
    if psl_row is not None:
        binding = find_binding_psl_test(psl_row)
        psl = {
            "d_max": psl_row["d_max"],
            "n_max_carry_order": psl_row["n_max_carry_order"],
            "row_lambda_psl_crit": psl_row["row_lambda_crit"],
            "dagger_holds": psl_row["dagger_holds"],
            "binding_test": binding,
        }

    normalizer = optional_normalizer(row_key, normalizer_rows, transfer_rows)
    partition_sum = h4 + h3 + remaining
    underpricing_gap = full - support

    return {
        "row_key": row_key,
        "ring": classification["ring"],
        "row_role": classification["row_role"],
        "label_count": classification["constructor"]["label_count"],
        "gamma_size": classification["constructor"].get("gamma_size"),
        "packets": classification["constructor"].get("packets", {}),
        "carry_record_count": classification["constructor"].get("carry_record_count"),
        "filtered_carry": {
            "full_filtered_residual": full,
            "support_projection_residual": support,
            "support_underpricing_gap_atoms": underpricing_gap,
            "h4_visible_atoms": h4,
            "h4_invisible_atoms": h4_invisible,
            "h3_contraction_visible_atoms": h3,
            "remaining_hidden_atoms": remaining,
            "visibility_partition_sum": partition_sum,
            "fractions_of_full": {
                "support_projection": ratio(support, full),
                "h4_visible": ratio(h4, full),
                "h3_contraction_visible": ratio(h3, full),
                "remaining_hidden": ratio(remaining, full),
                "support_underpricing_gap": ratio(underpricing_gap, full),
            },
        },
        "visible_fisher_shadow": {
            "status": visible["status"],
            "commutator_entries": visible.get("commutator_entries", 0),
            "commutator_orbits": visible.get("commutator_orbits", 0),
            "lifted_commutator_orbits": lift.get("lifted_commutator_orbits", 0),
            "mixed_h4_orbits_hit": lift.get("mixed_h4_orbits_hit", 0),
            "mixed_h4_orbits_total": lift.get("mixed_h4_orbits_total", 0),
            "pure_h4_orbits_hit": lift.get("pure_h4_orbits_hit", 0),
            "pure_h4_orbits_total": lift.get("pure_h4_orbits_total", 0),
        },
        "psl_depth_or_boundary_carry": psl,
        "normalizer_symmetry_premium": normalizer,
        "checks": {
            "classification_full_equals_h3_raw": full
            == h3_accounting["raw_residual_atoms"],
            "atom_shadow_full_equals_raw": full
            == atom_accounting["raw_residual_atoms"],
            "h4_visible_consistent": h4 == atom_accounting["visible_h4_incident_atoms"],
            "visibility_partition_sums_to_full": partition_sum == full,
            "support_projection_erases_full": support == 0 and full > 0,
            "visible_shadow_exact_or_empty": visible["status"] in {"exact", "empty"},
            "psl_dagger_holds_when_present": True
            if psl is None
            else psl["dagger_holds"] is True,
        },
    }


def aggregate_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_full = sum(row["filtered_carry"]["full_filtered_residual"] for row in rows)
    total_support = sum(
        row["filtered_carry"]["support_projection_residual"] for row in rows
    )
    total_h4 = sum(row["filtered_carry"]["h4_visible_atoms"] for row in rows)
    total_h3 = sum(
        row["filtered_carry"]["h3_contraction_visible_atoms"] for row in rows
    )
    total_remaining = sum(
        row["filtered_carry"]["remaining_hidden_atoms"] for row in rows
    )
    return {
        "row_count": len(rows),
        "total_full_filtered_residual": total_full,
        "total_support_projection_residual": total_support,
        "total_support_underpricing_gap_atoms": total_full - total_support,
        "total_h4_visible_atoms": total_h4,
        "total_h3_contraction_visible_atoms": total_h3,
        "total_remaining_hidden_atoms": total_remaining,
        "visibility_partition_sum": total_h4 + total_h3 + total_remaining,
        "fractions_of_total_full": {
            "support_projection": ratio(total_support, total_full),
            "h4_visible": ratio(total_h4, total_full),
            "h3_contraction_visible": ratio(total_h3, total_full),
            "remaining_hidden": ratio(total_remaining, total_full),
            "support_underpricing_gap": ratio(total_full - total_support, total_full),
        },
    }


def build_payload() -> dict[str, Any]:
    classification = load_json(ROW_CLASSIFICATION_JSON)
    atom_shadow = load_json(ATOM_SHADOW_JSON)
    h3_shadow = load_json(H3_CONTRACTION_JSON)
    visible_kernel = load_json(VISIBLE_KERNEL_JSON)
    normalizer = load_json(NORMALIZER_JSON)
    transfer = load_json(TRANSFER_JSON)
    psl = load_json(PSL_JSON)

    class_rows = rows_by_key(classification)
    atom_rows = rows_by_key(atom_shadow)
    h3_rows = rows_by_key(h3_shadow)
    visible_rows = rows_by_key(visible_kernel)
    normalizer_rows = audit_rows_by_key(normalizer)
    transfer_rows = audit_rows_by_key(transfer)
    psl_by_ring = psl_rows_by_ring(psl)

    rows = [
        build_row(
            row_key,
            class_rows[row_key],
            atom_rows[row_key],
            h3_rows[row_key],
            visible_rows[row_key],
            psl_by_ring,
            normalizer_rows,
            transfer_rows,
        )
        for row_key in class_rows
    ]
    checks = [
        {
            "name": "all_row_checks_pass",
            "observed": {
                row["row_key"]: all(row["checks"].values()) for row in rows
            },
            "expected": "all true",
            "pass": all(all(row["checks"].values()) for row in rows),
        },
        {
            "name": "all_support_projection_residuals_zero",
            "observed": {
                row["row_key"]: row["filtered_carry"]["support_projection_residual"]
                for row in rows
            },
            "expected": 0,
            "pass": all(
                row["filtered_carry"]["support_projection_residual"] == 0
                for row in rows
            ),
        },
        {
            "name": "aggregate_visibility_partition",
            "observed": aggregate_rows(rows)["visibility_partition_sum"],
            "expected": aggregate_rows(rows)["total_full_filtered_residual"],
            "pass": aggregate_rows(rows)["visibility_partition_sum"]
            == aggregate_rows(rows)["total_full_filtered_residual"],
        },
    ]
    return {
        "schema": "fc3_local_split_ledger.v1",
        "status": "FC3 local split-cost ledger across current exact FC2 rows",
        "certificate_pass": all(check["pass"] for check in checks),
        "sources": {
            "fc2_row_classification": source_path(ROW_CLASSIFICATION_JSON),
            "fc2_atom_shadow_map": source_path(ATOM_SHADOW_JSON),
            "fc2_h4_contraction_shadow": source_path(H3_CONTRACTION_JSON),
            "fc2_visible_fisher_kernel": source_path(VISIBLE_KERNEL_JSON),
            "normalizer_b0_investment": source_path(NORMALIZER_JSON),
            "normalizer_transfer_audit": source_path(TRANSFER_JSON),
            "per_row_carry_vs_depth": source_path(PSL_JSON),
        },
        "aggregate": aggregate_rows(rows),
        "rows": rows,
        "checks": checks,
        "interpretation": [
            "Support projection residual 0 is not full filtered closure.",
            "Every current row has positive full filtered residual erased by support projection.",
            "H4 and H3 are visibility projections of [kappa] shadows modulo kernels.",
            "Normalizer premium fields are included only where B3/B4 audits exist.",
            "PSL carry frontier fields are included only where per-row carry-vs-depth certificates match the row.",
        ],
    }


def format_float(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def render_markdown(payload: dict[str, Any]) -> str:
    aggregate = payload["aggregate"]
    lines = [
        "# FC3 Local Split-Cost Ledger",
        "",
        "This report extends FC3 from the first `F4[u]/(u^2)` bounded Noether",
        "ledger to the current exact FC2 row-classifier ledger.  It is a",
        "projection-cost certificate, not a claim that every row has the full",
        "FC1 Noether atlas.",
        "",
        "## Aggregate",
        "",
        "| field | value |",
        "|---|---:|",
        f"| rows | {aggregate['row_count']} |",
        f"| full filtered residual | {aggregate['total_full_filtered_residual']} |",
        f"| support projection residual | {aggregate['total_support_projection_residual']} |",
        f"| support underpricing gap | {aggregate['total_support_underpricing_gap_atoms']} |",
        f"| H4-visible atoms | {aggregate['total_h4_visible_atoms']} |",
        f"| H3-contraction visible atoms | {aggregate['total_h3_contraction_visible_atoms']} |",
        f"| remaining hidden atoms | {aggregate['total_remaining_hidden_atoms']} |",
        "",
        "## Row Ledger",
        "",
        "| row | full | support | H4 | H3 | remaining | underprice | K_CH status | PSL lambda | normalizer margin |",
        "|---|---:|---:|---:|---:|---:|---:|---|---:|---:|",
    ]
    for row in payload["rows"]:
        carry = row["filtered_carry"]
        visible = row["visible_fisher_shadow"]
        psl = row["psl_depth_or_boundary_carry"]
        normalizer = row["normalizer_symmetry_premium"]
        psl_lambda = None if psl is None else psl["row_lambda_psl_crit"]
        margin = None
        if normalizer is not None:
            margin = normalizer.get("transfer_break_even_margin")
        lines.append(
            "| {row} | {full} | {support} | {h4} | {h3} | {remaining} | "
            "{gap} | {status} | {psl} | {margin} |".format(
                row=f"{row['row_key']} ({row['ring']})",
                full=carry["full_filtered_residual"],
                support=carry["support_projection_residual"],
                h4=carry["h4_visible_atoms"],
                h3=carry["h3_contraction_visible_atoms"],
                remaining=carry["remaining_hidden_atoms"],
                gap=carry["support_underpricing_gap_atoms"],
                status=visible["status"],
                psl=format_float(psl_lambda),
                margin=format_float(margin),
            )
        )

    lines += [
        "",
        "## Visibility Fractions",
        "",
        "| row | support | H4 | H3 | remaining | underprice |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in payload["rows"]:
        fractions = row["filtered_carry"]["fractions_of_full"]
        lines.append(
            "| {row} | {support} | {h4} | {h3} | {remaining} | {gap} |".format(
                row=row["row_key"],
                support=format_float(fractions["support_projection"]),
                h4=format_float(fractions["h4_visible"]),
                h3=format_float(fractions["h3_contraction_visible"]),
                remaining=format_float(fractions["remaining_hidden"]),
                gap=format_float(fractions["support_underpricing_gap"]),
            )
        )

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
        "Across the current exact FC2 rows, support-only pricing reports `0`",
        f"residual while full filtered carry reports `{aggregate['total_full_filtered_residual']}`",
        "atoms.  This proves the FC3 local pricing rule at projection-ledger",
        "scope: full filtered carry must remain a separate cost channel, and",
        "H4/H3/remaining fields are visibility partitions rather than closure",
        "certificates.",
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
