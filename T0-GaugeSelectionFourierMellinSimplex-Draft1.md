# \heb{ל}0 — Gauge Selection and the Fourier-Mellin Simplex

**Leonardo Murillo Montero — leonardo.murillo@gmail.com**

*Preprint, version 1.0 — May 24, 2026*

---

> *A statistical theory begins by answering: what is additive?*

---

## Abstract

**Situation.** Information geometry — Rao, Chentsov, Amari, and the modern functional-analytic synthesis of Ay–Jost–Lê–Schwachhöfer (AJLS) — parameterizes statistical models by tensor order $n$ along a single track, treating the choice of representative on each ray of measures as a technical normalization.

**Gap.** That choice is *modeling content*: arithmetic-mean center vs log-density affine vs squared-amplitude additive selects a section of the positive projective cone, and the choice determines which arithmetic, cumulant projection, and classical literature applies. The known cells — Aitchison centered log-ratio (clr) transformation at $r=0$, Fisher–Rao at $r=2$, softmax at $r=1$, harmonic at $r=-1$, tropical at $r=\pm\infty$ — are samples of a single corridor.

**Action.** We name the gauge selection principle, fix the apex generator that encodes the full corridor, and structure the program as a two-axis grid: gauge exponent $\beta$ × cumulant/tensor order $n$. For unstructured labels, the apex is the moment-generating function $K_y(\beta)$ of the centered log-ledger. When labels carry $\mathbb Z/N$ structure, the apex upgrades to the Fourier–Mellin transform
$$\mathcal M_x(\beta,c)=\tfrac{1}{N}\textstyle\sum_{s\in\mathbb Z/N}e^{\beta y_s}\overline{\chi_c(s)},$$
whose $c=0$ mode is $e^{K_y}$, whose Taylor jets at $\beta=0$ are the character-twisted moment/cumulant tensors of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)–[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049), whose integer samples are the [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) power closures, whose Fisher gradient flow is the constant-fitness replicator equation, and whose Chinese Remainder Theorem (CRT) factorization over the primes dividing $N$ stratifies structure into prime-local depth and cross-prime interaction.

**Result.** Six core claims:

1. **Gauge Selection Principle.** Sections of $\mathbb R_{>0}^N/\mathbb R_{>0}^\times$ form the $L^r$ power-mean family ($r\in\mathbb R\cup\{\pm\infty\}$); choosing $r$ chooses the affine substance.
2. **Apex Generators.** $K_y(\beta)=\log\tfrac1N\sum_i e^{\beta y_i}$ is the entire cumulant generator of the centered log-ledger; under $\mathbb Z/N$ structure it upgrades to $\mathcal M_x(\beta,c)$ with $\mathcal M_x(\beta,0)=e^{K_y(\beta)}$.
3. **Two Sampling Diagonals.** Taylor jets at fixed $c$ give the moment/cumulant tower; integer $\beta$ samples give the power-closure tower; both obey $a_1+\cdots+a_n\equiv c\pmod N$ (negative samples via reciprocal-ledger substitution).
4. **$\beta$-Flow.** The escort family $P_\beta\propto e^{\beta y}$ satisfies the constant-fitness replicator equation; $K_y$ is its free energy ($K_y'=\mathbb E_{P_\beta}[y]$, $K_y''=\mathrm{Var}_{P_\beta}(y)\ge 0$).
5. **Prime Decomposition.** For $N=p^a$, the conductor lattice is the $p$-adic depth filtration; for $N$ with multiple distinct prime factors, CRT + analysis-of-variance (ANOVA)/Möbius separate single-axis from cross-axis strata, and $\mathcal M_x$ factorizes exactly when the ledger is separable.
6. **Radical Arithmetic & Anchor.** Helmert normalizers $\sqrt{k(k+1)}$ accumulate into $K_N=\mathbb Q(\sqrt p:p\le N)$ with field growth at prime $N$; $N=6=2\cdot 3$ is the smallest integer with non-trivial cross-prime interaction in $\mathcal M_x$, the canonical multi-prime worked example.

**Harvest.** AJLS's $S^r(\Omega)$ measure powers are the analytic shadow of the corridor; the canonical $n$-tensor on $S^{1/n}$ is the moment-root diagonal; [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s $m$-power conductor mixing is the closure diagonal — visible only when the corridor is named. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) are worked cells; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)–[\heb{ל}10](https://doi.org/10.5281/zenodo.20437847) form a coherent forward program on the same surface. The opening sentence, restated:
$$\boxed{\text{A statistical theory begins by answering: what is additive?}}$$

**Keywords:** information geometry, gauge selection, power means, Fourier–Mellin transform, cumulant tower, Fisher–Rao, Helmert ladder, conductor packets, replicator dynamics, multiquadratic fields, finite $L$-functions.

---

## Notation

We carry the notation of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) and consolidate it.

| Symbol | Meaning |
|---|---|
| $N$ | Number of categorical outcomes, integer $\ge 2$. |
| $\Delta^{N-1}$ | Probability simplex in $\mathbb R^N$. |
| $H_N$ | Mean-zero hyperplane $\{q\in\mathbb R^N:\sum_iq_i=0\}$, dimension $N-1$. |
| $u$ | Uniform distribution $u=(1/N,\ldots,1/N)$. |
| $\mathbb R_{>0}^N$ | Positive cone of $N$-slot ledgers. |
| $G(x)$ | Geometric mean $G(x)=(\prod_i x_i)^{1/N}$. |
| $y$ | Centered log-ledger: $y_i=\log x_i-\frac{1}{N}\sum_j\log x_j$; $\sum_i y_i=0$. |
| $\beta$ | Gauge exponent, real (extended to $\mathbb C$ where holomorphic). |
| $M_r(x)$ | Power mean $(\frac{1}{N}\sum_i x_i^r)^{1/r}$ for $r\ne 0$; $M_0=G$. |
| $S_r(x)$ | $r$-power closure $S_r(x)_i=x_i^r/\sum_j x_j^r$ for $r>0$. |
| $P_\beta$ | Escort distribution $P_\beta(i)=e^{\beta y_i}/\sum_j e^{\beta y_j}$. |
| $K_y(\beta)$ | Unstructured apex generator $K_y(\beta)=\log\frac{1}{N}\sum_i e^{\beta y_i}$. |
| $\kappa_n$ | $n$-th cumulant of the values $y_i$ under the uniform measure. |
| $\chi_c$ | Additive character on $\mathbb Z/N$: $\chi_c(s)=e^{2\pi ics/N}$. |
| $\widehat v_c$ | $c$-th character coefficient of $v\in\mathbb C^N$: $\widehat v_c=\frac{1}{N}\sum_s\overline{\chi_c(s)}v_s$. |
| $\mathrm{cond}(\chi_c)$ | Additive conductor of $\chi_c$, equal to $N/\gcd(c,N)$. |
| $H_d$ | Conductor packet $\mathrm{span}_{\mathbb C}\{\chi_c:\mathrm{cond}(\chi_c)=d\}$. |
| $\mathcal M_x(\beta,c)$ | Structured apex generator (Fourier-Mellin transform). |
| $h_k$ | Unnormalized Helmert ladder vector $(1,\ldots,1,-k,0,\ldots,0)$. |
| $e_k$ | Unit Helmert vector $h_k/\sqrt{k(k+1)}$. |
| $K_N$ | Multiquadratic field $\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$. |
| $P_N$ | Primorial $\prod_{p\le N}p$. |
| $\mathrm{sf}(n)$ | Squarefree kernel of $n$. |

**Acronyms.** Each is expanded on first use in the body; this table is for reference.

| Acronym | Expansion |
|---|---|
| AJLS | Ay–Jost–Lê–Schwachhöfer (modern functional-analytic synthesis of information geometry). |
| ANOVA | Analysis of variance (Hoeffding/Möbius decomposition over the subset lattice). |
| clr | Centered log-ratio transformation (Aitchison). |
| CM | Complex multiplication (number-field property). |
| CRT | Chinese Remainder Theorem. |
| DFT | Discrete Fourier transform. |
| ODE | Ordinary differential equation. |
| RMS | Root mean square ($r=2$ power mean). |

A persistent convention conflict deserves explicit dictionary: in the \heb{ל}-series, the gauge exponent $\beta$ (or $r$, used interchangeably) refers to the $L^r$ power-mean family acting on positive ledgers. In Ay–Jost–Lê–Schwachhöfer's *Information Geometry*, the symbol $r$ refers to the exponent of the Banach space $S^r(\Omega)$ of formal $r$-th powers of signed measures, with $r=1/2$ giving half-densities and $r=1/3$ giving cube-root densities; the order-$n$ canonical AJLS tensor lives on $S^{1/n}$. The two parameters are related by reciprocal duality on the underlying object (ledger vs measure) but are not the same scalar. We use $\beta$ for the \heb{ל}-series gauge exponent throughout and write AJLS-$r$ where the other convention is meant.

---

## 1. The Gauge Selection Principle {#sec:1}

### 1.1 Positive ledgers as projective rays

Let
$$x=(x_1,\ldots,x_N)\in\mathbb R_{>0}^N$$
be a positive ledger of $N$ slots — counts, intensities, weights, rates, amplitudes, conductances, costs. The label set is fixed; the values are positive reals.

The natural scaling action
$$x\mapsto cx,\qquad c>0,$$
acts on the cone. If only the relative pattern $(x_1:x_2:\cdots:x_N)$ matters — as is the case for probability after closure, or for any observable defined up to a scale — then the natural object is the projective ray
$$[x]=\{cx:c>0\}\in\mathbb R_{>0}^N/\mathbb R_{>0}^\times.$$

This quotient is an $(N-1)$-dimensional positive projective manifold. Every ray crosses every standard section exactly once.

### 1.2 Sections are gauges; gauges are observer choices

A **section** of the positive projective cone is a rule for picking one representative from each ray. The classical sections are exactly the level sets of power means (Hardy, Littlewood, and Pólya 1934, Ch. II):
$$\mathcal A_N=\{x:A(x)=1\},\qquad\mathcal G_N=\{x:G(x)=1\},\qquad\mathcal H_N=\{x:H(x)=1\},\qquad\mathcal R_N=\{x:R(x)=1\}.$$

These are the arithmetic, geometric, harmonic, and root-mean-square (RMS) sections respectively. Each can be parameterized by the **power-mean gauge** at exponent $r$:
$$\mathcal G^{(r)}_N=\{x:M_r(x)=1\}=\left\{x:\frac{1}{N}\sum_i x_i^r=1\right\},$$
with the convention $M_0=G$ obtained by the limit.

**Choosing a section is choosing the affine coordinate in which the observer treats the world as linear.**

- Arithmetic gauge: $x$ itself is affine. Mass is additive.
- Geometric gauge: $\log x$ is affine. Multiplicative scale is additive.
- Harmonic gauge: $1/x$ is affine. Reciprocal capacity is additive.
- RMS gauge: $x^2$ is affine. Quadratic intensity is additive.
- General $r$: $x^r$ is affine. The $r$-th-power substance is additive.

This is not nomenclature. The arithmetic mean is the right center exactly when the additive substance is $x$; the harmonic mean is the right center when the additive substance is $1/x$ (period, latency, compliance, parallel resistance); the geometric mean is the right center when $\log x$ is additive (multiplicative growth, compounding); the RMS is the right center when $x^2$ is additive (energy, intensity, Born-rule probability, kinetic energy, squared amplitude). The geometric-gauge case is the foundation of Aitchison's compositional analysis (Aitchison 1986; Pawlowsky-Glahn, Egozcue, and Tolosana-Delgado 2015).

> **Gauge Selection Principle.** *A statistical theory on positive ledgers begins by answering: what is additive? The answer selects a section of the positive projective cone — the gauge — and the choice of section determines which arithmetic, which cumulant projection, and which classical literature applies.*

### 1.3 The gauge corridor

Varying $r$ continuously interpolates between sections. The family
$$\{M_r:r\in\mathbb R\cup\{\pm\infty\}\}$$
forms a one-parameter corridor. We catalog the named rungs.

| $r$ | Gauge name | Additive substance | First classical reading |
|---|---|---|---|
| $+\infty$ | sup / tropical max | dominant coordinate | tropical algebra; large deviations |
| $\vdots$ | | | |
| $3$ | cubic | volume / chirality | $\chi^{(3)}$ nonlinear optics; Waring on cubes |
| $2$ | RMS / quadratic | intensity / amplitude squared | Fisher–Rao; Born rule; energy |
| $1$ | arithmetic | mass | simplex closure; softmax |
| $0$ | geometric | scale / log | Aitchison clr; Amari $e$-flat chart |
| $-1$ | harmonic | reciprocal capacity | softmin; parallel resistance |
| $-2$ | inverse-quadratic | inverse intensity | inverse participation ratio; compliance |
| $-3$ | inverse cubic | inverse volume | dipole-dipole; inverse cube law |
| $\vdots$ | | | |
| $-\infty$ | inf / tropical min | recessive coordinate | tropical algebra; min-plus |

The pair $(r,-r)$ is a polar pair under the involution $x_i\leftrightarrow x_i^{-1}$. The fixed point of the involution is $r=0$, the geometric center. Every classical mean, every named statistical normalization, and several physical observables sit at named integer rungs of this corridor.

### 1.4 Tangent space and dual coordinates

Every section's tangent space at its base point is naturally identified with the mean-zero hyperplane $H_N$. Linearizing $M_r(x)=1$ at the uniform $x=(1,\ldots,1)$ gives
$$\sum_i x_i^{r-1}\,\delta x_i=0\quad\Longrightarrow\quad\sum_i\delta x_i=0\;\text{ at }x=u,$$
so the linearization is the same for every $r$: $T_uM_r^{-1}(1)=H_N$. The gauge corridor parameterizes which non-linear submanifold the ray crosses, but every corridor section has the same tangent space at the uniform — namely $H_N$ — equipped with the bilinear form
$$g_{ij}|_u=p_i\delta_{ij}-p_i p_j|_u=\frac{1}{N}\delta_{ij}-\frac{1}{N^2},$$
which restricted to $H_N$ is the scalar matrix $\frac{1}{N}I_{H_N}$. This is the Fisher information at the uniform, the same in every gauge. It is at off-uniform points that the gauges genuinely diverge.

---

## 2. The Unstructured Apex: $K_y(\beta)$ {#sec:2}

### 2.1 The centered log-ledger

Define
$$y_i=\log x_i-\frac{1}{N}\sum_j\log x_j,\qquad\sum_i y_i=0.$$

The vector $y$ lives in $H_N$ and is invariant under positive scaling of $x$, so it depends only on the ray $[x]$. We call $y$ the **centered log-ledger** of $x$.

The centered log-ledger is the simplicial program's universal coordinate: it removes the global scale gauge ($r=0$), preserves the full $\mathbb R^N$ ambient algebra, and supports the cumulant tower of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) directly.

### 2.2 The apex generator

\hypertarget{stmt:2-1}{}
**Definition 2.1.** The **partition function** and **unstructured apex generator** of a positive ledger $x$ are
$$Z_y(\beta)=\frac{1}{N}\sum_{i=1}^N e^{\beta y_i},\qquad K_y(\beta)=\log Z_y(\beta).$$

$Z_y$ is the moment generating function of the discrete uniform distribution on $\{y_1,\ldots,y_N\}$; $K_y$ is its cumulant generating function on the domain where the logarithm is single-valued.

\hypertarget{stmt:2-2}{}
**Theorem 2.2 (Analytic and structural properties).**

1. (Analytic status.) $Z_y(\beta)$ is entire in $\beta\in\mathbb C$ as a finite sum of exponentials. $K_y(\beta)=\log Z_y(\beta)$ is real-analytic on $\beta\in\mathbb R$ (where $Z_y>0$ by strict positivity of real exponentials) and holomorphic on any zero-free domain of $Z_y$ in $\mathbb C$, with a canonical Taylor branch on a neighborhood of $\beta=0$. The complex zeros of $Z_y$ are the **Lee–Yang points** of the apex generator; their location encodes the support structure of $y$. (Example: $y=(-1,1)$ gives $Z_y(\beta)=\cosh\beta$, with zeros at $\beta=i\pi(k+\tfrac{1}{2})$.)
2. $K_y(0)=0$, $K_y'(0)=0$, and $K_y^{(n)}(0)=\kappa_n$ for $n\ge 2$, where $\kappa_n$ is the $n$-th cumulant of the values $y_i$ under the uniform measure.
3. (Power-mean evaluations.) For all real $\beta$,
$$K_y(\beta)=\log\frac{M_\beta(x)^\beta}{G(x)^\beta}.$$
In particular, $K_y(1)=\log(A(x)/G(x))$, $K_y(-1)=\log(G(x)/H(x))$, $K_y(2)=\log(R(x)^2/G(x)^2)$, and $K_y(m)$ for integer $m$ records the $m$-power gauge ratio against the geometric center.
4. (Parity pair.) $K_y(\beta)+K_y(-\beta)=2\sum_{m\ge 1}\frac{\kappa_{2m}}{(2m)!}\beta^{2m}$ (even cumulants doubled); $K_y(\beta)-K_y(-\beta)=2\sum_{m\ge 1}\frac{\kappa_{2m+1}}{(2m+1)!}\beta^{2m+1}$ (odd cumulants doubled), as formal series at $\beta=0$.
5. (Tropical limits.) $\lim_{\beta\to+\infty}\frac{1}{\beta}K_y(\beta)=\max_i y_i$ and $\lim_{\beta\to-\infty}\frac{1}{\beta}K_y(\beta)=\min_i y_i$. The Maslov dequantization parameter is $\beta$.

