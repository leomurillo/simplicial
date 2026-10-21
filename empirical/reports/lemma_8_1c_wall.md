# Lemma 8.1c: primorial character uniformity in Paper 22's RH route (re-scoped Oct 2026)

**Script:** `empirical/verify_lemma_8_1c_wall.py`  (builds on Paper 22 sec 8, the 8.1 sub-lemmas).
**Finding:** Paper 22's limit (Conjecture 5.2) reduces the prime side to Lemma 8.1.  Its analytic
piece 8.1c is a weighted character PNT UNIFORM over chi mod P_n, governed by Theta = max sup Re(rho).
**Correction:** earlier versions said 'uniform E_n->0 <=> no Siegel zero <=> GRH'.  That was an
overstatement.  Any fixed half-plane Theta <= theta < 1 suffices, for X >= (log P_n)^(2/(1-theta)+eps).
OpenAI 2026 (github.com/openai/math, family 003; model-generated; OpenAI reports Lean formalization)
gives theta = 7/8 for every Dirichlet L.  So 8.1c route 2 is now [A], resting on OpenAI 2026
(Paper 22 Proposition 8.1c').  BV/large sieve still give only the average (RMS), not the max.
The 'one wall' unification with Selberg lambda_1 >= 1/4 and pair correlation is WITHDRAWN: those concern
zeros on the critical line, and 8.1c needs only a strip.  The remaining wall of Paper 22 is archimedean
(the Archimedean Noether Limit).  NO RH/GRH claim.
**Nature:** numerical (sieve + mpmath) + literature-exact reduction.  Numerics illustrate; they prove nothing uniform.

```text
Lemma 8.1c (primorial character uniformity) in Paper 22's RH route: what it needs, and what discharges it.

Paper 22's limit (Conjecture 5.2 => RH, Thm 6.1) reduces the prime side to Lemma 8.1, now split:
  8.1a0  [P]  CRT isolation (VM projector = CRT packet projector; certified verify_lemma_8_1a0...).
  8.1a   [P skeleton / A occupation-lift]  squarefree mixed/single separation [P]; the prime-power
         occupation ladder Lambda(p^r)=log p at position r log p is EXTERNAL (the K_n->inf double cutoff).
  8.1b   [elementary]  double-cutoff tail (dominated convergence on a log-decaying dense test class).
  8.1c   [A, on OpenAI 2026]  the weighted character PNT, UNIFORM over all Dirichlet chi mod q=P_n:
            max_chi | sum_{m<=X} Lambda(m) chi(m) G_f(log m) - delta_{chi_0} \int G_f | <= X E_n(f),  E_n->0.
  8.1d   [density]  S_0^exp dense in the Weil topology.

Route 1 (Siegel-Walfisz-safe, M_n = exp(P_n^beta)) was always classical: huge cutoffs, ineffective.
Route 2 (natural scale, M_n polynomial in P_n) was the open finite-place gap.  BV / the large sieve give
the AVERAGE over chi (the RMS column below), not the MAX, so they do not settle it.

CORRECTION (Oct 2026).  Earlier versions of this probe said "uniform E_n->0 <=> no Siegel zero <=> GRH for
the primorial characters", and called this the same obstruction as Selberg lambda_1>=1/4.  That
overstated it.  By the explicit formula, E_n is governed by Theta = max_chi sup Re(rho).  ANY fixed
half-plane Theta <= theta < 1 gives
    |psi(X,chi) - delta X| << X^theta log^2(qX),    E_n << X^(theta-1) log^2(P_n X) -> 0
for X >= (log P_n)^(2/(1-theta)+eps).  GRH (theta=1/2) only improves the exponent.  Excluding Siegel zeros
is necessary at polynomial scale but weaker than a fixed half-plane.  The fixed half-plane theta = 7/8 is
now Theorem 1.1 of OpenAI, "The Quasi-Riemann Hypothesis" (30 Sep 2026, github.com/openai/math, family
003).  It is model-generated, and OpenAI reports it as Lean-formalized.  Paper 22 Proposition 8.1c' gives
the derivation.  So route 2 is DISCHARGED at tier [A], resting on OpenAI 2026.

The remaining genuine wall of Paper 22 is the ARCHIMEDEAN one: the Archimedean Noether Limit and Weil
positivity in the limit.  A zero-free strip 1/8 <= Re rho <= 7/8 says nothing about Re rho = 1/2.

This probe COMPUTES the 8.1c object on q=6 and q=30: the character sums psi(X,chi), MAX-over-chi vs
RMS-over-chi, the ratio of the MAX to the 7/8 envelope X^(-1/8) log^2(qX), and L(1,chi) for the real
characters.  NUMERICAL (sieve + mpmath).  Numerics at small q illustrate the bound; they prove nothing
uniform.  NO RH claim.

Sieving von Mangoldt up to X=60000 ...
  done.

================  PART B: the 8.1c character sums  psi(X,chi)/X  (q=6, q=30)  ================
  --- modulus q=6 : 2 Dirichlet characters ---
       X        principal psi/X (-> 1, PNT)   max_{chi != chi0} |psi/X|   RMS_{chi != chi0} |psi/X|   max / [X^(-1/8) log^2(qX)]
      10000        (0.9995596881606483+0j)                 0.006566501661835383              0.006566501661835383              0.0001715
      30000        (0.998058665906295+0j)                 0.0009605355406642975              0.0009605355406642975              2.38e-5
      60000        (1.0013518633096565+0j)                 4.816352329539045e-06              4.816352329539045e-06              1.164e-7
     => principal psi/X -> 1 (the PNT main term; the few p|q drop only O(log X)); nonprincipal -> 0 (PNT for L(s,chi)).
        max over the family >= RMS (average); the gap is ~sqrt(#chi) here, modest at small q.
        The last column (max over the 7/8 envelope) stays small, as Prop 8.1c' predicts.  Illustration only.

  --- modulus q=30 : 8 Dirichlet characters ---
       X        principal psi/X (-> 1, PNT)   max_{chi != chi0} |psi/X|   RMS_{chi != chi0} |psi/X|   max / [X^(-1/8) log^2(qX)]
      10000        (0.9987549692044313+0j)                 0.006727445453078795              0.004249770836252974              0.0001338
      30000        (0.997736778323808+0j)                 0.0035228281473716778              0.002257888933889763              6.799e-5
      60000        (1.0011909195184132+0j)                 0.0031023756487179393              0.0018750096439219218              5.916e-5
     => principal psi/X -> 1 (the PNT main term; the few p|q drop only O(log X)); nonprincipal -> 0 (PNT for L(s,chi)).
        max over the family >= RMS (average); the gap is ~sqrt(#chi) here, modest at small q.
        The last column (max over the 7/8 envelope) stays small, as Prop 8.1c' predicts.  Illustration only.

================  PART C: real characters, L(1,chi)>0, and the half-plane framing  ================
  real (quadratic) characters mod 30 and L(1,chi):
     chi[eps=1,c=2] : L(1,chi) = 0.86081788
     chi[eps=-1,c=0] : L(1,chi) = 1.0882796
     chi[eps=-1,c=2] : L(1,chi) = 0.81115574
  All real L(1,chi) at q=30 are bounded away from 0.  This is a finite check at one modulus.

  THE EXPLICIT-FORMULA LINK.  psi(X,chi) - delta_{chi0} X = - sum_{rho} X^rho/rho + ... over the zeros
  rho of L(s,chi), so |psi(X,chi)|/X is governed by Theta = max_chi sup Re(rho).  Precisely:
     Theta <= theta < 1 uniformly  ==>  E_n << X^(theta-1) log^2(P_n X) -> 0 for X >= (log P_n)^(2/(1-theta)+eps).
  GRH is NOT needed.  No-Siegel-zero is necessary at polynomial scale (a real zero with 1-beta <= c/log q
  contributes X^(beta-1) >= e^(-cA) at X = q^A), but it is weaker than a fixed half-plane.
  BV / the large sieve control the AVERAGE sum_chi |psi(X,chi)|^2 (the RMS column), not the MAX.

  THE DISCHARGE (Oct 2026).  OpenAI 2026 (family 003, Thm 1.1): every Dirichlet L(s,chi) is zero-free
  in Re s > 7/8 [A; model-generated; OpenAI reports Lean formalization].  The functional equation then
  puts every nontrivial zero in 1/8 <= beta <= 7/8.  The truncated explicit formula with T = X gives
  |psi(X,chi) - delta X| << X^(7/8) log^2(qX), so 8.1c route 2 holds with M_n polynomial in P_n.
  (Paper 22, Proposition 8.1c'.)

  RE-SCOPED COMPARISON.  The earlier claim that 8.1c, Selberg lambda_1 >= 1/4, pair correlation and
  de Bruijn-Newman are 'one' obstruction is withdrawn.  8.1c needs only a STRIP.  The others are
  statements about zeros ON the critical line.  The strip gives de Bruijn-Newman Lambda <= 9/32 only,
  which is worse than Polymath's 0.22, and leaves Re rho = 1/2 open.

  THE ROUTES (Paper 22 sec 8):
    route 1 (Siegel-Walfisz-safe): M_n = exp(P_n^beta), HUGE cutoffs, classical individual
       uniformity (q <= (log X)^A), INEFFECTIVE.
    route 2 (natural scale): M_n polynomial in P_n.  Was the gap.  Now [A] on OpenAI 2026, with
       EFFECTIVE constants and threshold X_n = (log P_n)^(16+eps) ~ p_n^(16+eps).

  THE WALL THAT REMAINS (not the prime side): the ARCHIMEDEAN Noether Limit (Conjecture 5.2 input #2,
  Theorem 5.2.2).  The archimedean place pi^{-s/2}Gamma(s/2) is NOT finitely-prime-generable (No-Go).
  Even granting the prime-side recovery, assembling the COMPLETED Weil form and its positivity in the
  limit is the marginal-archimedean-positivity step, which is RH itself.

HONEST SCOPE / VERDICT:
  [P]  8.1a0 (CRT isolation), the 8.1a squarefree skeleton, the finite leakage extinction.
  [A]  8.1c route 1 (Siegel-Walfisz, ineffective) and 8.1c route 2 (natural scale, on OpenAI 2026).
  [A]  the 8.1a occupation lift (K_n -> inf): external, still to be written in.
  [open]  projective critical-leaf closure (Theorem 5.1.3) and 8.1d density.
  [open == RH]  the Archimedean Noether Limit + Weil positivity in the limit.
  NO RH claim.  The finite-place character side no longer meets RH/GRH.  Paper 22's wall is archimedean.
```
