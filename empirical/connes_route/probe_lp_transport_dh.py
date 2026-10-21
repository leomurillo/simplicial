r"""
probe_lp_transport_dh.py -- the matched-pair falsifier for the LP transport section.

K/L pair (Paper 35 GPD method): zeta (Euler product, RH holds numerically) versus the
Davenport-Heilbronn function f = sum a_n n^{-s}, a = (0,1,k,-k,-1) mod 5 -- same functional-
equation SHAPE (self-dual, real coefficients, Gamma_R(s+1), conductor 5), NO Euler product,
zeros off the line (first: 0.808517 + 85.699348 i).  Same CCM/CvS machinery, same code
(lp_transport_core.py, kind='dh'): poles removed, beta=-1/2 archimedean kernel, log 5 conductor,
Lambda_f(n) on ALL n from -f'/f.

QUESTION.  The LP transport theorem says: (a) even-simple ground  +  S(lambda) bounded  +
convergence on one real interval  =>  the limit is Laguerre-Polya.  Xi_DH is NOT LP, so for DH at
least one of the three must fail.  WHICH ONE?

CHECKS
  D0  data: functional equation, the off-line zeros, on-line count vs N(T); Lambda_f vs -f'/f at s=3;
      archimedean (beta=-1/2, log 5) functional vs frequency-space digamma integral on a test pair.
  D1  zero-side validation of the DH matrix entry QW[V0,V0] at lambda=3 (all zeros <= 130 + tail).
  D2  the ladder: eps_even, odd ground, Krein-Langer index (# negative eigenvalues per sector),
      hypothesis (a), S(lambda), sigma = S/(L^2/24), real-rootedness when (a) holds.
  D3  the edge mode: post-transition S -> L^2/8 (sigma -> 3) = the scalar of cos(zL/2); the
      ground state's mass migrates to the window edges u = +-L/2.
  D4  detection thresholds: lambda at which each off-line quadruple adds a negative direction.

mpmath (pre-transition, tiny eigenvalues) + numpy float64 (post-transition, O(1) eigenvalues).
"""
import sys
import time
import math

sys.path.insert(0, r"C:/Projects/simplicial/empirical/connes_route")
import numpy as np
import mpmath as mp
import lp_transport_core as core

sys.stdout.reconfigure(encoding="utf-8")


def sectors_np(lam, N, kind, dps=20):
    keep = mp.mp.dps
    mp.mp.dps = dps
    S, D, L = core.per_frequency(mp.mpf(lam), N, kind)
    mp.mp.dps = keep
    Sv = np.array([float(S[k]) for k in range(N + 1)])
    Dv = np.array([float(D[k]) for k in range(N + 1)])
    Sf = lambda k: Sv[k] if k >= 0 else -Sv[-k]

    def QW(n, m):
        return Dv[abs(n)] if n == m else (Sf(m) - Sf(n)) / (np.pi * (n - m))

    Ev = np.zeros((N + 1, N + 1))
    Od = np.zeros((N, N))
    for k in range(N + 1):
        for l in range(N + 1):
            if k == 0 and l == 0:
                Ev[k, l] = QW(0, 0)
            elif k == 0:
                Ev[k, l] = math.sqrt(2) * QW(l, 0)
            elif l == 0:
                Ev[k, l] = math.sqrt(2) * QW(k, 0)
            else:
                Ev[k, l] = QW(k, l) + QW(k, -l)
    for k in range(1, N + 1):
        for l in range(1, N + 1):
            Od[k - 1, l - 1] = QW(k, l) - QW(k, -l)
    return Ev, Od, float(L)


def S_np(x, L):
    xi = np.concatenate([[x[0]], x[1:] / math.sqrt(2)])
    if xi[0] < 0:
        xi = -xi
    k = np.arange(1, len(xi))
    return L * L / 24 + L * L / (2 * math.pi ** 2) * np.sum(xi[1:] / k ** 2) / xi[0], xi


