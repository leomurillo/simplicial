"""B3 time-reversal blindness probe.

This is a synthetic falsifier for the B-series current bucket.

The probe builds three Markov worlds on the same ring:

    1. forward current: clockwise drift;
    2. reverse current: counter-clockwise drift;
    3. null current: detailed-balance dynamics.

All three worlds have the same stationary distribution, the same stay rate,
and the same symmetrized transition backbone. Scalar surprise and symmetric
geometry therefore have no principled way to distinguish forward from reverse.

The current bucket earns its keep only if a signed antisymmetric statistic
separates forward from reverse while a conformal current gate controls false
current admission on the detailed-balance null.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["forward", "reverse", "null"]
DIRECTION_LABELS = {"forward": 1, "reverse": -1, "null": 0}


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_direction: int
    has_current: bool
    forward_steps: int
    reverse_steps: int
    stay_steps: int
    scalar_score: float
    symmetric_score: float
    packet_unsigned_score: float
    current_score: float
    alpha_hat: float
    beta_hat: float
    predictor_block: list[list[float]]


@dataclass(frozen=True)
class ThresholdClassifier:
    score: str
    threshold: float
    high_label: int
    train_accuracy: float


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def simulate_ring(
    rng: np.random.Generator,
    n_states: int,
    length: int,
    forward_prob: float,
    reverse_prob: float,
    stay_prob: float,
) -> np.ndarray:
    probs = np.asarray([forward_prob, reverse_prob, stay_prob], dtype=float)
    probs = probs / float(np.sum(probs))
    steps = rng.choice(np.asarray([1, -1, 0], dtype=int), size=length, p=probs)

    # Materialize the ring walk to keep the test honest: this is a Markov chain
    # on states, not just an iid step sampler.
    states = np.empty(length + 1, dtype=int)
    states[0] = int(rng.integers(0, n_states))
    for t, step in enumerate(steps):
        states[t + 1] = (states[t] + int(step)) % n_states
    del states
    return steps


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_states: int,
    length: int,
    drift_prob: float,
    counter_prob: float,
    stay_prob: float,
) -> EpisodeMetrics:
    if kind == "forward":
        forward_prob = drift_prob
        reverse_prob = counter_prob
    elif kind == "reverse":
        forward_prob = counter_prob
        reverse_prob = drift_prob
    elif kind == "null":
        forward_prob = 0.5 * (drift_prob + counter_prob)
        reverse_prob = 0.5 * (drift_prob + counter_prob)
    else:
        raise ValueError(f"unknown kind: {kind}")

    steps = simulate_ring(
        rng,
        n_states=n_states,
        length=length,
        forward_prob=forward_prob,
        reverse_prob=reverse_prob,
        stay_prob=stay_prob,
    )

    sym_move_prob = 0.5 * (drift_prob + counter_prob)
    nll = np.where(
        steps == 0,
        -np.log(stay_prob),
        -np.log(sym_move_prob),
    )
    angle = 2.0 * np.pi / float(n_states)
    cos_steps = np.cos(angle * steps)
    sin_steps = np.sin(angle * steps)
    sin_unit = float(np.sin(angle))

    alpha_hat = float(np.mean(cos_steps))
    beta_hat = float(np.mean(sin_steps))
    current_score = beta_hat / max(abs(sin_unit), 1e-12)
    predictor_block = [
        [alpha_hat, beta_hat],
        [-beta_hat, alpha_hat],
    ]

    return EpisodeMetrics(
        kind=kind,
        true_direction=DIRECTION_LABELS[kind],
        has_current=kind != "null",
        forward_steps=int(np.sum(steps == 1)),
        reverse_steps=int(np.sum(steps == -1)),
        stay_steps=int(np.sum(steps == 0)),
        scalar_score=float(np.mean(nll)),
        symmetric_score=alpha_hat,
        packet_unsigned_score=abs(float(current_score)),
        current_score=float(current_score),
        alpha_hat=alpha_hat,
        beta_hat=beta_hat,
        predictor_block=predictor_block,
    )


def metric_score(m: EpisodeMetrics, score: str) -> float:
    if score == "abs_current_score":
        return abs(m.current_score)
    value = getattr(m, score)
    return float(value)


def classifier_predict(clf: ThresholdClassifier, value: float) -> int:
    low_label = -clf.high_label
    return clf.high_label if value >= clf.threshold else low_label


def fit_binary_threshold_classifier(
    metrics: list[EpisodeMetrics],
    score: str,
    positive_label: int,
    negative_label: int,
) -> ThresholdClassifier:
    rows = [
        (metric_score(m, score), m.true_direction)
        for m in metrics
        if m.true_direction in {positive_label, negative_label}
    ]
    values = np.asarray([v for v, _ in rows], dtype=float)
    labels = np.asarray([y for _, y in rows], dtype=int)

    unique_values = np.unique(values)
    if len(unique_values) == 1:
        candidates = np.asarray([unique_values[0]], dtype=float)
    else:
        mids = 0.5 * (unique_values[:-1] + unique_values[1:])
        candidates = np.concatenate(
            [
                np.asarray([unique_values[0] - 1e-9]),
                mids,
                np.asarray([unique_values[-1] + 1e-9]),
            ]
        )

    best = ThresholdClassifier(score=score, threshold=float(candidates[0]), high_label=positive_label, train_accuracy=-1.0)
    for threshold in candidates:
        for high_label in [positive_label, negative_label]:
            preds = np.where(values >= threshold, high_label, -high_label)
            acc = float(np.mean(preds == labels))
            if acc > best.train_accuracy:
                best = ThresholdClassifier(
                    score=score,
                    threshold=float(threshold),
                    high_label=int(high_label),
                    train_accuracy=acc,
                )
    return best


def fit_presence_threshold_classifier(
    metrics: list[EpisodeMetrics],
    score: str,
) -> ThresholdClassifier:
    rows = [(metric_score(m, score), 1 if m.has_current else -1) for m in metrics]
    values = np.asarray([v for v, _ in rows], dtype=float)
    labels = np.asarray([y for _, y in rows], dtype=int)

    unique_values = np.unique(values)
    if len(unique_values) == 1:
        candidates = np.asarray([unique_values[0]], dtype=float)
    else:
        mids = 0.5 * (unique_values[:-1] + unique_values[1:])
        candidates = np.concatenate(
            [
                np.asarray([unique_values[0] - 1e-9]),
                mids,
                np.asarray([unique_values[-1] + 1e-9]),
            ]
        )

    def balanced_accuracy(preds: np.ndarray) -> float:
        pos = labels == 1
        neg = labels == -1
        tpr = float(np.mean(preds[pos] == 1)) if np.any(pos) else float("nan")
        tnr = float(np.mean(preds[neg] == -1)) if np.any(neg) else float("nan")
        return 0.5 * (tpr + tnr)

    best = ThresholdClassifier(score=score, threshold=float(candidates[0]), high_label=1, train_accuracy=-1.0)
    for threshold in candidates:
        for high_label in [1, -1]:
            preds = np.where(values >= threshold, high_label, -high_label)
            acc = balanced_accuracy(preds)
            if acc > best.train_accuracy:
                best = ThresholdClassifier(
                    score=score,
                    threshold=float(threshold),
                    high_label=int(high_label),
                    train_accuracy=acc,
                )
    return best


def evaluate_direction_classifier(
    metrics: list[EpisodeMetrics],
    clf: ThresholdClassifier,
) -> dict[str, float]:
    rows = [m for m in metrics if m.kind in {"forward", "reverse"}]
    preds = [classifier_predict(clf, metric_score(m, clf.score)) for m in rows]
    truth = [m.true_direction for m in rows]
    return {
        "accuracy": float(np.mean([p == y for p, y in zip(preds, truth)])),
        "forward_accuracy": float(np.mean([p == y for p, y, m in zip(preds, truth, rows) if m.kind == "forward"])),
        "reverse_accuracy": float(np.mean([p == y for p, y, m in zip(preds, truth, rows) if m.kind == "reverse"])),
    }


def evaluate_presence_classifier(
    metrics: list[EpisodeMetrics],
    clf: ThresholdClassifier,
) -> dict[str, float]:
    preds = [1 if classifier_predict(clf, metric_score(m, clf.score)) == 1 else 0 for m in metrics]
    truth = [1 if m.has_current else 0 for m in metrics]
    return {
        "accuracy": float(np.mean([p == y for p, y in zip(preds, truth)])),
        "current_detection": float(np.mean([p == 1 for p, m in zip(preds, metrics) if m.has_current])),
        "null_false_admission": float(np.mean([p == 1 for p, m in zip(preds, metrics) if not m.has_current])),
    }


def conformal_current_predictions(
    metrics: list[EpisodeMetrics],
    current_threshold: float,
) -> list[int]:
    preds = []
    for m in metrics:
        if abs(m.current_score) <= current_threshold:
            preds.append(0)
        elif m.current_score > 0:
            preds.append(1)
        else:
            preds.append(-1)
    return preds


def evaluate_conformal_current(
    metrics: list[EpisodeMetrics],
    current_threshold: float,
) -> dict[str, float]:
    preds = conformal_current_predictions(metrics, current_threshold)
    current_rows = [(p, m) for p, m in zip(preds, metrics) if m.has_current]
    null_rows = [(p, m) for p, m in zip(preds, metrics) if not m.has_current]
    admitted_rows = [(p, m) for p, m in current_rows if p != 0]
    return {
        "direction_accuracy": float(np.mean([p == m.true_direction for p, m in current_rows])),
        "current_detection": float(np.mean([p != 0 for p, _m in current_rows])),
        "conditional_direction_accuracy": float(
            np.mean([p == m.true_direction for p, m in admitted_rows])
        )
        if admitted_rows
        else float("nan"),
        "null_false_admission": float(np.mean([p != 0 for p, _m in null_rows])),
    }


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


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_direction": m.true_direction,
        "has_current": m.has_current,
        "forward_steps": m.forward_steps,
        "reverse_steps": m.reverse_steps,
        "stay_steps": m.stay_steps,
        "scalar_score": m.scalar_score,
        "symmetric_score": m.symmetric_score,
        "packet_unsigned_score": m.packet_unsigned_score,
        "current_score": m.current_score,
        "alpha_hat": m.alpha_hat,
        "beta_hat": m.beta_hat,
        "predictor_block": m.predictor_block,
    }


def classifier_dict(clf: ThresholdClassifier) -> dict[str, Any]:
    return {
        "score": clf.score,
        "threshold": clf.threshold,
        "high_label": clf.high_label,
        "train_accuracy": clf.train_accuracy,
    }


def summarize(
    calibration: list[EpisodeMetrics],
    metrics: list[EpisodeMetrics],
    alpha: float,
) -> tuple[dict[str, Any], dict[str, float]]:
    current_threshold = quantile(
        [abs(m.current_score) for m in calibration if m.kind == "null"],
        1.0 - alpha / 2.0,
    )
    thresholds = {
        "alpha": alpha,
        "current_abs_null_gate": current_threshold,
        "current_abs_null_quantile": 1.0 - alpha / 2.0,
    }

    direction_scores = {
        "scalar": "scalar_score",
        "symmetric": "symmetric_score",
        "unsigned_packet": "packet_unsigned_score",
        "current_signed": "current_score",
    }
    presence_scores = {
        "scalar": "scalar_score",
        "symmetric": "symmetric_score",
        "unsigned_packet": "packet_unsigned_score",
        "current_abs": "abs_current_score",
    }

    direction_classifiers = {
        agent: fit_binary_threshold_classifier(
            calibration,
            score=score,
            positive_label=1,
            negative_label=-1,
        )
        for agent, score in direction_scores.items()
    }
    presence_classifiers = {
        agent: fit_presence_threshold_classifier(calibration, score=score)
        for agent, score in presence_scores.items()
    }

    agent_summary: dict[str, Any] = {}
    for agent, clf in direction_classifiers.items():
        direction_eval = evaluate_direction_classifier(metrics, clf)
        if agent == "current_signed":
            presence_eval = evaluate_presence_classifier(metrics, presence_classifiers["current_abs"])
        else:
            presence_eval = evaluate_presence_classifier(metrics, presence_classifiers[agent])
        agent_summary[agent] = {
            **direction_eval,
            "current_detection": presence_eval["current_detection"],
            "null_false_admission": presence_eval["null_false_admission"],
        }

    conformal_eval = evaluate_conformal_current(metrics, current_threshold)
    agent_summary["t18_conformal_current"] = {
        "accuracy": conformal_eval["direction_accuracy"],
        "forward_accuracy": float(
            np.mean(
                [
                    p == m.true_direction
                    for p, m in zip(conformal_current_predictions(metrics, current_threshold), metrics)
                    if m.kind == "forward"
                ]
            )
        ),
        "reverse_accuracy": float(
            np.mean(
                [
                    p == m.true_direction
                    for p, m in zip(conformal_current_predictions(metrics, current_threshold), metrics)
                    if m.kind == "reverse"
                ]
            )
        ),
        "current_detection": conformal_eval["current_detection"],
        "null_false_admission": conformal_eval["null_false_admission"],
        "conditional_direction_accuracy": conformal_eval["conditional_direction_accuracy"],
    }

    current_presence_labels = [1 if m.has_current else 0 for m in metrics]
    direction_rows = [m for m in metrics if m.kind in {"forward", "reverse"}]
    direction_labels = [1 if m.kind == "forward" else 0 for m in direction_rows]
    summary = {
        "agents": agent_summary,
        "direction_classifiers": {k: classifier_dict(v) for k, v in direction_classifiers.items()},
        "presence_classifiers": {k: classifier_dict(v) for k, v in presence_classifiers.items()},
        "auc": {
            "scalar_current_presence": auc(current_presence_labels, [m.scalar_score for m in metrics]),
            "symmetric_current_presence": auc(current_presence_labels, [m.symmetric_score for m in metrics]),
            "unsigned_packet_current_presence": auc(
                current_presence_labels,
                [m.packet_unsigned_score for m in metrics],
            ),
            "current_abs_current_presence": auc(current_presence_labels, [abs(m.current_score) for m in metrics]),
            "scalar_forward_vs_reverse": auc(direction_labels, [m.scalar_score for m in direction_rows]),
            "symmetric_forward_vs_reverse": auc(direction_labels, [m.symmetric_score for m in direction_rows]),
            "unsigned_packet_forward_vs_reverse": auc(
                direction_labels,
                [m.packet_unsigned_score for m in direction_rows],
            ),
            "current_signed_forward_vs_reverse": auc(direction_labels, [m.current_score for m in direction_rows]),
        },
        "mean_scores_by_kind": {
            kind: {
                "scalar": float(np.mean([m.scalar_score for m in metrics if m.kind == kind])),
                "symmetric": float(np.mean([m.symmetric_score for m in metrics if m.kind == kind])),
                "unsigned_packet": float(np.mean([m.packet_unsigned_score for m in metrics if m.kind == kind])),
                "current_signed": float(np.mean([m.current_score for m in metrics if m.kind == kind])),
                "alpha_hat": float(np.mean([m.alpha_hat for m in metrics if m.kind == kind])),
                "beta_hat": float(np.mean([m.beta_hat for m in metrics if m.kind == kind])),
            }
            for kind in KINDS
        },
        "mean_step_counts_by_kind": {
            kind: {
                "forward_steps": float(np.mean([m.forward_steps for m in metrics if m.kind == kind])),
                "reverse_steps": float(np.mean([m.reverse_steps for m in metrics if m.kind == kind])),
                "stay_steps": float(np.mean([m.stay_steps for m in metrics if m.kind == kind])),
            }
            for kind in KINDS
        },
    }

    tolerance = 0.10
    pass_checks = {
        "scalar_direction_blind": abs(summary["agents"]["scalar"]["accuracy"] - 0.5) <= tolerance,
        "symmetric_direction_blind": abs(summary["agents"]["symmetric"]["accuracy"] - 0.5) <= tolerance,
        "unsigned_packet_direction_blind": abs(summary["agents"]["unsigned_packet"]["accuracy"] - 0.5) <= tolerance,
        "current_signed_recovers_arrow": summary["agents"]["current_signed"]["accuracy"] >= 0.95,
        "conformal_recovers_arrow": summary["agents"]["t18_conformal_current"]["accuracy"] >= 0.95,
        "conformal_false_current_controlled": summary["agents"]["t18_conformal_current"]["null_false_admission"] <= alpha,
    }
    summary["pass_checks"] = pass_checks
    summary["overall_pass"] = bool(all(pass_checks.values()))
    return summary, thresholds


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
    thresholds: dict[str, float],
    summary: dict[str, Any],
) -> None:
    agent_rows = []
    for agent, data in summary["agents"].items():
        agent_rows.append(
            [
                agent,
                fmt(data["accuracy"]),
                fmt(data["forward_accuracy"]),
                fmt(data["reverse_accuracy"]),
                fmt(data["current_detection"]),
                fmt(data["null_false_admission"]),
            ]
        )

    auc_rows = [[name, fmt(value)] for name, value in summary["auc"].items()]
    score_rows = []
    for kind, scores in summary["mean_scores_by_kind"].items():
        score_rows.append(
            [
                kind,
                fmt(scores["scalar"]),
                fmt(scores["symmetric"]),
                fmt(scores["unsigned_packet"]),
                fmt(scores["current_signed"]),
                fmt(scores["beta_hat"]),
            ]
        )

    count_rows = []
    for kind, counts in summary["mean_step_counts_by_kind"].items():
        count_rows.append(
            [
                kind,
                fmt(counts["forward_steps"]),
                fmt(counts["reverse_steps"]),
                fmt(counts["stay_steps"]),
            ]
        )

    direction_fit_rows = []
    for agent, clf in summary["direction_classifiers"].items():
        direction_fit_rows.append(
            [
                agent,
                clf["score"],
                fmt(clf["threshold"]),
                clf["high_label"],
                fmt(clf["train_accuracy"]),
            ]
        )

    pass_rows = [[name, "pass" if value else "fail"] for name, value in summary["pass_checks"].items()]
    overall = "PASS" if summary["overall_pass"] else "FAIL"

    text = f"""# B3 Time-Reversal Blindness Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- states: `{config['n_states']}`
