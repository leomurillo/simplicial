# The real-quadratic Siegel core, where Heegner-Stark-Baker does not reach

**Script:** `empirical/verify_real_quadratic_siegel.py`
**Context:** pushes the GRH hard core for real characters (the regulator wild card).
**Finding:** imaginary L pinned by h (HSB-finite, 9 fields); real L=2hR/sqrt(D) carries the
regulator R (wild card), h=1 conjecturally infinite (Gauss) -- no HSB analogue; survives: Page,
Deuring-Heilbronn, Tatuzawa (effective <=1); residual = the one exceptional D = Chowla = open.
**Nature:** numerical/exact (mpmath; Kronecker+digamma; CF-Pell), validated.  NOT a proof.

```text
Pushing the real-quadratic Siegel core, where Heegner-Stark-Baker (HSB) does NOT reach.

Setup (the GRH hard core for real characters). For a quadratic character chi_D (D a fundamental
discriminant) the gap diagnostic is L(1,chi_D); a Siegel zero is L(1,chi_D) anomalously small.
By the Dirichlet class-number formula:
   IMAGINARY (D<0):  L(1,chi_D) = 2 pi h(D) / (w_D sqrt|D|)      -- controlled by h ALONE.
   REAL      (D>0):  L(1,chi_D) = 2 h(D) R_D / sqrt(D)           -- carries the REGULATOR R_D = log eps_D.

WHY HSB reaches imaginary but not real:
  * Imaginary: small L  <=>  small h.  The tightest case h=1 saturates L ~ 1/sqrt|D|, and the h=1
    fields are PROVABLY FINITE (exactly 9, last D=-163; Heegner-Stark-Baker).  So the tightest
    near-Siegel degeneracies are an explicit finite list.
  * Real: small L  <=>  small h*R.  The regulator R_D (the log of the fundamental unit, from Pell)
    is a WILD CARD -- it ranges from ~(1/2)log D up to ~sqrt(D) -- and DECOUPLES h from L.  Worse,
    h=1 occurs for arbitrarily large D and is CONJECTURALLY INFINITE (Gauss's real class-number
    problem, OPEN).  So there is NO finite list to enumerate: HSB has no analogue here.

This probe computes L(1,chi_D) directly (digamma formula, validated against closed forms) for both
families, exhibits the regulator wild card (Pell, continued-fraction), and shows the decisive
contrast: imaginary smallest-L is pinned and finite; real smallest-L is regulator-controlled and
NOT pinned.  Then the honest residual: what STILL survives for real (Page; Deuring-Heilbronn;
Tatuzawa's EFFECTIVE at-most-one) and what does not (excluding the one exceptional D = Chowla = open).

NUMERICAL/EXACT (mpmath; Kronecker symbol + digamma; CF-Pell), labelled.  NOT a proof of GRH.

================  validation (digamma L vs closed forms)  ================
  L(1,chi_{-4}) = 0.7853981634  vs pi/4 = 0.7853981634
  L(1,chi_{-3}) = 0.6045997881  vs pi/3sqrt3 = 0.6045997881
  L(1,chi_5)   = 0.430408941  vs 2log(phi)/sqrt5 = 0.430408941
  L(1,chi_8)   = 0.6232252401  vs 2log(1+sqrt2)/sqrt8 = 0.6232252401

================  PART 1 : REAL quadratic L(1,chi_D) and the regulator wild card  ==========
     D     L(1,chi_D)    Pell regulator R_D=log(eps)   L*sqrt(D)/2 = h*R (the 'gap quantum')
      5   0.4304089     2.887271          0.481212
      8   0.6232252     1.762747          0.881374
     12   0.760346     2.633916          1.31696
     13   0.6627354     7.168579          1.19476
     24   0.9358813     2.292432          2.29243
     29   0.6117663     9.883387          1.64723
     44   0.9024906     5.986446          2.99322
     56   0.9087108     3.400084          3.40008
     61   0.9383102     21.98531          3.66422
     76   1.33725     11.65787          5.82894
     89   1.464441     13.81551          6.90776
    124   1.440365     16.03923          8.01961
    136   1.457152     4.248291          8.49658
    173   0.3909108     15.42489          2.57081
    197   0.4750009     6.666955          3.33348
  ...(62 real fundamental discriminants in [5,200] computed)
  regulator RANGE: min R=1.7627 at D=8 ; max R=43.044 at D=181  -- the wild card (orders of magnitude).
  smallest L(1,chi_D) in range: 0.390911 at D=173.
  -> L = 2 h R / sqrt(D): the regulator R decouples h from L.  Large-D fields can have
     L = O(1) (large unit) OR small L (small unit) -- L does NOT track 1/sqrt(D).

================  PART 2 : IMAGINARY contrast -- L pinned by h, the tightest are FINITE  ====
  L(1,chi_D) = 2 pi h /(w sqrt|D|): NO regulator; small L <=> small h.  Smallest L in range:
     smallest L(1,chi_D) = 0.246069 at D=-163  (= -163 if range reaches it: the h=1 extreme).
  L(1,chi_{-163}) = 0.246069 ~ pi/sqrt163 (h=1, the tightest); and the h=1 fields are EXACTLY 9
  (D=-3,-4,-7,-8,-11,-19,-43,-67,-163; Heegner-Stark-Baker) -- a FINITE near-Siegel list.

================  PART 3 : the real-quadratic residual, honestly  ================
WHY HSB DOES NOT REACH REAL: the regulator R_D decouples h from L, and h=1 occurs for
arbitrarily large D -- conjecturally INFINITELY often (Gauss's real class-number problem,
OPEN).  There is no finite list of tightest fields to enumerate; the imaginary HSB miracle
(h=1 finite) has no real-quadratic analogue.

WHAT STILL SURVIVES (the family dividend, effective):
  * Page/Landau: at most ONE exceptional real character per range (orthogonality = large
    sieve = whitening).  Applies to real quadratic unchanged.
  * Deuring-Heilbronn: the one near-degeneracy REPELS all other zeros in the family.
  * Tatuzawa (1951): Siegel's bound L(1,chi_D) >> D^{-eps} is EFFECTIVE with AT MOST ONE
    exceptional D.  So even effectively, the real-quadratic Siegel zero is cornered to a
    SINGLE possible exceptional discriminant.

WHAT DOES NOT (= GRH's hard core): excluding that ONE exceptional D -- i.e. an effective
L(1,chi_D) >> 1/polylog(D) for ALL real D, equivalently no real-quadratic Siegel zero
(Chowla's conjecture).  This is OPEN, and it is exactly where the regulator wild card lives:
the one D where h*R could conspire to be anomalously small, with R uncontrolled.  The family
structure limits (Page), repels (Deuring-Heilbronn), and effectivizes-to-one (Tatuzawa) --
but does not exclude the one.  That residual = RH-for-L(s,chi_D) for the lone exceptional D.
Not crossed; GRH's real-quadratic core is pinned to a single discriminant, with the regulator
as the precise obstruction HSB cannot touch.
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

**This report.**  The residual "the one exceptional D = Chowla = open" is re-scoped to **[A], closed on
OpenAI 2026**.  There is still no finite list to enumerate (no HSB analogue).  That structural point stands.
But the analytic residual L(1,chi_D) >> 1/polylog(D) for ALL real D now holds, with 1/log log D in fact.
The "regulator wild card" survives only as the open question of splitting hR into h and R.
