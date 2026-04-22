# Open Issues — Durable Record

Unresolved review findings, AMBER halts, empirical refutations, and downgraded claims that require human adjudication. Each entry is dated and cites its originating cycle. Resolved entries are retained with a resolution note and the date of resolution.

---

## 2026-04-21 — Whole-Paper Consistency Sweep (Cycle 1) — double-GREEN

Whole-paper sweep including Appendices A–D, with mandated adjudication of every open entry per user directive ("readability + consistency > completeness; decline additions that duplicate existing signals"). Reviewer X GREEN (0C/0H/2M/4L new); Reviewer Y GREEN (0C/0H/0M/0L new). Both reports: `reviews/feedback_whole_paper_cycle_1_reviewer_x.md`, `reviews/feedback_whole_paper_cycle_1_reviewer_y.md`.

**Adjudication tally (17 non-RESOLVED entries at cycle start):** 3 LAND (`[S7-C2-L-2]`, `[S8-X-L-6]`, `[S8-V-L-2]`) → all RESOLVED below; 8 DECLINED (`[S7-L-1]`, `[S7-L-2]`, `[S7-L-4]`, `[S7-L-5]`, `[Y-L-2]`, `[S8-X-L-1]`, `[S8-V-L-1]`, `[S9-V-L-1]`); 3 DEFERRED-TO-LATEX (`[N-L-6]`, `[Y-L-3]`, `[S7-C2-L-1]`); 3 N/A (empirical-script polish items: `[E-Polish-1]`, `[E-Theorem-7-1-Polish]`, `[E-Proposition-6-1-Polish]` — out of scope for manuscript sweep; remain PENDING for a future empirical cleanup task).

### [WS-X-M-1] Theorem 4.1 clause reference `(ii)` → `(2)` in Remark 3.2 — **RESOLVED 2026-04-21**
- **Originating cycle:** Whole-paper sweep (Reviewer X, Medium).
- **Location:** `simplicial_vector_calculus.md` line 224 (end of Remark 3.2).
- **Claim:** Theorem 4.1 labels clauses with Arabic 1/2/3; every body reference uses Arabic; Remark 3.2's "(ii)" was the lone roman-numeral outlier.
- **Resolution:** One-token edit applied — `Theorem 4.1(ii)` → `Theorem 4.1(2)`.

### [WS-X-M-2] Proposition 2.2 → 2.1 (no antecedent 2.1) — **RESOLVED 2026-04-21**
- **Originating cycle:** Whole-paper sweep (Reviewer X, Medium).
- **Location:** `simplicial_vector_calculus.md` lines 149, 261, 547.
- **Claim:** §2 contained exactly one numbered proposition, labelled "2.2", with no antecedent "2.1" — stale numbering from an earlier draft; other sections number sequentially from 1.
- **Resolution:** Renumbered at the three sites: definition (line 149 §2.4), cross-reference (line 261 §3.4), Appendix A restatement heading (line 547).

