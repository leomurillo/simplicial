# Averaged height: repaired proof and its connection to the uniform target

12 October 2026. Independent examination of Paper 53 §§4.12–4.14. This note preserves the original manuscript. It proves the short-interval estimate by a different argument and makes the discrete averaging exact. The conclusions involving RH remain conditional; no unconditional square-root height bound is established.

## 1. Which optimum is being bounded

The exact factorial optimum H* and the Stirling-envelope optimum E* are different. Here E* is the unrestricted-complexity optimum from §4.12(c), after grouping all k≤x/2 with the same floor(x/k). It is not the earlier experiment restricted to k≤ceil(sqrt x).

Write W(x)=ψ(x)−ψ(floor(x/2)), and

\[
V(x)=\sum_{m\ge2}|M(x/m)-M(x/(m+1))|.
\]

Only nonempty integer cells contribute. The grouped Möbius construction gives

\[
W(x)\le E^*(x)\le E(\mu;x)
\le W(x)+(\log x+2)V(x).                                  \tag{1}
\]

The grouping identity follows from floor(floor(x/n)/k)=floor(floor(x/k)/n). Its feasibility is the exact two-window Möbius identity. These are unconditional algebraic facts.

The Stirling allowance can also be checked analytically, rather than through a finite numerical range. Put F(m)=log(m!)−log(floor(m/2)!), S(y)=(y/2)log y+(y/2)(log2−1), and b(y)=(1/2)log y+1. Using

\[
\log(n!)=(n+\tfrac12)\log n-n+\tfrac12\log(2\pi)+r_n,
\quad 0<r_n<1/(12n),
\]

gives, for m=2l,

\[
F(m)-S(m)=\tfrac12\log2+r_{2l}-r_l.
\]

For odd m≥3, use F(m)=F(m−1)+log m and S'(y)=(1/2)log(2y). This bounds F(m)−S(m) between (1/2)log m−1/12 and (1/2)log m+(1/2)log(m/(m−1))+1/24. On m≤y<m+1 subtract the integral of S' from m to y. These inequalities imply |F(floor y)−S(y)|≤b(y) for every y≥2. Since S±b are increasing there, the cell intersection of these brackets contains F(m), and its width is at most log x+2. This proves the penalty bound in (1).

## 2. Short-interval mean square: a direct proof under RH

**Lemma.** Under RH, for every ε>0, Y≥2 and 1≤T≤Y,

\[
\int_Y^{2Y}|M((1+1/T)y)-M(y)|^2\,dy
\ll_\varepsilon Y^{2+\varepsilon}/T.                       \tag{2}
\]

Fix positive a,η with η<1/2 and 2a+2η<ε. Let σ=1/2+a and δ=log(1+1/T). The standard RH consequences used here are

\[
M(u)\ll_\beta u^{1/2+\beta}\quad(\beta>0),\qquad
|1/\zeta(\sigma+it)|\ll_{a,\eta}(2+|t|)^\eta.
\tag{3}
\]

The latter follows from Littlewood's bounds for log ζ in a fixed half-plane to the right of 1/2; see the discussion of Titchmarsh §14.2 in [Simonič, *Estimates for L-functions in the Critical Strip Under GRH*](https://link.springer.com/article/10.1007/s00009-023-02289-2). These are RH-dependent analytic inputs, not consequences of floor identities.

Set S_T(y)=M(e^δy)−M(y), with M(y)=0 for 0<y<1. Taking β<a in (3) makes the relevant weighted Mellin integrals and square integrals converge. Direct substitution gives

\[
\int_0^\infty S_T(y)y^{-s-1}\,dy
=\frac{e^{\delta s}-1}{s\zeta(s)},\qquad\Re s=\sigma.
\tag{4}
\]

Indeed, partial summation first gives the transform of M as 1/(sζ(s)); conditional convergence of the Möbius Dirichlet series on this line follows from the same M bound. No truncated Perron formula is needed.

Mellin–Plancherel now yields

\[
\int_0^\infty|S_T(y)|^2y^{-2\sigma-1}\,dy
=\frac1{2\pi}\int_{\mathbb R}
\frac{|e^{\delta(\sigma+it)}-1|^2}{|\sigma+it|^2}
|1/\zeta(\sigma+it)|^2\,dt.
\tag{5}
\]

The kernel is bounded by a constant times min(T^(−2),(1+|t|)^(−2)). Consequently the right side is

\[
\ll_{a,\eta}\int_0^\infty(2+t)^{2\eta}
             \min(T^{-2},(1+t)^{-2})\,dt
\ll_{a,\eta}T^{-1+2\eta}.
\]

Multiplying by (2Y)^(2σ+1), and using T≤Y, proves (2). The separate parameters a and η make the final epsilon loss explicit.

**Audit conclusion:** the statement of Lemma 4.21 is supported by this proof. The draft's truncated-Perron remainder is unnecessary and should not be relied on without a separate uniform estimate. The full-transform proof also removes the need for a high-frequency Dirichlet-polynomial mean-value argument.

## 3. Integer hyperbola cells have an exact integral representation

For integer m≥1 define Δ_m(u)=M(u/m)−M(u/(m+1)). All its jumps occur at integers, because m and m+1 are integers. Hence for every integer x,

\[
\Delta_m(u)=\Delta_m(x)\quad(x\le u<x+1).
\]

For integer X this gives the exact identity

\[
\sum_{X<x\le2X}|\Delta_m(x)|^2
=\int_{X+1}^{2X+1}|\Delta_m(u)|^2\,du.                     \tag{6}
\]

