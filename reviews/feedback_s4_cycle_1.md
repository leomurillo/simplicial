# Synthesis — §4 Cycle 1
**Scope:** §4 Gauge-Compatibility and Descent to the Zero-Sum Quotient (lines 273–289)
**Date:** 2026-04-20
**Status:** AMBER (2 Reviewer X High, 2 Reviewer Y High; no Critical; Author revision required)

## Inputs
- `feedback_s4_cycle_1_reviewer_x.md` — 0 Critical, 2 High, 3 Medium, 2 Low
- `feedback_s4_cycle_1_reviewer_y.md` — 0 Critical, 2 High, 3 Medium, 2 Low

## Blocking items (must be resolved to reach GREEN)

### Descent logic tightening (Formalism High)
- **[F-H-1]** — inner-product invariance needs to be stated in **both slots**: $\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$. Requires one-line derivation via $\mathbf{1}^\top G = (G\mathbf{1})^\top = 0$ from symmetry of $G$.
- **[F-H-2]** — cross-product and rotation descent currently establishes gauge-compatibility only in the *input* $P$; for well-definedness of the quotient operator in its *axis* argument, also need $K(u + k\mathbf{1}) = K(u)$ (equivalently $R(u + k\mathbf{1},\theta) = R(u,\theta)$). The two-line derivation follows from Remark 3.2 linearity-in-$u$ + $K(\mathbf{1}) = 0$, but must be stated in §4.

### Narrative fixes (Narrative High)
- **[N-H-1]** — Theorem 4.1(ii) writes "for each zero-sum unit axis $u$" then invokes "$K(\mathbf{1}) = 0$" — $\mathbf{1}$ is neither zero-sum nor unit. The invocation relies on the formal linear extension of §3.2 Remark 3.2; add an explicit pointer.
- **[N-H-2]** — replace the awkward "(presently) the exponential map" hedge on line 275 with a clean forward reference, e.g. "the exponential map (constructed in §5)".

## Strongly recommended (non-blocking)
- **[F-M-1]** — state explicitly that $H$ is closed (as a finite-dimensional subspace), to close the partial-sum → limit argument for $R(H) \subseteq H$.
- **[F-M-2]** — emphasize **simplicial orthogonality** $R^\top G R = G$ as the intrinsic, descent-relevant isometry statement; demote $R^\top R = I$ to an ambient lift. The commutation $GK = KG$ (Remark 3.2(1) in §3) is the ingredient.
- **[F-M-3]** — fix "bilinear in its axis argument" → "linear in the axis argument" (or "bilinear in $(u, P)$" if that is the intended object). $K: u \mapsto K(u)$ is linear, not bilinear.
- **[N-M-1]** — remove or trim the redundant scope disclaimer at the end of Remark 4.2; keep one clean statement in the opening paragraph (line 275).
- **[N-M-2]** — anchor the "rigid-body mechanics" framing of Remark 4.2 with a canonical citation (Arnold, or Marsden–Ratiu).
- **[N-M-3]** — break up the long em-dash clause in Remark 4.2 (line 287).
- **[F-L-1]** — recall the zero-sum hyperplane $H$ (§2.3) as the canonical representative of $\mathbb{R}^N / \langle \mathbf{1}\rangle \cong \mathbb{R}^{N-1}$.
- **[F-L-2]** — tighten "all three operators" — inner product is a bilinear form, not an endomorphism. Prefer "operations" or distinguish explicitly.
- **[N-L-1]** — regularize theorem-clause formatting (currently mixes bullets and italicized roman numerals).
- **[N-L-2]** — add a one-phrase callback to §2.2.1 to enrich the descent's literature positioning (information geometry / CRNT).

## Propagation check (preemptive, per authorship-orchestration skill)

Retired / narrowed phrasings the Author will introduce:
- "(presently) the exponential map" → clean forward reference
- "bilinear in its axis argument" (applied to the single-argument map $u \mapsto K(u)$) → "linear in the axis argument"
- single-slot inner product invariance (first-slot only) → two-slot invariance

Author should grep for each retired phrasing across the full manuscript and either sweep immediately (with a `### Propagation check` subsection in the triage) or log pending to `reviews/open-issues.md`.

## Author triage

Post-edit line numbers refer to the revised `simplicial_vector_calculus.md`.

### Blocking findings

- **[F-H-1] Two-slot inner-product invariance — Accepted.** Rewrote clause (1) of Theorem 4.1 (line 279) to state both-slot gauge invariance $\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = \langle a, b\rangle$. Proof sketch (lines 285–286) now derives $\mathbf{1}^\top G = (G\mathbf{1})^\top = \mathbf{0}^\top$ from symmetry of $G$ and expands the full four-term bilinear computation.
- **[F-H-2] Axis-variable independence for $K$ and $R$ — Accepted.** Clause (2) (line 280) now closes with "$K$ depends only on the axis class, $K(u + k\mathbf{1}) = K(u)$ for every $k \in \mathbb{R}$," obtained via Remark 3.2 linearity and $K(\mathbf{1}) = 0$. Clause (3) (line 281) adds $R(u + k\mathbf{1},\theta) = R(u,\theta)$. Proof sketch supplies $K(u + k\mathbf{1}) = K(u) + k\,K(\mathbf{1}) = K(u)$ explicitly (line 287).
- **[N-H-1] Domain signposting for $K(\mathbf{1}) = 0$ — Accepted-with-variant.** Rather than splitting clause (2) into two sentences, kept it as a single clause but made the domain shift explicit by opening the second half with "Moreover, under the formal linear extension of $K$ to all of $\mathbb{R}^4$ (Remark 3.2), $K$ is linear in its axis argument and $K(\mathbf{1}) = 0$." The unit-axis hypothesis at the start still scopes the hyperplane-closure and annihilation claims; the pointer to Remark 3.2 prevents the domain leap from looking unjustified. Post-edit location: line 280.
- **[N-H-2] Remove "(presently)" hedge — Accepted.** Line 275 now reads "…and the exponential map (constructed in §5)…".

