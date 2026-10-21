# Arithmetic barrier attempt: what positivity does and does not supply

10 October 2026. Continuation of `N7-Divergence-Ledger-2026-10-10.md`.

**Outcome:** No one-sided polylogarithmic bound is established. This pass proves the prime-power correction is bounded and asymptotically explicit, identifies exactly how the ordinary prime-counting error enters the observable, and tests a positive convolution route. An explicit comparison measure shows why positivity, discreteness, and a power-saving counting estimate cannot alone close the argument. These are limitations of the specified approaches, not a proof that other approaches cannot work.

## 1. The higher prime powers can be controlled unconditionally

Keep a=log 2,

\[
g(v)=2e^{-|v|}-\tfrac12e^{|v|}\quad(|v|\le a),
\qquad g(v)=0\quad(|v|>a),
\]

and G(s)=(5−4cosh(as))/(1−s²), with removable values at ±1. Set A=G(1/2)=4(5−3sqrt2)/3. Split

\[
P(X)=\sum_{k\ge1}P_k(X),\qquad
P_k(X)=\sum_{X/2\le p^k\le2X}\frac{\log p}{p^{k/2}}
g(\log(p^k/X)).
\]

**Proposition.** As X tends to infinity,

\[
P_2(X)=\frac12+o(1),\qquad
\sum_{k\ge3}P_k(X)=O(X^{-1/6}).
\tag{1}
\]

In particular, the full prime-power contribution beyond primes is bounded.

**Proof for squares.** Write y=sqrt X and

\[
h(u)=u^{-1}g(2\log u),\qquad
P_2(X)=\frac1y\int h(t/y)\,d\theta(t),
\]

where theta(t)=sum_{p≤t} log p and h is supported on [1/sqrt2,sqrt2]. The prime number theorem theta(t)=t+o(t), Stieltjes integration by parts, and bounded variation of h give

\[
P_2(X)=\int h(u)\,du+o(1)
=\frac12\int_{-a}^a g(v)\,dv+o(1)
=\frac12G(0)+o(1)=\frac12+o(1).
\]

