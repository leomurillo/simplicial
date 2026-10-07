"""Four-body tetrahedral residual audit for Paper 28.

This is a controlled arity-resolution scaffold, not an astrophysical claim.
It asks whether a known connected 4-ary force channel can be recovered from
trajectories after pairwise Newtonian mechanics and lower-arity controls have
been priced.

The planted tetrahedral channel uses the parity-even potential

    V_4 = - beta * prod(m_i) * Delta_1234^2 / prod_{i<j} s_ij^gamma,

where Delta_1234 is the oriented tetrahedral volume and
s_ij = sqrt(|r_i-r_j|^2 + softening^2).  The force is derived analytically
from this translation/rotation invariant potential.

Outputs:
  empirical/reports/four_body_tetrahedral_residual_audit.json
  empirical/reports/four_body_tetrahedral_residual_audit.md
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np


DEFAULT_JSON = Path("empirical/reports/four_body_tetrahedral_residual_audit.json")
DEFAULT_REPORT = Path("empirical/reports/four_body_tetrahedral_residual_audit.md")
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
FACES = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
OPPOSITE_EDGE_IDXS = ((0, 5), (1, 4), (2, 3))
STAR_EDGE_IDXS = ((0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5))


@dataclass(frozen=True)
class ForceConfig:
    masses: np.ndarray
    gravity: float
    softening: float
    face_alpha: float
    beta: float
    gamma: float


def fmt(value: float, digits: int = 6) -> str:
    if not np.isfinite(value):
        return str(value)
    if value == 0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-4 or abs_value >= 1e5:
        return f"{value:.{digits}e}"
    return f"{value:.{digits}g}"


def args_safe_int(value: Any, default: int = 12) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def pair_force(pos: np.ndarray, masses: np.ndarray, gravity: float, softening: float) -> np.ndarray:
    force = np.zeros_like(pos, dtype=np.float64)
    for i, j in EDGES:
        delta = pos[j] - pos[i]
        s2 = float(np.dot(delta, delta) + softening * softening)
        fij = gravity * masses[i] * masses[j] * delta / (s2**1.5)
        force[i] += fij
        force[j] -= fij
    return force


def pair_potential(pos: np.ndarray, masses: np.ndarray, gravity: float, softening: float) -> float:
    potential = 0.0
    for i, j in EDGES:
        delta = pos[i] - pos[j]
        sij = float(np.sqrt(np.dot(delta, delta) + softening * softening))
        potential -= gravity * masses[i] * masses[j] / sij
    return potential


def face_triplet_force_base(pos: np.ndarray, masses: np.ndarray, softening: float, face: tuple[int, int, int]) -> np.ndarray:
    """Coefficient-free force from -prod(m_face)/(s_ab*s_ac*s_bc)."""
    force = np.zeros_like(pos, dtype=np.float64)
    local = list(face)
    sij: dict[tuple[int, int], float] = {}
    s2: dict[tuple[int, int], float] = {}
    for a in range(3):
        for b in range(a + 1, 3):
            i, j = local[a], local[b]
            delta = pos[i] - pos[j]
            value = float(np.dot(delta, delta) + softening * softening)
            key = (i, j) if i < j else (j, i)
            s2[key] = value
            sij[key] = float(np.sqrt(value))
    denom = 1.0
    for key in sij:
        denom *= sij[key]
    prefactor = float(np.prod(masses[local]) / denom)
    for i in local:
        acc = np.zeros(3, dtype=np.float64)
        for j in local:
            if i == j:
                continue
            key = (i, j) if i < j else (j, i)
            acc += (pos[j] - pos[i]) / s2[key]
        force[i] = prefactor * acc
    return force


def face_triplet_potential_base(
    pos: np.ndarray, masses: np.ndarray, softening: float, face: tuple[int, int, int]
) -> float:
    denom = 1.0
    for a in range(3):
        for b in range(a + 1, 3):
            i, j = face[a], face[b]
            delta = pos[i] - pos[j]
            denom *= float(np.sqrt(np.dot(delta, delta) + softening * softening))
    return -float(np.prod(masses[list(face)]) / denom)


def face_triplet_force_sum(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    force = np.zeros_like(pos, dtype=np.float64)
    for face in FACES:
        force += face_triplet_force_base(pos, masses, softening, face)
    return force


def face_triplet_potential_sum(pos: np.ndarray, masses: np.ndarray, softening: float) -> float:
    return float(sum(face_triplet_potential_base(pos, masses, softening, face) for face in FACES))


def tetra_delta_and_grad(pos: np.ndarray) -> tuple[float, np.ndarray]:
    a = pos[1] - pos[0]
    b = pos[2] - pos[0]
    c = pos[3] - pos[0]
    delta = float(np.dot(a, np.cross(b, c)) / 6.0)
    grad = np.zeros_like(pos, dtype=np.float64)
    grad[1] = np.cross(b, c) / 6.0
    grad[2] = np.cross(c, a) / 6.0
    grad[3] = np.cross(a, b) / 6.0
    grad[0] = -(grad[1] + grad[2] + grad[3])
    return delta, grad


def edge_lengths(pos: np.ndarray) -> np.ndarray:
    return np.array([float(np.linalg.norm(pos[i] - pos[j])) for i, j in EDGES], dtype=np.float64)


def shape_diagnostics(pos: np.ndarray) -> dict[str, float]:
    lengths = edge_lengths(pos)
    delta, _ = tetra_delta_and_grad(pos)
    return {
        "abs_tetra_volume": abs(delta),
        "edge_length_mean": float(np.mean(lengths)),
        "edge_length_cv": float(np.std(lengths) / max(np.mean(lengths), 1.0e-300)),
        "min_edge_length": float(np.min(lengths)),
        "max_edge_length": float(np.max(lengths)),
    }


def tetra_force_base(pos: np.ndarray, masses: np.ndarray, softening: float, gamma: float) -> np.ndarray:
    """Coefficient-free force from -prod(m)*Delta^2/prod(s_ij)^gamma."""
    delta, grad_delta = tetra_delta_and_grad(pos)
    product_s = 1.0
    grad_log = np.zeros_like(pos, dtype=np.float64)
    for i, j in EDGES:
        rij = pos[i] - pos[j]
        s2 = float(np.dot(rij, rij) + softening * softening)
        product_s *= float(np.sqrt(s2))
        term = rij / s2
        grad_log[i] += term
        grad_log[j] -= term
    scale = float(np.prod(masses) * product_s ** (-gamma))
    return scale * (2.0 * delta * grad_delta - gamma * delta * delta * grad_log)


def tetra_potential_base(pos: np.ndarray, masses: np.ndarray, softening: float, gamma: float) -> float:
    delta, _ = tetra_delta_and_grad(pos)
    product_s = 1.0
    for i, j in EDGES:
        rij = pos[i] - pos[j]
        product_s *= float(np.sqrt(np.dot(rij, rij) + softening * softening))
    return -float(np.prod(masses) * delta * delta * product_s ** (-gamma))


def total_force(pos: np.ndarray, config: ForceConfig) -> np.ndarray:
    return (
        pair_force(pos, config.masses, config.gravity, config.softening)
        + config.face_alpha * face_triplet_force_sum(pos, config.masses, config.softening)
        + config.beta * tetra_force_base(pos, config.masses, config.softening, config.gamma)
    )


def kinetic_energy(momentum: np.ndarray, masses: np.ndarray) -> float:
    return float(0.5 * np.sum(np.sum(momentum * momentum, axis=1) / masses))


def hamiltonian(pos: np.ndarray, momentum: np.ndarray, config: ForceConfig) -> float:
    return (
        kinetic_energy(momentum, config.masses)
        + pair_potential(pos, config.masses, config.gravity, config.softening)
        + config.face_alpha * face_triplet_potential_sum(pos, config.masses, config.softening)
        + config.beta * tetra_potential_base(pos, config.masses, config.softening, config.gamma)
    )


def total_momentum(momentum: np.ndarray) -> np.ndarray:
    return np.sum(momentum, axis=0)


def angular_momentum(pos: np.ndarray, momentum: np.ndarray) -> np.ndarray:
    return np.sum(np.cross(pos, momentum), axis=0)


def recenter(pos: np.ndarray, momentum: np.ndarray, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    center = np.sum(pos * masses[:, None], axis=0) / np.sum(masses)
    pos = pos - center
    momentum = momentum - np.sum(momentum, axis=0)[None, :] * masses[:, None] / np.sum(masses)
    return pos, momentum


def initial_condition(seed: int, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    pos = np.array(
        [
            [-0.90, -0.35, -0.20],
            [0.95, -0.28, 0.10],
            [0.04, 0.92, -0.15],
            [0.22, 0.18, 0.96],
        ],
        dtype=np.float64,
    )
    momentum = np.array(
        [
            [0.10, 0.42, -0.08],
            [-0.34, -0.16, 0.19],
            [0.25, -0.31, -0.12],
            [-0.01, 0.05, 0.01],
        ],
        dtype=np.float64,
    )
    pos += rng.normal(scale=0.04, size=pos.shape)
    momentum += rng.normal(scale=0.02, size=momentum.shape)
    return recenter(pos, momentum, masses)


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
    positions = np.empty((steps + 1, 4, 3), dtype=np.float64)
    momenta = np.empty((steps + 1, 4, 3), dtype=np.float64)
    positions[0] = pos
    momenta[0] = momentum
    force = force_fn(pos)
    for step in range(1, steps + 1):
        half_momentum = momentum + 0.5 * dt * force
        pos = pos + dt * half_momentum / masses[:, None]
        new_force = force_fn(pos)
        momentum = half_momentum + 0.5 * dt * new_force
        positions[step] = pos
        momenta[step] = momentum
        force = new_force
    return positions, momenta


def pairwise_radial_features(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
) -> np.ndarray:
    columns: list[np.ndarray] = []
    for i, j in EDGES:
        delta = pos[j] - pos[i]
        s2 = float(np.dot(delta, delta) + softening * softening)
        s = float(np.sqrt(s2))
        for power in powers:
            feature = np.zeros_like(pos, dtype=np.float64)
            fij = masses[i] * masses[j] * delta / (s**power)
            feature[i] += fij
            feature[j] -= fij
            columns.append(feature.reshape(-1))
    return np.stack(columns, axis=1)


def face_triplet_features(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return np.stack(
        [face_triplet_force_base(pos, masses, softening, face).reshape(-1) for face in FACES],
        axis=1,
    )


def pairwise_basis_force(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
) -> np.ndarray:
    return (pairwise_radial_features(pos, masses, softening, powers) @ coeffs).reshape(4, 3)


def face_basis_force(pos: np.ndarray, masses: np.ndarray, softening: float, coeffs: np.ndarray) -> np.ndarray:
    return (face_triplet_features(pos, masses, softening) @ coeffs).reshape(4, 3)


def q_from_pos(pos: np.ndarray) -> np.ndarray:
    return np.array([float(np.dot(pos[i] - pos[j], pos[i] - pos[j])) for i, j in EDGES], dtype=np.float64)


def cayley_menger_v2(q: np.ndarray) -> float:
    a, b, c, d, e, f = q
    matrix = np.array(
        [
            [0, 1, 1, 1, 1],
            [1, 0, a, b, c],
            [1, a, 0, d, e],
            [1, b, d, 0, f],
            [1, c, e, f, 0],
        ],
        dtype=np.float64,
    )
    return float(np.linalg.det(matrix) / 288.0)


def tetra_potential_base_q(q: np.ndarray, mass_product: float, softening: float, gamma: float) -> float:
    v2 = cayley_menger_v2(q)
    product_s = float(np.prod(np.sqrt(q + softening * softening)))
    return -mass_product * v2 * product_s ** (-gamma)


def face_potential_base_q(q: np.ndarray, masses: np.ndarray, softening: float) -> float:
    edge_to_idx = {edge: idx for idx, edge in enumerate(EDGES)}
    total = 0.0
    for face in FACES:
        denom = 1.0
        for a in range(3):
            for b in range(a + 1, 3):
                edge = tuple(sorted((face[a], face[b])))
                denom *= float(np.sqrt(q[edge_to_idx[edge]] + softening * softening))
        total -= float(np.prod(masses[list(face)]) / denom)
    return total


def mixed_derivative_q(fn: Callable[[np.ndarray], float], q: np.ndarray, idxs: tuple[int, ...], h: float) -> float:
    total = 0.0
    for mask in range(1 << len(idxs)):
        qq = q.copy()
        sign = 1.0
        for bit, idx in enumerate(idxs):
            if (mask >> bit) & 1:
                qq[idx] += h
            else:
                qq[idx] -= h
                sign *= -1.0
        total += sign * fn(qq)
    return float(total / ((2.0 * h) ** len(idxs)))


def c4_detector(pos: np.ndarray, config: ForceConfig, h: float) -> dict[str, Any]:
    q = q_from_pos(pos)
    mass_product = float(np.prod(config.masses))
    tetra_fn = lambda x: tetra_potential_base_q(x, mass_product, config.softening, config.gamma)
    face_fn = lambda x: face_potential_base_q(x, config.masses, config.softening)
    tetra_opp = [mixed_derivative_q(tetra_fn, q, idxs, h) for idxs in OPPOSITE_EDGE_IDXS]
    tetra_star = [mixed_derivative_q(tetra_fn, q, idxs, h) for idxs in STAR_EDGE_IDXS]
    face_opp = [mixed_derivative_q(face_fn, q, idxs, h) for idxs in OPPOSITE_EDGE_IDXS]
    face_star = [mixed_derivative_q(face_fn, q, idxs, h) for idxs in STAR_EDGE_IDXS]
    return {
        "q": q.tolist(),
        "tetra_opposite_edge_derivatives": tetra_opp,
        "tetra_vertex_star_derivatives": tetra_star,
        "face_opposite_edge_derivatives": face_opp,
        "face_vertex_star_derivatives": face_star,
        "tetra_opposite_edge_max_abs": float(max(abs(x) for x in tetra_opp)),
        "tetra_vertex_star_max_abs": float(max(abs(x) for x in tetra_star)),
        "face_opposite_edge_max_abs": float(max(abs(x) for x in face_opp)),
        "face_vertex_star_max_abs": float(max(abs(x) for x in face_star)),
        "tetra_c4_max_abs": float(max([abs(x) for x in tetra_opp + tetra_star])),
        "face_c4_max_abs": float(max([abs(x) for x in face_opp + face_star])),
    }


def heldout_trial_ids(trial_count: int, train_fraction: float) -> list[int]:
    train_count = max(1, int(round(train_fraction * trial_count)))
    return list(range(train_count, trial_count))


def c4_heldout_audit(dataset: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    trial_ids = heldout_trial_ids(len(dataset["trajectories"]), args.train_fraction)
    config = dataset["config"]
    samples: list[dict[str, Any]] = []
    for trial in trial_ids:
        positions = dataset["trajectories"][trial]["positions"]
        candidate_indices = np.linspace(
            args.sample_stride,
            len(positions) - args.sample_stride - 1,
            num=args.c4_holdout_samples_per_trial,
            dtype=int,
        )
        for time_index in candidate_indices:
            pos = positions[int(time_index)]
            detector = c4_detector(pos, config, args.c4_h)
            samples.append(
                {
                    "trial": trial,
                    "time_index": int(time_index),
                    "shape": shape_diagnostics(pos),
                    "detector": detector,
                    "tetra_to_face_c4_ratio": detector["tetra_c4_max_abs"]
                    / max(detector["face_c4_max_abs"], 1.0e-300),
                }
            )
    tetra_maxima = [s["detector"]["tetra_c4_max_abs"] for s in samples]
    face_maxima = [s["detector"]["face_c4_max_abs"] for s in samples]
    ratios = [s["tetra_to_face_c4_ratio"] for s in samples]
    volumes = [s["shape"]["abs_tetra_volume"] for s in samples]
    edge_cvs = [s["shape"]["edge_length_cv"] for s in samples]
    return {
        "trial_ids": trial_ids,
        "samples": samples,
        "summary": {
            "sample_count": len(samples),
            "min_abs_tetra_volume": float(min(volumes)),
            "min_edge_length_cv": float(min(edge_cvs)),
            "min_tetra_c4_max_abs": float(min(tetra_maxima)),
            "max_face_c4_max_abs": float(max(face_maxima)),
            "min_tetra_to_face_c4_ratio": float(min(ratios)),
            "max_tetra_opposite_edge_abs": float(
                max(s["detector"]["tetra_opposite_edge_max_abs"] for s in samples)
            ),
            "max_tetra_vertex_star_abs": float(
                max(s["detector"]["tetra_vertex_star_max_abs"] for s in samples)
            ),
        },
    }


def planar_degeneration_control(args: argparse.Namespace) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos = np.array(
        [
            [-0.80, -0.25, 0.0],
            [0.95, -0.18, 0.0],
            [0.12, 0.88, 0.0],
            [0.34, 0.19, 0.0],
        ],
        dtype=np.float64,
    )
    force = tetra_force_base(pos, masses, args.softening, args.gamma)
    potential = tetra_potential_base(pos, masses, args.softening, args.gamma)
    delta, _ = tetra_delta_and_grad(pos)
    return {
        "shape": shape_diagnostics(pos),
        "delta": delta,
        "tetra_force_norm": float(np.linalg.norm(force)),
        "tetra_potential_abs": abs(potential),
    }


def cluster_separation_control(args: argparse.Namespace) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    compact = np.array(
        [
            [-0.80, -0.25, -0.10],
            [0.95, -0.18, 0.06],
            [0.12, 0.88, -0.08],
            [0.34, 0.19, 1.05],
        ],
        dtype=np.float64,
    )
    separated = compact.copy()
    separated[3] = np.array([0.34, 0.19, args.cluster_radius])
    compact_force_norm = float(np.linalg.norm(tetra_force_base(compact, masses, args.softening, args.gamma)))
    separated_force_norm = float(np.linalg.norm(tetra_force_base(separated, masses, args.softening, args.gamma)))
    compact_potential = abs(tetra_potential_base(compact, masses, args.softening, args.gamma))
    separated_potential = abs(tetra_potential_base(separated, masses, args.softening, args.gamma))
    return {
        "cluster_radius": args.cluster_radius,
        "compact_shape": shape_diagnostics(compact),
        "separated_shape": shape_diagnostics(separated),
        "compact_force_norm": compact_force_norm,
        "separated_force_norm": separated_force_norm,
        "force_suppression_ratio": separated_force_norm / max(compact_force_norm, 1.0e-300),
        "compact_potential_abs": compact_potential,
        "separated_potential_abs": separated_potential,
        "potential_suppression_ratio": separated_potential / max(compact_potential, 1.0e-300),
    }


def make_dataset(
    face_alpha: float,
    beta: float,
    args: argparse.Namespace,
    powers: tuple[int, ...],
) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    config = ForceConfig(masses, args.gravity, args.softening, face_alpha, beta, args.gamma)
    rows: list[dict[str, Any]] = []
    trajectories: list[dict[str, Any]] = []
    for trial in range(args.trials):
        pos0, momentum0 = initial_condition(args.seed + trial, masses)
        positions, momenta = velocity_verlet(
            pos0,
            momentum0,
            masses,
            args.dt,
            args.steps,
            lambda x, cfg=config: total_force(x, cfg),
        )
        trajectories.append({"positions": positions, "momenta": momenta, "config": config})
        for t in range(1, args.steps):
            if t % args.sample_stride != 0:
                continue
            pos = positions[t]
            exact_force = total_force(pos, config)
            finite_difference_force = (momenta[t + 1] - momenta[t - 1]) / (2.0 * args.dt)
            pair = pair_force(pos, masses, args.gravity, args.softening)
            face_features = face_triplet_features(pos, masses, args.softening)
            tetra_feature = tetra_force_base(pos, masses, args.softening, args.gamma).reshape(-1)
            rows.append(
                {
                    "trial": trial,
                    "time_index": t,
                    "target_residual": (exact_force - pair).reshape(-1),
                    "finite_difference_residual": (finite_difference_force - pair).reshape(-1),
                    "pairwise_features": pairwise_radial_features(pos, masses, args.softening, powers),
                    "face_features": face_features,
                    "tetra_feature": tetra_feature,
                }
            )
    return {"rows": rows, "trajectories": trajectories, "config": config}


def split_rows(rows: list[dict[str, Any]], train_fraction: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    trials = sorted({row["trial"] for row in rows})
    train_count = max(1, int(round(train_fraction * len(trials))))
    train_trials = set(trials[:train_count])
    train = [row for row in rows if row["trial"] in train_trials]
    test = [row for row in rows if row["trial"] not in train_trials]
    return train, test


def stack_target(rows: list[dict[str, Any]], key: str = "target_residual") -> np.ndarray:
    return np.concatenate([row[key] for row in rows], axis=0)


def stack_feature(rows: list[dict[str, Any]], key: str) -> np.ndarray:
    if key == "tetra_feature":
        return np.concatenate([row[key][:, None] for row in rows], axis=0)
    if key in {"pairwise_features", "face_features"}:
        return np.concatenate([row[key] for row in rows], axis=0)
    if key == "lower_features":
        return np.concatenate([np.hstack([row["pairwise_features"], row["face_features"]]) for row in rows], axis=0)
    if key == "lower_plus_tetra":
        return np.concatenate(
            [np.hstack([row["pairwise_features"], row["face_features"], row["tetra_feature"][:, None]]) for row in rows],
            axis=0,
        )
    raise ValueError(key)


def fit_and_score(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray, y_test: np.ndarray) -> dict[str, Any]:
    coeffs, *_ = np.linalg.lstsq(x_train, y_train, rcond=None)
    pred_train = x_train @ coeffs
    pred_test = x_test @ coeffs
    train_sse = float(np.sum((y_train - pred_train) ** 2))
    test_sse = float(np.sum((y_test - pred_test) ** 2))
    train_sst = float(np.sum(y_train**2))
    test_sst = float(np.sum(y_test**2))
    return {
        "coefficients": coeffs.tolist(),
        "rank": int(np.linalg.matrix_rank(x_train)),
        "train_rmse": float(np.sqrt(np.mean((y_train - pred_train) ** 2))),
        "test_rmse": float(np.sqrt(np.mean((y_test - pred_test) ** 2))),
        "train_r2_vs_zero": 1.0 - train_sse / train_sst if train_sst > 0 else 0.0,
        "test_r2_vs_zero": 1.0 - test_sse / test_sst if test_sst > 0 else 0.0,
    }


def score_zero(y_train: np.ndarray, y_test: np.ndarray) -> dict[str, Any]:
    return {
        "train_rmse": float(np.sqrt(np.mean(y_train**2))),
        "test_rmse": float(np.sqrt(np.mean(y_test**2))),
        "train_r2_vs_zero": 0.0,
        "test_r2_vs_zero": 0.0,
    }


def shuffled_tetra_score(
    rows_train: list[dict[str, Any]],
    rows_test: list[dict[str, Any]],
    y_train: np.ndarray,
    y_test: np.ndarray,
    seed: int,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    train_features = [row["tetra_feature"].copy() for row in rows_train]
    test_features = [row["tetra_feature"].copy() for row in rows_test]
    rng.shuffle(train_features)
    rng.shuffle(test_features)
    x_train = np.concatenate([item[:, None] for item in train_features], axis=0)
    x_test = np.concatenate([item[:, None] for item in test_features], axis=0)
    return fit_and_score(x_train, y_train, x_test, y_test)


def random_same_rank_score(y_train: np.ndarray, y_test: np.ndarray, seed: int) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    x_train = rng.normal(size=(y_train.shape[0], 1))
    x_test = rng.normal(size=(y_test.shape[0], 1))
    return fit_and_score(x_train, y_train, x_test, y_test)


def evaluate_force_recovery(dataset: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    train_rows, test_rows = split_rows(dataset["rows"], args.train_fraction)
    y_train = stack_target(train_rows)
    y_test = stack_target(test_rows)
    finite_difference_train = stack_target(train_rows, key="finite_difference_residual")
    finite_difference_test = stack_target(test_rows, key="finite_difference_residual")
    return {
        "sample_count_train": len(train_rows),
        "sample_count_test": len(test_rows),
        "component_count_train": int(y_train.shape[0]),
        "component_count_test": int(y_test.shape[0]),
        "target_residual_rms_train": float(np.sqrt(np.mean(y_train**2))),
        "target_residual_rms_test": float(np.sqrt(np.mean(y_test**2))),
        "finite_difference_noise": {
            "train_rmse_finite_difference_minus_exact_force": float(
                np.sqrt(np.mean((finite_difference_train - y_train) ** 2))
            ),
            "test_rmse_finite_difference_minus_exact_force": float(
                np.sqrt(np.mean((finite_difference_test - y_test) ** 2))
            ),
        },
        "models": {
            "pairwise_null": score_zero(y_train, y_test),
            "pairwise_only_radial_basis": fit_and_score(
                stack_feature(train_rows, "pairwise_features"),
                y_train,
                stack_feature(test_rows, "pairwise_features"),
                y_test,
            ),
            "face_triplet_basis": fit_and_score(
                stack_feature(train_rows, "face_features"),
                y_train,
                stack_feature(test_rows, "face_features"),
                y_test,
            ),
            "lower_pairwise_plus_face": fit_and_score(
                stack_feature(train_rows, "lower_features"),
                y_train,
                stack_feature(test_rows, "lower_features"),
                y_test,
            ),
            "tetra_one_coefficient": fit_and_score(
                stack_feature(train_rows, "tetra_feature"),
                y_train,
                stack_feature(test_rows, "tetra_feature"),
                y_test,
            ),
            "lower_plus_tetra": fit_and_score(
                stack_feature(train_rows, "lower_plus_tetra"),
                y_train,
                stack_feature(test_rows, "lower_plus_tetra"),
                y_test,
            ),
            "shuffled_tetra_feature": shuffled_tetra_score(
                train_rows, test_rows, y_train, y_test, args.seed + 1000
            ),
            "random_same_rank_feature": random_same_rank_score(y_train, y_test, args.seed + 2000),
        },
    }


def trajectory_errors(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    diff = candidate - reference
    rms_by_t = np.sqrt(np.mean(diff * diff, axis=(1, 2)))
    return {
        "final_rms": float(rms_by_t[-1]),
        "max_rms": float(np.max(rms_by_t)),
        "mean_rms": float(np.mean(rms_by_t)),
    }


def invariant_summary(
    positions: np.ndarray,
    momenta: np.ndarray,
    config: ForceConfig | None,
) -> dict[str, float]:
    p_norms = np.array([np.linalg.norm(total_momentum(p)) for p in momenta])
    angular = np.array([angular_momentum(r, p) for r, p in zip(positions, momenta)])
    angular_drift = np.linalg.norm(angular - angular[0], axis=1)
    out = {
        "max_total_momentum_norm": float(np.max(p_norms)),
        "max_angular_momentum_drift": float(np.max(angular_drift)),
    }
    if config is not None:
        energy = np.array([hamiltonian(r, p, config) for r, p in zip(positions, momenta)])
        out["max_relative_energy_drift"] = float(
            np.max(np.abs(energy - energy[0])) / max(1e-12, abs(float(energy[0])))
        )
    return out


def divergence_audit(recovery: dict[str, Any], args: argparse.Namespace, powers: tuple[int, ...]) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos0, momentum0 = initial_condition(args.seed, masses)
    truth_config = ForceConfig(masses, args.gravity, args.softening, 0.0, args.beta, args.gamma)
    pair_config = ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.gamma)
    recovered_beta = float(recovery["models"]["tetra_one_coefficient"]["coefficients"][0])
    recovered_config = ForceConfig(masses, args.gravity, args.softening, 0.0, recovered_beta, args.gamma)
    pair_coeffs = np.array(recovery["models"]["pairwise_only_radial_basis"]["coefficients"])
    lower_coeffs = np.array(recovery["models"]["lower_pairwise_plus_face"]["coefficients"])
    pair_count = len(EDGES) * len(powers)
    lower_pair_coeffs = lower_coeffs[:pair_count]
    lower_face_coeffs = lower_coeffs[pair_count:]

    truth_pos, truth_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, truth_config)
    )
    pair_pos, pair_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, pair_config)
    )
    recovered_pos, recovered_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, recovered_config)
    )
    pair_basis_pos, pair_basis_mom = velocity_verlet(
        pos0,
        momentum0,
        masses,
        args.dt,
        args.steps,
        lambda x: pair_force(x, masses, args.gravity, args.softening)
        + pairwise_basis_force(x, masses, args.softening, powers, pair_coeffs),
    )
    lower_pos, lower_mom = velocity_verlet(
        pos0,
        momentum0,
        masses,
        args.dt,
        args.steps,
        lambda x: pair_force(x, masses, args.gravity, args.softening)
        + pairwise_basis_force(x, masses, args.softening, powers, lower_pair_coeffs)
        + face_basis_force(x, masses, args.softening, lower_face_coeffs),
    )

    return {
        "trial": 0,
        "true_beta": args.beta,
        "recovered_beta": recovered_beta,
        "position_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_pos, pair_pos),
            "pairwise_only_radial_basis": trajectory_errors(truth_pos, pair_basis_pos),
            "lower_pairwise_plus_face": trajectory_errors(truth_pos, lower_pos),
            "recovered_tetra": trajectory_errors(truth_pos, recovered_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_mom, pair_mom),
            "pairwise_only_radial_basis": trajectory_errors(truth_mom, pair_basis_mom),
            "lower_pairwise_plus_face": trajectory_errors(truth_mom, lower_mom),
            "recovered_tetra": trajectory_errors(truth_mom, recovered_mom),
        },
        "invariants": {
            "truth": invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_tetra": invariant_summary(recovered_pos, recovered_mom, recovered_config),
            "pairwise_only_radial_basis": invariant_summary(pair_basis_pos, pair_basis_mom, None),
            "lower_pairwise_plus_face": invariant_summary(lower_pos, lower_mom, None),
        },
        "c4_detector_first_sample": c4_detector(truth_pos[0], truth_config, args.c4_h),
    }


def arity_gate_summary(
    null_recovery: dict[str, Any],
    face_recovery: dict[str, Any],
    tetra_recovery: dict[str, Any],
    divergence: dict[str, Any],
    c4_heldout: dict[str, Any],
    planar: dict[str, Any],
    cluster: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    null_tetra_coeff = abs(float(null_recovery["models"]["tetra_one_coefficient"]["coefficients"][0]))
    face_tetra_r2 = float(face_recovery["models"]["tetra_one_coefficient"]["test_r2_vs_zero"])
    face_basis_r2 = float(face_recovery["models"]["face_triplet_basis"]["test_r2_vs_zero"])
    lower_tetra_r2 = float(tetra_recovery["models"]["lower_pairwise_plus_face"]["test_r2_vs_zero"])
    tetra_r2 = float(tetra_recovery["models"]["tetra_one_coefficient"]["test_r2_vs_zero"])
    recovered_beta = float(tetra_recovery["models"]["tetra_one_coefficient"]["coefficients"][0])
    beta_error = abs(recovered_beta - args.beta)
    replay_lower_final = float(divergence["position_error_vs_truth"]["lower_pairwise_plus_face"]["final_rms"])
    replay_tetra_final = float(divergence["position_error_vs_truth"]["recovered_tetra"]["final_rms"])
    c4s = c4_heldout["summary"]
    kills: list[str] = []
    if null_tetra_coeff > args.null_tetra_coeff_tol:
        kills.append("tetra feature hallucinated under pairwise null")
    if face_basis_r2 < args.face_r2_floor:
        kills.append("face planted regime was not recovered by face features")
    if face_tetra_r2 > args.face_tetra_leakage_max:
        kills.append("tetra feature overfit face-only planted data")
    if lower_tetra_r2 > args.lower_tetra_r2_max:
        kills.append("lower edge-plus-face features absorbed too much planted tetrahedral residual")
    if tetra_r2 < args.tetra_r2_floor:
        kills.append("tetra feature failed to explain planted tetrahedral residual")
    if beta_error > args.beta_tol:
        kills.append("recovered tetrahedral coefficient missed planted beta")
    if replay_tetra_final > args.replay_tetra_final_tol:
        kills.append("recovered tetra replay diverged from truth")
    if replay_lower_final <= args.replay_lower_min_final:
        kills.append("lower-arity replay tracked tetra truth too well")
    if c4s["min_abs_tetra_volume"] < args.heldout_volume_floor:
        kills.append("held-out tetrahedra include near-planar samples")
    if c4s["min_edge_length_cv"] < args.heldout_edge_cv_floor:
        kills.append("held-out tetrahedra are not sufficiently asymmetric")
    if c4s["min_tetra_c4_max_abs"] < args.c4_tetra_floor:
        kills.append("held-out tetra C4 detector fell below floor")
    if c4s["max_face_c4_max_abs"] > args.c4_face_tol:
        kills.append("face control C4 detector exceeded tolerance")
    if c4s["min_tetra_to_face_c4_ratio"] < args.c4_ratio_floor:
        kills.append("held-out tetra C4 detector did not dominate face control")
    if planar["tetra_force_norm"] > args.planar_force_tol or planar["tetra_potential_abs"] > args.planar_potential_tol:
        kills.append("planar degeneration did not suppress tetrahedral channel")
    if cluster["force_suppression_ratio"] > args.cluster_force_ratio_tol:
        kills.append("cluster separation did not suppress tetrahedral force enough")
    return {
        "status": "PASS_ARITY_RESOLUTION_GATE" if not kills else "KILL",
        "kills": kills,
        "null_tetra_coefficient_abs": null_tetra_coeff,
        "face_basis_test_r2": face_basis_r2,
        "face_tetra_feature_test_r2": face_tetra_r2,
        "tetra_lower_pairwise_plus_face_test_r2": lower_tetra_r2,
        "tetra_feature_test_r2": tetra_r2,
        "recovered_beta": recovered_beta,
        "beta_error": beta_error,
        "replay_lower_final_position_rms": replay_lower_final,
        "replay_tetra_final_position_rms": replay_tetra_final,
        "heldout_c4": c4s,
        "planar_control": {
            "tetra_force_norm": planar["tetra_force_norm"],
            "tetra_potential_abs": planar["tetra_potential_abs"],
        },
        "cluster_control": {
            "force_suppression_ratio": cluster["force_suppression_ratio"],
            "potential_suppression_ratio": cluster["potential_suppression_ratio"],
        },
    }


def compact_model_table(models: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name, item in models.items():
        row = {
            "model": name,
            "rank": item.get("rank", 0),
            "train_rmse": item["train_rmse"],
            "test_rmse": item["test_rmse"],
            "train_r2": item["train_r2_vs_zero"],
            "test_r2": item["test_r2_vs_zero"],
        }
        if "coefficients" in item and len(item["coefficients"]) == 1:
            row["coefficient"] = item["coefficients"][0]
        rows.append(row)
    return rows


def write_report(result: dict[str, Any], path: Path) -> None:
    tetra = result["tetra_planted"]
    face = result["face_planted"]
    null = result["null"]
    div = result["divergence_audit"]
    c4 = div["c4_detector_first_sample"]
    gate = result["arity_gate_summary"]
    c4_heldout = result["c4_heldout"]
    planar = result["planar_degenerated_control"]
    cluster = result["cluster_separation_control"]
    lines: list[str] = []
    lines.append("# Four-Body Tetrahedral Residual Audit")
    lines.append("")
    lines.append("This is a controlled Paper 28 arity-resolution scaffold, not a claim about real gravitation.")
    lines.append("The null is softened pairwise Newtonian mechanics. The tetrahedral planted alternative adds")
    lines.append("`V4 = -beta*prod(m_i)*Delta_1234^2/prod(s_ij)^gamma`.")
    lines.append("")
    lines.append("## Gate Verdict")
    lines.append("")
    lines.append(f"- Status: `{gate['status']}`")
    lines.append(f"- kills: `{gate['kills']}`")
    lines.append(f"- recovered beta: `{fmt(gate['recovered_beta'])}`")
    lines.append(f"- lower edge-plus-face held-out R2 on tetra planting: `{fmt(gate['tetra_lower_pairwise_plus_face_test_r2'])}`")
    lines.append(f"- tetra feature held-out R2 on tetra planting: `{fmt(gate['tetra_feature_test_r2'])}`")
    lines.append(f"- held-out C4 min tetra/face ratio: `{fmt(gate['heldout_c4']['min_tetra_to_face_c4_ratio'])}`")
    lines.append(f"- planar tetra force norm: `{fmt(gate['planar_control']['tetra_force_norm'])}`")
    lines.append(f"- cluster force suppression ratio: `{fmt(gate['cluster_control']['force_suppression_ratio'])}`")
    lines.append("")
    lines.append("## Configuration")
    lines.append("")
    lines.append(f"- trials: `{result['args']['trials']}`")
    lines.append(f"- steps: `{result['args']['steps']}`")
    lines.append(f"- dt: `{result['args']['dt']}`")
    lines.append(f"- sample stride: `{result['args']['sample_stride']}`")
    lines.append(f"- masses: `{result['args']['masses']}`")
    lines.append(f"- softening: `{result['args']['softening']}`")
    lines.append(f"- gamma: `{result['args']['gamma']}`")
    lines.append(f"- face alpha: `{result['args']['face_alpha']}`")
    lines.append(f"- tetra beta: `{result['args']['beta']}`")
    lines.append("")
    lines.append("## Force Recovery")
    lines.append("")
    for title, recovery in [
        ("Pairwise Null", null),
        ("Face-Triplet Planted", face),
        ("Tetrahedral Planted", tetra),
    ]:
        lines.append(f"### {title}")
        lines.append("")
        lines.append("| model | rank | train RMSE | test RMSE | train R2 | test R2 | coefficient |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for row in compact_model_table(recovery["models"]):
            lines.append(
                "| {model} | {rank} | {train_rmse} | {test_rmse} | {train_r2} | {test_r2} | {coefficient} |".format(
                    model=row["model"],
                    rank=row["rank"],
                    train_rmse=fmt(row["train_rmse"]),
                    test_rmse=fmt(row["test_rmse"]),
                    train_r2=fmt(row["train_r2"]),
                    test_r2=fmt(row["test_r2"]),
                    coefficient=fmt(row.get("coefficient", float("nan"))),
                )
            )
        lines.append("")
    lines.append("## Divergence Replay: Tetrahedral Planted Trajectory")
    lines.append("")
    lines.append("| replay model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |")
    lines.append("|---|---:|---:|---:|---:|")
    for name, pos_err in div["position_error_vs_truth"].items():
        mom_err = div["momentum_error_vs_truth"][name]
        lines.append(
            f"| {name} | {fmt(pos_err['final_rms'])} | {fmt(pos_err['max_rms'])} | "
            f"{fmt(mom_err['final_rms'])} | {fmt(mom_err['max_rms'])} |"
        )
    lines.append("")
    lines.append("## C4 Minimal-Nonface Detector")
    lines.append("")
    lines.append("The detector uses the three opposite-edge mixed derivatives and the four")
    lines.append("vertex-star mixed derivatives of the scalar potential in squared-edge")
    lines.append("coordinates.")
    lines.append("")
    lines.append(f"- first replay tetra C4 max abs: `{fmt(c4['tetra_c4_max_abs'])}`")
    lines.append(f"- first replay face C4 max abs: `{fmt(c4['face_c4_max_abs'])}`")
    lines.append(f"- tetra opposite-edge derivatives: `{[fmt(x) for x in c4['tetra_opposite_edge_derivatives']]}`")
    lines.append(f"- tetra vertex-star derivatives: `{[fmt(x) for x in c4['tetra_vertex_star_derivatives']]}`")
    lines.append("")
    lines.append("### Held-Out Asymmetric C4 Samples")
    lines.append("")
    lines.append(f"- held-out trial ids: `{c4_heldout['trial_ids']}`")
    lines.append(f"- sample count: `{c4_heldout['summary']['sample_count']}`")
    lines.append(f"- min tetra volume: `{fmt(c4_heldout['summary']['min_abs_tetra_volume'])}`")
    lines.append(f"- min edge-length CV: `{fmt(c4_heldout['summary']['min_edge_length_cv'])}`")
    lines.append(f"- min tetra C4 max abs: `{fmt(c4_heldout['summary']['min_tetra_c4_max_abs'])}`")
    lines.append(f"- max face C4 max abs: `{fmt(c4_heldout['summary']['max_face_c4_max_abs'])}`")
    lines.append(f"- min tetra/face C4 ratio: `{fmt(c4_heldout['summary']['min_tetra_to_face_c4_ratio'])}`")
    lines.append(f"- max opposite-edge C4 abs: `{fmt(c4_heldout['summary']['max_tetra_opposite_edge_abs'])}`")
    lines.append(f"- max vertex-star C4 abs: `{fmt(c4_heldout['summary']['max_tetra_vertex_star_abs'])}`")
    lines.append("")
    lines.append("| trial | t | volume | edge CV | tetra C4 | face C4 | ratio |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for sample in c4_heldout["samples"][: args_safe_int(result["args"].get("report_c4_sample_rows", 12))]:
        lines.append(
            f"| {sample['trial']} | {sample['time_index']} | "
            f"{fmt(sample['shape']['abs_tetra_volume'])} | {fmt(sample['shape']['edge_length_cv'])} | "
            f"{fmt(sample['detector']['tetra_c4_max_abs'])} | "
            f"{fmt(sample['detector']['face_c4_max_abs'])} | {fmt(sample['tetra_to_face_c4_ratio'])} |"
        )
    lines.append("")
    lines.append("## Degeneration Controls")
    lines.append("")
    lines.append("| control | value |")
    lines.append("|---|---:|")
    lines.append(f"| planar volume | {fmt(planar['shape']['abs_tetra_volume'])} |")
    lines.append(f"| planar tetra force norm | {fmt(planar['tetra_force_norm'])} |")
    lines.append(f"| planar tetra potential abs | {fmt(planar['tetra_potential_abs'])} |")
    lines.append(f"| cluster radius | {fmt(cluster['cluster_radius'])} |")
    lines.append(f"| cluster force suppression ratio | {fmt(cluster['force_suppression_ratio'])} |")
    lines.append(f"| cluster potential suppression ratio | {fmt(cluster['potential_suppression_ratio'])} |")
    lines.append("")
    lines.append("## Invariants")
    lines.append("")
    lines.append("| trajectory | max |P| | max angular drift | max relative energy drift |")
    lines.append("|---|---:|---:|---:|")
    for name, inv in div["invariants"].items():
        lines.append(
            f"| {name} | {fmt(inv['max_total_momentum_norm'])} | "
            f"{fmt(inv['max_angular_momentum_drift'])} | "
            f"{fmt(inv.get('max_relative_energy_drift', float('nan')))} |"
        )
    lines.append("")
    lines.append("## Reading")
    lines.append("")
    lines.append("The audit asks for type separation. Under the null, residual coefficients should vanish.")
    lines.append("Under face-triplet planting, lower-arity face features should explain the residual.")
    lines.append("Under tetrahedral planting, a one-coefficient tetrahedral feature should recover beta,")
    lines.append("while lower-arity shadows should be reported as controls rather than arity certificates.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=16)
    parser.add_argument("--steps", type=int, default=1400)
    parser.add_argument("--dt", type=float, default=0.0015)
    parser.add_argument("--sample-stride", type=int, default=20)
    parser.add_argument("--train-fraction", type=float, default=0.65)
    parser.add_argument("--seed", type=int, default=2804)
    parser.add_argument("--masses", type=float, nargs=4, default=[1.0, 1.18, 0.9, 1.07])
    parser.add_argument("--gravity", type=float, default=0.38)
    parser.add_argument("--softening", type=float, default=0.18)
    parser.add_argument("--face-alpha", type=float, default=0.025)
    parser.add_argument("--beta", type=float, default=0.08)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--powers", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6])
    parser.add_argument("--c4-h", type=float, default=1e-3)
    parser.add_argument("--c4-holdout-samples-per-trial", type=int, default=3)
    parser.add_argument("--report-c4-sample-rows", type=int, default=12)
    parser.add_argument("--null-tetra-coeff-tol", type=float, default=1e-12)
    parser.add_argument("--face-r2-floor", type=float, default=0.999)
    parser.add_argument("--face-tetra-leakage-max", type=float, default=0.20)
    parser.add_argument("--lower-tetra-r2-max", type=float, default=0.80)
    parser.add_argument("--tetra-r2-floor", type=float, default=0.999)
    parser.add_argument("--beta-tol", type=float, default=1e-10)
    parser.add_argument("--replay-tetra-final-tol", type=float, default=1e-12)
    parser.add_argument("--replay-lower-min-final", type=float, default=1e-6)
    parser.add_argument("--heldout-volume-floor", type=float, default=1e-3)
    parser.add_argument("--heldout-edge-cv-floor", type=float, default=0.05)
    parser.add_argument("--c4-tetra-floor", type=float, default=1e-5)
    parser.add_argument("--c4-face-tol", type=float, default=1e-6)
    parser.add_argument("--c4-ratio-floor", type=float, default=20.0)
    parser.add_argument("--planar-force-tol", type=float, default=1e-12)
    parser.add_argument("--planar-potential-tol", type=float, default=1e-12)
    parser.add_argument("--cluster-radius", type=float, default=10000.0)
    parser.add_argument("--cluster-force-ratio-tol", type=float, default=1e-3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    powers = tuple(args.powers)
    null_dataset = make_dataset(0.0, 0.0, args, powers)
    face_dataset = make_dataset(args.face_alpha, 0.0, args, powers)
    tetra_dataset = make_dataset(0.0, args.beta, args, powers)
    null_recovery = evaluate_force_recovery(null_dataset, args)
    face_recovery = evaluate_force_recovery(face_dataset, args)
    tetra_recovery = evaluate_force_recovery(tetra_dataset, args)
    divergence = divergence_audit(tetra_recovery, args, powers)
    c4_heldout = c4_heldout_audit(tetra_dataset, args)
    planar = planar_degeneration_control(args)
    cluster = cluster_separation_control(args)
    result = {
        "args": vars(args) | {"json_out": str(args.json_out), "report_out": str(args.report_out)},
        "null": null_recovery,
        "face_planted": face_recovery,
        "tetra_planted": tetra_recovery,
        "divergence_audit": divergence,
        "c4_heldout": c4_heldout,
        "planar_degenerated_control": planar,
        "cluster_separation_control": cluster,
        "arity_gate_summary": arity_gate_summary(
            null_recovery,
            face_recovery,
            tetra_recovery,
            divergence,
            c4_heldout,
            planar,
            cluster,
            args,
        ),
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    recovered_beta = result["tetra_planted"]["models"]["tetra_one_coefficient"]["coefficients"][0]
    lower_r2 = result["tetra_planted"]["models"]["lower_pairwise_plus_face"]["test_r2_vs_zero"]
    tetra_r2 = result["tetra_planted"]["models"]["tetra_one_coefficient"]["test_r2_vs_zero"]
    print(
        "four_body_tetrahedral_residual_audit: "
        f"status={result['arity_gate_summary']['status']}, "
        f"beta={fmt(args.beta)}, recovered_beta={fmt(recovered_beta)}, "
        f"lower_test_r2={fmt(lower_r2)}, tetra_test_r2={fmt(tetra_r2)}"
    )


if __name__ == "__main__":
    main()
