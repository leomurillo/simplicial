# N7 — The Single Open Step: The Riemann Hypothesis as the Even-Sector Convergence of the Finite Weil Form

**Leonardo Murillo Montero**

*Independent researcher*

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
2026-10-10: Section 5 added (Laguerre-Polya transport; the DH matched pair), certified by
empirical/connes_route/probe_lp_transport_zeta.py and probe_lp_transport_dh.py (shared exact
closed-form machinery lp_transport_core.py). Observations 4.1-4.2 and the open-step statement
corrected in place by its findings; the prolate row of Proposition 3.1 refined (Cor 5.5).
-->

---

## Abstract

We record the terminal status of the apex/cubic program's assault on the Riemann Hypothesis, integrated with Connes' prolate/Weil-positivity strategy. The Hypothesis is reduced — exactly, and with the finite half realized unconditionally — to a single analytic step: the even-sector convergence of the finite-prime Weil quadratic form's minimal eigenvector to Riemann's $\Xi$. We prove or certify every link except that step, and we show (adversarially, across six independent routes) that each of those routes closes at the same point, so none reaches the step from the program's available structures without circularity. We state the open terminus precisely, separate it cleanly from what is established, and decline — by the program's own discipline — to represent it as proved. As of Connes–Consani–Moscovici (November 2025), this step is open in the field; we add to it a from-scratch finite realization and an adversarially-verified map of why the routes around it close. Section 5 sharpens the step. Because the finite approximants are real-rooted, the Hadamard product controls their growth by one scalar, the log-variance $S(\lambda)$, so convergence is needed only on one real segment below the first zero, and the prolate proximity step needs only a logarithmic rate; we prove that a finite nonempty set of off-line zeros would force $S(\lambda)\to\infty$ along simple even ground states. Running the identical certified machinery on the Davenport–Heilbronn function, which shares the functional equation but has no Euler product, shows that evenness of the ground state carries no Riemann-Hypothesis content, while boundedness of $S$ does: off the Euler product the ground state leaves the bulk for the window edges.

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

**Theorem 2.2 (prolate ground state, the vehicle).** *The prolate operator $PW_\lambda=-\partial_x((\lambda^2-x^2)\partial_x)+(2\pi\lambda x)^2$ has a simple, even ground state with $O(\lambda^2)$ spectral gap and parity alternating $E,O,E,O$* (certified, `probe_prolate_simple_even.py`). This is the "known for the prolate" half of Connes [C1, Sect. 6.6(a)].

Thus both ends are in hand unconditionally: each finite truncation has its zeros on the line, and the limit target $k$ has transform $\Xi$.

---

## 3. Six routes, one closure point $\mathsf{[A]}$

An exhaustive adversarial analysis (six independent routes, each refuted by an independent skeptic checking for a hidden RH assumption) establishes:

**Proposition 3.1 (common closure point).** *Every route to the convergence step reduces, at its closure point, to the same archimedean limit positivity $\varphi'\ge0\iff$ RH. None yields a non-circular advance.* The routes and their sharp closure points:

| route | closes at | status |
|---|---|---|
| prolate-perturbation | prolate gap $\sim\lambda^2$ **grows**, Weil gap $\sim e^{-4\pi e^L}$ **shrinks**; perturbation $=$ gap | ruled out in operator norm; the trial-vector form is live (Corollary 5.5) |
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

The simplicity-and-evenness precondition (Connes [C1, Sect. 6.6(a)]) for the limit transfer is the sign of the even–odd ground split
$$
\Delta(\lambda)=\lambda_0^{\mathrm{odd}}(W_\lambda)-\lambda_0^{\mathrm{even}}(W_\lambda).
$$

**Observation 4.1 (the split is doubly-exponentially small in absolute terms, large in relative terms).** *The ground eigenvalue tracks the first self-dual prolate defect, $\varepsilon(\lambda)\approx c\,(1-\chi_4(\lambda))$ with $c\approx6$–$12$ ([N2], Prop. 4.3), so in absolute terms the split is doubly exponential in $L=2\log\lambda$. It is nevertheless resolved directly by the closed-form matrix of Section 5: $\varepsilon_{\rm even}=9.2\times10^{-13}$ against $\varepsilon_{\rm odd}=5.4\times10^{-10}$ at $\lambda=2$, and $4.0\times10^{-75}$ against $5.9\times10^{-71}$ at $\lambda=4$ (Table 5.1).* The relative split grows along the ladder. The earlier probes (`probe_weil_form_v3.py`, `probe_weil_evenodd_split.py`) sat at a $10^{-5}$ regularization floor; their reading that the split lies "below any feasible numerical resolution" is withdrawn.

**Observation 4.2 (the sign of the split is not the Riemann Hypothesis).** *We had argued that the minimizer of $\sum_\rho|\widehat\varphi(\gamma_\rho)|^2$ wins by being $\Xi$, which is even, so that "even ground state" $\iff$ "the minimizer is $\Xi$" $\iff$ RH. The matched pair of Section 5.5 refutes the first equivalence. The Davenport–Heilbronn form, whose function violates RH, has a simple even ground state at every window past its transition, and its ground-state transforms then have only real zeros (Observation 5.8). Evenness is the parity of the dominant mode. It is necessary for the Carathéodory–Fejér mechanism, but it does not carry the Hypothesis.*

**The open step, restated.** *The single step is the conjunction of (a), simple even ground states along a sequence $\lambda_j\to\infty$, with the interval convergence of Corollary 5.3; equivalently (a) with the spectral inequality of Corollary 5.5.* Either conjunction implies RH (Section 5). The converse is open as well: the CCM convergence is not known even assuming RH. The program's earlier framing, in which the sign of $\Delta$ is carried by the first parity-asymmetric term anchored by $L(\tfrac12,\chi_3)=0.4809$, survives only as a heuristic for (a); the Hypothesis itself sits in the normality of the approximant family (Theorems 5.2 and 5.6).

---

## 5. Laguerre–Pólya transport: the open step needs one interval, and the matched pair shows where it lives

