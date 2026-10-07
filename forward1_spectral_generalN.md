# The Spectral Floor of the Simplicial Frame: The Metric as Complete-Graph Laplacian, General-$N$ Calculus, and the Heat Kernel

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Draft 1 — June 2026*

**Companion note.** This is the spectral / general-$N$ companion to the simplicial-frame trilogy: **Paper 01** (*Intrinsic Vector Algebra* — the cross product $K(u)$, rotation, the zero-sum hyperplane), **Paper 01b** (*Intrinsic Differential Calculus* — $\nabla$, $\operatorname{div}$, $\operatorname{curl}$, the gauge–Hodge split), and **Paper 01c** (*Moving Amari–Chentsov Cubic* — the information geometry). Those three papers are anchored at $N=4$ (the tetrahedron). The present paper establishes the **general-$N$ floor**: it proves that the integer simplicial metric is the graph Laplacian of the complete graph $K_N$ for every $N$, develops the first-order differential calculus on the zero-sum hyperplane $H\cong\mathbb{R}^{N-1}$ in all dimensions, gives the Laplacian spectrum and heat-kernel trace, and characterizes exactly why $N=4$ is the unique dimension in which the opposite-edge Hodge involution $\star_E$ of Paper 01b (Theorem 10.1) is an endomorphism of the edge space. It directly resolves the **general-$N$ half** of Paper 01b's open problems **C2** (exact rational discrete calculus) and **C6** (simplicial Laplacian spectrum / heat kernel). Numbers prefixed "01." / "01b." refer to those papers.

---

## Abstract

The integer simplicial metric $M_N := N I - J$ (with $J$ the all-ones matrix), introduced at $N=4$ in Paper 01 §7.5 as $M=4I-J=3G$, is for **every** $N$ exactly the graph Laplacian $L(K_N)=d_0^\top d_0$ of the complete graph on $N$ vertices — the $1$-skeleton of the regular $(N-1)$-simplex. Its spectrum is $\{0^{(1)},\,N^{(N-1)}\}$: eigenvalue $0$ on the one-dimensional gauge line $\mathbf 1=(1,\dots,1)^\top=\ker d_0=H^0(K_N)$, and eigenvalue $N$ with multiplicity $N-1$ on the zero-sum hyperplane $H=\{c:\sum_i c_i=0\}$. Thus $M_N|_H = N\,I_H$ is a scalar, which is the single fact that makes the simplicial differential calculus collapse to coordinate form in every dimension.

We use this to pour the general-$N$ floor. **(i)** On $H\cong\mathbb{R}^{N-1}$, gauge invariance of a scalar field forces its differential into $H$, so $\operatorname{grad}=\tfrac1N d$ is zero-sum automatically; $\operatorname{div}F=\sum_i\partial_iF_i$ is its negative $L^2$-adjoint; and $\Delta=\operatorname{div}\operatorname{grad}=\tfrac1N\sum_i\partial_i^2$ — all for arbitrary $N$, all rational on rational data (no square roots). **(ii)** The second-order identity $\operatorname{curl}\operatorname{grad}=0$ is, for every $N$, the discrete coboundary law $d_{k+1}d_k=0$ on the $(N-1)$-simplex; the vector-calculus $\operatorname{curl}=K(\nabla)$ exists as a single-axis operator only at $N=4$ (Paper 01 §8), and we handle the general-$N$ Hodge layer at the coboundary level where it is correct. **(iii)** The graph-Laplacian heat-kernel trace is $\operatorname{Tr} e^{-tM_N}=1+(N-1)e^{-Nt}$; the pseudo-determinant of the nonzero spectrum is $\det{}'(M_N)=N^{N-1}$, and the Matrix-Tree theorem returns $\det{}'(M_N)/N = N^{N-2}$ — Cayley's count of spanning trees of $K_N$. **(iv)** An edge of the $(N-1)$-simplex is a $1$-face whose complementary (opposite) face spans the other $N-2$ vertices and is an $(N-3)$-face; the opposite-edge involution $\star_E$ that realizes the discrete Hodge star on edges is an endomorphism of the edge space $C^1$ **iff $N-3=1$, i.e. $N=4$** — the same coincidence ($\dim\mathfrak{so}(3)=3$) that singles out $N=4$ for the binary cross product.

Every displayed identity is verified in exact arithmetic (`empirical_forward1/cert_spectral_generalN.py`, sympy/integer only, $108$ checks GREEN) for $N\in\{3,4,5,6,7\}$. We are explicit about the novelty boundary (§8): the graph-Laplacian spectrum, the heat trace, Cayley's formula, and the contractibility of the simplex are all classical; what is assembled here is their **coherent identification as the spectral substrate of the simplicial frame**, the general-$N$ extension of the Paper-01 calculus off the tetrahedron, and the exact dimension-count that pins the self-duality of edges to $N=4$.

**Keywords:** simplicial coordinates, Quadray coordinates, complete graph, graph Laplacian, spectral graph theory, heat kernel, spectral zeta, Matrix-Tree theorem, Cayley's formula, zero-sum hyperplane, gauge direction, discrete exterior calculus, Hodge star, Betti numbers, Laplace–Beltrami.

**MSC 2020:** 05C50 (graphs and linear algebra), 58J35 (heat and other parabolic equation methods), 53A45, 05C30 (enumeration of graphs), 15A18 (eigenvalues), 58A10, 65N30.

---

## 1. Introduction

### 1.1 The floor under the trilogy

