r"""
prolate_core.py -- high-precision prolate spheroidal functions of PW_lambda and the CCM prolate
ansatz k_lambda = E(h_lambda) in the CCM basis V_n.

PROLATES.  PW_lambda = -d/dx((lambda^2 - x^2) d/dx) + (2 pi lambda x)^2 on [-lambda, lambda] becomes, in
t = x/lambda, the classical L_c = -d/dt((1-t^2) d/dt) + c^2 t^2 with c = 2 pi lambda^2.  Expanding
psi_n = sum_i beta_i Pbar_{2i+p}(t) in normalized Legendre functions Pbar_k = sqrt(k+1/2) P_k (parity p)
gives Bouwkamp's symmetric tridiagonal matrix
    T[i,i]   = k(k+1) + c^2 (2k^2+2k-1)/((2k-1)(2k+3)),           k = 2i+p,
    T[i,i+1] = c^2 (k+1)(k+2) / ((2k+3) sqrt((2k+1)(2k+5))).
Eigenvalues are found by Sturm bisection and eigenvectors by inverse iteration (both O(K) per step),
at the working precision.  The normalization sum beta_i^2 = 1 is int_{-1}^{1} psi^2 = 1.

FOURIER EIGENVALUE.  With CCM's convention F(f)(y) = int f(x) e^{2 pi i x y} dx and h_n(x) = psi_n(x/lambda),
F(h_n 1_[-lambda,lambda]) = chi_n h_n on [-lambda, lambda], where chi_n = lambda mu_n and
int_{-1}^{1} e^{icts} psi_n(s) ds = mu_n psi_n(t).  At t = 0 this is chi_n = lambda sqrt2 beta_0/psi_n(0)
(real, sign i^n).  An independent check uses int e^{icts} P_k(s) ds = 2 i^k j_k(ct) at t != 0.
|chi_n| = sqrt(concentration eigenvalue);  1 - |chi_n| is the n-th compression defect.

ANSATZ.  h_lambda = h_4/I_4 - h_0/I_0 (I_n = int h_n), the vanishing-integral combination of [CCM, Sect. 7],
supported in [-lambda, lambda].  k_lambda(u) = u^{1/2} sum_{j: ju <= lambda} h_lambda(ju) on [1/lambda, lambda].
In x = log(lambda u) in [0, L], V_n = e^{2 pi i n x/L}/sqrt L, the substitution y = ju gives
    c_n = <V_n, k> = L^{-1/2} sum_{j=1}^{floor(lambda^2)} j^{-1/2} e^{-i w_n a_j} Phi(w_n; log(j/lambda)),
    Phi(w; v0) = int_{v0}^{log lambda} h(e^v) e^{v/2} e^{-i w v} dv,   a_j = log(lambda/j),  w_n = 2 pi n/L,
so h is sampled once on [1/lambda, lambda] and Phi(w; .) are suffix sums of segment integrals.
The segment integrals use Gauss-Legendre on pieces of width <= dv_max; the inner loops (Legendre
recurrence, Fourier accumulation) run in fixed-point integer arithmetic with guard bits.
"""
import mpmath as mp
from mpmath import libmp


# ----------------------------------------------------------------------------- Bouwkamp tridiagonal
def bouwkamp(c, K, parity=0):
    """diagonal d (K) and off-diagonal e (K-1) of L_c in the basis Pbar_{2i+parity}."""
    c2 = c * c
    d, e = [], []
    for i in range(K):
        k = 2 * i + parity
        d.append(k * (k + 1) + c2 * mp.mpf(2 * k * k + 2 * k - 1) / ((2 * k - 1) * (2 * k + 3)))
        if i + 1 < K:
            e.append(c2 * mp.mpf((k + 1) * (k + 2)) / ((2 * k + 3) * mp.sqrt(mp.mpf((2 * k + 1) * (2 * k + 5)))))
    return d, e


def _sturm(d, e2, x):
    """number of eigenvalues < x."""
    cnt = 0
    q = d[0] - x
    if q < 0:
        cnt += 1
    tiny = mp.mpf(2) ** (-(mp.mp.prec + 20))
    for i in range(1, len(d)):
        if q == 0:
            q = tiny
        q = d[i] - x - e2[i - 1] / q
        if q < 0:
            cnt += 1
    return cnt


