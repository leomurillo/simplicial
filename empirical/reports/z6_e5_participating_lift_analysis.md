# Z6 E5 Participating Lift Analysis

Question: can a continuum/Bures or mass-participating lift derive the extra
suppression and body-removal behavior required by the E5 ephemeris gate?

## Candidate Participation Scalars

The minimal symmetric mass participation factor is
\[
  \mu_3(m)
  =
  {27m_1m_2m_3\over (m_1+m_2+m_3)^3}.
\]
It is dimensionless, homogeneous of degree zero, normalized to \(1\) for equal
masses, and vanishes linearly when any body is removed.

The minimal symmetric scale-free shape participation factor is the normalized
Heron quality
\[
  Q(s)
  =
  {432A^2\over (s_{12}+s_{23}+s_{31})^4}
  =
  {27\,\mathrm{area16}(s)\over (s_{12}+s_{23}+s_{31})^4}.
\]
It is \(1\) at the equilateral shape and vanishes on the collinear/dyadic
boundary.  The tested physical lift multiplies the finite-row E5 acceleration
by one of \(1,\mu_3,Q,\mu_3Q^p\).

## Body-Removal Test

For equal-side geometry with masses \((1,1,\epsilon)\), the unscaled relative
correction behaves as follows:

| lift | \(\epsilon=1\) | \(\epsilon=10^{-2}\) | \(\epsilon=10^{-6}\) | \(\epsilon=10^{-9}\) |
|---|---:|---:|---:|---:|
| none | \(1.6432\times10^{-3}\) | \(5.5307\times10^{-4}\) | \(2.3439\times10^{-4}\) | \(2.3433\times10^{-4}\) |
| mass | \(1.6432\times10^{-3}\) | \(1.8389\times10^{-5}\) | \(7.9105\times10^{-10}\) | \(7.9087\times10^{-13}\) |
| shape | \(1.6432\times10^{-3}\) | \(5.5307\times10^{-4}\) | \(2.3439\times10^{-4}\) | \(2.3433\times10^{-4}\) |
| mass_shape | \(1.6432\times10^{-3}\) | \(1.8389\times10^{-5}\) | \(7.9105\times10^{-10}\) | \(7.9087\times10^{-13}\) |

Mass participation therefore solves the body-removal boundary.  Shape
participation alone cannot, because equal-side shape does not see the missing
mass.

## Ephemeris Gate Results

All runs used the same E5 discriminator with \(\lambda_{\rm E5}\) fixed from
the weak-field ephemeris cap.

| lift | status | \(\lambda_{\rm E5}\) | dyadic max | controlled min signal | ephemeris max position | ephemeris max velocity |
|---|---|---:|---:|---:|---:|---:|
| none | KILL | \(7.4844\times10^{-11}\) | \(3.2087\times10^{-13}\) | \(2.2743\times10^{-14}\) | \(1.3643\times10^{-9}\) | \(3.7262\times10^{-9}\) |
| mass | KILL | \(2.3317\times10^{-3}\) | \(9.9962\times10^{-6}\) | \(7.0853\times10^{-7}\) | \(3.7898\times10^{-4}\) | \(4.9471\times10^{-4}\) |
| mass_shape, \(p=1\) | KILL | \(4.8776\times10^{-3}\) | \(3.4936\times10^{-9}\) | \(1.4748\times10^{-6}\) | \(7.9278\times10^{-4}\) | \(1.0347\times10^{-3}\) |
| mass_shape, \(p=2\) | KILL | \(1.0203\times10^{-2}\) | \(4.7479\times10^{-12}\) | \(3.0699\times10^{-6}\) | \(1.6572\times10^{-3}\) | \(2.1623\times10^{-3}\) |

Mass participation restores the controlled signal but fails the dyadic
far-body boundary.  Multiplying by Heron participation fixes the dyadic
far-body boundary, but the ephemeris replay residual still fails.

## Feasibility Intervals

Treating the measured residuals locally as linear in \(\lambda_{\rm E5}\), the
controlled signal floor gives a lower bound and the ephemeris velocity residual
gives an upper bound:

| lift | signal lower bound | velocity-residual upper bound | gap |
|---|---:|---:|---:|
| none | \(3.2909\times10^{-9}\) | \(2.0086\times10^{-12}\) | \(1.6384\times10^3\) |
| mass | \(3.2909\times10^{-9}\) | \(4.7132\times10^{-10}\) | \(6.9822\) |
| mass_shape, \(p=1\) | \(3.3072\times10^{-9}\) | \(4.7140\times10^{-10}\) | \(7.0157\) |
| mass_shape, \(p=2\) | \(3.3236\times10^{-9}\) | \(4.7187\times10^{-10}\) | \(7.0434\) |

Thus mass/shape participation narrows the original contradiction by more than
two orders of magnitude, but does not close it.  No tested scalar lift of the
form \(\mu_3Q^p\,a_{E5}\) has a nonempty \(\lambda_{\rm E5}\) interval satisfying
both controlled signal and ephemeris residual constraints.

## Bures Reading

The Bures/density-matrix lift can justify a richer ambient completion: Bures
restricts to Fisher on the diagonal and supplies noncommuting/off-diagonal
directions that the real simplex cannot carry.  By itself, however, Bures does
not know the external body masses or the weak-field speed-of-light scale.  A
mass-blind Bures lift would inherit the body-removal failure of the mass-blind
finite-row lift.

Therefore the only viable continuation is not "Bures instead of participation"
but a Bures/continuum map whose physical embedding derives a participation
scalar and an additional weak-field or dynamical suppression factor.  The
minimal participation scalar \(\mu_3Q^p\) is necessary for boundary behavior,
but the E5 ephemeris residual shows it is not sufficient.

## Dynamical Suppression Candidate

A natural finite-row dynamical response law is a shape-flow band-pass.  Let
\[
  \nu=\|\dot\sigma\|,
  \qquad
  \nu_*=\|(0.04,-0.02,0.015)\|,
\]
where \(\nu_*\) is the predeclared controlled shape velocity.  The symmetric
finite-row response window
\[
  B(\nu)
  =
  {4(\nu/\nu_*)^2\over\left(1+(\nu/\nu_*)^2\right)^2}
\]
has \(B(\nu_*)=1\), suppresses adiabatic shape drift as \(\nu^2\), and
suppresses rapidly averaged Keplerian shape phase as \(\nu^{-2}\).  It is the
simplest dynamical law with those three properties.

Tested lift:
\[
  a_{E5}^{\rm phys}=\lambda_{\rm E5}\,\mu_3Q\,B(\|\dot\sigma\|)\,a_{E5}.
\]

With \(\lambda_{\rm E5}\) still fixed by the weak-field ephemeris cap, this
returns KILL.  The weak-field calibrator drives
\(\lambda_{\rm E5}\approx2.12\times10^4\), so tiny numerical shape drift in
the synthetic Lagrange orbit wakes up catastrophically:

| lift | status | \(\lambda_{\rm E5}\) | controlled min signal | max ephemeris position | max ephemeris velocity |
|---|---|---:|---:|---:|---:|
| \(\mu_3QB\) | KILL | \(2.1215\times10^4\) | \(6.4147\) | \(1.1696\times10^7\) | \(2.0003\times10^6\) |

This is not a viable physical law under the same parameter-fixing protocol.
The failure is diagnostic: a dynamical response window can suppress fast
weak-field phases, but without an independently derived amplitude scale it
allows weak-field calibration to inflate \(\lambda_{\rm E5}\) and destabilize
near-equilateral conservative orbits.

## Verdict

The current finite-row E5 bridge can be upgraded to satisfy body-removal and
dyadic-boundary behavior by a principled mass-shape participation factor.
That upgrade still fails the full ephemeris discriminator.  The remaining
missing piece cannot be just a scalar response window.  A successful law must
derive both:

1. a participation factor such as \(\mu_3Q^p\), and
2. an independent weak-field amplitude scale, presumably from a continuum
   mass-energy/Bures embedding with a speed-of-light or Jacobi-energy scale.

Without that second scale, weak-field calibration simply reabsorbs the
suppression into \(\lambda_{\rm E5}\).
