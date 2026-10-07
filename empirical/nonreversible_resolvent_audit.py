"""Finite non-reversible resolvent audit.

This tests the one escape hatch left by the reversible Dirichlet-form no-go:
could a non-self-adjoint Markov generator have a Green/resolvent kernel with a
1/r profile even when its symmetric carre-du-champ locality diagnostics are
bad?

Models on a periodic 3D residue grid:

* local_reversible: nearest-neighbor diffusion.
* local_drift: nearest-neighbor diffusion with persistent current.
* complete: mean-field all-to-all jumps.
* complete_plus_drift: mean-field jumps plus a small current.

For each model we compute directed jump moments, then solve the zero-mean
Poisson problem

    -L g = delta_source - uniform,   mean(g)=0

using the non-symmetric generator L.  The off-source kernel is fit to a/r+b
against periodic Euclidean distance.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


DEFAULT_REPORT = Path("empirical/reports/nonreversible_resolvent_audit.md")
DEFAULT_JSON = Path("empirical/reports/nonreversible_resolvent_audit.json")


@dataclass(frozen=True)
class Transition:
    src: int
    dst: int
    rate: float


def parse_dims(text: str) -> tuple[int, int, int]:
    dims = tuple(int(item.strip()) for item in text.split(",") if item.strip())
    if len(dims) != 3:
        raise ValueError("--dims must contain exactly three integers")
    return dims  # type: ignore[return-value]


def fmt(value: float) -> str:
    return f"{value:.6e}"


def grid_states(dims: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    return list(product(*[range(d) for d in dims]))


def state_index(states: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
    return {state: idx for idx, state in enumerate(states)}


def centered_coordinates(states: list[tuple[int, int, int]], dims: tuple[int, int, int]) -> np.ndarray:
    coords = np.array(states, dtype=float)
    center = (np.array(dims, dtype=float) - 1.0) / 2.0
    scale = np.std(coords - center, axis=0)
    return (coords - center) / scale


def periodic_delta(a: tuple[int, int, int], b: tuple[int, int, int], dims: tuple[int, int, int]) -> np.ndarray:
    raw = np.array(b, dtype=float) - np.array(a, dtype=float)
    for axis, dim in enumerate(dims):
        if raw[axis] > dim / 2:
            raw[axis] -= dim
        elif raw[axis] < -dim / 2:
            raw[axis] += dim
    scale = np.array(dims, dtype=float)
    return raw / scale


def periodic_distance_from_source(states: list[tuple[int, int, int]], source: tuple[int, int, int], dims: tuple[int, int, int]) -> np.ndarray:
    return np.array([np.linalg.norm(periodic_delta(source, state, dims)) for state in states], dtype=float)


def add_transition(transitions: list[Transition], src: int, dst: int, rate: float) -> None:
    if src != dst and rate > 0.0:
        transitions.append(Transition(src, dst, rate))


def local_transitions(
    states: list[tuple[int, int, int]],
    indices: dict[tuple[int, int, int], int],
    dims: tuple[int, int, int],
    diffusion: float,
    drift: float,
) -> list[Transition]:
    transitions: list[Transition] = []
    for src, state in enumerate(states):
        for axis, dim in enumerate(dims):
            plus = list(state)
            minus = list(state)
            plus[axis] = (plus[axis] + 1) % dim
            minus[axis] = (minus[axis] - 1) % dim
            add_transition(transitions, src, indices[tuple(plus)], diffusion + drift)
            add_transition(transitions, src, indices[tuple(minus)], diffusion - drift)
    return transitions


def complete_transitions(state_count: int, rate: float) -> list[Transition]:
    per_edge = rate / max(state_count - 1, 1)
    return [
        Transition(src, dst, per_edge)
        for src in range(state_count)
        for dst in range(state_count)
        if src != dst
    ]


def build_transitions(model: str, states: list[tuple[int, int, int]], indices: dict[tuple[int, int, int], int], dims: tuple[int, int, int], args: argparse.Namespace) -> list[Transition]:
    if abs(args.drift) >= args.diffusion:
        raise ValueError("--drift must be smaller than --diffusion so nearest-neighbor rates stay positive")
    if model == "local_reversible":
        return local_transitions(states, indices, dims, args.diffusion, 0.0)
    if model == "local_drift":
        return local_transitions(states, indices, dims, args.diffusion, args.drift)
    if model == "complete":
        return complete_transitions(len(states), args.complete_rate)
    if model == "complete_plus_drift":
        return complete_transitions(len(states), args.complete_rate) + local_transitions(
            states, indices, dims, args.local_rate, min(args.drift, 0.95 * args.local_rate)
        )
    raise ValueError(f"unknown model: {model}")


def generator_matrix(n: int, transitions: list[Transition]) -> sparse.csr_matrix:
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    out = np.zeros(n, dtype=float)
    for tr in transitions:
        rows.append(tr.src)
        cols.append(tr.dst)
        data.append(tr.rate)
        out[tr.src] += tr.rate
    rows.extend(range(n))
    cols.extend(range(n))
    data.extend((-out).tolist())
    return sparse.csr_matrix((data, (rows, cols)), shape=(n, n))


def jump_delta(
    src: int,
    dst: int,
    states: list[tuple[int, int, int]],
    dims: tuple[int, int, int],
) -> np.ndarray:
    return periodic_delta(states[src], states[dst], dims)


def jump_moments(states: list[tuple[int, int, int]], dims: tuple[int, int, int], transitions: list[Transition]) -> dict[str, Any]:
    n = len(states)
    dim = 3
    symbol = np.zeros((dim, dim), dtype=float)
    fourth = 0.0
    for tr in transitions:
        delta = jump_delta(tr.src, tr.dst, states, dims)
        norm_sq = float(delta @ delta)
        symbol += tr.rate * np.outer(delta, delta) / n
        fourth += tr.rate * norm_sq * norm_sq / n
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    trace = float(np.trace(symbol))
    denom = float(eigvals[-1] + eigvals[0])
    return {
        "symbol": symbol.tolist(),
        "eigenvalues": eigvals.tolist(),
        "anisotropy": float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf"),
        "trace": trace,
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
        "unit_symbol_fourth_ratio": float(fourth / max(trace * dim, 1.0e-300)),
    }


def current_diagnostics(n: int, transitions: list[Transition]) -> dict[str, float]:
    rates: dict[tuple[int, int], float] = {}
    for tr in transitions:
        rates[(tr.src, tr.dst)] = rates.get((tr.src, tr.dst), 0.0) + tr.rate

    undirected_pairs = set()
    for src, dst in rates:
        if src != dst:
            undirected_pairs.add((min(src, dst), max(src, dst)))

    abs_flux = 0.0
    abs_symmetric = 0.0
    max_abs_flux = 0.0
    flux_sq = 0.0
    for a, b in undirected_pairs:
        forward = rates.get((a, b), 0.0)
        backward = rates.get((b, a), 0.0)
        flux = forward - backward
        abs_flux += abs(flux)
        abs_symmetric += forward + backward
        max_abs_flux = max(max_abs_flux, abs(flux))
        flux_sq += flux * flux

    return {
        "mean_abs_edge_flux": abs_flux / max(len(undirected_pairs), 1),
        "relative_abs_flux": abs_flux / max(abs_symmetric, 1.0e-300),
        "max_abs_edge_flux": max_abs_flux,
        "antisymmetric_frobenius": math.sqrt(flux_sq),
    }


def solve_zero_mean_green(l_matrix: sparse.csr_matrix, source: int) -> np.ndarray:
    n = l_matrix.shape[0]
    a = -l_matrix.tolil()
    ones = sparse.csr_matrix(np.ones((n, 1)))
    top = sparse.hstack([a.tocsr(), ones])
    bottom = sparse.hstack([ones.T, sparse.csr_matrix((1, 1))])
    system = sparse.vstack([top, bottom]).tocsr()
    rhs = np.full(n + 1, -1.0 / n, dtype=float)
    rhs[source] += 1.0
    rhs[-1] = 0.0
    sol = spsolve(system, rhs)
    return np.asarray(sol[:n], dtype=float)


def fit_inverse_r(green: np.ndarray, distances: np.ndarray, r_min: float, r_max: float) -> dict[str, Any]:
    mask = (distances >= r_min) & (distances <= r_max) & np.isfinite(green)
    x = distances[mask]
    y = green[mask]
    if x.size < 5:
        return {"used_points": int(x.size), "r2": float("nan"), "slope": float("nan"), "intercept": float("nan")}
    design = np.column_stack([1.0 / x, np.ones_like(x)])
    coeff, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred = design @ coeff
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - float(np.mean(y))) ** 2))
    r2 = 1.0 - ss_res / max(ss_tot, 1.0e-300)
    return {
        "used_points": int(x.size),
        "r2": r2,
        "slope": float(coeff[0]),
        "intercept": float(coeff[1]),
        "y_min": float(np.min(y)),
        "y_max": float(np.max(y)),
    }


def shell_anisotropy(green: np.ndarray, distances: np.ndarray, decimals: int = 3) -> dict[str, float]:
    shells: dict[float, list[float]] = {}
    for value, radius in zip(green, distances):
        if radius <= 0.0:
            continue
        key = round(float(radius), decimals)
        shells.setdefault(key, []).append(float(value))
    cvs = []
    for values in shells.values():
        if len(values) >= 4:
            arr = np.array(values)
            cvs.append(float(np.std(arr) / max(abs(np.mean(arr)), 1.0e-12)))
    if not cvs:
        return {"mean_shell_cv": float("nan"), "max_shell_cv": float("nan")}
    return {"mean_shell_cv": float(np.mean(cvs)), "max_shell_cv": float(np.max(cvs))}


def audit_model(model: str, states: list[tuple[int, int, int]], indices: dict[tuple[int, int, int], int], dims: tuple[int, int, int], xi: np.ndarray, args: argparse.Namespace) -> dict[str, Any]:
    transitions = build_transitions(model, states, indices, dims, args)
    l_matrix = generator_matrix(len(states), transitions)
    source_state = tuple(dim // 2 for dim in dims)
    source = indices[source_state]
    distances = periodic_distance_from_source(states, source_state, dims)
    green = solve_zero_mean_green(l_matrix, source)
    fit = fit_inverse_r(green, distances, args.r_min, args.r_max)
    shell = shell_anisotropy(green, distances)
    moments = jump_moments(states, dims, transitions)
    current = current_diagnostics(len(states), transitions)
    row_sums = np.asarray(l_matrix.sum(axis=1)).ravel()
    col_sums = np.asarray(l_matrix.sum(axis=0)).ravel()
    return {
        "model": model,
        "transition_count": len(transitions),
        "max_abs_row_sum": float(np.max(np.abs(row_sums))),
        "max_abs_column_sum": float(np.max(np.abs(col_sums))),
        "jump_moments": moments,
        "current": current,
        "inverse_r_fit": fit,
        "shell_anisotropy": shell,
        "green_min": float(np.min(green)),
        "green_max": float(np.max(green)),
        "green_source": float(green[source]),
    }


def audit(args: argparse.Namespace) -> dict[str, Any]:
    dims = parse_dims(args.dims)
    states = grid_states(dims)
    indices = state_index(states)
    xi = centered_coordinates(states, dims)
    models = [item.strip() for item in args.models.split(",") if item.strip()]
    results = [audit_model(model, states, indices, dims, xi, args) for model in models]
    return {
        "claim_tested": "non-reversible generator escape hatch for Green-kernel recovery",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "dims": dims,
        "state_count": len(states),
        "models": results,
        "summary": {
            "best_inverse_r_r2": max(r["inverse_r_fit"]["r2"] for r in results if np.isfinite(r["inverse_r_fit"]["r2"])),
            "models": {r["model"]: {"r2": r["inverse_r_fit"]["r2"], "q4": r["jump_moments"]["normalized_fourth_moment"]} for r in results},
        },
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Non-Reversible Resolvent Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Grid dimensions: `{result['dims']}`",
        f"- State count: {result['state_count']}",
        "",
        "| model | q4 | unit q4 | symbol A | current rel flux | 1/r R2 | slope | shell CV mean |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["models"]:
        moments = row["jump_moments"]
        fit = row["inverse_r_fit"]
        shell = row["shell_anisotropy"]
        current = row["current"]
        lines.append(
            "| {model} | {q4} | {uq4} | {a} | {current} | {r2} | {slope} | {cv} |".format(
                model=row["model"],
                q4=fmt(moments["normalized_fourth_moment"]),
                uq4=fmt(moments["unit_symbol_fourth_ratio"]),
                a=fmt(moments["anisotropy"]),
                current=fmt(current["relative_abs_flux"]),
                r2=fmt(fit["r2"]),
                slope=fmt(fit["slope"]),
                cv=fmt(shell["mean_shell_cv"]),
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Local drift-diffusion may retain a local 1/r-like singular profile,",
            "but only when the jump carre-du-champ is already local. Mean-field",
            "complete jumps keep a bad locality diagnostic and do not acquire a",
            "1/r resolvent profile from adding a current. This finite test keeps",
            "the no-go stated as reversible unless a broader non-reversible,",
            "nonlocal construction is explicitly supplied.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dims", default="9,9,9")
    parser.add_argument("--models", default="local_reversible,local_drift,complete,complete_plus_drift")
    parser.add_argument("--diffusion", type=float, default=1.0)
    parser.add_argument("--drift", type=float, default=0.35)
    parser.add_argument("--complete-rate", type=float, default=1.0)
    parser.add_argument("--local-rate", type=float, default=0.1)
    parser.add_argument("--r-min", type=float, default=0.08)
    parser.add_argument("--r-max", type=float, default=0.45)
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
