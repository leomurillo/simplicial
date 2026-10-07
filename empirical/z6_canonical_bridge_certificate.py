"""Consolidated certificate for the Paper 28 T*1' finite-row bridge.

The corrected bridge is:

  eta = Z6 e-pure dyadic product base + scale-free Heron-gated mixed copula
  Pi  = Euler-Lagrange projection of the pulled-back cubic Fisher action

This script does not rerun the lower-level audits. It reads their JSON reports
and issues a single certificate that separates:

  - required passes: e-purity/area-gate control and EL Noether conservation;
  - expected kills: algebraic K_CH shortcut and global metric homothety.

The expected kills are not hidden. They are the reason the physical projection
is Pi_EL and the finite row is interpreted as a controlled projection row
rather than a global Jacobi-Fisher isometry.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"missing audit report: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def summary_status(report: dict[str, Any]) -> str:
    return str(report.get("summary", {}).get("status", "UNKNOWN"))


def audit(args: argparse.Namespace) -> dict[str, Any]:
    area = load_json(args.area_json)
    noether = load_json(args.noether_json)
    shortcut = load_json(args.shortcut_json)
    metric = load_json(args.metric_json)

    area_s = area["summary"]
    noether_s = noether["summary"]
    shortcut_s = shortcut["summary"]
    metric_s = metric["summary"]

    required_failures: list[str] = []
    control_notes: list[str] = []

    if summary_status(area) != "PASS":
        required_failures.append("area-gated copula audit did not pass")
    if area_s.get("max_base_e_tangent_mixed_ratio", float("inf")) > args.e_purity_tol:
        required_failures.append("independent base is not e-pure within tolerance")
    if area_s.get("interior_theta", 0.0) <= args.theta_floor:
        required_failures.append("Heron area gate is not active in the interior")
    if area_s.get("boundary_theta", float("inf")) > args.boundary_theta_tol:
        required_failures.append("Heron area gate does not shut off on the boundary")
    if area_s.get("interior_copula_k_ch_mixed_ratio", 0.0) <= args.spillover_floor:
        required_failures.append("interior mixed K_CH spillover is at floor")

    if summary_status(noether) != "PASS":
        required_failures.append("EL projection Noether audit did not pass")
    if noether_s.get("max_relative_energy_drift", float("inf")) > args.energy_drift_tol:
        required_failures.append("EL projection energy drift exceeds tolerance")
    if noether_s.get("max_ternary_acceleration_norm", 0.0) <= args.ternary_floor:
        required_failures.append("copula-minus-base ternary acceleration is at floor")

    if summary_status(shortcut) == "KILL":
        control_notes.append("direct algebraic K_CH force shortcut remains falsified as expected")
    else:
        control_notes.append("direct algebraic K_CH shortcut was not killed; inspect because Pi_EL may not be necessary")

    if summary_status(metric) == "KILL":
        control_notes.append("global finite-row metric homothety remains falsified and is recorded as typed overflow")
    else:
        control_notes.append("metric homothety was not killed; inspect whether finite-row matching improved")

    status = "PASS_FINITE_ROW_CANONICAL_BRIDGE" if not required_failures else "KILL"
    return {
        "claim_tested": "Paper 28 T*1' corrected Z6 canonical bridge certificate",
        "selection_principle": {
            "row": "Z6 = Z2 x Z3, the minimal CRT row with dyadic and ternary sectors",
            "eta_base": "maximum-entropy/product dyadic base, pure in e-coordinates",
            "ternary_gate": "scale-free Heron shape gate times a normalized V2xV3 copula contrast",
            "physical_projection": "Pi_EL, the Euler-Lagrange projection of the pulled-back cubic Fisher action",
            "residual_policy": "finite-row metric mismatch is typed projection overflow, not silently erased",
        },
        "input_reports": {
            "area_json": str(args.area_json),
            "noether_json": str(args.noether_json),
            "shortcut_json": str(args.shortcut_json),
            "metric_json": str(args.metric_json),
        },
        "summary": {
            "status": status,
            "required_failures": required_failures,
            "control_notes": control_notes,
            "max_base_e_tangent_mixed_ratio": area_s.get("max_base_e_tangent_mixed_ratio"),
            "interior_theta": area_s.get("interior_theta"),
            "boundary_theta": area_s.get("boundary_theta"),
            "interior_copula_k_ch_mixed_ratio": area_s.get("interior_copula_k_ch_mixed_ratio"),
            "max_relative_energy_drift": noether_s.get("max_relative_energy_drift"),
            "max_ternary_acceleration_norm": noether_s.get("max_ternary_acceleration_norm"),
            "shortcut_status": shortcut_s.get("status"),
            "shortcut_max_relative_residual": shortcut_s.get("max_relative_acceleration_residual"),
            "metric_status": metric_s.get("status"),
            "metric_mean_relative_residual": metric_s.get("mean_relative_homothety_residual"),
        },
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    p = result["selection_principle"]
    lines = [
        "# Z6 Canonical Bridge Certificate",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        "",
        "## Selection Principle",
        "",
        f"- Row: {p['row']}",
        f"- Observation map: {p['eta_base']}",
        f"- Ternary gate: {p['ternary_gate']}",
        f"- Physical projection: {p['physical_projection']}",
        f"- Residual policy: {p['residual_policy']}",
        "",
        "## Required Gates",
        "",
        f"- max base e-tangent mixed ratio: {s['max_base_e_tangent_mixed_ratio']:.6e}",
        f"- interior theta: {s['interior_theta']:.6e}",
        f"- boundary theta: {s['boundary_theta']:.6e}",
        f"- interior copula K_CH mixed ratio: {s['interior_copula_k_ch_mixed_ratio']:.6e}",
        f"- max relative energy drift: {s['max_relative_energy_drift']:.6e}",
        f"- max ternary acceleration norm: {s['max_ternary_acceleration_norm']:.6e}",
        f"- required failures: {s['required_failures']}",
        "",
        "## Control Kills",
        "",
        f"- algebraic shortcut status: {s['shortcut_status']}",
        f"- algebraic shortcut max residual: {s['shortcut_max_relative_residual']:.6e}",
        f"- metric homothety status: {s['metric_status']}",
        f"- metric mean relative residual: {s['metric_mean_relative_residual']:.6e}",
        "",
        "## Interpretation",
        "",
        "A PASS certifies the corrected finite-row prototype: eta is selected by",
        "minimal CRT structure, e-coordinate dyadic purity, and the scale-free",
        "Heron copula gate; Pi is selected variationally as Pi_EL. This does not",
        "claim a law of celestial motion. It clears the finite-row projection",
        "canonicity bottleneck by replacing arbitrary channel choice with a",
        "declared selection principle and by recording the remaining metric",
        "mismatch as typed projection overflow.",
        "",
    ]
    if s["control_notes"]:
        lines.append("## Notes")
        lines.append("")
        for note in s["control_notes"]:
            lines.append(f"- {note}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--e-purity-tol", type=float, default=1.0e-8)
    parser.add_argument("--theta-floor", type=float, default=1.0e-12)
    parser.add_argument("--boundary-theta-tol", type=float, default=1.0e-8)
    parser.add_argument("--spillover-floor", type=float, default=1.0e-12)
    parser.add_argument("--energy-drift-tol", type=float, default=1.0e-5)
    parser.add_argument("--ternary-floor", type=float, default=1.0e-10)
    parser.add_argument(
        "--area-json",
        type=Path,
        default=Path("empirical/reports/z6_area_gated_copula_audit.json"),
    )
    parser.add_argument(
        "--noether-json",
        type=Path,
        default=Path("empirical/reports/z6_el_projection_noether_audit.json"),
    )
    parser.add_argument(
        "--shortcut-json",
        type=Path,
        default=Path("empirical/reports/z6_copula_variational_consistency_audit.json"),
    )
    parser.add_argument(
        "--metric-json",
        type=Path,
        default=Path("empirical/reports/z6_gaussian_base_metric_audit.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_canonical_bridge_certificate.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_canonical_bridge_certificate.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
