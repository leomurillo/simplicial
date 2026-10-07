# P∞ — What Is Multiplicative?

## The Intersection Metric and the Lorentzian Geometry of the Arithmetic Apex

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 7, 2026*

<!--
Program record (not part of the paper). Exterior פ-series GEOMETRIC KEYSTONE; the multiplicative
twin of ל-series T0 ("What Is Additive?"). Paired with P0 (P0 = place-completion / Γ / additive-at-∞;
P∞ = metric-completion / Hodge-intersection / multiplicative-at-∞). It does NOT prove RH. Its content:
the multiplicative second-order invariant is the INTERSECTION metric, which is LORENTZIAN (signature
(1,ρ-1)); the additive→multiplicative leap is the never-taken Riemannian→Lorentzian signature flip at
the level of the metric; RH = causality of the arithmetic light cone; the archimedean place is the
timelike direction. Anchoring certificate: empirical/p_infinity/probe_toy_lorentzian_intersection.py
(exact, green); genus generalization + arithmetic-energy-condition probes adjoined (§3, §4). Tiers
[P]/[A]/[C]. Honest: the deepest form is still the F_1 surface over Q = RH; the value is the signature
re-vision (stop building definite forms) + the energy-condition tool + the certificate.
-->

---

> *Additive geometry knows distance; multiplicative geometry knows time; the Gauss sum rotates one into the other.*

---

## Abstract

**Situation.** T0 built the additive apex on $\mathbb Z/N$ and identified its second-order invariant: the Fisher metric of the centered log-ledger — positive-definite, dually flat, the Riemannian heart of the categorical simplex. T8 carried the apex to the multiplicative group $(\mathbb Z/N)^\times$ and its Dirichlet characters; but its second-order structure (T8 Rem 2.8) is the *same* Fisher/cumulant metric with $N\rightsquigarrow\varphi(N)$. T15 completed the additive tower at the real place, producing the $\Gamma$-factor and the smooth primorial $פ$. Across the program the metric has been **additive** — and therefore positive-definite.

**Gap.** The genuinely multiplicative second-order invariant has never been constructed. It is not the Fisher metric. The multiplicative pairing of two classes is their **intersection** (cup product, Weil pairing), and by the Hodge index theorem that pairing is **not** positive-definite: it has signature $(1,\rho-1)$ — it is **Lorentzian**. The program has been measuring the Riemannian shadow of a Lorentzian object; the Tower Theorem (an additive form over $\mathbb Q$ is *definite $\iff$ vacuous*) is precisely the symptom. The additive→multiplicative leap was taken for the *group* and the *characters* (T0$\to$T8) but never for the *metric*.

**Action.** We define the **multiplicative metric** $\langle\cdot,\cdot\rangle_\times$ as the intersection pairing on the Néron–Severi space of the apex correspondence object, develop it as the structural dual of T0's Fisher metric, and prove the **signature flip**: the Gauss-sum / metaplectic duality (T8 §4, T15 §6) carries the Fisher metric (Riemannian, definite) to the intersection metric (Lorentzian, indefinite), and *the change of signature is the entire arithmetic content*. We identify the **archimedean place as the unique timelike (polarization) direction** and the finite primes as the spacelike directions, read the functional equation as the metric's time-reflection isometry and the de Bruijn–Newman constant as its tilt, and pose the **arithmetic energy condition** as the instrument that keeps the light cone causal.

**Result.** The central compression is
$$\boxed{\ \mathrm{RH}\iff \text{the arithmetic apex metric is Lorentzian–causal: the archimedean place timelike, the primes spacelike.}\ }$$
The structure theorems are tier-tagged $[\mathsf P]$ proved/certified, $[\mathsf A]$ structural, $[\mathsf C]$ the calibrated open target: (2) the intersection metric is Lorentzian $[\mathsf P/\mathbb F_q]$; (3) the Fisher–intersection duality is a signature flip $[\mathsf A]$; (4) the archimedean place is the timelike polarization $[\mathsf A]$; (5) RH $\iff$ the primitive cone is causal, with $\Lambda$ its tilt and the functional equation its time-reflection $[\mathsf C]$; (6) the Tower Theorem is the spacelike-blindness of additive forms $[\mathsf P]$; (7) the smooth primorial $פ$ is the scalar shadow of the indefiniteness, $D_3<0$ $[\mathsf P]$; (8) the arithmetic energy condition is the causality instrument, with $W_\lambda=-S^2+\dots$ the scaling d'Alembertian $[\mathsf C]$. All of (2)–(7) are anchored by an exact certificate (§2).

**Harvest.** P∞ supplies the exterior series with its *metric* foundation, as P0 supplied its *place* foundation, and it explains the program's history: the additive line was marginal because it measured the wrong signature. It gives the smooth primorial $פ$ its meaning (the multiplicative-$\Gamma$), specifies the observation platform (the idelic / scaling-momentum frame, where time exists), recasts the de Bruijn–Newman flow as a tilt of an arithmetic Minkowski metric, and opens the arithmetic energy condition as a new instrument distinct from the exhausted heat-flow monotones. It does **not** prove RH: the Lorentzian metric exists over $\mathbb F_q$ (Weil/Deligne) and its construction over $\mathbb Q$ is the $\mathbb F_1$ surface — the single, sharply-localized object toward which the completed apex now stands ready.

**Keywords.** intersection metric, Hodge index, Lorentzian signature, multiplicative metric, Fisher–intersection duality, archimedean polarization, light cone, causality, de Bruijn–Newman tilt, functional equation as time reflection, smooth primorial $פ$, moment obstruction, arithmetic energy condition, scaling d'Alembertian, $\mathbb F_1$ scaling-site square.

---

## 1. Introduction

### 1.1 Two Fourier structures, one metric

The categorical-simplex apex carries two dual Fourier structures. The **additive** one (T0, T7) lives on the labels of $\mathbb Z/N$: its characters are $\chi_c(s)=e^{2\pi ics/N}$, its selection rule is $a_1+\cdots+a_n\equiv c$, and its second-order invariant — the object that measures the local geometry of the centered log-ledger — is the **Fisher information metric**, positive-definite and dually flat. The **multiplicative** one (T8) lives on the units of $(\mathbb Z/N)^\times$: its characters are Dirichlet characters $\psi$, its selection rule is $\chi_1\cdots\chi_n=\psi$ in the dual group, and the two are intertwined by Gauss sums (T8 §4). T8 carried the *objects* across faithfully — the group changed, the characters changed, the convolution changed.

But one thing did not change: the **metric**. T8 Remark 2.8 inherits T0's dually-flat apparatus *verbatim*, with $N\rightsquigarrow\varphi(N)$ — the conjugate potential, the escort entropy, the Cramér rate function, the Fisher metric. The multiplicative apex of T8 is, at second order, *the additive Fisher metric living on the units*. The additive→multiplicative leap was taken for the group, the characters, and the selection rule; it was **never taken for the metric**. That omission is the subject of this paper, and we will argue it is the omission that has kept the whole program on the spacelike sheet of a Lorentzian object.

### 1.2 The multiplicative metric is the intersection form — and it is Lorentzian

