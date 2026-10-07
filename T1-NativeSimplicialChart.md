# \heb{ל}1 — Identifying 3: The Native Simplicial Chart

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 21, 2026*

## Abstract

**Situation.** Information geometry is usually introduced as an analyst's project: probability distributions live on a manifold with a normalization constraint, the natural metric (Fisher–Rao) is positive-definite but awkward to differentiate against, and the standard move — eliminating one coordinate to remove the constraint — silently breaks the permutation symmetry that the simplex obviously has. Most of the technical effort in introductory expositions is bookkeeping to repair what the elimination broke.

**Task.** Find a coordinate system in which the simplex's intrinsic structure is exposed rather than concealed.

**Action.** Refuse the elimination. Keep the redundant $N$-th coordinate, treat the constraint $\sum p_i = 1$ as a gauge fixing, and work on the overcomplete frame $\mathbb{R}^N$. Read probabilities as squared amplitudes: $p_i = a_i^2$ with $\sum a_i^2 = 1$. The amplitude vector $a$ is a point on the positive orthant of the unit sphere; the probability simplex is its squared shadow.

**Result.** Fisher–Rao is the pullback of the round sphere metric through the square-root map — sphere geometry in probability coordinates. The tangent space at any interior point of the simplex is the zero-sum hyperplane $H_0$, a genuine Euclidean vector space. The Fisher–Rao isometry group at the uniform distribution is $\mathrm{SO}(H_0)$. The chart carries an intrinsic vector algebra — inner product, cross product, Rodrigues rotation — that reproduces ordinary three-dimensional Euclidean vector algebra exactly in the tetrahedral case $N = 4$. This paper presents the chart and walks it through worked examples for $N = 2, 3, 4$.

This is \heb{ל}1 of the trilogy *Identifying 3*. \heb{ל}2 develops the cumulant tower of the categorical log-partition on this chart; \heb{ל}3 reads the chart through Pontryagin character orthogonality. \heb{ל}1 supplies the toolkit they share.

**Keywords:** information geometry, statistical manifold, probability simplex, categorical distributions, Fisher–Rao metric, square-root coordinates, amplitude sphere, zero-sum hyperplane, Bhattacharyya coefficient.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
Probability distributions over \(N\) outcomes live on a simplex --- a triangle for \(N=3\), a tetrahedron for \(N=4\) --- that sits awkwardly inside \(N\)-dimensional coordinates because the probabilities must sum to one. Take the square root of each probability and the awkwardness goes away: the simplex becomes the positive octant of a sphere, and the Fisher--Rao metric reduces to ordinary sphere geometry. No coordinate elimination, no Lagrange multipliers, full permutation symmetry preserved by construction. For four outcomes, the tangent space is three-dimensional and the chart's intrinsic algebra is literally ordinary 3D vector calculus --- inner product, cross product, rotation --- usable as-is.
\end{mdframed}

---

## Notation

| Symbol | Meaning |
|---|---|
| $N$ | Number of categorical outcomes; integer $\geq 2$. |
| $\Delta^{N-1}$ | Probability simplex in $\mathbb{R}^N$ (§1). |
| $H_0$ | Zero-sum hyperplane $\{x \in \mathbb{R}^N : \sum_i x_i = 0\}$ — the natural tangent space (§2). |
| $S^{N-1}_+$ | Positive orthant of the unit sphere (§3). |
| $u$ | Uniform distribution $u = \tfrac{1}{N}(1, \dots, 1)$, the centroid of $\Delta^{N-1}$. |
| $\psi,\ \varphi$ | Square-root and squaring maps; mutual inverses between $\Delta^{N-1}$ and $S^{N-1}_+$ (§3). |
| $g_{FR},\ g_S$ | Fisher–Rao metric on $\Delta^{N-1}$; round metric on $S^{N-1}_+$ (§4). |
| $\langle \cdot, \cdot \rangle$ | Ambient Euclidean inner product on $\mathbb{R}^N$. |
| $\nu$ | (for $N=4$ only) Unit normal to $H_0$ in $\mathbb{R}^4$: $\nu = \tfrac{1}{2}(1,1,1,1)$ (§6). |
| $\varepsilon_{ijk\ell}$ | Levi-Civita symbol on $\mathbb{R}^4$; $\varepsilon_{1234} = +1$ (§6). |

