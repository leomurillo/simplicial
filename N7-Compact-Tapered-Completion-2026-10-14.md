# Compact tapered completions: an exact small model and a global family

14 October 2026. This pass constructs and analyzes concrete completions rather than assuming tapering preserves positivity. It recovers an optimized small feasible model and proves a compact global family feasible. The global family's exact cost diverges, so it does not establish the sequence needed for RH. No RH proof is claimed.

## 1. A small tapered completion solved exactly

Preserve the forced prefix through 4 and use period 12:

\[
a_1=1,\quad a_2=-2,\quad a_3=-1,\quad a_4=1,
\quad a_6=2t,\quad a_{12}=1-4t.
\tag{1}
\]

The coefficient at 6 is the forced value 2 multiplied by a taper t. The terminal coefficient is the exact balance correction: Σa_d/d=0. On one period the step values are

\[
(0,1,0,0,0,1,2t-1,2t,2t,2t,2t-1,2t).
\]

Consequently global nonnegativity holds exactly when t≥1/2, the actual height is h=2t, and

\[
C=-\sum_d a_d\log(d)/d
=\frac{1+t}{3}\log2+\frac14\log3.
\tag{2}
\]

Both height and cost are minimized at t=1/2. This recovers the previous period-12 rule, with h=1 and δ=C-1/2=0.121226662447.... It is a genuine tapered completion, but a single finite model rather than an asymptotic sequence.

There is a relevant distinction: a globally monotone multiplicative taper of a_d* would write a_12=-u with 0≤u≤t≤1. Balance demands u=4t-1, while positivity demands t≥1/2. Then u≥1>t unless t=1, where u=3 is inadmissible. Equivalently u≤t gives t≤1/3, a contradiction. Thus even this small feasible example needs a terminal correction outside that monotone taper rule.

## 2. Direct linear coefficient tapers fail before their correction region

For the literal taper a_d=a_d* for d≤N and a_d=a_d*(M-d)/(M-N) for N<d≤M, exact rational calculations give:

| N | M | Witness y | g(y) |
|---:|---:|---:|---:|
| 4 | 6 | 6 | -3/2 |
| 6 | 10 | 10 | -7/4 |
| 6 | 12 | 10 | -7/6 |
| 8 | 12 | 10 | -1 |

Coefficients at indices d>M cannot alter these values. Hence a completion confined beyond M cannot repair these particular tapered prefixes. This excludes these instances, not all smooth tapers.

## 3. A compact multiplicative taper with automatic positivity

Let P be a squarefree product of primes containing 2, and choose rational weights 0≤λ_p≤1. Define

\[
c_d=\mu(d)\prod_{p\mid d}\lambda_p\quad(d\mid P),
\qquad
E=\prod_{p\mid P}(1-\lambda_p/p),\quad L=2P,
\quad h=PE.
\tag{3}
\]

Extend c by zero outside the divisors of P. A window-adjusted, balanced coefficient rule is

\[
\boxed{a_d=c_d-\mathbf1_{2\mid d}c_{d/2}
-h\mathbf1_{d=2P}.}
\tag{4}
\]

The coefficients are supported on divisors of 2P. This period includes the necessary extra power of 2. Formula (4) has a compact product description, though expanding all divisors still requires exponentially many entries in the number of primes.

To prove positivity, let

\[
b(n)=\sum_{d\mid n}c_d
=\prod_{p\mid\gcd(n,P)}(1-\lambda_p)\ge0,
\qquad W(y)=\sum_{y/2<n\le y}b(n).
\]

Divisor summation gives

\[
W(y)=\sum_{d\mid P}c_d
 (\lfloor y/d\rfloor-\lfloor y/(2d)\rfloor).
\]

Its drift is exactly W(y+2P)=W(y)+PE. Hence

\[
\boxed{g(y)=W(y)-h\lfloor y/(2P)\rfloor}
\tag{5}
\]

