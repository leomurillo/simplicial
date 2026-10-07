"""
probe_archimedean_edge_law.py — the ground-eigenvalue / edge-coefficient LAW of QW_lambda,
and the test of the prolate DEFINITE-SIGN hypothesis for the surviving obligation (H0').

ATTACK (Second Note §3-§4 / N11 §7):
  RH at the archimedean place  <=>  eps_lambda >= 0 surviving lambda->infty
       <=> edge Schur coefficient k_edge < 1 surviving  <=>  QW_lambda stays PSD.
  The CvS smallness mechanism (§3, probe_h2_linear_law) proves the UPPER bound
       R := QW_lambda(prolate guess) ~ poly(lambda) * (1 - chi_4(lambda)),
  where (1 - chi_4) > 0 ALWAYS (the prolate Fourier-compression defect). That bounds eps
  ABOVE (smallness). The OBLIGATION is the LOWER bound eps_lambda >= 0.

  THE TEST: does the TRUE ground eps_lambda track the always-positive prolate defect with a
  POSITIVE constant,  eps_lambda / (1 - chi_4) -> c_eps > 0  (stable in lambda, N)?
    * if YES  -> (H0') reduces to "c_eps > 0": the prolate cascade SUPPLIES the sign,
                 because (1 - chi_4) > 0 is a theorem of prolate theory.
    * if eps/(1-chi_4) -> 0 or flips sign -> the true ground sits below the prolate guess;
                 the sign is open at a finer scale than the smallness bound resolves.

STRUCTURE WATCH: the semilocal window contains primes p with p <= lambda^2, so a new prime
JOINS at lambda = sqrt(p): sqrt(2)=1.414, sqrt(3)=1.732, sqrt(5)=2.236. Each joining injects
NEGATIVE prime energy (-P). The ladder below crosses all three. Does eps_lambda dip (or go
negative) at a joining? That is the §13 prime-joining ladder seen inside Weil positivity.

Reuses build_QW (probe_h2_linear_law conventions) + even-fold/ldl (probe_archimedean_schur)
+ prolate_pair (probe_h2_linear_law). mpmath dps 30 for eps/k_edge (reliable ~1e-30); scipy
float64 for (1 - chi_4) (reliable ~1e-12, flagged below that). Deterministic, local. No torch.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

SQRT = {2: mp.sqrt(2), 3: mp.sqrt(3), 5: mp.sqrt(5), 7: mp.sqrt(7)}


def primes_upto(xx):
    out, n = [], 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW(lam, N):
    """Full (2N+1)x(2N+1) semilocal Weil matrix (probe_h2_linear_law conventions)."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    primes = primes_upto(float(mp.exp(L)) + 1e-12)
    pj = []
    for p in primes:
        j = 1
        while j * mp.log(p) <= L + mp.mpf("1e-30"):
            pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
            j += 1
    pts = mp.linspace(0, L, 16)
    S = {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj)
        S[k] = A - B - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = D[abs(n)] if n == m else (S[m] - S[n]) / (mp.pi * (n - m))
    return QW, L, primes


def even_sector(QW, N):
    """Fold to the (N+1)x(N+1) even sector (probe_archimedean_schur conventions)."""
    Ev = mp.matrix(N + 1, N + 1)
    for k in range(N + 1):
        for l in range(N + 1):
            a, b = QW[N + k, N + l], QW[N + k, N - l]
            if k == 0 and l == 0:
                Ev[k, l] = a
            elif k == 0 or l == 0:
                Ev[k, l] = mp.sqrt(2) * a
            else:
                Ev[k, l] = a + b
    return Ev


def ldl_pivots(A):
    n = A.rows
    M = mp.matrix(A.tolist())
    d, Lmat = [], mp.eye(n)
    for j in range(n):
        s = M[j, j] - mp.fsum(Lmat[j, k] ** 2 * d[k] for k in range(j))
        d.append(s)
        for i in range(j + 1, n):
            Lmat[i, j] = 0 if s == 0 else (M[i, j] - mp.fsum(Lmat[i, k] * Lmat[j, k] * d[k] for k in range(j))) / s
    return d


def edge_and_ground(Ev, N):
    diag = [Ev[m, m] for m in range(N + 1)]
    d = ldl_pivots(Ev)
    kk = []
    for m in range(N + 1):
        r = 1 - d[m] / diag[m] if diag[m] != 0 else mp.mpf(1)
        kk.append(mp.sqrt(r) if r >= 0 else -mp.sqrt(-r))
    k_edge = max(abs(x) for x in kk)
    eps = min(mp.mpf(str(e)) for e in mp.eigsy(Ev, eigvals_only=True))
    return eps, k_edge, min(d)


