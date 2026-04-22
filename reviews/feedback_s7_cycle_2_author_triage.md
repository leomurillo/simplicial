# §7 Cycle 2 — Author triage record

**Scope:** Surgical Cycle 2 revision of §7 under human-authorized Option B (clear all four Cycle 1 Mediums). Lows at Author discretion; took the two recommended.

**File edited:** `simplicial_vector_calculus.md` (§7 at lines ~403–449; References at ~533).

---

## Mediums landed (all four)

### `[S7-M-1]` — Theorem 7.1 precondition list (Reviewer X, Medium)

**Landed.** Theorem 7.1 restated verbatim to the user-specified form:

> **Theorem 7.1 (9-multiplication kernel).** *For $N = 4$, a simplicial rotation $R$ (Proposition 6.1), and a zero-sum input $P \in H$, the rotated point $RP$ can be computed using exactly 9 scalar multiplications.*

The previous statement omitted "$R$ is a simplicial rotation"; the new form makes the Proposition 6.1(6) dependency (hyperplane preservation) explicit and self-contained.

### `[Y-M-1]` — Theorem 7.1 proof marker (Reviewer Y, Medium)

**Landed.** Added a single prose proof block immediately after the theorem statement, in the paper's house style (`*Proof.*` … `$\square$`, matching the convention in §§3, 6, A, B, C, D):

> *Proof.* The reductions of §§7.1–7.2 exhibit an explicit 9-multiplication algorithm: three dot products of length 3 (nine multiplications in total) compute $(RP)_i$ for $i \in \{l, n, m\}$ via the reduced matrix $\tilde{R}_{ij} = R_{ij} - R_{ip}$, and $(RP)_p$ is recovered by negation at no multiplicative cost. $\square$

Phrasing is slightly expanded from Reviewer Y's minimal suggestion to point at the two concrete ingredients (three length-3 dot products; negation recovery of $(RP)_p$) so that the proof actually summarizes the construction rather than just pointing at it.

### `[S7-M-2]` — §7.3 basis phrasing (Reviewer X, Medium)

**Landed.** Replaced the definitionally-loose prose "picking three of the four simplicial basis vectors and absorbing the fourth into the zero-sum constraint" (which is wrong because $\{e_l, e_n, e_m\}$ are not in $H$) with:

> "…it is the restriction $R|_H$ expressed in the (non-orthonormal) basis $\{e_l - e_p,\; e_n - e_p,\; e_m - e_p\}$ of $H$ — where $e_i$ denotes the $i$-th standard coordinate vector of $\mathbb{R}^4$ — obtained by dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint."

Notation note: the paper uses $\mathbf{v}_i$ for simplicial vertex vectors (§2.5, in ambient $\mathbb{R}^3$) and briefly $\mathbf{e}_i$ for the $\mathbb{R}^3$ Cartesian basis (also §2.5). Neither fits the basis of $H \subset \mathbb{R}^4$ needed here. I introduced $e_i$ (unbolded, distinct from the §2.5 $\mathbf{e}_i$) with an inline appositive so the notation is self-contained at first use inside §7. The parenthetical "(non-orthonormal)" preserves the qualifier from the original sentence.

### `[Y-M-2]` — §7.4 renormalization wall-of-text split (Reviewer Y, Medium)

**Landed.** Inserted a paragraph break at the exact boundary requested: after "…without the non-commutative hypercomplex algebra of Hamilton products." and before "As with any matrix representation of rotations in floating-point arithmetic…". No content changed on either side of the break.

---

## Lows taken (two — per recommendation)

### `[S7-L-3]` — Soften "computationally equivalent to $\mathrm{SO}(3)$" (Reviewer X, Low)

**Landed.** In §7.3 final sentence, "…rotation in the simplicial system is computationally equivalent to $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$." is now:

> "…rotation in the simplicial system has the same per-apply cost as $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$, to which it is conjugate via the hyperplane isometry $V$ of §2.5."

This fits cleanly with the B6 reframing from external cycle 1 (rotation operators of this work are carried to their $\mathbb{R}^3$ counterparts under $V$).

### `[Y-L-1]` — Shoemake citation for quaternion multiplication counts (Reviewer Y, Low)

**Landed, with propagation to References.**

Narrative edit (§7.4, sentence introducing the comparison table):

> "Standard quaternion rotation pipelines offer two pathways to apply a rotation to a point (the multiplication counts below follow [Shoemake] and are standard in the computer graphics literature):"

**Propagation:** New References entry added, alphabetically between `[Pawlowsky-Glahn-Egozcue]` and `[Spivak]`:

> [Shoemake] Shoemake, K. "Animating Rotation with Quaternion Curves." *Computer Graphics (SIGGRAPH '85 Proceedings)* 19(3), 245–254 (1985).

This closes the only standard-knowledge citation gap in §7.

---

## Lows not taken (four — deferred to polish at Author discretion)

- `[S7-L-1]` — WLOG aside on which coordinate is absorbed. Not required; the concrete formulas fix $p$ explicitly.
- `[S7-L-2]` — Storage cost in theorem statement. Reviewer X's own recommendation was "no change required"; table remains canonical.
- `[S7-L-4]` — ~18-mult one-time quaternion→matrix conversion cost. Non-blocking; the existing "per-apply cost only" footnote already signals the cost-category distinction.
- `[S7-L-5]` — Sharpening "columns of $R$ restricted to $H$" to "$H$-block / projections along $\mathbf{1}$". Reviewer X flagged this as "purely stylistic"; intent is clear and result is the same under either reading.
- `[Y-L-2]` — One bridging sentence in §7.3. §7.3 already has the change-of-basis restatement now anchoring it to "drop $e_p$ and re-express via zero-sum"; this effectively supplies the bridging role the reviewer wanted.
- `[Y-L-3]` — Table footnote-vs-body-text formatting. Stylistic; Markdown-source footnotes render inconsistently across previewers, so I am deferring until the LaTeX conversion pass when a real footnote is available.

---

## Cycle status

All four Mediums cleared. §7 is ready for a Cycle 2 re-review from both Reviewer X and Reviewer Y. Expectation: both return STATUS GREEN with no C/H/M findings; any residual Lows can be addressed in the pre-submission pass.
