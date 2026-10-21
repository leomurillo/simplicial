# Attempt to construct the periodic sequence: forced prime support and Möbius prefix

12 October 2026. This is an unsuccessful attempt at the requested RH-closing sequence, with two rigorous restrictions obtained during the attempt. It does not prove that the sequence is impossible, and it does not prove RH. In particular, the sufficient criterion in the preceding note has not been turned into an existence theorem.

Use the earlier balanced, globally nonnegative floor rule

\[
g(y)=\sum_{d\mid L}a_d\lfloor y/d\rfloor,
\qquad a_1=1,\qquad\sum_d a_d/d=0.
\]

Write w=1_[1,2), r=g-w≥0, h=ess sup g, and

\[
\delta=\int_1^\infty r(y)y^{-2}\,dy.
\]

The requested construction still requires δ→0 and δh bounded by a fixed power of log(1/δ), or the weaker logarithmic-exponent condition in the previous note.

## 1. Every omitted prime costs a definite amount

Extend a_n by zero off its support. The exact jump formula is

\[
g(n)-g(n-1)=\sum_{d\mid n}a_d.
\tag{1}
\]

If a prime p does not divide L, then a_p=0, and (1) says g(p)=g(p-1)+1≥1. Since p≥2, w vanishes on [p,p+1). Therefore this interval contributes at least 1/[p(p+1)] to δ. Distinct prime intervals are disjoint, so

\[
\boxed{\delta\ge\sum_{p\nmid L}\frac1{p(p+1)}.}
\tag{2}
\]

More generally the same sum is valid over primes with a_p=0, whether or not p divides the displayed period. This argument permits rational or real coefficients; it does not assume integrality or RH.

In particular, δ<1/[p(p+1)] forces a_p≠0 and hence p|L. For every fixed η>0 and sufficiently small δ, all primes p≤(1-η)/sqrt(δ) must divide L. Thus even this individual-prime bound forces log L≥(1-o(1))/sqrt(δ), using the ordinary prime number theorem.

The three existing rules illustrate (2). Their first omitted primes are respectively 3, 5, and 11. Exact jump checks give g(p)-g(p-1)=1 and g(p)=1 in each case. The corresponding single-interval lower bounds on δ are 1/12, 1/30, and 1/132. These checks do not establish any asymptotic rate.

## 2. Summing the omitted primes gives a stronger period bound

Put B=log L. In the interval (2B,4B], the ordinary prime number theorem gives

\[
\#\{p:2B<p\le4B\}=(2+o(1))B/\log B.
\]

At most B/log(2B) of these primes can divide L, because each consumes at least log(2B) of its logarithm. Thus at least (1+o(1))B/log B are omitted. Each contributes at least 1/[4B(4B+1)] in (2). Consequently, as L→∞,

\[
\boxed{\delta\ge\frac{1/16+o(1)}{\log L\,\log\log L}.}
\tag{3}
\]

This uses only the ordinary PNT, not an RH-strength remainder; see [DLMF §25.16](https://dlmf.nist.gov/25.16). For sufficiently small δ, (3) implies, with some absolute c>0,

\[
\boxed{L\ge\exp\!\left(\frac{c}{\delta\log(1/\delta)}\right).}
\tag{4}
\]

To see the last implication, if B≥1/δ it is immediate. Otherwise log B≤log(1/δ), so δ B log B≥c implies B≥c/[δ log(1/δ)].

Therefore no family with period polynomial in 1/δ can achieve δ→0. A full-period enumeration would require at least exp(c/[δ log(1/δ)]) rows. This is a restriction on that enumeration method, not a lower bound on every possible symbolic description or proof. A huge period can have a compact representation.

In particular, an error scale δ≈1/N entails periods at least exp(cN/log N). This remains compatible with periods such as lcm(1,...,N); it does not disprove the target sequence.

## 3. Small error forces the initial coefficients toward Möbius inversion

Let r_j=g(j)-w(j), with r_0=0. Since r is nonnegative and constant on [j,j+1),

\[
0\le r_j\le\delta j(j+1).
\tag{5}
\]

If the a_d are integers and δ<1/[N(N+1)], all r_j vanish for 1≤j≤N. Inverting (1) then gives, for every n≤N,

\[
\boxed{a_n=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).}
\tag{6}
\]

Indeed the jumps of w are +1 at n=1, -1 at n=2, and zero thereafter; Dirichlet convolution with μ inverts the divisor sum in (1). Thus an integer construction cannot choose its initial segment freely once the target error is small.

For real or rational coefficients, the corresponding quantitative identity is

\[
a_n-\bigl(\mu(n)-\mathbf1_{2\mid n}\mu(n/2)\bigr)
=\sum_{d\mid n}\mu(n/d)(r_d-r_{d-1}).
\]

Equation (5) bounds this by

\[
\left|a_n-\mu(n)+\mathbf1_{2\mid n}\mu(n/2)\right|
\le2\delta\sum_{d\mid n}d^2
\le2\zeta(2)\delta n^2.
\tag{7}
\]

This is a forced local approximation to the Möbius prefix. It does not bound its eventual height or prove cancellation of its tail.

## 4. What failed, and what is still missing

The earlier finite improvements do not yield an extrapolatable construction. Their extension requires many additional prime coefficients, increasingly large periods, and initial coefficients constrained by (6) or (7). The missing task is to complete these forced prefixes while preserving global nonnegativity and the near-reciprocal error–height rate.

Neither the prime support bound nor the Möbius-prefix identity supplies that completion. Nor do they prohibit a compact arithmetic construction at exponential periods. At present this work establishes necessary conditions and a sufficient RH criterion, but not a sequence meeting that criterion. The requested RH proof has not been obtained.
