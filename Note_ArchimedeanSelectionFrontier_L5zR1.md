# Archimedean Selection Frontier

Random suffix: `L5zR1`

Mission: push the infinite Hilbert step after the \(Z/6\) Bures-Cayley divisor
factorization.

Verdict: the positive Archimedean packet is constructible; the divisor
boundary measure is not produced by that packet alone.  The remaining
non-circular law is exactly the metaplectic/Weyl-CCR positive-energy selection
plus finite-place Weil recovery named in Papers 22, 23, and 27.

## 1. What the finite CM layer now supplies

The finite tetrahedral edge layer gives
\[
{\mathcal C}_B(z):=\Delta_{\rm CM}(F_c(z))
=
\Xi(z){\mathcal A}_B(z),
\]
so
\[
{\mathcal T}_{\rm CM}(z)
:=
{{\mathcal C}_B(z)\over{\mathcal A}_B(z)}
=
\Xi(z).
\]

Thus the \(Z/6\) Bures-Cayley construction identifies the exact normalized
divisor.  It does not, by itself, prove that this divisor is supported on the
real spectral axis.

## 2. What the Archimedean packet supplies

Paper 27 already isolates the required infinite-place packet:

- a continuous height variable \(t\in\mathbb R\);
- an involution \(t\mapsto -t\) with the gamma multiplier;
- a positive spectral measure on the critical line;
- compatibility with the finite projective recovery maps.

Paper 22 supplies the oscillator model for the gamma factor.  The positive
radial measures are
\[
e^{-x}x^{s/2-1}\,dx,
\qquad
e^{-y}y^{(s+1)/2-1}\,dy.
\]

Their Mellin integrals are
\[
\int_0^\infty e^{-x}x^{s/2-1}\,dx=\Gamma(s/2),
\]
\[
\int_0^\infty e^{-y}y^{(s+1)/2-1}\,dy=\Gamma((s+1)/2).
\]

Hence the positive-energy oscillator packet gives
\[
\Gamma(s/2)\Gamma((s+1)/2),
\]
which is the gamma architecture needed by the completed zeta normalization
after the standard powers of \(2\) and \(\pi\) are restored.

This part is positive and non-mysterious.  It is the analytic infinite-place
body that the finite \(Z/6\) carrier was missing.

## 3. Why this still does not prove boundary support

The gamma/oscillator packet completes the functional equation side.  It does
not create the zero divisor measure
\[
d\mu_{\rm CM}
=
\sum_{\Xi(\gamma)=0}m_\gamma\delta_\gamma.
\]

That measure is the divisor of \(\Xi\).  Constructing it as a positive measure
on \(\mathbb R\) is equivalent to proving that all zeros of \(\Xi\) are real.

The Archimedean packet can make
\[
\xi(s)
=
\text{gamma factor}\times \zeta(s)
\]
canonical, symmetric, and \(K\)-covariant.  It cannot by itself move a
hypothetical off-line zero onto the critical line.  That is why Paper 22's
Proposition 5.2.5c is decisive: finite/projective Bures data do not
automatically select the Weyl/CCR positive-energy representation.  The
selection must be added or proved as an Archimedean theorem.

## 4. Three equivalent infinite selection laws

The remaining non-circular law can now be stated in three equivalent forms.

### Law A: CM divisor boundary support

\[
\operatorname{supp}\operatorname{div}
\left({{\mathcal C}_B\over{\mathcal A}_B}\right)
\subset\mathbb R.
\]

Since \({\mathcal C}_B/{\mathcal A}_B=\Xi\), this is RH.

### Law B: Bures-CM Pick positivity

\[
P_B(z,w)
=
{m_B(z)-\overline{m_B(w)}\over z-\bar w}
\succeq0,
\qquad
m_B=-{\Xi'\over\Xi}.
\]

This is the Herglotz/de Branges formulation.

### Law C: Positive canonical system

Construct
\[
H_{\rm CM}(t)\succeq0
\]
so that the Weyl function of
\[
J{dY\over dt}=zH_{\rm CM}(t)Y
\]
is
\[
m_{H_{\rm CM}}(z)=m_B(z).
\]

This is the strongest Hilbert-Pólya version, because positivity of
\(H_{\rm CM}\) forces \(m_B\) Herglotz.

## 5. The role of Weil positivity

The same law is also Weil's explicit-formula positivity:
\[
\mathcal W_\zeta(f)\ge0
\]
for the appropriate test-function class.  Papers 22 and 23 reduce this route
to:

1. finite-place recovery of the von Mangoldt/prime side;
2. projective closure of the finite Noether energies;
3. Archimedean positive-energy selection;
4. identification of the limit with the completed Weil quadratic form.

The Bures-Cayley work strengthens item 3 by identifying the exact finite
internal carrier and normalized divisor.  It does not eliminate items 1, 2,
or 4.

## 6. What is now closed

Closed:

1. \(Z/6\) is the tetrahedral six-edge carrier.
2. Cayley-Menger of the completed packet factors as \(\Xi{\mathcal A}_B\).
3. \(m_B\) is the normalized CM divisor log derivative.
4. The finite six-edge state space cannot equal \(P_B\).
5. The infinite divisor Hilbert space is explicit conditional on boundary
   support.
6. The positive Archimedean gamma packet is the even/odd oscillator Mellin
   packet.

Not closed:

1. Boundary support of the normalized CM divisor.
2. Pick positivity of \(m_B\).
3. Positive canonical-system Hamiltonian for \(m_B\).
4. Weil positivity from finite recovery plus Archimedean limit.

## 7. The exact next theorem to prove

The next theorem is not "find another finite matrix."  It is:

\[
\boxed{
\textbf{Metaplectic CM Selection Theorem.}
}
\]

The theorem should state:

The \(Z/6\) Bures-Cayley edge packet, together with the Archimedean
positive-energy oscillator packet and the canonical \(K\)-involution, selects
a positive canonical-system Hamiltonian \(H_{\rm CM}(t)\succeq0\) whose Weyl
function is
\[
m_B=-{\Xi'\over\Xi}.
\]

Proving this theorem would close the RH route.  The existing program proves
all finite carrier identities needed to state it sharply; the selection theorem
itself remains the infinite analytic heart.