def prolate_defect_and_R(lam_f, L, QWm, N):
    """1 - chi_4 (Fourier-compression defect of the 4th prolate mode) and R = guess Rayleigh.
    float64 (scipy); reliable while 1-chi_4 > ~1e-12."""
    M = 6001
    x = np.linspace(-lam_f, lam_f, M); dx = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    a = lam_f ** 2 - xm ** 2
    diag = np.zeros(M); diag[:-1] += a / dx ** 2; diag[1:] += a / dx ** 2
    diag += (2 * np.pi * lam_f * x) ** 2
    bands = np.vstack([diag, np.append(-a / dx ** 2, 0.0)])
    _, vv = eig_banded(bands, lower=True, select='i', select_range=(0, 4))
    h0 = vv[:, 0] / np.sqrt(dx); h4 = vv[:, 4] / np.sqrt(dx)
    if h0[M // 2] < 0: h0 = -h0
    if h4[M // 2] < 0: h4 = -h4
    F = np.exp(2j * np.pi * np.outer(x, x)) * dx
    d4 = float(np.dot(h4, h4 - (F @ h4).real) * dx)         # 1 - chi_4
    # prolate guess k_lambda and its Rayleigh R in the exact matrix
    hl = h4 - (np.trapezoid(h4, x) / np.trapezoid(h0, x)) * h0
    Lf = float(L)
    xg = np.linspace(0.0, Lf, 3001)
    u = np.exp(xg - Lf / 2)
    kl = np.zeros_like(u)
    for n in range(1, int(lam_f / max(u.min(), 1e-9)) + 2):
        msk = n * u <= lam_f
        kl[msk] += np.interp(n * u[msk], x[x >= 0], hl[x >= 0])
    kl *= np.sqrt(u)
    nrm = np.trapezoid(kl * kl, xg)
    if nrm <= 0:
        return d4, float('nan')
    kl /= np.sqrt(nrm)
    c = [mp.mpc(complex(np.trapezoid(kl * np.exp(-2j * np.pi * n * xg / Lf) / np.sqrt(Lf), xg)))
         for n in range(-N, N + 1)]
    R = float(mp.re(mp.fsum(mp.conj(c[i]) * QWm[i, j] * c[j]
                            for i in range(2 * N + 1) for j in range(2 * N + 1))))
    return d4, R


def joinings_crossed(lam):
    return [p for p in (2, 3, 5, 7) if abs(float(lam) - float(SQRT[p])) < 0.12]


def run_point(lam, N, want_prolate=True):
    QWm, L, primes = build_QW(lam, N)
    Ev = even_sector(QWm, N)
    eps, k_edge, min_piv = edge_and_ground(Ev, N)
    d4 = R = float('nan')
    if want_prolate:
        d4, R = prolate_defect_and_R(float(lam), L, QWm, N)
    return dict(lam=float(lam), N=N, primes=primes, eps=eps, k_edge=k_edge,
                min_piv=min_piv, d4=d4, R=R)


def fmt(x, n=4):
    try:
        return mp.nstr(mp.mpf(x), n)
    except Exception:
        return str(x)


def main():
    print("=" * 100)
    print("Archimedean edge-law of QW_lambda — the prolate definite-sign test for (H0')")
    print("  eps_lambda = ground (min eig, even sector); k_edge = max|Schur k_m|;")
    print("  1-chi_4 = prolate Fourier-compression defect (>0 always); R = prolate-guess Rayleigh (>= eps).")
    print("  TEST: eps/(1-chi_4) -> c_eps > 0 stable?   STRUCTURE: prime joins at lambda=sqrt(p).")
    print("=" * 100)

    ladder = [1.35, 1.45, 1.5, 1.6, 1.7, 1.75, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]
    N0 = 12
    print(f"\nPRIMARY LADDER (N={N0}):")
    print(f"  {'lambda':>7} {'primes':>10} {'eps_lambda':>13} {'sgn':>4} {'k_edge':>11} "
          f"{'1-k_edge':>11} {'1-chi_4':>11} {'eps/(1-chi4)':>13} {'R/(1-chi4)':>11} {'R/eps':>8}")
    rows = []
    for lf in ladder:
        r = run_point(mp.mpf(str(lf)), N0)
        eps, d4, R = r["eps"], r["d4"], r["R"]
        sgn = "+" if eps > 0 else ("0" if eps == 0 else "-")
        d4_ok = (d4 == d4) and d4 > 1e-12
        ratio_e = float(eps) / d4 if d4_ok else float('nan')
        ratio_R = R / d4 if (d4_ok and R == R) else float('nan')
        rR = (R / float(eps)) if (R == R and eps != 0) else float('nan')
        join = joinings_crossed(r["lam"])
        tag = f"  <- sqrt({join[0]}) JOIN" if join else ""
        print(f"  {r['lam']:>7.3f} {str(r['primes']):>10} {fmt(eps,4):>13} {sgn:>4} "
              f"{fmt(r['k_edge'],6):>11} {fmt(1-r['k_edge'],3):>11} "
              f"{(fmt(d4,3) if d4_ok else 'noise'):>11} "
              f"{(f'{ratio_e:.3f}' if ratio_e==ratio_e else '--'):>13} "
              f"{(f'{ratio_R:.2f}' if ratio_R==ratio_R else '--'):>11} "
              f"{(f'{rR:.3f}' if rR==rR else '--'):>8}{tag}")
        rows.append((r, ratio_e, ratio_R, d4_ok))

    # ---- synthesis ----
    print("\n" + "-" * 100)
    eps_all = [r[0]["eps"] for r in rows]
    all_pos = all(e > 0 for e in eps_all)
    print(f"  (1) eps_lambda > 0 at EVERY window (per-window H0'): {all_pos}")
    clean = [(r[0]["lam"], r[1]) for r in rows if r[3] and r[1] == r[1]]
    if clean:
        print(f"  (2) eps/(1-chi_4) across the FD-clean window (1-chi_4 > 1e-12):")
        for lam, re_ in clean:
            print(f"        lambda={lam:.3f}: eps/(1-chi_4) = {re_:.4f}")
        vals = [v for _, v in clean]
        pos = all(v > 0 for v in vals)
        span = (max(vals) / min(vals)) if min(vals) > 0 else float('inf')
        print(f"      -> all positive: {pos};  spread x{span:.2f} "
              f"({'stable-positive const => prolate SUPPLIES the sign' if pos and span < 8 else 'NOT a clean positive constant'})")
    Rratios = [r[2] for r in rows if r[3] and r[2] == r[2]]
    if Rratios:
        print(f"  (3) R/(1-chi_4) [h2 reproduction, smallness UPPER bound]: spread x"
              f"{max(Rratios)/min(Rratios):.2f}, all O(10): {all(1 < x < 200 for x in Rratios)}")
    edge_creep = "  ".join(f"{r[0]['lam']:.2f}:{float(r[0]['k_edge']):.5f}" for r in rows)
    print(f"  (4) edge creep k_edge:  {edge_creep}")
    # feature at the joinings
    print(f"  (5) prime-joining features (eps just below/above sqrt(p)):")
    for p in (2, 3, 5):
        below = [r[0] for r in rows if r[0]["lam"] < float(SQRT[p])]
        above = [r[0] for r in rows if r[0]["lam"] >= float(SQRT[p])]
        if below and above:
            eb, ea = below[-1], above[0]
            print(f"        sqrt({p})={float(SQRT[p]):.3f}: eps {fmt(eb['eps'],3)} (lam={eb['lam']:.2f}, {eb['primes']}) "
                  f"-> {fmt(ea['eps'],3)} (lam={ea['lam']:.2f}, {ea['primes']})")

    # ---- N-drift at two representative windows ----
    print("\n" + "-" * 100)
    print("  N-CONVERGENCE / DRIFT (the v2-audit discipline):")
    for lf in (1.7, 2.1):
        print(f"   lambda={lf}:")
        for Nd in (10, 12, 14):
            r = run_point(mp.mpf(str(lf)), Nd, want_prolate=False)
            print(f"      N={Nd}: eps={fmt(r['eps'],5)}  k_edge={fmt(r['k_edge'],7)}  min_piv={fmt(r['min_piv'],3)}")

    print("\n" + "=" * 100)
    print("READING: (1) per-window H0' holds iff all eps>0; (2) is the verdict on whether the")
    print("prolate defect SUPPLIES the sign (eps/(1-chi_4) -> positive const) or only bounds it;")
    print("(5) shows whether a prime-joining (sqrt p) pushes the Weil ground toward 0/negative.")
    print("=" * 100)


if __name__ == "__main__":
    main()
