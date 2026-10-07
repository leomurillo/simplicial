# T8 — The Multiplicative Apex and Finite Dirichlet Polynomials

**Leonardo Murillo Montero**

*First draft — May 25, 2026*

---

> *Additive Fourier knows the labels; multiplicative Fourier knows the units. Gauss sums know both.*

---

## Abstract

**Situation.** T0 (Murillo Montero 2026, T0) and T3 established the **additive** Fourier-Mellin transform on $\mathbb Z/N$: the apex generator $\mathcal M_x(\beta,c)$ uses additive characters $\chi_c(s)=e^{2\pi ics/N}$, which are homomorphisms $(\mathbb Z/N,+)\to\mathbb C^\times$ defined on every element of $\mathbb Z/N$. T7 lifted this apex from real-positive ledgers $\mathbb R_{>0}^N$ to complex amplitudes $\mathbb C^N$ via the Hopf/toric fibrations and the complex-log Riemann surface. Both T0 and T7 work with the additive Pontryagin dual of $\mathbb Z/N$ — call this the **additive sector** of the categorical simplex.

**Gap.** Classical analytic number theory — Dirichlet $L$-functions, Gauss sums, Kloosterman sums, the finite Fourier analysis underlying the Bombieri–Vinogradov theorem and the large sieve — uses **multiplicative** characters $\psi:(\mathbb Z/N)^\times\to\mathbb C^\times$, defined only on the units of $\mathbb Z/N$ rather than on all elements. The additive sector (T0, T7) and the multiplicative sector are dual but structurally distinct: they live on different underlying groups ($\mathbb Z/N$ vs $(\mathbb Z/N)^\times$, of sizes $N$ vs $\varphi(N)$), use different convolution structures (additive vs multiplicative selection rules), and connect to different classical literatures (cyclic Fourier theory vs Dirichlet $L$-functions and arithmetic statistics). T0 §6.2 scoped the multiplicative version as a forward door without development.

**Action.** We define the **multiplicative apex generator** on units,
$$\mathcal D_x(\beta,\psi):=\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\psi(s)},$$
parameterized by the gauge exponent $\beta\in\mathbb C$ and the Dirichlet character $\psi\in\widehat{(\mathbb Z/N)^\times}$. We establish the multiplicative analogs of T0's main theorems — trivial-mode reduction, moment diagonal, closure diagonal, Euler factorization over the structure of $(\mathbb Z/N)^\times$ — with the new feature that the **selection rules become multiplicative**: in place of T0's additive convolution rule $a_1+\cdots+a_n\equiv c\pmod N$, the multiplicative apex obeys $\chi_1\chi_2\cdots\chi_n=\psi$ in the dual group $\widehat{(\mathbb Z/N)^\times}$. We bridge to T0's additive apex via **Gauss sums**: a Dirichlet character $\psi$ and an additive character $\chi_a$ are dual via $\tau(\psi,a)=\sum_s\psi(s)\chi_a(s)$, and the bridge is the natural intertwiner between the two apex generators. We construct the **finite Dirichlet polynomial**
$$L_x(\beta,\psi):=\sum_{n=1}^N\chi(n)\,x_n^{-\beta}$$
as a direct finite analog of the classical Dirichlet $L$-function $L(s,\chi)=\sum_n\chi(n)/n^s$, and identify the conditions under which finite arithmetic ledgers (such as the characteristic function of primes mod $N$) produce non-trivial $L$-function structure.

**Result.** Eight core claims:

1. **Multiplicative apex generator.** $\mathcal D_x(\beta,\psi)$ is well-defined for every Dirichlet character $\psi$ and every $\beta\in\mathbb C$, holomorphic in $\beta$, and on the principal character $\psi=\psi_0$ reduces to the cumulant generating function of the centered log-ledger over units.

2. **Multiplicative selection rule (moment diagonal).** Taylor coefficients of $\mathcal D_x(\beta,\psi)$ at $\beta=0$ form a character-twisted moment tower with the multiplicative convolution constraint
$$\widehat{y^n}_\psi=\sum_{\substack{\chi_1,\ldots,\chi_n\in\widehat{(\mathbb Z/N)^\times}\\\chi_1\chi_2\cdots\chi_n=\psi}}\widehat y_{\chi_1}\widehat y_{\chi_2}\cdots\widehat y_{\chi_n},$$
where the convolution is in the dual group $\widehat{(\mathbb Z/N)^\times}$, not in $\mathbb Z/N$.

3. **Multiplicative closure diagonal.** Integer-$\beta$ samples satisfy
$$\mathcal D_x(m,\psi)=G(x)^{-m}\widehat{x^m}_\psi=G(x)^{-m}\sum_{\chi_1\chi_2\cdots\chi_m=\psi}\widehat x_{\chi_1}\cdots\widehat x_{\chi_m},$$
the multiplicative analog of T0 Theorem 3.5.

4. **Decomposition over the unit-group structure, in two layers.** The CRT factorization $(\mathbb Z/N)^\times\cong\prod_i(\mathbb Z/p_i^{a_i})^\times$ stratifies the multiplicative sector exactly as T0 §4.1 stratifies the additive sector, but with a structural asymmetry that has no additive counterpart: each odd-prime factor $(\mathbb Z/p^a)^\times$ is **cyclic**, so the *only* source of local (intra-prime) non-cyclicity is the **2-adic anomaly** $(\mathbb Z/2^a)^\times\cong\mathbb Z/2\times\mathbb Z/2^{a-2}$ ($a\ge 3$). Cross-axis content therefore arises in two distinct ways — intra-prime (the 2-adic anomaly, anchored at $N=8$) and cross-prime (the product over distinct primes, anchored at $N=12$) — and the apex factorizes over the CRT primes exactly when the ledger is separable across them.

5. **Gauss-sum bridge.** The classical Gauss sum $\tau(\psi,a)=\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\chi_a(s)$ intertwines the multiplicative apex $\mathcal D_x$ on units with the additive apex $\mathcal M_x$ on $\mathbb Z/N$, with explicit transformation rules at integer $\beta=m$.

6. **Finite Dirichlet polynomials.** On the arithmetic ledger $x_s=s$, the sign-flipped sample $L_x(-\beta,\chi)=\varphi(N)\,G(x)^\beta\,\mathcal D_x(\beta,\bar\chi)$ identifies the multiplicative apex as the natural finite analog of the classical Dirichlet $L$-function — a structural analog whose arithmetic ($L$-function) content is carried by the genuine $L(s,\chi)$, not the finite truncation.

7. **$N=8$ and $N=12$ as the two structural anchors.** $N=8$ is the smallest $N$ with non-cyclic $(\mathbb Z/N)^\times\cong\mathbb Z/2\times\mathbb Z/2$ (intra-prime, the 2-adic anomaly): its three non-principal characters $\{\chi_{-4},\chi_8,\chi_{-8}\}$ have conductors $\{4,8,8\}$, all powers of the single prime $2$. $N=12$ is the smallest $N$ whose non-cyclic $V_4$ is **cross-prime**, $(\mathbb Z/12)^\times\cong(\mathbb Z/4)^\times\times(\mathbb Z/3)^\times$: its non-principal characters have conductors $\{4,3,12\}$, the genuine multiplicative analog of T0's cross-prime $N=6$. Both are computed explicitly.

8. **Dynamical and dual structure.** The multiplicative apex carries the escort/replicator $\beta$-flow through the character-convolution law $\partial_\beta\mathcal D_x(\beta,\psi)=\sum_\chi\widehat y_\chi\,\mathcal D_x(\beta,\psi\bar\chi)$ (multiplicative dual of T0 Proposition 3.8); on the principal character it inherits T0's full dually-flat structure — conjugate potential, escort entropy, Cramér rate function — over the uniform measure on the $\varphi(N)$ units.

**Harvest.** The categorical-simplex apex carries two dual Fourier structures: the additive Fourier (T0, T7) on the labels of $\mathbb Z/N$, and the multiplicative Fourier (T8) on the units of $(\mathbb Z/N)^\times$. The two are connected by Gauss sums and together exhaust the classical Fourier analysis available on the finite cyclic group. The additive sector is the home of categorical Fourier theory (T0–T7); the multiplicative sector is the home of finite analogs of Dirichlet $L$-functions and is the precise bridge to the analytic number-theoretic content of the T-program (T0 §6.7). The RH-shaped questions of the program live most naturally on the multiplicative apex.

**Keywords:** Dirichlet characters, multiplicative characters, $(\mathbb Z/N)^\times$, Gauss sums, Kloosterman sums, finite Dirichlet polynomials, multiplicative Fourier-Mellin transform, multiplicative selection rule, multiplicative conductor depth, the 2-adic anomaly, intra-prime vs cross-prime non-cyclicity, escort/replicator flow, primitive root, character group duality, finite analog of $L$-functions, Pontryagin duality on units.

---

## Cross-references from prior papers

This paper builds on specific results from earlier papers of the \heb{ל}-series; we list the dependencies explicitly.

| Cited result | Used for |
|---|---|
| T0 §3.2 Definition 3.1 (additive apex generator $\mathcal M_x$) | Structural analog for $\mathcal D_x$ in Definition 2.1 |
| T0 §2.4 Theorem 2.4 (escort/replicator $\beta$-flow) | Structural analog for Proposition 2.6 (multiplicative flow) |
| T0 §2.7 Theorem 2.7 (dually-flat / conjugate potential) | Inherited on the principal character, Remark 2.8 |
| T0 §3.3 Theorem 3.3 (moment diagonal, additive selection rule) | Structural analog for Theorem 2.4 (multiplicative selection rule) |
| T0 §3.3 Theorem 3.5 (closure diagonal, additive selection rule) | Structural analog for Theorem 2.5 |
| T0 §3.3 Corollary 3.6 (negative-integer polar partner) | Structural analog for Corollary 2.7 |
| T0 §3.5 Proposition 3.8 ($\beta$-derivative as character convolution) | Structural analog for Proposition 2.6 |
| T0 §4.1–§4.2 (two prime layers; prime-power conductor depth) | Two-layer decomposition §3.3–§3.4 |
| T0 §4.3 Theorem 4.4 (separability $\Leftrightarrow$ Euler factorization) | Structural analog for Theorem 3.1 |
| T0 §4.4 Theorem 4.7 (ANOVA orthogonality and cumulant criterion) | Structural analog for §3.2 |
| T3 (cubic vertex selection rule) | Background for §7.1 cubic vertex on units |
| T7 §1, §2 (complex amplitude framework) | Forward door §7 mention |
| T9 / T9.4 (Helmert–Fourier matrix; Gauss-sum decomposition of conductor blocks) | Refines the Gauss-sum bridge §4 (forward) |
| T8.4 (Stieltjes positivity of the prime multiplicative apex) | Concrete instance of the RH-shaped door §7.3 (forward) |

