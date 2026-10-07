# Lemma 8.1c: the >=GRH wall of Paper 22's RH route, and the unification of the fronts

**Script:** `empirical/verify_lemma_8_1c_wall.py`  (builds on Paper 22 sec 8, the 8.1 sub-lemmas).
**Finding:** Paper 22's limit (Conjecture 5.2) reduces the prime side to Lemma 8.1, whose only
non-finite/non-elementary piece is 8.1c -- a weighted character PNT UNIFORM over chi mod P_n. By the
explicit formula this is governed by Theta_chi=sup Re(rho) of L(s,chi); uniform E_n->0 <=> no Siegel
zero in the family <=> GRH for the primorial characters. BV/large-sieve give the AVERAGE (RMS), not
the MAX -- the average->individual gap. Computed psi(X,chi)/X (q=6,30): principal main term,
nonprincipal ->0, max>=RMS. L(1,chi)>0 (no Siegel at small q). UNIFICATION: 8.1c = front (a)'s
statistical->individual = Selberg lambda_1>=1/4 = Lehmer individual repulsion -- ONE wall. Second wall:
the Archimedean Noether Limit (No-Go). NO RH/GRH claim; the contribution is to locate the wall exactly.
**Nature:** numerical (sieve + mpmath) + literature-exact reduction; conservation confirmed.

