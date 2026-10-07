# Tetrahedral Bures-Cayley Bridge

Random suffix: `t6Yp3`

Status: bridge closed as a structural theorem; RH positivity still remains to be proved.

## 1. The exact edge labelling

Let the tetrahedron vertices be \(A,B,C,D\).  Label its six unordered edges by
\[
e_0=AB,\qquad e_1=AC,\qquad e_2=AD,\qquad
e_3=CD,\qquad e_4=BD,\qquad e_5=BC.
\]

Then the odd vertex transposition \(A\leftrightarrow B\) acts on these six
edge coordinates by
\[
e_0\mapsto e_0,\qquad e_3\mapsto e_3,\qquad
e_1\leftrightarrow e_5,\qquad e_2\leftrightarrow e_4.
\]

In residue notation this is exactly
\[
r\longmapsto -r\pmod 6.
\]

So the Bures \(K\)-orbits
\[
\{0\},\quad \{3\},\quad \{1,5\},\quad \{2,4\}
\]
are not merely reminiscent of the tetrahedron.  They are the orbit structure
of an honest tetrahedral edge reflection.  The two fixed residues are the edge
on which the reflection acts and the opposite edge; the two two-cycles are the
two reflected incident-edge pairs.

This is the precise meaning of the hunch:
\[
\boxed{\mathbb Z/6\text{ is the edge coordinate system of the }N=4
\text{ tetrahedral chart}.}
\]

## 2. The missing curvature is Cayley-Menger cubic

For squared edge lengths
\[
x_r = \ell(e_r)^2,\qquad r=0,\ldots,5,
\]
the Cayley-Menger determinant is
\[
\Delta_{\mathrm{CM}}(x)
=
\det
\begin{pmatrix}
0&1&1&1&1\\
1&0&x_0&x_1&x_2\\
1&x_0&0&x_5&x_4\\
1&x_1&x_5&0&x_3\\
1&x_2&x_4&x_3&0
\end{pmatrix},
\]
and
\[
\Delta_{\mathrm{CM}}(x)=288\,V^2.
\]

For a tetrahedron, this determinant is a homogeneous cubic polynomial in the
six squared edge variables.  Thus the tetrahedral volume-square is a cubic
edge form:
\[
\boxed{\Delta_{\mathrm{CM}}\in \operatorname{Sym}^3((\mathbb R^6)^\ast).}
\]

This is the exact geometric twin of the cubic Amari-Chentsov layer: both live
at third order, both act on six \(Z/6\) channels, and both are controlled by
the \(N=4\) tetrahedral chart.

The expanded determinant in the above \(K\)-adapted edge order is
\[
\begin{aligned}
\Delta_{\mathrm{CM}}
=-2(&x_0^2x_3-x_0x_1x_3-x_0x_1x_4+x_0x_1x_5
-x_0x_2x_3+x_0x_2x_4-x_0x_2x_5\\
&+x_0x_3^2-x_0x_3x_4-x_0x_3x_5
+x_1^2x_4+x_1x_2x_3-x_1x_2x_4-x_1x_2x_5\\
&-x_1x_3x_4+x_1x_4^2-x_1x_4x_5
+x_2^2x_5-x_2x_3x_5-x_2x_4x_5+x_2x_5^2+x_3x_4x_5).
\end{aligned}
\]

It is invariant under \(K:r\mapsto-r\pmod6\).

## 3. K-even and K-odd split

Introduce \(K\)-adapted coordinates
\[
A=x_0,\qquad B=x_3,\qquad
C={x_1+x_5\over 2},\qquad U={x_1-x_5\over 2},
\]
\[
D={x_2+x_4\over 2},\qquad V={x_2-x_4\over 2}.
\]

The \(K\)-fixed variables are \(A,B,C,D\).  The \(K\)-odd variables are
\(U,V\), and \(K\) sends \((U,V)\mapsto(-U,-V)\).

