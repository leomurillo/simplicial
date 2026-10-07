# CCM Lemma 7.2 (prolate eigenfunction rate): derived, verified — and not the real obstacle

**Task.** Attempt the analytic estimate behind CCM 2511.22755 Lemma 7.2 — $\max_x|h_{n,\lambda}(x)-h_n(x)|\le c\,\lambda^{-2}$ for the prolate wave operator — as a prolate-spheroidal perturbation problem. **Outcome:** the rate is **derived from harmonic-oscillator perturbation theory and verified numerically to $p=-2.00$** (`empirical/probe_prolate_eigenfunction_rate.py`); and this *relocates* the genuine obstacle — it is **not** the eigenfunction rate (classical) but the **variational arch-vs-prime balance on the prolate trial vector** ($=$ the §8.7 pole-driven margin $=$ RH content).

---

## 1. The rate is the first harmonic-oscillator order (derived)

CCM's operator (eq. 7.5): $PW_\lambda=-\partial_x\big((\lambda^2-x^2)\partial_x\big)+(2\pi\lambda x)^2$ on $[-\lambda,\lambda]$. Rescale $x=\lambda u$ ($u\in[-1,1]$):
$$PW_\lambda=-\partial_u\big((1-u^2)\partial_u\big)+(2\pi\lambda^2)^2u^2=L_c,\qquad \boxed{c=2\pi\lambda^2}\ \ (\text{Slepian bandwidth}).$$
So $c\sim\lambda^2$. Pass to the oscillator variable $t=\sqrt c\,u$ (the concentration scale of the low eigenfunctions):
$$\frac{L_c}{c}= \underbrace{(-\partial_t^2+t^2)}_{H_{\mathrm{osc}}}\;+\;\frac1c\,\underbrace{\partial_t(t^2\partial_t)}_{W}\;,\qquad W=t^2\partial_t^2+2t\partial_t\ (\preceq0).$$
This is the harmonic oscillator plus a **$1/c$ perturbation**. First-order eigenvector perturbation theory gives, for each fixed $n$,
$$h_{n,\lambda}=h_n+\frac1c\,h_n^{(1)}+O(c^{-2}),\qquad h_n^{(1)}=\sum_{m\ne n}\frac{\langle m|W|n\rangle}{2(n-m)}\,h_m,$$
so $\|h_{n,\lambda}-h_n\|=O(1/c)=O(\lambda^{-2})$. **The $\lambda^{-2}$ of Lemma 7.2 is $1/c$ — the first anharmonic correction.** $\;\blacksquare$ (derivation)

*Reconciliation with Meixner–Schäfke [9] "Satz 9" ($O(\gamma^{-3/4})$, uniform on $[-1,1]$):* MS's weaker rate is the **boundary / turning-point** regime ($|u|\to1$, $|t|\to\sqrt c$), where the oscillator reduction fails — but there the eigenfunctions are amplitude $\sim e^{-c/2}$ (astronomically small), so the **bulk** $\lambda^{-2}$ dominates any mass-weighted norm. The two are consistent, not in conflict.

## 2. Verified numerically (rate $p=-2.00$, constant pinned)

`probe_prolate_eigenfunction_rate.py` discretizes $M(c)=H_{\mathrm{osc}}+\tfrac1cW$ and compares $h_{n,\lambda}$ (finite $c$) to $h_n$ ($c=\infty$, pure $H_{\mathrm{osc}}$) **on the same grid** (so discretization bias cancels and only the $1/c$ effect remains). Over $\lambda=6\ldots32$ (valid range $\sqrt c>T$):

| $n$ | fitted $p$ in $\mathrm{err}\sim\lambda^{p}$ | $\mathrm{err}\cdot c$ constancy |
|---|---|---|
| $0$ | $-2.004$ | $0.22\%$ |
| $2$ | $-2.007$ | $0.40\%$ |
| $4$ | $-2.010$ | $0.58\%$ |

