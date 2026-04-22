# Reviewer X — Whole-Paper Consistency Sweep (Cycle 1)

**Date:** 2026-04-21
**Scope:** Full manuscript `simplicial_vector_calculus.md` (front matter + §§1–9) + Appendices A–D + open-issues adjudication for every non-RESOLVED entry in `reviews/open-issues.md`.
**Lens:** Readability + consistency > completeness (user directive for this cycle).

---

## Overall STATUS: GREEN

**Finding counts (new):** Critical 0 / High 0 / Medium 2 / Low 4.
**Open-issue adjudications:** 3 LAND / 8 DECLINE / 3 DEFER-TO-LATEX / 3 N/A (empirical-script, out of scope).

No Critical or High findings in the manuscript. The two Medium items are bookkeeping (theorem-clause reference style and a numbering gap) rather than formalism flaws. The appendices (A–D) audit clean line-by-line; all numerical and symbolic derivations were checked.

---

## Part A — Whole-paper consistency sweep

### New findings

#### [WS-X-M-1] Theorem 4.1 clause reference uses roman numerals once, Arabic everywhere else — Medium

- **Location.** `simplicial_vector_calculus.md` line 224 (end of Remark 3.2): "This is the identity invoked in Theorem 4.1(ii) below."
- **Claim.** Theorem 4.1 itself (lines 273–275) labels its three clauses with Arabic "1./2./3.". Every other cross-reference uses Arabic: line 281 (proof) "For (2)"…"For (3)", line 293 (§5.1) "by Theorem 4.1(2)", line 326 (§5.2) "by Theorem 4.1(2)". Remark 3.2's "(ii)" is the lone outlier.
- **Severity.** Medium (cross-reference notation mismatch; not a logical flaw).
- **Action.** LAND. One-token edit: `Theorem 4.1(ii)` → `Theorem 4.1(2)`.

#### [WS-X-M-2] Proposition 2.2 has no Proposition 2.1 — Medium

- **Location.** Line 149 (§2.4): "**Proposition 2.2 (Zero-sum quadratic form).**"
- **Claim.** §2 contains exactly one numbered proposition, labelled "2.2". There is no Proposition 2.1 anywhere in §2 (or the paper). §§3, 4, 6, 7 all number sequentially from 1 within the section; §2's "2.2" looks like a stale number from an earlier draft.
- **Severity.** Medium (numbering anomaly; trips a careful reader and risks downstream LaTeX label issues).
- **Action.** LAND. Renumber `Proposition 2.2` → `Proposition 2.1` at definition (line 149) and all references: line 261 (§3.4), line 547 (Appendix A heading "Proposition A.1 (restating Proposition 2.2)"). App A's own `Proposition A.1` label stays.

#### [WS-X-L-1] "wedge-Hodge" hyphen at one site vs "wedge–Hodge" en-dash elsewhere — Low

- **Location.** Line 459 (§8.2 first sentence): "the intrinsic wedge-Hodge construction".
- **Claim.** En-dash "wedge–Hodge" appears in five places (lines 21, 55, 349, 455, 485). Line 459 is the sole hyphen variant. §3.4's "Relation to wedge and Hodge dual" heading (line 253) is a distinct spelled-out phrasing and is not at stake.
- **Severity.** Low (typographic drift).
- **Action.** LAND. `wedge-Hodge` → `wedge–Hodge` at line 459. Closes cross-section leg of `[S8-X-L-6]` (see Part C).

#### [WS-X-L-2] §1.2 item 4 displayed Rodrigues formula uses bare `K` inside an `R(u,\theta)` equation — Low

- **Location.** Line 50 (§1.2 item 4): `$$R(u, \theta) = I + \sin\theta\, K + (1 - \cos\theta)\, K^2,$$`
- **Claim.** Every other displayed Rodrigues formula in the manuscript outside the explicit §5 local shorthand uses argument-full `K(u)`: line 64 (§1.3), line 317 (§5.1, eq. (5.1)), line 347 (§5.3), line 482 (§9). §5.1 line 293 declares "For brevity we write $K$ for $K(u)$ throughout §5.1", which covers lines 310/314/340. Line 50 is in the §1.2 roadmap and is the only remaining non-conforming display.
- **Severity.** Low (notation drift in one display).
- **Action.** LAND. At line 50 change `K` → `K(u)` and `K^2` → `K(u)^2`.

