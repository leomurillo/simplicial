# Simplicial Coordinates as the Native Language of Information Geometry

**Leonardo Murillo Montero**

*[date]*

---

## Abstract

The probability simplex is the affine translate of the zero-sum hyperplane of the $N$-vector simplicial frame, with the normalization constraint $\sum p_i = 1$ acting as gauge fixing along the diagonal direction $\mathbf{1} = (1,\ldots,1)$. Under this identification, Amari's dually flat structure on the categorical exponential family becomes structurally transparent: the natural parameters $\theta$ and the moment parameters $\eta$ are both $N$-tuples in $\mathbb{R}^N / \langle \mathbf{1}\rangle$, and the Legendre transform that exchanges them is intrinsic to the simplicial Gram data — no reference outcome is singled out. At the uniform distribution, the Fisher information metric is a positive scalar multiple of the simplicial inner product of [Paper 1 §2.4]; the Fisher–Rao geodesics emanating from the uniform are, under the square-root map $x_i = \sqrt{p_i}$, the great circles on the unit sphere in $\mathbb{R}^N$, and the simplicial rotation operator $R(u,\theta)$ of [Paper 1 §5] acts as the Fisher–Rao isometry group on the tangent space at the uniform. The classical picture — obtained by choosing a reference distribution and parameterizing the simplex by $(N-1)$-dimensional affine charts — is a gauge-fixed shadow of this intrinsic structure. We make the identifications precise, restate Chentsov's uniqueness theorem in simplicial language, and exhibit the natural gradient step for softmax-parameterized categoricals at initialization as a closed-form simplicial operation. The framework gives a coordinate-free description of the categorical statistical manifold; it does not claim novelty in Amari's theorems, only in the coordinate system in which those theorems are expressed.

**Keywords:** information geometry, Fisher–Rao metric, simplicial coordinates, Quadray coordinates, zero-sum hyperplane, gauge redundancy, dually flat structure, exponential family, Chentsov's theorem, categorical distribution, natural gradient, softmax, Aitchison geometry.

**MSC 2020:** 53B12 (statistical manifolds), 62B10 (statistical aspects of information theory), 94A17 (measures of information, entropy).

---

## 1. Introduction

### 1.1 Context

In [Paper 1] an intrinsic algebraic vector calculus was developed on the zero-sum hyperplane $H$ of the $N$-vector simplicial frame: an inner product induced by the simplicial Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$, a skew-symmetric bilinear cross-product operator $K(u)$ for $N = 4$, and a closed-form Rodrigues rotation $R(u,\theta) = I + \sin\theta\,K(u) + (1-\cos\theta)\,K(u)^2$. The three operators are jointly compatible with the gauge action $c \mapsto c + k\mathbf{1}$: the inner product is gauge-invariant as a scalar, while $K(u)$ and $R(u,\theta)$ preserve $H$ and respectively annihilate and fix the gauge direction $\mathbf{1}$.

Section 8.1 of that paper observed, as a structural parallel, that the probability simplex $\{p : p_i \geq 0,\ \sum p_i = 1\}$ is the affine translate of $H$ by $\tfrac{1}{N}\mathbf{1}$, and that under the square-root map $x_i = \sqrt{p_i}$ the simplicial inner product agrees with the Fisher information metric up to a positive scalar at the uniform distribution. That observation was presented as interpretive motivation, not as a formal result, and the relationship between $R(u,\theta)$ and Fisher–Rao geodesic flow was explicitly left open.

The present paper takes up this program. We argue that simplicial coordinates are not merely a convenient chart for the probability simplex but the *native coordinate system* for Amari's dually flat structure [Amari] on the categorical exponential family. The conventional expositions of information geometry on the categorical — which parameterize by the first $N-1$ probabilities and treat $p_N = 1 - \sum_{i < N} p_i$ implicitly, or by natural parameters $\theta_i = \log(p_i/p_N)$ with $p_N$ as reference — systematically break the symmetric group $S_N$ symmetry that Chentsov's theorem tells us is structural. The simplicial frame restores this symmetry at the cost of one explicit coordinate redundancy, making explicit a gauge structure that the usual reference-fixed presentation tends to hide.

Recent empirical work on neural representation geometry gives an external anchor for this coordinate claim. Wurgaft et al. [Wurgaft et al. 2026] fit paired manifolds in activation space and output-probability space for cyclic and sequential concept tasks, and find that geodesic distances on the activation manifold are nearly isometric to geodesic distances on the behavior manifold; for weekdays, the reported manifold correlation is \(r\approx0.99\), while linear activation distances correlate more weakly with behavior-manifold distance. Their behavior manifold is built by aggregating probability mass over concept tokens and embedding the resulting categorical distributions by the Hellinger map \(p\mapsto\sqrt p\). Since this square-root map is the sphere-pullback presentation of the Fisher-Rao metric, their result is a measured instance of the present paper's native-coordinate thesis: the relevant behavioral object is not an arbitrary Euclidean cloud, but the categorical simplex in its Fisher/Hellinger geometry, with the cyclic concept structure living in the zero-sum quotient \(H=\mathbb R^N/\langle\mathbf1\rangle\). The point is not that their paper proves the simplicial-coordinate thesis; rather, it supplies a clean neural-network phenomenology in which the thesis is the natural structural explanation.

### 1.2 What this paper does (and does not) claim

**Does not claim.** We prove no new theorem in information geometry. Fisher–Rao uniqueness, the dually flat structure on exponential families, Chentsov's theorem, and the sphere-pullback characterization of Fisher–Rao are all classical. No foundational claim about the interpretation of probability, no bound on any estimator, no new convergence rate for an ML algorithm.

**Does claim.** The structural objects of Amari's dually flat geometry on the categorical manifold — the Fisher metric, the $e$- and $m$-connections, the Legendre duality between $\theta$ and $\eta$ coordinates, the canonical KL divergence, the tangent space at the uniform distribution — admit an $S_N$-equivariant, coordinate-free presentation in the simplicial frame. The single structural fact that organizes the presentation is that the probability simplex is a gauge slice of the simplicial frame's coordinate space, and that every classical object of information geometry either descends to or is gauge-fixed on this slice. The classical $(N-1)$-dimensional charts are gauge sections.

The companion cyclotomic notes use the same zero-sum hyperplane to study discrete spectral reflections, Galois normalizers, and cyclotomic units.  Those notes contain the discrete-geometric and arithmetic research questions.  The present paper uses them only as context for the Aitchison-versus-Fisher symmetry split: spectral reflections are natural flat/Aitchison isometries, while Chentsov/Fisher geometry retains only the permutation symmetries of the categorical outcomes.

### 1.3 Contributions

1. **The simplex as a gauge slice (§2).** The probability simplex is $\{p \in \mathbb{R}^N : p_i \geq 0,\ \sum p_i = 1\}$, an affine gauge slice of the simplicial coordinate space transverse to $\mathbf{1}$. Its interior is diffeomorphic to $H$ via the zero-sum shift $\eta_i := p_i - \tfrac{1}{N}$.

2. **Fisher–Rao via the sphere pullback (§3).** We make the §8.1 observation of [Paper 1] precise: the Fisher–Rao metric on the simplex interior is the pullback along $x_i = \sqrt{p_i}$ of a quarter of the round metric on $S^{N-1} \subset \mathbb{R}^N$. At the uniform distribution, this pulls back to exactly $(N-1)$ times the simplicial inner product on $H$, and the simplicial rotation $R(u,\theta)$ acts as the Fisher–Rao isometry group on the tangent space at the uniform.

