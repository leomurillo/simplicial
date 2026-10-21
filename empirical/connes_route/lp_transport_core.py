r"""
lp_transport_core.py -- shared exact machinery for the Laguerre-Polya transport probes.

Builds the semilocal Weil quadratic form QW_lambda in the CCM basis
    V_n(u) = U_n(log(lambda u)),  U_n(x) = e^{2 pi i n x / L} / sqrt(L)  on [0, L],  L = 2 log lambda
(Connes-Consani-Moscovici, arXiv:2511.22755, Prop. toadd + Lemma polarize0 + Lemma wsharp),
for three self-dual L-data:

  kind = 'zeta'    : zeta(s), gamma factor Gamma_R(s), conductor 1, poles at s = 0, 1, Euler product.
  kind = 'dh'      : the Davenport-Heilbronn function f(s) = sum a_n n^{-s}, a = (0,1,k,-k,-1) mod 5,
                     k = (sqrt(10-2 sqrt5)-2)/(sqrt5-1); gamma factor Gamma_R(s+1), conductor 5,
                     entire, NO Euler product, zeros off the critical line (first: 0.8085+85.699i).
  kind = 'epstein' : the Epstein zeta of Q = x^2+5y^2 (disc -20, class number 2),
                     zeta_Q(s) = (1/2) sum'_{(x,y)} Q(x,y)^{-s} = sum_n a_n n^{-s}, a_n = r_Q(n)/2,
                              = (1/2)[zeta(s) L(s,chi_-20) + L(s,chi_-4) L(s,chi_5)]   (genus theory);
                     DEGREE 2: Lambda(s) = (sqrt20/2pi)^s Gamma(s) zeta_Q(s) = Lambda(1-s), and
                     Gamma(s) = (2pi)^s/2 * Gamma_R(s) Gamma_R(s+1), so the archimedean kernel is the
                     SUM of the zeta (beta=+1/2) and DH (beta=-1/2) kernels, conductor 20 carried by
                     the second; simple poles at s = 0, 1 (residues -1/2, +1/2), NO Euler product,
                     zeros off the line (first: 0.93297+15.66825i).
  kind = 'dedekind': its Euler-product partner zeta_K = zeta L(chi_-20), K = Q(sqrt -5): the SAME
                     Gamma(s), conductor 20 and poles, Lambda_K(n) = Lambda(n)(1 + chi_-20(n)).

Every entry is in CLOSED FORM (digamma/trigamma + geometrically convergent tails + finite
prime sums); no quadrature.  The construction is validated against the quadrature-built matrix
of the CCM verification note (C:/Projects/Connes/probe_ccm_exact_matrix.py) in the probe.

Explicit formula used (q = g(y)+g(-y), the symmetrized autocorrelation, y >= 0):
  QW(f) = sum_rho h(gamma_rho)
        = [poles]  int_0^L q(y) 2cosh(y/2) dy                                  (zeta, epstein)
        - [arch]   sum over the archimedean components (beta, N) of
                   (gamma + log 4pi - log N + log tanh(L/2)) q(0)/2
                   + int_0^L [e^{beta y} q(y) - q(0)] / (2 sinh y) dy
                   components: zeta (+1/2, 1); dh (-1/2, 5); epstein (+1/2, 1) + (-1/2, 20)
        - [primes] sum_{n <= e^L} Lambda_f(n) n^{-1/2} q(log n).
The pole term sees only the ORDER of each pole (Lambda'/Lambda has residue -1 at a simple pole of
Lambda), not its residue, so it is the same for zeta_Q (residues -+1/2) as for zeta.
Matrix: QW[n,m] = (S_m - S_n)/(pi (n-m)) (n != m), QW[n,n] = D_|n|, with per-frequency scalars
S_k = A_k - B_k - P_k (sin parts) and D_k = Ad_k - WR_k - Pd_k (diagonal, q_d = 2(1-y/L)cos(w y)).
"""
import mpmath as mp


# ----------------------------------------------------------------------------- arithmetic data
def von_mangoldt(X):
    """dict n -> Lambda(n) for 2 <= n <= X (mp)."""
    X = int(X)
    lam = {}
    sieve = [True] * (X + 1)
    for p in range(2, X + 1):
        if sieve[p]:
            for m in range(p * p, X + 1, p):
                sieve[m] = False
            lp = mp.log(p)
            pe = p
            while pe <= X:
                lam[pe] = lp
                pe *= p
    return lam


