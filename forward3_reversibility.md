# The Discrete Hodge Decomposition on a Simplicial Complex: The Arrow of Time is the First Betti Number

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Draft 1 — June 2026*

**Companion note.** This is the *reversibility* sequel to the simplicial-frame trilogy: **Paper 01** (*Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates* — the cross product $K(u)$, rotation, the zero-sum hyperplane), **Paper 01b** (*Intrinsic Differential Calculus* — $\nabla$, $\operatorname{div}$, $\operatorname{curl}$, and the curvature/current split of the field Jacobian), and **Paper 01c** (*The Moving Amari–Chentsov Cubic* — the information geometry). Paper 01b worked on a *single* cell, the tetrahedron's $1$-skeleton $K_4$, where the field Jacobian splits $DF=S+A$ with $\operatorname{tr}S=\operatorname{div}F$ (curvature/source) and $A=\tfrac12\widetilde K(\operatorname{curl}F)$ (current/vorticity), and where the harmonic sector is empty because one cell has no loops. The present paper moves to a simplicial *complex*, where loops exist, and identifies the topologically protected current with the first Betti number. Numbers prefixed "01.", "01b.", "01c." refer to those papers.

---

## Abstract

On a simplicial complex the space of $1$-cochains $C^1$ carries the **discrete Hodge (Helmholtz) decomposition**
$$C^1=\operatorname{im}d_0\ \oplus\ \operatorname{im}d_1^\top\ \oplus\ \ker L_1,\qquad L_1=d_0d_0^\top+d_1^\top d_1,$$
into three mutually orthogonal subspaces — the **exact** (gradient/curvature), **coexact** (curl/current), and **harmonic** sectors — where $d_0:C^0\to C^1$ and $d_1:C^1\to C^2$ are the discrete coboundaries and $L_1$ is the $1$-Hodge-Laplacian. This is classical discrete exterior calculus [Eckmann, Hirani, Lim]. We make three points, all verified in exact arithmetic, that weld it to the simplicial-frame program and to the program's *reversibility / irreversible-blind-spot* line.

**(i) The arrow is $\beta_1$.** The dimension of the harmonic sector equals the first Betti number, $\dim\ker L_1=\beta_1$ — the number of independent loops. We verify this across a panel of complexes with $\beta_1\in\{0,1,2,3\}$, each three independent ways (nullity of $L_1$, the rank identity $\beta_1=\dim C^1-\operatorname{rank}d_0-\operatorname{rank}d_1$, and an independent numerical spectrum). The exact/coexact decomposition is the discrete-complex form of Paper 01b's curvature/current split, with the harmonic sector — *absent on a single cell* — appearing exactly when the complex has loops.

**(ii) Exact ↔ symmetric, coexact ↔ antisymmetric.** Reproducing Paper 01b cell-locally and promoting it: a gradient ($d_0$-exact) cochain has zero current (its field Jacobian is a symmetric Hessian, $A=0$); a curl ($d_1^\top$-coexact) cochain is trace-free ($\operatorname{div}\operatorname{curl}=0$); the harmonic sector is annihilated by both $d_0^\top$ and $d_1$ (closed *and* co-closed). A self-adjoint instrument — a single-encoder objective that probes a symmetric form $\langle x,Tx\rangle$ — sees only the symmetric/exact sector and is **blind** to the harmonic current of dimension $\beta_1$; recovering it requires a genuinely two-sided (predictor) probe. This is the simplicial-complex realization of the program's *Irreversible Blind Spot* and the *Curvature and Current* operator split, with the $\beta_1$ harmonic sector as the topologically protected, mesh-independent arrow.

**(iii) The general-$N$ bridge.** The integer simplicial metric $M=N\,I-J$ of the $N$-frame is the complete-graph $K_N$ Laplacian $L_0=d_0^\top d_0$, acting as the scalar $N$ on the zero-sum hyperplane $H$ (eigenvalue $N$ of multiplicity $N-1$) and annihilating the gauge line; at $N=4$ this is Paper 01's $4I-J$. The filled $N$-vertex simplex is contractible ($\beta_1=0$: a single cell carries no current), its $k$-skeleton has Betti number $\binom{N-1}{k+1}$, and the nonzero $L_1$ spectrum on the filled simplex is the single integer $N$ with full multiplicity.