T8 is structurally parallel to T0 with the multiplicative dual replacing the additive: every T0 theorem cited above has a multiplicative analog in T8.

---

## Notation

We carry the notation of T0 and add the multiplicative-character layer.

| Symbol | Meaning |
|---|---|
| $N$ | Positive integer modulus, $\ge 2$. |
| $(\mathbb Z/N)^\times$ | The multiplicative group of units mod $N$, of order $\varphi(N)$. |
| $\varphi(N)$ | Euler totient function: $|(\mathbb Z/N)^\times|$. |
| $\widehat{(\mathbb Z/N)^\times}$ | Pontryagin dual / Dirichlet character group of $(\mathbb Z/N)^\times$. |
| $\psi,\chi,\eta$ | Dirichlet characters (multiplicative characters of $(\mathbb Z/N)^\times$). |
| $\psi_0$ | Principal (trivial) Dirichlet character, $\psi_0(s)=1$ for $s\in(\mathbb Z/N)^\times$. |
| $\chi_c$ | Additive character $\chi_c(s)=e^{2\pi ics/N}$ of $\mathbb Z/N$ (T0 notation). |
| $x$ | Real-positive ledger on units, $x:(\mathbb Z/N)^\times\to\mathbb R_{>0}$. |
| $G(x)$ | Geometric mean over units: $G(x)=\big(\prod_{s\in(\mathbb Z/N)^\times}x_s\big)^{1/\varphi(N)}$. |
| $y_s$ | Centered log-ledger on units: $y_s=\log x_s-\frac{1}{\varphi(N)}\sum_t\log x_t$. |
| $\widehat x_\psi$ | Dirichlet-character Fourier coefficient: $\widehat x_\psi=\frac{1}{\varphi(N)}\sum_s x_s\overline{\psi(s)}$. |
| $\mathcal D_x(\beta,\psi)$ | Multiplicative apex generator (Definition 2.1). |
| $\mathcal M_x(\beta,c)$ | T0 additive apex generator. |
| $\tau(\psi,a)$ | Gauss sum: $\tau(\psi,a)=\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\chi_a(s)$. |
| $K(a,b;N)$ | Kloosterman sum: $K(a,b;N)=\sum_{s\in(\mathbb Z/N)^\times}\chi_a(s)\chi_b(s^{-1})$. |
| $L_x(\beta,\psi)$ | Finite Dirichlet polynomial (§5). |
| $\mathrm{cond}(\psi)$ | Conductor of the Dirichlet character $\psi$. |

**Convention.** Multiplication of Dirichlet characters $\chi_1\chi_2$ refers to pointwise multiplication of functions on $(\mathbb Z/N)^\times$: $(\chi_1\chi_2)(s):=\chi_1(s)\chi_2(s)$. This makes $\widehat{(\mathbb Z/N)^\times}$ a group under multiplication, isomorphic to $(\mathbb Z/N)^\times$ itself (non-canonically).

---

## 1. The multiplicative dual: Dirichlet characters of $(\mathbb Z/N)^\times$

### 1.1 The unit group and its structure

The set
$$(\mathbb Z/N)^\times:=\{s\in\mathbb Z/N:\gcd(s,N)=1\}$$
is the **group of units modulo $N$** under multiplication mod $N$, of order $\varphi(N)$. By the structure theorem of finite abelian groups,
$$(\mathbb Z/N)^\times\cong\prod_i\mathbb Z/d_i,\qquad d_1\mid d_2\mid\cdots,$$
a direct product of cyclic groups. The structure depends on $N$:

- $N=p$ odd prime: $(\mathbb Z/p)^\times\cong\mathbb Z/(p-1)$, cyclic.
- $N=p^a$ odd prime power: $(\mathbb Z/p^a)^\times\cong\mathbb Z/p^{a-1}(p-1)$, cyclic.
- $N=2$: $(\mathbb Z/2)^\times=\{1\}$, trivial.
- $N=4$: $(\mathbb Z/4)^\times=\{1,3\}\cong\mathbb Z/2$, cyclic.
- $N=2^a$ for $a\ge 3$: $(\mathbb Z/2^a)^\times\cong\mathbb Z/2\times\mathbb Z/2^{a-2}$, non-cyclic.
- $N=\prod p_i^{a_i}$ general: CRT decomposition $(\mathbb Z/N)^\times\cong\prod_i(\mathbb Z/p_i^{a_i})^\times$, where each factor is determined by the above.

**The non-cyclic cases.** The smallest $N$ for which $(\mathbb Z/N)^\times$ is non-cyclic is $N=8$, with $(\mathbb Z/8)^\times=\{1,3,5,7\}\cong\mathbb Z/2\times\mathbb Z/2$ (Klein four-group). Crucially, this non-cyclicity is **intra-prime**: it comes from the single prime $2$ via the anomaly $(\mathbb Z/2^a)^\times\cong\mathbb Z/2\times\mathbb Z/2^{a-2}$ ($a\ge 3$), since every odd-prime-power unit group is cyclic. The smallest $N$ whose non-cyclic $V_4$ is instead **cross-prime** — assembled from two distinct primes — is $N=12$, with $(\mathbb Z/12)^\times\cong(\mathbb Z/4)^\times\times(\mathbb Z/3)^\times\cong\mathbb Z/2\times\mathbb Z/2$. These two cases realize the *same* abstract group $V_4$ through *different* arithmetic; both are structural anchors of T8 (§6), and the distinction — the multiplicative refinement of T0 §4.1's two prime layers — is developed in §3.3–§3.4. ($N=6$ was T0's single additive anchor; the multiplicative sector splits it into two.)

### 1.2 Dirichlet characters as multiplicative characters

A **Dirichlet character mod $N$** is a group homomorphism
$$\psi:(\mathbb Z/N)^\times\longrightarrow\mathbb C^\times,$$
i.e., a function satisfying $\psi(s_1s_2)=\psi(s_1)\psi(s_2)$ for all $s_1,s_2\in(\mathbb Z/N)^\times$ and $\psi(1)=1$. Every value $\psi(s)$ is a root of unity (since $s^{\varphi(N)}=1$ forces $\psi(s)^{\varphi(N)}=1$); the values lie in $\mu_{\mathrm{ord}_s}$ where $\mathrm{ord}_s$ is the multiplicative order of $s$.

The set of all Dirichlet characters mod $N$, under pointwise multiplication, forms the **dual group**
$$\widehat{(\mathbb Z/N)^\times}=\{\psi:(\mathbb Z/N)^\times\to\mathbb C^\times\}\cong(\mathbb Z/N)^\times$$
(non-canonically, by Pontryagin duality for finite abelian groups). The dual group has order $\varphi(N)$.

The **principal character** is $\psi_0(s)=1$ for every $s\in(\mathbb Z/N)^\times$, the identity element of $\widehat{(\mathbb Z/N)^\times}$.

### 1.3 Conductor, primitivity, and multiplicative depth

A Dirichlet character $\psi$ mod $N$ is **induced from** a character $\psi'$ mod $N'$ for $N'\mid N$ if $\psi(s)=\psi'(s\bmod N')$ for every $s\in(\mathbb Z/N)^\times$. The **conductor** $\mathrm{cond}(\psi)$ is the smallest such $N'$; if $\mathrm{cond}(\psi)=N$, then $\psi$ is **primitive**.

**Multiplicative conductor depth.** Conductor depth is the multiplicative analog of T0 §4.2's prime-power conductor filtration, with one structural difference inherited from §1.1. For $N=p^a$ with $p$ **odd**, $(\mathbb Z/p^a)^\times\cong\mathbb Z/p^{a-1}(p-1)$ is cyclic and the conductors of its characters form a single chain $1\mid p\mid p^2\mid\cdots\mid p^a$ — a $p$-adic depth ladder mirroring the additive filtration $H_p\subset H_{p^2}\subset\cdots\subset H_{p^a}$ of T0 §4.2. For $p=2$ and $a\ge 3$ the unit group is non-cyclic, so the conductor data is no longer a chain: characters are classified by their behavior on *each* of the two generators $-1$ and $5$ of $(\mathbb Z/2^a)^\times=\langle-1\rangle\times\langle 5\rangle$. We compute this two-dimensional depth structure at $N=8$ in §6 and contrast it with the genuinely cross-prime case $N=12$ in §3.4.

**Primitivity and Gauss-sum magnitude.** Primitivity is the exact condition under which the Gauss sum $\tau(\psi,a)$ of §4 attains the clean magnitude $\sqrt N$. For **primitive** $\psi$ mod $N$ and $\gcd(a,N)=1$,
$$\tau(\psi,a)=\overline{\psi(a)}\,\tau(\psi,1),\qquad|\tau(\psi,1)|=\sqrt N,\qquad\text{and}\qquad\tau(\psi,a)=0\ \text{ whenever }\gcd(a,N)>1$$
(Iwaniec–Kowalski 2004, §3.4–3.5; Davenport 2000). For **induced** (non-primitive) $\psi$ the magnitude follows the induction/separability formula and is in general strictly smaller — it can vanish. The extreme case is the principal character, whose Gauss sum is the Ramanujan sum
$$\tau(\psi_0,a)=\sum_{s\in(\mathbb Z/N)^\times}e^{2\pi ias/N}=c_N(a),\qquad|c_N(1)|=|\mu(N)|\le 1,$$
nowhere near $\sqrt N$. This primitive/induced dichotomy is the multiplicative depth invariant — the analog of which additive conductor packet a character occupies in T0 §4.2 — and §4 is written so that the Gauss-sum bridge respects it.

### 1.4 Character orthogonality on units

The standard orthogonality relations for Dirichlet characters:
$$\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}\psi_1(s)\overline{\psi_2(s)}=\delta_{\psi_1,\psi_2},$$
$$\frac{1}{\varphi(N)}\sum_{\psi\in\widehat{(\mathbb Z/N)^\times}}\psi(s_1)\overline{\psi(s_2)}=\delta_{s_1,s_2}\quad(s_1,s_2\in(\mathbb Z/N)^\times),$$
giving the **multiplicative Fourier transform** on $(\mathbb Z/N)^\times$:
$$\widehat f_\psi:=\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}f(s)\overline{\psi(s)},\qquad f(s)=\sum_{\psi}\widehat f_\psi\,\psi(s),$$
for any $f:(\mathbb Z/N)^\times\to\mathbb C$.

This is the multiplicative analog of T0's Fourier transform on $\mathbb Z/N$. The structural difference: $(\mathbb Z/N)^\times$ has $\varphi(N)$ elements, fewer than $N$ in general; the multiplicative Fourier transform is "smaller" than the additive but still complete on its own group.

