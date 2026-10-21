# Effective lower bounds on hR for real quadratic fields: the honest layered state

**Script:** `empirical/verify_effective_hR_bound.py`
**Context:** the asked 'effective lower bound on hR' = the real-quadratic Siegel/Chowla problem.
**Result:** Layer 1 elementary (all D, hR>=log((1+sqrtD)/2), sharp at D=5, too weak by sqrtD/(logD)^2);
Layer 2 Tatuzawa (effective for all but <=1 D, >>D^{1/2-eps}); Layer 3 (the one exceptional D) = OPEN
(Chowla; Goldfeld-Gross-Zagier is imaginary-only).  NOT a proof of Layer 3.

```text
Effective lower bounds on hR (= the real-quadratic Siegel problem): the honest, layered state.

GOAL asked: an effective lower bound on h(D)*R(D) for real quadratic D, where R=log eps_D is the
regulator.  Since L(1,chi_D) = 2 h R / sqrt(D), this is an effective lower bound on L(1,chi_D).
A *no-exception* such bound (L >> 1/polylog for ALL real D) is equivalent to no real-quadratic
Siegel zero = Chowla's conjecture = OPEN.  This certificate lays out the THREE layers honestly.

LAYER 1 -- ELEMENTARY, holds for ALL D, but WEAK.  The fundamental unit satisfies eps_D >= (1+sqrt D)/2
  (sharp at D=5, the golden ratio), so R_D >= log((1+sqrt D)/2) ~ (1/2)log D, and with h>=1:
        h R >= log((1+sqrt D)/2),   i.e.   L(1,chi_D) >= 2 log((1+sqrt D)/2)/sqrt(D) ~ (log D)/sqrt(D).
  Effective, unconditional, for every D -- but it -> 0, far weaker than the GRH-strength target.

LAYER 2 -- TATUZAWA (1951), holds for ALL BUT <=1 D, and is STRONG.  Siegel's L(1,chi_D) >>_eps D^{-eps}
  is made EFFECTIVE with at most one exceptional discriminant.  This is the genuine effective bound on
  hR (>> D^{1/2-eps}) -- the family/anisotropy (large-sieve = whitening) dividend delivering an
  effective Siegel for all but one D.

LAYER 3 -- THE ONE EXCEPTIONAL D (no-exception bound) -- OPEN.  Excluding the single possible exceptional
  discriminant = a no-exception effective L >> 1/polylog = no real Siegel zero (Chowla).  The imaginary
  analogue was cracked (Goldfeld 1976 + Gross-Zagier 1986: h(-D) >> (log D)^{1-eps}, effective, via an
  L-function with a triple central zero / a Heegner-point height); that mechanism is IMAGINARY-specific
  and has NO real-quadratic analogue.  This layer is the open core.

This probe VERIFIES Layer 1 (the elementary bound, sharp at D=5), measures the gap to the GRH target,
confirms no near-Siegel discriminant in range, and states Layers 2-3 with their status.  NOT a proof
of Layer 3; that is Chowla/Siegel.

NUMERICAL/EXACT (mpmath; Kronecker + digamma), labelled.

================  LAYER 1 : hR >= log((1+sqrt D)/2)  (elementary, ALL D, weak)  ============
  hR = L(1,chi_D) sqrt(D)/2  (computed from L); bound B(D)=log((1+sqrt D)/2) (from eps_D>=(1+sqrtD)/2).
  hR >= B(D) for ALL 302 real fundamental discriminants in [5,1000]: True
  tightest (min hR/B): ratio 1.0 at D=5  (=1 exactly at D=5: hR=B=log(golden ratio))
  smallest L(1,chi_D) in range: 0.291061 at D=437 (no near-Siegel: bounded well away from 0).
  => unconditional effective bound, ALL D:  L(1,chi_D) >= 2 log((1+sqrtD)/2)/sqrt(D) ~ (log D)/sqrt(D).

================  THE GAP : effective (Layer 1) vs GRH-strength target  ================
  GRH-strength target (no Siegel zero): L(1,chi_D) >> 1/log D.  Compare the two at sample D:
     D        L (actual)     Layer-1 bound 2B/sqrtD     target ~1/log D     gap factor sqrtD/(logD)^2
           5   0.430409        0.4304              0.6213            0.86325
         101   0.596669        0.3402              0.2167            0.47184
        1000   (—)        0.1766              0.1448            0.66271
       10000   (—)        0.07844              0.1086            1.1788
     1000000   (—)        0.01243              0.07238            5.2392
   1000000000   (—)        0.0006115              0.04825            73.635
  the Layer-1 bound is weaker than the target by a factor ~ sqrt(D)/(log D)^2 -> infinity:
  the elementary regulator bound is SHARP (saturated at D=5) and cannot be improved
  elementarily; closing the gap needs analytic control of h (or the product) -- Layers 2-3.

================  LAYER 2 (Tatuzawa) and LAYER 3 (the open core)  ================
LAYER 2 -- EFFECTIVE for ALL BUT <=1 D (Tatuzawa 1951): hR >>_eps D^{1/2-eps}, effective,
  with at most one exceptional discriminant.  This is the genuine effective lower bound on hR;
  it is the family/large-sieve (= whitening) dividend made effective.  So an effective bound
  DOES exist -- up to a single possible exception per range.

LAYER 3 -- THE ONE EXCEPTIONAL D (no-exception bound) -- OPEN = Chowla/Siegel.  Excluding that
  one discriminant is a no-exception effective L >> 1/polylog = no real-quadratic Siegel zero.
  The imaginary analogue (Gauss class-number problem) WAS solved effectively (Goldfeld +
  Gross-Zagier: a triple central zero / Heegner-point height gives h(-D) >> (log D)^{1-eps});
  that construction is IMAGINARY-specific (central L-value of a weight-2 form; Heegner points
  on X_0(N)) and has NO real-quadratic analogue.  This is exactly where the regulator wild card
  lives: the one D where h*R could conspire small, with R uncontrolled.

================  HONEST VERDICT  ================
An effective lower bound on hR EXISTS for all but at most one real discriminant (Tatuzawa,
>> D^{1/2-eps}); the unconditional all-D bound is elementary and sharp (hR >= log((1+sqrtD)/2),
L >> (log D)/sqrt D) and provably too weak by ~sqrt(D)/(log D)^2.  A NO-EXCEPTION effective
bound -- closing the single exceptional discriminant -- IS the real-quadratic Siegel/Chowla
problem, OPEN, with the imaginary-only Goldfeld-Gross-Zagier mechanism not transferring.
I do not solve Layer 3; the regulator is the named obstruction, and fabricating a bound there
would be the fluent-but-false failure the discipline forbids.  GRH's real-quadratic core is
pinned to that one discriminant; Layers 1-2 are the honest, real effective state around it.
```

## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)

**Input, tier [A].**  OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s) > 7/8*
(30 Sep 2026, github.com/openai/math, family 003, Thm 1.1).  Every Dirichlet L(s,chi), for every modulus
and character, has no zero in Re s > 7/8.  The result is model-generated.  OpenAI reports that the
core statement is Lean-formalized (lean/docs/003.md).  We have not refereed it.  Everything below rests
on it and is [A], never [P].  The functional equation then gives 1/8 <= beta <= 7/8 for every nontrivial
zero.  In particular every real character has beta <= 7/8, with no exceptional modulus.

**Effective L(1,chi) (derivation, [A] on 003 + classical).**  The zero-free-rectangle lemma
(Granville-Soundararajan 2003, GAFA, Lemma 2.2; the Littlewood 1928 argument with 1/2 replaced by
sigma_0) takes sigma_0 = 7/8, s = 1, sigma_1 = 7/8 + 1/log y.  It gives
    log L(1,chi) = sum_{n<=y} Lambda(n) chi(n) / (n log n) + O( log q * y^(-1/8) * log^2 y ).
Take y = (log q)^B with B > 8.  The error is o(1), and
    |sum_{n<=y} Lambda(n) chi(n)/(n log n)| <= log log y + gamma + o(1) = log log log q + log B + gamma + o(1).
Hence, for every primitive real chi mod q and q >= q_0,
    c / log log q  <=  L(1,chi)  <=  C log log q,
with c and q_0 EFFECTIVE (any c < e^(-gamma)/8 and C > 8 e^gamma for q large).  This is the Littlewood
shape, with constants weaker than GRH's.  It needs no Siegel-zero hypothesis, because 003 excludes
that zero for every q at once.

**Consequences, each [A] on 003.**
- Imaginary quadratic: h(-d) = w sqrt(d) L(1,chi_{-d}) / (2 pi) >> sqrt(d)/log log d, EFFECTIVE.
  The previous effective record is Goldfeld-Gross-Zagier, h(-d) >> log d.
- Real quadratic: h(D) log eps_D = sqrt(D) L(1,chi_D) >> sqrt(D)/log log D, EFFECTIVE, no exceptional D.
  It does NOT separate h(D) from the regulator, and Gauss's real class-number questions stay open.
- PNT in APs: psi(x;q,a) = psi-main + O(x^(7/8) log^2(qx)), EFFECTIVE, uniform for q <= x^(1/8-eps).
  This replaces the ineffective Siegel-Walfisz range q <= (log x)^A.
- Linnik: p(q,a) << q^(8+eps) effectively.  This is NO gain: Xylouris's L = 5 is already effective.
- Euler's idoneal numbers (Weinberger 1973): the effective h(-4n) lower bound beats the genus count
  2^(omega(n)-1).  So "the 65 are complete" reduces to an EXPLICIT form of c, q_0 plus a finite search.
  That explicit bound and search are NOT done here.  Status: reduced to computation, not settled.
- NOT gained: GRH.  Complex zeros may still lie anywhere in 1/8 <= beta <= 7/8, and nothing here touches
  Re rho = 1/2.  "No Siegel zero << GRH" remains true and correct.  Only the "OPEN" labels on the
  Siegel / exceptional-zero items move, from open to [A].

**This report.**  LAYER 3 ("the one exceptional D = Chowla = OPEN") is re-scoped to **[A], closed on
OpenAI 2026**.  The effective bound h(D) log eps_D >> sqrt(D)/log log D now holds for EVERY D, with no
Tatuzawa exception.  Layers 1-2 are unchanged and still correct.  The remark that Goldfeld-Gross-Zagier is
imaginary-only stays true.  The closure comes from a zero-free half-plane, not from any regulator mechanism.
