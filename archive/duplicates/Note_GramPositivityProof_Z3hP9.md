# Note: Positivity of the Bures Pick Gram Formula

Date: 2026-05-22  
Mission: prove positivity of the Gram formula for

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}.
$$

## Result

The Gram formula's positivity is proved **exactly under K-unbroken boundary
support**:

$$
\operatorname{supp}D_B\subset\mathbb R.
$$

Without that boundary-support law, the desired positivity is not a smaller
lemma: it is equivalent to RH.

So the strongest honest theorem is:

$$
\boxed{
\mathsf P_B\succeq0\text{ on }\mathbb C_+
\iff
m_B\text{ is Herglotz}
\iff
\operatorname{supp}D_B\subset\mathbb R
\iff
\mathrm{RH}.
}
$$

## Proof of Positivity Under Boundary Support

Assume the Bures divisor current is K-unbroken:

$$
D_B=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma,
\qquad \Gamma\subset\mathbb R,\quad m_\gamma\in\mathbb N.
$$

Then

$$
m_B(z)=\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z}
$$

locally uniformly in the spectral upper half-plane. Hence

$$
\begin{aligned}
\mathsf P_B(z,w)
&=
\frac{m_B(z)-\overline{m_B(w)}}{z-\bar w}\\
&=
\sum_{\gamma\in\Gamma}
m_\gamma
\frac{(\gamma-z)^{-1}-(\gamma-\bar w)^{-1}}
{z-\bar w}\\
&=
\sum_{\gamma\in\Gamma}
\frac{m_\gamma}{(\gamma-z)(\gamma-\bar w)}.
\end{aligned}
$$

Now take any finite set

$$
z_1,\ldots,z_N\in\mathbb C_+
$$

and coefficients

$$
c_1,\ldots,c_N\in\mathbb C.
$$

Then

$$
\begin{aligned}
\sum_{i,j=1}^N c_i\overline{c_j}\mathsf P_B(z_i,z_j)
&=
\sum_{\gamma\in\Gamma}m_\gamma
\sum_{i,j}
\frac{c_i\overline{c_j}}
{(\gamma-z_i)(\gamma-\overline{z_j})}\\
&=
\sum_{\gamma\in\Gamma}m_\gamma
\left|
\sum_{i=1}^N\frac{c_i}{\gamma-z_i}
\right|^2\\
&\ge0.
\end{aligned}
$$

Thus

$$
\boxed{
\mathsf P_B\succeq0.
}
$$

Equivalently, with

$$
R_z(\gamma)=\frac1{\gamma-z},
\qquad
d\mu_B(\gamma)=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma,
$$

we have

$$
\boxed{
\mathsf P_B(z,w)=
\langle R_z,R_w\rangle_{L^2(d\mu_B)}.
}
$$

That is the positive Bures/K Gram formula.

## Converse: Positivity Forces Boundary Support

Assume instead that

$$
\mathsf P_B\succeq0
$$

on `C_+`.

Then, for every `z in C_+`,

$$
0\le \mathsf P_B(z,z)
=
\frac{\operatorname{Im}m_B(z)}{\operatorname{Im}z}.
$$

Therefore

$$
\operatorname{Im}m_B(z)\ge0
\qquad (z\in\mathbb C_+).
$$

Moreover, a positive kernel must be finite at every point of its domain.
Thus `m_B` cannot have a pole in `C_+`. Hence `m_B` is analytic in `C_+`
and maps `C_+` into its closure. So `m_B` is a Herglotz/Nevanlinna function.

But

$$
m_B=-\frac{\Xi'}{\Xi}.
$$

Any zero of `Xi` inside `C_+` is a pole of `m_B` inside `C_+`, impossible for
a Herglotz function. By K-reality of `Xi`, any non-real zero of `Xi` has one
member of its K-pair in `C_+`. Therefore all zeros of `Xi` are real.

Thus

$$
\boxed{
\mathsf P_B\succeq0\quad\Longrightarrow\quad\mathrm{RH}.
}
$$

## No-Free-Lunch Lemma

There is no unconditional proof of positivity from the formal Gram identity
alone.

The formal identity

$$
\mathsf P_B(z,w)
=
\frac{\pi K_{E_B}(z,w)}
{\Xi(z)\overline{\Xi(w)}},
\qquad
E_B=\Xi+i\Xi',
$$

is algebraic. It becomes a positive Gram kernel exactly when `E_B` is
Hermite-Biehler:

$$
|E_B(z)|>|E_B^\#(z)|\qquad(z\in\mathbb C_+).
$$

But

$$
|E_B|^2-|E_B^\#|^2
=
4|\Xi|^2\operatorname{Im}\left(-\frac{\Xi'}{\Xi}\right).
$$

So positivity of the de Branges kernel is exactly positivity of `Im m_B`,
which is exactly the Herglotz form of RH.

Therefore an unconditional proof of the Gram formula's positivity would be a
proof of RH. It cannot be supplied by Bures positivity unless one first proves
that the Bures metric being used is genuinely positive and independent of the
same Pick kernel.

## Final Form of the Proof Obligation

The positivity proof is complete in conditional form:

$$
\operatorname{supp}D_B\subset\mathbb R
\quad\Rightarrow\quad
\mathsf P_B\succeq0.
$$

And the converse is complete:

$$
\mathsf P_B\succeq0
\quad\Rightarrow\quad
\operatorname{supp}D_B\subset\mathbb R.
$$

Thus the remaining non-circular RH mission is exactly:

$$
\boxed{
\text{prove K-unbroken boundary support of }D_B
\text{ without assuming Pick positivity.}
}
$$

