"""The uniform construction: the Mobius vector in hyperbola-grouped form (Paper 53 §4.12, Theorem 4.18), certificate K11.

For every x the full Mobius vector c_k = mu(k), k <= x/2, is feasible: G_mu(j) = [j = 1] for every j <= x/2
(two-window Mobius identity).  On J(x) the columns collapse to the groups m = floor(x/k), with group coefficient
    c_m = M(floor(x/m)) - M(floor(x/(m+1))),
and the a priori height (Stirling bracket at the group ends, as in p53_apriori_full.py) is
    E(mu) = sum_m [ c_m^+ (S+b)(y_m^-) + c_m^- (b-S)(y_m^+) ]  =  [psi(x) - psi(x/2)] + theta * V_w(x),  0 <= theta <= 1,
    V_w(x) = sum_m |c_m| w_m,   w_m = (S+b)(y_m^-) - (S-b)(y_m^+),
because sum_m c_m F(m) = sum_k mu(k) F(floor(x/k)) = psi(x) - psi(x/2) exactly.  Only M at ~2 sqrt(x) points is needed.
Segmented Mobius sieve to x/2 and segmented prime sieve on (x/2, x].  Usage: python p53_mobius_construction.py x1 x2 ...
"""
import math
import sys
import time
import numpy as np
from p53_apriori_lp import S, b, F
from p53_apriori_full import groups


def small_primes(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


def mertens_at(points, N, block=10**7):
    """M(y) for each y in points (all <= N), by a segmented Mobius sieve."""
    pts = np.array(sorted(set(int(p) for p in points if p >= 1)), dtype=np.int64)
    out = {}
    P = small_primes(math.isqrt(N) + 1)
    run = 0
    lo = 1
    pi = 0
    while lo <= N:
        hi = min(lo + block, N + 1)
        n = np.arange(lo, hi, dtype=np.int64)
        sign = np.ones(hi - lo, dtype=np.int8)
        rem = n.copy()
        for p in P:
            p = int(p)
            if p * p >= hi and p >= hi:
                break
            st = (-lo) % p
            if st >= hi - lo:
                continue
            sign[st::p] *= -1
            rem[st::p] //= p
            pp = p * p
            st2 = (-lo) % pp
            if st2 < hi - lo:
                sign[st2::pp] = 0
        sign[rem > 1] *= -1                       # one prime factor > sqrt(N) remains
        cs = np.cumsum(sign, dtype=np.int64) + run
        while pi < len(pts) and pts[pi] < hi:
            out[int(pts[pi])] = int(cs[pts[pi] - lo]); pi += 1
        run = int(cs[-1])
        lo = hi
    out[0] = 0
    return out


def window_psi(x, block=10**7):
    """psi(x) - psi(x/2) by a segmented prime sieve on (x/2, x] plus prime powers."""
    lo0 = x // 2 + 1
    P = small_primes(math.isqrt(x) + 1)
    tot = 0.0
    lo = lo0
    while lo <= x:
        hi = min(lo + block, x + 1)
        isp = np.ones(hi - lo, bool)
        for p in P:
            p = int(p)
            if p * p >= hi:
                break
            st = max(p * p, ((lo + p - 1) // p) * p) - lo
            isp[st::p] = False
        idx = np.nonzero(isp)[0] + lo
        tot += float(np.sum(np.log(idx.astype(float))))
        lo = hi
    for p in P:                                    # prime powers p^r, r >= 2, in (x/2, x]
        p = int(p); q = p * p
        while q <= x:
            if q > x // 2:
                tot += math.log(p)
            q *= p
    return tot


def mobius_construction(x):
    G = groups(x)
    pts = []
    for (m, kmax, ylo, yhi) in G:
        pts += [kmax, x // (m + 1)]
    M = mertens_at(pts, x // 2 + 1)
    E = V = 0.0
    l1 = 0
    for (m, kmax, ylo, yhi) in G:
        c = M[kmax] - M[x // (m + 1)]
        up, dn = S(ylo) + b(ylo), S(yhi) - b(yhi)
        E += c * up if c > 0 else c * dn
        V += abs(c) * (up - dn)
        l1 += abs(c)
    return E, V, l1, len(G)


if __name__ == "__main__":
    for x in [int(float(a)) for a in sys.argv[1:]]:
        t0 = time.time()
        E, V, l1, ng = mobius_construction(x)
        win = window_psi(x)
        s = math.sqrt(x); L = math.log(x)
        th = (E - win) / V if V else float("nan")
        print(f"x = {x:.1e}: groups {ng}:  E(mu) - x/2 = {E - x/2:12.1f} = {(E - x/2)/(s*L):6.3f} sqrt x log x"
              f" = {(E - x/2)/(s*L*L):6.4f} sqrt x log^2 x;  window - x/2 = {win - x/2:10.1f};  V_w = {V:12.1f}"
              f" = {V/(s*L*L):6.4f} sqrt x log^2 x;  theta = {th:.3f};  grouped l1 = {l1} = {l1/(s*L):.3f} sqrt x log x"
              f"   [{time.time()-t0:.0f}s]", flush=True)
