# Explicit pooled coefficients: a uniform construction and its cost barrier

12 October 2026. This note derives an explicit all-X feasible rule, proves its cost bound, and tests a broad positive-weight refinement. The rule does not attain the RH-closing height. The requested square-root remainder remains unproved.

## 1. An explicit coefficient rule

Fix an integer X≥2, let r=floor(log_2 X), and take

\[
c_1=1,\qquad c_{2^j}=-1\ (1\le j\le r),\qquad
c_k=0\ \text{otherwise}.
\tag{1}
\]

There are r+1 nonzero coefficients, all integers. For 0≤y≤X, telescoping gives

\[
\begin{aligned}
G_c(y)
&=\sum_k c_k\bigl(\lfloor y/k\rfloor-\lfloor y/(2k)\rfloor\bigr)\\
&=\lfloor y\rfloor-2\lfloor y/2\rfloor
  +\lfloor y/2^{r+1}\rfloor\\
&=\lfloor y\rfloor-2\lfloor y/2\rfloor.
\end{aligned}
\]

The last expression is 0 or 1, and equals 1 when 1≤y<2. Therefore

\[
G_c(y)\ge\mathbf1_{[1,2)}(y).
\tag{2}
\]

For every n≥2 and X<x≤2X, y=x/n≤X. Summing (2) over x proves exactly the pooled constraints from the preceding note:

\[
\sum_kc_kB_{X,k}(n)\ge w_X(n).
\]

Thus (1) gives a nonzero integral auxiliary at every X, with no optimization, prime list, or RH assumption. This is the classical dyadic factorial construction expressed in the pooled coordinates, not a new prime-distribution theorem.

## 2. Its uniform cost, with the leading constant exposed

For each x in the block, telescoping the log-factorial cost gives

\[
\sum_kc_kF(\lfloor x/k\rfloor)
=\log(x!)-2\log(\lfloor x/2\rfloor!)
 +\log(\lfloor x/2^{r+1}\rfloor!).
\]

Since 2^(r+1)>X and x≤2X, the last factorial is 0! or 1!, so its logarithm vanishes. Consequently the pooled integer is

\[
U_X=\prod_{X<x\le2X}\frac{x!}{(\lfloor x/2\rfloor!)^2}.
\tag{3}
\]

For even x this factor is a central binomial coefficient, at most 2^x. For odd x it is x times a central binomial coefficient of order x−1, at most x2^(x−1). Hence, writing A_X=X(3X+1)/4,

\[
\boxed{\log U_X\le 2\log2\,A_X+X\log(2X).}
\tag{4}
\]

This is a fully explicit uniform upper bound. Stirling's formula also gives

\[
\log U_X=2\log2\,A_X+O(X\log X).
\tag{5}
\]

Thus the excess above A_X is genuinely of order X², with positive leading coefficient (3/4)(2log2−1). A more careful estimate of this same rule cannot change it into O(X^(3/2)log^m X).

This answers the explicit-rule and uniform-feasibility part of the request. It does not answer the crucial sharp-cost part.

## 3. A parameterization of possible improvements

Extend c by zero beyond its support and define its divisor transform

\[
b(n)=\sum_{d\mid n}c_d=(1*c)(n).
\]

Then

\[
G_c(y)=\sum_{y/2<n\le y}b(n),\qquad c=\mu*b.
\tag{6}
\]

For b(1)=1, the pooled constraints become

\[
\boxed{\sum_{r\ge2}b(r)w_X(nr)\ge0
\quad\text{for every }2\le n\le2X.}
\tag{7}
\]

All sums are finite; only r≤X matters. Their cost identity is

\[
\mathcal H_X(c)=\mathcal W(X)
+\sum_{r\ge2}b(r)\sum_{n\ge2}\Lambda(n)w_X(nr),
\tag{8}
\]

where \(\mathcal W(X)=\sum_{X<x\le2X}W(x)\). Formula (7), after multiplication by Λ(n) and summation, ensures that the total excess in (8) is nonnegative even when individual b(r) are negative.

For (1), the divisor weights are particularly simple:

\[
b(n)=1-v_2(n)\quad(n\le X).
\tag{9}
\]

They are negative on integers divisible by 4. This is permitted: feasibility requires the pooled sums (7) to be nonnegative, not every b(r) separately. The full Möbius rule instead has b(1)=1 and b(r)=0 for r>1, making the cost exactly \(\mathcal W(X)\); that restates the unknown prime count rather than bounding it.

## 4. Why a nonnegative divisor-square refinement cannot close the estimate

A natural positive construction is

\[
b(n)=\left(\sum_{\substack{d\mid n\\d\le z}}\lambda_d\right)^2,
\qquad\lambda_1=1,
\]

with coefficients

\[
c_k=\sum_{\substack{a,b\le z\\[a,b]=k}}\lambda_a\lambda_b.
\tag{10}
\]

It satisfies b=1*c, b(1)=1, and b(n)≥0, hence (7). Terms c_k with k>X may be discarded because they cannot affect any relevant divisor weight.

But for every prime p>z, b(p)=1 regardless of the other parameters. Suppose z≤X/2. Keeping just r=p in (8), with X/2<p≤3X/4, and just n=2, gives

\[
\mathcal H_X(c)-\mathcal W(X)
\ge(\log2)\sum_{X/2<p\le3X/4}w_X(2p)
\ge\frac{X\log2}{2}
\bigl(\pi(3X/4)-\pi(X/2)\bigr).
\tag{11}
\]

The ordinary prime number theorem implies that the right side is

\[
\left(\frac{\log2}{8}+o(1)\right)\frac{X^2}{\log X}.
\tag{12}
\]

This uses ordinary prime distribution, not RH-strength cancellation; see [DLMF §25.16](https://dlmf.nist.gov/25.16) for the distinction between the PNT and RH-strength error estimates.

The lower bound holds uniformly over every choice of λ_d with λ_1=1. Therefore this entire positive-square family cannot have square-root-scale excess above the true window. Even assuming RH, its absolute cost cannot obey A_X+O(X^(3/2)log^m X) for any fixed m: the RH error in \(\mathcal W(X)-A_X\) is too small to cancel (12).

This is a limitation of the specified positive divisor-square representation, not of all feasible pooled coefficients. Signed b satisfying (7), including (9), are outside that restricted family.

## 5. What an RH-closing rule would still have to prove

The required estimate remains

\[
\mathcal H_X(c_X)\le A_X+C X^{3/2}(\log X)^m
\quad\text{for all sufficiently large }X.
\tag{13}
\]

A successful explicit rule must supply both (7) and a direct estimate for its factorial cost (6) in the pooled-construction note. Merely showing that the excess in (8) is small would still leave the unknown window \(\mathcal W(X)\) unless that window is bounded independently.

This pass proves feasibility and a uniform cost for the dyadic rule, but its leading constant is too large. It also eliminates the proposed positive-square refinement at local cutoff z≤X/2. The surviving task is a signed coefficient construction with controlled pooled sums and a sharp leading cost, or a different arithmetic argument for (13). No such construction is proved here, and RH is not closed.
