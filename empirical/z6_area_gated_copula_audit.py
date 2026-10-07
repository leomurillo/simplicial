"""Audit an area-gated copula protocol for the Z6 projection problem.

Construction:

  P2(a) = softmax(a*rho)
  P3(b) = softmax(u*E_u(b)+w*E_w(b))
  eta(a,b) = P2(a) P3(b) [1 + theta * Phi(a,b)]

where Phi is a normalized V2xV3 cross-contrast and theta is proportional to the
scale-free Heron shape quality.  This audit tests:

1. Independent base tangent purity.
2. Controlled copula mixed tangent in the interior.
3. Interior K_CH mixed spillover.
4. Boundary shutoff when theta -> 0.
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


def softmax(x: np.ndarray) -> np.ndarray:
    y = x - np.max(x)
    e = np.exp(y)
    return e / float(np.sum(e))


def theta_from_sides(sides: np.ndarray, kappa: float) -> float:
    a, b, c = sides
    area16 = 2 * a * a * b * b + 2 * b * b * c * c + 2 * c * c * a * a - a**4 - b**4 - c**4
    area_sq = max(area16, 0.0) / 16.0
    # 432 A^2 / P^4 is dimensionless, symmetric, scale-free, zero on the
    # collinear/non-triangle boundary, and normalized to one at equilateral shape.
    perimeter = a + b + c
    quality = 432.0 * area_sq / max(perimeter**4, 1.0e-300)
    return kappa * quality


def marginals(sigma: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rho, u, w = sigma
    p2 = softmax(np.array([rho, -rho]))
    p3 = softmax(u * E_U + w * E_W)
    return p2, p3


def phi_cross(args: argparse.Namespace) -> np.ndarray:
    basis = z6_basis()
    mixed = basis["mixed"]
    coeffs = np.array(args.phi_coeffs, dtype=float)
    raw = coeffs @ mixed
    # Rescale so max absolute entry is 1; this makes positivity controlled by theta.
    return raw / max(float(np.max(np.abs(raw))), 1.0e-300)


def eta_independent(sigma: np.ndarray) -> np.ndarray:
    p2, p3 = marginals(sigma)
    return np.array([p2[a] * p3[b] for a in range(2) for b in range(3)])


def eta_copula(sigma: np.ndarray, theta: float, args: argparse.Namespace) -> np.ndarray:
    base = eta_independent(sigma)
    phi = phi_cross(args)
    eta = base * (1.0 + theta * phi)
    eta = eta / float(np.sum(eta))
    if np.any(eta <= 0):
        raise ValueError("copula left positive simplex; reduce kappa")
    return eta


def jacobian_eta(fn, sigma: np.ndarray, step: float) -> np.ndarray:
    jac = np.zeros((6, 3))
    for i in range(3):
        sp = sigma.copy()
        sm = sigma.copy()
        sp[i] += step
        sm[i] -= step
        jac[:, i] = (fn(sp) - fn(sm)) / (2.0 * step)
    return jac


def centered_log_eta_independent(sigma: np.ndarray) -> np.ndarray:
    logp = np.log(eta_independent(sigma))
    return logp - float(np.mean(logp))


def jacobian_log_eta(fn, sigma: np.ndarray, step: float) -> np.ndarray:
    jac = np.zeros((6, 3))
    for i in range(3):
        sp = sigma.copy()
        sm = sigma.copy()
        sp[i] += step
        sm[i] -= step
        jac[:, i] = (fn(sp) - fn(sm)) / (2.0 * step)
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


def audit_state(sigma: np.ndarray, theta: float, velocity: np.ndarray, args: argparse.Namespace, basis: dict) -> dict:
    j_base = jacobian_eta(eta_independent, sigma, args.fd_step)
    j_base_e = jacobian_log_eta(centered_log_eta_independent, sigma, args.fd_step)
    j_copula = jacobian_eta(lambda x: eta_copula(x, theta, args), sigma, args.fd_step)
    base_tangent = [sector_norms(j_base[:, i], basis) for i in range(3)]
    base_e_tangent = [sector_norms(j_base_e[:, i], basis) for i in range(3)]
    copula_tangent = [sector_norms(j_copula[:, i], basis) for i in range(3)]
    k_base = k_ch_uniform(j_base @ velocity, j_base @ velocity)
    k_copula = k_ch_uniform(j_copula @ velocity, j_copula @ velocity)
    return {
        "sigma": sigma.tolist(),
        "theta": theta,
        "eta_min": float(np.min(eta_copula(sigma, theta, args))),
        "base_tangent": base_tangent,
        "base_e_tangent": base_e_tangent,
        "copula_tangent": copula_tangent,
        "base_k_ch_sector": sector_norms(k_base, basis),
        "copula_k_ch_sector": sector_norms(k_copula, basis),
    }


def audit(args: argparse.Namespace) -> dict:
    basis = z6_basis()
    interior_sides = np.array(args.sides, dtype=float)
    boundary_sides = np.array([args.sides[0], args.sides[1], args.boundary_side], dtype=float)
    sigma = np.array(args.sigma, dtype=float)
    velocity = np.array(args.velocity, dtype=float)
    theta_interior = theta_from_sides(interior_sides, args.kappa)
    theta_boundary = theta_from_sides(boundary_sides, args.kappa)
    interior = audit_state(sigma, theta_interior, velocity, args, basis)
    boundary = audit_state(sigma, theta_boundary, velocity, args, basis)
    max_base_tangent_mixed = max(s["mixed_ratio"] for s in interior["base_tangent"])
    max_base_e_tangent_mixed = max(s["mixed_ratio"] for s in interior["base_e_tangent"])
    max_copula_tangent_mixed = max(s["mixed_ratio"] for s in interior["copula_tangent"])
    kills = []
    if max_base_e_tangent_mixed > args.base_e_mixed_tol:
        kills.append("independent base e-tangent is not sector-pure")
    if interior["copula_k_ch_sector"]["mixed_ratio"] <= args.spillover_floor:
        kills.append("interior copula K_CH mixed spillover at floor")
    if boundary["theta"] > args.boundary_theta_tol:
        kills.append("area gate theta does not shut off at boundary sample")
    if abs(boundary["copula_k_ch_sector"]["mixed_ratio"] - boundary["base_k_ch_sector"]["mixed_ratio"]) > args.boundary_ratio_delta_tol:
        kills.append("boundary copula K_CH does not reduce to independent-base K_CH")
    return {
        "claim_tested": "area-gated copula: pure independent base, controlled mixed interior, theta boundary shutoff",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "interior": interior,
        "boundary": boundary,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "max_base_tangent_mixed_ratio": max_base_tangent_mixed,
            "max_base_e_tangent_mixed_ratio": max_base_e_tangent_mixed,
            "max_copula_tangent_mixed_ratio": max_copula_tangent_mixed,
            "interior_theta": theta_interior,
            "boundary_theta": theta_boundary,
            "interior_copula_k_ch_mixed_ratio": interior["copula_k_ch_sector"]["mixed_ratio"],
            "boundary_copula_k_ch_mixed_ratio": boundary["copula_k_ch_sector"]["mixed_ratio"],
            "boundary_base_k_ch_mixed_ratio": boundary["base_k_ch_sector"]["mixed_ratio"],
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Area-Gated Copula Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- max base tangent mixed ratio: {s['max_base_tangent_mixed_ratio']:.6e}",
        f"- max base e-tangent mixed ratio: {s['max_base_e_tangent_mixed_ratio']:.6e}",
        f"- max copula tangent mixed ratio: {s['max_copula_tangent_mixed_ratio']:.6e}",
        f"- interior theta: {s['interior_theta']:.6e}",
        f"- boundary theta: {s['boundary_theta']:.6e}",
        f"- interior copula K_CH mixed ratio: {s['interior_copula_k_ch_mixed_ratio']:.6e}",
        f"- boundary copula K_CH mixed ratio: {s['boundary_copula_k_ch_mixed_ratio']:.6e}",
        f"- boundary base K_CH mixed ratio: {s['boundary_base_k_ch_mixed_ratio']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Interpretation",
        "",
        "This audit separates e-coordinate base purity from m-coordinate curvature",
        "and controlled physical copula mixing. A PASS does not yet prove",
        "Cotton-York matching or E6 variational closure;",
        "it only establishes that the area gate controls the mixed dependence in",
        "the advertised finite tests.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma", nargs=3, type=float, default=[0.2, 0.35, -0.15])
    parser.add_argument("--sides", nargs=3, type=float, default=[1.0, 1.15, 1.3])
    parser.add_argument("--boundary-side", type=float, default=100.0)
    parser.add_argument("--kappa", type=float, default=0.8)
    parser.add_argument("--phi-coeffs", nargs=2, type=float, default=[1.0, 0.0])
    parser.add_argument("--velocity", nargs=3, type=float, default=[0.4, -0.2, 0.15])
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--base-e-mixed-tol", type=float, default=1.0e-8)
    parser.add_argument("--spillover-floor", type=float, default=1.0e-12)
    parser.add_argument("--boundary-theta-tol", type=float, default=1.0e-5)
    parser.add_argument("--boundary-ratio-delta-tol", type=float, default=1.0e-5)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_area_gated_copula_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_area_gated_copula_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
