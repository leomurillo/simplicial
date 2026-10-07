"""E17 temporal PenDigits admission probe.

E17 follows the negative E16 static-image anchor with a temporal external
proxy. It uses the UCI Pen-Based Recognition of Handwritten Digits dataset,
where each example is a trajectory of eight (x, y) points.

The experiment separates three windows:

    - early prefix points define the continuous evidence field;
    - middle prefix points define a label-free persistence gate;
    - late prefix points define the durable admission target.

The question is whether early-stroke continuous confidence absorbs admission,
as in E16, or whether later-stroke persistence becomes useful once evidence is
sequential rather than static.
"""

from __future__ import annotations

import argparse
import json
import math
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


DATA_URLS = {
    "pendigits.tra": "https://archive.ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tra",
    "pendigits.tes": "https://archive.ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tes",
}
UCI_DATASET_URL = "https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits"
MODEL_ORDER = ["scalar", "continuous_early", "temporal_gate", "governed_temporal", "hybrid_full"]
DIGITS = list(range(10))


@dataclass(frozen=True)
class Classifier:
    prefix_points: int
    coef: list[list[float]]
    mean: list[float]
    sd: list[float]


@dataclass(frozen=True)
class Example:
    split: str
    label: int
    early_pred: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_same_fraction: float
    gate_mean_confidence: float
    audit_true_fraction: float
    local_evidence: float
    target_intensity_clean: float
    target_intensity_observed: float
    target_admission_clean: float
    target_admission_observed: float


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


def download_dataset(data_dir: Path) -> dict[str, Path]:
    data_dir.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    for name, url in DATA_URLS.items():
        path = data_dir / name
        if not path.exists():
            urllib.request.urlretrieve(url, path)
        paths[name] = path
    return paths


def load_pendigits(path: Path) -> tuple[np.ndarray, np.ndarray]:
    rows = []
    labels = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        values = [int(item) for item in line.split(",")]
        rows.append(values[:-1])
        labels.append(values[-1])
    x = np.asarray(rows, dtype=float) / 100.0
    y = np.asarray(labels, dtype=int)
    return x, y


def prefix(x: np.ndarray, points: int) -> np.ndarray:
    return x[:, : 2 * points]


def one_hot(y: np.ndarray, classes: int = 10) -> np.ndarray:
    out = np.zeros((len(y), classes), dtype=float)
    out[np.arange(len(y)), y] = 1.0
    return out