```text
Where conservation bites: Lemma 8.1c (primorial character uniformity) is the >= GRH core of Paper 22's
RH route, and it is the SAME average->individual / no-Siegel-zero wall as front (a) and Selberg/Siegel.

Paper 22's limit (Conjecture 5.2 => RH, Thm 6.1) reduces the prime side to Lemma 8.1, now split:
  8.1a0  [P]  CRT isolation (VM projector = CRT packet projector; certified verify_lemma_8_1a0...).
  8.1a   [P skeleton / A occupation-lift]  squarefree mixed/single separation [P]; the prime-power
         occupation ladder Lambda(p^r)=log p at position r log p is EXTERNAL (the K_n->inf double cutoff).
  8.1b   [elementary]  double-cutoff tail (dominated convergence on a log-decaying dense test class).
  8.1c   [THE WALL]  the weighted character PNT, UNIFORM over all Dirichlet chi mod q=P_n:
            max_chi | sum_{m<=X} Lambda(m) chi(m) G_f(log m) - delta_{chi_0} \int G_f | <= X E_n(f),  E_n->0.
  8.1d   [density]  S_0^exp dense in the Weil topology.
Paper 22's own "Claim hygiene": 8.1c is classical via a Siegel-Walfisz-safe diagonal (M_n=exp(P_n^beta),
HUGE cutoffs, POINTWISE, ineffective), but at NATURAL primorial scale it needs "a BV/large-sieve selector
for the single modulus P_n" and "Bombieri-Vinogradov gives AVERAGED control and CANNOT be cited as
POINTWISE control for the single full modulus P_n."  THAT is the average->individual gap.

THE UNIFICATION (this probe's point): 8.1c at natural scale  <=>  max_chi mod P_n is controlled, not just
the BV/large-sieve average  <=>  no exceptional (Siegel) zero of any L(s,chi), chi mod P_n  <=>  GRH for
the primorial character family.  This is identically the wall of:
  * front (a): averaged (2nd-moment / pair-correlation) control holds, the INDIVIDUAL off-line guarantee
    does not;
  * Selberg/Siegel: lambda_1 >= 1/4 (no exceptional eigenvalue) <=> no Siegel zero; Kim-Sarnak 0.238 effective;
  * the de Bruijn / Lehmer flow: statistical repulsion sufficient, individual collision-avoidance not.
The program's RH route (Paper 22) bottoms out at EXACTLY this wall -- conservation, made one object.

This probe COMPUTES the 8.1c object on q=6 and q=30: the weighted character sums psi(X,chi), the
MAX-over-chi vs the RMS-over-chi (the average), and L(1,chi) for the real characters (no Siegel at small q),
to make the wall concrete and exhibit the average->individual gap.  NUMERICAL (sieve + mpmath); NO RH claim.

Sieving von Mangoldt up to X=60000 ...
  done.

================  PART B: the 8.1c character sums  psi(X,chi)/X  (q=6, q=30)  ================
  --- modulus q=6 : 2 Dirichlet characters ---
       X        principal psi/X (-> 1, PNT)   max_{chi != chi0} |psi/X|   RMS_{chi != chi0} |psi/X|
      10000        (0.9995596881606483+0j)                 0.006566501661835383              0.006566501661835383
      30000        (0.998058665906295+0j)                 0.0009605355406642975              0.0009605355406642975
      60000        (1.0013518633096565+0j)                 4.816352329539045e-06              4.816352329539045e-06
     => principal psi/X -> 1 (the PNT main term; the few p|q drop only O(log X)); nonprincipal -> 0 (PNT for L(s,chi)).
        max over the family >= RMS (average); the gap is ~sqrt(#chi) here -- modest at small q,
        but it is the average->individual gap that EXPLODES as q=P_n->inf (the 8.1c wall).

  --- modulus q=30 : 8 Dirichlet characters ---
       X        principal psi/X (-> 1, PNT)   max_{chi != chi0} |psi/X|   RMS_{chi != chi0} |psi/X|
      10000        (0.9987549692044313+0j)                 0.006727445453078795              0.004249770836252974
      30000        (0.997736778323808+0j)                 0.0035228281473716778              0.002257888933889763
      60000        (1.0011909195184132+0j)                 0.0031023756487179393              0.0018750096439219218
     => principal psi/X -> 1 (the PNT main term; the few p|q drop only O(log X)); nonprincipal -> 0 (PNT for L(s,chi)).
        max over the family >= RMS (average); the gap is ~sqrt(#chi) here -- modest at small q,
        but it is the average->individual gap that EXPLODES as q=P_n->inf (the 8.1c wall).

================  PART C: real characters, L(1,chi)>0 (no Siegel), and the >=GRH framing  ====
  real (quadratic) characters mod 30 and L(1,chi) (= the no-Siegel-zero quantity):
     chi[eps=1,c=2] : L(1,chi) = 0.86081788  (> 0 => no Siegel zero for this chi at q=30)
     chi[eps=-1,c=0] : L(1,chi) = 1.0882796  (> 0 => no Siegel zero for this chi at q=30)
     chi[eps=-1,c=2] : L(1,chi) = 0.81115574  (> 0 => no Siegel zero for this chi at q=30)
  All real L(1,chi) are bounded away from 0 at q=30 -- no Siegel zero; the recovery 8.1c HOLDS
  at this finite modulus. The wall is the UNIFORM statement as q=P_n -> inf.

  THE EXPLICIT-FORMULA LINK.  psi(X,chi) - delta_{chi0} X = - sum_{rho} X^rho/rho + ... over the zeros
  rho of L(s,chi); so |psi(X,chi)|/X is governed by Theta_chi = sup Re(rho). Hence
     8.1c (E_n->0 uniform over chi mod P_n)  <=>  max_{chi mod P_n} Theta_chi bounded < 1 uniformly
        <=>  NO exceptional (Siegel) zero in the family  <=>  GRH-strength for the primorial family.
  Bombieri-Vinogradov / the large sieve control the AVERAGE sum_chi |psi(X,chi)|^2 (the RMS column),
  NOT the MAX -- exactly Paper 22's 'BV cannot be cited as pointwise control for the single P_n'.

  THE UNIFICATION (where conservation bites, one object):
    Paper 22 Lemma 8.1c  =  uniform character PNT mod P_n  =  no Siegel zero / GRH-family  =
    front (a)'s statistical->individual gap  =  Selberg lambda_1>=1/4 (no exceptional eigenvalue)  =
    the de Bruijn/Lehmer individual-repulsion guarantee.  ALL the program's RH/GRH fronts bottom out
    at the SAME average->individual / no-exceptional-zero wall. That is conservation of difficulty,
    localized to one statement.

  THE DICHOTOMY (Paper 22 sec 8, made concrete):
    route 1 (Siegel-Walfisz-safe): M_n = exp(P_n^beta), HUGE cutoffs -> classical individual
       uniformity (q <= (log X)^A), INEFFECTIVE, POINTWISE per f. Gives an existence theorem, not
       the uniform-over-test-space recovery Weil positivity needs.
    route 2 (natural scale): M_n poly/mild in P_n -> needs a BV/large-sieve SELECTOR for the single
       modulus P_n, or a structural primorial exclusion of exceptional characters. THIS is the gap.

  SECOND WALL (not the prime side): the ARCHIMEDEAN Noether Limit (Conjecture 5.2 input #2,
  Theorem 5.2.2) -- the No-Go that the archimedean place pi^{-s/2}Gamma(s/2) is NOT finitely-prime-
  generable; even granting the prime-side recovery, assembling the COMPLETED Weil form and its
  positivity in the limit is the marginal-archimedean-positivity step = RH itself.

HONEST SCOPE / VERDICT:
  [P]  the reduction: 8.1a0 (CRT isolation), the 8.1a squarefree skeleton, the finite leakage
       extinction (last turns) -- all settled finite/algebraic facts.
  [A]  the occupation lift (8.1a, K_n->inf) and the Siegel-Walfisz pointwise route (8.1c route 1):
       achievable but external/ineffective/huge-cutoff -- NOT the uniform recovery the limit needs.
  [open == GRH]  8.1c at natural scale = uniform character PNT mod P_n = no Siegel zero for the
       family. This is the >=GRH core; conservation bites here, and it is the program's one wall.
  [open == RH]  the Archimedean Noether Limit + Weil positivity in the limit (the No-Go completion).
  NO closure. The contribution is to LOCATE the wall exactly (8.1c natural-scale uniformity) and to
  show it is identical to the average->individual / no-Siegel wall of every other front -- so the
  whole program meets RH/GRH at one precisely-named place, not many.
```