is periodic of period 2P, equals the nonnegative W(y) on the whole first period, and is therefore globally nonnegative. Also a_1=1 and Σa_d/d=E/2-h/(2P)=0. The reflection identity gives 0≤g≤h and identifies h as its actual essential supremum. Consequently the original pooled constraints hold at every block scale.

When P contains every prime through N and λ_p=1 for those primes, (4) agrees with the forced coefficients a_d* for d≤N, provided 2P>N. Thus this construction really does complete arbitrary long exact prefixes; feasibility is not the missing step for this family.

## 4. The exact cost identifies its failure

Put

\[
E(s)=\prod_{p\mid P}(1-\lambda_p p^{-s}),
\qquad
A(s)=(1-2^{-s})E(s)-h(2P)^{-s}.
\]

Since C=-Σa_d log(d)/d=A'(1), differentiation gives

\[
\boxed{C=\frac E2\left[
\log(4P)+\sum_{p\mid P}\frac{\lambda_p\log p}{p-\lambda_p}
\right],\qquad\delta=C-\tfrac12.}
\tag{6}
\]

This includes the cost of the terminal balancing term. Omitting that term would remove the main cost of the construction.

For fixed P, differentiating (6) with respect to a single λ_p yields

\[
\frac{\partial C}{\partial\lambda_p}
=-\frac{E}{2(p-\lambda_p)}
\left[\log(4P/p)+
\sum_{q\mid P,\ q\ne p}\frac{\lambda_q\log q}{q-\lambda_q}\right]<0.
\tag{7}
\]

Also ∂h/∂λ_p=-h/(p-λ_p)<0. Thus reducing any prime weight increases both cost and height. The untapered choice λ_p=1 minimizes them simultaneously over this entire multiplicative-taper family. This is a theorem, not an inference from numerical samples.

For P=∏_{p≤N}p and all λ_p=1, the ordinary PNT and Mertens product formula give log P~N, E~e^(-γ)/log N, and Σ_{p≤N}log p/(p-1)=O(log N). Therefore

\[
\boxed{C\sim\frac{e^{-\gamma}N}{2\log N}\longrightarrow\infty.}
\tag{8}
\]

In particular δ does not tend to zero. No choice of weights in [0,1] rescues this family, by (7). The facts used here are classical; see [Mertens' prime product formula, dissected](https://arxiv.org/abs/2002.03361) and [DLMF §25.16](https://dlmf.nist.gov/25.16).

## 5. Exact certificates and numerical diagnostics

`empirical/connes_route/compact_euler_completion.py` constructs both full prime weights and weights halved above 3, for prime cutoffs 2,3,5,7,11,13. It clears denominators and verifies exact balance, all values across each full period, and reflection. It also checks (6) numerically at 60 decimal digits against the coefficient definition. All twelve certificates passed. Decimals are diagnostics, not interval bounds.

For full weights:

| Prime cutoff | Period | Actual height | δ, approximately |
|---:|---:|---:|---:|
| 2 | 4 | 1 | 0.193147 |
| 3 | 12 | 2 | 0.236751 |
| 5 | 60 | 8 | 0.357641 |
| 7 | 420 | 48 | 0.494575 |
| 11 | 4620 | 480 | 0.678204 |
| 13 | 60060 | 5760 | 0.854062 |

The period-12 row here is different from the optimized period-12 completion in §1: this family retains the full coefficient a_6*=2 and uses a larger terminal correction.

## 6. Consequence for the next construction

There is now an explicit compact family with global feasibility, exact prefix matching, and a computable height; its cost proves it unsuitable for the RH criterion. The failure is not an unidentified sign problem: the residue-count construction accumulates positive mass throughout a very long period, and its terminal balance correction retains that cost in (6).

The small model shows a way outside this family: alter intermediate coefficients and balance them before that mass accumulates. Extending that mechanism requires a signed, distributed correction with a global nonnegativity proof. No such growing family with δ→0 and δh of logarithmic size is established here. This pass narrows the ansatz; it does not close RH.
