"""Local power-series fit for the Z6 Jacobi-Fisher conformal isometry.

We fit a sector-pure map

    eta_base = p0 + epsilon * (psi_rho e_rho + psi_u e_u + psi_w e_w)

near the equilateral/uniform configuration.  The psi components are quadratic
polynomials in centered coordinates x=(rho-rho0,u,w).  The target is

    (D eta)^* g_Fisher = Omega^2(x) G_shape(x),

with Omega^2 allowed to vary per sample.  This is a numerical local attack on
the PDE, not a proof of integrability.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

from z6_jacobi_fisher_execution_audit import shape_metric


def monomial_powers(degree: int) -> list[tuple[int, int, int]]:
    powers = []
    for total in range(1, degree + 1):
        for p in itertools.product(range(total + 1), repeat=3):
            if sum(p) == total:
                powers.append(p)
    return powers


def features(x: np.ndarray, powers: list[tuple[int, int, int]]) -> np.ndarray:
    return np.array([np.prod(x**np.array(power)) for power in powers])


def jac_features(x: np.ndarray, powers: list[tuple[int, int, int]]) -> np.ndarray:
    jac = np.zeros((len(powers), 3))
    for row, power in enumerate(powers):
        for col in range(3):
            if power[col] == 0:
                continue
            reduced = list(power)
            reduced[col] -= 1
            jac[row, col] = power[col] * np.prod(x**np.array(reduced))
    return jac


def unpack(params: np.ndarray, n_features: int) -> np.ndarray:
    return params.reshape(3, n_features)


def fisher_pullback(params: np.ndarray, x: np.ndarray, powers: list[tuple[int, int, int]], eps: float) -> np.ndarray:
    coeffs = unpack(params, len(powers))
    dpsi = coeffs @ jac_features(x, powers)
    return eps**2 * dpsi.T @ dpsi


def conformal_residual(fisher_pb: np.ndarray, g_shape: np.ndarray) -> tuple[np.ndarray, float, float]:
    omega2 = float(np.sum(fisher_pb * g_shape) / max(np.sum(g_shape * g_shape), 1.0e-300))
    residual = fisher_pb - omega2 * g_shape
    rel = float(np.linalg.norm(residual) / max(np.linalg.norm(fisher_pb), 1.0e-300))
    return residual, omega2, rel


def sample_points(args: argparse.Namespace) -> list[np.ndarray]:
    rng = np.random.default_rng(args.seed)
    points = [np.zeros(3)]
    for _ in range(args.samples - 1):
        points.append(rng.uniform(-args.radius, args.radius, size=3))
    return points


def loss_and_residual_vector(
    params: np.ndarray,
    xs: list[np.ndarray],
    g_shapes: list[np.ndarray],
    powers: list[tuple[int, int, int]],
    args: argparse.Namespace,
) -> tuple[float, np.ndarray, list[float]]:
    pieces = []
    rels = []
    for x, g_shape in zip(xs, g_shapes):
        fpb = fisher_pullback(params, x, powers, args.epsilon)
        residual, _, rel = conformal_residual(fpb, g_shape)
        pieces.append((residual / max(np.linalg.norm(fpb), 1.0e-300)).reshape(-1))
        rels.append(rel)
    vec = np.concatenate(pieces)
    return float(np.dot(vec, vec) / len(xs)), vec, rels


def finite_difference_gradient(fn, params: np.ndarray, step: float) -> np.ndarray:
    grad = np.zeros_like(params)
    for idx in range(params.size):
        pp = params.copy()
        pm = params.copy()
        pp[idx] += step
        pm[idx] -= step
        grad[idx] = (fn(pp) - fn(pm)) / (2 * step)
    return grad


def fit(args: argparse.Namespace) -> dict:
    powers = monomial_powers(args.degree)
    n_features = len(powers)
    rho0 = math.log(args.perimeter0)
    xs = sample_points(args)
    sigmas = [np.array([rho0, 0.0, 0.0]) + x for x in xs]
    masses = np.array(args.masses, dtype=float)
    g_shapes = [shape_metric(sigma, masses, args.fd_step) for sigma in sigmas]

    # Start with the naive linear map psi=(rho,u,w) in centered coordinates.
    params = np.zeros((3, n_features))
    power_index = {power: i for i, power in enumerate(powers)}
    for col, power in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        params[col, power_index[power]] = 1.0
    params = params.reshape(-1)

    def objective(p: np.ndarray) -> float:
        val, _, _ = loss_and_residual_vector(p, xs, g_shapes, powers, args)
        reg = args.regularization * float(np.dot(p, p))
        return val + reg

    history = []
    best = params.copy()
    best_loss = objective(params)
    step_size = args.learning_rate
    for iteration in range(args.iterations):
        grad = finite_difference_gradient(objective, params, args.grad_step)
        candidate = params - step_size * grad
        cand_loss = objective(candidate)
        if cand_loss < best_loss:
            params = candidate
            best = candidate.copy()
            best_loss = cand_loss
            step_size *= 1.05
        else:
            step_size *= 0.5
        if iteration % args.report_every == 0 or iteration == args.iterations - 1:
            _, _, rels = loss_and_residual_vector(best, xs, g_shapes, powers, args)
            history.append(
                {
                    "iteration": iteration,
                    "loss": best_loss,
                    "max_relative_residual": max(rels),
                    "mean_relative_residual": float(np.mean(rels)),
                    "step_size": step_size,
                }
            )

    naive_params = np.zeros((3, n_features))
    for col, power in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        naive_params[col, power_index[power]] = 1.0
    _, _, naive_rels = loss_and_residual_vector(naive_params.reshape(-1), xs, g_shapes, powers, args)
    _, _, fit_rels = loss_and_residual_vector(best, xs, g_shapes, powers, args)
    status = "PASS" if max(fit_rels) <= args.target_residual else "KILL"
    return {
        "claim_tested": "quadratic local sector-pure power series can solve Jacobi-Fisher conformal matching numerically",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "powers": powers,
        "history": history,
        "coefficients": unpack(best, n_features).tolist(),
        "summary": {
            "status": status,
            "naive_max_relative_residual": max(naive_rels),
            "fit_max_relative_residual": max(fit_rels),
            "fit_mean_relative_residual": float(np.mean(fit_rels)),
            "improvement_factor": max(naive_rels) / max(max(fit_rels), 1.0e-300),
            "kills": [] if status == "PASS" else ["local polynomial fit did not meet target residual"],
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Jacobi-Fisher Local Power-Series Fit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- naive max relative residual: {s['naive_max_relative_residual']:.6e}",
        f"- fit max relative residual: {s['fit_max_relative_residual']:.6e}",
        f"- fit mean relative residual: {s['fit_mean_relative_residual']:.6e}",
        f"- improvement factor: {s['improvement_factor']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## History",
        "",
        "| iteration | loss | max residual | mean residual | step size |",
        "|---:|---:|---:|---:|---:|",
    ]
    for h in result["history"]:
        lines.append(
            "| {iteration} | {loss:.6e} | {max_relative_residual:.6e} | "
            "{mean_relative_residual:.6e} | {step_size:.6e} |".format(**h)
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "PASS means the local power-series ansatz solved the sampled conformal",
            "matching problem to the target tolerance. KILL means this ansatz is",
            "still too rigid or the finite-row isometry equation is obstructed.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--perimeter0", type=float, default=3.0)
    parser.add_argument("--degree", type=int, default=2)
    parser.add_argument("--samples", type=int, default=12)
    parser.add_argument("--radius", type=float, default=0.08)
    parser.add_argument("--seed", type=int, default=6606)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--iterations", type=int, default=80)
    parser.add_argument("--learning-rate", type=float, default=1.0e-2)
    parser.add_argument("--grad-step", type=float, default=1.0e-5)
    parser.add_argument("--regularization", type=float, default=1.0e-8)
    parser.add_argument("--target-residual", type=float, default=1.0e-2)
    parser.add_argument("--report-every", type=int, default=10)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_jacobi_fisher_local_fit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_jacobi_fisher_local_fit.json"),
    )
    args = parser.parse_args()
    result = fit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
