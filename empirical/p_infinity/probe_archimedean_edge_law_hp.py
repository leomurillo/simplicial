"""
probe_archimedean_edge_law_hp.py — HIGH-PRECISION prolate defect, extending the edge-law test.

The float64 prolate defect (1 - chi_4) of probe_archimedean_edge_law FLOORED at ~1e-11 (scipy
M=6001 grid + 64-bit cancellation), so eps/(1-chi_4) collapsed to noise past lambda~1.9. Here we
recompute (1 - chi_4) in arbitrary precision via the BOUWKAMP method and push the ladder to
lambda = 3.0, to settle the decisive question:

    does eps_lambda / (1 - chi_4)  stay a POSITIVE BOUNDED constant as the ground plunges
    (eps ~ 1e-12 ... 1e-30) across the prime-rich windows {2,3,5,7}?    [= (H0'), operator form]

METHOD (Bouwkamp, no oscillatory quadrature for the value):
  * The order-0 prolate ODE  -d/du[(1-u^2) d/du] psi + c^2 u^2 psi = chi psi  on [-1,1],
    c = 2 pi lambda^2, in the ORTHONORMAL Legendre basis P-bar_k = sqrt(k+1/2) P_k, is a
    symmetric tridiagonal matrix (even sector k=0,2,4,...):
        diag_k    = k(k+1) + c^2 (2k^2+2k-1)/((2k-1)(2k+3))
        offdiag_k = c^2 (k+1)(k+2) / ((2k+3) sqrt((2k+1)(2k+5)))    [k <-> k+2]
    Its eigenvectors are the prolate Legendre coefficients (mpmath, full precision).
  * The prolate diff. operator COMMUTES with the finite-Fourier operator F (kernel e^{i c x y})
    and hence with T = Re F (kernel cos), so psi_n is an eigenfunction of T with eigenvalue
    chi_n.  At x=0 this is a CLOSED FORM (no oscillatory integral):
        chi_4 = (T psi_4)(0) / psi_4(0) = lambda * integral psi_4 / psi_4(0)
              = lambda * sqrt(2) * beta_0  /  sum_i beta_i sqrt(2i+1/2) P_{2i}(0).
    1 - chi_4 then has only the benign "1 minus (~1)" cancellation, accurate to ~dps - 15 digits.

SELF-VALIDATION (GPD): (a) eigenfunction constancy — chi_4 from the x=0 closed form must equal
chi_4 = (T psi_4)(x)/psi_4(x) at an off-center x (oscillatory quad); (b) float64 calibration —
1-chi_4(hp) must match the scipy 1-chi_4 at lambda=1.5,1.7 (where float64 is reliable). Only then
is the high-lambda extension trusted.

Reuses build_QW/even_sector/ground (edge-law) for eps. mpmath dps 45. Deterministic, local. No torch.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 45
PI = mp.pi


# ----------------------------------------------------------------------- eps (QW ground)
def primes_upto(xx):
    out, n = [], 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW(lam, N):
    L = 2 * mp.log(lam)
    w = lambda k: 2 * PI * k / L
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
        WR = (mp.log(4 * PI) + mp.euler) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = D[abs(n)] if n == m else (S[m] - S[n]) / (PI * (n - m))
    return QW, primes


def ground(QW, N):
    Ev = mp.matrix(N + 1, N + 1)
    for k in range(N + 1):
        for l in range(N + 1):
            a, b = QW[N + k, N + l], QW[N + k, N - l]
            Ev[k, l] = a if (k == 0 and l == 0) else (mp.sqrt(2) * a if (k == 0 or l == 0) else a + b)
    return min(mp.mpf(str(e)) for e in mp.eigsy(Ev, eigvals_only=True))


# ----------------------------------------------------------------------- Bouwkamp prolate
def bouwkamp_even(c, K):
    """Symmetric tridiagonal of the order-0 prolate ODE, even sector k=0,2,...,2(K-1).
    Returns (eigenvalues ascending, eigenvector matrix Q) via mp.eigsy."""
    M = mp.zeros(K, K)
    for i in range(K):
        k = 2 * i
        M[i, i] = k * (k + 1) + c ** 2 * mp.mpf(2 * k * k + 2 * k - 1) / ((2 * k - 1) * (2 * k + 3))
        if i + 1 < K:
            off = c ** 2 * mp.mpf((k + 1) * (k + 2)) / ((2 * k + 3) * mp.sqrt((2 * k + 1) * (2 * k + 5)))
            M[i, i + 1] = off
            M[i + 1, i] = off
    E, Q = mp.eigsy(M)
    return E, Q


def chi4_hp(lam, K=None):
    """High-precision chi_4 = (T psi_4)(0)/psi_4(0), closed form in Bouwkamp coefficients.
    Returns (chi4, validation_residual, psi0)."""
    c = 2 * PI * lam ** 2
    if K is None:
        K = max(30, int(float(c) / 2) + 25)   # even-mode count; coeffs decay super-exp past ~c/2
    E, Q = bouwkamp_even(c, K)
    col = 2                                   # n=0,2,4 -> 4th mode (even) is index 2 (ascending)
    beta = [Q[i, col] for i in range(K)]      # orthonormal-Legendre coefficients of psi_4
    ks = [2 * i for i in range(K)]
    # psi_4(u) = sum beta_i sqrt(k_i + 1/2) P_{k_i}(u)
    def Psi(u):
        return mp.fsum(beta[i] * mp.sqrt(ks[i] + mp.mpf(1) / 2) * mp.legendre(ks[i], u) for i in range(K))
    psi0 = Psi(0)
    # closed form at x=0:  (T psi)(0) = lambda * integral_{-1}^1 Psi = lambda * sqrt(2) * beta_0
    chi0 = lam * mp.sqrt(2) * beta[0] / psi0
    # validation: eigenfunction constancy at an off-center xi (oscillatory quad)
    xi = mp.mpf("0.37")
    npar = max(40, int(float(c)) // 2)
    pts = mp.linspace(-1, 1, npar)
    Tpsi = lam * mp.quad(lambda u: mp.cos(c * xi * u) * Psi(u), pts)
    chi_xi = Tpsi / Psi(xi)
    resid = abs(chi0 - chi_xi)
    return chi0, resid, psi0


def chi4_f64(lam):
    """scipy float64 chi_4 (the original probe method) — for calibration in the clean window."""
    M = 6001
    x = np.linspace(-lam, lam, M); dx = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    a = lam ** 2 - xm ** 2
    diag = np.zeros(M); diag[:-1] += a / dx ** 2; diag[1:] += a / dx ** 2
    diag += (2 * np.pi * lam * x) ** 2
    bands = np.vstack([diag, np.append(-a / dx ** 2, 0.0)])
    _, vv = eig_banded(bands, lower=True, select='i', select_range=(0, 4))
    h4 = vv[:, 4] / np.sqrt(dx)
    if h4[M // 2] < 0: h4 = -h4
    F = np.exp(2j * np.pi * np.outer(x, x)) * dx
    return float(np.dot(h4, h4 - (F @ h4).real) * dx)        # 1 - chi_4


def ns(x, n=5):
    return mp.nstr(mp.mpf(x), n)


def main():
    print("=" * 104)
    print("HIGH-PRECISION edge-law: eps_lambda / (1 - chi_4) with Bouwkamp (arbitrary precision) prolate defect")
    print("  decisive test of (H0') operator form: does the ratio stay a POSITIVE BOUNDED constant as eps->0?")
    print("=" * 104)

    # ---- validation gate ----
    print("\nVALIDATION (must pass before trusting the extension):")
    print("  (a) eigenfunction constancy  |chi4(x=0) - chi4(x=0.37 lam)|   (should be ~1e-30)")
    print("  (b) float64 calibration      (1-chi4) hp vs scipy, lambda in clean window")
    gate_ok = True
    for lf in (1.5, 1.7):
        lam = mp.mpf(str(lf))
        chi, resid, _ = chi4_hp(lam)
        d_hp = 1 - chi
        d_f64 = chi4_f64(float(lam))
        rel = abs(d_hp - d_f64) / d_f64
        print(f"   lambda={lf}: 1-chi4(hp)={ns(d_hp,8)}  1-chi4(f64)={d_f64:.6e}  "
              f"rel.diff={float(rel):.2e}  eigfn-resid={ns(resid,2)}")
        gate_ok = gate_ok and (resid < mp.mpf("1e-20")) and (rel < 1e-5)
    print(f"  GATE: {'PASS' if gate_ok else 'FAIL — conventions off, do NOT trust extension'}")

    # ---- the extended ladder ----
    print("\n" + "-" * 104)
    ladder = [1.5, 1.7, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.7, 3.0]
    print("EXTENDED LADDER (eps: QW even-sector ground, N=14; 1-chi4: Bouwkamp hp):")
    print(f"  {'lambda':>7} {'primes':>12} {'eps_lambda':>13} {'1-chi4(hp)':>13} "
          f"{'eps/(1-chi4)':>13} {'eigfn-resid':>12}")
    rows = []
    for lf in ladder:
        lam = mp.mpf(str(lf))
        QW, primes = build_QW(lam, 14)
        eps = ground(QW, 14)
        chi, resid, _ = chi4_hp(lam)
        d_hp = 1 - chi
        ratio = eps / d_hp
        rows.append((lf, primes, eps, d_hp, ratio, resid))
        print(f"  {lf:>7.2f} {str(primes):>12} {ns(eps,5):>13} {ns(d_hp,5):>13} "
              f"{float(ratio):>13.4f} {ns(resid,2):>12}")

    # ---- synthesis ----
    print("\n" + "-" * 104)
    ratios = [r[4] for r in rows]
    allpos = all(r > 0 for r in ratios)
    pos_eps = all(r[2] > 0 for r in rows)
    valid = [r for r in rows if r[5] < mp.mpf("1e-15")]
    print(f"  eps_lambda > 0 at every window (per-window H0'): {pos_eps}")
    print(f"  eps/(1-chi4) > 0 at every window: {allpos}")
    if valid:
        rs = [float(r[4]) for r in valid]
        print(f"  eps/(1-chi4) over hp-validated windows: min={min(rs):.4f} max={max(rs):.4f} "
              f"spread x{max(rs)/min(rs):.2f}")
        print(f"     -> {'POSITIVE & BOUNDED across the plunge => prolate defect SUPPLIES the sign' if (min(rs)>0 and max(rs)/min(rs) < 30) else 'NOT a clean bounded positive constant — examine where it drifts'}")
    print(f"  ratio trend (lambda: eps/(1-chi4)):")
    print("     " + "  ".join(f"{r[0]:.2f}:{float(r[4]):.3f}" for r in rows))
    print("\n" + "=" * 104)
    print("READING: gate PASS validates the hp defect below the 1e-11 float64 floor. If eps/(1-chi4)")
    print("stays positive & O(1)-bounded as eps plunges through {2,3,5,7}, the prolate cascade supplies")
    print("the sign uniformly (strong (H0') evidence); a drift toward 0 localizes the difficulty.")
    print("=" * 104)


if __name__ == "__main__":
    main()