def eigval(d, e, j):
    """j-th smallest eigenvalue (0-based) by bisection to full working precision."""
    n = len(d)
    e2 = [v * v for v in e]
    rad = [(abs(e[i - 1]) if i > 0 else 0) + (abs(e[i]) if i < n - 1 else 0) for i in range(n)]
    lo = min(d[i] - rad[i] for i in range(n)) - 1
    hi = max(d[i] + rad[i] for i in range(n)) + 1
    tol = mp.mpf(2) ** (-(mp.mp.prec - 4))
    while hi - lo > tol * (abs(lo) + abs(hi)):
        mid = (lo + hi) / 2
        if _sturm(d, e2, mid) > j:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def inverse_iteration(d, e, theta, iters=3):
    """unit eigenvector for the eigenvalue theta (Thomas solves of (T - sigma) y = x)."""
    n = len(d)
    sigma = theta + (abs(theta) + 1) * mp.mpf(2) ** (-(mp.mp.prec - 40))
    x = [mp.mpf(1) / mp.sqrt(n)] * n
    for _ in range(iters):
        cp = [mp.mpf(0)] * n
        dp = [mp.mpf(0)] * n
        a0 = d[0] - sigma
        cp[0] = e[0] / a0 if n > 1 else mp.mpf(0)
        dp[0] = x[0] / a0
        for i in range(1, n):
            m = d[i] - sigma - e[i - 1] * cp[i - 1]
            if i < n - 1:
                cp[i] = e[i] / m
            dp[i] = (x[i] - e[i - 1] * dp[i - 1]) / m
        y = [mp.mpf(0)] * n
        y[n - 1] = dp[n - 1]
        for i in range(n - 2, -1, -1):
            y[i] = dp[i] - cp[i] * y[i + 1]
        nrm = mp.sqrt(mp.fsum(v * v for v in y))
        x = [v / nrm for v in y]
    return x


def residual(d, e, theta, v):
    n = len(d)
    r = []
    for i in range(n):
        s = (d[i] - theta) * v[i]
        if i > 0:
            s += e[i - 1] * v[i - 1]
        if i < n - 1:
            s += e[i] * v[i + 1]
        r.append(s)
    return mp.sqrt(mp.fsum(s * s for s in r))


def choose_K(c):
    """Legendre truncation: Bouwkamp coefficients decay super-exponentially once 2i >~ c."""
    cf = float(c)
    return int(cf / 2 + 6 * cf ** 0.5 + 60)


class ProlateSet:
    """The prolates psi_n(t; c), n in `ns` (all of one parity), with eigenvalues and Fourier eigenvalues."""

    def __init__(self, lam, ns, K=None):
        self.lam = mp.mpf(lam)
        self.c = 2 * mp.pi * self.lam ** 2
        par = ns[0] % 2
        assert all(n % 2 == par for n in ns)
        self.parity = par
        self.K = K if K is not None else choose_K(self.c)
        d, e = bouwkamp(self.c, self.K, par)
        self.beta, self.theta, self.res = {}, {}, {}
        for n in ns:
            j = (n - par) // 2
            th = eigval(d, e, j)
            v = inverse_iteration(d, e, th)
            # fix sign: first coefficient positive
            if v[0] < 0:
                v = [-x for x in v]
            self.beta[n] = v
            self.theta[n] = th
            self.res[n] = residual(d, e, th, v)
        self.tail = {n: abs(self.beta[n][-1]) for n in ns}

    def psi0(self, n):
        """psi_n(0) (parity 0 only)."""
        b = self.beta[n]
        s = mp.mpf(0)
        p = mp.mpf(1)                                        # P_{2i}(0) = (-1)^i binom(2i,i)/4^i
        for i in range(self.K):
            if i > 0:
                p = -p * (2 * i - 1) / (2 * i)
            s += b[i] * mp.sqrt(2 * i + mp.mpf(1) / 2) * p
        return s

    def chi(self, n):
        """signed chi_n = lambda mu_n from t = 0 (parity 0)."""
        return self.lam * mp.sqrt(2) * self.beta[n][0] / self.psi0(n)

    def chi_bessel(self, n, t=mp.mpf(1) / 2):
        """independent chi_n from int e^{icts} psi(s) ds = mu psi(t) at t != 0 (spherical Bessel)."""
        b = self.beta[n]
        x = self.c * t
        lhs = mp.mpf(0)
        for i in range(self.K):
            k = 2 * i + self.parity
            jk = mp.sqrt(mp.pi / (2 * x)) * mp.besselj(k + mp.mpf(1) / 2, x)
            ik = (-1) ** i                                   # i^k for even k (parity 0)
            lhs += b[i] * mp.sqrt(k + mp.mpf(1) / 2) * 2 * ik * jk
        return self.lam * lhs / self.psi_at(n, t)

    def psi_at(self, n, t):
        return mp.fsum(b * pb for b, pb in zip(self.beta[n], pbar_even(t, self.K)))

    def integral(self, n):
        """int_{-1}^{1} psi_n = sqrt2 beta_0 (parity 0)."""
        return mp.sqrt(2) * self.beta[n][0]


