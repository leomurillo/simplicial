# T13 - Exact Simplicial Renormalization

**Integrating Out Conductor Boundaries in the Finite Apex Algebra**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *Projection does not create arbitrary error. It creates a boundary source.*

---

## Abstract

**Situation.** T11 proved that apex interactions obey finite character-conservation rules and that projected packet sectors leak through conductor-fusion boundaries. T12 proved that the apparently infinite moment/cumulant tower is finite spectral data, governed by a closure polynomial or, more generally, a finite coordinate algebra after projection. Together they invite a renormalization theory: if a sector is retained and its boundary is omitted, what exact effective theory is induced on the retained sector?

**Gap.** The prior papers identify the boundary but do not yet integrate it. Applications naturally speak of residual forces, projected interactions, missing sectors, and effective corrections, but without a theorem-level mechanism those phrases risk sounding perturbative or heuristic. We need an exact finite statement: when a conductor packet is projected away, how does its effect reappear in the retained theory, when does it vanish, and what is the universal completion?

**Action.** We prove nine structure theorems. First, the **Boundary Source Decomposition Theorem**: every projected \(n\)-leg vertex splits into a retained part and a boundary source supported on \(\partial_nS\). Second, the **Exact Boundary Integration Theorem**: eliminating the boundary is finite marginalization and logarithmic connected projection. Third, the **Schur Complement Renormalization Theorem**: at quadratic order the exact correction is the Schur complement. Fourth, the **Finite Renormalization Closure Theorem**: all induced effective towers close inside a finite retained coordinate algebra. Fifth, the **Beta Function as Boundary Curvature Theorem**: running couplings are newly admitted boundary packets. Sixth, the **Fixed Sector / Renormalizability Theorem**: exact renormalizability is equivalent to fusion closure. Seventh, the **Universality of Fusion Completion Theorem**: coordinate choices do not change the minimal closed packet completion. Eighth, the **Exact \(N=6\) Four-Sector Renormalization Theorem**: the smallest cross-prime model forces the full-conductor \(H_6\) packet as the cubic boundary of \(H_2\oplus H_3\). Ninth, the **Fusion-Closure Renormalization Group Theorem**: the finite simplicial RG is the closure operator \(S\mapsto\operatorname{Cl}_n(S)\).

**Result.** The central compression is
\[
\boxed{
\text{RG flow}=\text{boundary adjunction},
\qquad
\text{fixed points}=\text{fusion-closed sectors}.
}
\]
Projected forces are not arbitrary extras. They are boundary contractions of a finite apex theory.

**Harvest.** T13 turns the lamed-series into an exact finite Wilsonian laboratory. T11 says which boundaries appear. T12 says their induced towers are finite. T13 says how projection pays back its omissions: by adjoining the conductor-fusion boundary until a fusion-closed sector is reached.

**Keywords:** finite renormalization, conductor packets, projection residuals, boundary source, effective action, Schur complement, beta function, closure operator, fusion closure, universality class, finite RG, simplicial field theory, apex calculus.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T0 structured apex \(\mathcal M_x(\beta,c)\) | Generating functional whose sectors are projected |
| T2 cumulant tower as effective action | Logarithmic connected projection in Section 3 |
| T3 character orthogonality and cubic selection | \(n=3\) instance of conductor-boundary forcing |
| T4-T6 Helmert, harmonic, and RMS gauges | Coordinate presentations of retained sectors |
| T8 multiplicative apex | Multiplicative analog of boundary integration, forward direction |
| T9 Helmert-Fourier transfer matrix | Basis change does not alter fusion completion |
| T10 Kummer clock and power hierarchy | Integer-gauge samples of the same finite closure |
| T11 Apex Vertex Calculus | Boundary source and fusion closure |
| T12 Finite Apex Determinacy | Effective towers close in finite coordinate algebras |

---

## Notation

Let
\[
G=\mathbb Z/N
\]
and let
\[
\chi_a(s)=e^{2\pi ias/N}
\]
be the additive character indexed by \(a\in G\). For a character index \(a\), define its additive conductor by
\[
\operatorname{cond}(a)=\frac{N}{\gcd(a,N)}
\]
with the convention \(\operatorname{cond}(0)=1\).

For each divisor \(d\mid N\), define the conductor packet
\[
H_d=\operatorname{span}_{\mathbb C}\{\chi_a:\operatorname{cond}(a)=d\}.
\]
The trivial packet \(H_1\) is the constant packet. The nontrivial conductor set is
\[
\mathcal D_N=\{d:d\mid N,\ d>1\}.
\]
For \(S\subseteq\mathcal D_N\), write
\[
H_S=\bigoplus_{d\in S}H_d.
\]
Let \(\Pi_S\) denote the projection onto \(H_S\) with respect to the character-packet decomposition.

The \(n\)-leg product vertex is
\[
V_n(u_1,\ldots,u_n)=u_1\cdots u_n.
\]
On characters,
\[
V_n(\chi_{a_1},\ldots,\chi_{a_n})
=\chi_{a_1+\cdots+a_n}.
\]

