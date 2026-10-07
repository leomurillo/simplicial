# Infinite CM Divisor Hilbert Space

Random suffix: `Q2wL9`

Mission: go infinite after the finite six-edge Cayley-Menger no-go.

Status: the infinite Hilbert-Pólya object is explicit, conditional on
K-unbroken boundary support.  The remaining non-circular proof obligation is
to construct its positive boundary measure from CM/Bures geometry without
assuming RH.

## 1. From finite edge carrier to infinite divisor space

The finite \(Z/6\) tetrahedral edge carrier gives the exact divisor identity
\[
{\mathcal C}_B(z):=\Delta_{\rm CM}(F_c(z))
=
\Xi(z)\,{\mathcal A}_B(z).
\]

The normalized transfer is
\[
{\mathcal T}_{\rm CM}(z)
:=
{{\mathcal C}_B(z)\over{\mathcal A}_B(z)}
=\Xi(z).
\]

Thus the finite CM layer identifies the right divisor.  It cannot itself be
the whole positive Hilbert space, because \(P_B\) has infinite rank.  The
correct Hilbert space is the \(L^2\)-space of the normalized divisor measure.

## 2. Boundary divisor measure

If the normalized CM divisor is K-unbroken, then
\[
\operatorname{supp}\operatorname{div}{\mathcal T}_{\rm CM}
\subset \mathbb R.
\]

Write the real spectral zeros as
\[
\Gamma=\{\pm\gamma_n:n\ge1\},
\]
with multiplicities \(m_\gamma\).  The boundary divisor measure is
\[
d\mu_{\rm CM}(\gamma)
=
\sum_{\gamma\in\Gamma}m_\gamma\,\delta_\gamma.
\]

Define
\[
{\mathcal H}_{\rm CM}^{\infty}
:=
L^2(\mathbb R,d\mu_{\rm CM})
\cong
\ell^2(\Gamma,m_\gamma).
\]

For \(z\in\mathbb C_+\), set
\[
R_z(\gamma)={1\over \gamma-z}.
\]

Since the zero counting law gives \(\gamma_n\sim 2\pi n/\log n\), the series
\[
\sum_{\gamma\in\Gamma}{m_\gamma\over |\gamma-z|^2}
\]
converges.  Hence \(R_z\in{\mathcal H}_{\rm CM}^{\infty}\).

## 3. The infinite Gram law

