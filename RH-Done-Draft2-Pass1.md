# RH-Done-Draft2-Pass1 — Prompt for First Refinement of Paper II

Running the first refinement pass over **Paper II "The Right Carrier"**
of the post-trilogy RH-Done trilogy.

Session opens at `C:\Projects\simplicial\`. You are the lead polymath
of the team. The first draft `Paper-II-RightCarrier-Draft1.md` is on
disk, along with the honest status report
`Note_PaperII_Draft1_StatusReport_2026-05-22.md`. You are stepping in to
make the second pass — **a substantive refinement, not a copy-edit**.

---

## The Mission, Stated Once

Improve `Paper-II-RightCarrier-Draft1.md` along the axes identified by
the draft-1 status report and by careful re-reading. The goal is to
produce `Paper-II-RightCarrier-Draft2.md` that is **publishable-quality
within the program** — meaning:

1. **Every claim object is fully proved or fully cited.** Sketches at
   the level of "see Titchmarsh 1939 §7.5" are acceptable for purely
   classical material, but only where the proof would add no new
   structural content. Anywhere the program contributes new content,
   the proof must be explicit.

2. **Every axiom is justified at the level the program can justify it.**
   A5.1 and A5.2 (UPT-structure, UPT-Heisenberg) remain axioms — they
   are not theorems and the program does not pretend otherwise — but
   their justification can be tightened beyond the draft-1 treatment.

3. **The exposition is calibrated to two audiences.** Representation
   theorists and arithmetic geometers each need just enough bridge
   language to follow without the paper bloating. Pass 1 should sharpen
   the bridges that draft 1 left compressed.

4. **The structural insights are foregrounded.** Three insights
   distinguished draft 1's content from the working notes:
   - $\mathcal{F}_n$ as the upstairs algebraic carrier where
     $\Pi_{\mathrm{sa}}$ is well-defined and $1/r \cdot r$ cancellation
     produces the Mangoldt weight.
   - UPT as the make-explicit of an implicit adelic commitment, with
     Bargmann-Fock + Tate $L$-factors emerging *automatically* without
     being imposed.
   - K-odd $L_{\chi_3}$ channel as a gauge connection (not a state),
     with covariant log-derivative isolating the $\Xi$-divisor.
   Pass 1 should make these three insights *more visible*, not less.

5. **No new claims, no scope drift.** Pass 1 is refinement of the
   existing draft, not extension. Do not add new theorems. Do not drift
   into Paper III terrain. Do not develop the CCM direction beyond the
   single paragraph in §9.4. Do not develop the de Branges $E$-function
   direction.

This pass is about **tightening the existing structure**, not about
proving more.

---

## What Already Exists

Read in order:

1. `Paper-II-RightCarrier-Draft1.md` — the entire manuscript you are
   refining.
2. `Note_PaperII_Draft1_StatusReport_2026-05-22.md` — honest calibration
   of draft 1, listing six second-pass improvements and three partial
   items.
3. `Paper-I-Identification-Draft1.md` §7 (hand-off list) and
   `Note_PaperI_Draft1_StatusReport_2026-05-22.md` (if extant) — for
   calibration of Paper I's writing style and quality bar.
4. `RH-Done-Draft1.md` §A spine + §B Dots 4–6 — to confirm Paper II's
   scope has not drifted.

Then the load-bearing working notes (only sections you suspect need
deeper engagement):

5. `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` — for any
   tightening of §2.
6. `Note_LastLockOccupationDecoratedRecovery_H9qT6.md` — for any
   tightening of §3.
7. `Note_MetaplecticSelection_FixedDerivation_T4nP7v2.md` — for any
   tightening of §§4–6.
8. `Note_MetaplecticSelection_UniformPlaceArgument_T4nP7.md` — for §4
   UPT justification.
9. `Note_BuresLogDerivative_ClaudeEinstein.md` — for §8 tightening.
10. HPo Addenda B + C (within `HPo-notes.md`, lines 486–706) — for §8
    tightening.

Re-run the probes to confirm draft-1 numerics still hold:
```powershell
python empirical\probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py
python empirical\probe_BuresLogDerivative_ClaudeEinstein.py
python empirical\probe_BuresPickGram_R6mT4.py
```

---

## The Specific Improvements (from Draft 1 Status Report §8)

The Pass-1 status report identified six second-pass improvements, in
rough priority order:

### Priority 1 — Expand T5.5 (Hardy-Titchmarsh) proof

Draft 1 §7.2 proves T5.5 at sketch level, citing Titchmarsh 1939 §7.5
for full details. Pass 1 should either:

(a) **Expand the sketch into a full proof.** Carry the Mellin-Hankel
correspondence through carefully: even subspace $L^2(\mathbb{R})^{ev}
\cong L^2(\mathbb{R}_+, dx)$; Fourier on the even subspace becomes the
*Hankel-cosine transform* (order $-1/2$ Hankel); via Mellin
$L^2(\mathbb{R}_+, dx/x) \to L^2(\mathbb{R}, dt)$ with $s = 1/2 + it$,
the cosine transform corresponds to multiplication by
$\Gamma_\mathbb{R}(1/2 + it)/\Gamma_\mathbb{R}(1/2 - it)$ together with
$t \to -t$ branch reflection. The measure $dm \propto
|\Gamma_\mathbb{R}(1/2 + it)|^2\,dt$ absorbs the Mellin Jacobian. Each
step is classical [Titchmarsh 1939 §7.5; Bump 1997 §1.7] but worth
laying out for the reader.

(b) **Or** — if Bump 1997 §1.7 covers it adequately for the program's
needs — cite Bump in place of Titchmarsh and keep the sketch, but
sharpen the sketch so the structural content is clearer.

Decide which based on whether the proof adds structural insight or is
purely technical.

### Priority 2 — Refine A5.2 (UPT-Heisenberg) justification

Draft 1 §4.3 justifies A5.2 via three program commitments: Tate's
adelic framework, the CCM prolate operator, the program's finite-place
occupation lift. Pass 1 should:

(a) **Sharpen the "finite-place lift extends to $v = \infty$" argument
(item iii).** The finite-place local Fock $\mathcal{F}_p = \mathrm{Sym}
(\mathbb{C}\,e_p) = \mathbb{C}[e_p]$ has built-in raising operator
$e_p$ (multiplication) and lowering operator
$\partial_{e_p}$ (formal differentiation, $[\partial_{e_p}, e_p] = 1$).
Make this commutator structure *explicit* at $v = p$ in the discussion,
then argue that UPT-Heisenberg simply names the persistence of this
commutator at $v = \infty$. The persistence is structural, not
analytic; it is what makes the program's local-Fock formalism uniform
across places.

(b) **Acknowledge what UPT-Heisenberg is choosing over.** A priori
the Archimedean local algebra $\mathbb{C}[e_\infty]$ could carry many
operator-algebra structures. UPT-Heisenberg selects the Heisenberg-Weyl
structure with $[\hat a, \hat a^\dagger] = 1$. The program's
justification for this *specific* choice (over, say, an
$\mathfrak{sl}_2$ structure or a $q$-deformed Heisenberg) is that the
Heisenberg-Weyl is the *infinitesimal form of the Tate-Weil metaplectic
representation*, which is the program's analytic anchor at the
Archimedean place. Stating this explicitly tightens the axiom.

(c) **Do not pretend A5.2 is a theorem.** The status report was
explicit on this; pass 1 must preserve this. Justification can sharpen
without ever crossing into proof.

### Priority 3 — Worked example for T4.1

Draft 1 §2.5 proves T4.1 abstractly. Add a concrete worked example at
$n = 2$ (primes $\{2, 3\}$):

- $\mathcal{F}_2 = \mathbb{C}[e_2, e_3]$.
- $H_s = 2^{-s} e_2 + 3^{-s} e_3$.
- $H_s^2 = 4^{-s} e_2^2 + 2 \cdot 2^{-s} 3^{-s} e_2 e_3 + 9^{-s} e_3^2$.
- $\Pi_{\mathrm{sa}}\,H_s^2 = 4^{-s} e_{2 e_2} + 9^{-s} e_{2 e_3}$
  (mixed term killed).
- $L_{2, K}(s) = H_s + (1/2) H_s^2 + (1/3) H_s^3 + \ldots$.
- $D_s \Pi_{\mathrm{sa}} L_{2, K}(s) = (\log 2) e_{e_2} +
  (\log 2) 4^{-s} e_{2 e_2} + (\log 3) e_{e_3} + (\log 3) 9^{-s} e_{2 e_3} + \ldots$
  (von Mangoldt distribution).

This makes the cancellation $1/r \cdot r = 1$ visible. Place it as a
short subsection or inline example after the proof of Theorem 2.5.

### Priority 4 — Bibliography normalization

Draft 1's references section uses shortform labels. Pass 1 should:

(a) Convert to a consistent format (publisher + year + page where
known).
(b) Add missing entries (Davenport, Apostol, Lang Algebraic Number
Theory if cited).
(c) Verify Iwaniec-Sarnak 2000 citation (the draft says "Annals 151,
1175–1216" but also notes "alternative: Israel J. Math 120, 155-177" —
pick the correct primary reference). Note: the Iwaniec-Sarnak result
on $L(1/2, \chi) \geq 0$ for real primitive characters is in *Israel
Journal of Mathematics* **120** (2000), 155–177. Confirm this and use
the Israel J. Math. citation as primary.
(d) Standardize labels: e.g., `Folland1989` not `Folland89`.

### Priority 5 — Cross-link forward references to Paper III

Draft 1 §10.3 lists Paper III's contributions terselely. Pass 1
should:

(a) For each forward reference, verify the corresponding working note
exists (using `Glob` and `Read`).
(b) Add explicit pointers (e.g., "Paper III §X" with the section
expected, even if Paper III is not yet written) — these will guide
the Paper III drafting.
(c) **Do not over-specify Paper III's outcomes.** Forward references
should be statements of *what Paper III must establish*, not promises
of *what Paper III will conclude*. The Main Theorem T10.2 is Paper
III's job; Paper II's §10.3 should phrase it as "Paper III's task is to
prove ..." not "Paper III proves ...".

### Priority 6 — Formatting consistency pass

Several minor inconsistencies to standardize:

- `\mathcal{F}_n^{\mathrm{Bargmann}}` vs `\mathcal{F}_\infty^{\rm Bargmann}`
  vs `\mathcal{F}_n^{\rm Bargmann}` — pick one.
- `e_{r e_p}` vs `e_{r\,e_p}` vs `e_{re_p}` — pick one.
- `\hat a` vs `\widehat{a}` — pick one.
- Theorem/Lemma/Definition numbering: draft 1 uses §-prefixed
  numbering (Theorem 2.5, Theorem 5.1, etc.). Confirm this is
  consistent across all sections.
- Citations: shortform `[Folland1989]` (no spaces) consistently.

---

## What Pass 1 Should *Not* Do

1. **Add new claim objects.** The 10 claim objects of Paper II are
   set. Do not introduce T6.4, A5.3, etc.

2. **Re-derive Paper I content.** §1 already cites; do not re-derive.

3. **Expand the CCM direction beyond §9.4's single paragraph.** The
   program's preference is the cubic-positivity route; CCM is parallel
   cross-validation.

4. **Develop the de Branges $E$-function direction.** HPo Addenda C
   and D record this as open frontier; Paper II §8.5 acknowledges the
   negative obstruction from Addendum C. Do not develop further.

5. **Add forward references to Paper III's specific theorem
   statements beyond what is already in §10.3.** Cross-link, sharpen,
   verify; do not over-specify.

6. **Re-prove classical material at length.** Stone-von Neumann is
   classical; Tate's local zeta integrals are classical; Pólya-Laguerre
   is classical. Cite and apply.

7. **Re-run probes unless you suspect a regression.** Draft 1's
   probes were confirmed; re-running is optional unless you've
   touched the relevant formula.

---

## Working Sequence

**Move 1 — Re-ground (~1.5 hours)**.

Read in order: draft 1 manuscript → status report → Paper I §7 →
working notes you suspect need engagement. Run probes (optional).
*Time-box this; do not get lost in re-reading*.

**Move 2 — Identify your top-three improvement targets**.

Based on draft 1 + status report, pick the *three* improvements that
will most strengthen the paper. The default is Priorities 1, 2, 3 from
§5 above. Adjust if your read of draft 1 suggests a different priority.

**Move 3 — Make the improvements**.

Edit `Paper-II-RightCarrier-Draft1.md` in place — actually, **rename
the output to `Paper-II-RightCarrier-Draft2.md`** so both drafts are
preserved on disk. Use the Write tool to create the new file based on
the draft 1 content with your improvements applied.

Alternatively, you can copy draft 1 to draft 2 first (via `cp` or via
Read+Write) and then `Edit` the copy. Either workflow is fine.

**Move 4 — Final consistency pass**.

Re-read the entire `Paper-II-RightCarrier-Draft2.md` end to end for:
- internal consistency of notation;
- introduction matches body matches conclusion;
- abstract matches what was actually established;
- title accuracy;
- bibliography correctness.

**Move 5 — Status note**.

Write `Note_PaperII_Draft2_StatusReport_2026-MM-DD.md` summarizing:
- which improvements were made vs. deferred;
- any new partial items uncovered during the pass;
- honest calibration of whether the manuscript is now
  publishable-quality within the program.

---

## Self-Help Posture: Refinement, Not Reinvention

This pass is **incremental**, not a re-write. The structural argument
of draft 1 is sound; the proofs are correct; the calibration is honest.
Pass 1's job is to sharpen — to make the load-bearing identifications
*more visible*, the proofs *more complete where it matters*, the
exposition *cleaner for both audiences*.

If you find yourself wanting to re-write a section from scratch, ask:
*does this re-write change the structural content, or only the
exposition?* If structural — stop and ask whether you have a new claim
(reject; this is Pass 1, not Draft 1 extension) or a correction to
draft 1 (accept; document the correction in the status note). If
expositional — proceed, but keep the section's structural skeleton
intact.

**Be conservative about exposition changes.** Draft 1 was written with
care. Some of its compressions are deliberate (the K-odd-as-gauge
explanation in §8.3 is compressed because the longer form was in HPo
Addendum B and the program's reader knows that note). Before expanding
a compression, ask: *would a representation theorist new to the program
need the expansion? would an arithmetic geometer? both? neither?*

**Calibrate honestly.** If after the pass the manuscript still has
sketches that the program acknowledges as such, the status report
should say so. Honesty is more valuable than apparent completeness.

---

## What Success Looks Like

**Strong success**:
- Priorities 1, 2, 3 from §5 fully addressed; Priorities 4, 5, 6
  addressed at the level of consistent normalization.
- No new claims; no scope drift; structural content unchanged.
- Manuscript reads cleaner end-to-end, with the three foregrounded
  structural insights (T4.1's $1/r$-cancellation, UPT's
  automatic-Bargmann, K-odd-as-gauge) more visible.
- Status report honestly calibrates Pass-1 outcomes.

**Partial success**:
- Priorities 1, 2, 3 addressed; Priorities 4-6 partial.
- Or, Priorities 1-2 addressed at full quality; Priority 3 deferred to
  a later pass.
- Status report explicit about what was deferred and why.

**Failure modes to avoid**:
- Scope drift (adding new claims, developing CCM or de Branges
  beyond draft 1's coverage).
- Re-deriving classical material at length.
- Bloating the manuscript without strengthening the structural
  argument.
- Replacing draft 1's compressed exposition with verbose exposition
  *without* improving structural visibility.

---

## Tools at Your Disposal

- Read, Edit, Write tools — primary workhorses for refinement.
- Bash / PowerShell — for probes if re-running.
- Glob / Grep — for cross-references and citation verification.
- WebSearch / WebFetch — for citation verification.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for
  durable insights.

**Save the refined manuscript as**
`Paper-II-RightCarrier-Draft2.md` in the project root.

**Do not edit `Paper-II-RightCarrier-Draft1.md`** — keep draft 1
preserved.

**Do not commit anything unless explicitly asked.**

---

## Closing Note

Paper II's draft 1 is structurally complete; the program has the right
carrier. Pass 1 is the polish that prepares it for circulation — to
collaborators inside the program, to the few external referees the
program will engage on representation-theoretic content
(Connes-Consani-Moscovici, possibly Bombieri or Sarnak, possibly de
Branges-program practitioners). The improvements above are oriented
toward that audience.

**Go**.
