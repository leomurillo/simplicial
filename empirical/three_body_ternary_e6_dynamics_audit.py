"""E6 dynamics audit for Paper 28, Theorem 7.2.

This is the first dynamical audit for the regular three-channel witness.  It
integrates

    rdot = p / m
    pdot = Pi(K_CH(Deta v, Deta v))

for the reference diagonal channel used in the static audit and monitors total
angular momentum.  It deliberately marks E3_red as BLOCKED unless a concrete
reduced Lagrangian/energy functional is supplied.  That is not a failure of
the integrator; it is the honest status of the present data.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def center_state(r: np.ndarray, p: np.ndarray, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    total_m = float(np.sum(masses))
    r_cm = np.sum(masses[:, None] * r, axis=0) / total_m
    p_cm = np.sum(p, axis=0) / total_m
    return r - r_cm, p - masses[:, None] * p_cm


def initial_state(seed: int, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    r = rng.normal(size=(3, 3))
    r[2] += np.array([0.35, -0.21, 0.41])
    p = 0.15 * rng.normal(size=(3, 3))
    return center_state(r, p, masses)


def side_data(r: np.ndarray, delta: float) -> dict:
    d12 = np.linalg.norm(r[0] - r[1])
    d23 = np.linalg.norm(r[1] - r[2])
    d31 = np.linalg.norm(r[2] - r[0])
    s12 = math.sqrt(d12 * d12 + delta * delta)
    s23 = math.sqrt(d23 * d23 + delta * delta)
    s31 = math.sqrt(d31 * d31 + delta * delta)
    area16 = (
        2 * d12 * d12 * d23 * d23
        + 2 * d23 * d23 * d31 * d31
        + 2 * d31 * d31 * d12 * d12
        - d12**4
        - d23**4
        - d31**4
    )
    area16_reg = (
        2 * s12 * s12 * s23 * s23
        + 2 * s23 * s23 * s31 * s31
        + 2 * s31 * s31 * s12 * s12
        - s12**4
        - s23**4
        - s31**4
    )
    perimeter_sq = max((d12 + d23 + d31) ** 2, 1.0e-300)
    quality = math.sqrt(max(area16, 0.0)) / perimeter_sq
    return {"s": np.array([s12, s23, s31]), "area16_reg": area16_reg, "quality": quality}


def q_values(r: np.ndarray, delta: float) -> np.ndarray:
    data = side_data(r, delta)
    s12, s23, s31 = data["s"]
    if data["area16_reg"] <= 0:
        raise ValueError("regularized Heron area is nonpositive")
    return np.array(
        [
            math.log(s12 + s23 + s31),
            0.5 * math.log(data["area16_reg"]),
            math.log(s12 * s23 * s31),
        ]
    )


def numerical_jacobian(fn, x: np.ndarray, step: float) -> np.ndarray:
    flat = x.reshape(-1)
    y_size = fn(x).size
    jac = np.zeros((y_size, flat.size))
    for idx in range(flat.size):
        xp = flat.copy()
        xm = flat.copy()
        xp[idx] += step
        xm[idx] -= step
        jac[:, idx] = (fn(xp.reshape(x.shape)) - fn(xm.reshape(x.shape))) / (2 * step)
    return jac


def q_gradients(r: np.ndarray, delta: float, fd_step: float) -> np.ndarray:
    return numerical_jacobian(lambda x: q_values(x, delta), r, fd_step).reshape(3, 3, 3)


def force(r: np.ndarray, p: np.ndarray, masses: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    grads = q_gradients(r, args.delta, args.fd_step)
    v = p / masses[:, None]
    qdot = np.einsum("abi,bi->a", grads, v)

    # Reference diagonal channel C^alpha_{beta gamma}=delta_{alpha beta}delta_{beta gamma}.
    f = np.zeros_like(r)
    for alpha in range(3):
        f += args.epsilon**2 * grads[alpha] * qdot[alpha] ** 2
    return f


def rhs(y: np.ndarray, masses: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    r = y[:9].reshape(3, 3)
    p = y[9:].reshape(3, 3)
    dr = p / masses[:, None]
    dp = force(r, p, masses, args)
    return np.concatenate([dr.reshape(-1), dp.reshape(-1)])


def rk4_step(y: np.ndarray, dt: float, masses: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    k1 = rhs(y, masses, args)
    k2 = rhs(y + 0.5 * dt * k1, masses, args)
    k3 = rhs(y + 0.5 * dt * k2, masses, args)
    k4 = rhs(y + dt * k3, masses, args)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def angular_momentum(r: np.ndarray, p: np.ndarray) -> np.ndarray:
    return np.sum(np.cross(r, p), axis=0)


def total_momentum(p: np.ndarray) -> np.ndarray:
    return np.sum(p, axis=0)


def audit(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    r, p = initial_state(args.seed, masses)
    if side_data(r, args.delta)["quality"] < args.min_shape_quality:
        raise ValueError("initial state failed the nondegenerate-shape gate")
    y = np.concatenate([r.reshape(-1), p.reshape(-1)])

    l0 = angular_momentum(r, p)
    p0 = total_momentum(p)
    l_norm = max(float(np.linalg.norm(l0)), 1.0)
    p_norm = max(float(np.linalg.norm(p0)), 1.0)

    max_l_drift = 0.0
    max_p_drift = 0.0
    min_quality = float("inf")
    for _ in range(args.steps):
        y = rk4_step(y, args.dt, masses, args)
        r = y[:9].reshape(3, 3)
        p = y[9:].reshape(3, 3)
        quality = side_data(r, args.delta)["quality"]
        min_quality = min(min_quality, quality)
        if quality < args.min_shape_quality:
            break
        max_l_drift = max(max_l_drift, float(np.linalg.norm(angular_momentum(r, p) - l0)) / l_norm)
        max_p_drift = max(max_p_drift, float(np.linalg.norm(total_momentum(p) - p0)) / p_norm)

    kills = []
    if min_quality < args.min_shape_quality:
        kills.append("trajectory left the nondegenerate-shape gate")
    if max_l_drift > args.angular_tol:
        kills.append("angular momentum drift exceeded tolerance")
    if max_p_drift > args.momentum_tol:
        kills.append("linear momentum drift exceeded tolerance")

    return {
        "kill_conditions": {
            "E6_L": f"angular momentum relative drift > {args.angular_tol}",
            "E6_P": f"linear momentum relative drift > {args.momentum_tol}",
            "E6_E3_red": "BLOCKED until a concrete reduced Lagrangian/energy functional is supplied",
        },
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "summary": {
            "status": "PASS" if not kills else "KILL",
            "E3_red_status": "BLOCKED_NOT_EVALUATED",
            "max_angular_momentum_relative_drift": max_l_drift,
            "max_linear_momentum_relative_drift": max_p_drift,
            "min_shape_quality": min_quality,
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    summary = result["summary"]
    lines = [
        "# Three-Body Ternary E6 Dynamics Audit",
        "",
        "This audit integrates the reference Theorem 7.2 force and evaluates",
        "momentum and angular-momentum drift. It does not claim to evaluate",
        "E3_red until the reduced Lagrangian/energy functional is specified.",
        "",
        "## Kill Conditions",
        "",
    ]
    for key, value in result["kill_conditions"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Status: {summary['status']}",
            f"- E3_red status: {summary['E3_red_status']}",
            f"- max angular momentum relative drift: {summary['max_angular_momentum_relative_drift']:.6e}",
            f"- max linear momentum relative drift: {summary['max_linear_momentum_relative_drift']:.6e}",
            f"- min shape quality: {summary['min_shape_quality']:.6e}",
            f"- kills: {summary['kills']}",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--delta", type=float, default=0.15)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--seed", type=int, default=2863)
    parser.add_argument("--steps", type=int, default=400)
    parser.add_argument("--dt", type=float, default=2.0e-3)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--min-shape-quality", type=float, default=1.0e-3)
    parser.add_argument("--angular-tol", type=float, default=1.0e-8)
    parser.add_argument("--momentum-tol", type=float, default=1.0e-10)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/three_body_ternary_e6_dynamics_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/three_body_ternary_e6_dynamics_audit.json"),
    )
    args = parser.parse_args()

    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
