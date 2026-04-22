# Reviewer X — Front-Matter Harmonization Audit (Cycle 2 Verification)

**Scope.** `simplicial_vector_calculus.md` Title, Abstract, Keywords, MSC 2020, §§1.1–1.3 (lines 1–67 after deletion of the standalone AI-Note block), plus confirmation checks on §8.1 / §9 / Theorem 4.1 canonical wording and Acknowledgments line 493.
**Mode.** Verification pass on Author Cycle 2 triage (`reviews/feedback_front_cycle_2_author_triage.md`) closing all 4 Cycle 1 Mediums, 4 of 7 Cycle 1 Lows, and the Reviewer Y Highs / Medium.
**Reference against Cycle 1.** `reviews/feedback_front_cycle_1_reviewer_x.md` — 0C / 0H / 4M / 7L.

## Overall STATUS: GREEN

- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low (new):** 0

All 4 Cycle 1 Mediums and all 4 of the 7 Cycle 1 Lows taken in this pass are cleanly CLOSED against verbatim body-comparanda. No new findings introduced by the Cycle 2 edits. `[L-2-1]` is correctly marked RESOLVED in `reviews/open-issues.md` with a pointer back to the triage record.

---

## Per-finding verdicts

### [F1-M-1] Abstract uniqueness-sentence hedge — **CLOSED**
- **Location.** Abstract, line 21.
- **Current wording.** "We identify $N = 4$ as the unique case *within the simplicial wedge–Hodge framework developed here* in which the construction yields a binary cross product and closed-form exponential …".
- **Body comparanda.** §1.2 item 6 line 55, §8.1 line 455, §9 line 485 — all use the italicized "*within the simplicial wedge–Hodge framework developed here*" verbatim.
- **Verdict.** Verbatim hedge inserted, italicized, and syntactically attached to the uniqueness claim (between "unique case" and "in which the construction yields …"). The regression-of-[S9-M-2]-at-the-Abstract-level concern is cleared and there are no stray pre-Cycle-2 surfaces of the claim without the hedge.

### [F1-M-2] §1.2 item 3 two-slot gauge-invariance (closes [L-2-1]) — **CLOSED**
- **Location.** §1.2 item 3, line 47.
- **Current wording.** "the inner product is gauge-invariant as a scalar in both arguments ($\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$)".
- **Body comparanda.** Theorem 4.1(1) line 273 reads "$\langle a + k\mathbf{1},\, b + m\mathbf{1} \rangle = \langle a, b \rangle$ for all $a, b \in \mathbb{R}^N$ and all $k, m \in \mathbb{R}$."
- **Verdict.** The displayed equation is verbatim with Theorem 4.1(1). The for-all quantifier over $a, b, k, m$ is elided (acceptable roadmap economy). The added qualifier "as a scalar" preserves the scalar-vs-vector distinction that is the organizing theme of Theorem 4.1's three clauses. The two-slot form is now in place.
- **[L-2-1].** Confirmed RESOLVED in `reviews/open-issues.md` line 32, with a pointer to the Cycle 2 triage. `open-issues.md` is internally consistent.

### [F1-M-3] Abstract "zero-sum unit axis" upgrade — **CLOSED**
- **Location.** Abstract item 2, line 18.
- **Current wording.** "… satisfying the Lie-algebraic identity $K^3 = -K$ when $u$ is a zero-sum unit axis."
- **Body comparanda.** Def 3.1 line 211, Remark 3.2(2) line 229, Theorem 3.3 — all use "zero-sum unit axis."
- **Verdict.** "unit vector" is gone; "zero-sum unit axis" now matches Def 3.1 verbatim. A reader applying the Abstract claim to a generic Euclidean unit vector no longer falls outside the theorem's hypotheses. Note (non-finding): the qualifier "when $u$ is a zero-sum unit axis" attaches only to $K^3 = -K$, and the earlier properties "gauge-annihilating, hyperplane-closing" hold for every $u \in \mathbb{R}^4$ under the formal linear extension (Remark 3.2(1)) — this is strictly correct, not a finding.

