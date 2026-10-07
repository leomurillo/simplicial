r"""Careful-read verification of P6 פmoment (the family-wide moment barrier).

Checks, in exact integer arithmetic (Bareiss; no floats in any sign decision):
  (1) the divisor family is non-moment with the claimed first-failure index N*;
  (2) the factorization  D_N = (prod_{i<=N} b_i) * det[b_{i+j}/b_i]  (sign carrier);
  (3) whether N* is REALLY invariant across prod(p^k-1), prod(p^k+1), prod p^k
      (P6's K2 claim, marked [P] "proved via factorization");
  (4) d(P_n)=2^n is the lone moment member;
  (5) the N*(k) sequence the paper reports as 3,3,4,4,5,9,9,9.

Also records the analytic identity zeta'(0)/zeta(0) = +log(2 pi) for comparison with the
paper's written "log 2pi = -zeta'(0)/zeta(0)".
"""

import math
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def primes(n):
    out, c = [], 2
    while len(out) < n:
        if all(c % p for p in out):
            out.append(c)
        c += 1
    return out


PR = primes(60)


def det_bareiss(M):
    M = [list(r) for r in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        piv = M[k][k]
        for i in range(k + 1, n):
            ri, mik = M[i], M[i][k]
            for j in range(k + 1, n):
                ri[j] = (ri[j] * piv - mik * M[k][j]) // prev
        prev = piv
    return sign * M[n - 1][n - 1]


def hankel(b, N):
    return [[b[i + j] for j in range(N + 1)] for i in range(N + 1)]


def bseq(f, length):
    b = [1]
    for i in range(length):
        b.append(b[-1] * f(PR[i]))
    return b


def Nstar(b, kmax):
    for N in range(1, kmax + 1):
        if det_bareiss(hankel(b, N)) < 0:
            return N
    return None


KMAX = 10
L = 2 * KMAX + 2

print(__doc__)
print("(1)+(3)+(5)  N* (first N with D_N<0) across the divisor family:")
print("  k | prod p^k | prod(p^k - 1) | prod(p^k + 1) | all three equal?")
print("  --+----------+---------------+---------------+-----------------")
seqN = {}
for k in range(1, 9):
    bp = bseq(lambda p, k=k: p ** k, L)
    bm = bseq(lambda p, k=k: p ** k - 1, L)
    bpl = bseq(lambda p, k=k: p ** k + 1, L)
    Np, Nm, Npl = Nstar(bp, KMAX), Nstar(bm, KMAX), Nstar(bpl, KMAX)
    seqN[k] = Np
    print("  %d | %-8s | %-13s | %-13s | %s" % (k, Np, Nm, Npl, Np == Nm == Npl))
print("  N*(k) for prod p^k, k=1..8 :", [seqN[k] for k in range(1, 9)])
print("  P6 claims                  : [3, 3, 4, 4, 5, 9, 9, 9]")
print()

print("(1) named members:")
for name, f in [("phi=prod(p-1)", lambda p: p - 1),
                ("sigma=prod(p+1)", lambda p: p + 1),
                ("J2=prod(p^2-1)", lambda p: p * p - 1),
                ("J3=prod(p^3-1)", lambda p: p ** 3 - 1),
                ("primorial=prod p", lambda p: p)]:
    b = bseq(f, L)
    D3 = det_bareiss(hankel(b, 3))
    print("  %-18s N* = %-4s  (D_3 = %d)" % (name, Nstar(b, KMAX), D3))
print()

print("(4) divisor count d(P_n) = 2^n:")
b2 = [2 ** n for n in range(22)]
print("  N* =", Nstar(b2, 10), " (None => moment; 2^n = moments of point mass at 2)")
print()

print("(2) factorization at the primorial, N=3:")
bP = bseq(lambda p: p, 8)
H3 = hankel(bP, 3)
prodb = 1
for i in range(4):
    prodb *= bP[i]
W = [[bP[i + j] // bP[i] for j in range(4)] for i in range(4)]
detW = det_bareiss(W)
print("  D_3 = %d ; prod_{i<=3} b_i = %d ; det[b_{i+j}/b_i] = %d ; product = %d ; match = %s"
      % (det_bareiss(H3), prodb, detW, prodb * detW, det_bareiss(H3) == prodb * detW))
print()

print("(zeta sign) analytic identity for comparison (not an integer check):")
print("  zeta'(0)/zeta(0) = log(2 pi) = +%.6f   (since zeta(0)=-1/2, zeta'(0)=-1/2 log 2pi)" % math.log(2 * math.pi))
print("  so 1/(2 pi) = exp(-zeta'(0)/zeta(0)) and log 2pi = +zeta'(0)/zeta(0).")
print("  P6 writes '1/2pi = e^{zeta'(0)/zeta(0)}' and 'log2pi = -zeta'(0)/zeta(0)': sign flipped.")
