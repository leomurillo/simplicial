"""E15 integrated continuous-absorber falsifier.

E15 tests the strongest synthetic escape hatch after B10 and E11-E14:

    Maybe there are no governed admissions at all. Maybe one sufficiently rich
    continuous policy absorbs current, structure, ambiguity, externalization,
    and refusal.

The probe pools all five domains into one training problem. The continuous
absorber receives domain tags and train-side continuous fields, and its feature
map is expanded with squares and pairwise interactions. The gate bank receives
only domain-calibrated held-out persistence scores.

The experiment separates two jobs:

    - predict graded operation intensity;
    - decide whether a signal is admitted into a durable operation.

The non-tautological result can split those jobs: a pooled continuous absorber
may fit intensity while a narrow conformal gate bank controls false admission
under bait/null pressure.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


DOMAINS = ["current", "structure", "ambiguity", "externalize", "refusal"]
FIELDS = [
    "local_drive",
    "train_evidence",
    "flow",
    "uncertainty",
    "eig",
    "resource_pressure",
    "risk_pressure",
    "value",
    "cost",
    "train_rule",
    "train_tool",
    "train_candidate",
    "compression",
    "precision",
    "competence",
]
MODEL_ORDER = [
    "scalar",
    "continuous_absorber",
    "gate_bank",
    "governed_absorber",
    "hybrid_full",
]

ADMITTED_SOURCE = {
    "current": "current_world",
    "structure": "structure_world",
    "ambiguity": "ambiguity_world",
    "externalize": "tool_world",
    "refusal": "forbidden_world",
}
BAIT_SOURCE = {
    "current": "current_bait_world",
    "structure": "uncertainty_bait_world",
    "ambiguity": "eig_bait_world",
    "externalize": "tool_bait_world",
    "refusal": "rule_bait_world",
}
OTHER_SOURCES = {
    "current": ["idle_world"],
    "structure": ["noise_world"],
    "ambiguity": ["no_sample_world"],
    "externalize": ["compress_world"],
    "refusal": ["risk_world"],
}


@dataclass(frozen=True)
class Episode:
    domain: str
    source: str
    operation: str
    scalar_score: float
    fields: dict[str, float]
    admission_score: float
    target_intensity_clean: float
    target_intensity_observed: float
    target_admission_clean: float
    target_admission_observed: float


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


def sample(rng: np.random.Generator, lo: float, hi: float) -> float:
    return float(rng.uniform(lo, hi))


def low_fields(rng: np.random.Generator) -> dict[str, float]:
    return {name: sample(rng, 0.04, 0.18) for name in FIELDS}


def set_fields(fields: dict[str, float], updates: dict[str, float]) -> dict[str, float]:
    out = dict(fields)
    out.update(updates)
    return out


def source_fields(rng: np.random.Generator, domain: str, source: str) -> tuple[dict[str, float], float]:
    fields = low_fields(rng)
    persistence = sample(rng, 0.05, 0.22)

    if domain == "current":
        if source in {"current_world", "current_bait_world"}:
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.72, 1.05),
                    "train_evidence": sample(rng, 0.70, 1.02),
                    "flow": sample(rng, 0.72, 1.06),
                    "value": sample(rng, 0.62, 0.92),
                    "precision": sample(rng, 0.56, 0.86),
                    "cost": sample(rng, 0.10, 0.28),
                },
            )
            persistence = sample(rng, 0.72, 1.04) if source == "current_world" else sample(rng, 0.08, 0.28)
        elif source == "idle_world":
            fields = set_fields(
                fields,
                {
                    "flow": sample(rng, 0.05, 0.20),
                    "value": sample(rng, 0.05, 0.24),
                    "precision": sample(rng, 0.30, 0.62),
                    "cost": sample(rng, 0.16, 0.34),
                },
            )

    elif domain == "structure":
        if source in {"structure_world", "uncertainty_bait_world"}:
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.66, 0.98),
                    "train_evidence": sample(rng, 0.72, 1.05),
                    "uncertainty": sample(rng, 0.72, 1.06),
                    "value": sample(rng, 0.54, 0.86),
                    "precision": sample(rng, 0.12, 0.36),
                    "cost": sample(rng, 0.14, 0.34),
                },
            )
            persistence = sample(rng, 0.72, 1.04) if source == "structure_world" else sample(rng, 0.07, 0.28)
        elif source == "noise_world":
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.42, 0.74),
                    "train_evidence": sample(rng, 0.18, 0.42),
                    "uncertainty": sample(rng, 0.68, 1.04),
                    "value": sample(rng, 0.20, 0.46),
                    "precision": sample(rng, 0.06, 0.26),
                },
            )

    elif domain == "ambiguity":
        if source in {"ambiguity_world", "eig_bait_world"}:
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.62, 0.94),
                    "train_evidence": sample(rng, 0.62, 0.96),
                    "uncertainty": sample(rng, 0.56, 0.90),
                    "eig": sample(rng, 0.72, 1.06),
                    "train_candidate": sample(rng, 0.72, 1.06),
                    "value": sample(rng, 0.58, 0.94),
                    "cost": sample(rng, 0.10, 0.32),
                },
            )
            persistence = sample(rng, 0.72, 1.04) if source == "ambiguity_world" else sample(rng, 0.08, 0.28)
        elif source == "no_sample_world":
            fields = set_fields(
                fields,
                {
                    "eig": sample(rng, 0.04, 0.22),
                    "train_candidate": sample(rng, 0.05, 0.24),
                    "uncertainty": sample(rng, 0.08, 0.30),
                    "value": sample(rng, 0.18, 0.44),
                    "cost": sample(rng, 0.28, 0.56),
                },
            )

    elif domain == "externalize":
        if source in {"tool_world", "tool_bait_world"}:
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.66, 0.98),
                    "resource_pressure": sample(rng, 0.72, 1.06),
                    "train_tool": sample(rng, 0.72, 1.06),
                    "value": sample(rng, 0.58, 0.94),
                    "cost": sample(rng, 0.12, 0.32),
                    "compression": sample(rng, 0.08, 0.30),
                    "precision": sample(rng, 0.42, 0.72),
                },
            )
            persistence = sample(rng, 0.72, 1.04) if source == "tool_world" else sample(rng, 0.08, 0.30)
        elif source == "compress_world":
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.46, 0.76),
                    "resource_pressure": sample(rng, 0.54, 0.86),
                    "train_tool": sample(rng, 0.12, 0.34),
                    "compression": sample(rng, 0.68, 1.02),
                    "value": sample(rng, 0.48, 0.78),
                    "cost": sample(rng, 0.12, 0.32),
                },
            )

    elif domain == "refusal":
        if source in {"forbidden_world", "rule_bait_world"}:
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.66, 0.98),
                    "train_rule": sample(rng, 0.72, 1.06),
                    "risk_pressure": sample(rng, 0.26, 0.52),
                    "value": sample(rng, 0.58, 0.94),
                    "cost": sample(rng, 0.12, 0.34),
                    "competence": sample(rng, 0.72, 1.06),
                },
            )
            persistence = sample(rng, 0.72, 1.04) if source == "forbidden_world" else sample(rng, 0.08, 0.30)
        elif source == "risk_world":
            fields = set_fields(
                fields,
                {
                    "local_drive": sample(rng, 0.62, 0.96),
                    "train_rule": sample(rng, 0.06, 0.24),
                    "risk_pressure": sample(rng, 0.72, 1.06),
                    "value": sample(rng, 0.58, 0.94),
                    "cost": sample(rng, 0.22, 0.48),
                    "competence": sample(rng, 0.70, 1.04),
                },
            )

    else:
        raise ValueError(f"unknown domain: {domain}")

    return fields, persistence


def domain_intensity(domain: str, fields: dict[str, float], admission: float) -> float:
    if domain == "current":
        score = 2.6 * fields["flow"] + 1.3 * fields["local_drive"] + 0.8 * fields["value"] - 1.8 * fields["cost"] - 1.9
    elif domain == "structure":
        score = 2.4 * fields["uncertainty"] + 1.7 * fields["train_evidence"] + 0.7 * fields["value"] - 1.7
    elif domain == "ambiguity":
        score = 2.7 * fields["eig"] + 1.5 * fields["train_candidate"] + 0.7 * fields["uncertainty"] - 1.8 * fields["cost"] - 1.9
    elif domain == "externalize":
        score = 2.5 * fields["resource_pressure"] + 1.7 * fields["train_tool"] + 0.6 * fields["value"] - 1.7 * fields["cost"] - 2.0
    elif domain == "refusal":
        score = 2.1 * fields["risk_pressure"] + 1.9 * fields["train_rule"] + 0.7 * fields["competence"] - 1.5
    else:
        raise ValueError(f"unknown domain: {domain}")
    return float(np.clip(sigmoid(score) + 0.04 * admission, 0.0, 1.0))


def operation_for(domain: str, source: str) -> str:
    if source == ADMITTED_SOURCE[domain]:
        return {
            "current": "admit_current",
            "structure": "close_structure",
            "ambiguity": "preserve_ambiguity",
            "externalize": "externalize_tool",
            "refusal": "refuse",
        }[domain]
    if source == BAIT_SOURCE[domain]:
        return {
            "current": "resist_transient_current",
            "structure": "resist_false_closure",
            "ambiguity": "resist_eig_bait",
            "externalize": "resist_tool_bait",
            "refusal": "resist_false_refusal",
        }[domain]
    return {
        "current": "idle",
        "structure": "track_noise",
        "ambiguity": "do_not_sample",
        "externalize": "compress_internally",
        "refusal": "risk_suppress",
    }[domain]


def make_episode(
    rng: np.random.Generator,
    domain: str,
    source: str,
    intensity_noise: float,
    admission_noise: float,
) -> Episode:
    fields, persistence = source_fields(rng, domain, source)
    fields = {key: noisy_clip(rng, value, 0.035, lo=0.0, hi=1.2) for key, value in fields.items()}
    target_admission_clean = 1.0 if source == ADMITTED_SOURCE[domain] else 0.0
    admission_score = noisy_clip(
        rng,
        0.82 * persistence + 0.10 * fields["local_drive"] + 0.08 * fields["value"],
        0.045,
        lo=0.0,
        hi=1.3,
    )
    intensity_clean = domain_intensity(domain, fields, target_admission_clean)
    return Episode(
        domain=domain,
        source=source,
        operation=operation_for(domain, source),
        scalar_score=noisy_clip(rng, 1.0, 0.020, lo=0.92, hi=1.08),
        fields=fields,
        admission_score=admission_score,
        target_intensity_clean=intensity_clean,
        target_intensity_observed=float(np.clip(intensity_clean + rng.normal(scale=intensity_noise), 0.0, 1.0)),
        target_admission_clean=target_admission_clean,
        target_admission_observed=float(np.clip(target_admission_clean + rng.normal(scale=admission_noise), 0.0, 1.0)),
    )


def make_dataset(
    rng: np.random.Generator,
    trials_per_domain: int,
    admitted_share: float,
    bait_share: float,
    intensity_noise: float,
    admission_noise: float,
) -> list[Episode]:
    episodes: list[Episode] = []
    admitted_share = float(np.clip(admitted_share, 0.0, 1.0))
    bait_share = float(np.clip(bait_share, 0.0, 1.0 - admitted_share))
    for domain in DOMAINS:
        for _ in range(trials_per_domain):
            u = rng.random()
            if u < admitted_share:
                source = ADMITTED_SOURCE[domain]
            elif u < admitted_share + bait_share:
                source = BAIT_SOURCE[domain]
            else:
                source = str(rng.choice(OTHER_SOURCES[domain]))
            episodes.append(make_episode(rng, domain, source, intensity_noise, admission_noise))
    rng.shuffle(episodes)
    return episodes


def calibrate_gates(episodes: list[Episode], alpha: float) -> dict[str, float]:
    gates: dict[str, float] = {}
    for domain in DOMAINS:
        nonadmitted = [
            ep.admission_score
            for ep in episodes
            if ep.domain == domain and ep.target_admission_clean < 0.5
        ]
        if not nonadmitted:
            gates[domain] = float("inf")
        else:
            gates[domain] = quantile(nonadmitted, 1.0 - alpha)
    return gates


def gate_bit(ep: Episode, gates: dict[str, float]) -> float:
    return 1.0 if ep.admission_score > gates[ep.domain] else 0.0


def domain_vector(domain: str) -> list[float]:
    return [1.0 if domain == item else 0.0 for item in DOMAINS]


def feature_vector(ep: Episode, kind: str, gates: dict[str, float]) -> list[float]:
    domain_bits = domain_vector(ep.domain)
    fields = [ep.fields[name] for name in FIELDS]
    bit = gate_bit(ep, gates)
    domain_gate_bits = [bit * d for d in domain_bits]
    if kind == "scalar":
        return [ep.scalar_score]
    if kind == "continuous":
        return domain_bits + fields
    if kind == "gate":
        return domain_bits + [bit] + domain_gate_bits
    if kind == "governed":
        return domain_bits + fields + [bit] + domain_gate_bits
    if kind == "hybrid":
        return domain_bits + fields + [ep.admission_score, bit] + domain_gate_bits
    raise ValueError(f"unknown feature kind: {kind}")


def target_vector(episodes: list[Episode], kind: str) -> np.ndarray:
    if kind == "intensity":
        return np.asarray([ep.target_intensity_observed for ep in episodes], dtype=float)
    if kind == "admission":
        return np.asarray([ep.target_admission_observed for ep in episodes], dtype=float)
    raise ValueError(f"unknown target kind: {kind}")


def raw_matrix(episodes: list[Episode], kind: str, gates: dict[str, float]) -> np.ndarray:
    return np.asarray([feature_vector(ep, kind, gates) for ep in episodes], dtype=float)


def expand_matrix(x: np.ndarray, mean: np.ndarray | None = None, sd: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    parts = [np.ones((z.shape[0], 1)), z, z * z]
    interactions = []
    for i in range(z.shape[1]):
        for j in range(i + 1, z.shape[1]):
            interactions.append((z[:, i] * z[:, j])[:, None])
    if interactions:
        parts.extend(interactions)
    return np.hstack(parts), mean, sd


def fit_ridge(
    episodes: list[Episode],
    name: str,
    feature_kind: str,
    target_kind: str,
    gates: dict[str, float],
    ridge: float,
) -> RidgeModel:
    x_raw = raw_matrix(episodes, feature_kind, gates)
    phi, mean, sd = expand_matrix(x_raw)
    y = target_vector(episodes, target_kind)
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


def predict(model: RidgeModel, episodes: list[Episode], gates: dict[str, float]) -> np.ndarray:
    x_raw = raw_matrix(episodes, model.feature_kind, gates)
    phi, _, _ = expand_matrix(
        x_raw,
        np.asarray(model.mean, dtype=float),
        np.asarray(model.sd, dtype=float),
    )
    pred = phi @ np.asarray(model.coef, dtype=float)
    return np.clip(pred, 0.0, 1.0)


def rmse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y - pred) ** 2)))


def r2(y: np.ndarray, pred: np.ndarray) -> float:
    denom = float(np.sum((y - y.mean()) ** 2))
    if denom <= 1e-12:
        return float("nan")
    return float(1.0 - np.sum((y - pred) ** 2) / denom)


def mean_or_nan(values: list[float]) -> float:
    if not values:
        return float("nan")
    return float(np.mean(np.asarray(values, dtype=float)))


def classification_metrics(
    episodes: list[Episode],
    pred: np.ndarray,
    threshold: float,
) -> dict[str, Any]:
    truth = np.asarray([ep.target_admission_clean >= 0.5 for ep in episodes], dtype=bool)
    calls = pred >= threshold
    domains: dict[str, dict[str, float]] = {}
    for domain in DOMAINS:
        mask = np.asarray([ep.domain == domain for ep in episodes], dtype=bool)
        admitted = mask & truth
        nonadmitted = mask & ~truth
        bait = np.asarray([ep.domain == domain and ep.source == BAIT_SOURCE[domain] for ep in episodes], dtype=bool)
        domains[domain] = {
            "detection": mean_or_nan([float(v) for v in calls[admitted]]),
            "false_admission": mean_or_nan([float(v) for v in calls[nonadmitted]]),
            "bait_false_admission": mean_or_nan([float(v) for v in calls[bait]]),
        }
    return {
        "accuracy": float(np.mean(calls == truth)),
        "admission_detection": mean_or_nan([float(v) for v in calls[truth]]),
        "nonadmitted_false_admission": mean_or_nan([float(v) for v in calls[~truth]]),
        "bait_false_admission": mean_or_nan(
            [float(calls[i]) for i, ep in enumerate(episodes) if ep.source == BAIT_SOURCE[ep.domain]]
        ),
        "other_false_admission": mean_or_nan(
            [
                float(calls[i])
                for i, ep in enumerate(episodes)
                if ep.target_admission_clean < 0.5 and ep.source != BAIT_SOURCE[ep.domain]
            ]
        ),
        "by_domain": domains,
    }


def source_means(episodes: list[Episode]) -> dict[str, dict[str, float]]:
    grouped: dict[str, list[Episode]] = {}
    for ep in episodes:
        key = f"{ep.domain}:{ep.source}"
        grouped.setdefault(key, []).append(ep)
    means: dict[str, dict[str, float]] = {}
    for key, rows in sorted(grouped.items()):
        means[key] = {
            "n": float(len(rows)),
            "intensity": float(np.mean([ep.target_intensity_clean for ep in rows])),
            "admission": float(np.mean([ep.target_admission_clean for ep in rows])),
            "admission_score": float(np.mean([ep.admission_score for ep in rows])),
            "local_drive": float(np.mean([ep.fields["local_drive"] for ep in rows])),
            "flow": float(np.mean([ep.fields["flow"] for ep in rows])),
            "uncertainty": float(np.mean([ep.fields["uncertainty"] for ep in rows])),
            "eig": float(np.mean([ep.fields["eig"] for ep in rows])),
            "resource": float(np.mean([ep.fields["resource_pressure"] for ep in rows])),
            "risk": float(np.mean([ep.fields["risk_pressure"] for ep in rows])),
            "train_rule": float(np.mean([ep.fields["train_rule"] for ep in rows])),
            "train_tool": float(np.mean([ep.fields["train_tool"] for ep in rows])),
            "train_candidate": float(np.mean([ep.fields["train_candidate"] for ep in rows])),
        }
    return means


def evaluate(
    train: list[Episode],
    calibration: list[Episode],
    test: list[Episode],
    alpha: float,
    ridge: float,
    admission_threshold: float,
) -> dict[str, Any]:
    gates = calibrate_gates(calibration, alpha)
    feature_kind = {
        "scalar": "scalar",
        "continuous_absorber": "continuous",
        "gate_bank": "gate",
        "governed_absorber": "governed",
        "hybrid_full": "hybrid",
    }
    y_intensity = target_vector(test, "intensity")
    y_admission = target_vector(test, "admission")
    overall: dict[str, Any] = {}
    models: dict[str, Any] = {}

    for name in MODEL_ORDER:
        intensity_model = fit_ridge(train, name, feature_kind[name], "intensity", gates, ridge)
        admission_model = fit_ridge(train, name, feature_kind[name], "admission", gates, ridge)
        intensity_pred = predict(intensity_model, test, gates)
        admission_pred = predict(admission_model, test, gates)
        overall[name] = {
            "intensity": {
                "rmse_observed": rmse(y_intensity, intensity_pred),
                "r2_observed": r2(y_intensity, intensity_pred),
            },
            "admission_regression": {
                "rmse_observed": rmse(y_admission, admission_pred),
                "r2_observed": r2(y_admission, admission_pred),
            },
            "admission_classification": classification_metrics(test, admission_pred, admission_threshold),
        }
        models[name] = {
            "intensity": {
                "feature_kind": intensity_model.feature_kind,
                "feature_count": intensity_model.feature_count,
                "expanded_count": intensity_model.expanded_count,
            },
            "admission": {
                "feature_kind": admission_model.feature_kind,
                "feature_count": admission_model.feature_count,
                "expanded_count": admission_model.expanded_count,
            },
        }

    return {
        "gates": gates,
        "overall": overall,
        "models": models,
        "test_source_means": source_means(test),
    }


def winner(overall: dict[str, Any], task: str) -> str:
    if task == "intensity":
        return min(MODEL_ORDER, key=lambda name: overall[name]["intensity"]["rmse_observed"])
    if task == "admission":
        return min(MODEL_ORDER, key=lambda name: overall[name]["admission_regression"]["rmse_observed"])
    raise ValueError(f"unknown task: {task}")


def decision_quantities(main: dict[str, Any]) -> dict[str, float]:
    overall = main["overall"]
    cont_cls = overall["continuous_absorber"]["admission_classification"]
    gate_cls = overall["gate_bank"]["admission_classification"]
    governed_cls = overall["governed_absorber"]["admission_classification"]
    hybrid_cls = overall["hybrid_full"]["admission_classification"]
    return {
        "continuous_intensity_rmse": overall["continuous_absorber"]["intensity"]["rmse_observed"],
        "gate_intensity_rmse": overall["gate_bank"]["intensity"]["rmse_observed"],
        "governed_intensity_rmse": overall["governed_absorber"]["intensity"]["rmse_observed"],
        "hybrid_intensity_rmse": overall["hybrid_full"]["intensity"]["rmse_observed"],
        "continuous_admission_rmse": overall["continuous_absorber"]["admission_regression"]["rmse_observed"],
        "gate_admission_rmse": overall["gate_bank"]["admission_regression"]["rmse_observed"],
        "governed_admission_rmse": overall["governed_absorber"]["admission_regression"]["rmse_observed"],
        "hybrid_admission_rmse": overall["hybrid_full"]["admission_regression"]["rmse_observed"],
        "continuous_false_admission": cont_cls["nonadmitted_false_admission"],
        "gate_false_admission": gate_cls["nonadmitted_false_admission"],
        "governed_false_admission": governed_cls["nonadmitted_false_admission"],
        "hybrid_false_admission": hybrid_cls["nonadmitted_false_admission"],
        "continuous_detection": cont_cls["admission_detection"],
        "gate_detection": gate_cls["admission_detection"],
        "governed_detection": governed_cls["admission_detection"],
        "hybrid_detection": hybrid_cls["admission_detection"],
        "continuous_bait_false": cont_cls["bait_false_admission"],
        "gate_bait_false": gate_cls["bait_false_admission"],
        "governed_bait_false": governed_cls["bait_false_admission"],
        "hybrid_bait_false": hybrid_cls["bait_false_admission"],
    }


def classify_finding(args: argparse.Namespace, main: dict[str, Any]) -> str:
    dq = decision_quantities(main)
    cont_fits_intensity = dq["continuous_intensity_rmse"] + args.decision_margin < dq["gate_intensity_rmse"]
    gate_controls = (
        dq["gate_false_admission"] + args.false_admission_margin < dq["continuous_false_admission"]
        and dq["gate_detection"] >= args.detection_floor
    )
    governed_controls = (
        dq["governed_false_admission"] + args.false_admission_margin < dq["continuous_false_admission"]
        and dq["governed_detection"] >= args.detection_floor
    )
    absorber_absorbs = (
        dq["continuous_false_admission"] <= dq["gate_false_admission"] + args.false_admission_margin
        and dq["continuous_detection"] >= args.detection_floor
        and cont_fits_intensity
    )
    if absorber_absorbs:
        return "CONTINUOUS_ABSORBER_ABSORBS_GOVERNANCE"
    if cont_fits_intensity and gate_controls and governed_controls:
        return "CONTINUOUS_ABSORBER_FITS_INTENSITY_BUT_GATES_CONTROL_ADMISSION"
    if governed_controls:
        return "INTEGRATED_HYBRID_NEEDED"
    return "INTEGRATED_ABSORBER_INCONCLUSIVE"


def run_once(
    args: argparse.Namespace,
    seed: int,
    trials_per_domain: int,
    admitted_share: float,
    bait_share: float,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    train = make_dataset(
        rng,
        trials_per_domain,
        admitted_share,
        bait_share,
        args.intensity_noise,
        args.admission_noise,
    )
    calibration = make_dataset(
        rng,
        max(80, trials_per_domain // 2),
        admitted_share,
        bait_share,
        args.intensity_noise,
        args.admission_noise,
    )
    test = make_dataset(
        rng,
        trials_per_domain,
        admitted_share,
        bait_share,
        args.intensity_noise,
        args.admission_noise,
    )
    return evaluate(train, calibration, test, args.alpha, args.ridge, args.admission_threshold)


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    main = run_once(
        args,
        args.seed,
        args.trials_per_domain,
        args.main_admitted_share,
        args.main_bait_share,
    )
    phase_rows = []
    for i, admitted_share in enumerate(args.admitted_grid):
        bait_share = min(args.main_bait_share, max(0.0, 1.0 - admitted_share - args.other_floor))
        row_result = run_once(
            args,
            args.seed + 101 + i,
            args.sweep_trials_per_domain,
            admitted_share,
            bait_share,
        )
        dq = decision_quantities(row_result)
        phase_rows.append(
            {
                "admitted_share": admitted_share,
                "bait_share": bait_share,
                "intensity_winner": winner(row_result["overall"], "intensity"),
                "admission_winner": winner(row_result["overall"], "admission"),
                "intensity_rmse": {
                    name: row_result["overall"][name]["intensity"]["rmse_observed"] for name in MODEL_ORDER
                },
                "admission_rmse": {
                    name: row_result["overall"][name]["admission_regression"]["rmse_observed"]
                    for name in MODEL_ORDER
                },
                "false_admission": {
                    name: row_result["overall"][name]["admission_classification"]["nonadmitted_false_admission"]
                    for name in MODEL_ORDER
                },
                "admission_detection": {
                    name: row_result["overall"][name]["admission_classification"]["admission_detection"]
                    for name in MODEL_ORDER
                },
                "continuous_bait_false": dq["continuous_bait_false"],
                "gate_bait_false": dq["gate_bait_false"],
                "governed_bait_false": dq["governed_bait_false"],
            }
        )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config": {
            "seed": args.seed,
            "trials_per_domain": args.trials_per_domain,
            "sweep_trials_per_domain": args.sweep_trials_per_domain,
            "main_admitted_share": args.main_admitted_share,
            "main_bait_share": args.main_bait_share,
            "other_floor": args.other_floor,
            "admitted_grid": args.admitted_grid,
            "intensity_noise": args.intensity_noise,
            "admission_noise": args.admission_noise,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "admission_threshold": args.admission_threshold,
        },
        "finding": classify_finding(args, main),
        "main": main,
        "decision_quantities": decision_quantities(main),
        "phase_sweep": phase_rows,
    }
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
        cls = overall[name]["admission_classification"]
        model_rows.append(
            [
                name,
                fmt(overall[name]["intensity"]["rmse_observed"]),
                fmt(overall[name]["intensity"]["r2_observed"]),
                fmt(overall[name]["admission_regression"]["rmse_observed"]),
                fmt(cls["accuracy"]),
                fmt(cls["admission_detection"]),
                fmt(cls["nonadmitted_false_admission"]),
                fmt(cls["bait_false_admission"]),
                fmt(cls["other_false_admission"]),
            ]
        )

    gate_rows = [[domain, fmt(value)] for domain, value in main["gates"].items()]

    domain_rows = []
    for domain in DOMAINS:
        cont = overall["continuous_absorber"]["admission_classification"]["by_domain"][domain]
        gate = overall["gate_bank"]["admission_classification"]["by_domain"][domain]
        governed = overall["governed_absorber"]["admission_classification"]["by_domain"][domain]
        domain_rows.append(
            [
                domain,
                fmt(cont["detection"]),
                fmt(cont["false_admission"]),
                fmt(cont["bait_false_admission"]),
                fmt(gate["detection"]),
                fmt(gate["false_admission"]),
                fmt(gate["bait_false_admission"]),
                fmt(governed["false_admission"]),
            ]
        )

    source_rows = []
    for key, data in main["test_source_means"].items():
        source_rows.append(
            [
                key,
                str(int(data["n"])),
                fmt(data["intensity"]),
                fmt(data["admission"]),
                fmt(data["admission_score"]),
                fmt(data["local_drive"]),
                fmt(data["flow"]),
                fmt(data["uncertainty"]),
                fmt(data["eig"]),
                fmt(data["resource"]),
                fmt(data["risk"]),
                fmt(data["train_rule"]),
                fmt(data["train_tool"]),
                fmt(data["train_candidate"]),
            ]
        )

    sweep_rows = []
    for row in result["phase_sweep"]:
        sweep_rows.append(
            [
                fmt(row["admitted_share"]),
                fmt(row["bait_share"]),
                row["intensity_winner"],
                row["admission_winner"],
                fmt(row["intensity_rmse"]["continuous_absorber"]),
                fmt(row["intensity_rmse"]["gate_bank"]),
                fmt(row["intensity_rmse"]["governed_absorber"]),
                fmt(row["false_admission"]["continuous_absorber"]),
                fmt(row["false_admission"]["gate_bank"]),
                fmt(row["admission_detection"]["gate_bank"]),
                fmt(row["continuous_bait_false"]),
                fmt(row["gate_bait_false"]),
            ]
        )

    lines = [
        "# E15 Integrated Absorber Falsifier",
        "",
        f"- timestamp: `{result['timestamp']}`",
        f"- seed: `{config['seed']}`",
        f"- trials per domain: `{config['trials_per_domain']}`",
        f"- admitted/bait share: `{config['main_admitted_share']}` / `{config['main_bait_share']}`",
        f"- alpha: `{config['alpha']}`",
        f"- ridge: `{config['ridge']}`",
        f"- finding: **{result['finding']}**",
        "",
        "## Claim Tested",
        "",
        "E15 tests whether a single pooled continuous policy can absorb the",
        "governed-admission story. The continuous absorber sees all domains,",
        "train-side control fields, squares, and pairwise interactions. The",
        "gate bank sees only domain-calibrated held-out persistence.",
        "",
        "The probe scores graded operation intensity separately from admission",
        "into a durable operation.",
        "",
        "## Main Decision Quantities",
        "",
        md_table(
            ["quantity", "value"],
            [
                ["continuous intensity RMSE", fmt(dq["continuous_intensity_rmse"])],
                ["gate intensity RMSE", fmt(dq["gate_intensity_rmse"])],
                ["governed intensity RMSE", fmt(dq["governed_intensity_rmse"])],
                ["hybrid intensity RMSE", fmt(dq["hybrid_intensity_rmse"])],
                ["continuous admission RMSE", fmt(dq["continuous_admission_rmse"])],
                ["gate admission RMSE", fmt(dq["gate_admission_rmse"])],
                ["governed admission RMSE", fmt(dq["governed_admission_rmse"])],
                ["hybrid admission RMSE", fmt(dq["hybrid_admission_rmse"])],
                ["continuous false admission", fmt(dq["continuous_false_admission"])],
                ["gate false admission", fmt(dq["gate_false_admission"])],
                ["governed false admission", fmt(dq["governed_false_admission"])],
                ["continuous detection", fmt(dq["continuous_detection"])],
                ["gate detection", fmt(dq["gate_detection"])],
                ["governed detection", fmt(dq["governed_detection"])],
                ["continuous bait false", fmt(dq["continuous_bait_false"])],
                ["gate bait false", fmt(dq["gate_bait_false"])],
            ],
        ),
        "",
        "## Model Summary",
        "",
        md_table(
            [
                "model",
                "intensity RMSE",
                "intensity R2",
                "admission RMSE",
                "admission acc",
                "detect",
                "nonadmit FA",
                "bait FA",
                "other FA",
            ],
            model_rows,
        ),
        "",
        "## Calibrated Gates",
        "",
        md_table(["domain", "gate"], gate_rows),
        "",
        "## Domain Admission Summary",
        "",
        md_table(
            [
                "domain",
                "cont detect",
                "cont FA",
                "cont bait FA",
                "gate detect",
                "gate FA",
                "gate bait FA",
                "governed FA",
            ],
            domain_rows,
        ),
        "",
        "## Source Means",
        "",
        md_table(
            [
                "source",
                "n",
                "intensity",
                "admit",
                "gate score",
                "drive",
                "flow",
                "uncert",
                "eig",
                "resource",
                "risk",
                "rule",
                "tool",
                "candidate",
            ],
            source_rows,
        ),
        "",
        "## Phase Sweep",
        "",
        md_table(
            [
                "admit share",
                "bait share",
                "intensity winner",
                "admission winner",
                "cont intensity",
                "gate intensity",
                "governed intensity",
                "cont FA",
                "gate FA",
                "gate detect",
                "cont bait FA",
                "gate bait FA",
            ],
            sweep_rows,
        ),
        "",
        "## Interpretation",
        "",
    ]

    if result["finding"] == "CONTINUOUS_ABSORBER_FITS_INTENSITY_BUT_GATES_CONTROL_ADMISSION":
        lines.extend(
            [
                "The pooled absorber wins the graded intensity problem against the",
                "gate-only model, which is exactly where continuous control fields",
                "should win. But it still admits bait/null cases too often. The",
                "calibrated gate bank recovers admission across domains while",
                "controlling false admission, and the governed absorber combines",
                "both advantages.",
            ]
        )
    elif result["finding"] == "CONTINUOUS_ABSORBER_ABSORBS_GOVERNANCE":
        lines.extend(
            [
                "The pooled continuous absorber controls false admission while",
                "preserving detection and fitting intensity. This would demote",
                "governed admission to a descriptive discretization in the current",
                "synthetic grammar.",
            ]
        )
    elif result["finding"] == "INTEGRATED_HYBRID_NEEDED":
        lines.extend(
            [
                "The integrated hybrid is needed: continuous fields and admission",
                "gates do different jobs, but neither side cleanly dominates alone.",
            ]
        )
    else:
        lines.extend(
            [
                "The pooled absorber and gate bank are too close or unstable in this",
                "configuration. E15 does not decide whether admission gates survive",
                "the integrated absorber challenge.",
            ]
        )

    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- scalar surprise is matched across all domains;",
            "- the continuous absorber pools all five domains and receives expanded nonlinear features;",
            "- admitted and bait cases share train-side continuous fields within each domain;",
            "- only held-out persistence separates durable admission from local bait;",
            "- gates are calibrated on non-admitted calibration cases, not on the test labels;",
            "- the result is synthetic architectural evidence, not biological validation.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-domain", type=int, default=650)
    parser.add_argument("--sweep-trials-per-domain", type=int, default=420)
    parser.add_argument("--main-admitted-share", type=float, default=0.60)
    parser.add_argument("--main-bait-share", type=float, default=0.30)
    parser.add_argument("--other-floor", type=float, default=0.10)
    parser.add_argument("--admitted-grid", type=float, nargs="+", default=[0.0, 0.25, 0.45, 0.60, 0.80, 1.0])
    parser.add_argument("--intensity-noise", type=float, default=0.045)
    parser.add_argument("--admission-noise", type=float, default=0.040)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=2e-3)
    parser.add_argument("--admission-threshold", type=float, default=0.50)
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
    json_path = args.report_dir / "e15_integrated_absorber_falsifier.json"
    md_path = args.report_dir / "e15_integrated_absorber_falsifier.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
