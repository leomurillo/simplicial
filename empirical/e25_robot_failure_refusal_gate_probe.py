"""E25 external robot failure/refusal gate probe.

E24 moved from command imitation to external action-outcome traces, but still
found that a trained no-gate MLP absorbed the gate. E25 targets an explicitly
costly failure setting: the UCI Robot Execution Failures data.

Each instance is a 15-step force/torque trace after failure detection in a robot
task phase. We build prefix packets and ask whether the agent should continue
or refuse/recover. The no-gate model is a trained MLP over task and prefix
features. The hybrid model has the same architecture plus a label-free temporal
failure gate.
"""

from __future__ import annotations

import argparse
import json
import math
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

import e22_trained_mlp_closed_loop_probe as e22


DATASET_PAGE = "https://archive.ics.uci.edu/dataset/138/robot+execution+failures"
KDD_PAGE = "https://kdd.ics.uci.edu/databases/robotfailure/robotfailure.html"
BASE_URL = "https://kdd.ics.uci.edu/databases/robotfailure/"
DATA_FILES = ["lp1.data", "lp2.data", "lp3.data", "lp4.data", "lp5.data"]
SAFE_LABELS = {"normal", "ok"}
ACTIONS = ["continue", "refuse_recover"]
PROBLEMS = ["lp1", "lp2", "lp3", "lp4", "lp5"]
MODEL_ORDER = ["scalar_mlp", "continuous_mlp", "hybrid_mlp"]


@dataclass(frozen=True)
class Instance:
    problem: str
    instance_id: int
    label: str
    safe: int
    rows: list[list[float]]


@dataclass(frozen=True)
class PrefixExample:
    split: str
    episode_id: int
    problem: str
    label: str
    safe: int
    prefix_len: int
    features: list[float]
    probe_safe_prob: float
    probe_failure_prob: float
    probe_margin: float
    probe_entropy: float
    anomaly_energy: float
    stability_safe: float
    stability_failure: float


@dataclass(frozen=True)
class Packet:
    split: str
    episode_id: int
    problem: str
    label: str
    safe: int
    action: str
    action_index: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_margin: float
    gate_stability: float
    unsafe_continue: float
    false_refusal: float
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


def parse_file(path: Path, problem: str) -> list[Instance]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    instances: list[Instance] = []
    i = 0
    instance_id = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        label = lines[i].strip()
        i += 1
        rows = []
        for _ in range(15):
            if i >= len(lines):
                break
            rows.append([float(value) for value in lines[i].split()])
            i += 1
        if len(rows) == 15:
            instances.append(
                Instance(
                    problem=problem,
                    instance_id=instance_id,
                    label=label,
                    safe=int(label in SAFE_LABELS),
                    rows=rows,
                )
            )
            instance_id += 1
    return instances


def load_instances(data_dir: Path) -> tuple[list[Instance], dict[str, Any]]:
    paths = download_dataset(data_dir)
    instances: list[Instance] = []
    per_file: dict[str, Any] = {}
    for name, path in paths.items():
        problem = name.split(".", 1)[0]
        local = parse_file(path, problem)
        instances.extend(local)
        per_file[problem] = {
            "path": str(path),
            "bytes": int(path.stat().st_size),
            "instances": int(len(local)),
            "labels": dict(Counter(instance.label for instance in local)),
            "safe": int(sum(instance.safe for instance in local)),
            "failure": int(sum(1 - instance.safe for instance in local)),
        }
    return instances, {
        "files": per_file,
        "instances": int(len(instances)),
        "safe": int(sum(instance.safe for instance in instances)),
        "failure": int(sum(1 - instance.safe for instance in instances)),
        "labels": dict(Counter(instance.label for instance in instances)),
    }


