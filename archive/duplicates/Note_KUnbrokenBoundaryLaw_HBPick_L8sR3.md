# Note: The K-Unbroken Boundary Law for the Bures Divisor Current

Date: 2026-05-22  
Mission: find the missing law that would force boundary support of the Bures
divisor current.

## Verdict

The missing law is the **Bures-Hermite-Biehler / Pick positivity law**:

$$
\boxed{
E_B(z):=\Xi(z)+i\Xi'(z)\ \text{is Hermite-Biehler}.
}
$$

Equivalently, for every `z` in the upper half-plane,

$$
\boxed{
|E_B(z)|>|E_B^\#(z)|,\qquad
E_B^\#(z)=\overline{E_B(\bar z)}=\Xi(z)-i\Xi'(z).
}
$$

This is exactly the K-unbroken boundary-support law in de Branges language.
It is not the failed raw two-channel law

$$
\Xi-i\mathcal L_3.
$$

The Bures/K correction has removed the numerator-channel gauge
`\mathcal L_3`; the boundary law lives on the denominator line and its Bures
covariant derivative.

## The Law in Four Equivalent Forms

Let

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}
$$

and

$$
D_B=-\frac1\pi\partial_{\bar z}m_B.
$$

The following are equivalent for the real entire function `Xi`:

### 1. Boundary support

$$
\boxed{
\operatorname{supp}D_B\subset\mathbb R.
}
$$

Equivalently,

$$
D_B\!\restriction_{\mathbb C_+}=0.
$$

### 2. Herglotz/Nevanlinna property

$$
\boxed{
m_B:\mathbb C_+\to\overline{\mathbb C_+}
}
$$

and `m_B` is analytic on `C_+`.

### 3. Pick kernel positivity

For every finite set `z_1,...,z_N in C_+`,

$$
\boxed{
\left[
\frac{m_B(z_i)-\overline{m_B(z_j)}}{z_i-\overline{z_j}}
\right]_{i,j=1}^N
\succeq 0.
}
$$

At `i=j`, this kernel reduces to

$$
\frac{\operatorname{Im}m_B(z_i)}{\operatorname{Im}z_i}\ge0.
$$

### 4. Hermite-Biehler derivative polarization

Let

$$
A_B(z)=\Xi(z),\qquad B_B(z)=-\Xi'(z).
$$

Then

$$
\frac{B_B(z)}{A_B(z)}=m_B(z).
$$

Define

$$
E_B(z)=A_B(z)-iB_B(z)=\Xi(z)+i\Xi'(z).
$$

The Hermite-Biehler inequality is

$$
\boxed{
|E_B(z)|>|E_B^\#(z)|,\qquad z\in\mathbb C_+.
}
$$

Indeed,

$$
\begin{aligned}
|E_B|^2-|E_B^\#|^2
&=
|\Xi+i\Xi'|^2-|\Xi-i\Xi'|^2\\
&=
4|\Xi|^2\operatorname{Im}\left(-\frac{\Xi'}{\Xi}\right)\\
&=
4|\Xi|^2\operatorname{Im}m_B.
\end{aligned}
$$

So the Hermite-Biehler inequality is exactly the positivity of `Im m_B`.

## Why This Is the Missing K-Unbroken Law

The anti-unitary `K` gives reality:

$$
\Xi^\#=\Xi.
$$

But K-reality alone only says zeros are invariant under reflection across the
real axis. It allows broken pairs

$$
a,\bar a,\qquad \operatorname{Im}a\ne0.
$$

The K-unbroken law is the stronger statement that the K-fixed set captures the
entire divisor:

$$
\operatorname{supp}D_B\subset\operatorname{Fix}(K)=\mathbb R.
$$

Hermite-Biehler/Pick positivity is exactly the analytic form of that stronger
law. In physical PT language:

- K-symmetry: the divisor is reflection-symmetric.
- K-unbroken: the divisor is fixed pointwise by K.

## Relation to Laguerre-Polya

For the completed xi function, the same law can be stated as:

$$
\boxed{
\Xi\in\mathcal{LP},
}
$$

the Laguerre-Polya class of real entire functions obtained as local uniform
limits of real-rooted polynomials.

Since `Xi` is real entire of order one, this is equivalent to all its zeros
being real. Thus:

$$
\boxed{
\Xi\in\mathcal{LP}
\iff
D_B\!\restriction_{\mathbb C_+}=0
\iff
m_B\text{ Herglotz}
\iff
E_B\text{ Hermite-Biehler}
\iff
\text{RH}.
}
$$

This is not yet an independent proof of RH. It is the exact missing law in its
classical analytic form.

## The Bures Version to Prove

The non-circular Bures target is not merely to assert that `E_B` is
Hermite-Biehler. It is to prove the Pick kernel positivity from the `Z/6`
Bures geometry:

$$
\boxed{
\mathsf P_B(z,w)
:=
\frac{m_B(z)-\overline{m_B(w)}}{z-\bar w}
=
\langle \mathcal R_z,\mathcal R_w\rangle_{\mathrm{Bures}/K}
}
$$

for some K-covariant Bures resolvent vectors `R_z`.

If such a Gram representation is proved, then

$$
\mathsf P_B\succeq0
$$

by Bures positivity, hence `m_B` is Herglotz, hence
`D_B` has boundary support, hence RH.

So the missing law is:

$$
\boxed{
\textbf{Bures-Pick Gram Law: }
\mathsf P_B(z,w)
\text{ is the Gram kernel of K-covariant Bures resolvent states.}
}
$$

This is the precise next proof obligation.

## What the Exact `Z/6` Decomposition Contributes

The exact decomposition

$$
F=\zeta E+L_3O
$$

gave the covariant subtraction

$$
d\log(\mathcal L_3/\Xi)-d\log\mathcal L_3=-d\log\Xi.
$$

That means the Bures geometry identifies the correct denominator-line
connection. The missing law asks for one further lift:

$$
-d\log\Xi
\quad\rightsquigarrow\quad
\text{positive Pick/Gram kernel}.
$$

The previous smooth Bures curvature

$$
\frac{|\Xi\mathcal L_3'-\mathcal L_3\Xi'|^2}
{(|\Xi|^2+|\mathcal L_3|^2)^2}
$$

is positive but finite at zeros. The Pick kernel has the correct singular
behavior:

$$
\mathsf P_B(z,z)=\frac{\operatorname{Im}m_B(z)}{\operatorname{Im}z},
$$

and therefore sees divisor atoms.

## Bottom Line

The missing law has been found in its minimal exact form:

$$
\boxed{
E_B(z)=\Xi(z)+i\Xi'(z)\text{ is Hermite-Biehler}
}
$$

or, equivalently,

$$
\boxed{
\left[
\frac{m_B(z_i)-\overline{m_B(z_j)}}{z_i-\overline{z_j}}
\right]\succeq0.
}
$$

The next non-circular mission is to prove this Pick kernel is a genuine
Bures/K Gram kernel coming from the `Z/6` lift.

