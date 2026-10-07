"""Six-body snap budget audit for Paper 28.

This audit asks whether lower-arity <=4 models can match short-horizon force
well while losing long-horizon replay on a planted 2x3 carry channel, and
whether the mass-weighted snap budget of the missed carry residual predicts
that loss.

State replay is tracked with position and momentum.  Residual derivatives are
tracked in force units:

    R       = missed residual force
    M^-1 dR/dt  = missed kinematic jerk
    M^-1 d2R/dt2 = missed kinematic snap

For constant masses, dF/dt = m*jerk and d2F/dt2 = m*snap.

Outputs:
  empirical/reports/six_body_snap_budget_audit.json
  empirical/reports/six_body_snap_budget_audit.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

import six_body_arity_carry_audit as carry


DEFAULT_JSON = Path("empirical/reports/six_body_snap_budget_audit.json")
DEFAULT_REPORT = Path("empirical/reports/six_body_snap_budget_audit.md")


def fmt(value: float, digits: int = 6) -> str:
    return carry.fmt(value, digits)


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


def derivative_blocks(
    rows: list[dict[str, Any]],
    feature_key: str,
    sample_dt: float,
) -> dict[str, np.ndarray]:
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
            x_prev = prev_row[feature_key]
            x_now = row[feature_key]
            x_next = next_row[feature_key]
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


def fit_force_only(train_rows: list[dict[str, Any]], key: str) -> np.ndarray:
    return coefficient_fit(carry.stack_feature(train_rows, key), carry.stack_target(train_rows))


def fit_jerk_aware(
    train_rows: list[dict[str, Any]],
    key: str,
    sample_dt: float,
    jerk_scale: float,
) -> np.ndarray:
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
    train_x = carry.stack_feature(train_rows, key)
    train_y = carry.stack_target(train_rows)
    test_x = carry.stack_feature(test_rows, key)
    test_y = carry.stack_target(test_rows)
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


def full_force_from_lower_coeffs(
    pos: np.ndarray,
    masses: np.ndarray,
    gravity: float,
    softening: float,
    powers: tuple[int, ...],
    coeffs: np.ndarray,
) -> np.ndarray:
    return carry.pair_force(pos, masses, gravity, softening) + carry.feature_force_from_coeffs(
        pos, masses, softening, powers, coeffs, "lower_le4_features"
    )


def residual_series(
    positions: np.ndarray,
    truth_force_fn: Any,
    model_force_fn: Any,
    masses: np.ndarray,
    dt: float,
) -> dict[str, Any]:
    residual_force = np.array([truth_force_fn(pos) - model_force_fn(pos) for pos in positions])
    acc_resid = residual_force / masses[None, :, None]
    jerk_resid = (residual_force[2:] - residual_force[:-2]) / (2.0 * dt)
    snap_resid = (residual_force[2:] - 2.0 * residual_force[1:-1] + residual_force[:-2]) / (dt * dt)
    mass_jerk = jerk_resid / masses[None, :, None]
    mass_snap = snap_resid / masses[None, :, None]
    return {
        "force": residual_force,
        "acc": acc_resid,
        "jerk": mass_jerk,
        "snap": mass_snap,
    }


def rms(array: np.ndarray) -> float:
    return float(np.sqrt(np.mean(array * array)))


def max_body_norm(array: np.ndarray) -> float:
    norms = np.linalg.norm(array, axis=2)
    return float(np.max(norms))


def budget_summary(series: dict[str, Any], horizon: float, tolerance: float) -> dict[str, float]:
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
        "mass_weighted_acc_max_body_norm": max_body_norm(series["acc"][1:-1]),
        "mass_weighted_jerk_max_body_norm": max_body_norm(series["jerk"]),
        "mass_weighted_snap_max_body_norm": max_body_norm(series["snap"]),
        "position_budget_acc_term": acc_term,
        "position_budget_jerk_term": jerk_term,
        "position_budget_snap_term": snap_term,
        "position_budget_total": total,
        "snap_must_track_ratio": snap_term / tolerance if tolerance > 0 else float("inf"),
        "total_budget_ratio": total / tolerance if tolerance > 0 else float("inf"),
    }


def trajectory_errors(reference: np.ndarray, candidate: np.ndarray) -> dict[str, float]:
    return carry.trajectory_errors(reference, candidate)


def replay_and_budget(
    force_only_coeffs: np.ndarray,
    jerk_aware_coeffs: np.ndarray,
    carry_coeff: float,
    args: argparse.Namespace,
    powers: tuple[int, ...],
) -> dict[str, Any]:
    masses = np.array(args.masses, dtype=np.float64)
    pos0, momentum0 = carry.initial_condition(args.seed + args.trials + 37, masses)
    truth_config = carry.ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.kappa_23)
    recovered_config = carry.ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, carry_coeff)
    pair_config = carry.ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, 0.0)

    truth_force = lambda x: carry.total_force(x, truth_config)
    pair_force = lambda x: carry.total_force(x, pair_config)
    force_only_force = lambda x: full_force_from_lower_coeffs(
        x, masses, args.gravity, args.softening, powers, force_only_coeffs
    )
    jerk_aware_force = lambda x: full_force_from_lower_coeffs(
        x, masses, args.gravity, args.softening, powers, jerk_aware_coeffs
    )
    recovered_force = lambda x: carry.total_force(x, recovered_config)

    truth_pos, truth_mom = carry.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, truth_force)
    pair_pos, pair_mom = carry.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, pair_force)
    force_only_pos, force_only_mom = carry.velocity_verlet(
        pos0, momentum0, masses, args.dt, args.replay_steps, force_only_force
    )
    jerk_aware_pos, jerk_aware_mom = carry.velocity_verlet(
        pos0, momentum0, masses, args.dt, args.replay_steps, jerk_aware_force
    )
    recovered_pos, recovered_mom = carry.velocity_verlet(pos0, momentum0, masses, args.dt, args.replay_steps, recovered_force)

    horizon = args.replay_steps * args.dt
    return {
        "horizon": horizon,
        "position_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_pos, pair_pos),
            "lower_force_only": trajectory_errors(truth_pos, force_only_pos),
            "lower_jerk_aware": trajectory_errors(truth_pos, jerk_aware_pos),
            "recovered_carry23": trajectory_errors(truth_pos, recovered_pos),
        },
        "momentum_error_vs_truth": {
            "pairwise_null": trajectory_errors(truth_mom, pair_mom),
            "lower_force_only": trajectory_errors(truth_mom, force_only_mom),
            "lower_jerk_aware": trajectory_errors(truth_mom, jerk_aware_mom),
            "recovered_carry23": trajectory_errors(truth_mom, recovered_mom),
        },
        "budget": {
            "lower_force_only": budget_summary(
                residual_series(truth_pos, truth_force, force_only_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
            "lower_jerk_aware": budget_summary(
                residual_series(truth_pos, truth_force, jerk_aware_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
            "recovered_carry23": budget_summary(
                residual_series(truth_pos, truth_force, recovered_force, masses, args.dt),
                horizon,
                args.position_tolerance,
            ),
        },
        "invariants": {
            "truth": carry.invariant_summary(truth_pos, truth_mom, truth_config),
            "pairwise_null": carry.invariant_summary(pair_pos, pair_mom, pair_config),
            "recovered_carry23": carry.invariant_summary(recovered_pos, recovered_mom, recovered_config),
            "lower_force_only": carry.invariant_summary(force_only_pos, force_only_mom, None),
            "lower_jerk_aware": carry.invariant_summary(jerk_aware_pos, jerk_aware_mom, None),
        },
    }


def write_report(result: dict[str, Any], path: Path) -> None:
    lines: list[str] = []
    lines.append("# Six-Body Snap Budget Audit")
    lines.append("")
    lines.append("This is a controlled Paper 28 scaffold, not a claim about real gravitation.")
    lines.append("Replay state is tracked as position and momentum. Residual derivatives are")
    lines.append("tracked in force units: `R`, `M^-1 dR/dt` (jerk), and `M^-1 d2R/dt2` (snap).")
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
        "kappa_23",
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
    lines.append("## Invariants")
    lines.append("")
    lines.append("| trajectory | max |P| | max angular drift | max relative energy drift |")
    lines.append("|---|---:|---:|---:|")
    for name, inv in replay["invariants"].items():
        lines.append(
            f"| {name} | {fmt(inv['max_total_momentum_norm'])} | "
            f"{fmt(inv['max_angular_momentum_drift'])} | "
            f"{fmt(inv.get('max_relative_energy_drift', float('nan')))} |"
        )
    lines.append("")
    lines.append("## Reading")
    lines.append("")
    lines.append("A lower-arity model may score well on force and jerk while still losing")
    lines.append("long-horizon replay. Snap becomes a must-track residual when the snap term")
    lines.append("exceeds the declared position tolerance or materially dominates the budget.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--steps", type=int, default=850)
    parser.add_argument("--dt", type=float, default=0.0015)
    parser.add_argument("--sample-stride", type=int, default=25)
    parser.add_argument("--train-fraction", type=float, default=0.6)
    parser.add_argument("--replay-steps", type=int, default=850)
    parser.add_argument("--seed", type=int, default=2806)
    parser.add_argument("--masses", type=float, nargs=carry.N, default=[1.0, 1.12, 0.94, 1.07, 0.89, 1.16])
    parser.add_argument("--gravity", type=float, default=0.18)
    parser.add_argument("--softening", type=float, default=0.3)
    parser.add_argument("--kappa-23", type=float, default=0.006)
    parser.add_argument("--powers", type=int, nargs="+", default=[1, 2, 3, 4, 5, 6])
    parser.add_argument("--jerk-scale", type=float, default=0.01)
    parser.add_argument("--position-tolerance", type=float, default=1e-3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-out", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    powers = tuple(args.powers)
    masses = np.array(args.masses, dtype=np.float64)
    sample_dt = args.dt * args.sample_stride
    config = carry.ForceConfig(masses, args.gravity, args.softening, 0.0, 0.0, args.kappa_23)
    dataset = carry.make_dataset(config, args, powers)
    train_rows, test_rows = carry.split_rows(dataset["rows"], args.train_fraction)
    force_only_coeffs = fit_force_only(train_rows, "lower_le4_features")
    jerk_aware_coeffs = fit_jerk_aware(train_rows, "lower_le4_features", sample_dt, args.jerk_scale)
    carry_coeff = coefficient_fit(carry.stack_feature(train_rows, "carry23_feature"), carry.stack_target(train_rows))
    result = {
        "args": vars(args) | {"json_out": str(args.json_out), "report_out": str(args.report_out)},
        "sample_dt": sample_dt,
        "models": {
            "lower_force_only": model_scores(force_only_coeffs, train_rows, test_rows, "lower_le4_features", sample_dt),
            "lower_jerk_aware": model_scores(jerk_aware_coeffs, train_rows, test_rows, "lower_le4_features", sample_dt),
            "carry23_one_coeff": model_scores(carry_coeff, train_rows, test_rows, "carry23_feature", sample_dt),
        },
        "coefficients": {
            "carry23": carry_coeff.tolist(),
        },
        "replay": replay_and_budget(force_only_coeffs, jerk_aware_coeffs, float(carry_coeff[0]), args, powers),
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.report_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report_out)
    force_r2 = result["models"]["lower_force_only"]["force_test"]["r2_vs_zero"]
    jerk_r2 = result["models"]["lower_jerk_aware"]["jerk_test"]["r2_vs_zero"]
    snap_ratio = result["replay"]["budget"]["lower_jerk_aware"]["snap_must_track_ratio"]
    final_error = result["replay"]["position_error_vs_truth"]["lower_jerk_aware"]["final_rms"]
    print(
        "six_body_snap_budget_audit: "
        f"force_only_test_r2={fmt(force_r2)}, jerk_aware_jerk_r2={fmt(jerk_r2)}, "
        f"jerk_aware_final_pos={fmt(final_error)}, snap_to_tol={fmt(snap_ratio)}"
    )


if __name__ == "__main__":
    main()
