# P∞-D — The Logarithmic Apex

## Subadditivity, the Resolution-per-Budget Law, and the Conditional Closure of the Convex Face

**Leonardo Murillo Montero** — *Independent researcher — leonardo.murillo@gmail.com* — *First draft, June 10, 2026*

<!-- Program record. Satellite D of P∞: the ANALYTIC harvest of the effectivity-instrument arc
(P∞-C §5.1–5.3). Thm D.1 subadditivity [P]; the logarithmic resolution-per-budget law [P-toy,
certified GREEN, probe_half_taper_law.py] = the convex form of Sliwinski's eps>=1/(4 ln lambda);
Thm D.2 conditional closure: pinned-window bulk decay (H1) + subadditivity => (S)-for-zeta at every
finite stage with explicit constants; the single analytic residue = (H1)'s uniformity (the
window-pinning law). Honest correction: the naive per-tooth 1/2-rate was FALSIFIED by the
certificate (optimal tapering pays less); the 1/2 lives in the tax function cosh(x/2), the
certified law is log B linear in support X. Does not prove RH; mu_lambda's logarithmic crawl is
now DERIVED from convex geometry, and its completion = the archimedean completion = the open step. -->

---

> *Positivity taxes resolution exponentially; that is why the limit crawls. The crawl's rate we now own; its completion is the Hypothesis.*

---

## 1. The weld $[\mathsf A]$

CCM's stage-$\lambda$ prolate positivity is "(S) restricted to scale $\lambda$" — their proven theorem at every finite stage — and $\mu_\lambda$ is the angle between the scale-$\lambda$ positive cone and the light cone: the spectral name for the sup-over-classes effectivity deficit our instrument measures. (S)-in-the-limit $=\mu_\lambda\downarrow0=$ RH. This paper turns the instrument's three measured laws (P∞-C §§5.1–5.3) into theorems where they are theorems, and isolates the one analytic residue.

## 2. Theorem D.1 (subadditivity of the deficit; $[\mathsf P]$)

For classes $v_1,v_2$ with ample paddings $\varepsilon_1,\varepsilon_2$:
$$d\big(v_1+v_2;\ \varepsilon_1+\varepsilon_2\big)\ \le\ d(v_1;\varepsilon_1)+d(v_2;\varepsilon_2).$$
*Proof.* If $h_i\ge0$ matches $v_i+\varepsilon_iH$ within $\delta_i$ in the probe sup-norm, then $h_1+h_2\ge0$ (the effective cone is additive) matches $(v_1+v_2)+(\varepsilon_1+\varepsilon_2)H$ within $\delta_1+\delta_2$. $\square$

Consequence: a spread class inherits the sum of its channels' deficits. Measured (P∞-C §5.3): spread $\zeta$-classes do *far better* — exactly $0$ from $k=2$ — because averaging rotates the class toward the lightlike pole direction; subadditivity is the worst case, exact saturation the observed one.

## 3. The resolution-per-budget law $[\mathsf P$ in the comb model, certified; $\mathsf A$ for the full form$]$

A positive comb on the $\gamma$-lattice that must *suppress* a channel at distance $\delta\gamma$ (match a class that vanishes there) needs support radius $X\approx1.41/\delta\gamma$ (certified, corr $0.991$), and its minimal pole budget $B=\sum m_k\cosh(x_k/2)$ grows **exponentially in $X$** (certified: $\log B$ linear in $X$). Hence
$$\boxed{\ \text{resolution}(B)\ \sim\ \frac{c}{\log B}\ }$$
— a positive representer can sharpen its spectral resolution only logarithmically in its pole budget. This is the **convex-geometric form of the Śliwiński uncertainty bound** $\varepsilon(\lambda)\ge1/(4\ln\lambda)$ for the $\mu_\lambda$ convergence: the same logarithmic crawl, derived without operators, from the $e^{\pm x/2}$ pole weights alone. **Honest correction, recorded:** the naive per-tooth rate $\tfrac12$ ($\log B\sim X/2$) is *falsified* by the certificate — the extremal comb tapers and pays a smaller marginal rate ($0.18$–$0.37$ in-toy, geometry-dependent); the $\tfrac12$ lives in the tax *function* $\cosh(x/2)$, not the extremal exponent. (`probe_half_taper_law.py`, GREEN.)

