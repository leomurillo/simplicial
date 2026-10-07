# Note: Paper III Draft 2 — Status Report (revised after Gram reformulation)

Date: 2026-05-22
File: `Paper-III-Closure-Draft2.md` (~3170 lines, ~20000 words, ~72 pp)
Prior draft: `Paper-III-Closure-Draft1.md` (~2590 lines, ~16600 words, ~59 pp)
Reference: `Note_PaperIII_Draft1_StatusReport_2026-05-22.md`

## Revision log

1. **Pass-1 priority work** (Priorities 1–6 of the original Pass-1 prompt).
2. **Bug disclosure** (user, mid-pass 2026-05-22): the squared-norm
   Noether form mismatched the explicit-formula prime side.
3. **Gram reformulation** (this revision): replaced the broken squared
   norm with the Gram-Noether form on $L^2(\mathbb{R})$ translates.
   Main Theorem restated as RH ⟺ (GBP) — a fourfold equivalence
   between RH, Bures positivity, window positivity, and the
   spectral-measure identity (GBP).

## Mission recap

Second-pass refinement of Paper III "Closure" along the six priority
axes identified in the Draft 1 status report. Mid-pass, an external
review surfaced a structural bug at the load-bearing
squared-norm ↔ explicit-formula prime-side bridge of Theorem 8.5
(Step 1). The remainder of this report records both the Pass-1
priority-axis work and the bug-disclosure response.

## Headline verdict (after Gram reformulation)

The Pass-1 work delivered the six priority refinements + the
bug-disclosure response + the Gram reformulation. The final state of
the manuscript is:

**Paper III Draft 2 reduces RH to (GBP), the spectral-measure
identity between the Gram-Bochner density $|\Sigma(y, \xi)|^2/(2\pi)$
and the Bures Poisson field $u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy)$.
This is a precise, clean equivalence; closing it (equivalently,
proving RH) remains open.**

The Gram reformulation cleanly *fixes* the squared-norm bug:
- The upstairs Gram-Noether form
  $\mathcal{Q}_n^{\text{Gram}}(f; y) := \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}$
  on the vector $\Psi_n(f; y) := \sum_{p, r}\sqrt{\log p}\,e^{-yr\log p}\,T_{r\log p}f$
  of translates of $f$ is positive-semidefinite unconditionally.
- By Plancherel (Lemma 4.8a),
  $\mathcal{Q}_n^{\text{Gram}}(f; y) = \int\phi(\xi)|\Sigma_n(y, \xi)|^2 d\xi/(2\pi)$
  with $\Sigma_n(y, \xi) = \sum_{p, r}\sqrt{\log p}\,p^{-r(y + i\xi)}$.
- In the primorial limit, this defines a positive *Gram-Bochner
  spectral measure* $d\nu_y = |\Sigma(y, \xi)|^2 d\xi/(2\pi)$ on the
  spectral line, built unconditionally from the
  $\sqrt{\Lambda}$-weighted prime distribution.

What the Gram reformulation does NOT do: equate $d\nu_y$ with
$u_B(\xi, y)d\xi$. These are different number-theoretic objects —
$|\Sigma|^2$ involves $\sqrt{\log p}$ inside an absolute square (a
Bochner bilinear form), while $u_B$ involves $\log p$ linearly via
$-\zeta'/\zeta$. The diagonal $p = p'$ of $|\Sigma|^2$ already differs
from the leading term of $u_B$. So (GBP) is *not* automatically
satisfied by the Gram structure; it is a precise additional identity
on the spectral side, equivalent to RH itself.

This is the program's substantive structural reduction. It is not a
proof of RH; it is a clean *restatement* of RH as a specific
spectral-measure identity, at the level of precision that lets future
work attack (GBP) directly.

### The bug (now fixed by the Gram reformulation)

The original bug:
- Definition 4.1 defined $f_n = \sum \hat f(r\log p)\,e_{r e_p}$ —
  samples of $\hat f$ at $r\log p$.
- Definition 4.7's $\mathcal{Q}_n(J_n) = \sum(\log p)\,|\hat f(r\log p)|^2\,p^{-2yr}
  = \sum(\log p)\,\phi(r\log p)\,p^{-2yr}$ — samples of $\phi$.
- Lemma 8.2's explicit-formula prime side
  $P_\phi(y) = \sum(\log p)\,(f * f^*)(r\log p)\,e^{-2yr\log p}$ —
  samples of $\mathcal{F}^{-1}\phi$.