What *is* the multiplicative second-order invariant, if not the Fisher metric? The additive second-order pairing of two tangent variations is their *covariance* — an average of a product of values, a positive-definite Gram. The multiplicative second-order pairing of two *classes* is their **intersection** — the cup product $\langle\alpha,\beta\rangle_\times=(\alpha\cdot\beta)$, the Weil pairing, the number of points two correspondences share. This is the genuine multiplicative metric, and it has a property the Fisher metric does not:

> **It is not positive-definite.** On a complete surface the intersection form has, by the Hodge index theorem, signature $(1,\rho-1)$ — one positive direction, the rest negative. It is **Lorentzian.**

This single fact reorganizes the program. The Tower Theorem (an additive moment form over $\mathbb Q$ is *definite $\iff$ vacuous*, contentful $\iff$ indefinite) is no longer a curiosity: it is the statement that the additive/Fisher metric, being positive-definite, lives entirely on the *spacelike sheet* and is therefore blind to the one timelike direction where the arithmetic content sits. Every marginal positivity the program met — the gates collapsing super-exponentially, the $\Lambda=0$ de Bruijn–Newman marginality, the (GBP)-as-identity failure — is the symptom of probing a Lorentzian object with a Riemannian instrument. The leap from additive to multiplicative is, at the level of the metric, the leap from **Riemannian to Lorentzian**: a *signature flip*.

### 1.3 The Einstein dictionary

A Lorentzian metric is the metric of relativity. The dictionary writes itself, and it is the geometric chamber this paper opens.

- The unique $+$ of the signature $(1,\rho-1)$ is the **polarization** (the ample class). We identify it with the **archimedean place** — the one place of $\mathbb Q$ that is qualitatively unlike the others, the place that *completes* (compactifies) $\operatorname{Spec}\mathbb Z$, in Arakelov geometry the point at infinity that makes the arithmetic line a complete curve. The archimedean place is **time**.
- The finite primes are the negative directions: **space**.
- **RH $\iff$ every primitive (functional-equation-odd) class is spacelike** $\iff$ the arithmetic **light cone is causal**, the polarization timelike and everything orthogonal to it negative. Over $\mathbb F_q$ the Cauchy–Schwarz of the cone, $(\Gamma_\infty\!\cdot\!\Delta)^2\le \Gamma_\infty^2\,\Delta^2$, is exactly $|a|\le 2\sqrt q$, the Weil bound.
- The **functional equation $s\leftrightarrow 1-s$** is the metric's time-reflection isometry.
- The **de Bruijn–Newman constant $\Lambda$** is the **tilt** of the metric: $\Lambda=0$ is exactly Minkowski (zeros null, on the critical line); $\Lambda>0$ tilts the cone until a zero leaves the spacelike sheet (goes off-line). Rodgers–Tao proved $\Lambda\ge0$ and the program established that there is no backward (anti-entropy) monotone — which is now not a defect but a **principle**: a light cone cannot be un-tilted by entropy. The deepest negative result of the program becomes the relativistic statement of causality.

This is why completeness was always the missing ingredient. The Hodge index theorem requires a *complete* (proper) surface; over $\mathbb F_q$, $C\times C$ is projective and completeness is free; over $\mathbb Q$, $\operatorname{Spec}\mathbb Z$ is affine and the Hodge index has nothing to descend from until one compactifies — and the compactification data is the archimedean place. The continuum that looks infinite from inside analysis is, from the Arakelov outside, a single compactifying point: *infinite from within, finite from without.*

### 1.4 The anchoring certificate

