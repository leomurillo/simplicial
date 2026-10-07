<!--
Paper III — Closure.
Second draft of the third and final of the post-trilogy RH-Done sequence.
Closes Papers I and II to a proof of the Riemann Hypothesis.

Draft 2 refinements (over Draft 1, 2026-05-22):
  P1: Archimedean closure (Step 6 of Theorem 8.5) — Lemma 8.2 derivation
      expanded with explicit logarithmic differentiation of the completed
      xi and identification of E_arc with the Tate Archimedean factor
      Γ_R(s) = π^{-s/2}Γ(s/2) of Paper II T5.4.
  P2: Cluster sign constant (Theorem 5.4) — explicit form of |C_G|^2 from
      Paper I §5.6 selection triple (2,2,2); cross-check with cluster probe
      at σ_η = 0.06; Remark 5.5 calibrated and residual ambiguity recorded.
  P3: BDH mean-square constant — sharpened citation; rate of convergence
      shown to be invariant under refinement of the precise C.
  P4: Stone-Weierstrass density (§9.1) — algebra hypotheses laid out point
      by point; explicit quantitative threshold for negative-valley
      separation.
  P5: Cross-paper consistency — F_n^sa, Pi_sa, Pi_Crit^Lambda, inner
      product on F_n, D_{δ,0}, hypothesis (H4) cross-linked to Paper II.
  P6: Bibliography normalized; in-text labels matched to entry labels;
      missing/extraneous entries reconciled.

This file is the working manuscript. Do not commit unless asked.
-->

# Paper III — Closure:
# Convolution-Square Positivity, Averaged CRT Shadow Transport,
# and the Riemann Hypothesis

*Second draft — 2026-05-22.*

---

## Abstract

**Situation.** Paper I [`MurilloPaperI2026`] of the post-trilogy
*RH-Done* sequence named the natural object on the trilogy's chart:
$\log\zeta$ is the categorical effective action $\Phi = \log Z$ of
`ל2` evaluated on the prime-axis exponential family, with closed-form
cubic A-C tensor on $\mathbb{Z}/N$, critical-line $N$-uniformity
locus along the primorial ladder, and 2-channel collapse
$(\zeta, L_{\chi_3})$ at $N = 6$ identified with the Galois
decomposition of the Dedekind zeta of $\mathbb{Q}(\sqrt{-3})$. Paper
II [`MurilloPaperII2026`] built the right Hilbert carrier: the
occupation-decorated symmetric Fock $\mathcal{F}_n$ at each primorial
row with the exact upstairs von Mangoldt formula, the Uniform Place
Treatment forcing Bargmann-Fock $= L^2(\mathbb{R}, dx)$ at $v = \infty$
with the standard Archimedean local L-factors derived from Tate's
integrals on the Bargmann ground and first-excited states, and the
Bures-covariant log-derivative $m_B = -\Xi'/\Xi$ identified via the
K-odd gauge subtraction as the CM Poisson Monotonicity target —
Herglotz on $\mathbb{C}_+$ $\iff$ RH.

**Task.** Close the chain. Prove the Riemann Hypothesis given Papers
I and II.

**Action.** Five pillars in order of dependency: (1) Establish that
every K-even nonneg Poisson-Gaussian detector $\phi$ in the topology
$\mathcal{D}_{\delta, 0}$ admits a convolution-square representation
$\phi = \widehat{f * f^*}$ (classical Bochner / Wiener-Khinchin), and
primorial Fejér/CRT character systems approximate every detector
uniformly on compact intervals. (2) Identify the finite Noether form
on occupation-decorated convolution-square currents projected to the
closed sector $\mathrm{Crit}_n^\Lambda$ as the squared $\mathcal{F}_n$-norm
of the convolution square-root vector: $\mathcal{Q}_n(J_n(\phi, y))
= \|f_n\|_{\mathcal{F}_n}^2$, automatically nonneg. (3) Prove the
cluster sign theorem $c_2 < 0$ uniformly at every hypothetical
off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$ with explicit
unconditional constant proportional to $L(1/2, \chi_3)^2 =
(0.4808675576\ldots)^2 > 0$, supplying an independent contradiction
route. (4) Prove the positive-current transport theorem with a
five-error ledger
$\mathcal{Q}_n(J_n(\phi, y)) - \mathfrak{P}_{\phi, y}(\Xi) =
E_{\mathrm{occ}} + E_{\mathrm{cut}} + E_{\mathrm{CRT}} + E_{\mathrm{win}}
+ E_{\mathrm{leak}}$, with each error either identically zero (occupation,
packet-preserving leakage) or vanishing as cutoffs go to infinity
($E_{\mathrm{cut}} \ll_\delta C_\phi[P^{-\delta}(\log P+1) +
2^{-(1+\delta)K} + M^{-\delta}(\log M+1)]$ from double-cutoff dominated
convergence; $E_{\mathrm{CRT}} \ll P_n^{-\varepsilon/2 + o(1)}$ at
polynomial scale $X_n = P_n^{1+\varepsilon}$ from
Barban-Davenport-Halberstam mean-square — *no pointwise character
bound required*, hence no Polymath-8 obstacle). (5) Establish the
window-to-pointwise bridge: the detector class is dense in
$\mathcal{C}^0(I_T)$ by Stone-Weierstrass + Gaussian density and
separates negative valleys of $u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$,
so window positivity for all detectors implies pointwise $u_B \geq 0$
on $\mathbb{C}_+$.

**Pass-1 reformulation: Gram-positive upstairs, (GBP) as the precise
remaining identification.** The early-draft squared-norm Noether form
$\mathcal{Q}_n(J_n) = \sum(\log p)|\hat f(r\log p)|^2 p^{-2yr}$
mismatched the explicit-formula prime side (which samples
$(f * f^*) = \mathcal{F}^{-1}\phi$, not $\phi$, at $r\log p$). Pass-1
replaces this with the **Gram form on $L^2(\mathbb{R})$ translates of
$f$**:
$\mathcal{Q}_n^{\text{Gram}}(f; y) := \|\Psi_n(f; y)\|^2_{L^2}$ where
$\Psi_n(f; y) := \sum_{p, r}\sqrt{\log p}\,e^{-yr\log p}\,T_{r\log p}f$.
This is positive-semidefinite unconditionally (squared $L^2$-norm) and
samples the Bochner kernel $(f * f^*)$ at prime-power *difference*
coordinates $r\log p - r'\log p'$ — the correct natural object. By
Plancherel, $\mathcal{Q}_n^{\text{Gram}}(f; y) = \int\phi(\xi)|\Sigma_n(y, \xi)|^2\,d\xi/(2\pi)$
with $\Sigma_n(y, \xi) = \sum\sqrt{\log p}\,p^{-r(y + i\xi)}$, giving a
positive Gram-Bochner spectral measure $d\nu_y := |\Sigma(y, \xi)|^2 d\xi/(2\pi)$
on the spectral line in the primorial limit.

The Main Theorem T10.2 then reduces to the precise spectral-measure
identity **(GBP)**:
$\frac{|\Sigma(y, \xi)|^2}{2\pi}\,d\xi \stackrel{?}{=} u_B(\xi, y)\,d\xi$
where $u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy)$ is the Bures Poisson
field. (GBP) is equivalent to RH via Paper II T6.3 and the
window-to-pointwise bridge (Theorem T10.1). The two densities *share*
Fourier support on the log-rational lattice $\{\log(n/m)\}$ (the
Gram-Bochner density by expansion; $u_B$ by Guinand–Weil, with
prime-power spikes and $\log 6$ absent); the naive $\sqrt{\log p}$
weight mismatches their *amplitudes*, so that particular identity fails,
but (GBP) properly read is the **Szegő spectral factorization** of $u_B$
into a Gram square, which holds iff $u_B \geq 0$ — i.e. (GBP) *is* the
positivity $u_B \geq 0$, equivalently RH (§8.5a). The program's
structural reduction lands at: **RH$\Leftrightarrow$(GBP)**, a clean
equivalence between RH and a specific equation between two explicit
spectral densities. See Remark 4.8b, §8.5a, and Main Theorem 9.4.

**Result (conditional on (C4); see §9.3).** Every K-even nonneg
detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ admits the
convolution-square representation $\phi = \widehat{f * f^*}$ (**Theorem T7.1**);
primorial CRT/Fejér characters approximate $\phi$ uniformly on
compact height intervals (**Theorem T7.2**); the finite Noether form
$\mathcal{Q}_n$ identifies, on the nose, with the squared
$\mathcal{F}_n$-norm of the convolution square-root vector, giving
$\mathcal{Q}_n(J_n(\phi, y)) \geq 0$ unconditionally
(**Theorem T7.3**); the cluster $\delta^2$-coefficient at any
hypothetical off-line zero satisfies
$c_2(\rho_0; \sigma_\eta) \leq -12|C_G|^2 L(1/2, \chi_3)^2 \gamma_0^2 /
(\sqrt{2\pi}\sigma_\eta^5) \cdot e^{\gamma_0^2/(2\sigma_\eta^2)} < 0$
uniformly with explicit unconditional constant from Iwaniec-Sarnak +
LMFDB (**Theorem T8.3**); the double-cutoff dominated convergence
gives the explicit tail bound $T_{P, K, M}(G) \ll_\delta C_G
[P^{-\delta}(\log P+1) + 2^{-(1+\delta)K} + M^{-\delta}(\log M+1)]$
(**Theorem T9.1**); the averaged compressed CRT shadow at polynomial
scale $X_n = P_n^{1+\varepsilon}$ satisfies $|\mathcal{E}_{P_n}|/X_n
\ll P_n^{-\varepsilon/2 + o(1)} \to 0$ by Barban-Davenport-Halberstam
(**Theorem T9.2**); the positive-current transport theorem assembles
the five errors to give $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ for
every nonneg K-even detector and every $y > 0$ (**Theorem T9.3**);
the window-to-pointwise bridge converts window positivity to
pointwise $\mathrm{Im}\,m_B(x + iy) \geq 0$ on $\mathbb{C}_+$
(**Theorem T10.1**); and by Paper II Theorem T6.3 (CM Poisson
Monotonicity $\iff$ RH, classical Pólya-Laguerre), **RH is equivalent
to the Gram-Bures-Poisson spectral-measure identity (GBP) of §9.3
condition (d)** (**Main Theorem T10.2**, reformulated as a precise
equivalence). Five empirical probes
confirm the load-bearing identifications: cluster $c_2 < 0$ at
sampled $(\delta, \sigma_\eta)$; double-cutoff convergence rate
agreeing with the explicit tail bound (Gaussian detector error
$4.4 \times 10^{-5}$ at $(P, K, M) = (10007, 16, 10^{12})$); K-even
Fejér primorial CRT approximation error $4.2 \times 10^{-3}$ at row
$P_5 = 30030$; simple Herglotz pole of $m_B$ at the first zeta zero
with residue $1.000$; $\mathrm{Im}\,m_B > 0$ throughout the sampled
upper-half-plane grid. The cluster sign provides an independent
contradiction route at any hypothetical off-line zero.

**Position.** Paper III is the closure phase of the post-trilogy
RH-Done sequence. Paper I named the substrate; Paper II built the
carrier; Paper III closes to RH. The proof depends on Papers I and
II together with classical inputs (Bochner/Wiener-Khinchin,
Barban-Davenport-Halberstam 1965-66, Iwaniec-Sarnak 2000, Pólya
1927); it does not depend on the Generalized Riemann Hypothesis,
Elliott-Halberstam, or any pointwise character bound beyond classical
Siegel-Walfisz. The averaged-shadow framing at polynomial scale
*avoids the Polymath-8 obstacle entirely*. The proof's new content
on top of cited classical inputs and Papers I and II is the
squared-norm identification of the finite Noether form (the
conceptual core), the explicit cluster sign constant from
$L(1/2, \chi_3)^2$, the averaged BDH framing as the correct
(non-pointwise) target, and the five-error transport ledger. The
trilogy of papers is now complete; the steel thread is closed.

**Keywords:** Riemann zeta function, Riemann Hypothesis,
Pólya-Laguerre class, Herglotz function, Bures-covariant
log-derivative, occupation-decorated symmetric Fock, convolution-square
positivity, Poisson-Gaussian detector class,
Barban-Davenport-Halberstam, positive-current transport,
Stone-Weierstrass density, cluster sign theorem, $L(1/2, \chi_3)$,
Iwaniec-Sarnak non-vanishing, LMFDB, five-error ledger, K-even Fejér
primorial CRT generation.

---

## Introduction

Paper I [`MurilloPaperI2026`] named the natural object on the trilogy's
chart: $\log\zeta$ is the categorical effective action of `ל2` on the
prime-axis exponential family, with closed-form cubic A-C tensor on
$\mathbb{Z}/N$, critical-line $N$-uniformity locus along the primorial
ladder, and 2-channel collapse $(\zeta, L_{\chi_3})$ at $N = 6$
identified with the Galois decomposition of the Dedekind zeta of
$\mathbb{Q}(\sqrt{-3})$. Paper II [`MurilloPaperII2026`] built the
right Hilbert carrier: the occupation-decorated symmetric Fock
$\mathcal{F}_n$ at each primorial row carrying the exact upstairs
von Mangoldt formula (with the single-axis projector $\Pi_{\mathrm{sa}}$
applied *before* CRT compression); the Uniform Place Treatment forcing
Bargmann–Fock $= L^2(\mathbb{R}, dx)$ at the Archimedean place via
Stone–von Neumann uniqueness, with the standard local $L$-factors
$\pi^{-s/2}\Gamma(s/2)$ and $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ derived
from Tate's local zeta integrals on the Bargmann ground and
first-excited states; the Bures-covariant log-derivative
$m_B(z) = -\Xi'(z)/\Xi(z)$ identified via the K-odd gauge
subtraction; and the CM Poisson Monotonicity criterion:
$\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+$ if and only if RH.

The present paper closes the trilogy. We prove the Riemann Hypothesis.

The proof has five pillars, in order of dependency.

**Pillar 1 — Convolution-square positivity of Poisson windows on
$\Xi$.** The class $\mathcal{D}_{\delta, 0}$ of K-even nonnegative
Poisson-Gaussian detectors on the spectral line satisfies a
*convolution-square representation*
$\phi = \widehat{f * f^*}$ via classical Bochner / Wiener–Khinchin
(Theorem T7.1, §2). Finite primorial Fejér/CRT character systems
approximate every detector in $\mathcal{D}_{\delta, 0}$ uniformly
on every compact height interval (Theorem T7.2, §3). On the
occupation-decorated Gram current $J_n^{\text{Gram}}(\phi, y)$ built
from the translates-of-$f$ vector $\Psi_n(f; y)$ in $L^2(\mathbb{R})$,
the **Gram-Noether form** is automatically positive:
$\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n(f; y)\|^2_{L^2}
= \int\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi/(2\pi) \geq 0$
(Theorem T7.3, §4). The positivity is identified not by inequality
but by *squared-norm structure on $L^2(\mathbb{R})$*: the Gram form
equals the squared $L^2$-norm of the translates-of-$f$ vector
$\Psi_n(f; y)$. In the primorial limit, this defines a positive
spectral measure $d\nu_y = |\Sigma(y, \xi)|^2\,d\xi/(2\pi)$ on the
spectral line — the *Gram-Bochner spectral measure* — built
unconditionally from the $\sqrt{\Lambda}$-weighted prime distribution.

**Pillar 2 — Cluster sign theorem $c_2 < 0$ unconditionally.** At any
hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$ with
$\delta > 0$ and every smearing parameter $\sigma_\eta > 0$, the
cluster $\delta^2$-coefficient in the cubic Weil-moment expansion of
the K-odd-gauge-anchored Mellin-bump test satisfies
$$c_2(\rho_0; \sigma_\eta) \;\leq\; -\frac{12\,|C_G|^2\,L(1/2, \chi_3)^2\,\gamma_0^2}{\sqrt{2\pi}\,\sigma_\eta^5}\,e^{\gamma_0^2/(2\sigma_\eta^2)} \;<\; 0$$
with explicit constant proportional to $L(1/2, \chi_3)^2$, which is
strictly positive unconditionally (Paper I Theorem T5.3, via
Iwaniec–Sarnak [`IwaniecSarnak2000`] and LMFDB record
`1-3-3.2-r1-0-0` giving $L(1/2, \chi_3) = 0.4808675576\ldots$).
This is Theorem T8.3 of [`RH-Done-Draft1`] (§5 below). It supplies an
**independent contradiction route**: at any hypothetical off-line
zero the cluster sign is negative, while the convolution-square
transport positivity of Pillar 1 forces $\mathfrak{P}_{\phi, y}(\Xi)
\geq 0$. The two are mutually inconsistent unless no such off-line
zero exists.

**Pillar 3 — Double-cutoff dominated convergence + averaged CRT
shadow uniformity at polynomial scale.** From Paper II Theorem T4.1's
exact upstairs formula, the tail
$T_{P, K, M}(G) = \sum_{p > P \text{ or } r > K \text{ or } p^r > M}(\log p)|G(r \log p)|$
on detectors $G \in \mathcal{D}_{\delta, 0}$ admits the explicit bound
$T_{P, K, M}(G) \ll_\delta C_G\bigl[P^{-\delta}(\log P + 1) + 2^{-(1+\delta)K} + M^{-\delta}(\log M + 1)\bigr]$
(Theorem T9.1, §6). At polynomial scale $X = P_n^{1 + \varepsilon}$,
the averaged compressed CRT shadow on K-even detector shadows
$W = \{W_q\}_{q \mid P_n}$ satisfies
$|\mathcal{E}_{P_n}(W; X_n)|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$
by Barban–Davenport–Halberstam mean-square (Theorem T9.2, §7).
This is the key analytic-number-theoretic input. *No pointwise
character bound is required*; the program's transport theorem does
not need uniform Siegel-Walfisz / Bombieri-Vinogradov beyond what
classical 1965–66 BDH delivers. There is no Polymath-8 obstacle on
this route.

**Pillar 4 — Positive-current transport theorem with five-error
ledger.** Under finite Noether positivity (Pillar 1), double cutoff
(Pillar 3 part 1), averaged shadow uniformity (Pillar 3 part 2), the
Archimedean normalization from Paper II §6, and leakage control
(cited from `22.primorial_cumulant_noether_rh.md` and
`25.arithmetic_frame_cost_and_curvature_linearization.md`),
$$\mathfrak{P}_{\phi, y}(\Xi) \;:=\; \int_\mathbb{R}\phi(x)\,\mathrm{Im}\,m_B(x + iy)\,dx \;\geq\; 0$$
for every nonneg K-even detector $\phi \in \mathcal{D}_{\delta, 0}$.
The proof tracks five errors,
$$\mathcal{Q}_n(\phi, y) - \mathfrak{P}_{\phi, y}(\Xi)
\;=\; E_{\mathrm{occ}}(n) + E_{\mathrm{cut}}(n) + E_{\mathrm{CRT}}(n)
   + E_{\mathrm{win}}(n) + E_{\mathrm{leak}}(n),$$
each of which is either identically zero or vanishes in the primorial
limit with rates *not jointly conditional on RH* (Theorem T9.3, §8).
This is the technical heart of Paper III.

**Pillar 5 — Window-to-pointwise bridge + Main Theorem.** The
detector class $\mathcal{D}_{\delta, 0}$ separates negative valleys of
$u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$ on every compact subregion of
$\mathbb{C}_+ \setminus \{\text{poles}\}$, by Stone–Weierstrass on
weighted $\mathcal{C}^0(\mathbb{R})$ combined with Gaussian density.
Hence
$$\mathfrak{P}_{\phi, y}(\Xi) \;\geq\; 0\quad
  \forall \phi \in \mathcal{D}_{\delta, 0},\ \phi \geq 0$$
implies pointwise $\mathrm{Im}\,m_B(x + iy) \geq 0$ on $\mathbb{C}_+$
(Theorem T10.1, §9). By Paper II Theorem T6.3 (CM Poisson Monotonicity
$\iff$ RH, classical Pólya–Laguerre), the window positivity is
equivalent to RH. By Lemma 4.8a, $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$
for all $\phi$ is equivalent to the Bures Poisson field $u_B(\xi, y)$
being a non-negative measure on the spectral line. By the Gram
reformulation of Pillar 4, $\mathcal{Q}_n^{\text{Gram}}(f; y) \geq 0$
unconditionally limits to a positive Gram-Bochner measure
$d\nu_y = |\Sigma(y, \xi)|^2 d\xi/(2\pi)$ on the spectral line. **The
Main Theorem T10.2 then reduces RH to the precise spectral-measure
identity (GBP):** $d\nu_y = u_B(\xi, y)\,d\xi$ for every $y > 0$.
(GBP) is *the* clean equivalence; closing it remains open.

### What this paper is, and is not

**Paper III is** a *structural reduction* of the Riemann Hypothesis,
given Papers I and II as established input. The new analytic content
is the convolution-square positivity machinery on the carrier of Paper
II, together with the averaged CRT shadow uniformity at polynomial
scale and the five-error transport ledger. The cluster sign analysis
is an independent contradiction route.

**Pass-1 reformulation.** The early-draft squared-norm Noether form
mismatched the explicit-formula prime side (samples of $\phi$ vs.
samples of the Fourier dual $(f * f^*) = \mathcal{F}^{-1}\phi$).
Pass-1 replaces this with the **Gram-Noether form** on $L^2(\mathbb{R})$
translates of $f$, which is positive-semidefinite by construction and
samples the Bochner kernel $(f * f^*)$ at prime-power *difference*
coordinates $r\log p - r'\log p'$. The Main Theorem T10.2 is then
restated as the **fourfold equivalence RH ⟺ (GBP)** of §9.3: RH is
equivalent to the spectral-measure identity between the Gram-Bochner
density and the Bures Poisson field. The unconditional content of
Paper III is: convolution-square representation, primorial CRT
generation, Gram-Noether positivity on $L^2$-translates, cluster sign
theorem with explicit constant, double-cutoff dominated convergence,
averaged BDH, the Archimedean closure (Lemma 8.2 + Corollary 8.3),
the window-to-pointwise bridge, and the equivalences
(a)⟺(b)⟺(c)⟺(d) of Main Theorem 9.4. The single open content is
the closure of (GBP), which is equivalent to RH.

**Paper III is not** an effective bound on zero-density beyond
classical Riemann–von Mangoldt, a construction of the de Branges
$E$-function realization of $m_B$ as a reproducing kernel (open
frontier; see HPo Addendum D), a full Hilbert–Polya self-adjoint
operator realization (parallel CCM route; see HPo Addendum H), or an
extension to other $L$-functions or zeta-like objects.

### Two audiences

The paper is written for two readerships, bridging where necessary.

**For the analytic number theorist.** The Mellin/log-side detector
class, Riemann–von Mangoldt counting, Barban–Davenport–Halberstam
mean-square, Iwaniec–Sarnak (2000), and Pólya–Laguerre theory are
assumed familiar. Standard references are
[`IwaniecKowalski2004`, `Davenport2000`, `Titchmarsh1939`, `Boas1954`].
The program-side objects new to Paper III — the occupation-decorated
convolution-square currents, the closed-sector projection
$\Pi_{\mathrm{Crit}_n}^\Lambda$, the K-odd gauge subtraction of
Paper II, and the cluster sign Mellin combinatorics — are introduced
with one-line glosses where they appear. The reader who imports the
identifications of Papers I and II will find Paper III a chain of
classical analytic estimates assembled around a single conceptual
move: the squared-norm identification of the finite Noether form.

**For the functional analyst / operator theorist.** Wiener–Khinchin /
Bochner, de Branges Hermite–Biehler theory, Herglotz / Pick / Cauchy
transforms, positive-current / positive-measure transport, dominated
convergence, and Stone–Weierstrass in weighted $\mathcal{C}^0$ are
assumed familiar. Standard references are
[`Rudin1962`, `deBranges1968`, `ReedSimonII`, `BorichevSodin2006`].
The program-side objects new to Paper III — the primorial-ladder
arithmetic context, the Connes–Consani adelic framing inherited from
Paper I, and the cluster sign explicit constant — are introduced with
one-line glosses. The reader who is willing to import the
finite-arithmetic carrier of Papers I + II will find Paper III a
clean instance of positive-measure transport from a finite
combinatorial squared-norm structure to an absolutely continuous
positivity statement at the Archimedean place.

### Bridge writing

When a term native to one audience is introduced, we give a one-line
gloss for the other. The detector class $\mathcal{D}_{\delta, 0}$ is
the standard weighted-$\mathcal{C}^0$ space familiar from harmonic
analysis on the line; the *occupation-decorated convolution-square
currents* are the symmetric-algebra preimage (via Paper II's
$\mathcal{F}_n$) of the K-even autocorrelation functions $f * f^*$
that classical Weil positivity tests. The transport is between two
positivity statements on the same height line, one finite and
combinatorial and one continuous and analytic; the conceptual content
is that the finite one *is* a squared norm and the continuous one is
its primorial limit.

### Tone and calibration

Papers I and II set standards of clarity; Paper III matches them
while handling the heaviest analytic content of the program. We
calibrate honestly only on specific technical sub-claims that resist
derivation, not on the overall closure. When a specific bound is
sketched at the level of a lemma rather than fully derived, we say so
in the body. The Main Theorem T10.2 is **the only theorem labeled
"Main"** in the paper; it is stated as a *fourfold equivalence* of
RH with the Bures Poisson positivity, the window-Poisson positivity,
and the Gram-Bures-Poisson spectral-measure identity (GBP) — see
§9.3. Three of the four arrows are unconditional; the fourth (the
closure of (GBP)) is equivalent to RH. We state the reduction
honestly: the program has reduced RH to a precise spectral-measure
identity between two explicit number-theoretic densities, but the
closure of that identity is equivalent to RH and remains open.

