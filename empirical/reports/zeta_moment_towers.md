# Front (a) cont'd: the two towers (Beyond-CBS) transported to zeta's moments

**Script:** `empirical/verify_zeta_moment_towers.py`  (builds on `verify_repulsion_to_individual.py`).
**Finding:** <|zeta|^{2k}> ~ a_k g_k (log T)^{k^2} IS the Beyond-CBS two towers as two factors -- g_k
spectral/dynamical (CUE/Barnes), a_k arithmetic/distributional (Euler product); equal only at k=1 (the
Gaussian corner = Selberg CLT). Computed + verified vs proven 2nd (=1) and 4th (=1/2pi^2) moments. The
mollifier proportion-on-line climbs this tower (k=1 = Levinson-Conrey 41.67%); the 4th-moment rung is
forced (not 3rd) by zeta's functional-equation symmetry (= Beyond-CBS symmetric world, first bend order 4);
the L-function family ring re-opens an order-3 TENSOR (cross-character trilinear, Bettin-Chandee) = the CBS
cross-packet cubic, the lever that extends theta on primorial moduli.
**Nature:** numerical (mpmath) + Beyond-CBS structural transport. NO claim RH is proved.

```text
FRONT (a), continued: the TWO TOWERS of "Beyond the Conductor Blind Spot" transported to zeta,
and why the mollified 4th moment (not 3rd) is the next rung -- with the ring/trilinear escape.

Beyond-CBS load-bearing distinction (its front-matter): two spectral towers, coinciding only at the
Gaussian -- (D) DYNAMICAL = eigenfunctions of the transition operator (the zero spectrum / GUE here);
(S) DISTRIBUTIONAL = cumulants/moments of the stationary law (the moments of zeta here).  CBS grades
the S-tower.  App B's sharpened fact: an UNSTRUCTURED SYMMETRIC world has scalar order-3 = 0 and first
bends at ORDER 4; a RING-structured world keeps an order-3 TENSOR (Amari-Chentsov cross-packet cubic)
alive even under symmetry.

TRANSPORT TO ZETA (the program-native reading of front (a)):
  * distributional tower  = the moment hierarchy  <|zeta(1/2+it)|^{2k}> ,  k = 1,2,3,...
  * dynamical tower       = the zero spectrum (GUE pair correlation, prior probe)
  * Gaussian corner where they coincide = SELBERG'S CLT: log|zeta(1/2+it)| ~ N(0, (1/2)loglog T).
  * Keating-Snaith / CFKRS: <|zeta|^{2k}> ~ a_k * g_k * (log T)^{k^2}, and this factorization IS the two
    towers as two FACTORS -- g_k the RANDOM-MATRIX (CUE, spectral/dynamical) factor, a_k the ARITHMETIC
    (Euler-product, distributional) factor.  At k=1 (2nd moment) a_1 g_1 = 1: the Gaussian corner, towers
    coincide.  For k>=2 they SPLIT (a_k != 1 arithmetic, g_k != 1 spectral) -- the beyond-2nd-order content.

WHY THE 4th MOMENT IS THE NEXT RUNG (and why this matches Beyond-CBS exactly):
  single zeta is FUNCTIONAL-EQUATION symmetric, so -- like Beyond-CBS's symmetric world (scalar kappa_3=0,
  first bend at order 4) -- its natural higher rung is the 4th moment (the hierarchy is even: 2,4,6,...).
  Levinson-Conrey (proportion on the line, prior probe, ceiling ~5/12) is a 2nd-moment method = the k=1
  Gaussian-corner rung.  Breaking past it = the MOLLIFIED 4th moment = the k=2 rung = first split tower.

THE RING ESCAPE (where order 3 survives, and the program's primorial direction lives):
  the L-function FAMILY mod q is a RING (Z/q).  There the cross-character TRILINEAR object (Bettin-Chandee
  theta_0 ~ 0.515) is the order-3 TENSOR the ring keeps alive where the single-function scalar (killed by
  the functional equation) vanishes -- exactly the CBS cross-packet cubic, transported.  It is what extends
  the mollifier length theta past 4/7 on primorial moduli.  So the program's two distinctive assets line up:
  CBS's scalar-vs-tensor distinction explains WHY trilinear (order-3 tensor) bounds are the right tool.

This probe COMPUTES the two tower-factors a_k (arithmetic Euler product) and g_k (CUE/Barnes) for k=1..5,
verifies them against the proven moments (k=1: 1; k=2: 1/(2 pi^2)), and lays out the refined thermometer.
NUMERICAL (mpmath); honest -- proves nothing about RH; it gives front (a) a computed two-tower coordinate.

================  PART A: the moment factorization <|zeta|^{2k}> ~ a_k g_k (log T)^{k^2}  =====
  g_k = CUE/Barnes (spectral/dynamical tower factor);  a_k = arithmetic Euler product (distributional).
  computing a_k over primes up to 2,000,000 (tail O(1/p^2), so this is accurate)...
    (148933 primes)

    k    g_k (CUE/Barnes)        a_k (arithmetic)        a_k*g_k (moment leading coeff)
    1    1.0                     1.0                     1.0
    2    0.08333333333           0.6079271215            0.05066059346
    3    0.0001157407407         0.04932168794           5.708528697e-6
    4    1.148221634e-9          0.0002146816598         2.465021263e-13
    5    4.520272874e-17         3.132566641e-8          1.416005601e-24

  VERIFY against proven moments:
    k=1 (2nd moment, Hardy-Littlewood):  a_1 g_1 = 1.0   (proven 1)            match: True
    k=2 (4th moment, Ingham):            a_2 g_2 = 0.0506605934601   (proven 1/2pi^2=0.05066059182)  match: True
    (also a_2 = 6/pi^2 = 1/zeta(2): computed 0.6079271215 vs 0.6079271019, match True)
    k=3 (6th moment, Conrey-Ghosh conj.): a_3 g_3 = 5.708528697e-6  (conj. 42 * a_3 g_3-form; leading coeff)

  READING: at k=1 (the 2nd moment) a_1 g_1 = 1 EXACTLY -- the GAUSSIAN CORNER, where the two towers
  coincide (Selberg CLT: log|zeta| is Gaussian).  For k>=2 the coefficient SPLITS into a_k (arithmetic)
  times g_k (spectral) -- both != 1 -- the beyond-second-order content.  This is the Beyond-CBS two-
  tower picture, exactly: distributional (a_k) and dynamical/spectral (g_k) factors, equal only at k=1.

================  PART B: Selberg's CLT = the Gaussian 2nd-order floor (towers coincide)  =====
  Selberg: log|zeta(1/2+it)| / sqrt((1/2)loglog T) -> N(0,1).  So the BULK value-distribution of
  zeta is Gaussian (log-normal |zeta|) -- the second-order picture, the conductor-blind-spot floor.
  A PURE log-normal with that variance would give moment coefficient 1 for every k.  The TRUE
  coefficients a_k g_k != 1 (k>=2) are the deviation -- the moments are dominated by RARE LARGE
  VALUES (the tails), which the 2nd-order CLT cannot see.  That deviation is the higher-cumulant /
  higher-tower content -- the same order>=2-sufficiency departure CBS names, here in zeta's values:
     k   a_k g_k        log-normal floor   deviation (a_k g_k - 1)   [tower split = beyond 2nd order]
     1   1.0            1                 -1.7797688e-27
     2   0.050660593    1                 -0.94933941
     3   5.7085287e-6   1                 -0.99999429
     4   2.4650213e-13   1                 -1.0
     5   1.4160056e-24   1                 -1.0
  => the deviation is 0 at k=1 (Gaussian corner) and grows with k: the tower-split IS the moment's
     departure from the Selberg-Gaussian floor, factored as arithmetic (a_k) x spectral (g_k).

================  PART C: the refined thermometer + the ring/trilinear escape  ================
  PROPORTION-ON-LINE (prior probe) climbs the DISTRIBUTIONAL tower via mollified moments:
    * k=1 rung (2nd moment) = Levinson-Conrey, ceiling ~5/12 = 41.67%  [the Gaussian corner rung].
    * k=2 rung (4th moment) = the next rung, and it IS the 4th (not 3rd) for the SAME reason
      Beyond-CBS's SYMMETRIC world first bends at order 4: single zeta is functional-equation
      symmetric, so its moment hierarchy is EVEN (2,4,6,...); the scalar order-3 is absent.
      The mollified 4th moment with a long mollifier is the open object that would raise the
      thermometer -- the exact analytic frontier named in the prior probe.

  THE RING ESCAPE (where order 3 survives -- the program's primorial direction):
    Beyond-CBS App B: a RING-structured index keeps an order-3 TENSOR (Amari-Chentsov cross-packet
    cubic) alive even under symmetry, where the scalar 3rd cumulant vanishes.  Transported: the
    L-FUNCTION FAMILY mod q is a ring Z/q; the cross-character TRILINEAR sum (Bettin-Chandee,
    theta_0 ~ 0.515) is precisely that order-3 tensor -- the CBS cross-packet cubic on the character
    group.  It is the object that extends the mollifier length theta past Conrey's 4/7 on primorial
    moduli.  So CBS's scalar-vs-tensor distinction EXPLAINS the tool: single zeta forces order 4,
    but the character-family ring re-opens order 3 (trilinear), which is the cheaper lever.

  THE TWO-TOWER THERMOMETER (front (a), refined by Beyond-CBS):
     moment rung k    object                              status
       k=1 (2nd)      Gaussian corner / Selberg CLT       a_1 g_1 = 1; Levinson-Conrey 41.67%
       k=2 (4th)      first split tower (a_2 g_2=1/2pi^2)  mollified-4th-moment frontier (open)
       ring order-3   cross-char trilinear tensor          Bettin-Chandee theta_0~0.515 (program lever)
       k -> infinity  all rungs / full tower               = RH (100% on the line)

================  PART D: honest residual + next step  ================
[P] computed: the two tower-factors a_k (arithmetic) and g_k (spectral), verified against the proven
    2nd (=1) and 4th (=1/2pi^2) moments; the factorization a_k g_k IS the Beyond-CBS two towers, equal
    only at the k=1 Gaussian corner.
[A] structural: proportion-on-line = climbing the distributional tower; stuck at k=1 (~41.67%); the
    4th-moment rung is forced (not 3rd) by zeta's functional-equation symmetry = Beyond-CBS symmetric
    world; the character-family ring re-opens an order-3 TENSOR (trilinear) = the CBS cross-packet cubic.
[open == RH] climbing to k -> infinity (all moment orders) = 100% on the line = RH.  Difficulty
    conserved -- but the coordinate is now explicit and matched to the program's two distinctive assets
    (the cumulant/CBS tower, and the primorial/trilinear character-family machinery).

NEXT STEP (concrete, fundable): set up the MOLLIFIED 4th moment with a Dirichlet-polynomial mollifier
  on a primorial modulus and test whether the program's cross-character (ring/tensor) structure makes
  the off-diagonal (the order-3 trilinear term) more tractable than the generic case -- i.e. whether
  the CBS cross-packet selection rule k+l+m=0 (mod q) organizes the trilinear sum.  That is the exact
  realization of 'raise the thermometer' and it is a finite analytic-number-theory target, not RH.
```