---

## 1. The probability simplex and its gauge redundancy

A discrete probability distribution over $N$ outcomes is a vector

$$p = (p_1, p_2, \dots, p_N) \in \mathbb{R}^N$$

with $p_i \geq 0$ and $\sum_{i=1}^N p_i = 1$. The set of such vectors is the **probability simplex**

$$\Delta^{N-1} = \{ p \in \mathbb{R}^N : p_i \geq 0,\ \textstyle\sum_i p_i = 1 \},$$

an $(N-1)$-dimensional convex polytope with $N$ vertices at the standard basis vectors $e_1, \dots, e_N$ (the deterministic distributions).

The dimensional mismatch is the first thing to notice: the simplex is $(N-1)$-dimensional but its natural description uses $N$ coordinates. One coordinate is redundant — fixed by the others through $p_N = 1 - p_1 - \cdots - p_{N-1}$.

The standard move is to **eliminate** the redundant coordinate. Work in $(p_1, \dots, p_{N-1})$, treat $p_N$ as derived. This gives an unconstrained chart on the interior of the simplex, at the cost of singling out the $N$-th outcome. The simplex's natural permutation symmetry is broken; every subsequent operation either carries the symmetry around manually or repairs it after the fact.

We will refuse the elimination.

## 2. The zero-sum hyperplane

Define

$$H_0 = \{ x \in \mathbb{R}^N : \textstyle\sum_i x_i = 0 \}.$$

This is the **zero-sum hyperplane**: a vector subspace of $\mathbb{R}^N$ of dimension $N-1$.

Two facts make $H_0$ the natural object.

**Tangent space.** Every tangent vector to $\Delta^{N-1}$ at any interior point lies in $H_0$. If $p(t)$ is a smooth curve in $\Delta^{N-1}$, differentiating $\sum_i p_i(t) = 1$ gives $\sum_i \dot{p}_i = 0$.

**Differences of distributions.** If $p, q \in \Delta^{N-1}$ then $p - q \in H_0$. Score functions, parameter perturbations, gradients of functions on the simplex — all live in $H_0$.

$H_0$ is therefore the natural arena for linear algebra on the simplex. It is a genuine Euclidean vector space, closed under addition, scaling, inner product, and rotation. No Lagrange multipliers; no constraint surface; no special handling of boundary versus interior.

The **uniform distribution**

$$u = \tfrac{1}{N}(1, 1, \dots, 1)$$

is the centroid of $\Delta^{N-1}$ and the unique simplex point fixed by all coordinate permutations. The displacement map

$$\Delta^{N-1} \longrightarrow H_0, \qquad p \longmapsto p - u$$

is the **centered simplicial chart**. It is overcomplete (still $N$ coordinates), but the coordinates satisfy a single linear relation and the chart preserves the full permutation symmetry by construction.

## 3. The square-root map and the amplitude sphere

Define the **square-root map**

$$\psi : \Delta^{N-1} \longrightarrow S^{N-1}_+, \qquad \psi(p) = (\sqrt{p_1}, \sqrt{p_2}, \dots, \sqrt{p_N})$$

where

$$S^{N-1}_+ = \{ a \in \mathbb{R}^N : a_i \geq 0,\ \textstyle\sum_i a_i^2 = 1 \}$$

is the **positive orthant of the unit sphere** in $\mathbb{R}^N$. The components $a_i = \sqrt{p_i}$ are called **amplitudes**.

The inverse is coordinate-wise squaring:

$$\varphi : S^{N-1}_+ \longrightarrow \Delta^{N-1}, \qquad \varphi(a) = (a_1^2, a_2^2, \dots, a_N^2).$$

Constraints transfer cleanly: $a_i \geq 0$ since $p_i \geq 0$; and $\sum a_i^2 = \sum p_i = 1$.

