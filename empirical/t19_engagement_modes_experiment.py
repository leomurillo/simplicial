"""T19 engagement modes experiment.

This experiment operationalizes four engagement regimes as policies over
boundary completion:

1. status_quo: no structural boundary is needed;
2. ambivalence: multiple lawful boundary completions are admitted;
3. devolution: a high-gain boundary completion is disallowed by governance;
4. higher_consciousness: a unique lawful completion expands the retained sector.

The finite world reuses the T19 minimal conscious-agent setup: the retained
terminal sector starts with z0, and candidate conscious packets are z0*zj.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


BENEFICIAL_PACKET = 1
AMBIVALENT_PACKET = 2
HARMFUL_PACKET = 3


@dataclass(frozen=True)
class Episode:
    condition: str
    scalar_surprise: float
    conformal_set: tuple[int, ...]
    raw_set: tuple[int, ...]
    top_packet: int | None
    engagement: str
    ungoverned_engagement: str
    self_delta: float
    local_reward: float
    governed_reward: float


def make_z(rng: np.random.Generator, n: int, d: int) -> np.ndarray:
    return rng.choice(np.array([-1.0, 1.0]), size=(n, d))


def packet(z: np.ndarray, idx: int) -> np.ndarray:
    return z[:, 0] * z[:, idx]


def make_y(rng: np.random.Generator, z: np.ndarray, condition: str) -> np.ndarray:
    if condition == "status_quo":
        return z[:, 0].copy()
    if condition == "ambivalence":
        selector = rng.choice(np.array([False, True]), size=len(z))
        y = packet(z, BENEFICIAL_PACKET)
        y[selector] = packet(z, AMBIVALENT_PACKET)[selector]
        return y
    if condition == "devolution":
        return packet(z, HARMFUL_PACKET)
    if condition == "higher_consciousness":
        return packet(z, BENEFICIAL_PACKET)
    raise ValueError(f"unknown condition: {condition}")


def retained_design(z: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(len(z)), z[:, 0]])


def extended_design(z: np.ndarray, idx: int) -> np.ndarray:
    return np.column_stack([np.ones(len(z)), z[:, 0], packet(z, idx)])


def fit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(x, y, rcond=None)
    return coef


def mse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean((y - pred) ** 2))


def accuracy(y: np.ndarray, pred: np.ndarray) -> float:
    labels = np.where(pred >= 0.0, 1.0, -1.0)
    return float(np.mean(labels == y))


def packet_gains(
    z_e: np.ndarray,
    y_e: np.ndarray,
    z_v: np.ndarray,
    y_v: np.ndarray,
    d: int,
) -> tuple[float, np.ndarray, np.ndarray]:
    base_coef = fit(retained_design(z_e), y_e)
    base_loss = mse(y_v, retained_design(z_v) @ base_coef)

    gains = np.zeros(d)
    rewards = np.zeros(d)
    for idx in range(1, d):
        coef = fit(extended_design(z_e, idx), y_e)
        gains[idx] = base_loss - mse(y_v, extended_design(z_v, idx) @ coef)
        rewards[idx] = accuracy(y_v, extended_design(z_v, idx) @ coef)
    return base_loss, gains, rewards


def build_null_ledger(
    rng: np.random.Generator,
    *,
    d: int,
    evidence_n: int,
    verify_n: int,
    calibration: int,
) -> dict[str, np.ndarray]:
    max_gains = []
    scalar_surprises = []
    for _ in range(calibration):
        z_e = make_z(rng, evidence_n, d)
        z_v = make_z(rng, verify_n, d)
        y_e = make_y(rng, z_e, "status_quo")
        y_v = make_y(rng, z_v, "status_quo")
        scalar_surprise, gains, _ = packet_gains(z_e, y_e, z_v, y_v, d)
        scalar_surprises.append(float(scalar_surprise))
        max_gains.append(float(np.max(gains[1:])))
    return {
        "max_gains": np.array(max_gains, dtype=float),
        "scalar_surprises": np.array(scalar_surprises, dtype=float),
    }


def conformal_p(null_max_gains: np.ndarray, gain: float) -> float:
    return float((1 + np.sum(null_max_gains >= gain)) / (len(null_max_gains) + 1))


def classify_engagement(
    *,
    conformal_set: tuple[int, ...],
    raw_set: tuple[int, ...],
    allowed: set[int],
    scalar_surprise: float,
    status_surprise_threshold: float,
) -> tuple[str, str, float]:
    allowed_set = tuple(idx for idx in conformal_set if idx in allowed)
    disallowed_set = tuple(idx for idx in conformal_set if idx not in allowed)

    if len(conformal_set) == 0:
        if scalar_surprise <= status_surprise_threshold:
            return "status_quo", "status_quo", 0.0
        return "unresolved_ambivalence", "unresolved_ambivalence", 0.0

    if disallowed_set and not allowed_set:
        return "devolution_blocked", "devolution", 0.0

    if len(allowed_set) > 1:
        return "unresolved_ambivalence", "unresolved_ambivalence", 0.0

    if len(allowed_set) == 1:
        chosen = allowed_set[0]
        if chosen == BENEFICIAL_PACKET and len(conformal_set) == 1:
            return "higher_consciousness", "higher_consciousness", 1.0
        return "unresolved_ambivalence", "unresolved_ambivalence", 0.0

    if raw_set:
        return "devolution_blocked", "devolution", 0.0

    return "unresolved_ambivalence", "unresolved_ambivalence", 0.0


def run_episode(
    rng: np.random.Generator,
    *,
    d: int,
    evidence_n: int,
    verify_n: int,
    condition: str,
    null_max_gains: np.ndarray,
    alpha: float,
    min_gain: float,
    allowed: set[int],
    status_surprise_threshold: float,
) -> Episode:
    z_e = make_z(rng, evidence_n, d)
    z_v = make_z(rng, verify_n, d)
    y_e = make_y(rng, z_e, condition)
    y_v = make_y(rng, z_v, condition)

    scalar_surprise, gains, rewards = packet_gains(z_e, y_e, z_v, y_v, d)
    pvals = np.array([1.0] + [conformal_p(null_max_gains, gains[idx]) for idx in range(1, d)])

    raw = tuple(int(idx) for idx in range(1, d) if gains[idx] > min_gain)
    conformal = tuple(int(idx) for idx in range(1, d) if gains[idx] > min_gain and pvals[idx] <= alpha)
    top_packet = int(np.argmax(gains[1:]) + 1) if len(raw) else None

    engagement, ungoverned_engagement, self_delta = classify_engagement(
        conformal_set=conformal,
        raw_set=raw,
        allowed=allowed,
        scalar_surprise=scalar_surprise,
        status_surprise_threshold=status_surprise_threshold,
    )

    base_reward = accuracy(y_v, retained_design(z_v) @ fit(retained_design(z_e), y_e))
    local_reward = float(rewards[top_packet]) if top_packet is not None else base_reward
    if engagement == "higher_consciousness":
        governed_reward = local_reward
    elif engagement == "devolution_blocked":
        governed_reward = base_reward
    else:
        governed_reward = base_reward

    return Episode(
        condition=condition,
        scalar_surprise=scalar_surprise,
        conformal_set=conformal,
        raw_set=raw,
        top_packet=top_packet,
        engagement=engagement,
        ungoverned_engagement=ungoverned_engagement,
        self_delta=self_delta,
        local_reward=local_reward,
        governed_reward=governed_reward,
    )


def confusion(rows: list[Episode], *, key: str) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    for row in rows:
        pred = getattr(row, key)
        out.setdefault(row.condition, {})
        out[row.condition][pred] = out[row.condition].get(pred, 0) + 1
    return out


def summarize(rows: list[Episode]) -> dict[str, Any]:
    by_condition: dict[str, list[Episode]] = {}
    for row in rows:
        by_condition.setdefault(row.condition, []).append(row)

    summary: dict[str, Any] = {}
    for condition, group in by_condition.items():
        summary[condition] = {
            "n": len(group),
            "mean_scalar_surprise": float(np.mean([r.scalar_surprise for r in group])),
            "mean_conformal_set_size": float(np.mean([len(r.conformal_set) for r in group])),
            "mean_raw_set_size": float(np.mean([len(r.raw_set) for r in group])),
            "mean_self_delta": float(np.mean([r.self_delta for r in group])),
            "mean_local_reward": float(np.mean([r.local_reward for r in group])),
            "mean_governed_reward": float(np.mean([r.governed_reward for r in group])),
        }
    return summary


def as_jsonable(rows: list[Episode]) -> list[dict[str, Any]]:
    return [
        {
            "condition": r.condition,
            "scalar_surprise": r.scalar_surprise,
            "conformal_set": list(r.conformal_set),
            "raw_set": list(r.raw_set),
            "top_packet": r.top_packet,
            "engagement": r.engagement,
            "ungoverned_engagement": r.ungoverned_engagement,
            "self_delta": r.self_delta,
            "local_reward": r.local_reward,
            "governed_reward": r.governed_reward,
        }
        for r in rows
    ]


def render_markdown(result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# T19 Engagement Modes Experiment")
    lines.append("")
    lines.append(f"- timestamp: `{result['timestamp']}`")
    lines.append(f"- seed: `{result['seed']}`")
    lines.append(f"- alpha: `{result['alpha']}`")
    lines.append(f"- allowed packets: `{result['allowed_packets']}`")
    lines.append(f"- harmful packet: `{HARMFUL_PACKET}`")
    lines.append("")
    lines.append("## Claim Tested")
    lines.append("")
    lines.append("The same boundary-completion machinery can distinguish four engagement modes: status quo, unresolved ambivalence, blocked devolution, and higher-consciousness expansion.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| condition | n | scalar surprise | conformal set size | raw set size | self delta | local reward | governed reward |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for condition, row in result["summary"].items():
        lines.append(
            "| {condition} | {n} | {surprise:.3f} | {csize:.3f} | {rsize:.3f} | {delta:.3f} | {local:.3f} | {gov:.3f} |".format(
                condition=condition,
                n=row["n"],
                surprise=row["mean_scalar_surprise"],
                csize=row["mean_conformal_set_size"],
                rsize=row["mean_raw_set_size"],
                delta=row["mean_self_delta"],
                local=row["mean_local_reward"],
                gov=row["mean_governed_reward"],
            )
        )
    lines.append("")
    lines.append("## Governed Engagement Confusion")
    lines.append("")
    for condition, preds in result["governed_confusion"].items():
        rendered = ", ".join(f"`{k}`={v}" for k, v in sorted(preds.items()))
        lines.append(f"- `{condition}`: {rendered}")
    lines.append("")
    lines.append("## Ungoverned Engagement Confusion")
    lines.append("")
    for condition, preds in result["ungoverned_confusion"].items():
        rendered = ", ".join(f"`{k}`={v}" for k, v in sorted(preds.items()))
        lines.append(f"- `{condition}`: {rendered}")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("A pass means: closed episodes maintain status quo; mixed structural episodes produce non-singleton ambivalence; harmful high-gain packets are detected but blocked by governance; and the unique lawful packet enters the higher-consciousness route with positive self delta.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=1902)
    parser.add_argument("--d", type=int, default=16)
    parser.add_argument("--evidence-n", type=int, default=128)
    parser.add_argument("--verify-n", type=int, default=256)
    parser.add_argument("--calibration", type=int, default=2000)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--min-gain", type=float, default=0.05)
    parser.add_argument("--out-json", type=Path, default=Path("empirical/reports/t19_engagement_modes_experiment.json"))
    parser.add_argument("--out-md", type=Path, default=Path("empirical/reports/t19_engagement_modes_experiment.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    if args.d <= HARMFUL_PACKET:
        raise ValueError("--d must be greater than the harmful packet index")

    null_ledger = build_null_ledger(
        rng,
        d=args.d,
        evidence_n=args.evidence_n,
        verify_n=args.verify_n,
        calibration=args.calibration,
    )
    null_max_gains = null_ledger["max_gains"]
    null_scalar_surprises = null_ledger["scalar_surprises"]
    status_surprise_threshold = float(np.quantile(null_scalar_surprises, 0.95, method="higher") + 1.0e-9)
    allowed = {BENEFICIAL_PACKET, AMBIVALENT_PACKET}

    rows: list[Episode] = []
    for condition in ("status_quo", "ambivalence", "devolution", "higher_consciousness"):
        for _ in range(args.episodes):
            rows.append(
                run_episode(
                    rng,
                    d=args.d,
                    evidence_n=args.evidence_n,
                    verify_n=args.verify_n,
                    condition=condition,
                    null_max_gains=null_max_gains,
                    alpha=args.alpha,
                    min_gain=args.min_gain,
                    allowed=allowed,
                    status_surprise_threshold=status_surprise_threshold,
                )
            )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "d": args.d,
        "evidence_n": args.evidence_n,
        "verify_n": args.verify_n,
        "calibration": args.calibration,
        "episodes_per_condition": args.episodes,
        "alpha": args.alpha,
        "min_gain": args.min_gain,
        "allowed_packets": sorted(allowed),
        "harmful_packet": HARMFUL_PACKET,
        "status_surprise_threshold": status_surprise_threshold,
        "null_max_gain_threshold": float(np.quantile(null_max_gains, 1.0 - args.alpha, method="higher")),
        "summary": summarize(rows),
        "governed_confusion": confusion(rows, key="engagement"),
        "ungoverned_confusion": confusion(rows, key="ungoverned_engagement"),
        "episodes": as_jsonable(rows),
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    args.out_md.write_text(render_markdown(result), encoding="utf-8")
    print(render_markdown(result))


if __name__ == "__main__":
    main()