def split_instances(args: argparse.Namespace, instances: list[Instance]) -> dict[str, list[Instance]]:
    groups: dict[tuple[str, int], list[Instance]] = defaultdict(list)
    for instance in instances:
        groups[(instance.problem, instance.safe)].append(instance)
    rng = np.random.default_rng(args.seed + 2525)
    splits = {"train": [], "calibration": [], "test": []}
    for group in groups.values():
        local = list(group)
        rng.shuffle(local)
        n = len(local)
        train_end = int(round(n * args.train_fraction))
        cal_end = int(round(n * (args.train_fraction + args.calibration_fraction)))
        if n >= 3:
            train_end = min(max(train_end, 1), n - 2)
            cal_end = min(max(cal_end, train_end + 1), n - 1)
        splits["train"].extend(local[:train_end])
        splits["calibration"].extend(local[train_end:cal_end])
        splits["test"].extend(local[cal_end:])
    return splits


def problem_bits(problem: str) -> list[float]:
    return [1.0 if problem == item else 0.0 for item in PROBLEMS]


def prefix_features(instance: Instance, prefix_len: int) -> tuple[np.ndarray, float]:
    rows = np.asarray(instance.rows[:prefix_len], dtype=float)
    current = rows[-1]
    first = rows[0]
    delta = current - first
    mean = rows.mean(axis=0)
    sd = rows.std(axis=0)
    minv = rows.min(axis=0)
    maxv = rows.max(axis=0)
    if len(rows) > 1:
        steps = np.diff(rows, axis=0)
        step_mean = steps.mean(axis=0)
        step_abs = np.mean(np.abs(steps), axis=0)
        anomaly_energy = float(np.mean(np.abs(steps)) + 0.02 * np.max(np.abs(delta)))
    else:
        step_mean = np.zeros(rows.shape[1], dtype=float)
        step_abs = np.zeros(rows.shape[1], dtype=float)
        anomaly_energy = 0.0
    features = np.concatenate(
        [
            np.asarray(problem_bits(instance.problem), dtype=float),
            np.asarray([prefix_len / 15.0], dtype=float),
            current,
            delta,
            mean,
            sd,
            minv,
            maxv,
            step_mean,
            step_abs,
            np.asarray([anomaly_energy], dtype=float),
        ]
    )
    return features, anomaly_energy


def one_hot(y: np.ndarray, classes: int) -> np.ndarray:
    out = np.zeros((len(y), classes), dtype=float)
    out[np.arange(len(y)), y] = 1.0
    return out


def softmax(values: np.ndarray) -> np.ndarray:
    centered = values - values.max(axis=1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=1, keepdims=True)


def fit_probe_classifier(x_train: np.ndarray, y_train: np.ndarray, ridge: float) -> dict[str, Any]:
    mean = x_train.mean(axis=0)
    sd = x_train.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x_train - mean) / sd
    design = np.hstack([np.ones((len(z), 1)), z, z * z])
    target = one_hot(y_train, 2)
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


def raw_examples(splits: dict[str, list[Instance]], args: argparse.Namespace) -> dict[str, list[dict[str, Any]]]:
    raw: dict[str, list[dict[str, Any]]] = {}
    for split, instances in splits.items():
        rows = []
        episode = 0
        for instance in instances:
            for prefix_len in args.prefix_lengths:
                features, anomaly_energy = prefix_features(instance, prefix_len)
                rows.append(
                    {
                        "episode_id": episode,
                        "problem": instance.problem,
                        "label": instance.label,
                        "safe": instance.safe,
                        "prefix_len": prefix_len,
                        "features": features,
                        "anomaly_energy": anomaly_energy,
                    }
                )
                episode += 1
        raw[split] = rows
    return raw