For conductor labels \(d_1,\ldots,d_n\), define their \(n\)-fold fusion support by
\[
\operatorname{Fuse}(d_1,\ldots,d_n)
=
\{\operatorname{cond}(a_1+\cdots+a_n):
\operatorname{cond}(a_i)=d_i\}.
\]
For a packet set \(S\), define
\[
\operatorname{Fuse}_n(S)
=
\bigcup_{d_1,\ldots,d_n\in S}
\operatorname{Fuse}(d_1,\ldots,d_n).
\]
The nontrivial conductor-fusion boundary is
\[
\partial_nS
=
\operatorname{Fuse}_n(S)\setminus(S\cup\{1\}).
\]
The set \(S\) is \(n\)-fusion-closed if
\[
\operatorname{Fuse}_n(S)\subseteq S\cup\{1\}.
\]
The minimal \(n\)-fusion-closed set containing \(S\) is denoted
\[
\operatorname{Cl}_n(S).
\]

For effective actions, let \(\Omega\) be the finite state set with weights \(w_s>0\), \(\sum_sw_s=1\). A retained observable map is written
\[
Y_S:\Omega\to\mathbb R^m.
\]
Its exact retained partition and cumulant functionals are
\[
Z_{\mathrm{eff},S}(J)=\mathbb E e^{\langle J,Y_S\rangle},
\qquad
K_{\mathrm{eff},S}(J)=\log Z_{\mathrm{eff},S}(J).
\]

---

## 1. Why projection is renormalization

Projection is not a passive operation. If a sector \(H_S\) is retained and the complement is ignored, the product vertex may still generate non-retained packets:
\[
V_n(H_S,\ldots,H_S)\not\subseteq H_S.
\]
T11 identifies the exact location of this failure:
\[
V_n(H_S,\ldots,H_S)
\subseteq
H_S\oplus H_1\oplus\bigoplus_{d\in\partial_nS}H_d.
\]
Thus the error of projection is not diffuse. It is a boundary.

T13 studies what happens next. The boundary can be:

1. ignored, producing a residual;
2. integrated out, producing effective retained couplings;
3. adjoined, producing a larger sector;
4. iterated until a fixed point is reached.

This is the finite simplicial renormalization group. Its flow is not scale flow in spacetime. It is closure flow on the conductor-packet lattice.

---

## 2. Boundary source decomposition

### Theorem 1. Boundary Source Decomposition Theorem

Let
\[
H_S=\bigoplus_{d\in S}H_d
\]
be a retained conductor-packet sector. For the \(n\)-leg apex interaction
\[
V_n(u_1,\ldots,u_n)=u_1\cdots u_n,
\qquad u_i\in H_S,
\]
there is a unique decomposition
\[
V_n=\Pi_SV_n+(1-\Pi_S)V_n.
\]
Moreover,
\[
(1-\Pi_S)V_n(H_S,\ldots,H_S)
\subseteq
\bigoplus_{d\in\partial_nS}H_d
\]
up to the trivial constant packet \(H_1\). The support is universal and sharp: every packet in \(\partial_nS\) is attained by some character inputs from \(H_S\).

**Proof.** Each input has a unique packet expansion
\[
u_i=\sum_{d_i\in S}u_{i,d_i},
\qquad
u_{i,d_i}\in H_{d_i}.
\]
By multilinearity,
\[
V_n(u_1,\ldots,u_n)
=
\sum_{d_1,\ldots,d_n\in S}
V_n(u_{1,d_1},\ldots,u_{n,d_n}).
\]
It is enough to analyze one packet product
\[
V_n(H_{d_1},\ldots,H_{d_n}).
\]

The packet \(H_d\) is spanned by characters \(\chi_a\) with \(\operatorname{cond}(a)=d\). A basis monomial satisfies
\[
\chi_{a_1}\cdots\chi_{a_n}
=\chi_{a_1+\cdots+a_n}.
\]
Hence the output conductor is
\[
\operatorname{cond}(a_1+\cdots+a_n).
\]
As the \(a_i\) range over all inputs with conductors \(d_i\), the possible output conductors are exactly
\[
\operatorname{Fuse}(d_1,\ldots,d_n).
\]
Therefore
\[
V_n(H_{d_1},\ldots,H_{d_n})
\subseteq
\bigoplus_{e\in\operatorname{Fuse}(d_1,\ldots,d_n)}H_e.
\]
Summing over \(d_i\in S\),
\[
V_n(H_S,\ldots,H_S)
\subseteq
\bigoplus_{e\in\operatorname{Fuse}_n(S)}H_e.
\]

The projection \(\Pi_S\) keeps the packets in \(S\) and kills all non-retained nontrivial packets. The complementary projection \(1-\Pi_S\) keeps only packets outside \(S\), with \(H_1\) treated as the trivial mean/gauge packet. Thus the nontrivial non-retained support is
\[
\operatorname{Fuse}_n(S)\setminus(S\cup\{1\})
=\partial_nS.
\]
The splitting
\[
V_n=\Pi_SV_n+(1-\Pi_S)V_n
\]
is unique because \(\Pi_S\) is a projection and the packet decomposition is direct.

