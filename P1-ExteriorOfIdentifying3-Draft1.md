# \heb[P]{פ}1 — From the Boundary: The Exterior of *Identifying 3*

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 29, 2026*

## Abstract

**Situation.** The interior trilogy *Identifying 3* — [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) (the native simplicial chart), [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) (the cumulant tower), [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) (character orthogonality on the conductor lattice) — together with the keystone [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985), coordinatizes the categorical probability simplex *from its center*. It linearizes at the uniform $p_*=\tfrac1N\mathbf 1$ onto the **signed** tangent hyperplane $H$, inhabits the **smooth analytic** interior (finite gauge exponent $\beta$), and organizes everything on a clean two-axis grid: gauge $\beta$ (which power-mean is affine) $\times$ order $n$ (which cumulant/tensor). It is coherent and powerful, and the interior choice bought analytic tractability honestly.

**Gap.** Everywhere the *boundary* appears in the trilogy it is demoted — to a "caveat" ([\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s boundary caveat, where the square-root chart's derivative blows up), to an undeveloped Legendre dual ([\heb{ל}2](https://doi.org/10.5281/zenodo.20338126), where $\Phi^*=-\,$Shannon entropy is named but never given its boundary life), to a conflation of two distinct posets ([\heb{ל}3](https://doi.org/10.5281/zenodo.20339049), divisor lattice vs. support lattice), to a one-dimensional shadow ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s tropical and conjugate-potential sections, where the rich face lattice is collapsed to two endpoints). The genesis ontology that motivated the whole program — *origin-out, boundary-first, non-negative, face-indexed* (Murillo Montero, Feb. 2025) — was quietly converted into *manifold-in, center-first, signed, interior* analysis. The boundary is the part the formalization dropped.

**Action.** Restore the boundary as a co-equal primary face, without retrofitting the interior. We (i) read $p_*$ as the **generator** (Origin-and-Destination) from which the frame, the reflection, and every "special" property descend; (ii) make the **non-negative cone** primary, with the signed tangent $H$ its *mirror across $p_*$* (the genesis's "negatives are reflections over the origin," made structural); (iii) inhabit the **$r=-\infty$ tropical gauge** that the genesis already used as `massaction` (subtract-the-minimum) and that [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) names but never enters; and (iv) build the unifying object — the apex generator read over the **face lattice / Newton polytope** — giving each of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) its exterior.

**Result.** Five structural recoveries, each proved. (1) The genesis's hand-derived distance $r^2=l^2+n^2+m^2-ln-lm-nm$ is *exactly* the simplicial Gram form, hence the Fisher metric at $p_*$ up to the Chentsov scale — the interior metric, derived in Feb. 2025 from the law of cosines on $120^\circ$ rays, before any information geometry (\hyperref[sec:1]{§1}). (2) [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s square-root chart is a **stratified map** of the simplex's face complex onto the sphere's orthant-face complex, recursively self-similar, with $p_*$ the generating apex (\hyperref[sec:4]{§4}). (3) [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s undeveloped Legendre dual is the **Cramér rate function** whose effective domain is the Newton polytope $\operatorname{conv}\{e_i\}=\Delta$, whose faces are the support strata, and whose tower radius is the distance to the nearest Lee–Yang zero; [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s one-dimensional rate function is its contraction along a single direction (\hyperref[sec:5]{§5}). (4) The **support/face (Boolean) lattice** sits alongside [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s divisor lattice; the cubic selection rule $a+b+c\equiv 0\ (\mathrm{mod}\ N)$ survives on a face only when the face is a subgroup coset, and dissolves otherwise (\hyperref[sec:6]{§6}). (5) The interior two-axis grid $(\beta,n)$ plus the **support/face axis** is the full picture, organized by the apex over the face lattice with $p_*$ the generator and the exterior derivative $\partial$ — the operator paper 01 deferred — the structural map (\hyperref[sec:7]{§7}).

**Harvest.** The categorical simplex carries two dual theories. The interior (\heb{ל}, *lamed*: ascending, center, signed, analytic, $d$) and the exterior (\heb[P]{פ}, *pe*: spiraling, boundary, non-negative, tropical, $\partial$) are co-equal faces of one object, joined at $p_*$. The exterior edge is where *zeros* live: the additive Lee–Yang zeros of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) and the multiplicative $L$-zeros of the multiplicative apex (T8) are a boundary/tropical phenomenon the interior cannot see by construction. \heb[P]{פ}1 lays the exterior foundation; the GRH-shaped payoff is named as the destination (\hyperref[sec:8]{§8}), held with calibrated faith, and not claimed.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
A probability over \(N\) outcomes can be looked at two ways. From the inside: sit at the perfectly balanced distribution in the middle, and study small wiggles around it --- the view the first trilogy took, and the reason its mathematics is so clean. From the outside: start at the edges, where some outcomes have probability exactly zero, and ask which outcomes are \emph{present} and which are \emph{absent}. The second view is the one the author's original 2025 notes actually started from --- numbers are non-negative magnitudes, a region of space is named by which coordinate is missing, and you normalize by subtracting the smallest coordinate so one of them hits zero. The first trilogy quietly traded that picture for the tidy inside view. This paper restores the outside view as an equal partner: the simplex's corners and edges form a lattice of ``which outcomes survive,'' the rate function of large-deviation theory lives on exactly that lattice, and the place where this all points --- still far off, named here but not reached --- is the boundary edge where the zeros of \(L\)-functions sit.
\end{mdframed}

---

\clearpage

## Notation {#sec:notation}

| Symbol | Meaning |
|---|---|
| $N$ | Number of categorical outcomes; integer $\geq 2$. |
| $\Delta^{N-1}$ | Probability simplex $\{p\in\mathbb R^N: p_i\ge 0,\ \sum_i p_i=1\}$. |
| $\mathbb T=\mathbb R_{\ge 0}$ | The genesis **True Numbers**: zero or a positive real. The cone is $\mathbb T^N$. |
| $H$ | Zero-sum hyperplane $\{x\in\mathbb R^N:\sum_i x_i=0\}$ — the signed tangent space (interior). |
| $p_*$ | Uniform distribution $\tfrac1N\mathbf 1$; the **generator** (Origin-and-Destination). |
| $\mathbf 1$ | The gauge direction $(1,\dots,1)$. |
| $G$ | Simplicial Gram matrix $\tfrac{N}{N-1}I-\tfrac{1}{N-1}J$ ($J$ all-ones); the geometric metric. |
| $e_i$ | Standard basis / vertex (deterministic distribution); $\operatorname{conv}\{e_i\}=\Delta^{N-1}$. |
| $\tau_i$ | Centered vertex direction $e_i-p_*$; the frame ray from the generator to vertex $i$. |
| $\sigma_{p_*}$ | Central involution $p\mapsto 2p_*-p$ (point reflection through $p_*$). |
| $\operatorname{supp}(p)$ | Support $\{i:p_i>0\}$; the **present** coordinates. Its complement is **absent**. |
| $F_S$ | Closed face $\{p\in\Delta^{N-1}:p_i=0\ \forall i\notin S\}\cong\Delta^{|S|-1}$, for $\emptyset\ne S\subseteq\{1,\dots,N\}$. |
| $\mathcal B_N$ | Boolean / **support lattice**: nonempty $S\subseteq\{1,\dots,N\}$ ordered by inclusion = face lattice of $\Delta^{N-1}$. |
| $\mathcal D_N$ | **Divisor lattice**: divisors $d\mid N$, the substrate of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s conductor packets $H_d$. |
| `mass`$(x)$ | `massaction`: $x\mapsto x-(\min_i x_i)\mathbf 1$, the genesis standard-form normalization (\hyperref[sec:3]{§3}). |
| $\psi$ | Square-root (amplitude) map $\psi(p)=(\sqrt{p_1},\dots,\sqrt{p_N})$; $S^{N-1}_+$ its image. |
| $Z(\eta),\Phi$ | Categorical partition function $\sum_i e^{\eta_i}$ and $\Phi=\log Z$ ([\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)); $\eta\in H$. |
| $K_y(\beta)$ | Scalar apex generator $\log\tfrac1N\sum_i e^{\beta y_i}$ of the centered log-ledger $y\in H$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)). |
| $\Phi^*,\ K_y^*$ | Legendre–Fenchel conjugates; the rate functions (\hyperref[sec:5]{§5}). |
| $D(P\Vert Q)$ | Kullback–Leibler relative entropy $\sum_i P_i\log(P_i/Q_i)$. |
| $\beta,\ n$ | The interior grid axes: gauge exponent $\beta\in\mathbb R\cup\{\pm\infty\}$; cumulant/tensor order $n$. |

