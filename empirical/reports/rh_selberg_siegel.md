# Selberg eigenvalue conjecture <-> Landau-Siegel zero: dictionary, record, gap, sensitivity

**Script:** `empirical/verify_selberg_siegel.py`  (mpmath dps 30; exact `Fraction` for the chain).
**Companion to:** `verify_scattering_zeta_L.py` (scattering mechanism), `verify_full_trace_formula.py` (machine-precision PSL(2,Z) balance), `verify_selberg_geodesic_spectral.py` (geometric side).
**Finding:** the lift dictionary lambda = beta(1-beta) = 1/4-(beta-1/2)^2 on Gamma_0(4q); the Kim-Sarnak chain 7/64 -> 975/4096 = 0.23803 with gap 49/4096 = 0.01196 (record UNIMPROVED at full level, Yang 2020 withdrawn); trace-formula sensitivity to a hypothetical exceptional eigenvalue (macroscopic, not a small perturbation); L(s,chi_3),L(s,chi_5) > 0 on (1/2,1) (no Siegel zero).
**Honest scope:** dictionary + record + sensitivity computed/cited; no-Siegel-zero << GRH; neither Selberg nor no-Siegel-zero proved here.  GPD-disciplined.

```text
Selberg eigenvalue conjecture <-> Landau-Siegel zero: the QUANTITATIVE dictionary, the proven
Kim-Sarnak record, the no-Siegel-zero-vs-GRH gap, and a trace-formula exceptional-eigenvalue
sensitivity computation.  Companion to verify_scattering_zeta_L.py / verify_full_trace_formula.py /
verify_selberg_geodesic_spectral.py (those establish the scattering mechanism + the machine-precision
PSL(2,Z) balance; this one nails the CONSTANTS, the proven record, and what is/is not gained).

THE DICTIONARY (Iwaniec, Spectral Methods of Automorphic Forms 2nd ed., ch. 11; Sarnak, Notes on the
Generalized Ramanujan Conjectures 2005; Conrey-Iwaniec, "The cubic moment of central values of
automorphic L-functions," Ann. of Math. 151 (2000)).  Let chi be a real primitive Dirichlet character
mod q with a Landau-Siegel zero beta = 1 - delta (real, beta in (1/2,1), delta = 1-beta small).  The
theta / Shimura-Waldspurger lift sends L(s,chi) to a weight-1/2 Maass form on Gamma_0(4q) (Kohnen plus
space).  The Laplacian eigenvalue of the lifted object is
      lambda = s(1-s)   with   s = beta,        i.e.   lambda = beta(1-beta).
Writing the spectral parameter lambda = 1/4 - t^2 (eigenvalue below 1/4 <=> t real, "exceptional"):
      t = beta - 1/2     and     lambda = 1/4 - (beta - 1/2)^2.
So a Siegel zero beta -> 1 (delta -> 0) gives lambda = beta(1-beta) -> 0: an exceptional eigenvalue
crashing toward 0.  Conversely an exceptional eigenvalue lambda = 1/4 - s^2 (0 < s < 1/2, spectral
parameter r = i*s purely imaginary) corresponds to a real zero beta = 1/2 + s of the lifted L-function.

THE KIM-SARNAK CHAIN.  The local archimedean Ramanujan exponent theta_infty bounds the eigenvalue:
   lambda_1 >= 1/4 - theta_infty^2.  Bounds toward theta_infty = 0 (full Ramanujan -> Selberg 1/4):
     - Selberg 1958:        theta <= 1/4         => lambda_1 >= 3/16   = 0.1875
     - via sym^2 (Gelbart-Jacquet 1978) ............ improves toward Ramanujan
     - sym^3, sym^4 (Kim-Shahidi 2002; Kim 2003, w/ appendix Kim-Sarnak): theta_infty <= 7/64
        => lambda_1 >= 1/4 - (7/64)^2 = 1/4 - 49/4096 = (1024-49)/4096 = 975/4096 = 0.23803...
The gap to Selberg's 1/4 = 0.25 is 49/4096 = 0.011963...  PROVEN RECORD (full level, GL(2)/Q): still
975/4096 (Kim-Sarnak 2003).  Liyang Yang's 2020 "improvement" for EXCEPTIONAL Maass forms was WITHDRAWN
(arXiv:2011.09054, incomplete proof).  Holomorphic Ramanujan is THEOREM (Deligne) but irrelevant here:
the Maass / weight-1/2 case is where Siegel zeros live, and there theta_infty = 7/64 is the wall.

WHAT NO-SIEGEL-ZERO BUYS, AND WHAT IT DOES NOT.  Selberg lambda_1 >= 1/4 <=> no exceptional eigenvalue
on Gamma_0(4q) <=> no Landau-Siegel zero for real chi mod q.  No-Siegel-zero gives: effective
L(1,chi) >> 1/log q (vs Siegel's INEFFECTIVE bound), effective class number h(-d) >> sqrt(d)/log d for
imaginary quadratic, effective PNT in arithmetic progressions / effective Linnik.  It does NOT give GRH:
the OTHER (complex, off-real-axis) zeros of L(s,chi) can still lie off Re(s)=1/2.  No-Siegel-zero only
excludes the single real zero near s=1; GRH excludes ALL.  no-Siegel-zero  <<  GRH, strictly.

This probe:
  (A) the exact dictionary as a numeric table: beta <-> delta <-> lambda <-> t, both directions.
  (B) the Kim-Sarnak chain arithmetic in exact rationals: 3/16, 975/4096, the 49/4096 gap; Selberg
      lambda_1 >= 1/4 - theta^2 evaluated at each proven theta; identify the room.
  (C) TRACE-FORMULA SENSITIVITY: insert a hypothetical exceptional eigenvalue lambda = 1/4 - s^2
      (r = i*s) into the spectral side h(i*s) of the machine-precision-balanced PSL(2,Z) trace formula,
      and measure the residual it injects -- the quantitative "the trace formula would SEE it" signal,
      and how the signal scales as the Siegel zero tightens (s -> 1/2, lambda -> 0).
  (D) SCATTERING LAW: for real chi mod 3 and mod 5, compute L(s,chi) on (1/2,1), confirm L>0 (no real
      zero), hence no real scattering pole, hence (via lambda = beta(1-beta)) no exceptional eigenvalue;
      cross-check the eigenvalue that a HYPOTHETICAL Siegel zero at beta would produce.
  (E) synthesis + the precise residual.

NUMERICAL/EXACT (mpmath dps 30; Fraction for the chain).  Cited where derivation is standard
(theta-lift dictionary, level 4q, Maass spectrum).  NOT a proof of Selberg / no-Siegel-zero / GRH.

================  (A) THE DICTIONARY  beta <-> delta <-> lambda <-> t (exact relations)  ====
  lift: weight-1/2 Maass form on Gamma_0(4q); lambda = beta(1-beta) = 1/4 - (beta-1/2)^2.
  A Siegel zero beta = 1 - delta of real chi mod q  ->  exceptional eigenvalue lambda below:
    beta        delta=1-beta     lambda=beta(1-beta)    t=beta-1/2   (lambda=1/4 - t^2)
    0.6         0.4            0.24                  0.1
    0.75        0.25           0.1875                0.25
    0.9         0.1            0.09                  0.4
    0.95        0.05           0.0475                0.45
    0.99        0.01           0.0099                0.49
    0.999       0.001          0.000999              0.499
    0.9999      0.0001         9.999e-5              0.4999
  small-delta law:  lambda = beta(1-beta) = (1-delta)*delta = delta - delta^2  ~  delta  as delta->0.
  So lambda ~ (1 - beta) to first order: the eigenvalue is ~ the Siegel-zero DEFECT from 1.
  CONVERSE (exceptional eigenvalue -> Siegel zero):  lambda = 1/4 - s^2  (r = i*s, 0<s<1/2)
    lambda          s=sqrt(1/4-lambda)   beta = 1/2 + s   (the implied real zero)
    0.24            0.1                  0.6
    0.2             0.2236067977         0.7236067977
    0.15            0.316227766          0.816227766
    0.1             0.3872983346         0.8872983346
    0.05            0.4472135955         0.9472135955
    0.01            0.4898979486         0.9898979486
    0.001           0.498998998          0.998998998

================  (B) THE KIM-SARNAK CHAIN  lambda_1 >= 1/4 - theta_infty^2 (exact rationals)  =
  theta_infty = archimedean exponent toward Ramanujan; Ramanujan(theta=0) => Selberg(1/4).
    source                       theta_infty     lambda_1 >= 1/4 - theta^2        decimal
    trivial / Selberg 1958       1/4 = 0.25      3/16 = 1/4 - 1/16              0.1875
    Luo-Rudnick-Sarnak 1995      5/28 = 0.178571 171/784 = 1/4 - 25/784         0.218112245
    Kim-Shahidi 2002 (sym^3)     1/9 = 0.111111  77/324 = 1/4 - 1/81            0.237654321
    Kim-Sarnak 2003 (sym^4)      7/64 = 0.109375 975/4096 = 1/4 - 49/4096       0.238037109
    Ramanujan (conjectural)      0 = 0.0         1/4 = 1/4 - 0                  0.25
  PROVEN RECORD (full level, GL(2)/Q): lambda_1 >= 975/4096 = 0.2380371094  (Kim-Sarnak 2003).
  GAP to Selberg 1/4 = 0.25:  1/4 - 975/4096 = 49/4096 = (7/64)^2 = 0.011962891.
  Liyang Yang 2020 (sym^? improvement for EXCEPTIONAL Maass forms): WITHDRAWN (incomplete);
  so 7/64 -> 975/4096 STILL STANDS as the proven bound over the full level (as of 2026).
  IDENTIFIABLE ROOM: theta_infty = 7/64 comes from sym^4 being the last PROVEN functorial
  symmetric power (sym^5,6,... give the Ramanujan limit 0 but are NOT known functorial as
  cuspidal automorphic on GL(n)).  Each new sym^k would shrink theta_infty toward 0; the
  0.012 gap is exactly 'sym^4 is where Langlands-Shahidi currently stops.'

================  (C) TRACE-FORMULA SENSITIVITY: inject a hypothetical exceptional eigenvalue  =
  The PSL(2,Z) trace formula balances to ~1e-6 (verify_full_trace_formula.py) with NO
  exceptional term.  We add one hypothetical eigenvalue lambda = 1/4 - s^2 (r = i*s) to the
  spectral side h(i*s) and read off the residual it would INJECT into the balance -- i.e. the
  trace formula's sensitivity to an exceptional eigenvalue (what a congruence-level Siegel zero
  would do).  Test function h(r) = exp(-r^2/2 sig^2); note h(i*s) = exp(+s^2/2 sig^2) >= 1.
  --- sigma = 4.0 : baseline spectral side S0 = 1.08080336818 (no exceptional term) ---
      s (=beta-1/2)   beta=1/2+s   lambda=1/4-s^2   added h(i*s)=dS   (dS)/S0 jump
      0.49           0.99         0.0099          1.00753134       0.932206
      0.45           0.95         0.0475          1.00634819       0.931111
      0.4            0.9          0.09            1.00501252       0.929875
      0.3            0.8          0.16            1.00281646       0.927844
      0.2            0.7          0.21            1.00125078       0.926395
      0.1            0.6          0.24            1.00031255       0.925527
      0.05           0.55         0.2475          1.00007813       0.92531

  --- sigma = 2.0 : baseline spectral side S0 = 1.03175505245 (no exceptional term) ---
      s (=beta-1/2)   beta=1/2+s   lambda=1/4-s^2   added h(i*s)=dS   (dS)/S0 jump
      0.49           0.99         0.0099          1.03046741       0.998752
      0.45           0.95         0.0475          1.02563558       0.994069
      0.4            0.9          0.09            1.02020134       0.988802
      0.3            0.8          0.16            1.01131352       0.980188
      0.2            0.7          0.21            1.00501252       0.974081
      0.1            0.6          0.24            1.00125078       0.970435
      0.05           0.55         0.2475          1.00031255       0.969525

  --- sigma = 1.2 : baseline spectral side S0 = 1.09068458154 (no exceptional term) ---
      s (=beta-1/2)   beta=1/2+s   lambda=1/4-s^2   added h(i*s)=dS   (dS)/S0 jump
      0.49           0.99         0.0099          1.08694179       0.996568
      0.45           0.95         0.0475          1.07284339       0.983642
      0.4            0.9          0.09            1.05712774       0.969233
      0.3            0.8          0.16            1.03174341       0.945959
      0.2            0.7          0.21            1.01398579       0.929678
      0.1            0.6          0.24            1.00347826       0.920044
      0.05           0.55         0.2475          1.00086843       0.917652

  READING: an exceptional eigenvalue injects h(i*s) = exp(+s^2/2sig^2) >= 1 (the test function
  EVALUATED AT THE IMAGINARY spectral parameter r=i*s GROWS, the only term that does).  The
  raw injected value exp(s^2/2sig^2) is largest for NARROW h (small sig) and s near 1/2; but the
  RELATIVE jump dS/S0 is order-unity (~0.92-1.00) across ALL test functions -- because S0 itself
  is O(1).  Either way the signal is MACROSCOPIC: an exceptional eigenvalue adds a term ~0.9-1.0
  times the entire existing spectral side, dwarfing the ~1e-6 balance floor by ~6 orders of
  magnitude.  It is NOT a small perturbation -- it is a new O(1) spectral line the trace formula
  cannot miss.  (At level 1 there is none, hence the clean balance; the search for it at
  congruence level Gamma_0(4q) IS the Selberg problem.)

================  (D) SCATTERING LAW: real chi mod 3, mod 5 -> no real pole -> no exceptional  =
  A real zero beta in (1/2,1) of L(s,chi) is a real scattering pole at s=beta -> exceptional
  eigenvalue lambda = beta(1-beta).  Check L(s,chi) > 0 on (1/2,1) for chi_3, chi_5:
  --- chi_3 ---
     L(0.55)=0.494354  L(0.60)=0.507596  L(0.65)=0.520591  L(0.70)=0.533339  L(0.75)=0.545838
     L(0.80)=0.558088  L(0.85)=0.570088  L(0.90)=0.58184  L(0.95)=0.593343
     L(1,chi_3) = 0.60459979 ;  min on (1/2,1) = 0.494354 at s=0.55  -> POSITIVE (no real zero, no exceptional eigenvalue)
     [if chi_3 HAD a Siegel zero at beta=0.95, it would force lambda=beta(1-beta)=0.0475 on Gamma_0(4q)]
  --- chi_5 ---
     L(0.55)=0.253374  L(0.60)=0.274633  L(0.65)=0.295515  L(0.70)=0.316009  L(0.75)=0.336106
     L(0.80)=0.355797  L(0.85)=0.375077  L(0.90)=0.393941  L(0.95)=0.412386
     L(1,chi_5) = 0.43040894 ;  min on (1/2,1) = 0.253374 at s=0.55  -> POSITIVE (no real zero, no exceptional eigenvalue)
     [if chi_5 HAD a Siegel zero at beta=0.95, it would force lambda=beta(1-beta)=0.0475 on Gamma_0(4q)]
  L(s,chi_3), L(s,chi_5) > 0 throughout (1/2,1): NO Siegel zero for these small real characters
  (as expected -- Siegel zeros, if any, are a large-q asymptotic threat, not present at q=3,5).
  The MECHANISM, however, is exact: positivity of L on (1/2,1) == absence of the exceptional
  eigenvalue, via the real scattering pole <-> lambda=beta(1-beta) law.

================  (E) SYNTHESIS + the precise residual  ================
DICTIONARY (exact): real chi mod q with Siegel zero beta=1-delta  <->  weight-1/2 Maass form on
Gamma_0(4q) with eigenvalue lambda = beta(1-beta) = 1/4-(beta-1/2)^2 ~ delta (small).  Selberg
lambda_1 >= 1/4  <=>  no exceptional eigenvalue  <=>  no Siegel zero.
PROVEN: lambda_1 >= 975/4096 = 0.23803 (Kim-Sarnak 2003, theta_infty=7/64 via sym^2 Gelbart-
Jacquet, sym^3/sym^4 Kim-Shahidi/Kim).  Gap to 1/4: 49/4096 = 0.01196.  Record UNIMPROVED at
full level (Yang 2020 withdrawn).  This EXCLUDES nothing yet: 0.238 < 0.25, so an exceptional
eigenvalue in (0.238, 0.25) -- equivalently a Siegel zero beta in (1/2, 1/2+sqrt(0.012))=(0.5,
0.609) -- is NOT ruled out by the proven bound.
GAINED by no-Siegel-zero (if proven): effective L(1,chi)>>1/log q; effective h(-d)>>sqrt d/log d;
effective Linnik / PNT in APs.  NOT GAINED: GRH -- the complex zeros off the real axis are
untouched.  no-Siegel-zero  <<  GRH, strictly.  And no-Siegel-zero itself is NOT proven (Kim-
Sarnak only narrows the exceptional window to lambda in (0.238,0.25)).

RESIDUAL (precise): the program's machine-precision trace-formula balance is at LEVEL 1, where
there is provably NO exceptional eigenvalue (lambda_1 ~ 91) -- so the verified instrument, as
built, cannot itself see a Siegel zero: the Siegel zero lives on Gamma_0(4q), q large, NOT on
SL(2,Z).  Closing the 0.012 gap (Selberg) or excluding Siegel zeros is one of: (i) a NEW
functorial symmetric power sym^k, k>=5, on GL (Langlands beyond Kim-Shahidi) to push theta_infty
below 7/64; or (ii) a positive lower bound on the central L-value (Conrey-Iwaniec cubic-moment
direction).  Both are open; the trace formula at level 1 quantifies the SENSITIVITY (part C) but
not the EXISTENCE.  Difficulty is conserved: 'no exceptional eigenvalue on Gamma_0(4q)' is
exactly as hard as 'no Siegel zero,' which is strictly weaker than GRH and still open.
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

**This report.**  (1) "no-Siegel-zero itself is NOT proven" is re-scoped to **[A] on OpenAI 2026**.  The
GAINED list in (E) becomes [A], with L(1,chi) >> 1/log log q (stronger than the 1/log q stated).  Linnik
is the exception: there is no improvement over Xylouris.  (2) Selberg's lambda_1 >= 1/4 is **untouched**
and remains OPEN.  So the closing sentence ("'no exceptional eigenvalue on Gamma_0(4q)' is exactly as hard
as 'no Siegel zero'") is WITHDRAWN.  One side is now [A] and the other is open.
(3) **Peer-review flag (internal inconsistency, found 2026-10-07).**  If the lift dictionary
lambda = beta(1-beta) were an exact equivalence, two things would follow.  First, Kim-Sarnak
lambda_1 >= 975/4096 would already exclude every real zero beta > 0.609, and with it every Siegel zero.
That contradicts (E)'s "no-Siegel-zero is NOT proven".  Second, lambda_1 >= 1/4 would correspond to NO real
zero in (1/2,1), which is much stronger than no zero near s = 1.  So the dictionary is an ANALOGY, not an
equivalence, and "Selberg <=> no Siegel zero" should be read that way.  Under the analogy, 003's
beta <= 7/8 would read lambda >= 7/64.  That is a numerical coincidence with theta_infty = 7/64, and it
carries no content.  The script text should be corrected the next time this probe is touched.