---

## 2. The multiplicative apex generator

### 2.1 Centered log-ledger on units

Given a positive ledger $x:(\mathbb Z/N)^\times\to\mathbb R_{>0}$, define the **geometric mean over units** as
$$G(x):=\Big(\prod_{s\in(\mathbb Z/N)^\times}x_s\Big)^{1/\varphi(N)},$$
and the **centered log-ledger on units** as
$$y_s:=\log x_s-\frac{1}{\varphi(N)}\sum_{t\in(\mathbb Z/N)^\times}\log x_t=\log\!\Big(\frac{x_s}{G(x)}\Big),\qquad s\in(\mathbb Z/N)^\times,$$
satisfying $\sum_s y_s=0$. The vector $y\in\mathbb R^{(\mathbb Z/N)^\times}$ lives in the mean-zero hyperplane of $\mathbb R^{\varphi(N)}$.

### 2.2 The multiplicative apex generator

**Definition 2.1 (Multiplicative apex generator).** Let $x:(\mathbb Z/N)^\times\to\mathbb R_{>0}$ be a positive ledger on units with centered log-ledger $y$. The **multiplicative apex generator** is
$$\boxed{\mathcal D_x(\beta,\psi):=\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}e^{\beta y_s}\,\overline{\psi(s)}=G(x)^{-\beta}\cdot\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\psi(s)},}$$
parameterized by $\beta\in\mathbb C$ and $\psi\in\widehat{(\mathbb Z/N)^\times}$.

The structure is directly parallel to T0 Definition 3.1, with three changes: (i) the sum is over $(\mathbb Z/N)^\times$ rather than $\mathbb Z/N$, of size $\varphi(N)$ rather than $N$; (ii) the character index is a Dirichlet character $\psi$, rather than an additive character; (iii) the normalization is by $\varphi(N)$ rather than $N$.

### 2.3 Spine theorems

**Theorem 2.2 (Holomorphy).** For each fixed ledger $x$ and Dirichlet character $\psi$, $\mathcal D_x(\cdot,\psi):\mathbb C\to\mathbb C$ is entire in $\beta$.

**Proof.** Each summand $e^{\beta y_s}\overline{\psi(s)}$ is entire in $\beta$ (composition of linear map with entire exponential, times a $\beta$-independent constant). Finite sums of entire functions are entire. $\square$

**Theorem 2.3 (Trivial mode reduction).** $\mathcal D_x(\beta,\psi_0)=e^{K_y(\beta)}$, where $K_y(\beta)=\log\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}e^{\beta y_s}$ is the cumulant generating function of the centered log-ledger over units (uniform measure on units).

**Proof.** $\overline{\psi_0(s)}=1$ for every $s\in(\mathbb Z/N)^\times$, so the sum reduces to $\frac{1}{\varphi(N)}\sum_s e^{\beta y_s}=e^{K_y(\beta)}$. $\square$

The trivial-mode reduction (Theorem 2.3) is the multiplicative analog of T0 Theorem 3.2: it identifies the principal-character slice of $\mathcal D_x$ with the unstructured apex on units (interpreting "unstructured" as ignoring the multiplicative group structure and using only the uniform measure on the $\varphi(N)$ units).

**Theorem 2.4 (Moment diagonal — multiplicative selection rule).** For each Dirichlet character $\psi$ and each integer $n\ge 0$,
$$\partial_\beta^n\mathcal D_x(0,\psi)=\widehat{y^n}_\psi=\sum_{\substack{\chi_1,\ldots,\chi_n\in\widehat{(\mathbb Z/N)^\times}\\\chi_1\chi_2\cdots\chi_n=\psi}}\widehat y_{\chi_1}\widehat y_{\chi_2}\cdots\widehat y_{\chi_n},$$
where the convolution constraint $\chi_1\chi_2\cdots\chi_n=\psi$ is multiplication in the dual group $\widehat{(\mathbb Z/N)^\times}$.

**Proof.** Differentiating $n$ times in $\beta$ and evaluating at $\beta=0$ yields
$$\partial_\beta^n\mathcal D_x(0,\psi)=\frac{1}{\varphi(N)}\sum_s y_s^n\overline{\psi(s)}=\widehat{y^n}_\psi.$$
For the convolution form, apply the multiplicative Fourier inversion $y_s=\sum_\chi\widehat y_\chi\chi(s)$ to obtain
$$y_s^n=\sum_{\chi_1,\ldots,\chi_n}\widehat y_{\chi_1}\cdots\widehat y_{\chi_n}\,\chi_1(s)\chi_2(s)\cdots\chi_n(s)=\sum_{\chi_1,\ldots,\chi_n}\widehat y_{\chi_1}\cdots\widehat y_{\chi_n}\,(\chi_1\chi_2\cdots\chi_n)(s),$$
using the group law in $\widehat{(\mathbb Z/N)^\times}$ (pointwise multiplication of characters is character multiplication in the dual group). Substituting,
$$\widehat{y^n}_\psi=\sum_{\chi_1,\ldots,\chi_n}\widehat y_{\chi_1}\cdots\widehat y_{\chi_n}\cdot\frac{1}{\varphi(N)}\sum_s(\chi_1\chi_2\cdots\chi_n)(s)\overline{\psi(s)}.$$
Multiplicative character orthogonality gives $\frac{1}{\varphi(N)}\sum_s\chi(s)\overline{\psi(s)}=\delta_{\chi,\psi}$, collapsing the inner sum to the indicator of $\chi_1\chi_2\cdots\chi_n=\psi$ in the dual group. $\square$

**Theorem 2.5 (Closure diagonal — multiplicative selection rule).** For each integer $m\ge 1$ and each Dirichlet character $\psi$,
$$\mathcal D_x(m,\psi)=G(x)^{-m}\widehat{x^m}_\psi=G(x)^{-m}\sum_{\substack{\chi_1,\ldots,\chi_m\in\widehat{(\mathbb Z/N)^\times}\\\chi_1\chi_2\cdots\chi_m=\psi}}\widehat x_{\chi_1}\widehat x_{\chi_2}\cdots\widehat x_{\chi_m}.$$

**Proof.** From $y_s=\log x_s-\log G(x)$ we have $e^{my_s}=(x_s/G(x))^m=G(x)^{-m}x_s^m$ for integer $m\ge 1$, so $\mathcal D_x(m,\psi)=G(x)^{-m}\widehat{x^m}_\psi$. Expanding $x_s=\sum_\chi\widehat x_\chi\chi(s)$ gives $x_s^m=\sum_{\chi_1,\ldots,\chi_m}\widehat x_{\chi_1}\cdots\widehat x_{\chi_m}(\chi_1\cdots\chi_m)(s)$, and multiplicative character orthogonality $\frac{1}{\varphi(N)}\sum_s(\chi_1\cdots\chi_m)(s)\overline{\psi(s)}=\delta_{\chi_1\cdots\chi_m,\psi}$ collapses the inner sum to the selection rule — the exact multiplicative transcription of T0 Theorem 3.5. $\square$

### 2.4 Dynamics and duality on the multiplicative apex

The principal-character slice $\mathcal D_x(\beta,\psi_0)=e^{K_y(\beta)}$ (Theorem 2.3) inherits, over the uniform measure on the $\varphi(N)$ units, the dynamical and dual structure T0 established for the additive trivial mode. We record the three statements; each proof is the multiplicative transcription of its T0 original.

**Proposition 2.6 ($\beta$-derivative as character convolution; escort flow).** For every $\beta\in\mathbb C$ and every Dirichlet character $\psi$,
$$\boxed{\partial_\beta\mathcal D_x(\beta,\psi)=\sum_{\chi\in\widehat{(\mathbb Z/N)^\times}}\widehat y_\chi\,\mathcal D_x(\beta,\psi\bar\chi),}$$
the multiplicative dual of T0 Proposition 3.8, with convolution in the dual group $\widehat{(\mathbb Z/N)^\times}$. In particular the **escort family on units** $P_\beta(s)=e^{\beta y_s}/\sum_{t}e^{\beta y_t}$ satisfies the constant-fitness replicator equation $\partial_\beta P_\beta(s)=P_\beta(s)\big(y_s-\mathbb E_{P_\beta}[y]\big)$ (T0 Theorem 2.4); at $\psi=\psi_0$ the identity reduces to $K_y'(\beta)=\mathbb E_{P_\beta}[y]$ and $K_y''(\beta)=\mathrm{Var}_{P_\beta}(y)\ge 0$.

**Proof.** Differentiating Definition 2.1, $\partial_\beta\mathcal D_x(\beta,\psi)=\frac{1}{\varphi(N)}\sum_s y_s\,e^{\beta y_s}\overline{\psi(s)}$. Expand $y_s=\sum_\chi\widehat y_\chi\chi(s)$ (multiplicative Fourier inversion, §1.4). Each character value is a root of unity, so $\overline{\chi(s)}=\chi(s)^{-1}$ and $\chi(s)\overline{\psi(s)}=\overline{(\psi\bar\chi)(s)}$; hence
$$\partial_\beta\mathcal D_x(\beta,\psi)=\sum_\chi\widehat y_\chi\cdot\frac{1}{\varphi(N)}\sum_s e^{\beta y_s}\,\overline{(\psi\bar\chi)(s)}=\sum_\chi\widehat y_\chi\,\mathcal D_x(\beta,\psi\bar\chi).$$
The escort and free-energy statements are the $\psi=\psi_0$ specialization, identical to the proofs of T0 Theorem 2.4 with $N$ replaced by $\varphi(N)$ and the sum taken over units. $\square$

**Corollary 2.7 (Negative-integer polar partner).** Let $x^{-1}$ be the reciprocal ledger on units, $(x^{-1})_s=x_s^{-1}$, whose centered log-ledger is $\tilde y=-y$. For each negative integer $-m'$ with $m'\ge 1$,
$$\mathcal D_x(-m',\psi)=\mathcal D_{x^{-1}}(m',\psi)=G(x^{-1})^{-m'}\sum_{\substack{\chi_1,\ldots,\chi_{m'}\\\chi_1\cdots\chi_{m'}=\psi}}\widehat{x^{-1}}_{\chi_1}\cdots\widehat{x^{-1}}_{\chi_{m'}},$$
the multiplicative analog of T0 Corollary 3.6: the negative closure diagonal is the positive closure diagonal of the reciprocal ledger.

**Proof.** $e^{-m'y_s}=e^{m'\tilde y_s}$ with $\tilde y=-y$ the centered log-ledger of $x^{-1}$ (reciprocation negates the log and preserves centering, $\sum_s\tilde y_s=0$); apply Theorem 2.5 to $x^{-1}$. $\square$

