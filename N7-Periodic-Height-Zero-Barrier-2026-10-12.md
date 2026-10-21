# Actual step height, Mellin zeros, and a weaker sufficient target

12 October 2026. This continues the signed periodic construction. It proves a restriction imposed by every zeta zero, and a sufficient RH criterion using actual step height rather than the coefficient norm. It does not construct the required family or prove RH. The method belongs to the classical Mellin/floor-function approximation approach; no novelty claim is made.

## 1. Reflection identifies the true height

Use the preceding note's finite real coefficients a_d, supported on divisors of L, with a_1=1, sum a_d/d=0, and

\[
g(y)=\sum_{d\mid L}a_d\lfloor y/d\rfloor\ge0\quad(y\ge0).
\]

Put

\[
h=-\sum_d a_d,\qquad
\delta=-\sum_d a_d\log(d)/d-\tfrac12.
\]

Here h is the step-function height, not the pooled logarithmic height H_X, and not S=Σ|a_d|. For noninteger y in (0,L), the floor reflection identity gives

\[
g(y)+g(L-y)=h.
\tag{1}
\]

Consequently 0≤g≤h almost everywhere, and h≥1 since g=1 on [1,2). The value h is attained just below L because g=0 just above 0. Thus h is precisely the essential supremum. In integer coordinates the exact check is g(j)+g(L-1-j)=h, 0≤j<L.

Let w(y)=1_[1,2)(y) and r(y)=g(y)-w(y). Then

\[
0\le r(y)\le h,\qquad
\delta=\int_1^\infty r(y)y^{-2}\,dy>0.
\tag{2}
\]

The equality was proved in the preceding note. Strict positivity follows from periodic repetition of the initial unit interval.

## 2. The residual has a prescribed Mellin value at every zero

Define A(s)=Σ_d a_d d^{-s}. For Re(s)>1, summing the floor integrals gives

\[
\int_1^\infty g(y)y^{-s-1}\,dy=\frac{\zeta(s)A(s)}s.
\tag{3}
\]

Because g is bounded, the left side is holomorphic on Re(s)>0. On the right, A(1)=0 cancels the pole of ζ at 1, so analytic continuation proves (3) throughout that half-plane. For any nontrivial zero ρ=β+iγ, 0<β<1,

\[
\boxed{\int_1^\infty r(y)y^{-\rho-1}\,dy
=-\frac{1-2^{-\rho}}\rho.}
\tag{4}
\]

The right side is nonzero: |2^{-ρ}|=2^{-β}<1. Thus the excess cannot disappear in every Mellin direction, even though its mass at exponent 1 may become small.

This is the same general zero obstruction that underlies Nyman–Beurling approximation. For the established framework, see [Balazard–Saias, The Nyman–Beurling Equivalent Form for the Riemann Hypothesis](https://www.esi.ac.at/preprints/esi623.pdf). Our nonnegative residual and bounded-height estimate below are proved directly; we do not identify this restricted periodic family with the full classical criterion.

## 3. An explicit error–height inequality

For any 0<β<1, substitute t=1/y and set f(t)=r(1/t). Then 0≤f≤h and ∫_0^1 f(t)dt=δ. Since t^(β-1) is decreasing, its integral against f is maximized by placing all available mass adjacent to 0:

\[
\int_1^\infty r(y)y^{-\beta-1}\,dy
=\int_0^1 f(t)t^{\beta-1}dt
\le h\int_0^{\delta/h}t^{\beta-1}dt
=\frac{h^{1-\beta}\delta^\beta}{\beta}.
\tag{5}
\]

For completeness, the rearrangement follows by comparing f with h·1_[0,δ/h]. Their total masses agree; the difference is nonpositive below δ/h and nonnegative above it, so multiplication by a decreasing weight makes its integral nonpositive. Also δ/h≤1, as required.

Taking absolute values in (4) and applying (5) yields the unconditional theorem

\[
\boxed{\delta^\beta h^{1-\beta}
\ge \beta\left|\frac{1-2^{-\rho}}\rho\right|.}
\tag{6}
\]

In particular, every known critical-line zero gives

\[
\boxed{\delta h\ge
\frac14\left|\frac{1-2^{-\rho}}\rho\right|^2>0.}
\tag{7}
\]

At the first critical-line zero, the exact right side is approximately 0.00352071462924284342548. This decimal is a numerical evaluation, not an interval certificate; the inequality with its exact symbolic constant is the theorem. A uniformly bounded h cannot accompany δ→0, regardless of how large the periods become.

## 4. A weaker sufficient construction target

Suppose a sequence of feasible periodic rules has

\[
\delta_j\longrightarrow0,\qquad
\limsup_{j\to\infty}
\frac{\log h_j}{\log(1/\delta_j)}\le1.
\tag{8}
\]

Then RH follows. Indeed, if a zero had β>1/2, choose ε>0 small enough that 2β-1-ε(1-β)>0. Condition (8) gives eventually h_j≤δ_j^(-1-ε). Therefore

\[
\delta_j^\beta h_j^{1-\beta}
\le\delta_j^{2\beta-1-\varepsilon(1-\beta)}\longrightarrow0,
\]

contradicting (6). Functional-equation symmetry then excludes zeros left of the critical line as well.

A concrete sufficient form of (8) is

\[
\delta_j\to0,\qquad
\delta_j h_j\ll(\log(1/\delta_j))^m
\tag{9}
\]

for some fixed m≥0. Unlike the earlier Stirling-based target, this direct zero-exclusion argument does not require a bound on Σ|a_d|. Large coefficient cancellation is allowed, provided actual step height remains controlled. It also needs only a sequence of successful approximants, without assigning one to every X.

This is a sufficient criterion for RH, not a proof that such a sequence exists, and not an asserted equivalence for this restricted family. The earlier coefficient-norm bound remains sufficient for the explicit pooled-height estimate; it is simply unnecessary for the separate implication (8) ⇒ RH.

## 5. What the existing certificates actually show

| Period | Actual height h | Weighted error δ | δh |
|---:|---:|---:|---:|
| 2 | 1 | 0.193147180560 | 0.193147180560 |
| 12 | 1 | 0.121226662447 | 0.121226662447 |
| 2520 | 7 | 0.065549150526 | 0.458844053684 |

The last rule reduces δ but increases the error–height product. These three points neither establish nor refute (8). In particular, decreasing the leading constant alone is not evidence that a sequence reaches the necessary efficiency.

The companion script `empirical/connes_route/check_periodic_height_barrier.py` checks reflection exactly for all three rules and compares the period-12 Mellin transform, calculated independently through Hurwitz-zeta interval sums, with (3) at four complex arguments. At 60 decimal digits the discrepancies were below 1.5×10^-61. These are numerical diagnostics, not substitutes for the analytic proofs above.

## 6. Status and decision

The previous construction has not reached the RH height bound. This calculation replaces a coefficient-norm requirement by a weaker actual-height requirement for a direct RH implication. It also prevents treating bounded-height refinements as a possible route to δ→0.

The remaining constructive statement is: produce globally feasible signed floor rules with δ→0 and log h/log(1/δ) asymptotically at most 1. Neither floor feasibility, balance, finite optimization, nor the Mellin identity proves that statement. Establishing it requires an additional arithmetic approximation argument. RH remains unproved in this work.