def dh_kappa():
    s5 = mp.sqrt(5)
    return (mp.sqrt(10 - 2 * s5) - 2) / (s5 - 1)


def dh_coeff(n, kap):
    r = n % 5
    return [mp.mpf(0), mp.mpf(1), kap, -kap, mp.mpf(-1)][r]


def lambda_f_dh(X):
    """Lambda_f(n), 1 <= n <= X, from -f'/f = sum Lambda_f(n) n^{-s}:
       a_n log n = sum_{d | n} Lambda_f(d) a_{n/d},  a_1 = 1."""
    X = int(X)
    kap = dh_kappa()
    a = [mp.mpf(0)] + [dh_coeff(n, kap) for n in range(1, X + 1)]
    divs = [[] for _ in range(X + 1)]
    for d in range(1, X + 1):
        for m in range(2 * d, X + 1, d):
            divs[m].append(d)                      # proper divisors d < m
    Lf = [mp.mpf(0)] * (X + 1)
    for n in range(2, X + 1):
        acc = a[n] * mp.log(n)
        for d in divs[n]:
            if d >= 2:
                acc -= Lf[d] * a[n // d]
        Lf[n] = acc
    return {n: Lf[n] for n in range(2, X + 1) if Lf[n] != 0}


def epstein_coeffs(X):
    """a_n = r_Q(n)/2, 1 <= n <= X, Q = x^2+5y^2, by direct lattice count (exact integers; a[0] unused)."""
    X = int(X)
    r = [0] * (X + 1)
    xm = int(X ** 0.5) + 1
    ym = int((X / 5) ** 0.5) + 1
    for x in range(-xm, xm + 1):
        x2 = x * x
        if x2 > X:
            continue
        for y in range(-ym, ym + 1):
            n = x2 + 5 * y * y
            if 0 < n <= X:
                r[n] += 1
    assert all(v % 2 == 0 for v in r)
    return [v // 2 for v in r]


def epstein_genus_coeffs(X):
    """the same a_n from the genus decomposition: (1/2)[sum_{d|n} chi_-20(d) + sum_{d|n} chi_-4(d) chi_5(n/d)]."""
    chi4 = (0, 1, 0, -1)
    chi5 = (0, 1, -1, -1, 1)
    X = int(X)
    two_a = [0] * (X + 1)
    for d in range(1, X + 1):
        c20 = chi4[d % 4] * chi5[d % 5]
        c4 = chi4[d % 4]
        for m in range(d, X + 1, d):
            two_a[m] += c20 + c4 * chi5[(m // d) % 5]
    assert all(v % 2 == 0 for v in two_a[1:])
    return [v // 2 for v in two_a]


def lambda_f_epstein_exact(X):
    """Lambda_Q(n), 2 <= n <= X, EXACTLY as integer combinations of log p, from -zeta_Q'/zeta_Q:
       a_n log n = sum_{d | n} Lambda_Q(d) a_{n/d},  a_1 = 1.  Lambda_Q(n) lies in span_Z{log p : p | n}.
       Returns dict n -> {p: integer coefficient} for the n with Lambda_Q(n) != 0."""
    X = int(X)
    a = epstein_coeffs(X)
    spf = list(range(X + 1))                               # smallest prime factor sieve
    for p in range(2, int(X ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, X + 1, p):
                if spf[m] == m:
                    spf[m] = p

    def logvec(n):
        v = {}
        while n > 1:
            p = spf[n]
            v[p] = v.get(p, 0) + 1
            n //= p
        return v

    divs = [[] for _ in range(X + 1)]
    for d in range(2, X + 1):
        for m in range(2 * d, X + 1, d):
            divs[m].append(d)                              # proper divisors 2 <= d < m
    Lf = [None] * (X + 1)
    for n in range(2, X + 1):
        acc = {}
        if a[n]:
            for p, e in logvec(n).items():
                acc[p] = a[n] * e
        for d in divs[n]:
            am = a[n // d]
            if am and Lf[d]:
                for p, c in Lf[d].items():
                    acc[p] = acc.get(p, 0) - c * am
        Lf[n] = {p: c for p, c in acc.items() if c != 0}
    return {n: Lf[n] for n in range(2, X + 1) if Lf[n]}


def lambda_f_epstein(X):
    """Lambda_Q(n) (mp values) for the n <= X where it is nonzero."""
    out = {}
    logs = {}
    for n, vec in lambda_f_epstein_exact(X).items():
        tot = mp.mpf(0)
        for p, c in vec.items():
            if p not in logs:
                logs[p] = mp.log(p)
            tot += c * logs[p]
        out[n] = tot
    return out


def lambda_dedekind(X):
    """Lambda_K(n) = Lambda(n) (1 + chi_-20(n)) for zeta_K = zeta L(chi_-20), K = Q(sqrt -5)."""
    chi4 = (0, 1, 0, -1)
    chi5 = (0, 1, -1, -1, 1)
    out = {}
    for n, v in von_mangoldt(X).items():
        c = 1 + chi4[n % 4] * chi5[n % 5]
        if c:
            out[n] = c * v
    return out


def prime_data(lam_, kind):
    """list of (y_n = log n, c_n = Lambda_f(n)/sqrt n) for 2 <= n <= lambda^2."""
    L = 2 * mp.log(lam_)
    X = int(mp.floor(mp.exp(L) + mp.mpf("1e-20")))
    table = {"zeta": von_mangoldt, "dh": lambda_f_dh, "epstein": lambda_f_epstein,
             "dedekind": lambda_dedekind}[kind](X)
    out = []
    for n, v in sorted(table.items()):
        y = mp.log(n)
        if y <= L:
            out.append((y, v / mp.sqrt(n)))
    return out


# ----------------------------------------------------------------------------- closed forms
def _tail_B(w, L, beta, tol):
    """sum_j w e^{-b_j L}/(b_j^2 + w^2), b_j = 2j+1-beta (geometric)."""
    s = mp.mpf(0)
    j = 0
    while True:
        b = 2 * j + 1 - beta
        t = w * mp.exp(-b * L) / (b * b + w * w)
        s += t
        if abs(t) < tol and j > 2:
            break
        j += 1
    return s


def _tail_Bint(w, L, beta, tol):
    s = mp.mpf(0)
    j = 0
    while True:
        b = 2 * j + 1 - beta
        q = b * b + w * w
        e = mp.exp(-b * L)
        t = (-b * e / q
             - e * ((1 - b * L) * q - 2 * b * b) / (L * q * q)
             + mp.exp(-(2 * j + 1) * L) / (2 * j + 1))
        s += t
        if abs(t) < tol and j > 2:
            break
        j += 1
    return s


ARCH = {"zeta": ((1, 1),), "dh": ((-1, 5),), "epstein": ((1, 1), (-1, 20)),
        "dedekind": ((1, 1), (-1, 20))}                                       # (sign of beta, conductor)
POLES = ("zeta", "epstein", "dedekind")


def per_frequency(lam_, N, kind):
    """S_k (k=0..N, S_{-k} = -S_k) and D_k (k=0..N) in closed form."""
    L = 2 * mp.log(lam_)
    comps = []                                        # one per archimedean component (beta, a', const)
    for sgn, cond in ARCH[kind]:
        beta = sgn * mp.mpf(1) / 2
        ap = (1 - beta) / 2                           # a' = 1/4 (beta=+1/2), 3/4 (beta=-1/2)
        logN = mp.mpf(0) if cond == 1 else mp.log(cond)
        comps.append((beta, ap, mp.euler + mp.log(4 * mp.pi) - logN + mp.log(mp.tanh(L / 2))))
    tol = mp.mpf(10) ** (-(mp.mp.dps + 5))
    pdat = prime_data(lam_, kind)
    S, D = {}, {}
    psi_half = mp.digamma(mp.mpf(1) / 2)
    for k in range(0, N + 1):
        w = 2 * mp.pi * k / L
        c = w / 2
        # ---- sin parts
        if kind in POLES:
            A = w * (2 - 2 * mp.cosh(L / 2)) / (mp.mpf(1) / 4 + w * w)
        else:
            A = mp.mpf(0)
        B = mp.mpf(0)
        for beta, ap, _ in comps:
            z = ap + 1j * c
            B += mp.im(mp.digamma(z)) / 2 - _tail_B(w, L, beta, tol)
        P = mp.fsum(cn * mp.sin(w * y) for y, cn in pdat)
        S[k] = A - B - P
        # ---- diagonal
        if kind in POLES:
            Ad = mp.mpf(0)
            for a in (mp.mpf(1) / 2, -mp.mpf(1) / 2):
                q = a * a + w * w
                eaL = mp.exp(a * L)
                G = a * (eaL - 1) / q
                H = ((eaL - 1 + a * L * eaL) * q - 2 * a * a * (eaL - 1)) / (q * q)
                Ad += 2 * (G - H / L)
        else:
            Ad = mp.mpf(0)
        WR = mp.mpf(0)
        for beta, ap, const_WR in comps:
            z = ap + 1j * c
            Bint = (psi_half - mp.re(mp.digamma(z)) - mp.re(mp.psi(1, z)) / (2 * L)
                    + 2 * _tail_Bint(w, L, beta, tol))
            WR += const_WR + Bint
        Pd = mp.fsum(cn * 2 * (1 - y / L) * mp.cos(w * y) for y, cn in pdat)
        D[k] = Ad - WR - Pd
    return S, D, L


def sectors(lam_, N, kind):
    """Even (N+1)x(N+1) and odd NxN sector matrices of QW_lambda^N, plus (S, D, L)."""
    S, D, L = per_frequency(lam_, N, kind)
    Sf = lambda k: S[k] if k >= 0 else -S[-k]

    def QW(n, m):
        if n == m:
            return D[abs(n)]
        return (Sf(m) - Sf(n)) / (mp.pi * (n - m))

    Ev = mp.matrix(N + 1, N + 1)
    Od = mp.matrix(N, N)
    r2 = mp.sqrt(2)
    for k in range(N + 1):
        for l in range(k, N + 1):
            if k == 0 and l == 0:
                v = QW(0, 0)
            elif k == 0:
                v = r2 * QW(l, 0)
            else:
                v = QW(k, l) + QW(k, -l)
            Ev[k, l] = v
            Ev[l, k] = v
    for k in range(1, N + 1):
        for l in range(k, N + 1):
            v = QW(k, l) - QW(k, -l)
            Od[k - 1, l - 1] = v
            Od[l - 1, k - 1] = v
    return Ev, Od, S, D, L


def full_entry_check(lam_, N, kind):
    """Full QW matrix (for cross-validation)."""
    S, D, L = per_frequency(lam_, N, kind)
    Sf = lambda k: S[k] if k >= 0 else -S[-k]
    dim = 2 * N + 1
    M = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            M[i, j] = D[abs(n)] if n == m else (Sf(m) - Sf(n)) / (mp.pi * (n - m))
    return M, S, D, L


# ----------------------------------------------------------------------------- spectra
def low_eig(M, count=3):
    """All eigenpairs via mp.eigsy, sorted ascending; returns (vals, vecs-as-lists)."""
    E, Q = mp.eigsy(M)
    n = M.rows
    order = sorted(range(n), key=lambda i: E[i])
    vals = [E[i] for i in order]
    vecs = [[Q[r, i] for r in range(n)] for i in order[:count]]
    return vals, vecs


def even_coeffs(x):
    """even-sector coordinates x_0..x_N -> V-basis xi_0, xi_k (k>=1) = x_k/sqrt2, sign fixed xi_0>0."""
    xi = [x[0]] + [xk / mp.sqrt(2) for xk in x[1:]]
    if xi[0] < 0:
        xi = [-v for v in xi]
    return xi


# ----------------------------------------------------------------------------- the LP scalar and F
def S_of(xi, L):
    """S = -F''(0)/2 = L^2/24 + (L^2/(2 pi^2)) sum_{k>=1} xi_k/(k^2 xi_0)."""
    return L * L / 24 + L * L / (2 * mp.pi ** 2) * mp.fsum(xi[k] / (k * k) for k in range(1, len(xi))) / xi[0]


def F_of(xi, L, z):
    """F(z) = xihat(z)/xihat(0) = (sin pi s/(pi s)) [1 - (2 s^2/xi_0) sum_k xi_k/(k^2-s^2)],  s = zL/2pi."""
    s = z * L / (2 * mp.pi)
    if abs(s) < mp.mpf(10) ** (-(mp.mp.dps // 2)):
        return mp.mpf(1)
    # (callers keep s off the nonzero integers; the singularities there are removable)
    tot = mp.fsum(xi[k] / (k * k - s * s) for k in range(1, len(xi)))
    return mp.sin(mp.pi * s) / (mp.pi * s) * (1 - 2 * s * s / xi[0] * tot)


def rho_v(xi, v):
    """secular function in v = s^2: zeros of xihat <-> roots of xi_0/v - 2 sum_k xi_k/(k^2 - v)."""
    return xi[0] / v - 2 * mp.fsum(xi[k] / (k * k - v) for k in range(1, len(xi)))


def _bisect(fun, a, b, fa, iters):
    for _ in range(iters):
        m = (a + b) / 2
        fm = fun(m)
        if fm == 0:
            return m
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2


def real_zeros_v(xi, pts_per_interval=40, refine=True):
    """Count/locate the positive real roots v of rho_v (each gives a real zero pair z = +-2pi sqrt(v)/L).
       Poles at v = 0, 1, 4, ..., N^2; exactly N roots in total (degree count).  Must be run at the
       working precision of xi: the secular function at height t carries a relative size ~ e^{-pi t/4},
       so low precision manufactures spurious sign changes.  Each interval between poles is sampled
       uniformly plus geometrically close to both poles (offsets 10^-m), so roots hugging a pole are
       caught.  Returns the sorted list of roots found (bisection-refined)."""
    N = len(xi) - 1
    f = lambda vv: rho_v(xi, vv)
    ms = sorted(set([2, 3, 4, 6, 8, 11, 15, 20, 27, 36, 48, 64, 85, 110, 140, 180, 230]))
    ms = [m for m in ms if m < mp.mp.dps - 6]
    roots = []
    for k in range(0, N + 1):
        lo = mp.mpf(k * k)
        if k < N:
            hi = mp.mpf((k + 1) ** 2)
            width = hi - lo
            fr = sorted(set([mp.mpf(10) ** (-m) for m in ms]
                            + [mp.mpf(j) / pts_per_interval for j in range(1, pts_per_interval)]
                            + [1 - mp.mpf(10) ** (-m) for m in ms]))
            grid = [lo + width * g for g in fr]
        else:                                              # beyond the last pole: geometric to 1e4 N^2
            base = lo if N > 0 else mp.mpf(1)
            grid = [base * (1 + mp.mpf(10) ** (-m)) for m in reversed(ms)] + \
                   [base * (1 + mp.mpf(10) ** (mp.mpf(e) / 8)) for e in range(-8, 33)]
        vals = [f(g) for g in grid]
        for j in range(len(grid) - 1):
            if vals[j] == 0 or (vals[j] > 0) != (vals[j + 1] > 0):
                roots.append(_bisect(f, grid[j], grid[j + 1], vals[j], 90) if refine else (grid[j] + grid[j + 1]) / 2)
    return sorted(roots)


# ----------------------------------------------------------------------------- targets
def Xi_zeta(t):
    s = mp.mpf(1) / 2 + 1j * t
    return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s))


def f_dh(s):
    kap = dh_kappa()
    a = [None, mp.mpf(1), kap, -kap, mp.mpf(-1)]
    return mp.power(5, -s) * mp.fsum(a[r] * mp.zeta(s, mp.mpf(r) / 5) for r in range(1, 5))


def Lambda_dh(s):
    return mp.power(5 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * f_dh(s)


def Xi_dh(t):
    return mp.re(Lambda_dh(mp.mpf(1) / 2 + 1j * t))


CHI4 = [0, 1, 0, -1]
CHI5 = [0, 1, -1, -1, 1]
CHI20 = [CHI4[n % 4] * CHI5[n % 5] for n in range(20)]


def f_epstein(s):
    """zeta_Q(s), Q = x^2+5y^2, by the genus decomposition (1/2)[zeta L(chi_-20) + L(chi_-4) L(chi_5)]."""
    return (mp.zeta(s) * mp.dirichlet(s, CHI20) + mp.dirichlet(s, CHI4) * mp.dirichlet(s, CHI5)) / 2


def Lambda_epstein(s):
    return mp.power(mp.sqrt(20) / (2 * mp.pi), s) * mp.gamma(s) * f_epstein(s)


def Xi_epstein(t):
    """Xi_Q(t) = s(s-1) Lambda_Q(s) at s = 1/2+it (entire, even, real on R)."""
    s = mp.mpf(1) / 2 + 1j * t
    return mp.re(s * (s - 1) * Lambda_epstein(s))


def Xi_dedekind(t):
    """the Euler-product control with the same Gamma(s), conductor 20 and poles:
       zeta_K = zeta L(chi_-20), K = Q(sqrt -5);  Xi_K(t) = s(s-1)(sqrt20/2pi)^s Gamma(s) zeta_K(s)."""
    s = mp.mpf(1) / 2 + 1j * t
    return mp.re(s * (s - 1) * mp.power(mp.sqrt(20) / (2 * mp.pi), s) * mp.gamma(s)
                 * mp.zeta(s) * mp.dirichlet(s, CHI20))