**Proof.**

*(1) Analytic status.* For each $i$, the map $\beta\mapsto e^{\beta y_i}$ is entire on $\mathbb C$ as a composition of the linear map $\beta\mapsto\beta y_i$ with the entire exponential. A finite sum of entire functions is entire, so $Z_y(\beta)=\frac{1}{N}\sum_i e^{\beta y_i}$ is entire on $\mathbb C$.

For $\beta\in\mathbb R$, each summand $e^{\beta y_i}$ is strictly positive, so $Z_y(\beta)\ge\min_i e^{\beta y_i}>0$. The real-logarithm $\log$ is real-analytic on $(0,\infty)$, so $K_y=\log\circ Z_y$ is real-analytic on all of $\mathbb R$.

At $\beta=0$ we have $Z_y(0)=\frac{1}{N}\sum_i 1=1$, so $Z_y$ is nonzero on some open disk $D\subset\mathbb C$ centered at $0$. On any simply connected zero-free open set $U\subset\mathbb C$ containing $0$, $Z_y$ admits a single-valued holomorphic logarithm $\log Z_y$ uniquely determined by the value $0$ at $\beta=0$; we take this branch as the canonical definition of $K_y$ on $U$. Choosing $U$ to be the largest disk about $0$ on which $Z_y$ is zero-free yields the convergent Taylor branch of $K_y$ at $\beta=0$. The complex zeros of $Z_y$ are isolated (since $Z_y$ is a non-trivial entire function whenever $y$ is not identically zero — and $y$ is non-trivial in any non-degenerate case, since $\sum_i y_i=0$ forces $y=0$ only if all $y_i$ coincide). These zeros are the **Lee–Yang points** of the apex generator; in the toy example $y=(-1,1)$ one computes $Z_y(\beta)=\cosh\beta$, with zeros at $\beta=i\pi(k+\tfrac{1}{2})$ for $k\in\mathbb Z$. Beyond the largest zero-free disk, $K_y$ extends as a multi-valued holomorphic function on the complement of the zero set, with logarithmic branch points at each zero of $Z_y$.

*(2) Cumulant identification at $\beta=0$.* Let $Y$ be the random variable taking value $y_i$ with probability $1/N$ each (uniform measure on the multiset $\{y_1,\ldots,y_N\}$). Then $Z_y(\beta)=\mathbb E[e^{\beta Y}]$ is the moment generating function of $Y$, hence $K_y(\beta)=\log\mathbb E[e^{\beta Y}]$ is the cumulant generating function. By construction $K_y(0)=\log Z_y(0)=\log 1=0$. Differentiating $K_y'(\beta)=Z_y'(\beta)/Z_y(\beta)$ at $\beta=0$ gives
$$K_y'(0)=Z_y'(0)/Z_y(0)=\frac{1}{N}\sum_i y_i\big/1=0,$$
since $y$ is centered. The standard moment-cumulant identity (Brillinger 1975, Ch. 2) then gives $K_y^{(n)}(0)=\kappa_n(Y)$ for all $n\ge 1$; combined with $K_y'(0)=0$ this is the claim.

*(3) Power-mean evaluations.* By the definition of $y_i$, $\log x_i=\log G(x)+y_i$, so $x_i=G(x)e^{y_i}$ and $x_i^\beta=G(x)^\beta e^{\beta y_i}$ for every real $\beta$. Therefore
$$\frac{1}{N}\sum_i x_i^\beta=G(x)^\beta\cdot\frac{1}{N}\sum_i e^{\beta y_i}=G(x)^\beta Z_y(\beta).$$
By definition $M_\beta(x)^\beta=\frac{1}{N}\sum_i x_i^\beta$, so $Z_y(\beta)=M_\beta(x)^\beta/G(x)^\beta$ and taking logs gives $K_y(\beta)=\log(M_\beta(x)^\beta/G(x)^\beta)$. Specializing: $\beta=1$ gives $K_y(1)=\log(A(x)/G(x))$ (with $A=M_1$); $\beta=-1$ gives $K_y(-1)=\log(M_{-1}(x)^{-1}/G(x)^{-1})=\log(G(x)/H(x))$ (with $H=M_{-1}$); $\beta=2$ gives $K_y(2)=\log(R(x)^2/G(x)^2)$ (with $R=M_2$); and for integer $m$, $K_y(m)$ is the log-ratio of the $m$-power gauge against the geometric center.

*(4) Parity pair.* Write the Taylor expansion at $\beta=0$ as $K_y(\beta)=\sum_{n\ge 0}\frac{\kappa_n}{n!}\beta^n$, with $\kappa_0=0$ and $\kappa_1=0$ by part (2). Then
$$K_y(\beta)+K_y(-\beta)=\sum_{n\ge 0}\frac{\kappa_n}{n!}\big(\beta^n+(-\beta)^n\big)=2\sum_{n\text{ even}}\frac{\kappa_n}{n!}\beta^n=2\sum_{m\ge 1}\frac{\kappa_{2m}}{(2m)!}\beta^{2m}$$
(the $n=0$ term vanishes since $\kappa_0=0$), and similarly
$$K_y(\beta)-K_y(-\beta)=2\sum_{n\text{ odd}}\frac{\kappa_n}{n!}\beta^n=2\sum_{m\ge 1}\frac{\kappa_{2m+1}}{(2m+1)!}\beta^{2m+1}$$
(the $n=1$ term vanishes since $\kappa_1=0$). The identities hold as formal series at $\beta=0$ and convergently on the largest disk about $0$ that is zero-free for $Z_y$ — equivalently, wherever both sides are defined as analytic functions.

*(5) Tropical limits.* Set $y_{\max}=\max_i y_i$ and let $I_+=\{i:y_i=y_{\max}\}$ with $|I_+|=m_+\ge 1$. For $\beta>0$, factor out the dominant exponential:
$$Z_y(\beta)=\frac{1}{N}e^{\beta y_{\max}}\left(m_++\sum_{i\notin I_+}e^{\beta(y_i-y_{\max})}\right).$$
For $i\notin I_+$, $y_i-y_{\max}<0$, so $e^{\beta(y_i-y_{\max})}\to 0$ as $\beta\to+\infty$. Therefore
$$\frac{1}{\beta}K_y(\beta)=\frac{1}{\beta}\log\frac{1}{N}\sum_i e^{\beta y_i}=y_{\max}+\frac{1}{\beta}\log\frac{m_+}{N}+\frac{1}{\beta}\log\!\Big(1+o(1)\Big)\longrightarrow y_{\max}.$$
For the $\beta\to-\infty$ limit, substitute $\beta=-\beta'$ with $\beta'\to+\infty$:
$$\frac{1}{\beta}K_y(\beta)=-\frac{1}{\beta'}\log\frac{1}{N}\sum_i e^{\beta'(-y_i)}\longrightarrow-\max_i(-y_i)=\min_i y_i,$$
applying the $+\infty$ case to the reflected ledger $-y$. The convergence parameter $\beta$ is precisely the Maslov dequantization parameter (Maslov 1987, Litvinov–Maslov 2005). $\square$

### 2.3 The corridor as a single function

\hyperlink{stmt:2-2}{Theorem~2.2} says that $K_y(\beta)$ at $\beta\in\{-1,0,1,2,3,\ldots\}$ recovers, respectively, the harmonic, geometric, arithmetic, RMS, cubic, and higher-power gauge ratios; its Taylor expansion at $\beta=0$ recovers the cumulant tower; its parity decomposition splits even and odd cumulants; its tropical limits at $\pm\infty$ recover the extremal supports.

> **The gauge corridor is the moment-generating function of the centered log-ledger, sampled at named values of $\beta$.**

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s choice of $\beta=1$ (the e-flat / softmax gauge) is one sample. [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s choice of $\beta=\pm 1$ (the harmonic dual pair) is another. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s choice of $\beta=2$ (RMS / Born) is another. Each previous paper of the trilogy worked one cell of the corridor; $K_y(\beta)$ is the cell itself.

### 2.4 The $\beta$-flow: replicator and natural-gradient dynamics

\hypertarget{stmt:2-3}{}
**Definition 2.3.** The **escort family** of a centered log-ledger $y$ is
$$P_\beta(i)=\frac{e^{\beta y_i}}{\sum_j e^{\beta y_j}},\qquad\beta\in\mathbb R.$$

At $\beta=0$, $P_\beta$ is the uniform $u$. As $\beta\to+\infty$, $P_\beta$ concentrates on $\arg\max_i y_i$; as $\beta\to-\infty$, on $\arg\min_i y_i$.

\hypertarget{stmt:2-4}{}
**Theorem 2.4 (Replicator flow).** The escort family satisfies the autonomous ordinary differential equation (ODE)
$$\boxed{\frac{d}{d\beta}P_\beta(i)=P_\beta(i)\Big(y_i-\mathbb E_{P_\beta}[y]\Big),}$$
the constant-fitness replicator equation with fitness vector $y$. This is the **Shahshahani/Fisher gradient flow on the simplex of the linear functional $p\mapsto\mathbb E_p[y]$**, restricted to the escort family $\{P_\beta\}_{\beta\in\mathbb R}$. The apex generator $K_y(\beta)$ is the **free energy along this flow**: by direct computation,
$$K_y'(\beta)=\mathbb E_{P_\beta}[y]\quad\text{and}\quad K_y''(\beta)=\mathrm{Var}_{P_\beta}(y)\ge 0.$$
So $K_y$ is convex on $\mathbb R$, its slope at $\beta$ is the mean fitness under $P_\beta$, and its curvature is the Fisher information of $P_\beta$ along $y$.

**Proof.**

*(ODE.)* Let $Z^\ast_y(\beta):=\sum_j e^{\beta y_j}=NZ_y(\beta)$ so that $P_\beta(i)=e^{\beta y_i}/Z^\ast_y(\beta)$. Direct differentiation in $\beta$:
$$\partial_\beta P_\beta(i)=\frac{y_i e^{\beta y_i}}{Z^\ast_y(\beta)}-\frac{e^{\beta y_i}}{Z^\ast_y(\beta)^2}\sum_j y_j e^{\beta y_j}=P_\beta(i)\,y_i-P_\beta(i)\sum_j y_j P_\beta(j)=P_\beta(i)\big(y_i-\mathbb E_{P_\beta}[y]\big),$$
which is the constant-fitness replicator equation with fitness $y$.

*(Shahshahani-gradient identification.)* The Shahshahani metric on the open simplex $\mathring\Delta^{N-1}\subset\mathbb R^N$ is $g^{Sh}_p(u,v)=\sum_i u_iv_i/p_i$ on the tangent hyperplane $T_p\Delta^{N-1}=\{w\in\mathbb R^N:\sum_iw_i=0\}$. For a smooth function $L:\Delta^{N-1}\to\mathbb R$, the gradient $\nabla^{Sh}L|_p\in T_p\Delta^{N-1}$ is defined by $dL_p(v)=g^{Sh}_p(\nabla^{Sh}L|_p,v)$ for all tangent $v$. Applied to $L(p)=\mathbb E_p[y]=\sum_ip_iy_i$, we have $dL_p(v)=\sum_iv_iy_i$. Seek $G\in T_p\Delta^{N-1}$ (so $\sum_iG_i=0$) with
$$\sum_i\frac{G_i\,v_i}{p_i}=\sum_iv_iy_i\quad\text{for all }v\in T_p\Delta^{N-1}.$$
This means $G_i/p_i-y_i$ is orthogonal to $T_p\Delta^{N-1}$, i.e., constant in $i$: $G_i/p_i=y_i+\lambda$ for some Lagrange multiplier $\lambda$. The constraint $\sum_iG_i=0$ fixes $\lambda=-\sum_ip_iy_i=-\mathbb E_p[y]$. Therefore
$$\big(\nabla^{Sh}L|_p\big)_i=p_i\big(y_i-\mathbb E_p[y]\big),$$
which evaluated at $p=P_\beta$ is precisely the right-hand side of the replicator ODE. Hence the escort flow $\beta\mapsto P_\beta$ is the Shahshahani gradient flow of $L$ on $\mathring\Delta^{N-1}$.

*(Free-energy identities.)* From $K_y(\beta)=\log Z_y(\beta)$ with $Z_y(\beta)=\frac{1}{N}\sum_i e^{\beta y_i}$,
$$K_y'(\beta)=\frac{Z_y'(\beta)}{Z_y(\beta)}=\frac{\frac{1}{N}\sum_iy_ie^{\beta y_i}}{\frac{1}{N}\sum_je^{\beta y_j}}=\sum_iy_iP_\beta(i)=\mathbb E_{P_\beta}[y].$$
Differentiating once more and using the replicator ODE,
$$K_y''(\beta)=\partial_\beta\mathbb E_{P_\beta}[y]=\sum_iy_i\,\partial_\beta P_\beta(i)=\sum_iy_iP_\beta(i)\big(y_i-\mathbb E_{P_\beta}[y]\big)=\mathbb E_{P_\beta}[y^2]-\mathbb E_{P_\beta}[y]^2=\mathrm{Var}_{P_\beta}(y)\ge 0.$$
The convexity $K_y''\ge 0$ on $\mathbb R$ is therefore the non-negativity of variance under the escort. $\square$

The classical literatures sitting at this flow include:

- **Population genetics:** $y$ is fitness, $P_\beta$ is the frequency under selection at intensity $\beta$.
- **Evolutionary game theory:** the replicator dynamic of Taylor–Jonker, Hofbauer–Sigmund.
- **Statistical mechanics:** the canonical ensemble at inverse temperature $\beta$ with energy $-y$.
- **Machine learning:** the natural-gradient annealing dynamic of Amari, with $\beta$ the inverse temperature.
- **Information geometry:** the Shahshahani gradient flow on the simplex.

These are five classical literatures whose central one-parameter family is, structurally, the gauge corridor traversed by the $\beta$-flow.

### 2.5 Compactification by tropical limits {#sec:2-5}

The corridor closes at $\pm\infty$ by the Maslov dequantization
$$F_\beta(y)=\frac{1}{\beta}K_y(\beta)\xrightarrow{\beta\to\pm\infty}\max_i y_i\text{ or }\min_i y_i.$$

These boundary limits are the **tropical extremes** of the corridor. They convert the ordinary algebra $(\mathbb R,+,\cdot)$ into the max-plus algebra $(\mathbb R,\max,+)$ in the standard sense of tropical geometry (Maslov, Litvinov–Maslov, Itenberg–Mikhalkin–Shustin, Viro). The replicator flow at large $|\beta|$ becomes winner-take-all or loser-take-all dynamics; the cumulant generator becomes the support function of the convex hull of $\{y_1,\ldots,y_N\}$ — equivalently, the boundary of the effective domain $\mathrm{dom}\,K_y^\ast=\mathrm{conv}\{y_i\}$ of the conjugate potential of \hyperref[sec:2-7]{§2.7}, with the tropical slopes realized as the rate function on the hull extremes (\hyperlink{stmt:2-8}{Corollary~2.8}).

Forward-door interpretation: **the gauge corridor is a one-parameter deformation between ordinary statistics ($\beta$ finite) and tropical/large-deviation statistics ($\beta\to\pm\infty$).** Tropical geometry, large-deviation theory, and Rényi/multifractal spectra are the corridor's boundary content.

### 2.6 Lee-Yang zeros at $N=2$

The Lee–Yang points named in \hyperlink{stmt:2-2}{Theorem~2.2.1} admit an exact description at the smallest non-trivial dimension.

