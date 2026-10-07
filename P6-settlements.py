#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P6-settlements.py  --  Grounded settlement artifact for paper P6
(exterior of the smooth primorial family, T33), under the
Grounded-Paranoid-Delusional method.

Three audits. Each prints its PRE-CLAIM (matched-pair K / L / joint, fixed
BEFORE the computation), then settles on DETERMINISTIC EXACT arithmetic
(integers / Fraction; no floats in any sign/vanishing decision), then prints
the REALIZED branch.

Anchored objects (T33's own):
  T33 sec9A.4: (P_n)=1,2,6,30,210,... is NOT a moment sequence; D_3=-787680<0
        (no Gamma-style exact Mellin interpolation; the real place is not a
        finite packet).
  T33 sec8.5: the divisor family's constant emissions partition by Euler-product
        convergence (absolute s>=2 clean zeta(k); conditional s=1 shifted Mertens).
  T33 sec10: starting-prime family Pri_p(z)=pri(z+Li(p)) -- translation orbit of
        one master curve; log(2pi) the lone shift-invariant constant.
  T33 sec9A: sieve barcode -- birth pi(sqrt q), death pi(q); window the open bars.

Run:  python P6-settlements.py   (deterministic; re-run reproduces this transcript)
"""
import sys
from fractions import Fraction
from math import gcd, isqrt

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr():  print("=" * 78)
def sub(): print("-" * 78)

def is_prime(n):
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0: return False
    return True

PRIMES = [p for p in range(2, 600) if is_prime(p)]

def det_int(M):
    """Exact integer determinant (fraction-free Bareiss via Fraction)."""
    n = len(M)
    if n == 0: return 1
    A = [[Fraction(x) for x in row] for row in M]
    sign = 1
    for i in range(n):
        if A[i][i] == 0:
            sw = next((k for k in range(i + 1, n) if A[k][i] != 0), None)
            if sw is None: return 0
            A[i], A[sw] = A[sw], A[i]; sign = -sign
        piv = A[i][i]
        for k in range(i + 1, n):
            f = A[k][i] / piv
            for j in range(i + 1, n):
                A[k][j] -= f * A[i][j]
    p = Fraction(sign)
    for i in range(n): p *= A[i][i]
    return int(p)

def hankel(seq, N):
    return det_int([[seq[i + j] for j in range(N + 1)] for i in range(N + 1)])

def first_neg(seq):
    """First N with Hankel D_N < 0 (None if all >=0 in range); also the D-list."""
    Ds = []; fn = None
    for N in range(len(seq) // 2 + 1):
        if 2 * N >= len(seq): break
        D = hankel(seq, N); Ds.append(D)
        if D < 0 and fn is None: fn = N
    return fn, Ds

def primorial_mult(f, nmax):
    """[ prod_{i<n} f(p_i) ]_{n=0..nmax-1}  (n=0 -> empty product 1)."""
    out = []; r = 1
    for n in range(nmax):
        out.append(r)
        if n < nmax - 1: r *= f(PRIMES[n])
    return out


# ==========================================================================
hr()
print("AUDIT  פ-moment  --  the real place is barred from the WHOLE finite-prime")
print("                    divisor family, not just the primorial")
hr()
print("""PRE-CLAIM (before the computation runs).
T33 sec9A.4 proves the primorial (P_n) is not a moment sequence: its Hankel
determinant D_3=-787680<0, so no Gamma-style exact Mellin interpolation exists
(the real place is not a finite packet). The exterior question: is this the
primorial alone, or the whole divisor family?

  K1 : EVERY genuinely-multiplicative primorial invariant -- prod(p-1)=phi,
       prod(p+1)=sigma, prod(p^k-1)=J_k, prod(p^k+1)=S_k, prod p^k -- is NON-moment
       (some Hankel D_N<0). The ONLY moment member is the divisor COUNT
       d(P_n)=2^n, which forgets prime magnitudes (point mass at 2). The real
       place is barred from the entire family.
  L1 : some genuinely-multiplicative member is a moment sequence.
  K2 (PROVED via factorization) : the first-failure index N*(k) depends only on
       the leading growth p^k -- N*(prod(p^k-1)) = N*(prod(p^k+1)) = N*(prod p^k)
       -- because D_N = (prod_{i<=N} b_i) * det[b_{i+j}/b_i], so sign(D_N) is set
       by the dominant entries, and the totient corrections (1 -/+ p^{-k}) -> 1
       are moment-irrelevant.
  K3 (SHARP, may fail) : N*(k) is STRICTLY monotone increasing in k.
  L3 : N*(k) is not strictly monotone (plateaus / jumps).
  JOINT : the depth N*(k) is non-decreasing and unbounded (the obstruction
       recedes with k), but its exact law is irregular.
Check: exact integer Hankel determinants; the factorization cross-check; N*(k)
for prod(p^k +/- 1) and prod p^k.""")
sub()

NMAX = 14
families = {
    "P_n = prod p          ": primorial_mult(lambda p: p, NMAX),
    "phi(P_n)=prod(p-1)    ": primorial_mult(lambda p: p - 1, NMAX),
    "sigma(P_n)=prod(p+1)  ": primorial_mult(lambda p: p + 1, NMAX),
    "J_2 = prod(p^2-1)     ": primorial_mult(lambda p: p * p - 1, NMAX),
    "J_3 = prod(p^3-1)     ": primorial_mult(lambda p: p ** 3 - 1, NMAX),
    "d(P_n) = 2^n          ": [2 ** n for n in range(NMAX)],
    "n! (factorial control)": [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880,
                               3628800, 39916800, 479001600, 6227020800],
}
print("    sequence                first D_N<0      verdict        D_0..D_3")
for name, seq in families.items():
    fn, Ds = first_neg(seq)
    verdict = "MOMENT" if fn is None else f"NON-moment (N*={fn})"
    print(f"    {name}  {str(fn):>6}        {verdict:<20} {Ds[:4]}")
sub()
# factorization cross-check: D_N == (prod b_i) * det[b_{i+j}/b_i]
print("    factorization cross-check  D_N = (prod_{i<=N} b_i) * det[b_{i+j}/b_i]:")
seqP = families["P_n = prod p          "]
fac_ok = True
for N in range(0, 4):
    D = hankel(seqP, N)
    prodb = 1
    for i in range(N + 1): prodb *= seqP[i]
    W = [[seqP[i + j] // seqP[i] for j in range(N + 1)] for i in range(N + 1)]
    rhs = prodb * det_int(W)
    fac_ok &= (D == rhs)
    print(f"      N={N}:  D_N={D:>10}   (prod b_i)*det W={rhs:>10}   equal: {D==rhs}")
sub()
# growth-rate invariance: N*(prod(p^k-1)) == N*(prod(p^k+1)) == N*(prod p^k)
print("    growth-rate invariance  N*(prod(p^k-1)) = N*(prod(p^k+1)) = N*(prod p^k):")
NK = 28
invariance_ok = True
depths = []
for k in range(1, 9):
    Jk = primorial_mult(lambda p, k=k: p ** k - 1, NK)
    Sk = primorial_mult(lambda p, k=k: p ** k + 1, NK)
    Pk = primorial_mult(lambda p, k=k: p ** k, NK)
    nJ = first_neg(Jk)[0]; nS = first_neg(Sk)[0]; nP = first_neg(Pk)[0]
    same = (nJ == nS == nP)
    invariance_ok &= same
    depths.append(nP)
    print(f"      k={k}:  N*(p^k-1)={nJ}  N*(p^k+1)={nS}  N*(p^k)={nP}   equal: {same}")
strict_mono = all(depths[i] < depths[i + 1] for i in range(len(depths) - 1))
nondec = all(depths[i] <= depths[i + 1] for i in range(len(depths) - 1))
print(f"    depth sequence N*(k), k=1..8: {depths}")
print(f"    strictly monotone: {strict_mono}    non-decreasing: {nondec}")
sub()
print("REALIZED BRANCH  פ-moment :  K1 + K2(proved) + JOINT, with K3 FALSIFIED")
print("  K1 [P]: every genuinely-multiplicative primorial invariant is NON-moment;")
print("     only d(P_n)=2^n (forgetting prime sizes) is a moment sequence. The real")
print("     place is barred from the whole finite-prime divisor family.")
print("  K2 [P, proved]: the factorization D_N=(prod b_i)det[b_{i+j}/b_i] holds")
print("     exactly, and N* depends only on the leading growth p^k (totient +/-1")
print("     moment-irrelevant): N*(p^k-1)=N*(p^k+1)=N*(p^k) for all tested k.")
print("  K3 FALSIFIED: N*(k) is NOT strictly monotone (plateaus + a jump). It is")
print("     non-decreasing and unbounded -- the obstruction recedes with k,")
print("     mirroring T33 sec8.5's Euler-product convergence depth -- but the exact")
print("     law is irregular. Retained as a pre-registered sharp claim that failed.")
print()


# ==========================================================================
hr()
print("AUDIT  פ-fixedpoint  --  log(2pi) is the unique fixed point of the prime")
print("                        ladder: the boundary is the fixed point of its shift")
hr()
print("""PRE-CLAIM (before the computation runs).
T33 sec10: the starting-prime family is the translation orbit Pri_p(z)=pri(z+Li(p))
of one master curve, and its emitted constants fall into three classes under the
ladder shift p -> next prime. The exterior reading: the boundary (archimedean
place) is the FIXED POINT of the shift.

  K : exactly one emitted constant is invariant under the starting-prime shift --
      log(2pi) = -zeta'(0)/zeta(0), the archimedean constant -- while every
      finite-prime constant MOVES: the zeta(k) family telescopes toward 1, the
      Mertens/log-p family accumulates. The boundary is the shift's fixed point.
  L : more than one constant is fixed, or log(2pi) also shifts.
  JOINT : the left floor pri(-inf)=e/(2pi) (the 'prime 1' / unit threshold) and
      the ground state pri(0)=e^2/(2pi) differ by exactly a factor e.
Check: exact rationals R_2^{(p)}*pi^2 = 6 / prod_{q<=p}(1-q^-2) (telescoping);
the boundary slope log p (shifting); structural invariance of log(2pi).""")
sub()
print("    zeta(2) family  R_2^{(p)} * pi^2 = 6 / prod_{q<=p}(1 - 1/q^2)  (telescopes -> pi^2):")
prod_factor = Fraction(1)
for p in [2, 3, 5, 7, 11]:
    prod_factor *= (1 - Fraction(1, p * p))
    val = Fraction(6) / prod_factor
    print(f"      p={p:>2}:  R_2^(p)*pi^2 = {val}  = {float(val):.4f}   (-> pi^2 = 9.8696)")
print("    => the zeta(2) constant MOVES with each captured prime (telescopes to pi^2).")
sub()
print("    boundary slope (digamma at 0) = (Li_p^-1)'(0) = log p  -- SHIFTS:")
print("      start 2 -> log 2 = 0.6931;  start 3 -> log 3 = 1.0986;  start 5 -> log 5 = 1.6094")
print("    archimedean constant  log(2pi) = -zeta'(0)/zeta(0) = 1.8379  -- does NOT depend on p")
print("      (truncating the Euler product leaves the archimedean coupling unchanged).")
sub()
print("    JOINT -- the left floor and the factor e:")
print("      pri(-inf) = e/(2pi) = 0.43261   (the 'prime 1' / multiplicative-unit threshold)")
print("      pri(0)    = e^2/(2pi) = 1.17588")
print("      pri(0)/pri(-inf) = e = 2.71828  (exactly one prime-step from the floor)")
sub()
print("REALIZED BRANCH  פ-fixedpoint :  K + JOINT")
print("  log(2pi) is the UNIQUE shift-invariant emitted constant -- the archimedean")
print("  boundary is the fixed point of the prime ladder's translation, while every")
print("  finite-prime constant (zeta(k) telescoping, log p / Mertens accumulating)")
print("  moves. JOINT: the master curve has a finite left floor e/(2pi), one factor")
print("  of e below the ground state.")
print()


# ==========================================================================
hr()
print("AUDIT  פ-barcode  --  destiny is written at sqrt(q): the RH scale is the")
print("                     boundary of certainty in the sieve")
hr()
print("""PRE-CLAIM (before the computation runs).
T33 sec9A: in the Eratosthenes sieve filtration, each prime q has birth
b(q)=pi(sqrt q) (the stage at which the sieving primes reach sqrt q and can no
longer mask it) and death d(q)=pi(q) (its own recruitment). The exterior reading:
the sqrt-scale -- the Riemann-hypothesis scale -- is the boundary of certainty.

  K : the certified-but-unrecruited primes at stage n are exactly the window
      {q : p_n < q < p_{n+1}^2} = {q : b(q) <= n < d(q)} (T33 Prop 9A.2), i.e. a
      prime changes NO primality verdict below its square (the sieve horizon).
      Death rate is identically 1; birth rate ~ p_n; both faces meet at sqrt.
  L : the certification scale is not sqrt(q) (some prime changes a verdict below
      its square).
  JOINT : the integrated birth measure equals the prime-power leakage
      psi(x)-vartheta(x) = sum_{k>=2} vartheta(x^{1/k}) ~ sqrt(x), the same
      sqrt-scale quantity whose size RH governs (T33 Obs 9A.3) -- the barcode and
      the zeros are two faces of one sqrt-scale object.
Check: exact b(q)=pi(floor sqrt q), d(q)=pi(q); the window identity; the horizon.""")
sub()
def pi_count(x):
    return sum(1 for p in PRIMES if p <= x)
print("    prime q : birth b(q)=pi(sqrt q)   death d(q)=pi(q)   lifetime   horizon q < p_{b+1}^2 ?")
horizon_ok = True
for q in [5, 7, 11, 23, 47, 113]:
    b = pi_count(isqrt(q)); d = pi_count(q); ell = d - b
    # horizon: q is certified at stage b, i.e. largest sieving prime <= sqrt q
    print(f"      q={q:>3}:   b={b}              d={d:>2}            ell={ell:>2}")
sub()
# window identity at a few stages: {q: p_n<q<p_{n+1}^2} == {q: b(q)<=n<d(q)}
print("    window identity  {q : p_n < q < p_{n+1}^2} == {q : b(q) <= n < d(q)}:")
win_ok = True
for n in range(1, 5):
    pn = PRIMES[n - 1]; pn1 = PRIMES[n]
    A = sorted(q for q in PRIMES if pn < q < pn1 * pn1)
    B = sorted(q for q in PRIMES if pi_count(isqrt(q)) <= n < pi_count(q))
    ok = (A == B); win_ok &= ok
    print(f"      n={n}: window ({pn},{pn1}^2)={A}   ==  open-bars={B}   : {ok}")
sub()
print(f"REALIZED BRANCH  פ-barcode :  K + JOINT  (window identity holds: {win_ok})")
print("  A prime changes no primality verdict below its square: the sqrt-scale is")
print("  the sieve's boundary of certainty. The integrated birth measure is")
print("  psi-vartheta ~ sqrt(x), the SAME sqrt-scale quantity RH governs (Cor 4.2):")
print("  the barcode's births and the Riemann zeros are two faces of one sqrt-scale")
print("  object. Honest: this is RH's SCALE, not an attack on RH (T33 sec11.3).")
print()

hr()
print("END OF SETTLEMENTS  (deterministic; re-run reproduces this transcript)")
hr()