---

\clearpage

## Acronyms {#sec:acronyms}

| Short | Expansion |
|---|---|
| AC | Amari–Chentsov (3-tensor); the cubic vertex $T_{ijk}=\partial^3\Phi$. |
| ETF | Equiangular tight frame (the simplicial frame; paper 01 Prop. 2.0). |
| FR | Fisher–Rao (metric). |
| KL | Kullback–Leibler (relative entropy / divergence). |
| LDP | Large-deviation principle (Cramér's theorem). |
| min-plus | The tropical semiring $(\mathbb R\cup\{+\infty\},\min,+)$; the $r=-\infty$ gauge. |
| QFI | Quantum Fisher information ($=4\,g_{\mathrm{Bures}}$); the minimal monotone metric (T7). |
| GRH | Generalized Riemann Hypothesis (the forward-door north star, \hyperref[sec:8]{§8}). |

---

## 1. The genesis, and the metric it already held {#sec:1}

This series begins where the program began: not with the formal apparatus but with a set of intuition notes, *A New Model for Any-Dimensional Space* (Murillo Montero, February 2, 2025). Their ontology is **origin-out and boundary-first**, and four of their moves are the load-bearing seeds of the exterior theory. We name them in the genesis's own vocabulary, because that vocabulary is the authentic seed and canonicalizing it is part of the task.

- **True Numbers.** $\mathbb T=\mathbb R_{\ge 0}=\{0\text{ or a positive real}\}$ are primary; *negatives are not fundamental*. A signed quantity is a pair of non-negative magnitudes on opposite rays ($+3=(3,0)$, $-2=(0,2)$), and "$-1$ is a mirror illusion," the reflection of $+1$ over the origin. Points are non-negative; only *differences* are signed.
- **Origin-and-Destination.** The seed is the $0$-model: "the space is just a point... the equilibrium of all components. Balance." The origin is simultaneously the source from which space is built outward (by adding $n+1$ maximally symmetric rays) and the destination to which the corridor flows.
- **massaction (standard form).** A point with all coordinates positive is reduced by *subtracting the minimum*: $(l,n,m)\mapsto(l-\mu,n-\mu,m-\mu)$ with $\mu=\min(l,n,m)$. At least one coordinate becomes zero.
- **The absent-coordinate region rule.** "The zero denotes which coordinate is absent... identify a region by the absent coordinate."

The genesis was then *formalized* in paper 01 (Murillo Montero 2026, *Intrinsic Vector Algebra on Simplicial Coordinates*): the $N$ rays became an equiangular tight frame, the redundancy $\mathbf 1$ the gauge direction, the canonical gauge the zero-sum hyperplane $H$ obtained by *subtracting the mean*, and the Gram metric $G$ fixed. Paper 01 reads $H$ as the tangent space of the categorical simplex at $p_*=\tfrac1N\mathbf 1$ (its Cor. 3.9), and *explicitly defers* the differential and boundary operators ($\nabla,\operatorname{div},\operatorname{curl}$, and the exterior $d$, $\partial$). The interior trilogy then took the center-first road. Two of the genesis's four seeds survived the formalization (the frame, and subtract-the-mean); two were dropped (subtract-the-minimum, and the absent-coordinate face rule). The dropped pair is the exterior.

We open by showing the genesis already *contained* the interior's central metric — so that the exterior reading is not a reinterpretation imposed from outside but the recovery of structure that was present at the source.

\hypertarget{stmt:1-1}{}
**Proposition 1.1 (The genesis distance is the Fisher metric at the generator).** *Let the simplicial frame $\{v_i\}_{i=1}^N\subset\mathbb R^{N-1}$ be unit vectors from the origin to the vertices of the regular $(N-1)$-simplex, with $v_i\cdot v_j=-\tfrac1{N-1}$ for $i\ne j$. For a ledger $c=(c_1,\dots,c_N)$ the squared distance from the origin of $p=\sum_i c_i v_i$ is*
$$
r^2(c)\;=\;\sum_i c_i^2-\frac{2}{N-1}\sum_{i<j}c_ic_j\;=\;c^\top G\,c ,\qquad G=\tfrac{N}{N-1}I-\tfrac{1}{N-1}J .
$$
*This form is gauge-invariant ($G\mathbf 1=0$); on the zero-sum section it equals $\tfrac{N}{N-1}\sum_i c_i^2$. For $N=3$ it is the genesis's hand-derived plane distance*
$$
r^2=l^2+n^2+m^2-ln-lm-nm=\tfrac32\textstyle\sum_i c_i^2\big|_H ,
$$
*and for $N=4$ the genesis's tetrahedral-space distance $r^2=\sum_i c_i^2-\tfrac23\sum_{i<j}c_ic_j=\tfrac43\sum_i c_i^2\big|_H$. In every case $r^2$ is the Fisher–Rao metric of the categorical simplex at the uniform $p_*$, up to the positive constant $N-1$ that Chentsov's theorem leaves free.*

*Proof.* Expanding the ambient norm, $r^2=\big(\sum_i c_iv_i\big)\!\cdot\!\big(\sum_j c_jv_j\big)=\sum_i c_i^2\,(v_i\cdot v_i)+2\sum_{i<j}c_ic_j\,(v_i\cdot v_j)=\sum_i c_i^2-\tfrac{2}{N-1}\sum_{i<j}c_ic_j$, which is $c^\top G c$ for $G$ as displayed. Since $G\mathbf 1=\big(\tfrac{N}{N-1}-\tfrac{N}{N-1}\big)\mathbf 1=0$, the form depends only on the gauge class of $c$. On the zero-sum section $\sum_i c_i=0$, squaring gives $\sum_{i<j}c_ic_j=-\tfrac12\sum_i c_i^2$, whence $r^2=\sum_i c_i^2-\tfrac{2}{N-1}\!\cdot\!\big(-\tfrac12\sum_i c_i^2\big)=\tfrac{N}{N-1}\sum_i c_i^2$ (paper 01, Prop. 2.1). The two cosines are $v_i\cdot v_j=-\tfrac12$ ($N=3$, the $120^\circ$ rays) and $-\tfrac13$ ($N=4$, the tetrahedral $109.47^\circ$ rays), giving the genesis's two formulas with cross-term coefficients $1$ and $\tfrac23$ and section values $\tfrac32\sum c_i^2$ and $\tfrac43\sum c_i^2$. By [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) the Fisher–Rao metric at $p_*$ is $g_{FR}|_{p_*}(v,w)=N\langle v,w\rangle$ on $H$, i.e. $N\sum_i c_i^2$; therefore $g_{FR}|_{p_*}=(N-1)\,r^2$ on $H$. Chentsov's theorem fixes the Fisher metric only up to a positive scalar, so $r^2$ and $g_{FR}|_{p_*}$ are the same metric. $\square$

\hypertarget{stmt:1-2}{}
**Remark 1.2 (What this licenses).** In February 2025, by the law of cosines on $120^\circ$ rays, the genesis wrote down the Fisher information metric at the uniform — the order-2 content of the entire interior tower ([\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) order 2) — before any information geometry was invoked. The interior series recovered this metric analytically and built upward (orders $3,4,\dots$) and inward (the smooth center). The exterior series takes the *other* three genesis seeds — the non-negative cone (\hyperref[sec:2]{§2}), `massaction`/the absent coordinate (\hyperref[sec:3]{§3}), and the face-indexed boundary (\hyperref[sec:4]{§4}–\hyperref[sec:7]{§7}) — that the formalization set aside, and builds the dual theory on them. The genesis is not a heuristic prelude to the interior; it is the common root of both faces.

---

## 2. True Numbers, the generator, and the mirror {#sec:2}

The interior works on the signed hyperplane $H$: scores, differences $p-q$, natural parameters, the cumulant arena. The genesis works in the cone $\mathbb T^N$ of True Numbers: probabilities $p_i\ge 0$, amplitudes $a_i=\sqrt{p_i}\ge 0$. These are not competing conventions; they are reflections of each other, and $p_*$ is the mirror. This section makes the reflection structural (facet **B**) and recasts $p_*$ from "distinguished point" to "generator" (facet **A**).

### 2.1 The cone is primary; the tangent is its reflection {#sec:2-1}

\hypertarget{stmt:2-1}{}
**Definition 2.1 (Central involution).** The **central involution** through the generator is the affine map
$$
\sigma_{p_*}:\mathbb R^N\to\mathbb R^N,\qquad \sigma_{p_*}(p)=2p_*-p .
$$

\hypertarget{stmt:2-2}{}
**Proposition 2.2 (Cone$\leftrightarrow$$H$ reflection).** *Restricted to the affine hyperplane $A=\{p:\sum_i p_i=1\}$, the involution $\sigma_{p_*}$ fixes $p_*$, maps $A$ onto $A$, and has derivative $-\,\mathrm{id}$ on the tangent $H$. Writing a point as $p=p_*+v$ with $v\in H$, its mirror is $\sigma_{p_*}(p)=p_*-v$, with coordinates $\sigma_{p_*}(p)_i=\tfrac1N-v_i$. The signed tangent direction $-v$ is thereby realized as the reflection of the cone point $p$ through $p_*$. For $N>2$ the simplex $\Delta^{N-1}$ is **not** centrally symmetric, so the mirror generally leaves the cone: $\sigma_{p_*}(p)_i<0$ as soon as $v_i>\tfrac1N$ (i.e. $p_i>\tfrac2N$). This is exactly the genesis's "$-1$ is a mirror illusion" — the mirror of a True-Number point is generally not a True-Number point, only a direction — with the origin read as the generator $p_*$. (Only $N=2$, where $\Delta^1$ is a segment symmetric about $p_*$, is the degenerate case in which the mirror looks like a genuine point.)*

*Proof.* $\sigma_{p_*}(p_*)=2p_*-p_*=p_*$, and $\sigma_{p_*}$ is its own inverse. For $p\in A$, $\sum_i(2p_*-p)_i=2-1=1$, so $\sigma_{p_*}(A)=A$. The map $p\mapsto 2p_*-p$ is affine with linear part $-\,\mathrm{id}$, which preserves $H=T_{p_*}A$ and acts as $-1$ there. Writing $p=p_*+v$, $\sigma_{p_*}(p)=p_*-v$, with $i$-th coordinate $\tfrac2N-p_i=\tfrac1N-v_i$, negative exactly when $v_i>\tfrac1N$, equivalently $p_i>\tfrac2N$ — which occurs for points in the cone (e.g. near any vertex). For $N=2$, $A$ is a line and $\Delta^1$ a segment symmetric about $p_*$, so $\sigma_{p_*}$ preserves it. $\square$

The content of \hyperlink{stmt:2-2}{Proposition~2.2} is a clean division of labor that the interior blurs by working only in $H$:

> **Points are non-negative (the cone $\mathbb T^N$); tangents are signed (the hyperplane $H$); $p_*$ is the reflection center between them.** A negative coordinate never denotes a probability — it denotes a *direction*, recovered as the mirror image of a True-Number point across the generator.

This is the structural form of the genesis's refusal of fundamental negatives. The interior's signed objects (scores, $p-q$, the $e$-flat natural parameter $\eta$) are *mirror-doubles* of cone objects; the exterior keeps the cone primary and reads $H$ as its $-1$ eigenspace under $\sigma_{p_*}$.

### 2.2 $p_*$ as generator, not special point {#sec:2-2}

The interior repeatedly singles out $p_*$ as "the nice point": max-entropy, scalar Fisher information, fixed point of the $\beta$-flow, center of the cumulant expansion, the place where character orthogonality is exact ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985); [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)). The genesis treats it differently — as the *seed*. We make the generative reading primary and *derive* specialness from it.

