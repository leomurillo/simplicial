"""B6 tool-use versus internal-compression probe.

This synthetic falsifier tests a capacity boundary in the B-series brain
hypothesis:

    some prediction errors should be externalized to a tool or memory aid
    instead of being compressed into the internal model.

The probe creates matched-surprise episodes:

    retained: a simple belief weight should be updated;
    compress: a low-rank structure should be internalized;
    tool: an exact high-cardinality lookup should be externalized;
    noise: no stable structure should be admitted.

The tool episodes are deliberately tempting for an internal key-memory rule:
memorizing the lookup table explains the data, but the required capacity is
large. A capacity-aware boundary agent should prefer an external tool because
the tool value beats the internal memory value after costs.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["retained", "compress", "tool", "noise"]
OPERATIONS = {
    "retained": "reweight",
    "compress": "compress",
    "tool": "externalize",
    "noise": "suppress",
}


@dataclass(frozen=True)
class FeatureBundle:
    belief: np.ndarray
    compression: np.ndarray
    keys: np.ndarray
    key_onehot: np.ndarray
    tool: np.ndarray


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    scalar_surprise: float
    retained_gain: float
    compression_gain: float
    compression_value: float
    key_memory_train_gain: float
    key_memory_gain: float
    key_memory_value: float
    tool_gain: float
    tool_value: float
    tool_over_memory: float
    tool_over_compression: float
    memory_capacity_cost: float
    compression_cost: float
    tool_cost: float


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = float(np.std(x))
    if sd < 1e-12:
        return np.zeros_like(x)
    return (x - float(np.mean(x))) / sd


def standardize_columns(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return np.column_stack([standardize(x[:, j]) for j in range(x.shape[1])])


def fit_coef(feature: np.ndarray, residual: np.ndarray, lam: float) -> np.ndarray:
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


def train_gain(feature: np.ndarray, residual: np.ndarray, lam: float) -> float:
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
    lam: float,
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


def make_features(
    rng: np.random.Generator,
    n: int,
    n_keys: int,
    tool_table: np.ndarray,
) -> FeatureBundle:
    z = rng.normal(size=(n, 5))
    keys = rng.integers(0, n_keys, size=n)
    compression = np.column_stack(
        [
            z[:, 1],
            z[:, 2],
            np.sin(z[:, 1] - 0.4 * z[:, 2]),
            z[:, 3] * z[:, 4],
        ]
    )
    return FeatureBundle(
        belief=standardize(z[:, 0]),
        compression=standardize_columns(compression),
        keys=keys,
        key_onehot=onehot(keys, n_keys),
        tool=tool_table[keys],
    )


def make_signal(
    kind: str,
    features: FeatureBundle,
    rng: np.random.Generator,
) -> np.ndarray:
    if kind == "retained":
        signal = features.belief
    elif kind == "compress":
        c = features.compression
        signal = 0.58 * c[:, 0] - 0.34 * c[:, 1] + 0.28 * c[:, 2] + 0.22 * c[:, 3]
    elif kind == "tool":
        signal = features.tool
    elif kind == "noise":
        signal = rng.normal(size=len(features.belief))
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
        return standardize(rng.normal(size=len(features.belief)))
    signal = make_signal(kind, features, rng)
    return standardize(signal + rng.normal(scale=noise_scale, size=len(signal)))


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    n_keys: int,
    noise_scale: float,
    ridge_lambda: float,
    compression_cost: float,
    memory_capacity_cost: float,
    tool_cost: float,
) -> EpisodeMetrics:
    tool_table = standardize(rng.normal(size=n_keys))
    train_f = make_features(rng, n_train, n_keys, tool_table)
    test_f = make_features(rng, n_test, n_keys, tool_table)
    train_y = make_residual(kind, train_f, rng, noise_scale)
    test_y = make_residual(kind, test_f, rng, noise_scale)

    retained_gain = heldout_gain(train_f.belief, train_y, test_f.belief, test_y, ridge_lambda)
    compression_gain = heldout_gain(
        train_f.compression,
        train_y,
        test_f.compression,
        test_y,
        ridge_lambda,
    )
    key_memory_train_gain = train_gain(train_f.key_onehot, train_y, ridge_lambda)
    key_memory_gain = heldout_gain(
        train_f.key_onehot,
        train_y,
        test_f.key_onehot,
        test_y,
        ridge_lambda,
    )
    tool_gain = heldout_gain(train_f.tool, train_y, test_f.tool, test_y, ridge_lambda)

    compression_value = compression_gain - compression_cost
    key_memory_value = key_memory_gain - memory_capacity_cost
    tool_value = tool_gain - tool_cost

    return EpisodeMetrics(
        kind=kind,
        true_operation=OPERATIONS[kind],
        scalar_surprise=float(np.mean(test_y**2)),
        retained_gain=float(retained_gain),
        compression_gain=float(compression_gain),
        compression_value=float(compression_value),
        key_memory_train_gain=float(key_memory_train_gain),
        key_memory_gain=float(key_memory_gain),
        key_memory_value=float(key_memory_value),
        tool_gain=float(tool_gain),
        tool_value=float(tool_value),
        tool_over_memory=float(tool_value - key_memory_value),
        tool_over_compression=float(tool_value - compression_value),
        memory_capacity_cost=memory_capacity_cost,
        compression_cost=compression_cost,
        tool_cost=tool_cost,
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "scalar_surprise": m.scalar_surprise,
        "retained_gain": m.retained_gain,
        "compression_gain": m.compression_gain,
        "compression_value": m.compression_value,
        "key_memory_train_gain": m.key_memory_train_gain,
        "key_memory_gain": m.key_memory_gain,
        "key_memory_value": m.key_memory_value,
        "tool_gain": m.tool_gain,
        "tool_value": m.tool_value,
        "tool_over_memory": m.tool_over_memory,
        "tool_over_compression": m.tool_over_compression,
        "memory_capacity_cost": m.memory_capacity_cost,
        "compression_cost": m.compression_cost,
        "tool_cost": m.tool_cost,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def calibrate_thresholds(
    rng: np.random.Generator,
    n_calibration: int,
    n_train: int,
    n_test: int,
    n_keys: int,
    noise_scale: float,
    ridge_lambda: float,
    compression_cost: float,
    memory_capacity_cost: float,
    tool_cost: float,
    alpha: float,
) -> dict[str, float]:
    null = [
        episode_metrics(
            "noise",
            rng,
            n_train,
            n_test,
            n_keys,
            noise_scale,
            ridge_lambda,
            compression_cost,
            memory_capacity_cost,
            tool_cost,
        )
        for _ in range(n_calibration)
    ]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    retained_q = quantile([m.retained_gain for m in null], q)
    compression_value_q = quantile([m.compression_value for m in null], q)
    key_memory_gain_q = quantile([m.key_memory_gain for m in null], q)
    tool_value_q = quantile([m.tool_value for m in null], q)
    route_margins = [
        max(
            m.retained_gain - retained_q,
            m.compression_value - compression_value_q,
            m.tool_value - tool_value_q,
        )
        for m in null
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "retained": retained_q,
        "compression_value": compression_value_q,
        "key_memory_gain": key_memory_gain_q,
        "tool_value": tool_value_q,
        "family_margin": quantile(route_margins, family_q),
        "fixed_gain": 0.12,
        "fixed_compression_value": 0.08,
        "fixed_memory_gain": 0.45,
        "fixed_tool_value": 0.08,
    }


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def compression_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["compression_value"] if conformal else thresholds["fixed_compression_value"]
    return "compress" if m.compression_value > threshold else "suppress"


def naive_internal_memory_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    memory_t = thresholds["key_memory_gain"] if conformal else thresholds["fixed_memory_gain"]
    compression_t = thresholds["compression_value"] if conformal else thresholds["fixed_compression_value"]
    if m.key_memory_gain > memory_t or m.compression_value > compression_t:
        return "compress"
    return "suppress"


def tool_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["tool_value"] if conformal else thresholds["fixed_tool_value"]
    return "externalize" if m.tool_value > threshold else "suppress"


def capacity_boundary_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        compression_t = thresholds["compression_value"]
        tool_t = thresholds["tool_value"]
        family_margin = thresholds["family_margin"]
    else:
        retained_t = thresholds["fixed_gain"]
        compression_t = thresholds["fixed_compression_value"]
        tool_t = thresholds["fixed_tool_value"]
        family_margin = 0.0

    candidates = [
        ("reweight", m.retained_gain - retained_t),
        ("compress", m.compression_value - compression_t),
        ("externalize", m.tool_value - tool_t),
    ]
    operation, margin = max(candidates, key=lambda item: item[1])
    if conformal and margin <= family_margin:
        return "suppress"
    return operation if margin > 0.0 else "suppress"


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
            "compress_success": float(
                np.mean([p == "compress" for p, m in zip(preds, metrics) if m.kind == "compress"])
            ),
            "tool_success": float(
                np.mean([p == "externalize" for p, m in zip(preds, metrics) if m.kind == "tool"])
            ),
            "tool_as_internal_compression": float(
                np.mean([p == "compress" for p, m in zip(preds, metrics) if m.kind == "tool"])
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
        "compression_value_compress_vs_noise": auc(
            [1 if m.kind == "compress" else 0 for m in metrics if m.kind in {"compress", "noise"}],
            [m.compression_value for m in metrics if m.kind in {"compress", "noise"}],
        ),
        "tool_value_tool_vs_noise": auc(
            [1 if m.kind == "tool" else 0 for m in metrics if m.kind in {"tool", "noise"}],
            [m.tool_value for m in metrics if m.kind in {"tool", "noise"}],
        ),
        "key_memory_gain_tool_vs_noise": auc(
            [1 if m.kind == "tool" else 0 for m in metrics if m.kind in {"tool", "noise"}],
            [m.key_memory_gain for m in metrics if m.kind in {"tool", "noise"}],
        ),
        "tool_value_tool_vs_compress": auc(
            [1 if m.kind == "tool" else 0 for m in metrics if m.kind in {"tool", "compress"}],
            [m.tool_value for m in metrics if m.kind in {"tool", "compress"}],
        ),
        "compression_value_compress_vs_tool": auc(
            [1 if m.kind == "compress" else 0 for m in metrics if m.kind in {"compress", "tool"}],
            [m.compression_value for m in metrics if m.kind in {"compress", "tool"}],
        ),
    }

    summary["mean_scores_by_kind"] = {
        kind: {
            "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
            "retained": float(np.mean([m.retained_gain for m in metrics if m.kind == kind])),
            "compression_value": float(np.mean([m.compression_value for m in metrics if m.kind == kind])),
            "key_memory_gain": float(np.mean([m.key_memory_gain for m in metrics if m.kind == kind])),
            "key_memory_value": float(np.mean([m.key_memory_value for m in metrics if m.kind == kind])),
            "tool_value": float(np.mean([m.tool_value for m in metrics if m.kind == kind])),
            "tool_over_memory": float(np.mean([m.tool_over_memory for m in metrics if m.kind == kind])),
            "tool_over_compression": float(np.mean([m.tool_over_compression for m in metrics if m.kind == kind])),
        }
        for kind in KINDS
    }

    scalar_range = (
        max(v["scalar"] for v in summary["mean_scores_by_kind"].values())
        - min(v["scalar"] for v in summary["mean_scores_by_kind"].values())
    )
    summary["pass_checks"] = {
        "scalar_surprise_matched": scalar_range <= 0.01,
        "compression_only_fails_tool": summary["agents"]["compression_only"]["tool_success"] <= 0.15,
        "naive_memory_overcompresses_tool": (
            summary["agents"]["naive_internal_memory"]["tool_as_internal_compression"] >= 0.85
        ),
        "tool_only_fails_compress": summary["agents"]["tool_only"]["compress_success"] <= 0.15,
        "capacity_boundary_routes_core_cases": (
            summary["agents"]["capacity_boundary"]["retained_success"] >= 0.95
            and summary["agents"]["capacity_boundary"]["compress_success"] >= 0.95
            and summary["agents"]["capacity_boundary"]["tool_success"] >= 0.95
        ),
        "conformal_routes_tool": summary["agents"]["t18_conformal_tool"]["tool_success"] >= 0.90,
        "conformal_false_admission_controlled": (
            summary["agents"]["t18_conformal_tool"]["noise_false_admission"] <= alpha
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
                fmt(data["compress_success"]),
                fmt(data["tool_success"]),
                fmt(data["tool_as_internal_compression"]),
            ]
        )

    by_kind_rows = []
    for kind, true_op in OPERATIONS.items():
        row = [kind, true_op]
        for agent in [
            "scalar",
            "compression_only",
            "naive_internal_memory",
            "tool_only",
            "capacity_boundary",
            "t18_conformal_tool",
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
                fmt(scores["compression_value"]),
                fmt(scores["key_memory_gain"]),
                fmt(scores["key_memory_value"]),
                fmt(scores["tool_value"]),
                fmt(scores["tool_over_memory"]),
            ]
        )

    pass_rows = [[name, "pass" if value else "fail"] for name, value in summary["pass_checks"].items()]
    overall = "PASS" if summary["overall_pass"] else "FAIL"

    text = f"""# B6 Tool Use Versus Internal Compression Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration episodes: `{config['n_calibration']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- lookup keys: `{config['n_keys']}`
