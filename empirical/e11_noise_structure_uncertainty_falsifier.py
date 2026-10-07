"""E11 noise-structure uncertainty falsifier.

This is the adversarial empirical companion to the B11 target.

B10 corrected the current bucket: continuous flow fit directional magnitude,
while a gate controlled false admission. E11 applies the same discipline to the
noise-versus-structure bucket family.

The probe gives a strong ACh/NE-style continuous uncertainty rival a fair shot.
Episodes can come from three worlds:

    1. noise_world: stochastic residuals with no stable structure;
    2. uncertainty_world: unexpected uncertainty/volatility without stable
       structure;
    3. structure_world: a stable hidden feature explains the residual.

The compared models must solve two tasks:

    - predict a graded precision/arousal response;
    - decide whether to admit a structural closure.

The intended falsifier is not "bucket wins everything." A good result can say
that continuous uncertainty wins graded response prediction, while a conformal
held-out gate is needed to prevent false structural closure.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


SOURCES = ["structure_world", "uncertainty_world", "noise_world"]
MODEL_ORDER = [
    "scalar",
    "continuous_uncertainty",
    "bucket_structure_gate",
    "governed_uncertainty_gate",
    "hybrid_uncertainty_structure",
]


@dataclass(frozen=True)
class Episode:
    source: str
    operation: str
    scalar_score: float
    expected_uncertainty: float
    unexpected_uncertainty: float
    volatility_signal: float
    precision_signal: float
    train_best_gain: float
    heldout_best_gain: float
    train_bait_gain: float
    bait_heldout_gain: float
    gain_gap: float
    structure_strength: float
    target_precision_clean: float
    target_precision_observed: float
    target_structure_clean: float
    target_structure_observed: float


@dataclass(frozen=True)
class LinearModel:
    name: str
    feature_kind: str
    target_kind: str
    coef: list[float]
    mean: list[float]
    sd: list[float]


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = float(np.std(x))
    if sd < 1e-12:
        return np.zeros_like(x)
    return (x - float(np.mean(x))) / sd


def fit_coef(feature: np.ndarray, residual: np.ndarray, ridge: float = 1e-6) -> np.ndarray:
    feature = np.asarray(feature, dtype=float)
    if feature.ndim == 1:
        feature = feature[:, None]
    gram = feature.T @ feature
    rhs = feature.T @ residual
    reg = ridge * np.eye(gram.shape[0])
    try:
        return np.linalg.solve(gram + reg, rhs)
    except np.linalg.LinAlgError:
        return np.linalg.pinv(gram + reg) @ rhs


def train_gain(feature: np.ndarray, residual: np.ndarray) -> float:
    feature = np.asarray(feature, dtype=float)
    if feature.ndim == 1:
        feature = feature[:, None]
    coef = fit_coef(feature, residual)
    base = float(np.mean(residual**2))
    improved = float(np.mean((residual - feature @ coef) ** 2))
    return base - improved


def heldout_gain(
    train_feature: np.ndarray,
    train_residual: np.ndarray,
    test_feature: np.ndarray,
    test_residual: np.ndarray,
) -> float:
    train_feature = np.asarray(train_feature, dtype=float)
    test_feature = np.asarray(test_feature, dtype=float)
    if train_feature.ndim == 1:
        train_feature = train_feature[:, None]
    if test_feature.ndim == 1:
        test_feature = test_feature[:, None]
    coef = fit_coef(train_feature, train_residual)
    base = float(np.mean(test_residual**2))
    improved = float(np.mean((test_residual - test_feature @ coef) ** 2))
    return base - improved


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def noisy_clip(rng: np.random.Generator, value: float, noise: float, lo: float = 0.0, hi: float = 1.2) -> float:
    return float(np.clip(value + rng.normal(scale=noise), lo, hi))


def make_features(rng: np.random.Generator, n: int) -> dict[str, np.ndarray]:
    z = rng.normal(size=(n, 8))
    return {
        "linear": standardize(z[:, 0] + 0.2 * z[:, 1]),
        "packet": standardize(z[:, 1] * z[:, 2]),
        "chart": standardize(np.sin(z[:, 3]) + 0.25 * z[:, 4] ** 2),
        "z": z,
    }


def make_candidate_bank(
    rng: np.random.Generator,
    source: str,
    train_base: dict[str, np.ndarray],
    test_base: dict[str, np.ndarray],
    train_y: np.ndarray,
    test_y: np.ndarray,
    n_distractors: int,
) -> list[tuple[str, np.ndarray, np.ndarray]]:
    train_z = train_base["z"]
    test_z = test_base["z"]
    candidates: list[tuple[str, np.ndarray, np.ndarray]] = []

    if source == "structure_world":
        # The stable structural feature is available, but it must be discovered
        # by held-out gain rather than by a semantic label.
        candidates.append(("stable_structure", train_base["packet"], test_base["packet"]))
    else:
        candidates.append(("stable_decoy", train_base["packet"], test_base["packet"]))

    for _ in range(n_distractors):
        i, j = rng.choice(train_z.shape[1], size=2, replace=False)
        train_feature = standardize(train_z[:, i] * train_z[:, j] + 0.2 * rng.normal(size=len(train_y)))
        test_feature = standardize(test_z[:, i] * test_z[:, j] + 0.2 * rng.normal(size=len(test_y)))
        candidates.append(("distractor", train_feature, test_feature))

    # A train-only bait makes train precision look deceptively promising in all
    # worlds. This is the anti-tautology pressure on the continuous rival.
    bait_train = standardize(train_y + 0.035 * rng.normal(size=len(train_y)))
    bait_test = standardize(rng.normal(size=len(test_y)))
    candidates.append(("train_bait", bait_train, bait_test))

    order = rng.permutation(len(candidates))
    return [candidates[int(i)] for i in order]


def source_parameters(rng: np.random.Generator, source: str) -> tuple[float, float, float]:
    if source == "noise_world":
        expected = float(rng.uniform(0.55, 0.95))
        unexpected = float(rng.uniform(0.04, 0.20))
        strength = 0.0
    elif source == "uncertainty_world":
        expected = float(rng.uniform(0.30, 0.70))
        unexpected = float(rng.uniform(0.55, 1.00))
        strength = 0.0
    elif source == "structure_world":
        # Structural violations look like unexpected uncertainty to the rival.
        expected = float(rng.uniform(0.30, 0.70))
        unexpected = float(rng.uniform(0.48, 0.95))
        strength = float(rng.uniform(0.65, 1.15))
    else:
        raise ValueError(f"unknown source: {source}")
    return expected, unexpected, strength


def make_episode(
    rng: np.random.Generator,
    source: str,
    n_train: int,
    n_test: int,
    n_distractors: int,
    precision_noise: float,
    structure_noise: float,
) -> Episode:
    expected, unexpected, strength = source_parameters(rng, source)
    train_base = make_features(rng, n_train)
    test_base = make_features(rng, n_test)

    train_noise_scale = 0.85 + expected
    test_noise_scale = train_noise_scale * (1.0 + 0.35 * unexpected)
    train_noise = train_noise_scale * rng.normal(size=n_train)
    test_noise = test_noise_scale * rng.normal(size=n_test)

    if source == "structure_world":
        train_y = strength * train_base["packet"] + train_noise
        test_y = strength * test_base["packet"] + test_noise
        operation = "close"
    elif source == "uncertainty_world":
        train_y = train_noise
        # A nonstationary but unstructured residual. It should raise precision
        # response without opening a stable structural packet.
        test_y = test_noise + 0.35 * unexpected * rng.normal(size=n_test)
        operation = "adjust_precision"
    elif source == "noise_world":
        train_y = train_noise
        test_y = test_noise
        operation = "suppress"
    else:
        raise ValueError(f"unknown source: {source}")

    train_y = standardize(train_y)
    test_y = standardize(test_y)

    candidates = make_candidate_bank(
        rng,
        source=source,
        train_base=train_base,
        test_base=test_base,
        train_y=train_y,
        test_y=test_y,
        n_distractors=n_distractors,
    )
    train_gains = [(name, train_gain(tr, train_y), heldout_gain(tr, train_y, te, test_y)) for name, tr, te in candidates]
    best_train = max(train_gains, key=lambda row: row[1])
    best_heldout = max(train_gains, key=lambda row: row[2])
    bait_rows = [row for row in train_gains if row[0] == "train_bait"]
    bait = bait_rows[0] if bait_rows else ("train_bait", 0.0, 0.0)

    expected_signal = noisy_clip(rng, expected, 0.060)
    unexpected_signal = noisy_clip(rng, unexpected + 0.08 * strength, 0.075)
    volatility_signal = noisy_clip(rng, 0.45 * expected + 0.85 * unexpected + 0.10 * strength, 0.070)
    precision_signal = noisy_clip(rng, 1.0 / (0.35 + expected + 0.65 * unexpected), 0.045)

    target_precision_clean = float(
        np.clip(
            np.tanh((0.45 * expected + 1.15 * unexpected + 0.30 * strength) / 1.20),
            0.0,
            1.0,
        )
    )
    target_structure_clean = 1.0 if source == "structure_world" else 0.0

    return Episode(
        source=source,
        operation=operation,
        scalar_score=float(np.mean(test_y**2)),
        expected_uncertainty=expected_signal,
        unexpected_uncertainty=unexpected_signal,
        volatility_signal=volatility_signal,
        precision_signal=precision_signal,
        train_best_gain=float(best_train[1]),
        heldout_best_gain=float(best_heldout[2]),
        train_bait_gain=float(bait[1]),
        bait_heldout_gain=float(bait[2]),
        gain_gap=float(best_train[1] - best_heldout[2]),
        structure_strength=strength,
        target_precision_clean=target_precision_clean,
        target_precision_observed=float(np.clip(target_precision_clean + rng.normal(scale=precision_noise), 0.0, 1.0)),
        target_structure_clean=target_structure_clean,
        target_structure_observed=float(np.clip(target_structure_clean + rng.normal(scale=structure_noise), 0.0, 1.0)),
    )


def make_dataset(
    rng: np.random.Generator,
    route_trials: int,
    null_trials: int,
    structure_mix: float,
    n_train: int,
    n_test: int,
    n_distractors: int,
    precision_noise: float,
    structure_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    for _ in range(route_trials):
        source = "structure_world" if rng.random() < structure_mix else "uncertainty_world"
        episodes.append(
            make_episode(
                rng,
                source=source,
                n_train=n_train,
                n_test=n_test,
                n_distractors=n_distractors,
                precision_noise=precision_noise,
                structure_noise=structure_noise,
            )
        )
    for _ in range(null_trials):
        episodes.append(
            make_episode(
                rng,
                source="noise_world",
                n_train=n_train,
                n_test=n_test,
                n_distractors=n_distractors,
                precision_noise=precision_noise,
                structure_noise=structure_noise,
            )
        )
    rng.shuffle(episodes)
    return episodes


def feature_matrix(episodes: list[Episode], feature_kind: str, structure_gate: float) -> np.ndarray:
    rows: list[list[float]] = []
    for e in episodes:
        admitted = 1.0 if e.heldout_best_gain > structure_gate else 0.0
        admitted_gain = admitted * e.heldout_best_gain
        continuous = [
            e.scalar_score,
            e.expected_uncertainty,
            e.unexpected_uncertainty,
            e.volatility_signal,
            e.precision_signal,
            e.train_best_gain,
            e.train_bait_gain,
            e.gain_gap,
        ]
        if feature_kind == "scalar":
            row = [e.scalar_score]
        elif feature_kind == "continuous_uncertainty":
            row = continuous
        elif feature_kind == "bucket_structure_gate":
            row = [e.scalar_score, admitted, admitted_gain]
        elif feature_kind == "governed_uncertainty_gate":
            row = continuous + [admitted, admitted_gain]
        elif feature_kind == "hybrid_uncertainty_structure":
            row = continuous + [
                e.heldout_best_gain,
                admitted,
                admitted_gain,
                e.heldout_best_gain / max(e.train_best_gain, 1e-9),
            ]
        else:
            raise ValueError(f"unknown feature kind: {feature_kind}")
        rows.append(row)
    return np.asarray(rows, dtype=float)


def target_vector(episodes: list[Episode], target_kind: str, observed: bool) -> np.ndarray:
    if target_kind == "precision":
        attr = "target_precision_observed" if observed else "target_precision_clean"
    elif target_kind == "structure":
        attr = "target_structure_observed" if observed else "target_structure_clean"
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
    structure_gate: float,
    ridge: float,
) -> LinearModel:
    x = feature_matrix(train, feature_kind, structure_gate=structure_gate)
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


def predict(model: LinearModel, episodes: list[Episode], structure_gate: float) -> np.ndarray:
    x = feature_matrix(episodes, model.feature_kind, structure_gate=structure_gate)
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
    return {
        "rmse_observed": rmse_obs,
        "rmse_clean": rmse_clean,
        "r2_observed": r2,
    }


def structure_metrics(episodes: list[Episode], pred: np.ndarray, threshold: float) -> dict[str, float]:
    truth = np.asarray([e.target_structure_clean > 0.5 for e in episodes], dtype=bool)
    predicted = np.asarray([v >= threshold for v in pred], dtype=bool)
    source = np.asarray([e.source for e in episodes], dtype=object)

    def mean_mask(mask: np.ndarray, value: np.ndarray) -> float:
        return float(np.mean(value[mask])) if np.any(mask) else float("nan")

    structure = source == "structure_world"
    uncertainty = source == "uncertainty_world"
    noise = source == "noise_world"
    nonstructure = ~structure
    return {
        "accuracy": float(np.mean(predicted == truth)),
        "structure_detection": mean_mask(structure, predicted),
        "nonstructure_false_admission": mean_mask(nonstructure, predicted),
        "uncertainty_false_admission": mean_mask(uncertainty, predicted),
        "noise_false_admission": mean_mask(noise, predicted),
    }


def evaluate_models(
    train: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    structure_threshold: float,
) -> dict[str, Any]:
    nonstructure_gains = [e.heldout_best_gain for e in train if e.source != "structure_world"]
    structure_gate = quantile(nonstructure_gains, 1.0 - alpha)

    models: dict[str, dict[str, LinearModel]] = {}
    predictions: dict[str, dict[str, np.ndarray]] = {}
    for name in MODEL_ORDER:
        models[name] = {}
        predictions[name] = {}
        for target in ["precision", "structure"]:
            model = fit_linear_model(name, name, target, train, structure_gate=structure_gate, ridge=ridge)
            models[name][target] = model
            predictions[name][target] = predict(model, test, structure_gate=structure_gate)

    y_precision_obs = target_vector(test, "precision", observed=True)
    y_precision_clean = target_vector(test, "precision", observed=False)
    y_structure_obs = target_vector(test, "structure", observed=True)
    y_structure_clean = target_vector(test, "structure", observed=False)

    overall: dict[str, dict[str, Any]] = {}
    for name in MODEL_ORDER:
        precision = regression_metrics(y_precision_obs, y_precision_clean, predictions[name]["precision"])
        structure_reg = regression_metrics(y_structure_obs, y_structure_clean, predictions[name]["structure"])
        structure_cls = structure_metrics(test, predictions[name]["structure"], threshold=structure_threshold)
        overall[name] = {
            "precision": precision,
            "structure_regression": structure_reg,
            "structure_classification": structure_cls,
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
                "precision": regression_metrics(
                    y_precision_obs[idx],
                    y_precision_clean[idx],
                    predictions[name]["precision"][idx],
                ),
                "structure": structure_metrics(rows, predictions[name]["structure"][idx], threshold=structure_threshold),
            }

    precision_winner = min(MODEL_ORDER, key=lambda name: overall[name]["precision"]["rmse_observed"])
    structure_winner = min(
        MODEL_ORDER,
        key=lambda name: (
            overall[name]["structure_classification"]["nonstructure_false_admission"],
            -overall[name]["structure_classification"]["structure_detection"],
            overall[name]["structure_regression"]["rmse_observed"],
        ),
    )

    return {
        "structure_gate": structure_gate,
        "models": {
            name: {target: model.__dict__ for target, model in target_models.items()}
            for name, target_models in models.items()
        },
        "overall": overall,
        "by_source": by_source,
        "precision_winner": precision_winner,
        "structure_winner": structure_winner,
        "prediction_sample": {
            name: {
                target: [float(v) for v in predictions[name][target][:8]]
                for target in ["precision", "structure"]
            }
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
            "expected_uncertainty": float(np.mean([e.expected_uncertainty for e in rows])),
            "unexpected_uncertainty": float(np.mean([e.unexpected_uncertainty for e in rows])),
            "volatility_signal": float(np.mean([e.volatility_signal for e in rows])),
            "train_best_gain": float(np.mean([e.train_best_gain for e in rows])),
            "heldout_best_gain": float(np.mean([e.heldout_best_gain for e in rows])),
            "target_precision": float(np.mean([e.target_precision_clean for e in rows])),
            "target_structure": float(np.mean([e.target_structure_clean for e in rows])),
        }
    return out


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    main_train = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        structure_mix=args.main_structure_mix,
        n_train=args.n_train,
        n_test=args.n_test,
        n_distractors=args.n_distractors,
        precision_noise=args.precision_noise,
        structure_noise=args.structure_noise,
    )
    main_test = make_dataset(
        rng,
        route_trials=args.route_trials,
        null_trials=args.null_trials,
        structure_mix=args.main_structure_mix,
        n_train=args.n_train,
        n_test=args.n_test,
        n_distractors=args.n_distractors,
        precision_noise=args.precision_noise,
        structure_noise=args.structure_noise,
    )
    main_eval = evaluate_models(
        main_train,
        main_test,
        alpha=args.alpha,
        ridge=args.ridge,
        structure_threshold=args.structure_threshold,
    )

    sweep: list[dict[str, Any]] = []
    for mix in args.mix_grid:
        train = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            structure_mix=float(mix),
            n_train=args.n_train,
            n_test=args.n_test,
            n_distractors=args.n_distractors,
            precision_noise=args.precision_noise,
            structure_noise=args.structure_noise,
        )
        test = make_dataset(
            rng,
            route_trials=args.sweep_route_trials,
            null_trials=args.sweep_null_trials,
            structure_mix=float(mix),
            n_train=args.n_train,
            n_test=args.n_test,
            n_distractors=args.n_distractors,
            precision_noise=args.precision_noise,
            structure_noise=args.structure_noise,
        )
        ev = evaluate_models(
            train,
            test,
            alpha=args.alpha,
            ridge=args.ridge,
            structure_threshold=args.structure_threshold,
        )
        sweep.append(
            {
                "structure_mix": float(mix),
                "counts": source_counts(test),
                "precision_winner": ev["precision_winner"],
                "structure_winner": ev["structure_winner"],
                "structure_gate": ev["structure_gate"],
                "precision_rmse": {
                    name: ev["overall"][name]["precision"]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "structure_false_admission": {
                    name: ev["overall"][name]["structure_classification"]["nonstructure_false_admission"]
                    for name in MODEL_ORDER
                },
                "structure_detection": {
                    name: ev["overall"][name]["structure_classification"]["structure_detection"]
                    for name in MODEL_ORDER
                },
            }
        )

    continuous_precision = main_eval["overall"]["continuous_uncertainty"]["precision"]["rmse_observed"]
    bucket_precision = main_eval["overall"]["bucket_structure_gate"]["precision"]["rmse_observed"]
    hybrid_precision = main_eval["overall"]["hybrid_uncertainty_structure"]["precision"]["rmse_observed"]
    continuous_false = main_eval["overall"]["continuous_uncertainty"]["structure_classification"]["nonstructure_false_admission"]
    bucket_false = main_eval["overall"]["bucket_structure_gate"]["structure_classification"]["nonstructure_false_admission"]
    governed_false = main_eval["overall"]["governed_uncertainty_gate"]["structure_classification"]["nonstructure_false_admission"]
    continuous_detection = main_eval["overall"]["continuous_uncertainty"]["structure_classification"]["structure_detection"]
    bucket_detection = main_eval["overall"]["bucket_structure_gate"]["structure_classification"]["structure_detection"]
    governed_detection = main_eval["overall"]["governed_uncertainty_gate"]["structure_classification"]["structure_detection"]

    if (
        continuous_precision + args.decision_margin < bucket_precision
        and continuous_false > max(args.alpha * 2.0, bucket_false + args.false_admission_margin)
        and bucket_false <= args.alpha * 1.5
        and bucket_detection >= args.detection_floor
    ):
        finding = "UNCERTAINTY_FITS_BUT_GATE_GOVERNS_STRUCTURE"
    elif (
        continuous_precision + args.decision_margin < bucket_precision
        and continuous_detection < args.detection_floor
        and governed_detection >= args.detection_floor
        and governed_false <= args.alpha * 1.5
    ):
        finding = "UNCERTAINTY_FITS_BUT_GATE_RECOVERS_STRUCTURE"
    elif (
        continuous_precision + args.decision_margin < bucket_precision
        and continuous_false <= args.alpha * 1.5
        and continuous_detection >= args.detection_floor
    ):
        finding = "CONTINUOUS_UNCERTAINTY_RIVAL_WINS"
    elif (
        bucket_precision <= continuous_precision + args.decision_margin
        and bucket_false <= args.alpha * 1.5
        and bucket_detection >= args.detection_floor
    ):
        finding = "DISCRETE_NOISE_STRUCTURE_BUCKET_SURVIVES"
    elif (
        hybrid_precision + args.decision_margin < continuous_precision
        and governed_false <= continuous_false - args.false_admission_margin
        and governed_detection >= args.detection_floor
    ):
        finding = "HYBRID_UNCERTAINTY_GATE_NEEDED"
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
            "main_structure_mix": args.main_structure_mix,
            "mix_grid": [float(v) for v in args.mix_grid],
            "n_train": args.n_train,
            "n_test": args.n_test,
            "n_distractors": args.n_distractors,
            "precision_noise": args.precision_noise,
            "structure_noise": args.structure_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "structure_threshold": args.structure_threshold,
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
            "continuous_precision_rmse": continuous_precision,
            "bucket_precision_rmse": bucket_precision,
            "hybrid_precision_rmse": hybrid_precision,
            "continuous_false_structure": continuous_false,
            "bucket_false_structure": bucket_false,
            "governed_false_structure": governed_false,
            "continuous_structure_detection": continuous_detection,
            "bucket_structure_detection": bucket_detection,
            "governed_structure_detection": governed_detection,
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
        precision = overall["precision"]
        structure = overall["structure_classification"]
        structure_reg = overall["structure_regression"]
        model_rows.append(
            [
                name,
                fmt(precision["rmse_observed"]),
                fmt(precision["r2_observed"]),
                fmt(structure_reg["rmse_observed"]),
                fmt(structure["accuracy"]),
                fmt(structure["structure_detection"]),
                fmt(structure["nonstructure_false_admission"]),
                fmt(structure["uncertainty_false_admission"]),
                fmt(structure["noise_false_admission"]),
            ]
        )

    source_rows = []
    for source, data in result["main_test_means"].items():
        source_rows.append(
            [
                source,
                fmt(data["scalar"]),
                fmt(data["expected_uncertainty"]),
                fmt(data["unexpected_uncertainty"]),
                fmt(data["volatility_signal"]),
                fmt(data["train_best_gain"]),
                fmt(data["heldout_best_gain"]),
                fmt(data["target_precision"]),
                fmt(data["target_structure"]),
            ]
        )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["structure_mix"]),
                row["precision_winner"],
                row["structure_winner"],
                fmt(row["precision_rmse"]["continuous_uncertainty"]),
                fmt(row["precision_rmse"]["bucket_structure_gate"]),
                fmt(row["precision_rmse"]["hybrid_uncertainty_structure"]),
                fmt(row["structure_false_admission"]["continuous_uncertainty"]),
                fmt(row["structure_false_admission"]["bucket_structure_gate"]),
                fmt(row["structure_detection"]["bucket_structure_gate"]),
            ]
        )

    lines = [
        "# E11 Noise-Structure Uncertainty Falsifier",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- main structure mix: `{config['main_structure_mix']}`",
        f"- route/null trials: `{config['route_trials']}` / `{config['null_trials']}`",
        f"- alpha: `{config['alpha']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E11 tests whether the noise-versus-structure bucket survives a strong",
        "continuous uncertainty rival. The rival receives expected uncertainty,",
        "unexpected uncertainty, volatility, precision, and train-side gain. The",
        "bucket gate receives held-out structural gain calibrated on nonstructure",
        "worlds.",
        "",
        "The probe scores two jobs separately: predicting graded precision response",
        "and controlling false structural admission.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous precision RMSE", fmt(dq["continuous_precision_rmse"])],
                ["bucket precision RMSE", fmt(dq["bucket_precision_rmse"])],
                ["hybrid precision RMSE", fmt(dq["hybrid_precision_rmse"])],
                ["continuous false structure", fmt(dq["continuous_false_structure"])],
                ["bucket false structure", fmt(dq["bucket_false_structure"])],
                ["governed false structure", fmt(dq["governed_false_structure"])],
                ["continuous structure detection", fmt(dq["continuous_structure_detection"])],
                ["bucket structure detection", fmt(dq["bucket_structure_detection"])],
                ["governed structure detection", fmt(dq["governed_structure_detection"])],
                ["conformal structure gate", fmt(main["structure_gate"])],
            ],
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "precision RMSE",
                "precision R2",
                "structure RMSE",
                "structure acc",
                "structure detect",
                "nonstructure FA",
                "uncertainty FA",
                "noise FA",
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
                "expected U",
                "unexpected U",
                "volatility",
                "train gain",
                "heldout gain",
                "target precision",
                "target structure",
            ],
            source_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "structure mix",
                "precision winner",
                "structure winner",
                "cont precision",
                "bucket precision",
                "hybrid precision",
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
    if finding == "UNCERTAINTY_FITS_BUT_GATE_GOVERNS_STRUCTURE":
        lines.extend(
            [
                "The continuous uncertainty rival wins the graded precision-response",
                "problem, but it falsely admits structure on nonstructure worlds.",
                "The conformal held-out gate does not explain all response magnitude;",
                "it governs structural closure. E11 therefore weakens the pure",
                "noise-versus-structure bucket and supports governed uncertainty:",
                "continuous neuromodulatory uncertainty plus a lawful structure gate.",
            ]
        )
    elif finding == "UNCERTAINTY_FITS_BUT_GATE_RECOVERS_STRUCTURE":
        lines.extend(
            [
                "The continuous uncertainty rival wins the graded precision-response",
                "problem and remains conservative on false structural admission,",
                "but it misses too many real structures. The conformal held-out gate",
                "recovers structural sensitivity at approximately calibrated false",
                "admission. E11 therefore supports governed uncertainty: continuous",
                "expected/unexpected uncertainty explains gain, while held-out",
                "boundary evidence decides when a residual becomes structure.",
            ]
        )
    elif finding == "CONTINUOUS_UNCERTAINTY_RIVAL_WINS":
        lines.extend(
            [
                "The continuous uncertainty rival predicts both graded response and",
                "structural admission while controlling false closure. This would",
                "falsify the discrete noise-versus-structure bucket as a distinct",
                "route variable.",
            ]
        )
    elif finding == "DISCRETE_NOISE_STRUCTURE_BUCKET_SURVIVES":
        lines.extend(
            [
                "The bucket gate controls false admission and does not lose the",
                "precision-response task. This would support a stronger discrete",
                "noise-versus-structure route.",
            ]
        )
    elif finding == "HYBRID_UNCERTAINTY_GATE_NEEDED":
        lines.extend(
            [
                "A hybrid uncertainty-plus-gate model is needed. The result points",
                "toward a two-level account: continuous uncertainty supplies the",
                "gain signal, and held-out boundary evidence controls structural",
                "admission.",
            ]
        )
    else:
        lines.extend(
            [
                "The rival and bucket models are too close. The honest conclusion is",
                "that bucket uniqueness is not established for noise versus",
                "structure.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- scalar surprise is approximately matched by standardizing residuals;",
            "- train-only bait creates high train gain in all worlds;",
            "- the continuous rival sees uncertainty and train-side gain, but not held-out gain;",
            "- the structural gate is calibrated only on nonstructure held-out gains;",
            "- the phase sweep includes worlds where continuous uncertainty should win.",
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
    parser.add_argument("--main-structure-mix", type=float, default=0.50)
    parser.add_argument("--mix-grid", type=float, nargs="+", default=[0.0, 0.25, 0.5, 0.75, 1.0])
    parser.add_argument("--n-train", type=int, default=96)
    parser.add_argument("--n-test", type=int, default=96)
    parser.add_argument("--n-distractors", type=int, default=12)
    parser.add_argument("--precision-noise", type=float, default=0.050)
    parser.add_argument("--structure-noise", type=float, default=0.040)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--structure-threshold", type=float, default=0.50)
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
    json_path = args.report_dir / "e11_noise_structure_uncertainty_falsifier.json"
    md_path = args.report_dir / "e11_noise_structure_uncertainty_falsifier.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
