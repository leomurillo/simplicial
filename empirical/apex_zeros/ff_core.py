"""
Finite-field / character machinery for the function-field apex lift (C9).

Over F_q (q prime here, N | q-1) we form the multiplicative-apex coefficients:
  * Gauss sum   g(chi)      = sum_{t in F_q^x} chi(t) psi(t),         |g| = sqrt q
  * Jacobi sum  J(chi^a,chi^b) = sum_{t != 0,1} chi^a(t) chi^b(1-t),  |J| = sqrt q
with chi a multiplicative character of order N (chi(g)=e^{2pi i/N} on a primitive
root g), psi(t)=e^{2pi i t/q} the additive character. The Jacobi sums are the
Frobenius eigenvalues on H^1 of the Fermat curve x^N+y^N+z^N=0; Weil's theorem
|alpha_i| = sqrt q is the curve RH, i.e. Re s = 1/2 under T = q^{-s}.

This module: primitive roots, discrete logs, Gauss/Jacobi sums (mpmath), and
brute projective point counts of the Fermat curve over F_q and F_{q^2}.
"""

import mpmath as mp

mp.mp.dps = 30


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d); n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def primitive_root(p):
    """Smallest primitive root mod p."""
    order = p - 1
    facs = prime_factors(order)
    for g in range(2, p):
        if all(pow(g, order // q, p) != 1 for q in facs):
            return g
    raise ValueError(f"no primitive root for {p}")


def dlog_table(p, g):
    """{t: k} with g^k = t (mod p), for t in 1..p-1."""
    tab, cur = {}, 1
    for k in range(p - 1):
        tab[cur] = k
        cur = (cur * g) % p
    return tab


# ---- characters & sums over F_p -------------------------------------------
def make_chars(p):
    g = primitive_root(p)
    dl = dlog_table(p, g)
    return g, dl


def gauss_sum(p, dl, N, a):
    """g(chi^a) = sum_{t=1}^{p-1} chi^a(t) psi(t),  chi^a(t)=e^{2pi i a*dlog(t)/N}."""
    s = mp.mpc(0)
    for t in range(1, p):
        s += mp.e ** (2j * mp.pi * (a * dl[t]) / N) * mp.e ** (2j * mp.pi * t / p)
    return s


def jacobi_sum(p, dl, N, a, b):
    """J(chi^a, chi^b) = sum_{t != 0,1} chi^a(t) chi^b(1-t)."""
    s = mp.mpc(0)
    for t in range(2, p):                       # t != 0 and t != 1
        u = (1 - t) % p                         # nonzero since t != 1
        s += (mp.e ** (2j * mp.pi * (a * dl[t]) / N)
              * mp.e ** (2j * mp.pi * (b * dl[u]) / N))
    return s


# ---- Fermat curve point counts --------------------------------------------
def fermat_count_Fp(p, N):
    """Projective points of x^N+y^N+z^N=0 over F_p."""
    powt = [pow(x, N, p) for x in range(p)]
    cnt = 0
    # chart z=1: x^N + y^N + 1 = 0
    for x in range(p):
        for y in range(p):
            if (powt[x] + powt[y] + 1) % p == 0:
                cnt += 1
    # chart z=0, y=1: x^N + 1 = 0   (point [1:0:0] has 1+0+0=1 != 0)
    for x in range(p):
        if (powt[x] + 1) % p == 0:
            cnt += 1
    return cnt


def _nonresidue(q):
    for n in range(2, q):
        if pow(n, (q - 1) // 2, q) == q - 1:
            return n
    raise ValueError("no nonresidue")


def fermat_count_Fq2(q, N):
    """Projective points over F_{q^2} = F_q[t]/(t^2 - nr), elements (a,b)=a+b t."""
    nr = _nonresidue(q)
    els = [(a, b) for a in range(q) for b in range(q)]

    def mul(u, v):
        a, b = u; c, d = v
        return ((a * c + b * d * nr) % q, (a * d + b * c) % q)

    def powN(u):
        r = (1, 0)
        for _ in range(N):
            r = mul(r, u)
        return r

    def add3(u, v, w):
        return ((u[0] + v[0] + w[0]) % q, (u[1] + v[1] + w[1]) % q)

    powtab = {u: powN(u) for u in els}
    one = (1, 0); zero = (0, 0)
    cnt = 0
    for x in els:
        xn = powtab[x]
        for y in els:
            if add3(xn, powtab[y], one) == zero:
                cnt += 1
    for x in els:                                # z=0, y=1
        if add3(powtab[x], one, zero) == zero:   # x^N + 1 = 0
            cnt += 1
    return cnt
