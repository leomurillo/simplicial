"""Z6 Jacobi-Fisher execution audit for Paper 28, T*1'.

This script executes the first finite-row test described in the manuscript:

1. Build the CRT sector basis for Z/6 ~= Z/2 x Z/3.
2. Use physical coordinates sigma=(rho,u,w), where rho is log perimeter and
   u,w are Helmert contrasts of log side lengths.
3. Numerically compute the mass-weighted shape metric G_shape in a fixed
   planar gauge.
4. Compare G_shape with the Fisher pullback of the sector-pure base map into
   V2 + V3.
5. Compute the mixed-sector spillover of K_CH for tangent velocities.

The result is an attack audit, not a proof.  A nonzero mixed spillover is only
useful if the metric matching and later E6 variational consistency also pass.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def z6_basis() -> dict[str, np.ndarray]:
    rows = [(a, b) for a in range(2) for b in range(3)]
    e2_raw = np.array([1.0 if a == 0 else -1.0 for a, _ in rows])
    e3a_raw = np.array([1.0, -1.0, 0.0] * 2)
    e3b_raw = np.array([1.0, 1.0, -2.0] * 2)

    def fisher_normalize(v: np.ndarray) -> np.ndarray:
        return v / math.sqrt(6.0 * float(np.dot(v, v)))

    e2 = fisher_normalize(e2_raw)
    e3a = fisher_normalize(e3a_raw)
    e3b = fisher_normalize(e3b_raw)
    mixed = []
    for e3 in (e3a, e3b):
        prod = e2_raw * (e3 / np.max(np.abs(e3)))
        mixed.append(fisher_normalize(prod - prod.mean()))
    return {"e_rho": e2, "e_u": e3a, "e_w": e3b, "mixed": np.stack(mixed), "rows": rows}


def fisher_inner(u: np.ndarray, v: np.ndarray) -> float:
    return 6.0 * float(np.dot(u, v))


def project_to_basis(x: np.ndarray, basis: np.ndarray) -> np.ndarray:
    return np.array([fisher_inner(x, b) for b in basis])


def tangent_projection(x: np.ndarray) -> np.ndarray:
    return x - x.mean()


def k_ch_uniform(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    # At p0=1/6, K_CH(u,v)=Pi((u*v)/p0)=Pi(6*u*v).
    return tangent_projection(6.0 * u * v)


def logs_from_sigma(sigma: np.ndarray) -> np.ndarray:
    rho, u, w = sigma
    contrasts = np.array(
        [
            u / math.sqrt(2.0) + w / math.sqrt(6.0),
            -u / math.sqrt(2.0) + w / math.sqrt(6.0),
            -2.0 * w / math.sqrt(6.0),
        ]
    )
    perimeter = math.exp(rho)
    mean_log = math.log(perimeter / float(np.sum(np.exp(contrasts))))
    return mean_log + contrasts


def sides_from_sigma(sigma: np.ndarray) -> np.ndarray:
    return np.exp(logs_from_sigma(sigma))


def triangle_positions_from_sides(sides: np.ndarray, masses: np.ndarray) -> np.ndarray:
    # sides are (s12, s23, s31).  Place r1=(0,0,0), r2=(s12,0,0), solve r3.
    s12, s23, s31 = sides
    x3 = (s31 * s31 + s12 * s12 - s23 * s23) / (2.0 * s12)
    y_sq = max(s31 * s31 - x3 * x3, 0.0)
    y3 = math.sqrt(y_sq)
    r = np.array([[0.0, 0.0, 0.0], [s12, 0.0, 0.0], [x3, y3, 0.0]])
    cm = np.sum(masses[:, None] * r, axis=0) / float(np.sum(masses))
    return r - cm


def shape_quality_from_sides(sides: np.ndarray) -> float:
    a, b, c = sides
    area16 = 2 * a * a * b * b + 2 * b * b * c * c + 2 * c * c * a * a - a**4 - b**4 - c**4
    return math.sqrt(max(area16, 0.0)) / max((a + b + c) ** 2, 1.0e-300)


def numerical_jacobian(fn, x: np.ndarray, step: float) -> np.ndarray:
    y0 = fn(x)
    jac = np.zeros((y0.size, x.size))
    for i in range(x.size):
        xp = x.copy()
        xm = x.copy()
        xp[i] += step
        xm[i] -= step
        jac[:, i] = (fn(xp).reshape(-1) - fn(xm).reshape(-1)) / (2 * step)
    return jac


def shape_metric(sigma: np.ndarray, masses: np.ndarray, step: float) -> np.ndarray:
    def r_of_sigma(sig: np.ndarray) -> np.ndarray:
        return triangle_positions_from_sides(sides_from_sigma(sig), masses)

    jac = numerical_jacobian(r_of_sigma, sigma, step).reshape(3, 3, 3)
    metric = np.zeros((3, 3))
    for mu in range(3):
        for nu in range(3):
            metric[mu, nu] = np.sum(masses[:, None] * jac[:, :, mu] * jac[:, :, nu])
    return 0.5 * (metric + metric.T)


def fisher_pullback(args: argparse.Namespace) -> np.ndarray:
    # Base map eta=p0+epsilon*(rho e_rho + u e_u + w e_w); basis is orthonormal.
    return args.epsilon**2 * np.eye(3)


def conformal_residual(fisher_pb: np.ndarray, g_shape: np.ndarray) -> tuple[float, float]:
    denom = float(np.sum(g_shape * g_shape))
    omega2 = float(np.sum(fisher_pb * g_shape) / denom)
    residual = fisher_pb - omega2 * g_shape
    rel = float(np.linalg.norm(residual) / max(np.linalg.norm(fisher_pb), 1.0e-300))
    return omega2, rel


def spillover_ratio(velocity: np.ndarray, basis: dict[str, np.ndarray], args: argparse.Namespace) -> dict:
    base = np.stack([basis["e_rho"], basis["e_u"], basis["e_w"]])
    tangent = args.epsilon * np.einsum("i,ij->j", velocity, base)
    k = k_ch_uniform(tangent, tangent)
    mixed_coeffs = project_to_basis(k, basis["mixed"])
    base_coeffs = project_to_basis(k, base)
    mixed_norm = float(np.linalg.norm(mixed_coeffs))
    total_norm = math.sqrt(max(fisher_inner(k, k), 0.0))
    return {
        "velocity": velocity.tolist(),
        "mixed_coefficients": mixed_coeffs.tolist(),
        "base_coefficients": base_coeffs.tolist(),
        "mixed_norm": mixed_norm,
        "total_norm": total_norm,
        "mixed_ratio": mixed_norm / max(total_norm, 1.0e-300),
    }


def audit(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    basis = z6_basis()
    gram = {
        name: fisher_inner(vec, vec)
        for name, vec in [("e_rho", basis["e_rho"]), ("e_u", basis["e_u"]), ("e_w", basis["e_w"])]
    }
    rng = np.random.default_rng(args.seed)
    samples = []
    kills = []
    for idx in range(args.samples):
        sigma = np.array(
            [
                rng.uniform(args.rho_min, args.rho_max),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
            ]
        )
        sides = sides_from_sigma(sigma)
        quality = shape_quality_from_sides(sides)
        if quality < args.min_shape_quality:
            samples.append({"index": idx, "evaluated": False, "sigma": sigma.tolist(), "quality": quality})
            continue
        g_shape = shape_metric(sigma, masses, args.fd_step)
        fisher_pb = fisher_pullback(args)
        omega2, rel = conformal_residual(fisher_pb, g_shape)
        velocity = rng.normal(size=3)
        spill = spillover_ratio(velocity, basis, args)
        samples.append(
            {
                "index": idx,
                "evaluated": True,
                "sigma": sigma.tolist(),
                "sides": sides.tolist(),
                "quality": quality,
                "G_shape": g_shape.tolist(),
                "fisher_pullback": fisher_pb.tolist(),
                "best_omega2": omega2,
                "conformal_relative_residual": rel,
                "spillover": spill,
            }
        )
    evaluated = [s for s in samples if s["evaluated"]]
    if not evaluated:
        kills.append("no samples passed the shape-quality gate")
        max_residual = float("inf")
        min_spillover = 0.0
    else:
        max_residual = max(s["conformal_relative_residual"] for s in evaluated)
        min_spillover = min(s["spillover"]["mixed_ratio"] for s in evaluated)
        if max_residual > args.conformal_tol:
            kills.append("linear Z6 base map is not conformal to G_shape within tolerance")
        if min_spillover <= args.spillover_floor:
            kills.append("mixed-sector K_CH spillover at floor")

    return {
        "claim_tested": "Z6 linear sector-pure Jacobi-Fisher base map plus K_CH mixed spillover",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "basis_gram": gram,
        "samples": samples,
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "max_conformal_relative_residual": max_residual,
            "min_mixed_spillover_ratio": min_spillover,
            "evaluated_samples": len(evaluated),
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    summary = result["summary"]
    lines = [
        "# Z6 Jacobi-Fisher Execution Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {summary['status']}",
        f"- evaluated samples: {summary['evaluated_samples']}",
        f"- max conformal relative residual: {summary['max_conformal_relative_residual']:.6e}",
        f"- min mixed spillover ratio: {summary['min_mixed_spillover_ratio']:.6e}",
        f"- kills: {summary['kills']}",
        "",
        "## Basis Gram",
        "",
    ]
    for key, value in result["basis_gram"].items():
        lines.append(f"- {key}: {value:.12f}")
    lines.extend(
        [
            "",
            "## Samples",
            "",
            "| idx | used | quality | conformal residual | mixed spillover ratio | omega^2 |",
            "|---:|:---:|---:|---:|---:|---:|",
        ]
    )
    for sample in result["samples"]:
        if not sample["evaluated"]:
            lines.append(f"| {sample['index']} | no | {sample['quality']:.6e} | -- | -- | -- |")
        else:
            lines.append(
                "| {index} | yes | {quality:.6e} | {conformal_relative_residual:.6e} | "
                "{spillover[mixed_ratio]:.6e} | {best_omega2:.6e} |".format(**sample)
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A KILL from the conformal residual means the naive linear sector-pure",
            "base map does not solve the Jacobi-Fisher isometry equation. A nonzero",
            "mixed spillover still matters: it shows the Z6 CRT tensor can generate",
            "a ternary mixed component once a valid base map is found.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--seed", type=int, default=606)
    parser.add_argument("--samples", type=int, default=8)
    parser.add_argument("--rho-min", type=float, default=-0.2)
    parser.add_argument("--rho-max", type=float, default=0.6)
    parser.add_argument("--contrast-radius", type=float, default=0.35)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--min-shape-quality", type=float, default=1.0e-3)
    parser.add_argument("--conformal-tol", type=float, default=1.0e-2)
    parser.add_argument("--spillover-floor", type=float, default=1.0e-12)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_jacobi_fisher_execution_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_jacobi_fisher_execution_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