The honest novelty boundary (§7): the Hodge decomposition and $\dim\ker L_1=\beta_1$ are classical; what is new here is the *identification with the simplicial-frame curvature/current split of Paper 01b* — promoting the single-cell $A=\tfrac12\widetilde K(\operatorname{curl}F)$ dictionary to the complex, where the harmonic sector is the arrow — and the explicit weld to the program's reversibility-axis blind-spot results.

**Keywords:** discrete exterior calculus, Hodge decomposition, Helmholtz decomposition, simplicial complex, first Betti number, harmonic cochain, Hodge Laplacian, graph Laplacian, cross product, curl, irreversibility, arrow of time, reversible/irreversible, self-supervised representation, predictor, Quadray coordinates.

**MSC 2020:** 58A14 (Hodge theory), 55N31, 05E45 (combinatorial aspects of simplicial complexes), 15A18 (eigenvalues), 53A45, 68T07 (artificial neural networks).

---

## 1. Introduction

### 1.1 From one cell to a complex

Paper 01b developed the first-order vector calculus of the simplicial frame on a *single* simplex's tangent hyperplane $H$, and proved (Prop. 01b.7.3) that the field Jacobian $DF$ of a vector field splits into a symmetric and an antisymmetric part carrying, respectively, the divergence (curvature/source) and the curl (current/vorticity):
$$DF=S+A,\qquad \operatorname{tr}S=\operatorname{div}F,\qquad A=\tfrac12\widetilde K(\operatorname{curl}F),$$
with $\widetilde K$ the cyclic-difference cross-product generator of Paper 01. The Helmholtz decomposition $F=\operatorname{grad}f+\operatorname{curl}B+h$ diagonalizes this: gradients are pure curvature ($A=0$), curls are pure current ($\operatorname{tr}S=0$), and the harmonic part $h$ is annihilated by both. Paper 01b further showed (Thm. 01b.10.1) that on the tetrahedron's $1$-skeleton $K_4$ the generator $\widetilde K(u)$ *is* the Hodge dual $\star_E(d_0u)$ of the discrete gradient, the metric $M=4I-J$ is the $K_4$ graph Laplacian $L_0=d_0^\top d_0$, and the gauge direction is $H^0(K_4)=\ker L_0$.

But on a single cell the harmonic sector of *vector fields* on $H$ is empty: the tetrahedron is contractible, $b_1=0$, and Paper 01b noted only that "on a domain with loops, [the harmonic sector] has dimension $b_1$" (Prop. 01b.7.3(3), Cor. 01b.C4). This paper supplies the *with-loops* picture. The arena is a simplicial **complex** — many cells glued along shared faces — and the object is the discrete Hodge decomposition of $1$-cochains, the genuine global assembly of Paper 01b's local fibre (the "DEC is the global assembly" remark of §01b.10.1). The harmonic sector is now nonempty exactly when the complex has loops, and its dimension is the first Betti number $\beta_1$.

### 1.2 Why this is the reversibility direction

The program carries a *reversibility axis* (the *Irreversible Blind Spot* and *Curvature and Current* line): an operator $T=S+A$ splits into a symmetric part $S$ (reversible "curvature", detailed balance) and an antisymmetric part $A$ (the probability current, the **arrow of time**); a single self-adjoint instrument is a functional of $S$ alone and is blind to $A$, because $\langle h,Ah\rangle=0$ for every real $h$ (the antisymmetric part is in the kernel of every symmetric quadratic form). The topological capstone of that line states that the protected, mesh-independent arrow is the *harmonic* part of the current, of dimension $\dim H^1=b_1$.

On the simplicial frame these are the *same* objects. The Helmholtz/Hodge sectors **are** the $S/A$ split: exact = symmetric/curvature ($A=0$), coexact = antisymmetric/current ($\operatorname{tr}S=0$), harmonic = the topologically protected arrow. Direction 3 is therefore the place where the simplicial-frame calculus and the program's reversibility-blind-spot theorems coincide on one combinatorial object, with $\beta_1$ — computed exactly from the coboundaries $d_0,d_1$ — as the number of independent arrows the frame can carry. The deterministic certificate (§6) verifies this coincidence across seven complexes.

### 1.3 Contributions

