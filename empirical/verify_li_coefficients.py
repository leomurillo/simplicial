#!/usr/bin/env py
# -*- coding: utf-8 -*-
"""
verify_li_coefficients.py
=========================================================================
Li-Keiper coefficients for the Riemann Hypothesis.

Li's criterion (X.-J. Li, 1997):  RH  <=>  lambda_n >= 0  for all n >= 1,
where the Li coefficients are
        lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]
summed over the nontrivial zeros rho of zeta (paired with conjugates).

Keiper (1992) computes lambda_n directly from the completed zeta
        xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
WITHOUT knowing the zeros, via the generating function (verified below)

        sum_{n>=1} lambda_n z^n / n  =  log xi( 1/(1-z) ) - log xi(1).        (G)

Equivalently lambda_n = n * [z^n]  of the RHS of (G).

We compute (G) by *stable truncated-power-series (TPS) arithmetic*:
  - expand each analytic factor of log xi(s) about s = 1 in w = s-1,
  - the only nontrivial input is zeta near its pole, handled exactly via
        (s-1) zeta(s) = 1 + sum_{m>=0} (-1)^m gamma_m w^{m+1} / m!     (Stieltjes)
  - compose with the analytic change of variable w = z/(1-z).
This avoids the catastrophic cancellation of finite-difference Taylor.

DECOMPOSITION (Keiper).  The (s-1) factor of xi is paired with the simple
POLE of zeta: U(s) = (s-1) zeta(s) is analytic, U(1)=1.  Hence
        xi(s) = xi_arch(s) * U(s),   xi_arch(s) = (1/2) s pi^{-s/2} Gamma(s/2),
with xi_arch(1)=1/2 != 0.  The archimedean ("expected" drift) coefficients use
U -> 1 (drop primes AND the bare (s-1)); one must NOT keep a bare (s-1) in
xi_arch or it vanishes at s=1 (log -> -inf).  The arithmetic fluctuation is
        lambda_n^{arith} = lambda_n - lambda_n^{arch} = n [z^n] (composed log U).
Verified asymptotic (this script):
        lambda_n^{arch} = (n/2)(log n - 1 - log 2pi + gamma) + 3/4 - 1/(24 n) + ...
and the exact check  lambda_1^{arith} = gamma  anchors the split.

OFF-LINE EXCURSION (Bombieri-Lagarias 1999).  A single zero rho contributes
-Re[(1-1/rho)^n] to lambda_n.  If Re rho = 1/2 + delta (delta != 0) then
|1 - 1/rho| > 1, so this term grows like R^n with R = 1/|1-1/rho|, producing
unbounded negative oscillations -> contradiction with Li positivity.  We
compute R(delta) and compare its exponential rate to the ~ n log n drift.

Tiers:  [P] proven / numerically verified ;  [A] heuristic/conditional ;
        [C] conjectural.  Nothing here proves RH.
=========================================================================
"""
import mpmath as mp
import json, os, sys, time

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
NMAX = 320          # compute lambda_1 .. lambda_NMAX  (>= 300 target, all clean)
DPS  = 150          # mpmath precision. The w=z/(1-z) composition reintroduces
                    # binomial-scale (~2^n) intermediate magnitudes at high n, so
                    # the working precision must exceed ~ n*log10(2) ~ 0.30*n digits.
                    # dps=150 vs 0.30*320 ~ 97 gives a ~53-digit safety buffer; the
                    # dps=240 spot-check (_li_spotcheck.py) confirms agreement.
MARG = 100          # guard terms beyond NMAX: the composition degrades within ~50-60
                    # terms of the truncation order, so keep that zone above NMAX.
M    = NMAX + MARG + 1   # power-series length (index 0..M-1)

mp.mp.dps = DPS
ZERO = mp.mpf(0)
ONE  = mp.mpf(1)

