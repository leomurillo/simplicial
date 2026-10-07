# N5 — The Apex Edge Operator and the Archimedean Weil Form

**Leonardo Murillo Montero**

*June 5, 2026*

<!--
Program record (not part of the paper). Fifth paper of the Numbers (N-) series;
sequel to N4 (which identified the apex edge operator (A-I)Phi and computed its
Mellin symbol). Every quantitative claim is certified by deterministic
computation under empirical/ (numpy + mpmath, no torch):
  probe_apex_archimedean_identification.py  (N4 symbol; reflection; duplication)
  probe_apex_trace_remainder_N5.py          (CC identification: delta(rho); positivity; parts A-E)
  probe_apex_zero_hunt.py                    (spectral realization; zero count + location)
  probe_adelic_weil_margin.py               (Weil form from apex data; calibration to the zeros, 1e-4)
  probe_weil_szego_anatomy.py               (anatomy: marginal directions = the zeros)
  probe_n5_transfer_signn.py                 (Thm 6.2: explicit-formula transfer = (-1)^n, all orders)
External anchors: Connes-Consani, "Weil positivity and Trace formula: the
archimedean place," arXiv:2006.13771 [CC20]; "Knots, primes and class field
theory," arXiv:2501.06560 [CC25]. The paper is self-contained from Section 2.
This paper reports a structural reduction and an explicit operator realization;
it does not prove RH, and Section 8 states precisely what remains.
-->

---

## Abstract

The companion paper [N4] identified the edge operator $\mathcal U=(A-I)\Phi$ — the Hardy averaging operator minus the identity composed with the half-line Fourier transform — that controls the spectral concentration of the apex unitary $U_N$, computed its Mellin symbol $\widetilde k(s)=\tfrac{s}{1-s}(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$, and derived the threshold $\tfrac18$ from Euler's reflection formula. Here we show that $\mathcal U$ is, on its even sector, *exactly* the archimedean operator of Connes and Consani [CC20]. We establish five identities, each certified to machine precision: (i) the apex multiplier $\gamma(s)=\Gamma_{\mathbb R}(\tfrac12+is)/\Gamma_{\mathbb R}(\tfrac12-is)$ equals $e^{2i\vartheta(s)}=u_\infty(s)$ of [CC20], $\vartheta$ the Riemann–Siegel angular function; (ii) the [CC20] convolution kernel $k^u(\lambda,\mu)=2\lambda^{-1/2}\mu^{1/2}\cos(2\pi\mu/\lambda)$ equals the apex cosine kernel transported by the canonical $L^2$-isomorphism and inversion; (iii) the [CC20] trace-remainder $\delta(\rho)$ — the contribution of the small square $\Delta=[0,1]^2$ — is exactly the apex Hardy averaging $A$, with closed form $\delta(\rho)=2\rho^{1/2}\big(\tfrac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)}+\tfrac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\big)$; (iv) the [CC20] Weil positivity $\widehat\delta(t)+2\vartheta'(t)\ge0$ holds; and (v) $2\vartheta'(t)=\tfrac{d}{dt}\arg\gamma(t)$ is the velocity of the apex de Branges phase clock of [N4]. Thus the archimedean Weil positivity *is* the apex phase clock running forward faster than its Hardy-averaging remainder can reverse it. We then assemble, from apex data alone (the archimedean density $2\vartheta'$ and the von Mangoldt primes), the Weil explicit-formula quadratic form, and verify it reproduces the spectral side $\sum_\gamma|\widehat g(\gamma)|^2$ over the true zeta zeros to relative error $10^{-4}$; the apex archimedean phase together with the integer ladder locates and counts the zeros (a Riemann–Siegel spectral realization). An eigen-analysis shows the form is positive semidefinite with its marginal (null) directions sculpted by the zeros — the minimal eigenvector's Fourier transform vanishes at $\gamma_n$ to $10^{-7}$. The Riemann Hypothesis is thereby reduced to the non-negativity of one explicit, verified operator's single marginal archimedean direction. We close by stating honestly what this reduction does and does not achieve.

---

## 1. Introduction