3. **Dually flat structure in simplicial coordinates (§4).** The natural parameters $\theta \in \mathbb{R}^N / \langle \mathbf{1}\rangle$ and moment parameters $\eta \in H$ of the categorical exponential family are both simplicial quantities carrying the same gauge. Legendre duality between them — expressed classically in terms of a reference-fixed $(N-1)$-dimensional chart — is a gauge-equivariant operation on the full $N$-dimensional simplicial frame. The canonical divergence (KL) has an explicit simplicial expression.

4. **Chentsov's uniqueness, simplicially (§5).** The Fisher–Rao metric is characterized by Chentsov's theorem as the unique (up to scaling) Markov-invariant Riemannian metric on statistical manifolds. For the categorical, this uniqueness descends to: the simplicial Gram matrix $G$ is the unique (up to scaling) $S_N$-invariant positive semidefinite bilinear form on $\mathbb{R}^N$ with $\mathbf{1}$ in its kernel. We record this as a linear-algebraic shadow of Chentsov, not as an independent theorem.

5. **Natural gradient at the uniform (§6).** For softmax-parameterized categoricals, the Fisher information matrix at logits $\theta = 0$ (equivalently: uniform output) is proportional to the simplicial Gram matrix restricted to $H$. Its pseudoinverse has the closed form $F^+ = N \cdot \Pi_H$ where $\Pi_H$ is the zero-sum projector. The natural gradient step at initialization therefore reduces to "subtract the mean of the gradient, scale by $N$" — a simplicial operation requiring no matrix inversion.

6. **Connections to adjacent structures (§7).** The Aitchison log-ratio geometry [Pawlowsky-Glahn–Egozcue] for compositional data analysis places simplicial coordinates on the log-simplex; we record the compatibility. The qubit SIC-POVM and its simplicial realization [companion note] provide a quantum-statistical instance of the same simplicial frame, with the Born rule acting as the simplicial-quantum analog of the sphere pullback.

---

## 2. The Probability Simplex as a Gauge Slice

Let $N \geq 2$. The *open probability simplex* is
$$\Delta_N^\circ := \left\{ p \in \mathbb{R}^N : p_i > 0,\ \sum_i p_i = 1 \right\}.$$
Its closure $\overline{\Delta_N}$ allows $p_i = 0$. The simplex interior is an $(N-1)$-dimensional smooth manifold.

### 2.1 Affine identification with the zero-sum hyperplane

Let $\mathbf{1} = (1,\ldots,1) \in \mathbb{R}^N$, and let $H = \{c \in \mathbb{R}^N : \sum c_i = 0\}$ be the zero-sum hyperplane of [Paper 1 §2.3]. The map
$$\eta : \Delta_N^\circ \to H, \quad \eta(p) := p - \tfrac{1}{N}\mathbf{1},$$
is an affine diffeomorphism of $\Delta_N^\circ$ with the open subset $\{c \in H : c_i > -\tfrac{1}{N}\} \subset H$. The uniform distribution $p = \tfrac{1}{N}\mathbf{1}$ maps to the origin of $H$.

This is the statement, made explicit, that the probability simplex is the slice of the gauge equivalence class through $\tfrac{1}{N}\mathbf{1}$: the gauge equivalence relation $c \sim c'$ iff $c - c' \in \mathbb{R}\mathbf{1}$ restricts to an equivalence of slices $\{c : \sum c_i = t\}$ indexed by $t \in \mathbb{R}$, and the probability simplex is the slice $t = 1$ restricted to the positive orthant.

### 2.2 Why this framing matters

Classical expositions treat the probability simplex as an abstract $(N-1)$-dimensional manifold and introduce charts in one of three standard ways:

(a) Project onto the first $N-1$ coordinates, treating $p_N = 1 - \sum_{i<N} p_i$ as dependent. This breaks $S_N$ symmetry by distinguishing $p_N$.

(b) Introduce natural parameters $\theta_i = \log(p_i/p_0)$ with $p_0$ a reference distribution — usually uniform, sometimes a boundary distribution. This breaks symmetry by distinguishing the reference.

(c) Use the square-root embedding $x_i = \sqrt{p_i}$ to realize the simplex as the positive orthant of $S^{N-1}$. This preserves $S_N$ symmetry but introduces an ambient Euclidean structure in $\mathbb{R}^N$ that is not justified by any intrinsic feature of the statistical manifold.

The simplicial framing of §2.1 does (c)'s preservation of $S_N$ symmetry without (c)'s appeal to an arbitrary Euclidean ambient: the ambient structure in simplicial coordinates is the Gram matrix $G$ of [Paper 1 §2.4], intrinsic to the simplicial frame, and the geometry of the simplex is read off from the restriction of $G$ to $H$. Section 3 makes the comparison precise.

**Remark 2.1 (Interior vs. closure).** Throughout this paper we work in the open simplex interior $\Delta_N^\circ$, where all $p_i > 0$; this is the domain on which the Fisher–Rao metric is classically defined and Amari's dually flat structure is smooth. Boundary strata ($p_i = 0$ for some $i$) correspond to degenerate distributions where the Fisher metric blows up; their treatment requires additional care and is standard in the information-geometry literature [Amari, Ch. 2].

---

## 3. The Fisher–Rao Metric and the Sphere Pullback

### 3.1 The Fisher metric on the simplex

The Fisher information metric on $\Delta_N^\circ$, expressed on tangent vectors $v, w \in T_p \Delta_N^\circ = H$, is
$$g^F_p(v, w) := \sum_{i=1}^N \frac{v_i w_i}{p_i}. \qquad (3.1)$$
The restriction $\sum v_i = \sum w_i = 0$ is automatic since $v, w \in H$.

### 3.2 The sphere pullback

Define $\varphi : \Delta_N^\circ \to \mathbb{R}^N$ by $\varphi(p)_i = \sqrt{p_i}$. Since $\sum (\sqrt{p_i})^2 = \sum p_i = 1$ and $\sqrt{p_i} > 0$, the image lies in the positive orthant of the unit sphere $S^{N-1} \subset \mathbb{R}^N$.

The differential of $\varphi$ acts on tangent vectors by
$$(d\varphi)_p(v)_i = \frac{v_i}{2\sqrt{p_i}}.$$
The pullback of the ambient Euclidean metric on $\mathbb{R}^N$ (which restricts to the round metric on $S^{N-1}$) is therefore
$$\varphi^*(dx \cdot dx)(v, w) = \sum_i \frac{v_i w_i}{4 p_i} = \tfrac{1}{4}\, g^F_p(v, w).$$

**Proposition 3.1 (Sphere characterization of Fisher–Rao).** *The Fisher–Rao metric on the open probability simplex is four times the pullback along the square-root map $\varphi$ of the round metric on the positive orthant of the unit sphere $S^{N-1} \subset \mathbb{R}^N$.*

This is classical; see Amari [Amari, §2.1] or Nielsen [Nielsen] for textbook statements. We record it here for reference because the rest of this section exploits it.

This also clarifies the geometry used in recent manifold-steering experiments. Wurgaft et al. [Wurgaft et al. 2026] use the square-root embedding \(p\mapsto\sqrt p\) to fit behavior manifolds in Hellinger geometry, then compare activation-manifold arc length with behavior-manifold arc length. Proposition 3.1 says exactly what this coordinate choice is: the positive orthant of the unit sphere pulls back to the Fisher-Rao metric on the open categorical simplex. It is therefore one admissible spherical presentation of the same object that the \(m\)- and \(e\)-flat coordinates present dually. Their cubic-spline curves should be read accordingly: depending on whether the interpolation parameter is treated as a probability/moment coordinate, a logit/natural coordinate, or a spherical Hellinger coordinate, the fitted path is approximating an \(m\)-flat, \(e\)-flat, or Fisher-Rao geodesic surrogate. The empirical fact that the Hellinger behavior manifold matches activation geometry is thus not a competing construction; it is a measured instance of the simplex geometry developed here.