**Why this is more than renaming.** The simplex normalization $\sum p_i = 1$ is *linear* in $p$ — it cuts out an affine hyperplane. The sphere normalization $\sum a_i^2 = 1$ is *quadratic* in $a$ — it cuts out a sphere. Affine hyperplanes carry no rotational symmetry beyond what the ambient space gives them. Spheres are homogeneous under their full rotation group $\mathrm{SO}(N)$. Trading a linear constraint for a quadratic one is trading flat geometry for curved — and curved is what statistics wants, because probability distributions are not equidistant in any meaningful sense of distinguishability.

**Boundary caveat.** $\psi$ is continuous on all of $\Delta^{N-1}$ but smooth only on the open interior, where every $p_i > 0$. At boundary points (some $p_i = 0$) the derivative $\partial \psi_i / \partial p_i = 1/(2\sqrt{p_i})$ diverges, and the simplex itself acquires corner structure where the tangent space is not $H_0$. All subsequent statements in this paper are made on the open interior, where the chart is smooth.

## 4. Fisher–Rao as the round metric, pulled back

The unit sphere carries the **round metric** — the restriction of the ambient Euclidean inner product:

$$g_S = \sum_{i=1}^N (da_i)^2\bigg|_{S^{N-1}}.$$

Pull this back through $\psi$. With $a_i = \sqrt{p_i}$:

$$da_i = \frac{dp_i}{2\sqrt{p_i}}, \qquad (da_i)^2 = \frac{(dp_i)^2}{4 p_i}.$$

Summing:

$$\psi^* g_S = \sum_i (da_i)^2 = \frac{1}{4} \sum_i \frac{(dp_i)^2}{p_i} = \frac{1}{4}\, g_{FR}(p),$$

where

$$g_{FR}(p) = \sum_i \frac{(dp_i)^2}{p_i}$$

is the **Fisher–Rao metric** [Fisher, 1925; Rao, 1945] on the simplex — the standard convention used throughout this paper. The metric is unique up to scale under invariance by sufficient statistics [Chentsov, 1982]; see [Amari & Nagaoka, 2000] for the canonical modern exposition. Some authors absorb the factor $1/4$ into $g_{FR}$ to make $\psi^* g_S = g_{FR}$ exactly; we keep it explicit because it simplifies the bookkeeping in §5.

Three immediate consequences:

**Distances are arc lengths.** The Fisher–Rao distance between $p, q \in \Delta^{N-1}$ is

$$d_{FR}(p, q) = 2 \arccos\!\left( \sum_i \sqrt{p_i\, q_i} \right) = 2\, \angle\bigl(\psi(p), \psi(q)\bigr),$$

twice the angle between the amplitude vectors on the sphere.

**The Bhattacharyya coefficient is the amplitude inner product.** The quantity $BC(p, q) = \sum_i \sqrt{p_i q_i}$ from classical statistics [Bhattacharyya, 1943] is exactly $\langle \psi(p), \psi(q) \rangle$, the Euclidean inner product in $\mathbb{R}^N$.

**Geodesics are great circles, pulled back.** The Fisher–Rao geodesic from $p$ to $q$ is the $\varphi$-image of the great-circle arc from $\psi(p)$ to $\psi(q)$ on the sphere.

## 5. The tangent space at the uniform

The uniform distribution has amplitude vector

$$\psi(u) = \tfrac{1}{\sqrt{N}}(1, 1, \dots, 1).$$

The tangent space to $S^{N-1}$ at $\psi(u)$ consists of vectors in $\mathbb{R}^N$ orthogonal to $\psi(u)$ — that is, vectors with $\sum_i v_i = 0$. So

$$T_{\psi(u)} S^{N-1} = H_0,$$

