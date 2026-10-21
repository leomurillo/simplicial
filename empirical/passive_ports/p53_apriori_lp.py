"""A priori (Stepanov-type) degree bound for factorial auxiliaries (Paper 53 §4.12), certificate K10(c).

Exact LP (p53_chebyshev_lp.py) uses the exact log-factorials F(floor(x/k)); its optimum is the Legendre sieve.
A priori version: replace each F(floor(y)) by Stirling's main term S(y) = (y/2) log y + (y/2)(log 2 - 1) plus an
explicit error allowance b(y) >= |F(floor(y)) - S(y)| (checked below on y <= 10^7).  Then for every feasible c
    psi(x) - psi(x/2) <= H(c) <= sum_k c_k S(x/k) + sum_k |c_k| b(x/k) =: E(c),
and E(c) uses NO prime and NO exact factorial: (x/2)[C(1)(log x + log 2 - 1) + C'(1)] + an l1 penalty.
Minimizing E over feasible c (positivity on J) is the Stepanov-shaped problem: vanishing at the window by positivity,
degree bounded a priori.  Reported: E*(x,K) - x/2 against sqrt(x), and the exact-LP optimum's own a priori data.
"""
import math
import numpy as np
from scipy.optimize import linprog
from p53_chebyshev_lp import J_of, F, solve, psi_table


def S(y):
    return 0.5 * y * math.log(y) + 0.5 * y * (math.log(2) - 1)


def b(y):
    return 0.5 * math.log(y) + 1.0


def apriori(x, K, J):
    ks = np.arange(1, K + 1, dtype=np.int64)
    A = (J[:, None] // ks[None, :] - J[:, None] // (2 * ks[None, :])).astype(float)
    rhs = (J == 1).astype(float)
    s = np.array([S(x / k) for k in ks]); bb = np.array([b(x / k) for k in ks])
    cost = np.concatenate([s + bb, -s + bb])                 # c = cp - cm, cp, cm >= 0
    res = linprog(cost, A_ub=-np.hstack([A, -A]), b_ub=-rhs, bounds=[(0, None)] * (2 * K), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    c = res.x[:K] - res.x[K:]
    return res.fun, c


if __name__ == "__main__":

    # check the error allowance: |F(floor y) - S(y)| <= b(y) for y in [2, 1e7] (integers and midpoints, the extremes of the sawtooth)
    worst = 0.0
    for y in list(range(2, 200001)) + list(range(200001, 10**7, 997)):
        for yy in (float(y), y + 0.999999):
            worst = max(worst, abs(F(int(yy)) - S(yy)) - b(yy))
    print(f"error allowance: max_y (|F(floor y) - S(y)| - b(y)) = {worst:.4f}  (must be <= 0)")
    psi, _ = psi_table(10**6)
    for x in (10**4, 10**5, 10**6):
        J = J_of(x); s = math.isqrt(x)
        win = psi[x] - psi[x // 2]
        print(f"x = {x}: window - x/2 = {win - x/2:.2f}, sqrt x = {s}")
        for r in (0.25, 0.5, 1.0, 2.0, 3.0):
            K = max(2, int(r * s))
            if x >= 10**6 and r > 1.0:
                continue
            E, c = apriori(x, K, J)
            C1 = float(np.sum(c / np.arange(1, K + 1)))
            print(f"   K = {K:5d} ({r:4.2f} sqrt x): a priori E* - x/2 = {E - x/2:12.2f}  ({(E - x/2)/s:8.2f} sqrt x)"
                  f"   l1 = {np.sum(np.abs(c)):8.2f}   C(1) = {C1:+.2e}")
        if x <= 10**5:
            K = int(2.75 * s)
            H, c, z, _, _ = solve(x, K, J)
            ks = np.arange(1, K + 1)
            C1 = float(np.sum(c / ks)); dC = float(-np.sum(c * np.log(ks) / ks))
            main = 0.5 * x * (C1 * (math.log(x) + math.log(2) - 1) + dC)
            pen = float(np.sum(np.abs(c) * np.array([b(x / k) for k in ks])))
            print(f"   exact-LP optimum at K = {K}: H* - window = {H - win:.2e};  Stirling main - x/2 = {main - x/2:.2f};"
                  f"  l1 = {np.sum(np.abs(c)):.1f};  a priori penalty = {pen:.1f};  C(1) = {C1:+.3e}, C'(1)-1 = {dC - 1:+.3e}")
