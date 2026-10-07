"""E14 governance versus risk/preference-control falsifier.

E14 tests whether governance/refusal is a primitive route or continuous
risk/preference suppression with a governance admission gate.

The strong rival is continuous risk control: competence gain, action value,
ordinary risk, preference conflict, policy cost, and train-side rule pressure.
The probe separates two jobs:

    - predict graded behavioral inhibition;
    - decide whether to admit governed refusal: represented competence blocked
      because the completion is disallowed.

Synthetic worlds:

    1. allowed_world: high competence, low risk, allowed action;
    2. risk_world: high competence, high ordinary risk, suppress but do not refuse;
    3. bait_world: local rule pressure looks forbidden but does not persist;
    4. forbidden_world: high competence and persistent governance violation;
    5. no_signal_world: weak competence, no reason to act or refuse.

The non-tautological result can split the jobs: continuous risk may fit
inhibition, while held-out governance persistence recovers refusal.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


SOURCES = ["forbidden_world", "risk_world", "bait_world", "allowed_world", "no_signal_world"]
MODEL_ORDER = [
    "scalar",
    "continuous_risk",
    "governance_gate",
    "governed_risk_gate",
    "hybrid_risk_governance",
]


@dataclass(frozen=True)
class Episode:
    source: str
    operation: str
    scalar_score: float
    competence_gain: float
    action_value: float
    ordinary_risk: float
    preference_conflict: float
    policy_cost: float
    train_rule_pressure: float
    heldout_rule_pressure: float
    train_sanction: float
    heldout_sanction: float
    represented_competence: float
    risk_suppression_score: float
    governance_persistence_score: float
    target_inhibition_clean: float
    target_inhibition_observed: float
    target_refusal_clean: float
    target_refusal_observed: float


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
    if source == "no_signal_world":
        return {
            "competence_gain": float(rng.uniform(0.02, 0.18)),
            "action_value": float(rng.uniform(0.02, 0.18)),
            "ordinary_risk": float(rng.uniform(0.05, 0.22)),
            "preference_conflict": float(rng.uniform(0.04, 0.20)),
            "policy_cost": float(rng.uniform(0.10, 0.26)),
            "train_rule_pressure": float(rng.uniform(0.02, 0.18)),
            "heldout_rule_pressure": float(rng.uniform(0.02, 0.18)),
            "train_sanction": float(rng.uniform(0.03, 0.18)),
            "heldout_sanction": float(rng.uniform(0.03, 0.18)),
            "refusal": 0.0,
        }
    if source == "allowed_world":
        return {
            "competence_gain": float(rng.uniform(0.68, 1.05)),
            "action_value": float(rng.uniform(0.70, 1.05)),
            "ordinary_risk": float(rng.uniform(0.05, 0.22)),
            "preference_conflict": float(rng.uniform(0.04, 0.20)),
            "policy_cost": float(rng.uniform(0.08, 0.22)),
            "train_rule_pressure": float(rng.uniform(0.03, 0.20)),
            "heldout_rule_pressure": float(rng.uniform(0.03, 0.20)),
            "train_sanction": float(rng.uniform(0.04, 0.20)),
            "heldout_sanction": float(rng.uniform(0.04, 0.20)),
            "refusal": 0.0,
        }
    if source == "risk_world":
        return {
            "competence_gain": float(rng.uniform(0.68, 1.05)),
            "action_value": float(rng.uniform(0.70, 1.05)),
            "ordinary_risk": float(rng.uniform(0.70, 1.05)),
            "preference_conflict": float(rng.uniform(0.58, 0.95)),
            "policy_cost": float(rng.uniform(0.16, 0.34)),
            "train_rule_pressure": float(rng.uniform(0.06, 0.24)),
            "heldout_rule_pressure": float(rng.uniform(0.05, 0.24)),
            "train_sanction": float(rng.uniform(0.08, 0.26)),
            "heldout_sanction": float(rng.uniform(0.08, 0.26)),
            "refusal": 0.0,
        }
    if source == "bait_world":
        # Local governance/rule pressure is high, but it does not persist. A
        # train-side risk/preference model should be tempted to over-refuse.
        return {
            "competence_gain": float(rng.uniform(0.68, 1.05)),
            "action_value": float(rng.uniform(0.68, 1.05)),
            "ordinary_risk": float(rng.uniform(0.20, 0.45)),
            "preference_conflict": float(rng.uniform(0.18, 0.42)),
            "policy_cost": float(rng.uniform(0.12, 0.28)),
            "train_rule_pressure": float(rng.uniform(0.70, 1.05)),
            "heldout_rule_pressure": float(rng.uniform(0.06, 0.24)),
            "train_sanction": float(rng.uniform(0.62, 1.00)),
            "heldout_sanction": float(rng.uniform(0.06, 0.24)),
            "refusal": 0.0,
        }
    if source == "forbidden_world":
        return {
            "competence_gain": float(rng.uniform(0.68, 1.05)),
            "action_value": float(rng.uniform(0.68, 1.05)),
            "ordinary_risk": float(rng.uniform(0.18, 0.45)),
            "preference_conflict": float(rng.uniform(0.18, 0.44)),
            "policy_cost": float(rng.uniform(0.12, 0.28)),
            "train_rule_pressure": float(rng.uniform(0.70, 1.05)),
            "heldout_rule_pressure": float(rng.uniform(0.70, 1.05)),
            "train_sanction": float(rng.uniform(0.62, 1.00)),
            "heldout_sanction": float(rng.uniform(0.62, 1.00)),
            "refusal": 1.0,
        }
    raise ValueError(f"unknown source: {source}")


def make_episode(
    rng: np.random.Generator,
    source: str,
    inhibition_noise: float,
    refusal_noise: float,
) -> Episode:
    p = source_parameters(rng, source)
    competence_gain = noisy_clip(rng, p["competence_gain"], 0.040, hi=1.2)
    action_value = noisy_clip(rng, p["action_value"], 0.040, hi=1.2)
    ordinary_risk = noisy_clip(rng, p["ordinary_risk"], 0.040, hi=1.2)
    preference_conflict = noisy_clip(rng, p["preference_conflict"], 0.040, hi=1.2)
    policy_cost = noisy_clip(rng, p["policy_cost"], 0.025, hi=0.8)
    train_rule_pressure = noisy_clip(rng, p["train_rule_pressure"], 0.045, hi=1.2)
    heldout_rule_pressure = noisy_clip(rng, p["heldout_rule_pressure"], 0.045, hi=1.2)
    train_sanction = noisy_clip(rng, p["train_sanction"], 0.045, hi=1.2)
    heldout_sanction = noisy_clip(rng, p["heldout_sanction"], 0.045, hi=1.2)

    represented_competence = noisy_clip(rng, competence_gain * action_value, 0.045, hi=1.2)
    risk_suppression_score = noisy_clip(
        rng,
        0.48 * ordinary_risk + 0.45 * preference_conflict + 0.28 * policy_cost + 0.22 * train_rule_pressure,
        0.045,
        hi=1.3,
    )
    governance_persistence_score = noisy_clip(
        rng,
        0.42 * heldout_rule_pressure + 0.42 * heldout_sanction + 0.20 * represented_competence,
        0.045,
        hi=1.4,
    )

    target_refusal_clean = float(p["refusal"])
    risk_inhibition = sigmoid(5.0 * (ordinary_risk + preference_conflict + 0.45 * policy_cost - action_value))
    governed_inhibition = 0.95 * target_refusal_clean
    target_inhibition_clean = float(np.clip(max(risk_inhibition, governed_inhibition), 0.0, 1.0))
    if source == "forbidden_world":
        operation = "refuse"
    elif source == "risk_world":
        operation = "risk_suppress"
    elif source == "bait_world":
        operation = "resist_false_refusal"
    elif source == "allowed_world":
        operation = "act"
    else:
        operation = "ignore"

    return Episode(
        source=source,
        operation=operation,
        scalar_score=noisy_clip(rng, 1.0, 0.020, lo=0.92, hi=1.08),
        competence_gain=competence_gain,
        action_value=action_value,
        ordinary_risk=ordinary_risk,
        preference_conflict=preference_conflict,
        policy_cost=policy_cost,
        train_rule_pressure=train_rule_pressure,
        heldout_rule_pressure=heldout_rule_pressure,
        train_sanction=train_sanction,
        heldout_sanction=heldout_sanction,
        represented_competence=represented_competence,
        risk_suppression_score=risk_suppression_score,
        governance_persistence_score=governance_persistence_score,
        target_inhibition_clean=target_inhibition_clean,
        target_inhibition_observed=float(np.clip(target_inhibition_clean + rng.normal(scale=inhibition_noise), 0.0, 1.0)),
        target_refusal_clean=target_refusal_clean,
        target_refusal_observed=float(np.clip(target_refusal_clean + rng.normal(scale=refusal_noise), 0.0, 1.0)),
    )


def make_dataset(
    rng: np.random.Generator,
    route_trials: int,
    null_trials: int,
    forbidden_mix: float,
    risk_share: float,
    bait_share: float,
    inhibition_noise: float,
    refusal_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    for _ in range(route_trials):
        u = rng.random()
        if u < forbidden_mix:
            source = "forbidden_world"
        else:
            v = rng.random()
            if v < risk_share:
                source = "risk_world"
            elif v < risk_share + bait_share:
                source = "bait_world"
            else:
                source = "allowed_world"
        episodes.append(make_episode(rng, source, inhibition_noise=inhibition_noise, refusal_noise=refusal_noise))
    for _ in range(null_trials):
        episodes.append(make_episode(rng, "no_signal_world", inhibition_noise=inhibition_noise, refusal_noise=refusal_noise))
    rng.shuffle(episodes)
    return episodes


def feature_matrix(episodes: list[Episode], feature_kind: str, governance_gate: float) -> np.ndarray:
    rows: list[list[float]] = []
    for e in episodes:
        admitted = 1.0 if e.governance_persistence_score > governance_gate else 0.0
        admitted_score = admitted * e.governance_persistence_score
        continuous = [
            e.scalar_score,
            e.competence_gain,
            e.action_value,
            e.ordinary_risk,
            e.preference_conflict,
            e.policy_cost,
            e.train_rule_pressure,
            e.train_sanction,
            e.represented_competence,
            e.risk_suppression_score,
        ]
        if feature_kind == "scalar":
            row = [e.scalar_score]
        elif feature_kind == "continuous_risk":
            row = continuous
        elif feature_kind == "governance_gate":
            row = [e.scalar_score, admitted, admitted_score]
        elif feature_kind == "governed_risk_gate":
            row = continuous + [admitted, admitted_score]
        elif feature_kind == "hybrid_risk_governance":
            row = continuous + [
                e.heldout_rule_pressure,
                e.heldout_sanction,
                e.governance_persistence_score,
                admitted,
                admitted_score,
            ]
        else:
            raise ValueError(f"unknown feature kind: {feature_kind}")
        rows.append(row)
    return np.asarray(rows, dtype=float)


def target_vector(episodes: list[Episode], target_kind: str, observed: bool) -> np.ndarray:
    if target_kind == "inhibition":
        attr = "target_inhibition_observed" if observed else "target_inhibition_clean"
    elif target_kind == "refusal":
        attr = "target_refusal_observed" if observed else "target_refusal_clean"
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
    governance_gate: float,
    ridge: float,
) -> LinearModel:
    x = feature_matrix(train, feature_kind, governance_gate=governance_gate)
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


def predict(model: LinearModel, episodes: list[Episode], governance_gate: float) -> np.ndarray:
    x = feature_matrix(episodes, model.feature_kind, governance_gate=governance_gate)
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


def refusal_metrics(episodes: list[Episode], pred: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([e.target_refusal_clean > 0.5 for e in episodes], dtype=bool)
    predicted = np.asarray([v >= threshold for v in pred], dtype=bool)
    source = np.asarray([e.source for e in episodes], dtype=object)

    def mean_mask(mask: np.ndarray, values: np.ndarray) -> float:
        return float(np.mean(values[mask])) if np.any(mask) else float("nan")

    forbidden = source == "forbidden_world"
    risk = source == "risk_world"
    bait = source == "bait_world"
    allowed = source == "allowed_world"
    no_signal = source == "no_signal_world"
    nonforbidden = ~forbidden
    return {
        "accuracy": float(np.mean(predicted == truth)),
        "refusal_detection": mean_mask(forbidden, predicted),
        "nonforbidden_false_refusal": mean_mask(nonforbidden, predicted),
        "risk_false_refusal": mean_mask(risk, predicted),
        "bait_false_refusal": mean_mask(bait, predicted),
        "allowed_false_refusal": mean_mask(allowed, predicted),
        "no_signal_false_refusal": mean_mask(no_signal, predicted),
    }


def evaluate_models(
    train: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    refusal_threshold: float,
) -> dict[str, Any]:
    nonforbidden_scores = [e.governance_persistence_score for e in train if e.source != "forbidden_world"]
    governance_gate = quantile(nonforbidden_scores, 1.0 - alpha)

    models: dict[str, dict[str, LinearModel]] = {}
    predictions: dict[str, dict[str, np.ndarray]] = {}
    for name in MODEL_ORDER:
        models[name] = {}
        predictions[name] = {}
        for target in ["inhibition", "refusal"]:
            model = fit_linear_model(name, name, target, train, governance_gate=governance_gate, ridge=ridge)
            models[name][target] = model
            predictions[name][target] = predict(model, test, governance_gate=governance_gate)

    y_inhib_obs = target_vector(test, "inhibition", observed=True)
    y_inhib_clean = target_vector(test, "inhibition", observed=False)
    y_ref_obs = target_vector(test, "refusal", observed=True)
    y_ref_clean = target_vector(test, "refusal", observed=False)

    overall: dict[str, dict[str, Any]] = {}
    for name in MODEL_ORDER:
        inhibition = regression_metrics(y_inhib_obs, y_inhib_clean, predictions[name]["inhibition"])
        refusal_reg = regression_metrics(y_ref_obs, y_ref_clean, predictions[name]["refusal"])
        refusal_cls = refusal_metrics(test, predictions[name]["refusal"], threshold=refusal_threshold)
        overall[name] = {
            "inhibition": inhibition,
            "refusal_regression": refusal_reg,
            "refusal_classification": refusal_cls,
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
                "inhibition": regression_metrics(
                    y_inhib_obs[idx],
                    y_inhib_clean[idx],
                    predictions[name]["inhibition"][idx],
                ),
                "refusal": refusal_metrics(rows, predictions[name]["refusal"][idx], threshold=refusal_threshold),
            }

    inhibition_winner = min(MODEL_ORDER, key=lambda name: overall[name]["inhibition"]["rmse_observed"])
    refusal_winner = min(
        MODEL_ORDER,
        key=lambda name: (
            overall[name]["refusal_classification"]["nonforbidden_false_refusal"],
            -overall[name]["refusal_classification"]["refusal_detection"],
            overall[name]["refusal_regression"]["rmse_observed"],
        ),
    )

    return {
        "governance_gate": governance_gate,
        "models": {
            name: {target: model.__dict__ for target, model in target_models.items()}
            for name, target_models in models.items()
        },
        "overall": overall,
        "by_source": by_source,
        "inhibition_winner": inhibition_winner,
        "refusal_winner": refusal_winner,
        "prediction_sample": {
            name: {target: [float(v) for v in predictions[name][target][:8]] for target in ["inhibition", "refusal"]}
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
            "competence_gain": float(np.mean([e.competence_gain for e in rows])),
            "action_value": float(np.mean([e.action_value for e in rows])),
            "ordinary_risk": float(np.mean([e.ordinary_risk for e in rows])),
            "preference_conflict": float(np.mean([e.preference_conflict for e in rows])),
            "train_rule_pressure": float(np.mean([e.train_rule_pressure for e in rows])),
            "heldout_rule_pressure": float(np.mean([e.heldout_rule_pressure for e in rows])),
            "governance_score": float(np.mean([e.governance_persistence_score for e in rows])),
            "target_inhibition": float(np.mean([e.target_inhibition_clean for e in rows])),
            "target_refusal": float(np.mean([e.target_refusal_clean for e in rows])),
        }
    return out


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    main_train = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        forbidden_mix=args.main_forbidden_mix,
        risk_share=args.risk_share,
        bait_share=args.bait_share,
        inhibition_noise=args.inhibition_noise,
        refusal_noise=args.refusal_noise,
    )
    main_test = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        forbidden_mix=args.main_forbidden_mix,
        risk_share=args.risk_share,
        bait_share=args.bait_share,
        inhibition_noise=args.inhibition_noise,
        refusal_noise=args.refusal_noise,
    )
    main_eval = evaluate_models(
        main_train,
        main_test,
        alpha=args.alpha,
        ridge=args.ridge,
        refusal_threshold=args.refusal_threshold,
    )

    sweep: list[dict[str, Any]] = []
    for mix in args.mix_grid:
        train = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            forbidden_mix=float(mix),
            risk_share=args.risk_share,
            bait_share=args.bait_share,
            inhibition_noise=args.inhibition_noise,
            refusal_noise=args.refusal_noise,
        )
        test = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            forbidden_mix=float(mix),
            risk_share=args.risk_share,
            bait_share=args.bait_share,
            inhibition_noise=args.inhibition_noise,
            refusal_noise=args.refusal_noise,
        )
        ev = evaluate_models(
            train,
            test,
            alpha=args.alpha,
            ridge=args.ridge,
            refusal_threshold=args.refusal_threshold,
        )
        sweep.append(
            {
                "forbidden_mix": float(mix),
                "counts": source_counts(test),
                "inhibition_winner": ev["inhibition_winner"],
                "refusal_winner": ev["refusal_winner"],
                "governance_gate": ev["governance_gate"],
                "inhibition_rmse": {
                    name: ev["overall"][name]["inhibition"]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "refusal_false_admission": {
                    name: ev["overall"][name]["refusal_classification"]["nonforbidden_false_refusal"]
                    for name in MODEL_ORDER
                },
                "refusal_detection": {
                    name: ev["overall"][name]["refusal_classification"]["refusal_detection"]
                    for name in MODEL_ORDER
                },
                "bait_false_refusal": {
                    name: ev["overall"][name]["refusal_classification"]["bait_false_refusal"]
                    for name in MODEL_ORDER
                },
                "risk_false_refusal": {
                    name: ev["overall"][name]["refusal_classification"]["risk_false_refusal"]
                    for name in MODEL_ORDER
                },
            }
        )

    continuous_inhibition = main_eval["overall"]["continuous_risk"]["inhibition"]["rmse_observed"]
    gate_inhibition = main_eval["overall"]["governance_gate"]["inhibition"]["rmse_observed"]
    hybrid_inhibition = main_eval["overall"]["hybrid_risk_governance"]["inhibition"]["rmse_observed"]
    continuous_false = main_eval["overall"]["continuous_risk"]["refusal_classification"]["nonforbidden_false_refusal"]
    gate_false = main_eval["overall"]["governance_gate"]["refusal_classification"]["nonforbidden_false_refusal"]
    governed_false = main_eval["overall"]["governed_risk_gate"]["refusal_classification"]["nonforbidden_false_refusal"]
    continuous_detection = main_eval["overall"]["continuous_risk"]["refusal_classification"]["refusal_detection"]
    gate_detection = main_eval["overall"]["governance_gate"]["refusal_classification"]["refusal_detection"]
    governed_detection = main_eval["overall"]["governed_risk_gate"]["refusal_classification"]["refusal_detection"]
    continuous_bait_false = main_eval["overall"]["continuous_risk"]["refusal_classification"]["bait_false_refusal"]
    gate_bait_false = main_eval["overall"]["governance_gate"]["refusal_classification"]["bait_false_refusal"]
    continuous_risk_false = main_eval["overall"]["continuous_risk"]["refusal_classification"]["risk_false_refusal"]
    gate_risk_false = main_eval["overall"]["governance_gate"]["refusal_classification"]["risk_false_refusal"]

    if (
        continuous_inhibition + args.decision_margin < gate_inhibition
        and (continuous_detection < args.detection_floor or continuous_false > gate_false + args.false_admission_margin)
        and governed_detection >= args.detection_floor
        and governed_false <= args.alpha * 1.5
    ):
        finding = "RISK_FITS_BUT_GATE_RECOVERS_REFUSAL"
    elif (
        continuous_inhibition + args.decision_margin < gate_inhibition
        and continuous_false <= args.alpha * 1.5
        and continuous_detection >= args.detection_floor
    ):
        finding = "CONTINUOUS_RISK_RIVAL_WINS"
    elif (
        gate_inhibition <= continuous_inhibition + args.decision_margin
        and gate_false <= args.alpha * 1.5
        and gate_detection >= args.detection_floor
    ):
        finding = "DISCRETE_GOVERNANCE_BUCKET_SURVIVES"
    elif (
        hybrid_inhibition + args.decision_margin < continuous_inhibition
        and governed_false <= continuous_false - args.false_admission_margin
        and governed_detection >= args.detection_floor
    ):
        finding = "HYBRID_RISK_GATE_NEEDED"
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
            "main_forbidden_mix": args.main_forbidden_mix,
            "risk_share": args.risk_share,
            "bait_share": args.bait_share,
            "mix_grid": [float(v) for v in args.mix_grid],
            "inhibition_noise": args.inhibition_noise,
            "refusal_noise": args.refusal_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "refusal_threshold": args.refusal_threshold,
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
            "continuous_inhibition_rmse": continuous_inhibition,
            "gate_inhibition_rmse": gate_inhibition,
            "hybrid_inhibition_rmse": hybrid_inhibition,
            "continuous_false_refusal": continuous_false,
            "gate_false_refusal": gate_false,
            "governed_false_refusal": governed_false,
            "continuous_refusal_detection": continuous_detection,
            "gate_refusal_detection": gate_detection,
            "governed_refusal_detection": governed_detection,
            "continuous_bait_false": continuous_bait_false,
            "gate_bait_false": gate_bait_false,
            "continuous_risk_false": continuous_risk_false,
            "gate_risk_false": gate_risk_false,
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
        inhibition = overall["inhibition"]
        refusal_reg = overall["refusal_regression"]
        refusal = overall["refusal_classification"]
        model_rows.append(
            [
                name,
                fmt(inhibition["rmse_observed"]),
                fmt(inhibition["r2_observed"]),
                fmt(refusal_reg["rmse_observed"]),
                fmt(refusal["accuracy"]),
                fmt(refusal["refusal_detection"]),
                fmt(refusal["nonforbidden_false_refusal"]),
                fmt(refusal["risk_false_refusal"]),
                fmt(refusal["bait_false_refusal"]),
                fmt(refusal["allowed_false_refusal"]),
            ]
        )

    source_rows = []
    for source, data in result["main_test_means"].items():
        source_rows.append(
            [
                source,
                fmt(data["scalar"]),
                fmt(data["competence_gain"]),
                fmt(data["action_value"]),
                fmt(data["ordinary_risk"]),
                fmt(data["preference_conflict"]),
                fmt(data["train_rule_pressure"]),
                fmt(data["heldout_rule_pressure"]),
                fmt(data["governance_score"]),
                fmt(data["target_inhibition"]),
                fmt(data["target_refusal"]),
            ]
        )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["forbidden_mix"]),
                row["inhibition_winner"],
                row["refusal_winner"],
                fmt(row["inhibition_rmse"]["continuous_risk"]),
                fmt(row["inhibition_rmse"]["governance_gate"]),
                fmt(row["inhibition_rmse"]["hybrid_risk_governance"]),
                fmt(row["refusal_false_admission"]["continuous_risk"]),
                fmt(row["refusal_false_admission"]["governance_gate"]),
                fmt(row["refusal_detection"]["governance_gate"]),
                fmt(row["bait_false_refusal"]["continuous_risk"]),
                fmt(row["risk_false_refusal"]["continuous_risk"]),
            ]
        )

    lines = [
        "# E14 Governance Risk Falsifier",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- main forbidden mix: `{config['main_forbidden_mix']}`",
        f"- risk/bait share: `{config['risk_share']}` / `{config['bait_share']}`",
        f"- route/null trials: `{config['route_trials']}` / `{config['null_trials']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E14 tests whether governance/refusal survives a strong continuous",
        "risk/preference rival. The rival sees competence, action value, ordinary",
        "risk, preference conflict, policy cost, and train-side rule pressure. The",
        "governance gate sees held-out rule/sanction persistence calibrated on",
        "non-forbidden worlds.",
        "",
        "The probe scores two jobs separately: predicting graded behavioral",
        "inhibition and admitting governed refusal.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous inhibition RMSE", fmt(dq["continuous_inhibition_rmse"])],
                ["gate inhibition RMSE", fmt(dq["gate_inhibition_rmse"])],
                ["hybrid inhibition RMSE", fmt(dq["hybrid_inhibition_rmse"])],
                ["continuous false refusal", fmt(dq["continuous_false_refusal"])],
                ["gate false refusal", fmt(dq["gate_false_refusal"])],
                ["governed false refusal", fmt(dq["governed_false_refusal"])],
                ["continuous refusal detection", fmt(dq["continuous_refusal_detection"])],
                ["gate refusal detection", fmt(dq["gate_refusal_detection"])],
                ["governed refusal detection", fmt(dq["governed_refusal_detection"])],
                ["continuous bait false", fmt(dq["continuous_bait_false"])],
                ["gate bait false", fmt(dq["gate_bait_false"])],
                ["continuous risk false", fmt(dq["continuous_risk_false"])],
                ["gate risk false", fmt(dq["gate_risk_false"])],
                ["conformal governance gate", fmt(main["governance_gate"])],
            ],
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "inhibition RMSE",
                "inhibition R2",
                "refusal RMSE",
                "refusal acc",
                "refusal detect",
                "nonforbid FA",
                "risk FA",
                "bait FA",
                "allowed FA",
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
                "competence",
                "action value",
                "risk",
                "pref conflict",
                "train rule",
                "heldout rule",
                "governance score",
                "target inhibit",
                "target refusal",
            ],
            source_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "forbidden mix",
                "inhibition winner",
                "refusal winner",
                "cont inhib",
                "gate inhib",
                "hybrid inhib",
                "cont FA",
                "gate FA",
                "gate detect",
                "cont bait FA",
                "cont risk FA",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    finding = result["finding"]
    if finding == "RISK_FITS_BUT_GATE_RECOVERS_REFUSAL":
        lines.extend(
            [
                "Continuous risk/preference variables win the graded inhibition",
                "problem, but train-side rule pressure confuses local bait and",
                "ordinary risk with governed refusal. The held-out governance gate",
                "recovers represented-but-blocked competence while controlling",
                "false refusal. E14 therefore supports governed risk control:",
                "risk explains inhibition, while rule persistence decides refusal.",
            ]
        )
    elif finding == "CONTINUOUS_RISK_RIVAL_WINS":
        lines.extend(
            [
                "The continuous risk/preference rival predicts both inhibition and",
                "refusal while controlling false refusal. This would demote",
                "governance to a descriptive risk/preference discretization.",
            ]
        )
    elif finding == "DISCRETE_GOVERNANCE_BUCKET_SURVIVES":
        lines.extend(
            [
                "The governance gate controls false refusal and does not lose the",
                "inhibition task. This would support a stronger primitive governance route.",
            ]
        )
    elif finding == "HYBRID_RISK_GATE_NEEDED":
        lines.extend(
            [
                "The hybrid risk-plus-gate model is needed. That supports the",
                "two-level hypothesis: continuous risk supplies inhibition, and",
                "held-out governance persistence supplies refusal admission.",
            ]
        )
    else:
        lines.extend(
            [
                "The risk rival and governance gate are too close. Governance bucket",
                "uniqueness is not established.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- scalar surprise is matched by construction;",
            "- risk worlds suppress action but are not governed refusals;",
            "- bait worlds have high train-side rule pressure but low held-out rule persistence;",
            "- forbidden worlds preserve competence and held-out rule violation;",
            "- the continuous rival sees risk/preference variables but not held-out governance persistence;",
            "- the governance gate is calibrated on held-out non-forbidden scores.",
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
    parser.add_argument("--main-forbidden-mix", type=float, default=0.40)
    parser.add_argument("--risk-share", type=float, default=0.35)
    parser.add_argument("--bait-share", type=float, default=0.35)
    parser.add_argument("--mix-grid", type=float, nargs="+", default=[0.0, 0.2, 0.4, 0.7, 1.0])
    parser.add_argument("--inhibition-noise", type=float, default=0.045)
    parser.add_argument("--refusal-noise", type=float, default=0.040)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--refusal-threshold", type=float, default=0.50)
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
    json_path = args.report_dir / "e14_governance_risk_falsifier.json"
    md_path = args.report_dir / "e14_governance_risk_falsifier.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
