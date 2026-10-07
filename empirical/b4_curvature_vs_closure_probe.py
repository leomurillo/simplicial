"""B4 curvature-versus-closure probe.

This synthetic falsifier targets the second Conductor Blind Spot ingredient
imported into the B-series: curvature.

The test asks whether a prediction-error router can distinguish two failure
modes that have the same scalar residual energy:

    1. chart error: the latent coordinate is already present, but read through
       the wrong nonlinear chart;
    2. packet error: the residual needs a genuine cross-coordinate interaction.

A packet-only closure rule is intentionally tempted by chart episodes because a
self-packet can explain much of a nonlinear one-coordinate warp. The bucket
router earns its keep only if it routes that case to rechart, while sending true
cross-coordinate interactions to closure and keeping noise under conformal
control.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["retained", "chart", "packet", "noise"]
OPERATIONS = {
    "retained": "reweight",
    "chart": "rechart",
    "packet": "close",
    "noise": "suppress",
}


@dataclass(frozen=True)
class FeatureBundle:
    linear: np.ndarray
    chart_blocks: dict[str, np.ndarray]
    packet_features: dict[str, np.ndarray]
    self_packet_names: list[str]
    cross_packet_names: list[str]


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    scalar_surprise: float
    retained_gain: float
    chart_gain: float
    second_chart_gain: float
    best_chart: str
    all_packet_gain: float
    self_packet_gain: float
    cross_packet_gain: float
    second_cross_packet_gain: float
    best_all_packet: str
    best_self_packet: str
    best_cross_packet: str
    chart_over_cross: float
    self_over_cross: float


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = float(np.std(x))
    if sd < 1e-12:
        return np.zeros_like(x)
    return (x - float(np.mean(x))) / sd


def standardize_columns(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    cols = [standardize(x[:, j]) for j in range(x.shape[1])]
    return np.column_stack(cols)


def ridge_heldout_gain(
    train_x: np.ndarray,
    train_y: np.ndarray,
    test_x: np.ndarray,
    test_y: np.ndarray,
    lam: float,
) -> float:
    train_x = np.asarray(train_x, dtype=float)
    test_x = np.asarray(test_x, dtype=float)
    if train_x.ndim == 1:
        train_x = train_x[:, None]
    if test_x.ndim == 1:
        test_x = test_x[:, None]
    gram = train_x.T @ train_x
    rhs = train_x.T @ train_y
    reg = gram + lam * np.eye(gram.shape[0])
    try:
        coef = np.linalg.solve(reg, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(reg) @ rhs
    base = float(np.mean(test_y**2))
    improved = float(np.mean((test_y - test_x @ coef) ** 2))
    return base - improved


def make_features(rng: np.random.Generator, n: int, n_latent: int) -> FeatureBundle:
    z = rng.normal(size=(n, n_latent))
    linear = standardize_columns(z)

    chart_blocks = {}
    for j in range(n_latent):
        x = z[:, j]
        block = np.column_stack(
            [
                x**2 - 1.0,
                np.cos(1.7 * x),
                x**4 - 3.0,
            ]
        )
        chart_blocks[f"x{j}"] = standardize_columns(block)

    packet_features = {}
    self_packet_names = []
    cross_packet_names = []
    for i in range(n_latent):
        for j in range(i, n_latent):
            name = f"x{i}*x{j}"
            packet_features[name] = standardize(z[:, i] * z[:, j])
            if i == j:
                self_packet_names.append(name)
            else:
                cross_packet_names.append(name)

    return FeatureBundle(
        linear=linear,
        chart_blocks=chart_blocks,
        packet_features=packet_features,
        self_packet_names=self_packet_names,
        cross_packet_names=cross_packet_names,
    )


def make_signal(kind: str, features: FeatureBundle, rng: np.random.Generator) -> np.ndarray:
    if kind == "retained":
        signal = features.linear[:, 0]
    elif kind == "chart":
        block = features.chart_blocks["x0"]
        signal = standardize(0.72 * block[:, 0] + 0.52 * block[:, 1] + 0.18 * block[:, 2])
    elif kind == "packet":
        signal = features.packet_features["x0*x1"]
    elif kind == "noise":
        signal = rng.normal(size=features.linear.shape[0])
    else:
        raise ValueError(f"unknown kind: {kind}")
    return standardize(signal)


def make_residual(
    kind: str,
    features: FeatureBundle,
    rng: np.random.Generator,
    noise_scale: float,
) -> np.ndarray:
    if kind == "noise":
        return standardize(rng.normal(size=features.linear.shape[0]))
    signal = make_signal(kind, features, rng)
    return standardize(signal + rng.normal(scale=noise_scale, size=features.linear.shape[0]))


def best_gain(items: list[tuple[str, float]]) -> tuple[str, float, float]:
    ordered = sorted(items, key=lambda item: item[1], reverse=True)
    best_name, best_value = ordered[0]
    second_value = ordered[1][1] if len(ordered) > 1 else float("-inf")
    return best_name, float(best_value), float(second_value)


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    n_latent: int,
    noise_scale: float,
    ridge_lambda: float,
) -> EpisodeMetrics:
    train_f = make_features(rng, n_train, n_latent)
    test_f = make_features(rng, n_test, n_latent)
    train_y = make_residual(kind, train_f, rng, noise_scale)
    test_y = make_residual(kind, test_f, rng, noise_scale)

    retained_gain = ridge_heldout_gain(train_f.linear, train_y, test_f.linear, test_y, ridge_lambda)
    chart_items = [
        (
            name,
            ridge_heldout_gain(block, train_y, test_f.chart_blocks[name], test_y, ridge_lambda),
        )
        for name, block in train_f.chart_blocks.items()
    ]
    packet_items = [
        (
            name,
            ridge_heldout_gain(feature, train_y, test_f.packet_features[name], test_y, ridge_lambda),
        )
        for name, feature in train_f.packet_features.items()
    ]
    self_items = [(name, gain) for name, gain in packet_items if name in train_f.self_packet_names]
    cross_items = [(name, gain) for name, gain in packet_items if name in train_f.cross_packet_names]

    best_chart, chart_gain, second_chart_gain = best_gain(chart_items)
    best_all_packet, all_packet_gain, _second_all_packet = best_gain(packet_items)
    best_self_packet, self_packet_gain, _second_self_packet = best_gain(self_items)
    best_cross_packet, cross_packet_gain, second_cross_packet_gain = best_gain(cross_items)

    return EpisodeMetrics(
        kind=kind,
        true_operation=OPERATIONS[kind],
        scalar_surprise=float(np.mean(test_y**2)),
        retained_gain=float(retained_gain),
        chart_gain=float(chart_gain),
        second_chart_gain=float(second_chart_gain),
        best_chart=best_chart,
        all_packet_gain=float(all_packet_gain),
        self_packet_gain=float(self_packet_gain),
        cross_packet_gain=float(cross_packet_gain),
        second_cross_packet_gain=float(second_cross_packet_gain),
        best_all_packet=best_all_packet,
        best_self_packet=best_self_packet,
        best_cross_packet=best_cross_packet,
        chart_over_cross=float(chart_gain - cross_packet_gain),
        self_over_cross=float(self_packet_gain - cross_packet_gain),
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "scalar_surprise": m.scalar_surprise,
        "retained_gain": m.retained_gain,
        "chart_gain": m.chart_gain,
        "second_chart_gain": m.second_chart_gain,
        "best_chart": m.best_chart,
        "all_packet_gain": m.all_packet_gain,
        "self_packet_gain": m.self_packet_gain,
        "cross_packet_gain": m.cross_packet_gain,
        "second_cross_packet_gain": m.second_cross_packet_gain,
        "best_all_packet": m.best_all_packet,
        "best_self_packet": m.best_self_packet,
        "best_cross_packet": m.best_cross_packet,
        "chart_over_cross": m.chart_over_cross,
        "self_over_cross": m.self_over_cross,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def calibrate_thresholds(
    rng: np.random.Generator,
    n_calibration: int,
    n_train: int,
    n_test: int,
    n_latent: int,
    noise_scale: float,
    ridge_lambda: float,
    alpha: float,
) -> dict[str, float]:
    null = [
        episode_metrics("noise", rng, n_train, n_test, n_latent, noise_scale, ridge_lambda)
        for _ in range(n_calibration)
    ]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    retained_q = quantile([m.retained_gain for m in null], q)
    chart_q = quantile([m.chart_gain for m in null], q)
    all_packet_q = quantile([m.all_packet_gain for m in null], q)
    cross_packet_q = quantile([m.cross_packet_gain for m in null], q)
    route_scores = [
        max(m.retained_gain, m.chart_gain, m.cross_packet_gain)
        for m in null
    ]
    route_q = quantile(route_scores, q)
    gate_scores = [
        max(
            m.retained_gain / max(retained_q, 1e-12),
            m.chart_gain / max(chart_q, 1e-12),
            m.cross_packet_gain / max(cross_packet_q, 1e-12),
            max(m.retained_gain, m.chart_gain, m.cross_packet_gain) / max(route_q, 1e-12),
        )
        for m in null
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "retained": retained_q,
        "chart": chart_q,
        "all_packet": all_packet_q,
        "cross_packet": cross_packet_q,
        "route": route_q,
        "family_gate": quantile(gate_scores, family_q),
        "fixed_gain": 0.12,
    }


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def retained_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["retained"] if conformal else thresholds["fixed_gain"]
    return "reweight" if m.retained_gain > threshold else "suppress"


def chart_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["chart"] if conformal else thresholds["fixed_gain"]
    return "rechart" if m.chart_gain > threshold else "suppress"


def packet_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["all_packet"] if conformal else thresholds["fixed_gain"]
    return "close" if m.all_packet_gain > threshold else "suppress"


def bucket_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        chart_t = thresholds["chart"]
        cross_packet_t = thresholds["cross_packet"]
        route_t = thresholds["route"]
        family_gate_t = thresholds["family_gate"]
    else:
        retained_t = thresholds["fixed_gain"]
        chart_t = thresholds["fixed_gain"]
        cross_packet_t = thresholds["fixed_gain"]
        route_t = thresholds["fixed_gain"]
        family_gate_t = 1.0

    route_score = max(m.retained_gain, m.chart_gain, m.cross_packet_gain)
    family_gate_score = max(
        m.retained_gain / max(retained_t, 1e-12),
        m.chart_gain / max(chart_t, 1e-12),
        m.cross_packet_gain / max(cross_packet_t, 1e-12),
        route_score / max(route_t, 1e-12),
    )
    if conformal and family_gate_score <= family_gate_t:
        return "suppress"

    if (
        m.retained_gain > retained_t
        and m.retained_gain >= m.chart_gain
        and m.retained_gain >= m.cross_packet_gain
    ):
        return "reweight"
    if (
        m.chart_gain > chart_t
        and m.chart_gain >= m.cross_packet_gain
        and m.best_all_packet == m.best_self_packet
    ):
        return "rechart"
    if m.cross_packet_gain > cross_packet_t:
        return "close"
    if m.chart_gain > chart_t:
        return "rechart"
    if m.retained_gain > retained_t:
        return "reweight"
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
            "chart_success": float(
                np.mean([p == "rechart" for p, m in zip(preds, metrics) if m.kind == "chart"])
            ),
            "packet_success": float(
                np.mean([p == "close" for p, m in zip(preds, metrics) if m.kind == "packet"])
            ),
            "chart_as_fake_closure": float(
                np.mean([p == "close" for p, m in zip(preds, metrics) if m.kind == "chart"])
            ),
        }

    for kind in KINDS:
        rows = [i for i, m in enumerate(metrics) if m.kind == kind]
        summary["by_kind"][kind] = {
            agent: float(np.mean([predictions[agent][i] == truth[i] for i in rows]))
            for agent in predictions
        }

    labels_non_noise = [0 if m.kind == "noise" else 1 for m in metrics]
    chart_or_packet = [m for m in metrics if m.kind in {"chart", "packet"}]
    chart_labels = [1 if m.kind == "chart" else 0 for m in chart_or_packet]
    packet_labels = [1 if m.kind == "packet" else 0 for m in chart_or_packet]
    summary["auc"] = {
        "scalar_non_noise_vs_noise": auc(labels_non_noise, [m.scalar_surprise for m in metrics]),
        "retained_gain_retained_vs_noise": auc(
            [1 if m.kind == "retained" else 0 for m in metrics if m.kind in {"retained", "noise"}],
            [m.retained_gain for m in metrics if m.kind in {"retained", "noise"}],
        ),
        "chart_gain_chart_vs_noise": auc(
            [1 if m.kind == "chart" else 0 for m in metrics if m.kind in {"chart", "noise"}],
            [m.chart_gain for m in metrics if m.kind in {"chart", "noise"}],
        ),
        "cross_packet_gain_packet_vs_noise": auc(
            [1 if m.kind == "packet" else 0 for m in metrics if m.kind in {"packet", "noise"}],
            [m.cross_packet_gain for m in metrics if m.kind in {"packet", "noise"}],
        ),
        "chart_gain_chart_vs_packet": auc(chart_labels, [m.chart_gain for m in chart_or_packet]),
        "cross_packet_gain_packet_vs_chart": auc(packet_labels, [m.cross_packet_gain for m in chart_or_packet]),
        "all_packet_gain_chart_or_packet_vs_noise": auc(
            [1 if m.kind in {"chart", "packet"} else 0 for m in metrics if m.kind in {"chart", "packet", "noise"}],
            [m.all_packet_gain for m in metrics if m.kind in {"chart", "packet", "noise"}],
        ),
    }

    summary["mean_scores_by_kind"] = {
        kind: {
            "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
            "retained": float(np.mean([m.retained_gain for m in metrics if m.kind == kind])),
            "chart": float(np.mean([m.chart_gain for m in metrics if m.kind == kind])),
            "all_packet": float(np.mean([m.all_packet_gain for m in metrics if m.kind == kind])),
            "self_packet": float(np.mean([m.self_packet_gain for m in metrics if m.kind == kind])),
            "cross_packet": float(np.mean([m.cross_packet_gain for m in metrics if m.kind == kind])),
            "chart_over_cross": float(np.mean([m.chart_over_cross for m in metrics if m.kind == kind])),
        }
        for kind in KINDS
    }

    summary["pass_checks"] = {
        "scalar_surprise_matched": (
            max(v["scalar"] for v in summary["mean_scores_by_kind"].values())
            - min(v["scalar"] for v in summary["mean_scores_by_kind"].values())
        )
        <= 0.01,
        "scalar_fails_routing": summary["agents"]["scalar"]["routing_accuracy"] <= 0.35,
        "packet_only_overcloses_chart": summary["agents"]["packet_only_closure"]["chart_as_fake_closure"] >= 0.85,
        "chart_only_fails_packet": summary["agents"]["chart_only_reparameterizer"]["packet_success"] <= 0.15,
        "post_cbs_separates_chart_packet": (
            summary["agents"]["post_cbs_bucket"]["chart_success"] >= 0.95
            and summary["agents"]["post_cbs_bucket"]["packet_success"] >= 0.95
        ),
        "conformal_separates_chart_packet": (
            summary["agents"]["t18_conformal_bucket"]["chart_success"] >= 0.90
            and summary["agents"]["t18_conformal_bucket"]["packet_success"] >= 0.90
        ),
        "conformal_false_admission_controlled": (
            summary["agents"]["t18_conformal_bucket"]["noise_false_admission"] <= alpha
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
                fmt(data["chart_success"]),
                fmt(data["packet_success"]),
                fmt(data["chart_as_fake_closure"]),
            ]
        )

    by_kind_rows = []
    for kind, true_op in OPERATIONS.items():
        row = [kind, true_op]
        for agent in [
            "scalar",
            "retained_only",
            "chart_only_reparameterizer",
            "packet_only_closure",
            "post_cbs_bucket",
            "t18_conformal_bucket",
        ]:
            row.append(fmt(summary["by_kind"][kind][agent]))
        by_kind_rows.append(row)

    score_rows = []
    for kind, scores in summary["mean_scores_by_kind"].items():
        score_rows.append(
            [
                kind,
                fmt(scores["scalar"]),
                fmt(scores["retained"]),
                fmt(scores["chart"]),
                fmt(scores["all_packet"]),
                fmt(scores["self_packet"]),
                fmt(scores["cross_packet"]),
                fmt(scores["chart_over_cross"]),
            ]
        )

    pass_rows = [[name, "pass" if value else "fail"] for name, value in summary["pass_checks"].items()]
    overall = "PASS" if summary["overall_pass"] else "FAIL"

    text = f"""# B4 Curvature Versus Closure Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration episodes: `{config['n_calibration']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- latent coordinates: `{config['n_latent']}`
