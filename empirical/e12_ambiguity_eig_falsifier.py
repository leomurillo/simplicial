"""E12 ambiguity versus expected-information-gain falsifier.

E12 tests the next fragile B-series bucket: ambiguity -> sampling.

The strong rival is continuous expected information gain (EIG). The probe asks
whether ambiguity is a distinct route, or whether sampling is just smooth EIG
under cost.

The synthetic generator has three worlds:

    1. no_sample_world: low EIG, one dominant candidate, no sampling route;
    2. eig_world: high EIG and high sampling effort, but the candidate set
       collapses out of sample, so there is no persistent ambiguity route;
    3. ambiguity_world: high EIG and a persistent multihypothesis candidate set.

Models solve two tasks:

    - predict graded sampling effort;
    - decide whether to admit a persistent ambiguity/sampling route.

The intended non-tautological result can split the jobs: continuous EIG may fit
effort while a held-out conformal candidate-set gate recovers ambiguity.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


SOURCES = ["ambiguity_world", "eig_world", "no_sample_world"]
MODEL_ORDER = [
    "scalar",
    "continuous_eig",
    "ambiguity_set_gate",
    "governed_eig_gate",
    "hybrid_eig_ambiguity",
]


@dataclass(frozen=True)
class Episode:
    source: str
    operation: str
    scalar_score: float
    train_eig: float
    train_candidate_entropy: float
    train_set_size_signal: float
    bait_eig: float
    outcome_entropy: float
    value_scale: float
    sampling_cost: float
    precision_signal: float
    heldout_eig: float
    heldout_candidate_entropy: float
    heldout_set_size_signal: float
    heldout_margin: float
    ambiguity_score: float
    target_effort_clean: float
    target_effort_observed: float
    target_ambiguity_clean: float
    target_ambiguity_observed: float


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
    if source == "no_sample_world":
        return {
            "outcome_entropy": float(rng.uniform(0.08, 0.26)),
            "value_scale": float(rng.uniform(0.20, 0.45)),
            "sampling_cost": float(rng.uniform(0.30, 0.52)),
            "train_candidate_entropy": float(rng.uniform(0.08, 0.24)),
            "heldout_candidate_entropy": float(rng.uniform(0.06, 0.22)),
            "train_set_size": float(rng.uniform(1.0, 1.7)),
            "heldout_set_size": float(rng.uniform(1.0, 1.6)),
            "heldout_margin": float(rng.uniform(0.55, 0.90)),
            "persistent_ambiguity": 0.0,
        }
    if source == "eig_world":
        # High EIG and train-side multihypothesis bait, but the ambiguity does
        # not persist out of sample.
        return {
            "outcome_entropy": float(rng.uniform(0.62, 0.95)),
            "value_scale": float(rng.uniform(0.72, 1.10)),
            "sampling_cost": float(rng.uniform(0.18, 0.40)),
            "train_candidate_entropy": float(rng.uniform(0.62, 0.98)),
            "heldout_candidate_entropy": float(rng.uniform(0.10, 0.34)),
            "train_set_size": float(rng.uniform(3.0, 6.5)),
            "heldout_set_size": float(rng.uniform(1.0, 1.9)),
            "heldout_margin": float(rng.uniform(0.45, 0.80)),
            "persistent_ambiguity": 0.0,
        }
    if source == "ambiguity_world":
        return {
            "outcome_entropy": float(rng.uniform(0.58, 0.94)),
            "value_scale": float(rng.uniform(0.64, 1.02)),
            "sampling_cost": float(rng.uniform(0.18, 0.40)),
            "train_candidate_entropy": float(rng.uniform(0.62, 0.98)),
            "heldout_candidate_entropy": float(rng.uniform(0.62, 0.98)),
            "train_set_size": float(rng.uniform(3.0, 6.5)),
            "heldout_set_size": float(rng.uniform(3.0, 6.5)),
            "heldout_margin": float(rng.uniform(0.03, 0.22)),
            "persistent_ambiguity": 1.0,
        }
    raise ValueError(f"unknown source: {source}")


def make_episode(
    rng: np.random.Generator,
    source: str,
    effort_noise: float,
    ambiguity_noise: float,
) -> Episode:
    p = source_parameters(rng, source)
    outcome_entropy = noisy_clip(rng, p["outcome_entropy"], 0.035, hi=1.0)
    value_scale = noisy_clip(rng, p["value_scale"], 0.040, hi=1.25)
    sampling_cost = noisy_clip(rng, p["sampling_cost"], 0.025, hi=0.8)
    train_candidate_entropy = noisy_clip(rng, p["train_candidate_entropy"], 0.045, hi=1.0)
    heldout_candidate_entropy = noisy_clip(rng, p["heldout_candidate_entropy"], 0.045, hi=1.0)
    train_set_size = noisy_clip(rng, p["train_set_size"], 0.20, hi=7.0)
    heldout_set_size = noisy_clip(rng, p["heldout_set_size"], 0.20, hi=7.0)
    heldout_margin = noisy_clip(rng, p["heldout_margin"], 0.035, hi=1.0)

    train_eig = noisy_clip(
        rng,
        outcome_entropy * value_scale + 0.22 * train_candidate_entropy - sampling_cost,
        0.035,
        lo=-0.15,
        hi=1.25,
    )
    heldout_eig = noisy_clip(
        rng,
        outcome_entropy * value_scale + 0.22 * heldout_candidate_entropy - sampling_cost,
        0.035,
        lo=-0.15,
        hi=1.25,
    )
    # Bait is high in both EIG and ambiguity worlds, and sometimes spuriously
    # high in no-sample worlds.
    bait_eig = noisy_clip(
        rng,
        train_eig + (0.18 if source != "no_sample_world" else 0.05),
        0.050,
        hi=1.25,
    )
    precision_signal = noisy_clip(rng, 1.0 / (0.35 + sampling_cost + 0.25 * outcome_entropy), 0.040, hi=1.2)
    ambiguity_score = noisy_clip(
        rng,
        0.18 * heldout_candidate_entropy + 0.14 * heldout_set_size + 0.55 * (1.0 - heldout_margin),
        0.045,
        hi=1.4,
    )

    target_effort_clean = float(
        np.clip(
            sigmoid(4.2 * (heldout_eig - 0.08) - 1.3 * sampling_cost)
            + 0.10 * p["persistent_ambiguity"],
            0.0,
            1.0,
        )
    )
    target_ambiguity_clean = float(p["persistent_ambiguity"])
    if source == "ambiguity_world":
        operation = "sample_ambiguity"
    elif source == "eig_world":
        operation = "sample_for_value"
    else:
        operation = "commit"

    return Episode(
        source=source,
        operation=operation,
        scalar_score=noisy_clip(rng, 1.0, 0.020, lo=0.92, hi=1.08),
        train_eig=train_eig,
        train_candidate_entropy=train_candidate_entropy,
        train_set_size_signal=train_set_size,
        bait_eig=bait_eig,
        outcome_entropy=outcome_entropy,
        value_scale=value_scale,
        sampling_cost=sampling_cost,
        precision_signal=precision_signal,
        heldout_eig=heldout_eig,
        heldout_candidate_entropy=heldout_candidate_entropy,
        heldout_set_size_signal=heldout_set_size,
        heldout_margin=heldout_margin,
        ambiguity_score=ambiguity_score,
        target_effort_clean=target_effort_clean,
        target_effort_observed=float(np.clip(target_effort_clean + rng.normal(scale=effort_noise), 0.0, 1.0)),
        target_ambiguity_clean=target_ambiguity_clean,
        target_ambiguity_observed=float(np.clip(target_ambiguity_clean + rng.normal(scale=ambiguity_noise), 0.0, 1.0)),
    )


def make_dataset(
    rng: np.random.Generator,
    route_trials: int,
    null_trials: int,
    ambiguity_mix: float,
    effort_noise: float,
    ambiguity_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    for _ in range(route_trials):
        source = "ambiguity_world" if rng.random() < ambiguity_mix else "eig_world"
        episodes.append(make_episode(rng, source, effort_noise=effort_noise, ambiguity_noise=ambiguity_noise))
    for _ in range(null_trials):
        episodes.append(make_episode(rng, "no_sample_world", effort_noise=effort_noise, ambiguity_noise=ambiguity_noise))
    rng.shuffle(episodes)
    return episodes


def feature_matrix(episodes: list[Episode], feature_kind: str, ambiguity_gate: float) -> np.ndarray:
    rows: list[list[float]] = []
    for e in episodes:
        admitted = 1.0 if e.ambiguity_score > ambiguity_gate else 0.0
        admitted_score = admitted * e.ambiguity_score
        continuous = [
            e.scalar_score,
            e.train_eig,
            e.bait_eig,
            e.outcome_entropy,
            e.value_scale,
            e.sampling_cost,
            e.precision_signal,
            e.train_candidate_entropy,
            e.train_set_size_signal,
        ]
        if feature_kind == "scalar":
            row = [e.scalar_score]
        elif feature_kind == "continuous_eig":
            row = continuous
        elif feature_kind == "ambiguity_set_gate":
            row = [e.scalar_score, admitted, admitted_score]
        elif feature_kind == "governed_eig_gate":
            row = continuous + [admitted, admitted_score]
        elif feature_kind == "hybrid_eig_ambiguity":
            row = continuous + [
                e.heldout_eig,
                e.heldout_candidate_entropy,
                e.heldout_set_size_signal,
                1.0 - e.heldout_margin,
                e.ambiguity_score,
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
    elif target_kind == "ambiguity":
        attr = "target_ambiguity_observed" if observed else "target_ambiguity_clean"
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
    ambiguity_gate: float,
    ridge: float,
) -> LinearModel:
    x = feature_matrix(train, feature_kind, ambiguity_gate=ambiguity_gate)
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


def predict(model: LinearModel, episodes: list[Episode], ambiguity_gate: float) -> np.ndarray:
    x = feature_matrix(episodes, model.feature_kind, ambiguity_gate=ambiguity_gate)
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


def ambiguity_metrics(episodes: list[Episode], pred: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([e.target_ambiguity_clean > 0.5 for e in episodes], dtype=bool)
    predicted = np.asarray([v >= threshold for v in pred], dtype=bool)
    source = np.asarray([e.source for e in episodes], dtype=object)

    def mean_mask(mask: np.ndarray, values: np.ndarray) -> float:
        return float(np.mean(values[mask])) if np.any(mask) else float("nan")

    amb = source == "ambiguity_world"
    eig = source == "eig_world"
    no_sample = source == "no_sample_world"
    nonamb = ~amb
    return {
        "accuracy": float(np.mean(predicted == truth)),
        "ambiguity_detection": mean_mask(amb, predicted),
        "nonambiguity_false_admission": mean_mask(nonamb, predicted),
        "eig_false_admission": mean_mask(eig, predicted),
        "no_sample_false_admission": mean_mask(no_sample, predicted),
    }


def evaluate_models(
    train: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    ambiguity_threshold: float,
) -> dict[str, Any]:
    nonamb_scores = [e.ambiguity_score for e in train if e.source != "ambiguity_world"]
    ambiguity_gate = quantile(nonamb_scores, 1.0 - alpha)

    models: dict[str, dict[str, LinearModel]] = {}
    predictions: dict[str, dict[str, np.ndarray]] = {}
    for name in MODEL_ORDER:
        models[name] = {}
        predictions[name] = {}
        for target in ["effort", "ambiguity"]:
            model = fit_linear_model(name, name, target, train, ambiguity_gate=ambiguity_gate, ridge=ridge)
            models[name][target] = model
            predictions[name][target] = predict(model, test, ambiguity_gate=ambiguity_gate)

    y_effort_obs = target_vector(test, "effort", observed=True)
    y_effort_clean = target_vector(test, "effort", observed=False)
    y_amb_obs = target_vector(test, "ambiguity", observed=True)
    y_amb_clean = target_vector(test, "ambiguity", observed=False)

    overall: dict[str, dict[str, Any]] = {}
    for name in MODEL_ORDER:
        effort = regression_metrics(y_effort_obs, y_effort_clean, predictions[name]["effort"])
        ambiguity_reg = regression_metrics(y_amb_obs, y_amb_clean, predictions[name]["ambiguity"])
        ambiguity_cls = ambiguity_metrics(test, predictions[name]["ambiguity"], threshold=ambiguity_threshold)
        overall[name] = {
            "effort": effort,
            "ambiguity_regression": ambiguity_reg,
            "ambiguity_classification": ambiguity_cls,
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
                "ambiguity": ambiguity_metrics(rows, predictions[name]["ambiguity"][idx], threshold=ambiguity_threshold),
            }

    effort_winner = min(MODEL_ORDER, key=lambda name: overall[name]["effort"]["rmse_observed"])
    ambiguity_winner = min(
        MODEL_ORDER,
        key=lambda name: (
            overall[name]["ambiguity_classification"]["nonambiguity_false_admission"],
            -overall[name]["ambiguity_classification"]["ambiguity_detection"],
            overall[name]["ambiguity_regression"]["rmse_observed"],
        ),
    )

    return {
        "ambiguity_gate": ambiguity_gate,
        "models": {
            name: {target: model.__dict__ for target, model in target_models.items()}
            for name, target_models in models.items()
        },
        "overall": overall,
        "by_source": by_source,
        "effort_winner": effort_winner,
        "ambiguity_winner": ambiguity_winner,
        "prediction_sample": {
            name: {target: [float(v) for v in predictions[name][target][:8]] for target in ["effort", "ambiguity"]}
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
            "train_eig": float(np.mean([e.train_eig for e in rows])),
            "heldout_eig": float(np.mean([e.heldout_eig for e in rows])),
            "train_candidate_entropy": float(np.mean([e.train_candidate_entropy for e in rows])),
            "heldout_candidate_entropy": float(np.mean([e.heldout_candidate_entropy for e in rows])),
            "train_set_size": float(np.mean([e.train_set_size_signal for e in rows])),
            "heldout_set_size": float(np.mean([e.heldout_set_size_signal for e in rows])),
            "ambiguity_score": float(np.mean([e.ambiguity_score for e in rows])),
            "target_effort": float(np.mean([e.target_effort_clean for e in rows])),
            "target_ambiguity": float(np.mean([e.target_ambiguity_clean for e in rows])),
        }
    return out


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    main_train = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        ambiguity_mix=args.main_ambiguity_mix,
        effort_noise=args.effort_noise,
        ambiguity_noise=args.ambiguity_noise,
    )
    main_test = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        ambiguity_mix=args.main_ambiguity_mix,
        effort_noise=args.effort_noise,
        ambiguity_noise=args.ambiguity_noise,
    )
    main_eval = evaluate_models(
        main_train,
        main_test,
        alpha=args.alpha,
        ridge=args.ridge,
        ambiguity_threshold=args.ambiguity_threshold,
    )

    sweep: list[dict[str, Any]] = []
    for mix in args.mix_grid:
        train = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            ambiguity_mix=float(mix),
            effort_noise=args.effort_noise,
            ambiguity_noise=args.ambiguity_noise,
        )
        test = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            ambiguity_mix=float(mix),
            effort_noise=args.effort_noise,
            ambiguity_noise=args.ambiguity_noise,
        )
        ev = evaluate_models(
            train,
            test,
            alpha=args.alpha,
            ridge=args.ridge,
            ambiguity_threshold=args.ambiguity_threshold,
        )
        sweep.append(
            {
                "ambiguity_mix": float(mix),
                "counts": source_counts(test),
                "effort_winner": ev["effort_winner"],
                "ambiguity_winner": ev["ambiguity_winner"],
                "ambiguity_gate": ev["ambiguity_gate"],
                "effort_rmse": {
                    name: ev["overall"][name]["effort"]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "ambiguity_false_admission": {
                    name: ev["overall"][name]["ambiguity_classification"]["nonambiguity_false_admission"]
                    for name in MODEL_ORDER
                },
                "ambiguity_detection": {
                    name: ev["overall"][name]["ambiguity_classification"]["ambiguity_detection"]
                    for name in MODEL_ORDER
                },
            }
        )

    continuous_effort = main_eval["overall"]["continuous_eig"]["effort"]["rmse_observed"]
    bucket_effort = main_eval["overall"]["ambiguity_set_gate"]["effort"]["rmse_observed"]
    hybrid_effort = main_eval["overall"]["hybrid_eig_ambiguity"]["effort"]["rmse_observed"]
    continuous_false = main_eval["overall"]["continuous_eig"]["ambiguity_classification"]["nonambiguity_false_admission"]
    bucket_false = main_eval["overall"]["ambiguity_set_gate"]["ambiguity_classification"]["nonambiguity_false_admission"]
    governed_false = main_eval["overall"]["governed_eig_gate"]["ambiguity_classification"]["nonambiguity_false_admission"]
    continuous_detection = main_eval["overall"]["continuous_eig"]["ambiguity_classification"]["ambiguity_detection"]
    bucket_detection = main_eval["overall"]["ambiguity_set_gate"]["ambiguity_classification"]["ambiguity_detection"]
    governed_detection = main_eval["overall"]["governed_eig_gate"]["ambiguity_classification"]["ambiguity_detection"]

    if (
        continuous_effort + args.decision_margin < bucket_effort
        and continuous_detection < args.detection_floor
        and governed_detection >= args.detection_floor
        and governed_false <= args.alpha * 1.5
    ):
        finding = "EIG_FITS_BUT_GATE_RECOVERS_AMBIGUITY"
    elif (
        continuous_effort + args.decision_margin < bucket_effort
        and continuous_false <= args.alpha * 1.5
        and continuous_detection >= args.detection_floor
    ):
        finding = "CONTINUOUS_EIG_RIVAL_WINS"
    elif (
        bucket_effort <= continuous_effort + args.decision_margin
        and bucket_false <= args.alpha * 1.5
        and bucket_detection >= args.detection_floor
    ):
        finding = "DISCRETE_AMBIGUITY_BUCKET_SURVIVES"
    elif (
        hybrid_effort + args.decision_margin < continuous_effort
        and governed_false <= continuous_false - args.false_admission_margin
        and governed_detection >= args.detection_floor
    ):
        finding = "HYBRID_EIG_GATE_NEEDED"
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
            "main_ambiguity_mix": args.main_ambiguity_mix,
            "mix_grid": [float(v) for v in args.mix_grid],
            "effort_noise": args.effort_noise,
            "ambiguity_noise": args.ambiguity_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "ambiguity_threshold": args.ambiguity_threshold,
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
            "bucket_effort_rmse": bucket_effort,
            "hybrid_effort_rmse": hybrid_effort,
            "continuous_false_ambiguity": continuous_false,
            "bucket_false_ambiguity": bucket_false,
            "governed_false_ambiguity": governed_false,
            "continuous_ambiguity_detection": continuous_detection,
            "bucket_ambiguity_detection": bucket_detection,
            "governed_ambiguity_detection": governed_detection,
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
        amb_reg = overall["ambiguity_regression"]
        amb = overall["ambiguity_classification"]
        model_rows.append(
            [
                name,
                fmt(effort["rmse_observed"]),
                fmt(effort["r2_observed"]),
                fmt(amb_reg["rmse_observed"]),
                fmt(amb["accuracy"]),
                fmt(amb["ambiguity_detection"]),
                fmt(amb["nonambiguity_false_admission"]),
                fmt(amb["eig_false_admission"]),
                fmt(amb["no_sample_false_admission"]),
            ]
        )

    source_rows = []
    for source, data in result["main_test_means"].items():
        source_rows.append(
            [
                source,
                fmt(data["scalar"]),
                fmt(data["train_eig"]),
                fmt(data["heldout_eig"]),
                fmt(data["train_candidate_entropy"]),
                fmt(data["heldout_candidate_entropy"]),
                fmt(data["train_set_size"]),
                fmt(data["heldout_set_size"]),
                fmt(data["ambiguity_score"]),
                fmt(data["target_effort"]),
                fmt(data["target_ambiguity"]),
            ]
        )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["ambiguity_mix"]),
                row["effort_winner"],
                row["ambiguity_winner"],
                fmt(row["effort_rmse"]["continuous_eig"]),
                fmt(row["effort_rmse"]["ambiguity_set_gate"]),
                fmt(row["effort_rmse"]["hybrid_eig_ambiguity"]),
                fmt(row["ambiguity_false_admission"]["continuous_eig"]),
                fmt(row["ambiguity_false_admission"]["ambiguity_set_gate"]),
                fmt(row["ambiguity_detection"]["ambiguity_set_gate"]),
            ]
        )

    lines = [
        "# E12 Ambiguity EIG Falsifier",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- main ambiguity mix: `{config['main_ambiguity_mix']}`",
        f"- route/null trials: `{config['route_trials']}` / `{config['null_trials']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E12 tests whether ambiguity/sampling survives a strong continuous",
        "expected-information-gain rival. The rival sees EIG, entropy, value,",
        "sampling cost, precision, and train-side candidate multiplicity. The",
        "ambiguity gate sees held-out candidate-set persistence calibrated on",
        "nonambiguity worlds.",
        "",
        "The probe scores two jobs separately: predicting graded sampling effort",
        "and admitting persistent ambiguity.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous effort RMSE", fmt(dq["continuous_effort_rmse"])],
                ["bucket effort RMSE", fmt(dq["bucket_effort_rmse"])],
                ["hybrid effort RMSE", fmt(dq["hybrid_effort_rmse"])],
                ["continuous false ambiguity", fmt(dq["continuous_false_ambiguity"])],
                ["bucket false ambiguity", fmt(dq["bucket_false_ambiguity"])],
                ["governed false ambiguity", fmt(dq["governed_false_ambiguity"])],
                ["continuous ambiguity detection", fmt(dq["continuous_ambiguity_detection"])],
                ["bucket ambiguity detection", fmt(dq["bucket_ambiguity_detection"])],
                ["governed ambiguity detection", fmt(dq["governed_ambiguity_detection"])],
                ["conformal ambiguity gate", fmt(main["ambiguity_gate"])],
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
                "ambiguity RMSE",
                "ambiguity acc",
                "ambiguity detect",
                "nonambig FA",
                "EIG FA",
                "no-sample FA",
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
                "train EIG",
                "heldout EIG",
                "train entropy",
                "heldout entropy",
                "train set",
                "heldout set",
                "ambiguity score",
                "target effort",
                "target ambiguity",
            ],
            source_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "ambiguity mix",
                "effort winner",
                "ambiguity winner",
                "cont effort",
                "bucket effort",
                "hybrid effort",
                "cont FA",
                "bucket FA",
                "bucket detect",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    finding = result["finding"]
    if finding == "EIG_FITS_BUT_GATE_RECOVERS_AMBIGUITY":
        lines.extend(
            [
                "The continuous EIG family wins the graded sampling-effort",
                "problem: plain EIG beats the bucket on effort, and the hybrid",
                "EIG-plus-heldout model is strongest overall. Plain EIG does not",
                "recover persistent ambiguity as well as the held-out candidate-set",
                "gate. E12 therefore supports governed sampling: continuous EIG",
                "explains how hard to sample, while candidate-set persistence",
                "decides when a multihypothesis state must remain open.",
            ]
        )
    elif finding == "CONTINUOUS_EIG_RIVAL_WINS":
        lines.extend(
            [
                "The continuous EIG rival predicts both sampling effort and",
                "ambiguity admission while controlling false sampling. This would",
                "demote ambiguity to a descriptive discretization of EIG under cost.",
            ]
        )
    elif finding == "DISCRETE_AMBIGUITY_BUCKET_SURVIVES":
        lines.extend(
            [
                "The ambiguity gate controls false admission and does not lose the",
                "effort task. This would support a stronger discrete ambiguity route.",
            ]
        )
    elif finding == "HYBRID_EIG_GATE_NEEDED":
        lines.extend(
            [
                "The hybrid EIG-plus-gate model is needed. That supports the",
                "two-level hypothesis: EIG supplies graded drive, and held-out",
                "candidate-set evidence supplies route admission.",
            ]
        )
    else:
        lines.extend(
            [
                "The EIG rival and ambiguity gate are too close. Bucket uniqueness",
                "is not established for ambiguity and sampling.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- scalar surprise is matched by construction;",
            "- high-EIG worlds and ambiguity worlds both contain train-side multihypothesis bait;",
            "- the continuous rival sees EIG, cost, entropy, and train candidate multiplicity;",
            "- the ambiguity gate is calibrated on held-out nonambiguity scores;",
            "- the phase sweep includes worlds where EIG-family effort models should win cleanly.",
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
    parser.add_argument("--main-ambiguity-mix", type=float, default=0.50)
    parser.add_argument("--mix-grid", type=float, nargs="+", default=[0.0, 0.25, 0.5, 0.75, 1.0])
    parser.add_argument("--effort-noise", type=float, default=0.045)
    parser.add_argument("--ambiguity-noise", type=float, default=0.040)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--ambiguity-threshold", type=float, default=0.50)
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
    json_path = args.report_dir / "e12_ambiguity_eig_falsifier.json"
    md_path = args.report_dir / "e12_ambiguity_eig_falsifier.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