**Remark 2.8 (Dually-flat structure on the principal character).** Since $\mathcal D_x(\beta,\psi_0)=e^{K_y(\beta)}$ is the cumulant generating function of $y$ under the uniform measure on the $\varphi(N)$ units, the dually-flat apparatus of T0 §2.7 transfers verbatim with $N\rightsquigarrow\varphi(N)$ and uniform center $u_\times=(1/\varphi(N),\ldots,1/\varphi(N))$ on units: the conjugate potential $K_y^\ast(\xi)=\sup_\beta(\beta\xi-K_y(\beta))$ equals the escort entropy $\log\varphi(N)-H(P_\beta)=D(P_\beta\Vert u_\times)$ and is the Cramér rate function for the empirical mean of i.i.d. draws from the uniform law on $\{y_s\}_{s\in(\mathbb Z/N)^\times}$; the canonical divergence is the relative entropy of escorts; and metric reciprocity $(K_y^\ast)''(\xi)=1/K_y''(\beta)$ holds. The non-principal modes $\psi\ne\psi_0$ are complex-valued and admit no Legendre conjugate, so — exactly as in T0 §3.4 — the **entropy diagonal lives only on $\psi_0$**. This is the multiplicative home of T0's entropy diagonal.

### 2.5 The two selection rules: additive vs multiplicative

The structural comparison between T0 (additive) and T8 (multiplicative) is sharpest at the level of selection rules:

| | T0 (Additive) | T8 (Multiplicative) |
|---|---|---|
| Underlying group | $\mathbb Z/N$ (size $N$) | $(\mathbb Z/N)^\times$ (size $\varphi(N)$) |
| Group operation | addition mod $N$ | multiplication mod $N$ |
| Characters | $\chi_c(s)=e^{2\pi ics/N}$ | $\psi(s)$ defined on units |
| Character group operation | addition of indices $c\in\mathbb Z/N$ | multiplication of characters in $\widehat{(\mathbb Z/N)^\times}$ |
| Moment selection rule | $a_1+\cdots+a_n\equiv c\pmod N$ | $\chi_1\chi_2\cdots\chi_n=\psi$ in $\widehat{(\mathbb Z/N)^\times}$ |
| Closure selection rule | $a_1+\cdots+a_m\equiv c\pmod N$ | $\chi_1\chi_2\cdots\chi_m=\psi$ in $\widehat{(\mathbb Z/N)^\times}$ |
| Reduces to abelian arithmetic | yes (cyclic group law) | yes (group law in $\widehat{(\mathbb Z/N)^\times}$, possibly non-cyclic) |

The additive selection rule is **always** a cyclic-additive condition (in $\mathbb Z/N$). The multiplicative selection rule lives in $\widehat{(\mathbb Z/N)^\times}$, which is **cyclic when $(\mathbb Z/N)^\times$ is cyclic** (e.g., $N$ prime, $N=p^a$ odd, $N=2$ or $4$) and **non-cyclic** otherwise (e.g., $N=8,12,15,16,20,\ldots$). The first non-cyclic case $N=8$ exhibits the multiplicative-Klein-four selection rule $\chi_1\chi_2\cdots\chi_n=\psi$ with $\widehat{(\mathbb Z/N)^\times}\cong\mathbb Z/2\times\mathbb Z/2$, qualitatively distinct from any additive selection rule.

---

## 3. Decomposition over the unit-group structure

### 3.1 CRT and cyclic-factor decomposition

The canonical decomposition of the unit group is the CRT factorization over the primes dividing $N$,
$$(\mathbb Z/N)^\times\cong\prod_{i=1}^k(\mathbb Z/p_i^{a_i})^\times,\qquad N=\prod_{i=1}^k p_i^{a_i},$$
the multiplicative shadow of T0 Proposition 4.3. Each factor is cyclic for odd $p_i$ and a product $\mathbb Z/2\times\mathbb Z/2^{a-2}$ for $p_i=2$, $a\ge 3$ (§1.1); refining further by the structure theorem of finite abelian groups gives
$$(\mathbb Z/N)^\times\cong\prod_{j}\mathbb Z/d_j,\qquad d_1\mid d_2\mid\cdots.$$
The dual group dualizes the same way, $\widehat{(\mathbb Z/N)^\times}\cong\prod_i\widehat{(\mathbb Z/p_i^{a_i})^\times}$, and every Dirichlet character factors as $\psi=\prod_i\psi_i$ over the prime-power components (equivalently, over the cyclic factors). The **prime-indexed** factorization is the one that parallels T0's CRT-over-primes; the cyclic refinement is finer and, for $p=2$, genuinely two-dimensional.

### 3.2 ANOVA on units

When the ledger $y:(\mathbb Z/N)^\times\to\mathbb R$ is separable across cyclic factors (i.e., $y(s_1,\ldots,s_k)=\sum_iy^{(i)}(s_i)$ in the cyclic-factor decomposition), the multiplicative apex factorizes:
$$\mathcal D_x(\beta,\psi)=\prod_{i=1}^k\mathcal D^{(i)}_{x^{(i)}}(\beta,\psi_i).$$

The proof and converse are exact multiplicative analogs of T0 Theorem 4.4 (separability $\Leftrightarrow$ Euler factorization) and T0 Theorem 4.7 (ANOVA orthogonality and cumulant separability criterion); we record this as:

**Theorem 3.1 (Multiplicative Euler factorization).** For $(\mathbb Z/N)^\times\cong\prod_i\mathbb Z/d_i$ and any ledger $x$ on units, the multiplicative apex $\mathcal D_x(\beta,\psi)$ factorizes as a product over the cyclic factors iff the centered log-ledger $y$ is separable across them, i.e., $y(s_1,\ldots,s_k)=\sum_iy^{(i)}(s_i)$.

The proof is identical in structure to T0 Theorem 4.4, with additive characters replaced by multiplicative characters and additive separability replaced by separability across cyclic factors. The cross-factor interaction stratum (the obstruction to factorization) is the multiplicative analog of T0's cross-prime ANOVA stratum.

### 3.3 Two layers of multiplicative structure

T0 §4.1 distinguished two layers of additive prime structure: **local prime-power depth** (the $p$-adic conductor filtration on $\mathbb Z/p^a$) and **global cross-prime interaction** (non-separability across the CRT factors of $\mathbb Z/N$). The multiplicative sector has the same two layers — with a structural asymmetry that has no additive counterpart.

- **Local layer (intra-prime).** On $(\mathbb Z/p^a)^\times$ the layer is a single $p$-adic conductor chain (§1.3) — *except* at $p=2$, $a\ge 3$, where the 2-adic anomaly $(\mathbb Z/2^a)^\times\cong\mathbb Z/2\times\mathbb Z/2^{a-2}$ makes the unit group non-cyclic and the local layer genuinely two-dimensional. For every odd prime the local unit group is cyclic, so **the only intra-prime cross-axis content in the entire multiplicative sector comes from the prime $2$.**
- **Global layer (cross-prime).** Across the CRT factorization $(\mathbb Z/N)^\times\cong\prod_i(\mathbb Z/p_i^{a_i})^\times$, the apex factorizes iff the ledger is separable (Theorem 3.1); the obstruction is the cross-prime interaction stratum, the exact multiplicative analog of T0's cross-prime ANOVA (§4.5).

Whereas T0's first non-trivial case $N=6$ is unambiguously cross-prime, the multiplicative sector's *first non-cyclic* case $N=8$ is intra-prime (the 2-adic anomaly), and its *first cross-prime non-cyclic* case is $N=12$. The corrected parallel with T0:

| Property | T0 (additive) | T8 (multiplicative) |
|---|---|---|
| Trivial-axis case | $N$ prime | $(\mathbb Z/N)^\times$ cyclic ($N\in\{2,4,p^a,2p^a\}$, $p$ odd) |
| Local depth source | $p$-adic filtration on $\mathbb Z/p^a$, every $p$ | $p$-adic chain (odd $p$); 2-adic anomaly (only $p=2$) |
| First non-cyclic case | — (additive $\mathbb Z/N$ is always cyclic) | $N=8$ (intra-prime $V_4$) |
| First cross-prime case | $N=6$ | $N=12$ (cross-prime $V_4$) |
| Cross-axis obstruction | cross-prime ANOVA on $\prod\mathbb Z/p_i^{a_i}$ | cross-prime ANOVA on $\prod(\mathbb Z/p_i^{a_i})^\times$ |

### 3.4 Intra-prime vs cross-prime non-cyclicity: the conductor signature

The cleanest diagnostic separating the two layers is the **conductor signature** — the multiset of conductors of the non-principal characters.

- At $N=8$ the three non-principal characters have conductors $\{4,8,8\}$, all powers of the single prime $2$ (§6.2): the Klein four-group is built entirely inside the prime $2$.
- At $N=12$ the three non-principal characters have conductors $\{4,3,12\}$ — one supported at the prime $2$ (conductor $4$), one at the prime $3$ (conductor $3$), and their cross-prime product (conductor $12$, §6.8): the Klein four-group is assembled from two distinct primes.

Both groups are abstractly $V_4$, but the conductor signature distinguishes them, and it is exactly the data that controls the apex. A ledger separable across the CRT primes factorizes $\mathcal D_x$ at $N=12$ — the conductor-$4$ and conductor-$3$ characters belong to different Euler factors — whereas at $N=8$ there is only one prime and no cross-prime factorization to be had: the entire $V_4$ interaction is local 2-adic depth. **$N=8$ and $N=12$ are the two minimal anchors of the multiplicative sector**, realizing the same $V_4$ through the local and the global layer respectively; T0's single anchor $N=6$ sees only the global layer.

---

## 4. The Gauss-sum bridge to T0

### 4.1 Gauss sums

The classical **Gauss sum** associated to a Dirichlet character $\psi$ mod $N$ and an integer $a$ is
$$\tau(\psi,a):=\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\,e^{2\pi ias/N}=\sum_{s\in(\mathbb Z/N)^\times}\psi(s)\chi_a(s),$$
mixing a multiplicative character $\psi$ with an additive character $\chi_a$ on the same underlying set.

The magnitude depends on primitivity (developed in §1.3). For **primitive** $\psi$ mod $N$,
$$|\tau(\psi,a)|=\sqrt N\ \ (\gcd(a,N)=1),\qquad\tau(\psi,a)=\overline{\psi(a)}\,\tau(\psi,1),\qquad\tau(\psi,a)=0\ \ (\gcd(a,N)>1)$$
(Iwaniec–Kowalski 2004, §3.4–3.5; Davenport 2000; Montgomery 1971). For **induced** (non-primitive) $\psi$ the magnitude follows the induction formula and is in general strictly smaller — possibly zero (§1.3). This is the case the bridge of §4.2 must track, since it sums over *all* characters $\psi$ at a fixed additive index $a$.

