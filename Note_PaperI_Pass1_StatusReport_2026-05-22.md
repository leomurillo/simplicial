# Paper I — Pass 1 Status Report

**Session date:** 2026-05-22 (later session, same day as Draft 1).
**Deliverable:** `Paper-I-Identification-Draft1.md` (edited in place).
**Status:** Pass 1 refinement complete.

---

## Scope

Pass 1 was a controlled refinement of the first-draft manuscript, discharging
the six second-pass priorities identified in
`Note_PaperI_Draft1_StatusReport_2026-05-22.md`. No redrafting, no
reorganization, no scope expansion. Two probes were re-run to confirm
numerical claims still hold.

---

## What was discharged

### Priority 1 — §3.4 term-by-term contraction (~2/3 page net)

The proof of **Theorem 3.1** (closed-form cubic A-C tensor on $\mathbb{Z}/N$)
now displays the five-term contraction of $T_{ijk}(Q^{(N)}(s))$ against
$\chi_a \otimes \chi_b \otimes \chi_c$ explicitly:

- *Term 1* (linear, $\delta_{ij}\delta_{ik}$) → $\hat Q^{(N)}_{a+b+c}$.
- *Term 2* (bilinear, $\delta_{ij}$) → $-\hat Q^{(N)}_{a+b}\,\hat Q^{(N)}_c$.
- *Term 3* (bilinear, $\delta_{ik}$) → $-\hat Q^{(N)}_{a+c}\,\hat Q^{(N)}_b$.
- *Term 4* (bilinear, $\delta_{jk}$) → $-\hat Q^{(N)}_a\,\hat Q^{(N)}_{b+c}$.
- *Term 5* (cubic, no $\delta$'s) → $+2\,\hat Q^{(N)}_a\,\hat Q^{(N)}_b\,\hat Q^{(N)}_c$.

The pre-theorem polynomial-in-$\hat Q$ display was trimmed (it was being
shown twice; now shown once, inside the proof).

**Bug fixed in passing.** While writing out the contraction I noticed the
displayed $T_{ijk}$ formula in §1.2 and the displayed substitution in §3.4
had a non-symmetric fourth term: `-p_j p_k δ_{jk}` (and the
$Q^{(N)}$-analog) instead of `-p_i p_j δ_{jk}`. The cumulant tensor is
totally symmetric by Clairaut, so the latter is correct. The resulting
final theorem statement was unaffected (the buggy term vanishes for
non-trivial characters under contraction, since the freed-up index has no
constraining $\delta$), but the primitive formula now matches the
symmetric Amari–Chentsov tensor. This is a Pass-1 internal-consistency
fix; the upstream sources (`siete.md`, `ל2`) were not edited per Pass 1
discipline. Flagged here for future propagation.

### Priority 2 — §5.6 explicit $T_j$ properties (~1/3 page net)

Took **Option B** as recommended. Added a "(P1)/(P2)/(P3)" structural-property
block immediately after the cubic-in-$r$ expansion display:

- (P1) $T_3(s) = 2\,\beta_a(s)\,\beta_b(s)\,\beta_c(s)$ — the $r^3$
  coefficient as a triple-$\beta$ product.
- (P2) $\beta_k(s) = 0$ on the K-fixed character indices $k \in \{0, 3\}$.
  (Proof from the K-odd DFT-pair $r \leftrightarrow k$.)
- (P3) $T_0(s)$ is the on-shell ($r = 0$, $L_3 = 0$) piece, a polynomial
  in the K-even $\alpha_k$'s alone.

Explicit pointer to [HPo-notes, Addendum A5] for the full closed forms.
The existing structural observation (a) was tightened to "immediate from
(P1), (P2)"; (b), (c) unchanged.

### Priority 3 — Numerical tables (~1/2 page net)

**§5.5:** Added a three-row table of probe output at the first three
$\zeta$-zero ordinates $\gamma_n$:

| $\gamma_n$ | Hurwitz max err | $|F_3(\rho_n)|$ | $|F_1 + F_5|(\rho_n)$ |
|---|---|---|---|
| $14.13472514\ldots$ | $1.01 \times 10^{-60}$ | $6.5 \times 10^{-16}$ | $1.8 \times 10^{-15}$ |
| $21.02203964\ldots$ | $\sim 10^{-60}$        | $9.7 \times 10^{-16}$ | $2.3 \times 10^{-15}$ |
| $25.01085758\ldots$ | $\sim 10^{-60}$        | $5.8 \times 10^{-16}$ | $1.5 \times 10^{-15}$ |

**§6.2:** Reformatted the class-number-formula check from inline
parenthetical to displayed equation. Computed value $L(1, \chi_3) \approx
0.6046000107$ (from current probe, deterministic at `mp.dps = 40`);
theoretical $\pi/(3\sqrt{3}) \approx 0.6045997881$; agreement within
$3 \times 10^{-7}$. The discrepancy is consistent with the probe's
evaluation at $s = 1 + 10^{-6}$ (deliberately off the pole), where the
residual offset $|L'(1, \chi_3)| \cdot 10^{-6}$ matches. The previous
draft phrasing "agreement to seven decimal places" was loose by strict
digit-by-digit comparison (the numerals diverge at the 4th decimal place,
though the magnitude of the difference is $\sim 10^{-7}$); the rewrite
gives the unambiguous $3 \times 10^{-7}$ bound.

### Priority 4 — Provenance ledger (~1/2 page net)

The "What is new here, what is cited" subsection of the Introduction was
rewritten from a three-bullet summary to a section-by-section ledger, one
bullet per claim object (T2.1, T2.2, T2.3, T3.1, T3.2, T3.3, I3.4, T5.3).
Each bullet now states *(claim label, descriptor, §-anchor)* + provenance
+ what is new in Paper I vs. inherited. The closing two-line probe
summary was tightened.

### Priority 5 — Explicit $L(s, \chi_6) = (1 + 2^{-s}) L(s, \chi_3)$ (~1/3 page net)

Inserted an explicit derivation paragraph after the proof of Theorem 5.1.
The derivation:
1. Factorizes characters mod 6 via CRT as products of mod-2 × mod-3 characters.
2. Identifies the unique non-trivial character mod 6 as $\chi_6^{\mathrm{ind}}
   := \chi_0^{(2)}\chi_3$ (non-primitive, conductor 3).
3. Compares Euler products factor by factor — only $p = 2$ differs,
   contributing $(1 + 2^{-s})$ as the missing Euler factor.

**Sharpening fixed in passing.** The previous draft phrase "the unique
non-trivial *primitive* Dirichlet character modulo $6$" was incorrect
(there is no primitive character of conductor 6; the unique non-trivial
mod-6 character is induced from $\chi_3$, hence non-primitive). The
rewrite uses the precise term "$\chi_6^{\mathrm{ind}}$ ... necessarily
non-primitive, induced from $\chi_3$ of conductor 3."

### Priority 6 — §6.4 row-by-row justification balanced (~1/3 page net)

All 7 rows now have explicit one-sentence justifications:

- **Row 1** (new): $\zeta_\mathbb{Q} = \zeta$ as the trivial rank-1 line
  bundle = K-fixed $\zeta$-channel.
- **Row 2** (lightly rephrased): the Galois-cover factorization
  $\zeta_K = \zeta \cdot L_{\chi_3}$ as the Connes–Consani 2-channel data.
- **Row 3** (promoted from closing paragraph to its own bullet): Arakelov
  norm = Bures Hermitian metric $h = (|\Xi|^2 + |\mathcal{L}_3|^2)^{-1}$,
  with pointer to [HPo-notes, Addendum C1].
- **Rows 4–5** (unchanged): K-involution = Galois involution via
  $\zeta_6^k \mapsto \zeta_6^{-k}$ under DFT pairing.
- **Row 6** (unchanged): singular strata = joint zeros of $\zeta$ and
  $L_{\chi_3}$, sorted by Galois parity.
- **Row 7** (new): Connes–Consani tensor product = multiplicative L-function
  product, instantiated by the Dedekind factorization.

The trailing "remaining rows are direct analogues" sentence was removed
(every row now has a dedicated justification).

---

## Issues found during end-to-end read

1. **Non-symmetric $T_{ijk}$ formula in §1.2 and §3.4** (described under
   Priority 1). Fixed in place in the manuscript; flagged for upstream
   propagation to `siete.md` and `ל2` (out of Pass 1 scope per rule 7).
2. **"Primitive character modulo 6"** in §5.2 (described under Priority 5).
   Fixed.
3. **Class-number-formula "seven decimal places" phrasing** (§6.2). Fixed
   to "within $3 \times 10^{-7}$" — same content, unambiguous.

No further inconsistencies, dead cross-references, or numbering bugs were
found. Theorem numbering (T1.1–T1.3, I1.4, T2.1–T2.3 = Thm 2.1, Thm 3.1,
Thm 4.1; T3.1, T3.2 = Thm 5.1, Thm 5.2; T5.3 = Thm 5.3; T3.3, I3.4 =
Identification statements in §6.4, §6.5) is consistent between body,
abstract, introduction provenance ledger, and §7.3 hand-off list.

---

## Length

**Before Pass 1:** 1497 lines, ~10.6 k words, ~78 kB.
**After Pass 1:** 1622 lines, ~11.5 k words, ~85 kB.
**Net:** +125 lines (+8.4%), +830 words (+7.8%), +7 kB.

Estimated LaTeX page count: 42–48 pp (was 40–45 pp). Within the Pass 1
target of +2–3 pp.

---

## Empirical re-verification

Both probes were re-run prior to editing:

- **`probe_Hurwitz_z6_closed_form.py`**: Hurwitz closed-form at
  60-digit `mpmath` precision verified across all five non-trivial residues
  $r \in \{1, \ldots, 5\}$ and the sample of $s$-values; max err
  $\sim 10^{-60}$. K-even constraints $|F_3|, |F_1 + F_5|, |F_2 + F_4| \leq
  3 \times 10^{-15}$ at the first three on-line $\zeta$-zero ordinates.
  $B_G$-at-zero closed form matches direct numerical evaluation to
  machine precision.
- **`probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`**: Dedekind
  factorization $\zeta_K = \zeta \cdot L_{\chi_3}$ verified against finite
  Euler product (norms $\leq 200$) at $s = 2, 3, 1.5, 2+5i$, diff
  $\leq 4 \times 10^{-2}$ (truncation-error-dominated; tail factor is
  $O(N^{-(\mathrm{Re}\,s - 1)})$). Class-number formula
  $L(1, \chi_3) \approx 0.6046000107$ vs $\pi/(3\sqrt{3}) \approx
  0.6045997881$, agreement within $3 \times 10^{-7}$.

Both probes pass. No empirical claims in the manuscript required revision
beyond §6.2's numerical display value.

---

## What Pass 1 did not address

The Pass-1 spec explicitly bounded scope; the following items remain (and
are correctly out of Pass-1 scope):

- **§4.2's $\chi^{\mathrm{full}}(s; d_k)$ multiplier** is still
  schematic. The status-report Pass-1 priorities did not include
  making this explicit; the schematic form suffices for §4.3's
  chi-factor cancellation argument.
- **Full closed forms for $T_1(s), T_2(s)$** (the middle two
  cubic-in-$r$ coefficients). Per Option B, only structural properties
  P1–P3 were added; the explicit forms remain in [HPo-notes, Addendum A5].
- **Bibliography normalization.** The reference list is still in
  short-label form (`Iwaniec & Kowalski, 2004`); LaTeX `\cite{}`
  conversion is a separate pre-submission step.

---

## Calibration

**Strong success on the six priorities.** Each was discharged with
in-place edits, no redrafting, no new theorems, no scope drift. Net
length increment is 8% — well within the +2–3 pp target.

**Two upstream bugs found and fixed within Paper I** (non-symmetric
$T_{ijk}$ formula; "primitive mod 6" misnomer). Both are consistency
fixes within the manuscript; they imply analogous corrections in
`siete.md` and `ל2` that are out of scope for Pass 1 but should land
in those documents in a future pass.

**Manuscript reads cleanly end-to-end** after Pass 1. Section structure
unchanged. Title, abstract, and theorem numbering unchanged. Provenance
ledger now granular section-by-section, which improves discoverability
for the next reader.

**Honest assessment of remaining roughness.** The pass did not attempt
the explicit forms of $T_1, T_2$, nor an explicit $\chi^{\mathrm{full}}$
in §4.2. Both were excluded from the Pass-1 spec; both are tractable in
a future Pass 2 if commissioned. Neither blocks downstream use of Paper
I as the substrate for Paper II.

---

## What is, and is not

**This refinement is:**
- A controlled second pass over Draft 1 of Paper I.
- The discharge of the six Move-7 status-report priorities.
- An internal-consistency check that caught and fixed two upstream
  formula bugs.

**This refinement is not:**
- A Draft 2 (no structural redraft was attempted).
- An expansion of the manuscript's analytic content (no new theorems).
- A propagation pass to upstream sources (`siete.md`, `ל2`, etc.).
- A LaTeX-ready preparation (bibliography normalization deferred).

The updated draft is on disk at
`C:\Projects\simplicial\Paper-I-Identification-Draft1.md`.
Pass 1 deliverable is complete.