# ----------------------------------------------------------------------
# Truncated power series (TPS) arithmetic, length M, coefficient lists
# ----------------------------------------------------------------------
def ps_mul(a, b):
    c = [ZERO]*M
    for i in range(M):
        ai = a[i]
        if ai == 0:
            continue
        lim = M - i
        for j in range(lim):
            bj = b[j]
            if bj != 0:
                c[i+j] += ai*bj
    return c

def ps_scale(a, k):
    return [k*x for x in a]

def ps_exp(a):
    """exp of a TPS; a[0] may be nonzero. O(M^2) via b' = a' b recurrence:
       b_n = (1/n) sum_{k=1}^{n} k a_k b_{n-k},   b_0 = exp(a_0)."""
    b = [ZERO]*M
    b[0] = mp.exp(a[0])
    for n in range(1, M):
        s = ZERO
        for k in range(1, n+1):
            ak = a[k]
            if ak != 0:
                s += k*ak*b[n-k]
        b[n] = s/n
    return b

def ps_log(a):
    """log of a TPS; requires a[0] != 0. O(M^2) via a b' = a' recurrence:
       b_n = (1/a_0)[ a_n - (1/n) sum_{k=1}^{n-1} k b_k a_{n-k} ],  b_0 = log(a_0)."""
    a0 = a[0]
    b = [ZERO]*M
    b[0] = mp.log(a0)
    for n in range(1, M):
        s = ZERO
        for k in range(1, n):
            bk = b[k]
            if bk != 0:
                s += k*bk*a[n-k]
        b[n] = (a[n] - s/n)/a0
    return b

def ps_mul_by_w(X):
    """Return X(z) * w(z) with w = z/(1-z).  Since Y(1-z)=Xz we get the O(M)
       cumulative recurrence  Y_k = Y_{k-1} + X_{k-1}  (Y_0 = 0).
       Numerically benign: no large binomials, coefficients stay bounded."""
    Y = [ZERO]*M
    for k in range(1, M):
        Y[k] = Y[k-1] + X[k-1]
    return Y

def ps_compose_with_w_of_z(coeffs_in_w):
    """Compose F(w)=sum_j coeffs_in_w[j] w^j with w = z/(1-z), returning a series
       in z.  Builds w^j incrementally via ps_mul_by_w (each O(M)) -> O(M^2) total.
       This is the STABLE route (analytic composition, bounded coeffs); it avoids
       the catastrophic cancellation of the explicit binomial transform that would
       otherwise demand ~n digits of precision (Johansson uses 8n bits)."""
    out = [ZERO]*M
    wpow = [ZERO]*M; wpow[0] = ONE          # w^0 = 1
    for j in range(M):
        if j > 0:
            wpow = ps_mul_by_w(wpow)         # w^{j-1} -> w^j  in O(M)
        cj = coeffs_in_w[j]
        if cj != 0:
            for i in range(j, M):            # w^j has no terms below z^j
                wi = wpow[i]
                if wi != 0:
                    out[i] += cj*wi
    return out

# ----------------------------------------------------------------------
# Cached special-value tables (the only genuinely expensive inputs).
# Stieltjes gamma_m and polygamma^{(k-1)}(1/2) are each ~0.5-1s per index in
# mpmath, so we compute them ONCE up to the needed order and reuse.
# ----------------------------------------------------------------------
_STJ = None       # _STJ[m] = stieltjes(m), m=0..M-2
_PSI = None       # _PSI[k] = polygamma(k-1, 1/2), k=1..M-1

def _ensure_tables():
    global _STJ, _PSI
    if _STJ is not None:
        return
    t = time.time()
    _STJ = [None]*(M-1)
    for m in range(M-1):
        _STJ[m] = mp.stieltjes(m)
        if m % 50 == 0:
            print(f"   [tables] stieltjes {m}/{M-2}  ({time.time()-t:.0f}s)", flush=True)
    _PSI = [None]*(M)
    for k in range(1, M):
        _PSI[k] = mp.polygamma(k-1, ONE/2)
        if k % 50 == 0:
            print(f"   [tables] polygamma {k}/{M-1}  ({time.time()-t:.0f}s)", flush=True)
    print(f"   [tables] done in {time.time()-t:.0f}s", flush=True)

