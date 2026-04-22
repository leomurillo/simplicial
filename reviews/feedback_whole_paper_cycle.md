# Whole-Paper Consistency Sweep — Cycle Synthesis

**Date:** 2026-04-21
**Scope.** Full manuscript `simplicial_vector_calculus.md` (front matter + §§1–9) + Appendices A–D + open-issues-register adjudication.
**Folds in:** Appendices A–D dedicated audit (first audit of this session).
**User directive this cycle:** readability + consistency > completeness; decline additions that duplicate existing signals; no bulk.

---

## 1. Cycle outcome — double-GREEN ×2

### Cycle 1 (sweep + adjudication)

- **Reviewer X** — formalism audit: **GREEN**. 2 Medium + 4 Low new findings (none Critical/High); open-issues tally 3 LAND / 8 DECLINE / 3 DEFER-TO-LATEX / 3 N/A (empirical-script, out of scope). Appendices A–D audited line-by-line, all clean on content; one typographic imbalance found in App C.
- **Reviewer Y** — narrative audit: **GREEN**. Zero new findings; all narrative cross-checks pass end-to-end. Convergent LAND recommendations with Reviewer X on the three overlap items.

Reports: `reviews/feedback_whole_paper_cycle_1_reviewer_x.md`, `reviews/feedback_whole_paper_cycle_1_reviewer_y.md`.

### Cycle 2 (verification of LAND edits)

- **Reviewer X** — verification: **GREEN**. All 7 LAND edits landed verbatim; no collateral damage; register internally consistent. One observational Low noted on §8.3's two "up to a positive scalar" clauses (asymmetry is accurate, log-only).
- **Reviewer Y** — verification: **GREEN**. Narrative flow intact; all edits integrate smoothly; no readability regression.

Reports: `reviews/feedback_whole_paper_cycle_2_reviewer_x.md`, `reviews/feedback_whole_paper_cycle_2_reviewer_y.md`.

---

## 2. LAND edits executed (7, all mechanical)