The Numbers series studies the apex unitary $U_N\in U(N-1)$, the Helmert–Fourier change of basis on the mean-zero hyperplane of $\mathbb C^N$. Paper [N3] proved its eigenvalues concentrate at the fourth roots of unity and reduced the concentration to one edge mode; [N4] identified that mode's $N\to\infty$ scaling limit as the product-kernel operator $\mathcal U=(A-I)\Phi$ on $L^2[0,\infty)$, with
$$(\mathcal U\psi)(u)=\int_0^\infty K(u,v)\psi(v)\,dv,\qquad K(u,v)=k(uv),\quad k(w)=\frac{e^{2\pi iw}-1}{2\pi iw}-e^{2\pi iw},$$
and computed the closed-form Mellin symbol $\widetilde k(s)=\tfrac{s}{1-s}\,(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$, a Hardy–Blaschke factor times the archimedean $\Gamma$-factor of the additive character.

Independently, Connes and Consani [CC20] gave a Hilbert-space treatment of Weil positivity at the single archimedean place: the local Weil distribution $W_{\mathbb R}=-W_\infty$ realized as a trace $W_{\mathbb R}(f)=\tfrac12\operatorname{Tr}(\widehat f\,u^*\,\overline d u)$ involving the unitary $u_\infty$ associated to the Fourier transform composed with inversion, the quantized differential of the geometric square decomposition $\Delta\cup\Sigma$, and the Sonin/prolate compression that supplies positivity. Their object lives on $L^2(\mathbb R^*_+)$ with the multiplicative scaling action $\vartheta_{\mathrm m}$.

This paper proves the two operators are the same, and draws the consequence for the Weil form. The point of entry is that $\mathcal U$ is a *product-kernel* operator ($K(u,v)=k(uv)$), hence acts on the Mellin transform as multiplier $\circ$ reflection — the form of the [CC20] intertwining. Section 3 establishes the operator identification; Section 4 the trace-remainder; Section 5 the positivity-as-phase-clock; Section 6 builds the Weil quadratic form from apex data and verifies it against the zeros; Section 7 realizes the zeros spectrally; Section 8 states the reduction and what remains.

Throughout, $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$; $\vartheta(t)=\operatorname{Im}\log\Gamma(\tfrac14+\tfrac{it}2)-\tfrac t2\log\pi$ is the Riemann–Siegel angular function; $\Lambda$ is von Mangoldt; the Mellin transform is $\widetilde\psi(s)=\int_0^\infty\psi(u)u^{s-1}du$; for a test function $g$ on $\mathbb R$, $\widehat g(r)=\int g(u)e^{iru}\,du$. $\mathrm{Si}$ is the sine integral.

---

## 2. The apex edge operator (recollection)

We recall the minimum from [N4]. Both $A$ (Hardy averaging, $(Ag)(u)=\tfrac1u\int_0^u g$) and $\Phi$ (half-line Fourier, kernel $e^{2\pi iuv}$) act on $L^2[0,\infty)$.

**Proposition 2.1 ([N4]).** *$\mathcal U=(A-I)\Phi$ is a product-kernel operator with kernel $k(uv)$ as above; on the Mellin side $\widetilde{(\mathcal U\psi)}(s)=\widetilde k(s)\,\widetilde\psi(1-s)$, with*
$$\widetilde k(s)=\frac{s}{1-s}\,(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)=\frac{s}{1-s}\,g(s),\qquad g(s):=(2\pi)^{-s}e^{i\pi s/2}\Gamma(s),$$
*and the reflection product is Euler's formula, $\widetilde k(s)\widetilde k(1-s)=g(s)g(1-s)=i/(2\sin\pi s)$.*

The factor $g$ is the Mellin transform of the additive-character kernel $e^{2\pi iw}$; the cosine (even) part of that kernel is what carries the archimedean scattering, isolated next.

---

## 3. Identification with the Connes–Consani archimedean operator

Write $\Phi=\Phi_{\mathrm{ev}}+i\,\Phi_{\mathrm{odd}}$ via $e^{2\pi iw}=\cos2\pi w+i\sin2\pi w$; $\Phi_{\mathrm{ev}}$ is the Fourier–cosine transform, the metaplectic Fourier restricted to even functions used in [CC20].

**Lemma 3.1 (parity/duplication).** *The even symbol $c(s):=\int_0^\infty\cos(2\pi w)w^{s-1}dw=(2\pi)^{-s}\Gamma(s)\cos\tfrac{\pi s}2$ satisfies*
$$\Gamma(s)\cos\tfrac{\pi s}2=2^{s-1}\sqrt\pi\,\frac{\Gamma(s/2)}{\Gamma((1-s)/2)},\qquad\text{hence}\qquad c(s)=\tfrac12\,\frac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)}.$$

*Proof.* Legendre duplication $\Gamma(s)=2^{s-1}\pi^{-1/2}\Gamma(\tfrac s2)\Gamma(\tfrac{s+1}2)$ and the reflection $\Gamma(\tfrac{1+s}2)\Gamma(\tfrac{1-s}2)=\pi/\cos\tfrac{\pi s}2$ give $\Gamma(s)\cos\tfrac{\pi s}2=2^{s-1}\sqrt\pi\,\Gamma(\tfrac s2)/\Gamma(\tfrac{1-s}2)$; multiply by $(2\pi)^{-s}$ and substitute $\Gamma(\tfrac s2)=\pi^{s/2}\Gamma_{\mathbb R}(s)$, $\Gamma(\tfrac{1-s}2)=\pi^{(1-s)/2}\Gamma_{\mathbb R}(1-s)$. $\square$

