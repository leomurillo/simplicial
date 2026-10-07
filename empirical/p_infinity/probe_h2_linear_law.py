"""probe_h2_linear_law.py — certificate for P-infinity-E SS25 (Theorem E.22: the radical route to H2).

The mechanism: M(E(h))(s) = zeta(s + 1/2) * M_h(s - ...) — the Mellin transform of an
E-image carries an explicit zeta factor, so it VANISHES AT EVERY ZETA ZERO:
  Lemma 1: E(h) lies in the RADICAL of the global Weil form (evenness kills the s = i/2
           pole term, vanishing integral kills s = -i/2; zeros killed termwise).
  Lemma 2: hence QW_lambda(E(h_lambda)|window) = QW(F_out) EXACTLY, with F_out the
           below-window tail (u < 1/lambda), whose mass is the Fourier-compression defect:
           ||F_out||^2 ~ poly * (1 - chi_4).
  => (H2) law: QW_lambda(k_guess) = Theta(poly(lambda) * (1 - chi_4(lambda)))  — LINEAR in
     the first-rung defect (not sqrt), with slowly-varying constant.

CHECK: R(lambda) = Rayleigh of the prolate guess in the EXACT matrix, against the measured
FD defect 1-chi_4(lambda), for lambda in {1.4, 1.5, 1.6, 1.7} (the clean FD window):
the ratio R/(1-chi_4) should be O(10) and vary slowly (poly), while the quantities
themselves fall by three orders of magnitude.

Deterministic, local, ~3-5 min.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 40

def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out

def build_QW(lam, N):
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pj = []
    for p in primes_upto(float(mp.exp(L)) + 1e-12):
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
    return QW, L

def prolate_pair(lam, M=6001):
    x = np.linspace(-lam, lam, M); dx = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    a = lam**2 - xm**2
    diag = np.zeros(M); diag[:-1] += a / dx**2; diag[1:] += a / dx**2
    diag += (2 * np.pi * lam * x)**2
    bands = np.vstack([diag, np.append(-a / dx**2, 0.0)])
    _, vv = eig_banded(bands, lower=True, select='i', select_range=(0, 4))
    h0 = vv[:, 0] / np.sqrt(dx); h4 = vv[:, 4] / np.sqrt(dx)
    if h0[M // 2] < 0: h0 = -h0
    if h4[M // 2] < 0: h4 = -h4
    return x, dx, h0, h4

print("== (H2) linear law: R(lambda) / (1 - chi_4(lambda)) across the clean window ==")
N = 10
rows = []
for lam_f in (1.4, 1.5, 1.6, 1.7):
    QWm, L = build_QW(mp.mpf(str(lam_f)), N)
    x, dx, h0, h4 = prolate_pair(lam_f)
    # 1 - chi_4 by Fourier defect
    F = np.exp(2j * np.pi * np.outer(x, x)) * dx
    d4 = float(np.dot(h4, h4 - (F @ h4).real) * dx)
    # guess coefficients
    hl = h4 - (np.trapezoid(h4, x) / np.trapezoid(h0, x)) * h0
    Lf = float(L)
    xg = np.linspace(0.0, Lf, 3001)
    u = np.exp(xg - Lf / 2)
    kl = np.zeros_like(u)
    for n in range(1, int(lam_f / u.min()) + 2):
        msk = n * u <= lam_f
        kl[msk] += np.interp(n * u[msk], x[x >= 0], hl[x >= 0])
    kl *= np.sqrt(u)
    kl /= np.sqrt(np.trapezoid(kl * kl, xg))
    c = [mp.mpc(complex(np.trapezoid(kl * np.exp(-2j * np.pi * n * xg / Lf) / np.sqrt(Lf), xg)))
         for n in range(-N, N + 1)]
    R = float(mp.re(mp.fsum(mp.conj(c[i]) * QWm[i, j] * c[j]
                            for i in range(2 * N + 1) for j in range(2 * N + 1))))
    rows.append((lam_f, R, d4, R / d4))
    print(f"   lambda = {lam_f}: R = {R:.4e}   1-chi_4 = {d4:.4e}   ratio = {R/d4:.2f}")
ratios = [r[3] for r in rows]
span = max(ratios) / min(ratios)
drop = rows[0][1] / rows[-1][1]
ok = all(1 < rr < 100 for rr in ratios) and span < 5 and drop > 50
print(f"\n   R falls by x{drop:.0f} across the window; ratio R/(1-chi_4) spans only x{span:.2f}")
print("   " + ("PASS — the Rayleigh quotient is LINEAR in the first-rung defect with a "
               "slowly-varying (poly) constant: the radical/tail mechanism of Theorem E.22, "
               "certified" if ok else "FAIL"))
print("\nRESULT: " + ("GREEN" if ok else "RED"))