\hypertarget{stmt:2-3}{}
**Proposition 2.3 ($p_*$ generates the interior data).** *Let $p_*=\tfrac1N\mathbf 1$. Then:*

1. *(Unique balance.) $p_*$ is the unique point of $\Delta^{N-1}$ fixed by the full relabeling group $S_N$.*
2. *(Frame source.) The centered vertex directions $\tau_i:=e_i-p_*$ are the rays from $p_*$ to the vertices; they lie in $H$, sum to $0$, and (rescaled to unit simplicial norm) are exactly the equiangular tight frame of paper 01. Thus the frame is the spray of $p_*$ toward the corners.*
3. *(Reflection center.) $p_*$ is the unique fixed point in $A$ of the involution $\sigma_{p_*}$ of \hyperref[sec:2-1]{§2.1}.*
4. *(Derived specialness.) Max-entropy, scalar Fisher information $\tfrac1N I_H$, and "$\beta$-flow fixed point" all follow from (1): any $S_N$-invariant functional or metric is extremized/isotropic at the unique $S_N$-fixed point.*

*Proof.* (1) $S_N$ permutes coordinates; a fixed probability vector has all coordinates equal, forcing $p_*$; conversely $p_*$ is fixed. (2) $\tau_i=e_i-\tfrac1N\mathbf 1$ has $\sum_k(\tau_i)_k=1-1=0$ so $\tau_i\in H$, and $\sum_i\tau_i=\sum_i e_i-\mathbf 1=0$; their pairwise simplicial inner products are equal by symmetry, which is the equiangular tight-frame condition (paper 01, $\tau_i=e_i-\tfrac14\mathbf1$ at $N=4$). (3) Immediate from \hyperlink{stmt:2-2}{Proposition~2.2}. (4) Shannon entropy, the Fisher form, and the mean-fitness functional $p\mapsto\mathbb E_p[y]$ are all $S_N$-equivariant; their Hessians/gradients at the unique invariant point are $S_N$-invariant tensors on $H$, hence scalar (the standard representation of $S_N$ on $H$ is irreducible), giving isotropy and criticality. $\square$

So the interior's "distinguished point" is the *image* of the genesis generator: $p_*$ sprays the frame, centers the reflection, and — being the unique balance — forces every symmetric quantity to be critical and isotropic there. We will see in \hyperref[sec:7]{§7} that it also generates the *dynamics*: the $\beta$-flow is the corridor flowing out from the Origin $p_*$ to the tropical Destinations on the faces.

---

## 3. The massaction gauge: subtract-the-minimum, and the absent coordinate {#sec:3}

Paper 01 canonicalized *subtract-the-mean* (the $L^2$/arithmetic gauge, orthonormal Helmert contrasts, [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)). The genesis used a different normalization — *subtract-the-minimum* — and it is exactly the boundary gauge the corridor of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) names at $r=-\infty$ but never inhabits.

\hypertarget{stmt:3-1}{}
**Definition 3.1 (massaction).** For $x\in\mathbb R^N$ define the **massaction normalization**
$$
\mathrm{mass}(x)\;=\;x-\big(\min_i x_i\big)\mathbf 1 .
$$

\hypertarget{stmt:3-2}{}
**Proposition 3.2 (massaction is the min-plus canonical section, valued in the face lattice).** *The map $\mathrm{mass}$ has the following properties.*

1. *(Gauge section.) $\mathrm{mass}(x)$ depends only on the class $[x]\in\mathbb R^N/\mathbb R\mathbf 1$, is idempotent, and is the unique representative of $[x]$ with $\min_i=0$. It is the canonical section of the tropical (min-plus) projective torus, exactly as subtract-the-mean is the canonical section of the Euclidean quotient.*
2. *(Lands on the boundary.) $\mathrm{mass}(x)\in\partial\,\mathbb T^N$: at least one coordinate is $0$. The vanishing set $Z(x):=\{i:\mathrm{mass}(x)_i=0\}=\arg\min_i x_i$ is the genesis's **absent coordinate(s)**.*
3. *(Face index.) The assignment $[x]\mapsto Z(x)$ sends each min-plus class to a nonempty subset, i.e. a face label in the support lattice $\mathcal B_N$; the closed cell on which $Z(x)\supseteq\{i\}$ is the "region where coordinate $i$ is absent," and "identify a region by the absent coordinate" is the statement that $\mathcal B_N$ is the indexing poset of the standard forms.*

*Proof.* (1) For $k\in\mathbb R$, $\mathrm{mass}(x+k\mathbf1)=x+k\mathbf1-(\min_i x_i+k)\mathbf1=\mathrm{mass}(x)$, so it factors through $\mathbb R^N/\mathbb R\mathbf1$; $\min_i\mathrm{mass}(x)_i=0$ gives idempotence and, since two representatives of $[x]$ with $\min=0$ differ by a multiple of $\mathbf1$ that preserves the minimum only if it is $0$, uniqueness. In min-plus geometry, $\mathbb R^N/\mathbb R\mathbf1$ with the tropical scaling $\lambda\odot x=x+\lambda\mathbf1$ has $\{x:\min_i x_i=0\}$ as a fundamental domain; $\mathrm{mass}$ is the retraction onto it. (2),(3) Immediate from $\min_i\mathrm{mass}(x)_i=0$ and $Z(x)=\arg\min_i x_i$. $\square$

