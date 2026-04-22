# §8 Cycle 2 — Synthesis

**Date.** 2026-04-21
**Scope.** Verification re-audit of `simplicial_vector_calculus.md` §8 ("Higher Dimensions and Future Work") following Author's Cycle 2 pass (see `feedback_s8_cycle_2_author_triage.md`). Both formalism (Reviewer X) and narrative (Reviewer Y) auditors re-inspected the section.

## Inputs

- Author triage: `reviews/feedback_s8_cycle_2_author_triage.md`
- Reviewer X verification: `reviews/feedback_s8_cycle_2_reviewer_x.md` — **STATUS: GREEN**
- Reviewer Y verification: `reviews/feedback_s8_cycle_2_reviewer_y.md` — **STATUS: GREEN**

## Outcome

**§8 Cycle 2: GREEN.** All Cycle 1 Critical/High/Medium findings (three Highs, four Mediums) are CLOSED. The three Lows taken by the Author are CLOSED. No new Critical, High, or Medium findings introduced.

### Highs — all CLOSED

| ID | Cycle 1 finding | Disposition |
|---|---|---|
| `[S8-H-1]` | §8.1 falsely claimed higher-$N$ wedge-Hodge generators have rank > 2 | CLOSED — rewrite correctly locates the obstruction at $\dim \mathfrak{so}(N-1) = \binom{N-1}{2} > N-1$ for $N-1 \geq 4$; wedge-Hodge blade generators remain rank-2 for all $N \geq 4$ and are individually Rodrigues-exponentiable |
| `[S8-H-2]` | Fixed-subspace claim "dim $N-3$" applied to generic rotations in $\mathrm{SO}(N-1)$ | CLOSED (folded into `[S8-H-1]`) — sentence now restricted to simple (blade-generated) rotations, where $N-3$ is correct |
| `[S8-Y-H-1]` | Abrupt §7 → §8 transition ("whiplash") | CLOSED — new opening paragraph at top of §8 bridges from the computational kernel back to the structural framing |

### Mediums — all CLOSED

| ID | Cycle 1 finding | Disposition |
|---|---|---|
| `[S8-M-1]` | "$N=4$ uniqueness" claim lacked "within our framework" hedge | CLOSED — italicized hedge matches §1.2 item 6; explicit Eckmann / octonion disclaimer with cross-reference |
| `[S8-M-2]` | Weierstrass substitution mis-attributed to Wildberger | CLOSED — Weierstrass left unattributed (classical); Wildberger now cited only for the rational-trigonometry program |
| `[S8-M-3]` + `[S8-Y-M-1]` (convergent) | "Tetrahedral symmetry family" undefined | CLOSED — concretized to $\sqrt{3}\,u \in \mathbb{Q}^4$ with inline justification for the rational-entries implication |
| `[S8-M-4]` + `[S8-Y-M-3]` (convergent) | Scatter-shot physics applications overclaimed (analog gravity, HDC, CRNT "all exhibit") | CLOSED — trimmed to the CRNT case; paragraph renamed "Connections to other disciplines" with explicit "open question" hedging |
| `[S8-Y-M-2]` + `[S8-X-L-3]` + `[S8-X-L-4]` (folded) | Dense ilr description + Fisher-metric scalar-match imprecision | CLOSED — ilr described at structural-intent level; Fisher match hedged "up to a positive scalar" |

### Lows taken — all CLOSED

- `[S8-X-L-2]` musical isomorphism in §8.2 — CLOSED.
- `[S8-X-L-5]` "(by Proposition 6.1)" pointer in §8.3 Composition Formulas — CLOSED.
- `[S8-Y-L-1]` "companion paper" softened to "natural direction for future investigation" — CLOSED.

### Lows deferred — logged to `open-issues.md`

Reviewer X Cycle 1 Lows not taken:
- `[S8-X-L-1]` minimal-polynomial ambient-dimension qualifier.
- `[S8-X-L-6]` wedge-Hodge vs wedge-and-Hodge typography.

Reviewer Y Cycle 1 Lows:
- `[S8-Y-L-2]` — partly absorbed by the `[S8-H-1]` rewrite (confirmed CLOSED by Reviewer Y on verification).

### New Lows surfaced in Cycle 2 verification — logged to `open-issues.md`

- `[S8-V-L-1]` (Reviewer X) — §8.3 simplified ilr sentence calls "ilr" what is strictly the *centered* log-ratio (clr); ilr = ONB ∘ clr. Acceptable expository shorthand given $H \cong \mathbb{R}^{N-1}$; flag for pre-submission polish.
- `[S8-V-L-2]` (Reviewer X, self-correction) — "simplicial inner product agrees with Fisher up to a positive scalar" is literally true only at the uniform distribution. Surfaced on re-read rather than as a regression introduced by Cycle 2. Non-blocking; an inline "at the uniform distribution" qualifier or softer "canonically associated with" would resolve.

## Cross-section coherence

- §8.1 and §8.2 tell a single consistent story: wedge-Hodge blade generators remain rank-2 for all $N \geq 4$; the obstruction to a single-axis closed-form exponential in higher dimensions is Lie-theoretic.
- §1.2 item 6 and §8.1 uniqueness paragraph use matching "within the simplicial wedge–Hodge framework" hedges.
- §8 opening bridge is consistent with §9's framing of the $N=4$ construction as an "autonomous presentation."
- No new references required; no cross-section propagation edits necessary.

## Recommended next step

§8 is publication-grade modulo the eight deferred Lows (six from Cycle 1 + two new from Cycle 2 verification), all of which belong to a pre-submission polish pass. The next natural scope expansion is:

- **Option A — Advance to §9 review.** Target §9 ("Conclusion") for its own Reviewer X + Reviewer Y cycle. Short section, likely single-cycle.
- **Option B — Full-paper Abstract + §1 harmonization pass.** Now that §§3–8 are all GREEN, re-audit the Abstract and §1 Introduction against the stabilized body. This is the natural place to land the `[L-2-1]` §1.2 item 3 shorthand upgrade and to check that the Abstract's claims still match the final body language.
- **Option C — Empirical cleanup pass.** Clear `[E-Polish-1]`, `[E-Theorem-7-1-Polish]`, and `[E-Proposition-6-1-Polish]` script hardening items in one batch before the first arXiv submission.

**Recommendation:** **Option A** (§9) to close out the body of the paper, then **Option B** for the Abstract + §1 harmonization. Option C can run in parallel with either or deferred to the pre-submission sweep.
