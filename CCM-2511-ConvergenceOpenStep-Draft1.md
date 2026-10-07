# The CCM Convergence, Pressed to its Source — the Open Step Sharpened (and a Correction)

**Scope.** Returning to the object every side-route (modular §8, Kloosterman/MR) provably terminates at: the CCM prolate→ζ convergence. Anchored to the actual paper — Connes–Consani–Moscovici, *Zeta Spectral Triples* (arXiv:2511.22755), fetched 2026-06-08. (Theorem/lemma numbers via the paper text; verify against the PDF before formal citation.) **Outcome: the open step is sharper and more concentrated than the program recorded — and one program-memory claim is corrected.**

---

## 1. The open step, from the source

Three facts from 2511.22755, in the order that matters:

- **[PROVEN — Thm 5.10(iii)]** For each fixed $(\lambda,N)$, the finite approximant $\widehat{\xi}^{\,\lambda,N}(z)$ is **entire with all zeros real**, coinciding with the spectrum of the self-adjoint $D_{\log}^{\lambda,N}$. The reality is proven via the **Carathéodory–Fejér** theorem (Lemmas 5.2, 5.4) and self-adjointness (Thm 5.10(i)). *So the approximants are already Hermite–Biehler / Laguerre–Pólya — the positivity of the finite objects is not in question.*
- **[CONJECTURAL — §7]** $\widehat\xi^{\,\lambda}(z)$, suitably normalized ($\times\,e^{a+ibz}$), **converges uniformly on closed substrips of $\{\Im(z)<\tfrac12\}$ to the Riemann $\Xi$-function** as $\lambda\to\infty$. "Establishing this convergence rigorously would amount to a proof of the Riemann Hypothesis."
- **[THE OBSTACLE — Lemma 7.2]** the eigenfunction estimate $\max_x|h_{n,\lambda}(x)-h_n(x)|\le c\,\lambda^{-2}$ ($n=0,4$) for the prolate wave operator $PW_\lambda$ (from "Satz 9 of [9]"). *"Justifying rigorously this step is the main remaining obstacle to our approach to RH."*

**The cleanest equivalent form — Cor 3.8.** $\mu_\lambda$ (the smallest eigenvalue of the perturbation operator $A_\lambda$) is a **decreasing** function of $\lambda$, and
$$\lim_{\lambda\to\infty}\mu_\lambda=0\ \Longrightarrow\ \mathrm{RH}.$$

**Net.** The Hurwitz route is *fully assembled*: finite approximants have all-real zeros (proven), they converge to $\Xi$ on substrips of $\{\Im z<\tfrac12\}$, and uniform-on-compacts convergence + all-real-zeros $\Rightarrow$ (Hurwitz/Laguerre–Pólya is closed under locally uniform limits) $\Xi$ all-real-zeros $=$ RH. **The entire RH-content is concentrated in a single $O(\lambda^{-2})$ eigenfunction-approximation estimate (Lemma 7.2), equivalently in one scalar limit $\mu_\lambda\downarrow0$ (Cor 3.8).**

## 2. Correction to the program record

- The program memory carried "§6.5 prolate convergence $\widehat k_\lambda\to\Xi$ **unconditional**." That belongs to the *finite-prime Weil object* of the Connes **2602.04022 *Letter***, a different paper. In **2511.22755** the determinant→$\Xi$ convergence is **conjectural** — its rigorous proof *is* RH. Keep the two papers distinct.
- What *is* unconditional in 2511.22755 is the **finite-approximant positivity** (all-real-zeros, Thm 5.10(iii), via Carathéodory–Fejér) — *not* the limit. So the gap is **(a) the convergence mode (Lemma 7.2)**, definitively **not (b) the approximants' Hermite–Biehler-ness** (that is proven). My earlier uncertainty (a)-vs-(b) is resolved by the source: **(a)**.

## 3. What this session's machinery adds (characterization, not a crack)