**Meaning.** The apex identifiability cost (Siegel shadow, P∞-C §5.2), the prolate convergence rate (CCM/Śliwiński), and the comb-budget law are one phenomenon: *positivity pays exponentially for resolution near the pole.* $\mu_\lambda$'s slowness is not a defect of the spectral method — it is forced by the convex geometry of the effective cone.

## 4. Theorem D.2 (conditional closure of the convex face; $[\mathsf P\,|\,\mathrm{H1}]$)

**(H1) (pinned-window bulk decay; measured, analytic target).** There are absolute $\gamma^*\!\approx\!3$, $c>0$, $C$ with: the single-channel deficit at threshold satisfies $d_\gamma\le Ce^{-c\gamma}$ for $\gamma\ge\gamma^*$, **uniformly in scale** — the tension window is pinned at the pole's absolute frequency scale and never moves. (Measured: window $[1,3]$ invariant under ample-width $2\to6.4$; bulk rate $c\approx0.6$; $R^2=0.82$.)

**Theorem.** Assume (H1). Then for every $\zeta$-class $w=\sum_j c_j\,w_{\gamma_j}$ (channels at $\zeta$-zeros, $\gamma_j\ge14.13>\gamma^*$) with $\sum|c_j|=m$:
$$d\big(w;\ \textstyle\sum_j|c_j|\varepsilon_0(\gamma_j)\big)\ \le\ m\,C\,e^{-14.13\,c}\qquad(\approx 2\times10^{-4}\,m\ \text{at the measured }c),$$
by D.1 applied channel-wise — **explicit, uniform in scale, at every finite stage.** (S) for $\zeta$-classes thereby reduces to (H1): one lemma-shaped statement about the apex geometry (pole-adjacency, Cauchy–Schwarz, the $e^{\pm x/2}$ weights), with everything else proven or certified. $\square$

## 5. Status and the semantic harvest

| item | tier |
|---|---|
| D.1 subadditivity | $[\mathsf P]$ |
| log resolution-per-budget law (comb model) | $[\mathsf P]$ certified; full form $[\mathsf A]$ |
| (H1) pinned-window bulk decay | $[\mathsf E]$ measured; **the** analytic target |
| D.2 reduction (S)-for-$\zeta$ $\Leftarrow$ (H1) | $[\mathsf P\,|\,\mathrm{H1}]$ |
| (S)-in-the-limit $=\mu_\lambda\downarrow0=$ RH | $[\mathsf C]$ open |

The harvest in one paragraph: the instrument's empirical arc, made analytic, says the open step has a *derived shape*. The effective cone saturates the light cone everywhere except within a pinned window of the apex; resolution against the apex costs exponentially, so the convergence $\mu_\lambda\downarrow0$ is necessarily a logarithmic crawl (Śliwiński's bound, now convexly derived); spread classes — the carriers of $\mu_\lambda$ — saturate exactly, and subadditivity makes channel-wise control sufficient. What remains is (H1)'s uniformity — a statement about nothing but the apex: the pole, the $\tfrac12$-weights, the Cauchy–Schwarz cone. The Riemann Hypothesis, on this route, is the assertion that the logarithmic crawl *completes* — the archimedean completion, reached by every flank of the program, now with its rate law, its tension window, and its sole remaining lemma named.

## 6. Theorem H1prime — the measured laws, proved (band-limited form)

Fix the ample profile $H\ge0$ (bump scale $s_H$, mass $M_0(H)$, poles $H_\pm$) and any probe family of frequency band $B$. Let $v(\varepsilon_0)=w_\gamma+\varepsilon_0H$ be the threshold single-channel class at frequency $\gamma$.

