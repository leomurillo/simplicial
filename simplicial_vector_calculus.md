# Intrinsic Vector Calculus on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*April 21, 2026*

---

## Abstract

Simplicial (Quadray) coordinate systems use $N$ frame vectors pointing from the origin to the vertices of a regular $(N-1)$-simplex, providing an overcomplete, permutation-symmetric coordinate description of $(N-1)$-dimensional Euclidean space whose $N$ frame vectors form an *equiangular tight frame* (ETF) for $\mathbb{R}^{N-1}$ (Proposition 2.0). Such coordinates carry a one-dimensional gauge redundancy along the diagonal direction $\mathbf{1} = (1, 1, \ldots, 1)$, and the physically meaningful geometry lives on the zero-sum hyperplane $\{v : \sum v_i = 0\}$, which is isometric to $\mathbb{R}^{N-1}$ under the metric inherited from the ambient Gram matrix.

We develop an intrinsic algebraic vector calculus on this hyperplane, comprising three operators — an inner product, a binary cross product, and a rotation; differential operators ($\nabla$, $\mathrm{div}$, $\mathrm{curl}$) are not treated here. These three operators are jointly compatible with the gauge action in a precise sense: the inner product is gauge-invariant as a scalar, while the binary cross product and rotation preserve the zero-sum hyperplane and respectively annihilate and fix the gauge direction $\mathbf{1}$. Once the simplicial Gram data is fixed, their formulas require no ongoing reference to a Cartesian frame:

1. The **inner product** induced by the simplicial Gram matrix $G = \tfrac{N}{N-1} I - \tfrac{1}{N-1} J$ of §2.4, whose associated quadratic form collapses on zero-sum vectors to $\langle c, c\rangle = \tfrac{N}{N-1}\sum_i c_i^2$.
2. A **skew-symmetric bilinear operator** $K(u)$ that, for $N = 4$, functions as an intrinsic cross product — gauge-annihilating, hyperplane-closing, and satisfying the Lie-algebraic identity $K^3 = -K$ when $u$ is a zero-sum unit axis.
3. The **exponential map** of $K(u)$ into $\mathrm{SO}(3)$ for $N = 4$, yielding the closed-form Rodrigues formula $R = I + \sin\theta\, K + (1 - \cos\theta)\, K^2$.

For $N = 4$ we prove $K^3 = -K$ and derive the scaling constant $1/\sqrt{3}$ from first principles; the resulting rotation matrix fixes the gauge direction ($R\mathbf{1} = \mathbf{1}$), preserves zero-sum, and supplies a 9-multiplication kernel for applying rotations to zero-sum inputs. We identify $N = 4$ as the unique case *within the simplicial wedge–Hodge framework developed here* in which the construction yields a binary cross product and closed-form exponential (higher $N$ proceeds via Hodge duals of wedge products of arity $N - 3$, sketched in §8): the simplicial-coordinate reflection of the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$.

**Keywords:** simplicial coordinates, Quadray coordinates, barycentric coordinates, overcomplete coordinates, equiangular tight frame, ETF, SIC-POVM, erasure-robust frame, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation.

**MSC 2020:** 15A72 (multilinear algebra), 15A75 (exterior algebra, Grassmann algebras), 22E60 (Lie algebras of Lie groups), 53A45 (differential geometric aspects in vector and tensor analysis), 65D18 (numerical aspects of computer graphics).

---

## 1. Introduction

### 1.1 Motivation

The Cartesian coordinate system is the default arena of classical vector calculus, but it is not the unique one. A $(N-1)$-dimensional Euclidean space can equally well be described using $N$ frame vectors directed toward the vertices of a regular $(N-1)$-simplex: four frame rays in tetrahedral arrangement for 3-space ($N = 4$), three frame rays in triangular arrangement for the plane ($N = 3$). Such coordinates are overcomplete — one more coordinate than dimension — and carry a one-dimensional redundancy. The trade is explicit: in exchange for the redundancy, one gains full permutation symmetry of the frame and a natural framework for problems whose geometry is intrinsically simplicial.

This family of coordinate systems has appeared under several names. *Quadray coordinates* — introduced by Jarmusch in 1981 and subsequently elaborated by Urner [Urner], Ace [Ace], and others [QuadrayWiki] — are the $N = 4$ case, tied historically to Fuller's synergetics [Fuller]. Barycentric coordinates on the $(N-1)$-simplex, used ubiquitously in finite element analysis [Ciarlet, Brenner-Scott] and computational geometry, are the same structure with a different normalization. The probability simplex in information geometry [Amari, Chentsov] is the affine translate of the relevant hyperplane by one unit along the redundancy direction. All are facets of the same underlying object.

The natural algebraic question is whether this coordinate description supports an intrinsic vector calculus: inner product, cross product, rotation, and their closure properties, defined without reference to an ambient Cartesian frame. Partial answers exist. The inner product is standard from Gram matrix considerations. A general rotation operator about an arbitrary simplicial axis has been attempted in the Spread-Quadray Rotors framework [Thomson, §19] but left as an open question, with the existing implementation falling back on quaternion composition for axes that are not frame vectors.

This paper supplies the missing ingredient for $N = 4$. We construct a skew-symmetric bilinear operator $K(u)$ acting on zero-sum vectors and parameterized by an axis $u$ of unit simplicial norm, prove the Lie-algebraic identity $K^3 = -K$, and exponentiate it in closed form to obtain a rotation about $u$. Around this construction we establish a single gauge-compatibility theorem that packages the distinct invariance properties of the three operators: the (scalar) inner product is gauge-invariant, while the (vector-valued) cross-product operator and rotation preserve the zero-sum hyperplane and fix or annihilate the gauge direction. Together these results yield, for $N = 4$, an intrinsic algebra of rotations and their Lie-algebraic generators on the simplicial zero-sum hyperplane: once the simplicial Gram data is fixed, the operators require no ongoing reference to any Cartesian frame. Differential operators ($\nabla$, $\mathrm{div}$, $\mathrm{curl}$) are not developed here and remain outside the present scope.

### 1.2 Contributions

1. **Clarification of gauge structure (Section 2).** We name the one-dimensional redundancy spanned by $\mathbf{1} = (1, 1, \ldots, 1)^\top$ the *gauge direction*, and identify the zero-sum form as the *canonical gauge*. This language is structurally analogous to the gauge redundancy of physical gauge theories, to the stoichiometric compatibility classes of chemical reaction network theory [Müller-Regensburger], and to the tangent directions killed by the simplex constraint in information geometry [Amari, Chentsov]; we present these parallels as interpretive motivation, not as a formal equivalence of categories.

2. **Intrinsic cross product (Section 3).** We define a skew-symmetric bilinear operator $K(u)$, acting on zero-sum vectors and parameterized by an axis $u$ that is zero-sum and of unit simplicial norm (i.e.\ $u^\top G u = 1$, where $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ is the simplicial Gram matrix of Section 2.4). We prove $K$ annihilates the gauge direction, preserves the zero-sum hyperplane, and satisfies the Lie-algebraic identity $K^3 = -K$ for $N = 4$. The scaling constant $1/\sqrt{3}$ is derived from first principles via a spectral/trace computation on the underlying rank-2 skew generator.

3. **Joint gauge-compatibility theorem (Section 4).** We consolidate the invariance properties of the three operators — inner product, cross product, and rotation — into one structural statement, distinguishing the scalar and vector cases: the inner product is gauge-invariant as a scalar in both arguments ($\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$), while $K(u)$ and $R(u,\theta)$ preserve the zero-sum hyperplane and annihilate (respectively, fix) the gauge direction. Consequently all three operators descend to well-defined operations on the quotient $\mathbb{R}^N / \langle \mathbf{1}\rangle \cong \mathbb{R}^{N-1}$. This makes precise the sense in which the construction is *intrinsic*: once the simplicial Gram data of Section 2 is fixed, the operators require no ongoing reference to a Cartesian embedding.

4. **Closed-form rotation by exponentiation (Sections 5–6).** From $K^3 = -K$ we derive the Rodrigues-type closed form
$$R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2,$$
viewed as a $4\times 4$ orthogonal matrix on the overcomplete coordinate space $\mathbb{R}^4$. As a gauge-compatible extension, $R$ fixes the gauge vector $\mathbf{1} = (1,1,1,1)^\top$ — equivalently, its rows and columns each sum to unity — and preserves the zero-sum hyperplane. *Restricted* to that hyperplane, $R$ is the genuine rotation about the axis $u$ by angle $\theta$ in $\mathrm{SO}(3)$; the full $4\times 4$ matrix is its canonical lift to the stabilizer subgroup $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$. We establish $R^\top R = I$ and $\det R = +1$.

5. **9-multiplication kernel (Section 7).** For $N = 4$, we show that applying $R$ to a zero-sum input admits two independent reductions — one using zero-sum output, one using zero-sum input — that together reduce the per-point apply cost from 16 multiplications to 9. This matches the performance of the quaternion-to-matrix pathway without invoking the $S^3$ double cover.

6. **Uniqueness of $N = 4$ within the simplicial framework (Section 8).** *Within the simplicial wedge–Hodge framework developed here*, we identify $N = 4$ as the unique case that yields a *binary* cross product and admits closed-form exponentiation via $K^3 = -K$; the claim is not a uniqueness theorem across all conceivable simplicial binary operations. This is the simplicial-coordinate reflection of two classical facts: the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$, and Eckmann's theorem, which classifies the real inner-product space dimensions $n$ admitting a bilinear cross product satisfying $\|a \times b\|^2 = \|a\|^2 \|b\|^2 - \langle a, b\rangle^2$ as exactly $n \in \{0, 1, 3, 7\}$ [Eckmann, Massey]; our $N = 4$ case is the simplicial realization of the $n = 3$ branch. The $n = 7$ realization — the octonion cross product on $\mathbb{R}^7$ — is binary but arises from the non-associative octonion algebra rather than from the simplicial wedge–Hodge construction of §3.4, and therefore lies outside the framework developed here. For $N \geq 5$, the analogous construction proceeds via Hodge duals of wedge products of arity $N - 3$, yielding operators of higher arity rather than binary cross products; we sketch this direction and leave the detailed construction to future work.

### 1.3 Terminological notes and low-$N$ cases

**Relation to exterior calculus.** The phrase *simplicial vector calculus* also appears in the discrete exterior calculus (DEC) tradition of Desbrun, Hirani, Leok, and Marsden [Desbrun-Hirani-Leok-Marsden] and the finite element exterior calculus (FEEC) of Arnold, Falk, and Winther [Arnold-Falk-Winther], where $\wedge$, $\star$, and $d$ are defined directly on simplicial complexes for the discretization of partial differential equations (PDEs). The present work is distinct in scope: we develop only the algebraic layer (inner product, binary cross product, rotation) on the $N$-axis frame of a single simplex and its associated zero-sum hyperplane, not on a complex, which is why differential operators are deferred here (as in §1.1; see also the scope remark in §4). The structural relationship between the present construction and DEC — in particular, whether $\tilde{K}(u)$ admits a description as a discrete exterior derivative applied to $u$ viewed as a 0-cochain on the tetrahedron's 1-skeleton (possibly combined with an edge-to-vertex contraction) — is left to future work. FEEC on unstructured tetrahedral meshes [Arnold-Falk-Winther] provides a natural application context; the intrinsic operators developed here could in principle supply pointwise algebraic operations on tetrahedral elements without reference to a global Cartesian frame.

Throughout this paper we use *simplicial coordinates* for the general $N$-frame family, *Quadray coordinates* for the specific $N = 4$ case, and *zero-sum hyperplane* for the canonical gauge. The descriptor *intrinsic* is used in the precise sense recorded in §1.2 item 3: once the simplicial Gram data is fixed, the operators require no ongoing reference to an ambient Cartesian frame. Section 4 and the Conclusion additionally describe the resulting calculus as an *autonomous presentation* of the algebraic layer of 3D Euclidean vector calculus: *autonomous* in the sense that, once the simplicial Gram data of §2 is fixed, the construction proceeds without recourse to a Cartesian reference frame; *presentation* rather than "theory" because it is isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5. We use "frame" in two senses that should not be conflated: the *simplicial frame* $\{\mathbf{v}_i\}$ of §2.1 (a unit-norm tight frame in the sense of Christensen [Christensen]) and the *Cartesian reference frame* of classical mechanics; context and modifiers disambiguate.