**Corollary 3.1.1 (Constant scalar curvature of the categorical Fisher–Rao base, all $N$).** *The Fisher–Rao metric $g^F$ on $\Delta_N^\circ$ has constant sectional curvature $1/4$ and constant scalar curvature*
$$R(g^F) \;=\; \frac{(N-1)(N-2)}{4}. \qquad (3.1\text{bis})$$
*Equivalently, $(\Delta_N^\circ, g^F)$ is isometric to the positive orthant of the round sphere of radius $2$ in $\mathbb{R}^N$.*

*Proof.* By Proposition 3.1, $g^F = 4\,\varphi^* h_{\mathrm{round}}$, where $h_{\mathrm{round}}$ is the round metric on the unit sphere $S^{N-1}\subset\mathbb{R}^N$. The unit $(N-1)$-sphere has constant sectional curvature $1$ and scalar curvature $(N-1)(N-2)$. A conformal rescaling $g\mapsto c^2 g$ multiplies sectional curvature and scalar curvature by $c^{-2}$; with $c^2=4$, the sectional curvature of $g^F$ is $1/4$ and its scalar curvature is $(N-1)(N-2)/4$. The image of $\varphi$ identifies $(\Delta_N^\circ, g^F)$ with the orthant of $S^{N-1}$ carrying the rescaled round metric $4 h_{\mathrm{round}}$, which is the round metric on the sphere of radius $2$. $\square$

The corollary is a direct consequence of Proposition 3.1 and standard sphere geometry. We record it because the single closed form covers every conductor depth $N$ and supplies the scalar-curvature input on which the later program builds. Two specializations have been independently verified in a recent nonlinear sigma-model construction on statistical-manifold bases: the $N=3$ case $R=1/2$ in Amaral [Amaral 2025, §3.3, Eq. (14)] and the $N=2$ Bernoulli case $R=0$ in [Amaral 2025, §3.1]. For the squarefree primorial values $N = P_n$ relevant to the conductor program of [Paper 47, Paper 48], the curvatures are $R(P_2{=}6)=5$, $R(P_3{=}30)=203$, $R(P_4{=}210)=10{,}868$, and $R(P_5{=}2310)=1{,}332{,}293$. Because curvature is constant, $\nabla R = 0$ and the Riemann normal coordinate expansion of $g^F$ truncates at $\mathcal O(\xi^4)$ at every point; the background-field perturbation theory exploited for $N=3$ in [Amaral 2025, §4.2] extends without modification to every $N$.

### 3.3 Fisher–Rao at the uniform

At $p_* := \tfrac{1}{N}\mathbf{1}$, formula (3.1) gives
$$g^F_{p_*}(v, w) = N \sum_i v_i w_i = N\, \langle v, w \rangle_{\mathrm{Euc}}, \quad v, w \in H,$$
where $\langle\cdot,\cdot\rangle_{\mathrm{Euc}}$ is the ambient Euclidean inner product on $\mathbb{R}^N$ restricted to $H$. The simplicial inner product on $H$ is $\langle v, w\rangle_s = \tfrac{N}{N-1}\langle v, w\rangle_{\mathrm{Euc}}$ [Paper 1 Prop. 2.1]. Therefore
$$g^F_{p_*} = (N - 1)\, \langle \cdot, \cdot \rangle_s. \qquad (3.2)$$

**Proposition 3.2 (Fisher–Rao = simplicial inner product, at the uniform).** *The Fisher–Rao metric at the uniform distribution $p_* = \tfrac{1}{N}\mathbf{1}$ is exactly $(N-1)$ times the simplicial inner product of [Paper 1 §2.4] restricted to $H = T_{p_*}\Delta_N^\circ$. In particular, the two metrics are conformally equivalent, with conformal factor $N - 1$, and determine the same Riemannian geometry on the tangent space at the uniform up to overall scale.*

The fact that Fisher–Rao is only defined up to positive rescaling [Chentsov, Amari §2.2] means Proposition 3.2 is a strict *equality* of metrics once the overall scale is fixed conventionally; no loss of information in the factor of $N-1$.

### 3.4 Tangent-space isometries at the uniform are simplicial rotations

Because the sphere pullback $\varphi$ sends $p_*$ to the point $\varphi(p_*) = \tfrac{1}{\sqrt{N}}\mathbf{1} \in S^{N-1}$, whose tangent space inside $\mathbb{R}^N$ is
$$T_{\varphi(p_*)} S^{N-1} = (\tfrac{1}{\sqrt{N}}\mathbf{1})^\perp = \mathbf{1}^\perp = H,$$
the tangent spaces on both sides of $\varphi$ at the respective base points coincide canonically with $H$. The Fisher–Rao isometry group of this tangent space is the orthogonal group $O(H, g^F_{p_*})$. By Proposition 3.2, this is $O(H, \langle\cdot,\cdot\rangle_s)$. Its identity component, $SO(H, \langle\cdot,\cdot\rangle_s)$, is realized by the simplicial rotations $R(u,\theta) = \exp(\theta K(u))$ of [Paper 1 §5] — exactly, with no intermediate change of variable.

**Proposition 3.3 (Simplicial rotations as Fisher–Rao tangent isometries at the uniform, $N = 4$).** *For $N = 4$, the group of orientation-preserving Fisher–Rao isometries of the tangent space $T_{p_*}\Delta_4^\circ = H$ at the uniform distribution $p_* = \tfrac{1}{4}\mathbf{1}$ is the image of the map $\{(u,\theta) : u \in H,\ \langle u,u\rangle_s = 1,\ \theta \in \mathbb{R}\} \to GL(H)$, $(u,\theta) \mapsto R(u,\theta)|_H$.*

*Proof.* By Proposition 3.2, the Fisher–Rao inner product on $H$ is a positive scalar multiple of the simplicial inner product. Orientation-preserving isometries of a three-dimensional inner-product space up to positive scalar are $SO(3)$. By [Paper 1 §5.2] the exponential map of $K(u)$ over unit zero-sum axes $u$ surjects onto the identity component of simplicial-orthogonal transformations of $H$, which is $SO(H, \langle\cdot,\cdot\rangle_s) \cong SO(3)$. $\square$

**Remark 3.4 (Global vs.\ local).** Proposition 3.3 addresses the tangent space at the uniform. The Fisher–Rao metric on the whole simplex $\Delta_N^\circ$ is *not* homogeneous under the simplicial rotation group: away from the uniform distribution, the metric (3.1) has coefficients $1/p_i$ that depend on position, and simplicial rotations do not preserve the simplex (they may send interior points to exterior points). The global Fisher–Rao isometry group of $\Delta_N^\circ$ is the discrete symmetric group $S_N$ (permutation of outcomes), reflecting the boundary structure of the simplex. Simplicial rotations describe the geometry of the Fisher–Rao metric *at the uniform point*; this is the point at which the simplex's maximal-entropy distribution is realized, and is the natural initialization point for parametric learning — which is what makes §6 computationally relevant.

**Remark 3.5 (The $\varphi$ pullback, explicit).** The simplicial rotation $R(u,\theta)$ acts on $H$; the sphere picture places $H$ as the tangent space at $\varphi(p_*) = \tfrac{1}{\sqrt{N}}\mathbf{1}$. The rotation in $\mathbb{R}^N$ whose action on the tangent plane at this point realizes $R(u,\theta)$ is the unique element of $SO(N) \cap \mathrm{Stab}(\tfrac{1}{\sqrt{N}}\mathbf{1})$ extending it — which is, by [Paper 1 §6], the $4 \times 4$ matrix $R(u,\theta)$ itself (for $N = 4$), interpreted as an element of $SO(N)$ via the embedding of simplicial coordinates into $\mathbb{R}^N$. The gauge-fixing $R(u,\theta)\mathbf{1} = \mathbf{1}$ of [Paper 1 Prop. 6.1(2)] is the statement that the rotation fixes the base point on the sphere, which is the defining feature of a tangent-space isometry. *The gauge-fixing property of Paper 1 is information-geometrically the invariance of the uniform distribution under Fisher–Rao isometries of its tangent space.*