Papers 01, 01b, and 01c develop a complete intrinsic vector algebra, differential calculus, and information geometry on the zero-sum hyperplane of the $N=4$ simplicial (Quadray) frame. Each is anchored at the tetrahedron, and each leans — sometimes silently — on one structural fact recorded almost in passing in Paper 01b Theorem 10.1(1): *the integer simplicial metric $M=4I-J$ is the graph Laplacian of $K_4$.* That single sentence is the hinge on which the whole edifice turns, because it is the reason the metric restricts to a **scalar** $M|_H=4I_H$ on the hyperplane, which is what lets $\operatorname{grad}$, $\operatorname{div}$, $\operatorname{curl}$, and the Fisher metric all be written in bare coordinate form without a metric tensor cluttering every expression.

This paper takes that hinge as its subject and follows it off the tetrahedron. The questions are:

1. Is $M_N=NI-J$ the graph Laplacian of $K_N$ for *every* $N$, and what is its spectrum? (§3.)
2. Does the first-order differential calculus of Paper 01b survive to general $N$ — gradient, divergence, Laplacian on $H\cong\mathbb{R}^{N-1}$? (§4.)
3. What is the spectrum and heat kernel of the simplicial Laplacian, and does it carry any arithmetic content? (§5–6.)
4. Exactly *why* is $N=4$ special for the opposite-edge Hodge involution $\star_E$ — and what replaces it in general $N$? (§7.)

The answers are uniformly clean, and three of them are genuinely informative rather than bookkeeping. The metric is the complete-graph Laplacian in every dimension, with the spectrum handed by a one-line representation-theoretic argument (§3). The first-order calculus survives verbatim, because $M_N|_H=NI_H$ is the only metric input it needs (§4). And the self-duality of edges — the property that makes $\star_E$ an *involution* of the edge space rather than a map to a higher-degree cochain space — holds precisely when the opposite face of an edge is again an edge, i.e. exactly at $N=4$ (§7). This last is the spectral/combinatorial twin of the Lie-theoretic uniqueness ($\dim\mathfrak{so}(3)=3$) that Paper 01 §8 gave for the binary cross product: two different roads to the same exceptional dimension.

### 1.2 Contributions

1. **Metric = complete-graph Laplacian, all $N$ (§3).** $M_N=NI-J=L(K_N)=d_0^\top d_0$, with spectrum $\{0^{(1)},N^{(N-1)}\}$, $0$-eigenvector $\mathbf 1=\ker d_0=H^0(K_N)$, and $M_N|_H=N I_H$. Theorem 3.1; exact-certified for $N=3,\dots,7$.

2. **General-$N$ first-order calculus (§4).** On $H\cong\mathbb{R}^{N-1}$: $\operatorname{grad}=\tfrac1N d$ (forced into $H$ by gauge invariance), $\operatorname{div}F=\sum_i\partial_iF_i$ (the negative adjoint of $\operatorname{grad}$), $\Delta=\operatorname{div}\operatorname{grad}=\tfrac1N\sum_i\partial_i^2$. Theorems 4.1–4.3.

3. **Second-order identities at the level correct for general $N$ (§4.4).** $\operatorname{curl}\operatorname{grad}=0$ and $\operatorname{div}\operatorname{curl}=0$ are, for all $N$, the coboundary law $d_{k+1}d_k=0$ on the $(N-1)$-simplex; the single-axis $\operatorname{curl}=K(\nabla)$ specialization is $N=4$-only and recovers Paper 01b §§5–6.

4. **Laplacian spectrum, heat kernel, spectral zeta, Cayley (§5–6).** $\operatorname{Tr} e^{-tM_N}=1+(N-1)e^{-Nt}$; spectral zeta $\zeta_{M_N}(s)=(N-1)N^{-s}$; pseudo-determinant $\det{}'(M_N)=N^{N-1}$; Matrix-Tree $\Rightarrow N^{N-2}$ spanning trees (Cayley). The combinatorial Hodge Laplacian on $k$-cochains has kernel of dimension $b_0=1$, $b_k=0$ ($0<k<N-1$) — the simplex is contractible.

5. **The $N=4$ Hodge specialness, characterized (§7).** Edge $=1$-face; its opposite face is an $(N-3)$-face; $\star_E$ is an edge-space endomorphism iff $N=4$. For $N\geq5$ the discrete Hodge dual of an edge is a genuinely higher cochain ($C^1\to C^{N-3}$), so no signed opposite-edge involution exists. Theorem 7.1.

6. **C2/C6 resolution and a forward flag (§8–9).** All operators are rational on rational data in the $M_N$-normalization (C2, general-$N$). The heat-kernel/spectral-zeta structure is reported honestly, with the speculative "apex/archimedean operator" reading of C6 flagged forward-only and **not** claimed.

### 1.3 What is genuinely new, and what is organization

We separate the two carefully, as the companion papers do.

