# Divergence ledger: one-sided arithmetic barriers and translated packets

10 October 2026. A continuation of `N7-LowerBound-Attempt-2026-10-10.md`.

**Status:** The requested prime-sum bound is not proved. This search gives a rigorous one-sided reduction, a two-sided oscillation consequence if RH fails, an obstruction to strict contraction, and frequency-sensitive arithmetic diagnostics. These distinguish possible mechanisms from reformulations of RH. No novelty claim is made for the explicit-formula or Landau arguments.

## 1. Fixed notation and the exact observable

Put a=log 2 and

\[
g(v)=\begin{cases}2e^{-|v|}-\tfrac12e^{|v|},&|v|\le a,\\0,&|v|>a,\end{cases}
\qquad
G(s)=\int g(v)e^{-sv}\,dv=\frac{5-4\cosh(as)}{1-s^2}.
\]

The singularities at s=±1 are removable. G has no zeros in |Re s|<1. For z=rho−1/2, where rho ranges over all nontrivial zeta zeros with multiplicity,

\[
|G(z)|\le C(1+|\Im z|)^{-2},\qquad \sum_\rho|G(z)|<\infty.
\]

Thus the real, continuous, even function

\[
K(t)=\sum_\rho G(\rho-\tfrac12)e^{(\rho-1/2)t}
\tag{1}
\]

is unconditionally well defined, with locally uniform absolute convergence and |K(t)|≤Ce^{|t|/2}.

The explicit formula in the preceding note gives, for X>2,

\[
\begin{aligned}
P(X)&=\sum_{X/2\le n\le2X}\frac{\Lambda(n)}{\sqrt n}g(\log(n/X)),\\
A&=G(1/2)=\frac43(5-3\sqrt2),\\
D(X)&=X^{-5/2}\int_{-a}^a\frac{g(v)e^{5v/2}}{1-X^{-2}e^{2v}}\,dv,\\
K(\log X)&=A\sqrt X-P(X)-D(X).
\end{aligned}
\tag{2}
\]

D(X)>0 and D(X)=O(X^{-5/2}) for X≥3. Write E(X)=P(X)−A√X.

## 2. A one-sided bound already suffices

**Proposition.** Each of the following statements is equivalent to RH:

1. For some finite C,m≥0, E(X)≤C(1+log X)^m for all sufficiently large X.
2. For some finite C,m≥0, E(X)≥−C(1+log X)^m for all sufficiently large X.
3. E(X) is bounded.

In particular, proving a two-sided discrepancy estimate is unnecessary. But neither one-sided estimate is established here.

**Proof.** For Re s>1/2, termwise Laplace integration in (1) is justified by absolute convergence and gives

\[
F(s)=\int_0^\infty K(t)e^{-st}\,dt
=\sum_\rho\frac{G(\rho-1/2)}{s-(\rho-1/2)}.
\tag{3}
\]

The right side extends meromorphically to the whole plane. Indeed, on a compact set, the sufficiently high-zero terms are uniformly O((1+|Im rho|)^{-3}); only finitely many remaining poles need be removed. At z=rho−1/2 its residue is the multiplicity of rho times G(z), which is nonzero. There is no cancellation between distinct zero locations.

F has no singularity on the positive real axis. There are no real nontrivial zeros: on 0<s<1 the alternating eta series is positive and zeta(s)=eta(s)/(1−2^{1−s})<0; for s>1 the Euler product is nonzero. The pole of zeta at 1 is not a zero and contributes no pole to (3).

Suppose K(t)≤C(1+t)^m eventually. Choose an integer M≥m, enlarge C if needed, and choose t0 so that

\[
h(t)=C(1+t)^M-K(t)\ge0\quad(t\ge t_0).
\]

Its Laplace transform H initially converges in Re s>1/2. Equation (3) gives a meromorphic continuation

\[
H(s)=C\int_{t_0}^\infty(1+t)^M e^{-st}\,dt-F(s)
+\int_0^{t_0}K(t)e^{-st}\,dt.
\tag{4}
\]

The first term extends meromorphically with its only possible pole at 0, and the last is entire. Hence H is analytic near every positive real number.

The Landau principle for a nonnegative Laplace integrand says that its finite abscissa of convergence c must be a singularity on the real axis. For completeness: if the transform were analytic near c, take b>c sufficiently close to c that its Taylor series about b has radius greater than b−c. The coefficients in the series for H(b−u) are the nonnegative moments ∫t^n h(t)e^{-bt}dt/n!. Tonelli identifies their sum, at a positive u>b−c inside the Taylor disk, with the convergent integral ∫h(t)e^{-(b−u)t}dt. This contradicts the definition of c. The case c=−infinity needs no argument.

