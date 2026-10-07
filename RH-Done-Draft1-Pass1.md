# Session prompt — Paper I Pass-1 Refinement

Second pass over **`Paper-I-Identification-Draft1.md`**. The first draft
landed; this session tightens it.

Session opens at `C:\Projects\simplicial\`. You are continuing the
polymath team's work on Paper I "Identification" of the RH-Done trilogy.

---

## The Mission, Stated Once

You are not rewriting Paper I. You are **polishing it** in a controlled
second pass that:

1. Discharges the six concrete priorities recorded in
   `Note_PaperI_Draft1_StatusReport_2026-05-22.md` (Move-7 deliverable
   from the first-draft session).
2. Reads cleanly end-to-end, with no internal contradictions.
3. Stays in scope. No drift into Paper II / Paper III terrain.

**Edit in place.** Save changes back to
`Paper-I-Identification-Draft1.md`. Do not create
`Paper-I-Identification-Draft2.md` — the first-pass refinement is part
of Draft 1's life cycle. (If a second *substantive* pass is needed later,
that will be Draft 2.)

---

## What Is Already on Disk

- `Paper-I-Identification-Draft1.md` — the first-draft manuscript.
  ~78 kB, ~1230 lines, ~10.6k words. Estimated 40–45 LaTeX pp.
- `Note_PaperI_Draft1_StatusReport_2026-05-22.md` — the session-end
  status report. **This is your refinement checklist.** Read it first.
- `RH-Done-Draft1.md` — the spine; reference for theorem numbering and
  scope.
- `siete.md` — source material for §§2–4 of Paper I.
- `HPo-notes.md` Addenda A and H — source material for §§5–6 of Paper I.
- The published trilogy: `T1-NativeSimplicialChart.md`,
  `T2-CumulantTowerEffectiveAction.md`, `T3-CharacterOrthogonalityConductorLattice.md`.
- Two probes for verifying claims:
  - `empirical/probe_Hurwitz_z6_closed_form.py`
  - `empirical/probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`

---

## The Six Priorities (Status Report §"Suggested second-pass priorities")

Discharge these in order. Each is bounded — do not let any one of them
expand into a redrafting exercise.

### Priority 1 — Expand §3.4 with the full term-by-term contraction

**Current state.** §3.4 sketches the contraction at one intermediate step
and jumps to the closed-form polynomial. The closed form is correct; the
derivation should be more explicit.

**Action.** Expand the contraction of $T_{ijk}(Q^{(N)}(s))$ against
$\chi_a \otimes \chi_b \otimes \chi_c$ to show each of the five terms
separately:

- Term 1: $\sum_{i,j,k} Q^{(N)}_i\,\delta_{ij}\delta_{ik}\,\chi_a(i)\chi_b(j)\chi_c(k)$
  reduces to $\sum_i Q^{(N)}_i\,\chi_{a+b+c}(i) = \hat Q^{(N)}_{a+b+c}(s)$.
- Term 2: $-\sum_{i,j,k} Q^{(N)}_i Q^{(N)}_k \delta_{ij}\,\chi_a(i)\chi_b(j)\chi_c(k)$
  reduces to $-\hat Q^{(N)}_{a+b}(s)\,\hat Q^{(N)}_c(s)$.
- Terms 3, 4: by symmetry.
- Term 5: $+2\sum_{i,j,k} Q^{(N)}_i Q^{(N)}_j Q^{(N)}_k\,\chi_a(i)\chi_b(j)\chi_c(k)$
  reduces to $+2\,\hat Q^{(N)}_a\,\hat Q^{(N)}_b\,\hat Q^{(N)}_c$.

Display each step. **Reference siete §5** for the same calculation (with
the same notation), but reproduce here cleanly. Length budget: add at
most 1 page (~300 words).

### Priority 2 — Explicit formulas for the four $T_j$ coefficients in §5.6

**Current state.** §5.6 states the cubic-in-$r$ structure
$T^\zeta = T_0 + i T_1 r - T_2 r^2 - i T_3 r^3$ but does not display
the four coefficients explicitly. The structural claims (vanishing on
K-fixed orbits; cluster residue proportional to $L_{\chi_3}(\rho)^3$) are
stated correctly.

**Action.** Option A: derive the four $T_j$ coefficients explicitly
(check HPo Addendum A5 lines 407-421 for the structural claim; the
explicit polynomial coefficients can be computed by substituting
$\hat Q^{(6)}_k(s) = \alpha_k(s) + i\beta_k(s)\,r(s)$ into Theorem 3.1
and collecting powers of $r(s)$). Display at least one ($T_0$, since it
is the on-shell piece) explicitly; reference HPo Addendum A5 for the
other three with a clear pointer.

Option B (simpler, sufficient for first-pass refinement): keep the
structural statement, but add explicit pointers — "$T_0(s), \ldots,
T_3(s)$ are polynomials in $a = 2^{-s}, b = 3^{-s}$ whose explicit form
is recorded in HPo Addendum A5; their key structural properties used
below are: (i) ..., (ii) ..., (iii) ..." — and then enumerate the
properties used. The reader can either derive or trust.

**Recommendation: Option B**, with the explicit pointer to HPo
Addendum A5. Length budget: add at most half a page.

### Priority 3 — Add short numerical verification tables in §5.5 and §6.2

**Current state.** §5.5 says "the probe verifies that..." in prose only.
§6.2 references the class number formula check ("agreement to seven
decimal places") in prose only.

**Action — §5.5.** Add a short three-row table from the probe output
showing the Hurwitz closed-form residuals at the first three zeta-zero
ordinates:

| $\gamma_n$ | $\max_r$ (Hurwitz closed-form err) | $|F_3(\rho_n)|$ | $|F_1(\rho_n) + F_5(\rho_n)|$ |
|---|---|---|---|
| 14.1347... | ~$10^{-60}$ | ~$10^{-16}$ | ~$10^{-15}$ |
| 21.0220... | ~$10^{-60}$ | ~$10^{-16}$ | ~$10^{-15}$ |
| 25.0109... | ~$10^{-60}$ | ~$10^{-16}$ | ~$10^{-15}$ |

(Exact values: re-run the probe and read off, or use the values already
in `Note_PaperI_Draft1_StatusReport_2026-05-22.md`. The probe is
deterministic.)

**Action — §6.2.** Add a two-line numerical display for the class
number formula check:

> Numerically (`probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`):
> $L(1, \chi_3) = 0.6045998107\ldots$; theoretical $\pi/(3\sqrt{3}) =
> 0.6045997881\ldots$; agreement to seven decimal places.

Length budget: half a page total.

### Priority 4 — Tighten the introduction's provenance ledger

**Current state.** The introduction's "What is new here, what is cited"
ledger lists T2.1, T2.2, T2.3 as rewrites of siete §§1–7 (correct, but
not granular); T3.1, T3.2, T3.3 as new in Paper I (correct).

**Action.** Tighten to map specific equations / theorems to specific
sources:

- T2.1 (§2.5) = clean rewrite of siete §2's substitution
  $\eta_p(s) = -s\log p \Rightarrow \Phi(\eta(s)) = \log\zeta(s)$,
  integrated with the trilogy notation.
- T2.2 (§3.4) = clean rewrite of siete §5's closed-form polynomial,
  with explicit term-by-term derivation new in Paper I (per Priority 1).
- T2.3 (§4.5) = clean rewrite of siete §7's modulus identity, with the
  three "1/2"s compatibility paragraph (§4.6) new in Paper I.
- T3.1 (§5.2) = promotion of HPo Addendum A1 (lines 332-348) to a
  formal theorem with three-step classical proof, new in Paper I.
- T3.2 (§5.3) = promotion of HPo Addendum A2-A3 (lines 349-381) to a
  formal theorem.
- T3.3 (§6.4) = promotion of HPo Addendum H1-H3 (lines 1352-1390) with
  entry-by-entry justification table, new in Paper I.
- I3.4 (§6.5) = closing identification combining T3.3 with the program's
  carrier language, new in Paper I.
- T5.3 (§5.6) = synthesis of Iwaniec-Sarnak 2000 + LMFDB
  `1-3-3.2-r1-0-0`, recorded in HPo Addendum A7 (lines 439-448), formal
  statement new in Paper I.

Length budget: replace the existing "What is new here" subsection
with the more granular version. Net change: ~half a page added.

### Priority 5 — Spell out $L(s, \chi_6) = (1 + 2^{-s}) L(s, \chi_3)$

**Current state.** §5.2's proof of Theorem 5.1 step (iii) uses the
identity $L(s, \chi_6) = (1 + 2^{-s})\,L(s, \chi_3)$ with the prose
justification "the unique non-trivial primitive Dirichlet character
modulo $6$ is induced from $\chi_3$." True and classical, but worth
one displayed-equation line for the information geometer.

**Action.** After the prose justification, add:

> *Explicitly*: every Dirichlet character modulo $6$ factors uniquely
> as $\chi^{(2)}\chi^{(3)}$ for characters mod 2 and mod 3. Mod 2 has
> only the trivial character $\chi_0^{(2)}$. Mod 3 has the trivial
> character $\chi_0^{(3)}$ and the unique non-trivial primitive
> character $\chi_3$. So the four characters mod 6 are
> $\chi_0^{(2)}\chi_0^{(3)} = \chi_0^{(6)}$ (trivial mod 6) and
> $\chi_0^{(2)}\chi_3$ (the unique non-trivial character mod 6, which
> is primitive of conductor 3, not 6). The standard $L$-function
> identity then gives
> $L(s, \chi_0^{(2)}\chi_3) = L(s, \chi_3) \cdot \prod_{p \mid 2}(1 - \chi_3(p)\,p^{-s})^{-1}\big|_{\text{induced}} \cdot (1 - p^{-s}\bigl|_{p = 2, \text{excluded}})$,
> which simplifies (since $\chi_3(2) = -1$, so the Euler factor at $p =
> 2$ contributes $(1 + 2^{-s})^{-1}$, and the lifted character mod 6
> has its $p = 2$ factor restored) to
> $L(s, \chi_6^{\mathrm{induced}}) = (1 + 2^{-s}) L(s, \chi_3)$.

(Tighten the derivation if the above is verbose; the key fact is
$\chi_3(2) = -1$ and the Euler-factor-restoration mechanism.)

Length budget: ~quarter page.

### Priority 6 — Polish the §6.4 entry-by-entry identification

**Current state.** §6.4 has a 7-row table + four paragraphs of row-by-row
justification (rows 2, 4–5, 6, with the remaining rows treated as
"direct analogues"). The table is good; the justification could be more
balanced — every row should get at least a sentence.

**Action.** For each of the 7 table rows, write one sentence of
justification:

- Row 1 (rank-1 line bundle on $\overline{\mathrm{Spec}}\,\mathbb{Z}$ ↔
  $\zeta$-channel): "The base field $\mathbb{Q}$ has Dedekind zeta
  $\zeta(s)$; this is the trivial rank-1 line bundle, identified with
  the K-fixed $\zeta$-channel of Theorem 5.2."
- Row 2 (Galois cover line bundle ↔ 2-channel pair): keep current
  justification.
- Row 3 (Arakelov metric ↔ Bures Hermitian metric): expand current
  justification to: "On a rank-1 line bundle the Arakelov norm is a
  Hermitian metric; for the Galois-cover line bundle viewed as
  $\mathbb{C}^2$, this is the Fubini-Study/Bures metric
  $h = (|\Xi|^2 + |\mathcal{L}_3|^2)^{-1}$ on the 2-channel pair, as
  developed in HPo Addendum C1."
- Row 4 (combinatorial datum): keep current justification.
- Row 5 (Galois involution = K-involution): keep current justification.
- Row 6 (singular strata): keep current justification.
- Row 7 (tensor product = adele product): "The Galois cover's
  $\zeta_K = \zeta \cdot L_{\chi_3}$ is the multiplicative product
  corresponding to the tensor product of the underlying line bundles;
  this is the Dedekind factorization at the L-function level."

Length budget: ~half a page added.

---

## Anti-Patterns to Avoid in the Refinement Pass

1. **Do not redraft any section structurally.** The §1 through §7
   organization is correct. Edit in place.

2. **Do not change the title or abstract.** They were written backward
   from the body and faithfully summarize the body. If a body change
   warrants an abstract tweak, make the minimum-necessary tweak.

3. **Do not add new theorems.** The 11 claim objects (T1.1, T1.2, T1.3,
   I1.4, T2.1, T2.2, T2.3, T3.1, T3.2, T3.3, I3.4 + bonus T5.3) are the
   complete set. Refinement adds clarity, not content.

4. **Do not drift into Paper II / Paper III terrain.** Same boundary
   as the first-draft session.

5. **Do not re-derive the trilogy.** Same as first draft.

6. **Do not pad.** If a sentence is already clear, leave it. The pass
   should add ~2–3 pages total, not 10.

7. **Do not edit `siete.md`, `HPo-notes.md`, or other source documents.**
   Those are upstream. If you find an error, note it in
   `Note_PaperI_Pass1_<finding>_<suffix>.md` for later integration.

---

## Working Sequence

**Move 1 — Re-ground (~30 minutes)**.

1. Read `Note_PaperI_Draft1_StatusReport_2026-05-22.md` — full file.
2. Read `Paper-I-Identification-Draft1.md` — full file. (Take notes on
   any internal inconsistencies you spot beyond the six priorities.)
3. Re-run the two probes to confirm numerical claims are still valid:
   ```powershell
   python empirical/probe_Hurwitz_z6_closed_form.py
   python empirical/probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py
   ```
4. Read HPo Addendum A5 (lines 407-421) and Addendum A1 (lines 332-348)
   for Priority 2 explicit-formulas reference.

**Move 2 — Discharge priorities in order**.

For each of the six priorities:
- Locate the relevant section / subsection of Paper I.
- Use Edit (not Write) to make the change in place.
- Verify the change reads cleanly with surrounding text.
- Move to the next priority.

**Move 3 — End-to-end read**.

After all six priorities are discharged, read the manuscript end-to-end.
Look for:
- Internal contradictions or duplicate statements introduced by the
  refinements.
- Cross-references that now point to wrong section numbers (none
  expected, but verify).
- Sentence flow at the boundaries of edited passages.
- Theorem numbering consistency.

Fix any issues found.

**Move 4 — Status note**.

Write `Note_PaperI_Pass1_StatusReport_<date>.md` summarizing:
- The six priorities discharged (with brief description of each
  change).
- Any new issues found and fixed during end-to-end read.
- Any remaining issues that did not warrant a fix in Pass 1 (these
  become Pass 2 priorities, if a Pass 2 is later commissioned).
- Updated word count / page count.
- Honest calibration on whether the manuscript now reads cleanly.

---

## What Pass 1 Is and Is Not

**Pass 1 IS**:
- A controlled refinement of the first-draft manuscript.
- Discharge of six specific, bounded priorities identified in the
  Move-7 status report.
- An end-to-end consistency check.
- ~2–3 pages of net length added.

**Pass 1 IS NOT**:
- A redraft.
- A reorganization.
- An expansion of scope.
- An addition of new theorems or new content beyond clarification.
- A re-derivation of any classical result.

---

## Success Criteria

**Strong success**:
- All six priorities discharged with the changes recorded in the Move-4
  status note.
- Manuscript reads cleanly end-to-end.
- Title, abstract, theorem numbering, and section structure unchanged.
- Net length: 42–48 pp (from baseline ~40–45 pp).
- No drift outside Paper I scope.

**Partial success**:
- Four or five of six priorities discharged; one or two deferred to
  Pass 2 with reason recorded.
- One or two minor end-to-end inconsistencies caught and fixed.

**Failure modes to avoid**:
- Redrafting beyond the six priorities.
- Adding new theorems.
- Length blowing up past 55 pp.
- Drift into Paper II / Paper III terrain.

---

## Tools at Your Disposal

- The Read tool for files (especially the manuscript and status report).
- The Edit tool for in-place changes to the manuscript. **Prefer Edit
  over Write.**
- The Bash / PowerShell tool for re-running probes.
- The Grep tool for locating specific equations or terms in the
  manuscript.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` —
  generally not needed for Pass 1, but available if you discover
  something durable.

**Do not create `Paper-I-Identification-Draft2.md`.** All edits go into
`Paper-I-Identification-Draft1.md`.

**Empirical probes** that you write (if any) go in `empirical/` with the
pattern `probe_PaperI_Pass1_<claim>_<suffix>.py`.

**Do not edit `siete.md`, `HPo-notes.md`, or the trilogy files.**

**Commits**: do not commit anything unless explicitly asked.

---

## The Big Picture, One Paragraph

The first draft of Paper I established the right content: $\log\zeta$ as
the categorical effective action on the prime-axis simplex; the
closed-form cubic A-C tensor on $\mathbb{Z}/N$; the critical line as the
$N$-uniformity locus; the $\mathbb{Z}/6$ 2D collapse to $(\zeta, L_{\chi_3})$;
the Galois identification with $\mathbb{Q}(\sqrt{-3})$. The Move-7 status
report identified six places where the first draft was correct in
substance but could be more rigorous, more explicit, or better-supported
by numerical display. Pass 1 discharges those six priorities. It does
not redraft, reorganize, or expand scope. The result is the same
manuscript, more polished, ready for whoever reads it next (collaborators,
external referees, or the Paper II author).

**Go**.
