# Bures-Cayley Pick Identity

Random suffix: `v4Nq8`

Status: the Cayley-Menger bridge gives an exact divisor identity.  Positivity
still reduces to the same boundary-support/RH step.

## 1. Hint from the collider paper

The attached paper
`C:\Users\leomu\Downloads\SciPost collider 2605.15910v1.pdf`
uses geometric algebra for collider events.  The relevant hint is its
Cayley-Menger/Gram "collapse" principle:

1. Higher-grade magnitudes are Gram/Cayley-Menger determinants of lower inner
   products.
2. The only genuinely extra datum is the orientation/pseudoscalar sign bit.

Translated to our problem:

- the six \(Z/6\) Bures channels should be treated as tetrahedral edge-square
  coordinates;
- the correct scalar curvature/divisor carrier is the Cayley-Menger cubic;
- the Janus/orientation \(Z/2\) bit is the square-root/sign data of volume, not
  the volume-square cone condition itself.

So the next object is not another arbitrary curvature scalar.  It must be the
Gram/Cayley-Menger determinant of the six Bures edge channels.

## 2. Exact holomorphic edge packet

Let
\[
a=2^{-s},\qquad b=3^{-s},\qquad Z=\zeta(s),\qquad L=L(s,\chi_3).
\]

Use the exact \(Z/6\) decomposition
\[
F(s)=Z(s)E(s)+L(s)O(s),
\]
with edge order
\[
0=AB,\quad 1=AC,\quad 2=AD,\quad 3=CD,\quad 4=BD,\quad 5=BC.
\]

The six components are
\[
F_0=abZ,
\]
\[
F_1={1\over2}(1-a)(1-b)Z+{1\over2}(1+a)L,
\]
\[
F_2={1\over2}a(1-b)Z+{1\over2}aL,
\]
\[
F_3=b(1-a)Z,
\]
\[
F_4={1\over2}a(1-b)Z-{1\over2}aL,
\]
\[
F_5={1\over2}(1-a)(1-b)Z-{1\over2}(1+a)L.
\]

This is the same \(F=\zeta E+L_3O\) packet from the \(Z/6\) Hurwitz
decomposition, now read as six tetrahedral edge-square coordinates.

## 3. Cayley-Menger factor theorem

Let \(\Delta_{\rm CM}(x_0,\ldots,x_5)\) be the tetrahedral Cayley-Menger
determinant in the edge order above:
\[
\Delta_{\rm CM}
=
\det
\begin{pmatrix}
0&1&1&1&1\\
1&0&x_0&x_1&x_2\\
1&x_0&0&x_5&x_4\\
1&x_1&x_5&0&x_3\\
1&x_2&x_4&x_3&0
\end{pmatrix}.
\]

Then direct symbolic expansion gives
\[
\boxed{
\Delta_{\rm CM}(F(s))
=
Z(s)\,A_{\rm CM}(s),
}
\]
where
\[
\boxed{
A_{\rm CM}(s)
=
-{a\over2}\left(L(s,\chi_3)^2 C_0(a,b)+Z(s)^2 C_2(a,b)\right),
}
\]
with
\[
C_0(a,b)=-4a^2b-4ab+4a+3b,
\]
and
\[
C_2(a,b)
=
b\left(4a^2b^2-8a^2b+4a^2-12ab^2+12ab-4a+9b^2-6b+1\right).
\]

This is the bridge in algebraic form:
\[
\boxed{
\text{the Bures divisor of }Z\text{ is a factor of the tetrahedral
Cayley-Menger edge divisor.}
}
\]

At a nontrivial zero \(\rho\) of \(\zeta\),
\[
\Delta_{\rm CM}(F(\rho))=0
\]
provided \(A_{\rm CM}(\rho)\) is finite.  Generically
\[
A_{\rm CM}(\rho)
=
-{2^{-\rho}\over2}L(\rho,\chi_3)^2
C_0(2^{-\rho},3^{-\rho}),
\]
so the zero is simple if \(L(\rho,\chi_3)\neq0\) and
\(C_0(2^{-\rho},3^{-\rho})\neq0\).

