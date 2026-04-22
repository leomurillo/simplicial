# Reviewer X — Formalism audit of external-review cycle 1 proposals

**Scope.** Red-team audit of the *proposals themselves* in `feedback_external_cycle_1_proposals.md` (A1, B1–B6, C1, D1–D3). Anchored against the current manuscript text (already STATUS GREEN through §6 + Appendix D in prior cycles). No Critical findings; one High finding (B4 prescription); a handful of Medium/Low items. Endorsed: A1, B1, B2, B3, B5 (body), C1, D1–D3.

## Proposal-by-proposal findings

**[A1] (Notation — Lie-algebra hyphen + $(\mathbb{R}^3, \times)$): endorse.**
The current abstract text and §1.2 item 6 / §3 / §8.1 speak of "$\mathfrak{so}(3) \cong \mathbb{R}^3$", which is ambiguous: $\mathbb{R}^3$ as a vector space is abelian as a Lie algebra (trivial bracket), so the isomorphism is vacuously false unless the cross-product bracket is stipulated. Writing $(\mathbb{R}^3, \times)$ makes the Lie-algebra structure explicit and is the standard remedy. Hyphenation of "Lie-algebra" as a compound modifier is grammatical and consistent with §1.2 item 6's existing "Lie-algebraic identity". No formalism objection.

**[P-L-B1] (octonion $n=7$ sentence): Low — endorse with one wording nit.**
The substantive claim — that the $n=7$ cross product is binary but originates from the (non-associative) octonion algebra rather than from a wedge–Hodge construction — is factually correct and consistent with the Eckmann [Eckmann] / Massey [Massey] references already in the manuscript. The seven-dimensional cross product is defined via octonion multiplication on $\mathrm{Im}(\mathbb{O})$; equivalently via a calibration 3-form (the associative calibration of a $G_2$-structure on $\mathbb{R}^7$), which is *not* of the form $\star(u\wedge\cdot)$ used in this paper. The manuscript's §3.4 Hodge-dual argument (dim $V = 3$ ⇒ $\star(u\wedge v)$ is a 1-vector; dim $V \geq 4$ ⇒ higher arity) already precludes $n=7$ as a wedge–Hodge cross product, so the new sentence is consistent.

*Nit (Low):* "arises from the non-associative octonion algebra rather than from wedge–Hodge duality" is a true but slightly imprecise contrast; a formalist reviewer might prefer "…rather than from the simplicial wedge–Hodge construction of §3.4". Optional softening; not blocking.

**[P-L-B2] (DEC paragraph + open question): Low — endorse with sharpening note.**
Phrasing the relationship with DEC as an open question is the right move and averts overclaim. The specific speculation — that $\tilde K(u)$ might be a discrete exterior derivative applied to $u$ viewed as a 0-cochain on the tetrahedron's 1-skeleton — is plausible and indeed a fair structural conjecture: for a tetrahedron with vertices $\{1,2,3,4\}$, the DEC coboundary $d_0: C^0 \to C^1$ sends a vertex-cochain $u = (u_1,\ldots,u_4)$ to the edge-cochain $(d_0 u)_{ij} = u_j - u_i$; these are exactly the six cyclic differences appearing as the off-diagonal entries of $\tilde K(u)$. So the conjecture is not false on its face.

*Nit (Low):* strictly, the entries of $\tilde K(u)$ are the *values* of $d_0 u$ on edges, but assembling them into a $4\times 4$ *operator* on 0-cochains requires an additional piece of structure (a sharp operator / edge-to-vertex contraction). The sentence "admits a description as a discrete exterior derivative applied to $u$" slightly understates what is needed. Since it is phrased as an open question ("whether"), this is acceptable; if the authors want to be fully airtight a parenthetical "(possibly combined with an edge-to-vertex contraction)" would do it.

**[P-M-B3] (descent proof expansion): endorse the chain; Medium nit on one elided step.**
The core chain
$$R^\top G R \;=\; \exp(-\theta K)\,G\,\exp(\theta K) \;=\; G\,\exp(-\theta K)\,\exp(\theta K) \;=\; G$$
is correct under the hypothesis $GK = KG$, and the logical skeleton ("commutation with $K$ ⇒ commutation with every power ⇒ commutation with $\exp(\theta K)$") is sound. Specifically:

- $R^\top = \exp(\theta K)^\top = \exp(\theta K^\top) = \exp(-\theta K)$, using that matrix transpose is a continuous algebra anti-involution that commutes with the power series defining $\exp$, together with $K^\top = -K$ (Definition 3.1 / Remark 3.2). ✓
- $G$ commutes with every polynomial in $K$ by an induction on degree from $GK = KG$ (Remark 3.2(1)); the convergent power series $\exp(\theta K) = \sum_{j\geq 0} (\theta K)^j/j!$ then commutes with $G$ because matrix multiplication is continuous, so $G \exp(\theta K) = \exp(\theta K) G$, equivalently $\exp(-\theta K) G = G \exp(-\theta K)$. ✓
- Substituting: $\exp(-\theta K) G \exp(\theta K) = G \exp(-\theta K) \exp(\theta K) = G \cdot I = G$. ✓

*Medium nit on one skipped step.* The proposed insertion writes $R^\top G R = \exp(-\theta K)\, G\, \exp(\theta K)$ as if the identification $R^\top = \exp(-\theta K)$ were self-evident. It is not — it requires $\exp(A)^\top = \exp(A^\top)$ (continuity of transpose through the series) plus $K^\top = -K$. Given that the whole point of the expansion is to close an "easy to see" gap, I recommend inserting a short parenthetical, e.g.

> "…since $G$ commutes with $K$ it commutes with every power and hence, by continuity of matrix multiplication, with $\exp(\theta K) = R$; together with $R^\top = \exp(\theta K)^\top = \exp(-\theta K)$ (using $K^\top = -K$), this gives $R^\top G R = \exp(-\theta K)\,G\,\exp(\theta K) = G\,\exp(-\theta K)\,\exp(\theta K) = G$;"

With that sentence, the derivation is self-contained at the formalism level. Without it, the expansion has replaced one "easy to see" with another.

**[P-H-B4] (§7 renormalization paragraph): High — the general correction is right, but the prescription is formally wrong for the object in play.**

The proposal correctly identifies that the current manuscript's claim "does not require renormalization after composition (no drift off a unit hypersphere, since $\tilde R$ is computed algebraically from a zero-sum unit axis)" is true only in exact arithmetic; in floating point, iterated composition of any rotation matrix drifts. This is a real bug in the current text and must be fixed. However, the replacement text prescribes

> "periodic re-orthogonalization of $\tilde R$ — for instance by QR or Gram–Schmidt applied to the reduced $3\times 3$ matrix"

and this prescription is not correct for the specific object $\tilde R$ of §7.2. The reduced matrix $\tilde R_{ij} = R_{ij} - R_{ip}$ (for $i,j \in \{l,n,m\}$) is, per the manuscript's own §7.3, "the rotation $R$ expressed in a three-vector (non-orthonormal) basis of $H$ obtained by picking three of the four simplicial basis vectors and absorbing the fourth into the zero-sum constraint." A rotation expressed in a non-orthonormal basis is *not* an orthogonal matrix, so $\tilde R^\top \tilde R \neq I_3$ in general. A quick sanity check against the worked example in §5.4 / Appendix D confirms this: with $u = (a,a,-a,-a)$, $\theta = 2\pi/3$, and $R$ as displayed, the reduced matrix has first row $((1-\sqrt 3)/4,\ (3-\sqrt 3)/4,\ -\sqrt 3/2)$ whose squared norm is $7/4 - \sqrt 3/2 \approx 0.884 \neq 1$.

Consequently, standard QR or classical Gram–Schmidt applied to $\tilde R$ as a $3\times 3$ array of real numbers would project it onto the manifold $\mathrm{O}(3)$, which is *not* the manifold of admissible reduced matrices. The correct re-orthogonalization procedure must respect the metric induced on the reduced-coordinate triple $(P_l, P_n, P_m)$ by the simplicial inner product after eliminating $P_p = -(P_l + P_n + P_m)$ — i.e., it must use the weighted inner product with Gram matrix $M = I_3 + \mathbf{1}_3 \mathbf{1}_3^\top$ (up to the $4/3$ prefactor), or equivalently one must lift $\tilde R$ back to the $4\times 4$ matrix $R$ and re-impose $R^\top R = I_4$, $R\mathbf{1} = \mathbf{1}$, before reducing.

Recommended minimal fix: replace the example prescription with something like