---

## 4. The Dually Flat Structure in Simplicial Coordinates

### 4.1 Categorical exponential family, gauge-symmetrically

The categorical distribution on $N$ outcomes in the exponential family form writes
$$p(x = i \mid \theta) = \frac{e^{\theta_i}}{\sum_{j=1}^N e^{\theta_j}} = \frac{e^{\theta_i}}{Z(\theta)}. \qquad (4.1)$$
The natural parameters $\theta \in \mathbb{R}^N$ carry the gauge redundancy
$$\theta' = \theta + k \mathbf{1} \quad \Longrightarrow \quad p(\cdot\mid\theta') = p(\cdot\mid\theta), \qquad (4.2)$$
because the shift by $k\mathbf{1}$ multiplies every $e^{\theta_i}$ by $e^k$, which cancels between numerator and partition function. The natural parameter space is therefore $\mathbb{R}^N / \langle \mathbf{1}\rangle$, canonically realized by $H$ (the zero-sum representatives).

The moment parameters of (4.1) are
$$\eta_i := \mathbb{E}_\theta[\mathbf{1}_{x = i}] = p(x = i \mid \theta) = \frac{e^{\theta_i}}{Z(\theta)}, \qquad (4.3)$$
so $\eta_i = p_i$. The moment parameters satisfy $\sum \eta_i = 1$ by construction (the normalization of $p$), making them the probability simplex coordinates of §2. Their zero-sum shift $\eta - \tfrac{1}{N}\mathbf{1}$ lies in $H$.

Both $\theta$ and $\eta$ therefore carry simplicial content, with a symmetric role: $\theta$ has gauge freedom, $\eta$ has a gauge-fixing constraint ($\sum \eta_i = 1$). This is not an accident. The exchange between them is the Legendre transform.

### 4.2 Legendre duality on the simplicial frame

The log partition function $\psi(\theta) := \log Z(\theta) = \log \sum_i e^{\theta_i}$ is the cumulant generating function of the exponential family. Its gradient gives the moment parameters:
$$\frac{\partial \psi}{\partial \theta_i} = \frac{e^{\theta_i}}{Z(\theta)} = \eta_i.$$
Its Hessian gives the Fisher information matrix in $\theta$-coordinates (see §4.4).

The Legendre conjugate of $\psi$ is the negative entropy
$$\varphi(\eta) := \sum_i \eta_i \log \eta_i,$$
defined for $\eta$ in the open simplex; its gradient recovers the natural parameters up to gauge:
$$\frac{\partial \varphi}{\partial \eta_i} = \log \eta_i + 1 = \theta_i + (1 - \psi(\theta)),$$
and the constant $(1 - \psi)$ is a pure gauge shift in $\theta$. Modulo gauge,
$$\theta \equiv \nabla \varphi(\eta) \pmod{\mathbb{R}\mathbf{1}}, \qquad \eta = \nabla \psi(\theta). \qquad (4.4)$$

Classical expositions "fix the gauge" in (4.4) by choosing a reference outcome $p_0$ (often the last component $p_N$) and writing $\theta_i = \log(p_i / p_0)$, at which point the "natural parameter space" is declared to be $\mathbb{R}^{N-1}$ and the above duality reads as a Legendre transform between $\mathbb{R}^{N-1}$ and the interior of the simplex. This gauge fixing is exactly analogous to the classical choice of Cartesian frame addressed in [Paper 1 §1]: it breaks $S_N$ symmetry for computational convenience and makes the $N$-fold symmetry of the underlying object harder to see.

In the simplicial frame, (4.4) is a duality between $\mathbb{R}^N / \langle \mathbf{1}\rangle$ (realized by $H$) on the $\theta$-side and the affine hyperplane $\{\eta : \sum \eta_i = 1\}$ (also realized by $H$ after the shift $\eta - \tfrac{1}{N}\mathbf{1}$) on the $\eta$-side. *Both sides are $H$.* The Legendre transform is an endomorphism of $H$, nonlinear away from the uniform, and $S_N$-equivariant throughout.

The equivariance group is exactly \(S_N\) if one asks for a linear symmetry that survives the Legendre passage.

**Proposition 4.1 (Linear Fisher-Legendre symmetries are permutations).** *Let \(A\in O(H)\). Suppose that for all zero-sum natural parameters \(\theta\in H\),*
$$
\eta(A\theta)-\frac1N\mathbf 1
=
A\left(\eta(\theta)-\frac1N\mathbf 1\right).
$$
*Then \(A\) is the restriction to \(H\) of a permutation matrix. Conversely, every permutation matrix satisfies this identity.*

*Proof.*  The centered moment map \(\theta\mapsto\eta(\theta)-\frac1N\mathbf 1\) has image the interior of the centered probability simplex, whose vertices are \(e_i-\frac1N\mathbf 1\).  If \(A\) satisfies the displayed identity and is invertible, it preserves this open simplex and therefore its closure.  A linear automorphism of a polytope that preserves the polytope maps extreme points to extreme points, so \(A\) permutes the centered vertices.  Hence \(A\) is the restriction of an element of \(S_N\).  Conversely, if \(P_\sigma\) is a permutation matrix, then \(\eta(P_\sigma\theta)=P_\sigma\eta(\theta)\) follows directly from the softmax formula. \(\square\)

### 4.3 The KL divergence in simplicial coordinates

The canonical divergence of the dually flat structure on the categorical is the Kullback–Leibler divergence,
$$D(p \,\|\, q) = \sum_i p_i \log\frac{p_i}{q_i}. \qquad (4.5)$$
By the Bregman expression for canonical divergences in dually flat spaces [Amari §3.4],
$$D(p \,\|\, q) = \psi(\theta_q) - \psi(\theta_p) - \langle \eta_p, \theta_q - \theta_p \rangle_{\mathrm{pair}}, \qquad (4.6)$$
where $\langle \cdot, \cdot \rangle_{\mathrm{pair}}$ is the duality pairing between the $\eta$- and $\theta$-sides. In simplicial coordinates, this pairing is the ambient Euclidean inner product on $\mathbb{R}^N$, *not* the simplicial inner product: because of the gauge freedom in $\theta$, the pairing $\langle \eta, \theta \rangle = \sum \eta_i \theta_i$ depends on the gauge representative of $\theta$, but the expression (4.6) is gauge-invariant because $\sum \eta_i = 1$ makes the ambiguity in $\sum \eta_i \theta_i$ equal to the ambiguity in $\psi(\theta)$. Explicitly, shifting $\theta \mapsto \theta + k\mathbf{1}$ shifts $\psi \mapsto \psi + k$ and the pairing $\langle \eta, \theta\rangle \mapsto \langle \eta, \theta\rangle + k$; these cancel in (4.6).

**Remark 4.1 (Gauge consistency of the Bregman form).** The ambient Euclidean pairing is not a geometric object on $H$ (it is not gauge-invariant), but the *difference* expression (4.6) is gauge-invariant because of the compensating gauge transformation of $\psi$. This is the simplicial-coordinate analog of the classical observation that KL divergence is independent of reference-distribution choice in the $\theta$-chart.

### 4.4 The Fisher metric in $\theta$-coordinates