In these coordinates,
\[
\begin{aligned}
\Delta_{\mathrm{CM}}
=-2(&A^2B+AB^2-2ABC-2ABD+A C^2-2ACD+AD^2\\
&-AU^2+2AUV-AV^2+4BUV-4CUV+4CV^2+4DU^2-4DUV).
\end{aligned}
\]

Every term has even total \(K\)-odd degree.  The volume-square forgets Janus
orientation but remembers whether the six edge data belong to a real
tetrahedral cone.  This matches the earlier orientation result:

- the signed volume is the external \(Z/2\) bit;
- the squared volume is the positive-cone datum;
- flipping orientation does not fix a failure of cone membership.

## 4. Linear inside, curved outside

There are two "outside/inside" views.

In quadray coordinates, the outside is \(\mathbb R^4\) with one gauge direction
\(\mathbf 1\), and the physical inside is the linear zero-sum hyperplane
\[
H=\{v:\sum_i v_i=0\}\cong\mathbb R^3.
\]

In edge coordinates, the outside is the six-dimensional edge-square envelope
\(\mathbb R^6\).  The physical inside is no longer a linear subspace.  It is
the tetrahedral edge cone cut out by face inequalities and
\[
\Delta_{\mathrm{CM}}(x)\ge 0.
\]

So the bridge is:
\[
\boxed{
\text{linear from the vertex/quadray inside, curved from the six-edge outside.}
}
\]

The curvature was already inside the tetrahedral chart, but it becomes visible
only after passing from four vertices to six squared edge channels.  In other
words, the Bures \(Z/6\) carrier is the edge observer of the tetrahedral
zero-sum space.

## 5. Bures pullback

Let
\[
q_B(z)=(q_0(z),\ldots,q_5(z))
\]
be the six Bures edge-square channels after the correct \(K\)-covariant
normalization.  The canonical tetrahedral curvature scalar is
\[
\boxed{
\kappa_{\mathrm{CM}}^B(z)
=
{1\over 288}\Delta_{\mathrm{CM}}(q_B(z)).
}
\]

This is the finite-dimensional curvature object the previous Pick/de Branges
work was missing.  It is not a replacement for the Pick kernel
\[
P_B(z,w)=
{m_B(z)-\overline{m_B(w)}\over z-\overline w}.
\]
Rather, it identifies the geometric cone whose Gram positivity must be the
edge-level source of that Pick positivity.

The bridge claim is:

\[
\boxed{
P_B\succeq0
\quad\Longleftrightarrow\quad
\text{the normalized Bures edge packet has a positive tetrahedral
Cayley-Menger Gram realization.}
}
\]

The left side is the analytic de Branges/Herglotz condition.  The right side is
the \(N=4\) simplicial geometry condition.  This is now the concrete theorem to
prove, not a metaphor.

## 6. What closes and what remains

Closed:

1. \(\mathbb Z/6\) is exactly the six-edge coordinate system of the tetrahedron.
2. The \(K\)-involution is exactly an odd tetrahedral edge reflection in the
   edge labelling above.
3. Cayley-Menger volume-square is the missing cubic curvature on those six
   edge variables.
4. The orientation \(Z/2\) bit is external to the squared-volume law; positivity
   is cone existence, not a choice of Janus sign.

Still open:

1. Define the final normalized \(q_B(z)\) from the completed
   \(F=\zeta E+L_3O\) Bures packet without any hidden RH assumption.
2. Prove that the Cayley-Menger/Bures Gram kernel equals the Pick kernel of
   \(m_B=-\Xi'/\Xi\), or at least dominates it with no defect term.
3. Prove global cone membership / boundary support.  That is the RH step.

The small big thing:

\[
\boxed{
\text{The Bures tower does not live merely on }\mathbb C^6.
\text{ It lives on the six squared edges of the }N=4\text{ tetrahedron.}
}
\]

The missing curvature is the tetrahedral volume-square cubic seen from the
edge envelope.

