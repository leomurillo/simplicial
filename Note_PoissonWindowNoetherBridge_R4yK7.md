# Note: Poisson-Window Bridge From Noether-Weil Positivity to CM Monotonicity

Random suffix: `R4yK7`

Mission: continue the infinite route after the finite Bures-Cayley no-go.
The goal is to isolate the exact bridge by which a global positive spectral
form, such as Weil positivity or the program's primorial Noether-Weil
positivity, forces pointwise CM Poisson Monotonicity.

## 1. The Local Quantity

The normalized Cayley-Menger transfer is
\[
{\mathcal T}_{\rm CM}(z)
=
{\Delta_{\rm CM}(F_c(z))\over {\mathcal A}_B(z)}
=
\Xi(z).
\]

Define
\[
m_B(z)=-{\Xi'(z)\over \Xi(z)},\qquad
u_B(x,y)=\operatorname{Im}m_B(x+iy).
\]

Since
\[
u_B(x,y)
=
\partial_y\log|\Xi(x+iy)|
=
\partial_y\log
\left|
{\Delta_{\rm CM}(F_c(x+iy))\over {\mathcal A}_B(x+iy)}
\right|,
\]
CM Poisson Monotonicity is
\[
u_B(x,y)\ge0,\qquad x\in{\mathbb R},\;y>0.
\]

The previous note showed this is equivalent to RH.  So the only non-circular
way forward is to derive \(u_B\ge0\) from an independent positive spectral
form.

## 2. Poisson-Window Functionals

For a nonnegative test window \(\phi\in C_c^\infty({\mathbb R})\) and \(y>0\),
define
\[
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}\phi(x)\,u_B(x,y)\,dx.
\]

Equivalently,
\[
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}
\phi(x)\,
\partial_y\log
\left|
{\Delta_{\rm CM}(F_c(x+iy))\over{\mathcal A}_B(x+iy)}
\right|dx.
\]

This is the weak, windowed form of CM Poisson Monotonicity.

## 3. Window Positivity Is Equivalent to Pointwise Monotonicity

**Lemma 3.1 (window-to-pointwise).**  
Assume \(u_B\) is locally integrable on \({\mathbb C}_+\) away from its poles.
Then the following are equivalent:

1. \(u_B(x,y)\ge0\) for every \(x\in{\mathbb R}\), \(y>0\) away from zeros;
2. \({\mathfrak P}_{\phi,y}(\Xi)\ge0\) for every \(y>0\) and every
   nonnegative \(\phi\in C_c^\infty({\mathbb R})\).

*Proof.*  
The pointwise statement implies the window statement by integration against
\(\phi\ge0\).

Conversely, suppose \(u_B(x_0,y_0)<0\) at a regular point.  By continuity
there is an interval \(I\) around \(x_0\) on which \(u_B(x,y_0)<-\epsilon\).
Choose \(0\le\phi\in C_c^\infty(I)\), \(\phi\not\equiv0\).  Then
\[
{\mathfrak P}_{\phi,y_0}(\Xi)
=
\int\phi(x)u_B(x,y_0)\,dx
<0,
\]
contradicting window positivity.

If the failure is caused by an off-boundary zero \(a=\alpha+i\beta\), then
for \(y<\beta\) sufficiently close to \(\beta\),
\[
u_B(\alpha,y)
=
{m\over y-\beta}+O(1)<0,
\]
so the same interval argument applies below the pole. \(\square\)

Thus:
\[
\boxed{
{\mathfrak P}_{\phi,y}(\Xi)\ge0
\ \forall \phi\ge0,\ y>0
\quad\Longleftrightarrow\quad
\text{CM Poisson Monotonicity}.
}
\]

This is useful because global positivity principles usually act on test
functions rather than pointwise values.

## 4. Real Boundary Divisors Give Positive Windows

If the divisor is boundary-supported,
\[
d\mu_\Xi=\sum_{\Xi(\gamma)=0}m_\gamma\delta_\gamma,
\]
then
\[
u_B(x,y)
=
\int_{\mathbb R}{y\over (x-t)^2+y^2}\,d\mu_\Xi(t).
\]

Therefore
\[
{\mathfrak P}_{\phi,y}(\Xi)
=
\int_{\mathbb R}
\left[
\int_{\mathbb R}
{\phi(x)y\over (x-t)^2+y^2}\,dx
\right]
d\mu_\Xi(t).
\]

The inner bracket is nonnegative for \(\phi\ge0\).  Thus boundary support
implies all Poisson windows are nonnegative.

The converse is the content of Lemma 3.1 plus the local off-boundary-zero
calculation: any interior divisor point creates a negative window just below
it.

## 5. How Weil Positivity Enters

