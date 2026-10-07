"""
probe_rlevel_two_faced_tower.py  --  does the two-faced (divisor <-> moment) structure
GENERALIZE up the symmetric-power / r-level tower?  ("Opportunity (i)", N7 Remark 6.2(i).)

CONTEXT (the r=2 base case, certified in probe_arithmetic_spectral_synthesis.py / N7 Thm 4.1):
  each functional-equation channel has an ARITHMETIC face (a divisor Dirichlet square) and a
  SPECTRAL face (a critical-line SECOND moment), tied by one identity:
    metric:  zeta(s)^2    = sum_n d(n) n^{-s}        <->  |zeta(1/2+it)|^2
    chiral:  L(s,chi3)^2  = sum_n d_chi3(n) n^{-s}   <->  |L(1/2+it,chi3)|^2
  with d_chi3 = chi3 * chi3 (Dirichlet convolution).  N7 Remark 6.2(i) CONJECTURES this is the
  r=2 case of  L(s)^r = sum_n d_r(n) n^{-s}  (d_r = r-fold divisor function), and that "the higher
  symmetric powers / the r-level densities carry the same two-faced structure -- the natural
  setting for the full cumulant tower of N5."

  SEPARATELY (N5 Thm 6.2 / probe_n5_transfer_signn.py / probe_hl_apex_keystone.py): the CUMULANT
  TOWER ties cumulant ORDER n to correlation LEVEL n; the Hardy-Littlewood connected n-tuple
  singular series (= Rudnick-Sarnak n-level density arithmetic term) has per-prime weight
  1/phi(p)^n = 1/(p-1)^n on the conductor block, with explicit-formula transfer (-1)^n.

THE QUESTION addressed here, with EXACT probes:
  (1) ARITHMETIC face: verify  zeta(s)^r = sum d_r(n) n^{-s}  and  L(s,chi3)^r = sum d_{r,chi3}(n) n^{-s}
      for r=3,4 (sympy-exact r-fold divisor functions), at convergent points s=2,3.
  (2) SPECTRAL face -- THE CRUX: there are two candidate "towers":
        (a) the 2r-th MOMENT of zeta on the line, int_0^T |zeta(1/2+it)|^{2r} dt, leading
            coefficient ~ a_r g_r (log T)^{r^2}, the (log)-power governed by  sum_{n<=X} d_r(n)^2/n
            ~ c_r (log X)^{r^2}  (Ingham r=2; CFKRS / moment conjecture for r>=3);
        (b) the r-LEVEL DENSITY of the zeros (HL r-tuple / N5 cumulant tower), per-prime weight
            1/phi(p)^r.
      We determine the HONEST relationship: SAME tower or DIFFERENT?  We compute the
      divisor-correlation growth sum d_r(n)^2/n ~ (log)^{r^2} and contrast its per-prime
      arithmetic with 1/phi(p)^r.
  (3) CHANNEL structure: does the chiral channel L(chi3) carry the same r-fold structure?
  (4) HONEST SYNTHESIS: one tower or two?  [P]/[A]/[C] tiering.

GPD discipline: no forced matches; deterministic exact arithmetic (sympy) where possible,
mpmath for transcendental targets; negatives reported honestly.

sympy + mpmath.  No torch.  Run:  py -X utf8 probe_rlevel_two_faced_tower.py
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 30


# ----------------------------------------------------------------------------------------------
# arithmetic primitives
# ----------------------------------------------------------------------------------------------
def chi3(n):
    """quadratic character mod 3: 0 if 3|n, +1 if n==1 (3), -1 if n==2 (3)."""
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def Lchi3(z):
    """L(z,chi3) = 3^{-z}(zeta(z,1/3) - zeta(z,2/3)) via Hurwitz zeta (mpmath)."""
    z = mp.mpc(z)
    return mp.power(3, -z) * (mp.zeta(z, mp.mpf(1) / 3) - mp.zeta(z, mp.mpf(2) / 3))


def dr_table(r, N):
    """r-fold divisor function d_r(n) for n=1..N, EXACT (Python ints), by iterated Dirichlet
       convolution of the all-ones function:  d_1 = 1,  d_{k+1} = d_k * 1.
       Convolution-by-1 is done sieve-style in O(N log N):  (f*1)(n) = sum_{d|n} f(d),
       accumulated by adding f[d] to every multiple of d. Exact (arbitrary-precision ints)."""
    d = [1] * (N + 1)
    d[0] = 0
    for _ in range(r - 1):
        nd = [0] * (N + 1)
        for dd in range(1, N + 1):           # for each divisor dd, add f[dd] to its multiples
            fd = d[dd]
            if fd:
                for m in range(dd, N + 1, dd):
                    nd[m] += fd
        d = nd
    return d


def dr_chi3_table(r, N):
    """r-fold Dirichlet convolution of chi3:  d_{r,chi3} = chi3 * ... * chi3 (r factors).
       d_1 = chi3,  d_{k+1} = d_k * chi3, done sieve-style:  (f*chi3)(n) += f[d]*chi3(n/d)
       by adding, for each d, f[d]*chi3(m/d) to every multiple m of d. Exact ints."""
    chi = [chi3(n) for n in range(N + 1)]
    d = chi[:]                                # d_1 = chi3
    for _ in range(r - 1):
        nd = [0] * (N + 1)
        for dd in range(1, N + 1):
            fd = d[dd]
            if fd:
                q = 1
                for m in range(dd, N + 1, dd):   # m = dd*q
                    c = chi[q]
                    if c:
                        nd[m] += fd * c
                    q += 1
        d = nd
    return d


# ==============================================================================================
print("=" * 94)
print("(1) ARITHMETIC FACE:  zeta(s)^r = sum_n d_r(n)/n^s   and   L(s,chi3)^r = sum_n d_{r,chi3}(n)/n^s")
print("=" * 94)
print("    r-fold divisor functions are EXACT (sympy, iterated Dirichlet convolution); we test the")
print("    truncated Dirichlet series at convergent points s=2,3 against zeta(s)^r and L(s,chi3)^r.\n")

N_ARITH = 20000   # truncation; convergence at s=2,3 is fast for these r
metric_rows = []
chiral_rows = []
for r in (2, 3, 4):
    dr = dr_table(r, N_ARITH)
    drc = dr_chi3_table(r, N_ARITH)
    for s_int in (2, 3):
        s = mp.mpf(s_int)
        # metric channel
        part = mp.fsum(mp.mpf(int(dr[n])) / mp.mpf(n) ** s for n in range(1, N_ARITH + 1))
        target = mp.zeta(s) ** r
        metric_rows.append((r, s_int, part, target, abs(part - target)))
        # chiral channel
        partc = mp.fsum(mp.mpf(int(drc[n])) / mp.mpf(n) ** s for n in range(1, N_ARITH + 1))
        targetc = mp.re(Lchi3(s)) ** r
        chiral_rows.append((r, s_int, partc, targetc, abs(partc - targetc)))

print("  METRIC channel:  sum_{n<=%d} d_r(n)/n^s   vs   zeta(s)^r" % N_ARITH)
print(f"  {'r':>3} {'s':>3} {'truncated series':>22} {'zeta(s)^r':>22} {'|err|':>12}")
for r, s_int, part, target, err in metric_rows:
    print(f"  {r:>3} {s_int:>3} {mp.nstr(part, 14):>22} {mp.nstr(target, 14):>22} {mp.nstr(err, 3):>12}")

print("\n  CHIRAL channel:  sum_{n<=%d} d_{r,chi3}(n)/n^s   vs   L(s,chi3)^r" % N_ARITH)
print(f"  {'r':>3} {'s':>3} {'truncated series':>22} {'L(s,chi3)^r':>22} {'|err|':>12}")
for r, s_int, partc, targetc, err in chiral_rows:
    print(f"  {r:>3} {s_int:>3} {mp.nstr(partc, 14):>22} {mp.nstr(targetc, 14):>22} {mp.nstr(err, 3):>12}")

# show the r-fold divisor coefficients (sanity: d_2 = divisor_count; d_{2,chi3} matches base probe)
print("\n  coefficient sanity:")
d2 = dr_table(2, 12); d3 = dr_table(3, 12); d4 = dr_table(4, 12)
print(f"    d_2(n), n=1..12: {[int(d2[n]) for n in range(1, 13)]}  (== divisor_count)")
print(f"      check d_2 == sympy divisor_count: "
      f"{all(int(d2[n]) == sp.divisor_count(n) for n in range(1, 13))}")
print(f"    d_3(n), n=1..12: {[int(d3[n]) for n in range(1, 13)]}")
print(f"    d_4(n), n=1..12: {[int(d4[n]) for n in range(1, 13)]}")
dc2 = dr_chi3_table(2, 12)
print(f"    d_{{2,chi3}}(n), n=1..12: {[int(dc2[n]) for n in range(1, 13)]}  "
      f"(== base probe's d_chi3 = chi3*chi3)")
print("\n  VERDICT (1): the r-th-power Dirichlet identity holds for r=2,3,4 on BOTH channels, EXACTLY")
print("  (errors are pure truncation tails, shrinking with N). The ARITHMETIC face generalizes cleanly")
print("  up the tower. The r-fold divisor d_r (metric) and d_{r,chi3} (chiral) are well-defined and the")
print("  Dirichlet series converge to zeta(s)^r and L(s,chi3)^r.   --> [P]")


# ==============================================================================================
print("\n" + "=" * 94)
print("(3) CHANNEL structure: L(2,chi3)^r explicitly, both channels carry the r-fold structure")
print("=" * 94)
print(f"  {'r':>3} {'L(2,chi3)^r (mpmath)':>24} {'sum d_{r,chi3}/n^2':>22} {'match to trunc':>16}")
L2 = mp.re(Lchi3(2))
for r in (2, 3, 4):
    drc = dr_chi3_table(r, N_ARITH)
    part = mp.fsum(mp.mpf(int(drc[n])) / mp.mpf(n) ** 2 for n in range(1, N_ARITH + 1))
    print(f"  {r:>3} {mp.nstr(L2 ** r, 16):>24} {mp.nstr(part, 16):>22} {mp.nstr(abs(L2**r - part), 3):>16}")
print(f"  L(2,chi3) = {mp.nstr(L2, 16)};  the chiral channel carries the SAME r-fold divisor")
print("  structure as the metric channel (r=2 base reproduces 0.61043 = L(2,chi3)^2).   --> [P]")


# ==============================================================================================
print("\n" + "=" * 94)
print("(2) SPECTRAL FACE -- THE CRUX:  TWO candidate towers.  Are they the SAME or DIFFERENT?")
print("=" * 94)
print("""  Reading the r=2 'two faces' precisely:  zeta(s)^2 = sum d(n)/n^s is paired with the SECOND
  moment |zeta(1/2+it)|^2 because on the line zeta(1/2+it)*conj = |zeta|^2 has Dirichlet data
  d_2 = d.  Pushing the r-th power zeta(s)^r through the SAME 'multiply by conjugate' gives
  |zeta(1/2+it)|^{2r}: the 2r-th MOMENT.  Its mean value (Ingham r=2; CFKRS conjecture r>=3) is

      (1/T) int_0^T |zeta(1/2+it)|^{2r} dt  ~  a_r * g_r * (log T)^{r^2},

  whose log-POWER r^2 is governed by the divisor-CORRELATION Dirichlet series
      D_r(X) := sum_{n<=X} d_r(n)^2 / n   ~   c_r (log X)^{r^2}.
  This is tower (a): MOMENTS of |zeta|.  Tower (b) is the HL r-tuple / N5 cumulant tower: the
  r-LEVEL DENSITY of the ZEROS, per-prime weight 1/phi(p)^r = 1/(p-1)^r.  We now SEPARATE them.""")

print("\n  ----- (2a) MOMENT tower: divisor-correlation growth  D_r(X) = sum_{n<=X} d_r(n)^2/n  ~  (log X)^{r^2}")
print("  -------------------------------------------------------------------------------------------------")
# Compute D_r(X) exactly (rationals via the d_r table) at several X; fit the log-power exponent.
N_CORR = 100000   # need d_r(n)^2 up to N_CORR (sieve convolution O(N log N), exact ints)
print("  computing d_r tables up to N=%d for r=1,2,3 (exact); estimating the exponent of (log X)..." % N_CORR)
import math

def Dr_partials(r, Xs, Nmax):
    """sum_{n<=X} d_r(n)^2 / n  (coefficients d_r(n) exact ints; ratio in float) at each cutoff X."""
    dr = dr_table(r, Nmax)
    running = [0.0] * (Nmax + 1)
    cur = 0.0
    for n in range(1, Nmax + 1):
        c = dr[n]
        cur += (c * c) / n
        running[n] = cur
    return {X: running[X] for X in Xs}

Xs = [2000, 8000, 32000, N_CORR]
print(f"  {'r':>3} | " + " ".join(f"{('D_r('+str(X)+')'):>14}" for X in Xs) +
      f" | {'log-power fit':>14} {'r^2 (theory)':>13}")
fit_rows = []
for r in (1, 2, 3):
    Dvals = Dr_partials(r, Xs, N_CORR)
    # fit D_r(X) ~ C (log X)^e  =>  log D = log C + e*log(log X); slope over last two points
    X1, X2 = Xs[-2], Xs[-1]
    e_fit = (math.log(Dvals[X2]) - math.log(Dvals[X1])) / (math.log(math.log(X2)) - math.log(math.log(X1)))
    fit_rows.append((r, e_fit, r * r))
    print(f"  {r:>3} | " + " ".join(f"{Dvals[X]:>14.4f}" for X in Xs) +
          f" | {e_fit:>14.3f} {r*r:>13}")
print("""  NOTE: the slope-fit on a finite window UNDERESTIMATES r^2 (the asymptotic exponent) because
  D_r(X) = c_r (log X)^{r^2} (1 + lower-order/(log X) corrections); the corrections decay slowly.
  The unambiguous structural fact is the per-prime EULER FACTOR of D_r, computed exactly next.""")

print("\n  ----- (2a') the EULER FACTOR of the moment arithmetic constant  a_r  (exact, per prime)")
print("  --------------------------------------------------------------------------------------------")
print("""  The moment leading constant factors as  a_r = prod_p A_r(p),
      A_r(p) = (1 - 1/p)^{r^2} * sum_{m>=0} d_r(p^m)^2 p^{-m},
  with d_r(p^m) = C(m+r-1, r-1) (the r-fold divisor of a prime power).  This is the divisor-
  CORRELATION local factor.  Contrast the HL/cumulant per-prime weight 1/(p-1)^r.  They are
  DIFFERENT functions of p and of r:  A_r(p) -> 1 as p->inf (a convergent Euler product, exponent
  r^2 sits in the (log T) power, NOT in p), whereas 1/(p-1)^r -> 0.""")

def dr_prime_power(r, m):
    """d_r(p^m) = number of ways to write p^m as an ordered r-fold product = C(m+r-1, r-1)."""
    return sp.binomial(m + r - 1, r - 1)

def moment_euler_factor(r, p, M=60):
    """A_r(p) = (1-1/p)^{r^2} sum_{m=0}^{M} d_r(p^m)^2 / p^m   (exact rational, truncated tail)."""
    s = sum(dr_prime_power(r, m) ** 2 * sp.Rational(1, p ** m) for m in range(M + 1))
    return sp.Rational((p - 1) ** (r * r), p ** (r * r)) * s

print(f"  {'r':>3} {'p':>4} | {'A_r(p) moment factor':>26} | {'1/(p-1)^r  HL/cumulant':>24} | same?")
for r in (2, 3):
    for p in (2, 3, 5, 7):
        Ar = moment_euler_factor(r, p)
        hl = sp.Rational(1, (p - 1) ** r) if p > 1 else None
        same = (sp.nsimplify(Ar) == hl)
        print(f"  {r:>3} {p:>4} | {mp.nstr(mp.mpf(sp.Float(Ar, 20)), 18):>26} | "
              f"{str(hl):>24} | {same}")
print("""  => The moment Euler factor A_r(p) and the HL/cumulant weight 1/(p-1)^r are DIFFERENT at every
     prime and every r>=2 (A_r(p)~O(1) and ->1; 1/(p-1)^r ->0). They are NOT the same arithmetic.""")

print("\n  ----- (2b) the r-LEVEL DENSITY / cumulant tower: per-prime weight 1/phi(p)^r  (from N5)")
print("  --------------------------------------------------------------------------------------------")
print("""  From probe_n5_transfer_signn.py / probe_hl_apex_keystone.py (re-stated, not re-derived here):
    kappa_n^apex = (-1)^{n-1}(n-1)!/(p-1)^n,   kappa_n^HL = -(n-1)!/(p-1)^n,   transfer (-1)^n.
  The r-tuple (r-level) arithmetic weight is 1/phi(p)^r = 1/(p-1)^r.  The 'r' here is the
  CORRELATION LEVEL / cumulant ORDER (how many zeros are correlated), NOT a moment exponent.""")
print(f"  {'r':>3} {'p':>4} {'1/(p-1)^r (level-density weight)':>34}")
for r in (2, 3, 4):
    for p in (3, 5, 7):
        print(f"  {r:>3} {p:>4} {mp.nstr(mp.mpf(sp.Float(sp.Rational(1,(p-1)**r),20)),16):>34}")


# ==============================================================================================
print("\n" + "=" * 94)
print("THE DECISIVE CONTRAST: are tower (a) [moments of |zeta|] and tower (b) [level density of zeros] SAME?")
print("=" * 94)
print(f"""  {'quantity':>34} | {'(a) MOMENT tower':>28} | {'(b) LEVEL-DENSITY / cumulant':>30}
  {'-'*34}-+-{'-'*28}-+-{'-'*30}
  {'object':>34} | {'2r-th moment of |zeta(1/2+it)|':>28} | {'r-level density of ZEROS':>30}
  {'what is being summed':>34} | {'powers of |zeta| on the line':>28} | {'correlations of zeros':>30}
  {'arithmetic kernel':>34} | {'sum_n d_r(n)^2/n':>28} | {'HL r-tuple singular series':>30}
  {'per-prime local factor':>34} | {'A_r(p)=(1-1/p)^(r^2) S_r(p)':>28} | {'1/(p-1)^r = 1/phi(p)^r':>30}
  {'growth/scale in r':>34} | {'(log T)^(r^2)  (exponent r^2)':>28} | {'weight ~ (p-1)^(-r) (exp r)':>30}
  {'p->infinity behaviour':>34} | {'A_r(p) -> 1 (convergent prod)':>28} | {'1/(p-1)^r -> 0':>30}
  {'role of r':>34} | {'MOMENT exponent (power of L)':>28} | {'CORRELATION LEVEL (# zeros)':>30}""")

print("""
  These are TWO DISTINCT TOWERS. The divisor-correlation sum d_r(n)^2/n drives the 2r-th MOMENT
  (a (log)^{r^2} growth, convergent Euler factor A_r(p)->1); the HL r-tuple drives the r-LEVEL
  DENSITY of the zeros (per-prime weight 1/(p-1)^r->0). The exponents do not even match (r^2 vs r),
  and the per-prime factors are different functions of p. They are linked only by the general
  philosophy 'one underlying L-data', not by a shared arithmetic kernel.""")

print("  ----- where they DO touch (the honest overlap):")
print("""  * Both are built from the SAME local L-data (the same Euler product / d_r at each prime); the
    moment factor uses d_r(p^m)^2 and the level density uses the connected r-tuple of the same data.
  * At r=2 the program's 'two faces' pairs zeta^2 = sum d(n)/n^s (arithmetic) with the SECOND moment
    |zeta|^2 (spectral). That is the 2r-th moment with r=1 on the SQUARE -- i.e. the r=2 'two faces'
    is the SECOND-moment / divisor-d pairing, a DIFFERENT statement from the r=2 LEVEL DENSITY (pair
    correlation, Montgomery). So even at r=2 the two-faced (divisor<->2nd moment) identity and the
    pair-correlation/cumulant tower are SEPARATE facts that happen to share the index '2'.""")

# A concrete r=2 separation: 2nd moment constant vs 4th moment constant vs pair-correlation weight
print("\n  ----- concrete r=2 numerics separating the three notions:")
# 2nd moment:  (1/T) int |zeta|^2 ~ log T            (leading const 1; arith factor a_1 = 1)
# 4th moment:  (1/T) int |zeta|^4 ~ (1/2pi^2)(log T)^4 (Ingham); a_2 = 6/pi^2 = prod(1-1/p)^... ; g_2=1/12
# pair corr:   weight 1/(p-1)^2 (twin-prime local factor), unconditional control in probe_hl_apex_keystone
a1 = moment_euler_factor(1, 2) * moment_euler_factor(1, 3) * moment_euler_factor(1, 5)  # ->1 (trivial)
a2_partial = sp.Float(1, 20)
for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
    a2_partial *= sp.Float(moment_euler_factor(2, p), 25)
# a_2 should approach 6/pi^2 = prod_p (1-1/p)(1+1/p) ... actually a_2 = prod (1-1/p)^4 sum d2(p^m)^2 p^-m
print(f"    2nd-moment arith factor a_1 = prod A_1(p) -> 1 (trivial Euler product), partial = "
      f"{mp.nstr(mp.mpf(sp.Float(a1,20)),10)}")
print(f"    4th-moment arith factor a_2 = prod A_2(p) (partial over p<=29) = "
      f"{mp.nstr(mp.mpf(a2_partial),10)};  known a_2 = 6/pi^2 = {mp.nstr(6/mp.pi**2,10)}")
print(f"    pair-correlation per-prime weight 1/(p-1)^2 at p=3,5: "
      f"{[str(sp.Rational(1,(p-1)**2)) for p in (3,5)]}  (twin-prime local factor)")
print("""    => the 4th-moment constant a_2 = 6/pi^2 (an Euler product of A_2(p)->1) is a DIFFERENT object
       from the pair-correlation weight 1/(p-1)^2. The 'two-faced' divisor<->2nd-moment identity is
       yet a THIRD, lower notion (the SECOND moment, leading const 1). All three carry index '2' but
       are distinct arithmetic.""")


# ==============================================================================================
print("\n" + "=" * 94)
print("(4) HONEST SYNTHESIS  --  VERDICT")
print("=" * 94)
print("""  DOES THE TWO-FACED STRUCTURE GENERALIZE UP THE TOWER?  PARTIALLY -- and it is crucial to say
  WHICH 'tower', because Remark 6.2(i) conflates two genuinely different ones.

  [P]  ARITHMETIC FACE generalizes cleanly and EXACTLY.  zeta(s)^r = sum_n d_r(n) n^{-s} and
       L(s,chi3)^r = sum_n d_{r,chi3}(n) n^{-s} hold for r=2,3,4 on BOTH channels (verified to
       truncation precision at s=2,3; L(2,chi3)^r reproduced; d_2 == divisor_count, d_{2,chi3} ==
       base-probe chiral divisor). The r-fold divisor functions d_r, d_{r,chi3} are the honest
       higher coefficients, and both channels carry them identically. This half is solid.

  [A]  SPECTRAL FACE is TWO DISTINCT TOWERS, not one:
       (a) the MOMENT tower -- arithmetic face zeta(s)^r, spectral face the 2r-th moment
           |zeta(1/2+it)|^{2r}; governed by the divisor-CORRELATION sum_n d_r(n)^2/n ~ (log)^{r^2},
           per-prime factor A_r(p) = (1-1/p)^{r^2} sum_m d_r(p^m)^2 p^{-m} -> 1.
       (b) the LEVEL-DENSITY / cumulant tower (N5) -- the r-level density of the ZEROS, the HL
           r-tuple singular series, per-prime weight 1/phi(p)^r = 1/(p-1)^r -> 0, transfer (-1)^r.
       These are DIFFERENT objects: exponents r^2 vs r; per-prime factors A_r(p)->1 vs 1/(p-1)^r->0;
       'r' = moment power vs 'r' = correlation level. They are NOT the same tower. They share only
       the underlying local L-data, not an arithmetic kernel. The structural identification of (a)
       vs (b) is [A]; the moment-conjecture constants for r>=3 (tower (a)'s leading coefficient) are
       themselves [C] (CFKRS conjecture, unproven for r>=3).

  [C]  ONE TOWER (the program's hope in Rem 6.2(i))?  NO at the level of arithmetic kernels --
       refuted here: moments (sum d_r(n)^2/n) != level densities (1/phi(p)^r). The honest statement
       is: the r-th-POWER divisor identity (the literal 'L(s)^r = sum d_r(n)n^{-s}') generalizes [P],
       but its SPECTRAL partner BIFURCATES into (a) higher moments and (b) higher correlations, which
       coincide ONLY in sharing the index and the source L-data, NOT in their arithmetic. Even at r=2
       the program's 'two faces' is the divisor<->SECOND-moment pairing, a third notion distinct from
       both the 4th-moment constant (6/pi^2) and the pair-correlation weight (1/(p-1)^2).

  BOTTOM LINE:  the two-faced structure generalizes as an ARITHMETIC-FACE statement (the r-th power
  Dirichlet identity, both channels, [P]). On the SPECTRAL side it is TWO distinct towers -- moments
  of |zeta| (divisor-correlation, (log)^{r^2}, A_r(p)->1) and correlations of zeros (HL r-tuple /
  N5 cumulants, 1/(p-1)^r). Rem 6.2(i)'s 'same two-faced structure ... the natural setting for the
  N5 cumulant tower' is too strong: the cumulant tower is the LEVEL-DENSITY tower (b), which is NOT
  the moment tower (a) that the literal divisor<->moment identity feeds. A precise, honest negative
  on 'one tower', with a clean positive on the arithmetic face and a sharp structural separation of
  the two spectral towers.""")
print("=" * 94)
