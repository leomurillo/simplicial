"""The arithmetic Frobenius: what Stepanov's auxiliary object costs over Z (Paper 53 §4.11), certificate K9.

Auxiliary object (Chebyshev's factorials with Mobius exponents, complexity K):
    N_K(x) = prod_{k<=K} ( floor(x/k)! / floor(x/2k)! )^{mu(k)},     log N_K = sum_{k<=K} mu(k) [T(x/k) - T(x/2k)],
    T(y) = log floor(y)!  (sizes known from Stirling: the archimedean Riemann–Roch, no primes needed).
Valuations: v_p = 1 at every prime power in (x/2, x], 0 at every prime power in (x/(K+1), x/2]; the only
'spurious zeros' are at prime powers n <= x/(K+1), where v = nu_K(x/n) - nu_K(x/2n), nu_K(y) = sum_{k<=K} mu(k) floor(y/k).
Hence  log N_K = [psi(x) - psi(x/2)] + spurious(K),  and for K >= x the object is exact: N_x(x) = exp(psi(x) - psi(x/2)).
Measured: how fast spurious(K) -> 0 with the complexity K, against Stepanov's q/K law and the sqrt(x) target.
"""
import math
import numpy as np


def mobius_vm(N):
    mu = np.ones(N + 1, dtype=np.int64); mu[0] = 0
    lam = np.zeros(N + 1)
    is_p = np.ones(N + 1, bool); is_p[:2] = False
    for p in range(2, N + 1):
        if is_p[p]:
            is_p[p * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
            pk = p
            while pk <= N:
                lam[pk] = math.log(p); pk *= p
    return mu, lam


def T(y):
    return math.lgamma(math.floor(y) + 1)


if __name__ == "__main__":
    XMAX = 4 * 10**6
    mu, lam = mobius_vm(XMAX)
    psi = np.cumsum(lam)
    for x in (10**5, 10**6, 4 * 10**6):
        window = psi[x] - psi[x // 2]
        terms = [int(mu[k]) * (T(x / k) - T(x / (2 * k))) for k in range(1, x + 1) if mu[k] != 0]
        exact = math.fsum(terms)
        print(f"x = {x}: psi(x)-psi(x/2) = {window:.6f};  Mobius-Chebyshev identity (K = x) gives {exact:.6f};"
              f"  |diff| = {abs(exact - window):.2e}")
        print(f"   target sqrt(x) log^2 x = {math.sqrt(x) * math.log(x)**2:.1f}")
        ks, spur = [], []
        running, k_done = 0.0, 0
        for K in (1, 3, 10, 30, 100, 300, 1000, 3000, 10**4, 3 * 10**4, 10**5, 3 * 10**5, 10**6, 4 * 10**6):
            if K > x:
                break
            running += math.fsum(int(mu[k]) * (T(x / k) - T(x / (2 * k))) for k in range(k_done + 1, K + 1) if mu[k] != 0)
            k_done = K
            s = running - window
            mK = float(np.sum(mu[1:K + 1] / np.arange(1, K + 1)))
            ks.append(K); spur.append(s)
            print(f"   K = {K:>8}: spurious(K) = {s:+14.2f}   x/K = {x / K:12.1f}   x/sqrt(K) = {x / math.sqrt(K):12.1f}"
                  f"   sum_(k<=K) mu(k)/k = {mK:+.2e}")
        sel = [(k, abs(v)) for k, v in zip(ks, spur) if 30 <= k <= x / 30 and abs(v) > 0]
        if len(sel) >= 3:
            a, b = np.polyfit(np.log([k for k, _ in sel]), np.log([v for _, v in sel]), 1)
            print(f"   fit |spurious(K)| ~ K^{a:.3f} over 30 <= K <= x/30  (Stepanov over F_q: K^-1)")
    # the parity pair (char-one standard form): M(x) = E(x) - O(x), slope of log|M| against log x
    M = np.cumsum(mu)
    print("\nparity pair (even vs odd squarefree counts): M(x)/sqrt(x) and max over [1, x]")
    for x in (10**3, 10**4, 10**5, 10**6, 4 * 10**6):
        print(f"   x = {x:>8}: M(x) = {int(M[x]):+6d}   M(x)/sqrt(x) = {M[x] / math.sqrt(x):+.3f}"
              f"   max_(1000<=y<=x) |M(y)|/sqrt(y) = {np.max(np.abs(M[1000:x + 1]) / np.sqrt(np.arange(1000, x + 1))):.3f}")