def pbar_even(t, K):
    """[Pbar_0(t), Pbar_2(t), ..., Pbar_{2K-2}(t)]."""
    out = []
    p0, p1 = mp.mpf(1), t
    out.append(p0 * mp.sqrt(mp.mpf(1) / 2))
    for k in range(1, 2 * K - 1):
        p0, p1 = p1, ((2 * k + 1) * t * p1 - k * p0) / (k + 1)
        if (k + 1) % 2 == 0:
            out.append(p1 * mp.sqrt(k + 1 + mp.mpf(1) / 2))
    return out[:K]


def combo(P, terms):
    """Legendre coefficients of sum_n a_n psi_n / I_n (I_n = int psi_n), terms = [(n, a_n)]."""
    K = P.K
    out = [mp.mpf(0)] * K
    for n, a in terms:
        I = P.beta[n][0]                                     # proportional to the integral
        for i in range(K):
            out[i] += a * P.beta[n][i] / I
    return out


def value_at0(P, coeff):
    s = mp.mpf(0)
    p = mp.mpf(1)
    for i in range(P.K):
        if i > 0:
            p = -p * (2 * i - 1) / (2 * i)
        s += coeff[i] * mp.sqrt(2 * i + mp.mpf(1) / 2) * p
    return s


# ----------------------------------------------------------------------------- Gauss-Legendre nodes
_GL = {}