These are strong claims, so the paper is anchored, before any construction over $\mathbb Q$, by an **exact certificate** that the multiplicative metric is genuinely Lorentzian and that RH-over-$\mathbb F_q$ is genuinely the causality of its light cone. On the surface $S=C\times C$ with basis $\{F_1,F_2,\Delta,\Gamma_F\}$ — the two fibers, the diagonal, and the Frobenius graph — the intersection numbers are classical (Lefschetz gives $\Gamma_F\cdot\Delta=\#C(\mathbb F_q)=q+1-a$), and the full $4\times4$ intersection Gram, evaluated on the *genuine* Frobenius traces of real elliptic curves, has signature $(1,0,3)$ at every prime: **Lorentzian**. Its primitive part is the $2\times2$ form $M=\begin{psmallmatrix}-2q&-a\\-a&-2\end{psmallmatrix}$, negative-definite exactly when $\det=4q-a^2>0$. Read in the signature — a congruence invariant by Sylvester's law, hence exact and frame-independent (§2 computes it from the characteristic polynomial, never from floating-point) — the certificate exhibits the **light-cone flip**: as $|a|$ crosses $2\sqrt q$, the primitive cone passes from spacelike (causal, RH) through null (the Hasse boundary, the critical line) to timelike (acausal, a zero off the line). The same certificate places the additive Fisher metric, signature $(n,0)$ Riemannian, beside it — the signature flip made literal — and recovers the scalar shadow: the primorial Hankel determinant $D_3=-787680<0$, the precise sense in which the multiplicative object admits no additive (moment) representation. §2 records it; §3 extends it to higher genus.

### 1.5 The open object and the energy-condition door

Nothing here proves RH, and the paper is explicit about where the difficulty lives. The Lorentzian-causal metric *exists* over $\mathbb F_q$ because the surface $C\times C$ exists and the Hodge index is a theorem (Weil, Deligne). Over $\mathbb Q$ there is no surface — this is the $\mathbb F_1$ obstruction — and constructing the scaling-site square $\overline{\operatorname{Spec}\mathbb Z}\times_{\mathbb F_1}\overline{\operatorname{Spec}\mathbb Z}$ with a negative-definite primitive intersection form *is* RH. The contribution of P∞ is to name the object as a Lorentzian metric, supply every local ingredient, and — this is the one genuinely new instrument — to identify the *kind of theorem* that keeps such a cone causal. In general relativity, light cones stay causal not because of a monotone but because matter satisfies an **energy condition** — a pointwise positivity on the stress tensor. The program has shown no heat-flow monotone can reach $\Lambda\le0$ (the flow is one-directional). The arithmetic energy condition (§4) is the replacement: a pointwise positivity on the prime correction, viewed as matter against the archimedean metric, that forces the primitive cone spacelike without a backward flow. We make the implication *energy condition $\Rightarrow$ causality $\Rightarrow$ RH-finite* an exact lemma (§4), leaving the energy condition itself — the arithmetic dominant-energy bound $|a|\le 2\sqrt q$ read as "prime energy does not exceed geometric capacity" — as the calibrated open target. (Satellite **P∞-B** takes the next step on the open object: it identifies the operator realizing the Connes–Consani Frobenius correspondences as the archimedean scaling flow, proves the finite compression of the correspondence lattice is order-2 arithmetic-free with *empty positive sector* — so the index certificate cannot live at finite level — and derives the program's cubic route as the order-3 shadow of the same missing index. Satellite **P∞-C** then transports Weil's proof pillar by pillar: geometric positivity at every place is proven with the archimedean intersection kernel in closed form (the trivial-zero ladder), measure expansion is identified as the ample degree via the trace-scaling flow of the $\mathrm{II}_\infty$ core, and the whole of RH is concentrated into the Saturation Conjecture — every numerically positive class is mobile-effective — with a conditional Castelnuovo theorem and a running, falsifiable effectivity-gap instrument.)

### 1.6 What this paper claims, and what it does not

P∞ is a re-vision of the program's geometry, not a proof of RH. Its theorems are the identification of the multiplicative metric with the intersection form and the proof that this metric is Lorentzian (a theorem over $\mathbb F_q$, certified exactly in §2–§3); its frontier is the construction over $\mathbb Q$ and the arithmetic energy condition (§4), each equal in strength to RH. The value of the re-vision is threefold and concrete: it makes a falsifiable structural prediction — *stop building positive-definite forms; the content is in the indefinite, controlled-signature geometry* — which the Tower Theorem now explains rather than merely records; it assigns the smooth primorial $פ$, the idelic observation platform, and the exterior פ-series their precise places; and it names one new instrument, the arithmetic energy condition, absent from every prior route and distinct from the exhausted entropy monotones. Throughout we hold the program's discipline: what is proved over $\mathbb F_q$ is marked $[\mathsf P]$, what is structural is $[\mathsf A]$, and the single open object is marked $[\mathsf C]$ and stated once, sharply, as the geometry toward which the completed apex stands ready.

---

## 2. The toy finite Lorentzian intersection form (anchoring certificate)

*Certificate: `empirical/p_infinity/probe_toy_lorentzian_intersection.py` — exact (sympy $\mathbb Z/\mathbb Q$), signature via characteristic polynomial $+$ Descartes (exact for symmetric matrices, all eigenvalues real), reading the Sylvester-invariant signature, not floating-point conditioning.*

**Setup.** On $S=C\times C$ ($C$ of genus $g$, elliptic $g=1$ for the toy), basis $B=[F_1,F_2,\Delta,\Gamma_F]$ with $F_1=C\times\{pt\}$, $F_2=\{pt\}\times C$, $\Gamma_F=$ graph of Frobenius. The exact intersection numbers are
$$F_1^2=F_2^2=0,\quad F_1\!\cdot\!F_2=1,\quad \Delta^2=2-2g,\quad \Delta\!\cdot\!F_1=\Delta\!\cdot\!F_2=1,$$
$$\Gamma_F\!\cdot\!F_1=q,\quad \Gamma_F\!\cdot\!F_2=1,\quad \Gamma_F\!\cdot\!\Delta=\#C(\mathbb F_q)=q+1-a\ \text{(Lefschetz = explicit formula)},\quad \Gamma_F^2=q(2-2g).$$
The primitive classes (orthogonal to the hyperbolic plane $\langle F_1,F_2\rangle$) are $\Delta_0=\Delta-F_1-F_2$ and $\Gamma_0=\Gamma_F-F_1-qF_2$, with primitive Gram, for $g=1$,
$$M=\begin{pmatrix}\Gamma_0^2 & \Gamma_0\!\cdot\!\Delta_0\\ \Gamma_0\!\cdot\!\Delta_0 & \Delta_0^2\end{pmatrix}=\begin{pmatrix}-2q & -a\\ -a & -2\end{pmatrix},\qquad \det M=4q-a^2.$$

**Lemma 2.0 (intersection numbers).** *The numbers above hold.*

*Proof.* $F_1,F_2$ are fibers of the two projections $S=C\times C\to C$; a fiber moves in a base-point-free pencil, so $F_1^2=F_2^2=0$, and a horizontal and a vertical fiber meet transversally in one point, $F_1\!\cdot\!F_2=1$. The diagonal $\Delta\cong C$ meets $C\times\{pt\}$ in the single point $(pt,pt)$, so $\Delta\!\cdot\!F_1=\Delta\!\cdot\!F_2=1$. The canonical of a product is $K_S=p_1^*K_C+p_2^*K_C=(2g-2)(F_1+F_2)$; adjunction $D^2=2p_a(D)-2-D\!\cdot\!K_S$ applied to $\Delta\cong C$ (so $p_a=g$) gives $\Delta^2=2g-2-(2g-2)(\Delta\!\cdot\!F_1+\Delta\!\cdot\!F_2)=(2g-2)(1-2)=2-2g$. For the Frobenius graph $\Gamma_F=\{(x,F x)\}$: meeting $C\times\{pt\}$ forces $Fx=pt$, which has $\deg F=q$ solutions, so $\Gamma_F\!\cdot\!F_1=q$; meeting $\{pt\}\times C$ forces $x=pt$, one point, $\Gamma_F\!\cdot\!F_2=1$. Adjunction on $\Gamma_F\cong C$ gives $\Gamma_F^2=2g-2-(2g-2)(q+1)=q(2-2g)$. Finally $\Gamma_F\!\cdot\!\Delta=\#\{x:Fx=x\}=\#C(\mathbb F_q)$, and the Lefschetz fixed-point formula on $C$,
$$\#\mathrm{Fix}(F)=\sum_i(-1)^i\operatorname{tr}(F\mid H^i_{\mathrm{\acute et}}(C))=\underbrace{1}_{H^0}-\underbrace{a}_{H^1}+\underbrace{q}_{H^2}=q+1-a,$$
is the explicit formula in geometric form, with $a=\operatorname{tr}(F\mid H^1)=\sum_{i=1}^{2g}\alpha_i$ the Frobenius trace. $\square$

**Theorem 2.1 (the metric is Lorentzian).** *The intersection form on $\langle F_1,F_2,\Delta,\Gamma_F\rangle$ has signature $(1,\rho-1)$; for the certified curves $\rho=4$, signature $(1,0,3)$.*

*Proof.* By the Hodge index theorem (Weil 1948 for $C\times C$; in general Grothendieck), the intersection form on $\mathrm{NS}(S)_{\mathbb R}$ has signature $(1,\rho-1)$: it is **Lorentzian**, with the single positive direction realized by any ample class. The plane $H=\langle F_1,F_2\rangle$ has Gram $\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ (eigenvalues $\pm1$), signature $(1,1)$; the ample class $F_1+F_2$ satisfies $(F_1+F_2)^2=2>0$ and is the positive direction. Decompose $\langle F_1,F_2,\Delta,\Gamma_F\rangle=H\perp H^\perp$ with $H^\perp=\langle\Delta_0,\Gamma_0\rangle$, $\Delta_0=\Delta-F_1-F_2$, $\Gamma_0=\Gamma_F-F_1-qF_2$ (one checks $\Delta_0\!\cdot\!F_i=\Gamma_0\!\cdot\!F_i=0$ directly from Lemma 2.0). The Hodge index forces $H^\perp$ negative-definite, so the signature is $(1,1)\perp(0,2)=(1,3)$. The certificate evaluates this exactly on $E:y^2=x^3+x+1/\mathbb F_p$ ($p=11,\dots,41$) with the genuine point-counted trace $a_p$, reading the Sylvester-invariant signature from the characteristic polynomial: $(1,0,3)$ at every prime. $\square$

**Theorem 2.2 (the light cone is RH over $\mathbb F_q$).** *In the basis $\{\Gamma_0,\Delta_0\}$ the primitive Gram is $M=\begin{psmallmatrix}-2gq&-a\\-a&-2g\end{psmallmatrix}$ (for $g=1$, $\begin{psmallmatrix}-2q&-a\\-a&-2\end{psmallmatrix}$), and*
$$M\ \text{negative-definite}\iff \det M=4g^2q-a^2>0\iff |a|<2g\sqrt q,$$
*which for $g=1$ is the Hasse bound and is RH for $E$. The certificate exhibits the exact signature flip: spacelike (causal, RH) $\to$ null (the Hasse boundary $=$ the critical line) $\to$ a timelike primitive class (a zero off the line).*

*Proof.* The entries are computed in Lemma 2.0: e.g. $\Gamma_0^2=\Gamma_F^2-2\Gamma_F\!\cdot\!F_1-2q\,\Gamma_F\!\cdot\!F_2+2q\,F_1\!\cdot\!F_2=q(2-2g)-2q-2q+2q=-2gq$, and $\Gamma_0\!\cdot\!\Delta_0=(q+1-a)-q-1-1+1-q+q=-a$. By Sylvester's criterion a symmetric $2\times2$ form is negative-definite iff its leading principal minors are $m_1<0$ and $m_2>0$; here $m_1=-2gq<0$ always and $m_2=\det M=4g^2q-a^2$, giving the stated equivalence. The Hodge index (Theorem 2.1) is exactly the assertion that this negative-definiteness holds, i.e. $|a|\le 2g\sqrt q$ — the Weil bound; for $g=1$ this is RH for $E$. At $\det M=0$ ($|a|=2g\sqrt q$) the form is negative-semidefinite with a null primitive vector; for $\det M<0$ it is indefinite, a primitive class becomes positive (timelike) and the full Gram signature flips $(1,3)\to(2,2)$ — an eigenvalue off $|\cdot|=\sqrt q$, a zero off the line. $\square$

The certificate confirms each regime exactly across $q=7,9,25$.

**Theorem 2.3 (the signature flip).** *The additive Fisher metric is Riemannian (signature $(n,0)$); the multiplicative intersection metric is Lorentzian (signature $(1,n-1)$). Same order, opposite signature.*

*Proof.* The Fisher metric of a strictly positive ledger $\rho$ is $\operatorname{diag}(1/\rho_i)$ (T0): diagonal with strictly positive entries, hence positive-definite, signature $(n,0)$ — Riemannian. The intersection metric is Lorentzian by Theorem 2.1. The Gauss-sum/metaplectic transform (T8 §4, T15 §6) intertwines the two sectors; the invariant that distinguishes them is the signature, and it differs by $n-2$ negative directions. $\square$

**Proposition 2.4 (unique timelike direction).** *$(F_1+F_2)^2=+2>0$ is the unique (up to scale and the cone) timelike direction; $\Gamma_0^2=-2gq<0$ and $\Delta_0^2=-2g<0$ are spacelike.*

*Proof.* By Theorem 2.1 the form has exactly one positive direction (signature $(1,\rho-1)$); $F_1+F_2$ realizes it. The primitive generators are spacelike by Theorem 2.2. The timelike direction is the polarization; over $\mathbb Q$, where the surface and its ample cone are not available, this single positive direction must be supplied at the one place that compactifies $\operatorname{Spec}\mathbb Z$ — the archimedean place. $\square$

**Proposition 2.5 (scalar shadow).** *The primorial $(P_n)=1,2,6,30,\dots$ is not a Hamburger moment sequence: its Hankel determinants are $D_0=1,D_1=2,D_2=24,D_3=-787680<0$. Hence no positive measure $\mu$ has $P_n=\int t^n\,d\mu$.*

*Proof.* Hamburger's theorem: $(P_n)$ is the moment sequence of a positive measure iff every Hankel determinant $D_n=\det[P_{i+j}]_{0\le i,j\le n}\ge0$. The certificate computes $D_3=-787680<0$ exactly, so the criterion fails. Consequently $פ$ admits no Mellin/measure (additive) representation; the factorial does ($n!=\int_0^\infty t^ne^{-t}dt$, whence $\Gamma$), but the primorial does not — the scalar witness of the indefiniteness Theorems 2.1–2.2 exhibit geometrically. $\square$

---

## 3. Higher genus: the Lorentzian structure persists

*Certificate: `empirical/p_infinity/probe_genus_lorentzian.py` — exact.*

The toy is not an elliptic accident. The intersection numbers carry an explicit genus parameter ($\Delta^2=2-2g$, $\Gamma_F^2=q(2-2g)$, $K_S=(2g-2)(F_1+F_2)$), and the primitive classes $\Delta_0=\Delta-F_1-F_2$, $\Gamma_0=\Gamma_F-F_1-qF_2$ give a primitive Gram that generalizes cleanly.

**Theorem 3.1 (Lorentzian at every genus).** *For genus $g$,*
$$M_g=\begin{pmatrix}-2gq & -a\\ -a & -2g\end{pmatrix},\qquad \det M_g=4g^2q-a^2,$$
*and the full $4\times4$ intersection Gram has signature $(1,0,3)$ — Lorentzian — at every genus. The primitive Gram is negative-definite $\iff|a|<2g\sqrt q$, the genus-$g$ Weil **trace** bound (the generalization of Hasse). Certified on the real genus-2 curve $C:y^2=x^5+x+1$ over $\mathbb F_p$ ($p=7,\dots,23$): the genuine trace $a_1$ satisfies $|a_1|\le 4\sqrt p$, $M_2$ is negative-definite, and the Gram is $(1,0,3)$ at every prime.* $\mathsf{[P]}$

*Proof.* Lemma 2.0 holds for every $g$; in particular $\Gamma_0^2=q(2-2g)-2q=-2gq$, $\Delta_0^2=(2-2g)-2=-2g$, $\Gamma_0\!\cdot\!\Delta_0=-a$ (the $g$-dependence cancels exactly as in Theorem 2.2), giving $M_g$ and $\det M_g=4g^2q-a^2$. The Hodge index (Theorem 2.1, valid for any genus) makes the form Lorentzian $(1,\rho-1)$ and forces $M_g\prec0$; Sylvester gives $M_g\prec0\iff\det M_g>0\iff|a|<2g\sqrt q$. The trace is $a=\sum_{i=1}^{2g}\alpha_i$, so under RH ($|\alpha_i|=\sqrt q$) the bound $|a|\le 2g\sqrt q$ is the triangle inequality — the genus-$g$ Hasse–Weil trace bound. The genus-2 curve is verified by point count. $\square$

The $4$-dimensional toy captures only the **first** eigenvalue moment $a=a_1$ — the trace. Full RH for genus $g$ asserts each of the $2g$ Frobenius eigenvalues lies on $|\cdot|=\sqrt q$, which is the next theorem.

**Theorem 3.2 (full RH = a positive Toeplitz form).** *Let $\alpha_1,\dots,\alpha_{2g}$ be the Frobenius eigenvalues, $\alpha_i=\sqrt q\,z_i$, with normalized power sums $t_k=\sum_i z_i^k=a_k/q^{k/2}$ ($a_k=\sum\alpha_i^k$, recoverable from point counts over $\mathbb F_{q^k}$). The $t_k$ are the trigonometric moments of the eigenvalue measure $\sum_i\delta_{z_i}$, so by the Herglotz–Bochner theorem the Frobenius-power Toeplitz form $\big[t_{|j-k|}\big]$ is positive semi-definite $\iff$ all $|z_i|=1\iff$ all $|\alpha_i|=\sqrt q\iff$ full RH over $\mathbb F_q$.* Certified exactly: on the circle (e.g. $z\in\{i,-i,1,-1\}$) the moments are $(4,0,0,0,4,\dots)$ and the Toeplitz form is PSD (signature $(4,3,0)$, no negative eigenvalue); replacing one conjugate pair by an off-circle reciprocal pair $\{2,\tfrac12\}$ makes the moments grow geometrically $(4,\tfrac52,\tfrac94,\tfrac{65}8,\dots)$ and the form acquires a negative eigenvalue (signature $(3,3,1)$) — RH violated. $\mathsf{[P]}$

*Proof.* ($\Leftarrow$) If $|z_i|=1$ write $z_i=e^{i\theta_i}$; then $t_k=\int e^{ik\theta}\,d\mu(\theta)$ for the positive measure $\mu=\sum_i\delta_{\theta_i}$, and for any $c_0,\dots,c_m$,
$$\sum_{j,k}c_j\bar c_k\,t_{j-k}=\int\Big|\sum_j c_j e^{ij\theta}\Big|^2 d\mu(\theta)\ge0,$$
so the Toeplitz form is PSD (Herglotz). ($\Rightarrow$) If the Toeplitz forms are PSD at every size, then by the Herglotz/Bochner theorem for $\mathbb Z$ the $t_k$ are the Fourier coefficients of a positive measure on the circle, hence bounded: $|t_k|\le t_0$ for all $k$. But the functional equation pairs $\alpha_i\leftrightarrow q/\alpha_i$, i.e. $z_i\leftrightarrow 1/\bar z_i$; if some $|z_i|=r>1$ then $t_k=\sum_i z_i^k$ grows like $r^k\to\infty$ (the maximal-modulus terms cannot cancel, being a strict majorant), contradicting boundedness — and indeed the certificate's off-circle case produces a negative eigenvalue at finite size. Hence all $|z_i|\le1$; the pairing $z\leftrightarrow1/\bar z$ then forces $|z_i|=1$ for all $i$, i.e. $|\alpha_i|=\sqrt q$ — full RH. $\square$

The toy Lorentzian form (Theorem 3.1, the **trace** face) and the Frobenius-power Toeplitz form (Theorem 3.2, the **full-spectrum** face) are the two exact faces of the same statement; both have the identical $\mathbb Q$-side obstruction — the $\mathbb F_1$ surface / arch-domination — and over $\mathbb Q$ the Toeplitz form is precisely the Bures/Nevanlinna circle-Toeplitz of the zeta zeros.

---

## 4. The arithmetic energy condition

*Certificate: `empirical/p_infinity/probe_arithmetic_energy_condition.py` — exact.*

In general relativity a light cone stays causal not because of a monotone but because matter satisfies a pointwise **energy condition** — a local positivity on the stress tensor — and a global focusing theorem (Raychaudhuri / Hawking–Penrose) turns that local positivity into the causal conclusion. The program has shown that no heat-flow monotone can reach $\Lambda\le0$ (the de Bruijn–Newman flow is one-directional; Rodgers–Tao give only $\Lambda\ge0$, and no backward/anti-entropy monotone exists). The energy condition is the structurally correct replacement: a positivity, not a monotone.

**The split.** Only the Lefschetz entry $\Gamma_F\!\cdot\!\Delta=q+1-a$ depends on the arithmetic; the intersection Gram splits as
$$G(q,a)=\underbrace{G(q,0)}_{\text{archimedean background }g}-\;a\,E,\qquad E=e_\Delta e_{\Gamma_F}^{\!\top}+e_{\Gamma_F}e_\Delta^{\!\top},$$
the prime flux $a$ entering linearly as the "matter" coupled through the stress direction $E$ (verified $G(q,a)=g-aE$ exactly).

**Lemma 4.1 (energy condition $\Rightarrow$ causality — exact, non-circular).** *On the Lorentzian background $g$, the dominant-energy bound $|a|\le 2\sqrt q$ holds $\iff$ the primitive Gram $M$ is negative-(semi)definite $\iff$ the primitive cone is spacelike (causal) $\iff$ RH-over-$\mathbb F_q$-finite. The prime flux $a$ is the matter; $2\sqrt q$ is the geometric "speed-of-light" capacity. ($n$-dimensional generalization: the bound is the spectral-radius-$<1$ condition on $g^{-1}T$ restricted to the spacelike sheet.)* This is the arithmetic Raychaudhuri/focusing step, the non-circular half. $\mathsf{[P]}$

*Proof.* On the primitive plane the background ($a=0$) Gram is $M(0)=\operatorname{diag}(-2q,-2)\prec0$ (spacelike), and the stress adds the off-diagonal $-a\,e$ ($e=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$): $M=M(0)-a\,e=\begin{psmallmatrix}-2q&-a\\-a&-2\end{psmallmatrix}$. By Sylvester, $M\prec0\iff -2q<0$ (automatic) and $\det M=4q-a^2>0$, i.e. $|a|<2\sqrt q$; equality is the semidefinite (null) boundary. For the general statement, let $V_s$ be the spacelike sheet ($g\!\restriction_{V_s}\prec0$) and define the $g$-self-adjoint stress operator $A$ on $V_s$ by $g(Av,w)=T(v,w)$. Then $(g+T)(v,v)=g((I+A)v,v)$, which is $<0$ for all $v\in V_s\setminus\{0\}$ iff every eigenvalue of $A$ is $<1$ — the dominant-energy condition $T(v,v)\le|g(v,v)|$ on spacelike $v$. Thus the energy bound is exactly the preservation of the spacelike (causal) sheet; over $\mathbb F_q$ this preservation is the content of the Hodge index (Theorem 2.1), and for $g=1$ it is RH for $E$. The implication is pure inertia (Sylvester/Weyl) — no analytic input on the zeros, hence non-circular. $\square$

**Proposition 4.2 (the energy condition is two-faced, and geometric over $\mathbb F_q$).** *The same bound is the negative-definiteness of the $C\times C$ primitive intersection form $M=\begin{psmallmatrix}-2q&-a\\-a&-2\end{psmallmatrix}$ and the positive-definiteness of the Rosati/Weil endomorphism form $R=\begin{psmallmatrix}2&a\\a&2q\end{psmallmatrix}$; both flip at exactly $|a|=2\sqrt q$ ($\det=4q-a^2=0$). Over $\mathbb F_q$ this is the Hodge/Rosati positivity on a genuine surface — the **geometric energy condition**, a theorem.* Certified across $(q,a)$ with $q=7,9,25$. $\mathsf{[P]/\mathbb F_q}$

*Proof.* With $S=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$, $S(-M)S=S\begin{psmallmatrix}2q&a\\a&2\end{psmallmatrix}S=\begin{psmallmatrix}2&a\\a&2q\end{psmallmatrix}=R$, so $R$ is congruent to $-M$; by Sylvester's law of inertia $R\succ0\iff -M\succ0\iff M\prec0$, and both equal $\det=4q-a^2>0$. The two faces are the intersection form on $\mathrm{NS}(C\times C)$ and the Rosati trace form on $\operatorname{End}^0(\mathrm{Jac}\,C)=\langle1,F\rangle$ — the latter positive-definite by the Rosati involution's positivity (Weil), which forces $|a|\le2\sqrt q$. Over $\mathbb F_q$ this positivity is a theorem (a genuine polarized abelian variety exists); it is the geometric energy condition supplied for free by the surface. $\square$

**The operator d'Alembertian.** The Connes–Consani–Moscovici operator $W_\lambda=-S^2+2\pi\lambda^2(4N+1)-\tfrac14$ is, read this way, a **wave operator plus confining potential**: $S$ is the self-adjoint dilation generator (scaling-*time* momentum), so $-S^2=\Box_t$ is the d'Alembertian of scaling-time (Lorentzian symbol, one time sign), and $V=2\pi\lambda^2(4N+1)\ge0$ is the confinement that cures the $xp$ continuous-spectrum disease. The polarization "$W_\lambda\ge0$" — RH-equivalent if merely asserted — is the statement that $\Box_t+V$ has no negative mode *given the arithmetic source* (the prime/von Mangoldt term). For a wave equation $\Box\phi=J$, positivity of the energy follows from an energy condition on the source $J$ (reflection positivity / unitarity), not from a flow.

**The new target $\mathsf{[C]}$.** Derive $W_\lambda\ge0$ from an **arithmetic null/dominant energy condition** on the prime source — the statement that the prime flux satisfies $|a|\le2\sqrt q$ at every scale (= arch-domination), proved via the reflection-positivity / unitarity of the underlying scaling field theory, the arithmetic analog of the Rosati positivity that is a theorem over $\mathbb F_q$. This is a new toolbox — pointwise positivity of an arithmetic stress tensor — distinct from the exhausted heat-flow monotones, and it is the precise sense in which $\mathbb F_q$'s "geometry supplies the energy condition for free" must be manufactured at the archimedean place over $\mathbb Q$.

**The genuine lever: the arithmetic Hodge index theorem, and its exact limit.** A natural and correct instinct is that the Lorentzian metric need not wait for the literal $\mathbb F_1$ surface, because **Arakelov geometry already supplies a complete arithmetic surface and a proven arithmetic Hodge index theorem** — the **Faltings–Hriljac theorem** [FH], in its modern strengthenings (Moriwaki [Mo]; Yuan–Zhang [YZ] over $\overline{\mathbb Q}$; Carney [Ca] over function fields). On a regular arithmetic surface $\mathcal X\to\operatorname{Spec}\mathcal O_K$ the Arakelov intersection pairing on numerically-trivial metrized line bundles is **negative semi-definite**, with kernel exactly the constant (trace) part, and on the primitive complement it is **negative-definite and equals $-\langle\cdot,\cdot\rangle_{\mathrm{NT}}$, the negative of the Néron–Tate height pairing on $\mathrm{Jac}(\mathcal X)$**. The signature is precisely $(1,\rho-1)$: the archimedean Green's-function data supplies the single timelike polarization, the fibral and horizontal classes the spacelike directions. *This is exactly the geometry P∞ predicts, proved unconditionally over $\mathbb Q$* — the strongest external corroboration of the signature re-vision (§1.2, Thm 2.3): the Lorentzian intersection metric is not an $\mathbb F_q$ artifact, a genuine $\mathbb Q$-side arithmetic Hodge index theorem of the same signature, with the archimedean place timelike, exists. $\mathsf{[P]}$

*But it is on the wrong surface, and the gap is exact.* The Faltings–Hriljac surface is a model of a **curve** $C/\mathbb Q$ fibered over $\operatorname{Spec}\mathbb Z$: one **geometric** dimension over one **arithmetic** dimension ($\operatorname{Spec}\mathbb Z$ as base). The negative directions it certifies are spanned by **Néron–Tate height classes** — $\mathrm{Jac}(C)(\overline{\mathbb Q})\otimes\mathbb R$ — and the zeros of the $L$-function are **nowhere among them**: they are not classes in $\mathrm{NS}$ or $\widehat{\mathrm{Pic}}^{\tau}$ of any such surface. The decisive tell is that **Faltings–Hriljac is unconditional**: if its negative-definiteness carried RH-content for the $L$-function of the generic fiber, it would already prove RH for every elliptic-curve $L$-function $L(E,s)$ — which it does not. It delivers *height positivity*, a genuinely different and strictly weaker statement than the *spectral positivity* RH requires. $\mathsf{[P]}$

The object RH needs is the **self-product** $\overline{\operatorname{Spec}\mathbb Z}\times_{\mathbb F_1}\overline{\operatorname{Spec}\mathbb Z}$: **two arithmetic directions, no geometric one**, with $\mathbb F_1$ the field of constants below — the surface on which the diagonal-against-Frobenius-graph count $\Gamma_F\!\cdot\!\Delta=\#\mathrm{Fix}$ of §2 becomes the explicit formula for $\zeta$. Faltings–Hriljac lives on a curve *over* $\operatorname{Spec}\mathbb Z$; the $\zeta$-surface is $\operatorname{Spec}\mathbb Z$ *as* the curve. The arithmetic Hodge index theorem on the first does not transfer to the second; the missing $\mathbb F_1$ base (= N7's single object) is exactly the missing second factor. The Connes–Consani scaling site and "Jacobian of $\overline{\operatorname{Spec}\mathbb Z}$" [CC, 2602.15941] are precisely the live construction of Faltings–Hriljac/Néron–Tate theory *for this missing object* — and there the analog of the Hodge-index positivity is **not** descended from [FH]: it is the Weil positivity, equal in strength to RH. The scaling site supplies the right geometric home but not a free positivity, because it is not a projective arithmetic surface.

*Net effect on the ledger.* The lever does **not** promote the RH-over-$\mathbb Q$ target out of $\mathsf{[C]}$: the arithmetic Hodge index / energy condition on the $\zeta$-surface remains exactly as open as before. What it *does* promote is the **confidence and precision of the framing**: (i) the signature flip (§2.3) and deposit (i) of §6 are upgraded from "$\mathbb F_q$ theorem $+$ analogy" to "$\mathbb F_q$ theorem $+$ an unconditional $\mathbb Q$-side arithmetic Hodge index theorem of identical signature"; (ii) the $\mathbb F_1$ obstruction is sharpened from "no Hodge index theorem over $\mathbb Q$" to the exact "the Hodge index theorem over $\mathbb Q$ exists and is unconditional, but on a curve over $\operatorname{Spec}\mathbb Z$ — giving Néron–Tate — not on $\operatorname{Spec}\mathbb Z$ over $\mathbb F_1$, which would give $\zeta$." In this light the arithmetic energy condition (Lemma 4.1) is the demand that the *Néron–Tate-type* negative-definiteness of Faltings–Hriljac be manufactured for the self-product at the archimedean place, with the **prime flux** — not a Mordell–Weil class — as the matter. $\mathsf{[C]}$

---

## 5. The energy condition as reflection positivity (Osterwalder–Schrader)

*Certificate: `empirical/p_infinity/probe_reflection_positivity.py` — exact.*

The energy condition of §4 has a precise home in constructive quantum field theory: the bridge from a Euclidean (statistical) theory to a Lorentzian (unitary, positive-energy) one is **reflection positivity** (Osterwalder–Schrader, OS). We make the identification, then — with the literature's discipline — separate what is a relabeling from what is a genuine importable tool.

### 5.1 The dictionary

| Euclidean QFT | arithmetic |
|---|---|
| Euclidean time | the scaling/log variable $u$ (the dilation flow's time on $\mathbb R^\times_+$) |
| time reflection $\theta$ | the functional equation $s\leftrightarrow1-s$ ($=$ Frobenius$\leftrightarrow$Verschiebung $F\leftrightarrow F^\vee=q/F$, the Rosati involution; the metric's time-reflection isometry, §1.3) |
| two-point function | the Weil explicit-formula / apex intersection kernel |
| positive-time half-space | test functions supported in $u>0$ (the prime side, $\operatorname{Re}s>\tfrac12$) |
| OS reflection pairing | $\langle\theta f,f\rangle=$ the Weil quadratic form $W(f)$ |

### 5.2 RH is reflection positivity — and what that does and does not buy

In this dictionary, Weil's criterion ($W(f)\ge0\ \forall f\iff\mathrm{RH}$) is exactly the OS reflection-positivity axiom $\langle\theta f,f\rangle\ge0$ for $f$ supported in positive time:
$$\mathrm{RH}\iff\text{the arithmetic explicit-formula theory is reflection-positive.}$$
**Honest calibration.** At the level of the *statement* this is a relabeling: the OS axiom one must verify *is* Weil positivity, which *is* RH — no free lunch from the renaming. The closest classical antecedent is Burnol's positive-type / convolution-square reading of the explicit formula [Bu]; the live Connes–Consani program realizes the same positivity through Sonin/prolate compression and does **not** use OS or Lorentzian language [CC], so the OS synthesis here is *unclaimed* but is not, by itself, new leverage. The value lies entirely in §5.3.

### 5.3 The genuine content: Herglotz $\iff$ OS $\iff$ positive-energy semigroup

What is rigorous, and what makes the framing more than cosmetic, is the **Neeb–Ólafsson reflection-positivity theory** [NÓ]: a function is reflection-positive iff it is a Laplace transform $\int e^{-\lambda|t|}\,d\mu(\lambda)$ of a positive measure (Bernstein–Widder), and OS reconstruction then yields a Hilbert space, a contractive **positive-energy** semigroup $e^{-tH}$ ($H\ge0$), and a unitary Lorentzian one-parameter group by analytic continuation (Lax–Phillips dilation). The key fact is that this is the *same analytic object* as **Herglotz/Nevanlinna positivity**:
$$m_B=-\Xi'/\Xi\ \text{Herglotz}\iff m_B\ \text{is an OS two-point function}\iff H\ge0\ (\text{positive energy}).$$
Hence the program's two sides are the two ends of one OS reconstruction, on real theorems rather than analogy:
- **Euclidean side** — the Weil form / explicit formula / Connes scaling site (the reflection-positive kernel);
- **Lorentzian side** — its OS reconstruction: the de Branges space of $E_B=\Xi+i\Xi'$ (Hermite–Biehler $=$ the Hardy/positive-energy half), the generator $W_\lambda=-S^2+V$ of §4 (the scaling one-parameter group, $S$ the dilation generator $=$ the timelike direction), $\operatorname{spec}(H)=$ the zeros, and $H\ge0$ $=$ zeros real $=$ RH.

This identification — *the de Branges/Herglotz RH apparatus is the OS-reconstructed Lorentzian theory of the reflection-positive explicit-formula system* — is, to the extent the literature shows, **unclaimed**, and it rests on independent theorems: Herglotz/Pick representation, Bernstein–Widder, Neeb–Ólafsson, Lax–Phillips, and de Branges $\Leftrightarrow$ canonical systems [Ro].

### 5.4 The certified template

**Theorem 5.1 (reflection positivity $=$ RH over $\mathbb F_q$).** *For the Frobenius transfer $F$ (one scaling step), the OS reflection form on $\mathbb Z[F]=\langle1,F,\dots,F^n\rangle$,*
$$H[j,k]=\operatorname{Tr}\!\big(F^j(F^\vee)^k\big)=\alpha^j\beta^k+\beta^j\alpha^k,\qquad\beta=F^\vee=q/\alpha,$$
*is positive semi-definite $\iff\beta=\bar\alpha\iff|\alpha|=\sqrt q\iff$ RH over $\mathbb F_q$.*

*Proof.* $H$ is the reflected pairing $\langle\theta F^k,F^j\rangle$ for $\theta=$ Rosati involution ($F\mapsto F^\vee$). If $|\alpha|=\sqrt q$ then $\beta=\bar\alpha$ and $H[j,k]=2\operatorname{Re}(\alpha^j\bar\alpha^k)=2(v_R v_R^\top+v_I v_I^\top)[j,k]$ with $v_j=\alpha^j$, a sum of two rank-one PSD matrices, hence PSD. If $\alpha,\beta$ are real and distinct (off circle) then $H=v\,w^\top+w\,v^\top$ ($v_j=\alpha^j,w_j=\beta^j$), rank two with one positive and one negative eigenvalue on $\langle v,w\rangle$ — indefinite. $\square$ Certified exactly: on-circle ($q=4,5$) signature $(2,4,0)$ PSD; off-circle signature $(1,4,1)$, one negative eigenvalue. Over $\mathbb F_q$ this PSD is the Rosati positivity (a theorem) — reflection positivity holds for free because the surface exists. This $H$ is the reflection-positive form of the Frobenius-power Toeplitz of §3.2, with the reflection $\theta$ now explicit.

### 5.5 What reflection positivity imports — and what it does not

Honest separation, following the constructive-QFT literature.

- **Importable and load-bearing** (the Q3 machinery): the Herglotz/Pick $\iff$ OS $\iff$ positive-energy-semigroup equivalence [NÓ], Lax–Phillips scattering as the unitary continuation, and reflection-positive *one-parameter group* structure matched to the **scaling group** — exactly where $W_\lambda=-S^2+V$ becomes literal. These convert "the arithmetic light cone is causal" into "the reconstructed scaling semigroup is positive-energy," a checkable analytic statement about $m_B$.
- **Not importable** (be skeptical): Gaussian domination, chessboard estimates, infrared bounds, correlation inequalities — the heavy artillery that *proves* positivity — require a genuine **local lattice action with a positive Boltzmann weight** and a reflection across a hyperplane of sites. The explicit formula / prolate operator has **no known such local lattice realization**, and the literature contains no positive transfer object whose OS reconstruction forces the zeros onto the line. Constructing one would itself be the hard theorem.

**The target $\mathsf{[C]}$.** Realize the explicit-formula theory as OS-reconstructable with a *positive* scaling transfer — equivalently, prove $m_B$ Herglotz uniformly $=$ arch-domination $=$ RH — using the reflection-positive scaling-semigroup structure (Neeb–Ólafsson) rather than a monotone. Over $\mathbb F_q$ the transfer (Frobenius) is positive for free (Theorem 5.1); over $\mathbb Q$ the positivity must be manufactured at the archimedean place — the OS reflection axis. This is the precise, literature-grounded form of the arithmetic energy condition: not a new positivity (it is RH), but a new *route to* it through the Herglotz/OS/semigroup machinery, distinct from the exhausted heat-flow monotones and honest about the absence of a ready lattice toolbox.

---

## 6. Honest status

P∞ does **not** prove the Riemann Hypothesis. What it proves, exactly and over $\mathbb F_q$, with full proofs in §§2–5 and exact certificates: the multiplicative metric is the intersection form, and this form is Lorentzian with RH realized as the causality of its light cone (§2–§3, $[\mathsf P]$); the Fisher–intersection signature flip and the energy-condition $\Rightarrow$ causality implication are exact lemmas (§2.3, §4.1, $[\mathsf P]$); the energy condition is two-faced (intersection neg-def $\iff$ Rosati pos-def) and over $\mathbb F_q$ is the Hodge/Rosati positivity, a theorem (§4.2, $[\mathsf P]$); full RH is the positivity of the Frobenius-power Toeplitz / OS reflection form (§3.2, §5.1, $[\mathsf P]$). What it identifies as the single open object, $[\mathsf C]$ and equal in strength to RH: the Lorentzian-causal intersection metric over $\mathbb Q$ — equivalently the $\mathbb F_1$ scaling-site square with a negative-definite primitive form, equivalently the arithmetic energy condition $|a|\le2\sqrt q$, equivalently (§5) reflection positivity of the explicit-formula theory with a positive scaling transfer. The genuine deposits beyond the framing are (i) the exact signature re-vision (with the Tower Theorem as its corollary — stop building definite forms), now anchored over $\mathbb Q$ by the unconditional Faltings–Hriljac arithmetic Hodge index theorem (§4, end), which exhibits exactly the predicted $(1,\rho-1)$ signature while demonstrating — by its very unconditionality — that the height positivity it gives is *not* the spectral positivity RH needs, and sharpening the $\mathbb F_1$ obstruction to "the Hodge index theorem over $\mathbb Q$ exists, but on a curve over $\operatorname{Spec}\mathbb Z$, not on $\operatorname{Spec}\mathbb Z$ over $\mathbb F_1$"; (ii) the energy-condition $\Rightarrow$ causality lemma (the arithmetic focusing step, non-circular); and (iii) the de Branges $=$ OS-reconstruction synthesis (§5.3) on independent theorems [NÓ],[Ro],[LP], which routes the open positivity through the Herglotz/OS/positive-energy-semigroup machinery rather than the exhausted heat-flow monotones. The honest ceiling is stated plainly in §5.5: the OS framing is a relabeling at the level of the statement, the lattice/Gaussian-domination toolbox is **not** available (no positive local realization of the explicit formula is known), and the construction over $\mathbb Q$ — the time direction the additive metric could not see — is the work that remains.

---

## References and anchors

[T0] Murillo Montero, L. (2026). *What Is Additive? The Fourier–Mellin Simplex and the Apex Generator.*
[T8] Murillo Montero, L. (2026). *The Multiplicative Apex and Finite Dirichlet Polynomials.*
[T15] Murillo Montero, L. (2026). *Finite-to-Archimedean Completion.*
[P0] Murillo Montero, L. (2026). *The Adelic Place-Completion Keystone.*
[N7] Murillo Montero, L. (2026). *The Single Object.* (Rosati/Hodge Gram; the $\mathbb F_1$ obstruction.)
[Weil] Weil, A. (1948). *Sur les courbes algébriques et les variétés qui s'en déduisent.* (Hodge index on $C\times C$; RH for function fields.)
[Deligne] Deligne, P. (1974). *La conjecture de Weil I.*
[FH] Faltings, G. (1984). *Calculus on arithmetic surfaces.* Ann. of Math. 119; Hriljac, P. (1985). *Heights and Arakelov's intersection theory.* Amer. J. Math. 107. (The arithmetic Hodge index theorem: Arakelov intersection $=-$ Néron–Tate height pairing; negative-definite on the primitive part — unconditional, on a curve over $\operatorname{Spec}\mathbb Z$.)
[Mo] Moriwaki, A. (2014). *Arithmetic Hodge index theorem in higher dimension.*
[YZ] Yuan, X., Zhang, S.-W. (2017). *The arithmetic Hodge index theorem for adelic line bundles.* Math. Ann. 367. (Negative-definiteness over $\overline{\mathbb Q}$.)
[Ca] Carney, A. (2019). *The arithmetic Hodge index theorem and rigidity of dynamical systems over function fields.* arXiv:1810.06342. (Function-field analog; Thm 1.1 = negative-semidefinite on $\widehat{\mathrm{Pic}}^\tau$ with kernel the $K/k$-trace.)
[CC] Connes, A., Consani, C. (2021–2026). *Scaling site; on the Jacobian of $\overline{\operatorname{Spec}\mathbb Z}$* (arXiv:2602.15941); *Weil positivity at the archimedean place* (arXiv:2006.13771).
[RT] Rodgers, B., Tao, T. (2020). *The de Bruijn–Newman constant is non-negative.*
[HE] Hawking, S., Ellis, G. (1973). *The Large Scale Structure of Space-Time.* (Energy conditions and causality.)
[Bu] Burnol, J.-F. (1998). *The explicit formula in simple terms.* arXiv:math/9810169. (Positive-type / convolution-square reading of the explicit formula; the classical antecedent to a positivity framing.)
[NÓ] Neeb, K.-H., Ólafsson, G. *Reflection positivity* (arXiv:1608.04010; 1312.6161; SpringerBriefs arXiv:1802.09037). (Reflection positivity $\iff$ Laplace transform of a positive measure $\iff$ contractive positive-energy semigroup; the rigorous Euclidean$\to$Lorentzian bridge.)
[Ro] Romanov, R. (2014). *Canonical systems and de Branges spaces.* arXiv:1408.6022.
[LP] Lax, P., Phillips, R. (1967). *Scattering Theory.* (Dilation of a contraction semigroup to a unitary group.)

*Note (independence).* A program-adjacent essay (Toupin, "Haar Positivity: From Weil to Wightman", PhilArchive TOUHPF, 2026) makes the Weil$=$Wightman$=$OS identification but is non-independent and self-describes it as a relabeling; it is not cited as external corroboration. The OS/Lorentzian framing is absent from the live Connes–Consani program, so §5.3's de Branges$=$OS-reconstruction synthesis is unclaimed but rests on the independent theorems [NÓ],[Ro],[LP].

**Internal anchors.**

| Object | Location |
|---|---|
| toy finite Lorentzian intersection form | §2, `probe_toy_lorentzian_intersection.py` |
| higher-genus persistence + full-RH Toeplitz | §3, `probe_genus_lorentzian.py` |
| arithmetic energy condition (implication lemma) | §4, `probe_arithmetic_energy_condition.py` |
| reflection positivity = RH/$\mathbb F_q$ (OS reflection form) | §5, `probe_reflection_positivity.py` |
