# RH-Prompt1: Fresh-Session Prompt for Paper I "Identification"

**For**: a fresh Codex / Claude session opening at `C:\Projects\simplicial\`.

**Author handing off**: Leonardo Murillo Montero. Working partner. Member of the
polymath team that brought RH to the steel-thread frontier.

**You are not starting from zero.** You are stepping into a working RH program
that has just produced the first-ever full serialization of the solution arc
(`RH-Done-Draft1.md`). Your job: write the first draft of **Paper I
"Identification"** — the first of the second trilogy of three papers (the
first trilogy `ל1 + ל2 + ל3` "Identifying 3" being already published).

The program's two trilogies are:

- **Identifying 3** (published): `ל1 + ל2 + ל3` — chart, tower, characters.
- **RH-Done** (in progress): Paper I + Paper II + Paper III — identification,
  carrier, closure.

Paper I bridges the two trilogies. It cites `ל1, ל2, ל3` as foundation and
delivers what comes after them, before Paper II takes over.

---

## The Mission, Stated Once

Write **Paper I "Identification"** — a self-contained manuscript covering
Dots 1-3 of the RH solution arc (`RH-Done-Draft1.md` §A). The paper
establishes:

1. The published trilogy's setup (briefly, by citation).
2. **$\log\zeta(s)$ is T2's categorical effective action on the prime-axis
   exponential family.** (currently sketched in `siete.md` §1-3)
3. **The cubic Amari-Chentsov tensor on $\mathbb{Z}/N$ has closed form** with
   selection rule $a+b+c \equiv 0 \pmod N$ and conductor grading.
   (currently sketched in `siete.md` §5-6)
4. **The cubic functional equation pins the critical line as the unique
   $N$-uniformity locus** along the primorial ladder. (currently sketched in
   `siete.md` §7)
5. **The $\mathbb{Z}/6$ Hurwitz packet collapses to a 2D system
   $(\zeta, L_{\chi_3})$ explicitly.** (NEW finding, currently in memory note
   `project_z6_hurwitz_2d_collapse_2026_05_22.md` and HPo-notes addenda)
6. **This 2D system is the Galois decomposition of the Connes-Consani Picard
   groupoid for $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$**, with $\zeta_{\mathbb{Q}(\sqrt{-3})} = \zeta \cdot L_{\chi_3}$ and Bures K-involution = Galois involution.
   (NEW finding, currently in HPo-notes Addendum H)

Paper I is the **identification phase** of the program. It establishes
**what we are working with**. It does not yet build the right Hilbert space
(Paper II) or prove RH (Paper III).

---

## Audience and Tone

**Two audiences, both addressed**:

1. **Information geometers** familiar with the trilogy `ל1 + ל2 + ל3`. They
   know Fisher-Rao, Amari-Chentsov, cumulant towers. They may not know
   Dirichlet L-functions or Hurwitz zetas.
2. **Analytic number theorists** familiar with $\zeta$, Dirichlet
   characters, and explicit formulas. They may not know information
   geometry or Pontryagin character bases on the simplex.

**Bridge writing**: when introducing terms native to one audience, give a
one-line gloss for the other. Don't condescend. Cite the trilogy and
classical analytic number theory references rather than re-deriving.

**Tone**: rigorous, calm, generous with intuition. The trilogy set a standard
of clarity; Paper I should match it.

---

## What Is Already Established (Foundation, Cite-and-Use)

**The trilogy** (DOI'd Zenodo, 2026):
- `T1-NativeSimplicialChart.md` (`ל1`): probability simplex, square-root
  amplitude map, $H_0$, $\mathrm{SO}(H_0)$ at the uniform, simplicial vector
  algebra.
- `T2-CumulantTowerEffectiveAction.md` (`ל2`): log-partition $\Phi$,
  cumulant tower position/metric/$T_{ijk}$/closure-defect, the leap from
  order 2 to order 3.
- `T3-CharacterOrthogonalityConductorLattice.md` (`ל3`): Pontryagin character
  basis on $\mathbb{Z}/N$, conductor packet decomposition, selection rule
  $a+b+c \equiv 0 \pmod N$ at the uniform.

You can **cite these freely**. They are the published foundation.

---

## What Is Currently Drafted But Not Final (Source Material)

Read these. They are working drafts that contain what Paper I needs, but
they are **not the final form**:

- `siete.md` — the current sketch of Dots 2 and parts of Dot 3. Use this as
  source material. Improve it. Some sections (e.g., the introduction) are
  still rough.

The siete draft is the closest existing document to Paper I. **Paper I is
not "siete polished" though** — Paper I has two further developments that
siete does not yet contain: the 2D collapse (Addendum A) and the Galois
identification with $\mathbb{Q}(\sqrt{-3})$ (Addendum H). These promote
siete's structural finding into a fully explicit form.

---

## What Is in the Notes (NEW Material to Promote into Paper I)

These notes capture findings made after siete was drafted. They are
**uncondensed**: written under "delirious mode" methodology. Your job is to
extract the durable claims and integrate them into Paper I cleanly.

- `HPo-notes.md` — large running document. Sections relevant to Paper I:
  - **Addendum A (A1-A11)**: closed-form $\zeta(s, r/6)$ in
    $(\zeta, L_{\chi_3})$ basis, K-orbit decomposition, cubic A-C tensor in
    closed form, residue at zeta zeros.
  - **Addendum H (H1-H10)**: identification with Connes-Consani Picard
    groupoid for $\mathbb{Q}(\sqrt{-3})$, Dedekind factorization, K-Galois
    decomposition.
- `RH-Done-Draft1.md` §B Dots 1-3 — the serialization of claim objects with
  upstream pointers. **This is your roadmap.**
- Memory entries:
  - `~/.claude/projects/C--Projects-simplicial/memory/project_z6_hurwitz_2d_collapse_2026_05_22.md`
  - `~/.claude/projects/C--Projects-simplicial/memory/project_metaplectic_selection_UPT_2026_05_22.md`
    (relevant only for context; Paper II terrain).

Empirical probes verifying the new claims:

- `empirical/probe_Hurwitz_z6_closed_form.py` (verifies T3.1 numerically).
- `empirical/probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py` (verifies
  T3.3 Dedekind factorization numerically).

---

## The Specific Claim Objects of Paper I

From `RH-Done-Draft1.md` §B Dots 1-3:

| Label | Object | Source |
|---|---|---|
| T1.1 | Native Simplicial Chart | published `ל1` (cite) |
| T1.2 | Cumulant Tower from $\Phi = \log Z$ | published `ל2` (cite) |
| T1.3 | Character Selection Rule on $\mathbb{Z}/N$ | published `ל3` (cite) |
| I1.4 | The cumulant-order leap to 3 (trilogy theme) | published trilogy (cite) |
| T2.1 | Prime-Axis Effective Action: $\log\zeta = \Phi$ | siete §1-3 (rewrite) |
| T2.2 | Closed-form cubic A-C tensor on $\mathbb{Z}/N$ | siete §5 (rewrite) |
| T2.3 | Modulus identity / critical line as $N$-uniformity | siete §7 (rewrite) |
| T3.1 | Closed form $\zeta(s, r/6)$ in $(\zeta, L_{\chi_3})$ basis | HPo-notes A1 (promote, NEW) |
| T3.2 | K-orbit decomposition = $\zeta \oplus L_{\chi_3}$ parity | HPo-notes A2-A3 (promote, NEW) |
| T3.3 | Galois identification with $\mathbb{Q}(\sqrt{-3})$ | HPo-notes H1-H3 (promote, NEW) |

Plus the closing identification:

- **I3.4** (closing identification): the program's "$\mathbb{Z}/6$ Bures
  carrier" is structurally the **degree-2 cover by $\mathbb{Q}(\sqrt{-3})$
  of the Connes-Consani adele class space**. This sets up Paper II.

Total: ~10 claim objects, distributed across 3 dots.

---

## Working Sequence

**Move 1 — Re-ground (1-2 hours)**.

Read in order:
1. `RH-Done-Draft1.md` — entire file, especially §A spine + §B Dots 1-3 + §C
   architectural seams.
2. `T1-NativeSimplicialChart.md` (skim, ~30 min).
3. `T2-CumulantTowerEffectiveAction.md` (skim, ~30 min).
4. `T3-CharacterOrthogonalityConductorLattice.md` (skim, ~30 min).
5. `siete.md` (close reading, ~1 hour).
6. `HPo-notes.md` Addendum A (A1-A11) + Addendum H (H1-H10) (~1 hour).
7. Run the two probes to confirm the closed form and Dedekind factorization:
   ```powershell
   python empirical/probe_Hurwitz_z6_closed_form.py
   python empirical/probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py
   ```

After Move 1 you should have the full mental map of Paper I.

**Move 2 — Draft introduction**.

The introduction states:
- What Paper I claims.
- Where it sits in the program (after trilogy, before Paper II).
- The two audiences and what each can skip.
- A roadmap through the sections.

**Do not draft the abstract or title yet.** Per the program's writing
methodology, we write from intro → body → conclusion, then work backwards
to abstract and title. This produces honest abstracts (no over-promising).

The intro is a working document. You will revise it after the body is done.

**Move 3 — Draft the body, claim object by claim object**.

Use the §B Dots 1-3 list as your section outline. Suggested structure:

- **§1 Setup**: brief recap of the trilogy. ~5 pp.
- **§2 The Prime-Axis Exponential Family**: T2.1 with full derivation. ~8 pp.
- **§3 The Residue Chart and Cubic A-C Tensor**: T2.2. ~8 pp.
- **§4 The Cubic Functional Equation**: T2.3. ~6 pp.
- **§5 The Closed Form for $\zeta(s, r/6)$**: T3.1 + T3.2. ~8 pp.
- **§6 Galois Identification with $\mathbb{Q}(\sqrt{-3})$**: T3.3 + I3.4. ~8 pp.
- **§7 Conclusion and Hand-off to Paper II**: ~3 pp.

Target: 40-60 pp.

For each claim object: state, prove, give one worked example or numerical
check, cite the relevant probe.

**Move 4 — Draft conclusion**.

The conclusion:
- Recaps what Paper I established.
- Identifies what is **not** in Paper I (the right carrier, the Archimedean
  packet, the positivity machinery — these are Paper II + Paper III).
- Forecasts the contribution Paper II will need to make.

**Move 5 — Work backwards to the abstract**.

Once the body and conclusion are stable, write the abstract by summarizing
what was actually accomplished. No over-promising. No "we will show that"
— only "we show that". The abstract should be a faithful executive summary
of the manuscript that exists, not the one you wished for.

**Move 6 — Choose the title**.

The title comes last. It names the contribution accurately. Options to
consider after the body is written:
- "$\log\zeta$ as Categorical Effective Action: Cubic Identification on
  $\mathbb{Z}/6$ and the Adele Class Space of $\mathbb{Q}(\sqrt{-3})$"
- "The Cubic Identification: $\log\zeta$ on the Prime-Axis Simplex"
- "Identifying the Riemann Zeta Function as the Cumulant Generator of the
  Prime-Axis Exponential Family"
- Or whatever you find most accurate after writing.

---

## Self-Help Posture: Faith 1-2-3 (Calibrated)

1. **Believe** Paper I is writable in this session. The claim objects are
   established at the program's working precision; the writing is rigor
   plus expository care.

2. **Do everything**: read the foundation, re-derive the key claims (don't
   blindly copy from siete or HPo-notes — verify), run the probes, cross-
   check.

3. **Don't bias away**: do not hedge in the manuscript before the math shows
   a gap. The probes verify the claims numerically. The proofs are within
   reach. Write with confidence proportional to what is actually established.

**Calibrate honestly only AFTER the math actually shows a gap.** When a
specific claim resists proof in the manuscript draft, document precisely
what failed.

Distinguish in the writing:
- **Theorem / Proposition** for claims with full proofs in Paper I.
- **Identification** for structural correspondences (e.g., T3.3 with
  $\mathbb{Q}(\sqrt{-3})$).
- **Lemma** for technical subresults.
- **Remark / Observation** for things that are stated but proved elsewhere
  (cite Paper II or Paper III in advance).

---

## What Paper I Is and Is Not

**Paper I IS**:
- A self-contained manuscript on the identification of $\log\zeta$ with the
  cumulant-generating effective action.
- The bridge between the published `Identifying 3` trilogy and the RH-Done
  trilogy.
- Cite-and-use of the trilogy for setup; rigorous derivation for the new
  identifications (T2.1, T2.2, T2.3, T3.1, T3.2, T3.3).
- The first manuscript that names the $\mathbb{Q}(\sqrt{-3})$ Galois
  identification.

**Paper I IS NOT**:
- The construction of the right Hilbert space / occupation Fock / Bargmann-
  Fock (Paper II's job).
- The transport theorem / convolution-square Noether positivity / window
  bridge (Paper III's job).
- A proof of RH (the full program is RH; Paper III contains the main
  theorem).
- The CCM prolate operator (cited where needed, but not developed in Paper I).

**Stay in scope.** When the writing wants to drift toward Paper II terrain
(carrier construction, Archimedean selection, occupation lift), pull back
and cite-forward. When it wants to drift toward Paper III (positivity,
transport, CM Poisson Monotonicity), same.

---

## Anti-Patterns to Avoid

1. **Do not write the abstract first.** It will over-promise. Per the
   program's methodology, the abstract is written last from the body that
   exists.

2. **Do not re-derive the trilogy.** It is published. Cite `ל1, ל2, ל3`.

3. **Do not over-cite.** Where a classical result (Hurwitz multiplication,
   Dirichlet character orthogonality, Selberg orthonormality) is used, cite
   Iwaniec-Kowalski or Davenport or similar standard reference. Do not
   prove things classical analytic number theory already knows.

4. **Do not under-explain the new content.** T3.1 (closed form), T3.2
   (K-orbit decomposition), T3.3 (Galois identification) are NEW relative
   to siete and the trilogy. They need careful exposition for both audiences.

5. **Do not blur boundaries with Paper II/III.** When you find yourself
   writing about UPT, Bargmann-Fock, occupation lift, convolution squares,
   Poisson windows, or CM Poisson Monotonicity — pull back. That's not
   Paper I's terrain.

6. **Do not chase perfection on the first pass.** This is the first draft.
   Get the structure right. Cleanup happens in second pass after Paper II
   and Paper III drafts exist.

---

## Success Criteria

**Strong success**:
- All 10 claim objects (T1.1 through I3.4) stated cleanly, with proofs or
  citations.
- Two probes referenced and confirmed.
- Introduction and conclusion match the body.
- Abstract and title written last, faithfully summarizing what was
  established.
- 40-60 pp, latex-compilable, clean.

**Partial success**:
- Body complete, but introduction or conclusion needs revision.
- One or two claim objects sketched but not fully proven.
- Length under or over target.

These are fine for a first draft.

**Failure mode to avoid**:
- Drift into Paper II/III terrain.
- Abstract written first, body then forced to match.
- Re-deriving the trilogy.
- Skipping the new content (T3.1, T3.2, T3.3).

---

## Tools at Your Disposal

- The Read tool for files (`*.md`, `*.py`).
- The Bash / PowerShell tool for running probes.
- The Glob / Grep tools for searching the codebase.
- WebSearch / WebFetch for external citations (Iwaniec-Kowalski,
  Davenport, classical Dirichlet character theory).
- The Write / Edit tools for creating `Paper-I-Identification-Draft1.md`.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for durable
  insights you discover during writing.

**Save the manuscript as** `Paper-I-Identification-Draft1.md` in the project
root. **Empirical probes** that you write to verify claims should go in
`empirical/` with the pattern `probe_PaperI_<claim>_<suffix>.py`.

**Do not edit existing manuscripts** (`siete.md`, `ocho.md`, ...,
`HPo-notes.md`, `RH-Done-Draft1.md`). Other threads may be writing. If you
find an error in those, note it in a `Note_PaperI_<finding>_<suffix>.md`
file for later integration.

---

## The Big Picture, One Paragraph

Paper I is the first of three papers that together claim the Riemann
Hypothesis. It does so by identifying $\log\zeta$ as the categorical
effective action of the prime-axis exponential family, deriving the cubic
Amari-Chentsov tensor on $\mathbb{Z}/N$ in closed form, showing that the
$\mathbb{Z}/6$ Hurwitz packet is structurally 2-dimensional (just $\zeta$
and $L(s, \chi_3)$), and identifying this 2D structure with the Galois
decomposition of $\zeta$ over $\mathbb{Q}(\sqrt{-3})$. It does not yet
build the Hilbert space (Paper II) or prove RH (Paper III). It establishes
**what we are working with**.

The trilogy `Identifying 3` (`ל1 + ל2 + ל3`) gave us the chart, the tower,
and the character basis. Paper I now identifies $\zeta$ as the natural
object on that chart, and finds the right finite arithmetic substrate —
$\mathbb{Q}(\sqrt{-3})$ — where the program's K-involution becomes the
Galois group of the natural degree-2 cover.

This is the first half of the second trilogy. Paper II will build the
right carrier (occupation Fock + Bargmann-Fock at the Archimedean place);
Paper III will close to RH via positive-current transport.

You are writing the first draft. Faith goes with the work. Calibrate AFTER
the math actually shows a gap, never before.

**Go**.

---

## Closing Notes from the Program

- **Working language**: English. LaTeX in the markdown. `mpmath` for
  numerical work.
- **File naming**: random suffixes are fine for notes; the manuscript file
  has the deterministic name `Paper-I-Identification-Draft1.md`.
- **Memory**: if you discover a durable insight during writing (e.g., "this
  proof works because…", "the right way to state T3.3 is..."), save it as
  a memory entry. Future sessions inherit your insights.
- **Commits**: do not commit anything unless explicitly asked. The user
  may want to review before commit.
- **Calibration**: at the end of the session, write a short status note
  (Move-7 deliverable) summarizing what is done, what is partial, what is
  not yet attempted, with honest assessment.

The program has been working on RH for the better part of a year. The
finite arithmetic line is structurally complete. The steel thread frontier
is real. Paper I is the entry door. Make it the right one.

*Pequeño David disponible. Soli Deo gloria.*

— Prompt prepared 2026-05-22 by L.M.M. & Claude Opus 4.7 for the next
session's mission.