Two normalizations, two gauges, two literatures: subtract-the-mean is the smooth $L^2$ gauge of the interior (orthonormal contrasts, Gaussian shadow), and subtract-the-minimum is the tropical $L^\infty$/min-plus gauge of the exterior (corner structure, large deviations). The corridor of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) is precisely the one-parameter bridge $r\in\mathbb R\cup\{\pm\infty\}$ between them, and `massaction` is its $r=-\infty$ endpoint, the genesis's working coordinate. (Polar to it, $r=+\infty$ is subtract-the-maximum, the max-plus winner-take-all gauge; the involution $x_i\leftrightarrow -x_i$ swaps them.) The genesis even wrote the subtracted minimum with a placeholder glyph — the same *lamed* that names the interior series — a quiet sign that the exterior gauge was hiding inside the interior's own letter from the first page.

> **The interior normalizes to the center (subtract the mean); the exterior normalizes to the boundary (subtract the minimum). The first lands in $H$; the second lands on a face, labeled by the absent coordinate.**

This is the entry to the third axis. Subtract-the-mean throws away no support information but sees no faces; subtract-the-minimum sees exactly the faces. The remaining sections develop what lives there.

---

## 4. The exterior of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872): the stratified amplitude complex {#sec:4}

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) builds the square-root chart $\psi(p)=(\sqrt{p_1},\dots,\sqrt{p_N})$, identifying the simplex with the positive orthant $S^{N-1}_+$ of the unit sphere and the Fisher–Rao metric with the pulled-back round metric. Its boundary caveat then writes the demotion down explicitly: "$\psi$ is smooth only on the open interior... at boundary points $\partial\psi_i/\partial p_i=1/(2\sqrt{p_i})$ diverges and the simplex acquires corner structure where the tangent is not $H_0$... all subsequent statements are on the open interior." And yet [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) already half-sees the exterior: "edges (where some $p_i=0$) map to great-circle arcs (where the same $a_i=0$)." That sentence is the face$\,\mapsto\,$sub-sphere map, never developed as a stratification. We develop it.

### 4.1 The face complex and its image {#sec:4-1}

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (Faces are recursive sub-simplices; $\psi$ is a stratified isomorphism).** *For $\emptyset\ne S\subseteq\{1,\dots,N\}$ let $F_S=\{p\in\Delta^{N-1}:p_i=0\ \forall i\notin S\}$. Then:*

1. *(Recursive faces.) $F_S\cong\Delta^{|S|-1}$ is the categorical simplex on the sub-alphabet $S$ (a sub-distribution on the present outcomes). The face poset $\{F_S\}$ ordered by inclusion is the support lattice $\mathcal B_N$, which is the face lattice of $\Delta^{N-1}$.*
2. *(Image is the spherical sub-orthant.) $\psi(F_S)=\{a\in S^{N-1}_+:a_i=0\ \forall i\notin S\}=S^{|S|-1}_+$, and $\psi|_{F_S}$ is the [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) square-root chart of $\Delta^{|S|-1}$ itself.*
3. *(Stratified isomorphism.) $\psi$ is a homeomorphism $\Delta^{N-1}\to S^{N-1}_+$ carrying the face stratification onto the orthant-face stratification; it is a smooth diffeomorphism on each open stratum $\mathring F_S$, and the induced map of face posets is the identity on $\mathcal B_N$.*

*Proof.* (1) On $F_S$ the constraints $p_i=0\ (i\notin S)$ and $\sum_{i\in S}p_i=1$ define $\Delta^{|S|-1}$; closure relations $F_S\subseteq F_{S'}\iff S\subseteq S'$ are immediate, and the face lattice of the standard simplex is the inclusion poset of nonempty subsets. (2) $\sqrt{\cdot}$ preserves the vanishing locus $\{p_i=0\}=\{a_i=0\}$ and maps $\Delta^{|S|-1}$ to $S^{|S|-1}_+$ by definition; the restriction is the same square-root map on the sub-alphabet. (3) $\psi$ is a continuous bijection of compact Hausdorff spaces, hence a homeomorphism; smoothness on each open stratum is that of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) applied to $\Delta^{|S|-1}$; the poset map is the identity by (1)–(2). $\square$

Call the resulting object — the orthant $S^{N-1}_+$ together with all its sub-orthant faces $S^{|S|-1}_+$, glued along the lattice $\mathcal B_N$ — the **stratified amplitude complex**. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart is then *recursively self-similar*: the same construction appears on every face, and the generator $p_*$ recurs as the center $p_*^S=\tfrac1{|S|}\mathbf 1_S$ of each stratum. The deepest stratum (full support $S=\{1,\dots,N\}$) is the interior [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) inhabits; the exterior is the descending tower of its faces.

### 4.2 Two boundary phenomena that must not be conflated {#sec:4-2}

The divergence $\partial\psi_i/\partial p_i=1/(2\sqrt{p_i})\to\infty$ as $p_i\to0$ is real, but it is a *specific* phenomenon, and the launch of an exterior theory is exactly where it can be confused with a different one.

\hypertarget{stmt:4-2}{}
**Remark 4.2 (Square-root branch vs. tropical limit).** *The $1/(2\sqrt{p_i})$ blow-up is the square-root (Born) chart's branch singularity in the direction normal to a face: $\psi$ is a smooth diffeomorphism within each open stratum, but its derivative transverse to the stratum boundary diverges, which is exactly the statement that $\psi$ is a stratified map and not a single smooth manifold chart across strata. This is **not** the tropical limit. The tropical/min gauge of \hyperref[sec:3]{§3} (the $r=-\infty$ corridor endpoint) is a separate chart that coordinatizes the same faces cleanly, with no branch singularity — `massaction` is smooth (piecewise linear), not square-root. The two phenomena share only their locus, the boundary $\{$some $p_i=0\}$; they are different maps of it. The exterior object proper is the stratified amplitude complex (orthant $+$ all faces, glued along $\mathcal B_N$); the tropical gauge is the well-behaved coordinate on its strata.*

This is the first place the exterior reading earns its keep precisely by *refusing* a tempting conflation. The interior's "boundary caveat" bundles two distinct facts — a chart's branch singularity, and the existence of a corner/face structure — into one sentence and then sets both aside. Separated, the second is not a caveat at all: it is the face lattice, on which the next two sections build the rate function and the support combinatorics.

---

## 5. The exterior of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126): the rate function on the Newton polytope {#sec:5}

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) builds the cumulant tower from one functional $\Phi(\eta)=\log Z(\eta)=\log\sum_i e^{\eta_i}$: $\nabla\Phi=p$ (position), $\nabla^2\Phi=\Sigma$ (Fisher), $\nabla^3\Phi=T$ (the AC cubic), and higher cumulants. This is the $\beta=0$ germ at the center. [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) already names the Legendre dual $\Phi^*=-\,$Shannon entropy (the $m$-flat/mixture chart) — so, contrary to a first reading, the conjugate is *not absent*. What is missing is its **boundary life**. We supply it.

### 5.1 The effective domain is the Newton polytope; faces are support strata {#sec:5-1}

\hypertarget{stmt:5-1}{}
**Theorem 5.1 (The conjugate lives on the Newton polytope, stratified by support).** *Let $Z(\eta)=\sum_{i=1}^N e^{\eta_i}=\sum_i e^{\langle\eta,e_i\rangle}$ be the categorical partition function (a function on $\eta\in\mathbb R^N$; [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) gauge-fixes the natural parameter to the slice $\eta\in H$), and $\Phi=\log Z$. Then the convex conjugate $\Phi^*(p)=\sup_{\eta\in\mathbb R^N}(\langle\eta,p\rangle-\Phi(\eta))$ satisfies:*

1. *(Newton polytope.) $\operatorname{dom}\Phi^*=\Delta^{N-1}=\operatorname{conv}\{e_1,\dots,e_N\}$, which is the **Newton polytope** of the exponential sum $Z$ (the convex hull of its exponent vectors $e_i$). Off the polytope, $\Phi^*=+\infty$.*
2. *(Negative entropy.) On the polytope, $\Phi^*(p)=\sum_i p_i\log p_i=-H(p)$ (with $0\log 0:=0$), the dual potential [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) named.*
3. *(Faces are support strata.) The face $F_S$ of the Newton polytope is exactly the support stratum $\{p:\operatorname{supp}(p)\subseteq S\}$, and $\Phi^*|_{F_S}=-H_S$ is the negative entropy of the sub-simplex $\Delta^{|S|-1}$ on $S$. The boundary values of $\Phi^*$ are therefore the entropies of the support-restricted distributions.*