#### [WS-X-L-3] Equation (5.1) is the only numbered display in the paper — Low

- **Location.** Line 317: `$$R(u,\theta) := I + \sin\theta\, K(u) + (1-\cos\theta)\, K(u)^2, \qquad (5.1)$$`
- **Claim.** This is the only numbered display equation in the manuscript; it is referenced exactly once, in the next paragraph (line 318). An orphan-numbered equation is slightly jarring.
- **Severity.** Low (cosmetic).
- **Action.** DEFER-TO-LATEX. Decide in LaTeX whether to (a) drop the `(5.1)` label and rewrite the follow-up reference, or (b) number equations systematically. Not worth touching the markdown source pre-conversion.

#### [WS-X-L-4] Unbalanced parenthesis in Appendix C "Trace" italic label — Low

- **Location.** Line 645 (Appendix C): `**Trace** $\operatorname{tr} R = 2 + 2\cos\theta$ *($4 \times 4$ lift); $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$).*`
- **Claim.** The italic block has one opening `(` and two closings `)`.
- **Severity.** Low (typographic).
- **Action.** LAND. Preferred minimal fix: `*($4 \times 4$ lift; $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$).*` (move `;` inside the parenthetical, drop the stray closing `)`).

### Cross-checks passed

- **Gram matrix notation.** $G = \tfrac{N}{N-1} I - \tfrac{1}{N-1} J$ uniform across Abstract line 17, §1.2 item 2 line 45, §2.4 lines 135/139/145, §3 header line 170, App A lines 549/559–561. `\tfrac` in inline / `\frac` in displays is the observed convention; no single display mixes the two. (Post-[F-H-5] fix is clean.)
- **Hedge-wording uniformity.** *within the simplicial wedge–Hodge framework developed here* appears verbatim (italicized, en-dash) in all four expected locations: Abstract line 21, §1.2 item 6 line 55, §8.1 line 455, §9 line 485.
- **Citation format.** Bracket style `[Author]` / `[Author-Coauthor]` / `[Author, Coauthor]` consistent throughout body, proofs, and appendices.
- **References list.** 22 entries, alphabetized correctly (Ace → Amari → Arnold → Arnold-Falk-Winther → … → Urner → Wildberger). Every bracket citation in the body is present in the list; spot-checked [Shoemake], [Thomson], [Massey], [Müller-Regensburger], [Arnold, §6.1], [Hall, §1.2], [Arnold, App.~2].
- **Ones vector.** `\mathbf{1}` used uniformly (49 occurrences); zero `\mathbb{1}` variants.
- **"autonomous presentation".** Exactly three occurrences, all `autonomous *presentation*`: §1.3 line 61, Remark 4.2 line 283, §9 line 481. No "autonomous arena"/"autonomous theory"/"on its own terms" regressions.
- **Terminology.** "simplicial" dominates the body; "barycentric" confined to Keywords line 23 and §1.1 line 35 (contrastive bridge paragraph). No drift.
- **"zero-sum unit axis".** Uniform (14 occurrences); no "simplicial unit axis" variants.
- **`R(u,\theta)` in displays.** Consistent outside the one line-50 exception flagged as [WS-X-L-2].
- **`K(u)` argument-full convention.** Consistent outside the §5.1 local shorthand and the §1.2 item 4 display flagged as [WS-X-L-2].
- **Numbering within §§3, 4, 6, 7.** Sequential, collision-free (Definition 3.1 → Remark 3.2 → Theorem 3.3 → Corollary 3.4 → Corollary 3.5; Theorem 4.1 → Remark 4.2; Proposition 6.1; Theorem 7.1).
- **Forward/backward references.** Every named artifact has both a definition and consistent references; no dangling forward-pointers.
- **Section cross-references.** Spot-checked "§2.4", "§3.1", "§5.4", "§7.4", "§8.1" — all point to correct subsections.
- **Theorem/abstract/roadmap alignment.** Theorem 4.1's three-clause structure matches Abstract paragraph 2 and §1.2 item 3; Proposition 6.1's nine items align with §7's reductions; Theorem 7.1 aligns with Abstract's 9-multiplication claim and §1.2 item 5. No regressions relative to Cycle-2 certifications.
- **Display formatting.** No stray anonymous displays; no single display mixes `\tfrac`/`\frac`; no trailing-period inconsistencies beyond [WS-X-L-4].

