#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32.1  Audit 3  --  Is the area-law negative measure-dependent?
====================================================================

Audit 2 found the boundary's DIMENSIONAL share phi(N)/(N-1) -> 0 (HORN B:
no geometric area law). Audit 3 asks whether that negative is an artifact of
the measure, by two pre-registered "rescue" horns:

----------------------------------------------------------------------------
PRE-REGISTERED QUESTION (Paper 32.1 sec 8.3)
----------------------------------------------------------------------------
  HORN A'  (metric / geometric rescue): does upgrading the CLASSICAL Fisher
           metric to the QUANTUM Bures metric on the lift D(C^Q) change the
           boundary/bulk VOLUME ratio at the Bekenstein-saturating state
           (the centroid rho_* = I/Q)?
  HORN B'  (arithmetic rescue): does weighting each mode by its intrinsic
           ARITHMETIC MASS -- the conductor c(k) = N/gcd(k,N), the very
           quantity that DEFINES the packets (Paper 32 sec 5.1) and plays the
           energy role in the program's conductor-graded Weil/Noether
           positivity -- make the boundary share non-vanishing?

----------------------------------------------------------------------------
FORCED-MATCH GUARD (GPD discipline, Paper 35)
----------------------------------------------------------------------------
The conductor weighting is PRE-JUSTIFIED (packet-defining; the arithmetic-mass
/ energy analog -- the natural Bekenstein weight, since Bekenstein weights
information by ENERGY), not selected post hoc to manufacture a nicer number.
ALL THREE measures are reported, including the negatives, so the CONTRAST is
the finding -- not a cherry-picked weighting.

----------------------------------------------------------------------------
ANCHORED [P] OBJECTS
----------------------------------------------------------------------------
- Fisher metric at the centroid:  g_{p*} = Q * I_H   (isotropic; Paper 32 sec 5.3)
- Conductor packets = conductor classes c(k) = N/gcd(k,N); boundary M = units
  (Z/N)^x = conductor-N (maximal) characters       (Paper 32 sec 5.1)
- SLD quantum-Fisher / Bures metric reduces to the classical Fisher metric on
  a commuting (diagonal) family                     (standard; Petz)

----------------------------------------------------------------------------
PRE-CLAIMED BRANCHES (matched pair)
----------------------------------------------------------------------------
HORN A' REFUTED : at rho_* the metric is isotropic (Fisher = Q*I_H, Bures a
                  global constant multiple), so the boundary/bulk volume ratio
                  is metric-independent = the dimension count -> 0. No metric
                  rescues the area law at the saturating state.
HORN B' CONFIRMED: conductor-weighted boundary share converges to a NON-ZERO
                  constant ~0.52 = prod_p (1 - 1/(p^2-p+1)). The boundary is
                  an O(1)-WEIGHT arithmetic locus; "boundary vanishes" was a
                  dimension-counting artifact.