**Rodrigues formula.** We use the unmarked phrase *Rodrigues formula* for the closed-form simplicial exponential
$$R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$$
derived in Section 5, written in simplicial coordinates. Under the hyperplane isometry it corresponds to the classical $3 \times 3$ Rodrigues rotation formula in Cartesian coordinates, but we distinguish the two by coordinate system: the present formula is an identity among $4 \times 4$ gauge-compatible matrices.

**Low-$N$ cases.** The simplicial coordinate system is perfectly well-defined for every $N \geq 1$; what varies with $N$ is the dimension of the zero-sum hyperplane and hence the algebraic structures it can carry. Since the paper foregrounds the exceptional status of $N = 4$, we record what happens at smaller $N$. For $N = 1$ the zero-sum hyperplane is $\{0\}$; for $N = 2$ it is one-dimensional, so no nontrivial antisymmetric bilinear form exists on it; for $N = 3$ it is two-dimensional, where rotations exist (parameterized by a single angle) but no *binary* cross product does — a bilinear antisymmetric map from a two-dimensional space to itself vanishes identically, by dimension count on $\Lambda^2 \mathbb{R}^2$. The first value of $N$ at which a binary cross product appears — and, as Section 8 shows, the only value at which the present simplicial construction delivers one — is $N = 4$.

---

## 2. Simplicial Coordinates: Setup

This section fixes the algebraic objects on which the rest of the paper operates: the $N$-vector overcomplete family of §2.1, the one-dimensional gauge direction it carries, the zero-sum hyperplane that serves as a canonical section across gauge classes, and the simplicial Gram matrix that induces the inner product. Throughout we take $N \geq 3$, since for $N = 1, 2$ the zero-sum hyperplane is at most one-dimensional and carries no nontrivial antisymmetric bilinear form (see §1.3).

### 2.1 The simplicial frame

Let $N \geq 3$ be an integer and let $\mathbf{v}_1, \ldots, \mathbf{v}_N$ be unit vectors in $\mathbb{R}^{N-1}$ pointing from the origin to the vertices of a regular $(N-1)$-simplex centered at the origin. We call the family $\{\mathbf{v}_i\}_{i=1}^N$ the *simplicial frame* and its elements *frame vectors*. We deliberately avoid the traditional Quadray term *basis* for this family: the $N$ vectors span the $(N-1)$-dimensional space $\mathbb{R}^{N-1}$ and are therefore linearly dependent — as the balancing identity below makes explicit — so they do not form a basis in the standard linear-algebra sense. The correct term is *frame*: a spanning set with deliberate, structurally useful redundancy; see Christensen [Christensen, Ch.~1] for the modern theory and Duffin and Schaeffer [Duffin-Schaeffer] for the original introduction of the notion. Where a genuine (linearly independent) basis of $\mathbb{R}^{N-1}$ or of the zero-sum hyperplane $H$ is needed, we say so explicitly (see §7.3). The pairwise inner products satisfy

$$\mathbf{v}_i \cdot \mathbf{v}_j = \begin{cases} 1 & \text{if } i = j, \\ -\tfrac{1}{N-1} & \text{if } i \neq j, \end{cases}$$

and the frame vectors satisfy the balancing identity

$$\sum_{i=1}^{N} \mathbf{v}_i = \mathbf{0}.$$

A *simplicial coordinate* of a point $\mathbf{p} \in \mathbb{R}^{N-1}$ is a tuple $(c_1, \ldots, c_N) \in \mathbb{R}^N$ such that

$$\mathbf{p} = \sum_{i=1}^N c_i \mathbf{v}_i.$$

Because the frame has $N$ vectors in an $(N-1)$-dimensional space, the map from coordinates to points is not injective: the balancing identity implies that adding any scalar multiple of $(1, 1, \ldots, 1)$ to a coordinate tuple yields the same point.

**Proposition 2.0 (Equiangular unit-norm tight frame; simplex ETF).** *The family $\{\mathbf{v}_i\}_{i=1}^N$ is an equiangular unit-norm tight frame (ETF) for $\mathbb{R}^{N-1}$ with frame bound $N/(N-1)$: for every $\mathbf{x} \in \mathbb{R}^{N-1}$,*

$$\sum_{i=1}^N \langle \mathbf{x}, \mathbf{v}_i\rangle^2 = \frac{N}{N-1}\,\|\mathbf{x}\|^2.$$

*Proof.* Consider the *analysis operator* $T: \mathbb{R}^{N-1} \to \mathbb{R}^N$, $T\mathbf{x} := (\langle \mathbf{x}, \mathbf{v}_i\rangle)_{i=1}^N$, and its adjoint the *synthesis operator* $T^\top: \mathbb{R}^N \to \mathbb{R}^{N-1}$, $T^\top \mathbf{c} = \sum_i c_i \mathbf{v}_i$; then $\sum_i \langle \mathbf{x}, \mathbf{v}_i\rangle^2 = \mathbf{x}^\top S \mathbf{x}$ where $S := T^\top T = \sum_i \mathbf{v}_i \mathbf{v}_i^\top \in \mathbb{R}^{(N-1)\times(N-1)}$ is the *frame operator*. By the symmetry group of the regular simplex (which acts irreducibly on $\mathbb{R}^{N-1}$), $S$ is invariant under this action and hence a scalar multiple of the identity; taking traces, $\mathrm{tr}(S) = \sum_i \|\mathbf{v}_i\|^2 = N$, so $S = \tfrac{N}{N-1}\,I_{N-1}$. Equiangularity ($\langle \mathbf{v}_i, \mathbf{v}_j\rangle = -\tfrac{1}{N-1}$ for all $i \neq j$) is already recorded. $\square$

The frame $\{\mathbf{v}_i\}_{i=1}^N$ is the *regular simplex ETF* — a canonical example in frame theory and arguably the simplest nontrivial ETF in each dimension [Christensen, Ch.~1]. The frame bound $N/(N-1)$ is the same constant that appears in the zero-sum quadratic form of Proposition 2.1 — a reflection of the fact that the simplicial inner product on $H$ is, up to sign conventions, the synthesis operator $T^\top$ of this tight frame composed with its analysis adjoint.

### 2.2 The gauge direction and equivalence classes

The overcompleteness of §2.1 is a structural feature, not a defect: the map from coordinate tuples to geometric points has a one-dimensional kernel, and the natural first step is to identify that kernel, name its generator, and describe the resulting equivalence of coordinate tuples. Factoring this redundancy out is a prerequisite for every linear-algebraic operation — inner product, cross product, rotation — to be well-defined on geometric points rather than on raw tuples.

Define the *gauge direction*

$$\mathbf{1} := (1, 1, \ldots, 1) \in \mathbb{R}^N$$

and the *gauge equivalence relation*: two coordinate tuples $c, c' \in \mathbb{R}^N$ are equivalent, written $c \sim c'$, if and only if $c' = c + k\mathbf{1}$ for some $k \in \mathbb{R}$. The gauge equivalence classes are lines in $\mathbb{R}^N$ parallel to $\mathbf{1}$, and each class corresponds uniquely to a point of $\mathbb{R}^{N-1}$.

We call this direction the *gauge direction* because it represents a one-dimensional redundancy in the coordinate description that does not alter the physical (geometric) content, which is precisely the definition of a gauge degree of freedom.

#### 2.2.1 Structural parallels across disciplines

The configuration just defined — an overcomplete coordinate description with a one-dimensional redundancy and a distinguished codimension-one subspace on which the physically meaningful dynamics lives — recurs in several apparently distinct settings, and the parallels are worth recording before we specialize. Consistent with the position taken in §1.2 item 1, we present these connections as structural analogies offered for interpretive motivation, not as a formal equivalence of categories: no functorial identification is constructed here between simplicial gauge classes in $\mathbb{R}^N / \langle \mathbf{1} \rangle$, stoichiometric compatibility classes in chemical reaction network theory (CRNT), and the affine simplex in information geometry.

In CRNT [Müller-Regensburger], conservation laws confine dynamical trajectories to *stoichiometric compatibility classes* — affine subspaces on which the totals of conserved species are fixed. Under the simplicial coordinate description of species concentrations, these compatibility classes are structurally analogous to the gauge equivalence classes of §2.2, with the reaction dynamics taking place *on* the classes. The analogy with CRNT is offered as interpretation, not as a formal identification of the two theories.

In information geometry [Amari, Chentsov], the probability simplex $\{\mathbf{p} : p_i \geq 0,\ \sum p_i = 1\}$ is the affine translate of the zero-sum hyperplane $H$ of §2.3 by $\tfrac{1}{N}\mathbf{1}$; the constraint $\sum p_i = 1$ plays the role of a gauge-fixing condition. Again, the parallel is structural rather than formal. We return to both threads in §8.

### 2.3 The zero-sum hyperplane (canonical gauge)

The gauge equivalence of §2.2 replaces each geometric point by a one-parameter family of coordinate tuples, which is unwieldy for computation. To recover a concrete $(N-1)$-dimensional arena on which linear algebra can proceed, we pick a distinguished representative from each equivalence class — equivalently, a linear section of the projection $\mathbb{R}^N \to \mathbb{R}^N / \langle \mathbf{1} \rangle$. The natural choice is the unique coordinate tuple whose components sum to zero, both because it is canonical (determined by the symmetric condition $\sum c_i = 0$) and because, as we will see in §2.4, it is the orthogonal complement of the gauge direction under both the standard and simplicial inner products.

Among all coordinate representatives of a given point, the *zero-sum representative* is the unique tuple satisfying $\sum c_i = 0$. Uniqueness is immediate: if $c' = c + k\mathbf{1}$ is also zero-sum, then $\sum c'_i = \sum c_i + kN = 0$ forces $k = -\tfrac{1}{N}\sum c_i$, so the scalar shift — and hence the representative — is determined. Concretely, the zero-sum representative is obtained from any representative $c$ by subtracting the mean $\bar{c} = \tfrac{1}{N}\sum c_i$ from each coordinate:

$$c^{\mathrm{zs}}_i := c_i - \bar{c}.$$

The set

$$H := \left\{ c \in \mathbb{R}^N : \sum_{i=1}^N c_i = 0 \right\}$$

is the *zero-sum hyperplane*, an $(N-1)$-dimensional linear subspace of $\mathbb{R}^N$ perpendicular to $\mathbf{1}$ under the standard Euclidean inner product. The map $c \mapsto c^{\mathrm{zs}}$ identifies $H$ with a canonical linear section of the quotient $\mathbb{R}^N / \langle \mathbf{1}\rangle$, so we may (and will) use $H$ interchangeably with the quotient wherever no confusion results. $H$ inherits the ambient Euclidean inner product from $\mathbb{R}^N$ and is, by the correspondence $c \mapsto \sum c_i \mathbf{v}_i$, isometric to $\mathbb{R}^{N-1}$ up to a scale factor we compute shortly.

Operationally, the zero-sum hyperplane is the canonical gauge for linear-algebraic operations on simplicial coordinates. The three operators of this paper interact with $H$ in complementary ways, which we distinguish carefully: the inner product of §2.4 is *gauge-invariant as a scalar* (its value is unchanged under $c \mapsto c + k\mathbf{1}$ in either argument), while the vector-valued operators developed later — the cross product $K(u)$ of §3 and the rotation $R(u, \theta) = \exp(\theta K(u))$ of §5 — *preserve $H$ as a subspace* and act on it by endomorphisms, annihilating (respectively, fixing) the gauge direction. The 9-multiplication apply kernel of §7 exploits this closure property directly. Working in $H$ thereby reduces the overcomplete $N$-dimensional description to a faithful $(N-1)$-dimensional one without breaking the permutation symmetry of the frame.

### 2.4 Inner product and the Gram matrix

Given two coordinate tuples $a, b \in \mathbb{R}^N$, the Euclidean inner product of the corresponding points in $\mathbb{R}^{N-1}$ is

$$\langle a, b \rangle := \left( \sum_i a_i \mathbf{v}_i \right) \cdot \left( \sum_j b_j \mathbf{v}_j \right) = \sum_{i,j} a_i b_j (\mathbf{v}_i \cdot \mathbf{v}_j) = a^\top G\, b,$$

where the *simplicial Gram matrix* $G$ is defined element-wise by the pairwise inner products of the frame vectors (§2.1):

$$G_{ij} := \mathbf{v}_i \cdot \mathbf{v}_j = \begin{cases} 1 & \text{if } i = j, \\ -\tfrac{1}{N-1} & \text{if } i \neq j. \end{cases}$$

In closed matrix form this reads

$$G = I - \frac{1}{N-1}(J - I) = \frac{N}{N-1} I - \frac{1}{N-1} J,$$

where $I$ is the $N \times N$ identity matrix and $J$ is the $N \times N$ all-ones matrix.

