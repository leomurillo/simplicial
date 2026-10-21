# Integral factorial majorants and generalized arithmetic sections

11 October 2026. Two constructive follow-ups: replace truncated Möbius coefficients by coefficients that certify integrality, and test whether the 2026 arithmetic Jacobian supports the Gaussian section construction. No asymptotic height bound or RH closure is established.

## 1. A prime-independent sufficient condition for an integer auxiliary

Fix an integer x≥2 and K≥1. For rational coefficients c_1,...,c_K define

\[
A_c(y)=\sum_{k=1}^K c_k\left(\lfloor y/k\rfloor-\lfloor y/(2k)\rfloor\right).
\]

Impose the finite rational inequalities

\[
A_c(1)\ge1,\qquad A_c(j)\ge0\quad(2\le j\le\lfloor x/2\rfloor).
\tag{1}
\]

Because all breakpoints of the floor functions are integers, (1) implies

\[
A_c(y)\ge\mathbf1_{[1,2)}(y)\quad(0\le y\le x/2).
\]

Let Q clear the coefficient denominators, and define the positive rational number

\[
U=\prod_{k=1}^K
\left(\frac{\lfloor x/k\rfloor!}{\lfloor x/(2k)\rfloor!}\right)^{Qc_k}.
\]

Legendre's formula and (1) imply, for every prime p,

\[
v_p(U)=Q\sum_{r\ge1}A_c(x/p^r)
\ge Q\#\{r:x/2<p^r\le x\}.                                \tag{2}
\]

Thus U is an integer divisible by W(x)^Q, where log W(x)=ψ(x)−ψ(x/2). No prime enumeration is needed to certify (1). The normalized log-height is

\[
H_x(c)=\frac{\log U}{Q}
=\sum_{k=1}^K c_k\left[\log(\lfloor x/k\rfloor!)
                     -\log(\lfloor x/(2k)\rfloor!)\right].   \tag{3}
\]

Equations (1)–(3) give a finite linear optimization problem: minimize H_x(c) subject to (1). This is a sufficient majorant construction, not a characterization of every possible integral factorial ratio. Requiring nonnegative contributions at every possible prime-power argument is stronger than requiring only the total prime valuations to be nonnegative.

**Conditional height theorem.** If for every sufficiently large integer x one can find feasible rational c with

\[
H_x(c)\le x/2+C\sqrt x\log^m x,                              \tag{4}
\]

then ψ(x)−ψ(x/2) obeys the same upper bound. Summing dyadic windows yields ψ(x)≤x+O(√x log^m x), for fixed m≥0. For real endpoints, integer rounding changes this by at most harmless logarithmic terms.

That one-sided bound implies RH. Indeed, for σ>1,

