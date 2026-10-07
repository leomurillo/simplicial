"""E19 selective PenDigits glimpse probe.

E19 moves from "request more" to "choose where to sample." From the first two
PenDigits trajectory points, the agent may either commit or inspect one future
point. Each sample action changes which evidence arrives.

The probe compares:

    - continuous action-value fields over candidate action packets;
    - a conformal action-admission gate over label-free packet confidence;
    - governed/hybrid policies that combine both.

The main metric is not just row-wise prediction. For each trajectory the model
must pick one action packet, and we score action accuracy and regret.
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


ACTIONS = ["commit", "p3", "p4", "p5", "p6", "p7", "p8"]
SAMPLE_ACTIONS = ["p3", "p4", "p5", "p6", "p7", "p8"]
ACTION_TO_POINT = {f"p{i}": i for i in range(3, 9)}
MODEL_ORDER = ["scalar", "continuous_action_value", "conformal_action_gate", "governed_action", "hybrid_full"]
DIGITS = list(range(10))


@dataclass(frozen=True)
class Packet:
    split: str
    episode_id: int
    label: int
    action: str
    early_pred: int
    packet_pred: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_margin: float
    gate_entropy: float
    action_cost: float
    utility_clean: float
    utility_observed: float
    target_select_clean: float
    target_select_observed: float


@dataclass(frozen=True)
class Classifier:
    kind: str
    point: int
    coef: list[list[float]]
    mean: list[float]
    sd: list[float]


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


def action_index(action: str) -> int:
    return ACTIONS.index(action)


def action_cost(action: str, base_cost: float, distance_cost: float) -> float:
    if action == "commit":
        return 0.0
    return base_cost + distance_cost * (ACTION_TO_POINT[action] - 2)


def packet_input(x: np.ndarray, early_points: int, action: str) -> np.ndarray:
    early = e17.prefix(x, early_points)
    if action == "commit":
        return early
    point = ACTION_TO_POINT[action]
    coords = x[:, 2 * (point - 1) : 2 * point]
    return np.hstack([early, coords])


def fit_packet_classifier(
    x: np.ndarray,
    y: np.ndarray,
    early_points: int,
    action: str,
    ridge: float,
) -> Classifier:
    xp = packet_input(x, early_points, action)
    mean = xp.mean(axis=0)
    sd = xp.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (xp - mean) / sd
    design = np.hstack([np.ones((z.shape[0], 1)), z])
    target = e17.one_hot(y)
    penalty = ridge * np.eye(design.shape[1])
    penalty[0, 0] = 0.0
    lhs = design.T @ design + penalty
    rhs = design.T @ target
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return Classifier(
        kind=action,
        point=ACTION_TO_POINT.get(action, early_points),
        coef=[[float(v) for v in row] for row in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
    )


def classifier_logits(model: Classifier, x: np.ndarray, early_points: int, action: str) -> np.ndarray:
    xp = packet_input(x, early_points, action)
    mean = np.asarray(model.mean, dtype=float)
    sd = np.asarray(model.sd, dtype=float)
    coef = np.asarray(model.coef, dtype=float)
    z = (xp - mean) / sd
    design = np.hstack([np.ones((z.shape[0], 1)), z])
    return design @ coef


def predict_proba(model: Classifier, x: np.ndarray, early_points: int, action: str) -> np.ndarray:
    return e17.softmax(classifier_logits(model, x, early_points, action))


def action_one_hot(action: str) -> list[float]:
    return [1.0 if action == item else 0.0 for item in ACTIONS]


def digit_vector(digit: int) -> list[float]:
    return [1.0 if digit == item else 0.0 for item in DIGITS]


def action_geometry(x: np.ndarray, early_points: int, action: str) -> np.ndarray:
    if action == "commit":
        return np.zeros((len(x), 6), dtype=float)
    point = ACTION_TO_POINT[action]
    coords = x[:, 2 * (point - 1) : 2 * point]
    last_early = x[:, 2 * (early_points - 1) : 2 * early_points]
    delta = coords - last_early
    dist = np.sqrt((delta * delta).sum(axis=1))
    return np.hstack(
        [
            coords,
            delta,
            dist[:, None],
            np.full((len(x), 1), (point - early_points) / 6.0),
        ]
    )


def collect_packets(
    split: str,
    x: np.ndarray,
    y: np.ndarray,
    classifiers: dict[str, Classifier],
    early_points: int,
    base_cost: float,
    distance_cost: float,
    utility_noise: float,
    select_noise: float,
    rng: np.random.Generator,
) -> list[Packet]:
    early_probs = predict_proba(classifiers["commit"], x, early_points, "commit")
    early_pred = np.argmax(early_probs, axis=1)
    early_top = early_probs[np.arange(len(x)), early_pred]
    early_sorted = np.sort(early_probs, axis=1)
    early_margin = early_sorted[:, -1] - early_sorted[:, -2]
    early_entropy = -np.sum(early_probs * np.log(early_probs + 1e-12), axis=1) / math.log(10.0)
    early_features = np.hstack(
        [
            e17.one_hot(early_pred),
            early_probs,
            early_top[:, None],
            early_margin[:, None],
            early_entropy[:, None],
            e17.trajectory_features(x, early_points),
            e17.prefix(x, early_points),
        ]
    )

    per_action: dict[str, dict[str, np.ndarray]] = {}
    for action in ACTIONS:
        probs = predict_proba(classifiers[action], x, early_points, action)
        pred = np.argmax(probs, axis=1)
        sorted_probs = np.sort(probs, axis=1)
        top = sorted_probs[:, -1]
        second = sorted_probs[:, -2]
        margin = top - second
        entropy = -np.sum(probs * np.log(probs + 1e-12), axis=1) / math.log(10.0)
        true_prob = probs[np.arange(len(x)), y]
        cost = action_cost(action, base_cost, distance_cost)
        utility = true_prob - cost
        gate_score = top * margin * (1.0 - 0.5 * entropy)
        per_action[action] = {
            "probs": probs,
            "pred": pred,
            "top": top,
            "margin": margin,
            "entropy": entropy,
            "true_prob": true_prob,
            "utility": utility,
            "gate_score": gate_score,
            "cost": np.full(len(x), cost),
            "geometry": action_geometry(x, early_points, action),
        }

    utility_matrix = np.vstack([per_action[action]["utility"] for action in ACTIONS]).T
    best_indices = np.argmax(utility_matrix, axis=1)

    packets: list[Packet] = []
    for i in range(len(x)):
        for action in ACTIONS:
            idx = action_index(action)
            action_bits = np.asarray(action_one_hot(action), dtype=float)
            packet_pred = int(per_action[action]["pred"][i])
            packet_probs = per_action[action]["probs"][i]
            action_scalar = float(per_action[action]["top"][i])
            cost = float(per_action[action]["cost"][i])
            point_norm = 0.0 if action == "commit" else ACTION_TO_POINT[action] / 8.0
            continuous = np.concatenate(
                [
                    action_bits,
                    np.asarray(digit_vector(int(early_pred[i])), dtype=float),
                    np.asarray(digit_vector(packet_pred), dtype=float),
                    early_features[i],
                    packet_probs,
                    np.asarray(
                        [
                            action_scalar,
                            float(per_action[action]["margin"][i]),
                            float(per_action[action]["entropy"][i]),
                            cost,
                            point_norm,
                            1.0 if packet_pred == int(early_pred[i]) else 0.0,
                            float(packet_probs[int(early_pred[i])]),
                        ],
                        dtype=float,
                    ),
                    per_action[action]["geometry"][i],
                ]
            )
            selected = 1.0 if idx == int(best_indices[i]) else 0.0
            utility_clean = float(per_action[action]["utility"][i])
            packets.append(
                Packet(
                    split=split,
                    episode_id=i,
                    label=int(y[i]),
                    action=action,
                    early_pred=int(early_pred[i]),
                    packet_pred=packet_pred,
                    scalar_score=action_scalar,
                    continuous_features=[float(v) for v in continuous],
                    gate_score=float(per_action[action]["gate_score"][i]),
                    gate_margin=float(per_action[action]["margin"][i]),
                    gate_entropy=float(per_action[action]["entropy"][i]),
                    action_cost=cost,
                    utility_clean=utility_clean,
                    utility_observed=float(utility_clean + rng.normal(scale=utility_noise)),
                    target_select_clean=selected,
                    target_select_observed=float(np.clip(selected + rng.normal(scale=select_noise), 0.0, 1.0)),
                )
            )
    return packets


def calibrate_gate(packets: list[Packet], alpha: float) -> float:
    nonselected = [p.gate_score for p in packets if p.target_select_clean < 0.5]
    if not nonselected:
        return float("inf")
    return float(np.quantile(np.asarray(nonselected, dtype=float), 1.0 - alpha, method="higher"))


def gate_bit(packet: Packet, threshold: float) -> float:
    return 1.0 if packet.gate_score > threshold else 0.0


def feature_vector(packet: Packet, kind: str, gate_threshold: float) -> list[float]:
    bit = gate_bit(packet, gate_threshold)
    action_bits = action_one_hot(packet.action)
    action_gate_bits = [bit * v for v in action_bits]
    if kind == "scalar":
        return [packet.scalar_score] + action_bits + [packet.action_cost]
    if kind == "continuous":
        return packet.continuous_features
    if kind == "gate":
        return action_bits + [bit] + action_gate_bits
    if kind == "governed":
        return packet.continuous_features + [bit] + action_gate_bits
    if kind == "hybrid":
        return packet.continuous_features + [
            packet.gate_score,
            packet.gate_margin,
            packet.gate_entropy,
            bit,
        ] + action_gate_bits
    raise ValueError(f"unknown feature kind: {kind}")


def raw_matrix(packets: list[Packet], kind: str, gate_threshold: float) -> np.ndarray:
    return np.asarray([feature_vector(p, kind, gate_threshold) for p in packets], dtype=float)


def target_vector(packets: list[Packet], kind: str) -> np.ndarray:
    if kind == "value":
        return np.asarray([p.utility_observed for p in packets], dtype=float)
    if kind == "select":
        return np.asarray([p.target_select_observed for p in packets], dtype=float)
    raise ValueError(f"unknown target kind: {kind}")


def expand_matrix_lite(
    x: np.ndarray,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Quadratic ridge basis without all-pairs interactions.

    E17's full expansion is useful for smaller admission probes, but E19 fans
    each trajectory into seven action packets and evaluates a cost sweep. The
    local basis keeps the falsifier about selective sampling instead of runtime.
    """
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    return np.hstack([np.ones((z.shape[0], 1)), z, z * z]), mean, sd


