"""E13 capacity versus resource-rational control falsifier.

E13 tests whether capacity/compression/tool-use is a primitive route or a
resource-rational control problem with an externalization admission gate.

The strong rival is continuous resource-rational control: memory load,
compression value, tool value, action cost, and capacity pressure. The probe
separates two jobs:

    - predict graded resource/cognitive effort;
    - decide whether to admit a persistent external tool/memory route.

Synthetic worlds:

    1. no_capacity_world: low load, no useful tool;
    2. compress_world: stable low-rank structure, internal compression is best;
    3. bait_world: train-side tool appears useful but fails out of sample;
    4. tool_world: stable external aid beats internal memory under capacity.

The non-tautological result can split the jobs: resource rationality may fit
effort, while held-out tool persistence governs externalization.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


SOURCES = ["tool_world", "compress_world", "bait_world", "no_capacity_world"]
MODEL_ORDER = [
    "scalar",
    "continuous_resource",
    "external_tool_gate",
    "governed_resource_gate",
    "hybrid_resource_tool",
]


@dataclass(frozen=True)
class Episode:
    source: str
    operation: str
    scalar_score: float
    memory_load: float
    capacity_pressure: float
    compression_ratio: float
    train_compression_value: float
    heldout_compression_value: float
    train_tool_value: float
    heldout_tool_value: float
    train_tool_reliability: float
    heldout_tool_reliability: float
    internal_memory_value: float
    internal_memory_cost: float
    tool_cost: float
    action_cost: float
    resource_value: float
    tool_persistence_score: float
    target_effort_clean: float
    target_effort_observed: float
    target_externalize_clean: float
    target_externalize_observed: float


@dataclass(frozen=True)
class LinearModel:
    name: str
    feature_kind: str
    target_kind: str
    coef: list[float]
    mean: list[float]
    sd: list[float]


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + float(np.exp(-x)))


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def noisy_clip(
    rng: np.random.Generator,
    value: float,
    noise: float,
    lo: float = 0.0,
    hi: float = 1.2,
) -> float:
    return float(np.clip(value + rng.normal(scale=noise), lo, hi))


def source_parameters(rng: np.random.Generator, source: str) -> dict[str, float]:
    if source == "no_capacity_world":
        return {
            "memory_load": float(rng.uniform(0.10, 0.28)),
            "capacity_pressure": float(rng.uniform(0.05, 0.20)),
            "compression_ratio": float(rng.uniform(0.10, 0.24)),
            "train_compression_value": float(rng.uniform(0.05, 0.16)),
            "heldout_compression_value": float(rng.uniform(0.04, 0.15)),
            "train_tool_value": float(rng.uniform(0.00, 0.12)),
            "heldout_tool_value": float(rng.uniform(0.00, 0.10)),
            "train_tool_reliability": float(rng.uniform(0.10, 0.30)),
            "heldout_tool_reliability": float(rng.uniform(0.08, 0.28)),
            "internal_memory_value": float(rng.uniform(0.08, 0.20)),
            "internal_memory_cost": float(rng.uniform(0.05, 0.16)),
            "tool_cost": float(rng.uniform(0.16, 0.32)),
            "action_cost": float(rng.uniform(0.08, 0.22)),
            "externalize": 0.0,
        }
    if source == "compress_world":
        return {
            "memory_load": float(rng.uniform(0.42, 0.68)),
            "capacity_pressure": float(rng.uniform(0.32, 0.58)),
            "compression_ratio": float(rng.uniform(0.68, 0.95)),
            "train_compression_value": float(rng.uniform(0.62, 0.95)),
            "heldout_compression_value": float(rng.uniform(0.60, 0.92)),
            "train_tool_value": float(rng.uniform(0.12, 0.34)),
            "heldout_tool_value": float(rng.uniform(0.10, 0.32)),
            "train_tool_reliability": float(rng.uniform(0.22, 0.48)),
            "heldout_tool_reliability": float(rng.uniform(0.20, 0.46)),
            "internal_memory_value": float(rng.uniform(0.54, 0.82)),
            "internal_memory_cost": float(rng.uniform(0.18, 0.34)),
            "tool_cost": float(rng.uniform(0.16, 0.34)),
            "action_cost": float(rng.uniform(0.10, 0.25)),
            "externalize": 0.0,
        }
    if source == "bait_world":
        # Locally this looks like a good tool case, but the tool does not
        # persist. A train-only resource model should be tempted to externalize.
        return {
            "memory_load": float(rng.uniform(0.72, 1.02)),
            "capacity_pressure": float(rng.uniform(0.70, 1.05)),
            "compression_ratio": float(rng.uniform(0.12, 0.34)),
            "train_compression_value": float(rng.uniform(0.18, 0.40)),
            "heldout_compression_value": float(rng.uniform(0.12, 0.30)),
            "train_tool_value": float(rng.uniform(0.72, 1.05)),
            "heldout_tool_value": float(rng.uniform(0.08, 0.28)),
            "train_tool_reliability": float(rng.uniform(0.72, 1.00)),
            "heldout_tool_reliability": float(rng.uniform(0.10, 0.34)),
            "internal_memory_value": float(rng.uniform(0.44, 0.68)),
            "internal_memory_cost": float(rng.uniform(0.58, 0.92)),
            "tool_cost": float(rng.uniform(0.14, 0.30)),
            "action_cost": float(rng.uniform(0.12, 0.28)),
            "externalize": 0.0,
        }
    if source == "tool_world":
        return {
            "memory_load": float(rng.uniform(0.72, 1.02)),
            "capacity_pressure": float(rng.uniform(0.70, 1.05)),
            "compression_ratio": float(rng.uniform(0.10, 0.32)),
            "train_compression_value": float(rng.uniform(0.16, 0.38)),
            "heldout_compression_value": float(rng.uniform(0.12, 0.32)),
            "train_tool_value": float(rng.uniform(0.72, 1.05)),
            "heldout_tool_value": float(rng.uniform(0.70, 1.04)),
            "train_tool_reliability": float(rng.uniform(0.72, 1.00)),
            "heldout_tool_reliability": float(rng.uniform(0.72, 1.00)),
            "internal_memory_value": float(rng.uniform(0.44, 0.68)),
            "internal_memory_cost": float(rng.uniform(0.58, 0.92)),
            "tool_cost": float(rng.uniform(0.14, 0.30)),
            "action_cost": float(rng.uniform(0.12, 0.28)),
            "externalize": 1.0,
        }
    raise ValueError(f"unknown source: {source}")


def make_episode(
    rng: np.random.Generator,
    source: str,
    effort_noise: float,
    external_noise: float,
) -> Episode:
    p = source_parameters(rng, source)
    memory_load = noisy_clip(rng, p["memory_load"], 0.035, hi=1.2)
    capacity_pressure = noisy_clip(rng, p["capacity_pressure"], 0.040, hi=1.2)
    compression_ratio = noisy_clip(rng, p["compression_ratio"], 0.035, hi=1.0)
    train_compression_value = noisy_clip(rng, p["train_compression_value"], 0.045, hi=1.2)
    heldout_compression_value = noisy_clip(rng, p["heldout_compression_value"], 0.045, hi=1.2)
    train_tool_value = noisy_clip(rng, p["train_tool_value"], 0.045, hi=1.2)
    heldout_tool_value = noisy_clip(rng, p["heldout_tool_value"], 0.045, hi=1.2)
    train_tool_reliability = noisy_clip(rng, p["train_tool_reliability"], 0.040, hi=1.0)
    heldout_tool_reliability = noisy_clip(rng, p["heldout_tool_reliability"], 0.040, hi=1.0)
    internal_memory_value = noisy_clip(rng, p["internal_memory_value"], 0.040, hi=1.0)
    internal_memory_cost = noisy_clip(rng, p["internal_memory_cost"], 0.035, hi=1.0)
    tool_cost = noisy_clip(rng, p["tool_cost"], 0.025, hi=0.8)
    action_cost = noisy_clip(rng, p["action_cost"], 0.025, hi=0.7)

    train_tool_net = train_tool_value * train_tool_reliability - tool_cost - 0.5 * action_cost
    heldout_tool_net = heldout_tool_value * heldout_tool_reliability - tool_cost - 0.5 * action_cost
    internal_net = max(
        heldout_compression_value * compression_ratio - 0.35 * internal_memory_cost,
        internal_memory_value - internal_memory_cost,
    )
    resource_value = max(internal_net, train_tool_net, heldout_tool_net)
    tool_persistence_score = noisy_clip(
        rng,
        0.55 * heldout_tool_value + 0.55 * heldout_tool_reliability - 0.45 * tool_cost - 0.20 * action_cost,
        0.050,
        lo=-0.2,
        hi=1.4,
    )

    target_effort_clean = float(
        np.clip(
            sigmoid(2.4 * memory_load + 2.1 * capacity_pressure + 1.0 * max(train_tool_net, internal_net) - 2.0)
            + 0.05 * p["externalize"],
            0.0,
            1.0,
        )
    )
    target_externalize_clean = float(p["externalize"])
    if source == "tool_world":
        operation = "externalize"
    elif source == "compress_world":
        operation = "compress"
    elif source == "bait_world":
        operation = "resist_bait"
    else:
        operation = "commit"

    return Episode(
        source=source,
        operation=operation,
        scalar_score=noisy_clip(rng, 1.0, 0.020, lo=0.92, hi=1.08),
        memory_load=memory_load,
        capacity_pressure=capacity_pressure,
        compression_ratio=compression_ratio,
        train_compression_value=train_compression_value,
        heldout_compression_value=heldout_compression_value,
        train_tool_value=train_tool_value,
        heldout_tool_value=heldout_tool_value,
        train_tool_reliability=train_tool_reliability,
        heldout_tool_reliability=heldout_tool_reliability,
        internal_memory_value=internal_memory_value,
        internal_memory_cost=internal_memory_cost,
        tool_cost=tool_cost,
        action_cost=action_cost,
        resource_value=resource_value,
        tool_persistence_score=tool_persistence_score,
        target_effort_clean=target_effort_clean,
        target_effort_observed=float(np.clip(target_effort_clean + rng.normal(scale=effort_noise), 0.0, 1.0)),
        target_externalize_clean=target_externalize_clean,
        target_externalize_observed=float(np.clip(target_externalize_clean + rng.normal(scale=external_noise), 0.0, 1.0)),
    )


def make_dataset(
    rng: np.random.Generator,
    route_trials: int,
    null_trials: int,
    tool_mix: float,
    compress_share: float,
    effort_noise: float,
    external_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    for _ in range(route_trials):
        if rng.random() < tool_mix:
            source = "tool_world"
        elif rng.random() < compress_share:
            source = "compress_world"
        else:
            source = "bait_world"
        episodes.append(make_episode(rng, source, effort_noise=effort_noise, external_noise=external_noise))
    for _ in range(null_trials):
        episodes.append(make_episode(rng, "no_capacity_world", effort_noise=effort_noise, external_noise=external_noise))
    rng.shuffle(episodes)
    return episodes


def feature_matrix(episodes: list[Episode], feature_kind: str, tool_gate: float) -> np.ndarray:
    rows: list[list[float]] = []
    for e in episodes:
        admitted = 1.0 if e.tool_persistence_score > tool_gate else 0.0
        admitted_score = admitted * e.tool_persistence_score
        train_tool_net = e.train_tool_value * e.train_tool_reliability - e.tool_cost - 0.5 * e.action_cost
        train_internal_net = max(
            e.train_compression_value * e.compression_ratio - 0.35 * e.internal_memory_cost,
            e.internal_memory_value - e.internal_memory_cost,
        )
        continuous = [
            e.scalar_score,
            e.memory_load,
            e.capacity_pressure,
            e.compression_ratio,
            e.train_compression_value,
            e.train_tool_value,
            e.train_tool_reliability,
            e.internal_memory_value,
            e.internal_memory_cost,
            e.tool_cost,
            e.action_cost,
            train_tool_net,
            train_internal_net,
            e.resource_value,
        ]
        if feature_kind == "scalar":
            row = [e.scalar_score]
        elif feature_kind == "continuous_resource":
            row = continuous
        elif feature_kind == "external_tool_gate":
            row = [e.scalar_score, admitted, admitted_score]
        elif feature_kind == "governed_resource_gate":
            row = continuous + [admitted, admitted_score]
        elif feature_kind == "hybrid_resource_tool":
            heldout_tool_net = e.heldout_tool_value * e.heldout_tool_reliability - e.tool_cost - 0.5 * e.action_cost
            heldout_internal_net = max(
                e.heldout_compression_value * e.compression_ratio - 0.35 * e.internal_memory_cost,
                e.internal_memory_value - e.internal_memory_cost,
            )
            row = continuous + [
                e.heldout_tool_value,
                e.heldout_tool_reliability,
                e.heldout_compression_value,
                heldout_tool_net,
                heldout_internal_net,
                e.tool_persistence_score,
                admitted,
                admitted_score,
            ]
        else:
            raise ValueError(f"unknown feature kind: {feature_kind}")
        rows.append(row)
    return np.asarray(rows, dtype=float)


def target_vector(episodes: list[Episode], target_kind: str, observed: bool) -> np.ndarray:
    if target_kind == "effort":
        attr = "target_effort_observed" if observed else "target_effort_clean"
    elif target_kind == "externalize":
        attr = "target_externalize_observed" if observed else "target_externalize_clean"
    else:
        raise ValueError(f"unknown target kind: {target_kind}")
    return np.asarray([getattr(e, attr) for e in episodes], dtype=float)


def standardize_train(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = np.mean(x, axis=0)
    sd = np.std(x, axis=0)
    sd = np.where(sd < 1e-12, 1.0, sd)
    return (x - mean) / sd, mean, sd


def fit_linear_model(
    name: str,
    feature_kind: str,
    target_kind: str,
    train: list[Episode],
    tool_gate: float,
    ridge: float,
) -> LinearModel:
    x = feature_matrix(train, feature_kind, tool_gate=tool_gate)
    y = target_vector(train, target_kind, observed=True)
    xs, mean, sd = standardize_train(x)
    design = np.column_stack([np.ones(len(xs)), xs])
    gram = design.T @ design
    reg = ridge * np.eye(gram.shape[0])
    reg[0, 0] = 0.0
    coef = np.linalg.solve(gram + reg, design.T @ y)
    return LinearModel(
        name=name,
        feature_kind=feature_kind,
        target_kind=target_kind,
        coef=[float(v) for v in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
    )


def predict(model: LinearModel, episodes: list[Episode], tool_gate: float) -> np.ndarray:
    x = feature_matrix(episodes, model.feature_kind, tool_gate=tool_gate)
    mean = np.asarray(model.mean, dtype=float)
    sd = np.asarray(model.sd, dtype=float)
    xs = (x - mean) / sd
    design = np.column_stack([np.ones(len(xs)), xs])
    coef = np.asarray(model.coef, dtype=float)
    return np.clip(design @ coef, -0.25, 1.25)


def regression_metrics(y_obs: np.ndarray, y_clean: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    rmse_obs = float(np.sqrt(np.mean((pred - y_obs) ** 2)))
    rmse_clean = float(np.sqrt(np.mean((pred - y_clean) ** 2)))
    denom = float(np.sum((y_obs - float(np.mean(y_obs))) ** 2))
    r2 = 1.0 - float(np.sum((pred - y_obs) ** 2)) / denom if denom > 1e-12 else float("nan")
    return {"rmse_observed": rmse_obs, "rmse_clean": rmse_clean, "r2_observed": r2}


def externalize_metrics(episodes: list[Episode], pred: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([e.target_externalize_clean > 0.5 for e in episodes], dtype=bool)
    predicted = np.asarray([v >= threshold for v in pred], dtype=bool)
    source = np.asarray([e.source for e in episodes], dtype=object)

    def mean_mask(mask: np.ndarray, values: np.ndarray) -> float:
        return float(np.mean(values[mask])) if np.any(mask) else float("nan")

    tool = source == "tool_world"
    bait = source == "bait_world"
    compress = source == "compress_world"
    no_capacity = source == "no_capacity_world"
    non_tool = ~tool
    return {
        "accuracy": float(np.mean(predicted == truth)),
        "externalize_detection": mean_mask(tool, predicted),
        "nonexternal_false_admission": mean_mask(non_tool, predicted),
        "bait_false_admission": mean_mask(bait, predicted),
        "compress_false_admission": mean_mask(compress, predicted),
        "no_capacity_false_admission": mean_mask(no_capacity, predicted),
    }


def evaluate_models(
    train: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    external_threshold: float,
) -> dict[str, Any]:
    non_tool_scores = [e.tool_persistence_score for e in train if e.source != "tool_world"]
    tool_gate = quantile(non_tool_scores, 1.0 - alpha)

    models: dict[str, dict[str, LinearModel]] = {}
    predictions: dict[str, dict[str, np.ndarray]] = {}
    for name in MODEL_ORDER:
        models[name] = {}
        predictions[name] = {}
        for target in ["effort", "externalize"]:
            model = fit_linear_model(name, name, target, train, tool_gate=tool_gate, ridge=ridge)
            models[name][target] = model
            predictions[name][target] = predict(model, test, tool_gate=tool_gate)

    y_effort_obs = target_vector(test, "effort", observed=True)
    y_effort_clean = target_vector(test, "effort", observed=False)
    y_ext_obs = target_vector(test, "externalize", observed=True)
    y_ext_clean = target_vector(test, "externalize", observed=False)

    overall: dict[str, dict[str, Any]] = {}
    for name in MODEL_ORDER:
        effort = regression_metrics(y_effort_obs, y_effort_clean, predictions[name]["effort"])
        ext_reg = regression_metrics(y_ext_obs, y_ext_clean, predictions[name]["externalize"])
        ext_cls = externalize_metrics(test, predictions[name]["externalize"], threshold=external_threshold)
        overall[name] = {
            "effort": effort,
            "externalize_regression": ext_reg,
            "externalize_classification": ext_cls,
        }

    by_source: dict[str, dict[str, dict[str, Any]]] = {}
    for source in SOURCES:
        rows = [e for e in test if e.source == source]
        if not rows:
            continue
        idx = np.asarray([i for i, e in enumerate(test) if e.source == source], dtype=int)
        by_source[source] = {}
        for name in MODEL_ORDER:
            by_source[source][name] = {
                "effort": regression_metrics(
                    y_effort_obs[idx],
                    y_effort_clean[idx],
                    predictions[name]["effort"][idx],
                ),
                "externalize": externalize_metrics(rows, predictions[name]["externalize"][idx], threshold=external_threshold),
            }

    effort_winner = min(MODEL_ORDER, key=lambda name: overall[name]["effort"]["rmse_observed"])
    externalize_winner = min(
        MODEL_ORDER,
        key=lambda name: (
            overall[name]["externalize_classification"]["nonexternal_false_admission"],
            -overall[name]["externalize_classification"]["externalize_detection"],
            overall[name]["externalize_regression"]["rmse_observed"],
        ),
    )

    return {
        "tool_gate": tool_gate,
        "models": {
            name: {target: model.__dict__ for target, model in target_models.items()}
            for name, target_models in models.items()
        },
        "overall": overall,
        "by_source": by_source,
        "effort_winner": effort_winner,
        "externalize_winner": externalize_winner,
        "prediction_sample": {
            name: {target: [float(v) for v in predictions[name][target][:8]] for target in ["effort", "externalize"]}
            for name in MODEL_ORDER
        },
    }


def source_counts(episodes: list[Episode]) -> dict[str, int]:
    return {source: sum(1 for e in episodes if e.source == source) for source in SOURCES}


def source_means(episodes: list[Episode]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for source in SOURCES:
        rows = [e for e in episodes if e.source == source]
        if not rows:
            continue
        out[source] = {
            "scalar": float(np.mean([e.scalar_score for e in rows])),
            "memory_load": float(np.mean([e.memory_load for e in rows])),
            "capacity_pressure": float(np.mean([e.capacity_pressure for e in rows])),
            "train_tool_value": float(np.mean([e.train_tool_value for e in rows])),
            "heldout_tool_value": float(np.mean([e.heldout_tool_value for e in rows])),
            "train_tool_reliability": float(np.mean([e.train_tool_reliability for e in rows])),
            "heldout_tool_reliability": float(np.mean([e.heldout_tool_reliability for e in rows])),
            "heldout_compression_value": float(np.mean([e.heldout_compression_value for e in rows])),
            "tool_persistence_score": float(np.mean([e.tool_persistence_score for e in rows])),
            "target_effort": float(np.mean([e.target_effort_clean for e in rows])),
            "target_externalize": float(np.mean([e.target_externalize_clean for e in rows])),
        }
    return out


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    main_train = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        tool_mix=args.main_tool_mix,
        compress_share=args.compress_share,
        effort_noise=args.effort_noise,
        external_noise=args.external_noise,
    )
    main_test = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        tool_mix=args.main_tool_mix,
        compress_share=args.compress_share,
        effort_noise=args.effort_noise,
        external_noise=args.external_noise,
    )
    main_eval = evaluate_models(
        main_train,
        main_test,
        alpha=args.alpha,
        ridge=args.ridge,
        external_threshold=args.external_threshold,
    )

    sweep: list[dict[str, Any]] = []
    for mix in args.mix_grid:
        train = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            tool_mix=float(mix),
            compress_share=args.compress_share,
            effort_noise=args.effort_noise,
            external_noise=args.external_noise,
        )
        test = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            tool_mix=float(mix),
            compress_share=args.compress_share,
            effort_noise=args.effort_noise,
            external_noise=args.external_noise,
        )
        ev = evaluate_models(
            train,
            test,
            alpha=args.alpha,
            ridge=args.ridge,
            external_threshold=args.external_threshold,
        )
        sweep.append(
            {
                "tool_mix": float(mix),
                "counts": source_counts(test),
                "effort_winner": ev["effort_winner"],
                "externalize_winner": ev["externalize_winner"],
                "tool_gate": ev["tool_gate"],
                "effort_rmse": {
                    name: ev["overall"][name]["effort"]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "externalize_false_admission": {
                    name: ev["overall"][name]["externalize_classification"]["nonexternal_false_admission"]
                    for name in MODEL_ORDER
                },
                "externalize_detection": {
                    name: ev["overall"][name]["externalize_classification"]["externalize_detection"]
                    for name in MODEL_ORDER
                },
                "bait_false_admission": {
                    name: ev["overall"][name]["externalize_classification"]["bait_false_admission"]
                    for name in MODEL_ORDER
                },
            }
        )

    continuous_effort = main_eval["overall"]["continuous_resource"]["effort"]["rmse_observed"]
    gate_effort = main_eval["overall"]["external_tool_gate"]["effort"]["rmse_observed"]
    hybrid_effort = main_eval["overall"]["hybrid_resource_tool"]["effort"]["rmse_observed"]
    continuous_false = main_eval["overall"]["continuous_resource"]["externalize_classification"]["nonexternal_false_admission"]
    gate_false = main_eval["overall"]["external_tool_gate"]["externalize_classification"]["nonexternal_false_admission"]
    governed_false = main_eval["overall"]["governed_resource_gate"]["externalize_classification"]["nonexternal_false_admission"]
    continuous_detection = main_eval["overall"]["continuous_resource"]["externalize_classification"]["externalize_detection"]
    gate_detection = main_eval["overall"]["external_tool_gate"]["externalize_classification"]["externalize_detection"]
    governed_detection = main_eval["overall"]["governed_resource_gate"]["externalize_classification"]["externalize_detection"]
    continuous_bait_false = main_eval["overall"]["continuous_resource"]["externalize_classification"]["bait_false_admission"]
    gate_bait_false = main_eval["overall"]["external_tool_gate"]["externalize_classification"]["bait_false_admission"]

    if (
        continuous_effort + args.decision_margin < gate_effort
        and (continuous_detection < args.detection_floor or continuous_false > gate_false + args.false_admission_margin)
        and governed_detection >= args.detection_floor
        and governed_false <= args.alpha * 1.5
    ):
        finding = "RESOURCE_FITS_BUT_GATE_RECOVERS_EXTERNALIZATION"
    elif (
        continuous_effort + args.decision_margin < gate_effort
        and continuous_false <= args.alpha * 1.5
        and continuous_detection >= args.detection_floor
    ):
        finding = "CONTINUOUS_RESOURCE_RIVAL_WINS"
    elif (
        gate_effort <= continuous_effort + args.decision_margin
        and gate_false <= args.alpha * 1.5
        and gate_detection >= args.detection_floor
    ):
        finding = "DISCRETE_CAPACITY_BUCKET_SURVIVES"
    elif (
        hybrid_effort + args.decision_margin < continuous_effort
        and governed_false <= continuous_false - args.false_admission_margin
        and governed_detection >= args.detection_floor
    ):
        finding = "HYBRID_RESOURCE_GATE_NEEDED"
    else:
        finding = "RIVAL_MATCH_BUCKET_NOT_UNIQUE"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "finding": finding,
        "config": {
            "seed": args.seed,
            "route_trials": args.route_trials,
            "null_trials": args.null_trials,
            "sweep_route_trials": args.sweep_route_trials,
            "sweep_null_trials": args.sweep_null_trials,
            "main_tool_mix": args.main_tool_mix,
            "compress_share": args.compress_share,
            "mix_grid": [float(v) for v in args.mix_grid],
            "effort_noise": args.effort_noise,
            "external_noise": args.external_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "external_threshold": args.external_threshold,
            "decision_margin": args.decision_margin,
            "false_admission_margin": args.false_admission_margin,
            "detection_floor": args.detection_floor,
        },
        "main_train_counts": source_counts(main_train),
        "main_test_counts": source_counts(main_test),
        "main_train_means": source_means(main_train),
        "main_test_means": source_means(main_test),
        "main_eval": main_eval,
        "decision_quantities": {
            "continuous_effort_rmse": continuous_effort,
            "gate_effort_rmse": gate_effort,
            "hybrid_effort_rmse": hybrid_effort,
            "continuous_false_externalize": continuous_false,
            "gate_false_externalize": gate_false,
            "governed_false_externalize": governed_false,
            "continuous_externalize_detection": continuous_detection,
            "gate_externalize_detection": gate_detection,
            "governed_externalize_detection": governed_detection,
            "continuous_bait_false": continuous_bait_false,
            "gate_bait_false": gate_bait_false,
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
    dq = result["decision_quantities"]

    model_rows = []
    for name in MODEL_ORDER:
        overall = main["overall"][name]
        effort = overall["effort"]
        ext_reg = overall["externalize_regression"]
        ext = overall["externalize_classification"]
        model_rows.append(
            [
                name,
                fmt(effort["rmse_observed"]),
                fmt(effort["r2_observed"]),
                fmt(ext_reg["rmse_observed"]),
                fmt(ext["accuracy"]),
                fmt(ext["externalize_detection"]),
                fmt(ext["nonexternal_false_admission"]),
                fmt(ext["bait_false_admission"]),
                fmt(ext["compress_false_admission"]),
                fmt(ext["no_capacity_false_admission"]),
            ]
        )

    source_rows = []
    for source, data in result["main_test_means"].items():
        source_rows.append(
            [
                source,
                fmt(data["scalar"]),
                fmt(data["memory_load"]),
                fmt(data["capacity_pressure"]),
                fmt(data["train_tool_value"]),
                fmt(data["heldout_tool_value"]),
                fmt(data["train_tool_reliability"]),
                fmt(data["heldout_tool_reliability"]),
                fmt(data["heldout_compression_value"]),
                fmt(data["tool_persistence_score"]),
                fmt(data["target_effort"]),
                fmt(data["target_externalize"]),
            ]
        )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["tool_mix"]),
                row["effort_winner"],
                row["externalize_winner"],
                fmt(row["effort_rmse"]["continuous_resource"]),
                fmt(row["effort_rmse"]["external_tool_gate"]),
                fmt(row["effort_rmse"]["hybrid_resource_tool"]),
                fmt(row["externalize_false_admission"]["continuous_resource"]),
                fmt(row["externalize_false_admission"]["external_tool_gate"]),
                fmt(row["externalize_detection"]["external_tool_gate"]),
                fmt(row["bait_false_admission"]["continuous_resource"]),
            ]
        )

    lines = [
        "# E13 Capacity Resource-Rational Falsifier",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- main tool mix: `{config['main_tool_mix']}`",
        f"- compress share: `{config['compress_share']}`",
        f"- route/null trials: `{config['route_trials']}` / `{config['null_trials']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E13 tests whether capacity/compression/tool-use survives a strong",
        "continuous resource-rational rival. The rival sees memory load,",
        "capacity pressure, compression value, train-side tool value, tool cost,",
        "and action cost. The externalization gate sees held-out tool persistence",
        "calibrated on non-tool worlds.",
        "",
        "The probe scores two jobs separately: predicting graded resource effort",
        "and admitting a persistent external tool route.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous effort RMSE", fmt(dq["continuous_effort_rmse"])],
                ["gate effort RMSE", fmt(dq["gate_effort_rmse"])],
                ["hybrid effort RMSE", fmt(dq["hybrid_effort_rmse"])],
                ["continuous false externalize", fmt(dq["continuous_false_externalize"])],
                ["gate false externalize", fmt(dq["gate_false_externalize"])],
                ["governed false externalize", fmt(dq["governed_false_externalize"])],
                ["continuous externalize detection", fmt(dq["continuous_externalize_detection"])],
                ["gate externalize detection", fmt(dq["gate_externalize_detection"])],
                ["governed externalize detection", fmt(dq["governed_externalize_detection"])],
                ["continuous bait false", fmt(dq["continuous_bait_false"])],
                ["gate bait false", fmt(dq["gate_bait_false"])],
                ["conformal tool gate", fmt(main["tool_gate"])],
            ],
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "effort RMSE",
                "effort R2",
                "external RMSE",
                "external acc",
                "tool detect",
                "non-tool FA",
                "bait FA",
                "compress FA",
                "no-cap FA",
            ],
            model_rows,
        ),
        "",
        "## Source Means",
        "",
        md_table(
            [
                "source",
                "scalar",
                "memory load",
                "capacity",
                "train tool",
                "heldout tool",
                "train rel",
                "heldout rel",
                "heldout compress",
                "tool score",
                "target effort",
                "target external",
            ],
            source_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "tool mix",
                "effort winner",
                "external winner",
                "cont effort",
                "gate effort",
                "hybrid effort",
                "cont FA",
                "gate FA",
                "gate detect",
                "cont bait FA",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    finding = result["finding"]
    if finding == "RESOURCE_FITS_BUT_GATE_RECOVERS_EXTERNALIZATION":
        lines.extend(
            [
                "Continuous resource-rational variables win the graded effort",
                "problem, but train-side utility alone confuses stable tools with",
                "bait. The held-out externalization gate recovers persistent tool",
                "use while controlling false admission. E13 therefore supports",
                "governed resource control: resource rationality explains load,",
                "while tool persistence decides when cognition should externalize.",
            ]
        )
    elif finding == "CONTINUOUS_RESOURCE_RIVAL_WINS":
        lines.extend(
            [
                "The continuous resource-rational rival predicts both effort and",
                "externalization while controlling false tool use. This would",
                "demote the capacity bucket to a descriptive cost discretization.",
            ]
        )
    elif finding == "DISCRETE_CAPACITY_BUCKET_SURVIVES":
        lines.extend(
            [
                "The discrete gate controls false admission and does not lose the",
                "effort task. This would support a stronger primitive capacity route.",
            ]
        )
    elif finding == "HYBRID_RESOURCE_GATE_NEEDED":
        lines.extend(
            [
                "The hybrid resource-plus-gate model is needed. That supports the",
                "two-level hypothesis: continuous resource control supplies effort,",
                "and held-out tool persistence supplies route admission.",
            ]
        )
    else:
        lines.extend(
            [
                "The resource rival and externalization gate are too close. Capacity",
                "bucket uniqueness is not established.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- scalar surprise is matched by construction;",
            "- tool worlds and bait worlds both have high train-side tool value;",
            "- compression worlds provide an internal resource competitor;",
            "- the continuous rival sees cost and train utility, but not held-out tool persistence;",
            "- the tool gate is calibrated on held-out non-tool scores;",
            "- the phase sweep includes worlds where resource rationality should win.",
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
    parser.add_argument("--main-tool-mix", type=float, default=0.50)
    parser.add_argument("--compress-share", type=float, default=0.45)
    parser.add_argument("--mix-grid", type=float, nargs="+", default=[0.0, 0.25, 0.5, 0.75, 1.0])
    parser.add_argument("--effort-noise", type=float, default=0.045)
    parser.add_argument("--external-noise", type=float, default=0.040)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--external-threshold", type=float, default=0.50)
    parser.add_argument("--decision-margin", type=float, default=0.010)
    parser.add_argument("--false-admission-margin", type=float, default=0.050)
    parser.add_argument("--detection-floor", type=float, default=0.850)
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
    json_path = args.report_dir / "e13_capacity_resource_falsifier.json"
    md_path = args.report_dir / "e13_capacity_resource_falsifier.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
