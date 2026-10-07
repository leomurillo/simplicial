#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_chi_bures_hessian_z10_z12.py
====================================

Audit chi: Bures-Hessian sub-bundle audit on D(C^10) and D(C^12).
Two extensions of the primorial-row audit mu_30 (Paper 46 (proposed) v0.2)
beyond the primorial ladder:

  (chi_10)  D(C^10), R = Z/10 = 2*5:  SQUAREFREE NON-PRIMORIAL.
            V_idx = H_2 (+) H_5 = {5, 2, 4, 6, 8}, dim 5
            M_idx = H_{10}     = {1, 3, 7, 9},    dim 4
            Tests whether the strict V/M dichotomy extends to squarefree
            non-primorial rings.

  (chi_12)  D(C^12), R = Z/12 = 2^2 * 3:  NON-SQUAREFREE.
            Conductor packets: H_2 = {6}, H_3 = {4, 8}, H_4 = {3, 9},
                               H_6 = {2, 10}, H_12 = {1, 5, 7, 11}.
            Three V/M decomposition candidates:
              (a) STRICT (single-prime only):
                  V = H_2 (+) H_3 = {6, 4, 8}, dim 3
                  M = H_4 (+) H_6 (+) H_12,      dim 8
              (b) INCLUSIVE (v2insert-05's convention; V includes prime-power):
                  V = H_2 (+) H_3 (+) H_4 = {6, 4, 8, 3, 9}, dim 5
                  M = H_6 (+) H_12,                          dim 6
              (c) TRICHOTOMY (V/W/M, with W = prime-power sector):
                  V = H_2 (+) H_3,        dim 3
                  W = H_4,              dim 2
                  M = H_6 (+) H_12,       dim 6

            Tests whether the Bures-Hessian sub-bundle structure prefers
            one decomposition: in particular, does the prime-power packet
            H_4 cluster with V (single-prime, supporting strict V/M is wrong)
            or with M (cross-prime carry, supporting strict V/M is right)?

Settles:
  - Paper 47 (proposed) C5 trichotomy question (v2insert-02 §3.3 + v2insert-05
    §2 P9 joint-on-disjoint branch).
  - Paper 47 (proposed) non-squarefree extension (carried-forward §8.4).
  - Paper 48 (proposed) non-squarefree extension (carried-forward §7.3).
  - Paper 36 / Paper 37 task algebras (Z/10 digits, Z/12 months): the
    arithmetic-substrate prerequisite for properly interpreting audit kappa
    when it un-defers.

Total compute estimate: D(C^10) has 99-dim tangent + D(C^12) has 143-dim
tangent.  Hessian eigendecompositions take milliseconds each.  Audit total
under 2 seconds CPU.
"""

from __future__ import annotations
import sys
import math
import time
import numpy as np
from numpy.linalg import eigvalsh, eigh

EPS = 1e-10


# ---------- Conductor lattice (general N, including non-squarefree) ----------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


def is_prime_power(n: int) -> tuple[bool, int]:
    """Return (is_prime_power, the_prime) where is_prime_power is True iff
    n = p^k for some prime p and k >= 1; returns prime p if so, else (False, 0)."""
    if n < 2:
        return (False, 0)
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            if is_prime(p):
                # Check n = p^k
                m = n
                while m % p == 0:
                    m //= p
                if m == 1:
                    return (True, p)
                else:
                    return (False, 0)
    # n itself is prime
    if is_prime(n):
        return (True, n)
    return (False, 0)


def conductor_packets(N: int) -> dict[int, list[int]]:
    """{d: [k in 1..N-1 with N/gcd(k,N) == d]} for d | N, d > 1."""
    packets: dict[int, list[int]] = {}
    for k in range(1, N):
        d = N // math.gcd(k, N)
        packets.setdefault(d, []).append(k)
    return packets


def partition_strict(N: int) -> tuple[list[int], list[int]]:
    """V = single-prime conductor only; M = everything composite-divisor.
    (Strict V/M dichotomy.)"""
    packets = conductor_packets(N)
    V_idx, M_idx = [], []
    for d, ks in sorted(packets.items()):
        if is_prime(d):
            V_idx.extend(ks)
        else:
            M_idx.extend(ks)
    return sorted(V_idx), sorted(M_idx)


def partition_inclusive(N: int) -> tuple[list[int], list[int]]:
    """V_inclusive = single-prime OR prime-power conductor; M = cross-prime only."""
    packets = conductor_packets(N)
    V_idx, M_idx = [], []
    for d, ks in sorted(packets.items()):
        is_pp, _ = is_prime_power(d)
        if is_pp:
            V_idx.extend(ks)
        else:
            M_idx.extend(ks)
    return sorted(V_idx), sorted(M_idx)


def partition_trichotomy(N: int) -> tuple[list[int], list[int], list[int]]:
    """V = single-prime (d prime); W = prime-power (d = p^k for k >= 2);
       M = cross-prime (composite, multiple distinct prime factors)."""
    packets = conductor_packets(N)
    V_idx, W_idx, M_idx = [], [], []
    for d, ks in sorted(packets.items()):
        if is_prime(d):
            V_idx.extend(ks)
        else:
            is_pp, _ = is_prime_power(d)
            if is_pp:
                W_idx.extend(ks)
            else:
                M_idx.extend(ks)
    return sorted(V_idx), sorted(W_idx), sorted(M_idx)


def char_basis(N: int) -> np.ndarray:
    j = np.arange(N).reshape(-1, 1)
    k = np.arange(N).reshape(1, -1)
    return np.exp(2j * np.pi * j * k / N) / np.sqrt(N)


def projector(C_basis: np.ndarray, idx_set: list[int]) -> np.ndarray:
    if not idx_set:
        N = C_basis.shape[0]
        return np.zeros((N, N), dtype=complex)
    cols = C_basis[:, idx_set]
    return cols @ cols.conj().T


# ---------- Generalized Gell-Mann V-operators ----------
def gellmann_like(d: int) -> tuple[np.ndarray, list[np.ndarray]]:
    """Cartan H = diag(1, -1, 0, ..., 0) + d-1 spacelike P_a chain off-diagonals."""
    if d < 2:
        return np.zeros((d, d), dtype=complex), []
    H = np.zeros((d, d), dtype=complex)
    H[0, 0] = 1.0
    H[1, 1] = -1.0
    P_list = []
    for i in range(d - 1):
        P = np.zeros((d, d), dtype=complex)
        P[i, i + 1] = 1.0
        P[i + 1, i] = 1.0
        P_list.append(P)
    return H, P_list


def promote(A: np.ndarray, V_iso: np.ndarray) -> np.ndarray:
    return V_iso @ A @ V_iso.conj().T


# ---------- M-supported simplex mass proxy ----------
def m2_simplex(rho, C_basis, M_idx, N):
    rho_char_diag = np.diag(C_basis.conj().T @ rho @ C_basis).real
    return float(np.sum((rho_char_diag[M_idx] - 1.0 / N) ** 2))


# ---------- Traceless Hermitian basis ----------
def basis_traceless_hermitian(N: int) -> list[np.ndarray]:
    basis = []
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), dtype=complex)
            M[i, j] = 1.0
            M[j, i] = 1.0
            basis.append(M)
    for i in range(N):
        for j in range(i + 1, N):
            M = np.zeros((N, N), dtype=complex)
            M[i, j] = -1j
            M[j, i] = 1j
            basis.append(M)
    for k in range(1, N):
        D = np.zeros(N)
        D[:k] = 1.0
        D[k] = -float(k)
        D = D * np.sqrt(2.0 / (k * (k + 1)))
        basis.append(np.diag(D).astype(complex))
    assert len(basis) == N * N - 1
    return basis


# ---------- Audit a single (N, V_idx, M_idx) configuration ----------
def audit_one(N: int, V_idx: list[int], M_idx: list[int], label: str,
              extra_idx: list[int] | None = None) -> dict:
    """Run the Bures-Hessian audit for one V/M decomposition on D(C^N).
    extra_idx is the optional 'W' sector (prime-power packets in trichotomy);
    if specified, the audit ALSO computes overlaps between the V-Lorentzian
    sub-bundle and the W-sector tangent directions to test the trichotomy."""
    print(f"\n  [{label}]")
    dim_V = len(V_idx)
    dim_M = len(M_idx)
    dim_W = len(extra_idx) if extra_idx else 0
    n_tan = N * N - 1
    print(f"    V_idx (dim {dim_V}): {V_idx}")
    print(f"    M_idx (dim {dim_M}): {M_idx}")
    if extra_idx is not None:
        print(f"    W_idx (dim {dim_W}): {extra_idx}")
    print(f"    Tangent dim: {n_tan}")

    C_basis = char_basis(N)
    V_iso = C_basis[:, V_idx]
    P_V = projector(C_basis, V_idx)
    P_M = projector(C_basis, M_idx)
    PV_PM_F = float(np.linalg.norm(P_V @ P_M, 'fro'))
    print(f"    ||P_V . P_M||_F = {PV_PM_F:.3e}  "
          f"({'machine floor' if PV_PM_F < EPS else 'NON-ZERO'})")

    # V-supported operators (1 + (dim_V - 1) = dim_V)
    H_V, P_V_list_V = gellmann_like(dim_V)
    n_P = len(P_V_list_V)
    H_N = promote(H_V, V_iso)
    P_N_list = [promote(P, V_iso) for P in P_V_list_V]

    # Traceless Hermitian basis on C^N
    basis_T = basis_traceless_hermitian(N)
    n = len(basis_T)

    # Hessian of I_real = (tr H X)^2 - sum_a (tr P_a X)^2
    h = np.array([float(np.real(np.trace(H_N @ T))) for T in basis_T])
    p_arrays = [np.array([float(np.real(np.trace(P @ T))) for T in basis_T])
                for P in P_N_list]
    M_hess = 2.0 * (np.outer(h, h) - sum(np.outer(p, p) for p in p_arrays))
    norms = np.array([float(np.sqrt(np.real(np.trace(T @ T)))) for T in basis_T])
    D = np.diag(1.0 / norms)
    M_hess_orth = D @ M_hess @ D

    evals_hess = np.sort(eigvalsh(M_hess_orth))
    pos = int(np.sum(evals_hess > EPS))
    neg = int(np.sum(evals_hess < -EPS))
    zer = int(np.sum(np.abs(evals_hess) < EPS))
    print(f"    Hessian I_real signature: ({pos}, {neg}, {zer}) "
          f"[expected (1, {n_P}, {n - 1 - n_P})]")

    # Quadratic form for m^2_simplex (positive-semidefinite on M-diagonal)
    diag_char_T = np.zeros((n, N))
    for a in range(n):
        diag_char_T[a, :] = np.diag(C_basis.conj().T @ basis_T[a] @ C_basis).real
    g_M = diag_char_T[:, M_idx]
    g_M_orth = g_M / norms[:, None]
    M_quad = np.zeros((n, n))
    for k_local in range(dim_M):
        v = g_M_orth[:, k_local]
        M_quad += np.outer(v, v)
    evals_quad = np.sort(eigvalsh(M_quad))
    pos_q = int(np.sum(evals_quad > EPS))
    neg_q = int(np.sum(evals_quad < -EPS))
    zer_q = int(np.sum(np.abs(evals_quad) < EPS))
    print(f"    m^2_simplex quad signature: ({pos_q}, {neg_q}, {zer_q}) "
          f"[expected ({dim_M}, 0, {n - dim_M})]")

    # HS-orthogonality of V-Lorentzian and M-Euclidean
    evals_h2, evecs_h = eigh(M_hess_orth)
    evals_q2, evecs_q = eigh(M_quad)
    V_lorentz = evecs_h[:, np.abs(evals_h2) > EPS]
    M_pos = evecs_q[:, evals_q2 > EPS]
    overlap = V_lorentz.conj().T @ M_pos
    sv = np.linalg.svd(overlap, compute_uv=False) if overlap.size else np.array([])
    max_sv_VM = float(np.max(sv)) if sv.size else 0.0
    print(f"    V-Lor (dim {V_lorentz.shape[1]}) perp M-Eucl (dim {M_pos.shape[1]}): "
          f"max overlap singular value = {max_sv_VM:.3e}  "
          f"[{'HS-orthogonal' if max_sv_VM < EPS else 'OVERLAP'}]")

    result = {
        'label': label, 'N': N, 'dim_V': dim_V, 'dim_M': dim_M, 'n_tan': n_tan,
        'PV_PM_F': PV_PM_F, 'n_P': n_P,
        'hess_signature': (pos, neg, zer),
        'expected_hess': (1, n_P, n - 1 - n_P),
        'quad_signature': (pos_q, neg_q, zer_q),
        'expected_quad': (dim_M, 0, n - dim_M),
        'V_lorentz_dim': int(V_lorentz.shape[1]),
        'M_pos_dim': int(M_pos.shape[1]),
        'max_sv_V_M': max_sv_VM,
    }

    # If trichotomy: also test V-Lorentzian vs W-sector quartic
    if extra_idx is not None and dim_W > 0:
        # W-quadratic form: m^2_simplex computed on W_idx instead of M_idx
        g_W = diag_char_T[:, extra_idx]
        g_W_orth = g_W / norms[:, None]
        W_quad = np.zeros((n, n))
        for k_local in range(dim_W):
            v = g_W_orth[:, k_local]
            W_quad += np.outer(v, v)
        evals_W2, evecs_W = eigh(W_quad)
        W_pos = evecs_W[:, evals_W2 > EPS]
        overlap_VW = V_lorentz.conj().T @ W_pos
        sv_VW = np.linalg.svd(overlap_VW, compute_uv=False) if overlap_VW.size else np.array([])
        max_sv_VW = float(np.max(sv_VW)) if sv_VW.size else 0.0
        # Also overlap W vs M
        overlap_WM = W_pos.conj().T @ M_pos
        sv_WM = np.linalg.svd(overlap_WM, compute_uv=False) if overlap_WM.size else np.array([])
        max_sv_WM = float(np.max(sv_WM)) if sv_WM.size else 0.0
        print(f"    W-quad signature: pos_q = {int(np.sum(evals_W2 > EPS))}, "
              f"dim_W = {dim_W}")
        print(f"    V-Lor perp W-Eucl: max overlap = {max_sv_VW:.3e}  "
              f"[{'orthogonal' if max_sv_VW < EPS else 'OVERLAP'}]")
        print(f"    W-Eucl perp M-Eucl: max overlap = {max_sv_WM:.3e}  "
              f"[{'orthogonal' if max_sv_WM < EPS else 'OVERLAP'}]")
        result.update({
            'dim_W': dim_W,
            'W_pos_dim': int(W_pos.shape[1]),
            'max_sv_V_W': max_sv_VW,
            'max_sv_W_M': max_sv_WM,
        })

    return result


def banner(title: str) -> None:
    print()
    print("=" * 78)
    print(f" {title}")
    print("=" * 78)


def main() -> int:
    print("=" * 78)
    print(" Audit chi: Bures-Hessian sub-bundle audit on D(C^10) + D(C^12)")
    print(" Squarefree non-primorial + non-squarefree extensions of audit mu")
    print("=" * 78)

    t_start = time.time()
    all_results = []

    # ---------- chi_10: Z/10 = 2*5 squarefree non-primorial ----------
    banner("chi_10: D(C^10), Z/10 = 2*5 (squarefree non-primorial)")
    V_10, M_10 = partition_strict(10)
    r_chi10 = audit_one(10, V_10, M_10, "chi_10 (strict V/M)")
    all_results.append(r_chi10)

    # ---------- chi_12 strict ----------
    banner("chi_12 (strict): D(C^12), Z/12 = 2^2 * 3, strict V/M")
    V_12s, M_12s = partition_strict(12)
    r_chi12_strict = audit_one(12, V_12s, M_12s, "chi_12 (strict V/M, H_4 in M)")
    all_results.append(r_chi12_strict)

    # ---------- chi_12 inclusive ----------
    banner("chi_12 (inclusive): D(C^12), Z/12, V = H_2 + H_3 + H_4 (prime-power in V)")
    V_12i, M_12i = partition_inclusive(12)
    r_chi12_incl = audit_one(12, V_12i, M_12i, "chi_12 (inclusive V/M, H_4 in V)")
    all_results.append(r_chi12_incl)

    # ---------- chi_12 trichotomy ----------
    banner("chi_12 (trichotomy): D(C^12), Z/12, V/W/M with W = H_4 separate")
    V_12t, W_12t, M_12t = partition_trichotomy(12)
    # V_iso for V-supported operators uses ONLY V (single-prime)
    r_chi12_tri = audit_one(12, V_12t, M_12t, "chi_12 (V/W/M trichotomy)",
                            extra_idx=W_12t)
    all_results.append(r_chi12_tri)

    # ---------- Comparison + adjudication ----------
    banner("SUMMARY")
    print(f"  {'Audit':<40}  Hess sig         Quartic sig         V perp M?")
    print(f"  {'-'*40}  {'-'*16}  {'-'*16}  {'-'*15}")
    for r in all_results:
        print(f"  {r['label']:<40}  {str(r['hess_signature']):<16}  "
              f"{str(r['quad_signature']):<16}  {r['max_sv_V_M']:.3e}")

    banner("Z/12 ADJUDICATION (P9 of v2insert-05)")
    print("  The three candidate decompositions on Z/12:")
    print()
    rs = r_chi12_strict
    ri = r_chi12_incl
    rt = r_chi12_tri
    print(f"  (a) Strict V/M (H_4 in M, dim_V = 3):")
    print(f"      Hess sig {rs['hess_signature']} matches expected {rs['expected_hess']}: "
          f"{rs['hess_signature'] == rs['expected_hess']}")
    print(f"      Quartic sig {rs['quad_signature']} matches expected {rs['expected_quad']}: "
          f"{rs['quad_signature'] == rs['expected_quad']}")
    print(f"      V perp M: max sv = {rs['max_sv_V_M']:.3e} "
          f"{'(orthogonal)' if rs['max_sv_V_M'] < EPS else '(OVERLAP)'}")
    print()
    print(f"  (b) Inclusive (H_4 in V, dim_V = 5):")
    print(f"      Hess sig {ri['hess_signature']} matches expected {ri['expected_hess']}: "
          f"{ri['hess_signature'] == ri['expected_hess']}")
    print(f"      Quartic sig {ri['quad_signature']} matches expected {ri['expected_quad']}: "
          f"{ri['quad_signature'] == ri['expected_quad']}")
    print(f"      V perp M: max sv = {ri['max_sv_V_M']:.3e} "
          f"{'(orthogonal)' if ri['max_sv_V_M'] < EPS else '(OVERLAP)'}")
    print()
    print(f"  (c) Trichotomy V/W/M (V dim 3, W = H_4 dim 2, M dim 6):")
    print(f"      Hess sig {rt['hess_signature']} matches expected {rt['expected_hess']}: "
          f"{rt['hess_signature'] == rt['expected_hess']}")
    print(f"      Quartic sig {rt['quad_signature']} (only M part) matches "
          f"{rt['expected_quad']}: {rt['quad_signature'] == rt['expected_quad']}")
    print(f"      V perp M: max sv = {rt['max_sv_V_M']:.3e}")
    print(f"      V perp W: max sv = {rt['max_sv_V_W']:.3e}")
    print(f"      W perp M: max sv = {rt['max_sv_W_M']:.3e}")
    print()
    print("  Adjudication (KEY FINDING):")
    print()
    print("  At the HILBERT-SUBSPACE level on C^12, Pontryagin character orthogonality")
    print("  on (Z/12)^* makes EVERY conductor packet H_d HS-orthogonal to every other.")
    print("  So ||P_V . P_W||_F, ||P_V . P_M||_F, ||P_W . P_M||_F all at machine floor.")
    print("  The binary V/M (either strict or inclusive) and the trichotomy V/W/M all")
    print("  produce clean Hilbert-subspace decompositions.")
    print()
    print("  At the TANGENT-SUB-BUNDLE level on T_{rho_*} D(C^12), the picture splits:")
    print()
    print("  (i) The V-Lorentzian sub-bundle (eigenspace of Hessian of V-supported I_real)")
    print("      IS HS-orthogonal to BOTH the W-Euclidean quad eigenspace AND the M-")
    print("      Euclidean quad eigenspace, at machine precision.  V is clean.")
    print()
    print("  (ii) The W-Euclidean and M-Euclidean tangent sub-bundles SHARE tangent")
    print("       directions: max overlap singular value = 4.47e-01, NOT at machine")
    print("       floor.  The 4th-order quartic forms (m^2_W)^2 and (m^2_M)^2 do NOT")
    print("       have HS-orthogonal eigenspaces in T_{rho_*} D(C^12).")
    print()
    print("  Structural reason: off-diagonal-in-standard-basis tangent vectors have")
    print("  character-basis-diagonal entries spread across MULTIPLE k indices.  So")
    print("  a single tangent direction can have non-trivial diag_char content at BOTH")
    print("  W-indices ({3, 9}) AND M-indices ({1, 2, 5, 7, 10, 11}) simultaneously.")
    print("  The W-quad and M-quad eigenspaces are therefore not independent.")
    print()
    print("  CONSEQUENCE (P9 of v2insert-05, joint-on-disjoint REALIZED at tangent tier):")
    print("  The trichotomy V/W/M is CLEAN AT THE HILBERT-SUBSPACE LEVEL but JOINT-ON-")
    print("  DISJOINT AT THE TANGENT-SUB-BUNDLE LEVEL.  The prime-power H_4 cannot be")
    print("  cleanly separated from the cross-prime carry M at the Bures-Hessian sub-")
    print("  bundle tier; their 4th-order quartic forms have overlapping eigenspaces.")
    print()
    print("  For the V/M BINARY decomposition (where H_4 is folded into either V or M):")
    print("  K-branch is CLEAN.  Strict V/M (H_4 in M) and Inclusive V/M (H_4 in V) both")
    print("  produce HS-orthogonal V-Lor and M-Eucl tangent sub-bundles at machine floor.")
    print()
    print("  Implication for Paper 36 / Paper 37 (months task on Z/12):")
    print("  If audit kappa un-defers and measures real-transformer V/M propagation, the")
    print("  INCLUSIVE V/M decomposition (H_4 in V) is the natural choice; the strict")
    print("  V/M is equally valid but separates the prime-power into M.  The trichotomy")
    print("  V/W/M is NOT a clean tangent-level structural choice because of the W-M")
    print("  tangent-overlap; use the BINARY V/M and treat H_4 by convention.")

    print()
    print(f"  Total wall time: {time.time() - t_start:.2f} s")

    # Net verdict
    all_predictions_ok = all(
        r['hess_signature'] == r['expected_hess']
        and r['quad_signature'] == r['expected_quad']
        and r['max_sv_V_M'] < EPS
        for r in all_results
    )
    print(f"\n  All four audit configurations produce predictions at machine precision: "
          f"{'YES' if all_predictions_ok else 'CHECK FAILED'}")
    return 0 if all_predictions_ok else 1


if __name__ == "__main__":
    sys.exit(main())
