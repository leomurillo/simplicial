# External-review cycle 1 synthesis

**Scope:** cross-cutting polish from an external reviewer's tour of the paper (groups A, B, D) plus one Author-initiated sentence in §8.3 (group C). Not scoped to a single section; affects Abstract, §§1.1–1.3, §2.5, §3 opening, §4 (descent proof), Remark 4.2, §7 (renormalization paragraph + table footnote), §8.1, §8.3, §9, References.

**Cycle:** 1 of 3 (terminated at **STATUS GREEN** from both reviewers on the verification pass).

**Files in this cycle:**
- `feedback_external_cycle_1_proposals.md` — the ten consolidated proposals (A1, B1–B6, C1, D1–D3).
- `feedback_external_cycle_1_reviewer_x.md` — Reviewer X (formalism) audit of proposals: `STATUS: AMBER`.
- `feedback_external_cycle_1_reviewer_y.md` — Reviewer Y (narrative) audit of proposals: `STATUS: AMBER`.
- `feedback_external_cycle_1_author_triage.md` — Author's implementation triage record.
- `feedback_external_cycle_1_verify_reviewer_x.md` — Reviewer X verification pass: `STATUS: GREEN`.
- `feedback_external_cycle_1_verify_reviewer_y.md` — Reviewer Y verification pass: `STATUS: GREEN`.

---

## Reviewer-X findings on proposals (adjudicated and closed)

