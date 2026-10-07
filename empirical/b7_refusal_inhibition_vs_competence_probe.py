"""B7 refusal/inhibition versus competence probe.

This synthetic falsifier tests the governance bucket in the B-series brain
hypothesis:

    an agent can be competent enough to predict a structure and still need to
    inhibit/refuse it because the structure is forbidden by governance.

The probe creates matched-surprise episodes:

    retained: update an existing belief weight;
    safe_packet: close a lawful missing interaction;
    forbidden: inhibit a predictive but forbidden interaction;
    noise: suppress.

The forbidden episode is deliberately predictive. A pure competence maximizer
should therefore close it. A governed boundary agent earns its keep only if it
routes the same predictive evidence to inhibition/refusal instead.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


KINDS = ["retained", "safe_packet", "forbidden", "noise"]
OPERATIONS = {
    "retained": "reweight",
    "safe_packet": "close",
    "forbidden": "inhibit",
    "noise": "suppress",
}


@dataclass(frozen=True)
class FeatureBundle:
    retained: np.ndarray
    safe_packet: np.ndarray
    forbidden_packet: np.ndarray
    decoy_packet: np.ndarray


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_operation: str
    scalar_surprise: float
    retained_gain: float
    safe_packet_gain: float
    forbidden_gain: float
    decoy_gain: float
    best_competence_gain: float
    best_competence_channel: str
    forbidden_over_safe: float
    governance_risk: float
    lawful_close_value: float
    forbidden_close_value: float
    inhibition_value: float
    sanction_cost: float


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


def make_features(rng: np.random.Generator, n: int) -> FeatureBundle:
    z = rng.normal(size=(n, 8))
    return FeatureBundle(
        retained=standardize(z[:, 0]),
        safe_packet=standardize(z[:, 1] * z[:, 2]),
        forbidden_packet=standardize(z[:, 3] * z[:, 4]),
        decoy_packet=standardize(z[:, 5] * z[:, 6] + 0.2 * z[:, 7]),
    )


def make_signal(kind: str, features: FeatureBundle, rng: np.random.Generator) -> np.ndarray:
    if kind == "retained":
        signal = features.retained
    elif kind == "safe_packet":
        signal = features.safe_packet
    elif kind == "forbidden":
        signal = features.forbidden_packet
    elif kind == "noise":
        signal = rng.normal(size=len(features.retained))
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
        return standardize(rng.normal(size=len(features.retained)))
    signal = make_signal(kind, features, rng)
    return standardize(signal + rng.normal(scale=noise_scale, size=len(signal)))


def episode_metrics(
    kind: str,
    rng: np.random.Generator,
    n_train: int,
    n_test: int,
    noise_scale: float,
    sanction_cost: float,
    inhibition_cost: float,
) -> EpisodeMetrics:
    train_f = make_features(rng, n_train)
    test_f = make_features(rng, n_test)
    train_y = make_residual(kind, train_f, rng, noise_scale)
    test_y = make_residual(kind, test_f, rng, noise_scale)

    retained_gain = heldout_gain(train_f.retained, train_y, test_f.retained, test_y)
    safe_gain = heldout_gain(train_f.safe_packet, train_y, test_f.safe_packet, test_y)
    forbidden_gain = heldout_gain(
        train_f.forbidden_packet,
        train_y,
        test_f.forbidden_packet,
        test_y,
    )
    decoy_gain = heldout_gain(train_f.decoy_packet, train_y, test_f.decoy_packet, test_y)
    packet_items = [
        ("safe_packet", safe_gain),
        ("forbidden_packet", forbidden_gain),
        ("decoy_packet", decoy_gain),
    ]
    best_channel, best_gain = max(packet_items, key=lambda item: item[1])
    forbidden_close_value = forbidden_gain - sanction_cost
    lawful_close_value = safe_gain
    inhibition_value = forbidden_gain - inhibition_cost

    return EpisodeMetrics(
        kind=kind,
        true_operation=OPERATIONS[kind],
        scalar_surprise=float(np.mean(test_y**2)),
        retained_gain=float(retained_gain),
        safe_packet_gain=float(safe_gain),
        forbidden_gain=float(forbidden_gain),
        decoy_gain=float(decoy_gain),
        best_competence_gain=float(best_gain),
        best_competence_channel=best_channel,
        forbidden_over_safe=float(forbidden_gain - safe_gain),
        governance_risk=float(max(0.0, forbidden_gain)),
        lawful_close_value=float(lawful_close_value),
        forbidden_close_value=float(forbidden_close_value),
        inhibition_value=float(inhibition_value),
        sanction_cost=sanction_cost,
    )


def as_dict(m: EpisodeMetrics) -> dict[str, Any]:
    return {
        "kind": m.kind,
        "true_operation": m.true_operation,
        "scalar_surprise": m.scalar_surprise,
        "retained_gain": m.retained_gain,
        "safe_packet_gain": m.safe_packet_gain,
        "forbidden_gain": m.forbidden_gain,
        "decoy_gain": m.decoy_gain,
        "best_competence_gain": m.best_competence_gain,
        "best_competence_channel": m.best_competence_channel,
        "forbidden_over_safe": m.forbidden_over_safe,
        "governance_risk": m.governance_risk,
        "lawful_close_value": m.lawful_close_value,
        "forbidden_close_value": m.forbidden_close_value,
        "inhibition_value": m.inhibition_value,
        "sanction_cost": m.sanction_cost,
    }


def quantile(values: list[float], q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q, method="higher"))


def calibrate_thresholds(
    rng: np.random.Generator,
    n_calibration: int,
    n_train: int,
    n_test: int,
    noise_scale: float,
    sanction_cost: float,
    inhibition_cost: float,
    alpha: float,
) -> dict[str, float]:
    null = [
        episode_metrics("noise", rng, n_train, n_test, noise_scale, sanction_cost, inhibition_cost)
        for _ in range(n_calibration)
    ]
    q = 1.0 - alpha
    family_q = 1.0 - alpha / 2.0
    retained_q = quantile([m.retained_gain for m in null], q)
    safe_q = quantile([m.safe_packet_gain for m in null], q)
    forbidden_q = quantile([m.forbidden_gain for m in null], q)
    route_scores = [
        max(m.retained_gain, m.safe_packet_gain, m.forbidden_gain)
        for m in null
    ]
    route_q = quantile(route_scores, q)
    gate_scores = [
        max(
            m.retained_gain / max(retained_q, 1e-12),
            m.safe_packet_gain / max(safe_q, 1e-12),
            m.forbidden_gain / max(forbidden_q, 1e-12),
            max(m.retained_gain, m.safe_packet_gain, m.forbidden_gain) / max(route_q, 1e-12),
        )
        for m in null
    ]
    return {
        "alpha": alpha,
        "scalar": quantile([m.scalar_surprise for m in null], q),
        "retained": retained_q,
        "safe_packet": safe_q,
        "forbidden": forbidden_q,
        "route": route_q,
        "family_gate": quantile(gate_scores, family_q),
        "fixed_gain": 0.12,
    }


def scalar_agent(m: EpisodeMetrics, thresholds: dict[str, float]) -> str:
    return "reweight" if m.scalar_surprise > thresholds["scalar"] else "suppress"


def competence_maximizer_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    retained_t = thresholds["retained"] if conformal else thresholds["fixed_gain"]
    packet_t = thresholds["route"] if conformal else thresholds["fixed_gain"]
    if m.retained_gain > retained_t and m.retained_gain >= m.best_competence_gain:
        return "reweight"
    if m.best_competence_gain > packet_t:
        return "close"
    return "suppress"


def refusal_only_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    threshold = thresholds["forbidden"] if conformal else thresholds["fixed_gain"]
    return "inhibit" if m.forbidden_gain > threshold else "suppress"


def governed_boundary_agent(m: EpisodeMetrics, thresholds: dict[str, float], conformal: bool) -> str:
    if conformal:
        retained_t = thresholds["retained"]
        safe_t = thresholds["safe_packet"]
        forbidden_t = thresholds["forbidden"]
        route_t = thresholds["route"]
        family_gate_t = thresholds["family_gate"]
    else:
        retained_t = thresholds["fixed_gain"]
        safe_t = thresholds["fixed_gain"]
        forbidden_t = thresholds["fixed_gain"]
        route_t = thresholds["fixed_gain"]
        family_gate_t = 1.0

    route_score = max(m.retained_gain, m.safe_packet_gain, m.forbidden_gain)
    family_gate_score = max(
        m.retained_gain / max(retained_t, 1e-12),
        m.safe_packet_gain / max(safe_t, 1e-12),
        m.forbidden_gain / max(forbidden_t, 1e-12),
        route_score / max(route_t, 1e-12),
    )
    if conformal and family_gate_score <= family_gate_t:
        return "suppress"
    if m.forbidden_gain > forbidden_t and m.forbidden_gain >= m.safe_packet_gain:
        return "inhibit"
    if m.retained_gain > retained_t and m.retained_gain >= m.safe_packet_gain:
        return "reweight"
    if m.safe_packet_gain > safe_t:
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
            "safe_packet_success": float(
                np.mean([p == "close" for p, m in zip(preds, metrics) if m.kind == "safe_packet"])
            ),
            "forbidden_inhibit_success": float(
                np.mean([p == "inhibit" for p, m in zip(preds, metrics) if m.kind == "forbidden"])
            ),
            "forbidden_as_closure": float(
                np.mean([p == "close" for p, m in zip(preds, metrics) if m.kind == "forbidden"])
            ),
            "safe_packet_false_inhibition": float(
                np.mean([p == "inhibit" for p, m in zip(preds, metrics) if m.kind == "safe_packet"])
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
        "safe_packet_gain_safe_vs_noise": auc(
            [1 if m.kind == "safe_packet" else 0 for m in metrics if m.kind in {"safe_packet", "noise"}],
            [m.safe_packet_gain for m in metrics if m.kind in {"safe_packet", "noise"}],
        ),
        "forbidden_gain_forbidden_vs_noise": auc(
            [1 if m.kind == "forbidden" else 0 for m in metrics if m.kind in {"forbidden", "noise"}],
            [m.forbidden_gain for m in metrics if m.kind in {"forbidden", "noise"}],
        ),
        "forbidden_gain_forbidden_vs_safe": auc(
            [1 if m.kind == "forbidden" else 0 for m in metrics if m.kind in {"forbidden", "safe_packet"}],
            [m.forbidden_gain for m in metrics if m.kind in {"forbidden", "safe_packet"}],
        ),
        "best_competence_forbidden_or_safe_vs_noise": auc(
            [
                1 if m.kind in {"forbidden", "safe_packet"} else 0
                for m in metrics
                if m.kind in {"forbidden", "safe_packet", "noise"}
            ],
            [
                m.best_competence_gain
                for m in metrics
                if m.kind in {"forbidden", "safe_packet", "noise"}
            ],
        ),
    }

    summary["mean_scores_by_kind"] = {
        kind: {
            "scalar": float(np.mean([m.scalar_surprise for m in metrics if m.kind == kind])),
            "retained": float(np.mean([m.retained_gain for m in metrics if m.kind == kind])),
            "safe_packet": float(np.mean([m.safe_packet_gain for m in metrics if m.kind == kind])),
            "forbidden": float(np.mean([m.forbidden_gain for m in metrics if m.kind == kind])),
            "best_competence": float(np.mean([m.best_competence_gain for m in metrics if m.kind == kind])),
            "forbidden_over_safe": float(np.mean([m.forbidden_over_safe for m in metrics if m.kind == kind])),
            "forbidden_close_value": float(
                np.mean([m.forbidden_close_value for m in metrics if m.kind == kind])
            ),
            "inhibition_value": float(np.mean([m.inhibition_value for m in metrics if m.kind == kind])),
        }
        for kind in KINDS
    }

    scalar_range = (
        max(v["scalar"] for v in summary["mean_scores_by_kind"].values())
        - min(v["scalar"] for v in summary["mean_scores_by_kind"].values())
    )
    summary["pass_checks"] = {
        "scalar_surprise_matched": scalar_range <= 0.01,
        "competence_closes_forbidden": (
            summary["agents"]["competence_maximizer"]["forbidden_as_closure"] >= 0.95
        ),
        "refusal_only_fails_safe_packet": (
            summary["agents"]["refusal_only"]["safe_packet_success"] <= 0.15
        ),
        "governed_boundary_inhibits_forbidden": (
            summary["agents"]["governed_boundary"]["forbidden_inhibit_success"] >= 0.95
        ),
        "governed_boundary_preserves_competence": (
            summary["agents"]["governed_boundary"]["retained_success"] >= 0.95
            and summary["agents"]["governed_boundary"]["safe_packet_success"] >= 0.95
        ),
        "conformal_inhibits_forbidden": (
            summary["agents"]["t18_conformal_governed"]["forbidden_inhibit_success"] >= 0.90
        ),
        "conformal_false_admission_controlled": (
            summary["agents"]["t18_conformal_governed"]["noise_false_admission"] <= alpha
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
                fmt(data["safe_packet_success"]),
                fmt(data["forbidden_inhibit_success"]),
                fmt(data["forbidden_as_closure"]),
                fmt(data["safe_packet_false_inhibition"]),
            ]
        )

    by_kind_rows = []
    for kind, true_op in OPERATIONS.items():
        row = [kind, true_op]
        for agent in [
            "scalar",
            "competence_maximizer",
            "refusal_only",
            "governed_boundary",
            "t18_conformal_governed",
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
                fmt(scores["safe_packet"]),
                fmt(scores["forbidden"]),
                fmt(scores["best_competence"]),
                fmt(scores["forbidden_close_value"]),
                fmt(scores["inhibition_value"]),
            ]
        )

    pass_rows = [[name, "pass" if value else "fail"] for name, value in summary["pass_checks"].items()]
    overall = "PASS" if summary["overall_pass"] else "FAIL"

    text = f"""# B7 Refusal/Inhibition Versus Competence Probe