def fit_classifier(x: np.ndarray, y: np.ndarray, points: int, ridge: float) -> Classifier:
    xp = prefix(x, points)
    mean = xp.mean(axis=0)
    sd = xp.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (xp - mean) / sd
    design = np.hstack([np.ones((z.shape[0], 1)), z])
    target = one_hot(y)
    penalty = ridge * np.eye(design.shape[1])
    penalty[0, 0] = 0.0
    lhs = design.T @ design + penalty
    rhs = design.T @ target
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return Classifier(
        prefix_points=points,
        coef=[[float(v) for v in row] for row in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
    )


def logits(model: Classifier, x: np.ndarray) -> np.ndarray:
    xp = prefix(x, model.prefix_points)
    mean = np.asarray(model.mean, dtype=float)
    sd = np.asarray(model.sd, dtype=float)
    coef = np.asarray(model.coef, dtype=float)
    z = (xp - mean) / sd
    design = np.hstack([np.ones((z.shape[0], 1)), z])
    return design @ coef


def softmax(values: np.ndarray) -> np.ndarray:
    centered = values - values.max(axis=1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=1, keepdims=True)


def predict_proba(model: Classifier, x: np.ndarray) -> np.ndarray:
    return softmax(logits(model, x))


def trajectory_features(x: np.ndarray, points: int) -> np.ndarray:
    coords = prefix(x, points).reshape((-1, points, 2))
    feats = []
    for row in coords:
        diffs = np.diff(row, axis=0)
        lengths = np.sqrt((diffs * diffs).sum(axis=1))
        total_length = float(lengths.sum())
        displacement = float(np.linalg.norm(row[-1] - row[0]))
        directness = displacement / (total_length + 1e-8)
        bbox = row.max(axis=0) - row.min(axis=0)
        centroid = row.mean(axis=0)
        angle = math.atan2(float(row[-1, 1] - row[0, 1]), float(row[-1, 0] - row[0, 0]) + 1e-8)
        if len(diffs) > 1:
            unit = diffs / (lengths[:, None] + 1e-8)
            curvature = float(np.abs(np.diff(np.arctan2(unit[:, 1], unit[:, 0]))).sum())
            length_cv = float(lengths.std() / (lengths.mean() + 1e-8))
        else:
            curvature = 0.0
            length_cv = 0.0
        feats.append(
            [
                total_length,
                displacement,
                directness,
                float(bbox[0]),
                float(bbox[1]),
                float(centroid[0]),
                float(centroid[1]),
                math.sin(angle),
                math.cos(angle),
                curvature,
                length_cv,
            ]
        )
    return np.asarray(feats, dtype=float)


def collect_examples(
    split: str,
    x: np.ndarray,
    y: np.ndarray,
    classifiers: dict[int, Classifier],
    early_points: int,
    gate_points: list[int],
    audit_points: list[int],
    audit_threshold: float,
    intensity_noise: float,
    admission_noise: float,
    rng: np.random.Generator,
) -> list[Example]:
    early_model = classifiers[early_points]
    early_probs = predict_proba(early_model, x)
    early_logits = logits(early_model, x)
    early_pred = np.argmax(early_probs, axis=1)
    sorted_probs = np.sort(early_probs, axis=1)
    top_prob = sorted_probs[:, -1]
    second_prob = sorted_probs[:, -2]
    margin = top_prob - second_prob
    entropy = -np.sum(early_probs * np.log(early_probs + 1e-12), axis=1) / math.log(10.0)
    true_prob = early_probs[np.arange(len(x)), y]
    top_logit = early_logits[np.arange(len(x)), early_pred]
    second_logit = np.partition(early_logits, -2, axis=1)[:, -2]
    logit_margin = top_logit - second_logit

    gate_preds = []
    gate_conf = []
    for points in gate_points:
        probs = predict_proba(classifiers[points], x)
        gate_preds.append(np.argmax(probs, axis=1))
        gate_conf.append(probs[np.arange(len(x)), early_pred])
    gate_preds_arr = np.vstack(gate_preds).T
    gate_conf_arr = np.vstack(gate_conf).T
    gate_same_fraction = np.mean(gate_preds_arr == early_pred[:, None], axis=1)
    gate_mean_confidence = np.mean(gate_conf_arr, axis=1)
    gate_score = top_prob * gate_same_fraction * gate_mean_confidence

    audit_true = []
    for points in audit_points:
        probs = predict_proba(classifiers[points], x)
        audit_true.append(np.argmax(probs, axis=1) == y)
    audit_true_arr = np.vstack(audit_true).T
    audit_true_fraction = np.mean(audit_true_arr, axis=1)
    admission_clean = ((early_pred == y) & (audit_true_fraction >= audit_threshold)).astype(float)

    early_bits = one_hot(early_pred)
    continuous = np.hstack(
        [
            early_bits,
            early_probs,
            top_prob[:, None],
            margin[:, None],
            entropy[:, None],
            logit_margin[:, None],
            trajectory_features(x, early_points),
            prefix(x, early_points),
        ]
    )
    local_evidence = top_prob * (0.30 + margin) * (1.0 - 0.40 * entropy)

    examples = []
    for i in range(len(x)):
        examples.append(
            Example(
                split=split,
                label=int(y[i]),
                early_pred=int(early_pred[i]),
                scalar_score=float(top_prob[i]),
                continuous_features=[float(v) for v in continuous[i]],
                gate_score=float(gate_score[i]),
                gate_same_fraction=float(gate_same_fraction[i]),
                gate_mean_confidence=float(gate_mean_confidence[i]),
                audit_true_fraction=float(audit_true_fraction[i]),
                local_evidence=float(local_evidence[i]),
                target_intensity_clean=float(top_prob[i]),
                target_intensity_observed=float(np.clip(top_prob[i] + rng.normal(scale=intensity_noise), 0.0, 1.0)),
                target_admission_clean=float(admission_clean[i]),
                target_admission_observed=float(
                    np.clip(float(admission_clean[i]) + rng.normal(scale=admission_noise), 0.0, 1.0)
                ),
            )
        )
    return examples


def calibrate_gate(examples: list[Example], alpha: float) -> float:
    nonadmitted = [ep.gate_score for ep in examples if ep.target_admission_clean < 0.5]
    if not nonadmitted:
        return float("inf")
    return float(np.quantile(np.asarray(nonadmitted, dtype=float), 1.0 - alpha, method="higher"))


def calibrate_bait(examples: list[Example], bait_quantile: float) -> float:
    nonadmitted = [ep.local_evidence for ep in examples if ep.target_admission_clean < 0.5]
    if not nonadmitted:
        return float("inf")
    return float(np.quantile(np.asarray(nonadmitted, dtype=float), bait_quantile, method="higher"))


def gate_bit(ep: Example, threshold: float) -> float:
    return 1.0 if ep.gate_score > threshold else 0.0


def digit_vector(digit: int) -> list[float]:
    return [1.0 if digit == item else 0.0 for item in DIGITS]


def feature_vector(ep: Example, kind: str, gate_threshold: float) -> list[float]:
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
            bit,
        ] + pred_gate_bits
    raise ValueError(f"unknown feature kind: {kind}")


