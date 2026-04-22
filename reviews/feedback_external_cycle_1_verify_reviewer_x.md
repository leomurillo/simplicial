# Reviewer X — Verification pass on external-review cycle 1 implementation

**Scope.** Verification-only re-audit of the sites edited by the Author per `feedback_external_cycle_1_author_triage.md` against the four formalism items I flagged in `feedback_external_cycle_1_reviewer_x.md` (`[P-H-B4]`, `[P-M-B3]`, `[P-M-B6a]`, `[P-M-B6b]`), plus spot-checks of the remaining proposals (A1×4, B1, B2, B5, C1, D1–D3), the Remark 4.2 tonal edit, and regressions at the edited sites.

## Verdict per flagged ID

### `[P-H-B4]` — §7.4 renormalization paragraph — **RESOLVED.**

The current §7.4 now reads:

> "…is constructed algebraically from a zero-sum unit axis rather than as a point on a unit hypersphere, and operates without the non-commutative hypercomplex algebra of Hamilton products. As with any matrix representation of rotations **in floating-point arithmetic**, iterated composition accumulates error and requires periodic re-enforcement of the manifold constraint. Because $\tilde{R}$ is the rotation expressed in a non-orthonormal basis of $H$ (§7.3), $\tilde{R}^\top \tilde{R} \neq I_3$ in general, so **standard QR/Gram–Schmidt on $\tilde{R}$ alone is formally inappropriate**; the correction is representation-specific. A natural recipe is to **lift $\tilde{R}$ back to the $4 \times 4$ gauge-compatible $R$ and re-impose $R^\top R = I$ together with $R\mathbf{1} = \mathbf{1}$**, via a Gram–Schmidt pass in the simplicial inner product…"

This replaces the original QR/GS-on-$\tilde R$ prescription with the correct lift-and-re-impose recipe I recommended. The over-broad "as with any matrix representation of rotations" is softened to "…in floating-point arithmetic"; the representation-specific nature of the *method* is spelled out. Sanity check: the row-1 squared ambient-norm of $\tilde R$ in the §5.4/App. D worked example is $7/4 - \sqrt 3/2 \approx 0.884 \neq 1$, and the revised text acknowledges this directly via $\tilde{R}^\top\tilde{R}\neq I_3$.

The §7.4 table footnote reads: *"The 'multiplications / apply' column reports per-apply cost only; periodic re-orthogonalization under repeated composition (discussed below) adds an amortized cost comparable to quaternion renormalization and is orthogonal to the per-apply figure."* Prevents conflation of the 9-mul per-apply cost with the occasional re-orthogonalization step. RESOLVED with one new Low finding (see `[V-L-1]`).

### `[P-M-B3]` — descent-theorem proof expansion — **RESOLVED.**

The edit landed in Theorem 4.1's proof (not §3 as the proposal loosely said):

> "…which follows from the commutation $GK(u) = K(u)G$ (Remark 3.2(1)): since $G$ commutes with $K$ it commutes with every power of $K$ and hence, **by continuity of matrix multiplication**, with $\exp(\theta K) = R$; combined with **$R^\top = \exp(\theta K)^\top = \exp(-\theta K)$ (using $K^\top = -K$, Definition 3.1)**, this gives $R^\top G R = \exp(-\theta K)\, G\, \exp(\theta K) = G\, \exp(-\theta K)\, \exp(\theta K) = G$;"

Every step I flagged is present: (i) the "commutation-with-$K$ ⇒ commutation-with-every-power ⇒ commutation-with-$\exp(\theta K)$" skeleton with explicit appeal to continuity of matrix multiplication; (ii) the $R^\top = \exp(-\theta K)$ identification with its justification from $K^\top = -K$; (iii) the equality chain $R^\top G R = \exp(-\theta K)\,G\,\exp(\theta K) = G\,\exp(-\theta K)\,\exp(\theta K) = G$. No "easy to see" gap remains. RESOLVED.

### `[P-M-B6a]` — terminology "isometric" vs "unitarily equivalent" — **RESOLVED.**

§9 paragraph 2 now reads: *"The construction is **isometric** to classical 3D vector calculus under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4)…"* "Unitarily equivalent" has been excised. The lone remaining "unitar"-stem is in Appendix B Step 3: *"Real skew-symmetric matrices are normal … hence unitarily diagonalizable over $\mathbb{C}$ by the spectral theorem for normal operators"* — standard normal-matrix terminology with explicit complex-field annotation, unrelated to B6a. RESOLVED.

### `[P-M-B6b]` — §2.5 definition of $V$ — **RESOLVED.**

§2.5 now introduces $V$ by local definition:

> "under the *hyperplane isometry* $V\colon H \to \mathbb{R}^3$ defined by $V(c) := \sum_{i=1}^4 c_i \mathbf{v}_i$ (so that $V$ sends the simplicial coordinate tuple $c \in H$ to the corresponding Cartesian point in the ambient $\mathbb{R}^3$); the structural characterization of $V$ as an orientation- and metric-preserving realization of $(H, \langle\cdot,\cdot\rangle)$ as Euclidean $\mathbb{R}^3$ via the Hodge construction is taken up in §3.4. Concretely, $V K(u) V^{-1} = [Vu]_\times$ for every $u \in H$…"

