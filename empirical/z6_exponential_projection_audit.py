"""Audit the Z6 exponential projection protocol for Paper 28, T*1'.

Candidate map:

    eta_{a,b}(r) = exp(beta * a * U_b(r)) / Z(r),
    a in {-1,+1}, b in {1,2,3}.

This script checks three finite claims:

1. Sector purity of D eta in the Z6 CRT decomposition.
2. Mixed K_CH spillover away from the dyadic boundary.
3. Boundary behavior when two edge potentials are sent to zero.

It intentionally does not certify Cotton-York evasion or E6 variational
closure.  Those remain separate tests.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_jacobi_fisher_execution_audit import fisher_inner, k_ch_uniform, project_to_basis, z6_basis


def eta_from_u(u: np.ndarray, beta: float) -> np.ndarray:
    vals = []
    for a in (1.0, -1.0):
        for b in range(3):
            vals.append(math.exp(beta * a * u[b]))
    raw = np.array(vals)
    return raw / float(np.sum(raw))


def jacobian_eta_u(u: np.ndarray, beta: float, step: float) -> np.ndarray:
    jac = np.zeros((6, 3))
    for i in range(3):
        up = u.copy()
        um = u.copy()
        up[i] += step
        um[i] -= step
        jac[:, i] = (eta_from_u(up, beta) - eta_from_u(um, beta)) / (2.0 * step)
    return jac


def sector_norms(x: np.ndarray, basis: dict) -> dict:
    base = np.stack([basis["e_rho"], basis["e_u"], basis["e_w"]])
    mixed = basis["mixed"]
    base_coeffs = project_to_basis(x, base)
    mixed_coeffs = project_to_basis(x, mixed)
    total = math.sqrt(max(fisher_inner(x, x), 0.0))
    base_norm = float(np.linalg.norm(base_coeffs))
    mixed_norm = float(np.linalg.norm(mixed_coeffs))
    return {
        "base_norm": base_norm,
        "mixed_norm": mixed_norm,
        "base_ratio": base_norm / max(total, 1.0e-300),
        "mixed_ratio": mixed_norm / max(total, 1.0e-300),
        "total_norm": total,
    }


def audit_point(u: np.ndarray, args: argparse.Namespace, basis: dict) -> dict:
    eta = eta_from_u(u, args.beta)
    jac = jacobian_eta_u(u, args.beta, args.fd_step)
    tangent_sector = [sector_norms(jac[:, i], basis) for i in range(3)]
    v = np.array(args.velocity, dtype=float)
    deta_v = jac @ v
    k = k_ch_uniform(deta_v, deta_v)
    k_sector = sector_norms(k, basis)
    return {
        "u": u.tolist(),
        "eta": eta.tolist(),
        "tangent_sector": tangent_sector,
        "k_ch_sector": k_sector,
    }


def audit(args: argparse.Namespace) -> dict:
    basis = z6_basis()
    interior = audit_point(np.array(args.u, dtype=float), args, basis)
    boundary = audit_point(np.array([args.u[0], 0.0, 0.0], dtype=float), args, basis)
    kills = []
    max_tangent_mixed = max(s["mixed_ratio"] for s in interior["tangent_sector"])
    if max_tangent_mixed > args.tangent_mixed_tol:
        kills.append("D eta has mixed-sector leakage; base map is not V2+V3 sector-pure")
    if interior["k_ch_sector"]["mixed_ratio"] <= args.spillover_floor:
        kills.append("interior K_CH mixed spillover at floor")
    if boundary["k_ch_sector"]["mixed_ratio"] > args.boundary_mixed_tol:
        kills.append("dyadic-boundary K_CH mixed spillover does not vanish")
    return {
        "claim_tested": "Z6 exponential projection sector purity, interior spillover, and dyadic-boundary vanishing",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "interior": interior,
        "dyadic_boundary": boundary,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "max_tangent_mixed_ratio": max_tangent_mixed,
            "interior_k_ch_mixed_ratio": interior["k_ch_sector"]["mixed_ratio"],
            "boundary_k_ch_mixed_ratio": boundary["k_ch_sector"]["mixed_ratio"],
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Exponential Projection Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- max tangent mixed ratio: {s['max_tangent_mixed_ratio']:.6e}",
        f"- interior K_CH mixed ratio: {s['interior_k_ch_mixed_ratio']:.6e}",
        f"- dyadic-boundary K_CH mixed ratio: {s['boundary_k_ch_mixed_ratio']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Interpretation",
        "",
        "A PASS would support the exponential protocol as a sector-pure base map",
        "with interior ternary spillover and dyadic-boundary shutoff. A KILL means",
        "one of those advertised properties is false for the tested convention.",
        "This audit does not evaluate Cotton-York matching or E6 variational",
        "closure.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.3)
    parser.add_argument("--u", nargs=3, type=float, default=[1.1, 0.8, 0.55])
    parser.add_argument("--velocity", nargs=3, type=float, default=[0.4, -0.2, 0.15])
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--tangent-mixed-tol", type=float, default=1.0e-8)
    parser.add_argument("--spillover-floor", type=float, default=1.0e-12)
    parser.add_argument("--boundary-mixed-tol", type=float, default=1.0e-8)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_exponential_projection_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_exponential_projection_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
