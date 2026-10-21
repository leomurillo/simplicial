# N7 lower-bound attempt: exact arithmetic cancellation and the remaining estimate

10 October 2026. Follow-up to `N7-Divergent-Audit-2026-10-10.md`.

**Outcome.** The requested uniform polynomial lower bound has not been established. This note establishes an explicit one-function test of the cancellation, proves its exact growth relation to zero displacement, and records an unconditional lower bound for the full form. None proves RH, and no novelty claim is made for these explicit-formula deductions.

## 1. The uniform lower bound obtainable by elementary estimates

Let f be supported in [-T,T], lambda=e^T, and use the pole-inclusive additive Weil form. Set Omega_0=psi(1/4)-log(pi). The archimedean multiplier is at least Omega_0: the series for the digamma function gives

\[
\Re\psi(a+it)-\psi(a)
=\sum_{k\ge0}\frac{t^2}{(k+a)((k+a)^2+t^2)}\ge0
\quad(a>0).
\]

Each prime translation has absolute quadratic contribution at most
2 Lambda(n)/sqrt(n) times ||f||_2^2. The pole operator is u tensor v + v tensor u, with u(x)=e^(x/2), v(x)=e^(-x/2) on the window. Its two nonzero eigenvalues are

\[
2T+2\sinh T,\qquad 2T-2\sinh T.
\]

Consequently the full spectral bottom satisfies

\[
e(T)\ge\Omega_0+2T-2\sinh T
-2\sum_{n\le e^{2T}}\frac{\Lambda(n)}{\sqrt n}.
\tag{1}
\]

Chebyshev's bound psi(x)=O(x) and partial summation give sum_{n<=Y} Lambda(n)/sqrt(n)=O(sqrt(Y)). Hence

\[
\boxed{e(T)\ge-Ce^T=-C\lambda.}
\tag{2}
\]

This is a full-form bound, uniform over all test functions. It is exponentially worse in T than the needed -C(1+T)^m. On even functions the pole term is nonnegative, but the prime-translation estimate still has order lambda. Thus parity alone does not repair this estimate.

## 2. One explicit function tests the cancellation

Set a=log(2) and choose the piecewise smooth form-domain function

\[
f(x)=e^x\mathbf 1_{[0,a]}(x),\qquad \|f\|_2^2=\frac32.
\]

Its autocorrelation g=f*f^* is

\[
g(v)=
\begin{cases}
2e^{-|v|}-\tfrac12e^{|v|},& |v|\le\log2,\\
0,& |v|>\log2.
\end{cases}
\tag{3}
\]

It is continuous, with piecewise smooth derivative. Its bilateral Laplace transform is the entire function

\[
G(s)=\int g(v)e^{-sv}\,dv
=\frac{(2^{1-s}-1)(2^{1+s}-1)}{1-s^2}
=\frac{5-4\cosh(s\log2)}{1-s^2}.
\tag{4}
\]

The singularities at s=+/-1 are removable, with G(+/-1)=3 log(2)/2. All its zeros have real part +1 or -1; the apparent zeros at s=+/-1 cancel. In particular,

\[
G(s)\ne0\quad\text{when }|\Re s|<1.
\tag{5}
\]

On the closed strip |Re(s)|<=1/2 it also satisfies |G(s)|<=C/(1+|Im(s)|^2). This decay makes the zero sums below absolutely convergent, without RH.

Let W be the additive Weil distribution, and define K(t)=(W*g)(t). Because g is even, this agrees with W(tau_t g). For t>a the support of the translated test misses the origin, and W has the ordinary expression

\[
W(x)=e^{x/2}+e^{-x/2}
-\frac{e^{-x/2}}{1-e^{-2x}}
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta(x-\log n),\quad x>0.
\]

Thus no regularization at zero is needed to compute K(t).

## 3. The exact prime-sum identity

For real X>2 define

\[
P(X)=\sum_{X/2\le n\le2X}\frac{\Lambda(n)}{\sqrt n}
g\!\left(\log\frac nX\right),
\qquad
A=G(1/2)=\frac43(5-3\sqrt2).
\tag{6}
\]

