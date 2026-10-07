"""B2 prediction-error bucket routing probe.

This is a synthetic falsifier for B2's STAR:

    A brain is not a prediction-error minimizer. A brain is a
    prediction-error router.

The probe creates matched-scalar-surprise episodes whose residuals have
different true causes:

    retained, chart, packet, current, ambiguity, capacity, noise, governance,
    and ledger errors.

It compares four routing rules:

    1. scalar surprise only;
    2. T17 gain-only structural update;
    3. post-CBS bucket features;
    4. T18 conformal bucket routing.

The point is not biological realism. The point is a local, reproducible
control task where the nine buckets have to earn their keep.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


OPERATIONS = [
    "reweight",
    "rechart",
    "close",
    "predict",
    "sample",
    "compress",
    "suppress",
    "inhibit",
    "recalibrate",
]

EPISODES = {
    "retained": "reweight",
    "chart": "rechart",
    "packet": "close",
    "current": "predict",
    "ambiguity": "sample",
    "capacity": "compress",
    "noise": "suppress",
    "governance": "inhibit",
    "ledger": "recalibrate",
}

PACKET_KEYS = ["packet", "ambig_a", "ambig_b"]
CAPACITY_KEYS = ["cap_0", "cap_1", "cap_2", "cap_3", "cap_4"]
ALL_BOUNDARY_KEYS = PACKET_KEYS + CAPACITY_KEYS


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    scalar_surprise: float
    retained_gain: float
    chart_gain: float
    current_gain: float
    forbidden_gain: float
    max_packet_gain: float
    second_packet_gain: float
    best_packet: str
    capacity_hits_raw: int
    ambiguity_gap: float
    ledger_shift: float


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = float(np.std(x))
    if sd < 1e-12:
        return np.zeros_like(x)
    return (x - float(np.mean(x))) / sd


def fit_coef(feature: np.ndarray, residual: np.ndarray) -> float:
    denom = float(np.dot(feature, feature))
    if denom < 1e-12:
        return 0.0
    return float(np.dot(feature, residual) / denom)


def heldout_gain(
    train_feature: np.ndarray,
    train_residual: np.ndarray,
    test_feature: np.ndarray,
    test_residual: np.ndarray,
) -> float:
    coef = fit_coef(train_feature, train_residual)
    base = float(np.mean(test_residual**2))
    improved = float(np.mean((test_residual - coef * test_feature) ** 2))
    return base - improved


def train_test_corr(
    train_feature: np.ndarray,
    train_residual: np.ndarray,
    test_feature: np.ndarray,
    test_residual: np.ndarray,
) -> float:
    c_train = fit_coef(train_feature, train_residual)
    c_test = fit_coef(test_feature, test_residual)
    return abs(c_train - c_test)


def make_features(rng: np.random.Generator, n: int) -> dict[str, np.ndarray]:
    x = rng.normal(size=(n, 12))
    u = rng.uniform(-1.0, 1.0, size=n)
    theta = rng.uniform(-np.pi, np.pi, size=n)
    direction = rng.choice([-1.0, 1.0], size=n)
    theta_next = theta + direction * 0.9 + rng.normal(scale=0.08, size=n)

    features = {
        "retained": standardize(x[:, 0]),
        "chart": standardize(u),
        "chart_linear_shadow": standardize(u**3 + 0.05 * rng.normal(size=n)),
        "packet": standardize(x[:, 0] * x[:, 1]),
        "ambig_a": standardize(x[:, 2] * x[:, 3]),
        "ambig_b": standardize(x[:, 4] * x[:, 5]),
        "forbidden": standardize(x[:, 6] * x[:, 7]),
        "current": standardize(np.sin(theta_next - theta)),
    }
    for i in range(5):
        features[f"cap_{i}"] = standardize(x[:, i] * x[:, i + 7])
    return features


def make_residual(
    kind: str,
    features: dict[str, np.ndarray],
    rng: np.random.Generator,
    split: str,
) -> np.ndarray:
    noise = rng.normal(scale=0.35, size=len(next(iter(features.values()))))
    if kind == "retained":
        signal = features["retained"]
    elif kind == "chart":
        signal = features["chart"]
    elif kind == "packet":
        signal = features["packet"]
    elif kind == "current":
        signal = features["current"]
    elif kind == "ambiguity":
        signal = standardize(features["ambig_a"] + features["ambig_b"])
    elif kind == "capacity":
        signal = standardize(sum(features[k] for k in CAPACITY_KEYS))
    elif kind == "governance":
        signal = features["forbidden"]
    elif kind == "ledger":
        sign = 1.0 if split == "train" else -1.0
        signal = sign * features["packet"]
    elif kind == "noise":
        signal = rng.normal(size=len(noise))
    else:
        raise ValueError(f"unknown episode kind: {kind}")
    return standardize(signal + noise)


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    raw_capacity_threshold: float,
) -> EpisodeMetrics:
    f_train = make_features(rng, n_train)
    f_test = make_features(rng, n_test)
    r_train = make_residual(kind, f_train, rng, "train")
    r_test = make_residual(kind, f_test, rng, "test")

    gains = {
        key: heldout_gain(f_train[key], r_train, f_test[key], r_test)
        for key in [
            "retained",
            "chart",
            "current",
            "forbidden",
            *ALL_BOUNDARY_KEYS,
        ]
    }
    packet_gain_items = sorted(
        [(key, gains[key]) for key in ALL_BOUNDARY_KEYS],
        key=lambda kv: kv[1],
        reverse=True,
    )
    best_packet, max_packet_gain = packet_gain_items[0]
    second_packet_gain = packet_gain_items[1][1]
    ledger_shift = max(
        train_test_corr(f_train[key], r_train, f_test[key], r_test)
        for key in ["retained", "chart", "current", "forbidden", *ALL_BOUNDARY_KEYS]
    )

    return EpisodeMetrics(
        kind=kind,
        true_operation=EPISODES[kind],
        scalar_surprise=float(np.mean(r_test**2)),
        retained_gain=float(gains["retained"]),
        chart_gain=float(gains["chart"]),
        current_gain=float(gains["current"]),
        forbidden_gain=float(gains["forbidden"]),
        max_packet_gain=float(max_packet_gain),
        second_packet_gain=float(second_packet_gain),
        best_packet=best_packet,
        capacity_hits_raw=sum(gains[k] > raw_capacity_threshold for k in CAPACITY_KEYS),
        ambiguity_gap=float(max_packet_gain - second_packet_gain),
        ledger_shift=float(ledger_shift),
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "scalar_surprise": m.scalar_surprise,
        "retained_gain": m.retained_gain,
        "chart_gain": m.chart_gain,
        "current_gain": m.current_gain,
        "forbidden_gain": m.forbidden_gain,
        "max_packet_gain": m.max_packet_gain,
        "second_packet_gain": m.second_packet_gain,
        "best_packet": m.best_packet,
        "capacity_hits_raw": m.capacity_hits_raw,
        "ambiguity_gap": m.ambiguity_gap,
        "ledger_shift": m.ledger_shift,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def calibrate_thresholds(
    rng: np.random.Generator,
    n_calibration: int,
    n_train: int,
    n_test: int,
    alpha: float,
    raw_capacity_threshold: float,
) -> dict[str, float]:
    null = [
        episode_metrics("noise", rng, n_train, n_test, raw_capacity_threshold)
        for _ in range(n_calibration)
    ]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    route_scores = [
        max(m.retained_gain, m.chart_gain, m.current_gain, m.forbidden_gain, m.max_packet_gain)
        for m in null
    ]
    route_q = quantile(route_scores, q)
    ledger_q = quantile([m.ledger_shift for m in null], q)
    gate_scores = [
        max(
            route / max(route_q, 1e-12),
            m.ledger_shift / max(ledger_q, 1e-12),
        )
        for route, m in zip(route_scores, null)
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "retained": quantile([m.retained_gain for m in null], q),
        "chart": quantile([m.chart_gain for m in null], q),
        "current": quantile([m.current_gain for m in null], q),
        "forbidden": quantile([m.forbidden_gain for m in null], q),
        "packet": quantile([m.max_packet_gain for m in null], q),
        "route": route_q,
        "ledger": ledger_q,
        "family_gate": quantile(gate_scores, family_q),
        "raw_capacity_threshold": raw_capacity_threshold,
    }


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def t17_gain_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    if max(m.chart_gain, m.current_gain, m.forbidden_gain, m.max_packet_gain) > thresholds["route"]:
        return "close"
    return "suppress"


def bucket_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        chart_t = thresholds["chart"]
        current_t = thresholds["current"]
        forbidden_t = thresholds["forbidden"]
        packet_t = thresholds["packet"]
        ledger_t = thresholds["ledger"]
        route_t = thresholds["route"]
        family_gate_t = thresholds["family_gate"]
        ambiguity_margin = 0.06
        capacity_min_hits = 3
    else:
        retained_t = 0.12
        chart_t = 0.12
        current_t = 0.12
        forbidden_t = 0.12
        packet_t = 0.12
        ledger_t = 0.95
        route_t = 0.12
        family_gate_t = 1.0
        ambiguity_margin = 0.08
        capacity_min_hits = 3

    route_score = max(
        m.retained_gain,
        m.chart_gain,
        m.current_gain,
        m.forbidden_gain,
        m.max_packet_gain,
    )
    family_gate_score = max(
        route_score / max(route_t, 1e-12),
        m.ledger_shift / max(ledger_t, 1e-12),
    )
    packet_open = m.max_packet_gain > packet_t
    any_open = (
        m.retained_gain > retained_t
        or m.chart_gain > chart_t
        or m.current_gain > current_t
        or m.forbidden_gain > forbidden_t
        or packet_open
    )

    if conformal and family_gate_score <= family_gate_t:
        return "suppress"
    if m.ledger_shift > ledger_t:
        return "recalibrate"
    if not any_open:
        return "suppress"
    if m.forbidden_gain > forbidden_t:
        return "inhibit"
    if m.current_gain > current_t:
        return "predict"
    if m.chart_gain > chart_t:
        return "rechart"
    if m.retained_gain > retained_t:
        return "reweight"
    if m.capacity_hits_raw >= capacity_min_hits:
        return "compress"
    if packet_open and m.ambiguity_gap < ambiguity_margin:
        return "sample"
    if packet_open:
        return "close"
    return "suppress"


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


def summarize(metrics: list[EpisodeMetrics], predictions: dict[str, list[str]]) -> dict[str, Any]:
    truth = [m.true_operation for m in metrics]
    summary: dict[str, Any] = {"agents": {}, "by_kind": {}, "auc": {}}
    for agent, preds in predictions.items():
        correct = [p == t for p, t in zip(preds, truth)]
        summary["agents"][agent] = {
            "routing_accuracy": float(np.mean(correct)),
            "noise_false_admission": float(
                np.mean([p != "suppress" for p, m in zip(preds, metrics) if m.kind == "noise"])
            ),
            "current_success": float(
                np.mean([p == "predict" for p, m in zip(preds, metrics) if m.kind == "current"])
            ),
            "ledger_success": float(
                np.mean([p == "recalibrate" for p, m in zip(preds, metrics) if m.kind == "ledger"])
            ),
        }
    for kind in EPISODES:
        rows = [i for i, m in enumerate(metrics) if m.kind == kind]
        summary["by_kind"][kind] = {
            agent: float(np.mean([predictions[agent][i] == truth[i] for i in rows]))
            for agent in predictions
        }
    labels = [0 if m.kind == "noise" else 1 for m in metrics if m.kind in {"noise", "packet", "chart", "current", "retained", "governance", "capacity", "ambiguity", "ledger"}]
    subset = [m for m in metrics if m.kind in EPISODES]
    summary["auc"] = {
        "scalar_vs_noise": auc(labels, [m.scalar_surprise for m in subset]),
        "max_packet_gain_vs_noise": auc(labels, [m.max_packet_gain for m in subset]),
        "current_gain_current_vs_noise": auc(
            [1 if m.kind == "current" else 0 for m in metrics if m.kind in {"current", "noise"}],
            [m.current_gain for m in metrics if m.kind in {"current", "noise"}],
        ),
        "ledger_shift_ledger_vs_noise": auc(
            [1 if m.kind == "ledger" else 0 for m in metrics if m.kind in {"ledger", "noise"}],
            [m.ledger_shift for m in metrics if m.kind in {"ledger", "noise"}],
        ),
    }
    summary["mean_scores_by_kind"] = {
        kind: {
            "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
            "retained": float(np.mean([m.retained_gain for m in metrics if m.kind == kind])),
            "chart": float(np.mean([m.chart_gain for m in metrics if m.kind == kind])),
            "current": float(np.mean([m.current_gain for m in metrics if m.kind == kind])),
            "packet": float(np.mean([m.max_packet_gain for m in metrics if m.kind == kind])),
            "ledger": float(np.mean([m.ledger_shift for m in metrics if m.kind == kind])),
        }
        for kind in EPISODES
    }
    return summary


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def fmt(x: float) -> str:
    return f"{x:.3f}"


def write_report(
    path: Path,
    config: dict[str, Any],
    thresholds: dict[str, float],
    summary: dict[str, Any],
) -> None:
    agent_rows = []
    for agent, data in summary["agents"].items():
        agent_rows.append(
            [
                agent,
                fmt(data["routing_accuracy"]),
                fmt(data["noise_false_admission"]),
                fmt(data["current_success"]),
                fmt(data["ledger_success"]),
            ]
        )
    kind_rows = []
    for kind, true_op in EPISODES.items():
        row = [kind, true_op]
        for agent in ["scalar", "t17_gain", "post_cbs_bucket", "t18_conformal_bucket"]:
            row.append(fmt(summary["by_kind"][kind][agent]))
        kind_rows.append(row)

    score_rows = []
    for kind, scores in summary["mean_scores_by_kind"].items():
        score_rows.append(
            [
                kind,
                fmt(scores["scalar"]),
                fmt(scores["retained"]),
                fmt(scores["chart"]),
                fmt(scores["current"]),
                fmt(scores["packet"]),
                fmt(scores["ledger"]),
            ]
        )

    text = f"""# B2 Prediction-Error Bucket Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration episodes: `{config['n_calibration']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- alpha: `{config['alpha']}`

