# Reviewer Y — Narrative & structural audit of external-review cycle 1 proposals

**Scope.** Red-team audit of the *proposals themselves* in `feedback_external_cycle_1_proposals.md` (A1, B1–B6, C1, D1–D3). Anchored against the current manuscript's narrative spine.

## Group A

- **[P-L-A1]** (Low) Hyphenating "Lie-algebra isomorphism" is non-standard in mathematical prose, though grammatically defensible as a compound modifier. The addition of $(\mathbb{R}^3, \times)$ is excellent for clarity. Endorse the bracket addition, but recommend keeping "Lie algebra" unhyphenated to match standard conventions. (Reviewer X endorses the hyphen; tie goes to Author's preference — non-blocking either way.)

## Group B

- **[P-L-B1]** (Low) The octonion aside in §1.2 is helpful for readers familiar with Eckmann's classification. It does not disrupt the flow significantly, though it is a slight digression. **Endorse.**

- **[P-M-B2]** (Medium) The DEC disambiguation is crucial for audience alignment. However, placing it *after* the "Low-$N$ degeneracies" paragraph buries it. It should **lead §1.3**, as title disambiguation is the first thing a DEC-literate reader needs to see. Reposition from "after Low-$N$" to "immediately under the §1.3 header, before Terminological notes / Low-$N$".

- **[P-L-B3]** (Low) **Endorse.** Makes the derivation explicit without adding bloat.

- **[P-L-B4]** (Low) **Endorse wholeheartedly.** Removing the over-strong "no renormalization" claim prevents an easy attack from numerical analysts, and the revised cost comparison remains a strong selling point.

- **[P-L-B5]** (Low) The Aitchison geometry connection is well-situated. The `ilr` detail is slightly dense for a "future work" section, but acceptable. The citation [Pawlowsky-Glahn-Egozcue] is an authoritative modern text, appropriate here.

- **[P-H-B6]** (High) The reframing in §9 from "autonomous arena" to "autonomous *presentation*" is a significant tonal shift that makes the claims much more defensible. However, this *must* propagate backward. Specifically, the Abstract, §1.1, and §1.2 must be sanity-checked for tonal consistency. If §9 walks back the "not merely a reparameterization" claim, §1 cannot still trumpet it unconditionally. Minimum sanity-check sites:
  - Abstract: "intrinsic algebraic calculus … once the simplicial Gram data is fixed, all formulas are expressible without further reference to a Cartesian frame." (This is a *presentation* claim and survives; confirm wording remains presentation-oriented.)
  - §1.2 item 3: "intrinsic … no ongoing reference to an ambient Cartesian embedding". (Presentation claim; should survive.)
  - §1.1: any phrase that could read as asserting *mathematical autonomy* of the simplicial system vs. Cartesian $\mathbb{R}^3$ should be softened so that it does not contradict §9's "isometric / unitarily equivalent" framing.
  - Remark 4.2 if present; the opening of the Introduction.

## Group C

- **[P-M-C1]** (Medium) The FEEC application sentence is currently proposed for §8.3. It would be much better placed in §1.3, **immediately following the B2 DEC paragraph**. This consolidates the DEC/FEEC disambiguation and application context into a single, coherent narrative block early in the paper. As a §8.3 bullet it reads as a bolt-on; paired with B2 up front it becomes part of the paper's positioning argument.

## Group D

- **[P-L-D1-D3]** (Low) Citations are well-chosen, standard, and appropriate for the target audiences.

## Summary

- High: `[P-H-B6]` (downstream tonal propagation).
- Medium: `[P-M-B2]` (placement of DEC paragraph); `[P-M-C1]` (relocation of FEEC sentence).
- Low: `[P-L-A1]` (hyphen taste); `[P-L-B1]`, `[P-L-B3]`, `[P-L-B4]`, `[P-L-B5]`, `[P-L-D1-D3]` (endorsements with minor notes).

Endorsed without reservation: B3, B4, D1–D3.

STATUS: AMBER
