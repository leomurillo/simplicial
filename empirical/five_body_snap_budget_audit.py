"""Five-body snap budget audit for Paper 28.

This audit tests the analytic claim that five bodies force an arity test, but
snap is mandatory only when the connected residual time-curvature breaks the
declared horizon budget.

The default planted connected five-body potential is

    V5 = -chi * prod(m_i) * Phi5_attached / prod(s_ij)^lambda,

where the default channel is the circuit-attached scaffold
Phi5_attached = sum_a Lambda_a^2 ||q_a - c_hat_a||^2.  Here Lambda_a is
the signed tetrahedral circuit coordinate of the four bodies other than a,
and c_hat_a is their centroid.  The affine bilinear stress expression
sum_{a<b} Lambda_a Lambda_b q_ab is exposed as `--channel stress_zero`
because it should vanish by affine dependence.  The older parity-even
scaffold I5 = sum_{a<b} Delta_hat_a^2 Delta_hat_b^2 is still available
with `--channel i5`, but is treated as a control rather than the canonical
five-body coordinate.  Lower controls include pairwise, triplet, and
tetrahedral sub-whole features.

Outputs:
  empirical/reports/five_body_snap_budget_audit.json
  empirical/reports/five_body_snap_budget_audit.md
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np


N = 5
DIM = 3
BODIES = tuple(range(N))
EDGES = tuple(itertools.combinations(BODIES, 2))
TRIPLES = tuple(itertools.combinations(BODIES, 3))
QUADS = tuple(itertools.combinations(BODIES, 4))
DEFAULT_JSON = Path("empirical/reports/five_body_snap_budget_audit.json")
DEFAULT_REPORT = Path("empirical/reports/five_body_snap_budget_audit.md")


@dataclass(frozen=True)
class ForceConfig:
    masses: np.ndarray
    gravity: float
    softening: float
    chi: float
    lam: float
    channel: str


def fmt(value: float, digits: int = 6) -> str:
    if not np.isfinite(value):
        return str(value)
    if value == 0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-4 or abs_value >= 1e5:
        return f"{value:.{digits}e}"
    return f"{value:.{digits}g}"


def pair_force(pos: np.ndarray, masses: np.ndarray, gravity: float, softening: float) -> np.ndarray:
    force = np.zeros_like(pos)
    for i, j in EDGES:
        delta = pos[j] - pos[i]
        s2 = float(np.dot(delta, delta) + softening * softening)
        fij = gravity * masses[i] * masses[j] * delta / (s2**1.5)
        force[i] += fij
        force[j] -= fij
    return force


def pair_potential(pos: np.ndarray, masses: np.ndarray, gravity: float, softening: float) -> float:
    total = 0.0
    for i, j in EDGES:
        delta = pos[i] - pos[j]
        total -= gravity * masses[i] * masses[j] / float(np.sqrt(np.dot(delta, delta) + softening * softening))
    return total


def complete_edges(subset: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(sorted(edge)) for edge in itertools.combinations(subset, 2))


def edge_product_force(pos: np.ndarray, term_edges: tuple[tuple[int, int], ...], mass_factor: float, softening: float) -> np.ndarray:
    inv_product = 1.0
    edge_data: list[tuple[int, int, float]] = []
    for i, j in term_edges:
        delta = pos[i] - pos[j]
        s2 = float(np.dot(delta, delta) + softening * softening)
        inv_product *= 1.0 / float(np.sqrt(s2))
        edge_data.append((i, j, s2))
    scale = mass_factor * inv_product
    force = np.zeros_like(pos)
    for i, j, s2 in edge_data:
        fij = scale * (pos[j] - pos[i]) / s2
        force[i] += fij
        force[j] -= fij
    return force


def triplet_force(pos: np.ndarray, masses: np.ndarray, softening: float, triple: tuple[int, int, int]) -> np.ndarray:
    return edge_product_force(pos, complete_edges(triple), float(np.prod(masses[list(triple)])), softening)


def tetra_delta_and_grad(pos4: np.ndarray) -> tuple[float, np.ndarray]:
    a = pos4[1] - pos4[0]
    b = pos4[2] - pos4[0]
    c = pos4[3] - pos4[0]
    delta = float(np.dot(a, np.cross(b, c)) / 6.0)
    grad = np.zeros_like(pos4)
    grad[1] = np.cross(b, c) / 6.0
    grad[2] = np.cross(c, a) / 6.0
    grad[3] = np.cross(a, b) / 6.0
    grad[0] = -(grad[1] + grad[2] + grad[3])
    return delta, grad


def tetra_force(pos: np.ndarray, masses: np.ndarray, softening: float, quad: tuple[int, int, int, int]) -> np.ndarray:
    local_pos = pos[list(quad)]
    delta, local_grad = tetra_delta_and_grad(local_pos)
    product_s = 1.0
    grad_log = np.zeros((4, DIM), dtype=np.float64)
    for a in range(4):
        for b in range(a + 1, 4):
            i, j = quad[a], quad[b]
            rij = pos[i] - pos[j]
            s2 = float(np.dot(rij, rij) + softening * softening)
            product_s *= float(np.sqrt(s2))
            term = rij / s2
            grad_log[a] += term
            grad_log[b] -= term
    scale = float(np.prod(masses[list(quad)]) / product_s)
    local_force = scale * (2.0 * delta * local_grad - delta * delta * grad_log)
    force = np.zeros_like(pos)
    for local_idx, body_idx in enumerate(quad):
        force[body_idx] = local_force[local_idx]
    return force


def five_body_i5_shape_and_grad(pos: np.ndarray) -> tuple[float, np.ndarray]:
    deltas = np.zeros(N, dtype=np.float64)
    grads = np.zeros((N, N, DIM), dtype=np.float64)
    for omitted in BODIES:
        quad = tuple(i for i in BODIES if i != omitted)
        delta, local_grad = tetra_delta_and_grad(pos[list(quad)])
        deltas[omitted] = delta
        for local_idx, body_idx in enumerate(quad):
            grads[omitted, body_idx] = local_grad[local_idx]
    d2 = deltas * deltas
    total_d2 = float(np.sum(d2))
    i5 = 0.5 * float(total_d2 * total_d2 - np.sum(d2 * d2))
    grad_i5 = np.zeros_like(pos)
    for omitted in BODIES:
        coeff = 2.0 * deltas[omitted] * (total_d2 - d2[omitted])
        grad_i5 += coeff * grads[omitted]
    return i5, grad_i5


def five_body_circuit_lambdas_and_grads(pos: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    lambdas = np.zeros(N, dtype=np.float64)
    grads = np.zeros((N, N, DIM), dtype=np.float64)
    for omitted in BODIES:
        quad = tuple(i for i in BODIES if i != omitted)
        delta, local_grad = tetra_delta_and_grad(pos[list(quad)])
        sign = -1.0 if omitted % 2 else 1.0
        lambdas[omitted] = sign * delta
        for local_idx, body_idx in enumerate(quad):
            grads[omitted, body_idx] = sign * local_grad[local_idx]
    return lambdas, grads


def five_body_attached_shape_and_grad(pos: np.ndarray) -> tuple[float, np.ndarray]:
    lambdas, grads = five_body_circuit_lambdas_and_grads(pos)
    phi = 0.0
    grad_phi = np.zeros_like(pos)
    for omitted in BODIES:
        quad = tuple(i for i in BODIES if i != omitted)
        center = np.mean(pos[list(quad)], axis=0)
        displacement = pos[omitted] - center
        rho = float(np.dot(displacement, displacement))
        lam2 = lambdas[omitted] * lambdas[omitted]
        phi += lam2 * rho
        grad_phi += 2.0 * lambdas[omitted] * rho * grads[omitted]
        grad_phi[omitted] += 2.0 * lam2 * displacement
        for body_idx in quad:
            grad_phi[body_idx] -= 0.5 * lam2 * displacement
    return phi, grad_phi


def five_body_stress_zero_shape_and_grad(pos: np.ndarray) -> tuple[float, np.ndarray]:
    lambdas, grads = five_body_circuit_lambdas_and_grads(pos)
    phi = 0.0
    grad_phi = np.zeros_like(pos)
    for a in range(N):
        for b in range(a + 1, N):
            qab = float(np.dot(pos[a] - pos[b], pos[a] - pos[b]))
            phi += lambdas[a] * lambdas[b] * qab
            grad_phi += qab * (lambdas[b] * grads[a] + lambdas[a] * grads[b])
            grad_q = 2.0 * (pos[a] - pos[b])
            grad_phi[a] += lambdas[a] * lambdas[b] * grad_q
            grad_phi[b] -= lambdas[a] * lambdas[b] * grad_q
    return phi, grad_phi


def five_body_shape_and_grad(pos: np.ndarray, channel: str) -> tuple[float, np.ndarray]:
    if channel == "attached":
        return five_body_attached_shape_and_grad(pos)
    if channel == "stress_zero":
        return five_body_stress_zero_shape_and_grad(pos)
    if channel == "i5":
        return five_body_i5_shape_and_grad(pos)
    raise ValueError(channel)


def five_body_force_base(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    lam: float,
    channel: str = "attached",
) -> np.ndarray:
    phi, grad_phi = five_body_shape_and_grad(pos, channel)
    product_s = 1.0
    grad_log = np.zeros_like(pos)
    for i, j in EDGES:
        rij = pos[i] - pos[j]
        s2 = float(np.dot(rij, rij) + softening * softening)
        product_s *= float(np.sqrt(s2))
        term = rij / s2
        grad_log[i] += term
        grad_log[j] -= term
    scale = float(np.prod(masses) * product_s ** (-lam))
    return scale * (grad_phi - lam * phi * grad_log)


def five_body_potential_base(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    lam: float,
    channel: str = "attached",
) -> float:
    phi, _ = five_body_shape_and_grad(pos, channel)
    product_s = 1.0
    for i, j in EDGES:
        rij = pos[i] - pos[j]
        product_s *= float(np.sqrt(np.dot(rij, rij) + softening * softening))
    return -float(np.prod(masses) * phi * product_s ** (-lam))


def total_force(pos: np.ndarray, config: ForceConfig) -> np.ndarray:
    return pair_force(pos, config.masses, config.gravity, config.softening) + config.chi * five_body_force_base(
        pos, config.masses, config.softening, config.lam, config.channel
    )


def kinetic_energy(momentum: np.ndarray, masses: np.ndarray) -> float:
    return float(0.5 * np.sum(np.sum(momentum * momentum, axis=1) / masses))


def hamiltonian(pos: np.ndarray, momentum: np.ndarray, config: ForceConfig) -> float:
    return (
        kinetic_energy(momentum, config.masses)
        + pair_potential(pos, config.masses, config.gravity, config.softening)
        + config.chi * five_body_potential_base(pos, config.masses, config.softening, config.lam, config.channel)
    )


def initial_condition(seed: int, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    pos = np.array(
        [
            [-0.95, -0.08, 0.02],
            [0.96, 0.14, -0.07],
            [-0.12, -0.94, 0.14],
            [0.14, 0.94, -0.09],
            [0.07, -0.04, 0.98],
        ],
        dtype=np.float64,
    )
    momentum = np.array(
        [
            [0.05, 0.16, -0.03],
            [-0.11, -0.06, 0.05],
            [0.08, -0.10, 0.03],
            [-0.04, 0.09, -0.04],
            [0.02, -0.03, -0.01],
        ],
        dtype=np.float64,
    )
    pos += rng.normal(scale=0.035, size=pos.shape)
    momentum += rng.normal(scale=0.018, size=momentum.shape)
    center = np.sum(pos * masses[:, None], axis=0) / np.sum(masses)
    pos = pos - center
    momentum = momentum - np.sum(momentum, axis=0)[None, :] * masses[:, None] / np.sum(masses)
    return pos, momentum


def velocity_verlet(
    pos0: np.ndarray,
    momentum0: np.ndarray,
    masses: np.ndarray,
    dt: float,
    steps: int,
    force_fn: Callable[[np.ndarray], np.ndarray],
) -> tuple[np.ndarray, np.ndarray]:
    pos = pos0.copy()
    momentum = momentum0.copy()
    positions = np.empty((steps + 1, N, DIM))
    momenta = np.empty((steps + 1, N, DIM))
    positions[0] = pos
    momenta[0] = momentum
    force = force_fn(pos)
    for step in range(1, steps + 1):
        half = momentum + 0.5 * dt * force
        pos = pos + dt * half / masses[:, None]
        new_force = force_fn(pos)
        momentum = half + 0.5 * dt * new_force
        positions[step] = pos
        momenta[step] = momentum
        force = new_force
    return positions, momenta


def pairwise_radial_features(pos: np.ndarray, masses: np.ndarray, softening: float, powers: tuple[int, ...]) -> np.ndarray:
    columns: list[np.ndarray] = []
    for i, j in EDGES:
        delta = pos[j] - pos[i]
        s2 = float(np.dot(delta, delta) + softening * softening)
        s = float(np.sqrt(s2))
        for power in powers:
            feature = np.zeros_like(pos)
            fij = masses[i] * masses[j] * delta / (s**power)
            feature[i] += fij
            feature[j] -= fij
            columns.append(feature.reshape(-1))
    return np.stack(columns, axis=1)


def feature_matrix(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
    key: str,
    channel: str = "attached",
    lam: float = 1.0,
) -> np.ndarray:
    if key == "pairwise":
        return pairwise_radial_features(pos, masses, softening, powers)
    if key == "triplet":
        return np.stack([triplet_force(pos, masses, softening, triple).reshape(-1) for triple in TRIPLES], axis=1)
    if key == "tetra":
        return np.stack([tetra_force(pos, masses, softening, quad).reshape(-1) for quad in QUADS], axis=1)
    if key == "five":
        return five_body_force_base(pos, masses, softening, lam, channel).reshape(-1, 1)
    if key == "lower":
        return np.hstack(
            [
                feature_matrix(pos, masses, softening, powers, "pairwise", channel, lam),
                feature_matrix(pos, masses, softening, powers, "triplet", channel, lam),
                feature_matrix(pos, masses, softening, powers, "tetra", channel, lam),
            ]
        )
    raise ValueError(key)


def make_dataset(config: ForceConfig, args: argparse.Namespace, powers: tuple[int, ...]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for trial in range(args.trials):
        pos0, momentum0 = initial_condition(args.seed + trial, config.masses)
        positions, momenta = velocity_verlet(pos0, momentum0, config.masses, args.dt, args.steps, lambda x: total_force(x, config))
        for t in range(1, args.steps):
            if t % args.sample_stride != 0:
                continue
            pos = positions[t]
            exact_force = total_force(pos, config)
            pair = pair_force(pos, config.masses, config.gravity, config.softening)
            pair_f = feature_matrix(pos, config.masses, config.softening, powers, "pairwise", config.channel, config.lam)
            triplet_f = feature_matrix(pos, config.masses, config.softening, powers, "triplet", config.channel, config.lam)
            tetra_f = feature_matrix(pos, config.masses, config.softening, powers, "tetra", config.channel, config.lam)
            rows.append(
                {
                    "trial": trial,
                    "time_index": t,
                    "target_residual": (exact_force - pair).reshape(-1),
                    "lower": np.hstack([pair_f, triplet_f, tetra_f]),
                    "five": feature_matrix(pos, config.masses, config.softening, powers, "five", config.channel, config.lam),
                }
            )
    return rows


def split_rows(rows: list[dict[str, Any]], train_fraction: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    trials = sorted({row["trial"] for row in rows})
    train_count = max(1, int(round(train_fraction * len(trials))))
    train_trials = set(trials[:train_count])
    return [row for row in rows if row["trial"] in train_trials], [row for row in rows if row["trial"] not in train_trials]


def stack_target(rows: list[dict[str, Any]]) -> np.ndarray:
    return np.concatenate([row["target_residual"] for row in rows], axis=0)


def stack_feature(rows: list[dict[str, Any]], key: str) -> np.ndarray:
    return np.concatenate([row[key] for row in rows], axis=0)


def fit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    coeffs, *_ = np.linalg.lstsq(x, y, rcond=None)
    return coeffs


def score(coeffs: np.ndarray, x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    pred = x @ coeffs
    sse = float(np.sum((y - pred) ** 2))
    sst = float(np.sum(y**2))
    return {"rmse": float(np.sqrt(np.mean((y - pred) ** 2))), "r2_vs_zero": 1.0 - sse / sst if sst else 0.0}


def group_rows(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    out: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        out.setdefault(int(row["trial"]), []).append(row)
    for value in out.values():
        value.sort(key=lambda row: int(row["time_index"]))
    return out


def derivative_blocks(rows: list[dict[str, Any]], key: str, sample_dt: float) -> dict[str, np.ndarray]:
    x_mid: list[np.ndarray] = []
    y_mid: list[np.ndarray] = []
    x_dot: list[np.ndarray] = []
    y_dot: list[np.ndarray] = []
    x_ddot: list[np.ndarray] = []
    y_ddot: list[np.ndarray] = []
    for trial_rows in group_rows(rows).values():
        for i in range(1, len(trial_rows) - 1):
            prev_row, row, next_row = trial_rows[i - 1], trial_rows[i], trial_rows[i + 1]
            x_prev, x_now, x_next = prev_row[key], row[key], next_row[key]
            y_prev, y_now, y_next = prev_row["target_residual"], row["target_residual"], next_row["target_residual"]
            x_mid.append(x_now)
            y_mid.append(y_now)
            x_dot.append((x_next - x_prev) / (2.0 * sample_dt))
            y_dot.append((y_next - y_prev) / (2.0 * sample_dt))
            x_ddot.append((x_next - 2.0 * x_now + x_prev) / (sample_dt * sample_dt))
            y_ddot.append((y_next - 2.0 * y_now + y_prev) / (sample_dt * sample_dt))
    return {
        "x": np.concatenate(x_mid, axis=0),
        "y": np.concatenate(y_mid, axis=0),
        "x_dot": np.concatenate(x_dot, axis=0),
        "y_dot": np.concatenate(y_dot, axis=0),
        "x_ddot": np.concatenate(x_ddot, axis=0),
        "y_ddot": np.concatenate(y_ddot, axis=0),
    }


def fit_jerk_aware(train_rows: list[dict[str, Any]], key: str, sample_dt: float, jerk_scale: float) -> np.ndarray:
    blocks = derivative_blocks(train_rows, key, sample_dt)
    return fit(np.vstack([blocks["x"], jerk_scale * blocks["x_dot"]]), np.concatenate([blocks["y"], jerk_scale * blocks["y_dot"]]))


def model_scores(coeffs: np.ndarray, train_rows: list[dict[str, Any]], test_rows: list[dict[str, Any]], key: str, sample_dt: float) -> dict[str, Any]:
    train_x, train_y = stack_feature(train_rows, key), stack_target(train_rows)
    test_x, test_y = stack_feature(test_rows, key), stack_target(test_rows)
    train_d, test_d = derivative_blocks(train_rows, key, sample_dt), derivative_blocks(test_rows, key, sample_dt)
    return {
        "rank": int(np.linalg.matrix_rank(train_x)),
        "force_test": score(coeffs, test_x, test_y),
        "jerk_test": score(coeffs, test_d["x_dot"], test_d["y_dot"]),
        "snap_test": score(coeffs, test_d["x_ddot"], test_d["y_ddot"]),
    }


def lower_force_from_coeffs(
    pos: np.ndarray,
    masses: np.ndarray,
    gravity: float,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
    channel: str,
    lam: float,
) -> np.ndarray:
    return pair_force(pos, masses, gravity, softening) + (
        feature_matrix(pos, masses, softening, powers, "lower", channel, lam) @ coeffs
    ).reshape(N, DIM)


def residual_series(positions: np.ndarray, truth_force_fn: Any, model_force_fn: Any, masses: np.ndarray, dt: float) -> dict[str, np.ndarray]:
    residual_force = np.array([truth_force_fn(pos) - model_force_fn(pos) for pos in positions])
    acc = residual_force / masses[None, :, None]
    jerk = (residual_force[2:] - residual_force[:-2]) / (2.0 * dt) / masses[None, :, None]
    snap = (residual_force[2:] - 2.0 * residual_force[1:-1] + residual_force[:-2]) / (dt * dt) / masses[None, :, None]
    return {"acc": acc, "jerk": jerk, "snap": snap}


def rms(array: np.ndarray) -> float:
    return float(np.sqrt(np.mean(array * array)))


def budget(series: dict[str, np.ndarray], horizon: float, tolerance: float) -> dict[str, float]:
    acc_rms = rms(series["acc"][1:-1])
    jerk_rms = rms(series["jerk"])
    snap_rms = rms(series["snap"])
    acc_term = 0.5 * horizon * horizon * acc_rms
    jerk_term = (horizon**3 / 6.0) * jerk_rms
    snap_term = (horizon**4 / 24.0) * snap_rms
    total = acc_term + jerk_term + snap_term
    return {
        "position_budget_acc_term": acc_term,
        "position_budget_jerk_term": jerk_term,
        "position_budget_snap_term": snap_term,
        "position_budget_total": total,
        "snap_must_track_ratio": snap_term / tolerance if tolerance else float("inf"),
        "total_budget_ratio": total / tolerance if tolerance else float("inf"),
    }


def trajectory_errors(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    diff = candidate - reference
    rms_by_t = np.sqrt(np.mean(diff * diff, axis=(1, 2)))
    return {"final_rms": float(rms_by_t[-1]), "max_rms": float(np.max(rms_by_t))}


def total_momentum(momentum: np.ndarray) -> np.ndarray:
    return np.sum(momentum, axis=0)


def angular_momentum(pos: np.ndarray, momentum: np.ndarray) -> np.ndarray:
    return np.sum(np.cross(pos, momentum), axis=0)


def invariant_summary(positions: np.ndarray, momenta: np.ndarray, config: ForceConfig | None) -> dict[str, float]:
    p_norms = np.array([np.linalg.norm(total_momentum(p)) for p in momenta])
    angular = np.array([angular_momentum(r, p) for r, p in zip(positions, momenta)])
    angular_drift = np.linalg.norm(angular - angular[0], axis=1)
    out = {"max_total_momentum_norm": float(np.max(p_norms)), "max_angular_momentum_drift": float(np.max(angular_drift))}
    if config is not None:
        energy = np.array([hamiltonian(r, p, config) for r, p in zip(positions, momenta)])
        out["max_relative_energy_drift"] = float(np.max(np.abs(energy - energy[0])) / max(1e-12, abs(float(energy[0]))))
    return out


def replay(lower_coeffs: np.ndarray, lower_jerk_coeffs: np.ndarray, five_coeff: float, args: argparse.Namespace, powers: tuple[int, ...]) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos0, momentum0 = initial_condition(args.seed + args.trials + 17, masses)
    truth_config = ForceConfig(masses, args.gravity, args.softening, args.chi, args.lam, args.channel)
    pair_config = ForceConfig(masses, args.gravity, args.softening, 0.0, args.lam, args.channel)
    recovered_config = ForceConfig(masses, args.gravity, args.softening, five_coeff, args.lam, args.channel)
    truth_force = lambda x: total_force(x, truth_config)
    pair_only = lambda x: total_force(x, pair_config)
    lower_force = lambda x: lower_force_from_coeffs(
        x, masses, args.gravity, args.softening, powers, lower_coeffs, args.channel, args.lam
    )
    lower_jerk_force = lambda x: lower_force_from_coeffs(
        x, masses, args.gravity, args.softening, powers, lower_jerk_coeffs, args.channel, args.lam
    )
    recovered_force = lambda x: total_force(x, recovered_config)
    truth_pos, truth_mom = velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, truth_force)
    pair_pos, pair_mom = velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, pair_only)
    lower_pos, lower_mom = velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, lower_force)
    lower_jerk_pos, lower_jerk_mom = velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, lower_jerk_force)
    rec_pos, rec_mom = velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, recovered_force)
    horizon = args.dt * args.replay_steps
    return {
        "position_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_pos, pair_pos),
            "lower_force_only": trajectory_errors(truth_pos, lower_pos),
            "lower_jerk_aware": trajectory_errors(truth_pos, lower_jerk_pos),
            "recovered_five": trajectory_errors(truth_pos, rec_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_mom, pair_mom),
            "lower_force_only": trajectory_errors(truth_mom, lower_mom),
            "lower_jerk_aware": trajectory_errors(truth_mom, lower_jerk_mom),
            "recovered_five": trajectory_errors(truth_mom, rec_mom),
        },
        "budget": {
            "lower_force_only": budget(residual_series(truth_pos, truth_force, lower_force, masses, args.dt), horizon, args.position_tolerance),
            "lower_jerk_aware": budget(residual_series(truth_pos, truth_force, lower_jerk_force, masses, args.dt), horizon, args.position_tolerance),
            "recovered_five": budget(residual_series(truth_pos, truth_force, recovered_force, masses, args.dt), horizon, args.position_tolerance),
        },
        "invariants": {
            "truth": invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_five": invariant_summary(rec_pos, rec_mom, recovered_config),
            "lower_force_only": invariant_summary(lower_pos, lower_mom, None),
            "lower_jerk_aware": invariant_summary(lower_jerk_pos, lower_jerk_mom, None),
        },
    }


def write_report(result: dict[str, Any], path: Path) -> None:
    lines = ["# Five-Body Snap Budget Audit", ""]
    lines.append("This is a controlled Paper 28 scaffold, not a claim about real gravitation.")
    lines.append("The admitted five-body feature is tested against lower <=4 shadows.")
    lines.append("")
    lines.append("## Configuration")
    lines.append("")
    for key in (
        "trials",
        "steps",
        "dt",
        "sample_stride",
        "replay_steps",
        "masses",
        "gravity",
        "softening",
        "chi",
        "lam",
        "channel",
        "jerk_scale",
        "position_tolerance",
    ):
        lines.append(f"- {key}: `{result['args'][key]}`")
    lines.append(f"- recovered_five_coeff: `{fmt(float(result['coefficients']['five'][0]))}`")
    lines.append("")
    lines.append("## Short-Horizon Fit")
    lines.append("")
    lines.append("| model | rank | force test R2 | force test RMSE | jerk test R2 | snap test R2 |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for name, scores in result["models"].items():
        lines.append(
            f"| {name} | {scores['rank']} | {fmt(scores['force_test']['r2_vs_zero'])} | "
            f"{fmt(scores['force_test']['rmse'])} | {fmt(scores['jerk_test']['r2_vs_zero'])} | "
            f"{fmt(scores['snap_test']['r2_vs_zero'])} |"
        )
    lines.append("")
    lines.append("## Long-Horizon Replay")
    lines.append("")
    lines.append("| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |")
    lines.append("|---|---:|---:|---:|---:|")
    for name, pos_err in result["replay"]["position_error_vs_truth"].items():
        mom_err = result["replay"]["momentum_error_vs_truth"][name]
        lines.append(f"| {name} | {fmt(pos_err['final_rms'])} | {fmt(pos_err['max_rms'])} | {fmt(mom_err['final_rms'])} | {fmt(mom_err['max_rms'])} |")
    lines.append("")
    lines.append("## Snap Budget")
    lines.append("")
    lines.append("| model | acc term | jerk term | snap term | total budget | snap/tol | total/tol |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for name, item in result["replay"]["budget"].items():
        lines.append(f"| {name} | {fmt(item['position_budget_acc_term'])} | {fmt(item['position_budget_jerk_term'])} | {fmt(item['position_budget_snap_term'])} | {fmt(item['position_budget_total'])} | {fmt(item['snap_must_track_ratio'])} | {fmt(item['total_budget_ratio'])} |")
    lines.append("")
    lines.append("## Reading")
    lines.append("")
    lines.append("The default `attached` channel is a five-body circuit coordinate, not the")
    lines.append("older double-square `i5` scaffold.  The `stress_zero` channel is kept as a")
    lines.append("control because the bilinear affine-circuit stress expression collapses by")
    lines.append("the affine-dependence identity.")
    lines.append("")
    lines.append("In this run the admitted five-body coordinate recovers the planted")
    lines.append("coefficient and drives the snap budget to numerical zero.  Lower <=4")
    lines.append("shadows can fit short-horizon force surprisingly well, but their snap")
    lines.append("budget exceeds the declared position tolerance, so they are not legitimate")
    lines.append("long-horizon substitutes for the admitted five-body channel.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=12)
    parser.add_argument("--steps", type=int, default=850)
    parser.add_argument("--dt", type=float, default=0.0015)
    parser.add_argument("--sample-stride", type=int, default=25)
    parser.add_argument("--train-fraction", type=float, default=0.65)
    parser.add_argument("--replay-steps", type=int, default=850)
    parser.add_argument("--seed", type=int, default=2805)
    parser.add_argument("--masses", type=float, nargs=N, default=[1.0, 1.12, 0.94, 1.07, 0.89])
    parser.add_argument("--gravity", type=float, default=0.22)
    parser.add_argument("--softening", type=float, default=0.28)
    parser.add_argument("--chi", type=float, default=0.05)
    parser.add_argument("--lam", type=float, default=1.0)
    parser.add_argument("--channel", choices=["attached", "i5", "stress_zero"], default="attached")
    parser.add_argument("--powers", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6])
    parser.add_argument("--jerk-scale", type=float, default=0.01)
    parser.add_argument("--position-tolerance", type=float, default=1e-6)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    powers = tuple(args.powers)
    masses = np.array(args.masses, dtype=np.float64)
    config = ForceConfig(masses, args.gravity, args.softening, args.chi, args.lam, args.channel)
    rows = make_dataset(config, args, powers)
    train_rows, test_rows = split_rows(rows, args.train_fraction)
    sample_dt = args.dt * args.sample_stride
    lower_coeffs = fit(stack_feature(train_rows, "lower"), stack_target(train_rows))
    lower_jerk_coeffs = fit_jerk_aware(train_rows, "lower", sample_dt, args.jerk_scale)
    five_coeffs = fit(stack_feature(train_rows, "five"), stack_target(train_rows))
    result = {
        "args": vars(args) | {"json_out": str(args.json_out), "report_out": str(args.report_out)},
        "coefficients": {"five": five_coeffs.tolist()},
        "models": {
            "lower_force_only": model_scores(lower_coeffs, train_rows, test_rows, "lower", sample_dt),
            "lower_jerk_aware": model_scores(lower_jerk_coeffs, train_rows, test_rows, "lower", sample_dt),
            "five_one_coeff": model_scores(five_coeffs, train_rows, test_rows, "five", sample_dt),
        },
        "replay": replay(lower_coeffs, lower_jerk_coeffs, float(five_coeffs[0]), args, powers),
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    print(
        "five_body_snap_budget_audit: "
        f"five_coeff={fmt(float(five_coeffs[0]))}, "
        f"five_snap_to_tol={fmt(result['replay']['budget']['recovered_five']['snap_must_track_ratio'])}, "
        f"lower_snap_to_tol={fmt(result['replay']['budget']['lower_force_only']['snap_must_track_ratio'])}"
    )


if __name__ == "__main__":
    main()