The gauge direction is a null direction of $G$ in the following sense:

$$G\mathbf{1} = \left(\frac{N}{N-1} I - \frac{1}{N-1} J\right)\mathbf{1} = \frac{N}{N-1}\mathbf{1} - \frac{N}{N-1}\mathbf{1} = \mathbf{0}.$$

Thus the inner product $\langle a, b \rangle$ is invariant under gauge shifts of either argument: since $G$ is symmetric, $\mathbf{1}^\top G = (G\mathbf{1})^\top = \mathbf{0}^\top$ as well, so $\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = \langle a, b\rangle$ for all $k, m \in \mathbb{R}$, confirming that the inner product descends to the quotient space $\mathbb{R}^N / \mathbb{R}\mathbf{1}$ and agrees with the Euclidean inner product on $\mathbb{R}^{N-1}$.

**Proposition 2.1 (Zero-sum quadratic form).** *For $c \in H$ (i.e.\ $\sum c_i = 0$),*

$$\langle c, c \rangle = \frac{N}{N-1} \sum_{i=1}^N c_i^2.$$

The proof, a short algebraic computation using the zero-sum identity $\sum_{i < j} c_i c_j = -\tfrac{1}{2}\sum_i c_i^2$, appears in Appendix A. In the $N = 4$ case (Quadray), the scaling factor is $\tfrac{4}{3}$; in $N = 3$, it is $\tfrac{3}{2}$.

### 2.5 Conventions for $N = 4$

For $N = 4$ we adopt a standard Quadray frame convention, with vertices at

$$\mathbf{v}_1 = \tfrac{1}{\sqrt{3}}(-1, -1, +1), \quad \mathbf{v}_2 = \tfrac{1}{\sqrt{3}}(+1, +1, +1),$$
$$\mathbf{v}_3 = \tfrac{1}{\sqrt{3}}(+1, -1, -1), \quad \mathbf{v}_4 = \tfrac{1}{\sqrt{3}}(-1, +1, -1),$$

retaining the generic indexed notation $(c_1, c_2, c_3, c_4)$ of §2.1 for the simplicial coordinates. The ambient $\mathbb{R}^3$ is taken with its standard right-handed orientation, so that the ordered triple $(\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3)$ is positively oriented; the chirality conventions used in §3 (for the cross product) and §5 (for rotation) are defined with respect to this fixed orientation, and the labelling $(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4)$ above is chosen so that the simplicial rotation agrees with standard right-handed Cartesian rotation under the *hyperplane isometry* $V\colon H \to \mathbb{R}^3$ defined by $V(c) := \sum_{i=1}^4 c_i \mathbf{v}_i$ (so that $V$ sends the simplicial coordinate tuple $c \in H$ to the corresponding Cartesian point in the ambient $\mathbb{R}^3$); the structural characterization of $V$ as an orientation- and metric-preserving realization of $(H, \langle\cdot,\cdot\rangle)$ as Euclidean $\mathbb{R}^3$ via the Hodge construction is taken up in §3.4. Concretely, $V K(u) V^{-1} = [Vu]_\times$ for every $u \in H$, where $[\cdot]_\times$ is the standard Cartesian cross-product matrix. Pairwise dot products satisfy $\mathbf{v}_i \cdot \mathbf{v}_j = -\tfrac{1}{3}$ for $i \neq j$, corresponding to the tetrahedral central angle $\arccos(-\tfrac{1}{3}) \approx 109.47^\circ$. The zero-sum hyperplane in this case is three-dimensional, isometric to ordinary $\mathbb{R}^3$ up to the scaling factor $\tfrac{4}{3}$.

---

## 3. The Intrinsic Cross Product

We now construct the central operator of this paper: a skew-symmetric bilinear form on the zero-sum hyperplane of the $N = 4$ simplicial system that serves as an intrinsic cross product. We present the construction in two stages: first an ansatz motivated by the properties the operator must satisfy, then a Lie-algebraic justification that establishes the closure identity $K^3 = -K$ and fixes the scaling constant.

The operation itself — a binary skew-symmetric product on a three-dimensional oriented inner-product space — is classical, and in the standard Cartesian setting it is equivalently realized as $\star(u \wedge \cdot)$, as $\mathrm{ad}_u$ on $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$, or as the bivector-to-vector map in the Clifford / Geometric Algebra of $\mathbb{R}^3$ [Hestenes]. Our contribution in this section is therefore not the geometric operation but its *simplicial realization*: an explicit $4 \times 4$ entrywise matrix $K(u)$ acting on the overcomplete coordinate $\mathbb{R}^4$, whose zero-sum and gauge-annihilating structure is built into the row and column sums, and whose normalization constant $1/\sqrt{3}$ is forced by the simplicial metric $G = \tfrac{4}{3} I - \tfrac{1}{3} J$ of §2.4. Throughout this section we specialize to $N = 4$; the analogous construction for general $N$ is discussed in §8.

### 3.1 Geometric motivation

Let $u \in H$ be a zero-sum unit axis, meaning $\sum u_i = 0$ and $\langle u, u \rangle = 1$ under the simplicial inner product, i.e.\ $\tfrac{4}{3}\sum u_i^2 = 1$. Let $P \in H$ be an arbitrary zero-sum point.

In ordinary 3D Cartesian geometry, the cross product $\hat{n} \times \vec{R}$ of a unit axis $\hat{n}$ with a vector $\vec{R}$ produces a vector perpendicular to both, of magnitude $|\vec{R}| \sin\theta$ where $\theta$ is the angle between them. Applying the cross product twice yields the classical identity

$$\hat{n} \times (\hat{n} \times \vec{R}) = -\vec{R}_\perp,$$

where $\vec{R}_\perp$ is the component of $\vec{R}$ perpendicular to $\hat{n}$. We seek an operator $K = K(u)$ acting on $H$ whose image lies in $u^\perp \cap H$ and which satisfies the double-application identity $K(u)^2 P = -P_\perp$, where $P_\perp$ denotes the simplicial-orthogonal projection of $P \in H$ onto $u^\perp \cap H$.

Rather than derive $K(u)$ from first principles, we write down the simplest matrix compatible with the structural requirements — linearity in $u$, skew-symmetry with respect to the simplicial inner product, annihilation of the gauge direction $\mathbf{1}$, closure on the zero-sum hyperplane $H$, and (eventually) a cubic closure of the form $K^3 \propto K$ — and then verify each property in turn. Labelling rows and columns by the indices $1, 2, 3, 4$, consider

$$\tilde{K}(u) = \begin{pmatrix}
0 & u_3 - u_4 & u_4 - u_2 & u_2 - u_3 \\
u_4 - u_3 & 0 & u_1 - u_4 & u_3 - u_1 \\
u_2 - u_4 & u_4 - u_1 & 0 & u_1 - u_2 \\
u_3 - u_2 & u_1 - u_3 & u_2 - u_1 & 0
\end{pmatrix}.$$

The entries are the six cyclic differences $u_i - u_j$, placed so that three of the five desired properties are immediate:

- $\tilde{K}(u)$ is linear in $u$ and elementwise skew-symmetric: $\tilde{K}(u)^\top = -\tilde{K}(u)$.
- Each row sums to zero, so $\tilde{K}(u) \mathbf{1} = \mathbf{0}$: the operator annihilates the gauge direction.
- Each column sums to zero (by the elementwise skew-symmetry), so $\sum_i (\tilde{K}(u) P)_i = \sum_j \bigl(\sum_i \tilde{K}(u)_{ij}\bigr) P_j = 0$ for every $P$, meaning $\tilde{K}(u)$ preserves the zero-sum hyperplane $H$.

Thus $\tilde{K}(u)$ is gauge-annihilating and hyperplane-closing; what remains is to verify the cubic closure and fix the *scale*. A spectral/trace computation (Appendix B) shows that, for a zero-sum unit axis $u$, the rank of $\tilde{K}(u)$ is two and its spectrum is $\{0, 0, +i\sqrt{3}, -i\sqrt{3}\}$, which yields

$$\tilde{K}(u)^3 = -c^2\, \tilde{K}(u), \qquad c^2 = 3.$$

To recover the clean classical identity $K^3 = -K$ — the identity satisfied by cross products with unit axes in 3D — we rescale by $1/\sqrt{c^2}$:

$$K(u) := \frac{1}{\sqrt{c^2}}\, \tilde{K}(u) = \frac{1}{\sqrt{3}}\, \tilde{K}(u).$$

The prefactor $1/\sqrt{3}$ is therefore not chosen aesthetically; it is forced by the simplicial metric. Geometrically, the cyclic-difference entries of $\tilde{K}$ measure differences in the raw (ambient $\mathbb{R}^4$) coordinates, whereas the squared length of a zero-sum vector on $H$ is inflated by the factor $4/3$ of §2.5 (so a vector of raw-coordinate norm $\sqrt{3}/2$ has simplicial norm $1$). The $1/\sqrt{3}$ is precisely what re-expresses $\tilde{K}$ in units compatible with the simplicial inner product, thereby aligning the algebraic identity $K^3 = -K$ with the geometric identity "double cross product equals minus the perpendicular component."

### 3.2 Definition

**Definition 3.1 (Intrinsic cross product).** *For $N = 4$ and a zero-sum unit axis $u = (u_1, u_2, u_3, u_4)$ (i.e.\ $\sum u_i = 0$ and $\tfrac{4}{3}\sum u_i^2 = 1$), define*

$$K(u) := \frac{1}{\sqrt{3}}\begin{pmatrix}
0 & u_3 - u_4 & u_4 - u_2 & u_2 - u_3 \\
u_4 - u_3 & 0 & u_1 - u_4 & u_3 - u_1 \\
u_2 - u_4 & u_4 - u_1 & 0 & u_1 - u_2 \\
u_3 - u_2 & u_1 - u_3 & u_2 - u_1 & 0
\end{pmatrix}.$$

The operator $K(u): \mathbb{R}^4 \to \mathbb{R}^4$ is bilinear in $(u, P)$, skew-symmetric, gauge-annihilating, and closes on the zero-sum hyperplane.

**Remark 3.2 (Formal linear extension of $K$).** The entrywise formula of Definition 3.1 depends linearly on the coordinates $(u_1, u_2, u_3, u_4)$ of $u$, so the same formula defines a matrix $K(u) \in \mathbb{R}^{4\times 4}$ for *every* $u \in \mathbb{R}^4$, not only for zero-sum unit axes. This formal extension is linear in $u$:

$$K(\alpha u + \beta v) = \alpha\, K(u) + \beta\, K(v), \qquad \alpha, \beta \in \mathbb{R}, \; u, v \in \mathbb{R}^4.$$

As an immediate consequence, $K(\mathbf{1}) = 0$: when $u = (1,1,1,1)$, every off-diagonal entry of Definition 3.1 is a difference of two equal coordinates and hence vanishes, so the entire matrix is zero. This is the identity invoked in Theorem 4.1(2) below.

Two distinct properties of $K(u)$ are worth distinguishing, because they have different scopes:

1. *Simplicial skew-symmetry holds for every $u \in \mathbb{R}^4$.* The matrix $K(u)$ has identically vanishing row and column sums (the row sums by inspection of the cyclic-difference pattern, the column sums by elementwise skew-symmetry). Writing the simplicial Gram matrix of §2.4 as $G = \tfrac{4}{3}I - \tfrac{1}{3}J$ where $J$ is the all-ones matrix, both $JK(u) = 0$ (row sums zero) and $K(u)J = 0$ (column sums zero), so $JK(u) = K(u)J$, hence $GK(u) = \tfrac{4}{3}K(u) = K(u)G$. Combined with $K(u)^\top = -K(u)$, this gives $(GK(u))^\top = -GK(u)$: the operator is simplicially skew-adjoint for every $u \in \mathbb{R}^4$, not only for zero-sum unit axes.
2. *The cubic identity and unit-axis geometry require the restriction.* The identity $K(u)^3 = -K(u)$ (Theorem 3.3) and the double-application statement $K(u)^2 P = -P_\perp$ (Corollary 3.4) rely on the unit-axis normalization $\tfrac{4}{3}\sum u_i^2 = 1$ and on $\sum u_i = 0$.

Thus the cross-product object proper is the bilinear form $(u, P) \mapsto K(u) P$ on $H \times H \to H$; the formal linear extension to all $u \in \mathbb{R}^4$ is a notational convenience that allows axis arguments such as $u = \mathbf{1}$ to be written down before restricting.

### 3.3 Core identity

**Theorem 3.3 (Closure identity for $N = 4$).** *For any zero-sum unit axis $u$, the operator $K(u)$ satisfies*