### 4.2 The bridge

**Theorem 4.1 (Gauss-sum Fourier-inversion bridge).** For any function $f:(\mathbb Z/N)^\times\to\mathbb C$ and any $a\in\widehat{\mathbb Z/N}$,
$$\boxed{\sum_{s\in(\mathbb Z/N)^\times}f(s)\,\overline{\chi_a(s)}=\frac{1}{\varphi(N)}\sum_{\psi\in\widehat{(\mathbb Z/N)^\times}}\overline{\tau(\psi,a)}\,\Big(\sum_{s\in(\mathbb Z/N)^\times}f(s)\,\psi(s)\Big).}$$
In particular, for $f=x^\beta$ with positive ledger $x:(\mathbb Z/N)^\times\to\mathbb R_{>0}$ and $\beta\in\mathbb C$,
$$\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\chi_a(s)}=\sum_{\psi\in\widehat{(\mathbb Z/N)^\times}}\overline{\tau(\psi,a)}\,\widehat{x^\beta}_{\bar\psi}\qquad\text{(with $\widehat{x^\beta}_\psi$ as in Definition 2.1).}$$

**Proof.** Restricted to $(\mathbb Z/N)^\times$, the additive character $\overline{\chi_a(s)}$ is a function that expands in the multiplicative Fourier basis $\{\psi:\psi\in\widehat{(\mathbb Z/N)^\times}\}$:
$$\overline{\chi_a(s)}=\sum_{\psi\in\widehat{(\mathbb Z/N)^\times}}c_\psi\,\psi(s),\qquad c_\psi=\frac{1}{\varphi(N)}\sum_{t\in(\mathbb Z/N)^\times}\overline{\chi_a(t)}\,\overline{\psi(t)}=\frac{\overline{\tau(\psi,a)}}{\varphi(N)},$$
using $\overline{\sum_t\psi(t)\chi_a(t)}=\overline{\tau(\psi,a)}$. Substituting into the left-hand side,
$$\sum_s f(s)\,\overline{\chi_a(s)}=\sum_s f(s)\cdot\frac{1}{\varphi(N)}\sum_\psi\overline{\tau(\psi,a)}\,\psi(s)=\frac{1}{\varphi(N)}\sum_\psi\overline{\tau(\psi,a)}\sum_s f(s)\psi(s),$$
which is the boxed identity. For $f=x^\beta$, the inner sum $\sum_s x_s^\beta\psi(s)=\varphi(N)\widehat{x^\beta}_{\bar\psi}$ (by Definition 2.1, with $\bar\psi$ in the conjugate slot of $\overline{(\bar\psi)}=\psi$); substituting collapses the $1/\varphi(N)$ factor and yields the second form. $\square$

### 4.3 Apex-level bridge

**Corollary 4.2 (Apex bridge).** Let $x:\mathbb Z/N\to\mathbb R_{>0}$ be a positive ledger on all of $\mathbb Z/N$, with both apex generators $\mathcal M_x(\beta,a)$ (T0, additive, normalized by $G(x)=(\prod_{s\in\mathbb Z/N}x_s)^{1/N}$) and $\mathcal D_x(\beta,\psi)$ (T8, multiplicative, normalized by $G_\times(x)=(\prod_{s\in(\mathbb Z/N)^\times}x_s)^{1/\varphi(N)}$) defined. The **unit-restricted** contribution to the additive apex,
$$\mathcal M_x^{\text{unit}}(\beta,a):=G(x)^{-\beta}\cdot\frac{1}{N}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\chi_a(s)},$$
satisfies the exact relation
$$\boxed{\mathcal M_x^{\text{unit}}(\beta,a)=\frac{\varphi(N)}{N}\cdot\Big(\frac{G_\times(x)}{G(x)}\Big)^\beta\cdot\frac{1}{\varphi(N)}\sum_{\psi\in\widehat{(\mathbb Z/N)^\times}}\overline{\tau(\psi,a)}\,\mathcal D_x(\beta,\bar\psi).}$$

The full additive apex decomposes as
$$\mathcal M_x(\beta,a)=\mathcal M_x^{\text{unit}}(\beta,a)+\mathcal M_x^{\text{non-unit}}(\beta,a),$$
where $\mathcal M_x^{\text{non-unit}}(\beta,a)=G(x)^{-\beta}\cdot\frac{1}{N}\sum_{s\notin(\mathbb Z/N)^\times}x_s^\beta\overline{\chi_a(s)}$ depends only on the ledger values at non-units, which are *not* encoded in the multiplicative apex. The multiplicative apex therefore reconstructs precisely the **unit-restricted** half of the additive apex via the Gauss-sum-weighted formula above; the non-unit half is independent information.

**Proof.** Substitute the second form of Theorem 4.1 into $\mathcal M_x^{\text{unit}}(\beta,a)=G(x)^{-\beta}\cdot\frac{1}{N}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\overline{\chi_a(s)}$:
$$\mathcal M_x^{\text{unit}}(\beta,a)=\frac{G(x)^{-\beta}}{N}\sum_\psi\overline{\tau(\psi,a)}\widehat{x^\beta}_{\bar\psi}=\frac{G(x)^{-\beta}}{N}\sum_\psi\overline{\tau(\psi,a)}\cdot G_\times(x)^\beta\mathcal D_x(\beta,\bar\psi),$$
using $\widehat{x^\beta}_\psi=G_\times(x)^\beta\mathcal D_x(\beta,\psi)$ (Definition 2.1). Pulling out $G_\times(x)^\beta/G(x)^\beta=(G_\times(x)/G(x))^\beta$ and recognizing $1/N=(\varphi(N)/N)\cdot(1/\varphi(N))$ gives the boxed formula. The additive decomposition $\mathcal M_x=\mathcal M_x^{\text{unit}}+\mathcal M_x^{\text{non-unit}}$ is by linearity of the character sum, partitioning $\mathbb Z/N$ into units and non-units. $\square$

The **geometric-mean ratio** $G_\times(x)/G(x)$ is the explicit factor measuring the discrepancy between the units-only and all-labels geometric centers. By the elementary identity $G(x)^N=G_\times(x)^{\varphi(N)}\cdot G_{\text{nu}}(x)^{N-\varphi(N)}$ (where $G_{\text{nu}}$ is the geometric mean over non-units, well-defined whenever the non-unit set is non-empty — i.e., for every $N\ge 2$),
$$\frac{G_\times(x)}{G(x)}=\Big(\frac{G_\times(x)}{G_{\text{nu}}(x)}\Big)^{(N-\varphi(N))/N},$$
a function of the relative scale of unit and non-unit ledger values. The geometric-mean factor $(G_\times/G)^\beta$ in the bridge equals $1$ precisely when $G_\times(x)=G_{\text{nu}}(x)$, i.e., when the geometric mean over units agrees with the geometric mean over non-units. For prime $N$, the non-unit set is the singleton $\{0\}$, so $G_{\text{nu}}(x)=x_0$ and the condition $G_\times=G$ becomes $x_0=G_\times(x)$ — a special condition rather than an automatic one; only the leading $\varphi(N)/N=(N-1)/N$ prefactor then survives (it is never $1$ for $N\ge 2$, since $\mathbb Z/N$ always contains the non-unit $0$).

### 4.4 Why Gauss sums are the natural bridge

The precise sense in which Gauss sums bridge the two sectors is Theorem 4.1: the coefficient expressing the unit-restricted additive character $\overline{\chi_a}\big|_{(\mathbb Z/N)^\times}$ in the Dirichlet-character basis is exactly $c_\psi=\overline{\tau(\psi,a)}/\varphi(N)$. Thus $\{\tau(\psi,a)\}_\psi$ is the change-of-basis between the additive and multiplicative Fourier bases on the units — the natural intertwiner of the two apex generators of T0 (additive) and T8 (multiplicative). For non-primitive $\psi$ the coefficient $c_\psi$ can vanish (§1.3), so a given additive character $\chi_a$ expands only over the multiplicative characters whose Gauss sum $\tau(\psi,a)$ is non-zero.

This bridge is **structural** — an exact change of basis on the $\varphi(N)$-dimensional space of functions on units — and not in itself a source of analytic leverage: as T9.4.1 §5.3 shows, the bilateral identity collapses to Parseval on units via Helmert orthonormality. Its value is organizational, positioning $\tau(\psi,a)$ as the explicit dictionary between the two sectors; the genuine analytic content — the Gauss-sum decomposition of conductor blocks and the bilateral factorization $UW=D^{\mathrm{rad}}V^{\mathrm{Gauss}}$ — is developed in T9.4.

The classical literatures emphasizing this connection include:
- **Dirichlet's theorem on primes in arithmetic progressions** (the original motivation for Dirichlet $L$-functions, which combine multiplicative characters with additive structure on the natural numbers).
- **The Davenport–Hasse relations** for Gauss sums in extensions of finite fields, which provide a multiplicative theory paralleling the simple multiplicative structure on $(\mathbb Z/N)^\times$ for our finite categorical case.
- **The Bombieri–Vinogradov theorem** and the **large sieve**, which use both additive and multiplicative Fourier analysis on $\mathbb Z/N$ together with Gauss-sum estimates.

T8's structural contribution is to position $\tau(\psi,a)$ explicitly as the **bridge** between the two apex generators of the categorical-simplex apex framework, rather than as an isolated arithmetic quantity.

---

## 5. Finite Dirichlet polynomials and finite $L$-function analogs

### 5.1 The finite Dirichlet polynomial

The **classical Dirichlet $L$-function** attached to a Dirichlet character $\chi$ mod $N$ is
$$L(s,\chi)=\sum_{n=1}^\infty\frac{\chi(n)}{n^s}=\prod_p\Big(1-\frac{\chi(p)}{p^s}\Big)^{-1},$$
defined for $\Re(s)>1$ and continuable to a meromorphic function on $\mathbb C$. The classical RH-shaped question asks whether the non-trivial zeros lie on the critical line $\Re(s)=1/2$ (generalized RH for $L$-functions).

The **finite analog** truncates the sum to a finite set, or equivalently works on a finite group. We propose:

**Definition 5.1 (Finite Dirichlet polynomial).** Given a positive ledger $x:\{1,2,\ldots,N\}\to\mathbb R_{>0}$ (or equivalently $x:\mathbb Z/N\to\mathbb R_{>0}$ with the natural representative) and a Dirichlet character $\chi$ mod $N$ (extended to all integers by $\chi(n)=0$ for $\gcd(n,N)>1$ and $\chi(n+N)=\chi(n)$), the **finite Dirichlet polynomial** is
$$L_x(\beta,\chi):=\sum_{n=1}^N\frac{\chi(n)}{x_n^\beta}.$$

