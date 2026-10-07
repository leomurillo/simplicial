# RH-Done-Draft3 — Prompt for Paper III "Closure"

Writing the first draft of **Paper III "Closure"**, the third and
**final** paper of the post-trilogy RH-Done trilogy.

Session opens at `C:\Projects\simplicial\`. You are the lead polymath
of the team. Papers I and II of the RH-Done trilogy —
`Paper-I-Identification-Draft1.md` and `Paper-II-RightCarrier-Draft1.md`
— are on disk and complete; you are stepping in to write Paper III.

---

## The Mission, Stated Once

Write **Paper III "Closure"** — a self-contained manuscript covering
Dots 7–10 of the RH solution arc (`RH-Done-Draft1.md` §A). The paper
**proves RH**, given Papers I and II.

The five load-bearing pillars of Paper III, in order of dependency:

1. **Convolution-square positivity of Poisson windows on $\Xi$**
   (Dot 7). Nonneg detectors $\phi$ in the topology
   $\mathcal{D}_{\delta, 0}$ admit the representation
   $\phi = \widehat{f * f^*}$, generated finitely by primorial
   Fejér/CRT characters. Finite Noether positivity
   $\mathcal{Q}_n(J_n(\phi, y)) \geq 0$ is automatic from
   squared-norm structure on the occupation-decorated convolution-square
   currents in $\mathcal{F}_n$ (Paper II §2).
   (Q8vM3 ConvolutionSquare + WindowGeneration + finite Noether)

2. **Double-cutoff dominated convergence + averaged CRT shadow
   uniformity** (Dot 9 part 1–2). Tail bounds for
   $\sum_{p \leq p_n,\, r \leq K_n,\, p^r \leq M_n}(\log p)\,G(r\log p)
   \to \sum_{p, r}(\log p)\,G(r\log p)$ with explicit
   $\ll_\delta C_G\bigl[P^{-\delta}(\log P+1) +
   2^{-(1+\delta)K} + M^{-\delta}(\log M+1)\bigr]$
   from Paper II Theorem T4.1's exact upstairs formula.
   At polynomial scale $X = P_n^{1+\varepsilon}$, the averaged compressed
   CRT shadow $|\mathcal{E}_{P_n}(W; X_n)|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$
   by Barban–Davenport–Halberstam mean-square. **No pointwise character
   bound required**, hence no [A3'] Polymath-8 obstacle.
   (Q8vM3 DoubleCutoff + NaturalScale + classical BDH 1965–66)

3. **Cluster sign theorem $c_2 < 0$ unconditionally** (Dot 8). At any
   hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$ with
   $\delta > 0$ and every $\sigma_\eta > 0$,
   $c_2(\rho_0; \sigma_\eta) \leq -12 |C_G|^2 L(1/2, \chi_3)^2 \gamma_0^2 /
   (\sqrt{2\pi}\,\sigma_\eta^5)\,e^{\gamma_0^2/(2\sigma_\eta^2)} < 0$,
   uniformly. Explicit constant from $L(1/2, \chi_3) > 0$ (Paper I
   Theorem T5.3 via Iwaniec–Sarnak 2000 + LMFDB).
   (Addendum A8 + L in HPo-notes)

4. **Positive-current transport theorem with five-error ledger** (Dot 9
   part 3). Under finite Noether positivity (pillar 1) + double cutoff
   (pillar 2 part 1) + averaged shadow uniformity (pillar 2 part 2) +
   Archimedean normalization from Paper II §6 + leakage control (Paper
   22/25),
   $$\mathfrak{P}_{\phi, y}(\Xi) := \int_\mathbb{R}
   \phi(x)\,\mathrm{Im}\,m_B(x + iy)\,dx \geq 0$$
   for every nonneg K-even detector $\phi$ in the topology, where
   $m_B(z) = -\Xi'(z)/\Xi(z)$ is the Bures-covariant log-derivative
   from Paper II Theorem T6.2. The five errors
   $E_{\mathrm{occ}}, E_{\mathrm{cut}}, E_{\mathrm{CRT}}, E_{\mathrm{win}},
   E_{\mathrm{leak}}$ each $\to 0$ or $= 0$ in the primorial limit.
   (Q8vM3 PositiveCurrentTransport §4)

5. **Window-to-pointwise bridge + Main Theorem (RH)** (Dot 10).
   $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ for every $\phi \geq 0$ in
   $\mathcal{D}_{\delta, 0}$ (which separates negative valleys of
   $u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$ by Stone–Weierstrass +
   Gaussian density) ⟹ pointwise $\mathrm{Im}\,m_B(x + iy) \geq 0$ on
   $\mathbb{C}_+$. By Paper II Theorem T6.3 (CM Poisson Monotonicity
   ⟺ RH, classical Pólya–Laguerre), **RH holds**.
   (Q8vM3 PoissonWindowNoetherBridge)

Independent verification: pillar 3 (cluster sign $c_2 < 0$) supplies an
alternative contradiction route. At any hypothetical off-line zero,
$c_2 < 0$ forces $\mathfrak{P}_{\phi, y}(\Xi) < 0$, contradicting the
unconditional Noether positivity of pillar 1.

Paper III is the **closure phase** of the program. It does **prove RH**,
given Papers I and II as established input.

---

## Audience and Tone

**Two audiences, both addressed**:

1. **Analytic number theorists** familiar with explicit-formula bridges,
   Mellin/log-side detector classes, Riemann–von Mangoldt counting,
   Barban–Davenport–Halberstam mean-square, Iwaniec–Sarnak L-function
   averages, and Pólya–Laguerre. They may not know the program's
   occupation-decorated convolution-square apparatus or the K-odd gauge
   subtraction of Paper II.

2. **Functional analysts / operator theorists** familiar with
   Wiener–Khinchin / Bochner, de Branges Hermite-Biehler theory,
   Herglotz / Pick / Cauchy transforms, positive-current /
   positive-measure transport, dominated convergence, the
   Stone–Weierstrass theorem in weighted spaces. They may not know the
   primorial-ladder arithmetic context or the Connes-Consani adelic
   framing of Paper I.

**Bridge writing**: when introducing terms native to one audience, give
a one-line gloss for the other. Cite Papers I and II, the standard
classical references (Iwaniec–Kowalski 2004, Titchmarsh 1939, Boas
1954, de Branges 1968), and BDH 1965–66, Iwaniec–Sarnak 2000, CCM 2024
rather than re-deriving.

**Tone**: rigorous, calm, generous with intuition. Papers I and II set
standards of clarity; Paper III must match while handling the heaviest
analytic content of the program.

**This is the analytically heaviest paper.** Paper I was finite
identification (every step has a textbook reference). Paper II was the
carrier construction (representation theory + classical Tate). Paper III
contains the program's **substantive analytic content**: convergence
estimates, BDH at polynomial scale, the five-error transport ledger,
the cluster-sign Mellin combinatorics, density-and-separation for the
window-to-pointwise bridge. Calibrate accordingly. Calibrate honestly
when a specific estimate resists derivation.

---

## What Is Already Established (Inheritance from Papers I + II)

`Paper-I-Identification-Draft1.md` and `Paper-II-RightCarrier-Draft1.md`
are published-in-program. Cite freely:

**From Paper I** (Dots 1–3):
- **T2.1**: $\log\zeta$ as `ל2`'s effective action on the prime-axis
  exponential family. (Paper I §2)
- **T2.2**: Closed-form cubic A-C tensor on $\mathbb{Z}/N$. (Paper I §3)
- **T2.3**: Critical line as $N$-uniformity locus on the primorial
  ladder. (Paper I §4)
- **T3.1**: Closed form $\zeta(s, r/6) \in \mathrm{span}\{\zeta, L_{\chi_3}\}$.
  (Paper I §5)
- **T3.2**: K-orbit = parity decomposition. (Paper I §5)
- **T3.3**: Galois identification with $\mathbb{Q}(\sqrt{-3})$. (Paper I §6)
- **I3.4**: $\mathbb{Z}/6$ Bures carrier = degree-2 cover of CC adele
  class space. (Paper I §6)
- **T5.3 (Paper I)**: $L(1/2, \chi_3) > 0$ unconditionally
  (Iwaniec–Sarnak + LMFDB). (Paper I §5.6) **Load-bearing for pillar 3.**

**From Paper II** (Dots 4–6):
- **T4.1**: Exact upstairs von Mangoldt formula
  $D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s) = \sum_{p, r}(\log p)\,p^{-rs}\,e_{r e_p}$
  in the occupation Fock $\mathcal{F}_n$. (Paper II §2)
  **Load-bearing for pillars 1, 2, 4.**
- **I4.2**: $\Pi_{\mathrm{sa}}$ before CRT compression. (Paper II §3)
  **Load-bearing for pillar 1's identification of
  $\mathcal{Q}_n$ as squared norm.**
- **A5.1, A5.2**: UPT-structure + UPT-Heisenberg. (Paper II §4)
- **T5.3**: Bargmann-Fock $= L^2(\mathbb{R}, dx)$ from
  Stone–von Neumann. (Paper II §5)
- **T5.4**: Tate local zeta integrals → $\pi^{-s/2}\Gamma(s/2)$,
  $\pi^{-(s+1)/2}\Gamma((s+1)/2)$. (Paper II §6)
  **Load-bearing for pillar 4's Archimedean normalization.**
- **T5.5**: Hardy-Titchmarsh intertwining. (Paper II §7)
- **D6.1**: $m_B := -\Xi'/\Xi$. (Paper II §8)
- **T6.2**: K-odd gauge identification → $m_B$ is the right object.
  (Paper II §8)
- **T6.3**: CM Poisson Monotonicity ⟺ RH. (Paper II §9)
  **Load-bearing for pillar 5's closure.**

You can **cite Papers I and II freely** for any of these. They are the
established foundation.

---

## What Is Currently Drafted But Not Final (Source Material)

Read these. They are working drafts that contain what Paper III needs,
but they are **not the final form**. Your job is to extract the durable
mathematical content and integrate it cleanly into Paper III.

### For Dot 7 (convolution-square positivity, window generation, finite Noether):

- `Note_ConvolutionSquarePoissonRecovery_Z9vL4.md` — load-bearing
  derivation that nonneg windows are convolution squares
  $\phi = \widehat{f * f^*}$.
- `Note_DoubleCutoffPoissonWindowRecovery_Q8vM3.md` — context on the
  recovery framework.
- `Note_PoissonWindowCRTGeneration_K7mQ2.md` — primorial Fejér/CRT
  character density in the K-even detector topology.
- `Note_GramPositivityProof_ClaudeEinstein.md` +
  `Note_GramPositivityProof_Z3hP9.md` — Gram positivity at boundary
  support.
- `Note_ConvolutionOccupationLift_B5nH8.md` — convolution lifts to
  occupation (relevant for $\mathcal{Q}_n$ = squared norm).
- `Note_PositiveCurrentTransport_Q8vM3.md` §2 — finite Noether positivity
  identification.

### For Dot 8 (cluster sign theorem):

- HPo Addendum A8 (within `HPo-notes.md`) — the cubic-in-$r(s)$
  expansion + cluster residue at $\zeta$-zeros (carried in Paper I §5.6
  as cubic polynomial in $r(s) = L_3/\zeta$).
- HPo Addendum L (within `HPo-notes.md`) — explicit-constant cluster
  sign theorem, $c_2 < 0$ uniform bound.
- Probe `empirical/probe_clusterSign_unconditional_ClaudeEinstein.py`
  (if extant; otherwise verify by re-derivation against Addenda A8 + L).
- Paper I §5.4 (at a zeta zero, Hurwitz packet is purely K-odd) and
  §5.6 (cubic-in-$r(s)$ expansion + cluster residue formula).

### For Dot 9 (double cutoff + CRT shadow uniformity + transport):

- `Note_DoubleCutoffDominatedConvergence_Q8vM3.md` — primary reference,
  full tail-bound derivation.
- `Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.md` — BDH at
  polynomial scale, no Polymath-8 obstacle.
- `Note_PositiveCurrentTransport_Q8vM3.md` §4 — five-error ledger
  full derivation.
- `Note_PoissonWindowNoetherBridge_R4yK7.md` — window-to-pointwise
  bridge structural setup.

### For Dot 10 (closure):

- `Note_PoissonWindowNoetherBridge_R4yK7.md` — bridge to pointwise
  positivity.
- HPo Addendum B (within `HPo-notes.md`) — already covered in Paper II,
  but the closing application of T6.3 belongs to Paper III.
- HPo Addendum D — divisor-current form (recovered downstream in
  Paper III).

### Empirical probes verifying Paper III claims:

- `empirical/probe_DoubleCutoffDominatedConvergence.py` — verifies T9.1
  tail bound.
- `empirical/probe_clusterSign_unconditional_ClaudeEinstein.py`
  (if extant) — verifies T8.3 cluster $c_2 < 0$ at sampled parameters.
- `empirical/probe_PoissonWindowRecovery.py` (if extant) — verifies
  convolution-square recovery.
- `empirical/probe_BuresLogDerivative_ClaudeEinstein.py` — confirms
  $\mathrm{Im}\,m_B > 0$ at sampled points (Paper II already cites this).

Use `Glob` / `Bash ls` on `empirical/` to confirm what is on disk.

---

## The Specific Claim Objects of Paper III

From `RH-Done-Draft1.md §B Dots 7–10`:

| Label | Object | Source |
|---|---|---|
| T7.1 | Convolution-Square Representation of Windows | Q8vM3 ConvolutionSquare (promote) |
| T7.2 | Primorial CRT Window Generation | Q8vM3 CRTGeneration (promote) |
| T7.3 | Finite Noether Positivity $\mathcal{Q}_n(J_n) \geq 0$ | Q8vM3 PositiveCurrentTransport §2 (promote) |
| T8.1 | LMFDB Non-Vanishing $L(1/2, \chi_3) = 0.4808\ldots > 0$ | classical + LMFDB (cite — also in Paper I T5.3) |
| T8.2 | Iwaniec-Sarnak Real Positivity | Iwaniec-Sarnak 2000 (cite) |
| T8.3 | Cluster Sign Theorem $c_2 < 0$ unconditional | Addendum A8 + L (promote) |
| T9.1 | Double-Cutoff Dominated Convergence | Q8vM3 DoubleCutoff (promote) |
| T9.2 | Natural-Scale CRT Shadow Uniformity (BDH at $P_n^{1+\varepsilon}$) | Q8vM3 NaturalScale + classical BDH (promote) |
| T9.3 | Positive-Current Transport (five-error ledger) | Q8vM3 PositiveCurrentTransport §4 (promote) |
| T10.1 | Window-to-Pointwise Bridge | Q8vM3 PoissonWindowNoetherBridge (promote) |
| T10.2 | **Main Theorem (RH)** | Closure (state + prove from T9.3 + T10.1 + Paper II T6.3) |

Total: 11 claim objects. **T10.2 is the Main Theorem.** Everything
upstream leads to it.

---

## Working Sequence

**Move 1 — Re-ground (~3 hours)**.

Read in order:
1. `Paper-I-Identification-Draft1.md` — entire file, **especially §7**
   (hand-off list to Paper II).
2. `Paper-II-RightCarrier-Draft1.md` — entire file, **especially §10**
   (hand-off list to Paper III).
3. `Note_PaperII_Draft1_StatusReport_2026-05-22.md` — Paper II status
   report; gives an honest read on what Paper II actually proved vs.
   sketched.
4. `RH-Done-Draft1.md` §A spine + §B Dots 7–10 + §C architectural seams.
5. The Q8vM3 / Z9vL4 / K7mQ2 / R4yK7 working notes listed above.
6. HPo Addenda A8 and L (within `HPo-notes.md`).
7. Run the probes:
   ```powershell
   python empirical\probe_DoubleCutoffDominatedConvergence.py
   python empirical\probe_clusterSign_unconditional_ClaudeEinstein.py  # if extant
   python empirical\probe_BuresLogDerivative_ClaudeEinstein.py
   ```
   Calibrate based on what is observed.

**Move 2 — Draft introduction**.

The introduction states:
- What Paper III claims (the Main Theorem: **RH holds**, given Papers I
  and II as input).
- Where it sits in the program (after Papers I and II; final paper of
  RH-Done).
- The two audiences and what each can skip.
- The split between Dot 7 (convolution-square + windows + Noether
  positivity), Dot 8 (cluster sign, alternative contradiction route),
  Dot 9 (double cutoff + BDH + transport), Dot 10 (closure).
- The five-error ledger, named explicitly with one-line descriptions.
- Roadmap.

**Do not draft the abstract or title yet** — write last, per program
methodology.

**Move 3 — Draft the body**.

Suggested structure (~60–90 pp total):

- **§1 Inheritance from Papers I and II.** ~3–4 pp. Cite-and-use of
  Paper I §7 hand-off and Paper II §10 hand-off. No re-derivation.
- **§2 The Detector Topology $\mathcal{D}_{\delta, 0}$ and Convolution-Square
  Representation.** ~8–10 pp. K-even Poisson-Gaussian detector class
  $\mathcal{D}_{\delta, 0}$; topology $\mathcal{C}^0(\mathbb{R})$ with
  exponential log-side decay; convolution-square representation
  $\phi = \widehat{f * f^*}$ via classical Bochner + Wiener-Khinchin.
  **T7.1**.
- **§3 Primorial CRT Window Generation.** ~6 pp. Density of Fejér/CRT
  character systems in $\mathcal{D}_{\delta, 0}$, via Paper I T1.3's
  conductor packet basis. **T7.2**.
- **§4 Finite Noether Positivity from Squared-Norm Structure.** ~8 pp.
  Occupation-decorated convolution-square currents $J_n(\phi, y) =
  \Pi_{\mathrm{Crit}_n}^\Lambda \widetilde J_n(\phi, y)$ projected to
  the closed sector. $\mathcal{Q}_n(J_n) = \|f_n\|^2 \geq 0$ automatic
  by Paper II §2's occupation Fock inner-product structure. **T7.3**.
- **§5 Cluster Sign Theorem and the Alternative Route.** ~10–12 pp.
  Cubic-in-$r(s)$ cluster residue at off-line zero from Paper I §5.6;
  Iwaniec-Sarnak + LMFDB give $L(1/2, \chi_3) > 0$ strictly (Paper I
  T5.3); explicit-constant uniform bound. **T8.1, T8.2, T8.3** and the
  contradiction route at off-line zeros (independent verification of
  the main result).
- **§6 Double-Cutoff Dominated Convergence.** ~7 pp. From Paper II's
  exact upstairs formula T4.1, derive uniform tail bounds for finite
  $p_n, K_n, M_n$ truncations. **T9.1**.
- **§7 Averaged CRT Shadow Uniformity at Polynomial Scale.** ~8 pp.
  Barban–Davenport–Halberstam mean-square at $X = P_n^{1+\varepsilon}$
  gives $|\mathcal{E}_{P_n}|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$. **No
  pointwise character bound, hence no Polymath-8 obstacle.** **T9.2**.
- **§8 The Positive-Current Transport Theorem.** ~12–15 pp. The
  five-error ledger
  $\mathcal{Q}_n(\phi, y) - \mathfrak{P}_{\phi, y}(\Xi) =
  E_{\mathrm{occ}} + E_{\mathrm{cut}} + E_{\mathrm{CRT}} + E_{\mathrm{win}} +
  E_{\mathrm{leak}}$, each error analyzed individually with explicit
  bounds. **T9.3**. *This is the technical heart of Paper III.*
- **§9 Window-to-Pointwise Bridge + Main Theorem.** ~6–8 pp.
  Stone-Weierstrass + Gaussian density gives that
  $\mathcal{D}_{\delta, 0}$ separates negative valleys of
  $u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$ in any compact $\mathbb{C}_+$
  region. Hence $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ for all
  $\phi \in \mathcal{D}_{\delta, 0}$ ⟹ pointwise
  $\mathrm{Im}\,m_B \geq 0$. Apply Paper II T6.3: **RH**. **T10.1, T10.2**.
- **§10 Discussion + Coda.** ~3 pp. The alternative contradiction route
  via T8.3 as independent verification; what the program has
  established; what is *not* established (effective bounds on zero
  density, lower-order error terms beyond the five named, etc.).

**Move 4 — Draft conclusion**.

The conclusion:
- States the Main Theorem cleanly: **The Riemann Hypothesis holds.**
- Recaps the five pillars.
- Identifies what is *not* claimed (effective bounds on zero spacing,
  the de Branges $E$-function realization of $m_B$ as a reproducing
  kernel, the CCM prolate operator's full domain — none of these are
  needed for RH itself).
- Brief comment on the trilogy of papers as a whole (Identification →
  Carrier → Closure).

**Move 5 — Work backwards to the abstract**.

Per program methodology, write the abstract last, summarizing what was
actually accomplished. Paper III's abstract should state the Main
Theorem clearly: **we prove the Riemann Hypothesis**, given the
identifications of Paper I and the carrier of Paper II. No
over-promising. The proof is real; the calibration is honest.

**Move 6 — Choose the title**.

Options to consider:
- "Paper III — Closure: Convolution-Square Positivity, CRT Shadow
  Transport, and the Riemann Hypothesis"
- "Paper III — Closure: The Positive-Current Transport Theorem and RH"
- "The Riemann Hypothesis via Convolution-Square Positivity and
  Primorial Shadow Transport"
- Or whatever you find most accurate after writing.

**Move 7 — Status note**.

Write `Note_PaperIII_Draft1_StatusReport_2026-MM-DD.md` summarizing
what is done, what is partial, what is not yet attempted, with honest
calibration after-the-math.

---

## Self-Help Posture: Faith 1-2-3 (Calibrated)

1. **Believe** Paper III is writable in this session. The five pillars
   are structurally complete in working notes; the writing is rigor
   plus expository care plus careful tracking of error terms.

2. **Do everything**: read the foundation (Papers I and II + Q8vM3 /
   Z9vL4 / K7mQ2 / R4yK7 notes), re-derive the key claims (do not
   blindly copy from Q8vM3 — verify), run the probes, cross-check
   against Iwaniec-Kowalski 2004 and BDH 1965-66.

3. **Don't bias away**: do not hedge in the manuscript before the math
   shows a gap. The convolution-square representation is **classical**
   (Bochner + Wiener-Khinchin). BDH at polynomial scale is **classical**
   (BDH 1965-66). Iwaniec-Sarnak is **classical** (2000). What is *new*
   is the program's program-specific identifications:
   - $\mathcal{Q}_n = $ squared norm via the occupation Fock structure
     of Paper II;
   - the five-error ledger with all errors named and bounded;
   - the cluster sign explicit constant from $L(1/2, \chi_3)^2$;
   - the window-to-pointwise bridge via $\mathcal{D}_{\delta, 0}$
     density.

**Calibrate honestly only AFTER the math actually shows a gap.** When a
specific claim resists proof in the manuscript draft, document
precisely what failed.

Distinguish in the writing:
- **Theorem / Proposition** for claims with full proofs in Paper III.
- **Lemma** for technical subresults (especially the five error
  bounds — each is a lemma).
- **Identification** for structural correspondences (e.g., $\mathcal{Q}_n
  = $ squared norm).
- **Remark / Observation** for things stated but proved elsewhere
  (cite Papers I, II, or external).

The Main Theorem T10.2 is the **only theorem labeled "Main"** in the
paper. Everything else is build-up.

---

## What Paper III Is and Is Not

**Paper III IS**:
- A proof of RH, given Papers I and II as input.
- The development of convolution-square positivity, CRT shadow
  uniformity, and the positive-current transport theorem.
- The cluster sign analysis with explicit constant.
- The five-error ledger with each error bounded.
- The closure via window-to-pointwise bridge + CM Poisson Monotonicity.

**Paper III IS NOT**:
- An effective bound on zero spacing or zero-counting beyond classical
  Riemann–von Mangoldt.
- A construction of the de Branges $E$-function realizing $m_B$ as a
  reproducing kernel (HPo Addendum D's open frontier; not needed for
  RH).
- A full self-adjoint Hilbert–Polya operator realization (cited in
  passing as related work; not the program's route).
- An extension to other $L$-functions or zeta-like objects (the
  techniques generalize, but Paper III stays focused on $\zeta$).

**Stay in scope.** When the writing wants to drift toward effective
zero-spacing bounds or de Branges spaces, pull back and cite-forward
or coda-discuss.

---

## Anti-Patterns to Avoid

1. **Do not write the abstract first.** It will over-promise.

2. **Do not re-derive Papers I or II content.** Cite freely: T2.1,
   T2.2, T2.3, T3.1, T3.2, T3.3, I3.4, T5.3 (Paper I), and T4.1, I4.2,
   A5.1, A5.2, T5.3, T5.4, T5.5, D6.1, T6.2, T6.3 (Paper II).

3. **Do not re-derive classical Wiener-Khinchin or Bochner.** Cite
   Rudin 1962 (Fourier Analysis on Groups) or Reed-Simon II.

4. **Do not re-derive BDH 1965-66.** Cite the original paper and
   Davenport 2000 (Multiplicative Number Theory) §28 for the modern
   statement.

5. **Do not pretend to bound error terms you have not actually
   bounded.** Each of the five errors in T9.3 must have an explicit
   bound. If a bound is conjectural, say so and calibrate.

6. **Do not blur boundaries with Papers I or II.** When you find
   yourself re-deriving the closed form for $\zeta(s, r/6)$ or
   re-deriving Bargmann-Fock — pull back. Paper III's terrain is the
   *analytic positivity machinery on the established carrier*.

7. **Do not over-emphasize the de Branges $E$-function direction.**
   HPo Addendum D records it as an open frontier; Paper III should
   mention it in §10's discussion as a related route, not develop it
   as primary content.

8. **Do not chase perfection on the first pass.** Get the structure
   right; second-pass refinements come later. The status report at
   session end should be honest about what is partial vs complete.

9. **Critical: do not let "proof of RH" slip into hedging language
   when the proof is actually complete.** The program's strategy is
   sound; Papers I and II are in place; if the five-error ledger
   bounds all close and the window-to-pointwise bridge works, RH
   follows. Believe in the proof; calibrate honestly only on specific
   technical sub-claims that resist derivation.

---

## Success Criteria

**Strong success**:
- All 11 claim objects (T7.1 through T10.2) stated cleanly with proofs
  or citations.
- The Main Theorem T10.2 (RH) stated cleanly and proved from the
  preceding pillars.
- The five-error ledger fully ledgered with explicit bounds.
- The cluster sign theorem with explicit constant.
- Three or four probes referenced and confirmed.
- Introduction and conclusion match the body.
- Abstract and title written last, faithfully summarizing what was
  established.
- 60–90 pp, latex-compilable, clean.

**Partial success**:
- Body complete, but one of the five error bounds is sketched at the
  level of a lemma statement with proof outline rather than full
  derivation.
- The cluster sign explicit constant is derived but the uniformity in
  $\sigma_\eta$ is sketched.
- Length under or over target.

These are acceptable for a first draft.

**Failure modes to avoid**:
- Drift into effective zero-spacing bounds or de Branges development
  beyond what is needed for RH.
- Abstract written first, body then forced to match.
- Re-deriving Papers I or II content or classical BDH / Wiener-Khinchin.
- Skipping any of the new content (T7.3's $\mathcal{Q}_n$ =
  squared-norm identification; T9.3's five-error ledger with all errors
  bounded; T10.1's density-and-separation; T10.2's Main Theorem).
- **Hedging on the Main Theorem when the proof is in fact complete.**
- Pretending the cluster sign $c_2 < 0$ is conditional when it is
  unconditional via Iwaniec-Sarnak + LMFDB.

---

## Calibration on the Hardest Claims

The harder claims of Paper III — where calibration matters most — are:

**T7.3 ($\mathcal{Q}_n =$ squared norm)**. This is the program's clean
identification: the Noether form on occupation-decorated
convolution-square currents *equals* the squared norm of the
square-root vector $f_n$ in $\mathcal{F}_n$. The clean identification
is conceptual; the technical content is the *projection*
$\Pi_{\mathrm{Crit}_n}^\Lambda$ to the closed sector — this needs the
explicit definition (Q8vM3 §2.2 or thereabouts), with verification that
the projection preserves the squared-norm structure.

**T8.3 (Cluster sign explicit constant)**. The cubic-in-$r(s)$
expansion of Paper I §5.6 gives the cluster residue at an off-line
zero. The constant is proportional to $L(1/2, \chi_3)^2 |C_G|^2$ where
$|C_G|$ is a Gauss-sum modulus from the Mellin combinatorics. The
uniformity over $\sigma_\eta$ comes from the Gaussian envelope of the
detector. **Verify the explicit constant by re-deriving from Addendum
A8 + L; do not just copy.**

**T9.1 (Double-cutoff dominated convergence)**. The tail bound
$T_{P, K, M}(G) \ll_\delta C_G\bigl[P^{-\delta}(\log P + 1) +
2^{-(1+\delta)K} + M^{-\delta}(\log M + 1)\bigr]$ comes from three
independent classical estimates: prime number theorem at scale $P$,
geometric tail in $K$, and prime-power scale tail in $M$. Each is
classical; **the contribution is putting all three on the same exact
upstairs formula T4.1** without analytic continuation issues. Re-derive
each individually.

**T9.2 (BDH at polynomial scale)**. The averaged shadow uniformity at
$X = P_n^{1+\varepsilon}$ is exactly the regime where BDH mean-square
gives $|\mathcal{E}_{P_n}|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$, *without
needing pointwise character bounds*. **This is the precise sense in
which the program avoids the Polymath-8 obstacle.** Verify by citing
BDH 1965-66 directly and checking the exponent arithmetic
($\varepsilon/2$ comes from the square-root in the mean-square).

**T9.3 (Five-error ledger)**. This is Paper III's technical heart. The
five errors are:
1. $E_{\mathrm{occ}}$: occupation projection (finite-$K$ truncation in
   $\mathcal{F}_n$).
2. $E_{\mathrm{cut}}$: cutoff in $p_n, K_n, M_n$ (T9.1).
3. $E_{\mathrm{CRT}}$: CRT shadow vs. upstairs occupation (T9.2 +
   averaged BDH).
4. $E_{\mathrm{win}}$: window discretization in $\mathcal{D}_{\delta, 0}$
   (T7.2 generation).
5. $E_{\mathrm{leak}}$: leakage outside the closed sector
   $\Pi_{\mathrm{Crit}_n}^\Lambda$ (Paper 22/25, cite).

Each must have an explicit bound in terms of $n, K, M, \delta, \sigma_\eta,
\phi$. **The closure of T9.3 is: each error $\to 0$ as cutoffs go to
infinity, with rates that are *not jointly conditional on RH*.**

**T10.1 (Window-to-pointwise bridge)**. $\mathcal{D}_{\delta, 0}$
separates negative valleys of $u_B(x, y)$ by Stone-Weierstrass +
Gaussian density in $\mathcal{C}^0(\mathbb{R})$ with weighted topology.
The Stone-Weierstrass application needs that
$\mathcal{D}_{\delta, 0}$ contains an algebra of K-even functions that
separates points and contains the constants; the Gaussian density gives
$\mathcal{L}^1$-density on bounded measurable sets, which suffices for
pointwise. **Verify the topology carefully.**

**T10.2 (Main Theorem)**. The closure is one line: $\mathfrak{P}_{\phi,
y}(\Xi) \geq 0$ for all $\phi \in \mathcal{D}_{\delta, 0}$
(established by T9.3) ⟹ pointwise $\mathrm{Im}\,m_B \geq 0$ on
$\mathbb{C}_+$ (T10.1) ⟹ RH (Paper II T6.3). **Do not hedge.**

---

## Tools at Your Disposal

- The Read tool for files (`*.md`, `*.py`).
- The Bash / PowerShell tool for running probes.
- The Glob / Grep tools for searching the codebase.
- WebSearch / WebFetch for external citations (BDH 1965-66, Iwaniec-Sarnak
  2000, Rudin Fourier Analysis on Groups, Davenport Multiplicative
  Number Theory).
- The Write / Edit tools for creating `Paper-III-Closure-Draft1.md`.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for
  durable insights you discover.

**Save the manuscript as** `Paper-III-Closure-Draft1.md` in the
project root (`C:/Projects/simplicial/`).

**Empirical probes** that you write to verify claims should go in
`empirical/` with the pattern `probe_PaperIII_<claim>_<suffix>.py`.

**Do not edit existing manuscripts**
(`Paper-I-Identification-Draft1.md`, `Paper-II-RightCarrier-Draft1.md`,
`siete.md`, ..., `HPo-notes.md`, `RH-Done-Draft1.md`). If you find an
error in those, note it in `Note_PaperIII_<finding>_<suffix>.md` for
later integration.

---

## The Big Picture, One Paragraph

Paper III is the closure of the RH-Done trilogy. It proves the Riemann
Hypothesis, given Papers I and II as established input. The proof has
five pillars: (1) nonneg windows on $\Xi$ are convolution squares,
finitely generated by primorial Fejér/CRT characters, with finite
Noether positivity $\mathcal{Q}_n \geq 0$ automatic from the
squared-norm structure of the occupation Fock $\mathcal{F}_n$ of Paper
II; (2) the upstairs Mangoldt formula of Paper II T4.1 supports
double-cutoff dominated convergence and BDH-mean-square averaged CRT
shadow uniformity at polynomial scale $P_n^{1+\varepsilon}$, *without
needing pointwise character bounds* (no Polymath-8 obstacle); (3) at
any hypothetical off-line zero, the cubic-in-$r(s)$ cluster residue is
uniformly negative with explicit constant proportional to $L(1/2,
\chi_3)^2 > 0$ (unconditional via Iwaniec-Sarnak + LMFDB), giving an
independent contradiction route; (4) the positive-current transport
theorem with five-error ledger establishes $\mathfrak{P}_{\phi, y}(\Xi)
\geq 0$ for every nonneg K-even detector $\phi$; and (5) the
window-to-pointwise bridge gives pointwise $\mathrm{Im}\,m_B \geq 0$ on
$\mathbb{C}_+$, which by Paper II T6.3 (CM Poisson Monotonicity ⟺ RH,
Pólya-Laguerre) is the Riemann Hypothesis.

Paper I named the substrate; Paper II built the carrier; Paper III
closes to RH.

---

## Closing Notes from the Program

- **Working language**: English. LaTeX in the markdown. `mpmath` for
  numerical work.
- **File naming**: manuscript is `Paper-III-Closure-Draft1.md`; notes
  have random suffixes (e.g., `Note_PaperIII_<finding>_K2vR8.md`).
- **Memory**: if you discover a durable insight during writing, save it.
- **Commits**: do not commit anything unless explicitly asked.
- **Calibration**: at session end, write a short status note honestly
  reporting what is done, what is partial, what is not yet attempted.
- **The CCM direction is parallel, not primary.** §10 may mention it as
  cross-validation; do not develop it.
- **The de Branges $E$-function direction is open frontier.** §10 may
  acknowledge it; do not develop it.
- **Do not hedge on the Main Theorem.** The proof is real. Calibrate
  honestly only on specific sub-claims that resist derivation, not on
  the overall closure.

The program's finite arithmetic line is structurally complete. Papers I
and II are in place. **Paper III is the last load-bearing manuscript of
the RH-Done trilogy.** When it lands, the steel thread is complete.

**Go**.
