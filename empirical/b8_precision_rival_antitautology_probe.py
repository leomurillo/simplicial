"""B8 precision-rival anti-tautology probe.

This probe is intentionally adversarial to the B-series bucket story.

Earlier B probes showed that bucket routers win when synthetic episodes are
generated from matching diagnostic channels. That is useful as a unit test, but
it risks tautology. B8 removes the semantic channel labels from the decision
problem and asks the harder question:

    Does an unlabeled bucket router beat a continuous precision-weighted active
    inference rival, or are the buckets just a readable discretization of a
    continuous precision/cost policy?

Every episode exposes a shuffled bank of candidate affordances. The agents do
not receive the true bucket label. They see train/held-out predictive gains,
candidate affordance ports, costs, and a governance port. The strongest rival,
precision_active_inference, chooses the best continuous gain-minus-cost policy.
If it ties the bucket router, the honest result is not "bucket confirmation";
it is "bucket uniqueness not established."
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["retained", "packet", "action", "tool", "forbidden", "noise"]
PORTS = ["retained", "internal", "active", "external", "forbidden"]
OPERATIONS = {
    "retained": "reweight",
    "packet": "close",
    "action": "act",
    "tool": "externalize",
    "forbidden": "inhibit",
    "noise": "suppress",
}
GOVERNED_PORT_OPERATION = {
    "retained": "reweight",
    "internal": "close",
    "active": "act",
    "external": "externalize",
    "forbidden": "inhibit",
}
UNGOVERNED_PORT_OPERATION = {
    "retained": "reweight",
    "internal": "close",
    "active": "act",
    "external": "externalize",
    "forbidden": "close",
}


@dataclass(frozen=True)
class Candidate:
    port: str
    train_feature: np.ndarray
    test_feature: np.ndarray
    is_train_bait: bool = False


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    true_port: str
    scalar_surprise: float
    aggregate_precision_gain: float
    best_train_port: str
    best_train_gain: float
    best_heldout_port: str
    best_heldout_gain: float
    heldout_gain_by_port: dict[str, float]
    train_gain_by_port: dict[str, float]
    train_bait_train_gain: float
    train_bait_heldout_gain: float
    candidate_count: int


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = float(np.std(x))
    if sd < 1e-12:
        return np.zeros_like(x)
    return (x - float(np.mean(x))) / sd


def standardize_columns(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return np.column_stack([standardize(x[:, j]) for j in range(x.shape[1])])


def fit_coef(feature: np.ndarray, residual: np.ndarray, lam: float = 1e-6) -> np.ndarray:
    feature = np.asarray(feature, dtype=float)
    if feature.ndim == 1:
        feature = feature[:, None]
    gram = feature.T @ feature
    rhs = feature.T @ residual
    reg = gram + lam * np.eye(gram.shape[0])
    try:
        return np.linalg.solve(reg, rhs)
    except np.linalg.LinAlgError:
        return np.linalg.pinv(reg) @ rhs


def train_gain(feature: np.ndarray, residual: np.ndarray, lam: float = 1e-6) -> float:
    feature = np.asarray(feature, dtype=float)
    if feature.ndim == 1:
        feature = feature[:, None]
    coef = fit_coef(feature, residual, lam)
    base = float(np.mean(residual**2))
    improved = float(np.mean((residual - feature @ coef) ** 2))
    return base - improved


def heldout_gain(
    train_feature: np.ndarray,
    train_residual: np.ndarray,
    test_feature: np.ndarray,
    test_residual: np.ndarray,
    lam: float = 1e-6,
) -> float:
    train_feature = np.asarray(train_feature, dtype=float)
    test_feature = np.asarray(test_feature, dtype=float)
    if train_feature.ndim == 1:
        train_feature = train_feature[:, None]
    if test_feature.ndim == 1:
        test_feature = test_feature[:, None]
    coef = fit_coef(train_feature, train_residual, lam)
    base = float(np.mean(test_residual**2))
    improved = float(np.mean((test_residual - test_feature @ coef) ** 2))
    return base - improved


def onehot(keys: np.ndarray, n_keys: int) -> np.ndarray:
    out = np.zeros((len(keys), n_keys), dtype=float)
    out[np.arange(len(keys)), keys] = 1.0
    return out


def make_base(
    rng: np.random.Generator,
    n: int,
    n_keys: int,
    tool_table: np.ndarray,
) -> dict[str, np.ndarray]:
    z = rng.normal(size=(n, 10))
    keys = rng.integers(0, n_keys, size=n)
    return {
        "z": z,
        "retained": standardize(z[:, 0]),
        "packet": standardize(z[:, 1] * z[:, 2]),
        "action": standardize(np.sin(z[:, 3]) + 0.25 * z[:, 4]),
        "forbidden": standardize(z[:, 5] * z[:, 6]),
        "tool": standardize(tool_table[keys]),
        "keys": keys,
        "key_onehot": onehot(keys, n_keys),
    }


def signal_for_kind(kind: str, base: dict[str, np.ndarray], rng: np.random.Generator) -> np.ndarray:
    if kind == "retained":
        return base["retained"]
    if kind == "packet":
        return base["packet"]
    if kind == "action":
        return base["action"]
    if kind == "tool":
        return base["tool"]
    if kind == "forbidden":
        return base["forbidden"]
    if kind == "noise":
        return standardize(rng.normal(size=len(base["retained"])))
    raise ValueError(f"unknown kind: {kind}")


def make_candidates(
    rng: np.random.Generator,
    train_base: dict[str, np.ndarray],
    test_base: dict[str, np.ndarray],
    n_keys: int,
    train_y: np.ndarray,
    test_y: np.ndarray,
    n_distractors: int,
) -> list[Candidate]:
    train_z = train_base["z"]
    test_z = test_base["z"]
    candidates = [
        Candidate("retained", train_base["retained"], test_base["retained"]),
        Candidate("internal", train_base["packet"], test_base["packet"]),
        Candidate("active", train_base["action"], test_base["action"]),
        Candidate("external", train_base["tool"], test_base["tool"]),
        Candidate("forbidden", train_base["forbidden"], test_base["forbidden"]),
    ]

    for _ in range(n_distractors):
        i, j = rng.choice(train_z.shape[1], size=2, replace=False)
        port = str(rng.choice(PORTS))
        train_feature = standardize(train_z[:, i] * train_z[:, j] + 0.15 * rng.normal(size=len(train_y)))
        test_feature = standardize(test_z[:, i] * test_z[:, j] + 0.15 * rng.normal(size=len(test_y)))
        candidates.append(Candidate(port, train_feature, test_feature))

    for _ in range(max(2, n_distractors // 3)):
        train_keys = train_base["keys"]
        test_keys = test_base["keys"]
        table = standardize(rng.normal(size=n_keys))
        candidates.append(Candidate("external", table[train_keys], table[test_keys]))

    bait_train = standardize(train_y + 0.04 * rng.normal(size=len(train_y)))
    bait_test = standardize(rng.normal(size=len(test_y)))
    candidates.append(Candidate(str(rng.choice(["internal", "active", "external"])), bait_train, bait_test, True))

    order = rng.permutation(len(candidates))
    return [candidates[i] for i in order]


def operation_for_kind(kind: str) -> tuple[str, str]:
    if kind == "retained":
        return "retained", "reweight"
    if kind == "packet":
        return "internal", "close"
    if kind == "action":
        return "active", "act"
    if kind == "tool":
        return "external", "externalize"
    if kind == "forbidden":
        return "forbidden", "inhibit"
    if kind == "noise":
        return "none", "suppress"
    raise ValueError(f"unknown kind: {kind}")


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    n_keys: int,
    noise_scale: float,
    n_distractors: int,
    ridge_lambda: float,
) -> EpisodeMetrics:
    tool_table = standardize(rng.normal(size=n_keys))
    train_base = make_base(rng, n_train, n_keys, tool_table)
    test_base = make_base(rng, n_test, n_keys, tool_table)
    train_signal = signal_for_kind(kind, train_base, rng)
    test_signal = signal_for_kind(kind, test_base, rng)
    if kind == "noise":
        train_y = standardize(train_signal)
        test_y = standardize(test_signal)
    else:
        train_y = standardize(train_signal + noise_scale * rng.normal(size=n_train))
        test_y = standardize(test_signal + noise_scale * rng.normal(size=n_test))

    candidates = make_candidates(
        rng,
        train_base,
        test_base,
        n_keys,
        train_y,
        test_y,
        n_distractors,
    )
    train_features = standardize_columns(np.column_stack([c.train_feature for c in candidates]))
    test_features = standardize_columns(np.column_stack([c.test_feature for c in candidates]))
    aggregate_gain = heldout_gain(train_features, train_y, test_features, test_y, ridge_lambda)

    train_gain_by_port = {port: float("-inf") for port in PORTS}
    heldout_gain_by_port = {port: float("-inf") for port in PORTS}
    train_bait_train_gain = float("-inf")
    train_bait_heldout_gain = float("-inf")
    for candidate in candidates:
        tg = train_gain(candidate.train_feature, train_y, ridge_lambda)
        hg = heldout_gain(candidate.train_feature, train_y, candidate.test_feature, test_y, ridge_lambda)
        train_gain_by_port[candidate.port] = max(train_gain_by_port[candidate.port], float(tg))
        heldout_gain_by_port[candidate.port] = max(heldout_gain_by_port[candidate.port], float(hg))
        if candidate.is_train_bait:
            train_bait_train_gain = float(tg)
            train_bait_heldout_gain = float(hg)

    best_train_port, best_train_gain = max(train_gain_by_port.items(), key=lambda item: item[1])
    best_heldout_port, best_heldout_gain = max(heldout_gain_by_port.items(), key=lambda item: item[1])
    true_port, true_operation = operation_for_kind(kind)

    return EpisodeMetrics(
        kind=kind,
        true_operation=true_operation,
        true_port=true_port,
        scalar_surprise=float(np.mean(test_y**2)),
        aggregate_precision_gain=float(aggregate_gain),
        best_train_port=best_train_port,
        best_train_gain=float(best_train_gain),
        best_heldout_port=best_heldout_port,
        best_heldout_gain=float(best_heldout_gain),
        heldout_gain_by_port={k: float(v) for k, v in heldout_gain_by_port.items()},
        train_gain_by_port={k: float(v) for k, v in train_gain_by_port.items()},
        train_bait_train_gain=train_bait_train_gain,
        train_bait_heldout_gain=train_bait_heldout_gain,
        candidate_count=len(candidates),
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "true_port": m.true_port,
        "scalar_surprise": m.scalar_surprise,
        "aggregate_precision_gain": m.aggregate_precision_gain,
        "best_train_port": m.best_train_port,
        "best_train_gain": m.best_train_gain,
        "best_heldout_port": m.best_heldout_port,
        "best_heldout_gain": m.best_heldout_gain,
        "heldout_gain_by_port": m.heldout_gain_by_port,
        "train_gain_by_port": m.train_gain_by_port,
        "train_bait_train_gain": m.train_bait_train_gain,
        "train_bait_heldout_gain": m.train_bait_heldout_gain,
        "candidate_count": m.candidate_count,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def port_values(m: EpisodeMetrics, costs: dict[str, float], source: str = "heldout") -> dict[str, float]:
    gains = m.heldout_gain_by_port if source == "heldout" else m.train_gain_by_port
    return {port: gains[port] - costs[port] for port in PORTS}


def calibrate_thresholds(
    calibration: list[EpisodeMetrics],
    costs: dict[str, float],
    alpha: float,
) -> dict[str, Any]:
    null = [m for m in calibration if m.kind == "noise"]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    port_value_thresholds = {
        port: quantile([port_values(m, costs)[port] for m in null], q)
        for port in PORTS
    }
    route_margins = [
        max(port_values(m, costs)[port] - port_value_thresholds[port] for port in PORTS)
        for m in null
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "aggregate_precision": quantile([m.aggregate_precision_gain for m in null], q),
        "train_precision_value": quantile([max(port_values(m, costs, "train").values()) for m in null], q),
        "port_value": port_value_thresholds,
        "family_margin": quantile(route_margins, family_q),
    }


def best_port_by_value(m: EpisodeMetrics, costs: dict[str, float], source: str = "heldout") -> tuple[str, float]:
    values = port_values(m, costs, source)
    return max(values.items(), key=lambda item: item[1])


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, Any]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def train_precision_agent(
    m: EpisodeMetrics,
    thresholds: dict[str, Any],
    costs: dict[str, float],
) -> str:
    port, value = best_port_by_value(m, costs, "train")
    if value <= thresholds["train_precision_value"]:
        return "suppress"
    return UNGOVERNED_PORT_OPERATION[port]


def full_precision_matrix_agent(m: EpisodeMetrics, thresholds: dict[str, Any]) -> str:
    if m.aggregate_precision_gain <= thresholds["aggregate_precision"]:
        return "suppress"
    if m.best_heldout_port == "retained":
        return "reweight"
    return "close"


def precision_active_inference_agent(
    m: EpisodeMetrics,
    thresholds: dict[str, Any],
    costs: dict[str, float],
) -> str:
    port, value = best_port_by_value(m, costs, "heldout")
    if value <= thresholds["port_value"][port]:
        return "suppress"
    return GOVERNED_PORT_OPERATION[port]


def bucket_router_unlabeled_agent(
    m: EpisodeMetrics,
    thresholds: dict[str, Any],
    costs: dict[str, float],
) -> str:
    values = port_values(m, costs, "heldout")
    margins = {port: values[port] - thresholds["port_value"][port] for port in PORTS}
    port, margin = max(margins.items(), key=lambda item: item[1])
    if margin <= thresholds["family_margin"]:
        return "suppress"
    return GOVERNED_PORT_OPERATION[port]


def oracle_agent(m: EpisodeMetrics) -> str:
    return m.true_operation


def evaluate_predictions(metrics: list[EpisodeMetrics], predictions: dict[str, list[str]]) -> dict[str, Any]:
    truth = [m.true_operation for m in metrics]
    out: dict[str, Any] = {"agents": {}, "by_kind": {}}
    for agent, preds in predictions.items():
        out["agents"][agent] = {
            "routing_accuracy": float(np.mean([p == t for p, t in zip(preds, truth)])),
            "noise_false_admission": float(
                np.mean([p != "suppress" for p, m in zip(preds, metrics) if m.kind == "noise"])
            ),
            "train_bait_error": float(
                np.mean(
                    [
                        p != m.true_operation
                        for p, m in zip(preds, metrics)
                        if m.train_bait_train_gain > 0.75 and m.kind != "noise"
                    ]
                )
            ),
        }
        for op in sorted(set(OPERATIONS.values())):
            rows = [(p, m) for p, m in zip(preds, metrics) if m.true_operation == op]
            if rows:
                out["agents"][agent][f"{op}_success"] = float(np.mean([p == m.true_operation for p, m in rows]))

    for kind in KINDS:
        rows = [i for i, m in enumerate(metrics) if m.kind == kind]
        out["by_kind"][kind] = {
            agent: float(np.mean([predictions[agent][i] == truth[i] for i in rows]))
            for agent in predictions
        }
    return out


def auc(labels: list[int], scores: list[float]) -> float:
    pos = [s for y, s in zip(labels, scores) if y == 1]
    neg = [s for y, s in zip(labels, scores) if y == 0]
    if not pos or not neg:
        return float("nan")
    wins = 0.0
    total = len(pos) * len(neg)
    for p in pos:
        for n in neg:
            if p > n:
                wins += 1.0
            elif p == n:
                wins += 0.5
    return wins / total


def make_predictions(
    metrics: list[EpisodeMetrics],
    thresholds: dict[str, Any],
    costs: dict[str, float],
) -> dict[str, list[str]]:
    return {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "train_precision": [train_precision_agent(m, thresholds, costs) for m in metrics],
        "full_precision_matrix": [full_precision_matrix_agent(m, thresholds) for m in metrics],
        "precision_active_inference": [
            precision_active_inference_agent(m, thresholds, costs) for m in metrics
        ],
        "bucket_router_unlabeled": [
            bucket_router_unlabeled_agent(m, thresholds, costs) for m in metrics
        ],
        "oracle": [oracle_agent(m) for m in metrics],
    }


def cost_sweep(
    calibration: list[EpisodeMetrics],
    metrics: list[EpisodeMetrics],
    base_costs: dict[str, float],
    alpha: float,
    multipliers: list[float],
) -> list[dict[str, Any]]:
    rows = []
    for multiplier in multipliers:
        costs = {k: v * multiplier for k, v in base_costs.items()}
        thresholds = calibrate_thresholds(calibration, costs, alpha)
        predictions = make_predictions(metrics, thresholds, costs)
        evaluated = evaluate_predictions(metrics, predictions)
        rows.append(
            {
                "cost_multiplier": multiplier,
                "precision_active_accuracy": evaluated["agents"]["precision_active_inference"]["routing_accuracy"],
                "bucket_accuracy": evaluated["agents"]["bucket_router_unlabeled"]["routing_accuracy"],
                "precision_active_noise_false_admission": evaluated["agents"]["precision_active_inference"]["noise_false_admission"],
                "bucket_noise_false_admission": evaluated["agents"]["bucket_router_unlabeled"]["noise_false_admission"],
            }
        )
    return rows


def summarize(
    calibration: list[EpisodeMetrics],
    metrics: list[EpisodeMetrics],
    thresholds: dict[str, Any],
    costs: dict[str, float],
    alpha: float,
) -> dict[str, Any]:
    predictions = make_predictions(metrics, thresholds, costs)
    evaluated = evaluate_predictions(metrics, predictions)
    labels_non_noise = [0 if m.kind == "noise" else 1 for m in metrics]
    active = evaluated["agents"]["precision_active_inference"]
    bucket = evaluated["agents"]["bucket_router_unlabeled"]
    rival_gap = bucket["routing_accuracy"] - active["routing_accuracy"]

    summary = {
        **evaluated,
        "auc": {
            "scalar_non_noise_vs_noise": auc(labels_non_noise, [m.scalar_surprise for m in metrics]),
            "aggregate_precision_non_noise_vs_noise": auc(
                labels_non_noise,
                [m.aggregate_precision_gain for m in metrics],
            ),
            "best_heldout_non_noise_vs_noise": auc(labels_non_noise, [m.best_heldout_gain for m in metrics]),
            "train_bait_train_vs_heldout": auc(
                [1 if m.kind != "noise" else 0 for m in metrics],
                [m.train_bait_train_gain - m.train_bait_heldout_gain for m in metrics],
            ),
        },
        "mean_scores_by_kind": {
            kind: {
                "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
                "aggregate_precision": float(
                    np.mean([m.aggregate_precision_gain for m in metrics if m.kind == kind])
                ),
                "best_heldout": float(np.mean([m.best_heldout_gain for m in metrics if m.kind == kind])),
                "train_bait_train": float(
                    np.mean([m.train_bait_train_gain for m in metrics if m.kind == kind])
                ),
                "train_bait_heldout": float(
                    np.mean([m.train_bait_heldout_gain for m in metrics if m.kind == kind])
                ),
            }
            for kind in KINDS
        },
        "cost_sweep": cost_sweep(
            calibration,
            metrics,
            costs,
            alpha,
            multipliers=[0.0, 0.5, 1.0, 1.5, 2.0, 3.0],
        ),
        "rival_gap": float(rival_gap),
    }

    summary["anti_tautology_checks"] = {
        "semantic_labels_removed": True,
        "train_bait_penalizes_train_precision": (
            summary["agents"]["train_precision"]["routing_accuracy"]
            < summary["agents"]["bucket_router_unlabeled"]["routing_accuracy"] - 0.15
        ),
        "scalar_still_blind": summary["agents"]["scalar"]["routing_accuracy"] <= 0.35,
        "continuous_rival_matches_bucket": (
            active["routing_accuracy"] >= 0.90 and abs(rival_gap) <= 0.05
        ),
        "bucket_uniqueness_not_established": (
            active["routing_accuracy"] >= 0.90 and abs(rival_gap) <= 0.05
        ),
        "bucket_controls_noise": bucket["noise_false_admission"] <= alpha,
    }
    if summary["anti_tautology_checks"]["bucket_uniqueness_not_established"]:
        summary["finding"] = "RIVAL_MATCH_BUCKET_NOT_UNIQUE"
    elif bucket["routing_accuracy"] > active["routing_accuracy"] + 0.05:
        summary["finding"] = "BUCKET_ADVANTAGE_UNDER_UNLABELED_CONTROLS"
    else:
        summary["finding"] = "INCONCLUSIVE"
    return summary


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def fmt(x: float) -> str:
    if isinstance(x, float) and np.isnan(x):
        return "nan"
    return f"{x:.3f}"


def write_report(
    path: Path,
    config: dict[str, Any],
    thresholds: dict[str, Any],
    costs: dict[str, float],
    summary: dict[str, Any],
) -> None:
    agent_rows = []
    for agent, data in summary["agents"].items():
        agent_rows.append(
            [
                agent,
                fmt(data["routing_accuracy"]),
                fmt(data["noise_false_admission"]),
                fmt(data.get("reweight_success", float("nan"))),
                fmt(data.get("close_success", float("nan"))),
                fmt(data.get("act_success", float("nan"))),
                fmt(data.get("externalize_success", float("nan"))),
                fmt(data.get("inhibit_success", float("nan"))),
            ]
        )

    kind_rows = []
    for kind, true_op in OPERATIONS.items():
        row = [kind, true_op]
        for agent in [
            "scalar",
            "train_precision",
            "full_precision_matrix",
            "precision_active_inference",
            "bucket_router_unlabeled",
            "oracle",
        ]:
            row.append(fmt(summary["by_kind"][kind][agent]))
        kind_rows.append(row)

    score_rows = []
    for kind, scores in summary["mean_scores_by_kind"].items():
        score_rows.append(
            [
                kind,
                fmt(scores["scalar"]),
                fmt(scores["aggregate_precision"]),
                fmt(scores["best_heldout"]),
                fmt(scores["train_bait_train"]),
                fmt(scores["train_bait_heldout"]),
            ]
        )

    sweep_rows = [
        [
            fmt(row["cost_multiplier"]),
            fmt(row["precision_active_accuracy"]),
            fmt(row["bucket_accuracy"]),
            fmt(row["precision_active_noise_false_admission"]),
            fmt(row["bucket_noise_false_admission"]),
        ]
        for row in summary["cost_sweep"]
    ]

    checks = [[name, "yes" if value else "no"] for name, value in summary["anti_tautology_checks"].items()]
    port_threshold_rows = [
        [port, fmt(value)]
        for port, value in thresholds["port_value"].items()
    ]

    text = f"""# B8 Precision-Rival Anti-Tautology Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration trials per kind: `{config['calibration_trials_per_kind']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- distractors per episode: `{config['n_distractors']}`
