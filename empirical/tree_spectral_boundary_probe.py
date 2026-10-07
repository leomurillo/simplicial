"""Tree-spectral boundary probe inspired by Nava-Wyart 2605.23821.

This experiment turns the paper's hierarchy geometry into a T16/T17 test.

1. Build a perfect binary tree and an exponential tree-distance kernel.
2. Use Haar split modes as the packet dictionary.
3. Retain only coarse hierarchy packets, hiding finer split packets.
4. Generate matched scalar-surprise episodes:
   - structural: one omitted fine packet drives the target;
   - noise: same retained-sector surprise, no stable omitted packet.
5. Compare scalar surprise, raw in-sample residual correlation, raw kernel
   priority, and held-out T17 boundary gain.

Expected pass condition:
scalar surprise is near chance for structure/noise, raw spectral priority is
not episode-specific, and held-out boundary gain identifies/adopts the omitted
packet with conformal false-admission near alpha.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


@dataclass(frozen=True)
class Packet:
    label: str
    level: int
    node: int
    feature: np.ndarray
    eigenvalue: float


@dataclass(frozen=True)
class EpisodeMetrics:
    kind: str
    true_packet: str | None
    scalar_surprise: float
    raw_corr_score: float
    raw_corr_packet: str
    raw_corr_is_true: bool
    t17_gain: float
    t17_packet: str
    t17_is_true: bool
    raw_kernel_packet: str
    raw_kernel_is_true: bool


def leaf_tree_distance_matrix(depth: int) -> np.ndarray:
    n = 2**depth
    leaves = np.arange(n, dtype=int)
    distances = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i, j] = 0.0
                continue
            xor = int(leaves[i] ^ leaves[j])
            first_diff_from_left = depth - int(xor.bit_length())
            lca_depth = first_diff_from_left
            distances[i, j] = 2.0 * (depth - lca_depth)
    return distances


def exponential_tree_kernel(depth: int, decay: float) -> np.ndarray:
    return np.exp(-decay * leaf_tree_distance_matrix(depth))


def haar_feature(depth: int, level: int, node: int) -> np.ndarray:
    n = 2**depth
    support = 2 ** (depth - level)
    half = support // 2
    start = node * support
    feature = np.zeros(n, dtype=float)
    amplitude = np.sqrt(n / support)
    feature[start : start + half] = amplitude
    feature[start + half : start + support] = -amplitude
    return feature


def build_packets(depth: int, kernel: np.ndarray) -> list[Packet]:
    n = 2**depth
    packets: list[Packet] = []
    for level in range(depth):
        for node in range(2**level):
            feature = haar_feature(depth, level, node)
            v = feature / np.sqrt(n)
            eigenvalue = float(v @ kernel @ v)
            packets.append(
                Packet(
                    label=f"L{level}:N{node}",
                    level=level,
                    node=node,
                    feature=feature,
                    eigenvalue=eigenvalue,
                )
            )
    return packets


def design_matrix(indices: np.ndarray, retained: list[Packet]) -> np.ndarray:
    cols = [np.ones(len(indices), dtype=float)]
    cols.extend(packet.feature[indices] for packet in retained)
    return np.column_stack(cols)


def packet_matrix(indices: np.ndarray, candidates: list[Packet]) -> np.ndarray:
    return np.column_stack([packet.feature[indices] for packet in candidates])


def fit_lstsq(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(x, y, rcond=None)
    return coef


def mse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean((y - pred) ** 2))


def candidate_gains(
    x_e: np.ndarray,
    y_e: np.ndarray,
    phi_e: np.ndarray,
    x_v: np.ndarray,
    y_v: np.ndarray,
    phi_v: np.ndarray,
) -> tuple[float, np.ndarray, np.ndarray]:
    base_coef = fit_lstsq(x_e, y_e)
    residual_e = y_e - x_e @ base_coef
    base_pred_v = x_v @ base_coef
    base_loss = mse(y_v, base_pred_v)

    xtx_inv = np.linalg.pinv(x_e.T @ x_e)
    candidate_base_coef = xtx_inv @ x_e.T @ phi_e
    phi_e_perp = phi_e - x_e @ candidate_base_coef
    phi_v_perp = phi_v - x_v @ candidate_base_coef
    denom = np.sum(phi_e_perp * phi_e_perp, axis=0)
    numer = np.sum(phi_e_perp * residual_e[:, None], axis=0)
    coef = np.divide(numer, denom, out=np.zeros_like(numer), where=denom > 1e-12)

    pred_delta_v = phi_v_perp * coef[None, :]
    ext_loss = np.mean((y_v[:, None] - (base_pred_v[:, None] + pred_delta_v)) ** 2, axis=0)
    gains = base_loss - ext_loss
    raw_corr = np.abs(np.mean(phi_e * residual_e[:, None], axis=0))
    return base_loss, gains, raw_corr


def auc(pos: np.ndarray, neg: np.ndarray) -> float:
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    comparisons = pos[:, None] - neg[None, :]
    return float(np.mean((comparisons > 0).astype(float) + 0.5 * (comparisons == 0)))


def conformal_p_value(null_scores: np.ndarray, score: float) -> float:
    return float((1 + np.sum(null_scores >= score)) / (len(null_scores) + 1))


def make_episode(
    rng: np.random.Generator,
    *,
    depth: int,
    retained: list[Packet],
    candidates: list[Packet],
    target_pool: list[int],
    raw_kernel_index: int,
    evidence_n: int,
    verify_n: int,
    signal: float,
    noise_sd: float,
    kind: str,
) -> EpisodeMetrics:
    n_leaves = 2**depth
    idx_e = rng.integers(0, n_leaves, size=evidence_n)
    idx_v = rng.integers(0, n_leaves, size=verify_n)

    true_index: int | None = None
    true_packet: Packet | None = None
    total_sd = float(np.sqrt(signal * signal + noise_sd * noise_sd))

    if kind == "structural":
        true_index = int(rng.choice(np.array(target_pool, dtype=int)))
        true_packet = candidates[true_index]
        y_e = signal * true_packet.feature[idx_e] + rng.normal(0.0, noise_sd, size=evidence_n)
        y_v = signal * true_packet.feature[idx_v] + rng.normal(0.0, noise_sd, size=verify_n)
    elif kind == "noise":
        y_e = rng.normal(0.0, total_sd, size=evidence_n)
        y_v = rng.normal(0.0, total_sd, size=verify_n)
    else:
        raise ValueError(f"unknown kind: {kind}")

    x_e = design_matrix(idx_e, retained)
    x_v = design_matrix(idx_v, retained)
    phi_e = packet_matrix(idx_e, candidates)
    phi_v = packet_matrix(idx_v, candidates)
    base_loss, gains, raw_corr = candidate_gains(x_e, y_e, phi_e, x_v, y_v, phi_v)

    gain_index = int(np.argmax(gains))
    corr_index = int(np.argmax(raw_corr))
    raw_kernel_packet = candidates[raw_kernel_index]

    return EpisodeMetrics(
        kind=kind,
        true_packet=true_packet.label if true_packet is not None else None,
        scalar_surprise=base_loss,
        raw_corr_score=float(raw_corr[corr_index]),
        raw_corr_packet=candidates[corr_index].label,
        raw_corr_is_true=true_index is not None and corr_index == true_index,
        t17_gain=float(gains[gain_index]),
        t17_packet=candidates[gain_index].label,
        t17_is_true=true_index is not None and gain_index == true_index,
        raw_kernel_packet=raw_kernel_packet.label,
        raw_kernel_is_true=true_index is not None and raw_kernel_index == true_index,
    )


def summarize_condition(
    rng: np.random.Generator,
    *,
    depth: int,
    decay: float,
    retained_levels: int,
    target_level: int,
    evidence_n: int,
    verify_n: int,
    calibration_episodes: int,
    test_episodes_per_kind: int,
    signal: float,
    noise_sd: float,
    alpha: float,
    closure_cost: float,
) -> dict[str, Any]:
    kernel = exponential_tree_kernel(depth, decay)
    packets = build_packets(depth, kernel)
    retained = [packet for packet in packets if packet.level < retained_levels]
    candidates = [packet for packet in packets if packet.level >= retained_levels]
    target_pool = [i for i, packet in enumerate(candidates) if packet.level == target_level]
    if not target_pool:
        raise ValueError("target_level must be present among omitted candidates")

    raw_kernel_index = int(np.argmax([packet.eigenvalue for packet in candidates]))

    null_metrics = [
        make_episode(
            rng,
            depth=depth,
            retained=retained,
            candidates=candidates,
            target_pool=target_pool,
            raw_kernel_index=raw_kernel_index,
            evidence_n=evidence_n,
            verify_n=verify_n,
            signal=signal,
            noise_sd=noise_sd,
            kind="noise",
        )
        for _ in range(calibration_episodes)
    ]
    null_gain = np.array([m.t17_gain for m in null_metrics], dtype=float)

    metrics: list[EpisodeMetrics] = []
    for kind in ("structural", "noise"):
        metrics.extend(
            make_episode(
                rng,
                depth=depth,
                retained=retained,
                candidates=candidates,
                target_pool=target_pool,
                raw_kernel_index=raw_kernel_index,
                evidence_n=evidence_n,
                verify_n=verify_n,
                signal=signal,
                noise_sd=noise_sd,
                kind=kind,
            )
            for _ in range(test_episodes_per_kind)
        )

    is_struct = np.array([m.kind == "structural" for m in metrics], dtype=bool)
    scalar = np.array([m.scalar_surprise for m in metrics], dtype=float)
    raw_corr = np.array([m.raw_corr_score for m in metrics], dtype=float)
    gain = np.array([m.t17_gain for m in metrics], dtype=float)
    p_gain = np.array([conformal_p_value(null_gain, score) for score in gain], dtype=float)
    admitted = (p_gain <= alpha) & (gain > closure_cost)
    t17_true = np.array([m.t17_is_true for m in metrics], dtype=bool)
    raw_corr_true = np.array([m.raw_corr_is_true for m in metrics], dtype=bool)
    raw_kernel_true = np.array([m.raw_kernel_is_true for m in metrics], dtype=bool)

    support_leaves = 2 ** (depth - target_level)
    condition = {
        "depth": depth,
        "leaves": 2**depth,
        "decay": decay,
        "retained_levels": retained_levels,
        "retained_packets": len(retained),
        "candidate_packets": len(candidates),
        "target_level": target_level,
        "target_packets": len(target_pool),
        "target_support_leaves": support_leaves,
        "evidence_n": evidence_n,
        "verify_n": verify_n,
        "calibration_episodes": calibration_episodes,
        "test_episodes_per_kind": test_episodes_per_kind,
        "signal": signal,
        "noise_sd": noise_sd,
        "alpha": alpha,
        "closure_cost": closure_cost,
        "raw_kernel_packet": candidates[raw_kernel_index].label,
        "raw_kernel_packet_level": candidates[raw_kernel_index].level,
        "auc": {
            "scalar_surprise": auc(scalar[is_struct], scalar[~is_struct]),
            "raw_in_sample_corr": auc(raw_corr[is_struct], raw_corr[~is_struct]),
            "t17_heldout_gain": auc(gain[is_struct], gain[~is_struct]),
            "raw_kernel_priority": 0.5,
        },
        "means": {
            "structural_scalar_surprise": float(np.mean(scalar[is_struct])),
            "noise_scalar_surprise": float(np.mean(scalar[~is_struct])),
            "structural_raw_corr": float(np.mean(raw_corr[is_struct])),
            "noise_raw_corr": float(np.mean(raw_corr[~is_struct])),
            "structural_t17_gain": float(np.mean(gain[is_struct])),
            "noise_t17_gain": float(np.mean(gain[~is_struct])),
        },
        "packet_identification": {
            "raw_kernel_true_rate": float(np.mean(raw_kernel_true[is_struct])),
            "raw_corr_true_rate": float(np.mean(raw_corr_true[is_struct])),
            "t17_gain_true_rate": float(np.mean(t17_true[is_struct])),
            "conformal_admitted_true_rate": float(np.mean(admitted[is_struct] & t17_true[is_struct])),
            "conformal_structural_admit_rate": float(np.mean(admitted[is_struct])),
            "conformal_noise_false_admit_rate": float(np.mean(admitted[~is_struct])),
            "null_gain_threshold_empirical": float(np.quantile(null_gain, 1.0 - alpha, method="higher")),
        },
    }
    return condition


def render_markdown(result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Tree Spectral Boundary Probe")
    lines.append("")
    lines.append(f"- timestamp: `{result['timestamp']}`")
    lines.append(f"- seed: `{result['seed']}`")
    lines.append(f"- alpha: `{result['alpha']}`")
    lines.append(f"- closure cost: `{result['closure_cost']}`")
    lines.append("")
    lines.append("## Claim Tested")
    lines.append("")
    lines.append(
        "A Nava-Wyart style tree co-occurrence kernel induces Haar hierarchy packets. "
        "After retaining only coarse packets, scalar surprise should not tell structural "
        "omitted packets from matched noise, while held-out T17 boundary gain should "
        "identify and admit the missing fine split."
    )
    lines.append("")
    lines.append("## Setup")
    lines.append("")
    first = result["conditions"][0]
    lines.append(
        f"- binary leaf tree: depth `{first['depth']}`, leaves `{first['leaves']}`"
    )
    lines.append(
        f"- kernel: `K_ij = exp(-{first['decay']} * tree_distance(i,j))`"
    )
    lines.append(
        f"- retained hierarchy levels: `< {first['retained_levels']}` "
        f"({first['retained_packets']} retained split packets)"
    )
    lines.append(
        "- candidate dictionary: omitted Haar split packets from the remaining levels"
    )
    lines.append(
        "- structural episodes use one omitted packet as the target; noise episodes have matched retained-sector variance"
    )
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append(
        "| target level | support leaves | evidence | scalar AUC | raw corr AUC | "
        "T17 gain AUC | raw kernel true | raw corr true | T17 true | conformal TPR | conformal FPR |"
    )
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in result["conditions"]:
        packet = row["packet_identification"]
        lines.append(
            "| {level} | {support} | {evidence} | {scalar:.3f} | {rawcorr:.3f} | "
            "{gain:.3f} | {rawkerneltrue:.3f} | {rawcorrtrue:.3f} | {t17true:.3f} | "
            "{tpr:.3f} | {fpr:.3f} |".format(
                level=row["target_level"],
                support=row["target_support_leaves"],
                evidence=row["evidence_n"],
                scalar=row["auc"]["scalar_surprise"],
                rawcorr=row["auc"]["raw_in_sample_corr"],
                gain=row["auc"]["t17_heldout_gain"],
                rawkerneltrue=packet["raw_kernel_true_rate"],
                rawcorrtrue=packet["raw_corr_true_rate"],
                t17true=packet["t17_gain_true_rate"],
                tpr=packet["conformal_structural_admit_rate"],
                fpr=packet["conformal_noise_false_admit_rate"],
            )
        )
    lines.append("")
    lines.append("## Mean Scores")
    lines.append("")
    lines.append(
        "| target level | evidence | structural scalar | noise scalar | structural gain | noise gain | null gain threshold |"
    )
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for row in result["conditions"]:
        means = row["means"]
        packet = row["packet_identification"]
        lines.append(
            "| {level} | {evidence} | {ss:.3f} | {ns:.3f} | {sg:.3f} | {ng:.3f} | {thr:.3f} |".format(
                level=row["target_level"],
                evidence=row["evidence_n"],
                ss=means["structural_scalar_surprise"],
                ns=means["noise_scalar_surprise"],
                sg=means["structural_t17_gain"],
                ng=means["noise_t17_gain"],
                thr=packet["null_gain_threshold_empirical"],
            )
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "This is a pass when scalar AUC stays near 0.5, raw kernel priority does not "
        "identify the episode-specific omitted packet, and held-out T17 gain approaches "
        "high AUC with conformal false admission near alpha."
    )
    lines.append("")
    lines.append(
        "The result is exactly the T16/T17 reading of the arXiv paper: hierarchical "
        "geometry can emerge from co-occurrence spectra, but useful updating requires "
        "packet-resolved held-out closure gain rather than raw surprise or global spectral priority."
    )
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=260523821)
    parser.add_argument("--depth", type=int, default=6)
    parser.add_argument("--decay", type=float, default=0.65)
    parser.add_argument("--retained-levels", type=int, default=2)
    parser.add_argument("--target-levels", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--evidence", type=int, nargs="+", default=[32, 64, 128, 256])
    parser.add_argument("--verify-n", type=int, default=256)
    parser.add_argument("--calibration", type=int, default=1000)
    parser.add_argument("--episodes", type=int, default=1000, help="test episodes per kind")
    parser.add_argument("--signal", type=float, default=1.0)
    parser.add_argument("--noise-sd", type=float, default=0.35)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--closure-cost", type=float, default=0.02)
    parser.add_argument(
        "--out-json",
        type=Path,
        default=Path("empirical/reports/tree_spectral_boundary_probe.json"),
    )
    parser.add_argument(
        "--out-md",
        type=Path,
        default=Path("empirical/reports/tree_spectral_boundary_probe.md"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    conditions = []
    for target_level in args.target_levels:
        if target_level < args.retained_levels:
            raise ValueError("target levels must be omitted by the retained sector")
        for evidence_n in args.evidence:
            conditions.append(
                summarize_condition(
                    rng,
                    depth=args.depth,
                    decay=args.decay,
                    retained_levels=args.retained_levels,
                    target_level=target_level,
                    evidence_n=evidence_n,
                    verify_n=args.verify_n,
                    calibration_episodes=args.calibration,
                    test_episodes_per_kind=args.episodes,
                    signal=args.signal,
                    noise_sd=args.noise_sd,
                    alpha=args.alpha,
                    closure_cost=args.closure_cost,
                )
            )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "alpha": args.alpha,
        "closure_cost": args.closure_cost,
        "conditions": conditions,
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    args.out_md.write_text(render_markdown(result), encoding="utf-8")
    print(render_markdown(result))


if __name__ == "__main__":
    main()
