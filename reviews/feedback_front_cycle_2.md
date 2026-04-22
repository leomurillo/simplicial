# Front-Matter Harmonization — Cycle 2 Synthesis

**Date:** 2026-04-21
**Scope:** Title, Abstract, Keywords, MSC 2020, (deleted) AI-Note, §1 (Introduction / §1.1 / §1.2 / §1.3).
**Cycle 1 baseline:** Reviewer X AMBER (0C / 0H / 4M / 7L); Reviewer Y AMBER (0C / 3H / 1M / 3L).
**Cycle 2 outcome:** Reviewer X **GREEN**; Reviewer Y **GREEN**. Double-GREEN certified.

## 1. Cycle 2 landing ledger

All convergent Cycle 1 findings cleared in a single Author pass (`reviews/feedback_front_cycle_2_author_triage.md`).

| Finding | Severity | Lane | Status |
|---|---|---|---|
| [F1-M-1] Abstract uniqueness hedge ("within the simplicial wedge–Hodge framework developed here") | M | X | CLOSED |
| [F1-M-2] §1.2 item 3 two-slot gauge-invariance (Theorem 4.1(1)-verbatim) — closes [L-2-1] | M | X | CLOSED |
| [F1-M-3] Abstract item 2 "unit vector" → "zero-sum unit axis" (Def 3.1 parity) | M | X | CLOSED |
| [F1-M-4] §1.3 "autonomous *presentation*" two-clause gloss | M | X | CLOSED |
| [F1-Y-H-1] Abstract paragraph-2 ↔ paragraph-4 redundancy | H | Y | CLOSED |
| [F1-Y-H-2] Abstract closing sentence (no longer ends on future work) | H | Y | CLOSED |
| [F1-Y-H-3] Duplicated AI-Note (standalone block deleted) | H | Y | CLOSED |
| [F1-Y-M-1] §1.3 DEC + FEEC merged into "Relation to exterior calculus" | M | Y | CLOSED |
| [F1-L-1] stylistic `admits`-repetition | L | X | CLOSED (side-effect of P4 rewrite) |
| [F1-L-3] §1.2 item 5 "requiring" → "invoking" (§9 parity) | L | X | CLOSED |
| [F1-L-4] §1.2 item 6 hedge harmonized to canonical form | L | X | CLOSED |
| [F1-L-5] Keywords expanded to 12 items | L | X | CLOSED |
| [F1-L-6] MSC 2020: +15A75, 22E70→22E60 | L | X | CLOSED |
| [F1-Y-L-1] §1.2 item 3 two-slot form (also closes X's [F1-M-2]) | L | Y | CLOSED |
| [F1-Y-L-2] Keywords granularity | L | Y | CLOSED |
| [F1-Y-L-3] "apply operations" → "applying rotations to zero-sum inputs" | L | Y | CLOSED |
| [F1-L-2] Abstract Rodrigues with explicit arguments | L | X | deferred (log-only; both formulations acceptable) |
| [F1-L-7] §1.3 paragraph-boldface cosmetic | L | X | deferred to LaTeX-conversion polish |

**Open-issues register:** `[L-2-1]` marked **RESOLVED 2026-04-21** with pointer to the Cycle 2 triage.

**No new findings** introduced by Cycle 2 (no `[F1-V-*]` entries from either reviewer).

## 2. Terminology adjudication — simplicial vs barycentric

A parallel consultation asked both reviewers whether to globally rename "simplicial" → "barycentric" throughout the manuscript. The user's decision rule: "*If both reviewer agents agree, we should change from simplicial to barycentric everywhere.*"

- **Reviewer X (formalism):** **Prefer keeping "simplicial."** Global rename is not formalism-safe. Standard "barycentric coordinates" carry a default normalization (either Möbius-projective $(c_1,\dots,c_N) \sim (\lambda c_1,\dots,\lambda c_N)$ or affine $\sum \lambda_i = 1$), whereas this paper uses an **additive** gauge $c \sim c + k\mathbf{1}$ with canonical representative $\sum c_i = 0$. The "zero-sum hyperplane" $H$ is the *linear* model (tangent space of the affine simplex at the centroid), not the affine simplex itself. Everything in §2.4 hinges on the linear null-space fact $G\mathbf{1} = 0$; under the affine $\sum = 1$ convention this is a different object. Load-bearing tokens like *simplicial Gram matrix*, *simplicial inner product*, *simplicial norm* refer specifically to the additive-gauge linear model; renaming invites readers to import the wrong equivalence relation. Additionally, §1.3's DEC disambiguation paragraph presupposes "simplicial" as the paper's own contrastive descriptor — erasing it would leave §1.3 arguing against a ghost.
- **Reviewer Y (narrative / positioning):** **Strongly support rename.** "Barycentric" is the mainstream term in FEM / computational geometry / DDG; it aligns with Ciarlet and Brenner–Scott (already cited); it eliminates the DEC collision ("simplicial calculus" in DEC-land implies simplicial-complex topology, misleading readers); it better serves arXiv math.RA / math.DG discoverability.

**Consensus check:** not met (X opposes, Y supports with formalism-level reasons opposing). **Decision:** **no global rename executed.**

**Compromise landed in Cycle 2 Keywords:** `barycentric coordinates` is now in the Keywords line (position 3 of 12), grouped with the other coordinate-family synonyms (`simplicial coordinates`, `Quadray coordinates`, `barycentric coordinates`, `overcomplete coordinates`). This delivers Reviewer Y's discoverability win without Reviewer X's formalism cost. Reviewer Y explicitly accepted this compromise in Cycle 2 verification: "adding `barycentric coordinates` to the keywords as a discoverability concession while retaining `simplicial` in the body text is a completely acceptable and pragmatic compromise."

Body terminology remains "simplicial."

## 3. Front matter final shape

```
Title       : Intrinsic Vector Calculus on Simplicial (Quadray) Coordinates: Cross Product, Rotation, and the Zero-Sum Hyperplane
Authors / Affiliation / Date
---
Abstract    : 4 paragraphs — context → compatibility framework → enumerated operators → $N=4$ synthesis (lands on $\mathfrak{so}(3) \cong (\mathbb{R}^3,\times)$)
Keywords    : 12 items (simplicial, Quadray, barycentric, overcomplete, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues, Lie algebra, rotation)
MSC 2020    : 15A72, 15A75, 22E60, 53A45, 65D18
---
§ 1. Introduction
  §1.1  Motivation (barycentric/simplicial bridge acknowledged)
  §1.2  Six-item roadmap (item 3 two-slot, item 5 "invoking", item 6 canonical hedge + octonion disclaimer)
  §1.3  Scope & terminology
          - "Relation to exterior calculus" merged paragraph (DEC + FEEC; [Desbrun-…] + [Arnold-Falk-Winther])
          - Terminology paragraph with autonomous-presentation two-clause gloss
          - Rodrigues-formula paragraph (retains $R(u,\theta)$, $K(u)$ arguments)
          - Low-$N$ degeneracies paragraph
```

Standalone "A Note on the Use of AI Tools" block deleted; Acknowledgments AI-disclosure (line 493) retained as sole placement.

## 4. Per-reviewer certificates

- `reviews/feedback_front_cycle_2_reviewer_x.md` — 0C / 0H / 0M / 0L, all Cycle 1 Mediums CLOSED, four Lows CLOSED, two Lows appropriately deferred. **STATUS: GREEN.**
- `reviews/feedback_front_cycle_2_reviewer_y.md` — 0C / 0H / 0M / 0L, all Cycle 1 Highs CLOSED, Medium CLOSED, all three Lows CLOSED. **STATUS: GREEN.**

Both reports independently confirm: no new findings, factual claims in the rewritten Abstract paragraph 4 all grounded in the body, §1.3 merged paragraph formally accurate with both citations preserved, open-issues register up to date.

## 5. Overall STATUS

**GREEN (double-GREEN).** Front matter is harmonization-complete and ready for arXiv-stage polish (LaTeX conversion, figure/table tuning) or additional body-section work.

## 6. Residual items tracked elsewhere

- `[F1-L-2]` Abstract Rodrigues-formula argument explicitness — log-only, either form acceptable.
- `[F1-L-7]` §1.3 paragraph-boldface cosmetic parity — deferred to LaTeX polish pass.

These are logged in this synthesis and in the Author triage; no separate entry needed in `open-issues.md` (both are aesthetic / conversion-stage).
