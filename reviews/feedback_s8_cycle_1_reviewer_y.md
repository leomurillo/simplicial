### Reviewer Y (Narrative & Structure) — Cycle 1 Audit of §8

**Scope.** §8 ("Higher Dimensions and Future Work") and its context (§9, Abstract, §1.3).

#### Findings

- **High: Abrupt transition from §7 to §8 (lines 453–455).**
    §7 concludes with a highly applied, computational discussion of the 9-multiplication kernel and quaternion pipelines. §8 immediately snaps back to the algebraic theory of §5 ("The closed-form Rodrigues exponentiation of §5 relies on..."). The reader experiences whiplash.
    *Recommendation:* Add a bridging sentence at the start of §8 that zooms the reader out from the computational kernel back to the structural properties of the $N=4$ framework before diving into the minimal polynomial.
- **Medium: "Tetrahedral symmetry family" is undefined (line 477).**
    In the Rational Trigonometry paragraph, the phrase "axes $u$ belonging to the tetrahedral symmetry family" is introduced without prior definition or a forward pointer. For a reader, this feels like missing context.
    *Recommendation:* Add a brief inline hedge (e.g., "defined more precisely in future work") or clarify what this means structurally in half a sentence.
- **Medium: Density of the `ilr` transformation description (line 479).**
    The sentence describing the isometric log-ratio (ilr) transformation ("structurally the composition of the component-wise log map with the zero-sum projection $c \mapsto c^{\mathrm{zs}}$ of §2.3 followed by a choice of orthonormal basis on $H$") is extremely dense and presupposes deep familiarity with Aitchison geometry. It interrupts the flow of an otherwise accessible paragraph.
    *Recommendation:* Simplify the structural mapping. Focus on the fact that Aitchison's ilr relies on the same zero-sum hyperplane geometry, rather than detailing the exact composition of maps.
- **Medium: Scatter-shot physics applications (line 481).**
    Listing "Analog gravity, stoichiometric compatibility classes in chemical reaction network theory, and cognitive hyperdimensional computing" in a single breath feels ungrounded and slightly speculative, bordering on buzzword-dropping.
    *Recommendation:* Either trim the list to the most structurally relevant example (CRNT is already well-motivated earlier in the paper) or briefly ground *why* each exhibits this specific gauge/zero-sum structure. The closing sentence ("Whether any of these benefit substantively...") is excellent and carries exactly the right skeptical tone.
- **Low: Cumulative volume of forward commitments (lines 467, 471, 480).**
    The section makes three distinct promises: "defer to future work" (§8.2), "left open for future work" (§8.3), and "a thread we plan to pursue in a companion paper" (§8.3). While acceptable for a conclusion, the "companion paper" commitment is a strong promise.
    *Recommendation:* Consider softening the companion paper claim to "a natural direction for future investigation" to avoid over-promising.
- **Low: Integration of the two uniqueness strands in §8.1 (lines 455–462).**
    The two explanations for $N=4$ uniqueness (the minimal polynomial of rank-2 skew matrices, and the $\dim \mathfrak{so}(3) = 3$ coincidence) sit slightly side-by-side. The narrative works, but could be tighter if the minimal polynomial behavior was explicitly framed as the *algebraic consequence* of the Lie-algebra isomorphism.

#### Cross-Cutting Observations

- **Tonal Consistency:** The tone aligns well with the "autonomous presentation" framing of §9. The old "autonomous arena" rhetoric has been successfully scrubbed.
- **Citations:** Spot-check confirms `[Wildberger]` and `[Pawlowsky-Glahn-Egozcue]` are correctly present in the References.
- **§8.2 Sketch:** The level of detail in the higher-$N$ sketch is appropriate and well-hedged ("or its impossibility").

STATUS: AMBER
