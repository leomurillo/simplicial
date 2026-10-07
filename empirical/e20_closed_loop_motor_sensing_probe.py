"""E20 closed-loop motor-sensing probe.

E20 follows the E19 negative anchor. E19 only selected an offline glimpse from
an existing trajectory. E20 makes action part of the data-generating process:
the same early state can become different future evidence under different
controls.

The synthetic task is intentionally small and auditable. A latent class defines
the correct sensorimotor basin. The agent sees an ambiguous early state, then
candidate actions either commit, hold, or push the state toward one of four
basins. A wrong push can deform the future state. The question is whether a
boundary-persistence admission gate carries policy information that continuous
action-value features fail to absorb.
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


CLASSES = list(range(4))
ACTIONS = ["commit", "hold", "aim_0", "aim_1", "aim_2", "aim_3"]
MODEL_ORDER = [
    "scalar",
    "continuous_transition_value",
    "conformal_transition_gate",
    "governed_transition",
    "hybrid_full",
]
PROTOTYPES = np.asarray(
    [
        [1.00, 0.00, 0.55, 0.00],
        [0.00, 1.00, 0.00, 0.55],
        [-1.00, 0.00, -0.55, 0.00],
        [0.00, -1.00, 0.00, -0.55],
    ],
    dtype=float,
)


@dataclass(frozen=True)
class Episode:
    split: str
    episode_id: int
    label: int
    early_state: list[float]
    ambiguity: float
    motor_sensitivity: float
    early_probs: list[float]
    early_pred: int
    early_top: float
    early_margin: float
    early_entropy: float


@dataclass(frozen=True)
class Packet:
    split: str
    episode_id: int
    label: int
    action: str
    action_target: int
    early_pred: int
    post_pred: int
    scalar_score: float
    continuous_features: list[float]
    gate_score: float
    gate_same: float
    gate_aligned: float
    gate_smoothness: float
    action_cost: float
    rupture: float
    unsafe_transition: float
    utility_clean: float
    utility_observed: float
    target_select_clean: float
    target_select_observed: float


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


def action_target(action: str) -> int:
    if action.startswith("aim_"):
        return int(action.split("_", 1)[1])
    return -1


def action_one_hot(action: str) -> list[float]:
    return [1.0 if action == item else 0.0 for item in ACTIONS]


def class_one_hot(value: int) -> list[float]:
    return [1.0 if value == item else 0.0 for item in CLASSES]


def softmax(values: np.ndarray) -> np.ndarray:
    centered = values - values.max(axis=-1, keepdims=True)
    exp = np.exp(centered)
    return exp / exp.sum(axis=-1, keepdims=True)


def class_probs(states: np.ndarray, temperature: float) -> np.ndarray:
    diffs = states[:, None, :] - PROTOTYPES[None, :, :]
    logits = -np.sum(diffs * diffs, axis=2) / temperature
    return softmax(logits)


def prob_summary(probs: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    pred = np.argmax(probs, axis=1)
    sorted_probs = np.sort(probs, axis=1)
    top = sorted_probs[:, -1]
    margin = sorted_probs[:, -1] - sorted_probs[:, -2]
    entropy = -np.sum(probs * np.log(probs + 1e-12), axis=1) / math.log(probs.shape[1])
    return pred, top, margin, entropy


def split_seed(seed: int, split: str) -> int:
    offset = {"train": 11, "calibration": 17, "test": 23}[split]
    return seed + offset * 1009


def generate_episodes(split: str, n: int, seed: int, temperature: float) -> list[Episode]:
    rng = np.random.default_rng(split_seed(seed, split))
    labels = rng.integers(0, len(CLASSES), size=n)
    rivals = (labels + rng.integers(1, len(CLASSES), size=n)) % len(CLASSES)
    ambiguity = rng.beta(2.2, 4.0, size=n)
    hard_mask = rng.random(n) < 0.22
    ambiguity = np.where(hard_mask, rng.uniform(0.38, 0.62, size=n), ambiguity)
    motor_sensitivity = rng.uniform(0.75, 1.25, size=n)
    early_state = (
        (1.0 - ambiguity)[:, None] * PROTOTYPES[labels]
        + ambiguity[:, None] * PROTOTYPES[rivals]
        + rng.normal(scale=0.22 + 0.22 * ambiguity[:, None], size=(n, PROTOTYPES.shape[1]))
    )
    probs = class_probs(early_state, temperature)
    pred, top, margin, entropy = prob_summary(probs)
    return [
        Episode(
            split=split,
            episode_id=i,
            label=int(labels[i]),
            early_state=[float(v) for v in early_state[i]],
            ambiguity=float(ambiguity[i]),
            motor_sensitivity=float(motor_sensitivity[i]),
            early_probs=[float(v) for v in probs[i]],
            early_pred=int(pred[i]),
            early_top=float(top[i]),
            early_margin=float(margin[i]),
            early_entropy=float(entropy[i]),
        )
        for i in range(n)
    ]


def transition_state(
    episode: Episode,
    action: str,
    rng: np.random.Generator,
    args: argparse.Namespace,
) -> tuple[np.ndarray, float, float, float]:
    early = np.asarray(episode.early_state, dtype=float)
    label = episode.label
    target = action_target(action)
    if action == "commit":
        return early.copy(), 0.0, 0.0, 0.0

    if action == "hold":
        drift_gain = args.hold_gain * episode.motor_sensitivity
        post = early + drift_gain * (PROTOTYPES[label] - early)
        post += rng.normal(scale=args.hold_noise + 0.05 * episode.ambiguity, size=early.shape)
        cost = args.hold_cost
        return post, cost, 0.0, float(np.linalg.norm(post - early))

    correct = float(target == label)
    gain = (args.correct_gain if correct else args.wrong_gain) * episode.motor_sensitivity
    intended = PROTOTYPES[target]
    post = early + gain * (intended - early)
    noise_scale = args.correct_noise if correct else args.wrong_noise
    post += rng.normal(scale=noise_scale + 0.10 * episode.ambiguity, size=early.shape)

    wrong_pressure = (1.0 - correct) * (0.28 + 0.50 * episode.ambiguity + 0.22 * episode.early_entropy)
    rupture = float(rng.random() < min(0.92, wrong_pressure))
    if rupture:
        alternative = (target + rng.integers(1, len(CLASSES))) % len(CLASSES)
        shock = args.rupture_gain * (PROTOTYPES[alternative] - PROTOTYPES[label])
        post += shock + rng.normal(scale=args.rupture_noise, size=early.shape)

    cost = args.aim_cost + args.energy_cost * float(np.linalg.norm(PROTOTYPES[target] - early))
    return post, cost, rupture, float(np.linalg.norm(post - early))


def packet_continuous_features(
    episode: Episode,
    action: str,
    post_state: np.ndarray,
    post_probs: np.ndarray,
    cost: float,
    displacement: float,
    rupture: float,
) -> list[float]:
    early_state = np.asarray(episode.early_state, dtype=float)
    early_probs = np.asarray(episode.early_probs, dtype=float)
    post_pred, post_top, post_margin, post_entropy = prob_summary(post_probs[None, :])
    delta = post_state - early_state
    target = action_target(action)
    target_bits = [0.0] * len(CLASSES) if target < 0 else class_one_hot(target)
    return [
        *action_one_hot(action),
        *target_bits,
        *early_probs.tolist(),
        *post_probs.tolist(),
        float(episode.early_top),
        float(episode.early_margin),
        float(episode.early_entropy),
        float(post_top[0]),
        float(post_margin[0]),
        float(post_entropy[0]),
        float(cost),
        float(displacement),
        float(episode.ambiguity),
        float(episode.motor_sensitivity),
        *early_state.tolist(),
        *post_state.tolist(),
        *delta.tolist(),
        float(np.dot(early_state, post_state)),
        float(np.linalg.norm(delta)),
        rupture,
    ]


def collect_packets(
    episodes: list[Episode],
    args: argparse.Namespace,
    utility_noise: float,
    select_noise: float,
) -> list[Packet]:
    rng = np.random.default_rng(split_seed(args.seed + 4040, episodes[0].split))
    utilities_by_episode: dict[int, list[float]] = {}
    raw_rows: list[dict[str, Any]] = []

    for episode in episodes:
        for action in ACTIONS:
            post_state, cost, rupture, displacement = transition_state(episode, action, rng, args)
            post_probs = class_probs(post_state[None, :], args.temperature)[0]
            post_pred_arr, post_top_arr, post_margin_arr, post_entropy_arr = prob_summary(post_probs[None, :])
            post_pred = int(post_pred_arr[0])
            post_top = float(post_top_arr[0])
            post_margin = float(post_margin_arr[0])
            post_entropy = float(post_entropy_arr[0])

            same = float(post_pred == episode.early_pred)
            target = action_target(action)
            aligned = float(action in {"commit", "hold"} or target == episode.early_pred)
            smoothness = float(math.exp(-displacement / args.smoothness_scale))
            gate_score = same * aligned * post_top * post_margin * (1.0 - 0.55 * post_entropy) * smoothness

            true_support = float(post_probs[episode.label])
            unsafe = float(post_pred != episode.label or rupture > 0.5)
            utility = true_support - cost - args.rupture_penalty * rupture - args.unsafe_penalty * unsafe
            raw_rows.append(
                {
                    "episode": episode,
                    "action": action,
                    "target": target,
                    "post_pred": post_pred,
                    "post_top": post_top,
                    "post_margin": post_margin,
                    "post_entropy": post_entropy,
                    "post_state": post_state,
                    "post_probs": post_probs,
                    "cost": cost,
                    "rupture": rupture,
                    "unsafe": unsafe,
                    "displacement": displacement,
                    "same": same,
                    "aligned": aligned,
                    "smoothness": smoothness,
                    "gate_score": gate_score,
                    "utility": utility,
                }
            )
            utilities_by_episode.setdefault(episode.episode_id, []).append(utility)

    best_by_episode = {
        episode_id: int(np.argmax(np.asarray(values, dtype=float)))
        for episode_id, values in utilities_by_episode.items()
    }

    packets: list[Packet] = []
    per_episode_counter: dict[int, int] = {}
    for row in raw_rows:
        episode = row["episode"]
        local_index = per_episode_counter.get(episode.episode_id, 0)
        per_episode_counter[episode.episode_id] = local_index + 1
        selected = float(local_index == best_by_episode[episode.episode_id])
        continuous = packet_continuous_features(
            episode=episode,
            action=row["action"],
            post_state=row["post_state"],
            post_probs=row["post_probs"],
            cost=row["cost"],
            displacement=row["displacement"],
            rupture=row["rupture"],
        )
        packets.append(
            Packet(
                split=episode.split,
                episode_id=episode.episode_id,
                label=episode.label,
                action=row["action"],
                action_target=int(row["target"]),
                early_pred=episode.early_pred,
                post_pred=int(row["post_pred"]),
                scalar_score=float(row["post_top"]),
                continuous_features=[float(v) for v in continuous],
                gate_score=float(row["gate_score"]),
                gate_same=float(row["same"]),
                gate_aligned=float(row["aligned"]),
                gate_smoothness=float(row["smoothness"]),
                action_cost=float(row["cost"]),
                rupture=float(row["rupture"]),
                unsafe_transition=float(row["unsafe"]),
                utility_clean=float(row["utility"]),
                utility_observed=float(row["utility"] + rng.normal(scale=utility_noise)),
                target_select_clean=selected,
                target_select_observed=float(np.clip(selected + rng.normal(scale=select_noise), 0.0, 1.0)),
            )
        )
    return packets


def calibrate_gate(packets: list[Packet], alpha: float) -> float:
    bad_scores = [p.gate_score for p in packets if p.target_select_clean < 0.5]
    if not bad_scores:
        return float("inf")
    return float(np.quantile(np.asarray(bad_scores, dtype=float), 1.0 - alpha, method="higher"))


def gate_bit(packet: Packet, threshold: float) -> float:
    return 1.0 if packet.gate_score > threshold else 0.0


def feature_vector(packet: Packet, kind: str, gate_threshold: float) -> list[float]:
    bit = gate_bit(packet, gate_threshold)
    action_bits = action_one_hot(packet.action)
    action_gate_bits = [bit * v for v in action_bits]
    if kind == "scalar":
        return [packet.scalar_score, packet.action_cost] + action_bits
    if kind == "continuous":
        return packet.continuous_features
    if kind == "gate":
        return action_bits + [bit] + action_gate_bits
    if kind == "governed":
        return packet.continuous_features + [bit] + action_gate_bits
    if kind == "hybrid":
        return packet.continuous_features + [
            packet.gate_score,
            packet.gate_same,
            packet.gate_aligned,
            packet.gate_smoothness,
            bit,
        ] + action_gate_bits
    raise ValueError(f"unknown feature kind: {kind}")


def raw_matrix(packets: list[Packet], kind: str, gate_threshold: float) -> np.ndarray:
    return np.asarray([feature_vector(packet, kind, gate_threshold) for packet in packets], dtype=float)


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


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    denom = float(np.sum((y_true - y_true.mean()) ** 2))
    if denom <= 1e-12:
        return float("nan")
    return float(1.0 - np.sum((y_true - y_pred) ** 2) / denom)


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
    regrets = []
    exact = []
    false_commit = []
    missed_control = []
    wrong_control = []
    unsafe_choices = []
    unnecessary_unsafe = []
    chosen_actions = {action: 0 for action in ACTIONS}
    optimal_actions = {action: 0 for action in ACTIONS}

    for episode_packets in groups.values():
        chosen = max(episode_packets, key=lambda packet: scores[id(packet)])
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        chosen_actions[chosen.action] += 1
        optimal_actions[optimal.action] += 1
        regret = optimal.utility_clean - chosen.utility_clean
        regrets.append(float(regret))
        exact.append(float(chosen.action == optimal.action))
        false_commit.append(float(chosen.action == "commit" and optimal.action != "commit"))
        missed_control.append(float(chosen.action in {"commit", "hold"} and optimal.action.startswith("aim_")))
        wrong_control.append(
            float(
                chosen.action.startswith("aim_")
                and optimal.action.startswith("aim_")
                and chosen.action != optimal.action
            )
        )
        unsafe_choices.append(chosen.unsafe_transition)
        unnecessary_unsafe.append(float(chosen.unsafe_transition > 0.5 and optimal.unsafe_transition < 0.5))

    return {
        "action_accuracy": float(np.mean(exact)),
        "mean_regret": float(np.mean(regrets)),
        "p90_regret": float(np.quantile(np.asarray(regrets, dtype=float), 0.90, method="higher")),
        "false_commit": float(np.mean(false_commit)),
        "missed_control": float(np.mean(missed_control)),
        "wrong_control": float(np.mean(wrong_control)),
        "unsafe_choice": float(np.mean(unsafe_choices)),
        "unnecessary_unsafe": float(np.mean(unnecessary_unsafe)),
        "chosen_actions": chosen_actions,
        "optimal_actions": optimal_actions,
    }


def row_metrics(packets: list[Packet], select_scores: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([p.target_select_clean >= 0.5 for p in packets], dtype=bool)
    calls = select_scores >= threshold
    return {
        "row_accuracy": float(np.mean(calls == truth)),
        "optimal_detection": mean_or_nan([float(v) for v in calls[truth]]),
        "nonoptimal_false_admission": mean_or_nan([float(v) for v in calls[~truth]]),
    }


def summarize_packets(packets: list[Packet]) -> dict[str, Any]:
    groups = group_packets(packets)
    optimal_actions = {action: 0 for action in ACTIONS}
    unsafe_by_action = {action: [] for action in ACTIONS}
    utility_by_action = {action: [] for action in ACTIONS}
    for episode_packets in groups.values():
        optimal = max(episode_packets, key=lambda packet: packet.utility_clean)
        optimal_actions[optimal.action] += 1
        for packet in episode_packets:
            unsafe_by_action[packet.action].append(packet.unsafe_transition)
            utility_by_action[packet.action].append(packet.utility_clean)
    return {
        "episodes": int(len(groups)),
        "packets": int(len(packets)),
        "optimal_actions": optimal_actions,
        "mean_utility": float(np.mean([p.utility_clean for p in packets])),
        "mean_gate_score": float(np.mean([p.gate_score for p in packets])),
        "mean_unsafe": float(np.mean([p.unsafe_transition for p in packets])),
        "mean_utility_by_action": {
            action: float(np.mean(values)) if values else float("nan")
            for action, values in utility_by_action.items()
        },
        "unsafe_by_action": {
            action: float(np.mean(values)) if values else float("nan")
            for action, values in unsafe_by_action.items()
        },
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
        "continuous_transition_value": "continuous",
        "conformal_transition_gate": "gate",
        "governed_transition": "governed",
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
                "rmse_observed": rmse(y_value, value_pred),
                "r2_observed": r2(y_value, value_pred),
            },
            "select_regression": {
                "rmse_observed": rmse(y_select, select_pred),
                "r2_observed": r2(y_select, select_pred),
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
        "continuous_value_rmse": overall["continuous_transition_value"]["value"]["rmse_observed"],
        "gate_value_rmse": overall["conformal_transition_gate"]["value"]["rmse_observed"],
        "governed_value_rmse": overall["governed_transition"]["value"]["rmse_observed"],
        "hybrid_value_rmse": overall["hybrid_full"]["value"]["rmse_observed"],
        "continuous_action_accuracy": overall["continuous_transition_value"]["policy"]["action_accuracy"],
        "gate_action_accuracy": overall["conformal_transition_gate"]["policy"]["action_accuracy"],
        "governed_action_accuracy": overall["governed_transition"]["policy"]["action_accuracy"],
        "hybrid_action_accuracy": overall["hybrid_full"]["policy"]["action_accuracy"],
        "continuous_regret": overall["continuous_transition_value"]["policy"]["mean_regret"],
        "gate_regret": overall["conformal_transition_gate"]["policy"]["mean_regret"],
        "governed_regret": overall["governed_transition"]["policy"]["mean_regret"],
        "hybrid_regret": overall["hybrid_full"]["policy"]["mean_regret"],
        "continuous_unnecessary_unsafe": overall["continuous_transition_value"]["policy"]["unnecessary_unsafe"],
        "gate_unnecessary_unsafe": overall["conformal_transition_gate"]["policy"]["unnecessary_unsafe"],
        "hybrid_unnecessary_unsafe": overall["hybrid_full"]["policy"]["unnecessary_unsafe"],
        "continuous_missed_control": overall["continuous_transition_value"]["policy"]["missed_control"],
        "gate_missed_control": overall["conformal_transition_gate"]["policy"]["missed_control"],
        "hybrid_missed_control": overall["hybrid_full"]["policy"]["missed_control"],
    }


def classify_finding(args: argparse.Namespace, result: dict[str, Any]) -> str:
    dq = decision_quantities(result)
    continuous_absorbs = (
        dq["continuous_regret"] <= dq["hybrid_regret"] + args.regret_margin
        and dq["continuous_action_accuracy"] >= dq["hybrid_action_accuracy"] - args.accuracy_margin
    )
    gate_wins = (
        dq["gate_regret"] + args.regret_margin < dq["continuous_regret"]
        and dq["gate_unnecessary_unsafe"] + args.unsafe_margin < dq["continuous_unnecessary_unsafe"]
    )
    hybrid_best = (
        dq["hybrid_regret"] + args.regret_margin < min(dq["continuous_regret"], dq["gate_regret"])
        and dq["hybrid_action_accuracy"] > max(dq["continuous_action_accuracy"], dq["gate_action_accuracy"]) + args.accuracy_margin
    )
    if continuous_absorbs:
        return "CLOSED_LOOP_CONTINUOUS_VALUE_ABSORBS_GATE"
    if gate_wins:
        return "CLOSED_LOOP_TRANSITION_GATE_GOVERNS_UNSAFE_ACTION"
    if hybrid_best:
        return "CLOSED_LOOP_HYBRID_GOVERNANCE_NEEDED"
    return "CLOSED_LOOP_MOTOR_SENSING_INCONCLUSIVE"


def build_packets_for_cost(args: argparse.Namespace, aim_cost: float) -> tuple[list[Packet], list[Packet], list[Packet]]:
    local_args = argparse.Namespace(**vars(args))
    local_args.aim_cost = aim_cost
    train_episodes = generate_episodes("train", args.train_n, args.seed, args.temperature)
    cal_episodes = generate_episodes("calibration", args.calibration_n, args.seed, args.temperature)
    test_episodes = generate_episodes("test", args.test_n, args.seed, args.temperature)
    train = collect_packets(train_episodes, local_args, args.utility_noise, args.select_noise)
    cal = collect_packets(cal_episodes, local_args, args.utility_noise, args.select_noise)
    test = collect_packets(test_episodes, local_args, args.utility_noise, args.select_noise)
    return train, cal, test


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    train, cal, test = build_packets_for_cost(args, args.aim_cost)
    main = evaluate(train, cal, test, args.alpha, args.ridge, args.row_threshold)
    cost_rows = []
    for aim_cost in args.aim_cost_grid:
        if abs(aim_cost - args.aim_cost) < 1e-12:
            row = main
        else:
            tr, ca, te = build_packets_for_cost(args, aim_cost)
            row = evaluate(tr, ca, te, args.alpha, args.ridge, args.row_threshold)
        dq = decision_quantities(row)
        cost_rows.append(
            {
                "aim_cost": aim_cost,
                "optimal_actions": row["test_summary"]["optimal_actions"],
                "continuous_accuracy": dq["continuous_action_accuracy"],
                "gate_accuracy": dq["gate_action_accuracy"],
                "hybrid_accuracy": dq["hybrid_action_accuracy"],
                "continuous_regret": dq["continuous_regret"],
                "gate_regret": dq["gate_regret"],
                "hybrid_regret": dq["hybrid_regret"],
                "continuous_unnecessary_unsafe": dq["continuous_unnecessary_unsafe"],
                "gate_unnecessary_unsafe": dq["gate_unnecessary_unsafe"],
                "hybrid_unnecessary_unsafe": dq["hybrid_unnecessary_unsafe"],
            }
        )
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "Synthetic closed-loop motor-sensing field",
            "classes": len(CLASSES),
            "state_dimension": int(PROTOTYPES.shape[1]),
            "actions": ACTIONS,
            "description": "Actions intervene on the future state rather than selecting an offline observation.",
        },
        "config": {
            "seed": args.seed,
            "train_n": args.train_n,
            "calibration_n": args.calibration_n,
            "test_n": args.test_n,
            "temperature": args.temperature,
            "aim_cost": args.aim_cost,
            "aim_cost_grid": args.aim_cost_grid,
            "hold_cost": args.hold_cost,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "row_threshold": args.row_threshold,
            "utility_noise": args.utility_noise,
            "select_noise": args.select_noise,
        },
        "main": main,
        "decision_quantities": decision_quantities(main),
        "cost_sweep": cost_rows,
    }
    result["finding"] = classify_finding(args, main)
    return result


def fmt(value: float) -> str:
    if isinstance(value, float) and math.isnan(value):
        return "nan"
    return f"{value:.3f}"


def action_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{action}:{counts.get(action, 0)}" for action in ACTIONS)


def write_report(path: Path, result: dict[str, Any]) -> None:
    config = result["config"]
    main = result["main"]
    dq = result["decision_quantities"]
    overall = main["overall"]
    lines: list[str] = []
    lines.extend(
        [
            "# E20 Closed-Loop Motor-Sensing Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{result['dataset']['name']}`",
            f"- train/calibration/test episodes: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
            f"- actions: `{ACTIONS}`",
            f"- aim/hold cost: `{config['aim_cost']}` / `{config['hold_cost']}`",
            f"- alpha: `{config['alpha']}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E20 tests whether boundary governance reappears when action",
            "changes the future state, instead of selecting an offline glimpse.",
            "Each candidate control is applied to the early state and produces",
            "a different post-action state before utility is scored.",
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
            f"| gate threshold | {fmt(main['gate_threshold'])} |",
            "",
            "## Split Summary",
            "",
            "| split | episodes | packets | mean utility | mean gate | mean unsafe | optimal actions |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for split_key in ["train_summary", "calibration_summary", "test_summary"]:
        s = main[split_key]
        lines.append(
            "| "
            + " | ".join(
                [
                    split_key.replace("_summary", ""),
                    str(s["episodes"]),
                    str(s["packets"]),
                    fmt(s["mean_utility"]),
                    fmt(s["mean_gate_score"]),
                    fmt(s["mean_unsafe"]),
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
            "| model | value RMSE | value R2 | action acc | regret | p90 regret | false commit | missed control | wrong control | unsafe choice | unnecessary unsafe | row detect | row false |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for name in MODEL_ORDER:
        item = overall[name]
        value = item["value"]
        policy = item["policy"]
        row = item["row_selection"]
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    fmt(value["rmse_observed"]),
                    fmt(value["r2_observed"]),
                    fmt(policy["action_accuracy"]),
                    fmt(policy["mean_regret"]),
                    fmt(policy["p90_regret"]),
                    fmt(policy["false_commit"]),
                    fmt(policy["missed_control"]),
                    fmt(policy["wrong_control"]),
                    fmt(policy["unsafe_choice"]),
                    fmt(policy["unnecessary_unsafe"]),
                    fmt(row["optimal_detection"]),
                    fmt(row["nonoptimal_false_admission"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Aim-Cost Sweep",
            "",
            "| aim cost | optimal actions | cont acc | gate acc | hybrid acc | cont regret | gate regret | hybrid regret | cont unsafe | gate unsafe | hybrid unsafe |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["cost_sweep"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    fmt(row["aim_cost"]),
                    action_counts(row["optimal_actions"]),
                    fmt(row["continuous_accuracy"]),
                    fmt(row["gate_accuracy"]),
                    fmt(row["hybrid_accuracy"]),
                    fmt(row["continuous_regret"]),
                    fmt(row["gate_regret"]),
                    fmt(row["hybrid_regret"]),
                    fmt(row["continuous_unnecessary_unsafe"]),
                    fmt(row["gate_unnecessary_unsafe"]),
                    fmt(row["hybrid_unnecessary_unsafe"]),
                ]
            )
            + " |"
        )

    finding = result["finding"]
    if finding == "CLOSED_LOOP_HYBRID_GOVERNANCE_NEEDED":
        interpretation = [
            "The hybrid policy wins on the closed-loop intervention task.",
            "Continuous value sees rich pre/post evidence, but the gate adds",
            "boundary-persistence information that improves action choice.",
        ]
    elif finding == "CLOSED_LOOP_TRANSITION_GATE_GOVERNS_UNSAFE_ACTION":
        interpretation = [
            "The transition gate wins by controlling unsafe action admission.",
            "This supports the claim that intervention needs governance once",
            "action can deform the future state.",
        ]
    elif finding == "CLOSED_LOOP_CONTINUOUS_VALUE_ABSORBS_GATE":
        interpretation = [
            "Continuous action value absorbs the transition gate here.",
            "This would extend the E19 negative anchor into the closed-loop",
            "synthetic task.",
        ]
    else:
        interpretation = [
            "The probe is inconclusive at the default margins.",
            "The result should be used as a design diagnostic rather than a",
            "positive governance result.",
        ]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- actions intervene on the future state before utility is scored;",
            "- every episode enumerates the same starting state under multiple controls;",
            "- wrong controls can rupture or deform the post-action evidence;",
            "- policy metrics choose one action per held-out episode and score regret;",
            "- continuous features include rich post-action evidence, so gate gains are not automatic;",
            "- the aim-cost sweep checks cheap, main, and expensive control regimes.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--train-n", type=int, default=7000)
    parser.add_argument("--calibration-n", type=int, default=2400)
    parser.add_argument("--test-n", type=int, default=3600)
    parser.add_argument("--temperature", type=float, default=0.42)
    parser.add_argument("--hold-gain", type=float, default=0.18)
    parser.add_argument("--correct-gain", type=float, default=0.78)
    parser.add_argument("--wrong-gain", type=float, default=0.70)
    parser.add_argument("--hold-noise", type=float, default=0.11)
    parser.add_argument("--correct-noise", type=float, default=0.09)
    parser.add_argument("--wrong-noise", type=float, default=0.16)
    parser.add_argument("--rupture-gain", type=float, default=0.55)
    parser.add_argument("--rupture-noise", type=float, default=0.28)
    parser.add_argument("--hold-cost", type=float, default=0.018)
    parser.add_argument("--aim-cost", type=float, default=0.040)
    parser.add_argument("--energy-cost", type=float, default=0.012)
    parser.add_argument("--aim-cost-grid", type=float, nargs="+", default=[0.000, 0.040, 0.100])
    parser.add_argument("--rupture-penalty", type=float, default=0.10)
    parser.add_argument("--unsafe-penalty", type=float, default=0.03)
    parser.add_argument("--smoothness-scale", type=float, default=1.65)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=7e-3)
    parser.add_argument("--utility-noise", type=float, default=0.012)
    parser.add_argument("--select-noise", type=float, default=0.020)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--regret-margin", type=float, default=0.004)
    parser.add_argument("--accuracy-margin", type=float, default=0.012)
    parser.add_argument("--unsafe-margin", type=float, default=0.015)
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
    json_path = args.report_dir / "e20_closed_loop_motor_sensing_probe.json"
    md_path = args.report_dir / "e20_closed_loop_motor_sensing_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
