"""Four-body snap budget audit for Paper 28.

This audit checks whether snap is mandatory after the correct tetrahedral
arity is admitted.  The planted truth is the four-body tetrahedral channel
from `four_body_tetrahedral_residual_audit.py`.

Replay is measured in position and momentum.  Residual derivatives are tracked
in force units:

    R              = missed residual force
    M^-1 dR/dt     = missed kinematic jerk
    M^-1 d2R/dt2   = missed kinematic snap

Outputs:
  empirical/reports/four_body_snap_budget_audit.json
  empirical/reports/four_body_snap_budget_audit.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

import four_body_tetrahedral_residual_audit as four


DEFAULT_JSON = Path("empirical/reports/four_body_snap_budget_audit.json")
DEFAULT_REPORT = Path("empirical/reports/four_body_snap_budget_audit.md")


def fmt(value: float, digits: int = 6) -> str:
    return four.fmt(value, digits)


def coefficient_fit(x_train: np.ndarray, y_train: np.ndarray) -> np.ndarray:
    coeffs, *_ = np.linalg.lstsq(x_train, y_train, rcond=None)
    return coeffs


def score_coeffs(coeffs: np.ndarray, x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    pred = x @ coeffs
    sse = float(np.sum((y - pred) ** 2))
    sst = float(np.sum(y**2))
    return {
        "rmse": float(np.sqrt(np.mean((y - pred) ** 2))),
        "r2_vs_zero": 1.0 - sse / sst if sst > 0 else 0.0,
    }


def group_rows(rows: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    grouped: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(int(row["trial"]), []).append(row)
    for trial_rows in grouped.values():
        trial_rows.sort(key=lambda item: int(item["time_index"]))
    return grouped


def derivative_blocks(rows: list[dict[str, Any]], key: str, sample_dt: float) -> dict[str, np.ndarray]:
    x_mid: list[np.ndarray] = []
    y_mid: list[np.ndarray] = []
    x_dot: list[np.ndarray] = []
    y_dot: list[np.ndarray] = []
    x_ddot: list[np.ndarray] = []
    y_ddot: list[np.ndarray] = []
    for trial_rows in group_rows(rows).values():
        for i in range(1, len(trial_rows) - 1):
            prev_row = trial_rows[i - 1]
            row = trial_rows[i]
            next_row = trial_rows[i + 1]
            x_prev = four.stack_feature([prev_row], key)
            x_now = four.stack_feature([row], key)
            x_next = four.stack_feature([next_row], key)
            y_prev = prev_row["target_residual"]
            y_now = row["target_residual"]
            y_next = next_row["target_residual"]
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
    x_aug = np.vstack([blocks["x"], jerk_scale * blocks["x_dot"]])
    y_aug = np.concatenate([blocks["y"], jerk_scale * blocks["y_dot"]])
    return coefficient_fit(x_aug, y_aug)


def model_scores(
    coeffs: np.ndarray,
    train_rows: list[dict[str, Any]],
    test_rows: list[dict[str, Any]],
    key: str,
    sample_dt: float,
) -> dict[str, Any]:
    train_x = four.stack_feature(train_rows, key)
    train_y = four.stack_target(train_rows)
    test_x = four.stack_feature(test_rows, key)
    test_y = four.stack_target(test_rows)
    train_deriv = derivative_blocks(train_rows, key, sample_dt)
    test_deriv = derivative_blocks(test_rows, key, sample_dt)
    return {
        "rank": int(np.linalg.matrix_rank(train_x)),
        "force_train": score_coeffs(coeffs, train_x, train_y),
        "force_test": score_coeffs(coeffs, test_x, test_y),
        "jerk_train": score_coeffs(coeffs, train_deriv["x_dot"], train_deriv["y_dot"]),
        "jerk_test": score_coeffs(coeffs, test_deriv["x_dot"], test_deriv["y_dot"]),
        "snap_train": score_coeffs(coeffs, train_deriv["x_ddot"], train_deriv["y_ddot"]),
        "snap_test": score_coeffs(coeffs, test_deriv["x_ddot"], test_deriv["y_ddot"]),
    }


def residual_series(positions: np.ndarray, truth_force_fn: Any, model_force_fn: Any, masses: np.ndarray, dt: float) -> dict[str, np.ndarray]:
    residual_force = np.array([truth_force_fn(pos) - model_force_fn(pos) for pos in positions])
    acc_resid = residual_force / masses[None, :, None]
    jerk_resid = (residual_force[2:] - residual_force[:-2]) / (2.0 * dt)
    snap_resid = (residual_force[2:] - 2.0 * residual_force[1:-1] + residual_force[:-2]) / (dt * dt)
    return {
        "acc": acc_resid,
        "jerk": jerk_resid / masses[None, :, None],
        "snap": snap_resid / masses[None, :, None],
    }


def rms(array: np.ndarray) -> float:
    return float(np.sqrt(np.mean(array * array)))


def budget_summary(series: dict[str, np.ndarray], horizon: float, tolerance: float) -> dict[str, float]:
    acc_rms = rms(series["acc"][1:-1])
    jerk_rms = rms(series["jerk"])
    snap_rms = rms(series["snap"])
    acc_term = 0.5 * horizon * horizon * acc_rms
    jerk_term = (horizon**3 / 6.0) * jerk_rms
    snap_term = (horizon**4 / 24.0) * snap_rms
    total = acc_term + jerk_term + snap_term
    return {
        "mass_weighted_acc_rms": acc_rms,
        "mass_weighted_jerk_rms": jerk_rms,
        "mass_weighted_snap_rms": snap_rms,
        "position_budget_acc_term": acc_term,
        "position_budget_jerk_term": jerk_term,
        "position_budget_snap_term": snap_term,
        "position_budget_total": total,
        "snap_must_track_ratio": snap_term / tolerance if tolerance > 0 else float("inf"),
        "total_budget_ratio": total / tolerance if tolerance > 0 else float("inf"),
    }


def lower_force_from_coeffs(
    pos: np.ndarray,
    masses: np.ndarray,
    gravity: float,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
) -> np.ndarray:
    pair_count = len(four.EDGES) * len(powers)
    return (
        four.pair_force(pos, masses, gravity, softening)
        + four.pairwise_basis_force(pos, masses, softening, powers, coeffs[:pair_count])
        + four.face_basis_force(pos, masses, softening, coeffs[pair_count:])
    )


def replay_and_budget(
    lower_coeffs: np.ndarray,
    lower_jerk_coeffs: np.ndarray,
    tetra_coeff: float,
    args: argparse.Namespace,
    powers: tuple[int, ...],
) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos0, momentum0 = four.initial_condition(args.seed + args.trials + 11, masses)
    truth_config = four.ForceConfig(masses, args.gravity, args.softening, 0.0, args.beta, args.gamma)
    pair_config = four.ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.gamma)
    recovered_config = four.ForceConfig(masses, args.gravity, args.softening, 0.0, tetra_coeff, args.gamma)
    truth_force = lambda x: four.total_force(x, truth_config)
    pair_force = lambda x: four.total_force(x, pair_config)
    lower_force = lambda x: lower_force_from_coeffs(x, masses, args.gravity, args.softening, powers, lower_coeffs)
    lower_jerk_force = lambda x: lower_force_from_coeffs(
        x, masses, args.gravity, args.softening, powers, lower_jerk_coeffs
    )
    recovered_force = lambda x: four.total_force(x, recovered_config)
    truth_pos, truth_mom = four.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, truth_force)
    pair_pos, pair_mom = four.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, pair_force)
    lower_pos, lower_mom = four.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, lower_force)
    lower_jerk_pos, lower_jerk_mom = four.velocity_verlet(
        pos0, momentum0, masses, args.dt, args.replay_steps, lower_jerk_force
    )
    recovered_pos, recovered_mom = four.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, recovered_force)
    horizon = args.dt * args.replay_steps
    return {
        "horizon": horizon,
        "position_error_vs_truth": {
            "pairwise_null": four.trajectory_errors(truth_pos, pair_pos),
            "lower_force_only": four.trajectory_errors(truth_pos, lower_pos),
            "lower_jerk_aware": four.trajectory_errors(truth_pos, lower_jerk_pos),
            "recovered_tetra": four.trajectory_errors(truth_pos, recovered_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": four.trajectory_errors(truth_mom, pair_mom),
            "lower_force_only": four.trajectory_errors(truth_mom, lower_mom),
            "lower_jerk_aware": four.trajectory_errors(truth_mom, lower_jerk_mom),
            "recovered_tetra": four.trajectory_errors(truth_mom, recovered_mom),
        },
        "budget": {
            "lower_force_only": budget_summary(
                residual_series(truth_pos, truth_force, lower_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
            "lower_jerk_aware": budget_summary(
                residual_series(truth_pos, truth_force, lower_jerk_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
            "recovered_tetra": budget_summary(
                residual_series(truth_pos, truth_force, recovered_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
        },
        "invariants": {
            "truth": four.invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": four.invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_tetra": four.invariant_summary(recovered_pos, recovered_mom, recovered_config),
            "lower_force_only": four.invariant_summary(lower_pos, lower_mom, None),
            "lower_jerk_aware": four.invariant_summary(lower_jerk_pos, lower_jerk_mom, None),
        },
    }


def write_report(result: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Four-Body Snap Budget Audit")
    lines.append("")
    lines.append("This is a controlled Paper 28 scaffold, not a claim about real gravitation.")
    lines.append("The admitted tetrahedral feature is tested against lower edge-plus-face shadows.")
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
        "beta",
        "gamma",
        "jerk_scale",
        "position_tolerance",
    ):
        lines.append(f"- {key}: `{result['args'][key]}`")
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
    replay = result["replay"]
    for name, pos_err in replay["position_error_vs_truth"].items():
        mom_err = replay["momentum_error_vs_truth"][name]
        lines.append(
            f"| {name} | {fmt(pos_err['final_rms'])} | {fmt(pos_err['max_rms'])} | "
            f"{fmt(mom_err['final_rms'])} | {fmt(mom_err['max_rms'])} |"
        )
    lines.append("")
    lines.append("## Snap Budget")
    lines.append("")
    lines.append("| model | acc term | jerk term | snap term | total budget | snap/tol | total/tol |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for name, item in replay["budget"].items():
        lines.append(
            f"| {name} | {fmt(item['position_budget_acc_term'])} | "
            f"{fmt(item['position_budget_jerk_term'])} | {fmt(item['position_budget_snap_term'])} | "
            f"{fmt(item['position_budget_total'])} | {fmt(item['snap_must_track_ratio'])} | "
            f"{fmt(item['total_budget_ratio'])} |"
        )
    lines.append("")
    lines.append("## Reading")
    lines.append("")
    lines.append("If the admitted tetrahedral model keeps snap/tolerance near numerical zero,")
    lines.append("snap is not mandatory after the correct 4-ary coordinate is admitted.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=16)
    parser.add_argument("--steps", type=int, default=1400)
    parser.add_argument("--dt", type=float, default=0.0015)
    parser.add_argument("--sample-stride", type=int, default=20)
    parser.add_argument("--train-fraction", type=float, default=0.65)
    parser.add_argument("--replay-steps", type=int, default=1400)
    parser.add_argument("--seed", type=int, default=2804)
    parser.add_argument("--masses", type=float, nargs=4, default=[1.0, 1.18, 0.9, 1.07])
    parser.add_argument("--gravity", type=float, default=0.38)
    parser.add_argument("--softening", type=float, default=0.18)
    parser.add_argument("--beta", type=float, default=0.08)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--powers", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6])
    parser.add_argument("--jerk-scale", type=float, default=0.01)
    parser.add_argument("--position-tolerance", type=float, default=1e-6)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    powers = tuple(args.powers)
    sample_dt = args.dt * args.sample_stride
    dataset = four.make_dataset(0.0, args.beta, args, powers)
    train_rows, test_rows = four.split_rows(dataset["rows"], args.train_fraction)
    lower_coeffs = coefficient_fit(four.stack_feature(train_rows, "lower_features"), four.stack_target(train_rows))
    lower_jerk_coeffs = fit_jerk_aware(train_rows, "lower_features", sample_dt, args.jerk_scale)
    tetra_coeff = coefficient_fit(four.stack_feature(train_rows, "tetra_feature"), four.stack_target(train_rows))
    result = {
        "args": vars(args) | {"json_out": str(args.json_out), "report_out": str(args.report_out)},
        "sample_dt": sample_dt,
        "coefficients": {"tetra": tetra_coeff.tolist()},
        "models": {
            "lower_force_only": model_scores(lower_coeffs, train_rows, test_rows, "lower_features", sample_dt),
            "lower_jerk_aware": model_scores(lower_jerk_coeffs, train_rows, test_rows, "lower_features", sample_dt),
            "tetra_one_coeff": model_scores(tetra_coeff, train_rows, test_rows, "tetra_feature", sample_dt),
        },
        "replay": replay_and_budget(lower_coeffs, lower_jerk_coeffs, float(tetra_coeff[0]), args, powers),
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    print(
        "four_body_snap_budget_audit: "
        f"tetra_coeff={fmt(float(tetra_coeff[0]))}, "
        f"tetra_snap_to_tol={fmt(result['replay']['budget']['recovered_tetra']['snap_must_track_ratio'])}, "
        f"lower_snap_to_tol={fmt(result['replay']['budget']['lower_force_only']['snap_must_track_ratio'])}"
    )


if __name__ == "__main__":
    main()
