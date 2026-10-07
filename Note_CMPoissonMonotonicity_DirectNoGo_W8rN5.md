# Note: CM Poisson Monotonicity Direct No-Go and Equivalent Closures

Random suffix: `W8rN5`

Mission: prove CM Poisson Monotonicity directly from the Bures-Cayley geometry,
and if the direct proof is impossible, prove the strongest available theorem
from another positivity framework.

## 1. The Exact Object

Let
\[
z=t+i y,\qquad s={1\over2}+iz,
\]
and let
\[
\Xi(z)=\xi\!\left({1\over2}+iz\right).
\]

The completed Bures-Cayley construction has already identified the normalized
Cayley-Menger transfer
\[
{\mathcal T}_{\rm CM}(z)
:=
{\Delta_{\rm CM}(F_c(z))\over {\mathcal A}_B(z)}
=
\Xi(z),
\]
where \(F_c\) is the completed six-edge \(Z/6\) Bures packet and
\({\mathcal A}_B\) is the nonzero CM cofactor.

CM Poisson Monotonicity is therefore the inequality
\[
\boxed{
\partial_y\log|{\mathcal T}_{\rm CM}(x+iy)|\ge 0
\quad (x\in{\mathbb R},\;y>0).
}
\]

Equivalently,
\[
\partial_y\log|\Xi(x+iy)|
=
\operatorname{Im}\left(-{\Xi'(x+iy)\over \Xi(x+iy)}\right)
=
\operatorname{Im}m_B(x+iy).
\]

Thus CM Poisson Monotonicity is exactly the Herglotz sign of the Bures
log-derivative \(m_B=-\Xi'/\Xi\).

## 2. Direct Finite Bures-Cayley Geometry Is Not Enough

The finite six-edge geometry gives:

1. the tetrahedral edge carrier \(F_c(z)\in{\mathbb C}^6\);
2. the antiunitary \(K:r\mapsto -r\pmod 6\), realized as edge reversal;
3. the Cayley-Menger cubic \(\Delta_{\rm CM}\);
4. the factorization
   \[
   \Delta_{\rm CM}(F_c)=\Xi\,{\mathcal A}_B;
   \]
5. the normalized divisor identity
   \[
   -\partial\log\Delta_{\rm CM}(F_c)+\partial\log{\mathcal A}_B
   =
   -{\Xi'\over\Xi}.
   \]

These are exact and powerful.  But they are divisor-identification laws, not
positive-measure laws.

To see the obstruction, take any \(\gamma>0\) and \(\beta>0\) and define the
real-even, \(K\)-symmetric fake transfer
\[
X_{\gamma,\beta}(z)
=
\big((z-\gamma)^2+\beta^2\big)
\big((z+\gamma)^2+\beta^2\big).
\]

It has the same formal spectral symmetries as \(\Xi\):
\[
X_{\gamma,\beta}^\#=X_{\gamma,\beta},\qquad
X_{\gamma,\beta}(-z)=X_{\gamma,\beta}(z),
\]
but its zeros are
\[
\gamma\pm i\beta,\qquad -\gamma\pm i\beta,
\]
which are off the boundary.

If \(A(z)\) is any nonvanishing \(K\)-real cofactor, then
\[
C_{\gamma,\beta}(z)=X_{\gamma,\beta}(z)A(z)
\]
has the same normalized-divisor form
\[
{C_{\gamma,\beta}(z)\over A(z)}=X_{\gamma,\beta}(z).
\]

Now
\[
\partial_y\log|X_{\gamma,\beta}(x+iy)|
=
\sum_{\rho\in Z(X_{\gamma,\beta})}
{y-\operatorname{Im}\rho\over |x+iy-\rho|^2}.
\]

At \(x=\gamma\) and \(0<y<\beta\), the zero
\(\rho=\gamma+i\beta\) contributes
\[
{y-\beta\over (y-\beta)^2}={1\over y-\beta}<0,
\]
and it tends to \(-\infty\) as \(y\uparrow\beta\).  All other zero
contributions remain bounded there.  Hence
\[
\partial_y\log|X_{\gamma,\beta}(\gamma+iy)|<0
\]
for \(y\) close enough to \(\beta\) from below.

Therefore the finite \(K\)-symmetric CM divisor algebra admits off-boundary
models unless an additional positive spectral-measure law is imposed.

**Conclusion.**
\[
\boxed{
\text{The direct finite Bures-Cayley geometry identifies the divisor,}
\quad
\text{but does not by itself prove CM Poisson Monotonicity.}
}
\]

Any proof from the finite data alone would have to smuggle in a positivity
principle stronger than factorization, \(K\)-symmetry, and gamma normalization.

## 3. Exact Equivalence: CM Poisson Monotonicity iff RH

### RH implies CM Poisson Monotonicity

Assume RH.  Then all zeros of \(\Xi\) are real.  Since \(\Xi\) is real-even of
order one, its symmetric Hadamard product has the form
\[
\Xi(z)=\Xi(0)\prod_{\gamma>0}\left(1-{z^2\over \gamma^2}\right)
\]
with standard convergence.

Each real zero pair \(\pm\gamma\) contributes
\[
\partial_y\log|z-\gamma|
=
{y\over (x-\gamma)^2+y^2},
\qquad
\partial_y\log|z+\gamma|
=
{y\over (x+\gamma)^2+y^2}.
\]

Thus
\[
\partial_y\log|\Xi(x+iy)|
=
\sum_{\gamma>0}m_\gamma
\left(
{y\over (x-\gamma)^2+y^2}
+
{y\over (x+\gamma)^2+y^2}
\right)
\ge0.
\]

So RH gives CM Poisson Monotonicity.

### CM Poisson Monotonicity implies RH

Assume CM Poisson Monotonicity and suppose, for contradiction, that
\(\Xi\) has a nonreal zero
\[
a=\alpha+i\beta,\qquad \beta>0.
\]

Factor locally
\[
\Xi(z)=(z-a)^m G(z),\qquad G(a)\ne0.
\]

Then
\[
\partial_y\log|\Xi(z)|
=
m\,{y-\beta\over (x-\alpha)^2+(y-\beta)^2}
+
\partial_y\log|G(z)|.
\]

At \(x=\alpha\), the first term tends to \(-\infty\) as
\(y\uparrow\beta\) from below, while the \(G\)-term stays bounded.  Therefore
\[
\partial_y\log|\Xi(\alpha+iy)|<0
\]
for \(y<\beta\) close enough to \(\beta\), contradicting CM Poisson
Monotonicity.

So \(\Xi\) has no zeros in \({\mathbb C}_+\).  Since \(\Xi\) is real entire,
nonreal zeros occur in conjugate pairs, hence no nonreal zeros exist at all.
Thus every zero of \(\Xi\) is real, i.e. every nontrivial zero of \(\zeta\)
lies on the critical line.

Hence
\[
\boxed{
\text{CM Poisson Monotonicity}
\quad\Longleftrightarrow\quad
\text{RH}.
}
\]

## 4. Proof From Something Else: Four Equivalent Positive Laws

The direct finite geometry does not close the sign.  The sign can be obtained
from any one of the following genuinely infinite positivity laws.

### 4.1 Laguerre-Polya

If
\[
\Xi\in{\mathcal{LP}},
\]
the Laguerre-Polya class of real entire functions, then all zeros of \(\Xi\)
are real.  The product proof above gives CM Poisson Monotonicity immediately.

Conversely, CM Poisson Monotonicity forbids nonreal zeros, so for the completed
zeta function it forces \(\Xi\in{\mathcal{LP}}\) in the relevant real-even
order-one class.

Thus the Laguerre-Polya route is not weaker:
\[
\Xi\in{\mathcal{LP}}
\quad\Longleftrightarrow\quad
\text{CM Poisson Monotonicity}
\quad\Longleftrightarrow\quad
\text{RH}.
\]

### 4.2 Herglotz/Pick

Define
\[
m_B(z)=-{\Xi'(z)\over\Xi(z)}.
\]

CM Poisson Monotonicity is exactly
\[
\operatorname{Im}m_B(z)\ge0,\qquad z\in{\mathbb C}_+.
\]

With the usual growth normalization, this is the Herglotz/Nevanlinna
representation
\[
m_B(z)=a z+b+\int_{\mathbb R}
\left({1\over t-z}-{t\over 1+t^2}\right)d\mu(t),
\qquad d\mu\ge0.
\]

For \(\Xi\), the atoms of \(d\mu\) are precisely the boundary zeros
\(\gamma\), counted with multiplicity.  Therefore Herglotz positivity is
equivalent to boundary support of the CM divisor current.

### 4.3 de Branges

Let
\[
E_B(z)=\Xi(z)+i\Xi'(z).
\]

The Hermite-Biehler inequality
\[
|E_B(z)|>|E_B^\#(z)|,\qquad z\in{\mathbb C}_+,
\]
is equivalent to
\[
4|\Xi(z)|^2\operatorname{Im}\left(-{\Xi'(z)\over\Xi(z)}\right)>0.
\]

Thus \(E_B\) is Hermite-Biehler exactly when CM Poisson Monotonicity holds
away from the divisor.  The de Branges reproducing kernel is then the positive
Pick kernel of \(m_B\).

### 4.4 Weil / Cubic Noether Positivity

The classical Weil positivity criterion is equivalent to RH.  Therefore it
implies CM Poisson Monotonicity by the theorem above.

Inside the simplicial program, the non-reformulational route is the cubic
Noether-Weil branch of `ocho.md` and `diez.md`:

\[
\text{cubic positivity}
\Longrightarrow
\text{no off-line zero}
\Longrightarrow
\text{RH}
\Longrightarrow
\text{CM Poisson Monotonicity}.
\]

This is the strongest "from something else" path currently in the corpus.  It
does not pass through the finite six-edge CM shape space alone; it passes
through an infinite zero-spectrum positivity law.

## 5. Final Status

The theorem is now exactly located:

\[
\boxed{
\partial_y\log
\left|
{\Delta_{\rm CM}(F_c(x+iy))\over{\mathcal A}_B(x+iy)}
\right|
\ge0
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

The Bures-Cayley geometry gives the left-hand side as a normalized tetrahedral
volume-transfer derivative.  The missing sign is not a finite tetrahedral
identity.  It is the same infinite positive spectral-measure law that appears
as:

1. Laguerre-Polya real-rootedness;
2. Herglotz/Pick positivity of \(m_B\);
3. Hermite-Biehler/de Branges positivity of \(E_B=\Xi+i\Xi'\);
4. Weil positivity;
5. the program's cubic Noether-Weil positivity route.

So the direct proof from finite Bures-Cayley geometry is blocked by explicit
\(K\)-symmetric off-boundary fake transfers.  The viable closure is not to
search for another six-edge identity; it is to prove the infinite positivity
law, most naturally through the cubic Noether-Weil branch.

