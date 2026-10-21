# Arithmetic sections, multiplicity, and the missing height estimate

11 October 2026. Continuation of the primitive-restriction target, incorporating Paper 53 §4.10 as read on disk. This companion note does not edit the peer's manuscript.

**Result.** The elementary arithmetic section space and its restriction maps can be constructed exactly. Their theta size is explicit. They do not yet provide the required quadratic pairing: the unknown prime discrepancy appears in their covolume. The calculations below also correct the raw degree normalization of the proposed multiplicity target and distinguish tropical scaling from a multiplicity advantage. No RH proof is claimed.

## 1. An actual section space with all the prescribed prime multiplicities

Let S be a finite set of primes and let k_p be nonnegative integers. Set

\[
Q=\prod_{p\in S}p^{k_p},\qquad L=Q\mathbb Z.
\]

The Chinese remainder theorem gives an exact sequence

\[
0\longrightarrow L\longrightarrow\mathbb Z
\xrightarrow{\mathrm{res}}\bigoplus_{p\in S}\mathbb Z/p^{k_p}\mathbb Z
\longrightarrow0.                                           \tag{1}
\]

Thus the space of integer sections vanishing to order at least k_p at each p, and the simultaneous restriction map, are completely explicit. In particular,

\[
\log[\mathbb Z:L]=\log Q=\sum_{p\in S}k_p\log p.              \tag{2}
\]

Endow L with the metric ||a||=|a|e^{-d}. Its Gaussian section size is

\[
h_L(d)=\log\sum_{a\in L}e^{-\pi a^2e^{-2d}}
=h_{\mathbb Z}(d-\log Q),                                   \tag{3}
\]

where h_Z(u)=log Σ_m exp(−πm²e^(−2u)). A nonzero section of norm at most one exists exactly when

\[
d\ge\log Q.                                                 \tag{4}
\]

This follows because the shortest nonzero section is ±Q. It is stronger information than the positivity of h_L: the Gaussian count is strictly positive for every finite d, even when there is no nonzero section of norm at most one.

Equations (1)–(4) construct a genuine arithmetic restriction model without assuming RH. They also show why applying a theta identity to it does not prove a sharp height estimate: the quantity log Q remains on the right side of the exact existence threshold.

### The restriction inequality is rigorous, and its full cost is sharp

In the same metric, decompose Z into its Q cosets modulo QZ. Each shifted Gaussian theta sum is at most the centered sum. Indeed, Poisson summation writes the shifted sum as a Fourier series with nonnegative coefficients; replacing each phase by 1 gives the centered sum. Therefore

\[
0\le h_{\mathbb Z}(d)-h_{Q\mathbb Z}(d)\le\log Q.             \tag{5a}
\]

More explicitly, for α>0,

\[
\sum_{m\in\mathbb Z}e^{-\pi\alpha(Qm+r)^2}
=\frac1{Q\sqrt\alpha}\sum_{k\in\mathbb Z}
 e^{-\pi k^2/(\alpha Q^2)}e^{2\pi i kr/Q}
\le\sum_{m\in\mathbb Z}e^{-\pi\alpha Q^2m^2}.
\]

The inequality follows by the triangle inequality; the left side is real and nonnegative. Summing over r=0,...,Q−1 proves the upper bound in (5a), while inclusion QZ⊂Z proves the lower bound.

For fixed Q, Poisson summation also gives h_Z(d)=d+o(1) as d→+∞. Using (3),

\[
\lim_{d\to+\infty}\bigl(h_{\mathbb Z}(d)-h_{Q\mathbb Z}(d)\bigr)
=\log Q.                                                     \tag{5b}
\]

Thus no smaller universal restriction-cost bound is available in this model over all archimedean scales. The same coset argument works for any finite-index inclusion of Euclidean lattices of the same rank, with log Q replaced by the logarithm of the index. This does not exclude smaller bounds at a specially chosen metric, but those need an additional estimate.

## 2. Multiplicity and degree must be normalized together

Suppose a nonzero integer N has v_p(N)≥M at every prime X/2<p≤2X. Unique factorization implies

\[
\log|N|\ge M\bigl(\vartheta(2X)-\vartheta(X/2)\bigr)
=(\tfrac32+o(1))MX,                                         \tag{5}
\]

using only the prime number theorem. For M of order √X, the raw logarithmic height is therefore of order at least X^(3/2). On the interval (X,2X], the corresponding leading constant is 1.

Hence the proposed condition “multiplicity of order √X and degree X+O(√X)” cannot use ordinary raw logarithmic height as degree. If degree denotes height divided by M, that must be stated; in that normalization it is a sharp prime-bound target rather than a small raw height.

Raising Chebyshev's integer to the M-th power illustrates the issue exactly:

\[
\frac1M\log\left(\binom{2X}{X}^{M}\right)
=\log\binom{2X}{X}.
\]

Multiplicity grows, but the normalized excess is unchanged. This does not exclude a different auxiliary construction with a better height-to-multiplicity ratio.

## 3. The packet-weighted version, including prime powers

Use the established packet

\[
g(v)=2e^{-|v|}-\tfrac12e^{|v|}\quad (|v|\le\log2),
\]

zero elsewhere, and

\[
P(X)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log(n/X)),
\qquad A=\tfrac43(5-3\sqrt2).
\]

The desired upper bound is P(X)≤A√X+O((log X)^m). In the unnormalized weighted Chebyshev scale, write

\[
B(X)=\sqrt X P(X)=\sum_p w_X(p)\log p,
\quad
w_X(p)=\sum_{k\ge1}\sqrt{X/p^k}\,g(\log(p^k/X)).               \tag{6}
\]

The weights are nonnegative and vanish for p>2X. The equivalent bound is