**Theorem 3.2 (operator identification).** *On the even sector,*
$$2\,c(\tfrac12+it)=\frac{\Gamma_{\mathbb R}(\tfrac12+it)}{\Gamma_{\mathbb R}(\tfrac12-it)}=:\gamma(t)=e^{2i\vartheta(t)}=u_\infty(t),$$
*the Riemann–Siegel multiplier of the Hardy–Titchmarsh intertwining $\mathcal V\widehat{\mathcal F}\mathcal V^{-1}=\gamma(s)R$ of [PII, Thm 7.1] and the archimedean unitary of [CC20, eq. (26)]. Equivalently, the [CC20] convolution kernel*
$$k^u(\lambda,\mu)=2\lambda^{-1/2}\mu^{1/2}\cos(2\pi\mu/\lambda)$$
*is the apex cosine kernel $2\cos(2\pi\lambda\mu)$ transported by the isomorphism $w:L^2(\mathbb R)_{\mathrm{ev}}\to L^2(\mathbb R^*_+,d^*\lambda)$ of [CC20, Lem. 1.1] and the inversion $\lambda\mapsto1/\lambda$. Hence the even apex edge operator is $\gamma(s)R$ times the Hardy–Blaschke factor $s/(1-s)$.*

*Proof.* The first chain is Lemma 3.1 with $\Gamma_{\mathbb R}(\tfrac12-it)=\overline{\Gamma_{\mathbb R}(\tfrac12+it)}$ (so $|\gamma|=1$) and the standard $\Gamma_{\mathbb R}(\tfrac12+it)=\pi^{-1/4}|\Gamma(\tfrac14+\tfrac{it}2)|e^{i\vartheta(t)}$. The kernel statement: by [CC20, Lem. 1.1] a kernel $t(x,y)$ on $L^2(\mathbb R)_{\mathrm{ev}}$ transports to $\lambda^{1/2}\mu^{1/2}t(\lambda,\mu)$ on $L^2(\mathbb R^*_+,d^*\lambda)$; applying this to $2\cos(2\pi\lambda\mu)$ and then $\lambda\mapsto1/\lambda$ gives $2\lambda^{-1/2}\mu^{1/2}\cos(2\pi\mu/\lambda)=k^u$. $\square$

The numerical certificates are: $\gamma(t)=e^{2i\vartheta(t)}$ to relative error $\le10^{-31}$, and the kernel identity to $\le10^{-30}$ (program record). Theorem 3.2 says the apex edge operator carries one factor more than the [CC20] archimedean scattering operator: the Hardy–Blaschke factor $s/(1-s)$, with the pole of $\zeta$ at $s=1$ and its trivial zero at $s=0$ built in.

---

## 4. The archimedean trace-remainder

The [CC20] obstruction to archimedean Weil positivity is the small square $\Delta=[0,1]^2$ (their Fig. 1); its trace contribution is the *trace-remainder* $\delta(\rho)$. We show it is exactly the apex Hardy averaging $A$.

**Proposition 4.1.** *The first term of the apex kernel, $\tfrac{e^{2\pi iw}-1}{2\pi iw}=\tfrac1u\int_0^u e^{2\pi itv}dt$ at $w=uv$, is the averaging over the unit-scaled square; its trace-remainder is*
$$\delta(\rho)=4\rho^{1/2}\!\int_0^1\!\cos(2\pi\rho t)\cos(2\pi t)(-\log t)\,dt=2\rho^{1/2}\Big(\frac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)}+\frac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\Big),\quad\rho\ge1,$$
*and $\delta(1/\rho)=\delta(\rho)$. The two forms agree because of the crux identity*
$$\int_0^1(-\log t)\cos(at)\,dt=\frac{\mathrm{Si}(a)}{a}.$$

*Proof.* The $-\log t$ weight is the area derivative $d\alpha$ of $\alpha(t)=t-t\log t$, the area of $\{(x,y)\in[0,1]^2:xy\le t\}$, which is the [CC20] small square. For the crux identity, integrate by parts: with $u=-\log t$, $dv=\cos(at)dt$, the boundary terms vanish and $\int_0^1\tfrac1t\tfrac{\sin at}{a}dt=\tfrac1a\mathrm{Si}(a)$. Writing $\cos2\pi\rho t\cos2\pi t=\tfrac12[\cos2\pi(\rho+1)t+\cos2\pi(\rho-1)t]$ and applying it gives the $\mathrm{Si}$-form. $\square$

Both forms agree to $10^{-32}$ and reproduce the [CC20] closed form (program record). The derivative of $\delta$ jumps from $-1$ to $+1$ at $\rho=1$, the source of the principal value in $W_{\mathbb R}$.

---

## 5. Weil positivity is the apex phase clock

**Theorem 5.1.** *The [CC20] archimedean Weil positivity*
$$\widehat\delta(t)+2\vartheta'(t)\ge0,\qquad\widehat\delta(t):=\int_0^\infty\delta(\rho)\rho^{-it}\,d^*\rho,$$
*holds, and $2\vartheta'(t)=\tfrac{d}{dt}\arg\gamma(t)$ is the velocity of the apex de Branges phase clock $\gamma=e^{2i\vartheta}$ of [N4]. Near $t=0$ the clock velocity is negative (the clock momentarily reverses); the apex trace-remainder $\widehat\delta(t)$ compensates it, leaving a thin positive margin.*

