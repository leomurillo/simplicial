"""Projected non-reversible quantum resolvent audit.

This is the finite test left open by the diagonal carre-du-champ audits.  It
does not evaluate Gamma on diagonal observables.  Instead it builds a genuine
operator-algebra generator

    L(A) = i[H,A] + D_dephase(A) + D_classical(A)

on M_N(C), projects the resolvent back to the diagonal physical readout, and
compares

    P(-L)^{-1}P

against the diagonal-only resolvent and the Feshbach/Schur effective operator

    L_eff = L_PP - L_PQ L_QQ^{-1} L_QP.

If the coherent sector can localize the physical Green kernel while the
diagonal Gamma remains nonlocal, it must show up in the difference between the
diagonal-only and full projected resolvents.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

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


DEFAULT_REPORT = Path("empirical/reports/quantum_nonreversible_resolvent_audit.md")
DEFAULT_JSON = Path("empirical/reports/quantum_nonreversible_resolvent_audit.json")


@dataclass(frozen=True)
class ClassicalRates:
    rates: np.ndarray
    out: np.ndarray
    support_name: str


def basis_pairs(n: int) -> list[tuple[int, int]]:
    diag = [(i, i) for i in range(n)]
    offdiag = [(i, j) for i in range(n) for j in range(n) if i != j]
    return diag + offdiag


def source_index(xi: np.ndarray) -> int:
    return int(np.argmin(np.sum(xi * xi, axis=1)))


def euclidean_distances(xi: np.ndarray, source: int) -> np.ndarray:
    return np.linalg.norm(xi - xi[source], axis=1)


def matrix_from_pairs(n: int, pairs: np.ndarray, strength: float, phase: str) -> np.ndarray:
    h = np.zeros((n, n), dtype=np.complex128)
    if pairs.size == 0:
        return h
    degree_scale = math.sqrt(max(1.0, 2.0 * pairs.shape[0] / n))
    value_scale = strength / degree_scale
    for idx, (i_raw, j_raw) in enumerate(pairs):
        i = int(i_raw)
        j = int(j_raw)
        if phase == "real":
            value = 1.0
        elif phase == "alternating":
            value = 1.0 if idx % 2 == 0 else -1.0
        elif phase == "four_phase":
            value = [1.0, 1.0j, -1.0, -1.0j][idx % 4]
        else:
            raise ValueError(f"unknown phase mode: {phase}")
        h[i, j] = value_scale * value
        h[j, i] = np.conjugate(h[i, j])
    return h


def mean_field_rates(n: int, rate: float) -> ClassicalRates:
    rates = np.full((n, n), rate / max(n - 1, 1), dtype=float)
    np.fill_diagonal(rates, 0.0)
    return ClassicalRates(rates=rates, out=np.sum(rates, axis=1), support_name="mean_field")


def target_local_rates(xi: np.ndarray, pairs: np.ndarray, rate: float) -> ClassicalRates:
    n = xi.shape[0]
    rates = np.zeros((n, n), dtype=float)
    if pairs.size:
        per_edge = rate
        for i_raw, j_raw in pairs:
            i = int(i_raw)
            j = int(j_raw)
            rates[i, j] += per_edge
            rates[j, i] += per_edge
    return ClassicalRates(rates=rates, out=np.sum(rates, axis=1), support_name="target_local")


def leg_complete_rates(states: list[tuple[int, ...]], rate: float) -> ClassicalRates:
    n = len(states)
    rates = np.zeros((n, n), dtype=float)
    for i, a in enumerate(states):
        for j, b in enumerate(states):
            if i == j:
                continue
            differences = sum(1 for av, bv in zip(a, b) if av != bv)
            if differences == 1:
                rates[i, j] = rate
    return ClassicalRates(rates=rates, out=np.sum(rates, axis=1), support_name="leg_complete")


def build_classical_rates(
    mode: str,
    states: list[tuple[int, ...]],
    xi: np.ndarray,
    target_pairs: np.ndarray,
    rate: float,
) -> ClassicalRates:
    if mode == "mean_field":
        return mean_field_rates(len(states), rate)
    if mode == "target_local":
        return target_local_rates(xi, target_pairs, rate)
    if mode == "leg_complete":
        return leg_complete_rates(states, rate)
    raise ValueError(f"unknown dissipator mode: {mode}")


def classical_dissipator(rates: ClassicalRates, a: np.ndarray) -> np.ndarray:
    diag = np.diag(a)
    out = np.empty_like(a)
    out[:, :] = -0.5 * (rates.out[:, None] + rates.out[None, :]) * a
    diagonal_out = rates.rates @ diag - rates.out * diag
    np.fill_diagonal(out, diagonal_out)
    return out


def dephase(a: np.ndarray, gamma: float) -> np.ndarray:
    diag = np.diag(np.diag(a))
    return gamma * (diag - a)


def generator_action(h: np.ndarray, rates: ClassicalRates, gamma: float) -> Callable[[np.ndarray], np.ndarray]:
    def action(a: np.ndarray) -> np.ndarray:
        return 1.0j * (h @ a - a @ h) + dephase(a, gamma) + classical_dissipator(rates, a)

    return action


def build_superoperator(action: Callable[[np.ndarray], np.ndarray], n: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    pairs = basis_pairs(n)
    index = {pair: idx for idx, pair in enumerate(pairs)}
    superop = np.zeros((n * n, n * n), dtype=np.complex128)
    for col, (i, j) in enumerate(pairs):
        basis = np.zeros((n, n), dtype=np.complex128)
        basis[i, j] = 1.0
        image = action(basis)
        for (a, b), row in index.items():
            value = image[a, b]
            if value != 0.0:
                superop[row, col] = value
    return superop, pairs


def solve_zero_mean(operator: np.ndarray, rhs: np.ndarray, diagonal_count: int) -> np.ndarray:
    dim = operator.shape[0]
    constraint = np.zeros((1, dim), dtype=np.complex128)
    constraint[0, :diagonal_count] = 1.0
    augmented = np.block(
        [
            [-operator, constraint.T],
            [constraint, np.zeros((1, 1), dtype=np.complex128)],
        ]
    )
    full_rhs = np.concatenate([rhs.astype(np.complex128), np.array([0.0], dtype=np.complex128)])
    sol = np.linalg.solve(augmented, full_rhs)
    return sol[:dim]


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


def weighted_jump_moments(xi: np.ndarray, rates: np.ndarray) -> dict[str, Any]:
    n, dim = xi.shape
    symbol = np.zeros((dim, dim), dtype=float)
    fourth = 0.0
    for i in range(n):
        for j in range(n):
            rate = float(rates[i, j])
            if rate == 0.0:
                continue
            delta = xi[j] - xi[i]
            norm_sq = float(delta @ delta)
            symbol += rate * np.outer(delta, delta) / n
            fourth += rate * norm_sq * norm_sq / n
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    trace = float(np.trace(symbol))
    denom = float(eigvals[-1] + eigvals[0])
    return {
        "eigenvalues": eigvals.tolist(),
        "trace": trace,
        "anisotropy": float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf"),
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
        "unit_symbol_fourth_ratio": float(fourth / max(trace * dim, 1.0e-300)),
    }


def kernel_metrics(name: str, values: np.ndarray, distances: np.ndarray, args: argparse.Namespace) -> dict[str, Any]:
    fit = fit_inverse_r(values, distances, args.r_min_quantile, args.r_max_quantile)
    shell = shell_anisotropy(values, distances)
    return {
        "name": name,
        "inverse_r_fit": fit,
        "shell_anisotropy": shell,
        "source_value_real": float(np.real(values[int(np.argmin(distances))])),
        "max_abs_imag": float(np.max(np.abs(np.imag(values)))),
        "real_min": float(np.min(np.real(values))),
        "real_max": float(np.max(np.real(values))),
    }


def audit(args: argparse.Namespace) -> dict[str, Any]:
    primes = prime_factors_squarefree(args.row)
    states = crt_states(primes)
    xi, labels = build_xi(primes, states, args.xi_mode, args.dimension, args.quotient_basis)
    radius = target_radius(len(states), distinct_xi_count(xi), args)
    target_pairs = target_local_pairs(xi, radius, args.max_target_pairs)
    rates = build_classical_rates(args.dissipator, states, xi, target_pairs, args.dissipation_rate)
    h = matrix_from_pairs(len(states), target_pairs, args.h_strength, args.phase)
    action = generator_action(h, rates, args.dephase_gamma)
    superop, pairs = build_superoperator(action, len(states))
    n = len(states)
    source = source_index(xi)
    distances = euclidean_distances(xi, source)
    rhs_p = np.full(n, -1.0 / n, dtype=np.complex128)
    rhs_p[source] += 1.0
    rhs_full = np.zeros(n * n, dtype=np.complex128)
    rhs_full[:n] = rhs_p

    l_pp = superop[:n, :n]
    l_pq = superop[:n, n:]
    l_qp = superop[n:, :n]
    l_qq = superop[n:, n:]

    diagonal_solution = solve_zero_mean(l_pp, rhs_p, n)
    full_solution = solve_zero_mean(superop, rhs_full, n)
    projected_full = full_solution[:n]

    schur_correction = l_pq @ np.linalg.solve(l_qq, l_qp)
    l_eff = l_pp - schur_correction
    schur_solution = solve_zero_mean(l_eff, rhs_p, n)

    moments = weighted_jump_moments(xi, rates.rates)
    h_support_rates = np.abs(h) ** 2
    h_moments = weighted_jump_moments(xi, h_support_rates)
    projected_difference = projected_full - diagonal_solution
    schur_error = projected_full - schur_solution
    return {
        "claim_tested": "non-reversible coherent sector contribution to projected Green kernel",
        "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        "row": args.row,
        "primes": primes,
        "state_count": n,
        "operator_dimension": n * n,
        "xi_labels": labels,
        "source_index": source,
        "target_radius": radius,
        "target_pair_count": int(target_pairs.shape[0]),
        "dissipator": rates.support_name,
        "diagonal_gamma_moments": moments,
        "hamiltonian_support_moments": h_moments,
        "block_norms": {
            "L_PP": float(np.linalg.norm(l_pp)),
            "L_PQ": float(np.linalg.norm(l_pq)),
            "L_QP": float(np.linalg.norm(l_qp)),
            "L_QQ": float(np.linalg.norm(l_qq)),
            "schur_correction": float(np.linalg.norm(schur_correction)),
            "schur_over_LPP": float(np.linalg.norm(schur_correction) / max(np.linalg.norm(l_pp), 1.0e-300)),
        },
        "kernels": {
            "diagonal_only": kernel_metrics("diagonal_only", diagonal_solution, distances, args),
            "projected_full": kernel_metrics("projected_full", projected_full, distances, args),
            "schur": kernel_metrics("schur", schur_solution, distances, args),
            "projected_minus_diagonal": kernel_metrics("projected_minus_diagonal", projected_difference, distances, args),
        },
        "consistency": {
            "max_abs_projected_full_minus_schur": float(np.max(np.abs(schur_error))),
            "relative_projected_full_minus_schur": float(
                np.linalg.norm(schur_error) / max(np.linalg.norm(projected_full), 1.0e-300)
            ),
            "max_abs_projected_full_minus_diagonal": float(np.max(np.abs(projected_difference))),
            "relative_projected_full_minus_diagonal": float(
                np.linalg.norm(projected_difference) / max(np.linalg.norm(diagonal_solution), 1.0e-300)
            ),
        },
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    gamma = result["diagonal_gamma_moments"]
    h_moments = result["hamiltonian_support_moments"]
    blocks = result["block_norms"]
    consistency = result["consistency"]
    lines = [
        "# Quantum Non-Reversible Projected Resolvent Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Row: {result['row']} with primes `{result['primes']}`",
        f"- State count: {result['state_count']}",
        f"- Operator dimension: {result['operator_dimension']}",
        f"- xi labels: `{result['xi_labels']}`",
        f"- Dissipator: `{result['dissipator']}`",
        f"- Target radius: {fmt(result['target_radius'])}",
        f"- Target-local H pairs: {result['target_pair_count']}",
        "",
        "## Diagonal Gamma Shadow",
        "",
        f"- Gamma anisotropy: {fmt(gamma['anisotropy'])}",
        f"- Gamma normalized q4: {fmt(gamma['normalized_fourth_moment'])}",
        f"- Gamma unit-symbol fourth: {fmt(gamma['unit_symbol_fourth_ratio'])}",
        f"- H-support unit-symbol fourth: {fmt(h_moments['unit_symbol_fourth_ratio'])}",
        "",
        "## Block Coupling",
        "",
        f"- ||L_PP||: {fmt(blocks['L_PP'])}",
        f"- ||L_PQ||: {fmt(blocks['L_PQ'])}",
        f"- ||L_QP||: {fmt(blocks['L_QP'])}",
        f"- ||L_QQ||: {fmt(blocks['L_QQ'])}",
        f"- ||Schur correction|| / ||L_PP||: {fmt(blocks['schur_over_LPP'])}",
        "",
        "## Kernel Fits",
        "",
        "| kernel | 1/r R2 | slope | shell CV mean | max imag | real range |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name in ["diagonal_only", "projected_full", "schur", "projected_minus_diagonal"]:
        kernel = result["kernels"][name]
        fit = kernel["inverse_r_fit"]
        shell = kernel["shell_anisotropy"]
        real_range = kernel["real_max"] - kernel["real_min"]
        lines.append(
            "| {name} | {r2} | {slope} | {shell} | {imag} | {rrange} |".format(
                name=name,
                r2=fmt(fit["r2"]),
                slope=fmt(fit["slope"]),
                shell=fmt(shell["mean_shell_cv"]),
                imag=fmt(kernel["max_abs_imag"]),
                rrange=fmt(real_range),
            )
        )
    lines.extend(
        [
            "",
            "## Schur Consistency",
            "",
            f"- max |projected full - Schur|: {fmt(consistency['max_abs_projected_full_minus_schur'])}",
            f"- relative |projected full - Schur|: {fmt(consistency['relative_projected_full_minus_schur'])}",
            f"- relative |projected full - diagonal only|: {fmt(consistency['relative_projected_full_minus_diagonal'])}",
            "",
            "## Interpretation",
            "",
            "This audit measures the non-symmetric resolvent projected back to the",
            "diagonal physical readout.  A coherent-sector localization signal",
            "would appear as a strong 1/r fit in `projected_full` and `schur` while",
            "the diagonal Gamma shadow remains nonlocal.  Agreement between",
            "`projected_full` and `schur` verifies that any effect is carried by",
            "the Feshbach correction L_PQ L_QQ^{-1} L_QP rather than by a Gamma",
            "calculation on diagonal observables.",
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
    parser.add_argument("--target-h-scale", type=float, default=8.0)
    parser.add_argument("--target-mesh-denominator", choices=["row", "distinct"], default="distinct")
    parser.add_argument("--max-target-pairs", type=int, default=2_000_000)
    parser.add_argument("--dissipator", choices=["mean_field", "leg_complete", "target_local"], default="mean_field")
    parser.add_argument("--dissipation-rate", type=float, default=1.0)
    parser.add_argument("--dephase-gamma", type=float, default=2.0)
    parser.add_argument("--h-strength", type=float, default=1.0)
    parser.add_argument("--phase", choices=["real", "alternating", "four_phase"], default="four_phase")
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
                "dissipator": result["dissipator"],
                "gamma_unit_fourth": result["diagonal_gamma_moments"]["unit_symbol_fourth_ratio"],
                "diagonal_r2": result["kernels"]["diagonal_only"]["inverse_r_fit"]["r2"],
                "projected_r2": result["kernels"]["projected_full"]["inverse_r_fit"]["r2"],
                "schur_r2": result["kernels"]["schur"]["inverse_r_fit"]["r2"],
                "schur_relative_error": result["consistency"]["relative_projected_full_minus_schur"],
                "projected_vs_diagonal": result["consistency"]["relative_projected_full_minus_diagonal"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