### [F1-M-4] §1.3 "autonomous *presentation*" gloss — **CLOSED**
- **Location.** §1.3 terminology paragraph, line 61.
- **Current wording.** "Section 4 and the Conclusion additionally describe the resulting calculus as an *autonomous presentation* of the algebraic layer of 3D Euclidean vector calculus: *autonomous* in the sense that, once the simplicial Gram data of §2 is fixed, the construction proceeds without recourse to a Cartesian frame; *presentation* rather than "theory" because it is isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5."
- **Body comparanda.** Remark 4.2 line 283 ("autonomous *presentation* … in the sense made precise in §9: isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5, but formulated and computed without passing through a Cartesian frame"); §9 opening line 481.
- **Verdict.** Two-clause gloss in place, using the exact terms requested: *autonomous* ↔ "proceeds without recourse to a Cartesian frame"; *presentation* ↔ "isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5." Forward references point correctly to §4 and the Conclusion. Terminology consistent with Remark 4.2 and §9. §1.3 now previews the framing rather than introducing it twice in the body without antecedent.

### [F1-L-3] §1.2 item 5 "without invoking" — **CLOSED**
- **Location.** §1.2 item 5, line 53.
- **Current wording.** "matches the performance of the quaternion-to-matrix pathway without invoking the $S^3$ double cover."
- **Body comparanda.** §9 line 483 "matching quaternion-to-matrix performance without invoking the $S^3$ double cover."
- **Verdict.** Single-token swap landed; parity with §9 achieved.

### [F1-L-4] §1.2 item 6 hedge harmonization; octonion disclaimer intact — **CLOSED**
- **Location.** §1.2 item 6, line 55.
- **Current wording.** "*Within the simplicial wedge–Hodge framework developed here*" (italicized) — harmonized with §8.1 / §9 / the Abstract.
- **Octonion disclaimer.** "The $n = 7$ realization — the octonion cross product on $\mathbb{R}^7$ — is binary but arises from the non-associative octonion algebra rather than from the simplicial wedge–Hodge construction of §3.4, and therefore lies outside the framework developed here." Intact and consistent with §8.1 line 455.
- **Verdict.** Hedge phrasing harmonized across all four appearances (Abstract, §1.2 item 6, §8.1, §9). Octonion disclaimer preserved.

### [F1-L-5] Keywords (12 items) — **CLOSED**
- **Current wording (line 23).** "simplicial coordinates, Quadray coordinates, barycentric coordinates, overcomplete coordinates, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation."
- **Count.** Exactly 12 items, as advertised in the triage.
- **Discoverability and appropriateness.** Each term is a load-bearing descriptor of either a paper object (cross product, Rodrigues formula, Hodge dual, wedge product, Lie algebra, rotation) or a structural / terminological pillar (gauge direction, zero-sum hyperplane, overcomplete coordinates) or a community-facing synonym (Quadray coordinates, barycentric coordinates). All are discoverable on arXiv / MathSciNet.
- **Redundancies / duplications.** "simplicial coordinates," "Quadray coordinates," "barycentric coordinates," and "overcomplete coordinates" are all coordinate-family terms — heavy but intentional, since each indexes a distinct audience (general math, Urner–Ace, FEM / computational geometry, linear-algebra structural). Not a redundancy finding; acceptable for an overcomplete-coordinates paper whose naming convention is a live discussion point.
- **`barycentric coordinates` placement.** Sandwiched between `Quadray coordinates` and `overcomplete coordinates`, i.e. grouped with other coordinate-family synonyms. Sensible placement. Reviewer X's Cycle 1 recommendation was neutral on the rename question; including `barycentric coordinates` in Keywords (for discoverability) without renaming the body term is the correct compromise given the parallel adjudication.
- **Verdict.** Well-formed, ordered, no lexical duplicates, all terms appropriate.

### [F1-L-6] MSC 2020 revision — **CLOSED**
- **Current wording (line 25).** "15A72 (multilinear algebra), 15A75 (exterior algebra, Grassmann algebras), 22E60 (Lie algebras of Lie groups), 53A45 (differential geometric aspects in vector and tensor analysis), 65D18 (numerical aspects of computer graphics)."
- **Code validation.**
  - **15A72 ✓** — "Vector and tensor algebra, theory of invariants" (MSC 2020; valid). Kept.
  - **15A75 ✓** — "Exterior algebra, Grassmann algebras" (MSC 2020; valid). **New** — appropriate classification for §3.4 / §8 wedge–Hodge material.
  - **22E60 ✓** — "Lie algebras of Lie groups" (MSC 2020; valid). **Replaces** 22E70 ("Applications of Lie groups to the sciences; explicit representations"). 22E60 is the correct subhead for the $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ material, the $K^3 = -K$ Lie-algebraic identity, and the exponential-map-into-$\mathrm{SO}(3)$ material of §§3–5; 22E70 was a defensible-but-suboptimal upstream parent. Swap is correct.
  - **53A45 ✓** — "Differential geometric aspects in vector and tensor analysis" (MSC 2020; valid). Kept. The parenthetical label matches the MSC 2020 caption.
  - **65D18 ✓** — "Numerical aspects of computer graphics, image analysis, and computational geometry" (MSC 2020; valid). Kept.