### Strongly recommended (non-blocking)

- **[F-M-1] Closed-subspace step for $R(H) \subseteq H$ — Accepted.** Proof sketch (line 287) now specifies "each partial sum $\sum_{j=0}^n (\theta K(u))^j/j!\, P$ lies in $H$ for $P \in H$, and $H$ is a closed finite-dimensional subspace of $\mathbb{R}^4$, so the limit remains in $H$."
- **[F-M-2] Simplicial orthogonality as primary statement — Accepted.** Proof sketch (line 287) now foregrounds $R^\top G R = G$ (equivalently $\langle RP, RQ\rangle = \langle P, Q\rangle$) as the intrinsic, descent-relevant isometry, citing the commutation $GK(u) = K(u)G$ from Remark 3.2(1), and relegates $R^\top R = I$ and $\det R = +1$ to "ambient Euclidean lift" established in §§5–6.
- **[F-M-3] "Bilinear" → "linear" in axis argument — Accepted.** Clause (2) (line 280) and the proof sketch (line 287) now say "linear in its axis argument" / "linearity in the axis." The bilinear object $(u, P) \mapsto K(u)P$ remains named as such in §3.2 lines 224, 237, where that phrasing is correct.
- **[N-M-1] Trim redundant scope disclaimer — Accepted.** Remark 4.2 (line 289) no longer repeats the scope disclaimer; the single authoritative iteration stays at line 275.
- **[N-M-2] Anchor rigid-body framing — Accepted.** Added `[Arnold, Marsden-Ratiu]` citation in Remark 4.2 (line 289). Added both references to the bibliography: `[Arnold]` Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer 1989; `[Marsden-Ratiu]` Marsden & Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer 1999.
- **[N-M-3] Break up em-dash clause in Remark 4.2 — Accepted.** The overloaded em-dash sentence was replaced by two sentences in Remark 4.2 (line 289): "This is the algebraic content of §1.2 item 3: once the simplicial Gram data of §2 is fixed, the formulas for these operations require no ongoing reference to a Cartesian embedding. The simplicial (Quadray) description of 3D Euclidean space thereby supports this algebraic layer of vector calculus on its own terms."
- **[F-L-1] Canonical representative — Accepted.** Descent paragraph (line 283) now reads "…the quotient $\mathbb{R}^N/\langle\mathbf{1}\rangle \cong \mathbb{R}^{N-1}$, canonically realized by the zero-sum hyperplane $H$ of §2.3…".
- **[F-L-2] "Operators" → more precise — Accepted.** Descent paragraph (line 283) now distinguishes explicitly: "the simplicial bilinear form, cross-product operator, and rotation." The opening paragraph (line 275) uses "operations" throughout.
- **[N-L-1] Regularize theorem-clause formatting — Accepted.** Changed the three clauses (lines 279–281) from mixed bullets/italicized roman numerals (`- *(i) …*`) to a numbered list with italicized bodies (`1. *(Scalar invariance.) …*`), matching the convention of Proposition 6.1.
- **[N-L-2] Literature callback for descent — Accepted.** Descent paragraph (line 283) closes with "…the same quotient that plays the organizing role across the structural parallels recorded in §2.2.1 (information geometry and chemical reaction network theory)."

### Propagation check (out-of-§4)

Grep results on the full manuscript (post-edit):

- `(presently)` (hedge form): **0 matches** anywhere. Clean.
- `bilinear in its axis argument`: **0 matches** anywhere. Clean. Other occurrences of "bilinear" refer to the correct object $(u, P) \mapsto K(u)P$ (line 224), the bilinear form on $H \times H \to H$ (line 237), or the generic "skew-symmetric bilinear operator" phrasing in the abstract/introduction, all of which describe the two-argument object and remain correct.
- Single-slot inner-product invariance: pre-edit, line 153 (§2.4) had prose "invariant under gauge shifts of either argument" but the symbolic expression showed only $\langle a + k\mathbf{1}, b\rangle = \langle a, b\rangle$. **Swept**: line 153 now gives the two-slot form $\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = \langle a, b\rangle$ for all $k, m \in \mathbb{R}$, with the one-line derivation via symmetry of $G$, keeping §2.4 symbolically aligned with the §4 descent claim.

No propagation-pending items logged to `reviews/open-issues.md`; all three retired phrasings were either absent elsewhere or swept in this cycle.