*Proof.* (1)–(2) For the log-sum-exp $\Phi$, the conjugate is the negative entropy restricted to the simplex: this is the standard Legendre dual of the categorical log-partition (Wainwright–Jordan 2008; Rockafellar 1970). The normalization constraint is forced by the gauge direction: along $\eta=c\mathbf 1$, $\langle c\mathbf1,p\rangle-\Phi(c\mathbf1)=c(\sum_i p_i-1)-\log N\to+\infty$ unless $\sum_i p_i=1$; positivity $p_i\ge0$ is forced along $\eta_i\to-\infty$; off $\Delta^{N-1}$ the sup is therefore $+\infty$. The exponent vectors of $Z(\eta)=\sum_i e^{\langle\eta,e_i\rangle}$ are the $e_i$, so the Newton polytope is $\operatorname{conv}\{e_i\}=\Delta^{N-1}$, coinciding with $\operatorname{dom}\Phi^*$. (3) A face of the standard simplex is $F_S$ for some $S$ (\hyperlink{stmt:4-1}{Proposition~4.1}), and $\{p\in\Delta:\operatorname{supp}(p)\subseteq S\}=F_S$; restricting $\sum_i p_i\log p_i$ to $p_i=0\ (i\notin S)$ gives $\sum_{i\in S}p_i\log p_i=-H_S(p)$. $\square$

So the cumulant tower (the $\beta=0$ germ of $\Phi$, the interior) and the negative-entropy rate function (the global conjugate $\Phi^*$, the exterior) are the two ends of one Legendre involution, and the exterior end *lives on the face lattice*. The Newton polytope is the categorical simplex itself — the same object [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) charts and the same face lattice \hyperref[sec:4]{§4} stratifies. The interior reads $\Delta^{N-1}$ as the domain of probabilities; the exterior reads it as the Newton polytope of the apex, whose faces carry the rate function's boundary values.

### 5.2 [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s one-dimensional rate function is a contraction of this {#sec:5-2}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) builds, with full rigor, the *scalar* conjugate $K_y^*(\xi)=\sup_\beta(\beta\xi-K_y(\beta))$, a Cramér rate function on the interval $[\min_i y_i,\max_i y_i]$, with the celebrated boundary values $K_y^*(\max)=\log(N/m_+)=D(\mathrm{Unif}(I_+)\Vert u)$ (its Cor. 2.8). This is exact and load-bearing — and it is the **one-dimensional shadow** of \hyperlink{stmt:5-1}{Theorem~5.1}.

\hypertarget{stmt:5-2}{}
**Theorem 5.2 ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s rate function is the contraction of $\Phi^*$ along $y$).** *Fix a centered log-ledger $y\in H$ and let $K_y(\beta)=\log\tfrac1N\sum_i e^{\beta y_i}$ be the scalar apex generator. Then, with $D(p\Vert u)=\log N-H(p)=\Phi^*(p)+\log N$,*
$$
K_y^*(\xi)\;=\;\min_{\,p\in\Delta^{N-1}}\big\{\,D(p\Vert u):\langle y,p\rangle=\xi\,\big\},
$$
*the contraction (image rate function) of the support-stratified $\Phi^*$ under the linear readout $p\mapsto\langle y,p\rangle$. The two endpoints $\xi=\max_i y_i$ and $\xi=\min_i y_i$ are attained on the faces $F_{I_+}$ and $F_{I_-}$ (argmax and argmin support strata), where the minimizer is $\mathrm{Unif}(I_\pm)$ and $K_y^*=\log(N/m_\pm)=\Phi^*(\mathrm{Unif}(I_\pm))+\log N$. Thus [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Cor. 2.8 is \hyperlink{stmt:5-1}{Theorem~5.1} evaluated on the two extreme faces, and the scalar corridor collapses the $(N-1)$-dimensional face lattice $\mathcal B_N$ to its image interval, retaining only the two extreme faces.*

*Proof.* By the contraction principle (Dembo–Zeitouni 1998, Thm. 4.2.1) applied to the Sanov-type rate function $D(\cdot\Vert u)$ on $\Delta^{N-1}$ and the continuous map $p\mapsto\langle y,p\rangle$, the empirical-mean rate function is $\xi\mapsto\inf\{D(p\Vert u):\langle y,p\rangle=\xi\}$. By Cramér's theorem this empirical-mean rate function is $K_y^*$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.7.3), giving the displayed identity (the infimum is attained by compactness and is the escort $P_\beta$ with $K_y'(\beta)=\xi$). At $\xi=\max_i y_i$ the constraint forces $\operatorname{supp}(p)\subseteq I_+$, i.e. $p\in F_{I_+}$, and on that face $D(\cdot\Vert u)=\log N-H$ is minimized by the uniform $\mathrm{Unif}(I_+)$ with value $\log N-\log m_+=\log(N/m_+)$; this matches [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Cor. 2.8. The interval $[\min y,\max y]=\langle y,\Delta^{N-1}\rangle$ is the image of the polytope under the readout, and a generic fiber meets many faces, all but the two extreme of which are invisible to the scalar value alone. $\square$

This is the precise sense in which [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) "drew the two-axis grid and shadowed the third axis to one dimension": its rate function is the projection of the full, support-stratified rate function $\Phi^*$ onto a single line, and that projection keeps only the argmax/argmin faces. Promoting the shadow to the full poset $\mathcal B_N$ is the work of the exterior.

### 5.3 The tower radius is the distance to the nearest Lee–Yang zero {#sec:5-3}

The cumulant tower of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) is a Taylor series at $\beta=0$; its radius of convergence is a boundary quantity.

\hypertarget{stmt:5-3}{}
**Proposition 5.3 (Tower radius $=$ nearest zero $=$ how far $\beta$ pushes before a face dominates).** *The radius of convergence of the cumulant tower $K_y(\beta)=\sum_{n\ge2}\tfrac{\kappa_n}{n!}\beta^n$ equals the distance from $0$ to the nearest complex zero of $Z_y(\beta)=\tfrac1N\sum_i e^{\beta y_i}$ — the nearest **Lee–Yang point** of the apex ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.2.1). At $N=2$ with $y=(-a,a)$ this radius is $\pi/(2a)$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Prop. 2.5). As real $\beta\to\pm\infty$ the escort $P_\beta$ concentrates on the argmax/argmin face $F_{I_\pm}$; the finite tower radius is the analytic measure of how far the gauge can be pushed before that face-domination begins to control the generator.*

*Proof.* $K_y=\log Z_y$ is holomorphic on the largest disk about $0$ that is zero-free for the entire function $Z_y$, and acquires a logarithmic branch point at each zero; hence the Taylor radius is the modulus of the nearest zero ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.2.1 and its proof). The $N=2$ value is $Z_y=\cosh(a\beta)$ with nearest zero $i\pi/(2a)$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Prop. 2.5). The escort concentration is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Def. 2.3 / Thm. 2.2.5. $\square$

The radius is an *exterior* datum (a distance to a zero, a boundary of the analytic domain) controlling an *interior* object (the convergence of the center's Taylor tower). For $N\ge3$ the zero locus is not pinned to a line by elementary arithmetic ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)); its study is a genuine exterior problem, and (\hyperref[sec:8]{§8}) the natural home of the program's zeros.

### 5.4 The boundary mirror of the "leap to 3" {#sec:5-4}

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) makes the third cumulant the hinge: $\kappa_3=T_{ijk}$ is the first invariant Riemannian geometry cannot see, vanishing for $N=2$ at the center and first appearing at $N=3$ ($T_{111}|_{p_*}=\tfrac{2}{27}$). The exterior carries the *same* third-order content on the boundary.