| ID | Severity | Subject | Adjudication |
|----|----------|---------|--------------|
| `[P-H-B4]` | High | §7 "no renormalization" claim + QR-on-$\tilde R$ prescription formally wrong (verified numerically: row-1 squared ambient-norm of $\tilde R$ in §5.4/App. D worked example is $7/4 - \sqrt 3/2 \approx 0.884 \neq 1$). | **RESOLVED.** Author rewrote §7.4 to (i) replace "no renormalization" with an accurate floating-point statement, (ii) replace QR/GS-on-$\tilde R$ with the lift-to-$4\times 4$-$R$-and-re-impose recipe, (iii) add a §7.4 table footnote separating per-apply cost from amortized re-orthogonalization. |
| `[P-M-B3]` | Medium | Descent proof expansion elides the $R^\top = \exp(-\theta K)$ step. | **RESOLVED.** The expanded chain now explicitly states $R^\top = \exp(\theta K)^\top = \exp(-\theta K)$ (using $K^\top = -K$, Definition 3.1), appeals to continuity of matrix multiplication for the power-series commutation, and carries the equality chain through. |
| `[P-M-B6a]` | Medium | "Unitarily equivalent" in §9 — reserved for complex inner products. | **RESOLVED.** §9 now uses "isometric". Remaining "unitarily diagonalizable" in Appendix B Step 3 is legitimate complex-spectral-theorem usage. |
| `[P-M-B6b]` | Medium | $V$ was introduced only as a forward reference in §2.5. | **RESOLVED.** §2.5 now defines $V(c) := \sum_i c_i \mathbf{v}_i$ as an isometric isomorphism $H \to \mathbb{R}^3$ (verified: inner-product preservation by direct expansion of $c^\top G c'$; injectivity from $\ker V \cap H = 0$; bijectivity by dimension). §9 cites "§2.5 (cf. §3.4)". |
| `[P-L-B1]`, `[P-L-B2]`, `[P-L-B5]`, `[P-L-C1]` | Low | Wording sharpenings (wedge–Hodge pointer to §3.4 in the octonion sentence; edge-to-vertex-contraction parenthetical in DEC paragraph; ilr hedge; FEEC global-vs-local Cartesian clarification). | All **addressed**; the first two landed in the body, the last two accepted as-is. |

## Reviewer-Y findings on proposals (adjudicated and closed)

| ID | Severity | Subject | Adjudication |
|----|----------|---------|--------------|
| `[P-H-B6]` | High | §9 reframing must propagate back to Abstract, §1.1, §1.2, Remark 4.2. | **RESOLVED.** Author audited all four sites. Abstract / §1.1 / §1.2 item 3 survive as presentation claims; Remark 4.2 retoned from "on its own terms" to "supports an autonomous *presentation* … isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5". No "not merely a reparameterization" or "autonomous arena" wording remains. |
| `[P-M-B2]` | Medium | DEC paragraph should lead §1.3. | **RESOLVED.** DEC paragraph now leads §1.3. |
| `[P-M-C1]` | Medium | FEEC sentence should move from §8.3 to §1.3 next to DEC. | **RESOLVED.** FEEC now follows DEC at the top of §1.3; no §8.3 bullet left behind. |
| `[P-L-A1]`, `[P-L-B1]`, `[P-L-B3]`–`[P-L-B5]`, `[P-L-D1-D3]` | Low | Stylistic / endorsements. | Not blocking; no action taken (or taken already via Reviewer X's parallel findings). |

## Verification pass — reviewer closing lines

- Reviewer X: `STATUS: GREEN` — all Critical and High findings RESOLVED; two new **Low** items introduced by implementation (see below).
- Reviewer Y: `STATUS: GREEN` — all flagged items RESOLVED; no new findings.

---

## Residual Low findings (decision surface for the human)

These are the only items still open after verification. Neither blocks. Listed so the user can decide **iterate this cycle** (surgical spot-patch) vs. **defer to next scope (§7 review)**.

### `[V-L-1]` — §7.4 phrasing "Gram–Schmidt pass in the simplicial inner product"

Reviewer X observes that the simplicial form $G = \tfrac{4}{3}I - \tfrac{1}{3}J$ is singular on $\mathbb{R}^4$ (null on $\operatorname{span}(\mathbf 1)$), so "Gram–Schmidt in the simplicial inner product" on $\mathbb{R}^4$ is ill-defined as literally stated. On the hyperplane block the simplicial form reduces to $\tfrac{4}{3} I_H$, so $G$-orthonormalization there differs from standard Euclidean GS only by a scale, and the recipe's intent is unambiguous. Suggested minimal patch: either

- insert the parenthetical "(equivalently, standard Gram–Schmidt applied to the columns of the hyperplane block of $R$)", or
- revert to "in the appropriate weighted inner product".

Fits naturally inside the §7 review scope. Non-blocking.

### `[V-L-2]` — §9 stylistic "isometric to classical 3D vector calculus"

Reviewer X notes that "classical 3D vector calculus" is a body of identities rather than a metric space, so "isometric to X" is a mild abuse of language. Read informally ("isometric to the classical realization on $\mathbb{R}^3$ of the inner-product/cross-product/rotation triple") it is unambiguous. Non-blocking.

---

## Recommendation to the human

Both reviewers returned `STATUS: GREEN` on the verification pass. The cycle is **formally closed at GREEN** and the manuscript is ready for the next scope.

The two open Low findings are both small wording issues that fit naturally inside the §7 scope that is coming up next (`[V-L-1]` is literally in §7.4; `[V-L-2]` concerns a §9 sentence that cross-references §7's kernel). Recommended path: **defer both to the §7 cycle 1 audit**, where they will be flagged by Reviewer X anyway and can be patched in the same pass without a separate loop.

Alternative: if you prefer a clean zero-open-findings checkpoint, a minimal spot-patch on `[V-L-1]` (two-phrase insertion in §7.4) and `[V-L-2]` (one-word or one-clause softening in §9) would close them immediately. This would be surgical and would not constitute a new cycle.

No open-issues log update required — both items are minor wording sharpenings, not disputes or downgraded claims.

---

## Author spot-patch (human-authorized, bounded)

User authorized surgical fixes for both residual Lows. Patches applied directly; not a new cycle (per the skill's "Post-AMBER spot-patch" convention, applied here to a post-GREEN zero-open-findings close).

- **`[V-L-1]` RESOLVED.** §7.4: the phrase "via a Gram–Schmidt pass in the simplicial inner product" was replaced by "via a Gram–Schmidt pass on the hyperplane block of $R$ (equivalently, standard Euclidean Gram–Schmidt applied to the columns of $R$ restricted to $H$, since the simplicial inner product reduces to a constant rescaling of the ambient Euclidean inner product on $H$)." This makes the recipe literally well-defined (avoiding the singularity of $G$ on $\mathbb{R}^4$) and gives the reader a concrete implementation.
- **`[V-L-2]` RESOLVED.** §9: "The construction is isometric to classical 3D vector calculus under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4); the novelty lies in…" was replaced by "Under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4), the inner product, cross product, and rotation operators constructed here are carried to their classical $\mathbb{R}^3$ counterparts; the novelty lies in…" The reformulation names the objects being isometrically transported (inner product, cross product, rotation operators), removing the mild stylistic abuse of treating "calculus" as a metric space.

Cycle closes at zero open findings across both reviewers. Manuscript is ready for the §7 cycle 1 audit.
