"""Audit the claimed homothety for the e-pure Gaussian base map.

Claim tested:
    (D eta_base)^* g_Fisher = lambda * G_shape

for the sector/product Gaussian-style base used in the Z6 copula protocol.
The audit computes the categorical Fisher pullback of eta_base(sigma) and
compares it to the physical mass-weighted shape metric up to best scalar.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from z6_area_gated_copula_audit import eta_independent
from z6_jacobi_fisher_execution_audit import shape_metric


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


def fisher_pullback_metric(sigma: np.ndarray, step: float) -> np.ndarray:
    eta = eta_independent(sigma)
    jac = numerical_jacobian(eta_independent, sigma, step)
    return jac.T @ np.diag(1.0 / eta) @ jac


def best_homothety_residual(g_pull: np.ndarray, g_shape: np.ndarray) -> tuple[float, float]:
    scale = float(np.sum(g_pull * g_shape) / max(np.sum(g_shape * g_shape), 1.0e-300))
    residual = g_pull - scale * g_shape
    rel = float(np.linalg.norm(residual) / max(np.linalg.norm(g_pull), 1.0e-300))
    return scale, rel


def audit(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    rng = np.random.default_rng(args.seed)
    samples = []
    kills = []
    for i in range(args.samples):
        sigma = np.array(
            [
                rng.uniform(args.rho_min, args.rho_max),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
            ]
        )
        g_pull = fisher_pullback_metric(sigma, args.fd_step)
        g_shape = shape_metric(sigma, masses, args.fd_step)
        scale, rel = best_homothety_residual(g_pull, g_shape)
        samples.append(
            {
                "index": i,
                "sigma": sigma.tolist(),
                "best_scale": scale,
                "relative_homothety_residual": rel,
                "pullback_metric": g_pull.tolist(),
                "shape_metric": g_shape.tolist(),
            }
        )
    max_rel = max(s["relative_homothety_residual"] for s in samples)
    if max_rel > args.homothety_tol:
        kills.append("Fisher pullback is not homothetic to G_shape within tolerance")
    return {
        "claim_tested": "e-pure Gaussian/product base Fisher pullback equals lambda times G_shape",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "samples": samples,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "max_relative_homothety_residual": max_rel,
            "mean_relative_homothety_residual": float(
                np.mean([s["relative_homothety_residual"] for s in samples])
            ),
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Gaussian Base Metric Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- max relative homothety residual: {s['max_relative_homothety_residual']:.6e}",
        f"- mean relative homothety residual: {s['mean_relative_homothety_residual']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Samples",
        "",
        "| idx | best scale | relative residual |",
        "|---:|---:|---:|",
    ]
    for sample in result["samples"]:
        lines.append(
            f"| {sample['index']} | {sample['best_scale']:.6e} | "
            f"{sample['relative_homothety_residual']:.6e} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A KILL means the discrete Z6 product/exponential base is not the",
            "continuous Gaussian statistical family whose Fisher metric recovers a",
            "Mahalanobis/Jacobi metric. The Cotton-York obstruction is therefore",
            "not annihilated by this argument.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--samples", type=int, default=8)
    parser.add_argument("--rho-min", type=float, default=-0.2)
    parser.add_argument("--rho-max", type=float, default=0.6)
    parser.add_argument("--contrast-radius", type=float, default=0.35)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--homothety-tol", type=float, default=1.0e-2)
    parser.add_argument("--seed", type=int, default=6676)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_gaussian_base_metric_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_gaussian_base_metric_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
