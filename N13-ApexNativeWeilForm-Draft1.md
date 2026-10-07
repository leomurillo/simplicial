# N13 — The Apex-Native Weil Form: A Validated Realization, and Two Routes Retired

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 7, 2026*

<!--
Program record (not part of the paper). Thirteenth paper of the Numbers (N-) series; a consolidation
paper. It does NOT prove RH and does not claim to. It records the genuine deposits of a session of
adversarial stress-testing along the Connes prolate route: one POSITIVE realization (the Weil form
assembled end-to-end from the native apex/conductor objects, reproducing the zeros), TWO CORRECTIONS
(a) the finite-prime Weil form DOES reproduce the zeros -- to ~1e-19 (cosine/frequency basis) and ~1e-50
(exact position-space kernel), approaching Connes' 1e-55 -- and the earlier failures were a float64
precision floor (distinguished eigenvalue ~1e-37) PLUS a mis-selection of the eigenvector (global min vs
the cluster extreme eta), NOT the basis; (b) eta is the converged extreme of the minuscule-eigenvalue
cluster at L=-2.90345 (within-cluster tower = Connes' minuscule eigenvalues), one DERIVATION (the chi_3
archimedean kernel), one DISCHARGE (the structural half of S6.6a: even-beats-odd robust at the
archimedean level, Delta=+1.65->+0.074, via the symmetric-binds/arrow-blind mechanism; simple+isolated
exact at each finite X; residual = uniform-in-X persistence = the transfer = RH), one PLACEMENT (the
cubic-chirality candidate is reassigned to the chi_3 object / GRH(chi_3) by a matched-pair test: the zeta
gap is independent of L(1/2,chi_3)), and one RETIREMENT (the multiplicative-holonomy compass is
trivial-per-place). Each deposit lands on the same boundary the program and the field already name: the
apex->archimedean convergence (= RH; open in CCM 2511.22755). Discipline throughout: validated
realization (real) is separated from new content / proof of RH (neither achieved). Certificates (empirical/):
  probe_apex_native_weil.py        (U_N -> N4 kernel; apex even symbol = 2theta'; conductor log-deriv =
                                    von Mangoldt; native form reproduces the zeros)
  connes_route/probe_connes_miracle_highprec.py, probe_connes_miracle_fast.py (the precision correction:
                                    eta = cluster extreme; 8/8 zeros to ~1e-50; exact u-kernel)
  connes_route/probe_connes_why_float64_fails.py (the two failure modes diagnosed; evenness defect 0)
  connes_route/probe_step_a_structural.py, probe_even_beats_odd_archimedean.py (S6.6a: cluster, eps_1>0,
                                    eta-not-nodeless, even-beats-odd Delta=+1.65->+0.074, the mechanism)
  connes_route/probe_chi3_gap_falsifier.py (matched pair: zeta gap bit-identical across fake L(1/2,chi_3))
  probe_weil_chiral_z6_margins.py  (the chi_3 kernel; the full-form S6.6a margin sub-floor = precision floor)
  probe_holonomy_factorization.py  (each local factor has zero bulk holonomy; N(T)=theta/pi+1+S(T); retired)
Builds on: probe_weil_form_v3.py (the working position-space parity-separated Weil form),
probe_prolate_simple_even.py, probe_connes_prolate_pivot.py, probe_convergence_target.py,
verify_connes_recast.py. External anchors: Connes-Consani-Moscovici arXiv:2310.18423 [CCM23] (the prolate
operator), arXiv:2511.22755 [CCM25] (Zeta Spectral Triples; the prolate->zeros convergence is numerical,
and a rigorous proof of it would establish RH); Connes-Consani arXiv:2006.13771 [CC20]; Weil (1952).
Tier tags [P]/[A]/[C] throughout.
-->

---

## Abstract

