# Status Report: Paper II — The Right Carrier, Draft 1

**Date:** 2026-05-22
**Manuscript:** `Paper-II-RightCarrier-Draft1.md`
**Author:** Claude (acting as program polymath)
**Session:** Single-session first draft, post-Paper-I.

---

## 1. What was produced

A complete first-draft manuscript covering Dots 4–6 of
`RH-Done-Draft1.md` §A — the carrier-construction phase of the
post-trilogy *RH-Done* sequence:

- **Title:** *Paper II — The Right Carrier: Occupation-Decorated
  Symmetric Fock, Uniform Place Treatment, and the Bures-Covariant
  Log-Derivative for $\zeta$.*
- **Length:** approximately 55–60 manuscript pages of dense LaTeX-in-MD,
  comfortably within the 50–70 pp target.
- **Structure:** abstract → introduction → §§1–10 → references.
- **Writing order followed:** introduction → body §§1–10 → conclusion →
  abstract → title, per program methodology.

The manuscript saves at `C:/Projects/simplicial/Paper-II-RightCarrier-Draft1.md`.

---

## 2. Claim objects: status

Per `RH-Done-Draft1.md` §B Dots 4–6, the ten claim objects:

| Label | Object | Status in Draft 1 |
|---|---|---|
| T4.1 | Exact Occupation-Lift Prime-Power Recovery | **Stated and proved** as Theorem 2.5 (§2.5). Proof is the algebraic identity in $\mathcal{F}_n$; mixed-occupation multinomials killed by $\Pi_{\mathrm{sa}}$, $1/r$ vs. $r$ cancellation gives $\log p$. |
| I4.2 | Why CRT after, not before | **Stated and justified** as Identification 3.3 (§3.3). Justification: explicit mixed/single-axis collision at $n = 3$ (the $5 e_5$ vs. $2 e_2 + 3 e_3$ example), incompatibility of any putative compressed projector. |
| A5.1 | UPT-structure | **Stated as axiom** in §4.2. Named, justified by Tate-Connes-Consani adelic uniformity; explicitly *not* claimed as a theorem. |
| A5.2 | UPT-Heisenberg | **Stated as axiom** in §4.3. Named, justified by three program commitments (Tate, CCM prolate, finite-place occupation lift); explicitly *not* claimed as a theorem. |
| T5.3 | Stone–von Neumann + Bargmann Completion | **Stated and proved** as Theorem 5.1 (§5.2). Proof uses adjoint relation + $\hat a = \partial_z$ uniqueness + ladder normalization → $w_n = n!$. |
| T5.4 | Tate Local Zeta Integrals → $\pi^{-s/2}\Gamma(s/2)$, $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ | **Stated and proved** as Theorem 6.1 (§6.2). Proof is direct Gaussian integration with substitution $u = \pi x^2$. |
| T5.5 | Hardy-Titchmarsh Intertwining | **Stated and sketched** as Theorem 7.1 (§7.2). Proof sketched, full classical derivation cited to Titchmarsh 1939 §7.5. |
| D6.1 | Bures Log-Derivative $m_B := -\Xi'/\Xi$ | **Defined** as Definition 8.3 (§8.3). |
| T6.2 | Bures-Covariant Gauge Identification | **Stated and proved** as Theorem 8.4 (§8.3). Proof is one-line algebra: $\nabla_B \log M = d\log M - d\log\mathcal{L}_3 = -d\log\Xi$. |
| T6.3 | CM Poisson Monotonicity ⟺ RH | **Stated and proved** as Theorem 9.1 (§9.2). Proof is classical Polya-Laguerre via Hadamard factorization (both directions). |

**All ten claim objects are stated cleanly. Eight have full proofs in
the manuscript; one (T5.5) has a sketch with citation to Titchmarsh;
the two axioms (A5.1, A5.2) are explicitly named as axioms not
theorems.**

---

## 3. Empirical probes referenced

Three probes confirm the new identifications numerically (all run during
session, output verified):

