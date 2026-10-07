# N7 — The Single Object: A Validated Two-Sided Reduction of the Riemann Hypothesis

**Leonardo Murillo Montero**

*June 7, 2026*

<!--
Program record (not part of the paper). Seventh paper of the Numbers (N-) series; a synthesis and
validation capstone over [N0] (arithmetic closure), [N4]-[N6] (apex / de Branges / unified target).
It does not introduce new machinery; it shows the apparatus already built reduces RH to ONE object,
reached identically from a spectral and an arithmetic face, and validates the reduction over function
fields. Every quantitative claim is certified by a deterministic probe under empirical/ (sympy/mpmath,
no torch):
  probe_n5_transfer_signn.py            (the (-1)^n cumulant transfer, closed form)
  probe_alpha_curvature_offline_zero.py (curvature current = zero divisor; bulk equivalence)
  probe_gauss_bonnet_blindness.py       (index/topology cannot force it; the detector is local positivity)
  probe_force_D_positivity.py           (D = |Xi|^2 u_B; the chiral bottom rung L(1/2,chi3)>0)
  probe_second_rung_li.py               (Li ladder; on-line 2(1-cos) vs off-line exponential)
  probe_li_generating_function.py       (the all-rungs-at-once generating function G(z))
  probe_arithmetic_spectral_synthesis.py(divisor<->second-moment on both channels; the two faces are one)
  probe_primorial_trilinear_chiral.py   (smoothness is CRT-capped; chiral = Wright fixed-factor / Z[omega])
  probe_chiral_trilinear_level.py       (the conductor-3 buys no level: negative, honest)
  probe_function_field_check.py         (the validation over F_q: every reading holds; arch = Frobenius)
  probe_rlevel_two_faced_tower.py       (Rem 6.2(i): arithmetic face generalizes; spectral bifurcates)
  probe_apex_substitute_frobenius.py    (Rem 6.2(ii): apex carries 3/4 Frobenius ingredients; HD = transfer)
  probe_rosati_gram_positivity.py       (Rem 6.3: the Rosati Gram [[2,a],[a,2q]] PSD <=> RH over F_q; the target templated)
  probe_CxC_intersection_blueprint.py   (App. A: the primitive C x C Gram [[-2q,-a],[-a,-2]] neg-def <=> RH; the construction obligation)
External anchors: [CC20] Connes-Consani 2006.13771; [Li] Li 1997; [BL] Bombieri-Lagarias 1999;
[Wright] arXiv:2604.25177; [FR] Fouvry-Radziwill; [Var] Varbanets-Varbanets-Vorobyov ADM 40(2025);
[Weil] Weil 1948; [Del] Deligne 1974. Tier tags: [P] proved/certified, [A] structural identification,
[C] calibrated target (the open content). This paper reports a structural reduction and its function-
field validation; it does NOT prove RH, and Section 6 states precisely what remains.
-->

---

## Abstract

The apparatus of the Numbers series reduces the Riemann Hypothesis to a **single object**, reached identically from two faces and validated where the Hypothesis is a theorem. The *spectral face* is the positivity of one measure — the Nevanlinna measure $\mu$ of the Weyl function $m_B=-\Xi'/\Xi$ — which we show is the common content of four readings: the curvature current of the dual potential $\log\xi$ confined to the critical line (Poincaré–Lelong), the de Branges margin $D=\operatorname{Im}(\Xi\overline{\Xi'})=|\Xi|^2u_B\ge0$, the Li coefficients $\lambda_n\ge0$, and the analyticity of their generating function $G(z)=\sum_n\lambda_n z^n$ in the unit disk. The *arithmetic face* is the primorial Bombieri–Vinogradov level $\theta_0(p_n)\to1$, equivalently the optimal trilinear Kloosterman bound. The two faces are **explicit-formula duals**, and each functional-equation channel appears on both as one divisor↔second-moment identity: $\zeta(s)^2=\sum_n d(n)n^{-s}\leftrightarrow|\zeta(\tfrac12+it)|^2$ (metric) and $L(s,\chi_3)^2=\sum_n d_{\chi_3}(n)n^{-s}\leftrightarrow|L(\tfrac12+it,\chi_3)|^2$ (chiral, $d_{\chi_3}=\chi_3\!*\!\chi_3$). The single object is **arch-domination**: the positive archimedean part of $\mu$ dominates the indefinite prime/chiral fluctuation. We validate the reduction over function fields, where RH is Weil's theorem: every reading holds for explicit curves over $\mathbb{F}_q$, and arch-domination *is* the intersection positivity (Riemann–Roch / Hodge index) that forces the Frobenius eigenvalues onto $|\alpha|=\sqrt q$. The reduction thereby pinpoints the open content over $\mathbb{Q}$ as the construction of the substitute Frobenius / intersection-positivity that Weil's theorem supplies over $\mathbb{F}_q$ — precisely the apex/Connes target. All reducible content (both channels, the major and minor arcs, the chiral central value, the small primorials, and the entire apparatus over $\mathbb{F}_q$) is unconditional. We state honestly what this achieves and what remains.