\hypertarget{stmt:2-5}{}
**Proposition 2.5 (Lee-Yang structure at $N=2$).** For $N=2$ with centered log-ledger $y=(-a,a)$ and $a>0$, the partition function is
$$Z_y(\beta)=\cosh(a\beta),$$
and the complete set of complex zeros forms the imaginary lattice
$$\{\beta\in\mathbb C:Z_y(\beta)=0\}=\Big\{i\frac{\pi}{a}\big(k+\tfrac{1}{2}\big):k\in\mathbb Z\Big\}.$$
In particular, all Lee-Yang zeros are purely imaginary; the canonical Taylor branch of $K_y=\log Z_y$ at $\beta=0$ converges on the open disk $|\beta|<\pi/(2a)$, and $K_y$ extends holomorphically to the horizontal strip $|\mathrm{Im}\,\beta|<\pi/(2a)$, with logarithmic branch points at the Lee–Yang lattice on its boundary.

**Proof.** $Z_y(\beta)=\frac{1}{2}(e^{-a\beta}+e^{a\beta})=\cosh(a\beta)$ by direct computation. The zeros of $\cosh$ are $\{z\in\mathbb C:z=i\pi(k+\tfrac{1}{2}),\,k\in\mathbb Z\}$, all purely imaginary; substituting $z=a\beta$ gives $\beta=i\pi(k+\tfrac{1}{2})/a$. The nearest zero to $\beta=0$ has $|\beta|=\pi/(2a)$, which is therefore both the Taylor radius at $0$ and the half-width of the maximal horizontal strip on which $\log\cosh(a\beta)$ extends single-valuedly. $\square$

\hyperlink{stmt:2-5}{Proposition~2.5} is the toy version of the Lee–Yang circle theorem (Lee–Yang 1952; the imaginary-axis location is the finite-categorical analog of the unit circle in fugacity variables). For $N\ge 3$, the zero structure of $Z_y$ is not pinned to a single line by elementary arithmetic; the analytic study of its zero locus is the forward door of \hyperref[sec:6-6]{§6.6}.

### 2.7 The conjugate potential: rate function, escort entropy, and dually-flat geometry {#sec:2-7}

\hyperlink{stmt:2-4}{Theorem~2.4} presented $K_y$ as a convex free energy with slope $K_y'(\beta)=\mathbb E_{P_\beta}[y]$ and curvature $K_y''(\beta)=\mathrm{Var}_{P_\beta}(y)$. Convexity has a conjugate. \heb{ל}0 has so far extracted only the *infinitesimal* content of that convexity — the Fisher/cumulant data in the second and higher derivatives of $K_y$ — and never taken the Legendre transform that turns the convex potential into its global dual. This dual is the entropy / large-deviation face of the apex and the natural home of its information geometry. We make it first-class.

\hypertarget{stmt:2-6}{}
**Definition 2.6 (Conjugate potential and mean coordinate).** The **conjugate potential** of $K_y$ is its Legendre–Fenchel transform (Rockafellar 1970, §12)
$$\boxed{K_y^\ast(\xi)=\sup_{\beta\in\mathbb R}\big(\beta\xi-K_y(\beta)\big),\qquad\xi\in\mathbb R.}$$
We call $\beta$ the **gauge (canonical) coordinate** and $\xi$ the dual **mean coordinate** of the corridor; their duality is the content of \hyperlink{stmt:2-7}{Theorem~2.7}.

\hypertarget{stmt:2-7}{}
**Theorem 2.7 (Dually-flat structure of the apex).** Let $y\in H_N$ be non-degenerate (not all $y_i$ equal), let $P_\beta$ be the escort family (\hyperlink{stmt:2-3}{Definition~2.3}), and write $u=(1/N,\ldots,1/N)$, $H(P)=-\sum_iP(i)\log P(i)$ for Shannon entropy, and $D(P\,\Vert\,Q)=\sum_iP(i)\log\frac{P(i)}{Q(i)}$ for relative (Kullback–Leibler) entropy.