$$K(u)^3 = -K(u).$$

The proof is a spectral/trace computation, given in Appendix B. The key facts: $K(u)$ is a $4 \times 4$ skew-symmetric matrix of rank 2, with spectrum $\{0, 0, +i, -i\}$ when $u$ is a zero-sum unit axis. The minimal polynomial of a rank-2 skew matrix with eigenvalues $\pm ci$ is $x(x^2 + c^2)$, so $K^3 = -c^2 K$; the normalization of $K$ is precisely what sets $c = 1$.

**Corollary 3.4 (Geometric double-application identity).** *For any $P \in H$,*

$$K(u)^2\, P = -P_\perp,$$

*where $P_\perp$ is the orthogonal projection (under the simplicial inner product) of $P$ onto the subspace of $H$ perpendicular to $u$.*

*Proof.* Write $H_u := u^\perp \cap H$ for the simplicial-orthogonal complement of $u$ inside $H$. We first show $\operatorname{im} K(u)|_H = H_u$. By Remark 3.2(1), $G K(u)$ is antisymmetric, so $\langle K(u) v, u \rangle = v^\top K(u)^\top G u = -v^\top G K(u) u = 0$ for every $v$ (using $K(u)u = 0$, proved in Appendix B Step 1). Also $K(u) v \in H$ by Corollary 3.5. Hence $\operatorname{im} K(u)|_H \subseteq H_u$. Both spaces are two-dimensional (the former because $K(u)$ has rank 2 on $H$, since $\ker K(u) \cap H = \mathbb{R} u$; the latter because $\dim H = 3$ and $u \neq 0$), so they coincide. Now for any $P \in H$, write $P = \alpha u + P_\perp$ with $P_\perp \in H_u$. Since $K(u) u = 0$, $K(u) P = K(u) P_\perp$, and because $P_\perp \in \operatorname{im} K(u)|_H$ there exists $w \in H$ with $K(u) w = P_\perp$. Theorem 3.3 applied to $w$ gives $K(u)^3 w = -K(u) w$, i.e.\ $K(u)^2 P_\perp = -P_\perp$. Combined with $K(u)^2 (\alpha u) = 0$, this yields $K(u)^2 P = -P_\perp$. $\square$

**Corollary 3.5 (Zero-sum preservation).** *$K(u)$ maps $H$ to itself. That is, if $P \in H$ then $K(u) P \in H$.*

*Proof of 3.5.* Each column of $K(u)$ sums to zero (by elementwise skew-symmetry of the $\tilde{K}$ construction together with the fact that each row sums to zero). Therefore, for any $P \in \mathbb{R}^4$, $\sum_i (K(u)P)_i = \sum_j \bigl(\sum_i K(u)_{ij}\bigr) P_j = 0$. $\square$

### 3.4 Relation to wedge and Hodge dual

The operator $K(u)$ can be understood as the Hodge dual of the wedge product with $u$. On an oriented inner-product space $V$ of dimension $d$, the Hodge star $\star: \Lambda^k V \to \Lambda^{d-k} V$ is characterized by

$$\alpha \wedge \star \beta = \langle \alpha, \beta \rangle\, \omega$$

for $\alpha, \beta \in \Lambda^k V$, where $\omega$ is the unit volume form associated with the inner product and the chosen orientation; see Flanders [Flanders, Ch.~2] or Spivak [Spivak, Ch.~7] for the standard development.

To apply this to our setting, note that the zero-sum hyperplane $H \subset \mathbb{R}^4$ carries the restriction of the simplicial inner product of §2.4, under which Proposition 2.1 gives $\langle c, c \rangle = \tfrac{4}{3}\sum c_i^2$. Equipped with this inner product and with the orientation on $H$ pulled back from the standard right-handed orientation of the ambient $\mathbb{R}^3$ via the hyperplane isometry $V$ of §2.5, $(H, \langle\cdot,\cdot\rangle)$ is a three-dimensional oriented inner-product space, and therefore non-canonically *isometric* (not merely isomorphic as a vector space) to ordinary $\mathbb{R}^3$. Under any such isometry, the Hodge-dual operator $\star(u \wedge \cdot): H \to H$ is skew-symmetric with respect to $\langle\cdot,\cdot\rangle$ and acts as cross product with $u$. Our $K(u)$ is the matrix representation of this operator in the overcomplete coordinates $(c_1, c_2, c_3, c_4) \in \mathbb{R}^4$ of §2.1. The $4/3$ scaling of the simplicial inner product is absorbed into the volume form $\omega$ and into the factor $1/\sqrt{3}$ of Definition 3.1, which is why the same identity $K^3 = -K$ that holds for the Cartesian cross product holds here without further adjustment.

The Hodge-dual viewpoint also clarifies why $N = 4$ is special. For $V$ of dimension $d = 3$, the Hodge dual converts a 2-form $u \wedge v$ into a 1-vector, so the cross product is binary. For $V$ of dimension $d \geq 4$ (equivalently, $N \geq 5$ in the simplicial count), the analogous construction converts a $(d-1)$-form into a 1-vector, so the operation takes $d - 1 = N - 3$ vector inputs rather than one; this is the standard obstruction to extending the binary cross product to higher dimensions [Massey]. The closed-form Rodrigues exponentiation depends on $K^3 = -K$, which is a feature of the binary case only. We return to this point in §8.

---

## 4. Gauge-Compatibility and Descent to the Zero-Sum Quotient

The three operations constructed or cited so far — the inner product $\langle \cdot, \cdot \rangle$, the cross product $K(u)\cdot$, and the exponential map (constructed in §5) — together form a gauge-compatible algebraic system on the zero-sum hyperplane. We consolidate their invariance properties into a single structural statement, distinguishing the scalar (inner product) and vector-valued (cross product, rotation) cases, and record the descent of each to the quotient $\mathbb{R}^N / \langle \mathbf{1}\rangle \cong \mathbb{R}^{N-1}$. We emphasize the scope of the claim: we address the algebraic layer of vector calculus (inner product, binary cross product, rotation); differential operators ($\nabla$, $\mathrm{div}$, $\mathrm{curl}$) are not developed here and remain outside the present scope.

**Theorem 4.1 (Joint gauge-compatibility and descent).** *For $N = 4$, the simplicial inner product, the intrinsic cross product $K$, and the matrix exponential $\exp(\theta K)$ are jointly compatible with the gauge action $c \mapsto c + k\mathbf{1}$ in the following precise sense:*

1. *(Scalar invariance.) The inner product is gauge-invariant in both arguments: $\langle a + k\mathbf{1},\, b + m\mathbf{1} \rangle = \langle a, b \rangle$ for all $a, b \in \mathbb{R}^N$ and all $k, m \in \mathbb{R}$.*
2. *(Hyperplane closure and gauge annihilation.) For each zero-sum unit axis $u$, the cross product operator $K(u)$ preserves the zero-sum hyperplane $H$ and annihilates the gauge direction: $K(u)\mathbf{1} = \mathbf{0}$ and $K(u)H \subseteq H$. Moreover, under the formal linear extension of $K$ to all of $\mathbb{R}^4$ (Remark 3.2), $K$ is linear in its axis argument and $K(\mathbf{1}) = 0$; consequently $K$ depends only on the axis class, $K(u + k\mathbf{1}) = K(u)$ for every $k \in \mathbb{R}$.*
3. *(Hyperplane closure and gauge fixing.) For each zero-sum unit axis $u$ and angle $\theta$, the rotation $R(u,\theta) := \exp(\theta K(u))$ preserves $H$ and fixes the gauge direction: $R(u,\theta)\mathbf{1} = \mathbf{1}$ and $R(u,\theta)H \subseteq H$. Axis-class independence follows from (2): $R(u + k\mathbf{1},\theta) = R(u,\theta)$ for every $k \in \mathbb{R}$.*

*Consequently the simplicial bilinear form, cross-product operator, and rotation descend to well-defined operations on the quotient $\mathbb{R}^N / \langle \mathbf{1}\rangle \cong \mathbb{R}^{N-1}$, canonically realized by the zero-sum hyperplane $H$ of §2.3; they yield the simplicial inner product, binary cross product, and rotation acting intrinsically on the $(N-1)$-dimensional geometric content carried by simplicial coordinates. This is the same quotient that plays the organizing role across the structural parallels recorded in §2.2.1 (information geometry and chemical reaction network theory).*

*Proof sketch.* (1) By §2.4, $G\mathbf{1} = \mathbf{0}$; since $G$ is symmetric, $\mathbf{1}^\top G = (G\mathbf{1})^\top = \mathbf{0}^\top$ as well, so
$$\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = a^\top G b + k\,\mathbf{1}^\top G b + m\, a^\top G\mathbf{1} + km\,\mathbf{1}^\top G\mathbf{1} = a^\top G b = \langle a, b\rangle.$$
For (2): $K(u)\mathbf{1} = \mathbf{0}$ because each row of the matrix in Definition 3.1 sums to zero, and $K(u)H \subseteq H$ by Corollary 3.5 (each column sums to zero); linearity in the axis is immediate from the entrywise formula of Remark 3.2, and $K(\mathbf{1}) = 0$ (also Remark 3.2) then yields $K(u + k\mathbf{1}) = K(u) + k\,K(\mathbf{1}) = K(u)$, the axis-class independence invoked in (3). For (3): $R(u,\theta) = \exp(\theta K(u))$ inherits hyperplane closure from (2) term-by-term, since each partial sum $\sum_{j=0}^n \tfrac{(\theta K(u))^j}{j!}\, P$ lies in $H$ for $P \in H$, and $H$ is a closed finite-dimensional subspace of $\mathbb{R}^4$, so the limit remains in $H$. Likewise $R(u,\theta)\mathbf{1} = \mathbf{1}$ because $K(u)\mathbf{1} = \mathbf{0}$ forces all higher series terms to vanish on $\mathbf{1}$. The descent-relevant isometry is the simplicial orthogonality $R^\top G R = G$ (equivalently $\langle RP, RQ\rangle = \langle P, Q\rangle$), which follows from the commutation $GK(u) = K(u)G$ (Remark 3.2(1)): since $G$ commutes with $K$ it commutes with every power of $K$ and hence, by continuity of matrix multiplication, with $\exp(\theta K) = R$; combined with $R^\top = \exp(\theta K)^\top = \exp(-\theta K)$ (using $K^\top = -K$, Definition 3.1), this gives $R^\top G R = \exp(-\theta K)\, G\, \exp(\theta K) = G\, \exp(-\theta K)\, \exp(\theta K) = G$; the ambient Euclidean lift $R^\top R = I$ and the orientation $\det R = +1$ are established in §§5–6. Descent to the quotient now follows from (1)–(3) together with the axis-class independence recorded in (2)–(3). $\square$

**Remark 4.2 (Structural interpretation).** The three operations — metric, cross product, rotation — are the core algebraic ingredients of classical rigid-body mechanics on $\mathbb{R}^3$ [Arnold, Marsden-Ratiu]: the metric supplies kinetic energy, the cross product supplies angular momentum, and rotation supplies the group of frame changes. Theorem 4.1 shows that, for $N = 4$, these ingredients descend intact to the simplicial zero-sum quotient. This is the algebraic content of §1.2 item 3: once the simplicial Gram data of §2 is fixed, the formulas for these operations require no ongoing reference to a Cartesian embedding. The simplicial (Quadray) description of 3D Euclidean space thereby supports an autonomous *presentation* of this algebraic layer of vector calculus, in the sense made precise in §9: isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5, but formulated and computed without passing through a Cartesian frame.

---

## 5. Closed-Form Rotation via the Exponential Map

Section 5 derives the simplicial Rodrigues rotation formula by two equivalent routes. The geometric derivation (§5.1) exploits the parallel/perpendicular splitting of the target vector relative to the axis $u$, reducing the rotation to a planar computation in $u^\perp \cap H$. The Lie-algebraic derivation (§5.2) recognizes $K(u)$ as an element of the Lie algebra $\mathfrak{so}(H, \langle\cdot,\cdot\rangle_s) \cong \mathfrak{so}(3)$ and evaluates its matrix exponential in closed form using the cubic identity $K^3 = -K$ of Theorem 3.3. The two derivations yield the same operator, as observed in §5.3. §5.4 gives a concrete worked example, and §8 takes up the higher-dimensional question.

### 5.1 Geometric derivation