"""

import numpy as np
from math import gcd, isqrt
from fractions import Fraction
from sympy import totient, primerange


# ===========================================================================
# HORN A' : metric (Fisher vs Bures) at the saturating centroid rho_* = I/Q
# ===========================================================================
def real_packet_directions(N):
    """
    Real diagonal traceless tangent directions on Delta_N, one representative
    per conductor packet, built from characters chi_k(a) = exp(2pi i k a / N):
    a boundary direction (a unit k), and bulk directions (non-unit k).
    Returns dict {label: (k, real_vector u with sum u = 0)}.
    """
    out = {}
    a = np.arange(N)
    seen_cond = {}
    for k in range(1, N):
        c = N // gcd(k, N)
        # one real representative per conductor value (cos part of chi_k)
        if c in seen_cond:
            continue
        u = np.cos(2 * np.pi * k * a / N)
        u = u - u.mean()                      # project into H_R (sum = 0)
        if np.allclose(u, 0):                 # cos part degenerate -> use sin
            u = np.sin(2 * np.pi * k * a / N)
            u = u - u.mean()
        seen_cond[c] = True
        out[f"k={k} (cond {c}{', UNIT/boundary' if c == N else ''})"] = (k, c, u)
    return out


def fisher_coeff(u, Q):
    """Classical Fisher at p_* = (1/Q,...): g(u,u) = sum u_a^2 / p_a = Q * |u|^2."""
    p = np.full(Q, 1.0 / Q)
    return float((u * u / p).sum())


def sld_qfi_coeff(u, Q):
    """
    SLD quantum-Fisher (Bures up to the conventional 1/4) at rho_* = I/Q for a
    DIAGONAL perturbation X = diag(u): solve the Lyapunov equation
        rho_* L + L rho_* = 2 X     (SLD operator L)
    then F_Q = tr(X L). Computed by genuine matrix solve (not the closed form),
    to verify the reduction to classical Fisher numerically.
    """
    rho = np.eye(Q) / Q
    X = np.diag(u).astype(float)
    # vectorized Lyapunov solve: (I (x) rho + rho^T (x) I) vec(L) = 2 vec(X)
    A = np.kron(np.eye(Q), rho) + np.kron(rho.T, np.eye(Q))
    L = np.linalg.solve(A, 2 * X.reshape(-1)).reshape(Q, Q)
    return float(np.trace(X @ L))


def horn_A_metric(N):
    dirs = real_packet_directions(N)
    Q = N
    rows = []
    for label, (k, c, u) in dirs.items():
        nrm = float((u * u).sum())
        gF = fisher_coeff(u, Q)
        gQ = sld_qfi_coeff(u, Q)
        rows.append((label, c, nrm, gF / nrm, gQ / nrm, gQ / gF))
    return rows


# ===========================================================================
# HORN B' : conductor-weighted boundary share
# ===========================================================================
def dimension_share(N):
    """Audit-2 baseline: phi(N)/(N-1)."""
    return Fraction(int(totient(N)), N - 1)


def conductor_share(N):
    """
    Boundary (units, conductor N) weight / total weight, weighting each
    character k by its conductor c(k) = N/gcd(k,N). Exact rational.
        boundary = sum_{gcd(k,N)=1} c(k) = phi(N) * N
        total    = sum_{k=1}^{N-1} c(k)
    """
    total = Fraction(0)
    boundary = Fraction(0)
    for k in range(1, N):
        g = gcd(k, N)
        c = Fraction(N, g)
        total += c
        if g == 1:
            boundary += c
    return boundary / total, boundary, total


def conductor_limit(pmax):
    """prod_{p <= pmax} (1 - 1/(p^2 - p + 1))  (the infinite-primorial limit)."""
    val = 1.0
    for p in primerange(2, pmax + 1):
        val *= (1 - 1.0 / (p * p - p + 1))
    return val


# ===========================================================================
# SECONDARY : conductor-weighted cubic coupling boundary share
# ===========================================================================
def conductor_weighted_cubic(N):
    """
    Weight each ordered closing triple (k,l,m), k+l+m=0 mod N, k,l,m in 1..N-1,
    by the product c(k)c(l)c(m). Return the share carried by triples with
    >= 1 unit (boundary) leg.  Parallels Audit 2's UNWEIGHTED beta_cubic.
    """
    c = np.array([0 if k == 0 else N // gcd(k, N) for k in range(N)],
                 dtype=np.float64)
    is_unit = np.array([1 if (k != 0 and gcd(k, N) == 1) else 0
                        for k in range(N)], dtype=bool)
    idx = np.arange(N)
    total_w = 0.0
    bulk_w = 0.0                       # all-nonunit legs
    for k in range(1, N):
        m = (N - k - idx) % N
        valid = (idx != 0) & (m != 0)
        w = c[k] * c[idx] * c[m]
        total_w += float(w[valid].sum())
        if not is_unit[k]:                      # leg k must be non-unit too
            bulk_w += float(w[valid & (~is_unit) & (~is_unit[m])].sum())
    boundary_share = (total_w - bulk_w) / total_w
    return boundary_share, total_w, bulk_w


# ===========================================================================
# Run
# ===========================================================================
def main():
    print("#" * 78)
    print("#  Paper 32.1  Audit 3 -- Is the area-law negative measure-dependent?")
    print("#" * 78)

    # ---------------- HORN A' ----------------
    print("\nHORN A' (metric rescue):  Fisher vs Bures at the centroid rho_* = I/Q")
    print("-" * 78)
    for N in (6, 30):
        print(f"\n  N = {N}  (one representative direction per conductor packet)")
        print(f"    {'direction':28s} | {'cond':>5} | "
              f"{'g_F/|u|^2':>10} | {'g_Q/|u|^2':>10} | {'g_Q/g_F':>8}")
        rows = horn_A_metric(N)
        coeffsF = []
        for (label, c, nrm, fc, qc, ratio) in rows:
            coeffsF.append(fc)
            print(f"    {label:28s} | {c:>5} | {fc:>10.4f} | {qc:>10.4f} | "
                  f"{ratio:>8.4f}")
        spread = max(coeffsF) - min(coeffsF)
        print(f"    -> Fisher coefficient spread across packets: {spread:.2e} "
              f"(isotropic if ~0; equals Q = {N})")

    # ---------------- HORN B' ----------------
    print("\n\nHORN B' (arithmetic rescue): dimension share vs conductor-weight share")
    print("-" * 78)
    print(f"{'N':>6} | {'dim share phi/(N-1)':>20} | "
          f"{'conductor share (exact)':>26} | {'cond share (float)':>18}")
    print("-" * 78)
    ladder = [6, 30, 210, 2310]
    dim_rows, cond_rows = [], []
    for N in ladder:
        ds = dimension_share(N)
        cs, b, t = conductor_share(N)
        dim_rows.append(float(ds))
        cond_rows.append(float(cs))
        print(f"{N:>6} | {float(ds):>20.4f} | "
              f"{str(cs):>26} | {float(cs):>18.4f}")

    lim = conductor_limit(100000)
    print(f"\n  conductor-share limit prod_p (1 - 1/(p^2-p+1))  (p <= 1e5)  "
          f"= {lim:.4f}")

    # ---------------- SECONDARY ----------------
    print("\n\nSECONDARY: conductor-WEIGHTED cubic coupling boundary share")
    print("   (parallels Audit 2's UNWEIGHTED beta_cubic 0.90 -> 0.49)")
    print("-" * 78)
    print(f"{'N':>6} | {'cond-weighted boundary share of cubic coupling':>48}")
    print("-" * 78)
    cw_rows = []
    for N in ladder:
        bshare, tw, bw = conductor_weighted_cubic(N)
        cw_rows.append(bshare)
        print(f"{N:>6} | {bshare:>48.4f}")

    # ---------------- VERDICT ----------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)

    # A': isotropy at the centroid -> metric gives no packet reweighting
    spreads_ok = True
    for N in (6, 30):
        rows = horn_A_metric(N)
        fc = [r[3] for r in rows]
        if max(fc) - min(fc) > 1e-8 or abs(max(fc) - N) > 1e-8:
            spreads_ok = False
    print(f"  HORN A' (metric rescue):  {'REFUTED' if spreads_ok else 'NOT REFUTED'}")
    print(f"      Fisher = Q*I_H isotropic at rho_*; SLD quantum-Fisher (Bures up")
    print(f"      to 1/4) reduces to it on the diagonal packet directions, so the")
    print(f"      boundary/bulk VOLUME ratio is metric-independent = dim count -> 0.")
    print(f"      No metric rescues the area law at the saturating centroid.")

    # B': conductor share converges to a non-zero constant
    horn_B = (cond_rows[-1] > 0.4) and (dim_rows[-1] < cond_rows[-1]) \
        and all(cond_rows[i] >= cond_rows[i + 1] - 1e-9
                for i in range(len(cond_rows) - 1))
    print(f"\n  HORN B' (arithmetic rescue):  {'CONFIRMED' if horn_B else 'NOT CONFIRMED'}")
    print(f"      dim share {dim_rows[0]:.3f} -> {dim_rows[-1]:.3f} (-> 0, Audit 2),")
    print(f"      but conductor share {cond_rows[0]:.3f} -> {cond_rows[-1]:.3f} "
          f"(-> {lim:.3f} != 0).")
    print(f"      The boundary carries an O(1) (~half) share of the intrinsic")
    print(f"      arithmetic-mass measure; 'boundary vanishes' was a dimension-")
    print(f"      counting artifact. Conductor-weighted cubic coupling is even more")
    print(f"      boundary-heavy: {cw_rows[0]:.3f} -> {cw_rows[-1]:.3f}.")

    print(f"\n  NET: the holographic boundary is NOT a metric/geometric area")
    print(f"  (no metric makes it non-vanishing at the Bekenstein point), but it")
    print(f"  IS a non-vanishing ARITHMETIC locus under conductor weight. The")
    print(f"  honest area-law negative of Audit 2 stands geometrically; the")
    print(f"  firewall-clean positive is arithmetic (conductor = pure-number mass).")

    print("\nFirewall discipline (sec 12): only dimensionless quantities emitted")
    print("(dimension counts, conductor integers, ratios, metric eigenvalues).")

    print("\nAUDIT 3:",
          "A' REFUTED + B' CONFIRMED (verdict measure-dependent, as pre-claimed)"
          if (spreads_ok and horn_B) else "SEE ABOVE")


if __name__ == "__main__":
    main()
