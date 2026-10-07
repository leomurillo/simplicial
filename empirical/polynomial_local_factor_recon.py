#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
polynomial_local_factor_recon.py  --  RECON for the polymath target:

  CLAIM: for every non-constant polynomial f with f(p)>0 on primes,
         b_n = prod_{i<=n} f(p_i) is NOT a Hamburger moment sequence
         (some Hankel determinant D_N = det(b_{i+j})_{0<=i,j<=N} < 0).

This is the SCOUTING pass: try hard to BREAK it before anyone proves it.
Exact integer / symbolic (sympy) arithmetic; a single D_N<0 proves non-moment.

Three experiments:
  (1) GRID: many polynomials f -> first-failure index N*(f) up to N=NMAX.
      A survivor (all D_N>=0 through NMAX) would be a candidate COUNTEREXAMPLE.
  (2) BIG-CONSTANT family f(p)=p+c: as c->inf the ratios ->1 (toward the
      constant/moment case).  Symbolic D_3(c), D_4(c) in c: do they stay <0?
      Plus numeric D_N for very large c (c=10^3,10^6) and N up to 8.
  (3) LEADING-TERM check: does N*(f) depend only on deg f, or on lower terms?
"""
import sys
from sympy import primerange, symbols, factor, Poly, Integer, simplify, oo, solve, Rational

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr(): print("=" * 96)

PRIMES = list(primerange(2, 400))

def bareiss_det(M):
    """Exact integer determinant via fraction-free Bareiss. M: list of list of int."""
    n = len(M)
    A = [row[:] for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if sw is None:
                return 0
            A[k], A[sw] = A[sw], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def b_seq(fvals, length):
    """fvals: list f(p_1),f(p_2),...  -> b_0..b_{length-1}, b_n=prod_{i<=n} fvals[i-1]."""
    b = [1]; acc = 1
    for i in range(1, length):
        acc *= fvals[i - 1]; b.append(acc)
    return b

def first_neg(fvals, NMAX):
    b = b_seq(fvals, 2 * NMAX + 2)
    for N in range(NMAX + 1):
        if 2 * N >= len(b): break
        H = [[b[i + j] for j in range(N + 1)] for i in range(N + 1)]
        D = bareiss_det(H)
        if D < 0:
            return N, D
    return None, None

# ---------------------------------------------------------------- (1) GRID
hr(); print("(1) GRID SEARCH  -- N*(f) = first N with D_N<0 (None = candidate COUNTEREXAMPLE)"); hr()
NMAX = 16
polys = []
# degree 1: a*p + b
for a in (1, 2, 3):
    for b in (-1, 0, 1, 2, 3, 5, 10, 50, 100, 1000, 10**6):
        polys.append((f"{a}p+{b}", lambda p, a=a, b=b: a * p + b))
# degree 2,3,4: p^k and p^k +/- 1 and shifted
for k in (2, 3, 4, 5):
    polys.append((f"p^{k}",     lambda p, k=k: p**k))
    polys.append((f"p^{k}-1",   lambda p, k=k: p**k - 1))
    polys.append((f"p^{k}+1",   lambda p, k=k: p**k + 1))
    polys.append((f"p^{k}+100", lambda p, k=k: p**k + 100))
# mixed
polys.append(("p^2+p+1", lambda p: p*p + p + 1))
polys.append(("(p-1)(p+1)=p^2-1", lambda p: (p-1)*(p+1)))
polys.append(("p^2+1000p", lambda p: p*p + 1000*p))

survivors = []
Nstars = {}
for name, f in polys:
    fvals = [f(p) for p in PRIMES]
    if any(v <= 0 for v in fvals[:2*NMAX+2]):
        print(f"   {name:14s}  skip (f(p)<=0 somewhere)"); continue
    Ns, D = first_neg(fvals, NMAX)
    Nstars[name] = Ns
    tag = "  <-- SURVIVOR (candidate counterexample!)" if Ns is None else ""
    print(f"   {name:14s}  N* = {str(Ns):>4}{tag}")
    if Ns is None:
        survivors.append(name)
print()
print(f"   survivors (all D_N>=0 through N={NMAX}): {survivors or 'NONE'}")
print(f"   N* range over non-survivors: {sorted(set(v for v in Nstars.values() if v is not None))}")
hr()

# ---------------------------------------------------------------- (2) f=p+c symbolic
hr(); print("(2) BIG-CONSTANT family f(p)=p+c :  symbolic sign of D_3(c), D_4(c)"); hr()
c = symbols('c', real=True)
def b_sym(length):
    b = [Integer(1)]; acc = Integer(1)
    for i in range(1, length):
        acc *= (PRIMES[i-1] + c); b.append(acc)
    return b

def hankel_sym(N):
    b = b_sym(2*N + 2)
    H = [[b[i+j] for j in range(N+1)] for i in range(N+1)]
    # sympy Matrix det
    from sympy import Matrix
    return Matrix(H).det()

for N in (1, 2, 3, 4):
    DN = factor(hankel_sym(N))
    print(f"   D_{N}(c) = {DN}")
    try:
        P = Poly(hankel_sym(N), c)
        roots = solve(P.as_expr(), c)
        realroots = [r for r in roots if r.is_real]
        print(f"        leading coeff (c->+inf): {P.LC()},  degree {P.degree()},  real roots: {realroots}")
    except Exception as e:
        print(f"        (root analysis skipped: {e})")
hr()

# ---------------------------------------------------------------- (2b) huge c numeric
hr(); print("(2b) f(p)=p+c at HUGE c (ratios ->1, nearest to the constant/moment case):"); hr()
for cval in (10, 100, 1000, 10**6, 10**9):
    fvals = [p + cval for p in PRIMES]
    Ns, D = first_neg(fvals, 12)
    print(f"   c = {cval:>12} :  N* = {Ns}   (None would mean moment up to N=12)")
hr()

# ---------------------------------------------------------------- (3) leading term
hr(); print("(3) Does N* depend only on deg f, or on lower-order terms?"); hr()
for name, f in [("p", lambda p: p), ("p+1000", lambda p: p+1000),
                ("p^2", lambda p: p*p), ("p^2+10^6", lambda p: p*p+10**6),
                ("p^3", lambda p: p**3), ("p^3+10^9", lambda p: p**3+10**9)]:
    fvals = [f(p) for p in PRIMES]
    Ns, _ = first_neg(fvals, 16)
    print(f"   {name:12s}  N* = {Ns}")
hr()
print("VERDICT printed after run.")
hr()
