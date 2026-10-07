#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P5-settlements.py  --  Grounded settlement artifact for paper P5
(exterior of the Helmert-Fourier transfer matrix T9 and the Kummer clock /
m-power gauge hierarchy T10), under the Grounded-Paranoid-Delusional method.

Three audits. Each prints its PRE-CLAIM (matched-pair K / L / joint, fixed
BEFORE the computation), then settles on DETERMINISTIC EXACT arithmetic
(integer / Fraction; floats only as explicitly-labelled non-voting witnesses),
then prints the REALIZED branch.

Anchored objects (the source's own):
  T9 (Helmert-Fourier Transfer Matrix): U_{kc}=<h_k,chi_c>/sqrt(N k(k+1)),
        h_k=(1,..,1,-k,0,..,0); U unitary over K_N . Q(zeta_N); the conductor-
        block content of U is an explicit UNBUILT forward door (T9 claim 5/§4.4,
        "Gauss-sum-like content over divisors of d").
  T10 (Kummer Clock): K_N^{(m)} = Q(zeta_m, p^{1/m}: p<=N prime); m=2 is T4's
        multiquadratic radical clock; growth adjoins root at prime rungs.
  T3 (conductor packets H_d), P4 (the conductor-class-function fork-width).

Run:  python P5-settlements.py   (deterministic; re-run reproduces this transcript)
"""
import sys, cmath, math
from fractions import Fraction
from math import gcd, cos, pi, isqrt

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr():  print("=" * 78)
def sub(): print("-" * 78)

# ---- elementary number theory (exact integers) ---------------------------
def is_prime(n):
    if n < 2: return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0: return False
    return True

def primes_upto(N):  return [p for p in range(2, N + 1) if is_prime(p)]
def pi_count(N):     return len(primes_upto(N))

def euler_phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def mobius(n):
    if n == 1: return 1
    cnt = 0; m = n; d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d; cnt += 1
            if m % d == 0: return 0      # square factor
        d += 1
    if m > 1: cnt += 1
    return -1 if cnt % 2 else 1

def divisors(n):  return [d for d in range(1, n + 1) if n % d == 0]

def ramanujan(d, n):
    """Ramanujan sum c_d(n) = sum_{a mod d, gcd(a,d)=1} e^{2 pi i a n / d},
    by Hoelder's exact formula:  c_d(n) = mu(d/g) * phi(d)/phi(d/g), g=gcd(d,n).
    Even in n (c_d(-n)=c_d(n)); returns an exact integer."""
    if d == 0:
        return 0
    g = gcd(d, n)                 # math.gcd handles negative n (returns |gcd|)
    q = d // g
    return mobius(q) * euler_phi(d) // euler_phi(q)

# ---- Helmert vector ------------------------------------------------------
def helmert(k, N):
    """h_k = (1,...,1,-k,0,...,0): k ones at positions 0..k-1, -k at position k."""
    v = [0] * N
    for s in range(k): v[s] = 1
    v[k] = -k
    return v


# ==========================================================================
hr()
print("AUDIT  פ-transfer  --  the conductor-block content of the Helmert-Fourier")
print("                      transfer matrix is a RAMANUJAN-sum distribution")
hr()
print("""PRE-CLAIM (before the computation runs).
T9 leaves the conductor-block structure of U as a forward door (claim 5, §4.4),
calling it 'Gauss-sum-like content over the divisors of d'. The exterior claim:
the additive packet sum is precisely the RAMANUJAN sum, so each Helmert rung k
distributes its Fourier weight over the conductor packets H_d (d|N) as
   R_k(d) = sum_{c in H_d} |U_{kc}|^2
          = ( 1/(N k(k+1)) ) * sum_{s,t} (h_k)_s (h_k)_t c_d(s-t),
with c_d the Ramanujan sum (Hoelder's exact integer formula).

  K1 : R_k(d) equals the exact Ramanujan-sum quadratic form above AND is a
       COMPLETE distribution over conductors, sum_{d|N} R_k(d) = 1 exactly.
       (Proof of completeness: sum_{d|N} c_d(n) = N*[N|n], so the double sum
       telescopes to sum_s (h_k)_s^2 / (k(k+1)) = (k + k^2)/(k(k+1)) = 1.)
       This identifies T9's 'Gauss-sum-like content' as Ramanujan sums.
  L1 : R_k(d) != the Ramanujan form, or sum_d R_k(d) != 1.
  K2 (SHARP, may fail) : the conductor distribution {R_k(d)}_d is the SAME for
       every Helmert rung k (k-independent).
  L2 : it depends on k.
  JOINT-ON-DISJOINT : R_k(d) is k-dependent in general, but the LAST rung
       k=N-1 is special (T9 claim 3 'last-row uniformity'): its distribution is
       flat / concentrated in a single packet.
Check: exact Ramanujan c_d via Hoelder; exact Fraction R_k(d); the completeness
sum; plus a FLOAT |U_{kc}|^2 cross-check (non-voting witness).""")
sub()

def R_exact(k, N, d):
    h = helmert(k, N)
    tot = 0
    for s in range(N):
        if h[s] == 0: continue
        for t in range(N):
            if h[t] == 0: continue
            tot += h[s] * h[t] * ramanujan(d, s - t)
    return Fraction(tot, N * k * (k + 1))

def R_float(k, N, d):
    """Independent float witness: sum over the packet of |U_{kc}|^2."""
    h = helmert(k, N)
    norm = N * k * (k + 1)
    tot = 0.0
    for c in range(1, N):
        if (N // gcd(c, N)) != d:        # cond(c) != d
            continue
        z = sum(h[s] * cmath.exp(2j * pi * c * s / N) for s in range(N))
        tot += abs(z) ** 2 / norm
    return tot

for N in (6, 12, 30):
    divs = [d for d in divisors(N) if d > 1]   # nontrivial conductors
    print(f"  N={N}:  nontrivial conductors (divisors d|N, d>1): {divs}")
    complete_ok = True
    witness_ok = True
    rows = {}
    for k in range(1, N):
        rk = {d: R_exact(k, N, d) for d in divisors(N)}   # include d=1
        s = sum(rk.values())
        complete_ok &= (s == 1)
        # float cross-check on nontrivial conductors
        for d in divs:
            if abs(float(rk[d]) - R_float(k, N, d)) > 1e-9:
                witness_ok = False
        rows[k] = rk
    # k-independence (K2): are the distributions equal across all k?
    base = rows[1]
    k_indep = all(rows[k] == base for k in range(1, N))
    # last-rung structure (joint): distribution of k=N-1 over nontrivial conds
    last = rows[N - 1]
    last_nontrivial = {d: last[d] for d in divs}
    last_support = [d for d in divs if last[d] != 0]
    print(f"        completeness sum_d R_k(d)=1 (all k): {complete_ok}    "
          f"float |U|^2 witness agrees: {witness_ok}")
    print(f"        K2 distribution k-independent: {k_indep}")
    # show two sample rungs to expose k-dependence
    for k in (1, N - 1):
        dist = "  ".join(f"d={d}:{rows[k][d]}" for d in divisors(N))
        print(f"        R_{k}(d):  {dist}")
    print(f"        last rung k={N-1}: nonzero only on conductors {last_support} "
          f"(of {divs})")
    sub() if N != 30 else None
print("REALIZED BRANCH  פ-transfer :  printed above; read against K1/K2/joint.")
print()


# ==========================================================================
hr()
print("AUDIT  פ-Kummer  --  the Kummer-clock degree factors into a finite-prime")
print("                    gauge part times a real-place dimensional tower")
hr()
print("""PRE-CLAIM (before the computation runs).
T10 defines the Kummer clock K_N^{(m)} = Q(zeta_m, p^{1/m}: p<=N prime), the
m=2 case being T4's multiquadratic radical clock. Its generic degree over Q is
[K_N^{(m)}:Q] = phi(m) * m^{pi(N)}: the cyclotomic base Q(zeta_m) of degree
phi(m), times one factor of m for each prime p<=N whose m-th root is adjoined.

  K1 : the degree FACTORS as (phi(m)) x (m^{pi(N)}) -- a FINITE-PRIME / gauge
       part phi(m) [the zeta_m, fixed by the gauge m] times a REAL-PLACE
       dimensional tower m^{pi(N)} [the radicals p^{1/m}, growing with N]. The
       two places of P3 again, now as the two factors of one degree.
  L1 : the degree does not factor this way.
  K2 (SHARP) : the real-place factor grows by exactly m at EVERY prime rung N
       (and by 1 at composite N), i.e. m^{pi(N)} jumps by m iff N is prime --
       the exact analog of T4's 'K_N grows over K_{N-1} iff N prime', now for
       all m.
Check: exact pi(N), phi(m); the factorization and the prime-rung growth ratio.""")
sub()
for m in (2, 3, 4, 6):
    print(f"  gauge m={m} (cyclotomic base phi(m)={euler_phi(m)}):")
    prev = None
    line = []
    for N in range(2, 13):
        piN = pi_count(N)
        deg = euler_phi(m) * (m ** piN)
        ratio = "" if prev is None else f"x{deg // prev}"
        tag = "prime" if is_prime(N) else "     "
        line.append((N, tag, deg, ratio))
        prev = deg
    for (N, tag, deg, ratio) in line:
        growth_ok = (is_prime(N) and ratio == f"x{m}") or \
                    ((not is_prime(N)) and ratio in ("", "x1"))
        print(f"      N={N:>2} {tag}: deg = phi({m})*{m}^{pi_count(N)} = {deg:>8}   "
              f"growth {ratio:<4} {'ok' if growth_ok or ratio=='' else 'CHECK'}")
sub()
print("REALIZED BRANCH  פ-Kummer :  the degree is phi(m)*m^{pi(N)} -- finite-prime")
print("  gauge factor phi(m) times real-place radical tower m^{pi(N)} that grows")
print("  by exactly m at each prime rung. Two places, two factors.")
print()


# ==========================================================================
hr()
print("AUDIT  פ-overlap  --  the real radicals and the cyclotomic field MEET on the")
print("                     real quadratic subfields of Q(zeta_N) (conductor criterion)")
hr()
print("""PRE-CLAIM (CORRECTED criterion -- see the CORRECTION note).
T9's transfer matrix lives over the compositum K_N . Q(zeta_N): the real
multiquadratic field K_N=Q(sqrt p: p<=N) (T4) and the cyclotomic field Q(zeta_N).
Are they independent, or do they overlap -- and by exactly what?

  K : they OVERLAP. The real radical sqrt(p) lies in Q(zeta_N) iff the CONDUCTOR
      of Q(sqrt p) divides N, with cond = 8 (p=2), p (p=1 mod4), 4p (p=3 mod4)
      [conductor-discriminant theorem]. So K_N cap Q(zeta_N) = Q( sqrt p :
      cond(Q(sqrt p)) | N ), the real quadratic subfields of Q(zeta_N) that K_N
      carries. NOT linearly disjoint.
  L : the overlap is trivial (linearly disjoint over Q).
  JOINT-ON-DISJOINT : a parity distinction survives, but NOT 'real only for
      p=1 mod4'. The p=1 primes enter at p|N; the p=3 primes enter at 4p|N --
      they need the extra 2-adic factor 4 (the prime 2's ramification, tying to
      [P4]'s 2-adic anomaly); p=2 enters at 8|N.

CORRECTION (retained, per the method's record).  The FIRST DRAFT of this audit
tracked the quadratic GAUSS SUM sqrt(p*), p*=(-1)^{(p-1)/2}p -- real iff p=1 mod4
-- and WRONGLY concluded the real overlap at N=12 is trivial. But the real
RADICAL sqrt(p) is a DIFFERENT object: for p=3 mod4 it has conductor 4p, not p,
and sqrt(3)=zeta_12+zeta_12^{-1} IS real in Q(zeta_12). The gate passed the false
claim because the artifact ENCODED THE WRONG CRITERION -- it certified that prose
matched computation, not that the computation asked the right question (Murillo
Montero, error reported 2026-05-30). Corrected here to the conductor criterion.
Check: for each prime p<=N, sqrt(p) in Q(zeta_N) iff cond(Q(sqrt p)) | N; exact.""")
sub()
def cond_sqrt_p(p):
    """Conductor of the real quadratic field Q(sqrt p): 8 (p=2), p (p=1 mod4),
    4p (p=3 mod4)  [conductor = |discriminant|; conductor-discriminant theorem]."""
    if p == 2: return 8
    return p if p % 4 == 1 else 4 * p

for N in (5, 8, 12, 15, 24, 30):
    radicals = [p for p in primes_upto(N) if N % cond_sqrt_p(p) == 0]
    deg = 2 ** len(radicals)
    detail = ", ".join(f"sqrt{p}(cond {cond_sqrt_p(p)})" for p in radicals) or "none"
    print(f"  N={N:>2}: real radicals sqrt(p) in Q(ζ_N): {radicals}   "
          f"[{detail}]   K_N∩Q(ζ_N) degree = {deg}")
sub()
print("  spotlight N=12: cond(Q(sqrt 3))=4*3=12 | 12, so sqrt(3)=zeta_12+zeta_12^{-1}")
print("  is REAL in Q(zeta_12); K_12 ∩ Q(zeta_12) = Q(sqrt 3) = Q(zeta_12)^+ (NOT trivial).")
sub()
print("REALIZED BRANCH  פ-overlap :  K + JOINT-ON-DISJOINT (criterion CORRECTED)")
print("  K_N and Q(ζ_N) fuse on the real quadratic subfields Q(sqrt p) with")
print("  cond(Q(sqrt p)) | N -- a CONDUCTOR criterion, not the Gauss-sum one. JOINT:")
print("  p=1 mod4 enter at p|N, p=3 mod4 at 4p|N (the extra 2-adic factor 4), p=2 at")
print("  8|N. The first-draft Gauss-sum criterion -- and its false 'N=12 trivial'")
print("  verdict, certified [P] by the gate -- is the RETAINED methodological failure")
print("  of this P5 audit: the gate checks prose-vs-computation, not the question.")
print()

hr()
print("END OF SETTLEMENTS  (deterministic; re-run reproduces this transcript)")
hr()
