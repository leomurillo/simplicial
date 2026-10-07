"""
N1c (CORRECTED 2026-06-08) -- Type-III admissibility for the n=6 primorial-BV row.

Heath-Brown K=5 (diez 3.2) produces Type-I, Type-II, AND Type-III pieces.  diez 3.3 addressed only
Type-I and Type-II -- Type-III is an UNADDRESSED gap.  Type-III is INDEPENDENT of Pascadi: it is the
ternary (d_3) sum, bounded via Deligne / hyper-Kloosterman (Kl_3), NOT the bilinear Kloosterman bound.

CORRECTION (2026-06-08): the prior version of this probe listed "Type-III general moduli = 1/2+1/34
(Heath-Brown 1986)" and posited a FURTHER smooth-moduli gain >= 1/255.  That was a mis-attribution of
the published constants.  The literature (verified):
  - Friedlander-Iwaniec 1985 : general, fixed a            : 1/2 + 1/231
  - Heath-Brown 1986         : general, fixed a            : 1/2 + 1/82   (~0.5122)
  - FKM 2015                 : prime, fixed a              : 1/2 + 1/46   (~0.5217)
  - FKM 2015                 : general (avg over moduli)   : 1/2 + 1/34   (~0.5294)
  - Ping Xi 2018 (Mathematika): SMOOTH squarefree, fixed a : 1/2 + 1/34   (~0.5294)   <-- the smooth record
  - Nguyen                   : general, AVERAGED over a    : 2/3          (~0.6667)
  - 2601.12601 (2026)        : prime,  averaged over a     : 8/11         (~0.7273)

So 1/2+1/34 is ALREADY the smooth-moduli (fixed-a) ceiling (Ping Xi), reached by exactly the
q-van der Corput + FKM trace-function machinery.  The smoothness gain is SPENT, not available.

n=6 target -- CORRECTED (2026-06-08, probe_exact_discharge_schedule): the EXACT requirement is
theta_0(6) = 1 - log(pure_V(P_6))/log(P_6) = 0.6000 = 3/5, NOT the asymptotic 1-2.80/6 = 8/15.
(pure_V(P_6)=sum_{p<=13}(p^2-1)/6=371/6; the asymptotic 1-C*/n is 1-2 rows optimistic at small n.)

THE CORRECTED FINDING (supersedes the earlier "1/255 Type-III gap", which used the WRONG theta_0(6)=8/15):
n=6 needs theta >= 3/5 = 0.600. Both current max-over-a levers fall well short -- bilinear Type-II
(Pascadi 6/11 = 0.545) AND smooth fixed-a Type-III (Ping Xi 1/2+1/34 = 0.529). So n=6 is OUT of reach
for current max-over-a technology by a real margin (~0.05-0.07), not a tiny 1/255 residual. The
max-over-a discharge frontier is n<=5 (Pascadi, razor-tight at n=5: 6/11=0.5455 > theta_0(5)=0.5453).
Classical BV (1/2) discharges only n<=3. Under the VARIANCE reformulation (N0 Lemma 6.8, the genuine
medium arc) n=6 -- like all n -- reduces to sparse-primorial BDH (open); it is not specially secured.
The bridge-coupling check (beta<=theta/8) is verified for fixed n (X->inf => beta->0), but is moot for
n=6 since the Type-II ceiling itself is below 3/5.
"""
import sympy as sp

half = sp.Rational(1, 2)
theta6 = sp.Rational(3, 5)                           # EXACT theta_0(6) = 0.600 (NOT 8/15)
typeII_pascadi = sp.Rational(6, 11)                  # N1b favorable-regime ceiling (bilinear, pinned)

d3 = {
    "FI 1985  general,  fixed a   ": half + sp.Rational(1, 231),
    "HB  1986  general,  fixed a   ": half + sp.Rational(1, 82),
    "FKM 2015  prime,    fixed a   ": half + sp.Rational(1, 46),
    "FKM 2015  gen(avg q),fixed a  ": half + sp.Rational(1, 34),
    "Xi  2018  SMOOTH sqf,fixed a  ": half + sp.Rational(1, 34),   # the smooth record
    "Nguyen    general,  avg over a": sp.Rational(2, 3),
    "2026      prime,    avg over a": sp.Rational(8, 11),
}

print("N1c CORRECTED -- Type-III (d_3) landscape for the n=6 primorial-BV row")
print("=" * 74)
for name, val in d3.items():
    print(f"  d_3 level [{name}] = {str(sp.nsimplify(val)):>9}  = {float(val):.4f}")
print("-" * 74)
print(f"  n=6 target        theta_0(6) = 3/5  (EXACT)    = {float(theta6):.4f}   [NOT 8/15=0.5333 asymptotic]")
print(f"  Type-II (Pascadi) theta_II   = 6/11           = {float(typeII_pascadi):.4f}  [pinned, N1b]")
print("-" * 74)

smooth_fixed_a = half + sp.Rational(1, 34)           # Ping Xi 2018 -- best smooth fixed-a Type-III
gapII  = theta6 - typeII_pascadi                      # Type-II shortfall at n=6
gapIII = theta6 - smooth_fixed_a                      # Type-III shortfall at n=6
assert theta6 == sp.Rational(3, 5) and gapII > 0 and gapIII > 0
print("VERDICT (CORRECTED 2026-06-08 -- supersedes the '1/255 Type-III gap').")
print(f"  * theta_0(6)=3/5 EXACT (probe_exact_discharge_schedule), NOT 8/15; the earlier 1/255 used 8/15.")
print(f"  * Type-II shortfall  = 3/5 - 6/11      = {sp.nsimplify(gapII)}  = {float(gapII):.4f}  (bilinear Pascadi short).")
print(f"  * Type-III shortfall = 3/5 - (1/2+1/34)= {sp.nsimplify(gapIII)} = {float(gapIII):.4f}  (smooth d_3 short).")
print(f"  * => n=6 needs theta>=3/5; BOTH current max-over-a levers fall short by ~0.05-0.07 -- it is")
print(f"    OUT of reach, NOT a tiny 1/255 residual. Max-over-a frontier = n<=5 (razor-tight at n=5).")
print(f"  * Under the VARIANCE form (N0 Lemma 6.8) n=6 -- like ALL n -- reduces to sparse-primorial BDH")
print(f"    (open); it is not specially secured. The d_3 landscape above is unchanged and correct.")
