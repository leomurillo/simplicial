# §8 Cycle 2 — Author triage record

**Scope.** Surgical Cycle 2 revision of §8 ("Higher Dimensions and Future Work") under human-authorized Option A: clear the three Cycle 1 Highs and four Mediums in a single Author pass; Lows at Author discretion.

**File edited:** `simplicial_vector_calculus.md` (§8 at lines ~453–483). No References changes required — Wildberger, Pawlowsky-Glahn-Egozcue, and Müller-Regensburger were already present from prior cycles; no analog-gravity or Kanerva/HDC reference introduced because the Option-A physics-applications trim drops those items.

---

## Highs landed (all three)

### `[S8-Y-H-1]` — §8 opening bridging paragraph (Reviewer Y, High)

**Landed.** Inserted a new top-of-§8 paragraph (immediately after the `## 8. Higher Dimensions and Future Work` heading and before `### 8.1 The uniqueness of $N = 4$`):

> Having established the $N = 4$ framework end-to-end — intrinsic operators (§§3–5), structural properties (§6), and a 9-multiplication apply kernel (§7) — we now step back to ask which features of the construction are specific to $N = 4$ and which remain open for higher dimensions or adjacent mathematical programs.

The sentence cushions the §7 → §8 transition from applied/computational back to structural/algebraic, matching the "framing-then-argument" pattern used at the start of §4 and §9.

### `[S8-H-1]` — Correct the "$N \geq 5$" obstruction paragraph (Reviewer X, High)

**Landed.** Replaced the old §8.1 middle paragraph wholesale. The replacement corrects two errors simultaneously:

- Drops the incorrect claim that higher-$N$ wedge–Hodge generators are "rank greater than 2." The new text explicitly states that a wedge of simplicial vectors is decomposable, its Hodge dual is a simple 2-form, and the associated skew operator is rank 2 for all $N \geq 4$ — so the Rodrigues formula applies to each *blade* generator individually.
- Replaces the "higher-degree minimal polynomial" pseudo-obstruction with the correct Lie-theoretic obstruction: for $N - 1 \geq 4$, $\dim \mathfrak{so}(N-1) = \binom{N-1}{2} > N - 1$, so a generic element of $\mathfrak{so}(N-1)$ is a linear combination of non-commuting blade generators, whose matrix exponentials do not refold into a single trigonometric closed form.

Per the user-supplied direction, the rewrite also subsumes what was previously the opening sentence of the *next* paragraph (the $\binom{N-1}{2} > N - 1$ dimension count), so the following paragraph no longer restates the same Lie-algebra point — see `[S8-M-1]` below.

### `[S8-H-2]` — Restrict the fixed-subspace claim to simple rotations (Reviewer X, High)

**Landed (folded into the `[S8-H-1]` rewrite).** The corrected text now says:

> Each individual blade-generated rotation fixes a subspace of dimension $(N-1) - 2 = N - 3$, strictly less than the $N - 2$ that a single 1-parameter rotation family in the 3D sense would require.

The grammatical subject is now "each individual blade-generated rotation" (i.e., the image under $\exp$ of a single rank-2 generator — a simple rotation), which is the scope where $N - 3$ holds. The false blanket statement "Rotations in $\mathrm{SO}(N-1)$ … have fixed subspaces of dimension $N-3$" has been removed.

---

## Mediums landed (all four)

### `[S8-M-1]` — "Within our framework" hedge on the uniqueness claim (Reviewer X, Medium)

**Landed.** Rewrote the former second paragraph of §8.1 (the one beginning "The uniqueness of $N = 4$ …"). Three compound changes:

- Added the *italicized* hedge "within the simplicial wedge–Hodge framework developed here," mirroring the phrasing of §1.2 item 6 (line 61).
- Appended an explicit Eckmann / octonion disclaimer and a cross-reference back to §1.2 item 6:
  > The $n = 7$ octonionic binary cross product admitted by Eckmann's classification arises from a different algebraic structure (non-associative division algebras) and lies outside the framework of this paper (§1.2 item 6).