The Pick kernel is
\[
P_B(z,w)
=
{m_B(z)-\overline{m_B(w)}\over z-\bar w},
\qquad
m_B(z)=-{\Xi'(z)\over\Xi(z)}.
\]

Under boundary support,
\[
m_B(z)=
\sum_{\gamma\in\Gamma}{m_\gamma\over\gamma-z}
\]
with the usual symmetric/canonical convergence.  Therefore
\[
\boxed{
P_B(z,w)
=
\sum_{\gamma\in\Gamma}
{m_\gamma\over(\gamma-z)(\gamma-\bar w)}
=
\langle R_z,R_w\rangle_{{\mathcal H}_{\rm CM}^{\infty}}.
}
\]

This is the infinite CM/Bures Gram law.  Positivity is immediate once the
measure is a positive boundary measure:
\[
\sum_{i,j}c_i\bar c_jP_B(z_i,z_j)
=
\int_{\mathbb R}
\left|\sum_i {c_i\over \gamma-z_i}\right|^2
d\mu_{\rm CM}(\gamma)
\ge0.
\]

## 4. The Hilbert-Pólya operator

Define the multiplication operator
\[
(\hat H_{\rm sym}f)(\gamma)=\gamma f(\gamma)
\]
on the domain
\[
{\mathcal D}(\hat H_{\rm sym})
=
\left\{
f\in L^2(d\mu_{\rm CM}):
\int_{\mathbb R}\gamma^2|f(\gamma)|^2\,d\mu_{\rm CM}(\gamma)<\infty
\right\}.
\]

This operator is self-adjoint.  Its spectrum is the closed support of
\(d\mu_{\rm CM}\), i.e.
\[
\operatorname{Spec}(\hat H_{\rm sym})=\{\pm\gamma_n:n\ge1\}.
\]

The positive Hilbert-Pólya operator is
\[
\hat H_+:=|\hat H_{\rm sym}|,
\]
with
\[
\boxed{
\operatorname{Spec}(\hat H_+)=\{\gamma_n:n\ge1\}.
}
\]

This is the exact infinite-dimensional operator once boundary support is
proved.

## 5. Why this is still conditional

The construction above starts from a positive boundary measure
\[
d\mu_{\rm CM}
=\sum_{\gamma\in\mathbb R}m_\gamma\delta_\gamma.
\]

That is precisely the statement that the normalized CM divisor has no
off-boundary atoms.  Since
\[
{\mathcal T}_{\rm CM}=\Xi,
\]
this is exactly RH.

So the Hilbert space is explicit, but the non-circular proof must construct
the positive measure directly from CM/Bures geometry:
\[
\boxed{
\text{construct }d\mu_{\rm CM}\ge0\text{ on }\mathbb R
\text{ with }
-{\Xi'\over\Xi}(z)
=
\int_{\mathbb R}{d\mu_{\rm CM}(\gamma)\over\gamma-z}.
}
\]

Equivalently, construct a positive canonical system whose Weyl function is
\[
m_B=-{\Xi'\over\Xi}.
\]

## 6. Canonical-system formulation

The infinite law can be expressed as:

Find a locally integrable Hamiltonian
\[
H_{\rm CM}(t)\succeq0,\qquad \operatorname{tr}H_{\rm CM}(t)=1,
\]
on a half-line, such that the canonical system
\[
J{dY\over dt}=zH_{\rm CM}(t)Y
\]
has Weyl function
\[
m_{H_{\rm CM}}(z)=m_B(z).
\]

If such \(H_{\rm CM}\) is built from the normalized Cayley-Menger edge
geometry, then \(m_B\) is Herglotz, the divisor is boundary-supported, and RH
follows.

This is the true infinite version of the finite \(Z/6\) program:
\[
\boxed{
Z/6\text{ identifies the divisor; }
H_{\rm CM}(t)\succeq0\text{ would prove its positivity.}
}
\]

## 7. Operational truncations

For computation, define
\[
\mu_N=\sum_{n=1}^N
\left(\delta_{\gamma_n}+\delta_{-\gamma_n}\right),
\]
and
\[
P_N(z,w)
=
\int {d\mu_N(\gamma)\over(\gamma-z)(\gamma-\bar w)}.
\]

Each \(P_N\) is a positive Gram kernel of rank at most \(2N\):
\[
P_N(z,w)
=
\langle R_z,R_w\rangle_{L^2(d\mu_N)}.
\]

As \(N\to\infty\), \(P_N\) converges to \(P_B\) under RH/canonical product
support.  Numerically, the truncations already reproduce the large diagonal
poles near low zeros and their rank grows with \(N\), matching the finite
no-go theorem.

## 8. What is now closed

Closed:

1. The finite \(Z/6\) Bures-Cayley layer identifies the normalized divisor
   \(\Xi\).
2. The correct infinite Hilbert space is
   \(L^2(\operatorname{div}\Xi)\) if the divisor is boundary-supported.
3. The Hilbert-Pólya operator is multiplication by \(\gamma\), with positive
   spectrum obtained by absolute value.
4. The Pick kernel is exactly the resolvent Gram kernel in that infinite
   space.

Still open:

1. Prove the normalized CM divisor is boundary-supported without assuming RH.
2. Equivalently construct the positive measure \(d\mu_{\rm CM}\) on
   \(\mathbb R\).
3. Equivalently construct the positive canonical-system Hamiltonian
   \(H_{\rm CM}(t)\) from the CM/Bures edge geometry.