\[
B(X)\le AX+O(\sqrt X(\log X)^m).                             \tag{7}
\]

This separates two normalizations that the phrase “smoothed prime count” can otherwise obscure.

Choose M=⌈√X⌉, k_p=⌈M w_X(p)⌉ and Q_X=∏p p^{k_p}. The exact rounding bounds are

\[
MB(X)\le\log Q_X\le MB(X)+\vartheta(2X).                     \tag{8}
\]

Since θ(2X)=O(X), division by M leaves only O(√X) rounding error. In particular, for m≥0 the following assertions are equivalent, with possibly different constants:

* the upper discrepancy estimate (7);
* for every sufficiently large X there is a nonzero integer N_X such that
  \[
  v_p(N_X)\ge\lceil M w_X(p)\rceil\quad\hbox{for every prime }p,
  \]
  \[
  \log|N_X|\le MAX+O(M\sqrt X(\log X)^m).                    \tag{9}
  \]

**Proof.** Divisibility implies |N_X|≥Q_X, so (9) and the lower inequality in (8) imply (7). Conversely, if (7) holds, take N_X=Q_X and use the upper inequality in (8), absorbing O(X) into the allowed error. ∎

This is a precise auxiliary-integer formulation, not an independent proof. The congruence lattice in §1 becomes Q_X Z; its shortest-vector threshold is exactly log Q_X. Invoking an existence theorem whose hypothesis already requires this threshold would be circular.

The formulation does leave room for a useful construction: an explicit family of integers with the required valuations and an independently proved height bound (9). It identifies the needed gain as an efficient height-to-multiplicity ratio, not multiplicity alone.

## 4. What theta Riemann–Roch supplies, and what it forgets

For the arithmetic curve over Q, Poisson summation proves

\[
h_{\mathbb Z}(u)-h_{\mathbb Z}(-u)=u.
\]

The established framework is [van der Geer–Schoof, Proposition 1 and Example 1](https://www.mat.uniroma2.it/~schoof/arakelov.pdf). In that framework the degree map Pic(Q)→R is an isomorphism. Thus degree-zero line bundles on this arithmetic curve all have the same class. The theta size is sensitive to degree but cannot distinguish a family of nontrivial primitive packet classes at degree zero.

For our explicit lattice, the degree parameter is u=d−log Q. The quadratic coefficient sought in the previous note cannot emerge simply by replacing this u by a linear degree parameter n·deg D. Along a degree-zero ray that parameter is constant. Inserting an n² coefficient involving K(t) into d or log Q would require an independent construction and proof of that coefficient.

A useful check against the zero-section argument is (4): h_L≥0 does not guarantee a usable nonzero auxiliary section. A construction must establish nonvanishing and the norm/height bound together.

The curve-level functional equation remains a valid ingredient. It does not identify the mixed packet intersection term D_t²=2(K(t)−q).

## 5. Test of the proposed characteristic-one amplification

On the min-plus semifield, multiplication by λ>0 preserves both minimum and addition:

\[
\lambda\min(x,y)=\min(\lambda x,\lambda y),\qquad
\lambda(x+y)=\lambda x+\lambda y.
\]

This gives an automorphism of the coefficient semifield. To test its multiplicity effect, take a piecewise-linear function F on a tropical curve, with divisor coefficients given by signed sums of outgoing slopes. Whenever scaling is permitted in the chosen slope system,

\[
\operatorname{div}(\lambda F)=\lambda\operatorname{div}(F).
\]

Positive and negative parts therefore scale equally:

\[
\deg\operatorname{div}_{\infty}(\lambda F)
=\lambda\deg\operatorname{div}_{\infty}(F),
\qquad
\operatorname{ord}_x(\lambda F)=\lambda\operatorname{ord}_x(F).
\tag{10}
\]

The pole-degree-to-multiplicity ratio is unchanged. Moreover, an arbitrary real scaling does not preserve an integral-slope sheaf simply as a fixed sheaf of functions; the relevant geometric action must be specified.

This calculation addresses scalar scaling of piecewise-linear functions, not every Frobenius correspondence on the scaling site. [Connes–Consani's scaling-site paper](https://arxiv.org/abs/1603.03191) constructs a topos with an integral-slope structure sheaf and proves real-dimensional Riemann–Roch on prime periodic orbits. Their [complex-lift paper](https://arxiv.org/abs/1805.10501) also constructs lifted Frobenius correspondences. Those constructions warrant investigating the actual correspondence action rather than identifying it with scalar amplification alone.

In a Stepanov-style construction, the additional requirement is a family of nonzero auxiliary sections in which high-order vanishing can be enforced with sufficiently few independent conditions and controlled pole degree or height. Scalar scaling (10) supplies no such saving by itself. In characteristic p, derivative annihilation of p-th powers is relevant to that condition count; the min-plus automorphism identity alone is not a corresponding condition-count theorem.

## 6. Consequence for the primitive restriction construction

The simultaneous restriction map exists in the elementary model, but its index is exactly the weighted prime cost. The Gaussian curve model packages that cost into one degree parameter and does not retain the primitive mixed pairing. Scalar tropical amplification preserves the cost-to-multiplicity ratio.

The next substantive input must therefore be an independently controlled family of auxiliary sections or correspondences that retains the mixed packet information and proves either:

* the height saving (9), with nonzero sections and all valuations verified; or
* the primitive quadratic lower estimate together with the subquadratic restriction counts in the preceding note.

For the first option, a useful next construction would specify its parameter space, its vanishing-condition map, an upper bound on the rank/index of those conditions, and a nonzero section's height. For the second, it must specify the actual restriction maps and the arithmetic source of their quadratic index. The calculations here establish neither global bound, but prevent the unknown prime estimate from being concealed inside the definition of degree or inside a lattice-existence hypothesis.
