# Author triage record — external-review cycle 1

**Scope.** Implementation of the proposals in `feedback_external_cycle_1_proposals.md` (A1, B1–B6, C1, D1–D3), adjusted for Reviewer X's formalism AMBER findings (`[P-M-B3]`, `[P-H-B4]`, `[P-M-B6a]`, `[P-M-B6b]`, consistency sweep) and Reviewer Y's narrative AMBER findings (`[P-M-B2]` placement, `[P-M-C1]` relocation, `[P-H-B6]` downstream tonal sweep). Hyphen dispute on "Lie-algebra" resolved in favour of Reviewer X (the hyphen) for consistency with the existing phrase "Lie-algebraic identity" in §1.2 item 6. Tour-reviewer proposals implemented **as-adjusted**; no rejections.

---

## Per-proposal record

### A1 — notation refinement (four sites)

- **Status:** landed as-proposed (hyphenated variant).
- **Reviewer finding incorporated:** Reviewer X `[A1]` — "$\mathbb{R}^3$ as a Lie algebra is abelian unless the cross-product bracket is stipulated; write $(\mathbb{R}^3, \times)$". Hyphen kept per Reviewer X; Reviewer Y's mild preference for the unhyphenated form noted and overridden in the interest of internal consistency.
- **Sites edited:** Abstract (line 21); §1.2 item 6 (line 61); §3 opening (line 174); §8.1 closing (line 457).
- **Sweep:** isolated phrase "$\dim \mathfrak{so}(3) = 3$" in §8.1 and §9 reviewed and left alone (per Reviewer X consistency check: reads cleanly after the four iso sentences are rewritten).

### B1 — octonion branch sentence (§1.2 item 6)

- **Status:** landed as-adjusted (Reviewer X `[P-L-B1]` nit incorporated).
- **Reviewer finding incorporated:** Reviewer X `[P-L-B1]` — "prefer 'the simplicial wedge–Hodge construction of §3.4' over 'wedge–Hodge duality'"; also trimmed "outside the simplicial framework developed here" to "outside the framework developed here" (minor tidying, no meaning change).
- **Exact phrase inserted:** "The $n = 7$ realization — the octonion cross product on $\mathbb{R}^7$ — is binary but arises from the non-associative octonion algebra rather than from the simplicial wedge–Hodge construction of §3.4, and therefore lies outside the framework developed here."

### B2 — DEC disambiguation (§1.3)

- **Status:** landed as-adjusted for both placement (Reviewer Y `[P-M-B2]`) and parenthetical (Reviewer X `[P-L-B2]`).
- **Reviewer findings incorporated:**
  - Reviewer Y Medium: DEC paragraph placed as the *first* content under the §1.3 header, before the terminological/Rodrigues/low-$N$ paragraphs, rather than at the end.
  - Reviewer X Low: parenthetical "(possibly combined with an edge-to-vertex contraction)" added to the open-question clause, acknowledging that the $\tilde K(u)$/exterior-derivative identification needs a sharp operator or equivalent to lift cochain *values* to a matrix.
- **Note on §1.3 structure vs. prompt description:** the prompt's description of the pre-edit §1.3 structure was slightly off — the actual existing content is an unlabeled "Throughout this paper…" terminology paragraph, a bolded "Rodrigues formula." paragraph, and a bolded "Low-$N$ degeneracies." paragraph. I preserved all three and inserted the two new labelled paragraphs above them, which realizes the intent expressed in the prompt ("DEC/FEEC context forms a single coherent block before the terminological notes / low-$N$ degeneracies").

### B3 — expanded $R^\top G R = G$ step (§4 descent-theorem proof)

- **Status:** landed as-adjusted (Reviewer X `[P-M-B3]` incorporated).
- **Reviewer finding incorporated:** Reviewer X Medium — the identification $R^\top = \exp(-\theta K)$ was elided in the proposal's insertion; added explicitly, with parenthetical justification "using $K^\top = -K$, Definition 3.1" and the pre-step "since $G$ commutes with $K$ it commutes with every power of $K$ and hence, by continuity of matrix multiplication, with $\exp(\theta K) = R$". The derivation chain is now self-contained without any remaining "easy to see" step.
- **Location:** the proposal labelled this the "§3 descent theorem proof"; the actual text is in the proof of Theorem 4.1 (§4). Edit made at the correct location.

### B4 — §7.4 renormalization paragraph