There is no discretization error. Apply u=(m+1)y and (2) with T=m. For m≤sqrt(X)/2, the transformed interval lies in [Y,2Y] with Y=(X+1)/(m+1), and m≤Y. Thus

\[
\sum_{X<x\le2X}|\Delta_m(x)|^2
\ll_\varepsilon X^{2+\varepsilon}/m^2.
\]

Cauchy–Schwarz gives

\[
\sum_{X<x\le2X}|\Delta_m(x)|
\ll_\varepsilon X^{3/2+\varepsilon}/m,
\]

after relabeling ε. For m>sqrt(X)/2, all cells together contain only k≤4sqrt(X), so their total contribution to V(x) is O(sqrt X) for each x. Summing m proves, under RH,

\[
\sum_{X<x\le2X}V(x)\ll_\varepsilon X^{3/2+\varepsilon}.     \tag{7}
\]

The logarithm from summing 1/m is absorbed by choosing a smaller initial epsilon. Formula (1) and the RH prime-number error estimate now prove the forward direction of Theorem 4.20.

## 4. The backward direction and its scope

Suppose the one-sided averaged E* bound holds for every sufficiently large real X and every ε>0. Since W≤E*, it bounds the dyadic averages of W(x)−x/2. Summing the exact identity ψ(x)=Σ_{k≥0}W(floor(x/2^k)) gives

\[
\sum_{X<x\le2X}(\psi(x)-x)\ll_\varepsilon X^{3/2+\varepsilon}.
\]

The partial endpoint blocks in this sum cost O(X) per scale: bound the actual W(y), not E*(y), using the elementary Chebyshev estimate W(y)=O(y). The binary-floor discrepancy contributes O(X log X). Both fit inside the stated bound.

Summing dyadic intervals converts this to the one-sided bound

\[
\Psi(U):=\int_1^U(\psi(u)-u)\,du
\le C_\varepsilon U^{3/2+\varepsilon}.
\]

For Re s>2 its Mellin transform is

\[
\int_1^\infty\Psi(U)U^{-s-1}\,dU
=\frac1s\left[-\frac{\zeta'(s-1)}{(s-1)\zeta(s-1)}
              -\frac1{s-2}\right].                        \tag{8}
\]

The apparent pole at s=2 cancels; every nontrivial zero ρ supplies a pole at ρ+1 with nonzero residue. Applying Landau's theorem to the nonnegative function C_ε U^(3/2+ε)−Ψ(U) excludes poles with real part greater than 3/2+ε, since there is no real singularity in that range. Taking all ε>0 proves RH.

Therefore the averaged equivalence is supported, with the repairs above and the precise definition of E*. No novelty claim is made here. It is an RH equivalence, not an unconditional derivation of the height estimate.

## 5. What this gives for uniform height

Under RH, (7) and Markov's inequality show that for any fixed δ>0, all but O_δ(X^(1−δ/2)) integers x in (X,2X] satisfy

\[
E^*(x)\le x/2+O_\delta(X^{1/2+\delta}).                     \tag{9}
\]

To obtain this count, use (7) with a sufficiently small epsilon, absorb the logarithmic penalty in (1), and use the uniform RH estimate for W. This is an almost-all statement; it leaves an exceptional set and does not prove a bound at every x.

For comparison, a pointwise bound M(u)=O(u^θ), 0<θ<1, yields

\[
V(x)\ll x^{1/(2-\theta)}.
\tag{10}
\]

Proof: for m≤L, sum the bound O((x/m)^θ), obtaining O(x^θ L^(1−θ)); for m>L, use disjointness of the cells to bound the sum of their lengths in integers by O(x/L). Balance at L=x^((1−θ)/(2−θ)). Taking θ just above 1/2 recovers the conditional pointwise exponent 2/3. Averaging avoids this absolute-value loss but does not automatically improve (10) at exceptional x.

There is also a simple unconditional uniform coefficient construction. Take c_1=1, c_(2^j)=−1 for 1≤j≤r, all other coefficients zero, with 2^(r+1)>x/2. Its floor function is

\[
\lfloor y\rfloor-2\lfloor y/2\rfloor+\lfloor y/2^{r+1}\rfloor,
\]

which is nonnegative and equals 1 at y=1. Its exact height is log(x!)−2log(floor(x/2)!), and its Stirling-envelope cost is therefore

\[
E^*(x)\le x\log2+O((\log x)^2).                            \tag{11}
\]

The envelope differs from the exact height by at most twice the sum of the b(x/k) terms, which is O(log²x). This recovers a classical Chebyshev-scale bound inside the same coefficient family. Its linear excess (log2−1/2)x remains much larger than the requested square-root error.

## 6. Research decision

The averaged polytope is a legitimate shared target for the two strategies. Its advantage is that the reverse implication needs only an averaged upper bound, while the forward analysis identifies the precise cancellation paid for by the absolute-value Stirling penalty.

An unconditional proof should seek a feasible coefficient family with a directly bounded envelope cost, or a bound on the dual polytope. Reusing (3) would assume RH at the crucial step. The full Möbius construction remains valuable for comparison and conditional estimates, but its cell variation has not been bounded unconditionally at square-root scale here.

The uniform-height task remains active as a mathematical objective. This pass establishes the overlap with Claude's averaged route, repairs its analytic proof, and identifies the exceptional-set gap between average and uniform control. It does not establish RH or the requested unconditional uniform height bound.
