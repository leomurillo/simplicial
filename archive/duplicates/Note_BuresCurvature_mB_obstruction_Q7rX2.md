# Note: Bures Curvature Versus the Log-Derivative Density

Date: 2026-05-22  
Mission: derive whether `Im m_B(z)` is a positive Bures/K-covariant norm or
curvature density using the exact `Z/6` decomposition

$$
F(s)=\zeta(s)E(s)+L(s,\chi_3)O(s).
$$

## Verdict

There is a canonical positive Bures/K-covariant curvature density attached to
the exact two-channel `Z/6` packet, but it is **not**

$$
\operatorname{Im} m_B(z).
$$

The positive density is the projective Bures/Fubini-Study curvature of the
even/odd packet:

$$
\kappa_B(z)
=
\frac{\|V\|_B^2\|D_zV\|_B^2-|\langle V,D_zV\rangle_B|^2}{\|V\|_B^4}
\ge 0.
$$

In the orthonormal two-channel reduction this becomes

$$
\kappa_{EO}(z)
=
\frac{|\Xi(z)\mathcal L_3'(z)-\mathcal L_3(z)\Xi'(z)|^2}
{\bigl(|\Xi(z)|^2+|\mathcal L_3(z)|^2\bigr)^2}
=
\frac{|M'(z)|^2}{(1+|M(z)|^2)^2}
\ge 0,
$$

where

$$
\Xi(z)=\xi\left(\frac12+iz\right),\qquad
\mathcal L_3(z)=\Lambda_3\left(\frac12+iz\right),\qquad
M(z)=\frac{\mathcal L_3(z)}{\Xi(z)}.
$$

The Bures log-derivative object found in the previous note is instead

$$
\boxed{
m_B(z)
=
\frac{d}{dz}\log\frac{\mathcal L_3(z)}{\Xi(z)}
-
\frac{d}{dz}\log\mathcal L_3(z)
=
-\frac{\Xi'(z)}{\Xi(z)}.
}
$$

Thus

$$
\operatorname{Im}m_B(z)
=
-\operatorname{Im}\frac{\Xi'(z)}{\Xi(z)}
=
\partial_y\log|\Xi(x+iy)|.
$$

This is a divisor/Poisson density, not a regular Bures curvature density.

## Exact `Z/6` Even/Odd Decomposition

Let

$$
a=2^{-s},\qquad b=3^{-s},\qquad L_3(s)=L(s,\chi_3),
$$

and let

$$
F_r(s)=6^{-s}\zeta\left(s,\frac r6\right)
$$

for the residue packet, with `r=0` denoting the multiples-of-six packet. Then

$$
F(s)=\zeta(s)E(s)+L_3(s)O(s),
$$

where

$$
\begin{aligned}
E(s)
&=
ab|0\rangle
+\frac12(1-a)(1-b)(|1\rangle+|5\rangle)
+\frac12a(1-b)(|2\rangle+|4\rangle)
+b(1-a)|3\rangle,\\
O(s)
&=
\frac12(1+a)(|1\rangle-|5\rangle)
+\frac12a(|2\rangle-|4\rangle).
\end{aligned}
$$

The anti-unitary `K` acts by

$$
K|r\rangle=|-r\bmod 6\rangle,\qquad K(c|r\rangle)=\bar c|-r\bmod 6\rangle.
$$

Accordingly the packet has a K-even channel and a K-odd channel:

$$
K E(z)=E^\#(z),\qquad K O(z)=-O^\#(z),
$$

with the usual real-entire involution

$$
f^\#(z)=\overline{f(\bar z)}.
$$

After completion, the same packet can be written as

$$
V(z)=\Xi(z)e(z)+\mathcal L_3(z)o(z),
$$

where `e,o` are the corresponding gamma/conductor-renormalized `E,O`
vectors. These renormalizations are smooth and nonzero in the region used for
the spectral test, so they cannot create or remove the zeta-divisor pole of
`m_B`.

## The Positive Bures/K Curvature

Let `h_B` be the Bures Hermitian form on the `Z/6` envelope, transported
through the K-covariant completion. Let `D_z` be its Chern/Bures covariant
derivative. The line `[V(z)]` has projective Bures curvature

$$
\boxed{
\kappa_B(z)
=
\frac{\|V\|_B^2\|D_zV\|_B^2
-|\langle V,D_zV\rangle_B|^2}{\|V\|_B^4}
=
\frac{\|P_{V^\perp}D_zV\|_B^2}{\|V\|_B^2}
\ge 0.
}
$$

This expression is K-covariant because `K` is anti-unitary and preserves the
Bures form:

$$
\|KV\|_B=\|V\|_B,\qquad
\langle KU,KV\rangle_B=\overline{\langle U,V\rangle_B}.
$$

In a local K-adapted orthonormal frame for the two channels, this reduces to

$$
\boxed{
\kappa_{EO}(z)
=
\frac{|\Xi\mathcal L_3'-\mathcal L_3\Xi'|^2}
{(|\Xi|^2+|\mathcal L_3|^2)^2}
=
\frac{|M'|^2}{(1+|M|^2)^2}
\ge0.
}
$$

So the exact decomposition does give a positive Bures/K density. It measures
the angular motion of the even/odd line in the Bures envelope.

## Why This Cannot Equal \(\operatorname{Im}m_B\)

The obstruction is local and structural.

Suppose `gamma` is a zeta-zero ordinate with

$$
\Xi(\gamma)=0,\qquad \mathcal L_3(\gamma)\ne0.
$$

Then the completed packet is not zero:

$$
V(\gamma)=\mathcal L_3(\gamma)o(\gamma)\ne0.
$$

Any regular Bures/K projective norm or curvature built from `V`, `D_zV`, and a
smooth positive Hermitian metric therefore remains finite near `gamma`.
Indeed, in the two-channel reduction,

$$
\kappa_{EO}(\gamma)
=
\frac{|\mathcal L_3(\gamma)\Xi'(\gamma)|^2}{|\mathcal L_3(\gamma)|^4}
=
\frac{|\Xi'(\gamma)|^2}{|\mathcal L_3(\gamma)|^2}
<\infty
$$

for a simple zero; higher multiplicity still gives algebraic behavior
incompatible with the Herglotz pole below.

But

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}.
$$

If `gamma` is a zero of multiplicity `m`, then

$$
\Xi(z)=(z-\gamma)^m g(z),\qquad g(\gamma)\ne0,
$$

and hence

$$
m_B(z)=-\frac{m}{z-\gamma}-\frac{g'(z)}{g(z)}.
$$

Approaching from the upper half-plane,

$$
z=\gamma+iy,\qquad y>0,
$$

gives

$$
\boxed{
\operatorname{Im}m_B(\gamma+iy)
=
\frac{m}{y}+O(1)
\longrightarrow +\infty.
}
$$

A finite Bures/K projective curvature cannot equal a quantity with this
Herglotz pole. Therefore

$$
\boxed{
\operatorname{Im}m_B
\ne
\text{a regular positive Bures/K norm or curvature density of }F.
}
$$

This is not a failure of positivity. It says the positive Bures curvature and
the Hilbert-Polya Weyl density are different layers of the same packet.

## The Correct Positive Representation

If RH holds, all zeros of `Xi` are real. Then the log derivative has the
Stieltjes expansion

$$
m_B(z)
=
\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z},
\qquad z\in\mathbb C_+,
$$

where `Gamma` is the symmetric real zeta-zero spectrum. Consequently

$$
\boxed{
\operatorname{Im}m_B(x+iy)
=
\sum_{\gamma\in\Gamma}
m_\gamma
\frac{y}{(x-\gamma)^2+y^2}
}
$$

is positive. This is the Poisson extension of the zero-counting divisor
measure

$$
d\mu_\Xi=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma.
$$

Equivalently,

$$
\operatorname{Im}m_B(x+iy)=\pi\,P_y*d\mu_\Xi(x)
$$

up to the convention for the Poisson kernel.

So the exact answer is:

1. **Regular Bures/K curvature:** yes, positive, explicit, covariant:
   `kappa_B >= 0`.
2. **Equality with `Im m_B`:** no, because `Im m_B` has zeta-divisor
   Herglotz poles while regular Bures projective curvature stays finite where
   the odd channel is nonzero.
3. **Positive representation of `Im m_B`:** yes, but only as the singular
   divisor/Poisson density of the denominator line `Xi`; this representation
   is equivalent to RH.

## Implication for the RH Mission

The Bures packet supplies the correct covariant subtraction:

$$
d\log(\mathcal L_3/\Xi)-d\log\mathcal L_3=-d\log\Xi.
$$

That isolates the zeta divisor exactly. But the final positivity needed for
Hilbert-Polya is not the smooth Bures curvature of the finite `Z/6` packet.
The remaining target is sharper:

$$
\boxed{
\text{Prove the singular divisor density }
\operatorname{Im}\left(-\frac{\Xi'}{\Xi}\right)
\text{ is positive on }\mathbb C_+.
}
$$

That statement is precisely the Herglotz form of RH. The Bures/K geometry gives
the correct object and a positive auxiliary curvature, but it does not by
itself convert the zeta divisor into a regular positive norm.

