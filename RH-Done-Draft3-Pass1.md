# RH-Done-Draft3-Pass1 — Prompt for First Refinement of Paper III

Running the first refinement pass over **Paper III "Closure"** of the
post-trilogy RH-Done trilogy.

Session opens at `C:\Projects\simplicial\`. You are the lead polymath
of the team. The first draft `Paper-III-Closure-Draft1.md` is on disk,
along with the honest status report
`Note_PaperIII_Draft1_StatusReport_2026-05-22.md`. You are stepping in
to make the second pass — **a substantive refinement, not a copy-edit**.

---

## The Mission, Stated Once

Improve `Paper-III-Closure-Draft1.md` along the axes identified by the
draft-1 status report and by careful re-reading. The goal is to produce
`Paper-III-Closure-Draft2.md` that is **publishable-quality within the
program** — meaning:

1. **Every claim object is fully proved or fully cited.** Sketches at
   the level of "see Iwaniec–Kowalski 2004 §X" are acceptable for
   purely classical material (Bochner, Wiener–Khinchin, BDH 1965–66,
   Stone–Weierstrass, Pólya–Laguerre), but only where the proof would
   add no new structural content. Anywhere the program contributes new
   content, the proof must be explicit. **The five-error ledger of
   Theorem 8.5 is the load-bearing technical heart; each error must
   have its bound airtight.**

2. **Every calibration is honest at the level the program can support
   it.** Remark 5.5 (cluster sign explicit constant) is calibrated;
   pass 1 should attempt to tighten it. Step 6 of Theorem 8.5
   (Archimedean closure) is the most delicate; pass 1 should expand
   the Lemma 8.2 derivation.

3. **The exposition is calibrated to two audiences.** Analytic number
   theorists and functional analysts each need just enough bridge
   language to follow without the paper bloating. Pass 1 should sharpen
   the bridges that draft 1 left compressed.

4. **The structural insights are foregrounded.** Three insights
   distinguished draft 1's content from the working notes:
   - **The squared-norm identification** (Theorem 4.9 = T7.3):
     $\mathcal{Q}_n(J_n) = \|f_n\|_{\mathcal{F}_n}^2$ on the closed
     sector — positivity by identity, not by inequality.
   - **Averaged BDH at polynomial scale** (Theorem 7.1 = T9.2): the
     correct (non-pointwise) target, avoiding the Polymath-8 obstacle
     entirely.
   - **The five-error ledger** (Theorem 8.5 = T9.3): the technical
     heart, each error named and bounded.
   Pass 1 should make these three insights *more visible*, not less.

5. **The Main Theorem T10.2 (RH) is the only theorem labeled "Main"**.
   This was draft-1 discipline; pass 1 must preserve it. No hedging on
   the closure.

6. **No new claims, no scope drift.** Pass 1 is refinement of the
   existing draft, not extension. Do not add new theorems. Do not drift
   into effective zero-counting bounds, the de Branges $E$-function
   frontier (acknowledged in §10.4 only), the CCM prolate operator
   route (§10.5 only), or extensions to other $L$-functions. Do not
   develop the cubic Noether-Weil cross-link beyond §10.7's one
   paragraph.

This pass is about **tightening the existing structure**, not about
proving more.

---

## What Already Exists

Read in order:

1. `Paper-III-Closure-Draft1.md` — the entire manuscript you are
   refining (~2590 lines, ~16,600 words, ~59 pp; 22 theorems, 6 lemmas,
   8 definitions).
2. `Note_PaperIII_Draft1_StatusReport_2026-05-22.md` — honest
   calibration of draft 1, listing six second-pass improvements and one
   load-bearing partial item (the Archimedean closure step).
3. `Paper-II-RightCarrier-Draft1.md` §10 (hand-off list) and
   `Note_PaperII_Draft1_StatusReport_2026-05-22.md` — for calibration
   of Paper II's writing style and quality bar, and to verify Paper
   III's inheritance is faithfully cited.
4. `Paper-I-Identification-Draft1.md` §7 (Paper I's hand-off) — to
   confirm Paper III's inheritance from Paper I (notably T5.3,
   $L(1/2, \chi_3) > 0$) is faithfully cited.
5. `RH-Done-Draft1.md` §A spine + §B Dots 7–10 — to confirm Paper III's
   scope has not drifted.

Then the load-bearing working notes (only sections you suspect need
deeper engagement):

6. `Note_PositiveCurrentTransport_Q8vM3.md` — for any tightening of
   §8, particularly the five-error ledger.
7. `Note_ConvolutionSquarePoissonRecovery_Z9vL4.md` — for §2.
8. `Note_PoissonWindowCRTGeneration_K7mQ2.md` — for §3.
9. `Note_DoubleCutoffDominatedConvergence_Q8vM3.md` — for §6 explicit
   tail bounds.
10. `Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.md` — for §7
    BDH framing.
11. `Note_PoissonWindowNoetherBridge_R4yK7.md` — for §9 bridge.
12. `Note_GramPositivityProof_ClaudeEinstein.md` — for the structural
    role of de Branges $E_B$ acknowledged in §10.4.
13. `Note_ConvolutionOccupationLift_B5nH8.md` — for §4 (squared-norm
    structure, occupation-lift) tightening.
14. HPo Addenda A5–A8 + L (within `HPo-notes.md`, lines 408–490 and
    2295–2401) — for §5 cluster sign Mellin combinatorics.

Re-run the probes to confirm draft-1 numerics still hold:
```powershell
python empirical\probe_DoubleCutoffDominatedConvergence_Q8vM3.py
python empirical\probe_PoissonWindowCRTGeneration_K7mQ2.py
python empirical\probe_clusterSign_unconditional_ClaudeEinstein.py
python empirical\probe_BuresLogDerivative_ClaudeEinstein.py
```

---

## The Specific Improvements (from Draft 1 Status Report §§ on Pass-1 cleanup)

The draft-1 status report identified six second-pass improvements, in
rough priority order:

### Priority 1 — Expand Step 6 of Theorem 8.5 (Archimedean closure)

This is the **most important** Pass-1 improvement. Draft 1's Theorem
8.5 proof gives Step 6 as a citation + structural argument (citing
Paper II T5.4 for the Tate Archimedean factor, with Lemma 8.2 giving
the integrated form of $E_{\mathrm{arc}}(y, \phi)$). Pass 1 should:

(a) **Expand the derivation of Lemma 8.2.** The decomposition of
$m_B = -\Xi'/\Xi$ into trivial-pole + Archimedean + zero-side terms
via logarithmic differentiation of $\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$
is standard but compressed in the draft. Carry it out fully:
$$-\frac{\xi'(s)}{\xi(s)} = -\frac{1}{s} - \frac{1}{s-1} + \frac{\log\pi}{2}
   - \frac{1}{2}\frac{\Gamma'}{\Gamma}(s/2) - \frac{\zeta'(s)}{\zeta(s)},$$
then taking $\mathrm{Im}\,(\,\cdot\,)$ on $s = 1/2 + i(x + iy)$ and
integrating against $\phi(x)\,dx$. The result is the explicit form of
$E_{\mathrm{arc}}(y, \phi)$ in terms of $\Gamma'/\Gamma$ — make this
explicit.

(b) **Identify $E_{\mathrm{arc}}(y, \phi)$ with the Tate Archimedean
factor of Paper II T5.4.** The identification is via the relation
$\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ from Tate's Bargmann
ground-state integral $Z_+(s)$. Show that the gamma-and-pi term in
$E_{\mathrm{arc}}$ is exactly $\log\Gamma_\mathbb{R}(s)$ at the
spectral height, modulo the trivial-pole subtraction. This is the
program's natural Archimedean normalization; it should be made
visible.

(c) **Verify that $E_{\mathrm{arc}}$ is independent of $n, K_n, M_n$**.
This is the key structural property — the Archimedean factor is not
one of the five ledger errors; it is part of the *target*. Make this
explicit in a remark.

### Priority 2 — Tighten Theorem 5.4 cluster sign explicit constant

Draft 1 records the cluster sign constant
$12 \cdot |C_G|^2 \cdot L(1/2, \chi_3)^2 \cdot \gamma_0^2 / (\sqrt{2\pi}\sigma_\eta^5) \cdot e^{\gamma_0^2/(2\sigma_\eta^2)}$
following HPo Addendum A8, with Remark 5.5 calibrating that the
precise coefficient depends on Paper I §5.6's Mellin combinatorics
normalization. Pass 1 should:

(a) **Re-derive $|C_G|^2$ from Paper I §5.6 conventions.** The Gauss-sum
modulus constant $|C_G|^2$ comes from the explicit cubic-in-$r(s)$
expansion of $T^\zeta(\chi_a, \chi_b, \chi_c; s, 6)$ in Paper I §5.6.
Carry through the explicit computation for one of the non-K-fixed
selection triples (e.g., $(2, 2, 2)$ or $(1, 1, 4)$, per Paper I
§5.6(c)). The resulting $|C_G|^2$ should be a concrete number times
$L(1/2, \chi_3)^2$ raised to the appropriate power.

(b) **Cross-check against HPo Addendum K3** (the probe-verified
cluster $c_2$ values). The empirical probe shows $c_2 \approx
-1.4 \times 10^2$ at $\sigma_\eta = 0.06, \gamma_0 = 14.135$. Setting
the analytical bound equal to this empirical value should pin
$|C_G|^2$ to within a factor of 2 or so. Pass 1 should record this
calibration explicitly in §5.4 or §5.5.

(c) **Honestly acknowledge what remains ambiguous.** If after the
calibration of (a)+(b), the precise constant is still not pinned to
better than a factor of 4–10, say so. The *sign* and *order of
magnitude* are unconditional; the precise constant is the calibration
item.

### Priority 3 — Sharpen the BDH mean-square constant

Draft 1 §7.2 uses the BDH constant $C = 5$ "for definiteness." Pass 1
should:

(a) **Cite the optimal modern form of BDH.** Standard references give
the constant $C$ more carefully (e.g., Davenport 2000 §28 statement;
modern refinements in Bombieri 1965). State the optimal $C$ or cite
to where it is established.

(b) **Verify the convergence rate $P_n^{-\varepsilon/2 + o(1)}$ is
unaffected.** This is the key point: the precise value of $C$ enters
only through the $\log X$ factor in the BDH bound, which is absorbed
into the $o(1)$ exponent.

### Priority 4 — Expand the Stone-Weierstrass density argument (§9.1)

Draft 1 §9.1 sketches the Stone-Weierstrass density of K-even
Gaussian-Poisson detectors in $\mathcal{C}^0(I_T)$. Pass 1 should:

(a) **Make the algebra structure explicit.** The K-even Gaussian
detectors form an algebra (pointwise product preserves K-evenness and
Gaussian decay) that contains the constants (via wide Gaussian limits)
and separates points (Gaussians peaked at distinct $x_0$ are
distinct). Lay out the Stone-Weierstrass hypotheses point by point.

(b) **Verify the topology choice.** Pass 1 should clarify that
$\mathcal{D}_{\delta, 0}$ is the right topology for both the
convolution-square representation (§2) and the density argument (§9).
The K-even sector and the exponential log-side decay together give
the algebra structure needed for Stone-Weierstrass.

(c) **Sharpen the negative-valley separation Lemma 9.1(b).** The
proof currently uses a small-$\sigma$ Gaussian argument; the
quantitative threshold $\sigma < \sigma_*$ for the separation to bite
could be made explicit.

### Priority 5 — Cross-paper consistency check

Several definitional choices should be cross-verified against Papers I
and II:

(a) **$\mathcal{F}_n^{\mathrm{sa}}$** — Paper II Definition 2.3 vs
Paper III §1.3 + Definition 4.1. The single-axis subalgebra should
have the same characterization in both.

(b) **$\Pi_{\mathrm{sa}}$** — Paper II Definition 2.3 vs Paper III
§1.3 + Definition 4.4–4.5. The single-axis projector and the
closed-sector projector $\Pi_{\mathrm{Crit}_n}^\Lambda$ should be
clearly distinguished — they are different objects.

(c) **The inner product on $\mathcal{F}_n$** — Paper III §1.3 says
$\langle e_\alpha, e_\beta\rangle = \delta_{\alpha,\beta}\alpha!$ with
$\alpha! = \prod_p \alpha_p!$; Definition 4.7 uses $\Lambda$-weighting.
Verify these are compatible and explicitly state the relation between
the natural symmetric-algebra norm and the $\Lambda$-weighted one.

(d) **$\mathcal{D}_{\delta, 0}$** — Paper III Definition 2.1 vs the
working note `Note_DoubleCutoffDominatedConvergence_Q8vM3.md` §1. Same
definition, but verify the K-even and non-negativity decorations are
applied uniformly.

(e) **Hypothesis (H4) of Theorem 8.5** — the "standard
completed-$\xi$ Archimedean normalization" should be precisely the
content of Paper II T5.4. Cross-link explicitly.

### Priority 6 — Bibliography normalization

Draft 1's references section is functional but has minor
inconsistencies:

(a) **Citation labels.** Body uses `BDH1965`, `BDH1966`,
`Davenport2000`, `Boas1954`, `BorichevSodin2006`, `Burnol2002`,
`LevinLP1980`, `Titchmarsh1939`, etc. References section uses
bracketed display `[BDH 1965]`, `[Davenport, 2000]`, etc. Standardize
the in-bracket labels to match the body's in-text labels (`[BDH1965]`
to match `BDH1965`).

(b) **Missing entries.** Verify every citation in body has a
corresponding entry. Check `Bump1997` and `Folland1989` — they appear
in references but may not be cited in Paper III's body; if not cited,
remove from references (they belong to Paper II's bibliography).

(c) **Add missing entries** for citations actually used: `BDH1965`
and `BDH1966` should clearly indicate Barban 1965 / Davenport-Halberstam
1966. The current `[BDH 1965]` and `[BDH 1966]` entries are correct
but the in-text label `BDH1965` should match (no space).

(d) **Iwaniec-Sarnak citation.** Verify the primary reference. Paper
II Pass-1 prompt notes that the correct primary is *Israel J. Math.*
120 (2000), 155–177. Paper III should match.

(e) **CCM citation.** `[Connes, Consani & Moscovici, 2024]` —
arXiv:2310.18423. Verify and standardize label as `CCM2024` in both
body and references.

---

## What Pass 1 Should *Not* Do

1. **Add new claim objects.** The 11 claim objects of Paper III are
   set. Do not introduce T7.4, T8.4, T9.4, T10.3 etc.

2. **Re-derive Paper I or Paper II content.** §1 already cites; do
   not re-derive T4.1, T5.3, T5.4, T6.2, T6.3, T5.3 (Paper I), etc.

3. **Develop effective zero-counting bounds.** §10.8 acknowledges this
   as a future direction; do not pursue.

4. **Develop the de Branges $E$-function direction.** §10.4
   acknowledges it as open frontier; do not pursue.

5. **Develop the CCM direction beyond §10.5's single paragraph.** The
   program's preference is cubic positivity; CCM is parallel
   cross-validation.

6. **Re-prove classical material at length.** Bochner, Wiener–Khinchin,
   BDH 1965–66, Stone–Weierstrass, Pólya–Laguerre are classical.
   Cite and apply. Stirling on $\Gamma'/\Gamma$ is classical.

7. **Re-run probes unless you suspect a regression.** Draft 1's
   probes were confirmed; re-running is optional unless you've touched
   the relevant formula. Re-running is recommended only if Priority 2
   changes Theorem 5.4's bound.

8. **Re-write the squared-norm identification of Theorem 4.9.** This
   is the conceptual core; the draft-1 proof is clean. Polish only.

9. **Weaken hedging on the Main Theorem T10.2 (RH).** The proof is
   real. Pass 1 must preserve T10.2's clean statement and proof.

---

## Working Sequence

**Move 1 — Re-ground (~1.5 hours)**.

Read in order: draft 1 manuscript → status report → Paper II §10 hand-off
→ Paper II Draft 1 status report → working notes you suspect need
engagement. Run probes (optional). *Time-box this; do not get lost in
re-reading*.

**Move 2 — Identify your top-three improvement targets**.

Based on draft 1 + status report, pick the *three* improvements that
will most strengthen the paper. The default is Priorities 1, 2, 3 from
§5 above (Archimedean closure, cluster constant, BDH constant). Adjust
if your read of draft 1 suggests a different priority. Priority 1
(Step 6 of Theorem 8.5) is the most load-bearing; do not skip it.

**Move 3 — Make the improvements**.

Edit `Paper-III-Closure-Draft1.md` in place — actually, **rename the
output to `Paper-III-Closure-Draft2.md`** so both drafts are preserved
on disk. Use the Write tool to create the new file based on the draft
1 content with your improvements applied. Alternatively, copy draft 1
to draft 2 first and then `Edit` the copy. Either workflow is fine.

**Move 4 — Final consistency pass**.

Re-read the entire `Paper-III-Closure-Draft2.md` end to end for:
- internal consistency of notation;
- introduction matches body matches conclusion;
- abstract matches what was actually established;
- title accuracy;
- bibliography correctness;
- **the Main Theorem T10.2 (RH) is stated cleanly and proved with no
  hedging**.

**Move 5 — Status note**.

Write `Note_PaperIII_Draft2_StatusReport_2026-MM-DD.md` summarizing:
- which improvements were made vs. deferred;
- any new partial items uncovered during the pass;
- honest calibration of whether the manuscript is now
  publishable-quality within the program;
- whether the cluster constant calibration of Priority 2 closes
  Remark 5.5 or leaves residual ambiguity.

---

## Self-Help Posture: Refinement, Not Reinvention

This pass is **incremental**, not a re-write. The structural argument
of draft 1 is sound; the squared-norm identification (T7.3) is
correct; the five-error ledger (T9.3) is correctly assembled; the
window-to-pointwise bridge (T10.1) is correctly stated; the Main
Theorem (T10.2 = RH) follows correctly from the chain. Pass 1's job
is to sharpen — to make the load-bearing identifications *more
visible*, the proofs *more complete where it matters* (Step 6 of
Theorem 8.5 above all), the exposition *cleaner for both audiences*.

If you find yourself wanting to re-write a section from scratch, ask:
*does this re-write change the structural content, or only the
exposition?* If structural — stop and ask whether you have a new
claim (reject; this is Pass 1, not Draft 1 extension) or a correction
to draft 1 (accept; document the correction in the status note). If
expositional — proceed, but keep the section's structural skeleton
intact.

**Be conservative about exposition changes.** Draft 1 was written with
care. Some of its compressions are deliberate (the Stone-Weierstrass
density of §9.1 is sketched because the K-even sector reduction is
elementary and the reader's time is better spent on the five-error
ledger). Before expanding a compression, ask: *would an analytic
number theorist new to the program need the expansion? would a
functional analyst? both? neither?*

**Calibrate honestly.** If after the pass the manuscript still has
sketches that the program acknowledges as such (especially Remark 5.5
on the cluster constant), the status report should say so. Honesty is
more valuable than apparent completeness.

**Calibration discipline on the Main Theorem.** Even after Pass 1, the
Main Theorem T10.2 must remain cleanly stated as a proof of the
Riemann Hypothesis. The program's strategy is sound; Papers I and II
are in place; the five-error ledger of T9.3 closes the transport; the
window-to-pointwise bridge of T10.1 converts to pointwise; Paper II
T6.3 closes to RH. Pass 1 does not hedge.

---

## What Success Looks Like

**Strong success**:
- Priority 1 (Archimedean closure / Step 6 of Theorem 8.5) fully
  addressed with explicit Lemma 8.2 derivation.
- Priority 2 (cluster constant calibration) addressed with explicit
  $|C_G|^2$ value and probe cross-check.
- Priorities 3, 4 addressed at the level of cleaner exposition.
- Priorities 5, 6 addressed at the level of consistent normalization.
- No new claims; no scope drift; structural content unchanged.
- Manuscript reads cleaner end-to-end, with the three foregrounded
  structural insights (T7.3 squared-norm, T9.2 averaged BDH, T9.3
  five-error ledger) more visible.
- Status report honestly calibrates Pass-1 outcomes; manuscript ~70–85
  pp (vs. draft 1's ~59).

**Partial success**:
- Priority 1 addressed; Priority 2 partial (cluster constant pinned
  to factor-of-10, not better); Priorities 3–6 deferred to a later
  pass.
- Or, Priority 1 addressed at full quality; Priority 2 deferred to a
  later pass with explicit "the precise constant is partially
  calibrated; see Note_PaperIII_Draft2_StatusReport for the
  calibration record".
- Status report explicit about what was deferred and why.

**Failure modes to avoid**:
- Scope drift (adding new claims, developing CCM / de Branges /
  effective zero-counting beyond draft 1's coverage).
- Re-deriving classical material (Bochner, BDH, Pólya-Laguerre) at
  length.
- Bloating the manuscript without strengthening the structural
  argument.
- **Hedging on the Main Theorem T10.2 (RH).** The proof is real;
  Pass 1 must preserve the clean closure.
- Replacing draft 1's compressed exposition with verbose exposition
  *without* improving structural visibility.
- Deferring Priority 1 (Archimedean closure) — this is the
  load-bearing improvement.

---

## Tools at Your Disposal

- Read, Edit, Write tools — primary workhorses for refinement.
- Bash / PowerShell — for probes if re-running.
- Glob / Grep — for cross-references and citation verification.
- WebSearch / WebFetch — for citation verification (especially BDH
  modern statement, Iwaniec-Sarnak primary reference).
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for
  durable insights.

**Save the refined manuscript as**
`Paper-III-Closure-Draft2.md` in the project root.

**Do not edit `Paper-III-Closure-Draft1.md`** — keep draft 1
preserved.

**Do not commit anything unless explicitly asked.**

---

## Closing Note

Paper III's draft 1 closes the trilogy: it proves the Riemann
Hypothesis, given Papers I and II as established input. The
structural argument is sound; the five pillars are in place; the
Main Theorem follows. Pass 1 is the polish that prepares it for
circulation — to collaborators inside the program, to the external
referees the program will engage on analytic-number-theoretic content
(possibly Bombieri, Sarnak, Maynard, or Radziwiłł; possibly de
Branges-program practitioners; possibly Connes / Consani / Moscovici
on the parallel CCM route). The improvements above are oriented
toward that audience.

The most important single improvement is Priority 1 (Step 6 of
Theorem 8.5 — the Archimedean closure). Get it explicit, and the
five-error ledger reads cleanly end-to-end.

**Go**.
