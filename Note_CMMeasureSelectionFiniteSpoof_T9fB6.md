# CM Measure Selection: Finite Spoofing

Random suffix: `T9fB6`

Mission: proceed from gamma multiplier selection to divisor measure selection.

Verdict: finite constraints do not select the Hilbert-Pólya measure.  The
measure-selection theorem must be an infinite/dense trace identity, equivalent
to constructing the positive boundary measure for \(m_B=-\Xi'/\Xi\).

## 1. The problem after gamma selection

The Archimedean gamma law fixes the multiplier:
\[
\iota(\psi_t)=e^{2i\theta(t)}\psi_{-t}.
\]

But every even positive measure \(d\mu(t)=d\mu(-t)\) supports this same unitary
involution.  The missing theorem is therefore not phase selection.  It is
measure selection:
\[
d\mu_{\rm CM}
=
\operatorname{div}\Xi
\quad\text{as a positive boundary measure.}
\]

Equivalently,
\[
m_B(z)=-{\Xi'(z)\over \Xi(z)}
=
\int_{\mathbb R}{d\mu_{\rm CM}(t)\over t-z}.
\]

## 2. Uniqueness if the full transform is known

Suppose \(d\mu\) and \(d\nu\) are positive locally finite measures on
\(\mathbb R\), and
\[
\int_{\mathbb R}{d\mu(t)\over t-z}
=
\int_{\mathbb R}{d\nu(t)\over t-z}
\]
for all \(z\in\mathbb C_+\) in a nonempty open set.  Then
\[
\mu=\nu.
\]

This is the standard Stieltjes/Nevanlinna uniqueness theorem.  The boundary
measure is recovered by the inversion formula
\[
\mu((a,b))
=
\lim_{y\downarrow0}{1\over\pi}
\int_a^b
\operatorname{Im}
\left(
\int_{\mathbb R}{d\mu(t)\over t-(x+iy)}
\right)dx
\]
at continuity intervals.

Therefore, if one proves
\[
-{\Xi'(z)\over\Xi(z)}
=
\int_{\mathbb R}{d\mu_{\rm CM}(t)\over t-z}
\]
with \(d\mu_{\rm CM}\ge0\), then the measure is uniquely forced and RH follows.

## 3. Why finite constraints cannot select the measure

Any finite list of Pick constraints
\[
P_B(z_i,z_j)
=
\int_{\mathbb R}
{d\mu(t)\over(t-z_i)(t-\bar z_j)}
,
\qquad 1\le i,j\le N,
\]
is only a finite system of linear equations on the infinite-dimensional cone
of even positive measures.

Thus finite constraints cannot determine \(d\mu\).  At best they can restrict
it.  There are many positive atomic measures that match or approximate the
same finite Pick data.

Empirically, using four sample points
\[
z\in
\{0.7+0.4i,\;5+0.5i,\;\gamma_1+0.5i,\;\gamma_2+0.5i\},
\]
nonnegative least-squares fits over unrelated symmetric atom grids reproduce
the finite \(P_B\) matrix to small residual.  These measures are positive and
even but are not the Hilbert-Pólya divisor measure.

This proves the operational point:
\[
\boxed{
\text{finite positivity tests can be spoofed by wrong positive measures.}
}
\]

## 4. The correct infinite selection law

The measure-selection theorem must therefore state equality on a dense class,
not finitely many probes.

Equivalent dense formulations:

### A. Cauchy transform identity

\[
\boxed{
-{\Xi'(z)\over\Xi(z)}
=
\int_{\mathbb R}{d\mu_{\rm CM}(t)\over t-z}
\quad
\forall z\in\mathbb C_+.
}
\]

### B. Pick kernel identity

\[
\boxed{
P_B(z,w)
=
\int_{\mathbb R}
{d\mu_{\rm CM}(t)\over(t-z)(t-\bar w)}
\quad
\forall z,w\in\mathbb C_+.
}
\]

### C. Weil trace identity

For a dense Weil test class \({\mathcal S}_W\),
\[
\boxed{
\mathcal W_\zeta(f)
=
\int_{\mathbb R}
|\widehat f(t)|^2\,d\mu_{\rm CM}(t)
\ge0
\quad
\forall f\in{\mathcal S}_W.
}
\]

### D. Canonical-system identity

Construct \(H_{\rm CM}(t)\succeq0\) with Weyl function
\[
\boxed{
m_{H_{\rm CM}}(z)
=
-{\Xi'(z)\over\Xi(z)}.
}
\]

All four are equivalent at the RH-strength level.

## 5. What this changes

The next theorem cannot be a finite verification, a finite Gram fit, or a
finite-rank construction.  It must be a dense spectral identity connecting:

1. finite-place Noether-Weil recovery;
2. the Archimedean gamma multiplier;
3. the normalized CM divisor \(\Delta_{\rm CM}(F_c)/{\mathcal A}_B=\Xi\);
4. a positive boundary measure selected by the full transform.

The theorem target is:

\[
\boxed{
\textbf{Dense CM Measure-Selection Theorem.}
}
\]

It says:

There exists a positive even measure \(d\mu_{\rm CM}\) on \(\mathbb R\), selected
by the \(Z/6\) Bures-Cayley packet plus the Archimedean infinite-place packet,
such that its Cauchy transform is \(m_B=-\Xi'/\Xi\).

Proving this is exactly the remaining Hilbert-Pólya/RH step.

