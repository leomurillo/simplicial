# Note: Metaplectic Archimedean Selection

Random suffix: `Q8vM3`

Mission: test whether the current Bures/Petz/projective closed-current
principles force the Weyl/CCR positive-energy oscillator representation, or
whether the metaplectic positive-energy packet remains an independent
Archimedean axiom.

Verdict:

\[
\boxed{
\text{The metaplectic positive-energy packet is not forced by the current
Bures/Petz/projective data.}
}
\]

The oscillator packet gives exactly the right even/odd gamma characters once
it is selected.  But the present principles fix at most metric geometry,
branch reflection, and the gamma multiplier.  They do not force a nontrivial
CCR cocycle, an irreducible Weyl system, the metaplectic Fourier operator, or
a positive-energy number operator.  Those data remain a representation
selection axiom unless a new Archimedean principle is added.

## 1. What Is Conditionally True

Assume a regular irreducible Weyl representation
\[
W(u,v)W(u',v')
=
e^{\pi i(uv'-vu')}W(u+u',v+v')
\]
on the cyclic closed sector, assume the branch involution is the metaplectic
Fourier lift
\[
\mathcal F W(u,v)\mathcal F^{-1}=W(v,-u),
\]
and assume a positive-energy oscillator polarization with ground ray
\[
\psi_0(x)=e^{-\pi x^2}
\]
and first odd ray
\[
\psi_1(x)=x e^{-\pi x^2}.
\]

Then the radial Mellin characters are
\[
\chi_+(s)=2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\pi^{-s/2}\Gamma(s/2)
\]
and
\[
\chi_-(s)=2\int_0^\infty e^{-\pi x^2}x^s\,dx
=
\pi^{-(s+1)/2}\Gamma((s+1)/2).
\]

This is the correct Archimedean packet.  The gamma integrals are not the
problem.

## 2. Attempted Forcing Routes

### 2.1 Projective Bures closed-current limit forces Weyl/CCR

Refuted from current data.

At finite primorial rows, the Bures lift is finite-dimensional.  Exact CCR
relations
\[
[Q,P]=i\hbar I,\qquad \hbar\ne0,
\]
cannot hold in finite dimension because
\[
\operatorname{Tr}[Q,P]=0
\]
but
\[
\operatorname{Tr}(i\hbar I)=i\hbar\dim H\ne0.
\]

An exact CCR can appear only after an additional limiting construction that
selects unbounded generators and a central two-cocycle.  The current
projective data supply a Bures metric, a symmetric \(A_2\) cubic tensor, and
leakage extinction.  They do not supply the antisymmetric symplectic form
\[
\omega((u,v),(u',v'))=uv'-vu'
\]
or the multiplier
\[
e^{\pi i\omega}.
\]

### 2.2 Critical branch involution forces metaplectic Fourier

Refuted from current data.

The finite/projective involution supplies branch reflection and, after
Archimedean gamma compatibility, the phase
\[
\gamma(t)=
{\Gamma_{\mathbb R}(1/2+it)\over\Gamma_{\mathbb R}(1/2-it)}.
\]
For every even positive measure \(d\mu(t)=d\mu(-t)\), the operator
\[
(Uf)(t)=\gamma(t)f(-t)
\]
is unitary on \(L^2(\mathbb R,d\mu)\).  These Hilbert spaces need not carry a
Weyl representation at all.  Therefore the gamma-reflection involution is
weaker than the metaplectic Fourier transform.  Fourier becomes forced only
after the Weyl/CCR structure has already been selected.

### 2.3 Petz/Bures minimality selects the positive-energy number operator

Refuted from current data.

The Bures metric is the minimal monotone Petz metric and the symmetric
logarithmic derivative metric on density matrices.  This selects a metric
geometry, not a Hamiltonian.  Many Hilbert realizations, direct sums, and
commuting radial models have the same visible Bures/Fisher shadow and the
same branch reflection, but no distinguished number operator \(N\ge0\).

Positive energy is an ordering and polarization statement.  It is not encoded
in the monotone metric alone.

### 2.4 K-involution plus positive cone plus energy bounded below

Insufficient unless "energy" is already part of the data.

The positive cone and \(K\)-reflection constrain the real structure.  They do
not define the generator whose spectrum is to be bounded below.  Adding an
operator \(N\) with spectrum \(\mathbb N\) is precisely the oscillator
selection.

### 2.5 de Branges/canonical-system interpretation

Equivalent to the missing positivity.

