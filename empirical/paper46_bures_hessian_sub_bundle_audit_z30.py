#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
paper46_bures_hessian_sub_bundle_audit_z30.py
================================================

Paper 46 (proposed) C5 geometric realization on D(C^30):
Bures-Hessian sub-bundle audit on the next primorial row Z/30.

Generalizes the Paper 32 sec 13.2B audit triad from D(C^6) to D(C^30):
verifies the hybrid signature pattern
  - V-Lorentzian (1, n_P) on a (1 + n_P)-dim V-supported tangent sub-bundle
    from the 2nd-order Hessian of the V-Casimir;
  - M-Euclidean positive-semidefinite on a (dim_M)-dim M-supported tangent
    sub-bundle from the 4th-order quartic form of m^2_simplex;
  - HS-orthogonal sub-bundles at machine precision;
  - flat (29 - n_P - (dim_M - 22))-dim complement.

Anchored objects (Paper 35 sec 3.3):
  - V/M conductor-lattice partition of (Z/30)^* \ {0}:
      V_idx = [6, 10, 12, 15, 18, 20, 24]   (dim 7,  single-prime conductor)
      M_idx = remaining 22 indices         (dim 22, composite-divisor conductor)
    Verified by integer arithmetic: gcd(k, 30) determines packet for each k.

  - Bures-Hessian metric on D(C^30) at rho_* = I_30/30: positive-definite
    on the 899-dim tangent space (Paper 18 sec 6, [P]).

  - Pontryagin character orthogonality on (Z/30)^*: <chi_k|chi_l> = 30 delta_{k,l}.
    Forces V perp M as Hilbert subspaces of C^30 (audit delta, [P]).

Construction of V-supported operators (analogous to Paper 32 sec 13.2 H, P_a):

  Identify V with C^7 via the column-isometry V_iso = char_basis(30)[:, V_idx]
  (7 unit-norm columns).  Build a 7x7 Hermitian Cartan H_V = diag(1, -1, 0,..,0)
  (analog of lambda_3 on 3x3).  Build n_P = dim_V - 1 = 6 spacelike Hermitian
  P_a (off-diagonal real-symmetric and imaginary-antisymmetric):

    P_1 = E_12 + E_21
    P_2 = -i E_12 + i E_21
    P_3 = E_13 + E_31
    P_4 = -i E_13 + i E_31
    P_5 = E_23 + E_32
    P_6 = (diagonal Cartan analog of lambda_8: diag(1, 1, -2, 0, 0, 0, 0)/sqrt(3))

  Promote to C^30 by  H_30 = V_iso @ H_V @ V_iso^H,  similarly for P_a.

Dispersion-Casimir on D(C^30):

  I_complex(rho) := <H>^2(rho) + alpha^2 * (m^2_simplex(rho))^2 - sum_a <P_a>^2(rho)

  where m^2_simplex(rho) := sum_{k in M_idx} (<chi_k|rho|chi_k> - 1/30)^2
  is the natural M-supported simplex-mass proxy (Paper 20 sec 3 analog).

Predicted signatures (Paper 47 (proposed) Theorem 3.1 + audit delta):

  Hessian of I_real(rho) at rho_*:
    signature (1, n_P, 899 - 1 - n_P) = (1, 6, 892)
    The (1, 6) Lorentzian sub-bundle is 7-dim, contained in V-supported tangent
    directions.  The remaining 892 zero modes contain all M-supported tangent
    directions.

  Quartic form (m^2_simplex(rho_*+X))^2:
    signature on m^2_simplex itself (quadratic in X): (dim_M, 0, 899 - dim_M)
    = (22, 0, 877).  Positive-semidefinite on the 22-dim M-diagonal sub-bundle.

  HS-orthogonality of V-Lorentzian and M-Euclidean sub-bundles: machine floor.

Computation cost:
  Tangent-space basis size:  30^2 - 1 = 899 traceless Hermitian operators.
  Hessian matrix: 899 x 899 symmetric real.
  Eigendecomposition: O((899)^3) ~ 7e8 ops, sub-second on numpy/LAPACK.
  Total wall time estimate: < 10 seconds CPU.
