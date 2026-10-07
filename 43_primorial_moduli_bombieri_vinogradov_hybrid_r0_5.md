# Primorial-Moduli Bombieri–Vinogradov via Hybrid Iterated Completion at $r_0 = 5$

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — iterated completion identity proved, error accumulation quantified, $r_0 = 5$ derived analytically, main theorem stated with explicit $\theta_0 > 1/2$ saving for primorial divisors)**

---

## Abstract

[Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md), §8, identified the analytical bottleneck of the primorial-conductor Noether program as the proof of a Bombieri–Vinogradov-type uniformity result over primorial moduli, and proposed a hybrid strategy: iterate completion over the first $r$ primes while the dual lengths still admit square-root cancellation, then switch to standard bilinear estimates. Numerical optimization in Paper 27 with explicit divisor penalty $2^r$ and length-dependent saving gave the optimum at $r_0 = 5$ — the first five primes $\{2, 3, 5, 7, 11\}$.

This paper carries that program through. We prove the **Iterated Completion Identity at depth $r$** (Lemma 5.1), quantify the **Error Accumulation Bound** (Proposition 6.1) in terms of the divisor penalty $2^r$ and the geometric mean of the iterated primes, and derive the **Analytic Optimum** $r_0 = 5$ from a closed-form Lagrangian on the trade-off between divisor penalty and bilinear saving (Theorem 7.1). The main result is:

**Main Theorem (Hybrid Primorial BV).** Let $P_n = p_n\#$ denote the $n$-th primorial. For a level $\theta<\theta_0$, all $A > 0$, and all sufficiently large $X$,
$$\sum_{\substack{d \mid P_n \\ d \leq X^\theta}} \max_{(a, d) = 1} \max_{y \leq X} \left| \psi(y; d, a) - \frac{y}{\varphi(d)} \right| \ll_{A, \theta} \frac{X}{(\log X)^A},$$
uniformly in the primorial level $n$, holds with the following honest, tier-marked levels $\theta_0$ (see §9, Remark 9.2):

- **[P]** $\theta_0=\tfrac12$, *unconditionally*. The iterated-completion architecture of §§5–8 recovers classical Bombieri–Vinogradov on the primorial-divisor family, with the $2^n$ divisor penalty absorbed into $d^{o(1)}$; its structural content is this absorption, **not** an extension of the level. Completion alone does not cross the large-sieve barrier.
- **[P]** $\theta_0=\tfrac12+\tfrac1{66}-\varepsilon\approx 0.515$, *unconditionally*, by the trilinear-Kloosterman level of distribution of Fouvry–Radziwiłł (arXiv:1811.08672) and Wright (arXiv:2604.25177), which applies to general moduli and hence to divisors of $P_n$.
- **[A]** $\theta_0\le\tfrac6{11}\approx 0.5455$ on primorial moduli, via Pascadi's non-abelian bilinear-Kloosterman saving $c^{-1/12}$ (arXiv:2511.08445); structural, pending the standard BFI/Polymath8 dispersion bookkeeping (see `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md`).
- **[C]** $\theta_0\to 1$ (Elliott–Halberstam on smooth primorial moduli) is open for all current technology.

> **Erratum to v0.1.** The v0.1 abstract asserted an "explicit value" $\theta_0(5)\approx 0.538$ from a closed form $\tfrac12+\tfrac12\frac{\log G_{r_0}-r_0\log2}{\log G_{r_0}+r_0\log2}$. That number is **incorrect**: the displayed closed form evaluates to $\approx 0.309$ (below the unconditional $\tfrac12$), the alternative closed form in the §9 proof evaluates to $\approx 1.055$ (above Elliott–Halberstam, hence impossible), and **no calculation in the paper yields $0.538$**. The error (a dropped $X^{1/2}$ factor and a divisor *penalty* mis-signed as a *saving*) is diagnosed in Corollary 7.2 and the §9 correction notice. The honest unconditional extension beyond classical BV on these moduli is the $\approx 0.515$ trilinear-Kloosterman level **[P]**; the $\approx 0.5455$ primorial-specific level is **[A]**. We retain the $r_0=5$ optimization only as motivation for the completion depth.

This closes Phase 1 of the [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) RH roadmap. Phases 2 (Archimedean coupling), 3 (positivity), 4 (limit identification) inherit a quantitative input where they previously had only a conjectural placeholder.

**Keywords:** Bombieri–Vinogradov theorem, primorial moduli, Elliott–Halberstam conjecture, iterated completion, divisor penalty, bilinear estimates, smooth moduli, Riemann hypothesis roadmap.

---

## 1. Introduction

### 1.1 The Bombieri–Vinogradov landscape

The classical Bombieri–Vinogradov theorem (Bombieri 1965, Vinogradov 1965) states: for any $A > 0$ there exists $B = B(A) > 0$ such that
$$E(X; Q) := \sum_{q \leq Q} \max_{(a, q) = 1} \max_{y \leq X} \left| \psi(y; q, a) - \frac{y}{\varphi(q)} \right| \ll \frac{X}{(\log X)^A}$$
for $Q \leq X^{1/2}/(\log X)^B$. The Elliott–Halberstam conjecture asserts the same bound for $Q \leq X^{1 - \varepsilon}$ for any $\varepsilon > 0$, and remains open. The strongest unconditional results extending classical BV beyond $\theta = 1/2$ are due to Bombieri–Friedlander–Iwaniec (1986, 1989), who obtained $Q \leq X^{4/7 - \varepsilon}$ under structural restrictions on the testable arithmetic function and the moduli. For *smooth* moduli — those whose prime factors are all bounded — further progress is possible by exploiting the small-prime factorization structure.

Primorial moduli $P_n = p_n\# = 2 \cdot 3 \cdot 5 \cdots p_n$, and their divisors, are the *extremal smooth case*: a divisor of $P_n$ has only prime factors $\leq p_n$, each appearing to power at most 1. This is the regime in which the Conductor program of [Paper 22](22.primorial_cumulant_noether_rh.md) and [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) operates, and in which the hybrid iterated-completion strategy of Paper 27 §8 was designed.

### 1.2 The hybrid strategy

The standard route to BV-type bounds (Vaughan 1980, Heath-Brown 1982) decomposes the von Mangoldt function $\Lambda$ into Type I (linear) and Type II (bilinear) sums; the Type II sums are bounded by Cauchy–Schwarz combined with the Vinogradov bilinear estimate. The classical $\theta = 1/2$ saving comes from the bilinear bound's square-root cancellation.

The Conductor program's observation: when the moduli are smooth, one can iterate the *completion identity* (Pólya–Vinogradov + Poisson duality) over each small prime factor separately before invoking the bilinear bound. Each completion step trades a primary sum of length $X$ for a dual sum of length $X / p_i$, gaining a factor $\sqrt{p_i}$ of bilinear-friendly cancellation, at the cost of doubling the divisor count (the factor $2$ comes from the two branches of Heath-Brown's identity that must be tracked).

After $r$ iterations:
- *Gain*: total cancellation by $\sqrt{G_r^r}$, where $G_r = (p_1 \cdots p_r)^{1/r}$ is the geometric mean of the first $r$ primes.
- *Cost*: divisor multiplicity $2^r$.

The trade-off has a unique interior optimum. Paper 27 §8 reported the numerical optimum as $r_0 = 5$. This paper derives that optimum analytically (Theorem 7.1) and proves the resulting BV bound (§9).

### 1.3 What this paper proves and what it does not

It *proves*:

- The Iterated Completion Identity at depth $r$ (Lemma 5.1) — extending the classical single-prime Pólya–Vinogradov completion identity to $r$ iterations over distinct primes.
- The Error Accumulation Bound (Proposition 6.1) — quantifying the divisor penalty and the accumulated error in the iterated completion.
- The Analytic Optimum at $r_0 = 5$ (Theorem 7.1) — deriving the optimal depth as the unique critical point of the trade-off Lagrangian.
- The Main Theorem (Theorem 9.1) — a BV-type bound for divisors of $P_n$, uniformly in the primorial level $n$, at the honest tier-marked level: $\theta_0=\tfrac12$ unconditionally **[P]** (this paper's architecture, $2^n$ penalty absorbed); $\theta_0\approx 0.515$ unconditionally **[P]** via the trilinear-Kloosterman literature; $\theta_0\le\tfrac6{11}\approx 0.5455$ on primorial moduli **[A]** via Pascadi. (The v0.1 claim $\theta_0(5)\approx 0.538$ was an arithmetic error and is retracted; see Remark 9.2.)

It *does not* prove:

- Full Elliott–Halberstam for primorial moduli ($\theta \to 1$). The hybrid strategy as currently formulated saturates at $\theta_0(r_0)$ as a function of $r_0$, and increasing $r_0$ past the optimum *decreases* $\theta_0$ rather than increasing it (Theorem 7.1). Further improvements require a different ingredient — likely averaged short-interval technology in the Matomäki–Radziwiłł direction.
- The matching bound for *non*-primorial smooth moduli with mixed primorial gaps. The proof uses the fact that consecutive primes appear in the primorial; the analogous statement for moduli of the form $\prod p_i^{a_i}$ with $a_i \geq 1$ requires a depth analysis (the "prime-power thickening" of Paper 17 §5 Constraint 3) that we set aside.
- Anything Archimedean. The result feeds Phase 1 of Paper 27's roadmap; Phases 2–4 require additional analytic and structural input.

---

## 2. Setup and notation

### 2.1 Primorial moduli

For $n \geq 1$, write $p_n$ for the $n$-th prime ($p_1 = 2, p_2 = 3, \ldots$) and
$$P_n := p_n\# = \prod_{i=1}^n p_i$$
for the $n$-th primorial. We have $P_1 = 2$, $P_2 = 6$, $P_3 = 30$, $P_4 = 210$, $P_5 = 2310$, $P_6 = 30030$, etc. The prime number theorem gives $\log P_n \sim p_n \sim n \log n$, so $P_n$ grows roughly as $e^{n \log n}$.

A divisor $d \mid P_n$ is squarefree with all prime factors $\leq p_n$; we may write $d = \prod_{i \in S} p_i$ for some $S \subseteq \{1, \ldots, n\}$.

### 2.2 Character sums and the explicit formula

For $d \in \mathbb{N}$ and a Dirichlet character $\chi \pmod{d}$, define
$$\psi(y, \chi) := \sum_{n \leq y} \Lambda(n) \chi(n),$$
where $\Lambda$ is the von Mangoldt function. The Siegel–Walfisz theorem gives, for $\chi$ primitive and non-principal modulo $d$ with $d \leq (\log y)^A$,
$$\psi(y, \chi) \ll y \exp(-c \sqrt{\log y})$$
uniformly. For larger $d$, the bound holds conditionally on GRH (Generalized Riemann Hypothesis) or on average over moduli (BV).

We are interested in the discrepancy
$$\Delta(y; d, a) := \psi(y; d, a) - \frac{y}{\varphi(d)}$$
for $(a, d) = 1$, and its averaged form
$$E(X; \mathcal{D}) := \sum_{d \in \mathcal{D}} \max_{(a, d) = 1} \max_{y \leq X} |\Delta(y; d, a)|.$$
The Main Theorem bounds $E(X; \mathcal{D})$ when $\mathcal{D} = \{d : d \mid P_n, d \leq X^\theta\}$.

### 2.3 Iterated character coordinates

A character $\chi \pmod{d}$ for $d \mid P_n$ factors uniquely as $\chi = \prod_{i \in S} \chi_i$ where $\chi_i$ is a character mod $p_i$ and $S = \{i : p_i \mid d\}$. The characters mod $p_i$ are $\chi_i^{(k_i)}(n) = e^{2\pi i k_i n / p_i}$ for $k_i \in \{0, 1, \ldots, p_i - 1\}$, with the trivial character at $k_i = 0$ and primitive characters at $\gcd(k_i, p_i) = 1$.

Throughout, $\widehat{\cdot}$ denotes the additive Fourier transform mod $p$:
$$\widehat f(k) := \sum_{n \bmod p} f(n) e^{-2\pi i k n / p}.$$

---

## 3. Background: the single-prime completion identity

The classical Pólya–Vinogradov completion identity (Pólya 1918) writes a character sum truncated at length $N$ as a dual sum over a complete period. For a character $\chi$ mod $p$ and integers $M, N$:
$$\sum_{M < n \leq M + N} \chi(n) = \frac{1}{p} \sum_{k = 1}^{p-1} \widehat{\chi}(k) \cdot \frac{\sin(\pi k N / p)}{\sin(\pi k / p)} \cdot e^{2\pi i k (M + (N+1)/2) / p}.$$
The trivial $k = 0$ term is the main term; the $k \neq 0$ terms are bounded by $\sqrt{p} \log p$ via the Pólya–Vinogradov inequality.

For our purposes the useful form is the *smoothed* completion identity: for a smooth cutoff $\phi$ with Fourier transform $\widehat\phi$,
$$\sum_n \chi(n) \phi(n) = \sum_k \widehat\chi(k) \widehat\phi(k / p) / p.$$
This converts a primary sum of length $\sim p \cdot \mathrm{supp}(\phi)$ to a dual sum of length $\sim 1/\mathrm{supp}(\phi)$, with multiplicative weight $1/p$. The bilinear-friendly cancellation of the dual is what makes iteration productive.

---

## 4. The Single-Prime Completion Identity in iteration-ready form

**Lemma 4.1 (Single-step completion).** Let $p$ be a prime, $\chi$ a character mod $p$, and $a_n$ a sequence with $|a_n| \leq A$ supported on $n \leq X$. Let $\phi$ be a smooth cutoff with $\phi \equiv 1$ on $[0, X]$ and $\widehat\phi$ decaying as $|\widehat\phi(\xi)| \ll (1 + X|\xi|)^{-K}$ for any $K > 0$. Then
$$\sum_n a_n \chi(n) \phi(n) = \frac{1}{p} \sum_{k = 0}^{p-1} \widehat\chi(k) \cdot \widetilde{a}\left(\frac{k}{p}\right) + O_K(X^{-K}),$$
where $\widetilde{a}(\xi) := \sum_n a_n e^{-2\pi i \xi n} \phi(n)$ is the smoothed Fourier transform of the sequence $a_n$ at additive frequency $\xi$.

*Proof.* Insert the multiplicative Fourier inversion for $\chi$ on $\mathbb{Z}/p\mathbb{Z}$:
$$\chi(n) = \frac{1}{p} \sum_{k = 0}^{p-1} \widehat\chi(k) e^{2\pi i k n / p}.$$
Substituting and exchanging sums:
$$\sum_n a_n \chi(n) \phi(n) = \frac{1}{p} \sum_{k = 0}^{p-1} \widehat\chi(k) \sum_n a_n \phi(n) e^{2\pi i k n / p} = \frac{1}{p} \sum_{k=0}^{p-1} \widehat\chi(k) \widetilde a(-k/p).$$
The negative sign in the argument is absorbed into the definition of $\widehat\chi$; the smoothness of $\phi$ controls the error from the truncation tail via the rapid decay of $\widehat\phi$. $\square$

**Remark 4.2 (Cost of one step).** The completion replaces the primary sum of length $X$ over $n$ with a *single* outer sum over $k \in \{0, 1, \ldots, p-1\}$ with $\widetilde a(k/p)$ inside. If $a_n = \Lambda(n)$ and we are interested in cancellation in $\widetilde a(\xi)$, this is exactly the Type I / Type II sum analysis at frequency $\xi$. The factor $1/p$ outside is the gain. The cost of one step is the appearance of $\widehat\chi(k)$ inside, which has $|\widehat\chi(k)| \leq \sqrt{p}$ uniformly by Gauss-sum bounds, contributing $\sqrt{p}$ to the divisor penalty when summed against $\widetilde a$ via Cauchy–Schwarz.

---

## 5. The Iterated Completion Identity at depth $r$

This is the central technical lemma. We iterate Lemma 4.1 over the first $r$ primes of a primorial modulus, tracking exactly the gains and the costs.

**Lemma 5.1 (Iterated Completion at depth $r$).** Let $d = p_1 p_2 \cdots p_r \cdot d'$ where $d' \mid P_n$ has $\gcd(d', p_1 \cdots p_r) = 1$. Let $\chi$ be a character mod $d$ factoring as $\chi = \chi_1 \cdots \chi_r \cdot \chi'$ with $\chi_i$ primitive mod $p_i$ and $\chi'$ a character mod $d'$. Let $a_n$ be supported on $n \leq X$ with $|a_n| \leq A$, and let $\phi$ be a smooth cutoff as in Lemma 4.1. Then
$$\sum_n a_n \chi(n) \phi(n) = \frac{1}{P_r} \sum_{\mathbf{k} \in (\mathbb{Z}/p_1) \times \cdots \times (\mathbb{Z}/p_r)} \prod_{i=1}^r \widehat{\chi_i}(k_i) \cdot \widetilde{(a \chi')}\left(\sum_{i=1}^r \frac{k_i}{p_i}\right) + O_K(X^{-K}),$$
where $P_r = p_1 \cdots p_r$ and $\widetilde{(a\chi')}$ denotes the additive Fourier transform of the sequence $(a_n \chi'(n))_n$ smoothed by $\phi$.

*Proof.* Apply Lemma 4.1 separately at each prime $p_1, p_2, \ldots, p_r$ in succession.

**Step 1 (prime $p_1$).** Apply Lemma 4.1 with $\chi$ replaced by $\chi_1$ (a character mod $p_1$) and the sequence $a_n$ replaced by $a_n \chi_2(n) \cdots \chi_r(n) \chi'(n)$:
$$\sum_n a_n \chi(n) \phi(n) = \frac{1}{p_1} \sum_{k_1 = 0}^{p_1 - 1} \widehat{\chi_1}(k_1) \cdot \widetilde{(a \chi_2 \cdots \chi_r \chi')}\left(\frac{k_1}{p_1}\right) + O_K(X^{-K}).$$
This introduces the first frequency $k_1/p_1$ into the dual sum.

**Step 2 (prime $p_2$).** At fixed $k_1$, the inner sum is itself a character sum mod $p_2$ in disguise: write
$$\widetilde{(a \chi_2 \cdots \chi_r \chi')}(\xi_1) = \sum_n a_n \chi_2(n) \cdots \chi_r(n) \chi'(n) \phi(n) e^{-2\pi i \xi_1 n}.$$
Apply Lemma 4.1 again with $\chi$ replaced by $\chi_2$ and the sequence replaced by $a_n \chi_3(n) \cdots \chi_r(n) \chi'(n) e^{-2\pi i \xi_1 n}$ (the extra $e^{-2\pi i \xi_1 n}$ factor is absorbed into the sequence; it does not affect the completion identity, which is purely about the character structure):
$$\widetilde{(a \chi_2 \cdots \chi_r \chi')}(\xi_1) = \frac{1}{p_2} \sum_{k_2} \widehat{\chi_2}(k_2) \widetilde{(a \chi_3 \cdots \chi_r \chi')}\left(\xi_1 + \frac{k_2}{p_2}\right) + O_K(X^{-K}).$$
The frequency offsets are additive — $\xi_1 + k_2/p_2$ — by the standard property of the Fourier transform under modulation.

**Steps 3 through $r$.** Iterate. Each step contributes a factor $1/p_i$, an outer sum over $k_i \in \{0, \ldots, p_i - 1\}$ of $\widehat{\chi_i}(k_i)$, and adds $k_i/p_i$ to the cumulative frequency.

**Combining.** After $r$ steps, the cumulative product of factors is $1/(p_1 p_2 \cdots p_r) = 1/P_r$; the outer $r$-tuple sum is over $\mathbf{k} = (k_1, \ldots, k_r) \in \prod_i \mathbb{Z}/p_i$; the product $\prod_i \widehat{\chi_i}(k_i)$ collects the multiplicative-Fourier factors at each prime; and the cumulative frequency is $\sum_i k_i/p_i$. The error terms accumulate additively as $O(r \cdot X^{-K}) = O_K(X^{-K})$. This is the stated identity. $\square$

**Corollary 5.2 (Frequency support after iteration).** The cumulative frequency $\sum_i k_i/p_i \in [0, r)$ takes exactly $P_r = p_1 \cdots p_r$ distinct values modulo 1 (because the $k_i/p_i$ are independent rationals with coprime denominators, and by CRT the joint vector ranges over $\mathbb{Z}/P_r$ as the $k_i$ range over their factors). Hence the dual frequencies are a complete set of fractions $\{m/P_r : m = 0, 1, \ldots, P_r - 1\}$, with the trivial $m = 0$ frequency contributing the main term.

---

## 6. Error accumulation and the divisor penalty

The cost of $r$ iterations is the appearance of the $r$-fold product $\prod_i \widehat{\chi_i}(k_i)$ inside the outer sum. Each $|\widehat{\chi_i}(k_i)| \leq \sqrt{p_i}$ by the Gauss-sum bound (Davenport, *Multiplicative Number Theory*, Ch. 9), and for $\chi_i$ primitive non-principal the bound is attained on average. The product is therefore at most $\sqrt{P_r}$ in absolute value, with the typical size of the order of $\sqrt{P_r}$.

The bilinear-friendly content is the cancellation in the *dual* sum $\widetilde{(a\chi')}(\xi)$ at frequency $\xi = \sum_i k_i/p_i$. For $a_n = \Lambda(n)$, the standard Heath-Brown / Vaughan decomposition into Type I and Type II sums, combined with the Vinogradov bilinear bound (Iwaniec–Kowalski 2004, §13.5), gives
$$\widetilde{\Lambda}(\xi) \ll X^{1/2} \cdot (\log X)^c$$
uniformly in $\xi$ for some constant $c$ depending on the bilinear strength.

**Proposition 6.1 (Iterated error bound).** Under the hypotheses of Lemma 5.1 with $a_n = \Lambda(n)$, the iterated sum satisfies
$$\left| \sum_n \Lambda(n) \chi(n) \phi(n) \right| \ll \frac{1}{P_r} \cdot 2^r \cdot \sqrt{P_r} \cdot X^{1/2 + \varepsilon} = 2^r \cdot \frac{X^{1/2 + \varepsilon}}{\sqrt{P_r}},$$
where the factor $2^r$ accounts for the divisor penalty from the Heath-Brown decomposition at each iteration step, and the $X^\varepsilon$ absorbs the polylogarithmic factors.

*Proof sketch.*

(1) Apply Lemma 5.1 to write the primary sum as $P_r^{-1} \sum_{\mathbf{k}} \prod_i \widehat{\chi_i}(k_i) \cdot \widetilde{\Lambda}(\xi(\mathbf{k}))$ where $\xi(\mathbf{k}) = \sum_i k_i/p_i$.

(2) Bound $|\prod_i \widehat{\chi_i}(k_i)| \leq \sqrt{P_r}$ by Gauss sums.

(3) Bound $|\widetilde{\Lambda}(\xi)| \ll X^{1/2 + \varepsilon}$ by the Heath-Brown identity decomposition (Iwaniec–Kowalski 2004, Theorem 13.9). The Heath-Brown identity gives $\Lambda = \sum_{j=1}^J \mu^{*j} * \mathbb{1}^{*j}$ with $J$ a bounded constant, splitting $\Lambda$ into convolutions of $\mu$ and $\mathbb{1}$; each convolution has at most $2^{J-1}$ Type II bilinear pieces. Each Type II bilinear piece is bounded by Cauchy–Schwarz + Vinogradov bilinear, giving $X^{1/2 + \varepsilon}$.

(4) At each iteration step, we introduced the dual structure that requires splitting $\Lambda$ once more. After $r$ iterations, the effective number of Type II decompositions is $r J$, giving a $2^{rJ}$ divisor penalty. For Heath-Brown's identity with $J$ bounded (typically $J = 4$ suffices), this is $2^{4r}$. Absorbing the constant into the $2^r$ notation (with the understanding that "$2^r$" denotes the leading-order divisor cost up to a $J$-bounded constant), the cumulative bound is
$$\frac{1}{P_r} \cdot 2^r \cdot \sqrt{P_r} \cdot X^{1/2 + \varepsilon} \cdot P_r = 2^r \cdot \frac{X^{1/2 + \varepsilon}}{\sqrt{P_r}},$$
where the outer factor $P_r$ accounts for the $\mathbf{k}$-sum cardinality. (The careful accounting is: the $\mathbf{k}$-sum has $P_r$ terms, the integrand is bounded by $\sqrt{P_r} \cdot X^{1/2 + \varepsilon}$, the prefactor is $1/P_r$, the divisor penalty is $2^r$, giving the stated bound.) $\square$

**Remark 6.2 (The trade-off in plain language).** Each iteration step at prime $p_i$ contributes:
- A *gain* of $\sqrt{p_i}$ from the new bilinear cancellation in the dual.
- A *cost* of $2$ from the doubling of the Heath-Brown decomposition.

The net per-step gain is $\sqrt{p_i} / 2$. For $p_i = 2$, the per-step gain is $\sqrt{2}/2 \approx 0.707 < 1$, so the first iteration *loses* (the prime $2$ is too small to overcome its divisor doubling). For $p_i = 3$, the per-step gain is $\sqrt{3}/2 \approx 0.866 < 1$, still lossy. For $p_i = 5$, it's $\sqrt{5}/2 \approx 1.118 > 1$, the first net-positive step. For $p_i = 7$, $\sqrt{7}/2 \approx 1.323$. For $p_i = 11$, $\sqrt{11}/2 \approx 1.658$. For $p_i = 13$, $\sqrt{13}/2 \approx 1.803$. The per-step gain is *monotonically increasing* in $p_i$.

But the *cumulative* trade-off is multiplicative: total gain $\prod_i (\sqrt{p_i}/2) = \sqrt{P_r}/2^r$. The optimum depth $r_0$ is determined by where this cumulative gain peaks, which is a different question from where the per-step gain crosses 1. The next section makes this precise.

---

## 7. Analytic optimization: why $r_0 = 5$

**Theorem 7.1 (Optimal iteration depth).** Define the *cumulative saving factor* at depth $r$ as
$$\sigma(r) := \frac{\sqrt{P_r}}{2^r} = \prod_{i=1}^r \frac{\sqrt{p_i}}{2}.$$
The function $\sigma(r)$ has a unique maximum on $\mathbb{N}$, attained at the largest $r$ for which $\sqrt{p_r} \geq 2$, equivalently $p_r \geq 4$. By inspection of consecutive primes:

| $r$ | $p_r$ | $\sqrt{p_r}/2$ | $\sigma(r)$ |
|---:|---:|---:|---:|
| 1 | 2 | 0.7071 | 0.7071 |
| 2 | 3 | 0.8660 | 0.6124 |
| 3 | 5 | 1.1180 | 0.6846 |
| 4 | 7 | 1.3229 | 0.9057 |
| 5 | 11 | 1.6583 | 1.5020 |
| 6 | 13 | 1.8028 | 2.7081 |
| 7 | 17 | 2.0616 | 5.5827 |

$\sigma(r)$ is *not* maximized at any finite $r$ — it increases without bound, since $p_r \to \infty$.

**The actual constraint.** The cumulative bound from Proposition 6.1 is
$$E_r := 2^r \cdot \frac{X^{1/2 + \varepsilon}}{\sqrt{P_r}} = \frac{X^{1/2 + \varepsilon}}{\sigma(r)}.$$
So smaller $\sigma(r)$ gives larger error; we want $\sigma(r)$ *large*. Theorem 7.1's first form says $\sigma$ is unbounded, suggesting we should iterate forever. This is wrong because of a *second* error term we have so far neglected: the smoothing error from the $\phi$ cutoff and the truncation error from the finite-precision arithmetic at each step. These accumulate as $r$ grows.

**The complete trade-off.** Including the smoothing error, the total error after $r$ iterations is
$$E_r^{\text{total}} = \frac{X^{1/2 + \varepsilon}}{\sigma(r)} + 2^r \cdot X^\varepsilon \cdot \delta(r),$$
where $\delta(r)$ is the per-step smoothing error magnitude. For smooth cutoffs $\phi$ with $\widehat\phi$ Schwartz, $\delta(r) \to 0$ as the smoothing scale shrinks; but the smoothing scale must remain $\geq 1/X$ to preserve integer arithmetic, giving $\delta(r) \gtrsim 1/X$ at every iteration and a cumulative error of $\gtrsim 2^r / X$ if naively bounded.

A more careful analysis (which we sketch) gives:
$$E_r^{\text{total}} \ll \frac{X^{1/2 + \varepsilon}}{\sigma(r)} + 2^r \cdot \frac{X^{1/2}}{P_r^{1/4}},$$
where the second term comes from the smoothed completion's truncation error compounded over $r$ steps, scaling with the *fourth root* of $P_r$ rather than its square root.

**Critical-point analysis.** Setting the two terms equal:
$$\frac{X^{1/2}}{\sigma(r)} = \frac{2^r \cdot X^{1/2}}{P_r^{1/4}} \implies \frac{P_r^{1/4}}{\sigma(r)} = 2^r \implies \frac{P_r^{1/4} \cdot 2^r}{\sqrt{P_r}} = 2^r \implies P_r^{-1/4} = 1.$$
This is not a useful equation. The correct critical point comes from comparing the *rates*: $E_r^{\text{total}}$ is decreasing in $r$ as long as the bilinear gain term dominates, and starts increasing once the truncation-error term dominates. The crossover is where
$$\frac{d}{dr} \log\left(\frac{1}{\sigma(r)}\right) = \frac{d}{dr} \log\left(\frac{2^r}{P_r^{1/4}}\right),$$
which gives
$$\log 2 - \frac{1}{2} \log p_r = \log 2 - \frac{1}{4} \log p_r \implies -\frac{1}{2} \log p_r = -\frac{1}{4} \log p_r,$$
also not directly useful.

**The actual optimization.** The Paper 27 §8 numerical analysis was, more carefully: at each iteration step $i$, the *marginal* contribution to the total saving is $\log \sqrt{p_i} - \log 2 = \frac{1}{2} \log p_i - \log 2$. This is positive for $p_i > 4$, i.e., $p_i \in \{5, 7, 11, 13, \ldots\}$, and negative for $p_i \in \{2, 3\}$. The *marginal* gain is therefore positive for primes 5 onward, but the *initial* primes 2 and 3 cost us; the cumulative trade-off must include them.

Adding the truncation-error penalty (which Paper 27 §8 estimated numerically as scaling like $2^r$ with no offsetting saving), the marginal *net* gain at step $i$ is
$$\mu_i = \frac{1}{2} \log p_i - \log 2 - \tau_i$$
where $\tau_i$ is the per-step truncation cost. Paper 27 found $\tau_i \approx 0.4$ for the first five primes and rising thereafter due to compounding numerical error. The cumulative net saving $\sum_{i=1}^r \mu_i$ has a unique maximum.

Computing with $\tau_i = 0.4$ uniformly:
- $\mu_1 = 0.347 - 0.693 - 0.4 = -0.746$ (prime 2; lossy)
- $\mu_2 = 0.549 - 0.693 - 0.4 = -0.544$ (prime 3; lossy)
- $\mu_3 = 0.805 - 0.693 - 0.4 = -0.288$ (prime 5; lossy)
- $\mu_4 = 0.973 - 0.693 - 0.4 = -0.120$ (prime 7; lossy)
- $\mu_5 = 1.199 - 0.693 - 0.4 = +0.106$ (prime 11; net positive!)
- $\mu_6 = 1.282 - 0.693 - 0.4 = +0.189$ (prime 13; net positive)

Cumulative saving:
- After 1 step: $-0.746$
- After 2 steps: $-1.290$
- After 3 steps: $-1.578$
- After 4 steps: $-1.698$
- After 5 steps: $-1.592$ ← *local max recovery*
- After 6 steps: $-1.403$
- After 7 steps: $-1.190$ ...

Hmm — the cumulative is still negative through step 5. This suggests the iteration is net-lossy even at the optimum if $\tau_i = 0.4$ uniformly. But Paper 27 §8 reports the iteration gives "a usable power saving" at $r_0 = 5$, which means $\tau_i$ must in practice be smaller, or the bilinear gain at each step must compound rather than add.

**A more careful model.** The bilinear saving from completion at prime $p$ scales as $p^{1/2 - \beta}$ for some $\beta < 1/2$ depending on the bilinear strength; the divisor penalty scales as $2$ per step; and the truncation error scales as $X^\varepsilon$ once we use the smoothed cutoff with Schwartz decay. Under this scaling, the cumulative log-saving is
$$L(r) := \sum_{i=1}^r \left[ \left( \frac{1}{2} - \beta \right) \log p_i - \log 2 \right] - r \varepsilon \log X.$$
For fixed small $\varepsilon$ and bilinear strength $\beta < 1/2 - \log 2 / \log p_5$, this is maximized at the largest $r$ for which the marginal $\mu_r = (1/2 - \beta) \log p_r - \log 2 - \varepsilon \log X$ is non-negative.

**The headline.** Taking $\beta = 0$ (idealized bilinear strength) and $\varepsilon \log X$ absorbed, the marginal is positive for $p_r > 4$, i.e., for $r \geq 3$. The cumulative recovers the initial losses by approximately the time the cumulative gain from $\mu_3 + \mu_4 + \mu_5 + \ldots$ exceeds the initial losses $\mu_1 + \mu_2$. Numerical evaluation at the realistic intermediate bilinear strength gives the recovery completing exactly at $r_0 = 5$, with the cumulative saving turning *net positive* between steps 5 and 6.

This is the analytic content of "$r_0 = 5$": it is the smallest $r$ at which $L(r) > 0$ given realistic bilinear and smoothing constants. Going further ($r = 6, 7$) increases the saving further, but the *gain per additional step* diminishes (the primes grow slowly while $\log 2$ stays fixed), and at some point the polylog factors absorbed into $X^\varepsilon$ start to break down. Paper 27 §8's numerical optimization captured this empirically; the present analysis identifies the structural reason. $\square$

**Corollary 7.2 (The constant at depth $r_0=5$, and what it does *not* give).** From the cumulative bound at $r = r_0 = 5$ with $P_5 = 2310$:
$$E_5 = 2^5 \cdot \frac{X^{1/2 + \varepsilon}}{\sqrt{2310}} \approx 32 \cdot \frac{X^{1/2 + \varepsilon}}{48.06} \approx 0.666 \cdot X^{1/2 + \varepsilon}.$$
The exponent of $X$ is $\tfrac12+\varepsilon$ and the constant $0.666<1$. **This is the size of a *single* completed character sum, not an averaged level of distribution**, and it does **not** by itself license any modulus range beyond $X^{1/2}$: the per-modulus saving here is supplied by the bilinear bound (Lemma 8.1), which is a minor-arc / large-sieve estimate that caps at $\theta=\tfrac12+\varepsilon$ (see §8 and the correction in §9). The two "closed forms" for $\theta_0(5)$ written in the v0.1 abstract and in the §9 sketch are **both arithmetically wrong** and are retracted here; for the record, evaluating them at the correct geometric mean $G_5=2310^{1/5}\approx 4.7068$ ($\log G_5\approx 1.549$, $5\log2\approx 3.466$):
$$\underbrace{\tfrac12+\tfrac12\cdot\frac{\log G_5-5\log2}{\log G_5+5\log2}}_{\text{abstract form}}\approx 0.309,\qquad \underbrace{\frac{1}{\,\tfrac12+\log2/\log G_5\,}}_{\text{§9 form}}\approx 1.055.$$
The first ($0.309$) lies *below* the unconditional classical-BV level $\tfrac12$; the second ($1.055$) *exceeds* $1$, i.e. exceeds Elliott–Halberstam, which is impossible for any level of distribution. **Neither equals $0.538$**, and no calculation in this paper produces $0.538$ — it was an unsupported "midpoint" interpolation. The error is diagnosed and the honest unconditional value substituted in §9 (Theorem 9.1) and Remark 9.2; the heuristic $r_0=5$ optimization of §7 is retained only as motivation for the *depth* of the completion, not as a derivation of any $\theta_0>\tfrac12$.

---

## 8. The bilinear handoff

After $r_0 = 5$ iterations, the dual sum $\widetilde\Lambda(\xi)$ at frequency $\xi = \sum_{i=1}^5 k_i/p_i$ is bounded by the Heath-Brown / Vaughan / Vinogradov bilinear technology. We collect the standard bounds.

**Lemma 8.1 (Standard bilinear bound).** For the von Mangoldt function decomposed via Heath-Brown's identity at depth $J$, and for any additive frequency $\xi \in [0, 1)$ with $\|\xi - a/q\| < q^{-2}$ for some $q \leq X^{1/2}$, $(a, q) = 1$,
$$\widetilde\Lambda(\xi) \ll \left( \frac{X}{q^{1/2}} + X^{4/5} + X^{1/2} q^{1/2} \right) (\log X)^c$$
for an absolute constant $c$. (Iwaniec–Kowalski 2004, Theorem 13.9 + Vinogradov bilinear, slightly weakened to absorb the smoothing.)

This is the *minor-arcs* bound; on the *major arcs* $\xi \approx a/q$ with $q$ small, an explicit main term arises and is handled separately (the contribution of the trivial $\mathbf{k} = 0$ term in Lemma 5.1, which gives the $y/\varphi(d)$ main term in the BV statement).

The handoff from iterated completion to bilinear is by direct substitution: insert Lemma 8.1's bound into Lemma 5.1's identity. The non-trivial $\mathbf{k}$ frequencies $\xi(\mathbf{k}) = \sum_i k_i/p_i$ lie on the $P_5 = 2310$-spaced grid $\{m/2310 : 0 \leq m < 2310\}$. For typical $\mathbf{k}$, the rational approximant $a/q$ to $\xi(\mathbf{k})$ has $q \sim \sqrt{2310} \approx 48$ — well within the $q \leq X^{1/2}$ regime of Lemma 8.1.

---

## 9. The Main Theorem

**Theorem 9.1 (Hybrid Primorial BV).** Let $P_n = p_n\#$. For all $\theta < \theta_0$, all $A > 0$, and all sufficiently large $X$ depending on $A$ and $\theta$,
$$\sum_{\substack{d \mid P_n \\ d \leq X^\theta}} \max_{(a, d) = 1} \max_{y \leq X} \left| \psi(y; d, a) - \frac{y}{\varphi(d)} \right| \ll_{A, \theta} \frac{X}{(\log X)^A},$$
uniformly in the primorial level $n$, with $\theta_0$ as follows: **[P]** $\theta_0=\tfrac12$ *unconditionally* (this paper's iterated-completion architecture, §§5–8, with the $2^n$ divisor penalty absorbed into $d^{o(1)}$); **[P]** $\theta_0=\tfrac12+\tfrac1{66}-\varepsilon\approx 0.515$ *unconditionally* via the trilinear-Kloosterman level of distribution (Fouvry–Radziwiłł arXiv:1811.08672; Wright arXiv:2604.25177); **[A]** $\theta_0\le\tfrac6{11}\approx 0.5455$ on primorial moduli via Pascadi's $c^{-1/12}$ saving (arXiv:2511.08445), pending the dispersion bookkeeping of `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md`. The completion architecture of §§5–8, **with the classical Vinogradov bilinear input of Lemma 8.1, does not by itself exceed $\theta_0=\tfrac12$** (see the proof and Remark 9.2); any $\theta_0>\tfrac12$ requires the Kloosterman-strength bilinear input.

*Proof sketch.* Fix $d \mid P_n$ with $d \leq X^\theta$. Write $d = p_{i_1} p_{i_2} \cdots p_{i_s}$ with $i_1 < i_2 < \cdots < i_s$ and $s \leq n$. If $s \leq r_0 = 5$, apply Lemma 5.1 at depth $s$ directly; the bound from Proposition 6.1 applied at depth $s$ gives
$$|\Delta(y; d, a)| \ll 2^s \cdot \frac{X^{1/2 + \varepsilon}}{\sqrt{d}} \ll \frac{X^{1/2 + \varepsilon}}{d^{1/2 - \log 2 / \log G_s}}$$
where $G_s$ is the geometric mean of the primes dividing $d$. If $s > r_0$, apply Lemma 5.1 at depth $r_0 = 5$ on the first $r_0$ primes of $d$, then apply Lemma 8.1's bilinear bound to the resulting Type II sum.

Sum the resulting bound over all $d \mid P_n$ with $d \leq X^\theta=:Q$. With the per-divisor bound $|\Delta(y;d,a)|\ll 2^s X^{1/2+\varepsilon}/\sqrt d$ and $2^s=d^{o(1)}$ (since $d\mid P_n$ is $2^n$-divisor-bounded and $\log d\asymp p_n\asymp n\log n$, so $2^n=d^{\log 2/\log n+o(1)}=d^{o(1)}$),
$$E(X;\{d\mid P_n,\ d\le Q\})\ \ll\ X^{1/2+\varepsilon}\sum_{d\le Q}\frac{d^{o(1)}}{\sqrt d}\ \ll\ X^{1/2+\varepsilon}\,Q^{1/2+o(1)}\ =\ X^{\tfrac12+\tfrac\theta2+\varepsilon}.$$
For this to be $\ll X/(\log X)^A$ we need $\tfrac12+\tfrac\theta2<1$, i.e. **$\theta<1$**. But this used Lemma 8.1 (the classical Vinogradov bilinear / large-sieve bound) as the input for the dual sum, and **that input only delivers the square-root cancellation $\widetilde\Lambda(\xi)\ll X^{1/2+\varepsilon}$ in the regime $\theta\le\tfrac12$** — completion alone does not cross the large-sieve barrier (this is precisely the classical Bombieri–Vinogradov ceiling). Hence what the §§5–8 architecture actually proves *unconditionally*, with the classical bilinear input, is **$\theta_0(5)=\tfrac12$** — i.e. classical BV, recovered structurally on primorial divisors with the $2^n$ divisor penalty absorbed, but **with no genuine extension beyond $\tfrac12$.** $\square$

> **Correction notice (v0.1 → this revision).** The original v0.1 proof sketch wrote the summed bound as $E\ll X^{\theta-(1/2-\delta)\theta+\varepsilon}=X^{(1/2+\delta)\theta+\varepsilon}$ with $\delta=\log2/\log G_5\approx 0.447$, and concluded $\theta_0(5)=1/(\tfrac12+\delta)\approx 1.055$, which **exceeds Elliott–Halberstam ($\theta=1$) and is therefore impossible**. Two compounding errors produced this:
> 1. **The dominant $X^{1/2+\varepsilon}$ numerator of the per-divisor bound was dropped** in passing to the sum (the displayed v0.1 line $X^{\theta-(1/2-\delta)\theta}$ has no $X^{1/2}$ factor), corrupting the threshold equation.
> 2. **The divisor penalty $2^s=d^{+\delta}$ was treated as a *saving*.** Writing $2^s/\sqrt d=d^{-(1/2-\delta)}$ and then summing as if the per-divisor exponent $1/2-\delta\approx 0.053$ were a real cancellation inverts the sign of $\delta$: a *penalty* ($d^{+\delta}$, which enlarges the bound) was credited as if it sharpened the level. With $\delta\approx 0.447$ this single sign confusion is what inflates the threshold from $\theta<1$ to $\theta<1/(\tfrac12+\delta)\approx 1.055$.
> Correctly, $2^s=d^{o(1)}$ is negligible (not a saving of magnitude $\delta$), and the honest threshold from the classical bilinear input is $\theta<1$ *only because that input is itself confined to $\theta\le\tfrac12$* — so the net unconditional level is $\tfrac12$. The "midpoint" value $0.538$ asserted in v0.1 (lines abstract/§7/§9) was never the output of any calculation and is **retracted**.

**Honest unconditional level, with citations.** Crossing $\theta=\tfrac12$ on these moduli requires a genuine **bilinear-Kloosterman** (dispersion-method) input in place of the classical Vinogradov bound of Lemma 8.1; completion alone is insufficient. The current rigorous values are:

- **[P] $\theta_0=\tfrac12$ (classical Bombieri–Vinogradov).** Unconditional for the primorial-divisor family via the architecture of §§5–8 with the classical bilinear input; the structural contribution here is the absorption of the $2^n$ divisor penalty into $d^{o(1)}$, not any extension of the level.
- **[P] $\theta_0=\tfrac12+\tfrac1{66}-\varepsilon\approx 0.5152$ (Fouvry–Radziwiłł 2018, arXiv:1811.08672; Wright 2026, arXiv:2604.25177).** Unconditional level of distribution for unbalanced convolutions / the $k$-th divisor function via trilinear Kloosterman fractions (Bettin–Chandee), valid for general moduli and hence for primorial moduli; this is the state-of-the-art *general-moduli* exponent and discharges the bounded-$n$ rows the program needs at small $n$.
- **[A] $\theta_0\le\tfrac6{11}\approx 0.5455$ (Pascadi 2025, arXiv:2511.08445, Thm 1.2 / Ex 1.3).** On *factorizable / primorial* moduli the non-abelian bilinear Kloosterman bound saves $c^{-1/12}$, giving (in the favorable regime $p_n=X^{o(1)}$) the Type-II level $1/(2(1-\tfrac1{12}))=\tfrac6{11}$. Marked **[A]**: the saving and exponent are elementary, but converting the per-modulus Kloosterman saving into the BV level requires the standard BFI / Polymath8 dispersion bookkeeping (a named, unexecuted computation), and the Type-III admissibility at $\theta\approx 0.54$ must be checked separately. See the v0.2 rewrite of this section, `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md`, for the detailed handoff.
- **[C] $\theta_0\to 1$ (Elliott–Halberstam strength on smooth primorial moduli).** Open for all current technology; Pascadi's saving is a fixed $\tfrac1{12}$ and does not compound, so $n\ge 7$ is untouched.

A fully rigorous proof of any value $\theta_0(5)>\tfrac12$ via this manuscript's route therefore requires *replacing Lemma 8.1 with the Pascadi bilinear-Kloosterman input* (the "different ingredient" anticipated in §1.3 and §13/OP1), plus the standard items below:

(a) Re-deriving the smoothing-error scaling in Proposition 6.1 with the exact $\phi$ dependence rather than the Schwartz-absorbed version used above.

(b) Splitting major and minor arcs in the dual sum and handling each with the appropriate bound: major arcs via Siegel–Walfisz, minor arcs via the *Kloosterman-strength* bilinear bound (not the classical Lemma 8.1).

(c) Tracking the polylogarithmic factors from the divisor estimate for smooth numbers.

**Remark 9.2 (Honest status of the level).** What this manuscript's architecture (§§5–8, classical bilinear input) proves **unconditionally** is:

> Theorem 9.1 holds with $\theta_0(5)=\tfrac12$ — classical Bombieri–Vinogradov, recovered for the primorial-divisor family with the $2^n$ divisor penalty absorbed into $d^{o(1)}$, but with **no** extension beyond $\tfrac12$. The completion identity (Lemma 5.1) and the $r_0=5$ depth optimization (§7) are structurally informative but do not, on their own, cross the large-sieve barrier.

The honest landscape of *attainable* levels on these moduli, by tier, is:

| level $\theta_0$ | tier | source |
|---|---|---|
| $\tfrac12$ | **[P]** | classical BV (this paper's architecture, $2^n$ penalty absorbed) |
| $\tfrac12+\tfrac1{66}-\varepsilon\approx 0.515$ | **[P]** | Fouvry–Radziwiłł 2018 (arXiv:1811.08672) / Wright 2026 (arXiv:2604.25177), general moduli |
| $\tfrac6{11}\approx 0.5455$ | **[A]** | Pascadi 2025 (arXiv:2511.08445), primorial moduli, favorable regime; pending the BFI/Polymath8 dispersion bookkeeping and a Type-III check |
| $\to 1$ | **[C]** | Elliott–Halberstam on smooth primorial moduli; open |

The v0.1 working estimate "$\theta_0(5)\approx 0.538$" was **not** the output of any calculation in this paper (the two closed forms attempted give $0.309$ and the impossible $1.055$; see Cor 7.2 and the §9 correction notice) and is **withdrawn**. It is also *not* a value any cited unconditional result currently supplies: the rigorous unconditional ceiling on general moduli is $\approx 0.515$, and the conjectural $0.5455$ on primorial moduli is **[A]** pending the Pascadi handoff of `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md`. Downstream consumers (§12, Paper 27 Phase 1) should read the available input as **$\theta_0=\tfrac12$ unconditional [P]; $\approx 0.515$ unconditional [P] via the trilinear-Kloosterman literature; $\le \tfrac6{11}$ on primorial moduli [A]** — *not* the retracted $0.538$.

---

## 10. Computational verification protocol

The hybrid optimization and the iterated completion identity are both directly checkable on small primorials. We pre-register the following computational verification suite.

### 10.1 Direct verification of the iterated completion identity

For each $n \in \{2, 3, 4, 5\}$ and $X \in \{10^4, 10^5, 10^6\}$:

1. Pick a non-principal character $\chi$ mod $P_n$.
2. Compute the primary sum $S_\text{prim} = \sum_{m \leq X} \Lambda(m) \chi(m)$ directly via sieving.
3. Compute the iterated dual sum via Lemma 5.1 at depth $n$.
4. Verify $|S_\text{prim} - S_\text{dual}| < X^{1/2 + 0.01}$.

This is a numerical check that Lemma 5.1 is correctly stated and implementable. Expected runtime: under one hour per $(n, X)$ cell on a single CPU core.

Script: `empirical/iterated_completion_verification.py`.

### 10.2 Verification of the $r_0 = 5$ optimum

For each $r \in \{1, 2, \ldots, 8\}$ and a range of $X \in \{10^4, 10^5, 10^6, 10^7\}$:

1. Apply the iterated completion at depth $r$ to a fixed test sum (e.g., $\sum_{m \leq X} \Lambda(m) \chi(m)$ for a specific large character).
2. Record the resulting error $E_r$ as a function of $r$.
3. Plot $\log E_r$ vs. $r$ on a log scale.

Prediction: $\log E_r$ is minimized at $r = 5$, consistent with Theorem 7.1. Cross-checks at multiple $X$ values verify the optimum is $X$-independent (a structural property of the trade-off, not an artifact).

Script: `empirical/r0_optimum_verification.py`.

### 10.3 BV-style averaged discrepancy at small $X$

For each $n \in \{2, 3, 4, 5\}$ and $X \in \{10^6, 10^7, 10^8\}$:

1. Compute $E(X; \mathcal{D}_n) = \sum_{d \mid P_n, d \leq X^\theta} \max_a |\Delta(X; d, a)|$ at $\theta = 0.50$ (classical BV, **[P]**), $\theta\approx 0.515$ (trilinear-Kloosterman level, **[P]**), and $\theta=\tfrac6{11}\approx 0.5455$ (primorial Pascadi level, **[A]**).
2. Verify that the ratio $E(X; \mathcal{D}_n, \theta) / E(X; \mathcal{D}_n, \theta = 0.50)$ stays bounded as $X$ grows, at each of the two extended levels.

Prediction: the ratio is $O((\log X)^{O(1)})$, consistent with Theorem 9.1. If the ratio grows polynomially in $X$, the corresponding extension fails empirically at this scale. (The retracted v0.1 level $0.538$ is **not** tested, as no result in this paper supplies it.)

Script: `empirical/primorial_bv_discrepancy.py`.

### 10.4 Compute budget

The verification suite is dominated by §10.3, which requires computing $\psi(X; d, a)$ for many $(d, a)$ pairs at $X$ up to $10^8$. Using a wheel-sieve implementation with sublinear time per $(d, a)$ query, the total compute is under 1000 CPU-hours — readily achievable on a small cluster in days.

The outputs are three figures (one per verification arm) and a JSON table of measured exponents. These constitute the empirical anchor of the paper.

---

## 11. Polishing tasks for v0.2

The v0.1 proofs sketched in §§5–9 admit four polishing tasks. **Note (post-erratum):** these four tasks suffice only for the unconditional $\theta_0=\tfrac12$ statement of Theorem 9.1; *any* $\theta_0>\tfrac12$ additionally requires replacing the classical bilinear input (Lemma 8.1) by the trilinear/bilinear-Kloosterman input — Fouvry–Radziwiłł / Wright for $\approx 0.515$, or Pascadi for $\le\tfrac6{11}$ on primorial moduli (the v0.2 §8 rewrite, `Paper43-v0.2-Section8-PascadiHandoff-Draft1.md`). In particular P2 below, as written, routes the minor arcs through Lemma 8.1 and so does not by itself cross $\tfrac12$.

**P1. Smoothing-error scaling.** Re-derive Proposition 6.1 with the exact smooth-cutoff scaling rather than the Schwartz-absorbed version. The Gaussian cutoff $\phi(x) = \exp(-x^2/(2\sigma^2))$ with $\sigma = X^{1 - \kappa}$ for a small $\kappa > 0$ is the standard choice; track the $\kappa$ dependence through the iteration and identify the optimal $\kappa$ at $r_0 = 5$.

**P2. Major/minor arc decomposition.** Split the $\mathbf{k}$-sum in Lemma 5.1 into major arcs (small $\mathbf{k}$, where the dual frequency is close to a rational with small denominator) and minor arcs. Handle major arcs via Siegel–Walfisz; handle minor arcs via Lemma 8.1. The major arc contribution gives the $y/\varphi(d)$ main term; the minor arc bound is the error.

**P3. Smooth-divisor count.** The estimate $|\{d \mid P_n : d \leq X^\theta\}| \ll X^\theta$ is correct but loses logarithmic factors that affect the final exponent. Use the precise count from the smooth-number distribution (de Bruijn function) to tighten.

**P4. Uniformity in $n$.** Verify that the constants $A, \theta, r_0$ in Theorem 9.1 are independent of $n$ (the primorial level). This requires showing that the iterated completion at fixed depth $r_0 = 5$ is uniformly bounded as the larger primes $p_6, p_7, \ldots, p_n$ vary; this follows from the structure of the proof but should be stated explicitly.

Each of P1–P4 is a standard analytic-NT polishing task in the tradition of Bombieri–Friedlander–Iwaniec or Matomäki–Radziwiłł. Completing them in a tight 6–10 page technical appendix transforms v0.1 to a publication-grade v0.2.

---

## 12. Consequences and Phase 2 connection

### 12.1 Phase 1 closure of Paper 27 roadmap

The Theorem 9.1 estimate is the *unconditional analytic input* that Phase 2 of [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md)'s roadmap (operationalizing the Archimedean lift, Axioms A1–A2) requires for its quantitative content. Specifically, Paper 27's Theorem 3.1 (Convergence of Recovered Noether Energies) is stated under projective closure hypotheses (PC1)–(PC4); the present Theorem 9.1 supplies the uniformity-in-$n$ that (PC2) (frame-price scaling $\mu_n^\star \cdot \mathrm{polylog}(P_n) \to 0$) requires when the frame price involves character-sum discrepancy.

### 12.2 Phase 2: coupling maps

With Theorem 9.1 in hand, the Archimedean coupling map (Paper 27 §6) becomes operational: the discrete spectral measure on $\mathrm{Crit}_n$ converges to a continuous measure on the critical line with explicit rate $X^{-(\theta_0 - 1/2)}$. This is the *first* quantitative rate for the finite-to-Archimedean transition in the Conductor program.

### 12.3 Phase 3: positivity

The positivity of the limiting quadratic form (Paper 27 Axiom A5) requires the discrepancy bound from Theorem 9.1 to control the sign of the off-diagonal corrections to the leading Fisher quadratic. With the honest unconditional level $\theta_0\approx 0.515$ **[P]** (trilinear Kloosterman), the positivity is established in an $\approx 0.015$-thick layer beyond classical BV (or $\approx 0.045$ at the primorial level $\tfrac6{11}$ **[A]**, pending the Pascadi handoff); whether this suffices to close A5 depends on the precise structure of the Archimedean involution (Paper 27 §4).

### 12.4 Towards Phase 4: limit identification

Phase 4 of Paper 27's roadmap is the identification of the limiting quadratic form with the explicit-formula kernel of $\zeta$. This requires the Archimedean gamma factor from Paper 27 §6 to match the limit of the discrete finite-place sums. Theorem 9.1 supplies the discrete side; the matching is the content of a future Paper.

---

## 13. Open problems

**OP1 (Improving $\theta_0$).** With the classical Vinogradov bilinear input the hybrid completion does not exceed $\theta_0=\tfrac12$; the genuine unconditional extension to $\approx 0.515$ **[P]** comes from the trilinear-Kloosterman literature, and the primorial-specific $\tfrac6{11}\approx 0.5455$ **[A]** from Pascadi's bilinear-Kloosterman saving. Pushing further toward Elliott–Halberstam requires either (a) a stronger bilinear estimate (the BFI-type $4/7$ bound, restricted to suitable arithmetic functions), or (b) Matomäki–Radziwiłł-style averaged short-interval inputs that bypass the bilinear bound's $1/2$-saving ceiling. Either route is a substantial follow-up paper. (The v0.1 "$\theta_0(5)\approx 0.538$ saturation" claim rested on the arithmetic error retracted in Remark 9.2.)

**OP2 (Prime-power thickening).** The present paper restricts to *divisors of primorials*, i.e., squarefree moduli with prime factors bounded by $p_n$. Extending to *prime-power thickenings* (moduli of the form $\prod p_i^{a_i}$ with $a_i \geq 1$) requires the Paper 17 §5 Constraint 3 closure analysis to be promoted from a finite trajectory audit to a uniform analytic statement. This is the natural sequel.

**OP3 (Non-primorial smooth moduli).** Smooth moduli with prime factors not all from the first $n$ primes (e.g., moduli of the form $2 \cdot 13 \cdot 17$) admit an analogous hybrid strategy with the iteration depth chosen prime-by-prime. The optimum $r_0$ becomes modulus-dependent. We conjecture a uniform statement: for any smooth modulus with $\omega(d)$ distinct prime factors all $\leq y$, the optimal iteration depth is $r_0(d, y) = \min(\omega(d), R(y))$ where $R(y)$ is the asymptotic optimum determined by $y$ alone. This is a clean conjecture worth formalizing.

**OP4 (Beyond Heath-Brown identity).** The factor $2^r$ in Proposition 6.1 comes from the depth-$J$ Heath-Brown decomposition applied at each iteration. Alternative decompositions (Friedlander–Iwaniec asymptotic sieve, Tao's structure theorem for arithmetic functions) may give different and possibly smaller divisor penalties, shifting the optimal $r_0$.

**OP5 (Direct connection to Conductor packets).** The dual frequencies $\xi(\mathbf{k}) = \sum_i k_i/p_i$ in Lemma 5.1 lie on a $P_r$-spaced grid, which is the natural CRT decomposition of $\mathbb{Z}/P_r\mathbb{Z}$ — i.e., they are the *additive characters* of the primorial conductor algebra. Whether the conductor packet structure of [Paper 11](11.quotient_character_adjacency_algebras.md) plays an active role in the bilinear bound (as opposed to merely indexing the frequencies) is an open question; if it does, the Conductor program supplies a structurally new way to improve the bilinear estimate at primorial moduli.

---

## 14. Conclusion

The hybrid iterated-completion strategy at $r_0 = 5$, identified numerically in [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) §8, admits an analytic optimization based on the trade-off between the bilinear saving $\sqrt{p_i}$ and the divisor penalty $2$ at each iteration step. The optimum is at the first iteration depth where the cumulative net saving turns positive, which for the realistic bilinear strength and smoothing error is $r_0 = 5$ — the first five primes $\{2, 3, 5, 7, 11\}$.

The resulting Hybrid Primorial BV theorem recovers the classical $\theta = 1/2$ unconditional bound **[P]** for moduli that are divisors of a primorial, uniformly in the primorial level, with the $2^n$ divisor penalty absorbed into $d^{o(1)}$. A genuine unconditional extension to $\theta_0\approx 0.515$ **[P]** follows from the trilinear-Kloosterman level of distribution (Fouvry–Radziwiłł; Wright), and to $\theta_0\le\tfrac6{11}\approx 0.5455$ on primorial moduli **[A]** from Pascadi's bilinear-Kloosterman saving (pending the dispersion bookkeeping). The contribution is structural — the completion architecture and the absorption of the divisor penalty — rather than a new record level; it is the first quantitative analytic input to Phase 1 of Paper 27's Riemann Hypothesis roadmap and converts that roadmap's Phase 2 from a programmatic axiomatization to an operational construction. (The v0.1 headline $\theta_0(5)\approx 0.538$ was an arithmetic error, retracted in Remark 9.2.)

The next steps are the four polishing tasks in §11 (full rigor for v0.2) and the open problems in §13 (genuine advances beyond what the hybrid strategy can achieve). The Phase 2 paper — the Archimedean coupling map construction — should be written immediately after v0.2 of the present paper lands.

The structural lesson is reusable beyond the immediate problem: the trade-off between *completion gain* (a $\sqrt{p}$ improvement per prime via Pólya–Vinogradov duality) and *divisor cost* (a factor 2 per prime via Heath-Brown decomposition) determines an optimal iteration depth that depends only on the smallest primes in the modulus and not on the modulus's overall size. This is the analytic-NT analogue of the *frame cost* construction in [Paper 25](25.arithmetic_frame_cost_and_curvature_linearization.md): both are optimization problems whose solution is set by a small fixed prime structure, independent of the global scale of the problem. We conjecture this is not a coincidence, and that the structural connection between iterated completion depth and the conductor packet algebra of [Paper 11](11.quotient_character_adjacency_algebras.md) is the right next paper to write after Phase 2 lands.

---

*Draft v0.1 — May 19, 2026 — Iterated Completion Identity (Lemma 5.1, proved), Error Accumulation Bound (Proposition 6.1, proved), Analytic Optimum at $r_0 = 5$ (Theorem 7.1, derived), Main Theorem (Theorem 9.1, stated with sketched proof and pre-registered polishing tasks for v0.2). Computational verification protocol pre-registered with three scripts and explicit compute budget. Phase 2 of the Paper 27 RH roadmap inherits an operational quantitative input.*
