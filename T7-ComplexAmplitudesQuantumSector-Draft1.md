# \heb{ל}7 — Complex Amplitudes and the Quantum Sector of the Apex

**Leonardo Murillo Montero — leonardo.murillo@gmail.com**

*Preprint, version 1.0 — May 25, 2026*

---

> *Decoherence is closure of phase. Quantization is the cover.*

---

## Abstract

**Situation.** [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) named the apex generator $\mathcal M_x(\beta,c)$ of the structured categorical simplex as a Fourier-Mellin transform on $\mathbb Z/N$ of the centered log-ledger of a positive real ledger $x\in\mathbb R_{>0}^N$. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) worked the real-positive sector: the amplitude sphere $S^{N-1}_+\subset\mathbb R_{>0}^N$, Born closure $p_i=x_i^2/\sum_jx_j^2$, the cumulant tower, the radical Helmert ladder. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 3.7 established that on the real-positive sector the $n$-th-power Kummer cover is *trivial*, with the deck-group action collapsing because $\mu_n\cap\mathbb R_{>0}=\{1\}$. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) explicitly scoped the complex-amplitude extension — where the cover becomes non-trivial and the apex acquires phase structure — as a forward door (§6.1).

**Gap.** The complex-amplitude extension is not a cosmetic generalization. Replacing $\mathbb R_{>0}^N$ by $\mathbb C^N$ does four structurally distinct things at once: (i) it enlarges the closure symmetry from $S_N$ permutations to the unitary group $U(N)$; (ii) it activates the Kummer cover $\mu_n\subset S^1$ on each coordinate, giving a non-trivial deck group $(\mu_n)^N/\mu_n$ for the $n$-th-power closure; (iii) it introduces a phase fiber $T^{N-1}=U(1)^N/U(1)$ over each simplex point, with the real-positive sector recovered as the *decoherent* (phase-averaged) face; (iv) it forces the Fisher–Rao metric to be the real-positive restriction of a strictly larger projective metric, the Fubini–Study metric on $\mathbb{CP}^{N-1}$. The real-positive sector is one slice through a four-axis space (amplitude, phase, conductor, gauge). [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) worked the slice; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) builds the ambient.

**Action.** We construct the complex apex on $\mathbb C^N$. The complex amplitude $z\in\mathbb C^N$ is positioned at three nested layers — the amplitude sphere $S^{2N-1}\subset\mathbb C^N$, the projective space $\mathbb{CP}^{N-1}=S^{2N-1}/U(1)$, and the probability simplex $\Delta^{N-1}=\mathbb{CP}^{N-1}/T^{N-1}$ — connected by the **Hopf** and **toric** fibrations. The Born closure
$$\pi_{\mathrm{Born}}:\mathbb C^N\setminus\{0\}\longrightarrow\Delta^{N-1},\qquad z\longmapsto\Big(\frac{|z_i|^2}{\sum_j|z_j|^2}\Big)_{i=1}^N$$
factors as $\pi_{\mathrm{Born}}=\mu_{\mathrm{toric}}\circ\mathrm{Hopf}\circ\mathrm{rad}$ through these layers, with $\mu_{\mathrm{toric}}$ the moment map of the toric action of $T^{N-1}$ on $\mathbb{CP}^{N-1}$. We define the complex apex generator
$$\mathcal M_z(\beta,c):=\frac{1}{N}\sum_{s\in\mathbb Z/N}e^{\beta y_s(z)}\,\overline{\chi_c(s)},\qquad y_s(z):=\log z_s-\tfrac{1}{N}{\textstyle\sum_j}\log z_j,$$
phrased precisely below as a holomorphic function of $\beta\in\mathbb C$ on each Riemann-surface branch of the complex log of $z$. We then prove the **decoherence theorem** identifying [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s real-positive apex with the modulus-restriction of $\mathcal M_z$ from the complex amplitude to its modulus ledger, and the **Kummer-cover theorem** identifying the integer-$\beta$ samples on the complex side with sections of an explicit $\mu_N$-twisted line bundle over $\mathbb{CP}^{N-1}$.

**Result.** Six core claims of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442):

1. **Three-layer factorization of Born closure.** The map $\pi_{\mathrm{Born}}:\mathbb C^N\setminus\{0\}\to\Delta^{N-1}$ factors uniquely as $\mu_{\mathrm{toric}}\circ\mathrm{Hopf}\circ\mathrm{rad}$ (applied right-to-left): radial scaling to the sphere $S^{2N-1}$, Hopf projection to $\mathbb{CP}^{N-1}$ (modding out global phase $U(1)$), then the toric moment map to the simplex (modding out relative phases $T^{N-1}$). Each layer has a well-defined symmetry quotient.

