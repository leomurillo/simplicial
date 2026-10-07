"""Noether audit for the Euler-Lagrange-defined Z6 copula projection.

After the algebraic K_CH projection failed variational consistency, the
physical projection is defined as the Euler-Lagrange projection of the pulled
back autonomous copula Lagrangian.  This audit integrates that EL flow and
monitors the Jacobi energy

    E = <qdot, dL/dqdot> - L.

It also records the ternary acceleration deviation:

    a_ternary = a_EL(copula) - a_EL(independent base).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from z6_copula_variational_consistency_audit import (
    el_acceleration,
    grad_vel,
    lagrangian,
)


def energy(sigma: np.ndarray, sigmadot: np.ndarray, args: argparse.Namespace) -> float:
    momentum = grad_vel(sigma, sigmadot, args)
    return float(np.dot(sigmadot, momentum) - lagrangian(sigma, sigmadot, args))


def rhs(y: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    sigma = y[:3]
    sigmadot = y[3:]
    accel = el_acceleration(sigma, sigmadot, args)
    return np.concatenate([sigmadot, accel])


def rk4_step(y: np.ndarray, dt: float, args: argparse.Namespace) -> np.ndarray:
    k1 = rhs(y, args)
    k2 = rhs(y + 0.5 * dt * k1, args)
    k3 = rhs(y + 0.5 * dt * k2, args)
    k4 = rhs(y + dt * k3, args)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def audit(args: argparse.Namespace) -> dict:
    y = np.concatenate([np.array(args.sigma, dtype=float), np.array(args.sigmadot, dtype=float)])
    e0 = energy(y[:3], y[3:], args)
    e_scale = max(abs(e0), 1.0)
    max_energy_drift = 0.0
    max_ternary_accel = 0.0
    samples = []
    for step in range(args.steps + 1):
        sigma = y[:3]
        sigmadot = y[3:]
        e = energy(sigma, sigmadot, args)
        drift = abs(e - e0) / e_scale
        max_energy_drift = max(max_energy_drift, drift)
        a_copula = el_acceleration(sigma, sigmadot, args)
        a_base = el_acceleration(sigma, sigmadot, args, fixed_theta=0.0)
        ternary_norm = float(np.linalg.norm(a_copula - a_base))
        max_ternary_accel = max(max_ternary_accel, ternary_norm)
        if step in (0, args.steps // 2, args.steps):
            samples.append(
                {
                    "step": step,
                    "energy": e,
                    "relative_energy_drift": drift,
                    "ternary_acceleration_norm": ternary_norm,
                }
            )
        if step < args.steps:
            y = rk4_step(y, args.dt, args)
    kills = []
    if max_energy_drift > args.energy_tol:
        kills.append("EL copula energy drift exceeded tolerance")
    if max_ternary_accel <= args.ternary_floor:
        kills.append("copula-minus-independent ternary acceleration at floor")
    return {
        "claim_tested": "EL-defined Z6 copula projection conserves autonomous Jacobi energy numerically",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "initial_energy": e0,
            "max_relative_energy_drift": max_energy_drift,
            "max_ternary_acceleration_norm": max_ternary_accel,
            "kills": kills,
        },
        "samples": samples,
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 EL Projection Noether Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- initial energy: {s['initial_energy']:.12e}",
        f"- max relative energy drift: {s['max_relative_energy_drift']:.6e}",
        f"- max ternary acceleration norm: {s['max_ternary_acceleration_norm']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Samples",
        "",
        "| step | energy | relative drift | ternary acceleration norm |",
        "|---:|---:|---:|---:|",
    ]
    for sample in result["samples"]:
        lines.append(
            "| {step} | {energy:.12e} | {relative_energy_drift:.6e} | "
            "{ternary_acceleration_norm:.6e} |".format(**sample)
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This audit tests the projection definition that makes the physical flow",
            "Euler-Lagrange by construction. It does not validate the older algebraic",
            "K_CH force shortcut; that shortcut remains a residual diagnostic.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sigma", nargs=3, type=float, default=[0.2, 0.35, -0.15])
    parser.add_argument("--sigmadot", nargs=3, type=float, default=[0.18, -0.09, 0.06])
    parser.add_argument("--steps", type=int, default=24)
    parser.add_argument("--dt", type=float, default=2.0e-3)
    parser.add_argument("--kappa", type=float, default=0.8)
    parser.add_argument("--phi-coeffs", nargs=2, type=float, default=[1.0, 0.0])
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--variation-step", type=float, default=2.0e-5)
    parser.add_argument("--lstsq-rcond", type=float, default=1.0e-10)
    parser.add_argument("--energy-tol", type=float, default=1.0e-5)
    parser.add_argument("--ternary-floor", type=float, default=1.0e-10)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_el_projection_noether_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_el_projection_noether_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
