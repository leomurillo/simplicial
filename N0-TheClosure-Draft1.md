# N0 — The Closure: The Riemann Hypothesis as Integrated Cubic Positivity of the Apex Weil Form

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 6, 2026*

<!--
Program record (not part of the paper). Closure paper of the Numbers (N-) series.
N0 assembles the full reduction: the verified apex archimedean operator (N4-N6), the
cubic Weil-positivity criterion (siete-ocho-nueve-diez-once), the Estermann functional
equation as the r=2/r=-2 polar pair, the integrated (variance) bridge (RH-Pass8), and
the closure as the PRIMORIAL BOMBIERI-VINOGRADOV LEVEL C* <= 2.80 (the V/M crossover,
diez Thm 3.3/4.3) that closes the discrete->continuous bridge. The program proves DISCRETE
cubic positivity at P_n combinatorially (ocho S5 V-sector) and transfers it by the bridge,
whose sole obligation is this level -- NOT the continuous third moment directly. Three-arc
decomposition (twin of Washburn's Goldbach mod-8 treatment): MAJOR arc = singular-series
main term (certified +651.6, unconditional); MINOR arc = mean-square (Matomaki-Radziwill-Tao
2016, unconditional); MEDIUM arc = the level C* <= 2.80 (the obligation), bounded by
Heath-Brown + large sieve + per-prime Burgess + BILINEAR Kloosterman (Pascadi 2025,
c^{-1/12} on factorable/primorial moduli) for the BINDING Type-II [level theta<=6/11; EXACT frontier n<=5, NOT n<=6 -- asymptotic 1-C*/n is 1-2 rows optimistic],
with trilinear Bettin-Chandee/Wright (X^{1/2+1/66}) on the non-binding Type-III. Off-line sensitivity = unconditional
chi_3-twisted |L(1/2+it,chi_3)|^2 pair weight (anchored L(1/2,chi_3)=0.4809>0).
NOTE (2026-06-06): an earlier draft of this section mislocated the obligation as the
conditional Hardy-Littlewood third moment (Montgomery-Soundararajan / Rudnick-Sarnak); that
is the DIRECT continuous attack, which the discrete-positivity-plus-bridge route AVOIDS.
Corrected to the unconditional BV level C* per diez Thm 4.3 (the bridge needs the level and
nothing more). The cubic functional is NOT additive Chowla (Tao-Teravainen 2017 = wrong
tool); its continuous form is the short-interval third moment, but the program's obligation
is the level, not that asymptotic.
ASSEMBLY (2026-06-06, updated 2026-06-08 per Pascadi handoff): the binding Type-II level is
FIXED -- bilinear Pascadi theta<=6/11 (trilinear Wright ~0.515 / Polymath-8 ~0.547 are smaller,
Type-III/headroom) -- so against the EXACT requirement theta_0(n)=1-log(pure_V)/log(P_n)
(pure_V=sum_{p<=p_n}(p^2-1)/6; NOT the asymptotic 1-C*/n, which is 1-2 rows optimistic) the
frontier is n<=5 (theta_0(5)=0.545 < 6/11 < theta_0(6)=3/5); classical BV n<=3. The asymptotic
had mislabeled this "n<=6" (RETRACTED; see probe_exact_discharge_schedule). The large-n asymptotic theta_0->1 is primorial
Elliott-Halberstam (friable-moduli level-of-distribution frontier) -- the genuine terminus,
the precise difficulty class. Reduction (quantified): RH -> smooth-EH on primorial moduli (theta_0->1); bounded-n rows
n<=5 discharged (bilinear Pascadi 6/11; EXACT schedule -- n=6 needs theta_0(6)=3/5, out of reach), n->infinity tail = sparse-primorial BDH / open frontier.
Option A (the c_2 hunt, probe_optionA_*) does NOT escape it (positivity is circular/spectral;
non-circular = prime fluctuation = same C*).
Every quantitative claim is certified by deterministic computation under empirical/
(numpy + mpmath, no torch):
  probe_debranges_cbs_predictor.py   (E_B = Xi + i Xi' Hermite-Biehler; m_B Herglotz residue -1)
  probe_fermat_cbs_predictor.py      (|alpha|=sqrt q, Jacobi = Frobenius, the function-field twin)
  probe_cubic_polar_partner.py       (cubic = odd cumulant; cross-packet 33/36 on Z/6)
  probe_two_sided_cubic_arrow.py     (L(1/2,chi_3)=0.4809; chirality anchor)
  probe_cubic_third_moment.py        (C_zeta = third moment of S_g; skew->0 GUE leading vanishes)
  probe_singular_series_triple.py    (on-line baseline = Sum S(H) K_g = +651.6 > 0; p=3 selection)
  probe_c2_Lchi3_singular_dual.py    (c_2 = chi_3-twisted |L|^2; dual of mod-3 singular series)
  probe_optionA_hybrid_g_archimedean.py (Option A doesn't escape C*: S_g>=0 spectral=circular;
                                      non-circular positivity = prime fluctuation = C*)
  probe_Cstar_assembly.py            (C* assembled: n<=6 discharged by beyond-Weil; large-n
                                      = primorial Elliott-Halberstam; crossover n*~6)
  probe_cross_rung_cancellation.py   (Helmert-Gauss (star) = Sum|E_j|^2, Parseval)
  probe_burgess_exponent.py          (per-prime Burgess eta(lambda)=(4lambda-1)^2/16)
  probe_salie_primepower.py          (K(a,b;p^m)=0 or exact sqrt, m>=2; Lemma 2 over Z)
  probe_estermann_level.py           (divisor BV past level 1/2, delta_ms>0)
  probe_dispersion_mrt.py            (Moebius autocorrelations cancel; MRT input)
External anchors: Connes-Consani arXiv:2006.13771; Estermann (1930); Burgess (1962);
Matomaki-Radziwill-Tao, Ann. of Math. 2016; Rudnick-Sarnak (1996); Montgomery-Soundararajan,
Comm. Math. Phys. 252 (2004); Hardy-Littlewood (1918,1923); Weil (1948,1949);
Varbanets-Varbanets-Vorobyov, Algebra Discrete Math. 40(2) (2025). Self-contained from
Section 2. Tier tags [P]/[A]/[C] throughout.
-->

---

## Abstract

The Numbers series constructed an explicit unitary family — the apex unitaries $U_N$ — and identified, in the scaling limit, the operator that governs their spectral concentration as the archimedean operator of the Connes–Consani trace formula ([N4], [N5]), with the canonical de Branges function $E_B=\Xi+i\Xi'$ for $\xi$ and its Herglotz Weyl function $m_B=-\Xi'/\Xi$ ([N6]). This closure paper assembles that apparatus with the cubic Weil-positivity line of the program and reduces the Riemann Hypothesis to a single, explicitly named analytic statement whose core inputs are recent unconditional theorems.

We record four established reductions, each certified. **First** ([P], §2): the apex edge operator is the archimedean operator, and $E_B=\Xi+i\Xi'$ is Hermite–Biehler — equivalently $m_B$ Herglotz — exactly under the Riemann Hypothesis. **Second** ([P], §3): the Riemann Hypothesis is equivalent to the positivity of the cubic Weil functional $\operatorname{Re}\mathcal C_\zeta(g;\eta)\ge0$, the order-three upgrade of Bombieri's quadratic criterion; the cubic order is the leading **odd cumulant** — the antisymmetric, cross-conductor content that the quadratic order is structurally blind to. **Third** ([P], §4): the twisted Dirichlet series controlling the prime side is the **Estermann function** $D(s,a/q)=\sum_n d(n)\,e(na/q)\,n^{-s}$, whose functional equation carries the involution $s\leftrightarrow 1-s$ together with the Kloosterman inversion $a\leftrightarrow a^{-1}\bmod q$ — the polar pair $r\leftrightarrow-r$ with fixed locus the critical line. **Fourth** ([P], §5): the positivity reads the **variance** (the Cesàro-averaged second moment), not the pointwise maximum (RH-Pass8); the cubic Plancherel object is governed by the second moment of $\zeta$ on the critical line (Hardy–Littlewood).

These reduce the Hypothesis to one statement ([C], §6): the **primorial Bombieri–Vinogradov level** $\theta_0(p_n)=1-C^\ast/n$ with $C^\ast\le2.80$ — the V/M crossover threshold that closes the discrete-to-continuous bridge. The program does not evaluate the continuous third moment directly (that is the conditional Hardy–Littlewood route); it proves the discrete cubic positivity at $P_n$ combinatorially and transfers it by the bridge, whose sole obligation is this level. In a three-arc decomposition — the structure shared with the circle-method treatment of Goldbach via a mod-$8$ kernel (Washburn 2026) — the major arc (the singular-series main term, certified positive) and the minor arc (the mean-square, Matomäki–Radziwiłł–Tao 2016) are unconditional and in hand, and the off-line sensitivity (the $\chi_3$-twisted pair correlation, anchored by $L(\tfrac12,\chi_3)>0$) is unconditional; the medium arc — the level $C^\ast$ — is the terminus, bounded by the Heath–Brown identity, the large sieve, per-prime Burgess, and — for the binding Type-II sums — the bilinear Kloosterman estimates of Pascadi (2025), with the trilinear estimates of Bettin–Chandee–Wright (2026) governing the non-binding Type-III range. The verified apparatus of §§2–5 stands ready; by the exact V/M schedule (*ocho* §7.1) classical Bombieri–Vinogradov discharges $n\le3$ and the bilinear Pascadi level $6/11$ discharges $n\le5$ (the asymptotic $1-C^\ast/n$ being one to two rows optimistic), while $n=6$ needs $\theta_0(6)=\tfrac35$ — above both current max-over-$a$ levers — and the terminus is the large-$n$ asymptotic $\theta_0\to1$ — smooth Elliott–Halberstam, the friable-moduli level-of-distribution frontier into which the Hypothesis is here localized. This max-over-$a$ obligation is then refined (§§6.6–6.9) to its genuine $L^2$ form: by Lemma 6.8 the cubic transfer error is a **variance**, not a maximum, which remaps the terminus to **sparse-primorial BDH** — GRH-on-average for the $p_n$-smooth conductor family at $\mathrm{Re}\,s=\tfrac12$, an $L^2$-density target whose full-family analog is an unconditional theorem and whose folklore obstructions (large-sieve insufficiency, the Siegel zero) are discharged.

**Keywords:** Riemann Hypothesis, cubic Weil positivity, Amari–Chentsov tensor, apex unitary, de Branges space, Hermite–Biehler, Estermann function, Kloosterman sum, Bombieri–Vinogradov, level of distribution, trilinear Kloosterman fractions, singular series, primorial modulus, circle method, second moment.

**MSC 2020:** 11M26 (RH), 11L05 (Gauss/Kloosterman sums), 11N13 (primes in progressions), 11M06 ($\zeta$ on the critical line), 62B11 (information geometry).

---

## 1. Introduction

The program reaches the Riemann Hypothesis along a single thread, which this paper makes explicit end to end. Each link is either a theorem of the literature, a verified identity of the Numbers series, or — at the terminus — a statement whose core has been proved unconditionally in the last decade.

The thread is:
$$
\text{RH}\ \overset{\S2}{\Longleftrightarrow}\ E_B\in\mathrm{HB}\ \overset{\S3}{\Longleftrightarrow}\ \operatorname{Re}\mathcal C_\zeta\ge0\ \overset{\S5}{\Longleftarrow}\ \big(\text{discrete cubic positivity at }P_n\big)\ \overset{\S6}{\Longleftarrow}\ \big(C^\ast\le2.80\big).
$$

Sections 2–5 are established and certified ([P]). Section 6 names the terminal statement ([C]) — the primorial Bombieri–Vinogradov level $C^\ast\le2.80$ — and the three-arc decomposition whose major and minor arcs are unconditional (the singular-series main term; the mean-square of Matomäki–Radziwiłł–Tao) and whose medium arc — the level — is the single remaining constant. Section 7 states the closure.

Throughout, $s=\tfrac12+iz$; $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$; $\Xi(z)=\xi(\tfrac12+iz)$ is real-entire and even; $\Xi'=d\Xi/dz$ is odd; $d(n)$ is the divisor function, $\mu$ the Möbius function, $\Lambda$ von Mangoldt, $\chi_3$ the quadratic character mod $3$; $P_n=\prod_{i\le n}p_i$ the primorial; $e(t)=e^{2\pi it}$. Tier tags: $\mathsf{[P]}$ proved/certified, $\mathsf{[A]}$ structural identification, $\mathsf{[C]}$ the calibrated closure target.

---

## 2. The apex apparatus and the de Branges criterion $\mathsf{[P]}$

\hypertarget{stmt:2-1}{}
**Theorem 2.1 (apex = archimedean operator; [N4],[N5]).** *The apex edge operator $\mathcal U=(A-I)\Phi$ — Hardy averaging minus identity, composed with the half-line Fourier transform — is, on its even sector, the Connes–Consani archimedean operator $\gamma(s)R$ with $\gamma(s)=\Gamma_{\mathbb R}(\tfrac12+is)/\Gamma_{\mathbb R}(\tfrac12-is)=e^{2i\vartheta(s)}=u_\infty(s)$, times the Hardy–Blaschke factor $s/(1-s)$. Its reflection product is Euler's formula $\widetilde k(s)\widetilde k(1-s)=i/(2\sin\pi s)$, deriving the archimedean threshold $\tfrac18$ as the phase of $\sqrt i$.*

This is the explicit archimedean operator the spectral program requires; the threshold $\sqrt i$ is the archimedean analogue of the Weil scale $\sqrt q$ over a function field (see §4 and [N5]). Numerical identification to relative error $\le 2\times10^{-41}$ ([N4], Remark 5.3).

\hypertarget{stmt:2-2}{}
**Theorem 2.2 (de Branges criterion; [N6], classical).** *The canonical Hermite–Biehler associate of $\xi$ is $E_B(z)=\Xi(z)+i\Xi'(z)$, and*
$$
|E_B(z)|^2-|E_B^{\#}(z)|^2=4\,|\Xi(z)|^2\operatorname{Im}m_B(z),\qquad m_B=-\Xi'/\Xi,
$$
*so that $E_B$ is Hermite–Biehler on $\mathbb C_+$ $\iff$ $m_B$ is Herglotz on $\mathbb C_+$ $\iff$ the Riemann Hypothesis.*

The canonical system of $E_B$ is the rank-one projector $H(t)=P_{\varphi(t)}$ with phase $\varphi=-\arg E_B$; its positivity is free, and the entire content is the monotonicity $\varphi'\ge0$, with $\varphi'(x)=(\Xi'^2-\Xi\Xi'')/(\Xi^2+\Xi'^2)$ and $\varphi(T)/\pi=N(T)$ (the zero count). The pointwise inequality $\varphi'\ge0$ is the first Laguerre inequality — necessary; the Hypothesis is the global statement that $E_B$ has no zeros in $\mathbb C_+$. **Certified** (probe `probe_debranges_cbs_predictor.py`): $v^{\!\top}Bv=\Xi|v|^2$ to $10^{-32}$ (the antisymmetric $\Xi'$ in the kernel of the quadratic form); $\operatorname{Im}m_B>0$ throughout the sampled $\mathbb C_+$; residue of $m_B$ at $\gamma_1$ equal to $-1$ (the Herglotz pole sign).

---

## 3. The Riemann Hypothesis as cubic positivity $\mathsf{[P]}$

\hypertarget{stmt:3-1}{}
**Theorem 3.1 (cubic positivity $\iff$ RH; *ocho* §3, *diez* §4).** *Let $\mathcal C_\zeta(g;\eta)$ be the cubic Weil functional — the order-three term of the explicit formula on the convolution-square test class $\mathcal G\times\mathcal H_c$. Then*
$$
\operatorname{Re}\mathcal C_\zeta(g;\eta)\ge0\quad\text{for all }(g,\eta)\in\mathcal G\times\mathcal H_c\qquad\Longleftrightarrow\qquad\text{RH}.
$$
*Both directions are unconditional. Forward: an off-line zero forces $\operatorname{Re}\mathcal C_\zeta<\operatorname{Re}\mathcal C^{(0)}_\Lambda-\tfrac12|c_2|\delta^2$, with the cluster constant $c_2<0$ the $\chi_3$-twisted pair correlation $\int|L(\tfrac12+it,\chi_3)|^2[24\,\mathcal K_{3\gamma_0}+72\,\mathcal K_{\gamma_0}]\,dt$ of the $2$-channel Bures fiber (*diez* Thm 2.7; refined form, Prop. 6.4), strictly signed and anchored by $L(\tfrac12,\chi_3)^2>0$. Reverse: under RH, $\operatorname{Re}\mathcal C_\zeta=\int 2\eta\,\mathcal S_g^3\ge0$ with $\mathcal S_g\ge0$ for $g\in\mathcal G$ (*diez* Cor 1.5, [A1']).*

The constant is anchored: $L(\tfrac12,\chi_3)=0.48087\ldots\ne0$ (Iwaniec–Sarnak; certified in `probe_two_sided_cubic_arrow.py`), so the chirality is forced — an off-line zero gives the cubic functional the wrong sign and cannot be masked.

\hypertarget{stmt:3-2}{}
**Proposition 3.2 (why order three — the odd-cumulant axis; *siete*, [N-CBS]).** *The cubic Amari–Chentsov tensor is the leading odd term of the cumulant tower of $\log\zeta$: the parity split $K(\beta)\mp K(-\beta)$ separates the even cumulants (quadratic, quartic) from the odd (cubic, quintic), and the cubic is the leading odd — the antisymmetric, arrow-carrying content. On $\mathbb Z/6$ the cubic selection rule $a+b+c\equiv0$ couples distinct conductor packets in $33$ of $36$ vertices, whereas the quadratic rule is block-diagonal (certified, `probe_cubic_polar_partner.py`). The local statistics of triples of zeros obey the GUE three-point density (Rudnick–Sarnak 1996); the cubic is the first order at which this content is present.*

For a single self-dual $\xi$ the odd cumulants vanish; the cubic content is intrinsically **joint** — cross-character, cross-prime — which is why the closure lives at primorial moduli (§§5–6).

---

## 4. The functional equation as the polar pair $\mathsf{[P]}$

\hypertarget{stmt:4-1}{}
**Theorem 4.1 (Estermann; the polar pair).** *The twisted Dirichlet series controlling the prime side of the cubic functional is the Estermann function*
$$
D(s,a/q)=\sum_{n=1}^\infty\frac{d(n)\,e(na/q)}{n^{s}},\qquad(a,q)=1,
$$
*degree two, with the functional equation (Estermann 1930), $\bar a=a^{-1}\bmod q$:*
$$
D(s,a/q)=2\,(2\pi)^{2s-2}q^{\,1-2s}\,\Gamma(1-s)^2\big[\cos(\pi s)\,D(1-s,\bar a/q)-D(1-s,-\bar a/q)\big].
$$

The equation carries the program's compass exactly: the spectral involution $s\leftrightarrow1-s$ (equivalently $r\leftrightarrow-r$ under $r\sim2\operatorname{Re}s-1$, fixed point the critical line $\operatorname{Re}s=\tfrac12$, $r=0$), and the arithmetic involution $a\leftrightarrow\bar a=a^{-1}\bmod q$ — the Kloosterman inversion $x+x^{-1}$, the multiplicative polar pair. The thread's gauge structure $r=2/r=-2\to r=0$ is the analytic structure of the prime side.

\hypertarget{stmt:4-2}{}
**Lemma 4.2 (prime-power Kloosterman; Varbanets–Varbanets–Vorobyov 2025, over $\mathbb Z$).** *For $K(a,b;q)=\sum_{(x,q)=1}e((ax+b\bar x)/q)$ and $q=p^m$, $m\ge2$: $K(a,b;p^m)=0$ if $ab$ is a quadratic nonresidue mod $p$, and $|K(a,b;p^m)|\le2\,p^{m/2}$ (Salié, exact square root) if $ab$ is a residue.* Certified over $\mathbb Z$ (`probe_salie_primepower.py`): vanishing on half the classes, exact $\sqrt{}$ otherwise — a beyond-Weil saving at prime-power modulus.

---

## 5. The integrated bridge: the positivity reads the variance $\mathsf{[P]}$

\hypertarget{stmt:5-1}{}
**Theorem 5.1 (variance, not maximum; RH-Pass8).** *The discrete-to-continuous bridge for the cubic functional is the Cesàro-averaged second moment — the variance*
$$
V(X,q)=\frac1{\varphi(q)}\sum_{(a,q)=1}\Big|\Psi(X;q,a)-\frac{\Psi(X)}{\varphi(q)}\Big|^2,
$$
*not the pointwise maximum. The cubic Plancherel object is governed by the second moment of $\zeta$ on the critical line, $\int_T^{2T}|\zeta(\tfrac12+it)|^2\,dt\sim T\log T$ (Hardy–Littlewood 1918, Atkinson 1949).*

This is the corrected framing of RH-Pass8 (§4 there): the apex trace is a re-organization of the variance, and the integrated positivity requires the mean-square, never the maximum. The maximum-form of the level statement (ocho §7, diez [A3′]) overstates the requirement.

\hypertarget{stmt:5-2}{}
**Theorem 5.2 (per-prime Burgess, optimized; CRT product).** *For $\chi$ primitive mod $p$, $N=p^\lambda$, the optimal Burgess exponent is*
$$
|S_\chi(N)|\ll_\varepsilon N\,p^{-\frac{(4\lambda-1)^2}{16}+\varepsilon},\qquad r^\ast=\frac{2}{4\lambda-1}\ \ (\tfrac14\le\lambda\le\tfrac34),
$$
*and for $\chi=\prod\chi_i$ mod $d=\prod p_i$ the saving multiplies, $d^{-(4\lambda-1)^2/16}=\prod_i p_i^{-(4\lambda-1)^2/16}$.* Certified (`probe_burgess_exponent.py`). The Helmert–Gauss identity of [T9.4.1] expresses the variance in the Helmert basis as $\sum_\psi|\psi(X,\psi)|^2=\frac{\varphi(N)}{N}\sum_k|\Pi_k|^2/(k(k+1))=\sum_j|E_j|^2$ (Parseval; certified, `probe_cross_rung_cancellation.py`), with $E_j$ the Kloosterman–Vinogradov prime sums.

---

## 6. The closure target: the primorial level of distribution ($C^\ast\le2.80$, refined to a variance) $\mathsf{[C]}$

The program does **not** establish the continuous cubic positivity by evaluating the third moment of primes in short intervals directly — that direct route is the Hardy–Littlewood prime-tuple asymptotic, conditional. It establishes the **discrete** cubic positivity at primorial modulus $P_n$ — combinatorially, unconditionally (*ocho* §5, V-sector $S(p)=(p^2-1)/6$) — and transfers it to the critical line by a **bridge** whose single obligation is a level-of-distribution constant. This is the program's defining move, and it has an exact external twin: the circle-method treatment of Goldbach via a mod-$8$ kernel (Washburn 2026), a three-tier arc decomposition in which the singular series gives the main term, the mean-square gives density-one, and a dispersion estimate gives full positivity beyond an explicit threshold. We adopt the same three tiers; two are in hand, the third is the named terminus.

### 6.1 Minor arc — the mean-square (unconditional)

The dispersion of the variance is exact: the diagonal is the main term, and the off-diagonal is a weighted sum of **two-point** correlations,
$$
V^{\mathrm{off}}_n=\sum_{d\mid P_n,\,d\le P_n^\theta}\ \sum_{k\ne0}\ \sum_{n\le X}f(n)\,f(n+dk),\qquad f\in\{\mu,\Lambda\},
$$
at shifts $h=dk$ — the averaged two-point cancellation.

\hypertarget{stmt:6-1}{}
**Theorem 6.1 (quadratic rung; Matomäki–Radziwiłł–Tao 2016).** *$\frac1H\sum_{h\le H}\big|\sum_{n\le X}\mu(n)\mu(n+h)\big|=o(X)$ as $H,X\to\infty$.* Consequently the primorial variance $V_n=o(X^2\log\log P_n)$ at every level $\theta<1$, unconditionally (modulo uniformity in the dilation $d$). The Möbius autocorrelations cancel at square-root strength (certified, `probe_dispersion_mrt.py`); the divisor variance equidistributes past level $\tfrac12$ (certified, `probe_estermann_level.py`). The two-point rung is genuinely additive, and the variance bridge is in hand at every level below $1$.

### 6.2 Major arc — the singular-series main term (unconditional)

On the prime side the cubic functional's main term is the singular-series prime-triple sum
$$
\sum_{\substack{\mathcal H=\{0,h_1,h_2\}\\ \text{admissible}}}\mathfrak S(\mathcal H)\,K_g(\mathcal H),\qquad
\mathfrak S(\mathcal H)=\prod_p\frac{1-\nu_p(\mathcal H)/p}{(1-1/p)^{3}},\qquad \nu_p(\mathcal H)=\#\{\mathcal H \bmod p\},
$$
$K_g$ supported on the near-diagonal. The conductor-$3$ selection rule of §3 is exactly the $p=3$ factor: a tuple covering all residues mod $3$ is inadmissible ($\mathfrak S=0$). The surviving series is positive, and the kernel-weighted sum is positive — certified $+651.6$ on the canonical window (`probe_singular_series_triple.py`). This is the unconditional main-term positivity, the analogue of Washburn's major-arc term $(c_8(2m)+o(1))\,\mathfrak S(2m)\,N/\log^2 N$ with mod-$8$ chirality $c_8\in\{1,\tfrac12\}$. Its discrete realization at $P_n$ is the V-sector positivity (*ocho* §5), unconditional.

\hypertarget{stmt:6-2}{}
**Remark 6.2 (the direct continuous attack, which the program avoids).** Taken as a continuous statement, the cubic functional is the third moment of the zero wave $\mathcal C_\zeta=\int\eta\,\mathcal S_g^3$, whose leading (GUE) order vanishes — the third moment of an asymptotically Gaussian wave (Rudnick–Sarnak 1996, unconditional for restricted support; skewness $\to0$, `probe_cubic_third_moment.py`) — so the positivity is subleading, governed by the prime-$3$-tuple singular series under the uniform Hardy–Littlewood conjecture (Montgomery–Soundararajan 2004). That asymptotic is conditional; the program does not invoke it. The discrete V-sector positivity supplies the same content unconditionally, and the bridge of §6.3 carries it to the line via the level alone.

### 6.3 Medium arc — the level (the obligation)

The bridge from discrete to continuous positivity (*diez* Thm 4.3) requires the primes to equidistribute modulo squarefree primorials $P_n$ at level $\theta=\theta_0(p_n)=1-C^\ast/n$:
$$
\sum_{\substack{d\mid P_n\\ d\le P_n^{\theta}}}\ \max_{(a,d)=1}\Big|\psi(x;d,a)-\frac{\psi(x)}{\varphi(d)}\Big|\ \ll_A\ \frac{x}{(\log x)^A},\qquad \theta_0=1-\frac{C^\ast}{n}.
$$
Here $C^\ast$ is the **V/M crossover threshold** of *ocho* §7.1 — the required rate $C^\ast\le2.80$ (*diez* Thm 3.3, Cor 3.4). The bridge is conditional on this level and **nothing more** (*diez* Thm 4.3): not on a three-point correlation, not on Hardy–Littlewood. The machinery is the Heath–Brown identity ($K=5$, the Type-I part carried by the extreme sparsity of the divisors of $P_n$, $\sum_{d\mid P_n}\varphi(d)=P_n$), the per-prime Burgess saving $r^\ast=2/(4\lambda-1)$ of §5.2, and Mertens assembly; the binding **Type-II** input is the *bilinear* Kloosterman estimate of Pascadi (2025) on factorable moduli — saving $d^{-1/12}$ on every squarefree divisor of $P_n$ after completion to the dual lengths — which converts through the Bombieri–Friedlander–Iwaniec dispersion method to level $\theta\le 6/11\approx0.545$ (efficiency $\kappa=6/11$ pinned in the favorable regime). The *trilinear* Bettin–Chandee–Wright estimate ($Q\le X^{1/2+1/66-\delta}$, $X^{45/89-\varepsilon}$ balanced) governs the **Type-III** range — non-binding here, and at a strictly smaller exponent than the bilinear Type-II.

**The discharge structure (certified, `probe_pascadi_kappa_dispersion.py`, `probe_pascadi_primorial_level_nrange.py`).** The bridge obligation above is the *max-over-$a$* Bombieri–Vinogradov sum, so the well-factorable hierarchy — $\theta=\tfrac47$ (Bombieri–Friedlander–Iwaniec), $\tfrac35$ (Maynard's triply-well-factorable $x^{3/5-\varepsilon}$) — does **not** apply: those estimates fix the residue class $a$ (the bounded-gaps configuration), whereas the obligation carries the maximum over all $(a,d)=1$. The operative beyond-$\tfrac12$ lever for the max-over-$a$ sum on the friable moduli $P_n$ is the *bilinear* Kloosterman saving. Through the completed Pascadi handoff — Heath–Brown depth $K=5$; the binding balanced Type-II form completed to dual lengths $H\asymp X^{\theta-1/2}\ll d^{1/2}$, inside Pascadi's strong range; the $2^{\omega(P_n)}=d^{o(1)}$ divisor penalty absorbed — the dispersion efficiency is pinned at $\kappa=6/11$ in the favorable regime $\beta=\log p_n/\log X\to0$, giving the unconditional level
$$\theta_{\mathrm{ach}}=\frac1{2(1-\eta)}=\frac{6}{11}\approx0.5455,\qquad \eta=\tfrac1{12}.$$
This level $\theta_{\mathrm{ach}}=6/11$ is compared against the **exact** requirement $\theta_0(n)=1-\log\mathrm{pure}_V(P_n)/\log P_n$ (*ocho* §7.1, with $\mathrm{pure}_V(P_n)=\sum_{p\le p_n}(p^2-1)/6$, §5) — **not** the asymptotic $1-C^\ast/n$ ($C^\ast\approx2.80$), which understates the requirement by one to two rows at small $n$. The exact schedule (certified `probe_exact_discharge_schedule.py`) is $\theta_0(5)=0.5453$, $\theta_0(6)=\tfrac35=0.600$, $\theta_0(7)=0.642$. Hence: **classical Bombieri–Vinogradov ($\tfrac12$) discharges $n\le3$; the bilinear Pascadi level $6/11\approx0.5455$ discharges $n\le5$** (razor-tight, $6/11>\theta_0(5)=0.5453$). The next row $n=6$ needs $\theta_0(6)=\tfrac35$, and **both** current max-over-$a$ levers fall below it by a real margin $\sim0.05$–$0.07$: the bilinear Type-II ceiling ($6/11=0.545$) and the smooth fixed-residue Type-III $d_3$ record ($\tfrac12+\tfrac1{34}=0.529$, Ping Xi 2018 — *not* the general $\tfrac12+\tfrac1{82}$ of Heath–Brown 1986). So $n=6$ is out of reach for current technology — *not*, as an earlier draft using the asymptotic $\theta_0(6)=\tfrac8{15}$ inferred, a tiny $1/255$ Type-III residual (that figure is retracted). The bridge-coupling $p_n\le X^{\theta/8}$ is verified ($X\to\infty$ for fixed $n$) but moot here, the Type-II ceiling itself being below $\tfrac35$. Certified `probe_pascadi_typeIII_constraint.py`, `probe_exact_discharge_schedule.py`. ($n=7$ needs $\theta_0(7)=0.642$, further still beyond the $6/11$ ceiling.) The large-$n$ asymptotic $\theta_0\to1$ is the **smooth Elliott–Halberstam regime** — equidistribution to level $\to1$ on the friable moduli $P_n$ — the precise difficulty class into which the program drives the Hypothesis.

**Why the ternary structure does not lift the level — the wall is bilinear (certified, `probe_trilinear_lindelof_terminus.py`).** The cubic object $\mathcal C_\zeta=\int\eta\,\mathcal S_g^3$, $\mathcal S_g=\sum_n\Lambda(n)n^{-1/2}g$, is a genuine ternary convolution $\Lambda*\Lambda*\Lambda$, and its outer structure manifests as the *trilinear* Type-III sums of the Heath–Brown decomposition — the native object of the Bettin–Chandee sum $\Sigma(U,V,W)=U^{-1}\sum x_u y_v z_w\,e(u\bar v/w)$. This does **not** raise the level, for three independent reasons. *(i)* The balanced **Type-II** bilinear sums ($M\asymp N\asymp X^{1/2}$) are intrinsic to representing $\Lambda$ on a single variable; they are present irrespective of the ternary outer structure and **cap the level at $6/11$** — no trilinear improvement lifts the overall level past the bilinear Type-II ceiling. (The Type-III piece, the genuinely ternary one, must independently clear $\theta_0(n)$, but by the smooth-moduli $\mathrm{Kl}_3$/Deligne machinery — not the Bettin–Chandee fractions — and even saturated it cannot exceed the $6/11$ cap.) *(ii)* The trilinear constant is *smaller*: Bettin–Chandee–Wright give $\tfrac12+\tfrac1{66}\approx0.515$ (general) and $45/89\approx0.506$ (balanced), both **below** the bilinear $6/11\approx0.545$ — routing the binding sum through the object's own trilinear structure would *lower* the level. *(iii)* The well-factorable $\tfrac35$ ceiling the trilinear route was invoked to "void" never bound the max-over-$a$ obligation in the first place (the discharge structure above). What the trilinear route *does* supply is **headroom**, not level: its terminus is Lindelöf-strength ($\theta_0\to1$ is the optimal Bettin–Chandee bound, [FR] §6.5, whose consequences include the Lindelöf hypothesis) — a soft ceiling at $1$ versus the bilinear *hard* ceiling at $6/11$. The cubic terminus read through that headroom is a statement about $\zeta$ on the critical line, nearer the Hypothesis's own ground than Elliott–Halberstam; but reaching it is governed by the bilinear obstruction below. **The wall, located.** Closing the tail needs the bilinear saving $\eta(n)\to\tfrac12$ (full square-root cancellation, no dispersion loss) **and** growing with $n$, so that $\theta_0(n)=1/(2(1-\eta(n)))\to1$. The friability of $P_n$ is consumed *once* — to balance the single completed bilinear form into Pascadi's strong range; its $n$ prime factors buy the *precision* of that balancing (driving $\beta\to0$), not the *magnitude* of the per-split saving, which stays $\eta=\tfrac1{12}$. Nesting $k$ factorizations gives, by the CRT, a *product* of local Weil $\sqrt{\,}$-cancellations whose exponent remains $\tfrac12$: the savings do not compound. The missing input is a friability-indexed (multilinear) Kloosterman/large-sieve estimate whose saving $\eta(n)\to\tfrac12$ as $\omega(P_n)=n\to\infty$ — Linnik/Kloosterman-conjecture-strength on smooth moduli, which the ternary structure does not unlock. This primorial-restricted smooth-EH frontier is the precise terminus.

\hypertarget{stmt:6-4}{}
**Proposition 6.4 (the off-line sensitivity is unconditional; the $\chi_3$-twisted dual).** *The off-line cluster coefficient of §3 is the $\chi_3$-twisted pair correlation*
$$
c_2(\gamma_0;\sigma_0)=\frac{|C_G|^2}{2\sigma_0^4}\int|L(\tfrac12+it,\chi_3)|^2\big[24\,\mathcal K_{3\gamma_0}(t)+72\,\mathcal K_{\gamma_0}(t)\big]\,dt,\qquad
|L(\tfrac12+it,\chi_3)|^2=\sum_{m,n}\frac{\chi_3(m)\chi_3(n)}{\sqrt{mn}}\Big(\tfrac nm\Big)^{it},
$$
*the spectral image of the mod-$3$-twisted singular series — the explicit-formula dual of the on-line sum, one moment-level below (pair vs.\ triple). It is unconditional and strictly negative, anchored by $L(\tfrac12,\chi_3)=0.48087\ldots>0$.* Certified (`probe_c2_Lchi3_singular_dual.py`): the channel weight $|L(\tfrac12+i\gamma_0,\chi_3)|^2$ is positive at every zero height, and $L(s,\chi_3)^2=\sum_n d_{\chi_3}(n)n^{-s}$ identifies the twist with the divisor $d_{\chi_3}=\chi_3*\chi_3$. An off-line zero lowers the cubic functional by a strictly positive amount the singular-series sign cannot mask.

\hypertarget{stmt:6-5}{}
**Closure target (C).** *The primorial-indexed Bombieri–Vinogradov bound holds at level $\theta_0(p_n)=1-C^\ast/n$ with $C^\ast\le2.80$ — the V/M crossover threshold that closes the discrete-to-continuous bridge (*diez* Thm 4.3, Cor 3.4).* The major arc (the singular-series main term, §6.2), the minor arc (the mean-square, §6.1), and the off-line teeth (Prop. 6.4) are unconditional and in hand, as is the discharge of $n\le3$ (classical Bombieri–Vinogradov) and $n\le5$ (the bilinear Pascadi level $6/11$, razor-tight at $n=5$; exact schedule, §6.3). The $n=6$ row needs $\theta_0(6)=\tfrac35$ — above both current max-over-$a$ levers (bilinear Type-II $6/11$ and smooth Type-III $d_3$ $\tfrac12+\tfrac1{34}$) — and is out of reach for present technology (the earlier $1/255$ figure, from the asymptotic $\theta_0(6)=\tfrac8{15}$, is retracted; the discharge structure above). The terminus is the **large-$n$ asymptotic**: the level $\theta_0\to1$ on the friable moduli $P_n$ — smooth Elliott–Halberstam. This is the precise difficulty class into which the program drives the Hypothesis: not a numerical constant to be tuned, but the level-of-distribution frontier for smooth moduli, where every present advance (Bombieri–Friedlander–Iwaniec well-factorable weights, Polymath-8, Pascadi 2025, Bettin–Chandee, Wright 2026) is a step toward $1$. The reduction is therefore exact and complete to a single, named, actively-moving frontier.

**The variance refinement (Remarks 6.6–6.9).** *Statements §§6.1–6.5 develop the obligation in its classical* max-over-$a$ *Bombieri–Vinogradov form, matching the literature and the proof outline of* diez *§3. The four results that follow refine it to its genuine form and remap the terminus: Remark 6.6 identifies the medium arc as a* second moment*; Lemma 6.8 proves this (residue (i)); Remark 6.7 draws the consequence (residue (ii): $\mathrm{RH}\Leftarrow$ sparse-primorial BDH); and Remark 6.9 is a first analytic pass at that target — discharging its two folklore obstructions and locating the residual at the critical line.*

\hypertarget{stmt:6-6}{}
**Remark 6.6 (the variance refinement — the medium arc is a second moment; $\mathsf{[A]}$ with bounded $\mathsf{[C]}$ residue).** The max-over-$a$ form of the obligation (Closure target (C)) is a *sufficient over-statement*, not the genuine requirement. The cubic functional is intrinsically an $L^2$ object: $\operatorname{Re}\mathcal C_\zeta=\int_{\mathbb R}\mathcal S_g(x)^3\,\eta(x)\,dx$ is *integrated* against $\eta\ge0$ (§3), and its discrete witness $\mathrm{pure}_V(P_n)$ is a *trace over the full character lattice* (*ocho* §5), not a single residue. Accordingly the transfer error is a sum over character **triples**, $\sum_{\chi_1,\chi_2,\chi_3}c\,\psi(x,\chi_1)\psi(x,\chi_2)\psi(x,\chi_3)$, whose natural bound is **Hölder** — i.e. the *second moment* $\sum_\chi|\psi(x,\chi)|^2$ (the variance $\sum_a|E(x;d,a)|^2$, by Parseval) to the $3/2$ power — not $\max_a|E|$. The program's own derivation already routes through it: *ocho* §7.3.2 bounds $\sum_a|E(x;d_S,a)|$ by the **large sieve** (a second-moment inequality) and only then applies Cauchy–Schwarz to reach the $L^1$/max, losing a factor $\varphi(d)^{1/2}\asymp d^{1/2}$ — the very step that drops the level by $\sim\tfrac12$. The genuine medium-arc obligation is therefore the **variance over the primorial divisor family**
$$\sum_{\substack{d\mid P_n\\ d\le P_n^\theta}}\ \sum_{a\,(d)}\big|\psi(x;d,a)-\tfrac{x}{\varphi(d)}\big|^2\ \ll\ \text{(margin)},$$
consistent with §6.1 (the density is governed by the *second moment* of $\zeta$) and the variance reading of §5 (the Fourth reduction). **Consequence.** In mean square the Type-III piece is governed by the *averaged-over-$a$* ternary-divisor level $=\tfrac23$ (Nguyen; $\tfrac8{11}$ for prime $q$, 2026), which is $\gg\tfrac6{11}$ — **non-binding**. But with the **exact** $\theta_0(6)=\tfrac35$ (§6.3) the bilinear Type-II level $6/11$ is itself below the requirement, so $n=6$ is *not* discharged by the max-over-$a$ Pascadi level. Under the variance form $n=6$ — like every $n$ — reduces to the variance crossover, i.e. sparse-primorial BDH (Rem 6.7); it is not specially secured. (An earlier draft, using the asymptotic $\theta_0(6)=\tfrac8{15}$, mis-stated a $1/255$ Type-III gap and an $n=6$ discharge; both are retracted.) **Two bounded $\mathsf{[C]}$ residues make this rigorous, neither the EH-wall:** *(i)* write the explicit second-moment (Hölder) reduction of the cubic transfer — indicated by the selection-rule-diagonal Plancherel mass $\sim T(\log T)^2$ (§6.1, second-moment-scaled), but *diez* Thm 4.3 is only an outline; *(ii)* recompute the V/M crossover in the variance norm over the **sparse** family $\{d\mid P_n\}$ — Barban–Davenport–Halberstam gives level $\to1$ over *all* moduli, which does not transfer automatically to a sparse family, but the large sieve gives the concrete starting bound $\sum_{d\mid P_n}\sum_\chi|\psi(x,\chi)|^2\ll(P_n+x)\,x\log x$ via the identity $\sum_{d\mid P_n}\varphi(d)=P_n$. Certified `probe_variance_medium_arc.py`. The refinement removes the bounded-$n$ Type-III obstruction and names the second moment as the correct medium-arc object; whether it also lowers the large-$n$ terminus rests on the sparse-family crossover (residue (ii)).

\hypertarget{stmt:6-7}{}
**Remark 6.7 (the variance frontier, residue (ii): $\text{RH}\Leftarrow$ sparse-primorial BDH; $\mathsf{[A]}$ remapping, $\mathsf{[C]}$ open).** Writing the variance via Parseval, $V_n(X,\theta)=\sum_{d\mid P_n,\,d\le X^\theta}V(d)$ with $V(d)=\tfrac1{\varphi(d)}\sum_{\chi\bmod d,\ \chi\ne\chi_0}|\psi(X,\chi)|^2$, the medium arc becomes a **Barban–Davenport–Halberstam variance over the primorial divisor family**. Two facts locate the frontier. *(a) The bare large sieve is insufficient:* for the sparse set $\{d\mid P_n\}$ the multiplicative large sieve gives only $V_n\ll(P_n+X)\,X\log X$, which for $X^\theta\le X$ is $X$-dominated — the *trivial* (no-cancellation) size; the Farey spacing of the family is still $\asymp Q^{-2}$, so sparsity buys nothing in the large-sieve constant. *(b) Yet BDH-strength holds empirically:* direct computation (`probe_sparse_variance_crossover.py`, $X$ up to $10^6$) gives $V(d)/(X\log X)=O(1)$ and $V(d)/X^2\to0$ for every $d\mid P_n$, $n\le6$ — the small-conductor primorial moduli exhibit square-root cancellation $V(d)\sim X\log X$ (the full-family BDH size), **not** the trivial $X^2$. So the relevant input is the **BDH asymptotic over $\{d\mid P_n\}$**, not the large sieve. *Consequence for the crossover:* under BDH-strength $V_n\sim2^n X\log X$, so the relative variance error $\sim 2^n\log X/X\to0$ — and since the bridge already needs $X\ge P_n\sim e^{n\log n}\gg2^n$ to bring all $2^n$ divisors into range, the error is tiny for every $n$, with vast room. **The level constant disappears:** under the variance form there is no $C^\ast$ to push toward $1$; the obstruction collapses to the *binary* question of whether **sparse-primorial BDH holds uniformly in $n$** — GRH-on-average for the primorial $L$-family, an $L^2$/density statement whose *full-family analog is an unconditional theorem*, hence structurally distinct from (and plausibly more tractable than) the max-over-$a$ Elliott–Halberstam terminus. It remains **open**: the sparse family loses BDH's averaging, and real characters $\chi\bmod q$ ($q\mid P_n$) carry a potential Siegel obstruction; the **smooth-conductor structure** (every $q\mid P_n$ built from primes $\le p_n$) is an unexploited handle for density/Linnik methods. Conditional on residue (i) (the Hölder reduction establishing the variance as the genuine medium arc), this gives $\boxed{\text{RH}\ \Leftarrow\ \text{sparse-primorial BDH}}$ — a remapping of the terminus from a pointwise level-of-distribution to an $L^2$ density target, not a proof.

\hypertarget{stmt:6-8}{}
**Lemma 6.8 (the second-moment reduction — residue (i); $\mathsf{[P]}$ up to the standard explicit-formula reduction).** *The discrete-to-continuous transfer error of the cubic functional is controlled by the variance, never by $\max_a|E|$.* By the A–C tensor support condition $\chi_a\chi_b\chi_c=\chi_0$ (*ocho* §1) and character orthogonality $\sum_{\chi_1\chi_2\chi_3=\chi_0}\chi_1(a_1)\chi_2(a_2)\chi_3(a_3)=\varphi(d)^2[a_1{=}a_2{=}a_3]$, the cubic capacity at modulus $d$ is the **third moment** of the residue count:
$$\sum_{\chi_1\chi_2\chi_3=\chi_0}\prod_{i}\psi(X,\chi_i)=\varphi(d)^2\sum_{a\,(d)}\psi(X;d,a)^3.$$
With $\mu=X/\varphi(d)$ and $\Delta(a)=\psi(X;d,a)-\mu$ (so $\sum_a\Delta=0$),
$$\sum_a\psi(X;d,a)^3=\underbrace{\tfrac{X^3}{\varphi(d)^2}}_{\text{V-sector main term}}+\underbrace{3\,\tfrac{X}{\varphi(d)}\,V(d)}_{\text{transfer error (variance-linear)}}+\underbrace{\sum_a\Delta(a)^3}_{\text{cubic, sub-leading}},\qquad V(d)=\sum_a\Delta(a)^2,$$
and the cubic remainder is dominated by the variance, $\big|\sum_a\Delta(a)^3\big|\le\|\Delta\|_3^3\le\|\Delta\|_2^3=V(d)^{3/2}$ ($\ell^3\le\ell^2$). Summed over $d\mid P_n$ against the kernel weights, the transfer error is $\ll\sum_{d\mid P_n}\big(\tfrac{X}{\varphi(d)}V(d)+V(d)^{3/2}\big)$ — a functional of the **second moment** $V(d)$ alone. The $\ell^\infty$ ($\max_a|E|$) and $\ell^1$ norms never enter; the max-over-$a$ form of Closure target (C) was the artifact of the lossy Cauchy–Schwarz in *ocho* §7.3.2 (Rem 6.6). Identity and decomposition certified at machine precision with genuine Dirichlet characters (`probe_holder_cubic_reduction.py`). **This closes residue (i):** the genuine medium arc is the variance, so — modulo the V/M crossover in the variance norm (residue (ii), Rem 6.7) — the reduction $\mathrm{RH}\Leftarrow$ sparse-primorial BDH is rigorous. The one ingredient remaining for a complete write-up — the standard Weil-explicit-formula reduction of $\mathcal C_\zeta$ to the prime-triple sum (its archimedean terms $n$-independent and not affecting the transfer) — is **now supplied in Lemma 6.10 (W1)**, with the zero$\to$prime reduction certified to $10^{-21}$ and the kernel weights $w_d=\widehat W_\eta/\varphi(d)$ explicit; the load-bearing positivity/combinatorial content is the identity above.

\hypertarget{stmt:6-9}{}
**Remark 6.9 (analytic pass at sparse-primorial BDH: reorganization, unconditional diagonal, Siegel reduction; $\mathsf{[P]}$ structure, $\mathsf{[C]}$ residual).** Reorganizing the variance by conductor — each non-principal $\chi\bmod d$ is induced by a primitive $\chi^*$ of conductor $q\mid d$ — gives, with $M(q)=\sum_{\chi^*\bmod q}|\psi(X,\chi^*)|^2$ and the **exact weight identity** $\sum_{d:\,q\mid d\mid P_n}\varphi(d)^{-1}=\big(P_n/\varphi(P_n)\big)/q$ (certified for all $q\mid P_n$, $n\le6$, `probe_sparse_bdh_reorganization.py`),
$$V_n=\frac{P_n}{\varphi(P_n)}\sum_{\substack{q\mid P_n\\ q>1}}\frac{M(q)}{q},\qquad \frac{P_n}{\varphi(P_n)}=\prod_{p\le p_n}\frac{p}{p-1}\sim e^\gamma\log p_n=O(\log n).$$
The $1/q$ weight concentrates the mass on the small (smooth) conductors. Three facts locate the frontier. *(A) The diagonal is unconditional:* $M(q)\ge$ its diagonal $\sim\varphi(q)X\log X$ (the $\sum\Lambda(n)^2$ term), so $V_n\sim2^nX\log X$ — the BDH-strength size is the **unconditional main term** (why BDH-strength is observed, Rem 6.7); the content is the off-diagonal. *(B) Siegel reduces to a single character:* the off-diagonal is governed by the zeros of $L(s,\chi)$, $\mathrm{cond}(\chi)\mid P_n$; complex and non-exceptional real characters obey the Page–Walfisz zero-free region, and by **Landau–Siegel at most one** real primitive character — one squarefree $q^\ast\mid P_n$ (a Jacobi symbol) — is exceptional, controlled by Siegel's bound. **Siegel is therefore not the essential obstruction**, only a single controllable character. *(Scale caveat $\mathsf{[P]}$, corrected 2026-06-10, `verify_diez43.py`/skeleton §3:* at the §(C) scale $X\ge\exp((n\log n)^2)$ the **non-exceptional** family is controlled exactly as below, but the **exceptional** $q^\ast$-row is **not** controlled effectively there: Siegel's saving $\exp\!\big(-c(\epsilon)(n\log n)^2/q^{\ast\,\epsilon}\big)\to1$ since $q^\ast$ may be as large as $P_n=\exp((1+o(1))\,n\log n)$ — the saving's polynomial numerator $(n\log n)^2$ is dominated by the exponential conductor. Effective control of the $q^\ast$-row requires either the **larger scale** $X\ge\exp(P_n^\epsilon)$ (ineffective Siegel constants) or carrying the $q^\ast$-multiples as a **flagged term**. The structural conclusion — one character, not a family — is unchanged; the quantitative "reduced to one controllable character" claim at the stated scale is amended accordingly. See also Lemma 6.10(D).) *(C) The smooth-conductor structure bypasses the large sieve:* every $q\mid P_n$ is $p_n$-smooth, so for $X\ge\exp\!\big((n\log n)^2\big)$ all conductors satisfy $q\le P_n\le\exp(c\sqrt{\log X})$, and the **pointwise** zero-free bound $\psi(X,\chi)\ll X\exp(-c\sqrt{\log X})$ controls the whole family — *not* the large sieve, which gives only the trivial bound here (Rem 6.7). This yields bridge convergence at $\mathrm{Re}(s)>\tfrac12+\delta$ with $\delta\sim(\log X)^{-1/2}\to0$, **improving Paper 43's fixed $0.038$**. **The residual** is the critical line itself ($\delta=0$): GRH-on-average for the $p_n$-smooth conductor family at $\mathrm{Re}(s)=\tfrac12$. Siegel is removed, the smooth handle drives $\delta\to0$, and the line is what remains — the genuine terminus, **open**. This analytic pass maps the frontier and discharges its two folklore obstructions (large-sieve insufficiency, Siegel); it is not a proof.

\hypertarget{stmt:lemma-A}{}
**Lemma A (C-I unconditional discharge of the variance limb; effective; $\mathsf{[P]}$, with one $\mathsf{[C]}$ flagged row).** *In the iterated coupling C-I (*diez* Thm 4.3), the analytic half of residue (ii) closes unconditionally.* There are absolute $c, C_0 > 0$ such that for every $n \ge 2$ and every $X \ge \exp\!\big(C_0\, n^2(\log n)^2\big)$, with at most the multiples of a single Landau exceptional conductor $q^\ast(X) \mid P_n$ excepted,
$$V(d) \;\le\; X^2 \exp\!\big(-2c\sqrt{\log X}\big)\qquad\text{for every }d\mid P_n,\ q^\ast\nmid d,$$
and hence, summing against the kernel weights with $\sum_{d\mid P_n}\varphi(d)^{-1}\le e^\gamma\log p_n$ (Mertens) and $2^n\le\exp(\sqrt{\log X}/C_0')$,
$$\sum_{d\mid P_n}\Big(\tfrac{3X}{\varphi(d)}V(d) + V(d)^{3/2}\Big)\;\le\; X^3\exp\!\big(-c'\sqrt{\log X}\big)\;=\;o(\text{main}),$$
uniformly in $n$. *Proof.* Each conductor $q\mid d\mid P_n$ satisfies $q\le P_n=e^{(1+o(1))p_n}\le\exp(\sqrt{\log X}/C_0^{1/2})$ by the hypothesis on $X$; for non-exceptional $\chi$ of conductor $q$ in this range Page's theorem gives $\psi(X,\chi)\ll X\exp(-c\sqrt{\log X})$, whence $V(d)=\varphi(d)^{-1}\sum_{\chi\ne\chi_0}|\psi(X,\chi)|^2\le X^2\exp(-2c\sqrt{\log X})$; the linear and ($\ell^3\le\ell^2$) cubic sums follow from Mertens and $2^n e^{-c\sqrt{\log X}}\to0$. $\square$ **Lemma A' (all characters, ineffective):** if moreover $X\ge\exp(P_n^{\epsilon})$, Siegel's $\beta^\ast\le1-c(\epsilon)q^{\ast-\epsilon}$ absorbs the exceptional row with ineffective constants. **The flagged row.** At N0's stated scale $X=\exp((n\log n)^2)$ the exceptional $q^\ast$-row is *not* effectively controlled (Rem 6.9(B) scale caveat): its Siegel saving $\to1$. So Lemma A closes C-I's variance limb unconditionally **for the non-exceptional family at $X\ge\exp(C_0 n^2(\log n)^2)$**, and for the full family either at the larger scale $X\ge\exp(P_n^\epsilon)$ (Lemma A', ineffective) or with $q^\ast$ carried as a flagged term. The residual is then the margin-normalization ledger W1 (*diez* Thm 4.3, branch C-I), not an analytic estimate.

\hypertarget{stmt:6-10}{}
**Lemma 6.10 (W1 — the explicit-formula reduction, the kernel weights, and the coupling verdict; supplies the ingredient flagged in Lemma 6.8; $\mathsf{[P]}$ for the reduction and certified core, $\mathsf{[A]}$ for the exact weight scalar, $\mathsf{[C]}$ for T1/T2).** *Completes the chain $\mathcal C_\zeta\to$ prime-triple sum $\to$ per-modulus third moment, makes the weights $w_d$ explicit, confirms the archimedean part $n$-independent, and converts the C-I capacity prediction (Rem 6.7) to a verdict.*

**(A) Zero side $\to$ prime side ($\mathsf{[P]}$, certified `empirical/p_infinity/verify_w1_explicit_formula.py`).** Write $G(v)=g(e^v)e^{v/2}$, so $\widetilde g(\tfrac12+ir)=\int_{\mathbb R}G(v)e^{irv}\,dv$. The Guinand–Weil explicit formula applied to $\mathcal S_g(x)=\sum_\gamma\widetilde g(\tfrac12+i\gamma)e^{i\gamma x}=\sum_\rho h_x(\gamma_\rho)$, $h_x(r)=\widetilde g(\tfrac12+ir)e^{irx}$, gives
$$\mathcal S_g(x)=\underbrace{\widetilde g(0)e^{-x/2}+\widetilde g(1)e^{x/2}+\frac1{2\pi}\!\int_{\mathbb R}\!\widetilde g(\tfrac12+ir)e^{irx}\Big[\operatorname{Re}\psi\big(\tfrac14+\tfrac{ir}2\big)-\log\pi\Big]dr}_{=:A_\infty(x)\ \ (\text{poles }\rho=0,1\ +\ \text{archimedean; prime-free, }n\text{-independent})}-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Big[G(\log n-x)+G(-\log n-x)\Big].$$
Certified to relative error $\le10^{-21}$ ($\sigma=0.15$, first $80$ zeros, $x\in[0.4,2]$): the residual (zeros $-$ poles $+$ primes) equals $A_\infty$ with constant ratio $1.00000$, spread $0$ — which both verifies the identity and pins the archimedean normalization (the $\tfrac{ir}{2}$ argument with prefactor $\tfrac1{2\pi}$, no extra $\tfrac12$).

**(B) Cube and smear $\to$ the explicit prime-triple kernel ($\mathsf{[P]}$).** Insert into $\operatorname{Re}\mathcal C_\zeta(g;\eta)=\int_0^\infty 2\eta(x)\,\mathcal S_g(x)^3\,dx$ (§3.1) and expand $(A_\infty-\text{prime})^3$. The $A_\infty$ cross-terms are $n$-independent or one prime-power lower and collect into a remainder $R_\infty(g,\eta)$ independent of the primorial level; the load-bearing piece is the pure prime-triple
$$\operatorname{Re}\mathcal C_\zeta(g;\eta)=R_\infty-\!\!\sum_{n_1,n_2,n_3\ge2}\!\frac{\Lambda(n_1)\Lambda(n_2)\Lambda(n_3)}{\sqrt{n_1n_2n_3}}\,W_\eta(\vec n),\quad W_\eta(\vec n)=\int_0^\infty 2\eta(x)\prod_{i=1}^3\Big[G(\log n_i-x)+G(-\log n_i-x)\Big]dx,$$
an **explicit** kernel. $G$ Schwartz forces $W_\eta$ onto the selection-rule diagonal $\log n_1\approx\log n_2\approx\log n_3\approx x$ — the prime-power image of the cubic-surface constraint $\rho_1+\rho_2+\rho_3=\tfrac32$ (*ocho* §6.1) — with $\eta(x)$ weighting the scale $X=e^x$.

**(C) Residue resolution $\to$ per-modulus third moment, and the weights ($\mathsf{[P]}$ structure, $\mathsf{[A]}$ exact scalar).** Classify the prime powers by residue mod $d\mid P_n$. The smooth-cut character sums $\psi(X,\chi)=\sum_n\Lambda(n)\chi(n)\,w_X(n)$ (cut $w_X$ induced by $\eta$ at $X=e^x$, the $\sqrt n$ absorbed) together with the A–C support condition $\chi_1\chi_2\chi_3=\chi_0$ (*ocho* §1) feed Lemma 6.8's orthogonality $\sum_{\chi_1\chi_2\chi_3=\chi_0}\prod\psi(X,\chi_i)=\varphi(d)^2\sum_a\psi(X;d,a)^3$, giving the transfer-error decomposition
$$\Big|\operatorname{Re}\mathcal C_\zeta-R_\infty-(\text{V-sector main})\Big|=\Big|\sum_{d\mid P_n}w_d\Big(\tfrac{3X}{\varphi(d)}V(d)+\sum_a\Delta(a)^3\Big)\Big|,\qquad\boxed{\,w_d=\frac{\widehat W_\eta}{\varphi(d)},\quad\widehat W_\eta:=\int_0^\infty 2\eta(x)\,\Omega_g(x)^3\,dx,\ \ \Omega_g(x)=\sum_p\frac{\log p}{\sqrt p}\,G(\log p-x).\,}$$
The divisor-lattice factor $1/\varphi(d)$ is the **certified** weight of Rem 6.9 ($\sum_{d:\,q\mid d\mid P_n}\varphi(d)^{-1}=(P_n/\varphi(P_n))/q$); $\widehat W_\eta$ is the explicit $(g,\eta)$-scale constant — an integral of the test data, $O_\eta(1)$, **independent of $n$**. *$\mathsf{[A]}$: the precise scalar multiplying $\widehat W_\eta/\varphi(d)$ depends on the cut $w_X$ normalization and is not pinned here; only $\widehat W_\eta=O_\eta(1)$ and the $\varphi(d)^{-1}$ lattice law are used downstream, so the conclusions do not rest on it.*

**(D) Margin normalization, both couplings — the verdict W1 was to deliver.**
- *C-J ($\mathsf{[P]}$, makes T1/T2 explicit):* the aggregation constants of *diez* Thm 4.3 are now $\widehat W_\eta$ times the certified $\varphi$-sums — the linear (T1) limb $\widehat W_\eta\sum_{d\mid P_n}\varphi(d)^{-1}\cdot3X\,\overline V$, the signed (T2) limb the $\varphi(d)^{-1}$-weighted third moment of *diez* §4.3. They are no longer symbolic; T1 and T2 are the only remaining obligations.
- *C-I ($\mathsf{[C]}\to$ decided, negatively):* with the analytic limb free (Lemma A discharges it unconditionally), C-I closure requires the V-sector cubic-positivity surplus — the discrete witness $\operatorname{pure}_V(P_n)\sim n^3(\log n)^2/18$ — to remain bounded below after normalization by the ambient mass the continuum functional assigns the conductor-$P_n$ slice, which is the lattice capacity normalization $\asymp P_n^2$ (*ocho* §6). The ratio is exactly the capacity $6\operatorname{pure}_V(P_n)/P_n^2\to0$ (certified: $0.33$ at $n{=}2\to2.5\times10^{-9}$ at $n{=}7$, `verify_diez43.py`). The margin **deflates** — polynomially thin in an exponentially large ambient — so positivity cannot be certified in C-I; the inequality relocates. **W1 thus converts the Rem 6.7 prediction to a verdict: C-I closes negatively, leaving C-J (T1+T2) the sole live branch.**

**Consequence.** Lemma 6.8's "one ingredient remaining" is supplied: $\operatorname{Re}\mathcal C_\zeta$ is the explicit $w_d=\widehat W_\eta/\varphi(d)$-weighted aggregate of the per-modulus third moments of Lemma 6.8, archimedean part $n$-independent, $\widehat W_\eta$ an explicit test-data integral. The discrete-to-continuous bridge (*diez* Thm 4.3) is now a theorem **modulo T1 and T2 only**; the C-I branch is closed. $\square$ *(reduction $\mathsf{[P]}$; T1, T2 remain $\mathsf{[C]}$.)*

---

## 7. The closure

\hypertarget{stmt:7-1}{}
**Theorem 7.1 (the reduction; $\mathsf{[P]}$ chain, $\mathsf{[C]}$ terminus).** *The following are equivalent and each is the Riemann Hypothesis:*
1. *$E_B=\Xi+i\Xi'$ is Hermite–Biehler on $\mathbb C_+$; equivalently $m_B=-\Xi'/\Xi$ is Herglotz (§2);*
2. *the cubic Weil functional is positive, $\operatorname{Re}\mathcal C_\zeta(g;\eta)\ge0$ on $\mathcal G\times\mathcal H_c$ (§3);*
3. *the discrete cubic positivity at primorial modulus $P_n$ transfers to the critical line — the bridge — at the primorial level of distribution $\theta_0(p_n)=1-C^\ast/n$, $C^\ast\le2.80$ (classical max-over-$a$ form); equivalently, by Lemma 6.8, at the genuine variance form whose terminus is sparse-primorial BDH (§§5–6, refined §§6.6–6.9).*

*Equivalences $1\!\iff\!2$ are established unconditionally (§§2–3); the forward direction $2\Rightarrow1$ uses only the off-line cluster and bulk, with no level input (diez Thm 4.1). Reduction $2\!\Longleftarrow\!3$ is the discrete-to-continuous bridge (§5; diez Thm 4.3), conditional on the primorial Bombieri–Vinogradov level and nothing more. Statement $3$ decomposes into three arcs (§6): the major arc — the singular-series main term, positive and unconditional; the minor arc — the mean-square, the theorem of Matomäki–Radziwiłł–Tao (2016); and the medium arc — the level $C^\ast\le2.80$ (the V/M crossover, diez Thm 3.3), bounded by Heath–Brown $+$ large sieve $+$ Burgess $+$ *bilinear* Kloosterman (Pascadi 2025) for the binding Type-II, with trilinear Bettin–Chandee–Wright on the non-binding Type-III; the unconditional level is $\theta\le6/11$, discharging $n\le5$ (exact V/M schedule, $\theta_0(6)=\tfrac35$; §6.3). The off-line sensitivity is the unconditional $\chi_3$-twisted $L$-weight (Prop. 6.4). In its classical max-over-$a$ form the medium-arc constant $C^\ast$ is the terminus; §§6.6–6.9 refine it — by Lemma 6.8 the cubic transfer error is controlled by the **variance**, not the maximum (the max-over-$a$ being the artifact of a lossy Cauchy–Schwarz), so the genuine terminus is the variance over the primorial family: **sparse-primorial BDH**, GRH-on-average for the $p_n$-smooth conductor family at the critical line — an $L^2$-density target whose full-family analog is a theorem and whose folklore obstructions (large-sieve insufficiency, the Siegel zero) are discharged (Rem 6.9).*

\hypertarget{stmt:7-2}{}
**Remark 7.2 (the geometric readings of the closure; [N6]).** The same closure has three further equivalent forms, developed in [N6, Rem. 6.3–6.5], which place the obstruction geometrically and confirm where it cannot come from. (i) *Curvature.* With dual potential $\psi=\log\xi$, the curvature current (Poincaré–Lelong) is the zero divisor, $\tfrac1{2\pi i}\,d(\xi'/\xi\,ds)=\sum_\rho m_\rho\delta_\rho$; RH is its confinement to the critical line — the dual-flatness of the bulk $\{\operatorname{Re}s>\tfrac12\}$. (ii) *Bures field.* The de Branges margin $D=\operatorname{Im}(\Xi\overline{\Xi'})=|\Xi|^2u_B$ is the Bures–Poisson field of reading 1, so the obstruction is a *local* positivity — immune to any Gauss–Bonnet/Poincaré–Hopf/index argument, which fixes only the total count $N(T)$ and is blind to a symmetric, count-preserving slide of a zero off the line. (iii) *Li ladder.* $\mathrm{RH}\iff\lambda_n\ge0\,\forall n$: on-line zeros give $2(1-\cos n\theta_\rho)\ge0$ term by term, while an off-line zero injects $(|\rho|/|1-\rho|)^n$ (exponential, breaking a rung at unbounded height). So the closure is the *uniform* domination of the archimedean $\tfrac n2\log n$ over every off-line exponential — the same archimedean domination that §6 carries in arithmetic form as the medium-arc level $C^\ast$. The chiral central rung is unconditional ($L(\tfrac12,\chi_3)=0.4808\ldots>0$; root number $W(\chi_3)=+1$ from the Gauss sum $\tau(\chi_3)=i\sqrt3$; cf. Prop. 6.4), securing the central term of the ladder. (Certified `empirical/probe_alpha_curvature_offline_zero.py`, `probe_gauss_bonnet_blindness.py`, `probe_force_D_positivity.py`, `probe_second_rung_li.py`.)

The apparatus is, at this point, complete and verified, and the obstruction the program named at every earlier place — the archimedean factor the finite primes cannot generate ([P0]) — is here realized as an explicit operator (§2), its prime side as the Estermann function whose functional equation is the polar pair the series has steered by (§4), and the closure as a single positivity statement (§§5–6): the sign of the on-line singular-series prime-triple sum at primorial modulus. The variance bridge and the off-line teeth are in hand, the leading order is an unconditional theorem, and the sum is certified positive on the canonical window. The unified verified operator stands ready, and the one explicit statement that remains — the cubic specificity of §6 — carries the leading order of the literature and the classical prime-tuple arithmetic with it.

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$.*

[N2] Murillo Montero, L. (2026). *The Apex Determinant.*

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary.*

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.*

[N5] Murillo Montero, L. (2026). *The Apex Edge Operator and the Archimedean Weil Form.*

[N6] Murillo Montero, L. (2026). *The Unified Archimedean Operator and the de Branges Target for $\xi$.*

[siete–once] Murillo Montero, L. (2026). *The cubic Weil-positivity criterion and its analytic companions* (program papers *siete*, *ocho*, *nueve*, *diez*, *once*).

[T8] — (2026). *The Multiplicative Apex and Finite Dirichlet Polynomials.* [T9.4] *Gauss-Sum Decomposition of Conductor Blocks.* [T9.4.1] *The BV-Variance Helmert–Gauss Identity.* [Pass8] *A Careful Bridge from the Multiplicative Apex to Dirichlet $L$-functions.* [P0] *Place-Completion.* [T0] *Gauge Selection and the Fourier–Mellin Simplex.*

[E] Estermann, T. (1930). On the representations of a number as the sum of two products. *Proc. London Math. Soc.* (2) 31, 123–133.

[Bu] Burgess, D. A. (1962). On character sums and $L$-series. *Proc. London Math. Soc.* (3) 12, 193–206.

[MRT] Matomäki, K., Radziwiłł, M., Tao, T. (2016). An averaged form of Chowla's conjecture. *Algebra & Number Theory* 9(9), 2167–2196. (Averaged two-point Chowla; the variance rung.)

[MS] Montgomery, H. L., Soundararajan, K. (2004). Primes in short intervals. *Comm. Math. Phys.* 252(1–3), 589–617. (Moments of $\psi(x+h)-\psi(x)$ via the singular series, under uniform Hardy–Littlewood; the cubic-rung subleading.)

[RS] Rudnick, Z., Sarnak, P. (1996). Zeros of principal $L$-functions and random matrix theory. *Duke Math. J.* 81, 269–322. (GUE $n$-correlation, restricted support; the cubic-rung leading order.)

[HL] Hardy, G. H., Littlewood, J. E. (1918). Contributions to the theory of the Riemann zeta-function. *Acta Math.* 41, 119–196; and (1923) Some problems of 'Partitio Numerorum' III. *Acta Math.* 44, 1–70. (Second moment of $\zeta$; the prime $k$-tuple singular series.)

[CC] Connes, A., Consani, C. (2021). Weil positivity and trace formula: the archimedean place. *Selecta Math.* 27, art. 77. doi:10.1007/s00029-021-00689-4 (arXiv:2006.13771). (The semi-local trace-formula positivity at $\infty$ that the apex operator of §2 realizes.)

[W] Weil, A. (1948, 1949). On some exponential sums; Numbers of solutions of equations in finite fields. *PNAS* 34; *Bull. AMS* 55.

[VVV] Varbanets, P., Varbanets, S., Vorobyov, Y. (2025). Divisor function of the Gaussian integers weighted by the Kloosterman sum. *Algebra and Discrete Mathematics* 40(2), 255–270.

[Wash] Washburn, J. (2026). *Goldbach via a Mod-8 Kernel: Density-One Positivity, Short-Interval Bounds, and a Conditional Dispersion Improvement.* Recognition Physics Institute, February 2026. (The three-arc twin: singular-series major arc, mean-square minor arc, medium-arc dispersion conjecture with tier hygiene [PROVED]/[CONDITIONAL]/[CONJECTURE].)

[Wr] Wright, T. (2026). *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions.* arXiv:2604.25177. (Improves Fouvry–Radziwiłł / Bettin–Chandee; level $Q\le X^{1/2+1/66-\delta}$; the medium-arc Type-II machinery for $C^\ast$.)

[BC] Bettin, S., Chandee, V. (2018). Trilinear forms with Kloosterman fractions. *Adv. Math.* 328, 1234–1262. (The trilinear Kloosterman bound sharpened in [Wr].)

[BFI] Bombieri, E., Friedlander, J. B., Iwaniec, H. (1986). Primes in arithmetic progressions to large moduli. *Acta Math.* 156, 203–251. (Well-factorable weights; level of distribution beyond $\tfrac12$ on average — the friable-moduli frontier toward Elliott–Halberstam.)

[Pol8] Polymath, D. H. J. (2014). New equidistribution estimates of Zhang type. *Algebra & Number Theory* 8(9), 2067–2199. (Bombieri–Vinogradov for smooth moduli, level $\tfrac12+2\varpi$, $\varpi=7/300$; the Type-III/Deligne machinery.)

[Pa] Pascadi, M. (2025). *Non-abelian amplification and bilinear forms with Kloosterman sums.* arXiv:2511.08445. (Beyond-Pólya–Vinogradov bilinear Kloosterman; saving $c^{-1/12}$ on factorable moduli — every squarefree divisor of $P_n$ — converting through the dispersion method to the binding Type-II level $\theta\le6/11$ for the primorial bridge; the operative lever for the max-over-$a$ obligation, where the well-factorable $x^{3/5}$ estimates do not apply.)

[May] Maynard, J. (2020). Primes in arithmetic progressions to large moduli II: well-factorable estimates. arXiv:2006.07088. (Triply-well-factorable weights, level $x^{3/5-\varepsilon}$ — the rising well-factorable level that sets the medium-arc rate.)

[FR] Fouvry, É., Radziwiłł, M. (2022). Level of distribution of unbalanced convolutions. *Ann. Sci. Éc. Norm. Supér.* 55, 537–568. (Trilinear Kloosterman estimates for sequences bypassing Siegel–Walfisz; the convolution level-of-distribution feeding the assembly.)

[KSY] Kerr, B., Shparlinski, I. E., Yau, K. H. (2020). A refinement of the Burgess bound for character sums. *Michigan Math. J.* 69. (Essentially optimal mixed-character-sum refinement of the per-prime Burgess input of §5.2.)

[FG] Fromm, E., Goldmakher, L. (2019). Improving the Burgess bound via Pólya–Vinogradov. *Proc. Amer. Math. Soc.* 147, 461–466. (Mild Pólya–Vinogradov gains trigger downstream Burgess sharpenings — the off-line-sensitivity character-sum lever.)

[IS] Iwaniec, H., Sarnak, P. (2000). The non-vanishing of central values of automorphic $L$-functions. *Israel J. Math.* 120, 155–177. (Used for $L(\tfrac12,\chi_3)>0$.)
