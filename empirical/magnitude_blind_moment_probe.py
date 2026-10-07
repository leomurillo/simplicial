#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
magnitude_blind_moment_probe.py

Serious run at the conjecture (paper sec 4.2, currently [A]):
    "b_n = prod_{i<=n} c_i is a Hamburger moment sequence  <=>  c_i eventually constant."

A sequence (b_n) is a Hamburger moment sequence  ==>  every Hankel determinant
D_N = det(b_{i+j})_{0<=i,j<=N} >= 0.  So a single D_N < 0 PROVES non-moment.
(The converse D_N>=0 for all N is necessary-not-sufficient -- Berg-Szwarc -- but
all D_N>0 over a long range is strong evidence FOR a moment sequence, and the
positive cases below are independently KNOWN moment sequences.)

We test a panel of ratio sequences (c_i), exact integer/rational arithmetic, and
record the first negative Hankel determinant (or 'moment' if none through N=NMAX).

Run: python magnitude_blind_moment_probe.py   (deterministic; sympy)
"""
import sys
from sympy import Integer, Rational, Matrix, primerange, factor, symbols, simplify, prod

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr(): print("=" * 92)

PRIMES = list(primerange(2, 200))

def hankel_first_neg(b, NMAX):
    """b = list of b_0..b_M (exact). Return (first N with D_N<0 or None, [D_0..]) ."""
    Ds = []; fn = None
    N = 0
    while 2 * N < len(b):
        M = Matrix(N + 1, N + 1, lambda i, j: b[i + j])
        D = M.det()
        Ds.append(D)
        if D < 0 and fn is None:
            fn = N
        N += 1
    return fn, Ds

def from_ratios(c, length):
    """b_0=1, b_n = prod_{i=1}^n c_i ; c is a function i(1-indexed)->value."""
    b = [Integer(1)]
    acc = Integer(1)
    for i in range(1, length):
        acc *= c(i)
        b.append(acc)
    return b

NMAX = 7
LEN = 2 * NMAX + 2

# ---- the panel: ratio sequences c_i (1-indexed) ----------------------------
panel = [
    ("c_i = 2                  (divisor count d=2^n; magnitude-blind)", lambda i: Integer(2)),
    ("c_i = 5                  (constant a; -> a^n)",                    lambda i: Integer(5)),
    ("c_i = i                  (factorial n!  =  prod pi(p_i))",         lambda i: Integer(i)),
    ("c_i = i+3                (Pochhammer (1+3)_n)",                    lambda i: Integer(i + 3)),
    ("c_i = i^2                ((n!)^2; Bessel moments)",               lambda i: Integer(i * i)),
    ("c_i = 2^i                (geometric; q^{n(n+1)/2}, log-normal)",  lambda i: Integer(2) ** i),
    ("c_i = p_i                (PRIMORIAL)",                            lambda i: Integer(PRIMES[i - 1])),
    ("c_i = p_i - 1            (Euler totient phi)",                    lambda i: Integer(PRIMES[i - 1] - 1)),
    ("c_i = p_i + 1            (sigma)",                                lambda i: Integer(PRIMES[i - 1] + 1)),
    ("c_i = p_i^2 - 1          (Jordan J_2)",                           lambda i: Integer(PRIMES[i - 1] ** 2 - 1)),
    ("c_i = p_i^2              (prod p^2)",                             lambda i: Integer(PRIMES[i - 1] ** 2)),
    ("c_i = nextprime-gap test: c_i = i-th odd number 1,3,5,7,9,..",    lambda i: Integer(2 * i - 1)),
]

hr()
print("MOMENT TEST  (first Hankel D_N<0 proves NON-moment; 'moment' = all D_N>0 through N=%d)" % NMAX)
hr()
print("    ratio sequence c_i                                          first D_N<0   verdict")
print("    " + "-" * 86)
results = {}
for name, c in panel:
    b = from_ratios(c, LEN)
    fn, Ds = hankel_first_neg(b, NMAX)
    verdict = "MOMENT" if fn is None else f"NON-moment (D_{fn}<0)"
    results[name] = (fn, Ds)
    # magnitude-blind?  c_i constant in i
    print(f"    {name:58s}  {str(fn):>5}        {verdict}")
hr()

# ---- the decisive counterexample, spelled out -----------------------------
print("DECISIVE COUNTEREXAMPLE to 'c_i non-constant => NON-moment':")
b_fact = from_ratios(lambda i: Integer(i), LEN)
fn, Ds = hankel_first_neg(b_fact, NMAX)
print(f"  c_i = i (NON-constant) gives b_n = n! = {[int(x) for x in b_fact[:8]]}")
print(f"  Hankel determinants D_0..D_{NMAX} = {[int(x) for x in Ds]}  -> all > 0 (MOMENT, measure e^-t)")
print(f"  And i = pi(p_i): so b_n = prod_{{i<=n}} pi(p_i), a product over primes with f=pi NON-constant.")
print("  => 'moment => f constant' is FALSE.  Likewise i^2 -> (n!)^2 and 2^i -> log-normal are moment.")
hr()

# ---- symbolic sign-determinant det W_N = sign(D_N) -------------------------
print("SYMBOLIC sign-determinant  det W_N  (sign(D_N) = sign(det W_N), W_{ij}=prod_{l=i+1}^{i+j} c_l):")
print("  Look for a clean factorization / a sufficient NON-moment condition.")
cs = symbols('c1:13', positive=True)          # c1..c12
def Wdet(N):
    def w(i, j):
        # prod_{l=i+1}^{i+j} c_l  (1-indexed c's: c_{l} = cs[l-1])
        p = Integer(1)
        for l in range(i + 1, i + j + 1):
            p *= cs[l - 1]
        return p
    return Matrix(N + 1, N + 1, w).det()

for N in (1, 2, 3):
    d = factor(Wdet(N))
    print(f"  det W_{N} = {d}")
hr()

# ---- evaluate det W_3 at the panel ratios to see when it goes negative -----
print("det W_3 evaluated (its sign = sign of D_3):")
W3 = Wdet(3)
for name, c in panel:
    cvals = {cs[k]: c(k + 1) for k in range(6)}   # need c1..c6 for N=3
    val = W3.subs(cvals)
    print(f"    {name:58s}  det W_3 = {val}   sign {'+' if val>0 else ('-' if val<0 else '0')}")
hr()
print("READING printed after run.")
hr()