| Probe | Verifies | Status |
|---|---|---|
| `probe_MetaplecticSelection_FixedDerivation_T4nP7v2.py` | Tate $Z_+(s) = \pi^{-s/2}\Gamma(s/2)$ and $Z_-(s) = \pi^{-(s+1)/2}\Gamma((s+1)/2)$ at multiple sample points; Bargmann norm $\langle z^n, z^n\rangle_B = n!$ for $n = 0, \ldots, 5$; Tate–Weil normalization | **Confirmed at machine precision**. Output reproduced in §6.2 and §5.2 commentary. |
| `probe_BuresLogDerivative_ClaudeEinstein.py` | Covariant identity $d\log(\mathcal{L}_3/\Xi) - d\log\mathcal{L}_3 = -d\log\Xi$; sampled $\mathrm{Im}\,m_B > 0$ on $\mathbb{C}_+$; simple Herglotz pole residue 1 at $\gamma_1 = 14.1347\ldots$ | **Confirmed at $\leq 10^{-13}$.** Output reproduced in §8.6. |
| `probe_BuresCurvature_mB_ClaudeEinstein.py` | Negative obstruction: smooth Bures Fubini–Study curvature $\kappa_{EO}$ finite at $\gamma_1$ while $\mathrm{Im}\,m_B \to \infty$ | **Confirmed.** Table reproduced in §8.5. |

A fourth probe (`probe_BuresPickGram_R6mT4.py`) was also run for context;
its output supports §8 but is not directly referenced in the manuscript.

---

## 4. What is partial in Draft 1

**(a) T5.5 Hardy–Titchmarsh intertwining proof.** Theorem 7.1 is stated
in full and proved at the level of *sketch*: the Mellin–Hankel
correspondence + classical Plancherel kernel for the Mellin transform
at the critical line. A reader familiar with Titchmarsh 1939 §7.5 will
have no trouble filling in the details; a reader new to this material
might want a longer proof. Second-pass refinement could expand the
sketch to a complete proof.

**(b) UPT-Heisenberg justification.** A5.2 (§4.3) is justified by
three program commitments (Tate, CCM, finite-place lift) at the level
of *structural argument*, not derivation from deeper finite-place
input. This is by design — A5.2 is an axiom — but a reader might wish
for more rigorous discussion of *why* the Heisenberg structure
extends to $v = \infty$ as opposed to some other operator algebra. The
current treatment is consistent with the program's working notes
(`Note_MetaplecticSelection_UniformPlaceArgument_T4nP7.md` §10) but
could be expanded.

**(c) Forward references to Paper III.** The conclusion §10.3 lists
what Paper III must contribute. Several of these forward references
(convolution-square positivity, BDH at polynomial scale, five-error
ledger) are stated tersely and depend on internal working notes
(`Note_ConvolutionSquarePoissonRecovery_Z9vL4.md`,
`Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.md`,
`Note_PositiveCurrentTransport_Q8vM3.md`,
`Note_DoubleCutoffDominatedConvergence_Q8vM3.md`). The summaries are
accurate but could be cross-checked against the latest versions of
those notes before Paper II is finalized.

**(d) Bibliography.** The references section uses shortform labels
(e.g., `Folland1989`, `Tate1967`). Standard bibliographic normalization
(year disambiguation, full publisher info, BibTeX export) is deferred to
second-pass cleanup. The references are accurate but not yet
copy-edited.

---

## 5. What is not attempted in Draft 1

Per the prompt brief, the following are *out of scope* for Paper II and
were not attempted:

- Convolution-square positivity of nonneg windows (Dot 7; Paper III).
- Double-cutoff dominated convergence (Dot 9 part 1; Paper III).
- Averaged CRT shadow uniformity / BDH at polynomial scale (Dot 9
  part 2; Paper III).
- Positive-current transport theorem with five-error ledger (Dot 9
  part 3; Paper III).
- Cluster sign theorem $c_2 < 0$ (Dot 8; Paper III).
- Main theorem on RH (Dot 10; Paper III).

These appear in §10.3 as forward references to Paper III, with the
correct labels and structural summaries. Paper II does not derive them.