There is no endpoint convention issue: g vanishes at +/-log(2). Put

\[
D(X)=X^{-5/2}\int_{-a}^{a}
\frac{g(v)e^{5v/2}}{1-X^{-2}e^{2v}}\,dv.
\tag{7}
\]

For X>=3, D is positive and O(X^(-5/2)). Substituting the positive-half-line expression for W and combining the decaying pole term with the archimedean term gives exactly

\[
\boxed{K(\log X)=A\sqrt X-P(X)-D(X).}
\tag{8}
\]

In detail, the two pole terms contribute A(sqrt(X)+1/sqrt(X)). The archimedean integral is

\[
X^{-1/2}\int_{-a}^{a}
\frac{g(v)e^{v/2}}{1-X^{-2}e^{2v}}\,dv
=AX^{-1/2}+D(X).
\]

This establishes both the sign and the size of the small correction.

The prime sum is particularly simple to evaluate. For n<=X its weight is

\[
\frac{\Lambda(n)}{\sqrt n}g(\log(n/X))
=\Lambda(n)\left(\frac{2\sqrt n}{X}-\frac{X}{2n^{3/2}}\right),
\]

and for n>=X its weight is

\[
\Lambda(n)\left(\frac{2X}{n^{3/2}}-\frac{\sqrt n}{2X}\right).
\]

## 4. An exact criterion and exact growth exponent

**Proposition.** The following are equivalent:

1. RH.
2. P(X)-A sqrt(X) is bounded for X>=3.
3. For some finite m, P(X)-A sqrt(X)=O((1+log(X))^m).

**Proof of 1 implies 2.** The explicit formula gives the absolutely convergent expansion

\[
K(t)=\sum_\rho G(\rho-1/2)e^{(\rho-1/2)t}.
\tag{9}
\]

Under RH, G(i gamma)=|integral_0^a e^x e^(-i gamma x) dx|^2 >=0. Therefore

\[
|K(t)|\le\sum_\rho G(i\gamma)=Q(f)<\infty.
\tag{10}
\]

Equation (8) proves boundedness. Clearly 2 implies 3.

**Proof of 3 implies 1.** Equation (8) gives polynomial growth of K(t) as t tends to +infinity. Cut W off smoothly near the origin and on the negative half-line, obtaining W_+. Then W_+*g agrees with K for all sufficiently large positive t and has support bounded below. Its Laplace transform is holomorphic for Re(s)>0. Initially for Re(s)>1/2 it equals