\[
\int_1^\infty(\psi(x)-x)x^{-s-1}\,dx
=-\frac{\zeta'(s)}{s\zeta(s)}-\frac1{s-1}.
\]

Subtract ψ(x)−x from a positive upper envelope C√x(1+log x)^m. After x=e^t this is a nonnegative Laplace transform. If a zeta zero had real part >1/2, the transform would have a pole there and a convergence abscissa >1/2. Landau's theorem would force a singularity at a positive real abscissa >1/2, where the displayed meromorphic expression and the envelope transform are holomorphic. The apparent singularity at s=1 cancels. This is the same one-sided-transform argument used in the previous notes.

The condition K≈√x is a desired economy of the construction, not a logical requirement for this implication. Coefficient sizes and denominators also count toward complexity; the number K alone does not measure the full size of a certificate.

## 2. A search followed by exact feasibility certification

The script `empirical/connes_route/optimized_factorial_majorant.py` uses a numerical linear-programming solver to find candidates for K=⌈√x⌉. It then rationalizes every coefficient and verifies every inequality (1) with exact integer arithmetic after clearing denominators. A rational correction in c_1 is available if rationalization creates a violation, since floor(y)−floor(y/2)≥1 for integer y≥1. No correction was needed in the runs below.

| x | K | certified denominator Q | H_x(c), approximate | H_x(c)−x/2, approximate |
|---:|---:|---:|---:|---:|
| 1,000 | 32 | 1 | 573.188674 | 73.188674 |
| 4,000 | 64 | 1 | 2,209.385618 | 209.385618 |
| 10,000 | 100 | 1 | 5,494.473331 | 494.473331 |

All three candidates have integral coefficients, so Q=1. Their divisibility is proved by (2), not inferred from floating-point optimization. The adjacent JSON stores the coefficients for reproduction. Prime enumeration is used only afterwards to compare with the actual window count, not to choose or certify the coefficients.

The decimal heights use floating-point log-factorials; they are diagnostic values, not interval-certified height bounds. Exact optimality of the LP solutions is not claimed. The exact mathematical result is feasibility and divisibility for the stored coefficients.

These three points do not establish (4), an efficiency exponent, or a bounded envelope. They demonstrate a replacement for the nonintegral truncated Möbius object that is genuinely integral at the tested scales. The remaining problem is a uniform coefficient construction with a provable height bound.

## 3. What the new geometry supplies

The [2026 Jacobian paper](https://arxiv.org/html/2602.15941), Definitions 2.12–2.14 and §3, extends classical metrized line bundles to rank-one torsion-free groups, allowing singular strata. In particular, a prime p is represented by Z[1/p], and tensor products encode unions of localized prime sets. This is a larger monoid than the classical Arakelov Picard group of Q. Our earlier statement that the latter has trivial degree-zero part does not rule out these generalized objects.

The [absolute-geometry paper](https://arxiv.org/abs/2606.06604) describes an absolute arithmetic curve and its local perfectoid and complex realizations. The [absolute-twistor paper](https://arxiv.org/html/2609.00299), introduction and §6, retains a canonical sign through the signed base F_(1²) and gives an odd-integer Frobenius action. Therefore “there is no minus sign in characteristic one” should not be used as a blanket objection to the newer signed geometry.

The abstracts and targeted sections inspected here do not supply the particular mixed-packet intersection inequality needed in our notes. This is not an exhaustive nonexistence claim about all literature.

## 4. The Gaussian count does not extend unchanged to Z[1/p]

Consider L=Z[1/p] with any fixed norm ||a||=c|a|, c>0. Its proposed ordinary theta sum diverges:

\[
\sum_{a\in L}e^{-\pi\|a\|^2}=+\infty.
\tag{5}
\]

**Proof.** The distinct elements p^(−r), r≥1, all have norm at most c, so each contributes at least exp(−πc²)>0. ∎

This is not a failure of the generalized Jacobian construction. It is a failure of directly reusing the unregularized Gaussian section size from discrete lattices.

For a concrete exhaustion L_r=p^(−r)Z, with metric |a|e^(−d),

\[
h_{L_r}(d)=h_{\mathbb Z}(d+r\log p).
\]

Poisson summation gives h_Z(u)=u+o(1) as u→+∞. Consequently

\[
\boxed{h_{L_r}(d)-r\log p\longrightarrow d.}                \tag{6}
\]

Subtracting the leading divergence leaves only the linear degree parameter. It can be negative, so it is not automatically a nonnegative section size of the kind required in the primitive-growth argument. Alternatively, subtracting h_(L_r)(0) also gives the limit d.

Thus the simplest exhaustion and subtraction do not construct the nonnegative mixed section theory. A different regularized dimension, additional cohomological data, or an analytic index may still do so, but its finiteness, sign, and explicit-formula quadratic term must be established.

## 5. The two remaining estimates are still distinct

For the auxiliary route, the open input is the height bound (4) for a uniformly specified family of feasible coefficients. For the geometric route, it is a well-defined section/index construction retaining the packet correlations, with the quadratic lower estimate and subquadratic primitive-ray growth.

The new integer candidates remove an actual integrality defect. The generalized section calculation identifies precisely why the simplest theta extension loses the required properties. Neither calculation proves the missing asymptotic estimate. The finite Möbius envelopes and the existence of Frobenius symmetries alone do not fill that gap.