def raw_matrix(examples: list[Example], kind: str, gate_threshold: float) -> np.ndarray:
    return np.asarray([feature_vector(ep, kind, gate_threshold) for ep in examples], dtype=float)


def target_vector(examples: list[Example], kind: str) -> np.ndarray:
    if kind == "intensity":
        return np.asarray([ep.target_intensity_observed for ep in examples], dtype=float)
    if kind == "admission":
        return np.asarray([ep.target_admission_observed for ep in examples], dtype=float)
    raise ValueError(f"unknown target kind: {kind}")


def expand_matrix(
    x: np.ndarray,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    parts = [np.ones((z.shape[0], 1)), z, z * z]
    interactions = []
    for i in range(z.shape[1]):
        for j in range(i + 1, z.shape[1]):
            interactions.append((z[:, i] * z[:, j])[:, None])
    if interactions:
        parts.extend(interactions)
    return np.hstack(parts), mean, sd


def fit_ridge(
    examples: list[Example],
    name: str,
    feature_kind: str,
    target_kind: str,
    gate_threshold: float,
    ridge: float,
) -> RidgeModel:
    x_raw = raw_matrix(examples, feature_kind, gate_threshold)
    phi, mean, sd = expand_matrix(x_raw)
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


def predict(model: RidgeModel, examples: list[Example], gate_threshold: float) -> np.ndarray:
    x_raw = raw_matrix(examples, model.feature_kind, gate_threshold)
    phi, _, _ = expand_matrix(
        x_raw,
        np.asarray(model.mean, dtype=float),
        np.asarray(model.sd, dtype=float),
    )
    return np.clip(phi @ np.asarray(model.coef, dtype=float), 0.0, 1.0)


def rmse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y - pred) ** 2)))


def r2(y: np.ndarray, pred: np.ndarray) -> float:
    denom = float(np.sum((y - y.mean()) ** 2))
    if denom <= 1e-12:
        return float("nan")
    return float(1.0 - np.sum((y - pred) ** 2) / denom)


def mean_or_nan(values: list[float]) -> float:
    if not values:
        return float("nan")
    return float(np.mean(np.asarray(values, dtype=float)))


def classification_metrics(
    examples: list[Example],
    pred: np.ndarray,
    threshold: float,
    bait_threshold: float,
) -> dict[str, Any]:
    truth = np.asarray([ep.target_admission_clean >= 0.5 for ep in examples], dtype=bool)
    calls = pred >= threshold
    bait = np.asarray(
        [
            ep.target_admission_clean < 0.5 and ep.local_evidence >= bait_threshold
            for ep in examples
        ],
        dtype=bool,
    )
    metrics: dict[str, Any] = {
        "accuracy": float(np.mean(calls == truth)),
        "admission_detection": mean_or_nan([float(v) for v in calls[truth]]),
        "nonadmitted_false_admission": mean_or_nan([float(v) for v in calls[~truth]]),
        "bait_false_admission": mean_or_nan([float(v) for v in calls[bait]]),
        "bait_count": int(bait.sum()),
        "durable_count": int(truth.sum()),
        "nonadmitted_count": int((~truth).sum()),
        "by_digit": {},
    }
    for digit in DIGITS:
        mask = np.asarray([ep.label == digit for ep in examples], dtype=bool)
        admitted = mask & truth
        nonadmitted = mask & ~truth
        digit_bait = mask & bait
        metrics["by_digit"][str(digit)] = {
            "detection": mean_or_nan([float(v) for v in calls[admitted]]),
            "false_admission": mean_or_nan([float(v) for v in calls[nonadmitted]]),
            "bait_false_admission": mean_or_nan([float(v) for v in calls[digit_bait]]),
            "n": int(mask.sum()),
        }
    return metrics