def prepare_examples(instances: list[Instance], args: argparse.Namespace) -> tuple[dict[str, list[PrefixExample]], dict[str, Any]]:
    splits = split_instances(args, instances)
    raw = raw_examples(splits, args)
    x_train = np.asarray([row["features"] for row in raw["train"]], dtype=float)
    y_train = np.asarray([row["safe"] for row in raw["train"]], dtype=int)
    probe = fit_probe_classifier(x_train, y_train, args.probe_ridge)
    examples: dict[str, list[PrefixExample]] = {}
    audit = {
        "split_instances": {},
        "prefix_counts": {},
        "probe_accuracy": {},
        "majority_accuracy": {},
        "probe_model": {
            "raw_feature_count": int(x_train.shape[1]),
            "expanded_feature_count": int(len(probe["coef"])),
        },
    }
    for split in ["train", "calibration", "test"]:
        local_instances = splits[split]
        audit["split_instances"][split] = {
            "instances": int(len(local_instances)),
            "safe": int(sum(instance.safe for instance in local_instances)),
            "failure": int(sum(1 - instance.safe for instance in local_instances)),
            "problems": dict(Counter(instance.problem for instance in local_instances)),
            "labels": dict(Counter(instance.label for instance in local_instances)),
        }
        x_split = np.asarray([row["features"] for row in raw[split]], dtype=float)
        y_split = np.asarray([row["safe"] for row in raw[split]], dtype=int)
        probs = predict_probe(probe, x_split)
        pred = np.argmax(probs, axis=1)
        audit["prefix_counts"][split] = int(len(raw[split]))
        audit["probe_accuracy"][split] = float(np.mean(pred == y_split))
        counts = np.bincount(y_split, minlength=2)
        audit["majority_accuracy"][split] = float(counts.max() / counts.sum())
        stability = []
        for i in range(len(raw[split])):
            start = max(0, i - args.stability_history + 1)
            local_pred = pred[start : i + 1]
            stability.append([float(np.mean(local_pred == 0)), float(np.mean(local_pred == 1))])
        split_examples: list[PrefixExample] = []
        for i, row in enumerate(raw[split]):
            safe_prob = float(probs[i, 1])
            fail_prob = float(probs[i, 0])
            margin = abs(safe_prob - fail_prob)
            entropy = float(-np.sum(probs[i] * np.log(probs[i] + 1e-12)) / math.log(2.0))
            split_examples.append(
                PrefixExample(
                    split=split,
                    episode_id=int(row["episode_id"]),
                    problem=str(row["problem"]),
                    label=str(row["label"]),
                    safe=int(row["safe"]),
                    prefix_len=int(row["prefix_len"]),
                    features=[float(v) for v in row["features"]],
                    probe_safe_prob=safe_prob,
                    probe_failure_prob=fail_prob,
                    probe_margin=float(margin),
                    probe_entropy=entropy,
                    anomaly_energy=float(row["anomaly_energy"]),
                    stability_safe=stability[i][1],
                    stability_failure=stability[i][0],
                )
            )
        examples[split] = split_examples
    return examples, audit


def action_bits(action_index: int) -> list[float]:
    return [1.0 if action_index == i else 0.0 for i in range(len(ACTIONS))]


def packet_continuous_features(example: PrefixExample, action_index: int) -> list[float]:
    action = ACTIONS[action_index]
    candidate_prob = example.probe_safe_prob if action == "continue" else example.probe_failure_prob
    candidate_stability = example.stability_safe if action == "continue" else example.stability_failure
    return [
        *action_bits(action_index),
        *example.features,
        example.probe_safe_prob,
        example.probe_failure_prob,
        example.probe_margin,
        example.probe_entropy,
        example.anomaly_energy,
        candidate_prob,
        candidate_stability,
    ]


