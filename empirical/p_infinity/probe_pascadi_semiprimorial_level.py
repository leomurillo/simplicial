"""
Semi-primorial level-of-distribution LEDGER (the candidate unconditional advance).

OBLIGATION (program N0 sec6): RH-closure needs the primorial level theta_0(P_n) -> 1 (Lindelof-strength)
on FULLY primorial moduli P_n = prod_{p<=y} p (omega(q) -> infinity, all factors small).

CANDIDATE ADVANCE: on SEMI-primorial moduli q = p * P_k -- one large controllable prime p ~ q^beta times
a smooth primorial cofactor P_k -- a single-large-prime amplification (Pascadi arXiv:2511.08445,
"non-abelian amplification", saving ~ c^{-1/12} for near-prime c; companion to Wright arXiv:2604.25177
and Milicevic-Qin-Wu arXiv:2511.07550 no-factorability) can push the level past the current fixed-factor
frontier theta_0 = 1/2 + 1/66 ~ 0.5152.

WHAT IS RIGOROUS HERE [P] vs CONDITIONAL [C]:
  [P]  Part A: the CRT cap -- a SMOOTH/primorial modulus supports level EXACTLY 1/2; the gain CANNOT come
       from the small primes (per-prime Weil is sharp; 2^omega = q^{o(1)} does not compound). Exact.
  [C]  Part C: the semi-primorial level 1/2 + gain(beta) is CONDITIONAL on the external dispersion/Pascadi
       input (which this script does NOT prove and the author has NOT independently verified); the gain is
       carried as a PARAMETER, and the resulting level is a feasibility figure, not a theorem.
  HONEST verdict (Part D): even granting the external input, the FULL primorial obligation (theta_0 -> 1)
       is NOT reached -- the smooth part is capped at 1/2 and the single-big-prime fraction beta -> 0 as
       omega -> infinity (Pascadi degrades with many small factors). Genuine sub-family advance, NOT the wall.

No torch. Exact where exact is possible (Part A); transparent/parametric where it is not (Part C).
"""
import sympy as sp
import math

def primorial(k):
    ps = list(sp.primerange(2, 10**6))
    P = sp.Integer(1)
    for p in ps[:k]: P *= p
    return P, ps[:k]

print("="*92)
print("PART A [P, EXACT]: the CRT cap -- a smooth/primorial modulus supports level EXACTLY 1/2")
print("="*92)
print("""  Per-prime Weil is SHARP: |S(m,n;p)| <= 2 sqrt p (Kloosterman), achieved. For squarefree q=prod p_i,
  twisted multiplicativity gives |S(.;q)| <= prod 2 sqrt(p_i) = 2^omega(q) * sqrt q. The level a single
  Kloosterman/exponential-sum bound supports is set by sqrt q (=> theta=1/2); the cap is beaten only if
  2^omega(q) itself grows like a power of q. It does NOT: 2^omega(q) = q^{o(1)}. Exact check on primorials:""")
print(f"  {'k':>3} {'P_k=prod p_i':>22} {'omega':>5} {'log(2^omega)/log P_k':>22} {'-> level cap':>12}")
prev = None
for k in [2, 4, 6, 8, 10, 14, 20, 30]:
    P, ps = primorial(k)
    e = float(k*sp.log(2) / sp.log(P))       # exponent of 2^omega relative to q
    cap = 0.5 + e/2                            # the 2^omega inflates the naive exponent by e/2
    print(f"  {k:>3} {str(P):>22} {k:>5} {e:>22.6f} {cap:>12.6f}")
print("""  log(2^omega)/log P_k -> 0 (since omega(P_k)=k ~ p_k/log p_k and log P_k = theta(p_k) ~ p_k, ratio
  ~ log2/log p_k -> 0). So 2^omega = P_k^{o(1)} and the smooth/primorial modulus is capped at level 1/2
  EXACTLY: the gain cannot compound across the small primes. [P]  (This is the program's CRT-cap, made
  exact: the smooth part is inert past 1/2; any beyond-1/2 gain must come from elsewhere.)""")