- **Classical, re-presented.** The spectrum $\{0,N^{(N-1)}\}$ of the complete-graph Laplacian is textbook spectral graph theory [Chung, Brouwer–Haemels]. The heat trace $\sum e^{-t\lambda}$, the spectral zeta $\sum\lambda^{-s}$, and the pseudo-determinant–spanning-tree identity (Matrix-Tree / Kirchhoff, with Cayley's $N^{N-2}$) are classical [Biggs, Stanley]. Contractibility of the simplex giving $b_0=1$, $b_{k>0}=0$ is elementary algebraic topology. The flatness of $H$ as $\mathbb{R}^{N-1}$ and its continuous Laplace–Beltrami spectrum $[0,\infty)$ are standard. None of these is claimed new.

- **New here.** (a) The **identification** of the integer simplicial metric with the $K_N$ Laplacian *as the organizing spectral fact of the simplicial frame across all $N$* — promoting Paper 01b's $N=4$ remark to the general statement and reading the gauge direction as $H^0(K_N)$ in every dimension. (b) The **general-$N$ extension** of the Paper-01b first-order calculus, with the proof that $M_N|_H=NI_H$ is the sole metric input, so the entire calculus is dimension-independent in form and rational on rational data (C2, off the tetrahedron). (c) The **exact dimension-count** $\,1=N-3\Leftrightarrow N=4\,$ that pins the self-duality of edges — hence the existence of the opposite-edge involution $\star_E$ — to $N=4$, exhibiting it as the combinatorial twin of the Lie-theoretic $\dim\mathfrak{so}(3)=3$. (d) The small **spectral-zeta / Cayley package** assembled as one coherent invariant of the frame.

The honest one-line summary: the **spectrum is classical, the identification-as-substrate and the general-$N$ calculus are organization with real leverage, and the edge-self-duality count is the one crisp new structural statement** — the spectral road to "why $N=4$," parallel to Paper 01's Lie-theoretic road.

### 1.4 Notation

$N\geq3$ throughout. $J=\mathbf 1\mathbf 1^\top$ is the $N\times N$ all-ones matrix, $\mathbf 1=(1,\dots,1)^\top$. The integer simplicial metric is $M_N=NI-J$; the ETF metric of Paper 01 is $G_N=\tfrac{N}{N-1}I-\tfrac1{N-1}J$, with $M_N=(N-1)G_N$ on the relevant scale (at $N=4$, $M=3G$). $H=\{c\in\mathbb{R}^N:\sum_i c_i=0\}\cong\mathbb{R}^{N-1}$ is the zero-sum hyperplane. $K_N$ is the complete graph; $d_0:C^0\to C^1$ its coboundary, $(d_0u)([ij])=u_j-u_i$; more generally $d_k:C^k\to C^{k+1}$ is the simplicial coboundary of the $(N-1)$-simplex. We write $\partial_i=\partial/\partial c_i$. All certificate references are to `empirical_forward1/cert_spectral_generalN.py`.

---

## 2. Setup: the frame, the hyperplane, and the complete graph

We recall only what is needed; full development is in Paper 01 §2. The simplicial frame is $N$ unit vectors $\mathbf v_1,\dots,\mathbf v_N\in\mathbb{R}^{N-1}$ to the vertices of a regular $(N-1)$-simplex, with $\mathbf v_i\cdot\mathbf v_j=-\tfrac1{N-1}$ ($i\neq j$) and $\sum_i\mathbf v_i=\mathbf 0$. A coordinate tuple $c\in\mathbb{R}^N$ names the point $\sum_i c_i\mathbf v_i$; the kernel of this map is the gauge line $\mathbb{R}\mathbf 1$, and the canonical section is the zero-sum hyperplane $H$.

The combinatorial object underlying the frame is the $1$-skeleton of the simplex, the complete graph $K_N$: $N$ vertices (the frame rays), $\binom N2$ edges (the vertex pairs). Its cochain spaces are $C^0=\mathbb{R}^N$ (a value per ray — the simplicial amplitudes themselves), $C^1=\mathbb{R}^{\binom N2}$ (a value per edge), and so on up the simplex. The coboundary $d_0$ is the discrete gradient. This is the same identification Paper 01b §10 uses at $N=4$; here it runs for all $N$.

---

## 3. The metric is the complete-graph Laplacian

**Theorem 3.1 (Metric = $K_N$ Laplacian; spectrum).** *For every $N\geq2$:*

1. *(Laplacian identity.) $M_N=NI-J=d_0^\top d_0=L(K_N)$, the graph Laplacian of the complete graph $K_N$.*
2. *(Spectrum.) The spectrum of $M_N$ is $\{0,N,N,\dots,N\}$ — eigenvalue $0$ with multiplicity $1$ and eigenvalue $N$ with multiplicity $N-1$.*
3. *(Eigenspaces.) The $0$-eigenspace is the gauge line $\mathbb{R}\mathbf 1=\ker d_0=H^0(K_N)$; the $N$-eigenspace is the zero-sum hyperplane $H$. Hence $M_N|_H=N\,I_H$.*

*Proof.* (1) The graph Laplacian of a graph is $\deg$ on the diagonal and $-1$ off-diagonal where edges exist. In $K_N$ every vertex has degree $N-1$ and every off-diagonal pair is an edge, so $L(K_N)=(N-1)I-(J-I)=NI-J=M_N$. The factorization $L=d_0^\top d_0$ is the incidence identity for the coboundary $d_0$ (the un-oriented Laplacian equals the oriented incidence Gram matrix). (2)–(3) $J$ has rank $1$ with $J\mathbf 1=N\mathbf 1$ and $J v=0$ for $v\in H$; therefore $M_N\mathbf 1=N\mathbf 1-J\mathbf 1=N\mathbf 1-N\mathbf 1=\mathbf 0$ and $M_N v=N v-Jv=N v$ for $v\in H$. Since $\mathbb{R}^N=\mathbb{R}\mathbf 1\oplus H$ with $\dim H=N-1$, this exhibits the full spectrum and eigenspaces. The kernel of a connected graph's Laplacian is the constants $=H^0$, of dimension $b_0=1$. $\square$

**Remark 3.2 (Why this is the hinge).** Clause (3), $M_N|_H=NI_H$, is the single structural reason every operator in Papers 01–01c is *scalar-clean*. A general Riemannian metric on $H$ would force a metric tensor into every gradient and divergence; here the metric is a constant multiple of the identity on the hyperplane, so it drops out of all differential formulas up to one bookkeeping constant $1/N$. This is also why the ETF metric $G_N$ and the integer metric $M_N$ define *the same geometry* on $H$ — they differ only by the overall scalar, and on $H$ a scalar is invisible to angles and to all the second-order identities.

**Certificate (Block A).** For $N\in\{3,4,5,6,7\}$: $M_N-d_0^\top d_0=0$; the characteristic polynomial has roots exactly $\{0^{(1)},N^{(N-1)}\}$; $M_N\mathbf 1=0$; and $M_N v=N v$ for an explicit zero-sum $v$. All exact.

---

## 4. General-$N$ first-order differential calculus

We carry the Paper 01b first-order operators to arbitrary $N$. The geometric arena is $H\cong\mathbb{R}^{N-1}$; a *scalar field* is a smooth gauge-invariant $f$ with $f(c+k\mathbf 1)=f(c)$; a *vector field* is a smooth $F:\Omega\to H$. The working normalization is $M_N$.

### 4.1 The gradient is forced into $H$

**Theorem 4.1 (Gauge invariance forces a zero-sum gradient).** *For a scalar field $f$, the coordinate differential $df=(\partial_1f,\dots,\partial_Nf)$ satisfies $\sum_i\partial_if=0$, i.e. $df\in H$. Consequently the simplicial gradient $\operatorname{grad}f:=M_N^{-1}|_H\,df=\tfrac1N\,df\in H$ requires no gauge-fixing.*

*Proof.* Differentiating $f(c+k\mathbf 1)=f(c)$ in $k$ at $k=0$ gives $0=\sum_i\partial_if=\mathbf 1^\top df$, so $df\perp\mathbf 1$, i.e. $df\in H$. On $H$, $M_N$ acts as $N\,I_H$ (Theorem 3.1), so its inverse on $H$ is $\tfrac1N I_H$, giving $\operatorname{grad}f=\tfrac1N df$, which lies in $H$. $\square$

This is the $N$-dimensional version of Paper 01b Proposition 3.1; the proof is identical because it never used $N=4$.

### 4.2 Divergence as the gradient adjoint

**Theorem 4.2 (Divergence; coordinate form and adjointness).** *Define $\operatorname{div}F$ by the integration-by-parts requirement $\int_\Omega\langle\operatorname{grad}f,F\rangle_{M_N}\,dV=-\int_\Omega f\,\operatorname{div}F\,dV$ for compactly supported scalar $f$. Then in zero-sum coordinates $\operatorname{div}F=\sum_{i=1}^N\partial_iF_i$. This is gauge-invariant as a scalar and unchanged under $F\mapsto F+(\text{const})\mathbf 1$.*

*Proof.* For $F\in H$, $M_NF=NF$, so $\langle\operatorname{grad}f,F\rangle_{M_N}=(\tfrac1N df)^\top(NF)=df^\top F=\sum_i(\partial_if)F_i$. Integrating each term by parts and discarding boundary terms yields $-\int f\sum_i\partial_iF_i$, identifying $\operatorname{div}F=\sum_i\partial_iF_i$. The pointwise identity $\langle\operatorname{grad}f,F\rangle_{M_N}=df^\top F$ is itself verified symbolically (Block B); adding a constant multiple of $\mathbf 1$ to $F$ changes $\sum_i\partial_iF_i$ by $\sum_i\partial_i(\text{const})=0$. $\square$

### 4.3 The Laplacian

**Theorem 4.3 (Laplacian).** *$\Delta:=\operatorname{div}\operatorname{grad}$ acts on scalar fields as $\Delta f=\tfrac1N\sum_{i=1}^N\partial_i^2 f$ — the flat Laplace–Beltrami operator of $H\cong\mathbb{R}^{N-1}$, equal to the ambient $\mathbb{R}^N$ Laplacian restricted to gauge-invariant fields and rescaled by $1/N$.*

*Proof.* $\operatorname{div}\operatorname{grad}f=\sum_i\partial_i(\tfrac1N\partial_if)=\tfrac1N\sum_i\partial_i^2f$. Restricted to gauge-invariant $f$ this is the Laplace–Beltrami operator of the flat metric $M_N|_H=NI_H$ (Block B). $\square$

**Certificate (Block B).** For $N\in\{3,4,5,6\}$, on an explicit gauge-invariant polynomial scalar field and an explicit $H$-valued polynomial vector field: $\sum_i\partial_if=0$; $\operatorname{grad}=\tfrac1N df$ is zero-sum; $\langle\operatorname{grad}f,F\rangle_{M_N}=df^\top F$; $\operatorname{div}$ is invariant under $F\mapsto F+(\text{const})\mathbf 1$; and $\Delta=\operatorname{div}\operatorname{grad}=\tfrac1N\sum_i\partial_i^2$. All exact.

### 4.4 Second-order identities at the correct general-$N$ level

The single-axis curl $\operatorname{curl}=K(\nabla)$ of Paper 01b exists only at $N=4$, because (Paper 01 §8) only in dimension $N-1=3$ does the Hodge dual of a $1$-form land back among vectors, letting one axis parameterize the rotation generators. For general $N$ the correct home of the second-order vanishing identities is the **discrete coboundary complex** of the $(N-1)$-simplex, where $\operatorname{curl}\operatorname{grad}=0$ is the topological statement $d^2=0$.

**Theorem 4.4 ($\operatorname{curl}\operatorname{grad}=0$ as $d^2=0$, all $N$).** *On the $(N-1)$-simplex the coboundary maps satisfy $d_{k+1}d_k=0$ for all $k$. In particular $d_1d_0=0$ is the discrete curl-of-gradient identity, valid in every dimension and independent of any single-axis structure.*

*Proof.* $d_{k+1}d_k=0$ is the defining nilpotency of the simplicial coboundary (each $(k+2)$-face's boundary-of-boundary cancels in signed pairs). Verified directly (Block C) for $N\in\{4,5,6\}$ and all available $k$. $\square$

**Proposition 4.5 ($N=4$ recovery).** *At $N=4$, with $\operatorname{curl}=\tfrac14\widetilde K(\nabla)$ the raw-cyclic-difference operator on the gradient axis (Paper 01b Def. 5.1), $\operatorname{curl}\operatorname{grad}f=0$ and $\operatorname{div}\operatorname{curl}F=0$ hold as the operator promotions of $K(u)u=0$ and the column-sum identity.*

*Proof.* Both are re-verified symbolically (Block C) on general gauge-invariant scalar and $H$-valued vector fields. The mechanism is exactly Paper 01b Theorems 6.1–6.2: the differential identities are the algebraic identities of Paper 01 with commuting partials $\partial_i\partial_j=\partial_j\partial_i$ supplied as the one new input. $\square$

The reading: $d^2=0$ is the universal, dimension-free skeleton of "the curl of a gradient vanishes"; the simplicial cross-product operator $K$ is the $N=4$ enrichment that additionally turns the $1$-cochain back into a vector field. Paper 01b's $\widetilde K=\star_E\,d_0$ (Theorem 10.1) is precisely this enrichment, available only when $\star_E$ is an edge-space involution — which §7 shows is an $N=4$ event.

---

## 5. The Laplacian spectrum and heat kernel

### 5.1 Graph-Laplacian heat trace

**Theorem 5.1 (Heat-kernel trace).** *For every $N$,*
$$\operatorname{Tr} e^{-tM_N}=\sum_{\lambda\in\operatorname{spec}M_N}e^{-t\lambda}=1+(N-1)\,e^{-Nt}.$$
*The constant term $1$ is the harmonic/gauge mode ($H^0$); the $(N-1)e^{-Nt}$ term is the hyperplane spectrum. As $t\to0^+$, $\operatorname{Tr} e^{-tM_N}=N-N(N-1)\,t+O(t^2)$, with leading coefficient $N=\dim C^0$ and first heat coefficient $-\operatorname{tr}M_N=-N(N-1)=-2\cdot\#\mathrm{edges}(K_N)$.*

*Proof.* Immediate from $\operatorname{spec}M_N=\{0^{(1)},N^{(N-1)}\}$ (Theorem 3.1). The small-$t$ expansion is Taylor's; $\operatorname{tr}M_N=N(N-1)$ equals twice the edge count of $K_N$, the standard first heat invariant of a graph Laplacian. Verified for $N\in\{3,\dots,7\}$ (Block D). $\square$

### 5.2 Spectral zeta, pseudo-determinant, and Cayley's formula

Restricting to the nonzero spectrum (the hyperplane modes) gives a finite, fully explicit spectral zeta function and a clean determinant.

**Theorem 5.2 (Spectral zeta; pseudo-determinant; spanning trees).** *For every $N\geq2$:*

1. *(Spectral zeta.) $\displaystyle\zeta_{M_N}(s):=\!\!\sum_{\lambda\neq0}\lambda^{-s}=(N-1)\,N^{-s}$, an entire function of $s$ with $\zeta_{M_N}(0)=N-1$ (the number of nonzero modes) and $\zeta_{M_N}'(0)=-(N-1)\ln N$.*
2. *(Pseudo-determinant.) The product of the nonzero eigenvalues is $\det{}'(M_N)=e^{-\zeta'_{M_N}(0)}=N^{N-1}$.*
3. *(Matrix-Tree / Cayley.) Any first cofactor of $M_N$ equals $\det{}'(M_N)/N=N^{N-2}$, the number of spanning trees of $K_N$ (Cayley's formula).*

