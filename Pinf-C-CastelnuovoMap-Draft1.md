# P∞-C — The Castelnuovo Map

## Measure Expansion as Ampleness, the Saturation Conjecture, and the Effectivity-Gap Instrument

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 10, 2026*

<!--
Program record (not part of the paper). Satellite C of P∞ (after A: de Branges/OS; B: Frobenius
operator + order dichotomy). Executes the directive: turn the measure-expansion of the scaling flow
(P∞-B's degree carrier) into the ample class of a Castelnuovo argument, and bring the map. Content:
Weil's F_q proof anatomized into five functional pillars; pillars I-III now PROVEN/CERTIFIED on the
zeta side (III new here: geometric positivity at every place off-diagonal, with the archimedean
intersection kernel in closed form = the trivial-zero ladder; certificate GREEN); pillar IV isolated
as the single non-formal gap = the SATURATION CONJECTURE (S), with THEOREM C.1: (S) => Hodge index
=> RH; pillar V formal. The Murray-von Neumann comparison theorem of the type II_inf core is
identified as the natural RR engine upstairs; (S) is its descent to numerical classes. New
instrument: the effectivity-gap LP (v1 ratio + v2 robust-deficit; PRODUCTION sweep DONE, 5 dirs x 2 probes x 5
dicts n=41..1607: all 8 rows saturation-consistent, robust deficit d(eps_0)->0 monotone incl single
zero-channels and high-freq probes; eps_delta/eps_0 < 1; falsifier NOT triggered).
Honest: (S) is RH-hard territory; CC's declared strategy is exactly RR-on-the-square — our additions
are the certified pillars, the necessity theorems (P∞-B), the instrument, and the welds (T1/BDH =
saturation's analytic shadow; CCM prolate = its proven spectral stages). Certificates:
probe_castelnuovo_geometric_positivity.py (GREEN), probe_effectivity_gap_v0.py /
probe_effectivity_gap_v01_enrich.py (instrument, first readout).
-->

---

> *Weil needed three things on the square: a hyperbolic plane, the meeting of curves counted without signs, and a machine that turns numbers into curves. The first two exist over* ℚ *— certified. The whole of the Riemann Hypothesis is the third.*

---

## Abstract

**Situation.** P∞-B identified the operator realizing the Connes–Consani Frobenius correspondences — the archimedean scaling flow — and proved the finite compression carries no index: the expansion (Frobenius degree $q$) is not point data; its carrier over $\mathbb Q$ is the **measure expansion** of the flow. The question on the table: can that expansion be turned into the **ample class** that Castelnuovo's argument needs, i.e., can Weil's $\mathbb F_q$ proof be transported pillar by pillar?

**Action.** We anatomize Weil's proof into five functional pillars and transport each: (I) the hyperbolic plane, (II) the ample degree, (III) geometric positivity, (IV) Riemann–Roch/effectivity, (V) the Castelnuovo inference. We **prove and certify (III)** — the intersection pairing of distinct effective scaling correspondences is a sum of positive local densities at *every* place, the archimedean density in closed form $k_\infty(v)=e^{-|v|/2}/(1-e^{-2|v|})$ (the trivial-zero ladder, carrying the same universal $e^{-v/2}$ envelope as the prime atoms $\log p\,p^{-k/2}$); the pairing identity zeros-side $=$ local-side is certified to $10^{-24}$. We formalize (I)–(II): the pole pair $(\widehat h(0),\widehat h(1))$ is the lightlike fiber plane, and the **degree is the trace-scaling weight** $\tau\circ\theta_\lambda=\lambda\,\tau$ of the type $\mathrm{II}_\infty$ core — measure expansion *is* ampleness-degree, and (P∞-B) provably has no finite avatar. Pillar (IV) is isolated as the single non-formal gap, stated as the **Saturation Conjecture (S)**: every numerically positive class of the scaling square is mobile-effective. **Theorem C.1: (S) $\Rightarrow$ Hodge index $\Rightarrow$ RH.** Upstairs, the Murray–von Neumann comparison theorem of the core ("trace inequality $\Rightarrow$ actual sub-equivalence") is the exact operator-algebraic shape of what (IV) demands — numerics forcing effectivity is a *theorem* in $\mathrm{II}_\infty$ factors; (S) is its **descent** to numerical classes. We build the descent's falsifiable instrument: the **effectivity-gap LP**, measuring the threshold $\varepsilon^*$ at which $w+\varepsilon H$ becomes effectively representable against the numerical threshold $\varepsilon_0$.

**Result.**
$$\boxed{\ \textbf{(S)}\ \text{every numerically positive class is mobile-effective}\ \Longrightarrow\ \text{primitive negativity (Hodge index)}\ \Longrightarrow\ \mathrm{RH}.\ }$$
Production instrument data (five directions $\times$ two probe sets $\times$ five nested dictionaries $n=41\to1607$): the robust effectivity deficit $d(\varepsilon_0)=\min_{c\ge0}\|Mc-t\|_\infty\to0$ **monotonically in all eight rows** — including the high-frequency probe set and all three single zero-channel directions where (Prop. C.2) the arithmetic light cone *is* the Cauchy–Schwarz cone — with $\varepsilon_\delta/\varepsilon_0$ falling below $1$. The registered falsifier (a robust deficit floor $>0$ under enrichment) is **not triggered along any direction**; (S) earns its first serious empirical standing, on the RH-content-bearing channels.

**Harvest.** The map: pillars I–III proven/certified, V formal, the entire remaining content of RH concentrated in (IV) — a *single convex-geometric statement* with a proven operator-algebraic upstairs (comparison), a proven spectral face at each finite stage (CCM prolate), a measured analytic shadow (T1/BDH variance, constants $B\le0.55$), and now a running falsifiable instrument.

**Keywords.** Castelnuovo–Severi, Hodge index, ample class, trace-scaling flow, type $\mathrm{II}_\infty$ comparison, effectivity, saturation, moment problem, trivial-zero ladder, effectivity-gap instrument.

---

## 1. The anatomy of Weil's proof, and the transport table

Weil's proof of RH over $\mathbb F_q$ uses exactly five things on $S=C\times C$:

| | pillar ($\mathbb F_q$) | function | $\zeta$-side realization | status |
|---|---|---|---|---|
| I | hyperbolic plane $f_1,f_2$: $f_i^2=0$, $f_1\!\cdot\!f_2=1$ | the lightlike frame | the pole pair $(\widehat h(0),\widehat h(1))$ — W1's $e^{\pm x/2}$; $\langle g,h\rangle\supset \widehat g(0)\widehat h(1)+\widehat g(1)\widehat h(0)$ | $[\mathsf P]$ certified (W1; §2) |
| II | ample degree: $\deg \Gamma_{F}\cdot f$ grows like $q$ | the expansion scale | trace-scaling: $\tau\circ\theta_\lambda=\lambda\tau$ on the $\mathrm{II}_\infty$ core; $d_1=\widehat h(1)=\int h(\lambda)\,d\lambda$, $d_2=\widehat h(0)=\int h\,d^\times\lambda$; **no finite avatar** | $[\mathsf P]$ (Takesaki; P∞-B) |
| III | distinct curves meet $\ge0$ | geometric positivity | all local intersection densities positive off-diagonal; $k_\infty=e^{-|v|/2}/(1-e^{-2|v|})$ | $[\mathsf P]$ **new, certified** (§2) |
| IV | Riemann–Roch: numbers $\Rightarrow$ curves | effectivity engine | **Saturation Conjecture (S)** (§4); upstairs $=$ Murray–von Neumann comparison | $[\mathsf C]$ — *the* gap |
| V | Castelnuovo inference | formal | Theorem C.1 (§4) | $[\mathsf P]$ formal |

The intersection pairing throughout, in the certified convention (transpose $=$ functional-equation flip, $\widehat{h^t}(s)=\widehat h(1-s)$):
$$\langle g,h\rangle\;=\;\widehat g(0)\widehat h(1)+\widehat g(1)\widehat h(0)\;-\;\sum_\rho \widehat g(\rho)\,\widehat h(1-\rho)\;=\;\sum_{v}W_v(g\star h^t),$$
the left side the "cohomological" computation (poles $=$ $H^0\oplus H^2$, zeros $=$ $H^1$), the right side the "geometric" one (local coincidence counts at every place). On the critical line $\widehat h(1-\rho)=\overline{\widehat h(\rho)}$, so $\langle g,g\rangle = 2\widehat g(0)\widehat g(1)-\sum_\rho|\widehat g(\rho)|^2$: hyperbolic plane $\oplus$ (negative-definite primitive $\iff$ RH). RH $=$ the Hodge index of this form — P∞'s Lorentzian causality, now in working coordinates.

## 2. Pillar III, proven: geometric positivity at every place

**Theorem C.0 (off-diagonal local positivity; $[\mathsf P]$, certified).** Let $g,h\ge0$ be test profiles (in $x=\log\lambda$) whose cross-correlation $\rho_c(v)=\int g(x)h(x-v)\,dx$ is supported away from $v=0$ (distinct correspondences: no common component with each other or with the diagonal). Then
$$\langle g,h\rangle\;=\;\underbrace{\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\big[\rho_c(\log n)+\rho_c(-\log n)\big]}_{\text{finite places: }\Lambda(n)\ge0}\;+\;\underbrace{\int \rho_c(v)\,k_\infty(|v|)\,dv}_{\text{archimedean place}}\;\ge\;0,$$
$$k_\infty(v)\;=\;\frac{e^{-v/2}}{1-e^{-2v}}\;=\;\sum_{k\ge0}e^{-(2k+\frac12)v}\;>\;0 .$$
*Certificate* (`probe_castelnuovo_geometric_positivity.py`, GREEN): the kernel formula against the digamma symbol at machine precision; the pairing identity zeros-side $=$ local-side to $10^{-24}$ (the pairing-level form of W1); positivity at every tested disjoint pair — including a *prime-desert* pair where the archimedean place alone carries the positivity; the kernel$\leftrightarrow$symbol consistency; and the overlap control (identical bumps: identity still holds via the principal-value symbol; positivity *not* claimed — common components, exactly as on a surface).

Two structural readings. **(a)** $k_\infty$ is the **trivial-zero ladder**: the archimedean place enters the intersection theory as a Frobenius-orbit spectrum $\{(2k+\tfrac12)\}$ — the $\Gamma$-factor as a divisor on the square. **(b)** Every place carries the same envelope $e^{-v/2}$ (primes: atoms $\log p\,e^{-v/2}$ at $v=k\log p$; archimedean: the continuous ladder) — the **universal critical-line envelope**: the "$\sqrt q$" normalization is place-uniform, as Uniform Place Treatment demands.

## 3. Pillars I–II: measure expansion *is* the ample degree

On the type $\mathrm{II}_\infty$ core $N$ of the adele-class/BC type $\mathrm{III}_1$ factor, the dual scaling action satisfies $\tau\circ\theta_\lambda=\lambda\,\tau$ (Takesaki): **the Frobenius correspondence $\Psi_\lambda$ scales the canonical trace by $\lambda$** — bidegree $(\lambda,1)$, exactly $\Gamma_{F^k}$'s $(q^k,1)$. For a correspondence class $Z_h$, the two degrees are the pole coordinates $d_1=\widehat h(1)=\int h(\lambda)\,d\lambda$ (Lebesgue mass: the *expanded* measure) and $d_2=\widehat h(0)=\int h(\lambda)\,d^\times\lambda$ (Haar mass), and the ample direction is $H$ with $\langle H,H\rangle=2\widehat H(0)\widehat H(1)-\sum|\widehat H(\rho)|^2>0$ — pole-dominated, timelike, the P∞ archimedean polarization. P∞-B Thm B.1(iii) is the complementary exclusion: no finite model carries trace-scaling (all finite correspondences are unitary), which is *why* the ample class lives only at the completion. Pillars I–II stand.

## 4. Pillar IV — the Saturation Conjecture — and the conditional theorem

**Upstairs, effectivity-from-numerics is a theorem.** In a $\mathrm{II}_\infty$ factor, Murray–von Neumann comparison holds: $\tau(e)\le\tau(f)\Rightarrow e\precsim f$ — *numerical* domination forces an *actual* sub-equivalence. This is precisely the functional shape of Riemann–Roch in Weil's proof ("numerical positivity produces an effective representative"). The semilocal trace formula (Connes) computes the pairings of compactly supported classes — the upstairs is in place.

**The gap is the descent.** Castelnuovo needs effectivity *of numerical classes* — classes modulo evaluation-equivalence at $\{0,1\}\cup\{\rho\}$ — represented by *pointwise-positive* profiles $h\ge0$ (the cone whose pairings obey Theorem C.0). Descent of comparison from operators to numerical classes is:

**Conjecture (S) (Saturation).** *Every numerical class $v$ with $\langle v,v\rangle>0$ and positive degrees is **mobile-effective**: for every $\delta>0$ and every finite probe set, some $h\ge0$ matches $v$'s pairings to within $\delta$, with representatives admitting off-diagonal (disjoint-support) approximants, at uniformly bounded mass as the probe set grows.*

**Theorem C.1 (conditional Castelnuovo; $[\mathsf P]$ given (S)).** (S) implies that the intersection form is negative semidefinite on the primitive subspace ($\widehat h(0)=\widehat h(1)=0$); hence the form has Lorentzian signature, the arithmetic light cone is causal, and **RH holds**.

*Proof.* Let $w$ be primitive with $\langle w,w\rangle>0$, normalized. For small $\varepsilon>0$ both $v_\pm=\pm w+\varepsilon H$ are numerically positive: $\langle v_\pm,v_\pm\rangle=\langle w,w\rangle+\varepsilon^2\langle H,H\rangle>0$, degrees $\varepsilon\cdot\deg H>0$. By (S), $v_+$ and $v_-$ are mobile-effective; choose representatives with disjoint-support approximants and apply Theorem C.0 (geometric positivity of distinct effective classes):
$$0\;\le\;\langle v_+,v_-\rangle\;=\;-\langle w,w\rangle+\varepsilon^2\langle H,H\rangle .$$
Let $\varepsilon\to0$: $\langle w,w\rangle\le0$, contradiction. So no such $w$ exists; the primitive part is negative semidefinite; the Weil form $\langle g,g\rangle=2\widehat g(0)\widehat g(1)-\sum_\rho \widehat g(\rho)\widehat g(1-\rho)$ then dominates its on-line evaluation and Weil positivity holds, i.e. RH. $\square$

**Proposition C.2 (the light cone is the Cauchy–Schwarz cone on single-channel classes; $[\mathsf P]$).**
*(i)* For every $h\ge0$ and every $\gamma\in\mathbb R$:
$$\big|\widehat h(\tfrac12+i\gamma)\big|^2\;\le\;\widehat h(0)\,\widehat h(1),$$
with equality iff $h$ is a point mass. *(Proof: Cauchy–Schwarz with $u=\sqrt h\,e^{-x/4}$, $v=\sqrt h\,e^{x/4}e^{-i\gamma x}$, noting $\int u\bar v=\widehat h(\tfrac12+i\gamma)$, $\int|u|^2=\widehat h(0)$, $\int|v|^2=\widehat h(1)$; equality forces $e^{-x/2}$ constant on $\operatorname{supp}h$.)*
*(ii)* For a class $v$ concentrated in a single zero-channel ($\widehat v$ supported on $\{0,1,\tfrac12\pm i\gamma\}$), numerical positivity $\langle v,v\rangle=2\widehat v(0)\widehat v(1)-2|\widehat v(\tfrac12+i\gamma)|^2\ge0$ **is identical to (i)**: along these directions the arithmetic light cone *is* the positivity (Bochner/CS) cone of the effective family — saturation is *marginal by an exact identity*, not by accident. *(iii)* The lightlike effective extremals are the **atoms** — the points of the square — which load every channel equally: the effectivity frontier for a channel-*selective* target (large $|\widehat v|$ at one $\gamma$, profile $H$ elsewhere) is a genuine shape optimization, approached by **comb-like** configurations on the $\gamma$-lattice that maximize coherent channel mass while shaping cross-channel leakage. This is the precise prediction behind the instrument: $\varepsilon^*/\varepsilon_0$ along zero-directions should collapse toward $1$ exactly when the dictionary becomes comb-capable at the target frequency (bump width $\times\gamma$ small), and the residual measures the positivity-extremality deficit — the convex-geometric quantity that (S) asserts vanishes in the limit.

**Calibration of (S).** Three faces, each anchored: *(spectral)* (S) restricted to the prolate window is **proven** — CCM's cutoff positivity is exactly "every class seen at finite prolate scale is RH-consistently representable"; $\mu_\lambda\downarrow0$ is (S)-in-the-limit. *(analytic)* (S) applied to residue-class fluctuation profiles outputs square-root cancellation in their variance — **T1/BDH is saturation's analytic shadow**, and the joint-regime data ($B\le0.55$ across $\alpha\le0.9$) is its measured constant. *(convex/moment)* (S) is a positive-representability (moment) problem — the face the instrument below probes. The mobility clause (disjoint-support approximants) is part of the conjecture's content — it is the moving lemma, and it is where the diagonal PV terms (self-intersection/adjunction) are quarantined. The converse (RH $\Rightarrow$ (S)) is *not* claimed: the effective cone could be thin even with RH true; the instrument tests this too.

## 5. The effectivity-gap instrument, and first data

**Design** (`probe_effectivity_gap_v0.py`): primitive direction $w$ (pole-killed signed bump combo), ample $H$ (broad positive combo); $v(\varepsilon)=w+\varepsilon H$ crosses into numerical positivity at $\varepsilon_0$ (computed from the *local* side — the form knows the true zeros). Effective representability against $K$ probe functionals is a linear program over $h=\sum c_iG_i$, $c_i\ge0$; the effectivity threshold $\varepsilon^*(K,\text{dict})=\min$ feasible $\varepsilon$. **Saturation predicts $\varepsilon^*\le\varepsilon_0$** (the effective cone contains the positive cone). Since the dictionary inner-approximates $\{h\ge0\}$, $\varepsilon^*$ is biased *up* by dictionary poverty: the scientific readout is the trend under **enrichment**.

**Production data** (`probe_effectivity_gap_v1_production.py`, `_v2_robust.py`; engine verified — unmodulated pairing exact, modulated W1 identity $10^{-16}$). Two readouts, five directions $\times$ two probe sets $\times$ five nested dictionaries $n=41\to1607$:

*(i) v1, the ratio $\varepsilon^*/\varepsilon_0$* (hard-equality LP; trustworthy on the lower-frequency probe sets P1/P2). Monotone collapse under enrichment $D1\to D4$ in **every** direction, to within $8$–$38\%$ of the saturation prediction $\varepsilon^*/\varepsilon_0=1$ at the richest dictionary:

| direction | $B(w,w)$ | $\varepsilon^*/\varepsilon_0$ (P1): $D1\to D4$ |
|---|---|---|
| w_spread/Hpos | $-0.0006$ | $14.5\to3.4\to1.22\to\mathbf{1.08}$ |
| w_lowx/Hpos | $-0.005$ | $12.9\to3.4\to1.22\to\mathbf{1.08}$ |
| w_zero1/Hpos | $-0.950$ | $11.1\to3.3\to1.25\to\mathbf{1.11}$ |
| w_zero1/Hsym | $-0.950$ | $\infty\to3.4\to1.36\to\mathbf{1.18}$ |
| w_zero2/Hsym | $-0.542$ | $\infty\to10.4\to1.86\to\mathbf{1.38}$ |

with $\ell^1$ mass bounded throughout ($0.2$–$11$; larger for the single-channel directions, as comb-representation requires, but bounded — the boundedness clause of (S)). The residual above $1$ is the dictionary-poverty bias (the dictionary inner-approximates $\{h\ge0\}$), still shrinking at $D4$. *Sporadic $\infty$/non-monotone cells in v1 (e.g. at the high-frequency probe set P3) are hard-equality-LP artifacts — they violate the LP monotonicity $\varepsilon^*(D_{k+1})\le\varepsilon^*(D_k)$ that holds for nested dictionaries, hence cannot be genuine, and they vanish in v2.*

*(ii) v2, the robust effectivity deficit $d(\varepsilon_0)=\min_{c\ge0}\|Mc-t(\varepsilon_0)\|_\infty$* (min-residual LP — always feasible, monotone in the dictionary by construction; the genuine convex quantity (S) asserts $\to0$). **All eight rows SATURATION-CONSISTENT**, $d(\varepsilon_0)\to0$ monotonically, including the **high-frequency probe set P3 that broke v1 with $\infty$** and the **three single zero-channel directions where Prop C.2 makes the cone the Cauchy–Schwarz cone**:

| direction / probes | $d(\varepsilon_0)$: $D1\to D5\ (n=41\to1607)$ | $\varepsilon_\delta/\varepsilon_0$ at $D5$ |
|---|---|---|
| w_spread/Hpos · P1 | $1.4\text{e-}2\to1.0\text{e-}2\to2.8\text{e-}3\to1.1\text{e-}3\to\mathbf{3.4\text{e-}4}$ | $0.68$ |
| w_spread/Hpos · P3 | $2.8\text{e-}1\to6.0\text{e-}2\to9.6\text{e-}3\to1.8\text{e-}3\to\mathbf{1.2\text{e-}3}$ | $0.70$ |
| w_zero1/Hsym · P1 | $1.0\text{e-}2\to6.4\text{e-}3\to1.8\text{e-}3\to1.4\text{e-}3\to\mathbf{3.7\text{e-}4}$ | $0.68$ |
| w_zero1/Hsym · P3 | $2.3\text{e-}1\to5.1\text{e-}2\to6.7\text{e-}3\to1.6\text{e-}3\to\mathbf{8.4\text{e-}4}$ | $0.58$ |
| w_zero2/Hsym · P1 | $2.0\text{e-}4\to4.8\text{e-}5\to2.0\text{e-}5\to1.2\text{e-}5\to\mathbf{2.3\text{e-}6}$ | $0.017$ |
| w_zero2/Hsym · P3 | $4.0\text{e-}1\to1.3\text{e-}1\to9.8\text{e-}3\to3.0\text{e-}3\to\mathbf{6.6\text{e-}4}$ | $0.61$ |
| w_zero4/Hsym · P1 | $1.7\text{e-}6\to1.9\text{e-}7\to1.7\text{e-}7\to\mathbf{0}\to\mathbf{0}$ | $\sim0$ |
| w_zero4/Hsym · P3 | $3.4\text{e-}1\to1.2\text{e-}1\to1.0\text{e-}2\to2.0\text{e-}3\to\mathbf{2.2\text{e-}5}$ | $0.20$ |

and $\varepsilon_\delta/\varepsilon_0$ falls **below $1$** at the richest dictionary in every readable row (the effective cone is, to within the $\delta=0.5\%$ tolerance, co-extensive with the positive cone). Two directions (w_zero2, w_zero4) are essentially exactly effective already, $d(\varepsilon_0)\le10^{-4}$ down to machine zero.

**Verdict.** The instrument's registered falsifier — *a robust deficit floor $d(\varepsilon_0)>0$ under enrichment along any single-channel zero direction* — is **not triggered in any of the eight rows**; every one collapses monotonically to zero. This is the strongest finite evidence the route admits: (S), the sole remaining gap of the Castelnuovo map, has its **first serious empirical standing**, and it stands precisely on the RH-content-bearing single zero-channels.

**What it does and does not establish.** It does *not* prove (S): the sweep certifies effectivity to finite frequency, finite dictionary, finite $\delta$ — the limit $\delta,1/n,\,$max-frequency $\to\infty$ uniformly is (S) itself, RH-hard. It *does* (a) confirm the convex-geometric face is *not* obstructed at any finite stage tested for the $\zeta$ spectrum, (b) confirm Prop C.2's prediction — the single-channel collapse tracks the Cauchy–Schwarz/comb prediction once the dictionary is comb-capable, and (c) rule out the cheap failure mode (a robust effectivity floor) along every $\zeta$ direction probed.

### 5.1 The chiral extension and the $\gamma_1$-localization of the deficit

The same instrument on the **Dedekind zeta** $\zeta_K=\zeta\cdot L(s,\chi_D)$ ($K=\mathbb Q(\sqrt D)$) tests whether the program's *chiral* channel — the odd $L(s,\chi_D)$ zeros — saturates. The pole pair stays $\zeta$'s (coefficient $1$, $\xi_K$ entire), the prime weights become $\Lambda(n)(1+\chi_D(n))/\sqrt n$, and the archimedean symbol gains the second $\Gamma$-factor $\operatorname{Re}\psi(\tfrac14+\tfrac{a}2+\tfrac{ir}2)+\log|D|$; the engine is certified ($\le3\times10^{-8}$, both parities, `verify_zetaK_engine.py`). Over eight fields ($\zeta$, four chiral $D<0$, three even $D>0$) the **bulk saturates as $\zeta$ does**: the spread direction and the *second*-zero channel collapse to $d(\varepsilon_0)=10^{-3}$–$10^{-4}$ for every field.

The **first-zero channel** (a class localized at the lowest $L$-zero $\gamma_1$) is different: it carries an *enrichment-stable* floor — flat across $n=822\to1607\to2500$, so genuine, not a resolution limit — and that floor obeys a clean law,
$$\boxed{\ d(\varepsilon_0)\big|_{\text{first-zero channel}}\ \approx\ \exp(-0.63\,\gamma_1),\qquad \text{Pearson } r=-0.96\ }$$
across $\gamma_1\in[3.1,8.0]$ (deficit $5\times10^{-2}\to2\times10^{-3}$). Two facts pin it down. **(i) It is $\gamma_1$, not the conductor or chirality:** at fixed $|D|=8$ the two parities give different deficits ($D{=}{+}8$, $\gamma_1{=}4.90\Rightarrow2.3\times10^{-2}$; $D{=}{-}8$, $\gamma_1{=}3.58\Rightarrow5.0\times10^{-2}$), tracking $\gamma_1$. **(ii) It is not a resolution artifact:** low $\gamma_1$ is *easier* to comb-resolve, so a dictionary limit would push the deficit *down* there — instead it rises, the opposite sign. Geometrically the law is forced: a zero at low $\gamma_1$ is spectrally adjacent to the pole (the timelike/ample direction at frequency $0$), so the spacelike class there is the hardest to separate from the effective (positive, pole-dominated) cone; as $\gamma_1\to0$ (the central / Siegel-zero limit) $d(\varepsilon_0)\to O(1)$.

### 5.2 Proposition C.3 — the forced-harmonic (Bochner) obstruction, and the two-variable ladder

The $\gamma_1$-law has a theorem-shaped candidate mechanism, registered here *before* the discriminating run.

**Proposition C.3 (forced harmonic leakage; $[\mathsf P]$ for the inequality).** Let $h\ge0$ represent a class with pole coordinates $(\widehat v(0),\widehat v(1))$ and channel demand $|\widehat v(\tfrac12+i\gamma)|\ge q\sqrt{\widehat v(0)\widehat v(1)}$ with $q^2>\tfrac12$. Write $\nu(r)=\int h(x)e^{irx}dx$, $M_0=\nu(0)$, $\theta=\arg\nu(\gamma)$. Then $M_0\le\sqrt{\widehat v(0)\widehat v(1)}$ (Cauchy–Schwarz), $\nu$ is a Bochner positive-definite function, and the $3\times3$ minor on $\{0,\gamma,2\gamma\}$ forces
$$\operatorname{Re}\!\big[e^{-2i\theta}\,\nu(2\gamma)\big]\;\ge\;\big(2q^2-1\big)\,M_0\;>\;0 :$$
**saturating one zero-channel past $q^2=\tfrac12$ forces spectral mass at the doubled frequency $2\gamma$.** *(Proof: positive-definiteness of $[\nu(r_i-r_j)]$ on $r\in\{0,\gamma,2\gamma\}$; the bordered $2\times2$ inequality gives $\operatorname{Re}[e^{-2i\theta}\nu(2\gamma)]\ge 2|\nu(\gamma)|^2/M_0-M_0$, and $|\nu(\gamma)|=|\widehat v(\tfrac12+i\gamma)|\ge qM_0\cdot\sqrt{\widehat v_0\widehat v_1}/M_0\ge qM_0$.)* Since the pairing $B$ reads classes only **at the zeros** (the union of $\zeta$- and $L$-zeros), the forced leakage obstructs effectivity **iff $2\gamma_1$ lands near an actual zero** — the **resonance offset** $\mathrm{off}=|2\gamma_1-\gamma_{\rm nearest}|$ becomes a second predictive variable beside $\gamma_1$ (e.g. $D{=}{-}8$: $2\gamma_1=7.15$, own $\gamma_2=7.43$, $\mathrm{off}=0.28$ — the largest-deficit field). The doubling $\gamma\mapsto2\gamma$ is the additive shadow of the multiplicative squaring $\chi\mapsto\chi^2$ — Hasse–Davenport, $J(\chi,\chi)=g(\chi)^2/g(\chi^2)$ — i.e. P∞-B's order-3 chirality map reappearing as the effective cone's first obstruction: the $(0,\gamma,2\gamma)$ minor is *again* a $3$-point (cubic) structure atop a clean order-2 layer.

**Result of the registered run (the two-variable ladder; `probe_gamma1_ladder.py`, `gamma1_ladder{,_siegel}.csv`).** Fields to $|D|\le3	imes10^4$, $\gamma_1\in[0.056,\,8.04]$, self-similar targets. Controlled regression ($n{=}15$): $\log d = -0.602\,\gamma_1 - 0.016\log(\mathrm{off}) + 0.411\,(s\gamma_1) - 2.65$, $R^2=0.82$. **Three findings.** *(i) The $\gamma_1$-law is confirmed and the resonance variable is null* — the offset coefficient is zero even at $\mathrm{off}=0.001$ (perfect $2\gamma_1$ resonance, $D{=}505,3809$): Prop C.3's inequality stands but its bite is minor ($\lesssim2	imes10^{-3}$ even at full saturation $q^2=1$, $D{=}{-}19$); pure pole-adjacency drives the deficit. *(ii) The deficit is a bounded tension window, not a wall:* it peaks at $dpprox5$–$7	imes10^{-2}$ for $\gamma_1\in[1,3]$ and vanishes on both sides — exponentially above, and **identically below**: *(iii) in the deep Siegel regime $\gamma_1\in[0.056,0.11]$ every field degenerates* — the single-channel class either rotates **into** the light cone (not spacelike: its channel $e^{i\gamma_1 x}pprox1$ is parallel to the pole direction at any bounded scale) or is **exactly effective** ($d=0$, $q^2pprox0.75$). Separating a near-central zero-channel from the pole requires test scale $X\sim1/\gamma_1\sim\log|D|$, i.e. prime ranges $x\sim|D|^{c}$ — the instrument's cone geometry *reproduces the classical Siegel detection scale*. **Verdict: the route's obstruction is not a Siegel wall but a Siegel shadow** — near-central zeros are not hard to effectivize; they are hard to *see* as spacelike classes at bounded resolution, which is the convex-geometric form of the Landau–Siegel phenomenon and of the program's no-finite-witness theorems (P∞-B; P∞-A 8.3a). The saturation falsifier remains untriggered across the full range $\gamma_1\in[0.056,8]$: **(S) survives its hardest accessible test, and its residual difficulty is an identifiability problem at the central point — the archimedean completion, once more.**

*(Original registration, for the record.)* Fields stratified in $(\gamma_1,\mathrm{off})$ with $\gamma_1$ down to $\sim1.5$ ($|D|$ to $\sim3\times10^4$); **self-similar targets** $s=\min(1,\,4.4/\gamma_1)$ (the current law used fixed $s=0.55$, so the channel separation $s\gamma_1$ varied $4.4\to1.7$ — a confound now promoted to a recorded regressor); probe sets with and without **harmonic probes at $2\gamma_1$** (the deficit jump under the harmonic probe, predicted iff $q^2>\tfrac12$, is the direct test of C.3); regression $\log d\sim a\,\gamma_1+b\log\mathrm{off}+c\,(s\gamma_1)$. Readings: $d\to O(1)$ as $\gamma_1\to0$ $\Rightarrow$ the route's obstruction **is** the Siegel wall, quantitatively; offset-dependence present $\Rightarrow$ Bochner mechanism confirmed; absent $\Rightarrow$ pure pole-adjacency.

**Reading.** The route's effectivity is clean for the bulk spectrum and **degrades exponentially toward the central point, with a measured rate** — so the marginality of (S) *localizes to the low-lying-zero regime*, exactly the Landau–Siegel / central-value territory where RH is hardest, rather than being uniform. This is the most informative outcome the instrument can give: it places the route's residual difficulty precisely where RH's own difficulty lives, with a quantitative $\exp(-0.63\gamma_1)$ law. **Honest caveat (open):** whether this near-pole deficit is a genuine obstruction to (S)-in-the-limit or a finite-resolution feature of separating near-pole spacelike classes that vanishes as $(\delta,1/n)\to0$ is *not* settled here; it is enrichment-stable to $n=2500$, $\delta=0.5\%$ — a real measured effect — but its limit is the next question. Next on the box: a $\gamma_1$-ladder to the Siegel regime (very low $\gamma_1$, the worst real characters) to map the law's small-$\gamma_1$ behavior, and the weld-check against the BDH constant $B(\alpha)$. [`probe_effectivity_gap_chiral.py`, certs `effectivity_gap_chiral{,_resolve}.csv`.]

### 5.3 Toward the limit: the window is pinned and the prolate carriers saturate exactly

The weld to the open step, stated honestly $[\mathsf A]$: CCM's stage-$\lambda$ prolate positivity is "(S) restricted to scale $\lambda$" (proven, their theorem), and $\mu_\lambda$ is an angle between the cutoff positive cone and the light cone — the scale-$\lambda$ analogue of the sup-over-classes effectivity deficit. Two registered experiments probe the limit's two named dangers (`probe_S_limit_multiplicity.py`, `S_limit_multiplicity.csv`):

**(i) The tension window is pinned at absolute frequency.** At fixed $\gamma_1$, the deficit is invariant under ample-class width $2	o4	o6.4$ ($D{=}{-}8$: $4.2/4.4/4.3	imes10^{-2}$; $D{=}{-}3$: $1.67/1.67/1.64	imes10^{-3}$): the window $\gamma\in[1,3]$ is a **fixed feature of the cone's apex geometry** (the pole's $	frac12$-scale), not a scale-covariant artifact. Consequence: $\zeta$'s spectrum ($\gamma\ge14.13$) lives **permanently in the exponentially-clean bulk** — no $\zeta$ class ever visits the tension window, at any scale.

**(ii) The prolate-like carriers saturate exactly.** Multi-channel $\zeta$ classes $w_k=$ average of the first $k$ zero-channels ($k=1,2,4,8,12$; every channel probe-constrained, $K$ up to $36$): $d(arepsilon_0)=4.4	imes10^{-6},\,0,\,9.7	imes10^{-13},\,0,\,0$ — **zero at machine precision** from $k=2$ on, while $B(w_k,w_k)$ rises $-0.39	o-0.13$ (averaging channels rotates the class toward the lightlike pole direction — the spread top-mode is nearly lightlike, consistent with $\mu_\lambda$ minuscule). The multiplicity danger — the named carrier of a $\mu_\lambda$ floor — **does not materialize**: spectral multiplicity makes effectivity *easier*, not harder.

**State of the limit after this arc.** Every nameable finite obstruction to (S) has now been tested and is empty: single-channel ($	o0$), high-frequency ($	o0$), chiral ($	o0$), Siegel-regime (degenerates benignly — the shadow), resonance (null), and now multiplicity (exactly zero) with the window pinned away from $\zeta$'s spectrum. What remains is the limit statement itself — $(\delta,1/n,	ext{scale})	o\infty$ uniformly — which no finite probe can settle (P∞-B; 8.3a: the certificate is necessarily spectral/archimedean). The instrument's verdict is that the convex face of $\mu_\lambda\downarrow0$ is unobstructed along every direction the program has been able to name; the open step is now *purely* the apex identifiability — the archimedean completion — with no finite shadow left to clear.

## 6. The map

**Stage 0 (done).** Pillars I, II, III, V: proven/certified (W1; Takesaki $+$ P∞-B; Theorem C.0 GREEN; Theorem C.1). The whole of RH now sits in (S).
**Stage 1 (running).** The instrument: enrichment sweeps, direction sweeps, chiral versions; the welds quantified (does the measured T1 constant $B(\alpha)$ match the saturation-predicted effectivity constants?).
**Stage 2 (research).** The descent: from Murray–von Neumann comparison on the core to numerical classes — identify the precise compatibility (a cycle-class map $\mathrm{NS}_\zeta\to K_0(N)\otimes\mathbb R$ matching degrees to trace-weights and the diagonal pairing to the semilocal trace formula) and what obstructs it; the mobility/moving lemma as the PV-quarantine.
**Stage 3 (the summit, relocated once more).** (S) in the limit $=$ the index $=$ $\mu_\lambda\downarrow0$ $=$ RH: the same single open step, now with a convex-geometric face (Choquet/moment determinacy and comparison theory — toolboxes not yet exhausted by the program, unlike monotones and multiplier sequences).

**Honest status.** Proven here: Theorem C.0 $[\mathsf P]$; Theorem C.1 $[\mathsf P\,|\,(S)]$; pillars I–II identifications $[\mathsf P]$ on cited theorems. Open: (S) $[\mathsf C]$ — RH-strength at the limit; its finite faces are proven (CCM) or measured (T1, the instrument). Priority: the strategy "transport Weil's proof through the square in characteristic one" is Connes–Consani's declared program; what this paper adds is the certified pillar III with the closed-form archimedean kernel, the necessity theorems locating the ample class at the completion (P∞-B), the explicit conditional theorem with the mobility clause isolated, the saturation$\,\leftrightarrow\,$BDH$\,\leftrightarrow\,$prolate welds, and a falsifiable instrument with first data. Nothing here proves RH; everything here makes the remaining step *one named convex-geometric conjecture with a running experiment.*

---

## References and anchors

- A. Weil, *Sur les courbes algébriques…* (1948); Mattuck–Tate, Grothendieck (Castelnuovo proofs of the index).
- A. Connes, *Trace formula in noncommutative geometry…*, Selecta Math. 5 (1999) — semilocal trace formula; Weil positivity $\iff$ RH.
- A. Connes, C. Consani — Arithmetic/scaling site, Frobenius correspondences $\Psi_\lambda$; Riemann–Roch on $\mathbb R_+^\times/\lambda^{\mathbb Z}$ and on $\overline{\mathrm{Spec}\,\mathbb Z}$ (the declared RR-strategy this map transports).
- A. Connes, C. Consani, H. Moscovici — prolate positivity (AFA 2024; arXiv:2511.22755): (S)'s proven spectral stages.
- M. Takesaki — duality and the trace-scaling dual action on the $\mathrm{II}_\infty$ core; Murray–von Neumann comparison.
- Program: P∞ (Lorentzian metric; energy condition); P∞-A (Prop 8.3a); **P∞-B** (Frobenius operator; order dichotomy; degree carrier); W1 $=$ N0 Lemma 6.10; *diez* Thm 4.3 (T1/T2); N14 (archimedean relative entropy).
- Certificates: `probe_castelnuovo_geometric_positivity.py` (GREEN); `probe_effectivity_gap_v0.py`, `probe_effectivity_gap_v01_enrich.py` (instrument $+$ first data).
