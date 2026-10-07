"""
POLYMATH: prove (b_n) with b_n = prod f(p_i) is NOT a Hamburger moment sequence.
Step 1: re-verify established results (deg 1).
Step 2: symbolic D_2(B,C), D_3(B,C) for monic quadratic f(p)=p^2+Bp+C.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, simplify, expand, Poly, Rational
import sympy as sp

P = list(primerange(2, 1000))
print("First 12 primes:", P[:12])

def bn(f, L):
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1])
        b.append(a)
    return b

def Ddet(f, N):
    b = bn(f, 2*N+2)
    M = Matrix(N+1, N+1, lambda i, j: b[i+j])
    return M.det()

# ---- RE-VERIFY deg 1 numeric anchor ----
print("\n=== RE-VERIFY numeric anchors ===")
print("D(p->p, 3) =", Ddet(lambda p: p, 3), " (expect -787680)")

# n! control (c_i = i): ratios c_i = i means b_n = n!
def fac_ratio(i):
    # b_n = prod_{i=1}^n i = n!  -> here 'f' is applied to prime p_i but we want ratio i
    return None
# Build n! directly to confirm it's a moment seq (all Hankel dets > 0)
def Dfac(N):
    b = [Integer(1)]
    for i in range(1, 2*N+2):
        b.append(b[-1]*i)   # b_n = n!
    M = Matrix(N+1, N+1, lambda i, j: b[i+j])
    return M.det()
print("n! Hankel dets D_1..D_4:", [Dfac(N) for N in range(1,5)], "(all >0 => moment)")
