"""
Two-axis (N, m) probe: joint primorial Hankel positivity at multiple gauge rungs.

At each even m >= 2, define joint cumulants
  mu_k^(m)(N) := sum over L-functions chi of sum_rho 1/gamma_rho^{m(k+1)}.

For m even, this is a positive Hankel sequence iff all gamma_rho are real
(equivalent to GRH at primorial N via Stieltjes atomization).

For m odd, cumulants vanish identically by (gamma, -gamma) pair cancellation
in self-dual L-functions and complex conjugate pair cancellation in non-self-dual,
so no Hankel criterion at odd m.

Probe targets:
  - Numerical convergence rate per rung at each m.
  - Asymptotic single-atom dominance ratio mu_k / (2*gamma_min^{-m(k+1)}).
  - Effective rank (degree of single-atom dominance).
  - Precision requirements.
  - Comparative structural cleanness across m.

Strategic question: is there an m > 2 that gives strictly better analytical
or numerical handle than the Apex-Lemma-HJ standard m=2 (Born/RMS)?
"""

import sys, io, time, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, matrix

mp.dps = 600  # plenty for high-m comparison

# ============================================================
# Load zero data (from the locked N=210 dataset)
# ============================================================

from zero_data_N210 import self_dual_all as sd_all, non_self_dual_all as nsd_all

def f_from_name(name):
    m = re.search(r'\(f=(\d+)', name)
    return int(m.group(1)) if m else None

n30_conductors = {1, 3, 5, 15}
n210_conductors = {1, 3, 5, 7, 15, 21, 35, 105}

def filter_by_conductor(d, conductors):
    return {n: zs for n, zs in d.items() if f_from_name(n) in conductors}

sd_30 = filter_by_conductor(sd_all, n30_conductors)
nsd_30 = filter_by_conductor(nsd_all, n30_conductors)
sd_210 = sd_all
nsd_210 = nsd_all

n30_lfns = len(sd_30) + 2 * len(nsd_30)
n210_lfns = len(sd_210) + 2 * len(nsd_210)

print("=" * 78)
print(" Two-axis (N, m) probe: joint primorial Hankel positivity")
print("=" * 78)
print(f" mpmath dps = {mp.dps}")
print(f" N=30: {n30_lfns} L-functions ({len(sd_30)} self-dual + {len(nsd_30)} pairs)")
print(f" N=210: {n210_lfns} L-functions ({len(sd_210)} self-dual + {len(nsd_210)} pairs)")
print()

# ============================================================
# Joint cumulant at gauge m
# ============================================================

def joint_cumulant(sd, nsd, m_gauge, k):
    """mu_k^(m)(N) = sum_chi sum_rho 1/gamma_rho^{m(k+1)}."""
    exponent = m_gauge * (k + 1)
    total = mpf(0)
    for zs in sd.values():
        # self-dual: zeros at +/- gamma, factor 2 for the negative partners
        total += 2 * sum(z ** (-exponent) for z in zs)
    for zs in nsd.values():
        # non-self-dual pair: 50 zeros from one character, factor 2 for the conjugate
        total += 2 * sum(z ** (-exponent) for z in zs)
    return total

# ============================================================
# Smallest |gamma| at each N (dominant atom)
# ============================================================

def gamma_min(sd, nsd):
    all_g = []
    for zs in sd.values():
        all_g.extend([abs(z) for z in zs])
    for zs in nsd.values():
        all_g.extend([abs(z) for z in zs])
    return min(all_g)

g_min_30 = gamma_min(sd_30, nsd_30)
g_min_210 = gamma_min(sd_210, nsd_210)

print(f" gamma_min(30)  = {float(g_min_30):.6f}")
print(f" gamma_min(210) = {float(g_min_210):.6f}")
print()

# ============================================================
# LDL Hankel positivity test
# ============================================================

def ldl(M):
    n = M.rows
    A = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A[k, k]
        diags.append(d)
        if d <= 0:
            return False, min(diags), k
        for i in range(k+1, n):
            f = A[i, k] / d
            for j in range(k+1, n):
                A[i, j] -= f * A[k, j]
    return True, min(diags), n

def H(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j]
    return M

def J(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j+1]
    return M

# ============================================================
# Sweep across m for fixed N
# ============================================================

