# ERRAND PROMPT — Merge T33 + P6 into a standalone smooth-primorial paper, build, stage for deposit

Open a fresh Claude Code session in `C:\Projects\simplicial` and paste everything below.

---

This is a CONSOLIDATION + PACKAGING errand, not research. The mathematics is FROZEN and
already settled at its stated tiers. Your job: merge two existing drafts into ONE
self-contained special-functions / analytic-number-theory paper that depends on NOTHING
unpublished, build the PDF, re-verify the exact certificates, and stage it for Leo's
review. Nothing is published or sent; Leo makes the go-call at the end.

## The two source drafts (READ BOTH IN FULL FIRST)

- `T33-SmoothPrimorialFamily-Draft1.md` — the CONSTRUCTION (interior tool paper).
  Builds the smooth primorial pri_♯(z) = e^{Li⁻¹(z)}/2π: forced by Riemann's explicit
  formula, unique by Bohr–Mollerup and Wielandt (exactly as Γ), the divisor-lattice
  constant tower (γ, ζ(k), log 2π as a starting-prime family), and the moment
  obstruction (Hankel D₃ = −787680). Its core (§2 onward) is explicitly built with "no
  T-series prereqs." Its §12 "Implications for the program" forward-references N1 and
  T15 — both UNPUBLISHED (this is the one thing that must be neutralized; see Rules).
- `P6-SmoothPrimorialMomentBarrier-Draft1.md` — the OBSTRUCTION (exterior reading).
  Names T33 as its companion and EXTENDS it with the headline theorem: every
  genuinely-multiplicative primorial invariant (φ, σ, J_k = ∏(pᵏ−1), ∏(pᵏ+1), ∏pᵏ) is
  non-moment (some Hankel D_N < 0); the ONLY moment member is the divisor count
  d(P_n) = 2ⁿ, which forgets prime magnitudes. Plus: log 2π is the unique
  shift-invariant constant under the starting-prime translation (fixed point), and the
  √-scale barcode (a prime changes no verdict below its square). The exact-integer
  artifact is `P6-settlements.py` (locate it; likely in `empirical/` or beside P6).

## Why merge

T33 alone is "here is the Γ-analogue, and it is not a moment sequence." P6 supplies the
real punchline — "and NO finite-prime multiplicative invariant is, except the
magnitude-blind 2ⁿ." P6 is anchored ONLY to T33 (no other program dependency), so the
two together are a complete, fully self-contained contribution with a theorem as its
climax. This is the program's intended FIRST publication past the L0–L7 (=T0–T7)
deposits, chosen precisely because its self-contained core needs none of the apex / N /
RH machinery.

## HARD RULES

1. **Math is frozen.** Do NOT re-derive, re-tier, or "strengthen" anything. Preserve
   every [P]/[A]/[C] tag exactly as in the sources. Preserve proofs; you are an editor
   merging and de-duplicating, not an author re-proving. The honest negatives stay
   (the strict-monotonicity pre-registration that FAILED: N*(k) = 3,3,4,4,5,9,…; the
   smooth-Mertens bias γ̃_* ≠ γ; "no GRH claim is made"). Failures are retained per the
   GPD method.
2. **Zero dependence on unpublished work.** The merged paper must cite NOTHING from the
   unpublished stack: no N-series (N0–N16), no P-series by number (P0–P5), no T-series
   by number (T0–T15, T33). Concretely:
   - Neutralize T33 §12: drop or soften the N1 / T15 implications to a single sentence
     like "these objects connect to the author's apex-operator program (companion work,
     forthcoming)" — NO numbered citation, NO claim that depends on them. The [P]
     results never depended on §12; it is commentary.
   - The smooth primorial may cite Γ, Li⁻¹, Bohr–Mollerup, Wielandt, Hamburger/Stieltjes
     moment theory, Mertens, the prime number theorem, Riemann's explicit formula — all
     classical, all fine.
   - Paper 35 (GPD methodology) is published; you MAY cite it once for method, or
     demote the methodology to a one-paragraph remark. Do not make the
     delusional/paranoid/grounded scaffolding load-bearing for the reader (see Rule 4).
3. **Drop the series glyph.** P6 writes the smooth primorial with the Hebrew letter
   פ via `\heb[P]{פ}` — that is the exterior-series house glyph and has a known build
   gotcha. For a standalone special-functions audience, replace it throughout with a
   plain notation (recommend `pri_♯` or `π♯`, matching T33's `pri_{idx,♯}`; pick one and
   use it consistently). No Hebrew glyph in the merged paper.
