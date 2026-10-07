# The Bigrading Probe: Order and Degree as Two Axes of the Polynomial-Form Bicomplex

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Probe note — June 2026*

**Question.** The simplicial-frame program runs two graded towers on the zero-sum hyperplane $H$: the **order axis** — the cumulant tower $T^{(n)}=\nabla^n\varphi$ (symmetric $n$-tensors, $\varphi=\sum_i p_i\log p_i$), with order-$2$ the Fisher metric and order-$3$ the Amari–Chentsov cubic; and the **degree axis** — the Hodge complex on the simplex ($k$-cochains, Laplacians $L_k$, Betti numbers $\beta_k$). The integration keystone found that a single integer $N$ is the eigenvalue of the order-$2$ rung *and* of every degree-$k$ Hodge Laplacian. Are the two towers two coordinates of one bigraded object? This note answers yes, identifies the object, and localizes precisely where the shared eigenvalue $N$ does and does not extend. Every claim is exact-certified in `empirical_integration/cert_bigrading_probe.py` (37/37 green).

---

## 1. The two axes, named correctly

- **Order axis = the symmetric algebra.** The cumulant $T^{(n)}=\nabla^n\varphi$ is a totally symmetric $n$-covariant tensor; under the classical isomorphism $\mathrm{Sym}^n(H^*)\cong\{\text{degree-}n\text{ homogeneous polynomials}\}$ it is a degree-$n$ polynomial. The order tower is therefore the symmetric/polynomial grading, indexed by $n$.
- **Degree axis = the exterior algebra.** The Hodge tower lives on $k$-cochains $\cong\Lambda^k(H^*)$, the antisymmetric grading, indexed by the form degree $k$.

These are the two halves of the $S+A$ division of labor (keystone §2): symmetric (order) versus antisymmetric (degree). The natural object carrying both gradings at once is the space of **polynomial differential forms**
$$P_n\Lambda^k \;=\; \mathrm{Sym}^n(H^*)\otimes\Lambda^k(H^*),$$
bigraded by $(n,k)$ = (polynomial/order degree, form/Hodge degree). This is exactly the bigraded space of finite element exterior calculus (FEEC), so the probe also reconnects to the DEC/FEEC bridge of Paper 01b §10.

## 2. The bigraded object and its unifying identity

$P_\bullet\Lambda^\bullet$ carries two grade-shifting differentials:
- the **de Rham differential** $d$, lowering polynomial degree and raising form degree, $d:P_n\Lambda^k\to P_{n-1}\Lambda^{k+1}$;
- the **Koszul/Euler contraction** $\kappa=\iota_E$ (contraction with the Euler field $E=\sum_i x_i\partial_i$), raising polynomial degree and lowering form degree, $\kappa:P_n\Lambda^k\to P_{n+1}\Lambda^{k-1}$.

**Theorem 2.1 (the bigrading is the Cartan bicomplex).** *On $P_n\Lambda^k$,*
$$d\,\kappa+\kappa\,d=(n+k)\,\mathrm{Id},\qquad d^2=0,\qquad \kappa^2=0.$$
*That is, $d$ and $\kappa$ are the two ways to move through the $(n,k)$ grid; their anticommutator is Cartan's magic formula for the Lie derivative along the Euler field, which acts on $P_n\Lambda^k$ as multiplication by the total degree $n+k$. The complex is exact off $(0,0)$ (the Koszul/Poincaré lemma).*

*Proof.* $d\kappa+\kappa d=\mathcal L_E$ is Cartan's identity; $\mathcal L_E$ scales a monomial $k$-form of polynomial degree $n$ by $n+k$. Verified directly for $d=3$ (the $N=4$ hyperplane), all $n\le3$, $k\le3$, on every basis monomial form, in `cert_bigrading_probe.py` block C, together with $d^2=\kappa^2=0$. $\square$

So the answer to the probe is **yes**: order and degree are the two coordinates of the polynomial-form bicomplex $P_n\Lambda^k$, with $d$ and $\kappa$ shifting along the two axes and conserved total degree $n+k$ the unifying grade.

**The two towers as slices.** The cumulant/order tower is the $k=0$ column $P_n\Lambda^0$ (polynomial functions $\cong$ symmetric tensors). The Hodge/degree tower is the form-degree axis $\Lambda^k$ (its simplicial realization is the cochain complex; the lowest-order, Whitney, level $r=1$). The de Rham $d$ is the bridge: $d:P_n\Lambda^0\to P_{n-1}\Lambda^1$ carries the order column into the degree row (certified). The towers are not parallel and independent — they are the column and the row of one bicomplex, joined at the de Rham differential.

