"""E16 external perceptual persistence anchor.

E16 is the first B/E-series probe to leave the purely synthetic sandbox. It
uses the UCI Optical Recognition of Handwritten Digits dataset and asks whether
the B-series split survives in a real perceptual proxy task:

    - original-image continuous evidence should predict graded recognition
      strength;
    - cross-context persistence should predict durable admission.

The probe trains a small NumPy ridge classifier on real 8x8 handwritten digits.
For each digit, original-image features define the continuous field. A separate
gate perturbation set estimates prediction persistence without using the label.
The admission target is evaluated on a different audit perturbation set using
the true label. This keeps the gate evidence and target related but not
identical.
"""

from __future__ import annotations

import argparse
import json
import math
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import numpy as np


DATA_URLS = {
    "optdigits.tra": "https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra",
    "optdigits.tes": "https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes",
}
UCI_DATASET_URL = "https://archive.ics.uci.edu/dataset/80/optical%2Brecognition%2Bof%2Bhandwritten%2Bdigits"
MODEL_ORDER = ["scalar", "continuous_evidence", "persistence_gate", "governed_evidence", "hybrid_full"]
DIGITS = list(range(10))


@dataclass(frozen=True)
class Classifier:
    coef: list[list[float]]
    mean: list[float]
    sd: list[float]


@dataclass(frozen=True)
class Example:
    split: str
    label: int
    pred: int
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


def load_optdigits(path: Path) -> tuple[np.ndarray, np.ndarray]:
    rows = []
    labels = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        values = [int(item) for item in line.split(",")]
        rows.append(values[:-1])
        labels.append(values[-1])
    x = np.asarray(rows, dtype=float) / 16.0
    y = np.asarray(labels, dtype=int)
    return x, y


def one_hot(y: np.ndarray, classes: int = 10) -> np.ndarray:
    out = np.zeros((len(y), classes), dtype=float)
    out[np.arange(len(y)), y] = 1.0
    return out


def fit_classifier(x: np.ndarray, y: np.ndarray, ridge: float) -> Classifier:
    mean = x.mean(axis=0)
    sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
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
        coef=[[float(v) for v in row] for row in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
    )


def classifier_logits(model: Classifier, x: np.ndarray) -> np.ndarray:
    mean = np.asarray(model.mean, dtype=float)
    sd = np.asarray(model.sd, dtype=float)
    coef = np.asarray(model.coef, dtype=float)
    z = (x - mean) / sd
    design = np.hstack([np.ones((z.shape[0], 1)), z])
    return design @ coef


def softmax(logits: np.ndarray) -> np.ndarray:
    centered = logits - logits.max(axis=1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=1, keepdims=True)


def predict_proba(model: Classifier, x: np.ndarray) -> np.ndarray:
    return softmax(classifier_logits(model, x))


