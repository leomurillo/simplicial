# Note: Cone Existence Is the Law; Orientation Is the Bit

Date: 2026-05-22  
Mission: close the interpretation-space result as a proof.

## Theorem

Let

$$
\Xi(z)=\xi\left(\frac12+iz\right)
$$

and

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}.
$$

Define the Pick kernel

$$
\mathsf P_B(z,w)
=
\frac{m_B(z)-\overline{m_B(w)}}{z-\bar w}.
$$

Then the following are equivalent:

$$
\boxed{
\mathsf P_B\succeq0\text{ on a chosen spectral half-plane}
}
$$

$$
\boxed{
\operatorname{supp}D_B\subset\mathbb R
}
$$

$$
\boxed{
\text{all zeros of }\Xi\text{ are real}
}
$$

$$
\boxed{
\mathrm{RH}.
}
$$

Moreover, reversing the global orientation cannot repair a failure of this
condition. If off-line zeros exist, no choice of upper/lower orientation and no
global sign flip makes the Pick kernel a positive Hilbert/Bures Gram kernel.

## Proof

The divisor current of the Bures log derivative is

$$
D_B=-\frac1\pi\partial_{\bar z}m_B
=
\sum_{\Xi(a)=0}m_a\delta_a.
$$

So the support of `D_B` is exactly the zero divisor of `Xi`.

### 1. Boundary Support Gives a Positive Cone

Assume

$$
\operatorname{supp}D_B\subset\mathbb R.
$$

Then

$$
m_B(z)=\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z},
\qquad \Gamma\subset\mathbb R.
$$

Therefore

$$
\mathsf P_B(z,w)
=
\sum_{\gamma\in\Gamma}
\frac{m_\gamma}{(\gamma-z)(\gamma-\bar w)}.
$$

For any finite list `z_i` in one spectral half-plane and any coefficients
`c_i`,

$$
\begin{aligned}
\sum_{i,j}c_i\overline{c_j}\mathsf P_B(z_i,z_j)
&=
\sum_{\gamma\in\Gamma}m_\gamma
\left|
\sum_i\frac{c_i}{\gamma-z_i}
\right|^2\\
&\ge0.
\end{aligned}
$$

Thus

$$
\mathsf P_B\succeq0.
$$

This is the positive Hilbert/Bures Gram cone:

$$
\mathsf P_B(z,w)=
\langle R_z,R_w\rangle_{L^2(D_B)},
\qquad
R_z(\gamma)=\frac1{\gamma-z}.
$$

### 2. A Positive Cone Forces Boundary Support

Conversely, suppose

$$
\mathsf P_B\succeq0
$$

on a spectral half-plane `H`. Then every diagonal value is finite and
nonnegative:

$$
\mathsf P_B(z,z)
=
\frac{\operatorname{Im}m_B(z)}{\operatorname{Im}z}
\ge0
\qquad (z\in H).
$$

In particular, `m_B` has no pole inside `H`, because a pole would make the
kernel undefined and no Hilbert norm could exist there.

But poles of

$$
m_B=-\Xi'/\Xi
$$

are precisely zeros of `Xi`. Hence `Xi` has no zeros in `H`.

Since `Xi` is real entire, any non-real zero comes with its conjugate. Thus if
there were any non-real zero, one member of the conjugate pair would lie in the
chosen half-plane. Contradiction.

Therefore all zeros of `Xi` are real:

$$
\operatorname{supp}D_B\subset\mathbb R.
$$

This is RH.

### 3. Why Orientation Reversal Does Not Save Off-Line Zeros

Let an off-line zero be

$$
\rho=\frac12+\delta+i\gamma,\qquad \delta>0.
$$

In spectral coordinates this produces zeros at

$$
\gamma+i\delta,\quad \gamma-i\delta
$$

and, by evenness,

$$
-\gamma+i\delta,\quad -\gamma-i\delta.
$$

So the divisor has atoms in both spectral half-planes.

If we call the upper half-plane "future," the upper atoms are interior poles.
If we call the lower half-plane "future," the lower atoms are interior poles.
Multiplying the kernel or `m_B` by a global sign changes the orientation of
the cone but does not remove the poles.

Therefore off-line zeros are not a wrong sign. They are the failure of cone
existence.

## Corollary: The Z/2 Bit Is Real but Secondary

Once boundary support holds, the system admits a positive cone. At that point
one may choose an orientation convention:

- upper half-plane as future;
- lower half-plane as future;
- positive current;
- negative current.

This is the Z/2 bit. It is arbitrary before it is chosen, but after it is
chosen it propagates as law.

But the existence of the cone is not arbitrary.

Thus:

$$
\boxed{
\text{orientation is a choice;}
\qquad
\text{cone existence is a theorem-level constraint.}
}
$$

## Link to the Physics Papers

Paper 20 identifies

$$
m_{\text{simplex}}^2\ge0
$$

as one inequality with several readings:

1. weak-energy / no-tachyon condition;
2. monotone decay exponent;
3. second law in program form;
4. Raychaudhuri-like focusing non-negativity.

Paper 32 refines the same point:

- the **magnitude** of projection non-closure is gravity-adjacent;
- the **sign** of projection non-closure is the arrow of time.

The Bures Pick kernel is the RH analog:

- the **divisor measure** is the spectral mass;
- the **Pick sign** is the spectral arrow;
- the **existence of a positive cone** is the non-negotiable law.

The "unmovable free will determined" pattern is therefore:

1. before the first irreversible projection, the two orientations are symmetric;
2. the first irreversible event locks one orientation;
3. after lock-in, the chosen bit propagates as if fundamental;
4. but the possibility of lock-in requires a cone to exist.

For RH, the cone exists exactly when the zeta divisor is K-unbroken:

$$
\boxed{
\operatorname{supp}D_B\subset\mathbb R.
}
$$

That is the closure.