Sharpness follows from the definition of \(\operatorname{Fuse}\): for every \(d\in\partial_nS\), there exist character indices \(a_1,\ldots,a_n\) with \(\operatorname{cond}(a_i)\in S\) and
\[
\operatorname{cond}(a_1+\cdots+a_n)=d.
\]
Then
\[
V_n(\chi_{a_1},\ldots,\chi_{a_n})
=\chi_{a_1+\cdots+a_n}\in H_d.
\]
Individual linear combinations may cancel, but no smaller universal boundary support works. \(\square\)

---

## 3. Exact boundary integration

### Theorem 2. Exact Boundary Integration Theorem

Let the mean-zero character space split as
\[
H=H_S\oplus H_B,
\]
where \(H_B\) contains the non-retained boundary packets produced by \(S\)-interactions. Write the ledger component as
\[
y=y_S+y_B,
\qquad y_S\in H_S,\quad y_B\in H_B.
\]
Define the two-source finite partition functional
\[
Z(J_S,J_B)
=
\mathbb E\exp(\langle J_S,y_S\rangle+\langle J_B,y_B\rangle)
\]
and
\[
K(J_S,J_B)=\log Z(J_S,J_B).
\]
Then the exact retained effective functional obtained by eliminating the boundary source is
\[
K_{\mathrm{eff},S}(J_S)=K(J_S,0)
=
\log\mathbb E\exp(\langle J_S,y_S\rangle).
\]
Its retained \(n\)-point cumulants are exactly the full connected cumulants with all external legs in \(S\):
\[
\kappa^{\mathrm{eff}}_{i_1\cdots i_n}
=
\left.
\frac{\partial^nK}
{\partial J_{i_1}\cdots\partial J_{i_n}}
\right|_{J_S=0,J_B=0},
\qquad i_1,\ldots,i_n\in S.
\]
In a vertex expansion, the induced corrections are finite connected contractions through boundary packets.

**Proof.** Since
\[
H=H_S\oplus H_B,
\]
the decomposition
\[
y=y_S+y_B
\]
is unique. The full source-dependent finite partition functional is
\[
Z(J_S,J_B)
=
\mathbb E\exp(\langle J_S,y_S\rangle+\langle J_B,y_B\rangle).
\]
To retain only \(S\)-sector observables, set the boundary source to zero:
\[
Z_{\mathrm{eff},S}(J_S)
=Z(J_S,0)
=\mathbb E\exp(\langle J_S,y_S\rangle).
\]
Taking logarithms gives
\[
K_{\mathrm{eff},S}(J_S)
=K(J_S,0).
\]
No approximation is made: the expectation remains over the original finite state space, while the source probes only the retained observable.

Differentiating,
\[
\kappa^{\mathrm{eff}}_{i_1\cdots i_n}
=
\left.
\frac{\partial^nK_{\mathrm{eff},S}}
{\partial J_{i_1}\cdots\partial J_{i_n}}
\right|_{J_S=0}.
\]
Since \(K_{\mathrm{eff},S}(J_S)=K(J_S,0)\), this equals
\[
\left.
\frac{\partial^nK}
{\partial J_{i_1}\cdots\partial J_{i_n}}
\right|_{J_S=0,J_B=0}
\]
for indices \(i_1,\ldots,i_n\in S\). Hence retained effective cumulants are full connected cumulants with retained external legs.

Because the state space and packet set are finite, every fixed-order expansion contains only finitely many packet assignments. By Theorem 1, any product of retained fields either remains in \(S\), falls into the trivial packet \(H_1\), or lands in \(\partial_nS\subseteq B\). Thus, in the corresponding connected expansion, omitted packets enter only as finite boundary contractions. \(\square\)

This is the finite analog of "integrating out modes": it is marginalization/pushforward plus logarithmic connected projection.

---

## 4. Quadratic renormalization

### Theorem 3. Schur Complement Renormalization Theorem

Let the quadratic part of a finite apex action split over retained and boundary modes:
\[
\phi=\phi_S+\phi_B,
\qquad
\phi_S\in H_S,\quad \phi_B\in H_B.
\]
Suppose the quadratic kernel is
\[
Q=
\begin{pmatrix}
Q_{SS}&Q_{SB}\\
Q_{BS}&Q_{BB}
\end{pmatrix},
\]
with \(Q_{BB}\) invertible. Then eliminating the boundary variables produces the effective quadratic kernel
\[
Q^{\mathrm{eff}}_S
=
Q_{SS}-Q_{SB}Q_{BB}^{-1}Q_{BS}.
\]