---

## Part B — Appendices A–D

### Appendix A: The Zero-Sum Inner Product Identity (lines 545–563)

- **Content.** Proposition A.1 faithfully restates Proposition 2.2. Proof expands $(\sum c_i)^2 = 0$ to $\sum_{i<j} c_i c_j = -\tfrac{1}{2}\sum c_i^2$, substitutes into $c^\top G c$, collapses to $\tfrac{N}{N-1}\sum c_i^2$. Each step verified. Inline-`\tfrac` / display-`\frac` convention respected.
- **Body consistency.** Matches §2.4 verbatim. $N=4$ ($4/3$) and $N=3$ ($3/2$) specializations match line 153.
- **Notation parity.** Clean. `Proposition A.1` has no label collisions.
- **Citations.** None.
- **Status.** Clean (depends on [WS-X-M-2] LAND propagating to App A heading).

### Appendix B: Proof of $K^3 = -K$ for $N = 4$ (lines 567–613)

- **Step 1 (rank).** Establishes $\mathbf{1}, u \in \ker K(u)$ and $\mathrm{rank}\, K(u) \leq 2$; skew-symmetry + $K(u) \neq 0$ → rank exactly 2. Component-1 computation of $K(u) u$ (line 575) verified by direct expansion: six cross terms pairwise cancel.
- **Step 2 (spectrum).** Uses $(M^2)_{ii} = -\sum_j M_{ij}^2$. Each of the six signed differences $\pm(u_i - u_j)$ appears exactly twice in $\tilde K$ — verified by enumerating antisymmetric pairs $(1,2)/(2,1), (1,3)/(3,1), (1,4)/(4,1), (2,3)/(3,2), (2,4)/(4,2), (3,4)/(4,3)$. $\sum_{i<j}(u_i - u_j)^2 = 4\sum_i u_i^2$ under zero-sum (N=4) verified. Final $\mathrm{tr}(K(u)^2) = -2$ at unit normalization — verified.
- **Step 3 (minimal polynomial).** Spectral theorem for normal matrices → minimal polynomial $x(x^2+1)$ → $K^3 = -K$. Rigor clean.
- **Body consistency.** Matches Theorem 3.3 statement and spectrum quoted at line 239.
- **Notation/labels/citations.** Clean. `Remark B.1` the only labelled object; no collisions.
- **Minor style note (not flagged).** Line 573 uses bare `K \mathbf{1}` in prose — acceptable under the App-B single-axis shorthand.
- **Status.** Clean.

### Appendix C: Properties of the Rotation Matrix $R$ (lines 617–649)

- **Orthogonality.** Expansion of $R^\top R$ verified; odd-power (linear+cubic) terms cancel; $K^2$ coefficient $2(1-\cos\theta) - \sin^2\theta - (1-\cos\theta)^2 = 0$ verified by expansion.
- **Gauge fixation, column sums, determinant, trace, preservation, equivariance, metric, spectrum.** Each derivation follows cleanly from $K^\top = -K$, $K\mathbf{1}=0$, $K^3=-K$, $\mathrm{tr}(K)=0$, $\mathrm{tr}(K^2)=-2$. Determinant via $\det \exp M = \exp \mathrm{tr} M$.
- **Trace split.** $\mathrm{tr}(R) = 2 + 2\cos\theta$ and $\mathrm{tr}(R|_H) = 1 + 2\cos\theta$ via $\mathrm{span}\{\mathbf{1}\} \oplus H$ — matches Proposition 6.1 item 5.
- **Spectrum.** Eigenvalue $+1$ on $\mathrm{span}\{\mathbf{1}, u\}$ (both in $\ker K$); $e^{\pm i\theta}$ on $u^\perp \cap H$. Correct.
- **Body consistency.** All nine items of Proposition 6.1 discharged; "Details omitted" for items 6–8 acceptable brevity.
- **Finding.** [WS-X-L-4] cosmetic paren imbalance.
- **Status.** Clean on content.