- noise scale: `{config['noise_scale']}`
- compression/memory/tool cost: `{config['compression_cost']}` / `{config['memory_capacity_cost']}` / `{config['tool_cost']}`
- alpha: `{config['alpha']}`

## Claim Tested

B6-E1 asks whether an agent should externalize exact high-cardinality lookup
problems instead of absorbing them as internal compression. Tool episodes are
solvable by internal key memory, but only at a high capacity cost. The
capacity-aware boundary should choose externalize.

## Conformal Null Thresholds

{md_table(['score', 'threshold'], [[k, fmt(v)] for k, v in thresholds.items()])}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'retained success', 'compress success', 'tool success', 'tool as internal compression'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'compression only', 'naive memory', 'tool only', 'capacity boundary', 'T18 conformal tool'], by_kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'retained', 'compression value', 'key memory gain', 'key memory value', 'tool value', 'tool minus memory'], score_rows)}

## Pass Checks

{md_table(['check', 'result'], pass_rows)}

Overall: **{overall}**

## Interpretation

This is a pass if scalar surprise stays matched, low-rank compression fails
exact lookup, naive internal key memory over-compresses tool episodes, tool-only
fails genuine compression, and the capacity-aware routers send lookup cases to
externalize while controlling false admissions under the conformal null.

This would falsify the tool-use bucket if internal compression solved exact
lookup as cheaply as tool use, or if tool use and compression collapsed under
matched surprise.
"""
    path.write_text(text, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--trials-per-kind", type=int, default=260)
    parser.add_argument("--n-calibration", type=int, default=800)
    parser.add_argument("--n-train", type=int, default=192)
    parser.add_argument("--n-test", type=int, default=192)
    parser.add_argument("--n-keys", type=int, default=64)
    parser.add_argument("--noise-scale", type=float, default=0.35)
    parser.add_argument("--ridge-lambda", type=float, default=1e-3)
    parser.add_argument("--compression-cost", type=float, default=0.08)
    parser.add_argument("--memory-capacity-cost", type=float, default=0.55)
    parser.add_argument("--tool-cost", type=float, default=0.16)
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
        n_keys=args.n_keys,
        noise_scale=args.noise_scale,
        ridge_lambda=args.ridge_lambda,
        compression_cost=args.compression_cost,
        memory_capacity_cost=args.memory_capacity_cost,
        tool_cost=args.tool_cost,
        alpha=args.alpha,
    )
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            n_keys=args.n_keys,
            noise_scale=args.noise_scale,
            ridge_lambda=args.ridge_lambda,
            compression_cost=args.compression_cost,
            memory_capacity_cost=args.memory_capacity_cost,
            tool_cost=args.tool_cost,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    predictions = {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "compression_only": [compression_only_agent(m, thresholds, conformal=False) for m in metrics],
        "naive_internal_memory": [
            naive_internal_memory_agent(m, thresholds, conformal=False) for m in metrics
        ],
        "tool_only": [tool_only_agent(m, thresholds, conformal=False) for m in metrics],
        "capacity_boundary": [capacity_boundary_agent(m, thresholds, conformal=False) for m in metrics],
        "t18_conformal_tool": [capacity_boundary_agent(m, thresholds, conformal=True) for m in metrics],
    }
    summary = summarize(metrics, predictions, args.alpha)

    config = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "trials_per_kind": args.trials_per_kind,
        "n_calibration": args.n_calibration,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "n_keys": args.n_keys,
        "noise_scale": args.noise_scale,
        "ridge_lambda": args.ridge_lambda,
        "compression_cost": args.compression_cost,
        "memory_capacity_cost": args.memory_capacity_cost,
        "tool_cost": args.tool_cost,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b6_tool_use_vs_internal_compression_probe.md"
    json_path = out_dir / "b6_tool_use_vs_internal_compression_probe.json"
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
