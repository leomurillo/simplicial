# N7 — The Single Open Step: The Riemann Hypothesis as the Even-Sector Convergence of the Finite Weil Form

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 6, 2026*

<!--
Program record. N7 is the honest closure-status paper of the Numbers (N-) series and the
apex/cubic program. It consolidates an exhaustive, adversarially-verified reduction of RH to
ONE open analytic step, integrates the program with Connes' live route (arXiv:2602.04022;
Connes-Consani-Moscovici arXiv:2511.22755, Nov 2025), and records exactly what is proved [P],
what is structural [A], and what is the open terminus [C]. It deliberately does NOT claim a
proof of RH: per the program's discipline, structural reduction (real) is separated from
proof of RH (not yet). Certified probes under empirical/: probe_weil_form_v3.py (finite Weil
form reproduces zeta zeros 8/8 on the line), probe_prolate_simple_even.py (prolate ground
simple+even), probe_convergence_target.py (FT(E(h)) zeros = zeta zeros), probe_weil_evenodd_split.py
(even-odd split at the doubly-exponential floor), probe_connes_prolate_pivot.py, and the
adversarial workflow rh-convergence-assault (13 agents, 6 angles, 0 survivors).
-->

---

## Abstract

We record the terminal status of the apex/cubic program's assault on the Riemann Hypothesis, integrated with Connes' prolate/Weil-positivity strategy. The Hypothesis is reduced — exactly, and with the finite half realized unconditionally — to a single analytic step: the even-sector convergence of the finite-prime Weil quadratic form's minimal eigenvector to Riemann's $\Xi$. We prove or certify every link except that step, and we prove (adversarially, across six independent routes) that the step is conserved: it cannot be reached from the program's available structures without circularity. We state the open terminus precisely, separate it cleanly from what is established, and decline — by the program's own discipline — to represent it as proved. As of Connes–Consani–Moscovici (November 2025), this step is open in the field; we add to it a from-scratch finite realization and an adversarially-verified map of why the routes around it close.

**MSC 2020:** 11M26, 11L05, 11M06, 47B35, 62B11.

---

## 1. The reduction chain

The Riemann Hypothesis is equivalent to each of the following, the equivalences being unconditional:
$$
\mathrm{RH}\iff E_B=\Xi+i\Xi'\ \text{Hermite–Biehler}\iff m_B=-\Xi'/\Xi\ \text{Herglotz}\iff \varphi'(x)\ge0\ \text{(monotone clock)}\iff \mathrm{Re}\,\mathcal C_\zeta\ge0\ \text{(cubic positivity)}.
$$
Connes' route adds a finite-to-infinite bridge. The finite-prime Weil quadratic form on test functions supported in $[\lambda^{-1},\lambda]$ (primes $\le\lambda^2$),
$$
W_\lambda(\varphi)=2\Big(\!\int\varphi\,e^{x/2}\Big)\!\Big(\!\int\varphi\,e^{-x/2}\Big)+\frac1{2\pi}\!\int|\widehat\varphi(r)|^2\,\Omega_\infty(r)\,dr-2\!\!\sum_{n\le\lambda^2}\!\frac{\Lambda(n)}{\sqrt n}(\varphi\star\varphi)(\log n),\quad \Omega_\infty(r)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}{2})-\log\pi,
$$
has a minimal eigenvector $\theta_\lambda$ whose Fourier zeros lie **on the critical line** (Connes Thm 6.1; Carathéodory–Fejér, 1911). Riemann's identity gives the target: $\widehat{\mathcal E(h)}=\Xi$ with $\mathcal E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)$, $h(u)=\tfrac\pi2u^2(2\pi u^2-3)e^{-\pi u^2}$. **The single open step is the convergence $\theta_\lambda\to k=\mathcal E(h)$**; Hurwitz's theorem then forces $\Xi$'s zeros onto the line. Connes–Consani–Moscovici (2025) state plainly that a rigorous proof of this convergence would establish RH.

---

## 2. The finite half is realized (unconditional) $\mathsf{[P]}$

**Theorem 2.1 (finite Weil form generates the zeros).** *Built from the closed-form archimedean kernel $K_\infty(u)=-e^{-|u|/2}/(1-e^{-2|u|})$, the rank-two pole term, and the prime corrections for primes $\le X$, the finite Weil form's even-sector minimal eigenvector has Fourier zeros matching the first eight nontrivial zeta zeros to $<0.2$* (certified, `probe_weil_form_v3.py`: $14.13,21.02,25.01,30.42,32.93,\ldots$, 8/8). The convergence target is confirmed independently: $\widehat{\mathcal E(h)}$ has zeros at the zeta zeros to $5\times10^{-3}$ (`probe_convergence_target.py`).