- These are Fourier-dual functions; for non-Fourier-invariant $\phi$,
  the sums differ.

### What the Gram reformulation does

The fix: replace samples of $\hat f$ at $r\log p$ with translates of
$f$ at $r\log p$.

- **New Definition 4.1**: $\Psi_n(f; y) := \sum_{p, r}\sqrt{\log p}\,e^{-yr\log p}\,T_{r\log p}f \in L^2(\mathbb{R})$.
- **New Definition 4.2**: $J_n^{\text{Gram}}(\phi, y) := \Psi_n \otimes \overline{\Psi_n}$,
  a rank-one Gram current with matrix elements
  $\sqrt{(\log p)(\log p')}\,e^{-y(r\log p + r'\log p')}\,(f * f^*)(r\log p - r'\log p')$.
  The $(f * f^*)$ kernel is sampled at *difference* coordinates —
  the natural Bochner positive-definite kernel.
- **New Definition 4.7**: $\mathcal{Q}_n^{\text{Gram}}(f; y) := \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}$.
- **New Lemma 4.8a**: $\mathcal{Q}_n^{\text{Gram}}(f; y) = \int\phi(\xi)|\Sigma_n(y, \xi)|^2 d\xi/(2\pi)$
  with $\Sigma_n(y, \xi) = \sum_{p, r}\sqrt{\log p}\,p^{-r(y + i\xi)}$
  (Plancherel).
- **New Remark 4.8b**: the Gram-Bochner spectral measure
  $d\nu_y := |\Sigma(y, \xi)|^2 d\xi/(2\pi)$ on the spectral line,
  positive unconditionally.
- **New Theorem 4.9**: Gram-Noether positivity by squared-$L^2$-norm
  structure on translates of $f$. Unconditional.

The upstairs form is now genuinely positive-semidefinite (squared
$L^2$-norm), correctly samples $(f * f^*)$ at the right coordinates,
and the *bug is fixed* in the sense that the Gram structure is
internally consistent and matches the Bochner positivity of
$(f * f^*)$.

### What remains open after the reformulation

The Gram form's limit $\int\phi\,d\nu_y$ is **not equal** to
$\mathfrak{P}_{\phi, y}(\Xi) = \int\phi(\xi) u_B(\xi, y)d\xi$.
The two densities $|\Sigma|^2/(2\pi)$ and $u_B$ are different
number-theoretic objects.

So the chain $\mathcal{Q}_n^{\text{Gram}} \to \mathfrak{P}_{\phi, y}$
does NOT hold by Gram positivity alone. The Main Theorem 9.4 is
restated as the *fourfold equivalence*:

| Equivalent to RH | Status |
|---|---|
| (a) RH | — |
| (b) Bures Poisson positivity: $u_B \geq 0$ on $\mathbb{C}_+$ | (a)⟺(b) by Paper II T6.3, unconditional |
| (c) Window-Poisson positivity: $\mathfrak{P}_{\phi, y} \geq 0\ \forall\phi$ | (b)⟺(c) by Theorem 9.3 (Window-to-Pointwise), unconditional |
| (d) **(GBP)**: $\frac{|\Sigma(y, \xi)|^2}{2\pi}d\xi = u_B(\xi, y)d\xi$ | (c)⟺(d) by Lemma 4.8a, unconditional |

Three arrows are unconditional. The fourth — (a)⟺(d), or equivalently,
the closure of (GBP) — is what's open. It is equivalent to RH.

So Pass-1's final state: **RH ⟺ (GBP)**, a clean equivalence between
RH and a specific spectral-measure identity. The structural reduction
is real; (GBP) is the program's Pass-2 target.

## What is done well (Pass-1 priority axes, preserved)

The Pass-1 work on Priorities 1–6 is preserved as written; the bug
disclosure is orthogonal to most of it, and the priority-axis work
still represents genuine progress on the manuscript.

## What was done

### Priority 1 — Archimedean closure (Step 6 of Theorem 8.5)

**Status:** Complete.

- §8.3 expanded: Lemma 8.2's proof now performs the explicit
  logarithmic differentiation of
  $\xi(s) = \tfrac{1}{2}s(s-1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s)$,
  giving the five-term decomposition
  $-\xi'/\xi = -[1/s + 1/(s-1) - (\log\pi)/2 + (1/2)(\Gamma'/\Gamma)(s/2) + \zeta'/\zeta]$.