1. **Discrete Hodge decomposition, exact-certified (§3, §6).** $C^1=\operatorname{im}d_0\oplus\operatorname{im}d_1^\top\oplus\ker L_1$ with the three sectors mutually orthogonal, spanning, and of dimensions that add to $\dim C^1$; $d_1d_0=0$ ($d^2=0$); verified on every test complex.
2. **The arrow is $\beta_1$ (§4, §6).** $\dim\ker L_1=\beta_1$, verified three independent ways on a panel with $\beta_1\in\{0,1,2,3\}$ (filled tetra-surface and disk → $0$; annulus and hollow triangle → $1$; figure-eight and theta graph → $2$; wedge of three loops → $3$).
3. **Exact↔symmetric, coexact↔antisymmetric, and self-adjoint blindness (§5, §6).** The Paper 01b cell-local dictionary ($\operatorname{tr}S=\operatorname{div}F$, $A=\tfrac12\widetilde K(\operatorname{curl}F)$, grad ⇒ $A=0$, curl ⇒ $\operatorname{tr}S=0$) is reproduced and promoted to the cochain level (curl·grad $=0$, div·curl $=0$, harmonic closed-and-co-closed); a symmetric instrument's quadratic form is shown blind (residual $0$) to an antisymmetric current installed on the harmonic sector, while a two-sided predictor reads it.
4. **General-$N$ bridge to Direction 1 (§5.3, §6).** $M=N I-J=L_0(K_N)$ with spectrum $N^{(N-1)}\oplus 0$; filled $N$-simplex $\beta_1=0$; $k$-skeleton $\beta_k=\binom{N-1}{k+1}$; nonzero $L_1$ spectrum on the filled simplex $=N$ with full multiplicity.

---

## 2. Setup: cochains, coboundaries, and the Hodge Laplacian

Let $X$ be a finite oriented simplicial complex with vertex set $V$, edge set $E$, and triangle set $F$. The **cochain spaces** are $C^0=\mathbb{R}^{|V|}$ (a value per vertex), $C^1=\mathbb{R}^{|E|}$ (per edge), $C^2=\mathbb{R}^{|F|}$ (per triangle), each with the standard Euclidean inner product (every simplex an orthonormal basis cochain). Orientation is the increasing vertex order. The **coboundary operators** are
$$(d_0u)([ij])=u_j-u_i,\qquad (d_1\alpha)([ijk])=\alpha([jk])-\alpha([ik])+\alpha([ij]),$$
i.e. the discrete gradient and discrete curl. They satisfy $d_1d_0=0$ ($d^2=0$). The adjoints $d_0^\top:C^1\to C^0$ (discrete $-\operatorname{div}$) and $d_1^\top:C^2\to C^1$ are the transposes in the standard bases.

The **$1$-Hodge-Laplacian** is
$$L_1:=d_0d_0^\top+d_1^\top d_1.$$
($L_0=d_0^\top d_0$ is the graph Laplacian; on $K_N$ it is the metric $M=N I-J$ of Paper 01, by Thm. 01b.10.1.)

These are the genuine global coboundaries of which Paper 01b's single-cell operators are the local fibre: on one cell, $\operatorname{grad}\leftrightarrow d_0$, $\operatorname{curl}\leftrightarrow d_1$ (via the opposite-edge Hodge star $\star_E$), $\operatorname{div}\leftrightarrow d_2$ (§01b.10.1).

---

## 3. The discrete Hodge decomposition

**Theorem 3.1 (Discrete Hodge / Helmholtz decomposition of $1$-cochains).** *For any finite simplicial complex, the space of $1$-cochains decomposes as an orthogonal direct sum*
$$C^1=\underbrace{\operatorname{im}d_0}_{\text{exact = grad}}\ \oplus\ \underbrace{\operatorname{im}d_1^\top}_{\text{coexact = curl}}\ \oplus\ \underbrace{\ker L_1}_{\text{harmonic}},$$
*and a $1$-cochain is harmonic iff it is closed and co-closed: $\ker L_1=\ker d_1\cap\ker d_0^\top$.*

