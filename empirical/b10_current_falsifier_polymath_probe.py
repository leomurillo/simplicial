"""B10 current falsifier polymath probe.

B10 is an adversarial synthetic test for the B-series current bucket.

B3 showed that signed current beats scalar and symmetric evidence when the task
is time reversal. B8 then warned that a continuous precision-active rival can
come close to the bucket router once labels are removed. This probe combines
those lessons.

The synthetic "brain" can generate directional behavior in three ways:

    1. null_world: no current, no directional action;
    2. continuous_world: action vigor varies smoothly with solenoidal current;
    3. bucket_world: a discrete current gate admits or refuses the route.

The scalar score, symmetric transition backbone, stationary occupancy, and ring
geometry are matched. The compared agents are deliberately simple:

    - scalar baseline;
    - symmetric baseline;
    - continuous_solenoidal rival;
    - conformal bucket_current gate;
    - hybrid flow-plus-gate model.

The B-series earns a strong current-bucket claim only when the bucket gate adds
held-out predictive power beyond the continuous solenoidal rival and controls
false current admission on null worlds. If the continuous rival wins or the
hybrid wins, B10 weakens the pure-bucket interpretation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


SOURCES = ["bucket_world", "continuous_world", "null_world"]
MODEL_ORDER = [
    "scalar",
    "symmetric",
    "continuous_solenoidal",
    "bucket_current",
    "governed_flow_gate",
    "hybrid_flow_gate",
]


@dataclass(frozen=True)
class Episode:
    source: str
    sign: int
    strength: float
    length: int
    target_clean: float
    target_observed: float
    scalar_score: float
    symmetric_score: float
    current_hat: float
    abs_current_hat: float
    precision: float
    forward_steps: int
    reverse_steps: int
    stay_steps: int


@dataclass(frozen=True)
class LinearModel:
    name: str
    feature_kind: str
    coef: list[float]
    mean: list[float]
    sd: list[float]


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def route_class(value: float, threshold: float) -> int:
    if value > threshold:
        return 1
    if value < -threshold:
        return -1
    return 0


def simulate_steps(
    rng: np.random.Generator,
    length: int,
    move_prob: float,
    current: float,
) -> np.ndarray:
    forward_prob = 0.5 * (move_prob + current)
    reverse_prob = 0.5 * (move_prob - current)
    stay_prob = 1.0 - move_prob
    if forward_prob < 0.0 or reverse_prob < 0.0 or stay_prob < 0.0:
        raise ValueError("invalid transition probabilities")
    return rng.choice(
        np.asarray([1, -1, 0], dtype=int),
        size=length,
        p=np.asarray([forward_prob, reverse_prob, stay_prob], dtype=float),
    )


def make_episode(
    rng: np.random.Generator,
    source: str,
    length_choices: list[int],
    move_prob: float,
    bucket_gate: float,
    continuous_scale: float,
    weak_range: tuple[float, float],
    strong_range: tuple[float, float],
    continuous_range: tuple[float, float],
    behavior_noise: float,
) -> Episode:
    length = int(rng.choice(np.asarray(length_choices, dtype=int)))
    if source == "null_world":
        sign = 0
        strength = 0.0
        current = 0.0
        target_clean = 0.0
    elif source == "bucket_world":
        sign = int(rng.choice(np.asarray([-1, 1], dtype=int)))
        if rng.random() < 0.5:
            strength = float(rng.uniform(*weak_range))
        else:
            strength = float(rng.uniform(*strong_range))
        current = sign * strength
        target_clean = float(sign) if strength >= bucket_gate else 0.0
    elif source == "continuous_world":
        sign = int(rng.choice(np.asarray([-1, 1], dtype=int)))
        strength = float(rng.uniform(*continuous_range))
        current = sign * strength
        target_clean = float(sign) * float(np.tanh(strength / continuous_scale))
    else:
        raise ValueError(f"unknown source: {source}")

    steps = simulate_steps(rng, length=length, move_prob=move_prob, current=current)
    stay_prob = 1.0 - move_prob
    move_side_prob = 0.5 * move_prob
    nll = np.where(steps == 0, -np.log(stay_prob), -np.log(move_side_prob))
    current_hat = float(np.mean(steps))
    symmetric_score = float(np.mean(np.abs(steps)))
    scalar_score = float(np.mean(nll))
    # Precision is an observation-quality variable available to the continuous
    # rival. It is not a hidden bucket label.
    precision = float(np.sqrt(length) / max(np.sqrt(move_prob * (1.0 - move_prob / 2.0)), 1e-9))
    target_observed = float(np.clip(target_clean + rng.normal(scale=behavior_noise), -1.25, 1.25))

    return Episode(
        source=source,
        sign=sign,
        strength=strength,
        length=length,
        target_clean=target_clean,
        target_observed=target_observed,
        scalar_score=scalar_score,
        symmetric_score=symmetric_score,
        current_hat=current_hat,
        abs_current_hat=abs(current_hat),
        precision=precision,
        forward_steps=int(np.sum(steps == 1)),
        reverse_steps=int(np.sum(steps == -1)),
        stay_steps=int(np.sum(steps == 0)),
    )


def make_dataset(
    rng: np.random.Generator,
    route_trials: int,
    null_trials: int,
    bucket_mix: float,
    length_choices: list[int],
    move_prob: float,
    bucket_gate: float,
    continuous_scale: float,
    weak_range: tuple[float, float],
    strong_range: tuple[float, float],
    continuous_range: tuple[float, float],
    behavior_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    for _ in range(route_trials):
        source = "bucket_world" if rng.random() < bucket_mix else "continuous_world"
        episodes.append(
            make_episode(
                rng,
                source=source,
                length_choices=length_choices,
                move_prob=move_prob,
                bucket_gate=bucket_gate,
                continuous_scale=continuous_scale,
                weak_range=weak_range,
                strong_range=strong_range,
                continuous_range=continuous_range,
                behavior_noise=behavior_noise,
            )
        )
    for _ in range(null_trials):
        episodes.append(
            make_episode(
                rng,
                source="null_world",
                length_choices=length_choices,
                move_prob=move_prob,
                bucket_gate=bucket_gate,
                continuous_scale=continuous_scale,
                weak_range=weak_range,
                strong_range=strong_range,
                continuous_range=continuous_range,
                behavior_noise=behavior_noise,
            )
        )
    rng.shuffle(episodes)
    return episodes


def feature_matrix(
    episodes: list[Episode],
    feature_kind: str,
    current_gate: float,
) -> np.ndarray:
    rows: list[list[float]] = []
    for e in episodes:
        admitted = 1.0 if e.abs_current_hat > current_gate else 0.0
        admitted_sign = float(np.sign(e.current_hat)) * admitted
        flow = e.current_hat * e.precision
        flow_abs = e.abs_current_hat * e.precision
        if feature_kind == "scalar":
            row = [e.scalar_score]
        elif feature_kind == "symmetric":
            row = [e.scalar_score, e.symmetric_score]
        elif feature_kind == "continuous_solenoidal":
            row = [e.scalar_score, e.symmetric_score, e.current_hat, e.abs_current_hat, flow, flow_abs]
        elif feature_kind == "bucket_current":
            row = [e.scalar_score, e.symmetric_score, admitted_sign, admitted]
        elif feature_kind == "governed_flow_gate":
            row = [
                e.scalar_score,
                e.symmetric_score,
                admitted * e.current_hat,
                admitted * e.abs_current_hat,
                admitted * flow,
                admitted * flow_abs,
                admitted,
            ]
        elif feature_kind == "hybrid_flow_gate":
            row = [
                e.scalar_score,
                e.symmetric_score,
                e.current_hat,
                e.abs_current_hat,
                flow,
                flow_abs,
                admitted_sign,
                admitted,
            ]
        else:
            raise ValueError(f"unknown feature kind: {feature_kind}")
        rows.append(row)
    return np.asarray(rows, dtype=float)


def standardize_train(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = np.mean(x, axis=0)
    sd = np.std(x, axis=0)
    sd = np.where(sd < 1e-12, 1.0, sd)
    return (x - mean) / sd, mean, sd


def standardize_apply(x: np.ndarray, mean: np.ndarray, sd: np.ndarray) -> np.ndarray:
    return (x - mean) / sd


def fit_linear_model(
    name: str,
    feature_kind: str,
    train: list[Episode],
    current_gate: float,
    ridge: float,
) -> LinearModel:
    x = feature_matrix(train, feature_kind, current_gate=current_gate)
    y = np.asarray([e.target_observed for e in train], dtype=float)
    xs, mean, sd = standardize_train(x)
    design = np.column_stack([np.ones(len(xs)), xs])
    gram = design.T @ design
    reg = ridge * np.eye(gram.shape[0])
    reg[0, 0] = 0.0
    coef = np.linalg.solve(gram + reg, design.T @ y)
    return LinearModel(
        name=name,
        feature_kind=feature_kind,
        coef=[float(v) for v in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
    )


def predict(model: LinearModel, episodes: list[Episode], current_gate: float) -> np.ndarray:
    x = feature_matrix(episodes, model.feature_kind, current_gate=current_gate)
    mean = np.asarray(model.mean, dtype=float)
    sd = np.asarray(model.sd, dtype=float)
    xs = standardize_apply(x, mean, sd)
    design = np.column_stack([np.ones(len(xs)), xs])
    coef = np.asarray(model.coef, dtype=float)
    return design @ coef


def regression_metrics(
    episodes: list[Episode],
    pred: np.ndarray,
    class_threshold: float,
) -> dict[str, float]:
    y = np.asarray([e.target_observed for e in episodes], dtype=float)
    clean = np.asarray([e.target_clean for e in episodes], dtype=float)
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    clean_rmse = float(np.sqrt(np.mean((pred - clean) ** 2)))
    mae = float(np.mean(np.abs(pred - y)))
    denom = float(np.sum((y - float(np.mean(y))) ** 2))
    r2 = 1.0 - float(np.sum((pred - y) ** 2)) / denom if denom > 1e-12 else float("nan")
    if len(pred) > 1 and float(np.std(pred)) > 1e-12 and float(np.std(y)) > 1e-12:
        corr = float(np.corrcoef(pred, y)[0, 1])
    else:
        corr = float("nan")
    pred_class = np.asarray([route_class(float(v), class_threshold) for v in pred], dtype=int)
    truth_class = np.asarray([route_class(float(v), class_threshold) for v in clean], dtype=int)
    route_accuracy = float(np.mean(pred_class == truth_class))
    false_action = float(np.mean(np.abs(pred) > class_threshold))
    return {
        "rmse_observed": rmse,
        "rmse_clean": clean_rmse,
        "mae_observed": mae,
        "r2_observed": r2,
        "corr_observed": corr,
        "route_accuracy_clean": route_accuracy,
        "action_rate_predicted": false_action,
    }


def evaluate_models(
    train: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    class_threshold: float,
) -> dict[str, Any]:
    null_abs = [e.abs_current_hat for e in train if e.source == "null_world"]
    current_gate = quantile(null_abs, 1.0 - alpha)
    models = {
        name: fit_linear_model(name, name, train, current_gate=current_gate, ridge=ridge)
        for name in MODEL_ORDER
    }
    predictions = {name: predict(model, test, current_gate=current_gate) for name, model in models.items()}

    overall = {
        name: regression_metrics(test, pred, class_threshold=class_threshold)
        for name, pred in predictions.items()
    }
    by_source: dict[str, dict[str, dict[str, float]]] = {}
    for source in SOURCES:
        rows = [e for e in test if e.source == source]
        if not rows:
            continue
        idx = np.asarray([i for i, e in enumerate(test) if e.source == source], dtype=int)
        by_source[source] = {
            name: regression_metrics(rows, pred[idx], class_threshold=class_threshold)
            for name, pred in predictions.items()
        }

    null_rows = [e for e in test if e.source == "null_world"]
    null_idx = np.asarray([i for i, e in enumerate(test) if e.source == "null_world"], dtype=int)
    null_false_action = {
        name: float(np.mean(np.abs(predictions[name][null_idx]) > class_threshold)) if null_rows else float("nan")
        for name in MODEL_ORDER
    }

    best_rmse = min(overall[name]["rmse_observed"] for name in MODEL_ORDER)
    winners = [
        name
        for name in MODEL_ORDER
        if abs(overall[name]["rmse_observed"] - best_rmse) <= 1e-9
    ]

    return {
        "current_gate": current_gate,
        "models": {name: model.__dict__ for name, model in models.items()},
        "overall": overall,
        "by_source": by_source,
        "null_false_action": null_false_action,
        "winner": winners[0],
        "predictions_sample": {
            name: [float(v) for v in predictions[name][:8]]
            for name in MODEL_ORDER
        },
    }


def source_counts(episodes: list[Episode]) -> dict[str, int]:
    return {source: sum(1 for e in episodes if e.source == source) for source in SOURCES}


def mean_episode_scores(episodes: list[Episode]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for source in SOURCES:
        rows = [e for e in episodes if e.source == source]
        if not rows:
            continue
        out[source] = {
            "strength": float(np.mean([e.strength for e in rows])),
            "target_clean_abs": float(np.mean([abs(e.target_clean) for e in rows])),
            "scalar_score": float(np.mean([e.scalar_score for e in rows])),
            "symmetric_score": float(np.mean([e.symmetric_score for e in rows])),
            "current_hat_abs": float(np.mean([e.abs_current_hat for e in rows])),
            "length": float(np.mean([e.length for e in rows])),
        }
    return out


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    length_choices = [int(x) for x in args.lengths.split(",") if x.strip()]
    weak_range = (args.weak_min, args.weak_max)
    strong_range = (args.strong_min, args.strong_max)
    continuous_range = (args.continuous_min, args.continuous_max)

    main_train = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        bucket_mix=args.main_bucket_mix,
        length_choices=length_choices,
        move_prob=args.move_prob,
        bucket_gate=args.bucket_gate,
        continuous_scale=args.continuous_scale,
        weak_range=weak_range,
        strong_range=strong_range,
        continuous_range=continuous_range,
        behavior_noise=args.behavior_noise,
    )
    main_test = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        bucket_mix=args.main_bucket_mix,
        length_choices=length_choices,
        move_prob=args.move_prob,
        bucket_gate=args.bucket_gate,
        continuous_scale=args.continuous_scale,
        weak_range=weak_range,
        strong_range=strong_range,
        continuous_range=continuous_range,
        behavior_noise=args.behavior_noise,
    )
    main_eval = evaluate_models(
        main_train,
        main_test,
        alpha=args.alpha,
        ridge=args.ridge,
        class_threshold=args.class_threshold,
    )

    sweep: list[dict[str, Any]] = []
    for mix in args.mix_grid:
        train = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            bucket_mix=float(mix),
            length_choices=length_choices,
            move_prob=args.move_prob,
            bucket_gate=args.bucket_gate,
            continuous_scale=args.continuous_scale,
            weak_range=weak_range,
            strong_range=strong_range,
            continuous_range=continuous_range,
            behavior_noise=args.behavior_noise,
        )
        test = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            bucket_mix=float(mix),
            length_choices=length_choices,
            move_prob=args.move_prob,
            bucket_gate=args.bucket_gate,
            continuous_scale=args.continuous_scale,
            weak_range=weak_range,
            strong_range=strong_range,
            continuous_range=continuous_range,
            behavior_noise=args.behavior_noise,
        )
        eval_result = evaluate_models(
            train,
            test,
            alpha=args.alpha,
            ridge=args.ridge,
            class_threshold=args.class_threshold,
        )
        sweep.append(
            {
                "bucket_mix": float(mix),
                "train_counts": source_counts(train),
                "test_counts": source_counts(test),
                "winner": eval_result["winner"],
                "current_gate": eval_result["current_gate"],
                "overall_rmse": {
                    name: eval_result["overall"][name]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "overall_route_accuracy": {
                    name: eval_result["overall"][name]["route_accuracy_clean"]
                    for name in MODEL_ORDER
                },
                "null_false_action": eval_result["null_false_action"],
                "hybrid_gain_over_continuous": (
                    eval_result["overall"]["continuous_solenoidal"]["rmse_observed"]
                    - eval_result["overall"]["hybrid_flow_gate"]["rmse_observed"]
                ),
                "bucket_penalty_vs_continuous": (
                    eval_result["overall"]["bucket_current"]["rmse_observed"]
                    - eval_result["overall"]["continuous_solenoidal"]["rmse_observed"]
                ),
            }
        )

    continuous_rmse = main_eval["overall"]["continuous_solenoidal"]["rmse_observed"]
    bucket_rmse = main_eval["overall"]["bucket_current"]["rmse_observed"]
    governed_rmse = main_eval["overall"]["governed_flow_gate"]["rmse_observed"]
    hybrid_rmse = main_eval["overall"]["hybrid_flow_gate"]["rmse_observed"]
    hybrid_gain = continuous_rmse - hybrid_rmse
    bucket_penalty = bucket_rmse - continuous_rmse
    null_fa_bucket = main_eval["null_false_action"]["bucket_current"]
    null_fa_cont = main_eval["null_false_action"]["continuous_solenoidal"]
    null_fa_governed = main_eval["null_false_action"]["governed_flow_gate"]

    if bucket_rmse + args.decision_margin < continuous_rmse and null_fa_bucket <= args.alpha:
        finding = "BUCKET_CURRENT_SURVIVES_STRONG_RIVAL"
    elif (
        continuous_rmse + args.decision_margin < bucket_rmse
        and null_fa_cont > max(args.alpha * 2.0, null_fa_bucket + args.false_action_margin)
    ):
        finding = "FLOW_FITS_BUT_GATE_GOVERNS_FALSE_ADMISSION"
    elif continuous_rmse + args.decision_margin < bucket_rmse and hybrid_gain <= args.decision_margin:
        finding = "CONTINUOUS_SOLENOIDAL_RIVAL_WINS"
    elif min(hybrid_rmse, governed_rmse) + args.decision_margin < min(bucket_rmse, continuous_rmse):
        finding = "HYBRID_FLOW_GATE_NEEDED"
    else:
        finding = "RIVAL_MATCH_BUCKET_NOT_UNIQUE"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config": {
            "seed": args.seed,
            "route_trials": args.route_trials,
            "null_trials": args.null_trials,
            "sweep_route_trials": args.sweep_route_trials,
            "sweep_null_trials": args.sweep_null_trials,
            "main_bucket_mix": args.main_bucket_mix,
            "mix_grid": [float(v) for v in args.mix_grid],
            "length_choices": length_choices,
            "move_prob": args.move_prob,
            "bucket_gate": args.bucket_gate,
            "continuous_scale": args.continuous_scale,
            "weak_range": list(weak_range),
            "strong_range": list(strong_range),
            "continuous_range": list(continuous_range),
            "behavior_noise": args.behavior_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "class_threshold": args.class_threshold,
            "decision_margin": args.decision_margin,
        },
        "finding": finding,
        "main_train_counts": source_counts(main_train),
        "main_test_counts": source_counts(main_test),
        "main_train_means": mean_episode_scores(main_train),
        "main_test_means": mean_episode_scores(main_test),
        "main_eval": main_eval,
        "decision_quantities": {
            "continuous_rmse": continuous_rmse,
            "bucket_rmse": bucket_rmse,
            "governed_rmse": governed_rmse,
            "hybrid_rmse": hybrid_rmse,
            "hybrid_gain_over_continuous": hybrid_gain,
            "bucket_penalty_vs_continuous": bucket_penalty,
            "bucket_null_false_action": null_fa_bucket,
            "continuous_null_false_action": null_fa_cont,
            "governed_null_false_action": null_fa_governed,
        },
        "phase_sweep": sweep,
    }


def fmt(value: float) -> str:
    if isinstance(value, float) and np.isnan(value):
        return "nan"
    return f"{value:.3f}"


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def write_report(path: Path, result: dict[str, Any]) -> None:
    config = result["config"]
    main = result["main_eval"]

    overall_rows = []
    for name in MODEL_ORDER:
        data = main["overall"][name]
        overall_rows.append(
            [
                name,
                fmt(data["rmse_observed"]),
                fmt(data["rmse_clean"]),
                fmt(data["r2_observed"]),
                fmt(data["route_accuracy_clean"]),
                fmt(main["null_false_action"][name]),
            ]
        )

    by_source_rows = []
    for source, source_data in main["by_source"].items():
        for name in MODEL_ORDER:
            data = source_data[name]
            by_source_rows.append(
                [
                    source,
                    name,
                    fmt(data["rmse_observed"]),
                    fmt(data["route_accuracy_clean"]),
                    fmt(data["action_rate_predicted"]),
                ]
            )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["bucket_mix"]),
                row["winner"],
                fmt(row["overall_rmse"]["continuous_solenoidal"]),
                fmt(row["overall_rmse"]["bucket_current"]),
                fmt(row["overall_rmse"]["governed_flow_gate"]),
                fmt(row["overall_rmse"]["hybrid_flow_gate"]),
                fmt(row["hybrid_gain_over_continuous"]),
                fmt(row["bucket_penalty_vs_continuous"]),
                fmt(row["null_false_action"]["bucket_current"]),
            ]
        )

    means_rows = []
    for source, data in result["main_test_means"].items():
        means_rows.append(
            [
                source,
                fmt(data["strength"]),
                fmt(data["target_clean_abs"]),
                fmt(data["scalar_score"]),
                fmt(data["symmetric_score"]),
                fmt(data["current_hat_abs"]),
                fmt(data["length"]),
            ]
        )

    dq = result["decision_quantities"]
    lines = [
        "# B10 Current Falsifier Polymath Probe",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- main bucket mix: `{config['main_bucket_mix']}`",
        f"- route/null trials: `{config['route_trials']}` / `{config['null_trials']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "B10 asks whether the current bucket survives a fair continuous",
        "solenoidal rival. The synthetic generator can be smooth-flow,",
        "discrete-gate, or mixed. If the model-selection result always favors",
        "the bucket, the experiment is suspicious. If the winner changes with",
        "the generating world, the probe is doing real falsifier work.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous RMSE", fmt(dq["continuous_rmse"])],
                ["bucket RMSE", fmt(dq["bucket_rmse"])],
                ["governed flow-gate RMSE", fmt(dq["governed_rmse"])],
                ["hybrid RMSE", fmt(dq["hybrid_rmse"])],
                ["hybrid gain over continuous", fmt(dq["hybrid_gain_over_continuous"])],
                ["bucket penalty vs continuous", fmt(dq["bucket_penalty_vs_continuous"])],
                ["bucket null false action", fmt(dq["bucket_null_false_action"])],
                ["continuous null false action", fmt(dq["continuous_null_false_action"])],
                ["governed null false action", fmt(dq["governed_null_false_action"])],
                ["conformal current gate", fmt(main["current_gate"])],
            ],
        ),
        "",
        "## Main Model Summary",
        "",
        md_table(
            [
                "model",
                "RMSE observed",
                "RMSE clean",
                "R2 observed",
                "route acc",
                "null false action",
            ],
            overall_rows,
        ),
        "",
        "## Source-Level Summary",
        "",
        md_table(
            ["source", "model", "RMSE observed", "route acc", "action rate pred"],
            by_source_rows,
        ),
        "",
        "## Main Test Means",
        "",
        md_table(
            [
                "source",
                "mean strength",
                "mean abs target",
                "scalar",
                "symmetric",
                "abs current_hat",
                "length",
            ],
            means_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "bucket mix",
                "winner",
                "continuous RMSE",
                "bucket RMSE",
                "governed RMSE",
                "hybrid RMSE",
                "hybrid gain",
                "bucket penalty",
                "bucket null FA",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    finding = result["finding"]
    if finding == "BUCKET_CURRENT_SURVIVES_STRONG_RIVAL":
        lines.extend(
            [
                "The bucket current gate beats the continuous solenoidal rival on",
                "held-out behavior while controlling false action on null worlds.",
                "That would support the stronger B-series reading: current is not",
                "just smooth flow; it also has a route-admission event.",
            ]
        )
    elif finding == "CONTINUOUS_SOLENOIDAL_RIVAL_WINS":
        lines.extend(
            [
                "The continuous solenoidal rival beats the bucket model, and the",
                "hybrid adds little. This is a falsifying result for the pure",
                "current-bucket story. The safer claim would be that the current",
                "bucket is a discretized readout of continuous temporal flow.",
            ]
        )
    elif finding == "FLOW_FITS_BUT_GATE_GOVERNS_FALSE_ADMISSION":
        lines.extend(
            [
                "The continuous solenoidal rival fits directional vigor better,",
                "but it produces too many false actions on null worlds. The",
                "bucket gate does not win magnitude prediction; it wins admission",
                "control. B10 therefore supports a governed-flow hypothesis:",
                "continuous temporal current supplies the variable, while a",
                "conformal-style gate decides when the current is actionable.",
            ]
        )
    elif finding == "HYBRID_FLOW_GATE_NEEDED":
        lines.extend(
            [
                "The hybrid model wins: smooth current magnitude and discrete",
                "current admission both carry predictive information. This does",
                "not vindicate a pure bucket story. It suggests a two-level",
                "hypothesis: continuous temporal flow with a governed route gate.",
            ]
        )
    else:
        lines.extend(
            [
                "The bucket and continuous rival are too close to separate. The",
                "honest conclusion is B8-like: current-bucket language may be a",
                "useful operational discretization, but uniqueness is not",
                "established.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the continuous rival receives signed current magnitude and precision;",
            "- the bucket model receives only a conformal admission gate and sign;",
            "- null worlds calibrate false current admission;",
            "- the phase sweep includes worlds where the bucket should lose;",
            "- the reported finding can weaken, not only confirm, the B-series.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--route-trials", type=int, default=900)
    parser.add_argument("--null-trials", type=int, default=450)
    parser.add_argument("--sweep-route-trials", type=int, default=700)
    parser.add_argument("--sweep-null-trials", type=int, default=350)
    parser.add_argument("--main-bucket-mix", type=float, default=0.50)
    parser.add_argument("--mix-grid", type=float, nargs="+", default=[0.0, 0.25, 0.5, 0.75, 1.0])
    parser.add_argument("--lengths", type=str, default="60,90,140")
    parser.add_argument("--move-prob", type=float, default=0.72)
    parser.add_argument("--bucket-gate", type=float, default=0.14)
    parser.add_argument("--continuous-scale", type=float, default=0.13)
    parser.add_argument("--weak-min", type=float, default=0.035)
    parser.add_argument("--weak-max", type=float, default=0.105)
    parser.add_argument("--strong-min", type=float, default=0.175)
    parser.add_argument("--strong-max", type=float, default=0.265)
    parser.add_argument("--continuous-min", type=float, default=0.025)
    parser.add_argument("--continuous-max", type=float, default=0.265)
    parser.add_argument("--behavior-noise", type=float, default=0.070)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--class-threshold", type=float, default=0.25)
    parser.add_argument("--decision-margin", type=float, default=0.010)
    parser.add_argument("--false-action-margin", type=float, default=0.050)
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "reports",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_probe(args)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.report_dir / "b10_current_falsifier_polymath_probe.json"
    md_path = args.report_dir / "b10_current_falsifier_polymath_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