Sections 2–4 locate the open step in the convergence $\widehat\theta_\lambda\to\Xi$. Connes–Consani–Moscovici [C2, Sect. 7–8] state the requirement as uniform convergence on closed substrips of $|\operatorname{Im}z|<\tfrac12$, which Hurwitz's theorem then transports to the zeros. This section shows that the requirement is far stronger than needed, isolates the one scalar that carries the content, and runs the identical machinery on a function with the same functional equation but no Euler product, to see which hypothesis fails when the Riemann Hypothesis does.

Throughout, $\lambda>1$, $L=2\log\lambda$, $QW_\lambda$ is the semilocal Weil form on $L^2([\lambda^{-1},\lambda],d^*u)$ (or its CCM truncation $QW_\lambda^N$ on $V_n$, $|n|\le N$), $\xi_\lambda$ its ground state, $\varepsilon(\lambda)$ its smallest eigenvalue, and $\widehat f(z)=\int f(u)u^{-iz}\,d^*u$. Hypothesis **(a)** is the first missing step of [C2, Sect. 8]: *the smallest eigenvalue is simple and its eigenvector even.* Under (a), $\widehat\xi_\lambda$ is an even entire function of exponential type whose zeros are all real ([CvS]; [C2, Thm 5.10(iii)] for $QW_\lambda^N$).

### 5.1 The transport theorem $\mathsf{[P]}$

Let $\mathcal L$ be the class of even real entire functions $F$ of genus at most one with only real zeros and $F(0)=1$. By Hadamard, $F(z)=\prod_k(1-z^2/a_k^2)$ over its positive zeros $a_1\le a_2\le\cdots$, and we write
$$
S(F)\;=\;\sum_k a_k^{-2}\;=\;-\tfrac12F''(0).
$$

**Lemma 5.1 (the Hadamard–Laguerre bounds).** *For $F\in\mathcal L$ with $S=S(F)$: (i) $|F(z)|\le e^{S|z|^2}$ for all $z\in\mathbb C$; (ii) for $0\le t<a_1$, $\;e^{-St^2/(1-t^2/a_1^2)}\le F(t)\le e^{-St^2}$.*

*Proof.* (i) $|1-z^2/a^2|\le1+|z|^2/a^2\le e^{|z|^2/a^2}$. (ii) For $x\in[0,1)$, $-x/(1-x)\le\log(1-x)\le-x$; apply with $x=t^2/a_k^2\le t^2/a_1^2$ and sum. $\square$

**Theorem 5.2 (Laguerre–Pólya transport).** *Let $F_j\in\mathcal L$ and suppose $F_j\to G$ uniformly on one real segment $[0,\eta]$, $\eta>0$, with $G$ continuous and positive there. Then:*

1. *$\limsup_j S(F_j)\le-\log G(\eta)/\eta^2$;*
2. *$\{F_j\}$ is a normal family on $\mathbb C$, and every locally uniform limit is an even entire function with only real zeros that agrees with $G$ on $[0,\eta]$;*
3. *if $G$ is the restriction of an entire function $\widehat G$, then $F_j\to\widehat G$ locally uniformly on $\mathbb C$, and $\widehat G$ has only real zeros.*

*Proof.* (1) Uniform convergence to a positive $G$ makes $F_j>0$ on $[0,\eta]$ for large $j$, so $a_1(F_j)>\eta$, and Lemma 5.1(ii) at $t=\eta$ gives $S(F_j)\le-\log F_j(\eta)/\eta^2\to-\log G(\eta)/\eta^2$. (2) Lemma 5.1(i) makes the family locally bounded; Montel gives normality. A limit $F$ satisfies $F(0)=1$, so $F\not\equiv0$, and by Hurwitz it has no zeros off $\mathbb R$, since the $F_j$ have none. (3) Every subsequential limit equals $\widehat G$ on $[0,\eta]$, hence everywhere; so the whole sequence converges to $\widehat G$. $\square$

The point of Theorem 5.2 is that for real-rooted families the *growth* control that Hurwitz needs is free: the single scalar $S$ supplies it, and $S$ is bounded as soon as the family converges at one real point below its first zero.

### 5.2 Consequences for the open step $\mathsf{[P]}$

**Corollary 5.3 (the second missing step, interval form).** *Suppose that along a sequence $\lambda_j\to\infty$ hypothesis (a) holds, $\widehat\xi_{\lambda_j}(0)\ne0$, and for some $\eta>0$*
$$
\frac{\widehat\xi_{\lambda_j}(t)}{\widehat\xi_{\lambda_j}(0)}\;\longrightarrow\;\frac{\Xi(t)}{\Xi(0)}\qquad\text{uniformly on }[0,\eta].
$$
*Then the Riemann Hypothesis holds. The same holds for the truncated CCM ground states $\xi_{\lambda,N(\lambda)}$.*

*Proof.* Under (a), $F_j=\widehat\xi_{\lambda_j}/\widehat\xi_{\lambda_j}(0)\in\mathcal L$. Since $\Xi(t)=\int\Phi(u)\cos(tu)\,du$ with Riemann's kernel $\Phi>0$, we have $\Xi(0)>0$ and $\Xi>0$ on $[0,\eta]$ for $\eta<\gamma_1$. Apply Theorem 5.2 with $\widehat G=\Xi/\Xi(0)$. $\square$

Corollary 5.3 replaces "uniformly on closed substrips of $|\operatorname{Im}z|<\tfrac12$" by "uniformly on one real segment, of any length, below the first zero". The segment carries no zeros of $\Xi$ at all; the transport of the zeros is done by the real-rootedness of the approximants.

**Corollary 5.4 (proximity at a logarithmic rate suffices).** *Let $k_\lambda=\mathcal E(h_\lambda)$ be the prolate ansatz of [C2, Sect. 7], $\tilde k_\lambda$ its even part, and $\theta_\lambda$ the angle between $\xi_\lambda$ and $\tilde k_\lambda$ in $L^2(d^*u)$. If (a) holds along $\lambda_j\to\infty$ and*
$$
\sin\theta_{\lambda_j}\cdot\sqrt{\log\lambda_j}\;\longrightarrow\;0,
$$
*then the Riemann Hypothesis holds.*

