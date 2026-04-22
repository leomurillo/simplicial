# Reviewer Y — Whole-Paper Consistency Sweep (Cycle 1)

**Date:** 2026-04-21
**Scope:** Full manuscript (front matter + §§1–9) + Appendices A–D + open-issues adjudication.

## Overall STATUS: GREEN

The manuscript is in excellent narrative shape with no new Critical or High findings. End-to-end flow is logical; roadmap promises are delivered; appendices integrate cleanly.

## Part A — Whole-paper narrative sweep

### New findings

None. The manuscript flows logically from §1 to §9. Voice is consistent, and the §1.2 roadmap maps perfectly to the body sections and the Conclusion. The recurring $K^3 = -K$ motif is load-bearing and serves as a clean anchor across §3 / §4 / §5 / Appendix B. Signposting is explicit and clear.

### Cross-checks passed

- **Section-to-section flow:** Smooth transitions; the §7→§8 bridge paragraph introduced in §8 Cycle 2 eliminates the former abrupt shift.
- **Abstract ↔ body alignment:** All major Abstract claims surface predictably in the body (Theorem 3.3 / Theorem 4.1 / Proposition 6.1 / Theorem 7.1 / §8.1 / §9).
- **§1.2 roadmap ↔ body delivery:** All six items map cleanly to their target sections.
- **§9 Conclusion ↔ Abstract ↔ §1.2:** Synthesis matches the promises; the Cycle-2 rewrite of §9 answers the §1.1 motivating question affirmatively for $N=4$.
- **Voice / tone uniformity:** Consistent first-person plural throughout body; appropriate passive in definitions and appendix derivations.
- **Hedge register:** "we conjecture"/"we sketch"/"future work"/"within the simplicial wedge–Hodge framework developed here" used uniformly.
- **Display density:** Appropriate. The single table in §7.4 is well-placed.
- **Appendix pointers:** Forward references from §2.4 → App A, §3 → App B, §4 / §6 → App C, §5.4 → App D all well-signposted.

## Part B — Appendices A–D

### Appendix A: The Zero-Sum Inner Product Identity

Reads well on its own. The derivation is pedagogical and integrates cleanly with §2.4. Terseness is appropriate.

### Appendix B: Proof of $K^3 = -K$ for $N = 4$

The step-by-step breakdown (Rank, Spectrum, Minimal polynomial) makes the dense matrix math highly readable. Terseness appropriate; this is a hard result requiring careful step-tracing.

### Appendix C: Properties of the Rotation Matrix $R$

Clear, item-by-item proofs. Good use of referencing prior established properties ($K^3 = -K$, $K\mathbf{1} = 0$, $\mathrm{tr}(K^2) = -2$) to keep individual derivations short. "Details omitted" for items 6–8 acceptable given the pattern is established.

### Appendix D: Worked Example Computations

Excellent didactic support. The step-by-step computation of $K$, $K^2$, $R$, $P'$ for the concrete axis $u = (a,a,-a,-a)$ with $\theta = 2\pi/3$ grounds the abstract formulas in a numeric case readers can reproduce by hand.

## Part C — Open-issues adjudication

- **[N-L-6]** Equation formatting in §5.2 — **DEFER-TO-LATEX** (mechanism-dependent).
- **[E-Polish-1]** `verify_rodrigues_formula.py` hardening — **N/A** (empirical scripts; out of scope for this cycle).
- **[S7-L-1]** WLOG aside on absorbed index — **DECLINE** (already signaled by named-label convention + empirical H6 confirmation).
- **[S7-L-2]** Storage cost in theorem statement — **DECLINE** (already signaled by table in §7.4).
- **[S7-L-4]** One-time quaternion→matrix conversion cost — **DECLINE** (already signaled by "per-apply cost only" footnote).
- **[S7-L-5]** Sharpen "$H$-block" phrasing — **DECLINE** (pedantic; current form is readable).
- **[Y-L-2]** Bridging sentence in §7.3 — **DECLINE** (already absorbed by Cycle-2 `[S7-M-2]` rewrite).
- **[Y-L-3]** Table footnote vs body-text formatting — **DEFER-TO-LATEX** (mechanism-dependent).
- **[S7-C2-L-1]** $e_i$ vs $\mathbf{e}_i$ notation — **DEFER-TO-LATEX** (notation block belongs in LaTeX preamble).
- **[S7-C2-L-2]** Mild redundancy in Theorem 7.1 proof block — **LAND** (trim "(nine multiplications in total)" for readability).
- **[E-Theorem-7-1-Polish]** — **N/A** (empirical scripts; out of scope).
- **[E-Proposition-6-1-Polish]** — **N/A** (empirical scripts; out of scope).
- **[S8-X-L-1]** Minimal-polynomial ambient-dimension qualifier — **DECLINE** (pedantic; current form is readable in context).
- **[S8-X-L-6]** "wedge-Hodge" / "wedge–Hodge" consistency — **LAND** (standardize to en-dash across the paper).
- **[S8-V-L-1]** §8.3 ilr vs clr shorthand — **DECLINE** (acceptable shorthand in a speculative future-work paragraph).
- **[S8-V-L-2]** Fisher metric "up to a positive scalar" scope — **LAND** (add "at the uniform distribution" qualifier for accuracy).
- **[S9-V-L-1]** "(§3.1)" pointer granularity — **DECLINE** (pointer is substantively correct; current form is readable).

## Summary

**STATUS: GREEN.** No new narrative findings. Appendices A–D well-integrated. Open-issue adjudication: **3 LAND** (`[S7-C2-L-2]`, `[S8-X-L-6]`, `[S8-V-L-2]`), **8 DECLINE**, **3 DEFER-TO-LATEX**, **3 N/A** (empirical). Convergent with Reviewer X on all three LAND items. After the mechanical landings, the manuscript is narrative-ready for LaTeX conversion.
