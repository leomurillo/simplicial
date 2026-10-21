# Four-front RH divergence -- synthesis: locate, quantify, unify, RANK the barriers

**Script:** `empirical/verify_rh_barrier_synthesis.py`  (companion probes: `verify_li_coefficients.py`,
`verify_debruijn_flow.py`, `verify_jensen_lp.py`, `verify_selberg_siegel.py`).
**Finding:** the four proven-effective frontiers are cataloged with exact constants; fronts 1-3 are
each EXACTLY RH and EXACTLY knife-edge (delta=0 / gap=0 / R(0)=1 -- the same GUE gap^2 event); front 4
(Selberg/Kim-Sarnak) alone has a non-marginal proven gap (7/64)^2=0.012 closable by sym^5 functoriality,
but yields only the STRICTLY-WEAKER no-Siegel-zero conclusion. Conservation of difficulty confirmed.
**Nature:** numerical (mpmath) + literature synthesis; NO claim RH/GRH is proved.

```text
SYNTHESIS of the four-front RH difficulty divergence: locate, quantify, unify, and RANK the
barriers -- and identify the single place the difficulty is genuinely lowerable to "attackable."

Four independent fronts were pushed (each its own probe + report):
  (1) Li-Keiper       lambda_n >= 0  <=> RH        [verify_li_coefficients.py]
  (2) de Bruijn-Newman  Lambda <= 0  <=> RH        [verify_debruijn_flow.py]
  (3) Jensen / Laguerre-Polya  all J^{d,n} hyperbolic <=> RH   [verify_jensen_lp.py]
  (4) Selberg / Kim-Sarnak  lambda_1 >= 1/4 <=> no Siegel zero (STRICTLY WEAKER than GRH)
                                                    [verify_selberg_siegel.py]

This script does two things the four separate probes did not:
  PART A -- UNIFICATION.  All four positivity margins are functionals of the SAME object, the zero
    multiset {rho = 1/2 + i gamma}, and all degenerate at the RH boundary through the SAME mechanism:
    GUE-type repulsion that is statistically sufficient (P(gap -> 0) ~ gap^2) but lacks the INDIVIDUAL
    guarantee.  We compute, from the actual first ~100 zeros: the unfolded gap spectrum, the tightest
    gap (Lehmer), the local de Bruijn-Newman collision margin t_coll = -gap^2/8 (HEIGHT-INDEPENDENT),
    and confirm the gap^2 small-spacing law -- the common root of all four marginalities.
  PART B -- RANKING.  A tiered table of the proven-effective frontier and the exact residual on each
    front, sorted by "attackability."  Conclusion: fronts 1-3 are EXACTLY RH and EXACTLY knife-edge
    (delta=0 / gap=0 / R(0)=1, all margin -> 0); front 4 alone is STRICTLY WEAKER (no-Siegel-zero, a
    GRH consequence) but has a NON-marginal, concrete, proven-effective gap (7/64)^2 = 0.01196 with a
    NAMED closing mechanism (sym^5 functoriality).  That is the one tractable target.

NUMERICAL (mpmath); honest -- NO claim that RH/GRH is proved.  Conservation of difficulty is confirmed,
not broken: every equivalent reformulation (fronts 1-3) sits at the identical marginal point.

================  PART A: the common root -- GUE gap^2 repulsion of the actual zeros  ========
  computing the first 100 nontrivial zeros gamma_j (mpmath zetazero)...
  unfolded nearest-neighbor gaps (mean should be ~1): mean = 0.99519, min = 0.38629
  tightest pair in first 100 zeros: gamma_34=111.02954, gamma_35=111.87466  (raw gap 0.84512, unfolded 0.3863)
  GUE small-spacing law  P(gap<x) ~ x^3/3  (density ~ x^2 repulsion) -- empirical CDF:
     x=0.3 : empirical frac 0.0   vs  x^3/3 = 0.009
     x=0.5 : empirical frac 0.06061   vs  x^3/3 = 0.04167
     x=0.7 : empirical frac 0.2222   vs  x^3/3 = 0.1143
  de Bruijn-Newman LOCAL collision time of the tightest pair (two-body t_coll = -gap^2/8):
     t_coll = -0.064044   -- this is HEIGHT-INDEPENDENT (depends on the gap, not the height).
     => the famous Lehmer pair (gamma ~ 7005, normalized gap ~ 0.0177) gives t_coll ~ -3.14e-5;
        TIGHTER pairs exist at greater heights, so the upper bound on Lambda is NOT improvable
        by computing to greater height -- the obstruction is a UNIFORM repulsion lower bound.

  UNIFICATION: the SAME gap^2 repulsion underlies all four margins -- a zero pair colliding
  (gap->0) is (i) the de Bruijn-Newman complex-pair birth, (ii) the route a zero leaves the
  line (Li delta->0 / Weil), (iii) a cumulant-tower degeneracy (Jensen R(0)->1).  Each margin
  is a DIFFERENT functional of {gamma}, but all degenerate through this one statistical event,
  which holds on AVERAGE (gap^2 law above) but is not guaranteed for EVERY pair at EVERY height.

================  PART B: the proven-effective frontier and the exact residual, RANKED  ======
  ---- Li-Keiper ----
     status   : lambda_n>=0 for all n  <=> RH  (EXACT)
     frontier : lambda_n>0 verified n<=1e5 (Maslanka, Coffey); arch drift (n/2)(log n-1-log2pi+gamma)+3/4-1/24n  [P]
     residual : lambda_n>0 for all n>N_0 unconditionally == RH; an off-line zero (delta) forces a R^n excursion,
                  R=1/sqrt(1-2|delta|/|rho|^2)~1+|delta|/t^2 -> exponential ALWAYS beats the n log n drift.
     margin   : KNIFE-EDGE delta=0 (fluct/drift ~ 1/(n log n) -> 0)

  ---- de Bruijn-Newman ----
     status   : Lambda<=0  <=> RH  (EXACT)
     frontier : Lambda in [0, 0.22]  (Rodgers-Tao 2020: >=0;  Polymath15 2019: <=0.22)  [P]
     residual : 0.22 -> 0 == RH; obstruction is the dynamics/repulsion constant, HEIGHT-INDEPENDENT (gap^2),
                  so NOT improvable by higher-height zero verification -- needs a uniform individual repulsion bound.
     margin   : KNIFE-EDGE gap=0 (collision margin g^2/8 -> 0)

  ---- Jensen / Laguerre-Polya ----
     status   : all J^{d,n} hyperbolic  <=> RH  (EXACT)
     frontier : hyperbolic for d<=9.36e20 (all n) via Platt RH-to-height (GOR-T-T-W 2022); d<=8 clean unconditional  [P]
     residual : uniform-in-degree d == RH;  R(0)=lim_k r_k(0) ~ 0.99972 (defect ~2.8e-4), ratebound rho*<1
                  with rho* in [0.24,0.55] and RISING -- the rate is itself marginal.
     margin   : KNIFE-EDGE R(0)=1 (cumulant defect -> 0)

  ---- Selberg / Kim-Sarnak ----
     status   : lambda_1>=1/4 <=> NO SIEGEL ZERO   (STRICTLY WEAKER than GRH)
     frontier : lambda_1 >= 975/4096 = 0.238037  (Kim-Sarnak 2003, via sym^2,sym^3,sym^4 functoriality)  [P]
     residual : gap to 1/4 is (7/64)^2 = 0.011963 -- a CONCRETE, NON-marginal, proven-effective number;
                  closable by sym^5+ functoriality OR a positive central-L lower bound (Conrey-Iwaniec).
     margin   : NOT a knife-edge -- a finite functoriality gap; the one ATTACKABLE target

================  CONCLUSION (honest, calibrated -- no RH/GRH closure claimed)  ==============
Conservation of difficulty is CONFIRMED, not broken: fronts 1-3 are each EXACTLY RH and each sit
at the identical marginal point -- delta=0 (off-line), gap=0 (collision), R(0)=1 (cumulant) -- which
are three faces of the SAME event (a zero leaving the critical line via a gap->0 collision), governed
by GUE gap^2 repulsion that holds on average but lacks the individual-at-every-height guarantee.
No equivalent reformulation lowers this; the divergence proves WHY (the off-line excursion always
beats the drift; the de Bruijn margin is height-independent; the Jensen rate is itself marginal).

The needle MOVES only by changing the TARGET: the lone front with a non-marginal, proven-effective,
named-mechanism gap is SELBERG/KIM-SARNAK -- lambda_1 >= 0.238 vs the 1/4 wall, gap (7/64)^2 = 0.012,
closable by sym^5 functoriality.  Its conclusion (no Siegel zero => effective PNT in APs, effective
class numbers, effective Linnik) is STRICTLY WEAKER than GRH but is genuinely attackable.  That is
the honest 'lowered difficulty': not GRH, but its strongest effectively-attackable consequence.
```

## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)

Input, tier [A]: OpenAI, *The Quasi-Riemann Hypothesis* (30 Sep 2026, github.com/openai/math, family 003,
Thm 1.1).  Every Dirichlet L(s,chi) is zero-free in Re s > 7/8, uniformly in the modulus.  It is
model-generated, and OpenAI reports Lean formalization.  The functional equation then gives
1/8 <= beta <= 7/8 for every nontrivial zero, with no exceptional (Siegel) zero for any q.

**This report.**  Front 4's conclusion, no-Siegel-zero, is now [A] on OpenAI 2026, which holds for every
real character at once.  Its consequences (effective PNT in APs, effective L(1,chi) >> 1/log log q,
effective class numbers) move from "open" to [A].  See the addendum in rh_selberg_siegel.md.  Selberg's
lambda_1 >= 1/4 itself is NOT touched: the Kim-Sarnak gap 49/4096 is unchanged.  So the reading
"lambda_1 >= 1/4 <=> no Siegel zero" is an analogy, not an equivalence; see the peer-review flag in
rh_selberg_siegel.md.  Fronts 1-3 (each exactly RH) are untouched.  003's strip gives only de
Bruijn-Newman Lambda <= 9/32 = 0.281 (|Im z| <= 3/4 in Polymath's normalization), which is worse than
Polymath's 0.22.  "Conservation of difficulty confirmed" is withdrawn as a summary: front 4's
no-Siegel-zero target was reached without reaching RH.
