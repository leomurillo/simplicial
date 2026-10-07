# Note: Off-Line Zeros and the Bures Divisor Current

Date: 2026-05-22  
Mission: prove the off-line zero contradiction in the Bures divisor current.

## Verdict

The contradiction is exact, but it requires the precise boundary-support
principle:

$$
\boxed{
D_B\!\restriction_{\mathbb C_+}=0
}
$$

or equivalently that

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}
$$

is a Herglotz/Weyl function analytic on the upper half-plane.

Under that principle, an off-line zero is impossible. The proof is a one-line
divisor-current test: an off-line zero forces a positive atom of `D_B` inside
the spectral upper half-plane, while the boundary-support principle says there
can be no interior atom.

What is not proved by this current calculation alone is the boundary-support
principle itself. K-covariance alone gives symmetry of the interior atoms, not
their absence. This is the exact remaining bridge.

## Setup

Use the spectral coordinate

$$
s=\frac12+iz,\qquad z=x+iy.
$$

Then

$$
\Xi(z)=\xi\left(\frac12+iz\right)
$$

is even and real entire:

$$
\Xi(-z)=\Xi(z),\qquad \Xi^\#=\Xi,\qquad
\Xi^\#(z)=\overline{\Xi(\bar z)}.
$$

The Bures-covariant log derivative found from the exact `Z/6` decomposition

$$
F=\zeta E+L(s,\chi_3)O
$$

is

$$
\boxed{
m_B(z)
=
d\log(\mathcal L_3/\Xi)-d\log\mathcal L_3
=
-\frac{\Xi'(z)}{\Xi(z)}.
}
$$

Define the Bures divisor current by the sign convention

$$
\boxed{
D_B:=-\frac1\pi\partial_{\bar z}m_B.
}
$$

Since

$$
\partial_{\bar z}\frac1{z-a}=\pi\delta_a,
$$

and near a zero `a` of multiplicity `m_a`,

$$
m_B(z)=-\frac{m_a}{z-a}+\text{holomorphic},
$$

we get the exact divisor-current identity

$$
\boxed{
D_B=\sum_{\Xi(a)=0}m_a\delta_a.
}
$$

This identity is unconditional.

## Off-Line Zero Cluster in Spectral Coordinates

Assume an off-line zeta zero

$$
\rho_+=\frac12+\delta+i\gamma,\qquad \delta>0.
$$

The functional equation and conjugation force the four-zero cluster

$$
\rho_\pm=\frac12\pm\delta+i\gamma,\qquad
\bar\rho_\pm=\frac12\pm\delta-i\gamma.
$$

Under

$$
s=\frac12+iz,
$$

these become the four spectral zeros

$$
\boxed{
z=\gamma-i\delta,\quad \gamma+i\delta,\quad
-\gamma-i\delta,\quad -\gamma+i\delta.
}
$$

Thus every off-line FE cluster places two zeros of `Xi` inside the spectral
upper half-plane:

$$
\gamma+i\delta,\qquad -\gamma+i\delta.
$$

Therefore

$$
\boxed{
D_B\!\restriction_{\mathbb C_+}
\ge
m_{\gamma+i\delta}\delta_{\gamma+i\delta}
+
m_{-\gamma+i\delta}\delta_{-\gamma+i\delta}.
}
$$

In particular, if `phi >= 0` is a smooth compactly supported test function
inside a tiny disk around `a=gamma+i delta`, with `phi(a)>0`, then

$$
\langle D_B,\phi\rangle
=
m_a\phi(a)>0.
$$

## Boundary-Support Contradiction

The Herglotz/de Branges/Weyl form of the Hilbert-Polya target says that
`m_B` is analytic on `C_+` with positive imaginary part. In current language,
all spectral measure must live on the K-fixed boundary `R`, so

$$
D_B\!\restriction_{\mathbb C_+}=0.
$$

But the off-line cluster gives, for the same test function `phi`,

$$
\langle D_B,\phi\rangle=m_a\phi(a)>0.
$$

Contradiction.

So:

$$
\boxed{
D_B\!\restriction_{\mathbb C_+}=0
\quad\Longrightarrow\quad
\text{no off-line zeta zero}.
}
$$

Since any off-line zero has a functional-equation partner that enters
`C_+`, this is equivalent to RH:

$$
\boxed{
D_B\!\restriction_{\mathbb C_+}=0
\iff
\text{RH}.
}
$$

Equivalently:

$$
\boxed{
m_B=-\Xi'/\Xi\text{ is Herglotz on }\mathbb C_+
\iff
\text{RH}.
}
$$

## What K-Covariance Gives and Does Not Give

K-covariance gives

$$
K_*D_B=D_B,
$$

because `Xi` is real entire and the zero set is invariant under conjugation.
For an off-line cluster, this means the upper atom at `gamma+i delta` is paired
with the lower atom at `gamma-i delta`, and similarly at `-gamma`.

But that symmetry is not a contradiction. A positive K-invariant divisor current
may have interior atoms:

$$
\delta_{\gamma+i\delta}+\delta_{\gamma-i\delta}
$$

is perfectly positive and K-invariant.

Therefore the missing law is not K-covariance. The missing law is
**K-unbroken boundary support**:

$$
\operatorname{supp}D_B\subset\mathbb R.
$$

That is exactly the same content as the desired Hilbert-Polya
self-adjointness/Herglotz property.

## Relation to the Cubic Bombieri Witness

The cubic Bombieri witness in `diez.md` detects the same off-line cluster in a
smeared third-order language. For a hypothetical

$$
\rho_0=\frac12+\delta+i\gamma_0,
$$

the FE cluster produces a negative second-order correction

$$
\operatorname{Re}\mathcal C_\zeta(g_0;\eta_0)
=
\operatorname{Re}\mathcal C_\Lambda^{(0)}(g_0;\eta_0)
+c_2\delta^2+o(\delta^2),
\qquad c_2<0.
$$

The divisor-current language says the same geometric thing more locally:
the off-line cluster creates interior spectral atoms at

$$
\pm\gamma_0+i\delta.
$$

If cubic positivity is identified with the boundary-support law

$$
D_B\!\restriction_{\mathbb C_+}=0,
$$

then the off-line contradiction is immediate and complete. Without that
identification, the current calculation gives a sharp equivalent form of RH,
not an unconditional proof.

## Status

Proved:

1. The Bures divisor current is exactly the `Xi` divisor:

   $$
   D_B=\sum_{\Xi(a)=0}m_a\delta_a.
   $$

2. Every off-line zero forces positive interior current in `C_+`.

3. Any Bures boundary-support/Herglotz principle contradicts that interior
   current and therefore proves RH.

Not proved here:

1. The boundary-support/Herglotz principle itself.
2. The identification of cubic positivity with that boundary-support law.

So the next exact target is:

$$
\boxed{
\text{prove from the cubic/Bures machinery that }
D_B\!\restriction_{\mathbb C_+}=0.
}
$$

