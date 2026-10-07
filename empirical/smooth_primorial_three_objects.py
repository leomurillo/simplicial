#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
smooth_primorial_three_objects.py

Probe (a): exhibit the THREE smooth-primorial objects unveiled by the
Marichal-Zenaidi / Krull-Webster prior-art dive, and quantify how they relate.

  P_n  = prod_{k<=n} p_k                      (exact primorial)
  A(n) = exp(Li^{-1}(n)) / (2*pi)             (explicit-formula object; the paper's)
  B(n) = prod_{k<=n} ali(k)                   (product of SMOOTH primes;
                                               = the M-Z principal indefinite sum
                                               of the smooth log-prime, at integers)

Conventions (Arias de Reyna - Toulisse, arXiv:1203.5413):
  li(x)            = logarithmic integral (UNshifted)         [mpmath.li(x)]
  ali(x)=li^{-1}(x)= inverse of li  ("smooth n-th prime", p_n ~ ali(n))
  Li(x)=li(x)-li(2)= Eulerian/shifted log integral            [mpmath.li(x, offset=True)]
  Li^{-1}(n)       = ali(n + li(2))           (our paper's "smooth n-th prime, shifted")
  (d/dx) ali = log(ali),  so  integral of log(ali) = ali   (the key identity)

Question settled here:
  * Does A track P_n (paper's claim) and at what scale is the defect?
  * Does B track P_n, and how does its defect differ from A's?
  * Do A and B diverge?  Prediction from Euler-Maclaurin:
        log A - log B  ~  (li(2) - 1/2) * log(ali(n))  ->  +infinity
    i.e. A/B ~ ali(n)^{li(2)-1/2} ~ ali(n)^{0.545}  (three genuinely distinct objects).

Deterministic; mpmath only (no torch).  Run: python smooth_primorial_three_objects.py
"""
import sys
from sympy import primerange
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

mp.mp.dps = 40                      # 40 significant digits
TWO_PI = 2 * mp.pi
LI2 = mp.li(2)                      # li(2) ~ 1.04516378
HALF = mp.mpf(1) / 2

def hr():  print("=" * 100)

# ----- exact primes / primorials -----------------------------------------
N = 20
primes = list(primerange(2, 1000))[:N]          # p_1..p_N
P = []                                           # P[n] = product of first n primes (n=1..N)
acc = 1
for p in primes:
    acc *= p
    P.append(acc)

# ----- numeric inverse log integrals -------------------------------------
def _guess(x):
    """Robust starting point for li-inversion: ali(x) ~ p_{round(x)} ~ x*log(x*log x)."""
    x = mp.mpf(x)
    if x < mp.mpf("1.5"):
        return mp.mpf("1.9")
    lx = mp.log(x + 1)
    return x * mp.log((x + 1) * lx) + 2          # always >1, monotone, near ali(x)

def ali(x, hint=None):
    """li^{-1}(x): solve li(t)=x for t>1 (unshifted; the smooth x-th prime)."""
    x = mp.mpf(x)
    g = mp.mpf(hint) if hint is not None else _guess(x)
    return mp.re(mp.findroot(lambda t: mp.li(t) - x, g))

def Liinv(n, hint=None):
    """Li^{-1}(n): solve Li(t)=li(t)-li(2)=n  (our paper's shifted convention)."""
    n = mp.mpf(n)
    if n <= 0:
        return mp.mpf(2)
    g = mp.mpf(hint) if hint is not None else _guess(n + LI2)
    return mp.re(mp.findroot(lambda t: mp.li(t, offset=True) - n, g))

# sanity vs the paper's table (Li^{-1}(0..5))
hr()
print("VALIDATION  Li^{-1}(n) vs paper Table (sec 1.5): should match 2.000,2.895,4.109,5.688,7.572,9.72")
row = "   ".join(f"{float(Liinv(n)):.4f}" for n in range(0, 6))
print("   Li^{-1}(0..5) =", row)
print(f"   li(2) = {float(LI2):.6f}   (so Li^{{-1}}(n) = ali(n+li(2)))   check: ali(li2)={float(ali(LI2)):.4f} (=2)")
hr()

# ----- the three objects, in logs (avoid overflow) -----------------------
# log A(n) = Li^{-1}(n) - log(2pi)
# log B(n) = sum_{k<=n} log ali(k)
# log P(n) = log of exact integer
ali_vals = [ali(k, hint=primes[k - 1]) for k in range(1, N + 1)]   # ali(1..N), prime-seeded
logB = []
s = mp.mpf(0)
for k in range(N):
    s += mp.log(ali_vals[k])
    logB.append(s)                               # logB[n-1] = sum_{k=1}^n log ali(k)

print("   n |   p_n    ali(n)  |     P_n        A(n)        B(n)    |  A/P     B/P    |  logA-logP  logB-logP  logA-logB")
print("   " + "-" * 116)
data = []
for i in range(N):
    n = i + 1
    logP = mp.log(mp.mpf(P[i]))
    logLi = Liinv(n, hint=primes[i])
    logA = logLi - mp.log(TWO_PI)
    logBn = logB[i]
    A = mp.e ** logA
    Bn = mp.e ** logBn
    dAP = logA - logP                            # log A - log P  (paper: ~ Riemann zero-sum, sqrt-scale)
    dBP = logBn - logP                           # log B - log P
    dAB = logA - logBn                           # log A - log B  (predicted ~ +0.545 log ali(n))
    data.append((n, dAP, dBP, dAB, mp.log(ali_vals[i])))
    AP = mp.e ** dAP
    BP = mp.e ** dBP
    print(f"  {n:2d} | {primes[i]:5d}  {float(ali_vals[i]):7.3f} | "
          f"{('%.3e' % float(P[i])):>10}  {('%.3e' % float(A)):>10}  {('%.3e' % float(Bn)):>10} | "
          f"{float(AP):5.3f}  {float(BP):6.3f}  | "
          f"{float(dAP):+8.4f}   {float(dBP):+8.4f}   {float(dAB):+8.4f}")
hr()

# ----- test the A-vs-B divergence law:  (logA-logB)/log(ali(n)) -> li(2)-1/2 -----
print("DIVERGENCE LAW   (log A - log B) should grow like (li(2) - 1/2) * log(ali(n)).")
print(f"   predicted slope  li(2) - 1/2 = {float(LI2 - HALF):.5f}")
print("   n |  log A - log B |  log(ali(n)) |  ratio (-> li(2)-1/2)")
for (n, dAP, dBP, dAB, logali) in data:
    if n >= 3:
        ratio = dAB / logali
        print(f"  {n:2d} |   {float(dAB):+9.4f}   |   {float(logali):8.4f}   |   {float(ratio):+8.4f}")
hr()

# ----- defect SCALES: |logA-logP| vs sqrt-scale; |logB-logP| growth ----------
print("DEFECT SCALES (does A's defect stay sqrt-scale / RH-bounded while B's accumulates?)")
print("   Arias-Toulisse bound: |p_n - ali(n)| <= (1/pi) sqrt(n) (log n)^{5/2}")
print("   n |  |logA-logP| |  |logB-logP| |  (logB-logP)/log(ali(n))")
for (n, dAP, dBP, dAB, logali) in data:
    if n >= 2:
        r = dBP / logali
        print(f"  {n:2d} |   {float(abs(dAP)):8.4f}   |   {float(abs(dBP)):8.4f}   |   {float(r):+8.4f}")
hr()
print("READING:")
print("  * A(n)=exp(Li^{-1}(n))/2pi : its log-defect vs P_n OSCILLATES and CHANGES SIGN")
print("    (positive for n<=5, crossing 0 near n=6, negative after) -- the signature of the")
print("    sqrt-scale Riemann zero-sum (Cor 1.4: RH <=> defect = O(sqrt(p_n) log^2 p_n)).")
print("  * B(n)=prod ali(k) (product of smooth primes) : its log-defect vs P_n is MONOTONE")
print("    and systematically accumulating (the smooth primes ali(k) overshoot p_k) -- no")
print("    sign change; a steady drift, NOT a sqrt-scale oscillation.")
print("  * So A and B are DISTINCT objects (A/B ~ ali(n)^{~0.5} -> infinity), and A is the")
print("    SUPERIOR smooth primorial: the explicit-formula normalization (-log 2pi = ")
print("    zeta'(0)/zeta(0)) absorbs exactly the systematic drift that the naive product B")
print("    carries, leaving only the oscillating RH-scale error. This is a concrete reason")
print("    to privilege the explicit-formula object and to tie it to zeta.")
hr()