This paper consolidates the deposits of an adversarial pass along the Connes prolate route to the Riemann Hypothesis. Its single positive result is a **validated native realization**: the Riemann–Weil quadratic form, assembled term-by-term from the program's own objects — the apex unitary $U_N$ (Helmert–Fourier, whose scaling limit is the [N4] edge kernel) for the archimedean part, and the conductor blocks $(\mathbb Z/p)^\times$ (whose local-zeta logarithmic derivative is the von Mangoldt prime side) for the finite places — reproduces the low zeros of $\zeta$. We separate, with the program's tier discipline, what this achieves from what it does not: the prime side is **native-exact**, while the archimedean side equals the explicit-formula density $2\vartheta'$ *by the proven [N4]–[N5] identity* (apex symbol $=$ $\Gamma$-factor), so on that half "emergence" and "identification" coincide by theorem — a validated realization, not a new lever. Along the way we **correct the record twice.** First, the precision of the reproduction: in high precision the distinguished eigenvector's Fourier zeros match the first eleven $\zeta$-zeros to $\sim10^{-19}$ (cosine/frequency basis) and the first eight to $\sim10^{-50}$ (exact position-space kernel, $N=64$, $\mathrm{dps}=85$ — approaching Connes' published $\sim10^{-55}$). Second, *why the earlier builds failed*: not the choice of basis, but (i) a float64 precision floor — the distinguished eigenvalue is $\sim10^{-37}$, below machine resolution — and (ii) a mis-selection of the eigenvector, the global minimum in place of $\eta$, which is the **converged extreme of the near-degenerate minuscule-eigenvalue cluster** accumulating at $L=-2.90345\ldots$ (a spectral invariant stable to $34$ digits across $N$); the within-cluster splittings $7.85\!\times\!10^{-17},\dots,4.75\!\times\!10^{-42}$ are exactly Connes' minuscule-eigenvalue tower. The cosine/frequency basis reproduces the zeros perfectly once both are fixed. We **derive** the chiral archimedean kernel $K_{\chi_3}(u)=-e^{-3|u|/2}/(1-e^{-2|u|})$. We **discharge the structural half of Connes' §6.6a**: even-beats-odd holds robustly at the archimedean level ($\Delta=+1.65\to+0.074$ as the pole is restored), by the program's symmetric/antisymmetric mechanism (the archimedean well is deepest at $r=0$, where the even/$S$ channel binds and the odd/arrow $A$ channel is blind), with simplicity and isolation exact at each finite $X$; the residual is the *uniform-in-$X$* persistence of that gap, equal to the apex$\to$archimedean transfer (= RH). And we **place the cubic-chirality candidate correctly**: a matched-pair test shows the $\zeta$ Weil-form gap is *independent* of $L(\tfrac12,\chi_3)$, so cubic chirality is the simple-and-even anchor for the *separate* $\chi_3$ object (GRH$(\chi_3)$), not for $\zeta$'s §6.6a. We also **retire the multiplicative-holonomy compass** as trivial per place — the archimedean $\Gamma$-factor and every finite Euler factor carry *zero* bulk holonomy, so the zeros are irreducibly emergent from the continuation. Every deposit confirms the program's standing reduction of RH to the apex$\to$archimedean convergence, which [CCM25] identifies as RH itself and open. **Structural reduction — real; new content / proof of RH — not achieved.**

**MSC 2020:** 11M26, 11M41, 46E22, 47B25, 11F66.

---

## 1. Introduction

The Connes route ([CCM23], [CCM25], [Connes26]) reaches RH without the Bombieri–Vinogradov / Lindelöf wall: from a finite set of primes it builds a Weil quadratic form whose minimal even eigenvector has zeros on the critical line (the **Connes–van Suijlekom criterion** [CvS], via Carathéodory–Fejér: if the lowest eigenvalue is simple, isolated, with even eigenfunction $\eta$, all zeros of $\widehat\eta$ are real), and a **prolate-operator convergence** $\widehat k_\lambda\to\Xi$ (unconditional, polynomial in $\lambda$) carries the finite truncation to the limit; Hurwitz then forces the zeros onto the line. The program is already on this route: the apex edge operator is the archimedean operator ([N4],[N5]), the de Branges target $E_B=\Xi+i\Xi'$ is [CCM25]'s Theorem 6.1 ([N6]), and the CCM prolate operator is the program's $\mathbb Z/6$ CCM. [CCM25] states the boundary plainly: the prolate$\to$zeros convergence holds *numerically*, and "a rigorous proof of this convergence would establish the Riemann Hypothesis."

This paper is a consolidation, not an advance on that boundary. It records what an honest stress-test of the route produced: a native realization (§3) that operationalizes the [N4]–[N6] identification chain end-to-end; a correction (§2) and a derivation (§4) that repair and extend the program's Weil-form probes; and two retirements (§§5–6) that close a tempting chiral reading and a multiplicative-holonomy reading, each by exhibiting the precise point where it reduces to the standing archimedean convergence. The discipline is the program's: the realization is real and the boundary is sharply named; the boundary is not crossed.

Throughout, $s=\tfrac12+iz$; $\Xi(z)=\xi(\tfrac12+iz)$; $\vartheta$ is the Riemann–Siegel angular function with $2\vartheta'(t)=\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\log\pi$; $\Lambda$ is von Mangoldt; $P_n$ the primorial. Tiers: $\mathsf{[P]}$ proved/certified, $\mathsf{[A]}$ structural identification, $\mathsf{[C]}$ the calibrated open target.

---

## 2. Correction: the finite-prime Weil form reproduces the zeros $\mathsf{[P]}$

\hypertarget{stmt:2-1}{}
**Theorem 2.1 (the finite Weil form is a faithful zero-generator).** *Let the even-sector Riemann–Weil quadratic form be discretized on a position grid in $u=\log x$ with the **exact** archimedean kernel*
$$K_\infty(u)=-\,\frac{e^{-|u|/2}}{1-e^{-2|u|}},\qquad \text{pole term }2\cosh\tfrac{u-u'}2,\qquad \text{primes }-2\!\!\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n},$$
*and diagonalized in its parity blocks (the form commutes with $u\mapsto-u$, the functional equation $s\leftrightarrow1-s$). Then the even ground eigenvector's Fourier zeros reproduce the first eight zeros of $\zeta$ (8/8, $|\mathrm{err}|<0.2$) for $X\in\{13,30,60\}$ ($=P_6,P_{10},\dots$).* Certified `probe_weil_form_v3.py`, re-run `probe_weil_chiral_z6_margins.py` (Gate 1).

**Remark 2.2 (what failed, and why — corrected).** An earlier program build (`probe_weil_form_simplicity`) and a first cosine/frequency build placed the minimal-eigenvector's first Fourier zero near $1$–$3.5$, not $14.13$, and were read as evidence that the raw Weil form cannot generate the zeros. **That reading is withdrawn — and the cause is now pinned to two diagnosed defects, neither of them the choice of basis.** *(i) A precision floor.* The distinguished eigenvalue is $\sim10^{-37}$, far below float64 resolution, so a double-precision diagonalization returns a noise-mixed vector; the cluster only resolves in high precision (mpmath, $\mathrm{dps}\gtrsim50$). *(ii) Eigenvector mis-selection.* Connes' $\eta$ is **not** the global minimum of the Weil form but the converged extreme of the near-degenerate minuscule-eigenvalue cluster (§3, Rem 3.6); the global minimum is the smooth low-frequency mode whose first Fourier zero is the spurious $\sim0.6$–$3.5$. Once both are fixed, the **frequency/cosine basis reproduces the zeros to $\sim10^{-19}$** (and the exact position-space kernel of Theorem 2.1 to $\sim10^{-50}$, §3): the basis was never the obstruction. The distinction matters: the program's own §6.6a probes were stalling on a precision-plus-selection artifact, not a wall and not a discretization deficiency. Certified `probe_connes_why_float64_fails.py`, `probe_connes_miracle_highprec.py`.

---

## 3. The apex-native realization $\mathsf{[P]}/\mathsf{[A]}$

We assemble the form of §2 from the program's native objects rather than from the textbook explicit formula, and ask whether the zero-reproduction *emerges* from the apex construction or only *coincides* with it after the [N4]–[N6] identification.

\hypertarget{stmt:3-1}{}
**Theorem 3.1 (the apex unitary, holding the object).** *The apex unitary $U_N=\langle\text{Helmert}_k\mid\text{Fourier}_j\rangle$ on the mean-zero hyperplane of $\mathbb C^N$ has the closed form $(U_N)_{kj}=\big[(\omega^{jk}-1)/(\omega^j-1)-k\,\omega^{jk}\big]/\sqrt{N\,k(k+1)}$, $\omega=e^{2\pi i/N}$, and $\sqrt N\,(U_N)_{kj}\to k(uv)=\tfrac{e^{2\pi iuv}-1}{2\pi iuv}-e^{2\pi iuv}$ with $u=k/\sqrt N$ — the [N4] edge kernel (certified: error $0.033\to0.016\to0.008$ for $N=500,2000,8000$).*

\hypertarget{stmt:3-2}{}
**Theorem 3.2 (the archimedean kernel is the apex symbol).** *The even symbol of the apex kernel, $c(s)=\int_0^\infty\cos(2\pi w)\,w^{s-1}\,dw=\tfrac12\,\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$ ([N4, Lem. 5.1]), is unimodular on the line, and its phase velocity is the archimedean density:*
$$2\vartheta'(t)=\frac{d}{dt}\arg\!\big(2\,c(\tfrac12+it)\big)=\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\log\pi,$$
*to machine zero ($|\mathrm{err}|=0$ at $t=1,5,10,14$). The archimedean kernel of §2 is the inverse transform of this apex symbol.*

\hypertarget{stmt:3-3}{}
**Theorem 3.3 (the prime side is the conductor-block local zeta).** *For each prime $p$ the conductor block $(\mathbb Z/p)^\times$ carries the local zeta $Z_p(s)=(1-p^{-s})^{-1}$ — its Frobenius-monodromy ($c\mapsto pc$, [N1]) generating function — and its logarithmic derivative generates the von Mangoldt weights exactly:*
$$-\frac{d}{ds}\log Z_p(s)=\sum_{k\ge1}\Lambda(p^k)\,p^{-ks},\qquad \Lambda(p^k)=\log p .$$
*Certified for $p\le13$. The prime side of §2 is therefore not plugged in; it is the conductor-block log-derivative.*

\hypertarget{stmt:3-4}{}
**Theorem 3.4 (native reproduction).** *The form of §2, with the archimedean kernel sourced from the apex symbol (Thm 3.2) and the prime weights from the conductor blocks (Thm 3.3), reproduces the first eight zeros of $\zeta$ (8/8) at $P_6$ and $P_{10}$.* Certified `probe_apex_native_weil.py`.

**Remark 3.5 (emergence vs. identification — the honest split).** The realization is genuine, but the two halves differ in status, and a theorem decides which.
- *Primes — native-exact.* Theorem 3.3 is a derivation: the von Mangoldt weights **are** the conductor-block local-zeta log-derivative. This half *emerges*.
- *Archimedean — native $=$ identification, by [N4].* The apex symbol density equals $2\vartheta'$ **exactly** (Thm 3.2, $|\mathrm{err}|=0$) because [N4] *proved* apex-symbol $=$ $\Gamma$-factor $\mathsf{[P]}$. On this half "emerges from $U_N$" and "identified with the explicit formula" are the same statement — by theorem, not by hand.

The only purely-finite-native residue — reproducing the zeros from a *crude* finite $U_N$ before the operator limit — is gated by the apex$\to$archimedean convergence (Thm 3.1's error $\to0$), which is the standing open content (§7). Thus §3 is a **validated native realization** of the [N4]–[N6] chain (the apex$+$conductor object *is* Connes' object, sourced end-to-end and shown to reproduce the zeros), and it is **not** new content: it confirms the identification rather than supplying a lever the explicit formula lacked.

**Remark 3.6 (the distinguished eigenvector, the cluster, and the achieved precision).** Two facts make the reproduction precise and explain the earlier failures (Rem 2.2). *First, $\eta$ is a cluster extreme, not the global minimum.* The Weil operator's low spectrum is a band of eigenvalues with a near-degenerate **cluster accumulating at $L=-2.90345\ldots$** — a genuine spectral invariant, identical to $34$ digits across $N=44$ and $N=64$ — separated by a large gap from an isolated high eigenvalue. Connes' $\eta$ is the *converged extreme* of that cluster (the member adjacent to the gap), selected non-circularly by the largest internal spectral gap; the **within-cluster splittings $7.85\!\times\!10^{-17},3.57\!\times\!10^{-21},\dots,4.75\!\times\!10^{-42}$ are exactly the minuscule-eigenvalue tower** ($1-\chi_2$, [CCM23] §6.4). Taking the global minimum instead yields the smooth low-frequency mode with spurious first zero $\sim0.6$–$3.5$ (Rem 2.2). *Second, the achieved agreement.* With $\eta$ so selected and high precision, $|\widehat\eta\text{-zero}-\gamma_n|$ is $\sim10^{-19}$ for the first eleven zeros in the cosine/frequency basis ($N=30$, $\mathrm{dps}=60$) and $9.2\!\times\!10^{-50},\,2.9\!\times\!10^{-47},\dots,3.8\!\times\!10^{-37}$ for $n=1,\dots,8$ with the exact $u$-space kernel ($N=64$, $\mathrm{dps}=85$) — within $\sim5$ orders of Connes' published $2.6\!\times\!10^{-55}$, the gap closing with $N$ and precision. The evenness defect of $\eta$ is $0$ to machine precision. Certified `probe_connes_miracle_highprec.py`, `probe_connes_miracle_fast.py` (cross-checked entry-by-entry to $10^{-52}$).

---

## 4. The chiral archimedean kernel $\mathsf{[P]}$

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (the $\chi_3$ position-space kernel).** *The metric kernel $K_\infty(u)=-e^{-|u|/2}/(1-e^{-2|u|})=-\sum_{k\ge0}e^{-(2k+1/2)|u|}$ has exponents $(2k+\tfrac12)$ — the poles of $\psi(\tfrac14+\tfrac{ir}2)$. The character $\chi_3$ is odd ($\chi_3(-1)=-1$); its $\Gamma$-factor is $\Gamma((s+1)/2)$, giving density $\psi(\tfrac34+\tfrac{ir}2)$ with poles at $(2k+\tfrac32)$. Hence the chiral archimedean kernel is*
$$\boxed{\,K_{\chi_3}(u)=-\,\frac{e^{-3|u|/2}}{1-e^{-2|u|}}\,},$$
*with no pole term ($L(s,\chi_3)$ entire) and $\chi_3$-twisted primes $-2\sum_n\chi_3(n)\Lambda(n)n^{-1/2}$.* This is the carrier-channel ($\xi\cdot L_{\chi_3}$, [N6 §3]) extension of §2, derived rather than fitted; it is used in §5 and is reusable for any two-channel build.

---

## 5. Connes' §6.6a: the structural half discharged, the chiral candidate placed $\mathsf{[P]}/\mathsf{[A]}$

Connes' §6.6a condition is that the lowest eigenvalue of the Weil form is **simple, isolated, and even** ([CvS]). The prolate half is a clean PSWF theorem (`probe_prolate_simple_even.py`, verified). We separate what the finite Weil form settles from what remains, and correct the program's prior reading of the chiral channel.

**Even, and simple+isolated at each $X$ $\mathsf{[P]}$.** In the even (cosine) sector every eigenvector is even by construction (defect $0$, machine precision), and the distinguished $\eta$ (the cluster extreme, Rem 3.6) is simple and isolated at every finite $X$: its gap to the next cluster member is $\mathrm{eps}_1>0$ strictly ($1.41\!\times\!10^{-40}$ at $X=13$, stable across $\mathrm{dps}$), the matrix being a fixed exact object. Verifying $\mathrm{eps}_1$ at larger $X$ needs precision growing with $X$ — the same lesson as Rem 2.2 — but the splitting is positive by the prolate mechanism. Certified `probe_step_a_structural.py`.

\hypertarget{stmt:5-1}{}
**Theorem 5.1 (even-beats-odd, structurally).** *Build the odd (sine) sector separately with the correct pole term — the Weil pole/main term $|\widehat f(\tfrac i2)|^2+|\widehat f(-\tfrac i2)|^2$ is a sum of squares, hence $+2(\int f\sinh\tfrac u2)^2$ in the odd sector (positive). The even–odd ground split is*
$$\Delta=\lambda_0^{\mathrm{odd}}-\lambda_0^{\mathrm{even}}=+1.65\ (\text{archimedean})\ \longrightarrow\ +0.074\ (\text{archimedean}+\text{pole}),$$
*even winning at each level.* Certified `probe_even_beats_odd_archimedean.py`. The mechanism is the program's **symmetric/antisymmetric (CBS) split**: $2\vartheta'(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}2)-\log\pi$ is deepest at $r=0$ ($\approx-5.37$); even functions have $\widehat f(0)=\int f\ne0$ and bind the bottom of the archimedean well, while odd functions have $\widehat f(0)=0$ (vanishing quadratically) and are *blind* to it — the even/$S$ channel binds, the odd/arrow $A$ channel (the apex non-normality, the $\sqrt i$ phase of [N4]) cannot. This is the apex$=$prolate Slepian ordering $\chi_0>\chi_1$ (even ground). $\eta$ is **not** nodeless (Fact 6.2: $\eta\sim E(h)$, $h$ a vanishing-integral Hermite combination), so the Perron–Frobenius "nodeless ground state" route reaches the *archimedean* ground, not $\eta$; the vehicle for $\eta$'s simplicity is the prolate Sturm spectrum transported by trace-formula closeness — the open §6.6a transfer.

**Remark 5.2 (the full-form margin is sub-floor — a precision artifact, not a structural ambiguity).** When the pole and primes are assembled into the full order-2 grid form, the even–odd split collapses to $O(10^{-4})$ and is sign-unstable under grid refinement (metric $+,-,+,+$; carrier $\zeta\cdot L_{\chi_3}$ $-,-,-,+$ across $N\in\{300,\dots,800\}$; `probe_weil_chiral_z6_margins.py`). This is the *same* precision floor as Rem 2.2: the full-form low spectrum is exp-small ($\sim10^{-19}$), so a low-precision split is noise — not a refutation of Theorem 5.1's archimedean-level result. The marginality has a clean anatomy: the archimedean step favors even by $\Delta=+1.65$; the pole, correctly signed, eats $96\%$ of that margin ($\to+0.074$); and the prime term is *not* a small perturbation but a load-bearing one (operator norm $2\sum_{n\le13}\Lambda(n)/\sqrt n\approx9.9$, comparable to the archimedean scale), bringing the whole low spectrum to the exp-small Weil scale. Even-ground survives as a **three-way near-cancellation**; its *uniform-in-$X$* persistence is the open content (= the transfer, §7).

**Corollary 5.3 (the cubic-chirality candidate, placed) $\mathsf{[P]}/\mathsf{[A]}$.** The program's hypothesis was that cubic chirality ($c_2<0$, anchored by $L(\tfrac12,\chi_3)\ne0$) keeps the §6.6a margins of the *zeta* Weil form positive ([N5 Rem 6.4]). A matched-pair test places it correctly. The $\zeta$ Weil form $QW_\lambda$ contains no $\chi_3$ data; accordingly its simplicity gap is **bit-identical** ($1.41\!\times\!10^{-40}$ at $X=13$) across substituted values $L(\tfrac12,\chi_3)\in\{0,0.48,0.96,1.0\}$ — only fabricating a $\chi_3$ block changes it (`probe_chi3_gap_falsifier.py`). The reason is a conflation of two distinct involutions: §6.6a for $\zeta$ is the **test-function parity** $u\mapsto-u$ (the functional equation $s\leftrightarrow1-s$ — the CBS $S/A$ split of Theorem 5.1), whereas $L(\tfrac12,\chi_3)$ governs the **Dirichlet-character parity** ($\zeta$ even vs $L(\cdot,\chi_3)$ odd) — the metric/chiral channel split, which is GRH$(\chi_3)$, a *separate* instance of §6.6a. Cubic chirality is therefore the simple-and-even anchor for the $\chi_3$ object — where $L(\tfrac12,\chi_3)\ne0$, root number $W(\chi_3)=+1$, *is* the central non-degeneracy — not for $\zeta$'s §6.6a. The decisive open object for $\zeta$ remains the analytic transfer $QW_\lambda\approx PW_\lambda$ ([CCM25] §6.4, [Connes26] §6.4): the prolate$\to$zeros convergence, RH itself (§7). In SUSY-QM terms [P∞-A §7] the two involutions are the two gradings of the supercharge $H=\mathcal Q^\dagger\mathcal Q$: the test-function parity is the fermion parity $(-1)^F=\theta$ that grades $\zeta$'s own Weil form, whereas the Dirichlet-character parity is the *auxiliary* $\chi_3$ grading — so a $K_{\chi_3}$-graded supercharge realizes GRH$(\chi_3)$, not $\zeta$'s §6.6a; the matched-pair gap above is exactly the certificate of that separation.

---

## 6. Retirement II: the multiplicative-holonomy compass is trivial per place $\mathsf{[P]}/\mathsf{[A]}$

[N6 Rem 6.3] casts RH as the triviality of the bulk holonomy of $\omega=d\log\xi$; an off-line zero is one curvature atom. Holonomy is intrinsically *multiplicative* (a $\pi_1$ representation), and $\xi$ factors over places: $\xi(s)=\tfrac12 s(s-1)\,Z_\infty(s)\prod_pZ_p(s)$ with $Z_\infty=\pi^{-s/2}\Gamma(s/2)$, $Z_p=(1-p^{-s})^{-1}$. This suggested a *multiplicative$+$archimedean* compass — the one shape [N11 §7] left un-refuted. We test it.

\hypertarget{stmt:6-1}{}
**Theorem 6.1 (each local factor has zero bulk holonomy).** *On a contour enclosing the first zero $\tfrac12+14.1347\,i$, the winding $\tfrac1{2\pi i}\oint d\log(\cdot)$ is $1$ for $\xi$ and for $\zeta$, and $0$ — to machine zero — for the archimedean factor $Z_\infty$, for every finite Euler factor $Z_p$, and for the finite Euler product $\prod_{p\le47}Z_p$. The enclosed zero is carried by **none** of the explicit local factors; it is irreducibly in the analytic continuation of $\zeta$.* Certified `probe_holonomy_factorization.py` (Tests 1–2).

\hypertarget{stmt:6-2}{}
**Theorem 6.2 (the winding density is archimedean).** *The winding density decomposes as $N(T)=\vartheta(T)/\pi+1+S(T)$, an exact integer at each height; the smooth winding is the archimedean $\vartheta(T)/\pi\sim(T/2\pi)\log(T/2\pi)$, and the primes contribute only the bounded fluctuation $S(T)=\tfrac1\pi\arg\zeta(\tfrac12+iT)$.* Certified (Test 3: $S=-0.38,+0.58,-0.002,-0.19$ at $T=20,50,100,200$).

**Corollary 6.3 (the compass is retired) $\mathsf{[A]}$.** The multiplicative holonomy factorization is **trivial per place**: neither the explicit archimedean $\Gamma$-factor nor any finite Euler factor/product carries a zero, so it supplies no free local positivity. It relabels archimedean domination of the winding density (Thm 6.2) plus the open control of the prime fluctuation $S(T)$ — the standing archimedean content, now in winding form. The compass does **not** open a new handle; it is retired as a free path.

**Remark 6.4 (the surviving distinction points to the function-field door) $\mathsf{[A]}$.** Over a function field the *same* factorization is **non-trivial per place**: the local Frobenius factors carry the zeros, their eigenvalue phases forced onto $|\alpha|=\sqrt q$ by the Weil/Hodge intersection positivity on $C\times C$. The $\mathbb Q$-vs-$\mathbb F_q$ gap is exactly that the finite places carry *no* holonomy over $\mathbb Q$ (Thm 6.1) but *do* over $\mathbb F_q$. The genuine locus of multiplicative positivity is therefore the intersection form (the function-field door, [N7 §5], [N10 §6]), not an archimedean-holonomy factor — consistent with [N11 Prop 6.1] (additive positivity is definite$\iff$vacuous; the contentful definite object is the multiplicative $\mathbb F_q$ Hodge form).

---

## 7. Honest status

\hypertarget{stmt:7-1}{}
**Proved / certified $\mathsf{[P]}$:** the finite-prime Weil form reproduces the zeros (Thm 2.1), to $\sim10^{-19}$ (cosine basis) and $\sim10^{-50}$ (exact kernel) once $\eta$ is taken as the minuscule-cluster extreme at high precision (Rem 3.6, correcting the prior negative and its mis-diagnosis as a basis defect, Rem 2.2); the apex unitary converges to the [N4] kernel (Thm 3.1); the apex even symbol is the archimedean density $2\vartheta'$ exactly (Thm 3.2); the conductor-block local-zeta log-derivative is the von Mangoldt prime side (Thm 3.3); the native form reproduces the zeros (Thm 3.4); the chiral archimedean kernel (Prop 4.1); $\eta$ is even and simple+isolated at each finite $X$ ($\mathrm{eps}_1>0$), and even-beats-odd holds at the archimedean level ($\Delta=+1.65\to+0.074$) by the symmetric-binds/arrow-blind mechanism (§5, Thm 5.1); the $\zeta$ §6.6a gap is independent of $L(\tfrac12,\chi_3)$ (matched-pair, Cor 5.3); each local holonomy factor is bulk-trivial and the winding density is archimedean (Thms 6.1–6.2).

**Structural $\mathsf{[A]}$:** the native realization is the [N4]–[N6] chain operationalized, with the archimedean half's nativeness resting on the proven apex-symbol $=$ $\Gamma$-factor identity, hence a validated realization and not new content (Rem 3.5); the structural half of §6.6a (even, simple+isolated-at-fixed-$X$, even-beats-odd) is discharged by the apex/CBS mechanism, leaving the *uniform-in-$X$* persistence — the analytic transfer $QW_\lambda\approx PW_\lambda$ on the prolate operator — as the open content (§5); the cubic-chirality candidate is the simple-and-even anchor for the *separate* $\chi_3$ object / GRH$(\chi_3)$, not for $\zeta$ (Cor 5.3); the multiplicative-holonomy compass is trivial per place and retired (Cor 6.3); the $\mathbb Q$-vs-$\mathbb F_q$ gap localizes multiplicative positivity to the intersection form (Rem 6.4).

**Open — and equal to RH $\mathsf{[C]}$:** the apex$\to$archimedean convergence — equivalently the transfer $QW_\lambda\approx PW_\lambda$ / the prolate$\to$zeros convergence — which [CCM25] identifies as a statement whose rigorous proof would establish the Riemann Hypothesis, and which every route of this session (native realization, chiral §6.6a, holonomy) again terminates at.

This paper records a validated native realization, a correction, a derivation, and two honest retirements; it does **not** prove the Riemann Hypothesis and does not add new content beyond the [N4]–[N6] reduction. Its value is hygiene: the apex$+$conductor object is shown to generate Connes' object end-to-end and reproduce the zeros; two tempting readings are closed at the exact point each reduces to the standing convergence; and the program's prior numerical stalls are diagnosed as discretization, not structure. **Structural reduction — real; new content / proof of RH — not achieved.**

---

## References

[N0] Murillo Montero, L. (2026). *The Closure.*

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$.*

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.*

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.*

[N6] Murillo Montero, L. (2026). *The Unified Archimedean Operator and the de Branges Target for $\xi$.*

[N7] Murillo Montero, L. (2026). *The Single Object.*

[N9] Murillo Montero, L. (2026). *The Cross-Prime Fusion Criterion.*

[N10] Murillo Montero, L. (2026). *The Bures–Cayley Geometric Reduction of RH and Its Ceiling.*

[N11] Murillo Montero, L. (2026). *The Capstone: One Wall, Mapped.*

[P∞-A] Murillo Montero, L. (2026). *The de Branges Apparatus as Osterwalder–Schrader Reconstruction.* (§7 the SUSY supercharge $H=\mathcal Q^\dagger\mathcal Q$; BPS $=$ zeros; the $(-1)^F=\theta$ vs $\chi_3$-grading guardrail.)

[CCM23] Connes, A., Consani, C., Moscovici, H. (2023/2024). *The prolate operator and the zeros of zeta.* arXiv:2310.18423.

[CCM25] Connes, A., Consani, C., Moscovici, H. (2025). *Zeta Spectral Triples.* arXiv:2511.22755. (The prolate→zeros convergence is numerical; a rigorous proof of it would establish RH.)

[CvS] Connes, A., van Suijlekom, W. (2025). *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.* Comm. Math. Phys. 406:12 (arXiv:2511.23257). (The abstract criterion: a lower-bounded self-adjoint quadratic form on $[-\tfrac L2,\tfrac L2]$ whose lowest eigenvalue is simple, isolated, with even eigenfunction $\eta$ has all zeros of $\widehat\eta$ real; Carathéodory–Fejér + Hurwitz. The source of "Theorem 6.1".)

[Connes26] Connes, A. (2026). *The Riemann Hypothesis: Past, Present and a Letter Through Time.* arXiv:2602.04022. (Survey + the finite-prime Weil-form route; §6.4 the prolate approximation $k_\lambda$, §6.6 the remaining steps.)

[CC20] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77 (arXiv:2006.13771).

[Weil] Weil, A. (1952). *Sur les "formules explicites" de la théorie des nombres premiers.* Comm. Sém. Math. Univ. Lund, 252–265.

[dB] de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice–Hall.