- **Ordering.** Numerical ascending (15A72, 15A75, 22E60, 53A45, 65D18). ✓
- **Verdict.** Change-log exactly as the triage states; all five codes valid under MSC 2020.

---

## Cross-review verifications (Reviewer Y lanes, formalism angle)

### Abstract paragraph 4 rewrite (Y's [F1-Y-H-1] / [F1-Y-H-2]) — **CLOSED (formalism-clean)**
- **Redundancy with paragraph 2.** Paragraph 2 (line 15) states the compatibility framework and enumerates the three operators at the statement-of-theorem level. Paragraph 4 (line 21) opens with "For $N = 4$ we prove $K^3 = -K$ and derive the scaling constant $1/\sqrt{3}$ from first principles …" — proof-specific content, with no restatement of paragraph 2's operator list. The former near-verbatim paragraph-2 echo ("Together these operators constitute an intrinsic algebraic calculus …") is gone.
- **Closing sentence.** Paragraph 4 closes on "the simplicial-coordinate reflection of the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$" — a synthesis landing, not a future-work disclaimer.
- **Factual audit of the new paragraph 4.** Every claim is grounded in the body:
  - "$K^3 = -K$ and … scaling constant $1/\sqrt{3}$ from first principles" ↔ Theorem 3.3 + the §3 / Appendix B spectral–trace derivation.
  - "rotation matrix fixes the gauge direction ($R\mathbf{1} = \mathbf{1}$), preserves zero-sum" ↔ Theorem 4.1(3), Prop 6.1(2).
  - "supplies a 9-multiplication kernel for applying rotations to zero-sum inputs" ↔ Theorem 7.1.
  - "unique case within the simplicial wedge–Hodge framework" ↔ §8.1 line 455.
  - "higher $N$ proceeds via Hodge duals of wedge products of arity $N - 3$, sketched in §8" ↔ §3.4 line 263, §8.2 lines 459–461, §8.1 line 453, §9 line 485. The phrase "arity $N - 3$" matches §3.4 ("takes $d - 1 = N - 3$ vector inputs") and §8.2 ("Taking $k = N - 3$ yields a 2-form"); "sketched in §8" is accurate given the explicit deferral of detailed constructions to future work in §8.2 line 461.
  - "$\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$" ↔ §8.1 line 455, §9 line 485.
- **Verdict.** All factual claims hold. Structurally clean. No new formalism finding.

### Standalone AI-Note deletion and Acknowledgments disclosure (Y's [F1-Y-H-3]) — **CLOSED**
- **AI-Note block.** `rg Note.on.the.Use.of.AI` across the manuscript returns zero matches for the standalone heading. Front-matter flow is now Abstract → Keywords → MSC → `---` → `## 1. Introduction`, consistent with the triage description.
- **Acknowledgments disclosure (line 493).** "The authors collaborated extensively with large language models — principally Anthropic's Claude and Google's Gemini — during the development of the derivations presented in this paper. We found these collaborations productive for real-time derivation checking, literature contextualization, and iterative exposition. We acknowledge this use transparently; the mathematical content and its correctness are the authors' responsibility." Intact, factually accurate (matches the actual workflow), and responsibility-appropriate.
- **Verdict.** Duplicated disclosure eliminated; the single Acknowledgments placement is retained. Formalism-clean.