- **Status:** landed as-adjusted (Reviewer X `[P-H-B4]` High finding honored in full).
- **Reviewer finding incorporated:** Reviewer X High — the proposal's prescription ("QR/Gram–Schmidt on the reduced $3\times 3$ $\tilde R$") is formally wrong because $\tilde R$ is a rotation in a non-orthonormal basis of $H$, so $\tilde R^\top \tilde R \neq I_3$ in general. Sanity-checked against the §5.4 / Appendix D worked example: row 1 of $\tilde R$ has squared ambient-norm $7/4 - \sqrt 3/2 \approx 0.884 \neq 1$, confirming that standard QR on $\tilde R$ is inappropriate. Replaced with Reviewer X's recommended fix: lift $\tilde R$ back to the $4\times 4$ gauge-compatible $R$ and re-impose $R^\top R = I$ together with $R\mathbf 1 = \mathbf 1$, via a Gram–Schmidt pass in the simplicial inner product. Also adopted Reviewer X's softening "as with any matrix representation of rotations in floating-point arithmetic" (representation-specific re-orthogonalization).
- **§7.4 table:** per-apply row for the intrinsic simplicial kernel left at 9 (unchanged; B4 is about a separate, occasional re-enforcement step, per Reviewer X's consistency sweep). Added a one-line clarifying note immediately after the table: "The 'multiplications / apply' column reports per-apply cost only; periodic re-orthogonalization under repeated composition (discussed below) adds an amortized cost comparable to quaternion renormalization and is orthogonal to the per-apply figure."

### B5 — §8.3 Information geometry → Information geometry and compositional data

- **Status:** landed as-proposed.
- **Reviewer finding incorporated:** Reviewer X `[P-L-B5]` — "structurally" hedge on the ilr decomposition kept as-is (harmless); Fisher-Rao → Fisher–Rao en-dash fix included. Reviewer Y Low endorsement noted.

### B6 — §9 paragraph 2 reframing + downstream tonal sweep

- **Status:** landed as-adjusted (Reviewer X `[P-M-B6a]`, `[P-M-B6b]`, and the Reviewer X + Y consistency-sweep items honored).

- **`[P-M-B6a]` — terminology:** replaced "unitarily equivalent" with "isometric" (Reviewer X: "unitary" is strictly reserved for complex inner-product spaces). Exact wording in §9: "The construction is isometric to classical 3D vector calculus under the hyperplane isometry $V: H \to \mathbb{R}^3$ of §2.5 (cf. §3.4)".

- **`[P-M-B6b]` — section pointer for $V$:** repaired §2.5 to promote $V$ from a forward reference to a local definition. §2.5 now reads "… under the *hyperplane isometry* $V\colon H \to \mathbb{R}^3$ defined by $V(c) := \sum_{i=1}^4 c_i \mathbf{v}_i$ … the structural characterization of $V$ as an orientation- and metric-preserving realization of $(H, \langle\cdot,\cdot\rangle)$ as Euclidean $\mathbb{R}^3$ via the Hodge construction is taken up in §3.4." §9 cites "§2.5 (cf. §3.4)", consistent with Reviewer X's recommendation. $V$ is now cleanly introduced by name in §2.5 when a reader arrives.

- **Main B6 text:** new paragraph 2 of §9 follows the prompt's specified wording, modulo "isometric" (not "unitarily equivalent") and the "§2.5 (cf. §3.4)" pointer.

- **Downstream tonal sweep (Reviewer Y `[P-H-B6]` High, Reviewer X consistency sweep).** Sites reviewed:

  1. **Abstract, line 15:** "We develop an intrinsic algebraic vector calculus …" and "Once the simplicial Gram data is fixed, their formulas require no ongoing reference to a Cartesian frame." — *presentation claim, left alone.* Reviewer Y flagged this as surviving the reframing; I concur.

  2. **Abstract, line 21:** "all formulas are expressible without further reference to a Cartesian frame." — *presentation claim, left alone.*

  3. **§1.1, line 43:** "whether this coordinate description supports an intrinsic vector calculus: inner product, cross product, rotation, and their closure properties, defined without reference to an ambient Cartesian frame." — *presentation claim, left alone.*

  4. **§1.1, line 45:** "an intrinsic algebra of rotations and their Lie-algebraic generators on the simplicial zero-sum hyperplane: once the simplicial Gram data is fixed, the operators require no ongoing reference to any Cartesian frame." — *presentation claim, left alone.*

  5. **§1.2 item 3, line 53:** "This makes precise the sense in which the construction is *intrinsic*: once the simplicial Gram data of Section 2 is fixed, the operators require no ongoing reference to a Cartesian embedding." — *presentation claim, left alone.* Explicitly scoped to "the operators require no ongoing reference" (operator-level, not mathematical-content-level).

  6. **§1.3, line 69:** "we reserve *intrinsic* in the precise sense recorded in §1.2 item 3 — once the simplicial Gram data is fixed, the operators require no ongoing reference to an ambient Cartesian frame." — *presentation claim, left alone; this sentence is actually the explicit definition of our use of "intrinsic" and is fully consistent with §9.*

  7. **Remark 4.2, line 291:** previously "supports this algebraic layer of vector calculus on its own terms" — this was the one Reviewer X flagged as the borderline case, endorseable on a strict reading but advisable to audit. **Edited** to "supports an autonomous *presentation* of this algebraic layer of vector calculus, in the sense made precise in §9: isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5, but formulated and computed without passing through a Cartesian frame." This aligns Remark 4.2 tonally with §9 (same "autonomous presentation / isometric via $V$" framing) and removes the ambiguous "on its own terms" phrasing.

  8. **Word "autonomous":** previously appeared only in the §9 paragraph being rewritten; now appears in §9 ("autonomous *presentation*", with emphasis markup making the presentation/arena distinction explicit) and in Remark 4.2 (consistently as "autonomous *presentation*"). No other occurrences.

  9. **Word "arena":** appears in §1.1 line 39 ("the default arena of classical vector calculus" — about Cartesian, not simplicial; irrelevant) and §2.3 line 117 ("a concrete $(N-1)$-dimensional arena on which linear algebra can proceed" — about the zero-sum hyperplane as a computational arena, no autonomy claim attached). Both left alone.

  10. **Phrase "not merely a reparameterization":** appeared only in the §9 paragraph replaced by B6; now removed.

### C1 — FEEC application sentence

- **Status:** landed as-adjusted; relocated from §8.3 to §1.3 per Reviewer Y `[P-M-C1]` Medium finding.
- **Reviewer finding incorporated:** Reviewer Y Medium — FEEC sentence belongs paired with B2 in §1.3 as part of the paper's positioning argument, not as a bolt-on bullet in §8.3.
- **Exact placement:** immediately after the new "Relation to discrete exterior calculus." paragraph (B2), before the existing "Throughout this paper…" terminology paragraph. §8.3 unchanged on this axis (no FEEC bullet was added there).
- **Reviewer X Low note on framing:** kept the proposal's "could in principle supply" hedge; did not adopt Reviewer X's optional sharpening about "without a local affine reference-to-physical map either" to avoid overclaim at this positioning stage. Non-blocking.

### D1–D3 — new references

- **Status:** all three landed as-proposed, inserted in alphabetical-key order.
- **Placements verified:**
  - `[Arnold-Falk-Winther]` between `[Arnold]` and `[Brenner-Scott]`. ✓
  - `[Desbrun-Hirani-Leok-Marsden]` between `[Ciarlet]` and `[Eckmann]`. ✓
  - `[Pawlowsky-Glahn-Egozcue]` between `[Müller-Regensburger]` and `[Spivak]`. ✓
- **Reviewer X D3 note:** citation key truncates the third author (Tolosana-Delgado), consistent with the paper's existing two-name key convention (e.g. `[Brenner-Scott]`, `[Marsden-Ratiu]`); body of the reference lists all three authors.

---

## Sanity checks performed

1. **A1 consistency:** ran a file-wide search for `\\mathfrak{so}(3) \\cong \\mathbb{R}^3` after edits; no remaining occurrences (all four sites converted).
2. **Reference order:** spot-checked the References section; new entries slot into alphabetical-key order without disturbing existing ordering.
3. **§1.3 rebuild:** confirmed new structure is header → DEC paragraph (B2) → FEEC paragraph (C1) → "Throughout this paper…" (unchanged) → "Rodrigues formula." (unchanged) → "Low-$N$ degeneracies." (unchanged).
4. **B3 derivation chain:** re-read the expanded step; the chain is now $GK = KG \Rightarrow G \exp(\theta K) = \exp(\theta K) G$ (continuity), combined with $R^\top = \exp(\theta K)^\top = \exp(-\theta K)$ (from $K^\top = -K$), giving $R^\top G R = G$. No remaining elided steps.
5. **B4 worked-example cross-check:** recomputed the squared ambient-norm of row 1 of $\tilde R$ in the §5.4 / Appendix D example ($u = (a,a,-a,-a)$, $\theta = 2\pi/3$) and confirmed it differs from 1, validating the formal incorrectness of QR-on-$\tilde R$ that Reviewer X identified.
6. **§7.4 table:** confirmed the per-apply row still reads 9 multiplications for the intrinsic simplicial kernel; added a one-line clarifying note immediately below the table so the per-apply cost and the (separate) re-orthogonalization cost are not conflated by a reader scanning the table alone.
7. **B6 downstream sweep:** enumerated every site that could read as a mathematical-autonomy claim (items 1–10 above); only Remark 4.2's "on its own terms" phrasing was soft enough to warrant a tonal edit, which was made. All other sites are cleanly scoped to operator-level / presentation-level claims and are consistent with §9's isometric-via-$V$ framing.
8. **$V$ introduction:** confirmed $V$ is now introduced by name in §2.5 (with explicit definition $V(c) := \sum c_i \mathbf{v}_i$), with the structural/Hodge characterization deferred to §3.4; §9 cites "§2.5 (cf. §3.4)", yielding a stable cross-reference.

## Rejections

None. All tour-reviewer proposals and the Author-initiated C1 item landed, either as-proposed or with Reviewer-X/Y-adjusted wording.