The classical case $x_n=n$ recovers the truncation $L_x(\beta,\chi)=\sum_{n=1}^N\chi(n)/n^\beta$, the partial sum of the Dirichlet $L$-function.

### 5.2 Relation to the multiplicative apex

**Proposition 5.2.** For ledger $x_n=n$ (the standard arithmetic ledger),
$$L_x(\beta,\chi)=\sum_{n=1}^N\frac{\chi(n)}{n^\beta}=\sum_{s\in(\mathbb Z/N)^\times}\frac{\chi(s)}{s^\beta},$$
since $\chi(n)=0$ for $\gcd(n,N)>1$. Comparing to Definition 2.1 with $x_s=s$ and substituting $\beta\to-\beta$ (since the apex uses $x_s^\beta$ while the $L$-function uses $n^{-\beta}$),
$$L_x(-\beta,\chi)=\sum_{s\in(\mathbb Z/N)^\times}\chi(s)\,s^\beta=\varphi(N)\cdot G(s)^\beta\,\mathcal D_s(\beta,\bar\chi),$$
where $G(s)=(\prod_{s\in(\mathbb Z/N)^\times}s)^{1/\varphi(N)}$ is the geometric mean of the units.

So the finite Dirichlet polynomial $L_x(-\beta,\chi)$ at sign-flipped $\beta$ is, up to the geometric-mean normalization, the multiplicative apex evaluated at the conjugate character.

### 5.3 RH-shaped questions

The classical Dirichlet $L$-function $L(s,\chi)$ has its non-trivial zeros conjecturally on the critical line $\Re(s)=1/2$ (GRH). The finite analog $L_x(\beta,\chi)=\sum_{n=1}^N\chi(n)x_n^{-\beta}$ is a finite **exponential sum** $\sum_n\chi(n)e^{-\beta\log x_n}$ — entire in $\beta$, a Dirichlet polynomial — with finitely many zeros in $\beta\in\mathbb C$. (It is a genuine polynomial in $e^{-\beta}$ only for geometric ledgers $x_n=c^{\,n}$; for $x_n=n$ the frequencies $\log n$ are incommensurable, so it is a true exponential sum.)

**Forward question.** For the arithmetic ledger $x_n=n$, where do the zeros of $L_x(\beta,\chi)$ — equivalently of the multiplicative apex $\mathcal D_s(\beta,\bar\chi)$ on units (Proposition 5.2) — lie in $\beta\in\mathbb C$?

**A scoping caveat.** One should not expect a finite "critical line" for free. The finite truncation carries no normalization — no functional equation, no Euler product — forcing its finitely many zeros onto any line; §7.3 makes this precise and explains that the RH-content is purchased not by passing from additive to multiplicative characters but by a *change of base ring* to function fields $\mathbb F_q(t)$, where Weil's theorem turns the critical line into a theorem. The arithmetically load-bearing object over $\mathbb Q$ is therefore the **genuine** $L(s,\chi)$ (and its logarithmic derivative $-\sum_n\Lambda(n)\chi(n)n^{-s}$), not the finite polynomial; the finite apex is its structural shadow. The first concrete positivity statement in this lineage — Stieltjes positivity of the prime-side multiplicative apex at primorial scale, conditional on GRH — is established in T8.4, which uses the multiplicative selection rule (Theorem 2.4) and the Gauss-sum bridge (Corollary 4.2) of the present paper.

This is the precise finite-categorical formulation of the GRH-shaped questions in the T-program (T0 §6.7), developed as the forward door §7.3.

---

## 6. Worked examples: $N=8$ (intra-prime) and $N=12$ (cross-prime)

### 6.1 The unit group at $N=8$

$(\mathbb Z/8)^\times=\{1,3,5,7\}$. Multiplication table modulo $8$:

| $\cdot$ | $1$ | $3$ | $5$ | $7$ |
|---|---|---|---|---|
| $1$ | $1$ | $3$ | $5$ | $7$ |
| $3$ | $3$ | $1$ | $7$ | $5$ |
| $5$ | $5$ | $7$ | $1$ | $3$ |
| $7$ | $7$ | $5$ | $3$ | $1$ |

Every non-identity element has order $2$ (since $3^2=9\equiv 1$, $5^2=25\equiv 1$, $7^2=49\equiv 1$). Hence $(\mathbb Z/8)^\times\cong\mathbb Z/2\times\mathbb Z/2$, the **Klein four-group** $V_4$ — the smallest non-cyclic abelian group.

### 6.2 The four Dirichlet characters mod $8$

The dual group $\widehat{(\mathbb Z/8)^\times}\cong V_4$ has four elements, all of order $1$ or $2$, all real-valued ($\psi(s)\in\{\pm 1\}$). Explicitly, with the standard Kronecker-symbol labels:

| | $\psi(1)$ | $\psi(3)$ | $\psi(5)$ | $\psi(7)$ | Kernel | Conductor |
|---|---|---|---|---|---|---|
| $\psi_0$ (principal) | $+1$ | $+1$ | $+1$ | $+1$ | $\{1,3,5,7\}$ | $1$ |
| $\chi_{-4}=(-4/\cdot)$ | $+1$ | $-1$ | $+1$ | $-1$ | $\{1,5\}$ | $4$ |
| $\chi_{8}=(8/\cdot)$ | $+1$ | $-1$ | $-1$ | $+1$ | $\{1,7\}$ | $8$ |
| $\chi_{-8}=\chi_{-4}\chi_8=(-8/\cdot)$ | $+1$ | $+1$ | $-1$ | $-1$ | $\{1,3\}$ | $8$ |

The three non-trivial characters are the **mod-4 character** $\chi_{-4}=(-1/\cdot)$ on odd integers — the *unique* one of conductor $4$, as it is the only character constant on residues mod $4$ (it cannot separate $1$ from $5$) and the character of $\mathbb Q(i)$; the **primitive even character** $\chi_8=(2/\cdot)$ of conductor $8$, character of $\mathbb Q(\sqrt2)$; and their product $\chi_{-8}=(-2/\cdot)$ of conductor $8$, character of $\mathbb Q(\sqrt{-2})$. The two conductor-$8$ characters $\chi_8,\chi_{-8}$ each separate $1$ from $5$ (both $\equiv1\bmod4$), so neither factors through mod $4$; this is why the conductor signature is $\{4,8,8\}$, all powers of the single prime $2$ (§3.4).

### 6.3 The multiplicative apex at $N=8$

For a positive ledger $x:(\mathbb Z/8)^\times\to\mathbb R_{>0}$ with components $x_1,x_3,x_5,x_7$, the centered log-ledger is
$$y_s=\log x_s-\tfrac{1}{4}\log(x_1x_3x_5x_7),\qquad s\in\{1,3,5,7\},$$
with $y_1+y_3+y_5+y_7=0$.

The multiplicative apex generator at each Dirichlet character:
$$\mathcal D_x(\beta,\psi_0)=\tfrac{1}{4}\big(e^{\beta y_1}+e^{\beta y_3}+e^{\beta y_5}+e^{\beta y_7}\big),$$
$$\mathcal D_x(\beta,\chi_{-4})=\tfrac{1}{4}\big(e^{\beta y_1}-e^{\beta y_3}+e^{\beta y_5}-e^{\beta y_7}\big),$$
$$\mathcal D_x(\beta,\chi_8)=\tfrac{1}{4}\big(e^{\beta y_1}-e^{\beta y_3}-e^{\beta y_5}+e^{\beta y_7}\big),$$
$$\mathcal D_x(\beta,\chi_{-8})=\tfrac{1}{4}\big(e^{\beta y_1}+e^{\beta y_3}-e^{\beta y_5}-e^{\beta y_7}\big).$$

The four character sums together form the multiplicative Fourier decomposition of the apex on $(\mathbb Z/8)^\times$.

### 6.4 The selection rule at $N=8$

The dual group $\widehat{(\mathbb Z/8)^\times}\cong V_4$ has multiplication table identical to the Klein four-group:
$$\chi_{-4}^2=\chi_8^2=\chi_{-8}^2=\psi_0,\qquad\chi_{-4}\chi_8=\chi_{-8},\qquad\chi_{-4}\chi_{-8}=\chi_8,\qquad\chi_8\chi_{-8}=\chi_{-4}.$$

For the closure diagonal at integer $m=2$, the selection rule $\chi_1\chi_2=\psi$ has the following solutions in $V_4$:

| Target $\psi$ | Solutions $(\chi_1,\chi_2)$ |
|---|---|
| $\psi_0$ | $(\psi_0,\psi_0),(\chi_{-4},\chi_{-4}),(\chi_8,\chi_8),(\chi_{-8},\chi_{-8})$ |
| $\chi_{-4}$ | $(\psi_0,\chi_{-4}),(\chi_{-4},\psi_0),(\chi_8,\chi_{-8}),(\chi_{-8},\chi_8)$ |
| $\chi_8$ | $(\psi_0,\chi_8),(\chi_8,\psi_0),(\chi_{-4},\chi_{-8}),(\chi_{-8},\chi_{-4})$ |
| $\chi_{-8}$ | $(\psi_0,\chi_{-8}),(\chi_{-8},\psi_0),(\chi_{-4},\chi_8),(\chi_8,\chi_{-4})$ |

Each target character has exactly $|V_4|=4$ ordered pairs of factors — uniform over $\psi$, reflecting the Klein-four-group structure. This is qualitatively different from the additive selection rule of T0 at $N=8$ (where the additive group $\mathbb Z/8$ is cyclic and the additive selection rule $a+b\equiv c\pmod 8$ has $8$ ordered pairs per target $c$).

### 6.5 Cross-axis interaction at $N=8$

Since $(\mathbb Z/8)^\times\cong\mathbb Z/2\times\mathbb Z/2$, ledgers on $(\mathbb Z/8)^\times$ decompose by the structure-theorem axes. Identifying $\mathbb Z/2\times\mathbb Z/2$ via $1\leftrightarrow(0,0)$, $7\leftrightarrow(0,1)$, $3\leftrightarrow(1,0)$, $5\leftrightarrow(1,1)$ (one choice; the identification is not canonical), the ANOVA decomposition of the centered log-ledger is
$$y=y^{(\{1\})}+y^{(\{2\})}+y^{(\{1,2\})},$$
where:
- $y^{(\{1\})}$ depends only on the first $\mathbb Z/2$ coordinate (separating $\{1,7\}$ from $\{3,5\}$ — i.e., the kernel of $\chi_8$);
- $y^{(\{2\})}$ depends only on the second $\mathbb Z/2$ coordinate (separating $\{1,3\}$ from $\{5,7\}$ — i.e., the kernel of $\chi_{-8}$);
- $y^{(\{1,2\})}$ is the cross-axis interaction term.