1. **Carathéodory–Fejér $=$ Nevanlinna–Pick.** CCM's positivity tool (Thm 5.10(iii)) and Pinf-A §5's Pick-matrix positivity (with the Kreĭn–Langer index $=$ #off-line zeros) are the **two dual faces of the same truncated moment-problem positivity**. So CCM's "approximants all-real-zeros" $=$ "finite Pick PSD / Kreĭn–Langer index $0$", and the open step **$\mu_\lambda\downarrow0$ $=$ the Kreĭn–Langer index stays $0$ in the limit** — a new, exact entry in the program's equivalent-faces stack, welding CCM to Pinf-A.
2. **$\mu_\lambda\downarrow0$ is the marginal-positivity face.** Via §8.4 (Borchers continuation $\Delta^{1/4}U(s)=e^{-sP}\Delta^{1/4}$): positive energy $=$ "$e^{-sP}$ bounded" $=$ $\mu_\infty=0$. Via §8.7: the margin is **pole-driven** (pole $\approx+2$, archimedean and prime both subtractive), so $\mu_\lambda\to0$ is a **small difference of large terms** (pole vs arch$+$prime) — the cancellation that makes the $O(\lambda^{-2})$ rate hard, and the precise reason the limit value (0 vs $>0$) is delicate.
3. **CCM supplies the monotone that de Bruijn–Newman lacked.** The program recorded "no $\Lambda\le0$ monotone." But $\mu_\lambda$ **is** monotone (decreasing), with $\mu_\lambda\downarrow0\iff$ RH. The "no monotone" obstruction is thereby *reframed*: a monotone exists (Cor 3.8); the open question is not its *existence* or *sign* but its *limit value* — i.e. the $O(\lambda^{-2})$ rate of Lemma 7.2.

## 4. Two-directional structural confirmation (the session's main deposit)

Independently of CCM, this session showed **both** routes to RH terminate at exactly this object, and by a **structural** argument (not just the empirical convergence-assault):

- **Direction A (operator-algebra/modular, §8).** Every modular handle (Borchers/+hsm, nuclearity) reduces to $e^{-sP}$ bounded $=$ positive energy, and the **Faltings–Hriljac guillotine** (an unconditional structure cannot supply RH-content) blocks closure — leaving exactly $\mu_\lambda\downarrow0$.
- **Direction B (Kloosterman/level, Pascadi+MR).** The primorial-BV tail needs the bilinear saving $\eta(n)\to\tfrac12$ *growing with $n$*; savings don't compound; unconditional tools cap at bounded $n$ — same guillotine, same residual.

So the localization is no longer "we tried and failed" but "**no unconditional lever from either direction can close it, and both walls are the single object $\mu_\lambda\downarrow0$ / Lemma 7.2.**"

## 5. Honest verdict

This session **does not crack Lemma 7.2.** That estimate is a prolate-spheroidal eigenfunction asymptotic — the "prolate-perturbation" angle the 2026 convergence-assault already ruled out as a route. The contribution here is:
- the **correction** (convergence conjectural; approximant-positivity proven; gap is the mode);
- the **sharpest form** (RH $\iff\mu_\lambda\downarrow0$, one decreasing scalar $\iff$ one $O(\lambda^{-2})$ estimate);
- the **CF$=$Pick unification** (CCM ↔ Pinf-A, Kreĭn–Langer index in the limit);
- the **monotone reframe** (CCM's $\mu_\lambda$ is the de Bruijn–Newman-type monotone, limit-value open);
- the **two-directional structural confirmation**.

**The RH-content is now pinned to a single inequality: $\mu_\lambda=O(\lambda^{-2})$ (Lemma 7.2).** Everything else (positivity of approximants, Hurwitz transfer, the equivalence to arch-domination / positive-energy / level-tail) is settled or structural. That is the cleanest the open step has been stated — and the honest place to stop, absent a genuinely new analytic idea for the prolate eigenfunction rate.

---

**Anchors.** Connes–Consani–Moscovici, *Zeta Spectral Triples* (arXiv:2511.22755): Thm 5.10(i),(iii), Cor 3.8, Lemma 7.2, §7; Lemmas 5.2/5.4 (Carathéodory–Fejér). Distinct: Connes, *Letter* (2602.04022, finite-prime). Program: Pinf-A §5 (Pick/Kreĭn–Langer), §8.4 (Borchers continuation), §8.7 (pole-driven margin); RH-proof-path anchor; convergence-assault (negative, 2026-06); `empirical/connes_route/` (numerical $\mu_\lambda\to0$, primes $\le13\to$ zeros).