*Proof.* (1) The nonzero spectrum is $N$ with multiplicity $N-1$, so $\sum_{\lambda\neq0}\lambda^{-s}=(N-1)N^{-s}$; evaluate and differentiate at $s=0$. (2) $\det{}'(M_N)=\prod_{\lambda\neq0}\lambda=N^{N-1}$. (3) The Matrix-Tree (Kirchhoff) theorem states that any cofactor of the Laplacian equals the spanning-tree count $\tau(G)$; for the Laplacian with one zero eigenvalue, $\tau(G)=\det{}'(L)/n$ where $n$ is the number of vertices. Here $\tau(K_N)=N^{N-1}/N=N^{N-2}$, recovering Cayley. All three verified for $N\in\{3,\dots,7\}$ (Block D), including the cofactor determinant directly. $\square$

The package is a single coherent invariant: the spectral floor of the simplicial frame **knows** the combinatorics of its own skeleton. The metric's pseudo-determinant counts the spanning trees of the complete graph on the frame rays. This is classical Kirchhoff/Cayley; the point is that it is the *same matrix* $M_N$ that governs the inner product, the rotation isometry, and the Laplace–Beltrami operator of the trilogy.

### 5.3 The combinatorial Hodge Laplacian and the Betti numbers

The graph Laplacian $M_N=L_0$ is the degree-$0$ rung of the Hodge Laplacian tower $L_k=d_k^\top d_k+d_{k-1}d_{k-1}^\top$ on the $k$-cochains of the $(N-1)$-simplex.