A ledger $y$ is separable across cyclic factors iff $y^{(\{1,2\})}=0$. By Theorem 3.1, separability iff the apex factorizes:
$$\mathcal D_x(\beta,\psi)=\mathcal D^{(1)}_{x^{(1)}}(\beta,\psi_1)\cdot\mathcal D^{(2)}_{x^{(2)}}(\beta,\psi_2)$$
with $\psi=\psi_1\psi_2$ in the cyclic-factor decomposition of $\widehat{(\mathbb Z/8)^\times}\cong\mathbb Z/2\times\mathbb Z/2$.

**The $N=8$ case is the smallest non-trivial cross-axis multiplicative apex** — but its cross-axis structure is *intra-prime*: both cyclic factors sit inside the prime $2$ (§3.3), so the factorization above is over structure-theorem cyclic factors, not an Euler product over distinct primes. The genuine cross-prime analog of T0's $N=6$ is $N=12$ (§6.8), where the two factors live at different primes.

### 6.6 Apex on the structural ledger $x_s=s$

A canonical arithmetic ledger on $(\mathbb Z/8)^\times$: $x_s=s$ for $s\in\{1,3,5,7\}$ — the residue-class representatives themselves.

$G(x)=(1\cdot 3\cdot 5\cdot 7)^{1/4}=105^{1/4}\approx 3.202$.

Centered log-ledger ($\tfrac14\log 105\approx 1.16349$):
$y_1=\log 1-\tfrac{1}{4}\log 105\approx -1.1635$
$y_3=\log 3-\tfrac{1}{4}\log 105\approx -0.0649$
$y_5=\log 5-\tfrac{1}{4}\log 105\approx 0.4460$
$y_7=\log 7-\tfrac{1}{4}\log 105\approx 0.7824$

Sum: $\sum_s y_s=\log(1\cdot 3\cdot 5\cdot 7)-\log 105=0$ as required by centering. (Equivalently $y_3=\tfrac14\log\tfrac{27}{35}$ and $y_7=\tfrac14\log\tfrac{343}{15}$.)

The closure diagonal at $\beta=1$ (the "linear arithmetic Dirichlet" rung), ordered as in the table of §6.2:
$$\mathcal D_x(1,\psi_0)=\tfrac{1}{4}\big(1+3+5+7\big)/G(x)=16/(4\cdot 105^{1/4})=4/105^{1/4}\approx 1.249,$$
$$\mathcal D_x(1,\chi_{-4})=\tfrac{1}{4}\big(1-3+5-7\big)/G(x)=-4/(4\cdot 105^{1/4})=-1/105^{1/4}\approx -0.313,$$
$$\mathcal D_x(1,\chi_8)=\tfrac{1}{4}\big(1-3-5+7\big)/G(x)=0,$$
$$\mathcal D_x(1,\chi_{-8})=\tfrac{1}{4}\big(1+3-5-7\big)/G(x)=-8/(4\cdot 105^{1/4})=-2/105^{1/4}\approx -0.625.$$

The vanishing $\mathcal D_x(1,\chi_8)=0$ at the structural ledger is the multiplicative version of an arithmetic "coincidence" — the sum $1-3-5+7=0$ for the character $\chi_8$. (Equivalently, $\chi_8(1)\cdot 1+\chi_8(3)\cdot 3+\chi_8(5)\cdot 5+\chi_8(7)\cdot 7=1-3-5+7=0$.) Such vanishings encode arithmetic information about the residue-class structure.

### 6.7 $N=8$ as the intra-prime anchor

$N=8$ provides the smallest worked example of:
- Non-cyclic $(\mathbb Z/N)^\times$ (the Klein four-group), arising **intra-prime** from the 2-adic anomaly;
- Non-trivial multiplicative selection rule (the $V_4$ structure);
- Two-dimensional local conductor depth, conductor signature $\{4,8,8\}$ (all 2-power, §3.4) — the multiplicative analog of T0's *prime-power depth*, not of its cross-prime ANOVA;
- Arithmetic structural ledger with non-trivial Dirichlet character sums (including the vanishing $\mathcal D_x(1,\chi_8)=0$);
- Bridge to T0's additive apex on the same underlying $\mathbb Z/8$ (where the additive sector is cyclic $\mathbb Z/8$, qualitatively different from the multiplicative $V_4$).

$N=8$ is the intra-prime anchor; the cross-prime anchor $N=12$ (§6.8) is the genuine analog of T0's $N=6$. Together they are T8's two canonical worked examples.

### 6.8 Cross-prime contrast: $N=12$

$(\mathbb Z/12)^\times=\{1,5,7,11\}$, with $5^2\equiv7^2\equiv11^2\equiv1\pmod{12}$: every non-identity element has order $2$, so $(\mathbb Z/12)^\times\cong V_4$ — abstractly the same Klein four-group as $(\mathbb Z/8)^\times$. But here the group is **cross-prime**. CRT gives
$$(\mathbb Z/12)^\times\cong(\mathbb Z/4)^\times\times(\mathbb Z/3)^\times\cong\mathbb Z/2\times\mathbb Z/2,$$
the first $\mathbb Z/2$ supported at the prime $2$ (generated by $-1\equiv3\bmod4$), the second at the prime $3$ (generated by $-1\equiv2\bmod3$). Under $s\leftrightarrow(s\bmod4,\,s\bmod3)$:
$$1\leftrightarrow(1,1),\quad 5\leftrightarrow(1,2),\quad 7\leftrightarrow(3,1),\quad 11\leftrightarrow(3,2).$$

**The four Dirichlet characters mod $12$** are products $\psi=\psi^{(2)}\psi^{(3)}$ of a character of $(\mathbb Z/4)^\times$ and one of $(\mathbb Z/3)^\times$:

| | $\psi(1)$ | $\psi(5)$ | $\psi(7)$ | $\psi(11)$ | Supported at | Conductor |
|---|---|---|---|---|---|---|
| $\psi_0$ | $+1$ | $+1$ | $+1$ | $+1$ | — | $1$ |
| $\chi_{-4}=(-4/\cdot)$ | $+1$ | $+1$ | $-1$ | $-1$ | prime $2$ | $4$ |
| $\chi_{-3}=(-3/\cdot)$ | $+1$ | $-1$ | $+1$ | $-1$ | prime $3$ | $3$ |
| $\chi_{12}=\chi_{-4}\chi_{-3}=(12/\cdot)$ | $+1$ | $-1$ | $-1$ | $+1$ | both | $12$ |

The conductor signature is $\{4,3,12\}$: one character at each prime and their cross-prime product, in contrast to $N=8$'s $\{4,8,8\}$. Here $\chi_{-4}$ depends only on $s\bmod4$ (character of $\mathbb Q(i)$), $\chi_{-3}$ only on $s\bmod3$ (the quadratic character mod $3$, character of $\mathbb Q(\sqrt{-3})$), and $\chi_{12}$ is the cross-prime product (character of $\mathbb Q(\sqrt3)$).

**Separability is genuinely cross-prime.** A ledger $y$ on $(\mathbb Z/12)^\times$ is separable iff $y(s)=y^{(2)}(s\bmod4)+y^{(3)}(s\bmod3)$, and then the apex Euler-factorizes over the two primes,
$$\mathcal D_x(\beta,\psi)=\mathcal D^{(2)}_{x^{(2)}}(\beta,\psi^{(2)})\cdot\mathcal D^{(3)}_{x^{(3)}}(\beta,\psi^{(3)}),$$
with $\chi_{-4}$ and $\chi_{-3}$ living in *different* Euler factors (Theorem 3.1). This is the exact multiplicative analog of T0's $N=6$ cross-prime ANOVA — impossible at $N=8$, where there is only one prime.

**Structural ledger $x_s=s$.** With $G=(1\cdot5\cdot7\cdot11)^{1/4}=385^{1/4}\approx4.430$, the closure diagonal at $\beta=1$:
$$\mathcal D_x(1,\psi_0)=\tfrac14(1+5+7+11)/G=6/385^{1/4}\approx1.354,$$
$$\mathcal D_x(1,\chi_{-4})=\tfrac14(1+5-7-11)/G=-3/385^{1/4}\approx-0.677,$$
$$\mathcal D_x(1,\chi_{-3})=\tfrac14(1-5+7-11)/G=-2/385^{1/4}\approx-0.451,$$
$$\mathcal D_x(1,\chi_{12})=\tfrac14(1-5-7+11)/G=0.$$
As at $N=8$, the top character vanishes on the structural ledger: $1-5-7+11=0$. The two anchors thus give the same abstract $V_4$ apex with the same kind of arithmetic vanishing, but the vanishing sits on the intra-prime conductor-$8$ character $\chi_8$ at $N=8$ and on the cross-prime conductor-$12$ character $\chi_{12}$ at $N=12$ — the conductor signature is what tells them apart.

---

## 7. Forward doors

The doors below are scoped as forward content; T8 commits to none of them as main claims.

### 7.1 Kloosterman sums and the multiplicative cubic vertex

T3 established the additive cubic vertex selection rule $a+b+c\equiv 0\pmod N$ for the third-order Amari–Chentsov tensor at the uniform. The multiplicative analog is the cubic vertex selection rule $\chi_1\chi_2\chi_3=\psi_0$ in $\widehat{(\mathbb Z/N)^\times}$, i.e., the constraint that three Dirichlet characters multiply to the principal character. **Kloosterman sums**
$$K(a,b;N)=\sum_{s\in(\mathbb Z/N)^\times}\chi_a(s)\chi_b(s^{-1}),$$
which mix multiplicative inversion with additive characters, are the natural arithmetic quantities at this rung. The classical Weil bound $|K(a,b;N)|\le 2\sqrt N$ ($N$ prime, $\gcd(a,b,N)=1$) is a fundamental result of finite Fourier analysis whose categorical-simplex interpretation lives in T8's cubic-vertex apex.

Forward paper title (planned): **T8.1 — Kloosterman Sums and the Multiplicative Cubic Vertex.**

### 7.2 Davenport–Hasse relations and lifts to finite-field extensions

The classical Davenport–Hasse relation gives the behavior of Gauss sums under lifts $\mathbb F_q\to\mathbb F_{q^n}$: $\tau(\psi^{(n)},\chi^{(n)})=(-1)^{n-1}\tau(\psi,\chi)^n$. The categorical-simplex analog would relate the multiplicative apex on $(\mathbb Z/N)^\times$ to that on $(\mathbb Z/N^k)^\times$ for $k\ge 2$ — a "tower of multiplicative apexes" with explicit transfer relations.