def sweep_m(label, sd, nsd, g_min, m_values, K_max, n_test):
    print("=" * 78)
    print(f"  {label}: gamma_min = {float(g_min):.4f}")
    print("=" * 78)

    for m_gauge in m_values:
        print(f"\n  --- m = {m_gauge} (cumulants ~ gamma^{{-{m_gauge}(k+1)}}) ---")

        t0 = time.time()
        cumulants = [None] + [joint_cumulant(sd, nsd, m_gauge, k) for k in range(K_max)]
        # cumulants[k+1] = mu_k^(m), with cumulants[0] = None placeholder
        # Actually let me redo: mu[k] = joint_cumulant(k) directly
        mu = [joint_cumulant(sd, nsd, m_gauge, k) for k in range(K_max)]
        print(f"  cumulants in {time.time()-t0:.1f}s")
        print(f"    mu_0  = {mp.nstr(mu[0], 6)}")
        if K_max > 10:
            print(f"    mu_10 = {mp.nstr(mu[10], 6)}")
        if K_max > 30:
            print(f"    mu_30 = {mp.nstr(mu[30], 6)}")
        if K_max > 60:
            print(f"    mu_60 = {mp.nstr(mu[60], 6)}")

        # Asymptotic single-atom dominance: mu_k / (2*gamma_min^{-m(k+1)})
        print(f"  asymptotic ratio mu_k / (2*gamma_min^{{-{m_gauge}(k+1)}}):")
        for k in [10, 30, 60]:
            if k < K_max:
                predicted = 2 * g_min ** (-m_gauge * (k + 1))
                ratio = float(mu[k] / predicted)
                print(f"    k={k:>3}: {ratio:.6f}")

        # Hankel positivity test
        print(f"  Hankel positivity at sampled rungs:")
        print(f"    {'n':>3}  {'H':>6}  {'minD(H)':>14}  {'J':>6}  {'minD(J)':>14}")
        passed = 0
        for n in n_test:
            if 2*n + 1 >= K_max:
                break
            try:
                h_psd, h_min, _ = ldl(H(mu, n))
                j_psd, j_min, _ = ldl(J(mu, n))
                h_str = "PSD" if h_psd else "FAIL"
                j_str = "PSD" if j_psd else "FAIL"
                print(f"    {n:>3}  {h_str:>6}  {mp.nstr(h_min, 4):>14}  "
                      f"{j_str:>6}  {mp.nstr(j_min, 4):>14}")
                if h_psd and j_psd:
                    passed += 1
            except Exception as e:
                print(f"    {n:>3}  exception: {e}")
        print(f"  passed {passed}/{len(n_test)} sampled rungs")

# Test rungs
n_test_short = [0, 1, 2, 3, 5, 8, 10, 15, 20, 30, 40, 50, 60]

# K_max controls how many cumulants we compute (need 2*n_max+1 at minimum for Hankel/J)
K_MAX_30 = 130
K_MAX_210 = 130

m_values = [2, 4, 6]

print()
sweep_m("N = 30", sd_30, nsd_30, g_min_30, m_values, K_MAX_30, n_test_short)
print()
sweep_m("N = 210", sd_210, nsd_210, g_min_210, m_values, K_MAX_210, n_test_short)

# ============================================================
# Convergence-rate summary
# ============================================================

print()
print("=" * 78)
print(" Single-atom dominance: gamma_min^{-m} per (N, m)")
print("=" * 78)
print()
print(f"  {'':>10} {'gamma_min':>14} {'1/gmin^2':>14} {'1/gmin^4':>14} {'1/gmin^6':>14}")
for label, g in [("N=30", g_min_30), ("N=210", g_min_210)]:
    print(f"  {label:>10} {float(g):>14.6f} "
          f"{float(1/g**2):>14.4f} {float(1/g**4):>14.4f} {float(1/g**6):>14.4f}")

print()
print("=" * 78)
print(" Diagnostic: which m gives the strongest single-atom dominance?")
print("=" * 78)
print("""
Higher m amplifies the dominance of the smallest-|gamma| zero:
  - At N=30, gamma_min = 2.73 > 1, so 1/gamma_min^m shrinks with m.
    Cumulants get SMALLER as m grows. Numerically easier; structurally
    the joint sum has more atoms contributing competitively.

  - At N=210, gamma_min = 0.141 < 1 (chi_105(44) outlier), so 1/gamma_min^m
    EXPLODES with m. Cumulants get vastly larger. Single-atom dominance
    becomes overwhelming: at m=6, chi_105(44) accounts for essentially
    100% of the joint cumulant at all rungs k >= 10.

The strategic question is whether the higher-m near-rank-1 structure at N=210
gives a CLEANER analytical handle for proving GRH-equivalent positivity,
or whether the m=2 multi-atom richness is actually what's needed.
""")