- timestamp: `{config['timestamp']}`
- seed: `{config['seed']}`
- trials per kind: `{config['trials_per_kind']}`
- calibration episodes: `{config['n_calibration']}`
- evidence train/test: `{config['n_train']}` / `{config['n_test']}`
- noise scale: `{config['noise_scale']}`
- sanction/inhibition cost: `{config['sanction_cost']}` / `{config['inhibition_cost']}`
- alpha: `{config['alpha']}`

## Claim Tested

B7-E1 asks whether governance is distinct from incompetence. Forbidden episodes
are genuinely predictive: a competence maximizer can explain them. The governed
boundary should inhibit/refuse them while still closing lawful packets.

## Conformal Null Thresholds

{md_table(['score', 'threshold'], [[k, fmt(v)] for k, v in thresholds.items()])}

## Agent Summary

{md_table(['agent', 'routing accuracy', 'noise false admission', 'retained success', 'safe packet success', 'forbidden inhibit success', 'forbidden as closure', 'safe false inhibition'], agent_rows)}

## Accuracy by Episode Kind

{md_table(['kind', 'true op', 'scalar', 'competence maximizer', 'refusal only', 'governed boundary', 'T18 conformal governed'], by_kind_rows)}

## AUC Checks

{md_table(['check', 'AUC'], [[k, fmt(v)] for k, v in summary['auc'].items()])}

