"""The construction under RH alone: the Mobius vector, averaged over x (Paper 53 §4.14), certificate K12.

Theorem 4.20 (claim):  RH  <=>  sum_{X<x<=2X} (E*(x) - x/2) << X^{3/2+eps}.
  (<=) E*(x) >= psi(x)-psi(x/2), dyadic summation, Landau on the integrated psi.
  (=>) E*(x) <= E(mu)(x) <= psi(x)-psi(x/2) + V_w(x)  (Theorem 4.18);  von Koch for the window;  and Lemma 4.21:
       on RH,  int_Y^{2Y} |M(y(1+1/T)) - M(y)|^2 dy << (Y^2/T) Y^eps   (square-root cancellation of mu in short
       intervals, in mean square), which averages the hyperbola variation V(x) to X^{1/2+eps}.
Measured here:
  (i)  the mean square of Mobius on relative-length 1/T intervals against the random model (6/pi^2) Y^2/T;
  (ii) the x-average of E(mu)(x) - x/2 and of V(x) on (X, 2X], and the pointwise spread.
"""
import math
import numpy as np
from p53_apriori_lp import S, b


def tables(N):
    mu = np.ones(N + 1, dtype=np.int8); mu[0] = 0
    lam = np.zeros(N + 1)
    isp = np.ones(N + 1, bool); isp[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if isp[p]:
            isp[p * p::p] = False
    for p in np.nonzero(isp)[0]:
        p = int(p)
        mu[p::p] *= -1
        if p * p <= N:
            mu[p * p::p * p] = 0
        pk = p
        while pk <= N:
            lam[pk] = math.log(p); pk *= p
    return np.cumsum(mu, dtype=np.int64), np.cumsum(lam)


def mobius_height(x, M, psi):
    """E(mu)(x), V(x), V_w(x): singletons k <= sqrt x, cells (x/(m+1), x/m] for k > sqrt x."""
    s = math.isqrt(x)
    k = np.arange(1, s + 1)
    ck = (M[k] - M[k - 1]).astype(float)                 # mu(k)
    y = x / k
    Sy = np.array([S(v) for v in y]); By = np.array([b(v) for v in y])
    E = float(np.sum(np.where(ck > 0, ck * (Sy + By), ck * (Sy - By))))
    V = float(np.sum(np.abs(ck))); Vw = float(np.sum(np.abs(ck) * 2 * By))
    for m in range(1, x // (s + 1) + 1):
        kmax = x // m
        kmin = max(x // (m + 1) + 1, s + 1)
        if kmin > kmax or kmax > x // 2:
            continue
        c = float(M[kmax] - M[kmin - 1])
        ylo, yhi = x / kmax, x / kmin
        up, dn = S(ylo) + b(ylo), S(yhi) - b(yhi)
        E += c * up if c > 0 else c * dn
        V += abs(c); Vw += abs(c) * (up - dn)
    win = psi[x] - psi[x // 2]
    return E, V, Vw, win


if __name__ == "__main__":
    NMAX = 2 * 10**7 + 10
    M, psi = tables(NMAX)
    print("(i) Lemma 4.21, mean square of Mobius on relative-length 1/T intervals: "
          "(1/Y) sum_{Y<y<=2Y} |M(y(1+1/T)) - M(y)|^2  /  (Y/T)   (random model: 6/pi^2 = 0.608)")
    for Y in (10**5, 10**6, 10**7):
        ys = np.arange(Y + 1, 2 * Y + 1)
        row = []
        for T in (2, 5, 10, 30, 100, 300, 1000, 3000):
            if T > Y // 10 or int(2 * Y * (1 + 1 / T)) + 2 > NMAX:
                continue
            hi = np.floor(ys * (1 + 1 / T)).astype(np.int64)
            ms = np.mean((M[hi] - M[ys]).astype(float) ** 2)
            row.append(f"T={T}: {ms / (Y / T):.3f}")
        print(f"   Y = {Y:.0e}:  " + ";  ".join(row))
    print("\n(ii) the Mobius construction averaged over x in (X, 2X] (400 random x per X)")
    rng = np.random.default_rng(20261011)
    for X in (10**4, 10**5, 10**6, 10**7):
        xs = rng.integers(X + 1, 2 * X + 1, size=400)
        ex, vv, ww, wn = [], [], [], []
        for x in xs:
            E, V, Vw, win = mobius_height(int(x), M, psi)
            ex.append((E - x / 2) / (math.sqrt(x) * math.log(x))); vv.append(V / (math.sqrt(x) * math.log(x)))
            ww.append((win - x / 2) / (math.sqrt(x) * math.log(x)))
        ex, vv, ww = map(np.array, (ex, vv, ww))
        print(f"   X = {X:.0e}: mean (E(mu)-x/2)/(sqrt x log x) = {ex.mean():.3f} (min {ex.min():.3f}, max {ex.max():.3f});"
              f"  mean V/(sqrt x log x) = {vv.mean():.3f} (max {vv.max():.3f});"
              f"  mean (window-x/2)/(sqrt x log x) = {ww.mean():+.4f}", flush=True)