## Claim Tested

B2's STAR says that a brain-like agent should route prediction errors by
bucket, not by scalar surprise alone. This probe constructs matched-surprise
episodes for nine true buckets and compares scalar routing, T17 gain-only
routing, post-CBS bucket routing, and T18 conformal bucket routing.

## Conformal Null Thresholds

{md_table(['score', 'threshold'], [[k, fmt(v)] for k, v in thresholds.items() if isinstance(v, float)])}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'current success', 'ledger success'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'T17 gain', 'post-CBS bucket', 'T18 conformal bucket'], kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'retained', 'chart', 'current', 'packet', 'ledger'], score_rows)}

## Interpretation

This is a pass for the STAR if scalar surprise stays uninformative under
matched residual energy, T17 gain identifies structure but collapses distinct
structural operations, post-CBS features separate chart/current/packet buckets,
and T18 conformal routing keeps noise false admission near the declared alpha.

The synthetic setting is intentionally small. Its job is to expose whether the
nine buckets are operationally separable before we try to map them onto neural
recordings.
"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-kind", type=int, default=240)
    parser.add_argument("--n-calibration", type=int, default=800)
    parser.add_argument("--n-train", type=int, default=64)
    parser.add_argument("--n-test", type=int, default=64)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--out-dir", type=Path, default=Path("empirical/reports"))
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    raw_capacity_threshold = 0.12
    thresholds = calibrate_thresholds(
        rng,
        args.n_calibration,
        args.n_train,
        args.n_test,
        args.alpha,
        raw_capacity_threshold,
    )
    metrics: list[EpisodeMetrics] = []
    for kind in EPISODES:
        for _ in range(args.trials_per_kind):
            metrics.append(
                episode_metrics(kind, rng, args.n_train, args.n_test, raw_capacity_threshold)
            )

    predictions = {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "t17_gain": [t17_gain_agent(m, thresholds) for m in metrics],
        "post_cbs_bucket": [bucket_agent(m, thresholds, conformal=False) for m in metrics],
        "t18_conformal_bucket": [bucket_agent(m, thresholds, conformal=True) for m in metrics],
    }
    summary = summarize(metrics, predictions)
    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "trials_per_kind": args.trials_per_kind,
        "n_calibration": args.n_calibration,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "alpha": args.alpha,
    }
    output = {
        "config": config,
        "thresholds": thresholds,
        "summary": summary,
        "episodes": [as_dict(m) for m in metrics],
        "predictions": predictions,
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "b2_prediction_error_bucket_probe.json"
    md_path = args.out_dir / "b2_prediction_error_bucket_probe.md"
    json_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    write_report(md_path, config, thresholds, summary)
    print(f"wrote {md_path}")
    print(f"wrote {json_path}")
    print(json.dumps(summary["agents"], indent=2))


if __name__ == "__main__":
    main()