1. **(Dual coordinates.)** $\beta\mapsto\xi=K_y'(\beta)$ is a strictly increasing real-analytic diffeomorphism $\mathbb R\to(\min_iy_i,\max_iy_i)$, with inverse $\xi\mapsto\beta=(K_y^\ast)'(\xi)$. The supremum in \hyperlink{stmt:2-6}{Definition~2.6} is attained at the unique $\beta$ with $K_y'(\beta)=\xi$, and the **Fenchel–Young pairing**
$$\boxed{K_y(\beta)+K_y^\ast(\xi)=\beta\xi\quad\Longleftrightarrow\quad\xi=K_y'(\beta)}$$
holds. This is the dually-flat (Amari) pairing of the exponential ($e$-flat) coordinate $\beta$ and the mixture ($m$-flat) mean coordinate $\xi$ (Amari–Nagaoka 2000, §3; AJLS 2017, §4.3).

2. **(Escort entropy.)** At $\xi=K_y'(\beta)$,
$$\boxed{K_y^\ast(\xi)=\log N-H(P_\beta)=D(P_\beta\,\Vert\,u).}$$
The conjugate potential is the negative entropy of the escort, shifted by the constant $\log N=H(u)$ — equivalently, the relative entropy of the escort from the uniform center.

3. **(Cramér rate function.)** $K_y^\ast$ is the large-deviation rate function of Cramér's theorem (Dembo–Zeitouni 1998, Thm 2.2.3) for the empirical mean $\bar Y_n=\frac1n\sum_{k=1}^nY_k$ of i.i.d. draws $Y_k$ from the uniform law $u$ on $\{y_1,\ldots,y_N\}$: $\bar Y_n$ obeys a large-deviation principle with good rate function $K_y^\ast$, informally $\Pr(\bar Y_n\approx\xi)=e^{-n\,K_y^\ast(\xi)+o(n)}$. Its effective domain is the convex hull $\mathrm{dom}\,K_y^\ast=[\min_iy_i,\max_iy_i]=\mathrm{conv}\{y_i\}$, and $K_y^\ast\ge 0$ with equality iff $\xi=0$ — the centered mean, realized at the uniform/geometric center $\beta=0$, where $K_y$ also vanishes.

4. **(Metric reciprocity.)** On the open domain,
$$(K_y^\ast)''(\xi)=\frac{1}{K_y''(\beta)}=\frac{1}{\mathrm{Var}_{P_\beta}(y)}.$$
The Fisher information of the corridor is $K_y''$ read in the gauge coordinate and $(K_y^\ast)''$ read in the mean coordinate; the two are mutually reciprocal — the one-dimensional shadow of the dual Hessians $g=\nabla^2K_y$ and $g^{-1}=\nabla^2K_y^\ast$ of a dually-flat manifold.

5. **(Bregman $=$ relative entropy.)** The Bregman divergence generated by $K_y$ equals the relative entropy between escorts with transposed arguments,
$$\boxed{B_{K_y}(\beta_1\,\Vert\,\beta_2):=K_y(\beta_1)-K_y(\beta_2)-K_y'(\beta_2)(\beta_1-\beta_2)=D(P_{\beta_2}\,\Vert\,P_{\beta_1}),}$$
and dually $B_{K_y^\ast}(\xi_1\,\Vert\,\xi_2)=D(P_{\beta(\xi_1)}\,\Vert\,P_{\beta(\xi_2)})$. The canonical divergence of the dually-flat structure $(K_y,K_y^\ast)$ is therefore the Kullback–Leibler divergence of escorts (Amari–Nagaoka 2000, §3.4).

**Proof.**

*(1) Dual coordinates.* By \hyperlink{stmt:2-4}{Theorem~2.4}, $K_y''(\beta)=\mathrm{Var}_{P_\beta}(y)$; for finite $\beta$ the escort $P_\beta$ has full support, so $\mathrm{Var}_{P_\beta}(y)>0$ whenever $y$ is non-degenerate. Hence $K_y$ is strictly convex and $K_y'$ strictly increasing on $\mathbb R$, and it is real-analytic with non-vanishing derivative (\hyperlink{stmt:2-2}{Theorem~2.2.1}), so it is a real-analytic diffeomorphism onto its image. The tropical limits $K_y'(\beta)=\mathbb E_{P_\beta}[y]\to\max_iy_i$ ($\beta\to+\infty$) and $\to\min_iy_i$ ($\beta\to-\infty$) (\hyperlink{stmt:2-2}{Theorem~2.2.5}, with $K_y'=\mathbb E_{P_\beta}[y]$ from \hyperlink{stmt:2-4}{Theorem~2.4}) identify that image as the open interval $(\min_iy_i,\max_iy_i)$. For $\xi$ in this interval the strictly concave map $\beta\mapsto\beta\xi-K_y(\beta)$ has a unique critical point at $K_y'(\beta)=\xi$, its global maximum; substituting gives $K_y^\ast(\xi)=\beta\xi-K_y(\beta)$ (the Fenchel–Young equality) at $\xi=K_y'(\beta)$. Differentiating $K_y^\ast(\xi)=\beta(\xi)\,\xi-K_y(\beta(\xi))$ and using $K_y'(\beta)=\xi$ to cancel the $\beta'(\xi)$ terms gives $(K_y^\ast)'(\xi)=\beta$, the inverse map. The $e$-flat / $m$-flat reading is the standard exponential-family duality (Amari–Nagaoka 2000, §3).

*(2) Escort entropy.* From $P_\beta(i)=e^{\beta y_i}/\sum_je^{\beta y_j}=e^{\beta y_i}/(NZ_y(\beta))$ and $K_y=\log Z_y$,
$$\log P_\beta(i)=\beta y_i-\log\!\big(NZ_y(\beta)\big)=\beta y_i-K_y(\beta)-\log N.$$
Hence $H(P_\beta)=-\sum_iP_\beta(i)\log P_\beta(i)=-\beta\,\mathbb E_{P_\beta}[y]+K_y(\beta)+\log N=-\beta\xi+K_y(\beta)+\log N$, so $K_y^\ast(\xi)=\beta\xi-K_y(\beta)=\log N-H(P_\beta)$ by part (1). Finally $D(P_\beta\Vert u)=\sum_iP_\beta(i)\log\frac{P_\beta(i)}{1/N}=-H(P_\beta)+\log N$ equals the same expression.

*(3) Cramér rate function.* The variables $Y_k$ have moment generating function $\mathbb E_u[e^{\beta Y}]=Z_y(\beta)$, with log-MGF $\Lambda(\beta)=K_y(\beta)$ (\hyperlink{stmt:2-1}{Definition~2.1}). Cramér's theorem in $\mathbb R$ (Dembo–Zeitouni 1998, Thm 2.2.3) gives a large-deviation principle for $\bar Y_n$ with good rate function $\Lambda^\ast=K_y^\ast$, the convex conjugate. The effective domain of $\Lambda^\ast$ is the closed convex hull of the support, $[\min_iy_i,\max_iy_i]=\mathrm{conv}\{y_i\}$ (outside it no $\beta$ bounds the linear term, so the supremum is $+\infty$). Non-negativity and the unique zero at $\xi=\mathbb E_u[Y]=0$ follow from part (2): $K_y^\ast\ge 0$ since $\beta=0$ yields $-K_y(0)=0$ in the supremum, and $H(P_\beta)\le\log N$ with equality iff $P_\beta=u$ iff $\beta=0$ iff $\xi=K_y'(0)=0$.

*(4) Metric reciprocity.* Differentiate the inverse relation $(K_y^\ast)'(\xi)=\beta(\xi)$ from part (1): by the inverse-function theorem $(K_y^\ast)''(\xi)=\beta'(\xi)=1/K_y''(\beta)$, and $K_y''(\beta)=\mathrm{Var}_{P_\beta}(y)$ by \hyperlink{stmt:2-4}{Theorem~2.4}.

*(5) Bregman $=$ relative entropy.* Using $\log P_\beta(i)=\beta y_i-K_y(\beta)-\log N$ from part (2),
$$D(P_{\beta_2}\Vert P_{\beta_1})=\sum_iP_{\beta_2}(i)\big[(\beta_2-\beta_1)y_i-K_y(\beta_2)+K_y(\beta_1)\big]=(\beta_2-\beta_1)\xi_2-K_y(\beta_2)+K_y(\beta_1),$$
with $\xi_2=K_y'(\beta_2)$. Rearranging, this is $K_y(\beta_1)-K_y(\beta_2)-K_y'(\beta_2)(\beta_1-\beta_2)=B_{K_y}(\beta_1\Vert\beta_2)$. The dual identity follows from the general Bregman duality $B_{K_y}(\beta_1\Vert\beta_2)=B_{K_y^\ast}(\xi_2\Vert\xi_1)$ for Legendre pairs (Amari–Nagaoka 2000, §3.4). $\square$

\hypertarget{stmt:2-8}{}
**Corollary 2.8 (Tropical boundary as rate function on the hull extremes).** Let $I_+=\{i:y_i=\max_jy_j\}$ and $I_-=\{i:y_i=\min_jy_j\}$, with $m_\pm=|I_\pm|$. The conjugate potential attains its boundary values
$$K_y^\ast(\max_iy_i)=\lim_{\beta\to+\infty}\big(\beta\max_iy_i-K_y(\beta)\big)=\log\frac{N}{m_+},\qquad K_y^\ast(\min_iy_i)=\log\frac{N}{m_-}.$$
Equivalently, the Maslov tropical slopes $\max_iy_i$ and $\min_iy_i$ of \hyperlink{stmt:2-2}{Theorem~2.2.5} are the two supporting lines of $K_y$ at the endpoints of $\mathrm{dom}\,K_y^\ast=\mathrm{conv}\{y_i\}$, and the rate function at each hull extreme is the relative entropy $\log(N/m_\pm)=D\big(\mathrm{Unif}(I_\pm)\,\Vert\,u\big)$ of the winner-take-all (resp. loser-take-all) escort — the uniform distribution on the argmax (argmin) set — from the uniform center. The \hyperref[sec:2-5]{§2.5} statement that the $\beta\to\pm\infty$ generator is the support function of $\mathrm{conv}\{y_i\}$ is precisely the assertion that $K_y^\ast$ has effective domain $\mathrm{conv}\{y_i\}$, support function and convex conjugate being the same operation here.

**Proof.** By the proof of \hyperlink{stmt:2-2}{Theorem~2.2.5}, $K_y(\beta)=\beta\max_iy_i+\log(m_+/N)+o(1)$ as $\beta\to+\infty$, so $\beta\max_iy_i-K_y(\beta)\to-\log(m_+/N)=\log(N/m_+)$. Since $K_y'(\beta)\uparrow\max_iy_i$, this monotone limit equals $\sup_\beta(\beta\max_iy_i-K_y(\beta))=K_y^\ast(\max_iy_i)$ by continuity of $K_y^\ast$ up to the boundary of its domain. As $\beta\to+\infty$ the escort $P_\beta\to\mathrm{Unif}(I_+)$, with entropy $\log m_+$, so \hyperlink{stmt:2-7}{Theorem~2.7.2} recovers $K_y^\ast=\log N-\log m_+$. The minimum case is the reflection $y\mapsto-y$. $\square$

**The entropy diagonal.** The structured apex of \hyperref[sec:3]{§3} is read along two diagonals (\hyperref[sec:3-4]{§3.4}): the *moment/cumulant diagonal* (Taylor jets in $\beta$ at $\beta=0$) and the *closure diagonal* (integer $\beta$-samples), both traversing the gauge coordinate $\beta$ at a fixed character mode $c$. \hyperlink{stmt:2-7}{Theorem~2.7} exposes a third, transverse reading — the **entropy diagonal** — obtained not by sampling $\beta$ but by the Legendre involution $(\beta,K_y)\leftrightarrow(\xi,K_y^\ast)$ that swaps the gauge coordinate for its dual mean coordinate $\xi$ and the free energy for the rate function. The two sampling diagonals live on the $e$-side, where cumulants and moments are derivatives of the potential $K_y$; the entropy diagonal is the $m$-side, where the same content is reorganized as escort entropy / relative entropy. It is carried entirely by the conductor-trivial mode $K_y=\log\mathcal M_x(\cdot,0)$ (\hyperlink{stmt:3-2}{Theorem~3.2}): the non-trivial character modes $c\ne 0$ are complex-valued and admit no Legendre conjugate, so the entropy diagonal lives exactly where the connected (cumulant) part of the tower already lives.

**Remark 2.7a (The quantum lift: Kubo–Mori, not Bures).** Classically the convex potential $K_y$ carries a *unique* second-derivative metric — Chentsov's theorem: Fisher–Rao is the only monotone metric on the simplex — and its Legendre dual is the negative Shannon entropy. The quantum analog replaces the centered log-ledger $y$ by a centered modular Hamiltonian $L=\log\rho-\frac1N\mathrm{tr}(\log\rho)\,I_N$ and $K_y(\beta)$ by the quantum free energy $\beta\mapsto\log\mathrm{tr}\,e^{\beta L}$. There Chentsov uniqueness fails: the monotone (quantum Fisher) metrics form the Morozova–Chentsov–Petz family parameterized by operator-monotone functions (Morozova–Chentsov 1991; Petz 1996). The member carrying a genuine dually-flat structure — whose dual potential is the von Neumann entropy $-\mathrm{tr}(\rho\log\rho)$ and whose canonical divergence is the Umegaki relative entropy, the exact non-commutative counterpart of \hyperlink{stmt:2-7}{Theorem~2.7.2},(5) — is the **Kubo–Mori (Bogoliubov–Kubo–Mori) metric** (Petz–Tóth 1993), *not* the Bures/SLD metric. The quantum sector of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) (§7.2–7.3) lifts the replicator $\beta$-flow to the Bures metric / quantum Fisher information $g_{\mathrm{QFI}}=4g_{\mathrm{Bures}}$ — the *minimal* monotone metric, the one governing state estimation — whereas the entropy/dually-flat structure of the present subsection lifts to the Kubo–Mori member. The two agree only on the decoherent (commutative) stratum, where the whole monotone family collapses to Fisher–Rao. The quantum dually-flat apex on the Kubo–Mori metric is thus a distinct forward door from the Bures apex named in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.2.

---

## 3. The Structured Apex: $\mathcal M_x(\beta,c)$ {#sec:3}

### 3.1 When labels carry algebraic structure

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) treated the label set $\{1,\ldots,N\}$ as unstructured. [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) introduced the stipulation that the labels carry the additive structure of $\mathbb Z/N$, motivated by naturally cyclic categorical settings (days of the week, residues modulo a prime, decimal digits, hours of the day). With this stipulation, the label set acquires a Pontryagin dual (Pontryagin 1939): the group $\widehat{\mathbb Z/N}$ of characters $\chi_c(s)=e^{2\pi ics/N}$, indexed by $c\in\mathbb Z/N$.

The character basis $\{\chi_c\}_{c=0}^{N-1}$ is the discrete Fourier transform (DFT) basis of $\mathbb Z/N$. [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) used it to diagonalize $\Sigma$ and to derive the cubic vertex selection rule $a+b+c\equiv 0\pmod N$.

\heb{ל}0 extends this: the entire cumulant tower and the entire gauge corridor read together through the character basis form a single two-parameter object.

### 3.2 The Fourier-Mellin transform

\hypertarget{stmt:3-1}{}
**Definition 3.1.** The **structured apex generator** of a positive ledger $x$ on $\mathbb Z/N$ is the function
$$\boxed{\mathcal M_x(\beta,c)=\frac{1}{N}\sum_{s\in\mathbb Z/N}e^{\beta y_s}\overline{\chi_c(s)},\qquad\beta\in\mathbb C,\ c\in\widehat{\mathbb Z/N}.}$$

We call $\mathcal M_x$ the **Fourier-Mellin transform** of $x$, by analogy with the classical Mellin transform $\int_0^\infty f(t)t^{s-1}\,dt$ and the Pontryagin transform on finite abelian groups; $\beta$ plays the role of the Mellin parameter, $c$ the character index.

The terminology is by analogy and convenience: we are working with additive characters on $\mathbb Z/N$ and an exponential-Laplace kernel in $\beta$, which is a finite-categorical discrete analog of the integral Mellin transform on $\mathbb R_{>0}$. The literal Mellin transform on $(\mathbb Z/N)^\times$ requires multiplicative characters and a Dirichlet sum; that natural multiplicative-character upgrade is a forward door (\hyperref[sec:6-2]{§6.2}). Throughout \heb{ל}0, "Fourier-Mellin" means the additive-character version of \hyperlink{stmt:3-1}{Definition~3.1}.

### 3.3 Spine theorems

\hypertarget{stmt:3-2}{}
**Theorem 3.2 (Trivial mode reduction).** $\mathcal M_x(\beta,0)=e^{K_y(\beta)}$ for all $\beta$.

**Proof.** $\overline{\chi_0(s)}=1$ identically, so $\mathcal M_x(\beta,0)=\frac{1}{N}\sum_s e^{\beta y_s}=e^{K_y(\beta)}$ by \hyperlink{stmt:2-1}{Definition~2.1}. $\square$

So the unstructured apex is the trivial Fourier mode of the structured apex. **$K_y$ is the scalar shadow of $\mathcal M_x$.**

\hypertarget{stmt:3-3}{}
**Theorem 3.3 (Moment diagonal — Taylor jets at $\beta=0$).** For each character index $c$ and each integer $n\ge 0$,
$$\boxed{\partial_\beta^n\mathcal M_x(0,c)=\widehat{y^n}_c=\sum_{\substack{a_1,\ldots,a_n\\a_1+\cdots+a_n\equiv c\pmod N}}\widehat y_{a_1}\widehat y_{a_2}\cdots\widehat y_{a_n}.}$$

**Proof.** Differentiating $\mathcal M_x(\beta,c)=\frac{1}{N}\sum_s e^{\beta y_s}\overline{\chi_c(s)}$ $n$ times in $\beta$ commutes with the finite sum and produces $\partial_\beta^n e^{\beta y_s}=y_s^n e^{\beta y_s}$, so
$$\partial_\beta^n\mathcal M_x(\beta,c)=\frac{1}{N}\sum_s y_s^n e^{\beta y_s}\overline{\chi_c(s)}.$$
Setting $\beta=0$ gives $\partial_\beta^n\mathcal M_x(0,c)=\frac{1}{N}\sum_s y_s^n\overline{\chi_c(s)}=\widehat{y^n}_c$, the $c$-th Fourier coefficient of the pointwise $n$-th power of $y$.

For the convolution form, apply Fourier inversion to write $y_s=\sum_{a\in\widehat{\mathbb Z/N}}\widehat y_a\chi_a(s)$. Then by the character group law $\chi_{a_1}(s)\cdots\chi_{a_n}(s)=\chi_{a_1+\cdots+a_n}(s)$,
$$y_s^n=\sum_{a_1,\ldots,a_n\in\widehat{\mathbb Z/N}}\widehat y_{a_1}\cdots\widehat y_{a_n}\,\chi_{a_1+\cdots+a_n}(s).$$
Substituting into $\widehat{y^n}_c=\frac{1}{N}\sum_s y_s^n\overline{\chi_c(s)}$ and interchanging the finite sums,
$$\widehat{y^n}_c=\sum_{a_1,\ldots,a_n}\widehat y_{a_1}\cdots\widehat y_{a_n}\cdot\frac{1}{N}\sum_s\chi_{a_1+\cdots+a_n-c}(s).$$
Character orthogonality on $\mathbb Z/N$ gives $\frac{1}{N}\sum_s\chi_d(s)=\delta_{d\equiv 0\,(\mathrm{mod}\,N)}$, so the inner sum collapses to the indicator of $a_1+\cdots+a_n\equiv c\pmod N$:
$$\widehat{y^n}_c=\sum_{\substack{a_1,\ldots,a_n\in\widehat{\mathbb Z/N}\\a_1+\cdots+a_n\equiv c\,(\mathrm{mod}\,N)}}\widehat y_{a_1}\widehat y_{a_2}\cdots\widehat y_{a_n}.\qquad\square$$

The Taylor jet at $\beta=0$ in the $c$-th character mode is the $c$-th Fourier coefficient of the $n$-th power of the centered log-ledger — a **character-twisted raw moment** of $y$ — with the conductor selection rule $a_1+\cdots+a_n\equiv c\pmod N$ enforced by character orthogonality. This is the **moment diagonal** of the apex.

**Remark 3.3a (Moments vs cumulants).** \hyperlink{stmt:3-3}{Theorem~3.3} produces raw moment coefficients, not cumulant coefficients. The two coincide at the trivial Fourier mode $c=0$ only up to standard partition-subtraction: $\partial_\beta^n\mathcal M_x(0,0)=\widehat{y^n}_0=\mathbb E_u[y^n]$, the $n$-th raw moment of $y$ under the uniform measure, while the cumulant $\kappa_n=\partial_\beta^n K_y(0)=\partial_\beta^n\log\mathcal M_x(0,0)$ is the connected part obtained via the standard moment-cumulant Möbius/partition formula. Since $y$ is centered ($\kappa_1=0$), raw moments and cumulants agree at orders $n\le 3$ ($\kappa_2=\mu_2$, $\kappa_3=\mu_3$) but diverge from $n=4$ onward ($\kappa_4=\mu_4-3\mu_2^2$, etc.). For non-trivial Fourier modes $c\ne 0$, the connected (cumulant) version requires the analogous logarithmic expansion of $\mathcal M_x$, which produces character-twisted connected coefficients with the same selection rule but distinct values from order 4 up. The **cumulant diagonal** of $\mathcal M_x$ is therefore obtained by applying the partition-subtraction operation to the moment diagonal mode by mode; the two diagonals coincide through order 3 thanks to centering.

\hypertarget{stmt:3-4}{}
**Corollary 3.4 ([\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) reproduced).** Setting $n=3$ and $c=0$ in \hyperlink{stmt:3-3}{Theorem~3.3}, restricted to non-trivial characters,
$$\widehat{y^3}_0=\sum_{\substack{a,b,c\ne 0\\a+b+c\equiv 0\pmod N}}\widehat y_a\widehat y_b\widehat y_c.$$
Since $y$ is centered, $\widehat{y^3}_0=\mathbb E_u[y^3]=\mu_3=\kappa_3$, so this also equals the third cumulant. The Amari–Chentsov tensor of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)/[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) at the uniform is the $n=3,c=0$ slice of the moment (equivalently, cumulant) diagonal of $\mathcal M_x$.

\hypertarget{stmt:3-5}{}
**Theorem 3.5 (Closure diagonal — positive integer samples).** For each positive integer $m\ge 1$ and each character index $c$,
$$\boxed{\mathcal M_x(m,c)=G(x)^{-m}\widehat{x^m}_c=G(x)^{-m}\sum_{\substack{a_1,\ldots,a_m\\a_1+\cdots+a_m\equiv c\pmod N}}\widehat x_{a_1}\widehat x_{a_2}\cdots\widehat x_{a_m}.}$$

**Proof.** By definition $y_s=\log x_s-\frac{1}{N}\sum_j\log x_j=\log x_s-\log G(x)$, so $e^{y_s}=x_s/G(x)$ and for any integer $m\ge 1$,
$$e^{my_s}=\Big(\frac{x_s}{G(x)}\Big)^m=G(x)^{-m}x_s^m.$$
Substituting into the definition of $\mathcal M_x$,
$$\mathcal M_x(m,c)=\frac{1}{N}\sum_s e^{my_s}\overline{\chi_c(s)}=G(x)^{-m}\cdot\frac{1}{N}\sum_s x_s^m\overline{\chi_c(s)}=G(x)^{-m}\widehat{x^m}_c,$$
which is the first equality.

For the convolution form, apply Fourier inversion to $x$: $x_s=\sum_{a\in\widehat{\mathbb Z/N}}\widehat x_a\chi_a(s)$, valid as a finite Fourier expansion of any function on $\mathbb Z/N$ (here $x$ is real and positive but the expansion is complex-linear). By the character group law $\chi_{a_1}(s)\cdots\chi_{a_m}(s)=\chi_{a_1+\cdots+a_m}(s)$,
$$x_s^m=\sum_{a_1,\ldots,a_m\in\widehat{\mathbb Z/N}}\widehat x_{a_1}\cdots\widehat x_{a_m}\,\chi_{a_1+\cdots+a_m}(s).$$
Therefore
$$\widehat{x^m}_c=\frac{1}{N}\sum_s x_s^m\overline{\chi_c(s)}=\sum_{a_1,\ldots,a_m}\widehat x_{a_1}\cdots\widehat x_{a_m}\cdot\frac{1}{N}\sum_s\chi_{a_1+\cdots+a_m-c}(s),$$
and character orthogonality $\frac{1}{N}\sum_s\chi_d(s)=\delta_{d\equiv 0\,(\mathrm{mod}\,N)}$ collapses the inner sum to the indicator $\mathbf 1_{a_1+\cdots+a_m\equiv c\,(\mathrm{mod}\,N)}$. Combining,
$$\mathcal M_x(m,c)=G(x)^{-m}\widehat{x^m}_c=G(x)^{-m}\sum_{\substack{a_1,\ldots,a_m\\a_1+\cdots+a_m\equiv c\,(\mathrm{mod}\,N)}}\widehat x_{a_1}\widehat x_{a_2}\cdots\widehat x_{a_m}.$$
The argument requires $m\ge 1$ integer because $x_s^m$ must be the pointwise $m$-th power on $\mathbb Z/N$, whose character expansion is the $m$-fold convolution of $\widehat x$ above; the negative-integer case is covered by \hyperlink{stmt:3-6}{Corollary~3.6} via the reciprocal-ledger substitution. $\square$

\hypertarget{stmt:3-6}{}
**Corollary 3.6 (Polar case — negative integer samples).** Let $u_s=x_s^{-1}$ be the reciprocal ledger and let $\tilde y_s=-y_s$ be its centered log-ledger. Then for each negative integer $m=-m'$ with $m'\ge 1$,
$$\mathcal M_x(-m',c)=\mathcal M_u(m',c)=G(u)^{-m'}\widehat{u^{m'}}_c,$$
and the selection rule $a_1+\cdots+a_{m'}\equiv c\pmod N$ governs the convolution of $\widehat u$-coefficients.

**Proof.** $\mathcal M_x(-m',c)=\frac{1}{N}\sum_s e^{-m' y_s}\overline{\chi_c(s)}=\frac{1}{N}\sum_s e^{m'\tilde y_s}\overline{\chi_c(s)}=\mathcal M_u(m',c)$, since $\tilde y=-y$ is the centered log-ledger of $u=1/x$ (centering and reciprocation commute). Apply \hyperlink{stmt:3-5}{Theorem~3.5} to $u$. $\square$

The integer sample $\mathcal M_x(m,c)$ at positive $m$ records the $m$-power closure's character content; the polar partner at negative $m$ is the same theorem applied to the reciprocal ledger. The two cases are not literally a single polynomial selection rule on $\widehat x$: positive $m$ is polynomial in $\widehat x$, negative $m$ is polynomial in $\widehat u=\widehat{x^{-1}}$, and the two are related by reciprocal involution rather than algebraic continuation. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s RMS-conductor mixing theorem is the $m=2$ case of \hyperlink{stmt:3-5}{Theorem~3.5}; its polar partner is the $m=-2$ case (Born-dual / inverse-participation closure) given by \hyperlink{stmt:3-6}{Corollary~3.6} with $m'=2$.

### 3.4 The two diagonals as paired sampling regimes {#sec:3-4}

Theorems 3.3 and 3.5 sample the same surface $\mathcal M_x(\beta,c)$ at two different regimes:

- **Moment diagonal:** Taylor jets in $\beta$ at $\beta=0$; produces order-$n$ character-twisted raw moments (and, via partition-subtraction, cumulant tensors) with selection rule $a_1+\cdots+a_n\equiv c\pmod N$.
- **Closure diagonal:** integer samples in $\beta$ at $\beta=m\ge 1$; produces $m$-input/$1$-output closures with selection rule $a_1+\cdots+a_m\equiv c\pmod N$. The polar partner at $m\le -1$ is the same theorem applied to the reciprocal ledger (\hyperlink{stmt:3-6}{Corollary~3.6}).

The two diagonals share *modular selection rules* at $n=m$ (the same equation in the indices), but they are distinct *as operations on the underlying coordinates*:

- The moment diagonal at order $n$ is naturally read in the $n$-th root chart $p^{1/n}$ in which the order-$n$ canonical tensor linearizes (the AJLS half-density chart for $n=2$, the $1/3$ chart for $n=3$, etc.).
- The closure diagonal at exponent $m$ is the $m$-th power closure $x\mapsto x^m/\sum x^m$ which produces probability from amplitude (RMS Born for $m=2$, cubic for $m=3$, etc.).

**Organizing structure (Kummer-cover interpretation).** The pair of operations $p\mapsto p^{1/n}$ (adjoining an $n$-th root) and $x\mapsto x^m/\sum_j x_j^m$ (passing back through the $m$-th power map and renormalizing) is naturally organized by the Kummer cover of the simplex. The cover is trivial on the real positive sector and acquires its full deck group only in the complex amplitude extension; the precise statement is the following.

\hypertarget{stmt:3-7}{}
**Proposition 3.7 (Real-sector Kummer triviality).** For every integer $n\ge 1$, the $n$-th power closure
$$\pi_n:\mathring{\mathbb R}_{>0}^N/\mathbb R_{>0}^\times\longrightarrow\Delta^{N-1},\qquad[x]\longmapsto\Big(\frac{x_i^n}{\sum_j x_j^n}\Big)_{i=1}^N,$$
is a real-analytic homeomorphism of positive projective rays onto the open simplex, with inverse $p\mapsto[(p_1^{1/n},\ldots,p_N^{1/n})]$.

**Proof.** Pointwise positive $n$-th power $x\mapsto x^n$ is a real-analytic bijection of $\mathbb R_{>0}$ onto itself with real-analytic inverse $u\mapsto u^{1/n}$ (the unique positive $n$-th root). Componentwise extension to $\mathbb R_{>0}^N$, followed by the simplex closure $u\mapsto u/\sum_j u_j$, is well-defined on projective rays since both maps are equivariant under positive scaling ($\pi_n(cx)=\pi_n(x)$). Inverting closure on the positive sector by lifting back to the open ray of $L^n$-normalized vectors $\{x:\sum_jx_j^n=1\}$ and applying the inverse power yields the stated inverse. The intersection $\mu_n\cap\mathbb R_{>0}=\{1\}$ forces the deck group of the cover to be trivial on the real positive sector: any other lift of $p$ to a positive vector would require multiplication by some non-trivial $\zeta\in\mu_n$ with $\zeta\in\mathbb R_{>0}$, which forces $\zeta=1$. $\square$

The complex-amplitude extension is non-trivial: replacing $\mathbb R_{>0}^N$ by $\mathbb C^N$ with closure $p_i=|z_i|^n/\sum_j|z_j|^n$ enlarges the fiber of $\pi_n$ to the deck group $(\mu_n)^N/\mu_n$ (after quotienting global phase), turning $\pi_n$ into an honest Kummer cover with non-trivial Galois action. The diagonal pair $(p^{1/n},\,x^m/\sum x^m)$ then becomes a Galois-dual pair of operations on the cover, with the moment diagonal living on the upstairs Kummer fiber and the closure diagonal collapsing back to the simplex. This complex extension is the content of \hyperref[sec:6-1]{§6.1}; \heb{ל}0's contribution at the real-positive level is \hyperlink{stmt:3-7}{Proposition~3.7}.

> **The two diagonals are paired sampling regimes of the apex surface $\mathcal M_x(\beta,c)$ — moment at $\beta=0$, closure at integer $\beta=m$ — sharing a modular selection rule and organized by the Kummer cover of the simplex (trivial on the real positive sector, \hyperlink{stmt:3-7}{Proposition~3.7}; non-trivial Galois action only in the complex amplitude extension of \hyperref[sec:6-1]{§6.1}).**

A third reading is transverse to both. The **entropy diagonal** (\hyperref[sec:2-7]{§2.7}, \hyperlink{stmt:2-7}{Theorem~2.7}) is the Legendre involution $(\beta,K_y)\leftrightarrow(\xi,K_y^\ast)$ of the conductor-trivial mode: it leaves the $\beta$-axis entirely, replacing the gauge coordinate by the dual mean coordinate $\xi$ and the free energy by the rate function, and reorganizes the same content as escort entropy / relative entropy. The two sampling diagonals are the $e$-side (derivatives of $K_y$); the entropy diagonal is the $m$-side. It is carried only by $c=0$, since the character modes $c\ne 0$ are complex and admit no Legendre conjugate.

### 3.5 Replicator flow on the apex surface

The flow of \hyperlink{stmt:2-4}{Theorem~2.4} lifts to a clean character-convolution identity.

\hypertarget{stmt:3-8}{}
**Proposition 3.8 ($\beta$-derivative as character convolution).** For every $\beta\in\mathbb C$ and every $c\in\widehat{\mathbb Z/N}$,
$$\boxed{\partial_\beta\mathcal M_x(\beta,c)=\sum_{a\in\widehat{\mathbb Z/N}}\widehat y_a\,\mathcal M_x(\beta,c-a).}$$

**Proof.** $\partial_\beta\mathcal M_x(\beta,c)=\frac{1}{N}\sum_s y_s\,e^{\beta y_s}\overline{\chi_c(s)}$. Expanding $y_s=\sum_a\widehat y_a\chi_a(s)$ and using $\chi_a\overline{\chi_c}=\overline{\chi_{c-a}}$ gives
$$\partial_\beta\mathcal M_x(\beta,c)=\sum_a\widehat y_a\cdot\frac{1}{N}\sum_s e^{\beta y_s}\overline{\chi_{c-a}(s)}=\sum_a\widehat y_a\,\mathcal M_x(\beta,c-a).\qquad\square$$

At $c=0$ this reproduces the scalar \hyperlink{stmt:2-4}{Theorem~2.4} statement: $\partial_\beta\mathcal M_x(\beta,0)=\sum_a\widehat y_a\mathcal M_x(\beta,-a)$ and dividing by $\mathcal M_x(\beta,0)=e^{K_y(\beta)}$ recovers $K_y'(\beta)=\mathbb E_{P_\beta}[y]$ once the right-hand side is reorganized as an expectation. For $c\ne 0$ the identity is a genuinely vectorial replicator law on the character-indexed apex surface: differentiation in $\beta$ is convolution with $\widehat y$ in the conductor index. The corridor is therefore a holomorphic flow on the Fourier-Mellin surface compatible with the character decomposition.

The full holomorphic structure of $\mathcal M_x$ in complex $\beta$ — with its zeros, contour deformations, and analytic continuation — is a forward door (\hyperref[sec:6-6]{§6.6}).

---

## 4. Prime Decomposition {#sec:4}

### 4.1 Two prime layers

When $N$ has multiple prime factors, the conductor lattice acquires structure beyond the single-prime case. Two layers must be distinguished:

- **Local prime-power depth.** For $N=p^a$, the conductor packets form a $p$-adic filtration $H_p\subset H_{p^2}\subset\cdots\subset H_{p^a}$. This depth is non-trivial even in the single-prime case; it is the $p$-adic refinement of $\mathcal M_x$ on $\mathbb Z/p^a$.
- **Global cross-prime interaction.** For $N=\prod_i p_i^{a_i}$ with at least two distinct primes, the Chinese Remainder Theorem decomposes labels into a product over prime axes; the ledger's failure to be separable across these axes is its cross-prime interaction content.

These two layers are independent: prime-power $N$ has no cross-prime interaction (only depth); squarefree $N$ with multiple primes has no depth within each axis (only interaction); general $N$ has both.

### 4.2 Local prime-power conductor depth

\hypertarget{stmt:4-1}{}
**Proposition 4.1 (Prime-power locality).** For $N=p^a$ with $p$ prime and $a\ge 1$, every conductor of a non-trivial character is a positive power of $p$:
$$\mathrm{cond}(\chi_c)\in\{p,p^2,\ldots,p^a\}\quad\text{for }c\ne 0.$$

**Proof.** $\mathrm{cond}(\chi_c)=N/\gcd(c,N)=p^a/\gcd(c,p^a)$. Since $\gcd(c,p^a)=p^j$ for some $0\le j\le a-1$ when $c\ne 0$, the conductor is $p^{a-j}$, a positive power of $p$. $\square$

This gives a $p$-adic depth stratification:
$$H_0\otimes\mathbb C=\bigoplus_{j=1}^{a}H_{p^j},\qquad\dim_{\mathbb C}H_{p^j}=\varphi(p^j)=p^{j-1}(p-1).$$

The depth ladder $p\to p^2\to\cdots\to p^a$ is the local prime-power refinement of the conductor lattice. Each rung adds a layer of characters of strictly higher conductor; the cubic vertex selection rule restricted to $H_{p^a}$ is the prime-power-local version of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049).