Since h has exponential order, its abscissa is bounded above. Equation (4) and the principle force c≤0. Therefore H is holomorphic in Re s>0. It follows from (4) that F has no pole there. The nonzero residues in (3) exclude every zero with Re rho>1/2; functional-equation symmetry proves RH.

The same argument with h(t)=C(1+t)^M+K(t) treats a lower bound for K. Formula (2) transfers either one-sided bound between E and K. Conversely, under RH the sum in (1) is bounded by Σrho|G(i Im rho)|, so E is bounded. This proves all assertions.

This is a standard positivity/analytic-continuation mechanism, not a new source of arithmetic cancellation. Closely related one-sided criteria and the nonnegative-Laplace argument appear in [Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, Theorems 1.6–1.7 and §7.2](https://arxiv.org/html/2206.03682).

### An oscillation consequence without an isolated rightmost zero

Let Θ=sup_rho(Re rho−1/2). If Θ>0, then for every 0≤α<Θ,

\[
\limsup_{X\to\infty}\frac{E(X)}{X^\alpha}=+\infty,
\qquad
\liminf_{X\to\infty}\frac{E(X)}{X^\alpha}=-\infty.
\tag{5}
\]

To prove this, repeat (4) with Ce^{αt} in place of the polynomial. Its transform has its only real pole at α. An eventual upper or lower bound of this size would force the nonnegative transform's abscissa to be ≤α and would make F holomorphic in Re s>α. This contradicts any zero with Re rho−1/2>α. Failure of every eventual bound by every finite C gives the stated infinite limsup and liminf. The negligible D term does not affect them.

Thus a failure of RH cannot hide in only one sign of this discrepancy. This does not rely on a maximal zero, a finite exceptional set, or linear independence of ordinates.

## 3. Strict contraction is the wrong target for these correlations

Under RH,

\[
K(t)=\sum_\rho b_\rho e^{i\gamma_\rho t},\qquad
b_\rho=\frac{5-4\cos(a\gamma_\rho)}{1+\gamma_\rho^2}>0,
\quad\sum b_\rho=q_0=K(0).
\]

Numerically q0=0.29984744568842157736. Absolute summability gives uniform almost periodicity. More explicitly, choose a finite set carrying all but ε of the mass. Simultaneous recurrence of its finitely many phases supplies arbitrarily large t with all phases as close to 1 as desired. The remaining contribution has magnitude ≤ε. Consequently there are t_j→infinity with K(t_j)→q0.

It follows that a bound |K(t)|≤q0−η for every sufficiently large t, with fixed η>0, is incompatible with RH. The natural conditional stability here is recurrent and marginal. A strict global dissipative margin cannot establish this particular correlation bound. This observation concerns this observable, not every conceivable spectral method.

## 4. Frequency-modulated packets: a better diagnostic, not a proof

Use f_ω(x)=e^{(1+iω)x} on [0,a], zero elsewhere. Its autocorrelation is g_ω(v)=e^{iωv}g(v), its squared norm is 3/2, and its Mellin filter is G(s−iω). The convolution K_ω=W*g_ω has the exact spectral expansion

\[
K_\omega(t)=\sum_\rho G(\rho-1/2-i\omega)e^{(\rho-1/2)t}.
\tag{6}
\]

For X>2 it can instead be computed entirely from primes:

\[
\begin{aligned}
P_\omega(X)&=\sum_{X/2\le n\le2X}\frac{\Lambda(n)}{\sqrt n}
g(\log(n/X))e^{-i\omega\log(n/X)},\\
D_\omega(X)&=X^{-5/2}\int_{-a}^a
\frac{g(v)e^{(5/2+i\omega)v}}{1-X^{-2}e^{2v}}\,dv,\\
K_\omega(\log X)&=\sqrt X\,G(1/2-i\omega)-P_\omega(X)-D_\omega(X).
\end{aligned}
\tag{7}
\]

The exact diagonal q_ω=Q(f_ω)=K_ω(0) is

\[
2\Re G(1/2-i\omega)-\frac32\left(\gamma_E+\log(4\pi)+\log\tanh(a/2)\right)
-\int_0^a\frac{e^{v/2}g(v)\cos(\omega v)-3/2}{\sinh v}\,dv.
\tag{8}
\]

There is no prime contribution at the base window, since g(log2)=0. In the two-dimensional subspace of two disjoint translated copies (t>a), the least Rayleigh quotient is

\[
\frac{q_\omega-|K_\omega(t)|}{3/2}.
\tag{9}
\]

The off-diagonal entry may be K_ω or its conjugate according to translation convention; its modulus and (9) are unchanged. Endpoint jumps are admissible by approximation in the form domain; the Fourier decay is O(1/|u|), sufficient for the logarithmic archimedean weight.

A hypothetical zero z=δ+iH is suppressed by G(δ+iH)=O(H^{-2}) in the fixed packet. Choosing ω=H instead gives G(δ), which is of order one for small δ. This improves sensitivity to a specified height. It neither guarantees domination over other terms nor asserts that such a zero exists.

The arithmetic experiment used X in {3,10,100,1000,10000,100000,1000000} and ω in {0,14,21,50,100}. All 35 tested two-packet Rayleigh quotients were positive; the smallest was approximately 0.0962951. The largest tested |K_ω|/q_ω was approximately 0.886443. These finite samples prove no universal inequality. Three independent 60-digit spot checks differed from double arithmetic by at most 1.14e−14 in K and 9.52e−16 in q. They are not interval enclosures.

Reproducible files:

- `empirical/connes_route/probe_modulated_weil_packets.py` and its JSON output.
- `empirical/connes_route/check_modulated_weil_packets.py` and its JSON output.

## 5. Other branches and the precise obstruction found

### Reusing the 7/8 argument

The inspected [OpenAI manuscript source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) has a normalized low-side estimate with exponent 3/16, labelled `eq:part-II-normalized-low`. Its final normalization is C(s)=s−11/16 and target σ0=7/8, so C(σ0)=3/16. Moving σ0 left while retaining this normalization requires improving that estimate. The continuation factor is also established in the stated region. Thus the existing result does not itself furnish an iterable contraction toward 1/2. This is an inspection of the relevant estimates, not an independent verification of the entire manuscript or a proof that its method cannot be improved.

### An exact dyadic recurrence

In distributions, g''−g=2δ_{−a}−5δ_0+2δ_a. Writing S_a for translation by a,

\[
(1-\partial_t^2)K=(5-2S_a-2S_{-a})W.
\]

The inverse shift kernel is c_j=(1/3)2^{-|j|}. It is summable on exponentially weighted spaces of rate α<1. That is an exact inversion, but it preserves the admitted exponential rate rather than improving it. Applying it to exponential modes makes the absence of a contraction explicit. Boundedness of the inverse does not establish that its input is bounded.

### Euler-product probability

For σ>1, ζ(σ+it)/ζ(σ) is the characteristic function of log n under the zeta probability distribution. Its compound-Poisson description has masses p^{-kσ}/k at k log p. For σ≤1, even the k=1 mass at large jumps diverges. A deterministic centering cannot fix the required finite Lévy mass away from zero. Hence this particular positive probabilistic representation does not continue to the needed region. This says nothing against a different representation with an independently proved positivity property.

### Mean-square control

A polynomial bound for ∫_0^T|K(t)|²dt would imply convergence of its Laplace transform in every positive half-plane by Cauchy–Schwarz, and hence RH by (3). Squaring a growing mode and then taking a square root leaves its growth exponent unchanged. Expanding the arithmetic mean square introduces prime-pair correlations; merely changing to a mean square has not supplied a bound for them.

### Infinite log-concavity is insufficient by itself

The coefficient sequence (1,1.9,1), padded by zeros, stays nonnegative under every iteration of L(a)_n=a_n²−a_{n−1}a_{n+1}. The middle entry evolves by x↦x²−1; from 1.9 it remains positive and increases. Yet 1+1.9z+z² has discriminant −0.39 and nonreal zeros. Thus infinite log-concavity alone cannot justify the required real-rootedness. Additional Xi-specific structure would need its own proof.

## 6. Where the search actually stands

The sharpest remaining arithmetic target from this pass is either one of

\[
P(X)\ge A\sqrt X-C(1+\log X)^m,
\qquad\text{or}\qquad
P(X)\le A\sqrt X+C(1+\log X)^m
\]

uniformly for all sufficiently large X. The one-sided proof identifies how such an estimate would exclude zeros; it does not derive the estimate from primes. The modulated packets provide a more sensitive test of proposed inequalities, not a reason they hold. The known strip still gives a positive power of X, and every route above retains an unproved step if used to claim a polynomial in log X.

The next decisive advance must therefore be an independent arithmetic inequality or a demonstrable improvement in the continuation estimates. Relabelling a positivity condition, extrapolating the numerical margin, or assuming strict contraction would not provide that advance. RH remains unproved in this work.
