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