## 4. Completed/K-normalized version

Move to spectral coordinates
\[
s={1\over2}+iz,
\]
and replace
\[
Z(s)\mapsto \Xi(z)=\xi(1/2+iz),
\]
\[
L(s,\chi_3)\mapsto {\mathcal L}_3(z)
=
\Lambda_3(1/2+iz).
\]

Define the completed edge packet
\[
F_c(z)=\Xi(z)E(s)+{\mathcal L}_3(z)O(s).
\]

The same algebra gives
\[
\boxed{
{\mathcal C}_B(z)
:=
\Delta_{\rm CM}(F_c(z))
=
\Xi(z)\,{\mathcal A}_B(z),
}
\]
where
\[
{\mathcal A}_B(z)
=
-{a\over2}
\left({\mathcal L}_3(z)^2C_0(a,b)+\Xi(z)^2C_2(a,b)\right),
\qquad
a=2^{-s},\;b=3^{-s}.
\]

Therefore the Bures log-derivative object is exactly
\[
\boxed{
m_B(z)
=
-{\Xi'(z)\over \Xi(z)}
=
-\partial_z\log{\mathcal C}_B(z)
+\partial_z\log{\mathcal A}_B(z).
}
\]

This is the Cayley-Menger version of the previous Bures transfer subtraction.
The raw CM divisor contains the \(\Xi\)-divisor plus the cofactor divisor; the
correct K-normalized transfer subtracts the cofactor and leaves exactly the
\(\Xi\)-divisor.

## 5. Pick kernel interpretation

Define
\[
m_{\rm CM}(z)
:=
-\partial_z\log{\mathcal C}_B(z)
+\partial_z\log{\mathcal A}_B(z).
\]

Then
\[
m_{\rm CM}=m_B,
\]
and hence
\[
\boxed{
P_B(z,w)
=
{m_{\rm CM}(z)-\overline{m_{\rm CM}(w)}\over z-\bar w}.
}
\]

So the Pick kernel is the Pick kernel of the normalized Cayley-Menger divisor
transfer
\[
{\mathcal C}_B/{\mathcal A}_B=\Xi.
\]

This closes the missing bridge:

\[
\boxed{
\text{Bures }Z/6\text{ edge packet}
\xrightarrow{\Delta_{\rm CM}}
\text{Cayley-Menger divisor}
\xrightarrow{\text{cofactor subtraction}}
m_B
\xrightarrow{\text{Pick}}
P_B.
}
\]

## 6. Positivity and the remaining gap

The real tetrahedral Cayley-Menger determinant gives
\[
\Delta_{\rm CM}=288V^2.
\]

At the regular tetrahedron with all squared edges \(8/3\), the Hessian of
\(\Delta_{\rm CM}\) has one positive scale direction and five negative
shape directions.  Therefore
\[
-D^2\Delta_{\rm CM}
\]
is positive definite after the scale direction is quotiented out.  This is the
finite-dimensional Bures/K edge-cone metric.

But this finite-dimensional cone positivity is not yet the full Pick
positivity.  The Pick positivity says that the divisor of
\[
{\mathcal C}_B/{\mathcal A}_B=\Xi
\]
has no atoms in \(\mathbb C_+\), equivalently that every \(\Xi\)-zero is real
in the spectral coordinate.  That is still RH.

So the situation is:

Closed:

1. The six-channel Bures packet is an edge-square packet.
2. The Cayley-Menger determinant of that packet factors by the zeta/Xi
   channel.
3. The Bures log derivative \(m_B\) is exactly the normalized
   Cayley-Menger divisor derivative.
4. The collider-paper hint explains why the orientation bit is the only extra
   datum beyond Gram/Cayley-Menger magnitudes.

Still open:

1. Prove K-unbroken boundary support of the normalized CM divisor.
2. Equivalently prove \(P_B\succeq0\).
3. Equivalently prove RH.

The bridge is no longer missing.  The remaining theorem is now sharply named:

\[
\boxed{
\textbf{K-unbroken Cayley-Menger divisor support for }
{\mathcal C}_B/{\mathcal A}_B.
}
\]