def summarize_examples(examples: list[Example]) -> dict[str, float]:
    truth = np.asarray([ep.target_admission_clean >= 0.5 for ep in examples], dtype=bool)
    early_correct = np.asarray([ep.early_pred == ep.label for ep in examples], dtype=bool)
    return {
        "n": float(len(examples)),
        "early_accuracy": float(early_correct.mean()),
        "durable_rate": float(truth.mean()),
        "mean_intensity": float(np.mean([ep.target_intensity_clean for ep in examples])),
        "mean_gate_score": float(np.mean([ep.gate_score for ep in examples])),
        "mean_gate_same_fraction": float(np.mean([ep.gate_same_fraction for ep in examples])),
        "mean_audit_true_fraction": float(np.mean([ep.audit_true_fraction for ep in examples])),
        "mean_local_evidence": float(np.mean([ep.local_evidence for ep in examples])),
    }


def digit_summary(examples: list[Example], bait_threshold: float) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for digit in DIGITS:
        rows = [ep for ep in examples if ep.label == digit]
        if not rows:
            continue
        truth = [ep.target_admission_clean >= 0.5 for ep in rows]
        correct = [ep.early_pred == ep.label for ep in rows]
        bait = [ep.target_admission_clean < 0.5 and ep.local_evidence >= bait_threshold for ep in rows]
        out[str(digit)] = {
            "n": float(len(rows)),
            "early_accuracy": float(np.mean(correct)),
            "durable_rate": float(np.mean(truth)),
            "bait_rate": float(np.mean(bait)),
            "mean_intensity": float(np.mean([ep.target_intensity_clean for ep in rows])),
            "mean_gate_score": float(np.mean([ep.gate_score for ep in rows])),
            "mean_audit_true_fraction": float(np.mean([ep.audit_true_fraction for ep in rows])),
        }
    return out


