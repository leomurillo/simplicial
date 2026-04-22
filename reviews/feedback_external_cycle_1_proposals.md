# External-review cycle 1 — proposal sheet

**Scope:** cross-cutting polish proposed by an external reviewer (tour feedback), consolidated as a diff against `simplicial_vector_calculus.md`. Plus one Author-initiated addition in §8.3.

**Status at compile time:** Proposals only. Not yet implemented in the manuscript. Reviewers X and Y are asked to adjudicate each item on the severity ladder (Critical / High / Medium / Low) and to identify anything they would block.

---

## Group A — Notation refinement (four sites)

**A1.** Replace "exceptional Lie algebra isomorphism $\mathfrak{so}(3) \cong \mathbb{R}^3$" with "exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$" (hyphenate "Lie-algebra" as a compound modifier; clarify that the isomorphism is of Lie algebras, where the $\mathbb{R}^3$ side is equipped with the cross-product bracket rather than the trivial abelian bracket).

Affected sites:
- Abstract, paragraph after itemized list (currently: ". . . reflection of the exceptional Lie algebra isomorphism $\mathfrak{so}(3) \cong \mathbb{R}^3$. Higher $N$ . . .").
- §1.2 item 6.
- §3 opening paragraph (the classical-realizations list: "$\mathrm{ad}_u$ on $\mathfrak{so}(3) \cong \mathbb{R}^3$").
- §8.1 closing paragraph (". . . exceptional Lie algebra isomorphism $\mathfrak{so}(3) \cong \mathbb{R}^3$.").

---

## Group B — Substantive edits

**B1. §1.2 item 6 — Eckmann classification: octonion branch.** After the sentence identifying $N = 4$ as the simplicial realization of the $n = 3$ branch, append:

> "The $n = 7$ realization — the octonion cross product on $\mathbb{R}^7$ — is binary but arises from the non-associative octonion algebra rather than from wedge–Hodge duality, and therefore lies outside the simplicial framework developed here."

Rationale: Eckmann classifies $n \in \{0, 1, 3, 7\}$; the paper currently claims "$N = 4$ is the unique simplicial case" without explaining why the $n = 7$ entry does not also appear as a simplicial construction. The sentence explicitly situates the $n = 7$ cross product outside the simplicial / wedge–Hodge framework.

**B2. §1.3 — New paragraph "Relation to discrete exterior calculus".** Insert after the "Low-$N$ degeneracies" paragraph, before the "---" divider:

> "**Relation to discrete exterior calculus.** The phrase *simplicial vector calculus* also appears in the discrete exterior calculus tradition of Desbrun, Hirani, Leok, and Marsden [Desbrun-Hirani-Leok-Marsden] and the finite element exterior calculus of Arnold, Falk, and Winther [Arnold-Falk-Winther], where $\wedge$, $\star$, and $d$ are defined directly on simplicial complexes for PDE discretization. The present work is distinct in scope: we develop only the algebraic layer (inner product, binary cross product, rotation) on the $N$-axis frame of a single simplex and its associated zero-sum hyperplane, not on a complex, and differential operators $\nabla$, $\mathrm{div}$, $\mathrm{curl}$ are deferred (§1.1, §4). The structural relationship between the present construction and DEC — in particular, whether $\tilde{K}(u)$ admits a description as a discrete exterior derivative applied to $u$ viewed as a 0-cochain on the tetrahedron's 1-skeleton — is left to future work."

Rationale: disambiguates the paper's title phrase from an established DEC/FEEC tradition; acknowledges prior use of the term "simplicial" in an adjacent literature; flags an honest open question about the relationship.

**B3. §3 descent theorem proof — expand $R^\top G R = G$ step.** In the final paragraph of the proof (currently: ". . . which follows from the commutation $GK(u) = K(u)G$ (Remark 3.2(1)); the ambient Euclidean lift . . ."), replace the semicolon after "Remark 3.2(1))" with a colon and insert the explicit derivation:

> "which follows from the commutation $GK(u) = K(u)G$ (Remark 3.2(1)): since $G$ commutes with $K$ it commutes with every power, hence with $\exp(\theta K) = R$, so $R^\top G R = \exp(-\theta K)\, G\, \exp(\theta K) = G\, \exp(-\theta K)\, \exp(\theta K) = G$; the ambient Euclidean lift $R^\top R = I$ and . . ."

Rationale: makes an otherwise terse derivation step fully explicit (commutation with $K$ ⇒ commutation with every power ⇒ commutation with $\exp(\theta K)$), removing a potential "easy to see" gap.

**B4. §7 — Correct the "no renormalization" claim.** In the paragraph comparing the simplicial kernel to quaternion-to-matrix, replace

> "does not require renormalization after composition (no drift off a unit hypersphere, since $\tilde{R}$ is computed algebraically from a zero-sum unit axis), and operates without the non-commutative hypercomplex algebra of Hamilton products."

with

> "is constructed algebraically from a zero-sum unit axis rather than as a point on a unit hypersphere, and operates without the non-commutative hypercomplex algebra of Hamilton products. As with any matrix representation of rotations, however, iterated composition accumulates floating-point error and requires periodic re-orthogonalization of $\tilde{R}$ — for instance by QR or Gram–Schmidt applied to the reduced $3\times 3$ matrix — an operation comparable to but slightly more expensive than renormalizing a unit quaternion."

Rationale: the current claim ("does not require renormalization after composition") is mathematically correct only at exact arithmetic; any floating-point implementation of a rotation *matrix* accumulates error under composition and requires re-orthogonalization. The replacement (i) removes the over-strong claim, (ii) keeps the genuine structural distinction (algebraic construction from a zero-sum unit axis, not a point on $S^3$), and (iii) is honest about the cost trade-off vs. quaternion renormalization.