and via $\psi^{-1}_*$, the Fisher–Rao tangent space at $u$ is also $H_0$. This matches the **centered chart of §2** directly: linearizing the affine constraint $\sum p_i = 1$ at $u$ gives the linear constraint $\sum x_i = 0$, which is the defining equation of $H_0$. The two charts of §§2–3 therefore converge at the uniform, both identifying $T_u \Delta^{N-1}$ with $H_0$ as a vector space — differing only by the scalar Jacobian $\psi_*\big|_u = (\sqrt{N}/2)\cdot \mathrm{id}_{H_0}$ obtained from differentiating $\psi$ at $u$.

Evaluating $g_{FR}$ at $u$:

$$g_{FR}(v, w)\big|_u = \sum_i \frac{v_i\, w_i}{u_i} = N \sum_i v_i w_i = N \langle v, w \rangle_{\mathbb{R}^N}, \qquad v, w \in H_0.$$

Fisher–Rao at the uniform is therefore $N$ times the ambient Euclidean inner product, restricted to $H_0$. (Equivalently, by §4, $\psi^* g_S\big|_u = (N/4)\langle \cdot, \cdot \rangle$ — the factor of $1/4$ from §4 and the factor of $N$ from evaluating $1/u_i$ multiply to give $N/4$.)

**Tangent (isotropy) isometry group at the uniform.** Rotations of $S^{N-1}$ that fix $\psi(u)$ form the subgroup

$$\mathrm{Stab}(\psi(u)) = \mathrm{SO}(H_0) \cong \mathrm{SO}(N-1)$$

acting linearly on the tangent space. *Proof of the linear-isometry claim.* The round metric $g_S$ is $O(N)$-invariant; in particular, the stabilizer of any point $a \in S^{N-1}$ acts on $T_a S^{N-1}$ by linear isometries of $g_S$. Since $\psi^* g_S = g_{FR}/4$ (§4), the same linear maps preserve the bilinear form $g_{FR}|_u$ on $T_u \Delta^{N-1} = H_0$. Therefore $\mathrm{SO}(H_0)$ is the **full linear (isotropy) isometry group of the Fisher–Rao tangent inner product at the uniform** — the group of linear self-maps of $H_0$ preserving $g_{FR}|_u$, equivalently the isotropy representation on $T_{\psi(u)} S^{N-1}$. The discrete subgroup generated by coordinate permutations is the symmetric group $S_N$, acting on $H_0$ as the standard $(N-1)$-dimensional irreducible representation.

*Scope of the claim.* This is the **tangent/isotropy** statement — symmetries of the bilinear form on $T_u \Delta^{N-1}$. The **global** isometry group of $(\Delta^{N-1}, g_{FR})$ as a Riemannian manifold is strictly smaller: a generic element of $\mathrm{SO}(H_0)$ does not lift through $\psi$ to a sphere rotation preserving the positive orthant $S^{N-1}_+$, so it does not extend to a global Fisher–Rao isometry of the simplex. The automatic global symmetry is only the relabeling action of $S_N$. Throughout this paper and the trilogy, "the isometry group at $u$" — and the corresponding $\mathrm{SO}(H_0)$ label — refers to the linear isometry group of $g_{FR}|_u$ on the tangent space, unless stated otherwise.

This is the key fact the chart was built to expose:

> **The linear isometry group of the Fisher–Rao tangent inner product at the uniform is $\mathrm{SO}(H_0)$ — the full rotation group of the zero-sum hyperplane.**

The simplicial rotation operator and the Fisher–Rao tangent isometry at $u$ are not analogues; they are the same Lie group acting on the same tangent space.

## 6. Intrinsic vector algebra on $H_0$

Because $H_0$ is a Euclidean vector space, ordinary finite-dimensional linear algebra applies on it without modification. Three operations are worth naming.

**Inner product.** For $v, w \in H_0$,

$$\langle v, w \rangle = \sum_{i=1}^N v_i w_i.$$

Restricted to $H_0$ this is positive-definite. It is $1/N$ of the Fisher–Rao inner product at the uniform (by §5).

**Cross product (the tetrahedral case $N = 4$).** When $N = 4$, $H_0$ is three-dimensional. Fix the unit normal to $H_0$ in $\mathbb{R}^4$:

$$\nu = \tfrac{1}{2}(1, 1, 1, 1) \in \mathbb{R}^4, \qquad |\nu| = 1, \qquad \nu \perp H_0.$$

Define the **simplicial cross product** $\times_S : H_0 \times H_0 \to H_0$ by

$$(v \times_S w)_i = \sum_{j,k,\ell = 1}^{4} \varepsilon_{ijk\ell}\, v_j\, w_k\, \nu_\ell, \qquad \varepsilon_{1234} = +1,$$

where $\varepsilon$ is the standard Levi-Civita symbol on $\mathbb{R}^4$. Equivalently, $v \times_S w$ is the Hodge dual of $v \wedge w \wedge \nu$ in $\mathbb{R}^4$.

The product is bilinear and antisymmetric in $(v, w)$ from the antisymmetry of $\varepsilon$ in $(j, k)$. It lands in $H_0$: the inner product

$$\langle v \times_S w, \nu \rangle = \sum_{i,j,k,\ell} \varepsilon_{ijk\ell}\, \nu_i\, v_j\, w_k\, \nu_\ell$$

vanishes because $\varepsilon$ is antisymmetric in $(i, \ell)$ while $\nu_i \nu_\ell$ is symmetric. In any orthonormal frame on $H_0$ (such as the Helmert frame of §7.3, verified there by direct computation), $\times_S$ agrees with the ordinary three-dimensional Euclidean cross product. The tetrahedral case is not an analogy to 3D vector algebra; the two algebras are isomorphic.

**Rodrigues rotation.** For a unit vector $n \in H_0$ and angle $\theta$, the operator

$$R_{n, \theta}(v) = (\cos\theta)\, v + (\sin\theta)\, n \times_S v + (1 - \cos\theta)\, \langle n, v \rangle\, n$$

is a rotation of $H_0$ by angle $\theta$ about the axis $n$. For $N = 4$ this is the Fisher–Rao isometry of $\Delta^3$ at the uniform, rotating tangent directions by $\theta$.

Higher $N$ does not admit a binary cross product (Hodge duality on $H_0$ no longer lands in $H_0$), but the generators of $\mathrm{SO}(H_0)$ are still the elements of $\Lambda^2 H_0$ and Rodrigues generalizes via the matrix exponential. The case $N = 4$ is special only because $\dim H_0 = 3$.

## 7. Worked examples

### 7.1. $N = 2$: Bernoulli (the 1-simplex)

$\Delta^1$ is the segment from $e_1 = (1, 0)$ to $e_2 = (0, 1)$, with $H_0$ the line spanned by $(1, -1)/\sqrt{2}$.

The square-root map sends $\Delta^1$ to the quarter-circle $S^1_+$. Parameterize by angle $\theta \in [0, \pi/2]$:

$$\psi(p) = (\cos\theta, \sin\theta), \qquad p = (\cos^2\theta, \sin^2\theta).$$

| $\theta$ | $p_1$ | $p_2$ | $a_1$ | $a_2$ |
|---|---|---|---|---|
| $0$ | $1$ | $0$ | $1$ | $0$ |
| $\pi/6$ | $3/4$ | $1/4$ | $\sqrt{3}/2$ | $1/2$ |
| $\pi/4$ | $1/2$ | $1/2$ | $1/\sqrt{2}$ | $1/\sqrt{2}$ |
| $\pi/3$ | $1/4$ | $3/4$ | $1/2$ | $\sqrt{3}/2$ |
| $\pi/2$ | $0$ | $1$ | $0$ | $1$ |

The Fisher–Rao distance between $\theta_1$ and $\theta_2$ is $2|\theta_1 - \theta_2|$. The total Fisher–Rao length of $\Delta^1$ is $\pi$. Notice that the gap in $p_1$ between $\theta = \pi/4$ and $\theta = \pi/3$ (fair to mildly biased) is $0.25$ — the same as the gap between $\theta = \pi/3$ and $\theta = \pi/2$ (mildly biased to deterministic). But the Fisher–Rao distance is $\pi/6$ for the first pair and $\pi/3$ for the second: the second is twice as far. The angular coordinate tracks **statistical distinguishability**; the probability coordinate does not.

