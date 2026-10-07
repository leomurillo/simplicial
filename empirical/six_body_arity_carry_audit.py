"""Six-body arity/carry audit for Paper 28.

This is a controlled scaffold, not an astrophysical claim.  Six bodies are the
first room where the prime covers 2 and 3 both tile the whole cleanly.  The
audit tests whether planted six-body cover channels can be separated from
lower-arity pair, triplet, and tetrahedral shadows.

Planted channels:
  matching_222: sum over perfect matchings, a 2+2+2 dyadic cover.
  bitriangle_33: sum over partitions into two triples, a 3+3 ternary cover.
  carry_23: sum over 2x3 grids, coupling two triplet rows with three pair
             columns.

Outputs:
  empirical/reports/six_body_arity_carry_audit.json
  empirical/reports/six_body_arity_carry_audit.md
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np


N = 6
DIM = 3
BODY_IDS = tuple(range(N))
EDGES = tuple(itertools.combinations(BODY_IDS, 2))
TRIPLES = tuple(itertools.combinations(BODY_IDS, 3))
QUADS = tuple(itertools.combinations(BODY_IDS, 4))
DEFAULT_JSON = Path("empirical/reports/six_body_arity_carry_audit.json")
DEFAULT_REPORT = Path("empirical/reports/six_body_arity_carry_audit.md")


@dataclass(frozen=True)
class ForceConfig:
    masses: np.ndarray
    gravity: float
    softening: float
    mu_222: float
    nu_33: float
    kappa_23: float


def fmt(value: float, digits: int = 6) -> str:
    if not np.isfinite(value):
        return str(value)
    if value == 0:
        return "0"
    abs_value = abs(value)
    if abs_value < 1e-4 or abs_value >= 1e5:
        return f"{value:.{digits}e}"
    return f"{value:.{digits}g}"


def complete_edges(subset: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(sorted(edge)) for edge in itertools.combinations(subset, 2))


def perfect_matchings(items: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    if not items:
        return [()]
    first = items[0]
    out: list[tuple[tuple[int, int], ...]] = []
    for idx in range(1, len(items)):
        second = items[idx]
        rest = items[1:idx] + items[idx + 1 :]
        for matching in perfect_matchings(rest):
            out.append((tuple(sorted((first, second))),) + matching)
    return out


def triple_partitions() -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    out = []
    for left in itertools.combinations(BODY_IDS, 3):
        if 0 not in left:
            continue
        right = tuple(i for i in BODY_IDS if i not in left)
        out.append((tuple(left), right))
    return out


MATCHING_TERMS = perfect_matchings(BODY_IDS)
TRIPLE_PARTITIONS = triple_partitions()
BITRIANGLE_TERMS = tuple(complete_edges(left) + complete_edges(right) for left, right in TRIPLE_PARTITIONS)


def grid23_terms() -> tuple[tuple[tuple[int, int], ...], ...]:
    terms: list[tuple[tuple[int, int], ...]] = []
    for left, right in TRIPLE_PARTITIONS:
        left_sorted = tuple(sorted(left))
        for permuted_right in itertools.permutations(right):
            cross = tuple(tuple(sorted(edge)) for edge in zip(left_sorted, permuted_right))
            terms.append(complete_edges(left) + complete_edges(right) + cross)
    return tuple(terms)


GRID23_TERMS = grid23_terms()


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


def edge_product_force(
    pos: np.ndarray,
    terms: tuple[tuple[tuple[int, int], ...], ...] | list[tuple[tuple[int, int], ...]],
    mass_factor: float,
    softening: float,
) -> np.ndarray:
    force = np.zeros_like(pos, dtype=np.float64)
    for term_edges in terms:
        inv_product = 1.0
        edge_data: list[tuple[int, int, float]] = []
        for i, j in term_edges:
            delta = pos[i] - pos[j]
            s2 = float(np.dot(delta, delta) + softening * softening)
            inv_product *= 1.0 / float(np.sqrt(s2))
            edge_data.append((i, j, s2))
        scale = mass_factor * inv_product
        for i, j, s2 in edge_data:
            fij = scale * (pos[j] - pos[i]) / s2
            force[i] += fij
            force[j] -= fij
    return force


def edge_product_potential(
    pos: np.ndarray,
    terms: tuple[tuple[tuple[int, int], ...], ...] | list[tuple[tuple[int, int], ...]],
    mass_factor: float,
    softening: float,
) -> float:
    total = 0.0
    for term_edges in terms:
        inv_product = 1.0
        for i, j in term_edges:
            delta = pos[i] - pos[j]
            s2 = float(np.dot(delta, delta) + softening * softening)
            inv_product *= 1.0 / float(np.sqrt(s2))
        total += inv_product
    return -mass_factor * total


def triplet_force_base(pos: np.ndarray, masses: np.ndarray, softening: float, triple: tuple[int, int, int]) -> np.ndarray:
    return edge_product_force(pos, [complete_edges(triple)], float(np.prod(masses[list(triple)])), softening)


def tetra_delta_and_grad(pos4: np.ndarray) -> tuple[float, np.ndarray]:
    a = pos4[1] - pos4[0]
    b = pos4[2] - pos4[0]
    c = pos4[3] - pos4[0]
    delta = float(np.dot(a, np.cross(b, c)) / 6.0)
    grad = np.zeros_like(pos4, dtype=np.float64)
    grad[1] = np.cross(b, c) / 6.0
    grad[2] = np.cross(c, a) / 6.0
    grad[3] = np.cross(a, b) / 6.0
    grad[0] = -(grad[1] + grad[2] + grad[3])
    return delta, grad


def tetra_force_base(pos: np.ndarray, masses: np.ndarray, softening: float, quad: tuple[int, int, int, int]) -> np.ndarray:
    local_pos = pos[list(quad)]
    delta, local_grad = tetra_delta_and_grad(local_pos)
    product_s = 1.0
    local_grad_log = np.zeros((4, DIM), dtype=np.float64)
    for a in range(4):
        for b in range(a + 1, 4):
            i, j = quad[a], quad[b]
            rij = pos[i] - pos[j]
            s2 = float(np.dot(rij, rij) + softening * softening)
            product_s *= float(np.sqrt(s2))
            term = rij / s2
            local_grad_log[a] += term
            local_grad_log[b] -= term
    scale = float(np.prod(masses[list(quad)]) / product_s)
    local_force = scale * (2.0 * delta * local_grad - delta * delta * local_grad_log)
    force = np.zeros_like(pos, dtype=np.float64)
    for local_idx, body_idx in enumerate(quad):
        force[body_idx] = local_force[local_idx]
    return force


def matching222_force(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return edge_product_force(pos, MATCHING_TERMS, float(np.prod(masses)), softening)


def bitriangle33_force(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return edge_product_force(pos, BITRIANGLE_TERMS, float(np.prod(masses)), softening)


def carry23_force(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return edge_product_force(pos, GRID23_TERMS, float(np.prod(masses)), softening)


def matching222_potential(pos: np.ndarray, masses: np.ndarray, softening: float) -> float:
    return edge_product_potential(pos, MATCHING_TERMS, float(np.prod(masses)), softening)


def bitriangle33_potential(pos: np.ndarray, masses: np.ndarray, softening: float) -> float:
    return edge_product_potential(pos, BITRIANGLE_TERMS, float(np.prod(masses)), softening)


def carry23_potential(pos: np.ndarray, masses: np.ndarray, softening: float) -> float:
    return edge_product_potential(pos, GRID23_TERMS, float(np.prod(masses)), softening)


def total_force(pos: np.ndarray, config: ForceConfig) -> np.ndarray:
    return (
        pair_force(pos, config.masses, config.gravity, config.softening)
        + config.mu_222 * matching222_force(pos, config.masses, config.softening)
        + config.nu_33 * bitriangle33_force(pos, config.masses, config.softening)
        + config.kappa_23 * carry23_force(pos, config.masses, config.softening)
    )


def kinetic_energy(momentum: np.ndarray, masses: np.ndarray) -> float:
    return float(0.5 * np.sum(np.sum(momentum * momentum, axis=1) / masses))


def hamiltonian(pos: np.ndarray, momentum: np.ndarray, config: ForceConfig) -> float:
    return (
        kinetic_energy(momentum, config.masses)
        + pair_potential(pos, config.masses, config.gravity, config.softening)
        + config.mu_222 * matching222_potential(pos, config.masses, config.softening)
        + config.nu_33 * bitriangle33_potential(pos, config.masses, config.softening)
        + config.kappa_23 * carry23_potential(pos, config.masses, config.softening)
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
            [-1.05, -0.12, 0.02],
            [0.97, 0.18, -0.08],
            [-0.18, -1.02, 0.16],
            [0.16, 0.96, -0.11],
            [0.08, -0.14, -1.04],
            [-0.10, 0.08, 1.02],
        ],
        dtype=np.float64,
    )
    momentum = np.array(
        [
            [0.06, 0.18, -0.04],
            [-0.12, -0.08, 0.06],
            [0.09, -0.11, 0.03],
            [-0.04, 0.10, -0.05],
            [0.03, -0.02, 0.12],
            [-0.02, -0.07, -0.12],
        ],
        dtype=np.float64,
    )
    pos += rng.normal(scale=0.035, size=pos.shape)
    momentum += rng.normal(scale=0.018, size=momentum.shape)
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
    positions = np.empty((steps + 1, N, DIM), dtype=np.float64)
    momenta = np.empty((steps + 1, N, DIM), dtype=np.float64)
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


def triplet_features(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return np.stack([triplet_force_base(pos, masses, softening, triple).reshape(-1) for triple in TRIPLES], axis=1)


def tetra_features(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return np.stack([tetra_force_base(pos, masses, softening, quad).reshape(-1) for quad in QUADS], axis=1)


def cover_features(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    return np.stack(
        [
            matching222_force(pos, masses, softening).reshape(-1),
            bitriangle33_force(pos, masses, softening).reshape(-1),
            carry23_force(pos, masses, softening).reshape(-1),
        ],
        axis=1,
    )


def make_feature_matrix(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
    key: str,
) -> np.ndarray:
    if key == "pairwise_features":
        return pairwise_radial_features(pos, masses, softening, powers)
    if key == "triplet_features":
        return triplet_features(pos, masses, softening)
    if key == "tetra_features":
        return tetra_features(pos, masses, softening)
    if key == "lower_le4_features":
        return np.hstack(
            [
                pairwise_radial_features(pos, masses, softening, powers),
                triplet_features(pos, masses, softening),
                tetra_features(pos, masses, softening),
            ]
        )
    if key == "cover_features":
        return cover_features(pos, masses, softening)
    if key == "matching222_feature":
        return matching222_force(pos, masses, softening).reshape(-1, 1)
    if key == "bitriangle33_feature":
        return bitriangle33_force(pos, masses, softening).reshape(-1, 1)
    if key == "carry23_feature":
        return carry23_force(pos, masses, softening).reshape(-1, 1)
    if key == "lower_plus_cover_features":
        return np.hstack(
            [
                pairwise_radial_features(pos, masses, softening, powers),
                triplet_features(pos, masses, softening),
                tetra_features(pos, masses, softening),
                cover_features(pos, masses, softening),
            ]
        )
    raise ValueError(key)


def make_dataset(config: ForceConfig, args: argparse.Namespace, powers: tuple[int, ...]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    trajectories: list[dict[str, Any]] = []
    for trial in range(args.trials):
        pos0, momentum0 = initial_condition(args.seed + trial, config.masses)
        positions, momenta = velocity_verlet(
            pos0,
            momentum0,
            config.masses,
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
            pair = pair_force(pos, config.masses, config.gravity, config.softening)
            pair_features = pairwise_radial_features(pos, config.masses, config.softening, powers)
            triple_features = triplet_features(pos, config.masses, config.softening)
            quad_features = tetra_features(pos, config.masses, config.softening)
            covers = cover_features(pos, config.masses, config.softening)
            row = {
                "trial": trial,
                "time_index": t,
                "target_residual": (exact_force - pair).reshape(-1),
                "finite_difference_residual": (finite_difference_force - pair).reshape(-1),
                "pairwise_features": pair_features,
                "triplet_features": triple_features,
                "tetra_features": quad_features,
                "lower_le4_features": np.hstack([pair_features, triple_features, quad_features]),
                "matching222_feature": covers[:, 0:1],
                "bitriangle33_feature": covers[:, 1:2],
                "carry23_feature": covers[:, 2:3],
                "cover_features": covers,
                "lower_plus_cover_features": np.hstack([pair_features, triple_features, quad_features, covers]),
            }
            rows.append(row)
    return {"rows": rows, "trajectories": trajectories, "config": config}


def split_rows(rows: list[dict[str, Any]], train_fraction: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    trials = sorted({row["trial"] for row in rows})
    train_count = max(1, int(round(train_fraction * len(trials))))
    train_trials = set(trials[:train_count])
    return [row for row in rows if row["trial"] in train_trials], [row for row in rows if row["trial"] not in train_trials]


def stack_target(rows: list[dict[str, Any]], key: str = "target_residual") -> np.ndarray:
    return np.concatenate([row[key] for row in rows], axis=0)


def stack_feature(rows: list[dict[str, Any]], key: str) -> np.ndarray:
    return np.concatenate([row[key] for row in rows], axis=0)


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


def random_same_rank_score(y_train: np.ndarray, y_test: np.ndarray, seed: int) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    return fit_and_score(
        rng.normal(size=(y_train.shape[0], 1)),
        y_train,
        rng.normal(size=(y_test.shape[0], 1)),
        y_test,
    )


def shuffled_feature_score(
    rows_train: list[dict[str, Any]],
    rows_test: list[dict[str, Any]],
    key: str,
    y_train: np.ndarray,
    y_test: np.ndarray,
    seed: int,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    train_features = [row[key].copy() for row in rows_train]
    test_features = [row[key].copy() for row in rows_test]
    rng.shuffle(train_features)
    rng.shuffle(test_features)
    return fit_and_score(np.concatenate(train_features, axis=0), y_train, np.concatenate(test_features, axis=0), y_test)


def evaluate_force_recovery(dataset: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    train_rows, test_rows = split_rows(dataset["rows"], args.train_fraction)
    y_train = stack_target(train_rows)
    y_test = stack_target(test_rows)
    finite_difference_train = stack_target(train_rows, key="finite_difference_residual")
    finite_difference_test = stack_target(test_rows, key="finite_difference_residual")
    models = {
        "pairwise_null": score_zero(y_train, y_test),
        "pairwise_radial_basis": fit_and_score(
            stack_feature(train_rows, "pairwise_features"), y_train, stack_feature(test_rows, "pairwise_features"), y_test
        ),
        "triplet_basis": fit_and_score(
            stack_feature(train_rows, "triplet_features"), y_train, stack_feature(test_rows, "triplet_features"), y_test
        ),
        "tetra_basis": fit_and_score(
            stack_feature(train_rows, "tetra_features"), y_train, stack_feature(test_rows, "tetra_features"), y_test
        ),
        "lower_le4_basis": fit_and_score(
            stack_feature(train_rows, "lower_le4_features"), y_train, stack_feature(test_rows, "lower_le4_features"), y_test
        ),
        "matching222_one_coeff": fit_and_score(
            stack_feature(train_rows, "matching222_feature"),
            y_train,
            stack_feature(test_rows, "matching222_feature"),
            y_test,
        ),
        "bitriangle33_one_coeff": fit_and_score(
            stack_feature(train_rows, "bitriangle33_feature"),
            y_train,
            stack_feature(test_rows, "bitriangle33_feature"),
            y_test,
        ),
        "carry23_one_coeff": fit_and_score(
            stack_feature(train_rows, "carry23_feature"), y_train, stack_feature(test_rows, "carry23_feature"), y_test
        ),
        "cover_222_33_23_basis": fit_and_score(
            stack_feature(train_rows, "cover_features"), y_train, stack_feature(test_rows, "cover_features"), y_test
        ),
        "lower_plus_cover_basis": fit_and_score(
            stack_feature(train_rows, "lower_plus_cover_features"),
            y_train,
            stack_feature(test_rows, "lower_plus_cover_features"),
            y_test,
        ),
        "shuffled_carry23_feature": shuffled_feature_score(
            train_rows, test_rows, "carry23_feature", y_train, y_test, args.seed + 1000
        ),
        "random_same_rank_feature": random_same_rank_score(y_train, y_test, args.seed + 2000),
    }
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
        "models": models,
    }


def feature_force_from_coeffs(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
    key: str,
) -> np.ndarray:
    return (make_feature_matrix(pos, masses, softening, powers, key) @ coeffs).reshape(N, DIM)


def trajectory_errors(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    diff = candidate - reference
    rms_by_t = np.sqrt(np.mean(diff * diff, axis=(1, 2)))
    return {
        "final_rms": float(rms_by_t[-1]),
        "max_rms": float(np.max(rms_by_t)),
        "mean_rms": float(np.mean(rms_by_t)),
    }


def invariant_summary(positions: np.ndarray, momenta: np.ndarray, config: ForceConfig | None) -> dict[str, float]:
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
    truth_config = ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.kappa_23)
    pair_config = ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, 0.0)
    recovered_kappa = float(recovery["models"]["carry23_one_coeff"]["coefficients"][0])
    recovered_config = ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, recovered_kappa)
    lower_coeffs = np.array(recovery["models"]["lower_le4_basis"]["coefficients"])
    cover_coeffs = np.array(recovery["models"]["cover_222_33_23_basis"]["coefficients"])

    truth_pos, truth_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, truth_config)
    )
    pair_pos, pair_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, pair_config)
    )
    lower_pos, lower_mom = velocity_verlet(
        pos0,
        momentum0,
        masses,
        args.dt,
        args.steps,
        lambda x: pair_force(x, masses, args.gravity, args.softening)
        + feature_force_from_coeffs(x, masses, args.softening, powers, lower_coeffs, "lower_le4_features"),
    )
    cover_pos, cover_mom = velocity_verlet(
        pos0,
        momentum0,
        masses,
        args.dt,
        args.steps,
        lambda x: pair_force(x, masses, args.gravity, args.softening)
        + feature_force_from_coeffs(x, masses, args.softening, powers, cover_coeffs, "cover_features"),
    )
    recovered_pos, recovered_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, recovered_config)
    )

    return {
        "trial": 0,
        "true_kappa_23": args.kappa_23,
        "recovered_kappa_23": recovered_kappa,
        "position_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_pos, pair_pos),
            "lower_le4_basis": trajectory_errors(truth_pos, lower_pos),
            "cover_222_33_23_basis": trajectory_errors(truth_pos, cover_pos),
            "recovered_carry23": trajectory_errors(truth_pos, recovered_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_mom, pair_mom),
            "lower_le4_basis": trajectory_errors(truth_mom, lower_mom),
            "cover_222_33_23_basis": trajectory_errors(truth_mom, cover_mom),
            "recovered_carry23": trajectory_errors(truth_mom, recovered_mom),
        },
        "invariants": {
            "truth": invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_carry23": invariant_summary(recovered_pos, recovered_mom, recovered_config),
            "lower_le4_basis": invariant_summary(lower_pos, lower_mom, None),
            "cover_222_33_23_basis": invariant_summary(cover_pos, cover_mom, None),
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
    lines: list[str] = []
    lines.append("# Six-Body Arity/Carry Audit")
    lines.append("")
    lines.append("This is a controlled Paper 28 scaffold, not a claim about real gravitation.")
    lines.append("Six bodies are the first room where 2 and 3 both tile the whole:")
    lines.append("perfect matchings (`2+2+2`), bi-triangles (`3+3`), and `2x3` carry.")
    lines.append("")
    lines.append("## Configuration")
    lines.append("")
    for key in ("trials", "steps", "dt", "sample_stride", "masses", "gravity", "softening", "mu_222", "nu_33", "kappa_23"):
        lines.append(f"- {key}: `{result['args'][key]}`")
    lines.append("")
    lines.append("## Force Recovery")
    lines.append("")
    for title, recovery in [
        ("Pairwise Null", result["null"]),
        ("Matching 2+2+2 Planted", result["matching222_planted"]),
        ("Bi-Triangle 3+3 Planted", result["bitriangle33_planted"]),
        ("2x3 Carry Planted", result["carry23_planted"]),
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
    div = result["divergence_audit"]
    lines.append("## Divergence Replay: 2x3 Carry Planted Trajectory")
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
    lines.append("The audit asks whether lower arities explain planted 6-body prime-cover channels.")
    lines.append("Under the pairwise null, all residual models should remain at zero.")
    lines.append("Under 2x3 carry planting, the carry feature should beat lower <=4 shadows and")
    lines.append("recover the planted coefficient on held-out trajectories.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--steps", type=int, default=850)
    parser.add_argument("--dt", type=float, default=0.0015)
    parser.add_argument("--sample-stride", type=int, default=25)
    parser.add_argument("--train-fraction", type=float, default=0.6)
    parser.add_argument("--seed", type=int, default=2806)
    parser.add_argument("--masses", type=float, nargs=N, default=[1.0, 1.12, 0.94, 1.07, 0.89, 1.16])
    parser.add_argument("--gravity", type=float, default=0.18)
    parser.add_argument("--softening", type=float, default=0.3)
    parser.add_argument("--mu-222", type=float, default=0.015)
    parser.add_argument("--nu-33", type=float, default=0.02)
    parser.add_argument("--kappa-23", type=float, default=0.006)
    parser.add_argument("--powers", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6])
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    powers = tuple(args.powers)
    masses = np.array(args.masses, dtype=np.float64)
    configs = {
        "null": ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, 0.0),
        "matching222_planted": ForceConfig(masses, args.gravity, args.softening, args.mu_222, 0.0, 0.0),
        "bitriangle33_planted": ForceConfig(masses, args.gravity, args.softening, 0.0, args.nu_33, 0.0),
        "carry23_planted": ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.kappa_23),
    }
    result: dict[str, Any] = {
        "args": vars(args) | {"json_out": str(args.json_out), "report_out": str(args.report_out)},
        "term_counts": {
            "edges": len(EDGES),
            "triples": len(TRIPLES),
            "quads": len(QUADS),
            "perfect_matchings": len(MATCHING_TERMS),
            "triple_partitions": len(TRIPLE_PARTITIONS),
            "grid23_terms": len(GRID23_TERMS),
        },
    }
    datasets: dict[str, Any] = {}
    for name, config in configs.items():
        datasets[name] = make_dataset(config, args, powers)
        result[name] = evaluate_force_recovery(datasets[name], args)
    result["divergence_audit"] = divergence_audit(result["carry23_planted"], args, powers)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    carry_recovered = result["carry23_planted"]["models"]["carry23_one_coeff"]["coefficients"][0]
    lower_r2 = result["carry23_planted"]["models"]["lower_le4_basis"]["test_r2_vs_zero"]
    carry_r2 = result["carry23_planted"]["models"]["carry23_one_coeff"]["test_r2_vs_zero"]
    cover_r2 = result["carry23_planted"]["models"]["cover_222_33_23_basis"]["test_r2_vs_zero"]
    print(
        "six_body_arity_carry_audit: "
        f"kappa={fmt(args.kappa_23)}, recovered_kappa={fmt(carry_recovered)}, "
        f"lower_le4_test_r2={fmt(lower_r2)}, carry_test_r2={fmt(carry_r2)}, "
        f"cover_test_r2={fmt(cover_r2)}"
    )


if __name__ == "__main__":
    main()
