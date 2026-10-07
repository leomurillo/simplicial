"""Structural audit for Paper 28, Theorem 7.2.

This script checks the finite, implementation-facing static preconditions
behind E7--E8 and explicitly defers E6:

E6 kill condition:
  A future dynamical integrator must keep E3_red and L at the integrator floor.
  This script does not integrate dynamics; it records the structural inputs
  required before that test is meaningful.

E7 kill condition:
  If the non-target connected mixed partial is at numerical floor, the chosen
  channels are not functioning as genuinely ternary channels.

E8 kill condition:
  If an SE(3)-invariant eta has rank(Deta) > 3 or more than 3 nonzero
  unreduced Hessian eigenvalues, the implementation is not invariant.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def helmert_fisher_frame(q: int, channels: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """Return uniform p0 and Fisher-orthonormal zero-sum tangent directions."""
    if q - 1 < channels:
        raise ValueError("need simplex dimension at least the number of channels")
    p0 = np.full(q, 1.0 / q)
    raw = []
    for k in range(channels):
        v = np.zeros(q)
        v[: k + 1] = 1.0
        v[k + 1] = -(k + 1)
        v -= v.mean()
        raw.append(v)
    mat = np.stack(raw, axis=1)
    qmat, _ = np.linalg.qr(mat)
    # For uniform p0, g(u,v)=q*u.v, so Euclidean norm must be 1/sqrt(q).
    frame = (qmat[:, :channels] / math.sqrt(q)).T
    return p0, frame


def centered_sample(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    r = rng.normal(size=(3, 3))
    r -= r.mean(axis=0, keepdims=True)
    # Push away from collinearity with a fixed small offset.
    r[2] += np.array([0.17, -0.11, 0.23])
    r -= r.mean(axis=0, keepdims=True)
    return r


def side_data(r: np.ndarray, delta: float) -> dict:
    d12 = np.linalg.norm(r[0] - r[1])
    d23 = np.linalg.norm(r[1] - r[2])
    d31 = np.linalg.norm(r[2] - r[0])
    s12 = math.sqrt(d12 * d12 + delta * delta)
    s23 = math.sqrt(d23 * d23 + delta * delta)
    s31 = math.sqrt(d31 * d31 + delta * delta)
    area16_reg = (
        2 * s12 * s12 * s23 * s23
        + 2 * s23 * s23 * s31 * s31
        + 2 * s31 * s31 * s12 * s12
        - s12**4
        - s23**4
        - s31**4
    )
    area16 = (
        2 * d12 * d12 * d23 * d23
        + 2 * d23 * d23 * d31 * d31
        + 2 * d31 * d31 * d12 * d12
        - d12**4
        - d23**4
        - d31**4
    )
    perimeter_sq = max((d12 + d23 + d31) ** 2, 1.0e-300)
    # Dimensionless triangle quality: 0 at collinearity, O(1) for good triangles.
    quality = math.sqrt(max(area16, 0.0)) / perimeter_sq
    return {
        "d": np.array([d12, d23, d31]),
        "s": np.array([s12, s23, s31]),
        "area16": area16,
        "area16_reg": area16_reg,
        "quality": quality,
    }


def q_values(r: np.ndarray, delta: float) -> np.ndarray:
    data = side_data(r, delta)
    s12, s23, s31 = data["s"]
    area16_reg = data["area16_reg"]
    if area16_reg <= 0:
        raise ValueError("regularized Heron area is nonpositive")
    return np.array(
        [
            math.log(s12 + s23 + s31),
            0.5 * math.log(area16_reg),
            math.log(s12 * s23 * s31),
        ]
    )


def eta(r: np.ndarray, p0: np.ndarray, frame: np.ndarray, delta: float, eps: float) -> np.ndarray:
    qv = q_values(r, delta)
    # psi_alpha(q)=q in this reference audit, so psi'=1.
    return p0 + eps * (qv @ frame)


def numerical_jacobian(fn, x: np.ndarray, step: float) -> np.ndarray:
    flat = x.reshape(-1)
    y_size = fn(x).size
    jac = np.zeros((y_size, flat.size))
    for idx in range(flat.size):
        xp = flat.copy()
        xm = flat.copy()
        xp[idx] += step
        xm[idx] -= step
        jac[:, idx] = (fn(xp.reshape(x.shape)) - fn(xm.reshape(x.shape))) / (2 * step)
    return jac


def gradients_q(r: np.ndarray, delta: float, step: float) -> np.ndarray:
    jac = numerical_jacobian(lambda x: q_values(x, delta), r, step)
    return jac.reshape(3, 3, 3)


def relative_rank(matrix: np.ndarray, rel_tol: float) -> tuple[int, list[float], float]:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    scale = float(singular_values[0]) if singular_values.size else 0.0
    tol = rel_tol * max(scale, 1.0e-300)
    return int(np.sum(singular_values > tol)), singular_values.tolist(), tol


def audit(args: argparse.Namespace) -> dict:
    p0, frame = helmert_fisher_frame(args.outcomes, 3)
    fisher_gram = frame @ np.diag(1.0 / p0) @ frame.T

    samples = []
    for seed in range(args.seeds):
        r = centered_sample(args.seed0 + seed)
        shape = side_data(r, args.delta)
        if shape["quality"] < args.min_shape_quality:
            samples.append(
                {
                    "seed": args.seed0 + seed,
                    "evaluated": False,
                    "skip_reason": "shape quality below nondegenerate-stratum gate",
                    "shape_quality": shape["quality"],
                }
            )
            continue

        eta_r = eta(r, p0, frame, args.delta, args.epsilon)
        if np.any(eta_r <= 0):
            raise ValueError("eta left the simplex; reduce epsilon")

        q_jac = numerical_jacobian(lambda x: q_values(x, args.delta), r, args.fd_step)
        deta = args.epsilon * frame.T @ q_jac
        rank_deta, deta_singular_values, deta_rank_tol = relative_rank(
            deta, args.rel_rank_tol
        )

        fisher = np.diag(1.0 / eta_r)
        hessian_scaled = (deta.T @ fisher @ deta) / max(args.epsilon**2, 1.0e-300)
        h_rank, h_singular_values, h_rank_tol = relative_rank(
            hessian_scaled, args.rel_rank_tol
        )

        grads = q_jac.reshape(3, 3, 3)
        # Reference diagonal C^0_{00}=1 contribution to the i=0, j=1, k=2 tensor.
        connected = 2.0 * args.epsilon**2 * np.einsum(
            "a,b,c->abc", grads[0, 0], grads[0, 1], grads[0, 2]
        )
        connected_norm = float(np.linalg.norm(connected))
        connected_scale = float(
            2.0
            * args.epsilon**2
            * np.linalg.norm(grads[0, 0])
            * np.linalg.norm(grads[0, 1])
            * np.linalg.norm(grads[0, 2])
        )
        connected_ratio = connected_norm / max(connected_scale, 1.0e-300)

        samples.append(
            {
                "seed": args.seed0 + seed,
                "evaluated": True,
                "rank_Deta": rank_deta,
                "Deta_singular_values": deta_singular_values,
                "Deta_relative_tolerance": deta_rank_tol,
                "unreduced_hessian_scaled_rank": h_rank,
                "unreduced_hessian_scaled_singular_values": h_singular_values,
                "unreduced_hessian_relative_tolerance": h_rank_tol,
                "connected_tensor_norm": connected_norm,
                "connected_tensor_scale": connected_scale,
                "connected_tensor_ratio": connected_ratio,
                "shape_quality": shape["quality"],
                "q": q_values(r, args.delta).tolist(),
            }
        )

    kills = []
    evaluated = [s for s in samples if s["evaluated"]]
    if not evaluated:
        kills.append("no samples passed the nondegenerate-stratum shape-quality gate")
        max_rank = 0
        max_h_rank = 0
        min_connected = 0.0
        min_connected_ratio = 0.0
    else:
        max_rank = max(s["rank_Deta"] for s in evaluated)
        max_h_rank = max(s["unreduced_hessian_scaled_rank"] for s in evaluated)
        min_connected = min(s["connected_tensor_norm"] for s in evaluated)
        min_connected_ratio = min(s["connected_tensor_ratio"] for s in evaluated)
    if not np.allclose(fisher_gram, np.eye(3), atol=args.orth_tol):
        kills.append("Fisher Gram(s_alpha) != I_3 within tolerance")
    if max_rank > 3:
        kills.append("rank(Deta_r) exceeded 3, violating Theorem 5.2")
    if max_h_rank > 3:
        kills.append("unreduced Hessian had more than 3 nonzero eigenvalues")
    if evaluated and min_connected_ratio <= args.connected_ratio_floor:
        kills.append("dimensionless connected tensor ratio sat at numerical floor")

    return {
        "kill_conditions": {
            "E6": "NOT EVALUATED HERE: future integrator drift of E3_red or L beyond floor",
            "E7": "evaluated statically: dimensionless connected tensor ratio at numerical floor",
            "E8": "implementation self-test: rank(Deta)>3 or unreduced Hessian rank>3 for invariant eta",
        },
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "fisher_gram": fisher_gram.tolist(),
        "samples": samples,
        "summary": {
            "max_rank_Deta": max_rank,
            "max_unreduced_hessian_rank": max_h_rank,
            "min_connected_tensor_norm": min_connected,
            "min_connected_tensor_ratio": min_connected_ratio,
            "evaluated_samples": len(evaluated),
            "skipped_samples": len(samples) - len(evaluated),
            "E6_status": "NOT_EVALUATED",
            "static_status": "PASS" if not kills else "KILL",
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    summary = result["summary"]
    lines = [
        "# Three-Body Ternary Reduced Static Audit",
        "",
        "This report is a static structural precondition check. It does not integrate",
        "the Theorem 7.2 dynamics and therefore does not evaluate E6.",
        "",
        "## Pre-registered conditions",
        "",
    ]
    for key, value in result["kill_conditions"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- E6 status: {summary['E6_status']}",
            f"- Static E7/E8 status: {summary['static_status']}",
            f"- evaluated samples: {summary['evaluated_samples']}",
            f"- skipped samples: {summary['skipped_samples']}",
            f"- max rank(Deta): {summary['max_rank_Deta']}",
            f"- max epsilon-normalized unreduced Hessian rank: {summary['max_unreduced_hessian_rank']}",
            f"- min raw connected tensor norm: {summary['min_connected_tensor_norm']:.6e}",
            f"- min dimensionless connected tensor ratio: {summary['min_connected_tensor_ratio']:.6e}",
            f"- kills: {summary['kills']}",
            "",
            "## Samples",
            "",
            "| seed | used | quality | rank(Deta) | Hessian rank | connected ratio | raw connected norm |",
            "|---:|:---:|---:|---:|---:|---:|---:|",
        ]
    )
    for sample in result["samples"]:
        if not sample["evaluated"]:
            lines.append(
                f"| {sample['seed']} | no | {sample['shape_quality']:.6e} | -- | -- | -- | -- |"
            )
        else:
            lines.append(
                "| {seed} | yes | {shape_quality:.6e} | {rank_Deta} | "
                "{unreduced_hessian_scaled_rank} | {connected_tensor_ratio:.6e} | "
                "{connected_tensor_norm:.6e} |".format(**sample)
            )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outcomes", type=int, default=6)
    parser.add_argument("--delta", type=float, default=0.15)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--seeds", type=int, default=8)
    parser.add_argument("--seed0", type=int, default=2800)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--rel-rank-tol", type=float, default=1.0e-8)
    parser.add_argument("--orth-tol", type=float, default=1.0e-10)
    parser.add_argument("--connected-ratio-floor", type=float, default=1.0e-8)
    parser.add_argument("--min-shape-quality", type=float, default=1.0e-3)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/three_body_ternary_reduced_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/three_body_ternary_reduced_audit.json"),
    )
    args = parser.parse_args()

    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
