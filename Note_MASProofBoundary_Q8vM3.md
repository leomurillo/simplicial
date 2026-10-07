# Note: MAS Proof Boundary

Random suffix: `Q8vM3`

Mission: try to prove MAS directly and record the exact mathematical boundary.

Verdict:

\[
\boxed{
\text{MAS cannot be proved from the present Bures/Petz/projective axioms.}
}
\]

This is not a limitation of effort; it is a theorem.  The present axioms have
a model that is not metaplectic.  Therefore no derivation of MAS from those
axioms can be valid.  What can be proved is the exact replacement:

\[
\boxed{
\text{Archimedean symplectic covariance + positive-energy polarization}
\Longleftrightarrow
\text{MAS}.
}
\]

In other words, the missing piece is not another gamma identity.  It is the
antisymmetric Weyl cocycle and the positive-energy complex structure.

## 1. Current Axioms Cannot Imply MAS

Let the current Archimedean axiom package be:

1. projective Bures/Fisher closed-current limit;
2. Bures/Petz metric functoriality;
3. canonical branch reflection \(t\mapsto -t\);
4. gamma multiplier
   \[
   \gamma(t)
   =
   {\Gamma_{\mathbb R}(1/2+it)\over
    \Gamma_{\mathbb R}(1/2-it)};
   \]
5. compatibility with finite recovery and leakage projection.

The even atomic packet
\[
\mu_{\rm at}
=
\delta_0+\sum_{k\ge1}2^{-k}(\delta_k+\delta_{-k})
\]
on
\[
{\mathcal H}_{\rm at}=L^2(\mathbb R,d\mu_{\rm at})
\]
satisfies all five.  The branch reflection
\[
(Uf)(t)=\gamma(t)f(-t)
\]
is unitary and involutive because \(\mu_{\rm at}\) is even and
\(\gamma(t)\gamma(-t)=1\).  Conjugation by \(U\) preserves the Bures metric
on density matrices over \({\mathcal H}_{\rm at}\).

But it cannot support a regular Weyl representation with height as the
position branch.  If \(T f(t)=t f(t)\) and \(V(v)T V(v)^*=T+vI\), then for the
support set \(S=\mathbb Z\),
\[
I=E_T(S)
\quad\Longrightarrow\quad
I=V(1/2)E_T(S)V(1/2)^*
=E_T(S+1/2)=0,
\]
since \(S+1/2\) misses the support.  Contradiction.

Therefore:

\[
\boxed{
\text{current axioms}\not\Rightarrow\text{MAS}.
}
\]

## 2. The Missing Structure

MAS requires data of a different type from Bures metric data.

The Bures/Petz metric supplies a symmetric tensor:
\[
g(X,Y)=g(Y,X).
\]

The Weyl relation requires an antisymmetric two-cocycle:
\[
\omega((u,v),(u',v'))=uv'-vu',
\]
and the multiplier
\[
\sigma((u,v),(u',v'))=e^{\pi i\omega((u,v),(u',v'))}.
\]

No symmetric monotone metric, by itself, determines this cocycle.  The atomic
countermodel realizes the metric and gamma reflection while killing
translation covariance, so the missing datum is exactly symplectic/projective,
not metric.

## 3. Exact Sufficient Replacement

Define the following two additional Archimedean principles.

**ASC (Archimedean Symplectic Covariance).**  
The two closed Cartan branches integrate to a strongly continuous irreducible
projective unitary representation \(W\) of \(\mathbb R^2\) with multiplier
\[
W(u,v)W(u',v')
=
e^{\pi i(uv'-vu')}W(u+u',v+v'),
\]
and the critical branch involution implements the symplectic quarter-turn:
\[
{\mathcal F}W(u,v){\mathcal F}^{-1}=W(v,-u).
\]

**PEP (Positive-Energy Polarization).**  
The Bures completion selects the standard compatible positive complex
structure on this symplectic plane, with number operator \(N\ge0\), cyclic
even ground ray
\[
\psi_0(x)=e^{-\pi x^2},
\]
and first odd ray
\[
\psi_1(x)=x e^{-\pi x^2}.
\]

## 4. Boundary Theorem

**Theorem 4.1 (MAS boundary theorem).**  
Current Bures/Petz/projective axioms plus ASC plus PEP imply MAS.  Conversely,
MAS implies ASC and PEP on the cyclic closed sector.  Hence MAS is exactly
equivalent, over the present axiom package, to adding Archimedean symplectic
covariance and positive-energy polarization.

*Proof.*  Suppose ASC and PEP hold.  ASC gives a regular irreducible Weyl
system with the standard multiplier.  By the Stone-von Neumann theorem, the
cyclic closed sector is unitarily equivalent to the Schrodinger representation
on \(L^2(\mathbb R)\).  The branch involution is the metaplectic Fourier lift
by the second half of ASC.  PEP selects the oscillator complex structure, the
number operator, and the parity split into the even ground and odd first
Hermite rays.  This is precisely MAS.

Conversely, MAS states that the projective Bures completion selects the
regular irreducible Weyl representation with cocycle \(e^{\pi i(uv'-vu')}\),
the metaplectic Fourier branch involution, and the positive-energy oscillator
polarization.  These are exactly ASC and PEP. \(\square\)

## 5. Conditional Gamma Character

Under MAS, the oscillator Mellin character is no longer a hand insertion:
\[
2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-s/2}\Gamma(s/2),
\]
and
\[
2\int_0^\infty x e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-(s+1)/2}\Gamma((s+1)/2).
\]

These are exactly the even and odd Archimedean branches needed by the
completed zeta normalization.

## 6. Final Consequence

There are only two honest ways forward:

1. **Assume MAS/ASC+PEP.**  Then the steelthread is complete:
   \[
   \text{Finite Noether positivity + MAS}
   \Rightarrow
   \mathfrak P_{\phi,y}(\Xi)\ge0
   \Rightarrow
   \mathrm{RH}.
   \]
2. **Prove ASC+PEP from new data.**  The new data must force an antisymmetric
   symplectic cocycle and a positive-energy complex structure.  It cannot be
   only Bures/Petz metric minimality, gamma reflection, or finite/projective
   leakage control, because the atomic packet satisfies those and fails MAS.

Thus a direct proof of MAS from the current corpus would contradict the
countermodel.  The problem is now maximally localized:

\[
\boxed{
\text{Find an internal source of the Archimedean symplectic cocycle and
positive-energy polarization, or declare MAS as the final axiom.}
}
\]