Forward paper title (planned): **T8.2 — The Davenport–Hasse Tower for Multiplicative Apexes.**

### 7.3 RH-shaped questions for finite Dirichlet polynomials

The natural setting for RH-shaped questions in the T-program is the multiplicative apex: for an arithmetic ledger $x$ (such as $x_s=s$ on units, or $x_s$ = characteristic function of primes mod $N$, or $x_s$ = Möbius function on units, etc.), where do the zeros of $\mathcal D_x(\beta,\psi)$ in $\beta\in\mathbb C$ lie? When do they cluster on a critical line $\Re(\beta)=\beta_0$ for some $\beta_0$? The classical GRH is the statement that the zeros of the infinite Dirichlet $L$-functions lie on $\Re(s)=1/2$; the finite analog asks for the corresponding statement on the categorical simplex.

**Where the critical line is a conjecture, and where it is a theorem.** A scoping distinction governs this door. Over $(\mathbb Z/N)^\times$ with $\mathbb Z/N$ the residue ring of the number field $\mathbb Q$, the finite Dirichlet polynomial $L_x(\beta,\chi)$ of §5 (for the arithmetic ledger $x_s=s$) is a truncation of the classical Dirichlet $L$-function over $\mathbb Q$, whose critical-line statement is GRH — a *conjecture* (over $\mathbb Q$ even the strongest unconditional results are partial, e.g. a positive proportion of $\zeta$ zeros on the critical line, Selberg 1942) — while the truncation's own finitely many zeros carry no normalization forcing them onto any line. The additive door of T7 §7.6 over $\mathbb Z/N$ is in the same conjectural regime. The move from additive to multiplicative characters is necessary but not sufficient: it is the *change of base ring* that purchases a theorem. Replace $\mathbb Q$ by a **function field** $\mathbb F_q(t)$, equivalently take multiplicative characters of $\mathbb F_q^\times$ of order dividing $N$ (existing precisely when $N\mid q-1$). The Gauss-sum bridge $\tau(\psi,a)$ of §4 then becomes the genuine $\mathbb F_q$ Gauss sum $\tau_q(\chi)=\sum_{t\in\mathbb F_q^\times}\chi(t)\psi_{\mathrm{add}}(t)$ ($\psi_{\mathrm{add}}$ a fixed nontrivial additive character of $\mathbb F_q$) with $|\tau_q(\chi)|=q^{1/2}$, and the Jacobi sums $J(\chi^a,\chi^b)=\sum_t\chi^a(t)\chi^b(1-t)$ ($|J|=q^{1/2}$ for nontrivial factors of nontrivial product) are the Frobenius eigenvalues on $H^1$ of the Fermat curve $C_N:\ x_0^N+x_1^N+x_2^N=0$ over $\mathbb F_q$ (Weil 1949). The concrete provable-RH object is the finite $L$-function attached to these multiplicative-character amplitudes encoding point-counts,
$$Z(C_N/\mathbb F_q,T)=\exp\!\Big(\sum_{n\ge1}\tfrac{\#C_N(\mathbb F_{q^n})}{n}T^n\Big)=\frac{P(T)}{(1-T)(1-qT)},\quad P(T)=\prod_{i=1}^{2g}(1-\alpha_iT),\ \ g=\tfrac{(N-1)(N-2)}{2},$$
with $\#C_N(\mathbb F_{q^n})=q^n+1-\sum_i\alpha_i^n$ and inverse roots $\alpha_i$ the Jacobi sums. $P(T)$ is a polynomial (rationality: Dwork/Grothendieck), satisfies a functional equation (Poincaré duality), and obeys **Weil's RH for curves** — $|\alpha_i|=q^{1/2}$ (Weil 1948, 1949; Deligne 1974, *Weil II*, in arbitrary dimension) — which under $T=q^{-s}$ is exactly $\Re(s)=1/2$, a theorem. The categorical multiplicative apex $\mathcal D_x(\beta,\psi)$ defined here is the $\mathbb F_q\!\rightsquigarrow\!(\mathbb Z/N)^\times$ shadow of this $L$-function; the program's concrete RH-shaped target is its $\mathbb F_q$ lift, where Weil's theorem replaces conjecture.

Forward paper cluster (in progress): **the RH-shaped program (multiple papers).** The provable-RH target is the **function-field multiplicative apex** above; the conjectural classical target (RH for $\zeta$ over $\mathbb Q$) is the subject of the T20 governed-closure programme, which reaches the Archimedean place by a cofinal lift in place of the Frobenius that makes the function-field critical line free. A first concrete positivity result on the multiplicative apex itself — Stieltjes positivity of the prime-side apex at primorial scale, conditional on GRH — is established in T8.4, built on the selection rule (Theorem 2.4) and Gauss-sum bridge (Corollary 4.2) of the present paper. This cluster overlaps with the additive-side RH-shaped program of T0 §6.7, the holomorphic escort flow now lifted in Proposition 2.6, and the Lee–Yang zero structure of T0 Proposition 2.5 (lifted to the multiplicative sector — forward).

### 7.4 The full bilateral Pontryagin theory

The pair (T0 additive | T8 multiplicative) realizes the **full Pontryagin duality** on the finite group $\mathbb Z/N$: every finite Fourier analysis on $\mathbb Z/N$ uses either the additive characters (T0) or the multiplicative characters on the unit subgroup (T8). A future paper assembling the two into a single **bilateral framework**, with explicit Gauss-sum-mediated transformations between them, would complete the categorical Fourier analysis of the T-program. Partial realization is already in hand: T9.4 establishes the Gauss-sum decomposition of conductor blocks and the bilateral factorization $UW=D^{\mathrm{rad}}V^{\mathrm{Gauss}}$ between the Helmert and character bases.

Forward paper title (planned): **T8.3 — The Bilateral Pontryagin Apex.**

---

## 8. Coda

T0 named the additive apex. T7 lifted it to the complex amplitude space, exhibiting the quantum / Hopf / Kummer structure of finite-dimensional QM as the cover of the categorical simplex. T8 turns the dial in the orthogonal direction: from the additive Fourier of the labels to the multiplicative Fourier of the units. Together the three papers (T0 + T7 + T8) establish the categorical-simplex apex as a four-axis structure:

1. **Gauge axis $\beta$** (T0): the cumulant-and-closure gauge corridor.
2. **Label axis $c$** (T0): additive characters of $\mathbb Z/N$.
3. **Phase axis** (T7): the Hopf-and-toric phase fiber of complex amplitudes.
4. **Unit axis $\psi$** (T8): multiplicative characters of $(\mathbb Z/N)^\times$.

The four-axis apex is the natural home of the categorical-simplex Fourier analysis: T0's cumulant tower and conductor packets, T7's Bloch-sphere phase deformations and Kummer covers, T8's Dirichlet-character sums and Gauss-sum bridges. The RH-shaped questions of the T-program live precisely where the four axes meet — on the integer-$\beta$ closure diagonal of the multiplicative apex with arithmetic ledgers $x$, with phase structure inherited from T7, conductor structure from T0, and Dirichlet-character structure from T8.

The one-sentence apex of T8:

> **The multiplicative apex generator $\mathcal D_x(\beta,\psi)$ on units of $\mathbb Z/N$ is the finite-categorical analog of the Dirichlet $L$-function, obeying the multiplicative selection rule $\chi_1\cdots\chi_n=\psi$ in $\widehat{(\mathbb Z/N)^\times}$ in place of T0's additive selection rule, with the Gauss-sum bridge $\tau(\psi,a)$ intertwining it with T0's additive apex on the same underlying $\mathbb Z/N$.**

And the closing slogan:

> **Additive Fourier knows the labels; multiplicative Fourier knows the units. Gauss sums know both.**

---

## Acknowledgments

The framing in this paper crystallized through extended dialogue with multiple AI collaborators (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, xAI's Grok 4.3). The development of the multiplicative selection rule, the Gauss-sum bridge, and the $N=8$ and $N=12$ structural anchors emerged through a sequence of critique-and-upgrade exchanges that I record transparently. The mathematical content and its correctness are my responsibility.

---

## References

Bombieri, E. (1965). On the large sieve. *Mathematika* 12, 201–225.

Davenport, H. (2000). *Multiplicative Number Theory.* Third edition. Graduate Texts in Mathematics 74. Springer.

Davenport, H. and Hasse, H. (1935). Die Nullstellen der Kongruenzzetafunktionen in gewissen zyklischen Fällen. *Journal für die reine und angewandte Mathematik* 172, 151–182.

Deligne, P. (1974). La conjecture de Weil. I. *Publications Mathématiques de l'IHÉS* 43, 273–307.

Ireland, K. and Rosen, M. (1990). *A Classical Introduction to Modern Number Theory.* Second edition. Graduate Texts in Mathematics 84. Springer. (Gauss and Jacobi sums; Fermat-curve point counts, Ch. 8 & 11.)

Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory.* American Mathematical Society Colloquium Publications 53.

Lang, S. (2002). *Algebra.* Revised third edition. Graduate Texts in Mathematics 211. Springer.

Montgomery, H. L. (1971). *Topics in Multiplicative Number Theory.* Lecture Notes in Mathematics 227. Springer.

Murillo Montero, L. (2026). *T0 — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint, DOI 10.5281/zenodo.20423985.

Murillo Montero, L. (2026). *T3 — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint, DOI 10.5281/zenodo.20339049.

Murillo Montero, L. (2026). *T7 — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo preprint, DOI 10.5281/zenodo.20392442.

Murillo Montero, L. (2026). *T8.4 — Stieltjes Positivity of the Prime-Side Multiplicative Apex at Primorial Scale.* In preparation.

Murillo Montero, L. (2026). *T9 — The Helmert–Fourier Transfer Matrix.* In preparation.

Murillo Montero, L. (2026). *T9.4 — Gauss-Sum Decomposition of the Conductor Blocks.* In preparation.

Murillo Montero, L. (2026). *T9.4.1 — The BV-Variance Helmert–Gauss Algebraic Identity.* In preparation.

Pontryagin, L. S. (1939). *Topological Groups.* Princeton University Press.

Selberg, A. (1942). On the zeros of Riemann's zeta-function. *Skrifter Norske Videnskaps Akademi Oslo* 10, 1–59.

Vinogradov, A. I. (1965). The density hypothesis for Dirichlet $L$-series. *Izvestiya Akademii Nauk SSSR Seriya Matematicheskaya* 29, 903–934.

Weil, A. (1948). On some exponential sums. *Proceedings of the National Academy of Sciences of the USA* 34, 204–207.

Weil, A. (1949). Numbers of solutions of equations in finite fields. *Bulletin of the American Mathematical Society* 55, 497–508.