def fit_ridge(
    packets: list[Packet],
    name: str,
    feature_kind: str,
    target_kind: str,
    gate_threshold: float,
    ridge: float,
) -> RidgeModel:
    x_raw = raw_matrix(packets, feature_kind, gate_threshold)
    phi, mean, sd = expand_matrix_lite(x_raw)
    y = target_vector(packets, target_kind)
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


def predict(model: RidgeModel, packets: list[Packet], gate_threshold: float) -> np.ndarray:
    x_raw = raw_matrix(packets, model.feature_kind, gate_threshold)
    phi, _, _ = expand_matrix_lite(
        x_raw,
        np.asarray(model.mean, dtype=float),
        np.asarray(model.sd, dtype=float),
    )
    return phi @ np.asarray(model.coef, dtype=float)


def group_packets(packets: list[Packet]) -> dict[int, list[Packet]]:
    groups: dict[int, list[Packet]] = {}
    for packet in packets:
        groups.setdefault(packet.episode_id, []).append(packet)
    return groups


def policy_metrics(packets: list[Packet], select_scores: np.ndarray) -> dict[str, Any]:
    groups = group_packets(packets)
    by_packet = {id(packet): float(select_scores[i]) for i, packet in enumerate(packets)}
    rows = []
    regrets = []
    exact = []
    false_commit = []
    false_sample = []
    wrong_sample = []
    chosen_actions: dict[str, int] = {action: 0 for action in ACTIONS}
    optimal_actions: dict[str, int] = {action: 0 for action in ACTIONS}
    for episode, episode_packets in groups.items():
        chosen = max(episode_packets, key=lambda packet: by_packet[id(packet)])
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        chosen_actions[chosen.action] += 1
        optimal_actions[optimal.action] += 1
        regret = optimal.utility_clean - chosen.utility_clean
        regrets.append(float(regret))
        exact.append(float(chosen.action == optimal.action))
        false_commit.append(float(chosen.action == "commit" and optimal.action != "commit"))
        false_sample.append(float(chosen.action != "commit" and optimal.action == "commit"))
        wrong_sample.append(float(chosen.action != "commit" and optimal.action != "commit" and chosen.action != optimal.action))
        rows.append((episode, chosen.action, optimal.action, chosen.utility_clean, optimal.utility_clean))
    return {
        "action_accuracy": float(np.mean(exact)),
        "mean_regret": float(np.mean(regrets)),
        "p90_regret": float(np.quantile(np.asarray(regrets, dtype=float), 0.90, method="higher")),
        "false_commit": float(np.mean(false_commit)),
        "false_sample": float(np.mean(false_sample)),
        "wrong_sample": float(np.mean(wrong_sample)),
        "chosen_actions": chosen_actions,
        "optimal_actions": optimal_actions,
    }