\[
G(s)\left[
\frac1{s-1/2}+\frac{\zeta'}{\zeta}(s+1/2)+H(s)
\right],
\tag{11}
\]

where H is holomorphic for Re(s)>0. A zero rho to the right of the critical line creates a pole at s=rho-1/2. By (5), G cannot cancel it. The pole at s=1/2 is already canceled by the zeta pole; it is not a nontrivial zero. This contradiction excludes zeros to the right; the functional equation excludes those to the left. QED.

This argument applies to the continuous g in (3): after the cutoff W_+ is a locally finite signed measure, and the convolutions and Laplace transforms are ordinary locally convergent integrals/sums. For (9), piecewise regularity and the O(1/|gamma|^2) transform decay also allow the usual explicit formula by smooth approximation.

There is a sharper statement. Define

\[
\Theta=\sup_\rho(\Re\rho-1/2),\qquad 0\le\Theta\le1/2.
\]

Then

\[
\boxed{
\limsup_{X\to\infty}
\frac{\log(1+|P(X)-A\sqrt X|)}{\log X}=\Theta.
}
\tag{12}
\]

For the upper bound use (9), |G(rho-1/2)|<=C/(1+|Im(rho)|^2), and standard zero counting to get |K(t)|<=C exp(Theta*t) for t>=0. For the lower bound, an exponent strictly smaller than Theta would make the transform (11) holomorphic in a half-plane containing at least one of its nonremovable zero poles. If Theta=0, (9) gives boundedness and the displayed limsup is zero.

Consequently the external 7/8 strip, if used, gives the proved estimate

\[
P(X)-A\sqrt X=O(X^{3/8}).
\tag{13}
\]

No logarithmic factor is required for this fixed smoothing kernel. It does not yield boundedness. Equation (12) explains why smoothing itself cannot remove a genuine positive displacement exponent. It is not an impossibility theorem for an additional arithmetic argument that might show Theta=0.

## 5. Connection to the requested lower bound

The two translates f +/- tau_t f have disjoint supports for t>a. Recenter their support in [-T,T], where T=(t+a)/2. Their norm squared is 3 and

\[
Q(f\pm\tau_t f)=2Q(f)\pm2K(t).
\]

Hence

\[
e((t+a)/2)\le\frac{Q(f)-|K(t)|}{3/2}.
\tag{14}
\]

A polynomial lower bound on e(T) would therefore imply polynomial growth of this one K(t), and hence RH by Section 4. Thus the sought cancellation must hold already on these two-dimensional families. No choice of prolate truncation or ground-state parity removes that necessary test.

Conversely, establishing boundedness of this explicit prime discrepancy would prove RH and therefore the full lower bound with C=0. This replaces the universal form inequality by a scalar arithmetic estimate, but does not supply that estimate.

There is even an explicit constant available conditionally on RH. Since this f is at the first-prime threshold and g(log(2))=0, Q(f) has no prime contribution. Its arithmetic expression is

\[
q_0=2A-\frac32\left(\gamma_E+\log(4\pi)+\log\tanh(a/2)\right)
-\int_0^a\frac{e^{v/2}g(v)-3/2}{\sinh v}\,dv.
\tag{15}
\]

Numerically q_0=0.29984744568842157736... . Under RH, (10) gives

\[
|P(X)-A\sqrt X+D(X)|\le q_0\quad(X>2).
\tag{16}
\]

The formula for q_0 is unconditional; asserting (16) for every X would prove RH. Its availability as a number does not prove the inequality.

## 6. Numerical checks and what they do not establish

The accompanying script `empirical/connes_route/probe_translated_prime_cancellation.py` sieves all prime powers through 2,000,000 and evaluates seven sample windows. It independently checks three sums with 50-digit arithmetic and checks (4) against quadrature at three complex arguments. These are numerical cross-checks, not interval certificates or a test of every X in a continuum.

| X | P(X)-A sqrt(X) |
|---:|---:|
| 3 | 0.0410126110 |
| 10 | -0.0737456288 |
| 100 | 0.0832944813 |
| 1,000 | 0.0704725411 |
| 10,000 | -0.0015523923 |
| 100,000 | -0.0493732542 |
| 1,000,000 | -0.0838142386 |

The independent 50-digit residual comparisons differed from double precision by at most 6.4e-15 at the checked samples; the transform checks differed by at most 2.7e-51. These finite data do not bound the infinite tail and do not improve a zero-free region.

## 7. What remains unestablished

The missing assertion is now explicit:

\[
\left|\sum_{X/2\le n\le2X}\frac{\Lambda(n)}{\sqrt n}
g(\log(n/X))-\frac43(5-3\sqrt2)\sqrt X\right|
\le C(1+\log X)^m
\quad\text{for every real }X\ge3.
\]

Neither (1), the external fixed strip, the point-value defect lemma, nor small Rayleigh quotients establish this assertion. The elementary universal lower estimate remains -C lambda, and the strip-based estimate for this fixed scalar discrepancy remains O(X^(3/8)). There is no justified passage here from either exponential scale to the required polynomial-in-log scale.

This is a completed derivation of the necessary arithmetic cancellation and its obstruction, not a completion of the requested RH proof.

## Sources and provenance

- [Connes–Consani–Moscovici, Zeta Spectral Triples](https://arxiv.org/html/2511.22755v1), for the form and its piecewise smooth core conventions.
- [DLMF 27.4](https://dlmf.nist.gov/27.4), for the von Mangoldt logarithmic-derivative Dirichlet series.
- [OpenAI family 003 scope](https://github.com/openai/math/blob/main/lean/docs/003.md), only for the external reported 7/8 strip in (13); the main identities and equivalences do not depend on it.
- Equations (1)–(16) were derived in this work from the stated definitions and the explicit formula. No claim of independent verification of the external Lean formalization is made.
