"""B5 active-sensing versus belief-revision probe.

This synthetic falsifier tests the B-series claim that an animal-like boundary
system should sometimes act to make an error decidable before revising belief.

The probe creates matched-surprise episodes whose true operations are:

    retained: update an existing belief weight;
    sample: request a cheap additional cue;
    act: move the sensor/viewpoint to disambiguate the cause;
    packet: add a missing interaction packet;
    noise: suppress.

The active episodes are adversarial: a naive in-context belief update looks
tempting on the training view, but does not generalize. The action feature is
the stable resolving evidence. The active bucket earns its keep only if it
selects action instead of premature belief revision.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["retained", "sample", "act", "packet", "noise"]
OPERATIONS = {
    "retained": "reweight",
    "sample": "sample",
    "act": "act",
    "packet": "close",
    "noise": "suppress",
}


@dataclass(frozen=True)
class FeatureBundle:
    belief: np.ndarray
    sample: np.ndarray
    action: np.ndarray
    packet: np.ndarray


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    scalar_surprise: float
    retained_train_gain: float
    retained_gain: float
    sample_gain: float
    sample_value: float
    action_gain: float
    action_value: float
    packet_gain: float
    premature_revision_risk: float
    action_over_belief: float
    sample_cost: float
    action_cost: float


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


def train_gain(feature: np.ndarray, residual: np.ndarray) -> float:
    coef = fit_coef(feature, residual)
    base = float(np.mean(residual**2))
    improved = float(np.mean((residual - coef * feature) ** 2))
    return base - improved


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


def make_features(rng: np.random.Generator, n: int) -> FeatureBundle:
    z = rng.normal(size=(n, 5))
    return FeatureBundle(
        belief=standardize(z[:, 0]),
        sample=standardize(z[:, 1]),
        action=standardize(z[:, 2]),
        packet=standardize(z[:, 3] * z[:, 4]),
    )


def make_signal(
    kind: str,
    features: FeatureBundle,
    rng: np.random.Generator,
    split: str,
) -> np.ndarray:
    if kind == "retained":
        signal = features.belief
    elif kind == "sample":
        signal = features.sample
    elif kind == "act":
        if split == "train":
            signal = standardize(0.58 * features.belief + features.action)
        else:
            signal = features.action
    elif kind == "packet":
        signal = features.packet
    elif kind == "noise":
        signal = rng.normal(size=len(features.belief))
    else:
        raise ValueError(f"unknown kind: {kind}")
    return standardize(signal)


def make_residual(
    kind: str,
    features: FeatureBundle,
    rng: np.random.Generator,
    split: str,
    noise_scale: float,
) -> np.ndarray:
    if kind == "noise":
        return standardize(rng.normal(size=len(features.belief)))
    signal = make_signal(kind, features, rng, split)
    return standardize(signal + rng.normal(scale=noise_scale, size=len(signal)))


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    noise_scale: float,
    sample_cost: float,
    action_cost: float,
) -> EpisodeMetrics:
    train_f = make_features(rng, n_train)
    test_f = make_features(rng, n_test)
    train_y = make_residual(kind, train_f, rng, "train", noise_scale)
    test_y = make_residual(kind, test_f, rng, "test", noise_scale)

    retained_train = train_gain(train_f.belief, train_y)
    retained = heldout_gain(train_f.belief, train_y, test_f.belief, test_y)
    sample = heldout_gain(train_f.sample, train_y, test_f.sample, test_y)
    action = heldout_gain(train_f.action, train_y, test_f.action, test_y)
    packet = heldout_gain(train_f.packet, train_y, test_f.packet, test_y)

    return EpisodeMetrics(
        kind=kind,
        true_operation=OPERATIONS[kind],
        scalar_surprise=float(np.mean(test_y**2)),
        retained_train_gain=float(retained_train),
        retained_gain=float(retained),
        sample_gain=float(sample),
        sample_value=float(sample - sample_cost),
        action_gain=float(action),
        action_value=float(action - action_cost),
        packet_gain=float(packet),
        premature_revision_risk=float(retained_train - retained),
        action_over_belief=float(action - retained),
        sample_cost=sample_cost,
        action_cost=action_cost,
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "scalar_surprise": m.scalar_surprise,
        "retained_train_gain": m.retained_train_gain,
        "retained_gain": m.retained_gain,
        "sample_gain": m.sample_gain,
        "sample_value": m.sample_value,
        "action_gain": m.action_gain,
        "action_value": m.action_value,
        "packet_gain": m.packet_gain,
        "premature_revision_risk": m.premature_revision_risk,
        "action_over_belief": m.action_over_belief,
        "sample_cost": m.sample_cost,
        "action_cost": m.action_cost,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def calibrate_thresholds(
    rng: np.random.Generator,
    n_calibration: int,
    n_train: int,
    n_test: int,
    noise_scale: float,
    sample_cost: float,
    action_cost: float,
    alpha: float,
) -> dict[str, float]:
    null = [
        episode_metrics("noise", rng, n_train, n_test, noise_scale, sample_cost, action_cost)
        for _ in range(n_calibration)
    ]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    retained_q = quantile([m.retained_gain for m in null], q)
    sample_value_q = quantile([m.sample_value for m in null], q)
    action_value_q = quantile([m.action_value for m in null], q)
    packet_q = quantile([m.packet_gain for m in null], q)
    route_margins = [
        max(
            m.retained_gain - retained_q,
            m.sample_value - sample_value_q,
            m.action_value - action_value_q,
            m.packet_gain - packet_q,
        )
        for m in null
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "retained_train": quantile([m.retained_train_gain for m in null], q),
        "retained": retained_q,
        "sample_value": sample_value_q,
        "action_value": action_value_q,
        "packet": packet_q,
        "family_margin": quantile(route_margins, family_q),
        "fixed_gain": 0.12,
        "fixed_sample_value": 0.10,
        "fixed_action_value": 0.10,
    }


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def naive_belief_revision_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["retained_train"] if conformal else thresholds["fixed_gain"]
    return "reweight" if m.retained_train_gain > threshold else "suppress"


def passive_bucket_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        sample_t = thresholds["sample_value"]
        packet_t = thresholds["packet"]
    else:
        retained_t = thresholds["fixed_gain"]
        sample_t = thresholds["fixed_sample_value"]
        packet_t = thresholds["fixed_gain"]
    candidates = [
        ("reweight", m.retained_gain - retained_t),
        ("sample", m.sample_value - sample_t),
        ("close", m.packet_gain - packet_t),
    ]
    operation, margin = max(candidates, key=lambda item: item[1])
    return operation if margin > 0.0 else "suppress"


def active_boundary_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        sample_t = thresholds["sample_value"]
        action_t = thresholds["action_value"]
        packet_t = thresholds["packet"]
        family_margin = thresholds["family_margin"]
    else:
        retained_t = thresholds["fixed_gain"]
        sample_t = thresholds["fixed_sample_value"]
        action_t = thresholds["fixed_action_value"]
        packet_t = thresholds["fixed_gain"]
        family_margin = 0.0
    candidates = [
        ("reweight", m.retained_gain - retained_t),
        ("sample", m.sample_value - sample_t),
        ("act", m.action_value - action_t),
        ("close", m.packet_gain - packet_t),
    ]
    operation, margin = max(candidates, key=lambda item: item[1])
    if conformal and margin <= family_margin:
        return "suppress"
    return operation if margin > 0.0 else "suppress"


def packet_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["packet"] if conformal else thresholds["fixed_gain"]
    return "close" if m.packet_gain > threshold else "suppress"


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


def summarize(metrics: list[EpisodeMetrics], predictions: dict[str, list[str]], alpha: float) -> dict[str, Any]:
    truth = [m.true_operation for m in metrics]
    summary: dict[str, Any] = {"agents": {}, "by_kind": {}, "auc": {}}
    for agent, preds in predictions.items():
        correct = [p == t for p, t in zip(preds, truth)]
        summary["agents"][agent] = {
            "routing_accuracy": float(np.mean(correct)),
            "noise_false_admission": float(
                np.mean([p != "suppress" for p, m in zip(preds, metrics) if m.kind == "noise"])
            ),
            "retained_success": float(
                np.mean([p == "reweight" for p, m in zip(preds, metrics) if m.kind == "retained"])
            ),
            "sample_success": float(
                np.mean([p == "sample" for p, m in zip(preds, metrics) if m.kind == "sample"])
            ),
            "act_success": float(
                np.mean([p == "act" for p, m in zip(preds, metrics) if m.kind == "act"])
            ),
            "packet_success": float(
                np.mean([p == "close" for p, m in zip(preds, metrics) if m.kind == "packet"])
            ),
            "act_as_belief_revision": float(
                np.mean([p == "reweight" for p, m in zip(preds, metrics) if m.kind == "act"])
            ),
        }

    for kind in KINDS:
        rows = [i for i, m in enumerate(metrics) if m.kind == kind]
        summary["by_kind"][kind] = {
            agent: float(np.mean([predictions[agent][i] == truth[i] for i in rows]))
            for agent in predictions
        }

    labels_non_noise = [0 if m.kind == "noise" else 1 for m in metrics]
    summary["auc"] = {
        "scalar_non_noise_vs_noise": auc(labels_non_noise, [m.scalar_surprise for m in metrics]),
        "retained_gain_retained_vs_noise": auc(
            [1 if m.kind == "retained" else 0 for m in metrics if m.kind in {"retained", "noise"}],
            [m.retained_gain for m in metrics if m.kind in {"retained", "noise"}],
        ),
        "sample_value_sample_vs_noise": auc(
            [1 if m.kind == "sample" else 0 for m in metrics if m.kind in {"sample", "noise"}],
            [m.sample_value for m in metrics if m.kind in {"sample", "noise"}],
        ),
        "action_value_act_vs_noise": auc(
            [1 if m.kind == "act" else 0 for m in metrics if m.kind in {"act", "noise"}],
            [m.action_value for m in metrics if m.kind in {"act", "noise"}],
        ),
        "packet_gain_packet_vs_noise": auc(
            [1 if m.kind == "packet" else 0 for m in metrics if m.kind in {"packet", "noise"}],
            [m.packet_gain for m in metrics if m.kind in {"packet", "noise"}],
        ),
        "train_belief_act_vs_noise": auc(
            [1 if m.kind == "act" else 0 for m in metrics if m.kind in {"act", "noise"}],
            [m.retained_train_gain for m in metrics if m.kind in {"act", "noise"}],
        ),
        "action_value_act_vs_retained": auc(
            [1 if m.kind == "act" else 0 for m in metrics if m.kind in {"act", "retained"}],
            [m.action_value for m in metrics if m.kind in {"act", "retained"}],
        ),
    }

    summary["mean_scores_by_kind"] = {
        kind: {
            "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
            "retained_train": float(np.mean([m.retained_train_gain for m in metrics if m.kind == kind])),
            "retained": float(np.mean([m.retained_gain for m in metrics if m.kind == kind])),
            "sample_value": float(np.mean([m.sample_value for m in metrics if m.kind == kind])),
            "action_value": float(np.mean([m.action_value for m in metrics if m.kind == kind])),
            "packet": float(np.mean([m.packet_gain for m in metrics if m.kind == kind])),
            "premature_revision_risk": float(
                np.mean([m.premature_revision_risk for m in metrics if m.kind == kind])
            ),
            "action_over_belief": float(np.mean([m.action_over_belief for m in metrics if m.kind == kind])),
        }
        for kind in KINDS
    }

    scalar_range = (
        max(v["scalar"] for v in summary["mean_scores_by_kind"].values())
        - min(v["scalar"] for v in summary["mean_scores_by_kind"].values())
    )
    summary["pass_checks"] = {
        "scalar_surprise_matched": scalar_range <= 0.01,
        "naive_belief_overupdates_action": (
            summary["agents"]["naive_belief_revision"]["act_as_belief_revision"] >= 0.85
        ),
        "passive_bucket_misses_action": summary["agents"]["passive_bucket"]["act_success"] <= 0.15,
        "active_boundary_recovers_action": summary["agents"]["active_boundary"]["act_success"] >= 0.95,
        "active_boundary_routes_core_cases": (
            summary["agents"]["active_boundary"]["retained_success"] >= 0.95
            and summary["agents"]["active_boundary"]["sample_success"] >= 0.95
            and summary["agents"]["active_boundary"]["packet_success"] >= 0.95
        ),
        "conformal_recovers_action": summary["agents"]["t18_conformal_active"]["act_success"] >= 0.90,
        "conformal_false_admission_controlled": (
            summary["agents"]["t18_conformal_active"]["noise_false_admission"] <= alpha
        ),
    }
    summary["overall_pass"] = bool(all(summary["pass_checks"].values()))
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
                fmt(data["retained_success"]),
                fmt(data["sample_success"]),
                fmt(data["act_success"]),
                fmt(data["packet_success"]),
                fmt(data["act_as_belief_revision"]),
            ]
        )

    by_kind_rows = []
    for kind, true_op in OPERATIONS.items():
        row = [kind, true_op]
        for agent in [
            "scalar",
            "naive_belief_revision",
            "packet_only_closure",
            "passive_bucket",
            "active_boundary",
            "t18_conformal_active",
        ]:
            row.append(fmt(summary["by_kind"][kind][agent]))
        by_kind_rows.append(row)

    score_rows = []
    for kind, scores in summary["mean_scores_by_kind"].items():
        score_rows.append(
            [
                kind,
                fmt(scores["scalar"]),
                fmt(scores["retained_train"]),
                fmt(scores["retained"]),
                fmt(scores["sample_value"]),
                fmt(scores["action_value"]),
                fmt(scores["packet"]),
                fmt(scores["premature_revision_risk"]),
            ]
        )

    pass_rows = [[name, "pass" if value else "fail"] for name, value in summary["pass_checks"].items()]
    overall = "PASS" if summary["overall_pass"] else "FAIL"

    text = f"""# B5 Active Sensing Versus Belief Revision Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration episodes: `{config['n_calibration']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- noise scale: `{config['noise_scale']}`