To rotate a point $P \in H$ around a zero-sum unit axis $u$ by angle $\theta$, we decompose $P$ into components parallel and perpendicular to $u$ (under the simplicial inner product $\langle\cdot,\cdot\rangle_s := \langle\cdot,\cdot\rangle$ of §2.4) and rotate the perpendicular component through angle $\theta$ in the oriented plane $u^\perp \cap H$. We take $u \in H$ throughout; this is without loss of generality, since by Theorem 4.1(2) $K(u + k\mathbf{1}) = K(u)$ for every $k \in \mathbb{R}$, so all constructions below depend only on the gauge class of $u$. For brevity we write $K$ for $K(u)$ throughout §5.1.

From Corollary 3.4, $P_\perp = -K^2 P$, and the parallel component follows as $P_\parallel = P - P_\perp = (I + K^2)\, P$. The cross product $K P$ lies in $u^\perp \cap H$: by Corollary 3.5, $KP \in H$; by simplicial skew-adjointness (Remark 3.2(1), equivalently $GK + K^\top G = 0$) together with $Ku = 0$ (Appendix B, Step 1),
$$\langle KP, u\rangle_s = -\langle P, Ku\rangle_s = 0.$$
We claim that, provided $P \notin \mathrm{span}(u)$, the pair $\{P_\perp, KP\}$ is a simplicially orthogonal basis of $u^\perp \cap H$ with $\|P_\perp\|_s = \|KP\|_s$.

*Orthogonality.* Applying simplicial skew-adjointness twice together with $K^3 = -K$ (Theorem 3.3),
$$\langle KP, K^2 P\rangle_s = -\langle P, K^3 P\rangle_s = \langle P, KP\rangle_s = -\langle KP, P\rangle_s,$$
so $\langle KP, K^2 P\rangle_s = 0$, whence $\langle KP, P_\perp\rangle_s = \langle KP, -K^2 P\rangle_s = 0$.

*Equal norms.* Since $P_\parallel = \alpha u$ for some $\alpha \in \mathbb{R}$ and $Ku = 0$, we have $KP = KP_\perp$. Corollary 3.4 gives $K^2|_{u^\perp \cap H} = -I$, so $K$ restricted to $u^\perp \cap H$ is a simplicial isometry of that subspace. Computationally,
$$\|KP\|_s^2 = \langle KP, KP\rangle_s = -\langle P, K^2 P\rangle_s = \langle P, P_\perp\rangle_s = \langle P_\perp, P_\perp\rangle_s = \|P_\perp\|_s^2,$$
where the last step uses $\langle P_\parallel, P_\perp\rangle_s = \alpha\,\langle u, P_\perp\rangle_s = 0$.

*Axial degenerate case.* If $P \in \mathrm{span}(u)$, then $P_\perp = KP = 0$ and the formula below collapses to $P' = P_\parallel = P$, consistent with the geometric expectation that axial vectors are fixed by rotations about $u$. Otherwise $\{P_\perp, KP\}$ is the simplicially orthogonal basis of $u^\perp \cap H$ claimed above.

The rotation of $P_\perp$ by angle $\theta$ in this plane is
$$P_\perp' = \cos\theta\, P_\perp + \sin\theta\, KP = -\cos\theta\, K^2 P + \sin\theta\, KP,$$
with the sign convention that positive $\theta$ corresponds to positive rotation in the oriented plane $u^\perp \cap H$ — the orientation inherited from the right-handed ambient $\mathbb{R}^3$ of §2.5 through the Hodge-dual realization of §3.4.

Reassembling,
$$P' = P_\parallel + P_\perp' = (I + K^2)\, P + \sin\theta\, KP - \cos\theta\, K^2 P = \bigl[\,I + \sin\theta\, K + (1-\cos\theta)\, K^2\,\bigr]\, P.$$

Defining the rotation operator by
$$R(u,\theta) := I + \sin\theta\, K(u) + (1-\cos\theta)\, K(u)^2, \qquad (5.1)$$
we obtain a closed-form rotation by angle $\theta$ about the axis $u$; the classical $3 \times 3$ Rodrigues rotation formula is the same identity written in Cartesian coordinates (see [Arnold, §6.1] or [Hall, §1.2] for modern expositions). Equation (5.1) is stated as an operator on $H$; under the formal linear extension of $K$ to $\mathbb{R}^4$ (Remark 3.2), the same expression defines a $4 \times 4$ matrix — the gauge-compatible lift of §4 — which agrees with (5.1) on $H$ and fixes the gauge direction $\mathbf{1}$.

### 5.2 Lie-algebraic derivation

The same formula arises from the exponential map of the Lie algebra $\mathfrak{so}(3)$ into the Lie group $\mathrm{SO}(3)$, realized here on the zero-sum hyperplane $H$.

Restricting to $H$, the simplicially skew-adjoint endomorphisms of the three-dimensional inner-product space $(H, \langle\cdot,\cdot\rangle_s)$ form the Lie algebra
$$\mathfrak{so}(H, \langle\cdot,\cdot\rangle_s) \;\cong\; \mathfrak{so}(3)$$
under the matrix commutator. Our operators $K(u)$ provide a distinguished $4 \times 4$ lift of such endomorphisms to $\mathbb{R}^4$; in that lift, they additionally satisfy $K(u)\mathbf{1} = 0$ by Theorem 4.1(2). Since $G|_H = \tfrac{4}{3}\, I_H$ (equivalently, the simplicial Gram matrix restricted to $H$ is a positive scalar multiple of the identity), simplicial and ambient-Euclidean skew-adjointness coincide on $H$ and no distinction is needed once the restriction has been taken. The axis map $u \mapsto K(u)$ sends each zero-sum unit axis $u$ to a skew operator satisfying $K(u)^3 = -K(u)$ — equivalently, one whose restriction to $u^\perp \cap H$ acts as a quarter-turn — mirroring the classical hat-map $\mathbb{R}^3 \to \mathfrak{so}(3)$ of Cartesian rigid-body mechanics (cf. [Arnold, App.~2]; [Hall, §1.2]). The matrix exponential
$$\exp(\theta K) := \sum_{k=0}^{\infty} \frac{\theta^k K^k}{k!}$$
therefore maps $\mathfrak{so}(H, \langle\cdot,\cdot\rangle_s)$ into the identity component $\mathrm{SO}(3)$ of the orthogonal group: every $X \in \mathfrak{so}(H)$ satisfies $\mathrm{tr}(X) = 0$, so
$$\det \exp(\theta X) = e^{\theta\,\mathrm{tr}(X)} = 1,$$
placing the image in $\mathrm{SO}(3)$ rather than merely $\mathrm{O}(3)$ [Hall, §3.5].

Using the identity $K^3 = -K$ from Theorem 3.3, we have $K^{2n+1} = (-1)^n K$ and $K^{2n+2} = (-1)^n K^2$ for $n \geq 0$, and the Taylor series decomposes as

$$\exp(\theta K) = I + \theta K + \frac{\theta^2}{2!}K^2 + \frac{\theta^3}{3!}K^3 + \cdots$$

Regrouping by parity of the exponent and using the closure identity,

$$\exp(\theta K) = I + \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots \right) K + \left( \frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \cdots \right) K^2$$

$$= I + \sin\theta\, K + (1 - \cos\theta)\, K^2,$$

recovering the geometric result of §5.1. This is the Rodrigues rotation formula [Arnold, §6.1; Hall, §1.2] written in simplicial coordinates — intrinsic to the algebraic layer of the simplicial system in the sense made precise in §1.2 item 3.

### 5.3 Comparison of the two derivations

The geometric derivation (§5.1) and the Lie-algebraic derivation (§5.2) yield the same closed-form operator. The geometric derivation is more elementary and clarifies the structural role of the three matrices $I$, $K$, $K^2$ (as identity, in-plane quarter-turn, and negative perpendicular projection respectively; hence $I + K^2$ is the simplicial parallel projector onto $\mathrm{span}(u)$ and $-K^2$ is the projector onto $u^\perp \cap H$). The Lie-algebraic derivation makes the connection with $\mathfrak{so}(3)$ explicit and places the exponential step on a standard footing. On $H$, therefore,
$$R(u,\theta) \;=\; \exp(\theta K(u)) \;=\; I + \sin\theta\, K(u) + (1-\cos\theta)\, K(u)^2.$$

The wedge–Hodge construction underlying $K(u)$ itself has a higher-dimensional analog (see §8), which yields skew operators of higher arity when $N \geq 5$. The analog of the cubic identity $K^3 = -K$ and any comparable closed-form exponentiation, however, are *not* established in this paper; the higher-$N$ question is formulated but left open in §8.

### 5.4 Worked example

To illustrate the formula of §5.3 on a concrete axis that is not a frame vector, let $u$ be the midpoint axis between the frame vectors $\mathbf{v}_1$ and $\mathbf{v}_2$, in simplicial coordinates $u = (a, a, -a, -a)$ with $a = \sqrt{3}/4$. Verify:

- Zero-sum: $\sum u_i = 0$. $\checkmark$
- Unit length under the simplicial metric: $\tfrac{4}{3}\sum u_i^2 = \tfrac{4}{3} \cdot 4 \cdot \tfrac{3}{16} = 1$. $\checkmark$

Take $\theta = 2\pi/3$, so $\sin\theta = \sqrt{3}/2$ and $1 - \cos\theta = 3/2$. Direct computation (Appendix D) yields

$$R = \frac{1}{4}\begin{pmatrix}
1 & 3 & -\sqrt{3} & \sqrt{3} \\
3 & 1 & \sqrt{3} & -\sqrt{3} \\
\sqrt{3} & -\sqrt{3} & 1 & 3 \\
-\sqrt{3} & \sqrt{3} & 3 & 1
\end{pmatrix}.$$

Verification: row sums are all $1$, column sums are all $1$, $R^\top R = I$, and $\operatorname{tr} R = 1 = 2 + 2\cos(2\pi/3)$. Applied to the zero-sum point $P = (1/2, -3/2, -1/2, 3/2)$, the rotated point is

$$P' = \left(\tfrac{\sqrt{3} - 2}{2},\ -\tfrac{\sqrt{3}}{2},\ \tfrac{\sqrt{3} + 2}{2},\ -\tfrac{\sqrt{3}}{2}\right),$$

which verifies $\sum P'_i = 0$ and $\langle P', P' \rangle_s = \langle P, P \rangle_s = 20/3$, confirming zero-sum preservation and isometry on a non-trivial example.

---

## 6. Properties of the Rotation Matrix

We record the principal structural properties of $R(u, \theta)$. Each is provable directly from the defining formula, the identity $K^3 = -K$, and the gauge-annihilation $K\mathbf{1} = \mathbf{0}$. Item-by-item proofs appear in Appendix C.

**Proposition 6.1.** *For any zero-sum unit axis $u$ and angle $\theta$:*

1. *(Orthogonality)* $R^\top R = I$.
2. *(Gauge fixation)* $R\mathbf{1} = \mathbf{1}$. Equivalently, every row of $R$ sums to $1$.
3. *(Column sums)* $R^\top \mathbf{1} = \mathbf{1}$. Every column of $R$ sums to $1$.
4. *(Determinant)* $\det R = +1$.
5. *(Trace)* $\operatorname{tr} R = 2 + 2\cos\theta$ as a $4 \times 4$ real matrix (gauge lift). Equivalently, the restriction $R|_H$ has trace $1 + 2\cos\theta$ — the classical $\mathrm{SO}(3)$ formula — since $R$ acts as the identity on $\mathrm{span}\{\mathbf{1}\}$ and $\operatorname{tr}(R) = 1 + \operatorname{tr}(R|_H)$.
6. *(Hyperplane preservation)* If $P \in H$ then $RP \in H$.
7. *(Gauge-equivariance)* $R(P + k\mathbf{1}) = RP + k\mathbf{1}$ for all $k \in \mathbb{R}$.
8. *(Metric preservation)* $\langle RP, RQ \rangle_s = \langle P, Q \rangle_s$ for all $P, Q \in \mathbb{R}^4$ (equivalently $R^\top G R = G$).
9. *(Spectrum)* $R$ has eigenvalues $\{1, 1, e^{i\theta}, e^{-i\theta}\}$. The eigenvalue $1$ has two-dimensional eigenspace spanned by $\mathbf{1}$ and $u$.

Property 7 is especially important: it says that the rotation operator is compatible with the gauge equivalence, so that rotating a coordinate representative produces a valid coordinate representative of the rotated point. Combined with property 2, this makes $R$ a well-defined operator on the quotient space $\mathbb{R}^N / \mathbb{R}\mathbf{1}$, and hence on the geometric points of $\mathbb{R}^{N-1}$.

---

## 7. Computational Kernel: The 9-Multiplication Apply