### 7.2. $N = 3$: categorical over three outcomes (the 2-simplex)

$\Delta^2$ is an equilateral triangle in $\mathbb{R}^3$ with vertices $e_1, e_2, e_3$ and centroid $u = (1/3, 1/3, 1/3)$. $H_0$ is the plane orthogonal to $(1, 1, 1)$.

$\psi$ sends $\Delta^2$ to the positive octant of $S^2$ — a curved spherical triangle. The vertices coincide (they were already unit vectors). The centroid lifts:

$$u = (1/3, 1/3, 1/3), \ |u| = 1/\sqrt{3}; \qquad \psi(u) = (1/\sqrt{3}, 1/\sqrt{3}, 1/\sqrt{3}), \ |\psi(u)| = 1.$$

$\psi$ "inflates" the flat triangle's interior radially onto the spherical surface. Edges (where some $p_i = 0$) map to great-circle arcs (where the same $a_i = 0$).

\begin{figure}[H]
\centering
\begin{tikzpicture}[scale=1.2]
  % --- LEFT PANEL: flat probability simplex Delta^2 ---
  \begin{scope}[xshift=0cm]
    \coordinate (e1) at (0, 0);
    \coordinate (e2) at (2.4, 0);
    \coordinate (e3) at (1.2, 2.078);
    \coordinate (u)  at (1.2, 0.693);

    \fill[gray!10] (e1) -- (e2) -- (e3) -- cycle;
    \draw[thick]   (e1) -- (e2) -- (e3) -- cycle;

    \filldraw (e1) circle (0.05);
    \filldraw (e2) circle (0.05);
    \filldraw (e3) circle (0.05);
    \filldraw (u)  circle (0.06);

    \node[below left]  at (e1) {$e_1$};
    \node[below right] at (e2) {$e_2$};
    \node[above]       at (e3) {$e_3$};
    \node[right]       at (u)  {$u$};

    \node[below] at (1.2, -0.5) {(a) $\Delta^2 \subset \mathbb{R}^3$};
  \end{scope}

  % --- Arrow: psi ---
  \draw[->, thick] (3.3, 1.04) -- (4.5, 1.04) node[midway, above] {$\psi$};

  % --- RIGHT PANEL: spherical octant psi(Delta^2) = S^2_+ ---
  \begin{scope}[xshift=5.4cm]
    \coordinate (e1)   at (0, 0);
    \coordinate (e2)   at (2.4, 0);
    \coordinate (e3)   at (1.2, 2.078);
    \coordinate (psiu) at (1.2, 0.85);

    \fill[gray!10] (e1) to[bend right=28] (e2)
                          to[bend right=28] (e3)
                          to[bend right=28] (e1);
    \draw[thick]   (e1) to[bend right=28] (e2)
                          to[bend right=28] (e3)
                          to[bend right=28] (e1);

    \filldraw (e1)   circle (0.05);
    \filldraw (e2)   circle (0.05);
    \filldraw (e3)   circle (0.05);
    \filldraw (psiu) circle (0.06);

    \node[below left]  at (e1)   {$e_1$};
    \node[below right] at (e2)   {$e_2$};
    \node[above]       at (e3)   {$e_3$};
    \node[right]       at (psiu) {$\psi(u)$};

    \node[below] at (1.2, -0.5) {(b) $\psi(\Delta^2) = S^2_+$};
  \end{scope}
\end{tikzpicture}
\caption{The square-root map $\psi : \Delta^2 \to S^2_+$ for $N = 3$.
(a)~The probability simplex $\Delta^2$, an equilateral triangle in $\mathbb{R}^3$ with vertices at the standard basis vectors $e_1, e_2, e_3$ and centroid $u = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})$ at radial distance $1/\sqrt{3}$ from the origin.
(b)~The spherical triangle $\psi(\Delta^2) = S^2_+$, the positive octant of the unit sphere, sharing the same vertices (already unit vectors) but with the centroid lifted radially to $\psi(u) = (1/\sqrt{3}, 1/\sqrt{3}, 1/\sqrt{3})$ on the sphere.
The flat edges (where some $p_i = 0$) become the spherical triangle's great-circle arcs (where the corresponding amplitude $a_i = 0$).}
\label{fig:psi-N3}
\end{figure}