The Hessian of $\psi$ gives the Fisher metric in natural coordinates:
$$F(\theta)_{ij} = \frac{\partial^2 \psi}{\partial \theta_i \partial \theta_j}.$$
Direct computation from $\psi = \log Z$:
$$\frac{\partial^2 \psi}{\partial \theta_i \partial \theta_j} = \frac{\partial}{\partial \theta_j}\frac{e^{\theta_i}}{Z} = \frac{e^{\theta_i}\delta_{ij}}{Z} - \frac{e^{\theta_i} e^{\theta_j}}{Z^2} = p_i \delta_{ij} - p_i p_j. \qquad (4.7)$$

Denote this matrix $F(\theta) = \mathrm{diag}(p) - p p^\top$. By construction $F(\theta)\mathbf{1} = p - p \cdot (\sum p_i) = 0$, so the gauge direction is in the kernel — as it must be, since shifting $\theta$ by $k\mathbf{1}$ does not change $p$ and so cannot affect the Fisher information.

At $\theta = 0$ (where $p = p_* = \tfrac{1}{N}\mathbf{1}$):
$$F(0)_{ij} = \frac{1}{N}\delta_{ij} - \frac{1}{N^2} = \frac{1}{N^2}\bigl(N \delta_{ij} - 1\bigr) = \frac{1}{N^2}\bigl(N I - J\bigr)_{ij}. \qquad (4.8)$$

Compare the simplicial Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J = \tfrac{1}{N-1}(N I - J)$. Therefore
$$F(0) = \frac{N - 1}{N^2}\, G. \qquad (4.9)$$

**Proposition 4.2 (Softmax Fisher at initialization equals simplicial Gram, up to scale).** *The Fisher information matrix of the softmax-parameterized categorical (4.1), evaluated at $\theta = 0$, is $\tfrac{N-1}{N^2}$ times the simplicial Gram matrix $G$ of [Paper 1 §2.4].*

This is the content of §6: the Fisher information at initialization has no content beyond what is already in the simplicial frame.

---

## 5. Chentsov Uniqueness, Simplicially

Chentsov's theorem [Chentsov; Amari §2.3] states that the Fisher–Rao metric is, up to positive rescaling, the unique Riemannian metric on statistical manifolds invariant under Markov morphisms (equivalently: coarsenings that respect the statistical structure). For the categorical manifold $\Delta_N^\circ$ on fixed $N$, a weaker statement suffices: the Fisher–Rao metric is the unique $S_N$-invariant Riemannian metric up to positive rescaling at the uniform distribution (the only point of the simplex fixed by the full $S_N$-action).

This has a linear-algebraic shadow on the simplicial frame:

**Proposition 5.1 (Simplicial Gram is the unique $S_N$-invariant form).** *Let $B$ be a symmetric positive semidefinite bilinear form on $\mathbb{R}^N$ that is $S_N$-invariant (i.e., $B(P_\sigma a, P_\sigma b) = B(a, b)$ for every permutation $\sigma$ and permutation matrix $P_\sigma$) and has $\mathbf{1}$ in its kernel. Then $B$ is a nonnegative scalar multiple of the simplicial Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$.*

*Proof sketch.* $S_N$-invariance of $B$ forces $B$ to have two independent parameters: $\alpha = B_{ii}$ (diagonal) and $\beta = B_{ij}$ for $i \neq j$ (off-diagonal). So $B = \alpha I + \beta(J - I) = (\alpha - \beta)I + \beta J$. The condition $B\mathbf{1} = 0$ gives $(\alpha - \beta) + N\beta = 0$, i.e.\ $\beta = -\alpha/(N-1)$. Substituting, $B = \alpha(I - \tfrac{1}{N-1}(J - I)) = \alpha \cdot G$. Positive semidefiniteness forces $\alpha \geq 0$. $\square$

Proposition 5.1 is a purely linear-algebraic fact. Its content is that, once we ask for an $S_N$-invariant inner product on the zero-sum hyperplane — which is exactly what Chentsov's theorem demands at the uniform — there is only the simplicial one. The scalar $(N-1)$ appearing in (3.2) is the unique scalar that makes this Fisher–Rao.

**Remark 5.2 (Status of this result).** This is not a new theorem; it is a linear-algebraic restatement of the standard $S_N$-invariance argument that any text treats implicitly in the categorical case. The simplicial framing makes it transparent: the Gram matrix $G$ is not a coincidence of the simplicial construction, it is forced by the statistical geometry.

---

## 6. Natural Gradient in Simplicial Coordinates

### 6.1 The problem

Natural gradient descent [Amari 1998] replaces the Euclidean gradient $\nabla L(\theta)$ of a loss function by the Fisher-rescaled gradient $F(\theta)^{-1}\nabla L(\theta)$, where $F$ is the Fisher information matrix. For softmax-parameterized categoricals (4.1), $F(\theta) = \mathrm{diag}(p) - p p^\top$ of (4.7), which is gauge-degenerate: $F\mathbf{1} = 0$. The natural gradient is therefore defined up to a gauge shift, and requires a pseudoinverse.

Standard implementations handle this by one of:
(a) Fixing the gauge ($\theta_N \equiv 0$) and working in the $(N-1) \times (N-1)$ Fisher block, then inverting explicitly. Cost: $O(N^3)$ per step for $N$ classes.
(b) Using the Sherman–Morrison identity on $F = \mathrm{diag}(p) - p p^\top$ to avoid full inversion, yielding $O(N^2)$ per step.
(c) Approximating $F$ by its diagonal ($F_{\mathrm{diag}} = \mathrm{diag}(p)$) and dividing coordinate-wise. $O(N)$, inaccurate except near boundary.

At initialization ($\theta = 0$, $p = p_*$), the simplicial framing collapses (a) and (b) to a closed form.

### 6.2 Closed form at the uniform

By Proposition 4.2, $F(0) = \tfrac{N-1}{N^2}\, G$ where $G$ is the simplicial Gram matrix. By [Paper 1 §2.4] and the computation following Prop. 2.1, $G$ restricted to $H$ equals $\tfrac{N}{N-1}\, I_H$. Therefore
$$F(0)\big|_H = \frac{N - 1}{N^2} \cdot \frac{N}{N-1}\, I_H = \frac{1}{N}\, I_H.$$
The Moore–Penrose pseudoinverse $F(0)^+$ on the gauge-complement $H$ is therefore
$$F(0)^+\big|_H = N\, I_H, \qquad F(0)^+(\mathbf{1}) = 0,$$
yielding the explicit formula
$$F(0)^+ = N\, \Pi_H, \qquad (6.1)$$
where $\Pi_H$ is the orthogonal projector onto $H$ (with respect to either the simplicial or the ambient Euclidean inner product; the two coincide on the gauge-complement).

The natural gradient step at initialization is therefore
$$\Delta \theta = -\varepsilon\, F(0)^+ \nabla L(0) = -\varepsilon N\, \Pi_H \nabla L(0), \qquad (6.2)$$
i.e., "subtract the mean of the gradient, scale by $N$, step." This is $O(N)$ and involves no matrix inversion.

**Proposition 6.1 (Softmax natural gradient at initialization).** *For any smooth loss $L : \mathbb{R}^N \to \mathbb{R}$ on softmax natural parameters, the natural gradient of $L$ evaluated at $\theta = 0$ is*
$$\nabla^{\mathrm{nat}} L(0) = N \cdot \bigl(\nabla L(0) - \overline{\nabla L(0)}\, \mathbf{1}\bigr),$$
*where $\overline{\nabla L(0)} = \tfrac{1}{N}\sum_i \partial_i L(0)$ is the mean of the gradient.*

*Proof.* Apply (6.1) to $\nabla L(0)$. $\square$

