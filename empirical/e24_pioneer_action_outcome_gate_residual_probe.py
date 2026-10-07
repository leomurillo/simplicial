"""E24 Pioneer-1 action-outcome gate-residual probe.

E23 used external robot command imitation. E24 moves to the UCI KDD Pioneer-1
data, where each trace is an "experience" in which the robot takes an action
and undergoes a controlled interaction with the environment.

We focus on move and turn experiences. From prefixes of each experience, the
models predict the final qualitative outcome:

    clear_visible, obstructed, discover, vanish, push

The no-gate model is a trained MLP over action and prefix sensor features. The
hybrid model has the same architecture plus label-free temporal gate features
derived from candidate outcome stability and confidence. Trials, not rows, are
split by action family so prefixes from the same experience never cross splits.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

import e22_trained_mlp_closed_loop_probe as e22


DATASET_PAGE = "https://kdd.ics.uci.edu/databases/pioneer/pioneer.html"
DESCRIPTION_PAGE = "https://kdd.ics.uci.edu/databases/pioneer/pioneer.data.html"
BASE_URL = "https://kdd.ics.uci.edu/databases/pioneer/"
DATA_FILES = ["move.data.gz", "turn.data.gz"]
OUTCOMES = ["clear_visible", "obstructed", "discover", "vanish", "push"]
OUTCOME_TO_INDEX = {name: i for i, name in enumerate(OUTCOMES)}
MODEL_ORDER = ["scalar_mlp", "continuous_mlp", "hybrid_mlp"]
ACTION_FAMILIES = ["move", "retr", "turn"]


@dataclass(frozen=True)
class Trial:
    trial_id: str
    file_kind: str
    description: str
    action_family: str
    signed_speed: float
    outcome: str
    rows: list[list[float]]


@dataclass(frozen=True)
class PrefixExample:
    split: str
    episode_id: int
    trial_id: str
    file_kind: str
    label: int
    progress: float
    action_features: list[float]
    prefix_features: list[float]
    probe_probs: list[float]
    probe_pred: int
    probe_top: float
    probe_margin: float
    probe_entropy: float
    stability: list[float]
    effect_energy: float


@dataclass(frozen=True)
class Packet:
    split: str
    episode_id: int
    trial_id: str
    label: int
    candidate: str
    candidate_index: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_stability: float
    gate_margin: float
    unsafe_proxy: float
    utility_clean: float
    utility_observed: float
    target_select_clean: float
    target_select_observed: float


def download_dataset(data_dir: Path) -> dict[str, Path]:
    data_dir.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    for name in DATA_FILES:
        path = data_dir / name
        if not path.exists():
            urllib.request.urlretrieve(BASE_URL + name, path)
        paths[name] = path
    return paths


def parse_action(description: str, file_kind: str) -> tuple[str, float]:
    if file_kind == "turn":
        match = re.search(r"turn(-?\d+)", description)
        if match:
            return "turn", float(match.group(1))
        return "turn", 0.0
    if "retr-" in description:
        match = re.search(r"retr-(\d+)", description)
        return "retr", -float(match.group(1)) if match else -100.0
    match = re.search(r"move(\d+)", description)
    return "move", float(match.group(1)) if match else 100.0


def parse_outcome(description: str) -> str:
    if ".P" in description:
        return "push"
    if ".D" in description:
        return "discover"
    if ".V" in description:
        return "vanish"
    if description.startswith("o-"):
        return "obstructed"
    return "clear_visible"


def load_trials(data_dir: Path) -> tuple[list[Trial], dict[str, Any]]:
    paths = download_dataset(data_dir)
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    row_counts = {}
    for filename, path in paths.items():
        file_kind = filename.split(".", 1)[0]
        rows_seen = 0
        with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as raw:
            for row in csv.reader(raw):
                if not row:
                    continue
                trial_id = row[0]
                description = row[1]
                values = [float(v) for v in row[2:]]
                key = (file_kind, trial_id)
                if key not in grouped:
                    action_family, signed_speed = parse_action(description, file_kind)
                    grouped[key] = {
                        "trial_id": trial_id,
                        "file_kind": file_kind,
                        "description": description,
                        "action_family": action_family,
                        "signed_speed": signed_speed,
                        "outcome": parse_outcome(description),
                        "rows": [],
                    }
                grouped[key]["rows"].append(values)
                rows_seen += 1
        row_counts[filename] = rows_seen

    trials = [
        Trial(
            trial_id=str(item["trial_id"]),
            file_kind=str(item["file_kind"]),
            description=str(item["description"]),
            action_family=str(item["action_family"]),
            signed_speed=float(item["signed_speed"]),
            outcome=str(item["outcome"]),
            rows=item["rows"],
        )
        for item in grouped.values()
    ]
    trials.sort(key=lambda trial: (0 if trial.file_kind == "move" else 1, int(re.search(r"T(\d+)", trial.trial_id).group(1))))
    meta = {
        "files": {name: str(path) for name, path in paths.items()},
        "file_sizes": {name: int(path.stat().st_size) for name, path in paths.items()},
        "row_counts": row_counts,
        "trial_count": int(len(trials)),
        "outcome_trials": dict(Counter(trial.outcome for trial in trials)),
        "outcome_rows": dict(Counter(trial.outcome for trial in trials for _ in trial.rows)),
        "action_families": dict(Counter(trial.action_family for trial in trials)),
        "rows_per_trial": {
            "min": int(min(len(trial.rows) for trial in trials)),
            "max": int(max(len(trial.rows) for trial in trials)),
            "mean": float(np.mean([len(trial.rows) for trial in trials])),
        },
    }
    return trials, meta


def split_trials(args: argparse.Namespace, trials: list[Trial]) -> dict[str, list[Trial]]:
    by_kind: dict[str, list[Trial]] = defaultdict(list)
    for trial in trials:
        by_kind[trial.file_kind].append(trial)
    splits = {"train": [], "calibration": [], "test": []}
    if args.split_strategy == "chronological":
        split_groups = list(by_kind.values())
    elif args.split_strategy == "stratified":
        by_group: dict[tuple[str, str], list[Trial]] = defaultdict(list)
        for trial in trials:
            by_group[(trial.file_kind, trial.outcome)].append(trial)
        rng = np.random.default_rng(args.seed + 2424)
        split_groups = []
        for group in by_group.values():
            local = list(group)
            rng.shuffle(local)
            split_groups.append(local)
    else:
        raise ValueError(f"unknown split strategy: {args.split_strategy}")

    for kind_trials in split_groups:
        n = len(kind_trials)
        train_end = int(round(n * args.train_fraction))
        cal_end = int(round(n * (args.train_fraction + args.calibration_fraction)))
        if n >= 3:
            train_end = min(max(train_end, 1), n - 2)
            cal_end = min(max(cal_end, train_end + 1), n - 1)
        splits["train"].extend(kind_trials[:train_end])
        splits["calibration"].extend(kind_trials[train_end:cal_end])
        splits["test"].extend(kind_trials[cal_end:])
    return splits


def action_features(trial: Trial) -> np.ndarray:
    file_bit = [1.0 if trial.file_kind == kind else 0.0 for kind in ["move", "turn"]]
    family_bit = [1.0 if trial.action_family == family else 0.0 for family in ACTION_FAMILIES]
    return np.asarray([*file_bit, *family_bit, trial.signed_speed / 250.0, abs(trial.signed_speed) / 250.0], dtype=float)


def prefix_feature_vector(rows: np.ndarray, end: int, action: np.ndarray) -> tuple[np.ndarray, float]:
    prefix = rows[: end + 1]
    first = prefix[0]
    current = prefix[-1]
    mean = prefix.mean(axis=0)
    sd = prefix.std(axis=0)
    minv = prefix.min(axis=0)
    maxv = prefix.max(axis=0)
    delta = current - first
    if len(prefix) > 1:
        step = np.diff(prefix, axis=0)
        step_mean = step.mean(axis=0)
        energy = float(np.mean(np.abs(step)))
    else:
        step_mean = np.zeros_like(current)
        energy = 0.0
    return np.concatenate([action, current, delta, mean, sd, minv, maxv, step_mean]), energy


def make_raw_examples(trial_splits: dict[str, list[Trial]], args: argparse.Namespace) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    raw: dict[str, list[dict[str, Any]]] = {}
    audit = {"split_trials": {}, "prefix_counts": {}}
    for split, trials in trial_splits.items():
        rows = []
        audit["split_trials"][split] = {
            "trials": int(len(trials)),
            "outcomes": dict(Counter(trial.outcome for trial in trials)),
            "action_families": dict(Counter(trial.action_family for trial in trials)),
        }
        episode = 0
        for trial in trials:
            data = np.asarray(trial.rows, dtype=float)
            act = action_features(trial)
            start = min(args.min_prefix, len(data) - 1)
            for end in range(start, len(data), args.prefix_stride):
                features, energy = prefix_feature_vector(data, end, act)
                rows.append(
                    {
                        "episode_id": episode,
                        "trial_id": trial.trial_id,
                        "file_kind": trial.file_kind,
                        "label": OUTCOME_TO_INDEX[trial.outcome],
                        "progress": float((end + 1) / len(data)),
                        "action_features": act,
                        "prefix_features": features,
                        "effect_energy": energy,
                    }
                )
                episode += 1
        raw[split] = rows
        audit["prefix_counts"][split] = int(len(rows))
    return raw, audit


def softmax(values: np.ndarray) -> np.ndarray:
    centered = values - values.max(axis=1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=1, keepdims=True)


def one_hot(y: np.ndarray, classes: int) -> np.ndarray:
    out = np.zeros((len(y), classes), dtype=float)
    out[np.arange(len(y)), y] = 1.0
    return out


def fit_probe_classifier(x_train: np.ndarray, y_train: np.ndarray, ridge: float) -> dict[str, Any]:
    mean = x_train.mean(axis=0)
    sd = x_train.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x_train - mean) / sd
    design = np.hstack([np.ones((len(z), 1)), z, z * z])
    target = one_hot(y_train, len(OUTCOMES))
    penalty = ridge * np.eye(design.shape[1])
    penalty[0, 0] = 0.0
    lhs = design.T @ design + penalty
    rhs = design.T @ target
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return {"mean": mean.tolist(), "sd": sd.tolist(), "coef": coef.tolist()}


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


def stability_by_trial(rows: list[dict[str, Any]], preds: np.ndarray, args: argparse.Namespace) -> list[list[float]]:
    trial_positions: dict[str, list[int]] = defaultdict(list)
    for i, row in enumerate(rows):
        trial_positions[row["trial_id"]].append(i)
    stability = [[0.0 for _ in OUTCOMES] for _ in rows]
    for positions in trial_positions.values():
        for local, pos in enumerate(positions):
            previous = positions[max(0, local - args.stability_history + 1) : local + 1]
            local_preds = preds[previous]
            for k in range(len(OUTCOMES)):
                stability[pos][k] = float(np.mean(local_preds == k))
    return stability


def prepare_examples(trials: list[Trial], args: argparse.Namespace) -> tuple[dict[str, list[PrefixExample]], dict[str, Any]]:
    splits = split_trials(args, trials)
    raw, audit = make_raw_examples(splits, args)
    x_train = np.asarray([row["prefix_features"] for row in raw["train"]], dtype=float)
    y_train = np.asarray([row["label"] for row in raw["train"]], dtype=int)
    probe = fit_probe_classifier(x_train, y_train, args.probe_ridge)

    examples: dict[str, list[PrefixExample]] = {}
    audit["probe_accuracy"] = {}
    audit["majority_accuracy"] = {}
    audit["probe_model"] = {
        "raw_feature_count": int(x_train.shape[1]),
        "expanded_feature_count": int(len(probe["coef"])),
    }
    for split in ["train", "calibration", "test"]:
        x_split = np.asarray([row["prefix_features"] for row in raw[split]], dtype=float)
        y_split = np.asarray([row["label"] for row in raw[split]], dtype=int)
        probs = predict_probe(probe, x_split)
        pred, top, margin, entropy = summarize_probs(probs)
        stability = stability_by_trial(raw[split], pred, args)
        counts = np.bincount(y_split, minlength=len(OUTCOMES))
        audit["majority_accuracy"][split] = float(counts.max() / counts.sum())
        audit["probe_accuracy"][split] = float(np.mean(pred == y_split))
        split_examples: list[PrefixExample] = []
        for i, row in enumerate(raw[split]):
            split_examples.append(
                PrefixExample(
                    split=split,
                    episode_id=int(row["episode_id"]),
                    trial_id=str(row["trial_id"]),
                    file_kind=str(row["file_kind"]),
                    label=int(row["label"]),
                    progress=float(row["progress"]),
                    action_features=[float(v) for v in row["action_features"]],
                    prefix_features=[float(v) for v in row["prefix_features"]],
                    probe_probs=[float(v) for v in probs[i]],
                    probe_pred=int(pred[i]),
                    probe_top=float(top[i]),
                    probe_margin=float(margin[i]),
                    probe_entropy=float(entropy[i]),
                    stability=stability[i],
                    effect_energy=float(row["effect_energy"]),
                )
            )
        examples[split] = split_examples
    return examples, audit


def outcome_bits(index: int) -> list[float]:
    return [1.0 if index == i else 0.0 for i in range(len(OUTCOMES))]


def unsafe_proxy(candidate: int, true_label: int) -> float:
    if candidate == true_label:
        return 0.0
    candidate_name = OUTCOMES[candidate]
    true_name = OUTCOMES[true_label]
    if candidate_name == "clear_visible" and true_name in {"push", "obstructed"}:
        return 1.0
    if candidate_name in {"push", "obstructed"} and true_name == "clear_visible":
        return 0.8
    if {candidate_name, true_name} == {"discover", "vanish"}:
        return 0.6
    return 0.35


def packet_continuous_features(example: PrefixExample, candidate: int) -> list[float]:
    probs = np.asarray(example.probe_probs, dtype=float)
    candidate_prob = float(probs[candidate])
    other_max = float(np.max(np.delete(probs, candidate)))
    candidate_margin = candidate_prob - other_max
    return [
        *outcome_bits(candidate),
        *example.prefix_features,
        *example.probe_probs,
        example.probe_top,
        example.probe_margin,
        example.probe_entropy,
        candidate_prob,
        candidate_margin,
        example.progress,
        example.effect_energy,
    ]


def collect_packets(examples: list[PrefixExample], args: argparse.Namespace) -> list[Packet]:
    rng = np.random.default_rng(args.seed + {"train": 610, "calibration": 710, "test": 810}[examples[0].split])
    packets: list[Packet] = []
    for example in examples:
        probs = np.asarray(example.probe_probs, dtype=float)
        for candidate, outcome in enumerate(OUTCOMES):
            candidate_prob = float(probs[candidate])
            other_max = float(np.max(np.delete(probs, candidate)))
            margin = candidate_prob - other_max
            positive_margin = max(0.0, margin)
            stability = float(example.stability[candidate])
            gate_score = (
                candidate_prob
                * positive_margin
                * stability
                * (1.0 - 0.55 * example.probe_entropy)
                * math.exp(-example.effect_energy / args.energy_scale)
            )
            selected = float(candidate == example.label)
            unsafe = unsafe_proxy(candidate, example.label)
            utility = selected - args.unsafe_penalty * unsafe
            packets.append(
                Packet(
                    split=example.split,
                    episode_id=example.episode_id,
                    trial_id=example.trial_id,
                    label=example.label,
                    candidate=outcome,
                    candidate_index=candidate,
                    scalar_score=candidate_prob,
                    continuous_features=packet_continuous_features(example, candidate),
                    gate_score=float(gate_score),
                    gate_stability=stability,
                    gate_margin=float(margin),
                    unsafe_proxy=float(unsafe),
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
        return [packet.scalar_score, packet.gate_margin, *outcome_bits(packet.candidate_index)]
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
    unsafe_wrong = []
    severe_miss = []
    chosen = {outcome: 0 for outcome in OUTCOMES}
    optimal_counts = {outcome: 0 for outcome in OUTCOMES}
    for episode_packets in groups.values():
        chosen_packet = max(episode_packets, key=lambda packet: scores[id(packet)])
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        chosen[chosen_packet.candidate] += 1
        optimal_counts[optimal.candidate] += 1
        exact.append(float(chosen_packet.candidate_index == optimal.candidate_index))
        regrets.append(float(optimal.utility_clean - chosen_packet.utility_clean))
        unsafe_wrong.append(float(chosen_packet.unsafe_proxy >= 0.8 and chosen_packet.candidate_index != optimal.candidate_index))
        severe_miss.append(float(chosen_packet.candidate == "clear_visible" and OUTCOMES[optimal.candidate_index] in {"push", "obstructed"}))
    return {
        "action_accuracy": float(np.mean(exact)),
        "mean_regret": float(np.mean(regrets)),
        "p90_regret": float(np.quantile(np.asarray(regrets, dtype=float), 0.90, method="higher")),
        "unsafe_wrong_proxy": float(np.mean(unsafe_wrong)),
        "severe_miss_proxy": float(np.mean(severe_miss)),
        "chosen_actions": chosen,
        "optimal_actions": optimal_counts,
    }


def summarize_packets(packets: list[Packet]) -> dict[str, Any]:
    groups = group_packets(packets)
    optimal_counts = {outcome: 0 for outcome in OUTCOMES}
    for episode_packets in groups.values():
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        optimal_counts[optimal.candidate] += 1
    return {
        "episodes": int(len(groups)),
        "packets": int(len(packets)),
        "optimal_actions": optimal_counts,
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
        "continuous_severe_miss": overall["continuous_mlp"]["policy"]["severe_miss_proxy"],
        "hybrid_severe_miss": overall["hybrid_mlp"]["policy"]["severe_miss_proxy"],
        "continuous_select_rmse": overall["continuous_mlp"]["select_regression"]["rmse_observed"],
        "hybrid_select_rmse": overall["hybrid_mlp"]["select_regression"]["rmse_observed"],
    }


def classify_finding(args: argparse.Namespace, audit: dict[str, Any], dq: dict[str, float]) -> str:
    majority = audit["majority_accuracy"]["test"]
    if dq["continuous_accuracy"] < majority + args.minimum_gain_over_majority:
        return "PIONEER_ACTION_OUTCOME_ANCHOR_TOO_WEAK"
    weak_hybrid_edge = (
        dq["hybrid_regret"] < dq["continuous_regret"]
        and dq["hybrid_accuracy"] > dq["continuous_accuracy"]
        and dq["hybrid_unsafe_wrong"] <= dq["continuous_unsafe_wrong"]
    )
    continuous_absorbs = (
        dq["continuous_regret"] <= dq["hybrid_regret"] + args.regret_margin
        and dq["continuous_accuracy"] >= dq["hybrid_accuracy"] - args.accuracy_margin
    )
    hybrid_survives = (
        dq["hybrid_regret"] + args.regret_margin < dq["continuous_regret"]
        and dq["hybrid_accuracy"] > dq["continuous_accuracy"] + args.accuracy_margin
    )
    if hybrid_survives:
        return "PIONEER_GATE_RESIDUAL_SURVIVES_MLP"
    if continuous_absorbs and weak_hybrid_edge:
        return "PIONEER_MLP_ABSORBS_GATE_WITH_WEAK_HYBRID_EDGE"
    if continuous_absorbs:
        return "PIONEER_MLP_ABSORBS_GATE"
    return "PIONEER_ACTION_OUTCOME_INCONCLUSIVE"


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    trials, dataset_meta = load_trials(args.data_dir)
    examples, audit = prepare_examples(trials, args)
    train = collect_packets(examples["train"], args)
    cal = collect_packets(examples["calibration"], args)
    test = collect_packets(examples["test"], args)
    gate_threshold = calibrate_gate(cal, args.alpha)
    overall = {
        "scalar_mlp": train_and_score_mlp(train, cal, test, "scalar_mlp", "scalar", gate_threshold, args, 3300),
        "continuous_mlp": train_and_score_mlp(train, cal, test, "continuous_mlp", "continuous", gate_threshold, args, 3400),
        "hybrid_mlp": train_and_score_mlp(train, cal, test, "hybrid_mlp", "hybrid", gate_threshold, args, 3500),
    }
    dq = decision_quantities(overall)
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "UCI KDD Pioneer-1 Mobile Robot Data",
            "page": DATASET_PAGE,
            "description_page": DESCRIPTION_PAGE,
            "base_url": BASE_URL,
            **dataset_meta,
        },
        "config": {
            "seed": args.seed,
            "min_prefix": args.min_prefix,
            "prefix_stride": args.prefix_stride,
            "stability_history": args.stability_history,
            "split_strategy": args.split_strategy,
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


def counts_text(counts: dict[str, int]) -> str:
    return ", ".join(f"{name}:{counts.get(name, 0)}" for name in OUTCOMES)


def write_report(path: Path, result: dict[str, Any]) -> None:
    dataset = result["dataset"]
    config = result["config"]
    audit = result["audit"]
    overall = result["overall"]
    dq = result["decision_quantities"]
    lines: list[str] = []
    lines.extend(
        [
            "# E24 Pioneer Action-Outcome Gate-Residual Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{dataset['name']}`",
            f"- dataset page: `{dataset['page']}`",
            f"- description page: `{dataset['description_page']}`",
            f"- trials/files: `{dataset['trial_count']}` / `{DATA_FILES}`",
            f"- rows per trial: `{dataset['rows_per_trial']}`",
            f"- split strategy: `{config['split_strategy']}`",
            f"- min prefix / stride: `{config['min_prefix']}` / `{config['prefix_stride']}`",
            f"- gate threshold: `{fmt(result['gate_threshold'])}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E24 asks whether a label-free temporal gate adds residual value",
            "after a trained no-gate MLP learns qualitative action outcomes",
            "from external Pioneer-1 robot experiences.",
            "",
            "## Dataset Audit",
            "",
            "| quantity | value |",
            "| --- | --- |",
            f"| outcome trials | {dataset['outcome_trials']} |",
            f"| outcome rows | {dataset['outcome_rows']} |",
            f"| action families | {dataset['action_families']} |",
            f"| split trials | {audit['split_trials']} |",
            f"| prefix counts | {audit['prefix_counts']} |",
            f"| probe accuracy | {audit['probe_accuracy']} |",
            f"| majority accuracy | {audit['majority_accuracy']} |",
            f"| probe model | {audit['probe_model']} |",
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
            "| split | episodes | packets | mean utility | mean gate | mean unsafe proxy | optimal outcomes |",
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
                    counts_text(s["optimal_actions"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Model Summary",
            "",
            "| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe wrong | severe miss | row detect | row false |",
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
                    fmt(policy["severe_miss_proxy"]),
                    fmt(row["optimal_detection"]),
                    fmt(row["nonoptimal_false_admission"]),
                ]
            )
            + " |"
        )
    finding = result["finding"]
    if finding == "PIONEER_GATE_RESIDUAL_SURVIVES_MLP":
        interpretation = [
            "The hybrid MLP beats the no-gate MLP on external Pioneer-1",
            "action-outcome traces. This is a candidate external gate residual.",
        ]
    elif finding == "PIONEER_MLP_ABSORBS_GATE_WITH_WEAK_HYBRID_EDGE":
        interpretation = [
            "The hybrid MLP keeps a small edge, but the gain is below the",
            "configured survival margins. This is absorption with a weak",
            "hybrid hint, not a clean gate residual.",
        ]
    elif finding == "PIONEER_MLP_ABSORBS_GATE":
        interpretation = ["The trained no-gate MLP absorbs the temporal gate on Pioneer-1 outcomes."]
    elif finding == "PIONEER_ACTION_OUTCOME_ANCHOR_TOO_WEAK":
        interpretation = ["The Pioneer-1 target is too weak at the configured standard."]
    else:
        interpretation = ["The external action-outcome anchor is inconclusive."]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external UCI KDD Pioneer-1 robot experience data;",
            "- splits are by trial, not by row;",
            "- the default split is stratified by file and outcome to keep rare outcomes represented;",
            "- outcome markers are used only as targets, not predictor features;",
            "- continuous_mlp receives no gate score or gate bit;",
            "- hybrid_mlp has the same architecture plus gate features;",
            "- the outcome utility is a proxy over qualitative descriptions, not a measured reward.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data" / "pioneer_robot")
    parser.add_argument("--min-prefix", type=int, default=8)
    parser.add_argument("--prefix-stride", type=int, default=3)
    parser.add_argument("--stability-history", type=int, default=5)
    parser.add_argument("--split-strategy", choices=["stratified", "chronological"], default="stratified")
    parser.add_argument("--train-fraction", type=float, default=0.60)
    parser.add_argument("--calibration-fraction", type=float, default=0.20)
    parser.add_argument("--probe-ridge", type=float, default=3e-2)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--energy-scale", type=float, default=45.0)
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
    json_path = args.report_dir / "e24_pioneer_action_outcome_gate_residual_probe.json"
    md_path = args.report_dir / "e24_pioneer_action_outcome_gate_residual_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