A direct evaluation of $RP$ for a general $4 \times 4$ matrix $R$ and vector $P \in \mathbb{R}^4$ requires 16 scalar multiplications. The structural properties of $R$ and the zero-sum constraint on $P$ admit two independent reductions, which together bring this cost down to 9 multiplications — matching the per-apply cost of the quaternion-to-matrix rotation pipeline in graphics applications.

### 7.1 Output redundancy (16 → 12)

If $P \in H$ (zero-sum input), then by Proposition 6.1 item 6, $RP \in H$, so $(RP)_1 + (RP)_2 + (RP)_3 + (RP)_4 = 0$. The fourth coordinate is therefore determined by the first three:

$$(RP)_4 = -\left[(RP)_1 + (RP)_2 + (RP)_3\right].$$

Only three rows of $R$ need be evaluated (three dot products of length 4). Cost: 12 multiplications + additions.

### 7.2 Input redundancy (12 → 9)

The zero-sum constraint also applies to the input: $P_4 = -(P_1 + P_2 + P_3)$. Substituting into each of the three active rows, for $i \in \{1, 2, 3\}$,

$$(RP)_i = \sum_{j=1}^{4} R_{ij} P_j = \sum_{j=1}^{3} R_{ij} P_j + R_{i4}\, P_4 = \sum_{j=1}^{3} R_{ij} P_j - R_{i4}(P_1 + P_2 + P_3).$$

Grouping by input coordinate,

$$(RP)_i = \sum_{j=1}^{3} (R_{ij} - R_{i4})\, P_j = \sum_{j=1}^{3} \tilde{R}_{ij}\, P_j,$$

where $\tilde{R}_{ij} := R_{ij} - R_{i4}$ (for $i, j \in \{1, 2, 3\}$) is the $i,j$-th entry of a reduced $3 \times 3$ matrix $\tilde{R}$. Each row of the reduced apply is a 3-dot-product: 3 multiplications per row, 3 rows, totaling 9 multiplications. The fourth output coordinate is recovered by negation at no multiplicative cost.

**Theorem 7.1 (9-multiplication kernel).** *For $N = 4$, a simplicial rotation $R$ (Proposition 6.1), and a zero-sum input $P \in H$, the rotated point $RP$ can be computed using exactly 9 scalar multiplications.*

*Proof.* The reductions of §§7.1–7.2 exhibit an explicit 9-multiplication algorithm: three dot products of length 3 compute $(RP)_i$ for $i \in \{1, 2, 3\}$ via the reduced matrix $\tilde{R}_{ij} = R_{ij} - R_{i4}$, and $(RP)_4$ is recovered by negation at no multiplicative cost. $\square$

### 7.3 Interpretation as a change of basis

The $3 \times 3$ reduced matrix $\tilde{R}$ admits a clean structural interpretation: it is the restriction $R|_H$ expressed in the (non-orthonormal) basis $\{e_1 - e_4,\; e_2 - e_4,\; e_3 - e_4\}$ of $H$ — where $e_i$ denotes the $i$-th standard coordinate vector of $\mathbb{R}^4$ — obtained by dropping the $e_4$ coordinate and re-expressing $e_4 = -(e_1 + e_2 + e_3)$ via the zero-sum constraint. The 9-multiplication count is therefore the statement that, once the gauge redundancy is eliminated on both sides (input and output), rotation in the simplicial system has the same per-apply cost as $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$, to which it is conjugate via the hyperplane isometry $V$ of §2.5.

### 7.4 Comparison with quaternion pathways

Standard quaternion rotation pipelines offer two pathways to apply a rotation to a point (the multiplication counts below follow [Shoemake] and are standard in the computer graphics literature):

| Method | Storage (rotation) | Storage (point) | Multiplications / apply |
|---|---|---|---|
| Quaternion sandwich $q v q^{-1}$ | 4 (quaternion) | 3 | ~15 |
| Quaternion → $3 \times 3$ matrix, then apply | 4 + 9 derived | 3 | 9 |
| Intrinsic simplicial (this work) | 9 (reduced matrix $\tilde{R}$) | 3 | 9 |

The "multiplications / apply" column reports per-apply cost only; periodic re-orthogonalization under repeated composition (discussed below) adds an amortized cost comparable to quaternion renormalization and is orthogonal to the per-apply figure.

The intrinsic simplicial kernel ties the quaternion-to-matrix pipeline in per-apply cost and loses slightly in rotation storage (9 scalars vs.\ 4). The structural differences are qualitative: the simplicial kernel does not involve the $S^3$ double cover (so there are no sign ambiguities associated with $q$ vs.\ $-q$), is constructed algebraically from a zero-sum unit axis rather than as a point on a unit hypersphere, and operates without the non-commutative hypercomplex algebra of Hamilton products.

As with any matrix representation of rotations in floating-point arithmetic, iterated composition accumulates error and requires periodic re-enforcement of the manifold constraint. Because $\tilde{R}$ is the rotation expressed in a non-orthonormal basis of $H$ (§7.3), $\tilde{R}^\top \tilde{R} \neq I_3$ in general, so standard QR/Gram–Schmidt on $\tilde{R}$ alone is formally inappropriate; the correction is representation-specific. A natural recipe is to lift $\tilde{R}$ back to the $4 \times 4$ gauge-compatible $R$ and re-impose $R^\top R = I$ together with $R\mathbf{1} = \mathbf{1}$, via a Gram–Schmidt pass on the hyperplane block of $R$ (equivalently, standard Euclidean Gram–Schmidt applied to the columns of $R$ restricted to $H$, since the simplicial inner product reduces to a constant rescaling of the ambient Euclidean inner product on $H$). The cost is comparable to, but somewhat more expensive than, renormalizing a unit quaternion.

---

## 8. Higher Dimensions and Future Work

Having established the $N = 4$ framework end-to-end — intrinsic operators (§§3–5), structural properties (§6), and a 9-multiplication apply kernel (§7) — we now step back to ask which features of the construction are specific to $N = 4$ and which remain open for higher dimensions or adjacent mathematical programs.

### 8.1 The uniqueness of $N = 4$

The closed-form Rodrigues exponentiation of §5 relies on the Lie-algebraic identity $K^3 = -K$, which allowed the Taylor series of $\exp(\theta K)$ to refold into a finite trigonometric expression involving only $I$, $K$, and $K^2$. For $N = 4$, this identity holds because $K(u)$ is a rank-2 skew-symmetric $4 \times 4$ matrix, and rank-2 skew matrices have minimal polynomial $x(x^2 + c^2)$ for some constant $c$ (which we normalize to $1$).

For $N \geq 5$, the single-axis Rodrigues refolding does not extend. A wedge of $N - 3$ simplicial vectors is decomposable, and its Hodge dual is again a simple 2-form, so the associated skew operator is still rank 2 and satisfies the same minimal-polynomial identity as in the $N = 4$ case; the Rodrigues formula therefore applies to each such *blade* generator individually. The obstruction to a closed-form single-axis exponentiation is instead Lie-theoretic: the rotation group acting on the $(N-1)$-dimensional hyperplane is $\mathrm{SO}(N-1)$, and for $N - 1 \geq 4$ its dimension $\binom{N-1}{2} = \tfrac{(N-1)(N-2)}{2}$ strictly exceeds $N - 1$. A generic element of $\mathfrak{so}(N-1)$ is therefore not of the form $\theta\, K(u)$ for a single zero-sum axis $u$ — it is a linear combination of non-commuting blade generators, and matrix exponentials of non-commuting generators do not admit a single trigonometric closed form. Correspondingly, the intrinsic "cross-product-like" operator on the simplicial zero-sum hyperplane for general $N$ takes $N - 3$ inputs rather than a single axis — it is the Hodge dual of the wedge product of $N - 3$ vectors.

The uniqueness of $N = 4$ for a binary cross product with closed-form exponentiation *within the simplicial wedge–Hodge framework developed here* is the simplicial-coordinate reflection of the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$: in dimension 3, skew-symmetric matrices form a 3-dimensional Lie algebra, which coincides in dimension with the underlying vector space, and this coincidence is what permits the identification of an axis with a rotation generator — hence the binary cross product. The $n = 7$ octonionic binary cross product admitted by Eckmann's classification arises from a different algebraic structure (non-associative division algebras) and lies outside the framework of this paper (§1.2 item 6). In frame-theoretic language, this is the statement that the rotation calculus developed here lives natively on the $N = 4$ regular simplex ETF — the four-vector ETF in $\mathbb{R}^3$ — whose distinguished status in frame theory we revisit in §8.3.

### 8.2 The higher-$N$ construction (sketch)

For general $N$, the intrinsic wedge–Hodge construction proceeds as follows. The zero-sum hyperplane $H \cong \mathbb{R}^{N-1}$ carries an inner product from the Gram matrix and a volume form from the ambient orientation. For $k$ vectors $u_1, \ldots, u_k \in H$, their wedge product $u_1 \wedge \cdots \wedge u_k$ is a $k$-form, and the Hodge dual $\star(u_1 \wedge \cdots \wedge u_k)$ is an $(N-1-k)$-form, which can be represented as an $(N-1-k)$-vector under the canonical identification $H^* \cong H$. Taking $k = N - 3$ yields a 2-form, which when contracted against another vector and raised via the simplicial metric produces a vector, i.e.\ a linear operator on $H$.

The operator thus defined for $k = N - 3$ is the natural generalization of $K(u)$; for $N = 4$, $k = 1$ recovers our binary cross product. The explicit matrix representation in the overcomplete simplicial frame, the generalization of the $1/\sqrt{N-1}$ scaling constant, the analog of $K^3 = -K$ (or its failure), and the closed form (or its impossibility) for the exponential map are all computations that we defer to future work.

### 8.3 Other directions

**Composition formulas.** The product of two rotation matrices $R(u_1, \theta_1)\, R(u_2, \theta_2)$ is again a rotation matrix (by Proposition 6.1), necessarily of the form $R(u_3, \theta_3)$ for some axis $u_3$ and angle $\theta_3$. Explicit formulas for $(u_3, \theta_3)$ in terms of the inputs — analogous to the classical Rodrigues composition formulas for axis-angle pairs — would complete the intrinsic algebraic description of $\mathrm{SO}(3)$ action on the simplicial system, and are left open for future work.

**Rational Trigonometry.** Substituting the Weierstrass parameter $t = \tan(\theta/2)$ into our formula — in the spirit of Wildberger's program of rational trigonometry [Wildberger] — yields

$$R(u, t) = I + \left(\frac{2t}{1 + t^2}\right) K(u) + \left(\frac{2t^2}{1 + t^2}\right) K(u)^2,$$

which is rational in $t$ and in the entries of $u$. For axes $u \in H$ with $\sqrt{3}\,u \in \mathbb{Q}^4$ (equivalently, entries of $u$ in $\sqrt{3}\,\mathbb{Q}$), the entries of $K(u)$ are rational — the entries of $\tilde K(u)$ are differences of components of $u$, which lie in $\sqrt{3}\,\mathbb{Q}$, and the $1/\sqrt{3}$ in Definition 3.1 then clears — so $R(u, t)$ has rational entries for all rational $t$. For generic axes this rationality does not hold. Characterizing precisely which axes admit the rational parameterization is a concrete open question, and a natural complement to Wildberger's program of rational trigonometry.

**Information geometry and compositional data.** The zero-sum hyperplane, translated by $\tfrac{1}{N}\mathbf{1}$, becomes the probability simplex. Under the transformation $x_i = \sqrt{p_i}$, which maps the probability simplex to the positive orthant of the unit sphere, the simplicial inner product agrees with the Fisher information metric up to a positive scalar *at the uniform distribution $x \propto \mathbf{1}$* — a canonical match, since the Fisher metric is itself defined only up to positive rescaling. Aitchison geometry for compositional data analysis [Pawlowsky-Glahn-Egozcue] is built on the same zero-sum hyperplane $H$: the isometric log-ratio (ilr) transformation maps the probability simplex to $H$ after a component-wise log, and the associated inner-product structure agrees up to a positive scalar with the simplicial inner product of §2.4. The relationship between the intrinsic rotation operator constructed here and the geodesic flow on the probability simplex under Fisher–Rao — or rotation-compatible coordinate systems on Aitchison simplices — is a natural direction for future investigation.