Applied directly by the parent agent without Author dispatch (per user's preference for script/command-level edits when work is mechanical and pre-specified).

| # | Location | Edit | Originating ID(s) |
|---|---|---|---|
| 1 | §1.2 item 4 Rodrigues display (line 50) | `K` → `K(u)`, `K^2` → `K(u)^2` | `[WS-X-L-2]` |
| 2 | §2.4 (line 149), §3.4 (line 261), App A heading (line 547) | Proposition 2.2 → 2.1 (three sites) | `[WS-X-M-2]` |
| 3 | Remark 3.2 (line 224) | `Theorem 4.1(ii)` → `Theorem 4.1(2)` | `[WS-X-M-1]` |
| 4 | Theorem 7.1 proof (line 421) | Drop "(nine multiplications in total)" | `[S7-C2-L-2]` |
| 5 | §8.2 (line 459) | `wedge-Hodge` → `wedge–Hodge` | `[WS-X-L-1]` ≡ `[S8-X-L-6]` |
| 6 | §8.3 Fisher sentence (line 473) | Insert `*at the uniform distribution $x \propto \mathbf{1}$*` | `[S8-V-L-2]` |
| 7 | Appendix C Trace item (line 645) | Paren imbalance fix | `[WS-X-L-4]` |

All seven verified CLEAN by both reviewers in Cycle 2.

---

## 3. Open-issues register dispositions

**Tally:** 17 non-RESOLVED entries at sweep start → 3 RESOLVED (LAND) + 8 DECLINED + 3 DEFERRED-TO-LATEX + 3 unchanged (empirical-script polishes, out of scope).

**RESOLVED (LAND):**
- `[S7-C2-L-2]` Theorem 7.1 proof-block redundancy trim.
- `[S8-X-L-6]` wedge-Hodge / wedge–Hodge unification.
- `[S8-V-L-2]` Fisher-metric uniform-distribution qualifier.

**DECLINED** (all with explicit rationale — see `reviews/open-issues.md`):
- `[S7-L-1]` — already signaled by named-label convention + empirical H6.
- `[S7-L-2]` — already signaled by §7.4 table's storage column; reviewer's own "no change required".
- `[S7-L-4]` — already signaled by existing "per-apply cost only" footnote.
- `[S7-L-5]` — pedantic; current form readable; longer alternative adds bulk.
- `[Y-L-2]` — already absorbed by §7 Cycle 2 `[S7-M-2]` rewrite.
- `[S8-X-L-1]` — qualifier's own note: "correct in context"; out-of-context reading not a realistic concern.
- `[S8-V-L-1]` — entry's own note: "acceptable expository shorthand"; §8.3 is explicitly speculative.
- `[S9-V-L-1]` — entry's own note: "substantively correct"; §3.1 pointer correctly targets the displayed form.

**DEFERRED-TO-LATEX** (mechanism-dependent, natural at conversion):
- `[N-L-6]` §5.2 aligned display blocks.
- `[Y-L-3]` §7.4 table footnote mechanism.
- `[S7-C2-L-1]` bold/unbold $e_i$ disambiguation via Notation preamble.
- Plus `[WS-X-L-3]` orphan equation label (5.1) — newly added during the sweep.

**Unchanged (empirical scripts, tracked separately):**
- `[E-Polish-1]` `verify_rodrigues_formula.py` hardening.
- `[E-Theorem-7-1-Polish]` Theorem 7.1 script polish.
- `[E-Proposition-6-1-Polish]` Proposition 6.1 script polish.

These three remain PENDING cleanup pass; none affect manuscript claims. They can be addressed as a consolidated empirical-polish task at any time (doesn't block LaTeX conversion).

---

## 4. Appendices A–D audit summary

First dedicated audit of the appendices this session. All four clean on content:

- **Appendix A** (Zero-sum inner-product identity). Derivation verified; label `Proposition A.1` no collisions; matches §2.4 $N=3$ and $N=4$ specializations.
- **Appendix B** (Proof of $K^3 = -K$ for $N=4$). Step-by-step verification line-by-line: rank (verified component-1 expansion), spectrum (verified six signed differences appear twice each, $\sum_{i<j}(u_i-u_j)^2 = 4\sum u_i^2$ under zero-sum), minimal polynomial via spectral theorem.
- **Appendix C** (Properties of rotation $R$). All nine proofs verified; one typographic paren imbalance (now fixed).
- **Appendix D** (Worked example). Numerical derivations for $u = (a,a,-a,-a)$, $a = \sqrt{3}/4$, $\theta = 2\pi/3$ verified end-to-end: $K$, $K^2$, $R$ matrices; $(RP)_1, \ldots, (RP)_4$; zero-sum and inner-product invariance checks. Matches §5.4 and the empirical scripts.

---

## 5. Manuscript state summary

- **§§1–9 and front matter:** double-GREEN across their respective cycles.
- **Appendices A–D:** audited and clean (this cycle).
- **Theorem 4.1, Theorem 7.1, Proposition 6.1:** all empirically validated GREEN via dedicated scripts (`empirical/verify_theorem_7_1_nine_multiplication.py`, `empirical/verify_proposition_6_1_rotation_properties.py`, `empirical/verify_rodrigues_formula.py`).
- **Open issues:** all manuscript-level items either RESOLVED, DECLINED (with rationale), or DEFERRED-TO-LATEX (mechanism-dependent). No Critical or High items open.
- **Terminology:** "simplicial" retained as body descriptor; "barycentric coordinates" in Keywords for discoverability (Cycle 1 rename consultation resolved without consensus).

---

## 6. LaTeX-conversion readiness

**Both reviewers, both cycles: GREEN.** The manuscript is ready for LaTeX conversion.

Four items naturally land during conversion:
- `[N-L-6]` — `\begin{aligned}` merges in §5.2.
- `[Y-L-3]` — native `\footnote` for §7.4 table.
- `[S7-C2-L-1]` — Notation preamble for $e_i$ vs $\mathbf{e}_i$.
- `[WS-X-L-3]` — orphan `(5.1)` label — either drop or number systematically.

One empirical-polish task is orthogonal and can be handled at any time:
- `[E-Polish-1]` + `[E-Theorem-7-1-Polish]` + `[E-Proposition-6-1-Polish]` — consolidated empirical cleanup.

No Critical, High, or Medium open findings. No blockers.

**STATUS: double-GREEN ×2. Ready for LaTeX conversion.**