- Dropped the now-redundant final sentence "The coincidence fails for $\mathfrak{so}(d)$ with $d \geq 4$, where $\dim \mathfrak{so}(d) = \binom{d}{2} > d$." The same dimensional point is made (correctly and with more load-bearing weight) in the `[S8-H-1]` rewrite of the preceding paragraph.

Net effect: §8.1's closing paragraph is now a single-point observation about $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ and its classification-based context, not a restatement of the obstruction.

### `[S8-M-2]` — Detach Weierstrass from Wildberger (Reviewer X, Medium)

**Landed.** In §8.3 Rational Trigonometry paragraph, replaced "Substituting Wildberger's Weierstrass parameter $t = \tan(\theta/2)$" with:

> Substituting the Weierstrass parameter $t = \tan(\theta/2)$ into our formula — in the spirit of Wildberger's program of rational trigonometry [Wildberger] — yields …

The Weierstrass substitution is now correctly unattributed (it is classical, 19th century), and Wildberger appears only as the author of the rational-trigonometry *program* the paragraph builds on. Cite placement anchors the attribution.

### `[S8-M-3]` + `[S8-Y-M-1]` (convergent) — Concretize "tetrahedral symmetry family" (both reviewers, Medium)

**Landed.** In §8.3 Rational Trigonometry paragraph, replaced the undefined "tetrahedral symmetry family" with the concrete candidate set recommended by Reviewer X and folded in a brief justification so that the subsequent "Characterizing precisely which axes admit the rational parameterization" sentence has a well-defined anchor:

> For axes $u \in H$ with $\sqrt{3}\,u \in \mathbb{Q}^4$ (equivalently, entries of $u$ in $\sqrt{3}\,\mathbb{Q}$), the entries of $K(u)$ are rational — the entries of $\tilde K(u)$ are differences of components of $u$, which lie in $\sqrt{3}\,\mathbb{Q}$, and the $1/\sqrt{3}$ in Definition 3.1 then clears — so $R(u, t)$ has rational entries for all rational $t$.

The open-question sentence ("Characterizing precisely which axes …") is retained unchanged; it now asks about a well-defined candidate set rather than an undefined family.

### `[S8-M-4]` + `[S8-Y-M-3]` (convergent) — Trim physics-applications paragraph (both reviewers, Medium)