**Erasure-robust frame coordinates.** The tight-frame structure of Proposition 2.0 is precisely what provides *erasure robustness* in frame-theoretic signal processing: equal-norm tight frames are optimal one-erasure codes for the spaces they represent [Goyal-Kovacevic-Kelner, Holmes-Paulsen], and the regular simplex ETF is the canonical such frame in $\mathbb{R}^{N-1}$. The 9-multiplication apply kernel of §7 already exploits this structure computationally — the fourth output coordinate is recovered from the first three by the zero-sum parity check $c_4 = -(c_1 + c_2 + c_3)$, which is exactly one-erasure decoding of the simplex-ETF code. Moreover, Proposition 6.1(7) makes rotation *gauge-equivariant*, $R(P + k\mathbf{1}) = RP + k\mathbf{1}$, so $R(u,\theta)$ descends to a well-defined action on erasure-coded data without first decoding to a minimal Cartesian basis. A systematic treatment of simplicial vector calculus as a suite of intrinsic operations on tight-frame-encoded signals — and the extension to higher-redundancy simplex codes via the $N > 4$ frames — is a natural direction for future work.

**Equiangular tight frames and single-qubit SIC-POVMs.** The $N = 4$ simplicial frame realizes the real ETF of four unit vectors in $\mathbb{R}^3$ with pairwise inner product $-\tfrac{1}{3}$. Under the Bloch-sphere representation of qubit density matrices, this is *exactly* the configuration of the four Bloch vectors of a single-qubit Symmetric Informationally Complete POVM [Renes-Blume-Kohout-Scott-Caves, Fuchs-Hoang-Stacey]: the SIC overlap condition $|\langle\psi_i|\psi_j\rangle|^2 = \tfrac{1}{3}$ translates via $\vec{n}_i \cdot \vec{n}_j = 2|\langle\psi_i|\psi_j\rangle|^2 - 1$ to $\vec{n}_i \cdot \vec{n}_j = -\tfrac{1}{3}$, and POVM completeness $\sum_i E_i = I$ translates to $\sum_i \vec{n}_i = \vec{0}$, both of which the Quadray frame satisfies identically (§2.1). The rotation operators $R(u, \theta)$ of §5 therefore provide a simplicial-coordinate realization of the $SO(3) \cong SU(2)/\{\pm I\}$ action of projective qubit unitaries on such POVMs, directly on the zero-sum hyperplane — and by §7.4, without passage through the $SU(2)$ double cover that quaternion pipelines require. Whether this intrinsic parameterization yields advantages for quantum-tomography algorithms, symmetric state estimation, or frame-robustness analyses in quantum information is a natural open question.

**Connections to other disciplines.** Beyond the motivations already discussed, stoichiometric compatibility classes in chemical reaction network theory [Müller-Regensburger] exhibit the same gauge-direction plus zero-sum-hyperplane structure; whether the intrinsic rotation operator developed here has substantive content in that setting — as opposed to the static inner-product structure alone — is an open question. Other gauge-quotient settings (for example, probabilistic simplices in compositional data analysis, just discussed) share the metric but do not obviously benefit from an analog of $R(u,\theta)$.

---

## 9. Conclusion

The simplicial (Quadray) coordinate system supports an autonomous *presentation* of the algebraic layer of 3D Euclidean vector calculus: inner product, binary cross product, and rotation can be stated and computed intrinsically on the zero-sum hyperplane $H$, with the diagonal redundancy handled as a gauge direction and no passage through a Cartesian frame at any step. Theorem 4.1 makes this precise in three clauses — the inner product is scalar-valued and gauge-invariant in both arguments, while the cross product $K(u)$ and the rotation $R(u,\theta) := \exp(\theta K(u))$ are vector-valued, preserve $H$, and respectively annihilate and fix the gauge direction $\mathbf{1}$. For $N = 4$, $K(u)$ satisfies the Lie-algebraic identity $K(u)^3 = -K(u)$, from which
$$R(u, \theta) = I + \sin\theta\, K(u) + (1 - \cos\theta)\, K(u)^2$$
follows by exponentiation; $R(u,\theta)$ is Euclidean orthogonal with $\det = +1$ and admits a 9-multiplication apply kernel for zero-sum inputs, matching quaternion-to-matrix performance without invoking the $S^3$ double cover. Under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4), these operators are carried (after restriction to $H$) to their classical $\mathbb{R}^3$ counterparts; the principal technical novelties are the joint gauge-compatibility theorem of §4, the explicit cyclic-difference form of $K(u)$ (§3.1), the gauge-compatible $4 \times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and the 9-multiplication apply kernel of §7.

The $N = 4$ case is distinguished, *within the simplicial wedge–Hodge framework developed here*, by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential (higher-$N$ generalizations, via Hodge duals of wedge products of arity $N - 3$, are discussed in §8). This answers the motivating question of §1.1 affirmatively for $N = 4$: the algebraic layer of 3D Euclidean vector calculus is self-contained on the zero-sum hyperplane of the simplicial coordinate frame, with no recourse to a Cartesian basis required at any stage.

---

## Acknowledgments

[Standard acknowledgments here.]

The author collaborated extensively with large language models — principally Anthropic's Claude and Google's Gemini — during the development of the derivations presented in this paper. These collaborations were productive for real-time derivation checking, literature contextualization, and iterative exposition. The author acknowledges this use transparently; the mathematical content and its correctness are the author's responsibility.

---

## References

[Ace] Ace, T. "Quadray formulas." http://minortriad.com/quadray.html.

[Amari] Amari, S. *Information Geometry and Its Applications*. Applied Mathematical Sciences, vol. 194. Springer, 2016.

[Arnold] Arnold, V.I. *Mathematical Methods of Classical Mechanics*. 2nd ed., Graduate Texts in Mathematics, vol. 60. Springer, 1989.

[Arnold-Falk-Winther] Arnold, D.N., Falk, R.S., Winther, R. "Finite element exterior calculus, homological techniques, and applications." *Acta Numerica* 15, 1–155 (2006).

[Brenner-Scott] Brenner, S.C., Scott, L.R. *The Mathematical Theory of Finite Element Methods*. 3rd ed., Texts in Applied Mathematics, vol. 15. Springer, 2008.

[Chentsov] Chentsov, N.N. *Statistical Decision Rules and Optimal Inference* (English translation). American Mathematical Society, 1982.

[Christensen] Christensen, O. *An Introduction to Frames and Riesz Bases*. 2nd ed., Applied and Numerical Harmonic Analysis. Birkhäuser, 2016.

[Ciarlet] Ciarlet, P.G. *The Finite Element Method for Elliptic Problems*. Classics in Applied Mathematics, vol. 40. SIAM, 2002.

[Desbrun-Hirani-Leok-Marsden] Desbrun, M., Hirani, A.N., Leok, M., Marsden, J.E. "Discrete Exterior Calculus." arXiv:math/0508341 (2005).

[Duffin-Schaeffer] Duffin, R.J., Schaeffer, A.C. "A class of nonharmonic Fourier series." *Transactions of the American Mathematical Society* 72, 341–366 (1952).

[Eckmann] Eckmann, B. "Stetige Lösungen linearer Gleichungssysteme." *Commentarii Mathematici Helvetici* 15, 318–339 (1943).

[Flanders] Flanders, H. *Differential Forms with Applications to the Physical Sciences*. Dover, 1989 (reprint of Academic Press, 1963).

[Fuchs-Hoang-Stacey] Fuchs, C.A., Hoang, M.C., Stacey, B.C. "The SIC Question: History and State of Play." *Axioms* 6(3), 21 (2017).

[Fuller] Fuller, R.B. *Synergetics: Explorations in the Geometry of Thinking*. Macmillan, 1975.

[Goyal-Kovacevic-Kelner] Goyal, V.K., Kovačević, J., Kelner, J.A. "Quantized frame expansions with erasures." *Applied and Computational Harmonic Analysis* 10(3), 203–233 (2001).

[Hall] Hall, B. *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*. 2nd ed., Graduate Texts in Mathematics, vol. 222. Springer, 2015.

[Hestenes] Hestenes, D. *New Foundations for Classical Mechanics*. 2nd ed., Fundamental Theories of Physics, vol. 99. Kluwer, 1999.

[Holmes-Paulsen] Holmes, R.B., Paulsen, V.I. "Optimal frames for erasures." *Linear Algebra and its Applications* 377, 31–51 (2004).

[Marsden-Ratiu] Marsden, J.E., Ratiu, T.S. *Introduction to Mechanics and Symmetry: A Basic Exposition of Classical Mechanical Systems*. 2nd ed., Texts in Applied Mathematics, vol. 17. Springer, 1999.

[Massey] Massey, W.S. "Cross Products of Vectors in Higher-Dimensional Euclidean Spaces." *American Mathematical Monthly* 90(10), 697–701 (1983).

[Müller-Regensburger] Müller, S., Regensburger, G. "Generalized Mass Action Systems: Complex Balancing Equilibria and Sign Vectors of the Stoichiometric and Kinetic-Order Subspaces." *SIAM Journal on Applied Mathematics* 72(6), 1926–1947 (2012).

[Pawlowsky-Glahn-Egozcue] Pawlowsky-Glahn, V., Egozcue, J.J., Tolosana-Delgado, R. *Modeling and Analysis of Compositional Data*. Statistics in Practice. Wiley, 2015.

[QuadrayWiki] "Quadray coordinates." Wikipedia. https://en.wikipedia.org/wiki/Quadray_coordinates. (Attributes the coordinate system to Darrel Jarmusch, 1981.)

[Renes-Blume-Kohout-Scott-Caves] Renes, J.M., Blume-Kohout, R., Scott, A.J., Caves, C.M. "Symmetric informationally complete quantum measurements." *Journal of Mathematical Physics* 45(6), 2171–2180 (2004).

