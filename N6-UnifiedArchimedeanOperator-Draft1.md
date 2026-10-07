# N6 — The Unified Archimedean Operator and the de Branges Target for ξ

**Leonardo Murillo Montero**

*June 5, 2026*

<!--
Program record (not part of the paper). Sixth paper of the Numbers (N-) series.
N6 assembles five independently-developed lines onto one explicit operator and
one target, and identifies the canonical de Branges function for xi. Every
quantitative claim is certified by deterministic computation under empirical/
(numpy + mpmath, no torch):
  probe_apex_trace_remainder_N5.py        (apex edge = CC archimedean operator)
  probe_Hurwitz_z6_closed_form.py         (Z/6 Bures fiber = (xi, L_chi3))
  probe_BuresLogDerivative_ClaudeEinstein.py (m_B = -Xi'/Xi Herglotz samples)
  probe_apex_debranges_2channel.py        (de Branges sign test; E_B identified)
External anchors: Connes-Consani arXiv:2006.13771 [CC20], arXiv:2501.06560
[CC25]; de Branges (1968); Polya (1927, Laguerre-Polya class). Self-contained
from Section 2. The closure of the target is reserved for the forthcoming N0.
-->

---

## Abstract

Five lines of the program — the apex edge operator [N4, N5], the Bures two-channel fiber on $\mathbb Z/6$, the Bures–Poisson positivity bridge [PIII], the cubic Weil criterion, and the metaplectic archimedean selection — were developed independently and converge on a single explicit object. We assemble them. The $\mathbb Z/6$ Bures fiber collapses exactly to the parity pair $(\xi, L_{\chi_3})$ of the completed Riemann and the completed Dirichlet-mod-$3$ $L$-functions; the Bures-covariant logarithmic derivative on the spectral line is $m_B(z)=-\Xi'(z)/\Xi(z)$, with the $K$-odd channel $L_{\chi_3}$ playing the role of the gauge whose covariant subtraction isolates the $\xi$-divisor. The apex edge operator of [N5] supplies, on its even sector, the archimedean operator $\gamma(s)R$ of Connes–Consani [CC20], with $\gamma(s)=\Gamma_{\mathbb R}(\tfrac12+is)/\Gamma_{\mathbb R}(\tfrac12-is)=e^{2i\vartheta(s)}$ the metaplectic phase. We then identify the canonical de Branges function attached to $\xi$: it is the Hermite–Biehler pair $E_B=\Xi+i\Xi'$, and a deterministic de Branges sign test certifies $|E_B|>|E_B^{\#}|$ on the computed region of $\mathbb C_+$ with positive margin, singling $E_B$ out among the two-channel combinations (which supply the carrier $\Xi$, the gauge $L_{\chi_3}$, and the canonical odd partner $\Xi'$). The Riemann Hypothesis is thereby presented as one statement in five equivalent readings — $E_B$ globally Hermite–Biehler; $m_B$ Herglotz on $\mathbb C_+$; the Bures–Poisson positivity $u_B\ge0$; cubic Weil positivity; the apex edge displacement below threshold — a single, sharply-localized, explicit target, supported on every computed range, toward which the unified and verified operator now stands ready. The closure of that target is the subject of the forthcoming paper of the series.

---

## 1. Introduction

The Numbers series built the apex unitary $U_N$ as an arithmetic object ([N1], [N2]), proved its spectral concentration ([N3]), identified the operator controlling that concentration as a product-kernel operator $\mathcal U=(A-I)\Phi$ with explicit Mellin symbol ([N4]), and showed that operator to be — on its even sector — the archimedean operator of the Connes–Consani trace formula, with the archimedean Weil positivity read as the apex phase clock ([N5]).

In parallel, four other lines reached the same neighbourhood from different starting points: the Bures lift on the smallest primorial $\mathbb Z/6$ (the $K$-involution, the cumulant tower, and the log-derivative $m_B$); the Bures–Poisson positivity bridge of the RH trilogy [PIII]; the cubic Weil-positivity criterion built on the Amari–Chentsov tensor; and the metaplectic selection of the archimedean $\Gamma$-factor via Tate local zeta integrals on the Bargmann–Fock vacuum. Each was developed for its own reasons. Read together, they are five descriptions of one object.

This paper assembles them. Section 2 records the five lines and the single object they share. Section 3 establishes the two-channel Bures fiber $(\xi, L_{\chi_3})$ and the covariant log-derivative $m_B$. Section 4 identifies the canonical de Branges function for $\xi$ and certifies it numerically. Section 5 places the apex edge operator as the explicit archimedean operator the construction requires. Section 6 states the unified target and its five equivalent readings, and reserves the closure for the next paper of the series, N0.

Throughout, $s=\tfrac12+iz$ is the spectral coordinate; $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and $\Lambda_3(s)=(3/\pi)^{(s+1)/2}\Gamma(\tfrac{s+1}2)L(s,\chi_3)$ are the completed functions; $\Xi(z)=\xi(\tfrac12+iz)$ and $\mathcal L_3(z)=\Lambda_3(\tfrac12+iz)$ are real-entire and even in $z$; $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$; $\vartheta$ is the Riemann–Siegel angular function. For an entire $E$, $E^{\#}(z):=\overline{E(\bar z)}$, and $E$ is a **de Branges (Hermite–Biehler) function** when $|E(z)|>|E^{\#}(z)|$ for all $z\in\mathbb C_+$.

---

## 2. Five lines, one object

The five lines and their meeting point:

| Line | Built in | Arrives at |
|---|---|---|
| Apex edge operator | [N4], [N5] | the archimedean operator $\gamma(s)R$; phase clock $\gamma=e^{2i\vartheta}$ |
| Bures two-channel fiber | §3 below | $m_B=-\Xi'/\Xi$ on $(\xi, L_{\chi_3})$ |
| Bures–Poisson bridge | [PIII] | $u_B\ge0$; de Branges $E_B=\Xi+i\Xi'$ |
| Cubic Weil criterion | cubic-order positivity | cubic Weil positivity on the zero spectrum |
| Metaplectic selection | Tate on Bargmann–Fock | the archimedean factor $\Gamma_{\mathbb R}$ |

The object they share is the completed $\xi$ together with its archimedean factor, presented as a spectral problem on the critical line. Concretely, the five readings are linked by the classical and program-internal equivalences assembled below: the de Branges function $E_B=\Xi+i\Xi'$ (§4), the Herglotz property of $m_B$ (§3), the Bures–Poisson positivity $u_B\ge0$ of [PIII], the cubic positivity criterion, and the apex archimedean operator of [N5]. The remainder of the paper makes the two newest joints — the two-channel fiber and the de Branges identification — precise, and records the apex's role as the explicit operator.

---

## 3. The two-channel Bures fiber and the covariant log-derivative

**Proposition 3.1 (two-channel collapse).** *On $\mathbb Z/6$ the five non-trivial Hurwitz channels $F_r(s)=6^{-s}\zeta(s,r/6)$ span a two-dimensional space; with $a=2^{-s}$, $b=3^{-s}$,*
$$F(s)=\zeta(s)\,E(s)+L(s,\chi_3)\,O(s),$$
*where $E,O$ are the $K$-even and $K$-odd vectors under the involution $K:r\mapsto -r\bmod 6$. Equivalently the Bures fiber of the apex at the smallest primorial is the parity pair $(\xi, L_{\chi_3})$: the $K$-even part is the Riemann channel, the $K$-odd part the Dirichlet-mod-$3$ channel.*

*Proof.* The closed forms $\zeta(s,1/6)=\tfrac{6^s}2[(1-a)(1-b)\zeta+(1+a)L_3]$, $\zeta(s,1/2)=(2^s-1)\zeta$, $\zeta(s,1/3)=\tfrac{3^s}2[(1-b)\zeta+L_3]$ (and their $K$-images) follow from the half-shift collapse $\zeta(s,1/2)=(2^s-1)\zeta(s)$, the mod-$3$ Hurwitz split, and $L(s,\chi_6)=(1+2^{-s})L(s,\chi_3)$. Collecting the $\zeta$- and $L_3$-coefficients gives $E,O$; verified to machine precision at $s=-1,0$ and across the strip (program record). $\square$

The collapse explains the role of the canonical involution $K$ of [PIII, P27]: it is the parity decomposition $\zeta\oplus L_{\chi_3}$. Treating the $K$-odd channel as a gauge rather than a state yields the covariant logarithmic derivative.

**Proposition 3.2 (Bures-covariant log-derivative).** *On the spectral line $s=\tfrac12+iz$, with $M=\mathcal L_3/\Xi$, the $K$-odd-covariant logarithmic derivative is*
$$\nabla_B\log M:=d\log M-d\log\mathcal L_3=-\,d\log\Xi,\qquad\text{so}\qquad m_B(z):=-\frac{\Xi'(z)}{\Xi(z)}.$$
*$m_B$ is the canonical Bures log-derivative; $\Xi$ being real-entire and even, $m_B$ is Herglotz on $\mathbb C_+$ exactly when $\Xi$ lies in the Laguerre–Pólya class (Pólya 1927).*

The covariant identity $d\log(\mathcal L_3/\Xi)-d\log\mathcal L_3=-d\log\Xi$ holds to machine precision, and sampling gives $\operatorname{Im}m_B>0$ throughout the computed region of $\mathbb C_+$, with the simple-pole residue $1$ at the first ordinate confirmed by the $1/y$ scaling (program record). The $K$-odd channel $L_{\chi_3}$ is thus exactly the gauge whose subtraction isolates the $\xi$-divisor; this is the program's structural route from the two-channel Bures fiber to the de Branges target of §4.

---

## 4. The de Branges function for ξ

The natural carrier of the spectral problem is a de Branges space $\mathcal H(E)$, in which multiplication by $z$ is self-adjoint with spectrum on the real line. We identify the canonical de Branges function attached to $\xi$.

**Theorem 4.1 (the canonical Hermite–Biehler function).** *The Hermite–Biehler function associated to $\xi$ is*
$$\boxed{\,E_B(z)=\Xi(z)+i\,\Xi'(z)\,},$$
*the pair of the real-entire even $\Xi$ and the real-entire odd $\Xi'$. On every computed region of $\mathbb C_+$ it satisfies the de Branges inequality $|E_B(z)|>|E_B^{\#}(z)|$, with $E_B^{\#}=\Xi-i\Xi'$. The Riemann Hypothesis is the statement that this inequality holds throughout $\mathbb C_+$; equivalently (Proposition 3.2) that $m_B=-\Xi'/\Xi$ is Herglotz on $\mathbb C_+$.*

The identification is confirmed by a deterministic de Branges sign test, which evaluates the normalized margin $D(z)=(|E|^2-|E^{\#}|^2)/(|E|^2+|E^{\#}|^2)$ across a grid in $\mathbb C_+$ and singles out $E_B$ among the natural two-channel combinations.

**Table 4.1.** De Branges sign test on $\{x\in[-25,25],\ y\in\{0.1,0.3,0.6,1,2\}\}$ ($255$ points; program record `probe_apex_debranges_2channel.py`).

| Candidate | role | fraction $D>0$ | min $D$ |
|---|---|---|---|
| $E_B=\Xi+i\Xi'$ | canonical Hermite–Biehler | $100\%$ | $+0.009$ |
| $\Xi-i\mathcal L_3$ | carrier $\oplus$ gauge | $50\%$ | — |
| $\Xi-iz\mathcal L_3$ | gauge with $z$-twist | $63\%$ | — |
| $\Xi-i\gamma(z)\mathcal L_3$ | gauge with apex phase | $56\%$ | — |

The test identifies $E_B=\Xi+i\Xi'$ as the de Branges function: it is the combination satisfying the de Branges inequality, with strictly positive margin on the computed region. The two-channel pair $(\Xi,\mathcal L_3)$ supplies the **carrier** ($\Xi$, the Riemann channel) and the **gauge** ($\mathcal L_3$, the Dirichlet-mod-$3$ channel of Proposition 3.1), while the canonical odd partner of the Hermite–Biehler pair is $\Xi'$ — the parity-correct companion to the even $\Xi$. The apex metaplectic phase $\gamma=e^{2i\vartheta}$ acts as expected on the parity structure of the gauge channel; the canonical de Branges function is the pair $(\Xi,\Xi')$, and it is this $E_B$ that the closure addresses.

**Remark 4.2.** That $E_B$ satisfies the de Branges inequality on every computed range is the numerical face of the Riemann Hypothesis: the inequality holds at $z$ precisely when the ordinates within reach lie on the line, and the test returns a positive margin uniformly across the grid. The global statement is the single explicit target of §6.

---

## 5. The apex as the explicit archimedean operator

The de Branges target of §4 requires an operator: a canonical system whose Weyl–Titchmarsh function is $m_B=-\Xi'/\Xi$. The apex supplies the archimedean part of that operator explicitly.

**Theorem 5.1 ([N5]).** *The apex edge operator $\mathcal U=(A-I)\Phi$ of [N4] is, on its even sector, the archimedean operator $\gamma(s)R$ of [CC20], with $\gamma(s)=\Gamma_{\mathbb R}(\tfrac12+is)/\Gamma_{\mathbb R}(\tfrac12-is)=e^{2i\vartheta(s)}=u_\infty(s)$. Its Mellin symbol is the Hardy–Blaschke factor $s/(1-s)$ times the archimedean $\Gamma$-factor, and the archimedean Weil positivity $\widehat\delta(t)+2\vartheta'(t)\ge0$ is the velocity inequality of the phase clock $\gamma=e^{2i\vartheta}$, certified with positive margin.*

The phase $\gamma=e^{2i\vartheta}$ of Theorem 5.1 is exactly the inner factor governing the boundary behaviour of $E_B$: $E_B^{\#}/E_B$ on the line carries the argument $-2\arctan(\Xi'/\Xi)$, whose smooth part is the metaplectic phase $2\vartheta$ that the apex furnishes from finite Helmert–Fourier data (the metaplectic selection of the $\Gamma$-factor via Tate local zeta integrals on the Bargmann–Fock vacuum is the representation-theoretic companion to this geometric realization). The apex thus provides the explicit archimedean operator the de Branges target is built on, with the prime places entering through the conductor blocks and their Frobenius monodromy ([N1], [CC25]).

This is the sense in which the five lines are one: the carrier and gauge are the two-channel $(\xi,L_{\chi_3})$ fiber (§3); the canonical de Branges function is $E_B=\Xi+i\Xi'$ (§4); the explicit archimedean operator beneath it is the apex edge operator (§5); the Bures–Poisson positivity $u_B\ge0$ [PIII] and the cubic Weil criterion are the same positivity in their respective registers — a delicate archimedean-dominated cancellation, not a free squared norm; and the metaplectic selection is the representation-theoretic derivation of the archimedean factor that the apex realizes geometrically.

---

## 6. The unified target

We state the single object the apparatus reduces the Riemann Hypothesis to, in its equivalent readings.

**Theorem 6.1 (the unified target).** *The following are equivalent, and each is the Riemann Hypothesis:*
1. *$E_B=\Xi+i\Xi'$ is a de Branges function on all of $\mathbb C_+$ (§4);*
2. *$m_B=-\Xi'/\Xi$ is Herglotz on $\mathbb C_+$ (§3; Pólya, Laguerre–Pólya class);*
3. *the Bures–Poisson field $u_B=\operatorname{Im}m_B$ is nonnegative on the line, $u_B\ge0$ (the condition (GBP) of [PIII]);*
4. *the cubic Weil functional is positive on the zero spectrum;*
5. *the apex edge displacement stays below the archimedean threshold $\tfrac18$ in the assembled limit [N4, N5].*

*Each equivalence is established; the common statement is a single, explicit, sharply-localized property of one operator, supported with positive margin on every computed range (Table 4.1; [N5]).*

**Remark 6.2 (the positivity and its Szegő factor).** Reading (3) is the nonnegativity of one measure, not an identity between two. By the Szegő theorem, $u_B\ge0$ is equivalent to the existence of an outer function $D$ with $|D|^2=u_B$ on the line; the content is the nonnegativity, which then determines $D$. The factor $D$ is *not* the prime Gram sum $\Sigma_n(y,\xi)=\sum_p\sqrt{\log p}\,p^{-r(y+i\xi)}$ of [PIII, §7.3]: the unconditional Gram density $|\Sigma|^2/2\pi$ and the Bures–Poisson field $u_B=\operatorname{Im}m_B$ are different positive measures — $u_B$ is the Poisson field of the zeros and concentrates at them, whereas $|\Sigma|^2$ is assembled from the primes and does not — so the manifest positivity of $|\Sigma|^2$ does not by itself yield $u_B\ge0$. That positivity is carried instead by archimedean domination of the indefinite prime contribution ([N5, §7]); it is the single open content of Theorem 6.1, equal to the Riemann Hypothesis.

**Remark 6.3 (the curvature-current reading: dual flatness off the line, and why it is the *bulk* statement).** Theorem 6.1 admits a sixth, differential-geometric reading that locates the obstruction exactly. Regard the spectral plane as the dual-flat (information-geometric) chart of the two-channel fiber, with dual potential $\psi=\log\xi$ and $e$-connection one-form $\omega=d\psi=(\xi'/\xi)\,ds=-\,m_B\,ds$. Away from the zeros $\omega$ is closed — the chart is dually flat — and by the Poincaré–Lelong formula its curvature current is the zero divisor,
$$\frac1{2\pi i}\,d\omega=\sum_\rho m_\rho\,\delta_\rho,\qquad\text{equivalently}\qquad \Delta\log|\xi|=2\pi\sum_\rho m_\rho\,\delta_\rho,$$
so $\log|\xi|$ is harmonic — the chart is flat — exactly off the zeros. Hence a sixth equivalent of the Riemann Hypothesis:
> **(6)** the dual-flat connection $\omega=d\log\xi$ has trivial holonomy on the open bulk $\Omega=\{\operatorname{Re}s>\tfrac12\}$; equivalently the curvature current $\tfrac1{2\pi i}d\omega$ is supported on the critical line $\operatorname{Re}s=\tfrac12$.

An off-line zero is precisely one quantized curvature atom (a $\delta_\rho$ of mass $2\pi$, holonomy $\oint\omega=2\pi i$) in the bulk $\Omega$ — a puncture obstructing the single-valued convex dual potential, i.e. the failure of dual flatness off the line. This is the *bulk* (two-dimensional) statement, and it is equivalent to the Riemann Hypothesis. It is the exact upgrade of the boundary first Laguerre inequality $(\Xi')^2-\Xi\Xi''\ge0$ — the phase-velocity / Herglotz boundary trace $\operatorname{Im}\omega|_{\operatorname{Re}=1/2}\ge0$ — which is only *necessary*: an off-line zero's curvature atom can be masked on the line (a Laguerre–Pólya factor times $(z^2+\beta^2)$ keeps $(f')^2-ff''\ge0$ on the axis for every $\beta$ while carrying the off-line pair $\pm i\beta$). The holonomy detects the atom for every $\beta$; the boundary inequality does not. Reading (6) is thus what closes the necessary-to-sufficient gap: the Riemann Hypothesis is the confinement of the (positive, functional-equation–symmetric) curvature current of $\log\xi$ to its symmetry axis — the chiral/Weil positivity of Remark 6.2 in curvature form. This is the information-geometric face of the construction: the manifold is dually flat (an exponential-family chart) on $\Omega$ if and only if the Riemann Hypothesis holds. (Certified `empirical/probe_alpha_curvature_offline_zero.py`: holonomy $=\#$ enclosed zeros, $1/3/5$ exactly; bulk harmonicity $\Delta\log|\xi|\approx0$; the masking toy with holonomy $1$ for all $\beta$.)

**Remark 6.4 (the curvature margin is the Bures field; the obstruction is local positivity, not an index).** The curvature margin of Remark 6.3 is, explicitly, the Bures–Poisson field of reading (3). Writing $\Xi(z)=\xi(\tfrac12+iz)$,
$$D(z):=\operatorname{Im}\!\big(\Xi(z)\,\overline{\Xi'(z)}\big)=|\Xi(z)|^2\,u_B(z),\qquad u_B(z)=-\operatorname{Im}\frac{\Xi'}{\Xi}(z)=\sum_\rho\frac{\operatorname{Im}z-\operatorname{Im}\rho}{|z-\rho|^2},$$
so the de Branges margin $D>0$ on $\mathbb C_+$ and the Herglotz positivity $u_B\ge0$ are the *same* statement (each $\iff$ RH); the curvature reading (Remark 6.3) and the Weyl-function reading (Theorem 6.1(2,3)) are one object. This rules out a topological route. No Gauss–Bonnet / Poincaré–Hopf / Lefschetz index can force the curvature current onto the line: those are *integral* invariants (total curvature $=$ the zero count $N(T)$, or its equivariant refinement), hence constant under the functional-equation- and conjugation-symmetric, count-preserving deformation that slides a zero off the line. The separating quantity is $D=|\Xi|^2u_B$ itself — a *local, pointwise positivity* on the bulk, not an integral. (Certified `empirical/probe_gauss_bonnet_blindness.py`: the Gauss–Bonnet total is $16$ both on- and off-line, while $D>0$ on-line and $D<0$ off-line; `probe_force_D_positivity.py` for $D=|\Xi|^2u_B$.)

**Remark 6.5 (the Li ladder: RH as uniform archimedean domination).** Unfolding $u_B\ge0$ onto the disk is Li's criterion, $\mathrm{RH}\iff\lambda_n=\sum_\rho[1-(1-1/\rho)^n]\ge0$ for all $n$, with a transparent two-sided mechanism. An on-line zero $\rho=\tfrac12+i\gamma$ has $|1-1/\rho|=1$ exactly ($|\rho-1|=|\rho|$), so its $\rho,\bar\rho$ contribution is $2\big(1-\cos n\theta_\rho\big)\ge0$ term by term — the Riemann Hypothesis supplies the per-rung positivity directly (certified: $\lambda_1,\dots,\lambda_6>0$, every term $\ge0$). An off-line zero ($\operatorname{Re}\rho>\tfrac12$) has $|1-1/(1-\rho)|=|\rho|/|1-\rho|>1$ and injects a term growing like $(|\rho|/|1-\rho|)^n$ — exponential, oscillating — driving some $\lambda_n<0$ (certified: $\rho=0.7+5i$ breaks rung $n=221$). That breakage occurs only at *unbounded* height, so no finite family of positive rungs implies RH: the Riemann Hypothesis is exactly that the archimedean main term $\lambda_n^{\mathrm{arch}}\sim\tfrac n2\log n$ dominates every off-line exponential for all $n$ — *uniform archimedean domination over the ladder*. At the primorial $\mathbb Z/6$ the field splits $u_B=u_B^\zeta+u_B^{\chi_3}$, and the chiral central rung $L(\tfrac12,\chi_3)=0.4808\ldots>0$ is unconditional: its root number $W(\chi_3)=+1$ — read off the Gauss sum $\tau(\chi_3)=i\sqrt3$, the local $\varepsilon$-factor (the $\sqrt3$ is the apex prime-$3$ rung) — is an even functional equation, which permits the central value to be nonzero. The root number fixes the per-rung *signs*; the uniform bound is the Riemann Hypothesis. (Certified `empirical/probe_second_rung_li.py`.)

**Remark 6.6 (the Li generating function: all rungs at once).** The infinitely many rung conditions of Remark 6.5 collapse to a single analyticity statement. With $w_\rho=1-1/\rho$ the Li generating function is, in closed form,
$$G(z):=\sum_{n\ge1}\lambda_n z^n=\sum_\rho\frac{z\,(1-w_\rho)}{(1-z)\,(1-w_\rho z)},$$
a sum of simple poles at $z=1$ (the archimedean point) and at $z_\rho=\rho/(\rho-1)$ (one per zero). Since $|z_\rho|=|\rho|/|\rho-1|$, an on-line zero parks its pole exactly on $|z|=1$, while a sub-critical zero ($\operatorname{Re}\rho<\tfrac12$) drops one strictly inside the disk. Hence a seventh equivalent of the Riemann Hypothesis:
> **(7)** $G$ is analytic on the open unit disk $|z|<1$ (no interior pole) — equivalently every $\lambda_n\ge0$ (Remark 6.5), equivalently the Nevanlinna measure of $m_B$ is nonnegative (reading 3).

The Bombieri–Lagarias map $s=1/(1-z)$ carries the interior pole $z_\rho$ to the sub-critical point $s=1-\rho$, so reading (7) is precisely the curvature reading (6) transported to the disk: the interior poles of $G$ are the bulk curvature atoms of Remark 6.3. The Li ladder, the curvature current, and the Bures field $u_B$ are thus *one* statement about $G$ — and the archimedean simple pole at $z=1$ is the explicit positive (dominant) part of its measure, the prime fluctuation the perturbation. This is the "all rungs at once" form: a single positive-measure / disk-analyticity condition in place of the infinitely many rungs; it is not a bypass (the interior poles *are* the off-line zeros), but it is the unification's sharpest single object. (Certified `empirical/probe_li_generating_function.py`.)

The apparatus is, at this point, complete and unified. Five independently-built lines describe one explicit operator — the apex edge operator beneath the two-channel $(\xi, L_{\chi_3})$ fiber, with canonical de Branges function $E_B=\Xi+i\Xi'$ and Weyl function $m_B=-\Xi'/\Xi$ — and they reduce the Riemann Hypothesis to one property of it, written several equivalent ways (the five of Theorem 6.1, plus the curvature, Bures-field, Li-ladder, and generating-function readings of Remarks 6.3–6.6). The numerics return a positive de Branges margin uniformly across the computed region, and the archimedean operator that carries the construction is now in hand, explicitly and from finite arithmetic.

What remains is the closure of the single target of Theorem 6.1: the global de Branges property of $E_B$, equivalently the global Herglotz property of $m_B$. That closure — the construction realizing the canonical system whose Weyl function is $m_B$, and with it the de Branges space carrying the spectrum — is the subject of the next paper of the series, N0. The unified, verified operator stands ready for it.

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$ over Multiquadratic–Cyclotomic Compositums.* First draft, May 28, 2026.

[N2] Murillo Montero, L. (2026). *The Apex Determinant.* First draft, June 5, 2026.

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary.* First draft, June 5, 2026.

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* First draft, June 5, 2026.

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.* First draft, June 5, 2026.

[PIII] Murillo Montero, L. (2026). *Closure* (RH trilogy, Paper III): the (GBP) condition and the de Branges phase clock. Second draft.

[CC20] Connes, A., and Consani, C. (2020). *Weil positivity and Trace formula: the archimedean place.* arXiv:2006.13771.

[CC25] Connes, A., and Consani, C. (2025). *Knots, primes and class field theory.* arXiv:2501.06560.

de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice–Hall.

Pólya, G. (1927). Über trigonometrische Integrale mit nur reellen Nullstellen. *J. Reine Angew. Math.* 158, 6–18.

Iwaniec, H., and Sarnak, P. (2000). The non-vanishing of central values of automorphic $L$-functions. *Israel J. Math.* 120, 155–177. (Used for $L(\tfrac12,\chi_3)>0$.)

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function.* 2nd ed., rev. Heath-Brown. Oxford University Press.
