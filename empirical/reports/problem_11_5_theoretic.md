# Problem 11.5: Canonical Binary Ext Representative

**Status:** closed for the first mixed row.
**Row:** \(R={\mathbb F}_4[u]/(u^2)\), with
\({\mathbb F}_4={\mathbb F}_2[\omega]/(\omega^2+\omega+1)\).
**Paper hook:** Section 9.1.1 of
`11.quotient_character_adjacency_algebras.md`.

---

## Canonical Section

Choose a wild base point

$$
\omega_0=a_{\omega_0}+b_{\omega_0}u,\qquad a_{\omega_0}\ne0.
$$

The Hayes normalizer is transitive on \(X_{u^2}\), so the section may be
written after rebasing as \(a_{\omega_0}=1,\ b_{\omega_0}=0\).  The canonical
coordinates are

$$
T_{\nu_T}=\nu_Tu,\qquad
W_{\rho,\nu}=\rho+\rho\nu u,
$$

where \(\nu_T,\rho\in{\mathbb F}_4^\times\) and
\(\nu\in{\mathbb F}_4\).  Equivalently, before rebasing:

$$
\rho=\frac a{a_{\omega_0}},
\qquad
\nu=\frac ba-\frac{b_{\omega_0}}{a_{\omega_0}},
\qquad
\nu_T=\frac b{a_{\omega_0}}.
$$

The filtered section is therefore

$$
s(\overline{T_{\nu_T}})=A_{\nu_Tu},
\qquad
s(\overline{W_{\rho,\nu}})=A_{\rho+\rho\nu u},
$$

with the relevant conductor source and target projectors included.

---

## Cocycle Representative

For composable quotient-shifts, the normalized carry is

$$
\kappa_s(A_\zeta^{\mathfrak g,\mathfrak f},
         A_\eta^{\mathfrak f,\mathfrak e})
=
\operatorname{gr}_{+}
\left(
P_{\mathfrak g}M_\zeta P_{\mathfrak f}M_\eta P_{\mathfrak e}
-
P_{\mathfrak g}M_{\zeta+\eta}P_{\mathfrak e}
\right).
$$

The reducer report
`empirical/reports/ext_ch_cocycle_f4_u2.md` materializes this finite cochain:

$$
\begin{array}{c|c}
\text{quantity}&\text{value}\\
\hline
\text{raw atoms}&1569\\
\text{nonzero carry pairs}&369\\
\text{atom orbits}&71\\
\text{pair orbits}&20\\
\text{missing atom or pair orbit entries}&0.
\end{array}
$$

The full-block coboundary diagnostic is

$$
\dim C^1=3204,\qquad
\dim C^2=76320,\qquad
\operatorname{rank}B^2=3204,
$$

with residual support \(1569\).  Thus the carry is not a coboundary in the
full-block section-change model.

---

## Orbit Canonicalization

Apply the \((T_{\nu_T},W_{\rho,\nu})\) coordinate rule slotwise to

$$
(\tau,\omega_0,\alpha,\beta,\chi_{\mathrm{in}},\chi_{\mathrm{out}})
$$

and quotient by Frobenius.  Section 9.1 verifies that this signature has no
collisions:

$$
4438/4438
\quad\text{full-defect signatures},\qquad
592/592
\quad\text{commutator signatures}.
$$

Therefore the first mixed representative needs no additional local invariant
beyond conductor slot type, the residue ratio \(\rho\), the nil-tail balance
\(\nu\), and the Frobenius quotient.  The \(4438\) full-defect orbits and the
\(592\) commutator orbits are linear consequences of the finite carry table
under this section.

---

## What Remains Open

Problem 11.5 is closed at binary arity for
\({\mathbb F}_4[u]/(u^2)\).  The next open layer is not another hand audit of
this representative; it is the higher tower:

$$
\operatorname{Ext}_{CH}^{(n)},\qquad n\ge3,
$$

including the arity-4 class behind the measured \(592\)-orbit mixed curvature
lift and the operadic composition law for the quotient-character
hyper-adjacency tower.