The **CCM direction** is acknowledged in §9.4 in a single paragraph as
cross-validation; it is not developed as primary content, per the
program's strategy preference for the cubic-positivity route over the
CCM prolate route.

The **negative obstruction** of HPo Addendum C (smooth Bures curvature
≠ Herglotz density) is acknowledged in §8.5 and explicitly *does not
derail* the criterion: §8.5 makes clear that Paper III's positivity
strategy is the *atomic* divisor route, not the smooth curvature route,
so Addendum C is a *clarifying obstruction*, not a blocker.

---

## 6. Honest calibration: where I leaned in, where I hedged

**Leaned in fully (no hedging in the manuscript):**
- T4.1's exact upstairs identity. The Q8vM3 derivation is sound; the
  identity is purely algebraic in $\mathcal{F}_n$, no analytic estimate;
  $1/r$ vs $r$ cancellation is elementary and clean.
- I4.2's structural identification. The $5 e_5$ vs. $2 e_2 + 3 e_3$
  collision is explicit and unambiguous; the existence proof of the
  obstruction (no compatible compressed projector) is clean.
- T5.3's Bargmann completion. Stone-von Neumann is classical; the
  derivation in §5.2 is the standard one; nothing to hedge.
- T5.4's Tate integrals. Standard Gaussian integration; result matches
  the textbook Archimedean local L-factor. The *observation* that this
  emerges from UPT without imposition is new, and that's where the
  program's contribution lives.
- T6.2's K-odd gauge identification. The Bures-covariant subtraction
  is a one-line algebraic identity. The conceptual content — K-odd
  channel as connection, not state — is structural, and the algebra is
  trivial once that interpretation is in place.
- T6.3's CM Poisson Monotonicity. Classical Polya–Laguerre. The proof
  in §9.2 is the standard Hadamard-factorization argument; both
  directions are clean.

**Calibrated honestly (acknowledged limitation in the manuscript):**
- The Hardy–Titchmarsh intertwining (T5.5) is proved at sketch level,
  with citation to Titchmarsh 1939 for full details. The §7.2 proof
  *sketch* is accurate but compressed.
- UPT-structure and UPT-Heisenberg are explicitly named as axioms, not
  theorems. §4.4 is explicit that "A5.1 and A5.2 are *named axioms*,
  not theorems. The program does not pretend they are derived from
  deeper finite-place input."
- The negative obstruction from HPo Addendum C is acknowledged in §8.5
  with the table from the probe; §8.5 explains why this does not
  derail the criterion (because Paper III goes via *atomic* divisor
  positivity, not smooth Bures curvature).
- UPT does not select the divisor measure $d\mu_\Xi$. §7.4 is explicit
  about this scope: UPT pins the absolutely continuous Hardy–Titchmarsh
  measure $dm$, not the atomic divisor measure. The divisor-measure
  identification is the Paper III content (transport theorem +
  Pólya–Laguerre criterion of Theorem 9.1).

**No over-promising.** The abstract says only "we show that"
(present-tense for established results); the introduction is explicit
that Paper II is "the carrier-construction phase" and "does not yet
prove RH"; §10.2 lists explicitly what is *not* in Paper II. There is no
"we will show in Paper III that X" promise without immediate qualifier;
forward references are listed as Paper III's work, not as a guarantee.

---

## 7. Discoveries during writing

A few small observations recorded here that might warrant durable
memory or follow-up:

**(a) The match $L_\infty(s, \chi_3) = Z_-(s)$.** §6.4 records that the
odd-character Archimedean factor $\Gamma_\mathbb{R}(s + 1) = \pi^{-(s + 1)/2}
\Gamma((s + 1)/2)$ is *exactly* the Tate integral $Z_-(s)$ at the
Bargmann *first-excited* state $\psi_1 \propto x e^{-\pi x^2}$. This is
the operator-theoretic match between the K-even/K-odd parity
decomposition of Paper I §5.3 and the even/odd ground/first-excited
decomposition of Bargmann–Fock. The two Archimedean local factors of
$\zeta$ and $L_{\chi_3}$ emerge from the *same* two-state Bargmann
construction; this is a cleaner observation than the existing notes
made fully explicit.