\hypertarget{stmt:4-2}{}
**Example 4.2 ($N=8$).** Divisors $\{1,2,4,8\}$. Conductors of non-trivial characters: $8$ (four chars: $c=1,3,5,7$), $4$ (two chars: $c=2,6$), $2$ (one char: $c=4$). Depth filtration $H_2\subset H_2\oplus H_4\subset H_2\oplus H_4\oplus H_8$ of complex dimensions $1\subset 3\subset 7$. [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s cubic selection rule $a+b+c\equiv 0\pmod 8$ restricted to $H_8$ couples only the four highest-depth characters; cross-depth triples couple depths additively under conductor multiplication.

### 4.3 Global CRT decomposition

\hypertarget{stmt:4-3}{}
**Proposition 4.3 (Domain CRT factorization).** For $N=\prod_{i=1}^k p_i^{a_i}$ with $p_1,\ldots,p_k$ distinct primes, the Chinese Remainder Theorem gives the ring isomorphism
$$\mathbb Z/N\cong\prod_{i=1}^k\mathbb Z/p_i^{a_i}$$
sending $s\leftrightarrow(s_1,\ldots,s_k)$ with $s_i=s\bmod p_i^{a_i}$. The character group dualizes:
$$\widehat{\mathbb Z/N}\cong\prod_{i=1}^k\widehat{\mathbb Z/p_i^{a_i}},\qquad\chi_c(s)=\prod_{i=1}^k\chi^{(p_i^{a_i})}_{c_i}(s_i),$$
where $c=(c_1,\ldots,c_k)$ via CRT applied to the indices.

**Proof.** The ring isomorphism $\mathbb Z/N\cong\prod_i\mathbb Z/p_i^{a_i}$ is the classical Chinese Remainder Theorem (Lang, *Algebra* II §2). Dualizing — characters of a finite product abelian group factor as products of characters of the factors, $\widehat{G\times H}\cong\widehat G\times\widehat H$ — yields the character factorization with $\chi_c(s)=\prod_i\chi^{(p_i^{a_i})}_{c_i}(s_i)$ for $c=(c_1,\ldots,c_k)$ via the CRT isomorphism applied to the index set. $\square$

The **domain** of $\mathcal M_x$ — the index space $(\beta,c)\in\mathbb C\times\widehat{\mathbb Z/N}$ — always factorizes across primes. The **function** $\mathcal M_x$ factorizes if and only if the ledger does:

\hypertarget{stmt:4-4}{}
**Theorem 4.4 (Separability $\Leftrightarrow$ Euler factorization).** Let $N=\prod_{i=1}^k p_i^{a_i}$, identify labels with $(s_1,\ldots,s_k)\in\prod_i\mathbb Z/p_i^{a_i}$ via CRT (\hyperlink{stmt:4-3}{Proposition~4.3}), and write the centered log-ledger as $y(s_1,\ldots,s_k)$. The Fourier-Mellin transform factorizes
$$\mathcal M_x(\beta,c)=\prod_{i=1}^k\mathcal M^{(p_i^{a_i})}_{x^{(i)}}(\beta,c_i)\qquad\text{for all }(\beta,c)\in\mathbb C\times\widehat{\mathbb Z/N}$$
into a product of single-axis apex generators on the prime-power factors if and only if $y$ is separable across prime axes:
$$y(s_1,\ldots,s_k)=\sum_{i=1}^k y^{(i)}(s_i)$$
(equivalently, $y_A=0$ for $|A|\ge 2$ in the ANOVA decomposition; see \hyperlink{stmt:4-5}{Theorem~4.5} and \hyperlink{stmt:4-6}{Definition~4.6} below).

**Proof.**

*($\Leftarrow$)* Suppose $y=\sum_i y^{(i)}(s_i)$, with each $y^{(i)}$ satisfying $\sum_{s_i}y^{(i)}(s_i)=0$ (the zero-marginal condition forced by the ANOVA structure of \hyperlink{stmt:4-5}{Theorem~4.5}). Then $e^{\beta y(s)}=\prod_i e^{\beta y^{(i)}(s_i)}$, and the CRT character factorization $\chi_c(s)=\prod_i\chi^{(p_i^{a_i})}_{c_i}(s_i)$ from \hyperlink{stmt:4-3}{Proposition~4.3} gives
$$\mathcal M_x(\beta,c)=\frac{1}{N}\sum_{(s_1,\ldots,s_k)}\prod_i e^{\beta y^{(i)}(s_i)}\,\overline{\chi^{(p_i^{a_i})}_{c_i}(s_i)}=\prod_i\frac{1}{p_i^{a_i}}\sum_{s_i}e^{\beta y^{(i)}(s_i)}\,\overline{\chi^{(p_i^{a_i})}_{c_i}(s_i)}=\prod_i\mathcal M^{(p_i^{a_i})}_{x^{(i)}}(\beta,c_i),$$
where $x^{(i)}_{s_i}:=e^{y^{(i)}(s_i)}$ is the marginal ledger on $\mathbb Z/p_i^{a_i}$ (geometric mean $1$, so the apex is normalized).

*($\Rightarrow$)* Suppose the multiplicative identity holds for all $(\beta,c)$ — say $\mathcal M_x(\beta,c)=\prod_i F_i(\beta,c_i)$, with each factor depending only on $\beta$ and the single CRT component $c_i$. We deduce separability by reading off the first-order Taylor coefficient in $\beta$ at $\beta=0$.

At $\beta=0$, character orthogonality gives $\mathcal M_x(0,c)=\frac{1}{N}\sum_s\overline{\chi_c(s)}=\delta_{c,0}=\prod_i\delta_{c_i,0}$. Varying $c$ along one CRT axis at a time forces $F_i(0,c_i)=\delta_{c_i,0}$ for every $i$ and every $c_i\in\widehat{\mathbb Z/p_i^{a_i}}$.

Differentiate the multiplicative identity in $\beta$ at $\beta=0$. The left-hand side is the $n=1$ instance of \hyperlink{stmt:3-3}{Theorem~3.3}:
$$\partial_\beta\mathcal M_x(0,c)=\widehat y_c.$$
The right-hand side, by the product rule combined with $F_i(0,c_i)=\delta_{c_i,0}$, equals
$$\partial_\beta\prod_i F_i(0,c_i)=\sum_{i=1}^k F'_i(0,c_i)\prod_{j\ne i}\delta_{c_j,0}.$$
For a fixed $c$ with at least two non-zero CRT components $c_{i_1}\ne 0$ and $c_{i_2}\ne 0$, every term in the sum requires $c_j=0$ for all $j\ne i$, which is impossible for both $j=i_1$ and $j=i_2$ simultaneously. Hence the right-hand side vanishes, and therefore $\widehat y_c=0$ whenever $c$ has at least two non-zero CRT components.

Inverting the Fourier transform: characters $\chi_c$ with at most one non-zero CRT component depend on a single coordinate $s_i$, so
$$y(s)=\sum_{c\in\widehat{\mathbb Z/N}}\widehat y_c\chi_c(s)=\widehat y_0+\sum_{i=1}^k\sum_{\substack{c:\,c_j=0\,\forall j\ne i\\c_i\ne 0}}\widehat y_c\chi_c(s_i)=\sum_{i=1}^k y^{(i)}(s_i),$$
where we used $\widehat y_0=\frac{1}{N}\sum_s y(s)=0$ (centering) and defined $y^{(i)}(s_i):=\sum_{c_i\ne 0}\widehat y_{(0,\ldots,c_i,\ldots,0)}\chi^{(p_i^{a_i})}_{c_i}(s_i)$. Hence $y$ is additively separable across the prime axes. $\square$

> **Domain always factorizes via CRT; function factorizes iff ledger is separable. The deviation from factorization is the ledger's prime-interaction content.**

### 4.4 ANOVA decomposition of the ledger

Cross-prime non-separability admits a canonical decomposition.

\hypertarget{stmt:4-5}{}
**Theorem 4.5 (ANOVA / Möbius decomposition).** For $N=\prod_{i=1}^k p_i^{a_i}$ and any function $y:\prod_i\mathbb Z/p_i^{a_i}\to\mathbb R$ with $\sum_s y(s)=0$, there is a unique decomposition
$$\boxed{y=\sum_{\emptyset\ne A\subseteq\{1,\ldots,k\}}y_A,}$$
where $y_A$ depends only on the coordinates $(s_i)_{i\in A}$ and has zero marginal over each $s_i$ for $i\in A$:
$$\sum_{s_i\in\mathbb Z/p_i^{a_i}}y_A(\ldots,s_i,\ldots)=0\quad\text{for every }i\in A.$$

This is the **Hoeffding / ANOVA / Möbius decomposition** over the subset lattice, classical in statistics and combinatorics.

**Proof.** Write $\mathcal X_i:=\mathbb Z/p_i^{a_i}$ and, for each $B\subseteq\{1,\ldots,k\}$, define the **average-out marginal**
$$y_{(\le B)}(s_B):=\frac{1}{\prod_{j\notin B}|\mathcal X_j|}\sum_{(s_j)_{j\notin B}}y(s_B,s_{\bar B}),$$
a function of $s_B=(s_j)_{j\in B}$ alone (with $y_{(\le\emptyset)}=\frac{1}{N}\sum_s y(s)=0$ by centering, and $y_{(\le\{1,\ldots,k\})}=y$). Möbius-invert on the Boolean lattice of subsets to define
$$y_A(s_A):=\sum_{B\subseteq A}(-1)^{|A\setminus B|}\,y_{(\le B)}(s_B).$$
By construction $y_A$ depends only on $s_A$. By Möbius inversion on the subset lattice (Rota 1964; Stanley, *Enumerative Combinatorics I*, §3.7),
$$y_{(\le A)}=\sum_{B\subseteq A}y_B,$$
and applying this at $A=\{1,\ldots,k\}$ recovers $y=\sum_{B\subseteq\{1,\ldots,k\}}y_B=\sum_{\emptyset\ne B}y_B$ (the empty stratum vanishes by centering).

*Zero-marginal condition.* Fix $i\in A$ and sum $y_A$ over $s_i$. For $B\subseteq A$, summing $y_{(\le B)}(s_B)$ over $s_i$ behaves as follows:
- If $i\in B$, $y_{(\le B)}$ depends on $s_i$, and $\sum_{s_i}y_{(\le B)}(s_B)=|\mathcal X_i|\cdot y_{(\le B\setminus\{i\})}(s_{B\setminus\{i\}})$.
- If $i\notin B$, $y_{(\le B)}$ is independent of $s_i$, and $\sum_{s_i}y_{(\le B)}(s_B)=|\mathcal X_i|\cdot y_{(\le B)}(s_B)$.

Combining, with $C:=B\setminus\{i\}$ in the first family and $C:=B$ in the second (both range over $C\subseteq A\setminus\{i\}$):
$$\frac{1}{|\mathcal X_i|}\sum_{s_i}y_A(s)=\sum_{C\subseteq A\setminus\{i\}}\Big[(-1)^{|A\setminus(C\cup\{i\})|}+(-1)^{|A\setminus C|}\Big]y_{(\le C)}(s_C).$$
Since $i\in A\setminus C$ (because $i\in A$ and $i\notin C$), $|A\setminus C|=|A\setminus(C\cup\{i\})|+1$, so the two signs cancel and each bracket is zero. Hence $\sum_{s_i}y_A=0$ for every $i\in A$.

*Uniqueness.* Suppose $y=\sum_A z_A$ is another decomposition with each $z_A$ depending only on $s_A$ and having zero marginal on each $s_i$ for $i\in A$. Average over $s_{\bar B}$: each $z_A$ with $A\not\subseteq B$ contains some $i\in A\setminus B\subseteq\bar B$, and the zero-marginal property kills it. Hence $y_{(\le B)}=\sum_{A\subseteq B}z_A$, and Möbius inversion gives $z_A=y_A$, the uniqueness claim. $\square$

\hypertarget{stmt:4-6}{}
**Definition 4.6.** A ledger $y$ is **separable across prime axes** if $y_A=0$ for every $|A|\ge 2$ in its ANOVA decomposition. Equivalently, $y$ is a sum of single-axis terms.

\hypertarget{stmt:4-7}{}
**Theorem 4.7 (ANOVA orthogonality and the cumulant separability criterion).** Let $S=(S_1,\ldots,S_k)$ be uniform on $\prod_i\mathbb Z/p_i^{a_i}$ (equivalently, $S$ uniform on $\mathbb Z/N$ via CRT) and let $y=\sum_A y_A$ be the ANOVA decomposition of \hyperlink{stmt:4-5}{Theorem~4.5}.

(a) *(Orthogonality.)* For $A\ne B$, the strata are uncorrelated under the uniform measure:
$$\mathbb E\big[y_A(S)\,y_B(S)\big]=0.$$

(b) *(Cumulant separability criterion.)* The centered log-ledger $y$ is separable across prime axes if and only if the cumulant generator factorizes additively over single-axis strata:
$$K_y(\beta)=\sum_{i=1}^k\log\mathbb E\big[e^{\beta y^{(i)}(S_i)}\big],\qquad y^{(i)}:=y_{\{i\}}.$$
Equivalently, the **cross-prime interaction defect**
$$\Delta_y(\beta):=K_y(\beta)-\sum_{i=1}^k\log\mathbb E\big[e^{\beta y^{(i)}(S_i)}\big]$$
vanishes identically iff $y$ is separable. The Taylor coefficients of $\Delta_y$ at $\beta=0$ are the **higher-order interaction information** quantities of Han (1980), McGill (1954), and Yeung (1991).

**Proof.**

*(a) Orthogonality.* Let $A\ne B$ and pick $i\in A\bigtriangleup B$ (symmetric difference; at least one element exists since $A\ne B$). Without loss of generality $i\in A\setminus B$, so $y_B$ does not depend on $s_i$. Conditioning on the other coordinates $S_{\ne i}:=(S_j)_{j\ne i}$,
$$\mathbb E\big[y_A(S)y_B(S)\mid S_{\ne i}\big]=y_B(S_{\ne i})\cdot\frac{1}{p_i^{a_i}}\sum_{s_i\in\mathbb Z/p_i^{a_i}}y_A(s_i,S_{\ne i})=y_B(S_{\ne i})\cdot 0=0,$$
using the zero-marginal property of $y_A$ on the coordinate $i\in A$ (\hyperlink{stmt:4-5}{Theorem~4.5}). The tower property gives $\mathbb E[y_A y_B]=0$.

*(b) Cumulant separability criterion, forward direction $(\Rightarrow)$.* If $y=\sum_i y^{(i)}(s_i)$ with $y_A\equiv 0$ for $|A|\ge 2$, then since the coordinates $S_1,\ldots,S_k$ are mutually independent under the uniform product measure on $\prod_i\mathbb Z/p_i^{a_i}$ (immediate from the CRT factorization, \hyperlink{stmt:4-3}{Proposition~4.3}), the random variables $y^{(i)}(S_i)$ are mutually independent. Therefore
$$\mathbb E\big[e^{\beta y(S)}\big]=\mathbb E\Big[\prod_i e^{\beta y^{(i)}(S_i)}\Big]=\prod_i\mathbb E\big[e^{\beta y^{(i)}(S_i)}\big],$$
and taking logs gives $K_y(\beta)=\sum_i\log\mathbb E[e^{\beta y^{(i)}(S_i)}]$, i.e., $\Delta_y\equiv 0$.

*(b) Reverse direction $(\Leftarrow)$.* Suppose $\Delta_y\equiv 0$, so $\mathbb E[e^{\beta y(S)}]=\prod_i\mathbb E[e^{\beta y^{(i)}(S_i)}]$ for all $\beta\in\mathbb R$. Reading off the coefficient of $\beta^2/2$ (the second cumulant on each side equals the second moment, since both $y$ and the $y^{(i)}$ have zero mean), the identity gives
$$\mathbb E\big[y(S)^2\big]=\sum_i\mathbb E\big[y^{(i)}(S_i)^2\big]+2\sum_{i<j}\mathbb E[y^{(i)}(S_i)]\,\mathbb E[y^{(j)}(S_j)]=\sum_i\mathbb E\big[y^{(i)}(S_i)^2\big],$$
where the cross terms vanish since each $y^{(i)}$ has zero mean (part (a) with $A=\{i\}$, $B=\emptyset$; equivalently, zero-marginal). Expanding the left-hand side via the ANOVA decomposition $y=\sum_A y_A$ and applying part (a) to the cross terms,
$$\mathbb E\big[y(S)^2\big]=\mathbb E\Big[\Big(\sum_A y_A(S)\Big)^2\Big]=\sum_A\mathbb E\big[y_A(S)^2\big].$$
Subtracting,
$$0=\mathbb E[y(S)^2]-\sum_i\mathbb E[y^{(i)}(S_i)^2]=\sum_{|A|\ge 2}\mathbb E\big[y_A(S)^2\big].$$
Each summand is non-negative, so $\mathbb E[y_A(S)^2]=0$ for every $A$ with $|A|\ge 2$, forcing $y_A\equiv 0$ as functions on $\prod_i\mathbb Z/p_i^{a_i}$. Hence $y=\sum_i y^{(i)}(s_i)$ is separable. $\square$

> **Separable ledger $\Leftrightarrow$ only single-axis ANOVA terms $\Leftrightarrow$ Euler factorization of $\mathcal M_x$ $\Leftrightarrow$ vanishing higher-order interaction information across prime axes.**

Four equivalent statements; pick the literature whose language fits.

### 4.5 $N=6$ as the structural anchor {#sec:4-5}

\hypertarget{stmt:4-8}{}
**Proposition 4.8.** $N=6=2\cdot 3$ is the smallest integer admitting a non-trivial cross-prime ANOVA interaction term.

**Proof.** $N\in\{2,3,4,5\}$ are prime or prime powers, so they have only one prime axis and no cross-prime interaction (\hyperlink{stmt:4-1}{Proposition~4.1}). $N=6$ is the smallest squarefree integer with two distinct prime factors. $\square$

For $N=6$, the ANOVA decomposition of the centered log-ledger is
$$y(s_2,s_3)=y_{\{2\}}(s_2)+y_{\{3\}}(s_3)+y_{\{2,3\}}(s_2,s_3),$$
where $s_2\in\mathbb Z/2$, $s_3\in\mathbb Z/3$, $s\leftrightarrow(s_2,s_3)$ by CRT. The interaction term $y_{\{2,3\}}$ has both row- and column-marginals zero, giving
$$\dim y_{\{2,3\}}=(|\mathbb Z/2|-1)(|\mathbb Z/3|-1)=1\cdot 2=2$$
degrees of freedom. The single-axis strata contribute $|\mathbb Z/2|-1=1$ and $|\mathbb Z/3|-1=2$ degrees of freedom respectively, recovering the full $N-1=5$ dimensions of the mean-zero space as $1+2+2$. $\mathcal M_x$ factorizes over the product $\mathbb Z/2\times\mathbb Z/3$ exactly when $y_{\{2,3\}}=0$.

This makes $N=6$ the **smallest worked example** of:
- non-trivial cross-prime interaction;
- failure of Euler factorization of $\mathcal M_x$;
- non-vanishing higher-order interaction information across prime axes;
- non-trivial cubic vertex selection rule cross-coupling two distinct conductor packets ([\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) §7.2);
- the smallest $N$ at which the conductor selection rule $a+b+c\equiv 0\pmod N$ for non-trivial characters distributes across multiple primes simultaneously.

\heb{ל}0 takes $N=6$ as the canonical example throughout. Earlier worked examples at $N=4$ ([\heb{ל}1](https://doi.org/10.5281/zenodo.20336872), [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) §7.1) illustrate local prime-power depth; $N=6$ illustrates cross-prime interaction; together they exhibit both layers of prime structure on the apex.

### 4.6 Theorem-style summary

> **Prime-Power Locality.** *For $N=p^a$, the conductor arithmetic of $\mathcal M_x$ is $p$-local; conductor packets form a $p$-adic depth filtration of $H_0$ with dimensions $\varphi(p^j)$ for $j=1,\ldots,a$.*

> **CRT Cross-Prime Interaction.** *For $N=\prod p_i^{a_i}$ with at least two distinct primes, the centered log-ledger admits a canonical ANOVA decomposition $y=\sum_A y_A$ over subsets $A\subseteq\{1,\ldots,k\}$ of prime axes; mixed terms $y_A$ for $|A|\ge 2$ are the cross-prime interaction content. The Fourier-Mellin transform $\mathcal M_x$ factorizes over the CRT decomposition iff all mixed terms vanish, equivalently iff the cross-prime higher-order interaction information vanishes.*

---

## 5. The Dimensional Axis: Helmert Ladder {#sec:5}

### 5.1 The integer ladder

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) builds the reversible dimensional ladder on the mean-zero space. For $1\le k\le N-1$, the unnormalized Helmert vector
$$h_k=(1,\ldots,1,-k,0,\ldots,0)\in\mathbb R^N$$
has $k$ leading ones, $-k$ in slot $k+1$, and $N-k-1$ trailing zeros; the all-ones vector $h_N=(1,\ldots,1)$ closes the basis of $\mathbb R^N$. The vectors $h_1,\ldots,h_{N-1}$ are mutually orthogonal in $H_N$ with norms
$$\|h_k\|^2=k(k+1),$$
and every $q\in\mathbb R^N$ decomposes uniquely as
$$q=\bar q\,h_N/N+\sum_{k=1}^{N-1}\frac{h_k\cdot q}{k(k+1)}h_k.$$

The Helmert ladder is therefore an orthogonal integer basis of $\mathbb R^N$ which, restricted to $H_N$, is a rational orthogonal basis. It is reversible across dimension: descending $N\to N-1$ records the mean and projects; ascending $N-1\to N$ appends the balancing coordinate determined by the mean-zero condition.

### 5.2 Unit normalization and the radical clock

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s main theorem: unit normalization of the Helmert ladder forces a quadratic field extension exactly at prime rungs.

\hypertarget{stmt:5-1}{}
**Theorem 5.1 ([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504), restated).** Let $e_k=h_k/\sqrt{k(k+1)}$ be the unit Helmert vector, and let
$$K_N=\mathbb Q\big(\sqrt{\mathrm{sf}(k(k+1))}:1\le k<N\big).$$
Then $K_N=\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$, and the inclusion $K_{N-1}\subseteq K_N$ is proper iff $N$ is prime.

**Proof sketch (full argument in [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) §3).**

*Forward inclusion.* For any $1\le k<N$ and any prime $p\mid k(k+1)$, $p$ divides either $k$ or $k+1$, hence $p\le k+1\le N$. Therefore $\sqrt{\mathrm{sf}(k(k+1))}$, a product of square-roots of primes $\le N$, lies in $\mathbb Q(\sqrt p:p\le N)$. This gives $K_N\subseteq\mathbb Q(\sqrt p:p\le N,\;p\text{ prime})$.

*Reverse inclusion.* Induct on primes $p\le N$. Base case $p=2$: take $k=1$, then $k(k+1)=2$ and $\sqrt 2=\sqrt{\mathrm{sf}(2)}\in K_2\subseteq K_N$. Inductive step at odd prime $p\le N$: take $k=p-1$, so $k(k+1)=(p-1)p$. Since $\gcd(p,p-1)=1$, $\mathrm{sf}((p-1)p)=p\cdot\mathrm{sf}(p-1)$, and the inductive hypothesis gives $\sqrt q\in K_N$ for every prime $q\mid p-1$, hence $\sqrt{\mathrm{sf}(p-1)}=\prod_{q\mid p-1}\sqrt q\in K_N$. Dividing,
$$\sqrt p=\frac{\sqrt{p\cdot\mathrm{sf}(p-1)}}{\sqrt{\mathrm{sf}(p-1)}}=\frac{\sqrt{\mathrm{sf}(k(k+1))}}{\sqrt{\mathrm{sf}(p-1)}}\in K_N.$$

*Prime growth criterion.* If $N$ is composite, write the new generator $\sqrt{\mathrm{sf}((N-1)N)}=\sqrt{\mathrm{sf}(N-1)\cdot\mathrm{sf}(N)}$ (coprime factors). Every prime divisor of $(N-1)N$ is $<N$ when $N$ is composite (since $N=ab$ forces every prime factor of $N$ to be $\le N/2<N$, and primes of $N-1$ are $\le N-1<N$). By the forward-direction argument plus the inductive hypothesis, the new generator lies in $K_{N-1}$, so $K_N=K_{N-1}$.

If $N$ is prime, then $N\mid\mathrm{sf}((N-1)N)$ and so $\sqrt N$ enters the generator set at rung $k=N-1$. Multiquadratic-field linear independence — Kronecker's theorem that $\{\sqrt{p_1\cdots p_r}:S\subseteq\{p_1,\ldots,p_r\}\}$ is $\mathbb Q$-linearly independent for any set of distinct primes (Lang, *Algebra* VI §1) — shows $\sqrt N\notin K_{N-1}=\mathbb Q(\sqrt p:p<N,\;p\text{ prime})$. Hence $K_{N-1}\subsetneq K_N$. $\square$

The dimensional axis $N\to N+1$ is therefore a **radical clock**: the field $K_N$ is the multiquadratic extension of $\mathbb Q$ generated by all primes up to $N$, and its growth rungs are exactly the prime rungs.

### 5.3 The dimensional axis in the apex framing

In \heb{ל}0's framing, the Helmert ladder is the dimensional axis of the apex. Each fixed $N$ supports a copy of the Fourier-Mellin surface $\mathcal M_x(\beta,c)$; varying $N$ moves between surfaces along the Helmert flag. Unit normalization (passing from $h_k$ to $e_k$) is the metric choice that exposes the radical arithmetic of [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504); metric-trick retention (keeping integer $h_k$ and carrying $M_N=NI_N-J_N$ as the bilinear form) hides the radicals in the metric instead.

The Helmert ladder and the Fourier basis are two orthogonal bases of $H_N$:
- Helmert: integer / rational, exposes radical arithmetic across the $N$-axis.
- Fourier (character): complex unitary, exposes conductor arithmetic at fixed $N$.

The **Helmert-Fourier transfer matrix** — the change-of-basis matrix between $\{e_k\}_{k=1}^{N-1}$ and $\{\chi_c\}_{c=1}^{N-1}$ — is the apex's arithmetic Jacobian between its dimensional and conductor axes. [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Conjecture 2 asks for the explicit factorization of this matrix into (trigonometric conductor data) × (radical normalization data); we record this here as the principal forward door of the dimensional axis (\hyperref[sec:6-3]{§6.3}).

### 5.4 Worked example: $N=4$

([\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) §3 Example, restated.) For $N=4$:
- $\|h_1\|=\sqrt 2$, $\|h_2\|=\sqrt 6$, $\|h_3\|=\sqrt{12}=2\sqrt 3$.
- $K_4=\mathbb Q(\sqrt 2,\sqrt 3)$.
- Composite rung $N=4$ adds no new generator: $\sqrt{12}=2\sqrt 3$ lies in $K_3$.

Worked example: $N=6$. The Helmert constants are $\sqrt 2,\sqrt 6,\sqrt{12},\sqrt{20},\sqrt{30}$. Squarefree kernels: $2,6,3,5,30$. The field is $K_6=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5)$ — no new generator at $N=6$ since $\sqrt{30}=\sqrt 2\sqrt 3\sqrt 5\in K_5$. Note that $N=6$ is composite and does not advance the radical clock; its arithmetic significance is on the conductor axis (cross-prime ANOVA, \hyperref[sec:4-5]{§4.5}), not on the dimensional axis.

The dimensional and conductor axes carry independent arithmetic content: the radical clock advances at *prime* $N$; the cross-prime interaction stratum activates at *composite* $N$ with multiple prime factors. The two arithmetics meet through the transfer matrix.

### 5.5 The Helmert-Fourier transfer matrix at $N=6$ {#sec:5-5}

We compute the transfer matrix explicitly at the cross-prime anchor $N=6$, anchoring the forward conjecture of \hyperref[sec:6-3]{§6.3} in a closed-form worked example.

Let $\omega:=e^{2\pi i/6}=\zeta_6$, so $\mathbb Q(\omega)=\mathbb Q(\zeta_6)$ is the $6$-th cyclotomic field. Let $\tilde\chi_c:=\chi_c/\sqrt N$ denote the $L^2$-normalized character and $e_k:=h_k/\sqrt{k(k+1)}$ the unit Helmert vector. The transfer matrix has entries
$$U_{kc}:=\langle e_k,\tilde\chi_c\rangle=\frac{1}{\sqrt{N\cdot k(k+1)}}\,\langle h_k,\chi_c\rangle,\qquad k,c\in\{1,\ldots,N-1\}.$$

\hypertarget{stmt:5-2}{}
**Proposition 5.2 (Closed form of $\langle h_k,\chi_c\rangle$).** For $1\le k\le N-1$ and $c\in\widehat{\mathbb Z/N}$ with $c\ne 0$,
$$\langle h_k,\chi_c\rangle=\frac{1-\omega^{kc}}{1-\omega^c}-k\,\omega^{kc}.$$
(The right-hand side is interpreted by continuity when $\omega^{kc}=1$: the first term then evaluates to $0$ since the numerator vanishes while $1-\omega^c\ne 0$, and the full expression simplifies to $-k$.) For $c=0$, $\langle h_k,\chi_0\rangle=0$ by centering.

**Proof.** $\langle h_k,\chi_c\rangle=\sum_s(h_k)_s\chi_c(s)=\sum_{s=0}^{k-1}\omega^{cs}-k\omega^{kc}$, and the geometric sum $\sum_{s=0}^{k-1}\omega^{cs}=(1-\omega^{kc})/(1-\omega^c)$ converges for $\omega^c\ne 1$. The $c=0$ case is $\sum_s(h_k)_s=k-k=0$. $\square$

**Radical-cyclotomic factorization.** $U_{kc}$ factors as
$$\boxed{U_{kc}=\frac{1}{\sqrt{N\cdot k(k+1)}}\cdot\left[\frac{1-\omega^{kc}}{1-\omega^c}-k\,\omega^{kc}\right],}$$
where the first factor is the *radical normalizer* on the Helmert (dimensional) axis — living in the multiquadratic field $K_N\subseteq\mathbb R$ — and the bracketed second factor is the *cyclotomic kernel* on the conductor (character) axis — living in $\mathbb Q(\zeta_N)$. Therefore every entry lies in the compositum $K_N\cdot\mathbb Q(\zeta_N)$, the natural arithmetic field of the transfer matrix.

**Specialization to $N=6$.** The radical normalizers $\sqrt{6\cdot k(k+1)}$ for $k=1,\ldots,5$ are
$$\sqrt{12}=2\sqrt 3,\quad\sqrt{36}=6,\quad\sqrt{72}=6\sqrt 2,\quad\sqrt{120}=2\sqrt{30},\quad\sqrt{180}=6\sqrt 5,$$
which span the radical field $\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5)=K_6$ (with $\sqrt{30}=\sqrt 2\sqrt 3\sqrt 5\in K_6$, no new generator at the composite rung $N=6$). The cyclotomic factor lives in $\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3})$. Hence
$$U_{kc}\in K_6\cdot\mathbb Q(\zeta_6)=\mathbb Q(\sqrt 2,\sqrt 3,\sqrt 5,\zeta_6),$$
the compositum of dimensions $[K_6:\mathbb Q]\cdot[\mathbb Q(\zeta_6):\mathbb Q]/[K_6\cap\mathbb Q(\zeta_6):\mathbb Q]=8\cdot 2/1=16$ over $\mathbb Q$ (the intersection is trivial since $K_6\subset\mathbb R$ while $\mathbb Q(\zeta_6)$ is a complex-multiplication (CM) field with $\sqrt 3\in\mathbb R$ but $\sqrt 3\notin\mathbb Q(\zeta_6)$, only $i\sqrt 3=\zeta_6-\zeta_6^{-1}$).