**Mathematical well-formedness.** Let $c, c' \in H$. The simplicial inner product is $\langle c, c'\rangle = c^\top G c' = \sum_{i,j} c_i c'_j (\mathbf{v}_i\cdot\mathbf{v}_j)$, while $V(c)\cdot V(c') = (\sum_i c_i \mathbf{v}_i)\cdot(\sum_j c'_j \mathbf{v}_j) = \sum_{i,j} c_i c'_j (\mathbf{v}_i\cdot\mathbf{v}_j) = \langle c, c'\rangle$. So $V|_H$ preserves inner products. Injectivity: $\ker V$ in $\mathbb{R}^4$ is $\operatorname{span}(\mathbf{1})$ (by the balancing identity $\sum\mathbf{v}_i = 0$), and $\operatorname{span}(\mathbf{1})\cap H = \{0\}$. Dimension count: $\dim H = 3 = \dim\mathbb{R}^3$, so $V|_H$ is a bijective isometry. Cross-reference from §9 to "§2.5 (cf. §3.4)" resolves cleanly. Consistency with §3.4: §3.4 speaks of "any such isometry" (non-canonical); §2.5 fixes the labeling. RESOLVED.

## Spot checks on remaining proposals

- **A1 (four sites).** Abstract, §1.2 item 6, §3 opening, §8.1 closing — all four carry the `$\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$` with "Lie-algebra" hyphen; isolated `$\dim \mathfrak{so}(3) = 3$` phrases in §8.1 / §9 still read cleanly. Ripgrep for the bare `\mathfrak{so}(3) \cong \mathbb{R}^3` returns zero hits. ✓
- **B1.** §1.2 item 6 contains the octonion sentence with my Low sharpening ("simplicial wedge–Hodge construction of §3.4" instead of "wedge–Hodge duality"). ✓
- **B2 + C1.** §1.3 now reads: header → DEC paragraph (with my "possibly combined with an edge-to-vertex contraction" Low parenthetical) → FEEC paragraph → existing terminology / Rodrigues / Low-$N$ paragraphs. Citation keys match Reference entries. ✓
- **B5.** §8.3 label "Information geometry and compositional data" present, Aitchison sentences with correct ilr composition, Fisher–Rao en-dash, `[Pawlowsky-Glahn-Egozcue]` key matches. ✓
- **D1–D3.** `[Arnold-Falk-Winther]` between `[Arnold]` and `[Brenner-Scott]`; `[Desbrun-Hirani-Leok-Marsden]` between `[Ciarlet]` and `[Eckmann]`; `[Pawlowsky-Glahn-Egozcue]` between `[Müller-Regensburger]` and `[Spivak]`. Bibliographic fields match what I endorsed. ✓

## Remark 4.2 tonal edit

Final sentence of Remark 4.2 now reads: *"The simplicial (Quadray) description of 3D Euclidean space thereby supports an autonomous *presentation* of this algebraic layer of vector calculus, in the sense made precise in §9: isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5, but formulated and computed without passing through a Cartesian frame."* Tonal; introduces no new mathematical claim requiring independent proof. No formalism regression.

## Regression checks

1. Numbered equation references: only (5.1), referenced as "(5.1)" later; no breakage.
2. Remark 3.2 pointer to Theorem 4.1(ii) vs. 4.1(2) — pre-existing Roman/Arabic inconsistency, not introduced by this cycle.
3. §1.3 structure is clean (header, five paragraphs, no orphans).
4. Cross-reference chain for $V$: §2.5 defines → §3.4 characterizes → §9 cites back to §2.5; no cycle, no dangling forward reference.
5. "Autonomous" now appears only in §9 and Remark 4.2 as "autonomous *presentation*". "Not merely a reparameterization" removed. "Arena" occurrences in §1.1 and §2.3 do not attach autonomy claims and are fine.

## New findings

- **`[V-L-1]` (Low).** §7.4: *"via a Gram–Schmidt pass in the simplicial inner product"* is slightly imprecise. The constraint to re-impose on the lifted matrix is $R^\top R = I$ in the **ambient** Euclidean inner product (with $R\mathbf{1}=\mathbf{1}$), not the simplicial $G$-inner product on $\mathbb{R}^4$. $G = \tfrac{4}{3}I - \tfrac{1}{3}J$ is singular on all of $\mathbb{R}^4$ (null on $\operatorname{span}(\mathbf{1})$), so "Gram–Schmidt in the simplicial inner product" on $\mathbb{R}^4$ is ill-defined as literally stated. The saving grace is that on $H$ the simplicial form is $\tfrac{4}{3}I_H$, so $G$-orthonormalization on the hyperplane block differs from standard Euclidean GS only by a global scale. Non-blocking; recommend a parenthetical "(equivalently, standard Gram–Schmidt applied to the columns of the hyperplane block of $R$)" or reversion to "in the appropriate weighted inner product".

- **`[V-L-2]` (Low, stylistic).** §9: *"The construction is isometric to classical 3D vector calculus…"* — strictly, "classical 3D vector calculus" is a body of identities, not a metric space, so "isometric to X" is a mild stylistic abuse. Read informally as "isometric to the classical realization on $\mathbb{R}^3$ of the (inner-product, cross-product, rotation) triple" it is unambiguous. Non-blocking.

## Summary of findings by ID

- Critical: none.
- High: none. `[P-H-B4]` RESOLVED.
- Medium: none. `[P-M-B3]`, `[P-M-B6a]`, `[P-M-B6b]` all RESOLVED.
- Low: two new minor items — `[V-L-1]`, `[V-L-2]`. Neither blocks.

STATUS: GREEN