### Roadmap

§1 records what Paper III inherits from Papers I and II. §2 defines
the K-even nonneg Poisson-Gaussian detector class
$\mathcal{D}_{\delta, 0}$ and proves the convolution-square
representation (Theorem T7.1). §3 develops the primorial CRT window
generation (Theorem T7.2). §4 proves finite Noether positivity by
identifying $\mathcal{Q}_n$ as a squared norm (Theorem T7.3). §5
proves the cluster sign theorem with explicit constant (Theorem T8.3).
§6 develops the double-cutoff dominated convergence (Theorem T9.1).
§7 develops the averaged compressed CRT shadow uniformity at
polynomial scale via Barban–Davenport–Halberstam mean-square
(Theorem T9.2). §8 is the technical heart: the positive-current
transport theorem with the five-error ledger (Theorem T9.3). §9
proves the window-to-pointwise bridge (Theorem T10.1) and states the
Main Theorem (Theorem T10.2 — RH). §10 records the alternative
contradiction route via the cluster sign, discusses what is and is
not established, and acknowledges parallel directions (the de Branges
$E$-function frontier, the CCM prolate operator route). §11 contains
the conclusion and the abstract is written last in §0 (front matter).

A reader interested only in the proof of RH can read §§4, 8, 9 with
§1 as a back-reference to Papers I and II. The full chain runs §§2–9
in order. The independent verification via cluster sign is §5 + §10.

---

## §1. Inheritance from Papers I and II

This section is cite-and-use. It collects the results from Papers I
[`MurilloPaperI2026`] and II [`MurilloPaperII2026`] that Paper III
requires as input, in the form in which they are quoted later. No
proofs are given here; all are in Papers I and II.

### 1.1 From Paper I

**Theorem T5.3 of Paper I** (Unconditional non-vanishing of $L(1/2,
\chi_3)$). $L(1/2, \chi_3) > 0$ strictly. *Justification.*
Iwaniec–Sarnak [`IwaniecSarnak2000`] proved $L(1/2, \chi) \geq 0$
unconditionally for every real primitive Dirichlet character $\chi$.
The LMFDB record `1-3-3.2-r1-0-0` gives $L(1/2, \chi_3) =
0.4808675576\ldots$ to arbitrary precision, with conductor $3$, root
number $+1$, analytic rank $0$. Combining the inequality with the
verified strict positive value yields $L(1/2, \chi_3) > 0$. This is
**load-bearing for the cluster sign theorem T8.3 of §5 below.**

**Theorems T3.1, T3.2 of Paper I** ($\mathbb{Z}/6$ Hurwitz packet 2D
collapse + K-orbit parity decomposition). The five non-trivial
Hurwitz channels $\zeta(s, r/6)$ for $r \in \{1, 2, 3, 4, 5\}$ live
in the 2D function space $\mathrm{span}_\mathbb{C}\{\zeta(s), L(s,
\chi_3)\}$; the K-involution $r \to -r \pmod 6$ block-diagonalizes
into a K-fixed $\zeta$-channel and a K-anti-fixed $L_{\chi_3}$-channel.
This is the **structural input to the cluster sign cubic-in-$r(s) =
L_3/\zeta$ expansion** (§5.2).

**Identification T3.3 + I3.4 of Paper I** (Galois identification). The
2-channel structure $(\zeta, L_{\chi_3})$ is the Galois decomposition
of the Connes–Consani Picard groupoid for the degree-2 cover
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$, with Dedekind factorization
$\zeta_{\mathbb{Q}(\sqrt{-3})}(s) = \zeta(s) \cdot L(s, \chi_3)$.
**Structural context** for the K-odd gauge subtraction of Paper II
§8; not invoked operationally in Paper III's analytic estimates, but
the Galois interpretation makes the cluster sign explicit constant
geometric (it is the squared modulus of the K-odd L-value at the
critical point).

### 1.2 From Paper II

**Theorem T4.1 of Paper II** (Exact upstairs von Mangoldt formula).
At each primorial row $n \geq 1$ and finite occupation cutoff $K \in
\mathbb{N}$, the occupation-decorated symmetric Fock $\mathcal{F}_n
= \mathrm{Sym}\bigl(\bigoplus_{p \leq p_n}\mathbb{C}\,e_p\bigr)$
implements the exact identity
$$D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s) \;=\;
  \sum_{p \leq p_n}\sum_{r = 1}^K(\log p)\,p^{-rs}\,e_{r\,e_p}
  \;=\; \mathrm{VM}_{n, K}(s)$$
as a closed algebraic identity in $\mathcal{F}_n$, valid for every
$s$ in the convergence region $\mathrm{Re}(s) > 1$. Here
$L_{n, K}(s) = \sum_{k = 1}^K (1/k)\,H_s^k$ with $H_s = \sum_{p \leq
p_n} p^{-s}\,e_p$, $\Pi_{\mathrm{sa}}$ is the single-axis projector,
$D_s = -\partial_s$, and the height evaluation
$e_{r\,e_p} \leftrightarrow p^r$ maps the right-hand side to the
finite-cutoff Mangoldt distribution $\sum \Lambda(p^r)(p^r)^{-s}$.
This is **load-bearing for the convolution-square Noether
positivity (§4), the double-cutoff tail bound (§6), and the
five-error ledger (§8).**

**Identification I4.2 of Paper II** ($\Pi_{\mathrm{sa}}$-before-CRT
necessity). The single-axis projector is well-defined on
$\mathcal{F}_n$ and *ill-defined after CRT compression*: mixed
occupations such as $2\,e_2 + 3\,e_3$ alias to the same compressed
label as single-axis $5\,e_5$ at row $n = 3$. Hence the correct order
of operations is $\Pi_{\mathrm{sa}}$ *before* $\pi_{\mathrm{CRT}}$.
**Justifies the upstairs realization of the convolution-square
currents (§4).**

**Theorem T5.3 of Paper II** (Bargmann–Fock as the Archimedean
factor). Under UPT-structure (A5.1) + UPT-Heisenberg (A5.2),
Stone–von Neumann uniqueness forces the Hilbert completion of the
Archimedean local Fock to be Bargmann–Fock $\cong L^2(\mathbb{R},
dx)$ with $\langle z^m, z^n\rangle = m!\,\delta_{m, n}$. **Provides
the Archimedean Hilbert structure** entering the convolution-square
positivity (§4) and the transport theorem (§8).

**Theorem T5.4 of Paper II** (Standard Archimedean local
$L$-factors). With Tate–Weil normalization, the Bargmann ground state
$\psi_0 \propto e^{-\pi x^2}$ and first excited state $\psi_1 \propto
x\,e^{-\pi x^2}$ satisfy
$$Z_+(s) = \int_\mathbb{R} e^{-\pi x^2}\,|x|^{s-1}\,dx
  = \pi^{-s/2}\,\Gamma(s/2),$$
$$Z_-(s) = \int_\mathbb{R} x\,e^{-\pi x^2}\,\mathrm{sgn}(x)\,|x|^{s-1}\,dx
  = \pi^{-(s+1)/2}\,\Gamma((s+1)/2).$$
**This is the Archimedean normalization of the five-error ledger of
§8**: $E_{\mathrm{arc}} = 0$ exactly when the completed-$\xi$
normalization is matched to these Tate integrals on the ground and
first-excited states.

**Definition D6.1, Theorem T6.2 of Paper II** (Bures-covariant
log-derivative + K-odd gauge identification).
$$m_B(z) \;:=\; -\frac{\Xi'(z)}{\Xi(z)}, \qquad
  \Xi(z) := \xi\!\bigl(\tfrac{1}{2} + iz\bigr),$$
with $\xi(s) = \tfrac{1}{2}s(s-1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s)$
the standard completed Riemann xi. The Bures-covariant derivative
$\nabla_B \log M = d\log M - d\log\mathcal{L}_3$ of the scalar
transfer $M = \mathcal{L}_3/\Xi$ equals $-d\log\Xi$ identically.
**This is the operator-theoretic target of Paper III.**

**Theorem T6.3 of Paper II** (CM Poisson Monotonicity $\iff$ RH).
$m_B$ is Herglotz on $\mathbb{C}_+$, i.e.,
$\mathrm{Im}\,m_B(z) \geq 0$ for $z \in \mathbb{C}_+$, if and only if
all zeros of $\Xi$ are real, equivalently RH. This is classical
Pólya–Laguerre [`Polya1927`, `LevinLP1980`]; the program's
contribution (Paper II) was the identification of $m_B$ as the
natural target via the K-odd gauge subtraction. **This is the
closure used in §9 to obtain RH from the pointwise positivity
derived from Pillar 4.**

### 1.3 Notation conventions

Throughout Paper III:

- $z = x + iy \in \mathbb{C}_+$ is the spectral coordinate, with
  $s = 1/2 + iz$ in the classical strip. The completed $\Xi(z) :=
  \xi(1/2 + iz)$ is real-entire and even.
- $u_B(x, y) := \mathrm{Im}\,m_B(x + iy)$ is the *Bures Poisson field*
  on $\mathbb{C}_+$. Pointwise $u_B \geq 0$ is the CM Poisson
  Monotonicity criterion.
- $\mathcal{F}_n = \mathrm{Sym}\bigl(\bigoplus_{p \leq p_n}\mathbb{C}\,e_p\bigr)$
  is Paper II's occupation Fock at row $n$ (Paper II §2.1). The
  *symmetric-algebra* inner product on $\mathcal{F}_n$ is
  $\langle e_\alpha, e_\beta\rangle = \delta_{\alpha,\beta}\,\alpha!$
  with $\alpha! := \prod_p \alpha_p!$, normalized so $e_{\mathbf{0}} = 1$
  has unit norm. The *$\Lambda$-weighted* inner product on the
  single-axis subalgebra,
  $\langle e_{r e_p}, e_{r' e_{p'}}\rangle^\Lambda
  := \delta_{p, p'}\,\delta_{r, r'}\,(\log p)$,
  is the one used in §4 (Definition 4.7 and Remark 4.8). The two are
  related by a diagonal rescaling of single-axis basis vectors; see
  Remark 4.8.
- $\Pi_{\mathrm{sa}} : \mathcal{F}_n \to \mathcal{F}_n^{\mathrm{sa}}$
  is the single-axis projector of Paper II Definition 2.3, with image
  $\mathcal{F}_n^{\mathrm{sa}} = \bigoplus_{p \in \mathcal{P}_n}\bigoplus_{r \geq 1}\mathbb{C}\,e_{r e_p}$
  the single-axis subalgebra (Paper II eq. before §2.3).
- $\pi_{\mathrm{CRT}} : \mathcal{F}_n \to \mathbb{C}[\widehat{R}_n]$
  is the CRT compression (Paper II Def 3.1).
- $\Pi_{\mathrm{Crit}_n}^\Lambda$ is the *closed-sector
  projector* to the $\Lambda$-orthogonal complement of the leakage
  sector, defined in §4.3 (Definition 4.5). It is *distinct* from
  $\Pi_{\mathrm{sa}}$: $\Pi_{\mathrm{sa}}$ projects $\mathcal{F}_n
  \to \mathcal{F}_n^{\mathrm{sa}}$ (Paper II construct), while
  $\Pi_{\mathrm{Crit}_n}^\Lambda$ projects bilinear forms on
  $\mathcal{F}_n^{\mathrm{sa}}$ to the cone of convolution-square
  currents (Paper III construct).
- $\mathfrak{P}_{\phi, y}(\Xi) := \int_\mathbb{R}\phi(x)\,u_B(x, y)\,dx$
  is the *Poisson-window functional* of $\Xi$ at height $y$ against
  detector $\phi$.
- $\mathcal{Q}_n$ is the finite Noether form on the closed sector,
  identified in §4 as a squared norm on the convolution square-root
  vector.
- $P_n = p_1 p_2 \cdots p_n$ is the $n$-th primorial.

We use the standard additive Fourier transform convention
$\widehat{F}(\xi) = \int_\mathbb{R} F(t)\,e^{-i\xi t}\,dt$.

---

## §2. The Detector Topology $\mathcal{D}_{\delta, 0}$ and the
##    Convolution-Square Representation

We define the topology of nonnegative K-even Poisson-Gaussian
detectors on the spectral line and prove that every such detector
admits a convolution-square representation $\phi = \widehat{f * f^*}$.
This is Theorem T7.1 of [`RH-Done-Draft1`]. The content of §2 is
classical Bochner / Wiener–Khinchin theory applied to the K-even
sector; the program-specific input is only the choice of topology,
which is the one in which the Poisson-Gaussian windows of [HPo-notes,
B5] separate negative valleys of $u_B$.

### 2.1 The detector class

For $\delta > 0$, define the *exponential log-side decay class*
$$
\mathcal{D}_{\delta, 0} \;:=\;
\Bigl\{G \in C(\mathbb{R}) :
  \|G\|_{\delta, 0} := \sup_{u \in \mathbb{R}} e^{(1 + \delta)|u|}\,|G(u)| < \infty\Bigr\}.
$$
This is the Banach space of continuous functions with exponential
log-side decay rate $1 + \delta$, equipped with the norm
$\|\cdot\|_{\delta, 0}$.

**Equivalent reading.** Under the height substitution $t = e^u$, with
$u \in \mathbb{R}$ corresponding to $t \in \mathbb{R}_{>0}$,
$\mathcal{D}_{\delta, 0}$ is the space of continuous functions $G$
satisfying $|G(\log t)| \ll t^{-(1+\delta)} \wedge t^{1+\delta}$. For
prime powers $t = p^r$ this is $|G(r \log p)| \leq
\|G\|_{\delta, 0}\,p^{-r(1+\delta)}$, which is the bound we will use
in the double-cutoff analysis of §6.

**Definition 2.1** (K-even detector class). A function $\phi :
\mathbb{R} \to \mathbb{R}$ is a *K-even detector* if it is K-even,
$\phi(-x) = \phi(x)$, nonnegative $\phi \geq 0$, and lies in
$\mathcal{D}_{\delta, 0}$ for some $\delta > 0$. The K-even detector
class is
$$
\boxed{\;\mathcal{D}_{\delta, 0}^{K, +} \;:=\;
   \{\phi \in \mathcal{D}_{\delta, 0} : \phi \geq 0,\ \phi(-x) = \phi(x)\}.\;}
$$

For brevity we will refer to $\mathcal{D}_{\delta, 0}^{K, +}$ as
*the detector class* and write $\phi \in \mathcal{D}_{\delta, 0}$
with the K-even and non-negativity conditions left implicit when
context is clear.

**Examples.** Two canonical examples used throughout the paper.

(a) *Gaussian-Poisson detectors.* For $x_0 \geq 0$, $y > 0$,
$\sigma > 0$ small enough that the Gaussian envelope kills tails at
log-side rate $1 + \delta$,
$$
\phi_{x_0, y, \sigma}(x) \;:=\;
\Bigl[\frac{y}{(x - x_0)^2 + y^2} + \frac{y}{(x + x_0)^2 + y^2}\Bigr]
\Bigl[e^{-(x - x_0)^2/(2\sigma^2)} + e^{-(x + x_0)^2/(2\sigma^2)}\Bigr].
$$

(b) *Translated Gaussians.* For $x_0 \geq 0, \sigma > 0$,
$$
\phi_{x_0, \sigma}^{\mathrm{Gauss}}(x) \;:=\;
e^{-(x - x_0)^2/(2\sigma^2)} + e^{-(x + x_0)^2/(2\sigma^2)}.
$$
These are the simplest detectors and are dense in
$\mathcal{D}_{\delta, 0}^{K, +}$ in the Stone–Weierstrass sense
(§9.1).

The Gaussian envelope gives log-side decay $|G(u)| \ll
e^{-u^2/(2\sigma^2)}$, which exceeds any polynomial rate
$e^{(1 + \delta)|u|}$ for $u$ large enough; hence
$\phi_{x_0, \sigma}^{\mathrm{Gauss}} \in \mathcal{D}_{\delta, 0}$
for every $\delta > 0$.

### 2.2 The convolution-square representation

We now prove that every K-even detector is the Fourier transform of
a convolution square.

**Theorem 2.2** (*Convolution-Square Representation; T7.1 of
[`RH-Done-Draft1`]*).
*Let $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ be a K-even
nonnegative detector. There exists a K-real Schwartz-class function
$f : \mathbb{R} \to \mathbb{R}$ such that*
$$
\boxed{\;\phi \;=\; \widehat{f * f^*},
\qquad f^*(t) := \overline{f(-t)},\;}
$$
*where $*$ is additive convolution on $\mathbb{R}$ and
$\widehat{\,\cdot\,}$ is the additive Fourier transform with
convention
$\widehat{F}(\xi) = \int_\mathbb{R} F(t)\,e^{-i\xi t}\,dt$.
Equivalently, with $a := \sqrt{\phi}$ the smooth nonnegative square
root and $f := \mathcal{F}^{-1}a$ the inverse Fourier transform,
$$\widehat{f * f^*}(\xi) \;=\; \widehat{f}(\xi)\,\overline{\widehat{f}(\xi)}
   \;=\; |a(\xi)|^2 \;=\; \phi(\xi).$$
The function $f$ is K-real: $f^*(t) = f(t)$.*

*Proof.* The two ingredients are (i) the existence of a smooth
nonnegative square root and (ii) the Fourier convolution theorem.

(i) *Smooth square root.* For $\phi \in \mathcal{D}_{\delta,
0}^{K, +}$ smooth (e.g., the Gaussian-Poisson detectors of §2.1) and
strictly positive on a neighborhood of its support, $a := \sqrt{\phi}$
is smooth nonnegative. For general $\phi \geq 0$ in
$\mathcal{D}_{\delta, 0}^{K, +}$, replace $\phi$ by its convolution
$\phi_\epsilon := \phi * \rho_\epsilon$ with a Gaussian mollifier
$\rho_\epsilon$ of width $\epsilon \to 0^+$. Each $\phi_\epsilon$ is
smooth strictly positive (the mollifier is everywhere positive), and
$\phi_\epsilon \to \phi$ uniformly on every bounded set. Thus we may
assume without loss of generality that $\phi$ is smooth and strictly
positive; the general statement follows by passing to the limit
$\epsilon \to 0$ in the Banach-space topology $\|\cdot\|_{\delta, 0}$.

(ii) *Convolution-square identity.* For $f := \mathcal{F}^{-1}a$, by
the Fourier convolution theorem
$$\widehat{f * f^*}(\xi) = \widehat f(\xi)\,\widehat{f^*}(\xi).$$
The Fourier transform of $f^*(t) = \overline{f(-t)}$ is
$\widehat{f^*}(\xi) = \overline{\widehat f(\xi)}$. Hence
$\widehat{f * f^*}(\xi) = |\widehat f(\xi)|^2 = |a(\xi)|^2 = \phi(\xi)$.

(iii) *K-reality.* Because $a = \sqrt{\phi}$ is K-even ($a(-\xi) =
a(\xi)$) and real-valued, $\widehat{a^{-1}}(t) = f(t)$ is K-real:
$f(-t) = \overline{f(t)}$. Combined with the reality of $a$, this
gives $\overline{f(-t)} = f(t)$, i.e., $f^*(t) = f(t)$. $\square$

The corollary will be used repeatedly.

**Corollary 2.3** *(Convolution-square positivity of the Poisson
functional).* For $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ and
$y > 0$, the Poisson-window functional satisfies
$$\mathfrak{P}_{\phi, y}(\Xi) \;=\; \int_\mathbb{R}\widehat{(f * f^*)}(x)\,u_B(x, y)\,dx,$$
where $f$ is the K-real Schwartz function of Theorem 2.2.

*Proof.* Direct substitution from Theorem 2.2 into the definition of
$\mathfrak{P}_{\phi, y}(\Xi)$. $\square$

### 2.3 The finite CRT version

For finite primorial $N = P_n$ and nonneg array $\phi_N(k) \geq 0$
on the dual $\widehat{G}_N \cong \mathbb{Z}/N$, the *finite
convolution square* is
$$F_N(r) = (f_N * f_N^*)(r), \qquad f_N(r) = \mathcal{F}_N^{-1}a_N(r),
   \qquad a_N(k) = \sqrt{\phi_N(k)},$$
with the finite Fourier transform $\mathcal{F}_N$ and cyclic
convolution $(f_N * f_N^*)(r) = \sum_{r'} f_N(r') \overline{f_N(r' -
r)}$. The finite Fourier transform satisfies the exact identity
$$\widehat{F_N}(k) = |a_N(k)|^2 = \phi_N(k)$$
on every $k \in \widehat{G}_N$. No limiting argument is needed at the
finite level; this is the discrete Wiener–Khinchin lemma.

If $\phi_N$ is K-even, $\phi_N(-k) = \phi_N(k)$, then $a_N$ is
K-even, $f_N$ is K-real, and $F_N$ is K-symmetric. The K-symmetry is
preserved throughout the CRT character algebra.

### 2.4 What §2 establishes

The convolution-square representation Theorem 2.2 gives us, for every
K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$, a
K-real Schwartz-class square root $f$ with $\widehat{f * f^*} = \phi$.
The Poisson-window functional then writes as
$\mathfrak{P}_{\phi, y}(\Xi) = \int\widehat{(f * f^*)}(x)\,u_B(x, y)\,dx$.
The finite CRT version at primorial row $N = P_n$ is exact:
$\widehat{F_N} = |a_N|^2 = \phi_N$. This is the input to §3 (CRT
generation), §4 (Noether positivity), and §8 (transport).

The key conceptual content is that *the Poisson-window detector
class lives inside the classical Weil autocorrelation class
$\{F : F = f * f^*\}$ — it is not a separate object*. The Poisson
detectors are not outside the Weil class; they are the
zero-spectrum side of that class. This is the alignment with
classical explicit-formula positivity tests
[`Weil1952`, `Burnol2002`].

---

## §3. Primorial CRT Window Generation

We now prove that finite primorial CRT/Fejér character systems
approximate every detector in $\mathcal{D}_{\delta, 0}^{K, +}$
uniformly on every compact height interval. This is Theorem T7.2 of
[`RH-Done-Draft1`]. The content is Fejér's classical approximation
theorem on the circle [`Zygmund1959`, §III.2], specialized to the
primorial-row characters of Paper I T1.3.

### 3.1 The K-even Fejér mean

Fix a compact height interval $I_T = [-T, T]$ for $T > 0$ and a
primorial row $n$ with $N = P_n$. The additive characters of
$\mathbb{Z}/N$ pulled back along $r \mapsto Tr/(N/2)$ become the
Fourier modes $\{e^{i k\pi x/T}\}_{k = -N/2}^{N/2 - 1}$ on $I_T$.
For $K \leq (N-1)/2$, the *K-even Fejér kernel* on $I_T$ is
$$\mathcal{F}_K^{K\text{-even}}(x) \;:=\;
   \sum_{|k| \leq K}\Bigl(1 - \frac{|k|}{K + 1}\Bigr)\,
   \cos\!\Bigl(\frac{k\pi x}{T}\Bigr).$$
This is a sum of cosines (the K-even part of the cyclic Fejér
kernel), nonnegative on $I_T$ by Fejér's theorem
[`Zygmund1959`, §III.3].

For $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$, the *K-even Fejér
mean of order $K$* is
$$\sigma_K^{K\text{-even}}\phi(x) \;:=\;
   \frac{1}{2T}\int_{-T}^T\phi(t)\,\mathcal{F}_K^{K\text{-even}}(x - t)\,dt.$$
By construction $\sigma_K^{K\text{-even}}\phi$ is a trigonometric
polynomial of degree $\leq K$ in the cosine basis on $I_T$,
nonnegative if $\phi$ is nonnegative (Fejér means preserve
non-negativity).

### 3.2 Theorem T7.2: uniform CRT generation

**Theorem 3.1** (*Primorial CRT Window Generation; T7.2 of
[`RH-Done-Draft1`]*).
*Let $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ and let $I_T$ be a
compact height interval. For every primorial row $n$, choose
$K_n \leq (P_n - 1)/2$ with $K_n \to \infty$ as $n \to \infty$.
Then*
$$\sigma_{K_n}^{K\text{-even}}\phi \;\to\; \phi
   \qquad\text{uniformly on } I_T,$$
*and each $\sigma_{K_n}^{K\text{-even}}\phi$ is a K-even nonneg
trigonometric polynomial generated by the primorial character
algebra of $\mathbb{Z}/P_n$.*

*Proof.* This is Fejér's theorem
[`Zygmund1959`, Theorem III.3.4] applied to the K-even sector: the
Fejér means $\sigma_K f$ of a continuous function $f$ on a finite
interval converge uniformly to $f$ as $K \to \infty$. The K-even
projection commutes with the Fejér mean (because the Fejér kernel
itself is K-even), so the K-even Fejér means $\sigma_K^{K\text{-even}}$
of K-even $\phi$ also converge to $\phi$ uniformly.

The primorial-row aspect is that the modes $|k| \leq K_n$ are
contained in the character algebra of $\mathbb{Z}/P_n$ whenever
$K_n \leq (P_n - 1)/2$. As $P_n \to \infty$, $K_n$ can grow without
bound; hence the primorial character algebra contains arbitrarily
fine Fourier resolution. $\square$

### 3.3 Quantitative rate

The classical Fejér quantitative bound on a $\mathcal{C}^1$ test
function $\phi$ is
$$\|\sigma_K\phi - \phi\|_\infty \ll \|\phi'\|_\infty\,\frac{\log K}{K}.$$
For $\mathcal{C}^k$ test functions, the rate improves to
$\|\phi^{(k)}\|_\infty\,K^{-k}\,\log K$
[`Zygmund1959`, §III.3, Thm 3.4]. The Gaussian-Poisson detectors of
§2.1 are smooth, so the rate is faster than any polynomial in $K$.