**Conductor block structure at $N=6$.** The characters partition by conductor (\hyperlink{stmt:4-1}{Proposition~4.1} extended to $N=p_1p_2$):
- $H_2=\mathrm{span}\{\chi_3\}$, with $\chi_3(s)=(-1)^s$ (the unique real non-trivial character, conductor $2$);
- $H_3=\mathrm{span}\{\chi_2,\chi_4\}$ (conductor $3$, conjugate pair);
- $H_6=\mathrm{span}\{\chi_1,\chi_5\}$ (conductor $6$, conjugate pair).

Computing the entire $c=3$ column explicitly (the real conductor-$2$ packet): with $\omega^3=-1$, \hyperlink{stmt:5-2}{Proposition~5.2} gives $\langle h_k,\chi_3\rangle=\tfrac{1-(-1)^k}{2}-k(-1)^k$, so the column $(\langle h_k,\chi_3\rangle)_{k=1}^5=(2,-2,4,-4,6)$ and
$$U_{\cdot,3}=\bigg(\frac{1}{\sqrt 3},\,-\frac{1}{3},\,\frac{\sqrt 2}{3},\,-\frac{2}{\sqrt{30}},\,\frac{1}{\sqrt 5}\bigg)^\top,$$
a vector with entries in $K_6$ alone (no cyclotomic content, as expected since $\chi_3$ is real).