- lookup keys: `{config['n_keys']}`
- noise scale: `{config['noise_scale']}`
- alpha: `{config['alpha']}`
- finding: **{summary['finding']}**

## Claim Tested

B8 asks whether the B-series bucket router still has unique operational bite
after semantic channel labels are removed. Agents see shuffled candidate
affordances, held-out predictive gains, costs, and governance ports. They do
not receive the true episode bucket.

## Costs

{md_table(['port', 'cost'], [[k, fmt(v)] for k, v in costs.items()])}

## Conformal / Precision Thresholds

{md_table(['threshold', 'value'], [['scalar', fmt(thresholds['scalar'])], ['aggregate_precision', fmt(thresholds['aggregate_precision'])], ['train_precision_value', fmt(thresholds['train_precision_value'])], ['family_margin', fmt(thresholds['family_margin'])]])}

{md_table(['port', 'value threshold'], port_threshold_rows)}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'reweight', 'close', 'act', 'externalize', 'inhibit'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'train precision', 'full precision matrix', 'precision active inference', 'bucket router unlabeled', 'oracle'], kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'aggregate precision', 'best heldout', 'bait train', 'bait heldout'], score_rows)}

## Cost Sweep

{md_table(['cost multiplier', 'precision active acc', 'bucket acc', 'precision active noise FA', 'bucket noise FA'], sweep_rows)}