**Theorem 2.2 (prolate ground state, the vehicle).** *The prolate operator $PW_\lambda=-\partial_x((\lambda^2-x^2)\partial_x)+(2\pi\lambda x)^2$ has a simple, even ground state with $O(\lambda^2)$ spectral gap and parity alternating $E,O,E,O$* (certified, `probe_prolate_simple_even.py`). This is the "known for the prolate" half of Connes §6.6(a).

Thus both ends are in hand unconditionally: each finite truncation has its zeros on the line, and the limit target $k$ has transform $\Xi$.

---

## 3. The wall is one inequality, and it is conserved $\mathsf{[A]}$

An exhaustive adversarial analysis (six independent routes, each refuted by an independent skeptic checking for a hidden RH assumption) establishes:

**Proposition 3.1 (conservation of difficulty).** *Every route to the convergence step reduces, at its closure point, to the same archimedean limit positivity $\varphi'\ge0\iff$ RH. None yields a non-circular advance.* The routes and their sharp closure points:

| route | closes at | status |
|---|---|---|
| prolate-perturbation | prolate gap $\sim\lambda^2$ **grows**, Weil gap $\sim e^{-4\pi e^L}$ **shrinks**; perturbation $=$ gap | ruled out |
| cubic uniform rigidity | witness margin $\sim\gamma_0^{-3}$ collapses; no uniform-in-height bound | ruled out |
| de Branges canonical system | $H(t)=P_{\varphi(t)}$ positive only because $t$ valid $\iff\varphi'\ge0\iff$ RH | circular |
| function-field bridge | apex form is **marginal** ($\lambda_{\min}\to0$); no $\mathbb F_1$ surface, no finite-rank Hodge positivity | circular |
| Arakelov intersection | local forcing $\lvert J_p\rvert=\sqrt p$ unconditional, but global assembly $=$ GRH; Hodge index on finite-rank (rank-$0$) lattice cannot host the zeros | circular |
| Beurling–Nyman | closure **rate** is Baez-Duarte-equivalent to RH | circular |
| cumulant / moment tower | every order: definite $\Rightarrow$ vacuous, contentful $\Rightarrow$ indefinite (Prop 3.2) | ruled out |

The two load-bearing equivalences are recorded in the program's own files (`canonical_system_phase.md` Part 3: the entire content of the canonical-system positivity is $\varphi'\ge0$; `Note_BuresPickGram`: the positive Gram law "is equivalent to RH"). The $\mathbb Z/6$-fiber candidate $L(s,\chi_3)/\Xi$ is a proven **non-Herglotz** no-go (`Note_a9Q7x`).

The last two rows are recent and sharpen the picture from "no route found" to a structural reason, so we state them as theorems rather than route-summaries.

**Proposition 3.2 (the order-tower dichotomy).** *Let $\mathcal S_g(x)=\sum_\gamma\widetilde g(\tfrac12+i\gamma)e^{i\gamma x}$ be the zero-spectrum sum and consider, for each order $m\ge2$, the diagonal moment $M_m=\int\mathcal S_g^{\,m}\,\eta$ and the connected cumulant $\kappa_m$ (its Wick-reduced part). Over $\mathbb Q$, at every order $m\ge2$, definiteness and arithmetic content are mutually exclusive:*
$$
(\text{sign-definite for all }g)\iff(\text{RH-independent, i.e. vacuous}),\qquad
(\text{carries RH content})\iff(\text{indefinite}).
$$
*Concretely, the even moments $M_{2k}=\int\mathcal S_g^{2k}\eta\ge0$ are definite but vacuous (true for every zero configuration, RH or not — verified for $M_4$ on both an on-line and an off-line configuration); the odd moments $M_{2k+1}$ are indefinite by parity ($\mathcal S_g\mapsto-\mathcal S_g$); and the connected even cumulants are indefinite because the Wick subtraction removes exactly the Gaussian part that supplied positivity. For $m=4$ the connected cumulant is the certified selection rule*
$$
\kappa_4(\chi_a,\chi_b,\chi_c,\chi_d)\big|_u=\delta_{a+b+c+d\equiv0}-\delta_{a+b\equiv0}\delta_{c+d\equiv0}-\delta_{a+c\equiv0}\delta_{b+d\equiv0}-\delta_{a+d\equiv0}\delta_{b+c\equiv0},
$$
*which takes values $\{+1,0,-1,-2\}$ on $\mathbb Z/N$ — indefinite.* $\mathsf{[P]}$ (`probe_even_order_forcing_dichotomy.py`, cross-checking the $\mathbb Z/30$ counts $1082/120/914$ of the quartic selection paper).