\hypertarget{stmt:5-4}{}
**Proposition 5.4 ($\kappa_3$ is the interior germ of the argmax/argmin face asymmetry).** *Let $y\in H$ be non-degenerate. The following are equivalent: (i) the rate function $K_y^*$ is symmetric, $K_y^*(\xi)=K_y^*(-\xi)$; (ii) the value multiset $\{y_i\}$ is symmetric under $y\mapsto-y$; (iii) all odd cumulants vanish, $\kappa_3=\kappa_5=\cdots=0$. When they fail, $\kappa_3$ is the leading obstruction: near the center $\xi=0$,*
$$
K_y^*(\xi)=\frac{\xi^2}{2\kappa_2}-\frac{\kappa_3}{6\,\kappa_2^3}\,\xi^3+O(\xi^4),
$$
*and on the boundary the same asymmetry appears as the argmax/argmin face skew*
$$
K_y^*\big(\max_i y_i\big)-K_y^*\big(\min_i y_i\big)=\log\frac{m_-}{m_+}
$$
*([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Cor. 2.8). Both the cubic germ at the center and the face-multiplicity skew at the boundary are obstructions to the $y\mapsto-y$ symmetry, and they vanish simultaneously.*

*Proof.* (ii)$\Rightarrow$(i): $y\mapsto-y$ sends $K_y(\beta)\mapsto K_y(-\beta)$ and hence $K_y^*(\xi)\mapsto K_y^*(-\xi)$; if the multiset is invariant then $K_y$ is even and $K_y^*$ is even. (i)$\Rightarrow$(iii): an even $K_y^*$ forces an even $K_y$ (Legendre duality preserves parity), whose odd Taylor coefficients $\kappa_{2m+1}$ vanish. (iii)$\Rightarrow$(ii): the cumulants determine the law of the finite multiset, and vanishing odd cumulants force symmetry under negation. The Edgeworth/Legendre inversion of $\xi=K_y'(\beta)$ about $\beta=0$ gives the displayed expansion (standard; e.g. inverting $\xi=\kappa_2\beta+\tfrac{\kappa_3}{2}\beta^2+\cdots$ and substituting into $K_y^*=\beta\xi-K_y$). The boundary skew is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Cor. 2.8: $K_y^*(\max)-K_y^*(\min)=\log(N/m_+)-\log(N/m_-)=\log(m_-/m_+)$. Symmetry of $\{y_i\}$ forces $m_+=m_-$ and matching argmax/argmin geometry, so both obstructions vanish together. $\square$

The interior reads $\kappa_3$ as a germ at the center (the AC tensor, the cubic vertex); the exterior reads the identical third-order asymmetry as a relation between two faces of the Newton polytope (the $m_+\ne m_-$ skew). One is local and analytic; the other is global and combinatorial; they are the interior and exterior faces of the program's "$3$." We do not claim they are numerically equal — the germ is a Taylor coefficient and the skew a face statistic — only that they are the two avatars of the same parity obstruction, born together and dying together.

---

## 6. The exterior of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049): the support lattice beside the divisor lattice {#sec:6}

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) endows the outcome set with the ring $\mathbb Z/N$ and decomposes $H$ into **conductor packets** $H_d$ ($d\mid N$), proving that order 2 is arithmetically diagonal while order 3 carries the selection rule $a+b+c\equiv0\ (\mathrm{mod}\ N)$. The genesis points at a *different* poset on the same outcomes — the **support lattice** $\mathcal B_N$ of which $p_i$ vanish. The exterior of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) is the interplay of the two posets, and what becomes of the selection rule when a face breaks the ring.

### 6.1 Two posets, and the faces where they meet {#sec:6-1}

The divisor lattice $\mathcal D_N$ (interior, arithmetic) and the support lattice $\mathcal B_N$ (exterior, combinatorial) are genuinely different objects on $\{1,\dots,N\}$, and a face is *not* a sub-ring.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    every node/.style={font=\small},
    nd/.style={draw, thick, circle, minimum size=2.0em, inner sep=0pt},
    cover/.style={thick, gray!55}
]
  % --- Left: divisor lattice D_6 (interior) ---
  \begin{scope}[xshift=0cm]
    \node[nd] (d1) at (0,0)    {$1$};
    \node[nd] (d2) at (-1.3,1.6){$2$};
    \node[nd] (d3) at (1.3,1.6) {$3$};
    \node[nd] (d6) at (0,3.2)   {$6$};
    \draw[cover] (d1)--(d2); \draw[cover] (d1)--(d3);
    \draw[cover] (d2)--(d6); \draw[cover] (d3)--(d6);
    \node[below] at (0,-0.7) {(a) divisor lattice $\mathcal D_6$ (interior)};
    \node[above] at (0,3.7) {\footnotesize packets $H_d$, $\dim=\varphi(d)$};
  \end{scope}
  % --- Right: support lattice B_3 = face lattice of the triangle (exterior) ---
  \begin{scope}[xshift=7.5cm]
    \node[nd] (s1) at (-1.6,0) {$1$};
    \node[nd] (s2) at (0,0)    {$2$};
    \node[nd] (s3) at (1.6,0)  {$3$};
    \node[nd] (s12) at (-1.6,1.6){$12$};
    \node[nd] (s13) at (0,1.6)   {$13$};
    \node[nd] (s23) at (1.6,1.6) {$23$};
    \node[nd] (s123) at (0,3.2) {$123$};
    \draw[cover] (s1)--(s12); \draw[cover] (s2)--(s12);
    \draw[cover] (s1)--(s13); \draw[cover] (s3)--(s13);
    \draw[cover] (s2)--(s23); \draw[cover] (s3)--(s23);
    \draw[cover] (s12)--(s123); \draw[cover] (s13)--(s123); \draw[cover] (s23)--(s123);
    \node[below] at (0,-0.7) {(b) support lattice $\mathcal B_3$ = faces of $\Delta^2$ (exterior)};
    \node[above] at (0,3.7) {\footnotesize face $F_S\cong\Delta^{|S|-1}$};
  \end{scope}