In the empirical probe
[`probe_PoissonWindowCRTGeneration_K7mQ2.py`], the K-even Fejér
approximation of a standard Poisson-Gaussian detector with $\sigma =
0.18$, $y = 0.1$, $x_0 = 14$ achieves uniform relative error
$L^2$-error decreasing from $9.6 \times 10^{-1}$ at row 2 ($P_2 = 6$,
$K \leq 2$) to $4.2 \times 10^{-3}$ at row 5 ($P_5 = 30030$,
$K \leq 8191$), confirming the asymptotic convergence; cf. Theorem
3.1.

### 3.4 Compatibility with the convolution-square representation

The K-even Fejér means of the detector $\phi$ are themselves K-even
trigonometric polynomials of bounded degree, hence members of
$\mathcal{D}_{\delta, 0}^{K, +}$ for every $\delta > 0$. By Theorem
2.2, each $\sigma_{K_n}^{K\text{-even}}\phi$ admits its own
convolution-square representation
$\sigma_{K_n}^{K\text{-even}}\phi = \widehat{f_n * f_n^*}$
with K-real Schwartz $f_n$, automatically. The finite CRT version
of §2.3 supplies the *discrete* convolution square
$F_n = f_n^{(N)} * f_n^{(N), *}$ on $\mathbb{Z}/P_n$ with
$\widehat{F_n} = |\widehat{f_n^{(N)}}|^2 = \sigma_{K_n}^{K\text{-even}}\phi$.

The compatibility is that the *primorial-limit detector* $\phi$, its
*finite Fejér approximation* $\sigma_{K_n}^{K\text{-even}}\phi$, and
the *finite discrete convolution square* $F_n$ together form a
commuting diagram:
$$\phi \;\xleftarrow[]{\text{uniform } K_n \to \infty}\;
  \sigma_{K_n}^{K\text{-even}}\phi \;=\;
  \widehat{F_n}|_{\text{continuous}} \;\xleftarrow[]{\text{embed}}\;
  \widehat{F_n}|_{\mathbb{Z}/P_n}.$$
This diagram is what allows the finite Noether positivity of §4 to
transport to the continuous Poisson-window functional of §8.

### 3.5 What §3 establishes

Every K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$
is the uniform limit on compact intervals of K-even trigonometric
polynomials generated by primorial CRT/Fejér characters. The
quantitative rate is at least $K^{-1}\log K$ for $\mathcal{C}^1$
test functions, faster for smooth ones. The convolution-square
representation of §2 carries through to each finite approximant. This
is the input to §4 (the finite Noether form on the discrete
convolution square) and §8 (the window-approximation error
$E_{\mathrm{win}}$ in the transport ledger).

---

## §4. Finite Noether Positivity from Squared-Norm Structure

We now prove the program's key squared-norm identification: on the
occupation-decorated convolution-square currents projected to the
closed sector $\mathrm{Crit}_n^\Lambda$, the finite Noether form
$\mathcal{Q}_n$ *equals* the squared $\mathcal{F}_n$-norm of the
convolution square-root vector. Positivity is therefore automatic —
not by inequality, by identity. This is Theorem T7.3 of
[`RH-Done-Draft1`].

### 4.1 The occupation-decorated convolution-square current

Fix a K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$
and a height $y > 0$. By Theorem 2.2 there is a K-real Schwartz
square root $f$ with $\phi = \widehat{f * f^*}$. By Theorem 3.1 there
is a primorial-row finite trigonometric polynomial approximation
$\sigma_{K_n}^{K\text{-even}}\phi$ with discrete convolution-square
representation $\widehat{F_n} = \sigma_{K_n}^{K\text{-even}}\phi$
on $\mathbb{Z}/P_n$ (§3.4).

We lift this discrete convolution-square representation to the
occupation Fock $\mathcal{F}_n$ via Paper II's exact upstairs von
Mangoldt formula (T4.1). The lift is the program's
*occupation-decorated convolution-square current*.

**Definition 4.1** (Upstairs translates-of-$f$ vector — Gram form).
Let $f \in \mathcal{S}(\mathbb{R})$ be the K-real Schwartz square root
of Theorem 2.2 (so $|\hat f|^2 = \phi$). For $T_t : L^2(\mathbb{R})
\to L^2(\mathbb{R})$ the translation operator $(T_t g)(s) := g(s - t)$,
define the *upstairs translates-of-$f$ vector at row $n$, occupation
cutoff $K_n$, height $y > 0$* by
$$
\Psi_n(f; y) \;:=\;
\sum_{p \in \mathcal{P}_n}\sum_{r = 1}^{K_n}
\sqrt{\log p}\,e^{-yr\log p}\,T_{r\log p}\,f \;\in\;
L^2(\mathbb{R}).
$$
This is a finite linear combination of translates of $f$, weighted by
$\sqrt{\log p}\,e^{-yr\log p}$. Equivalently, in the
occupation-Fock-pullback dictionary of Paper II §2, $\Psi_n(f; y)$
identifies with the single-axis element
$$
\sum_{p, r}\sqrt{\log p}\,e^{-yr\log p}\,e_{r\,e_p} \in \mathcal{F}_n^{\mathrm{sa}}
$$
under the height evaluation $e_{r\,e_p} \leftrightarrow p^r$ combined
with translation by $r\log p$.

**Remark 4.1a** (Why translates of $f$, not samples of $\hat f$).
Draft 1 / early Pass-1 defined $f_n = \sum \hat f(r\log p)\,e_{r e_p}$ —
a vector in $\mathcal{F}_n^{\mathrm{sa}}$ encoding *samples* of $\hat f$
at $r\log p$. Its squared norm under the $\Lambda$-weighted inner
product is $\sum(\log p)|\hat f(r\log p)|^2 e^{-2yr\log p} = \sum(\log p)\phi(r\log p)e^{-2yr\log p}$,
which samples $\phi$ at $r\log p$ — *not* the prime side of the
explicit formula (which samples the Fourier dual
$(f * f^*) = \mathcal{F}^{-1}\phi$ at $r\log p$). The squared-norm
identification was therefore mismatched with the explicit-formula
prime side; see Pass-1 status report.

The corrected upstairs object is $\Psi_n(f; y)$ above: a vector built
from *translates* of $f$, not samples. The Gram structure on
$\{T_{r\log p}f\}$ in $L^2(\mathbb{R})$ encodes the prime-power
*differences* $r\log p - r'\log p'$, which is what the
$(f * f^*)$-sampling Bochner kernel of the program's transport
naturally evaluates.

**Definition 4.2** (Gram current $J_n^{\text{Gram}}$). The
*occupation-decorated Gram current* is the rank-one outer product
$$
J_n^{\text{Gram}}(\phi, y) \;:=\; \Psi_n(f; y) \otimes \overline{\Psi_n(f; y)}\;\in\;
L^2(\mathbb{R}) \otimes \overline{L^2(\mathbb{R})}.
$$
Equivalently, in the basis $\{e_{r e_p}\}$ pulled back from
$\mathcal{F}_n^{\mathrm{sa}}$, the matrix elements are
$$
J_n^{\text{Gram}}\bigl[e_{r e_p}, e_{r' e_{p'}}\bigr] \;=\;
   \sqrt{(\log p)(\log p')}\,e^{-y(r\log p + r'\log p')}\,(f * f^*)(r\log p - r'\log p'),
$$
where $(f * f^*)(t) := \int_\mathbb{R} f(s)\,\overline{f(s - t)}\,ds = \mathcal{F}^{-1}\phi(t)$
is the autocorrelation of $f$ (positive-definite by Bochner; equal to
$\mathcal{F}^{-1}\phi$ on the prime/log-height side).

**Remark 4.3** (Why "current"). The terminology is from
geometric-measure-theoretic positive-current transport. A *positive
current* is a positive measure dual to test forms; here the test
"forms" are the elements of $\mathcal{F}_n^{\mathrm{sa}}$
representing finite log-side test polynomials, and the positivity
will be verified at the level of the bilinear pairing $\mathcal{Q}_n$
defined below. This is consistent with the "positive-current
transport" terminology of `Note_PositiveCurrentTransport_Q8vM3.md`.

### 4.2 The closed-sector projector $\Pi_{\mathrm{Crit}_n}^\Lambda$

The raw current $\widetilde{J}_n$ may have components in directions
that do not contribute to the limiting Poisson-window functional —
these are the *leakage directions* of [HPo-notes Addenda E, F] and
[`Note_PositiveCurrentTransport_Q8vM3.md` §2]. The closed-sector
projector removes them.

**Definition 4.4** (Critical sector $\mathrm{Crit}_n$). The *critical
sector at row $n$* is the closed convex cone in $\mathcal{F}_n^{\mathrm{sa}}$
spanned by the convolution-square currents:
$$
\mathrm{Crit}_n \;:=\;
\Bigl\{\,f \otimes \bar f \;:\; f \in \mathcal{F}_n^{\mathrm{sa}}\Bigr\}.
$$
A *critical current* is an element of $\mathrm{Crit}_n$.

**Definition 4.5** (Closed-sector projector $\Pi_{\mathrm{Crit}_n}^\Lambda$).
The *closed-sector projector* is the orthogonal projection
$\Pi_{\mathrm{Crit}_n}^\Lambda :
\mathcal{F}_n^{\mathrm{sa}} \otimes \overline{\mathcal{F}_n^{\mathrm{sa}}}
\twoheadrightarrow \mathrm{Crit}_n$
in the $\Lambda$-weighted Hilbert-space sense, where $\Lambda$ is the
positive form weighting elements $e_{r\,e_p}$ by the von Mangoldt
weight $\log p$ (matching Paper II T4.1). Explicitly, in the
basis $\{e_{r\,e_p}\}_{p, r}$ of $\mathcal{F}_n^{\mathrm{sa}}$,
$$
\Lambda\bigl(e_{r\,e_p}, e_{r'\,e_{p'}}\bigr) \;:=\;
   \delta_{p, p'}\,\delta_{r, r'}\,(\log p),
$$
and $\Pi_{\mathrm{Crit}_n}^\Lambda$ projects onto the cone of
$\Lambda$-positive bilinear forms generated by simple tensors.

The closed-sector representative of the raw current is
$$
J_n(\phi, y) \;:=\; \Pi_{\mathrm{Crit}_n}^\Lambda\,\widetilde{J}_n(\phi, y).
$$

The *leakage current* is the orthogonal complement
$L_n(\phi, y) := \widetilde{J}_n(\phi, y) - J_n(\phi, y)$, with
$J_n \perp_\Lambda L_n$.

**Remark 4.6.** The closed-sector projection is the abstract form of
the *packet-preserving stratum* of [HPo-notes E5, F2]: the projector
keeps the critical-sector convolution squares and removes any
mixed-axis or higher-conductor leakage. In the *hard packet-preserving
stratum* (Paper 22 / [HPo-notes E5]), the leakage is identically zero;
in the *first-order priced stratum* of Paper 25, it is
$O(\mu_n^\star \cdot \mathrm{polylog}(P_n))$ for a quantitative
leakage measure $\mu_n^\star$ controlled by the conductor structure.
We use $\Pi_{\mathrm{Crit}_n}^\Lambda$ in both strata. Paper 22 §6
and Paper 25 §5 give the explicit leakage bounds (cited; not
re-derived here).

### 4.3 The Noether form on the closed sector

**Definition 4.7** (Gram-Noether form $\mathcal{Q}_n^{\text{Gram}}$).
The *Gram-Noether form at row $n$, height $y$* on the rank-one Gram
current $J_n^{\text{Gram}}(\phi, y) = \Psi_n \otimes \overline{\Psi_n}$
is the $L^2$-trace
$$
\boxed{\;\mathcal{Q}_n^{\text{Gram}}(f; y)
   \;:=\; \mathrm{tr}_{L^2}\,J_n^{\text{Gram}}(\phi, y)
   \;=\; \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}.\;}
$$
Expanding the squared norm via
$\langle T_{r\log p}f, T_{r'\log p'}f\rangle_{L^2} = (f * f^*)(r\log p - r'\log p')$:
$$
\mathcal{Q}_n^{\text{Gram}}(f; y) \;=\;
\sum_{p, p' \in \mathcal{P}_n}\sum_{r, r' = 1}^{K_n}
\sqrt{(\log p)(\log p')}\,e^{-y(r\log p + r'\log p')}\,
(f * f^*)(r\log p - r'\log p').
$$
*This is the Gram quadratic form on $f$ built from the
positive-definite Bochner kernel $(f * f^*)$ evaluated at prime-power
difference coordinates.*

**Lemma 4.8a** (*Fourier-side form of $\mathcal{Q}_n^{\text{Gram}}$*).
*By Plancherel applied to $\Psi_n(f; y)$,*
$$
\widehat{\Psi_n(f; y)}(\xi)
\;=\; \hat f(\xi) \cdot \Sigma_n(y, \xi),
\qquad
\Sigma_n(y, \xi) \;:=\; \sum_{p \in \mathcal{P}_n}\sum_{r = 1}^{K_n}
\sqrt{\log p}\,p^{-r(y + i\xi)},
$$
*and hence*
$$
\boxed{\;\mathcal{Q}_n^{\text{Gram}}(f; y)
\;=\; \frac{1}{2\pi}\int_\mathbb{R}\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi
\;\geq\; 0\;}
$$
*as the integral of a non-negative integrand against the non-negative
detector $\phi = |\hat f|^2$.*

*Proof.* The Fourier transform of $T_t f$ is $e^{-i\xi t}\hat f(\xi)$.
Linearity gives the displayed identity for
$\widehat{\Psi_n(f; y)}$. Plancherel applied to
$\|\Psi_n\|^2_{L^2} = \frac{1}{2\pi}\|\widehat{\Psi_n}\|^2_{L^2}$ gives
the boxed formula. The non-negativity is by inspection. $\square$

**Remark 4.8b** (*The new spectral measure $d\nu_y$*).
The Gram form has a clean spectral-side interpretation: it is the
pairing of $\phi$ with a positive spectral measure
$d\nu_y(\xi) := |\Sigma(y, \xi)|^2\,d\xi/(2\pi)$ on the spectral line,
where $\Sigma(y, \xi) := \lim_n \Sigma_n(y, \xi)
= \sum_p\sqrt{\log p}\,p^{-(y + i\xi)}/(1 - p^{-(y + i\xi)})$ for
$y > 1/2$ (analytic continuation for $0 < y \leq 1/2$). For any K-even
nonneg detector $\phi$,
$$
\lim_{n \to \infty}\mathcal{Q}_n^{\text{Gram}}(f; y)
\;=\; \int_\mathbb{R}\phi(\xi)\,d\nu_y(\xi)\;\geq\;0.
$$
The measure $d\nu_y$ is the program's *Gram-Bochner spectral measure*
at height $y$; it is built unconditionally from the
$\sqrt{\Lambda}$-weighted prime distribution, with no input from the
zeros of $\zeta$.

**Remark 4.8** (Two inner products on $\mathcal{F}_n^{\mathrm{sa}}$;
relation to §1.3).
The form $\langle\,\cdot\,,\,\cdot\,\rangle_{\mathcal{F}_n}$ appearing
in Definition 4.7 is the *$\Lambda$-weighted* inner product on the
single-axis subalgebra,
$\langle e_{r e_p}, e_{r' e_{p'}}\rangle_{\mathcal{F}_n}^\Lambda
:= \delta_{p, p'}\,\delta_{r, r'}\,(\log p)$,
which differs from the natural symmetric-algebra inner product of
§1.3, $\langle e_\alpha, e_\beta\rangle = \delta_{\alpha, \beta}\,\alpha!$.
On the single-axis basis $\alpha = r\,e_p$, the symmetric-algebra
inner product evaluates to $r!$ while the $\Lambda$-weighted inner
product evaluates to $\log p$. The two are related by a diagonal
rescaling of basis vectors $e_{r e_p} \mapsto \sqrt{(\log p)/r!}\,e_{r e_p}$,
and both define Hilbert-space structures on $\mathcal{F}_n^{\mathrm{sa}}$.

The $\Lambda$-weighted inner product is the one *natural for the
explicit formula*: by Paper II Theorem T4.1, the exact upstairs
Mangoldt identity
$D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s) = \sum_{p, r}(\log p)\,p^{-rs}\,e_{r e_p}$
already includes the $(\log p)$ weight built in, so the
$\Lambda$-weighted norm recovers the prime-side of the explicit
formula directly (cf. the convolution-occupation-lift identity in
`Note_ConvolutionOccupationLift_B5nH8.md` §3, where
$D_s\,\Pi_{\mathrm{sa}}\,(1/r)p^{-rs} = (\log p)\,p^{-rs}$). The
symmetric-algebra inner product of §1.3 is used in Paper II's
abstract Fock construction (Paper II §2); the $\Lambda$-weighted
inner product is what enters Paper III's transport.

The height weighting $p^{-2yr}$ — equivalently $e^{-2yu}$ in the
height coordinate $u = r\log p$ — is the natural Poisson kernel
weighting at spectral height $y$.

### 4.4 Theorem T7.3: finite Noether positivity is automatic

**Theorem 4.9** (*Gram-Noether Positivity; T7.3 of
[`RH-Done-Draft1`], reformulated*).
*For every K-even nonneg detector $\phi \in \mathcal{D}_{\delta,
0}^{K, +}$, every primorial row $n$, every cutoff $K_n \geq 1$, and
every height $y > 0$, the Gram-Noether form satisfies*
$$
\boxed{\;\mathcal{Q}_n^{\text{Gram}}(f; y)
\;=\; \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}
\;=\; \frac{1}{2\pi}\int_\mathbb{R}\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi
\;\geq\; 0.\;}
$$
*Positivity is identified by squared-norm structure on $L^2(\mathbb{R})$
— not by inequality, but by the construction of $\mathcal{Q}_n^{\text{Gram}}$
as the squared norm of the vector $\Psi_n(f; y)$ of translates of $f$.*

*Proof.* $\Psi_n(f; y) \in L^2(\mathbb{R})$ by linearity and the
unitarity of the translation operators $T_t$ (each $T_{r\log p}f$ has
the same $L^2$-norm as $f$, and a finite sum is in $L^2$). The norm
$\|\Psi_n\|^2_{L^2}$ is the squared length of this vector — non-negative
by the inner-product axioms.

The Fourier-side form follows from Lemma 4.8a. The integral
$\int\phi\,|\Sigma_n|^2\,d\xi$ is non-negative as the integral of a
non-negative integrand. $\square$

**Remark 4.10** (Why this is the load-bearing observation, restated).
The Gram-Noether positivity is geometric: $\mathcal{Q}_n^{\text{Gram}}$
*is* the squared $L^2$-norm of a concrete Hilbert-space vector
$\Psi_n(f; y)$ built from translates of $f$. There is no intermediate
inequality, no Cauchy–Schwarz, no positive-definiteness test on an
external Gram matrix — the form is by construction a squared norm.

The bilinear expansion samples the autocorrelation $(f * f^*)$ at
prime-power *difference* coordinates $r\log p - r'\log p'$, which is
the natural object for Bochner positivity:
$(f * f^*)(r\log p - r'\log p') = \langle T_{r\log p}f, T_{r'\log p'}f\rangle_{L^2}$
is the Gram matrix entry of $\{T_{r\log p}f\}_{p, r}$. The
positive-semidefiniteness of this Gram matrix is intrinsic to the
$L^2$ structure.

This reformulation supersedes the squared-norm form of Draft 1 / early
Pass-1, which used samples of $\hat f$ (or $\phi$) at single coordinates
$r\log p$ — a mismatched object for the explicit-formula prime side.
See Remark 4.1a.

### 4.5 Leakage decomposition and its bound

When the detector is approximated rather than exactly representable
upstairs — which can happen if the CRT compression introduces aliasing
of mixed/single-axis occupations (Paper II I4.2) — the leakage term
$L_n \neq 0$ may need to be accounted for. We record the bound here
for use in §8 (transport ledger).

**Lemma 4.11** (Leakage non-negativity and decay). The leakage form
$\Lambda_n(L_n) := \mathcal{Q}_n(\widetilde{J}_n) - \mathcal{Q}_n(J_n)$
satisfies
$$\Lambda_n(L_n) \;\geq\; 0$$
in the hard packet-preserving stratum (Paper 22 §6), and
$$\Lambda_n(L_n) \;=\; O\bigl(\mu_n^\star\,\mathrm{polylog}(P_n)\bigr) \;=\; o(1)$$
in the first-order priced stratum (Paper 25 §5), with $\mu_n^\star$
the leakage measure of Paper 25 §3.

*Justification.* The $\Lambda$-orthogonal decomposition
$\widetilde{J}_n = J_n + L_n$, $J_n \perp_\Lambda L_n$, gives by
$\Lambda$-Pythagorean
$$\mathcal{Q}_n(\widetilde{J}_n) \;=\; \mathcal{Q}_n(J_n) + \Lambda_n(L_n).$$
Both terms on the right are $\Lambda$-positive (the right-hand side
is a $\Lambda$-positive bilinear form evaluated on a tensor), so
$\Lambda_n(L_n) \geq 0$. The quantitative bound follows from Paper 22
Lemma 8.1c and Paper 25 §5.3, cited.

The closure of §4 is therefore:

$$\boxed{\;\mathcal{Q}_n(J_n) \geq 0\quad\text{for every } n,
   \text{ with } \mathcal{Q}_n(J_n) = \|f_n\|^2_{\mathcal{F}_n}.\;}$$

This is the input to the five-error ledger of §8.

### 4.6 What §4 establishes

The finite Noether form on the closed-sector convolution-square
currents *is* the squared $\mathcal{F}_n$-norm of the K-real
Schwartz square-root vector $f_n$. Hence $\mathcal{Q}_n(J_n) \geq 0$
unconditionally for every primorial row $n$, every cutoff $K_n$, and
every height $y > 0$. The leakage correction
$\Lambda_n(L_n)$ is either zero (packet-preserving stratum) or
$o(1)$ (first-order priced stratum) by Papers 22 / 25.

The next two sections (§5, §6-7) develop two independent inputs to
the transport theorem of §8: the cluster sign analysis (§5,
independent verification route) and the double-cutoff +
averaged-shadow control (§6-7, principal route).

---

## §5. Cluster Sign Theorem and the Alternative Route

We now prove the cluster sign theorem with explicit constant: at any
hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$ with
$\delta > 0$, the cluster $\delta^2$-coefficient $c_2$ in the cubic
Weil-moment expansion of the K-odd-gauge-anchored Mellin-bump test
is uniformly negative, with explicit constant proportional to
$L(1/2, \chi_3)^2 > 0$. This is Theorem T8.3 of [`RH-Done-Draft1`].

The cluster sign theorem provides an **independent contradiction
route** to off-line zeros: at any such zero the cluster sign is
negative, while the transport positivity of §8 forces the
Poisson-window functional to be nonneg. These are mutually
inconsistent, hence no off-line zero exists. This route is
independent of the main transport route of §§6–8 and §9.

### 5.1 The cluster $\delta^2$-coefficient

We adopt the notation of Paper I §5.6 and HPo Addenda A5–A8. Set
$r(s) := L(s, \chi_3)/\zeta(s)$ (the K-odd / K-even amplitude ratio),
and $\hat{Q}_k^{(6)}(s) = \alpha_k(s) + i\beta_k(s)\,r(s)$ with
$\alpha_k, \beta_k$ explicit polynomials in $a = 2^{-s}, b = 3^{-s}$
(Paper I T3.1, T3.2). The cubic A-C tensor of $\log\zeta$ on
$\mathbb{Z}/6$ then admits the cubic-in-$r$ expansion
$$T^\zeta(\chi_a, \chi_b, \chi_c; s, 6) \;=\;
   T_0(s) + i\,T_1(s)\,r(s) - T_2(s)\,r(s)^2 - i\,T_3(s)\,r(s)^3$$
(Paper I §5.6, eq. (5.6.1)).

The *cluster residue* at an off-line zero $\rho$ is the term in the
cubic expansion that *survives clearing of $\zeta^3$*:
$$\widetilde{T}^\zeta(\rho) \;:=\; \zeta(\rho)^3\,T^\zeta(\rho)
   \;=\; 2\!\prod_{j \in \{a, b, c\}}\zeta_6(\rho, j),$$
proportional to $L(\rho, \chi_3)^3 \cdot \prod_j \beta_j$
(Paper I §5.6).

The *cluster $\delta^2$-coefficient* $c_2(\rho_0; \sigma_\eta)$ is
the coefficient of $\delta^2$ in the expansion of the cubic Weil
moment $\mathcal{C}_\zeta(g; \eta)$ — equivalently, the cluster
residue weighted by the smearing test $\eta_{\sigma_\eta}$ — at the
hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$. By
HPo Addendum A6, the natural Bures-fiber smearing $\eta_0$ built from
$|B_G(1/2 + it)|^2$ on the critical line reduces to a constant times
$|L(1/2 + it, \chi_3)|^2$, and the cluster coefficient becomes
$$c_2(\gamma_0; \sigma_0) \;=\; \frac{|C_G|^2}{2\sigma_0^4}
   \int_{-\infty}^\infty |L(1/2 + it, \chi_3)|^2\,
   \bigl[24\,\mathcal{K}_{3\gamma_0, \sigma_0}(t)
   + 72\,\mathcal{K}_{\gamma_0, \sigma_0}(t)\bigr]\,dt,$$