*Proof.* Orthogonality of $\operatorname{im}d_0$ and $\operatorname{im}d_1^\top$ is $d_1d_0=0$: $\langle d_0u,d_1^\top\beta\rangle=\langle d_1d_0u,\beta\rangle=0$. For the harmonic characterization, $\langle L_1\alpha,\alpha\rangle=\|d_0^\top\alpha\|^2+\|d_1\alpha\|^2$, so $L_1\alpha=0$ iff $d_0^\top\alpha=0$ and $d_1\alpha=0$; such $\alpha$ is orthogonal to both $\operatorname{im}d_0$ (since $d_0^\top\alpha=0$) and $\operatorname{im}d_1^\top$ (since $d_1\alpha=0$). The three subspaces are mutually orthogonal and, by the rank–nullity identity below, their dimensions sum to $|E|$; hence they span. $\square$

**Reading.** This is the cochain-level form of Paper 01b's Helmholtz decomposition $F=\operatorname{grad}f+\operatorname{curl}B+h$. The exact sector is the discrete gradient (curvature), the coexact sector the discrete curl (current), and — the new ingredient relative to one cell — the harmonic sector $\ker L_1$ is generically nonzero on a complex with loops.

The decomposition is verified in `cert_hodge_arrow.py` block (H): on each test complex the exact $d_1d_0=0$ holds, the dimensions add ($\dim\operatorname{im}d_0+\dim\operatorname{im}d_1^\top+\dim\ker L_1=|E|$), the three numerical projectors are mutually orthogonal (overlaps $<10^{-9}$, in fact $\sim 10^{-16}$) and sum to the identity (spanning).

---

## 4. The arrow is the first Betti number

**Theorem 4.1 ($\dim\ker L_1=\beta_1$).** *For any finite simplicial complex, the dimension of the harmonic $1$-cochain sector equals the first Betti number,*
$$\dim\ker L_1=\beta_1=\dim C^1-\operatorname{rank}d_0-\operatorname{rank}d_1.$$

*Proof.* By Theorem 3.1, $\ker L_1$ is the orthogonal complement of $\operatorname{im}d_0\oplus\operatorname{im}d_1^\top$ in $C^1$, so $\dim\ker L_1=|E|-\operatorname{rank}d_0-\operatorname{rank}d_1$. The de Rham/Hodge theorem for cochain complexes identifies $\ker L_1$ with the first cohomology $H^1(X;\mathbb{R})$ [Eckmann]; over $\mathbb{R}$, $\dim H^1=\beta_1$, the first Betti number. The displayed rank formula is the same number written via rank–nullity: $\operatorname{rank}d_0=|V|-\beta_0$ and $\operatorname{rank}d_1=|F|-\beta_2$ give $\beta_1=|E|-\operatorname{rank}d_0-\operatorname{rank}d_1$. $\square$

**Corollary 4.2 (The single cell has no current).** *On the tetrahedron's filled surface (a $2$-sphere) and on any contractible complex, $\beta_1=0$, so $\ker L_1=0$: there is no harmonic current. This is the structural reason Paper 01b's harmonic sector was empty on one cell.*

**The certificate.** `cert_hodge_arrow.py` block (B) verifies $\dim\ker L_1=\beta_1$ on:

| complex | $V/E/F$ | $\beta_1$ | $\dim\ker L_1$ |
|---|---|---|---|
| tetrahedron surface $S^2$ (filled) | $4/6/4$ | $0$ | $0$ |
| filled disk (hexagon fan) | $7/12/6$ | $0$ | $0$ |
| triangulated annulus (one hole) | $12/24/12$ | $1$ | $1$ |
| hollow triangle ($2$-cell removed) | $3/3/0$ | $1$ | $1$ |
| figure-eight (two loops) | $5/6/0$ | $2$ | $2$ |
| theta graph (two cycles) | $5/6/0$ | $2$ | $2$ |
| wedge of three loops | $7/9/0$ | $3$ | $3$ |

Each row is checked three ways — exact nullity of $L_1$ over $\mathbb{Q}$, the rank identity, and the topological $\beta_1$ — all agreeing, with an independent numerical eigenvalue count confirming the nullity and reporting the spectral gap to the first nonzero eigenvalue.

The annulus is the cleanest *protected* case: filling in $2$-cells everywhere except around the central hole leaves exactly one harmonic loop, $\beta_1=1$. This is the discrete model of "one circulation around a hole" — the canonical single arrow.

---

## 5. Exact ↔ symmetric, coexact ↔ antisymmetric: the reversibility weld