"""

from __future__ import annotations
import sys
import math
import time
import numpy as np
from numpy.linalg import eigvalsh, eigh, norm

EPS = 1e-10


# ---------- Conductor lattice on Z/N (audit delta machinery) ----------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


def V_M_indices(N: int) -> tuple[list[int], list[int]]:
    """Partition (Z/N)^* \ {0} into single-prime V_idx and composite M_idx."""
    V_idx: list[int] = []
    M_idx: list[int] = []
    for k in range(1, N):
        d = N // math.gcd(k, N)
        (V_idx if is_prime(d) else M_idx).append(k)
    return V_idx, M_idx


def char_basis(N: int) -> np.ndarray:
    """N x N DFT character basis, columns orthonormal in C^N."""
    j = np.arange(N).reshape(-1, 1)
    k = np.arange(N).reshape(1, -1)
    return np.exp(2j * np.pi * j * k / N) / np.sqrt(N)


# ---------- Generalized Gell-Mann operators on dim-d Hermitian traceless ----------
def gellmann_like(d: int) -> tuple[np.ndarray, list[np.ndarray]]:
    """Construct a Cartan + spacelike operator set on the d-dim subspace.

    Returns (H_V, P_V_list) where:
      H_V is d x d Hermitian traceless: diag(1, -1, 0, .., 0).
      P_V_list has length d-1: a mix of off-diagonal and Cartan operators
      analogous to lambda_1, lambda_2, lambda_4, lambda_5, lambda_6, ..., lambda_d^2-1.

    Specifically we include:
      - real symmetric off-diagonal E_ij + E_ji   for j = i+1 (chains)
      - imaginary antisymmetric -i E_ij + i E_ji  for j = i+1
      - one extra diagonal Cartan analogous to lambda_8: diag(1, 1, -2, 0,..,0)/sqrt(3)
      until we have d-1 total P_a.
    """
    H_V = np.zeros((d, d), dtype=complex)
    H_V[0, 0] = 1.0
    H_V[1, 1] = -1.0
    # H_V is traceless if d >= 2.

    P_V_list: list[np.ndarray] = []

    # 1.  Real symmetric chain off-diagonal: E_{i, i+1} + E_{i+1, i}, i = 0..d-2
    for i in range(d - 1):
        P = np.zeros((d, d), dtype=complex)
        P[i, i + 1] = 1.0
        P[i + 1, i] = 1.0
        P_V_list.append(P)
        if len(P_V_list) >= d - 1:
            return H_V, P_V_list

    # 2.  Imaginary antisymmetric chain off-diagonal
    for i in range(d - 1):
        P = np.zeros((d, d), dtype=complex)
        P[i, i + 1] = -1j
        P[i + 1, i] = 1j
        P_V_list.append(P)
        if len(P_V_list) >= d - 1:
            return H_V, P_V_list

    # 3.  Cartan generators of the lambda_8 type
    for k in range(2, d):
        D = np.zeros(d)
        D[:k] = 1.0
        D[k] = -float(k)
        # Normalize so tr(D^2) = 2 (Gell-Mann normalization)
        D = D * np.sqrt(2.0 / (k * (k + 1)))
        P_V_list.append(np.diag(D).astype(complex))
        if len(P_V_list) >= d - 1:
            return H_V, P_V_list

    return H_V, P_V_list


# ---------- Promote V-operators to ambient C^N via column isometry ----------
def promote_V_to_N(A_V: np.ndarray, V_iso: np.ndarray) -> np.ndarray:
    """A_V is dim_V x dim_V Hermitian.  Return ambient N x N: V_iso @ A_V @ V_iso^H."""
    return V_iso @ A_V @ V_iso.conj().T


# ---------- M-supported simplex mass proxy ----------
def m2_simplex(rho: np.ndarray, C_basis: np.ndarray, M_idx: list[int], N: int) -> float:
    """m^2_simplex(rho) = sum_{k in M_idx} (<chi_k|rho|chi_k> - 1/N)^2.
    Vanishes at rho_* = I/N; quadratic in deviations along the M-diagonal."""
    rho_char_diag = np.diag(C_basis.conj().T @ rho @ C_basis).real
    M_diff = rho_char_diag[M_idx] - 1.0 / N
    return float(np.sum(M_diff ** 2))


# ---------- Casimirs ----------
def casimir_real(rho: np.ndarray, H_N: np.ndarray, P_N_list: list[np.ndarray]) -> float:
    eH = np.real(np.trace(H_N @ rho))
    eP = [np.real(np.trace(P @ rho)) for P in P_N_list]
    return float(eH ** 2 - sum(p ** 2 for p in eP))


def casimir_complex(rho: np.ndarray, H_N: np.ndarray, P_N_list: list[np.ndarray],
                    alpha: float, C_basis: np.ndarray, M_idx: list[int], N: int) -> float:
    eH = np.real(np.trace(H_N @ rho))
    eP = [np.real(np.trace(P @ rho)) for P in P_N_list]
    m2 = m2_simplex(rho, C_basis, M_idx, N)
    return float(eH ** 2 + (alpha ** 2) * (m2 ** 2) - sum(p ** 2 for p in eP))


# ---------- Traceless Hermitian basis on C^N ----------
def basis_traceless_hermitian(N: int) -> list[np.ndarray]:
    """Construct an HS-orthogonal basis of N^2-1 traceless Hermitian N x N matrices.

    Construction:  N*(N-1)/2 real-symmetric off-diagonals (E_ij + E_ji),
                   N*(N-1)/2 imaginary-antisymmetric off-diagonals,
                   N-1 diagonal Cartan generators.
    Total = N(N-1) + (N-1) = N^2 - 1.

    Returns a list, each element is N x N complex Hermitian traceless,
    HS-orthogonal but NOT unit-normalized.  tr(T_a T_b) = 2 delta_ab.
    """
    basis: list[np.ndarray] = []

    # Real symmetric off-diagonal
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), dtype=complex)
            M[i, j] = 1.0
            M[j, i] = 1.0
            basis.append(M)

    # Imaginary antisymmetric off-diagonal
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), dtype=complex)
            M[i, j] = -1j
            M[j, i] = 1j
            basis.append(M)

    # Diagonal Cartan generators
    for k in range(1, N):
        D = np.zeros(N)
        D[:k] = 1.0
        D[k] = -float(k)
        D = D * np.sqrt(2.0 / (k * (k + 1)))
        basis.append(np.diag(D).astype(complex))

    assert len(basis) == N * N - 1, f"Basis size: {len(basis)} != {N*N - 1}"
    return basis


# ---------- The audit ----------
def banner(title: str) -> None:
    print()
    print("=" * 78)
    print(f" {title}")
    print("=" * 78)


def audit_bures_hessian(N: int = 30) -> dict:
    """Run the Bures-Hessian sub-bundle audit on D(C^N).
    Returns a dict of audit outputs (signatures, overlaps).
    """
    banner(f"Bures-Hessian sub-bundle audit on D(C^{N})")

    t0 = time.time()

    # --- Conductor lattice ---
    V_idx, M_idx = V_M_indices(N)
    dim_V = len(V_idx)
    dim_M = len(M_idx)
    print(f"  Conductor lattice on Z/{N}:")
    print(f"    V_idx (single-prime conductor, dim_V = {dim_V}): {V_idx}")
    print(f"    M_idx (composite-divisor, dim_M = {dim_M}): "
          f"{M_idx if dim_M <= 8 else f'[{M_idx[0]}, ..., {M_idx[-1]}] (full list elided)'}")

    # --- Character basis ---
    C_basis = char_basis(N)
    V_iso = C_basis[:, V_idx]  # N x dim_V column isometry
    M_iso = C_basis[:, M_idx]  # N x dim_M column isometry

    P_V = V_iso @ V_iso.conj().T   # N x N projector onto V
    P_M = M_iso @ M_iso.conj().T   # N x N projector onto M
    PV_PM_F = float(np.linalg.norm(P_V @ P_M, 'fro'))
    print(f"  Pontryagin check: ||P_V . P_M||_F = {PV_PM_F:.3e}  "
          f"(machine floor = {EPS:.0e})")
    assert PV_PM_F < EPS, "Pontryagin character orthogonality fails!"
    print(f"  V perp M at machine floor: YES")

    # --- V-supported operators ---
    H_V, P_V_list_V = gellmann_like(dim_V)
    n_P = len(P_V_list_V)
    H_N = promote_V_to_N(H_V, V_iso)
    P_N_list = [promote_V_to_N(P, V_iso) for P in P_V_list_V]
    print(f"  Constructed V-supported H ({dim_V} x {dim_V} promoted to N x N)")
    print(f"  Constructed n_P = {n_P} V-supported P_a operators")

    # --- (A) Casimir along V-rays: check it's quadratic exactly ---
    banner(f"(A) Casimir I_real(rho_*+tX) along V-rays")
    rho_star = np.eye(N, dtype=complex) / N
    alpha = 1.0

    # Test directions in V-traceless
    X_V_choices = [
        ("timelike  (X = H direction)", H_V),
        ("spacelike (X = P_1 direction)", P_V_list_V[0]),
        ("mixed     (X = (H + P_1)/sqrt(2))", (H_V + P_V_list_V[0]) / np.sqrt(2.0)),
    ]
    all_clean = True
    for label, X_V in X_V_choices:
        X_N = promote_V_to_N(X_V, V_iso)
        if abs(np.real(np.trace(X_N))) > EPS:
            print(f"  WARN: X has nonzero trace {np.trace(X_N)}")
        ratio_R = None
        for t in [0.001, 0.01, 0.05, 0.1]:
            rho = rho_star + t * X_N
            I_R = casimir_real(rho, H_N, P_N_list)
            I_C = casimir_complex(rho, H_N, P_N_list, alpha, C_basis, M_idx, N)
            m2 = m2_simplex(rho, C_basis, M_idx, N)
            r = I_R / (t * t)
            if ratio_R is None:
                ratio_R = r
            else:
                if abs(r - ratio_R) > 1e-8:
                    all_clean = False
            # Also: m2_simplex should be exactly zero along V-rays
            if abs(m2) > EPS:
                all_clean = False
        # Use the last t for reporting
        t_rep = 0.1
        rho = rho_star + t_rep * X_N
        I_R = casimir_real(rho, H_N, P_N_list)
        I_C = casimir_complex(rho, H_N, P_N_list, alpha, C_basis, M_idx, N)
        m2 = m2_simplex(rho, C_basis, M_idx, N)
        print(f"  {label}: t=0.1, I_R={I_R:.6f}, I_C={I_C:.6f}, "
              f"m^2_simplex={m2:.3e}, I_R/t^2={I_R/(t_rep**2):.6f}")
    print(f"  All V-ray checks gave I_R/t^2 constant + m^2_simplex == 0: "
          f"{'CONFIRMED' if all_clean else 'CHECK FAILED'}")

    # --- (B) Full Hessian + Quartic on tangent space ---
    banner(f"(B) Full D(C^{N}) tangent space: dim = {N*N - 1}")

    t1 = time.time()
    print(f"  Building {N*N - 1}-dim traceless Hermitian basis ...")
    basis_T = basis_traceless_hermitian(N)
    n = len(basis_T)
    print(f"  Basis size: {n} (expected {N*N - 1})")

    # Normalization: T_a / sqrt(tr T_a^2) gives orthonormal
    norms = np.array([float(np.sqrt(np.real(np.trace(T @ T)))) for T in basis_T])
    # tr(T @ T) = 2 for Gell-Mann-style basis; check
    assert np.allclose(norms, np.sqrt(2.0)), \
        f"basis norms not sqrt(2): min={norms.min()}, max={norms.max()}"
    print(f"  All basis elements have tr(T^2) = 2 (Gell-Mann normalization)")

    # --- Hessian of I_real ---
    # I_real(rho_* + X) = (tr H X)^2 - sum_a (tr P_a X)^2 (since I_real is exactly
    # quadratic in (rho - rho_*) when H, P_a are V-supported and rho_* is centroid).
    # d^2/dr_a dr_b I_real(...)|_0 = 2 [ h_a h_b - sum_k p_ka p_kb ]
    # where h_a = tr(H T_a), p_ka = tr(P_k T_a).
    print(f"  Computing Hessian of I_real on {n}-dim tangent (4-5 s estimated) ...")
    t2 = time.time()
    h = np.array([float(np.real(np.trace(H_N @ T))) for T in basis_T])
    p_arrays = [np.array([float(np.real(np.trace(P @ T))) for T in basis_T])
                for P in P_N_list]
    M_hess = 2.0 * (np.outer(h, h) - sum(np.outer(p, p) for p in p_arrays))

    # Normalize to orthonormal basis: T_a / sqrt(2)
    D = np.diag(1.0 / norms)
    M_hess_orth = D @ M_hess @ D
    print(f"  Hessian built in {time.time() - t2:.2f} s")

    print(f"  Eigendecomposing the {n} x {n} Hessian ...")
    t3 = time.time()
    evals_hess = np.sort(eigvalsh(M_hess_orth))
    print(f"  Eigendecomposition in {time.time() - t3:.2f} s")
    pos = int(np.sum(evals_hess > EPS))
    neg = int(np.sum(evals_hess < -EPS))
    zer = int(np.sum(np.abs(evals_hess) < EPS))
    expected_pos = 1
    expected_neg = n_P
    expected_zer = n - 1 - n_P
    print(f"  Hessian of I_real signature on {n}-dim tangent:")
    print(f"    (pos, neg, zero) = ({pos}, {neg}, {zer})")
    print(f"    expected          = ({expected_pos}, {expected_neg}, {expected_zer})  "
          f"(Lorentzian (1, {n_P}) on V's H+P_a sub-bundle + 0 elsewhere)")
    nonzero_evals = [e for e in evals_hess if abs(e) > EPS]
    print(f"    non-zero eigenvalues: "
          f"[{', '.join(f'{e:+.4f}' for e in nonzero_evals)}]")
    hess_signature_ok = (pos == expected_pos and neg == expected_neg and zer == expected_zer)

    # --- Quartic form m^2_simplex^2 ---
    print(f"\n  Computing quartic form (m^2_simplex(rho_*+X))^2 ...")
    t4 = time.time()
    # m^2_simplex(rho_*+X) = sum_{k in M_idx} (diag_char(X)_k)^2 (quadratic in X)
    # For X = sum_a r_a T_a: diag_char(X)_k = sum_a r_a g_{k,a}, where
    # g_{k, a} = diag_char(T_a)_k = (chi_k^H T_a chi_k) on standard basis.
    diag_char_T = np.zeros((n, N))
    for a in range(n):
        diag_char_T[a, :] = np.diag(C_basis.conj().T @ basis_T[a] @ C_basis).real
    g_M = diag_char_T[:, M_idx]   # (n, dim_M)
    g_M_orth = g_M / norms[:, None]  # in orthonormal basis (T_a / sqrt(2))

    M_quad = np.zeros((n, n))
    for k_local in range(dim_M):
        v = g_M_orth[:, k_local]
        M_quad += np.outer(v, v)
    print(f"  Quartic form built in {time.time() - t4:.2f} s")

    evals_quad = np.sort(eigvalsh(M_quad))
    pos_q = int(np.sum(evals_quad > EPS))
    neg_q = int(np.sum(evals_quad < -EPS))
    zer_q = int(np.sum(np.abs(evals_quad) < EPS))
    print(f"  Quadratic-in-X form (m^2_simplex) signature on {n}-dim r-space:")
    print(f"    (pos, neg, zero) = ({pos_q}, {neg_q}, {zer_q})")
    print(f"    expected         = ({dim_M}, 0, {n - dim_M})  "
          f"(positive-semidefinite on M-diagonal sub-bundle)")
    quad_signature_ok = (pos_q == dim_M and neg_q == 0 and zer_q == n - dim_M)

    # --- HS-orthogonality of V-Lorentzian and M-Euclidean sub-bundles ---
    print(f"\n  HS-orthogonality check: V-Lorentzian vs M-Euclidean sub-bundles")
    t5 = time.time()
    evals_hess2, evecs_hess = eigh(M_hess_orth)
    evals_quad2, evecs_quad = eigh(M_quad)

    V_lorentz = evecs_hess[:, np.abs(evals_hess2) > EPS]   # (n, 1 + n_P)
    M_pos = evecs_quad[:, evals_quad2 > EPS]              # (n, dim_M)

    overlap = V_lorentz.conj().T @ M_pos
    sv = np.linalg.svd(overlap, compute_uv=False)
    max_sv = float(np.max(sv))
    print(f"  Eigendecomposition + overlap in {time.time() - t5:.2f} s")
    print(f"  V-Lorentzian sub-bundle dim: {V_lorentz.shape[1]}  (expected {1 + n_P})")
    print(f"  M-Euclidean sub-bundle dim:  {M_pos.shape[1]}  (expected {dim_M})")
    print(f"  Singular values of (V-Lorentzian)^H (M-Euclidean):")
    print(f"    {[f'{s:.3e}' for s in sv]}")
    print(f"  Max singular value (overlap): {max_sv:.3e}")
    orthogonality_ok = max_sv < EPS
    print(f"  HS-orthogonal at machine floor: "
          f"{'YES' if orthogonality_ok else 'NO'}")

    total_time = time.time() - t0
    print(f"\n  Total audit wall time: {total_time:.2f} s")

    return {
        "N": N,
        "dim_V": dim_V,
        "dim_M": dim_M,
        "n_P": n_P,
        "PV_PM_Frobenius": PV_PM_F,
        "hess_signature": (pos, neg, zer),
        "expected_hess": (expected_pos, expected_neg, expected_zer),
        "hess_signature_ok": hess_signature_ok,
        "quad_signature": (pos_q, neg_q, zer_q),
        "expected_quad": (dim_M, 0, n - dim_M),
        "quad_signature_ok": quad_signature_ok,
        "V_lorentz_dim": int(V_lorentz.shape[1]),
        "M_pos_dim": int(M_pos.shape[1]),
        "max_overlap_singular_value": max_sv,
        "orthogonality_ok": orthogonality_ok,
        "wall_time_s": total_time,
        "V_rays_clean": all_clean,
    }


def main() -> int:
    print("#" * 78)
    print("#  Paper 46 (proposed) C5 geometric realization on D(C^30)")
    print("#  Bures-Hessian sub-bundle audit on the next primorial row Z/30")
    print("#  CPU-tractable extension of Paper 32 sec 13.2B audit triad")
    print("#" * 78)

    results = audit_bures_hessian(N=30)

    banner("VERDICT")
    print(f"  (A) Casimir along V-rays exactly quadratic + m^2_simplex == 0: "
          f"{'CONFIRMED' if results['V_rays_clean'] else 'FAILED'}")
    print()
    print(f"  (B) Hessian of I_real signature: {results['hess_signature']} "
          f"(expected {results['expected_hess']}): "
          f"{'CONFIRMED' if results['hess_signature_ok'] else 'MISMATCH'}")
    print(f"      The V-Lorentzian (1, {results['n_P']}) sub-bundle is "
          f"{results['V_lorentz_dim']}-dimensional, supported on V-tangent directions.")
    print()
    print(f"  (C) Quartic m^2_simplex signature: {results['quad_signature']} "
          f"(expected {results['expected_quad']}): "
          f"{'CONFIRMED' if results['quad_signature_ok'] else 'MISMATCH'}")
    print(f"      The M-Euclidean (positive-semidefinite) sub-bundle is "
          f"{results['M_pos_dim']}-dimensional, supported on M-diagonal directions.")
    print()
    print(f"  (D) V-Lorentzian and M-Euclidean sub-bundles HS-orthogonal "
          f"at machine precision: "
          f"{'CONFIRMED' if results['orthogonality_ok'] else 'FAILED'}")
    print(f"      Max overlap singular value: {results['max_overlap_singular_value']:.3e}")
    print()
    print(f"  Wall time: {results['wall_time_s']:.2f} s")
    print()

    all_ok = (results['V_rays_clean'] and results['hess_signature_ok']
              and results['quad_signature_ok'] and results['orthogonality_ok'])

    if all_ok:
        banner("STRUCTURAL SETTLEMENT")
        print("  The Hartle-Hawking signature pattern of Paper 32 sec 13.2B")
        print(f"  extends to D(C^30) (the next primorial row):")
        print()
        print(f"    V-Lorentzian (1, {results['n_P']}) sub-bundle of dim "
              f"{results['V_lorentz_dim']}, supported on V-traceless directions,")
        print(f"    exact along V-rays (quadratic in t, no higher-order corrections).")
        print()
        print(f"    M-Euclidean positive-semidefinite sub-bundle of dim "
              f"{results['M_pos_dim']}, supported on M-diagonal directions,")
        print(f"    from the 4th-order quartic form (m^2_simplex)^2.")
        print()
        print(f"    HS-orthogonal at machine precision "
              f"(max singular value {results['max_overlap_singular_value']:.3e}).")
        print()
        print(f"  Flat (29 - 1 - {results['n_P']} - {results['M_pos_dim']} + ...)")
        print(f"  = {899 - results['V_lorentz_dim'] - results['M_pos_dim']} dim of")
        print(f"  flat tangent directions (zero in both Hessian and 4th-order quartic).")
        print()
        print("  Paper 46 (proposed) C5 geometric realization extends from D(C^6)")
        print("  to D(C^30) at the [P] tier (deterministic float audit, machine-floor")
        print("  precision).  K-branch realized on the next primorial row.")
        return 0
    else:
        banner("FAILED")
        print("  One or more audit predictions failed.  Investigate.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
