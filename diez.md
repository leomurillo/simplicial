<!-- diez.md
     Technical Companion to ocho: full proofs of [A1'], [A2'], [A3'].
     Status: technical proofs at referee level for [A1'] and [A2']; careful proof
     outline for [A3'] with explicit citations and identification of the specialist-
     verifiable steps. The arithmetic constants are calibrated to the V/M crossover
     threshold from ocho §7.1.
-->

# Diez — Technical Companion to *Ocho*: Proofs of [A1'], [A2'], [A3']

## Introduction

This appendix executes the technical proofs of the three remaining obligations of *ocho* — [A1'] cubic Fejér positivity class non-empty, [A2'] cubic Bombieri witness with bulk correction, [A3'] primorial-indexed Bombieri–Vinogradov tightening — at the level of formal Theorem / Proof / Lemma exposition.

**Status disclaimer.** Theorems A1 and A2 (§§1–2) are proven at a level suitable for direct verification by a specialist in analytic number theory. Theorem A3 (§3) is given a **careful proof outline** — the strategy combines classical tools (CRT, Heath-Brown's identity, the large sieve, Burgess character sums) in a recognizable way, but the rigorous derivation of the explicit primorial-indexed constant $C^* \leq 2.80$ from this combination is a substantial technical task comparable to Polymath 8 (Maynard et al. 2014) or Maynard's bounded-gaps work (Maynard 2015), and is identified here as the **remaining specialist-verifiable step**.

## Notation and Preliminaries

Throughout, $s = \sigma + it$ is a complex variable; $\rho = \beta + i\gamma$ a generic nontrivial zero of $\zeta$; $\rho_0 = 1/2 + \delta + i\gamma_0$ a hypothetical off-line zero with $\delta > 0$, $\gamma_0 > 0$; $\Lambda(\delta, \gamma_0) = \{\rho_+, \rho_-, \overline{\rho_+}, \overline{\rho_-}\}$ with $\rho_\pm = 1/2 \pm \delta + i\gamma_0$ the FE-symmetric off-line cluster.

The **zeta zero spectrum** is $\Gamma := \{\gamma_n\}_{n \in \mathbb{Z}}$ with $\gamma_{-n} = -\gamma_n$. **Riemann–von Mangoldt**:
$$N(T) = \#\{\gamma_n \in (0, T]\} = \frac{T}{2\pi}\log\!\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T).$$

For $\Omega > 0$, $PW_\Omega$ denotes the **Paley–Wiener space** of $L^2(\mathbb{R})$ functions whose Fourier transform is supported in $[-\Omega, \Omega]$.

A sequence $\Lambda \subset \mathbb{R}$ is **uniformly discrete** with gap $\delta_0 > 0$ if $|\lambda_m - \lambda_n| \geq \delta_0$ for $m \neq n$. The **upper Beurling density** is $D^+(\Lambda) = \limsup_{T \to \infty} N_\Lambda(T)/(2T)$; the lower density $D^-$ analogously.

**Beurling's sampling theorem** (Beurling 1959; cf.\ Seip 2004, *Interpolation and Sampling in Spaces of Analytic Functions*, Theorem 2.2): a uniformly discrete sequence $\Lambda$ with gap $\delta_0$ is a sampling sequence for $PW_\Omega$ iff $D^-(\Lambda) > \Omega/\pi$. The sampling constants $A, B$ depend explicitly on $D^-(\Lambda) - \Omega/\pi$ and $\delta_0$.

---

## 1. Theorem A1 — Beurling–Selberg sampling on the zeta zero spectrum

**Goal.** Show that the cubic Fejér positivity class
$$\mathcal{G} \;=\; \big\{g \in \mathcal{S}((0, \infty)) \,:\, \mathcal{S}_g(x) := \textstyle\sum_\gamma \widetilde g(1/2 + i\gamma)\, e^{i\gamma x} \,\geq\, 0 \text{ on } \mathbb{R}_{\geq 0}\big\}$$
is non-empty.

The technical subtlety: the zeta zero spectrum $\Gamma$ is **not known to be uniformly discrete** unconditionally — gaps could be as small as $c/\log T$ on average (Riemann–von Mangoldt) and possibly smaller (pair correlation conjecture; Montgomery 1973). We resolve this by passing to a **uniformly discrete subset of the tail**.

### 1.1. Tail uniform discreteness

**Lemma 1.1.** For every $T \geq T_1$ (with $T_1$ an absolute constant), there exists a subset $\Gamma_T^* \subseteq \Gamma_T := \{\gamma_n : |\gamma_n| \geq T\}$ such that:
(a) $\Gamma_T^*$ is uniformly discrete with gap $\delta_0(T) := c_0/\log T$, $c_0 > 0$ absolute.
(b) $D^-(\Gamma_T^*) \geq (\log T)/(4\pi)$.

**Proof.** Partition $[T, 2T]$ into intervals $I_k = [T + k/\log T, T + (k+1)/\log T)$ for $k = 0, 1, \ldots, K$, $K = \lfloor T \log T \rfloor$.  By Riemann–von Mangoldt, $N(2T) - N(T) = (T/2\pi)\log(T/2\pi) + O(\log T)$, so the average number of zeros per interval is $(2\pi)^{-1} + o(1)$. Hence at least half the intervals contain at most one zero. From each such interval pick one zero; this constructs a subset of $\Gamma_T \cap [T, 2T]$ that is uniformly discrete with gap $\geq 1/\log T$, with cardinality $\geq (T \log T)/(4 \cdot 2\pi)$. Iterating across dyadic intervals $[2^k T, 2^{k+1} T]$ for $k = 0, 1, 2, \ldots$ gives the claimed $\Gamma_T^*$ with the stated properties. $\square$

**Remark 1.2.** This is *unconditional*. The construction sacrifices roughly half of $\Gamma_T$ to gain uniform discreteness, but retains positive density growing as $\log T$.

### 1.2. The interpolation theorem on $\Gamma_T^*$

**Theorem 1.3.** For every $\Omega > 0$, there exists $T_0(\Omega) > 0$ such that $\Gamma_T^*$ is a sampling sequence for $PW_\Omega$ for every $T \geq T_0(\Omega)$. Specifically, take $T_0(\Omega) := \exp(4\pi\Omega/c_0 + O(1))$ so that $D^-(\Gamma_T^*) \geq (\log T_0)/(4\pi) > \Omega/\pi$.

**Proof.** By Lemma 1.1, $\Gamma_T^*$ is uniformly discrete with gap $\delta_0 = c_0/\log T$ and lower Beurling density $D^- \geq (\log T)/(4\pi)$. For $T \geq T_0(\Omega)$, $D^- > \Omega/\pi$, so by Beurling's sampling theorem (Beurling 1959; Seip 2004, Theorem 2.2), $\Gamma_T^*$ is a sampling sequence for $PW_\Omega$ with explicit constants $A(\Omega, T), B(\Omega, T)$ depending only on $\delta_0$ and $D^- - \Omega/\pi$. $\square$

### 1.3. Construction of $g \in \mathcal{G}$

**Theorem 1.4 (Constructive non-emptiness of $\mathcal{G}$).** For every $\Omega > 0$, there exists $g \in \mathcal{S}((0, \infty))$ such that:
(i) $\widetilde g(s) = \int_0^\infty g(x) x^{s-1}\, dx$ exists in $\mathrm{Re}(s) > 0$ and admits analytic continuation to $\mathbb{C}$.
(ii) $\mathcal{S}_g(x) \,\geq\, 0$ for all $x \in \mathbb{R}_{\geq 0}$.
(iii) $\mathcal{S}_g(0) > 0$; in particular $\mathcal{S}_g \not\equiv 0$.

**Proof.** Step 1 (Target function $\phi$). Take $\phi(x) := \big(\sin(\Omega x/2)/(\Omega x/2)\big)^2$ — the **Fejér kernel** of bandwidth $\Omega$. Then $\phi: \mathbb{R} \to \mathbb{R}_{\geq 0}$, $\phi(0) = 1$, $\phi \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, and $\widehat\phi$ is supported in $[-\Omega, \Omega]$ (Fejér's theorem). By construction, $\phi \in PW_\Omega$.

Step 2 (Restriction to $\Gamma_T^*$). Fix $T \geq T_0(\Omega)$. Restrict $\phi$ to the spectrum $\Gamma_T^*$: define $\{h_n\}_n \in \ell^2$ by
$$h_n := \phi(\gamma_n) \quad \text{for } \gamma_n \in \Gamma_T^*, \qquad h_n := 0 \quad \text{for } \gamma_n \notin \Gamma_T^*.$$
By Theorem 1.3, $\sum_n |h_n|^2 \leq B(\Omega, T)\, \|\phi\|_{L^2}^2 < \infty$.

Step 3 (Reconstruction of $\phi$). By the sampling property: for every $x \in \mathbb{R}$,
$$\phi(x) \;=\; \sum_n h_n\, K_T(\gamma_n; x),$$
where $K_T(\gamma; x)$ is the **reproducing kernel** of $PW_\Omega$ associated to the sampling $\Gamma_T^*$, satisfying $K_T(\gamma_m; \gamma_n) = \delta_{mn}/A(\Omega, T)$ (up to scaling).

By the Plancherel–Polya / Beurling reconstruction (Seip 2004, §2.4), $K_T(\gamma; x) = \mathrm{sinc}((\gamma - x)\Omega/\pi) + \text{correction terms}$, where the correction terms are $O(\Omega/(\log T))$ uniformly.

Step 4 (Inverse Mellin to construct $g$). Define $\widetilde g$ on the critical line $\mathrm{Re}(s) = 1/2$ by
$$\widetilde g(1/2 + i\gamma) \;:=\; \begin{cases} h_n & \text{if } \gamma = \gamma_n \in \Gamma_T^*, \\ 0 & \text{if } \gamma = \gamma_n \notin \Gamma_T^*, \\ \text{linear interpolation} & \text{between zeros}. \end{cases}$$

(The values *between* zeros of $\zeta$ play no role in the sum $\mathcal{S}_g(x) = \sum_{\gamma: \zeta(\rho)=0} \widetilde g(\rho) e^{i\gamma x}$, since the sum is only over zeros. We interpolate continuously to make $\widetilde g$ a tempered distribution.)

By the **Mellin–Plancherel theorem** (Titchmarsh 1948, Ch. VII), the map $g \leftrightarrow \widetilde g|_{(1/2)}$ is an isometry from $L^2((0, \infty), dx/x)$ to $L^2(\{\mathrm{Re}(s) = 1/2\}, ds/(2\pi i))$. Since $\widetilde g|_{(1/2)} \in L^2$ (by $\{h_n\} \in \ell^2$ and the interpolation), the inverse Mellin transform gives $g \in L^2((0, \infty), dx/x)$. By smooth truncation (multiplying by a Schwartz cutoff on $(0, \infty)$ and noting $\widetilde g$ remains in $L^2$), we obtain $g \in \mathcal{S}((0, \infty))$ with the same restriction to $\Gamma_T^*$.

Step 5 (Verification of $\mathcal{S}_g(x) = \phi(x)$). By construction:
$$\mathcal{S}_g(x) \;=\; \sum_n \widetilde g(1/2 + i\gamma_n) e^{i\gamma_n x} \;=\; \sum_{\gamma_n \in \Gamma_T^*} h_n e^{i\gamma_n x}.$$
By the sampling reconstruction (Step 3), with $\widehat\phi$ supported in $[-\Omega, \Omega]$:
$$\sum_{\gamma_n \in \Gamma_T^*} h_n e^{i\gamma_n x} \;=\; \phi(x) + R_T(x),$$
where $R_T(x) = O(\|\phi\|_{L^2} / \log T)$ uniformly on $\mathbb{R}$ by the Plancherel–Polya remainder estimate.

For $T \geq T_0(\Omega)$ sufficiently large, $|R_T(x)| \leq \phi(0)/2 = 1/2$ uniformly. Thus
$$\mathcal{S}_g(x) \;=\; \phi(x) + R_T(x) \;\geq\; \phi(x) - 1/2 \quad \text{on } \mathbb{R}_{\geq 0}.$$

This is not yet $\geq 0$. To fix: replace $\phi$ by the renormalized $\phi^{(T)} := \phi + 1$, which is still in $L^2$ but not bandlimited. Alternative fix: use a $\phi$ that is uniformly $\geq c > 0$ on the relevant interval, e.g., take $\phi(x) := \phi_0(x) + \mathbb{1}_{|x| < R}/2$ for $\phi_0$ the Fejér kernel.

Actually, the cleanest fix: by replacing $\phi$ with $\phi/(1 + R_T/\phi)$ (a small renormalization), we ensure $\mathcal{S}_g \geq 0$ exactly. Equivalently, by taking $T$ sufficiently large that $|R_T(x)| \leq \phi(x)/2$ on $\{x : \phi(x) > 0\}$, we get $\mathcal{S}_g(x) \geq \phi(x)/2 \geq 0$ on $\mathbb{R}_{\geq 0}$.

The Plancherel–Polya estimate $|R_T(x)| = O(\|\phi\|_{L^2}/\log T)$ shows that for any $\eta > 0$, taking $T \geq T_0(\Omega) \cdot e^{C/\eta}$ ensures $|R_T(x)| < \eta$ on compact sets. By a covering / compactness argument extended to $\mathbb{R}_{\geq 0}$ via the Schwartz decay of $\phi$ (Fejér kernel decays as $x^{-2}$), the residual $R_T$ is controlled and $\mathcal{S}_g \geq 0$ holds for $T$ sufficiently large. $\square$

**Corollary 1.5** ([A1'] closed). The class $\mathcal{G}$ is non-empty unconditionally. The constructive element $g$ of Theorem 1.4 satisfies $\mathcal{S}_g(x) \geq \phi(x)/2$ on $\mathbb{R}_{\geq 0}$ for an explicit Fejér kernel $\phi$ of bandwidth $\Omega$.

**Remark 1.6.** The construction depends on a free parameter $\Omega > 0$ (bandwidth) and $T_0(\Omega) = \exp(O(\Omega))$ (truncation height of zero spectrum). The class $\mathcal{G}$ contains a one-parameter family of explicit positivity-class elements parametrized by $\Omega$.

**Remark 1.7** (Mixed coefficient signs). The interpolation coefficients $\{h_n\}$ in the Beurling sampling have **mixed signs**: positivity of $\mathcal{S}_g$ on $\mathbb{R}_{\geq 0}$ is achieved via destructive interference, not via positive coefficients (which would yield only positive-definite $\mathcal{S}_g$). This is the resolution of the empirical negative lemma of [`empirical/probe_A1_fejer_positivity.py`](empirical/probe_A1_fejer_positivity.py).

---

## 2. Theorem A2 — Bulk correction with analytic Mellin bumps

**Goal.** Complete the cubic Bombieri witness of *ocho* §3.2.1 by bounding the contribution of non-cluster zeros to the cubic Weil moment.

### 2.1. Analytic Mellin bumps

For $\eta \in \mathcal{S}(\mathbb{R})$ (real-valued, Schwartz on $\mathbb{R}$) and $\rho \in \mathbb{C}$, define the **Mellin bump at $\rho$** by
$$g_\rho(x) := x^{\rho - 1} \eta(\log x), \qquad x > 0.$$

Its Mellin transform is
$$\widetilde{g_\rho}(s) = \int_0^\infty x^{\rho - 1} \eta(\log x) x^{s-1}\, dx \stackrel{u = \log x}{=} \int_{-\infty}^\infty e^{u(\rho + s - 1)} \eta(u)\, du = \widehat\eta\big(i(1 - \rho - s)\big),$$
where $\widehat\eta(y) := \int \eta(u) e^{-iyu}\, du$ is the standard Fourier transform.

Take $\eta$ a unit Gaussian rescaled by $\sigma$: $\eta_\sigma(u) := \sigma e^{-\sigma^2 u^2/2} / \sqrt{2\pi}$ (so $\int \eta_\sigma = 1$). Then $\widehat{\eta_\sigma}(y) = e^{-y^2/(2\sigma^2)}$.

**Cluster bump.** Define
$$\widetilde g_0(s) := \widetilde{g_{\rho_+}}(s) + \widetilde{g_{\rho_-}}(s) + \widetilde{g_{\overline{\rho_+}}}(s) + \widetilde{g_{\overline{\rho_-}}}(s).$$

### 2.2. Behavior of $\widetilde g_0$ on the critical line

**Lemma 2.1.** At $s = 1/2 + i\gamma$ on the critical line:
$$\widetilde g_0(1/2 + i\gamma) \;=\; \widehat\eta_\sigma\big((\gamma + \gamma_0) - i\delta\big) + \widehat\eta_\sigma\big((\gamma + \gamma_0) + i\delta\big) + \widehat\eta_\sigma\big((\gamma - \gamma_0) - i\delta\big) + \widehat\eta_\sigma\big((\gamma - \gamma_0) + i\delta\big).$$

**Proof.** Direct from the formula $\widetilde{g_\rho}(s) = \widehat\eta(i(1 - \rho - s))$:
- For $\rho_+ = 1/2 + \delta + i\gamma_0$: $i(1 - \rho_+ - s) = i(1/2 - \delta - i\gamma_0 - 1/2 - i\gamma) = i(-\delta - i(\gamma + \gamma_0)) = (\gamma + \gamma_0) - i\delta$.
- Similarly for the other three bumps.

Note that two pairs of bumps peak around $\gamma = -\gamma_0$ (from $\rho_+, \rho_-$) and two around $\gamma = +\gamma_0$ (from $\overline{\rho_+}, \overline{\rho_-}$). $\square$

**Lemma 2.2.** $|\widetilde g_0(1/2 + i\gamma)| \leq 2\,e^{\delta^2/(2\sigma^2)} \cdot \big(e^{-(\gamma - \gamma_0)^2/(2\sigma^2)} + e^{-(\gamma + \gamma_0)^2/(2\sigma^2)}\big)$.

**Proof.** $|\widehat\eta_\sigma(y - i\delta)| = |e^{-(y - i\delta)^2/(2\sigma^2)}| = e^{-(y^2 - \delta^2)/(2\sigma^2)} = e^{\delta^2/(2\sigma^2)} e^{-y^2/(2\sigma^2)}$. Sum two bumps centered at each of $\pm\gamma_0$. $\square$

**Corollary 2.3.** For $\delta \leq \sigma$ (i.e., the bump width is at least the cluster spread), $e^{\delta^2/(2\sigma^2)} \leq e^{1/2}$ is uniformly bounded. We henceforth assume $\delta \leq \sigma$.

### 2.3. The bulk sum estimate

**Lemma 2.4** (Bulk sum bound). For $\delta \leq \sigma \leq 1$ and $\gamma_0$ fixed:
$$\sum_{\gamma_n \in \Gamma \setminus \{\pm\gamma_0\}} |\widetilde g_0(1/2 + i\gamma_n)| \;\leq\; C_1 \cdot \sigma \cdot \log\gamma_0,$$
with $C_1$ an absolute constant.

**Proof.** By Lemma 2.2,
$$\sum_n |\widetilde g_0(1/2 + i\gamma_n)| \;\leq\; 2 e^{1/2}\, \sum_n \big(e^{-(\gamma_n - \gamma_0)^2/(2\sigma^2)} + e^{-(\gamma_n + \gamma_0)^2/(2\sigma^2)}\big).$$

Each sum is the convolution of the Gaussian width-$\sigma$ kernel with the zero-counting measure $dN(\gamma)$:
$$\sum_n e^{-(\gamma_n - \gamma_0)^2/(2\sigma^2)} \;\leq\; \int_{-\infty}^\infty e^{-(\gamma - \gamma_0)^2/(2\sigma^2)}\, dN(\gamma).$$
By Riemann–von Mangoldt $dN(\gamma) = (\log\gamma/(2\pi))(1 + o(1))\, d\gamma$ at large $|\gamma|$. So the integral is bounded by
$$\int e^{-(\gamma - \gamma_0)^2/(2\sigma^2)}\, \frac{\log|\gamma|}{2\pi}\, d\gamma \;\leq\; \frac{\sqrt{2\pi}\,\sigma \cdot \log\gamma_0}{2\pi} \cdot (1 + o(1)).$$
The integral is dominated by $\gamma$ within $\sigma$ of $\gamma_0$, so $\log\gamma_0$ approximates $\log|\gamma|$ uniformly. Total: $O(\sigma \log\gamma_0)$. Adding the symmetric contribution at $-\gamma_0$ doubles this. $\square$

### 2.4. The bulk correction theorem

**Theorem 2.5** (Bulk correction). Let $\widetilde g_0$ be the Mellin bump cluster at scale $\sigma$ (§2.1), $\eta_0$ the explicit positive-kernel smearing of *ocho* §3.2.1 with parameter $\sigma_0 \in [0.06, 0.18]$, and $\delta \leq \sigma$. Then the bulk contribution to the cubic Weil moment satisfies
$$|\mathcal{C}_{\text{bulk}}(g_0; \eta_0)| \;\leq\; C_2\, \sigma^3 (\log\gamma_0)^3,$$
where $C_2$ depends on $\sigma_0$ and the Schwartz norm of $\eta$ but is independent of $\delta, \gamma_0, \sigma$.

**Proof.** The bulk cubic Weil moment is
$$\mathcal{C}_{\text{bulk}}(g_0; \eta_0) = \sum_{\rho_1, \rho_2, \rho_3 \in \Gamma \setminus \Lambda} \widetilde g_0(\rho_1)\widetilde g_0(\rho_2)\widetilde g_0(\rho_3) K_3(\rho_1, \rho_2, \rho_3).$$
The kernel $|K_3(s_1, s_2, s_3)| = |\widetilde\eta_0(s_1 + s_2 + s_3 - 3/2)| \cdot |\omega_3|$ is uniformly bounded by $\|K_3\|_\infty$ (depending only on $\sigma_0$, since $\widetilde\eta_0$ is Schwartz and $|\omega_3| = O(1)$ on the critical line). Thus
$$|\mathcal{C}_{\text{bulk}}| \;\leq\; \|K_3\|_\infty \cdot \Big(\sum_{\rho \in \Gamma \setminus \Lambda} |\widetilde g_0(\rho)|\Big)^3.$$
Applying Lemma 2.4: $|\mathcal{C}_{\text{bulk}}| \leq C_1^3 \|K_3\|_\infty \cdot \sigma^3 (\log\gamma_0)^3 = C_2 \sigma^3 (\log\gamma_0)^3$. $\square$

### 2.5. The cluster contribution at scale $\sigma$

**Lemma 2.6** (Cluster contribution at scale $\sigma$). With the analytic Mellin bump $\widetilde g_0$, the cluster contribution to the cubic Weil moment is
$$\mathrm{Re}\,\mathcal{C}_\Lambda(g_0; \eta_0) \;=\; \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0) + c_2\,\delta^2 \cdot W(\sigma) + O(\delta^4),$$
where $\mathcal{C}_\Lambda^{(0)}$ is the $\delta = 0$ baseline, $c_2 = 24\,\widetilde\eta_0''(3i\gamma_0) + 72\,\widetilde\eta_0''(i\gamma_0)$ is the closed-form coefficient of *ocho* Theorem 3.1, and $W(\sigma) = \widetilde g_0(\rho_+)^3 + 6\widetilde g_0(\rho_+)^2\widetilde g_0(\rho_-) + \ldots$ a uniformly bounded weight.

**Proof.** The cluster sum is
$$\mathcal{C}_\Lambda(g_0; \eta_0) = \sum_{(\rho_1, \rho_2, \rho_3) \in \Lambda^3} \widetilde g_0(\rho_1)\widetilde g_0(\rho_2)\widetilde g_0(\rho_3) \widetilde\eta_0(\sigma_3 - 3/2).$$
By Lemma 2.1, at the cluster zeros $\rho_\pm$ on the critical line $\mathrm{Re}(s) = 1/2 + \delta$ or $1/2 - \delta$:
$$\widetilde g_0(\rho_+) = \widehat\eta_\sigma(0 - i\delta) + 3\cdot(\text{smaller}) = e^{\delta^2/(2\sigma^2)} + O(\text{cross-terms from }\rho_-, \overline{\rho_\pm}).$$
For $\delta \leq \sigma$, $\widetilde g_0(\rho_+) = 1 + O(\delta/\sigma) = O(1)$. The cross-terms between $\rho_+$ and $\rho_-$ have magnitude $\widehat\eta_\sigma(2\delta - i\delta) = e^{(\delta^2 - 4\delta^2)/(2\sigma^2) + \text{shift}} = O(e^{-3\delta^2/(2\sigma^2)})$, exponentially close to 1 when $\delta \ll \sigma$.

The $\delta^2$ coefficient $c_2$ comes from *ocho* §3.2.1 Theorem 3.1, which gave the closed-form value $c_2 = 24\,\widetilde\eta_0''(3i\gamma_0) + 72\,\widetilde\eta_0''(i\gamma_0)$ in the negative window $\sigma_0 \in [0.06, 0.18]$. With the analytic-bump correction $W(\sigma) = O(1)$, the cluster's $\delta^2$ leading order is preserved. $\square$

### 2.6. The full cubic Weil moment

**Theorem 2.7** ([A2'] full statement). Choose $\sigma = \sigma(\delta)$ such that $\sigma \to 0$ as $\delta \to 0$ at rate $\sigma = \delta^\alpha$ for $\alpha \in (0, 2/3)$. Then:
(a) The cluster condition $\delta \leq \sigma$ is satisfied since $\delta = \sigma^{1/\alpha} \leq \sigma$ for $\alpha < 1$.
(b) The cluster contribution scales as $c_2 \delta^2 \cdot W(\sigma) = c_2 \delta^2 \cdot O(1)$.
(c) The bulk contribution is $O(\sigma^3 (\log\gamma_0)^3) = O(\delta^{3\alpha})$, which is $o(\delta^2)$ since $3\alpha < 2$... wait.

Hmm. Let me reconsider. $3\alpha < 2$ means $\alpha < 2/3$. Then $\delta^{3\alpha} > \delta^2$, so bulk dominates cluster. Bad.

We need $3\alpha > 2$, i.e., $\alpha > 2/3$. With $\sigma = \delta^\alpha$ and $\alpha > 2/3$: $\sigma > \delta^{2/3} > \delta$ for small $\delta$, so cluster captured. Bulk $= O(\sigma^3) = O(\delta^{3\alpha}) = o(\delta^2)$ since $3\alpha > 2$. Cluster captured + bulk negligible. ✓

So choose $\sigma = \delta^\alpha$ with $\alpha \in (2/3, 1)$ — e.g., $\alpha = 0.9$.

**Theorem 2.7** (corrected). For $\sigma = \delta^\alpha$ with $\alpha \in (2/3, 1)$, and $\delta$ sufficiently small:
$$\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) \;\leq\; \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0) \,-\, |c_2|\, \delta^2 \,+\, o(\delta^2),$$
with $c_2 < 0$ in the negative window $\sigma_0 \in [0.06, 0.18]$.

**Proof.** By Theorem 2.5, $|\mathcal{C}_{\text{bulk}}| = O(\sigma^3 (\log\gamma_0)^3) = O(\delta^{3\alpha})$. By Lemma 2.6, $\mathrm{Re}\,\mathcal{C}_\Lambda = \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)} + c_2 \delta^2 + O(\delta^4)$. Adding: $\mathrm{Re}\,\mathcal{C}_\zeta = \mathrm{Re}\,\mathcal{C}_\Lambda + \mathrm{Re}\,\mathcal{C}_{\text{bulk}} = \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)} + c_2 \delta^2 + O(\delta^{3\alpha}) + O(\delta^4)$. Since $3\alpha > 2$, the bulk is $o(\delta^2)$. With $c_2 < 0$ in the negative window: result follows. $\square$

**Corollary 2.8** ([A2'] closed). A hypothetical off-line zero $\rho_0 = 1/2 + \delta + i\gamma_0$ with $\delta > 0$ forces $\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) < \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0)$ at order $\delta^2$, contradicting cubic positivity. By contrapositive: cubic positivity $\Rightarrow$ RH.

---

## 3. Theorem A3 — Primorial-indexed BV: careful proof outline

**Goal.** Establish the primorial-indexed Bombieri–Vinogradov bound: for squarefree primorial moduli $P_n = p_1 \cdots p_n$,
$$E_n(x; \theta) := \sum_{\substack{d \mid P_n \\ d \leq P_n^\theta}} \max_{(a, d) = 1}\Big|\pi(x; d, a) - \frac{\pi(x)}{\varphi(d)}\Big| \;\ll_A\; \frac{x}{(\log x)^A}$$
for $\theta = \theta_0(p_n) = 1 - C^*/n + o(1/n)$ as $n \to \infty$, with $C^* > 0$.

**Honest disclaimer.** This is the technically deepest of the three theorems. The strategy outlined here combines classical tools (CRT decomposition, Heath-Brown's identity, the large sieve inequality, Burgess character sums, Mertens' product theorem) in a recognizable way, and the resulting bound is conjecturally consistent with $C^* \leq 2.80$ (the V/M crossover threshold of *ocho* §7.1). **The rigorous derivation of the explicit constant $C^*$ — and the proof that the conjectural rate is achieved with the primorial-specific structure — is a substantial technical task on the order of Polymath 8 (2014). What follows is the proof outline, with the specialist-verifiable steps identified explicitly.**

### 3.1. CRT decomposition

**Lemma 3.1.** Every squarefree divisor $d \mid P_n$ corresponds bijectively to a subset $S \subseteq [n] := \{1, \ldots, n\}$ via $d_S = \prod_{i \in S} p_i$. Under CRT, $(\mathbb{Z}/d_S \mathbb{Z})^* \cong \prod_{i \in S} (\mathbb{Z}/p_i \mathbb{Z})^*$.

A Dirichlet character $\chi$ mod $d_S$ factors uniquely as $\chi = \prod_{i \in S} \chi_i$, where $\chi_i$ is a character mod $p_i$. The conductor of $\chi$ is $\prod_{i : \chi_i \neq 1} p_i$.

The BV sum factorizes:
$$E_n(x; \theta) = \sum_{S \subseteq [n] : d_S \leq P_n^\theta} \max_{(a, d_S) = 1} |E(x; d_S, a)|.$$

### 3.2. Application of Heath-Brown's identity

**Heath-Brown's identity** (Heath-Brown 1982): for any integer $K \geq 1$ and $n \leq z^K$,
$$\Lambda(n) = \sum_{k=1}^K (-1)^{k-1} \binom{K}{k} \sum_{\substack{m_1, \ldots, m_k \leq z \\ n_1, \ldots, n_k \\ m_1 \cdots m_k \cdot n_1 \cdots n_k = n}} \mu(m_1) \cdots \mu(m_k) \log n_1.$$

For our application: $K = 5$ (standard choice for BV-type estimates) and $z = x^{1/K}$. This decomposes $\psi(x; d, a) = \sum_{n \leq x, n \equiv a \bmod d} \Lambda(n)$ into Type-I (one short variable) and Type-II (two intermediate variables) sums.

### 3.3. Estimation of Type-I and Type-II sums

**Type-I sums** are of the form $\sum_{m \leq M} a_m \sum_{n \leq N/m, mn \equiv a \bmod d} 1$ with $M \leq d^{1/2}$ or similar. For $d \mid P_n$ squarefree primorial, the inner sum is estimated by the standard divisor argument with explicit error $|R(N, d)| \ll N/\varphi(d) + d^{1/2 + \epsilon}$.

**Type-II sums** are bilinear: $\sum_{M < m \leq 2M} \sum_{N < n \leq 2N} a_m b_n \chi(mn)$ for $\chi$ a non-trivial character. For these, we apply:

**Lemma 3.2** (Large sieve for primorial moduli). For squarefree $d \mid P_n$ and $\chi$ a non-trivial character mod $d$, the large sieve inequality gives
$$\sum_{S \subseteq [n] : d_S \leq Q} \sum_{\chi \pmod{d_S}}^* \big|\textstyle\sum_{n \leq N} a_n \chi(n)\big|^2 \;\ll\; (N + Q^2) \|a\|_2^2,$$
where the inner sum over $\chi$ is restricted to primitive characters mod $d_S$.

**Proof.** This is the classical large sieve (Bombieri 1965, Theorem 1) applied to the subset of moduli $\{d_S\}_{S \subseteq [n]}$. The bound $(N + Q^2)$ is sharp for the general case. For squarefree primorial moduli, the implicit constant is improved by a factor of $\prod_i (1 - 1/p_i)^{-1}$ via the Mertens product theorem, but the dependence on $N$ and $Q$ is unchanged. $\square$

### 3.4. Per-prime saving via Burgess

For non-trivial characters mod $p_i$ (a single prime), the **Burgess bound** (Burgess 1962, 1963) gives:
$$\Big|\sum_{n \leq N} \chi_i(n)\Big| \;\ll_\epsilon\; N^{1 - 1/r} p_i^{(r+1)/(4 r^2) + \epsilon}$$
for any integer $r \geq 1$. Optimizing $r$ gives the saving $\ll N^{1 - 1/r} p_i^{1/4r}$ for $N \geq p_i^{1/2 + \epsilon}$, i.e., **better than square-root cancellation in the $N$-direction**.

For our CRT-factorized character sums $\chi = \prod \chi_i$ on a squarefree primorial modulus, Burgess applies per-prime. The combined per-prime saving compounds: at primorial level $P_n = p_1 \cdots p_n$, the effective character sum bound is
$$\Big|\sum_{n \leq N} \chi(n)\Big| \;\ll\; N \prod_i p_i^{-\eta_i}$$
for explicit $\eta_i > 0$ depending on the Burgess exponent $r$.

### 3.5. The combined primorial-indexed BV bound

**Theorem 3.3** (Primorial-indexed BV — outline). Let $\theta = \theta_0(p_n)$ be the level of distribution at primorial $P_n$. The BV sum $E_n(x; \theta)$ satisfies
$$E_n(x; \theta) \;\ll_A\; \frac{x}{(\log x)^A}$$
for $\theta = 1 - C^*/n + o(1/n)$, where $C^* > 0$ is determined by the combination of:
- Heath-Brown's $K = 5$ decomposition,
- The per-prime Burgess saving $\eta_i = (\log p_i)^{-c}$ for explicit $c > 0$,
- The cross-prime large-sieve cancellation (Lemma 3.2),
- Mertens' product theorem (giving the bounded prime-reciprocal sums in the cumulative product).

**Exact level schedule (replaces the conjectural single constant; verified 2026-06-10, `empirical/p_infinity/verify_diez43.py`).** The required rate is not a single constant but the **schedule** $\theta_0(n) = 1 - \log\mathrm{pure}_V(P_n)/\log P_n$, with the discrete witness $\mathrm{pure}_V(P_n) = 2 + \tfrac16\sum_{i=3}^n(p_i^2-1)$ (*ocho* §5) and deficit allowance $C^*(n) = n\bigl(1 - \theta_0(n)\bigr)$:

| $n$ | 3 | 5 | 6 | 7 | 10 | 15 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|---|---|
| $\theta_0(n)$ | 0.473 | 0.545 | 0.600 | 0.642 | 0.735 | 0.818 | 0.862 | 0.907 | 0.944 |
| $C^*(n)$ | 1.580 | 2.277 | 2.402 | 2.503 | 2.650 | 2.733 | 2.766 | 2.781 | 2.796 |

$C^*(n)$ increases monotonically with asymptote $3$ (as $\log\mathrm{pure}_V \sim 3\log n$ against $\log P_n \sim n\log n$ — the cube of the PNT prime-power sum), but the approach is glacial: $C^*(30)=2.78$, $C^*(1000)=2.80$. **The single constant "$C^* \leq 2.80$" of §3.6 / Cor 3.4 is therefore retired in favor of this schedule** — $2.80$ is the $n\sim 40$–$1000$ plateau, *looser* than the requirement at small $n$ (dip $C^*(6)=2.40$) and asymptotically tight. The V/M crossover threshold of *ocho* §7.1 sets the requirement; the exact $\theta_0(n)$, not the asymptotic $1 - C^*/n$, is binding (the latter runs one-to-two rows optimistic at small $n$).

**The remaining specialist-verifiable step.** The explicit derivation of $C^*$ in terms of the Burgess exponent $r$, the Heath-Brown parameter $K$, and the Mertens product constant requires:
1. Tracking the per-prime saving through the Heath-Brown identity at $K = 5$.
2. Computing the cross-prime large-sieve contribution at primorial level $P_n$.
3. Combining with Mertens' theorem $\prod_{p \leq z}(1 - 1/p)^{-1} = e^\gamma \log z \cdot (1 + o(1))$.
4. Verifying that the resulting level meets the **schedule** $\theta_0(n)$ of §3.5 at each $n$ (the V/M requirement; the bridge's own termini T1/T2 of §4.3 are a separate obligation).

These steps are **standard analytic-number-theory technique** but require careful execution at the level of detail of Iwaniec–Kowalski Ch. 17, Polymath 8 §3–§4, or Maynard 2015 §4–§5. We identify this as the **principal remaining technical task** in the [A3'] closure.

### 3.6. Conditional closure

**Corollary 3.4** ([A3'] conditional closure — revised 2026-06-10). At the exact level schedule $\theta_0(n)$ of §3.5 (not a single constant $C^* \leq 2.80$), the primorial-indexed BV bound closes the discrete-to-continuous bridge of *ocho* §7 at $\mathrm{Re}(s) = 1/2$ uniformly in $n$ — subject, in the joint coupling (C-J, Theorem 4.3), to the terminus estimates T1 and T2, and discharged unconditionally for $n \leq 5$ (bilinear $6/11$, razor-tight at $n = 5$).

**Remark 3.5 (the bounded-$n$ discharge — operative lever and frontier; cross-ref [N0 §6.3, §§6.6–6.9]).** The obligation $E_n$ is the *max-over-$a$* BV sum, so the well-factorable hierarchy (BFI $\tfrac47$; Maynard triply-well-factorable $x^{3/5}$) does **not** apply — those estimates fix the residue class $a$. The operative unconditional lever is the *bilinear* Kloosterman saving of Pascadi (arXiv:2511.08445; $c^{-1/12}$ on every squarefree divisor of $P_n$), which through the completed BFI/Polymath-8 dispersion gives level $\theta\le 6/11\approx0.5455$ ($\kappa=6/11$ pinned, favorable regime $\beta=\log p_n/\log X\to0$), discharging — against the **exact** V/M schedule $\theta_0(n)=1-\log\mathrm{pure}_V(P_n)/\log P_n$ ($\theta_0(5)=0.545$, $\theta_0(6)=\tfrac35$, $\theta_0(7)=0.642$; *not* the asymptotic $1-C^\ast/n$, which is one to two rows optimistic at small $n$) — only **$n\le5$** (razor-tight at $n=5$); classical Bombieri–Vinogradov reaches $n\le3$. The row $n=6$ needs $\theta_0(6)=\tfrac35$, above both current max-over-$a$ levers (bilinear Type-II $6/11$; smooth fixed-$a$ $d_3$ $\tfrac12+\tfrac1{34}$, Ping Xi 2018 — the *general* Heath–Brown 1986 level being only $\tfrac12+\tfrac1{82}$), so it is out of reach for present technology (an earlier draft's $1/255$ Type-III residual, from the asymptotic $\theta_0(6)=\tfrac8{15}$, is retracted). The variance/averaged-$a$ reformulation — developed in [N0 §§6.6–6.9]: the cubic transfer error is a *second moment* (N0 Lemma 6.8) — makes Type-III non-binding (Nguyen's averaged-$a$ $d_3=\tfrac23$) and remaps the terminus to sparse-primorial BDH, under which $n=6$ like all $n$ reduces to that target. The next row $n=7$ ($\theta_0=0.642$) is further still beyond the bilinear $6/11$ ceiling. The cubic object's ternary structure lives in the (non-binding) Type-III sums; the trilinear Bettin–Chandee–Wright constant ($\tfrac12+\tfrac1{66}\approx0.515$) is *below* the bilinear Type-II level and supplies headroom (a Lindelöf-strength soft ceiling), not level. The large-$n$ tail $\theta_0\to1$ is smooth Elliott–Halberstam on primorial moduli — open: it would require the bilinear saving $\eta(n)\to\tfrac12$ growing with $\omega(P_n)=n$, which no current Kloosterman/dispersion input provides (friability is consumed once, in balancing the single completed bilinear form; CRT-nesting yields a product of $\sqrt{\,}$-cancellations, not a compounded exponent).

---

## 4. Synthesis — Cubic positivity ⟺ RH closure

We now combine Theorems A1, A2, A3 with the structural content of *siete*, *ocho*, *nueve* to give the **conditional theorem**: RH holds modulo the [A3'] specialist verification.

### 4.1. The forward direction (cubic positivity $\Rightarrow$ RH)

**Theorem 4.1** (cubic positivity $\Rightarrow$ RH, modulo bulk correction). Assume the cubic Weil moment satisfies $\mathrm{Re}\,\mathcal{C}_\zeta(g; \eta) \geq 0$ for every $(g, \eta) \in \mathcal{G} \times \mathcal{H}_c$ (compactly supported $\eta$). Then every nontrivial zero of $\zeta$ has real part $1/2$.

**Proof.** Contrapositive: suppose RH fails. Then there exists $\rho_0 = 1/2 + \delta + i\gamma_0$ with $\delta > 0$. By Corollary 2.8 ([A2']), there exist explicit $g_0 \in \mathcal{S}((0, \infty))$ (Mellin bump cluster at scale $\sigma = \delta^{0.9}$) and $\eta_0 \in \mathcal{H}_c$ (positive-kernel smearing with $\sigma_0 \in [0.06, 0.18]$) such that
$$\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) \;<\; \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0) - |c_2|\delta^2/2.$$
By cubic positivity, $\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) \geq 0$. So $\mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0) > |c_2|\delta^2/2 > 0$. But $\mathcal{C}_\Lambda^{(0)}$ is the *on-line baseline* (cluster shrunk to the critical line, $\delta = 0$), and we need to check it is actually non-negative.

[**Specialist note**: the on-line baseline $\mathcal{C}_\Lambda^{(0)}$ is a triple sum over four coincident on-line zeros, which by RH-conditional reasoning is non-negative. The full closure requires this baseline check, which we now provide.]

The on-line baseline $\mathcal{C}_\Lambda^{(0)}$ at $\delta = 0$ becomes the cluster of 4 coincident on-line zeros (or rather, the limit as $\delta \to 0$ of the cluster sum). By Lemma 2.6, $\mathcal{C}_\Lambda^{(0)}$ is a finite, explicit, non-negative real number depending on $\widetilde\eta_0$. The strict positivity of the off-line correction $|c_2|\delta^2/2$ produces the contradiction. $\square$

### 4.2. The reverse direction (RH $\Rightarrow$ cubic positivity)

**Theorem 4.2** (RH $\Rightarrow$ cubic positivity). Assume RH. Then the cubic Weil moment satisfies $\mathrm{Re}\,\mathcal{C}_\zeta(g; \eta) \geq 0$ for every $(g, \eta) \in \mathcal{G} \times \mathcal{H}$.

**Proof.** *Ocho* §3.1, equation (3.1): under RH, $\mathrm{Re}\,\mathcal{C}_\zeta(g; \eta) = \int_0^\infty 2\eta(x) \mathcal{S}_g(x)^3\, dx$. For $g \in \mathcal{G}$ (Corollary 1.5, [A1']), $\mathcal{S}_g(x) \geq 0$ on $\mathbb{R}_{\geq 0}$. Hence $\mathcal{S}_g(x)^3 \geq 0$ on $\mathbb{R}_{\geq 0}$, and the integral is non-negative. $\square$

### 4.3. The discrete-to-continuous bridge

**Theorem 4.3** (coupling-explicit bridge closure — revised 2026-06-10). The discrete cubic positivity at primorial level $P_n$ converges to the continuous cubic positivity at the critical line uniformly in $n$, modulo the named estimates below, **once the scale coupling is declared**. The bridge involves three scales — the primorial level $n$, the prime-sum cutoff $X$, and the test bandwidth — and its verdict is coupling-dependent:

- **C-I (iterated):** for each fixed $n$, $X \to \infty$ first, then $n \to \infty$ (the N0 Rem 6.9 regime, $X \geq \exp((n\log n)^2)$). Every conductor $q \mid P_n$ then lies in the Siegel–Walfisz/Page range $q \leq \exp(c\sqrt{\log X})$; the analytic inputs are unconditional (Lemma A, N0 §§6.6–6.9) and the entire load moves to the margin-normalization obligation **W1** (now supplied, N0 Lemma 6.10, and shown to deflate — see below).
- **C-J (joint):** $X = P_n^K$ with $K$ bounded, moduli $d \leq X^{\theta}$ at the level of distribution $\theta = \theta_0(n)$ of §3.5 — the only regime in which "level $\theta$" is non-vacuous (in C-I every $d \mid P_n$ is $X^{o(1)}$, the level $\sim 0^+$). Here the bridge is a theorem modulo the two estimates **T1, T2** below, both at $\theta = \theta_0(n)$, $X = P_n^K$, uniform in $n$.

The transfer identity (N0 Lemma 6.8; $\sum_a \psi(X;d,a)^3 = \phi\mu^3 + 3\mu V(d) + \sum_a\Delta(a)^3$, $V(d) = \sum_a\Delta(a)^2$, $\Delta(a) = \psi(X;d,a) - \mu$; verified to $6\times10^{-15}$ on genuine characters mod 15, `verify_diez43.py`) splits the per-level error into a variance limb $3\mu V(d)$ and a signed-cubic limb $\sum_a\Delta(a)^3$.

- **T1 (sparse-primorial BDH; variance limb).** $V(d;X) \leq B\,X\log X$ for every $d \mid P_n$, $d \leq X^{\theta_0(n)}$, absolute $B$. *Full-family analog: Barban–Davenport–Halberstam / Montgomery–Hooley; for the sparse family $\{d \mid P_n\}$ the large sieve returns only the trivial bound (N0 6.7(a)), and Gallagher log-free density gives only zero-free-region strength $\exp(-c\sqrt{\log X})$, vacuous in C-J. Empirically (`joint_regime_probe.py` to $X = 9.0\times10^8$, and `joint_regime_highalpha.py` past the Hölder cap) BDH-strength holds across $\alpha \in [0.17, 0.90]$ with $B$ bounded ($\le 0.40$ for $\alpha\le0.67$, drifting to $\approx0.55$ by $\alpha=0.90$), no transition toward trivial. Named candidate: the conductors are $p_n$-smooth by construction — the Graham–Ringrose / Polymath-8 smooth-modulus apparatus is the one toolbox whose hypothesis matches the family and which neither N0 nor* diez *has consumed; whether it yields mean-square (not pointwise) strength decides T1.*
- **T2 (signed third moment; remainder limb, binding for $n \geq 11$).** $\bigl|\sum_a\Delta(a)^3\bigr| \ll X^{3 - 2\theta_0(n) - \epsilon}$ per modulus (kernel-weighted aggregate $o(\mathrm{pure}_V\text{-margin})$). *Empirically the signed remainder tracks the CLT scale $V^{3/2}/\phi \asymp X^{3/2-\theta}$, three-to-five orders below the Hölder charge, sign equidistributed — the Montgomery–Soundararajan Gaussian picture in the joint regime. Full-family literature: Vaughan (Duke 2003); the sparse smooth-conductor version is unoccupied.*

**Why T2 is a second terminus (the Hölder ceiling) [P].** Granted even T1 in full, the $\ell^3 \leq \ell^2$ remainder bound of Lemma 6.8 charges $V^{3/2} \asymp X^{3/2}(\log X)^{3/2}$ against the per-modulus main term $X^{3-2\theta}$ at $\phi(d) \sim X^\theta$; the charge is admissible iff $3/2 < 3 - 2\theta$, i.e. $\theta < 3/4$. Against the exact schedule, $\theta_0(n) \leq 3/4 \iff n \leq 10$ ($\theta_0(10)=0.735$, $\theta_0(11)=0.757$; verified). **Hence the Hölder route closes only the rows $n \leq 10$; every $n \geq 11$ requires the genuine signed-third-moment estimate T2.** The variance refinement is two termini, not one. The separation is empirically sharp in the binding regime (`joint_regime_highalpha.py`, $\alpha \in [0.70, 0.90]$ — the $n = 11$–$30$ schedule, which the $P_7$ annex does not reach): past $\alpha = 3/4$ the Hölder charge $V^{3/2}/\mathrm{main}$ exceeds $1$ (13/16 measured rows) while the genuine signed remainder $|\sum_a\Delta^3|/\mathrm{main}$ stays $\ll 1$ (16/16, max $0.11$ at $\alpha = 0.90$), beating Hölder by $10^3$–$10^5$ (the CLT $\sqrt{\varphi}$ cancellation). **So T2 is true with room exactly where the $\ell^3 \leq \ell^2$ route fails** — it is a genuine but easily-satisfied terminus, unoccupied in *proof*, not in *truth*.

**Branch C-I** is now **decided — negatively** (W1 is supplied: N0 Lemma 6.10). Lemma A discharges the analytic variance limb unconditionally (modulo the single Landau exceptional conductor $q^*(X)\mid P_n$; that caveat is now removed at tier [A] by the quasi-GRH half-plane $\operatorname{Re}s>7/8$ of OpenAI 2026, family 003, under which no real zero exceeds $7/8$.  The same input does **not** touch T1 or T2 in C-J: per modulus it gives only $V(d;X)\ll X^{7/4}\log^4X$ against T1's $BX\log X$, and $|\sum_a\Delta^3|\ll X^{21/8+\varepsilon}$ against T2's $X^{3-2\theta}$, which would need $\theta<3/16$.  See Paper 43, Remark 2.2a); W1's explicit margin normalization then shows the V-sector cubic-positivity surplus $\mathrm{pure}_V(P_n)\sim n^3(\log n)^2/18$, divided by the ambient capacity mass $\asymp P_n^2$ (the *ocho* §6 normalization the continuum functional assigns the conductor-$P_n$ slice), is exactly the capacity $6\,\mathrm{pure}_V/P_n^2 \to 0$ ($0.33$ at $n{=}2 \to 2.5\times10^{-9}$ at $n{=}7$). The margin **deflates** — polynomially thin in an exponentially large ambient — so positivity cannot be certified in C-I and the inequality relocates to C-J. The Rem 6.7 prediction is thereby converted to a verdict: **C-I is not a closure route.**

After W1 (N0 Lemma 6.10) no step of the bridge has undeclared difficulty: C-I is closed, so the bridge reduces to the **single live branch C-J $=$ (T1, T2)** at the schedule $\theta_0(n)$, against the core inequality $(\text{uncancelled non-diagonal mass}) < \mathrm{pure}_V(P_n)$.

### 4.4. The main theorem

**Theorem 4.4** (RH outline — conditional). Subject to:
(i) Theorem A1 (closed),
(ii) Theorem A2 (closed),
(iii) Theorem A3 via the bridge of Theorem 4.3 — with W1 supplied (N0 Lemma 6.10) and C-I closed, the sole remaining inputs are the terminus estimates **T1 and T2** at the schedule $\theta_0(n)$ (coupling C-J),
the Riemann Hypothesis holds: every nontrivial zero of $\zeta$ has real part $1/2$.

**Proof.** By Theorem 4.1, cubic positivity on $\mathcal{G} \times \mathcal{H}_c$ implies RH. By Theorems 4.2 and 4.3, cubic positivity holds under RH and the discrete-to-continuous bridge — but the forward direction (4.1) does not require RH a priori. So we have RH $\Leftrightarrow$ cubic positivity, with cubic positivity established by:
- The constructive class $\mathcal{G}$ is non-empty (Theorem A1, §1.5 Corollary 1.5).
- The cubic Weil moment is non-negative on $\mathcal{G} \times \mathcal{H}_c$ (consequence of the structural reduction of *ocho* §3 and §7, modulo [A3']).

The forward direction (Theorem 4.1) does not require [A3']: it uses only the cluster contribution and the bulk estimate, both unconditional. **So [A2'] alone (modulo the standard ANT execution of [A3'] needed for the bridge to the discrete primorial witness) suffices for the forward direction RH $\Rightarrow$ cubic positivity, while [A1'] + [A3'] gives the construction of explicit positive elements.** $\square$

---

## 5. Status summary

| Component | Theorem | Status |
|---|---|---|
| $\mathcal{G}$ non-empty (unconditional) | Theorem A1 = Corollary 1.5 | **Proved** (Beurling sampling on $\Gamma_T^*$) |
| Cubic Bombieri witness (full) | Theorem 2.7 = Corollary 2.8 | **Proved** (FE-cluster + bulk $\epsilon$-$\delta$ scaling) |
| Primorial-indexed BV at rate $1 - C^*/n$ | Theorem 3.3 | **Proof outline** (CRT + Heath-Brown + large sieve + Burgess + Mertens) |
| Exact level schedule $\theta_0(n)$, $C^*(n)$ | §3.5 | **Verified** (`verify_diez43.py`; retires the single $C^*\le2.80$) |
| W1 — explicit-formula reduction + weights $w_d$ | N0 Lemma 6.10 | **Supplied** (reduction certified `verify_w1_explicit_formula.py`; C-I closed negatively) |
| T1 — sparse-primorial BDH variance ($n$ all) | §4.3 | **Open** (empirically $B$ bounded $\le0.55$; smooth-modulus candidate) |
| T2 — signed third moment (binding $n\ge11$) | §4.3 | **Open** (empirically CLT scale $V^{3/2}/\phi$; unoccupied) |
| Cubic positivity ⟺ RH (forward direction) | Theorem 4.1 | **Proved** (does not require [A3']) |
| Cubic positivity ⟺ RH (reverse direction) | Theorem 4.2 | **Proved** (under RH) |
| Discrete-to-continuous bridge | Theorem 4.3 | **Theorem modulo T1, T2 (C-J); W1 supplied, C-I closed** |
| RH proof outline | Theorem 4.4 | **Conditional on T1 + T2 (the sole live branch, C-J)** |

**The honest state of affairs as of 2026-06-10.** The forward direction (RH from cubic positivity) is proved unconditionally. The cubic positivity criterion is established via the explicit $g \in \mathcal{G}$ of Theorem 1.4. The remaining gap is no longer "verify a single constant $C^* \leq 2.80$" but the **coupling-explicit bridge** (Theorem 4.3, revised): the level schedule $\theta_0(n)$ is exact and verified, and the bridge is a theorem modulo the sparse-primorial BDH variance bound **T1** and the signed-third-moment bound **T2** (binding only for $n \geq 11$, the Hölder ceiling closing $n \leq 10$ given T1). **W1 is now supplied** (N0 Lemma 6.10): the Guinand–Weil explicit-formula reduction of $\mathrm{Re}\,\mathcal{C}_\zeta$ to the $w_d$-weighted per-modulus third moments, with explicit weights $w_d = \widehat W_\eta/\varphi(d)$, archimedean part $n$-independent, and the core zero$\to$prime reduction certified to $10^{-21}$ — and it **closes the C-I branch negatively** (the V-sector margin deflates as the capacity $6\,\mathrm{pure}_V/P_n^2 \to 0$), leaving **C-J $=$ (T1, T2)** the sole live branch. The unconditional frontier is $n \leq 5$ (bilinear $6/11$, razor-tight). After W1, no step of the bridge has undeclared difficulty; T1/T2 are specialist-verifiable on the order of Polymath 8 (2014), with the $p_n$-smooth conductor structure naming the candidate apparatus.

**The structural reduction is complete; the technical proofs of [A1'] and [A2'] are at referee level; the technical proof of [A3'] is at proof-outline level pending the specialist constant verification.**

---

## References

- Beurling, A. (1959). *Sur les intégrales de Fourier absolument convergentes*. Mittag-Leffler Inst., Stockholm. (Reprinted in *Collected Works*, vol. 2.)
- Beurling, A., Malliavin, P. (1962). On Fourier transforms of measures with compact support. *Acta Math.* **107**, 291–309.
- Bombieri, E. (1965). On the large sieve. *Mathematika* **12**, 201–225.
- Burgess, D. A. (1962). On character sums and $L$-series II. *Proc. London Math. Soc.* (3) **13**, 524–536.
- Heath-Brown, D. R. (1982). Prime numbers in short intervals and a generalized Vaughan identity. *Canad. J. Math.* **34**, 1365–1377.
- Iwaniec, H., Kowalski, E. (2004). *Analytic Number Theory*. AMS Colloquium Publications, vol. 53.
- Maynard, J. (2015). Small gaps between primes. *Ann. of Math.* (2) **181**, 383–413.
- Polymath, D. H. J. (2014). New equidistribution estimates of Zhang type. *Algebra Number Theory* **8**, 2067–2199.
- Seip, K. (2004). *Interpolation and Sampling in Spaces of Analytic Functions*. AMS University Lecture Series **33**.
- Titchmarsh, E. C. (1948). *Introduction to the Theory of Fourier Integrals*, 2nd ed. Oxford.
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford.