### 5.1 The cell-local dictionary, reproduced and promoted

On the tetrahedron $K_4$ (one cell), the certificate re-derives the Paper 01b split in the integer normalization $M=4I-J$, for a general quadratic vector field $F$ carried into the frame:
$$\operatorname{tr}S=\operatorname{div}F\quad(\text{residual }0),\qquad A=\tfrac12\widetilde K(\operatorname{curl}F)\quad(\text{residual }0),$$
$$F=\operatorname{grad}f\Rightarrow A=0,\qquad F=\operatorname{curl}B\Rightarrow\operatorname{tr}S=0.$$
The first pair is the $S/A$ content of the field Jacobian; the second pair is the Helmholtz diagonalization. **Exact (gradient) ⇒ symmetric (no current); coexact (curl) ⇒ trace-free (pure current).**

Promoted to the cochain level on every complex (`cert_hodge_arrow.py` block (C)):

- **curl·grad $=0$:** $d_1d_0=0$ — every exact cochain is closed (a gradient has no curl).
- **div·curl $=0$:** $d_0^\top d_1^\top=0$ — every coexact cochain is co-closed (a curl is divergence-free).
- **harmonic closed-and-co-closed:** every $h\in\ker L_1$ satisfies $d_1h=0$ and $d_0^\top h=0$.

These are exactly the statements "$\operatorname{curl}\operatorname{grad}=0$", "$\operatorname{div}\operatorname{curl}=0$", and "harmonic = both", now on a complex, and they place the three Hodge sectors in correspondence with the symmetric (exact), antisymmetric (coexact), and protected-arrow (harmonic) sectors of the reversibility split.

### 5.2 The self-adjoint instrument is blind to the current

**Proposition 5.1 (Self-adjoint blindness, simplicial-complex form).** *Let $T=T_{\mathrm{sym}}+C$ act on $C^1$, with $T_{\mathrm{sym}}=I-tL_1$ symmetric and $C=-C^\top$ an antisymmetric circulation supported on the harmonic (cycle) sector. Then the symmetric quadratic form $q(x)=\langle x,Tx\rangle$ satisfies $q(x)=\langle x,T_{\mathrm{sym}}x\rangle$ for all $x$ — it is identically blind to $C$ — whereas a two-sided (predictor) probe recovers $C=\tfrac12(T-T^\top)\neq0$.*

*Proof.* $\langle x,Cx\rangle=0$ for every real $x$ because $C$ is antisymmetric; hence $q(x)=\langle x,T_{\mathrm{sym}}x\rangle+\langle x,Cx\rangle=\langle x,T_{\mathrm{sym}}x\rangle$. The predictor reads $\tfrac12(T-T^\top)=C$. $\square$

This is the *Irreversible Blind Spot* (Lemma 1: $\langle h,Ah\rangle=0$) on the simplicial frame: the harmonic current — the $\beta_1$-dimensional arrow — lives in the kernel of every symmetric instrument and is recoverable only by a non-self-adjoint probe. `cert_hodge_arrow.py` block (D) confirms, on every $\beta_1\geq1$ complex, that $\max_x|\langle x,Tx\rangle-\langle x,T_{\mathrm{sym}}x\rangle|$ is at machine zero ($\lesssim 10^{-14}$) while $\|\tfrac12(T-T^\top)\|>0$. A single-encoder objective (which probes only $\langle h,Th\rangle$) cannot encode the arrow; the predictor head (two charts, the SVD of $T$) is the minimal device that does — the simplicial realization of *Curvature and Current* Thm 7 and the *Predictive DSL* improvement (§5.4).

### 5.3 The general-$N$ bridge (Direction 1)

`cert_generalN_bridge.py` makes the weld to the general-$N$ $K_N$ program exact:

- **(1) Metric = $K_N$ Laplacian.** $M=N I-J=L_0(K_N)$ for $N=3,\dots,7$, with eigenvalues $N$ (multiplicity $N-1$, on $H$) and $0$ (the gauge line). The Gram matrix is $G=L_0/(N-1)$ on $H$. At $N=4$ this is Paper 01's $4I-J$.
- **(2) Filled simplex acyclic.** The complete $N$-vertex complex has $\beta_1=0=\dim\ker L_1$ for $N=4,\dots,7$: a single solid simplex carries no current.
- **(3) $k$-skeleton Betti.** The $k$-skeleton of the $(N-1)$-simplex is a wedge of $k$-spheres: $\beta_1(K_N)=\binom{N-1}{2}$ and $\beta_2=\binom{N-1}{3}$, verified for $N=4,\dots,7$. This is the general-$N$ count of how many independent currents the frame skeleton can carry.
- **(4) $L_1$ spectrum.** On the filled $N$-vertex simplex the nonzero $L_1$ spectrum is the single integer $N$ with full multiplicity — the same eigenvalue $L_0$ has on $H$.

Result (4) is the sharpest new observation of this paper (§7): the filled simplex is "Hodge-flat" with a single integral eigenvalue $N$ at every degree where it acts, mirroring the scalar action $N$ of the metric on $H$.

### 5.4 Predictive DSL on the simplicial frame (validation design)

The *Predictive (two-chart) DSL* improvement applies verbatim. A Deep Sturm–Liouville encoder built from one self-adjoint eigenbasis — here the eigenbasis of $L_1$ (or of its exact-sector restriction) — lives in the $A=0$ corner and is arrow-blind. The two-chart predictor learns the operator $T$ itself; its optimum is the SVD of $T$, and the recovered antisymmetric part $\tfrac12(P-P^\top)$ of the predictor head reads the harmonic arrow. On a $\beta_1=1$ annulus the single recoverable arrow is the circulation around the hole, with strength the gap $\Delta=\sum\sigma(T)-\sum\lambda(S)\geq0$ ($=0$ at detailed balance). A trained confirmation is provided as a **GCP-only torch script** (`gcp_only_predictive_dsl_simplicial.py`, **not run locally** — see the constraints note), mirroring the program's E11/e67 recipe: single-chart loss reversal-invariant (blind); two-chart $|\widehat\omega|$ tracking the installed current and flipping under time reversal. The deterministic gate is the sympy/numpy certificate of §6; the torch script is an optional out-of-gate validation.

---

## 6. Exact-arithmetic verification

Two deterministic certificates, sympy/numpy only (no floating point in the load-bearing checks; numpy used for independent spectral cross-checks with residuals reported). Both return **ALL GREEN** under `py` (Python 3.13, sympy 1.14, numpy 2.4).

**`empirical_forward3/cert_hodge_arrow.py`.**
- **(B)** $\dim\ker L_1=\beta_1$ on the seven complexes (Table, §4), each three independent ways plus a numpy spectrum nullity cross-check.
- **(H)** Hodge decomposition: $d_1d_0=0$; dimensions add to $|E|$; three projectors mutually orthogonal ($\sim10^{-16}$) and summing to $I$ (spanning).
- **(C)** Cell-local Paper 01b weld on $K_4$ ($\operatorname{tr}S=\operatorname{div}F$; $A=\tfrac12\widetilde K(\operatorname{curl}F)$; grad ⇒ $A=0$; curl ⇒ $\operatorname{tr}S=0$), then cochain-level curl·grad $=0$, div·curl $=0$, harmonic closed-and-co-closed on every complex.
- **(D)** Self-adjoint blindness: symmetric form blind to an installed harmonic current (residual $\lesssim10^{-14}$) while the predictor's antisymmetric part is nonzero, on every $\beta_1\geq1$ complex.

**`empirical_forward3/cert_generalN_bridge.py`.** The four general-$N$ statements of §5.3, for $N=3,\dots,7$ (exact ranks via sympy; numpy spectra reported).

---

## 7. Novelty versus organization

We are explicit, as the program requires.