- episode length: `{config['length']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration trials per kind: `{config['calibration_trials_per_kind']}`
- drift/counter/stay: `{config['drift_prob']}` / `{config['counter_prob']}` / `{config['stay_prob']}`
- alpha: `{config['alpha']}`

## Claim Tested

B3-E1 tests whether the current bucket is operationally distinct from scalar
surprise and symmetric boundary geometry. The forward, reverse, and null worlds
share a uniform stationary distribution and the same symmetrized transition
backbone. The only difference between forward and reverse is the sign of the
antisymmetric current.

## Conformal Current Gate

{md_table(['threshold', 'value'], [[k, fmt(v)] for k, v in thresholds.items()])}

## Agent Summary

{md_table(['agent', 'direction accuracy', 'forward acc', 'reverse acc', 'current detection', 'null false admission'], agent_rows)}

## Direction Classifier Fits

{md_table(['agent', 'score', 'threshold', 'high label', 'train accuracy'], direction_fit_rows)}

## AUC Checks

{md_table(['check', 'AUC'], auc_rows)}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'symmetric', 'unsigned packet', 'signed current', 'beta'], score_rows)}

## Mean Step Counts by Kind

{md_table(['kind', 'forward steps', 'reverse steps', 'stay steps'], count_rows)}

## Pass Checks

{md_table(['check', 'result'], pass_rows)}

Overall: **{overall}**

## Interpretation

This is a pass if scalar and symmetric agents remain near chance on
forward-versus-reverse direction, unsigned packet evidence detects that a
current exists but cannot name its arrow, signed current recovers the arrow,
and the conformal current gate keeps detailed-balance false admission below
alpha.

This would falsify the B-series current bucket if scalar surprise, symmetric
geometry, or unsigned packet magnitude recovered the time direction as well as
the signed current statistic under these matched-backbone controls.
"""
    path.write_text(text, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--n-states", type=int, default=17)
    parser.add_argument("--length", type=int, default=256)
    parser.add_argument("--trials-per-kind", type=int, default=600)
    parser.add_argument("--calibration-trials-per-kind", type=int, default=700)
    parser.add_argument("--drift-prob", type=float, default=0.56)
    parser.add_argument("--counter-prob", type=float, default=0.16)
    parser.add_argument("--stay-prob", type=float, default=0.28)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--report-dir", type=Path, default=Path("empirical/reports"))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if abs(args.drift_prob + args.counter_prob + args.stay_prob - 1.0) > 1e-9:
        raise ValueError("drift_prob + counter_prob + stay_prob must equal 1")
    if args.drift_prob <= args.counter_prob:
        raise ValueError("drift_prob must exceed counter_prob for a forward arrow")

    rng = np.random.default_rng(args.seed)
    calibration = [
        episode_metrics(
            kind,
            rng,
            n_states=args.n_states,
            length=args.length,
            drift_prob=args.drift_prob,
            counter_prob=args.counter_prob,
            stay_prob=args.stay_prob,
        )
        for kind in KINDS
        for _ in range(args.calibration_trials_per_kind)
    ]
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_states=args.n_states,
            length=args.length,
            drift_prob=args.drift_prob,
            counter_prob=args.counter_prob,
            stay_prob=args.stay_prob,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    summary, thresholds = summarize(calibration, metrics, args.alpha)

    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "n_states": args.n_states,
        "length": args.length,
        "trials_per_kind": args.trials_per_kind,
        "calibration_trials_per_kind": args.calibration_trials_per_kind,
        "drift_prob": args.drift_prob,
        "counter_prob": args.counter_prob,
        "stay_prob": args.stay_prob,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b3_time_reversal_blindness_probe.md"
    json_path = out_dir / "b3_time_reversal_blindness_probe.json"
    write_report(md_path, config, thresholds, summary)
    json_path.write_text(
        json.dumps(
            {
                "config": config,
                "thresholds": thresholds,
                "summary": summary,
                "metrics": [as_dict(m) for m in metrics],
                "calibration_metrics": [as_dict(m) for m in calibration],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(json.dumps(summary["agents"], indent=2))
    print(f"\nreport: {md_path}")
    print(f"json:   {json_path}")


if __name__ == "__main__":
    main()
