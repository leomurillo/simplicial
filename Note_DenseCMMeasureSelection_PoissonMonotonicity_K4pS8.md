# Dense CM Measure Selection: Poisson Monotonicity

Random suffix: `K4pS8`

Mission: attack the dense CM measure-selection theorem.

Verdict: the dense theorem has an equivalent and very concrete form:
vertical modulus monotonicity of the normalized Cayley-Menger transfer
\[
{\mathcal T}_{\rm CM}(z)
=
{{\mathcal C}_B(z)\over{\mathcal A}_B(z)}
=
\Xi(z).
\]

This does not prove RH by itself, but it converts the remaining measure
selection problem into a sharp geometric inequality.

## 1. The Poisson family

Let
\[
m_B(z)=-{\Xi'(z)\over\Xi(z)}.
\]

For \(z=x+iy\), analyticity gives
\[
\partial_y\log|\Xi(x+iy)|
=
\operatorname{Re}\left(i{\Xi'(z)\over\Xi(z)}\right)
=
\operatorname{Im}\left(-{\Xi'(z)\over\Xi(z)}\right)
=
\operatorname{Im}m_B(z).
\]

Therefore the dense measure-selection law
\[
m_B(z)=\int_{\mathbb R}{d\mu(t)\over t-z}
\]
is equivalent to positivity of the Poisson family
\[
\boxed{
u_y(x)
:=
{1\over\pi}\partial_y\log|\Xi(x+iy)|
=
{1\over\pi}\operatorname{Im}m_B(x+iy)
\ge0
}
\]
for every \(x\in\mathbb R\), \(y>0\), plus the usual growth condition for a
Nevanlinna representation.

In CM language:
\[
\boxed{
\partial_y
\log
\left|
{{\mathcal C}_B(x+iy)\over{\mathcal A}_B(x+iy)}
\right|
\ge0.
}
\]

The normalized Cayley-Menger volume transfer must grow away from the
K-fixed boundary.

## 2. Why real boundary zeros give positivity

If the zeros of \(\Xi\) are real, then locally/canonically
\[
\Xi(z)=C\prod_{\gamma\in\Gamma}(1-z/\gamma)
\]
with the standard symmetric convergence.  Each real zero contributes
\[
\partial_y\log|z-\gamma|
=
{y\over (x-\gamma)^2+y^2}
>0.
\]

Thus
\[
\partial_y\log|\Xi(x+iy)|
=
\sum_{\gamma\in\Gamma}
{m_\gamma y\over (x-\gamma)^2+y^2}
\ge0.
\]

This is exactly the Poisson extension of the boundary divisor measure:
\[
u_y(x)
=
{1\over\pi}
\sum_{\gamma\in\Gamma}
{m_\gamma y\over (x-\gamma)^2+y^2}
=
(P_y*d\mu)(x).
\]

Letting \(y\downarrow0\) recovers
\[
d\mu=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma.
\]

## 3. Why an off-boundary zero breaks positivity

Suppose \(\Xi\) had a zero
\[
a=\alpha+i\beta,\qquad \beta>0.
\]

The local factor \(z-a\) contributes
\[
\partial_y\log|z-a|
=
{y-\beta\over (x-\alpha)^2+(y-\beta)^2}.
\]

At \(x=\alpha\) and \(0<y<\beta\), this equals
\[
{1\over y-\beta}<0,
\]
and tends to \(-\infty\) as \(y\uparrow\beta\) from below.  All other
nonzero analytic factors are locally bounded in logarithmic derivative, so
the total vertical derivative becomes negative in a punctured neighborhood
below the off-boundary zero.

Therefore
\[
\boxed{
\partial_y\log|\Xi(x+iy)|\ge0
\;\forall x,\;y>0
\quad\Longleftrightarrow\quad
\operatorname{zeros}(\Xi)\subset\mathbb R.
}
\]

Equivalently,
\[
\boxed{
\text{Poisson monotonicity of }{\mathcal T}_{\rm CM}
\quad\Longleftrightarrow\quad
\text{RH}.
}
\]

## 4. The new exact theorem target

The Dense CM Measure-Selection Theorem can now be stated as:

\[
\boxed{
\textbf{CM Poisson Monotonicity Theorem.}
}
\]

For every \(x\in\mathbb R\) and \(y>0\),
\[
\partial_y
\log
\left|
{{\Delta_{\rm CM}(F_c(x+iy))}\over{\mathcal A}_B(x+iy)}
\right|
\ge0.
\]

Since the quotient is \(\Xi\), this theorem would prove RH.  The value of the
CM/Bures reduction is that it asks for positivity of a normalized
Cayley-Menger transfer, rather than positivity of an abstract zeta object.

## 5. What remains non-circular

The proof cannot use:

1. real-rootedness of \(\Xi\);
2. positivity of the divisor measure;
3. pre-existing Herglotz/de Branges positivity of \(m_B\).

It must prove the vertical monotonicity directly from:

1. the six-edge \(Z/6\) Bures-Cayley packet;
2. the cofactor subtraction \({\mathcal A}_B\);
3. K-covariance and the Archimedean gamma multiplier;
4. the finite-place Noether-Weil recovery/positivity structure.

This is the current best formulation of the infinite selection lock.

