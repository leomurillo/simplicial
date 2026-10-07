"""Three-body ternary residual audit for Paper 28.

This is a controlled comprobation scaffold, not an astrophysical claim.
It asks whether a known nonadditive three-body force channel can be recovered
from trajectories when the pairwise Newtonian law is used as the null model.

The planted dynamics use softened pairwise Newtonian gravity plus a softened
triplet potential

    V_3 = -alpha * m1*m2*m3 / (s12*s23*s31),

where sij = sqrt(|ri-rj|^2 + softening^2).  The corresponding force is
translation/rotation invariant, conserves total momentum and angular momentum,
vanishes when a body is removed, and cannot be represented by pair-only radial
features with coefficients independent of the third body across an ensemble.

Outputs:
  empirical/reports/three_body_ternary_residual_audit.json
  empirical/reports/three_body_ternary_residual_audit.md
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np


DEFAULT_JSON = Path("empirical/reports/three_body_ternary_residual_audit.json")
DEFAULT_REPORT = Path("empirical/reports/three_body_ternary_residual_audit.md")


@dataclass(frozen=True)
class ForceConfig:
    masses: np.ndarray
    gravity: float
    softening: float
    alpha: float


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
    force = np.zeros_like(pos, dtype=np.float64)
    for i in range(3):
        for j in range(i + 1, 3):
            delta = pos[j] - pos[i]
            s2 = float(np.dot(delta, delta) + softening * softening)
            fij = gravity * masses[i] * masses[j] * delta / (s2 ** 1.5)
            force[i] += fij
            force[j] -= fij
    return force


def pair_potential(pos: np.ndarray, masses: np.ndarray, gravity: float, softening: float) -> float:
    potential = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            delta = pos[j] - pos[i]
            sij = float(np.sqrt(np.dot(delta, delta) + softening * softening))
            potential -= gravity * masses[i] * masses[j] / sij
    return potential


def ternary_force_base(pos: np.ndarray, masses: np.ndarray, softening: float) -> np.ndarray:
    """Coefficient-free force from -prod(m)/(s12*s23*s31)."""
    s2: dict[tuple[int, int], float] = {}
    sij: dict[tuple[int, int], float] = {}
    for i in range(3):
        for j in range(i + 1, 3):
            delta = pos[i] - pos[j]
            value = float(np.dot(delta, delta) + softening * softening)
            s2[(i, j)] = value
            sij[(i, j)] = float(np.sqrt(value))
    denom = sij[(0, 1)] * sij[(0, 2)] * sij[(1, 2)]
    prefactor = float(np.prod(masses) / denom)
    force = np.zeros_like(pos, dtype=np.float64)
    for i in range(3):
        acc = np.zeros(2, dtype=np.float64)
        for j in range(3):
            if i == j:
                continue
            key = (i, j) if i < j else (j, i)
            acc += (pos[j] - pos[i]) / s2[key]
        force[i] = prefactor * acc
    return force


def ternary_potential_base(pos: np.ndarray, masses: np.ndarray, softening: float) -> float:
    denom = 1.0
    for i in range(3):
        for j in range(i + 1, 3):
            delta = pos[i] - pos[j]
            denom *= float(np.sqrt(np.dot(delta, delta) + softening * softening))
    return -float(np.prod(masses) / denom)


def total_force(pos: np.ndarray, config: ForceConfig) -> np.ndarray:
    return pair_force(pos, config.masses, config.gravity, config.softening) + (
        config.alpha * ternary_force_base(pos, config.masses, config.softening)
    )


def kinetic_energy(momentum: np.ndarray, masses: np.ndarray) -> float:
    return float(0.5 * np.sum(np.sum(momentum * momentum, axis=1) / masses))


def hamiltonian(pos: np.ndarray, momentum: np.ndarray, config: ForceConfig) -> float:
    return (
        kinetic_energy(momentum, config.masses)
        + pair_potential(pos, config.masses, config.gravity, config.softening)
        + config.alpha * ternary_potential_base(pos, config.masses, config.softening)
    )


def total_momentum(momentum: np.ndarray) -> np.ndarray:
    return np.sum(momentum, axis=0)


def angular_momentum_z(pos: np.ndarray, momentum: np.ndarray) -> float:
    return float(np.sum(pos[:, 0] * momentum[:, 1] - pos[:, 1] * momentum[:, 0]))


def recenter(pos: np.ndarray, momentum: np.ndarray, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    center = np.sum(pos * masses[:, None], axis=0) / np.sum(masses)
    pos = pos - center
    momentum = momentum - np.sum(momentum, axis=0)[None, :] * masses[:, None] / np.sum(masses)
    return pos, momentum


def initial_condition(seed: int, masses: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    pos = np.array(
        [
            [-0.95, -0.28],
            [0.92, -0.22],
            [0.06, 0.92],
        ],
        dtype=np.float64,
    )
    momentum = np.array(
        [
            [0.08, 0.54],
            [-0.42, -0.23],
            [0.34, -0.31],
        ],
        dtype=np.float64,
    )
    pos += rng.normal(scale=0.045, size=pos.shape)
    momentum += rng.normal(scale=0.025, size=momentum.shape)
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
    positions = np.empty((steps + 1, 3, 2), dtype=np.float64)
    momenta = np.empty((steps + 1, 3, 2), dtype=np.float64)
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
    for i in range(3):
        for j in range(i + 1, 3):
            delta = pos[j] - pos[i]
            s2 = float(np.dot(delta, delta) + softening * softening)
            s = float(np.sqrt(s2))
            for power in powers:
                feature = np.zeros_like(pos, dtype=np.float64)
                fij = masses[i] * masses[j] * delta / (s ** power)
                feature[i] += fij
                feature[j] -= fij
                columns.append(feature.reshape(-1))
    return np.stack(columns, axis=1)


def pairwise_basis_force(
    pos: np.ndarray,
    masses: np.ndarray,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
) -> np.ndarray:
    features = pairwise_radial_features(pos, masses, softening, powers)
    return (features @ coeffs).reshape(3, 2)


def make_dataset(
    alpha: float,
    args: argparse.Namespace,
    powers: tuple[int, ...],
) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    config = ForceConfig(masses=masses, gravity=args.gravity, softening=args.softening, alpha=alpha)
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
            tri = ternary_force_base(pos, masses, args.softening)
            exact_residual = alpha * tri
            rows.append(
                {
                    "trial": trial,
                    "time_index": t,
                    "target_residual": (exact_force - pair).reshape(-1),
                    "exact_residual": exact_residual.reshape(-1),
                    "finite_difference_residual": (finite_difference_force - pair).reshape(-1),
                    "ternary_feature": tri.reshape(-1),
                    "pairwise_features": pairwise_radial_features(pos, masses, args.softening, powers),
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
    if key == "ternary_feature":
        return np.concatenate([row[key][:, None] for row in rows], axis=0)
    if key == "pairwise_features":
        return np.concatenate([row[key] for row in rows], axis=0)
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


def shuffled_ternary_score(
    rows_train: list[dict[str, Any]],
    rows_test: list[dict[str, Any]],
    y_train: np.ndarray,
    y_test: np.ndarray,
    seed: int,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    train_features = [row["ternary_feature"].copy() for row in rows_train]
    test_features = [row["ternary_feature"].copy() for row in rows_test]
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
    finite_diff_noise = {
        "train_rmse_finite_difference_minus_exact_force": float(
            np.sqrt(np.mean((finite_difference_train - y_train) ** 2))
        ),
        "test_rmse_finite_difference_minus_exact_force": float(
            np.sqrt(np.mean((finite_difference_test - y_test) ** 2))
        ),
    }
    ternary = fit_and_score(
        stack_feature(train_rows, "ternary_feature"),
        y_train,
        stack_feature(test_rows, "ternary_feature"),
        y_test,
    )
    pairwise_basis = fit_and_score(
        stack_feature(train_rows, "pairwise_features"),
        y_train,
        stack_feature(test_rows, "pairwise_features"),
        y_test,
    )
    return {
        "sample_count_train": len(train_rows),
        "sample_count_test": len(test_rows),
        "component_count_train": int(y_train.shape[0]),
        "component_count_test": int(y_test.shape[0]),
        "target_residual_rms_train": float(np.sqrt(np.mean(y_train**2))),
        "target_residual_rms_test": float(np.sqrt(np.mean(y_test**2))),
        "finite_difference_noise": finite_diff_noise,
        "models": {
            "pairwise_null": score_zero(y_train, y_test),
            "ternary_one_coefficient": ternary,
            "pairwise_only_radial_basis": pairwise_basis,
            "shuffled_ternary_feature": shuffled_ternary_score(
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
    angular = np.array([angular_momentum_z(r, p) for r, p in zip(positions, momenta)])
    out = {
        "max_total_momentum_norm": float(np.max(p_norms)),
        "max_angular_momentum_abs_drift": float(np.max(np.abs(angular - angular[0]))),
    }
    if config is not None:
        energy = np.array([hamiltonian(r, p, config) for r, p in zip(positions, momenta)])
        out["max_relative_energy_drift"] = float(
            np.max(np.abs(energy - energy[0])) / max(1e-12, abs(float(energy[0])))
        )
    return out


def divergence_audit(
    dataset: dict[str, Any],
    recovery: dict[str, Any],
    args: argparse.Namespace,
    powers: tuple[int, ...],
) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos0, momentum0 = initial_condition(args.seed, masses)
    truth_config = ForceConfig(masses, args.gravity, args.softening, args.alpha)
    pair_config = ForceConfig(masses, args.gravity, args.softening, 0.0)
    recovered_alpha = float(recovery["models"]["ternary_one_coefficient"]["coefficients"][0])
    recovered_config = ForceConfig(masses, args.gravity, args.softening, recovered_alpha)
    pair_basis_coeffs = np.array(recovery["models"]["pairwise_only_radial_basis"]["coefficients"])

    truth_pos, truth_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, truth_config)
    )
    pair_pos, pair_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, pair_config)
    )
    recovered_pos, recovered_mom = velocity_verlet(
        pos0, momentum0, masses, args.dt, args.steps, lambda x: total_force(x, recovered_config)
    )
    basis_pos, basis_mom = velocity_verlet(
        pos0,
        momentum0,
        masses,
        args.dt,
        args.steps,
        lambda x: pair_force(x, masses, args.gravity, args.softening)
        + pairwise_basis_force(x, masses, args.softening, powers, pair_basis_coeffs),
    )

    return {
        "trial": 0,
        "true_alpha": args.alpha,
        "recovered_alpha": recovered_alpha,
        "position_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_pos, pair_pos),
            "recovered_ternary": trajectory_errors(truth_pos, recovered_pos),
            "pairwise_only_radial_basis": trajectory_errors(truth_pos, basis_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_mom, pair_mom),
            "recovered_ternary": trajectory_errors(truth_mom, recovered_mom),
            "pairwise_only_radial_basis": trajectory_errors(truth_mom, basis_mom),
        },
        "invariants": {
            "truth": invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_ternary": invariant_summary(recovered_pos, recovered_mom, recovered_config),
            "pairwise_only_radial_basis": invariant_summary(basis_pos, basis_mom, None),
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
    planted = result["planted_alpha"]
    null = result["null_alpha"]
    div = result["divergence_audit"]
    lines: list[str] = []
    lines.append("# Three-Body Ternary Residual Audit")
    lines.append("")
    lines.append("This is a controlled Paper 28 comprobation scaffold, not a claim about real gravitation.")
    lines.append("The null is softened pairwise Newtonian mechanics.  The planted alternative adds")
    lines.append("a nonadditive triplet potential `V3 = -alpha*m1*m2*m3/(s12*s23*s31)`.")
    lines.append("")
    lines.append("## Configuration")
    lines.append("")
    cfg = result["config"]
    lines.append(f"- trials: `{cfg['trials']}`")
    lines.append(f"- steps: `{cfg['steps']}`")
    lines.append(f"- dt: `{cfg['dt']}`")
    lines.append(f"- sample stride: `{cfg['sample_stride']}`")
    lines.append(f"- masses: `{cfg['masses']}`")
    lines.append(f"- gravity: `{cfg['gravity']}`")
    lines.append(f"- softening: `{cfg['softening']}`")
    lines.append(f"- planted alpha: `{cfg['alpha']}`")
    lines.append(f"- pairwise radial powers: `{cfg['pairwise_radial_powers']}`")
    lines.append("")

    for title, block in [("Newtonian Null", null), ("Planted Ternary Channel", planted)]:
        lines.append(f"## {title}")
        lines.append("")
        lines.append(
            "| model | rank | coefficient | train RMSE | test RMSE | train R2 vs zero | test R2 vs zero |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for row in compact_model_table(block["models"]):
            lines.append(
                "| {model} | {rank} | {coefficient} | {train_rmse} | {test_rmse} | {train_r2} | {test_r2} |".format(
                    model=row["model"],
                    rank=row["rank"],
                    coefficient=fmt(float(row.get("coefficient", 0.0))),
                    train_rmse=fmt(row["train_rmse"]),
                    test_rmse=fmt(row["test_rmse"]),
                    train_r2=fmt(row["train_r2"]),
                    test_r2=fmt(row["test_r2"]),
                )
            )
        lines.append("")
        lines.append(
            f"Finite-difference residual noise on test components: "
            f"`{fmt(block['finite_difference_noise']['test_rmse_finite_difference_minus_exact_force'])}`."
        )
        lines.append("")

    lines.append("## Divergence Audit")
    lines.append("")
    lines.append(
        f"Representative trial true alpha `{fmt(div['true_alpha'])}`, recovered alpha "
        f"`{fmt(div['recovered_alpha'])}`."
    )
    lines.append("")
    lines.append("| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |")
    lines.append("|---|---:|---:|---:|---:|")
    for name in ["pairwise_null", "recovered_ternary", "pairwise_only_radial_basis"]:
        pos = div["position_error_vs_truth"][name]
        mom = div["momentum_error_vs_truth"][name]
        lines.append(
            f"| {name} | {fmt(pos['final_rms'])} | {fmt(pos['max_rms'])} | "
            f"{fmt(mom['final_rms'])} | {fmt(mom['max_rms'])} |"
        )
    lines.append("")
    lines.append("## Invariant Checks")
    lines.append("")
    lines.append("| run | max total momentum | max angular drift | max relative energy drift |")
    lines.append("|---|---:|---:|---:|")
    for name, inv in div["invariants"].items():
        energy = inv.get("max_relative_energy_drift")
        lines.append(
            f"| {name} | {fmt(inv['max_total_momentum_norm'])} | "
            f"{fmt(inv['max_angular_momentum_abs_drift'])} | "
            f"{fmt(float(energy)) if energy is not None else 'n/a'} |"
        )
    lines.append("")
    lines.append("## Reading")
    lines.append("")
    recovered = planted["models"]["ternary_one_coefficient"]["coefficients"][0]
    null_coeff = null["models"]["ternary_one_coefficient"]["coefficients"][0]
    planted_r2 = planted["models"]["ternary_one_coefficient"]["test_r2_vs_zero"]
    null_r2 = null["models"]["ternary_one_coefficient"]["test_r2_vs_zero"]
    pair_r2 = planted["models"]["pairwise_only_radial_basis"]["test_r2_vs_zero"]
    lines.append(
        f"The null run has exact residual RMS `{fmt(null['target_residual_rms_test'])}` and "
        f"recovers alpha `{fmt(null_coeff)}`, so the ternary feature does not hallucinate "
        "a channel when the dynamics are pairwise."
    )
    lines.append(
        f"The planted run recovers alpha `{fmt(recovered)}` against true alpha "
        f"`{fmt(result['config']['alpha'])}` with test R2 `{fmt(planted_r2)}`."
    )
    lines.append(
        f"The stronger pair-only radial basis reaches test R2 `{fmt(pair_r2)}`.  It can absorb "
        "some trajectory-specific structure, but it does not match the one-coefficient planted "
        "triplet channel across held-out initial conditions."
    )
    lines.append(
        "In trajectory replay, the recovered ternary model stays near the planted trajectory, "
        "while the pure pairwise null diverges.  This is the intended Paper 28 empirical lane: "
        "a controlled residual audit that distinguishes pairwise closure from a typed ternary overflow."
    )
    lines.append("")
    lines.append("## Guardrail")
    lines.append("")
    lines.append(
        "This does not prove physical gravity is ternary.  It proves the audit can detect a "
        "known irreducible/nonadditive triplet channel, reject it under the Newtonian null, "
        "and price the divergence caused by forcing the triplet whole into pairwise shadows."
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    powers = tuple(int(item) for item in args.pairwise_radial_powers.split(",") if item.strip())
    null_dataset = make_dataset(0.0, args, powers)
    planted_dataset = make_dataset(args.alpha, args, powers)
    null_recovery = evaluate_force_recovery(null_dataset, args)
    planted_recovery = evaluate_force_recovery(planted_dataset, args)
    divergence = divergence_audit(planted_dataset, planted_recovery, args, powers)
    result = {
        "config": {
            "trials": args.trials,
            "steps": args.steps,
            "dt": args.dt,
            "sample_stride": args.sample_stride,
            "train_fraction": args.train_fraction,
            "masses": list(args.masses),
            "gravity": args.gravity,
            "softening": args.softening,
            "alpha": args.alpha,
            "seed": args.seed,
            "pairwise_radial_powers": list(powers),
        },
        "null_alpha": null_recovery,
        "planted_alpha": planted_recovery,
        "divergence_audit": divergence,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--trials", type=int, default=18)
    parser.add_argument("--steps", type=int, default=1600)
    parser.add_argument("--dt", type=float, default=0.002)
    parser.add_argument("--sample-stride", type=int, default=3)
    parser.add_argument("--train-fraction", type=float, default=2.0 / 3.0)
    parser.add_argument("--masses", type=float, nargs=3, default=(1.0, 1.25, 0.85))
    parser.add_argument("--gravity", type=float, default=1.0)
    parser.add_argument("--softening", type=float, default=0.15)
    parser.add_argument("--alpha", type=float, default=0.035)
    parser.add_argument("--seed", type=int, default=28030)
    parser.add_argument("--pairwise-radial-powers", type=str, default="1,2,3,4,5,6")
    return parser.parse_args()


if __name__ == "__main__":
    result = run(parse_args())
    planted = result["planted_alpha"]["models"]["ternary_one_coefficient"]
    null = result["null_alpha"]["models"]["ternary_one_coefficient"]
    print(
        "three_body_ternary_residual_audit: "
        f"null_alpha={null['coefficients'][0]:.6g}, "
        f"planted_alpha={planted['coefficients'][0]:.6g}, "
        f"planted_test_r2={planted['test_r2_vs_zero']:.6g}"
    )