def gl_nodes(m):
    """Gauss-Legendre nodes/weights on [-1,1] at the working precision (Newton on P_m), cached."""
    key = (m, mp.mp.prec)
    if key in _GL:
        return _GL[key]
    xs, ws = [], []
    for i in range(1, m // 2 + 1):
        x = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (m + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), x
            for k in range(1, m):
                p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
            dp = m * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < mp.mpf(2) ** (-(mp.mp.prec + 8)):
                break
        p0, p1 = mp.mpf(1), x
        for k in range(1, m):
            p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = m * (x * p1 - p0) / (x * x - 1)
        w = 2 / ((1 - x * x) * dp * dp)
        xs += [x, -x]
        ws += [w, w]
    if m % 2 == 1:
        p0, p1 = mp.mpf(1), mp.mpf(0)
        for k in range(1, m):
            p0, p1 = p1, ((2 * k + 1) * 0 * p1 - k * p0) / (k + 1)
        dp = m * (0 - p0) / (-1)
        xs.append(mp.mpf(0))
        ws.append(2 / (dp * dp))
    _GL[key] = (xs, ws)
    return xs, ws


# ----------------------------------------------------------------------------- fixed-point helpers
def _fx(x, P):
    return libmp.to_fixed(mp.mpf(x)._mpf_, P)


def _mp(i, P):
    return mp.mpf(libmp.from_man_exp(i, -P))


def _legendre_fixed(tf, K, P):
    """fixed-point [Pbar_{2i}(t)] i<K (unnormalized P_{2i} times fixed sqrt factors applied later)."""
    out = [0] * K
    one = 1 << P
    p0, p1 = one, tf
    out[0] = p0
    idx = 1
    for k in range(1, 2 * K - 1):
        p2 = ((2 * k + 1) * ((tf * p1) >> P) - k * p0) // (k + 1)
        p0, p1 = p1, p2
        if (k + 1) % 2 == 0:
            out[idx] = p1
            idx += 1
            if idx == K:
                break
    return out


# ----------------------------------------------------------------------------- the E-map coefficients
def ansatz_coeffs(lam, P_set, coeff_list, M, dv_max=mp.mpf("0.08"), m_gl=192, guard=48):
    """For each Legendre coefficient vector in coeff_list (functions h(y) = sum b_i Pbar_{2i}(y/lam) on
    [0, lam]), return the complex V_n-coordinates c_n, n = 0..M, of k = E(h) on [1/lam, lam].
    Returns list (one per coeff vector) of lists of mpc."""
    lam = mp.mpf(lam)
    L = 2 * mp.log(lam)
    K = P_set.K
    J = int(mp.floor(lam * lam + mp.mpf("1e-30")))
    Pbits = mp.mp.prec + guard
    # breakpoints in v = log y, y in [1/lam, lam]
    bps = sorted(set([mp.log(mp.mpf(j) / lam) for j in range(1, J + 1)] + [mp.log(lam)]))
    pieces = []
    for a, b in zip(bps[:-1], bps[1:]):
        if b - a <= 0:
            continue
        nsub = int(mp.ceil((b - a) / dv_max))
        for s in range(nsub):
            pieces.append((a + (b - a) * s / nsub, a + (b - a) * (s + 1) / nsub))
    xs, ws = gl_nodes(m_gl)
    sq = [mp.sqrt(2 * i + mp.mpf(1) / 2) for i in range(K)]
    cf = [[_fx(b * s, Pbits) for b, s in zip(co, sq)] for co in coeff_list]   # fixed coeffs incl. sqrt
    ncf = len(coeff_list)
    two_pi_over_L = 2 * mp.pi / L
    # segment integrals I[piece][cell][n] (complex as (re, im) fixed ints)
    seg = []
    for (a, b) in pieces:
        half = (b - a) / 2
        mid = (a + b) / 2
        acc = [[[0] * (M + 1), [0] * (M + 1)] for _ in range(ncf)]
        for xg, wg in zip(xs, ws):
            v = mid + half * xg
            y = mp.exp(v)
            t = y / lam
            tf = _fx(t, Pbits)
            leg = _legendre_fixed(tf, K, Pbits)
            wfac = wg * half * mp.exp(v / 2)                 # weight * e^{v/2}
            wfx = _fx(wfac, Pbits)
            ph = two_pi_over_L * v
            zr = _fx(mp.cos(ph), Pbits)
            zi = -_fx(mp.sin(ph), Pbits)                     # e^{-i (2pi/L) v}
            for ci in range(ncf):
                co = cf[ci]
                hv = 0
                for i in range(K):
                    hv += co[i] * leg[i]
                hv >>= Pbits                                 # h(y) in fixed point
                pr = (hv * wfx) >> Pbits
                pi_ = 0
                ar, ai = acc[ci]
                for n in range(M + 1):
                    ar[n] += pr
                    ai[n] += pi_
                    pr, pi_ = (pr * zr - pi_ * zi) >> Pbits, (pr * zi + pi_ * zr) >> Pbits
        seg.append((a, acc))
    # suffix sums: Phi(w_n; v_j) = sum over pieces with left end >= v_j
    out = []
    for ci in range(ncf):
        cn = [mp.mpc(0) for _ in range(M + 1)]
        for j in range(1, J + 1):
            vj = mp.log(mp.mpf(j) / lam)
            sr = [0] * (M + 1)
            si = [0] * (M + 1)
            for (a, acc) in seg:
                if a >= vj - mp.mpf(10) ** (-(mp.mp.dps // 2)):
                    ar, ai = acc[ci]
                    for n in range(M + 1):
                        sr[n] += ar[n]
                        si[n] += ai[n]
            aj = mp.log(lam / j)
            fac = 1 / mp.sqrt(mp.mpf(j) * L)
            for n in range(M + 1):
                ph = -two_pi_over_L * n * aj
                e = mp.mpc(mp.cos(ph), mp.sin(ph))
                cn[n] += fac * e * mp.mpc(_mp(sr[n], Pbits), _mp(si[n], Pbits))
        out.append(cn)
    return out


def k_direct(lam, P_set, coeff, x):
    """direct k(x) = lam^{-1/2} e^{x/2} sum_{j: j e^x <= lam^2} h(j e^x/lam) (for spot checks)."""
    lam = mp.mpf(lam)
    u = mp.exp(x) / lam
    s = mp.mpf(0)
    j = 1
    while j * u <= lam:
        t = j * u / lam
        s += mp.fsum(b * pb for b, pb in zip(coeff, pbar_even(t, P_set.K)))
        j += 1
    return mp.sqrt(u) * s


def even_vec(cn, N):
    """even-sector coordinates (e_0 = V_0, e_k = (V_k+V_-k)/sqrt2) of the iota-even part."""
    return [mp.re(cn[0])] + [mp.sqrt(2) * mp.re(cn[k]) for k in range(1, N + 1)]


def odd_vec(cn, N):
    """odd-sector coordinates (o_k = (V_k-V_-k)/sqrt2, real form) of the iota-odd part."""
    return [mp.sqrt(2) * mp.im(cn[k]) for k in range(1, N + 1)]