> "…requires periodic re-enforcement of the manifold constraint. A natural recipe is to lift the reduced matrix back to the $4\times 4$ gauge-compatible $R$ and re-impose $R^\top R = I$ together with $R\mathbf{1} = \mathbf{1}$, which can be done by a Gram–Schmidt pass in the appropriate weighted inner product. The cost is comparable to, but somewhat more expensive than, renormalizing a unit quaternion."

Additionally, the phrase "as with any matrix representation of rotations" is slightly over-broad: a Cartesian $3\times 3$ rotation matrix *can* be re-orthogonalized by standard QR/GS, whereas the simplicial reduced $\tilde R$ cannot — the *method* depends on the representation, even though the *phenomenon* (drift under composition) is universal. Suggest softening to "as with any matrix representation of rotations in floating-point arithmetic, iterated composition accumulates error; restoring the manifold constraint on $\tilde R$ requires a representation-specific re-orthogonalization…"

This is the only finding I would consider a blocker in its current wording. It is easily patched.

**[P-L-B5] (ilr paragraph): endorse; Low note on one wording.**
The composition described — $\text{ilr} = V \circ c^{\mathrm{zs}} \circ \log$, where $V$ is a choice of orthonormal basis on the clr hyperplane $H$ — matches the standard Aitchison-geometry construction: clr = (log then centering, i.e., zero-sum projection of the componentwise log), ilr = (clr followed by an orthonormal basis transformation $H \to \mathbb{R}^{N-1}$). The ordering in the proposal ("component-wise log map with the zero-sum projection $c \mapsto c^{\mathrm{zs}}$ of §2.3 followed by a choice of orthonormal basis on $H$") is correct. The "structurally the composition" hedge is actually stronger-than-needed — the equality really does hold on the nose for a suitable choice of basis. If a reviewer wants to drop the hedge, they may; if kept, it is harmless. No formalism blocker. The Fisher-Rao → Fisher–Rao en-dash fix is uncontroversial.

**[P-M-B6] (§9 reframing): endorse the direction; Medium on terminology and Medium on section-pointer + downstream consistency.**

*Direction endorsed.* The current §9 paragraph ("not merely a reparameterization … autonomous arena") does overreach: by Theorem 4.1 together with §2.5/§3.4, the simplicial system on $H$ is isometric to Euclidean $\mathbb{R}^3$, so on the intrinsic-equivalence layer there is *no* mathematical content beyond classical 3D vector calculus — the novelty is in the concrete presentation (cyclic-difference $K$, $4\times 4$ lift into $\mathrm{SO}(4)\cap\mathrm{Stab}(\mathbf 1)$, 9-mul kernel). The reframing is defensible and, in my view, strengthens the paper.

*Two Medium nits on execution.*

1. *Terminology — "unitarily equivalent".* In the real-inner-product-space setting relevant here, the technically precise term is "*orthogonally* equivalent" or simply "isometric via $V$". "Unitary" is sometimes used loosely as a synonym, but is strictly reserved for complex-inner-product spaces in most formal writing. A pedantic reviewer will flag this. Suggest "isometric to classical 3D vector calculus under the hyperplane isometry $V: H \to \mathbb{R}^3$" or "conjugate by the orthogonal isomorphism $V$".

2. *Section pointer for $V$.* The proposal writes "the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5". However, §2.5 of the current manuscript introduces $V$ only as a forward reference: "…under the isometry $V\colon H \to \mathbb{R}^3$ of §3.4". §3.4 then describes the isometry structurally (as any realization of $(H, \langle\cdot,\cdot\rangle)$ as oriented Euclidean $\mathbb{R}^3$ via the Hodge construction) but does not explicitly name it. So $V$ is introduced *by name* in §2.5 but *by construction* in §3.4. Either (a) change B6's attribution to "§3.4" (or "§2.5/§3.4"), or (b) plan a light edit to §2.5 that promotes the forward reference into a local definition of $V$. Pick one; as written, the cross-reference is slightly unstable.