- sample/action cost: `{config['sample_cost']}` / `{config['action_cost']}`
- alpha: `{config['alpha']}`

## Claim Tested

B5-E1 asks whether an active boundary agent moves or samples before revising
belief when the current view is underdetermined. Active episodes are designed
so a naive belief update fits the training view, but only the action cue
generalizes.

## Conformal Null Thresholds

{md_table(['score', 'threshold'], [[k, fmt(v)] for k, v in thresholds.items()])}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'retained success', 'sample success', 'act success', 'packet success', 'act as belief revision'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'naive belief', 'packet only', 'passive bucket', 'active boundary', 'T18 conformal active'], by_kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'train belief', 'heldout belief', 'sample value', 'action value', 'packet', 'premature revision risk'], score_rows)}

## Pass Checks

{md_table(['check', 'result'], pass_rows)}

Overall: **{overall}**

## Interpretation

This is a pass if scalar surprise is matched, naive belief revision
over-updates active episodes, passive routing misses the action cases, and the
active routers choose action while keeping noise admission under conformal
control.

This would falsify the active-sensing bucket if belief revision generalized as
well as action on the active episodes, or if the passive bucket router solved
the action cases without an intervention channel.
"""
    path.write_text(text, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-kind", type=int, default=300)
    parser.add_argument("--n-calibration", type=int, default=900)
    parser.add_argument("--n-train", type=int, default=72)
    parser.add_argument("--n-test", type=int, default=72)
    parser.add_argument("--noise-scale", type=float, default=0.35)
    parser.add_argument("--sample-cost", type=float, default=0.06)
    parser.add_argument("--action-cost", type=float, default=0.18)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--report-dir", type=Path, default=Path("empirical/reports"))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    rng = np.random.default_rng(args.seed)
    thresholds = calibrate_thresholds(
        rng,
        n_calibration=args.n_calibration,
        n_train=args.n_train,
        n_test=args.n_test,
        noise_scale=args.noise_scale,
        sample_cost=args.sample_cost,
        action_cost=args.action_cost,
        alpha=args.alpha,
    )
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            noise_scale=args.noise_scale,
            sample_cost=args.sample_cost,
            action_cost=args.action_cost,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    predictions = {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "naive_belief_revision": [
            naive_belief_revision_agent(m, thresholds, conformal=False) for m in metrics
        ],
        "packet_only_closure": [packet_only_agent(m, thresholds, conformal=False) for m in metrics],
        "passive_bucket": [passive_bucket_agent(m, thresholds, conformal=False) for m in metrics],
        "active_boundary": [active_boundary_agent(m, thresholds, conformal=False) for m in metrics],
        "t18_conformal_active": [active_boundary_agent(m, thresholds, conformal=True) for m in metrics],
    }
    summary = summarize(metrics, predictions, args.alpha)

    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "trials_per_kind": args.trials_per_kind,
        "n_calibration": args.n_calibration,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "noise_scale": args.noise_scale,
        "sample_cost": args.sample_cost,
        "action_cost": args.action_cost,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b5_active_sensing_vs_belief_revision_probe.md"
    json_path = out_dir / "b5_active_sensing_vs_belief_revision_probe.json"
    write_report(md_path, config, thresholds, summary)
    json_path.write_text(
        json.dumps(
            {
                "config": config,
                "thresholds": thresholds,
                "summary": summary,
                "metrics": [as_dict(m) for m in metrics],
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