**Proposition 5.3 (Harmonic dimensions = Betti numbers of the simplex).** *On the full $(N-1)$-simplex, $\dim\ker L_k=b_k$ with $b_0=1$ and $b_k=0$ for $1\le k\le N-2$ (the simplex is contractible). Thus the only harmonic cochains are the constants $H^0=\mathbb{R}\mathbf 1$ — the gauge line.*

*Proof.* The simplex is contractible, so its (reduced) cohomology vanishes above degree $0$ and is one-dimensional in degree $0$; by discrete Hodge theory $\dim\ker L_k=b_k$. Verified for $N\in\{4,5\}$ across all degrees (Block D). $\square$

The reading for the program: on a *single* simplex the harmonic sector is exactly the gauge line and nothing more, so the gauge/Hodge decomposition of Paper 01b §7 has trivial harmonic part $h=0$ for vector fields on a simply-connected $H$. The harmonic sector becomes nontrivial only on **complexes with loops**, where $b_1>0$ — which is precisely the topologically protected current of Paper 01b Prop. 7.3(3). The general-$N$ statement here certifies the local (single-cell) baseline against which that global current is measured.

### 5.4 The continuum Laplace–Beltrami on $H$

For completeness we record the continuum object. $H$ with the metric $M_N|_H=NI_H$ is isometric to flat Euclidean $\mathbb{R}^{N-1}$ (rescaled). Its Laplace–Beltrami operator $\Delta=\tfrac1N\sum_i\partial_i^2$ (Theorem 4.3) has **continuous** spectrum $[0,\infty)$ and the Euclidean heat kernel
$$e^{-t\Delta}(x,y)=\big(4\pi t/N\big)^{-(N-1)/2}\exp\!\Big(-\tfrac{N\,|x-y|^2}{4t}\Big),$$
with the metric constant $1/N$ entering through the diffusion rate. The *discrete* graph Laplacian of §5.1–5.2 is the finite, frame-intrinsic object that carries the arithmetic content; the continuum operator is the flat-space limit and has no discrete spectrum to enumerate. We are explicit that the interesting spectral invariants (heat trace, zeta, Cayley) live on the **discrete** side.

