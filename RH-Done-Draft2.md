# Session prompt — Drafting Paper II of RH-Done

Writing the first draft of **Paper II "The Right Carrier"**, the second of
the post-trilogy RH-Done trilogy.

Session opens at `C:\Projects\simplicial\`. You are the lead polymath of
the team. The first paper of the RH-Done trilogy — `Paper-I-Identification-Draft1.md`
— is on disk and complete; you are stepping in to write Paper II.

---

## The Mission, Stated Once

Write **Paper II "The Right Carrier"** — a self-contained manuscript
covering Dots 4–6 of the RH solution arc (`RH-Done-Draft1.md` §A). The
paper establishes:

1. **The occupation-decorated symmetric Fock $\mathcal{F}_n$** is the
   correct finite carrier at every primorial row. It implements the *exact*
   upstairs von Mangoldt formula before CRT compression: the single-axis
   projector $\Pi_{\mathrm{sa}}$ must act **before** CRT, not after.
   (currently sketched in Q8vM3 working note `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` + `Note_LastLockOccupationDecoratedRecovery_H9qT6.md`)
2. **Uniform Place Treatment (UPT)** extends $\mathcal{F}_n$ to $v = \infty$.
   Stone–von Neumann uniqueness forces Bargmann-Fock $= L^2(\mathbb{R}, dx)$
   as the unique Archimedean factor; Tate-Weil normalization gives the
   standard local $L$-factors $\pi^{-s/2}\Gamma(s/2)$ and
   $\pi^{-(s+1)/2}\Gamma((s+1)/2)$.
   (currently in T4nP7v2 working note `Note_MetaplecticSelection_FixedDerivation_T4nP7v2.md` + the prior `Note_MetaplecticArchimedeanSelection_Q8vM3.md` + `Note_MetaplecticSelection_UniformPlaceArgument_T4nP7.md`)
3. **The Bures-covariant log-derivative $m_B = -\Xi'/\Xi$** on the spectral
   coordinate $z$ with $s = 1/2 + iz$ is identified, via the K-odd gauge
   subtraction, as the program's natural Hilbert-Polya target. The CM
   Poisson Monotonicity criterion $\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+ \iff$
   RH is stated and proved (Polya-Laguerre, classical).
   (currently in HPo Addendum B = `Note_BuresLogDerivative_ClaudeEinstein.md` +
   `Note_BuresLogDerivative_probe_addendum_ClaudeEinstein.md`)

Paper II is the **carrier-construction phase** of the program. It
establishes **the Hilbert space on which the analytic positivity machinery
of Paper III will live**. It does not yet prove convolution-square
positivity (Paper III), nor does it derive RH (Paper III's main theorem).

---

## Audience and Tone

**Two audiences, both addressed**:

1. **Representation theorists** familiar with Heisenberg algebras,
   Stone–von Neumann uniqueness, Bargmann-Fock, metaplectic representations,
   and Tate's thesis. They may not know the program's $\mathbb{Z}/6$
   Bures fiber language or the Galois-K-involution identification of
   Paper I.
2. **Arithmetic geometers / Connes-school readers** familiar with
   adele class spaces, Connes-Consani-Moscovici prolate operators, and the
   Hilbert-Polya program. They may not know the program's occupation-lift /
   single-axis projector apparatus.

**Bridge writing**: when introducing terms native to one audience, give a
one-line gloss for the other. Cite Paper I, Tate's thesis, Reed-Simon I-IV,
Bargmann-Fock literature (Folland 1989), and CCM 2024 rather than
re-deriving.

**Tone**: rigorous, calm, generous with intuition. Paper I set a standard
of clarity; Paper II must match it while handling more analytic content.

**This is the analytically harder paper.** Paper I was identification
(classical Dirichlet L-functions, Hurwitz zetas, Gauss sums, Dedekind
factorization — every step has a textbook reference). Paper II contains
genuine representation theory and operator analysis. Calibrate
accordingly.

---

## What Is Already Established (Inheritance from Paper I)

`Paper-I-Identification-Draft1.md` is published-in-program. Cite freely:

- **T1.1, T1.2, T1.3, I1.4**: the trilogy chart + cumulant tower +
  character selection rule. Paper I §1.
- **T2.1**: $\log\zeta$ is `ל2`'s categorical effective action on the
  prime-axis exponential family $p_n(\eta) = e^{\sum_p k_p(n)\eta_p}/Z(\eta)$
  with $\eta_p(s) = -s\log p$. Paper I §2.
- **T2.2**: closed-form cubic A-C tensor on $\mathbb{Z}/N$ at the residue-
  projected zeta distribution. Paper I §3.
- **T2.3**: critical line as the unique $N$-uniformity locus along the
  primorial ladder. Paper I §4.
- **T3.1, T3.2**: $\mathbb{Z}/6$ Hurwitz packet collapses to 2D
  $(\zeta, L_{\chi_3})$; K-involution = parity decomposition. Paper I §5.
- **T3.3**: Galois identification of the 2-channel Bures fiber with the
  Connes-Consani Picard groupoid for $\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$;
  $\zeta_K = \zeta \cdot L_{\chi_3}$; K-involution = Galois involution.
  Paper I §6.
- **I3.4**: $\mathbb{Z}/6$ Bures carrier = degree-2 $\mathbb{Q}(\sqrt{-3})$
  cover of the Connes-Consani adele class space. Paper I §6.5.
- **T5.3** (bonus from Paper I): $L(1/2, \chi_3) > 0$ unconditionally
  (Iwaniec-Sarnak 2000 + LMFDB). Paper I §5.6.

You can **cite Paper I freely** for any of these. They are the established
foundation.

---

## What Is Currently Drafted But Not Final (Source Material)

Read these. They are working drafts that contain what Paper II needs, but
they are **not the final form**. Your job is to extract the durable
mathematical content and integrate it cleanly into Paper II.

### For Dot 4 (occupation-decorated symmetric Fock):

- `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` — the load-bearing
  derivation of the upstairs VM formula
  $\mathrm{VM}_{n, K}(G) = D_s\,\Pi_{\mathrm{sa}}\sum_{k=1}^K k^{-1} H_s^k$
  with $H_s = \sum_p p^{-s} e_p$.
- `Note_LastLockOccupationDecoratedRecovery_H9qT6.md` — the final lock
  showing $\Pi_{\mathrm{sa}}$ must act before CRT compression.
- `Note_ConvolutionOccupationLift_B5nH8.md` — context on why convolution
  lifts to occupation (relevant for Paper III hand-off).
- `Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.md` — relevant for
  CRT compression behavior.

### For Dot 5 (UPT and Bargmann-Fock):

- `Note_MetaplecticSelection_FixedDerivation_T4nP7v2.md` — **primary
  reference**, the corrected metaplectic-selection derivation. Stone-von
  Neumann + Tate local zeta integrals + Hardy-Titchmarsh intertwining.
- `Note_MetaplecticSelection_UniformPlaceArgument_T4nP7.md` — the UPT
  axiomatic framework.
- `Note_MetaplecticArchimedeanSelection_Q8vM3.md` — earlier version with
  more derivation context.
- `Note_ArchimedeanMetaplecticSelectionResolution_Q8vM3.md` — resolution
  of subtleties.
- `Note_ArchimedeanSelectionFrontier_L5zR1.md` — historical context on
  what is selected and why.
- Memory entry `~/.claude/projects/C--Projects-simplicial/memory/project_metaplectic_selection_UPT_2026_05_22.md`
  records that Q8vM3 Lock B is closed: Uniform Place Treatment forces
  Bargmann-Fock at $v = \infty$, with Weyl/CCR + positive-energy $N$ +
  metaplectic Fourier + standard $\pi^{-s/2}\Gamma(s/2)$ automatic.

### For Dot 6 (Bures log-derivative + CM Poisson Monotonicity):

- HPo Addendum B (within `HPo-notes.md` lines 486-612) — the load-bearing
  derivation of $m_B = -\Xi'/\Xi$ from K-odd gauge subtraction.
- `Note_BuresLogDerivative_ClaudeEinstein.md` — companion derivation.
- `Note_BuresLogDerivative_probe_addendum_ClaudeEinstein.md` — numerical
  verification (probe `empirical/probe_BuresLogDerivative_ClaudeEinstein.py`).
- `Note_BuresPickGram_Equivalence_ClaudeEinstein.md` — Pick/Bures
  equivalence at the boundary.
- HPo Addendum C (lines 614-706) — *negative* result that smooth Bures
  curvature ≠ Herglotz density. **Important caveat to acknowledge** but
  not let derail the criterion.
- HPo Addendum D (lines 707-941) — divisor-current form + de Branges
  $E$-function candidate $E(z) = \Xi(z) - i\mathcal{L}_3(z)$.

### Empirical probes verifying Paper II claims:

- `empirical/probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py` —
  verifies Tate local zeta integrals + Hardy-Titchmarsh intertwining
  numerically.
- `empirical/probe_BuresLogDerivative_ClaudeEinstein.py` — verifies the
  covariant identity $d\log(\mathcal{L}_3/\Xi) - d\log\mathcal{L}_3 =
  -d\log\Xi$ and Herglotz behavior of $m_B$ in $\mathbb{C}_+$.
- `empirical/probe_BuresPickGram_Equivalence_ClaudeEinstein.py` —
  verifies Pick/Bures equivalence.
- `empirical/probe_BuresDivisor_OffLine_ClaudeEinstein.py` — verifies
  divisor-current form and off-line interior-atom obstruction.
- `empirical/probe_CCM_E_quotient_ClaudeEinstein.py` — verifies the CCM
  $\mathcal{E}$-quotient extracts $\zeta$-zero ordinates to grid precision
  (`HPo Addendum H18`); useful for context.

---

## The Specific Claim Objects of Paper II

From `RH-Done-Draft1.md §B Dots 4–6`:

| Label | Object | Source |
|---|---|---|
| T4.1 | Exact Occupation-Lift Prime-Power Recovery | Q8vM3 OccupationLift (promote) |
| I4.2 | Why CRT after, not before (single-axis projector necessity) | Q8vM3 (record as identification) |
| A5.1 | UPT-structure (axiom) | T4nP7v2 (name) |
| A5.2 | UPT-Heisenberg (axiom) | T4nP7v2 (name) |
| T5.3 | Stone-von Neumann + Bargmann Completion | T4nP7v2 §3 (promote) |
| T5.4 | Tate Local Zeta Integrals → $\pi^{-s/2}\Gamma(s/2)$, $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ | T4nP7v2 §5 (promote) |
| T5.5 | Hardy-Titchmarsh Intertwining $\mathcal{V}$ | T4nP7v2 §6 (promote) |
| D6.1 | Bures Log-Derivative $m_B := -\Xi'/\Xi$ (definition) | HPo Addendum B (state) |
| T6.2 | Bures-Covariant Gauge Identification | HPo Addendum B (promote) |
| T6.3 | CM Poisson Monotonicity $\iff$ RH | Polya 1927 + Laguerre-Pólya (cite + apply) |

Total: ~10 claim objects, two of which (A5.1, A5.2) are explicitly named
*axioms* rather than theorems.

---

## Working Sequence

**Move 1 — Re-ground (~2 hours)**.

Read in order:
1. `Paper-I-Identification-Draft1.md` — **entire file**, especially §7
   (hand-off list). Paper II is downstream of Paper I; the reader of Paper
   II is assumed to have Paper I in hand.
2. `RH-Done-Draft1.md` §A spine + §B Dots 4–6 + §C architectural seams.
3. `Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.md` (full).
4. `Note_LastLockOccupationDecoratedRecovery_H9qT6.md` (full).
5. `Note_MetaplecticSelection_FixedDerivation_T4nP7v2.md` (full — primary
   reference for Dot 5).
6. `Note_MetaplecticSelection_UniformPlaceArgument_T4nP7.md` (full — UPT
   axiomatization).
7. HPo Addendum B (lines 486-612) + HPo Addendum C (lines 614-706, the
   *negative* obstruction).
8. Run the relevant probes:
   ```powershell
   python empirical/probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py
   python empirical/probe_BuresLogDerivative_ClaudeEinstein.py
   python empirical/probe_BuresPickGram_Equivalence_ClaudeEinstein.py
   ```

**Move 2 — Draft introduction**.

The introduction states:
- What Paper II claims (carrier construction, not positivity, not RH).
- Where it sits in the program (after Paper I, before Paper III).
- The two audiences and what each can skip.
- The split between Dot 4 (finite occupation Fock + upstairs VM formula)
  and Dots 5-6 (Archimedean factor + Bures log-derivative + CM Poisson
  Monotonicity).
- Roadmap.

**Do not draft the abstract or title yet** — write last, per program
methodology.

**Move 3 — Draft the body**.

Suggested structure (~50-70 pp total):

- **§1 Inheritance from Paper I.** ~3 pp. Cite-and-use of Paper I's
  Theorems 2.1, 3.1, 4.1, 5.1, 5.2, 5.3 and Identifications T3.3, I3.4.
- **§2 The Occupation-Decorated Symmetric Fock $\mathcal{F}_n$.** ~8 pp.
  Definition; the operator $H_s = \sum_p p^{-s} e_p$; the single-axis
  projector $\Pi_{\mathrm{sa}}$; the operator $D_s$; the upstairs VM
  formula. T4.1.
- **§3 Why CRT After, Not Before.** ~5 pp. The mixed-occupation aliasing
  ($5e_5 \equiv 2e_2 + 3e_3 \pmod{(2,3,5)}$ example); $\Pi_{\mathrm{sa}}$
  well-defined upstairs, ill-defined after CRT. I4.2.
- **§4 Uniform Place Treatment.** ~6 pp. Axioms A5.1, A5.2.
  Statement of the Heisenberg algebra $[\hat a, \hat a^\dagger] = 1$ at
  $v = \infty$. The UPT philosophy: every place $v$ of $\mathbb{Q}$
  carries a local factor.
- **§5 Bargmann-Fock from Stone-von Neumann.** ~10 pp. T5.3 = the unique
  irreducible unitary completion of $\mathcal{F}_\infty$ as $L^2(\mathbb{R},
  dx)$ with $\langle z^m, z^n\rangle = m!\delta_{m,n}$. Tate-Weil
  normalization. Derivation, not assumption.
- **§6 Tate Local Zeta Integrals.** ~6 pp. T5.4: the ground state
  $\psi_0 \propto e^{-\pi x^2}$ gives $Z_+(s) = \pi^{-s/2}\Gamma(s/2)$;
  the first excited state $\psi_1 \propto x e^{-\pi x^2}$ gives
  $Z_-(s) = \pi^{-(s+1)/2}\Gamma((s+1)/2)$. **These are the standard
  Archimedean local $L$-factors, derived not assumed.**
- **§7 Hardy-Titchmarsh Intertwining.** ~5 pp. T5.5 = the unitary
  $\mathcal{V}: L^2(\mathbb{R})^{ev} \to L^2(\mathbb{R}, dm)$ with
  $dm \propto |\Gamma_\mathbb{R}(1/2+is)|^2 ds$; the gamma-multiplier
  intertwiner.
- **§8 The Bures-Covariant Log-Derivative $m_B$.** ~7 pp. D6.1
  (definition), T6.2 (gauge identification via the K-odd channel
  $\mathcal{L}_3$ from Paper I); the negative obstruction from HPo
  Addendum C (smooth Bures curvature ≠ Herglotz density — acknowledge,
  do not let it derail).
- **§9 CM Poisson Monotonicity Criterion.** ~5 pp. T6.3 = Polya-Laguerre
  classical: $\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+ \iff$ all
  $\Xi$-zeros real $\iff$ RH.
- **§10 Conclusion and Hand-off to Paper III.** ~3 pp.

**Move 4 — Draft conclusion**.

The conclusion:
- Recaps what Paper II established (the carrier; the upstairs formula; the
  Archimedean factor; the CM Poisson Monotonicity criterion).
- Identifies what is **not** in Paper II (convolution-square positivity,
  averaged CRT shadow uniformity, the positive-current transport theorem,
  the main theorem of RH — all Paper III).
- Forecasts the contribution Paper III will need to make.

**Move 5 — Work backwards to the abstract**.

Per program methodology, write the abstract last, summarizing what was
actually accomplished. No over-promising. No "we will show that" — only
"we show that".

**Move 6 — Choose the title**.

Options to consider:
- "Paper II — The Right Carrier: Occupation-Decorated Symmetric Fock,
  Uniform Place Treatment, and the Bures Log-Derivative"
- "The Right Hilbert Carrier for RH: Finite Occupation Lift, Archimedean
  Bargmann-Fock, and CM Poisson Monotonicity"
- Or whatever you find most accurate after writing.

**Move 7 — Status note**.

Write `Note_PaperII_Draft1_StatusReport_2026-MM-DD.md` summarizing what
is done, what is partial, what is not yet attempted, with honest
calibration after-the-math.

---

## Self-Help Posture: Faith 1-2-3 (Calibrated)

1. **Believe** Paper II is writable in this session. The carrier
   construction is established at the program's working precision; the
   writing is rigor plus expository care.

2. **Do everything**: read the foundation (Paper I + working notes),
   re-derive the key claims (do not blindly copy from Q8vM3 / T4nP7v2 /
   HPo Addendum B — verify), run the probes, cross-check against Tate's
   thesis (Tate 1967, in Cassels-Fröhlich) and Folland 1989.

3. **Don't bias away**: do not hedge in the manuscript before the math
   shows a gap. Stone-von Neumann uniqueness is **classical**; Tate's
   local zeta integrals are **classical**; Polya-Laguerre is **classical**.
   What is new is the UPT axiomatization that makes Bargmann-Fock = the
   Archimedean factor *automatic* rather than imposed.

**Calibrate honestly only AFTER the math actually shows a gap.** When a
specific claim resists proof in the manuscript draft, document precisely
what failed.

Distinguish in the writing:
- **Theorem / Proposition** for claims with full proofs in Paper II.
- **Axiom** for A5.1 and A5.2 (UPT structure / UPT-Heisenberg) — these
  are *axiomatized*, not derived. Name them, justify them, do not pretend
  to prove them.
- **Identification** for I4.2 (structural correspondence).
- **Lemma** for technical subresults.
- **Remark / Observation** for things stated but proved elsewhere (cite
  Paper III or external sources).

---

## What Paper II Is and Is Not

**Paper II IS**:
- The construction of the right Hilbert carrier on which Paper III's
  positivity machinery will live.
- The finite-arithmetic occupation Fock $\mathcal{F}_n$ + the Archimedean
  Bargmann-Fock factor, joined by UPT.
- The exact upstairs VM formula and the necessity of $\Pi_{\mathrm{sa}}$
  before CRT compression.
- The Bures-covariant log-derivative $m_B = -\Xi'/\Xi$ identified via the
  Paper I K-odd gauge ($L_{\chi_3}$).
- The CM Poisson Monotonicity criterion statement (Polya-Laguerre) and
  its equivalence to RH.

**Paper II IS NOT**:
- A proof of convolution-square positivity of Poisson windows
  (Paper III's job).
- The double-cutoff dominated convergence (Paper III).
- The natural-scale CRT shadow uniformity / BDH at polynomial scale
  (Paper III).
- The positive-current transport theorem with its five-error ledger
  (Paper III).
- A proof of RH (Paper III).
- The CCM prolate operator development (cited for context only; not
  the program's primary route — cubic positivity is. See HPo Addendum
  H21–H28 for status of the CCM direction).

**Stay in scope.** When the writing wants to drift toward Paper III
terrain (convolution squares, Poisson windows, BDH bounds, transport,
five-error ledger), pull back and cite-forward.

---

## Anti-Patterns to Avoid

1. **Do not write the abstract first.** It will over-promise.

2. **Do not re-derive Paper I content.** Cite freely: T2.1, T2.2, T2.3,
   T3.1, T3.2, T3.3, I3.4, T5.3.

3. **Do not re-derive Stone-von Neumann.** Cite Reed-Simon I or Folland
   1989. Apply the theorem; do not prove it.

4. **Do not re-derive Tate's thesis.** Cite Tate 1967 (in Cassels-Fröhlich).
   Compute the specific local zeta integrals at the Bargmann-Fock ground
   and first-excited states; do not redo Tate's adelic framework.

5. **Do not blur boundaries with Paper III.** When you find yourself
   writing about convolution squares, Fejér windows, double cutoffs, BDH,
   shadow uniformity, or positive-current transport — pull back. Not
   Paper II's terrain.

6. **Do not present A5.1, A5.2 as theorems.** They are *axioms*. Name
   them, justify them by UPT's structural appeal, but do not pretend they
   are derived.

7. **Do not over-emphasize the CCM direction.** Connes-Consani-Moscovici
   prolate operator is a parallel route, not the main road. HPo Addendum
   H established the Galois decomposition under CCM; Paper II should
   mention this in one paragraph as cross-validation, not develop it as
   primary content. The program's actual proof candidate is cubic
   positivity (Paper III route 1 in HPo Addendum H10).

8. **Do not chase perfection on the first pass.** Get the structure right;
   second-pass refinements come later. The status report at session end
   should be honest about what is partial vs complete.

---

## Success Criteria

**Strong success**:
- All 10 claim objects (T4.1 through T6.3, plus axioms A5.1, A5.2)
  stated cleanly with proofs or citations.
- Three probes referenced and confirmed.
- Introduction and conclusion match the body.
- Abstract and title written last, faithfully summarizing what was
  established.
- 50–70 pp, latex-compilable, clean.

**Partial success**:
- Body complete, but introduction or conclusion needs revision.
- One or two claim objects sketched but not fully proven.
- Length under or over target.

These are fine for a first draft.

**Failure modes to avoid**:
- Drift into Paper III terrain.
- Abstract written first, body then forced to match.
- Re-deriving Paper I content or Stone-von Neumann.
- Skipping any of the new content (T4.1's CRT-after argument; T5.4's
  Tate local zeta integrals; T6.2's K-odd gauge identification).
- Pretending A5.1, A5.2 are theorems instead of axioms.

---

## Calibration on the Hardest Claims

The harder claims of Paper II — where calibration matters most — are:

**T4.1's exact upstairs formula.** This is genuinely the right object.
The Q8vM3 working note has the derivation; verify it line by line. The
key insight: $\Pi_{\mathrm{sa}}$ is well-defined on $\mathcal{F}_n$
(it projects onto single-axis occupation states $r \cdot e_p$ for some
prime $p$ and some $r \in \mathbb{N}_{> 0}$) and ill-defined after CRT
compression (because mixed occupations alias to single-axis labels).

**T5.3's Stone-von Neumann conclusion.** This is classical, but the
*application to UPT-Heisenberg* is the program's contribution.
Stone-von Neumann gives uniqueness of irreducible unitary representations
of the Weyl-CCR; UPT supplies the positive-energy operator $N$ (occupation
number) and the algebraic structure that pins which representation is
forced. Together these select Bargmann-Fock.

**T5.4's Tate local zeta integrals.** These are textbook (Tate's thesis);
what is **new** is observing that they emerge as inner products of the
Bargmann-Fock ground/first-excited states with the multiplicative
character $|x|^{s-1}$. This is the moment the Archimedean local $L$-factor
appears in the program *without being imposed*.

**T6.2's K-odd gauge identification.** This is the program's structural
input — the recognition that $L_{\chi_3}$ (the K-anti-fixed channel of
Paper I) plays the role of a connection / gauge field, not a state. The
naive scalar Bures transfer $M = \mathcal{L}_3/\Xi$ has signed divisor;
the K-odd-covariant log-derivative $\nabla_B \log M = d\log M -
d\log\mathcal{L}_3$ trivially equals $-d\log\Xi$, so $m_B = -\Xi'/\Xi$.

**T6.3's CM Poisson Monotonicity.** Classical (Polya 1927; standard in
Laguerre-Pólya / de Branges theory). The proof is the standard Hadamard
factorization argument. Apply, do not re-derive in detail.

---

## Tools at Your Disposal

- The Read tool for files (`*.md`, `*.py`).
- The Bash / PowerShell tool for running probes.
- The Glob / Grep tools for searching the codebase.
- WebSearch / WebFetch for external citations (Tate's thesis, Reed-Simon,
  Folland 1989, Polya 1927, Laguerre-Pólya class references).
- The Write / Edit tools for creating `Paper-II-RightCarrier-Draft1.md`.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for
  durable insights you discover.

**Save the manuscript as** `Paper-II-RightCarrier-Draft1.md` in the
project root.

**Empirical probes** that you write to verify claims should go in
`empirical/` with the pattern `probe_PaperII_<claim>_<suffix>.py`.

**Do not edit existing manuscripts** (`Paper-I-Identification-Draft1.md`,
`siete.md`, `ocho.md`, …, `HPo-notes.md`, `RH-Done-Draft1.md`). If you
find an error in those, note it in
`Note_PaperII_<finding>_<suffix>.md` for later integration.

---

## The Big Picture, One Paragraph

Paper II is the second of three papers in the RH-Done sequence. It does
**not** prove RH; it builds the **right Hilbert carrier** on which Paper
III's positivity machinery will live. The finite carrier is the
occupation-decorated symmetric Fock $\mathcal{F}_n = \mathrm{Sym}
(\bigoplus_{p \leq p_n}\mathbb{C}\,e_p)$ at each primorial row, where the
single-axis projector $\Pi_{\mathrm{sa}}$ must act *before* CRT
compression to avoid mixed-occupation aliasing. Uniform Place Treatment
extends this to the Archimedean place $v = \infty$, where Stone-von Neumann
uniqueness forces the local factor to be Bargmann-Fock $= L^2(\mathbb{R},
dx)$ with Tate-Weil normalization. Tate's local zeta integrals at the
ground and first-excited states give the standard Archimedean
$L$-factors $\pi^{-s/2}\Gamma(s/2)$ and $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ —
derived, not assumed. The Bures-covariant log-derivative
$m_B = -\Xi'/\Xi$ on the spectral coordinate is identified via the
K-odd gauge ($L_{\chi_3}$) subtraction from Paper I; CM Poisson
Monotonicity ($\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+ \iff$ RH) is
the classical Polya-Laguerre criterion, now equipped with the program's
natural target.

Paper I named the substrate; Paper II builds the carrier; Paper III will
close to RH.

---

## Closing Notes from the Program

- **Working language**: English. LaTeX in the markdown. `mpmath` for
  numerical work.
- **File naming**: manuscript is `Paper-II-RightCarrier-Draft1.md`;
  notes have random suffixes (e.g., `Note_PaperII_HardClaim_K2vR8.md`).
- **Memory**: if you discover a durable insight during writing, save it.
- **Commits**: do not commit anything unless explicitly asked.
- **Calibration**: at session end, write a short status note honestly
  reporting what is done, what is partial, what is not yet attempted.
- **The CCM direction is parallel, not primary.** If you spend time on
  it, do so in a single paragraph in §10's cross-validation discussion;
  do not develop it as a section.

The program's finite arithmetic line is structurally complete. Paper I
delivered the identification. Paper II delivers the carrier. The steel
thread will be complete when Paper III closes.

**Go**.