def collect_packets(examples: list[PrefixExample], args: argparse.Namespace) -> list[Packet]:
    rng = np.random.default_rng(args.seed + {"train": 725, "calibration": 825, "test": 925}[examples[0].split])
    packets: list[Packet] = []
    for example in examples:
        for action_index, action in enumerate(ACTIONS):
            if action == "continue":
                selected = float(example.safe == 1)
                utility = 1.0 if example.safe else -args.unsafe_continue_penalty
                unsafe_continue = float(example.safe == 0)
                false_refusal = 0.0
                candidate_prob = example.probe_safe_prob
                candidate_stability = example.stability_safe
                margin = example.probe_safe_prob - example.probe_failure_prob
            else:
                selected = float(example.safe == 0)
                utility = (1.0 - args.refusal_cost) if not example.safe else -args.false_refusal_penalty
                unsafe_continue = 0.0
                false_refusal = float(example.safe == 1)
                candidate_prob = example.probe_failure_prob
                candidate_stability = example.stability_failure
                margin = example.probe_failure_prob - example.probe_safe_prob
            positive_margin = max(0.0, margin)
            gate_score = (
                candidate_prob
                * positive_margin
                * candidate_stability
                * (1.0 - 0.55 * example.probe_entropy)
                * math.exp(-example.anomaly_energy / args.energy_scale if action == "continue" else 0.0)
            )
            if action == "refuse_recover":
                gate_score *= 1.0 + min(1.0, example.anomaly_energy / args.energy_scale)
            packets.append(
                Packet(
                    split=example.split,
                    episode_id=example.episode_id,
                    problem=example.problem,
                    label=example.label,
                    safe=example.safe,
                    action=action,
                    action_index=action_index,
                    scalar_score=float(candidate_prob),
                    continuous_features=packet_continuous_features(example, action_index),
                    gate_score=float(gate_score),
                    gate_margin=float(margin),
                    gate_stability=float(candidate_stability),
                    unsafe_continue=unsafe_continue,
                    false_refusal=false_refusal,
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
            packet.gate_margin,
            packet.gate_stability,
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
    unsafe_continue = []
    false_refusal = []
    chosen_actions = {action: 0 for action in ACTIONS}
    optimal_actions = {action: 0 for action in ACTIONS}
    for episode_packets in groups.values():
        chosen = max(episode_packets, key=lambda packet: scores[id(packet)])
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        chosen_actions[chosen.action] += 1
        optimal_actions[optimal.action] += 1
        exact.append(float(chosen.action == optimal.action))
        regrets.append(float(optimal.utility_clean - chosen.utility_clean))
        unsafe_continue.append(chosen.unsafe_continue)
        false_refusal.append(chosen.false_refusal)
    return {
        "action_accuracy": float(np.mean(exact)),
        "mean_regret": float(np.mean(regrets)),
        "p90_regret": float(np.quantile(np.asarray(regrets, dtype=float), 0.90, method="higher")),
        "unsafe_continue": float(np.mean(unsafe_continue)),
        "false_refusal": float(np.mean(false_refusal)),
        "chosen_actions": chosen_actions,
        "optimal_actions": optimal_actions,
    }


def summarize_packets(packets: list[Packet]) -> dict[str, Any]:
    groups = group_packets(packets)
    optimal_actions = {action: 0 for action in ACTIONS}
    labels = Counter()
    for episode_packets in groups.values():
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        optimal_actions[optimal.action] += 1
        labels[optimal.label] += 1
    return {
        "episodes": int(len(groups)),
        "packets": int(len(packets)),
        "optimal_actions": optimal_actions,
        "labels": dict(labels),
        "mean_gate_score": float(np.mean([packet.gate_score for packet in packets])),
        "mean_utility": float(np.mean([packet.utility_clean for packet in packets])),
        "mean_unsafe_continue": float(np.mean([packet.unsafe_continue for packet in packets])),
        "mean_false_refusal": float(np.mean([packet.false_refusal for packet in packets])),
    }


def decision_quantities(overall: dict[str, Any]) -> dict[str, float]:
    return {
        "scalar_accuracy": overall["scalar_mlp"]["policy"]["action_accuracy"],
        "continuous_accuracy": overall["continuous_mlp"]["policy"]["action_accuracy"],
        "hybrid_accuracy": overall["hybrid_mlp"]["policy"]["action_accuracy"],
        "scalar_regret": overall["scalar_mlp"]["policy"]["mean_regret"],
        "continuous_regret": overall["continuous_mlp"]["policy"]["mean_regret"],
        "hybrid_regret": overall["hybrid_mlp"]["policy"]["mean_regret"],
        "continuous_unsafe_continue": overall["continuous_mlp"]["policy"]["unsafe_continue"],
        "hybrid_unsafe_continue": overall["hybrid_mlp"]["policy"]["unsafe_continue"],
        "continuous_false_refusal": overall["continuous_mlp"]["policy"]["false_refusal"],
        "hybrid_false_refusal": overall["hybrid_mlp"]["policy"]["false_refusal"],
        "continuous_select_rmse": overall["continuous_mlp"]["select_regression"]["rmse_observed"],
        "hybrid_select_rmse": overall["hybrid_mlp"]["select_regression"]["rmse_observed"],
    }


def classify_finding(args: argparse.Namespace, audit: dict[str, Any], dq: dict[str, float]) -> str:
    majority = audit["majority_accuracy"]["test"]
    if dq["continuous_accuracy"] < majority + args.minimum_gain_over_majority:
        return "ROBOT_FAILURE_REFUSAL_ANCHOR_TOO_WEAK"
    weak_hybrid_safety = (
        dq["hybrid_unsafe_continue"] < dq["continuous_unsafe_continue"]
        and dq["hybrid_regret"] <= dq["continuous_regret"] + args.regret_margin
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
        return "ROBOT_FAILURE_REFUSAL_GATE_SURVIVES_MLP"
    if continuous_absorbs and weak_hybrid_safety:
        return "ROBOT_FAILURE_MLP_ABSORBS_GATE_WITH_SAFETY_HINT"
    if continuous_absorbs:
        return "ROBOT_FAILURE_MLP_ABSORBS_GATE"
    return "ROBOT_FAILURE_REFUSAL_INCONCLUSIVE"


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    instances, dataset_meta = load_instances(args.data_dir)
    examples, audit = prepare_examples(instances, args)
    train = collect_packets(examples["train"], args)
    cal = collect_packets(examples["calibration"], args)
    test = collect_packets(examples["test"], args)
    gate_threshold = calibrate_gate(cal, args.alpha)
    overall = {
        "scalar_mlp": train_and_score_mlp(train, cal, test, "scalar_mlp", "scalar", gate_threshold, args, 4250),
        "continuous_mlp": train_and_score_mlp(train, cal, test, "continuous_mlp", "continuous", gate_threshold, args, 4350),
        "hybrid_mlp": train_and_score_mlp(train, cal, test, "hybrid_mlp", "hybrid", gate_threshold, args, 4450),
    }
    dq = decision_quantities(overall)
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "UCI Robot Execution Failures",
            "page": DATASET_PAGE,
            "kdd_page": KDD_PAGE,
            "base_url": BASE_URL,
            **dataset_meta,
        },
        "config": {
            "seed": args.seed,
            "prefix_lengths": args.prefix_lengths,
            "stability_history": args.stability_history,
            "train_fraction": args.train_fraction,
            "calibration_fraction": args.calibration_fraction,
            "alpha": args.alpha,
            "hidden": args.hidden,
            "epochs": args.epochs,
            "patience": args.patience,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "unsafe_continue_penalty": args.unsafe_continue_penalty,
            "false_refusal_penalty": args.false_refusal_penalty,
            "refusal_cost": args.refusal_cost,
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
    return ", ".join(f"{action}:{counts.get(action, 0)}" for action in ACTIONS)


def write_report(path: Path, result: dict[str, Any]) -> None:
    dataset = result["dataset"]
    audit = result["audit"]
    config = result["config"]
    overall = result["overall"]
    dq = result["decision_quantities"]
    lines: list[str] = []
    lines.extend(
        [
            "# E25 Robot Failure Refusal Gate Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{dataset['name']}`",
            f"- dataset page: `{dataset['page']}`",
            f"- KDD page: `{dataset['kdd_page']}`",
            f"- instances safe/failure: `{dataset['safe']}` / `{dataset['failure']}`",
            f"- prefix lengths: `{config['prefix_lengths']}`",
            f"- gate threshold: `{fmt(result['gate_threshold'])}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E25 asks whether a label-free failure/refusal gate adds residual",
            "policy value after a trained no-gate MLP sees force/torque",
            "prefixes from external robot execution failures.",
            "",
            "## Dataset Audit",
            "",
            "| quantity | value |",
            "| --- | --- |",
            f"| files | {dataset['files']} |",
            f"| labels | {dataset['labels']} |",
            f"| split instances | {audit['split_instances']} |",
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
            "| split | episodes | packets | mean utility | mean gate | unsafe continue | false refusal | optimal actions |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
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
                    fmt(s["mean_unsafe_continue"]),
                    fmt(s["mean_false_refusal"]),
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
            "| model | features | value RMSE | select RMSE | action acc | regret | p90 regret | unsafe continue | false refusal | row detect | row false |",
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
                    fmt(policy["unsafe_continue"]),
                    fmt(policy["false_refusal"]),
                    fmt(row["optimal_detection"]),
                    fmt(row["nonoptimal_false_admission"]),
                ]
            )
            + " |"
        )
    finding = result["finding"]
    if finding == "ROBOT_FAILURE_REFUSAL_GATE_SURVIVES_MLP":
        interpretation = [
            "The hybrid refusal gate beats the no-gate MLP on external robot",
            "failure traces. This is a candidate failure-cost gate residual.",
        ]
    elif finding == "ROBOT_FAILURE_MLP_ABSORBS_GATE_WITH_SAFETY_HINT":
        interpretation = [
            "The trained no-gate MLP absorbs the gate on the primary metrics,",
            "but the hybrid keeps a small unsafe-continue safety hint.",
        ]
    elif finding == "ROBOT_FAILURE_MLP_ABSORBS_GATE":
        interpretation = ["The trained no-gate MLP absorbs the failure/refusal gate."]
    elif finding == "ROBOT_FAILURE_REFUSAL_ANCHOR_TOO_WEAK":
        interpretation = ["The failure/refusal anchor is too weak at the configured standard."]
    else:
        interpretation = ["The failure/refusal gate probe is inconclusive."]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external robot execution failure data;",
            "- normal/ok labels define continue; every other label defines refuse/recover;",
            "- splits are by instance, not by prefix;",
            "- continuous_mlp receives no gate score or gate bit;",
            "- hybrid_mlp has the same architecture plus gate features;",
            "- refusal utility includes explicit unsafe-continue and false-refusal costs;",
            "- failure cost is still a proxy over labels, not a measured reward.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data" / "robot_execution_failures")
    parser.add_argument("--prefix-lengths", type=int, nargs="+", default=[3, 6, 9, 12, 15])
    parser.add_argument("--stability-history", type=int, default=7)
    parser.add_argument("--train-fraction", type=float, default=0.60)
    parser.add_argument("--calibration-fraction", type=float, default=0.20)
    parser.add_argument("--probe-ridge", type=float, default=2e-2)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--energy-scale", type=float, default=9.0)
    parser.add_argument("--utility-noise", type=float, default=0.010)
    parser.add_argument("--select-noise", type=float, default=0.018)
    parser.add_argument("--unsafe-continue-penalty", type=float, default=1.00)
    parser.add_argument("--false-refusal-penalty", type=float, default=0.25)
    parser.add_argument("--refusal-cost", type=float, default=0.08)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--hidden", type=int, nargs="+", default=[72, 36])
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
    json_path = args.report_dir / "e25_robot_failure_refusal_gate_probe.json"
    md_path = args.report_dir / "e25_robot_failure_refusal_gate_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