### 6.3 Rotation-step interpretation

Beyond the uniform, the natural gradient direction at initialization can be expressed as a simplicial rotation of the canonical basis. Let $u := \nabla^{\mathrm{nat}} L(0) / \|\nabla^{\mathrm{nat}} L(0)\|_s$ be the unit simplicial direction of descent (assume non-degenerate). The first-order update $\theta \mapsto \theta - \varepsilon u$ can be equivalently written, for small $\varepsilon$, as the action of a simplicial rotation on $\theta$ in the plane $(\theta, u)$: by [Paper 1 §5], this is $R(w, \varepsilon \|u\|)$ for an axis $w$ orthogonal to both $\theta$ and $u$.

At $\theta = 0$, every $w \in H$ with $\langle w, u\rangle_s = 0$ qualifies, and the update becomes geometrically a Fisher–Rao geodesic step on the statistical manifold — the tangent geodesic from $p_*$ in direction $u$, pulled back from the sphere through $\varphi^{-1}$. Away from initialization, this interpretation requires correction by the Amari–Chentsov cubic of the statistical manifold under the chosen connection. With the Paper 11 sign convention,
$$
K^{CH}=\Gamma^{(m)}-\Gamma^{(e)},\qquad
g_p(K^{CH}_p(u)v,w)=T_p(u,v,w),
$$
so \(K^{CH}\) is the raised cubic operator measuring the first systematic separation between \(m\)-flat, \(e\)-flat, and Fisher/Hellinger-geodesic motion. If a calculation uses the opposite \(e/m\) convention, the norms are unchanged but the displayed signed endpoint deviations must be reversed.

For the tetrahedral categorical simplex, this cubic has an entirely
simplicial presentation at the uniform point.  Let
\(p_*=\frac14\mathbf1\), \(H=T_{p_*}\Delta_4^\circ\), \(M=4I-J\), and
\(\tau_i=e_i-\frac14\mathbf1\).  The vectors \(\tau_i\) are the four
centered tetrahedral vertex directions, and Paper 1, Section 3.5 defines
the symmetric product
$$
u\circ_\Delta v
:=
\frac34\sum_{i=1}^4
\langle\tau_i,u\rangle_M\left(I+K(\tau_i)^2\right)v.
$$
Since \(g_{p_*}(u,v)=\langle u,v\rangle_M\), the raised
Amari-Chentsov cubic satisfies
$$
K^{CH}_{p_*}(u)v=u\circ_\Delta v.
$$
In coordinates this recovers
\(4(u\odot v)-(\sum_i u_iv_i)\mathbf1\), but the intrinsic formula uses
only the Gram pairing and the cross-product projector squares
\(I+K(\tau_i)^2\).

This is also the operator that appears when the Fisher geometry is pulled back through a behavior map. If \(F:A\to\Delta_N^\circ\) sends activations to output distributions and \(g_y\) is the behavior-space Fisher/Hellinger metric, then
$$
G_F(h)=J_F(h)^\top g_y(F(h))J_F(h)+\epsilon I
$$
is the leading quadratic Fisher pullback used by Wurgaft et al. [Wurgaft et al. 2026]. The next local term is governed by the Amari-Chentsov cubic pulled back along \(F\), together with the covariant Hessian of \(F\) when \(F\) is not locally affine. Thus the measured recovery of activation-manifold paths from behavior-manifold targets is the experimental counterpart of the Fisher pullback story: if \(F\) is approximately a Riemannian quasi-isometry on a concept region, then Hellinger/Fisher geodesics in behavior space and density geodesics in activation space must agree to leading order, with the first systematic discrepancy controlled by the pulled-back \(K^{CH}\).

### 6.4 Practical consequences

The $O(N)$ natural gradient step of (6.2) is known in the ML folklore as "subtract the mean" — see e.g.\ implementations of softmax-cross-entropy backward pass, where the mean-subtraction appears naturally as the derivative of the log-softmax. The simplicial framing identifies this familiar step as the exact natural gradient at initialization, not an approximation or heuristic. In particular, during the initial phase of softmax-cross-entropy training — before the output distribution has substantially concentrated on any class — the Euclidean gradient with mean-subtraction is, up to a rescaling, *exactly* the natural gradient. This is a reframing of a standard algorithm, not a new algorithm.

For NLP classifiers and policy networks with $N$ much larger than input/hidden dimensions (typical: $N$ = vocabulary size = $10^4$–$10^5$; hidden dimension $d \ll N$), (6.2) avoids the $O(N^2)$ Fisher matrix and its factorization, matching the $O(Nd)$ cost of standard backpropagation.

---

## 7. Connections to Adjacent Structures

### 7.1 Aitchison geometry

Compositional data analysis [Pawlowsky-Glahn–Egozcue] treats vectors of positive proportions modulo rescaling, with the *Aitchison inner product* on the log-simplex
$$\langle p, q \rangle_A := \frac{1}{N}\sum_{i < j}(\log p_i - \log p_j)(\log q_i - \log q_j).$$
After the component-wise logarithm and the isometric log-ratio (ilr) transformation, compositional data lives in $H$ with an inner product proportional to the ambient Euclidean one. On $H$, this agrees up to a positive scalar with the simplicial inner product of [Paper 1 §2.4].

The Aitchison metric is not the Fisher–Rao metric of §3; the two measure different notions of distance on the simplex (Aitchison measures log-ratio discrepancies, which are appropriate for compositional interpretation; Fisher–Rao measures statistical-estimation discrepancies). Both, however, share the simplicial frame as their native coordinate system, and the simplicial rotation $R(u,\theta)$ acts simultaneously as an isometry of the Aitchison metric and (at the uniform) as a Fisher–Rao tangent-space isometry. The geometric and statistical interpretations of the rotation differ; the kinematic object is the same.

