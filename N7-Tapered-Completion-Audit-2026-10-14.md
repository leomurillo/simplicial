# Audit of the proposed tapered Möbius completion

14 October 2026. The proposed completion remains a possible ansatz, but its stated proof does not establish a feasible sequence or RH. The issues below distinguish false implications from estimates that merely remain unproved.

## 1. The zero obstruction has the opposite direction

The proved inequality is δ^β h^(1-β)≥β|(1-2^(-ρ))/ρ|. At a critical-line zero this gives δh≥c_ρ>0. It supplies no upper bound on δh. An upper bound requires an independent estimate. A bound h=o(N) alone does not establish a rate for δ.

If δ is of order N^(-α) and h is of order N^θ, their product has scale N^(θ-α). For the logarithmic-exponent criterion one needs a proved relationship between these rates, not separate qualitative assertions of cancellation and convergence.

## 2. The prime-support scaling is reversed, and its contribution is only a lower bound

The established result is δ≥Σ_{p not dividing L}1/[p(p+1)]. For a primorial through N this sum is asymptotic to 1/(N log N), by the ordinary PNT and partial summation. It is a lower bound on the total residual, not an upper bound. It says nothing about additional excess caused by composite-indexed intervals.

At N of order δ^(-1/2), even the omitted-prime sum has order sqrt(δ)/log(1/δ), which is larger than δ as δ→0. Likewise an O(1/N) estimate would have scale sqrt(δ), not a smaller scale than δ. One needs at least N log N of order 1/δ to accommodate this necessary condition.

## 3. A primorial cannot support the exact stated prefix

The forced coefficient a_4*=μ(4)-μ(2)=1. A squarefree primorial has no divisor 4. Thus it cannot realize the exact prefix once N≥4. Using lcm(1,...,N), or an appropriately enlarged primorial with the required powers of 2, fixes this support issue. It is not by itself an obstruction to the overall approach.

## 4. Balance repair has a measurable cost

For preliminary coefficients a, put B=Σa_d/d. A correction q supported beyond N and preserving the prefix must satisfy Σq_d/d=-B. Necessarily

\[
\sum_d|q_d|\ge(N+1)|B|.
\]

If the correction is solely at d=L, its coefficient is exactly q_L=-LB. Calling B small does not make q_L small. A coefficient correction of total variation O(1/N) would require B=O(1/N²); that bound has not been proved. Multiplying all coefficients by a scalar cannot simultaneously preserve a_1=1 and repair nonzero balance.

For the exact untapered prefix,

\[
B_N=m(N)-\tfrac12m(\lfloor N/2\rfloor),
\qquad m(u)=\sum_{n\le u}\mu(n)/n.
\]

This identity is not an O(1/N) estimate.

An exact finite diagnostic: N=4 gives a_1=1,a_2=-2,a_3=-1,a_4=1, and B=-1/12. Taking L=12 and a_12=1 balances the rule perfectly, preserves its prefix, and makes it periodic. Yet

\[
g(6)=6-2\cdot3-2+1=-1.
\]

This is not a counterexample to every possible taper. It shows that prefix correctness plus a one-coordinate balance repair does not guarantee feasibility.

## 5. Reflection and average cancellation do not prove positivity

The reflection identity g(y)+g(L-y)=h requires both g(y)≥0 and g(y)≤h on a half-period to establish 0≤g≤h on the other half. A lower bound on only the first half supplies only an upper bound on the reflected half.

Furthermore r≥0 was a hypothesis used to derive r_j≤δj(j+1) in the preceding note. That inequality cannot be invoked in reverse to prove nonnegativity for a candidate that has not been shown feasible. Exact prefix coefficients give exact local agreement; approximately correct coefficients can introduce negative values where the target equals zero.

The averaged-energy decomposition Q=D+R supplies a positive diagonal contribution to a quadratic mean. It is not a pointwise positive margin for the linear function g. No identity in the proposal establishes the asserted transfer from damping R to g(y)≥0 at every y.

[Matomäki–Radziwiłł, Multiplicative functions in short intervals](https://arxiv.org/abs/1501.04585) proves cancellation in almost all short intervals. Their [sequel](https://arxiv.org/abs/2007.04290) quantifies exceptional sets. Such results do not imply the claimed every-point sign condition. Results for all intervals also have length and quantitative hypotheses that must be checked; naming a hyperbola decomposition does not supply those estimates.

## 6. The stated zero-free-region consequence is incorrect

Classical zero-free regions give bounds of shapes such as

\[
M(x)\ll x\exp[-c(\log x)^{3/5}(\log\log x)^{-1/5}],
\]

not a fixed-power bound M(x)=O(x^θ) for some θ<1. The displayed majorant divided by x^θ tends to infinity for every fixed θ<1. See [Lee–Leong, New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function](https://arxiv.org/abs/2208.06141).

A uniform-in-N fixed-power bound for the proposed tapered prefix would imply the same kind of bound for M itself. On the range where the taper is identically 1, its sum is F(x)=M(x)-M(x/2). By choosing N sufficiently large for each x and using uniform constants, F(x)=O(x^θ). Dyadic telescoping then gives M(x)=O(x^θ) for θ>0. If the constants instead depend without control on N, this deduction fails, but so does the proposed uniform construction argument.

The family of estimates M(x)=O_ε(x^(1/2+ε)) for every ε>0 is equivalent to RH, not far weaker. A single fixed exponent between 1/2 and 1 would be weaker than RH but is not obtained from the stated classical shrinking zero-free region, nor does it on its own prove the required positivity and residual estimates.

## 7. Failure of an ansatz is not a zero-detection theorem

The proven logic is: a sequence with the required feasibility and rate implies RH. Its contrapositive is: if RH is false, no such sequence exists. It does not say that failure to construct the sequence implies RH is false, still less that failure of one taper produces an off-line zero. Moreover, an actual off-line zero would disprove RH, not prove it.

## Conclusion

The taper needs a precise definition, a specified balance correction with a proved cost bound, and an independent every-point positivity theorem coupled to the residual estimate. Those are not consequences of the cited unconditional cancellation results. The proposal identifies an ansatz worth testing, but its assertion that either outcome closes RH is logically invalid. No RH proof follows from the supplied argument.
