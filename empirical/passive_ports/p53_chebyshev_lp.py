"""The optimal factorial auxiliary at complexity K, and its dual (Paper 53 §4.12), certificate K10.

Primal (prime-free).  Coefficients c_1..c_K (real), step function G_c(j) = sum_k c_k (floor(j/k) - floor(j/2k)).
    minimize   H_x(c) = sum_k c_k [log floor(x/k)! - log floor(x/2k)!]
    subject to G_c(1) >= 1,  G_c(j) >= 0 for j in J(x) minus {1},   J(x) = { floor(x/n) : 2 <= n <= x }.
Since floor(y/k) = floor(floor(y)/k), the valuation identity v_p = sum_r G_c(floor(x/p^r)) only ever reads G_c on J(x);
so these |J| ~ 2 sqrt(x) inequalities are sufficient (Astro's note imposes all 2 <= j <= x/2: a subset of our feasible set
is theirs, so our optimum is <= theirs).  Lambda >= 0 then gives  psi(x) - psi(x/2) <= H_x(c)  for every feasible c.
Dual.  z_j >= 0 on J with  sum_j z_j (floor(j/k) - floor(j/2k)) = F(floor(x/k)) for k <= K  ("fake prime masses" that
reproduce the first K factorial identities);  maximize z_1.  The true primes, z_j = psi(x/j) - psi(x/(j+1)), are feasible.
"""
import math
import sys
import time
import numpy as np
from scipy.optimize import linprog


def J_of(x):
    s = math.isqrt(x)
    small = set(range(1, s + 1))
    big = {x // n for n in range(2, s + 2)}
    return np.array(sorted(j for j in small | big if 1 <= j <= x // 2), dtype=np.int64)


def F(j):
    return math.lgamma(j + 1) - math.lgamma(j // 2 + 1)


def solve(x, K, J=None):
    J = J_of(x) if J is None else J
    ks = np.arange(1, K + 1, dtype=np.int64)
    A = J[:, None] // ks[None, :] - J[:, None] // (2 * ks[None, :])
    b = (J == 1).astype(float)
    cost = np.array([F(x // k) for k in ks])
    res = linprog(cost, A_ub=-A.astype(float), b_ub=-b, bounds=[(None, None)] * K, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    z = -res.ineqlin.marginals          # dual: fake prime masses on J
    return res.fun, res.x, z, J, A


def psi_table(N):
    lam = np.zeros(N + 1)
    sieve = np.ones(N + 1, bool); sieve[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    for p in np.nonzero(sieve)[0]:
        pk = int(p)
        while pk <= N:
            lam[pk] = math.log(p); pk *= int(p)
    return np.cumsum(lam), sieve


def mobius(N):
    mu = np.ones(N + 1, dtype=np.int64); mu[0] = 0
    is_p = np.ones(N + 1, bool); is_p[:2] = False
    for p in range(2, N + 1):
        if is_p[p]:
            is_p[p * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    return mu


if __name__ == "__main__":
    XMAX = 10**7
    psi, _ = psi_table(XMAX)
    mu = mobius(20000)
    print("(i) Astro's three points, re-solved on the sufficient constraint set J(x) (|J| ~ 2 sqrt x)")
    for x in (1000, 4000, 10000):
        K = math.isqrt(x) + (math.isqrt(x)**2 < x)
        H, c, z, J, A = solve(x, K)
        win = psi[x] - psi[x // 2]
        print(f"  x={x:6d} K={K:4d} |J|={len(J):5d}  H*={H:12.4f}  H*-x/2={H - x/2:9.3f}  H*-window={H - win:9.3f}"
              f"  (Astro, all j<=x/2: 573.19 / 2209.39 / 5494.47)")
    print("\n(ii) the complexity curve: H*(x,K) - x/2 and H*(x,K) - window, K from sqrt(x)/4 to past sqrt(x)")
    for x in (10**4, 10**5, 10**6):
        win = psi[x] - psi[x // 2]
        s = math.isqrt(x)
        J = J_of(x)
        print(f"  x = {x}: window psi(x)-psi(x/2) = {win:.3f}, x/2 = {x/2:.0f}, sqrt x = {s}")
        for K in sorted({max(2, s // 4), s // 2, s, 2 * s, 4 * s, 8 * s}):
            if K > x // 2:
                continue
            t0 = time.time()
            H, c, z, _, _ = solve(x, K, J)
            print(f"    K={K:6d}  H*-x/2={H - x/2:12.3f}  H*-window={H - win:12.3f}  (H*-x/2)/sqrt x={(H - x/2)/s:8.3f}"
                  f"  x/K={x/K:10.1f}  x/sqrt K={x/math.sqrt(K):10.1f}  [{time.time()-t0:.1f}s]", flush=True)
    print("\n(iii) the optimal coefficients rediscover the parity function: agreement of c*_k with mu(k)")
    for x in (10**4, 10**5, 10**6):
        s = math.isqrt(x)
        H, c, z, J, A = solve(x, s)
        cr = np.round(c).astype(int)
        agree = np.nonzero(cr != mu[1:s + 1])[0]
        first = int(agree[0]) + 1 if len(agree) else None
        frac = 1 - len(agree) / s
        print(f"  x={x:8d} K={s}: c* integral to 1e-9: {np.max(np.abs(c - cr)) < 1e-9};  c*_k = mu(k) for k < {first};"
              f"  agreement {frac:.3f};  first 24: {list(cr[:24])}")
    sys.stdout.flush()