### Appendix D: Worked Example Computations (lines 653–697)

- **Setup.** $u = (a,a,-a,-a)$, $a = \sqrt{3}/4$. Six off-diagonal $\tilde K$ entries (lines 659–664) verified: $\{0, -2a, 2a, 2a, -2a, 0\}$ at positions $(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)$.
- **K, K², R.** After $1/\sqrt{3}$ scaling: $K$ entries in $\{0, \pm 1/2\}$. $K^2$ matrix (line 677) verified by direct multiplication (row-1: $-1/2, 1/2, 0, 0$). $R = I + (\sqrt{3}/2) K + (3/2) K^2$ row-1: $1/4, 3/4, -\sqrt{3}/4, \sqrt{3}/4$ — matches displayed matrix.
- **Verifications.** Row sums all 1 ✓; column sums all 1 ✓ (independent check); $\mathrm{tr}(R) = 1 = 2 + 2\cos(2\pi/3)$ ✓.
- **P and P'.** All four components of $RP$ verified:
  - $(RP)_1 = (\sqrt{3}-2)/2$, $(RP)_2 = -\sqrt{3}/2$, $(RP)_3 = (\sqrt{3}+2)/2$, $(RP)_4 = -\sqrt{3}/2$ ✓
  - $\sum = 0$ ✓; $\tfrac{4}{3}\sum (P'_i)^2 = 20/3 = \langle P, P\rangle_s$ ✓.
- **Body consistency.** Matches §5.4 (line 360, line 369). Matches empirical validation of Theorem 7.1 and Proposition 6.1.
- **Status.** Clean. Strong didactic support.

---

## Part C — Open-issues adjudication

Every non-RESOLVED entry in `reviews/open-issues.md` is covered below.

### [N-L-6] Equation formatting in §5.2 — **DEFER-TO-LATEX**

Mechanism-dependent; LaTeX has native `aligned`/`split`. Markdown previewers render inconsistently. Defer.

### [E-Polish-1] `verify_rodrigues_formula.py` hardening — **N/A (empirical scripts; out of scope for this cycle)**

### [S7-L-1] WLOG aside on absorbed index — **DECLINE**

Already signaled by the named-label convention (§7.1 uses $(RP)_p$ explicitly; §7.2 opens with $P_p = -(P_l + P_n + P_m)$). Empirical (Theorem 7.1 H6) further confirms symmetry. Adding a "WLOG" clause duplicates existing signaling.

### [S7-L-2] Storage cost in theorem statement — **DECLINE**

Reviewer's own "no change required"; §7.4 table already canonicalizes the storage column. Log-only per the entry.

### [S7-L-4] Quaternion→matrix one-time conversion cost — **DECLINE**

Already signaled by the existing "per-apply cost only" footnote under the §7.4 table (line 437).

### [S7-L-5] Sharpen "$H$-block" phrasing — **DECLINE**

Reviewer flagged as "purely stylistic"; proposed replacement is longer and the "along $\mathbf{1}$" specification is already implied by Proposition 6.1's gauge-fixation clause.

### [Y-L-2] Bridging sentence in §7.3 — **DECLINE**

Already absorbed by the Cycle-2 `[S7-M-2]` rewrite ("dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint").

### [Y-L-3] Table footnote vs body-text formatting — **DEFER-TO-LATEX**

Markdown-source footnotes render inconsistently; LaTeX has native `\footnote`. Natural fit for conversion.

### [S7-C2-L-1] $e_i$ vs $\mathbf{e}_i$ notation — **DEFER-TO-LATEX**

No collision in practice (disambiguated by boldness + index type + ambient space). Best addressed via a small "Notation" preamble in the LaTeX version.

### [S7-C2-L-2] Mild redundancy in Theorem 7.1 proof block — **LAND**

Trim: the theorem title already says "9-multiplication kernel", so "three dot products of length 3 (nine multiplications in total)" is doubly redundant.
- **Minimal edit** (line 421): `three dot products of length 3 (nine multiplications in total) compute` → `three dot products of length 3 compute`.

### [E-Theorem-7-1-Polish] — **N/A (empirical scripts; out of scope)**

### [E-Proposition-6-1-Polish] — **N/A (empirical scripts; out of scope)**

### [S8-X-L-1] Minimal-polynomial ambient-dimension qualifier — **DECLINE**

Entry's own note: "correct in context". Adding a qualifier increases §8.1 bulk for a pedantic out-of-context reading; the paragraph is not excerpted in practice.

### [S8-X-L-6] "wedge-Hodge" vs "wedge-and-Hodge" cross-section consistency — **LAND (same action as [WS-X-L-1])**

- **Minimal edit** (line 459): `wedge-Hodge` → `wedge–Hodge`.

### [S8-V-L-1] §8.3 ilr vs clr shorthand — **DECLINE**

§8.3 is explicitly speculative / future-work; entry's own note says "Acceptable expository shorthand"; candidate fix adds exposition bulk.

### [S8-V-L-2] Fisher metric "up to a positive scalar" scope — **LAND**

Rigor-affecting: the claim is literally true only at the uniform distribution. A three-word qualifier restores accuracy with minimal bulk; leaving a subtly-false statement in a future-work paragraph is worse than a short hedge.
- **Minimal edit** (line 473): after `up to a positive scalar`, insert `*at the uniform distribution $x \propto \mathbf{1}$*`. Concretely:
  `the simplicial inner product agrees with the Fisher information metric up to a positive scalar — a canonical match, since the Fisher metric is itself defined only up to positive rescaling.`
  →
  `the simplicial inner product agrees with the Fisher information metric up to a positive scalar *at the uniform distribution $x \propto \mathbf{1}$* — a canonical match, since the Fisher metric is itself defined only up to positive rescaling.`

### [S9-V-L-1] "(§3.1)" pointer granularity — **DECLINE**

Entry's own note: "§3.1 pointer is substantively correct." The cyclic-difference *form* is displayed at §3.1 (lines 184–189); Definition 3.1 (§3.2) adds normalization but is the same matrix. §3.1 is the right pointer for the *form*.

---

## Summary

**Overall STATUS: GREEN.**

**New findings table:**

| ID | Severity | Location | Action |
|---|---|---|---|
| WS-X-M-1 | Medium | line 224 (Remark 3.2) | LAND — `(ii)` → `(2)` |
| WS-X-M-2 | Medium | line 149 (+ refs at 261, 547) | LAND — rename Proposition 2.2 → 2.1 |
| WS-X-L-1 | Low | line 459 (§8.2) | LAND — hyphen → en-dash |
| WS-X-L-2 | Low | line 50 (§1.2 item 4) | LAND — `K`→`K(u)`, `K^2`→`K(u)^2` |
| WS-X-L-3 | Low | line 317 (eq. (5.1)) | DEFER-TO-LATEX |
| WS-X-L-4 | Low | line 645 (App C Trace) | LAND — unbalanced paren |

**Open-issue tally:** 17 non-RESOLVED entries — **3 LAND**, **8 DECLINE**, **3 DEFER-TO-LATEX**, **3 N/A (empirical; out of scope)**. LAND items: [S7-C2-L-2], [S8-X-L-6] (≡ WS-X-L-1), [S8-V-L-2].

**Consolidated LAND list for the Author this cycle (7 edits, all one-token / renumbering / three-word):**

1. Line 224: `Theorem 4.1(ii)` → `Theorem 4.1(2)`.
2. Renumber Proposition 2.2 → Proposition 2.1 at line 149 and references at line 261 and line 547.
3. Line 459: `wedge-Hodge` → `wedge–Hodge`.
4. Line 50: `K` → `K(u)`, `K^2` → `K(u)^2`.
5. Line 645: fix paren imbalance in App C Trace italic label.
6. Line 421: drop `(nine multiplications in total)` from Theorem 7.1 proof.
7. Line 473: insert `*at the uniform distribution $x \propto \mathbf{1}$*` after `up to a positive scalar`.

After the Author lands these seven items, a focused verification cycle on the touched lines should clear the manuscript for LaTeX conversion. There are no formalism blockers.

STATUS: GREEN