| $(p_1, p_2, p_3)$ | $(a_1, a_2, a_3)$ |
|---|---|
| $(1, 0, 0)$ | $(1, 0, 0)$ |
| $(1/2, 1/2, 0)$ | $(1/\sqrt{2}, 1/\sqrt{2}, 0)$ |
| $(1/2, 1/4, 1/4)$ | $(1/\sqrt{2}, 1/2, 1/2)$ |
| $(1/3, 1/3, 1/3)$ | $(1/\sqrt{3}, 1/\sqrt{3}, 1/\sqrt{3})$ |
| $(0.8, 0.1, 0.1)$ | $(0.894, 0.316, 0.316)$ |

Fisher–Rao distances are arc lengths between amplitude images. For instance,

$$d_{FR}(u, e_1) = 2 \arccos\!\bigl( \langle \psi(u), e_1 \rangle \bigr) = 2 \arccos(1/\sqrt{3}) \approx 1.911.$$

The cyclic group $\mathbb{Z}/3 \subset S_3$ acts on $H_0$ as rotation by $2\pi/3$ about the axis through $\psi(u)$.

### 7.3. $N = 4$: tetrahedral (the 3-simplex)

$\Delta^3$ has four vertices and centroid $u = (1/4, 1/4, 1/4, 1/4)$. $H_0$ is three-dimensional. $\psi(\Delta^3)$ is a curved spherical tetrahedron — the positive orthant of $S^3$.

This is the case in which "the simplicial frame is just Euclidean 3-space" is literally true. Choose the **Helmert frame** [Helmert, 1876] on $H_0$:

$$e_1' = \tfrac{1}{\sqrt{2}}(1, -1, 0, 0), \quad e_2' = \tfrac{1}{\sqrt{6}}(1, 1, -2, 0), \quad e_3' = \tfrac{1}{\sqrt{12}}(1, 1, 1, -3).$$

These vectors are mutually orthogonal, of unit length, all in $H_0$. The map

