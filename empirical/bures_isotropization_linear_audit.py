"""Finite linearization audit for the CRT/Bures isotropization lemma.

The audit tests the principal-symbol fork before any Mosco-limit theorem is
attempted.  For each squarefree CRT row, it builds a declared physical quotient
xi_n, computes the second jump-moment tensor

    M = E_x sum_y c(x,y) (xi_y - xi_x)(xi_y - xi_x)^T,

and records the anisotropy

    A = (lambda_max - lambda_min) / (lambda_max + lambda_min).

The diagonal-only tower is modeled by cyclic nearest-neighbor conductances on
each CRT leg.  The Bures off-diagonal linearization is modeled by the complete
set of leg-local matrix-unit coherences, with SLD/Bures leg normalization.
The script also reports normalized fourth jump moments, because isotropic
complete-graph symbols can still fail locality.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy.spatial import cKDTree


DEFAULT_REPORT = Path("empirical/reports/bures_isotropization_linear_audit.md")
DEFAULT_JSON = Path("empirical/reports/bures_isotropization_linear_audit.json")


@dataclass(frozen=True)
class Edge:
    i: int
    j: int
    weight: float


def parse_rows(text: str) -> list[int]:
    return [int(item.strip()) for item in text.split(",") if item.strip()]


def prime_factors_squarefree(n: int) -> tuple[int, ...]:
    factors: list[int] = []
    value = n
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            factors.append(factor)
            value //= factor
            if value % factor == 0:
                raise ValueError(f"row {n} is not squarefree")
        factor += 1 if factor == 2 else 2
    if value > 1:
        factors.append(value)
    product_value = 1
    for factor in factors:
        product_value *= factor
    if product_value != n:
        raise ValueError(f"could not factor row {n}")
    return tuple(factors)


def crt_states(primes: tuple[int, ...]) -> list[tuple[int, ...]]:
    return list(product(*[range(p) for p in primes]))


def state_index(states: list[tuple[int, ...]]) -> dict[tuple[int, ...], int]:
    return {state: idx for idx, state in enumerate(states)}


def helmert_average_orthonormal(p: int) -> np.ndarray:
    """Columns have zero mean and average inner product delta_ij."""
    cols: list[np.ndarray] = []
    for j in range(p - 1):
        col = np.zeros(p, dtype=float)
        scale = math.sqrt(p / ((j + 1) * (j + 2)))
        col[: j + 1] = scale
        col[j + 1] = -(j + 1) * scale
        cols.append(col)
    return np.column_stack(cols) if cols else np.zeros((p, 0), dtype=float)


def leg_mode_columns(primes: tuple[int, ...], states: list[tuple[int, ...]]) -> list[dict[str, Any]]:
    columns: list[dict[str, Any]] = []
    for leg, p in enumerate(primes):
        h = helmert_average_orthonormal(p)
        for mode in range(h.shape[1]):
            values = np.array([h[state[leg], mode] for state in states], dtype=float)
            columns.append(
                {
                    "leg": leg,
                    "prime": p,
                    "mode": mode,
                    "values": values,
                    "label": f"p{p}:h{mode + 1}",
                }
            )
    return columns


def real_fourier_average_orthonormal(p: int) -> tuple[np.ndarray, list[str]]:
    """Real Fourier columns with zero mean and average inner product delta_ij."""
    x = np.arange(p, dtype=float)
    columns: list[np.ndarray] = []
    labels: list[str] = []
    for k in range(1, p // 2 + 1):
        if 2 * k == p:
            columns.append(((-1.0) ** x).astype(float))
            labels.append(f"f{k}r")
        else:
            theta = 2.0 * math.pi * k * x / p
            columns.append(math.sqrt(2.0) * np.cos(theta))
            labels.append(f"f{k}c")
            columns.append(math.sqrt(2.0) * np.sin(theta))
            labels.append(f"f{k}s")
    return np.column_stack(columns) if columns else np.zeros((p, 0), dtype=float), labels


def leg_fourier_columns(primes: tuple[int, ...], states: list[tuple[int, ...]]) -> list[dict[str, Any]]:
    columns: list[dict[str, Any]] = []
    for leg, p in enumerate(primes):
        basis, labels = real_fourier_average_orthonormal(p)
        for mode, label in enumerate(labels):
            values = np.array([basis[state[leg], mode] for state in states], dtype=float)
            columns.append(
                {
                    "leg": leg,
                    "prime": p,
                    "mode": mode,
                    "values": values,
                    "label": f"p{p}:{label}",
                }
            )
    return columns


def leg_residue_columns(primes: tuple[int, ...], states: list[tuple[int, ...]]) -> list[dict[str, Any]]:
    columns: list[dict[str, Any]] = []
    for leg, p in enumerate(primes):
        values = np.array([state[leg] for state in states], dtype=float)
        values = values - float(np.mean(values))
        scale = math.sqrt(float(np.mean(values * values)))
        values = values / max(scale, 1.0e-300)
        columns.append(
            {
                "leg": leg,
                "prime": p,
                "mode": 0,
                "values": values,
                "label": f"p{p}:res",
            }
        )
    return columns


def select_xi_columns(columns: list[dict[str, Any]], primes: tuple[int, ...], mode: str, dim: int) -> list[dict[str, Any]]:
    if mode == "sector_fill":
        selected = columns[:dim]
    elif mode == "prime_first":
        selected = []
        for leg, _prime in enumerate(primes):
            for col in columns:
                if col["leg"] == leg and col["mode"] == 0:
                    selected.append(col)
                    break
            if len(selected) == dim:
                break
        if len(selected) < dim:
            for col in columns:
                if col not in selected:
                    selected.append(col)
                    if len(selected) == dim:
                        break
    elif mode == "largest_prime_modes":
        largest = max(primes)
        selected = [col for col in columns if col["prime"] == largest][:dim]
    elif mode == "largest_primes":
        selected = []
        for prime in sorted(primes, reverse=True):
            for col in columns:
                if col["prime"] == prime and col["mode"] == 0:
                    selected.append(col)
                    break
            if len(selected) == dim:
                break
    else:
        raise ValueError(f"unknown xi mode: {mode}")
    if len(selected) < dim:
        raise ValueError(f"row has only {len(selected)} quotient columns; need {dim}")
    return selected


def whiten_columns(values: np.ndarray) -> np.ndarray:
    centered = values - np.mean(values, axis=0, keepdims=True)
    cov = centered.T @ centered / centered.shape[0]
    eigvals, eigvecs = np.linalg.eigh(cov)
    if float(np.min(eigvals)) <= 1.0e-12:
        raise ValueError(f"singular quotient covariance: {eigvals}")
    inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
    return centered @ inv_sqrt


def build_xi(
    primes: tuple[int, ...],
    states: list[tuple[int, ...]],
    mode: str,
    dim: int,
    basis: str,
) -> tuple[np.ndarray, list[str]]:
    if basis == "helmert":
        columns = leg_mode_columns(primes, states)
    elif basis == "fourier":
        columns = leg_fourier_columns(primes, states)
    elif basis == "residue":
        columns = leg_residue_columns(primes, states)
    else:
        raise ValueError(f"unknown quotient basis: {basis}")
    selected = select_xi_columns(columns, primes, mode, dim)
    raw = np.column_stack([col["values"] for col in selected])
    xi = whiten_columns(raw)
    return xi, [str(col["label"]) for col in selected]


def leg_weight(p: int, scaling: str) -> float:
    if scaling == "raw":
        return 1.0
    if scaling == "sld":
        return 1.0 / float(p)
    if scaling == "variance":
        return 1.0 / max(float(p - 1), 1.0)
    raise ValueError(f"unknown scaling: {scaling}")


def add_edge_once(edges: dict[tuple[int, int], float], i: int, j: int, weight: float) -> None:
    if i == j:
        return
    key = (i, j) if i < j else (j, i)
    edges[key] = edges.get(key, 0.0) + weight


def cycle_leg_edges(
    states: list[tuple[int, ...]],
    indices: dict[tuple[int, ...], int],
    primes: tuple[int, ...],
    scaling: str,
) -> list[Edge]:
    edges: dict[tuple[int, int], float] = {}
    for i, state in enumerate(states):
        for leg, p in enumerate(primes):
            if p == 2 and state[leg] != 0:
                continue
            nxt = list(state)
            nxt[leg] = (nxt[leg] + 1) % p
            j = indices[tuple(nxt)]
            add_edge_once(edges, i, j, leg_weight(p, scaling))
    return [Edge(i, j, w) for (i, j), w in sorted(edges.items())]


def parse_bandwidth_spec(spec: str, p: int) -> int:
    item = spec.strip().lower()
    if item in {"complete", "full"}:
        return p // 2
    if item == "sqrt":
        return max(1, int(math.floor(math.sqrt(p))))
    if item.startswith("pow:"):
        exponent = float(item.split(":", 1)[1])
        return max(1, int(math.floor(p**exponent)))
    if item.startswith("frac:"):
        fraction = float(item.split(":", 1)[1])
        return max(1, int(math.floor(fraction * p)))
    return int(item)


def parse_bandwidths(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def banded_leg_edges(
    states: list[tuple[int, ...]],
    indices: dict[tuple[int, ...], int],
    primes: tuple[int, ...],
    scaling: str,
    bandwidth_spec: str,
) -> list[Edge]:
    edges: dict[tuple[int, int], float] = {}
    for i, state in enumerate(states):
        for leg, p in enumerate(primes):
            bandwidth = min(parse_bandwidth_spec(bandwidth_spec, p), p // 2)
            if bandwidth <= 0:
                continue
            weight = leg_weight(p, scaling)
            for distance in range(1, bandwidth + 1):
                nxt = list(state)
                nxt[leg] = (nxt[leg] + distance) % p
                if 2 * distance == p and state[leg] > nxt[leg]:
                    continue
                add_edge_once(edges, i, indices[tuple(nxt)], weight)
    return [Edge(i, j, w) for (i, j), w in sorted(edges.items())]


def complete_leg_edges(
    states: list[tuple[int, ...]],
    indices: dict[tuple[int, ...], int],
    primes: tuple[int, ...],
    scaling: str,
) -> list[Edge]:
    edges: dict[tuple[int, int], float] = {}
    for leg, p in enumerate(primes):
        weight = leg_weight(p, scaling)
        fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
        for state in states:
            key = state[:leg] + state[leg + 1 :]
            fibers.setdefault(key, []).append(state)
        for fiber in fibers.values():
            for left_state, right_state in combinations(fiber, 2):
                add_edge_once(edges, indices[left_state], indices[right_state], weight)
    return [Edge(i, j, w) for (i, j), w in sorted(edges.items())]


def global_complete_edges(n: int, scaling: str) -> list[Edge]:
    weight = 1.0 / float(n) if scaling == "sld" else 1.0
    return [Edge(i, j, weight) for i, j in combinations(range(n), 2)]


def moment_stats(xi: np.ndarray, edges: Iterable[Edge]) -> dict[str, Any]:
    n, dim = xi.shape
    symbol = np.zeros((dim, dim), dtype=float)
    point_symbols = np.zeros((n, dim, dim), dtype=float)
    fourth = 0.0
    point_fourth = np.zeros(n, dtype=float)
    total_weight = 0.0
    edge_count = 0
    for edge in edges:
        delta = xi[edge.j] - xi[edge.i]
        outer = np.outer(delta, delta)
        norm_sq = float(delta @ delta)
        contribution = edge.weight * outer
        point_symbols[edge.i] += contribution
        point_symbols[edge.j] += contribution
        point_fourth[edge.i] += edge.weight * norm_sq * norm_sq
        point_fourth[edge.j] += edge.weight * norm_sq * norm_sq
        symbol += 2.0 * contribution / n
        fourth += 2.0 * edge.weight * norm_sq * norm_sq / n
        total_weight += edge.weight
        edge_count += 1
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    denom = float(eigvals[-1] + eigvals[0])
    anisotropy = float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf")
    trace = float(np.trace(symbol))
    point_anisotropies: list[float] = []
    for px in point_symbols:
        pe = np.linalg.eigvalsh(0.5 * (px + px.T))
        pdenom = float(pe[-1] + pe[0])
        point_anisotropies.append(float((pe[-1] - pe[0]) / pdenom) if pdenom > 1.0e-15 else float("inf"))
    return {
        "edge_count": edge_count,
        "total_edge_weight": total_weight,
        "symbol": symbol.tolist(),
        "eigenvalues": eigvals.tolist(),
        "trace": trace,
        "anisotropy": anisotropy,
        "mean_point_anisotropy": float(np.mean(point_anisotropies)),
        "max_point_anisotropy": float(np.max(point_anisotropies)),
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
        "mean_point_fourth_moment": float(np.mean(point_fourth)),
        "max_point_fourth_moment": float(np.max(point_fourth)),
    }


def moment_stats_from_pairs(xi: np.ndarray, pairs: np.ndarray) -> dict[str, Any]:
    n, dim = xi.shape
    if pairs.size == 0:
        return {
            "edge_count": 0,
            "symbol": [[0.0 for _ in range(dim)] for _ in range(dim)],
            "eigenvalues": [],
            "trace": 0.0,
            "anisotropy": float("inf"),
            "fourth_moment": 0.0,
            "normalized_fourth_moment": float("inf"),
        }
    deltas = xi[pairs[:, 1]] - xi[pairs[:, 0]]
    symbol = 2.0 * np.einsum("ni,nj->ij", deltas, deltas) / n
    norm_sq = np.einsum("ni,ni->n", deltas, deltas)
    fourth = float(2.0 * np.sum(norm_sq * norm_sq) / n)
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    denom = float(eigvals[-1] + eigvals[0])
    anisotropy = float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf")
    trace = float(np.trace(symbol))
    return {
        "edge_count": int(pairs.shape[0]),
        "symbol": symbol.tolist(),
        "eigenvalues": eigvals.tolist(),
        "trace": trace,
        "anisotropy": anisotropy,
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
    }


def target_radius(state_count: int, distinct_count: int, args: argparse.Namespace) -> float:
    denominator = state_count if args.target_mesh_denominator == "row" else distinct_count
    return args.target_h_scale * float(denominator) ** (-1.0 / 3.0)


def distinct_xi_count(xi: np.ndarray, decimals: int = 12) -> int:
    rounded = np.round(xi, decimals=decimals)
    return int(np.unique(rounded, axis=0).shape[0])


def target_local_pairs(xi: np.ndarray, radius: float, max_pairs: int) -> np.ndarray:
    pairs = cKDTree(xi).query_pairs(radius, output_type="ndarray")
    if pairs.shape[0] > max_pairs:
        raise RuntimeError(f"target-local pair count {pairs.shape[0]} exceeds cap {max_pairs}")
    return np.asarray(pairs, dtype=np.int64)


def leg_class(
    left: tuple[int, ...],
    right: tuple[int, ...],
    primes: tuple[int, ...],
) -> tuple[int, int] | None:
    changed = [idx for idx, (a, b) in enumerate(zip(left, right)) if a != b]
    if len(changed) != 1:
        return None
    leg = changed[0]
    p = primes[leg]
    forward = (right[leg] - left[leg]) % p
    backward = (left[leg] - right[leg]) % p
    distance = min(forward, backward)
    return (leg, distance)


def leg_class_sizes(state_count: int, primes: tuple[int, ...]) -> dict[tuple[int, int], int]:
    sizes: dict[tuple[int, int], int] = {}
    for leg, p in enumerate(primes):
        fibers = state_count // p
        for distance in range(1, p // 2 + 1):
            cycle_edges = p // 2 if 2 * distance == p else p
            sizes[(leg, distance)] = fibers * cycle_edges
    return sizes


def bures_projection_residuals(
    pairs: np.ndarray,
    states: list[tuple[int, ...]],
    primes: tuple[int, ...],
) -> dict[str, Any]:
    target_count = int(pairs.shape[0])
    if target_count == 0:
        return {
            "target_edge_count": 0,
            "admissible_edge_count": 0,
            "admissible_fraction": 0.0,
            "support_residual": float("inf"),
            "class_cone_residual": float("inf"),
            "class_counts": {},
        }
    class_sizes = leg_class_sizes(len(states), primes)
    class_counts: dict[tuple[int, int], int] = defaultdict(int)
    admissible = 0
    for i, j in pairs:
        cls = leg_class(states[int(i)], states[int(j)], primes)
        if cls is not None:
            admissible += 1
            class_counts[cls] += 1
    support_residual = math.sqrt(max(target_count - admissible, 0) / target_count)
    projection_energy = 0.0
    for cls, count in class_counts.items():
        projection_energy += (count * count) / max(class_sizes[cls], 1)
    class_residual = math.sqrt(max(target_count - projection_energy, 0.0) / target_count)
    return {
        "target_edge_count": target_count,
        "admissible_edge_count": admissible,
        "admissible_fraction": admissible / target_count,
        "support_residual": support_residual,
        "class_cone_residual": class_residual,
        "class_counts": {f"leg{leg}:d{distance}": count for (leg, distance), count in sorted(class_counts.items())},
    }


def target_local_result(
    xi: np.ndarray,
    states: list[tuple[int, ...]],
    primes: tuple[int, ...],
    args: argparse.Namespace,
) -> dict[str, Any]:
    distinct_count = distinct_xi_count(xi)
    radius = target_radius(len(states), distinct_count, args)
    pairs = target_local_pairs(xi, radius, args.max_target_pairs)
    stats = moment_stats_from_pairs(xi, pairs)
    residuals = bures_projection_residuals(pairs, states, primes)
    return {
        "model": "target-local indicator kernel in pushed xi-space",
        "radius": radius,
        "h_scale": args.target_h_scale,
        "mesh_denominator": args.target_mesh_denominator,
        "distinct_xi_count": distinct_count,
        **stats,
        "bures_projection": residuals,
    }


def row_audit(row: int, args: argparse.Namespace) -> dict[str, Any]:
    primes = prime_factors_squarefree(row)
    states = crt_states(primes)
    indices = state_index(states)
    xi, xi_labels = build_xi(primes, states, args.xi_mode, args.dimension, args.quotient_basis)
    diag_edges = cycle_leg_edges(states, indices, primes, args.diag_scaling)
    bures_edges = complete_leg_edges(states, indices, primes, args.bures_scaling)
    diag_stats = moment_stats(xi, diag_edges)
    bures_stats = moment_stats(xi, bures_edges)
    if len(states) <= args.global_control_max_states:
        global_edges = global_complete_edges(len(states), args.bures_scaling)
        global_stats = moment_stats(xi, global_edges)
    else:
        global_stats = None
    banded_results = []
    for spec in parse_bandwidths(args.bandwidths):
        band_edges = banded_leg_edges(states, indices, primes, args.bures_scaling, spec)
        band_stats = moment_stats(xi, band_edges)
        banded_results.append(
            {
                "spec": spec,
                "model": f"CRT leg cyclic band, bandwidth={spec}, scaling={args.bures_scaling}",
                **band_stats,
            }
        )
    target_result = None
    if args.target_local:
        try:
            target_result = target_local_result(xi, states, primes, args)
        except RuntimeError as exc:
            target_result = {"model": "target-local indicator kernel in pushed xi-space", "skipped": str(exc)}
    return {
        "row": row,
        "primes": primes,
        "state_count": len(states),
        "xi_mode": args.xi_mode,
        "quotient_basis": args.quotient_basis,
        "xi_labels": xi_labels,
        "diag_model": f"CRT leg cycles, scaling={args.diag_scaling}",
        "bures_model": f"CRT leg complete off-diagonal coherences, scaling={args.bures_scaling}",
        "global_complete_control": f"all pairs, scaling={args.bures_scaling}",
        "diag": diag_stats,
        "bures": bures_stats,
        "global_complete": global_stats,
        "banded": banded_results,
        "target_local": target_result,
    }


def audit(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_rows(args.rows)
    row_results = [row_audit(row, args) for row in rows]
    kills: list[str] = []
    if len(row_results) >= 2:
        first = row_results[0]
        last = row_results[-1]
        if last["bures"]["anisotropy"] > first["bures"]["anisotropy"] + args.decay_slack:
            kills.append("Bures anisotropy increased along the tested refinement")
        if last["bures"]["anisotropy"] >= last["diag"]["anisotropy"]:
            kills.append("Bures anisotropy is not below diagonal anisotropy on the finest tested row")
        if last["bures"]["normalized_fourth_moment"] > first["bures"]["normalized_fourth_moment"] + args.decay_slack:
            kills.append("Bures normalized fourth moment increased along the tested refinement")
    if row_results[-1]["bures"]["anisotropy"] > args.bures_anisotropy_tol:
        kills.append("Bures principal-symbol anisotropy exceeds tolerance on the finest tested row")
    if row_results[-1]["diag"]["anisotropy"] < args.diag_anisotropy_floor:
        kills.append("Diagonal anisotropy is not bounded away from zero on the finest tested row")
    return {
        "claim_tested": "finite-n linearization of the CRT/Bures isotropization lemma",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "rows": row_results,
        "summary": {
            "status": "PASS_LINEAR_SYMBOL" if not kills else "KILL_OR_INCONCLUSIVE",
            "kills": kills,
            "finest_row": row_results[-1]["row"],
            "finest_diag_anisotropy": row_results[-1]["diag"]["anisotropy"],
            "finest_bures_anisotropy": row_results[-1]["bures"]["anisotropy"],
            "finest_global_complete_anisotropy": (
                row_results[-1]["global_complete"]["anisotropy"]
                if row_results[-1]["global_complete"] is not None
                else None
            ),
            "finest_bures_normalized_fourth": row_results[-1]["bures"]["normalized_fourth_moment"],
            "finest_diag_normalized_fourth": row_results[-1]["diag"]["normalized_fourth_moment"],
            "finest_target_local_class_residual": (
                row_results[-1]["target_local"]["bures_projection"]["class_cone_residual"]
                if row_results[-1].get("target_local")
                and "bures_projection" in row_results[-1]["target_local"]
                else None
            ),
            "finest_target_local_support_residual": (
                row_results[-1]["target_local"]["bures_projection"]["support_residual"]
                if row_results[-1].get("target_local")
                and "bures_projection" in row_results[-1]["target_local"]
                else None
            ),
        },
    }


def fmt(value: float) -> str:
    return f"{value:.6e}"


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Bures Isotropization Linear Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- Finest row: {s['finest_row']}",
        f"- Finest diagonal anisotropy: {fmt(s['finest_diag_anisotropy'])}",
        f"- Finest Bures anisotropy: {fmt(s['finest_bures_anisotropy'])}",
        "- Finest global-complete control anisotropy: "
        + (
            fmt(s["finest_global_complete_anisotropy"])
            if s["finest_global_complete_anisotropy"] is not None
            else "skipped"
        ),
        f"- Finest diagonal normalized fourth moment: {fmt(s['finest_diag_normalized_fourth'])}",
        f"- Finest Bures normalized fourth moment: {fmt(s['finest_bures_normalized_fourth'])}",
        "- Finest target-local support residual: "
        + (
            fmt(s["finest_target_local_support_residual"])
            if s["finest_target_local_support_residual"] is not None
            else "not run"
        ),
        "- Finest target-local class-cone residual: "
        + (
            fmt(s["finest_target_local_class_residual"])
            if s["finest_target_local_class_residual"] is not None
            else "not run"
        ),
        f"- Kills/inconclusive flags: {s['kills']}",
        "",
        "## Pre-registered Models",
        "",
        "- Diagonal-only: cyclic nearest-neighbor conductances on each CRT leg.",
        "- Bures: complete leg-local off-diagonal matrix-unit coherences with SLD leg normalization.",
        "- Global-complete: all-pairs control; useful because it isotropizes any whitened quotient but is not CRT-local.",
        "",
        "## Row Results",
        "",
        "| row | xi labels | diag A | Bures A | global A | diag q4 | Bures q4 |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in result["rows"]:
        lines.append(
            "| {row} | `{labels}` | {diag_a} | {bures_a} | {glob_a} | {diag_q4} | {bures_q4} |".format(
                row=row["row"],
                labels=row["xi_labels"],
                diag_a=fmt(row["diag"]["anisotropy"]),
                bures_a=fmt(row["bures"]["anisotropy"]),
                glob_a=(
                    fmt(row["global_complete"]["anisotropy"])
                    if row["global_complete"] is not None
                    else "skipped"
                ),
                diag_q4=fmt(row["diag"]["normalized_fourth_moment"]),
                bures_q4=fmt(row["bures"]["normalized_fourth_moment"]),
            )
        )
    if any(row["banded"] for row in result["rows"]):
        lines.extend(
            [
                "",
                "## Banded Sweep",
                "",
                "| row | bandwidth | A | q4 | edges |",
                "|---:|---|---:|---:|---:|",
            ]
        )
        for row in result["rows"]:
            for band in row["banded"]:
                lines.append(
                    "| {row} | `{spec}` | {a} | {q4} | {edges} |".format(
                        row=row["row"],
                        spec=band["spec"],
                        a=fmt(band["anisotropy"]),
                        q4=fmt(band["normalized_fourth_moment"]),
                        edges=band["edge_count"],
                    )
                )
    lines.extend(
        [
            "",
            "## Target-Local Kernel",
            "",
        ]
    )
    if any(row.get("target_local") for row in result["rows"]):
        lines.extend(
            [
                "| row | radius | target edges | A | q4 | support residual | class residual | admissible fraction |",
                "|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in result["rows"]:
            target = row.get("target_local")
            if not target:
                lines.append(f"| {row['row']} | -- | -- | -- | -- | -- | -- | -- |")
            elif "skipped" in target:
                lines.append(f"| {row['row']} | skipped | `{target['skipped']}` | -- | -- | -- | -- | -- |")
            else:
                projection = target["bures_projection"]
                lines.append(
                    "| {row} | {radius} | {edges} | {a} | {q4} | {support} | {klass} | {frac} |".format(
                        row=row["row"],
                        radius=fmt(target["radius"]),
                        edges=target["edge_count"],
                        a=fmt(target["anisotropy"]),
                        q4=fmt(target["normalized_fourth_moment"]),
                        support=fmt(projection["support_residual"]),
                        klass=fmt(projection["class_cone_residual"]),
                        frac=fmt(projection["admissible_fraction"]),
                    )
                )
    else:
        lines.append("Target-local kernel was not run. Use `--target-local` to enable it.")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The complete leg-local Bures model is the isotropic mean-field",
            "endpoint; its normalized fourth moment is therefore the locality",
            "obstruction.  The banded sweep exposes the source-local tradeoff:",
            "narrow bands preserve some locality but remain anisotropic, while",
            "isotropizing bands fall back to the complete-leg fourth-moment floor.",
            "When `--target-local` is enabled, the final columns measure the new",
            "bridge: distance from a target-local pushed kernel to the diagonal",
            "shadow cone of Bures-admissible leg matrix units.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", default="6,30")
    parser.add_argument("--dimension", type=int, default=3)
    parser.add_argument(
        "--xi-mode",
        choices=["sector_fill", "prime_first", "largest_prime_modes", "largest_primes"],
        default="prime_first",
    )
    parser.add_argument("--quotient-basis", choices=["helmert", "fourier", "residue"], default="helmert")
    parser.add_argument("--diag-scaling", choices=["raw", "sld", "variance"], default="raw")
    parser.add_argument("--bures-scaling", choices=["raw", "sld", "variance"], default="sld")
    parser.add_argument("--bandwidths", default="1,2,sqrt,complete")
    parser.add_argument("--global-control-max-states", type=int, default=1000)
    parser.add_argument("--target-local", action="store_true")
    parser.add_argument("--target-h-scale", type=float, default=3.0)
    parser.add_argument("--target-mesh-denominator", choices=["row", "distinct"], default="row")
    parser.add_argument("--max-target-pairs", type=int, default=2_000_000)
    parser.add_argument("--bures-anisotropy-tol", type=float, default=1.0e-10)
    parser.add_argument("--diag-anisotropy-floor", type=float, default=1.0e-3)
    parser.add_argument("--decay-slack", type=float, default=1.0e-12)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