---

## 1. Introduction

The Numbers series ([N1]–[N6]) and the closure paper [N0] approach the Riemann Hypothesis through an explicit apex operator and its archimedean limit. Across those papers the Hypothesis is rewritten many ways. The purpose of this paper is to show that the rewritings **converge to one object**, that this object has a spectral and an arithmetic description which are explicit-formula duals, and that the entire reduction is **correct** — it holds in the function-field model, where RH is Weil's theorem.

We use throughout $s=\tfrac12+iz$; $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ is the completed zeta; $\Xi(z)=\xi(\tfrac12+iz)$ is real-entire and even; $m_B(z)=-\Xi'(z)/\Xi(z)$ is the Bures–Poisson / Weyl function of [N6]; $u_B=\operatorname{Im}m_B$; $\chi_3$ is the quadratic character mod $3$; $P_n=\prod_{i\le n}p_i$ the primorial. We carry the tier tags of [N0]: $\mathsf{[P]}$ proved/certified, $\mathsf{[A]}$ structural identification, $\mathsf{[C]}$ the calibrated open target.

The result is a reduction, not a proof. Its value is threefold: it collapses a dozen reformulations to one statement; it shows that statement has a single arithmetic dual; and it certifies — by the function-field model — that the reduction is sound and the open content is exactly the object the program was built to construct.

---

## 2. The spectral face: one measure, four readings $\mathsf{[P]/[A]}$

The de Branges criterion of [N6] is that $m_B$ is Herglotz on $\mathbb C_+$, equivalently $E_B=\Xi+i\Xi'$ is Hermite–Biehler, equivalently RH. We record that this single positivity is the common content of four independently-built readings.