$$H_0 \xrightarrow{\ \sim\ } \mathbb{R}^3, \qquad v_1' e_1' + v_2' e_2' + v_3' e_3' \longmapsto (v_1', v_2', v_3')$$

is an isometric isomorphism. Under it the simplicial cross product $\times_S$ on $H_0$ becomes the ordinary $\mathbb{R}^3$ cross product, and the simplicial Rodrigues operator becomes the ordinary 3D Rodrigues formula.

**Verification.** Compute $e_1' \times_S e_2'$ from the formula of §6 with $\nu = (1,1,1,1)/2$ and $\varepsilon_{1234} = +1$. Expanding the sum over $\{j, k, \ell\} = \{2, 3, 4\}$ as a cofactor identity:

$$(e_1' \times_S e_2')_1 = (e_1')_2 \bigl[(e_2')_3\, \nu_4 - (e_2')_4\, \nu_3\bigr] - (e_1')_3 [\cdots] + (e_1')_4 [\cdots].$$

Since $(e_1')_3 = (e_1')_4 = 0$, only the first bracket contributes:

$$(e_1' \times_S e_2')_1 = \bigl(-\tfrac{1}{\sqrt{2}}\bigr)\bigl[\bigl(-\tfrac{2}{\sqrt{6}}\bigr)\bigl(\tfrac{1}{2}\bigr) - 0\bigr] = \bigl(-\tfrac{1}{\sqrt{2}}\bigr)\bigl(-\tfrac{1}{\sqrt{6}}\bigr) = \tfrac{1}{\sqrt{12}} = (e_3')_1.$$

The remaining three components, computed analogously, also match $e_3'$ — so $e_1' \times_S e_2' = e_3'$. Antisymmetry and analogous computations on the other two pairs give the full cyclic identities

$$e_1' \times_S e_2' = e_3', \qquad e_2' \times_S e_3' = e_1', \qquad e_3' \times_S e_1' = e_2'.$$

This is the standard right-hand rule of 3D Euclidean cross product, holding verbatim in the Helmert frame on $H_0 \subset \mathbb{R}^4$.

The orientation-preserving tetrahedral group $A_4$ acts on $H_0$ as a discrete subgroup of $\mathrm{SO}(3)$ of order $12$ (rotational symmetries of the regular tetrahedron). Including reflections gives $S_4 \cong T_d$ of order $24$. The cyclic subgroup $\mathbb{Z}/3 \subset A_4$ generated by rotation about a vertex-centroid axis is the rotational symmetry visible in §7.2's three-outcome case, lifted to the full tetrahedral frame.

This is the case used in the Quadray / synergetics tradition [Fuller, 1975], and it is the case in which all of \heb{ל}1's claims can be checked by hand against ordinary 3D vector calculus.

## 8. The chart, as a working toolkit

\heb{ל}1's toolkit, compressed:

| Object | Standard chart | Native simplicial chart |
|---|---|---|
| Probability vector | $(p_1, \dots, p_{N-1})$; $p_N$ derived | $(p_1, \dots, p_N)$ with $\textstyle\sum p_i = 1$ as gauge |
| Tangent space | Constraint-aware, varies with chart | $H_0$ (fixed Euclidean $(N-1)$-space) |
| Metric | $g_{FR}$ on a constrained manifold | $4 \cdot (\text{round sphere metric})$, pulled back via $\psi$ |
| Tangent isometry group at $u$ | Computed via Chentsov uniqueness | $\mathrm{SO}(H_0)$, by direct identification (linear isometries of $g_{FR}|_u$ on $H_0$; the global isometry group of $(\Delta^{N-1}, g_{FR})$ is strictly smaller) |
| Tangent inner product at $u$ | $\sum (v_i w_i / p_i)$ at $p$ | $N \langle v, w \rangle_{\mathbb{R}^N}$ on $H_0$ (ambient Euclidean, scaled by $N$) |
| Bhattacharyya coefficient | Defined separately | $\langle \psi(p), \psi(q) \rangle$ |
| Geodesics | Solved via Fisher–Rao ODE | $\varphi$-image of great circles |

The native chart removes machinery rather than adding it. Two maps — the centering $p \mapsto p - u$ and the square root $\psi$ — expose the simplex's Euclidean tangent space, sphere metric, and rotation group simultaneously. The chart, the map $\psi$, the zero-sum hyperplane $H_0$, the identification of Fisher–Rao with the pulled-back round metric, and the intrinsic vector algebra on $H_0$ are complete in themselves as a coordinatization of the categorical probability simplex.

\heb{ל}2 develops the cumulant tower of the categorical log-partition on this chart; \heb{ל}3 reads the chart through Pontryagin character orthogonality. Neither modifies \heb{ל}1's toolkit; both inherit it.

## 9. References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Lecture Notes in Statistics 28. Springer.

Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs 191. American Mathematical Society.

Bhattacharyya, A. (1943). On a measure of divergence between two statistical populations defined by their probability distributions. *Bulletin of the Calcutta Mathematical Society* 35, 99–109.

Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs 53. American Mathematical Society. (Russian original 1972.)

Fisher, R. A. (1925). Theory of statistical estimation. *Proceedings of the Cambridge Philosophical Society* 22, 700–725.

Fuller, R. B. (1975). *Synergetics: Explorations in the Geometry of Thinking.* Macmillan.

Helmert, F. R. (1876). Die Genauigkeit der Formel von Peters zur Berechnung des wahrscheinlichen Beobachtungsfehlers direkter Beobachtungen gleicher Genauigkeit. *Astronomische Nachrichten* 88, 113–132.

Rao, C. R. (1945). Information and the accuracy attainable in the estimation of statistical parameters. *Bulletin of the Calcutta Mathematical Society* 37, 81–91.
