"""E23 external Wall-Following gate-residual probe.

E22 showed that a trained no-gate MLP absorbs the gate on our synthetic
closed-loop simulator. E23 moves to an external sequential robot-control anchor:
the UCI Wall-Following Robot Navigation dataset.

The task is command imitation, not a causal intervention log. Each row contains
ultrasound readings and the command label used for wall following. We build
short sensor-history windows, score candidate command packets, and compare:

    - a trained no-gate continuous MLP;
    - a same-architecture hybrid MLP with label-free temporal gate features.

If the hybrid does not beat the no-gate MLP, the external anchor supports the
E22 absorption correction. If it does, it suggests a gate-like residual in real
sequential robot data.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import urllib.request
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

import e22_trained_mlp_closed_loop_probe as e22


DATASET_PAGE = "https://archive-beta.ics.uci.edu/dataset/194/wall+following+robot+navigation+data"
DATASET_DOI = "https://doi.org/10.24432/C57C8W"
DATA_URL = "https://cdn.uci-ics-mlr-prod.aws.uci.edu/194/wall%2Bfollowing%2Brobot%2Bnavigation%2Bdata.zip"
DATA_FILE = "sensor_readings_24.data"
ACTION_ORDER = ["Move-Forward", "Slight-Left-Turn", "Slight-Right-Turn", "Sharp-Right-Turn"]
ACTION_TO_INDEX = {name: i for i, name in enumerate(ACTION_ORDER)}
TURN_SEVERITY = {
    "Move-Forward": 0,
    "Slight-Left-Turn": -1,
    "Slight-Right-Turn": 1,
    "Sharp-Right-Turn": 2,
}
MODEL_ORDER = ["scalar_mlp", "continuous_mlp", "hybrid_mlp"]


@dataclass(frozen=True)
class WindowExample:
    split: str
    episode_id: int
    row_index: int
    label: int
    window: list[float]
    current: list[float]
    delta: list[float]
    stats: list[float]
    probe_probs: list[float]
    probe_pred: int
    probe_top: float
    probe_margin: float
    probe_entropy: float
    smoothness: float
    action_stability: list[float]


@dataclass(frozen=True)
class Packet:
    split: str
    episode_id: int
    row_index: int
    label: int
    action: str
    action_index: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_bit_clean: float
    gate_stability: float
    gate_margin: float
    unsafe_proxy: float
    utility_clean: float
    utility_observed: float
    target_select_clean: float
    target_select_observed: float


def download_dataset(data_dir: Path) -> Path:
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / "wall_following_robot_navigation.zip"
    if not path.exists():
        urllib.request.urlretrieve(DATA_URL, path)
    return path


def load_wall_following(data_dir: Path) -> tuple[np.ndarray, np.ndarray, list[str], dict[str, Any]]:
    zip_path = download_dataset(data_dir)
    with zipfile.ZipFile(zip_path) as z:
        names = z.namelist()
        if DATA_FILE not in names:
            raise FileNotFoundError(f"{DATA_FILE} not found in {zip_path}; found {names}")
        rows = []
        labels = []
        with z.open(DATA_FILE) as raw:
            text = (line.decode("utf-8").strip() for line in raw)
            reader = csv.reader(text)
            for row in reader:
                if not row:
                    continue
                rows.append([float(v) for v in row[:-1]])
                labels.append(row[-1])
    x = np.asarray(rows, dtype=float)
    y = np.asarray([ACTION_TO_INDEX[label] for label in labels], dtype=int)
    meta = {
        "zip_path": str(zip_path),
        "zip_size": int(zip_path.stat().st_size),
        "rows": int(len(x)),
        "features": int(x.shape[1]),
        "labels": {name: int(sum(label == name for label in labels)) for name in ACTION_ORDER},
        "change_rate": float(np.mean(y[1:] != y[:-1])),
        "files": names,
    }
    return x, y, labels, meta


def split_bounds(n: int, train_fraction: float, calibration_fraction: float) -> dict[str, tuple[int, int]]:
    train_end = int(round(n * train_fraction))
    cal_end = int(round(n * (train_fraction + calibration_fraction)))
    return {
        "train": (0, train_end),
        "calibration": (train_end, cal_end),
        "test": (cal_end, n),
    }


def window_indices(bounds: tuple[int, int], history: int) -> np.ndarray:
    start, end = bounds
    first = start + history - 1
    if first >= end:
        return np.asarray([], dtype=int)
    return np.arange(first, end, dtype=int)


def base_window_features(x: np.ndarray, index: int, history: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    window = x[index - history + 1 : index + 1]
    current = window[-1]
    previous = window[-2] if history > 1 else window[-1]
    delta = current - previous
    mean = window.mean(axis=0)
    sd = window.std(axis=0)
    minv = window.min(axis=0)
    maxv = window.max(axis=0)
    stats = np.concatenate([mean, sd, minv, maxv])
    smoothness = float(math.exp(-np.mean(np.abs(np.diff(window, axis=0))) / 0.15)) if history > 1 else 1.0
    return window.reshape(-1), current, delta, stats, smoothness


def softmax(values: np.ndarray) -> np.ndarray:
    centered = values - values.max(axis=1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=1, keepdims=True)


def one_hot(y: np.ndarray, classes: int) -> np.ndarray:
    out = np.zeros((len(y), classes), dtype=float)
    out[np.arange(len(y)), y] = 1.0
    return out


def fit_probe_classifier(x_train: np.ndarray, y_train: np.ndarray, ridge: float) -> dict[str, list[list[float]] | list[float]]:
    mean = x_train.mean(axis=0)
    sd = x_train.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x_train - mean) / sd
    design = np.hstack([np.ones((len(z), 1)), z, z * z])
    target = one_hot(y_train, len(ACTION_ORDER))
    penalty = ridge * np.eye(design.shape[1])
    penalty[0, 0] = 0.0
    lhs = design.T @ design + penalty
    rhs = design.T @ target
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return {
        "mean": [float(v) for v in mean],
        "sd": [float(v) for v in sd],
        "coef": [[float(v) for v in row] for row in coef],
    }


def predict_probe(model: dict[str, Any], x_raw: np.ndarray) -> np.ndarray:
    mean = np.asarray(model["mean"], dtype=float)
    sd = np.asarray(model["sd"], dtype=float)
    coef = np.asarray(model["coef"], dtype=float)
    z = (x_raw - mean) / sd
    design = np.hstack([np.ones((len(z), 1)), z, z * z])
    return softmax(design @ coef)


def summarize_probs(probs: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    pred = np.argmax(probs, axis=1)
    sorted_probs = np.sort(probs, axis=1)
    top = sorted_probs[:, -1]
    margin = sorted_probs[:, -1] - sorted_probs[:, -2]
    entropy = -np.sum(probs * np.log(probs + 1e-12), axis=1) / math.log(probs.shape[1])
    return pred, top, margin, entropy


def action_stability(preds: np.ndarray, position: int, history: int) -> list[float]:
    first = max(0, position - history + 1)
    local = preds[first : position + 1]
    return [float(np.mean(local == i)) for i in range(len(ACTION_ORDER))]


def prepare_examples(
    x: np.ndarray,
    y: np.ndarray,
    args: argparse.Namespace,
) -> tuple[dict[str, list[WindowExample]], dict[str, Any]]:
    bounds = split_bounds(len(x), args.train_fraction, args.calibration_fraction)
    feature_rows: dict[str, np.ndarray] = {}
    index_rows: dict[str, np.ndarray] = {}
    labels: dict[str, np.ndarray] = {}
    for split, bound in bounds.items():
        indices = window_indices(bound, args.history)
        rows = []
        for idx in indices:
            window, current, delta, stats, smoothness = base_window_features(x, int(idx), args.history)
            rows.append(np.concatenate([window, delta, stats, [smoothness]]))
        feature_rows[split] = np.asarray(rows, dtype=float)
        index_rows[split] = indices
        labels[split] = y[indices]

    probe = fit_probe_classifier(feature_rows["train"], labels["train"], args.probe_ridge)
    all_feature_rows = np.vstack([feature_rows[split] for split in ["train", "calibration", "test"]])
    all_probs = predict_probe(probe, all_feature_rows)
    cursor = 0
    probs_by_split: dict[str, np.ndarray] = {}
    pred_by_split: dict[str, np.ndarray] = {}
    for split in ["train", "calibration", "test"]:
        count = len(feature_rows[split])
        probs = all_probs[cursor : cursor + count]
        probs_by_split[split] = probs
        pred_by_split[split] = np.argmax(probs, axis=1)
        cursor += count

    examples: dict[str, list[WindowExample]] = {}
    for split in ["train", "calibration", "test"]:
        probs = probs_by_split[split]
        pred, top, margin, entropy = summarize_probs(probs)
        split_examples: list[WindowExample] = []
        for local_pos, idx in enumerate(index_rows[split]):
            window, current, delta, stats, smoothness = base_window_features(x, int(idx), args.history)
            stability = action_stability(pred_by_split[split], local_pos, args.stability_history)
            split_examples.append(
                WindowExample(
                    split=split,
                    episode_id=local_pos,
                    row_index=int(idx),
                    label=int(y[idx]),
                    window=[float(v) for v in window],
                    current=[float(v) for v in current],
                    delta=[float(v) for v in delta],
                    stats=[float(v) for v in stats],
                    probe_probs=[float(v) for v in probs[local_pos]],
                    probe_pred=int(pred[local_pos]),
                    probe_top=float(top[local_pos]),
                    probe_margin=float(margin[local_pos]),
                    probe_entropy=float(entropy[local_pos]),
                    smoothness=float(smoothness),
                    action_stability=stability,
                )
            )
        examples[split] = split_examples

    audit = {
        "bounds": {split: [int(a), int(b)] for split, (a, b) in bounds.items()},
        "windows": {split: int(len(v)) for split, v in examples.items()},
        "probe_accuracy": {
            split: float(np.mean(np.argmax(probs_by_split[split], axis=1) == labels[split]))
            for split in ["train", "calibration", "test"]
        },
        "probe_model": {
            "raw_feature_count": int(feature_rows["train"].shape[1]),
            "expanded_feature_count": int(len(probe["coef"])),
        },
    }
    return examples, audit


def action_bits(action_index: int) -> list[float]:
    return [1.0 if action_index == i else 0.0 for i in range(len(ACTION_ORDER))]


def unsafe_proxy(candidate: int, true_label: int) -> float:
    if candidate == true_label:
        return 0.0
    cand_name = ACTION_ORDER[candidate]
    true_name = ACTION_ORDER[true_label]
    cand = TURN_SEVERITY[cand_name]
    true = TURN_SEVERITY[true_name]
    if cand == 0 and true != 0:
        return 1.0
    if cand != 0 and true != 0 and np.sign(cand) != np.sign(true):
        return 1.0
    if abs(cand - true) >= 2:
        return 1.0
    return 0.0


def packet_features(example: WindowExample, action_index: int) -> list[float]:
    probs = np.asarray(example.probe_probs, dtype=float)
    candidate_prob = float(probs[action_index])
    other_max = float(np.max(np.delete(probs, action_index)))
    candidate_margin = candidate_prob - other_max
    severity = TURN_SEVERITY[ACTION_ORDER[action_index]]
    return [
        *action_bits(action_index),
        severity / 2.0,
        abs(severity) / 2.0,
        *example.window,
        *example.delta,
        *example.stats,
        *example.probe_probs,
        example.probe_top,
        example.probe_margin,
        example.probe_entropy,
        candidate_prob,
        candidate_margin,
        example.smoothness,
    ]


def collect_packets(
    examples: list[WindowExample],
    args: argparse.Namespace,
    gate_threshold: float | None = None,
) -> list[Packet]:
    rng = np.random.default_rng(args.seed + {"train": 310, "calibration": 410, "test": 510}[examples[0].split])
    packets: list[Packet] = []
    for example in examples:
        probs = np.asarray(example.probe_probs, dtype=float)
        for action_index, action in enumerate(ACTION_ORDER):
            candidate_prob = float(probs[action_index])
            other_max = float(np.max(np.delete(probs, action_index)))
            gate_margin = candidate_prob - other_max
            stability = float(example.action_stability[action_index])
            positive_margin = max(0.0, gate_margin)
            gate_score = (
                candidate_prob
                * positive_margin
                * stability
                * (1.0 - 0.55 * example.probe_entropy)
                * example.smoothness
            )
            unsafe = unsafe_proxy(action_index, example.label)
            selected = float(action_index == example.label)
            utility = selected - args.unsafe_penalty * unsafe
            bit = 0.0 if gate_threshold is None else float(gate_score > gate_threshold)
            packets.append(
                Packet(
                    split=example.split,
                    episode_id=example.episode_id,
                    row_index=example.row_index,
                    label=example.label,
                    action=action,
                    action_index=action_index,
                    scalar_score=candidate_prob,
                    continuous_features=packet_features(example, action_index),
                    gate_score=float(gate_score),
                    gate_bit_clean=bit,
                    gate_stability=stability,
                    gate_margin=float(gate_margin),
                    unsafe_proxy=unsafe,
                    utility_clean=float(utility),
                    utility_observed=float(utility + rng.normal(scale=args.utility_noise)),
                    target_select_clean=selected,
                    target_select_observed=float(np.clip(selected + rng.normal(scale=args.select_noise), 0.0, 1.0)),
                )
            )
    return packets


def calibrate_gate(packets: list[Packet], alpha: float) -> float:
    nonselected = [packet.gate_score for packet in packets if packet.target_select_clean < 0.5]
    if not nonselected:
        return float("inf")
    return float(np.quantile(np.asarray(nonselected, dtype=float), 1.0 - alpha, method="higher"))


def feature_vector(packet: Packet, kind: str, gate_threshold: float) -> list[float]:
    bit = float(packet.gate_score > gate_threshold)
    if kind == "scalar":
        return [packet.scalar_score, packet.gate_margin, *action_bits(packet.action_index)]
    if kind == "continuous":
        return packet.continuous_features
    if kind == "hybrid":
        return packet.continuous_features + [
            packet.gate_score,
            packet.gate_stability,
            packet.gate_margin,
            bit,
            bit * packet.scalar_score,
        ]
    raise ValueError(f"unknown feature kind: {kind}")


def raw_matrix(packets: list[Packet], kind: str, gate_threshold: float) -> np.ndarray:
    return np.asarray([feature_vector(packet, kind, gate_threshold) for packet in packets], dtype=float)


def target_vector(packets: list[Packet], kind: str) -> np.ndarray:
    if kind == "value":
        return np.asarray([packet.utility_observed for packet in packets], dtype=float)
    if kind == "select":
        return np.asarray([packet.target_select_observed for packet in packets], dtype=float)
    raise ValueError(f"unknown target kind: {kind}")


def train_and_score_mlp(
    train: list[Packet],
    cal: list[Packet],
    test: list[Packet],
    name: str,
    feature_kind: str,
    gate_threshold: float,
    args: argparse.Namespace,
    seed_offset: int,
) -> dict[str, Any]:
    train_x = raw_matrix(train, feature_kind, gate_threshold)
    cal_x = raw_matrix(cal, feature_kind, gate_threshold)
    test_x = raw_matrix(test, feature_kind, gate_threshold)
    train_value = target_vector(train, "value")
    cal_value = target_vector(cal, "value")
    test_value = target_vector(test, "value")
    train_select = target_vector(train, "select")
    cal_select = target_vector(cal, "select")
    test_select = target_vector(test, "select")

    value_model = e22.train_mlp(train_x, train_value, cal_x, cal_value, feature_kind, "value", args, seed_offset)
    select_model = e22.train_mlp(train_x, train_select, cal_x, cal_select, feature_kind, "select", args, seed_offset + 1)
    value_pred = e22.predict_mlp(value_model, test_x)
    select_pred = e22.predict_mlp(select_model, test_x)
    return {
        "value": {
            "rmse_observed": e22.e20.rmse(test_value, value_pred),
            "r2_observed": e22.e20.r2(test_value, value_pred),
        },
        "select_regression": {
            "rmse_observed": e22.e20.rmse(test_select, select_pred),
            "r2_observed": e22.e20.r2(test_select, select_pred),
        },
        "row_selection": row_metrics(test, select_pred, args.row_threshold),
        "policy": policy_metrics(test, select_pred),
        "model": {
            "feature_kind": feature_kind,
            "basis_kind": "trained_mlp",
            "feature_count": int(train_x.shape[1]),
            "hidden": args.hidden,
            "value_history": value_model.history,
            "select_history": select_model.history,
        },
    }


def row_metrics(packets: list[Packet], select_scores: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([packet.target_select_clean >= 0.5 for packet in packets], dtype=bool)
    calls = select_scores >= threshold
    return {
        "row_accuracy": float(np.mean(calls == truth)),
        "optimal_detection": mean_or_nan([float(v) for v in calls[truth]]),
        "nonoptimal_false_admission": mean_or_nan([float(v) for v in calls[~truth]]),
    }


def mean_or_nan(values: list[float]) -> float:
    if not values:
        return float("nan")
    return float(np.mean(np.asarray(values, dtype=float)))


def group_packets(packets: list[Packet]) -> dict[int, list[Packet]]:
    groups: dict[int, list[Packet]] = {}
    for packet in packets:
        groups.setdefault(packet.episode_id, []).append(packet)
    return groups


def policy_metrics(packets: list[Packet], select_scores: np.ndarray) -> dict[str, Any]:
    groups = group_packets(packets)
    scores = {id(packet): float(select_scores[i]) for i, packet in enumerate(packets)}
    exact = []
    regrets = []
    unsafe_choice = []
    unsafe_wrong = []
    boundary_errors = []
    chosen_actions = {action: 0 for action in ACTION_ORDER}
    optimal_actions = {action: 0 for action in ACTION_ORDER}
    for episode_packets in groups.values():
        chosen = max(episode_packets, key=lambda packet: scores[id(packet)])
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        chosen_actions[chosen.action] += 1
        optimal_actions[optimal.action] += 1
        exact.append(float(chosen.action_index == optimal.action_index))
        regrets.append(float(optimal.utility_clean - chosen.utility_clean))
        unsafe_choice.append(chosen.unsafe_proxy)
        unsafe_wrong.append(float(chosen.unsafe_proxy > 0.5 and chosen.action_index != optimal.action_index))
        boundary_errors.append(float(chosen.action_index != optimal.action_index and chosen.label != ACTION_TO_INDEX["Move-Forward"]))
    return {
        "action_accuracy": float(np.mean(exact)),
        "mean_regret": float(np.mean(regrets)),
        "p90_regret": float(np.quantile(np.asarray(regrets, dtype=float), 0.90, method="higher")),
        "unsafe_choice_proxy": float(np.mean(unsafe_choice)),
        "unsafe_wrong_proxy": float(np.mean(unsafe_wrong)),
        "boundary_error": float(np.mean(boundary_errors)),
        "chosen_actions": chosen_actions,
        "optimal_actions": optimal_actions,
    }


def summarize_packets(packets: list[Packet]) -> dict[str, Any]:
    groups = group_packets(packets)
    optimal_actions = {action: 0 for action in ACTION_ORDER}
    for episode_packets in groups.values():
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        optimal_actions[optimal.action] += 1
    return {
        "episodes": int(len(groups)),
        "packets": int(len(packets)),
        "optimal_actions": optimal_actions,
        "mean_gate_score": float(np.mean([packet.gate_score for packet in packets])),
        "mean_utility": float(np.mean([packet.utility_clean for packet in packets])),
        "mean_unsafe_proxy": float(np.mean([packet.unsafe_proxy for packet in packets])),
    }


def decision_quantities(overall: dict[str, Any]) -> dict[str, float]:
    return {
        "scalar_accuracy": overall["scalar_mlp"]["policy"]["action_accuracy"],
        "continuous_accuracy": overall["continuous_mlp"]["policy"]["action_accuracy"],
        "hybrid_accuracy": overall["hybrid_mlp"]["policy"]["action_accuracy"],
        "scalar_regret": overall["scalar_mlp"]["policy"]["mean_regret"],
        "continuous_regret": overall["continuous_mlp"]["policy"]["mean_regret"],
        "hybrid_regret": overall["hybrid_mlp"]["policy"]["mean_regret"],
        "continuous_unsafe_wrong": overall["continuous_mlp"]["policy"]["unsafe_wrong_proxy"],
        "hybrid_unsafe_wrong": overall["hybrid_mlp"]["policy"]["unsafe_wrong_proxy"],
        "continuous_boundary_error": overall["continuous_mlp"]["policy"]["boundary_error"],
        "hybrid_boundary_error": overall["hybrid_mlp"]["policy"]["boundary_error"],
        "continuous_select_rmse": overall["continuous_mlp"]["select_regression"]["rmse_observed"],
        "hybrid_select_rmse": overall["hybrid_mlp"]["select_regression"]["rmse_observed"],
    }


def classify_finding(args: argparse.Namespace, audit: dict[str, Any], dq: dict[str, float]) -> str:
    test_probe = audit["probe_accuracy"]["test"]
    majority = audit["majority_accuracy"]["test"]
    if dq["continuous_accuracy"] < majority + args.minimum_gain_over_majority:
        return "EXTERNAL_CONTROL_ANCHOR_TOO_WEAK"
    continuous_absorbs = (
        dq["continuous_regret"] <= dq["hybrid_regret"] + args.regret_margin
        and dq["continuous_accuracy"] >= dq["hybrid_accuracy"] - args.accuracy_margin
    )
    weak_hybrid_edge = (
        dq["hybrid_regret"] < dq["continuous_regret"]
        and dq["hybrid_accuracy"] > dq["continuous_accuracy"]
        and dq["hybrid_unsafe_wrong"] <= dq["continuous_unsafe_wrong"]
    )
    hybrid_survives = (
        dq["hybrid_regret"] + args.regret_margin < dq["continuous_regret"]
        and dq["hybrid_accuracy"] > dq["continuous_accuracy"] + args.accuracy_margin
    )
    if continuous_absorbs:
        if weak_hybrid_edge:
            return "EXTERNAL_MLP_ABSORBS_GATE_WITH_WEAK_HYBRID_EDGE"
        return "EXTERNAL_MLP_ABSORBS_GATE"
    if hybrid_survives:
        return "EXTERNAL_GATE_RESIDUAL_SURVIVES_MLP"
    if test_probe < majority + args.minimum_gain_over_majority:
        return "EXTERNAL_CONTROL_ANCHOR_TOO_WEAK"
    return "EXTERNAL_WALL_FOLLOWING_INCONCLUSIVE"


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    x, y, labels, dataset_meta = load_wall_following(args.data_dir)
    examples, audit = prepare_examples(x, y, args)
    cal_pre = collect_packets(examples["calibration"], args)
    gate_threshold = calibrate_gate(cal_pre, args.alpha)
    train = collect_packets(examples["train"], args, gate_threshold)
    cal = collect_packets(examples["calibration"], args, gate_threshold)
    test = collect_packets(examples["test"], args, gate_threshold)
    majority_by_split = {}
    for split, split_examples in examples.items():
        split_labels = [example.label for example in split_examples]
        counts = np.bincount(np.asarray(split_labels, dtype=int), minlength=len(ACTION_ORDER))
        majority_by_split[split] = float(counts.max() / counts.sum())
    audit["majority_accuracy"] = majority_by_split

    overall = {
        "scalar_mlp": train_and_score_mlp(train, cal, test, "scalar_mlp", "scalar", gate_threshold, args, 2300),
        "continuous_mlp": train_and_score_mlp(train, cal, test, "continuous_mlp", "continuous", gate_threshold, args, 2400),
        "hybrid_mlp": train_and_score_mlp(train, cal, test, "hybrid_mlp", "hybrid", gate_threshold, args, 2500),
    }
    dq = decision_quantities(overall)
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "UCI Wall-Following Robot Navigation Data",
            "page": DATASET_PAGE,
            "doi": DATASET_DOI,
            "download_url": DATA_URL,
            **dataset_meta,
        },
        "config": {
            "seed": args.seed,
            "history": args.history,
            "stability_history": args.stability_history,
            "train_fraction": args.train_fraction,
            "calibration_fraction": args.calibration_fraction,
            "alpha": args.alpha,
            "hidden": args.hidden,
            "epochs": args.epochs,
            "patience": args.patience,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "unsafe_penalty": args.unsafe_penalty,
        },
        "audit": audit,
        "gate_threshold": gate_threshold,
        "train_summary": summarize_packets(train),
        "calibration_summary": summarize_packets(cal),
        "test_summary": summarize_packets(test),
        "overall": overall,
        "decision_quantities": dq,
    }
    result["finding"] = classify_finding(args, audit, dq)
    return result


def fmt(value: float) -> str:
    if isinstance(value, float) and math.isnan(value):
        return "nan"
    return f"{value:.3f}"


def action_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{action}:{counts.get(action, 0)}" for action in ACTION_ORDER)


def write_report(path: Path, result: dict[str, Any]) -> None:
    dataset = result["dataset"]
    config = result["config"]
    audit = result["audit"]
    overall = result["overall"]
    dq = result["decision_quantities"]
    lines: list[str] = []
    lines.extend(
        [
            "# E23 External Wall-Following Gate-Residual Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{dataset['name']}`",
            f"- dataset page: `{dataset['page']}`",
            f"- DOI: `{dataset['doi']}`",
            f"- rows/features: `{dataset['rows']}` / `{dataset['features']}`",
            f"- history/stability: `{config['history']}` / `{config['stability_history']}`",
            f"- train/cal/test windows: `{audit['windows']['train']}` / `{audit['windows']['calibration']}` / `{audit['windows']['test']}`",
            f"- command change rate: `{fmt(dataset['change_rate'])}`",
            f"- gate threshold: `{fmt(result['gate_threshold'])}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E23 asks whether a label-free temporal gate adds residual policy",
            "value after a trained no-gate MLP has learned command selection",
            "from external sequential robot sensor data.",
            "",
            "This is an imitation/control-label benchmark, not a causal",
            "intervention log.",
            "",
            "## Dataset Audit",
            "",
            "| quantity | value |",
            "| --- | --- |",
            f"| labels | {dataset['labels']} |",
            f"| split bounds | {audit['bounds']} |",
            f"| probe accuracy | {audit['probe_accuracy']} |",
            f"| majority accuracy | {audit['majority_accuracy']} |",
            f"| probe features | {audit['probe_model']} |",
            "",
            "## Main Decision Quantities",
            "",
            "| quantity | value |",
            "| --- | --- |",
        ]
    )
    for key, value in dq.items():
        lines.append(f"| {key.replace('_', ' ')} | {fmt(value)} |")
    lines.extend(
        [
            "",
            "## Split Summary",
            "",
            "| split | episodes | packets | mean utility | mean gate | mean unsafe proxy | optimal actions |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for key in ["train_summary", "calibration_summary", "test_summary"]:
        s = result[key]
        lines.append(
            "| "
            + " | ".join(
                [
                    key.replace("_summary", ""),
                    str(s["episodes"]),
                    str(s["packets"]),
                    fmt(s["mean_utility"]),
                    fmt(s["mean_gate_score"]),
                    fmt(s["mean_unsafe_proxy"]),
                    action_counts(s["optimal_actions"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Model Summary",
            "",
            "| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe wrong | boundary error | row detect | row false |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for name in MODEL_ORDER:
        item = overall[name]
        model = item["model"]
        value = item["value"]
        select = item["select_regression"]
        policy = item["policy"]
        row = item["row_selection"]
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    str(model["feature_count"]),
                    fmt(value["rmse_observed"]),
                    fmt(select["rmse_observed"]),
                    fmt(policy["action_accuracy"]),
                    fmt(policy["mean_regret"]),
                    fmt(policy["p90_regret"]),
                    fmt(policy["unsafe_wrong_proxy"]),
                    fmt(policy["boundary_error"]),
                    fmt(row["optimal_detection"]),
                    fmt(row["nonoptimal_false_admission"]),
                ]
            )
            + " |"
        )
    finding = result["finding"]
    if finding == "EXTERNAL_MLP_ABSORBS_GATE":
        interpretation = [
            "The trained no-gate MLP absorbs the temporal gate on this external",
            "sequential-control anchor.",
        ]
    elif finding == "EXTERNAL_MLP_ABSORBS_GATE_WITH_WEAK_HYBRID_EDGE":
        interpretation = [
            "The hybrid MLP keeps a small edge, but the gain is below the",
            "configured survival margins. This counts as absorption with a",
            "weak hybrid hint rather than a gate residual.",
        ]
    elif finding == "EXTERNAL_GATE_RESIDUAL_SURVIVES_MLP":
        interpretation = [
            "The hybrid MLP beats the no-gate MLP on this external robot",
            "sequence. This is a candidate external gate residual.",
        ]
    elif finding == "EXTERNAL_CONTROL_ANCHOR_TOO_WEAK":
        interpretation = [
            "The Wall-Following command-label task is too weak for the gate",
            "residual question at the configured standard.",
        ]
    else:
        interpretation = ["The external anchor is inconclusive at the configured margins."]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external UCI robot navigation data;",
            "- splits are chronological, not random;",
            "- continuous_mlp has no gate score or gate bit;",
            "- hybrid_mlp has the same architecture plus gate features;",
            "- the gate is calibrated on non-selected calibration command packets;",
            "- unsafe-command is only a proxy derived from command mismatch severity;",
            "- this is command imitation, not causal intervention evidence.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data" / "wall_following_robot_navigation")
    parser.add_argument("--history", type=int, default=5)
    parser.add_argument("--stability-history", type=int, default=7)
    parser.add_argument("--train-fraction", type=float, default=0.60)
    parser.add_argument("--calibration-fraction", type=float, default=0.20)
    parser.add_argument("--probe-ridge", type=float, default=2e-2)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--utility-noise", type=float, default=0.010)
    parser.add_argument("--select-noise", type=float, default=0.018)
    parser.add_argument("--unsafe-penalty", type=float, default=0.35)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--hidden", type=int, nargs="+", default=[80, 40])
    parser.add_argument("--epochs", type=int, default=70)
    parser.add_argument("--batch-size", type=int, default=384)
    parser.add_argument("--lr", type=float, default=0.0025)
    parser.add_argument("--l2", type=float, default=2e-4)
    parser.add_argument("--patience", type=int, default=10)
    parser.add_argument("--min-delta", type=float, default=1e-5)
    parser.add_argument("--history-every", type=int, default=10)
    parser.add_argument("--regret-margin", type=float, default=0.010)
    parser.add_argument("--accuracy-margin", type=float, default=0.010)
    parser.add_argument("--minimum-gain-over-majority", type=float, default=0.030)
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
    json_path = args.report_dir / "e23_external_wall_following_gate_residual_probe.json"
    md_path = args.report_dir / "e23_external_wall_following_gate_residual_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
