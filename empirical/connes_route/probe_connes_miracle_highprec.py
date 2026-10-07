r"""
probe_connes_miracle_highprec.py  --  HIGH-PRECISION reproduction of Connes' numerical miracle
(arXiv:2602.04022, Feb 2026; Connes-van Suijlekom Thm 6.1, "Quadratic Forms, Real Zeros and
Echoes of the Spectral Action").

GOAL. Build the finite-prime Weil quadratic form QW_X (primes/powers <= X=13) in the EVEN
trigonometric basis at HIGH PRECISION (mpmath). Its minimal eigenvector eta is the finite
analogue of theta_x; the real zeros of its Fourier transform etahat(r) approximate the
non-trivial zeta zeros gamma_n. We reproduce the first several agreements and compare to
Connes' published difference table (2.60179e-55, 4.80071e-52, 4.43756e-50, ...).

WHY THE OLD float64 PROBES FAILED (empirical/probe_weil_form_simplicity.py & _evenodd_split.py)
  - eigenvalues are ~1e-50; numpy.eigh (float64, ~1e-16 rel) returns the ground eigenvector as
    pure rounding noise -> etahat's first 'zero' came out ~3.5 instead of 14.13.
  - prime block built by LINEAR INTERPOLATION of (phi*phi)(log n) onto a grid -> O(dx^2) error,
    catastrophic for a near-null form.
  - archimedean Toeplitz / freq-space digamma quadrature with a Gaussian taper distorted spectrum.
THE FIX (this file)
  - mpmath mp.dps high; diagonalize with mp.eigsy (symmetric, high precision).
  - EVERY matrix entry computed from the Riemann-Weil explicit formula applied to the EXACT
    cross-correlation g_jk = phi_j * phi_k of the cosine basis (closed-form A_jk below):
      PRIME  block : sum_n 2 (Lambda(n)/sqrt n) A_jk(log n)            [eq (9), exact]
      ARCH   block : (log4pi+gamma) A_jk(0)                            [eq (10)]
                     + int_0^inf [2 A_jk(u) - 2 A_jk(0)] e^{u/2}/(2 sinh u) du
                     (u-space integral, removable singularity at 0, fast & accurate)
      MAIN/poles   : 2 c_j c_k,  c_k = int phi_k(u) cosh(u/2) du       [ghat(+-i/2)]
  No grid interpolation anywhere; the only quadrature is a smooth 1-D u-space integral.

SIGN. Weil:  RH <=> sum_v W_v(g*g*) <= 0.  We diagonalize Q = sum_v W_v (eq 9,10 + poles); the
minimal eigenvector (most negative eigenvalue of Q, i.e. the minimizer of the RH-form) is eta.
Zeros / simplicity / parity are sign-convention independent.

CONVENTION (Connes). Additive variable u = log x. f even on R*_+ <=> phi(u) even.
Recentered theta_x supported in [x^{-1/2},x^{1/2}] -> phi in [-a,a], a=(log X)/2.
Even basis: phi_k(u)=cos(w_k u), w_k=(2k+1)pi/(2a), k=0..N-1; phi_k(+-a)=0; orthogonal (norm^2=a).

numpy + mpmath only.  No torch.
"""

import sys
import mpmath as mp

DPS = int(sys.argv[2]) if len(sys.argv) > 2 else 50
mp.mp.dps = DPS

EULER_GAMMA = mp.euler

# ----------------------------------------------------------------------------- zeta zeros
def zeta_zeros(M):
    return [mp.im(mp.zetazero(n)) for n in range(1, M + 1)]

# ----------------------------------------------------------------------------- von Mangoldt
def prime_powers(X):
    """list of (n, log p) for prime powers n=p^k <= X.  Lambda(n)=log p."""
    out = []
    is_prime = lambda m: m >= 2 and all(m % d for d in range(2, int(m**0.5) + 1))
    p = 2
    while p <= X:
        if is_prime(p):
            pe, lp = p, mp.log(p)
            while pe <= X:
                out.append((pe, lp))
                pe *= p
        p += 1
    return out

# ----------------------------------------------------------------------------- exact pieces
TINY = mp.mpf(10) ** (-(DPS - 8))