def edge_fraction(xi, L, width=0.5, M=4001):
    """fraction of |f(u)|^2 within `width` of the window edges, f(v)=sum c_n e^{2 pi i n v/L}, v in [-L/2, L/2]."""
    v = np.linspace(-L / 2, L / 2, M)
    f = np.full_like(v, xi[0])
    for k in range(1, len(xi)):
        f = f + 2 * ((-1) ** k) * xi[k] * np.cos(2 * math.pi * k * v / L)
    w = f * f
    edge = np.abs(np.abs(v) - L / 2) <= width
    return float(np.trapezoid(w * edge, v) / np.trapezoid(w, v))


def secular_real_count_np(xi):
    """count positive real roots of rho(v) = xi0/v - 2 sum xi_k/(k^2 - v) (expect N if all real)."""
    N = len(xi) - 1
    ks = np.arange(1, N + 1)
    cnt = 0
    M = 400
    cheb = 0.5 - 0.5 * np.cos(np.pi * np.arange(1, M) / M)          # clustered at both ends
    cheb = np.concatenate([[1e-12, 1e-9, 1e-6], cheb, [1 - 1e-6, 1 - 1e-9, 1 - 1e-12]])
    for k in range(0, N):
        lo, hi = float(k * k), float((k + 1) ** 2)
        g = lo + (hi - lo) * cheb
        r = xi[0] / g - 2 * np.array([np.sum(xi[1:] / (ks ** 2 - gg)) for gg in g])
        cnt += int(np.sum(np.sign(r[:-1]) != np.sign(r[1:])))
    g = float(N * N) * (1 + np.geomspace(1e-12, 1e4, 4000))         # beyond the last pole
    r = xi[0] / g - 2 * np.array([np.sum(xi[1:] / (ks ** 2 - gg)) for gg in g])
    cnt += int(np.sum(np.sign(r[:-1]) != np.sign(r[1:])))
    return cnt


