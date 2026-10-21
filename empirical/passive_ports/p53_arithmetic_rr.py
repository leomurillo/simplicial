"""Arithmetic Riemann–Roch on the curve Spec Z-bar (Paper 53 §4.10), certificate K8.

Arakelov degree d in R  <->  the lattice Z with the metric |n| e^{-d}.  Sections: h0(d) = log sum_{n in Z} exp(-pi n^2 e^{-2d}).
    (i)   h0(d) >= 0 for every d (the zero section is always there);
    (ii)  Riemann–Roch  h0(d) - h0(-d) = d   (canonical degree 0; Jacobi theta inversion = Poisson summation);
    (iii) the completed zeta is the Mellin transform of the section count:
          xi(s) / (s(s-1)/2) = pi^{-s/2} Gamma(s/2) zeta(s) = int_0^inf (e^{h0(d)} - 1)/2 * e^{-2 d (s/2) ...}
          concretely  Lambda(s) = int_0^inf (theta(x) - 1)/2 x^{s/2} dx/x,  theta(x) = exp h0(-log(x)/2).
and the Frobenius at scale X (Stepanov's ingredient) is what the curve-level statement does NOT contain.
"""
import mpmath as mp

mp.mp.dps = 40
theta_direct = lambda x: mp.jtheta(3, 0, mp.exp(-mp.pi * x))   # the sum itself, no inversion used
# for the Mellin integral only (x -> 0), evaluate through the inversion theorem
theta = lambda x: theta_direct(x) if x >= 1 else theta_direct(1 / x) / mp.sqrt(x)
h0 = lambda d: mp.log(theta_direct(mp.exp(-2 * d)))

print("(i)-(ii) Riemann–Roch on Spec Z-bar: h0(d) >= 0 and h0(d) - h0(-d) - d")
for d in (-3, -1, -0.25, 0, 0.5, 1, 2.5, 4):
    d = mp.mpf(d)
    print(f"  d = {float(d):6.2f}:  h0(d) = {mp.nstr(h0(d), 12):>16}   RR residual = {mp.nstr(h0(d) - h0(-d) - d, 3)}")

print("\n(iii) Lambda(s) = int_0^inf (theta(x)-1)/2 x^{s/2} dx/x  vs  pi^{-s/2} Gamma(s/2) zeta(s), Re s > 1;"
      " and the continued form (Riemann) on the critical line")
for s in (mp.mpf(2), mp.mpf(3.5), mp.mpc(2, 5)):
    lhs = mp.quad(lambda x: (theta(x) - 1) / 2 * x ** (s / 2 - 1), [0, 1, mp.inf])
    rhs = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    print(f"  s = {mp.nstr(s, 6)}: |difference| = {mp.nstr(abs(lhs - rhs), 3)}")
riemann = lambda s: -1 / (s * (1 - s)) + mp.quad(lambda x: (theta(x) - 1) / 2 * (x ** (s / 2) + x ** ((1 - s) / 2)) / x, [1, mp.inf])
for s in (mp.mpc(0.5, 14.134725141734693790), mp.mpc(0.5, 10), mp.mpc(0.3, 7)):
    rhs = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    print(f"  s = {mp.nstr(s, 8)}: |RR-continuation - Lambda(s)| = {mp.nstr(abs(riemann(s) - rhs), 3)};"
          f"  |Lambda(s) - Lambda(1-s)| = {mp.nstr(abs(riemann(s) - riemann(1 - s)), 3)}")

# ---- (iv) Stepanov's half over Z at multiplicity one: Chebyshev's auxiliary integer C(2X, X)
# Every prime in (X, 2X] divides C(2X, X) exactly once ("vanishes" there to order 1), and its "degree"
# log C(2X, X) bounds their weighted count: theta(2X) - theta(X) <= log C(2X, X) ~ 2X log 2.
# Stepanov's multiplicity M = p^mu (char-p Frobenius) is what turns the error from O(count) into O(sqrt(count)).
import math
import numpy as np
N = 2 * 10**6
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
logs = np.where(sieve, np.log(np.arange(N + 1, dtype=float)), 0.0)
cum = np.cumsum(logs)
print("\n(iv) multiplicity one (Chebyshev): theta(2X)-theta(X) vs log C(2X,X); RH needs error ~ sqrt(X) log^2 X")
for X in (10**3, 10**4, 10**5, 10**6):
    count = cum[2 * X] - cum[X]
    aux = math.lgamma(2 * X + 1) - 2 * math.lgamma(X + 1)
    print(f"  X = {X:>8}: theta(2X)-theta(X) = {count:12.1f} | log C(2X,X) = {aux:12.1f} | excess = {aux - count:12.1f}"
          f" | sqrt(X) log^2 X = {math.sqrt(X) * math.log(X)**2:10.1f}")
