# Factorial auxiliary: integrality, repair cost, and the exponent target

11 October 2026. Exact follow-up to the peer's Möbius–factorial construction in Paper 53. The source manuscript and its running computations are unchanged.

**Result.** The truncated factorial auxiliary is generally rational, not integral. Its signed error can hide negative valuations. This note supplies the minimal integral repair, an exact compressed tail identity, and a proof that improving the Möbius mean itself to a uniform exponent greater than 1/2 is impossible. These results correct the construction target; they do not prove the remaining height estimate or RH.

## 1. The exact object and a small counterexample

For integer x≥2 and 1≤K≤x, define

\[
N_K(x)=\prod_{k\le K}
\left(\frac{\lfloor x/k\rfloor!}{\lfloor x/(2k)\rfloor!}\right)^{\mu(k)}.
\]

This is a positive rational number. Negative Möbius exponents require an integrality proof before it can be called an integer auxiliary. In fact,

\[
\boxed{N_5(18)=\frac{2\cdot11\cdot13\cdot17}{3}=\frac{4862}{3}.}
\tag{1}
\]

Its 3-adic valuation is −1. Therefore “spurious zeros” must, in general, include poles. Raising this ratio to a positive integer power does not cure that issue.

This check is in the spirit of the integrality conditions studied in [Adolphson–Sperber, *On the integrality of factorial ratios and mirror maps*](https://arxiv.org/abs/1802.08348): signs of the relevant floor functions matter. Our counterexample follows directly from the displayed factorial ratio and does not rely on a classification theorem.

## 2. Prime-power contributions versus actual prime valuations

Put

\[
\nu_K(y)=\sum_{k\le K}\mu(k)\lfloor y/k\rfloor,
\qquad a_K(y)=\nu_K(y)-\nu_K(y/2).
\]

Legendre's formula gives

\[
v_p(N_K(x))=\sum_{j\ge1}a_K(x/p^j).                         \tag{2}
\]

Thus a_K(x/n) is a contribution indexed by a prime power n, not a separate valuation at n. The Möbius identity yields a_K(x/n)=1 for x/2<n≤x, and zero for x/(K+1)<n≤x/2. Contributions at smaller prime powers may have either sign.

Let

\[
t_p=\#\{j\ge1:x/2<p^j\le x\},\quad
W(x)=\prod_p p^{t_p}
=\frac{\operatorname{lcm}(1,\ldots,x)}
       {\operatorname{lcm}(1,\ldots,\lfloor x/2\rfloor)}.
\]

Then log W(x)=ψ(x)−ψ(x/2). Write

\[
s_p=v_p(N_K(x))-t_p.
\]

The peer's signed error is exactly

\[
\log N_K(x)-\log W(x)=\sum_p s_p\log p.                     \tag{3}
\]

Cancellation in (3) does not certify that N_K has all the target multiplicities as an integer.

## 3. The minimal repair and the correct nonnegative excess

Define

\[
C_K(x)=\prod_p p^{\max(0,-s_p)},\qquad U_K(x)=N_K(x)C_K(x).
\]

For each p,

\[
v_p(U_K)=t_p+\max(s_p,0).
\]

Hence U_K is an integer divisible by W, and C_K is the smallest positive integer multiplier achieving these target valuations. Its height is

\[
\boxed{\log U_K(x)=\psi(x)-\psi(x/2)
                  +\sum_p\max(s_p,0)\log p.}                \tag{4}
\]

This repair must account for target prime powers as well as negative total valuations. Clearing the denominator alone can fail to restore a target multiplicity lost to a negative small-prime-power contribution.

For (1), W(18)=4862 and C_5(18)=3, so U_5(18)=W(18). That particular repair is exact. The general issue is proving a height bound for the repaired object without first knowing the desired prime estimate.

The useful sufficient target is

\[
\log N_K(x)+\sum_p\max(0,-s_p)\log p
\le x/2+O(\sqrt x\log^m x),                                \tag{5}
\]

at an explicitly specified choice of K. Formula (4) would then give the one-sided dyadic prime-power bound. A fit to the signed quantity (3) alone does not establish (5).

## 4. Exact compression of the omitted terms

Let M(u)=Σ_{k≤u}μ(k) and F(j)=log(j!)−log(⌊j/2⌋!). Since
⌊x/(2k)⌋=⌊⌊x/k⌋/2⌋, grouping by j=⌊x/k⌋ gives

\[
\log W(x)-\log N_K(x)
=\sum_{1\le j\le\lfloor x/(K+1)\rfloor}
F(j)\left[M(\lfloor x/j\rfloor)
-M\!\left(\max\{K,\lfloor x/(j+1)\rfloor\}\right)\right].    \tag{6}
\]

At K≈√x, this has O(√x) blocks. It is an exact computational compression, but the coefficients still require Mertens values up to x. It supplies no cancellation estimate for those coefficients. The j=1 block vanishes because F(1)=0.

At full complexity K=x, N_x=W exactly. The full object is the lcm quotient above; its existence does not bound its logarithm more sharply than the prime count it encodes.

## 5. The proposed leading-error approximation has an uncontrolled remainder

Write

\[
m_K=\sum_{k\le K}\frac{\mu(k)}k,\qquad
R_K(y)=\sum_{k\le K}\mu(k)\{y/k\}.
\]

Then, exactly,

\[
a_K(y)=\tfrac12ym_K-R_K(y)+R_K(y/2).
\]

With z=x/(K+1), the signed spurious term is therefore

\[
\operatorname{spur}(K)=
\tfrac{x}{2}m_K\sum_{n\le z}\frac{\Lambda(n)}n
-\sum_{n\le z}\Lambda(n)
 \left[R_K(x/n)-R_K(x/(2n))\right].                         \tag{7}
\]

The elementary bound on the second term is

\[
|\text{second term}|\le K\psi(z)=O(x),                     \tag{8}
\]

using |{u}−{v}|≤1 and the classical Chebyshev bound. Consequently the observed approximation by (x/2)m_K log(x/K) is not yet a controlled asymptotic in the joint x,K range of interest. Its fractional-part remainder must be bounded with its sign and correlations intact.

## 6. Improving the Möbius mean to exponent 1 is the wrong target

There is a rigorous distinction between improving an auxiliary object's total error and improving m_K itself.

**Proposition.** There is no bound

\[
m(x):=\sum_{n\le x}\frac{\mu(n)}n
=O(x^{-\alpha}(\log x)^B)
\]

for any fixed α>1/2 and finite B, valid for all sufficiently large x.

**Proof.** For Re s>1, partial summation gives

\[
\frac1{\zeta(s)}=(s-1)\int_1^\infty m(x)x^{-s}\,dx.          \tag{9}
\]

The asserted bound would make the right side holomorphic on Re s>1−α, by locally uniform absolute convergence. It would therefore continue 1/ζ holomorphically across every critical-line zero. Such zeros exist, and 1−α<1/2, a contradiction. ∎

The needed existence of critical-line zeros is classical; see [DLMF §25.10](https://dlmf.nist.gov/25.10). Finite-range fitted exponents above 1/2 do not contradict this proposition: they are not uniform asymptotic bounds.

Thus a putative improvement from x/√K to x/K cannot be obtained by proving m_K=O(1/K), even if RH is assumed. Any such improvement for the full auxiliary must use cancellation with the remainder in (7), different coefficients, or a different construction. The usual RH-equivalent square-root bounds also allow epsilon losses; finite envelope measurements do not remove those quantifiers.

## 7. Exact verification and present status

`empirical/connes_route/check_factorial_auxiliary.py` checks all integer x from 2 through 80 and all 1≤K≤x. Its 50,887 prime-valuation checks verify the grouped-tail identity, the minimal-repair identity, and the full-complexity identity. The factorial ratio at (18,5) is separately evaluated using exact rational arithmetic. The adjacent JSON records the results.

The construction now has an explicit integrality correction and an exact error decomposition. The height saving (5) is unproved. No quadratic explicit-formula intersection pairing is constructed by these factorial identities. Further work must bound the repaired height, rather than infer an integral auxiliary or an asymptotic efficiency exponent from the signed numerical fit.