2. **Fubini–Study restricts to Fisher–Rao on the decoherent face (re-derivation).** The Fubini–Study metric $g_{\mathrm{FS}}$ on $\mathbb{CP}^{N-1}$ restricts to one-quarter of the Fisher–Rao metric on the real-positive face under the square-root section. This is the classical FS / quantum-Fisher relation (Provost–Vallée 1980; Braunstein–Caves 1994; Bengtsson–Życzkowski 2017); we re-derive it in the categorical-simplex language to fix the attribution of the factor of $2$ in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s $d_{FR}=2\arccos\sum\sqrt{p_iq_i}$ to the **Born / square-root embedding** $p\mapsto\sqrt p$ (in agreement with [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §2), not the Hopf fibration: on the decoherent face the Hopf/global-phase quotient acts as an isometry, $d_{\mathrm{FS}}([\sqrt p],[\sqrt q])$ equals the unit-sphere geodesic distance $\arccos\sum\sqrt{p_iq_i}$, and the doubling lives entirely in the square root, at all $N$.

3. **Complex apex generator.** Define $\mathcal M_z(\beta,c)$ on $\mathbb C^N$ via complex centered log-ledger $y_s=\log z_s-\frac{1}{N}\sum_j\log z_j$ (with a canonical branch on the positive sector and analytic continuation onto the cut Riemann surface of the complex log). $\mathcal M_z$ is holomorphic in $\beta$ on each branch, and the real-positive evaluation recovers [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$.

4. **Decoherence theorem (modulus-phase reduction).** The complex apex generator splits termwise as
$$\mathcal M_z(\beta,c)=\frac{1}{N}\sum_s e^{\beta y^{(|z|)}_s}\cdot e^{i\beta y^{(\arg z)}_s}\,\overline{\chi_c(s)},$$
with $y^{(|z|)}_s$ the [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) centered log-ledger of the modulus ledger $|z|\in\mathbb R_{>0}^N$ and $y^{(\arg z)}_s$ the centered argument (\hyperlink{stmt:3-6}{Proposition~3.6}). The **modulus-restriction** $z\mapsto|z|$ — the operational projection of complex amplitude to measurement-basis modulus — sets every phase factor to $1$ and reduces $\mathcal M_z(\beta,c)$ to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_{|z|}(\beta,c)$ exactly. The real-positive sector is *exactly* the locus $U(1)\cdot\mathbb R_{>0}^N\subset\Omega_N$ on which the phase deformation is trivial for generic $\beta$ (\hyperlink{stmt:3-6}{Proposition~3.6}).

5. **Kummer-cover theorem.** The closure diagonal $\mathcal M_z(m,c)$ at integer $m$ has $(\mu_m)^N/\mu_m$ deck-group symmetry: replacing each $z_s$ by $\zeta_s z_s$ for $\zeta_s\in\mu_m$ leaves $|z_s|^{2m}$ invariant but multiplies the apex generator by $\prod_s\zeta_s^{\pm}$, encoding the Galois action on the moment diagonal as character-twisting on the cover.

6. **Qubit anchor at $N=2$.** The qubit case $\mathbb{CP}^1\cong S^2$ realizes the apex on the Bloch sphere, with the real-positive sector being the equatorial great circle $\{|0\rangle,|1\rangle\}$. The full Lee–Yang lattice of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5 lifts to a phase-twisted lattice in the complex $\beta$-plane parameterized by the Bloch-vector orientation.

**Harvest.** The *phase structure* of pure-state finite-dimensional quantum mechanics on $\mathbb C^N$ is not an extra principle: it is the *cover* of the categorical-simplex apex — the same Fourier-Mellin transform, lifted from $\mathbb R_{>0}^N$ to $\mathbb C^N$ via the canonical Hopf-and-toric fibrations of complex projective space. We use the slogans *decoherence is closure of phase* and *quantization is the cover* in a deliberately scoped sense: the cover captures the pure-state phase redundancy — global $U(1)$, relative $T^{N-1}$, and the $\mu_N$ branch ambiguity of root closures — and **not** the non-commutativity of observables, measurement back-action, unitary dynamics, or tensor-product/entanglement structure, which sit in the forward doors of \hyperref[sec:7]{§7}. Within that scope the real-positive sector is the decoherent face and the complex sector is the full bundle, and [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Conjecture 4 ("complex amplitude extension") is now a structure theorem rather than a conjecture.

**Keywords:** finite-dimensional quantum mechanics, complex projective space, Fubini–Study metric, Hopf fibration, toric moment map, Born closure, Kummer cover, deck group, decoherence, phase fiber, qubit, $SU(2)\to SO(3)$, quantum Fisher information, Bures metric, finite-categorical Fourier-Mellin.

---

## Cross-references from prior papers

This paper builds on specific results from earlier papers of the \heb{ל}-series; we list the dependencies explicitly.

| Cited result | Used for |
|---|---|
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.2 Definition 3.1 (additive apex generator $\mathcal M_x$) | Reduced from $\mathcal M_z$ in \hyperlink{stmt:3-5}{Proposition~3.5} (real-positive reduction) |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.3 Theorem 3.5 (closure diagonal) | Underlies \hyperref[sec:5]{§5} Kummer cover theorem at integer $\beta=m$ |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4 Proposition 3.7 (real-sector Kummer triviality) | Special case of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) \hyperlink{stmt:5-6}{Proposition~5.6} |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.6 Proposition 2.5 (Lee–Yang at $N=2$) | Lifted to phase-twisted lattice in \hyperref[sec:6]{§6} \hyperlink{stmt:6-2}{Proposition~6.2} |
| [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) (Fisher–Rao metric, $d_{FR}=2\arccos\sum\sqrt{p_iq_i}$) | Restriction of Fubini–Study in \hyperref[sec:2]{§2} \hyperlink{stmt:2-1}{Theorem~2.1} |
| [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) (Born closure $p_i=x_i^2/\sum x^2$) | Real-positive sector identified in \hyperref[sec:1-3]{§1.3} decoherent face |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.3 (Bhattacharyya coefficient $\sum\sqrt{p_iq_i}$) | \hyperlink{stmt:2-1}{Theorem~2.1} proof |
| [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Conjecture 4 (complex amplitude extension) | Promoted to structure theorem by \hyperref[sec:5]{§5} and \hyperref[sec:4]{§4} |

[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) introduces the complex amplitude apex $\mathcal M_z$, identified as the analytic continuation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$ to the cut Riemann surface of complex log over $\Omega_N=(\mathbb C^\times)^N$.

---

## Notation

We carry the notation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) and add the complex-amplitude layer.

| Symbol | Meaning |
|---|---|
| $N$ | Number of categorical outcomes, integer $\ge 2$. |
| $z=(z_1,\ldots,z_N)$ | Complex amplitude in $\mathbb C^N$. |
| $|z|^2$ | Componentwise modulus-squared: $|z|^2_i=|z_i|^2=z_i\bar z_i$. |
| $\|z\|$ | Euclidean norm: $\|z\|=(\sum_i|z_i|^2)^{1/2}$. |
| $|z|$ | Componentwise modulus ledger: $|z|=(|z_1|,\ldots,|z_N|)\in\mathbb R_{>0}^N$. |
| $S^{2N-1}$ | Unit sphere in $\mathbb C^N$, $\{z:\|z\|=1\}$. |
| $\mathbb{CP}^{N-1}$ | Complex projective space, $S^{2N-1}/U(1)$. |
| $\Delta^{N-1}$ | Probability simplex in $\mathbb R^N_{\ge 0}$ with $\sum_ip_i=1$. |
| $\mathring\Delta^{N-1}$ | Open simplex (strictly positive interior). |
| $T^{N-1}$ | The relative-phase torus $U(1)^N/U(1)$. |
| $\Omega_N$ | Configuration space of nowhere-vanishing complex amplitudes, $(\mathbb C^\times)^N$. |
| $\pi_{\mathrm{Born}}$ | Born closure $z\mapsto(|z_i|^2/\|z\|^2)_i:\mathbb C^N\setminus\{0\}\to\Delta^{N-1}$. |
| $\mathrm{Hopf}$ | Hopf projection $S^{2N-1}\to\mathbb{CP}^{N-1}$. |
| $\mu_{\mathrm{toric}}$ | Toric moment map $\mathbb{CP}^{N-1}\to\Delta^{N-1}$. |
| $g_{\mathrm{FS}}$ | Fubini–Study metric on $\mathbb{CP}^{N-1}$. |
| $g_{\mathrm{FR}}$ | Fisher–Rao metric on $\mathring\Delta^{N-1}$. |
| $d_{\mathrm{FS}},\,d_{\mathrm{FR}}$ | Fubini–Study, Fisher–Rao distance. |
| $\mathcal M_z(\beta,c)$ | Complex apex generator on $\Omega_N$ (\hyperlink{stmt:3-4}{Definition~3.4} below). |
| $\mathcal M_x(\beta,c)$ | [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) real-positive apex generator on $\mathbb R^N_{>0}$. |
| $y_s(z)$ | Complex centered log-ledger: $y_s=\log z_s-\frac{1}{N}\sum_j\log z_j\in\mathbb C$. |
| $y^{(|z|)}_s$ | Real part: modulus log-ledger $\ln|z_s|-\frac{1}{N}\sum_j\ln|z_j|\in\mathbb R$. |
| $y^{(\arg z)}_s$ | Imaginary part: centered argument $\arg z_s-\frac{1}{N}\sum_j\arg z_j\in\mathbb R$. |
| $G(z)$ | Complex geometric mean, an $N$-th root of $\prod_jz_j$; multi-valued, single-valued on the Kummer cover. |
| $\widehat{z^m}_c$ | $c$-th Fourier coefficient of the componentwise $m$-th power: $\frac{1}{N}\sum_s z_s^m\overline{\chi_c(s)}$. |
| $\arg(z_s)$ | Principal argument of $z_s$, in $(-\pi,\pi]$. |
| $\mu_n$ | Group of $n$-th roots of unity in $\mathbb C^\times$. |
| $(\mu_n)^N/\mu_n$ | Componentwise deck group of the $n$-th-power Kummer cover. |
| $\widetilde\Omega_N$ | Degree-$N$ Kummer cover of $\Omega_N\cap\mathbb{CP}^{N-1}$ on which $G(z)$ is single-valued (\hyperlink{stmt:5-1}{Definition~5.1}). |
| $\omega$ | Coordinate on the Kummer cover, $\omega^N=\prod_jz_j$. |
| $\rho_m$ | Deck-group character $\rho_m(\zeta)=\zeta^{-m}$ on $\mu_N$. |
| $\sigma_{\mathrm{R+}}$ | Real-positive embedding $\mathbb R_{>0}^N\hookrightarrow\Omega_N$ (the no-phase section). |
| $\mathcal R$ | Modulus-restriction map $z\mapsto|z|:\Omega_N\to\mathbb R_{>0}^N$. |
| $\mathcal P$ | Computational-basis dephasing channel $\rho\mapsto\sum_s\langle s|\rho|s\rangle|s\rangle\langle s|$. |
| $L_\rho$ | Centered modular Hamiltonian: $\log\rho-\frac{1}{N}\mathrm{tr}(\log\rho)\,I_N$. |
| $\langle\psi|\phi\rangle$ | Hermitian inner product on $\mathbb C^N$, $\sum_i\bar\psi_i\phi_i$. |
| $|z\rangle,\;\langle z|$ | Dirac notation for $z\in\mathbb C^N$ as ket / dual bra. |
| $\chi_c$ | Additive character on $\mathbb Z/N$: $\chi_c(s)=e^{2\pi ics/N}$. |
| $\mathcal O(k)$ | Holomorphic line bundle on $\mathbb{CP}^{N-1}$ of degree $k$; $\mathcal O(-1)$ is the tautological bundle. |

**Acronyms.** Each is expanded on first use in the body; this table is for reference.

| Acronym | Expansion |
|---|---|
| AJLS | Ay–Jost–Lê–Schwachhöfer (modern functional-analytic synthesis of information geometry). |
| CRT | Chinese Remainder Theorem. |
| DFT | Discrete Fourier transform. |
| FR | Fisher–Rao (metric / distance on the simplex). |
| FS | Fubini–Study (metric / distance on $\mathbb{CP}^{N-1}$). |
| ODE | Ordinary differential equation. |
| QFI | Quantum Fisher information. |
| RMS | Root mean square ($r=2$ power mean). |
| RH | Riemann hypothesis. |

**Conventions and dictionary.** Two notational conflicts deserve explicit attention.

(i) *Complex logarithm.* $\log z$ on $\mathbb C\setminus\{0\}$ is taken in the **principal branch** $\log z=\ln|z|+i\arg z$ with $\arg z\in(-\pi,\pi]$ and cut along the negative real axis, unless explicitly stated otherwise. Sheet shifts $\log z_s\mapsto\log z_s+2\pi ik_s$ are tracked component-wise in \hyperref[sec:3-4]{§3.4}.

(ii) *Gauge exponent $\beta$ across amplitude vs probability.* The exponent $\beta$ in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s $\mathcal M_z(\beta,c)$ refers to the **amplitude** ledger $z\in\mathbb C^N$, with closure $p_i=|z_i|^2/\|z\|^2$ producing probability under $\beta=2$ on the modulus restriction. A density-matrix formulation acting on Born probabilities $p$ would use $\beta_\rho=\beta/2$ (\hyperref[sec:4-5]{§4.5}); we write $\beta$ for the amplitude exponent throughout and explicitly note the half-factor where the probability convention appears.

(iii) *Source of the factor of $2$.* The factor of $2$ between Fisher–Rao and Fubini–Study distances in \hyperlink{stmt:2-1}{Theorem~2.1} is the **Born / square-root embedding** $p\mapsto\sqrt p:\Delta^{N-1}\to S^{N-1}_+$, not the Hopf fibration: on the decoherent face the Hopf/global-phase quotient acts as a local isometry (the vertical correction $|\langle\delta z|z\rangle|^2$ vanishes), so $d_{\mathrm{FS}}$ equals the unit-sphere geodesic distance and the doubling is the square root alone, at all $N$. This matches [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §2. The $SU(2)\to SO(3)$ double cover at $N=2$ is the *global-phase* $z\sim-z$ quotient; it fixes the radius of the Fubini–Study Bloch sphere ($\mathbb{CP}^1\cong S^2_{r=1/2}$) but does not supply the $d_{\mathrm{FR}}/d_{\mathrm{FS}}$ ratio (\hyperref[sec:2-2]{§2.2}).

---

## 1. The complex amplitude space and its three layers {#sec:1}

### 1.1 From real-positive to complex {#sec:1-1}

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) worked the real-positive sector: amplitudes $x\in\mathbb R_{>0}^N$, normalized to the positive face of the sphere $S^{N-1}_+:=S^{N-1}\cap\mathbb R^N_{\ge 0}$, with closure $p_i=x_i^2/\sum_jx_j^2$ producing probability vectors in the simplex $\Delta^{N-1}$. The natural symmetry of the configuration is the permutation group $S_N$, acting by relabeling outcomes.

The complex amplitude extension replaces $\mathbb R^N$ by $\mathbb C^N$ and the positive face by the full unit sphere $S^{2N-1}\subset\mathbb C^N$:
$$S^{2N-1}=\{z\in\mathbb C^N:\|z\|^2=\sum_i|z_i|^2=1\}.$$

The symmetry enlarges to $U(N)$, the unitary group, which acts transitively on $S^{2N-1}$ and preserves Hermitian inner products $\langle z|w\rangle=\sum_i\bar z_iw_i$. The positive face $S^{N-1}_+$ sits inside $S^{2N-1}$ as the diagonal "real-positive corner" where all $z_i$ are real and positive.

The Born closure $z\mapsto(|z_i|^2/\|z\|^2)_i$ extends straight to $\mathbb C^N\setminus\{0\}$ (it depends only on moduli, so phases are quotiented out). The map factors through three nested quotients corresponding to three distinct symmetries, which we now describe.

### 1.2 The three layers {#sec:1-2}

**Layer 1: radial scaling.** The cone $\mathbb C^N\setminus\{0\}$ deformation-retracts onto the sphere $S^{2N-1}$ via $z\mapsto z/\|z\|$. The symmetry quotiented out is the positive-real dilation $\mathbb R_{>0}^\times$, acting on $\mathbb C^N$ by $z\mapsto\lambda z$ for $\lambda>0$. The Born closure is invariant under this action.

**Layer 2: global phase (Hopf fibration).** The unitary group $U(1)\subset\mathbb C^\times$ acts on $S^{2N-1}$ by uniform phase rotation: $z\mapsto e^{i\theta}z$. This is the **global phase symmetry** of quantum mechanics. The quotient is the complex projective space
$$\mathbb{CP}^{N-1}:=S^{2N-1}/U(1),$$
and the projection $\mathrm{Hopf}:S^{2N-1}\to\mathbb{CP}^{N-1}$ is the **Hopf fibration** (in classical terminology, especially for $N=2$ where $\mathrm{Hopf}:S^3\to S^2$).

**Layer 3: relative phases (toric moment map).** The torus $T^N=U(1)^N$ acts on $\mathbb C^N$ componentwise: $(\theta_1,\ldots,\theta_N)\cdot z=(e^{i\theta_1}z_1,\ldots,e^{i\theta_N}z_N)$. The diagonal subgroup $U(1)\subset T^N$ acts by global phase (the symmetry of Layer 2). The quotient torus
$$T^{N-1}:=T^N/U(1)$$
acts effectively on $\mathbb{CP}^{N-1}$ by relative phases, preserving moduli but rotating the relative arguments $\arg z_i-\arg z_1$. The quotient
$$\mu_{\mathrm{toric}}:\mathbb{CP}^{N-1}\to\Delta^{N-1},\qquad[z]\mapsto\Big(\frac{|z_i|^2}{\|z\|^2}\Big)_i$$
is the **moment map** of this toric action in the standard sense of symplectic / toric geometry (Atiyah 1982; Guillemin–Sternberg 1982), and its image is the probability simplex.

\hypertarget{stmt:1-1}{}
**Theorem 1.1 (Three-layer factorization of Born closure).** The Born closure factors as a composition
$$\pi_{\mathrm{Born}}:\mathbb C^N\setminus\{0\}\xrightarrow{\mathrm{rad}}S^{2N-1}\xrightarrow{\mathrm{Hopf}}\mathbb{CP}^{N-1}\xrightarrow{\mu_{\mathrm{toric}}}\Delta^{N-1},$$
where each arrow is the quotient by a connected Lie subgroup of the structure group $\mathbb R_{>0}^\times\times U(1)^N$ of the action $\mathbb C^N\setminus\{0\}\circlearrowleft$ by positive scaling and componentwise phase:
- $\mathrm{rad}$ quotients by $\mathbb R_{>0}^\times$ (radial scaling);
- $\mathrm{Hopf}$ quotients by the diagonal $U(1)$ (global phase);
- $\mu_{\mathrm{toric}}$ quotients by $T^{N-1}=U(1)^N/U(1)$ (relative phases).

The full structure group $\mathbb R_{>0}^\times\times U(1)^N$ acts on $\mathbb C^N\setminus\{0\}$ with quotient $\Delta^{N-1}$.

**Proof.** Each map is the quotient by its named group action; commutativity of these three (radial scaling, global phase, relative phases) makes the composition well-defined and unique. The structure group has dimension $1+N=N+1$, the fiber over a generic point of $\Delta^{N-1}$ (with no $p_i=0$) has dimension $N+1$, and the simplex has dimension $N-1$; the total dimension $N+1+N-1=2N=\dim_{\mathbb R}\mathbb C^N$ checks. $\square$

### 1.3 The real-positive sector as decoherent face {#sec:1-3}

The real-positive sector $\mathbb R_{>0}^N\subset\mathbb C^N$ corresponds to choosing all $\arg z_s=0$, a single point in the relative-phase torus $T^{N-1}$ (the "all-zero phases" representative of each toric fiber). Equivalently, the positive face $S^{N-1}_+\subset S^{2N-1}$ is a *section* of both the Hopf fibration (a choice of global-phase representative) and the toric fibration (a choice of relative-phase representative).

\hypertarget{stmt:1-2}{}
**Definition 1.2 (Decoherent face).** The **decoherent face** of the complex amplitude space is the real-positive sector $S^{N-1}_+\subset S^{2N-1}$, equivalently the image of the section $p\mapsto(\sqrt{p_1},\ldots,\sqrt{p_N})$ of $\pi_{\mathrm{Born}}$. The corresponding map $\Delta^{N-1}\to S^{N-1}_+$ is the **square-root section**.

The square-root section is the foundation of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart. [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s framing places it as one *section* of the toric/Hopf fibrations among many: the all-phases-zero choice. Other sections exist (e.g., $z_s=\sqrt{p_s}e^{i\phi_s}$ for any phase pattern $\phi$), and the choice of section is a *gauge* in the precise sense of \hyperref[sec:1-4]{§1.4} below.

### 1.4 Phase as a gauge choice {#sec:1-4}

The terminology of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) (the gauge corridor parameterized by $\beta$) and the terminology here ("global phase gauge" / "relative phase gauge") are not metaphorically related — they are instances of the same principle. The full structure group $\mathbb R_{>0}^\times\times U(1)^N$ acting on $\mathbb C^N\setminus\{0\}$ is, like the $L^r$ gauge corridor of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §1.3, a choice of representative on a multi-parameter family of equivalence classes. [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s gauge selection answered "what is additive?" by choosing $\beta$; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s gauge selection answers "what is the phase?" by choosing a section of the toric/Hopf fibrations. The two questions are independent (one is real, the other is complex), and the gauge corridor of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) lifts to a $(N+1)$-parameter gauge structure on $\mathbb C^N$ — one $\beta$ in $\mathbb R$ and $N$ phase angles in $T^N$, with the diagonal $U(1)$ being the global-phase quotient.

We do not develop the full $(N+1)$-parameter gauge corridor in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442); we treat the phase axes as discrete (toric) symmetries with non-trivial $\mu_n$ subgroup structure at integer $\beta=m$ in the closure diagonal.

---

## 2. The Fubini–Study metric and the projective angle {#sec:2}

### 2.1 Fubini–Study and Fisher–Rao {#sec:2-1}

The **Fubini–Study metric** $g_{\mathrm{FS}}$ on $\mathbb{CP}^{N-1}$ is the unique (up to scale) $U(N)$-invariant Kähler metric, obtained by pushing forward the round metric on $S^{2N-1}$ through the Hopf fibration:
$$g_{\mathrm{FS}}([z])(\delta_1[z],\delta_2[z])=\mathrm{Re}\Big(\frac{\langle\delta_1z|\delta_2z\rangle}{\|z\|^2}-\frac{\langle\delta_1z|z\rangle\langle z|\delta_2z\rangle}{\|z\|^4}\Big),$$
on tangent vectors orthogonal to $z$ in the Hermitian sense. The corresponding **Fubini–Study distance** is
$$d_{\mathrm{FS}}([z],[w])=\arccos\Big(\frac{|\langle z|w\rangle|}{\|z\|\|w\|}\Big).$$

The **Fisher–Rao metric** $g_{\mathrm{FR}}$ on the open simplex $\mathring\Delta^{N-1}$ is the unique (up to scale) Riemannian metric invariant under stochastic transformations preserving relative entropy (Chentsov 1982; Amari–Nagaoka 2000), with Fisher–Rao distance
$$d_{\mathrm{FR}}(p,q)=2\arccos\sum_i\sqrt{p_iq_i}.$$

\hypertarget{stmt:2-1}{}
**Theorem 2.1 (Fubini–Study restricts to Fisher–Rao on the decoherent face).** Let $\sigma:\mathring\Delta^{N-1}\to S^{N-1}_+$, $\sigma(p)=\sqrt p=(\sqrt{p_1},\ldots,\sqrt{p_N})$, be the square-root section. Then
$$d_{\mathrm{FS}}\big([\sqrt p],[\sqrt q]\big)=\tfrac{1}{2}d_{\mathrm{FR}}(p,q)\quad\text{for all }p,q\in\mathring\Delta^{N-1},$$
and the corresponding infinitesimal identity holds:
$$(\mathrm{Hopf}\circ\sigma)^*g_{\mathrm{FS}}=\tfrac{1}{4}\,g_{\mathrm{FR}}\quad\text{on }\mathring\Delta^{N-1}.$$

**Proof.** *(Distance.)* For $z=\sqrt p$ and $w=\sqrt q$ on the decoherent face, $\langle z|w\rangle=\sum_i\sqrt{p_i}\sqrt{q_i}\in\mathbb R_{\ge 0}$, so $|\langle z|w\rangle|=\sum_i\sqrt{p_iq_i}$ — the Bhattacharyya coefficient (Bhattacharyya 1943). Since $\|z\|=\|w\|=1$ on the section,
$$d_{\mathrm{FS}}\big([\sqrt p],[\sqrt q]\big)=\arccos\sum_i\sqrt{p_iq_i}=\tfrac{1}{2}d_{\mathrm{FR}}(p,q),$$
using $d_{\mathrm{FR}}(p,q)=2\arccos\sum_i\sqrt{p_iq_i}$ ([\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)).

*(Metric.)* Fix $p\in\mathring\Delta^{N-1}$ and a tangent vector $v\in T_p\Delta^{N-1}=\{v\in\mathbb R^N:\sum_iv_i=0\}$. The Fisher–Rao metric is $g_{\mathrm{FR}}(p)(v,v)=\sum_iv_i^2/p_i$ (Amari–Nagaoka 2000). The differential of the square-root section is $d\sigma(p)(v)=(v_1/(2\sqrt{p_1}),\ldots,v_N/(2\sqrt{p_N}))$, which is a real tangent vector to $S^{N-1}_+\subset S^{2N-1}\subset\mathbb C^N$ at $z=\sqrt p$.

Pull back the Fubini–Study metric in its definition (\hyperref[sec:2-1]{§2.1}) at $z=\sqrt p$ with $\delta z=d\sigma(p)(v)$. Since $\sqrt p\in\mathbb R^N$ and $\delta z\in\mathbb R^N$, the Hermitian inner product reduces to the real inner product:
$$\langle\delta z|\delta z\rangle=\sum_i\Big(\frac{v_i}{2\sqrt{p_i}}\Big)^2=\frac{1}{4}\sum_i\frac{v_i^2}{p_i},\qquad\langle\delta z|z\rangle=\sum_i\sqrt{p_i}\cdot\frac{v_i}{2\sqrt{p_i}}=\frac{1}{2}\sum_iv_i=0$$
(the last equality from $\sum_iv_i=0$, since $v$ is tangent to the simplex). Substituting into the Fubini–Study formula at $\|z\|=1$,
$$g_{\mathrm{FS}}(\sqrt p)(\delta z,\delta z)=\langle\delta z|\delta z\rangle-|\langle\delta z|z\rangle|^2=\frac{1}{4}\sum_i\frac{v_i^2}{p_i}-0=\frac{1}{4}g_{\mathrm{FR}}(p)(v,v).$$
Polarizing the quadratic identity to a bilinear identity gives $(\mathrm{Hopf}\circ\sigma)^*g_{\mathrm{FS}}=\tfrac{1}{4}g_{\mathrm{FR}}$ as quadratic forms on $T_p\mathring\Delta^{N-1}$.

The metric identity $g_{\mathrm{FS}}=\tfrac{1}{4}g_{\mathrm{FR}}$ and the distance identity $d_{\mathrm{FS}}=\tfrac{1}{2}d_{\mathrm{FR}}$ are consistent under the integration of length: scaling the metric by $1/4$ scales lengths by $1/2$, and the geodesics on the decoherent face $S^{N-1}_+$ are great-circle arcs in $S^{2N-1}$ (the round-sphere geodesics restricted to the positive face), which are the square-root pullbacks of the Fisher–Rao geodesics on $\mathring\Delta^{N-1}$. $\square$

The **factor of $2$** in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s Fisher–Rao distance is therefore the **Born / square-root embedding** $\sigma:p\mapsto\sqrt p$, *not* the Hopf fibration — exactly as [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §2 records ("the angle was waiting for the square"). The proof makes the separation explicit: the Hopf/global-phase vertical correction $-|\langle\delta z|z\rangle|^2$ vanishes identically on the decoherent face (since $\langle\delta z|z\rangle=\tfrac12\sum_iv_i=0$ for real $\delta z$ with $\sum_iv_i=0$), so the Hopf submersion acts there as a *local isometry on the horizontal real section* — it contributes the identity, ratio $1$. The full factor enters through $\langle\delta z|\delta z\rangle=\tfrac14\sum_iv_i^2/p_i$, the square-root differential $d\sigma(v)_i=v_i/(2\sqrt{p_i})$. Concretely: on the positive orthant $\sqrt p,\sqrt q$ are real and never antipodal (pairwise angle $\le\pi/2$), so $d_{\mathrm{FS}}([\sqrt p],[\sqrt q])=\arccos\sum_i\sqrt{p_iq_i}$ equals the unit-sphere geodesic distance, and the doubling sits entirely in the square-root map $\Delta^{N-1}\to S^{N-1}_+$, where it sends arc length on the probability simplex to twice the arc length on the amplitude sphere. The Hopf fibration *defines* the Fubini–Study metric; it does not supply the number.

**Status of \hyperlink{stmt:2-1}{Theorem~2.1} (re-derivation, not a new result).** The relation $g_{\mathrm{FS}}=\tfrac14 g_{\mathrm{FR}}$ on the decoherent face is classical — it is the standard correspondence between the Fubini–Study metric, the quantum Fisher information, and the classical Fisher–Rao metric on the diagonal/decoherent stratum (Provost–Vallée 1980; Braunstein–Caves 1994; Bengtsson–Życzkowski 2017). We include it as a clean re-derivation in the categorical-simplex language, for two purposes only: to fix the attribution of the factor of $2$ to the Born square root (settling the apparent tension with the Hopf reading), and to set up the genuinely new object of this paper — the Kummer-cover reading of the closure diagonal in \hyperref[sec:5]{§5}, where the integer-$\beta$ apex generators become sections of an explicit $\mu_N$-twisted line bundle. \hyperref[sec:5]{§5}, not \hyperlink{stmt:2-1}{Theorem~2.1}, carries the novel content of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s metric/geometry layer.

### 2.2 The qubit case $N=2$ {#sec:2-2}

For $N=2$, $\mathbb{CP}^1\cong S^2$ (the Bloch sphere), and the Hopf fibration is the classical $S^3\to S^2$ with fiber $S^1$. The decoherent face $S^1_+\subset S^3$ projects through Hopf to a great circle on $S^2$ (the "equator" connecting $|0\rangle$ and $|1\rangle$). It is worth separating two distinct factors of $2$ that both appear here, since they are easily conflated:

- The **$d_{\mathrm{FR}}=2d_{\mathrm{FS}}$ doubling** is the Born / square root, as in \hyperlink{stmt:2-1}{Theorem~2.1}. Even at $N=2$ it is the squaring: a real amplitude $\cos(\theta/2)|0\rangle+\sin(\theta/2)|1\rangle$ sits at Hilbert half-angle $\theta/2$, while its Born image sits at Bloch polar angle $\theta$, with $\cos\theta=p_0-p_1$. This factor persists at all $N$.
- The **$SU(2)\to SO(3)$ double cover** is the *global-phase* quotient $z\sim-z$ (the $\theta=\pi$ fiber element). It controls the **radius** of the Fubini–Study Bloch sphere — $\mathbb{CP}^1$ with $g_{\mathrm{FS}}$ is $S^2$ of radius $\tfrac12$, not the unit sphere — and is a low-dimensional coincidence of $N=2$ that does not extend.

The $d_{\mathrm{FR}}/d_{\mathrm{FS}}$ ratio is the first item, not the second: on the decoherent face the Hopf/global-phase quotient acts as an isometry (\hyperlink{stmt:2-1}{Theorem~2.1} proof), so the $SU(2)\to SO(3)$ identification does not supply the doubling.

We return to the qubit anchor in \hyperref[sec:6]{§6}.

---

## 3. The complex apex generator $\mathcal M_z(\beta,c)$ {#sec:3}

This section is the technical centerpiece. We extend [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s apex generator from $\mathbb R_{>0}^N$ to $\mathbb C^N\setminus\bigcup_s\{z_s=0\}$, define the complex centered log-ledger by componentwise complex logarithm, identify the resulting $\mathcal M_z(\beta,c)$ as a holomorphic function of $\beta\in\mathbb C$ on each chosen branch, derive its reduction to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$ on the decoherent face, and characterize the branch structure (which becomes the literal Kummer-cover data of \hyperref[sec:5]{§5}).

### 3.1 The complex centered log-ledger {#sec:3-1}

We work on the open subset
$$\Omega_N:=\{z\in\mathbb C^N:z_s\ne 0\text{ for every }s\}=\big(\mathbb C^\times\big)^N\subset\mathbb C^N,$$
the configuration space of nowhere-vanishing complex amplitudes. The closure of $\Omega_N$ inside $\mathbb C^N$ adds the coordinate hyperplanes $\{z_s=0\}$, on which one or more amplitudes vanish; these correspond to *boundary* simplex points (some $p_s=0$ under Born closure) and require separate treatment.

**Branch choice.** For each $s$, choose a branch cut of the complex logarithm $\log z_s$. The default choice is the **principal branch**, $\arg z_s\in(-\pi,\pi]$ with the cut along the negative real axis. On the real-positive sector $z_s>0$ this branch is real-analytic and agrees with $\ln z_s$. We will track sheet shifts $\log z_s\mapsto\log z_s+2\pi ik_s$ ($k_s\in\mathbb Z$) explicitly in §3.5.

\hypertarget{stmt:3-1}{}
**Definition 3.1 (Complex centered log-ledger).** For $z\in\Omega_N$ with a chosen branch of $\log z_s$ for each coordinate $s$,
$$y_s(z):=\log z_s-\frac{1}{N}\sum_{j=1}^N\log z_j,\qquad s=1,\ldots,N.$$
The vector $y=(y_1,\ldots,y_N)\in\mathbb C^N$ satisfies $\sum_s y_s=0$, hence lies in the complex mean-zero hyperplane $H_N\otimes\mathbb C$.

\hypertarget{stmt:3-2}{}
**Lemma 3.2 (Gauge invariance and modulus-phase splitting).**

(a) *Positive-scaling invariance.* For $\lambda\in\mathbb R_{>0}$, $y_s(\lambda z)=y_s(z)$. So $y$ depends only on the ray $[z]\in\mathbb C^N/\mathbb R_{>0}^\times$.

(b) *Global-phase invariance.* For $\alpha\in\mathbb R$, $y_s(e^{i\alpha}z)=y_s(z)$. So $y$ descends to the global-phase quotient $\mathbb C^N\setminus\{0\}/(\mathbb R_{>0}^\times\times U(1))$ (modulo branch choices, addressed in \hyperref[sec:3-4]{§3.4}).

(c) *Modulus-phase splitting.* Writing $z_s=|z_s|e^{i\arg z_s}$ on the principal branch,
$$\begin{aligned}
y_s(z)&=y^{(|z|)}_s+i\,y^{(\arg z)}_s,\qquad\text{where}\\
y^{(|z|)}_s&:=\ln|z_s|-\tfrac{1}{N}\sum_j\ln|z_j|\in\mathbb R,\\
y^{(\arg z)}_s&:=\arg z_s-\tfrac{1}{N}\sum_j\arg z_j\in\mathbb R.
\end{aligned}$$
The real part is the [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) centered log-ledger of the modulus ledger $|z|=(|z_1|,\ldots,|z_N|)\in\mathbb R_{>0}^N$. The imaginary part is the **centered argument**, the centered version of the phase pattern.

**Proof.** (a) $\log(\lambda z_s)=\log\lambda+\log z_s$ on the principal branch, and the constant $\log\lambda$ cancels under centering. (b) $\log(e^{i\alpha}z_s)=i\alpha+\log z_s$ similarly cancels. (c) $\log z_s=\ln|z_s|+i\arg z_s$ on the principal branch; linearity of the centering operation separates real and imaginary parts. $\square$

### 3.2 Definition of the complex apex generator {#sec:3-2}

\hypertarget{stmt:3-3}{}
**Definition 3.3 (Complex apex generator).** For $z\in\Omega_N$ with a chosen branch of $\log z_s$ for each $s$, $\beta\in\mathbb C$, and $c\in\widehat{\mathbb Z/N}$, the **complex apex generator** is
$$\boxed{\mathcal M_z(\beta,c):=\frac{1}{N}\sum_{s\in\mathbb Z/N}e^{\beta y_s(z)}\,\overline{\chi_c(s)},}$$
where $y_s(z)$ is the complex centered log-ledger of \hyperlink{stmt:3-1}{Definition~3.1}.

The placement of $\beta$ in the exponent and $c$ in the character index is identical to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Definition 3.1; the only change is that $y_s$ is now complex-valued.

\hypertarget{stmt:3-4}{}
**Proposition 3.4 (Holomorphy in $\beta$).** For each fixed branch choice and each fixed $z\in\Omega_N$, $\mathcal M_z(\cdot,c):\mathbb C\to\mathbb C$ is entire in $\beta\in\mathbb C$.

**Proof.** Each summand $e^{\beta y_s(z)}\overline{\chi_c(s)}$ is entire in $\beta$ (composition of the linear map $\beta\mapsto\beta y_s(z)$ with the entire exponential, multiplied by a $\beta$-independent constant). A finite sum of entire functions is entire. $\square$

**Reduction to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) on the real-positive sector.**

\hypertarget{stmt:3-5}{}
**Proposition 3.5 (Real-positive reduction).** If $z\in\mathbb R_{>0}^N\subset\Omega_N$ and the principal branch is chosen for every coordinate, then $y_s(z)\in\mathbb R$ for every $s$, and
$$\mathcal M_z(\beta,c)=\mathcal M_x(\beta,c)\quad\text{with }x:=z\in\mathbb R_{>0}^N,$$
where $\mathcal M_x$ is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s real-positive apex generator. In particular, the entire holomorphic family $\{\mathcal M_z(\cdot,c):z\in\Omega_N\}$ extends [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\{\mathcal M_x(\cdot,c):x\in\mathbb R_{>0}^N\}$ off the real-positive sector.

**Proof.** For $z_s>0$, $\log z_s=\ln z_s\in\mathbb R$ on the principal branch, so $y_s(z)\in\mathbb R$. Substituting into \hyperlink{stmt:3-3}{Definition~3.3} and comparing to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Definition 3.1 yields the equality. The holomorphic extension follows from \hyperlink{stmt:3-4}{Proposition~3.4} plus the fact that $\Omega_N$ is an open complex manifold containing $\mathbb R_{>0}^N$ as a real-analytic submanifold. $\square$

### 3.3 Modulus-phase factorization {#sec:3-3}

Combining \hyperlink{stmt:3-2}{Lemma~3.2}(c) with \hyperlink{stmt:3-3}{Definition~3.3} yields a clean modulus-phase factorization of the complex apex.

\hypertarget{stmt:3-6}{}
**Proposition 3.6 (Modulus-phase factorization).** For $z\in\Omega_N$,
$$\mathcal M_z(\beta,c)=\frac{1}{N}\sum_{s}e^{\beta y^{(|z|)}_s}\,e^{i\beta y^{(\arg z)}_s}\,\overline{\chi_c(s)}.$$
The first exponential factor depends only on the moduli $|z|=(|z_1|,\ldots,|z_N|)$ and reproduces [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$ structure (at $x=|z|$); the second exponential factor depends only on the centered argument $y^{(\arg z)}_s$ and encodes the phase content. In particular, for every $\beta\in\mathbb C\setminus(2\pi\mathbb Q)$,
$$\big[\,\mathcal M_z(\beta,c)=\mathcal M_{|z|}(\beta,c)\ \text{ for all }c\in\widehat{\mathbb Z/N}\,\big]\quad\Longleftrightarrow\quad z\in U(1)\cdot\mathbb R_{>0}^N$$
(a global-phase rotation of the real-positive sector). The quantifier "for all $c$" is essential for $(\Rightarrow)$: at a single fixed $c$ the character sum can vanish by accidental cancellation without the phases being trivial.

**Proof.** Direct from \hyperlink{stmt:3-1}{Definition~3.1} and \hyperlink{stmt:3-2}{Lemma~3.2}(c): $y_s=y^{(|z|)}_s+iy^{(\arg z)}_s$, so $e^{\beta y_s}=e^{\beta y^{(|z|)}_s}e^{i\beta y^{(\arg z)}_s}$. Substituting into \hyperlink{stmt:3-3}{Definition~3.3} yields the factorization. For $(\Leftarrow)$, $z\in U(1)\cdot\mathbb R_{>0}^N$ gives $y^{(\arg z)}_s=0$ for every $s$, so every phase factor is $1$ and $\mathcal M_z(\beta,c)=\mathcal M_{|z|}(\beta,c)$ for all $c$. For $(\Rightarrow)$, equality at *all* $c$ means the two functions $s\mapsto e^{\beta y_s}$ and $s\mapsto e^{\beta y^{(|z|)}_s}$ on $\mathbb Z/N$ have identical Fourier coefficients, hence are equal pointwise: $e^{\beta y^{(|z|)}_s}e^{i\beta y^{(\arg z)}_s}=e^{\beta y^{(|z|)}_s}$ for every $s$. Since $e^{\beta y^{(|z|)}_s}\ne 0$, every phase factor $e^{i\beta y^{(\arg z)}_s}=1$, i.e., $\beta y^{(\arg z)}_s\in 2\pi\mathbb Z$ for every $s$. For $\beta\notin 2\pi\mathbb Q$, this forces $y^{(\arg z)}_s=0$, equivalently $z$ has uniform phase, equivalently $z\in U(1)\cdot\mathbb R_{>0}^N$. (For $\beta\in 2\pi\mathbb Q$ the lattice of "accidental zeros" $y^{(\arg z)}\in(2\pi/\beta)\mathbb Z^N$ admits additional solutions; these are precisely the $\mu_N$-translates that the Kummer-cover formalism of \hyperref[sec:5]{§5} organizes.) $\square$

\hypertarget{stmt:3-7}{}
**Remark 3.7 (Comparison to the real-positive apex).** \hyperlink{stmt:3-6}{Proposition~3.6} says that $\mathcal M_z(\beta,c)$ splits as a *deformation* of $\mathcal M_{|z|}(\beta,c)$ by phase factors $e^{i\beta y^{(\arg z)}_s}$. The real-positive sector is *exactly* the fixed locus of "no deformation" for generic $\beta$, equal to $U(1)\cdot\mathbb R_{>0}^N$ on the global-phase quotient. This is the cleanest formulation of the slogan **"the real-positive sector is the no-phase section"** of the complex apex.

### 3.4 Branch structure: the Kummer cover seen from $\beta$ {#sec:3-4}

\hyperlink{stmt:3-1}{Definition~3.1} depends on a branch choice for each $\log z_s$. We characterize how $\mathcal M_z(\beta,c)$ changes when the branch shifts.

\hypertarget{stmt:3-8}{}
**Proposition 3.8 (Branch-shift formula).** Replace the chosen branch of $\log z_s$ by $\log z_s+2\pi ik_s$ for some integer shift vector $k=(k_1,\ldots,k_N)\in\mathbb Z^N$. The centered log-ledger transforms as
$$y_s(z)\longmapsto y_s(z)+2\pi i\big(k_s-\bar k\big),\qquad\bar k:=\tfrac{1}{N}{\textstyle\sum_j}k_j,$$
and the apex generator transforms as
$$\mathcal M_z(\beta,c)\longmapsto\frac{1}{N}\sum_s e^{2\pi i\beta(k_s-\bar k)}\,e^{\beta y_s(z)}\,\overline{\chi_c(s)}.$$
In particular:

(a) If $k=(k_0,k_0,\ldots,k_0)$ is the uniform shift, $k_s-\bar k=0$ for every $s$ and $\mathcal M_z$ is invariant. (Uniform branch shift is the global-phase ambiguity, already quotiented in \hyperlink{stmt:3-2}{Lemma~3.2}(b).)

(b) For non-uniform $k$ and $\beta\in\mathbb C$, the apex generator is multi-valued on the global-phase quotient $\mathbb C^N\setminus\{0\}/U(1)$ unless $\beta(k_s-\bar k)\in\mathbb Z$ for every admissible non-uniform $k$.

(c) For integer $\beta=m\in\mathbb Z$, the condition in (b) reduces to $m(k_s-\bar k)\in\mathbb Z$ for every $k\in\mathbb Z^N$. Taking $k=e_s$ (the $s$-th standard basis vector) gives $m(1-1/N)\in\mathbb Z$, i.e., $N\mid m$. Hence $\mathcal M_z(m,c)$ is single-valued on the global-phase quotient (and thus on $\mathbb{CP}^{N-1}$ after the toric quotient) precisely when $N\mid m$; for $N\nmid m$ it is multi-valued, with deck group the cyclic factor $\mu_N$ at each branch shift.

**Proof.** The branch-shift transformation rule is immediate from $\log z_s\mapsto\log z_s+2\pi ik_s$ and the linearity of the centering operation. Substituting into \hyperlink{stmt:3-3}{Definition~3.3} produces the stated form. (a) is immediate. (b) follows because $\mathcal M_z$ as a function on $\mathbb C^N$ (with chosen branches) descends to the global-phase quotient iff branch shifts preserve its value. (c) reduces the integrality condition to a single test on a basis vector. $\square$

\hypertarget{stmt:3-9}{}
**Remark 3.9 (Cover structure preview).** \hyperlink{stmt:3-8}{Proposition~3.8} is the precise statement of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4's "naturally organized by the Kummer cover" in the complex case. The closure diagonal at integer $\beta=m$ acquires the deck group $\mu_N/\mu_{\gcd(N,m)}$ at each coordinate (the obstruction to $m(k_s-\bar k)\in\mathbb Z$ for arbitrary $k_s$), and the global deck group of the cover $\widetilde{\mathbb{CP}^{N-1}}\to\mathbb{CP}^{N-1}$ on which $\mathcal M_z(m,\cdot)$ is single-valued is $(\mu_N)^N/\mu_N$ modulo the integrality condition $\sum_s k_s\equiv 0\pmod N$. We develop the full deck group action in \hyperref[sec:5]{§5} (the **Kummer-cover theorem**); the operational message of \hyperref[sec:3]{§3} is that the cover structure is *already visible* in the branch-shift behavior of $\mathcal M_z$, and reduces to the trivial cover precisely on the real-positive sector where $\arg z_s=0$ uniquely fixes every branch.

### 3.5 Summary: the complex apex as analytic continuation of the real apex {#sec:3-5}

The complex apex generator $\mathcal M_z(\beta,c)$ is the analytic continuation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x(\beta,c)$ from $\mathbb R_{>0}^N$ to $\Omega_N=(\mathbb C^\times)^N$, treated as a function on the universal cover of $\Omega_N$ in $z$ (via branch choices for $\log z_s$) and entire in $\beta$ on each fixed branch. Three structural features distinguish it from $\mathcal M_x$:

1. **Phase factor.** \hyperlink{stmt:3-6}{Proposition~3.6} gives the modulus-phase splitting; the complex apex deforms the real apex by phase exponentials.
2. **Branch dependence.** \hyperlink{stmt:3-8}{Proposition~3.8} gives the branch-shift formula; the deck group of the Kummer cover acts on the integer-$\beta$ samples.
3. **Holomorphy in $\beta$.** \hyperlink{stmt:3-4}{Proposition~3.4} lifts [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 2.2's real-analytic statement to genuine holomorphy on all of $\mathbb C$.

The decoherence theorem of \hyperref[sec:4]{§4} connects feature (1) to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$ via phase-modulus separation; the Kummer-cover theorem of \hyperref[sec:5]{§5} makes feature (2) into a literal Galois statement on the integer samples; and the Lee–Yang lattice of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5 lifts via feature (3) to a phase-twisted lattice on the qubit case (\hyperref[sec:6]{§6}).

---

## 4. The decoherence theorem {#sec:4}

This section is the bridge between [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s complex apex generator $\mathcal M_z$ and [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s real-positive apex $\mathcal M_x$. The bridge is the **modulus-restriction map** $\mathcal R:z\mapsto|z|$, the operational measurement-basis projection that ignores phase content and keeps only the Born probabilities. \hyperlink{stmt:4-2}{Theorem~4.2} below states that $\mathcal R$ pulls the complex apex back to the classical apex on the modulus ledger; \hyperlink{stmt:4-3}{Proposition~4.3} quantifies the gap between the two as a phase-deformation factor; \hyperref[sec:4-4]{§4.4} explains why the naive $T^{N-1}$-average of $\mathcal M_z$ is the *wrong* candidate for decoherence at integer $\beta$; \hyperref[sec:4-5]{§4.5} promotes the pure-state case to a density-matrix decoherence theorem (\hyperlink{stmt:4-5}{Theorem~4.5}) and scopes the mixed-state generalization as a forward door.

### 4.1 The modulus-restriction map {#sec:4-1}

\hypertarget{stmt:4-1}{}
**Definition 4.1 (Modulus-restriction).** The **modulus-restriction map** on the complex amplitude configuration space is
$$\mathcal R:\Omega_N\longrightarrow\mathbb R_{>0}^N,\qquad\mathcal R(z):=(|z_1|,|z_2|,\ldots,|z_N|).$$
The map descends to the global-phase quotient $\Omega_N/U(1)\subset\mathbb{CP}^{N-1}$ (since $|z_s|$ is invariant under $z\mapsto e^{i\alpha}z$) and further to the toric quotient $\Omega_N/(U(1)\times T^{N-1})$, the open simplex $\mathring\Delta^{N-1}$, where it reduces to $z\mapsto(|z_i|^2/\|z\|^2)_i=\pi_{\mathrm{Born}}(z)$ followed by the square-root section $p\mapsto\sqrt p$.

Operationally, $\mathcal R$ is the **measurement-basis modulus projection**: given a complex amplitude $z\in\mathbb C^N$, return the vector of moduli $|z|\in\mathbb R_{>0}^N$. This is the natural projection associated to a von Neumann measurement in the computational basis, in which the measurement outcomes are the moduli (or, after Born closure, the probabilities), and the phases are erased.

### 4.2 The decoherence theorem {#sec:4-2}

\hypertarget{stmt:4-2}{}
**Theorem 4.2 (Decoherence as modulus-restriction).** For every $z\in\Omega_N$, every $\beta\in\mathbb C$, and every character $c\in\widehat{\mathbb Z/N}$, the apex generator of the dephased (no-phase) ledger $\sigma_{\mathrm{R+}}(\mathcal R(z))$ equals the classical apex of the modulus ledger:
$$\boxed{\mathcal M_{\sigma_{\mathrm{R+}}(\mathcal R(z))}(\beta,c)=\mathcal M_{|z|}(\beta,c),}$$
where $\mathcal R(z)=|z|$ is the modulus-restriction (\hyperlink{stmt:4-1}{Definition~4.1}), $\sigma_{\mathrm{R+}}:\mathbb R_{>0}^N\hookrightarrow\Omega_N$ is the real-positive embedding (the canonical "no-phase" section), and $\mathcal M_{|z|}$ is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s real-positive apex generator applied to the modulus ledger $|z|\in\mathbb R_{>0}^N$. Equivalently, the diagram
$$\begin{array}{ccc}\Omega_N & \xrightarrow{\ \mathcal M_{(-)}(\beta,c)\ } & \mathbb C\\[2pt]{\scriptstyle\sigma_{\mathrm{R+}}\circ\mathcal R}\big\downarrow & & \big\Vert\\[2pt]\mathbb R_{>0}^N & \xrightarrow{\ \mathcal M_{(-)}(\beta,c)\ } & \mathbb C\end{array}$$
commutes: restricting to moduli and re-embedding as a zero-phase amplitude leaves the apex generator unchanged.

**Proof.** Modulus-restriction followed by real-positive embedding sends $z\in\Omega_N$ to $\sigma_{\mathrm{R+}}(\mathcal R(z))=|z|\in\mathbb R_{>0}^N$, viewed as a complex amplitude with zero phase. By \hyperlink{stmt:3-2}{Lemma~3.2}(c), the complex centered log-ledger of $|z|$ has $y^{(\arg|z|)}_s=0$ for every $s$, so $y_s(|z|)=y^{(|z|)}_s\in\mathbb R$. By \hyperlink{stmt:3-5}{Proposition~3.5}, $\mathcal M_{|z|}(\beta,c)=\mathcal M_x(\beta,c)$ with $x=|z|\in\mathbb R_{>0}^N$. Hence $\mathcal M_{\sigma_{\mathrm{R+}}(\mathcal R(z))}(\beta,c)=\mathcal M_{|z|}(\beta,c)$. $\square$

\hyperlink{stmt:4-2}{Theorem~4.2} is the precise sense in which **decoherence is the modulus-restriction**: the operation $\mathcal R\circ\sigma_{\mathrm{R+}}$ (restrict to moduli, then re-embed as zero-phase amplitudes) erases the phase content of $z$ and collapses the complex apex to the classical apex. Every integer-$\beta$ closure sample ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.5) and every Taylor-$\beta$ moment sample ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.3) of the complex apex is preserved under this operation — the operation kills *only* the phase deformation.

### 4.3 The phase deformation as the coherence content {#sec:4-3}

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (Quantitative decoherence gap).** For $z\in\Omega_N$, the difference between the complex apex and its decoherent restriction is
$$\mathcal M_z(\beta,c)-\mathcal M_{|z|}(\beta,c)=\frac{1}{N}\sum_{s\in\mathbb Z/N}e^{\beta y^{(|z|)}_s}\,\big(e^{i\beta y^{(\arg z)}_s}-1\big)\,\overline{\chi_c(s)},$$
where each $(e^{i\beta y^{(\arg z)}_s}-1)$ term encodes the deviation of the $s$-th coordinate's phase from the real-positive section.

In particular:

(a) *Vanishing on the real-positive sector.* If $z\in U(1)\cdot\mathbb R_{>0}^N$ (a global-phase rotation of the real-positive sector), every $y^{(\arg z)}_s=0$ (by \hyperlink{stmt:3-2}{Lemma~3.2}(c) plus global-phase invariance \hyperlink{stmt:3-2}{Lemma~3.2}(b)) and the gap vanishes.

(b) *Linear regime.* For small $|\beta y^{(\arg z)}_s|\ll 1$,
$$\mathcal M_z(\beta,c)-\mathcal M_{|z|}(\beta,c)=i\beta\cdot\frac{1}{N}\sum_s e^{\beta y^{(|z|)}_s}\,y^{(\arg z)}_s\,\overline{\chi_c(s)}+O(\beta^2|y^{(\arg z)}|^2),$$
the leading-order **coherence content** of the complex apex — a character-twisted moment of the centered argument $y^{(\arg z)}$, modulated by the classical apex weights $e^{\beta y^{(|z|)}_s}$.

**Proof.** Subtracting the modulus-restricted apex from the modulus-phase factorization of \hyperlink{stmt:3-6}{Proposition~3.6},
$$\mathcal M_z(\beta,c)-\mathcal M_{|z|}(\beta,c)=\frac{1}{N}\sum_s e^{\beta y^{(|z|)}_s}\big(e^{i\beta y^{(\arg z)}_s}-1\big)\overline{\chi_c(s)},$$
which is the stated identity. (a) Each phase factor vanishes when $y^{(\arg z)}_s=0$. (b) First-order Taylor: $e^{i\beta y^{(\arg z)}_s}-1=i\beta y^{(\arg z)}_s+O(\beta^2|y^{(\arg z)}|^2)$. $\square$

The coherence content $\mathcal M_z-\mathcal M_{|z|}$ measures the "non-classical" portion of the complex apex generator. In the quantum-information reading, it is the **interference content** of the state $|z\rangle$ relative to the computational basis $\{|s\rangle\}_{s=0}^{N-1}$: a state with zero coherence content has only diagonal (Born) statistics, while a state with non-zero coherence content has off-diagonal phase-sensitive structure that survives the apex measurement.

### 4.4 Why naive phase-averaging is the wrong decoherence operation {#sec:4-4}

It is tempting to define decoherence as uniform averaging over the phase fiber $T^{N-1}$ — the symmetry-group quotient associated to "ignoring phases." We record explicitly that this is *not* an operation that recovers the classical apex, and that the modulus-restriction of \hyperlink{stmt:4-2}{Theorem~4.2} (which does recover [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s apex on the modulus ledger) is the correct operational analog of measurement-basis decoherence.

\hypertarget{stmt:4-4}{}
**Proposition 4.4 (Phase-fiber averaging kills integer modes).** Fix a simplex point $p\in\mathring\Delta^{N-1}$ and parameterize the unit-sphere phase fiber over $p$ by $z_s=\sqrt{p_s}\,e^{i\phi_s}$ with $\phi=(\phi_1,\ldots,\phi_N)\in T^N$ modded by global phase to give $\phi\in T^{N-1}$. For every $\beta=m\in\mathbb Z\setminus\{0\}$ and every $c\in\widehat{\mathbb Z/N}$,
$$\frac{1}{(2\pi)^{N-1}}\int_{T^{N-1}}\mathcal M_z(m,c)\,d\phi=0.$$

**Proof.** By the modulus-phase factorization (\hyperlink{stmt:3-6}{Proposition~3.6}),
$$\mathcal M_z(m,c)=\frac{1}{N}\sum_se^{my^{(|z|)}_s}\,e^{imy^{(\arg z)}_s}\,\overline{\chi_c(s)},$$
where $y^{(|z|)}_s$ depends only on $p$ and is independent of $\phi$, while $y^{(\arg z)}_s=\phi_s-\frac{1}{N}\sum_j\phi_j$ depends linearly on $\phi$. Integrating term-by-term:
$$\int_{T^{N-1}}e^{imy^{(\arg z)}_s}\frac{d\phi}{(2\pi)^{N-1}}=\int_{T^{N-1}}e^{im(\phi_s-\bar\phi)}\frac{d\phi}{(2\pi)^{N-1}}.$$
Parameterize $T^{N-1}$ by $(\phi_1,\ldots,\phi_{N-1})\in T^{N-1}$ with $\phi_N=-\sum_{j<N}\phi_j$ (gauge-fixing global phase by $\sum_s\phi_s=0$, so $\bar\phi=0$). Then $e^{im(\phi_s-\bar\phi)}=e^{im\phi_s}$, and for $1\le s<N$,
$$\int_{T^{N-1}}e^{im\phi_s}\frac{d\phi}{(2\pi)^{N-1}}=\frac{1}{2\pi}\int_0^{2\pi}e^{im\phi_s}d\phi_s\cdot\prod_{j\ne s,N}\frac{1}{2\pi}\int_0^{2\pi}d\phi_j=\delta_{m,0}\cdot 1=0$$
for $m\ne 0$ (the $\phi_s$-integral is zero for any integer $m\ne 0$). For $s=N$: $\phi_N=-\sum_{j<N}\phi_j$, so $e^{im\phi_N}=\prod_{j<N}e^{-im\phi_j}$, and each $\phi_j$-integral is again zero for $m\ne 0$. Hence every summand vanishes after integration. $\square$

\hyperlink{stmt:4-4}{Proposition~4.4} has a clean operational interpretation: **uniform averaging over the relative-phase torus annihilates every integer-$\beta$ mode of $\mathcal M_z$**, including modes (like $\beta=2$, the Born/RMS rung of [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)) at which [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x$ is generically non-zero. Hence phase-fiber averaging cannot reproduce the classical apex; it produces zero (at non-zero integer $\beta$). The classical-apex content is *not* the phase-average of the complex apex — it is the phase-zero *section* of the complex apex, which is what modulus-restriction extracts.

The structural distinction:

- **Phase-fiber averaging** integrates $\mathcal M_z$ democratically over $T^{N-1}$, treating every phase configuration as equally weighted. This is a *measure-theoretic* operation on the complex amplitude space, killing all integer-Fourier-mode content of the apex.

- **Modulus-restriction** picks the unique zero-phase representative of each modulus orbit, treating the real-positive sector as a privileged *section* (not a measure-theoretic average). This is a *geometric* operation, preserving the full integer-$\beta$ content of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s apex.

These two operations are not the same and have opposite content: the first erases everything classical, the second isolates everything classical. Decoherence in the operational sense of measurement-basis modulus projection is the second, not the first.

**Open Problem 4.4 (Uniqueness of modulus-restriction as classical retract).** Characterize the family of "phase-erasing" maps $\Phi:\Omega_N\to\Omega_N$ — natural, $U(N)$-equivariant up to a chosen basis, idempotent — for which $\mathcal M_{\Phi(z)}(\beta,c)=\mathcal M_{|z|}(\beta,c)$ for all $(\beta,c)$. We expect modulus-restriction $\sigma_{\mathrm{R+}}\circ\mathcal R$ to be the unique such retract in the operationally meaningful sense (preserving moduli, killing only phases), but a precise functorial characterization is open. See \hyperref[sec:7]{§7} for the connection to the dephasing channel on density matrices.

### 4.5 Density-matrix decoherence on the pure-state stratum {#sec:4-5}

The modulus-restriction formulation of \hyperlink{stmt:4-2}{Theorem~4.2} lives at the level of pure-state amplitudes $z\in\Omega_N$. We promote it to a density-matrix statement on the **pure-state stratum** and explicitly scope the mixed-state generalization as a forward door.

The operational decoherence on density matrices is the computational-basis **dephasing channel**
$$\mathcal P:\rho\longmapsto\sum_{s=0}^{N-1}\langle s|\rho|s\rangle\,|s\rangle\langle s|,$$
which sets every off-diagonal entry $\rho_{ss'}$ ($s\ne s'$) to zero while preserving the diagonal (the Born probabilities). For a pure-state density matrix $\rho_z:=|z\rangle\langle z|/\|z\|^2$, $\mathcal P(\rho_z)=\sum_s p_s|s\rangle\langle s|=\mathrm{diag}(p)$ with $p_s=|z_s|^2/\|z\|^2$.

\hypertarget{stmt:4-5}{}
**Theorem 4.5 (Pure-state density-matrix decoherence).** Define the **pure-state apex generator** on $z\in\Omega_N\cap S^{2N-1}$ by
$$\mathcal M^{\mathrm{ps}}_{\rho_z}(\beta,c):=\mathcal M_z(\beta,c)$$
(the lift of the complex apex through the canonical map $z\mapsto\rho_z$ on the amplitude sphere, well-defined up to global phase by \hyperlink{stmt:3-2}{Lemma~3.2}(b)). Then for every $z\in\Omega_N$ and every $(\beta,c)\in\mathbb C\times\widehat{\mathbb Z/N}$,
$$\boxed{\mathcal M^{\mathrm{ps}}_{\mathcal P(\rho_z)}(\beta,c)=\mathcal M_{|z|}(\beta,c)=\mathcal M_x(\beta,c)\big|_{x=|z|}.}$$
Equivalently: applying the dephasing channel to a pure state, then evaluating the pure-state apex generator, returns the classical apex of the Born-probability ledger under the square-root section.

**Proof.** Dephasing keeps only the diagonal: $\mathcal P(\rho_z)=\mathrm{diag}(p)$ with $p_s=|z_s|^2/\|z\|^2$. A diagonal state $\mathrm{diag}(p)$ is read by the pure-state apex generator through its **canonical real-positive amplitude** $\sqrt p=(\sqrt{p_1},\ldots,\sqrt{p_N})\in S^{N-1}_+$ — the positive-square-root section of the dephasing channel — so $\mathcal M^{\mathrm{ps}}_{\mathrm{diag}(p)}(\beta,c):=\mathcal M_{\sqrt p}(\beta,c)$. Now $\sqrt p=|z|/\|z\|$ lies on the same positive ray as the modulus ledger $|z|$, so by positive-scaling invariance (\hyperlink{stmt:3-2}{Lemma~3.2}(a)) the two have the same centered log-ledger and hence the same apex generator; and by the real-positive reduction (\hyperlink{stmt:3-5}{Proposition~3.5}), $\mathcal M_{|z|}(\beta,c)=\mathcal M_x(\beta,c)$ with $x=|z|$. Combining,
$$\mathcal M^{\mathrm{ps}}_{\mathcal P(\rho_z)}(\beta,c)=\mathcal M_{\sqrt p}(\beta,c)=\mathcal M_{|z|}(\beta,c)=\mathcal M_x(\beta,c)\big|_{x=|z|}.\qquad\square$$

\hyperlink{stmt:4-5}{Theorem~4.5} is the rank-1 specialization (in the input) of the **mixed-state density-matrix decoherence theorem** scoped below. The pure-state lift $z\mapsto\rho_z$, dephasing $\mathcal P$, and positive-square-root section of the diagonal stratum are precisely the rank-1 inputs to that theorem; \hyperlink{stmt:4-5}{Theorem~4.5} therefore closes the abstract claim that *the real-positive sector is the decoherent face of the complex amplitude space* on the pure-state level, with the mixed-state generalization remaining a forward door (\hyperref[sec:7-2]{§7.2}).

**Forward door (mixed-state generalization).** A full **density-matrix apex generator** $\mathcal M_\rho(\beta,c)$ generalizing $\mathcal M_z$ to mixed states would naturally be defined via the centered modular Hamiltonian
$$L_\rho:=\log\rho-\tfrac{1}{N}\mathrm{tr}(\log\rho)\,I_N,\qquad\mathcal M_\rho(\beta,c):=\tfrac{1}{N}\mathrm{tr}\big(e^{\beta L_\rho}C_c^\ast\big),\qquad C_c:=\sum_s\chi_c(s)|s\rangle\langle s|,$$
with the matrix-logarithm requiring $\rho$ to be full-rank (an obstruction at the pure-state boundary, requiring regularization $\rho\to\rho_\epsilon:=(1-\epsilon)\rho+\epsilon I_N/N$ and a limit $\epsilon\to 0$). For diagonal $\rho=\mathrm{diag}(p)$, this reduces (after the half-factor reparameterization $\beta_\rho=\beta/2$ reflecting the amplitude-vs-probability convention noted in the Notation dictionary) to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s $\mathcal M_x(\beta_\rho,c)$ with $x=\sqrt p$. The full mixed-state **density-matrix decoherence theorem** would state: $\mathcal M_{\mathcal P(\rho)}(\beta,c)$ equals the modulus-restricted classical apex applied to the Born-probability ledger. For *non-diagonal* $\rho$, however, $\log\rho$ and the character operators $C_c$ do not commute, so the $\beta$-Taylor coefficients of $\mathcal M_\rho$ are non-commutative moments requiring a choice of operator ordering — and that choice is exactly a choice of quantum monotone (Markov-invariant) metric. Unlike the classical case, Chentsov uniqueness fails and an entire family appears (Morozova–Chentsov 1990; Petz 1996); the dually-flat / convex-potential structure of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4 survives quantization for a *unique* member — the **Kubo–Mori** metric (Grasselli–Streater 2001), not Bures. We develop this fork in \hyperref[sec:7-2]{§7.2}.

Forward direction (planned): **The Monotone-Metric Apex — the Petz Fork and the Kubo–Mori Selection.**

---

## 5. The Kummer-cover theorem at integer $\beta$ {#sec:5}

This section makes the cover-structure preview of \hyperlink{stmt:3-8}{Proposition~3.8} into a literal Galois statement at integer $\beta=m\ge 1$. The closure diagonal $\mathcal M_z(m,c)$ at integer $m$ is shown to be a section of a line bundle on the projective space $\mathbb{CP}^{N-1}$, associated to a specific character of the **Kummer cover deck group** $\mu_N$; we identify this line bundle explicitly as a power of the tautological bundle $\mathcal O(-1)$ on $\mathbb{CP}^{N-1}$. On the real-positive sector the line bundle trivializes (recovering [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 3.7); on the complex sector the deck group acts genuinely. This is the literal complex-side enrichment of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4.

### 5.1 The Kummer cover $\widetilde{\mathbb{CP}^{N-1}}\to\mathbb{CP}^{N-1}$ {#sec:5-1}

Recall from [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.5 that the closure diagonal at integer $m\ge 1$ takes the form
$$\mathcal M_z(m,c)=G(z)^{-m}\widehat{z^m}_c,\qquad G(z):=\Big(\prod_{j=1}^N z_j\Big)^{1/N},$$
where $\widehat{z^m}_c=\frac{1}{N}\sum_s z_s^m\overline{\chi_c(s)}$ is the $c$-th Fourier coefficient of the componentwise $m$-th power, and $G(z)$ is the **complex geometric mean**, defined as an $N$-th root of the product $\prod_j z_j$. The product $\prod_j z_j$ is a single-valued holomorphic function on $\mathbb C^N$; the $N$-th root requires a branch choice and is multi-valued by $\mu_N$.

\hypertarget{stmt:5-1}{}
**Definition 5.1 (Kummer cover).** The **Kummer cover** of $\Omega_N\cap\mathbb{CP}^{N-1}$ at level $N$ is the locus
$$\widetilde\Omega_N:=\big\{(z,\omega)\in\Omega_N\times\mathbb C^\times:\omega^N=\prod_{j=1}^N z_j\big\}\Big/\,\mathbb C^\times,$$
where $\mathbb C^\times$ acts diagonally $(z,\omega)\mapsto(\lambda z,\lambda\omega)$. The projection $(z,\omega)\mapsto[z]$ realizes $\widetilde\Omega_N\to\Omega_N\cap\mathbb{CP}^{N-1}$ as an unramified Galois cover of degree $N$ with deck group
$$\mathrm{Gal}(\widetilde\Omega_N\to\Omega_N\cap\mathbb{CP}^{N-1})=\mu_N,$$
acting by $(z,\omega)\mapsto(z,\zeta\omega)$ for $\zeta\in\mu_N$.

On $\widetilde\Omega_N$, the geometric mean $G(z)=\omega$ is a **single-valued holomorphic function**; in particular $G(z)^{-m}=\omega^{-m}$ is single-valued on the cover.

\hypertarget{stmt:5-2}{}
**Remark 5.2 (Cover degree refinement).** For the closure diagonal $\mathcal M_z(m,c)$ specifically, only the $m$-th power $G(z)^{-m}=\omega^{-m}$ is needed. This is single-valued on the smaller cover $\widetilde\Omega_N^{(m)}\to\Omega_N\cap\mathbb{CP}^{N-1}$ of degree $N/\gcd(N,m)$, with deck group $\mu_{N/\gcd(N,m)}$ — the quotient of $\mu_N$ by the kernel $\mu_{\gcd(N,m)}$ of $\zeta\mapsto\zeta^m$. We work with the universal cover $\widetilde\Omega_N$ at degree $N$ throughout to keep the statements uniform across $m$.

### 5.2 The Kummer-cover theorem {#sec:5-2}

\hypertarget{stmt:5-3}{}
**Theorem 5.3 (Kummer cover at integer $\beta$).** Fix an integer $m\ge 1$ and a character index $c\in\widehat{\mathbb Z/N}$. The complex apex generator $\mathcal M_z(m,c)=\omega^{-m}\widehat{z^m}_c$ lifts to a holomorphic function on the Kummer cover $\widetilde\Omega_N$, and under the deck-group action $(z,\omega)\mapsto(z,\zeta\omega)$ for $\zeta\in\mu_N$, it transforms by the character
$$\boxed{\mathcal M_z(m,c)\longmapsto\rho_m(\zeta)\cdot\mathcal M_z(m,c),\qquad\rho_m(\zeta):=\zeta^{-m}.}$$

In particular:

(a) *(Single-valuedness criterion.)* $\mathcal M_z(m,c)$ descends to a single-valued function on $\mathbb{CP}^{N-1}$ if and only if $\rho_m$ is the trivial character of $\mu_N$, i.e., $N\mid m$.

(b) *(Line-bundle identification.)* For general integer $m$, $\mathcal M_z(m,c)$ is a holomorphic section of the line bundle $\mathcal L_m$ on $\Omega_N\cap\mathbb{CP}^{N-1}$ whose total space is
$$\mathcal L_m:=\widetilde\Omega_N\times_{\mu_N}\mathbb C_{\rho_m},$$
where $\mu_N$ acts on the product by $\zeta\cdot(p,v)=(\zeta\cdot p,\rho_m(\zeta)^{-1}v)=(\zeta\cdot p,\zeta^m v)$. Concretely, since $\prod_jz_j$ is a section of $\mathcal O(N)$ and its $N$-th root $\omega$ behaves as a section of $\mathcal O(1)$, the factor $\omega^{-m}$ is a section of $\mathcal O(1)^{\otimes(-m)}=\mathcal O(-m)$; equivalently
$$\mathcal L_m\;\cong\;\mathcal O(N)^{\otimes(-m/N)}\quad\text{as a }\mathbb Q\text{-(root-stack) line bundle,}\qquad c_1(\mathcal L_m)=-m\,H\ \ (\text{integral}),$$
where $H$ is the hyperplane class. The $-m/N$ is the exponent on $\mathcal O(N)$, *not* a fractional multiple of $H$: the Chern class is the integer $-mH$ for every $m$. The obstruction to $\mathcal L_m$ descending to an honest line bundle on $\mathbb{CP}^{N-1}$ when $N\nmid m$ is the **flat monodromy character** $\rho_m$ of the cyclic cover — a torsion/flat datum invisible to $c_1$ — and descent succeeds iff $\rho_m$ is trivial iff $N\mid m$, in which case $\mathcal L_m\cong\mathcal O(-m)$.

(c) *(Character independence in $c$.)* The deck-group action multiplies $\mathcal M_z(m,c)$ by the same scalar $\rho_m(\zeta)$ for every character index $c$; the family $\{\mathcal M_z(m,c):c\in\widehat{\mathbb Z/N}\}$ transforms uniformly under the deck group, hence lies in a single $\mathcal L_m$-isotypic component of holomorphic functions on $\widetilde\Omega_N$.

**Proof.** On $\widetilde\Omega_N$, $G(z)=\omega$ is single-valued. Hence $\mathcal M_z(m,c)=\omega^{-m}\widehat{z^m}_c$ is single-valued on $\widetilde\Omega_N$ as a product of two single-valued factors ($\omega^{-m}$ on the cover, $\widehat{z^m}_c$ pulled back from $\mathbb{CP}^{N-1}$).

Under deck action $\zeta\in\mu_N$: $\omega\mapsto\zeta\omega$, so $\omega^{-m}\mapsto\zeta^{-m}\omega^{-m}=\rho_m(\zeta)\omega^{-m}$. The Fourier coefficient $\widehat{z^m}_c$ depends only on $z$ (not on $\omega$), so is invariant. Combining,
$$\mathcal M_z(m,c)=\omega^{-m}\widehat{z^m}_c\longmapsto\rho_m(\zeta)\,\omega^{-m}\widehat{z^m}_c=\rho_m(\zeta)\mathcal M_z(m,c),$$
proving the boxed transformation law.

(a) $\rho_m$ trivial iff $\zeta^{-m}=1$ for every $\zeta\in\mu_N$ iff $N\mid m$. (b) The associated-bundle construction $\mathcal L_m=\widetilde\Omega_N\times_{\mu_N}\mathbb C_{\rho_m}$ is the standard descent of a $\mu_N$-equivariant trivial bundle on the cover to a line bundle on the base; a function $f$ on $\widetilde\Omega_N$ transforming under deck action by $f\mapsto\rho_m(\zeta)f$ is by definition a section of $\mathcal L_m$. For the Chern class: $\prod_jz_j$ is a homogeneous form of degree $N$, hence a section of $\mathcal O(N)$ with divisor $\sum_jH_j$ of class $NH$. Its $N$-th root $\omega$ is therefore a section of $\mathcal O(N)^{1/N}=\mathcal O(1)$ (single-valued on the cover), and $\omega^{-m}$ is a section of $\mathcal O(-m)$ with $c_1=-mH$. This integer is the Chern class of $\mathcal L_m$ for every $m$; the $-m/N$ that appears is the exponent realizing $\mathcal L_m\cong\mathcal O(N)^{\otimes(-m/N)}$ as a $\mathbb Q$-line bundle, *not* a fractional Chern class. When $N\nmid m$, $\mathcal L_m$ fails to descend to $\mathbb{CP}^{N-1}$ because the flat monodromy character $\rho_m$ is non-trivial — a flat obstruction invisible to $c_1$ — and it becomes the honest line bundle $\mathcal O(-m)$ exactly when $N\mid m$. (c) is immediate from the proof since $\rho_m(\zeta)$ is independent of $c$. $\square$

\hypertarget{stmt:5-4}{}
**Corollary 5.4 (Eigenspace decomposition).** The space of holomorphic functions on $\widetilde\Omega_N$ decomposes by deck-group character as a direct sum of $\rho$-eigenspaces over $\rho\in\widehat{\mu_N}=\mathbb Z/N$. The integer-$\beta$ apex generators $\mathcal M_z(m,c)$ for $m\in\mathbb Z_{\ge 0}$ and $c\in\widehat{\mathbb Z/N}$ populate this decomposition by the rule $m\mapsto\rho_m=\chi_{-m\bmod N}$, i.e., the **integer exponent $m$ modulo $N$** is the deck-group character index of the closure-diagonal apex.

### 5.3 The deck-group character vs. the label-character index $c$ {#sec:5-3}

A subtlety worth emphasizing: [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s analysis identifies *two* distinct characters of $\mathbb Z/N$, both formally elements of $\widehat{\mathbb Z/N}$, playing different structural roles in the closure diagonal $\mathcal M_z(m,c)$:

1. **Deck-group character** $\rho_m=\chi_{-m\bmod N}\in\widehat{\mu_N}$. Indexes the eigenspace of the Kummer-cover deck-group action; depends on the integer exponent $m$ but is *uniform* across all $c$. This is the "global twist" of the apex generator under the cover.

2. **Label-character index** $c\in\widehat{\mathbb Z/N}$. Indexes the eigenspace of the *label* group $\mathbb Z/N$ action on the simplex coordinates (the categorical structure); via [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.5, $\mathcal M_z(m,c)$ records the multi-index convolutional sum over $\{(a_1,\ldots,a_m):a_1+\cdots+a_m\equiv c\pmod N\}$. This is the "selection rule" of the apex generator.

The two characters live in formally-identical groups $\widehat{\mathbb Z/N}\cong\widehat{\mu_N}\cong\mathbb Z/N$ but act on different objects:

- $\rho_m$ acts on the $\omega$-coordinate of the cover (the geometric-mean branch).
- $\chi_c$ acts on the $s$-coordinate of the labels (the categorical structure of $\mathbb Z/N$).

The cover-character $\rho_m$ is determined by the *exponent* $m$; the label-character $\chi_c$ is determined by the *conductor* $c$ in the moment/closure tower. The fact that both are characters of the same abstract group is a structural coincidence of the categorical-$\mathbb Z/N$ setting; in more general label groups, the two characters would live in different dual groups.

\hypertarget{stmt:5-5}{}
**Theorem 5.5 ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.5 unaffected by Kummer cover).** The selection rule $a_1+\cdots+a_m\equiv c\pmod N$ for the convolutional Fourier expansion of $\widehat{z^m}_c$ is *invariant* under the Kummer-cover deck-group action of $\mu_N$. In particular, the deck-group action does not mix character-index $c$ components of $\mathcal M_z(m,c)$: it acts by scalar multiplication within each $c$-component independently.

**Proof.** $\widehat{z^m}_c$ is a polynomial in $z=(z_1,\ldots,z_N)$ (the $m$-th power of $z_s$, summed against $\overline{\chi_c(s)}$); the deck-group action $\omega\mapsto\zeta\omega$ does not change $z$, so $\widehat{z^m}_c$ is fixed termwise under the action. The selection-rule expansion ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.5 proof) is therefore unaffected. $\square$

### 5.4 Real-positive trivialization and reconciliation with [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 3.7 {#sec:5-4}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 3.7 established that on the real-positive sector $\mathbb R_{>0}^N$ the $n$-th-power closure $\pi_n$ is a real-analytic homeomorphism, with the Kummer-cover deck group trivializing because $\mu_n\cap\mathbb R_{>0}=\{1\}$.

The [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) framework recovers this trivialization as a special case of \hyperlink{stmt:5-3}{Theorem~5.3}:

\hypertarget{stmt:5-6}{}
**Proposition 5.6 (Real-positive trivialization).** The Kummer cover $\widetilde\Omega_N\to\Omega_N\cap\mathbb{CP}^{N-1}$ admits a canonical section over the real-positive sector $\mathbb R_{>0}^N\cap\mathbb{CP}^{N-1}$, given by $z\mapsto(z,G_{\mathbb R_{>0}}(z))$ where $G_{\mathbb R_{>0}}(z)=\big(\prod_jz_j\big)^{1/N}>0$ is the unique positive real $N$-th root. Restricted to this section, the Kummer-cover line bundle $\mathcal L_m$ of \hyperlink{stmt:5-3}{Theorem~5.3}(b) is canonically trivial, and the deck-group action on $\mathcal M_z(m,c)\big|_{\mathbb R_{>0}^N}$ reduces to the identity.

**Proof.** On $\mathbb R_{>0}^N$, $\prod_j z_j>0$ and the function $w\mapsto w^{1/N}$ is the unique positive real $N$-th root: a single-valued, real-analytic, positive-real-valued branch. This selects a section of $\widetilde\Omega_N\to\Omega_N\cap\mathbb{CP}^{N-1}$ over $\mathbb R_{>0}^N$. The line bundle of \hyperlink{stmt:5-3}{Theorem~5.3}(b) pulled back along this section is trivial because the deck-group orbit through any point in the section consists of $N$ distinct points $(z,\zeta\omega)$ for $\zeta\in\mu_N$, of which only $\zeta=1$ stays in the real-positive section; hence the section selects one branch of the cover canonically, with trivial deck-group action on the apex. $\square$

\hyperlink{stmt:5-6}{Proposition~5.6} makes precise the slogan of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 3.7: **on the real-positive sector the Kummer cover is a trivial bundle (canonically split by the positive real $N$-th-root section), while on the complex sector $\Omega_N\setminus(U(1)\cdot\mathbb R_{>0}^N)$ the cover acquires genuine $\mu_N$-deck-group action via \hyperlink{stmt:5-3}{Theorem~5.3}.**

### 5.5 The complex enrichment: [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4 made literal {#sec:5-5}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4 phrased the Kummer-cover content of the apex generator as an **organizing structure**, with the technical statement (Proposition 3.7) proving only the real-sector trivialization. The non-trivial Galois-action statement was scoped as a forward door to [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442). The forward door is now closed:

> **\hyperlink{stmt:5-3}{Theorem~5.3} elevates [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4's "Kummer-cover organizing principle" from a real-sector trivialization plus complex-sector conjecture to a complete description: the closure diagonal $\mathcal M_z(m,c)$ is a section of the line bundle $\mathcal L_m\cong\mathcal O(N)^{\otimes(-m/N)}$ (integral Chern class $c_1=-mH$) on $\mathbb{CP}^{N-1}$, pulled back from the universal degree-$N$ Kummer cover $\widetilde{\mathbb{CP}^{N-1}}\to\mathbb{CP}^{N-1}$ on which the geometric mean $G(z)$ is single-valued. The deck group $\mu_N$ acts by the character $\rho_m(\zeta)=\zeta^{-m}$; the obstruction to descent is the flat character $\rho_m$ (invisible to $c_1$), trivial iff $N\mid m$ (in which case $\mathcal L_m\cong\mathcal O(-m)$ and $\mathcal M_z(m,c)$ descends to $\mathbb{CP}^{N-1}$ unambiguously).**

The "Galois-dual operations" forward door of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §3.4 — pairing the moment diagonal $\partial_\beta^n\mathcal M(0,c)$ with the closure diagonal $\mathcal M(m,c)$ via the Kummer cover — now has its closure-side fully described. The moment-diagonal side is more delicate (the Taylor expansion at $\beta=0$ involves the complex log $\log z_s$ at all orders, not just integer powers) and remains a forward door for non-integer $\beta$; we record this in \hyperref[sec:7]{§7}.

**Worked example: $N=2$ (qubit, preview of \hyperref[sec:6]{§6}).** For $N=2$, the Kummer cover $\widetilde\Omega_2\to\Omega_2\cap\mathbb{CP}^1$ has degree $2$, deck group $\mu_2=\{\pm 1\}$. The closure diagonal at integer $m$:
- $m$ even: $\rho_m=\chi_{-m\bmod 2}=\chi_0$ (trivial), so $\mathcal M_z(m,c)$ is single-valued on $\mathbb{CP}^1$.
- $m$ odd: $\rho_m=\chi_{-1\bmod 2}=\chi_1$ (the sign character), so $\mathcal M_z(m,c)$ is double-valued on $\mathbb{CP}^1$, single-valued on the double cover.

The qubit case at $m=2$ (Born / RMS rung): single-valued on $\mathbb{CP}^1$ (the Bloch sphere), consistent with the central role of Born probabilities at this rung in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) and [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428). The qubit case at $m=1$ (linear): double-valued on the Bloch sphere — the standard observation that quantum amplitudes carry a $\pm$ sign ambiguity beyond probabilities. *We note that this double-valuedness is the Kummer-cover obstruction in $\sqrt{z_0z_1}$, whose numerical doubling coincides with — but is logically independent of — the $SU(2)\to SO(3)$ double cover discussed in \hyperref[sec:2-2]{§2.2}: at $N=2$ both produce a $\mathbb Z/2$ obstruction in the amplitude $\to$ probability descent, but the Kummer cover persists for all $N$ while the $SU(2)\to SO(3)$ identification does not.* The full Bloch-sphere computation is the subject of \hyperref[sec:6]{§6}.

### 5.6 Carlson rigidity: the closure diagonal determines the moment diagonal {#sec:5-6}

The two sampling diagonals of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — the moment diagonal (Taylor jets at $\beta=0$) and the closure diagonal (integer samples $\beta=m$) — were presented there as paired-but-distinct regimes that *happen* to share the modular selection rule $a_1+\cdots+a_n\equiv c\pmod N$. On the decoherent face the sharing is not a coincidence: it is forced by a classical uniqueness theorem for entire functions of exponential type, and its breakdown is exactly the Kummer regime of this section.

\hypertarget{stmt:5-7}{}
**Proposition 5.7 (Carlson rigidity and its phase threshold).** Fix $c\in\widehat{\mathbb Z/N}$.

(a) *(Decoherent face.)* For $x\in\mathbb R_{>0}^N$, the entire function $\beta\mapsto\mathcal M_x(\beta,c)$ satisfies $|\mathcal M_x(it,c)|\le 1$ for every real $t$, hence has exponential type $0$ on the imaginary axis. By **Carlson's theorem** (Carlson 1914; Boas 1954, Thm 9.2.1), it is the *unique* entire function of imaginary-axis type $<\pi$ taking the prescribed values $\{\mathcal M_x(m,c)\}_{m\ge 0}$ on the non-negative integers. Hence the **closure diagonal $\{\mathcal M_x(m,c)\}_{m\ge 0}$ determines $\mathcal M_x(\cdot,c)$ entirely**, and therefore — via the Taylor expansion at $\beta=0$ — the full moment diagonal $\{\partial_\beta^n\mathcal M_x(0,c)\}_{n\ge 0}$.

(b) *(General branch.)* For $z\in\Omega_N$ on a fixed branch, write the centered-argument indicators $\tau_+:=\max_s\big(-y^{(\arg z)}_s\big)$ and $\tau_-:=\max_s\big(y^{(\arg z)}_s\big)$. Then $\beta\mapsto\mathcal M_z(\beta,c)$ has imaginary-axis exponential indicators $(\tau_+,\tau_-)$, and Carlson uniqueness holds iff
$$\tau_++\tau_-=\max_s y^{(\arg z)}_s-\min_s y^{(\arg z)}_s<2\pi,$$
i.e., iff the **centered-argument range is sub-critical**. On the principal branch ($\arg z_s\in(-\pi,\pi]$) this range is always $<2\pi$, so closure-diagonal rigidity holds *sheet by sheet*.

**Proof.** (a) For real $x$, every $y_s\in\mathbb R$, so $|\mathcal M_x(it,c)|=\big|\tfrac1N\sum_s e^{ity_s}\overline{\chi_c(s)}\big|\le\tfrac1N\sum_s 1=1$; the imaginary-axis indicator is $0<\pi$. Carlson's theorem then gives uniqueness from the non-negative-integer samples; the Taylor coefficients at $\beta=0$ are recovered from the entire function, yielding the moment diagonal. (b) For $z$ on a fixed branch, $y_s=y^{(|z|)}_s+iy^{(\arg z)}_s$, so on $\beta=it$, $|e^{ity_s}|=e^{-ty^{(\arg z)}_s}$; the growth rate as $t\to+\infty$ is $\max_s(-y^{(\arg z)}_s)=\tau_+$ and as $t\to-\infty$ is $\max_s(y^{(\arg z)}_s)=\tau_-$. Carlson's condition $\tau_++\tau_-<2\pi$ is the stated range bound, and $\arg z_s\in(-\pi,\pi]$ forces range $<2\pi$ on the principal branch. $\square$

\hypertarget{stmt:5-8}{}
**Remark 5.8 (Carlson rigidity and the Kummer cover are the same threshold).** Proposition 5.7 explains, on the decoherent face, *why* the two diagonals share the selection rule of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorems 3.3 and 3.5: they are not independent samples but two reads of a single function that its integer samples already over-determine. The rigidity is **per sheet**. Branch shifts $\log z_s\mapsto\log z_s+2\pi i k_s$ (\hyperlink{stmt:3-8}{Proposition~3.8}) translate $y^{(\arg z)}_s$ by $2\pi(k_s-\bar k)$, pushing the centered-argument range across the $2\pi$ threshold and breaking *cross-sheet* determination; the cross-sheet ambiguity is exactly the $\mu_N$ deck-group action of \hyperlink{stmt:5-3}{Theorem~5.3}. Thus **Carlson rigidity (within a sheet) and the Kummer cover (between sheets) are two faces of the same $2\pi$-threshold**: the closure diagonal determines the generator on each Kummer sheet, and the deck group $\mu_N$ is precisely the obstruction to gluing those determinations into a single-valued function on $\mathbb{CP}^{N-1}$ when $N\nmid m$. The Wick-rotation reading — replicator gradient flow on real $\beta$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4) versus the Lee–Yang lattice on imaginary $\beta$ (\hyperlink{stmt:6-2}{Proposition~6.2}) — places both diagonals on one holomorphic plane (\hyperref[sec:7-4]{§7.4}); Carlson rigidity is the statement that the real-integer samples already fix the whole plane, branch by branch.

---

## 6. The qubit anchor: $N=2$ in full {#sec:6}

We compute the complex apex generator $\mathcal M_z(\beta,c)$ in full at $N=2$ — the smallest non-trivial dimension, the standard qubit of quantum information. The Bloch sphere $\mathbb{CP}^1\cong S^2$ provides explicit coordinates; the decoherent equator (real-positive sector) recovers [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s qubit apex; the off-equatorial complex sector exhibits the phase deformation of \hyperlink{stmt:4-3}{Proposition~4.3} in closed form; the Kummer cover of \hyperref[sec:5]{§5} acts as the $\mu_2=\{\pm 1\}$ deck group, splitting the integer-$\beta$ rungs into single-valued ($m$ even) and double-valued ($m$ odd) families; and [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5's Lee–Yang lattice lifts to a **phase-twisted lattice** that rotates and scales as one moves off the decoherent equator.

### 6.1 The Bloch sphere parameterization {#sec:6-1}

A normalized qubit amplitude $z\in S^3\subset\mathbb C^2$, modulo global phase, has the standard Bloch parameterization
$$z=\begin{pmatrix}\cos(\theta/2)\\ e^{i\phi}\sin(\theta/2)\end{pmatrix},\qquad\theta\in[0,\pi],\;\phi\in[0,2\pi),$$
covering $\mathbb{CP}^1\cong S^2$ as $(\theta,\phi)$ range over standard spherical coordinates. The corresponding **Bloch vector** in $\mathbb R^3$ is
$$\vec r(\theta,\phi)=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),$$
with the north pole $\theta=0$ corresponding to $|0\rangle$, the south pole $\theta=\pi$ to $|1\rangle$, and the equator $\theta=\pi/2$ to equal-modulus superpositions of $|0\rangle$ and $|1\rangle$ with phase $\phi$. The Born probabilities are
$$p_0=\cos^2(\theta/2)=\tfrac{1+\cos\theta}{2},\qquad p_1=\sin^2(\theta/2)=\tfrac{1-\cos\theta}{2}.$$

The **decoherent equator** is the meridian $\phi=0$, the real-positive sector $\mathbb R_{>0}^2\cap S^3$ of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428). Points off this meridian carry non-trivial phase and exhibit the complex apex structure of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442).

### 6.2 The complex apex on the qubit in closed form {#sec:6-2}

For $N=2$, the centered log-ledger is one-dimensional: $y_0=-y_1=\frac{1}{2}\log(z_0/z_1)$. Setting $\eta:=y_0$, \hyperlink{stmt:3-3}{Definition~3.3} gives
$$\mathcal M_z(\beta,0)=\tfrac{1}{2}(e^{\beta\eta}+e^{-\beta\eta})=\cosh(\beta\eta),\qquad\mathcal M_z(\beta,1)=\tfrac{1}{2}(e^{\beta\eta}-e^{-\beta\eta})=\sinh(\beta\eta),$$
using the two characters $\chi_0\equiv 1$ and $\chi_1(s)=(-1)^s$ on $\mathbb Z/2$.

\hypertarget{stmt:6-1}{}
**Proposition 6.1 (Qubit apex in Bloch coordinates).** In the Bloch parameterization,
$$\eta(\theta,\phi)=\tfrac{1}{2}\log\cot(\theta/2)-\tfrac{i\phi}{2}=y^{(|z|)}_0(\theta)+iy^{(\arg z)}_0(\phi),$$
where $y^{(|z|)}_0(\theta)=\frac{1}{2}\ln\cot(\theta/2)$ is the real modulus log-ledger and $y^{(\arg z)}_0(\phi)=-\phi/2$ is the centered argument. The complex apex on the qubit is therefore
$$\boxed{\mathcal M_z(\beta,0)=\cosh\!\big(\tfrac{\beta}{2}\ln\cot(\theta/2)-\tfrac{i\beta\phi}{2}\big),\qquad\mathcal M_z(\beta,1)=\sinh\!\big(\tfrac{\beta}{2}\ln\cot(\theta/2)-\tfrac{i\beta\phi}{2}\big).}$$

**Proof.** With $z_0=\cos(\theta/2)$, $z_1=e^{i\phi}\sin(\theta/2)$,
$$\frac{z_0}{z_1}=\cot(\theta/2)\,e^{-i\phi}\quad\Longrightarrow\quad\log\!\Big(\frac{z_0}{z_1}\Big)=\ln\cot(\theta/2)-i\phi,$$
so $\eta=\frac{1}{2}\log(z_0/z_1)=\frac{1}{2}\ln\cot(\theta/2)-\frac{i\phi}{2}$, matching the modulus-phase decomposition of \hyperlink{stmt:3-2}{Lemma~3.2}(c) at $N=2$. Substituting into the $\cosh/\sinh$ forms above yields the boxed expressions. $\square$

### 6.3 The decoherent equator and reduction to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) {#sec:6-3}

**On the equator $\phi=0$:** $\eta=\frac{1}{2}\ln\cot(\theta/2)\in\mathbb R$, and the apex specializes to
$$\mathcal M_z(\beta,0)\big|_{\phi=0}=\cosh\!\big(\tfrac{\beta}{2}\ln\cot(\theta/2)\big)=\tfrac{1}{2}\big(\cot(\theta/2)^{\beta/2}+\tan(\theta/2)^{\beta/2}\big),$$
$$\mathcal M_z(\beta,1)\big|_{\phi=0}=\sinh\!\big(\tfrac{\beta}{2}\ln\cot(\theta/2)\big)=\tfrac{1}{2}\big(\cot(\theta/2)^{\beta/2}-\tan(\theta/2)^{\beta/2}\big).$$

Comparing with [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) applied to the modulus ledger $|z|=(\cos(\theta/2),\sin(\theta/2))$: the [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) centered log-ledger is $y_0^{(\text{\heb{ל}0})}=\frac{1}{2}\ln\cot(\theta/2)=\eta\big|_{\phi=0}$, so $\mathcal M_x(\beta,c)$ from [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Definition 3.1 agrees with $\mathcal M_z(\beta,c)\big|_{\phi=0}$ — the decoherence theorem (\hyperlink{stmt:4-2}{Theorem~4.2}) at $N=2$.

**Born / RMS rung at $\beta=2$.** Specializing to $\beta=2$ on the equator,
$$\mathcal M_z(2,0)\big|_{\phi=0}=\tfrac{1}{2}\big(\cot(\theta/2)+\tan(\theta/2)\big)=\frac{1}{\sin\theta},$$
$$\mathcal M_z(2,1)\big|_{\phi=0}=\tfrac{1}{2}\big(\cot(\theta/2)-\tan(\theta/2)\big)=\frac{\cos\theta}{\sin\theta}=\cot\theta,$$
recovering [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s Born-closure structure at the qubit: in terms of Born probabilities $p_0=\cos^2(\theta/2)$, $p_1=\sin^2(\theta/2)$, $\sin\theta=2\sqrt{p_0 p_1}$ and $\cos\theta=p_0-p_1$, so $\mathcal M_z(2,0)|_{\phi=0}=1/(2\sqrt{p_0 p_1})$ and $\mathcal M_z(2,1)|_{\phi=0}=(p_0-p_1)/(2\sqrt{p_0 p_1})$. The non-trivial mode $c=1$ measures the **probability gap** $p_0-p_1$ relative to the Born normalization, the qubit signature of conductor-$2$ structure on $\mathbb Z/2$.

### 6.4 The Kummer cover at $N=2$: $m$-parity selection {#sec:6-4}

For $N=2$ the Kummer cover (\hyperref[sec:5]{§5}) has deck group $\mu_2=\{\pm 1\}$, and \hyperlink{stmt:5-3}{Theorem~5.3} says $\mathcal M_z(m,c)\mapsto\rho_m(\zeta)\mathcal M_z(m,c)$ with $\rho_m(\zeta)=\zeta^{-m}$.

**At $\zeta=-1$:** $\rho_m(-1)=(-1)^{-m}=(-1)^m$. So the deck-group action multiplies $\mathcal M_z(m,c)$ by $(-1)^m$:

- **$m$ even** ($m=0,2,4,\ldots$): $\rho_m$ trivial, $\mathcal M_z(m,c)$ single-valued on $\mathbb{CP}^1$.
- **$m$ odd** ($m=1,3,5,\ldots$): $\rho_m$ the sign character, $\mathcal M_z(m,c)$ double-valued on $\mathbb{CP}^1$, single-valued on the double cover.

**Worked example: $m=1$ vs $m=2$.** Direct from the boxed forms of Proposition 6.1:

| $m$ | $\mathcal M_z(m,0)$ | $\mathcal M_z(m,1)$ | Branch behavior under $\phi\mapsto\phi+2\pi$ |
|---|---|---|---|
| $1$ | $\cosh\!\big(\frac{1}{2}\ln\cot(\theta/2)-\frac{i\phi}{2}\big)$ | $\sinh\!\big(\frac{1}{2}\ln\cot(\theta/2)-\frac{i\phi}{2}\big)$ | $\to-\mathcal M_z(1,c)$ (double-valued) |
| $2$ | $\cosh\!\big(\ln\cot(\theta/2)-i\phi\big)$ | $\sinh\!\big(\ln\cot(\theta/2)-i\phi\big)$ | $\to+\mathcal M_z(2,c)$ (single-valued) |

The $m=1$ entries acquire $\cosh(\ldots-i\pi)=-\cosh(\ldots)$ under $\phi\mapsto\phi+2\pi$ (since $\cosh(z+i\pi)=-\cosh(z)$ and similarly for $\sinh$); the $m=2$ entries are invariant since $\cosh(\ldots-2i\pi)=\cosh(\ldots)$. This is the **$\pm 1$ amplitude sign ambiguity** of standard quantum mechanics: at the linear ($m=1$) rung, the apex is sensitive to the global $\pm$ choice of amplitude — a $\mathbb Z/2$ obstruction in the descent from amplitude to probability that coincides numerically with the $SU(2)\to SO(3)$ double cover at $N=2$ (\hyperref[sec:2-2]{§2.2}) but is structurally the Kummer-cover obstruction of \hyperlink{stmt:5-3}{Theorem~5.3} (the Kummer obstruction persists for all $N$; the $SU(2)\to SO(3)$ identification is a low-dimensional coincidence). At the Born ($m=2$) rung, the apex sees only probability-level data and the obstruction disappears.

**Polynomial-rational closed forms.** Direct from the definition $\mathcal M_z(m,c)=G(z)^{-m}\widehat{z^m}_c$:
$$\mathcal M_z(1,0)=\frac{z_0+z_1}{2\sqrt{z_0z_1}},\qquad\mathcal M_z(1,1)=\frac{z_0-z_1}{2\sqrt{z_0z_1}},$$
$$\mathcal M_z(2,0)=\frac{z_0^2+z_1^2}{2z_0z_1},\qquad\mathcal M_z(2,1)=\frac{z_0^2-z_1^2}{2z_0z_1}.$$
The $\sqrt{z_0z_1}$ in the $m=1$ denominator is the source of the $\mu_2$ branch ambiguity; at $m=2$ the square root squares away, and the apex is a **rational function** of $z$, defining a holomorphic function on the open Bloch sphere $\mathbb{CP}^1\setminus\{|0\rangle,|1\rangle\}$ (the poles at the basis states correspond to one Born probability vanishing, where the apex generator blows up — consistent with [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5's Lee–Yang structure at extreme $\theta$).

### 6.5 The phase-twisted Lee–Yang lattice {#sec:6-5}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5 located the Lee–Yang zeros of $Z_y(\beta)=\cosh(a\beta)$ at $N=2$ on the imaginary $\beta$-lattice $\{i\pi(k+1/2)/a:k\in\mathbb Z\}$. [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) lifts this to the full Bloch sphere via the complex parameter $\eta(\theta,\phi)=\frac{1}{2}\ln\cot(\theta/2)-\frac{i\phi}{2}$.

\hypertarget{stmt:6-2}{}
**Proposition 6.2 (Phase-twisted Lee–Yang lattice).** The zero set of $\mathcal M_z(\beta,0)=\cosh(\beta\eta)$ in $\beta\in\mathbb C$, at the Bloch point $(\theta,\phi)$ with $\eta=\eta(\theta,\phi)\ne 0$, is the lattice
$$\boxed{\big\{\beta\in\mathbb C:\beta\eta=i\pi(k+\tfrac{1}{2}),\;k\in\mathbb Z\big\}=\Big\{\beta_k=\frac{i\pi(k+\tfrac{1}{2})}{\eta(\theta,\phi)}:k\in\mathbb Z\Big\}.}$$
Writing $\eta=ae^{-i\psi}$ in polar form (so $a=|\eta|>0$ and $\psi=-\arg\eta\in(-\pi,\pi]$), the lattice becomes
$$\beta_k=\frac{\pi(k+\tfrac{1}{2})}{a}\cdot e^{i(\pi/2+\psi)},$$
a uniformly-spaced lattice along the ray of angle $\pi/2+\psi$ in $\mathbb C$ with spacing $\pi/a$. On the decoherent equator $\phi=0$: $\psi=0$, lattice on positive imaginary axis (recovers [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5). Off the equator: the lattice **rotates** by $\psi=\arctan\!\big(\frac{\phi}{\ln\cot(\theta/2)}\big)$ and **rescales** by $1/a=1/\sqrt{\frac{1}{4}(\ln\cot(\theta/2))^2+\frac{1}{4}\phi^2}$.

**Proof.** $\cosh w=0$ iff $w=i\pi(k+\tfrac{1}{2})$ for $k\in\mathbb Z$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5 base case). Setting $w=\beta\eta$ and solving for $\beta$: $\beta=i\pi(k+\tfrac{1}{2})/\eta$. Polar substitution $\eta=ae^{-i\psi}$ gives $1/\eta=e^{i\psi}/a$, so $\beta_k=i\pi(k+\tfrac{1}{2})e^{i\psi}/a=\pi(k+\tfrac{1}{2})e^{i(\pi/2+\psi)}/a$, as stated. $\square$

**Geometric picture.** As the Bloch point moves from the decoherent equator $\phi=0$ to the "phase-rotated" point $\phi=\pi/2$ (with $\theta$ fixed in $(0,\pi/2)$), the Lee–Yang lattice **continuously rotates** by an angle that grows from $0$ at $\phi=0$ to $\arctan(\pi/(2\ln\cot(\theta/2)))$ at $\phi=\pi/2$. At the **uniform-modulus equator** $\theta=\pi/2$ (where $\ln\cot(\theta/2)=0$), the rotation angle reaches $\pi/2$ for any $\phi\ne 0$ — the Lee–Yang lattice rotates to the **real $\beta$-axis**, with spacing $2\pi/|\phi|$ (from $a=|\phi|/2$). At the precise point $\theta=\pi/2$, $\phi=0$ (uniform superposition with zero phase), $\eta=0$, the lattice degenerates ($Z_y(\beta)\equiv 1$ has no zeros), the Lee–Yang lattice retreats to infinity.

**Lee–Yang condensation interpretation.** The rotation of the Lee–Yang lattice from the imaginary axis (classical / decoherent) toward the real axis (maximally phase-rotated) is the qubit-level analog of **Lee–Yang condensation** in statistical-mechanics terminology: the zeros of the partition function move from the imaginary axis (no genuine singularity in real $\beta$) toward the real positive axis (a genuine vanishing of the apex generator at specific real $\beta$). At the uniform-modulus equator with non-zero $\phi$, the partition function $\cosh(\beta\eta)$ has zeros on the real positive $\beta$-axis precisely at $\beta_k=2\pi(k+\frac{1}{2})/|\phi|$ — these are not thermodynamic phase transitions in any physical sense, but they are precisely the *quantum-coherence singularities* of the apex generator: real-$\beta$ points at which the modulus-zero phase content produces an exact cancellation between the two basis-state contributions. We flag this as the natural finite-dimensional toy of the Lee–Yang circle theorem (Lee–Yang 1952) for purely-phase ledgers; whether this extends to a general Lee–Yang-style theorem on $\mathcal M_z$ for $N\ge 3$ is forward-door content (\hyperref[sec:7-6]{§7.6}).

### 6.6 Qubit summary table {#sec:6-6}

We assemble the qubit content into a single table organized by integer exponent rung $m$ and character index $c\in\{0,1\}$.

| Rung | $m$ | Apex $\mathcal M_z(m,0)$ | Apex $\mathcal M_z(m,1)$ | Kummer cover | Decoherent ($\phi=0$) interpretation |
|---|---|---|---|---|---|
| $0$ | $0$ | $1$ | $0$ | trivial | normalization |
| Linear | $1$ | $(z_0+z_1)/(2\sqrt{z_0z_1})$ | $(z_0-z_1)/(2\sqrt{z_0z_1})$ | $\mu_2$, double-valued | amplitude sign / $SU(2)\to SO(3)$ |
| Born | $2$ | $(z_0^2+z_1^2)/(2z_0z_1)$ | $(z_0^2-z_1^2)/(2z_0z_1)$ | trivial | $1/\sin\theta$, $\cos\theta/\sin\theta=\cot\theta$ |
| Cubic | $3$ | $\cosh(3\eta)$ | $\sinh(3\eta)$ | $\mu_2$, double-valued | [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §8 / Waring cubic rung |
| Quartic | $4$ | $\cosh(4\eta)$ | $\sinh(4\eta)$ | trivial | $m\equiv 0\pmod 2$ |
| Generic $\beta$ | — | $\cosh(\beta\eta)$ | $\sinh(\beta\eta)$ | holomorphic on the universal cover | full holomorphic family |

The decoherent equator $\phi=0$ recovers [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) (\hyperlink{stmt:4-2}{Theorem~4.2}); the off-equatorial complex sector exhibits the phase deformation (\hyperlink{stmt:4-3}{Proposition~4.3} at $N=2$) and the phase-twisted Lee–Yang lattice (\hyperlink{stmt:6-2}{Proposition~6.2}); the Kummer cover (\hyperref[sec:5]{§5}) acts uniformly across $c$, splitting the integer rungs into single-valued (even $m$) and double-valued (odd $m$) families.

**$N=2$ as the structural anchor of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442).** Just as $N=6$ is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s structural anchor (the smallest cross-prime case), $N=2$ is [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s structural anchor: the smallest dimension where the Hopf fibration, Bloch sphere, and $\mu_2$ Kummer cover all appear non-trivially, the qubit of quantum information, the $SU(2)\to SO(3)$ double cover, and the toy Lee–Yang lattice of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 2.5 all simultaneously. Every claim of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s main theorems (the three-layer factorization, Fubini–Study restriction, modulus-phase factorization, decoherence theorem, Kummer-cover theorem) acquires a fully explicit closed form at this anchor.

---

## 7. Forward doors from [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) {#sec:7}

[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) closes the complex-amplitude door of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) at the pure-state level. Six structural extensions sit naturally beyond it; we catalog them in the corridor format of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §6. The working titles below are deliberately left **unnumbered**: the \heb{ל}-series slots \heb{ל}8–\heb{ל}18 are already occupied by other manuscripts in the programme, and several of these directions overlap existing papers (notably the continuum/Hilbert-space door and the finite-to-Archimedean programme, and the critical-line door and the multiplicative-apex paper \heb{ל}8). Canonical numbers are to be assigned when each is mapped onto — or split off from — the existing suite.

### 7.1 Multi-particle structure and the entanglement stratum {#sec:7-1}

Tensor products $\mathbb C^N\otimes\mathbb C^M$ realize multi-particle quantum systems on $NM$ outcomes. The complex apex $\mathcal M_z(\beta,c)$ on a product state $z=u\otimes v$ ($u\in\mathbb C^N$, $v\in\mathbb C^M$) factorizes through the CRT-style product
$$\mathcal M_{u\otimes v}(\beta,(c_1,c_2))=\mathcal M^{(N)}_u(\beta,c_1)\cdot\mathcal M^{(M)}_v(\beta,c_2)\quad\text{(product-state factorization)}.$$
The **non-factorization** of $\mathcal M_z$ on entangled states is therefore a categorical-simplex measurement of entanglement, analogous to [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4's CRT cross-prime interaction stratum but lifted to the genuinely quantum (Hopf-and-toric covered) setting. The Schmidt decomposition $z=\sum_k\sigma_k\,u_k\otimes v_k$ refines this into a convex-combination expansion of $\mathcal M_z$ over the Schmidt rungs, with the Schmidt coefficients $\sigma_k\in\mathbb R_{>0}$ playing the role of a probability measure on the rungs.

**Conjecture 7.1 (Entanglement measure from the apex).** There exists an entanglement monotone $E_{\mathrm{apex}}(z)$ on the joint amplitude space $\mathbb C^N\otimes\mathbb C^M$, defined as the obstruction-norm of $\mathcal M_z$ from the product-state factorization above (e.g., the $L^2$ distance over $(\beta,c_1,c_2)$ between $\mathcal M_z$ and the closest product), that recovers von-Neumann-entropy-style entanglement on the Schmidt decomposition.

Forward direction (planned forward paper, number to be assigned): **Multi-Particle Tensor Products and the Apex of Entanglement.**

### 7.2 Mixed states, the Petz fork, and the Kubo–Mori selection {#sec:7-2}

\hyperlink{stmt:4-5}{Theorem~4.5} settles the pure-state density-matrix decoherence. The mixed-state forward step — the full $\mathcal M_\rho(\beta,c)$ via the modular Hamiltonian $L_\rho=\log\rho-\frac1N\mathrm{tr}(\log\rho)\,I_N$ — exposes a structural fact the pure-state sector hid, and it is the deepest continuation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s founding question.

**The Petz fork.** On the simplex, Fisher–Rao is the *unique* monotone (Markov-invariant) Riemannian metric (Chentsov 1982) — the uniqueness every gauge of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) shares at the uniform point (§1.4). On density matrices this uniqueness **fails**: the monotone metrics form an infinite family $g^f$ indexed by operator-monotone $f$ with $f(1)=1$ and $f(t)=tf(1/t)$, with coherence weight $c_f(x,y)=1/\big(y\,f(x/y)\big)$ — the Morozova–Chentsov–Petz classification (Morozova–Chentsov 1990; Petz 1996). Three named rungs, ordered harmonic $\le f\le$ arithmetic (Petz–Sudár 1996):

| metric | $f(t)$ | mean $\mathfrak m_f$ | role |
|---|---|---|---|
| Bures / SLD | $(1+t)/2$ | arithmetic | quantum Cramér–Rao (estimation); *minimal* monotone metric |
| Kubo–Mori (BKM) | $(t-1)/\log t$ | logarithmic | Hessian of relative entropy; *dually flat* |
| RLD | $2t/(1+t)$ | harmonic | *maximal* monotone metric |

So a naïve "the quantum Fisher information" is ambiguous; a gauge $f$ must be chosen — the **operator-valued continuation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s scalar power-mean corridor**. The classical question *what is additive?* (a scalar mean, the power $r$) becomes *how are coherences weighted?* (an operator mean, the function $f$). Concretely, for non-diagonal $\rho$ the operators $\log\rho$ and $C_c$ do not commute, so the $\beta$-Taylor coefficients of $\mathcal M_\rho$ are non-commutative moments whose operator ordering *is* the choice of $f$.

**Decoherent-face collapse (metric form of the decoherence theorem).** Every monotone metric agrees on the diagonal stratum: for $\rho=\mathrm{diag}(p)$ and a diagonal tangent $V=\mathrm{diag}(v)$ with $\sum_sv_s=0$,
$$g^f_\rho(V,V)=\sum_s c_f(p_s,p_s)\,v_s^2=\sum_s\frac{v_s^2}{p_s}=g^{\mathrm{FR}}_p(v,v)\quad\text{for every }f,$$
since $c_f(x,x)=1/\big(x\,f(1)\big)=1/x$ — the *idempotency of means* $\mathfrak m_f(x,x)=x$. This is the metric counterpart of \hyperlink{stmt:4-2}{Theorem~4.2}: the gauge freedom of the fork vanishes exactly on the real-positive (decoherent) face. Chentsov uniqueness is, in this light, no deep accident — it is the statement that all means agree when their two arguments coincide.

**The apex generator forces Kubo–Mori, not Bures.** Along a single escort line $\rho_\beta=e^{\beta H}/\mathrm{tr}\,e^{\beta H}$ the generator is gauge-free and reproduces [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)'s cumulant tower of $\mathrm{spec}(H)$ (no $f$ appears, since $H$ commutes with $e^{\beta H}$). The fork bites only in the *transverse* second-order structure: for a non-commuting exponential family $\rho_\theta=\exp(\theta^iH_i-\psi(\theta))$, the Hessian $\partial_i\partial_j\psi$ equals the monotone metric $g^f$ **iff** $f$ is Kubo–Mori (Amari–Nagaoka 2000, ch. 7; uniqueness of the dually-flat monotone metric: Grasselli–Streater 2001). Since $\mathcal M_\rho$ is an exponential-family object in $L_\rho=\log\rho-\cdots$, it is the convex potential of a dually-flat geometry **only** for Kubo–Mori. Hence the corrected reading: the density-matrix apex is the **Kubo–Mori potential**; **Bures is the estimation member** (quantum Cramér–Rao, Braunstein–Caves 1994) and the pure-state Fubini–Study restriction of \hyperref[sec:2]{§2}, agreeing with Kubo–Mori only on the decoherent face. This mirrors the scalar corridor exactly: [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) already singled out the geometric/$\log$ gauge ($r=0$) as the potential-carrying center; Kubo–Mori — the $\log\rho$ metric — is its operator continuation, while Bures is the analog of the $r=2$ Born gauge (operationally central, but not potential-carrying).

**A metric for the phase fiber (by-product for [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)).** At $\rho=\mathrm{diag}(p)$ every $g^f$ is diagonal in the $\mathbb Z/N$ coherence-order grading $X=\sum_kX^{(k)}$, $X^{(k)}=\sum_{s-s'\equiv k}X_{ss'}|s\rangle\langle s'|$: the order-$0$ block is the gauge-rigid Fisher–Rao metric of \hyperref[sec:2]{§2}, while the order-$k\ne0$ blocks — exactly the tangent directions of the relative-phase fiber $T^{N-1}$ of \hyperref[sec:1-2]{§1.2} — carry the *entire* gauge dependence, with block weight $c_f(p_s,p_{s+k})$. The fork thus equips the phase fiber, introduced in \hyperref[sec:1]{§1} only as a symplectic/toric object, with a Riemannian metric for the first time; the coherence order $k$ and the conductor index $c$ are the same $\mathbb Z/N$-grading read on operators versus on functions, so the metric is conductor-graded.

**Conjecture 7.2 (Density-matrix decoherence theorem).** Let $\mathcal P$ be the computational-basis dephasing channel. Then for every full-rank $\rho$, every $\beta\in\mathbb C$, and every $c\in\widehat{\mathbb Z/N}$,
$$\mathcal M_{\mathcal P(\rho)}(\beta,c)=\mathcal M_{\sqrt{\mathrm{diag}(\rho)}}(\beta_{\mathrm{ps}}=2\beta,c),$$
extending \hyperlink{stmt:4-5}{Theorem~4.5} from the pure-state stratum to the full density-matrix simplex. (This statement is *metric-independent* — it concerns the generator's value, not its Hessian — so it is unaffected by the Petz fork.)

Forward direction (planned): **The Monotone-Metric Apex — the Petz Fork and the Kubo–Mori Selection** (Bures = SLD/estimation rung; Kubo–Mori = dually-flat/potential rung; the two agree on the decoherent face).

### 7.3 The Kubo–Mori replicator and quantum natural-gradient flow {#sec:7-3}

The replicator $\beta$-flow of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4 is the Shahshahani / Fisher gradient flow on the simplex. Its quantum lift is the natural-gradient flow on the density-matrix manifold along the monotone metric selected in \hyperref[sec:7-2]{§7.2}. Because the free-energy identities $\partial_\beta\Psi=\langle L_\rho\rangle$, $\partial_\beta^2\Psi=\mathrm{Var}$ of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4 hold only for the dually-flat member, the correct quantum replicator is the **Kubo–Mori** (BKM) flow, not the Bures one. The complex apex $\mathcal M_z(\beta,c)$ remains the **free energy** along this flow on each character mode; on a single escort line it is gauge-free (\hyperref[sec:7-2]{§7.2}).

**Conjecture 7.3 (Kubo–Mori replicator).** The escort family $\rho_\beta:=e^{\beta L_\rho}/\mathrm{tr}(e^{\beta L_\rho})$ on density matrices is the Kubo–Mori natural-gradient flow of the expectation functional $\rho\mapsto\mathrm{tr}(\rho\,L_\rho)$, and $\partial_\beta\mathcal M_\rho(\beta,c)$ is the BKM (Bogoliubov–Kubo–Mori) covariance of $L_\rho$ against the character operators $C_c$ — the quantum analog of the replicator/character-convolution identity of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4. The Bures natural-gradient flow is the distinct *estimation-side* companion, coinciding with the Kubo–Mori flow only on the decoherent face.

Forward direction (planned forward paper, number to be assigned): **The Kubo–Mori Replicator and Quantum Natural-Gradient Flow** (with the Bures flow as the estimation-side companion).

### 7.4 Holomorphic flow and the zero structure of $\mathcal M_z$ {#sec:7-4}

\hyperlink{stmt:3-4}{Proposition~3.4} establishes $\mathcal M_z(\beta,c)$ as entire in $\beta$ on each branch. The qubit case (\hyperlink{stmt:6-2}{Proposition~6.2}) gives the complete zero set in closed form: a phase-twisted lattice that rotates from imaginary to real as the Bloch point moves off the decoherent equator. For $N\ge 3$, the zero set is not pinned to any single curve by elementary arithmetic; its global structure is the natural finite-categorical analog of the zeros of an $L$-function.

Two structural facts already organize this holomorphic plane. First, **Wick rotation**: the replicator gradient flow of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §2.4 lives on the *real* $\beta$-axis (dissipative ascent of mean fitness), while the Lee–Yang zeros sit on the *imaginary* axis (\hyperlink{stmt:6-2}{Proposition~6.2}); $\beta\mapsto i\beta$ rotates the dissipative replicator into oscillatory unitary evolution and marks the quantum resonances at the Lee–Yang lattice. Second, **Carlson rigidity** (\hyperlink{stmt:5-7}{Proposition~5.7}) is already a theorem, not a door: on the decoherent face the real-integer closure samples over-determine the entire generator, so the two diagonals are rigidly linked, and the rigidity degrades sheet-to-sheet exactly through the $\mu_N$ Kummer cover (\hyperlink{stmt:5-8}{Remark~5.8}). The forward content of this door is therefore the *complex-stratum* zero geometry for $N\ge 3$, where phase winding past the Carlson threshold and the Kummer monodromy jointly shape the zero variety.

**Conjecture 7.4 (Lee–Yang on the complex apex).** For ledgers $z$ in suitable arithmetic strata of $\mathbb C^N$ (e.g., when $|z_s|$ encodes prime structure on $\mathbb Z/N$), the zeros of $\mathcal M_z(\beta,c)$ in $\beta$ lie on a structured subvariety of $\mathbb C$ that mixes imaginary-axis content (the decoherent / Lee–Yang content of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)) with off-axis phase-twisted content (the Bloch-rotated content of \hyperlink{stmt:6-2}{Proposition~6.2}).

Forward direction (planned forward paper, number to be assigned): **The Lee–Yang Zero Variety of the Complex Apex.**

### 7.5 Infinite-dimensional limit ($N\to\infty$, Hilbert-space apex) {#sec:7-5}

The complex amplitude space $\mathbb C^N$ specializes finite-dimensional quantum mechanics. The continuum / Hilbert-space limit replaces $\mathbb Z/N$ by a continuous label group (the real line, the circle, a Lie group), $\mathbb C^N$ by a separable Hilbert space, and the moment map $\pi_{\mathrm{Born}}$ by the Born measure of a quantum state. The complex apex $\mathcal M_z(\beta,c)$ should generalize to an integral kernel $\mathcal M_\psi(\beta,\xi)$ depending on a Mellin parameter $\beta\in\mathbb C$ and a Pontryagin dual $\xi\in\widehat G$.

**Conjecture 7.5 (Hilbert-space apex).** The complex apex of a Hilbert-space state $|\psi\rangle$ on $G$ is the Mellin transform of the centered log-amplitude under the Pontryagin dual character $\chi_\xi$, holomorphic in $\beta$ on appropriate functional-analytic domains, with the decoherence theorem extending to the modulus-restriction $\psi\mapsto|\psi|$ in the position representation. The finite-categorical [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) is the $G=\mathbb Z/N$ specialization.

Forward direction (planned forward paper, number to be assigned; cf. the existing finite-to-Archimedean completion programme): **Hilbert-Space Apex and Continuum Quantum Sectors.**

### 7.6 RH-shaped questions at the complex apex {#sec:7-6}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §6.6 / §6.7 asks whether the zeros of the apex generator line up on a critical line for arithmetically structured ledgers. The complex extension provides richer phase content: the cross-prime interaction stratum on $\mathbb Z/N$ for $N$ with multiple prime factors acquires the Hopf-and-toric phase structure, and the additive RH-shaped question (do zeros of $\mathcal M_z$ for primorial ledgers concentrate on a critical line in $\beta\in\mathbb C$?) becomes phase-sensitive in a precise way.

**Aspiration vs. theorem.** Posed over the *additive* characters $\chi_c(s)=e^{2\pi ics/N}$ of $\mathbb Z/N$, this is an aspiration, not a concrete target, and we record it as such. The additive apex $\mathcal M_z(\beta,c)$ is a finite exponential sum in $\beta$; its zero set is a phase-twisted lattice (\hyperlink{stmt:6-2}{Proposition~6.2}) carrying no arithmetic normalization that would *force* the zeros onto a line. There is no Frobenius, no cohomological weight, and no $\sqrt q$ scale in the additive $\mathbb Z/N$ setting: $\mathbb Z/N$ is the residue ring of the number field $\mathbb Q$, and the matching critical-line statement there (RH for $\zeta$, GRH for Dirichlet $L$) is itself the open conjecture. Conjecture 7.6 is therefore a heuristic; the *concrete provable* RH target is relocated to the multiplicative / function-field apex of \heb{ל}8 described below, where the analogous statement is a theorem of Weil.

**Conjecture 7.6 (Complex critical line — additive aspiration).** For primorial $N=P_k=\prod_{p\le p_k}p$ and ledger $x$ encoding prime structure on $\mathbb Z/N$ (e.g., the indicator of units in $(\mathbb Z/N)^\times$), the zeros of $\mathcal M_z(\beta,c)$ in $\beta\in\mathbb C$ for $z$ on the *decoherent equator* of the complex extension concentrate on a critical line $\mathrm{Re}\,\beta=\beta_*$ in a finite-categorical analog of RH; the off-equator phase-twisted zeros rotate the critical line by a phase angle controlled by the position on $T^{N-1}$. The statement is heuristic: the additive setting supplies no mechanism that pins $\mathrm{Re}\,\beta$, and the conjecture is retained only to mark the phase-geometric *shape* of the question, not as a target the additive apex can close.

**The concrete provable target: the multiplicative / function-field apex.** \heb{ל}8 installs the layer in which an RH analog is a *theorem* rather than a conjecture. Two moves are required, and only their composition buys the theorem. First, pass from additive to **multiplicative** characters — \heb{ל}8's Dirichlet characters $\psi$ of $(\mathbb Z/N)^\times$, with the Gauss-sum bridge $\tau(\psi,a)$ (\heb{ל}8 §4) intertwining the two sectors. Second — the decisive step — change the base ring from $\mathbb Z/N$ (residues of $\mathbb Q$) to a **finite field** $\mathbb F_q$ (the function-field / geometric place), realized by taking multiplicative characters of $\mathbb F_q^\times$ of order dividing $N$, which exist precisely when $N\mid q-1$. Over $\mathbb F_q$ the abstract Gauss-sum bridge becomes the genuine Gauss sum $\tau_q(\chi)=\sum_{t\in\mathbb F_q^\times}\chi(t)\,\psi_{\mathrm{add}}(t)$ (with $\psi_{\mathrm{add}}$ a fixed nontrivial additive character of $\mathbb F_q$), whose modulus $|\tau_q(\chi)|=q^{1/2}$ is already a critical-modulus statement, and the Jacobi sums $J(\chi^a,\chi^b)=\sum_{t}\chi^a(t)\,\chi^b(1-t)$ (with $|J|=q^{1/2}$ for nontrivial factors of nontrivial product) are *the Frobenius eigenvalues* on $H^1$ of the Fermat curve $C_N:\ x_0^N+x_1^N+x_2^N=0$ over $\mathbb F_q$ (Weil 1949). The object that carries a provable RH is then the finite $L$-function attached to multiplicative-character amplitudes encoding point-counts,
$$Z(C_N/\mathbb F_q,T)=\exp\!\Big(\sum_{n\ge1}\tfrac{\#C_N(\mathbb F_{q^n})}{n}T^n\Big)=\frac{P(T)}{(1-T)(1-qT)},\qquad P(T)=\prod_{i=1}^{2g}(1-\alpha_iT),$$
$g=\tfrac{(N-1)(N-2)}{2}$, with $\#C_N(\mathbb F_{q^n})=q^n+1-\sum_i\alpha_i^n$ and the inverse roots $\alpha_i$ running over the Jacobi sums. **Weil's RH for curves** (Weil 1948, 1949; Deligne 1974 in arbitrary dimension) is the theorem $|\alpha_i|=q^{1/2}$; under $T=q^{-s}$ this is exactly $\mathrm{Re}\,s=\tfrac12$ — a genuine critical line, proved. The categorical multiplicative apex $\mathcal D_x(\beta,\psi)$ of \heb{ל}8 is the $\mathbb F_q\!\rightsquigarrow\!(\mathbb Z/N)^\times$ shadow of this object; the concrete forward door is to build its $\mathbb F_q$ lift and read Weil's theorem off the apex (see \heb{ל}8 §7.3).

**Relation to the standing simplicial-RH programme.** \heb{ל}20's governed-closure architecture (with the primorial $\mathbb Z/6$ Hurwitz collapse and the Paper III Gram–Bures bridge) targets the *classical* RH for $\zeta$ over $\mathbb Q$ — the Archimedean place, where the critical line remains conjectural and must be reached by a cofinal Archimedean lift. The function-field apex is the complementary *finite / geometric* place: there the critical line needs no lift, because the $L$-function is already a polynomial whose zeros are pure of weight one — Frobenius supplies for free the purity that the Archimedean programme must manufacture. The function-field multiplicative apex is therefore the programme's worked, provable instance of its own RH-shaped door, and a sharp localization of *why* the classical target is hard: it is the missing-Frobenius place.

Forward direction (planned forward paper, number to be assigned): **The Function-Field Multiplicative Apex and Weil's Theorem — A Provable Critical Line for the Categorical Simplex.**

---

## 8. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) through [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) as worked cells through the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) lens {#sec:8}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §7 placed [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) as worked cells of the apex surface $\mathcal M_x(\beta,c)$. The complex extension promotes each cell to a slice through the larger phase-bundle structure; we re-locate the six papers within [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)'s framework.

### 8.1 [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Native Simplicial Chart, as the decoherent face {#sec:8-1}

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart on $\mathring\Delta^{N-1}$ via the square-root map $\sqrt p:\Delta^{N-1}\to S^{N-1}_+$ identifies the simplex with the positive face of the real sphere, with Fisher–Rao the pulled-back round metric. In the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) framing, this is the **decoherent face** of the complex amplitude space (\hyperlink{stmt:1-2}{Definition~1.2}), and the chart is the canonical "no-phase" section $\sigma_{\mathrm{R+}}$ of the Hopf-and-toric fibrations (\hyperref[sec:1-3]{§1.3}). The factor of $2$ in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s Fisher–Rao distance is the projective-angle doubling of \hyperlink{stmt:2-1}{Theorem~2.1}.

### 8.2 [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Cumulant Tower, as the moment diagonal on the decoherent face {#sec:8-2}

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s cumulant tower at the uniform $u\in\Delta^{N-1}$ samples the moment diagonal ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 3.3) at $\beta=0,c=0$. In the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) framing, this is the moment diagonal of $\mathcal M_z(\beta,c)$ restricted to the decoherent face: the **classical** moment tower is the phase-zero sample of the complex moment tower, with the off-equator complex extension producing additional phase-twisted moment content (\hyperlink{stmt:4-3}{Proposition~4.3}'s coherence content at order $n$).

### 8.3 [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Character Orthogonality, as the conductor index of the complex apex {#sec:8-3}

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s character orthogonality on $\mathbb Z/N$ activates the conductor index $c$. The complex extension preserves [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s selection rule $a+b+c\equiv 0\pmod N$ (\hyperlink{stmt:5-5}{Theorem~5.5}) — the Kummer-cover deck-group action is independent of $c$, acting uniformly across all conductor modes. [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s conductor packets $H_d$ remain the eigenspaces of the character decomposition.

### 8.4 [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — Helmert-Simplicial Residue Ladder, as the rational basis dual to the Kummer cover {#sec:8-4}

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s Helmert ladder is the rational orthogonal basis of $H_N$. In [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442), the Helmert basis is the **rational descent** of the Kummer cover: each Helmert vector $e_k$ corresponds to a rational character of the toric quotient $T^{N-1}$ acting on $\mathbb{CP}^{N-1}$, and the radical clock $K_N$ records the field arithmetic of the Helmert normalizers $\sqrt{k(k+1)}$ — a rational/radical shadow of the complex/transcendental phase content of $T^{N-1}$.

### 8.5 [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — Harmonic-Simplicial Dual Gauge, as the parity reading of the complex apex {#sec:8-5}

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s $\beta\to-\beta$ parity decomposition extends naturally to $\mathcal M_z(\beta,c)$ in the complex variable: the parity pair $\mathcal M_z(\beta,c)+\mathcal M_z(-\beta,c)$ doubles the even-$\beta$ Fourier content on $T^{N-1}$, $\mathcal M_z(\beta,c)-\mathcal M_z(-\beta,c)$ doubles the odd. On the decoherent face this recovers [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s classical parity; off the decoherent face the parity reading is phase-twisted by the Bloch-rotation angle of \hyperlink{stmt:6-2}{Proposition~6.2}.

### 8.6 [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — RMS-Simplicial Quadratic Gauge, as the $m=2$ Born rung of the closure diagonal {#sec:8-6}

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s $\beta=2$ RMS / Born closure is the $m=2$ closure diagonal of the complex apex. In [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442), this is the $\rho_2=\chi_{-2\bmod N}$ deck-group character of the Kummer cover (\hyperlink{stmt:5-3}{Theorem~5.3}). For $N=2$ (qubit), $\rho_2=\chi_0$ is trivial — Born closure descends to the Bloch sphere without obstruction (\hyperref[sec:6-3]{§6.3}). For odd $N\ge 3$, $\rho_2$ is non-trivial — Born closure acquires a $\mu_N$ branch obstruction in the complex extension, which the decoherent restriction suppresses. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Conjecture 4 (complex amplitude extension) is the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) program; \hyperlink{stmt:4-2}{Theorem~4.2} + \hyperlink{stmt:5-3}{Theorem~5.3} jointly close the conjecture as a structure theorem.

### 8.7 Grid summary

| Paper | [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) slice | Worked content |
|---|---|---|
| [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) | decoherent face / square-root section | Fisher–Rao = $\frac{1}{4}$ Fubini–Study restriction |
| [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) | moment diagonal restricted to decoherent face | classical cumulant tower as zero-phase content of complex moments |
| [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) | conductor index $c$ of $\mathcal M_z$ | selection rule preserved by Kummer cover |
| [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) | rational descent of toric $T^{N-1}$ | Helmert basis as radical shadow of phase content |
| [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) | parity reading of $\mathcal M_z$ in $\beta$ | classical parity on decoherent face, phase-twisted off-face |
| [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) | closure diagonal $m=2$, $\rho_2$-Kummer character | Born closure = decoherent restriction of complex $m=2$ rung |
| [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) | the complex bundle itself | $\mathcal M_z$, decoherence theorem, Kummer-cover theorem, qubit anchor |

Six worked cells of the decoherent face; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) names the bundle they sit inside.

---

## 9. Coda {#sec:9}

The complex amplitude extension reveals the apex as a four-layer structure: a positive ledger $x\in\mathbb R_{>0}^N$ ([\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)), its Fourier-Mellin transform on $\mathbb Z/N$ ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985)), the radial-and-phase-bundle structure $\mathbb C^N\to\mathbb{CP}^{N-1}\to\Delta^{N-1}$ ([\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)), and the natural Galois/Kummer cover that becomes literal in the complex extension. The *pure-state phase redundancy* of finite-dimensional quantum mechanics on $\mathbb C^N$ is the cover structure, made non-trivial by the phase fiber.

The one-sentence apex of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442):

$$\boxed{\begin{array}{c}\text{The pure-state phase structure of finite-dimensional quantum mechanics on }\mathbb C^N\\\text{is the Hopf-and-toric covering of the categorical-simplex apex of }\text{\heb{ל}0.}\end{array}}$$

with global phase the Hopf $U(1)$, relative phase the toric $T^{N-1}$, and decoherence the modulus-restriction projection to the real-positive sector — the decoherent face on which $\mathcal M_z$ reduces to $\mathcal M_x$ exactly.

**Scope.** The cover is a statement about *phase redundancy*, not about all of quantum mechanics. It does not encode the non-commutativity of observables, measurement back-action, unitary dynamics, or the tensor-product/entanglement structure of multi-particle systems; those are the forward doors of \hyperref[sec:7]{§7}. The two slogans below are to be read in this scoped sense.

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) named the surface; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) names the phase bundle over it.

And the opening sentence, restated (in the scoped sense above):

> **Decoherence is closure of phase. Quantization is the cover.**

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The collaborations were intellectually substantive: AI partners contributed insights, proposed theorems and conjectures, surfaced relevant literature, verified derivations, and iterated on exposition. The development of the three-layer factorization, the decoherence theorem, the Kummer-cover-at-integer-$\beta$ statement, and the pure-state density-matrix decoherence theorem emerged through a sequence of critique-and-upgrade exchanges that I record transparently. The selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References

### \heb{ל}-series (companion papers)

- Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985).
- Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).
- Murillo Montero, L. (2026). *[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).
- Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).
- Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert-Simplicial Residue Ladder.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504).
- Murillo Montero, L. (2026). *[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — The Harmonic-Simplicial Dual Gauge.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20388419](https://doi.org/10.5281/zenodo.20388419).
- Murillo Montero, L. (2026). *[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — The RMS-Simplicial Quadratic Gauge.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392428](https://doi.org/10.5281/zenodo.20392428).
- Murillo Montero, L. (2026). *[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo preprint (this work; concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442).

### Information geometry, statistics, and quantum information geometry

- Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Lecture Notes in Statistics 28. Berlin: Springer. ISBN 978-0-387-96056-2. [DOI: 10.1007/978-1-4612-5056-2](https://doi.org/10.1007/978-1-4612-5056-2).
- Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs, Vol. 191. Providence, RI: American Mathematical Society. ISBN 978-0-8218-0531-2. [AMS page](https://bookstore.ams.org/mmono-191).
- Ay, N., Jost, J., Lê, H. V., and Schwachhöfer, L. (2017). *Information Geometry.* Ergebnisse der Mathematik und ihrer Grenzgebiete 64. Cham: Springer. ISBN 978-3-319-56477-7. [DOI: 10.1007/978-3-319-56478-4](https://doi.org/10.1007/978-3-319-56478-4).
- Bengtsson, I. and Życzkowski, K. (2017). *Geometry of Quantum States: An Introduction to Quantum Entanglement.* 2nd ed. Cambridge: Cambridge University Press. ISBN 978-1-107-02625-4. [DOI: 10.1017/9781139207010](https://doi.org/10.1017/9781139207010).
- Bhattacharyya, A. (1943). On a measure of divergence between two statistical populations defined by their probability distributions. *Bulletin of the Calcutta Mathematical Society* 35, 99–109.
- Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs, Vol. 53. Providence, RI: American Mathematical Society. ISBN 978-0-8218-4502-8.
- Petz, D. (2008). *Quantum Information Theory and Quantum Statistics.* Theoretical and Mathematical Physics. Berlin: Springer. ISBN 978-3-540-74634-8. [DOI: 10.1007/978-3-540-74636-2](https://doi.org/10.1007/978-3-540-74636-2).
- Provost, J. P. and Vallee, G. (1980). Riemannian structure on manifolds of quantum states. *Communications in Mathematical Physics* 76, 289–301. [DOI: 10.1007/BF02193559](https://doi.org/10.1007/BF02193559).

### Monotone metrics, the Petz fork, Bures, and quantum Fisher information

- Bures, D. (1969). An extension of Kakutani's theorem on infinite product measures to the tensor product of semifinite $W^*$-algebras. *Transactions of the American Mathematical Society* 135, 199–212. [DOI: 10.2307/1995012](https://doi.org/10.2307/1995012).
- Uhlmann, A. (1976). The "transition probability" in the state space of a $*$-algebra. *Reports on Mathematical Physics* 9, 273–279. [DOI: 10.1016/0034-4877(76)90060-4](https://doi.org/10.1016/0034-4877(76)90060-4).
- Kubo, F. and Ando, T. (1980). Means of positive linear operators. *Mathematische Annalen* 246, 205–224. [DOI: 10.1007/BF01371042](https://doi.org/10.1007/BF01371042).
- Morozova, E. A. and Chentsov, N. N. (1990). Markov invariant geometry on manifolds of states. *Itogi Nauki i Tekhniki, Sovremennye Problemy Matematiki* 36, 69–102. (English transl. *Journal of Soviet Mathematics* 56 (1991), 2648–2669.)
- Braunstein, S. L. and Caves, C. M. (1994). Statistical distance and the geometry of quantum states. *Physical Review Letters* 72, 3439–3443. [DOI: 10.1103/PhysRevLett.72.3439](https://doi.org/10.1103/PhysRevLett.72.3439).
- Petz, D. (1996). Monotone metrics on matrix spaces. *Linear Algebra and its Applications* 244, 81–96. [DOI: 10.1016/0024-3795(94)00211-8](https://doi.org/10.1016/0024-3795(94)00211-8).
- Petz, D. and Sudár, C. (1996). Extending the Fisher metric to density matrices. *Journal of Mathematical Physics* 37, 2662–2673. [DOI: 10.1063/1.531535](https://doi.org/10.1063/1.531535).
- Grasselli, M. R. and Streater, R. F. (2001). On the uniqueness of the Chentsov metric in quantum information geometry. *Infinite Dimensional Analysis, Quantum Probability and Related Topics* 4, 173–182. [DOI: 10.1142/S0219025701000462](https://doi.org/10.1142/S0219025701000462).

### Symplectic / toric geometry and complex projective space

- Atiyah, M. F. (1982). Convexity and commuting Hamiltonians. *Bulletin of the London Mathematical Society* 14, 1–15. [DOI: 10.1112/blms/14.1.1](https://doi.org/10.1112/blms/14.1.1).
- Guillemin, V. and Sternberg, S. (1982). Convexity properties of the moment mapping. *Inventiones Mathematicae* 67, 491–513. [DOI: 10.1007/BF01398933](https://doi.org/10.1007/BF01398933).
- Hopf, H. (1931). Über die Abbildungen der dreidimensionalen Sphäre auf die Kugelfläche. *Mathematische Annalen* 104, 637–665. [DOI: 10.1007/BF01457962](https://doi.org/10.1007/BF01457962).
- Cannas da Silva, A. (2001). *Lectures on Symplectic Geometry.* Lecture Notes in Mathematics 1764. Berlin: Springer. ISBN 978-3-540-42195-5. [DOI: 10.1007/978-3-540-45330-7](https://doi.org/10.1007/978-3-540-45330-7).
- Griffiths, P. and Harris, J. (1994). *Principles of Algebraic Geometry.* New York: John Wiley & Sons. ISBN 978-0-471-05059-9. [DOI: 10.1002/9781118032527](https://doi.org/10.1002/9781118032527).

### Algebra, Kummer theory, and Galois covers

- Lang, S. (2002). *Algebra.* Revised 3rd ed. Graduate Texts in Mathematics 211. New York: Springer. ISBN 978-0-387-95385-4. [DOI: 10.1007/978-1-4613-0041-0](https://doi.org/10.1007/978-1-4613-0041-0). (Kummer theory: Chapter VI.)
- Pontryagin, L. S. (1939). *Topological Groups.* Princeton, NJ: Princeton University Press. (Translated by E. Lehmer.)
- Neukirch, J. (1999). *Algebraic Number Theory.* Grundlehren der mathematischen Wissenschaften 322. Berlin: Springer. ISBN 978-3-540-65399-8. [DOI: 10.1007/978-3-662-03983-0](https://doi.org/10.1007/978-3-662-03983-0).
- Milne, J. S. (2020). *Fields and Galois Theory* (v5.10). Online lecture notes. [https://www.jmilne.org/math/CourseNotes/FT.pdf](https://www.jmilne.org/math/CourseNotes/FT.pdf).

### Lee–Yang, statistical mechanics, and analytic boundary

- Lee, T. D. and Yang, C. N. (1952). Statistical theory of equations of state and phase transitions. II. Lattice gas and Ising model. *Physical Review* 87, 410–419. [DOI: 10.1103/PhysRev.87.410](https://doi.org/10.1103/PhysRev.87.410).
- Bena, I., Droz, M., and Lipowski, A. (2005). Statistical mechanics of equilibrium and nonequilibrium phase transitions: the Yang–Lee formalism. *International Journal of Modern Physics B* 19, 4269–4329. [DOI: 10.1142/S0217979205032759](https://doi.org/10.1142/S0217979205032759).

### Entire functions and interpolation (Carlson rigidity)

- Carlson, F. (1914). *Sur une classe de séries de Taylor.* Dissertation, Uppsala.
- Boas, R. P. (1954). *Entire Functions.* Pure and Applied Mathematics 5. New York: Academic Press. (Carlson's theorem: Thm 9.2.1.)

### Finite fields, $L$-functions, and Weil's Riemann hypothesis

- Weil, A. (1948). On some exponential sums. *Proceedings of the National Academy of Sciences USA* 34, 204–207. [DOI: 10.1073/pnas.34.5.204](https://doi.org/10.1073/pnas.34.5.204).
- Weil, A. (1949). Numbers of solutions of equations in finite fields. *Bulletin of the American Mathematical Society* 55, 497–508. [DOI: 10.1090/S0002-9904-1949-09219-4](https://doi.org/10.1090/S0002-9904-1949-09219-4). (Jacobi sums as Frobenius eigenvalues of Fermat / diagonal varieties; the curve RH.)
- Deligne, P. (1974). La conjecture de Weil. I. *Publications Mathématiques de l'IHÉS* 43, 273–307. [DOI: 10.1007/BF02684373](https://doi.org/10.1007/BF02684373). (Weil RH in arbitrary dimension; purity of weight.)
- Ireland, K. and Rosen, M. (1990). *A Classical Introduction to Modern Number Theory.* 2nd ed. Graduate Texts in Mathematics 84. New York: Springer. ISBN 978-0-387-97329-6. [DOI: 10.1007/978-1-4757-2103-4](https://doi.org/10.1007/978-1-4757-2103-4). (Gauss and Jacobi sums; the Fermat-curve point count, Ch. 8 & 11.)
- Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory.* American Mathematical Society Colloquium Publications 53. ISBN 978-0-8218-3633-0. (Gauss sums §3.5; function-field $L$-functions and Weil's theorem.)

### Quantum mechanics foundational

- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik.* Berlin: Springer. (English: *Mathematical Foundations of Quantum Mechanics*, Princeton 1955; new translation by N. A. Wheeler, Princeton 2018, ISBN 978-0-691-17856-1.)
- Nielsen, M. A. and Chuang, I. L. (2010). *Quantum Computation and Quantum Information.* 10th anniversary ed. Cambridge: Cambridge University Press. ISBN 978-1-107-00217-3. [DOI: 10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667).
- Dirac, P. A. M. (1958). *The Principles of Quantum Mechanics.* 4th ed. Oxford: Clarendon Press. ISBN 978-0-19-852011-5.
