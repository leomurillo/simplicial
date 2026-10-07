#!/usr/bin/env python3
"""
Jensen d-TOWER margin sweep over self-dual (Kronecker) L-functions.
Purpose: reduce the noise in the chiral-margin-vs-conductor trend (laptop run was |D|<=67, 12 points)
and measure the d-TOWER infimum -- the actual RH-bearing quantity the floor-lift localized.

For each fundamental discriminant D (the real primitive quadratic character chi_D, parity = sign D):
  completed Xi_D(t) = Lambda(1/2+it, chi_D)  (real, even);  a_m = (-1)^m [t^{2m}] Xi_D  (>0 under GRH).
  Jensen polynomial  J^{d,n}(X) = sum_j C(d,j) a_{n+j} X^j;  margin = min-gap/spread of its real roots.
  We record, at shift n=0 (the infimum/tightest), the margins for d=2..DMAX_TOWER and the Hermite-relative
  margin (margin / Hermite_d margin) -- the latter isolates the arithmetic deviation from the GUE/Gaussian.

Backends: PARI via cypari2 (fast approximate-functional-equation L-eval, high conductor) if importable;
else mpmath (direct Hurwitz sum, |D| <~ 800). DFT-Cauchy Taylor coeffs + root margins done in mpmath.
Parallel over discriminants. Output: CSV (one row per character).

Usage:  python jensen_dtower_sweep.py --dmax 2000 --procs 32 --out sweep.csv
        python jensen_dtower_sweep.py --dmax 50 --procs 4 --backend mpmath   # local validation
No torch. Deterministic.
"""
import sys, csv, argparse, math
import mpmath as mp
from multiprocessing import Pool

import os
mp.mp.dps = int(os.environ.get("JDPS", "40"))
NPTS = int(os.environ.get("JNPTS", "128"))            # DFT points
TOWER = list(range(2, int(os.environ.get("JTOWER", "9")) + 1))   # d = 2..JTOWER
PARIPREC = int(os.environ.get("JPARIPREC", "40"))
def radius_for(q):     # SMALL radius, safely inside the first zero for all conductors in range
    return max(mp.mpf('0.4'), min(mp.mpf('0.6'), mp.mpf('2.5')/(2 + mp.log(q))))

# ---------- number theory ----------
def squarefree(n):
    n = abs(n); d = 2
    while d*d <= n:
        if n % (d*d) == 0: return False
        if n % d == 0: n //= d
        else: d += 1
    return True

def is_fundamental(D):
    if D in (0, 1): return False
    if D % 4 == 1: return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return (m % 4 in (2, 3)) and squarefree(m)
    return False

def kronecker(a, n):
    if n == 0: return 1 if abs(a) == 1 else 0
    res = 1
    if n < 0:
        n = -n
        if a < 0: res = -res
    if n % 2 == 0:
        if a % 2 == 0: return 0          # (even / even) = 0 for ANY power of 2 in n
        while n % 2 == 0:
            n //= 2
            if a % 8 in (3, 5): res = -res
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

# ---------- backends: Xi_D(t) (analytic; real on R) ----------
def make_Xi_mpmath(D):
    q = abs(D); eps = 1 if D < 0 else 0
    chi = [kronecker(D, a) for a in range(q)]
    def L(s): return q**(-s) * mp.fsum(chi[a]*mp.zeta(s, mp.mpf(a)/q) for a in range(1, q) if chi[a])
    def Xi(t):
        s = mp.mpf(1)/2 + 1j*t
        return (q/mp.pi)**((s+eps)/2) * mp.gamma((s+eps)/2) * L(s)
    return Xi

def make_Xi_pari(pari, D):
    Lf = pari.lfuncreate(int(D))
    nd = mp.mp.dps + 5
    bits = int(mp.mp.dps * 3.3219) + 40       # computation precision (cypari2 wants BITS)
    PSC = pari(10)**nd; rnd = pari("round"); rl = pari("real"); im = pari("imag")
    den = mp.mpf(10)**nd
    def Xi(t):                                # t = mpmath.mpc on the contour
        tr = pari(mp.nstr(mp.re(t), nd)); ti = pari(mp.nstr(mp.im(t), nd))
        s = pari("1/2") + pari("I")*(tr + ti*pari("I"))
        z = pari.lfunlambda(Lf, s, precision=bits)   # cypari2 str() caps display -> extract via int scaling
        zr = mp.mpf(int(rnd(rl(z)*PSC))) / den
        zi = mp.mpf(int(rnd(im(z)*PSC))) / den
        return mp.mpc(zr, zi)
    return Xi

# ---------- Taylor coeffs + Jensen margins ----------
def taylor_a(Xi, M, r):
    pts = [Xi(r*mp.e**(2j*mp.pi*j/NPTS)) for j in range(NPTS)]
    out = []
    for m in range(M+1):
        c = mp.fsum(pts[j]*mp.e**(-2j*mp.pi*(2*m)*j/NPTS) for j in range(NPTS)) / (NPTS*r**(2*m))
        out.append((-1)**m * mp.re(c))
    return out