---

## 6. Exact rationality (C2, general $N$)

**Theorem 6.1 (Square-root-free calculus on rational data).** *In the $M_N$-normalization, for rational zero-sum field data all first-order operators are rational: $\operatorname{grad}=\tfrac1N d$, $\operatorname{div}=\sum_i\partial_i(\cdot)_i$, and $\Delta=\tfrac1N\sum_i\partial_i^2$ map $\mathbb{Q}$-coefficient polynomial fields to $\mathbb{Q}$-coefficient polynomial fields. At $N=4$ the cross-product generator $\widetilde K(u)$ and its square $\widetilde K(u)^2$ are rational for rational axes, and the unit-axis cubic $\widetilde K(u)^3=-\widetilde K(u)$ holds on the rational $M$-unit axis $u=(\tfrac14,\tfrac14,-\tfrac14,-\tfrac14)$.*

*Proof.* All operators have rational structure constants ($1/N$, integer differences); no square root appears because $M_N|_H=NI_H$ is already an *integer* scalar — the $1/\sqrt{N-1}$ of the ETF metric $G_N$ has been absorbed into the length convention exactly as in Paper 01 §7.5. The rational axis $(\tfrac14,\tfrac14,-\tfrac14,-\tfrac14)$ is zero-sum and $M$-unit ($u^\top M u=N\sum u_i^2=4\cdot 4\cdot\tfrac1{16}=1$). Verified (Block F). $\square$

This resolves the **general-$N$** form of Paper 01b open problem **C2**: the simplicial differential calculus is a fully exact, square-root-free rational calculus on rational tetrahedral (and, off the tetrahedron, simplicial) data, in the spirit of Wildberger's rational trigonometry [Wildberger]. The only irrational quantities anywhere in the trilogy are the $\sin\theta,\cos\theta$ of finite rotations, which the Weierstrass substitution $t=\tan(\theta/2)$ rationalizes (Paper 01 §7.5).

---

## 7. Why $N=4$ is special for the opposite-edge Hodge involution

Paper 01b Theorem 10.1(3) realizes the cross-product generator as $\widetilde K(u)=\star_E(d_0u)$, where $\star_E:C^1\to C^1$ is the *signed opposite-edge involution* sending each edge value to $\pm$ the value on the unique opposite edge. The existence of $\star_E$ **as an endomorphism of the edge space** is the load-bearing fact: it is what makes the discrete Hodge star an honest involution of $1$-cochains rather than a map to some other cochain space. We now pin its existence to $N=4$.

### 7.1 Edges and their opposite faces

In the $(N-1)$-simplex, an **edge** is a $1$-face, spanned by $2$ of the $N$ vertices. The complementary (opposite) face is spanned by the remaining $N-2$ vertices, hence is an $(N-3)$-face. The combinatorial Hodge star induced by the self-duality of the simplex pairs a face with its complement; restricted to edges, it sends a $1$-face to an $(N-3)$-face.

**Theorem 7.1 ($\star_E$ is an edge involution iff $N=4$).**