The distinction becomes concrete for the parity-dual involution $\rho_2$ from the cyclotomic-simplicial frame.  For even $N$, let $s=(1,-1,\ldots,1,-1)$ and let
$$\rho_2\theta=\theta-\frac{2}{N}(s\cdot\theta)s.$$
In clr/ilr coordinates, $\rho_2$ is an orthogonal reflection of $H$, hence a global Aitchison isometry.  It is never a global Fisher–Rao isometry for even $N\geq4$: the Fisher geometry of $\Delta_N^\circ$ is globally preserved by outcome permutations, while $\rho_2\notin S_N$.  The $N=4$ stella-octangula coincidence only says $\rho_2\in S_4\cdot\{\pm I\}$, not that $\rho_2$ itself is a Fisher symmetry.  In dual coordinates, the same failure appears as
$$
\eta_i(\rho_2\theta)
=
\eta_i(\theta)\,
\frac{\exp\!\left(-\frac{2}{N}(s\cdot\theta)s_i\right)}{Z'(\theta)},
$$
for the normalizing factor $Z'(\theta)$.  Thus $\rho_2$ is linear on the $e$-flat $\theta$ side, but becomes a parity-weighted log-ratio rescaling on the $m$-flat $\eta$ side rather than an affine symmetry of the probability simplex.

At the centroid this failure is invisible: \(g^F_{p_*}\) is conformally equivalent to the Aitchison/simplicial metric, so every element of \(O(H)\) is an infinitesimal Fisher symmetry there.  What distinguishes \(\rho_2\) is not the local metric at \(p_*\), but the cyclotomic naming of a canonical reflection that the global Fisher-Legendre geometry does not retain.  More generally, the cyclotomic decomposition supplies the \(e\)-flat/Aitchison side with spectral block reflections in \(O(H)\), while Proposition 4.1 says that the Fisher-Legendre side remembers only their permutation combinations, such as the Galois multiplier actions of [Paper 7].

### 7.2 Quantum statistical manifolds: the qubit SIC

For a single qubit, the simplicial frame's four vectors in $H \cong \mathbb{R}^3$ are the Bloch vectors of a Symmetric Informationally Complete POVM [Renes–Blume-Kohout–Scott–Caves, companion note]. The SIC-probability vector $p \in \Delta_4^\circ$ of a density matrix $\rho$ is related to the Bloch vector $\vec{r}$ by
$$p_i = \frac{1}{4}(1 + \vec{r} \cdot \vec{n}_i),$$
and the zero-sum shift $p - \tfrac{1}{4}\mathbf{1}$ is proportional to the simplicial realization of $\vec{r}$. The quantum Fisher information (Helstrom/Bures metric [Braunstein–Caves]) at the maximally mixed state $\rho = I/2$ agrees up to scale with the classical Fisher–Rao on SIC probabilities at the uniform $p = \tfrac{1}{4}\mathbf{1}$. Projective unitary evolution of $\rho$ acts on $p$ by the simplicial rotation $R(u,\theta)$ of [Paper 1 §5], as shown in the companion note.

The qubit SIC is therefore the simplicial-quantum instance of §3.3: the simplicial rotation is simultaneously the Fisher–Rao tangent isometry (classical) and the Born-rule image of projective unitary evolution (quantum), and the two interpretations coincide at the simplicial-rotation level. *This is the §3.3–§6 Amari theory for a specific quantum statistical manifold.*

### 7.3 Markov chains and reaction networks

The chemical reaction network analogy recorded in [Paper 1 §2.2.1] has a statistical analog: on the probability simplex, continuous-time Markov chain generators $Q$ with $\mathbf{1}^\top Q = 0$ (conservation of probability) are the simplicial analog of stoichiometric compatibility. The simplicial framework of Amari's dually flat structure does not immediately yield new results for Markov chain analysis, but positions the three settings (CRNT, MCMC generators, Amari categorical) as instances of the same gauge-slice structure, which is a structural observation of potential future use.

---

## 8. Open Questions

### 8.1 Beyond the uniform: curvature in simplicial coordinates

Proposition 3.3 identifies simplicial rotations as Fisher–Rao isometries of the tangent space at the uniform. Away from the uniform, the Fisher metric has nonzero Amari–Chentsov curvature tensor, and its geodesic flow is not a simplicial rotation. Whether there is a position-dependent modification of $R(u,\theta)$ that realizes Fisher–Rao geodesic flow at arbitrary points on the simplex — equivalently, whether the $e$- or $m$-geodesics of Amari's dually flat structure have a simplicial expression — is open. Candidate: use the sphere pullback to reduce Fisher geodesics to great circles on $S^{N-1}$, then express the sphere rotation as a product of simplicial rotations using a composition formula for $R$ (currently open in [Paper 1 §8.3]).

The open question in the preceding paragraph should now be read as the
global finite-step question.  The local tangent-space replacement is explicit
in the tetrahedral case.  For \(p\in\Delta_4^\circ\), set
\(r_i=\sqrt{p_i}\) and define
$$
\bigl(K_p(u)\bigr)_{i\ell}
=
-\sum_{j,k=1}^4
\varepsilon_{ijk\ell}\frac{r_i r_j}{r_k r_\ell}u_k,
\qquad \varepsilon_{1234}=+1.
$$
This Fisher-Hodge matrix is the pullback of the Euclidean Hodge cross product
on \(r^\perp\) under the isometry \(x_i\mapsto x_i/r_i\).  It satisfies
\(D_pK_p(u)+K_p(u)^\top D_p=0\), \(K_p(u)p=0\), and
\(K_p(u)^3=-\|u\|_{g_p}^2K_p(u)\) on \(H\), with
\(D_p=\operatorname{diag}(1/p_i)\).  Hence for a \(g_p\)-unit axis,
$$
R_p(u,\theta)=I_H+\sin\theta\,K_p(u)+(1-\cos\theta)K_p(u)^2
$$
is the Fisher-orthogonal Rodrigues operator on \(T_p\Delta_4^\circ\).

The immediate computable version is no longer just qualitative.  At the
tetrahedral uniform point, Paper 1, Section 3.5 gives
\(K^{CH}_{p_*}\) as the symmetric product generated by the projector squares
\(I+K(\tau_i)^2\).  Off the centroid there is still an exact moving-frame
formula.  For each outcome \(i\), set
\(\sigma_i(p)=e_i-p\).  Then
$$
K^{CH}_p(u)v
=
\sum_i p_i\,g_p(\sigma_i(p),u)\,g_p(\sigma_i(p),v)\,\sigma_i(p).
$$
Equivalently, if \(\Pi_i^p\) is the Fisher-orthogonal projector onto
\(\mathbb R\sigma_i(p)\),
$$
K^{CH}_p(u)v
=
\sum_i(1-p_i)g_p(\sigma_i(p),u)\Pi_i^p v.
$$
For \(N=4\), \(\Pi_i^p=I+K_p(\widehat\sigma_i(p))^2\), where \(K_p\) is the
cross-product operator for the Fisher metric at \(p\).  Thus along
\(p(t)=p_*+th\), the uniform projectors deform by moving the score axes,
the metric, and the weights.  Comparing this exact cubic operator with the
second-order endpoint deviation of \(m\)-flat, \(e\)-flat, and
Hellinger/Fisher interpolation is the local invariant that Paper 11 studies
arithmetically and that Wurgaft et al. measure empirically through manifold
steering.

### 8.2 Prime cyclic behavior manifolds

The weekday experiment of Wurgaft et al. suggests a first benchmark beyond the uniform theorem. For a prime cyclic simplex \(C_\ell\), especially \(\ell=7\), the nontrivial Fisher tangent space is a single \((\ell-1)\)-dimensional additive-character conductor packet. At \(p_*=(1/\ell)\mathbf1\),
$$
K^{CH}_{p_*}(h)v=\ell\,h*v-\ell\langle h,v\rangle p_*,
$$
and in the additive-character basis the operator is pure convolution in \(\widehat{C_\ell}\). Thus the prime cyclic case isolates the behavior-side cubic with no nontrivial conductor splitting. The open problem is to replace parametric cyclic centroids by empirical output centroids and decompose the observed linear-versus-manifold gap into: intrinsic behavior cubic \(K^{CH}\) on \(M_y\), activation-side distortion of the pullback \(J_F^\top g_yJ_F\), and spline/parameterization residuals.

### 8.3 Higher-dimensional SICs and quantum statistical manifolds

For $d$-dimensional quantum systems with $d \geq 3$, the Bloch space is $(d^2 - 1)$-dimensional and the SIC configuration (when it exists) is not a regular simplex in that space. The classical analog — probability simplex on $N = d^2$ outcomes — is simplicially perfect, but the quantum-classical bridge of §7.2 fails: the quantum Fisher-Bures metric on $d$-dim density matrices does not reduce to the $N = d^2$ simplicial inner product at the maximally mixed state. Whether higher-rank simplicial operators (the $(N-3)$-ary Hodge-dual construction of [Paper 1 §8.2]) play any role for $d \geq 3$ quantum statistical manifolds is open.

### 8.4 Natural gradient beyond initialization

§6 gives a closed form for the natural gradient at the uniform. Away from the uniform, $F(\theta) = \mathrm{diag}(p) - p p^\top$ is not proportional to $G$; the simplicial framing loses its computational advantage. Whether a simplicial-coordinate-native form of position-dependent Fisher inversion — perhaps exploiting the sphere pullback $\varphi$ to reduce $F$-inversion to a sphere-tangent computation — is useful for mid-training natural gradient, is open. Related: preconditioned methods like K-FAC [Martens–Grosse] approximate the layerwise Fisher; the simplicial frame may or may not clarify that approximation for the output layer.

### 8.5 Chentsov in the simplicial wedge-Hodge framework

Chentsov's theorem for general statistical manifolds (not just the categorical) relies on Markov-morphism invariance. The simplicial frame of [Paper 1] is an object of categorical geometry, not of general statistical geometry; its natural symmetry group is $S_N$, not the full Markov category. Whether there is a simplicial-style intrinsic description for exponential families beyond the categorical — for example, for the Gaussian family or the discrete Markov chain family — is open. Candidate routes: replace the simplex with a Grassmannian or Stiefel manifold carrying an analogous gauge structure; or work with the relative-entropy structure directly as a Bregman divergence on the simplicial frame, extending §4.

---

## 9. Conclusion

The probability simplex is, at the level of coordinate geometry, a gauge slice of the simplicial coordinate system of [Paper 1]. The Fisher–Rao metric at the uniform distribution is the simplicial inner product rescaled by $(N-1)$; the simplicial rotation $R(u,\theta)$ realizes the Fisher–Rao tangent-isometry group at the uniform. The exponential-family natural parameters $\theta$ and the moment parameters $\eta$ both live in the gauge-redundant $\mathbb{R}^N / \langle \mathbf{1}\rangle$, with the Legendre duality between them equivariant under $S_N$. The Fisher information matrix of the softmax categorical at initialization is, up to a known scalar, the simplicial Gram matrix, yielding an $O(N)$ closed form for the natural gradient at that point. Chentsov's uniqueness theorem for the Fisher–Rao metric restricts, on the simplicial frame, to the linear-algebraic uniqueness of the simplicial Gram matrix as the $S_N$-invariant positive semidefinite bilinear form with $\mathbf{1}$ in its kernel.

The empirical behavior manifolds of Wurgaft et al. [Wurgaft et al. 2026] are a useful external test of this framing because their Hellinger construction is exactly the sphere-pullback presentation of Fisher-Rao geometry. In that setting, the first systematic deviation between linear paths and manifold paths has a named intrinsic operator: the pulled-back Amari-Chentsov cubic \(K^{CH}\).

We have made no new claims in information geometry proper. We have exhibited Amari's dually flat structure on the categorical in a coordinate system that preserves the $S_N$ symmetry the structure is built to respect — and in doing so have made visible, in a single $N$-dimensional gauge-redundant frame, what conventional expositions treat by breaking symmetry into $(N-1)$-dimensional charts. The claim of this paper is that the simplicial frame is not merely a convenient chart; it is the native one.

---

## Acknowledgments

[Standard.]

---

## References

[Amari] Amari, S. *Information Geometry and Its Applications*. Applied Mathematical Sciences, vol. 194. Springer, 2016.

[Amari 1998] Amari, S. "Natural gradient works efficiently in learning." *Neural Computation* 10(2), 251–276 (1998).

[Braunstein–Caves] Braunstein, S.L., Caves, C.M. "Statistical distance and the geometry of quantum states." *Physical Review Letters* 72(22), 3439–3443 (1994).

[Chentsov] Chentsov, N.N. *Statistical Decision Rules and Optimal Inference* (English translation). American Mathematical Society, 1982.

[companion note] Murillo Montero, L. "The Single-Qubit SIC-POVM as a Simplicial Coordinate System." [in preparation]

[Martens–Grosse] Martens, J., Grosse, R. "Optimizing neural networks with Kronecker-factored approximate curvature." *ICML* 2015.

[Nielsen] Nielsen, F. "An elementary introduction to information geometry." *Entropy* 22(10), 1100 (2020).

[Paper 1] Murillo Montero, L. "Intrinsic Vector Algebra on Simplicial (Quadray) Coordinates." 2026.

[Pawlowsky-Glahn–Egozcue] Pawlowsky-Glahn, V., Egozcue, J.J., Tolosana-Delgado, R. *Modeling and Analysis of Compositional Data*. Wiley, 2015.

[Renes–Blume-Kohout–Scott–Caves] Renes, J.M., Blume-Kohout, R., Scott, A.J., Caves, C.M. "Symmetric informationally complete quantum measurements." *J. Math. Phys.* 45(6), 2171–2180 (2004).

[Wurgaft et al. 2026] Wurgaft, D., Rager, C., Kowal, M., Shyam, V., Feucht, S., Bhalla, U., Haklay, T., Bigelow, E., Sarfati, R., McGrath, T., Lewis, O., Merullo, J., Goodman, N.D., Fel, T., Geiger, A., and Lubana, E.S. "Manifold Steering Reveals the Shared Geometry of Neural Network Representation and Behavior." arXiv:2605.05115v1, 2026.

---

## Notes to self (drafting, not for submission)

- **Length target.** 20–25 pages. This is a full paper, not a companion note — Paper 1's Fisher/Aitchison paragraph promised a full treatment, and this is it. If any section runs over, §7.3 (Markov chains) can be cut and §8.5 can be compressed; §5 could also be folded into a long remark inside §4 if space is tight.

- **The headline to foreground in §1.** Not (i) "Fisher = simplicial at uniform" — that's the setup. The headline is (ii): $\theta$ and $\eta$ both live in $\mathbb{R}^N / \langle \mathbf{1}\rangle$ and the Legendre transform is an endomorphism of $H$. This is the structural observation that a Fuchs / Nielsen / Amari-school reader registers as *new exposition*, not new math.

- **Critical cross-reference.** The claim "at the uniform" appears in §3, §4.4, §6 — verify consistency of the $(N-1)$ scalar across all of them. My calculation: $g^F_{p_*} = N \cdot \langle\cdot,\cdot\rangle_{\mathrm{Euc}}|_H$, simplicial $= \tfrac{N}{N-1}\cdot\langle\cdot,\cdot\rangle_{\mathrm{Euc}}|_H$, so ratio is $N-1$. And $F(0) = \tfrac{N-1}{N^2} G$, with $G|_H = \tfrac{N}{N-1} I_H$, so $F(0)|_H = \tfrac{1}{N} I_H$. The various scalars are mutually consistent but need a single consistent-units appendix to avoid reader confusion.

- **What I'm NOT claiming, in order of importance.** No new convergence rate for NGD. No new statistical estimator. No foundational claim about probability. §6 is a reframing of the softmax-cross-entropy gradient, not a new algorithm. §7.2 defers to the companion note. If the reader wants novelty in the pure-math sense, it is only in the simplicial-coordinate expression, nothing else.

- **Venue.** *Information Geometry* (Springer) is the natural home if the editor reads §4 as sufficiently novel as framing; *Entropy* is the safer second choice. *Foundations of Physics* would want §7.2 expanded substantially, which takes the paper in a different direction — probably better to keep §7.2 short here and let the companion note carry the physics audience.

- **Worked example to add if room permits.** The $N = 4$ case throughout §3–§6, with explicit matrices: the simplicial Gram, the Fisher at uniform, the pseudoinverse, a small natural gradient step on a 4-class softmax. Makes the ML reader's experience concrete.

- **Title alternatives.**
  1. *Simplicial Coordinates as the Native Language of Information Geometry* — current
  2. *Amari's Dually Flat Structure in Gauge-Symmetric Coordinates*
  3. *The Probability Simplex as a Gauge Slice: Information Geometry in Simplicial Coordinates*

  (1) is punchiest, (2) is most descriptive, (3) is safest. Decision deferred to v2.

- **Open for discussion:** Do I want to push §8.1 (beyond the uniform) into the main text? It is the natural continuation, but it is also the hardest open problem, and putting it in §8 rather than §3 keeps the paper's promise size calibrated to what the paper delivers.

---

*[End of draft.]*