**Proof.** The quadratic action is
\[
\Gamma_2(\phi_S,\phi_B)
=
\frac12
\begin{pmatrix}\phi_S\\\phi_B\end{pmatrix}^T
\begin{pmatrix}
Q_{SS}&Q_{SB}\\
Q_{BS}&Q_{BB}
\end{pmatrix}
\begin{pmatrix}\phi_S\\\phi_B\end{pmatrix}.
\]
Expanding,
\[
\Gamma_2
=
\frac12\phi_S^TQ_{SS}\phi_S
+\phi_S^TQ_{SB}\phi_B
+\frac12\phi_B^TQ_{BB}\phi_B.
\]
Since \(Q_{BB}\) is invertible, complete the square:
\[
\frac12\phi_B^TQ_{BB}\phi_B+\phi_S^TQ_{SB}\phi_B
=
\frac12
(\phi_B+Q_{BB}^{-1}Q_{BS}\phi_S)^T
Q_{BB}
(\phi_B+Q_{BB}^{-1}Q_{BS}\phi_S)
-
\frac12\phi_S^TQ_{SB}Q_{BB}^{-1}Q_{BS}\phi_S.
\]
Therefore
\[
\Gamma_2
=
\frac12\phi_S^T
\left(Q_{SS}-Q_{SB}Q_{BB}^{-1}Q_{BS}\right)
\phi_S
+
\frac12
(\phi_B+Q_{BB}^{-1}Q_{BS}\phi_S)^T
Q_{BB}
(\phi_B+Q_{BB}^{-1}Q_{BS}\phi_S).
\]
Gaussian integration over \(\phi_B\), or equivalently substitution of the stationary boundary value
\[
\phi_B^*=-Q_{BB}^{-1}Q_{BS}\phi_S,
\]
leaves only a determinant constant independent of \(\phi_S\). Thus the retained effective kernel is
\[
Q^{\mathrm{eff}}_S
=
Q_{SS}-Q_{SB}Q_{BB}^{-1}Q_{BS}.
\]
\(\square\)

If \(Q\) is a precision/action kernel, the theorem is exactly as written. If one starts from a covariance block, the corresponding statement applies to the inverse kernel.

---

## 5. Finite renormalization closure

### Theorem 4. Finite Renormalization Closure Theorem

Let \(\Omega\) be finite. Let the retained sector be represented by a finite-dimensional observable map
\[
Y_S:\Omega\to\mathbb R^m.
\]
Define
\[
Z_{\mathrm{eff},S}(J)=\mathbb E e^{\langle J,Y_S\rangle},
\qquad
K_{\mathrm{eff},S}(J)=\log Z_{\mathrm{eff},S}(J).
\]
Then \(K_{\mathrm{eff},S}\) is generated by a finite atomic measure on the retained image
\[
Y_S(\Omega)=\{v_1,\ldots,v_q\}\subset\mathbb R^m.
\]
Consequently, all renormalized retained moments and cumulants close inside the finite coordinate algebra
\[
A_S=\mathbb R[z_1,\ldots,z_m]/I(Y_S(\Omega)),
\]
where \(I(Y_S(\Omega))\) is the ideal of polynomials vanishing on the retained image.

For every source direction \(h\in(\mathbb R^m)^*\), the diagonal effective tower
\[
K_{\mathrm{eff},S}(\beta h)
\]
is governed by the finite closure polynomial
\[
P_{S,h}(t)=\prod_{\rho\in h(Y_S(\Omega))}(t-\rho).
\]

**Proof.** Since \(\Omega\) is finite, the retained image is finite:
\[
Y_S(\Omega)=\{v_1,\ldots,v_q\}.
\]
Group states by retained value:
\[
\Omega_\alpha=\{s\in\Omega:Y_S(s)=v_\alpha\},
\qquad
W_\alpha=\sum_{s\in\Omega_\alpha}w_s.
\]
Then \(W_\alpha>0\) and \(\sum_\alpha W_\alpha=1\). The effective partition functional is
\[
Z_{\mathrm{eff},S}(J)
=
\sum_{s\in\Omega}w_s e^{\langle J,Y_S(s)\rangle}.
\]
Grouping by fibers,
\[
Z_{\mathrm{eff},S}(J)
=
\sum_{\alpha=1}^q
W_\alpha e^{\langle J,v_\alpha\rangle}.
\]
Thus boundary integration is the pushforward of the original finite measure to
\[
\nu_S=\sum_{\alpha=1}^qW_\alpha\delta_{v_\alpha}.
\]

Now let
\[
A_S=\mathbb R[z_1,\ldots,z_m]/I(Y_S(\Omega)).
\]
Evaluation identifies \(A_S\) with the coordinate algebra of a finite set, hence a finite-dimensional algebra. Define
\[
L_S(f)=\sum_{\alpha=1}^qW_\alpha f(v_\alpha).
\]
For a multi-index \(\mathbf n=(n_1,\ldots,n_m)\),
\[
\mu_{\mathbf n}^{\mathrm{eff}}
=
\left.\partial_J^{\mathbf n}Z_{\mathrm{eff},S}(J)\right|_{J=0}
=
\sum_{\alpha=1}^qW_\alpha
v_{\alpha,1}^{n_1}\cdots v_{\alpha,m}^{n_m}
=L_S(z^{\mathbf n}).
\]
Thus every retained moment is a linear functional applied to a monomial in the finite algebra \(A_S\).