### §1.3 merged "Relation to exterior calculus" paragraph (Y's [F1-Y-M-1]) — **CLOSED (formalism-clean)**
- **Location.** §1.3 line 59.
- **Scope label.** "**Relation to exterior calculus.**" — captures both DEC and FEEC under one umbrella. Formally accurate: both DEC (Desbrun–Hirani–Leok–Marsden) and FEEC (Arnold–Falk–Winther) are exterior-calculus frameworks in the same lineage.
- **Citation preservation.** [Arnold-Falk-Winther] appears twice in the merged paragraph — once for FEEC introduction ("the finite element exterior calculus of Arnold, Falk, and Winther [Arnold-Falk-Winther]") and once as an application-context pointer ("Finite element exterior calculus on unstructured tetrahedral meshes [Arnold-Falk-Winther]"). [Desbrun-Hirani-Leok-Marsden] preserved. No citation dropped.
- **Structural accuracy of the distinction.** The paragraph distinguishes the present work (algebraic layer on the $N$-axis frame of a single simplex, no differential operators, on the zero-sum hyperplane) from DEC/FEEC (algebraic plus differential, on simplicial complexes). This distinction is formally correct and the "scope of this paper" claim ("differential operators … are deferred") is consistent with §1.1 line 39 and §4 line 277. The speculative forward-pointer about $\tilde{K}(u)$ as a DEC discrete exterior derivative and the FEEC application context are flagged as "left to future work" and "could in principle" respectively — appropriately hedged.
- **Verdict.** Merged structure is formally accurate. No overstatement. No citation regression.

---

## Cross-checks that passed (no finding logged)

1. Abstract line 17 Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ and collapsed quadratic form — matches §2.4 (previously verified in Cycle 1, unchanged). ✓
2. Abstract paragraph 3 three-clause structure (inner product / skew operator $K(u)$ / exponential map) — matches Theorem 4.1 clauses (1)/(2)/(3). ✓
3. Abstract paragraph 2 scalar-vs-vector compatibility distinction — matches Theorem 4.1's organizing split. ✓
4. Abstract paragraph 4 claims — all grounded in Theorem 3.3 / Theorem 4.1 / Prop 6.1 / Theorem 7.1 / §8.1 (see "Abstract paragraph 4 rewrite" above). ✓
5. §1.2 item 2 "axis $u$ that is zero-sum and of unit simplicial norm" — still matches Def 3.1 verbatim. ✓
6. §1.2 item 3 two-slot form — matches Theorem 4.1(1) display verbatim. ✓
7. §1.2 item 4 $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$ lift + restriction-to-$H$ — unchanged from Cycle 1, still matches §6 Prop 6.1 and §9. ✓
8. §1.2 item 5 "without invoking the $S^3$ double cover" — matches §9 verbatim. ✓
9. §1.2 item 6 within-framework hedge + octonion disclaimer — consistent with §8.1. ✓
10. §1.3 Rodrigues-formula paragraph display — still uses $R(u,\theta)$, $K(u)$ argumentfull, consistent with §5 and §9. ✓
11. §1.3 low-$N$ degeneracies — dimension count on $\Lambda^2 \mathbb{R}^2$ correct; unchanged from Cycle 1. ✓
12. §1.3 "autonomous *presentation*" gloss — two-clause structure matches Remark 4.2 / §9. ✓
13. §1.3 "Relation to exterior calculus." merged paragraph — formally accurate; both [Arnold-Falk-Winther] and [Desbrun-Hirani-Leok-Marsden] citations preserved. ✓
14. Acknowledgments AI-disclosure line 493 — intact, factually accurate. ✓
15. `reviews/open-issues.md` — `[L-2-1]` marked RESOLVED 2026-04-21 with correct pointer. ✓

---

## New findings (Cycle 2 edits)

None. No `[F1-V-H-*]`, `[F1-V-M-*]`, or `[F1-V-L-*]` entries to log. The Cycle 2 edits are verbatim-consistent with the canonical body phrasing, citations are preserved, and no formalism regression is introduced.

---

## Cycle-2 patch audit summary

| Finding | Cycle 1 severity | Triage status | Verification verdict |
|---|---|---|---|
| [F1-M-1] | Medium | Landed | CLOSED |
| [F1-M-2] | Medium | Landed (closes [L-2-1]) | CLOSED |
| [F1-M-3] | Medium | Landed | CLOSED |
| [F1-M-4] | Medium | Landed | CLOSED |
| [F1-L-1] | Low | Covered by P4 rewrite | CLOSED (side-effect) |
| [F1-L-2] | Low | Not taken (log-only) | n/a (deferral accepted) |
| [F1-L-3] | Low | Landed | CLOSED |
| [F1-L-4] | Low | Landed | CLOSED |
| [F1-L-5] | Low | Landed | CLOSED |
| [F1-L-6] | Low | Landed | CLOSED |
| [F1-L-7] | Low | Deferred to LaTeX polish | n/a (deferral accepted) |

All Cycle 1 Mediums CLOSED. All Cycle 1 Lows either CLOSED or appropriately deferred per the triage record. No new findings.

**STATUS: GREEN**
