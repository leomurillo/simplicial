"""
probe_T8p4_lemma_6p4_Q_matrix.py
================================

Numerical check of T8.4 Lemma 6.4 (sketched in T8.4 §6.4):

    The matrix
        Q(N, n)_{i,j} := R_{i+j+1} * <h_{i+j+1}, chi_1>,     i, j = 0, ..., n
    is positive semidefinite at primorial N >= 30 for every n >= 0.

Here:
    R_k                = 1 / sqrt(N * k * (k+1))                  (T9 §2.4)
    h_k                = (1, 1, ..., 1, -k, 0, ..., 0) in Z^N     (T9 §2.1; first k ones, then -k, then zeros)
    chi_c(s)           = omega^{c s},  omega = exp(2 pi i / N)
    <h_k, chi_c>       = sum_{s=1}^{k} omega^{cs}  -  k * omega^{c(k+1)}     (T9 Thm 2.1)

In particular for c = 1 (the principal-coset Helmert-Fourier coefficient that
appears after T8 §2.4's multiplicative selection rule has collapsed the
joint prime cumulant to the residue class n ≡ 1 mod N — see T8.4 §6.4),

    <h_k, chi_1> = sum_{s=1}^{k} omega^s  -  k * omega^{k+1}.

This is complex in general; Lemma 6.4 concerns its real part (the prime
cumulant is real, so any imaginary contribution must cancel against the
conjugate-pair partner in the actual joint sum — captured here by taking
the real part directly, which is the symmetric/Hermitian half of Q).

Per T8.4-PreviousPapersInsert §5: a focused numerical probe at N in {30, 210}
for n up to ~20 verifying Q(N, n) >= 0 supplies the empirical confirmation
the full Stieltjes-representation proof (forward to T8.4.2, the Apex-H paper)
will later make rigorous.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, mpc, sqrt, exp, pi, mpmathify, matrix, re, fabs

mp.dps = 60   # plenty for moderate n; Lemma 6.4 is a structural identity, not a delicate cancellation.


# ---------------------------------------------------------------------
# Core entries
# ---------------------------------------------------------------------

def helmert_radical(N, k):
    """R_k = 1 / sqrt(N k (k+1))  (T9 §2.4)."""
    return mpf(1) / sqrt(mpf(N) * mpf(k) * mpf(k + 1))


def helmert_fourier_c1(N, k):
    """
    <h_k, chi_1> = sum_{s=1}^{k} omega^s - k * omega^{k+1},
    omega = exp(2 pi i / N).
    Requires 1 <= k <= N - 1.
    """
    assert 1 <= k <= N - 1, f"Helmert axis k={k} out of range for N={N}"
    omega = exp(mpc(0, 1) * 2 * pi / mpf(N))
    s_sum = mpc(0, 0)
    w = mpc(1, 0)
    for _ in range(k):
        w = w * omega          # w = omega^1, ..., omega^k
        s_sum += w
    last = w * omega           # omega^{k+1}
    return s_sum - mpf(k) * last


def Q_entry(N, k):
    """Real part of R_k * <h_k, chi_1>  (Lemma 6.4 entry at axis k)."""
    return re(helmert_radical(N, k) * helmert_fourier_c1(N, k))


# ---------------------------------------------------------------------
# Q matrix + LDL diagnostic
# ---------------------------------------------------------------------

def Q_matrix(N, n):
    """Q(N, n)_{i,j} = R_{i+j+1} <h_{i+j+1}, chi_1>_re,  0 <= i, j <= n."""
    M = matrix(n + 1)
    diag_axes = [Q_entry(N, k) for k in range(1, 2 * n + 2)]
    for i in range(n + 1):
        for j in range(n + 1):
            M[i, j] = diag_axes[i + j]
    return M, diag_axes


def ldl_min_diagonal(M):
    """
    LDL^T factorization (no pivoting) of a symmetric matrix M.
    Returns (min_diag, ldl_diags) — min(D_ii) is the PSD certificate
    (>= 0 iff M is PSD, given symmetry).
    Returns (None, ...) if a zero pivot is encountered before completion.
    """
    n = M.rows
    A = matrix(M)   # copy
    D = []
    for i in range(n):
        d = A[i, i]
        D.append(d)
        if abs(d) < mpf(10) ** (-mp.dps + 5):
            # numerical zero — record and continue with zeros below (rank drop)
            for j in range(i + 1, n):
                A[j, i] = mpf(0)
            continue
        for j in range(i + 1, n):
            A[j, i] = A[j, i] / d
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                A[j, k] = A[j, k] - A[j, i] * d * A[i, k] / d * A[k, i] if False else A[j, k] - A[j, i] * d * A[i, k]
                # standard LDL update: A[j,k] -= L[j,i] * D[i] * L[k,i]
        # simpler/correct rewrite:
    return min(D), D


def ldl_decompose(M):
    """
    Clean LDL^T (no pivoting) for a symmetric mpmath matrix.
    Returns list D of diagonal entries; min(D) >= 0 (up to precision) iff PSD.
    """
    n = M.rows
    L = matrix(n)
    D = [mpf(0)] * n
    for i in range(n):
        s = M[i, i]
        for k in range(i):
            s -= L[i, k] * L[i, k] * D[k]
        D[i] = s
        L[i, i] = mpf(1)
        if abs(D[i]) < mpf(10) ** (-mp.dps + 5):
            # rank-deficient pivot: leave L below zero, continue
            for j in range(i + 1, n):
                L[j, i] = mpf(0)
            continue
        for j in range(i + 1, n):
            t = M[j, i]
            for k in range(i):
                t -= L[j, k] * L[i, k] * D[k]
            L[j, i] = t / D[i]
    return D, L


def is_psd(D, tol_dps_margin=10):
    tol = mpf(10) ** (-mp.dps + tol_dps_margin)
    return all(d >= -tol for d in D)


# ---------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------

def run(N, n_max):
    print()
    print("=" * 78)
    print(f"  T8.4 Lemma 6.4 probe  —  N = {N}   (dps = {mp.dps})")
    print("=" * 78)
    # show the diagonal axis values R_k <h_k, chi_1> for k = 1..2 n_max+1
    print()
    print(f"  Axis entries  R_k * Re<h_k, chi_1>  for k = 1, ..., {2*n_max+1}:")
    for k in range(1, 2 * n_max + 2):
        if k > N - 1:
            print(f"    k = {k:3d}    (out of range; k > N-1)")
            break
        val = Q_entry(N, k)
        print(f"    k = {k:3d}    {mp.nstr(val, 12)}")
    print()

    print(f"  Q(N={N}, n)  PSD test via LDL^T (no pivoting):")
    print(f"    {'n':>4}   {'dim':>4}   {'min D_ii':>22}   {'PSD?':>5}")
    for n in range(0, n_max + 1):
        if 2 * n + 1 > N - 1:
            print(f"    {n:>4}   {'—':>4}   {'axis k > N-1':>22}   {'—':>5}")
            continue
        M, _ = Q_matrix(N, n)
        D, _L = ldl_decompose(M)
        md = min(D)
        flag = "yes" if is_psd(D) else "NO "
        print(f"    {n:>4}   {n+1:>4}   {mp.nstr(md, 12):>22}   {flag:>5}")
    print()


if __name__ == "__main__":
    # N = 30 — smallest primorial with N_E >= 1 (ArchStruct §6.1)
    run(N=30,  n_max=14)
    # N = 210 — full LMFDB-anchor primorial (ArchStruct §6.2; J^prime_n empirical PSD at n <= 14)
    run(N=210, n_max=20)