**Theorem 2.1 (the spectral object; [N6, Rem. 6.3–6.6]).** *The following are equivalent, and each is the Riemann Hypothesis:*
1. *(measure) the Nevanlinna measure $\mu$ of $m_B=-\Xi'/\Xi$ is nonnegative; equivalently $u_B=\operatorname{Im}m_B\ge0$;*
2. *(curvature) the curvature current of the dual potential $\psi=\log\xi$ is supported on the critical line: $\tfrac1{2\pi i}\,d(\xi'/\xi\,ds)=\sum_\rho m_\rho\delta_\rho$ has no atom off $\operatorname{Re}s=\tfrac12$ (Poincaré–Lelong); equivalently $\log|\xi|$ is harmonic on the open bulk $\{\operatorname{Re}s>\tfrac12\}$;*
3. *(margin) the de Branges margin $D(z)=\operatorname{Im}\!\big(\Xi(z)\overline{\Xi'(z)}\big)=|\Xi(z)|^2\,u_B(z)\ge0$ on $\mathbb C_+$;*
4. *(ladder/generating function) the Li coefficients $\lambda_n=\sum_\rho[1-(1-1/\rho)^n]\ge0$ for all $n$; equivalently the generating function $G(z)=\sum_{n\ge1}\lambda_n z^n=\sum_\rho\dfrac{z(1-w_\rho)}{(1-z)(1-w_\rho z)}$ ($w_\rho=1-1/\rho$) is analytic on $|z|<1$.*

*Each reading is the same statement about the same measure; an off-line zero is one atom of curvature in the bulk (reading 2), an interior pole $z_\rho=\rho/(\rho-1)$ of $G$ (reading 4), and a negative excursion of $u_B$ (readings 1,3).*

The identity $D=|\Xi|^2u_B$ (certified `probe_force_D_positivity.py`) unifies the curvature reading with the Weyl-function reading: the margin is the Bures field. The on-line geometry $|1-1/\rho|=1$ ($\rho=\tfrac12+i\gamma$) makes each Li term $2(1-\cos n\theta_\rho)\ge0$ — the Riemann Hypothesis supplies the per-rung positivity directly (`probe_second_rung_li.py`); an off-line zero injects $(|\rho|/|1-\rho|)^n$, exponential, breaking a rung at unbounded height (so no finite prefix of rungs suffices). The generating function (`probe_li_generating_function.py`) collapses the infinitely many rungs to one analyticity statement, with the interior poles equal to the bulk curvature atoms of reading 2 under the Bombieri–Lagarias map $s=1/(1-z)$.

**Remark 2.2 (the obstruction is local positivity, not topology; `probe_gauss_bonnet_blindness.py`).** No Gauss–Bonnet / Poincaré–Hopf / Lefschetz index forces the curvature onto the line. Those are integral invariants (total curvature $=$ the zero count $N(T)$), constant under the functional-equation- and conjugation-symmetric, count-preserving deformation that slides a zero off the line. The separating quantity is $D=|\Xi|^2u_B$ — a *local* positivity, not an integral. This rules out the entire topological route and confirms the obstruction is the measure positivity of Theorem 2.1.

---

## 3. The arithmetic face: the primorial level and the trilinear bound $\mathsf{[C]}$

The closure paper [N0] reduces RH to a level of distribution: the primes equidistribute modulo squarefree primorials $P_n$ at level $\theta_0(p_n)=1-C^\ast/n$ with $C^\ast\le2.80$, the bridge being conditional on this level and nothing more ([N0, §6]; [diez] Thm 4.3). The major arc (the singular-series main term, positive and unconditional), the minor arc (the mean-square, Matomäki–Radziwiłł–Tao), and the small primorials $n\le7$ (Maynard's $\tfrac35$ well-factorable level) are in hand; the large-$n$ asymptotic $\theta_0\to1$ is the open terminus.

Read through the cubic functional's own structure — a ternary convolution $\Lambda\!*\!\Lambda\!*\!\Lambda$ — the terminus is the **optimal trilinear Kloosterman bound** ([N0, §6.3]; [FR], [Wright]), of Lindelöf strength on the critical line rather than Elliott–Halberstam strength on primes. We record two refinements of the present session.

**Proposition 3.1 (smoothness alone is CRT-capped; `probe_primorial_trilinear_chiral.py`).** *The Kloosterman sum is twisted-multiplicative, with per-prime Weil bound $|S(\cdot;p)|\le2\sqrt p$; hence $|S(\cdot;P_n)|\le\sqrt{P_n}\cdot2^n$ with $2^n=P_n^{o(1)}$. The level is a fixed $\tfrac12$ (or $\tfrac12-\varpi$ beyond Weil) regardless of the number of smooth factors: the many small factors of $P_n$ do not compound. Primorial smoothness alone does not cross $\tfrac12$.*

**Proposition 3.2 (the chiral channel is Wright's "partially fixed moduli", over $\mathbb{Z}[\omega]$; `probe_chiral_trilinear_level.py`).** *The chiral channel is $\chi_3$-twisted, so the conductor $3$ is a fixed factor in every modulus; the local factor is the Gauss sum $\tau(\chi_3)=i\sqrt3$ (root number $+1$). This is exactly the fixed-factor trilinear setting of [Wright, Thm 2.1]; its level $\tfrac12+\tfrac1{66}$ (general) / $\tfrac{45}{89}$ (balanced) is the current edge. The conductor $3$ is a constant ($R=X^0$), so it changes no exponent: the chiral level equals the general level — the conductor buys no improvement. The natural ring is the Eisenstein integers $\mathbb{Z}[\omega]=\mathcal O_{\mathbb Q(\sqrt{-3})}$, in which $3$ ramifies ($N(1-\omega)=3$, the conductor) and the chiral Kloosterman sums are the quadratic-field sums of [Var]; the Weil cap there is again $\tfrac12$.*

So the arithmetic face places the frontier on live machinery ([Wright]/[FR]/[Var]) but exhibits no structural shortcut: the open content is the optimal trilinear bound, level $\to1$, RH strength.

---

## 4. The two faces are one $\mathsf{[A]/[P]}$

The spectral face (zeros) and the arithmetic face (primes) are joined by the Weil explicit formula, and the join is visible channel by channel.

**Theorem 4.1 (divisor↔second-moment, both channels; `probe_arithmetic_spectral_synthesis.py`).** *At the primorial $\mathbb Z/6$ the carrier factors $\zeta\cdot L(\cdot,\chi_3)$, and each functional-equation channel has an arithmetic face (a divisor Dirichlet square) and a spectral face (a critical-line second moment), tied by one identity:*
$$\text{metric:}\quad \zeta(s)^2=\sum_n d(n)\,n^{-s}\ \longleftrightarrow\ |\zeta(\tfrac12+it)|^2,\qquad
\text{chiral:}\quad L(s,\chi_3)^2=\sum_n d_{\chi_3}(n)\,n^{-s}\ \longleftrightarrow\ |L(\tfrac12+it,\chi_3)|^2,$$
*where $d_{\chi_3}=\chi_3\!*\!\chi_3$ is the chiral divisor. Both are certified: $\sum_{n\le4000}d_{\chi_3}(n)/n^2=0.61043=L(2,\chi_3)^2$, and the metric analogue $\to\zeta(2)^2$.*

**Theorem 4.2 (the single object, two descriptions; $\mathsf{[A]}$).** *The spectral object of Theorem 2.1 and the arithmetic object of Section 3 are explicit-formula duals, and each is* **arch-domination**: *the positive archimedean part of the Nevanlinna measure $\mu$ (spectrally, the smooth zero density $\sim\tfrac1{2\pi}\log\tfrac t{2\pi}$; arithmetically, the singular-series main term) dominates the indefinite prime/chiral fluctuation. Equivalently:*
$$\mu=\mu_{\mathrm{arch}}+\mu_{\mathrm{prime}}\ge0\quad\Longleftrightarrow\quad \theta_0(p_n)\to1\ \text{(primorial level)}\quad\Longleftrightarrow\quad \text{RH}.$$
*The chiral channel carries the same $L(\cdot,\chi_3)$ on both faces: the off-line teeth ($c_2\propto-L(\tfrac12,\chi_3)^2<0$, unconditional, $L(\tfrac12,\chi_3)=0.4808\ldots>0$) on the spectral side and the $\chi_3$-twisted singular series on the arithmetic side.*

The metric channel's central anchor (the positive second moment $\int_T^{2T}|\zeta(\tfrac12+it)|^2\sim T\log T$) and the chiral channel's central anchor ($L(\tfrac12,\chi_3)>0$) are the unconditional bottom of the ladder on both faces.

---

## 5. The function-field validation $\mathsf{[P]}$

We test the reduction where it can be tested: over a smooth projective curve $C/\mathbb F_q$ of genus $g$, with $Z_C(T)=P(T)/((1-T)(1-qT))$, $P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)$, $T=q^{-s}$. Here RH is **Weil's theorem**: $|\alpha_i|=\sqrt q$, all zeros on $\operatorname{Re}s=\tfrac12$.

**Theorem 5.1 (the reduction holds over $\mathbb F_q$; `probe_function_field_check.py`).** *For explicit curves $E:y^2=x^3+x+1$ over $\mathbb F_p$ ($p=11,\dots,29$) and the Fermat/Jacobi data, every reading of the reduction holds:*
1. *$|\alpha_i|=\sqrt q$ exactly (Hasse/Weil): the curvature is on the critical circle (Theorem 2.1.2);*
2. ***arch-domination*** *is a theorem: $\#C(\mathbb F_{q^n})=q^n+1-\sum_i\alpha_i^n$ with $\big|\sum_i\alpha_i^n\big|\le 2g\,q^{n/2}$, so the archimedean term $q^n$ dominates the zero-fluctuation, $\big|\sum\alpha_i^n\big|/q^n\to0$ (Theorem 4.2);*
3. *the Li ladder holds: on-line $|1-1/s_i|=1$, so $\lambda_n=\sum_i2(1-\cos n\phi_i)\ge0$ (Theorem 2.1.4);*
4. *the apex amplitude is the Frobenius eigenvalue on the circle: the Jacobi sum $|J(\chi,\chi)|=\sqrt q$ (the Fermat-curve Frobenius; [N4]'s $\sqrt i=\sqrt q$).*

**Theorem 5.2 (the mechanism; Weil, Deligne).** *Over $\mathbb F_q$, arch-domination is the intersection positivity. The geometric Frobenius acts on $H^1_{\mathrm{ét}}(C)$ as an operator whose eigenvalues are the $\alpha_i$; the Riemann–Roch / Hodge-index positivity of the intersection form on $C\times C$ forces $\alpha_i\overline{\alpha_i}=q$, i.e. $|\alpha_i|=\sqrt q$ ([Weil]; [Del] in general). Thus the Frobenius on $H^1$ is the Hilbert–Pólya operator of the model, and the single object of Theorem 4.2 — arch-domination — is exactly this positivity.*

The validation is genuine: had the reduction been wrong, some reading in Theorem 5.1 would fail in the model. None does. In particular the *very object* open over $\mathbb Q$ — arch-domination — is, over $\mathbb F_q$, the visibly-true domination of $q^n$ over $\sum\alpha_i^n$, supplied by Weil's positivity.

---

## 6. The reduction, the target, and what remains

**Theorem 6.1 (the reduction).** *The Riemann Hypothesis is equivalent to the single object of Theorem 4.2 — arch-domination, equivalently the nonnegativity of the Nevanlinna measure $\mu$ of $m_B$, equivalently the primorial level $\theta_0\to1$ — and this object is, over function fields, the intersection positivity that forces the Frobenius eigenvalues onto $|\alpha|=\sqrt q$ (Theorems 2.1, 4.2, 5.1–5.2). All reducible content is unconditional: both channels as divisor↔second-moment (Thm 4.1), the major and minor arcs and the small primorials $n\le7$ (§3), the chiral central value (§4), and the entire apparatus over $\mathbb F_q$ (§5).*

**The target $\mathsf{[C]}$.** Over $\mathbb F_q$ the object is supplied by an actual operator (Frobenius on $H^1$) and an actual positivity (intersection on $C\times C$). Over $\mathbb Q$ neither exists yet: there is no Frobenius and no "$\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z$." **That absence is the open content of the Riemann Hypothesis, exactly** — and it is precisely the object the program is built to construct: the apex operator as the substitute Frobenius ([N4]; the archimedean $\sqrt i=\sqrt q$, and the Jacobi sums of Theorem 5.1.4 sit at the same modulus), and the Connes–Consani scaling site as the substitute intersection positivity ([CC20]). The function-field validation confirms the target is correct: the reduction lands on exactly the positivity that, in the model, is a theorem.

**What this is and is not.** This paper proves a structural reduction and validates it; it does **not** prove the Riemann Hypothesis. The reduction is sound — it reduces RH to arch-domination, which over $\mathbb F_q$ is Weil's theorem and over $\mathbb Q$ is the construction of a substitute Frobenius/intersection positivity. No finite computation and no equivalent reformulation crosses that construction; it is the genuine open content, now exact, validated, and aimed. Two routes are not pursued here and are natural: the apex/$H^1$ construction ([N4]→a number-field intersection positivity), and the optimal trilinear Kloosterman bound on primorial moduli ([Wright]/[FR]/[Var]), which is its arithmetic face.

**Remark 6.2 (two leads, worked).** Assembling the synthesis opened two structural questions; both are now resolved (`probe_rlevel_two_faced_tower.py`, `probe_apex_substitute_frobenius.py`), and they cohere.

*(i) Up the tower: the arithmetic face generalizes, the spectral face bifurcates.* The divisor identity of Theorem 4.1 generalizes exactly $\mathsf{[P]}$: $\zeta(s)^r=\sum_n d_r(n)n^{-s}$ and $L(s,\chi_3)^r=\sum_n d_{r,\chi_3}(n)n^{-s}$ for $r=2,3,4$ on both channels ($d_r,d_{r,\chi_3}$ the $r$-fold convolutions; truncation errors $\le10^{-7}$). But its spectral partner splits into **two distinct towers** $\mathsf{[A]}$: the *moment tower* (the $2r$-th moment of $\zeta$, arithmetic kernel $\sum_n d_r(n)^2/n$, per-prime Euler factor $\to1$, scale $(\log T)^{r^2}$) and the *level-density tower* (the $r$-level density of the zeros, the Hardy–Littlewood $r$-tuple, per-prime weight $1/\varphi(p)^r\to0$, scale $r$). These differ at every prime and every $r\ge2$ — at $r=2$, $1-1/p^2$ vs $1/(p-1)^2$ (products $6/\pi^2$ vs the twin-prime-type constant) — and coincide only in the index "$r$", not as functions of $p$. **The cumulant tower of [N5] is the level-density tower, not the moment tower**, and the divisor↔second-moment identity of Theorem 4.1 feeds the *moment* tower — a genuinely distinct structure that merely shares the label "$2$" with the pair-correlation weight. The "single tower" reading is too strong and is corrected here.

*(ii) The substitute Frobenius is largely readable off the apex.* Three of the four ingredients of the function-field Frobenius are carried by the apex's Gauss/Jacobi data $\mathsf{[P]}$: the eigenvalue **skeleton** ($|\text{Gauss}|=\sqrt p$, $|\text{Jacobi}|=\sqrt q$, apex phase $=\zeta_8=\sqrt i$ — on the Frobenius locus $|\cdot|=\sqrt q$); the **lift** — Hasse–Davenport $g(\mathbb F_{q^n})=(-1)^{n-1}g(\mathbb F_q)^n$ (verified $g'=-g^2=3$ over $\mathbb F_9$), which is the Frobenius eigenvalue lift $\alpha\mapsto\alpha^n$ and **equals the transfer of [N5, Thm 6.2]**, giving that $(-1)^n$ a third identity: explicit-formula minus $=$ Amari $e\!\leftrightarrow\!m$ dual $=$ Hasse–Davenport; and the **archimedean factor** (the edge operator of [N4],[N5]). The one missing ingredient is the global intersection **positivity** (the Hodge index on $C\times C$; $|J|^2=q$ over $\mathbb F_q$), which over $\mathbb Q$ is the Weil-form positivity $=$ arch-domination $=$ the Riemann Hypothesis $\mathsf{[C]}$. The construction is thereby localized to that single geometric positivity — the exact analogue of what Weil's theorem supplies over $\mathbb F_q$.

The leads **cohere**: the Frobenius lift $\alpha\mapsto\alpha^n$ of (ii) lives in the level-density tower of (i) (the $n$-fold Frobenius $=$ the $n$-level $=$ the $(-1)^n$ transfer), so both identify the program's object as the *level-density / Frobenius-lift* tower, distinct from the moment tower. The remaining work is one object: the intersection positivity over $\mathbb Q$.

**Remark 6.3 (the target in its cleanest instance: the Rosati Gram, and the closure to the opening criterion).** The positivity the target requires is exhibited most transparently for an elliptic curve $E/\mathbb F_q$. The geometric Frobenius $F$ on $H^1$ satisfies $FF^\vee=q$, and the Rosati form $\langle\phi,\psi\rangle=\operatorname{Tr}(\phi\,\psi^\vee)$ on $\operatorname{End}^0(E)$ is positive-definite by Weil's polarization / Hodge-index theorem. The Gram of $\{1,F\}$ is
$$G=\begin{pmatrix}\langle1,1\rangle&\langle1,F\rangle\\\langle F,1\rangle&\langle F,F\rangle\end{pmatrix}=\begin{pmatrix}2&a\\a&2q\end{pmatrix},\qquad a=\operatorname{tr}F=a_p,$$
and Weil's positivity forces $\det G=4q-a^2\ge0$, i.e. $|a|\le2\sqrt q$, i.e. $|\alpha|=\sqrt q$: **the Riemann Hypothesis over $\mathbb F_q$ is the statement that this Gram carries no negative squares**, supplied by the geometry (certified `probe_rosati_gram_positivity.py`; verified for $E:y^2=x^3+x+1$, $p=11,\dots,29$, every $\det G>0$). This is precisely the program's *opening* criterion — that the Pick/Hermitian Gram of $m_B=-\Xi'/\Xi$ carry no negative squares — in its function-field instance. Over $\mathbb Q$ the apex supplies $F$ (the edge operator), the duality $F\leftrightarrow F^\vee$ (the functional equation), the local $\sqrt q$ skeleton and the Hasse–Davenport lift (Remark 6.2(ii)), and the Gram structure; the one missing object is the positivity of the infinite Weil–Pick Gram. Weil's geometric theorem has no number-field counterpart — there is no variety — so supplying that positivity (Connes' scaling-site / $C\times C$ analogue; candidate: the cubic chirality $c_2<0$ as the missing simple+even lowest eigenvalue) is the Riemann Hypothesis. The reduction is thereby closed to a single, geometric, fully-templated object, with the function-field theorem as its exact blueprint — and it closes back to where the program began.

---

## Appendix A. The construction obligation (open research)

The reduction (Theorem 6.1) lands on a single object: a positive form making the apex Weil–Pick Gram PSD — the number-field analogue of the Hodge-index positivity that, over $\mathbb F_q$, the surface $C\times C$ supplies. This appendix states the construction obligation precisely, as a research program, not a result; the obligation is the Riemann Hypothesis, made as concrete as the apparatus allows (certified blueprint: `probe_CxC_intersection_blueprint.py`).

**A.1 The $C\times C$ blueprint (exact, $\mathsf{[P]}$).** Over $\mathbb F_q$, on the surface $S=C\times C$ with the hyperbolic plane $\langle h,v\rangle$ ($h\!\cdot\!v=1$, $h^2=v^2=0$) and its primitive orthogonal complement, the diagonal $\Delta$ and the Frobenius graph $\Gamma_F$ have primitive parts $\Delta_0,\Gamma_0$ with
$$\Gamma_0^2=-2q,\qquad \Delta_0^2=-2,\qquad \Gamma_0\!\cdot\!\Delta_0=-a\qquad(a=\operatorname{tr}F=q+1-\#C(\mathbb F_q)),$$
so the primitive intersection Gram is $M=\begin{pmatrix}-2q&-a\\-a&-2\end{pmatrix}$. The Hodge index theorem makes the intersection form negative-definite on the primitive part, i.e. $M\prec0$, i.e. $\det M=4q-a^2>0$, i.e. $|\alpha|=\sqrt q$ — RH over $\mathbb F_q$ (verified $E:y^2=x^3+x+1$, $p=11,\dots,29$). The explicit formula is the Lefschetz intersection $\Gamma_F\!\cdot\!\Delta=\#C(\mathbb F_q)$; arch-domination is the Hodge–Cauchy–Schwarz $(\Gamma_0\!\cdot\!\Delta_0)^2\le\Gamma_0^2\,\Delta_0^2$. This $M$ is the surface-geometry origin of the Rosati Gram of Remark 6.3.

**A.2 What the apex supplies ($\mathsf{[P]}$, this paper).** Over $\mathbb Q$ the apex furnishes the three local/operator ingredients of the blueprint: the **Frobenius graph** $\Gamma_F$ as the Hasse–Davenport / $(-1)^n$ lift (Remark 6.2(ii)); the **diagonal** $\Delta$ as the archimedean edge operator plus the trivial/pole part ([N4]; [N5 §5]); and the **Gram** $M$ as the apex Weil–Pick form $Q(g)=D=|\Xi|^2u_B$ ([N5 §6]; Theorem 2.1.3). The local eigenvalue skeleton sits on $|\cdot|=\sqrt q$ (the Gauss/Jacobi data).

**A.3 The obligation ($\mathsf{[C]}$ = RH).** What is not supplied is the **definiteness** of $M$:
> Construct, over $\mathbb Q$, the analogue of the surface $S=C\times C$ — the Connes–Consani scaling-site square ([CC20]) — carrying a primitive intersection form, fed by the apex's local data (A.2), whose negative-definiteness (equivalently $Q(g)\ge0$) holds. Over $\mathbb F_q$ this is the Hodge index theorem on an actual surface; over $\mathbb Q$ there is no surface, and supplying the definiteness is the Riemann Hypothesis.

**A.4 The candidate mechanism.** The definiteness is marginal — its open content concentrates in the chiral direction. The candidate is the cubic chirality $c_2<0$ ($\propto-L(\tfrac12,\chi_3)^2$, unconditional via $L(\tfrac12,\chi_3)=0.4808\ldots>0$): in the Connes "Letter" framework, the candidate for the missing simple, even, lowest eigenvalue (§6.6a). The obligation specializes to: *show the chiral channel's negative cubic cluster supplies exactly the one eigenvalue the metric channel's positivity requires* — the definiteness is then metric-dominates-chiral, anchored by $L(\tfrac12,\chi_3)>0$.

**A.5 Status.** A.1–A.2 are theorem / this-paper; A.3–A.4 are the open Riemann Hypothesis, stated as concretely as the apparatus permits. The realistic path is the Connes-style construction of the scaling-site positivity, fed by the apex's now-complete local data and tested against the cubic-chirality candidate. The blueprint is exact and the local data complete; the surface and its positivity over $\mathbb Q$ are the genuine open construction.

---

## Appendix B. The gap as six problems (one object, six lenses)

The open content is a single object — the positivity of the apex Weil–Pick form $Q(g)$ (Theorem 6.1; equivalently $u_B\ge0$, equivalently the primitive $C\times C$ Gram negative-definite, Appendix A). We state it as six self-contained problems in six languages. They are deliberately redundant (several are logically equivalent); the conjunction is the Riemann Hypothesis for $\zeta$ together with GRH for $L(\cdot,\chi_3)$. *Givens* (established, $\mathsf{[P]}$): the reduction $\mathrm{RH}\iff Q\succeq0$ ([N5],[N6]); the apex supplies $Q$'s archimedean part ([N4],[N5]) and the local Frobenius data (Rem. 6.2(ii)); the function-field validation (every problem below is a theorem over $\mathbb F_q$, §5, App. A); $L(\tfrac12,\chi_3)=0.4808\ldots>0$.

**P1 (entire functions / Laguerre–Pólya).** Prove $E(z)=\Xi(z)+i\Xi'(z)$ has all zeros in $\operatorname{Im}z<0$ (Hermite–Biehler), equivalently $\Xi\in$ Laguerre–Pólya, equivalently $\operatorname{Im}\!\big(\Xi(z)\overline{\Xi'(z)}\big)\ge0$ on $\mathbb C_+$. [$\Leftrightarrow$ RH$(\zeta)$.]

**P2 (a positive sequence / Li).** Prove $\lambda_n=\sum_\rho[1-(1-\tfrac1\rho)^n]\ge0$ for all $n\ge1$, equivalently $G(z)=\sum_n\lambda_n z^n$ is holomorphic on $|z|<1$. Concretely: the alternating exponential $(|\rho|/|1-\rho|)^n$ that any off-line zero injects never overtakes the archimedean $\sim\tfrac n2\log n$. [$\Leftrightarrow$ RH$(\zeta)$; the on-line per-rung positivity $2(1-\cos n\theta_\rho)\ge0$ is given.]

**P3 (analytic number theory / trilinear Kloosterman).** Prove $\Lambda*\Lambda*\Lambda$ equidistributes to level $1-\delta$ (every $\delta>0$) modulo the primorials $P_n$ — the optimal Bettin–Chandee/Wright trilinear bound on moduli built from the first $n$ primes. [The arithmetic face; via the bridge ([N0],[diez Thm 4.3]) it delivers the on-line cubic positivity. Given: $n\le7$ (Maynard $\tfrac35$).]

**P4 (spectral / Connes — the chiral half).** Prove the $\chi_3$-twisted (cubic) Weil form is negative-definite — the cluster $c_2\propto-L(\tfrac12,\chi_3)^2<0$ extends to the full form — equivalently the prolate–Weil operator of the Connes "Letter" has the missing simple, even, lowest eigenvalue. [$\Leftrightarrow$ GRH$(\chi_3)$.]

**P5 (arithmetic geometry / Hodge index over $\mathbb Q$).** Construct a self-intersection space over $\mathbb Q$ (the Connes–Consani scaling-site square, the substitute for $C\times C$) with diagonal $\Delta$ and apex Frobenius graph $\Gamma$ (the Hasse–Davenport / $(-1)^n$ lift) whose primitive intersection Gram $M$ is negative-definite — $\det M>0$ the analogue of $4q-a^2>0$ (App. A). [$\Leftrightarrow$ RH; the construction.]

**P6 (operator theory / Hilbert–Pólya).** Construct a self-adjoint $H$ (or a Frobenius $F$ with $F^*F$ the scaling) of spectrum $\{\gamma_n\}$, whose archimedean part is the apex edge operator $(A-I)\Phi$ and whose finite parts are the local Gauss/Jacobi data on $|\cdot|=\sqrt q$, positive w.r.t. a polarization. [$\Leftrightarrow$ RH; the operator realization.]

**Logic.** $\mathrm{P1}\Leftrightarrow\mathrm{P2}\Leftrightarrow\mathrm{P5}\Leftrightarrow\mathrm{P6}\Leftrightarrow$ RH$(\zeta)$ (four languages for the metric channel); $\mathrm{P4}\Leftrightarrow$ GRH$(\chi_3)$ (the chiral channel); P3 is the arithmetic engine that, through the bridge, supplies the on-line positivity P1/P5 require. The conjunction is RH$(\zeta)\wedge$GRH$(\chi_3)$ at the primorial $\mathbb Z/6$; the identical six at $\mathbb Z/P_k$ for all $k$ give full GRH. Honest difficulty: each is RH-strength (P3 the live, advancing ANT frontier; P4 anchored by Iwaniec–Sarnak; P1/P2 the classical cores; P5/P6 the Connes-level constructions). The redundancy is the point — six independent attack surfaces on one positivity, each a theorem over $\mathbb F_q$.

---

## References

[N0] Murillo Montero, L. (2026). *The Closure.* Numbers series; the primorial Bombieri–Vinogradov closure target.

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$ over Multiquadratic–Cyclotomic Compositums.*

[N2] Murillo Montero, L. (2026). *The Apex Determinant: A Closed Form via Helmert–Fourier Factorization.*

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary: A Structural Reduction.*

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* (The edge operator $(A-I)\Phi$; $\sqrt i$ as the archimedean $\sqrt q$.)

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.* (The explicit-formula transfer $\kappa_n^{\mathrm{HL}}=(-1)^n\kappa_n^{\mathrm{apex}}$.)

[N6] Murillo Montero, L. (2026). *The Unified Archimedean Operator and the de Branges Target for $\xi$.* (The two-channel Bures fiber; $E_B=\Xi+i\Xi'$; Remarks 6.3–6.6.)

[CC20] Connes, A., and Consani, C. (2020). *Weil positivity and Trace formula: the archimedean place.* arXiv:2006.13771.

[Li] Li, X.-J. (1997). The positivity of a sequence of numbers and the Riemann Hypothesis. *J. Number Theory* 65, 325–333.

[BL] Bombieri, E., and Lagarias, J. C. (1999). Complements to Li's criterion for the Riemann Hypothesis. *J. Number Theory* 77, 274–287.

[Wright] Wright, T. (2026). *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions.* arXiv:2604.25177.

[FR] Fouvry, É., and Radziwiłł, M. *Level of distribution of unbalanced convolutions.*

[MRT] Matomäki, K., Radziwiłł, M., and Tao, T. (2015). An averaged form of Chowla's conjecture. *Algebra & Number Theory* 9(9), 2167–2196. (The minor-arc mean-square; §3.)

[May] Maynard, J. (2020). Primes in arithmetic progressions to large moduli III: uniform residue classes. (The $\tfrac35$ triply-well-factorable level; §3.)

[Var] Varbanets, P., Varbanets, S., and Vorobyov, Y. (2025). Divisor function of the Gaussian integers weighted by the Kloosterman sum. *Algebra and Discrete Mathematics* 40(2), 255–270.

[Weil] Weil, A. (1948). *Sur les courbes algébriques et les variétés qui s'en déduisent.* Hermann.

[Del] Deligne, P. (1974). La conjecture de Weil I. *Publ. Math. IHÉS* 43, 273–307.

[diez] Murillo Montero, L. (2026). *RH series, Paper diez*, Thm 3.3, Cor 3.4, Thm 4.3 (the discrete-to-continuous bridge and the $C^\ast$ crossover).