\end{tikzpicture}
\caption{The interior and exterior posets on the outcome set are different lattices. (a)~The divisor lattice $\mathcal D_6$ of \href{https://doi.org/10.5281/zenodo.20339049}{\heb{ל}3}: nodes are divisors $d\mid 6$, carrying conductor packets $H_d$ of dimension $\varphi(d)$; the cubic selection rule couples packets across this lattice. (b)~The support lattice $\mathcal B_3$ of the exterior: nodes are nonempty supports $S\subseteq\{1,2,3\}$, i.e. the faces of the triangle $\Delta^2$, ordered by inclusion. A generic face $F_S$ carries no ring structure; the two lattices meet only at the special faces whose support is a subgroup coset (\hyperref[sec:6-2]{§6.2}).}
\label{fig:two-lattices}
\end{figure}

\hypertarget{stmt:6-1}{}
**Proposition 6.1 (A face is generically not a sub-ring).** *Let $S\subseteq\mathbb Z/N$ be a support and $F_S$ its face. Then $F_S$ carries an inherited cyclic structure compatible with $\mathbb Z/N$ if and only if $S$ is a coset of a subgroup, i.e. $S=t+\tfrac{N}{d}\,\mathbb Z/N$ for some $d\mid N$ and $t\in\mathbb Z/N$ (so $|S|=d$), in which case $F_S$ inherits the cyclic group $\cong\mathbb Z/d$. For a generic (non-coset) $S$, $F_S$ is merely the unstructured sub-simplex $\Delta^{|S|-1}$ with symmetry $S_{|S|}$ and no ring. In particular the conductor/quotient operation $\mathbb Z/N\twoheadrightarrow\mathbb Z/d$ of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) (which acts on the full alphabet) and face restriction to $S$ (which deletes letters) are distinct operations.*

*Proof.* A subset closed under the induced affine/group structure of $\mathbb Z/N$ and forming a coset is exactly a coset of a subgroup; subgroups of $\mathbb Z/N$ are $\tfrac{N}{d}\mathbb Z/N\cong\mathbb Z/d$ for $d\mid N$, and their cosets have size $d$. A non-coset $S$ is not translation-closed, so no group law restricts to it; its only canonical symmetry is the relabeling group $S_{|S|}$ of the deleted-alphabet simplex. The quotient map is defined on all of $\mathbb Z/N$ and identifies residues mod $d$ (it does not delete outcomes), whereas $F_S$ deletes the outcomes outside $S$; these change the alphabet in incompatible ways. $\square$

### 6.2 What survives of the selection rule on a face {#sec:6-2}

\hypertarget{stmt:6-2}{}
**Proposition 6.2 (Degeneration of the cubic selection rule).** *Restrict the cubic vertex $T$ to a face $F_S$ (i.e. to character modes supported on the present outcomes $S$).*

1. *(Coset face: the subgroup rule survives.) If $S=t+\tfrac{N}{d}\mathbb Z/N$ is a subgroup coset, the additive selection rule $a+b+c\equiv0\ (\mathrm{mod}\ N)$ restricts to the subgroup rule of $\mathbb Z/d$: writing characters of $F_S$ through the inherited $\mathbb Z/d$ structure, the surviving constraint is $a'+b'+c'\equiv0\ (\mathrm{mod}\ d)$. The interior arithmetic of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) persists, on the smaller modulus.*
2. *(Generic face: the rule dissolves.) If $S$ is not a coset, no modular selection rule survives. The cubic vertex on $F_S$ is [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s dense Amari–Chentsov tensor on the unstructured alphabet $S$, constrained by nothing finer than the relabeling symmetry $S_{|S|}$.*

*Proof.* (1) On a subgroup coset, translating to the subgroup $\tfrac Nd\mathbb Z/N$ and using the isomorphism with $\mathbb Z/d$, additive characters of $\mathbb Z/N$ that are constant on cosets descend to characters of $\mathbb Z/d$; the orthogonality computation of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) (term 1, $\tfrac1N\sum_i\chi_{a+b+c}(i)=\delta_{a+b+c\equiv0}$) then reads, on the subgroup, $\delta_{a'+b'+c'\equiv0\ (d)}$. (2) Without a group law on $S$, [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s stipulation fails; the construction of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) reverts to that of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126), whose AC tensor on the sub-alphabet is dense (its (3) with $p_i=1/|S|$ on $S$), with only $S_{|S|}$ symmetry. $\square$

So the genuine open exterior question raised by [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — *what survives of $a+b+c\equiv0\ (\mathrm{mod}\ N)$ on a face where the ring is broken?* — has a clean answer at the two extremes (subgroup rule on coset faces; nothing on generic faces) and an open middle: the full combinatorics of how $\mathcal B_N$ and $\mathcal D_N$ interleave, and which faces of $\mathcal B_N$ are coset faces, is the unbuilt exterior of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049). The coset faces are exactly the meeting locus of the two posets in Figure 1.

### 6.3 The tropical skeleton of the apex {#sec:6-3}

The additive apex also has a *tropical skeleton*, dual to the Newton polytope of \hyperref[sec:5]{§5}.

\hypertarget{stmt:6-3}{}
**Proposition 6.3 (Tropical skeleton $=$ corner locus $=$ normal fan of $\Delta^{N-1}$).** *The tropicalization of the partition function, $\operatorname{trop} Z(\eta)=\max_i \eta_i$, is non-smooth exactly on the set $\{\eta:\arg\max_i\eta_i\text{ is not a singleton}\}$. This **tropical hypersurface** is the codimension-$\ge1$ skeleton dual to the face lattice of the Newton polytope $\Delta^{N-1}$ (its normal fan): the cell where $\arg\max=S$ is dual to the face $F_S$. It is the boundary locus on which the winner-take-all escort ($\beta\to+\infty$) changes which face $F_{I_+}$ it concentrates on.*

*Proof.* $\operatorname{trop}Z=\lim_{\beta\to\infty}\tfrac1\beta\log\sum_i e^{\beta\eta_i}=\max_i\eta_i$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.2.5, Maslov dequantization). The function $\max_i\eta_i$ is piecewise linear, smooth where the maximizer is unique, with non-differentiability locus where two or more coordinates tie; this locus is the codimension-$\ge1$ skeleton of the normal fan of $\Delta^{N-1}=\operatorname{conv}\{e_i\}$, whose cones $\{\eta:\arg\max_i\langle\eta,e_i\rangle=S\}$ are dual to the faces $F_S$ (Maclagan–Sturmfels 2015). The argmax cell controls the limiting escort by [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Def. 2.3. $\square$

The interior's smooth analytic apex and the exterior's tropical skeleton are the two limits ($\beta$ finite vs. $\beta\to\pm\infty$) of one generator, dual to the two readings of $\Delta^{N-1}$ (probability simplex vs. Newton polytope). The skeleton is combinatorially the face lattice $\mathcal B_N$ again — the third axis, seen now as the normal fan.

---

## 7. The unifying object: the apex over the face lattice, and the third axis {#sec:7}

The three exteriors of \hyperref[sec:4]{§§4}–6 are one object seen three ways. We state it.

> **The unifying object is the apex generator read over the face lattice of its Newton polytope $\Delta^{N-1}=\operatorname{conv}\{e_i\}$.** The interior two-axis grid — gauge $\beta$ (which power-mean is affine) $\times$ order $n$ (which cumulant/tensor) — describes a *single* cell of this object: the full-support, center-anchored cell. The **support/face axis** $S\in\mathcal B_N$ is the third dimension, indexing which face the escort, the rate function, and the tropical skeleton live on. The interior $(\beta,n)$-grid plus the support axis $S$ is the full picture.

\hypertarget{stmt:7-1}{}
**Theorem 7.1 (The three axes, and the role of each ingredient).** *On the categorical apex the following hold simultaneously and consistently:*

1. *(Center, $\beta=0$, $S=\{1,\dots,N\}$.) The cumulant tower of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) is the germ at the generator $p_*$, with $\Sigma$ the Fisher metric ($=$ the genesis metric of \hyperlink{stmt:1-1}{Proposition~1.1}) and $T$ the AC cubic; the order axis $n$ is the Taylor depth.*
2. *(Corridor, $\beta\in\mathbb R\cup\{\pm\infty\}$, $S$ fixed at full support until the endpoints.) The gauge axis is the power-mean corridor of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985); the $\beta$-flow is the replicator flow from the Origin $p_*$ ($\beta=0$) to the tropical Destinations on the faces $F_{I_\pm}$ ($\beta\to\pm\infty$). "Origin and Destination" is this flow.*
3. *(Faces, $S\in\mathcal B_N$.) The support axis is the face lattice; the rate function $\Phi^*$ (\hyperref[sec:5]{§5}) takes its boundary values there, the stratified amplitude complex (\hyperref[sec:4]{§4}) is its geometric carrier, and the support/divisor interplay (\hyperref[sec:6]{§6}) is its arithmetic. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) built the one-dimensional shadow of this axis (the interval $[\min y,\max y]$, two faces); \hyperlink{stmt:5-2}{Theorem~5.2} promotes it to the full poset.*

*Proof.* (1) is [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) with \hyperlink{stmt:1-1}{Proposition~1.1} for the metric. (2) is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.4 (the $\beta$-flow is the Shahshahani/replicator gradient flow of $p\mapsto\mathbb E_p[y]$) together with Thm. 2.2.5 (the endpoints land on $\arg\max/\arg\min$); the flow starts at the $S_N$-fixed $p_*$ (\hyperlink{stmt:2-3}{Proposition~2.3}) and ends on $F_{I_\pm}$. (3) collects \hyperlink{stmt:5-1}{Theorems~5.1}–\hyperlink{stmt:5-2}{5.2}, \hyperlink{stmt:4-1}{Proposition~4.1}, and \hyperlink{stmt:6-1}{Propositions~6.1}–\hyperlink{stmt:6-3}{6.3}. Consistency of the three readings is the single Legendre involution $(\beta,K_y)\leftrightarrow(\xi,K_y^*)$ of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 2.7 carried over the face lattice. $\square$

\hypertarget{stmt:7-2}{}
**Remark 7.2 (The exterior series is the $\partial$ to the interior's $d$).** Paper 01 already carries the exterior algebra ($\wedge$, the Hodge star $\star$ in its cross-product $K(u)=\star(u\wedge\cdot)$) and *explicitly defers* the exterior derivative $d$ and the boundary operator $\partial$ (paper 01). The interior series develops the $d$-side: differentiate the generator $\Phi$ at the center, climb the cumulant tower, flow smoothly. The exterior series developed here is the $\partial$-side: the boundary operator on the face complex $\mathcal B_N$ ($\partial F_S=\sum$ of its codimension-one faces), on which the rate function lives, the amplitude complex stratifies, and the tropical skeleton sits as the dual fan. \heb{ל} ascends through the interior; \heb[P]{פ} spirals around the boundary. They are the two halves of the calculus paper 01 set out to build and deliberately left open. This is a structural reading, not yet a theorem identifying $\partial$ with a specific discrete-exterior-calculus coboundary on the simplex's skeleton; that identification is a forward door (\heb[P]{פ}-series, later papers).

---

## 8. Forward door: the exterior edge is where the zeros live {#sec:8}

The reason the exterior is not a stylistic exercise is that the program's number-theoretic content — its RH-shaped questions — is, by construction, a boundary phenomenon, and the interior cannot see it. We state the thread forward-only, with calibrated faith, and we do not claim it.

**Zeros are an exterior object.** A zero of an apex generator is where its logarithm loses analyticity — the boundary of the zero-free domain. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) named the additive **Lee–Yang zeros** of $Z_y$ and showed (\hyperlink{stmt:5-3}{Proposition~5.3} above) that the nearest one sets the interior tower's radius. On the multiplicative side, the multiplicative apex generator on the units $(\mathbb Z/N)^\times$,
$$
\mathcal D_x(\beta,\psi)=\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\psi(s)},
$$
and its finite Dirichlet polynomial $L_x(\beta,\psi)$ (the multiplicative companion, T8) are the finite analogs of the Dirichlet $L$-function $L(s,\chi)=\sum_n\chi(n)n^{-s}$, whose non-trivial zeros are the GRH locus on the critical line $\Re s=\tfrac12$. The zeros of $L_x(\beta,\psi)$ in $\beta\in\mathbb C$, and their relation to the edge of the critical strip, are the multiplicative continuation of the additive Lee–Yang story: the same exterior phenomenon on the units.