Weil positivity is a global spectral positivity law on a dense class of
autocorrelation tests \(F=f*f^*\):
\[
{\mathcal W}_\zeta(F)\ge0.
\]

The classical theorem says this is equivalent to RH.  For this program, the
important local reformulation is:

> It is enough for the Weil/Noether-Weil test class to contain, or approximate
> in the Weil topology, the Poisson-window autocorrelations that detect
> negativity of \(u_B\).

Indeed, Gaussian autocorrelations
\[
\Phi_{x_0,\sigma}(x)
=
\exp\!\left(-{(x-x_0)^2\over 2\sigma^2}\right)
\]
are positive windows.  If \(u_B(x_0,y_0)<0\), then for \(\sigma\) small,
\[
{\mathfrak P}_{\Phi_{x_0,\sigma},y_0}(\Xi)<0.
\]

So any global positivity theorem that controls all sufficiently narrow
Gaussian/Poisson windows rules out off-boundary zeros and forces CM Poisson
Monotonicity.

## 6. The Primorial Noether-Weil Bridge

Paper 22 proposes finite positive forms
\[
{\mathcal Q}_n(J)\ge0
\]
and the Primorial Noether-Weil Identity
\[
\lim_{n\to\infty}{\mathcal Q}_n(\mathscr R_n f)
=
{\mathcal W}_\zeta(f*f^*).
\]

Therefore, if the recovery class is dense enough to approximate the
Poisson-window autocorrelations above, then
\[
{\mathcal W}_\zeta(f*f^*)\ge0
\quad\Longrightarrow\quad
{\mathfrak P}_{\phi,y}(\Xi)\ge0
\quad\Longrightarrow\quad
u_B(x,y)\ge0.
\]

In diagram form:
\[
\boxed{
\text{finite Noether positivity}
\Rightarrow
\text{Weil positivity}
\Rightarrow
\text{Poisson-window positivity}
\Rightarrow
\text{CM Poisson Monotonicity}
\Rightarrow
\mathrm{RH}.
}
\]

This is not circular if the Primorial Noether-Weil Identity is proved from the
finite primorial/current geometry, because the implication then starts from
\({\mathcal Q}_n\ge0\), not from boundary support of \(\Xi\).

## 7. Cubic Noether-Weil Specialization

The cubic branch in `ocho.md` and `diez.md` supplies the local obstruction in a
stronger, third-order form:

1. A hypothetical off-line zero forces an FE-symmetric four-zero cluster.
2. The cubic Bombieri witness creates a negative \(\delta^2\) correction.
3. Cubic positivity forbids that correction.
4. Therefore cubic positivity implies no off-line zeros.

Translated into the present window language:

\[
\text{off-line zero}
\Rightarrow
\exists(\phi,y)\text{ with }{\mathfrak P}_{\phi,y}<0
\Rightarrow
\exists(g,\eta)\text{ with cubic witness }{\mathcal C}_\zeta(g;\eta)<0.
\]

The first arrow is pure divisor/Poisson geometry.  The second arrow is the
program's cubic refinement: it does not merely see a negative local window; it
packages the same defect into the \(Z/6\)-native cubic selection rule.

Thus the cubic branch is the most native path to the missing sign, while the
Poisson-window formulation is the clean local shadow of that path.

## 8. What Is Still Missing

The remaining non-circular theorem is now even sharper:

\[
\boxed{
\textbf{Poisson-Window Recovery Theorem.}
}
\]

The primorial recovery maps \(\mathscr R_n\) must approximate the positive
Poisson-window autocorrelations densely enough that finite Noether positivity
\({\mathcal Q}_n\ge0\) passes to
\[
{\mathfrak P}_{\phi,y}(\Xi)\ge0
\quad
(\phi\ge0,\ y>0).
\]

Paper 22 calls the all-order version the Primorial Noether-Weil Identity.
`ocho.md` and `diez.md` call the cubic route the [A3] primorial
Bombieri-Vinogradov tightening to the critical line.  These are two faces of
the same infinite closure problem:

1. recover the completed explicit-formula positivity from finite primorial
   currents;
2. ensure the recovered test class includes the local windows that detect
   off-boundary CM divisor mass.

## 9. Status

We now have a precise bridge theorem:

\[
\boxed{
\text{Poisson-window positivity}
\Longleftrightarrow
\text{CM Poisson Monotonicity}
\Longleftrightarrow
\mathrm{RH}.
}
\]

And a precise programmatic route:

\[
\boxed{
\text{Primorial Noether-Weil recovery on Gaussian/Poisson windows}
\Longrightarrow
\text{Poisson-window positivity}
\Longrightarrow
\mathrm{RH}.
}
\]

So the next mathematical work is no longer to invent a new local curvature.
It is to prove the Poisson-Window Recovery Theorem inside the primorial
Noether-Weil/cubic-BV machinery.