4. **Reader-facing tone = special-functions / ANT journal.** Keep the GPD machinery as
   INTERNAL HTML-comment plantation notes (pandoc drops them) plus at most a short
   "Methods" remark stating results were pre-registered and settled by exact-integer
   computation. The body should read as a clean math paper: construction → uniqueness →
   constant tower → the moment barrier (single, then family-wide) → honest limits. A
   referee should not need to know what "delusional/paranoid/grounded" means.

## RECOMMENDED STRUCTURE (adjust if a better merge emerges)

- Abstract: factorial : Γ :: primorial : smooth primorial. Build it; it is forced and
  unique; but unlike the factorial it is not a moment sequence, and the barrier is
  family-wide (only 2ⁿ survives). Constant tower as a bonus. State the √-scale / RH
  connection carefully (the gap is governed by RH; NO proof of RH claimed).
- §1 The smooth primorial (T33 construction: Li⁻¹, the 1/2π archimedean constant).
- §2 Uniqueness: Bohr–Mollerup and Wielandt (T33 Parts C, D).
- §3 The divisor family and the constant tower (T33 §8, §10; the γ̃_* bias negative).
- §4 The moment barrier: single (D₃ = −787680) then the family-wide theorem (P6
  פmoment: the W_{ij} = b_{i+j}/b_i factorization carrying sign(D_N); only d = 2ⁿ
  survives; N* invariance across families [exact, finite-verified, general left open];
  the failed strict-monotonicity sharpening retained).
- §5 (optional, if it tightens the story) Structure of the barrier: the log 2π fixed
  point and the √-scale barcode.
- §6 Honest limits / what does not translate / the RH connection stated as an
  equivalence, not a result.
- Appendix: the exact-integer artifact (P6-settlements.py + any T33 numeric cert),
  with reproduction instructions.

## EXECUTION

1. Read both drafts fully. Sketch the merged outline and a short de-duplication map
   (T33 and P6 both restate the construction and the D₃ fact — keep one canonical copy).
2. Locate and RE-RUN the exact-integer certificate(s): `P6-settlements.py` and any T33
   numeric check. Confirm the load-bearing numbers reproduce: D₃ = −787680; the
   family-wide non-moment result; N*(k) = 3,3,4,4,5,9,… (note it is NON-decreasing, the
   pre-registered STRICT monotonicity FAILED — keep that honest); 1/ζ(k) exact / γ̃_*
   biased. These are sympy/mpmath-grade local probes — NO torch. If anything fails to
   reproduce, STOP and report rather than editing numbers.
3. Write the merged manuscript to a new file, e.g.
   `SmoothPrimorialMomentBarrier-Draft1.md`, own descriptive title, NO L/T/P series tag
   (mirror how the Quadray-algebra paper and the two CBS papers shipped untagged).
   Use Leo's affiliation line from P6 ("ITCR, UNA, UCR", leonardo.murillo@gmail.com)
   unless Leo says otherwise — flag it as a Leo call.
4. Build the PDF with the established pipeline (`build.ps1` / `build.sh`; consult
   `BUILD.md`). Build gotchas: affiliation line is required; title/author/date parse
   from the H1 block and the first `---` closes it; do NOT hand-write hypertargets; run
   the cross-reference linker once (not idempotent for §); `\clearpage` before wide
   tables; and ALWAYS visually inspect the rendered PDF page by page — a clean LaTeX log
   does not mean a clean render (check the math, the tables, and that NO פ glyph or
   stray N1/T15 reference survived).
5. Sanity sweep: grep the merged source for leaked references — `N1`, `T15`, `T33`,
   `P6`, `\heb`, `פ`, any "§" cross-paper pointer — and confirm none remain in
   reader-facing text (internal HTML comments may keep provenance notes).

## DELIVERABLES + FINAL CHECKLIST FOR LEO

- The merged manuscript + built, visually-inspected PDF.
- A one-screen report: the de-duplication map; confirmation the certificates
  reproduced (with the key numbers); the list of neutralized forward-references; the
  three Leo calls — (A) final title, (B) affiliation line, (C) deposit target (Zenodo
  DOI is the primary channel, as with the L-series and CBS papers — arXiv math.NT needs
  an endorser the author does not currently have, so do NOT assume arXiv); and (D) your
  recommendation on whether §5 belongs in or is better cut for length.
- If, having done the merge, you judge the two are genuinely better kept as a pair than
  fused, SAY SO with reasons — but default to the merge.

STOP at the checklist. Do not create a Zenodo deposition or publish anything; that is
Leo's call in a separate step.