*Proof.* Normalize $\|\xi\|=1$ and write $\xi=c\,\tilde k/\|\tilde k\|+e$ with $e\perp\tilde k$, $\|e\|=\sin\theta$, $c=\cos\theta$. For real $t$, $|\widehat f(t)|\le\|f\|_{L^1(d^*u)}\le\sqrt L\,\|f\|_{L^2}$, so
$$
\Big|\frac{\widehat\xi(t)}{\widehat\xi(0)}-\frac{\widehat{\tilde k}(t)}{\widehat{\tilde k}(0)}\Big|
=\frac{|\widehat e(t)\widehat{\tilde k}(0)-\widehat{\tilde k}(t)\widehat e(0)|}{|\widehat\xi(0)\widehat{\tilde k}(0)|}
\le\frac{\sqrt L\,\sin\theta\,\big(1+\sup_t|\widehat{\tilde k}(t)|/|\widehat{\tilde k}(0)|\big)}{|\widehat\xi(0)|}.
$$
By [C2, Lem. 7.3] (resting on the classical prolate estimate [C2, Lem. 7.2]), $\widehat k_\lambda$, and hence $\widehat{\tilde k}_\lambda$ since $\Xi$ is even, converges to a fixed multiple of $\Xi$ uniformly on closed substrips, in particular on all of $\mathbb R$; and $|\Xi(t)|\le\int\Phi=\Xi(0)$ on $\mathbb R$. So the supremum is bounded, $\widehat{\tilde k}_\lambda(0)/\|\tilde k_\lambda\|$ is bounded away from $0$, and $|\widehat\xi(0)|\ge c\,|\widehat{\tilde k}(0)|/\|\tilde k\|-\sqrt L\sin\theta$ is bounded away from $0$ once $\sqrt L\sin\theta\to0$. The right side then tends to $0$ uniformly on $\mathbb R$, and Corollary 5.3 applies. $\square$

**Corollary 5.5 (the spectral form).** *Let $\mu_1(\lambda)$ be the second eigenvalue of $QW_\lambda$ on even functions and $R(f)=QW_\lambda(f)/\|f\|^2$. If (a) holds along $\lambda_j\to\infty$ and*
$$
\frac{R(\tilde k_\lambda)-\varepsilon(\lambda)}{\mu_1(\lambda)-\varepsilon(\lambda)}\;\log\lambda\;\longrightarrow\;0,
$$
*then the Riemann Hypothesis holds.*

*Proof.* Write $\tilde k/\|\tilde k\|=\cos\theta\,\xi+\sin\theta\,w$ with $w$ even, $w\perp\xi$, $\|w\|=1$. Since $\xi$ is an eigenvector, $R(\tilde k)=\cos^2\theta\,\varepsilon+\sin^2\theta\,R(w)\ge\cos^2\theta\,\varepsilon+\sin^2\theta\,\mu_1$, so $\sin^2\theta\le(R(\tilde k)-\varepsilon)/(\mu_1-\varepsilon)$. Apply Corollary 5.4. $\square$

Corollary 5.5 turns the second missing step into an inequality between two numbers of the semilocal Weil form: the Rayleigh excess of an explicit trial vector, and the second even eigenvalue. The required margin is only logarithmic.

The Rayleigh excess is controlled in closed form by the first self-dual prolate defect. The exact tail identity of the companion note [N2] (Lem. 3.2) gives $QW_\lambda(k_\lambda)=QW(F_{\rm out})$, and $R(k_\lambda)/(1-\chi_4(\lambda))$ stays between $4.9$ and $13.2$ for $\lambda\in[1.4,1.7]$ ([N2], Sect. 3). Where the excess has been measured directly ($\lambda=1.5$: $R(\tilde k)-\varepsilon=2.12\times10^{-5}$ in [N2], with $\mu_1-\varepsilon=0.275$ from Table 5.1), the left side of Corollary 5.5 is $3\times10^{-5}$.

Beyond $\lambda=1.7$ the finite-difference prolate of [N2] is not accurate enough to measure $R(\tilde k_\lambda)$. What Table 5.1 does certify at every rung is the denominator. The ratio $\mu_1/\varepsilon$ grows from $1.9\times10^3$ at $\lambda=1.5$ to $1.1\times10^8$ at $\lambda=4$ and $2.9\times10^8$ at $\lambda=4.5$. Since $\varepsilon\approx c(1-\chi_4)$ ([N2], Prop. 4.3), this ratio tracks the next self-dual prolate rung, $(1-\chi_8)/(1-\chi_4)\asymp\lambda^8$, with a slowly drifting constant ($\approx0.2$ at $\lambda=2$, $\approx0.46$ at $\lambda=4$ and $4.5$). If $R(\tilde k_\lambda)-\varepsilon=O(\varepsilon)$ persists, as it does where it has been measured ($R/\varepsilon=1.1$–$1.3$ at $\lambda=1.5$), the left side of Corollary 5.5 is of order $\log\lambda\,/\,(\mu_1/\varepsilon)\approx10^{-8}$ at $\lambda=4$ $\mathsf{[C]}$.

This reopens the prolate row of Proposition 3.1 in a sharper form. The operator-norm comparison recorded there is dead; the trial-vector comparison has polynomial room against a logarithmic requirement at every computed window. The analytic target it leaves is a two-rung prolate comparison for the Weil form. Section 5.6 proves the upper half (Proposition 5.13), and shows that in the direction of RH the $\varepsilon$-term makes the lower half contain Weil positivity (Remark 5.14); the comparison is the exact missing input for the converse direction (Corollary 5.15):
$$
R(\tilde k_\lambda)-\varepsilon(\lambda)\ \lesssim\ \lambda^{A}\,(1-\chi_4(\lambda)),\qquad \mu_1(\lambda)\ \gtrsim\ \lambda^{-B}\,(1-\chi_8(\lambda)),\qquad A+B<8.
$$

### 5.3 Where the content sits when the Hypothesis fails $\mathsf{[P]}$

**Theorem 5.6 (a finite exceptional set destroys normality).** *Suppose $\zeta$ has at least one, and only finitely many, zeros off the critical line. Let $\lambda_j\to\infty$ with (a) holding for $QW^{N_j}_{\lambda_j}$, $N_j$ large enough that $\varepsilon_{N_j}(\lambda_j)\to-\infty$, and $\widehat\xi_{\lambda_j}(0)\ne0$. Then $S(\lambda_j)\to\infty$. In particular the family is not normal, and the convergence of Corollary 5.3 fails on every real segment.*