## Anti-Tautology Checks

{md_table(['check', 'result'], checks)}

## Interpretation

The key quantity is not whether the bucket router scores well. The key quantity
is whether it beats a continuous precision-active rival once labels are removed.

Here, **{summary['finding']}**. If the precision-active rival matches the
unlabeled bucket router, B8 does not support bucket uniqueness. It supports the
weaker and safer claim that bucket language is an operational discretization of
a continuous precision/cost control problem.

This is exactly the uncomfortable outcome B8 was built to detect.
"""
    path.write_text(text, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-kind", type=int, default=260)
    parser.add_argument("--calibration-trials-per-kind", type=int, default=260)
    parser.add_argument("--n-train", type=int, default=96)
    parser.add_argument("--n-test", type=int, default=96)
    parser.add_argument("--n-keys", type=int, default=48)
    parser.add_argument("--n-distractors", type=int, default=16)
    parser.add_argument("--noise-scale", type=float, default=0.35)
    parser.add_argument("--ridge-lambda", type=float, default=0.05)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--retained-cost", type=float, default=0.03)
    parser.add_argument("--internal-cost", type=float, default=0.08)
    parser.add_argument("--active-cost", type=float, default=0.14)
    parser.add_argument("--external-cost", type=float, default=0.16)
    parser.add_argument("--forbidden-cost", type=float, default=0.06)
    parser.add_argument("--report-dir", type=Path, default=Path("empirical/reports"))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    costs = {
        "retained": args.retained_cost,
        "internal": args.internal_cost,
        "active": args.active_cost,
        "external": args.external_cost,
        "forbidden": args.forbidden_cost,
    }
    rng = np.random.default_rng(args.seed)
    calibration = [
        episode_metrics(
            "noise",
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            n_keys=args.n_keys,
            noise_scale=args.noise_scale,
            n_distractors=args.n_distractors,
            ridge_lambda=args.ridge_lambda,
        )
        for _ in range(args.calibration_trials_per_kind)
    ]
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            n_keys=args.n_keys,
            noise_scale=args.noise_scale,
            n_distractors=args.n_distractors,
            ridge_lambda=args.ridge_lambda,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    thresholds = calibrate_thresholds(calibration, costs, args.alpha)
    summary = summarize(calibration, metrics, thresholds, costs, args.alpha)

    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "trials_per_kind": args.trials_per_kind,
        "calibration_trials_per_kind": args.calibration_trials_per_kind,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "n_keys": args.n_keys,
        "n_distractors": args.n_distractors,
        "noise_scale": args.noise_scale,
        "ridge_lambda": args.ridge_lambda,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b8_precision_rival_antitautology_probe.md"
    json_path = out_dir / "b8_precision_rival_antitautology_probe.json"
    write_report(md_path, config, thresholds, costs, summary)
    json_path.write_text(
        json.dumps(
            {
                "config": config,
                "costs": costs,
                "thresholds": thresholds,
                "summary": summary,
                "metrics": [as_dict(m) for m in metrics],
                "calibration_metrics": [as_dict(m) for m in calibration],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(json.dumps({
        "finding": summary["finding"],
        "rival_gap": summary["rival_gap"],
        "agents": summary["agents"],
    }, indent=2))
    print(f"\nreport: {md_path}")
    print(f"json:   {json_path}")


if __name__ == "__main__":
    main()