*Downstream consistency sweep (Medium).* If B6 lands, the abstract ("once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame") and §1.2 item 3 (the "intrinsic … no ongoing reference to an ambient Cartesian embedding" framing) remain. These are not inconsistent with B6 — "no ongoing reference to a Cartesian frame" is a *presentation* claim and is still true — but the deliberate narrowing from "autonomous arena" to "autonomous presentation" in §9 should be audited against Remark 4.2 ("…supports this algebraic layer of vector calculus on its own terms") and §2.3's "Operationally, the zero-sum hyperplane is the canonical gauge…" paragraph. Neither of those needs editing on a strict reading — they speak of *operators* being well-defined intrinsically, not of *mathematical content* being novel — but an Author sweep ensuring the word "autonomous" is used consistently (presentation, not arena) would prevent a future reviewer from pulling on this thread.

**[P-L-C1] (FEEC §8.3 sentence): endorse; Low nit on the framing.**
"FEEC on tetrahedral meshes" is a real and active domain [Arnold-Falk-Winther]; "pointwise algebraic operations on tetrahedral elements without reference to a global Cartesian frame" is defensible specifically because of the word *global*: FEEC computations are already element-local in the sense that the relevant bilinear forms are assembled per-element and can be implemented without a global Cartesian frame. What FEEC practice typically *does* use per element is a reference-to-physical affine map (essentially a local Cartesian embedding of the reference element). So the honest reading is: the simplicial operators developed here offer the possibility of element-local operations computed in *barycentric-style simplicial coordinates* with no local Cartesian embedding either — which is a genuinely new twist, but not quite what the sentence says verbatim. The phrasing "could in principle supply" is already appropriately hedged. Not a blocker. If sharpening: "…without reference to a global Cartesian frame, and — in the case where the simplicial cross product and rotation are exploited directly on the element — without a local affine reference-to-physical map either."

**[D1] Arnold–Falk–Winther, *Acta Numerica* 15, 1–155 (2006): endorse.**
Real paper, title accurate, volume and year correct, author list correct. Pagination 1–155 matches the survey. Endorse.

**[D2] Desbrun–Hirani–Leok–Marsden, arXiv:math/0508341 (2005): endorse.**
Title "Discrete Exterior Calculus" correct, author list correct, arXiv identifier matches (the paper is in math.DG, registered 2005). Endorse.

**[D3] Pawlowsky-Glahn–Egozcue–Tolosana-Delgado, *Modeling and Analysis of Compositional Data*, Wiley 2015, Statistics in Practice: endorse.**
Real book, series correct, publisher correct, year correct, three-author team correct. The citation-key `[Pawlowsky-Glahn-Egozcue]` truncates the third author (Tolosana-Delgado); consistent with the paper's existing two-name key convention (e.g. `[Brenner-Scott]`, `[Marsden-Ratiu]`, `[Müller-Regensburger]`), so not a defect, just noting the author-list in the body will need all three.

## Summary of findings by ID

- Critical: none.
- High: `[P-H-B4]` — re-orthogonalization prescription on the reduced $3\times 3$ $\tilde R$ is formally incorrect as stated; replace with weighted/lifted re-orthogonalization.
- Medium: `[P-M-B3]` — insert the $R^\top = \exp(-\theta K)$ identification step explicitly; `[P-M-B6a]` — "unitarily" → "isometrically/orthogonally"; `[P-M-B6b]` — section pointer and downstream consistency sweep.
- Low: `[P-L-B1]`, `[P-L-B2]`, `[P-L-B5]`, `[P-L-C1]`, plus the minor author-key note on D3.

## Downstream consistency sweeps these edits force

1. If B6 lands with "autonomous *presentation*" in §9, a light pass is warranted across (a) the abstract's "intrinsic algebraic vector calculus" language, (b) §1.2 item 3, and (c) Remark 4.2 to ensure "autonomous" consistently means *autonomous presentation of the algebraic layer*, not *autonomous mathematical arena*.
2. If A1 lands in all four sites, also verify the isolated phrase "$\dim \mathfrak{so}(3) = 3$" in §8.1 and §9 (these are kept; A1 doesn't touch them) still reads cleanly after the Abstract / §1.2 / §3 / §8.1 iso sentences are rewritten.
3. If B4 lands, a cross-reference check with the §7.4 table is worth doing — the "multiplications/apply" column still reports 9 multiplications for the intrinsic simplicial row, which is compatible with B4's rewrite (B4 is about a *separate, occasional* re-orthogonalization step, not the per-apply cost). Author may wish to annotate the table footnote to say so explicitly.

STATUS: AMBER