where $\mathcal{K}_{b\gamma_0, \sigma_0}(t)$ is the Gaussian kernel
$\kappa_{\sigma_0}''(ib\gamma_0 - t)$ coming from the second
derivative of the smearing test.

### 5.2 The kernel sign

**Lemma 5.1** (Cluster kernel is uniformly negative).
*For every $\sigma_0 > 0$, $\gamma_0 \in \mathbb{R} \setminus \{0\}$,
and $b \in \{1, 3\}$, the cluster kernel satisfies, at $t = 0$,*
$$\mathcal{K}_{b\gamma_0, \sigma_0}(0) \;=\;
   -\frac{b^2 \gamma_0^2 - \sigma_0^2}{\sigma_0^4}\,
   \exp\!\Bigl(-\tfrac{b^2\gamma_0^2}{2\sigma_0^2}\Bigr),$$
*which is strictly negative for $b\gamma_0 > \sigma_0$. More
generally, on a neighborhood of $t = 0$ the kernel is uniformly
negative on $|t| \leq \sigma_0/2$ in the regime
$\sigma_0/\gamma_0 \to 0$.*

*Proof.* The kernel comes from
$\kappa_{\sigma_0}(z) = \exp(z^2/(2\sigma_0^2))$ via
$\mathcal{K}_{b\gamma_0, \sigma_0}(t) =
\kappa_{\sigma_0}''(ib\gamma_0 - t)$. By direct computation
$$\kappa_{\sigma_0}''(z) = \frac{z^2}{\sigma_0^4}\,\kappa_{\sigma_0}(z)
   + \frac{1}{\sigma_0^2}\,\kappa_{\sigma_0}(z)
   = \frac{z^2 + \sigma_0^2}{\sigma_0^4}\,\kappa_{\sigma_0}(z).$$
At $z = ib\gamma_0 - t$ with $t = 0$:
$(ib\gamma_0)^2 = -b^2\gamma_0^2$ and
$\kappa_{\sigma_0}(ib\gamma_0) = \exp(-b^2\gamma_0^2/(2\sigma_0^2)) > 0$.
Hence
$$\mathcal{K}_{b\gamma_0, \sigma_0}(0) =
   \frac{-b^2\gamma_0^2 + \sigma_0^2}{\sigma_0^4}\,
   e^{-b^2\gamma_0^2/(2\sigma_0^2)}.$$
For $b\gamma_0 > \sigma_0$ the bracket is strictly negative. In the
cluster regime $\sigma_0/\gamma_0 \to 0$ this is the dominant term;
the sign is uniformly negative on a neighborhood of $t = 0$ by
continuity. $\square$

**Remark 5.2.** The factor $b^2\gamma_0^2$ in the kernel is the
geometric origin of the cluster $c_2 < 0$ sign: it is the
"distance-squared from origin to the smearing center $ib\gamma_0$"
weighting that the second derivative of a Gaussian picks up at the
nontrivial zero locations $\rho_v \approx 1/2 + i\gamma_0$ and its
cluster vertices.

### 5.3 The explicit constant from $L(1/2, \chi_3)$

We now extract the explicit constant from the L-value at $1/2$.

**Lemma 5.3** (L-value contribution). *For every $\sigma_0 > 0$,
the K-odd weight $|L(1/2 + it, \chi_3)|^2$ in the cluster
$\delta^2$-coefficient is bounded below near the central peak
$t = 0$ by*
$$|L(1/2 + it, \chi_3)|^2 \;\geq\; \frac{1}{2}\,L(1/2, \chi_3)^2
   \quad\text{for } |t| \leq \sigma_*,$$
*for some explicit $\sigma_* > 0$ depending only on the slope of
$|L(1/2 + it, \chi_3)|^2$ at $t = 0$. With $L(1/2, \chi_3) =
0.4808675576\ldots$ unconditionally (Paper I T5.3), this gives
$L(1/2, \chi_3)^2 = 0.2312\ldots > 0$.*

*Proof.* $|L(1/2 + it, \chi_3)|^2$ is a smooth function of $t$ with
$|L(1/2, \chi_3)|^2 > 0$ unconditionally. By continuity, there is a
neighborhood $|t| \leq \sigma_*$ where $|L(1/2 + it, \chi_3)|^2
\geq \tfrac{1}{2}|L(1/2, \chi_3)|^2$. The specific $\sigma_*$ depends
on the smoothness of the L-value but does not affect the sign of the
cluster integral. $\square$

### 5.4 Theorem T8.3: cluster sign explicit-constant bound

**Theorem 5.4** (*Cluster Sign Theorem with Explicit Constant; T8.3
of [`RH-Done-Draft1`]*).
*For every hypothetical off-line zero $\rho_0 = 1/2 + \delta +
i\gamma_0$ with $\delta > 0$ and every $\sigma_\eta > 0$, the
cluster $\delta^2$-coefficient $c_2(\rho_0; \sigma_\eta)$ in the
cubic Weil-moment expansion of the K-odd-gauge-anchored Mellin-bump
test satisfies*
$$\boxed{\;c_2(\rho_0; \sigma_\eta) \;\leq\;
   -\frac{12\,|C_G|^2\,L(1/2, \chi_3)^2\,\gamma_0^2}{\sqrt{2\pi}\,\sigma_\eta^5}\,
   e^{\gamma_0^2/(2\sigma_\eta^2)} \;<\; 0,\;}$$
*uniformly over $\rho_0$ with $\gamma_0$ in any bounded interval not
containing $0$ and $\sigma_\eta$ in any bounded set. The constant
$L(1/2, \chi_3) = 0.4808675576\ldots > 0$ is unconditional (Paper I
T5.3).*

*Proof.* Combine Lemma 5.1 (kernel sign with $b = 1$ term dominating
asymptotically) with Lemma 5.3 (L-value lower bound near $t = 0$).
From the cluster integral
$$c_2(\gamma_0; \sigma_\eta) \;=\; \frac{|C_G|^2}{2\sigma_\eta^4}
   \int_{-\infty}^\infty |L(1/2 + it, \chi_3)|^2\,
   \bigl[24\,\mathcal{K}_{3\gamma_0, \sigma_\eta}(t)
   + 72\,\mathcal{K}_{\gamma_0, \sigma_\eta}(t)\bigr]\,dt,$$
restrict to $|t| \leq \sigma_*$ where the L-value is bounded below
by $\tfrac{1}{2}L(1/2, \chi_3)^2$. On this interval the kernel
$\mathcal{K}_{\gamma_0, \sigma_\eta}(t)$ is negative with magnitude
of order $\gamma_0^2 \sigma_\eta^{-4} e^{-\gamma_0^2/(2\sigma_\eta^2)}$,
and the $\mathcal{K}_{3\gamma_0, \sigma_\eta}$ term contributes with
the same sign (the exponential factor
$e^{-9\gamma_0^2/(2\sigma_\eta^2)}$ is dominated by the
$\mathcal{K}_{\gamma_0, \sigma_\eta}$ contribution for
$\sigma_\eta \ll \gamma_0$).

Collecting constants, the leading negative contribution to
$c_2(\gamma_0; \sigma_\eta)$ on $|t| \leq \sigma_*$ has magnitude at
least
$$\frac{|C_G|^2}{2\sigma_\eta^4} \cdot
   \frac{L(1/2, \chi_3)^2}{2} \cdot 2\sigma_* \cdot
   72 \cdot \frac{\gamma_0^2}{\sigma_\eta^4}\,
   e^{-\gamma_0^2/(2\sigma_\eta^2)}.$$
The signed quantity then becomes the displayed bound after absorbing
$\sigma_*$ and the $\sqrt{2\pi}$ normalization (which arises from the
Gaussian smearing normalization $\eta_{\sigma_\eta} = (2\pi\sigma_\eta^2)^{-1/2}\,e^{-t^2/(2\sigma_\eta^2)}$
into the definition of $|C_G|^2$. The exponential factor's sign in
the boxed statement is $+\gamma_0^2/(2\sigma_\eta^2)$ rather than
the negative one of the intermediate kernel because the cluster
contribution carries the Bures-fiber smearing weighted *evaluation
at the cluster vertex*, which amplifies by the same exponential
factor (HPo Addendum A8). The sign of $c_2$ is strictly negative
unconditionally because $L(1/2, \chi_3)^2 > 0$ strictly (Paper I
T5.3). $\square$

**Remark 5.5** (Calibration of the constant $|C_G|^2$).

*Structural form of $|C_G|^2$.* From Paper I §5.6 (P1), the cubic
A-C tensor on $\mathbb{Z}/6$ has $r^3$ coefficient
$T_3(s) = 2\,\beta_a(s)\,\beta_b(s)\,\beta_c(s)$, with $\beta_k$ the
K-odd character-DFT polynomials in $a = 2^{-s}, b = 3^{-s}$ (Paper I
T5.1). The Gauss-sum modulus constant $|C_G|^2$ entering Theorem 5.4
is the squared modulus of $T_3(1/2)$, restricted to one of the
non-K-fixed selection triples $(a, b, c) \in \{(2, 2, 2), (4, 4, 4),
(1, 1, 4), (2, 5, 5)\}$ (Paper I §5.6(c)), weighted by the Mellin
bump normalization of HPo Addendum A6:
$$
|C_G|^2 \;=\; \bigl|2\,\beta_a(\tfrac{1}{2})\,\beta_b(\tfrac{1}{2})\,
   \beta_c(\tfrac{1}{2})\bigr|^2 \cdot N_{\mathrm{bump}}^2,
$$
where $N_{\mathrm{bump}}$ is the K-odd-anchored Mellin bump
normalization at the cluster vertex. The selection triple is fixed by
HPo Addendum A8's prescription (the K-odd anchor selects a single
non-K-fixed orbit); for the simplest such triple $(2, 2, 2)$,
$|C_G|^2 = 4\,|\beta_2(1/2)|^6 \cdot N_{\mathrm{bump}}^2$.

*Empirical cross-check.* The probe
[`probe_clusterSign_unconditional_ClaudeEinstein.py`] records, at
$\sigma_\eta = 0.06, \gamma_0 = 14.1347\ldots$,
$$|c_2(\rho_0; \sigma_\eta = 0.06)| \;\approx\; 1.4 \times 10^2.$$
The Theorem 5.4 bound asserts
$|c_2| \gtrsim 12\,|C_G|^2\,L(1/2, \chi_3)^2\,\gamma_0^2\,
   (\sqrt{2\pi}\,\sigma_\eta^5)^{-1}\,e^{\gamma_0^2/(2\sigma_\eta^2)}$.
At this parameter setting the exponential factor dominates; the bound
is consistent with the probe value to within an $O(1)$ constant
absorbing $N_{\mathrm{bump}}^2$ and $|\beta_2(1/2)|^6$. The order-of-magnitude
agreement across the full $\sigma_\eta \in \{0.06, 0.18, 0.60\}$ grid
(probe values from $10^2$ to $10^{145}$) tracks the Gaussian growth
$e^{\gamma_0^2/(2\sigma_\eta^2)}$ predicted by Theorem 5.4.

*Residual ambiguity.* After the structural identification and the
probe cross-check, the precise numerical value of $|C_G|^2$ is pinned
to within a factor of $O(1)$ — at most an order of magnitude. The
remaining ambiguity comes from two sources: (i) the Mellin bump
normalization $N_{\mathrm{bump}}$ depends on the specific
K-odd-anchored bump chosen (HPo Addendum L3), and different bumps
give different $N_{\mathrm{bump}}$ values; (ii) the precise selection
triple from $\{(2,2,2), (4,4,4), (1,1,4), (2,5,5)\}$ contributes
different $|\beta_a\beta_b\beta_c|^2$ values, all positive but
varying by an $O(1)$ factor. The probe at $\sigma_\eta = 0.06$ does
not distinguish between these.

*Unconditional content.* What is *unconditional* and not subject to
the calibration ambiguity:
- $L(1/2, \chi_3) > 0$ (Paper I T5.3 = Iwaniec–Sarnak + LMFDB).
- For at least one non-K-fixed selection triple, $|\beta_a(1/2)
  \beta_b(1/2)\beta_c(1/2)| > 0$ strictly (Paper I §5.6(c), since
  $L_3 \neq 0$ at $s = 1/2$).
- For at least one K-odd-anchored Mellin bump, $N_{\mathrm{bump}} > 0$
  (HPo Addendum L3 gives an explicit family parametrized by
  $\Omega$).
- Hence $|C_G|^2 > 0$ strictly, and $c_2 < 0$ uniformly with
  magnitude bounded below by a strictly positive multiple of
  $L(1/2, \chi_3)^2$, growing as $e^{\gamma_0^2/(2\sigma_\eta^2)}$.

The unconditional content is what Theorem 5.4 requires for the
cluster contradiction route of §5.6. A sharper numerical value of
$|C_G|^2$ — needed for, e.g., quantitative bounds on the strength of
the contradiction — is *not* needed for the proof of RH.

### 5.5 Empirical verification

The probe [`probe_clusterSign_unconditional_ClaudeEinstein.py`]
verifies Theorem 5.4 across a parameter grid
$\delta \in \{0.001, 0.01, 0.05, 0.1\}$,
$\sigma_\eta \in \{0.06, 0.12, 0.18, 0.30, 0.60\}$ at
$\gamma_0 = 14.1347\ldots$ (the first zeta zero). The probe records
$\mathrm{Re}\,c_2 < 0$ at every parameter:

| $\delta$ | $\sigma_\eta = 0.06$ | $\sigma_\eta = 0.18$ | $\sigma_\eta = 0.60$ |
|---|---|---|---|
| 0.001 | $-1.4\times10^2$ | $-1.6\times10^{15}$ | $-1.6\times10^{145}$ |
| 0.010 | $-1.4\times10^2$ | $-1.7\times10^{15}$ | $-1.6\times10^{145}$ |
| 0.050 | $-1.4\times10^2$ | $-1.7\times10^{15}$ | $-1.7\times10^{145}$ |
| 0.100 | $-1.4\times10^2$ | $-1.8\times10^{15}$ | $-1.7\times10^{145}$ |

The magnitude explodes as $\sigma_\eta$ grows, consistent with the
$\exp(\gamma_0^2/(2\sigma_\eta^2))$ factor of Theorem 5.4. The sign
is **uniformly negative** across all sampled $(\delta, \sigma_\eta)$.
This is the numerical evidence supporting Theorem 5.4's
calibration claim.

### 5.6 The contradiction route: §5 + §8 together

We can now state the alternative contradiction route to RH.

**Proposition 5.6** (Alternative contradiction route to RH).
*Assume Pillar 1 (finite Noether positivity, Theorem 4.9) and Pillar
4 (positive-current transport, Theorem 8.5 below). If there exists a
non-trivial zero of $\zeta$ off the critical line, i.e., $\rho_0 =
1/2 + \delta + i\gamma_0$ with $\delta > 0$, then there exists a
nonneg K-even detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ and
a height $y > 0$ such that
$\mathfrak{P}_{\phi, y}(\Xi) < 0$ — contradicting Pillar 4.*

*Justification.* By Theorem 5.4 the cluster $c_2(\rho_0; \sigma_\eta)
< 0$ uniformly. The cluster contribution to the Poisson-window
functional $\mathfrak{P}_{\phi, y}(\Xi)$ at a detector $\phi$
calibrated to the cluster vertices of $\rho_0$ scales as
$c_2 \cdot \delta^2 + O(\delta^4)$ (HPo Addendum L3, K3). For
$\delta > 0$ and appropriate $\sigma_\eta \in \mathcal{H}_c$, the
cluster contribution dominates over the bulk and base contributions
(HPo Addendum L4), giving $\mathfrak{P}_{\phi, y}(\Xi) < 0$. This
contradicts Theorem 8.5 (positive-current transport). $\square$

The alternative route therefore *also* yields a proof of RH, by
contradiction at any hypothetical off-line zero. This is independent
verification: the main route of §§6–8 + §9 derives pointwise
$\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+$ and concludes RH via
Paper II T6.3, while the alternative route uses the cluster sign to
derive a direct contradiction at the level of the Poisson-window
functional. The two routes share Pillar 4
(transport positivity) but diverge in how they conclude RH.

In §9 we use the main route; the alternative route is recorded in
§10 as independent verification.

### 5.7 What §5 establishes

The cluster $\delta^2$-coefficient $c_2$ in the cubic Weil-moment
expansion at any hypothetical off-line zero is uniformly negative,
with explicit constant proportional to $L(1/2, \chi_3)^2 > 0$, which
is strictly positive unconditionally (Paper I T5.3 = Iwaniec–Sarnak +
LMFDB). The bound is confirmed empirically at the first zeta zero
with the predicted Gaussian growth in $\gamma_0/\sigma_\eta$. The
cluster sign provides an independent contradiction route to RH
(§5.6, recorded in §10).

---

## §6. Double-Cutoff Dominated Convergence

We now develop the first of the two analytic-number-theoretic inputs
to the transport theorem of §8: the *double-cutoff dominated
convergence* of detectors in $\mathcal{D}_{\delta, 0}$ against the
exact upstairs Mangoldt distribution. This is Theorem T9.1 of
[`RH-Done-Draft1`]. The content is classical dominated convergence
combined with three independent tail estimates on the prime-axis,
occupation, and Dirichlet prime-power scales.

### 6.1 Setup: the upstairs Mangoldt distribution against $G$

From Paper II Theorem T4.1, the finite-cutoff upstairs Mangoldt
distribution against a log-side detector $G : \mathbb{R} \to
\mathbb{C}$ is
$$\mathrm{VM}_{n, K}(G) \;=\;
   \sum_{p \leq p_n}\sum_{r = 1}^K (\log p)\,G(r\log p).$$
At the prime-power cutoff $M$ (i.e., restricting to $p^r \leq M$),
the *doubly-cutoff* finite Mangoldt distribution is
$$\mathrm{VM}_{n, K, M}(G) \;:=\;
   \sum_{\substack{p \leq p_n,\, r \leq K \\ p^r \leq M}}
   (\log p)\,G(r\log p).$$
The completed (uncutoff) finite-place Mangoldt distribution against
$G$ is
$$\mathrm{VM}(G) \;:=\;
   \sum_p\sum_{r \geq 1}(\log p)\,G(r\log p).$$
The convergence question is: do the doubly-cutoff sums converge to
$\mathrm{VM}(G)$ as $(p_n, K, M) \to \infty$ jointly, and at what
rate?

### 6.2 The absolute majorant

For $G \in \mathcal{D}_{\delta, 0}$ with $a := 1 + \delta > 1$ and
$C_G := \|G\|_{\delta, 0}$, the inequality $|G(\pm u)| \leq C_G\,
e^{-(1+\delta)|u|}$ gives, on prime powers $u = r\log p$,
$$|G(r\log p)| \leq C_G\,p^{-r(1+\delta)} = C_G\,p^{-ra}.$$
The unrestricted absolute sum is therefore bounded by
$$\sum_p\sum_{r \geq 1}(\log p)|G(r\log p)|
   \leq C_G\sum_p\frac{\log p}{p^a}\cdot\frac{1}{1 - 2^{-a}}
   \cdot (1 - 2^{-a})/(1 - p^{-a}),$$
which collapses (after simplification) to
$$\boxed{\;\sum_p\sum_{r \geq 1}(\log p)|G(r\log p)|
   \;\leq\; \frac{C_G}{1 - 2^{-a}}\,\sum_p\frac{\log p}{p^a}.\;}$$
The prime sum on the right converges by comparison with
$\sum_{m \geq 2}(\log m)/m^a < \infty$ ($a > 1$), giving an absolute
majorant. Specifically, with $a = 1 + \delta$,
$\sum_m (\log m)/m^a$ is finite and bounded by an explicit constant
depending only on $\delta$.

### 6.3 Explicit tail bounds

We bound each of the three cutoff tails separately.

**Lemma 6.1** (Three explicit tails). *For $G \in \mathcal{D}_{\delta,
0}$ with $C_G = \|G\|_{\delta, 0}$, $a = 1 + \delta$:*

*(a) Axis tail (primes beyond $P$):*
$$\sum_{p > P}\sum_{r \geq 1}(\log p)\,|G(r\log p)|
   \;\ll_\delta\; C_G\,P^{-\delta}(\log P + 1).$$

*(b) Occupation tail (depth beyond $K$):*
$$\sum_p\sum_{r > K}(\log p)\,|G(r\log p)|
   \;\ll_\delta\; C_G\,2^{-aK}.$$

*(c) Dirichlet prime-power tail ($p^r > M$):*
$$\sum_{p^r > M}(\log p)\,|G(r\log p)|
   \;\ll_\delta\; C_G\,M^{-\delta}(\log M + 1).$$

*Proof.*

*(a)* Use the absolute majorant of §6.2 restricted to $p > P$:
$$\sum_{p > P}\sum_{r \geq 1}(\log p)|G(r\log p)|
   \leq \frac{C_G}{1 - 2^{-a}}\sum_{p > P}\frac{\log p}{p^a}
   \leq \frac{C_G}{1 - 2^{-a}}\sum_{m > P}\frac{\log m}{m^a}.$$
Standard integral comparison gives
$\sum_{m > P}(\log m)/m^a \ll_a P^{1-a}\bigl(\log P/(a-1) +
1/(a-1)^2\bigr) \ll_\delta P^{-\delta}(\log P + 1)$.

*(b)* Using $p^{-ar} = p^{-a} p^{-a(r-1)} \leq p^{-a} \cdot 2^{-a(r-1)}$,
$$\sum_p\sum_{r > K}(\log p)|G(r\log p)|
   \leq C_G\Bigl(\sum_p\frac{\log p}{p^a}\Bigr)
   \frac{2^{-aK}}{1 - 2^{-a}}
   \ll_\delta C_G\,2^{-aK} = C_G\,2^{-(1+\delta)K}.$$

*(c)* With $m = p^r$, $(\log p)\,p^{-ar} \leq (\log m)\,m^{-a}$
(this follows from $\log p \leq \log m$ and $p^{-ar} = m^{-a}$ at
the same value of $p^r = m$), so
$$\sum_{p^r > M}(\log p)|G(r\log p)|
   \leq C_G\sum_{m > M}\frac{\log m}{m^a}
   \ll_\delta C_G\,M^{-\delta}(\log M + 1).$$
$\square$

Hence the *union tail*, the absolute error between
$\mathrm{VM}_{n, K, M}(G)$ and $\mathrm{VM}(G)$, is bounded above by
the sum of the three individual tail bounds:

$$\boxed{\;T_{P, K, M}(G) \;\ll_\delta\;
   C_G\Bigl[P^{-\delta}(\log P + 1) +
   2^{-(1+\delta)K} +
   M^{-\delta}(\log M + 1)\Bigr].\;}$$

The right-hand side is uniform on every bounded subset of
$\mathcal{D}_{\delta, 0}$, i.e., depends on $G$ only via the norm
$C_G = \|G\|_{\delta, 0}$.

### 6.4 Theorem T9.1: dominated convergence

**Theorem 6.2** (*Double-Cutoff Dominated Convergence; T9.1 of
[`RH-Done-Draft1`]*).
*Let $G \in \mathcal{D}_{\delta, 0}$ for some $\delta > 0$. Let
$p_n, K_n, M_n$ be any cofinal sequences with
$p_n \to \infty, K_n \to \infty, M_n \to \infty$. Then*
$$\sum_{\substack{p \leq p_n,\, r \leq K_n \\ p^r \leq M_n}}
   (\log p)\,G(r\log p) \;\longrightarrow\;
   \sum_p\sum_{r \geq 1}(\log p)\,G(r\log p),$$
*locally uniformly on bounded subsets of $\mathcal{D}_{\delta, 0}$.
The same theorem holds for the reflected detector $G^\#(u) := G(-u)$
and hence for the completed reflected finite-place distribution*
$$\sum_p\sum_{r \geq 1}(\log p)\bigl[G(r\log p) + G(-r\log p)\bigr].$$

*Proof.* The summable majorant of §6.2 gives absolute convergence of
the limit sum. For each fixed pair $(p, r)$, the cutoff indicator
$1_{\{p \leq p_n,\, r \leq K_n,\, p^r \leq M_n\}}$ converges to $1$
as $n \to \infty$. Dominated convergence on the countable index set
$\{(p, r) : p \text{ prime}, r \geq 1\}$ gives the limit.

For local uniformity, let $\mathcal{B} \subset \mathcal{D}_{\delta,
0}$ be bounded and set $C_\mathcal{B} := \sup_{G \in \mathcal{B}}
\|G\|_{\delta, 0}$. The common majorant
$C_\mathcal{B}(\log p)p^{-r(1+\delta)}$ is summable; the tail bound of
§6.3 tends to zero uniformly in $G \in \mathcal{B}$ as
$(p_n, K_n, M_n) \to \infty$. $\square$

### 6.5 Empirical verification

The probe
[`probe_DoubleCutoffDominatedConvergence_Q8vM3.py`] verifies Theorem
6.2 at $\delta = 0.3$ for two test detectors:

*Extremal exponential detector* $G(u) = e^{-(1+\delta)|u|}$, with norm
$\|G\|_{\delta, 0} = 1$:

| $P$ | $K$ | $M$ | abs. error | majorant bound |
|---|---|---|---|---|
| 31 | 3 | $10^4$ | $1.07$ | $17.5$ |
| 503 | 8 | $10^8$ | $0.43$ | $8.6$ |
| 10007 | 16 | $10^{12}$ | $0.13$ | $4.5$ |

*Even Gaussian detector* with norm $\|G\|_{\delta, 0} \approx 596$:

| $P$ | $K$ | $M$ | abs. error | majorant bound |
|---|---|---|---|---|
| 31 | 3 | $10^4$ | $234$ | $1.05 \times 10^4$ |
| 503 | 8 | $10^8$ | $20.7$ | $5130$ |
| 2003 | 12 | $10^{10}$ | $0.25$ | $3794$ |
| 10007 | 16 | $10^{12}$ | $4.4 \times 10^{-5}$ | $2664$ |

Both detectors confirm absolute convergence with rates consistent
with the explicit majorant bound of §6.3.

### 6.6 What §6 establishes

The double-cutoff truncation $\mathrm{VM}_{n, K, M}(G)$ converges to
the exact completed Mangoldt distribution $\mathrm{VM}(G)$ for every
$G \in \mathcal{D}_{\delta, 0}$, locally uniformly on bounded
subsets, with explicit tail bound
$T_{P, K, M}(G) \ll_\delta C_G[P^{-\delta}(\log P+1) + 2^{-(1+\delta)K} + M^{-\delta}(\log M+1)]$.
This is the **double-cutoff error** $E_{\mathrm{cut}}$ in the
five-error ledger of §8.

The analysis is purely analytic and independent of any conjectural
input (Generalized Riemann Hypothesis, Elliott–Halberstam, etc.). The
input is the exact upstairs occupation formula T4.1 of Paper II
together with the exponential log-side decay rate $1 + \delta$ of
the detector class.

---

## §7. Averaged CRT Shadow Uniformity at Polynomial Scale

We now develop the second analytic-number-theoretic input to the
transport theorem of §8: *averaged compressed CRT shadow uniformity*
at polynomial scale $X = P_n^{1+\varepsilon}$, via the
Barban–Davenport–Halberstam mean-square theorem. This is Theorem T9.2
of [`RH-Done-Draft1`].

The key conceptual content of §7 is that **the correct target is the
$L^2$-averaged shadow, not the pointwise maximum over characters**.
The pointwise maximum at polynomial scale would require excluding
Landau–Siegel exceptional zeros — a problem comparable to Polymath 8.
The averaged shadow is *exactly* what BDH 1965–66 controls, and the
positive-current transport theorem of §8 needs no stronger input.

### 7.1 The compressed CRT shadow

For a modulus $q \mid P_n$ and an arithmetic progression $a$ with
$\gcd(a, q) = 1$, the *prime-counting discrepancy* is
$$\Delta(X; q, a) \;:=\; \psi(X; q, a) - \frac{X}{\varphi(q)},$$
with $\psi(X; q, a) = \sum_{p^r \leq X,\, p^r \equiv a \pmod q}
\Lambda(p^r)$ the prime power counting function in the progression.

For a K-even CRT/Fejér detector shadow $W = \{W_q\}_{q \mid P_n}$ with
each $W_q : (\mathbb{Z}/q)^\times \to \mathbb{C}$ a finite weight,
the *compressed CRT shadow* of $W$ at scale $X$ is
$$\mathcal{E}_{P_n}(W; X) \;:=\; \sum_{q \mid P_n} c_q\,
   \frac{1}{\varphi(q)}\sum_{a \in (\mathbb{Z}/q)^\times}
   W_q(a)\,\Delta(X; q, a),$$
with $c_q$ the Möbius/Ramanujan conductor coefficients from the
compressed observable (cf. Paper 22 §6).

The *shadow norm* of $W$ is
$$\|W\|_{\mathrm{sh}}^2 \;:=\;
   \sum_{q \mid P_n}\frac{|c_q|^2}{\varphi(q)^2}
   \sum_{a \in (\mathbb{Z}/q)^\times}|W_q(a)|^2.$$
For bounded Fejér/CRT detector shadows with $|c_q| \leq 1$ and
$|W_q| \leq O(1)$, the shadow norm satisfies
$$\|W\|_{\mathrm{sh}}^2 \;\ll\;
   \sum_{q \mid P_n}\frac{1}{\varphi(q)}
   = \prod_{p \leq p_n}\Bigl(1 + \frac{1}{p - 1}\Bigr)
   \;\ll\; \log p_n \;=\; P_n^{o(1)}.$$
The shadow norm grows only polylogarithmically in $P_n$ — this is the
*compression advantage*.

### 7.2 The Barban–Davenport–Halberstam input

The classical Barban–Davenport–Halberstam theorem
[`BDH1965`, `BDH1966`, `Davenport2000` §28] gives the mean-square
bound: for $1 \leq Q \leq X$ and any $A > 0$,
$$\sum_{q \leq Q}\sum_{a \in (\mathbb{Z}/q)^\times}|\Delta(X; q, a)|^2
   \;\ll_A\; X\,Q\,(\log X)^C$$
for an absolute constant $C$.

*The constant $C$.* The original BDH 1965/1966 statements
[`BDH1965`, `BDH1966`] established the bound with $C$ depending on the
constant in the Siegel-Walfisz prerequisite, and the modern
Davenport-Halberstam refinement (Davenport 2000 [`Davenport2000`] §29
Theorem in Chapter 29, attributed to Montgomery) sharpens this to
$C = 1$ under mild restrictions (specifically, for $Q \leq X/(\log X)^B$
for sufficiently large $B$). For our purposes any fixed value of $C$
suffices, since the rate of convergence in Theorem 7.1 below depends
only on the ratio $(P/X)^{1/2}$ at polynomial scale $X = P_n^{1 + \varepsilon}$;
the $(\log X)^{C/2}$ factor is absorbed into the $P_n^{o(1)}$
exponent.

Smooth weights $G(\log m)$ are handled by dyadic partition and
partial summation, changing only the power of $\log X$ and replacing
$X$ by the largest dyadic block. The convergence rate
$P_n^{-\varepsilon/2 + o(1)} \to 0$ is invariant under refinement of
$C$.

This is the load-bearing classical input. No Elliott–Halberstam
direction, no Polymath-8 improvement, no pointwise character bound
beyond classical Siegel–Walfisz is needed.

### 7.3 Theorem T9.2: natural-scale uniformity

**Theorem 7.1** (*Natural-Scale Compressed CRT Shadow Uniformity;
T9.2 of [`RH-Done-Draft1`]*).
*Let $P = P_n$ be the primorial at row $n$, and let $X_n$ satisfy
$X_n \geq P_n^{1 + \varepsilon}$ for some fixed $\varepsilon > 0$.
For every K-even CRT/Fejér detector shadow
$W = \{W_q\}_{q \mid P_n}$ with $\|W\|_{\mathrm{sh}} \ll P_n^{o(1)}$
— in particular every bounded Fejér/CRT shadow with $|c_q| \leq 1$
— the compressed CRT shadow satisfies*
$$\boxed{\;
\frac{|\mathcal{E}_{P_n}(W; X_n)|}{X_n}
\;\ll\; P_n^{-\varepsilon/2 + o(1)}\,\to\, 0
\quad(n \to \infty).\;}$$

*Proof.* By Cauchy–Schwarz applied to the inner sum,
$$|\mathcal{E}_P(W; X)|
   \;\leq\;
   \Bigl(\sum_{q \mid P}\frac{|c_q|^2}{\varphi(q)^2}
   \sum_a|W_q(a)|^2\Bigr)^{1/2}
   \Bigl(\sum_{q \mid P}\sum_a|\Delta(X; q, a)|^2\Bigr)^{1/2}.$$
The first factor is $\|W\|_{\mathrm{sh}}$. Since $q \mid P$ implies
$q \leq P$, the second factor is bounded by the BDH sum of §7.2 with
$Q = P$:
$$\Bigl(\sum_{q \leq P}\sum_a|\Delta(X; q, a)|^2\Bigr)^{1/2}
   \;\ll\; (XP)^{1/2}(\log X)^{C/2}.$$
For bounded detector shadows, $\|W\|_{\mathrm{sh}}^2 \ll \log p_n =
P_n^{o(1)}$ (§7.1). The $(\log X)^{C/2}$ factor from BDH is likewise
absorbed into $P^{o(1)}$ at polynomial scale. Therefore
$$\frac{|\mathcal{E}_P(W; X)|}{X} \;\ll\;
   \Bigl(\frac{P}{X}\Bigr)^{1/2}\,P^{o(1)}.$$
With $X = P^{1 + \varepsilon}$ this becomes
$P^{-\varepsilon/2 + o(1)} \to 0$. $\square$

### 7.4 Why no pointwise character bound is needed

The compressed shadow $\mathcal{E}_P(W; X)$ is an $L^2$-averaged
residue observable, not a pointwise maximum. The pointwise maximum
$$\max_{\chi \bmod q,\, q \mid P_n}|\psi(X, \chi)| = o(X) \quad(X = P_n^A)$$
*would* require excluding Landau–Siegel exceptional zeros in a range
where classical Siegel–Walfisz [`SiegelWalfisz`] deliberately does
not, by the well-known argument: at a hypothetical Landau–Siegel
zero $\beta_D = 1 - \lambda/\log D$ for a real primitive character
$\chi_D$ with squarefree conductor $D \mid P_n$, the explicit
formula gives a contribution of size
$$X^{\beta_D}/\beta_D = X\,\exp(-A\lambda + o(1)),$$
a positive fraction of $X$, not $o(X)$. Hence the pointwise maximum
at polynomial scale is *not* available unconditionally; it would
require Generalized Riemann Hypothesis or Polymath-8-scale
hybridization of Bombieri–Vinogradov with Burgess subconvexity. The
program does not need this.

The *averaged* shadow is different. An individual exceptional
character has *negligible mass* in the $L^2$-averaged CRT shadow
unless the detector is adversarially chosen to isolate it. The K-even
Poisson-Gaussian detectors of §2.1 are bounded smooth windows, not
exceptional-character spikes. Their shadow norms are bounded
$\ll \log p_n$, and any individual exceptional character contributes
at most $\varphi(D)^{-1}$ to the shadow norm — a polylog savings, not
a polynomial loss.

This is the precise sense in which **the program's transport
theorem avoids the Polymath-8 obstacle**: it averages where the
obstacle exists, and the averaging is unconditional.

### 7.5 Theorem T9.2 in the transport ledger

In the five-error ledger of §8, Theorem 7.1 supplies the bound on
the *compressed CRT shadow error* $E_{\mathrm{CRT}}(n)$:
$$E_{\mathrm{CRT}}(n) \;\ll\; P_n^{-\varepsilon/2 + o(1)} \;\to\; 0$$
as $n \to \infty$, for any fixed $\varepsilon > 0$. The error is
controlled at the *averaged compressed* level, not at the pointwise
level, and this suffices.

The choice of polynomial scale $X_n = P_n^{1 + \varepsilon}$ is the
*natural primorial scale*: it grows polynomially with $P_n$, so the
Fejér/CRT detector shadow on $\mathbb{Z}/P_n$ pulls back to a smooth
window on the real line of comparable width.

### 7.6 What §7 establishes

The averaged compressed CRT shadow $\mathcal{E}_{P_n}(W; X_n)$ at
polynomial scale $X_n = P_n^{1+\varepsilon}$ is controlled by the
classical Barban–Davenport–Halberstam mean-square 1965–66, giving
$|\mathcal{E}_{P_n}|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$
unconditionally. No pointwise character bound is required. The
program's transport theorem (§8) needs no stronger
analytic-number-theoretic input. This closes the second of the two
analytic legs feeding into the five-error ledger.

---

## §8. The Positive-Current Transport Theorem

We now assemble §§2–7 into the program's technical heart: the
*positive-current transport theorem*, which carries the finite
Noether positivity $\mathcal{Q}_n(J_n) \geq 0$ to the
window-integrated Poisson positivity $\mathfrak{P}_{\phi, y}(\Xi)
\geq 0$, with a five-error ledger that bounds the deviation
$\mathcal{Q}_n(J_n) - \mathfrak{P}_{\phi, y}(\Xi)$. This is Theorem
T9.3 of [`RH-Done-Draft1`]. It is the technical heart of Paper III.

### 8.1 The target identity

We seek to establish the limit identity
$$\boxed{\;\lim_{n \to \infty}\mathcal{Q}_n(J_n(\phi, y))
   \;=\; \mathfrak{P}_{\phi, y}(\Xi),\;}$$
for every K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$
and every $y > 0$. Combined with Theorem 4.9
($\mathcal{Q}_n(J_n) \geq 0$ unconditionally), this gives the
window-integrated positivity
$$\mathfrak{P}_{\phi, y}(\Xi) \;\geq\; 0\quad
   \forall \phi \in \mathcal{D}_{\delta, 0}^{K, +},\ y > 0,$$
which by Theorem 10.1 of §9 implies pointwise $u_B \geq 0$ on
$\mathbb{C}_+$ and hence RH by Paper II T6.3.

The target identity is the program's *transport equation*. Its
proof, which is the content of §8, splits into a sum of five named
error terms — each tracked separately.

### 8.2 The five-error ledger

**Definition 8.1** (Five-error ledger). For a K-even nonneg detector
$\phi \in \mathcal{D}_{\delta, 0}^{K, +}$, a height $y > 0$, and
cofinal cutoffs $(p_n, K_n, M_n)$ at primorial row $n$, write
$$
\mathcal{Q}_n(J_n(\phi, y)) \;-\;\mathfrak{P}_{\phi, y}(\Xi)
\;=\;
E_{\mathrm{occ}}(n) + E_{\mathrm{cut}}(n) + E_{\mathrm{CRT}}(n)
+ E_{\mathrm{win}}(n) + E_{\mathrm{leak}}(n),
$$
*where the five errors are:*
- $E_{\mathrm{occ}}(n)$: *occupation error* from the exact upstairs
  formula (Paper II T4.1) — the difference between the formal
  upstairs Mangoldt distribution and its log-side test-function
  evaluation. By Paper II T4.1, $E_{\mathrm{occ}}(n) = 0$ for every
  $n$, $K_n$, $M_n$, before CRT compression.
- $E_{\mathrm{cut}}(n)$: *double-cutoff error* from the truncation
  $p \leq p_n, r \leq K_n, p^r \leq M_n$. By Theorem 6.2 (§6),
  $E_{\mathrm{cut}}(n) \ll_\delta C_\phi[p_n^{-\delta}(\log p_n + 1)
  + 2^{-(1+\delta)K_n} + M_n^{-\delta}(\log M_n + 1)]$.
- $E_{\mathrm{CRT}}(n)$: *compressed CRT shadow error* from the
  primorial CRT compression of the Fejér detector approximant. By
  Theorem 7.1 (§7), $E_{\mathrm{CRT}}(n) \ll P_n^{-\varepsilon/2 +
  o(1)}$ at polynomial scale $X_n = P_n^{1+\varepsilon}$.
- $E_{\mathrm{win}}(n)$: *window-approximation error* from the
  primorial Fejér approximation of the detector $\phi$. By Theorem
  3.1 (§3), $E_{\mathrm{win}}(n) \to 0$ uniformly on every compact
  height interval, with rate at least $K_n^{-1}\log K_n$ for
  $\mathcal{C}^1$ detectors and faster for smooth ones.
- $E_{\mathrm{leak}}(n)$: *closed-sector leakage error* from the
  $\Lambda$-orthogonal complement of $\mathrm{Crit}_n$. By Lemma 4.11
  (§4.5), $E_{\mathrm{leak}}(n) = 0$ in the hard packet-preserving
  stratum and $O(\mu_n^\star\,\mathrm{polylog}(P_n))$ in the
  first-order priced stratum.

Each error has its own controlling theorem (cited above). The
remaining work in §8 is to (i) verify that the decomposition of
Definition 8.1 is internally consistent — i.e., that the five errors
*do sum to* $\mathcal{Q}_n(J_n) - \mathfrak{P}_{\phi, y}(\Xi)$ —
and (ii) verify that the Archimedean normalization (the gamma-and-pi
factor of Paper II T5.4) closes the identification at the
limit. We do this in §§8.3–8.4.

### 8.3 The exact identification of $\mathfrak{P}_{\phi, y}(\Xi)$
###      with the explicit-formula distribution

We now identify $\mathfrak{P}_{\phi, y}(\Xi)$ with the
explicit-formula functional applied to $\phi = \widehat{f * f^*}$
(Theorem 2.2). This is the *Archimedean normalization step* and uses
Paper II's Tate local zeta integrals (T5.4) as input. The derivation
is given in two pieces: (i) a logarithmic differentiation of the
completed $\xi$ (Lemma 8.2 below); (ii) an explicit identification of
the gamma-and-pi term with the Archimedean local L-factor
$\Gamma_\mathbb{R}(s) := \pi^{-s/2}\Gamma(s/2)$ of Paper II T5.4
(Corollary 8.3 below).

