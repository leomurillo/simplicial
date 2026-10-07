"""
Minimal F_{p^d} arithmetic for higher-genus point counting (C10).

Polynomials over F_p as low-index-first coefficient lists. Field F_{p^d} =
F_p[x]/(f), f a monic irreducible of degree d. Elements are coeff-tuples of
length d. We only need: enumerate elements, 4th powers, and (-1). Point counts
use the fast frequency-convolution
    #{(x,y): x^4 + y^4 = c} = sum_u freq[u] * freq[c - u],  freq[u]=#{x: x^4=u},
so counting the Fermat quartic over F_{p^d} is O(p^d), not O(p^{2d}).
"""

from collections import Counter


# ---- polynomials over F_p (low index = low power) -------------------------
def _trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, p):
    n = max(len(a), len(b)); r = [0] * n
    for i in range(len(a)): r[i] = a[i]
    for i in range(len(b)): r[i] = (r[i] + b[i]) % p
    return _trim(r)


def pmul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
    return _trim(r)


def pmod(a, f, p):
    a = _trim(a[:]); df = len(f) - 1
    finv = pow(f[-1], p - 2, p)
    while len(a) - 1 >= df and any(a):
        d = len(a) - 1
        c = (a[-1] * finv) % p
        if c:
            for i in range(len(f)):
                a[d - df + i] = (a[d - df + i] - c * f[i]) % p
        a = _trim(a)
        if a == [0]:
            break
    return _trim(a)


def pmulmod(a, b, f, p):
    return pmod(pmul(a, b, p), f, p)


def ppowmod(a, n, f, p):
    r = [1]; base = pmod(a[:], f, p)
    while n > 0:
        if n & 1:
            r = pmulmod(r, base, f, p)
        base = pmulmod(base, base, f, p)
        n >>= 1
    return r


def pgcd(a, b, p):
    a = _trim(a[:]); b = _trim(b[:])
    while any(b):
        a, b = b, pmod(a, b, p)
    # normalise to monic
    inv = pow(a[-1], p - 2, p)
    return _trim([(c * inv) % p for c in a])


def _prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d); n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def is_irreducible(f, p):
    d = len(f) - 1
    x = [0, 1]
    if ppowmod(x, p ** d, f, p) != _trim(x[:]):              # x^{p^d} == x mod f
        return False
    for r in _prime_factors(d):
        g = pgcd(_sub(ppowmod(x, p ** (d // r), f, p), x, p), f, p)
        if len(g) - 1 != 0:                              # nontrivial common factor
            return False
    return True


def _sub(a, b, p):
    return padd(a, [(-c) % p for c in b], p)


def find_irreducible(p, d):
    # search monic f = x^d + c_{d-1} x^{d-1} + ... + c_0
    from itertools import product
    for tail in product(range(p), repeat=d):
        f = list(tail) + [1]
        if f[0] == 0:
            continue                                   # x | f -> reducible
        if is_irreducible(f, p):
            return f
    raise ValueError(f"no irreducible deg {d} over F_{p}")


# ---- F_{p^d} field & quartic point count ----------------------------------
class GFpk:
    def __init__(self, p, d):
        self.p, self.d = p, d
        if d == 1:
            self.f = None
            self.elements = [(i,) for i in range(p)]
        else:
            self.f = find_irreducible(p, d)
            from itertools import product
            self.elements = [tuple(c) for c in product(range(p), repeat=d)]
        self.zero = tuple([0] * d)
        self.one = tuple([1] + [0] * (d - 1))
        self.minus_one = tuple([(-1) % p] + [0] * (d - 1))

    def _mul(self, a, b):
        if self.d == 1:
            return ((a[0] * b[0]) % self.p,)
        r = pmulmod(list(a), list(b), self.f, self.p)
        r = r + [0] * (self.d - len(r))
        return tuple(r)

    def pow4(self, a):
        a2 = self._mul(a, a)
        return self._mul(a2, a2)

    def sub(self, a, b):
        return tuple((a[i] - b[i]) % self.p for i in range(self.d))


def fermat_quartic_count(p, d):
    """#C(F_{p^d}) for x^4 + y^4 + z^4 = 0, via frequency convolution."""
    F = GFpk(p, d)
    freq = Counter(F.pow4(e) for e in F.elements)
    m1 = F.minus_one
    # z=1 chart: x^4 + y^4 = -1
    s = 0
    for u, cu in freq.items():
        s += cu * freq.get(F.sub(m1, u), 0)
    # z=0, y=1 chart: x^4 = -1
    s += freq.get(m1, 0)
    return s