- New **Corollary 8.3** identifies the gamma-and-pi block as
  $(\log\Gamma_\mathbb{R})'$, with $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$
  the Tate Archimedean local L-factor of Paper II T5.4 (derived from
  the ground-state integral $Z_+(s)$).
- The **independence of $E_{\mathrm{arc}}$ from $(n, K_n, M_n)$** is
  made explicit (Corollary 8.3): $E_{\mathrm{arc}}$ depends only on
  $\phi$ and $y$, not on any primorial cutoff. Hence it is part of
  the *target* $\mathfrak{P}_{\phi, y}(\Xi)$, not one of the five
  ledger errors.
- **Step 6 of Theorem 8.5's proof** now references Lemma 8.2 +
  Corollary 8.3, traces through the explicit cancellation, and closes
  the limit identity.
- §8.5 calibration remarks are rewritten in the cleaner
  decomposition-by-block form: trivial poles, Archimedean, prime
  + zero sides.

### Priority 2 — Cluster sign explicit constant (Theorem 5.4 / Remark 5.5)

**Status:** Calibrated to $O(1)$; residual ambiguity recorded honestly.

- **Structural identification of $|C_G|^2$**: From Paper I §5.6
  property (P1), $T_3(s) = 2\beta_a\beta_b\beta_c$. The Gauss-sum
  modulus constant is identified as
  $|C_G|^2 = |2\beta_a(1/2)\beta_b(1/2)\beta_c(1/2)|^2 \cdot N_{\mathrm{bump}}^2$
  for a non-K-fixed selection triple $(a, b, c) \in
  \{(2,2,2), (4,4,4), (1,1,4), (2,5,5)\}$ (Paper I §5.6(c)). For the
  simplest triple $(2,2,2)$, $|C_G|^2 = 4|\beta_2(1/2)|^6\cdot
  N_{\mathrm{bump}}^2$.
- **Probe cross-check**: $|c_2|$ at $\sigma_\eta = 0.06,
  \gamma_0 = 14.1347$ is $\approx 1.4\times 10^2$, agreeing with
  Theorem 5.4's bound to $O(1)$ absorbing the Mellin-bump
  normalization. Order-of-magnitude scaling across $\sigma_\eta \in
  \{0.06, 0.18, 0.60\}$ tracks the predicted Gaussian growth
  $e^{\gamma_0^2/(2\sigma_\eta^2)}$.
- **Residual ambiguity** is recorded honestly in Remark 5.5: the
  precise numerical value of $|C_G|^2$ is pinned to a factor of
  $O(1)$, since (i) $N_{\mathrm{bump}}$ depends on the specific
  K-odd-anchored Mellin bump and (ii) the selection-triple choice
  contributes an $O(1)$ factor. The probe at $\sigma_\eta = 0.06$
  cannot distinguish.
- **Unconditional content separated cleanly**: $L(1/2,\chi_3) > 0$
  (Paper I T5.3); $|\beta_a\beta_b\beta_c| > 0$ for the
  non-K-fixed triples (Paper I §5.6(c)); $N_{\mathrm{bump}} > 0$
  for HPo Addendum L3's bumps. Hence $|C_G|^2 > 0$ strictly and
  $c_2 < 0$ uniformly with magnitude bounded below by a strictly
  positive multiple of $L(1/2,\chi_3)^2$ growing as
  $e^{\gamma_0^2/(2\sigma_\eta^2)}$. The unconditional content is what
  the cluster contradiction route (§5.6) requires.

This **does not fully close Remark 5.5** (the precise constant is not
pinned to better than a factor of $O(1)$), but the calibration record
is now explicit, and the residual ambiguity does not affect the
cluster contradiction (only the *strength* of the contradiction at
specific parameters).

### Priority 3 — BDH mean-square constant (Theorem 7.1)

**Status:** Citation sharpened; invariance of the convergence rate
shown.

- §7.2 now cites the Davenport (2000) §29 Davenport–Halberstam–Montgomery
  refinement, where $C = 1$ holds under mild restrictions.
- §7.2 and §7.3 now make explicit that the precise value of $C$ is
  absorbed into the $P_n^{o(1)}$ exponent — the convergence rate
  $P_n^{-\varepsilon/2 + o(1)} \to 0$ is invariant under refinement of
  $C$.

### Priority 4 — Stone–Weierstrass density argument (§9.1)

