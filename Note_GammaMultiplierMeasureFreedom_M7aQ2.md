# Gamma Multiplier vs Divisor Measure

Random suffix: `M7aQ2`

Source hint:
`C:\Projects\simplicial\AttentionSinksSatisfyArchimedeanGammaLaw\AttentionSinksSatisfyArchimedeanGammaLaw.md`

Mission: use the attention-sinks Archimedean gamma paper as a theorem schema
for the CM/Bures metaplectic selection problem.

Verdict: the paper supplies a real theorem schema, but it also proves why the
gamma phase alone cannot close RH.  The gamma multiplier is unique once the
infinite-place packet is assumed; the positive spectral measure on that packet
is still free.  RH needs the measure-selection theorem, not just the
multiplier-selection theorem.

## 1. The transferable theorem

The attention-sinks paper's load-bearing analytic statement is its
Archimedean multiplier theorem:

Let
\[
{\mathcal H}_\infty=L^2(\mathbb R,d\mu)
\]
with \(d\mu\) an even positive height measure.  Let an involution act on the
height basis by
\[
\iota(\psi_t)=c(t)\psi_{-t}.
\]

If:

1. \(\iota\) reflects height \(t\mapsto -t\);
2. \(\iota\) is norm-preserving;
3. the completed wavefunction
   \[
   \Gamma_{\mathbb R}(1/2+it)\tilde\psi(t)
   \]
   is compatible with the functional-equation reflection;

then
\[
\boxed{
c(t)=
{\Gamma_{\mathbb R}(1/2+it)\over
\Gamma_{\mathbb R}(1/2-it)}
=
e^{2i\theta(t)}.
}
\]

This is directly usable.  It says the Archimedean phase is not adjustable.
Under the standard infinite-place assumptions, the Riemann-Siegel phase is
forced.

## 2. Translation to the CM/Bures program

Our finite layer has already found
\[
{\mathcal T}_{\rm CM}(z)
=
{{\mathcal C}_B(z)\over{\mathcal A}_B(z)}
=
\Xi(z).
\]

The infinite Hilbert step requires an Archimedean packet
\[
{\mathcal H}_{\rm CM}^{\infty}
=
L^2(\mathbb R,d\mu_{\rm CM})
\]
and a canonical involution
\[
\iota(\psi_t)=\gamma(t)\psi_{-t},
\qquad
\gamma(t)=e^{2i\theta(t)}.
\]

The attention-sink theorem proves that, if this packet has the standard
completed-zeta functional-equation compatibility, then the multiplier must be
\(\gamma(t)\).  Good: the phase is uniquely selected.

But the theorem does not determine \(d\mu_{\rm CM}\).

## 3. Measure freedom

For every even positive measure \(d\mu(t)=d\mu(-t)\), the operator
\[
(\iota f)(t)=\gamma(t)f(-t)
\]
is unitary on \(L^2(\mathbb R,d\mu)\), because
\[
|\gamma(t)|=1
\]
and the measure is even:
\[
\int |(\iota f)(t)|^2\,d\mu(t)
=
\int |f(-t)|^2\,d\mu(t)
=
\int |f(t)|^2\,d\mu(t).
\]

Thus gamma compatibility fixes the phase but leaves the spectral measure
undetermined.

Examples of allowed even positive measures:

1. Gaussian continuous measure \(e^{-t^2}dt\).
2. Cauchy continuous measure \((1+t^2)^{-1}dt\).
3. Arbitrary symmetric finite atoms \(\sum_k a_k(\delta_{\lambda_k}+
   \delta_{-\lambda_k})\).
4. The desired divisor measure
   \[
   \sum_{\Xi(\gamma)=0}m_\gamma\delta_\gamma.
   \]

All of them admit the same gamma multiplier.  Only the fourth measure carries
the Hilbert-Pólya spectrum.

Therefore:
\[
\boxed{
\text{gamma multiplier selection}\;\not\Rightarrow\;
\text{divisor measure selection}.
}
\]

## 4. The sharpened remaining theorem

The metaplectic CM selection theorem must have two parts.

### Part I: Multiplier selection

The Archimedean \(K\)-involution on the CM/Bures infinite-place packet has
\[
\gamma(t)=e^{2i\theta(t)}.
\]

This part is essentially supplied by the attention-sinks theorem schema.

### Part II: Measure selection

The same structure must select the measure
\[
d\mu_{\rm CM}
=
\operatorname{div}\Xi
\]
as a positive boundary measure:
\[
d\mu_{\rm CM}
=
\sum_{\gamma\in\mathbb R,\;\Xi(\gamma)=0}
m_\gamma\delta_\gamma.
\]

Equivalently,
\[
-{\Xi'(z)\over\Xi(z)}
=
\int_{\mathbb R}{d\mu_{\rm CM}(t)\over t-z}.
\]

This is the actual RH step.

## 5. Corrected theorem target

The next theorem should be named more precisely:

\[
\boxed{
\textbf{Metaplectic CM Measure-Selection Theorem.}
}
\]

It should state:

The finite \(Z/6\) Bures-Cayley edge packet, the normalized CM transfer
\(\Xi\), the unique Archimedean gamma multiplier, and the finite-place
Noether-Weil recovery maps jointly select the positive boundary measure
\[
d\mu_{\rm CM}=\operatorname{div}\Xi
\]
on the real spectral axis.

If this theorem is proved, then
\[
P_B(z,w)
=
\int_{\mathbb R}
{d\mu_{\rm CM}(t)\over(t-z)(t-\bar w)}
\succeq0,
\]
and RH follows.

## 6. What the attention-sinks paper contributes

It contributes:

1. a clean self-contained proof that the gamma multiplier is unique;
2. the distinction between spectral-side unitary height reflection and
   Bures-side antiunitary real structure;
3. a falsifiability template: magnitude \(|\gamma|=1\), phase
   \(2\theta(t)\), and shape rigidity against simpler phase nulls;
4. the critical warning that phase/multiplier data are not measure data.

This is not merely vibe.  It tells us exactly which half of the Archimedean
selection theorem is already structurally understood, and which half remains
the real RH content.