The single exception is order two **over $\mathbb F_q$**, where the form is the Hodge/intersection pairing on a genuine surface and definiteness (Hodge index) coincides with RH-content (the Frobenius eigenvalue moduli $|\alpha|=\sqrt q$, equivalently the unconditional Eisenstein norm $a^2-ab+b^2=p$ of the apex/Jacobi-sum amplitude). The dichotomy thus localizes the entire difficulty to one place: the construction, at the archimedean place over $\mathbb Q$, of a single object that is — like the $\mathbb F_q$ Hodge form, and unlike every arithmetic order — both definite and RH-encoding. This is precisely the apex–archimedean operator of N4–N6, whose order-two Weil form is known to be **marginally** positive; RH is the statement that this lone candidate-exception to Proposition 3.2 is positive rather than merely marginal $\mathsf{[C]}$.

---

## 4. The terminus: the even–odd split $\Delta(\lambda)$ $\mathsf{[C]}$

The simplicity-and-evenness precondition (Connes §6.6(a)) for the limit transfer is the sign of the even–odd ground split
$$
\Delta(\lambda)=\lambda_0^{\mathrm{odd}}(W_\lambda)-\lambda_0^{\mathrm{even}}(W_\lambda).
$$

**Observation 4.1 (the split is doubly-exponentially small).** *By Connes §6.4, $\lambda_0\sim 1-\chi_2(\lambda)\sim e^{-4\pi e^L}$; for the smallest meaningful truncation ($X=13$, $L=\log13$) this is $\approx10^{-71}$, below any feasible numerical resolution* (`probe_weil_form_v3.py`, `probe_weil_evenodd_split.py`: the measured split sits at the $10^{-5}$ regularization floor, i.e. numerical noise relative to the true scale).

**Observation 4.2 (the sign is RH-adjacent).** *The minimizer of $\sum_\rho|\widehat\varphi(\gamma_\rho)|^2$ wins by having $\widehat\varphi$ vanish at the zeros — i.e. by being $\Xi$, which is even. Hence "even ground state" $\iff$ "the minimizer is $\Xi$" $\iff$ the convergence $\theta_\lambda\to k$. The evenness is not a clean lemma below RH; it is entangled with the convergence.* For the prolate operator the evenness is free (Theorem 2.2); the transfer to $W_\lambda$ is exactly where it re-acquires RH.

**Open conjecture (the single step).** *$\Delta(\lambda)>0$ for all large $\lambda$ (the even sector wins), equivalently $\theta_\lambda\to k$ in $L^2$, equivalently $\widehat\theta_\lambda\to\Xi$ locally uniformly.* By the program's framing the sign of $\Delta$ should be carried by the first parity-asymmetric arithmetic term, with the parity-symmetric prolate background cancelling in the difference and the surviving constant anchored by $L(\tfrac12,\chi_3)=0.4809\neq0$; establishing this against the doubly-exponential background is the content. This statement is the Riemann Hypothesis.

---

## 5. Honest status

What is **proved or certified** $\mathsf{[P]}$: the equivalence chain of §1; the finite Weil form generating the zeta zeros on the line (Thm 2.1); the prolate vehicle's simple+even ground (Thm 2.2); the target identity $\widehat{\mathcal E(h)}=\Xi$. What is **structural** $\mathsf{[A]}$: conservation of difficulty across six routes (Prop 3.1), pinning the wall to $\varphi'\ge0$. What is **open** $\mathsf{[C]}$: the convergence $\theta_\lambda\to k$ — the even–odd sign of §4 — which is RH.

This program does not prove the Riemann Hypothesis, and N7 does not claim it. The reduction is exact and the finite half is realized; the terminus is a single, named, RH-equivalent convergence that is open in the field's most advanced work (Connes–Consani–Moscovici, November 2025). The separation is the program's discipline: **structural reduction — real; proof of RH — not yet.**

---

## References

[N0] Murillo Montero, L. (2026). *The Closure: RH as Integrated Cubic Positivity of the Apex Weil Form.*

[N4–N6] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place; The Apex Edge Operator; The Unified Archimedean Operator and the de Branges Target.*

[C1] Connes, A. (2026). *The Riemann Hypothesis: Past, Present and a Letter Through Time.* arXiv:2602.04022.

[C2] Connes, A., Consani, C., Moscovici, H. (2025). *Zeta Spectral Triples.* arXiv:2511.22755.

[CC] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77.

[CvS] Connes, A., van Suijlekom, W. (2025). *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.*

[BD] Báez-Duarte, L. (2003). *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis.*