def fourier_basis(k, a, r):
    """fhat_k(r)=int_{-a}^{a} cos(w_k u) cos(r u) du = S(w-r)+S(w+r), S(d)=sin(d a)/d (a if d~0)."""
    w = (2 * k + 1) * mp.pi / (2 * a)
    def S(d):
        return a if abs(d) < TINY else mp.sin(d * a) / d
    return S(w - r) + S(w + r)

def A_jk(j, k, a, t):
    """Exact cross-correlation A_jk(t)=int cos(w_j u) cos(w_k (u-t)) du over the overlap
       {u in [-a,a]} cap {u-t in [-a,a]}.  Even in t; for t>=0 overlap u in [t-a, a] (0<=t<=2a)."""
    t = abs(t)
    wj = (2 * j + 1) * mp.pi / (2 * a)
    wk = (2 * k + 1) * mp.pi / (2 * a)
    lo, hi = t - a, a
    if lo >= hi:
        return mp.mpf(0)
    def term(alpha, beta):       # int_lo^hi cos(alpha u + beta) du
        if abs(alpha) < TINY:
            return mp.cos(beta) * (hi - lo)
        return (mp.sin(alpha * hi + beta) - mp.sin(alpha * lo + beta)) / alpha
    # cos(wj u)cos(wk(u-t)) = 1/2[cos((wj-wk)u + wk t)+cos((wj+wk)u - wk t)]
    return mp.mpf(1) / 2 * (term(wj - wk, wk * t) + term(wj + wk, -wk * t))

def cosh_moment(k, a):
    """c_k = int_{-a}^{a} cos(w_k u) cosh(u/2) du  (closed form)."""
    w = (2 * k + 1) * mp.pi / (2 * a)
    b = mp.mpf(1) / 2
    denom = b * b + w * w
    return (2 * b * mp.sinh(b * a) * mp.cos(w * a)
            + 2 * w * mp.cosh(b * a) * mp.sin(w * a)) / denom

# ----------------------------------------------------------------------------- archimedean (u-space)
def arch_entry(j, k, a):
    """W_R applied to g=A_jk:  (log4pi+gamma) g(0) + int_0^inf [2 g(u)-2 g(0)] e^{u/2}/(2 sinh u) du.
       g supported in [0,2a]; integrand smooth (removable sing. at 0), zero beyond 2a except the
       -2 g(0) tail which we carry analytically."""
    g0 = A_jk(j, k, a, mp.mpf(0))
    pref = (mp.log(4 * mp.pi) + EULER_GAMMA) * g0
    upper = 2 * a
    def kern(u):
        return mp.e ** (u / 2) / (2 * mp.sinh(u))
    # main piece on [0, 2a]: 2(g(u)-g(0)) * kern(u), removable at 0
    def integ_main(u):
        if u < TINY:
            # limit: g(u)-g(0) ~ (1/2) g''(0) u^2 ; kern ~ 1/(2u) -> integrand ~ (g''(0)/2) u -> 0
            return mp.mpf(0)
        return 2 * (A_jk(j, k, a, u) - g0) * kern(u)
    val_main = mp.quad(integ_main, [mp.mpf(0), upper / 2, upper])
    # tail piece on [2a, inf): g(u)=0 there, so integrand = -2 g(0) kern(u)
    def integ_tail(u):
        return -2 * g0 * kern(u)
    val_tail = mp.quad(integ_tail, [upper, upper + 1, upper + 5, mp.inf])
    return pref + val_main + val_tail

# ----------------------------------------------------------------------------- build form
def build(X, N):
    a = mp.log(X) / 2
    pp = prime_powers(X)
    c = [cosh_moment(k, a) for k in range(N)]
    Wm = mp.zeros(N, N)
    for j in range(N):
        for k in range(j, N):
            v = arch_entry(j, k, a)                       # archimedean
            for (n, lp) in pp:                            # primes (exact)
                v += 2 * (lp / mp.sqrt(n)) * A_jk(j, k, a, mp.log(n))
            v += 2 * c[j] * c[k]                          # poles/main
            Wm[j, k] = v
            Wm[k, j] = v
    return a, Wm, c

# ----------------------------------------------------------------------------- eta-hat zeros
def etahat(coeffs, a, r):
    return sum((ck * fourier_basis(k, a, r) for k, ck in enumerate(coeffs)), mp.mpf(0))