The two complex-conjugate columns $(c=2,c=4)$ produce the $H_3$ block; the columns $(c=1,c=5)$ produce the $H_6$ block. Their entries combine the radical column-normalizers with cyclotomic-Gaussian-period factors from $\mathbb Q(\zeta_6)$; the full $5\times 5$ matrix $U$ is the apex's arithmetic Jacobian between the dimensional (Helmert/radical) and conductor (character/cyclotomic) axes at $N=6$.

The closed-form \hyperlink{stmt:5-2}{Proposition~5.2} establishes [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Conjecture 2 ("factorize the transfer matrix into trigonometric conductor data $\times$ radical normalization data") *at the level of individual entries*: each $U_{kc}$ is the product of one radical factor in $K_N$ and one cyclotomic factor in $\mathbb Q(\zeta_N)$. The remaining content of [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Conjecture 2 — interpreting the full matrix as a structured object, e.g., as a Gauss-sum / Vandermonde / DFT hybrid with explicit block-diagonalization over the conductor packets — is the topic of \hyperref[sec:6-3]{§6.3} (\heb{ל}9).

The doors below are clearly marked as forward content. \heb{ל}0 commits to none of them as main claims; each is named, scoped, and deferred to its own forthcoming paper.

## 6. Forward Directions {#sec:6}

### 6.1 Complex amplitudes and finite-dimensional quantum mechanics {#sec:6-1}

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Conjecture 4 proposes complex amplitudes: replace $a\in S^{N-1}_+\subset\mathbb R^N$ by $z\in S^{2N-1}\subset\mathbb C^N$, with closure $p_i=|z_i|^2/\sum_j|z_j|^2$. The projective space is $\mathbb{CP}^{N-1}$; the natural metric extension of Fisher–Rao is the Fubini–Study metric; the symmetry enlarges from $S_N$ to $U(N)$; the phase fiber over each simplex point is $U(1)^N/U(1)\cong T^{N-1}$.

This is, structurally, **finite-dimensional quantum mechanics on $\mathbb C^N$**. The real positive sector of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) is the diagonal $\mathbb R_{\ge 0}^N$ face of $\mathbb C^N$, equivalently the decoherent (phase-averaged) face of the projective Hilbert space. The Kummer cover of the simplex (the $(\mu_n)^N/\mu_n$ deck group of $n$-th-root branches) is the natural finite phase structure of the present framework; in the complex extension it becomes the literal $U(1)^N/U(1)$ gauge fiber of finite-dim QM.

The factor of 2 in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s Fisher–Rao distance $d_{FR}=2\arccos\sum\sqrt{p_iq_i}$ (with $\sum\sqrt{p_iq_i}$ the Bhattacharyya coefficient, Bhattacharyya 1943) becomes, in this extension, the standard $SU(2)\to SO(3)$ double-cover signature: the projective angle on $\mathbb{CP}^{N-1}$ is half the Riemannian angle on $S^{2N-1}$, and squaring amplitudes is the map that doubles angles.

Forward paper title (releasing soon): **[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex.**

### 6.2 Multiplicative character layer {#sec:6-2}

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) and \hyperref[sec:3]{§3} of \heb{ל}0 use **additive** characters of $\mathbb Z/N$: homomorphisms to $\mathbb C^\times$ defined on every element. Classical Dirichlet $L$-functions use **multiplicative** characters of $(\mathbb Z/N)^\times$: homomorphisms defined only on units.

These are dual but not identical. The natural multiplicative-character version of $\mathcal M_x$ would be a Dirichlet sum
$$\mathcal D_x(\beta,\psi)=\frac{1}{\varphi(N)}\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\,\overline{\psi(s)}$$
indexed by Dirichlet characters $\psi$ of $(\mathbb Z/N)^\times$. This produces Gauss sums, Kloosterman sums, and the natural finite analog of Dirichlet $L$-functions when $x$ encodes arithmetic information (e.g., the characteristic function of primes mod $N$).

Forward paper title (drafted): **[\heb{ל}8](https://doi.org/10.5281/zenodo.20437817) — The Multiplicative Apex and Finite Dirichlet Polynomials.**

### 6.3 Helmert-Fourier transfer matrix {#sec:6-3}

The change-of-basis matrix between the Helmert basis $\{e_k\}_{k=1}^{N-1}$ and the character basis $\{\chi_c\}_{c=1}^{N-1}$ of $H_N\otimes\mathbb C$ should decompose explicitly into trigonometric conductor data and radical normalization data:
$$\langle e_k,\chi_c\rangle=\frac{1}{\sqrt{k(k+1)}}\cdot\big(\text{trigonometric kernel of }k\text{ and }c\big).$$

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) Conjecture 2 asks for the closed form. \heb{ל}0's contribution to the conjecture is the framing: the transfer matrix is the apex's arithmetic Jacobian between the dimensional and conductor axes, and its entries are expected to factor as (cyclotomic conductor data) × (radical Helmert data).

Forward paper title (drafted): **[\heb{ל}9](https://doi.org/10.5281/zenodo.20437843) — The Helmert-Fourier Transfer Matrix.** (Closed-form entries proven in \hyperref[sec:5-5]{§5.5}; remaining content: full block-diagonalization over conductor packets, Gauss-sum decomposition.)

### 6.4 $m$-Power gauge for $|m|\ge 3$

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §8 sketches the $m$-power closure for $m\ge 3$ and notes that the conductor selection rule generalizes to $a_1+\cdots+a_m\equiv c\pmod N$. The $m=3$ row of the corridor table (cubic substance / volume / chirality / four-wave mixing / Waring on cubes / Kummer cubic extensions) is the natural next worked rung, with the $m=-3$ polar partner (inverse-cube / dipole-dipole / pure cubic compliance) as its dual.

For complex amplitudes, the $m$-power closure introduces $\mu_m$ branch structure, and the radical field becomes a Kummer extension $\mathbb Q(\zeta_m,\sqrt[m]{\cdot})$ in place of [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s quadratic clock. The radical clock generalizes to a **Kummer clock**, with each integer $m$-rung adding cyclotomic and Kummer generators.

Forward paper title (drafted): **[\heb{ל}10](https://doi.org/10.5281/zenodo.20437847) — The Kummer Clock and the $m$-Power Gauge Hierarchy.**

### 6.5 Tropical / Maslov boundary

The $\beta\to\pm\infty$ limits of $K_y$ and $\mathcal M_x$ are Maslov dequantizations to max-plus and min-plus algebra. The corridor is a one-parameter deformation between ordinary categorical statistics and tropical statistics. The full tropical theory at the boundary should connect:
- Large-deviation theory (Cramér, Sanov, Donsker–Varadhan);
- Rényi/multifractal spectra at integer order;
- Tropical geometry of the simplex (Mikhalkin, Itenberg, Speyer–Sturmfels);
- Argmax / argmin selection on the support faces of the simplex.

A dedicated treatment of this boundary is planned as a forthcoming companion paper.

### 6.6 Holomorphic flow on the apex {#sec:6-6}

$\mathcal M_x(\beta,c)$ is entire in $\beta$ for fixed $c$ (as a finite sum of exponentials in $\beta$), so its Taylor expansion at $\beta=0$ (the moment/cumulant samples) and its integer values at $\beta=m\in\mathbb Z$ (the closure samples) are two natural sampling regimes on the same entire function. The contour-deformation between $\beta=0$ and $\beta=m$ in the complex plane interpolates the two diagonals as a holomorphic isotopy. Analytic continuation, contour residues, and the zero structure of $\mathcal M_x$ — its Lee–Yang points — are the natural objects for an analytic study of the apex.

For arithmetic ledgers (where $y_i$ encodes prime structure), the zeros of $\mathcal M_x(\beta,c)$ in $\beta$ are the natural finite-categorical analog of the zero locus of Dirichlet $L$-functions. Their distribution — how zeros arrange in $\beta$, how cross-prime interaction affects degeneracies — is the natural analytic object for an arithmetic study of the apex.

A dedicated analytic treatment of $\mathcal M_x$'s zero structure is planned as a forthcoming companion paper. (Toy $N=2$ case proven in \hyperlink{stmt:2-5}{Proposition~2.5}.)

---

## 7. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) through [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) as Worked Cells {#sec:7}

We close by repositioning each existing paper as a worked cell of the apex grid. The grid axes are $(N,\beta,c,n)$: simplex dimension, gauge exponent, conductor index, cumulant order.

### 7.1 [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Native Simplicial Chart {#sec:7-1}

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) establishes the chart that the apex lives on. It identifies $H_N$ as the tangent space; identifies Fisher–Rao as the round sphere metric pulled back through the square-root map; identifies $\mathrm{SO}(H_N)$ as the tangent isometry group at the uniform. In the apex framing, [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) is the **chart at fixed $N$, all gauges**; the square-root map is the AJLS half-density chart, equivalently the gauge corridor at $\beta=2$ on the amplitude side. The factor of 2 in the Fisher–Rao distance is the projective-angle doubling of the cumulant-root diagonal at $n=2$.

### 7.2 [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Cumulant Tower as Effective Action {#sec:7-2}

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) establishes the one-functional generation principle: $\Phi=\log Z$ generates the cumulant tower. In the apex framing, [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s $\Phi$ is $K_y(\beta)$ evaluated at $\beta=1$ (the e-flat / softmax gauge); its Taylor expansion at the uniform is the cumulant tower along the **moment diagonal** of $\mathcal M_x$ at $c=0$, with cumulants recovered from moments via standard partition-subtraction (Remark 3.3a). [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s leap from order 2 to order 3 — the Amari–Chentsov tensor as first invariant beyond Riemannian — is the first cell of the moment diagonal where the conductor selection rule (when labels carry $\mathbb Z/N$ structure) becomes non-trivial. Centering of $y$ makes moment and cumulant coincide at order 3, so [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s cubic vertex reads identically through either lens.

### 7.3 [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Character Orthogonality

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) introduces the structured labels and reads [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s cubic tensor through the character basis. In the apex framing, [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) is **the activation of the conductor index $c$**: $\mathcal M_x(\beta,c)$ at non-trivial $c$ replaces $K_y(\beta)$. [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s selection rule $a+b+c\equiv 0\pmod N$ is the $n=3$ slice of the moment diagonal (\hyperlink{stmt:3-3}{Theorem~3.3}, \hyperlink{stmt:3-4}{Corollary~3.4}). [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s conductor packets $H_d$ are the eigenspaces of the apex generator's character decomposition.

### 7.4 [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — Helmert-Simplicial Residue Ladder

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) is the dimensional axis of the apex (\hyperref[sec:5]{§5}). The radical clock $K_N=\mathbb Q(\sqrt p:p\le N)$ is the metric arithmetic accumulated by climbing the dimensional ladder under unit normalization. The Helmert basis is the orthogonal rational basis of $H_N$ complementary to the character basis; the transfer matrix between them is forward (\hyperref[sec:6-3]{§6.3}).

### 7.5 [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — Harmonic-Simplicial Dual Gauge

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) establishes the polar pair structure $(M_r,M_{-r})$ and the parity decomposition of cumulants. In the apex framing, [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) is **the parity reading of the gauge corridor**: $K_y(\beta)+K_y(-\beta)$ doubles even cumulants and $K_y(\beta)-K_y(-\beta)$ doubles odd cumulants (\hyperlink{stmt:2-2}{Theorem~2.2.4}). [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s $\beta=\pm 1$ pair is the first non-trivial parity sample; its $\beta=\pm 2$ pair (continued in [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)) is the next.

### 7.6 [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — RMS-Simplicial Quadratic Gauge

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) establishes the $\beta=2$ gauge and identifies it as Born closure / Fisher–Rao amplitude. In the apex framing, [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) is **the closure diagonal at $m=2$**: $\mathcal M_x(2,c)$ produces the RMS-conductor mixing rule $a+b-c\equiv 0\pmod N$ (\hyperlink{stmt:3-5}{Theorem~3.5}). [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) §8's $m$-wave generalization is the closure diagonal extended to all integer $m$; [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) Conjecture 4 (complex amplitudes) is the forward door \hyperref[sec:6-1]{§6.1}; [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428)'s Theorem 7.1 (radical universality for sum-of-squares) is the integer-arithmetic shadow of the $m=2$ closure rung.

### 7.7 Grid summary

\begin{center}
\renewcommand{\arraystretch}{1.35}
\begin{tabular}{@{}p{0.10\linewidth}p{0.38\linewidth}p{0.44\linewidth}@{}}
\toprule
\textbf{Paper} & \textbf{Apex slice} & \textbf{Worked content} \\
\midrule
\href{https://doi.org/10.5281/zenodo.20336872}{\heb{ל}1} & $H_N$ chart, all gauges & square-root sphere, Fisher–Rao, rotation group \\
\midrule
\href{https://doi.org/10.5281/zenodo.20338126}{\heb{ל}2} & $K_y(\beta)$ Taylor jets at $\beta=0$, $c=0$ & cumulant tower, leap to order 3 \\
\midrule
\href{https://doi.org/10.5281/zenodo.20339049}{\heb{ל}3} & $\mathcal M_x$ activated; $n=3$ slice of moment diagonal & character orthogonality, cubic selection rule \\
\midrule
\href{https://doi.org/10.5281/zenodo.20383504}{\heb{ל}4} & dimensional axis $N\to N+1$ & Helmert ladder, multiquadratic radical clock \\
\midrule
\href{https://doi.org/10.5281/zenodo.20388419}{\heb{ל}5} & parity pair $(\beta,-\beta)$ of $K_y$ & harmonic dual, even/odd cumulant split \\
\midrule
\href{https://doi.org/10.5281/zenodo.20392428}{\heb{ל}6} & closure diagonal at $m=2$ & RMS / Born, conductor mixing, radical universality \\
\midrule
\href{https://doi.org/10.5281/zenodo.20423985}{\heb{ל}0} & the surface itself & $K_y(\beta)$, $\mathcal M_x(\beta,c)$, both diagonals, prime decomposition, all forward doors \\
\bottomrule
\end{tabular}
\end{center}

Six worked cells; \heb{ל}0 names the surface they sample.

---

## 8. Coda {#sec:8}

The trilogy *Identifying 3* and its successor papers identify the third order in five independent senses: cumulant order beyond Gaussian, simplex dimension beyond Bernoulli, cubic conductor selection rule, mean-triad parity center, and first non-trivial integer power gauge. \heb{ל}0's apex framing collapses these to one structural fact:

> *Order 3 is the first cell of the moment diagonal at which the conductor selection rule, the closure mixing rule, and the cross-character coupling all carry non-trivial content — coincident with the cumulant tensor at this order thanks to centering.*

The trilogy was right to identify "3." \heb{ל}0 identifies the surface on which "3" appears, and the axes by which it can be sampled at any other order.

The one-sentence apex:

> **The structured categorical simplex is governed by the Fourier-Mellin transform $\mathcal M_x(\beta,c)$ of its centered log-ledger — a finite-categorical analog of a Dirichlet polynomial, holomorphic in $\beta$, character-indexed in $c$, equipped with the natural Fisher-replicator flow, factorizing via CRT over the primes dividing $N$ exactly under ledger separability, with cumulant tensors as its Taylor jets, power closures as its integer samples, tropical limits as its $\beta=\pm\infty$ boundary, and the Helmert dimensional ladder supplying the cross-$N$ radical arithmetic that the conductor lattice cannot see at fixed $N$.*

And the one-sentence opening, which remains:

> **A statistical theory begins by answering: what is additive?**

Everything between the two sentences is the catalog of what is read off the apex when the question is answered.

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The collaborations were intellectually substantive: AI partners contributed insights, proposed theorems and conjectures, surfaced relevant literature, verified derivations, and iterated on exposition. I acknowledge this use transparently; the selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References

### \heb{ל}-series (companion papers)

- Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).
- Murillo Montero, L. (2026). *[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).
- Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).
- Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert-Simplicial Residue Ladder.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504).
- Murillo Montero, L. (2026). *[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — The Harmonic-Simplicial Dual Gauge.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20388419](https://doi.org/10.5281/zenodo.20388419).
- Murillo Montero, L. (2026). *[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — The RMS-Simplicial Quadratic Gauge.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392428](https://doi.org/10.5281/zenodo.20392428).
- Murillo Montero, L. (2026). *[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442).
- Murillo Montero, L. (2026). *[\heb{ל}8](https://doi.org/10.5281/zenodo.20437817) — The Multiplicative Apex and Finite Dirichlet Polynomials.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20437817](https://doi.org/10.5281/zenodo.20437817).
- Murillo Montero, L. (2026). *[\heb{ל}9](https://doi.org/10.5281/zenodo.20437843) — The Helmert-Fourier Transfer Matrix.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20437843](https://doi.org/10.5281/zenodo.20437843).
- Murillo Montero, L. (2026). *[\heb{ל}10](https://doi.org/10.5281/zenodo.20437847) — The Kummer Clock and the $m$-Power Gauge Hierarchy.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20437847](https://doi.org/10.5281/zenodo.20437847).
- Murillo Montero, L. (2026). *[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier-Mellin Simplex.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20423985](https://doi.org/10.5281/zenodo.20423985). (This work.)

### Information geometry and statistics

- Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Lecture Notes in Statistics 28. Berlin: Springer. ISBN 978-0-387-96056-2. [DOI: 10.1007/978-1-4612-5056-2](https://doi.org/10.1007/978-1-4612-5056-2).
- Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs, Vol. 191. Providence, RI: American Mathematical Society. ISBN 978-0-8218-0531-2. [AMS page](https://bookstore.ams.org/mmono-191).
- Ay, N., Jost, J., Lê, H. V., and Schwachhöfer, L. (2017). *Information Geometry.* Ergebnisse der Mathematik und ihrer Grenzgebiete 64. Cham: Springer. ISBN 978-3-319-56477-7. [DOI: 10.1007/978-3-319-56478-4](https://doi.org/10.1007/978-3-319-56478-4).
- Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs, Vol. 53. Providence, RI: American Mathematical Society. ISBN 978-0-8218-4502-8.
- Fisher, R. A. (1925). Theory of statistical estimation. *Proceedings of the Cambridge Philosophical Society* 22, 700–725. [DOI: 10.1017/S0305004100009580](https://doi.org/10.1017/S0305004100009580).
- Rao, C. R. (1945). Information and the accuracy attainable in the estimation of statistical parameters. *Bulletin of the Calcutta Mathematical Society* 37, 81–91. (Reprinted in *Breakthroughs in Statistics*, Vol. I, Springer 1992. [DOI: 10.1007/978-1-4612-0919-5_16](https://doi.org/10.1007/978-1-4612-0919-5_16).)
- Bhattacharyya, A. (1943). On a measure of divergence between two statistical populations defined by their probability distributions. *Bulletin of the Calcutta Mathematical Society* 35, 99–109.
- Brillinger, D. R. (1975). *Time Series: Data Analysis and Theory.* New York: Holt, Rinehart and Winston. SIAM reissue 2001. ISBN 978-0-89871-501-9. [DOI: 10.1137/1.9780898719246](https://doi.org/10.1137/1.9780898719246).
- Rockafellar, R. T. (1970). *Convex Analysis.* Princeton Mathematical Series 28. Princeton, NJ: Princeton University Press. ISBN 978-0-691-01586-6. [DOI: 10.1515/9781400873173](https://doi.org/10.1515/9781400873173).

### Compositional and power-mean

- Aitchison, J. (1986). *The Statistical Analysis of Compositional Data.* London: Chapman & Hall. ISBN 978-0-412-28060-3. [DOI: 10.1007/978-94-009-4109-0](https://doi.org/10.1007/978-94-009-4109-0).
- Pawlowsky-Glahn, V., Egozcue, J. J., and Tolosana-Delgado, R. (2015). *Modeling and Analysis of Compositional Data.* Chichester: John Wiley & Sons. ISBN 978-1-118-44306-4. [DOI: 10.1002/9781119003144](https://doi.org/10.1002/9781119003144).
- Hardy, G. H., Littlewood, J. E., and Pólya, G. (1934). *Inequalities.* Cambridge: Cambridge University Press. 2nd ed. 1952; Cambridge Mathematical Library reissue 1988. ISBN 978-0-521-35880-4.

### Algebra and number theory

- Lang, S. (2002). *Algebra.* Revised 3rd ed. Graduate Texts in Mathematics 211. New York: Springer. ISBN 978-0-387-95385-4. [DOI: 10.1007/978-1-4613-0041-0](https://doi.org/10.1007/978-1-4613-0041-0).
- Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory.* AMS Colloquium Publications 53. Providence, RI: American Mathematical Society. ISBN 978-0-8218-3633-0.
- Pontryagin, L. S. (1939). *Topological Groups.* Princeton, NJ: Princeton University Press. (Translated by E. Lehmer.)

### Combinatorics and Möbius / ANOVA

- Rota, G.-C. (1964). On the foundations of combinatorial theory I. Theory of Möbius functions. *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* 2, 340–368. [DOI: 10.1007/BF00531932](https://doi.org/10.1007/BF00531932).
- Stanley, R. P. (2012). *Enumerative Combinatorics, Volume 1.* 2nd ed. Cambridge Studies in Advanced Mathematics 49. Cambridge: Cambridge University Press. ISBN 978-1-107-60262-5.
- McGill, W. J. (1954). Multivariate information transmission. *Psychometrika* 19, 97–116. [DOI: 10.1007/BF02289159](https://doi.org/10.1007/BF02289159).
- Han, T. S. (1980). Multiple mutual informations and multiple interactions in frequency data. *Information and Control* 46, 26–45. [DOI: 10.1016/S0019-9958(80)90478-7](https://doi.org/10.1016/S0019-9958(80)90478-7).
- Yeung, R. W. (1991). A new outlook on Shannon's information measures. *IEEE Transactions on Information Theory* 37, 466–474. [DOI: 10.1109/18.79902](https://doi.org/10.1109/18.79902).

### Evolutionary dynamics and Shahshahani metric

- Shahshahani, S. (1979). *A New Mathematical Framework for the Study of Linkage and Selection.* Memoirs of the American Mathematical Society, no. 211. Providence, RI: AMS. ISBN 978-0-8218-2211-1.
- Taylor, P. D. and Jonker, L. B. (1978). Evolutionarily stable strategies and game dynamics. *Mathematical Biosciences* 40, 145–156. [DOI: 10.1016/0025-5564(78)90077-9](https://doi.org/10.1016/0025-5564(78)90077-9).
- Hofbauer, J. and Sigmund, K. (1998). *Evolutionary Games and Population Dynamics.* Cambridge: Cambridge University Press. ISBN 978-0-521-62570-8. [DOI: 10.1017/CBO9781139173179](https://doi.org/10.1017/CBO9781139173179).

### Lee–Yang, tropical / Maslov, and large-deviation boundary

- Lee, T. D. and Yang, C. N. (1952). Statistical theory of equations of state and phase transitions. II. Lattice gas and Ising model. *Physical Review* 87, 410–419. [DOI: 10.1103/PhysRev.87.410](https://doi.org/10.1103/PhysRev.87.410).
- Maslov, V. P. (1987). On a new superposition principle for optimization problems. *Russian Mathematical Surveys* 42(3), 39–48. [DOI: 10.1070/RM1987v042n03ABEH001440](https://doi.org/10.1070/RM1987v042n03ABEH001440).
- Litvinov, G. L. and Maslov, V. P., eds. (2005). *Idempotent Mathematics and Mathematical Physics.* Contemporary Mathematics 377. Providence, RI: American Mathematical Society. ISBN 978-0-8218-3538-8.
- Speyer, D. and Sturmfels, B. (2009). Tropical mathematics. *Mathematics Magazine* 82, 163–173. [DOI: 10.4169/193009809X468760](https://doi.org/10.4169/193009809X468760).
- Dembo, A. and Zeitouni, O. (1998). *Large Deviations Techniques and Applications.* 2nd ed. Applications of Mathematics 38. New York: Springer. ISBN 978-0-387-98406-3. [DOI: 10.1007/978-3-642-03311-7](https://doi.org/10.1007/978-3-642-03311-7).

### Quantum information geometry and monotone metrics

- Morozova, E. A. and Chentsov, N. N. (1991). Markov invariant geometry on manifolds of states. *Journal of Soviet Mathematics* 56(5), 2648–2669. [DOI: 10.1007/BF01095975](https://doi.org/10.1007/BF01095975). (English translation; Russian original *Itogi Nauki i Tekhniki* 1990.)
- Petz, D. (1996). Monotone metrics on matrix spaces. *Linear Algebra and its Applications* 244, 81–96. [DOI: 10.1016/0024-3795(94)00211-8](https://doi.org/10.1016/0024-3795(94)00211-8).
- Petz, D. and Tóth, G. (1993). The Bogoliubov inner product in quantum statistics. *Letters in Mathematical Physics* 27, 205–216. [DOI: 10.1007/BF00739578](https://doi.org/10.1007/BF00739578).
- Umegaki, H. (1962). Conditional expectation in an operator algebra IV (entropy and information). *Kodai Mathematical Seminar Reports* 14(2), 59–85. [DOI: 10.2996/kmj/1138844604](https://doi.org/10.2996/kmj/1138844604).

### Helmert

- Helmert, F. R. (1876). *Die Genauigkeit der Formel von Peters zur Berechnung des wahrscheinlichen Beobachtungsfehlers directer Beobachtungen gleicher Genauigkeit.* Astronomische Nachrichten 88, 113–132. [Wikipedia: Helmert transformation](https://en.wikipedia.org/wiki/Helmert_transformation).