- **Classical, re-presented.** The discrete Hodge decomposition $C^1=\operatorname{im}d_0\oplus\operatorname{im}d_1^\top\oplus\ker L_1$ and the identity $\dim\ker L_1=\beta_1$ are textbook discrete exterior calculus / combinatorial Hodge theory [Eckmann, Hirani, Lim, Desbrun–Hirani–Leok–Marsden]. The graph Laplacian of $K_N$, the contractibility of the filled simplex, and the $k$-skeleton Betti numbers $\binom{N-1}{k+1}$ are standard. None is claimed new.
- **New here.** (a) The **identification of the discrete Hodge sectors with Paper 01b's curvature/current split** of the field Jacobian — exact = symmetric/$A=0$, coexact = antisymmetric/$\operatorname{tr}S=0$, harmonic = the protected arrow — promoting the single-cell dictionary $A=\tfrac12\widetilde K(\operatorname{curl}F)$ to the complex, where the harmonic sector first appears and equals $\beta_1$. (b) The explicit **weld to the program's reversibility-axis blind-spot results** (Irreversible Blind Spot, Curvature and Current, Predictive DSL): the $\beta_1$ harmonic sector *is* the topologically protected arrow, in the kernel of every self-adjoint instrument; the predictor is the lift. (c) The observation that the **nonzero $L_1$ spectrum on the filled $N$-simplex is the single integer $N$** with full multiplicity, matching the scalar action of the metric $M=N I-J$ on $H$ — the "Hodge-flat" general-$N$ statement.

The honest one-line summary: the Hodge theory is organization; its *identification with the simplicial-frame $S/A$ split and the reversibility arrow*, and the integral $L_1=N$ spectrum on the filled simplex, are the new content. The conceptual payoff is that one object — the discrete coboundary chain $d_0,d_1$ on a simplicial complex — simultaneously carries Paper 01b's curl, the program's irreversible arrow, and the general-$N$ frame metric, with $\beta_1$ as the dimension of the protected current.

---

## 8. Open problems

Ordered most-tractable to highest-ceiling.

- **O1 (Weighted / metric Hodge Laplacian).** Replace the standard cochain inner products by the simplicial ($M$-)metric weights, giving a weighted $L_1$. Does $\dim\ker L_1=\beta_1$ persist (it must, by Hodge), and what is the weighted spectrum on the $K_N$ skeleton? *Tractable; concrete.*
- **O2 (Higher Betti as higher arrows).** The $2$-Hodge-Laplacian $L_2=d_1^\top d_1+d_2 d_2^\top$ has $\dim\ker L_2=\beta_2$; on the $K_N$ skeleton $\beta_2=\binom{N-1}{3}$. Is there an "order-$2$ current" reading (a flux of fluxes) matching the cumulant-tower order axis of Direction 2? *Medium; bridges Directions 2 and 3.*
- **O3 (Mesh independence and de Rham).** Make precise the FEEC commuting diagram between Paper 01b's continuum operators on a refining tetrahedral mesh and the discrete $d_0,d_1$, so that the harmonic $\beta_1$ is the mesh-independent (de Rham) arrow of *Curvature and Current* Thm 5. *Standard FEEC; engineering.*
- **O4 (Trained predictive-DSL on the frame).** Run the GCP-only torch validation (§5.4) and, if it confirms, write the short "Predictive DSL on the simplicial frame" note. *Out-of-gate; gated on GCP.*
- **O5 (Apex/archimedean reading).** Does the program's apex/archimedean reflection operator admit a harmonic-cochain realization on a simplicial complex whose $\beta_1$ is the relevant count? *Speculative; highest ceiling — flagged forward-only.*

---

## References

[Desbrun–Hirani–Leok–Marsden] Desbrun, M., Hirani, A.N., Leok, M., Marsden, J.E. "Discrete Exterior Calculus." arXiv:math/0508341 (2005).

[Eckmann] Eckmann, B. "Harmonische Funktionen und Randwertaufgaben in einem Komplex." *Commentarii Mathematici Helvetici* 17, 240–255 (1944). [Discrete Hodge theorem: harmonic cochains $\cong$ cohomology.]

[Hirani] Hirani, A.N. *Discrete Exterior Calculus*. Ph.D. thesis, Caltech, 2003.

[Lim] Lim, L.-H. "Hodge Laplacians on graphs." *SIAM Review* 62(3), 685–715 (2020).

[Paper 01] Murillo Montero, L. *Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane*. v2, 2026. DOI 10.5281/zenodo.19689049.

[Paper 01b] Murillo Montero, L. *Intrinsic Differential Calculus on Simplicial (Quadray) Coordinates: Gradient, Divergence, Curl, and the Gauge–Hodge Decomposition*. Draft 1, 2026.

[Paper 01c] Murillo Montero, L. *The Moving Amari–Chentsov Cubic in Simplicial (Quadray) Coordinates*. Draft 1, 2026.

---

*[End of Draft 1.]*