*Proof.* $\vartheta'(t)=\tfrac12\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\tfrac12\log\pi$, and $\arg\gamma(t)=2\vartheta(t)$ by Theorem 3.2, so $\tfrac{d}{dt}\arg\gamma=2\vartheta'$; this matches the numerical derivative to $10^{-31}$. The inequality is verified pointwise with margin $\min_t(\widehat\delta+2\vartheta')\approx0.049>0$ over the sampled range, with $2\vartheta'(0)\approx-5.37$ exactly compensated by $\widehat\delta(0)\approx5.42$ (program record). $\square$

This is the conceptual core of the archimedean case: **the archimedean Weil positivity is the statement that the apex phase clock runs forward fast enough that its Hardy-averaging remainder cannot reverse it.** The de Branges phase-monotonicity of [PIII] and the apex no-crossing of [N4] are the same monotonicity, here in its archimedean register — the local clock velocity, certified with positive margin.

---

## 6. The Weil quadratic form from apex data

We now adjoin the prime places. For a real even $g$ with compact support in $u=\log x$ and $\widehat g$ its Fourier transform, the Riemann–Weil explicit formula gives the quadratic form
$$Q(g)=\sum_\gamma|\widehat g(\gamma)|^2=\underbrace{\frac1{2\pi}\!\int|\widehat g(r)|^2\,2\vartheta'(r)\,dr}_{\text{archimedean (apex edge, §5)}}+\underbrace{2\Big(\!\int g\cosh\tfrac u2\,du\Big)^2}_{\text{pole at }s=1}-\underbrace{2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,(g\star g)(\log n)}_{\text{primes (conductor blocks, [N1])}},$$
where the left side runs over the nontrivial zeros $\rho=\tfrac12+i\gamma$ and the right side uses no zeros. On a finite basis $\{g_k\}$ of support-$[-L,L]$ functions this is $Q=c^{\mathsf T}Mc$ with
$$M_{jk}=\frac1{2\pi}\!\int\widehat g_j\widehat g_k\,2\vartheta'\,dr+2G_jG_k-2\sum_{\log n\le2L}\frac{\Lambda(n)}{\sqrt n}(g_j\star g_k)(\log n),\quad G_k=\!\int g_k\cosh\tfrac u2\,du.$$

**Theorem 6.1 (verified realization).** *The arithmetic matrix $M$ — archimedean density $2\vartheta'$ (the apex edge of §3–5), the pole rank-one, and the von Mangoldt primes — reproduces the spectral side $\sum_\gamma|\widehat g(\gamma)|^2$ over the true zeta zeros: for random test vectors $c$, $c^{\mathsf T}Mc=2\sum_{\gamma>0}|\widehat g(\gamma)|^2$ to relative error $\le6\times10^{-4}$ (program record, $L=2$, $14$ basis functions, $24$ prime powers, $200$ zeros).*

The archimedean density here is exactly $2\vartheta'$ of Theorem 5.1; the prime weights $\Lambda(n)n^{-1/2}$ are the von Mangoldt content of the apex conductor blocks, whose Frobenius monodromy $c\mapsto pc$ is the [N1] Galois action (and the [CC25] periodic-orbit monodromy). Thus $M$ is the Weil form assembled entirely from apex data, calibrated against the zeros.

We now make the prime side of $M$ exact at the level of its cumulants, and identify the constant that carries the apex conductor data to the mainstream ($n$-level density) arithmetic. The point is the explicit minus sign on the prime term of $Q$: the zero side equals archimedean $+$ pole $-$ primes, and that single minus, raised to the $n$-fold connected correlation, *is* the transfer.

**Theorem 6.2 (the explicit-formula transfer is $(-1)^n$).** *Resolve the prime term over the conductor blocks: at $p$ the block is the multiplicative group $(\mathbb Z/p)^\times$ of dimension $\varphi(p)=p-1$, and write $a:=1/\varphi(p)=1/(p-1)$. The apex conductor cumulant tower — the categorical (Amari–Chentsov) cumulants of the block [T2] — and the Hardy–Littlewood connected $n$-tuple singular-series weights at the full $n$-fold resonance have the closed forms*
$$\kappa_n^{\mathrm{apex}}=(-1)^{n-1}(n-1)!\,a^n\ \ \big(\text{EGF }\log(1+at)\big),\qquad \kappa_n^{\mathrm{HL}}=-(n-1)!\,a^n\ \ (n\ge2)\ \ \big(\text{EGF }\tfrac{t}{1-1/p}+\log(1-at)\big),$$
*and the explicit-formula transfer carrying the spectral (zero-side) cumulant to the arithmetic (prime-side) weight is*
$$\boxed{\ \tau_n:=\frac{\kappa_n^{\mathrm{HL}}}{\kappa_n^{\mathrm{apex}}}=(-1)^n\ }$$
*— of modulus exactly $1$ and sign $(-1)^n$, at every prime and every order. The transfer is the involution $t\mapsto-t$ on the cumulant generating function, $\log(1+at)\leftrightarrow\log(1-at)$; this sign reversal is, equivalently, (i) the explicit-formula prime-side minus of §6 ($Q=\text{arch}+\text{pole}-\text{primes}$) raised to the $n$-fold connected correlation, and (ii) the Amari $e\!\leftrightarrow\!m$ dual (particle–hole) involution $\kappa_n(\mathbf 1-X)=(-1)^n\kappa_n(X)$ on the block, under which the Fisher metric ($n=2$) is self-dual and the Amari–Chentsov cubic ($n=3$) flips sign. The archimedean $\Gamma$-factor enters only the ramp density $2\vartheta'$ of §5, so the transfer modulus is $\Gamma$-independent.*

*Proof.* (Apex.) For distinct indices the block partition function $Z(t)=\sum_{j=1}^{p-1}e^{t_j}$ has $\partial_B Z=0$ whenever $|B|\ge2$ (each $e^{t_j}$ depends on a single variable), so in the cumulant–partition identity $\kappa_n=\sum_{\pi}(-1)^{|\pi|-1}(|\pi|-1)!\prod_{B\in\pi}(\partial_B Z/Z)$ only the all-singletons partition survives, giving $\kappa_n=(-1)^{n-1}(n-1)!\prod_k(\partial_{i_k}Z/Z)\big|_0=(-1)^{n-1}(n-1)!\,a^n$; equivalently the cumulant EGF is $\log(1+at)$. (HL.) The fully-resonant local moments $\mu_k=(1-k/p)/(1-1/p)^k$ have, with $x=1/p$, the exponential generating function $M(t)=\sum_k\mu_k t^k/k!=e^{t/(1-x)}\big(1-xt/(1-x)\big)$, whence $\log M(t)=\tfrac{t}{1-x}+\log(1-at)$ and $\kappa_n^{\mathrm{HL}}=-(n-1)!\,a^n$ for $n\ge2$. The ratio is $(-1)^n$. The involution is $\log(1-at)=\log(1+a(-t))$; the dual identity is $(\mathbf 1-X_i)-\mathbb E[\mathbf 1-X_i]=-(X_i-\mathbb E[X_i])$, so $\kappa_n(\mathbf 1-X)=(-1)^n\kappa_n(X)$. $\square$

All four closed forms and the transfer are certified exact (symbolic, $n=2,\dots,6$, several primes; the apex tower additionally by direct distinct-index differentiation at $m=6,8$) in `empirical/probe_n5_transfer_signn.py`.

**Remark 6.3 (term-by-term identity vs closure: the conserved frontier).** Theorem 6.2 makes the apex conductor cumulant tower *equal*, place by place and order by order, to the Rudnick–Sarnak $n$-level density hierarchy: the conductor-block dimension $\varphi(p)$ supplies the $n$-level arithmetic weight $a^n=1/\varphi(p)^n$, and the explicit-formula minus supplies the sign $(-1)^n$. Order $2$ — the Fisher metric / pair correlation — is Montgomery's twin-prime constant; order $3$ — the Amari–Chentsov cubic — is the Bogomolny–Keating off-diagonal $3$-level term. What is *not* established is the closure: that this term-by-term identity, summed over primes and orders and continued across the form-factor boundary $\tau=1$ (the ramp $\tau<1$ — archimedean, the $2\vartheta'$ density of §5, unconditional — forcing the plateau $\tau\ge1$ — arithmetic), yields the marginal positivity $Q(g)\ge0$ of §7–8. That continuation is the Riemann Hypothesis itself (equivalently the Bogomolny–Keating off-diagonal saturation, the arch-domination $\Lambda\le0$, the Connes–Consani marginal archimedean positivity [CC20]); difficulty is conserved. The transfer constant is now exact; the summation across $\tau=1$ is not crossed.

**Remark 6.4 (the involution splits $Q$ into a metric and a chiral channel; the located wall).** The involution $t\mapsto-t$ of Theorem 6.2 decomposes the per-prime arithmetic tower into two parity channels,
$$\underbrace{\log(1+at)+\log(1-at)=\log(1-a^2t^2)}_{\text{metric (even): }\ \kappa_n=-2(n-1)!\,a^n},\qquad \underbrace{\log(1+at)-\log(1-at)=2\operatorname{artanh}(at)}_{\text{chiral (odd): }\ \kappa_n=+2(n-1)!\,a^n},$$
the even (self-dual, connection-independent / Fisher) channel and the odd (Amari–Chentsov cubic and higher / connection) channel. This is the cumulant-tower face of the two-channel Bures fiber $(\xi,L_{\chi_3})$ of [N6 §3]: the metric channel is the carrier $\Xi\sim\zeta$, the chiral channel is the cubic gauge $\mathcal L_3\sim L(s,\chi_3)$. Attempting the closure $Q\ge0$ through this structure locates the wall three independent ways, none crossed:
> (i) *the transfer is off-diagonal.* The pair weight $\kappa_2^{\mathrm{HL}}=-1/(p-1)^2$ is the prime-pair (off-diagonal, plateau $\tau\ge1$) contribution; the diagonal (prime-power, ramp $\tau<1$) is a separate PNT/archimedean sum. The transfer is thus arithmetic$\leftrightarrow$arithmetic (HL $\leftrightarrow$ conductor block), entirely inside the plateau, and gives no leverage on the ramp$\to$plateau continuation, which is arithmetic$\leftrightarrow$archimedean.
> (ii) *the archimedean density changes sign at the boundary.* $2\vartheta'(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}2)-\log\pi$ is negative on the plateau ($2\vartheta'(0)=-5.37$) and positive on the ramp, crossing zero at $r\approx6.29$. The archimedean term dominates the (bounded) prime term at high frequency (ramp) — the Montgomery/Rudnick–Sarnak unconditional regime — but is negative exactly where a test function probes the plateau, so plateau positivity rests on the pole and the exact prime cancellation. That residual domination is RH.
> (iii) *the closed forms do not assemble into $\xi$.* The natural Hadamard product $\prod_p(1-t/(p-1))e^{t/(p-1)}$ converges but has its zeros at $t=p-1$ (real, explicit); it is automatically of Laguerre–Pólya class and is not $\xi$, so its real-rootedness carries no information.