*Proof.* *Step 1 ($\varepsilon\to-\infty$).* Let $\rho_0=\tfrac12+\delta+it_0$ be an off-line zero of maximal displacement $\delta>0$, and let $\Delta_1,\ldots,\Delta_m$ be the finitely many nonzero frequencies $\pm(t'\mp t_0)$, $t'+t_0$ attached to the off-line zeros $\tfrac12\pm\delta+it'$ of the same displacement, together with $2t_0$. Since the exponentials $e^{(\delta+i\Delta)v}$ are linearly independent, we can fix a real $\varphi\in C_c^\infty(-1,1)$ with
$$
\int\varphi(v)e^{\delta v}\,dv=1,\qquad \int\varphi(v)e^{(\delta+i\Delta_j)v}\,dv=0\quad(1\le j\le m).
$$
Put $c=L/2-1$, $g(u)=\varphi(u-c)\cos(t_0u+\tfrac\pi2)$ and $f(u)=g(u)+g(-u)$. Then $f$ is even and supported in the window, and by the explicit formula $QW_\lambda(f)=\sum_\rho\widehat f(\gamma_\rho)^2$.

The on-line terms total at most $B=\sum_\gamma(|\widehat\varphi(\gamma-t_0)|+|\widehat\varphi(\gamma+t_0)|)^2<\infty$, independent of $\lambda$, because $|\widehat f|$ on $\mathbb R$ does not see the translation by $c$. In $\widehat f(\gamma_0)$, $\gamma_0=t_0-i\delta$, the piece of $f$ at the near edge contributes $O(e^{-\delta c})$. The piece at the far edge contributes $-\tfrac i2e^{\delta c}$, plus the conditions above, which kill every term carrying a factor $e^{i\Delta_jc}$. Hence the quadruple of $\rho_0$ contributes $4\operatorname{Re}\widehat f(\gamma_0)^2=-e^{2\delta c}$, the other quadruples of displacement $\delta$ contribute nothing at order $e^{2\delta c}$, and those of smaller displacement contribute $o(e^{2\delta c})$.

Since $\|f\|$ is fixed, $\varepsilon(\lambda)\le QW_\lambda(f)/\|f\|^2\le-C\lambda^{2\delta}$ for large $\lambda$. By density the same holds for $\varepsilon_N(\lambda)$ once $N$ is large.

*Step 2 (energy identity).* For the ground state, $\sum_\rho\widehat\xi_\lambda(\gamma_\rho)^2=QW_\lambda(\xi_\lambda)=\varepsilon(\lambda)\|\xi_\lambda\|^2$. With $F_\lambda=\widehat\xi_\lambda/\widehat\xi_\lambda(0)$ and Plancherel,
$$
\sum_\rho F_\lambda(\gamma_\rho)^2=\frac{\varepsilon(\lambda)}{2\pi}\int_{\mathbb R}F_\lambda(t)^2\,dt.
$$

*Step 3.* Suppose $S(\lambda_j)\le M$ along a subsequence. Then $a_1\ge M^{-1/2}$, and Lemma 5.1(ii) gives $F_\lambda\ge e^{-1/3}$ on $|t|\le\tau=1/(2\sqrt M)$, so the right side is at most $\varepsilon(\lambda_j)\,\tau e^{-2/3}/\pi\to-\infty$. On the left, every on-line term is $\ge0$ because $F_\lambda$ is real on $\mathbb R$, and the finitely many off-line terms are bounded below by $-\sum_{\text{off}}e^{2M|\gamma_\rho|^2}$ (Lemma 5.1(i)). This is a contradiction. $\square$

Quantitatively, Step 3 forces $e^{2S T^2}\sqrt S\gtrsim\lambda^{2\delta}$ for a zero at height $T$, that is $S(\lambda)\gtrsim\delta\log\lambda/T^2$. This rate is weak; the experiment below shows that the actual growth is quadratic in $\log\lambda$.

### 5.4 The certificate on $\zeta$ $\mathsf{[A]}$

`empirical/connes_route/probe_lp_transport_zeta.py` builds $QW_\lambda^N$ with every entry in closed form — digamma and trigamma values, geometrically convergent tails, finite prime sums — which agrees with the quadrature-certified matrix of [N2] to $3\times10^{-40}$ and is roughly seventy times faster. Precision is set to resolve $\varepsilon(\lambda)$, up to 143 digits, and $N\ge2\lambda^2L+24$ resolves the height $2\pi\lambda^2$ at which the window's maximal real-zero density $L/2\pi$ meets the density of the zeta zeros.

| $\lambda$ | $\varepsilon$ | $\varepsilon_{\rm odd}/\varepsilon$ | $\mu_1/\varepsilon$ | $S(\lambda)$ | $\lambda^2(S_\Xi-S)$ | $\Delta_{[0,1]}$ | edge | $\sigma$ |
|---|-------|------|------|-------|------|------|------|-----|
| 1.3 | 0.024 | 15 | 37 | 0.0078209 | 0.0258 | 0.015 | — | 0.682 |
| 1.5 | $1.5{\cdot}10^{-4}$ | 92 | $1.9{\cdot}10^{3}$ | 0.0126950 | 0.0234 | 0.010 | — | 0.463 |
| 2.0 | $9.2{\cdot}10^{-13}$ | 588 | $1.9{\cdot}10^{5}$ | 0.0176929 | 0.0216 | $5.3{\cdot}10^{-3}$ | 0.17 | 0.221 |
| 2.5 | $5.9{\cdot}10^{-24}$ | $1.5{\cdot}10^{3}$ | $1.3{\cdot}10^{6}$ | 0.0197517 | 0.0210 | $3.3{\cdot}10^{-3}$ | $2.9{\cdot}10^{-3}$ | 0.141 |
| 3.0 | $3.7{\cdot}10^{-38}$ | $3.6{\cdot}10^{3}$ | $7.1{\cdot}10^{6}$ | 0.0208125 | 0.0206 | $2.2{\cdot}10^{-3}$ | $9.5{\cdot}10^{-6}$ | 0.103 |
| 3.5 | $3.1{\cdot}10^{-55}$ | $7.4{\cdot}10^{3}$ | $3.1{\cdot}10^{7}$ | 0.0214381 | 0.0204 | $1.6{\cdot}10^{-3}$ | $6.4{\cdot}10^{-9}$ | 0.082 |
| 4.0 | $4.0{\cdot}10^{-75}$ | $1.5{\cdot}10^{4}$ | $1.1{\cdot}10^{8}$ | 0.0218373 | 0.0203 | $1.2{\cdot}10^{-3}$ | $1.3{\cdot}10^{-12}$ | 0.068 |
| 4.5 | $8.5{\cdot}10^{-98}$ | $2.3{\cdot}10^{4}$ | $2.9{\cdot}10^{8}$ | 0.0221075 | 0.0202 | $9.8{\cdot}10^{-4}$ | $4.1{\cdot}10^{-17}$ | 0.059 |

**Table 5.1 (the $\zeta$ ladder).** $\varepsilon$ and $\mu_1$ are the smallest and second eigenvalues of $QW_\lambda^N$ on even vectors, and $\varepsilon_{\rm odd}$ is the odd ground. $S$ is computed from the moment formula, $\Delta_{[0,1]}=\sup_{0\le t\le1}|F_\lambda(t)-\Xi(t)/\Xi(0)|$, edge is the share of $|\xi_\lambda|^2$ within $\tfrac12$ of the window edges (a dash where the window is narrower than $1$), and $\sigma=24S/L^2$.

The resolutions are $N=25, 27, 35, 46, 63, 85, 112, 145$, at 40–143 digits. At every rung all $N$ secular roots are real. The first zero is $z_1=16.066$ and $14.175$ at $\lambda=1.3,1.5$, and $14.13472514$ ($\gamma_1$ to ten digits) from $\lambda=2$ on. Raising $N$ by a quarter moves $S$ by $4\times10^{-6}$ (relative) at $\lambda=4$ and by $1.2\times10^{-6}$ at $\lambda=4.5$.

Every rung satisfies (a), with the even–odd split resolved directly, so Observation 4.1's resolution claim is withdrawn. All $N$ secular roots are real (the CvS mechanism), and $S$ computed from the moment formula $S=L^2/24+(L^2/2\pi^2)\sum_{k\ge1}\xi_k/(k^2\xi_0)$ agrees to fifteen digits with $\sum z_j^{-2}$ over the zeros, including the frame zeros $s=k>N$ of the truncation. Three laws are visible:

1. **The scalar converges.** $S(\lambda)\uparrow S_\Xi=-\Xi''(0)/2\Xi(0)=0.0231049931\ldots$ with $\lambda^2(S_\Xi-S(\lambda))$ settling near $0.020$. The deficit is the contribution of the zeros above the Nyquist height $2\pi\lambda^2$, which the window cannot yet resolve.
2. **The interval converges.** $\Delta_{[0,1]}=\sup_{[0,1]}|F_\lambda-\Xi/\Xi(0)|$ falls in step with $S_\Xi-S$: $\lambda^2\Delta_{[0,1]}$ runs from $0.025$ to $0.0197$ across the ladder, as it must, since $F_\lambda(t)\approx e^{-S(\lambda)t^2}$ below the first zero. And $z_1(\lambda)=\gamma_1$ to ten digits from $\lambda=2$ on. This is the hypothesis of Corollary 5.3, observed at the rate $\lambda^{-2}$.
3. **The ground state is a bulk state.** The share of $|\xi_\lambda|^2$ within $\tfrac12$ of the window edges falls from $3\times10^{-3}$ ($\lambda=2.5$) to $10^{-9}$ ($\lambda=3.5$) and $4\times10^{-17}$ ($\lambda=4.5$), and $\sigma(\lambda):=S(\lambda)/(L^2/24)\to0$.

### 5.5 The matched pair: Davenport–Heilbronn through the same machine $\mathsf{[A]}$

The Davenport–Heilbronn function $f(s)=\sum a_nn^{-s}$, $a=(0,1,\kappa,-\kappa,-1)$ modulo $5$, $\kappa=(\sqrt{10-2\sqrt5}-2)/(\sqrt5-1)$, has real coefficients, the functional equation $\Lambda(s)=(5/\pi)^{(s+1)/2}\Gamma(\tfrac{s+1}2)f(s)=\Lambda(1-s)$, no Euler product, and zeros off the line. The certificate locates the first four at $0.808517+85.699348i$, $0.650830+114.163343i$, $0.574356+166.479306i$ and $0.724258+176.702461i$. `probe_lp_transport_dh.py` runs the identical code with three changes forced by the data: no pole terms, the archimedean kernel $e^{-y/2}$ in place of $e^{y/2}$ (from $\Gamma(\tfrac{s+1}2)$), and $\log5$ in the constant, with $\Lambda_f(n)$ on all $n$ from $-f'/f$. The construction is validated three ways: $\Lambda_f$ against $-f'/f(3)$; the archimedean functional against its frequency-space digamma form, to all digits; and the matrix entry $QW[V_0,V_0]$ against the zero side, summing all $75$ zeros below height $130$, the four off-line ones included, within the tail allowance.

[TABLE 5.2 here]

**Observation 5.7 (the bulk–edge transition).** *For $\lambda\le5.5$ the DH ground state behaves like zeta's:*
- *$\varepsilon>0$ and exponentially small, and (a) holds;*
- *the zeros of $\widehat\xi_\lambda$ track the DH zeros on the line: $5.0942,\ 8.9401,\ 12.137,\ldots$ at $\lambda=3$, against $5.0942,\ 8.9399,\ 12.1335$;*
- *$S$ rises toward $S_{\Xi_{DH}}=0.0981$ with $\lambda^2(S_{\Xi_{DH}}-S)\approx0.10\approx5\times0.020$, the Nyquist law with conductor $5$;*
- *the edge share vanishes.*

*Between $\lambda=5.5$ and $5.75$ the form turns negative, and each resolved off-line quadruple then adds one negative direction per sector. At $\lambda=12$ the four negative even modes peak at heights $86.6,\ 175.8,\ 115.1,\ 165.4$, against the quadruples at $85.70,\ 176.70,\ 114.16,\ 166.48$, and their depths order with the displacement $\delta$. The ground state migrates to the window edges, and $\sigma(\lambda)\to3$ ($\sigma=3.006$ at $\lambda=30$). This is exactly the value for $\cos(zL/2)$, the transform of a pair of edge spikes ($S=L^2/8$).* The ground eigenvalue deepens at least as fast as Step 1 of Theorem 5.6 requires: $-\varepsilon/\lambda^{2\delta}$, with $\delta=0.309$, grows from $0.49$ to $0.70$ between $\lambda=15$ and $30$.

**Observation 5.8 (where the content is not).** *Hypothesis (a) holds for DH at every computed window except the onset band $\lambda\in[5.75,6]$, where the first negative mode is odd. For $\lambda\ge6.5$ the ground-state transforms therefore have only real zeros (all $N$ secular roots, certified), while RH fails for DH.* Hence the equivalence "even ground $\iff$ RH" asserted in Observation 4.2 is false: evenness is the parity of the edge doublet, not the Hypothesis. In the matched pair the content sits in normality — the boundedness of $S$, equivalently the interval convergence of Corollary 5.3 — exactly as Theorem 5.6 predicts for a finite exceptional set.

**Conjecture 5.9 (bulk–edge dichotomy).** *Under (a), $S(\lambda)$ stays bounded, equivalently $\sigma(\lambda)=O(L^{-2})$, if and only if the Riemann Hypothesis holds; if it fails, $\sigma(\lambda)\to3$.* For a finite exceptional set, Theorem 5.6 proves that bounded $S$ excludes it. $\mathsf{[C]}$

**Remark 5.10 (a boundary reading).** The dichotomy is a statement about the boundary of the window. In the log variable the window is $|v|\le L/2$, its edges sit at $u=\lambda^{\pm1}$, and the prime powers $n\approx\lambda^2$ are exactly the translations that carry one edge onto the other. An off-line zero acts as a state localized at that boundary, as in the trial functions of Theorem 5.6, Step 1, and in the DH edge mode. Under the Euler product, the boundary of every computed window carries less than $10^{-16}$ of the ground state (Table 5.1, $\lambda=4.5$). The Hypothesis, read this way, says that the edges stay quiet at every scale.

**Remark 5.11 (the Hadamard Gaussian off the axis).** For $\zeta$, inside the critical strip, $F_\lambda$ and $\Xi/\Xi(0)$ differ mainly by one Gaussian factor. $F_\lambda$ lacks the zeros above the Nyquist height, and their Hadamard factors contribute $e^{-(S_\Xi-S(\lambda))z^2}$ at leading order. The raw relative error at $z=30+0.4i$ is $7.0$ at $\lambda=3$ and $2.1$ at $\lambda=4$. It is almost exactly $e^{(S_\Xi-S)z^2}-1$, and multiplying by $e^{-(S_\Xi-S)z^2}$ removes it: the corrected errors are $1.5\times10^{-2}$ and $2.3\times10^{-3}$, and $1.8\times10^{-6}$ at $z=5+0.3i$, $\lambda=4$. The gain is between $478$ and $1.8\times10^4$ at every sample point, and both errors fall with $\lambda$ (`probe_lp_transport_offaxis.py`, GREEN). The multiplier $e^{-cz^2}$ with $c=S_\Xi-S(\lambda)\ge0$ is itself Laguerre–Pólya, so the corrected family is still real-rooted. The approach to $\Xi$ is therefore governed, to leading order, by the same single scalar that controls normality.

![The order parameter $\sigma(\lambda)=24S(\lambda)/L^2$ of the Weil ground state. (a) For $\zeta$ it stays in the bulk phase, $\sigma\to0$. For the Davenport–Heilbronn function it jumps to the edge value $\sigma=3$ of $\cos(zL/2)$ when its form turns negative. (b) The Davenport–Heilbronn Krein–Langer index, one negative direction per resolved off-line quadruple (heights $85.70$, $114.16$, $176.70$, $166.48$ in order of appearance).](empirical/connes_route/fig_lp_transport.png)

### 5.6 The upper side of the prolate comparison, and what the $\varepsilon$-term contains

Corollary 5.5 compares two numbers: the Rayleigh excess of the prolate trial vector, $R(\tilde k_\lambda)-\varepsilon(\lambda)$, and the second even gap, $\mu_1(\lambda)-\varepsilon(\lambda)$. This subsection closes the upper side, $R(\tilde k_\lambda)\lesssim\lambda^{A}(1-\chi_4(\lambda))$, and then shows that the $\varepsilon$-term is not a technicality. In the direction of RH it *is* Weil positivity, which changes what the two-rung comparison can and cannot deliver.

Write $H=h_\lambda\mathbf 1_{[-\lambda,\lambda]}$ with $\|H\|_2=1$, $h_\lambda=a\,h_{0,\lambda}+b\,h_{4,\lambda}$ ($a^2+b^2=1$), and $\widehat H(\xi)=\int H(x)e^{-2\pi ix\xi}dx$. The prolate functions of $PW_\lambda$ ($c=2\pi\lambda^2$) satisfy three classical facts (Slepian–Pollak; Slepian 1965; Bonami–Karoui for explicit bounds):

- **(duality)** $\widehat{h_{n,\lambda}\mathbf 1}=\mu_n h_{n,\lambda}$ on $[-\lambda,\lambda]$, with $\mu_n=(-i)^n\sqrt{\chi_n}$;
- **(leakage)** $\int_{|\xi|>\lambda}|\widehat{h_{n,\lambda}\mathbf 1}|^2=1-\chi_n$;
- **(endpoint jets)** $|h_{n,\lambda}^{(j)}(\pm\lambda)|^2\le C_j\lambda^{a_j}(1-\chi_n)$ for $j\le2$, from the prolate equation at the endpoint together with Slepian's formula for $d\chi_n/dc$.

**Lemma 5.12 (the point mass is a defect).** $h_\lambda(0)=a\,h_{0,\lambda}(0)\big(1-\sqrt{\chi_0/\chi_4}\big)$; in particular $|h_\lambda(0)|\le C(1-\chi_4)$.

*Proof.* $\int h_\lambda=\widehat H(0)=a\sqrt{\chi_0}h_{0,\lambda}(0)+b\sqrt{\chi_4}h_{4,\lambda}(0)=0$ by duality; substitute for $b\,h_{4,\lambda}(0)$ in $h_\lambda(0)=a h_{0,\lambda}(0)+b h_{4,\lambda}(0)$, and use $\sqrt{\chi_0}-\sqrt{\chi_4}\le(1-\chi_4)/\sqrt{\chi_4}$. $\square$

*Certificate.* With prolate functions computed from the Legendre (Bouwkamp) expansion at 80 digits, $h_\lambda(0)/(1-\chi_4)=-0.357,\,-0.426,\,-0.482,\,-0.531$ at $\lambda=1.5,2,2.5,3$, where $1-\chi_4=4.8\times10^{-5},\,2.5\times10^{-13},\,1.1\times10^{-24},\,6.1\times10^{-39}$.

**Proposition 5.13 (the upper side).** *Assume a fixed zero-free strip: every nontrivial zero has $|\beta-\tfrac12|\le\tfrac12-\delta_0$ for some $\delta_0>0$. Theorem OAI ([OAI]; cf. Paper 22) gives $\delta_0=\tfrac18$. Then for $\lambda\ge2$,*
$$
R(\tilde k_\lambda)\;\le\;\frac{|QW_\lambda(\tilde k_\lambda)|}{\|\tilde k_\lambda\|^2}\;\le\;C(\delta_0)\,\lambda^{A}\,(1-\chi_4(\lambda))
$$
*with an absolute exponent $A$.* $\mathsf{[A]}$ (proof sketch; it rests on Theorem OAI and the classical prolate facts above, and the constants are not optimized).

*Proof sketch.*

*(i) Only the leakage survives below the window.* For $0<u<1/\lambda$, Poisson summation and $\widehat H(0)=0$ give
$$
F_{\rm out}(u):=\mathcal E(H)(u)=u^{-1/2}\sum_{m\ge1}\widehat H(m/u)-\tfrac12u^{1/2}H(0).
$$
Every argument $m/u$ exceeds $\lambda$, so only out-of-band values enter; the last term is $O(1-\chi_4)$ by Lemma 5.12. Integrating by parts twice in $\widehat H$ splits the out-of-band values into endpoint-jet terms of size $O(\lambda^{a}(1-\chi_4)^{1/2})$ and a remainder whose $L^2$ mass is controlled by the leakage. This gives, for $y\in[-\tfrac12+\delta_0,\tfrac12]$ and $0<s<\delta_0$, the weighted log-Sobolev bound $\|u^{y}F_{\rm out}\|_{H^s(d^*u)}^2\le C\lambda^{a}(1-\chi_4)$. (The sawtooth from the endpoint jump oscillates at log-frequency $\lambda/u$ with amplitude $u^{y+1/2}$; this is square-integrable in $H^s$ exactly when $s<y+\tfrac12$, which is why a fixed strip is used.)

*(ii) The zero side, unconditionally.* $\mathcal E(H)$ lies in the radical of the global Weil form: its Mellin transform is $\zeta(\tfrac12+iz)\,\mathcal M_H(z)$ for $\operatorname{Im}z>-\tfrac12$ (Lemma 3.1 of [N2]). Hence $\widehat k_\lambda(\gamma_\rho)=-\widehat F_{\rm out}(\gamma_\rho)$ at every nontrivial zero, on or off the line. The explicit formula, $QW_\lambda(\tilde k)=\sum_\rho\widehat{\tilde k}(\gamma_\rho)^2$, together with the symmetry $\gamma\mapsto-\gamma$ of the zero set, gives
$$
|QW_\lambda(\tilde k_\lambda)|\;\le\;\sum_\rho|\widehat F_{\rm out}(\gamma_\rho)|^2 .
$$
No positivity is used. The zero side is evaluated with absolute values, so off-line zeros are allowed.

*(iii) The zero sum.* There are $O(\log T)$ zeros with height in $[T,T+1]$, all at distance at least $\delta_0$ from $\operatorname{Im}z=\pm\tfrac12$. Bounding each $|\widehat F_{\rm out}|^2$ by its mean over a disk of radius $\delta_0/2$ (subharmonicity) and summing over $T$ gives
$$
\sum_\rho|\widehat F_{\rm out}(\gamma_\rho)|^2\ \le\ C(\delta_0)\sup_{|y|\le\frac12-\frac{\delta_0}2}\int|\widehat F_{\rm out}(t+iy)|^2(1+|t|)^{2s}dt\ \le\ C\lambda^{A}(1-\chi_4)
$$
by Plancherel and (i). Finally $\|\tilde k_\lambda\|\to\|k\|>0$ ([C2], Lem. 7.3 estimates). $\square$

Proposition 5.13 is the first rigorous form of the "linear law" observed in [N2], where $R/(1-\chi_4)$ stays between $4.9$ and $13.2$. Its structure is worth stating plainly. The trial vector's energy is the zeta-zero sum of the transform of its below-window tail, and that tail is made of prolate leakage only.

**Remark 5.14 (the $\varepsilon$-term is Weil positivity).** In Corollary 5.5, if $\varepsilon\ge0$ then $(R-\varepsilon)/(\mu_1-\varepsilon)\le R/\mu_1$. If $\varepsilon<0$ the ratio is at least $|\varepsilon|/(\mu_1+|\varepsilon|)$. The hypothesis of Corollary 5.5 therefore forces $\varepsilon(\lambda)\ge-o(\mu_1(\lambda)/\log\lambda)$, and $\mu_1(\lambda)\to0$.

Now $\varepsilon(\lambda)$ is non-increasing in $\lambda$, because the windows are nested. A non-increasing function that is eventually above every negative constant is non-negative everywhere. So in the direction of RH, Corollary 5.5 contains Weil positivity at every scale, which is RH itself (Yoshida; [C2], Cor. 3.8). The spectral form adds a second-eigenvalue condition to positivity; it does not reduce positivity. For RH, the live hypothesis remains the interval convergence of Corollary 5.3, whose statement does not name $\varepsilon$, together with the bulk–edge dichotomy behind it (Theorem 5.6, Conjecture 5.9). We record this so that the two-rung comparison is not mistaken for a route that bypasses positivity.

What the comparison *does* deliver is the converse direction, which is open even under RH (Section 4).

**Corollary 5.15 (RH plus one spectral bound gives the CCM convergence).** *Assume RH, hypothesis (a) along $\lambda_j\to\infty$, a fixed zero-free strip as in Proposition 5.13 (implied by RH), and*
$$
\mu_1(\lambda)\ \ge\ c\,\lambda^{-B}\,(1-\chi_8(\lambda))\qquad\text{with }A+B<8 .
$$
*Then $\widehat\xi_{\lambda_j}/\widehat\xi_{\lambda_j}(0)\to\Xi/\Xi(0)$ locally uniformly on $\mathbb C$. This is the convergence of [C2], Sect. 7.* $\mathsf{[A]}$

*Proof.* RH gives $\varepsilon\ge0$, so $\sin^2\theta_\lambda\le(R-\varepsilon)/(\mu_1-\varepsilon)\le R/\mu_1\le C\lambda^{A+B}(1-\chi_4)/(1-\chi_8)\asymp\lambda^{A+B-8}$, using Proposition 5.13 and the prolate asymptotics $(1-\chi_8)/(1-\chi_4)\asymp c^4\asymp\lambda^8$. Then $\sin\theta_\lambda\sqrt{\log\lambda}\to0$; the argument of Corollary 5.4 gives uniform convergence on $\mathbb R$, and Theorem 5.2(3) upgrades it to $\mathbb C$. $\square$

So the second-eigenvalue bound is exactly the input that turns "RH" into "the Connes–Consani–Moscovici approximants converge". The measured ladder ($\mu_1/\varepsilon\asymp(1-\chi_8)/(1-\chi_4)$, constant $0.2$–$0.46$, Table 5.1) says it holds at every computed window.

---

## 6. Honest status

What is **proved or certified** $\mathsf{[P]}$:

- the equivalence chain of §1;
- the finite Weil form generating the zeta zeros on the line (Thm 2.1);
- the prolate vehicle's simple even ground state (Thm 2.2);
- the target identity $\widehat{\mathcal E(h)}=\Xi$;
- the Laguerre–Pólya transport and its consequences for the open step (Theorem 5.2, Corollaries 5.3–5.5);
- the destruction of normality by a finite exceptional set (Theorem 5.6).
- the point-mass lemma (Lemma 5.12) and, resting on Theorem OAI, the upper side of the prolate comparison and the conditional convergence theorem (Proposition 5.13, Corollary 5.15; tier $\mathsf{[A]}$, proof sketch).

What is **certified numerically** $\mathsf{[A]}$: Table 5.1 for $\zeta$ and Table 5.2 for the Davenport–Heilbronn control, both computed from closed-form matrices at up to 143 digits.

What is **structural** $\mathsf{[A]}$: the common closure point of six routes (Prop 3.1), which is $\varphi'\ge0$, with the prolate row refined by Corollary 5.5.

What is **open** $\mathsf{[C]}$:

- the step restated in Section 4, namely (a) together with the interval convergence of Corollary 5.3, equivalently with the two-rung prolate comparison following Corollary 5.5;
- the bulk–edge dichotomy (Conjecture 5.9).

The matched pair settles one point that had been open in the program's record. The evenness of the ground state is not where the Hypothesis lives; the normality of the approximant family is.

This program does not prove the Riemann Hypothesis, and N7 does not claim it. The reduction is exact, the finite half is realized, and the open step is now quantified. It is a convergence on one real interval, or equivalently a spectral inequality with a logarithmic margin, against observed margins of order $\lambda^8$ at every computed window. It remains open in the field's most advanced work (Connes–Consani–Moscovici, November 2025). The separation is the program's discipline: **structural reduction — real; proof of RH — not yet.**

---

## References

[N0] Murillo Montero, L. (2026). *The Closure: RH as Integrated Cubic Positivity of the Apex Weil Form.*

[N4–N6] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place; The Apex Edge Operator; The Unified Archimedean Operator and the de Branges Target.*

[C1] Connes, A. (2026). *The Riemann Hypothesis: Past, Present and a Letter Through Time.* arXiv:2602.04022.

[C2] Connes, A., Consani, C., Moscovici, H. (2025). *Zeta Spectral Triples.* arXiv:2511.22755.

[CC] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77.

[CvS] Connes, A., van Suijlekom, W. (2025). *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.*

[BD] Báez-Duarte, L. (2003). *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis.*

[N2] Murillo Montero, L. (2026). *The Semilocal Weil Form inside the Connes–van Suijlekom Real-Zeros Theorem: Hypothesis Verification, a Closed-Form Smallness Mechanism, and a Function-Field Instance.* Companion to the verification note (v2, doi:10.5281/zenodo.20680667), July 3, 2026.

[DH] Davenport, H., Heilbronn, H. (1936). *On the zeros of certain Dirichlet series I, II.* J. London Math. Soc. 11, 181–185 and 307–312.

[Sp] Spira, R. (1994). *Some zeros of the Titchmarsh counterexample.* Math. Comp. 63, 747–748.

[BS] Balanzario, E. P., Sánchez-Ortiz, J. (2007). *Zeros of the Davenport–Heilbronn counterexample.* Math. Comp. 76, 2045–2049.

[Po] Pólya, G. (1926). *Bemerkung über die Integraldarstellung der Riemannschen $\xi$-Funktion.* Acta Math. 48, 305–317.

[OAI] OpenAI (2026). *The Quasi-Riemann Hypothesis: a zero-free half-plane $\operatorname{Re}s>7/8$.* github.com/openai/math, family 003; model-generated, Lean-formalized as reported by OpenAI. Cited at tier $\mathsf{[A]}$ only.

[Le] Levin, B. Ja. (1964). *Distribution of Zeros of Entire Functions.* Transl. Math. Monographs 5, AMS. (The Laguerre–Pólya class; Hadamard factorization; closure under locally uniform limits.)