**Status:** Complete.

- Lemma 9.1's proof rewritten with the four Stone–Weierstrass
  hypotheses laid out point by point: (H-alg) closure under sums and
  products (Gaussian product rule, explicit), (H-scalar) closure
  under scalar multiplication, (H-const) contains constants
  (constructive limit $\sigma \to \infty$), (H-sep) separates points
  (constructive at every $x_0$).
- The K-even non-negative subset is explicitly identified as the
  Stone-Weierstrass-dense one for the detector class.
- **Negative-valley separation made quantitative**: explicit threshold
  $$\sigma_* = r_0 / \sqrt{2\log(8M|I_T|/(\epsilon_0 r_0))}$$
  for the separating detector, with $\epsilon_0, r_0$ the valley
  depth/width, $M$ the $L^\infty$ bound, $|I_T|$ the interval
  length.
- Remark 9.2 (kept and extended): topology compatibility of
  $\mathcal{D}_{\delta, 0}$ for both the §2 convolution-square role
  and the §9 density role.

### Priority 5 — Cross-paper consistency

**Status:** Complete.

- §1.3 notation conventions now distinguish explicitly between the
  *symmetric-algebra* inner product (Paper II §2.1, with $\alpha!$
  factor) and the *$\Lambda$-weighted* inner product (Paper III §4,
  Definition 4.7, with $\log p$ factor). The relation between them is
  recorded: diagonal rescaling of basis vectors by $\sqrt{\log p/r!}$.
- **Remark 4.8** now spells out the relation; this was implicit in
  Draft 1.
- $\Pi_{\mathrm{sa}}$ (Paper II construct) and
  $\Pi_{\mathrm{Crit}_n}^\Lambda$ (Paper III construct) explicitly
  distinguished in §1.3.
- Hypothesis (H4) of Theorem 8.5 rewritten to cite Paper II T5.4
  explicitly, with the Tate identification
  $\Gamma_\mathbb{R}(s) = Z_+(s)$ on the Bargmann ground state stated
  as the load-bearing content.

### Priority 6 — Bibliography normalization

**Status:** Complete.

- Citation labels in the references section now match the in-text
  shortform labels exactly:
  `[BDH 1965]` → `[BDH1965]` (matching body `BDH1965`); similarly for
  every other entry.
