# The signed Selberg recurrence: centering and the missing contraction

10 October 2026. This note continues the arithmetic barrier attempt. It does not prove RH or a polynomial-in-log discrepancy bound.

## 1. Retain the convolution exactly

Set

\[
R(x)=\psi(x)-x,\qquad
S(x)=R(x)\log x+\sum_{n\le x}\Lambda(n)R(x/n)
\quad(x\ge1).
\tag{1}
\]

The standard Selberg symmetry estimate gives S(x)=O(x). See [Selberg's original paper, equations (2.8)–(2.9)](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf); the prime-power version follows with errors of size O(x). An independently implemented formal treatment is available in [the Archive of Formal Proofs](https://isa-afp.org/browser_info/current/AFP/Prime_Distribution_Elementary/Selberg_Asymptotic_Formula.html).

With S defined by (1), the recurrence is exact:

\[
R(x)=-\frac1{\log x}\sum_{n\le x}\Lambda(n)R(x/n)
+\frac{S(x)}{\log x},\qquad x>1.
\tag{2}
\]

The sign in front of the convolution matters. Replacing it by an absolute-value bound discards precisely the cancellation being sought.

## 2. The positive operator amplifies power envelopes

For 0<beta<1, apply the absolute convolution operator to the envelope f(y)=y^beta:

\[
\frac1{\log x}\sum_{n\le x}\Lambda(n)f(x/n)
=x^\beta N_\beta(x),\qquad
N_\beta(x)=\frac1{\log x}\sum_{n\le x}\frac{\Lambda(n)}{n^\beta}.
\]

Partial summation and psi(x)~x prove

\[
\sum_{n\le x}\frac{\Lambda(n)}{n^\beta}
=x^{-\beta}\psi(x)+\beta\int_1^x\frac{\psi(t)}{t^{\beta+1}}\,dt
\sim\frac{x^{1-\beta}}{1-\beta}.
\]

Consequently

\[
\boxed{N_\beta(x)\sim\frac{x^{1-\beta}}{(1-\beta)\log x}\longrightarrow\infty.}
\tag{3}
\]

For functions controlled only by |f(y)|≤Cy^beta, this factor is the sharp pointwise operator bound: equality is attained by the positive envelope itself. It follows that this absolute-value estimate does not preserve, let alone improve, a power-saving envelope for R. This is a statement about this operator bound, not an impossibility theorem for the signed recurrence or all elementary methods.

Restricting the sum to n≤(log x)^k gives a factor asymptotic to (log x)^{k(1−beta)−1}/(1−beta), so that small part can contract if k(1−beta)<1. The omitted part still requires a signed estimate. Discarding it is not justified.

## 3. The residual has a removable leading term

**Proposition.** Unconditionally,

\[
S(x)=-(1+\gamma_E)x+o(x).
\tag{4}
\]

Here gamma_E is Euler's constant. The proof uses classical quantitative PNT, not RH.

Put

\[
M(x)=\sum_{n\le x}\frac{\Lambda(n)}n,
\qquad C(x)=\sum_{mn\le x}\Lambda(m)\Lambda(n).
\]

Classical PNT implies R(x)=o(x/log x) and

\[
M(x)=\log x-\gamma_E+o(1).
\tag{5}
\]

To identify the constant in (5), partial summation with the classical integrable PNT remainder gives a constant limit for M−log. The Laurent expansion −zeta'(1+u)/zeta(1+u)=1/u−gamma_E+O(u) identifies that constant as −gamma_E by Abelian integration. Only a remainder O(x/log^K x) for fixed K>2 is needed here, available from classical PNT estimates.

Let y=sqrt x. The exact hyperbola identity is

\[
C(x)=2\sum_{n\le y}\Lambda(n)\psi(x/n)-\psi(y)^2.
\]

For n≤y the arguments x/n are at least sqrt x. Uniformly using psi(z)=z+O(z/log^K z), the error in replacing psi(x/n) by x/n is O(x M(y)/log^K x)=o(x). Also psi(y)^2=x+o(x). Hence

\[
C(x)=2xM(\sqrt x)-x+o(x)
=x\log x-(2\gamma_E+1)x+o(x).
\tag{6}
\]

From the definition (1),

\[
S(x)=R(x)\log x+C(x)-xM(x).
\]

Equations (5)–(6) and R(x)log x=o(x) prove (4).

Thus the natural centered forcing is

\[
T(x)=S(x)+(1+\gamma_E)x=o(x).
\tag{7}
\]

This centering is a proved asymptotic improvement over the coarse O(x) residual. It is not a square-root bound: the proof inherits classical PNT precision and gives no contraction toward the critical line.

## 4. The exact signed transform still contains the zero obstruction

For Re s>1, put

\[
F(s)=-\frac{\zeta'(s)}{\zeta(s)},\qquad
r(s)=\int_1^\infty R(x)x^{-s-1}\,dx
=\frac{F(s)}s-\frac1{s-1}.
\]

Absolute convergence permits differentiation and interchange of the convolution and integral. Therefore the Mellin transform of S is exactly

\[
\begin{aligned}
\widehat S(s)&=-r'(s)+F(s)r(s)\\
&=\frac{\zeta''(s)}{s\zeta(s)}+\frac{F(s)}{s^2}
-\frac1{(s-1)^2}-\frac{F(s)}{s-1}.
\end{aligned}
\tag{8}
\]

Its residue at s=1 is −(1+gamma_E), in agreement with (4). Centering T adds (1+gamma_E)/(s−1) to (8), canceling this pole.

The differential equation can be written

\[
\boxed{(\zeta(s)r(s))'=-\zeta(s)\widehat S(s).}
\tag{9}
\]

Locally, on a simply connected zero-free domain, its solution is

\[
r(s)=\frac{C-\int_{s_0}^s\zeta(u)\widehat S(u)\,du}{\zeta(s)}.
\tag{10}
\]

The actual initial value fixes C; it is not a free parameter we may choose to force cancellation at zeros. Extending (10) across a zero requires the numerator to vanish to sufficient order there. Neither the O(x) estimate nor the o(x) centered estimate supplies this divisibility. Even regularity of a prescribed forcing would not, by itself, eliminate the homogeneous solution C/zeta.

There is another diagnostic. At a zero rho of multiplicity m, write zeta(s)=(s−rho)^m h(s), with h(rho) nonzero. Then

\[
\frac{\zeta''(s)}{\zeta(s)}
=\frac{m(m-1)}{(s-\rho)^2}
+\frac{2m}{s-\rho}\frac{h'(s)}{h(s)}
+\frac{h''(s)}{h(s)}.
\]

For a simple zero, the double pole cancels exactly in F²−F'. Remaining singularities need not cancel. Thus the nonlinear-looking Selberg identity does not automatically magnify every zero into a contradiction with its O(x) remainder. A term of size x^beta, or x^beta log x, with beta<1 is itself compatible with that coarse remainder. This is a scale comparison, not an assertion that every hypothetical zero produces a nonzero residue in (8).

## 5. Checks and actual outcome

`empirical/connes_route/probe_selberg_recurrence.py` evaluates (1) directly from a sieve and reports the positive-operator factors. It uses the real argument x/n in R(x/n)=psi(floor(x/n))−x/n; replacing the second term by floor(x/n) would change the residual.

At x=1,000,000 the numerical values are:

- S(x)/x ≈ −1.57806166.
- T(x)/x ≈ −0.00084599.
- N_(7/8)(x) ≈ 2.63353.
- N_(1/2)(x) ≈ 144.54093.

These finite computations illustrate the analytic formulas; they are not interval certificates or a proof of any asymptotic.

Retaining the convolution has yielded an exact centered equation and located the obstruction in both real and Mellin variables. The absolute operator is not a contraction at the needed exponent, and the signed equation retains the reciprocal-zeta denominator. No uniform one-sided bound for the original smoothed prime discrepancy follows from the estimates established here. Such a bound remains the unproved step.