[Shoemake] Shoemake, K. "Animating Rotation with Quaternion Curves." *Computer Graphics (SIGGRAPH '85 Proceedings)* 19(3), 245–254 (1985).

[Spivak] Spivak, M. *Calculus on Manifolds: A Modern Approach to Classical Theorems of Advanced Calculus*. W. A. Benjamin, 1965.

[Thomson] Thomson, A. "Spread-Quadray Rotors – v4.0: A Tetrahedral Alternative to Quaternions for Gimbal-Lock-Free Rotation Representation." Thomson Architecture, Inc. / ARTexplorer Project. DOI: 10.13140/RG.2.2.23476.51846. April 2026.

[Urner] Urner, K. "Quadray Coordinates: A Logical Alternative." http://www.grunch.net/synergetics/quadintro.html.

[Wildberger] Wildberger, N.J. *Divine Proportions: Rational Trigonometry to Universal Geometry*. Wild Egg Books, 2005.

---

## Appendix A: The Zero-Sum Inner Product Identity

**Proposition A.1 (restating Proposition 2.1).** *Let $c \in \mathbb{R}^N$ satisfy $\sum c_i = 0$. Then*

$$\langle c, c \rangle = c^\top G\, c = \frac{N}{N-1} \sum_{i=1}^N c_i^2.$$

*Proof.* Squaring the zero-sum constraint:

$$\left(\sum_{i=1}^N c_i\right)^2 = \sum_{i=1}^N c_i^2 + 2\sum_{i < j} c_i c_j = 0,$$

so $\sum_{i < j} c_i c_j = -\tfrac{1}{2}\sum c_i^2$.

Now compute:

$$c^\top G\, c = \sum_i c_i^2 - \frac{1}{N-1}\sum_{i \neq j} c_i c_j = \sum_i c_i^2 - \frac{2}{N-1}\sum_{i < j} c_i c_j$$

$$= \sum_i c_i^2 - \frac{2}{N-1} \cdot \left(-\frac{1}{2}\sum_i c_i^2\right) = \left(1 + \frac{1}{N-1}\right) \sum_i c_i^2 = \frac{N}{N-1}\sum_i c_i^2. \quad \square$$

For $N = 4$, the factor is $4/3$; for $N = 3$, it is $3/2$.

---

## Appendix B: Proof of $K^3 = -K$ for $N = 4$

We prove Theorem 3.3: for any zero-sum unit axis $u$ (i.e.\ $\sum u_i = 0$ and $\tfrac{4}{3}\sum u_i^2 = 1$), the operator $K(u)$ defined in Definition 3.1 satisfies $K(u)^3 = -K(u)$.

**Step 1: Rank of $K(u)$.** The operator $K(u)$ is skew-symmetric, so its rank is even. We claim its rank is exactly 2.

The kernel of $K(u)$ contains $\mathbf{1}$ (since $K \mathbf{1} = 0$ by Remark 3.2) and $u$. To verify $K(u) u = 0$, compute the first component explicitly using Definition 3.1:

$$\begin{aligned}
\bigl(K(u)\, u\bigr)_1
&= \tfrac{1}{\sqrt{3}}\bigl[(u_3 - u_4) u_2 + (u_4 - u_2) u_3 + (u_2 - u_3) u_4\bigr] \\
&= \tfrac{1}{\sqrt{3}}\bigl[u_3 u_2 - u_4 u_2 + u_4 u_3 - u_2 u_3 + u_2 u_4 - u_3 u_4\bigr] \\
&= 0,
\end{aligned}$$

where each term in the bracket cancels against its partner. Components 2, 3, and 4 are obtained from component 1 by cyclically permuting the indices $(1, 2, 3, 4)$ and vanish analogously. Thus $u \in \ker K(u)$. Since $u$ is zero-sum while $\mathbf{1}$ is not, $\{\mathbf{1}, u\}$ are linearly independent and $\ker K(u)$ is at least two-dimensional, so $\mathrm{rank}\, K(u) \leq 2$.

Conversely, when $u$ is a zero-sum unit axis, $K(u)$ is not the zero matrix, so $\mathrm{rank}\, K(u) \geq 1$; by skew-symmetry, the rank must be even, so $\mathrm{rank}\, K(u) = 2$.

**Step 2: Spectrum.** A $4 \times 4$ skew-symmetric real matrix of rank 2 has spectrum $\{0, 0, +ci, -ci\}$ for some real $c \geq 0$. Summing squared eigenvalues gives $\operatorname{tr}(K^2) = -2c^2$, so it suffices to compute $\operatorname{tr}(K(u)^2)$.

For any real matrix $M$ with $M^\top = -M$, one has $(M^2)_{ii} = \sum_j M_{ij} M_{ji} = -\sum_j M_{ij}^2$, so

$$\operatorname{tr}(\tilde{K}(u)^2) = -\sum_{i,j} \tilde{K}(u)_{ij}^2 = -\,\bigl(\text{sum of squares of off-diagonal entries of }\tilde{K}(u)\bigr).$$

The off-diagonal entries of $\tilde{K}(u)$ are exactly the six signed pairwise differences $\pm(u_i - u_j)$ for $1 \leq i < j \leq 4$, and each such difference (up to sign, which squares away) appears in $\tilde{K}$ exactly *twice* — once in position $(i',j')$ and once in position $(j',i')$ for appropriate row/column placements $(i',j')$. Hence the sum of squared entries is

$$\sum_{i,j} \tilde{K}(u)_{ij}^2 = 2\sum_{i < j} (u_i - u_j)^2.$$

We now evaluate $\sum_{i<j} (u_i - u_j)^2$ on the zero-sum hyperplane. Expanding,

$$\sum_{i<j} (u_i - u_j)^2 = \sum_{i<j}\bigl(u_i^2 + u_j^2 - 2 u_i u_j\bigr) = (N-1)\sum_i u_i^2 - 2 \sum_{i<j} u_i u_j.$$

The zero-sum constraint $\sum_i u_i = 0$ gives $\bigl(\sum_i u_i\bigr)^2 = \sum_i u_i^2 + 2\sum_{i<j} u_i u_j = 0$, so $2\sum_{i<j} u_i u_j = -\sum_i u_i^2$. Substituting (with $N = 4$),

$$\sum_{i<j} (u_i - u_j)^2 = 3\sum_i u_i^2 + \sum_i u_i^2 = 4\sum_i u_i^2.$$

Therefore the sum of squared entries of $\tilde{K}(u)$ equals $2 \cdot 4 \sum_i u_i^2 = 8 \sum_i u_i^2$, and

$$\operatorname{tr}(\tilde{K}(u)^2) = -8 \sum_i u_i^2.$$

For the scaled operator $K(u) = \tfrac{1}{\sqrt{3}}\, \tilde{K}(u)$, $\operatorname{tr}(K^2) = \tfrac{1}{3}\operatorname{tr}(\tilde{K}^2) = -\tfrac{8}{3}\sum_i u_i^2$. Applying the unit-axis condition $\tfrac{4}{3}\sum_i u_i^2 = 1$ (equivalently $\sum_i u_i^2 = 3/4$) yields

$$\operatorname{tr}(K(u)^2) = -\tfrac{8}{3}\cdot\tfrac{3}{4} = -2,$$

so $-2c^2 = -2$ and $c = 1$. Equivalently, $\operatorname{tr}(\tilde{K}(u)^2) = -8 \cdot \tfrac{3}{4} = -6$, giving unscaled eigenvalues $\pm i\sqrt{3}$.

**Step 3: Minimal polynomial.** Real skew-symmetric matrices are normal ($M M^\top = M^\top M$), hence unitarily diagonalizable over $\mathbb{C}$ by the spectral theorem for normal operators. Their minimal polynomial therefore factors into distinct linear factors over $\mathbb{C}$. For spectrum $\{0, 0, +i, -i\}$ this minimal polynomial is $x(x-i)(x+i) = x(x^2 + 1) = x^3 + x$. Therefore $K(u)^3 + K(u) = 0$, i.e.

$$K(u)^3 = -K(u). \quad \square$$

**Remark B.1.** The prefactor $1/\sqrt{3}$ in Definition 3.1 is precisely the factor required to set $c = 1$. Without this factor — that is, using $\tilde{K}(u)$ directly — the spectrum would be $\{0, 0, +i\sqrt{3}, -i\sqrt{3}\}$ and the cubic identity would read $\tilde{K}(u)^3 = -3\, \tilde{K}(u)$, which does not produce a clean Rodrigues exponentiation. The $1/\sqrt{3}$ is geometrically forced by the mismatch between raw coordinates and the simplicial inner product, as discussed after Definition 3.1.

---

## Appendix C: Properties of the Rotation Matrix $R$

We prove Proposition 6.1 items in turn.

**Orthogonality** ($R^\top R = I$). Since $K^\top = -K$, we have

$$R^\top = I - \sin\theta\, K + (1 - \cos\theta)\, K^2.$$

Then

$$R^\top R = (I - \sin\theta K + (1 - \cos\theta)K^2)(I + \sin\theta K + (1 - \cos\theta)K^2).$$

Expanding and using $K^3 = -K$ (so $K^4 = -K^2$):

$$= I + \left[(1 - \cos\theta) + (1-\cos\theta) - \sin^2\theta\right] K^2 + \left[(1-\cos\theta)^2\right] K^4 + \text{(odd-power terms)}.$$

Odd-power terms cancel: the linear-in-$K$ terms sum to $(\sin\theta - \sin\theta) K = 0$; the cubic-in-$K$ terms sum to $\sin\theta(1-\cos\theta) K^3 - \sin\theta(1-\cos\theta) K^3 = 0$.

Collecting $K^2$ coefficients: $2(1 - \cos\theta) - \sin^2\theta - (1-\cos\theta)^2 = 2(1 - \cos\theta) - (1 - \cos^2\theta) - (1 - 2\cos\theta + \cos^2\theta) = 2 - 2\cos\theta - 1 + \cos^2\theta - 1 + 2\cos\theta - \cos^2\theta = 0$.

So $R^\top R = I$. $\square$

**Gauge fixation** ($R\mathbf{1} = \mathbf{1}$). Since $K\mathbf{1} = \mathbf{0}$, we have $K^2 \mathbf{1} = \mathbf{0}$, so $R\mathbf{1} = I\mathbf{1} + 0 + 0 = \mathbf{1}$. $\square$

**Column sums** ($R^\top \mathbf{1} = \mathbf{1}$). From $R^\top = R^{-1}$ (by orthogonality) and $R\mathbf{1} = \mathbf{1}$, applying $R^{-1}$ to both sides gives $\mathbf{1} = R^{-1}\mathbf{1} = R^\top\mathbf{1}$. $\square$

**Determinant** ($\det R = +1$). $R$ is orthogonal with positive determinant because the exponential of a skew-symmetric matrix always has determinant $+1$: $\det \exp(M) = \exp(\operatorname{tr} M) = \exp(0) = 1$ for skew $M$. $\square$

**Trace** $\operatorname{tr} R = 2 + 2\cos\theta$ *($4 \times 4$ lift; $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$).* $\operatorname{tr}(I) = 4$. $\operatorname{tr}(K) = 0$ (skew). $\operatorname{tr}(K^2) = -2$ (Appendix B). So $\operatorname{tr}(R) = 4 + 0 + (1 - \cos\theta)(-2) = 2 + 2\cos\theta$. Since $R$ fixes $\mathbf{1}$, splitting $\mathbb{R}^4 = \mathrm{span}\{\mathbf{1}\} \oplus H$ gives $\operatorname{tr}(R) = 1 + \operatorname{tr}(R|_H)$, hence $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$ (the classical $\mathrm{SO}(3)$ trace of a rotation by $\theta$ in the hyperplane). $\square$

**Hyperplane preservation, gauge-equivariance, metric preservation**: these follow from properties 1, 2, and 3 combined. Details omitted.

**Spectrum**: $R$ has eigenvalue $+1$ on the two-dimensional subspace spanned by $\mathbf{1}$ and $u$ (both annihilated by $K$); on the orthogonal complement of this subspace (a 2D plane), $R$ acts as a planar rotation by $\theta$, with eigenvalues $e^{\pm i\theta}$. $\square$

---

## Appendix D: Worked Example Computations

For $u = (a, a, -a, -a)$ with $a = \sqrt{3}/4$ and $\theta = 2\pi/3$:

The cyclic-difference matrix $\tilde{K}(u)$ has entries $\tilde{K}_{ij} = u_{\sigma(i,j)_1} - u_{\sigma(i,j)_2}$ where $\sigma$ is the appropriate permutation. For this specific $u$:

- $\tilde{K}_{12} = u_3 - u_4 = -a - (-a) = 0$.
- $\tilde{K}_{13} = u_4 - u_2 = -a - a = -2a$.
- $\tilde{K}_{14} = u_2 - u_3 = a - (-a) = 2a$.
- $\tilde{K}_{23} = u_1 - u_4 = a - (-a) = 2a$.
- $\tilde{K}_{24} = u_3 - u_1 = -a - a = -2a$.
- $\tilde{K}_{34} = u_1 - u_2 = a - a = 0$.

Multiplying by $1/\sqrt{3}$ and using $a = \sqrt{3}/4$:

$$K(u) = \begin{pmatrix}
0 & 0 & -\tfrac{1}{2} & \tfrac{1}{2} \\
0 & 0 & \tfrac{1}{2} & -\tfrac{1}{2} \\
\tfrac{1}{2} & -\tfrac{1}{2} & 0 & 0 \\
-\tfrac{1}{2} & \tfrac{1}{2} & 0 & 0
\end{pmatrix}.$$

Computing $K^2$:

$$K^2 = \begin{pmatrix}
-\tfrac{1}{2} & \tfrac{1}{2} & 0 & 0 \\
\tfrac{1}{2} & -\tfrac{1}{2} & 0 & 0 \\
0 & 0 & -\tfrac{1}{2} & \tfrac{1}{2} \\
0 & 0 & \tfrac{1}{2} & -\tfrac{1}{2}
\end{pmatrix}.$$

Verification: $K^3 = K \cdot K^2 = -K$ (entries match with flipped signs). $\checkmark$

For $\theta = 2\pi/3$: $\sin\theta = \sqrt{3}/2$, $1 - \cos\theta = 3/2$.

$$R = I + \frac{\sqrt{3}}{2} K + \frac{3}{2} K^2 = \frac{1}{4}\begin{pmatrix}
1 & 3 & -\sqrt{3} & \sqrt{3} \\
3 & 1 & \sqrt{3} & -\sqrt{3} \\
\sqrt{3} & -\sqrt{3} & 1 & 3 \\
-\sqrt{3} & \sqrt{3} & 3 & 1
\end{pmatrix}.$$

Row sums: $(1 + 3 - \sqrt{3} + \sqrt{3})/4 = 1$. $\checkmark$. Trace of the $4 \times 4$ matrix: $4 \cdot \tfrac{1}{4} = 1 = 2 + 2\cos(2\pi/3) = 2 - 1$. $\checkmark$

For completeness, applying $R$ to the zero-sum point $P = (1/2, -3/2, -1/2, 3/2)$ gives $P' = \left(\tfrac{\sqrt{3} - 2}{2},\ -\tfrac{\sqrt{3}}{2},\ \tfrac{\sqrt{3} + 2}{2},\ -\tfrac{\sqrt{3}}{2}\right)$ as stated in §5.4, and one checks directly that $\sum P'_i = 0$ and $\tfrac{4}{3}\sum (P'_i)^2 = \tfrac{4}{3} \cdot 5 = 20/3 = \langle P, P \rangle_s$.

---

*[End of paper.]*