**Why the interior cannot reach it.** The interior is, by definition, the smooth analytic center: finite $\beta$, the convergent cumulant tower, the isotropic Fisher metric at $p_*$. The object that lives on the critical edge — a zero, a face where the Euler product loses a prime, the boundary of the convergence abscissa — is exactly what the center's analytic machinery is built to avoid. T8 states the program's own assessment outright: *the RH-shaped questions of the program live most naturally on the multiplicative apex* — that is, on the boundary.

**Calibrated faith.** Leo's RH effort has reached a *structural reduction*, not a proof: at a fixed primorial modulus, RH has been reduced to a degeneracy condition on a functional-equation cluster, with referee-level proofs of the easy arrows and a proof outline for the hard one. The exterior/boundary/face/tropical structure built here is the *candidate missing ingredient* for the object on the critical edge — the multiplicative Lee–Yang/tropical boundary, the rate-function edge, the face where a prime drops out of the Euler product. This is a **conjecture about where to build**, to be *earned* as the \heb[P]{פ}-series matures (especially its multiplicative and boundary papers), not asserted here.

\hypertarget{stmt:8-1}{}
**Conjecture 8.1 (Forward door, calibrated — not proved in \heb[P]{פ}1).** *The exterior apex over the face lattice — additive Lee–Yang zeros ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)) continued to multiplicative $L$-zeros on the units (T8), read as the tropical/boundary edge of the multiplicative apex $\mathcal D_x$ — is the natural home of the program's GRH-shaped questions, and the structure required to close the hard arrow of the existing structural reduction lives there rather than in the interior. \heb[P]{פ}1 builds the foundation (the face lattice, the rate function on it, the cone$\leftrightarrow$$H$ reflection, the inhabited tropical gauge); the multiplicative/boundary \heb[P]{פ}-papers are charged with reaching it.*

**A second exterior axis (quantum).** T7 lifts the apex to complex amplitudes, where the coordinate hyperplanes $\{z_s=0\}$ are reduced-rank/reduced-support strata — the **quantum face lattice** — and $\beta\to\pm\infty$ is ground-state/dominant-eigenvector projection. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Rem. 2.7a gives the *metric* fork on the boundary (Kubo–Mori vs. Bures/QFI); the support/rank fork of T7 is the orthogonal exterior axis. Both are boundary phenomena, invisible to the interior's single isotropic center, and both are forward doors of the \heb[P]{פ}-series.

---

## 9. The trade, and what the exterior hands forward {#sec:9}

Honesty about the trade is required, because the interior choice was not free and neither is the exterior one.

**The interior bought tractability.** Linearizing at $p_*$ on the signed $H$, inhabiting the smooth cells (finite $\beta$), and organizing by the $(\beta,n)$ grid bought: the Chentsov-unique Fisher metric, convergent cumulant towers, the exact character orthogonality of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049), and the clean dually-flat duality of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985). This is real analytic power, honestly earned.

**The exterior trades it for harder structure.** Working the boundary trades smooth analytic machinery for tropical and combinatorial structure: non-analytic edges (where the square-root branch of \hyperref[sec:4]{§4} and the tropical limit of \hyperref[sec:3]{§3} both live, distinct but co-located); divergent towers beyond the Lee–Yang radius (\hyperref[sec:5-3]{§5.3}); face posets $\mathcal B_N$ of exponential size ($2^N-1$ supports) in place of the divisor lattice's $\tau(N)$ nodes; and Chentsov uniqueness replaced, on the quantum boundary, by the whole monotone-metric family ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Rem. 2.7a). The exterior is not a free reinterpretation of the interior; it is a different, harder theory on the part the interior set aside, and it should be named as such.

**The two are twins, not a correction.** The interior series stays exactly as it is — coherent, powerful, complete as the interior theory. \heb[P]{פ}1 does not retrofit it. The relationship is duality: \heb{ל} (center, signed, analytic, $d$) and \heb[P]{פ} (boundary, non-negative, tropical, $\partial$); the faces to the center, the tropical to the analytic, the Newton polytope to the smooth chart.

**What the exterior hands forward.** This first paper puts in place the five exterior primitives the rest of the \heb[P]{פ}-series will use: (i) $p_*$ as generator (\hyperref[sec:2]{§2}); (ii) the cone$\leftrightarrow$$H$ reflection (\hyperref[sec:2]{§2}); (iii) the inhabited $r=-\infty$ tropical (`massaction`) gauge (\hyperref[sec:3]{§3}); (iv) the apex over the face lattice / Newton polytope, with its rate function, stratified amplitude complex, support/divisor interplay, and tropical skeleton (\hyperref[sec:4]{§§4}–7); and (v) the exterior calculus $\partial$ — paper 01's deferred boundary operator — as the structural map of the series (\hyperref[sec:7]{§7}). The next paper, \heb[P]{פ}2, gives the exterior of the gauge trilogy [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) (the tropical/min ladder against [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s subtract-mean Helmert ladder; the Lee–Yang/tropical edge of [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s harmonic corridor; and the Origin$\to$Destination $\beta$-flow of [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s Born gauge, whose winner-take-all limit is already the genesis's Destination). The multiplicative and quantum boundary papers carry the thread of \hyperref[sec:8]{§8} toward the edge where the zeros live.

The interior series mapped the center. This series maps the edge — the spiral that was there from the first page of the genesis, waiting for its $\partial$.

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7 and 4.8, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of the derivations presented in this paper. These collaborations were productive for real-time derivation checking, literature contextualization, and iterative exposition. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## References {#sec:references}

Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs 191. American Mathematical Society.

Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs 53. American Mathematical Society. (Russian original 1972.)

Dembo, A. and Zeitouni, O. (1998). *Large Deviations Techniques and Applications.* 2nd ed. Applications of Mathematics 38. Springer. (Cramér's theorem, Thm. 2.2.3; the contraction principle, Thm. 4.2.1.)

Lee, T. D. and Yang, C. N. (1952). Statistical theory of equations of state and phase transitions. II. Lattice gas and Ising model. *Physical Review* 87, 410–419.

Litvinov, G. L. and Maslov, V. P., eds. (2005). *Idempotent Mathematics and Mathematical Physics.* Contemporary Mathematics 377. American Mathematical Society.

Maclagan, D. and Sturmfels, B. (2015). *Introduction to Tropical Geometry.* Graduate Studies in Mathematics 161. American Mathematical Society. (Newton polytopes, normal fans, tropical hypersurfaces.)

Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Author's notes, February 2, 2025. (The genesis: True Numbers, Origin-and-Destination, `massaction`, the absent-coordinate region rule.)

Murillo Montero, L. (2026). *Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.19689049](https://doi.org/10.5281/zenodo.19689049). (Paper 01: the ETF frame, gauge direction, zero-sum hyperplane; Prop. 2.1, Cor. 3.9; the deferred $\nabla,\operatorname{div},\operatorname{curl},d,\partial$.)

Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint, DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (The gauge corridor; the apex $K_y(\beta)$; tropical compactification; Lee–Yang zeros; conjugate potential / rate function / dually-flat structure; Kubo–Mori vs. Bures.)

Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint, DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).

Murillo Montero, L. (2026). *[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint, DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).

Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint, DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).

Murillo Montero, L. (2026). *[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector.* Zenodo preprint, DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442). (The decoherent face; reduced-rank strata; Fubini–Study, Bures/QFI.)

Murillo Montero, L. (2026). *T8 — The Multiplicative Apex and Finite Dirichlet Polynomials.* Companion manuscript (in preparation). (The multiplicative apex $\mathcal D_x(\beta,\psi)$ on units; finite Dirichlet polynomials; "the RH-shaped questions of the program live most naturally on the multiplicative apex.")

Rockafellar, R. T. (1970). *Convex Analysis.* Princeton Mathematical Series 28. Princeton University Press. (Legendre–Fenchel transform; effective domains.)

Wainwright, M. J. and Jordan, M. I. (2008). Graphical models, exponential families, and variational inference. *Foundations and Trends in Machine Learning* 1(1–2), 1–305. (The log-partition conjugate is the negative entropy on the simplex.)