def margin(A, d, n=0):
    if A[n+1] == 0: return None
    rho = A[n]/A[n+1]
    coef = [mp.binomial(d, j)*A[n+j]*rho**j for j in range(d+1)]
    roots = mp.polyroots([coef[d-j] for j in range(d+1)], maxsteps=800, extraprec=150)
    im = max(abs(mp.im(r)) for r in roots); re = sorted(mp.re(r) for r in roots)
    if im > mp.mpf(10)**-6 * (1 + max(abs(x) for x in re)): return None
    sp = re[-1]-re[0]
    if sp == 0: return None
    g = [re[i+1]-re[i] for i in range(len(re)-1)]
    return float(min(g)/sp)

# Hermite reference margins (n->inf limit), computed once
def _hermite_coeffs(d):
    H = [[mp.mpf(1)], [mp.mpf(0), mp.mpf(2)]]
    for k in range(1, d):
        nxt = [mp.mpf(0)]*(k+2)
        for i, c in enumerate(H[k]): nxt[i+1] += 2*c
        for i, c in enumerate(H[k-1]): nxt[i] -= 2*k*c
        H.append(nxt)
    return list(reversed(H[d]))
def hermite_margin(d):
    with mp.workdps(60):                       # reference constants -> fixed modest precision (fast)
        rts = mp.polyroots(_hermite_coeffs(d), extraprec=40)
        re = sorted(mp.re(r) for r in rts); sp = re[-1]-re[0]
        g = [re[i+1]-re[i] for i in range(len(re)-1)]
        return float(min(g)/sp)
HERM = {d: hermite_margin(d) for d in TOWER}

# ---------- per-character worker ----------
def worker(item):
    D, backend = item
    try:
        pari = None
        if backend in ("auto", "pari"):
            try:
                import cypari2
                pari = cypari2.Pari(); pari.set_real_precision(PARIPREC)
            except Exception:
                pari = None
        Xi = make_Xi_pari(pari, D) if pari is not None else make_Xi_mpmath(D)
        A = taylor_a(Xi, max(TOWER), radius_for(abs(D)))
        if not all(mp.re(x) > 0 for x in A[:5]):
            return (D, abs(D), "odd" if D < 0 else "even", None, {}, "coeffs<=0")
        row = {}
        for d in TOWER:
            m = margin(A, d, 0)
            row[d] = m
        cv = float(A[0])     # ~ central value (completed)
        return (D, abs(D), "odd" if D < 0 else "even", cv, row, "ok")
    except Exception as e:
        return (D, abs(D), "odd" if D < 0 else "even", None, {}, f"err:{type(e).__name__}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dmax", type=int, default=2000)
    ap.add_argument("--procs", type=int, default=8)
    ap.add_argument("--backend", choices=["auto", "pari", "mpmath"], default="auto")
    ap.add_argument("--out", default="jensen_dtower_sweep.csv")
    ap.add_argument("--parity", choices=["odd", "even", "both"], default="both")
    ap.add_argument("--only", default="", help="comma-separated explicit discriminants (overrides --dmax)")
    args = ap.parse_args()
    if args.only:
        cand = [int(x) for x in args.only.split(",")]
    else:
        cand = list(range(-args.dmax, args.dmax+1))
    Ds = [D for D in cand if is_fundamental(D)
          and (args.parity == "both" or (args.parity == "odd") == (D < 0))]
    print(f"[sweep] {len(Ds)} fundamental discriminants |D|<={args.dmax}; backend={args.backend}; "
          f"procs={args.procs}; tower d={TOWER}; Hermite margins={ {d: round(HERM[d],4) for d in TOWER} }")
    sys.stdout.flush()

    rows = []
    work = [(D, args.backend) for D in Ds]
    with Pool(args.procs) as pool:
        for i, res in enumerate(pool.imap_unordered(worker, work, chunksize=1)):
            rows.append(res)
            if (i+1) % 25 == 0:
                print(f"[sweep] {i+1}/{len(Ds)} done"); sys.stdout.flush()

    rows.sort(key=lambda r: r[0])
    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["D", "conductor", "parity", "central"] +
                   [f"margin_d{d}" for d in TOWER] + [f"rel_d{d}" for d in TOWER] + ["status"])
        for D, q, par, cv, row, st in rows:
            mvals = [row.get(d) for d in TOWER]
            rvals = [(row.get(d)/HERM[d]) if row.get(d) is not None else None for d in TOWER]
            w.writerow([D, q, par, cv] + mvals + rvals + [st])
    ok = sum(1 for r in rows if r[5] == "ok")
    print(f"[sweep] wrote {args.out}: {ok}/{len(rows)} ok")

if __name__ == "__main__":
    main()