**B5. §8.3 — "Information geometry" → "Information geometry and compositional data".** Rename the bolded paragraph label and append the Aitchison-geometry sentences. The current paragraph ends:

> "The relationship between the intrinsic rotation operator constructed here and the geodesic flow on the probability simplex under Fisher-Rao is a thread we plan to pursue in a companion paper."

The proposed replacement paragraph is:

> "**Information geometry and compositional data.** The zero-sum hyperplane, translated by $\tfrac{1}{N}\mathbf{1}$, becomes the probability simplex. The simplicial inner product pulls back to the Fisher information metric under the transformation $x_i = \sqrt{p_i}$, mapping the probability simplex to the positive orthant of the unit sphere. The zero-sum hyperplane structure is also central to Aitchison geometry for compositional data analysis [Pawlowsky-Glahn-Egozcue]: the isometric log-ratio (ilr) transformation on the probability simplex is structurally the composition of the component-wise log map with the zero-sum projection $c \mapsto c^{\mathrm{zs}}$ of §2.3 followed by a choice of orthonormal basis on $H$. The relationship between the intrinsic rotation operator constructed here and the geodesic flow on the probability simplex under Fisher–Rao — or rotation-compatible coordinate systems on Aitchison simplices — is a thread we plan to pursue in a companion paper."

Rationale: Aitchison geometry is the natural statistical home of the zero-sum hyperplane and is widely cited; the paragraph already invokes Fisher-Rao, so adding the compositional-data tradition is a small, well-situated extension. Also fixes "Fisher-Rao" (hyphen) → "Fisher–Rao" (en-dash).

**B6. §9 Conclusion paragraph 2 — drop "not merely a reparameterization".** Replace

> "The simplicial coordinate system is not merely a reparameterization of Cartesian geometry. It is an autonomous arena in which the algebraic layer of 3D Euclidean vector calculus (inner product, binary cross product, rotation) can be formulated intrinsically, with a gauge structure (the diagonal redundancy), a canonical hyperplane (zero-sum), and natively defined inner products, cross products, and rotations. The $N = 4$ case is distinguished by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits the binary cross product and closed-form exponential. Higher-$N$ generalizations exist via Hodge duals of wedge products and open a program of simplicial exterior calculus that we leave to future work."

with

> "The simplicial coordinate system thereby supports an autonomous *presentation* of the algebraic layer of 3D Euclidean vector calculus: inner product, binary cross product, and rotation can be stated and computed intrinsically, with a gauge structure (the diagonal redundancy) and a canonical hyperplane (zero-sum), without passing through a Cartesian frame at any step. The construction is unitarily equivalent to classical 3D vector calculus under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5; the novelty lies in the explicit cyclic-difference form of $K(u)$, the gauge-compatible $4 \times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, and the 9-multiplication apply kernel of §7. The $N = 4$ case is distinguished by the coincidence $\dim \mathfrak{so}(3) = 3$, which permits a binary cross product and closed-form exponential. Higher-$N$ generalizations exist via Hodge duals of wedge products and open a program of simplicial exterior calculus that we leave to future work."

Rationale: the earlier framing ("not merely a reparameterization . . . autonomous arena") over-reaches; in exact terms the simplicial construction is unitarily equivalent to classical 3D vector calculus under the §2.5 isometry. Reframing "novelty" around concrete deliverables (cyclic-difference $K$, gauge-compatible $4\times 4$ lift into $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$, 9-mul kernel) is more defensible and avoids a potential reviewer complaint.

---

## Group C — Author-initiated addition (§8.3)

**C1. §8.3 — FEEC application-context sentence.** Add a new paragraph inside §8.3, after the Information-geometry paragraph (B5) and before or near the "Generalized physics applications" paragraph:

> "**Finite element exterior calculus.** Finite element exterior calculus on unstructured tetrahedral meshes [Arnold-Falk-Winther] provides a natural application context; the intrinsic operators developed here could in principle supply pointwise algebraic operations on tetrahedral elements without reference to a global Cartesian frame."

Rationale: identifies a concrete potential application of the algebraic layer (element-local pointwise operations on tetrahedral meshes), complementing the §1.3 DEC/FEEC disambiguation in B2 without overstating the contribution.

---

## Group D — New references (three)

**D1.** `[Arnold-Falk-Winther] Arnold, D.N., Falk, R.S., Winther, R. "Finite element exterior calculus, homological techniques, and applications." *Acta Numerica* 15, 1–155 (2006).`

**D2.** `[Desbrun-Hirani-Leok-Marsden] Desbrun, M., Hirani, A.N., Leok, M., Marsden, J.E. "Discrete Exterior Calculus." arXiv:math/0508341 (2005).`

**D3.** `[Pawlowsky-Glahn-Egozcue] Pawlowsky-Glahn, V., Egozcue, J.J., Tolosana-Delgado, R. *Modeling and Analysis of Compositional Data*. Statistics in Practice. Wiley, 2015.`

To be inserted in alphabetical-key order in the References list.

---

## What reviewers are asked to adjudicate

1. For each item (A1, B1–B6, C1, D1–D3): does the proposed edit **strengthen**, **neutrally change**, or **weaken** the manuscript? If weaken, at what severity?
2. Any factual or citation errors in the new references or in the bodies of B1, B2, B5, C1?
3. Any downstream consistency sweeps these edits force (e.g., if §9's reframing lands, do §1 claims about "autonomous arena" need to be softened too)?
4. Any missing alternative framings?

Close with a single `STATUS: GREEN` / `STATUS: AMBER` line per the usual convention.