def evaluate_models(
    train_examples: list[Example],
    calibration_examples: list[Example],
    test_examples: list[Example],
    alpha: float,
    bait_quantile: float,
    ridge: float,
    admission_threshold: float,
) -> dict[str, Any]:
    gate_threshold = calibrate_gate(calibration_examples, alpha)
    bait_threshold = calibrate_bait(calibration_examples, bait_quantile)
    feature_kind = {
        "scalar": "scalar",
        "continuous_early": "continuous",
        "temporal_gate": "gate",
        "governed_temporal": "governed",
        "hybrid_full": "hybrid",
    }
    y_intensity = target_vector(test_examples, "intensity")
    y_admission = target_vector(test_examples, "admission")
    overall: dict[str, Any] = {}
    models: dict[str, Any] = {}
    for name in MODEL_ORDER:
        intensity_model = fit_ridge(train_examples, name, feature_kind[name], "intensity", gate_threshold, ridge)
        admission_model = fit_ridge(train_examples, name, feature_kind[name], "admission", gate_threshold, ridge)
        intensity_pred = predict(intensity_model, test_examples, gate_threshold)
        admission_pred = predict(admission_model, test_examples, gate_threshold)
        overall[name] = {
            "intensity": {
                "rmse_observed": rmse(y_intensity, intensity_pred),
                "r2_observed": r2(y_intensity, intensity_pred),
            },
            "admission_regression": {
                "rmse_observed": rmse(y_admission, admission_pred),
                "r2_observed": r2(y_admission, admission_pred),
            },
            "admission_classification": classification_metrics(
                test_examples,
                admission_pred,
                admission_threshold,
                bait_threshold,
            ),
        }
        models[name] = {
            "intensity": {
                "feature_kind": intensity_model.feature_kind,
                "feature_count": intensity_model.feature_count,
                "expanded_count": intensity_model.expanded_count,
            },
            "admission": {
                "feature_kind": admission_model.feature_kind,
                "feature_count": admission_model.feature_count,
                "expanded_count": admission_model.expanded_count,
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
        "test_digit_summary": digit_summary(test_examples, bait_threshold),
    }


def winner(overall: dict[str, Any], task: str) -> str:
    if task == "intensity":
        return min(MODEL_ORDER, key=lambda name: overall[name]["intensity"]["rmse_observed"])
    if task == "admission":
        return min(MODEL_ORDER, key=lambda name: overall[name]["admission_regression"]["rmse_observed"])
    raise ValueError(f"unknown task: {task}")


def decision_quantities(result: dict[str, Any]) -> dict[str, float]:
    overall = result["overall"]
    cont_cls = overall["continuous_early"]["admission_classification"]
    gate_cls = overall["temporal_gate"]["admission_classification"]
    gov_cls = overall["governed_temporal"]["admission_classification"]
    hybrid_cls = overall["hybrid_full"]["admission_classification"]
    return {
        "continuous_intensity_rmse": overall["continuous_early"]["intensity"]["rmse_observed"],
        "gate_intensity_rmse": overall["temporal_gate"]["intensity"]["rmse_observed"],
        "governed_intensity_rmse": overall["governed_temporal"]["intensity"]["rmse_observed"],
        "hybrid_intensity_rmse": overall["hybrid_full"]["intensity"]["rmse_observed"],
        "continuous_admission_rmse": overall["continuous_early"]["admission_regression"]["rmse_observed"],
        "gate_admission_rmse": overall["temporal_gate"]["admission_regression"]["rmse_observed"],
        "governed_admission_rmse": overall["governed_temporal"]["admission_regression"]["rmse_observed"],
        "hybrid_admission_rmse": overall["hybrid_full"]["admission_regression"]["rmse_observed"],
        "continuous_false_admission": cont_cls["nonadmitted_false_admission"],
        "gate_false_admission": gate_cls["nonadmitted_false_admission"],
        "governed_false_admission": gov_cls["nonadmitted_false_admission"],
        "hybrid_false_admission": hybrid_cls["nonadmitted_false_admission"],
        "continuous_detection": cont_cls["admission_detection"],
        "gate_detection": gate_cls["admission_detection"],
        "governed_detection": gov_cls["admission_detection"],
        "hybrid_detection": hybrid_cls["admission_detection"],
        "continuous_bait_false": cont_cls["bait_false_admission"],
        "gate_bait_false": gate_cls["bait_false_admission"],
        "governed_bait_false": gov_cls["bait_false_admission"],
        "hybrid_bait_false": hybrid_cls["bait_false_admission"],
    }


def classify_finding(args: argparse.Namespace, result: dict[str, Any]) -> str:
    dq = decision_quantities(result)
    cont_fits_intensity = dq["continuous_intensity_rmse"] <= dq["gate_intensity_rmse"] + args.decision_margin
    gate_controls = (
        dq["gate_false_admission"] + args.false_admission_margin < dq["continuous_false_admission"]
        and dq["gate_detection"] >= args.detection_floor
    )
    governed_controls = (
        dq["governed_false_admission"] + args.false_admission_margin < dq["continuous_false_admission"]
        and dq["governed_detection"] >= args.detection_floor
    )
    continuous_absorbs = (
        cont_fits_intensity
        and dq["continuous_false_admission"] <= dq["gate_false_admission"] + args.false_admission_margin
        and dq["continuous_detection"] >= args.detection_floor
    )
    if continuous_absorbs:
        return "EARLY_TEMPORAL_EVIDENCE_ABSORBS_PERSISTENCE"
    if cont_fits_intensity and gate_controls:
        return "TEMPORAL_PERSISTENCE_GOVERNS_ADMISSION"
    if governed_controls:
        return "TEMPORAL_HYBRID_EVIDENCE_PERSISTENCE_NEEDED"
    return "TEMPORAL_PENDIGITS_ANCHOR_INCONCLUSIVE"


def prepare_splits(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    paths = download_dataset(args.data_dir)
    x_full_train, y_full_train = load_pendigits(paths["pendigits.tra"])
    x_test, y_test = load_pendigits(paths["pendigits.tes"])
    rng = np.random.default_rng(args.seed)
    perm = rng.permutation(len(x_full_train))
    cal_count = int(round(args.calibration_fraction * len(x_full_train)))
    cal_idx = perm[:cal_count]
    train_idx = perm[cal_count:]
    return (
        x_full_train[train_idx],
        y_full_train[train_idx],
        x_full_train[cal_idx],
        y_full_train[cal_idx],
        x_test,
        y_test,
    )


def build_classifiers(x_train: np.ndarray, y_train: np.ndarray, args: argparse.Namespace) -> dict[int, Classifier]:
    needed = sorted(set([args.early_points] + args.gate_points + args.audit_points))
    return {points: fit_classifier(x_train, y_train, points, args.classifier_ridge) for points in needed}


def build_examples(
    args: argparse.Namespace,
    classifiers: dict[int, Classifier],
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_cal: np.ndarray,
    y_cal: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    audit_threshold: float,
) -> tuple[list[Example], list[Example], list[Example]]:
    rng = np.random.default_rng(args.seed + int(round(1000 * audit_threshold)) + 17)
    train_examples = collect_examples(
        "train",
        x_train,
        y_train,
        classifiers,
        args.early_points,
        args.gate_points,
        args.audit_points,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    cal_examples = collect_examples(
        "calibration",
        x_cal,
        y_cal,
        classifiers,
        args.early_points,
        args.gate_points,
        args.audit_points,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    test_examples = collect_examples(
        "test",
        x_test,
        y_test,
        classifiers,
        args.early_points,
        args.gate_points,
        args.audit_points,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    return train_examples, cal_examples, test_examples


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    x_train, y_train, x_cal, y_cal, x_test, y_test = prepare_splits(args)
    classifiers = build_classifiers(x_train, y_train, args)

    train_examples, cal_examples, test_examples = build_examples(
        args,
        classifiers,
        x_train,
        y_train,
        x_cal,
        y_cal,
        x_test,
        y_test,
        args.audit_threshold,
    )
    main = evaluate_models(
        train_examples,
        cal_examples,
        test_examples,
        args.alpha,
        args.bait_quantile,
        args.ridge,
        args.admission_threshold,
    )

    sweep = []
    for early_points in args.early_grid:
        local_args = argparse.Namespace(**vars(args))
        local_args.early_points = early_points
        local_args.gate_points = [p for p in args.gate_points if p > early_points]
        local_args.audit_points = [p for p in args.audit_points if p > early_points]
        if not local_args.gate_points or not local_args.audit_points:
            continue
        local_classifiers = build_classifiers(x_train, y_train, local_args)
        tr, ca, te = build_examples(
            local_args,
            local_classifiers,
            x_train,
            y_train,
            x_cal,
            y_cal,
            x_test,
            y_test,
            args.audit_threshold,
        )
        row = evaluate_models(tr, ca, te, args.alpha, args.bait_quantile, args.ridge, args.admission_threshold)
        dq = decision_quantities(row)
        sweep.append(
            {
                "early_points": early_points,
                "gate_points": local_args.gate_points,
                "audit_points": local_args.audit_points,
                "durable_rate": row["test_summary"]["durable_rate"],
                "early_accuracy": row["test_summary"]["early_accuracy"],
                "intensity_winner": winner(row["overall"], "intensity"),
                "admission_winner": winner(row["overall"], "admission"),
                "continuous_intensity_rmse": dq["continuous_intensity_rmse"],
                "gate_intensity_rmse": dq["gate_intensity_rmse"],
                "continuous_false_admission": dq["continuous_false_admission"],
                "gate_false_admission": dq["gate_false_admission"],
                "continuous_detection": dq["continuous_detection"],
                "gate_detection": dq["gate_detection"],
                "continuous_bait_false": dq["continuous_bait_false"],
                "gate_bait_false": dq["gate_bait_false"],
            }
        )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "UCI Pen-Based Recognition of Handwritten Digits",
            "url": UCI_DATASET_URL,
            "raw_files": DATA_URLS,
            "features": 16,
            "points": 8,
            "classes": 10,
        },
        "config": {
            "seed": args.seed,
            "calibration_fraction": args.calibration_fraction,
            "early_points": args.early_points,
            "gate_points": args.gate_points,
            "audit_points": args.audit_points,
            "early_grid": args.early_grid,
            "audit_threshold": args.audit_threshold,
            "alpha": args.alpha,
            "bait_quantile": args.bait_quantile,
            "classifier_ridge": args.classifier_ridge,
            "ridge": args.ridge,
            "intensity_noise": args.intensity_noise,
            "admission_noise": args.admission_noise,
            "admission_threshold": args.admission_threshold,
            "train_n": len(x_train),
            "calibration_n": len(x_cal),
            "test_n": len(x_test),
        },
        "main": main,
        "decision_quantities": decision_quantities(main),
        "prefix_sweep": sweep,
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
        cls = overall[name]["admission_classification"]
        model_rows.append(
            [
                name,
                fmt(overall[name]["intensity"]["rmse_observed"]),
                fmt(overall[name]["intensity"]["r2_observed"]),
                fmt(overall[name]["admission_regression"]["rmse_observed"]),
                fmt(cls["accuracy"]),
                fmt(cls["admission_detection"]),
                fmt(cls["nonadmitted_false_admission"]),
                fmt(cls["bait_false_admission"]),
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
                fmt(s["durable_rate"]),
                fmt(s["mean_intensity"]),
                fmt(s["mean_gate_score"]),
                fmt(s["mean_gate_same_fraction"]),
                fmt(s["mean_audit_true_fraction"]),
            ]
        )

    digit_rows = []
    for digit, data in main["test_digit_summary"].items():
        cont = overall["continuous_early"]["admission_classification"]["by_digit"][digit]
        gate = overall["temporal_gate"]["admission_classification"]["by_digit"][digit]
        digit_rows.append(
            [
                digit,
                str(int(data["n"])),
                fmt(data["early_accuracy"]),
                fmt(data["durable_rate"]),
                fmt(data["bait_rate"]),
                fmt(data["mean_intensity"]),
                fmt(data["mean_gate_score"]),
                fmt(data["mean_audit_true_fraction"]),
                fmt(cont["false_admission"]),
                fmt(gate["false_admission"]),
            ]
        )

    sweep_rows = []
    for row in result["prefix_sweep"]:
        sweep_rows.append(
            [
                str(row["early_points"]),
                ",".join(str(v) for v in row["gate_points"]),
                ",".join(str(v) for v in row["audit_points"]),
                fmt(row["early_accuracy"]),
                fmt(row["durable_rate"]),
                row["intensity_winner"],
                row["admission_winner"],
                fmt(row["continuous_false_admission"]),
                fmt(row["gate_false_admission"]),
                fmt(row["continuous_detection"]),
                fmt(row["gate_detection"]),
                fmt(row["continuous_bait_false"]),
                fmt(row["gate_bait_false"]),
            ]
        )

    lines = [
        "# E17 Temporal PenDigits Admission Probe",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- dataset: `{result['dataset']['name']}`",
        f"- dataset URL: `{result['dataset']['url']}`",
        f"- train/calibration/test: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
        f"- early/gate/audit points: `{config['early_points']}` / `{config['gate_points']}` / `{config['audit_points']}`",
        f"- audit threshold: `{config['audit_threshold']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E17 tests whether E16's negative static-image result changes when",
        "the external proxy has temporal structure. Early trajectory points",
        "supply local continuous evidence, middle points supply a label-free",
        "persistence gate, and late points define durable admission.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous intensity RMSE", fmt(dq["continuous_intensity_rmse"])],
                ["gate intensity RMSE", fmt(dq["gate_intensity_rmse"])],
                ["governed intensity RMSE", fmt(dq["governed_intensity_rmse"])],
                ["hybrid intensity RMSE", fmt(dq["hybrid_intensity_rmse"])],
                ["continuous admission RMSE", fmt(dq["continuous_admission_rmse"])],
                ["gate admission RMSE", fmt(dq["gate_admission_rmse"])],
                ["governed admission RMSE", fmt(dq["governed_admission_rmse"])],
                ["hybrid admission RMSE", fmt(dq["hybrid_admission_rmse"])],
                ["continuous false admission", fmt(dq["continuous_false_admission"])],
                ["gate false admission", fmt(dq["gate_false_admission"])],
                ["governed false admission", fmt(dq["governed_false_admission"])],
                ["continuous detection", fmt(dq["continuous_detection"])],
                ["gate detection", fmt(dq["gate_detection"])],
                ["continuous bait false", fmt(dq["continuous_bait_false"])],
                ["gate bait false", fmt(dq["gate_bait_false"])],
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
                "durable rate",
                "mean intensity",
                "mean gate",
                "gate same",
                "audit true",
            ],
            summary_rows,
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "intensity RMSE",
                "intensity R2",
                "admission RMSE",
                "admission acc",
                "detect",
                "nonadmit FA",
                "bait FA",
                "bait n",
            ],
            model_rows,
        ),
        "",
        "## Digit Summary",
        "",
        md_table(
            [
                "digit",
                "n",
                "early acc",
                "durable rate",
                "bait rate",
                "intensity",
                "gate score",
                "audit true",
                "cont FA",
                "gate FA",
            ],
            digit_rows,
        ),
        "",
        "## Prefix Sweep",
        "",
        md_table(
            [
                "early",
                "gate",
                "audit",
                "early acc",
                "durable rate",
                "intensity winner",
                "admission winner",
                "cont FA",
                "gate FA",
                "cont detect",
                "gate detect",
                "cont bait FA",
                "gate bait FA",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    if result["finding"] == "TEMPORAL_PERSISTENCE_GOVERNS_ADMISSION":
        lines.extend(
            [
                "Temporal persistence survives the external proxy: early continuous",
                "stroke evidence fits graded intensity, but middle-stroke stability",
                "controls false admission into durable recognition.",
            ]
        )
    elif result["finding"] == "EARLY_TEMPORAL_EVIDENCE_ABSORBS_PERSISTENCE":
        lines.extend(
            [
                "Early trajectory evidence absorbs temporal persistence on this",
                "configuration. This would extend E16's negative static-image",
                "anchor into a simple temporal proxy.",
            ]
        )
    elif result["finding"] == "TEMPORAL_HYBRID_EVIDENCE_PERSISTENCE_NEEDED":
        lines.extend(
            [
                "The external temporal proxy does not give the gate a clean solo",
                "win, but the governed/hybrid models control admission better than",
                "early evidence alone. This supports the narrower B-series claim:",
                "temporal persistence matters when early local evidence is",
                "insufficient, but it works best as a governed field rather than a",
                "standalone bucket.",
            ]
        )
    else:
        lines.extend(
            [
                "The temporal PenDigits anchor is inconclusive under this",
                "configuration. Either the prefix split is too easy, too hard, or",
                "the gate and continuous field are not yet cleanly separated.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external pen-trajectory digit data, not a synthetic B-series generator;",
            "- early evidence uses only the first trajectory points;",
            "- the persistence gate is label-free and uses middle trajectory points;",
            "- durable admission is evaluated on later trajectory points and true labels;",
            "- calibration thresholds are estimated on calibration examples and scored on the held-out test file;",
            "- the prefix sweep tests whether the result depends on how much early evidence is available.",
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
    parser.add_argument("--audit-points", type=int, nargs="+", default=[7, 8])
    parser.add_argument("--early-grid", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--audit-threshold", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--bait-quantile", type=float, default=0.70)
    parser.add_argument("--classifier-ridge", type=float, default=1e-2)
    parser.add_argument("--ridge", type=float, default=5e-3)
    parser.add_argument("--intensity-noise", type=float, default=0.015)
    parser.add_argument("--admission-noise", type=float, default=0.020)
    parser.add_argument("--admission-threshold", type=float, default=0.50)
    parser.add_argument("--decision-margin", type=float, default=0.005)
    parser.add_argument("--false-admission-margin", type=float, default=0.030)
    parser.add_argument("--detection-floor", type=float, default=0.650)
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
    json_path = args.report_dir / "e17_temporal_pendigits_admission_probe.json"
    md_path = args.report_dir / "e17_temporal_pendigits_admission_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