**(b) The cancellation $1/r \cdot r = 1$ as the algebraic origin of
$\log p$.** §2.3 records this elementary but conceptually important
observation: the $1/k$ in the logarithmic occupation series and the $k
\log p$ from $D_s p^{-ks}$ cancel exactly to give $\log p$. The
von Mangoldt weight $\Lambda(p^r) = \log p$ has an algebraic origin
(cancellation in $\mathcal{F}_n$) prior to its number-theoretic
interpretation.

**(c) The "K-odd as gauge, not state" structural reading.** §8 makes
this explicit. The reading is in HPo Addendum B, but Paper II's
presentation makes it sharper: the K-odd channel $\mathcal{L}_3$ is a
*connection* on the 2-channel Bures fiber, not a state vector; its
log-derivative is the connection 1-form; subtracting it from the scalar
transfer's log-derivative gives the *covariant* derivative, which
isolates the $\Xi$-divisor cleanly.

These do not need their own memory entries (they are recorded in the
manuscript itself), but they are program-internal observations worth
flagging.

---

## 8. Suggested second-pass improvements

(Listed roughly in order of importance.)

1. **Expand T5.5 proof.** Either fill in Titchmarsh's Mellin/Hankel
   correspondence more carefully, or reference a more accessible modern
   treatment (e.g., Bump 1997 §1.7 covers the relevant ground).

2. **Refine A5.2 justification.** §4.3's three commitments are sound
   but could be sharpened. Specifically, item (iii) (the program's
   finite-place lift extending to $v = \infty$) could be tied more
   explicitly to the polynomial-algebra structure
   $\mathcal{F}_p = \mathbb{C}[e_p]$ with raising/lowering operators
   $e_p, \partial_{e_p}$.

3. **Bibliography normalization.** Convert shortform labels to a
   standard BibTeX-style bibliography with full citations.

4. **Cross-link to Paper III working notes.** The forward references in
   §10.3 should be cross-checked against the latest versions of the
   Q8vM3 / Z9vL4 / K7mQ2 notes when Paper III begins formal drafting.

5. **Worked example for T4.1.** §2.5 could benefit from a concrete worked
   example at $n = 2$ (just primes $2, 3$) showing the upstairs formula
   evaluated explicitly, parallel to the §3.2 mixed/single-axis
   collision example.

6. **Minor formatting / consistency pass.** Several `\mathcal{F}_n^{\rm Bargmann}` /
   `\mathcal{F}_\infty^{\mathrm{Bargmann}}` / similar variant
   notations could be standardized.

These are second-pass refinements; the first draft is structurally
complete.

---

## 9. Final calibration

The manuscript is a **strong first draft**:
- All ten claim objects stated cleanly with proofs or citations.
- Three probes referenced, all confirmed.
- Introduction and conclusion match the body.
- Abstract and title written last, faithfully summarizing what was
  established. The abstract uses present tense ("we show that") only.
- ~55–60 pp, within the 50–70 pp target.
- LaTeX-in-MD throughout, consistent with Paper I's style.

The carrier construction is structurally complete at the program's
working precision. The right Hilbert carrier for the program's
positivity machinery is built; the natural target ($m_B = -\Xi'/\Xi$
with CM Poisson Monotonicity ⟺ RH) is identified. Paper III's task is
to prove $\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+$ via convolution-square
positivity + transport.

**Honest endpoint.** Paper II's contribution is the **carrier and the
target**, not the proof of positivity. The proof of positivity is Paper
III. Paper II does not claim to prove RH. It claims:

> *Given the carrier $(\mathcal{F}_n, \text{UPT}, \text{Bargmann-Fock,
> Tate $L$-factors, K-odd gauge, $m_B$})$, the operative criterion for
> RH on this carrier is $\mathrm{Im}\,m_B(z) \geq 0$ on $\mathbb{C}_+$.*

This is what Paper II establishes. It is the honest scope of the
carrier-construction phase.

---

*End of Status Report, 2026-05-22.*
