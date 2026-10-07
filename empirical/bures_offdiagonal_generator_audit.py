"""Instantiate an off-diagonal generator and test its diagonal shadow.

This audit addresses the distinction between:

1. a classical diagonal conductance graph; and
2. a genuine off-diagonal generator on the matrix algebra.

For diagonal coordinate observables X_mu=diag(xi_mu), a Hermitian off-diagonal
coupling H gives the derivation delta_H(X)=i[H,X].  At the maximally mixed
state the SLD/Bures norm of this derivation is

    <delta_H X_mu, delta_H X_nu>_B
      = N * sum_{ij} |H_ij|^2 (xi_j^mu-xi_i^mu)(xi_j^nu-xi_i^nu).

The associated Hermitian Lindblad dissipator D_H(A)=-1/2[H,[H,A]] has the same
quadratic form up to the conventional factor 1/2.  A pure Hamiltonian
commutator i[H,.] is skew-adjoint and has zero symmetric Dirichlet form.

Thus this audit is only a diagonal-shadow consistency check.  It does not test
whether a coherent, non-reversible generator can localize the Green kernel via
the non-symmetric resolvent, because all Gamma evaluations below are on the
commuting diagonal coordinate subalgebra and Gamma is linear in the generator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from bures_isotropization_linear_audit import (
    build_xi,
    crt_states,
    distinct_xi_count,
    fmt,
    moment_stats_from_pairs,
    prime_factors_squarefree,
    target_local_pairs,
    target_radius,
)


DEFAULT_REPORT = Path("empirical/reports/bures_offdiagonal_generator_audit.md")
DEFAULT_JSON = Path("empirical/reports/bures_offdiagonal_generator_audit.json")


def matrix_from_pairs(n: int, pairs: np.ndarray, phase: str) -> np.ndarray:
    h = np.zeros((n, n), dtype=np.complex128)
    for idx, (i, j) in enumerate(pairs):
        if phase == "real":
            value = 1.0
        elif phase == "alternating":
            value = 1.0 if idx % 2 == 0 else -1.0
        elif phase == "four_phase":
            value = [1.0, 1.0j, -1.0, -1.0j][idx % 4]
        else:
            raise ValueError(f"unknown phase mode: {phase}")
        h[int(i), int(j)] = value
        h[int(j), int(i)] = np.conjugate(value)
    return h


def diagonal_observables(xi: np.ndarray) -> list[np.ndarray]:
    return [np.diag(xi[:, mu]).astype(np.complex128) for mu in range(xi.shape[1])]


def bures_inner_maximally_mixed(x: np.ndarray, y: np.ndarray) -> complex:
    n = x.shape[0]
    return n * np.trace(x.conj().T @ y)


def sld_inner_diagonal_rho(x: np.ndarray, y: np.ndarray, rho_diag: np.ndarray) -> complex:
    denom = rho_diag[:, None] + rho_diag[None, :]
    return np.sum(2.0 * np.conjugate(x) * y / denom)


def commutator(h: np.ndarray, a: np.ndarray) -> np.ndarray:
    return h @ a - a @ h


def reference_probabilities(xi: np.ndarray, beta: float, mode: str) -> np.ndarray:
    if mode == "uniform" or abs(beta) <= 0.0:
        energy = np.zeros(xi.shape[0], dtype=float)
    elif mode == "norm2":
        energy = np.sum(xi * xi, axis=1)
    elif mode == "first":
        energy = xi[:, 0]
    else:
        raise ValueError(f"unknown rho mode: {mode}")
    logits = -beta * (energy - float(np.mean(energy)))
    logits = logits - float(np.max(logits))
    weights = np.exp(logits)
    return weights / float(np.sum(weights))


def explicit_bures_tensors(h: np.ndarray, xi: np.ndarray) -> dict[str, Any]:
    obs = diagonal_observables(xi)
    dim = len(obs)
    n = h.shape[0]
    derivations = [1.0j * commutator(h, a) for a in obs]
    second = np.zeros((dim, dim), dtype=float)
    lindblad_quadratic = np.zeros((dim, dim), dtype=float)
    hamiltonian_symmetric = np.zeros((dim, dim), dtype=float)
    h2 = h @ h
    for mu in range(dim):
        for nu in range(dim):
            second[mu, nu] = float(np.real(bures_inner_maximally_mixed(derivations[mu], derivations[nu])))
            # Heisenberg Hamiltonian generator L(A)=i[H,A] is skew-adjoint.
            l_ham = 1.0j * commutator(h, obs[nu])
            hamiltonian_symmetric[mu, nu] = float(np.real(bures_inner_maximally_mixed(obs[mu], -l_ham)))
            # Hermitian Lindblad dissipator D_H(A)=H A H - 1/2{H^2,A}.
            d_h = h @ obs[nu] @ h - 0.5 * (h2 @ obs[nu] + obs[nu] @ h2)
            lindblad_quadratic[mu, nu] = float(np.real(bures_inner_maximally_mixed(obs[mu], -d_h)))
    return {
        "derivation_second": second.tolist(),
        "derivation_eigenvalues": np.linalg.eigvalsh(0.5 * (second + second.T)).tolist(),
        "lindblad_quadratic": lindblad_quadratic.tolist(),
        "lindblad_eigenvalues": np.linalg.eigvalsh(0.5 * (lindblad_quadratic + lindblad_quadratic.T)).tolist(),
        "hamiltonian_symmetric_form": hamiltonian_symmetric.tolist(),
        "max_abs_hamiltonian_symmetric_form": float(np.max(np.abs(hamiltonian_symmetric))),
        "max_abs_lindblad_minus_half_derivation": float(np.max(np.abs(lindblad_quadratic - 0.5 * second))),
        "normalization": "Bures at rho=I/N uses <X,Y>_B = N Tr(X^*Y)",
        "state_count": n,
    }


def lindblad_h(h: np.ndarray, a: np.ndarray) -> np.ndarray:
    h2 = h @ h
    return h @ a @ h - 0.5 * (h2 @ a + a @ h2)


def hamiltonian_generator(h: np.ndarray, a: np.ndarray) -> np.ndarray:
    return 1.0j * commutator(h, a)


def gamma_matrix(generator, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return 0.5 * (generator(a @ b) - generator(a) @ b - a @ generator(b))


def sld_tangent_fourth_ratio(tangents: list[np.ndarray], rho_diag: np.ndarray) -> dict[str, Any]:
    dim = len(tangents)
    second = np.zeros((dim, dim), dtype=float)
    fourth = 0.0
    denom = rho_diag[:, None] + rho_diag[None, :]
    vectors = np.stack(tangents, axis=0)
    for mu in range(dim):
        for nu in range(dim):
            second[mu, nu] = float(np.real(sld_inner_diagonal_rho(tangents[mu], tangents[nu], rho_diag)))
    for i in range(rho_diag.size):
        for j in range(rho_diag.size):
            weight = 2.0 / denom[i, j]
            norm_sq = float(np.real(np.vdot(vectors[:, i, j], vectors[:, i, j])))
            fourth += weight * norm_sq * norm_sq
    eigvals = np.linalg.eigvalsh(0.5 * (second + second.T))
    trace = float(np.trace(second))
    return {
        "second": second.tolist(),
        "eigenvalues": eigvals.tolist(),
        "trace": trace,
        "anisotropy": float((eigvals[-1] - eigvals[0]) / (eigvals[-1] + eigvals[0]))
        if eigvals[-1] + eigvals[0] > 1.0e-15
        else float("inf"),
        "entry_fourth": float(fourth),
        "unit_symbol_fourth_ratio": float(fourth / max(trace * dim, 1.0e-300)),
    }


def thermal_bures_tensors(h: np.ndarray, xi: np.ndarray, rho_diag: np.ndarray) -> dict[str, Any]:
    obs = diagonal_observables(xi)
    derivations = [hamiltonian_generator(h, a) for a in obs]
    dissipative_images = [lindblad_h(h, a) for a in obs]
    full_images = [d + l for d, l in zip(derivations, dissipative_images)]

    gen_h = lambda a: hamiltonian_generator(h, a)
    gen_d = lambda a: lindblad_h(h, a)
    gen_full = lambda a: gen_h(a) + gen_d(a)
    max_gamma_h = 0.0
    max_gamma_cross = 0.0
    max_gamma_full_minus_d = 0.0
    for a in obs:
        for b in obs:
            gamma_h = gamma_matrix(gen_h, a, b)
            gamma_d = gamma_matrix(gen_d, a, b)
            gamma_full = gamma_matrix(gen_full, a, b)
            gamma_cross = gamma_full - gamma_h - gamma_d
            max_gamma_h = max(max_gamma_h, float(np.max(np.abs(gamma_h))))
            max_gamma_cross = max(max_gamma_cross, float(np.max(np.abs(gamma_cross))))
            max_gamma_full_minus_d = max(max_gamma_full_minus_d, float(np.max(np.abs(gamma_full - gamma_d))))

    deriv = sld_tangent_fourth_ratio(derivations, rho_diag)
    diss = sld_tangent_fourth_ratio(dissipative_images, rho_diag)
    full = sld_tangent_fourth_ratio(full_images, rho_diag)
    second_cross = np.array(full["second"]) - np.array(deriv["second"]) - np.array(diss["second"])
    return {
        "rho_min": float(np.min(rho_diag)),
        "rho_max": float(np.max(rho_diag)),
        "rho_condition": float(np.max(rho_diag) / max(np.min(rho_diag), 1.0e-300)),
        "derivation_image": deriv,
        "dissipative_image": diss,
        "full_generator_image": full,
        "sld_image_cross_second": second_cross.tolist(),
        "max_abs_sld_image_cross_second": float(np.max(np.abs(second_cross))),
        "max_abs_gamma_hamiltonian": max_gamma_h,
        "max_abs_gamma_cross": max_gamma_cross,
        "max_abs_gamma_full_minus_dissipative": max_gamma_full_minus_d,
        "gamma_note": "Carre-du-champ is linear in the generator, so the residual cross term is algebraically zero; Hamiltonian derivations cancel by Leibniz.",
        "image_norm_note": "The SLD norm of (Hamiltonian + dissipative)(X) can have cross terms but is not the Markov Dirichlet form.",
        "scope_note": "All Gamma evaluations are restricted to diagonal coordinate observables; this is not a non-symmetric resolvent audit.",
    }


def edge_formula_from_h(h: np.ndarray, xi: np.ndarray) -> dict[str, Any]:
    n, dim = xi.shape
    weights = np.abs(h) ** 2
    symbol = np.zeros((dim, dim), dtype=float)
    fourth = 0.0
    edge_weight_sum = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            weight = float(weights[i, j])
            if weight == 0.0:
                continue
            delta = xi[j] - xi[i]
            norm_sq = float(delta @ delta)
            symbol += 2.0 * n * weight * np.outer(delta, delta)
            fourth += 2.0 * n * weight * norm_sq * norm_sq
            edge_weight_sum += weight
    eigvals = np.linalg.eigvalsh(0.5 * (symbol + symbol.T))
    trace = float(np.trace(symbol))
    denom = float(eigvals[-1] + eigvals[0])
    anisotropy = float((eigvals[-1] - eigvals[0]) / denom) if denom > 1.0e-15 else float("inf")
    return {
        "symbol": symbol.tolist(),
        "eigenvalues": eigvals.tolist(),
        "anisotropy": anisotropy,
        "trace": trace,
        "fourth_moment": fourth,
        "normalized_fourth_moment": float(fourth / max(trace * trace, 1.0e-300)),
        "unit_symbol_fourth_ratio": float(fourth / max(trace * xi.shape[1], 1.0e-300)),
        "edge_weight_sum": edge_weight_sum,
    }


def unit_symbol_fourth_ratio(stats: dict[str, Any], dim: int) -> float:
    return float(stats["fourth_moment"] / max(stats["trace"] * dim, 1.0e-300))


def audit(args: argparse.Namespace) -> dict[str, Any]:
    primes = prime_factors_squarefree(args.row)
    states = crt_states(primes)
    xi, labels = build_xi(primes, states, args.xi_mode, args.dimension, args.quotient_basis)
    radius = target_radius(len(states), distinct_xi_count(xi), args)
    pairs = target_local_pairs(xi, radius, args.max_target_pairs)
    classical = moment_stats_from_pairs(xi, pairs)
    result: dict[str, Any] = {
        "claim_tested": "off-diagonal Bures generator diagonal-shadow identity check",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "row": args.row,
        "primes": primes,
        "state_count": len(states),
        "xi_labels": labels,
        "target_radius": radius,
        "target_pair_count": int(pairs.shape[0]),
        "classical_shadow": classical,
    }
    if len(states) <= args.explicit_max_states and int(pairs.shape[0]) <= args.explicit_max_pairs:
        h = matrix_from_pairs(len(states), pairs, args.phase)
        explicit = explicit_bures_tensors(h, xi)
        rho_diag = reference_probabilities(xi, args.beta, args.rho_mode)
        thermal = thermal_bures_tensors(h, xi, rho_diag)
        edge_formula = edge_formula_from_h(h, xi)
        deriv = np.array(explicit["derivation_second"], dtype=float)
        edge_symbol = np.array(edge_formula["symbol"], dtype=float)
        result["explicit_bures"] = explicit
        result["thermal_bures"] = thermal
        result["edge_formula"] = edge_formula
        result["summary"] = {
            "status": "EXPLICIT_BUILT",
            "target_pair_count": int(pairs.shape[0]),
            "classical_anisotropy": classical["anisotropy"],
            "classical_q4": classical["normalized_fourth_moment"],
            "classical_unit_symbol_fourth_ratio": unit_symbol_fourth_ratio(classical, xi.shape[1]),
            "bures_derivation_q4": edge_formula["normalized_fourth_moment"],
            "bures_unit_symbol_fourth_ratio": edge_formula["unit_symbol_fourth_ratio"],
            "max_abs_derivation_minus_edge_formula": float(np.max(np.abs(deriv - edge_symbol))),
            "max_abs_hamiltonian_symmetric_form": explicit["max_abs_hamiltonian_symmetric_form"],
            "max_abs_lindblad_minus_half_derivation": explicit["max_abs_lindblad_minus_half_derivation"],
            "rho_condition": thermal["rho_condition"],
            "thermal_max_abs_gamma_hamiltonian": thermal["max_abs_gamma_hamiltonian"],
            "thermal_max_abs_gamma_cross": thermal["max_abs_gamma_cross"],
            "thermal_full_image_unit_symbol_fourth_ratio": thermal["full_generator_image"]["unit_symbol_fourth_ratio"],
            "thermal_max_abs_sld_image_cross_second": thermal["max_abs_sld_image_cross_second"],
        }
    else:
        result["summary"] = {
            "status": "SHADOW_ONLY_TOO_LARGE_FOR_EXPLICIT_MATRIX",
            "target_pair_count": int(pairs.shape[0]),
            "classical_anisotropy": classical["anisotropy"],
            "classical_q4": classical["normalized_fourth_moment"],
            "classical_unit_symbol_fourth_ratio": unit_symbol_fourth_ratio(classical, xi.shape[1]),
            "reason": f"state_count={len(states)} pairs={pairs.shape[0]} exceed explicit caps",
        }
    return result


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Bures Off-Diagonal Generator Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- Row: {result['row']}",
        f"- State count: {result['state_count']}",
        f"- xi labels: `{result['xi_labels']}`",
        f"- target radius: {fmt(result['target_radius'])}",
        f"- target pair count: {result['target_pair_count']}",
        f"- classical shadow anisotropy: {fmt(s['classical_anisotropy'])}",
        f"- classical shadow q4: {fmt(s['classical_q4'])}",
        f"- classical unit-symbol fourth ratio: {fmt(s['classical_unit_symbol_fourth_ratio'])}",
        "",
    ]
    if s["status"] == "EXPLICIT_BUILT":
        lines.extend(
            [
                "## Explicit Bures Checks",
                "",
                f"- Bures derivation q4: {fmt(s['bures_derivation_q4'])}",
                f"- Bures unit-symbol fourth ratio: {fmt(s['bures_unit_symbol_fourth_ratio'])}",
                f"- max |derivation second - edge formula|: {fmt(s['max_abs_derivation_minus_edge_formula'])}",
                f"- max |Hamiltonian symmetric form|: {fmt(s['max_abs_hamiltonian_symmetric_form'])}",
                f"- max |Lindblad - 1/2 derivation|: {fmt(s['max_abs_lindblad_minus_half_derivation'])}",
                f"- thermal rho condition: {fmt(s['rho_condition'])}",
                f"- thermal max |Gamma_H|: {fmt(s['thermal_max_abs_gamma_hamiltonian'])}",
                f"- thermal max |Gamma cross|: {fmt(s['thermal_max_abs_gamma_cross'])}",
                f"- thermal full-image unit-symbol fourth ratio: {fmt(s['thermal_full_image_unit_symbol_fourth_ratio'])}",
                f"- thermal max |SLD image cross second|: {fmt(s['thermal_max_abs_sld_image_cross_second'])}",
                "",
                "## Interpretation",
                "",
                "This is a diagonal-shadow consistency check, not a",
                "coherent-sector no-go.  The observables are",
                "X_mu=diag(xi_mu), so the Markov carre-du-champ is evaluated",
                "only on a commuting subalgebra.",
                "",
                "For diagonal physical observables at the maximally mixed state, the",
                "off-diagonal SLD/Bures derivation norm is exactly the edge-weight",
                "shadow with weights |H_ij|^2. The pure Hamiltonian commutator is",
                "skew-adjoint and contributes zero symmetric Dirichlet form. The",
                "Hermitian Lindblad dissipator gives one half of the derivation",
                "quadratic form. The raw q4 changes under the global Bures scale,",
                "so the scale-invariant comparison is the unit-symbol fourth ratio;",
                "there the off-diagonal realization matches the diagonal edge",
                "shadow rather than reducing its locality cost.",
                "",
                "For non-maximally mixed diagonal rho, the reported Gamma cross",
                "term is a residual of three evaluations of a linear map:",
                "Gamma_{H+D}-Gamma_H-Gamma_D. It is therefore algebraically zero,",
                "with the displayed value only measuring floating-point noise. The",
                "Hamiltonian derivation also cancels from Gamma on these observables",
                "by the Leibniz rule. The SLD norm of the generator image can have a",
                "Hamiltonian/dissipative cross term, but that is a different",
                "diagnostic from the symmetric Dirichlet form used for reversible",
                "Green-kernel recovery.",
                "",
                "The live coherent-route question is not addressed here: compute",
                "the Green kernel from the non-symmetric resolvent of a genuinely",
                "non-reversible quantum generator on the relevant quotient/full",
                "algebra, without replacing that resolvent by Gamma on the diagonal",
                "subalgebra.",
                "",
            ]
        )
    else:
        lines.extend(["## Interpretation", "", s["reason"], ""])
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
    parser.add_argument("--explicit-max-states", type=int, default=64)
    parser.add_argument("--explicit-max-pairs", type=int, default=20_000)
    parser.add_argument("--phase", choices=["real", "alternating", "four_phase"], default="four_phase")
    parser.add_argument("--beta", type=float, default=0.75)
    parser.add_argument("--rho-mode", choices=["uniform", "norm2", "first"], default="norm2")
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