### [WS-X-L-2] `K`→`K(u)` in §1.2 item 4 Rodrigues display — **RESOLVED 2026-04-21**
- **Originating cycle:** Whole-paper sweep (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` line 50 (§1.2 item 4).
- **Claim:** Every other displayed Rodrigues formula outside the explicit §5 local shorthand used argument-full `K(u)`; §1.2 item 4 was the only non-conforming display.
- **Resolution:** `K` → `K(u)`, `K^2` → `K(u)^2` at line 50.

### [WS-X-L-3] Orphan equation number `(5.1)` — **DEFERRED-TO-LATEX 2026-04-21**
- **Originating cycle:** Whole-paper sweep (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` line 317 (§5.1).
- **Claim:** Equation (5.1) is the only numbered display in the manuscript, referenced once. Either drop the label or number equations systematically.
- **Disposition:** Defer to LaTeX conversion. Natural to handle at LaTeX-equation-numbering phase.

### [WS-X-L-4] Appendix C Trace italic-label paren imbalance — **RESOLVED 2026-04-21**
- **Originating cycle:** Whole-paper sweep (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` line 645 (Appendix C, Trace item).
- **Claim:** Italic block had one `(` and two `)` — typographic imbalance.
- **Resolution:** Fixed to `*($4 \times 4$ lift; $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$).*` (moved `;` inside parenthetical; dropped stray `)`).

---

## 2026-04-20 — §1 Introduction, AMBER halt at Cycle 3 → RESOLVED via post-AMBER spot-patch

### [F-H-5] Gram matrix notation inconsistency — **RESOLVED 2026-04-20**
- **Originating cycle:** Cycle 3 (Reviewer X formalism audit).
- **Locations:** `simplicial_vector_calculus.md` Abstract line 17, §1.2 item 2 line 51.
- **Claim:** Both sites wrote $G = I - \tfrac{1}{N}J$, but §2.4 line 129 defines $G := \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$. The matrix $I - \tfrac{1}{N}J$ is the orthogonal projector onto the zero-sum hyperplane, not the Gram matrix.
- **Verified:** Yes (cross-checked against §2.4 line 143, which gives $\langle c, c \rangle = \tfrac{N}{N-1}\sum_i c_i^2$).
- **Resolution:** Post-AMBER spot-patch on 2026-04-20. Both locations now use the correct simplicial Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$, and the Abstract additionally displays the collapsed quadratic form. Confirmed by Reviewer X spot-verification (`feedback_cycle_3_spotpatch_reviewer_x.md`, STATUS: GREEN).

### [F-M-7] Abstract / Theorem 4.1 phrasing mismatch — **RESOLVED 2026-04-20**
- **Originating cycle:** Cycle 3 (Reviewer X).
- **Location:** Abstract, second paragraph; compare Theorem 4.1 in §4.
- **Claim:** The Abstract's summary blurred the scalar-vs-vector distinction that Theorem 4.1 was revised to make precise.
- **Resolution:** Post-AMBER spot-patch on 2026-04-20. Abstract paragraph 2 now distinguishes scalar gauge-invariance of the inner product from hyperplane-closure plus gauge-annihilation/fixing for the vector-valued operators, matching Theorem 4.1's three-clause structure. Confirmed by Reviewer X spot-verification (STATUS: GREEN).

### [F-M-8] Domain of $K$ extension used in Theorem 4.1 — **RESOLVED 2026-04-20**
- **Originating cycle:** Cycle 3 (Reviewer X).
- **Location:** §4 Theorem 4.1(ii); compare Definition 3.1 and Remark 3.2.
- **Claim:** Theorem 4.1(ii) invoked $K(\mathbf{1}) = 0$, but Definition 3.1 defined $K(u)$ only for zero-sum unit axes. The linear extension of $K$ to all of $\mathbb{R}^4$ (via the entrywise formula) should be stated as a formal definition before being used.
- **Resolution:** Post-AMBER spot-patch on 2026-04-20. Remark 3.2 promoted to "Formal linear extension of $K$", explicitly stating the extension to $\mathbb{R}^4$, linearity, and $K(\mathbf{1}) = 0$. The identity $K(\mathbf{1}) = 0$ was independently verified by the Author from Definition 3.1's entrywise formula. Confirmed by Reviewer X spot-verification (STATUS: GREEN).

---

## 2026-04-20 — §1.2 roadmap-shorthand note (non-blocking)

### [L-2-1] One-slot shorthand in §1.2 item 3 — **RESOLVED 2026-04-21**
- **Originating cycle:** §4 Cycle 2 (Reviewer X, Low finding).
- **Location:** `simplicial_vector_calculus.md` §1.2 item 3 line 53.
- **Claim:** The parenthetical "(values unchanged under $x \mapsto x + t\mathbf{1}$)" states one-slot gauge invariance of the simplicial inner product. After §4 Cycle 1, the formal theorem layer (Theorem 4.1(1), §2.4 line 153) states the full two-slot invariance required for well-definedness on the quotient.
- **Verified:** Yes (flagged by Reviewer X in `feedback_s4_cycle_2_reviewer_x.md`; not blocking).
- **Resolution:** Front-Matter Cycle 2 on 2026-04-21. §1.2 item 3 parenthetical upgraded to the Theorem 4.1(1)-verbatim two-slot form: "the inner product is gauge-invariant as a scalar in both arguments ($\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$)". Convergent with `[F1-M-2]` (Reviewer X, Medium) and `[F1-Y-L-1]` (Reviewer Y, Low). See `reviews/feedback_front_cycle_2_author_triage.md`.

---

## 2026-04-20 — §5 Cycle 1 empirical finding (follow-ups logged, not blocking)

### [E-Conv-1] §8 pre-check: sign consistency with Def 3.1 — **RESOLVED 2026-04-21 (superseded by §2.5 vertex swap)**
- **Originating cycle:** §5 Cycle 1 (Empirical Skeptical + Empirical Reviewer).
- **Location (historical):** former §8 (Ace's $F, G, H$ circulants) vs `simplicial_vector_calculus.md` §3.1 Definition 3.1.
- **Claim:** Empirical Reviewer analytically established $V K(u) V^{-1} = -[Vu]_\times$ under the original §2.5 vertex labelling. The simplicial rotation was left-handed relative to that right-handed Cartesian embedding.
- **Resolution:** On 2026-04-21, at user direction, the §2.5 labelling was changed via an odd permutation of two vertex assignments ($\mathbf v_3 \leftrightarrow \mathbf v_4$). Under the new labelling, the empirical script's Test 4 reports a positive-$\theta$ residual of 4.44e-16 and a negative-$\theta$ residual of 2.31 — i.e.\ the simplicial system is now right-handed and agrees directly with standard Cartesian rotation. The previous former §8 (Ace's $F, G, H$) has been evicted in the same pass, so the downstream pre-check is moot.
- **Verified:** Yes. Rerun of `empirical/verify_rodrigues_formula.py` after the swap, exit code 0 (`empirical/reports/rodrigues_formula.md`, STATUS: GREEN).

### [F-M-6] Remark 5.1 notation `V^\top` vs `V^{-1}` — **RESOLVED 2026-04-21 (superseded by Remark 5.1 deletion)**
- **Originating cycle:** §5 Cycle 2 (Reviewer X, Medium).
- **Location (historical):** `simplicial_vector_calculus.md` §5 Remark 5.1 (lines 357–361 as of 2026-04-20).
- **Resolution:** After the §2.5 vertex relabelling on 2026-04-21, there is no longer a chirality mismatch between the simplicial system and the Cartesian embedding to annotate, so Remark 5.1 has been deleted in its entirety. The §5 roadmap paragraph was updated to drop the forward reference, and the §2.5 convention paragraph now states the right-handed agreement positively and in-place. The notation issue is therefore moot.

### [N-L-6] Equation formatting in §5.2 — **DEFERRED-TO-LATEX 2026-04-21**
- **Originating cycle:** §5 Cycle 2 (Reviewer Y, Low).
- **Location:** `simplicial_vector_calculus.md` §5.2 lines 340–346.
- **Claim:** Purely cosmetic — merging two display blocks via `\begin{aligned}` would reduce visual stutter.
- **Status:** Not blocking. Defer to pre-submission polish pass.
- **Disposition:** Log-only.

### [E-Polish-1] `verify_rodrigues_formula.py` hardening — **PENDING cleanup pass**
- **Originating cycle:** §5 Cycle 1 (Empirical Reviewer QA, Medium findings).
- **Location:** `empirical/verify_rodrigues_formula.py`, `empirical/reports/rodrigues_formula.md`.
- **Claim:** The validation script should (a) add `assert` statements with tolerance thresholds, (b) seed all tests and loop over multiple seeds, (c) add a vertex-permutation control (swap $\mathbf v_3 \leftrightarrow \mathbf v_4$) to localize the orientation mismatch to Def 3.1 vs §2.5, and (d) soften the Test 1 report wording to reflect that it is a one-axis symbolic check, not a polynomial-identity proof.
- **Status:** Not blocking. None of these items change the headline empirical conclusion (which was independently verified analytically by the Empirical Reviewer).
- **Verified:** Yes (Empirical Reviewer QA).
- **Disposition:** Address in a future empirical cleanup task, or alongside the next empirical validation (likely §8's Ace circulants).

---

## 2026-04-21 — §7 Cycle 2 Lows (deferred to pre-submission polish)

### [S7-L-1] WLOG aside on absorbed index — **DECLINED 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §7.2.
- **Claim:** The derivation fixes the absorbed coordinate $p$ implicitly; a one-clause "WLOG" aside naming the choice would help the reader.
- **Status:** Not blocking. Empirical validation (Theorem 7.1, H6) has since confirmed that all four choices of absorbed index yield the same $RP$ to 4e-15 across 4×10⁴ trials, so the WLOG is empirically as well as structurally justified.
- **Disposition:** Defer to next §7 polish or §10 pre-submission sweep.

### [S7-L-2] Storage cost in theorem statement — **DECLINED 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §7.4 comparison table.
- **Claim:** Consider exposing storage cost alongside multiplication count in Theorem 7.1.
- **Status:** Not blocking. Reviewer X's own recommendation was "no change required"; the table in §7.4 already canonicalizes the storage column.
- **Disposition:** Log-only; retain table as-is.

### [S7-L-4] One-time quaternion→matrix conversion cost — **DECLINED 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §7.4 comparison table footnote.
- **Claim:** A parenthetical noting the ~18-mult one-time quaternion-to-matrix conversion cost would make the cost-category distinction (per-apply vs. setup) fully explicit.
- **Status:** Not blocking. The existing "per-apply cost only" footnote already signals the distinction.
- **Disposition:** Defer to pre-submission polish.

### [S7-L-5] Sharpen "$H$-block" phrasing — **DECLINED 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §7.4 renormalization recipe.
- **Claim:** Sharpen "columns of $R$ restricted to $H$" to "$H$-block of $R$, equivalently projections of the columns of $R$ onto $H$ along $\mathbf{1}$".
- **Status:** Not blocking. Reviewer X flagged as "purely stylistic"; intent is clear under either reading.
- **Disposition:** Defer to pre-submission polish.

### [Y-L-2] Bridging sentence in §7.3 — **DECLINED 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer Y, Low).
- **Location:** `simplicial_vector_calculus.md` §7.3.
- **Claim:** A single bridging sentence connecting "absorbing the fourth coordinate" to the 4D → 3D hyperplane reduction would help narrative flow.
- **Status:** Not blocking. The Cycle 2 `[S7-M-2]` rewrite of the basis phrasing ("dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint") effectively supplies the bridging role.
- **Disposition:** Log-only.

### [Y-L-3] Table footnote vs. body-text formatting — **DEFERRED-TO-LATEX 2026-04-21**
- **Originating cycle:** §7 Cycle 1 (Reviewer Y, Low).
- **Location:** `simplicial_vector_calculus.md` §7.4 table footnote sentence.
- **Claim:** Make the table "footnote" either a true footnote or integrate into body text.
- **Status:** Not blocking. Markdown-source footnotes render inconsistently across previewers; deferring until the LaTeX conversion pass when a real footnote mechanism is available.
- **Disposition:** Defer to LaTeX conversion.

### [S7-C2-L-1] Notation: $e_i$ (§7.3) vs $\mathbf{e}_i$ (§2.5) — **DEFERRED-TO-LATEX 2026-04-21**
- **Originating cycle:** §7 Cycle 2 (Reviewer X verification pass, Low).
- **Location:** `simplicial_vector_calculus.md` §7.3 vs §2.5.
- **Claim:** Unbold $e_i \in \mathbb{R}^4$ (§7.3) and bold $\mathbf{e}_i \in \mathbb{R}^3$ (§2.5) coexist without collision in practice (disambiguated by boldness + index type + ambient space), but a one-line notation block in a future "Notation" preamble would make this explicit.
- **Status:** Not blocking.
- **Disposition:** Defer to LaTeX conversion / Notation block if one is added.

### [S7-C2-L-2] Mild redundancy in Theorem 7.1 proof block — **RESOLVED 2026-04-21**
- **Originating cycle:** §7 Cycle 2 (Reviewer X verification pass, Low).
- **Location:** `simplicial_vector_calculus.md` §7 Theorem 7.1 proof block (line 421).
- **Claim:** "Three dot products of length 3 (nine multiplications in total)" states the count twice — once structurally ($3\times 3$) and once numerically (nine). Either alone discharges the proof.
- **Resolution:** Whole-paper consistency sweep 2026-04-21. The parenthetical "(nine multiplications in total)" was deleted from the Theorem 7.1 proof; the structural "three dot products of length 3" suffices given the theorem title already says "9-multiplication kernel". Convergent LAND recommendation from both Reviewer X and Reviewer Y.

### [E-Theorem-7-1-Polish] `verify_theorem_7_1_nine_multiplication.py` polish — **PENDING cleanup pass**
- **Originating cycle:** Theorem 7.1 empirical validation (Loop 2, Empirical Reviewer).
- **Location:** `empirical/verify_theorem_7_1_nine_multiplication.py`.
- **Claim:** (M-new-1) Test 4 uses a hard `assert` before the verdict return, creating a single-point abort; (L-new-1) K-property tolerance `1e-14` inconsistent with `1e-12` identity tolerance; (L-new-2) unreachable `else 1` branch in `test_2_and_3_symbolic_count`; (L-new-3) per-call generator asserts run 10⁵ + 10⁴ times where a canary draw would suffice.
- **Status:** Not blocking. None changes the empirical conclusion (all six hypotheses PASS at or below machine epsilon).
- **Disposition:** Address in a future empirical cleanup task.

### [E-Proposition-6-1-Polish] `verify_proposition_6_1_rotation_properties.py` polish — **PENDING cleanup pass**
- **Originating cycle:** Proposition 6.1 empirical validation (Empirical Reviewer, single-loop GREEN).
- **Location:** `empirical/verify_proposition_6_1_rotation_properties.py`.
- **Claim:** (i) P5 docstring omits the equivalent restricted-trace form $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$ (only the gauge-lift form is computed; the restricted form follows from P2 + subtraction of 1). (ii) P9 eigenvalue pairing sort key `(|z-1|, \Im z)` has theoretical edge-case fragility at $\theta \in \{0, \pi, 2\pi\}$; a Hungarian-style min-weight matching would be defensively more robust. Not triggered with seed 42. (iii) P3 tail-extremum ~15× above structurally symmetric P2 is a sampling artefact, not a generator bug. (iv) P5' (Appendix D deterministic block) doesn't mirror P9's eigenspace/rank checks — stochastic P9 covers it but coverage parity would be cleaner.
- **Status:** Not blocking. None changes the empirical conclusion (all ten tests PASS at or below machine epsilon).
- **Disposition:** Address in a future empirical cleanup task alongside `[E-Theorem-7-1-Polish]`.

---

## 2026-04-21 — §8 Cycle 2 Lows (deferred to pre-submission polish)

### [S8-X-L-1] Minimal-polynomial ambient-dimension qualifier — **DECLINED 2026-04-21**
- **Originating cycle:** §8 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §8.1 first paragraph.
- **Claim:** "Rank-2 skew matrices with at least one zero eigenvalue have minimal polynomial $x(x^2+c^2)$" — correct in context (preceding clause establishes $K(u)$ is $4 \times 4$), but an explicit ambient-dimension qualifier would make the statement readable out of context.
- **Status:** Not blocking. Not touched by the Cycle 2 `[S8-H-1]` rewrite.
- **Disposition:** Defer to pre-submission polish.

### [S8-X-L-6] Typography: "wedge-Hodge" vs "wedge–Hodge" — **RESOLVED 2026-04-21**
- **Originating cycle:** §8 Cycle 1 (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` line 459 (§8.2 first sentence).
- **Claim:** Hyphenation variants coexisted across §§3.4, 8.1, 8.2. After Cycle 2 the en-dash form "wedge–Hodge" was canonical at lines 21, 55, 349, 455, 485, but line 459 retained the hyphen variant.
- **Resolution:** Whole-paper consistency sweep 2026-04-21. `wedge-Hodge` → `wedge–Hodge` at line 459. The manuscript is now uniform (en-dash, six occurrences). Convergent LAND from both Reviewer X (as `[WS-X-L-1]`) and Reviewer Y.

### [S8-V-L-1] §8.3 ilr vs clr shorthand — **DECLINED 2026-04-21**
- **Originating cycle:** §8 Cycle 2 verification (Reviewer X, Low).
- **Location:** `simplicial_vector_calculus.md` §8.3 Information-geometry paragraph.
- **Claim:** After the `[S8-Y-M-2]` simplification, the sentence "the isometric log-ratio (ilr) transformation maps the probability simplex to $H$ after a component-wise log" calls "ilr" what is strictly the *centered* log-ratio (clr); ilr = ONB ∘ clr. Acceptable expository shorthand given the isometry $H \cong \mathbb{R}^{N-1}$.
- **Status:** Not blocking. Readers familiar with [Pawlowsky-Glahn-Egozcue] reconstruct the full factorization without friction.
- **Disposition:** Defer to pre-submission polish. Candidate fix: restore "after a component-wise log and a choice of orthonormal basis on $H$."

### [S8-V-L-2] Fisher metric "up to a positive scalar" scope — **RESOLVED 2026-04-21**
- **Originating cycle:** §8 Cycle 2 verification (Reviewer X self-correction).
- **Location:** `simplicial_vector_calculus.md` §8.3 Information-geometry paragraph (line 473).
- **Claim:** The claim that the simplicial inner product agrees with the Fisher metric "up to a positive scalar" was literally true only at the uniform distribution. Under $x_i = \sqrt{p_i}$, tangent vectors satisfy $\sum x_i v_i = 0$ but *not* $\sum v_i = 0$ in general; the simplicial quadratic form on $T_x(\text{sphere})$ carried a base-point-dependent $-\tfrac{1}{3}(\sum v_i)^2$ correction that vanishes only at $x \propto \mathbf{1}$.
- **Resolution:** Whole-paper consistency sweep 2026-04-21. Inline qualifier inserted: "agrees with the Fisher information metric up to a positive scalar *at the uniform distribution $x \propto \mathbf{1}$*". Convergent LAND from both Reviewer X and Reviewer Y.

---

## 2026-04-21 — §9 Cycle 2 Lows (deferred to pre-submission polish)

### [S9-V-L-1] "(§3.1)" pointer granularity for the cyclic-difference form — **DECLINED 2026-04-21**
- **Originating cycle:** §9 Cycle 2 verification (Reviewer X, Low observation).
- **Location:** `simplicial_vector_calculus.md` §9 novelty list ("the explicit cyclic-difference form of $K(u)$ (§3.1)").
- **Claim:** The cyclic-difference form of $K(u)$ is *introduced and displayed* in §3.1 but *formally defined* in Definition 3.1 of §3.2. A pedantic reader could prefer "(§3.1–3.2)" or "(Definition 3.1)."
- **Status:** Not blocking. §3.1 pointer is substantively correct.
- **Disposition:** Defer to pre-submission polish; trivial one-token fix.

---

<!--
Append new entries above this line using the same heading pattern:
## YYYY-MM-DD — <scope>, <status>
### [ID] <short title>
-->