- noise scale: `{config['noise_scale']}`
- alpha: `{config['alpha']}`

## Claim Tested

B4-E1 asks whether a brain-like prediction-error router distinguishes a bad
chart from a missing packet. Chart episodes are one-coordinate nonlinear warps.
Packet episodes are true cross-coordinate interactions. Scalar residual energy
is matched by construction.

## Conformal Null Thresholds

{md_table(['score', 'threshold'], [[k, fmt(v)] for k, v in thresholds.items()])}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'retained success', 'chart success', 'packet success', 'chart as fake closure'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'retained only', 'chart only', 'packet only', 'post-CBS bucket', 'T18 conformal bucket'], by_kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'retained', 'chart', 'all packet', 'self packet', 'cross packet', 'chart minus cross'], score_rows)}

## Pass Checks

{md_table(['check', 'result'], pass_rows)}

Overall: **{overall}**

## Interpretation

This is a pass if scalar surprise stays matched, packet-only closure mistakes
chart curvature for a fake packet, chart-only routing fails true packets, and
the bucket routers separate rechart from close while T18 conformal gating keeps
noise admission below alpha.

This would falsify the curvature bucket if closure alone separated the cases,
or if chart and packet evidence collapsed under matched surprise.
"""
    path.write_text(text, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-kind", type=int, default=260)
    parser.add_argument("--n-calibration", type=int, default=900)
    parser.add_argument("--n-train", type=int, default=72)
    parser.add_argument("--n-test", type=int, default=72)
    parser.add_argument("--n-latent", type=int, default=6)
    parser.add_argument("--noise-scale", type=float, default=0.35)
    parser.add_argument("--ridge-lambda", type=float, default=1e-3)
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
        n_latent=args.n_latent,
        noise_scale=args.noise_scale,
        ridge_lambda=args.ridge_lambda,
        alpha=args.alpha,
    )
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            n_latent=args.n_latent,
            noise_scale=args.noise_scale,
            ridge_lambda=args.ridge_lambda,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    predictions = {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "retained_only": [retained_only_agent(m, thresholds, conformal=False) for m in metrics],
        "chart_only_reparameterizer": [chart_only_agent(m, thresholds, conformal=False) for m in metrics],
        "packet_only_closure": [packet_only_agent(m, thresholds, conformal=False) for m in metrics],
        "post_cbs_bucket": [bucket_agent(m, thresholds, conformal=False) for m in metrics],
        "t18_conformal_bucket": [bucket_agent(m, thresholds, conformal=True) for m in metrics],
    }
    summary = summarize(metrics, predictions, args.alpha)

    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "trials_per_kind": args.trials_per_kind,
        "n_calibration": args.n_calibration,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "n_latent": args.n_latent,
        "noise_scale": args.noise_scale,
        "ridge_lambda": args.ridge_lambda,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b4_curvature_vs_closure_probe.md"
    json_path = out_dir / "b4_curvature_vs_closure_probe.json"
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