def row_metrics(packets: list[Packet], select_scores: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([p.target_select_clean >= 0.5 for p in packets], dtype=bool)
    calls = select_scores >= threshold
    return {
        "row_accuracy": float(np.mean(calls == truth)),
        "optimal_detection": e17.mean_or_nan([float(v) for v in calls[truth]]),
        "nonoptimal_false_admission": e17.mean_or_nan([float(v) for v in calls[~truth]]),
    }


def summarize_packets(packets: list[Packet]) -> dict[str, Any]:
    groups = group_packets(packets)
    optimal_actions = {action: 0 for action in ACTIONS}
    mean_utilities = {action: [] for action in ACTIONS}
    for episode_packets in groups.values():
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        optimal_actions[optimal.action] += 1
        for packet in episode_packets:
            mean_utilities[packet.action].append(packet.utility_clean)
    return {
        "episodes": int(len(groups)),
        "packets": int(len(packets)),
        "optimal_actions": optimal_actions,
        "mean_utility_by_action": {
            action: float(np.mean(values)) if values else float("nan")
            for action, values in mean_utilities.items()
        },
        "mean_gate_score": float(np.mean([packet.gate_score for packet in packets])),
        "mean_utility": float(np.mean([packet.utility_clean for packet in packets])),
    }


def evaluate(
    train: list[Packet],
    calibration: list[Packet],
    test: list[Packet],
    alpha: float,
    ridge: float,
    row_threshold: float,
) -> dict[str, Any]:
    gate_threshold = calibrate_gate(calibration, alpha)
    feature_kind = {
        "scalar": "scalar",
        "continuous_action_value": "continuous",
        "conformal_action_gate": "gate",
        "governed_action": "governed",
        "hybrid_full": "hybrid",
    }
    y_value = target_vector(test, "value")
    y_select = target_vector(test, "select")
    overall: dict[str, Any] = {}
    models: dict[str, Any] = {}
    for name in MODEL_ORDER:
        value_model = fit_ridge(train, name, feature_kind[name], "value", gate_threshold, ridge)
        select_model = fit_ridge(train, name, feature_kind[name], "select", gate_threshold, ridge)
        value_pred = predict(value_model, test, gate_threshold)
        select_pred = predict(select_model, test, gate_threshold)
        overall[name] = {
            "value": {
                "rmse_observed": e17.rmse(y_value, value_pred),
                "r2_observed": e17.r2(y_value, value_pred),
            },
            "select_regression": {
                "rmse_observed": e17.rmse(y_select, select_pred),
                "r2_observed": e17.r2(y_select, select_pred),
            },
            "row_selection": row_metrics(test, select_pred, row_threshold),
            "policy": policy_metrics(test, select_pred),
        }
        models[name] = {
            "value": {
                "feature_kind": value_model.feature_kind,
                "feature_count": value_model.feature_count,
                "expanded_count": value_model.expanded_count,
            },
            "select": {
                "feature_kind": select_model.feature_kind,
                "feature_count": select_model.feature_count,
                "expanded_count": select_model.expanded_count,
            },
        }
    return {
        "gate_threshold": gate_threshold,
        "overall": overall,
        "models": models,
        "train_summary": summarize_packets(train),
        "calibration_summary": summarize_packets(calibration),
        "test_summary": summarize_packets(test),
    }


def decision_quantities(result: dict[str, Any]) -> dict[str, float]:
    overall = result["overall"]
    return {
        "continuous_value_rmse": overall["continuous_action_value"]["value"]["rmse_observed"],
        "gate_value_rmse": overall["conformal_action_gate"]["value"]["rmse_observed"],
        "governed_value_rmse": overall["governed_action"]["value"]["rmse_observed"],
        "hybrid_value_rmse": overall["hybrid_full"]["value"]["rmse_observed"],
        "continuous_action_accuracy": overall["continuous_action_value"]["policy"]["action_accuracy"],
        "gate_action_accuracy": overall["conformal_action_gate"]["policy"]["action_accuracy"],
        "governed_action_accuracy": overall["governed_action"]["policy"]["action_accuracy"],
        "hybrid_action_accuracy": overall["hybrid_full"]["policy"]["action_accuracy"],
        "continuous_regret": overall["continuous_action_value"]["policy"]["mean_regret"],
        "gate_regret": overall["conformal_action_gate"]["policy"]["mean_regret"],
        "governed_regret": overall["governed_action"]["policy"]["mean_regret"],
        "hybrid_regret": overall["hybrid_full"]["policy"]["mean_regret"],
        "continuous_false_commit": overall["continuous_action_value"]["policy"]["false_commit"],
        "gate_false_commit": overall["conformal_action_gate"]["policy"]["false_commit"],
        "hybrid_false_commit": overall["hybrid_full"]["policy"]["false_commit"],
        "continuous_wrong_sample": overall["continuous_action_value"]["policy"]["wrong_sample"],
        "gate_wrong_sample": overall["conformal_action_gate"]["policy"]["wrong_sample"],
        "hybrid_wrong_sample": overall["hybrid_full"]["policy"]["wrong_sample"],
    }


def classify_finding(args: argparse.Namespace, result: dict[str, Any]) -> str:
    dq = decision_quantities(result)
    hybrid_best = (
        dq["hybrid_regret"] + args.regret_margin < min(dq["continuous_regret"], dq["gate_regret"])
        and dq["hybrid_action_accuracy"] > max(dq["continuous_action_accuracy"], dq["gate_action_accuracy"]) + args.accuracy_margin
    )
    continuous_absorbs = (
        dq["continuous_regret"] <= dq["hybrid_regret"] + args.regret_margin
        and dq["continuous_action_accuracy"] >= dq["hybrid_action_accuracy"] - args.accuracy_margin
    )
    gate_wins = (
        dq["gate_regret"] + args.regret_margin < dq["continuous_regret"]
        and dq["gate_action_accuracy"] > dq["continuous_action_accuracy"] + args.accuracy_margin
    )
    if continuous_absorbs:
        return "SELECTIVE_SAMPLING_CONTINUOUS_ACTION_VALUE_ABSORBS_GATE"
    if gate_wins:
        return "SELECTIVE_SAMPLING_GATE_GOVERNS_ACTION_CHOICE"
    if hybrid_best:
        return "SELECTIVE_SAMPLING_HYBRID_ACTION_GOVERNANCE_NEEDED"
    return "SELECTIVE_PENDIGITS_GLIMPSE_INCONCLUSIVE"


def prepare(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, dict[str, Classifier]]:
    x_train, y_train, x_cal, y_cal, x_test, y_test = e17.prepare_splits(args)
    classifiers = {
        action: fit_packet_classifier(x_train, y_train, args.early_points, action, args.classifier_ridge)
        for action in ACTIONS
    }
    return x_train, y_train, x_cal, y_cal, x_test, y_test, classifiers


def build_packets_for_cost(
    args: argparse.Namespace,
    classifiers: dict[str, Classifier],
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_cal: np.ndarray,
    y_cal: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    base_cost: float,
) -> tuple[list[Packet], list[Packet], list[Packet]]:
    rng = np.random.default_rng(args.seed + 1919 + int(round(10000 * base_cost)))
    train = collect_packets(
        "train",
        x_train,
        y_train,
        classifiers,
        args.early_points,
        base_cost,
        args.distance_cost,
        args.utility_noise,
        args.select_noise,
        rng,
    )
    cal = collect_packets(
        "calibration",
        x_cal,
        y_cal,
        classifiers,
        args.early_points,
        base_cost,
        args.distance_cost,
        args.utility_noise,
        args.select_noise,
        rng,
    )
    test = collect_packets(
        "test",
        x_test,
        y_test,
        classifiers,
        args.early_points,
        base_cost,
        args.distance_cost,
        args.utility_noise,
        args.select_noise,
        rng,
    )
    return train, cal, test


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    x_train, y_train, x_cal, y_cal, x_test, y_test, classifiers = prepare(args)
    train, cal, test = build_packets_for_cost(
        args,
        classifiers,
        x_train,
        y_train,
        x_cal,
        y_cal,
        x_test,
        y_test,
        args.base_cost,
    )
    main = evaluate(train, cal, test, args.alpha, args.ridge, args.row_threshold)
    cost_rows = []
    for base_cost in args.base_cost_grid:
        if abs(base_cost - args.base_cost) < 1e-12:
            row = main
        else:
            tr, ca, te = build_packets_for_cost(
                args,
                classifiers,
                x_train,
                y_train,
                x_cal,
                y_cal,
                x_test,
                y_test,
                base_cost,
            )
            row = evaluate(tr, ca, te, args.alpha, args.ridge, args.row_threshold)
        dq = decision_quantities(row)
        cost_rows.append(
            {
                "base_cost": base_cost,
                "optimal_actions": row["test_summary"]["optimal_actions"],
                "continuous_accuracy": dq["continuous_action_accuracy"],
                "gate_accuracy": dq["gate_action_accuracy"],
                "hybrid_accuracy": dq["hybrid_action_accuracy"],
                "continuous_regret": dq["continuous_regret"],
                "gate_regret": dq["gate_regret"],
                "hybrid_regret": dq["hybrid_regret"],
                "continuous_false_commit": dq["continuous_false_commit"],
                "gate_false_commit": dq["gate_false_commit"],
                "hybrid_false_commit": dq["hybrid_false_commit"],
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
            "actions": ACTIONS,
            "base_cost": args.base_cost,
            "distance_cost": args.distance_cost,
            "base_cost_grid": args.base_cost_grid,
            "alpha": args.alpha,
            "classifier_ridge": args.classifier_ridge,
            "ridge": args.ridge,
            "row_threshold": args.row_threshold,
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
        policy = overall[name]["policy"]
        row = overall[name]["row_selection"]
        model_rows.append(
            [
                name,
                fmt(overall[name]["value"]["rmse_observed"]),
                fmt(overall[name]["value"]["r2_observed"]),
                fmt(policy["action_accuracy"]),
                fmt(policy["mean_regret"]),
                fmt(policy["p90_regret"]),
                fmt(policy["false_commit"]),
                fmt(policy["false_sample"]),
                fmt(policy["wrong_sample"]),
                fmt(row["optimal_detection"]),
                fmt(row["nonoptimal_false_admission"]),
            ]
        )

    summary_rows = []
    for key in ["train_summary", "calibration_summary", "test_summary"]:
        s = main[key]
        optimal = s["optimal_actions"]
        summary_rows.append(
            [
                key.replace("_summary", ""),
                str(s["episodes"]),
                str(s["packets"]),
                fmt(s["mean_utility"]),
                fmt(s["mean_gate_score"]),
                ", ".join(f"{a}:{optimal[a]}" for a in ACTIONS),
            ]
        )

    cost_rows = []
    for row in result["cost_sweep"]:
        optimal = row["optimal_actions"]
        cost_rows.append(
            [
                fmt(row["base_cost"]),
                ", ".join(f"{a}:{optimal[a]}" for a in ACTIONS),
                fmt(row["continuous_accuracy"]),
                fmt(row["gate_accuracy"]),
                fmt(row["hybrid_accuracy"]),
                fmt(row["continuous_regret"]),
                fmt(row["gate_regret"]),
                fmt(row["hybrid_regret"]),
                fmt(row["continuous_false_commit"]),
                fmt(row["gate_false_commit"]),
                fmt(row["hybrid_false_commit"]),
            ]
        )

    lines = [
        "# E19 Selective PenDigits Glimpse Probe",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- dataset: `{result['dataset']['name']}`",
        f"- dataset URL: `{result['dataset']['url']}`",
        f"- train/calibration/test: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
        f"- early points: `{config['early_points']}`",
        f"- actions: `{config['actions']}`",
        f"- base/distance cost: `{config['base_cost']}` / `{config['distance_cost']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E19 moves from request-more to choose-where-to-sample. Each action",
        "packet is either commit now or inspect one future trajectory point.",
        "The model must pick one action per trajectory, so policy regret is the",
        "main score.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous value RMSE", fmt(dq["continuous_value_rmse"])],
                ["gate value RMSE", fmt(dq["gate_value_rmse"])],
                ["governed value RMSE", fmt(dq["governed_value_rmse"])],
                ["hybrid value RMSE", fmt(dq["hybrid_value_rmse"])],
                ["continuous action accuracy", fmt(dq["continuous_action_accuracy"])],
                ["gate action accuracy", fmt(dq["gate_action_accuracy"])],
                ["governed action accuracy", fmt(dq["governed_action_accuracy"])],
                ["hybrid action accuracy", fmt(dq["hybrid_action_accuracy"])],
                ["continuous regret", fmt(dq["continuous_regret"])],
                ["gate regret", fmt(dq["gate_regret"])],
                ["governed regret", fmt(dq["governed_regret"])],
                ["hybrid regret", fmt(dq["hybrid_regret"])],
                ["continuous false commit", fmt(dq["continuous_false_commit"])],
                ["gate false commit", fmt(dq["gate_false_commit"])],
                ["hybrid false commit", fmt(dq["hybrid_false_commit"])],
                ["continuous wrong sample", fmt(dq["continuous_wrong_sample"])],
                ["gate wrong sample", fmt(dq["gate_wrong_sample"])],
                ["hybrid wrong sample", fmt(dq["hybrid_wrong_sample"])],
                ["gate threshold", fmt(main["gate_threshold"])],
            ],
        ),
        "",
        "## Split Summary",
        "",
        md_table(["split", "episodes", "packets", "mean utility", "mean gate", "optimal actions"], summary_rows),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "value RMSE",
                "value R2",
                "action acc",
                "regret",
                "p90 regret",
                "false commit",
                "false sample",
                "wrong sample",
                "row detect",
                "row false",
            ],
            model_rows,
        ),
        "",
        "## Cost Sweep",
        "",
        md_table(
            [
                "base cost",
                "optimal actions",
                "cont acc",
                "gate acc",
                "hybrid acc",
                "cont regret",
                "gate regret",
                "hybrid regret",
                "cont false commit",
                "gate false commit",
                "hybrid false commit",
            ],
            cost_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    if result["finding"] == "SELECTIVE_SAMPLING_HYBRID_ACTION_GOVERNANCE_NEEDED":
        lines.extend(
            [
                "Selective sampling needs the hybrid policy. Continuous action",
                "values estimate which glimpses may be useful, while the conformal",
                "packet gate improves admission of high-confidence sample packets.",
                "Neither side alone gives the best action policy.",
            ]
        )
    elif result["finding"] == "SELECTIVE_SAMPLING_CONTINUOUS_ACTION_VALUE_ABSORBS_GATE":
        lines.extend(
            [
                "The continuous action-value policy absorbs the action gate on this",
                "selective-sampling proxy. That would make E19 a negative anchor",
                "for the governance claim.",
            ]
        )
    elif result["finding"] == "SELECTIVE_SAMPLING_GATE_GOVERNS_ACTION_CHOICE":
        lines.extend(
            [
                "The conformal action gate beats the continuous value policy on",
                "action choice and regret. That would support a strong admission",
                "reading for selective sampling.",
            ]
        )
    else:
        lines.extend(
            [
                "The selective glimpse proxy is inconclusive under this",
                "configuration. Action value and action admission are not cleanly",
                "separated enough.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the dataset is external pen-trajectory digit data;",
            "- the agent sees only the first two trajectory points before action packets;",
            "- each sample action exposes a different future point, so action changes which evidence arrives;",
            "- action utility is computed from true-label support minus action cost;",
            "- the conformal gate is calibrated on non-optimal action packets;",
            "- policy metrics choose one action per held-out trajectory and score regret;",
            "- the cost sweep tests whether the result depends on sampling cost.",
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
    parser.add_argument("--base-cost", type=float, default=0.010)
    parser.add_argument("--distance-cost", type=float, default=0.003)
    parser.add_argument("--base-cost-grid", type=float, nargs="+", default=[0.000, 0.010, 0.040])
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--classifier-ridge", type=float, default=1e-2)
    parser.add_argument("--ridge", type=float, default=5e-3)
    parser.add_argument("--utility-noise", type=float, default=0.010)
    parser.add_argument("--select-noise", type=float, default=0.020)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--regret-margin", type=float, default=0.003)
    parser.add_argument("--accuracy-margin", type=float, default=0.010)
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
    json_path = args.report_dir / "e19_selective_pendigits_glimpse_probe.json"
    md_path = args.report_dir / "e19_selective_pendigits_glimpse_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
