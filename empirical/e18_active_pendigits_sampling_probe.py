"""E18 active PenDigits sampling probe.

E18 turns the temporal E17 recognition anchor into an active decision problem.
At an early trajectory prefix, the agent can either commit to its current digit
prediction or request more of the stroke. Requesting more has a cost, so the
right policy is not "always sample."

The probe separates two jobs:

    - predict graded sampling value;
    - admit a safe early commit while controlling false commits.

The external data are the UCI PenDigits trajectories already used by E17.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

import e17_temporal_pendigits_admission_probe as e17


MODEL_ORDER = ["scalar", "continuous_sampling", "temporal_commit_gate", "governed_sampling", "hybrid_full"]
DIGITS = list(range(10))


@dataclass(frozen=True)
class ActiveExample:
    split: str
    label: int
    early_pred: int
    full_pred: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_same_fraction: float
    gate_mean_confidence: float
    full_confidence: float
    local_evidence: float
    early_correct: float
    full_correct: float
    request_gain: float
    target_sampling_clean: float
    target_sampling_observed: float
    target_commit_clean: float
    target_commit_observed: float


@dataclass(frozen=True)
class RidgeModel:
    name: str
    feature_kind: str
    target_kind: str
    coef: list[float]
    mean: list[float]
    sd: list[float]
    feature_count: int
    expanded_count: int


def utility(correct: bool) -> float:
    return 1.0 if correct else -1.0


def collect_active_examples(
    split: str,
    x: np.ndarray,
    y: np.ndarray,
    classifiers: dict[int, e17.Classifier],
    early_points: int,
    gate_points: list[int],
    full_points: int,
    observation_cost: float,
    sampling_noise: float,
    commit_noise: float,
    rng: np.random.Generator,
) -> list[ActiveExample]:
    early_model = classifiers[early_points]
    full_model = classifiers[full_points]
    early_probs = e17.predict_proba(early_model, x)
    early_logits = e17.logits(early_model, x)
    full_probs = e17.predict_proba(full_model, x)
    early_pred = np.argmax(early_probs, axis=1)
    full_pred = np.argmax(full_probs, axis=1)

    sorted_probs = np.sort(early_probs, axis=1)
    top_prob = sorted_probs[:, -1]
    second_prob = sorted_probs[:, -2]
    margin = top_prob - second_prob
    entropy = -np.sum(early_probs * np.log(early_probs + 1e-12), axis=1) / math.log(10.0)
    top_logit = early_logits[np.arange(len(x)), early_pred]
    second_logit = np.partition(early_logits, -2, axis=1)[:, -2]
    logit_margin = top_logit - second_logit
    early_true_prob = early_probs[np.arange(len(x)), y]
    full_true_prob = full_probs[np.arange(len(x)), y]
    full_confidence = full_probs[np.arange(len(x)), full_pred]

    gate_preds = []
    gate_conf = []
    for points in gate_points:
        probs = e17.predict_proba(classifiers[points], x)
        gate_preds.append(np.argmax(probs, axis=1))
        gate_conf.append(probs[np.arange(len(x)), early_pred])
    gate_preds_arr = np.vstack(gate_preds).T
    gate_conf_arr = np.vstack(gate_conf).T
    gate_same_fraction = np.mean(gate_preds_arr == early_pred[:, None], axis=1)
    gate_mean_confidence = np.mean(gate_conf_arr, axis=1)
    gate_score = top_prob * gate_same_fraction * gate_mean_confidence

    early_correct = early_pred == y
    full_correct = full_pred == y
    # Use support for the true label, not only binary correctness, so the
    # request target changes when observation cost changes.
    commit_utility = early_true_prob
    request_utility = full_true_prob - observation_cost
    request_gain = request_utility - commit_utility
    commit_clean = (commit_utility >= request_utility).astype(float)

    # Smooth graded sampling target. It is high when the completed trajectory
    # improves true-label support enough to pay the observation cost.
    sampling_clean = np.clip(0.5 + 4.0 * request_gain, 0.0, 1.0)

    pred_bits = e17.one_hot(early_pred)
    continuous = np.hstack(
        [
            pred_bits,
            early_probs,
            top_prob[:, None],
            margin[:, None],
            entropy[:, None],
            logit_margin[:, None],
            e17.trajectory_features(x, early_points),
            e17.prefix(x, early_points),
        ]
    )
    local_evidence = top_prob * (0.30 + margin) * (1.0 - 0.40 * entropy)

    examples = []
    for i in range(len(x)):
        examples.append(
            ActiveExample(
                split=split,
                label=int(y[i]),
                early_pred=int(early_pred[i]),
                full_pred=int(full_pred[i]),
                scalar_score=float(top_prob[i]),
                continuous_features=[float(v) for v in continuous[i]],
                gate_score=float(gate_score[i]),
                gate_same_fraction=float(gate_same_fraction[i]),
                gate_mean_confidence=float(gate_mean_confidence[i]),
                full_confidence=float(full_confidence[i]),
                local_evidence=float(local_evidence[i]),
                early_correct=float(early_correct[i]),
                full_correct=float(full_correct[i]),
                request_gain=float(request_gain[i]),
                target_sampling_clean=float(sampling_clean[i]),
                target_sampling_observed=float(np.clip(sampling_clean[i] + rng.normal(scale=sampling_noise), 0.0, 1.0)),
                target_commit_clean=float(commit_clean[i]),
                target_commit_observed=float(np.clip(commit_clean[i] + rng.normal(scale=commit_noise), 0.0, 1.0)),
            )
        )
    return examples


def calibrate_commit_gate(examples: list[ActiveExample], alpha: float) -> float:
    request_needed = [ep.gate_score for ep in examples if ep.target_commit_clean < 0.5]
    if not request_needed:
        return float("inf")
    return float(np.quantile(np.asarray(request_needed, dtype=float), 1.0 - alpha, method="higher"))


def calibrate_bait(examples: list[ActiveExample], bait_quantile: float) -> float:
    request_needed = [ep.local_evidence for ep in examples if ep.target_commit_clean < 0.5]
    if not request_needed:
        return float("inf")
    return float(np.quantile(np.asarray(request_needed, dtype=float), bait_quantile, method="higher"))


def gate_bit(ep: ActiveExample, threshold: float) -> float:
    return 1.0 if ep.gate_score > threshold else 0.0


def digit_vector(digit: int) -> list[float]:
    return [1.0 if digit == item else 0.0 for item in DIGITS]


def feature_vector(ep: ActiveExample, kind: str, gate_threshold: float) -> list[float]:
    pred_bits = digit_vector(ep.early_pred)
    bit = gate_bit(ep, gate_threshold)
    pred_gate_bits = [bit * value for value in pred_bits]
    if kind == "scalar":
        return [ep.scalar_score]
    if kind == "continuous":
        return ep.continuous_features
    if kind == "gate":
        return pred_bits + [bit] + pred_gate_bits
    if kind == "governed":
        return ep.continuous_features + [bit] + pred_gate_bits
    if kind == "hybrid":
        return ep.continuous_features + [
            ep.gate_score,
            ep.gate_same_fraction,
            ep.gate_mean_confidence,
            ep.full_confidence,
            bit,
        ] + pred_gate_bits
    raise ValueError(f"unknown feature kind: {kind}")


def raw_matrix(examples: list[ActiveExample], kind: str, gate_threshold: float) -> np.ndarray:
    return np.asarray([feature_vector(ep, kind, gate_threshold) for ep in examples], dtype=float)


def target_vector(examples: list[ActiveExample], kind: str) -> np.ndarray:
    if kind == "sampling":
        return np.asarray([ep.target_sampling_observed for ep in examples], dtype=float)
    if kind == "commit":
        return np.asarray([ep.target_commit_observed for ep in examples], dtype=float)
    raise ValueError(f"unknown target kind: {kind}")


def fit_ridge(
    examples: list[ActiveExample],
    name: str,
    feature_kind: str,
    target_kind: str,
    gate_threshold: float,
    ridge: float,
) -> RidgeModel:
    x_raw = raw_matrix(examples, feature_kind, gate_threshold)
    phi, mean, sd = e17.expand_matrix(x_raw)
    y = target_vector(examples, target_kind)
    penalty = ridge * np.eye(phi.shape[1])
    penalty[0, 0] = 0.0
    lhs = phi.T @ phi + penalty
    rhs = phi.T @ y
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return RidgeModel(
        name=name,
        feature_kind=feature_kind,
        target_kind=target_kind,
        coef=[float(v) for v in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
        feature_count=int(x_raw.shape[1]),
        expanded_count=int(phi.shape[1]),
    )


def predict(model: RidgeModel, examples: list[ActiveExample], gate_threshold: float) -> np.ndarray:
    x_raw = raw_matrix(examples, model.feature_kind, gate_threshold)
    phi, _, _ = e17.expand_matrix(
        x_raw,
        np.asarray(model.mean, dtype=float),
        np.asarray(model.sd, dtype=float),
    )
    return np.clip(phi @ np.asarray(model.coef, dtype=float), 0.0, 1.0)


def classification_metrics(
    examples: list[ActiveExample],
    pred: np.ndarray,
    threshold: float,
    bait_threshold: float,
) -> dict[str, Any]:
    truth_commit = np.asarray([ep.target_commit_clean >= 0.5 for ep in examples], dtype=bool)
    calls_commit = pred >= threshold
    bait = np.asarray(
        [
            ep.target_commit_clean < 0.5 and ep.local_evidence >= bait_threshold
            for ep in examples
        ],
        dtype=bool,
    )
    return {
        "accuracy": float(np.mean(calls_commit == truth_commit)),
        "commit_detection": e17.mean_or_nan([float(v) for v in calls_commit[truth_commit]]),
        "false_commit": e17.mean_or_nan([float(v) for v in calls_commit[~truth_commit]]),
        "request_detection": e17.mean_or_nan([float(not v) for v in calls_commit[~truth_commit]]),
        "bait_false_commit": e17.mean_or_nan([float(v) for v in calls_commit[bait]]),
        "bait_count": int(bait.sum()),
        "commit_count": int(truth_commit.sum()),
        "request_count": int((~truth_commit).sum()),
    }


def summarize_examples(examples: list[ActiveExample]) -> dict[str, float]:
    commit = np.asarray([ep.target_commit_clean >= 0.5 for ep in examples], dtype=bool)
    return {
        "n": float(len(examples)),
        "early_accuracy": float(np.mean([ep.early_correct for ep in examples])),
        "full_accuracy": float(np.mean([ep.full_correct for ep in examples])),
        "commit_rate": float(commit.mean()),
        "request_rate": float((~commit).mean()),
        "mean_sampling": float(np.mean([ep.target_sampling_clean for ep in examples])),
        "mean_request_gain": float(np.mean([ep.request_gain for ep in examples])),
        "mean_gate_score": float(np.mean([ep.gate_score for ep in examples])),
        "mean_gate_same_fraction": float(np.mean([ep.gate_same_fraction for ep in examples])),
    }


def evaluate_models(
    train_examples: list[ActiveExample],
    calibration_examples: list[ActiveExample],
    test_examples: list[ActiveExample],
    alpha: float,
    bait_quantile: float,
    ridge: float,
    commit_threshold: float,
) -> dict[str, Any]:
    gate_threshold = calibrate_commit_gate(calibration_examples, alpha)
    bait_threshold = calibrate_bait(calibration_examples, bait_quantile)
    feature_kind = {
        "scalar": "scalar",
        "continuous_sampling": "continuous",
        "temporal_commit_gate": "gate",
        "governed_sampling": "governed",
        "hybrid_full": "hybrid",
    }
    y_sampling = target_vector(test_examples, "sampling")
    y_commit = target_vector(test_examples, "commit")
    overall: dict[str, Any] = {}
    models: dict[str, Any] = {}
    for name in MODEL_ORDER:
        sampling_model = fit_ridge(train_examples, name, feature_kind[name], "sampling", gate_threshold, ridge)
        commit_model = fit_ridge(train_examples, name, feature_kind[name], "commit", gate_threshold, ridge)
        sampling_pred = predict(sampling_model, test_examples, gate_threshold)
        commit_pred = predict(commit_model, test_examples, gate_threshold)
        overall[name] = {
            "sampling": {
                "rmse_observed": e17.rmse(y_sampling, sampling_pred),
                "r2_observed": e17.r2(y_sampling, sampling_pred),
            },
            "commit_regression": {
                "rmse_observed": e17.rmse(y_commit, commit_pred),
                "r2_observed": e17.r2(y_commit, commit_pred),
            },
            "commit_classification": classification_metrics(test_examples, commit_pred, commit_threshold, bait_threshold),
        }
        models[name] = {
            "sampling": {
                "feature_kind": sampling_model.feature_kind,
                "feature_count": sampling_model.feature_count,
                "expanded_count": sampling_model.expanded_count,
            },
            "commit": {
                "feature_kind": commit_model.feature_kind,
                "feature_count": commit_model.feature_count,
                "expanded_count": commit_model.expanded_count,
            },
        }
    return {
        "gate_threshold": gate_threshold,
        "bait_threshold": bait_threshold,
        "overall": overall,
        "models": models,
        "train_summary": summarize_examples(train_examples),
        "calibration_summary": summarize_examples(calibration_examples),
        "test_summary": summarize_examples(test_examples),
    }


def winner(overall: dict[str, Any], task: str) -> str:
    if task == "sampling":
        return min(MODEL_ORDER, key=lambda name: overall[name]["sampling"]["rmse_observed"])
    if task == "commit":
        return min(MODEL_ORDER, key=lambda name: overall[name]["commit_regression"]["rmse_observed"])
    raise ValueError(f"unknown task: {task}")


def decision_quantities(result: dict[str, Any]) -> dict[str, float]:
    overall = result["overall"]
    cont_cls = overall["continuous_sampling"]["commit_classification"]
    gate_cls = overall["temporal_commit_gate"]["commit_classification"]
    gov_cls = overall["governed_sampling"]["commit_classification"]
    hybrid_cls = overall["hybrid_full"]["commit_classification"]
    return {
        "continuous_sampling_rmse": overall["continuous_sampling"]["sampling"]["rmse_observed"],
        "gate_sampling_rmse": overall["temporal_commit_gate"]["sampling"]["rmse_observed"],
        "governed_sampling_rmse": overall["governed_sampling"]["sampling"]["rmse_observed"],
        "hybrid_sampling_rmse": overall["hybrid_full"]["sampling"]["rmse_observed"],
        "continuous_commit_rmse": overall["continuous_sampling"]["commit_regression"]["rmse_observed"],
        "gate_commit_rmse": overall["temporal_commit_gate"]["commit_regression"]["rmse_observed"],
        "governed_commit_rmse": overall["governed_sampling"]["commit_regression"]["rmse_observed"],
        "hybrid_commit_rmse": overall["hybrid_full"]["commit_regression"]["rmse_observed"],
        "continuous_false_commit": cont_cls["false_commit"],
        "gate_false_commit": gate_cls["false_commit"],
        "governed_false_commit": gov_cls["false_commit"],
        "hybrid_false_commit": hybrid_cls["false_commit"],
        "continuous_commit_detection": cont_cls["commit_detection"],
        "gate_commit_detection": gate_cls["commit_detection"],
        "governed_commit_detection": gov_cls["commit_detection"],
        "hybrid_commit_detection": hybrid_cls["commit_detection"],
        "continuous_request_detection": cont_cls["request_detection"],
        "gate_request_detection": gate_cls["request_detection"],
        "continuous_bait_false_commit": cont_cls["bait_false_commit"],
        "gate_bait_false_commit": gate_cls["bait_false_commit"],
    }


def classify_finding(args: argparse.Namespace, result: dict[str, Any]) -> str:
    dq = decision_quantities(result)
    continuous_fits_sampling = dq["continuous_sampling_rmse"] <= dq["gate_sampling_rmse"] + args.decision_margin
    gate_controls_commit = (
        dq["gate_false_commit"] + args.false_commit_margin < dq["continuous_false_commit"]
        and dq["gate_commit_detection"] >= args.commit_detection_floor
    )
    governed_controls = (
        dq["governed_false_commit"] + args.false_commit_margin < dq["continuous_false_commit"]
        and dq["governed_commit_detection"] >= args.commit_detection_floor
    )
    hybrid_needed = (
        dq["hybrid_sampling_rmse"] + args.decision_margin
        < min(dq["continuous_sampling_rmse"], dq["gate_sampling_rmse"])
        and dq["hybrid_commit_rmse"] + args.decision_margin
        < min(dq["continuous_commit_rmse"], dq["gate_commit_rmse"])
        and dq["hybrid_commit_detection"] >= args.commit_detection_floor
        and dq["hybrid_false_commit"] <= dq["continuous_false_commit"] + args.false_commit_margin
    )
    continuous_absorbs = (
        continuous_fits_sampling
        and dq["continuous_false_commit"] <= dq["gate_false_commit"] + args.false_commit_margin
        and dq["continuous_commit_detection"] >= args.commit_detection_floor
    )
    if continuous_absorbs:
        return "ACTIVE_EARLY_EVIDENCE_ABSORBS_SAMPLING_GATE"
    if continuous_fits_sampling and gate_controls_commit:
        return "SAMPLING_VALUE_FITS_EARLY_FIELD_BUT_TEMPORAL_GATE_CONTROLS_COMMIT"
    if hybrid_needed or governed_controls:
        return "ACTIVE_HYBRID_SAMPLING_GATE_NEEDED"
    return "ACTIVE_PENDIGITS_SAMPLING_INCONCLUSIVE"


def prepare(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, dict[int, e17.Classifier]]:
    x_train, y_train, x_cal, y_cal, x_test, y_test = e17.prepare_splits(args)
    needed = sorted(set([args.early_points, args.full_points] + args.gate_points))
    classifiers = {points: e17.fit_classifier(x_train, y_train, points, args.classifier_ridge) for points in needed}
    return x_train, y_train, x_cal, y_cal, x_test, y_test, classifiers


def build_examples(
    args: argparse.Namespace,
    classifiers: dict[int, e17.Classifier],
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_cal: np.ndarray,
    y_cal: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
) -> tuple[list[ActiveExample], list[ActiveExample], list[ActiveExample]]:
    rng = np.random.default_rng(args.seed + 1818)
    train = collect_active_examples(
        "train",
        x_train,
        y_train,
        classifiers,
        args.early_points,
        args.gate_points,
        args.full_points,
        args.observation_cost,
        args.sampling_noise,
        args.commit_noise,
        rng,
    )
    cal = collect_active_examples(
        "calibration",
        x_cal,
        y_cal,
        classifiers,
        args.early_points,
        args.gate_points,
        args.full_points,
        args.observation_cost,
        args.sampling_noise,
        args.commit_noise,
        rng,
    )
    test = collect_active_examples(
        "test",
        x_test,
        y_test,
        classifiers,
        args.early_points,
        args.gate_points,
        args.full_points,
        args.observation_cost,
        args.sampling_noise,
        args.commit_noise,
        rng,
    )
    return train, cal, test


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    x_train, y_train, x_cal, y_cal, x_test, y_test, classifiers = prepare(args)
    train, cal, test = build_examples(args, classifiers, x_train, y_train, x_cal, y_cal, x_test, y_test)
    main = evaluate_models(
        train,
        cal,
        test,
        args.alpha,
        args.bait_quantile,
        args.ridge,
        args.commit_threshold,
    )

    cost_rows = []
    for cost in args.cost_grid:
        local_args = argparse.Namespace(**vars(args))
        local_args.observation_cost = cost
        tr, ca, te = build_examples(local_args, classifiers, x_train, y_train, x_cal, y_cal, x_test, y_test)
        row = evaluate_models(tr, ca, te, args.alpha, args.bait_quantile, args.ridge, args.commit_threshold)
        dq = decision_quantities(row)
        cost_rows.append(
            {
                "observation_cost": cost,
                "commit_rate": row["test_summary"]["commit_rate"],
                "request_rate": row["test_summary"]["request_rate"],
                "sampling_winner": winner(row["overall"], "sampling"),
                "commit_winner": winner(row["overall"], "commit"),
                "continuous_sampling_rmse": dq["continuous_sampling_rmse"],
                "gate_sampling_rmse": dq["gate_sampling_rmse"],
                "continuous_false_commit": dq["continuous_false_commit"],
                "gate_false_commit": dq["gate_false_commit"],
                "continuous_commit_detection": dq["continuous_commit_detection"],
                "gate_commit_detection": dq["gate_commit_detection"],
                "continuous_bait_false_commit": dq["continuous_bait_false_commit"],
                "gate_bait_false_commit": dq["gate_bait_false_commit"],
            }
        )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "UCI Pen-Based Recognition of Handwritten Digits",
            "url": e17.UCI_DATASET_URL,
            "raw_files": e17.DATA_URLS,
            "features": 16,
            "points": 8,
            "classes": 10,
        },
        "config": {
            "seed": args.seed,
            "calibration_fraction": args.calibration_fraction,
            "early_points": args.early_points,
            "gate_points": args.gate_points,
            "full_points": args.full_points,
            "observation_cost": args.observation_cost,
            "cost_grid": args.cost_grid,
            "alpha": args.alpha,
            "bait_quantile": args.bait_quantile,
            "classifier_ridge": args.classifier_ridge,
            "ridge": args.ridge,
            "sampling_noise": args.sampling_noise,
            "commit_noise": args.commit_noise,
            "commit_threshold": args.commit_threshold,
            "train_n": len(x_train),
            "calibration_n": len(x_cal),
            "test_n": len(x_test),
        },
        "main": main,
        "decision_quantities": decision_quantities(main),
        "cost_sweep": cost_rows,
    }
    result["finding"] = classify_finding(args, main)
    return result


def fmt(value: float) -> str:
    if value != value:
        return "nan"
    return f"{value:.3f}"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def write_report(path: Path, result: dict[str, Any]) -> None:
    config = result["config"]
    main = result["main"]
    dq = result["decision_quantities"]
    overall = main["overall"]

    model_rows = []
    for name in MODEL_ORDER:
        cls = overall[name]["commit_classification"]
        model_rows.append(
            [
                name,
                fmt(overall[name]["sampling"]["rmse_observed"]),
                fmt(overall[name]["sampling"]["r2_observed"]),
                fmt(overall[name]["commit_regression"]["rmse_observed"]),
                fmt(cls["accuracy"]),
                fmt(cls["commit_detection"]),
                fmt(cls["false_commit"]),
                fmt(cls["request_detection"]),
                fmt(cls["bait_false_commit"]),
                str(cls["bait_count"]),
            ]
        )

    summary_rows = []
    for key in ["train_summary", "calibration_summary", "test_summary"]:
        s = main[key]
        summary_rows.append(
            [
                key.replace("_summary", ""),
                str(int(s["n"])),
                fmt(s["early_accuracy"]),
                fmt(s["full_accuracy"]),
                fmt(s["commit_rate"]),
                fmt(s["request_rate"]),
                fmt(s["mean_sampling"]),
                fmt(s["mean_request_gain"]),
                fmt(s["mean_gate_score"]),
            ]
        )

    cost_rows = []
    for row in result["cost_sweep"]:
        cost_rows.append(
            [
                fmt(row["observation_cost"]),
                fmt(row["commit_rate"]),
                fmt(row["request_rate"]),
                row["sampling_winner"],
                row["commit_winner"],
                fmt(row["continuous_sampling_rmse"]),
                fmt(row["gate_sampling_rmse"]),
                fmt(row["continuous_false_commit"]),
                fmt(row["gate_false_commit"]),
                fmt(row["continuous_commit_detection"]),
                fmt(row["gate_commit_detection"]),
                fmt(row["continuous_bait_false_commit"]),
                fmt(row["gate_bait_false_commit"]),
            ]
        )

    lines = [
        "# E18 Active PenDigits Sampling Probe",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- dataset: `{result['dataset']['name']}`",
        f"- dataset URL: `{result['dataset']['url']}`",
        f"- train/calibration/test: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
        f"- early/gate/full points: `{config['early_points']}` / `{config['gate_points']}` / `{config['full_points']}`",
        f"- observation cost: `{config['observation_cost']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E18 turns E17 into an active decision problem. At an early trajectory",
        "prefix, the agent can commit now or pay to request more of the stroke.",
        "The probe separates graded sampling value from safe commit admission.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous sampling RMSE", fmt(dq["continuous_sampling_rmse"])],
                ["gate sampling RMSE", fmt(dq["gate_sampling_rmse"])],
                ["governed sampling RMSE", fmt(dq["governed_sampling_rmse"])],
                ["hybrid sampling RMSE", fmt(dq["hybrid_sampling_rmse"])],
                ["continuous commit RMSE", fmt(dq["continuous_commit_rmse"])],
                ["gate commit RMSE", fmt(dq["gate_commit_rmse"])],
                ["governed commit RMSE", fmt(dq["governed_commit_rmse"])],
                ["hybrid commit RMSE", fmt(dq["hybrid_commit_rmse"])],
                ["continuous false commit", fmt(dq["continuous_false_commit"])],
                ["gate false commit", fmt(dq["gate_false_commit"])],
                ["governed false commit", fmt(dq["governed_false_commit"])],
                ["continuous commit detection", fmt(dq["continuous_commit_detection"])],
                ["gate commit detection", fmt(dq["gate_commit_detection"])],
                ["continuous request detection", fmt(dq["continuous_request_detection"])],
                ["gate request detection", fmt(dq["gate_request_detection"])],
                ["continuous bait false commit", fmt(dq["continuous_bait_false_commit"])],
                ["gate bait false commit", fmt(dq["gate_bait_false_commit"])],
                ["gate threshold", fmt(main["gate_threshold"])],
                ["bait threshold", fmt(main["bait_threshold"])],
            ],
        ),
        "",
        "## Split Summary",
        "",
        md_table(
            [
                "split",
                "n",
                "early acc",
                "full acc",
                "commit rate",
                "request rate",
                "sampling",
                "request gain",
                "gate score",
            ],
            summary_rows,
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "sampling RMSE",
                "sampling R2",
                "commit RMSE",
                "commit acc",
                "commit detect",
                "false commit",
                "request detect",
                "bait false",
                "bait n",
            ],
            model_rows,
        ),
        "",
        "## Cost Sweep",
        "",
        md_table(
            [
                "cost",
                "commit rate",
                "request rate",
                "sampling winner",
                "commit winner",
                "cont sampling",
                "gate sampling",
                "cont false commit",
                "gate false commit",
                "cont commit detect",
                "gate commit detect",
                "cont bait false",
                "gate bait false",
            ],
            cost_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    if result["finding"] == "SAMPLING_VALUE_FITS_EARLY_FIELD_BUT_TEMPORAL_GATE_CONTROLS_COMMIT":
        lines.extend(
            [
                "Early continuous evidence fits the graded value of sampling, while",
                "the temporal gate controls false commits. This supports the active",
                "boundary split: value fields decide how much more evidence is",
                "worth, but commit admission requires persistence.",
            ]
        )
    elif result["finding"] == "ACTIVE_EARLY_EVIDENCE_ABSORBS_SAMPLING_GATE":
        lines.extend(
            [
                "Early evidence absorbs both sampling value and safe commit",
                "admission. This would extend E16's negative result to active",
                "sampling in this configuration.",
            ]
        )
    elif result["finding"] == "ACTIVE_HYBRID_SAMPLING_GATE_NEEDED":
        lines.extend(
            [
                "The governed/hybrid active policy is needed. The pure gate does not",
                "win alone, but persistence improves commit control when combined",
                "with early sampling evidence.",
            ]
        )
    else:
        lines.extend(
            [
                "The active PenDigits sampling proxy is inconclusive under this",
                "configuration. Sampling value and commit admission may not be",
                "separated cleanly enough.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external pen-trajectory digit data;",
            "- early evidence uses only the first trajectory points;",
            "- requesting more has an explicit cost, so the target is not always-sample;",
            "- the gate is label-free and uses middle trajectory persistence;",
            "- the commit target is evaluated from early utility versus full-trajectory utility;",
            "- calibration thresholds are estimated on calibration examples and scored on the held-out test file;",
            "- the cost sweep tests whether the active result depends on the sampling cost.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data" / "pendigits")
    parser.add_argument("--calibration-fraction", type=float, default=0.25)
    parser.add_argument("--early-points", type=int, default=2)
    parser.add_argument("--gate-points", type=int, nargs="+", default=[4, 5, 6])
    parser.add_argument("--full-points", type=int, default=8)
    parser.add_argument("--observation-cost", type=float, default=0.025)
    parser.add_argument("--cost-grid", type=float, nargs="+", default=[0.00, 0.01, 0.025, 0.05, 0.10])
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--bait-quantile", type=float, default=0.70)
    parser.add_argument("--classifier-ridge", type=float, default=1e-2)
    parser.add_argument("--ridge", type=float, default=5e-3)
    parser.add_argument("--sampling-noise", type=float, default=0.015)
    parser.add_argument("--commit-noise", type=float, default=0.020)
    parser.add_argument("--commit-threshold", type=float, default=0.50)
    parser.add_argument("--decision-margin", type=float, default=0.005)
    parser.add_argument("--false-commit-margin", type=float, default=0.030)
    parser.add_argument("--commit-detection-floor", type=float, default=0.650)
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
    json_path = args.report_dir / "e18_active_pendigits_sampling_probe.json"
    md_path = args.report_dir / "e18_active_pendigits_sampling_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