## Mean Scores by Kind

{md_table(['kind', 'scalar', 'retained', 'safe packet', 'forbidden', 'best competence', 'forbidden close value', 'inhibition value'], score_rows)}

## Pass Checks

{md_table(['check', 'result'], pass_rows)}

Overall: **{overall}**

## Interpretation

This is a pass if scalar surprise stays matched, unconstrained competence closes
forbidden predictive structure, refusal-only behavior fails lawful competence,
and governed routers inhibit forbidden structure while preserving retained and
lawful packet performance.

This would falsify the governance bucket if forbidden structure were merely
noise, if refusal were just incompetence, or if the governed router could not
separate lawful closure from forbidden closure under matched predictive gain.
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
    parser.add_argument("--sanction-cost", type=float, default=1.05)
    parser.add_argument("--inhibition-cost", type=float, default=0.10)
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
        sanction_cost=args.sanction_cost,
        inhibition_cost=args.inhibition_cost,
        alpha=args.alpha,
    )
    metrics = [
        episode_metrics(
            kind,
            rng,
            n_train=args.n_train,
            n_test=args.n_test,
            noise_scale=args.noise_scale,
            sanction_cost=args.sanction_cost,
            inhibition_cost=args.inhibition_cost,
        )
        for kind in KINDS
        for _ in range(args.trials_per_kind)
    ]
    predictions = {
        "scalar": [scalar_agent(m, thresholds) for m in metrics],
        "competence_maximizer": [
            competence_maximizer_agent(m, thresholds, conformal=False) for m in metrics
        ],
        "refusal_only": [refusal_only_agent(m, thresholds, conformal=False) for m in metrics],
        "governed_boundary": [governed_boundary_agent(m, thresholds, conformal=False) for m in metrics],
        "t18_conformal_governed": [
            governed_boundary_agent(m, thresholds, conformal=True) for m in metrics
        ],
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
        "sanction_cost": args.sanction_cost,
        "inhibition_cost": args.inhibition_cost,
        "alpha": args.alpha,
    }

    out_dir = args.report_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "b7_refusal_inhibition_vs_competence_probe.md"
    json_path = out_dir / "b7_refusal_inhibition_vs_competence_probe.json"
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
