"""Hamiltonian L=JK Schur audit.

This audit tests the conservative version of the Schur bridge.  Instead of a
non-self-adjoint Lindblad/Markov generator, it constructs a finite Hamiltonian
linearization

    zdot = L z,   L = J H''

with a physical coordinate block P and hidden coherent coordinate block Q.  The
hidden coordinates are eliminated at the stiffness level:

    K_eff = K_PP - K_PQ K_QQ^{-1} K_QP.

If K_eff has a local 1/r Green kernel while K_PP is mean-field/nonlocal, then
the Schur mechanism can be conservative in finite row.  This is an existence
audit only: the default spectral completion chooses K_PQ by factoring the
desired difference K_PP-K_target, so it does not prove CRT/Bures canonicity.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path
from typing import Any

import numpy as np

from bures_isotropization_linear_audit import (
    build_xi,
    crt_states,
    distinct_xi_count,
    fmt,
    prime_factors_squarefree,
    target_local_pairs,
    target_radius,
)


DEFAULT_REPORT = Path("empirical/reports/hamiltonian_schur_audit.md")
DEFAULT_JSON = Path("empirical/reports/hamiltonian_schur_audit.json")


def centered_projector(n: int) -> np.ndarray:
    one = np.ones((n, 1), dtype=float)
    return np.eye(n) - (one @ one.T) / n


def complete_stiffness(n: int, alpha: float) -> np.ndarray:
    return alpha * centered_projector(n)


def laplacian_from_pairs(n: int, pairs: np.ndarray, weight: float) -> np.ndarray:
    lap = np.zeros((n, n), dtype=float)
    for i_raw, j_raw in pairs:
        i = int(i_raw)
        j = int(j_raw)
        lap[i, i] += weight
        lap[j, j] += weight
        lap[i, j] -= weight
        lap[j, i] -= weight
    return lap


def connected_components(n: int, pairs: np.ndarray) -> int:
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for i_raw, j_raw in pairs:
        i = int(i_raw)
        j = int(j_raw)
        adjacency[i].append(j)
        adjacency[j].append(i)
    seen = [False] * n
    count = 0
    for start in range(n):
        if seen[start]:
            continue
        count += 1
        seen[start] = True
        queue: deque[int] = deque([start])
        while queue:
            node = queue.popleft()
            for nxt in adjacency[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    queue.append(nxt)
    return count


def source_index(xi: np.ndarray) -> int:
    return int(np.argmin(np.sum(xi * xi, axis=1)))


def fit_inverse_r(values: np.ndarray, distances: np.ndarray, r_min_quantile: float, r_max_quantile: float) -> dict[str, Any]:
    nonzero = distances > 1.0e-12
    radii = distances[nonzero]
    if radii.size < 6:
        return {"used_points": int(radii.size), "r2": float("nan"), "slope": float("nan"), "intercept": float("nan")}
    r_min = float(np.quantile(radii, r_min_quantile))
    r_max = float(np.quantile(radii, r_max_quantile))
    mask = nonzero & (distances >= r_min) & (distances <= r_max)
    x = distances[mask]
    y = np.real(values[mask])
    design = np.column_stack([1.0 / x, np.ones_like(x)])
    coeff, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred = design @ coeff
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - float(np.mean(y))) ** 2))
    r2 = 1.0 - ss_res / max(ss_tot, 1.0e-300)
    return {
        "used_points": int(x.size),
        "r_min": r_min,
        "r_max": r_max,
        "r2": r2,
        "slope": float(coeff[0]),
        "intercept": float(coeff[1]),
        "value_min": float(np.min(y)),
        "value_max": float(np.max(y)),
    }


def shell_anisotropy(values: np.ndarray, distances: np.ndarray, decimals: int = 3) -> dict[str, float]:
    shells: dict[float, list[float]] = {}
    for value, radius in zip(np.real(values), distances):
        if radius <= 1.0e-12:
            continue
        shells.setdefault(round(float(radius), decimals), []).append(float(value))
    cvs = []
    for shell_values in shells.values():
        if len(shell_values) >= 3:
            arr = np.array(shell_values)
            cvs.append(float(np.std(arr) / max(abs(np.mean(arr)), 1.0e-12)))
    if not cvs:
        return {"mean_shell_cv": float("nan"), "max_shell_cv": float("nan")}
    return {"mean_shell_cv": float(np.mean(cvs)), "max_shell_cv": float(np.max(cvs))}


def solve_zero_mean_green(stiffness: np.ndarray, source: int) -> np.ndarray:
    n = stiffness.shape[0]
    constraint = np.ones((n, 1), dtype=float)
    system = np.block(
        [
            [stiffness, constraint],
            [constraint.T, np.zeros((1, 1), dtype=float)],
        ]
    )
    rhs = np.full(n + 1, -1.0 / n, dtype=float)
    rhs[source] += 1.0
    rhs[-1] = 0.0
    sol = np.linalg.solve(system, rhs)
    return sol[:n]


def kernel_metrics(name: str, stiffness: np.ndarray, xi: np.ndarray, args: argparse.Namespace) -> dict[str, Any]:
    source = source_index(xi)
    distances = np.linalg.norm(xi - xi[source], axis=1)
    green = solve_zero_mean_green(stiffness, source)
    fit = fit_inverse_r(green, distances, args.r_min_quantile, args.r_max_quantile)
    shell = shell_anisotropy(green, distances)
    return {
        "name": name,
        "inverse_r_fit": fit,
        "shell_anisotropy": shell,
        "green_source": float(green[source]),
        "green_min": float(np.min(green)),
        "green_max": float(np.max(green)),
        "real_range": float(np.max(green) - np.min(green)),
    }


def stiffness_moments(xi: np.ndarray, stiffness: np.ndarray) -> dict[str, Any]:
    n, dim = xi.shape
    symbol = np.zeros((dim, dim), dtype=float)
    fourth = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            conductance = -float(stiffness[i, j])
            if conductance <= 1.0e-14:
                continue
            delta = xi[j] - xi[i]
            norm_sq = float(delta @ delta)
            symbol += 2.0 * conductance * np.outer(delta, delta) / n
            fourth += 2.0 * conductance * norm_sq * norm_sq / n
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    trace = float(np.trace(symbol))
    denom = float(eigvals[-1] + eigvals[0])
    return {
        "eigenvalues": eigvals.tolist(),
        "anisotropy": float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf"),
        "trace": trace,
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
        "unit_symbol_fourth_ratio": float(fourth / max(trace * dim, 1.0e-300)),
    }


def spectral_completion(k_pp: np.ndarray, k_target: np.ndarray, tolerance: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    difference = 0.5 * ((k_pp - k_target) + (k_pp - k_target).T)
    eigvals, eigvecs = np.linalg.eigh(difference)
    keep = eigvals > tolerance
    if not np.any(keep):
        k_pq = np.zeros((k_pp.shape[0], 0), dtype=float)
        k_qq = np.zeros((0, 0), dtype=float)
        return k_pq, k_qq, difference
    k_pq = eigvecs[:, keep] @ np.diag(np.sqrt(eigvals[keep]))
    k_qq = np.eye(int(np.sum(keep)), dtype=float)
    return k_pq, k_qq, difference


def make_hamiltonian_matrix(k_full: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = k_full.shape[0]
    hessian = np.block(
        [
            [k_full, np.zeros((m, m), dtype=float)],
            [np.zeros((m, m), dtype=float), np.eye(m)],
        ]
    )
    j = np.block(
        [
            [np.zeros((m, m), dtype=float), np.eye(m)],
            [-np.eye(m), np.zeros((m, m), dtype=float)],
        ]
    )
    return j @ hessian, j, hessian


def audit(args: argparse.Namespace) -> dict[str, Any]:
    primes = prime_factors_squarefree(args.row)
    states = crt_states(primes)
    xi, labels = build_xi(primes, states, args.xi_mode, args.dimension, args.quotient_basis)
    n = len(states)
    radius = target_radius(n, distinct_xi_count(xi), args)
    pairs = target_local_pairs(xi, radius, args.max_target_pairs)
    k_target = laplacian_from_pairs(n, pairs, args.target_weight)
    target_eigvals = np.linalg.eigvalsh(0.5 * (k_target + k_target.T))
    max_target = float(np.max(target_eigvals))
    alpha = args.complete_alpha if args.complete_alpha is not None else args.alpha_safety * max(max_target, 1.0)
    k_pp = complete_stiffness(n, alpha)
    k_pq, k_qq, difference = spectral_completion(k_pp, k_target, args.factor_tolerance)
    if k_qq.size:
        k_eff = k_pp - k_pq @ np.linalg.solve(k_qq, k_pq.T)
    else:
        k_eff = k_pp.copy()
    hidden_dim = k_qq.shape[0]
    k_full = np.block(
        [
            [k_pp, k_pq],
            [k_pq.T, k_qq],
        ]
    )
    l_matrix, j_matrix, hessian = make_hamiltonian_matrix(k_full)
    hamiltonian_defect = l_matrix.T @ hessian + hessian @ l_matrix
    k_full_eigvals = np.linalg.eigvalsh(0.5 * (k_full + k_full.T))
    k_eff_eigvals = np.linalg.eigvalsh(0.5 * (k_eff + k_eff.T))
    diff_eigvals = np.linalg.eigvalsh(difference)
    return {
        "claim_tested": "conservative Hamiltonian Schur completion for Green-kernel localization",
        "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        "row": args.row,
        "primes": primes,
        "state_count": n,
        "hidden_coordinate_dim": hidden_dim,
        "phase_space_dim": 2 * (n + hidden_dim),
        "xi_labels": labels,
        "target_radius": radius,
        "target_pair_count": int(pairs.shape[0]),
        "target_components": connected_components(n, pairs),
        "complete_alpha": alpha,
        "moments": {
            "K_PP_complete": stiffness_moments(xi, k_pp),
            "K_target": stiffness_moments(xi, k_target),
            "K_eff": stiffness_moments(xi, k_eff),
        },
        "kernels": {
            "K_PP_complete": kernel_metrics("K_PP_complete", k_pp, xi, args),
            "K_target": kernel_metrics("K_target", k_target, xi, args),
            "K_eff_schur": kernel_metrics("K_eff_schur", k_eff, xi, args),
        },
        "schur_consistency": {
            "max_abs_K_eff_minus_target": float(np.max(np.abs(k_eff - k_target))),
            "relative_K_eff_minus_target": float(np.linalg.norm(k_eff - k_target) / max(np.linalg.norm(k_target), 1.0e-300)),
            "difference_min_eig": float(np.min(diff_eigvals)),
            "difference_max_eig": float(np.max(diff_eigvals)),
            "K_full_min_eig": float(np.min(k_full_eigvals)),
            "K_full_second_min_eig": float(np.sort(k_full_eigvals)[1]) if k_full_eigvals.size > 1 else float("nan"),
            "K_eff_min_eig": float(np.min(k_eff_eigvals)),
            "K_eff_second_min_eig": float(np.sort(k_eff_eigvals)[1]) if k_eff_eigvals.size > 1 else float("nan"),
        },
        "hamiltonian_checks": {
            "max_abs_J_plus_JT": float(np.max(np.abs(j_matrix + j_matrix.T))),
            "max_abs_H_minus_HT": float(np.max(np.abs(hessian - hessian.T))),
            "max_abs_LTH_plus_HL": float(np.max(np.abs(hamiltonian_defect))),
            "max_real_eig_L": float(np.max(np.abs(np.real(np.linalg.eigvals(l_matrix))))),
        },
        "interpretation": {
            "status": "CONSERVATIVE_EXISTENCE_COMPLETION",
            "caveat": "K_PQ is chosen by spectral factorization of K_PP-K_target; this proves finite Hamiltonian Schur realizability, not CRT/Bures canonicity.",
        },
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Hamiltonian L=JK Schur Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Row: {result['row']} with primes `{result['primes']}`",
        f"- State count: {result['state_count']}",
        f"- Hidden coordinate dimension: {result['hidden_coordinate_dim']}",
        f"- Phase-space dimension: {result['phase_space_dim']}",
        f"- xi labels: `{result['xi_labels']}`",
        f"- Target radius: {fmt(result['target_radius'])}",
        f"- Target-local pairs: {result['target_pair_count']}",
        f"- Target graph components: {result['target_components']}",
        f"- Complete stiffness alpha: {fmt(result['complete_alpha'])}",
        "",
        "## Kernel Fits",
        "",
        "| stiffness | unit fourth | 1/r R2 | slope | shell CV mean | real range |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name in ["K_PP_complete", "K_target", "K_eff_schur"]:
        moments = result["moments"]["K_eff" if name == "K_eff_schur" else name]
        kernel = result["kernels"][name]
        fit = kernel["inverse_r_fit"]
        shell = kernel["shell_anisotropy"]
        lines.append(
            "| {name} | {unit} | {r2} | {slope} | {shell} | {rrange} |".format(
                name=name,
                unit=fmt(moments["unit_symbol_fourth_ratio"]),
                r2=fmt(fit["r2"]),
                slope=fmt(fit["slope"]),
                shell=fmt(shell["mean_shell_cv"]),
                rrange=fmt(kernel["real_range"]),
            )
        )
    schur = result["schur_consistency"]
    ham = result["hamiltonian_checks"]
    lines.extend(
        [
            "",
            "## Schur And Hamiltonian Checks",
            "",
            f"- max |K_eff - K_target|: {fmt(schur['max_abs_K_eff_minus_target'])}",
            f"- relative |K_eff - K_target|: {fmt(schur['relative_K_eff_minus_target'])}",
            f"- min eig(K_PP-K_target): {fmt(schur['difference_min_eig'])}",
            f"- min eig(K_full): {fmt(schur['K_full_min_eig'])}",
            f"- second min eig(K_eff): {fmt(schur['K_eff_second_min_eig'])}",
            f"- max |J+J^T|: {fmt(ham['max_abs_J_plus_JT'])}",
            f"- max |H-H^T|: {fmt(ham['max_abs_H_minus_HT'])}",
            f"- max |L^T H + H L|: {fmt(ham['max_abs_LTH_plus_HL'])}",
            f"- max |Re eig(L)|: {fmt(ham['max_real_eig_L'])}",
            "",
            "## Interpretation",
            "",
            "This is a conservative existence completion.  The audit builds a",
            "Hamiltonian linear system L=JK whose hidden-coordinate Schur",
            "complement exactly recovers the target-local stiffness, while the",
            "uneliminated physical block K_PP is mean-field.  Therefore the",
            "Schur localization mechanism is compatible with conservative",
            "Hamiltonian algebra in finite row.",
            "",
            "The caveat is essential: K_PQ is chosen by spectral factorization of",
            "K_PP-K_target.  This proves finite Hamiltonian realizability, not",
            "that CRT/Bures structure naturally supplies this coupling or that it",
            "comes from K^CH(Deta v,Deta v).",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", type=int, default=30)
    parser.add_argument("--dimension", type=int, default=3)
    parser.add_argument(
        "--xi-mode",
        choices=["sector_fill", "prime_first", "largest_prime_modes", "largest_primes"],
        default="largest_primes",
    )
    parser.add_argument("--quotient-basis", choices=["helmert", "fourier", "residue"], default="residue")
    parser.add_argument("--target-h-scale", type=float, default=7.0)
    parser.add_argument("--target-mesh-denominator", choices=["row", "distinct"], default="distinct")
    parser.add_argument("--max-target-pairs", type=int, default=2_000_000)
    parser.add_argument("--target-weight", type=float, default=1.0)
    parser.add_argument("--alpha-safety", type=float, default=1.25)
    parser.add_argument("--complete-alpha", type=float, default=None)
    parser.add_argument("--factor-tolerance", type=float, default=1.0e-10)
    parser.add_argument("--r-min-quantile", type=float, default=0.10)
    parser.add_argument("--r-max-quantile", type=float, default=0.80)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "row": result["row"],
                "hidden_dim": result["hidden_coordinate_dim"],
                "target_pairs": result["target_pair_count"],
                "target_components": result["target_components"],
                "complete_r2": result["kernels"]["K_PP_complete"]["inverse_r_fit"]["r2"],
                "target_r2": result["kernels"]["K_target"]["inverse_r_fit"]["r2"],
                "schur_r2": result["kernels"]["K_eff_schur"]["inverse_r_fit"]["r2"],
                "schur_error": result["schur_consistency"]["relative_K_eff_minus_target"],
                "hamiltonian_defect": result["hamiltonian_checks"]["max_abs_LTH_plus_HL"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
