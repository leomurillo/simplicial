"""Variational consistency audit for the Z6 area-gated copula protocol.

This is the final-gate audit proposed for Paper 28 T*1':

  a_IG = Pi(K_CH_eta(D eta v, D eta v))
  a_EL = Euler-Lagrange acceleration of
         L = 1/2 g_eta(D eta v, D eta v)
             + 1/3 T_eta(h, D eta v, D eta v)

The concrete choices here are intentionally minimal:

  - eta is the area-gated copula from z6_area_gated_copula_audit.
  - K_CH_eta(u,v)=Pi_0((u*v)/eta), the finite categorical Chentsov product.
  - Pi is the mass-metric least-squares pullback from simplex force covector
    to physical acceleration coordinates.
  - T_eta(h,u,u)=sum h_i u_i^2 / eta_i, the diagonal categorical cubic.

If this KILLs, the copula protocol has not closed E6.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_area_gated_copula_audit import eta_copula, theta_from_sides
from z6_jacobi_fisher_execution_audit import sides_from_sigma


def theta_sigma(sigma: np.ndarray, args: argparse.Namespace) -> float:
    return theta_from_sides(sides_from_sigma(sigma), args.kappa)


def eta_sigma(
    sigma: np.ndarray, args: argparse.Namespace, fixed_theta: float | None = None
) -> np.ndarray:
    theta = theta_sigma(sigma, args) if fixed_theta is None else fixed_theta
    return eta_copula(sigma, theta, args)


def tangent_projection(x: np.ndarray) -> np.ndarray:
    return x - float(np.mean(x))


def k_ch_eta(eta: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return tangent_projection((u * v) / eta)


def numerical_jacobian(fn, x: np.ndarray, step: float) -> np.ndarray:
    y0 = fn(x)
    jac = np.zeros((y0.size, x.size))
    for i in range(x.size):
        xp = x.copy()
        xm = x.copy()
        xp[i] += step
        xm[i] -= step
        jac[:, i] = (fn(xp) - fn(xm)) / (2.0 * step)
    return jac


def eta_jacobian(
    sigma: np.ndarray, args: argparse.Namespace, fixed_theta: float | None = None
) -> np.ndarray:
    return numerical_jacobian(lambda x: eta_sigma(x, args, fixed_theta), sigma, args.fd_step)


def fisher_metric(eta: np.ndarray) -> np.ndarray:
    return np.diag(1.0 / eta)


def lagrangian(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> float:
    eta = eta_sigma(sigma, args, fixed_theta)
    jac = eta_jacobian(sigma, args, fixed_theta)
    u = jac @ sigmadot
    h = eta - np.full(6, 1.0 / 6.0)
    kinetic = 0.5 * float(np.sum(u * u / eta))
    cubic = (1.0 / 3.0) * float(np.sum(h * u * u / eta))
    return kinetic + cubic


def grad_sigma(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    out = np.zeros(3)
    for i in range(3):
        sp = sigma.copy()
        sm = sigma.copy()
        sp[i] += args.variation_step
        sm[i] -= args.variation_step
        out[i] = (lagrangian(sp, sigmadot, args, fixed_theta) - lagrangian(sm, sigmadot, args, fixed_theta)) / (2.0 * args.variation_step)
    return out


def grad_vel(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    out = np.zeros(3)
    for i in range(3):
        vp = sigmadot.copy()
        vm = sigmadot.copy()
        vp[i] += args.variation_step
        vm[i] -= args.variation_step
        out[i] = (lagrangian(sigma, vp, args, fixed_theta) - lagrangian(sigma, vm, args, fixed_theta)) / (2.0 * args.variation_step)
    return out


def hessian_vv(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    out = np.zeros((3, 3))
    for i in range(3):
        vp = sigmadot.copy()
        vm = sigmadot.copy()
        vp[i] += args.variation_step
        vm[i] -= args.variation_step
        out[:, i] = (grad_vel(sigma, vp, args, fixed_theta) - grad_vel(sigma, vm, args, fixed_theta)) / (2.0 * args.variation_step)
    return 0.5 * (out + out.T)


def jac_grad_vel_sigma(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    out = np.zeros((3, 3))
    for i in range(3):
        sp = sigma.copy()
        sm = sigma.copy()
        sp[i] += args.variation_step
        sm[i] -= args.variation_step
        out[:, i] = (grad_vel(sp, sigmadot, args, fixed_theta) - grad_vel(sm, sigmadot, args, fixed_theta)) / (2.0 * args.variation_step)
    return out


def el_acceleration(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    hess = hessian_vv(sigma, sigmadot, args, fixed_theta)
    rhs = grad_sigma(sigma, sigmadot, args, fixed_theta) - jac_grad_vel_sigma(sigma, sigmadot, args, fixed_theta) @ sigmadot
    accel, *_ = np.linalg.lstsq(hess, rhs, rcond=args.lstsq_rcond)
    return accel


def ig_acceleration(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    args: argparse.Namespace,
    fixed_theta: float | None = None,
) -> np.ndarray:
    eta = eta_sigma(sigma, args, fixed_theta)
    jac = eta_jacobian(sigma, args, fixed_theta)
    u = jac @ sigmadot
    simplex_force = k_ch_eta(eta, u, u)
    # Pull back the simplex force to sigma acceleration via the Fisher normal equations.
    metric = jac.T @ fisher_metric(eta) @ jac
    covector = jac.T @ fisher_metric(eta) @ simplex_force
    accel, *_ = np.linalg.lstsq(metric, covector, rcond=args.lstsq_rcond)
    return accel


def audit(args: argparse.Namespace) -> dict:
    rng = np.random.default_rng(args.seed)
    samples = []
    kills = []
    for i in range(args.samples):
        sigma = np.array(args.sigma, dtype=float) + rng.uniform(-args.radius, args.radius, size=3)
        sigmadot = np.array(args.sigmadot, dtype=float) + rng.uniform(-args.velocity_radius, args.velocity_radius, size=3)
        fixed_theta = theta_sigma(sigma, args)
        a_el = el_acceleration(sigma, sigmadot, args)
        a_ig = ig_acceleration(sigma, sigmadot, args)
        residual = a_ig - a_el
        denom = max(float(np.linalg.norm(a_el)), float(np.linalg.norm(a_ig)), 1.0e-300)
        rel = float(np.linalg.norm(residual) / denom)
        a_el_frozen = el_acceleration(sigma, sigmadot, args, fixed_theta=fixed_theta)
        a_ig_frozen = ig_acceleration(sigma, sigmadot, args, fixed_theta=fixed_theta)
        frozen_residual = a_ig_frozen - a_el_frozen
        frozen_denom = max(
            float(np.linalg.norm(a_el_frozen)), float(np.linalg.norm(a_ig_frozen)), 1.0e-300
        )
        frozen_rel = float(np.linalg.norm(frozen_residual) / frozen_denom)
        samples.append(
            {
                "index": i,
                "sigma": sigma.tolist(),
                "sigmadot": sigmadot.tolist(),
                "theta": fixed_theta,
                "relative_acceleration_residual": rel,
                "frozen_theta_relative_acceleration_residual": frozen_rel,
                "el_acceleration_norm": float(np.linalg.norm(a_el)),
                "ig_acceleration_norm": float(np.linalg.norm(a_ig)),
                "frozen_el_acceleration_norm": float(np.linalg.norm(a_el_frozen)),
                "frozen_ig_acceleration_norm": float(np.linalg.norm(a_ig_frozen)),
            }
        )
    max_rel = max(s["relative_acceleration_residual"] for s in samples)
    max_frozen_rel = max(s["frozen_theta_relative_acceleration_residual"] for s in samples)
    if max_rel > args.consistency_tol:
        kills.append("copula IG acceleration is not Euler-Lagrange for L_copula")
    gradient_only = max_frozen_rel <= args.consistency_tol
    return {
        "claim_tested": "area-gated copula IG force equals Euler-Lagrange acceleration of pullback cubic Lagrangian",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "samples": samples,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "max_relative_acceleration_residual": max_rel,
            "max_frozen_theta_relative_acceleration_residual": max_frozen_rel,
            "mean_relative_acceleration_residual": float(
                np.mean([s["relative_acceleration_residual"] for s in samples])
            ),
            "mean_frozen_theta_relative_acceleration_residual": float(
                np.mean([s["frozen_theta_relative_acceleration_residual"] for s in samples])
            ),
            "area_gate_gradient_explains_failure": gradient_only,
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Copula Variational Consistency Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- max relative acceleration residual: {s['max_relative_acceleration_residual']:.6e}",
        f"- mean relative acceleration residual: {s['mean_relative_acceleration_residual']:.6e}",
        f"- max frozen-theta residual: {s['max_frozen_theta_relative_acceleration_residual']:.6e}",
        f"- mean frozen-theta residual: {s['mean_frozen_theta_relative_acceleration_residual']:.6e}",
        f"- area-gate gradient explains failure: {s['area_gate_gradient_explains_failure']}",
        f"- kills: {s['kills']}",
        "",
        "## Samples",
        "",
        "| idx | theta | residual | frozen-theta residual | EL accel norm | IG accel norm |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for sample in result["samples"]:
        lines.append(
            "| {index} | {theta:.6e} | {relative_acceleration_residual:.6e} | "
            "{frozen_theta_relative_acceleration_residual:.6e} | "
            "{el_acceleration_norm:.6e} | {ig_acceleration_norm:.6e} |".format(**sample)
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A PASS would close the E6 variational consistency gate for this concrete",
            "copula convention. A KILL means the information-geometric projection force",
            "is still not generated by the tested autonomous cubic Lagrangian. If the",
            "frozen-theta residual also stays large, the failure is broader than the",
            "area-gate gradient term alone.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma", nargs=3, type=float, default=[0.2, 0.35, -0.15])
    parser.add_argument("--sigmadot", nargs=3, type=float, default=[0.25, -0.12, 0.08])
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--radius", type=float, default=0.03)
    parser.add_argument("--velocity-radius", type=float, default=0.02)
    parser.add_argument("--kappa", type=float, default=0.8)
    parser.add_argument("--phi-coeffs", nargs=2, type=float, default=[1.0, 0.0])
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--variation-step", type=float, default=2.0e-5)
    parser.add_argument("--lstsq-rcond", type=float, default=1.0e-10)
    parser.add_argument("--consistency-tol", type=float, default=1.0e-3)
    parser.add_argument("--seed", type=int, default=6686)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_copula_variational_consistency_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_copula_variational_consistency_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