$\mathrm{err}\cdot c$ is constant to $<1\%$ — i.e. $\mathrm{err}=A_n/c=A_n/(2\pi)\cdot\lambda^{-2}$ exactly. **The Lemma-7.2 rate is confirmed $\lambda^{-2}$, classical, and quantitatively pinned.** (The $\lambda=4$ point fails only because $\sqrt c<T$ there — the $(1/c)W$ expansion's validity needs $|t|<\sqrt c$; a discretization artifact, not a rate effect.)

## 3. So the rate is NOT the obstacle — the obstacle is the variational balance

CCM's own statement (§7) locates the obstacle at **propagating** the eigenfunction estimate to $\mu_\lambda\to0$ (not the estimate itself). Make this precise. $\mu_\lambda=\inf\mathrm{spec}\,A_\lambda$ (Weil-form operator, Cor 3.7), decreasing, and $\mu_\lambda\to0\Rightarrow$ RH (Cor 3.8). The prolate "educated guess" $k_\lambda=E(h_\lambda)$ is a **trial vector**, giving the variational upper bound
$$\mu_\lambda\ \le\ \frac{\langle k_\lambda,\,A_\lambda\,k_\lambda\rangle}{\langle k_\lambda,k_\lambda\rangle}.$$
By the explicit formula, $\langle k_\lambda,A_\lambda k_\lambda\rangle$ is the **Weil functional on the prolate test function** — i.e. (pole) $+$ (archimedean) $-$ (prime), evaluated on $k_\lambda$. **This is exactly the §8.7 object** (heat-trace $=$ Cramér $=$ pole $+$ arch $-$ prime), now on the prolate trial vector. So:
$$\mu_\lambda\to0\ \Longleftarrow\ \big[\text{Weil functional on the prolate }k_\lambda\big]\to0\ =\ \big[\text{archimedean energy of }k_\lambda\approx\text{prime energy of }k_\lambda\big].$$
**CCM's "$\mu_\lambda\to0$" is the §8.7 arch-domination / pole-driven margin, evaluated on the prolate trial vector.** And **Lemma 7.2's $\lambda^{-2}$ is the precision** needed to evaluate the *prime* part (the explicit-formula prime sum $\sum\Lambda(n)g_{k_\lambda}(\log n)$) on $k_\lambda$ accurately enough — which is why CCM need the eigenfunction estimate, but as an *input to the balance*, not as the obstacle itself.

## 4. Honest verdict

- **Settled this session [P]:** the Lemma-7.2 eigenfunction rate is $\lambda^{-2}=1/c$, the first harmonic-oscillator order — derived (HO reduction of $PW_\lambda$, $c=2\pi\lambda^2$) and verified ($p=-2.00$, $\mathrm{err}\cdot c$ const $<1\%$). The "Satz 9" classical content is demystified; the bulk rate is $\lambda^{-2}$ (MS's $\gamma^{-3/4}$ is the amplitude-negligible boundary).
- **Relocated:** the residual obstacle is **not** the rate. It is the **variational balance** $\langle k_\lambda,A_\lambda k_\lambda\rangle\to0$ — the archimedean and prime energies of the prolate trial vector cancelling in the limit. That balance is the §8.7 **pole-driven margin** ($=$ arch-domination $=$ Weil's criterion $=$ the irreducible RH content), now pinned to a specific test function.
- **Not closed:** this is the same RH content every face of the program reaches; the rate result does not move it. But two genuine deposits: **(a)** the eigenfunction rate is classical HO-PT (verified) — it can be removed from the list of "hard unknowns"; **(b)** CCM's $\mu_\lambda\to0$ is unified with the program's own §8.7/N14–N15 arch-domination at the level of the *explicit Weil functional on the prolate trial vector* — the operator thread (CCM) and the analytic thread (§8.7/Cramér) are the same computation on $k_\lambda$.

**Net.** Attempting the rate succeeded and clarified the landscape: the prolate eigenfunction asymptotics are tractable and done; what remains is, once again, the archimedean-vs-prime balance — now as concrete as "the Weil functional on the explicit prolate trial vector $k_\lambda$ tends to $0$," with the eigenfunction rate $\lambda^{-2}$ supplying the precision but not the difficulty.

---

**Anchors.** CCM 2511.22755 (eq. 7.5 $PW_\lambda$; Cor 3.7/3.8 $\mu_\lambda$; Lemma 7.2; §7; ref [9] Meixner–Schäfke, *Mathieusche Funktionen und Sphäroidfunktionen*, Satz 9 p.243). Probe `empirical/probe_prolate_eigenfunction_rate.py` (rate $p=-2.00$). Program: §8.7 (`Pinf-A`, heat-trace $=$ Cramér $=$ pole$+$arch$-$prime, pole-driven); N14/N15 (Weil positivity, arch-domination); `CCM-2511-ConvergenceOpenStep-Draft1.md` (the open step $\mu_\lambda\downarrow0$); `empirical/connes_route/` (numerical $\mu_\lambda\to0$).
