# Note: The Pick Kernel of \(m_B\) as a Bures/K Gram Kernel

Date: 2026-05-22  
Mission: prove the Pick kernel of

$$
m_B(z)=-\frac{\Xi'(z)}{\Xi(z)}
$$

is a Bures/K Gram kernel.

## Verdict

There is an exact Gram formula, but its positive-definite Bures meaning is
equivalent to RH.

The correct statement is:

$$
\boxed{
\mathsf P_B(z,w)
:=
\frac{m_B(z)-\overline{m_B(w)}}{z-\bar w}
=
\int_{\mathbb R}
\frac{d\mu_B(\gamma)}
{(\gamma-z)(\gamma-\bar w)}
}
$$

with

$$
d\mu_B(\gamma)=\sum_{\Xi(\gamma)=0}m_\gamma\delta_\gamma
$$

provided the Bures divisor current is K-unbroken, i.e. supported on the real
axis.

Equivalently,

$$
\mathsf P_B(z,w)
=
\langle R_z,R_w\rangle_{L^2(d\mu_B)},
\qquad
R_z(\gamma)=\frac1{\gamma-z}.
$$

This is the desired Bures/K Gram kernel. But proving that this is a **positive
Hilbert/Bures** Gram kernel is the same as proving the divisor is supported on
the K-fixed boundary, hence the same as RH.

So:

$$
\boxed{
\mathsf P_B\text{ is a positive Bures/K Gram kernel on }\mathbb C_+
\iff
\text{RH}.
}
$$

## Algebraic de Branges Identity

Let

$$
A(z)=\Xi(z),\qquad B(z)=-\Xi'(z),
$$

so that

$$
m_B(z)=\frac{B(z)}{A(z)}.
$$

The derivative-polarized de Branges function is

$$
E_B(z)=A(z)-iB(z)=\Xi(z)+i\Xi'(z),
$$

with

$$
E_B^\#(z)=A(z)+iB(z)=\Xi(z)-i\Xi'(z).
$$

The de Branges reproducing kernel associated with `E_B` is formally

$$
K_{E_B}(z,w)
=
\frac{
E_B(z)\overline{E_B(w)}
-
E_B^\#(z)\overline{E_B^\#(w)}
}
{2\pi i(\bar w-z)}.
$$

Expanding `E_B=A-iB` gives

$$
K_{E_B}(z,w)
=
\frac{
B(z)\overline{A(w)}
-
A(z)\overline{B(w)}
}
{\pi(z-\bar w)}.
$$

Therefore

$$
\boxed{
\mathsf P_B(z,w)
=
\frac{\pi K_{E_B}(z,w)}
{A(z)\overline{A(w)}}.
}
$$

This identity is unconditional wherever `A(z)A(w) != 0`. It proves the exact
algebraic Gram form.

The issue is positivity: `K_{E_B}` is a positive reproducing kernel exactly
when `E_B` is Hermite-Biehler. That is exactly the Herglotz property of
`m_B`, hence exactly RH.

## Boundary Divisor Gram Formula

Assume K-unbroken boundary support:

$$
\operatorname{supp}D_B\subset\mathbb R.
$$

Then the divisor current is a positive boundary measure

$$
d\mu_B=\sum_{\gamma\in\Gamma}m_\gamma\delta_\gamma.
$$

The Hadamard product gives

$$
m_B(z)=\sum_{\gamma\in\Gamma}\frac{m_\gamma}{\gamma-z}
$$

locally uniformly in `C_+`. Hence

$$
\begin{aligned}
\mathsf P_B(z,w)
&=
\frac{m_B(z)-\overline{m_B(w)}}{z-\bar w}\\
&=
\sum_{\gamma\in\Gamma}
m_\gamma
\frac{
\frac1{\gamma-z}-\frac1{\gamma-\bar w}
}
{z-\bar w}\\
&=
\sum_{\gamma\in\Gamma}
\frac{m_\gamma}{(\gamma-z)(\gamma-\bar w)}.
\end{aligned}
$$

Thus

$$
\boxed{
\mathsf P_B(z,w)
=
\langle R_z,R_w\rangle_{L^2(d\mu_B)},
\qquad
R_z(\gamma)=\frac1{\gamma-z}.
}
$$

This is a genuine positive Gram representation. In the Bures language, the
Hilbert space is the K-fixed boundary divisor space of the denominator line.

## Converse: Any Positive Bures/K Gram Proves RH

Suppose there exists a positive Bures/K Hilbert space `H_B` and vectors `R_z`
for every `z in C_+` such that

$$
\mathsf P_B(z,w)=\langle R_z,R_w\rangle_{H_B}.
$$

Then, for every `z in C_+`,

$$
\frac{\operatorname{Im}m_B(z)}{\operatorname{Im}z}
=
\mathsf P_B(z,z)
=
\|R_z\|_{H_B}^2
\ge0.
$$

Also, a finite Hilbert norm at every `z in C_+` rules out poles of `m_B` in
`C_+`. Thus `m_B` is analytic on `C_+` and has nonnegative imaginary part
there. So `m_B` is Herglotz.

But

$$
m_B=-\Xi'/\Xi
$$

is Herglotz on `C_+` if and only if every zero of `Xi` is real. Therefore
the positive Bures/K Gram law implies RH.

Combining with the boundary-divisor construction:

$$
\boxed{
\text{positive Bures/K Gram law}
\iff
\text{K-unbroken boundary support}
\iff
\text{RH}.
}
$$

## What Can Be Proved Unconditionally

Unconditionally, one has:

1. the algebraic de Branges identity

   $$
   \mathsf P_B(z,w)
   =
   \frac{\pi K_{E_B}(z,w)}
   {\Xi(z)\overline{\Xi(w)}};
   $$

2. the divisor-current identity

   $$
   D_B=\sum_{\Xi(a)=0}m_a\delta_a;
   $$

3. a formal divisor expansion with possible interior atoms.

If interior atoms exist, the corresponding form is not a positive Hilbert
Gram form on `C_+`. It becomes a Krein/Pontryagin-type divisor form with
indefinite directions. This is exactly what the artificial off-line cluster
probe shows.

## Conclusion

The requested proof is possible in the following exact sense:

$$
\boxed{
\text{If }D_B\text{ is K-unbroken, then }\mathsf P_B
\text{ is the }L^2(D_B)\text{ Bures/K Gram kernel.}
}
$$

But the unconditional positive Gram statement is not a smaller lemma. It is
equivalent to RH.

The next non-circular target is therefore not to rewrite the kernel as a Gram
kernel, which we have done conditionally. The target is to derive positivity
of the singular boundary divisor space from the `Z/6` Bures lift without
assuming boundary support:

$$
\boxed{
\text{derive }\operatorname{supp}D_B\subset\mathbb R
\text{ from the cubic/Bures structure.}
}

