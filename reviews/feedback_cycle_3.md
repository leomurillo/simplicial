# Cycle 3 Synthesis — §1 Introduction (Terminal Cycle)
**Scope:** §1 Introduction + Abstract + §4 (post-Cycle-2 revision)
**Cycle:** 3 of 3 (CRITICAL LIMIT)
**Reviewers:** Reviewer X (formalism), Reviewer Y (narrative)
**Status (joint):** **AMBER at cycle close → GREEN after human-authorized post-AMBER spot-patch (2026-04-20)**
**Spot-patch verifications:** [`feedback_cycle_3_spotpatch_reviewer_x.md`](./feedback_cycle_3_spotpatch_reviewer_x.md) (GREEN), [`feedback_cycle_3_spotpatch_reviewer_y.md`](./feedback_cycle_3_spotpatch_reviewer_y.md) (GREEN).
**Date:** 2026-04-20

Per-reviewer files:
- [`feedback_cycle_3_reviewer_x.md`](./feedback_cycle_3_reviewer_x.md) — All 4 Cycle 2 findings RESOLVED; 1 new High [F-H-5], 2 new Medium.
- [`feedback_cycle_3_reviewer_y.md`](./feedback_cycle_3_reviewer_y.md) — Regression-check clean; 0 new Critical/High/Medium; 1 new Low.

## Terminal state: AMBER

The 3-loop cap has been reached. Per `.cursor/skills/authorship-orchestration/SKILL.md` ("STATUS AMBER"), the loop halts and unresolved findings are surfaced for human adjudication.

## Unresolved loop-blocking finding

### [F-H-5] Gram matrix notation inconsistency (verified correct)

**Locations:** Abstract line 17; §1.2 item 2 line 51.
**Issue:** Both sites write the simplicial Gram matrix as
$$G = I - \tfrac{1}{N}J,$$
but §2.4 line 129 — the actual definition — gives
$$G := \tfrac{N}{N-1}I - \tfrac{1}{N-1}J.$$
$I - \tfrac{1}{N}J$ is the orthogonal projector onto the zero-sum hyperplane (eigenvalues $0$ on $\mathbf{1}$, $1$ on the hyperplane), not the Gram matrix.

**Confirmed by cross-check against §2.4:** line 143 gives $\langle c, c \rangle = \tfrac{N}{N-1} \sum_i c_i^2$, which matches the §2.4 Gram matrix, not $I - \tfrac{1}{N}J$.

**Impact:** Front-matter summary inconsistent with setup. Straightforward to fix — three locations, two lines of notation — but outside the 3-loop cap.

## Non-blocking findings (at Author discretion, not loop-triggering)

- **[F-M-7]** Abstract paragraph 2 "close on the hyperplane and commute with the gauge action" is formally blurrier than Theorem 4.1, which carefully distinguishes scalar invariance from vector-valued hyperplane-closure and gauge-annihilation/fixing.
- **[F-M-8]** Theorem 4.1(ii) references $K(\mathbf{1}) = 0$, but Definition 3.1 only defines $K(u)$ for zero-sum unit axes; the linear extension used in Theorem 4.1 is not stated as a definition before use.
- **[N-L-2]** The differential-operator carve-out is stated twice in the Abstract (paragraphs 2 and 4) — minor repetition.

## Recommendation to the human

