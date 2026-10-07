# Normalized CM Divisor Boundary Attempt

Random suffix: `r9Xc2`

Mission: prove that the normalized Cayley-Menger divisor has boundary support
only.

Verdict: the exact statement is equivalent to RH.  The present
Cayley-Menger/K algebra proves the equivalence, but it does not yet supply an
independent positivity law strong enough to prove boundary support.

## 1. Normalized CM divisor

From `Note_BuresCayleyPickIdentity_v4Nq8.md`, the completed Bures edge packet
satisfies
\[
{\mathcal C}_B(z):=\Delta_{\rm CM}(F_c(z))
=
\Xi(z)\,{\mathcal A}_B(z),
\]
where
\[
{\mathcal A}_B(z)
=
-{a\over2}
\left({\mathcal L}_3(z)^2C_0(a,b)+\Xi(z)^2C_2(a,b)\right),
\qquad
a=2^{-1/2-iz},\quad b=3^{-1/2-iz}.
\]

The normalized Cayley-Menger transfer is therefore
\[
{\mathcal T}_{\rm CM}(z)
:=
{{\mathcal C}_B(z)\over{\mathcal A}_B(z)}
=
\Xi(z)
\]
as a meromorphic identity, with removable cancellation understood at common
zeros of numerator and cofactor.

Thus the normalized CM divisor current is
\[
D_{\rm CM}^{\rm norm}
=
\operatorname{div}{\mathcal T}_{\rm CM}
=
\operatorname{div}\Xi.
\]

Equivalently, for the log derivative,
\[
m_{\rm CM}(z)
:=
-\partial_z\log{\mathcal C}_B(z)
+\partial_z\log{\mathcal A}_B(z)
=
-{\Xi'(z)\over\Xi(z)}
=m_B(z),
\]
and
\[
D_{\rm CM}^{\rm norm}
=
-{1\over\pi}\partial_{\bar z}m_{\rm CM}
=
-{1\over\pi}\partial_{\bar z}m_B.
\]

## 2. Boundary support is exactly RH

Let \(s=1/2+iz\).  A nontrivial zeta zero
\[
\rho=\beta+i\gamma
\]
corresponds to a zero of \(\Xi\) at
\[
z_\rho=\gamma-i(\beta-1/2).
\]

Therefore
\[
z_\rho\in\mathbb R
\quad\Longleftrightarrow\quad
\beta=1/2.
\]

Hence
\[
\boxed{
\operatorname{supp}D_{\rm CM}^{\rm norm}\subset\mathbb R
\quad\Longleftrightarrow\quad
\operatorname{supp}\operatorname{div}\Xi\subset\mathbb R
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

This is a clean theorem, but it is an equivalence theorem.  It does not by
itself prove RH.

## 3. Why the existing CM/K facts do not force it

The already-proved ingredients are:

1. \(Z/6\) is the tetrahedral six-edge coordinate system.
2. \(K:r\mapsto-r\pmod6\) is an odd tetrahedral edge reflection.
3. \(\Delta_{\rm CM}(F_c)=\Xi{\mathcal A}_B\).
4. The normalized log derivative equals \(m_B=-\Xi'/\Xi\).
5. The finite-dimensional Cayley-Menger Hessian gives a positive shape metric
   after the scale direction is removed.

These facts are not enough to force boundary support.  The reason is that the
factorization is algebraic in the denominator channel.  If one replaces
\(\Xi\) by a real-even \(K\)-symmetric fake denominator with an off-boundary
quartet of zeros, the same normalized CM divisor construction produces that
off-boundary divisor.

For example,
\[
X_{\gamma,\delta}(z)
=
\big((z-\gamma)^2+\delta^2\big)
\big((z+\gamma)^2+\delta^2\big)
\]
is real entire and even.  Its zeros are
\[
\gamma\pm i\delta,\qquad -\gamma\pm i\delta.
\]
The quartet is \(K\)-symmetric, but not \(K\)-fixed.

Using the same formal Cayley-Menger transfer
\[
{\mathcal C}_{\rm fake}=X_{\gamma,\delta}{\mathcal A}_{\rm fake},
\qquad
{\mathcal T}_{\rm fake}
={{\mathcal C}_{\rm fake}\over{\mathcal A}_{\rm fake}}
=X_{\gamma,\delta},
\]
the normalized divisor has support away from the real boundary.

So the CM factorization proves that the Bures divisor is the correct one.  It
does not prove that the divisor is boundary-supported.

## 4. Pick positivity is the missing positive law

For a real entire denominator \(X\), define
\[
m_X(z)=-{X'(z)\over X(z)}.
\]
If \(X\) has a zero \(a=\gamma+i\delta\) in \(\mathbb C_+\), then \(m_X\) has
an interior pole there.  A Herglotz/Pick function cannot have such a pole.
Indeed, near the pole,
\[
m_X(z)\sim -{1\over z-a}.
\]
Taking \(z=a-i\varepsilon\), with \(0<\varepsilon<\delta\), gives
\[
m_X(z)\sim -{1\over -i\varepsilon}
=
-{i\over\varepsilon},
\]
so
\[
\operatorname{Im}m_X(z)<0.
\]
Consequently
\[
P_X(z,z)
=
{\operatorname{Im}m_X(z)\over\operatorname{Im}z}
<0.
\]

Thus the exact missing law is not more \(K\)-symmetry.  It is positivity:
\[
\boxed{
P_{\rm CM}(z,w)
=
{m_{\rm CM}(z)-\overline{m_{\rm CM}(w)}\over z-\bar w}
\succeq0.
}
\]

Since \(m_{\rm CM}=m_B\), this is exactly the Bures Pick positivity law.

## 5. What a real proof must add

To prove normalized CM boundary support unconditionally, we must prove one of
the following without using RH:

1. **Cayley-Menger Pick law**
   \[
   P_{\rm CM}\succeq0
   \quad\text{on }\mathbb C_+.
   \]

2. **Cayley-Menger Hermite-Biehler law**
   \[
   E_{\rm CM}(z):=\Xi(z)+i\Xi'(z)
   \quad\text{is Hermite-Biehler,}
   \]
   derived from the CM/Bures edge geometry rather than asserted.

3. **CM canonical-system law**: construct a positive Hamiltonian
   \(H_{\rm CM}(t)\succeq0\) whose Weyl \(m\)-function is
   \[
   m_{\rm CM}=-\Xi'/\Xi.
   \]

4. **Boundary current law**
   \[
   D_{\rm CM}^{\rm norm}\restriction_{\mathbb C_+}=0
   \]
   by a direct current/maximum-principle argument for the normalized
   Cayley-Menger transfer.

All four are equivalent in strength to the RH step.  The fake off-boundary
model shows why the current package of algebraic identities does not decide
which one is true.

## 6. Final status

What is proved here:

\[
\boxed{
D_{\rm CM}^{\rm norm}
\text{ has boundary support only}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

What is not yet proved:

\[
\boxed{
D_{\rm CM}^{\rm norm}
\text{ has boundary support only.}
}
\]

The next non-circular target is therefore not another factorization.  It is
the positive CM/Bures Gram law:
\[
\boxed{
P_{\rm CM}=P_B
\text{ is a Gram kernel for positive K-covariant CM edge states.}
}
\]