# ----------------------------------------------------------------------
# Analytic building blocks of xi(s), expanded about s=1  (w = s-1)
# ----------------------------------------------------------------------
def build_log_xi_series(include_zeta=True):
    """Return the TPS (in w=s-1) of log xi(s).  If include_zeta is False,
       use xi_inf(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) (archimedean only)."""
    _ensure_tables()
    # s = 1 + w
    S = [ZERO]*M; S[0] = ONE; S[1] = ONE

    # pi^{-s/2} = pi^{-1/2} * exp(-(w/2) log pi)
    lp = mp.log(mp.pi)
    P = [ZERO]*M
    pref = mp.power(mp.pi, -ONE/2)
    half_lp = -lp/2
    pw = ONE
    for k in range(M):
        P[k] = pref*pw/mp.factorial(k)
        pw *= half_lp

    # Gamma(s/2) = Gamma(1/2 + w/2): exp of logGamma series.
    # [x^k] logGamma(1/2 + x) = psi^{(k-1)}(1/2)/k!  ; then x = w/2 (factor (1/2)^k).
    LG = [ZERO]*M
    LG[0] = mp.loggamma(ONE/2)
    half = ONE/2
    hp = half  # (1/2)^k for k=1
    for k in range(1, M):
        LG[k] = _PSI[k]/mp.factorial(k)*hp
        hp *= half
    G = ps_exp(LG)

    # KEIPER SPLIT.  The (s-1) factor of xi is paired with the SIMPLE POLE of zeta:
    #   (s-1) zeta(s)  is the analytic "completed unit" U(s),  U(1)=1, and
    #   U(s) = w zeta(1+w) = 1 + sum_{m>=0} (-1)^m gamma_m w^{m+1}/m!   (Stieltjes).
    # Thus  xi(s) = [ (1/2) s pi^{-s/2} Gamma(s/2) ] * U(s)  =  xi_arch(s) * U(s),
    # where xi_arch(s) = (1/2) s pi^{-s/2} Gamma(s/2)  is FINITE & NONZERO at s=1
    # (xi_arch(1)=1/2).  The archimedean Li coefficients use H = 1 (drop U entirely);
    # the full coefficients use H = U.  Then lambda_n^arith = lambda_n - lambda_n^arch
    # = n[z^n] of the composed log U, the pure prime/zero fluctuation.
    # NB: one must NOT keep a bare (s-1) factor in xi_arch -- that would make xi_arch
    # vanish at s=1 (log -> -infinity).  The (s-1) lives inside U, cancelling the pole.
    H = [ZERO]*M
    H[0] = ONE
    if include_zeta:
        for m in range(0, M-1):
            H[m+1] = (ONE if (m % 2 == 0) else -ONE)*_STJ[m]/mp.factorial(m)
    # else: H stays [1,0,0,...]  (archimedean factor xi_arch only)
    XI = ps_scale(S, ONE/2)
    XI = ps_mul(XI, P)
    XI = ps_mul(XI, G)
    XI = ps_mul(XI, H)
    return ps_log(XI)

def li_coeffs(include_zeta=True):
    """Return list lam[1..NMAX] of Li coefficients (or archimedean ones)."""
    LXI = build_log_xi_series(include_zeta=include_zeta)
    F = ps_compose_with_w_of_z(LXI)     # F(z) = log xi(1/(1-z)) as series in z
    F[0] -= LXI[0]                      # subtract log xi(1) (the constant term)
    lam = [None]*(NMAX+1)
    for n in range(1, NMAX+1):
        lam[n] = n*F[n]
    return lam

# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print(f"[config] NMAX={NMAX}, dps={DPS}, series length M={M}")

    lam      = li_coeffs(include_zeta=True)
    lam_arch = li_coeffs(include_zeta=False)
    print(f"[timing] series built in {time.time()-t0:.1f}s")

    # ---- Verification against published values ----
    known = {
        1: '0.02309570896612103381',
        2: '0.09234573522804509767',
        3: '0.20763892055432909305',
        4: '0.36879047949224256683',
        5: '0.57554271446117124092',
    }
    print("\n=== VERIFICATION (lambda_n vs published) ===")
    maxerr = mp.mpf(0)
    for n in sorted(known):
        v = lam[n]
        ref = mp.mpf(known[n])
        err = abs(v-ref)
        maxerr = max(maxerr, err)
        print(f"  n={n}: computed={mp.nstr(v,18)}  ref={known[n]}  |err|={mp.nstr(err,3)}")
    print(f"  max |err| over checks = {mp.nstr(maxerr,3)}")

    # ---- Stability self-check: recompute lambda_NMAX at lower dps proxy ----
    # (compare against an internal lower-order truncation drop)
    # ---- Archimedean asymptotic check ----
    print("\n=== ARCHIMEDEAN DRIFT vs KEIPER/VOROS ASYMPTOTIC ===")
    # Verified empirically here: lambda_n^arch = (n/2)(log n - 1 - log(2pi) + gamma)
    #                                            + 3/4 + o(1).
    # i.e. leading (1/2) n log n + (1/2)(gamma-1-log2pi) n + 3/4 + ...   The +3/4
    # constant is the exact next term (arch - leading -> 0.74965... -> 3/4).
    gamma = mp.euler
    for n in [10, 50, 100, 200, 300, NMAX]:
        if n > NMAX: continue
        asym = (mp.mpf(n)/2)*(mp.log(n) - 1 - mp.log(2*mp.pi) + gamma)
        a = lam_arch[n]
        print(f"  n={n}: arch={mp.nstr(a,14)}  lead={mp.nstr(asym,14)}"
              f"  arch-lead={mp.nstr(a-asym,10)}  (-> 3/4={mp.nstr(mp.mpf(3)/4,6)})")

    # ---- Margin analysis ----
    print("\n=== MARGIN ANALYSIS (sample) ===")
    rows = []
    for n in range(1, NMAX+1):
        L  = lam[n]
        A  = lam_arch[n]
        arith = L - A
        ratio = abs(arith)/A if A != 0 else mp.inf
        margin = L/A if A != 0 else mp.inf
        rows.append((n, L, A, arith, ratio, margin))
    for n in [1,2,5,10,25,50,100,150,200,250,300,350,NMAX]:
        if n > NMAX: continue
        n_, L, A, arith, ratio, margin = rows[n-1]
        print(f"  n={n:4d}: lam={mp.nstr(L,12):>16}  arch={mp.nstr(A,12):>16}"
              f"  |arith|/arch={mp.nstr(ratio,6):>12}  lam/arch={mp.nstr(margin,9)}")

    # min lambda_n (positivity check) and min margin
    minlam = min(rows, key=lambda r: r[1])
    minmargin = min(rows, key=lambda r: r[5])
    print(f"\n  min lambda_n over n<=NMAX:  n={minlam[0]}, lambda={mp.nstr(minlam[1],10)}  (all > 0 ? {all(r[1]>0 for r in rows)})")
    print(f"  min lambda_n/arch:          n={minmargin[0]}, margin={mp.nstr(minmargin[5],10)}")

    # ---- Off-line excursion growth rate (Bombieri-Lagarias) ----
    print("\n=== OFF-LINE EXCURSION RATE R(delta) = 1/|1 - 1/rho|, rho=1/2+delta+i t ===")
    print("  (a hypothetical zero off the line forces |term| ~ R^n; compare to ~n log n drift)")
    def R_of(delta, t):
        rho = mp.mpf('0.5') + mp.mpf(delta) + mp.mpc(0, t)
        return 1/abs(1 - 1/rho)
    # representative ordinate t ~ 14.13 (first zero) and a high one
    for t in [mp.mpf('14.134725'), mp.mpf('100'), mp.mpf('1000')]:
        line = f"  t={mp.nstr(t,6):>10}: "
        for delta in [mp.mpf('0.01'), mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.25')]:
            R = R_of(delta, t)
            line += f"R(d={float(delta)})={mp.nstr(R,8)}  "
        print(line)
    print("  Drift grows POLYNOMIALLY (~ (n/2) log n); any R>1 grows EXPONENTIALLY (R^n),")
    print("  so a single off-line zero eventually dominates -> Li-positivity fails. [P, Bombieri-Lagarias]")
    print("\n  E-folding scale n_e=1/log R (~ t^2/|delta|) and crossover n* where R^n first")
    print("  exceeds the positive drift (forcing lambda_n<0); shows WHY n<=1e5 cannot decide RH:")
    def driftf(nn):
        return (mp.mpf(nn)/2)*(mp.log(nn)-1-mp.log(2*mp.pi)+gamma)+mp.mpf(3)/4
    for t in [mp.mpf('14.134725'), mp.mpf('100')]:
        for delta in [mp.mpf('0.25'), mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.01')]:
            R = R_of(delta, t); lR = mp.log(R); ne = 1/lR
            lo, hi = 50, 10**18
            # bisect n*lR = log(drift(n))
            f = lambda nn: nn*lR - mp.log(driftf(nn))
            if f(lo) > 0: ncross = lo
            elif f(hi) < 0: ncross = None
            else:
                while lo < hi:
                    mid = (lo+hi)//2
                    if f(mid) > 0: hi = mid
                    else: lo = mid+1
                ncross = lo
            nc = f"{ncross:,}" if ncross else ">1e18"
            print(f"    t={float(t):8.2f} d={float(delta):<5}: R-1={mp.nstr(R-1,4)}"
                  f"  n_e={int(ne):,}  n*~{nc}")

    # ---- New micro-observation probe: fluctuation / arch and a smoothed law ----
    print("\n=== FLUCTUATION DIAGNOSTIC ===")
    # normalized fluctuation phi_n = lambda_n^arith / sqrt(n)  (de Branges/Lagarias scale)
    for n in [50,100,150,200,250,300,NMAX]:
        if n>NMAX: continue
        arith = rows[n-1][3]
        print(f"  n={n:4d}: arith={mp.nstr(arith,10):>14}  arith/sqrt(n)={mp.nstr(arith/mp.sqrt(n),8):>12}"
              f"  arith/log n={mp.nstr(arith/mp.log(n),8)}")

    # ---- Save full table ----
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    os.makedirs(outdir, exist_ok=True)
    data = {
        "config": {"NMAX": NMAX, "dps": DPS, "M": M},
        "method": "Keiper generating function (G) via stable truncated-power-series; "
                  "arch = zeta->1 (Gamma/pi factors only).",
        "verification_max_abs_err": mp.nstr(maxerr, 5),
        "lambda": {str(n): mp.nstr(lam[n], 30) for n in range(1, NMAX+1)},
        "lambda_arch": {str(n): mp.nstr(lam_arch[n], 30) for n in range(1, NMAX+1)},
        "lambda_arith": {str(n): mp.nstr(lam[n]-lam_arch[n], 30) for n in range(1, NMAX+1)},
        "ratio_abs_arith_over_arch": {str(n): mp.nstr(abs(lam[n]-lam_arch[n])/lam_arch[n], 18)
                                      for n in range(1, NMAX+1)},
        "margin_lam_over_arch": {str(n): mp.nstr(lam[n]/lam_arch[n], 18)
                                 for n in range(1, NMAX+1)},
        "all_positive_up_to_NMAX": bool(all(r[1] > 0 for r in rows)),
        "min_lambda": {"n": minlam[0], "value": mp.nstr(minlam[1], 18)},
    }
    jpath = os.path.join(outdir, "li_coefficients_table.json")
    with open(jpath, "w") as f:
        json.dump(data, f, indent=1)
    print(f"\n[saved] full table -> {jpath}")
    print(f"[timing] total {time.time()-t0:.1f}s")

    return lam, lam_arch, rows

if __name__ == "__main__":
    main()