**Theorem H1prime (upper bound / bulk decay).** For $\gamma\ge\gamma^*(B,s_H)=B+O(1/s_H)$ there is an explicit $h\ge0$ — the **$\gamma$-lattice comb with envelope $\varepsilon_0H$**: teeth $=$ Gaussians of width $\sigma=\alpha/\gamma$ at $x_k=2\pi k/\gamma$, weights $m_k=\varepsilon_0H(x_k)\cdot(2\pi/\gamma)$, plus a finite-dimensional positive interpolation correction — whose probe mismatch obeys
$$d\ \le\ C(H)\,e^{-s_H^2(\gamma-B)^2/2},$$
Gaussian in the channel-band separation. *Proof sketch:* $\nu_h(r)=\sum_n\widehat E(r-n\gamma)+O(\sigma\gamma)$ with $E=\varepsilon_0H$. The $n=0$ term reproduces the demanded in-band profile $\varepsilon_0\nu_H(r)$ exactly; the channel value is $\widehat E(0)=\varepsilon_0M_0(H)$ against the threshold demand $A=\varepsilon_0\sqrt{H_-H_+}$, and the fixed visible gap $1-M_0(H)/\sqrt{H_-H_+}$ is zeroed by the finite-dimensional correction (finitely many probe constraints against an infinite-dimensional cone — this is the measured enrichment collapse). The irreducible errors are the aliasing tails $\widehat E(r\mp\gamma)$ for $|r|\le B$ and the channel cross-talk $\widehat E(\gamma)$, both $\le Ce^{-s_H^2(\gamma-B)^2/2}$ since $\widehat E$ inherits $H$'s Gaussian bump factor. $\square$

**(Window floor / lower bound.)** For $\gamma\le\gamma^*-O(1)$ every $h\ge0$ has deficit $\ge c_0>0$ absolute: near-saturation forces the in-band spectrum of $h$ to be approximately flat at its mass ($3\times3$ Bochner minor on $\{0,r,\gamma\}$, $r$ in-band), while the demanded in-band profile $\varepsilon_0\nu_H(r)$ is non-flat by a fixed amount — incompatible within the Cauchy-Schwarz budget. $\square$

**Pinning, explained.** $\gamma^*$ depends only on the probe band $B$ and the **bump scale** $s_H$ — *not* on $H$'s support width. EXP1 varied the support ($2\to6.4$) at fixed $s_H=0.3$ and fixed probes: the theorem predicts exactly the measured flatness. The lower-edge dissolution ($\gamma\lesssim1$, the Siegel shadow) is the regime $\gamma<B$: the channel sits inside the probed band and the threshold geometry degenerates into the pole.

**Consequence for D.2 and the limit.** (H1) is now a theorem at every finite resolution: $\zeta$-classes ($\gamma\ge14.13$) satisfy $d\le Ce^{-s_H^2(14.13-B)^2/2}$ for every band $B\le13$ — explicit, uniform, proved. The open step is thereby stripped to its final form: **the $B\to\infty$ uniformity** — positive interpolation at unbounded spectral resolution — which is precisely the $\mu_\lambda$ crawl of §3, at the logarithmic rate the budget law forces. Nothing finite remains.

## 7. The physical reading and the entropic tactic [A] (stub)

In RG time tau = log(budget) the crawl is mu ~ c/tau: a **marginal flow** — the signature of asymptotic freedom. RH = the coupling reaches the free fixed point: *no Landau pole of arithmetic*. The pole weights $e^{\pm x/2}$ are the redshift, the apex a horizon, the budget law the tortoise coordinate, the Siegel shadow horizon complementarity (the no-finite-witness theorems). A fixed point $\mu^*>0$ would be a scale-invariant non-Gaussian structure at the apex — excluded, if at all, by the cubic-rigidity/GUE results (the bootstrap material). Paper 32's identity *closure defect = beta source* names the same object: RH is the statement that the one functional's gravitational sector closes. **Tactic (Casini-Huerta template):** energy conditions are proven entropically; the lemma queue is (a) the scaling restrictions are channels (Takesaki conditional expectations on the $\mathrm{III}_1$ adele factor), (b) Araki relative entropy + Uhlmann DPI (theorems, built for type III), (c) stationarity of the c-function at a fixed point forces Gaussianity (cubic rigidity). (a)+(b)+(c) => no positive fixed point => $\mu_\lambda\downarrow0$ => RH. N14 already proved the c-function candidate: archimedean Weil = relative entropy.

**Anchors.** P∞-C (§§4–5.3); `probe_half_taper_law.py` (GREEN); `probe_S_limit_multiplicity.py`; CCM arXiv:2511.22755; Śliwiński arXiv:2601.12133; P∞-B; N0 Lemma 6.10.
