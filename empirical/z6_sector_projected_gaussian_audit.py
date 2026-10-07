"""Audit the sector-projected Gaussian protocol for Paper 28, T*1'.

Candidate logits:

    L_{a,b} = a*rho + u*E_u(b) + w*E_w(b),

where (rho,u,w) are obtained from v_b=-lambda*s_b^2 by Helmert decomposition.

This tests the corrected proposal's finite claims:

1. D eta sector purity in V2+V3.
2. Interior K_CH mixed spillover.
3. Boundary mixed-spillover shutoff as one edge weight is sent to zero.

Important: the exponential of a sum of pure sector logits can still produce
mixed tangent components after normalization. This audit checks, rather than
assumes, sector purity.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_jacobi_fisher_execution_audit import fisher_inner, k_ch_uniform, project_to_basis, z6_basis


E_U = np.array([1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0), 0.0])
E_W = np.array([1.0 / math.sqrt(6.0), 1.0 / math.sqrt(6.0), -2.0 / math.sqrt(6.0)])


def helmert_from_squared_sides(sides: np.ndarray, lam: float) -> np.ndarray:
    v = -lam * sides * sides
    rho = float(np.mean(v))
    centered = v - rho
    u = float(np.dot(centered, E_U))
    w = float(np.dot(centered, E_W))
    return np.array([rho, u, w])


def eta_from_sigma(sigma: np.ndarray) -> np.ndarray:
    rho, u, w = sigma
    vals = []
    for a in (1.0, -1.0):
        for b in range(3):
            vals.append(math.exp(a * rho + u * E_U[b] + w * E_W[b]))
    raw = np.array(vals)
    return raw / float(np.sum(raw))


def jacobian_eta_sigma(sigma: np.ndarray, step: float) -> np.ndarray:
    jac = np.zeros((6, 3))
    for i in range(3):
        sp = sigma.copy()
        sm = sigma.copy()
        sp[i] += step
        sm[i] -= step
        jac[:, i] = (eta_from_sigma(sp) - eta_from_sigma(sm)) / (2.0 * step)
    return jac


def sector_norms(x: np.ndarray, basis: dict) -> dict:
    base = np.stack([basis["e_rho"], basis["e_u"], basis["e_w"]])
    mixed = basis["mixed"]
    base_coeffs = project_to_basis(x, base)
    mixed_coeffs = project_to_basis(x, mixed)
    total = math.sqrt(max(fisher_inner(x, x), 0.0))
    return {
        "base_norm": float(np.linalg.norm(base_coeffs)),
        "mixed_norm": float(np.linalg.norm(mixed_coeffs)),
        "base_ratio": float(np.linalg.norm(base_coeffs)) / max(total, 1.0e-300),
        "mixed_ratio": float(np.linalg.norm(mixed_coeffs)) / max(total, 1.0e-300),
        "total_norm": total,
    }


def audit_sigma(sigma: np.ndarray, velocity: np.ndarray, step: float, basis: dict) -> dict:
    jac = jacobian_eta_sigma(sigma, step)
    tangent_sector = [sector_norms(jac[:, i], basis) for i in range(3)]
    deta_v = jac @ velocity
    k = k_ch_uniform(deta_v, deta_v)
    return {
        "sigma": sigma.tolist(),
        "eta": eta_from_sigma(sigma).tolist(),
        "tangent_sector": tangent_sector,
        "k_ch_sector": sector_norms(k, basis),
    }


def audit(args: argparse.Namespace) -> dict:
    basis = z6_basis()
    interior_sides = np.array(args.sides, dtype=float)
    interior_sigma = helmert_from_squared_sides(interior_sides, args.lam)
    boundary_sides = np.array([args.sides[0], args.sides[1], args.boundary_side], dtype=float)
    boundary_sigma = helmert_from_squared_sides(boundary_sides, args.lam)
    velocity = np.array(args.velocity, dtype=float)
    interior = audit_sigma(interior_sigma, velocity, args.fd_step, basis)
    boundary = audit_sigma(boundary_sigma, velocity, args.fd_step, basis)

    max_tangent_mixed = max(s["mixed_ratio"] for s in interior["tangent_sector"])
    kills = []
    if max_tangent_mixed > args.tangent_mixed_tol:
        kills.append("D eta has mixed-sector leakage; base map is not V2+V3 sector-pure")
    if interior["k_ch_sector"]["mixed_ratio"] <= args.spillover_floor:
        kills.append("interior K_CH mixed spillover at floor")
    if boundary["k_ch_sector"]["mixed_ratio"] > args.boundary_mixed_tol:
        kills.append("boundary K_CH mixed spillover does not vanish")

    return {
        "claim_tested": "sector-projected Gaussian protocol sector purity, interior spillover, boundary shutoff",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "interior": interior,
        "boundary": boundary,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "interior_sigma": interior_sigma.tolist(),
            "boundary_sigma": boundary_sigma.tolist(),
            "max_tangent_mixed_ratio": max_tangent_mixed,
            "interior_k_ch_mixed_ratio": interior["k_ch_sector"]["mixed_ratio"],
            "boundary_k_ch_mixed_ratio": boundary["k_ch_sector"]["mixed_ratio"],
            "boundary_edge_probability_mass": float(sum(boundary["eta"][2::3])),
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Sector-Projected Gaussian Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- max tangent mixed ratio: {s['max_tangent_mixed_ratio']:.6e}",
        f"- interior K_CH mixed ratio: {s['interior_k_ch_mixed_ratio']:.6e}",
        f"- boundary K_CH mixed ratio: {s['boundary_k_ch_mixed_ratio']:.6e}",
        f"- boundary broken-edge probability mass: {s['boundary_edge_probability_mass']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Interpretation",
        "",
        "This audit checks the corrected Gaussian protocol rather than assuming it",
        "works. A KILL on tangent mixed ratio means the normalized exponential map",
        "still creates mixed-sector tangent components despite pure-sector logits.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lam", type=float, default=0.1)
    parser.add_argument("--sides", nargs=3, type=float, default=[1.0, 1.25, 1.55])
    parser.add_argument("--boundary-side", type=float, default=12.0)
    parser.add_argument("--velocity", nargs=3, type=float, default=[0.4, -0.2, 0.15])
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--tangent-mixed-tol", type=float, default=1.0e-8)
    parser.add_argument("--spillover-floor", type=float, default=1.0e-12)
    parser.add_argument("--boundary-mixed-tol", type=float, default=1.0e-6)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_sector_projected_gaussian_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_sector_projected_gaussian_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