def main():
    ok = True
    print("=" * 100)
    print("LP transport, matched pair: Davenport-Heilbronn through the CCM/CvS machine")
    print("=" * 100)

    # ------------------------------------------------------------------ D0: data
    mp.mp.dps = 30
    fe = max(abs(core.Lambda_dh(s) - core.Lambda_dh(1 - s)) / abs(core.Lambda_dh(s))
             for s in (mp.mpc(0.3, 2.1), mp.mpc(0.8, 10.5), mp.mpc(2.0, 0.7)))
    offl = []
    for g in (mp.mpc("0.8085", "85.699"), mp.mpc("0.6508", "114.163"), mp.mpc("0.5744", "166.479"),
              mp.mpc("0.7242", "176.702")):
        r = mp.findroot(core.f_dh, g)
        offl.append(r)
    print(f"D0  functional equation |Lambda(s)-Lambda(1-s)|/|Lambda| <= {mp.nstr(fe, 3)}")
    for r in offl:
        print(f"    off-line zero {mp.nstr(r, 12)}   delta = Re(rho)-1/2 = {mp.nstr(mp.re(r) - 0.5, 6)}   "
              f"|f| = {mp.nstr(abs(core.f_dh(r)), 2)}")
    ok &= fe < mp.mpf("1e-25") and all(abs(core.f_dh(r)) < mp.mpf("1e-20") for r in offl)
    # Lambda_f vs -f'/f at s = 3
    Lf = core.lambda_f_dh(20000)
    s3 = mp.mpf(3)
    lhs = mp.fsum(v * mp.power(n, -s3) for n, v in Lf.items())
    rhs = -mp.diff(core.f_dh, s3) / core.f_dh(s3)
    print(f"    Lambda_f check: sum_(n<=2e4) Lambda_f(n) n^-3 = {mp.nstr(lhs, 14)}  vs  -f'/f(3) = {mp.nstr(rhs, 14)}")
    ok &= abs(lhs - rhs) < mp.mpf("1e-7")
    # archimedean functional (beta=-1/2, log 5) vs frequency-space formula on a Gaussian test pair:
    # g(y) = exp(-y^2/2) (q = 2g), h(t) = sqrt(2 pi) exp(-t^2/2)
    #   u-space: (log5 - log pi - gamma) g(0) + int_0^inf [e^{-y} g(0) - e^{-y/2} g(y)] / sinh y dy
    #   t-space: (log5 - log pi) g(0) + (1/2pi) int h(t) Re psi(3/4 + i t/2) dt
    g = lambda y: mp.exp(-y * y / 2)
    u_side = ((mp.log(5) - mp.log(mp.pi) - mp.euler) * g(0)
              + mp.quad(lambda y: (mp.exp(-y) * g(0) - mp.exp(-y / 2) * g(y)) / mp.sinh(y) if y > 0 else mp.mpf(0),
                        [0, 1, 5, mp.inf]))
    t_side = ((mp.log(5) - mp.log(mp.pi)) * g(0)
              + mp.quad(lambda t: mp.sqrt(2 * mp.pi) * mp.exp(-t * t / 2) * mp.re(mp.digamma(mp.mpf(3) / 4 + 1j * t / 2)),
                        [-mp.inf, 0, mp.inf]) / (2 * mp.pi))
    print(f"    archimedean functional: u-space {mp.nstr(u_side, 15)}  vs  t-space {mp.nstr(t_side, 15)}")
    ok &= abs(u_side - t_side) < mp.mpf("1e-20")

    # ------------------------------------------------------------------ D1: zero-side validation
    mp.mp.dps = 30
    lam = mp.mpf(3)
    L = 2 * mp.log(lam)
    S_, D_, _ = core.per_frequency(lam, 2, "dh")
    entry = D_[0]
    # zero side: sum over all zeros rho of h(gamma_rho), h = FT of the diag autocorrelation g(y)=(1-|y|/L)
    #            h(z) = int_{-L}^{L} (1-|y|/L) e^{i z y} dy = L (sin(zL/2)/(zL/2))^2  (entire)
    hz = lambda z: L * (mp.sin(z * L / 2) / (z * L / 2)) ** 2
    zs = []
    prev_t, prev_v = mp.mpf("0.05"), core.Xi_dh(mp.mpf("0.05"))
    t = prev_t
    while t < 130:
        t += mp.mpf("0.05")
        v = core.Xi_dh(t)
        if (v > 0) != (prev_v > 0):
            zs.append(mp.findroot(core.Xi_dh, (prev_t, t), solver="anderson"))
        prev_t, prev_v = t, v
    on = mp.fsum(2 * hz(z) for z in zs)                       # +-gamma
    off = mp.mpf(0)
    for r in offl:
        if mp.im(r) < 130:
            gam = -1j * (r - mp.mpf(1) / 2)                     # t - i delta
            for gg in (gam, mp.conj(gam), -gam, -mp.conj(gam)):
                off += hz(gg)
    zero_side = on + mp.re(off)
    # tail beyond T=130: density (1/2pi) log(5t/2pi), mean of h ~ 2/(L t^2), both signs
    T = mp.mpf(130)
    tail = 2 * mp.quad(lambda tt: mp.log(5 * tt / (2 * mp.pi)) / (2 * mp.pi) * 2 / (L * tt * tt), [T, mp.inf])
    print(f"\nD1  QW_DH[V0,V0] at lambda=3: closed form {mp.nstr(entry, 10)}; zero side (|gamma|<130, "
          f"{len(zs)} on-line + {sum(1 for r in offl if mp.im(r) < 130)} off-line pairs) {mp.nstr(zero_side, 10)}; "
          f"tail allowance ~{mp.nstr(tail, 3)}")
    d1 = abs(entry - zero_side) < 2 * tail
    print("    " + ("PASS" if d1 else "FAIL") + f"  (|diff| = {mp.nstr(abs(entry - zero_side), 3)})")
    ok &= d1

    # ------------------------------------------------------------------ D2/D3: the ladder
    print("\nD2  ladder (all rungs mpmath; 110 digits through the transition, where the bulk ground's")
    print("    transform is ~e^{-pi t/4} at the top heights; 40 digits for the O(1) edge regime)")
    print("    idx(e,o) = resolved Krein-Langer index: # eigenvalues < -10^{-dps/2} in the even / odd sector")
    print("  lambda    L     N   eps_even        odd ground      mu1_even       idx(e,o)  (a)  S(lambda)    "
          "sigma=S/(L^2/24)  real roots  edge mass(|u|>L/2-1/2)")
    ladder = [2, 3, 4, 4.5, 5, 5.25, 5.5, 5.75, 6, 6.5, 7, 8, 10, 12, 15, 20, 30]
    records = []
    for lam_f in ladder:
        L = 2 * math.log(lam_f)
        N = int(max(40, 33 * L))                          # resolves heights 2 pi N / L >= ~205
        mp.mp.dps = 110 if lam_f <= 6.5 else 40
        Ev, Od, _, _, Lm = core.sectors(mp.mpf(lam_f), N, "dh")
        ve, vecs = core.low_eig(Ev, 1)
        vo, _ = core.low_eig(Od, 1)
        xi_mp = core.even_coeffs(vecs[0])
        Sl = float(core.S_of(xi_mp, Lm))
        xi = np.array([float(v) for v in xi_mp])
        # resolved Krein-Langer index: eigenvalues below -tau, tau = 10^{-dps/2}, far above round-off
        # (~10^{-dps}); the shrinking bulk cluster below tau is reported as unresolved, not counted
        tau = mp.mpf(10) ** (-(mp.mp.dps // 2))
        ne = sum(1 for v in ve if v < -tau)
        no = sum(1 for v in vo if v < -tau)
        eps, mu1, odd0 = float(ve[0]), float(ve[1]), float(vo[0])
        a_ok = eps < odd0 and eps < mu1
        # CvS: (a) => all N secular roots real; counted at full working precision
        nreal = len(core.real_zeros_v(xi_mp, pts_per_interval=30, refine=False)) if a_ok else -1
        sigma = Sl / (L * L / 24)
        ef = edge_fraction(xi, L)
        records.append((lam_f, L, N, eps, odd0, mu1, ne, no, a_ok, Sl, sigma, nreal, ef))
        print(f"  {lam_f:6.2f} {L:5.2f} {N:5d}  {eps: .4e}   {odd0: .4e}   {mu1: .4e}   ({ne},{no})    "
              f"{'Y' if a_ok else 'N'}   {Sl: .5e}   {sigma:8.4f}         "
              f"{(str(nreal)+'/'+str(N)) if nreal >= 0 else '  -  ':>9s}   {ef:.3f}")
        if a_ok:
            ok &= (nreal == N)                                  # CvS: (a) => all real

    # D3: the edge mode
    post = [r for r in records if r[0] >= 10]
    sig_last = post[-1][10]
    print(f"\nD3  edge mode: sigma -> {sig_last:.4f} at lambda = {post[-1][0]} (cos(zL/2) has sigma = 3 exactly: "
          f"S = L^2/8); pre-transition sigma -> S_Xi_DH/(L^2/24) -> 0")
    ok &= abs(sig_last - 3) < 0.05
    # ------------------------------------------------------------------ D4: thresholds
    print("\nD4  Krein-Langer index (negative directions per sector) vs lambda; off-line quadruples by height:")
    for r in offl:
        print(f"      T = {mp.nstr(mp.im(r), 8):>10s}   delta = {mp.nstr(mp.re(r) - 0.5, 5)}")
    jumps = []
    prev = 0
    lam_grid = np.round(np.arange(4.5, 16.01, 0.25), 2)
    for lam_f in lam_grid:
        L = 2 * math.log(lam_f)
        N = int(max(40, 33 * L))
        Ev, Od, L = sectors_np(lam_f, N, "dh")
        ne = int(np.sum(np.linalg.eigvalsh(Ev) < -1e-9))
        if ne != prev:
            jumps.append((lam_f, prev, ne))
            prev = ne
    for lam_f, a, b in jumps:
        print(f"      even-sector index {a} -> {b} between lambda = {lam_f - 0.25:.2f} and {lam_f:.2f}")

    print("\nRESULT:", "GREEN" if ok else "RED")
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