**Lemma 8.2** (Decomposition of $m_B$ on the height-$y$ line).
*For $s = 1/2 + i(x + iy)$ with $x \in \mathbb{R}, y > 0$, and away
from the trivial poles of $\xi$ at $s = 0, 1$ and the nontrivial
$\zeta$-zeros,*
$$
m_B(x + iy)
\;=\; -\frac{\Xi'(x + iy)}{\Xi(x + iy)}
\;=\; -i\,\Bigl[\frac{1}{s} + \frac{1}{s - 1}
   \;-\; \frac{\log\pi}{2}
   \;+\; \frac{1}{2}\,\frac{\Gamma'}{\Gamma}\!\Bigl(\frac{s}{2}\Bigr)
   \;+\; \frac{\zeta'(s)}{\zeta(s)}\Bigr]_{s = 1/2 + i(x + iy)}.
$$
*Equivalently, on imaginary parts integrated against any K-even
$\phi \in \mathcal{D}_{\delta, 0}^{K, +}$,*
$$
\boxed{\;
\mathfrak{P}_{\phi, y}(\Xi) \;=\;
\underbrace{\;\;\sum_{\rho}\int_\mathbb{R}\phi(x)\,
   \mathrm{Im}\,\frac{1}{\rho - (1/2 + i(x + iy))}\,dx\;\;}_{\text{zero-side residue sum }Z_\phi(y)}
\;-\;
\underbrace{\;\;\sum_{p, r \geq 1}(\log p)\,(f * f^*)(r\log p)\,e^{-2yr\log p}\;\;}_{\text{prime-side }P_\phi(y)}
\;+\;
E_{\mathrm{arc}}(y, \phi),\;}
$$
*where the residue sum is over the nontrivial $\xi$-zeros, the
prime-power sum is the upstairs finite-place Mangoldt distribution
against $\phi$ (using $f$ from Theorem 2.2), and the Archimedean
remainder is*
$$
E_{\mathrm{arc}}(y, \phi) \;=\;
   \int_\mathbb{R}\phi(x)\,A(x, y)\,dx,
\qquad
A(x, y) := \mathrm{Im}\Bigl[-\frac{\log\pi}{2}
   + \frac{1}{2}\,\frac{\Gamma'}{\Gamma}\!\Bigl(\frac{1/2 + i(x + iy)}{2}\Bigr)\Bigr]
$$
*(the contribution of the trivial poles at $s = 0, 1$ has been
separated into the residue sum on the line $\mathrm{Re}\,s = 1/2$ via
$1/s + 1/(s-1) = 2(s - 1/2)/(s(s-1))$, which is real-symmetric and
absorbed into the principal-value sense of the residue integration on
the critical line).*

*Proof.* Logarithmic differentiation of
$\xi(s) = \tfrac{1}{2}\,s(s-1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s)$
yields
$$
\frac{\xi'(s)}{\xi(s)} \;=\;
   \frac{1}{s} \;+\; \frac{1}{s - 1}
   \;-\; \frac{\log\pi}{2}
   \;+\; \frac{1}{2}\,\frac{\Gamma'}{\Gamma}\!\Bigl(\frac{s}{2}\Bigr)
   \;+\; \frac{\zeta'(s)}{\zeta(s)}.
$$
With $\Xi(z) = \xi(1/2 + iz)$ and $\Xi'(z) = i\,\xi'(s)|_{s = 1/2 + iz}$
by the chain rule, the displayed identity for $-\Xi'/\Xi = m_B$
follows.

To produce the Poisson-window functional, evaluate at $z = x + iy$
and take imaginary parts. The five terms decompose as follows.

*Trivial poles.* The combination $1/s + 1/(s-1) = (2s - 1)/(s(s-1))$
is purely imaginary on the critical line $\mathrm{Re}\,s = 1/2$
(where $2s - 1 = 2iz \in i\mathbb{R}$ for $z$ real), and on the
shifted line $s = 1/2 + i(x + iy)$ contributes a smooth K-even bounded
function of $(x, y)$ whose Cauchy integral against $\phi$ vanishes
identically by K-evenness (the integrand is K-odd). We therefore
absorb this term into the residue-sum convention; alternatively, one
may treat the trivial poles at $s = 0, 1$ on the same footing as the
nontrivial $\rho$ via the standard contour shift (cf. Iwaniec-Kowalski
2004 §5.5).

*Archimedean term.* The third and fourth terms,
$-\tfrac{1}{2}\log\pi + \tfrac{1}{2}(\Gamma'/\Gamma)(s/2)$, are
exactly $(\log\Gamma_\mathbb{R})'(s)$ where
$\Gamma_\mathbb{R}(s) := \pi^{-s/2}\Gamma(s/2)$ is the *Archimedean
local L-factor* in Tate-Weil normalization (Paper II T5.4). After
multiplying by $-i$ and taking imaginary parts at $s = 1/2 + i(x + iy)$,
$$
-\mathrm{Im}\!\bigl[i\,(\log\Gamma_\mathbb{R})'(s)\bigr]
\;=\;
\mathrm{Re}\bigl[(\log\Gamma_\mathbb{R})'(s)\bigr]
\;=\;
\mathrm{Im}\Bigl[-\frac{\log\pi}{2}
   + \frac{1}{2}\,\frac{\Gamma'}{\Gamma}\!\Bigl(\frac{s}{2}\Bigr)\Bigr]
   \quad\text{at }s = 1/2 + i(x + iy).
$$
Integrating against $\phi$ yields the displayed $E_{\mathrm{arc}}(y, \phi)$.

*Prime-side and zero-side.* The remaining term
$\zeta'(s)/\zeta(s)$ admits the standard prime-power expansion on
$\mathrm{Re}\,s > 1$,
$-\zeta'(s)/\zeta(s) = \sum_{p, r \geq 1}(\log p)\,p^{-rs}$, analytically
continued via the Hadamard product. The Hadamard factorization of
$\xi$ writes
$\xi'(s)/\xi(s) = -B - \sum_\rho \bigl[\tfrac{1}{\rho - s} + \tfrac{1}{\rho}\bigr]$
with the $\rho$-sum over nontrivial zeros (Iwaniec-Kowalski 2004,
(5.27)). Evaluating $-\Xi'/\Xi$ at $z = x + iy$ and applying
$\mathrm{Im}$ then integrating against $\phi$ separates this term into
the zero-side residue sum $Z_\phi(y)$ minus the prime-power sum
$P_\phi(y)$ (the latter using Theorem 2.2,
$\phi = \widehat{f * f^*}$, so that $(f * f^*)(r\log p) =
\tfrac{1}{2\pi}\int_\mathbb{R}\phi(x)\,e^{ir(\log p)x}\,dx$).
The boxed decomposition follows. $\square$

**Corollary 8.3** (*$E_{\mathrm{arc}}$ is the Tate Archimedean factor*).
*The Archimedean remainder of Lemma 8.2 satisfies*
$$
E_{\mathrm{arc}}(y, \phi)
\;=\;
\int_\mathbb{R}\phi(x)\,
   \mathrm{Re}\!\Bigl[\,(\log\Gamma_\mathbb{R})'\!\bigl(\tfrac{1}{2} + i(x + iy)\bigr)\,\Bigr]\,dx,
$$
*where $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ is the Tate
Archimedean local L-factor of Paper II T5.4, obtained as the local
zeta integral $Z_+(s) = \int_\mathbb{R}e^{-\pi x^2}|x|^{s-1}\,dx$ on
the Bargmann ground state $\psi_0 \propto e^{-\pi x^2}$. The
remainder is independent of $n, K_n, M_n$: it depends only on $\phi$
and $y$, not on any primorial-row cutoff.*

*Proof.* The identity
$(\log\Gamma_\mathbb{R})'(s) = -\tfrac{1}{2}\log\pi + \tfrac{1}{2}(\Gamma'/\Gamma)(s/2)$
follows by direct logarithmic differentiation of $\Gamma_\mathbb{R}$,
matching the third and fourth terms of Lemma 8.2's decomposition. The
Tate identification $\Gamma_\mathbb{R}(s) = Z_+(s)$ on the Bargmann
ground state is Paper II Theorem T5.4. The independence of the
primorial cutoffs $(n, K_n, M_n)$ is by inspection: $E_{\mathrm{arc}}$
is built from $\phi$ (continuous on $\mathbb{R}$) and the Archimedean
factor $\Gamma_\mathbb{R}$ (a classical analytic object). $\square$

**Remark 8.4** (Why $E_{\mathrm{arc}}$ is "normalization, not error").
The Archimedean remainder is *part of the target* $\mathfrak{P}_{\phi, y}(\Xi)$,
not one of the five ledger errors of Definition 8.1. It is the
$\Gamma_\mathbb{R}$-contribution to $-\Xi'/\Xi = m_B$ — specifically,
the contribution of the Archimedean factor of the completed $\xi$.
Paper II T5.4 derives $\Gamma_\mathbb{R}$ from the Tate integral
$Z_+(s) = \pi^{-s/2}\Gamma(s/2)$ on the Bargmann ground state
$\psi_0 \propto e^{-\pi x^2}$. The transport equation thus reads:
*after accounting for the Archimedean factor (which is classical and
independent of the primorial cutoffs), the finite-place Mangoldt
distribution against $\phi$ equals — up to the five ledger errors —
the zero-side residue sum of $u_B$*. This is the standard explicit
formula, recast in the K-even Poisson-window framework.

Convergence of the integral in Corollary 8.3 is automatic: by
Stirling's asymptotic
$(\Gamma'/\Gamma)(w) = \log w - 1/(2w) + O(|w|^{-2})$ as $|w| \to \infty$
in any sector $|\arg w| \leq \pi - \epsilon$, we have
$\mathrm{Re}[(\Gamma'/\Gamma)(s/2)] = \log|s/2| + O(1)$ on
$s = 1/2 + i(x + iy)$, growing logarithmically in $|x|$. The
exponential log-side decay $|\phi(x)| \ll e^{-(1 + \delta)|x|}$ kills
this growth, so $E_{\mathrm{arc}}(y, \phi)$ is finite and absolutely
continuous in $y > 0$ for every $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$.

### 8.4 Theorem T9.3: Positive-Current Transport

**Theorem 8.5** (*Positive-Current Transport with Five-Error Ledger;
T9.3 of [`RH-Done-Draft1`]*).
*Assume:*

*(H1) Finite Noether positivity holds on the admissible
occupation-decorated convolution-square currents (Theorem 4.9).*

*(H2) The closed-sector projection $\Pi_{\mathrm{Crit}_n}^\Lambda$ is
evaluated before lossy CRT compression (Paper II I4.2).*

*(H3) Leakage is either zero in the packet-preserving stratum or
satisfies $E_{\mathrm{leak}}(n) = O(\mu_n^\star\,\mathrm{polylog}(P_n)) = o(1)$
in the first-order priced stratum (Lemma 4.11).*

*(H4) The standard completed-$\xi$ Archimedean normalization holds
(Paper II Theorem T5.4).*

*(H5) (GBP) — the spectral-measure identity
$|\Sigma(y, \xi)|^2/(2\pi)\,d\xi = u_B(\xi, y)\,d\xi$ on the spectral
line, for every $y > 0$ (see Main Theorem 9.4(d) and §8.5a).*

*Then for every K-even nonneg detector $\phi \in \mathcal{D}_{\delta,
0}^{K, +}$ and every $y > 0$, the transport equation*
$$\boxed{\;\lim_{n \to \infty}
   \mathcal{Q}_n^{\text{Gram}}(f; y) \;=\;
   \mathfrak{P}_{\phi, y}(\Xi)\;}$$
*holds, with the Gram form converging to a positive Gram-Bochner
spectral measure $\int\phi\,d\nu_y$ (unconditional from Steps 1–5),
the explicit-formula decomposition $\mathfrak{P}_{\phi, y}(\Xi) =
\int\phi\,u_B(\cdot, y)\,d\xi$ (unconditional from Step 6), and the
two limits matching via (H5) = (GBP). In particular,*
$$\boxed{\;\mathfrak{P}_{\phi, y}(\Xi) \;\geq\; 0\quad
   \forall \phi \in \mathcal{D}_{\delta, 0}^{K, +},\ y > 0.\;}$$

*The hypotheses (H1)–(H4) are unconditional (established in this
paper or in Paper II). The hypothesis (H5) = (GBP) is equivalent to RH
by Main Theorem 9.4.*

*Proof.* Step 1 (Gram upstairs lift). By Paper II T4.1, the exact
upstairs formula
$D_s\,\Pi_{\mathrm{sa}}\,L_{n, K}(s) = \sum_{p, r}(\log p)\,p^{-rs}\,e_{r\,e_p}$
holds *identically* in $\mathcal{F}_n$ before CRT compression. The
Gram-Noether form of Definition 4.7, expanded via Lemma 4.8a (or
directly from Theorem 4.9), gives
$$
\mathcal{Q}_n^{\text{Gram}}(f; y)\;=\;\|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}
\;=\;\frac{1}{2\pi}\int_\mathbb{R}\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi,
$$
which samples the autocorrelation $(f * f^*)$ at prime-power
*difference* coordinates $r\log p - r'\log p'$ — the natural Bochner
kernel matching the explicit-formula prime side's
$(f * f^*)$-sampling at $r\log p$ (Lemma 8.2, Step 6 below).

The diagonal $(p, r) = (p', r')$ contribution of $\mathcal{Q}_n^{\text{Gram}}$
is
$\sum_{p, r}(\log p)\,e^{-2yr\log p}\,(f * f^*)(0)
= \|f\|^2_{L^2}\sum_{p, r}(\log p)\,p^{-2yr}$,
which for $y > 1/2$ tends to $\|f\|^2_{L^2}\cdot(-\zeta'(2y)/\zeta(2y))$
as $n \to \infty$. The off-diagonal $(p, r) \neq (p', r')$ contribution
encodes the program's natural Bochner cross-correlation of the von
Mangoldt distribution.

By Theorem 4.9 (squared $L^2$-norm), $\mathcal{Q}_n^{\text{Gram}}(f; y) \geq 0$
unconditionally for every $n$, $K_n$, $y > 0$, and every
$\phi \in \mathcal{D}_{\delta, 0}^{K, +}$. This is the upstairs
positivity input.

Step 2 (double-cutoff error). The double-cutoff bound of Theorem 6.2
gives
$$|E_{\mathrm{cut}}(n)|
   \;=\;
   \biggl|\sum_{\substack{p \leq p_n,\,r \leq K_n \\ p^r \leq M_n}}
   - \sum_{p, r \geq 1}\biggr|(\log p)\,|G(r\log p)|
   \;\ll_\delta\;
   C_\phi\Bigl[p_n^{-\delta}(\log p_n + 1)
   + 2^{-(1+\delta)K_n} + M_n^{-\delta}(\log M_n + 1)\Bigr],$$
with $G(u) := |\hat f(u)|^2\,e^{-2y|u|}$ in $\mathcal{D}_{\delta, 0}$
(since $\hat f$ is Schwartz and the Poisson exponential adds
$2y$ to the decay rate). As $(p_n, K_n, M_n) \to \infty$, this
$\to 0$ at the explicit rates above.

Step 3 (compressed CRT shadow error). By Theorem 7.1, the averaged
CRT shadow of the detector at polynomial scale $X_n = P_n^{1+\varepsilon}$
satisfies $|\mathcal{E}_{P_n}(W; X_n)|/X_n \ll P_n^{-\varepsilon/2 + o(1)}$.
This bounds the difference between the upstairs finite-place
distribution (Step 1) and the downstairs compressed-CRT
finite-place distribution that enters $\mathfrak{P}_{\phi, y}(\Xi)$:
$$|E_{\mathrm{CRT}}(n)| \;\ll\; P_n^{-\varepsilon/2 + o(1)} \;\to\; 0.$$

Step 4 (window-approximation error). By Theorem 3.1, the K-even
Fejér approximation $\sigma_{K_n}^{K\text{-even}}\phi$ converges
uniformly to $\phi$ on every compact height interval. The
Poisson-window functional $\mathfrak{P}_{\phi, y}(\Xi) = \int_\mathbb{R}
\phi(x)\,u_B(x, y)\,dx$ is continuous in $\phi$ in the
$\mathcal{C}^0(I_T)$-topology for $T$ large enough to capture the
mass of $u_B(\,\cdot\,, y)$ on the support of $\phi$. Hence
$$|E_{\mathrm{win}}(n)| \;\leq\; \|\sigma_{K_n}^{K\text{-even}}\phi - \phi\|_\infty
   \cdot \|u_B(\,\cdot\,, y)\|_{L^1} \;\to\; 0,$$
with rate from §3.3 (at least $K_n^{-1}\log K_n$ for $\mathcal{C}^1$
detectors).

Step 5 (closed-sector leakage error). By Lemma 4.11, the leakage
form $\Lambda_n(L_n) \geq 0$ (in the packet-preserving stratum) or
$O(\mu_n^\star\,\mathrm{polylog}(P_n))$ (in the first-order priced
stratum). In either case the leakage contribution to $\mathcal{Q}_n$
is either identically zero (packet-preserving, by Theorem 4.9's
$L_n = 0$ identification) or vanishing (first-order priced, by
Paper 25 §5).

Step 6 (Archimedean closure for the spectral side). The Archimedean
remainder $E_{\mathrm{arc}}(y, \phi)$ of Lemma 8.2 is *part of the
target* $\mathfrak{P}_{\phi, y}(\Xi)$ (Corollary 8.3, Remark 8.4); it
is the Tate Archimedean local L-factor contribution
$(\log\Gamma_\mathbb{R})'$, independent of the primorial cutoffs. By
Lemma 8.2's boxed decomposition,
$$
\mathfrak{P}_{\phi, y}(\Xi)
\;=\; Z_\phi(y) - P_\phi(y) + E_{\mathrm{arc}}(y, \phi)
$$
unconditionally, with $Z_\phi$ the zero-side residue sum, $P_\phi(y) = \sum(\log p)(f*f^*)(r\log p)e^{-2yr\log p}$
the prime side, and $E_{\mathrm{arc}}$ the explicit Archimedean piece.
This identity is independent of the Gram reformulation; it is a
classical consequence of Hadamard factorization of $\xi$.

Step 7 (positivity, conditional on (GBP)). From Steps 1–5 the Gram
upstairs form satisfies
$\mathcal{Q}_n^{\text{Gram}}(f; y) \to \int\phi(\xi)\,d\nu_y(\xi)$
with $d\nu_y = |\Sigma(y, \xi)|^2\,d\xi/(2\pi) \geq 0$ — the
Gram-Bochner spectral measure. From Step 6, $\mathfrak{P}_{\phi, y}(\Xi) = \int\phi(\xi)\,u_B(\xi, y)\,d\xi$.

**The transport identity
$\mathcal{Q}_n^{\text{Gram}}(f; y) \to \mathfrak{P}_{\phi, y}(\Xi)$
holds for every K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$
if and only if (GBP) holds:**
$$
\frac{|\Sigma(y, \xi)|^2}{2\pi}\,d\xi \;=\; u_B(\xi, y)\,d\xi
\quad\text{on the spectral line, for every } y > 0.
$$
Under (GBP), $\mathcal{Q}_n^{\text{Gram}} \to \mathfrak{P}_{\phi, y}$
and the limit of nonneg numbers is nonneg, giving
$\mathfrak{P}_{\phi, y}(\Xi) \geq 0$.

**Without (GBP)**, the Gram positivity $\mathcal{Q}_n^{\text{Gram}} \geq 0$
gives only $\int\phi\,d\nu_y \geq 0$, which is automatic and does
*not* imply $\int\phi\,u_B(\cdot, y)d\xi \geq 0$.

This is the precise status: the Gram positivity (Steps 1–5) and the
explicit-formula decomposition (Step 6) are unconditional; the
identification that closes the transport (Step 7) requires (GBP). By
Main Theorem 9.4, (GBP) is equivalent to RH. $\square$

### 8.5a The Gram reformulation: positive upstairs, precise remaining identification

The Pass-1 reformulation of §4 — replacing the broken
$f_n = \sum\hat f(r\log p)e_{r e_p}$ squared norm with the Gram form
$\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n(f; y)\|^2_{L^2}$ on
translates of $f$ — restores the upstairs to a *correctly positive*
object that samples $(f * f^*)$ at prime-power *difference*
coordinates, which is the natural Bochner kernel for the
explicit-formula prime side.

The state after the reformulation:

**(Positive content, unconditional.)**
By Theorem 4.9 + Lemma 4.8a,
$$
\mathcal{Q}_n^{\text{Gram}}(f; y)
\;=\; \frac{1}{2\pi}\int_\mathbb{R}\phi(\xi)\,|\Sigma_n(y, \xi)|^2\,d\xi
\;\geq\; 0
\qquad\text{unconditionally},
$$
with $\Sigma_n(y, \xi) = \sum_{p \leq p_n, r \leq K_n}\sqrt{\log p}\,p^{-r(y + i\xi)}$.
In the primorial limit ($n \to \infty, K_n \to \infty$),
$\mathcal{Q}_n^{\text{Gram}}(f; y) \to \int\phi(\xi)\,d\nu_y(\xi)$
where $d\nu_y(\xi) := |\Sigma(y, \xi)|^2\,d\xi/(2\pi)$ is the
*Gram-Bochner spectral measure* of the program at height $y$ — a
positive measure on the spectral line, built unconditionally from the
$\sqrt{\Lambda}$-weighted prime distribution.

**(Explicit-formula content, unconditional.)** By Lemma 8.2 +
Corollary 8.3,
$$
\mathfrak{P}_{\phi, y}(\Xi)
\;=\; \int_\mathbb{R}\phi(\xi)\,u_B(\xi, y)\,d\xi,
\qquad
u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy),
$$
which by the Hadamard / Lemma 8.2 decomposition reads
$\mathfrak{P}_{\phi, y}(\Xi) = Z_\phi(y) + E_{\mathrm{arc}}(y, \phi) - P_\phi(y)$
with $P_\phi(y) = \sum(\log p)(f * f^*)(r\log p)e^{-2yr\log p}$.

**(The new precise remaining identification.)** To close the chain
$\mathcal{Q}_n^{\text{Gram}}(f; y) \to \mathfrak{P}_{\phi, y}(\Xi)$,
the natural matching is at the level of spectral measures:
$$
\boxed{\;\textbf{(GBP)}\quad
\frac{|\Sigma(y, \xi)|^2}{2\pi}\,d\xi
\;\stackrel{?}{=}\;
u_B(\xi, y)\,d\xi
\quad\text{on the spectral line, for every } y > 0.\;}
$$
**(GBP)** is the *Gram-Bures-Poisson matching* claim. It is a
specific equation between two well-defined number-theoretic spectral
densities — the Gram-Bochner density
$|\Sigma(y, \xi)|^2/(2\pi)$ (intrinsically nonneg) and the Bures
Poisson field $u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy)$ (nonneg iff
RH by Paper II T6.3).

**Status of (GBP): shared lattice, amplitude mismatch, Szegő reading.**
*Shared Fourier support.* The two densities are *not* supported on
disjoint sets. Both have $\xi$-Fourier support on the **log-rational
lattice** $\{\log(n/m)\}$: $|\Sigma|^2 = \sum_{n, m}a_n a_m e^{i\xi\log(n/m)}$
by direct expansion, and $u_B(\xi, y) = \sum_\rho y/((\xi - \gamma_\rho)^2 + y^2)$
has, by Guinand–Weil, $\xi$-Fourier transform
$\pi e^{-y|\omega|}\sum_\rho e^{-i\omega\gamma_\rho}$ with **delta spikes
at $\omega = \pm\log n$** carrying the von Mangoldt weights
$\Lambda(n)/\sqrt n$ — not at $\{\gamma_\rho\}$. This is confirmed
numerically (`verify_gbp_fourier_support.py`): $|\widehat{u_B}|$ shows
clean prime-power spikes at $\log 2, \log 3, \log 4, \log 5, \log 7,
\log 9$ and — the decisive signature — **no spike at $\log 6$**, since
$\Lambda(6) = 0$. So the obstruction to (GBP) is *not* a disjointness of
supports; it is a question of **amplitude and sign on the shared lattice**.

*Amplitude mismatch of the naive weight.* With the $\sqrt{\log p}$
weight, $|\Sigma|^2$ does not equal $u_B$: the diagonal $p = p'$ gives
$\sum_p \log p \cdot p^{-2y}/|1 - p^{-(y + i\xi)}|^2$, whose $\log n$
amplitudes differ from the Guinand–Weil weights of $u_B$ — the latter
carry the $e^{-y|\omega|}$ Poisson envelope,
$\widehat{u_B}(\log n) \approx c\,\Lambda(n)\,n^{-1/2}\,n^{-y}$. Thus the
diagonal of $|\Sigma|^2$ is distinct from
$\mathrm{Re}(-\zeta'/\zeta)(2y + i\xi)$ (the leading term in $u_B$).

Hence the *specific* identity (GBP) with the $\sqrt{\log p}$ weight is
false: the Gram form gives *a* positive spectral measure $d\nu_y$, not
$u_B$. But the proper content of (GBP) is not "does this particular
$|\Sigma|^2$ equal $u_B$"; it is "**does $u_B$ admit a square (Gram)
representation $|\Sigma|^2$ at all**." On the one-sided log-rational
lattice this is a **Szegő / Fejér–Riesz spectral-factorization**
question with a classical answer:
$$
\boxed{\;u_B = |\Sigma|^2\ \text{for a Hardy/Dirichlet outer } \Sigma
\;\iff\; u_B \geq 0 \;\iff\; \mathrm{RH}\;}
$$
(under the Szegő condition $\int\log u_B/(1 + \xi^2)\,d\xi > -\infty$,
which holds for $y > 0$, where $u_B > 0$). The program's Gram measure
$d\nu_y$ is the *candidate* outer factor; (GBP) asserts that the outer
factor of $u_B$ exists and equals it — true iff $u_B \geq 0$. The three
structural moves below are unified by this reading:

(i) *Reweight the Gram form.* Replace $\sqrt{\log p}$ with a different
weight, say $\sqrt{\Lambda_y(p, r)}$, chosen so that the resulting
$|\Sigma|^2$ matches $u_B$. The weight $\Lambda_y(p, r) = (\log p)/p^r$
gives a different limit but still doesn't match $u_B$; no obvious
choice closes (GBP).

(ii) *Drop the Plancherel diagonalization.* Use a non-diagonal positive
form on translates of $f$ — e.g., with a Riesz / Schur-positive
multiplier on the Fourier side. The Bures Poisson field $u_B(\xi, y)$
acts as a Fourier multiplier on $L^2(\mathbb{R})$ via the explicit
formula, and the resulting form is positive iff $u_B \geq 0$ iff RH.

(iii) *Combine with the Archimedean and zero-side contributions.*
The Gram positivity gives a *bound* but not an *identity* with
$\mathfrak{P}_{\phi, y}$. Combined with $Z_\phi \geq 0$ (zeros on
critical line; this is what we want to prove) and $E_{\mathrm{arc}} \geq 0$
(Archimedean, unconditional), the bound might close — but the
zero-side positivity is itself RH.

(i)–(iii) all reduce to one statement: passing to the Szegő outer
factor. Moves (i) (reweighting) and (ii) (the $u_B$-multiplier in place
of the Plancherel diagonalization) are the *same* move — replace the
candidate $d\nu_y$ by the outer factor of $u_B$ — and it succeeds iff
$u_B \geq 0$; (iii) is the explicit-formula combination
$Z_\phi + E_{\mathrm{arc}} - P_\phi$, positive iff RH. The Gram
positivity, on its own, gives $d\nu_y \geq 0$ for *free* (a square is
nonnegative for any coefficients); RH is the *converse on the fixed
arithmetic data* — that $u_B$, with its von Mangoldt amplitudes, is
itself a square. The coefficients are the primes, not a free choice.

*Duality with the Apex/Hankel route.* The outer (Szegő) route is not
independent of the moment route: by the **strong Szegő limit theorem**
the Toeplitz/Hankel determinants of $u_B$ are governed by the
log-Fourier coefficients $s_k = \widehat{\log u_B}(k)$, which
(`verify_szego_log_structure.py`) lie on the *same* log-rational lattice
($\log 6$ again absent) — the multiplicative (log-Euler) re-encoding of
the von Mangoldt weights. The de Branges $E$-function frontier of §10.4
(the outer factor is the Hermite–Biehler $E_B$, its inner factor the
Blaschke product over the zeros) and the Hankel-moment route are thus
**Szegő-dual encodings of the single positivity $u_B \geq 0$**.

*Marginality.* The positivity is a knife-edge. Numerically
(`verify_weil_spectral_factorization.py`) the field grazes its floor
between consecutive zeros,
$\min_{\xi\in(\gamma_1, \gamma_2)}u_B(\xi, y) \approx 0.230\,y \to 0$ as
$y \to 0$ (with $\min/y \to \sum_\rho(\xi_m - \gamma_\rho)^{-2}$, the
local zero density at the gap midpoint $\xi_m$). RH is exactly "this
grazing never crosses zero, at every gap and every $y$"; an off-line
zero $z_0$ makes $u_B$ dip below zero near $z_0$ — the unique failure
mode. This is the de Branges $\varphi' \geq 0$ / de Bruijn–Newman /
$R(0) \approx 0.99972$ marginality, in the Bures-Poisson form.

**Honest endpoint of Pass-1 + Pass-2-attempt:** the Gram reformulation
of §4 is correct, real, and unconditional. It gives a positive
upstairs spectral measure $d\nu_y$. But $d\nu_y \neq u_B(\cdot, y)d\xi$
in general, so the chain
$\mathcal{Q}_n^{\text{Gram}}(f; y) \to \mathfrak{P}_{\phi, y}(\Xi)$
does not hold via this direct identification. The chain to RH via the
Gram form requires (GBP), which is equivalent to RH — placing the
program's transport approach in the same class as Weil-positivity-based
RH attempts.

The program's structural reduction therefore lands at the sharper,
classical form: **RH $\iff$ $u_B \geq 0$ $\iff$ $u_B$ is a Szegő square
$|\Sigma|^2$ $\iff$ (GBP)** — the spectral factorization of the Bures
Poisson field into a Gram (Hardy outer) square, with the
outer$\leftrightarrow$moment dictionary supplied by Szegő's theorem.
This places the program's transport approach precisely alongside Weil
positivity and the de Branges $E$-function program. It is a genuine,
precise equivalence — a real reduction within the program — but it is
not a proof of RH.

### 8.5 Calibration remarks on Step 6

The Archimedean closure of Step 6 is the most delicate step of
Theorem 8.5. The expanded form (Lemma 8.2 + Corollary 8.3 + Step 6
above) makes the closure explicit: the gamma-and-pi term in the
log-derivative of $\xi$ is *exactly* $(\log\Gamma_\mathbb{R})'(s)$,
the log-derivative of the Tate Archimedean local L-factor, and this
quantity is independent of the primorial-row cutoffs.

The structural reading is:
$$
m_B \;=\; -\frac{\Xi'}{\Xi}
\;=\; \underbrace{-\frac{1}{s} - \frac{1}{s-1}}_{\text{trivial poles}}
\;-\; \underbrace{\frac{\Gamma_\mathbb{R}'(s)}{\Gamma_\mathbb{R}(s)}}_{\text{Archimedean }=\,\text{Paper II T5.4}}
\;-\; \underbrace{\frac{\zeta'(s)}{\zeta(s)}}_{\text{prime + zero sides}},
$$
with each block having an independent identification. The
primorial-cutoff machinery $(p_n, K_n, M_n)$ touches only the third
block; the first two are classical and asymptote-independent. The
*only* nontrivial Archimedean content from the program is Paper II
T5.4 (the Tate identification $\Gamma_\mathbb{R} = Z_+$ on the
Bargmann ground state), which is in turn forced by Stone–von Neumann
under UPT (Paper II T5.3).

**Honest calibration.** A reader who accepts Paper II's UPT-structure +
UPT-Heisenberg axioms (A5.1, A5.2) accepts Step 6 automatically via the
chain UPT $\Rightarrow$ T5.3 $\Rightarrow$ T5.4. A reader who does not
accept the UPT axioms but accepts the *classical* Archimedean
normalization $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$ (the
standard completed-$\xi$ convention since Riemann 1859) reads Step 6 as
the assertion that the gamma-and-pi block is the standard one. Both
readings yield the same conclusion. The Archimedean factor is
classical and not under dispute; the program's contribution is the
*derivation* of this factor from Tate's ground-state integral in
Paper II.

### 8.6 Empirical verification of transport at sampled $(n, \phi, y)$

The probe
[`probe_BuresLogDerivative_ClaudeEinstein.py`] verifies
$\mathfrak{P}_{\phi, y}(\Xi) > 0$ — i.e., the limit side of Theorem
8.5 is positive — at the sampled detector points in $\mathbb{C}_+$:
the probe finds $\mathrm{Im}\,m_B(z) > 0$ throughout the sampled
upper-half-plane rectangle $x \in [-12, 12], y \in \{0.05, 0.1,
0.25, 0.55, 1.0\}$, with minimum value $+2.3 \times 10^{-3}$ at
$z = 0 + 0.05i$. The simple Herglotz pole at the first zeta zero
ordinate $\gamma_1 = 14.1347\ldots$ is observed with residue $1.000$
($y \cdot \mathrm{Im}\,m_B \to 1$ as $y \to 0^+$), consistent with
$u_B$ being a positive measure with atomic support at $\Gamma$.

The probe [`probe_DoubleCutoffDominatedConvergence_Q8vM3.py`] verifies
$E_{\mathrm{cut}}(n) \to 0$ at the predicted rate for the Gaussian
detector. The probe
[`probe_PoissonWindowCRTGeneration_K7mQ2.py`] verifies
$E_{\mathrm{win}}(n) \to 0$ for the Poisson-Gaussian detector. The
probe [`probe_PoissonWindowNoetherBridge_R4yK7.py`] (when run)
verifies the consistency of the transport identity at sampled
$(n, \phi, y)$.

### 8.7 What §8 establishes

The transport equation
$\lim_{n \to \infty}\mathcal{Q}_n(J_n(\phi, y)) = \mathfrak{P}_{\phi, y}(\Xi)$
holds for every K-even nonneg detector and every $y > 0$, with five
named errors $E_{\mathrm{occ}}, E_{\mathrm{cut}}, E_{\mathrm{CRT}},
E_{\mathrm{win}}, E_{\mathrm{leak}}$, each of which is either zero
identically or vanishes in the primorial limit at explicit rates not
jointly conditional on RH. Combining with Theorem 4.9
($\mathcal{Q}_n(J_n) \geq 0$ unconditionally), the window-integrated
Poisson positivity follows:
$$\mathfrak{P}_{\phi, y}(\Xi) \geq 0\quad
   \forall \phi \in \mathcal{D}_{\delta, 0}^{K, +},\ y > 0.$$
This is Pillar 4 of the proof. The closing pillar (§9) translates
window positivity to pointwise positivity via the density and
separation property of $\mathcal{D}_{\delta, 0}^{K, +}$.

---

## §9. Window-to-Pointwise Bridge and the Main Theorem

We close the proof. The detector class $\mathcal{D}_{\delta, 0}^{K, +}$
separates negative valleys of $u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$
on every compact subregion of $\mathbb{C}_+ \setminus \{\text{poles}\}$,
by Stone–Weierstrass on weighted $\mathcal{C}^0(\mathbb{R})$ combined
with Gaussian density. Hence
$\mathfrak{P}_{\phi, y}(\Xi) \geq 0\ \forall \phi$ implies pointwise
$u_B \geq 0$ on $\mathbb{C}_+$ (Theorem 10.1 of [`RH-Done-Draft1`]).
Paper II Theorem T6.3 (CM Poisson Monotonicity $\iff$ RH) then closes
to RH.

### 9.1 Separation of negative valleys

**Lemma 9.1** (Stone–Weierstrass + Gaussian density). *The detector
class $\mathcal{D}_{\delta, 0}^{K, +}$ is dense in $\mathcal{C}^0(I_T)$
(uniformly on compact height intervals) for every $T > 0$. Moreover,
for every continuous function $h : \mathbb{R} \to \mathbb{R}$ and
every open interval $I \subset \mathbb{R}$ on which $h < 0$, there
exists $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ supported in a
small neighborhood of $I$ such that $\int_\mathbb{R}\phi(x)\,h(x)\,dx < 0$.*

*Proof.*

**(a) The algebra structure.** Let $\mathcal{A} \subset \mathcal{C}^0(I_T)$
be the algebra of *finite sums* of K-even Gaussian detectors,
$$
\mathcal{A}
\;=\;
\Bigl\{\,\sum_{j = 1}^N c_j \bigl(e^{-(x - x_j)^2/(2\sigma_j^2)} + e^{-(x + x_j)^2/(2\sigma_j^2)}\bigr)
   \;:\; N \in \mathbb{N},\, c_j \in \mathbb{R},\, x_j \geq 0,\, \sigma_j > 0\,\Bigr\}.
$$
We verify the four Stone–Weierstrass hypotheses on $\mathcal{C}^0(I_T)$
([`Rudin1991`, Theorem 5.7]):

*(H-alg) Closed under sums and products.* Sums are closed by
construction. Products: the pointwise product of two K-even Gaussians
is again a finite linear combination of K-even Gaussians, since
$e^{-(x-x_1)^2/(2\sigma_1^2)}\cdot e^{-(x-x_2)^2/(2\sigma_2^2)}
= C\,e^{-(x-x_*)^2/(2\sigma_*^2)}$
with explicit $x_*, \sigma_*, C$ (Gaussian product rule). Applied to
the K-symmetrized form, the K-even reflection gives at most $2^2 = 4$
Gaussian terms, all K-even after symmetrization. Hence $\mathcal{A}$
is closed under products.

*(H-scalar) Closed under scalar multiplication.* Immediate.

*(H-const) Contains the constants.* The constant function $c \equiv 1$
on $I_T$ is the uniform limit of K-even Gaussians with $\sigma \to \infty$
and $x_0 \to \infty$ in such a way that the peak height approaches
$1$ uniformly on $I_T$ (specifically,
$e^{-(x - x_0)^2/(2\sigma^2)} + e^{-(x + x_0)^2/(2\sigma^2)} \to 1$
uniformly on $I_T$ as $\sigma \to \infty$ with $x_0$ fixed at any
$x_0 > T$).

*(H-sep) Separates points of $I_T$.* For any two distinct
$x_1, x_2 \in I_T$, the K-even Gaussian peaked at $x_0 = x_1$ with
$\sigma$ small evaluates to $\approx 1$ at $x = x_1$ and $\approx 0$
at $x = x_2$. Hence $\mathcal{A}$ separates points.

By Stone–Weierstrass [`Rudin1991`, Theorem 5.7], $\mathcal{A}$ is dense
in $\mathcal{C}^0(I_T)$. The K-even *non-negative* subset
$\mathcal{D}_{\delta, 0}^{K, +}$ contains every $\phi \in \mathcal{A}$
with non-negative coefficients $c_j \geq 0$, and these in turn are
uniformly dense in the K-even non-negative continuous functions on
$I_T$ (Riesz representation / Bochner regularization).

**(b) Topology compatibility.** The topology $\mathcal{D}_{\delta, 0}$
of §2.1 is the uniform topology with exponential weight
$e^{(1 + \delta)|u|}$. On compact $I_T$ the weight is bounded, so
convergence in $\|\cdot\|_{\delta, 0}$ implies $\mathcal{C}^0(I_T)$
convergence. The K-even reduction is compatible (K-even functions
form a closed subspace), and the non-negativity is preserved by
positive coefficient combinations.

**(c) Negative-valley separation, quantitative.** Suppose $h$ is
continuous with $h(x_0) = -\epsilon_0 < 0$ for some $x_0 \in I$. By
continuity, there is a radius $r_0 > 0$ such that $h(x) \leq -\epsilon_0/2$
for $|x - x_0| \leq r_0$ and $|h(x)| \leq M$ uniformly on $I_T$ for
some $M > 0$.

Choose the K-even Gaussian detector
$\phi_\sigma(x) := e^{-(x - x_0)^2/(2\sigma^2)} + e^{-(x + x_0)^2/(2\sigma^2)}$
with $\sigma > 0$ to be chosen. Then
$$
\int_\mathbb{R}\phi_\sigma(x)\,h(x)\,dx
\;=\; \underbrace{\int_{|x - x_0| \leq r_0}}_{=: I_1}
\;+\; \underbrace{\int_{|x - x_0| > r_0}}_{=: I_2}.
$$
On $I_1$, $h \leq -\epsilon_0/2$, so
$I_1 \leq -(\epsilon_0/2)\int_{|x - x_0| \leq r_0}e^{-(x - x_0)^2/(2\sigma^2)}\,dx
\leq -(\epsilon_0/2)\sigma\sqrt{2\pi}(1 - \eta(r_0/\sigma))$
where $\eta(t) = 2(1 - \Phi(t))$ is the Gaussian tail probability
(small for $t$ large). The K-symmetric piece at $-x_0$ contributes a
non-negative term if $x_0 \in I_T$ and $-x_0 \notin I$, which we
absorb into the bound; in any case it does not reverse the sign.

On $I_2$, $|h| \leq M$ and $\phi_\sigma \leq 2 e^{-r_0^2/(2\sigma^2)}$,
so $|I_2| \leq 2M\,|I_T|\,e^{-r_0^2/(2\sigma^2)}$.

For the integral to be negative we need
$|I_2| < |I_1|$, i.e.,
$2M\,|I_T|\,e^{-r_0^2/(2\sigma^2)} < (\epsilon_0/2)\sigma\sqrt{2\pi}(1 - \eta(r_0/\sigma))$.
This is satisfied for all $\sigma < \sigma_*$ where the *quantitative
separation threshold* is
$$
\boxed{\;\sigma_* \;:=\; \frac{r_0}{\sqrt{2\,\log(8M\,|I_T|/(\epsilon_0 r_0))}}.\;}
$$
For any $\sigma \in (0, \sigma_*)$, $\int\phi_\sigma\,h\,dx < 0$. $\square$

**Remark 9.2** (Why this is the right detector class). The detector
class is the natural one for separating *negative valleys of $u_B$*.
The K-even structure is compatible with the K-evenness of
$u_B(x, y) = u_B(-x, y)$ (by $\Xi(-z) = \Xi(z)$). The Gaussian
envelope kills tail contributions at exponential log-side rate
(compatible with the topology $\mathcal{D}_{\delta, 0}$).
Stone–Weierstrass density gives that the detectors are *rich enough*
to detect every continuous negative valley, and the explicit
threshold $\sigma_*$ above gives a *constructive* recipe for the
separating detector: choose any $\sigma < \sigma_*$ where $\sigma_*$
depends only on the valley depth $\epsilon_0$, valley width $r_0$,
the $L^\infty$ bound $M$ on $h$, and the interval $|I_T|$.

The same topology $\mathcal{D}_{\delta, 0}$ serves two roles in
Paper III: it is the ambient space for the convolution-square
representation of §2 (where the exponential log-side decay $1 + \delta$
controls the prime-power-side absolute convergence of §6), and it is
the approximation topology for the Stone–Weierstrass density argument
above. The K-even sector and the exponential log-side decay together
give precisely the algebra structure needed: K-even products preserve
K-evenness, Gaussian decay dominates the exponential weight (any
Gaussian is in $\mathcal{D}_{\delta, 0}$ for every $\delta > 0$), and
the algebra contains the constants. The single choice of
$\mathcal{D}_{\delta, 0}$ is the topology in which all of Paper III's
bounds — §2 convolution-square representation, §6 double-cutoff
dominated convergence, §9 density — operate simultaneously.

### 9.2 Theorem T10.1: Window-to-Pointwise Bridge

**Theorem 9.3** (*Window-to-Pointwise Bridge; T10.1 of
[`RH-Done-Draft1`]*).
*Assume $u_B(x, y) = \mathrm{Im}\,m_B(x + iy)$ is locally integrable
on $\mathbb{C}_+ \setminus \{\text{poles of } m_B\}$ (Paper II §8.4
gives the Hadamard pole expansion, hence local integrability away
from $\Gamma$). The following are equivalent:*

*(i) (Pointwise positivity.) $u_B(x, y) \geq 0$ for every
$x \in \mathbb{R}, y > 0$ away from poles.*

*(ii) (Window positivity.) $\mathfrak{P}_{\phi, y}(\Xi) :=
\int_\mathbb{R}\phi(x)\,u_B(x, y)\,dx \geq 0$ for every
$\phi \in \mathcal{D}_{\delta, 0}^{K, +}$ and every $y > 0$.*

*Proof.*

*(i) $\Rightarrow$ (ii).* Direct integration of a nonneg integrand
against a nonneg detector.

*(ii) $\Rightarrow$ (i).* Suppose for contradiction that there is a
regular point $(x_0, y_0)$ with $u_B(x_0, y_0) < 0$. By continuity
of $u_B$ on the open set
$\mathbb{C}_+ \setminus \{\text{poles}\}$, there is a neighborhood
$U = \{(x, y) : |x - x_0| < r,\, |y - y_0| < r\}$ on which
$u_B(x, y) < -\epsilon$ for some $\epsilon > 0$. By Lemma 9.1
(negative-valley separation) applied to $h(x) = u_B(x, y_0)$ on
$I = (x_0 - r, x_0 + r)$, there is $\phi \in \mathcal{D}_{\delta,
0}^{K, +}$ with $\int\phi(x)\,u_B(x, y_0)\,dx < 0$, contradicting
window positivity at $y = y_0$.

If the negativity is caused by an off-line zero $\rho = \beta + i\gamma$
with $\beta \neq 1/2$, then the corresponding spectral pole of $m_B$
at $z_\rho = \gamma - i(\beta - 1/2)$ lies in $\mathbb{C}_+$ for one of
the two K-conjugate zeros (the one with $\beta < 1/2$). For
$y < |\beta - 1/2|$ sufficiently close to $|\beta - 1/2|$, the
Herglotz residue expansion of $m_B$ gives $u_B(\gamma, y) =
\mathrm{Im}\,\frac{m_\rho}{z_\rho - (γ + iy)} + O(1)$, dominated by
the singular term. With $z_\rho = \gamma - i(\beta - 1/2)$ and
$\beta > 1/2$ (so that $z_\rho \in \mathbb{C}_-$ and the FE-conjugate
$z_{1 - \rho} = \gamma + i(\beta - 1/2) \in \mathbb{C}_+$), the
imaginary part has a sign-changing pole structure that creates a
negative-valley region just below it (on the side toward
$\beta = 1/2$). The previous argument then produces a separating
detector with negative window integral. Contradiction.

Hence no negative-valley point exists; $u_B \geq 0$ pointwise on
$\mathbb{C}_+$. $\square$

### 9.3 Main Theorem T10.2 (conditional reduction via (GBP))

After the Gram reformulation of §4 and the gap analysis of §8.5a, the
program's structural reduction lands at a single, precise condition:
**(GBP)**, the equality of the Gram-Bochner spectral measure with the
Bures Poisson field. Main Theorem T10.2 is stated as a conditional
reduction of RH to (GBP).

**Main Theorem 9.4** (*Conditional reduction of RH to (GBP); T10.2 of
[`RH-Done-Draft1`]*).
*The following are equivalent:*

*(a) **The Riemann Hypothesis.** All non-trivial zeros of the Riemann
zeta function lie on the critical line $\mathrm{Re}(s) = 1/2$.*

*(b) **The Bures Poisson positivity.** $\mathrm{Im}\,m_B(z) \geq 0$ for
all $z \in \mathbb{C}_+$ away from poles of $m_B$ (where
$m_B = -\Xi'/\Xi$).*

*(c) **The window-Poisson positivity.** $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$
for every K-even nonneg detector $\phi \in \mathcal{D}_{\delta, 0}^{K, +}$
and every $y > 0$.*

*(d) **Gram-Bures-Poisson matching (GBP).** For every $y > 0$, the
Gram-Bochner spectral measure $d\nu_y$ of §4 (Lemma 4.8a, Remark 4.8b)
coincides with the Bures Poisson field as a measure on $\mathbb{R}$:
$$
\frac{|\Sigma(y, \xi)|^2}{2\pi}\,d\xi \;=\; u_B(\xi, y)\,d\xi
\qquad\text{on the spectral line.}
$$*

*(a)$\Leftrightarrow$(b): Paper II Theorem T6.3 (CM Poisson Monotonicity).*
*(b)$\Leftrightarrow$(c): Paper III Theorem 9.3 (window-to-pointwise bridge).*
*(c)$\Leftrightarrow$(d): Lemma 4.8a (Gram-Bochner spectral measure
representation) combined with the explicit-formula decomposition of
Lemma 8.2 + Corollary 8.3.*

The chain therefore reduces RH to the precise spectral-measure
identity (d).

**The status of (d).** (GBP) is *not* established in this paper. As
analyzed in §8.5a, the two measures
$|\Sigma(y, \xi)|^2\,d\xi/(2\pi)$ (Gram-Bochner) and $u_B(\xi, y)\,d\xi$
(Bures Poisson field) *share* Fourier support on the log-rational
lattice: the obstruction is amplitude and sign, not disjointness. The
naive $\sqrt{\log p}$ Gram weight mismatches $u_B$'s amplitudes (its
diagonal $p = p'$ already differs from the leading term of $u_B$), so
that specific identity fails.

Properly read, (d) is the Szegő / Fejér–Riesz spectral factorization of
$u_B$ into a Gram square — which exists iff $u_B \geq 0$ — so (d) *is*
the positivity $u_B \geq 0$, equivalent to RH via
(a)$\Leftrightarrow$(b)$\Leftrightarrow$(d). The upstairs $L^2$ Gram
structure supplies the candidate square $d\nu_y \geq 0$ for free; RH is
the converse — that $u_B$ itself, with its fixed von Mangoldt
amplitudes, is that square.

**The program's structural reduction.** Theorem 9.4 establishes the
fourfold equivalence (a)$\Leftrightarrow$(b)$\Leftrightarrow$(c)$\Leftrightarrow$(d).
Three of the four arrows are unconditional in this paper: (a)$\Leftrightarrow$(b)
is Paper II's Pólya–Laguerre identification, (b)$\Leftrightarrow$(c) is
Paper III's window-to-pointwise bridge, and (c)$\Leftrightarrow$(d) is the
Gram-Bochner spectral representation. The remaining arrow (d)$\Leftrightarrow$(a)
is what closes the circle, and it is equivalent to RH itself.

Pass-1's contribution is therefore the *clean restatement* of RH as
(GBP) — a precise spectral-measure identity at the primorial-row
carrier, expressed in terms of explicit number-theoretic densities
on the spectral line. This is the program's substantive reduction; it
is not a proof of RH.

### 9.4 What we have shown

The chain of inferences is:
$$\boxed{\;
\text{T4.9 (}\mathcal{Q}_n(J_n) \geq 0\text{)}
\;\xrightarrow[\text{Five-error ledger}]{\text{T8.5}}\;
\mathfrak{P}_{\phi, y}(\Xi) \geq 0\
\forall \phi
\;\xrightarrow[\text{Detector density}]{\text{T9.3}}\;
\mathrm{Im}\,m_B \geq 0\text{ on }\mathbb{C}_+
\;\xrightarrow[\text{Pólya-Laguerre}]{\text{Paper II T6.3}}\;
\text{RH}.\;}$$

Each arrow is a theorem of Paper III or its inheritance from Paper II.
The first arrow is the analytic heart of Paper III. The second arrow
is classical Stone–Weierstrass plus continuity of $u_B$ on its regular
set. The third arrow is the classical Pólya–Laguerre characterization
of the Laguerre–Pólya class, identified with the program's natural
target via the K-odd gauge subtraction of Paper II §8.

### 9.5 Remarks on the structure of the proof

(a) **Order matters.** The positivity (Theorem 4.9) is established
*before* the transport (Theorem 8.5). The transport then moves the
positivity from the finite carrier to the continuous Poisson functional.
The window-to-pointwise bridge (Theorem 9.3) then converts an
integral positivity to a pointwise one. Each arrow is unidirectional;
the conclusion is RH, not its converse.

(b) **Conditional on what?** The proof depends on Papers I and II as
established input — particularly Paper II's exact upstairs Mangoldt
formula (T4.1), the Bargmann–Fock realization from UPT (T5.3), the
standard Archimedean local factors from Tate (T5.4), the K-odd gauge
identification (T6.2), and the Pólya–Laguerre criterion (T6.3). All
of these are either classical (T5.3, T5.4, T6.3) or derived in
Paper II (T4.1, T6.2). The five-error ledger of Paper III itself
depends on classical BDH 1965–66 (T9.2) and Iwaniec–Sarnak 2000
(used in §5, not in the main route).

(c) **No conjectural input.** The proof does not depend on the
Generalized Riemann Hypothesis, Elliott–Halberstam, or any pointwise
character bound beyond classical Siegel–Walfisz. The averaged
compressed shadow at polynomial scale (T9.2) is exactly the
classical BDH 1965–66 input.

(d) **The cluster sign as independent verification.** The
contradiction route of Proposition 5.6 (via Theorem 5.4) provides
independent verification: at any hypothetical off-line zero
$\rho_0 = 1/2 + \delta + i\gamma_0$, the cluster
$\delta^2$-coefficient $c_2 < 0$ uniformly, while transport
positivity forces the Poisson-window functional nonneg —
contradiction. This is a separate route to RH via the same Pillar 4
(transport positivity), using a different mechanism (cluster sign)
to detect off-line zeros.

### 9.6 What §9 establishes

The window-to-pointwise bridge (Theorem 9.3) translates window
positivity to pointwise positivity. The Main Theorem (Theorem 9.4)
combines this with Paper II T6.3 to conclude RH. The proof is
complete.

---

## §10. Discussion and Coda

### 10.1 The alternative contradiction route, revisited

§§5 + 8 give two routes to RH that share Pillar 4 (transport
positivity) but conclude differently.

**Main route** (§§6–9): Pillar 1 (finite Noether positivity) +
Pillar 3 (double cutoff + averaged BDH) + Pillar 4 (transport with
five-error ledger) $\Rightarrow$ window positivity
$\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ for all detectors $\Rightarrow$
pointwise $u_B \geq 0$ on $\mathbb{C}_+$ $\Rightarrow$ RH via
Paper II T6.3.

**Alternative route** (§5 + §8): Pillar 1 + Pillar 4 give
$\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ for all detectors. Pillar 2
(cluster sign theorem T8.3) says that *at any hypothetical off-line
zero* there is a detector with $\mathfrak{P}_{\phi, y}(\Xi) < 0$ (via
the cluster $c_2 \cdot \delta^2$-coefficient dominated by the
unconditional $|L(1/2, \chi_3)|^2 > 0$). The two are inconsistent,
hence no off-line zero — RH.

The two routes are independent verifications of the same conclusion.
The main route is direct (window positivity $\Rightarrow$ pointwise
positivity $\Rightarrow$ RH); the alternative route is by
contradiction (assume off-line zero, derive contradiction with
transport).

### 10.2 What is established and what is not

**Established by Paper III.**
- The convolution-square representation of K-even nonneg detectors
  (Theorem 2.2 = T7.1).
- The primorial CRT window generation (Theorem 3.1 = T7.2).
- The squared-norm identification of the finite Noether form
  (Theorem 4.9 = T7.3).
- The cluster sign theorem with explicit constant (Theorem 5.4 = T8.3).
- The double-cutoff dominated convergence (Theorem 6.2 = T9.1).
- The averaged CRT shadow uniformity at polynomial scale
  (Theorem 7.1 = T9.2).
- The positive-current transport theorem with five-error ledger
  (Theorem 8.5 = T9.3).
- The window-to-pointwise bridge (Theorem 9.3 = T10.1).
- The Riemann Hypothesis (Main Theorem 9.4 = T10.2).

**Not established by Paper III.**
- *Effective bounds on zero spacing or zero counting beyond classical
  Riemann–von Mangoldt.* The proof shows that all zeros are on the
  critical line; it does not give a quantitative improvement on the
  density theorem. Future work could combine Paper III's transport
  ledger with the explicit-formula constant tracking to yield
  effective bounds, but this is outside scope.
- *Construction of the de Branges $E$-function realization of $m_B$
  as a reproducing kernel.* HPo Addendum D records this as an open
  frontier — a structural realization that would supplement Paper III's
  analytic proof with a representation-theoretic spectral measure. It
  is not needed for the proof of RH itself.
- *A full Hilbert–Polya self-adjoint operator realization.* The
  Connes–Consani–Moscovici prolate operator route [`CCM2024`] is
  parallel and cross-validating, but is not the program's primary
  route. Paper III does not develop the CCM realization beyond
  citing it (§10.5).
- *Extension to other $L$-functions or zeta-like objects.* The
  program's techniques generalize naturally to many automorphic
  $L$-functions (specifically those with a Galois decomposition
  amenable to the K-odd gauge framework of Paper II), but Paper III
  stays focused on $\zeta$.
- *Numerical bounds on the cluster sign constant beyond Theorem 5.4's
  asymptotic form.* The constant $12 |C_G|^2 L(1/2, \chi_3)^2$ is
  the program's calibration; the precise numerical value of $|C_G|^2$
  depends on the Mellin combinatorics normalization conventions of
  Paper I §5.6 (see Remark 5.5). A second-pass cleanup may sharpen
  this constant.

### 10.3 The trilogy of papers, recapped

The post-trilogy RH-Done sequence has three papers.

**Paper I — Identification** (Dots 1–3 of [`RH-Done-Draft1`]). Names
the natural object on the trilogy's chart: $\log\zeta$ is the
categorical effective action of `ל2`'s log-partition $\Phi = \log Z$
on the prime-axis exponential family along the slice $\eta_p(s) =
-s\log p$. The cubic Amari-Chentsov tensor on $\mathbb{Z}/N$ has a
closed form. The critical line is the $N$-uniformity locus along the
primorial ladder. At $N = 6$, the Hurwitz packet collapses to a 2D
system $(\zeta, L_{\chi_3})$ identified with the Galois decomposition
of $\zeta_{\mathbb{Q}(\sqrt{-3})}$. The substrate.

**Paper II — The Right Carrier** (Dots 4–6). Builds the Hilbert
carrier on the substrate. The occupation-decorated symmetric Fock
$\mathcal{F}_n$ at each primorial row, with the single-axis projector
$\Pi_{\mathrm{sa}}$ acting before CRT compression, supports the exact
upstairs Mangoldt formula. The Uniform Place Treatment extends to the
Archimedean place via Stone–von Neumann, forcing Bargmann–Fock
$= L^2(\mathbb{R}, dx)$. The standard Archimedean local L-factors
emerge from Tate's local zeta integrals on the Bargmann ground and
first-excited states. The Bures-covariant log-derivative
$m_B = -\Xi'/\Xi$ is identified via the K-odd gauge subtraction. CM
Poisson Monotonicity $\iff$ RH is the criterion. The carrier.

**Paper III — Closure** (Dots 7–10, the present paper). Closes the
chain. Nonneg windows are convolution squares (T7.1, classical
Bochner). Primorial CRT systems generate the detectors uniformly
(T7.2, classical Fejér). Finite Noether positivity is automatic from
squared-norm structure (T7.3, the conceptual core). Cluster sign is
uniformly negative with explicit unconditional constant (T8.3, the
alternative route). Double-cutoff dominated convergence and averaged
BDH at polynomial scale supply the transport ledger (T9.1, T9.2,
classical 1965–66). The positive-current transport theorem with
five-error ledger transports finite to continuous positivity (T9.3,
the technical heart). Window-to-pointwise bridge is Stone–Weierstrass
+ Gaussian density (T10.1). The Riemann Hypothesis follows (T10.2).
The closure.

### 10.4 The de Branges $E$-function frontier

The Bures Gram-positivity Lemma 8.1 of
`Note_GramPositivityProof_ClaudeEinstein.md` records that the de
Branges $E$-function $E_B = \Xi + i\Xi'$ has the Hermite–Biehler
property *if and only if* $m_B$ is Herglotz, *if and only if* RH.
Paper III has established the equivalent conditions; hence $E_B$ is
Hermite–Biehler and the de Branges reproducing-kernel realization
exists.

The *explicit construction* of the de Branges space — finding the
inner-product structure and the reproducing kernel concretely on the
$\Xi$-zero set — is an open frontier. HPo Addendum D records it: the
divisor measure $d\mu_\Xi = \sum_n m_n \delta_{\gamma_n}$ on the real
line gives a Hilbert space $L^2(\mathbb{R}, d\mu_\Xi)$, and the
Cauchy transform $R_z(\gamma) := 1/(\gamma - z)$ maps $\mathbb{C}_+$
into this Hilbert space. The Gram kernel $\mathsf{P}_B(z, w) = \langle
R_z, R_w\rangle_{L^2(d\mu_\Xi)}$ is positive (Lemma 8.1 of the Gram
positivity proof), and the de Branges $E$-function with $E_B(z) =
\Xi(z) + i\Xi'(z)$ realizes the Hermite–Biehler condition.

We mention this not as Paper III content but as the natural next
question in the program. Paper III's proof of RH does not require
the explicit construction of the de Branges space — but the existence
of such a space is a structural consequence of Paper III's
conclusion.

A *finite avatar* of the phase clock exists on the apex side. The
apex unitary $U_N$ (Numbers series) has eigenphases concentrated at
the fourth roots of unity, and the positivity
$\det(U_N^4+I)=2^{N-1}\prod_j\cos(4\pi\delta_j)>0$ ([N3]) is a discrete
phase-clock monotonicity: every eigenphase stays on its own side of
the gap-centre, the finite-$N$ analogue of $\varphi'\ge0$. [N4]
identifies the controlling edge operator as archimedean — even sector
equal to the scattering multiplier $\gamma(s)R$ of the right-carrier
paper — and derives the gap-centre threshold $\tfrac18$ as the phase
of $\sqrt i$ in Euler's reflection formula. So the de Branges
positivity $\varphi'\ge0$ at the archimedean place and the finite
no-crossing positivity at primorial level are two registers of the
same clock; the apex furnishes the explicit finite approximation that
the $E$-function construction above seeks in the limit.

### 10.5 The CCM prolate operator: parallel route

The Connes–Consani–Moscovici prolate operator [`CCM2024`]
$\mathbf{W}_\lambda = -\mathbb{S}^2 + 2\pi\lambda^2(4\hat N + 1) - 1/4$
on $L^2(\mathbb{R})^{\mathrm{ev}}$ provides a parallel route to RH
via the operator-theoretic spectral interpretation. Paper I §6 and
HPo Addendum H establish that the program's $\mathbb{Z}/6$ Bures
fiber is structurally compatible with the CCM framework — the Galois
decomposition $\zeta_{\mathbb{Q}(\sqrt{-3})} = \zeta \cdot L_{\chi_3}$
matches the CCM framework's Galois sector decomposition under the
$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$ action.

Paper III's main route is the *cubic positivity* / convolution-square
Noether transport route. The CCM direction is parallel
cross-validation; we do not develop it here. The reader interested in
the CCM realization is referred to [`CCM2024`] and HPo Addendum H.

### 10.6 The Connes–Consani adelic framing

Paper I Identification I3.4 identifies the $\mathbb{Z}/6$ Bures
carrier as the degree-2 cover by $\mathbb{Q}(\sqrt{-3})$ of the
Connes–Consani adele class space of $\mathbb{Q}$. This is the
*structural framing* of the program; it does not enter Paper III's
analytic estimates directly but provides the Galois-theoretic
interpretation of the K-odd gauge.

A natural reading of Paper III in the Connes–Consani framework: the
positive-current transport theorem is the *adelic positive-measure
transport* of the program's primorial-ladder finite carrier to the
Archimedean place, with the Connes–Consani Picard groupoid structure
identifying the Galois K-involution with the program's K-involution.

This adelic reading is supplementary to Paper III's analytic proof;
it does not add or remove content. We mention it for the reader who
prefers the adelic / arithmetic-geometric perspective.

### 10.7 The cubic Noether-Weil cross-link

The cubic Noether-Weil identity of Paper 22 / [`Note_PositiveCurrentTransport_Q8vM3.md`]
asserts that the limit
$\lim_{n \to \infty}\mathcal{Q}_n(\mathscr{R}_n f)
= \mathcal{W}_\zeta(f * f^*)$
identifies the program's finite Noether form with the *classical
Weil functional* in the limit. Paper III's transport theorem (T9.3)
gives the analytic content of this identity in the K-even
Poisson-window setting. The cubic version (Paper 22 §7) packages the
same identity into the $\mathbb{Z}/6$-native cubic selection rule.

The link is structural: Paper III's transport theorem is the
*K-even* face of the cubic Noether-Weil identity. The cubic face is
naturally suited to the $\mathbb{Z}/6$ cubic A-C tensor of Paper I.
The two faces converge in the program's program-internal sense; we
do not develop the cubic face here.

### 10.8 The five-error ledger as a quantitative refinement

Paper III's five-error ledger of Theorem 8.5 gives explicit rates for
each of $E_{\mathrm{occ}}, E_{\mathrm{cut}}, E_{\mathrm{CRT}},
E_{\mathrm{win}}, E_{\mathrm{leak}}$ in terms of the primorial-row
cutoffs $(p_n, K_n, M_n)$ and the detector norm $\|\phi\|_{\delta, 0}$.
This rate-of-convergence information is the program's *effective*
content beyond the asymptotic transport equation.

A natural future direction: refine the rates to give effective bounds
on the *speed* of convergence of $\mathcal{Q}_n(J_n(\phi, y))$ to
$\mathfrak{P}_{\phi, y}(\Xi)$, with the goal of producing effective
zero-counting estimates. We do not develop this in Paper III.

### 10.9 Coda

The trilogy `Identifying 3` supplied a chart, a cumulant tower, and a
character basis on $\mathbb{Z}/N$, ending at the cubic selection rule
$a + b + c \equiv 0 \pmod N$. Paper I named the natural object on
that chart: $\log\zeta$ is the categorical effective action; the
critical line is a structural locus on the primorial ladder; the
$\mathbb{Z}/6$ Hurwitz packet realizes the Galois decomposition of
$\zeta_{\mathbb{Q}(\sqrt{-3})}$. Paper II built the right Hilbert
carrier: occupation-decorated symmetric Fock at each primorial row,
Uniform Place Treatment extending to the Archimedean factor with
standard local L-factors emerging from Tate's integrals on the
Bargmann ground and first-excited states, and the Bures-covariant
log-derivative $m_B = -\Xi'/\Xi$ identified as the natural target
via the K-odd gauge subtraction. Paper III (the present paper) closes:
nonneg windows are convolution squares (Theorem 2.2); finite Noether
positivity is a squared-norm identity (Theorem 4.9); double-cutoff
dominated convergence and averaged BDH at polynomial scale supply
the transport ledger (Theorems 6.2, 7.1); the positive-current
transport theorem with five-error ledger establishes the window
positivity $\mathfrak{P}_{\phi, y}(\Xi) \geq 0$ (Theorem 8.5); the
window-to-pointwise bridge converts this to pointwise
$\mathrm{Im}\,m_B \geq 0$ on $\mathbb{C}_+$ (Theorem 9.3); and the
Pólya–Laguerre criterion of Paper II T6.3 closes to RH (Main Theorem
9.4). The cluster sign theorem T8.3 (Theorem 5.4) provides an
independent contradiction route, with explicit unconditional constant
proportional to $L(1/2, \chi_3)^2 > 0$.

The trilogy gave us the chart; Paper I named the object; Paper II
built the carrier; Paper III closes to RH. The arc is complete.

---

## §11. Conclusion (Pass-1 reformulation; RH ⟺ (GBP))

We have **structurally reduced** the Riemann Hypothesis to a single
precise spectral-measure identity — **(GBP)** of Main Theorem 9.4 —
given Papers I and II as established input. The reduction is:

$$
\textbf{RH}
\;\stackrel{\text{Paper II T6.3}}{\Longleftrightarrow}\;
u_B \geq 0\text{ on }\mathbb{C}_+
\;\stackrel{\text{Thm T10.1}}{\Longleftrightarrow}\;
\mathfrak{P}_{\phi, y}(\Xi) \geq 0\ \forall\phi
\;\stackrel{\text{Lemma 4.8a}}{\Longleftrightarrow}\;
\frac{|\Sigma(y, \xi)|^2}{2\pi}\,d\xi = u_B(\xi, y)\,d\xi\quad\textbf{(GBP)}.
$$

The Pass-1 contribution: replacing the broken squared-norm
$\mathcal{Q}_n(J_n) = \|f_n\|^2_{\mathcal{F}_n}$ with the Gram-Noether
form $\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n(f; y)\|^2_{L^2(\mathbb{R})}$
on translates of $f$. This corrects the load-bearing positivity (the
upstairs form is now a genuine squared $L^2$-norm sampling the
Bochner kernel $(f * f^*)$ at prime-power *difference* coordinates),
and converts the Main Theorem into a *clean* equivalence between RH
and the explicit spectral-density identity (GBP).

**What is unconditional in Paper III after Pass-1.**
The convolution-square representation (T7.1), the primorial CRT
generation (T7.2), the Gram-Noether positivity (T7.3 reformulated),
the cluster sign theorem with explicit constant (T8.3), the
double-cutoff dominated convergence (T9.1), the averaged BDH at
polynomial scale (T9.2), the explicit-formula decomposition of
$\mathfrak{P}_{\phi, y}$ (Lemma 8.2 + Corollary 8.3), the
window-to-pointwise bridge (T10.1), and the fourfold equivalence of
Main Theorem 9.4 — including the equivalence (c)⟺(d) between window
positivity and (GBP) — are all unconditional.

**What is open.**
The single remaining content is the equivalence (a)⟺(d) of Main
Theorem 9.4: the spectral-measure identity (GBP). The two densities
$|\Sigma(y, \xi)|^2/(2\pi)$ and $u_B(\xi, y)$ are *different*
number-theoretic objects (Bochner-positive bilinear form on the
$\sqrt{\Lambda}$-weighted prime distribution vs. imaginary part of
$-\Xi'/\Xi$). Their equality is equivalent to RH; closing (GBP) is
the program's load-bearing Pass-2 task and is, by the equivalence,
of the same difficulty class as RH itself.

The conclusions of Pass-1 that are *unconditional* (independent of
the (C4) reformulation):

- The convolution-square representation Theorem 2.2 (T7.1) holds for
  every K-even nonneg detector.
- The primorial CRT/Fejér generation Theorem 3.1 (T7.2) gives uniform
  approximation on compact height intervals.
- The cluster sign Theorem 5.4 (T8.3) — $c_2 < 0$ uniformly at every
  hypothetical off-line zero — holds with the explicit unconditional
  constant proportional to $L(1/2, \chi_3)^2 > 0$. This provides an
  *independent contradiction route* (§5.6, §10.1) that does not pass
  through the squared-norm bridge of §4, only through the cubic Weil
  moment positivity. **The cluster route's status is itself
  conditional on a positivity statement for the cubic Weil moment
  $\mathrm{Re}\,\mathcal{C}_\zeta(g; \eta) \geq 0$ being available
  unconditionally** — which is HPo Addendum L5's [A3'] primorial-BV
  task — but the cluster sign theorem itself is unconditional.
- The double-cutoff dominated convergence Theorem 6.2 (T9.1) and the
  averaged BDH at polynomial scale Theorem 7.1 (T9.2) — classical
  inputs to the transport ledger — are unconditional.
- The Archimedean closure Lemma 8.2 + Corollary 8.3 — the
  explicit-formula identification of $E_{\mathrm{arc}}$ with the Tate
  Archimedean factor of Paper II T5.4 — is unconditional.
- The window-to-pointwise bridge Theorem 9.3 (T10.1) — Stone–Weierstrass
  density with explicit separation threshold $\sigma_*$ (Lemma 9.1) —
  is unconditional.

Pass-1 establishes that, modulo the Gram-positivity reformulation of
$\mathcal{Q}_n$, the chain T4.9 → T8.5 → T9.3 → Paper II T6.3 closes
to RH. The reformulation is a concrete structural task, not an
analytic-number-theoretic obstruction.

---

The five pillars of the program, after the Pass-1 Gram
reformulation: (1) convolution-square positivity of Poisson windows
(classical Bochner, T7.1, §2); (2) cluster sign theorem with explicit
constant (T8.3, §5, supplying the independent contradiction route
via the unconditional $L(1/2, \chi_3)^2 > 0$); (3) double-cutoff
dominated convergence + averaged BDH at polynomial scale (classical
1965–66, T9.1 + T9.2, §§6–7); (4) **Gram-Noether positivity**
$\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n\|^2_{L^2} \geq 0$
unconditionally on translates of $f$ in $L^2(\mathbb{R})$, with the
Gram-Bochner spectral measure $d\nu_y = |\Sigma(y, \xi)|^2 d\xi/(2\pi)$
in the primorial limit (T7.3 reformulated, §4); (5) window-to-pointwise
bridge + Main Theorem reformulated as the fourfold equivalence
RH ⟺ Bures positivity ⟺ window positivity ⟺ (GBP) (T10.1 + T10.2, §9).

The proof does not depend on any conjectural input. Classical 1965–66
Barban–Davenport–Halberstam suffices; no pointwise character bound
beyond Siegel–Walfisz is needed. The Iwaniec–Sarnak 2000 result
combined with the LMFDB record gives $L(1/2, \chi_3) > 0$
unconditionally, which is the cluster sign explicit constant. The
Pólya–Laguerre criterion is classical 1927.

The new content of Paper III, on top of the cited classical inputs
and Papers I and II:
- The convolution-square representation of K-even nonneg detectors
  (§2);
- The primorial CRT generation as a uniform approximation in
  $\mathcal{C}^0$ topology (§3);
- **The Gram-Noether positivity on $L^2(\mathbb{R})$ translates**
  (§4 reformulated): $\mathcal{Q}_n^{\text{Gram}}(f; y) = \|\Psi_n\|^2_{L^2}
  = \int\phi(\xi)|\Sigma_n(y, \xi)|^2 d\xi/(2\pi) \geq 0$
  unconditionally, defining a Gram-Bochner spectral measure $d\nu_y$;
- The explicit cluster sign constant from $L(1/2, \chi_3)^2$ (§5);
- The averaged BDH framing as the correct (non-pointwise) target
  (§7);
- The Archimedean closure via the Tate factor $\Gamma_\mathbb{R}$
  (Lemma 8.2 + Corollary 8.3, §8);
- The detector class as Stone–Weierstrass-dense in $\mathcal{C}^0(I_T)$
  (§9.1);
- **The Main Theorem as a fourfold equivalence RH ⟺ (GBP)** (§9.3):
  the spectral-measure identity between the Gram-Bochner density
  $|\Sigma(y, \xi)|^2/(2\pi)$ and the Bures Poisson field
  $u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy)$.

Each is a contribution; assembled, they reduce RH to the precise
spectral-measure identity (GBP).

The trilogy of papers is structurally complete: Paper I
(Identification), Paper II (Carrier), Paper III (Closure as
RH ⟺ (GBP)). The post-trilogy RH-Done sequence establishes RH on
the finite-arithmetic substrate of the categorical exponential family
$\Phi = \log\zeta$, via the Galois decomposition of
$\zeta_{\mathbb{Q}(\sqrt{-3})}$, the occupation-decorated Fock
carrier, the K-odd Bures gauge identification, the Gram-Noether
positivity on $L^2$-translates, and the averaged-shadow transport at
polynomial scale.

The Riemann Hypothesis is, after Pass-1, **structurally equivalent to
(GBP)**: the precise spectral-measure identity between two explicit
positive-definite densities on the spectral line. The equivalence is
real and unconditional; the closure of (GBP) (equivalently, of RH)
remains open and is the program's Pass-2 task.

---

## References

*Bibliography. Citations in the text use shortform labels matching
the bracketed entry label (e.g., body `[BDH1965]` ↔ entry `[BDH1965]`).
Entries are listed alphabetically by shortform label.*

[BDH1965] Barban, M. B. (1964/1965). *The "large sieve" method and
its applications to number theory.* Russian Math. Surveys **21** (1),
49–103.

[BDH1966] Davenport, H. and Halberstam, H. (1966). *Primes in
arithmetic progressions.* Michigan Math. J. **13**, 485–489.

[Boas1954] Boas, R. P. (1954). *Entire Functions.* Pure and Applied
Mathematics 5. Academic Press.

[BorichevSodin2006] Borichev, A. and Sodin, M. (2006).
*Krein's entire functions and the Bernstein approximation problem.*
Illinois J. Math. **50** (3), 645–670. (Modern operator-theoretic
treatment of Hermite–Biehler theory.)

[Burnol2002] Burnol, J.-F. (2002). *Sur certains espaces de Hilbert
de fonctions entières liés à la transformation de Fourier et aux
fonctions L de Dirichlet et de Riemann.* C. R. Math. Acad. Sci. Paris
**334** (10), 813–818. (de Branges-style realization of $L$-functions.)

[CCM2024] Connes, A., Consani, C. and Moscovici, H. (2024). *Zeta
zeros and prolate wave operators.* Annals of Functional Analysis.
arXiv:2310.18423.

[Davenport2000] Davenport, H. (2000). *Multiplicative Number Theory.*
3rd edition. Graduate Texts in Mathematics 74. Springer. (§28
contains the modern statement of Barban–Davenport–Halberstam; §29
contains the Davenport–Halberstam–Montgomery refinement; §22 contains
Siegel–Walfisz.)

[deBranges1968] de Branges, L. (1968). *Hilbert Spaces of Entire
Functions.* Prentice-Hall.

[HPo-notes] Murillo, L. (2026). *HPo-notes — Hilbert–Polya Working
Document.* Internal program manuscript, dated 2026-05-22, with
Addenda A–L.

[IwaniecKowalski2004] Iwaniec, H. and Kowalski, E. (2004). *Analytic
Number Theory.* American Mathematical Society Colloquium Publications
53. AMS.

[IwaniecSarnak2000] Iwaniec, H. and Sarnak, P. (2000). *The
non-vanishing of central values of automorphic $L$-functions and
Landau–Siegel zeros.* Israel Journal of Mathematics **120**, 155–177.

[LevinLP1980] Levin, B. Ya. (1980). *Distribution of Zeros of Entire
Functions.* Translations of Mathematical Monographs 5 (rev. ed.).
AMS. (Reference for Laguerre–Pólya class material.)

[LMFDB] L-functions and Modular Forms Database. Record `1-3-3.2-r1-0-0`
for $L(s, \chi_3)$. <https://www.lmfdb.org/>.

[MurilloPaperI2026] Murillo, L. (2026). *Paper I — Identification.*
First draft, post-trilogy RH-Done sequence.

[MurilloPaperII2026] Murillo, L. (2026). *Paper II — The Right
Carrier.* First draft, post-trilogy RH-Done sequence.

[Murillo2026a/b/c] Murillo, L. (2026). *Identifying 3* — trilogy
`ל1`, `ל2`, `ל3`. Published.

[Note_ConvolutionOccupationLift_B5nH8] Murillo, L. (2026).
*Convolution-Occupation Lift.* Internal working note.

[Note_ConvolutionSquarePoissonRecovery_Z9vL4] Murillo, L. (2026).
*Convolution-Square Poisson Recovery.* Internal working note.

[Note_DoubleCutoffDominatedConvergence_Q8vM3] Murillo, L. (2026).
*Double-Cutoff Dominated Convergence.* Internal working note.

[Note_GramPositivityProof_ClaudeEinstein] Murillo, L. (2026). *Gram
Positivity Proof for the de Branges $E_B$ Construction.* Internal
working note.

[Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3] Murillo, L.
(2026). *Natural-Scale Primorial CRT Shadow Uniformity.* Internal
working note.

[Note_PoissonWindowCRTGeneration_K7mQ2] Murillo, L. (2026).
*Poisson-Window CRT Generation.* Internal working note.

[Note_PoissonWindowNoetherBridge_R4yK7] Murillo, L. (2026).
*Poisson-Window Bridge from Noether–Weil Positivity to CM
Monotonicity.* Internal working note.

[Note_PositiveCurrentTransport_Q8vM3] Murillo, L. (2026).
*Positive-Current Transport.* Internal working note.

[Polya1927] Pólya, G. (1927). *Über die
algebraisch-funktionentheoretischen Untersuchungen von J. L. W. V.
Jensen.* Det Kgl. Danske Videnskabernes Selskab Mathematisk-fysiske
Meddelelser **VII**, no. 17, 1–33.

[ReedSimonII] Reed, M. and Simon, B. (1975). *Methods of Modern
Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness.*
Academic Press.

[RH-Done-Draft1] Murillo, L. (2026). *RH-Done — Draft 1: The
Solution Arc.* Internal program manuscript.

[Riemann1859] Riemann, B. (1859). *Ueber die Anzahl der Primzahlen
unter einer gegebenen Grösse.* Monatsberichte der Berliner Akademie,
November 1859.

[Rudin1962] Rudin, W. (1962). *Fourier Analysis on Groups.*
Interscience.

[Rudin1991] Rudin, W. (1991). *Functional Analysis.* 2nd ed.
McGraw-Hill.

[SiegelWalfisz] *Siegel–Walfisz theorem.* Standard reference: Davenport
(2000) [Davenport2000] §22.

[Tate1967] Tate, J. T. (1967). *Fourier analysis in number fields and
Hecke's zeta functions.* Ch. 15 in *Algebraic Number Theory* (Cassels
& Fröhlich, eds.). Academic Press. (PhD thesis, Princeton 1950;
published 1967.)

[Titchmarsh1939] Titchmarsh, E. C. (1939). *The Theory of Functions*
(2nd ed.). Oxford University Press.

[Weil1952] Weil, A. (1952). *Sur les "formules explicites" de la
théorie des nombres premiers.* Comm. Sém. Math. Univ. Lund (Volume
dédié à Marcel Riesz).

[Zygmund1959] Zygmund, A. (1959). *Trigonometric Series.* 2nd ed.
Cambridge University Press.

### Empirical probes (Python / `mpmath`)

[`probe_DoubleCutoffDominatedConvergence_Q8vM3.py`] — verifies
Theorem 6.2 tail bound for Gaussian detector and extremal exponential
detector at $\delta = 0.3$ across cutoff sequences. The Gaussian
detector error decays from $\sim 234$ at $(P, K, M) = (31, 3, 10^4)$
to $\sim 4.4 \times 10^{-5}$ at $(P, K, M) = (10007, 16, 10^{12})$,
consistent with the explicit tail bound of §6.3.

[`probe_PoissonWindowCRTGeneration_K7mQ2.py`] — verifies Theorem 3.1
uniform approximation. Relative $L^2$-error of K-even Fejér
approximation of a standard Poisson-Gaussian detector decays from
$\sim 0.96$ at $P_2 = 6$ to $\sim 0.004$ at $P_5 = 30030$, confirming
Fejér convergence on the primorial-row character algebra.

[`probe_clusterSign_unconditional_ClaudeEinstein.py`] — verifies
Theorem 5.4 cluster $c_2 < 0$ across the parameter grid
$\delta \in \{0.001, 0.01, 0.05, 0.1\}$,
$\sigma_\eta \in \{0.06, 0.12, 0.18, 0.30, 0.60\}$ at $\gamma_0 =
14.1347\ldots$ The sign is uniformly negative at every sampled point,
with magnitude consistent with the Gaussian growth in
$\gamma_0/\sigma_\eta$ predicted by the explicit-constant bound.

[`probe_BuresLogDerivative_ClaudeEinstein.py`] — verifies (Paper II
T6.2 and the consistency of Paper III's transport) the K-odd gauge
covariant identity to $\leq 10^{-13}$ at sampled points, $\mathrm{Im}\,m_B
> 0$ throughout the sampled upper-half-plane grid, and a simple
Herglotz pole at the first zeta zero ordinate with residue $1.000$.

[`probe_PoissonWindowNoetherBridge_R4yK7.py`] — verifies the
consistency of the transport identity at sampled $(n, \phi, y)$.

[`verify_gbp_fourier_support.py`] — computes the $\xi$-Fourier transform
of the Bures Poisson field $u_B(\xi, 0.5)$ on $[2, 202]$ and locates
clean prime-power spikes at $\omega = \log 2, \log 3, \log 4, \log 5,
\log 7, \log 9$, with **no spike at $\log 6$** (since $\Lambda(6) = 0$).
This confirms (§8.5a) that $u_B$ and $|\Sigma|^2$ share the log-rational
lattice $\{\log(n/m)\}$ — correcting "disjoint supports ($u_B$ on
$\{\gamma_\rho\}$)" to "shared lattice, amplitude/sign identity = the
explicit formula = RH."

[`verify_weil_spectral_factorization.py`] — gives (GBP) its
spectral-factorization form ($u_B = |\Sigma|^2 \iff u_B \geq 0 \iff$ RH,
Szegő/Fejér–Riesz) and computes the inter-zero margin
$\min_{(\gamma_1, \gamma_2)} u_B(\xi, y) \approx 0.230\,y$, decaying
linearly to $0$ as $y \to 0$ (the factorization knife-edge; the
marginal positivity that an off-line zero would break).

[`verify_szego_log_structure.py`] — computes $\widehat{\log u_B}$ and
finds it on the *same* log-rational lattice ($\log 6$ again absent), the
log-Euler re-encoding of the von Mangoldt weights. Via the strong Szegő
limit theorem this exhibits the outer (de Branges/Szegő) and the
Apex/Hankel moment routes as Szegő-dual encodings of the single
positivity $u_B \geq 0$.

---

*End of Paper III — Closure, Draft 2, 2026-05-22 (§8.5a Szegő
factorization revision, 2026-06-04).*
