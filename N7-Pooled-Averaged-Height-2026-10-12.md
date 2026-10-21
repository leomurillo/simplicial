# One auxiliary for an entire block: the averaged height construction

12 October 2026. This construction pursues the averaged height bound directly. It allows compensation across scales in the divisibility constraints, rather than imposing a separate auxiliary inequality at each scale. Exact finite feasibility is established below; the uniform asymptotic cost estimate remains unproved.

## 1. The sharp calibration permits a genuine block construction

For each x choose B_x=max(2,ceil(x^(1/3))) in the sharp-envelope note. Its unconditional theorem gives

\[
0\le\mathcal E^*_{B_x}(x)-W(x)\le25/432,
\quad W(x)=\psi(x)-\psi(\lfloor x/2\rfloor).
\]

Therefore, for integer X≥2,

\[
\sum_{X<x\le2X}W(x)
\le\sum_{X<x\le2X}\mathcal E^*_{B_x}(x)
\le\sum_{X<x\le2X}W(x)+25X/432.                           \tag{1}
\]

An upper bound for the actual block mass now transfers to the revised-envelope average with only O(X) loss. This is why a single block auxiliary is useful. It does not impose a new consistency constraint on the old independent dual problems, and it does not imply an upper bound for the old coarse-envelope optimum.

## 2. The aggregate divisibility weights

The number of scales x in (X,2X] whose prime-power window contains n is

\[
w_X(n)=\max\bigl(0,\min(2X,2n-1)-\max(X+1,n)+1\bigr).
\tag{2}
\]

Hence the exact block mass is

\[
\mathcal W(X)=\sum_{X<x\le2X}W(x)
=\sum_{2\le n\le2X}\Lambda(n)w_X(n).                     \tag{3}
\]

Its target main term is

\[
A_X=\sum_{X<x\le2X}\frac x2=\frac{X(3X+1)}4.
\]

For k≥1 put

\[
B_{X,k}(n)=\sum_{X<x\le2X}
\left(\left\lfloor\frac{x}{kn}\right\rfloor
      -\left\lfloor\frac{x}{2kn}\right\rfloor\right).
\]

These coefficients can be computed with integer arithmetic alone. If q=floor(N/d), r=N−qd, then

\[
S(N,d):=\sum_{x=1}^{N}\lfloor x/d\rfloor
=dq(q-1)/2+q(r+1),
\]

so B_(X,k)(n)=S(2X,kn)−S(X,kn)−S(2X,2kn)+S(X,2kn).

## 3. The pooled auxiliary theorem

Choose rational c_1,...,c_K satisfying

\[
\boxed{\sum_{k\le K}c_kB_{X,k}(n)\ge w_X(n)
\quad\text{for every integer }2\le n\le2X.}                \tag{4}
\]

Let Q clear all coefficient denominators and define

\[
U_X(c)=\prod_{k\le K}\prod_{X<x\le2X}
\left(\frac{\lfloor x/k\rfloor!}
           {\lfloor x/(2k)\rfloor!}\right)^{Qc_k}.
\]

**Theorem.** This is an integer, and

\[
\prod_{X<x\le2X}\left(
\frac{\operatorname{lcm}(1,\ldots,x)}
     {\operatorname{lcm}(1,\ldots,\lfloor x/2\rfloor)}
\right)^Q\ \mid\ U_X(c).
\tag{5}
\]

**Proof.** Legendre's formula and (4) give

\[
v_p(U_X)=Q\sum_{r\ge1}\sum_kc_kB_{X,k}(p^r)
\ge Q\sum_{r\ge1}w_X(p^r)
\]

for every prime p. The right side is the valuation of the integer on the left of (5), proving integrality and divisibility. ∎

The normalized log-height is the linear objective

\[
\mathcal H_X(c)=\frac{\log U_X(c)}Q
=\sum_{k\le K}c_kT_X(k),
\quad T_X(k)=\sum_{X<x\le2X}F(\lfloor x/k\rfloor),
\tag{6}
\]

where F(j)=log(j!)−log(floor(j/2)!). Thus

\[
\mathcal W(X)\le\mathcal H_X(c).                           \tag{7}
\]

This construction permits some individual scales' valuations to fall short, provided their total at each prime is sufficient. Condition (4) is still a sufficient condition stronger than checking only total prime valuations, because it majorizes each integer-indexed contribution separately. It uses no prime list.

## 4. The theorem that would finish the averaged route

It suffices to construct feasible rational coefficients for all sufficiently large X with

\[
\boxed{\mathcal H_X(c)\le A_X+C\,X^{3/2}(\log X)^m}         \tag{8}
\]

for fixed C,m. A bound O_ε(X^(3/2+ε)) for every ε>0 would also suffice. Equations (1) and (7) transfer it to the averaged sharp-envelope bound; the dyadic telescoping and one-sided Landau argument in the audit note then imply RH.

The full Möbius vector with K=X is feasible and gives equality in (7). Indeed, summing the two-window Möbius identity over x gives Σ_k μ(k)B_(X,k)(n)=w_X(n). This guarantees feasibility but does not prove (8): that certificate has height exactly equal to the unknown block mass.

The original uniform target remains sufficient, but it is stronger than what is needed here. The pooled construction aims directly at the averaged implication.

## 5. Finite construction and exact checks

`empirical/connes_route/pooled_height_majorant.py` searches (4) using log-factorial costs, rationalizes the coefficients, and verifies every inequality after clearing denominators. If rationalization introduces a violation, it increases c_1 by the smallest nonnegative rational correction covering all violations. This works because B_(X,1)(n)>0 for every 2≤n≤2X.

The numerical search restricts each coefficient to [−100,100], before the rational repair. This is a candidate search, not a claim of an unrestricted optimum. Without coefficient bounds, floating-point logarithms produced a spurious report of unboundedness; the mathematical objective has the lower bound (7). The certificate does not depend on the solver's optimality claim.

| X | K | normalized log-height, approximately | excess over A_X |
|---:|---:|---:|---:|
| 100 | 14 | 7,810.548957 | 285.548957 |
| 100 | 42 | 7,634.978935 | 109.978935 |
| 300 | 24 | 69,517.255902 | 1,942.255902 |
| 300 | 72 | 67,196.492356 | −378.507644 |
| 1,000 | 44 | 763,496.147278 | 13,246.147278 |
| 1,000 | 132 | 751,690.332068 | 1,440.332068 |

All six rational certificates satisfy (4) exactly. Their common denominators have between 32 and 129 decimal digits, so K alone understates their arithmetic size. The JSON stores every coefficient. Heights are floating-point diagnostics, not interval-certified bounds; the exact certification concerns feasibility and divisibility.

These samples do not establish (8), a growth exponent, or a comparison with the best independently chosen per-scale auxiliaries. They show that the pooled construction can be instantiated and checked without prime data.

## 6. Next mathematical step

The open task is an explicit X-dependent coefficient rule for (4) whose objective (6) can be bounded by (8), or an upper-bound theorem for the pooled dual. A proof must control the objective uniformly; optimizing a finite list of X values cannot supply that quantifier.

The progress in this pass is the block auxiliary itself and its exact divisibility theorem. The sharp calibration makes its relevance to the averaged envelope rigorous. The required unconditional averaged height bound remains unproved.