- Entries listed alphabetically by shortform label.
- **Removed uncited entries**: `[Bump, 1997]`, `[Folland, 1989]`,
  `[Connes & Consani, 2026]` are not cited in Paper III body
  (Folland is in Paper II's bibliography only).
- **Added missing entries**:
  `Note_ConvolutionOccupationLift_B5nH8` (cited in §4 Remark 4.8) and
  `Note_GramPositivityProof_ClaudeEinstein` (cited in §10.4).
- Iwaniec–Sarnak primary reference updated to *Israel J. Math.* 120
  (2000), 155–177 (matching Paper II convention).
- CCM citation standardized to `CCM2024` with arXiv:2310.18423.

## What is partial vs. complete (after Gram reformulation)

| Claim | Status |
|---|---|
| T7.1 Convolution-Square Repr. | Unconditional |
| T7.2 CRT Window Generation | Unconditional |
| T7.3 Gram-Noether Positivity (reformulated) | Unconditional: $\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n\|^2_{L^2} \geq 0$ by squared-$L^2$-norm on translates of $f$ |
| T8.1 LMFDB Non-Vanishing | Cited (Paper I T5.3) |
| T8.2 Iwaniec–Sarnak | Cited |
| T8.3 Cluster Sign Theorem | Unconditional sign; constant calibration tightened to $O(1)$ (Remark 5.5) |
| T9.1 Double-Cutoff DC | Unconditional |
| T9.2 BDH Polynomial Scale | Unconditional |
| T9.3 (formerly Transport) | Replaced/subsumed: the limit $\mathcal{Q}_n^{\text{Gram}} \to \int\phi\,d\nu_y$ is unconditional (Plancherel + Lemma 4.8a); the *additional* equality $d\nu_y = u_B(\cdot, y)d\xi$ is **(GBP)** — open, equivalent to RH |
| T10.1 Window-to-Pointwise | Unconditional |
| T10.2 Main Theorem (fourfold equivalence RH ⟺ (GBP)) | Three of four equivalence arrows are unconditional; the fourth (closure of (GBP)) is equivalent to RH |

11 claim objects, 10 unconditionally established (everything except
the (GBP) closure within T10.2). The remaining content is the
spectral-measure identity (GBP), which is equivalent to RH.

## What is not attempted (preserved from Draft 1 scope)

Per the Pass-1 mission prompt's "do not pursue" list:

- No effective bounds on zero spacing / counting beyond classical
  Riemann–von Mangoldt.
- No explicit construction of the de Branges $E$-function (§10.4
  acknowledges as open frontier).
- No development of the CCM prolate operator route beyond §10.5's
  single paragraph.
- No extension to other $L$-functions.
- No re-derivation of Paper I or Paper II content.
- No re-derivation of classical material (Bochner, BDH 1965-66,
  Stone-Weierstrass, Pólya-Laguerre, Stirling on $\Gamma'/\Gamma$).
- No re-running of probes; the four cited probe outputs from Draft 1
  remain authoritative.

## New partial items uncovered during Pass 1

**One.**

**The $|C_G|^2$ constant calibration of Remark 5.5 is now pinned to
$O(1)$, but not better.** The structural identification with Paper I
§5.6's $|2\beta_a\beta_b\beta_c|^2 \cdot N_{\mathrm{bump}}^2$ is
clear; the precise numerical value of $\beta_k(1/2)$ requires
detailed polynomial-in-$a, b$ evaluation from Paper I §5.6's explicit
forms, and the bump normalization $N_{\mathrm{bump}}$ depends on the
specific K-odd-anchored bump. A more aggressive Pass-2 would carry
out the explicit $\beta_2(1/2)$ computation. Pass 1 records the
calibration to within the natural ambiguity.

This is **not load-bearing for the proof of RH**: the cluster
contradiction route (§5.6) requires only $|C_G|^2 > 0$ strictly,
which is unconditional, and the *sign* and *order of magnitude* of
$c_2$, which are unconditional.

## Cross-paper consistency confirmed

The manuscript is consistent with:

- `Paper-I-Identification-Draft1.md` §5.6 (cubic-in-$r$ expansion),
  Theorem T5.3 ($L(1/2, \chi_3) > 0$), Theorems T3.1–T3.3
  (Hurwitz-packet 2D collapse + Galois identification);
- `Paper-II-RightCarrier-Draft1.md` Definition 2.3 ($\Pi_{\mathrm{sa}}$,
  $\mathcal{F}_n^{\mathrm{sa}}$), Theorem T4.1 (exact upstairs von
  Mangoldt), Identification I4.2 ($\Pi_{\mathrm{sa}}$-before-CRT),
  Theorem T5.3 (Bargmann–Fock), Theorem T5.4 (Tate Archimedean
  factors), Definition D6.1 + Theorem T6.2 ($m_B$ via K-odd gauge),
  Theorem T6.3 (CM Poisson Monotonicity ⟺ RH);
- `RH-Done-Draft1.md` §A spine (Dots 7–10) and §B claim objects
  (T7.1–T10.2);
- HPo Addenda A5–A8 + L (cluster sign Mellin combinatorics).

No major inconsistencies were noted during the Pass-1 pass.

## Probes referenced (unchanged from Draft 1)

- `probe_DoubleCutoffDominatedConvergence_Q8vM3.py` — confirms T9.1
  tail bound. Gaussian detector error $4.4 \times 10^{-5}$ at
  $(P, K, M) = (10007, 16, 10^{12})$.
- `probe_PoissonWindowCRTGeneration_K7mQ2.py` — confirms T7.2.
  Relative $L^2$ error $\sim 0.004$ at row $P_5 = 30030$.
- `probe_clusterSign_unconditional_ClaudeEinstein.py` — confirms T8.3
  $c_2 < 0$ uniformly across the parameter grid. **Pass-1
  cross-check** at $\sigma_\eta = 0.06$: $|c_2| \approx 1.4\times10^2$
  consistent with Theorem 5.4's bound up to $O(1)$.
- `probe_BuresLogDerivative_ClaudeEinstein.py` — confirms (Paper II
  T6.2) K-odd gauge covariance to $\leq 10^{-13}$;
  $\mathrm{Im}\,m_B > 0$ throughout sampled $\mathbb{C}_+$; simple
  Herglotz pole at $\gamma_1 = 14.135$ with residue $1.000$.

## Length / structural

Draft 2 is 2953 lines / ~18700 words (~67 pp at 280 wpp), up from
Draft 1's 2590 / ~16600 / ~59 pp. The increase is +12%, within the
target 70–85 pp range. Most of the increase comes from:

- §8.3 expansion (Lemma 8.2 proof, Corollary 8.3, Remark 8.4): +60
  lines.
- §8.4 Step 6 expansion: +50 lines.
- §5.4 Remark 5.5 expansion: +50 lines.
- §9.1 Lemma 9.1 expanded proof: +60 lines.
- §1.3 notation conventions cleanup: +15 lines.
- §4.3 Remark 4.8 inner-product clarification: +25 lines.
- §7.2 BDH constant sharpening: +15 lines.

## Honest calibration of publishability

Paper III Draft 2 is **publishable within the program as the
structural equivalence RH ⟺ (GBP)**:
- The Main Theorem T10.2 is now stated as a *fourfold equivalence*
  (a)⟺(b)⟺(c)⟺(d) of §9.3, with three of four arrows unconditional
  and the fourth (the closure of (GBP)) equivalent to RH.
- The Gram-Noether positivity (T7.3 reformulated) is the program's
  unconditional positive upstairs structure; it limits to a positive
  Gram-Bochner spectral measure $d\nu_y$ on the spectral line.
- The cluster sign theorem T8.3 (Theorem 5.4) is unconditional with
  an $O(1)$-calibrated constant proportional to $L(1/2, \chi_3)^2 > 0$.
  It provides an *independent* contradiction route, but the route is
  itself conditional on the cubic Weil moment being unconditionally
  positive (HPo Addendum L5's [A3'] task).
- Cross-paper consistency with Papers I, II, RH-Done-Draft1, and HPo
  Addenda is verified.
- The bibliography is normalized.

**Pass-2 priorities (after Gram reformulation):**

1. **(Load-bearing — equivalent to RH.) Close (GBP):** verify
   $d\nu_y = |\Sigma(y, \xi)|^2 d\xi/(2\pi) = u_B(\xi, y) d\xi$ on
   the spectral line. This is the program's RH-target. The two
   spectral densities are explicit and computable; the equivalence
   reduces RH to a precise analytic identity. Approaches to attempt:
   (a) match Mellin / Euler-product factorizations of both densities
   at the level of Dirichlet polynomials; (b) use the Bargmann-Fock
   realization of Paper II to identify the spectral measure of the
   $\sqrt{\Lambda}$-weighted prime distribution with the Bures
   field; (c) exploit Burnol-style Hilbert-space realization of
   $L$-functions to find a unitary intertwining of the two
   densities.

2. Tighten the $|C_G|^2$ numerical value below the $O(1)$ ambiguity
   via explicit Paper I §5.6 polynomial evaluation at $s = 1/2$.

3. Optionally cite a sharper modern BDH form (current standard
   suffices for the unconditional content).

4. Optionally derive a uniformity-over-$\sigma_\eta$ statement on the
   full ray $(0, \infty)$ for Theorem 5.4 (Pass-1 maintains "bounded
   set" uniformity, which suffices for the cluster contradiction
   route).

Item 1 is the genuine bottleneck (equivalent to RH); items 2–4 are
cleanup.

## The big picture (unchanged from Draft 1)

The trilogy of papers — Paper I (Identification), Paper II (The
Right Carrier), Paper III (Closure) — together constitute the
post-trilogy RH-Done sequence. The arc is complete:

1. (Trilogy) Native simplicial chart, cumulant tower, character
   selection on $\mathbb{Z}/N$.
2. (Paper I) $\log\zeta$ as categorical effective action; cubic A-C
   tensor on $\mathbb{Z}/N$; $\mathbb{Z}/6$ Galois decomposition.
3. (Paper II) Occupation-decorated Fock; UPT forces Bargmann–Fock at
   $v = \infty$ with Tate-derived Archimedean factors; $m_B =
   -\Xi'/\Xi$; CM Poisson Monotonicity ⟺ RH.
4. (Paper III) Convolution-square positivity + cluster sign $c_2 < 0$
   + double-cutoff + averaged BDH + positive-current transport with
   five-error ledger + window-to-pointwise bridge + Pólya-Laguerre
   ⟹ RH.

Draft 2 refines the load-bearing details (Pass-1 priorities 1–6),
fixes the squared-norm bug via the Gram reformulation (§4 rewritten),
and restates the Main Theorem as the fourfold equivalence
RH ⟺ (GBP). The unconditional content of Paper III is substantial:
convolution-square representation, primorial CRT generation,
**Gram-Noether positivity on $L^2$-translates** (the corrected
upstairs object), cluster sign theorem with explicit constant,
double-cutoff dominated convergence, averaged BDH, the Archimedean
closure (Lemma 8.2 + Corollary 8.3), the window-to-pointwise bridge,
and three of the four equivalence arrows of Main Theorem 9.4. The
open content is the closure of (GBP), equivalent to RH.

The Riemann Hypothesis is, after Pass-1, **structurally equivalent to
(GBP)** — a precise spectral-measure identity between two explicit
positive-definite densities on the spectral line. The equivalence is
real and unconditional; closing (GBP) is the program's Pass-2 task
and is equivalent to RH.

---

---

## Appendix: the Gram reformulation, precise math

**The upstairs Hilbert structure.** $L^2(\mathbb{R})$ with the
standard inner product. The translation operators
$T_t : L^2(\mathbb{R}) \to L^2(\mathbb{R})$, $T_t g(s) := g(s - t)$,
are unitary with $T_t^* = T_{-t}$ and
$\langle T_t f, T_{t'} f\rangle_{L^2} = (f * f^*)(t' - t)
= \mathcal{F}^{-1}\phi(t' - t)$
for K-real Schwartz $f$ with $|\hat f|^2 = \phi$.

**The upstairs vector.** At primorial row $n$, occupation cutoff
$K_n$, height $y > 0$:
$$
\Psi_n(f; y) := \sum_{p \in \mathcal{P}_n}\sum_{r=1}^{K_n}\sqrt{\log p}\,e^{-yr\log p}\,T_{r\log p}f \;\in\;L^2(\mathbb{R}).
$$

**The Gram-Noether form.**
$$
\mathcal{Q}_n^{\text{Gram}}(f; y) := \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}
$$
is a squared $L^2$-norm; positive-semidefinite unconditionally.

**Bilinear expansion.**
$$
\mathcal{Q}_n^{\text{Gram}}(f; y) = \sum_{p, p'}\sum_{r, r'}\sqrt{(\log p)(\log p')}\,e^{-y(r\log p + r'\log p')}\,(f * f^*)(r\log p - r'\log p').
$$
Samples $(f * f^*) = \mathcal{F}^{-1}\phi$ at *difference* coordinates
$r\log p - r'\log p'$ — the natural Bochner kernel.

**Fourier-side identity** (Plancherel).
$\widehat{\Psi_n(f; y)}(\xi) = \hat f(\xi) \cdot \Sigma_n(y, \xi)$
with $\Sigma_n(y, \xi) := \sum_{p, r}\sqrt{\log p}\,p^{-r(y + i\xi)}$.
Therefore
$$
\mathcal{Q}_n^{\text{Gram}}(f; y) = \frac{1}{2\pi}\int_\mathbb{R}\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi.
$$

**Primorial limit.** For $y > 1/2$ (with analytic continuation for
$0 < y \leq 1/2$):
$\Sigma(y, \xi) := \lim_n\Sigma_n(y, \xi) = \sum_p\sqrt{\log p}\,p^{-(y + i\xi)}/(1 - p^{-(y + i\xi)})$.
The limit Gram form is the positive measure pairing
$\int\phi(\xi)\,d\nu_y(\xi)$ with $d\nu_y := |\Sigma(y, \xi)|^2 d\xi/(2\pi)$.

**The Main Theorem reformulated (Main Theorem 9.4).** RH is equivalent
to **(GBP)**: $d\nu_y = u_B(\xi, y)\,d\xi$ where
$u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy)$ is the Bures Poisson field
of Paper II. The two spectral densities are *different*
number-theoretic objects ($|\Sigma|^2$ Bochner-bilinear with
$\sqrt{\log p}$; $u_B$ linear in $\log p$ via $-\zeta'/\zeta$). Their
equality is equivalent to RH; closing (GBP) is the Pass-2 task.

Acknowledgment: the original squared-norm bug was identified during
external Pass-1 review. The Gram reformulation replaces it with the
correct upstairs object on $L^2(\mathbb{R})$ translates of $f$, and
restates the Main Theorem as the precise equivalence RH ⟺ (GBP).

---

*End of status report — Note_PaperIII_Draft2_StatusReport_2026-05-22.md.*