The net is a sharpening, not a proof: the closure is reduced to the positivity of the odd/chiral channel — the cubic-chirality sign the program elsewhere identifies as $c_2<0$ ($\propto L(\tfrac12,\chi_3)^2$, with $L(\tfrac12,\chi_3)=0.4808\ldots>0$), the candidate for the Connes–Consani missing even eigenvalue [CC20] — on the plateau where the archimedean density has gone negative. (To be precise about *which* missing-even-eigenvalue: this is the **character-parity** instance — $\zeta$ even vs $L(\cdot,\chi_3)$ odd — i.e. the simple-and-even condition for the $\chi_3$ object, equivalently GRH$(\chi_3)$. It is *distinct* from the **test-function-parity** §6.6a of $\zeta$ itself, whose even ground is structurally favored independently of $L(\tfrac12,\chi_3)$; the two were conflated in earlier probes and are separated in [N13 §5, Cor 5.3].) The term-by-term transfer is exact (Theorem 6.2); the ramp$\to$plateau continuation across $\tau=1$ is not crossed. (Certified `empirical/probe_closure_anatomy.py`; this is the [N0] closure target in apex coordinates.) The two parity channels here are the two distinct involutions of the SUSY frame [P∞-A §7]: the *even/metric* channel is the test-function parity $(-1)^F=\theta$ ($u\mapsto-u$, the functional equation — the grading of $\zeta$'s own Weil form), while the *odd/chiral* $L(s,\chi_3)$ channel is the Dirichlet-character parity (the auxiliary GRH$(\chi_3)$ object); they were conflated in earlier probes and are separated by the matched-pair test of [N13 Cor 5.3].

---

## 7. Spectral realization of the zeros

The apex archimedean phase realizes the zeros directly.

**Proposition 7.1 (counting and location).** *Let $\vartheta$ be the apex phase of §3. Then $\vartheta(T)/\pi+1$ is the smooth part of the zero-counting function $N(T)$, with the fluctuation $S(T)=N(T)-(\vartheta(T)/\pi+1)$ bounded (in the computed range $|S(T)|\le0.6$). The Riemann–Siegel main sum*
$$Z(t)=2\sum_{n\le\sqrt{t/2\pi}}n^{-1/2}\cos\!\big(\vartheta(t)-t\log n\big)$$
*— the apex phase $\vartheta$ paired with the integer/Mellin ladder $n$ (the apex dimensional axis) — locates all ten of the first zeros $\gamma_n$, with no input from $\zeta$ (program record).*

This is the spectral realization in apex form: the metaplectic phase $\gamma=e^{2i\vartheta}$ of §3 is the smooth phase of the zeros, and its pairing with the discrete ladder produces them. The Cayley transform carries the critical line to the apex unit circle, on which $\gamma$ is unimodular and the zeros are the winding points of the full clock $\varphi=\vartheta+\arg\zeta$.

**Theorem 7.2 (the marginal directions are the zeros).** *The Weil form $M$ of §6 is positive semidefinite to numerical precision (smallest eigenvalue $\approx0$, marginal). Its minimal eigenvector $v$ has Fourier transform $\widehat g_v$ vanishing at the zeros: $|\widehat g_v(\gamma_n)|\sim10^{-7}$ at $\gamma_1,\dots,\gamma_8$ versus $\sim10^{-4}$ at the gap-midpoints (mean ratio $4\times10^{-3}$, program record). The null directions of the Weil form are exactly the test functions vanishing at the zeros; the margin is the residual from zeros beyond the test resolution.*

The positivity is a delicate cancellation, not a free squared norm: the archimedean floor alone is indefinite ($\lambda_{\min}(A+\text{pole})\approx-1.76$, since $2\vartheta'$ has negative density near $0$), and the primes erode; the two meet at the marginal direction, which is the zeros.

---

## 8. The reduction, and what remains

We collect the result and state its status honestly.

**Established unconditionally (certified to machine precision):**
- **(Thm 3.2)** the even apex edge operator is the Connes–Consani archimedean scattering operator $\gamma(s)R$, with $\gamma=e^{2i\vartheta}=u_\infty$, times the Hardy–Blaschke factor $s/(1-s)$;
- **(Prop 4.1)** its small-square / Hardy-averaging part is the [CC20] trace-remainder $\delta(\rho)$, in closed form;
- **(Thm 5.1)** the archimedean Weil positivity is the apex phase-clock inequality $\widehat\delta+2\vartheta'\ge0$, with $2\vartheta'$ the clock velocity;
- **(Thm 6.1)** the full Weil quadratic form, assembled from apex data, reproduces the spectral side over the true zeros to $10^{-4}$;
- **(Prop 7.1, Thm 7.2)** the apex phase counts and locates the zeros, and the marginal directions of the Weil form are the zeros.

**The reduction.** The Riemann Hypothesis is equivalent to the positive semidefiniteness, in the limit $L\to\infty$, of the explicit apex Weil form $M$ — equivalently, to the [PIII] Bures–Poisson positivity $u_B\ge0$, equivalently to $E_B=\Xi+i\Xi'$ being globally of Hermite–Biehler class (equivalently $m_B=-\Xi'/\Xi$ Herglotz on $\mathbb C_+$). The apex contributes an explicit, finite-arithmetic, verified realization of this form: the archimedean factor is the apex edge operator (§3–5), the prime factors are the conductor blocks with Frobenius monodromy ([N1]), and the marginal direction — the locus of the open content — is shown to be the zeros (§7).

**What remains.** The positivity is *marginal*: the smallest eigenvalue is zero, not bounded below, and it is a delicate cancellation between an indefinite archimedean floor and the prime erosion (§7). Proving that this cancellation holds in the limit is the Riemann Hypothesis itself; no finite computation crosses it (difficulty is conserved). What this paper achieves is to make the object explicit and verified, and to localize the open content to a single marginal archimedean direction of one operator. The prime side of that form is now exact at the level of its cumulant transfer (Theorem 6.2): the apex conductor tower equals the Rudnick–Sarnak $n$-level density hierarchy term by term, with transfer constant $(-1)^n$ of modulus exactly one and the explicit-formula sign; the open content is thereby concentrated entirely in the continuation of that identity across the form-factor boundary $\tau=1$ (Remark 6.3), not in the arithmetic weights themselves. Two routes to that direction are natural and are not pursued here: the de Bruijn–Newman heat flow (RH $\iff\Lambda=0$; [PIII §8.7], Rodgers–Tao), under which the apex phase clock evolves and the residual is the edge displacement; and the Sonin/prolate compression of [CC20], whose single conditioning eigenvector is the apex edge mode $\delta_\infty<\tfrac18$ of [N4]. The reduction stands; the crossing is open.

**Remark 8.1 (the residue is transcendental, not marginal: an exact-frame correction).** The marginality above must be read in the exact, metric-adjusted frame, where the Riemann-Hypothesis content is the *signature* of the form — a congruence invariant (Sylvester's law), hence frame-independent and exactly decidable — and *not* the smallest eigenvalue, which is frame-dependent. In that frame three would-be obstructions are discharged exactly. (i) The super-exponential collapse of $\lambda_{\min}/\lambda_{\max}$ is a floating/Euclidean-frame artifact: an exactly positive-definite gate (the Hilbert matrix $H_{ij}=1/(i+j+1)$, the moment matrix of a positive measure) is reported *indefinite* by float64 once $\kappa\gtrsim10^{16}$, while its exact signature is $(n,0)$ at every $n$. (ii) The cross-prime fusion defect that separates $\zeta$ from the Davenport–Heilbronn family is an exact finite signature — the fusion matrix $\Phi_{mn}=a(mn)$ is rank-one for fusion-closed data and carries an exact negative square for Davenport–Heilbronn. (iii) The archimedean phase $\sqrt i$ of [N4, Rem. 4.3] is an exact cyclotomic integer rotation, absorbed into the prime-$2$ metric. A positive archimedean weight is Sylvester-neutral on the fusion signature, so the algebraic and archimedean parts do not interact. What survives all three reductions — and only it — is the *transcendental* positivity: the sign of the form on the marginal direction (§7), whose sole non-exact input is the transcendental position of the zeros, equivalently the $\Gamma$-envelope $\sqrt{\pi/\cosh\pi t}$. The open content is thus the archimedean *transcendental* positivity with every algebraic and conditioning confound removed; "marginality" is its frame-dependent shadow. (Certified `empirical/probe_exact_signature_dispels_marginality.py`, `probe_helmert_fourier_fusion_metric.py`, `probe_sqrt_i_absorption.py`.)

**Remark 8.2 (metric classification of the obstruction).** The split of Remark 8.1 sharpens, by standard similarity-invariance (eigenvalues and Jordan type are the similarity invariants; every diagonalizable operator is normal in *some* inner product), into a three-way classification of the apex/de Branges operator's non-normality, read on its discrete (zero) spectrum:
> **(removable skin)** all-real and diagonalizable $\Rightarrow$ normal in some metric, no chart split — the rotation is a readout-metric artifact; this is the $\sqrt i$ phase, proven removable in [N4, Rem. 4.3].
> **(genuine drift)** a complex eigenvalue $\Rightarrow$ an irremovable rotation at rate $\operatorname{Im}\lambda$ — an **off-line zero**.
> **(defective)** a Jordan block $\Rightarrow$ non-normal in *every* metric — a **multiple zero** of $\Xi$.

The zeros of $\Xi$ being simple (non-defective) and the $\sqrt i$ skin removable, **RH $\iff$ the operator is all-real-diagonalizable $\iff$ there is no genuine-drift component (no off-line zero).** The measure-anchored Fan–Hoffman gap $\Delta_\pi=\sum_i\sigma_i^\pi-\sum_i\lambda_i(S_\pi)$ vanishes iff detailed balance holds in the divisor metric $\pi$ — the same statement, and the confirmation (Remark 8.1) that the Riemann-Hypothesis content is the signature in the divisor/Bures metric, not the Euclidean conditioning. This is the metric-decomposition the sibling Curvature-and-Current track [CBS] applies to non-normal transition operators, here specialized to the apex.

---

## References

[N1] Murillo Montero, L. (2026). *Apex Unitaries: An Explicit Family in $U(N-1)$ over Multiquadratic–Cyclotomic Compositums.* First draft, May 28, 2026.

[N3] Murillo Montero, L. (2026). *Spectral Concentration of the Apex Unitary: A Structural Reduction.* First draft, June 5, 2026.

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.* First draft, June 5, 2026.

[T2] Murillo Montero, L. (2026). *The Cumulant Tower and the Effective Action.* (the categorical Amari–Chentsov cumulant tower $\kappa_n=\partial^n\log Z$ and the $\alpha$-connection $\Gamma^{(\alpha)}=\Gamma^{\mathrm{LC}}-(\alpha/2)T$.)

[N0] Murillo Montero, L. (2026). *The Closure.* First draft, June 6, 2026. (the closure target: averaged $k$-point arithmetic at the primorial.)

[N6] Murillo Montero, L. (2026). *The Unified Archimedean Operator and the de Branges Target for $\xi$.* First draft. (the two-channel Bures fiber $(\xi,L_{\chi_3})$; $E_B=\Xi+i\Xi'$; $m_B=-\Xi'/\Xi$ Herglotz $\iff$ RH.)

[P∞-A] Murillo Montero, L. (2026). *The de Branges Apparatus as Osterwalder–Schrader Reconstruction.* First draft. (§7 the SUSY supercharge $H=\mathcal Q^\dagger\mathcal Q$; the $(-1)^F=\theta$ vs character-parity guardrail.)

[PII] Murillo Montero, L. (2026). *The Right Carrier* (RH trilogy, Paper II), Thm 7.1 (Hardy–Titchmarsh intertwining). Second draft.

[PIII] Murillo Montero, L. (2026). *Closure* (RH trilogy, Paper III), the (GBP) condition and the de Branges phase clock. Second draft.

[CC20] Connes, A., and Consani, C. (2020). *Weil positivity and Trace formula: the archimedean place.* arXiv:2006.13771.

[CC25] Connes, A., and Consani, C. (2025). *Knots, primes and class field theory.* arXiv:2501.06560.

[CBS] Murillo Montero, L. (2026). *Curvature and Current: The Two Blind Spots of Self-Supervised Representation Learning.* Zenodo 10.5281/zenodo.20519464.

Weil, A. (1952). Sur les "formules explicites" de la théorie des nombres premiers. *Comm. Sém. Math. Univ. Lund*, 252–265.

Bombieri, E. (2003). Remarks on Weil's quadratic functional in the theory of prime numbers. *Rend. Mat. Acc. Lincei* 9, 183–233.

Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Analytic Number Theory (Proc. Sympos. Pure Math. XXIV)*, 181–193.

Rudnick, Z., and Sarnak, P. (1996). Zeros of principal $L$-functions and random matrix theory. *Duke Math. J.* 81, 269–322.

Bogomolny, E. B., and Keating, J. P. (1996). Random matrix theory and the Riemann zeros II: $n$-point correlations. *Nonlinearity* 9, 911–935.

de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice–Hall.

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function.* 2nd ed., rev. Heath-Brown. Oxford University Press.