1. **Adjudicate [F-H-5].** The finding is verified. Authorize a minimal post-cap fix (correct the Gram-matrix notation at the two Abstract / §1 sites — ideally by citing §2.4's definition verbatim) before any further cycles on other sections. Alternatively, accept AMBER and defer.
2. **Optionally address [F-M-7], [F-M-8], [N-L-2]** in the same minimal pass; they are cheap.
3. After the spot-fix, §1 + Abstract + §4 should be GREEN-ready without another full cycle.

The §1 + Abstract + §4 region is otherwise in strong shape: the scope narrowing is coherent, literature positioning is defensible, and the Joint gauge-compatibility / descent framing of §4 is mathematically cleaner than the Cycle-1 predecessor.

---

## Author triage (post-AMBER spot-patch)

**Scope bound:** edits restricted to the four authorized finding IDs below; no other content touched. Markdown only.

### [F-H-5] Gram matrix notation — Abstract and §1.2 item 2 — **Accepted**

Both sites previously wrote $G = I - \tfrac{1}{N}J$, which is actually the orthogonal projector onto the zero-sum hyperplane, not the simplicial Gram matrix. Replaced with the correct matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ of §2.4 at both sites; the Abstract replacement additionally gives the collapsed zero-sum quadratic form explicitly.

**Abstract line 17 — before:**
> 1. The **inner product** induced by the Gram matrix $G = I - \tfrac{1}{N}J$, with the corresponding quadratic form collapsing on zero-sum vectors to a simple scaled sum of squares.

**Abstract line 17 — after:**
> 1. The **inner product** induced by the simplicial Gram matrix $G = \tfrac{N}{N-1} I - \tfrac{1}{N-1} J$ of §2.4, whose associated quadratic form collapses on zero-sum vectors to $\langle c, c\rangle = \tfrac{N}{N-1}\sum_i c_i^2$.

**§1.2 item 2 — before (fragment):**
> $u^\top G u = 1$, where $G = I - \tfrac{1}{N}J$ is the Gram matrix of Section 2

**§1.2 item 2 — after (fragment):**
> $u^\top G u = 1$, where $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ is the simplicial Gram matrix of Section 2.4

Both replacements use language and the expression $\tfrac{N}{N-1}\sum_i c_i^2$ that match §2.4 line 129 and Proposition 2.2 (line 143) verbatim.

### [F-M-7] Abstract paragraph 2 — scalar vs vector invariance — **Accepted**

The blurry phrase "close on the hyperplane and commute with the gauge action" has been replaced by a three-clause summary matching the structure of Theorem 4.1 (i)/(ii)/(iii), kept at Abstract-length density: the inner product is gauge-invariant *as a scalar*; the binary cross product and rotation preserve the zero-sum hyperplane and respectively *annihilate* and *fix* the gauge direction $\mathbf{1}$. The final clause ("once the simplicial Gram data is fixed, their formulas require no ongoing reference to a Cartesian frame") is preserved as a separate sentence rather than being subordinated.

### [F-M-8] Formal linear extension of $K$ — Remark 3.2 promotion — **Accepted**

Rewrote Remark 3.2 to the four bullets requested:
1. The entrywise formula of Definition 3.1 defines $K(u)$ for every $u \in \mathbb{R}^4$, not only for zero-sum unit axes.
2. The extension is linear: $K(\alpha u_1 + \beta u_2) = \alpha K(u_1) + \beta K(u_2)$.
3. As an immediate consequence, $K(\mathbf{1}) = 0$.
4. Skew-symmetry with respect to the simplicial inner product and the cubic identity $K^3 = -K$ require the zero-sum unit-axis restriction; on general $u \in \mathbb{R}^4$, $K(u)$ is merely well-defined.

**Verification of $K(\mathbf{1}) = 0$ from Definition 3.1:** Confirmed by direct substitution. Each off-diagonal entry of the matrix in Definition 3.1 has the form $u_i - u_j$ for some $i \neq j$ drawn from $\{l, n, m, p\}$ (e.g. $u_m - u_p$, $u_p - u_n$, $u_n - u_m$ in the first row). For $u = (1,1,1,1)$ each such difference is $0$, and the diagonal is already $0$, so $K(\mathbf{1}) = 0$ identically — matching Theorem 4.1(ii)'s claim. No contradiction.

No forward reference was added in §4 before Theorem 4.1(ii): Theorem 4.1(ii)'s own proof sketch already cites "the cyclic-difference form of [Definition 3.1's] entries" as the basis for $K(\mathbf{1}) = 0$, which, in light of the revised Remark 3.2, now reads cleanly.

### [N-L-2] Abstract differential-operator carve-out duplication — **Accepted**

Removed the parenthetical "with differential operators deferred to future work" from line 21; the $\nabla, \mathrm{div}, \mathrm{curl}$ carve-out at line 15 is sufficient and the line-21 sentence now reads more tightly while keeping the Gram-fixed qualifier.

**Line 21 — before (fragment):**
> Together these operators constitute an intrinsic algebraic calculus — inner product, binary cross product, and rotation, with differential operators deferred to future work — on the zero-sum hyperplane; once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame.

**Line 21 — after (fragment):**
> Together these operators constitute an intrinsic algebraic calculus — inner product, binary cross product, and rotation — on the zero-sum hyperplane; once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame.

### Scope confirmation

No edits were made outside the four authorized finding IDs. §2, §4, §5, and the Appendices were not modified. `reviews/open-issues.md` was not touched, per instructions.