The error is uniform over this fixed compact scaling interval. This uses only the ordinary prime number theorem, not an RH-strength remainder. The [NIST DLMF account of prime distribution](https://dlmf.nist.gov/25.16) distinguishes the ordinary PNT from its RH-strength error estimate.

**Proof for higher powers.** Since 0≤g≤3/2 and theta(y)≤Cy, with C absolute,

\[
0\le P_k(X)\le C X^{-1/2}(2X)^{1/k}.
\]

The k=3 term is O(X^{-1/6}). Only k≤log_2(2X) can occur. Summing k≥4 therefore gives O(X^{-1/4}log X)=O(X^{-1/6}). This proves (1).

It follows that

\[
E(X):=P(X)-A\sqrt X
=P_1(X)-A\sqrt X+\frac12+o(1).
\tag{2}
\]

Thus either one-sided polynomial-in-log bound for E is equivalent to the corresponding bound for the corrected prime-only discrepancy P1−A sqrt X+1/2. The correction has now been proved harmless. The prime-only bound remains unproved.

## 2. Exact passage to the prime-counting error

Define

\[
w(u)=u^{-1/2}g(\log u)
=\begin{cases}
2\sqrt u-\tfrac12u^{-3/2},&1/2\le u\le1,\\
2u^{-3/2}-\tfrac12\sqrt u,&1\le u\le2,\\
0,&\text{otherwise}.
\end{cases}
\]

Then ∫w(u)du=A and, with Rtheta(x)=theta(x)−x,

\[
P_1(X)-A\sqrt X
=-X^{-1/2}\int_{1/2}^{2}R_\theta(Xu)w'(u)\,du.
\tag{3}
\]

This is Stieltjes integration by parts; w is continuous, piecewise differentiable, and zero at the endpoints. Its derivative is positive on (1/2,1) and negative on (1,2). Consequently, a bound on only one side of Rtheta does not directly yield the desired one-sided bound in (3): its multiplier changes sign.

A uniform estimate |Rtheta(x)|≤C x^b(log x)^m implies only

\[
|P_1(X)-A\sqrt X|\le C'X^{b-1/2}(\log X)^m.
\tag{4}
\]

This calculation explains exactly why a fixed strip estimate, used through its ordinary counting-error consequence, retains a positive power of X. The smoothing does not automatically lower that exponent.

## 3. A positive comparison measure that defeats the coarse argument

This section is a counterexample to a set of proposed analytic assumptions, **not** a counterexample involving the actual primes, their Euler product, or RH.

Choose 0<delta<1/2, beta=1/2+delta, H>0, and

\[
\varepsilon=\frac1{4|\beta+iH|},\qquad
r(x)=1+\varepsilon\Re\big((\beta+iH)x^{\beta+iH-1}\big)
\quad(x\ge1).
\]

Because beta<1,

\[
\frac34\le r(x)\le\frac54.
\tag{5}
\]

Hence dnu(x)=r(x)dx is a positive measure with increasing counting function

\[
\nu([1,x])=x-1+\varepsilon\big(x^\beta\cos(H\log x)-1\big)
=x+O(x^\beta).
\tag{6}
\]

It has a PNT-like main term with a power-saving remainder. Nevertheless its smoothed discrepancy, for X≥2, is exactly

\[
\begin{aligned}
E_\nu(X)
&=\int x^{-1/2}g(\log(x/X))\,d\nu(x)-A\sqrt X\\
&=\varepsilon\Re\left((\beta+iH)G(\delta+iH)X^{\delta+iH}\right).
\end{aligned}
\tag{7}
\]

The substitution x=Xe^v proves (7). G is even and nonzero at delta+iH. The amplitude is therefore nonzero. At alternating sequences of phases, E_nu equals positive and negative constants times X^delta. It violates both one-sided polylogarithmic bounds.

For example, delta=1/4 gives a counting remainder O(x^{3/4}), stronger than an O(x^{7/8}) remainder, yet discrepancy of order X^{1/4}. This comparison concerns counting-error bounds; it does not claim the measure satisfies the actual zeta zero-free theorem or zeta functional equation.

Discreteness does not repair this example. Set b_n=∫_n^{n+1}r(x)dx and replace dnu by sum_{n≥1}b_n delta_n. The counting function changes by O(1). The smoothing changes by O(X^{-1/2}): its weight is X^{-1/2}w(x/X), with global Lipschitz constant O(X^{-3/2}), and only O(X) unit cells intersect its support. Thus (7) persists up to a vanishing error for a positive measure supported on integers. This discrete measure still lacks prime support and the identities that uniquely characterize Lambda.

The conclusion is narrowly defined: positivity, monotonicity, integer support, and a power-saving counting estimate alone do not imply the missing barrier. Any valid proof must use stronger assumptions; here the unused arithmetic information is the multiplicative structure of Lambda.

## 4. What Selberg's positive convolution identity supplies

With Dirichlet convolution denoted by *, define

\[
c(n)=\Lambda(n)\log n+(\Lambda*\Lambda)(n).
\]

The exact coefficient identity is

\[
c=\mu*(\log^2),\qquad c(n)\ge0.
\tag{8}
\]

Here log² means the arithmetic function n↦(log n)². To verify (8), in Re s>1 differentiate the absolutely convergent Dirichlet series:

\[
\sum_n\frac{c(n)}{n^s}
=\left(\frac{\zeta'}\zeta\right)'(s)
+\left(\frac{\zeta'}\zeta\right)^2(s)
=\frac{\zeta''(s)}{\zeta(s)}.
\]

Multiplication of the series for 1/zeta and zeta'' gives the right side of (8). This is the coefficient form underlying Selberg's symmetry identity; no continuation of a positive Dirichlet series to the critical strip is being assumed.

Against the nonnegative weight W_X(n)=n^{-1/2}g(log(n/X)), (8) gives

\[
\sum_n\Lambda(n)\log n\,W_X(n)
=\sum_n c(n)W_X(n)
-\sum_n(\Lambda*\Lambda)(n)W_X(n).
\tag{9}
\]

Dropping the final nonnegative sum is legitimate but loses a main term. Indeed, the ordinary PNT gives

\[
\sum_{n\le x}\Lambda(n)\log n\sim x\log x,
\qquad
\sum_{n\le x}(\Lambda*\Lambda)(n)\sim x\log x.
\]

For the second asymptotic, write the sum as sum_{d≤x}Lambda(d)psi(x/d), split at d=x/Y, apply the PNT uniformly for x/d≥Y, and use Chebyshev's bound on the remaining range; then let Y grow. Partial summation gives sum_{d≤x}Lambda(d)/d∼log x. Thus the discarded term has the same leading size as the retained Lambda-log term.

In this fixed proportional window, the smoothed c sum consequently has leading term 2A sqrt X log X. Also log n≥log X−a on the support. The direct dropped-term inequality therefore yields at best

\[
P(X)\le(2A+o(1))\sqrt X,
\tag{10}
\]

which is even weaker than the ordinary smoothed PNT. Retaining the convolution exactly preserves the cancellation problem. Equation (10) rules out this particular use of positivity, not all possible quantitative refinements of Selberg's method.

## 5. Numerical checks and stopping point of the deduction

The script `empirical/connes_route/probe_prime_power_split.py` computes the three contributions independently from a sieve through 2,000,000 and checks the comparison-measure transform by 60-digit quadrature. Its JSON file records all results. For example, at X=1,000,000:

- Prime squares contribute approximately 0.49480567.
- Powers of exponent at least three contribute approximately 0.04806650.
- E(X) is approximately −0.08381424.
- The prime-only discrepancy with the +1/2 correction is approximately −0.12668641.

The differences match (2); finite samples do not prove its asymptotic, which was established analytically above. The comparison-transform quadrature agrees to better than 1e−60 in the selected samples. No interval certificate or RH inference is claimed.

The requested endpoint would require a uniform one-sided bound for

\[
\sum_{X/2\le p\le2X}\frac{\log p}{\sqrt p}g(\log(p/X))
-A\sqrt X+\frac12.
\]

This pass has proved the remaining prime powers are harmless and rejected two insufficient mechanisms. It has not established this bound, produced an independent positivity mechanism, or proved RH. The earlier equivalence does not turn these reductions into a proof.
