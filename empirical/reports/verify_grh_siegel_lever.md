# verify_grh_siegel_lever — the GRH primorial/large-sieve lever vs the Siegel core

**Probe:** `empirical/verify_grh_siegel_lever.py` (mpmath dps 40; exact `Fraction` for V-sector counts and crossover index). Illustrative numerics, GPD-disciplined — **no proof claimed**.

**Date:** 2026-05-31.

## What it demonstrates

Three quantitative facts pinning where the in-house GRH lever reaches and where the Siegel (exceptional / Landau–Siegel) zero obstructs the average→individual upgrade.

### PART A — primorial lever reach (Paper 43 θ₀(5)=0.538 + ocho §5.3 integer V-sector)

- ocho §5.3 closed form `pure_V(P_n) = 2 + (1/6)Σ_{p≥5}(p²−1)` is an **exact non-negative integer** at every primorial row (asserted in `assert V.denominator==1`, passes for all n tested): 2, 6, 14, 34, 62, 110, … at n=2,3,4,5,6,7.
- Paper 43's **unconditional** primorial-moduli BV level θ₀(5)=0.538 controls the cross-prime (M) error of size `P_n^(1−θ₀)=P_n^0.462`.
- **Crossover:** the positive integer V-sector dominates the M-error using only θ₀=0.538 from primorial index **n\*=3 (P₃=30) onward** (θ_req=1−logV/logP drops below 0.538). n=2 (the P₂=6 row) is the single finite row needing the explicit gap.
- **Honest reach:** this is exactly ocho §5.3's statement — unconditional positivity on **Re(s) > 1/2 + 0.038**, with the **0.038-thick layer down to the critical line the remaining obligation**. Off-critical zeros (and any Siegel zero of the family) live in that layer.

### PART B — large sieve absorbs ONE exceptional zero on average; individual fails

Model: a real χ mod q with Siegel zero β=1−λ/log q contributes a single term `~(X^β/β)²` to the family L² sum `Σ_χ|ψ(X,χ)|² ≪ (X+q²)X`, and shifts `ψ(X;q,a)` by `~−χ(a)X^β/β`.

- For q∈{10³,10⁶}, λ∈{0.5,0.05,0.005}, X=q²: **`absorbed?`=YES in every row** — the single exceptional term is ≤ the large-sieve bound. GRH-on-average is untouched by a Siegel zero.
- But `indiv/main` (individual discrepancy / main term X/φ(q)) is **Θ(1)–Θ(10⁵–10⁶), not →0**: the individual progression is NOT equidistributed at this scale.
- Equidistribution needs `X^(1−β)=X^(λ/log q)` large, i.e. **log X ≫ log q / λ → ∞** as λ→0 (tabulated: log X needed ≈ 138, 1382 at q=10³; 276, 2763 at q=10⁶ for λ=0.05, 0.005). This divergence IS the average→individual obstruction.

### PART C — Deuring–Heilbronn repulsion (only classical handle), quantified

If β=1−λ/log q hugs 1 (λ small), no other zero of any L(s,χ') in the family lies in `Re(s) > 1 − c·log(1/λ)/log q`.

- At q=10⁶: repulsion radius / normal zero-free-region scale = `log(1/λ)` = 0.69, 2.30, 4.61, 6.91 at λ=0.5, 0.1, 0.01, 0.001. A tighter Siegel zero repels the rest of the family by a **larger** factor.
- This is **consistency pressure** (constrains the rest GIVEN the bad zero — Linnik's theorem is the consequence), **not exclusion**. Excluding the zero = a lower bound L(1,χ)≫1/√q (Siegel, ineffective) or GRH-strength 1/polylog (open).

## The precise residual (primorial-CRT contrast)

The family mod P_n the program handles "all at once" via CRT is the **same** family Deuring–Heilbronn acts on. But CRT rigidity (character orthogonality, exact integer packet ranks φ(d)=∏(p−1)) is an **algebraic** fact about ℤ/P_n; it delivers the large-sieve mean-square (Part B) and the integer V-sector count (Part A) — both **averaged/structural**. It yields **no lower bound on L(1,χ) for the lone real χ mod P_n**. The Siegel zero is an **analytic** property of one real L-function at the strip edge; CRT touches the whole family symmetrically and is blind to the asymmetry of a single real character. **That asymmetry is the irreducible residual.**

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

**This report.**  Part C's "Excluding the zero = ... GRH-strength 1/polylog (open)" is re-scoped to
**[A] on OpenAI 2026**.  The Part B rows become counterfactual.  Under beta <= 7/8, lambda = (1-beta) log q
is at least (log q)/8 (about 0.86 at q = 10^3), so lambda in {0.5, 0.05, 0.005} cannot occur for
q >= 10^3.  Part A (the 0.038-thick layer above 1/2) is unaffected, because 7/8 is far weaker than 0.538.
The structural point of "The precise residual" STANDS: CRT rigidity is blind to a single real character.
The residual is now discharged EXTERNALLY by a half-plane theorem, not by CRT.