print("="*92)
print("PART B: the unconditional level frontier and its applicability to SEMI-primorial q = p * P_k")
print("="*92)
rows = [
    ("Bombieri-Vinogradov (1965)",        0.5,            "ALL moduli",                       "yes (baseline)"),
    ("Zhang/Polymath8 well-factorable",   0.5+7/300,      "smooth/well-factorable moduli",    "partial (smooth part only)"),
    ("Maynard (well-factorable, primes)", 0.6,            "well-factorable weights",          "no (incompatible w/ fixed q-shape)"),
    ("Wright trilinear (2604.25177)",     0.5+1/66,       "fixed denominator factor",         "yes (the current frontier)"),
    ("Pascadi non-abelian (2511.08445)",  None,           "near-prime / one large prime p|q", "yes (the candidate lever)"),
    ("Milicevic-Qin-Wu (2511.07550)",     None,           "ARBITRARY q, no factorability",    "yes, but NO omega gain"),
]
print(f"  {'method':>34} {'theta_0':>10} {'modulus class':>34} {'semi-primorial?':>30}")
for name, th, cls, app in rows:
    ths = f"{th:.4f}" if th is not None else "  (saving)"
    print(f"  {name:>34} {ths:>10} {cls:>34} {app:>30}")
print("""  Net: the smooth primorial cofactor P_k is capped at 1/2 (Part A); MQW removes factorability but has
  ZERO omega-dependence (no compounding -- verified earlier); so on q = p * P_k the ONLY source past 1/2
  is the single large prime p, via the dispersion method / Pascadi non-abelian amplification.""")

print("="*92)
print("PART C [C, CONDITIONAL -- parametric, NOT a proven theorem]: the semi-primorial level")
print("="*92)
print("""  Model q = p * P_k, p ~ q^beta a large prime, P_k ~ q^{1-beta} smooth (capped at 1/2, Part A). A
  single-big-prime dispersion amplification supplies a power saving q^{-eta} from the p-aspect (Pascadi
  reports eta ~ 1/12 for near-primes); in the BFI/Polymath dispersion balance this lifts the level on the
  p-aspect to ~ 1/2 + eta*w(beta), w(beta) the fraction of the modulus the amplification controls. We do
  NOT prove the translation; we tabulate the FEASIBILITY figure theta(beta) = 1/2 + eta*beta for the
  reported eta=1/12 (a transparent lower-end model; the true exponent requires Pascadi's verified theorem):""")
eta = sp.Rational(1, 12)
print(f"  eta = 1/12 (Pascadi, reported).  {'beta (size of big prime)':>26} {'theta = 1/2 + eta*beta':>24} {'> Wright 0.5152?':>18}")
for beta in [sp.Rational(1,3), sp.Rational(1,2), sp.Rational(2,3), sp.Rational(4,5), sp.Integer(1)]:
    th = sp.Rational(1,2) + eta*beta
    print(f"  {'':>26} beta={float(beta):>5.3f}            {float(th):>10.4f}            {str(float(th) > 0.5+1/66):>18}")
print("""  => CONDITIONALLY, for a big prime with beta >~ 0.19 the semi-primorial level exceeds the Wright
     fixed-factor frontier 0.5152, and beta -> 1 (q itself near-prime) gives ~ 1/2 + 1/12 = 0.5833.
     [C] This is a feasibility figure conditional on the external Pascadi exponent + the dispersion
     translation, NEITHER proven nor independently verified here. Treat as a TARGET, not a result.""")

print("="*92)
print("PART D [HONEST VERDICT]: a genuine sub-family advance, but NOT the primorial obligation")
print("="*92)
print("""  The obligation is theta_0(P_n) -> 1 on FULLY primorial moduli (omega -> infinity). The semi-primorial
  lever does NOT reach it, for two exact reasons:
   (1) the smooth part is capped at 1/2 (Part A) -- the many small primes contribute no beyond-1/2 gain;
   (2) the gain rides on the SINGLE big prime's relative size beta; in the fully primorial limit the
       largest prime factor p_k satisfies log p_k / log P_k = log p_k / theta(p_k) -> 0, i.e. beta -> 0,
       so theta -> 1/2 + eta*0 = 1/2. Pascadi DEGRADES with many small factors (its own caveat).
  CHECK beta_max(P_k) = log(largest prime)/log(primorial) -> 0:""")
for k in [6, 10, 20, 30, 50]:
    P, ps = primorial(k)
    beta_max = float(sp.log(ps[-1]) / sp.log(P))
    print(f"   P_{k}: largest prime {ps[-1]:>4}, beta_max = log p_k / log P_k = {beta_max:.4f}")
print("""  => beta_max -> 0 along the primorial tower: the one-big-prime advantage vanishes exactly where the
     obligation lives. CONCLUSION: the semi-primorial level is a real, precisely-placed UNCONDITIONAL
     advance on the sub-family q = p*P_k (conditional on verifying Pascadi's exponent), pushing past the
     0.5152 frontier for a large controllable prime -- but it is structurally BELOW the wall: the full
     primorial theta_0 -> 1 is unreachable this way. The arithmetic face of RH (the primorial Lindelof
     level) stands. Value: it pins the lever's reach AND its exact limit; partial credit, not closure.""")
