"""Bures Hamiltonian split audit.

This is the G_split gate for the conservative Schur program.  It does not try
to recover a Green kernel.  It asks whether a proposed physical/coherent split
is compatible with the leaf Poisson tensor of a conservative Bures/unitary
orbit.

The audit builds a diagonal faithful state rho_* on C[R], verifies that a
diagonal Hamiltonian has zero unitary vector field at rho_*, constructs the
real off-diagonal tangent basis of the unitary orbit, and forms the KKS
Poisson tensor J in 2x2 blocks for each unordered matrix-unit pair.

Candidate P-subspaces:

* diagonal_readout: invalid for unitary leaves; diagonal population directions
  are not tangent to the orbit.
* target_q_only: one quadrature for target-local pairs; expected to fail.
* target_symplectic_pairs: both quadratures for target-local pairs; expected
  to pass the block-compatibility gate.
* xi_q: three aggregate coordinate readouts on q-quadratures; expected to fail.
* xi_once_closure: span{xi_q, J xi_q}; may fail when KKS block weights vary.

The load-bearing metric is the relative J-cross block / invariance defect.  A
split can support the clean Hamiltonian Schur factorization only when P is a
nondegenerate J-invariant subspace, equivalently J_PQ and J_QP vanish in a
P/Q decomposition.
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
    prime_factors_squarefree,
    target_local_pairs,
    target_radius,
)


DEFAULT_REPORT = Path("empirical/reports/bures_hamiltonian_split_audit.md")
DEFAULT_JSON = Path("empirical/reports/bures_hamiltonian_split_audit.json")


def faithful_reference_state(xi: np.ndarray, beta: float, tie_breaker: float) -> np.ndarray:
    norm_sq = np.sum(xi * xi, axis=1)
    tilt = np.arange(xi.shape[0], dtype=float) / max(xi.shape[0] - 1, 1)
    logits = -beta * norm_sq - tie_breaker * tilt
    logits -= float(np.max(logits))
    weights = np.exp(logits)
    return weights / float(np.sum(weights))


def unitary_equilibrium_residual(rho: np.ndarray) -> float:
    h_eq = np.diag(-np.log(np.maximum(rho, 1.0e-300)))
    rho_matrix = np.diag(rho)
    vector_field = -1.0j * (h_eq @ rho_matrix - rho_matrix @ h_eq)
    return float(np.linalg.norm(vector_field))


def unordered_pairs(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def build_poisson_tensor(rho: np.ndarray, pairs: list[tuple[int, int]]) -> tuple[np.ndarray, dict[tuple[int, int], int], np.ndarray]:
    dim = 2 * len(pairs)
    j_matrix = np.zeros((dim, dim), dtype=float)
    pair_index: dict[tuple[int, int], int] = {}
    weights = np.zeros(len(pairs), dtype=float)
    for block, (i, j) in enumerate(pairs):
        pair_index[(i, j)] = block
        omega = float(rho[i] - rho[j])
        weights[block] = omega
        q = 2 * block
        p = q + 1
        j_matrix[q, p] = omega
        j_matrix[p, q] = -omega
    return j_matrix, pair_index, weights


def q_index(pair_index: dict[tuple[int, int], int], i: int, j: int) -> int:
    if i > j:
        i, j = j, i
    return 2 * pair_index[(i, j)]


def p_index(pair_index: dict[tuple[int, int], int], i: int, j: int) -> int:
    return q_index(pair_index, i, j) + 1


def unit_columns(dim: int, indices: list[int]) -> np.ndarray:
    if not indices:
        return np.zeros((dim, 0), dtype=float)
    mat = np.zeros((dim, len(indices)), dtype=float)
    for col, idx in enumerate(indices):
        mat[idx, col] = 1.0
    return mat


def orthonormal_basis(columns: np.ndarray, tolerance: float) -> np.ndarray:
    if columns.size == 0 or columns.shape[1] == 0:
        return np.zeros((columns.shape[0], 0), dtype=float)
    u, singular_values, _ = np.linalg.svd(columns, full_matrices=False)
    rank = int(np.sum(singular_values > tolerance))
    return u[:, :rank]


def split_metrics(name: str, columns: np.ndarray, j_matrix: np.ndarray, tolerance: float) -> dict[str, Any]:
    dim = j_matrix.shape[0]
    u_p = orthonormal_basis(columns, tolerance)
    p_dim = u_p.shape[1]
    if p_dim == 0:
        return {
            "name": name,
            "status": "INVALID_EMPTY_OR_NOT_TANGENT",
            "p_dim": 0,
            "q_dim": dim,
            "rank_J_PP": 0,
            "relative_cross": float("nan"),
            "relative_invariance_defect": float("nan"),
            "reason": "P has no nonzero tangent directions on the unitary leaf.",
        }

    projector_p = u_p @ u_p.T
    j_u = j_matrix @ u_p
    outside = (np.eye(dim) - projector_p) @ j_u
    invariance_defect = float(np.linalg.norm(outside) / max(np.linalg.norm(j_u), 1.0e-300))

    q_full, _ = np.linalg.qr(u_p, mode="complete")
    u_q = q_full[:, p_dim:]
    j_pp = u_p.T @ j_matrix @ u_p
    j_pq = u_p.T @ j_matrix @ u_q
    j_qp = u_q.T @ j_matrix @ u_p
    relative_cross = float(
        max(np.linalg.norm(j_pq), np.linalg.norm(j_qp)) / max(np.linalg.norm(j_matrix), 1.0e-300)
    )
    rank_j_pp = int(np.linalg.matrix_rank(j_pp, tol=tolerance))
    nondegenerate = p_dim % 2 == 0 and rank_j_pp == p_dim
    compatible = relative_cross <= tolerance and invariance_defect <= tolerance and nondegenerate
    return {
        "name": name,
        "status": "PASS_SYMPLECTIC_BLOCK" if compatible else "FAIL_SPLIT",
        "p_dim": p_dim,
        "q_dim": u_q.shape[1],
        "rank_J_PP": rank_j_pp,
        "nondegenerate_P": bool(nondegenerate),
        "relative_cross": relative_cross,
        "relative_invariance_defect": invariance_defect,
        "norm_J_PP": float(np.linalg.norm(j_pp)),
        "norm_J_PQ": float(np.linalg.norm(j_pq)),
        "norm_J_QP": float(np.linalg.norm(j_qp)),
    }


def candidate_columns(
    name: str,
    xi: np.ndarray,
    target_pairs: np.ndarray,
    pair_index: dict[tuple[int, int], int],
    j_matrix: np.ndarray,
) -> np.ndarray:
    dim = j_matrix.shape[0]
    if name == "diagonal_readout":
        return np.zeros((dim, 0), dtype=float)

    q_indices = [q_index(pair_index, int(i), int(j)) for i, j in target_pairs]
    p_indices = [idx + 1 for idx in q_indices]

    if name == "target_q_only":
        return unit_columns(dim, q_indices)
    if name == "target_symplectic_pairs":
        return unit_columns(dim, q_indices + p_indices)

    if name in {"xi_q", "xi_once_closure"}:
        cols = []
        for mu in range(xi.shape[1]):
            vec = np.zeros(dim, dtype=float)
            for i_raw, j_raw in target_pairs:
                i = int(i_raw)
                j = int(j_raw)
                vec[q_index(pair_index, i, j)] = xi[j, mu] - xi[i, mu]
            cols.append(vec)
        base = np.column_stack(cols) if cols else np.zeros((dim, 0), dtype=float)
        if name == "xi_q":
            return base
        return np.column_stack([base, j_matrix @ base])

    raise ValueError(f"unknown split candidate: {name}")


def audit(args: argparse.Namespace) -> dict[str, Any]:
    primes = prime_factors_squarefree(args.row)
    states = crt_states(primes)
    xi, labels = build_xi(primes, states, args.xi_mode, args.dimension, args.quotient_basis)
    if len(states) > args.max_states:
        raise ValueError(f"row has {len(states)} states, above --max-states={args.max_states}")
    radius = target_radius(len(states), distinct_xi_count(xi), args)
    target_pairs = target_local_pairs(xi, radius, args.max_target_pairs)
    rho = faithful_reference_state(xi, args.beta, args.tie_breaker)
    pairs = unordered_pairs(len(states))
    j_matrix, pair_index, weights = build_poisson_tensor(rho, pairs)
    skew_defect = float(np.max(np.abs(j_matrix + j_matrix.T)))
    rank_j = int(np.linalg.matrix_rank(j_matrix, tol=args.tolerance))
    candidates = [item.strip() for item in args.candidates.split(",") if item.strip()]
    split_results = []
    for candidate in candidates:
        columns = candidate_columns(candidate, xi, target_pairs, pair_index, j_matrix)
        split_results.append(split_metrics(candidate, columns, j_matrix, args.tolerance))
    return {
        "claim_tested": "G_split gate for conservative Bures Hamiltonian Schur reduction",
        "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        "row": args.row,
        "primes": primes,
        "state_count": len(states),
        "xi_labels": labels,
        "target_radius": radius,
        "target_pair_count": int(target_pairs.shape[0]),
        "unitary_orbit": {
            "real_dimension": int(j_matrix.shape[0]),
            "matrix_unit_pairs": len(pairs),
            "rho_min": float(np.min(rho)),
            "rho_max": float(np.max(rho)),
            "rho_condition": float(np.max(rho) / max(np.min(rho), 1.0e-300)),
            "min_abs_kks_weight": float(np.min(np.abs(weights))),
            "max_abs_kks_weight": float(np.max(np.abs(weights))),
            "equilibrium_residual": unitary_equilibrium_residual(rho),
            "skew_defect": skew_defect,
            "rank_J": rank_j,
        },
        "splits": split_results,
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    orbit = result["unitary_orbit"]
    lines = [
        "# Bures Hamiltonian Split Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Row: {result['row']} with primes `{result['primes']}`",
        f"- State count: {result['state_count']}",
        f"- xi labels: `{result['xi_labels']}`",
        f"- Target radius: {fmt(result['target_radius'])}",
        f"- Target-local pairs: {result['target_pair_count']}",
        "",
        "## G_eq / G_J",
        "",
        f"- unitary orbit real dimension: {orbit['real_dimension']}",
        f"- matrix-unit pairs: {orbit['matrix_unit_pairs']}",
        f"- rho condition: {fmt(orbit['rho_condition'])}",
        f"- min |KKS weight|: {fmt(orbit['min_abs_kks_weight'])}",
        f"- max |KKS weight|: {fmt(orbit['max_abs_kks_weight'])}",
        f"- equilibrium residual ||-i[H_eq,rho]||: {fmt(orbit['equilibrium_residual'])}",
        f"- skew defect max |J+J^T|: {fmt(orbit['skew_defect'])}",
        f"- rank J: {orbit['rank_J']}",
        "",
        "## G_split",
        "",
        "| split | status | dim P | rank J_PP | cross/J | invariance defect |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for split in result["splits"]:
        lines.append(
            "| {name} | {status} | {pdim} | {rank} | {cross} | {inv} |".format(
                name=split["name"],
                status=split["status"],
                pdim=split["p_dim"],
                rank=split["rank_J_PP"],
                cross=fmt(split["relative_cross"]) if np.isfinite(split["relative_cross"]) else "nan",
                inv=fmt(split["relative_invariance_defect"])
                if np.isfinite(split["relative_invariance_defect"])
                else "nan",
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The clean Hamiltonian Schur factorization is available only for a",
            "nondegenerate J-invariant P sector.  Diagonal population readout is",
            "not tangent to the unitary orbit.  Q-only or coordinate-only",
            "readouts fail because their conjugate partners live in Q.  A split",
            "made from complete matrix-unit quadrature pairs passes because it is",
            "symplectically block-compatible by construction.",
            "",
            "A PASS here does not prove localization or CRT canonicity.  It only",
            "says the proposed P/Q split is eligible for a conservative Schur",
            "stiffness audit.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def strict_jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: strict_jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [strict_jsonable(item) for item in value]
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        value = float(value)
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    return value


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
    parser.add_argument("--max-states", type=int, default=64)
    parser.add_argument("--beta", type=float, default=0.75)
    parser.add_argument("--tie-breaker", type=float, default=0.05)
    parser.add_argument("--tolerance", type=float, default=1.0e-10)
    parser.add_argument(
        "--candidates",
        default="diagonal_readout,target_q_only,target_symplectic_pairs,xi_q,xi_once_closure",
    )
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    json_result = strict_jsonable(result)
    args.json.write_text(json.dumps(json_result, indent=2, allow_nan=False), encoding="utf-8")
    print(
        json.dumps(
            strict_jsonable(
                {
                    "row": result["row"],
                    "orbit_dim": result["unitary_orbit"]["real_dimension"],
                    "target_pairs": result["target_pair_count"],
                    "skew_defect": result["unitary_orbit"]["skew_defect"],
                    "splits": {
                        split["name"]: {
                            "status": split["status"],
                            "p_dim": split["p_dim"],
                            "rank": split["rank_J_PP"],
                            "cross": split["relative_cross"],
                            "invariance": split["relative_invariance_defect"],
                        }
                        for split in result["splits"]
                    }
                }
            ),
            indent=2,
            allow_nan=False,
        )
    )


if __name__ == "__main__":
    main()
