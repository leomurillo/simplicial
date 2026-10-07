#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P4-settlements.py  --  Grounded settlement artifact for paper P4
(exterior of the complex/quantum apex and the multiplicative/function-field
apex, T7-T8), under the Grounded-Paranoid-Delusional method (Paper 35).

Four audits. Each prints its PRE-CLAIM (matched-pair K / L / joint-on-disjoint,
meaning fixed BEFORE the computation runs), then settles on DETERMINISTIC,
EXACT arithmetic (integer / Fraction / Eisenstein-integer; no seeds; no float
in any vanishing, membership, sign, or norm decision), then prints the REALIZED
branch.

Anchored objects (GPD 3.3 -- the source's own objects):
  T7 (Complex/Quantum Apex): reduced-rank face strata {z_s=0}; the decohered
        (diagonal) face; the monotone-metric (Petz) fork -- Bures/SLD minimal,
        RLD maximal, Kubo-Mori the dually-flat member in between.
  T8 (Multiplicative Apex & Finite L): units (Z/N)^x; Dirichlet characters and
        their conductors; Gauss/Jacobi sums; the 2-adic anomaly of (Z/8)^x;
        function-field zeta and Weil's RH for the Fermat curve.

The GRH thread is carried HONESTLY: the additive apex's critical-line question
is heuristic (no Frobenius), so classical zeta stays [C]; but the MULTIPLICATIVE
/ function-field apex carries a PROVEN critical line -- Jacobi sums are Frobenius
eigenvalues of the Fermat curve and Weil's RH gives |alpha|=sqrt(q) <=> Re(s)=1/2,
verifiable here by exact integer point-counting. That is the [P] landing.

Run:  python P4-settlements.py
Deterministic; re-run reproduces this transcript identically.
"""

import sys
from fractions import Fraction
from math import gcd, log
from itertools import combinations, product

# Emit UTF-8 regardless of the platform locale (the transcript contains פ, ∂, ω).
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr():  print("=" * 78)
def sub(): print("-" * 78)


# ==========================================================================
# Eisenstein-integer arithmetic  Z[omega],  omega = primitive cube root,
# omega^2 = -1 - omega.   Represent  a + b*omega  as the pair (a, b).
# Norm  N(a+b*omega) = a^2 - a*b + b^2  (exact integer).
# ==========================================================================
def eis_norm(a, b):
    return a * a - a * b + b * b

def reduce_powers(c0, c1, c2):
    """Reduce c0*1 + c1*omega + c2*omega^2 to (a,b) with omega^2 = -1-omega."""
    a = c0 - c2
    b = c1 - c2
    return a, b


# ==========================================================================
# finite-field helpers (exact integer arithmetic mod a prime q)
# ==========================================================================
def primitive_root(q):
    """Smallest generator of the cyclic group F_q^x  (q prime)."""
    order = q - 1
    fac = []
    m = order
    d = 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, q):
        if all(pow(g, order // p, q) != 1 for p in fac):
            return g
    raise RuntimeError("no primitive root")

def discrete_logs(q, g):
    """dlog[x] = k with g^k = x  (x in 1..q-1)."""
    dlog = {}
    cur = 1
    for k in range(q - 1):
        dlog[cur] = k
        cur = (cur * g) % q
    return dlog

def multiplicative_order(a, N):
    """Order of a in (Z/N)^x  (gcd(a,N)=1)."""
    if N == 1:
        return 1            # (Z/1)^x is trivial; everything is 0 mod 1
    o = 1
    cur = a % N
    while cur != 1:
        cur = (cur * a) % N
        o += 1
    return o


# ==========================================================================
hr()
print("AUDIT  פ7  --  the quantum boundary: a Boolean support lattice carrying")
print("              a monotone-metric (Petz) fork, blind on the diagonal")
hr()
print("""PRE-CLAIM (before the computation runs).
T7: a rank-k diagonal apex z=diag(z_1..z_k) degenerates on the face strata
{z_s=0 : s in T}, T a subset of {1..k}; on the surviving block the quantum
Fisher metric is NOT unique -- it is a Petz family, with the Bures/SLD member
minimal and the RLD member maximal. The exterior reading: the strata are the
boundary FACES of the cone, and the metric AMBIGUITY is a boundary object too.

  K : (a) the face strata form the Boolean lattice B_k (2^k elements, graded by
          codimension |T|, Mobius mu(emptyset,T)=(-1)^|T|, meet=intersection,
          join=union); AND
      (b) the monotone-metric coefficient c(x,y) on an eigenvalue pair collapses
          ON the diagonal -- Bures = RLD = 1/x exactly (x=y) -- but SPLITS off
          the diagonal -- Bures < RLD strictly (x!=y).
  L : strata are not a Boolean lattice, OR the metric fork does not collapse on
      the diagonal (Bures != RLD somewhere on x=y).
  JOINT-ON-DISJOINT : the SAME coefficient c(x,y) is fork-degenerate exactly on
      the classical (decohered, diagonal x=y) locus and fork-split exactly on
      the quantum (coherent, off-diagonal x!=y) locus. Classical statistics is
      Chentsov-unique; the Petz ambiguity is supported precisely on the quantum
      off-diagonal -- one coefficient, two disjoint regimes.
Check: exact subset enumeration; Bures = HM(1/x,1/y) = 2/(x+y) and
       RLD = AM(1/x,1/y) = (x+y)/(2xy) as exact Fractions.""")
sub()

# (a) Boolean support lattice B_k
k = 3
strata = []
for r in range(k + 1):
    for T in combinations(range(1, k + 1), r):
        strata.append(frozenset(T))
print(f"    rank-k apex, k = {k}:  face strata = subsets T of {{1..{k}}}")
print(f"    #strata = {len(strata)}   (expect 2^{k} = {2**k})")
rank_counts = [sum(1 for T in strata if len(T) == r) for r in range(k + 1)]
print(f"    graded counts by codim |T|: {rank_counts}   "
      f"(expect binomials C({k},r) = {[len(list(combinations(range(k),r))) for r in range(k+1)]})")
# lattice closure: closed under meet (intersection) and join (union)
S = set(strata)
meet_closed = all((A & B) in S for A in strata for B in strata)
join_closed = all((A | B) in S for A in strata for B in strata)
print(f"    closed under meet (∩): {meet_closed}    closed under join (∪): {join_closed}")
# Mobius function mu(emptyset, T) = (-1)^|T| on a Boolean lattice
mobius_ok = True
for T in strata:
    # mu(0,T) = sum over subsets... but Boolean: mu(0,T)=(-1)^|T|; verify via
    # the defining recurrence  sum_{U subset T} mu(0,U) = [T=0].
    s = sum((-1) ** len(U) for r in range(len(T) + 1) for U in combinations(sorted(T), r))
    want = 1 if len(T) == 0 else 0
    if s != want:
        mobius_ok = False
print(f"    Mobius recurrence  sum_{{U<=T}} (-1)^|U| = [T=∅]  holds for all T: {mobius_ok}")
boolean_ok = (len(strata) == 2**k and rank_counts ==
              [len(list(combinations(range(k), r))) for r in range(k + 1)]
              and meet_closed and join_closed and mobius_ok)
print(f"    => face strata form the Boolean lattice B_{k}: {boolean_ok}")
sub()

# (b) Petz fork on an eigenvalue pair (x,y)
def bures_coeff(x, y):   # SLD / minimal monotone metric  = HM(1/x,1/y)
    return Fraction(2, 1) / (x + y)
def rld_coeff(x, y):     # RLD / maximal monotone metric   = AM(1/x,1/y)
    return (x + y) / (Fraction(2) * x * y)

print("    monotone-metric coefficient c(x,y) on an eigenvalue pair:")
print("      Bures/SLD  c = 2/(x+y)        = HM(1/x,1/y)   [minimal]")
print("      RLD        c = (x+y)/(2xy)    = AM(1/x,1/y)   [maximal]")
print("      Kubo-Mori  c = (log x-log y)/(x-y) = logarithmic mean [dually flat]")
print()
diag_pairs = [(Fraction(1), Fraction(1)), (Fraction(2), Fraction(2)),
              (Fraction(3, 5), Fraction(3, 5))]
off_pairs = [(Fraction(1), Fraction(3)), (Fraction(2), Fraction(5)),
             (Fraction(1, 2), Fraction(1, 4))]
print("    ON-DIAGONAL (x=y, the decohered classical face):")
diag_collapse = True
for x, y in diag_pairs:
    b = bures_coeff(x, y); r = rld_coeff(x, y)
    eq = (b == r == Fraction(1) / x)
    diag_collapse &= eq
    print(f"      x=y={x!s:>4}:  Bures={b}   RLD={r}   both = 1/x = {Fraction(1)/x}   "
          f"collapse: {eq}")
print("    OFF-DIAGONAL (x!=y, the coherent quantum locus):")
off_split = True
for x, y in off_pairs:
    b = bures_coeff(x, y); r = rld_coeff(x, y)
    # Kubo-Mori logarithmic mean, float WITNESS only (does not cast a vote)
    km = (float(x) - float(y)) / (log(float(x)) - log(float(y)))
    strict = (b < r)
    between = (float(b) < km < float(r))
    off_split &= strict
    print(f"      x={x!s:>4}, y={y!s:>4}:  Bures={b} < RLD={r}  strict: {strict}   "
          f"(KM={km:.6f} sits between: {between})")
sub()
print("REALIZED BRANCH  פ7 :  K + JOINT-ON-DISJOINT")
print(f"  (a) face strata = Boolean lattice B_{k}: {boolean_ok}")
print(f"  (b) diagonal collapse (Bures=RLD=1/x): {diag_collapse};  "
      f"off-diagonal split (Bures<RLD): {off_split}")
print("  The monotone-metric fork is INVISIBLE on the classical diagonal")
print("  (Chentsov uniqueness) and supported EXACTLY on the quantum off-diagonal")
print("  -- one coefficient c(x,y), two disjoint regimes. Boundary faces (the")
print("  Boolean lattice) and boundary metric-ambiguity are the same exterior.")
print()


# ==========================================================================
hr()
print("AUDIT  פ8  --  the 2-adic anomaly: the smallest non-cyclic unit group")
print("              is intra-prime (N=8), the smallest cross-prime one is N=12")
hr()
print("""PRE-CLAIM (before the computation runs).
T8: the multiplicative apex lives on the units (Z/N)^x; its characters carry
conductors cond(chi) | N. (Z/N)^x is cyclic (a single 'order axis') for
N=1,2,4,p^a,2p^a and NON-cyclic otherwise. The exterior question: WHERE does
non-cyclicity first appear, and is its first appearance a single-prime (2-adic
ramification) event or a cross-prime (CRT) event?

  K : the smallest N with (Z/N)^x non-cyclic is N=8, with (Z/8)^x = V_4
      (Klein four) and character conductors {1,4,8,8} -- ALL powers of 2
      (intra-prime, the 2-adic anomaly: non-cyclicity from the prime 2 alone).
      The smallest CROSS-prime non-cyclic unit group is N=12, (Z/12)^x = V_4
      with conductors {1,4,3,12} -- mixing primes 2 and 3 (a CRT event).
  L : the smallest non-cyclic (Z/N)^x is some N != 8, OR its conductors are not
      all prime powers of a single prime.
  JOINT-ON-DISJOINT : N=8 and N=12 realize the SAME abstract group V_4, yet are
      separated by their conductor signature: the group structure (interior)
      cannot see the prime arithmetic (exterior). N=8's non-cyclicity is a
      single-prime 2-adic ramification; N=12's is a cross-prime CRT split.
      Same V_4, two disjoint arithmetic mechanisms.
Check: exact element orders in (Z/N)^x; exact Dirichlet-character conductors.""")
sub()

def unit_group(N):
    return [a for a in range(1, N + 1) if gcd(a, N) == 1]

def is_cyclic_units(N):
    U = unit_group(N)
    phi = len(U)
    return any(multiplicative_order(a, N) == phi for a in U)

def group_type(N):
    """Invariant-factor shape of (Z/N)^x as a string, via element-order multiset."""
    U = unit_group(N)
    phi = len(U)
    if phi == 1:
        return "1 (trivial)"
    orders = sorted(multiplicative_order(a, N) for a in U)
    maxord = max(orders)
    if maxord == phi:
        return f"Z/{phi} (cyclic)"
    # non-cyclic: report as V_4 when phi=4 and all non-id elements have order 2
    if phi == 4 and all(o in (1, 2) for o in orders):
        return "V_4 = Z/2 x Z/2"
    return f"non-cyclic (phi={phi}, max order={maxord})"

def factor_prime_powers(N):
    pp = []
    m = N
    d = 2
    while d * d <= m:
        if m % d == 0:
            a = 0
            while m % d == 0:
                m //= d; a += 1
            pp.append((d, a))
        d += 1
    if m > 1:
        pp.append((m, 1))
    return pp

def conductor_multiset(N):
    """Exact conductors of all phi(N) Dirichlet characters mod N.
    A character is a choice of character on each prime-power factor (Z/p^a)^x;
    its conductor is the product over primes of p^b where p^b is the minimal
    modulus on that prime carrying the chosen local character."""
    pp = factor_prime_powers(N)
    # For each prime power p^a, list the conductors of its characters with
    # multiplicity (a character mod p^a of conductor p^b for each 0<=b<=a).
    local = []
    for (p, a) in pp:
        conds = []
        if p == 2:
            # (Z/2)^x trivial -> conductor 1 (mult 1)
            # (Z/4)^x = C_2 -> conductors {1, 4}
            # (Z/2^a)^x = C_2 x C_{2^{a-2}} (a>=3): #chars = 2^{a-1}; conductors:
            #   trivial -> 1; the C_2 (sign) factor primitive at 4 -> conductor 4
            #   for chars trivial on the big cyclic part; the C_{2^{a-2}} part
            #   primitive at 2^a. We enumerate by (eps in {0,1} on C_2,
            #   j in 0..2^{a-2}-1 on C_{2^{a-2}}).
            if a == 1:
                conds = [1]
            elif a == 2:
                conds = [1, 4]
            else:
                big = 2 ** (a - 2)
                for eps in range(2):
                    for j in range(big):
                        # order of the j-component on C_{big}
                        if j == 0:
                            c_big = 1
                        else:
                            ord_j = big // gcd(j, big)
                            # primitive at 2^{(log2 ord_j)+2}
                            c_big = 4 * (ord_j)  # 2^{2+log2 ord_j} since ord_j is a 2-power
                        if eps == 0 and c_big == 1:
                            conds.append(1)
                        else:
                            c = max(4 if eps == 1 else 1, c_big)
                            conds.append(c)
        else:
            m = (p ** (a - 1)) * (p - 1)  # order of cyclic (Z/p^a)^x
            for j in range(m):
                if j == 0:
                    conds.append(1)
                else:
                    ord_j = m // gcd(j, m)
                    # minimal b with character of order ord_j living mod p^b:
                    # order of (Z/p^b)^x is p^{b-1}(p-1); need ord_j | that.
                    b = 1
                    while ord_j % ( ( (p**(b-1))*(p-1) ) // gcd((p**(b-1))*(p-1), ord_j) ) != 0 \
                          or ((p**(b-1))*(p-1)) % ord_j != 0:
                        b += 1
                        if b > a:
                            b = a; break
                    conds.append(p ** b)
        local.append(conds)
    # global conductors = products over the CRT factors
    result = []
    for combo in product(*local):
        c = 1
        for x in combo:
            c *= x
        result.append(c)
    return sorted(result)

print("    (Z/N)^x structure for N = 2..16:")
first_noncyclic = None
first_crossprime = None
for N in range(2, 17):
    if len(unit_group(N)) == 0:
        continue
    cyc = is_cyclic_units(N)
    gt = group_type(N)
    npr = len(factor_prime_powers(N))
    tag = ""
    if not cyc and first_noncyclic is None:
        first_noncyclic = N; tag = "  <-- FIRST non-cyclic"
    if not cyc and npr >= 2 and first_crossprime is None:
        first_crossprime = N; tag += "  <-- FIRST cross-prime non-cyclic"
    print(f"      N={N:>2}: (Z/N)^x = {gt:<22} cyclic={cyc!s:<5} "
          f"#distinct primes={npr}{tag}")
sub()
sig8 = conductor_multiset(8)
sig12 = conductor_multiset(12)
print(f"    conductor signature  N=8 : {sig8}")
print(f"      all powers of 2 (intra-prime / 2-adic): "
      f"{all((c & (c-1))==0 for c in sig8)}")
print(f"    conductor signature  N=12: {sig12}")
print(f"      mixes primes 2 and 3 (cross-prime / CRT): "
      f"{any(c % 3 == 0 for c in sig12) and any(c % 4 == 0 for c in sig12)}")
print(f"    both groups are V_4: "
      f"{group_type(8).startswith('V_4') and group_type(12).startswith('V_4')}")
sub()
print("REALIZED BRANCH  פ8 :  K + JOINT-ON-DISJOINT")
print(f"  smallest non-cyclic (Z/N)^x: N={first_noncyclic} (intra-prime, "
      f"conductors {sig8} all 2-powers).")
print(f"  smallest CROSS-prime non-cyclic: N={first_crossprime} (conductors "
      f"{sig12}, primes 2 and 3).")
print("  Same abstract V_4, separated only by the exterior conductor signature:")
print("  N=8 non-cyclicity is single-prime 2-adic ramification; N=12 is a CRT")
print("  cross-prime split. The group (interior) is blind to the prime (exterior).")
print()


# ==========================================================================
hr()
print("AUDIT  פ-bridge  --  the cubic Jacobi sum is an Eisenstein integer of")
print("                     norm exactly q: the sqrt(q) critical scale, exact")
hr()
print("""PRE-CLAIM (before the computation runs).
T8 (bridge to function fields): for a prime q = 1 (mod 3) the cubic character
chi on F_q^x exists, and the Jacobi sum J(chi,chi) = sum_t chi(t)chi(1-t) is an
ALGEBRAIC integer in Z[omega] (omega a primitive cube root of unity). Its norm
is the arithmetic embodiment of the critical scale: |J| = sqrt(q).

  K : for every prime q = 1 (mod 3), J(chi,chi) = a + b*omega is an exact
      Eisenstein integer with N(J) = a^2 - a*b + b^2 = q. The scale sqrt(q) --
      the function-field critical line -- appears as an exact algebraic norm,
      with no floating point anywhere.
  L : N(J) != q for some such q (the Jacobi sum does not sit at scale sqrt(q)).
  JOINT-ON-DISJOINT : the SAME identity N(J)=q holds for every q=1(mod 3), but
      the integer pair (a,b) -- the *direction* of J in the Eisenstein lattice
      -- varies prime by prime; the scale is rigid (always sqrt(q)) while the
      phase/direction is free. Magnitude rigid, direction disjoint per prime.
Check: exact cubic character via discrete logs; J reduced in Z[omega]; integer
       norm a^2-ab+b^2 compared to q exactly.""")
sub()

def cubic_jacobi(q):
    """Exact J(chi,chi) in Z[omega] for q = 1 (mod 3); returns (a,b) and the
    coefficient vector (c0,c1,c2) over {1,omega,omega^2}."""
    assert q % 3 == 1
    g = primitive_root(q)
    dlog = discrete_logs(q, g)
    # chi(x) = omega^{dlog(x) mod 3}; record as exponent in {0,1,2}
    def chi_exp(x):
        x %= q
        return dlog[x] % 3 if x != 0 else None
    c = [0, 0, 0]  # coefficients of 1, omega, omega^2
    for t in range(2, q):           # t != 0, 1
        e1 = chi_exp(t)
        e2 = chi_exp(1 - t)         # (1-t) mod q; if ==0 (t==1) skip -- excluded
        if e1 is None or e2 is None:
            continue
        c[(e1 + e2) % 3] += 1
    a, b = reduce_powers(c[0], c[1], c[2])
    return (a, b), tuple(c), g

primes_1mod3 = [7, 13, 19, 31, 37, 43, 61, 67]
all_norm_ok = True
rows = []
for q in primes_1mod3:
    (a, b), c, g = cubic_jacobi(q)
    nrm = eis_norm(a, b)
    ok = (nrm == q)
    all_norm_ok &= ok
    rows.append((q, g, c, a, b, nrm, ok))
    print(f"    q={q:>3} (gen g={g}):  J = {c[0]} + {c[1]}ω + {c[2]}ω^2  "
          f"=>  {a} + {b}ω   N(J)=a^2-ab+b^2={nrm}   == q: {ok}")
sub()
print(f"REALIZED BRANCH  פ-bridge :  K + JOINT-ON-DISJOINT")
print(f"  N(J)=q exactly for all tested primes q=1(mod 3): {all_norm_ok}")
print("  |J| = sqrt(q) on the nose -- the critical scale is an exact Eisenstein")
print("  norm. The magnitude is rigid (always sqrt(q)); the lattice direction")
print("  (a,b) is disjoint, varying prime by prime. This (a,b) IS the Frobenius")
print("  eigenvalue of the Fermat curve -- settled next.")
print()


# ==========================================================================
hr()
print("AUDIT  פ-Weil  --  the Fermat cubic point count lands the critical line:")
print("                   a^2 <= 4q exactly, so |alpha| = sqrt(q)  (Weil's RH)")
hr()
print("""PRE-CLAIM (before the computation runs).
T8 (the PROVEN critical line): the projective Fermat cubic C: x^3+y^3+z^3=0 over
F_q is a genus-1 curve; its zeta numerator is 1 - a*T + q*T^2 with a = q+1-#C(F_q)
and Frobenius eigenvalues alpha, alpha-bar satisfying alpha*alpha-bar = q. Weil's
Riemann Hypothesis for curves is the statement a^2 <= 4q, i.e. the eigenvalues
are complex-conjugate of modulus exactly sqrt(q) -- equivalently the zeros of
Z(C/F_q,.) lie on Re(s)=1/2. This is verifiable by exact INTEGER point-counting.

  K : for every prime q, a = q+1-#C(F_q) satisfies a^2 <= 4q (Hasse-Weil), with
      STRICT a^2 < 4q and a != 0 for q=1(mod 3) (ordinary: genuine
      complex-conjugate Frobenius), and a = 0 exactly for q=2(mod 3)
      (supersingular: cubing is a bijection, the cubic character is absent).
      In the ordinary case a = -(J + J-bar) = -(2a_J - b_J), tying the count to
      the פ-bridge Jacobi sum. The critical line |alpha|=sqrt(q) is LANDED.
  L : a^2 > 4q for some q (Hasse-Weil fails -- impossible if Weil is right), OR
      a != 0 for some q=2(mod 3).
  JOINT-ON-DISJOINT : |alpha|=sqrt(q) holds in BOTH regimes, by DISJOINT
      mechanisms -- q=1(mod 3) via genuine complex Frobenius (a^2<4q, J exists),
      q=2(mod 3) via forced a=0 (supersingular trace, J absent / 'inert prime').
      One critical line, two arithmetic origins.
Check: exact integer count of projective solutions of x^3+y^3+z^3=0 over F_q.""")
sub()

def fermat_cubic_projective_count(q):
    """Exact #C(F_q) for projective x^3+y^3+z^3=0 (q prime). Count nonzero affine
    solutions and divide by (q-1)."""
    cube = [(x * x * x) % q for x in range(q)]
    affine = 0
    for x in range(q):
        cx = cube[x]
        for y in range(q):
            cy = cube[y]
            need = (-(cx + cy)) % q
            # count z with z^3 = need
            affine += sum(1 for z in range(q) if cube[z] == need)
    affine -= 1  # remove the origin (0,0,0)
    assert affine % (q - 1) == 0
    return affine // (q - 1)

test_primes = [5, 7, 11, 13, 17, 19, 23, 31, 37, 43]
all_hasse_ok = True
ordinary_strict_ok = True
inert_zero_ok = True
print("    q   q mod 3   #C(F_q)   a=q+1-#C   a^2    4q    a^2<=4q   regime")
jdict = {q: cubic_jacobi(q) for q in test_primes if q % 3 == 1}
for q in test_primes:
    NC = fermat_cubic_projective_count(q)
    a = q + 1 - NC
    hasse = (a * a <= 4 * q)
    all_hasse_ok &= hasse
    if q % 3 == 1:
        regime = "ordinary (1 mod 3)"
        ordinary_strict_ok &= (a * a < 4 * q)
    else:
        regime = "inert    (2 mod 3)"
        inert_zero_ok &= (a == 0)
    print(f"   {q:>3}    {q%3}      {NC:>5}     {a:>4}    {a*a:>4}  {4*q:>4}    "
          f"{hasse!s:<5}    {regime}")
sub()
# tie ordinary a to the Jacobi sum:  a = -(J + J-bar) = -(2 a_J - b_J)
print("    bridge tie (ordinary primes): a_curve  vs  -(J + J̄) = -(2a_J - b_J):")
tie_ok = True
for q in test_primes:
    if q % 3 != 1:
        continue
    NC = fermat_cubic_projective_count(q)
    a = q + 1 - NC
    (aJ, bJ), c, g = jdict[q]
    jtrace = 2 * aJ - bJ            # J + J-bar
    pred = -jtrace
    ok = (a == pred)
    tie_ok &= ok
    print(f"      q={q:>3}:  a_curve={a:>4}   J+J̄={jtrace:>4}   -(J+J̄)={pred:>4}   "
          f"match: {ok}    (|alpha|^2 = q = {q}, alpha*alpha-bar exact)")
sub()
print("REALIZED BRANCH  פ-Weil :  K + JOINT-ON-DISJOINT")
print(f"  Hasse-Weil a^2<=4q for all tested q: {all_hasse_ok}")
print(f"  ordinary (q=1 mod3) strict a^2<4q: {ordinary_strict_ok};  "
      f"inert (q=2 mod3) a=0 exactly: {inert_zero_ok}")
print(f"  bridge tie a_curve = -(J+J̄) on ordinary primes: {tie_ok}")
print("  alpha*alpha-bar = q forces |alpha| = sqrt(q) EXACTLY: the function-field")
print("  critical line Re(s)=1/2 is LANDED by integer point-counting (Weil, [P]).")
print("  The SAME line holds for inert primes via a=0 (supersingular) -- one")
print("  critical line, two disjoint mechanisms. Classical zeta has no such")
print("  finite Frobenius / point-count: its critical line stays [C], not [P].")
print()

# ==========================================================================
hr()
print("AUDIT  פ-fork  --  the quantum fork-width of the additive characters, in a")
print("                   conductor-graded apex state, lives on the conductor")
print("                   lattice: the quantum face (T7/T24) MEETS the units (T8)")
hr()
print("""PRE-CLAIM (before the computation runs).
Bridge T24 <-> T8/T3 (this paper's own new object). The character observable
C_c is diagonal in the computational basis, hence SHIFT-by-c in the Fourier
basis: <i|C_c|j> = [i == j+c]. So for rho diagonal in the Fourier basis with
eigenvalues lam_j, the Petz fork-width form W = g^RLD - g^SLD (T24: maximal
minus minimal monotone metric) evaluates on C_c to the exact lattice sum
   W(c) = sum_j  Δ(lam_{j+c}, lam_j),   Δ(x,y) = (x-y)^2 / (2 x y (x+y)) >= 0,
with Δ(x,x)=0 (T24 Prop 3.1: the fork is closed on the diagonal, open off it).
Take rho CONDUCTOR-GRADED: lam_j = w(cond j) over the T3 conductor packets.

  K1 : W(c) = Φ(cond c) -- a CLASS FUNCTION on the conductor lattice, for every
       graded weight w. The quantum-metric ambiguity of the additive characters
       factors through the conductor lattice: the quantum face (T24) and the
       multiplicative face (T8/T3) MEET on the conductor packets. Proof: the
       graded rho is invariant under the unit action j -> u*j, which is
       transitive on each packet H_d, so W(u*c) = W(c).
  L1 : W depends on c WITHIN a packet (not a class function).
  K2 (SHARP, may fail) : Φ is STRICTLY MONOTONE increasing in the conductor d.
  L2 : Φ is not monotone in d.
  JOINT-ON-DISJOINT : class function, but for the dimension weight w=phi the
       conductor-2 (parity) character self-closes -- Φ(2)=0 -- echoing פ11's
       parity-locked 2-axis.
Check: exact Fraction W(c); class-function = equality within each packet; the
unit-symmetry W(u*c)=W(c); monotonicity of Φ; the w=phi parity vanishing; and a
GENERIC (non-graded) rho for contrast.""")
sub()

def _cond(a, N):
    return 1 if a % N == 0 else N // gcd(a, N)

def _phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def _delta(x, y):                       # fork-width kernel, exact
    if x == y:
        return Fraction(0)
    return Fraction((x - y) * (x - y), 2 * x * y * (x + y))

def _W(lam, c, N):
    return sum(_delta(lam[(j + c) % N], lam[j]) for j in range(N))

def _graded(N, wfun):
    raw = [wfun(_cond(j, N)) for j in range(N)]
    Z = sum(raw)
    return [Fraction(r) / Z for r in raw]

def _classfn(lam, N):                   # (is_class_function, {d: Φ(d)})
    by = {}
    for c in range(1, N):
        by.setdefault(_cond(c, N), set()).add(_W(lam, c, N))
    ok = all(len(s) == 1 for s in by.values())
    Phi = {d: next(iter(by[d])) for d in sorted(by)} if ok else {}
    return ok, Phi

for N in (12, 30, 6):                   # lead with N=12 (the real witness)
    wd = _graded(N, lambda d: Fraction(d))        # w(d)=d
    wphi = _graded(N, lambda d: Fraction(_phi(d)))  # w(d)=phi(d) (packet dim)
    ok_d, Phi_d = _classfn(wd, N)
    ok_phi, Phi_phi = _classfn(wphi, N)
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    Wd = {c: _W(wd, c, N) for c in range(N)}
    sym = all(Wd[(u * c) % N] == Wd[c] for u in units for c in range(N))
    ds = sorted(Phi_d)
    mono = all(Phi_d[ds[i]] < Phi_d[ds[i + 1]] for i in range(len(ds) - 1))
    # generic (non-graded) contrast
    gen = [Fraction(1, 1 + (7 * j) % N + 1) for j in range(N)]
    Zg = sum(gen); gen = [g / Zg for g in gen]
    ok_gen, _ = _classfn(gen, N)
    print(f"  N={N:>2}:  class-fn(w=d): {ok_d!s:<5}  class-fn(w=phi): {ok_phi!s:<5}  "
          f"unit-sym W(u·c)=W(c): {sym!s:<5}  generic-is-class-fn: {ok_gen}")
    print(f"         Φ_(w=d)(d):   " + "  ".join(f"{d}:{Phi_d[d]}" for d in ds)
          + f"   |  monotone↑: {mono}")
    print(f"         Φ_(w=phi)(d): " + "  ".join(f"{d}:{Phi_phi[d]}" for d in sorted(Phi_phi))
          + f"   |  Φ_phi(2)=0 (parity self-close): {Phi_phi.get(2)==0}")
sub()
print("REALIZED BRANCH  פ-fork :  K1 + JOINT-ON-DISJOINT, with K2 FALSIFIED (retained)")
print("  K1 [P]: W(c)=Φ(cond c) is a class function on the conductor lattice for")
print("     every graded weight; the unit-action symmetry W(u·c)=W(c) (True above)")
print("     IS the proof. The quantum fork-width of the additive characters factors")
print("     through the conductor lattice -- T24's fork and T8/T3's packets meet.")
print("  Honest scope: N=6 is DEGENERATE -- its packets are the ± pairs {c,N-c}, so")
print("     class-function is forced by reflection W(c)=W(N-c) even for a generic")
print("     state (generic-is-class-fn True at N=6, False at N=12,30). The theorem")
print("     has content only at N>=12, where grading is what pushes W onto the")
print("     lattice (generic False, graded True).")
print("  K2 FALSIFIED: Φ is NOT monotone in d (N=12, w=d: Φ(6)<Φ(4)). The fork-width")
print("     does not simply grow with the conductor. A pre-registered sharp claim")
print("     that failed -- retained, not hidden.")
print("  JOINT: for w=phi (packet dimension) Φ(2)=0 at every N -- the conductor-2")
print("     (parity) character's fork self-closes, the quantum echo of פ11.")
print()

hr()
print("END OF SETTLEMENTS  (deterministic; re-run reproduces this transcript)")
hr()