## 3. Where the universal eigenvalue $N$ lives — and where it does not

The bigrading is real, but the eigenvalue $N$ that motivated the question is **not** a bigrading invariant. The honest localization:

**Proposition 3.1 (degree axis is $N$-flat; order axis grows).**
1. *(Degree.) The combinatorial Hodge Laplacian $L_k$ on the filled $(N-1)$-simplex has nonzero spectrum identically $N$ for every degree $k$ (certified $N=4,5,6$, all $k$). The eigenvalue $N$ is the degree-axis constant, forced by the completeness of $K_N$.*
2. *(Order.) The order-$n$ cumulant at the uniform point is $\nabla^n\varphi|_{p_*}=(-1)^n(n-2)!\,N^{\,n-1}$ (certified $N=4,5,6$, $n=2..6$): $N,\,-N^2,\,2N^3,\,-6N^4,\dots$ — factorial-$N$ growth, not flat.*

**Corollary 3.2 (one shared rung).** *The two towers coincide at exactly one bidegree: the corner $(n,k)=(2,0)$, where the order-$2$ cumulant equals the degree-$0$ graph Laplacian $L_0=M=NI-J$, eigenvalue $N$. Above the corner they diverge — the order axis as $N^{n-1}(n-2)!$, the degree axis flat at $N$.*

So the "universal eigenvalue $N$" is the **degree-axis (Hodge/Whitney) eigenvalue**, a consequence of $K_N$ completeness; it appears at the base of the order axis (order $2$) because the Fisher metric there *is* the graph Laplacian, but it does not climb the order axis. The unifying invariant of the bicomplex is the **total degree $n+k$** (Theorem 2.1), not $N$.

## 4. Verdict

**Affirmative core (certified).** Order and degree are two coordinates of one bigraded object: the polynomial-differential-form bicomplex $P_n\Lambda^k$ (the FEEC / Cartan–Koszul double complex over $H$), with de Rham $d$ and Euler contraction $\kappa$ as the grade-shifting differentials, $d\kappa+\kappa d=(n+k)\mathrm{Id}$, and the cumulant tower ($k=0$ column) joined to the Hodge tower (form-degree axis) by $d$.

**Refuted over-strong form (certified).** There is no single operator with eigenvalue $N$ across the whole bicomplex. $N$ is the degree-axis Hodge eigenvalue (from $K_N$ completeness); the order axis carries $N^{n-1}(n-2)!$; the towers meet only at the graph-Laplacian corner $(2,0)$.

**Net.** The bigrading question reduces to a classical, exactly-solved structure — polynomial differential forms with Cartan's identity — and the program's two towers are its symmetric column and exterior row. The "universal $N$" is honestly relocated from "a bigrading invariant" (false) to "the degree-axis eigenvalue meeting the order axis at its base" (true). This is a structural reduction, not a new force: it says the cumulant tower and the Hodge tower were never going to merge into one $N$-eigenvalue object, but they do sit inside one bicomplex, and exactly one rung is shared.

**Program reading.** The two blind spots correspond to moving along the two axes of $P_n\Lambda^k$: the conductor blind spot is failing to climb the order ($n$) axis past $2$; the irreversible blind spot is failing to leave the symmetric column ($k=0$) for the exterior ($k\ge1$) part. They are distinct moves in one bicomplex, which is why the program needs both a higher-order probe (cumulants) and a non-self-adjoint probe (predictor) — neither subsumes the other.

---

## Appendix: certificate

`empirical_integration/cert_bigrading_probe.py` (numpy+sympy, exact, 37/37 green):
- **A.** $L_k$ nonzero spectrum $=N$ on the filled $(N-1)$-simplex, all $k$, $N=4,5,6$.
- **B.** $\nabla^n\varphi|_{p_*}=(-1)^n(n-2)!N^{n-1}$, $N=4,5,6$, $n=2..6$.
- **C.** $d\kappa+\kappa d=(n+k)\mathrm{Id}$, $d^2=0$, $\kappa^2=0$ on $P_n\Lambda^k$ ($d=3$); de Rham bridge $P_n\Lambda^0\to\Lambda^1$.
- **D.** corner $(2,0)=N=L_0$; order-$3=-N^2\ne N$ (divergence), $N=4,5,6$.

---

*[End of probe note.]*