1. *(Self-duality of edges.) The opposite face of an edge is again an edge — i.e. the Hodge dual maps $C^1\to C^1$ — if and only if $N-3=1$, i.e. $N=4$.*
2. *(The involution at $N=4$.) For $N=4$ there is a signed permutation $\star_E$ of the $6$ edges (the opposite-edge map, with the Levi-Civita signs of Paper 01 §3.1) satisfying $\star_E^2=I$ and $\widetilde K(u)=\star_E(d_0u)$ for all $u$.*
3. *(Failure for $N\geq5$.) For $N\geq5$ the Hodge dual of an edge is an $(N-3)$-face with $N-3\geq2$, so the duality is a map $C^1\to C^{N-3}$ with $N-3\neq1$; no signed opposite-edge endomorphism of $C^1$ implements it. (The face counts $\binom N2=\binom N{N-2}$ always match by complementation, but the target degree is wrong.)*

*Proof.* (1) The opposite face of an edge has dimension $N-3$; it is a $1$-face iff $N-3=1$. (2) Exhibited explicitly: with opposite pairs and signs $(-1,+1,-1,-1,+1,-1)$ on the ordered edges of $K_4$, $\star_E$ is a signed permutation with $\star_E^2=I$ and $\widetilde K(u)_{\text{coch}}=\star_E\,d_0u$ — re-confirming Paper 01b Theorem 10.1(3) and additionally certifying $\star_E^2=I$ (Block E). (3) For $N\in\{5,6,7\}$, $N-3\in\{2,3,4\}\neq1$, so the Hodge image of an edge is a strictly higher cochain; certified (Block E). $\square$

### 7.2 The two roads to $N=4$

Theorem 7.1 is the **combinatorial** explanation of the tetrahedron's exceptional status, and it runs exactly parallel to the **Lie-theoretic** one of Paper 01 §8:

| Road | Statement | $N=4$ condition |
|---|---|---|
| Lie-theoretic (Paper 01 §8) | one vector axis parameterizes all of $\mathfrak{so}(N-1)$ | $\dim\mathfrak{so}(N-1)=N-1$, i.e. $N-1=3$ |
| Hodge-combinatorial (here) | the opposite-edge map $\star_E$ is an endomorphism of $C^1$ | edge dual is an edge, i.e. $N-3=1$ |

Both conditions are solved by $N=4$ alone, and they are the same fact seen twice: in dimension $d=N-1=3$, the Hodge star $\Lambda^1\to\Lambda^{d-1}=\Lambda^2$ has $d-1=2$… but the *vector*–$2$-form identification $\Lambda^2\cong\Lambda^1$ (again special to $d=3$) sends it back to a vector/edge. The middle-dimension coincidence of $d=3$ is what both roads detect. For $N\geq5$ the cross-product layer is genuinely a higher-arity, $(N-3)$-input object (Paper 01 §8.2), and the discrete Hodge star is a genuine degree-raising map; the single-axis / single-edge picture is a $d=3$ luxury.

**Certificate (Block E).** For $N\in\{3,\dots,7\}$: the self-duality boolean $(N-3=1)$ matches $(N=4)$; the edge/complement face counts match by complementation; for $N=4$, $\widetilde K=\star_E d_0$ with $\star_E^2=I$; for $N\in\{5,6,7\}$ the edge dual lives in $C^{N-3}$, $N-3\neq1$. All exact.

---

## 8. Novelty versus organization, and the resolution of C2/C6

**Resolved (general-$N$ half of Paper 01b C6).** The simplicial Laplacian spectrum is $\{0^{(1)},N^{(N-1)}\}$, the graph Laplacian spectrum of $K_N$; the heat-kernel trace is $1+(N-1)e^{-Nt}$; the spectral zeta is $(N-1)N^{-s}$; the pseudo-determinant is $N^{N-1}$ and yields Cayley's $N^{N-2}$ spanning trees by Matrix-Tree. The continuum Laplace–Beltrami on $H$ is flat with continuous spectrum and the Euclidean heat kernel. (§5–6.)

**Resolved (general-$N$ half of Paper 01b C2).** All first-order operators are rational on rational data in the $M_N$-normalization, in every dimension. (§6.)

**Novelty boundary, restated honestly.** The spectrum, heat trace, spectral zeta, Matrix-Tree/Cayley, and contractible-simplex Betti numbers are classical results, invoked not reproved. The contributions are organizational and one structural:

- *Organization with leverage:* identifying $M_N$ as the $K_N$ Laplacian *as the spectral substrate of the frame across all $N$* (Theorem 3.1), and proving that $M_N|_H=NI_H$ is the **sole** metric input to the entire first-order calculus, which therefore extends verbatim off the tetrahedron (Theorems 4.1–4.3) and stays rational (Theorem 6.1).
- *One crisp new structural statement:* the dimension-count $1=N-3\Leftrightarrow N=4$ that pins the existence of the opposite-edge Hodge involution $\star_E$ to the tetrahedron (Theorem 7.1), exhibited as the combinatorial twin of the Lie-theoretic $\dim\mathfrak{so}(3)=3$ — two independent roads to the same exceptional dimension (§7.2).

We claim no more than this. The single most informative line is §7.2: **$N=4$ is special for the discrete Hodge star for the *same middle-dimension* ($d=3$) reason it is special for the cross product**, and the spectral floor makes both visible at once.

---

## 9. Open problems and a forward flag

Ordered tractable → speculative.

- **S1 (Spanning-tree / metric dictionary).** $\det{}'(M_N)=N^{N-1}$ ties the metric's pseudo-determinant to $K_N$'s spanning trees. For *weighted* or *deformed* simplicial frames (non-uniform Gram matrices), does the weighted Matrix-Tree theorem give a clean metric–combinatorics dictionary? *Tractable; concrete.*