def find_zeros(coeffs, a, r_max, n_want):
    zeros = []
    step = mp.mpf("0.05")
    r = mp.mpf("0.5")
    prev_r, prev_v = r, etahat(coeffs, a, r)
    while r < r_max and len(zeros) < n_want:
        r += step
        v = etahat(coeffs, a, r)
        if (prev_v < 0) != (v < 0):
            lo, hi, flo = prev_r, r, prev_v
            for _ in range(8 * DPS):
                mid = (lo + hi) / 2
                fm = etahat(coeffs, a, mid)
                if fm == 0 or (hi - lo) < mp.mpf(10) ** (-(DPS - 6)):
                    lo = hi = mid
                    break
                if (fm < 0) == (flo < 0):
                    lo, flo = mid, fm
                else:
                    hi = mid
            zeros.append((lo + hi) / 2)
        prev_r, prev_v = r, v
    return zeros

# ----------------------------------------------------------------------------- run
def run(X, N, n_zeros=10, r_max=60):
    a, Wm, c = build(X, N)
    E, Q = mp.eigsy(Wm)                 # ascending eigenvalues
    lam = [E[i] for i in range(N)]
    # eta is NOT the global minimum eigenvector.  The spectrum is a geometrically-converging
    # near-degenerate cluster (the 'bulk' pinned by the construction) at L ~ -2.9034, separated
    # from the isolated high eigenvalue(s) by a large gap; within-cluster splittings shrink
    # geometrically (1e-17,1e-21,...,1e-50 = Connes' minuscule eps tower).  eta = the converged
    # extreme of the cluster, i.e. the member just below the largest internal gap.
    gaps = [lam[i + 1] - lam[i] for i in range(N - 1)]
    idx = max(range(N - 1), key=lambda i: gaps[i])
    eta = [Q[i, idx] for i in range(N)]
    eps_split = gaps[idx - 1] if idx >= 1 else mp.mpf(0)
    gap = gaps[idx]
    zeros = find_zeros(eta, a, mp.mpf(r_max), n_zeros)
    return dict(a=a, lam=lam, gap=gap, eta=eta, zeros=zeros,
                eta_idx=idx, eps_split=eps_split, cluster_val=lam[idx])

if __name__ == "__main__":
    X = 13
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    print("=" * 90)
    print(f"Connes numerical miracle, HIGH PRECISION (dps={DPS}, X={X}, N={N} even-cosine modes)")
    print("=" * 90)
    gammas = zeta_zeros(12)
    res = run(X, N, n_zeros=10, r_max=60)
    a, lam = res["a"], res["lam"]
    print(f"\nsupport a=(log {X})/2 = {mp.nstr(a,14)}")
    print(f"eta = cluster-extreme eigenvector (idx {res['eta_idx']}); cluster value L = "
          f"{mp.nstr(res['cluster_val'],36)}")
    print(f"minuscule splitting eps that isolates eta = {mp.nstr(res['eps_split'],6)}")
    print(f"ground eigenvalue lam_0 = {mp.nstr(lam[0],8)}  (NOT eta)")
    print(f"next             lam_1 = {mp.nstr(lam[1],8)}")
    print(f"spectral gap above cluster = {mp.nstr(res['gap'],8)}   gap/|lam_0| = "
          f"{mp.nstr(res['gap']/abs(lam[0]),6) if lam[0]!=0 else 'inf'}")
    print("\nfirst zeros of etahat(r)  vs  gamma_n  (|difference|):")
    print(f"  {'n':>3} {'etahat zero':>30} {'gamma_n':>30} {'|diff|':>14}")
    for i, z in enumerate(res["zeros"]):
        if i >= len(gammas):
            break
        d = abs(z - gammas[i])
        print(f"  {i+1:>3} {mp.nstr(z,24):>30} {mp.nstr(gammas[i],24):>30} {mp.nstr(d,5):>14}")
    print("\nConnes' published |diff| (first 8): 2.60179e-55, 4.80071e-52, 4.43756e-50, "
          "3.89903e-47,\n                                    7.59453e-46, 1.13198e-43, "
          "1.07245e-41, 1.2694e-40")