If the Archimedean packet selected a positive canonical-system Hamiltonian
\[
H_{\rm CM}(t)\succeq0
\]
with Weyl function
\[
m_B(z)=-{\Xi'(z)\over\Xi(z)},
\]
then \(m_B\) would be Herglotz and the divisor would be boundary-supported.
That is RH in canonical-system language.  It cannot be used as a proof of
selection unless the Hamiltonian is constructed from independent data.

## 3. Concrete Countermodel: Gamma Phase With Free Measure

Let \(\gamma(t)\) be the completed-zeta gamma multiplier on the critical
line.  For any even positive measure \(\mu\), define
\[
U_\mu f(t)=\gamma(t)f(-t)
\]
on \(L^2(\mathbb R,d\mu)\).

Then
\[
\|U_\mu f\|_{L^2(\mu)}^2
=
\int|\gamma(t)|^2|f(-t)|^2\,d\mu(t)
=
\int|f(t)|^2\,d\mu(t),
\]
because \(|\gamma(t)|=1\) and \(\mu\) is even.

Examples:

1. \(d\mu(t)=e^{-t^2}dt\);
2. \(d\mu(t)=(1+t^2)^{-1}dt\);
3. \(d\mu(t)=\sum_k a_k(\delta_{\lambda_k}+\delta_{-\lambda_k})\);
4. the desired divisor measure, if RH is true.

All four admit the same gamma phase and unitary branch reflection.  Only the
fourth is the Hilbert-Polya divisor measure.  Therefore:

\[
\boxed{
\text{gamma multiplier selection does not imply divisor measure selection.}
}
\]

## 4. Independence Statement

**Theorem 4.1 (Metaplectic selection is independent of the current axioms).**  
The following data:

1. finite occupation-decorated von Mangoldt recovery;
2. projective Bures/Fisher metric compatibility;
3. closed-current leakage extinction;
4. \(A_2\) symmetric cubic survival;
5. branch reflection \(t\mapsto -t\);
6. the unique gamma multiplier for that reflection;

do not determine the Weyl/CCR positive-energy oscillator representation, the
metaplectic Fourier branch exchange, or the divisor spectral measure.

*Proof.*  Items 1--4 are finite/projective and metric/symmetric.  They do not
contain an antisymmetric symplectic cocycle.  Finite-dimensional rows cannot
carry an exact CCR by the trace obstruction.  Item 5 plus item 6 can be
realized on \(L^2(\mathbb R,d\mu)\) for every even positive measure \(\mu\),
as shown in Section 3.  Choosing two different measures, for example Gaussian
continuous measure and symmetric atomic measure, gives non-equivalent spectral
packets with the same gamma phase and branch reflection.  At most one can be
the divisor measure of \(\Xi\).  Hence the current axioms do not select the
desired representation or measure. \(\square\)

## 5. Correct Conditional Theorem

The valid theorem is conditional:

**Theorem 5.1 (Metaplectic Archimedean Selection, conditional form).**  
If the projective Bures completion of the surviving \(A_2\) cylinder class is
equipped with:

1. a regular irreducible Weyl representation with cocycle
   \(e^{\pi i(uv'-vu')}\);
2. metaplectic Fourier implementation of the critical branch involution;
3. a positive-energy number operator whose even ground and odd first rays
   map under the Bures diagonal measurement to the radial densities
   \(e^{-\pi x^2}\) and \(x e^{-\pi x^2}\);
4. no unaccounted extra Cartan factor;

then the Archimedean character is
\[
\pi^{-s/2}\Gamma(s/2)
\quad\text{and}\quad
\pi^{-(s+1)/2}\Gamma((s+1)/2)
\]
on the even and odd branches, with product
\[
\pi^{-(2s+1)/2}\Gamma(s/2)\Gamma((s+1)/2).
\]

This theorem attaches correctly to the finite-place occupation recovery, but
the attachment still depends on the representation-selection hypothesis.

## 6. Final Status

Closed:

1. the even/odd oscillator Mellin characters;
2. uniqueness of the gamma multiplier once the infinite-place reflection
   packet is assumed;
3. the no-go showing that current Bures/Petz/projective data do not force the
   Weyl/CCR positive-energy representation.

Open:

1. a new principle that forces the antisymmetric CCR cocycle from the
   projective closed-current limit;
2. a proof that the critical involution is metaplectic Fourier rather than
   mere gamma-reflection on an arbitrary even measure;
3. a proof that Bures/Petz geometry selects the positive-energy number
   operator;
4. measure selection for the CM divisor without assuming boundary support.

Thus the honest lock statement is:

\[
\boxed{
\text{Metaplectic positive-energy selection remains an independent
Archimedean axiom at the current stage.}
}
\]

Addendum Q8vM3 resolution:
`Note_ArchimedeanMetaplecticSelectionResolution_Q8vM3.md` sharpens this into
the final axiom/countermodel statement.  The current Bures/Petz/projective
data plus gamma phase admit an even atomic height packet with Bures-isometric
gamma reflection but no Weyl covariance for the height branch.  Therefore the
unconditional implication to the Weyl/CCR oscillator packet is false for the
present axiom list.  The required additional input is MAS, the Metaplectic
Archimedean Selection Axiom.