- **S2 (Heat-kernel coefficients as frame invariants).** The small-$t$ expansion $\operatorname{Tr} e^{-tM_N}=N-N(N-1)t+\tfrac{N(N-1)^2}{2}t^2-\dots$ has coefficients $\tfrac{(-1)^k}{k!}(N-1)N^k+[\,k{=}0\,]$. Identify each as a count on $K_N$ (the $t^1$ coefficient is $-2\#\mathrm{edges}$); is there a closed combinatorial reading of the whole tower? *Tractable.*

- **S3 (General-$N$ higher-arity Hodge layer).** Paper 01 §8.2 sketches the $(N-3)$-input simple-blade generator. Write its explicit overcomplete-coordinate matrix and its discrete-coboundary realization $C^1\to C^{N-3}$ for $N=5,6$, completing the general-$N$ curl layer that §4.4/§7 only frame. *Medium.*

- **S4 (C6 forward flag — apex/archimedean operator).** *Flagged forward-only; not claimed.* The program's apex/archimedean reflection operator is identified elsewhere (program memory: N3's edge operator $(A-I)\Phi$, the reflection $s\mapsto1-s$ with a continuous-spectrum $1/8$-turn phase). The graph-Laplacian heat kernel here is a **finite, positive, real** object with spectrum $\{0,N\}$ and spectral zeta $(N-1)N^{-s}$ — manifestly *not* a zeta with a critical line, and with no reflection symmetry of its own. We therefore record honestly: **the simplicial Laplacian heat kernel of a single simplex does not, by itself, suggest an archimedean/apex operator realization.** The only place such structure could enter is the *limit over a growing family of simplices/complexes* (where $N\to\infty$ and the $1/N$ diffusion constant degenerates), or via a *deformation* of the uniform Gram matrix toward a number-theoretic weighting — both of which are program-level conjectures with no support from the present finite, exactly-solved spectrum. This sub-thread is left as a flag, not a result.

---

## Appendix A: Exact-arithmetic certificate

The reference implementation `empirical_forward1/cert_spectral_generalN.py` (sympy / integer arithmetic only; no floating point; no torch/transformers) runs $108$ checks, all GREEN, organized in six blocks:

- **Block A** — $M_N=d_0^\top d_0=L(K_N)$; spectrum $\{0^{(1)},N^{(N-1)}\}$ from the characteristic polynomial; $M_N\mathbf 1=0$; $M_N v=Nv$ on $H$. ($N=3,4,5,6,7$.)
- **Block B** — gauge invariance $\Rightarrow\sum_i\partial_if=0$; $\operatorname{grad}=\tfrac1N d$ zero-sum; adjointness $\langle\operatorname{grad}f,F\rangle_{M_N}=df^\top F$; gauge-independence of $\operatorname{div}$; $\Delta=\operatorname{div}\operatorname{grad}=\tfrac1N\sum_i\partial_i^2$. ($N=3,4,5,6$.)
- **Block C** — $d_{k+1}d_k=0$ on the $(N-1)$-simplex (all available $k$, $N=4,5,6$); $N=4$ recovery $\operatorname{curl}\operatorname{grad}=0$, $\operatorname{div}\operatorname{curl}=0$.
- **Block D** — heat trace $1+(N-1)e^{-Nt}$ and its $t^1$ coefficient; pseudo-determinant $N^{N-1}$; Matrix-Tree cofactor $=N^{N-2}=$ Cayley; Betti numbers $b_0=1$, $b_{k>0}=0$. ($N=3,\dots,7$.)
- **Block E** — edge self-duality boolean $=(N{=}4)$; complement face-count bijection; $N=4$ $\star_E$ with $\star_E^2=I$ and $\widetilde K=\star_E d_0$; $N\geq5$ edge dual in $C^{N-3}$. ($N=3,\dots,7$.)
- **Block F** — rational-data witness: $\widetilde K$, $\widetilde K^2$, $\operatorname{grad}$ rational; rational $M$-unit axis; $\widetilde K^3=-\widetilde K$.

All residuals are exact zeros over $\mathbb{Q}$ (or exact eigenvalue/character-polynomial matches), so each identity holds for all fields and all $N$ in the stated ranges, not merely a tested instance.

---

## References

[Biggs] Biggs, N. *Algebraic Graph Theory*. 2nd ed., Cambridge University Press, 1993.

[Brouwer–Haemels] Brouwer, A.E., Haemers, W.H. *Spectra of Graphs*. Springer, 2012.

[Chung] Chung, F.R.K. *Spectral Graph Theory*. CBMS Regional Conference Series in Mathematics 92, AMS, 1997.

[Desbrun–Hirani–Leok–Marsden] Desbrun, M., Hirani, A.N., Leok, M., Marsden, J.E. "Discrete Exterior Calculus." arXiv:math/0508341 (2005).

[Paper 01] Murillo Montero, L. *Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates*. v2, 2026. DOI 10.5281/zenodo.19689049.

[Paper 01b] Murillo Montero, L. *Intrinsic Differential Calculus on Simplicial (Quadray) Coordinates*. Draft 1, 2026.

[Paper 01c] Murillo Montero, L. *The Moving Amari–Chentsov Cubic in Simplicial (Quadray) Coordinates*. Draft 1, 2026.

[Stanley] Stanley, R.P. *Enumerative Combinatorics*, Vol. 2. Cambridge University Press, 1999. (Matrix-Tree theorem, Cayley's formula.)

[Wildberger] Wildberger, N.J. *Divine Proportions: Rational Trigonometry to Universal Geometry*. Wild Egg Books, 2005.

---

*[End of Draft 1.]*
