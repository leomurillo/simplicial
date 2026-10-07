"""Minimum viable T19 conscious-boundary agent experiment.

This script tests the first operational signature of T19:

    conscious access tracks governed boundary gain, not raw surprise.

The world is finite and deliberately small. The terminal retained sector starts
with z0 only. The hidden structural condition requires the boundary packet
z0*z1. The noise condition is matched in scalar surprise but has no stable
missing packet.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


TRUE_PACKET_INDEX = 1


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    scalar_surprise: float
    boundary_score: float
    gain: float
    net_gain: float
    top_packet: int
    top_is_true: bool
    baseline_reward: float
    admitted_reward: float


@dataclass(frozen=True)
class AgentOutcome:
    admitted: bool
    correct_packet: bool
    reward: float


def make_world(rng: np.random.Generator, n: int, d: int, kind: str) -> tuple[np.ndarray, np.ndarray]:
    z = rng.choice(np.array([-1.0, 1.0]), size=(n, d))
    if kind == "structural":
        y = z[:, 0] * z[:, TRUE_PACKET_INDEX]
    elif kind == "noise":
        flips = rng.choice(np.array([-1.0, 1.0]), size=n)
        y = z[:, 0] * flips
    else:
        raise ValueError(f"unknown kind: {kind}")
    return z, y


def design_retained(z: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(len(z)), z[:, 0]])


def packet_values(z: np.ndarray, packet: int) -> np.ndarray:
    return z[:, 0] * z[:, packet]


def design_extended(z: np.ndarray, packet: int) -> np.ndarray:
    return np.column_stack([np.ones(len(z)), z[:, 0], packet_values(z, packet)])


def fit_lstsq(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(x, y, rcond=None)
    return coef


def mse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean((y - pred) ** 2))


def accuracy_reward(y: np.ndarray, pred: np.ndarray) -> float:
    labels = np.where(pred >= 0.0, 1.0, -1.0)
    return float(np.mean(labels == y))


def top_boundary_packet(z: np.ndarray, residual: np.ndarray, d: int) -> tuple[int, float]:
    candidates = np.arange(1, d)
    packets = z[:, [0]] * z[:, candidates]
    scores = np.abs(np.mean(packets * residual[:, None], axis=0))
    winner = int(candidates[int(np.argmax(scores))])
    return winner, float(np.max(scores))


def episode_metrics(
    rng: np.random.Generator,
    *,
    d: int,
    evidence_n: int,
    verify_n: int,
    action_n: int,
    kind: str,
    closure_cost: float,
    action_cost: float,
) -> EpisodeMetrics:
    z_e, y_e = make_world(rng, evidence_n, d, kind)
    z_v, y_v = make_world(rng, verify_n, d, kind)
    z_a, y_a = make_world(rng, action_n, d, kind)

    x_e = design_retained(z_e)
    base_coef = fit_lstsq(x_e, y_e)
    residual_e = y_e - x_e @ base_coef

    top_packet, boundary_score = top_boundary_packet(z_e, residual_e, d)

    base_verify_loss = mse(y_v, design_retained(z_v) @ base_coef)
    ext_coef = fit_lstsq(design_extended(z_e, top_packet), y_e)
    ext_verify_loss = mse(y_v, design_extended(z_v, top_packet) @ ext_coef)
    gain = base_verify_loss - ext_verify_loss
    net_gain = gain - closure_cost

    base_reward = accuracy_reward(y_a, design_retained(z_a) @ base_coef)
    admitted_reward = accuracy_reward(y_a, design_extended(z_a, top_packet) @ ext_coef) - action_cost

    return EpisodeMetrics(
        kind=kind,
        scalar_surprise=base_verify_loss,
        boundary_score=boundary_score,
        gain=float(gain),
        net_gain=float(net_gain),
        top_packet=top_packet,
        top_is_true=top_packet == TRUE_PACKET_INDEX,
        baseline_reward=float(base_reward),
        admitted_reward=float(admitted_reward),
    )


def conformal_p_value(null_scores: np.ndarray, score: float) -> float:
    return float((1 + np.sum(null_scores >= score)) / (len(null_scores) + 1))


def auc(pos: np.ndarray, neg: np.ndarray) -> float:
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    comparisons = pos[:, None] - neg[None, :]
    return float(np.mean((comparisons > 0).astype(float) + 0.5 * (comparisons == 0)))


def scalar_raw_agent(m: EpisodeMetrics, closure_cost: float) -> AgentOutcome:
    admitted = m.scalar_surprise > closure_cost
    return AgentOutcome(admitted, admitted and m.top_is_true, m.admitted_reward if admitted else m.baseline_reward)


def boundary_raw_agent(m: EpisodeMetrics, closure_cost: float) -> AgentOutcome:
    admitted = m.boundary_score > closure_cost
    return AgentOutcome(admitted, admitted and m.top_is_true, m.admitted_reward if admitted else m.baseline_reward)


def t17_gain_agent(m: EpisodeMetrics) -> AgentOutcome:
    admitted = m.net_gain > 0.0
    return AgentOutcome(admitted, admitted and m.top_is_true, m.admitted_reward if admitted else m.baseline_reward)


def t19_conscious_agent(m: EpisodeMetrics, null_gain_scores: np.ndarray, alpha: float) -> AgentOutcome:
    p = conformal_p_value(null_gain_scores, m.gain)
    admitted = (m.net_gain > 0.0) and (p <= alpha)
    return AgentOutcome(admitted, admitted and m.top_is_true, m.admitted_reward if admitted else m.baseline_reward)


def summarize_agent(outcomes: list[AgentOutcome], kinds: list[str]) -> dict[str, float]:
    arr_admit = np.array([o.admitted for o in outcomes], dtype=bool)
    arr_correct = np.array([o.correct_packet for o in outcomes], dtype=bool)
    rewards = np.array([o.reward for o in outcomes], dtype=float)
    kinds_arr = np.array(kinds)
    is_struct = kinds_arr == "structural"
    is_noise = kinds_arr == "noise"

    def mean_mask(values: np.ndarray, mask: np.ndarray) -> float:
        if not np.any(mask):
            return float("nan")
        return float(np.mean(values[mask]))

    return {
        "structural_admit_rate": mean_mask(arr_admit.astype(float), is_struct),
        "noise_false_admit_rate": mean_mask(arr_admit.astype(float), is_noise),
        "structural_correct_packet_rate": mean_mask(arr_correct.astype(float), is_struct),
        "noise_correct_packet_rate": mean_mask(arr_correct.astype(float), is_noise),
        "structural_reward": mean_mask(rewards, is_struct),
        "noise_reward": mean_mask(rewards, is_noise),
        "overall_reward": float(np.mean(rewards)),
    }


def run_condition(
    rng: np.random.Generator,
    *,
    d: int,
    evidence_n: int,
    verify_n: int,
    action_n: int,
    calibration_episodes: int,
    test_episodes_per_kind: int,
    alpha: float,
    closure_cost: float,
    action_cost: float,
) -> dict[str, Any]:
    null_metrics = [
        episode_metrics(
            rng,
            d=d,
            evidence_n=evidence_n,
            verify_n=verify_n,
            action_n=action_n,
            kind="noise",
            closure_cost=closure_cost,
            action_cost=action_cost,
        )
        for _ in range(calibration_episodes)
    ]
    null_scalar = np.array([m.scalar_surprise for m in null_metrics], dtype=float)
    null_boundary = np.array([m.boundary_score for m in null_metrics], dtype=float)
    null_gain = np.array([m.gain for m in null_metrics], dtype=float)

    metrics: list[EpisodeMetrics] = []
    for kind in ("structural", "noise"):
        metrics.extend(
            episode_metrics(
                rng,
                d=d,
                evidence_n=evidence_n,
                verify_n=verify_n,
                action_n=action_n,
                kind=kind,
                closure_cost=closure_cost,
                action_cost=action_cost,
            )
            for _ in range(test_episodes_per_kind)
        )

    kinds = [m.kind for m in metrics]
    struct = np.array([m.kind == "structural" for m in metrics], dtype=bool)
    scalar = np.array([m.scalar_surprise for m in metrics], dtype=float)
    boundary = np.array([m.boundary_score for m in metrics], dtype=float)
    gain = np.array([m.gain for m in metrics], dtype=float)
    top_true = np.array([m.top_is_true for m in metrics], dtype=float)

    scalar_p = np.array([conformal_p_value(null_scalar, s) for s in scalar], dtype=float)
    boundary_p = np.array([conformal_p_value(null_boundary, s) for s in boundary], dtype=float)
    gain_p = np.array([conformal_p_value(null_gain, s) for s in gain], dtype=float)

    agents = {
        "scalar_raw": [scalar_raw_agent(m, closure_cost) for m in metrics],
        "boundary_score_raw": [boundary_raw_agent(m, closure_cost) for m in metrics],
        "t17_gain_only": [t17_gain_agent(m) for m in metrics],
        "t19_conformal_conscious": [t19_conscious_agent(m, null_gain, alpha) for m in metrics],
    }

    return {
        "d": d,
        "candidate_packets": d - 1,
        "evidence_n": evidence_n,
        "verify_n": verify_n,
        "action_n": action_n,
        "calibration_episodes": calibration_episodes,
        "test_episodes_per_kind": test_episodes_per_kind,
        "alpha": alpha,
        "closure_cost": closure_cost,
        "action_cost": action_cost,
        "auc": {
            "scalar_surprise": auc(scalar[struct], scalar[~struct]),
            "boundary_score": auc(boundary[struct], boundary[~struct]),
            "boundary_gain": auc(gain[struct], gain[~struct]),
        },
        "means": {
            "structural_scalar_surprise": float(np.mean(scalar[struct])),
            "noise_scalar_surprise": float(np.mean(scalar[~struct])),
            "structural_boundary_score": float(np.mean(boundary[struct])),
            "noise_boundary_score": float(np.mean(boundary[~struct])),
            "structural_gain": float(np.mean(gain[struct])),
            "noise_gain": float(np.mean(gain[~struct])),
            "structural_top_true_rate": float(np.mean(top_true[struct])),
            "noise_top_true_rate": float(np.mean(top_true[~struct])),
        },
        "conformal_diagnostics": {
            "scalar_structural_gate_rate": float(np.mean(scalar_p[struct] <= alpha)),
            "scalar_noise_gate_rate": float(np.mean(scalar_p[~struct] <= alpha)),
            "boundary_structural_gate_rate": float(np.mean(boundary_p[struct] <= alpha)),
            "boundary_noise_gate_rate": float(np.mean(boundary_p[~struct] <= alpha)),
            "gain_structural_gate_rate": float(np.mean(gain_p[struct] <= alpha)),
            "gain_noise_gate_rate": float(np.mean(gain_p[~struct] <= alpha)),
            "null_gain_threshold_empirical": float(np.quantile(null_gain, 1.0 - alpha, method="higher")),
            "null_scalar_threshold_empirical": float(np.quantile(null_scalar, 1.0 - alpha, method="higher")),
        },
        "agents": {name: summarize_agent(outcomes, kinds) for name, outcomes in agents.items()},
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# T19 Minimal Conscious Agent Experiment")
    lines.append("")
    lines.append(f"- timestamp: `{result['timestamp']}`")
    lines.append(f"- seed: `{result['seed']}`")
    lines.append(f"- alpha: `{result['alpha']}`")
    lines.append(f"- closure cost: `{result['closure_cost']}`")
    lines.append(f"- action cost: `{result['action_cost']}`")
    lines.append("")
    lines.append("## Claim Tested")
    lines.append("")
    lines.append("Scalar surprise is matched between structural and noise episodes, but only structural episodes contain a stable boundary packet that should enter the conscious content set.")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append("| d | evidence | scalar AUC | boundary AUC | gain AUC | structural gain | noise gain | T19 TPR | T19 FPR | T19 structural reward | T19 noise reward |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in result["conditions"]:
        t19 = row["agents"]["t19_conformal_conscious"]
        lines.append(
            "| {d} | {evidence_n} | {scalar:.3f} | {boundary:.3f} | {gain:.3f} | "
            "{sgain:.3f} | {ngain:.3f} | {tpr:.3f} | {fpr:.3f} | {sr:.3f} | {nr:.3f} |".format(
                d=row["d"],
                evidence_n=row["evidence_n"],
                scalar=row["auc"]["scalar_surprise"],
                boundary=row["auc"]["boundary_score"],
                gain=row["auc"]["boundary_gain"],
                sgain=row["means"]["structural_gain"],
                ngain=row["means"]["noise_gain"],
                tpr=t19["structural_correct_packet_rate"],
                fpr=t19["noise_false_admit_rate"],
                sr=t19["structural_reward"],
                nr=t19["noise_reward"],
            )
        )
    lines.append("")
    lines.append("## Agent Comparison")
    lines.append("")
    for row in result["conditions"]:
        lines.append(f"### d={row['d']}, evidence={row['evidence_n']}")
        lines.append("")
        lines.append("| agent | structural admit | noise false admit | structural correct packet | structural reward | noise reward |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for name, stats in row["agents"].items():
            lines.append(
                "| {name} | {sa:.3f} | {nf:.3f} | {cp:.3f} | {sr:.3f} | {nr:.3f} |".format(
                    name=name,
                    sa=stats["structural_admit_rate"],
                    nf=stats["noise_false_admit_rate"],
                    cp=stats["structural_correct_packet_rate"],
                    sr=stats["structural_reward"],
                    nr=stats["noise_reward"],
                )
            )
        lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("A pass has scalar-surprise AUC near 0.5, boundary-gain AUC near 1.0, T19 false conscious admission near the finite-rank alpha level, and T19 structural admission near oracle performance.")
    lines.append("")
    lines.append("The conscious content set in this MVP has capacity one, so a successful T19 episode has `C_t = {z0*z1}` in the structural condition and `C_t = empty` in the noise condition.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=1901)
    parser.add_argument("--d", type=int, nargs="+", default=[16, 64])
    parser.add_argument("--evidence", type=int, nargs="+", default=[8, 16, 32, 64])
    parser.add_argument("--verify-n", type=int, default=64)
    parser.add_argument("--action-n", type=int, default=256)
    parser.add_argument("--calibration", type=int, default=2000)
    parser.add_argument("--episodes", type=int, default=2000, help="test episodes per kind")
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--closure-cost", type=float, default=0.0)
    parser.add_argument("--action-cost", type=float, default=0.05)
    parser.add_argument("--out-json", type=Path, default=Path("empirical/reports/t19_minimal_conscious_agent.json"))
    parser.add_argument("--out-md", type=Path, default=Path("empirical/reports/t19_minimal_conscious_agent.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    conditions = []
    for d in args.d:
        for evidence_n in args.evidence:
            conditions.append(
                run_condition(
                    rng,
                    d=d,
                    evidence_n=evidence_n,
                    verify_n=args.verify_n,
                    action_n=args.action_n,
                    calibration_episodes=args.calibration,
                    test_episodes_per_kind=args.episodes,
                    alpha=args.alpha,
                    closure_cost=args.closure_cost,
                    action_cost=args.action_cost,
                )
            )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "alpha": args.alpha,
        "closure_cost": args.closure_cost,
        "action_cost": args.action_cost,
        "conditions": conditions,
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    args.out_md.write_text(render_markdown(result), encoding="utf-8")

    print(render_markdown(result))


if __name__ == "__main__":
    main()