For a one-source direction \(h\), set
\[
\rho_\alpha=\langle h,v_\alpha\rangle.
\]
Then
\[
Z_{\mathrm{eff},S}(\beta h)
=
\sum_{\alpha=1}^qW_\alpha e^{\beta\rho_\alpha}.
\]
After merging equal \(\rho_\alpha\), this is a finite exponential sum. Let
\[
P_{S,h}(t)=\prod_{\rho\in h(Y_S(\Omega))}(t-\rho).
\]
Then \(P_{S,h}(\rho_\alpha)=0\) for every \(\alpha\). Multiplying by \(\rho_\alpha^n\), summing with weights, and translating to moments gives the finite recurrence for the diagonal effective moment tower. Since
\[
K_{\mathrm{eff},S}=\log Z_{\mathrm{eff},S}
\]
and \(Z_{\mathrm{eff},S}(0)=1\), the effective cumulants are determined by the same finite atomic data. \(\square\)

The closure polynomial after projection is generally \(P_{S,h}\), not necessarily the original scalar \(P_x\). It agrees with or divides an original closure polynomial when the retained observable is a function of the original scalar ledger.

---

## 6. Beta functions as boundary curvature

### Theorem 5. Beta Function as Boundary Curvature Theorem

Fix an interaction order \(n\). Let
\[
S\subseteq S'
\]
be retained packet sectors. Define the discrete beta source from \(S\) to \(S'\) by
\[
\beta^{(n)}_{S\to S'}
=
(\Pi_{S'}-\Pi_S)V_n\big|_{H_S^{\otimes n}}.
\]
Then
\[
\beta^{(n)}_{S\to S'}=0
\]
if and only if no \(n\)-fold boundary packet of \(S\) lies in the newly admitted sector:
\[
\partial_nS\cap(S'\setminus S)=\varnothing.
\]
If \(S'\) contains every possible nontrivial \(n\)-fold output of \(S\), then
\[
\beta^{(n)}_{S\to S'}=0
\quad\Longleftrightarrow\quad
S\text{ is }n\text{-fusion-closed}.
\]

**Proof.** By Theorem 1,
\[
V_n(H_S,\ldots,H_S)
\subseteq
H_S\oplus H_1\oplus\bigoplus_{d\in\partial_nS}H_d.
\]
The operator \(\Pi_{S'}-\Pi_S\) kills packets already in \(S\), kills packets outside \(S'\), and keeps exactly packets in \(S'\setminus S\). Therefore
\[
\beta^{(n)}_{S\to S'}
\]
is supported in
\[
\bigoplus_{d\in\partial_nS\cap(S'\setminus S)}H_d.
\]
If this intersection is empty, the beta source is zero.

Conversely, suppose
\[
\partial_nS\cap(S'\setminus S)\ne\varnothing.
\]
Choose \(d\) in this intersection. By sharpness in Theorem 1, there exist input characters \(\chi_{a_1},\ldots,\chi_{a_n}\in H_S\) such that
\[
\operatorname{cond}(a_1+\cdots+a_n)=d.
\]
Then
\[
V_n(\chi_{a_1},\ldots,\chi_{a_n})
=\chi_{a_1+\cdots+a_n}\in H_d.
\]
Since \(d\in S'\setminus S\), this component is killed by \(\Pi_S\) and kept by \(\Pi_{S'}\). Hence
\[
(\Pi_{S'}-\Pi_S)V_n(\chi_{a_1},\ldots,\chi_{a_n})\ne0,
\]
so the beta source is nonzero.

If \(S'\) contains all possible nontrivial \(n\)-fold outputs of \(S\), the condition becomes
\[
\partial_nS=\varnothing,
\]
which is equivalent to
\[
\operatorname{Fuse}_n(S)\subseteq S\cup\{1\}.
\]
That is exactly \(n\)-fusion closure. \(\square\)

Thus, in this finite setting, couplings run exactly when the projection crosses a conductor-fusion boundary.

---

## 7. Fixed sectors and renormalizability

### Theorem 6. Fixed Sector / Renormalizability Theorem

Fix an interaction order \(n\). A retained sector
\[
H_S=\bigoplus_{d\in S}H_d
\]
is exactly renormalizable under \(n\)-leg apex interactions if and only if \(S\) is \(n\)-fusion-closed:
\[
\operatorname{Fuse}_n(S)\subseteq S\cup\{1\}.
\]
If \(S\) is not \(n\)-fusion-closed, then the minimal exactly renormalizable packet sector containing \(S\) is
\[
H_{\operatorname{Cl}_n(S)}.
\]

**Proof.** Call \(H_S\) exactly renormalizable at order \(n\) if every \(n\)-leg interaction with inputs in \(H_S\) requires no nontrivial packet outside \(H_S\). Equivalently,
\[
(1-\Pi_S)V_n(H_S,\ldots,H_S)=0
\]
modulo \(H_1\).

By Theorem 1,
\[
(1-\Pi_S)V_n(H_S,\ldots,H_S)
\subseteq
\bigoplus_{d\in\partial_nS}H_d,
\]
and this support is sharp. Hence the non-retained component vanishes for all inputs if and only if
\[
\partial_nS=\varnothing.
\]
But
\[
\partial_nS=\operatorname{Fuse}_n(S)\setminus(S\cup\{1\}),
\]
so \(\partial_nS=\varnothing\) is equivalent to
\[
\operatorname{Fuse}_n(S)\subseteq S\cup\{1\}.
\]
Thus exact renormalizability is exactly \(n\)-fusion closure.

Now suppose \(S\) is not closed. Define \(\operatorname{Cl}_n(S)\) as the intersection of all \(n\)-fusion-closed packet sets containing \(S\). The full nontrivial divisor set \(\mathcal D_N\) is finite and closed, so this family is nonempty. Intersections of \(n\)-fusion-closed packet sets are \(n\)-fusion-closed: if inputs lie in an intersection, their fusion support lies in each closed set, hence in the intersection, up to \(H_1\). Therefore \(\operatorname{Cl}_n(S)\) is \(n\)-fusion-closed and contains \(S\).

By the first part, \(H_{\operatorname{Cl}_n(S)}\) is exactly renormalizable. If \(S'\) is any exactly renormalizable packet set containing \(S\), then \(S'\) is \(n\)-fusion-closed, so by definition of the intersection,
\[
\operatorname{Cl}_n(S)\subseteq S'.
\]
Therefore \(H_{\operatorname{Cl}_n(S)}\) is the minimal exactly renormalizable completion. \(\square\)

---

## 8. Universality of completion

### Theorem 7. Universality of Fusion Completion

Fix an interaction order \(n\). Let
\[
C=\operatorname{Cl}_n(S)
\]
be the minimal \(n\)-fusion-closed packet set containing \(S\). Then \(H_C\) is independent of the chosen basis, coordinate projection, Helmert presentation, character representatives, or channel coordinates used to describe \(H_S\). Any renormalization scheme that begins with the same packet set \(S\) and closes all required \(n\)-leg boundary packets produces the same completed sector
\[
H_{\operatorname{Cl}_n(S)}.
\]

**Proof.** Construct the iterative sequence
\[
S_0=S,
\]
\[
S_{k+1}=S_k\cup(\operatorname{Fuse}_n(S_k)\setminus\{1\}).
\]
This construction uses only conductor labels and the conductor-fusion rule. It does not mention a basis of \(H_d\), a Helmert system, a choice of character representatives, or a matrix representation of projection. Since \(\mathcal D_N\) is finite, the sequence stabilizes. Its stable value is \(\operatorname{Cl}_n(S)\).

Now let two schemes begin with the same packet set \(S\). By Theorem 1, both schemes face the same first forced boundary
\[
\partial_nS=\operatorname{Fuse}_n(S)\setminus(S\cup\{1\}).
\]
If they close the theory, both must add those packets. After adding them, both schemes have the same packet set \(S_1\). Repeating the argument inductively, both schemes generate the same sequence \(S_k\), hence the same stable packet set \(C=\operatorname{Cl}_n(S)\).

Different coordinates on \(H_C\) give conjugate tensor presentations of the same multilinear vertex. If \(U:H_C\to H_C\) is an invertible change of basis, the vertex transforms as
\[
V_n^U(u_1,\ldots,u_n)
=
U\,V_n(U^{-1}u_1,\ldots,U^{-1}u_n).
\]
Coupling arrays may change, but closure, boundary support, and renormalizability do not, because the packet set \(C\) is unchanged.

Finally, by Theorem 6, any exactly renormalizable packet set containing \(S\) must be \(n\)-fusion-closed and therefore contains \(\operatorname{Cl}_n(S)\). Thus no coordinate scheme can produce a smaller closed completion. \(\square\)

The universal object is not the projection matrix. It is the fusion-closed packet completion.

---

## 9. The \(N=6\) four-sector model

### Theorem 8. Exact \(N=6\) Four-Sector Renormalization Theorem

Let \(G=\mathbb Z/6\). The nontrivial additive conductor packets are
\[
H_2,\qquad H_3,\qquad H_6.
\]
Write
\[
A_2=H_2,\qquad A_3=H_3,\qquad M=H_6.
\]
For the retained sector
\[
S=\{2,3\},
\qquad
H_S=A_2\oplus A_3,
\]
the cubic conductor-fusion boundary is
\[
\partial_3S=\{6\}.
\]
Therefore any cubic effective theory retaining \(A_2\oplus A_3\) but eliminating \(M\) has a forced boundary correction supported on \(M\).

**Proof.** The characters of \(\mathbb Z/6\) are indexed by \(a\in\mathbb Z/6\), and
\[
\operatorname{cond}(a)=\frac6{\gcd(a,6)}.
\]
Thus
\[
H_1=\operatorname{span}\{\chi_0\},
\]
\[
H_2=\operatorname{span}\{\chi_3\},
\]
\[
H_3=\operatorname{span}\{\chi_2,\chi_4\},
\]
\[
H_6=\operatorname{span}\{\chi_1,\chi_5\}.
\]

Compute cubic products with inputs from \(H_2\oplus H_3\). Character multiplication adds indices modulo \(6\).

For \(H_2H_2H_2\),
\[
3+3+3\equiv3\pmod6,
\]
so the output lies in \(H_2\).

For \(H_2H_2H_3\),
\[
3+3+2\equiv2,
\qquad
3+3+4\equiv4,
\]
so the output lies in \(H_3\).

For \(H_3H_3H_3\), using indices \(2,4\),
\[
2+2+2\equiv0,
\]
\[
2+2+4\equiv2,
\]
\[
2+4+4\equiv4,
\]
\[
4+4+4\equiv0.
\]
Thus the outputs lie in \(H_1\oplus H_3\).

For \(H_2H_3H_3\),
\[
3+2+2\equiv1,
\]
\[
3+2+4\equiv3,
\]
\[
3+4+4\equiv5.
\]
Thus the outputs lie in
\[
H_6\oplus H_2.
\]
Therefore
\[
\operatorname{Fuse}_3(\{2,3\})=\{1,2,3,6\}.
\]
Removing the retained packets \(2,3\) and ignoring the trivial packet \(1\),
\[
\partial_3\{2,3\}
=
\{1,2,3,6\}\setminus(\{2,3\}\cup\{1\})
=\{6\}.
\]
The boundary is sharp because
\[
\chi_3\chi_2\chi_2
=\chi_{3+2+2}
=\chi_1\in H_6.
\]
Thus the full-conductor packet \(M=H_6\) is forced as the cubic boundary of \(A_2\oplus A_3\). If \(M\) is eliminated, its effect must reappear as an exact finite boundary correction in the retained effective action. \(\square\)

This is the theorem-level form of the application slogan: the residual \(M\)-sector is not an arbitrary fourth ingredient. It is the forced cubic boundary of the two retained prime packets.

---

## 10. The finite simplicial RG

### Theorem 9. The Fusion-Closure Renormalization Group Theorem

Fix an interaction order \(n\). For each packet set
\[
S\subseteq\mathcal D_N,
\]
let \(\operatorname{Cl}_n(S)\) be the smallest \(n\)-fusion-closed packet set containing \(S\). Then
\[
S\mapsto\operatorname{Cl}_n(S)
\]
is an extensive, monotone, idempotent closure operator on the finite packet lattice \(\mathcal P(\mathcal D_N)\). Its fixed points are exactly the exactly renormalizable packet sectors.

The discrete boundary-adjunction flow
\[
S_{k+1}=S_k\cup\partial_nS_k
\]
terminates after finitely many steps at
\[
\operatorname{Cl}_n(S_0).
\]
Moreover, two projected sectors \(S,S'\) lie in the same finite simplicial universality class if and only if
\[
\operatorname{Cl}_n(S)=\operatorname{Cl}_n(S').
\]

**Proof.** Since \(\mathcal D_N\) is finite and itself \(n\)-fusion-closed, the family of \(n\)-fusion-closed packet sets containing \(S\) is nonempty. Define
\[
\operatorname{Cl}_n(S)
=
\bigcap
\{C\subseteq\mathcal D_N:
S\subseteq C,\ C\text{ is }n\text{-fusion-closed}\}.
\]
Intersections of \(n\)-fusion-closed sets are \(n\)-fusion-closed, so this is the smallest closed packet set containing \(S\).

Extensivity is immediate:
\[
S\subseteq\operatorname{Cl}_n(S),
\]
because every set in the intersection contains \(S\).

For monotonicity, suppose \(S\subseteq S'\). Every closed set containing \(S'\) also contains \(S\). Thus the closed supersets of \(S'\) form a subfamily of the closed supersets of \(S\). Intersecting over a smaller family gives a larger or equal result, hence
\[
\operatorname{Cl}_n(S)\subseteq\operatorname{Cl}_n(S').
\]

For idempotence, \(\operatorname{Cl}_n(S)\) is already closed. Therefore its smallest closed superset is itself:
\[
\operatorname{Cl}_n(\operatorname{Cl}_n(S))
=
\operatorname{Cl}_n(S).
\]
Thus \(\operatorname{Cl}_n\) is a closure operator.

The fixed points are exactly the closed sets:
\[
\operatorname{Cl}_n(S)=S
\quad\Longleftrightarrow\quad
S\text{ is }n\text{-fusion-closed}.
\]
By Theorem 6, this is equivalent to exact renormalizability of \(H_S\).

Now define the flow
\[
S_{k+1}=S_k\cup\partial_nS_k
=
S_k\cup(\operatorname{Fuse}_n(S_k)\setminus\{1\}).
\]
This gives an increasing chain
\[
S_0\subseteq S_1\subseteq S_2\subseteq\cdots.
\]
Since \(\mathcal D_N\) is finite, the chain stabilizes. Let the stable value be \(S_\infty\). At stabilization,
\[
S_\infty
=
S_\infty\cup(\operatorname{Fuse}_n(S_\infty)\setminus\{1\}),
\]
so
\[
\operatorname{Fuse}_n(S_\infty)\subseteq S_\infty\cup\{1\}.
\]
Thus \(S_\infty\) is closed and contains \(S_0\), so
\[
\operatorname{Cl}_n(S_0)\subseteq S_\infty.
\]

Conversely, let \(C\) be any \(n\)-fusion-closed set containing \(S_0\). We prove by induction that \(S_k\subseteq C\) for all \(k\). This holds for \(k=0\). If \(S_k\subseteq C\), then
\[
\operatorname{Fuse}_n(S_k)\subseteq\operatorname{Fuse}_n(C)
\subseteq C\cup\{1\}.
\]
Therefore
\[
S_{k+1}
=
S_k\cup(\operatorname{Fuse}_n(S_k)\setminus\{1\})
\subseteq C.
\]
Hence \(S_\infty\subseteq C\) for every closed \(C\) containing \(S_0\). Taking the intersection over all such \(C\),
\[
S_\infty\subseteq\operatorname{Cl}_n(S_0).
\]
Combining inclusions,
\[
S_\infty=\operatorname{Cl}_n(S_0).
\]

Finally define
\[
S\sim S'
\quad\Longleftrightarrow\quad
\operatorname{Cl}_n(S)=\operatorname{Cl}_n(S').
\]
This is an equivalence relation because equality is reflexive, symmetric, and transitive. By Theorem 7, sectors with the same closure have the same minimal exactly renormalizable completion. Conversely, if two sectors have the same universal completed sector, their closures are equal. Thus finite simplicial universality classes are precisely the fibers of the closure operator. \(\square\)

This is the capstone:
\[
\boxed{
\text{finite RG}=\text{the closure operator generated by conductor fusion}.
}
\]

---

## 11. What T13 does not claim

1. **It does not claim to be continuum Wilsonian QFT.** T13 is finite, arithmetic, and simplicial. Its value is exactness and structural clarity, not direct continuum dynamics.

2. **It does not claim all residuals are physical forces.** It proves that projected apex residuals are boundary sources. Physical interpretation requires an application map.

3. **It does not remove coordinate dependence of coefficients.** Numerical coupling arrays change under basis transformations. The invariant object is the packet closure.

4. **It does not imply every projection should be closed.** Some useful models deliberately truncate. The theorem identifies the price of truncation.

5. **It does not say boundary integration is always numerically stable.** Finite exactness is algebraic. Conditioning, estimation, and empirical robustness are separate analytic issues.

6. **It does not replace T12.** T13 says which packets must be included; T12 says why the induced order towers remain finite.

---

## 12. Forward doors

### 12.1 Multiscale packet filtrations

The conductor lattice can be ordered by divisibility, prime depth, or application-specific packet energy. Different filtrations produce different finite RG paths, but all paths terminate at the same fusion closure when they begin from the same \(S\).

### 12.2 Exact counterterm calculus

The boundary source
\[
(1-\Pi_S)V_n
\]
can be read as a finite counterterm generator. The next technical layer is an explicit counterterm algebra: which retained tensors must be added to reproduce eliminated boundary packets to a chosen order?

### 12.3 Multiplicative renormalization

T8 suggests replacing additive characters by Dirichlet characters. Then conductor fusion becomes multiplicative conductor interaction, and the RG fixed points become closed sets in a Dirichlet conductor lattice.

### 12.4 AI representation closure

A feature subspace that is not closed under its interaction algebra must emit residuals. In AI language:
\[
\text{feature residual}=\text{interaction boundary}.
\]
The fusion-closure test becomes a mathematical metaphor and possible diagnostic for representation sufficiency.

### 12.5 Noncommutative effective sectors

The commutative packet algebra should have a density-matrix analog. Boundary integration would then become finite operator-algebra compression, with Schur complements and conditional expectations replacing scalar packet projections.

---

## 13. Coda

T11 found the boundary. T12 proved the induced towers are finite. T13 turns both facts into renormalization.

The sequence of ideas is now:
\[
\text{project}
\quad\Longrightarrow\quad
\text{boundary source}
\quad\Longrightarrow\quad
\text{finite effective correction}
\quad\Longrightarrow\quad
\text{fusion closure}
\quad\Longrightarrow\quad
\text{RG fixed point}.
\]

The paper's final sentence can be said without metaphor:
\[
\boxed{
\text{A projected finite apex theory is exactly renormalizable iff its retained packet set is fusion-closed.}
}
\]

---

## References and anchors

This draft uses standard facts from:

1. finite Fourier analysis on \(\mathbb Z/N\);
2. conductor packet decompositions;
3. projection onto direct-sum packet sectors;
4. Schur complements of block quadratic forms;
5. finite pushforward measures and cumulant generating functions;
6. coordinate algebras of finite point sets;
7. closure operators on finite lattices;
8. the preceding lamed-series papers T0-T12.

Internal anchors:

| Object | Location |
|---|---|
| boundary support | Theorem 1 |
| exact marginalization | Theorem 2 |
| quadratic Schur complement | Theorem 3 |
| finite effective closure | Theorem 4 |
| beta source | Theorem 5 |
| renormalizability criterion | Theorem 6 |
| universal completion | Theorem 7 |
| \(N=6\) four-sector model | Theorem 8 |
| closure-operator RG | Theorem 9 |