**Landed (trim option, per Reviewer X's cleanest suggestion).** Renamed the paragraph header from "**Generalized physics applications.**" to "**Connections to other disciplines.**" and rewrote the body to keep only the structurally well-motivated CRNT case (already cited via `[Müller-Regensburger]`) and to explicitly note that other gauge-quotient settings (compositional data) share the metric but not obviously the rotation operator. Analog gravity and cognitive hyperdimensional computing were dropped entirely, which is why no Kanerva or Barceló-Liberati-Visser reference had to be added:

> **Connections to other disciplines.** Beyond the motivations already discussed, stoichiometric compatibility classes in chemical reaction network theory [Müller-Regensburger] exhibit the same gauge-direction plus zero-sum-hyperplane structure; whether the intrinsic rotation operator developed here has substantive content in that setting — as opposed to the static inner-product structure alone — is an open question. Other gauge-quotient settings (for example, probabilistic simplices in compositional data analysis, just discussed) share the metric but do not obviously benefit from an analog of $R(u,\theta)$.

The closing skeptical-tone sentence that both reviewers praised ("Whether any of these benefit substantively from the intrinsic rotation operator … is an open question") is preserved in slightly rephrased form, now attached specifically to the CRNT case where it carries weight.

### `[S8-Y-M-2]` + `[S8-X-L-3]` + `[S8-X-L-4]` (folded) — Simplify ilr description + Fisher up-to-scalar (both reviewers)

**Landed (all three folded into one sentence cluster).** Rewrote the §8.3 Information-geometry paragraph so that:

- The ilr map is described at the level of structural intent ("the ilr transformation maps the probability simplex to $H$ after a component-wise log, and the associated inner-product structure agrees up to a positive scalar with the simplicial inner product of §2.4") rather than as a full factorization, per `[S8-Y-M-2]` and `[S8-X-L-3]`.
- The Fisher claim is now correctly hedged "up to a positive scalar," with the parenthetical "since the Fisher metric is itself defined only up to positive rescaling" absorbing `[S8-X-L-4]`.

Result: the paragraph is lighter by roughly one dense clause and carries precise scalar-match claims where previously it carried an imprecise "pulls back to" claim.

---

## Lows taken (three — per recommendation)

### `[S8-X-L-2]` — Musical isomorphism in §8.2 (Reviewer X, Low)

**Landed.** In §8.2 line ~467, "a 2-form, which when contracted against another vector produces a vector" is now:

> a 2-form, which when contracted against another vector and raised via the simplicial metric produces a vector

Brings §8.2's level of care into line with §§3.4 and 4.

### `[S8-X-L-5]` — "by Proposition 6.1" pointer (Reviewer X, Low)

**Landed.** In §8.3 Composition Formulas paragraph, "The product of two rotation matrices $R(u_1, \theta_1)\, R(u_2, \theta_2)$ is again a rotation matrix, necessarily of the form …" is now:

> … is again a rotation matrix (by Proposition 6.1), necessarily of the form …

Makes the "necessarily" traceable. One-word fix.

### `[S8-Y-L-1]` — Soften "companion paper" (Reviewer Y, Low)

**Landed.** "is a thread we plan to pursue in a companion paper" is now:

> is a natural direction for future investigation

Reduces forward-commitment volume without loss of content. This and the existing "deferred to future work" / "left open for future work" in §§8.2 and 8.3 Composition Formulas now sit at roughly the same level of promise.

---

## Lows not taken (three — deferred)

- `[S8-X-L-1]` — Ambient-dimension qualifier on the minimal-polynomial statement. The sentence in §8.1 (first paragraph) was not touched by the H1 rewrite; the statement is correct in context (the preceding clause establishes $K(u)$ is $4 \times 4$). Defer to pre-submission polish.
- `[S8-X-L-6]` — "wedge-Hodge" vs "wedge-and-Hodge" typography consistency. Optional; §8 itself is internally consistent, cross-section consistency is a pre-submission pass concern.
- `[S8-Y-L-2]` — Integration of the two $N = 4$ uniqueness strands in §8.1. Partly absorbed by the H1 rewrite (the minimal-polynomial-identity story and the Lie-theoretic dimension count now appear in a single paragraph instead of two parallel paragraphs); the surviving §8.1 final paragraph is a single-claim observation about $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$. No further integration needed at this cycle.

---

## Propagation edits

- **No References changes.** All Medium-related citations (`[Wildberger]`, `[Pawlowsky-Glahn-Egozcue]`, `[Müller-Regensburger]`) were already present from earlier cycles. The physics-applications trim (`[S8-M-4]`) removed items for which new citations (Kanerva 2009, Barceló-Liberati-Visser) *would* have been required under the alternative "hedge + cite" option; the trim option was taken precisely because it avoids introducing speculative references.
- **No cross-section edits** were necessary. The bridging paragraph at the top of §8 is self-contained and does not propagate to §7's closing prose; §9's closing paragraph about higher-$N$ simplicial exterior calculus is still consistent with §8.1/§8.2 after the rewrite (the "rank 2 per blade, but non-commuting for $N \geq 5$" story is the same story §9 hints at more briefly).
- **No theorem numbers or proofs** were added or changed.

---

## Cycle status

All three Highs and all four Mediums cleared. Three of the seven Cycle 1 Lows taken (per Author recommendation); five deferred to pre-submission polish or subsumed by the High/Medium rewrites. §8 is ready for a Cycle 2 re-review from both Reviewer X and Reviewer Y. Expectation: both return STATUS GREEN with no C/H/M findings.