def fit_centroids(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    centroids = []
    for digit in DIGITS:
        rows = x[y == digit]
        centroids.append(rows.mean(axis=0))
    return np.asarray(centroids, dtype=float)


def shift_image(img: np.ndarray, dy: int, dx: int) -> np.ndarray:
    out = np.zeros_like(img)
    src_y0 = max(0, -dy)
    src_y1 = min(img.shape[0], img.shape[0] - dy)
    dst_y0 = max(0, dy)
    dst_y1 = min(img.shape[0], img.shape[0] + dy)
    src_x0 = max(0, -dx)
    src_x1 = min(img.shape[1], img.shape[1] - dx)
    dst_x0 = max(0, dx)
    dst_x1 = min(img.shape[1], img.shape[1] + dx)
    out[dst_y0:dst_y1, dst_x0:dst_x1] = img[src_y0:src_y1, src_x0:src_x1]
    return out


def blur_image(img: np.ndarray) -> np.ndarray:
    padded = np.pad(img, 1, mode="edge")
    acc = np.zeros_like(img)
    for dy in range(3):
        for dx in range(3):
            acc += padded[dy : dy + img.shape[0], dx : dx + img.shape[1]]
    return np.clip(acc / 9.0, 0.0, 1.0)


def thicken_image(img: np.ndarray) -> np.ndarray:
    padded = np.pad(img, 1, mode="constant")
    neighborhoods = []
    for dy, dx in [(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)]:
        neighborhoods.append(padded[dy : dy + img.shape[0], dx : dx + img.shape[1]])
    return np.clip(np.maximum.reduce(neighborhoods), 0.0, 1.0)


def center_occlude(img: np.ndarray) -> np.ndarray:
    out = img.copy()
    out[3:5, 3:5] *= 0.25
    return out


def border_fade(img: np.ndarray) -> np.ndarray:
    out = img.copy()
    out[0, :] *= 0.45
    out[-1, :] *= 0.45
    out[:, 0] *= 0.45
    out[:, -1] *= 0.45
    return out


def transform_batch(x: np.ndarray, transform: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    imgs = x.reshape((-1, 8, 8))
    out = np.asarray([transform(img).reshape(-1) for img in imgs], dtype=float)
    return np.clip(out, 0.0, 1.0)


def gate_transforms() -> list[tuple[str, Callable[[np.ndarray], np.ndarray]]]:
    return [
        ("shift_up", lambda img: shift_image(img, -1, 0)),
        ("shift_down", lambda img: shift_image(img, 1, 0)),
        ("shift_left", lambda img: shift_image(img, 0, -1)),
        ("shift_right", lambda img: shift_image(img, 0, 1)),
        ("fade", lambda img: np.clip(0.82 * img, 0.0, 1.0)),
        ("brighten", lambda img: np.clip(1.12 * img, 0.0, 1.0)),
    ]


def audit_transforms() -> list[tuple[str, Callable[[np.ndarray], np.ndarray]]]:
    return [
        ("shift_up_left", lambda img: shift_image(img, -1, -1)),
        ("shift_down_right", lambda img: shift_image(img, 1, 1)),
        ("shift_up_right", lambda img: shift_image(img, -1, 1)),
        ("blur", blur_image),
        ("thicken", thicken_image),
        ("center_occlude", center_occlude),
        ("border_fade", border_fade),
    ]


def image_shape_features(x: np.ndarray) -> np.ndarray:
    imgs = x.reshape((-1, 8, 8))
    rows = np.arange(8, dtype=float)
    cols = np.arange(8, dtype=float)
    yy, xx = np.meshgrid(rows, cols, indexing="ij")
    features = []
    for img in imgs:
        mass = float(img.sum())
        norm = mass + 1e-8
        ink_mean = float(img.mean())
        contrast = float(img.std())
        row_edge = float(np.mean(np.abs(np.diff(img, axis=0))))
        col_edge = float(np.mean(np.abs(np.diff(img, axis=1))))
        edge = 0.5 * (row_edge + col_edge)
        sym_h = 1.0 - float(np.mean(np.abs(img - np.flip(img, axis=1)))) / (ink_mean + 1e-3)
        sym_v = 1.0 - float(np.mean(np.abs(img - np.flip(img, axis=0)))) / (ink_mean + 1e-3)
        cx = float((img * xx).sum() / norm) / 7.0
        cy = float((img * yy).sum() / norm) / 7.0
        spread_x = float((img * (xx / 7.0 - cx) ** 2).sum() / norm)
        spread_y = float((img * (yy / 7.0 - cy) ** 2).sum() / norm)
        center_mass = float(img[2:6, 2:6].sum() / norm)
        features.append(
            [
                ink_mean,
                contrast,
                edge,
                np.clip(sym_h, -1.5, 1.0),
                np.clip(sym_v, -1.5, 1.0),
                cx,
                cy,
                spread_x,
                spread_y,
                center_mass,
            ]
        )
    return np.asarray(features, dtype=float)


def centroid_features(x: np.ndarray, centroids: np.ndarray, pred: np.ndarray) -> np.ndarray:
    distances = np.sqrt(((x[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=2))
    sorted_dist = np.sort(distances, axis=1)
    nearest_digit = np.argmin(distances, axis=1)
    pred_dist = distances[np.arange(len(x)), pred]
    nearest_dist = sorted_dist[:, 0]
    second_dist = sorted_dist[:, 1]
    centroid_margin = second_dist - nearest_dist
    pred_is_nearest = (pred == nearest_digit).astype(float)
    return np.vstack([pred_dist, nearest_dist, centroid_margin, pred_is_nearest]).T


def collect_examples(
    split: str,
    x: np.ndarray,
    y: np.ndarray,
    classifier: Classifier,
    centroids: np.ndarray,
    audit_threshold: float,
    intensity_noise: float,
    admission_noise: float,
    rng: np.random.Generator,
) -> list[Example]:
    probs = predict_proba(classifier, x)
    logits = classifier_logits(classifier, x)
    pred = np.argmax(probs, axis=1)
    sorted_probs = np.sort(probs, axis=1)
    top_prob = sorted_probs[:, -1]
    second_prob = sorted_probs[:, -2]
    margin = top_prob - second_prob
    entropy = -np.sum(probs * np.log(probs + 1e-12), axis=1) / math.log(10.0)
    true_prob = probs[np.arange(len(x)), y]
    true_logit = logits[np.arange(len(x)), y]
    top_logit = logits[np.arange(len(x)), pred]
    logit_margin = top_logit - np.partition(logits, -2, axis=1)[:, -2]
    shape = image_shape_features(x)
    centroid = centroid_features(x, centroids, pred)

    gate_preds = []
    gate_confidences = []
    for _, transform in gate_transforms():
        tx = transform_batch(x, transform)
        tprobs = predict_proba(classifier, tx)
        gate_preds.append(np.argmax(tprobs, axis=1))
        gate_confidences.append(tprobs[np.arange(len(x)), pred])
    gate_preds_arr = np.vstack(gate_preds).T
    gate_conf_arr = np.vstack(gate_confidences).T
    gate_same_fraction = np.mean(gate_preds_arr == pred[:, None], axis=1)
    gate_mean_confidence = np.mean(gate_conf_arr, axis=1)
    gate_score = top_prob * gate_same_fraction * gate_mean_confidence

    audit_true = []
    for _, transform in audit_transforms():
        tx = transform_batch(x, transform)
        tpred = np.argmax(predict_proba(classifier, tx), axis=1)
        audit_true.append(tpred == y)
    audit_true_arr = np.vstack(audit_true).T
    audit_true_fraction = np.mean(audit_true_arr, axis=1)
    original_correct = pred == y
    admission_clean = (original_correct & (audit_true_fraction >= audit_threshold)).astype(float)

    pred_one_hot = one_hot(pred)
    continuous = np.hstack(
        [
            pred_one_hot,
            top_prob[:, None],
            margin[:, None],
            entropy[:, None],
            logit_margin[:, None],
            top_logit[:, None],
            shape,
            centroid,
        ]
    )
    local_evidence = top_prob * (0.35 + margin) * (1.0 - 0.35 * entropy)

    examples = []
    for i in range(len(x)):
        intensity_clean = float(true_prob[i])
        examples.append(
            Example(
                split=split,
                label=int(y[i]),
                pred=int(pred[i]),
                scalar_score=float(top_prob[i]),
                continuous_features=[float(v) for v in continuous[i]],
                gate_score=float(gate_score[i]),
                gate_same_fraction=float(gate_same_fraction[i]),
                gate_mean_confidence=float(gate_mean_confidence[i]),
                audit_true_fraction=float(audit_true_fraction[i]),
                local_evidence=float(local_evidence[i]),
                target_intensity_clean=intensity_clean,
                target_intensity_observed=float(np.clip(intensity_clean + rng.normal(scale=intensity_noise), 0.0, 1.0)),
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


def calibrate_bait_threshold(examples: list[Example], bait_quantile: float) -> float:
    nonadmitted = [ep.local_evidence for ep in examples if ep.target_admission_clean < 0.5]
    if not nonadmitted:
        return float("inf")
    return float(np.quantile(np.asarray(nonadmitted, dtype=float), bait_quantile, method="higher"))


def gate_bit(ep: Example, gate_threshold: float) -> float:
    return 1.0 if ep.gate_score > gate_threshold else 0.0


def digit_vector(digit: int) -> list[float]:
    return [1.0 if digit == item else 0.0 for item in DIGITS]


def feature_vector(ep: Example, kind: str, gate_threshold: float) -> list[float]:
    pred_bits = digit_vector(ep.pred)
    bit = gate_bit(ep, gate_threshold)
    digit_gate_bits = [bit * value for value in pred_bits]
    if kind == "scalar":
        return [ep.scalar_score]
    if kind == "continuous":
        return ep.continuous_features
    if kind == "gate":
        return pred_bits + [bit] + digit_gate_bits
    if kind == "governed":
        return ep.continuous_features + [bit] + digit_gate_bits
    if kind == "hybrid":
        return ep.continuous_features + [
            ep.gate_score,
            ep.gate_same_fraction,
            ep.gate_mean_confidence,
            bit,
        ] + digit_gate_bits
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
    pred = phi @ np.asarray(model.coef, dtype=float)
    return np.clip(pred, 0.0, 1.0)


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
    correct = np.asarray([ep.pred == ep.label for ep in examples], dtype=bool)
    return {
        "n": float(len(examples)),
        "original_accuracy": float(correct.mean()),
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
        correct = [ep.pred == ep.label for ep in rows]
        bait = [ep.target_admission_clean < 0.5 and ep.local_evidence >= bait_threshold for ep in rows]
        out[str(digit)] = {
            "n": float(len(rows)),
            "original_accuracy": float(np.mean(correct)),
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
    bait_threshold = calibrate_bait_threshold(calibration_examples, bait_quantile)
    feature_kind = {
        "scalar": "scalar",
        "continuous_evidence": "continuous",
        "persistence_gate": "gate",
        "governed_evidence": "governed",
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
    cont_cls = overall["continuous_evidence"]["admission_classification"]
    gate_cls = overall["persistence_gate"]["admission_classification"]
    gov_cls = overall["governed_evidence"]["admission_classification"]
    hybrid_cls = overall["hybrid_full"]["admission_classification"]
    return {
        "continuous_intensity_rmse": overall["continuous_evidence"]["intensity"]["rmse_observed"],
        "gate_intensity_rmse": overall["persistence_gate"]["intensity"]["rmse_observed"],
        "governed_intensity_rmse": overall["governed_evidence"]["intensity"]["rmse_observed"],
        "hybrid_intensity_rmse": overall["hybrid_full"]["intensity"]["rmse_observed"],
        "continuous_admission_rmse": overall["continuous_evidence"]["admission_regression"]["rmse_observed"],
        "gate_admission_rmse": overall["persistence_gate"]["admission_regression"]["rmse_observed"],
        "governed_admission_rmse": overall["governed_evidence"]["admission_regression"]["rmse_observed"],
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
    cont_fits_intensity = dq["continuous_intensity_rmse"] + args.decision_margin < dq["gate_intensity_rmse"]
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
        return "EXTERNAL_CONTINUOUS_EVIDENCE_ABSORBS_PERSISTENCE"
    if cont_fits_intensity and gate_controls and governed_controls:
        return "EXTERNAL_EVIDENCE_FITS_INTENSITY_BUT_PERSISTENCE_GOVERNS_ADMISSION"
    if governed_controls:
        return "EXTERNAL_HYBRID_EVIDENCE_PERSISTENCE_NEEDED"
    return "EXTERNAL_DIGITS_ANCHOR_INCONCLUSIVE"


def prepare_splits(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    paths = download_dataset(args.data_dir)
    x_full_train, y_full_train = load_optdigits(paths["optdigits.tra"])
    x_test, y_test = load_optdigits(paths["optdigits.tes"])
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


def build_examples_for_threshold(
    args: argparse.Namespace,
    classifier: Classifier,
    centroids: np.ndarray,
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_cal: np.ndarray,
    y_cal: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    audit_threshold: float,
) -> tuple[list[Example], list[Example], list[Example]]:
    rng = np.random.default_rng(args.seed + int(round(1000 * audit_threshold)))
    train_examples = collect_examples(
        "train",
        x_train,
        y_train,
        classifier,
        centroids,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    cal_examples = collect_examples(
        "calibration",
        x_cal,
        y_cal,
        classifier,
        centroids,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    test_examples = collect_examples(
        "test",
        x_test,
        y_test,
        classifier,
        centroids,
        audit_threshold,
        args.intensity_noise,
        args.admission_noise,
        rng,
    )
    return train_examples, cal_examples, test_examples


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    x_train, y_train, x_cal, y_cal, x_test, y_test = prepare_splits(args)
    classifier = fit_classifier(x_train, y_train, args.classifier_ridge)
    centroids = fit_centroids(x_train, y_train)

    train_examples, cal_examples, test_examples = build_examples_for_threshold(
        args,
        classifier,
        centroids,
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
    for threshold in args.audit_grid:
        tr, ca, te = build_examples_for_threshold(
            args,
            classifier,
            centroids,
            x_train,
            y_train,
            x_cal,
            y_cal,
            x_test,
            y_test,
            threshold,
        )
        row = evaluate_models(tr, ca, te, args.alpha, args.bait_quantile, args.ridge, args.admission_threshold)
        dq = decision_quantities(row)
        sweep.append(
            {
                "audit_threshold": threshold,
                "durable_rate": row["test_summary"]["durable_rate"],
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
            "name": "UCI Optical Recognition of Handwritten Digits",
            "url": UCI_DATASET_URL,
            "raw_files": DATA_URLS,
            "features": 64,
            "classes": 10,
            "gate_transforms": [name for name, _ in gate_transforms()],
            "audit_transforms": [name for name, _ in audit_transforms()],
        },
        "config": {
            "seed": args.seed,
            "calibration_fraction": args.calibration_fraction,
            "audit_threshold": args.audit_threshold,
            "audit_grid": args.audit_grid,
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
        "phase_sweep": sweep,
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

    digit_rows = []
    for digit, data in main["test_digit_summary"].items():
        cont = overall["continuous_evidence"]["admission_classification"]["by_digit"][digit]
        gate = overall["persistence_gate"]["admission_classification"]["by_digit"][digit]
        digit_rows.append(
            [
                digit,
                str(int(data["n"])),
                fmt(data["original_accuracy"]),
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
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["audit_threshold"]),
                fmt(row["durable_rate"]),
                row["intensity_winner"],
                row["admission_winner"],
                fmt(row["continuous_intensity_rmse"]),
                fmt(row["gate_intensity_rmse"]),
                fmt(row["continuous_false_admission"]),
                fmt(row["gate_false_admission"]),
                fmt(row["continuous_detection"]),
                fmt(row["gate_detection"]),
                fmt(row["continuous_bait_false"]),
                fmt(row["gate_bait_false"]),
            ]
        )

    summary_rows = []
    for split_key in ["train_summary", "calibration_summary", "test_summary"]:
        s = main[split_key]
        summary_rows.append(
            [
                split_key.replace("_summary", ""),
                str(int(s["n"])),
                fmt(s["original_accuracy"]),
                fmt(s["durable_rate"]),
                fmt(s["mean_intensity"]),
                fmt(s["mean_gate_score"]),
                fmt(s["mean_gate_same_fraction"]),
                fmt(s["mean_audit_true_fraction"]),
            ]
        )

    lines = [
        "# E16 External Digits Persistence Anchor",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- dataset: `{result['dataset']['name']}`",
        f"- dataset URL: `{result['dataset']['url']}`",
        f"- train/calibration/test: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
        f"- audit threshold: `{config['audit_threshold']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E16 tests the B-series field/gate split on a real perceptual proxy:",
        "the UCI handwritten digit recognition dataset. Original-image",
        "evidence supplies the continuous field. Perturbation persistence",
        "supplies the admission gate. The admission target is evaluated on a",
        "different audit perturbation set, so the gate evidence is not the same",
        "quantity as the test label.",
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
                "orig acc",
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
                "orig acc",
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
        "## Audit-Threshold Sweep",
        "",
        md_table(
            [
                "audit th",
                "durable rate",
                "intensity winner",
                "admission winner",
                "cont intensity",
                "gate intensity",
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

    if result["finding"] == "EXTERNAL_EVIDENCE_FITS_INTENSITY_BUT_PERSISTENCE_GOVERNS_ADMISSION":
        lines.extend(
            [
                "The real-data proxy preserves the E15 split. Original-image",
                "continuous evidence is better for graded recognition strength,",
                "while perturbation persistence controls durable admission. This",
                "does not prove a neural gate, but it shows the architecture is not",
                "only a hand-written synthetic generator artifact.",
            ]
        )
    elif result["finding"] == "EXTERNAL_CONTINUOUS_EVIDENCE_ABSORBS_PERSISTENCE":
        lines.extend(
            [
                "Original-image continuous evidence absorbs the persistence gate on",
                "this task. This is a negative anchor for the broad gate claim:",
                "simple static recognition may not require a distinct admission",
                "gate when local evidence already predicts perturbation durability.",
            ]
        )
    elif result["finding"] == "EXTERNAL_HYBRID_EVIDENCE_PERSISTENCE_NEEDED":
        lines.extend(
            [
                "The governed or hybrid models are needed. The result supports a",
                "field-plus-persistence reading, but the split is not clean enough",
                "to say the gate alone governs admission.",
            ]
        )
    else:
        lines.extend(
            [
                "The external digit proxy is inconclusive under this configuration.",
                "Either the perturbation audit is too weak, too harsh, or original",
                "evidence and persistence are not separated cleanly enough.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external real handwritten digit data, not a synthetic B-series generator;",
            "- the OCR classifier is trained from scratch using NumPy only;",
            "- continuous evidence uses the original image only;",
            "- gate evidence uses label-free persistence under one perturbation set;",
            "- durable admission is evaluated with true labels under a different audit perturbation set;",
            "- calibration thresholds are estimated on calibration examples and scored on the held-out test set;",
            "- this is still not brain data; it is a real perceptual proxy and protocol rehearsal.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data" / "optdigits")
    parser.add_argument("--calibration-fraction", type=float, default=0.25)
    parser.add_argument("--classifier-ridge", type=float, default=1e-2)
    parser.add_argument("--ridge", type=float, default=5e-3)
    parser.add_argument("--audit-threshold", type=float, default=0.50)
    parser.add_argument("--audit-grid", type=float, nargs="+", default=[0.50, 0.58, 0.72, 0.86, 1.00])
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--bait-quantile", type=float, default=0.70)
    parser.add_argument("--intensity-noise", type=float, default=0.015)
    parser.add_argument("--admission-noise", type=float, default=0.020)
    parser.add_argument("--admission-threshold", type=float, default=0.50)
    parser.add_argument("--decision-margin", type=float, default=0.005)
    parser.add_argument("--false-admission-margin", type=float, default=0.050)
    parser.add_argument("--detection-floor", type=float, default=0.750)
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
    json_path = args.report_dir / "e16_external_digits_persistence_anchor.json"
    md_path = args.report_dir / "e16_external_digits_persistence_anchor.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
