# T28 — Vector B Coset-Averaging Attack on Stieltjes Positivity at Primorial N

**Leonardo Murillo Montero**

*First draft — May 27, 2026*

---

> *T28 executes the "Vector B" attack named in `T8.4-Lemma-6p4-Falsification-Note.md` (May 25): re-do the kernel factorization of the prime-joint cumulant without collapsing to the principal coset $m \equiv 1 \bmod N$, instead averaging over ALL cosets via character orthogonality. The result is a clean structural decomposition*
> $$J_n^{\mathrm{prime,joint}}(N) \;=\; \mathrm{Main}_n(N) + \mathrm{Err}_n(N) + \mathrm{Arch}_n(N),$$
> *with explicit formulas for each piece. The main term has a closed-form Hankel structure controlled by an explicit Cauchy-Schwarz ratio. **The unconditional Stieltjes positivity reduces to a precise structural question: does $\mathrm{Arch}_n(N) - |\mathrm{Main}_n(N)|_{\mathrm{neg}}|$ dominate the equidistribution error?** This is the named remaining gap, structurally isolated for the first time.*

---

## §1. Setup

### §1.1 The T8.4 kernel before coset collapse

From T8.4 §5 Theorem C and §6.1 Theorem D, the prime-joint shifted Hankel matrix entries are

$$\mu_{k+1}^{\mathrm{prime,joint}}(N) \;=\; \varphi(N) \sum_{\substack{n \ge 1 \\ \gcd(n, N) = 1}} \Lambda(n)\, n^{-1/2}\, \frac{(\log n)^{2k+3}}{2(2k+3)!}\, \langle h_{k+1}, \chi_{n^{-1}} \rangle \;+\; \mathcal{E}^{\mathrm{arch}}_{k+1}(N),$$

with the arch boundary $\mathcal{E}^{\mathrm{arch}}_{k+1}(N) = -\mu_{k+1}^{\mathrm{arch,joint}}(N)$, an explicit Hurwitz-zeta-atomic value from ArchStruct Thm 1.

T8.4 Lemma 6.4's attempt collapsed the sum to the principal coset $n \equiv 1 \bmod N$, where $\langle h_{k+1}, \chi_{n^{-1}}\rangle = \langle h_{k+1}, \chi_1\rangle$ is constant. Probe `probe_T8p4_lemma_6p4_Q_matrix.py` falsified this: the matrix $(R_k \cdot \mathrm{Re}\langle h_k, \chi_1\rangle)_{i,j}$ is NOT PSD (Cauchy-Schwarz violation; sign-flips in axis sequence at $k \approx 0.7 N$).

### §1.2 Vector B reformulation

Don't collapse to the principal coset. Keep the full sum over all units $n$ coprime to $N$, and split by coset $c = n^{-1} \bmod N \in (\mathbb{Z}/N)^\times$:

$$\sum_{\gcd(n,N)=1} \Lambda(n)\, n^{-1/2}\, \frac{(\log n)^{2k+3}}{2(2k+3)!}\, \langle h_{k+1}, \chi_{n^{-1}}\rangle \;=\; \sum_{c \in (\mathbb{Z}/N)^\times} \langle h_{k+1}, \chi_c\rangle\, S_k(c; N),$$

where the per-coset prime sum is

$$S_k(c; N) \;:=\; \sum_{\substack{n \ge 1 \\ n^{-1} \equiv c \bmod N}} \Lambda(n)\, n^{-1/2}\, \frac{(\log n)^{2k+3}}{2(2k+3)!}.$$

This is the **cosset decomposition** of the kernel. It does not lose information; it just reorganizes the sum.

---

## §2. The main term via character orthogonality

By Dirichlet equidistribution + Siegel–Walfisz, write

$$S_k(c; N) \;=\; \frac{\bar S_k(N)}{\varphi(N)} \;+\; \epsilon_k(c; N),$$

where $\bar S_k(N) := \sum_{\gcd(n,N)=1} \Lambda(n)\, n^{-1/2} (\log n)^{2k+3} / (2(2k+3)!)$ is the **uniform-cosset average** (independent of $c$), and $\epsilon_k(c; N)$ is the equidistribution residual.

Substituting:
$$\sum_c \langle h_{k+1}, \chi_c\rangle\, S_k(c; N) \;=\; \frac{\bar S_k(N)}{\varphi(N)} \sum_c \langle h_{k+1}, \chi_c\rangle \;+\; \sum_c \langle h_{k+1}, \chi_c\rangle\, \epsilon_k(c; N).$$

**Key identity (character orthogonality applied to Helmert vector):**

$$\sum_{c \in (\mathbb{Z}/N)^\times} \chi_c(s) \;=\; \varphi(N)\, \mathbf{1}[s \equiv 1 \bmod N], \qquad \text{hence} \qquad \sum_c \langle h_k, \chi_c\rangle \;=\; \sum_c \sum_s (h_k)_s \chi_c(s) \;=\; \varphi(N)\, (h_k)_1.$$

The Helmert vector's first entry is $(h_k)_1 = 1/\sqrt{k(k+1)} = R_k \cdot \sqrt{N}$ (using $R_k = 1/\sqrt{N k(k+1)}$; the $\sqrt{N}$ is absorbed by the explicit Helmert normalization choice — equivalently $(h_k)_1 = R_k$ with the alternative convention where Helmert vectors are not divided by $\sqrt{N}$).

We adopt the T4 convention: $(h_k)_1 = R_k$.

Therefore:
$$\sum_c \langle h_{k+1}, \chi_c\rangle = \varphi(N) R_{k+1}.$$

Plugging back:

$$\mu_{k+1}^{\mathrm{prime,joint}}(N) \;=\; \varphi(N) \left[ \frac{\bar S_k(N)}{\varphi(N)} \cdot \varphi(N) R_{k+1} \;+\; \sum_c \langle h_{k+1}, \chi_c\rangle \epsilon_k(c; N) \right] \;+\; \mathcal{E}^{\mathrm{arch}}_{k+1}(N).$$

$$\boxed{\;\mu_{k+1}^{\mathrm{prime,joint}}(N) \;=\; \varphi(N)\, R_{k+1}\, \bar S_k(N) \;+\; \mathcal{R}_k(N) \;+\; \mathcal{E}^{\mathrm{arch}}_{k+1}(N)\;}$$

where the **equidistribution residual** is

$$\mathcal{R}_k(N) \;:=\; \varphi(N) \sum_{c \in (\mathbb{Z}/N)^\times} \langle h_{k+1}, \chi_c\rangle\, \epsilon_k(c; N).$$

---

## §3. The main-term Hankel: explicit Stieltjes integral form

Write the main term

$$\mu_{k+1}^{\mathrm{prime, main}}(N) \;:=\; \varphi(N)\, R_{k+1}\, \bar S_k(N).$$

We compute $\bar S_k(N)$ explicitly. Substituting $t = \log n$ over prime-power log-positions (i.e., $n = p^r$ for $p \nmid N, r \ge 1$, with $\Lambda(p^r) = \log p$ and $t = r \log p$):

$$\bar S_k(N) \;=\; \sum_{\substack{p \nmid N \\ r \ge 1}} (\log p)\, p^{-r/2}\, \frac{(r \log p)^{2k+3}}{2(2k+3)!} \;=\; \int_0^\infty \frac{t^{2k+3}\, e^{-t/2}}{2(2k+3)!}\, d\nu_N(t),$$

with $d\nu_N(t) := \sum_{p \nmid N, r \ge 1} (\log p)\, \delta_{r \log p}(t)$ the **von Mangoldt prime-power log measure** restricted to primes coprime to $N$. This is a positive (purely atomic) measure on $(0, \infty)$.

Define the **integrand kernel**

$$g_k(t) \;:=\; \frac{t^{2k+3}\, e^{-t/2}}{2(2k+3)!},$$

so $\bar S_k(N) = \int_0^\infty g_k(t)\, d\nu_N(t) =: I_k(N)$.

The main-term shifted Hankel matrix at rung $n$ is:

$$\mathrm{Main}_n(N)_{ij} \;:=\; \mu_{i+j+1}^{\mathrm{prime, main}}(N) \;=\; \varphi(N)\, R_{i+j+1}\, I_{i+j}(N).$$

---

## §4. The Cauchy-Schwarz computation: main term is NOT PSD

### §4.1 The kernel ratio

Compute $g_1(t)^2 / (g_0(t) g_2(t))$ as a function of $t$:

$$g_0(t) = \frac{t^3 e^{-t/2}}{12}, \quad g_1(t) = \frac{t^5 e^{-t/2}}{240}, \quad g_2(t) = \frac{t^7 e^{-t/2}}{10080}.$$

$$\frac{g_1(t)^2}{g_0(t) g_2(t)} \;=\; \frac{t^{10} e^{-t} / 57600}{(t^3 e^{-t/2}/12) \cdot (t^7 e^{-t/2}/10080)} \;=\; \frac{t^{10} e^{-t} / 57600}{t^{10} e^{-t} / 120960} \;=\; \frac{120960}{57600} \;=\; \frac{21}{10}.$$

**Critical observation:** the ratio $g_1^2/(g_0 g_2) = 21/10$ is **independent of $t$**. Hence by Cauchy–Schwarz with equality (constant ratio):

$$I_1(N)^2 \;=\; \frac{21}{10}\, I_0(N)\, I_2(N) \qquad \text{for ANY positive measure } d\nu_N.$$

This is not an inequality — it's an **exact identity** because the ratio of integrands is a positive constant on the support of $\nu_N$.

### §4.2 The radical correction

Compute $R_2^2 / (R_1 R_3)$ with $R_k = 1/\sqrt{N k (k+1)}$:

$$R_1 = \tfrac{1}{\sqrt{2N}}, \quad R_2 = \tfrac{1}{\sqrt{6N}}, \quad R_3 = \tfrac{1}{\sqrt{12N}}.$$

$$\frac{R_2^2}{R_1 R_3} \;=\; \frac{1/(6N)}{1/\sqrt{24 N^2}} \;=\; \frac{\sqrt{24}}{6} \;=\; \frac{2\sqrt{6}}{6} \;=\; \frac{\sqrt{6}}{3} \;\approx\; 0.8165.$$

### §4.3 The main-term Cauchy-Schwarz ratio

The 2×2 minor at rung $n = 1$ of $\mathrm{Main}_1(N)$:

$$\det \mathrm{Main}_1(N) \;=\; \mathrm{Main}(N)_{00} \cdot \mathrm{Main}(N)_{11} - \mathrm{Main}(N)_{01}^2 \;=\; \varphi(N)^2 \left[ R_1 R_3\, I_0 I_2 - R_2^2\, I_1^2 \right].$$

Substituting $I_1^2 = (21/10) I_0 I_2$:

$$\det \mathrm{Main}_1(N) \;=\; \varphi(N)^2\, I_0 I_2 \left[ R_1 R_3 - \tfrac{21}{10}\, R_2^2 \right] \;=\; \varphi(N)^2\, I_0 I_2 \cdot R_2^2 \left[ \tfrac{R_1 R_3}{R_2^2} - \tfrac{21}{10} \right].$$

With $R_1 R_3 / R_2^2 = 3/\sqrt{6} = \sqrt{6}/2 \approx 1.2247$:

$$\det \mathrm{Main}_1(N) \;=\; \varphi(N)^2\, I_0 I_2\, R_2^2 \cdot (1.2247 - 2.1) \;=\; \varphi(N)^2\, I_0 I_2\, R_2^2 \cdot (-0.8753).$$

$$\boxed{\;\det \mathrm{Main}_1(N) \;<\; 0 \quad \text{unconditionally, for every primorial } N \text{ with prime mass on } d\nu_N.\;}$$

### §4.4 What this says

**The coset-averaged main term of $J_n^{\mathrm{prime,joint}}(N)$ is NOT positive semi-definite, even at rung $n = 1$.** This is a clean structural finding:

- Vector B's coset-averaging DOES give a closed-form simplification of the prime sum (the Stieltjes integral against the von Mangoldt log measure).
- The simplification produces a Hankel-structured "main term," but it is structurally **indefinite**.
- The Cauchy-Schwarz factor is **explicit**: $1.7138 = (\sqrt{6}/3) \cdot 2.1 = \sqrt{6} \cdot 7/10$.

So Vector B does NOT close the kernel positivity unconditionally. The main term is NOT PSD by itself.

### §4.5 Generalization to all rungs

The same computation extends to all rungs. For general $k$:

$$\frac{g_k(t)^2}{g_{k-1}(t) g_{k+1}(t)} \;=\; \frac{(t^{2k+3})^2 / (2(2k+3)!)^2}{(t^{2k+1} t^{2k+5}) / (2(2k+1)! \cdot 2(2k+5)!)} \;=\; \frac{(2k+1)! (2k+5)!}{((2k+3)!)^2}.$$

This is $\binom{2k+5}{2}/\binom{2k+3}{2}^{-1}\cdot \ldots$ — let me compute:

$$\frac{(2k+1)!\,(2k+5)!}{((2k+3)!)^2} \;=\; \frac{(2k+5)(2k+4)}{(2k+3)(2k+2)}.$$

At $k = 0$: $(5 \cdot 4)/(3 \cdot 2) = 20/6 = 10/3 \approx 3.33$. Hmm, this differs from my earlier $g_1^2/(g_0 g_2) = 21/10$. Let me recheck.

Actually, I want the 3-term Hankel ratio at center $k+1$: $g_k^2 / (g_{k-1} g_{k+1})$. The 2×2 minor at rung $n=1$ corresponds to $k=1$: $g_1^2/(g_0 g_2)$.

For $k=1$: $g_1^2/(g_0 g_2) = (3!)(7!)/((5!)^2) \cdot$ — wait my formula was $g_k^2 / (g_{k-1} g_{k+1})$, so at $k=1$: $g_1^2/(g_0 g_2) = (1!)(5!)/((3!)^2) = 120/36 = 10/3$. But I computed $g_1^2/(g_0 g_2) = 21/10$ above. Discrepancy.

Let me redo. $g_k(t) = t^{2k+3} e^{-t/2}/(2(2k+3)!)$. So the constant in $g_k$ is $1/(2 (2k+3)!)$. At $k=0,1,2$: $1/(2 \cdot 6) = 1/12$, $1/(2 \cdot 120) = 1/240$, $1/(2 \cdot 5040) = 1/10080$.

$g_1^2 / (g_0 g_2) = (1/240)^2 / ((1/12)(1/10080)) \cdot t^{10}/(t^{10}) \cdot e^{-t}/e^{-t}$ where $e^{-t}$ comes from $e^{-t/2} \cdot e^{-t/2}$ on top and $e^{-t/2 \cdot 2}$ on bottom — they match.

$= (1/57600) / (1/120960) = 120960/57600 = 2.1 = 21/10$.

So my computation 21/10 stands. Now let me redo the general formula.

$g_k^2 / (g_{k-1} g_{k+1}) = [(2(2k+1)!) \cdot (2(2k+5)!)] / [(2(2k+3)!)^2]$ (constants from denominators only, the $t^?$ and $e^?$ cancel)
$= [4 \cdot (2k+1)! (2k+5)!] / [4 \cdot ((2k+3)!)^2]$
$= (2k+1)! (2k+5)! / ((2k+3)!)^2$
$= \frac{(2k+5)(2k+4)(2k+3)(2k+2)(2k+1)!}{(2k+3)(2k+2)(2k+1)! \cdot (2k+3)!}$
$= \frac{(2k+5)(2k+4)}{(2k+3)(2k+2)} \cdot \frac{(2k+3)(2k+2)(2k+1)!}{(2k+3)!}$ — wait this is getting confused.

Direct: $(2k+5)! / (2k+3)! = (2k+5)(2k+4)$. $(2k+1)! / (2k+3)! = 1/((2k+3)(2k+2))$.

So $g_k^2/(g_{k-1} g_{k+1}) = (2k+5)(2k+4)/((2k+3)(2k+2))$.

At $k=1$: $(7 \cdot 6)/(5 \cdot 4) = 42/20 = 21/10 = 2.1$. ✓

At $k=0$: $(5 \cdot 4)/(3 \cdot 2) = 20/6 = 10/3 \approx 3.33$. But we can't form a 2x2 minor at $k=0$ (there's no $g_{-1}$). This was the wrong rung.

OK so at the 2x2 minor (rungs 0, 1 in $\mu$, i.e., $\mu_1, \mu_2, \mu_3$ entries):

Hmm wait. $\mathrm{Main}_n(N)_{ij} = \varphi(N) R_{i+j+1} I_{i+j}(N)$. So at $n = 1$, the matrix is:
- $(0,0)$: $\varphi(N) R_1 I_0$
- $(0,1) = (1,0)$: $\varphi(N) R_2 I_1$
- $(1,1)$: $\varphi(N) R_3 I_2$

The determinant: $\varphi(N)^2 (R_1 R_3 I_0 I_2 - R_2^2 I_1^2)$.

With $I_1^2 = (21/10) I_0 I_2$:
$R_1 R_3 - (21/10) R_2^2 = R_2^2 [R_1 R_3 / R_2^2 - 21/10] = R_2^2 [\sqrt{6}/2 - 21/10] = R_2^2[(5\sqrt{6} - 21)/10]$.

$5\sqrt{6} \approx 5 \times 2.449 = 12.247$. So $5\sqrt{6} - 21 \approx -8.75 < 0$.

So the 2x2 minor is NEGATIVE. ✓ Confirms the main term is not PSD.

### §4.6 The exact Cauchy-Schwarz failure ratio

Set $\rho_k := g_k^2 / (g_{k-1} g_{k+1}) = (2k+5)(2k+4)/((2k+3)(2k+2))$ and $r_k := R_k^2 / (R_{k-1} R_{k+1})$.

For Hankel PSD at the 2x2 minor centered at rung $k$: need $r_k \cdot \rho_k \le 1$.

Compute $r_k = R_k^2/(R_{k-1}R_{k+1}) = (1/(N k(k+1)))/(1/\sqrt{N(k-1)k \cdot N k(k+1)(k+2)})$ — wait this is wrong. Let me redo.

$R_k = 1/\sqrt{Nk(k+1)}$. $R_k^2 = 1/(Nk(k+1))$. $R_{k-1}R_{k+1} = 1/\sqrt{N(k-1)k} \cdot 1/\sqrt{N(k+1)(k+2)} = 1/(N \sqrt{(k-1)k(k+1)(k+2)})$.

$r_k = R_k^2/(R_{k-1}R_{k+1}) = (1/(Nk(k+1))) \cdot N\sqrt{(k-1)k(k+1)(k+2)} = \sqrt{(k-1)k(k+1)(k+2)}/(k(k+1)) = \sqrt{(k-1)(k+2)/(k(k+1))}$.

Simplify: $r_k = \sqrt{(k-1)(k+2)/(k(k+1))}$. For $k \ge 2$, this is $\sqrt{(k^2+k-2)/(k^2+k)} = \sqrt{1 - 2/(k^2+k)} < 1$. So $r_k < 1$ for $k \ge 2$. (At $k=2$: $r_2 = \sqrt{1 \cdot 4 / 6} = \sqrt{2/3} \approx 0.816$.)

And $\rho_k = (2k+5)(2k+4)/((2k+3)(2k+2)) = 1 + (2k+5)(2k+4)/((2k+3)(2k+2)) - 1$.

Numerator: $(2k+5)(2k+4) - (2k+3)(2k+2) = 4k^2 + 18k + 20 - (4k^2 + 10k + 6) = 8k + 14$.

So $\rho_k = 1 + (8k+14)/((2k+3)(2k+2))$. At $k=1$: $\rho_1 = 1 + 22/(5 \cdot 4) = 1 + 22/20 = 42/20 = 21/10$. ✓ At $k=2$: $\rho_2 = 1 + 30/(7 \cdot 6) = 1 + 30/42 = 1 + 5/7 = 12/7 \approx 1.714$.

So as $k \to \infty$: $r_k \to 1$ and $\rho_k \to 1$. The product $r_k \rho_k \to 1$. The question is whether $r_k \rho_k$ ever drops below 1.

At $k=1$: $r_1 = \sqrt{0 \cdot 3 / (1 \cdot 2)} = 0$. Wait that's wrong — $r_1$ requires $R_0$ which is undefined ($R_0 = 1/\sqrt{N \cdot 0 \cdot 1}$, divergent).

Right, the formula $r_k$ requires $k \ge 1$ and $k - 1 \ge 1$, i.e., $k \ge 2$.

So at $k=2$: $r_2 = \sqrt{2/3} \approx 0.816$, $\rho_2 = 12/7 \approx 1.714$, product $\approx 1.399 > 1$. NOT PSD at rung-2 minor.

At $k=3$: $r_3 = \sqrt{2 \cdot 5/(3 \cdot 4)} = \sqrt{10/12} = \sqrt{5/6} \approx 0.913$, $\rho_3 = 1 + 38/(9 \cdot 8) = 1 + 38/72 = 1 + 19/36 = 55/36 \approx 1.528$. Product $\approx 1.395 > 1$. NOT PSD.

General: $r_k \rho_k = \sqrt{(k-1)(k+2)/(k(k+1))} \cdot (2k+5)(2k+4)/((2k+3)(2k+2))$.

Asymptotic as $k \to \infty$: $r_k = 1 - 1/k^2 + O(1/k^3)$, $\rho_k = 1 + 4/(2k)^2 \cdot 2 + O(1/k^3) = 1 + 2/k^2 + O(1/k^3)$. Product $\approx 1 + 1/k^2$. Always $> 1$ asymptotically.

**$r_k \rho_k > 1$ for all $k \ge 2$, hence the coset-averaged main term Hankel is NOT PSD at any 2×2 minor.**

This is a clean structural failure of Vector B's main term to be PSD, **independent of $N$ and independent of the prime measure $d\nu_N$**. The Cauchy-Schwarz violation is structural.

---

## §5. The arch part and the structural residual

### §5.1 Arch Hankel is PSD

By ArchStruct Cor 2(ii), the arch Hankel $J_n^{\mathrm{arch,joint}}(N) \preceq 0$ (negative semi-definite), so the boundary $\mathcal{E}^{\mathrm{arch}}_{k+1}(N) = -\mu_{k+1}^{\mathrm{arch,joint}}(N)$ produces a Hankel matrix $\mathrm{Arch}_n(N) := (\mathcal{E}^{\mathrm{arch}}_{i+j+1}(N))_{i,j}$ that is PSD (Hankel of $-\mu^{\mathrm{arch}}_{k+1}(N)$).

This is the **arch term**: positive Hankel, with explicit Hurwitz-zeta atomic structure.

### §5.2 Equidistribution residual

The residual $\mathcal{R}_k(N) = \varphi(N) \sum_c \langle h_{k+1}, \chi_c\rangle \epsilon_k(c; N)$ is controlled by Siegel–Walfisz applied to the prime-power density $d\nu_N$.

For any $X$ and any $A > 0$: $|\epsilon_k(c; N)| \le C_k \bar S_k(N) (\log X)^{-A}$ uniformly in $c$, for $N \le (\log X)^A$ (Siegel–Walfisz, ineffective).

The Hankel matrix of residuals $\mathrm{Err}_n(N) := (\mathcal{R}_{i+j}(N))_{i,j}$ has operator norm bounded by $\sup_c \|Q_c^{(N)}\| \cdot \varphi(N) \cdot \sup_c |\epsilon_k(c; N)|$ where $Q_c^{(N)}$ is the $c$-coset Q-matrix at rung-$k$ structure. For any FIXED $n$, $N$, the operator norm $\to 0$ as the cutoff in $d\nu_N$ grows.

In the limit of full $d\nu_N$ (no cutoff), the residual $\mathcal{R}_k(N) \to 0$? **No — the prime sum is unconditionally divergent for the unweighted von Mangoldt density, but the polynomial-times-exponential weight makes $\bar S_k(N) < \infty$.** The residual is bounded by Mertens-type bounds on the equidistribution rate; ineffective Siegel–Walfisz makes $\mathcal{R}_k(N) / \bar S_k(N) \to 0$ asymptotically but not uniformly in $k$.

### §5.3 The decomposition

Assembling:

$$\boxed{\;J_n^{\mathrm{prime,joint}}(N) \;=\; \mathrm{Main}_n(N) \;+\; \mathrm{Err}_n(N) \;+\; \mathrm{Arch}_n(N), \;}$$

with the structural signs:
- $\mathrm{Main}_n(N)$: indefinite, with $\det$ at every 2x2 minor strictly NEGATIVE by §4 Cauchy-Schwarz computation. **Pulls the positivity DOWN.**
- $\mathrm{Err}_n(N)$: sign-indefinite, but vanishes as cutoff grows (Siegel–Walfisz). **Small.**
- $\mathrm{Arch}_n(N)$: PSD (positive Hankel of arch atomic measure). **Pulls the positivity UP.**

### §5.4 The remaining structural question

**Unconditional Stieltjes positivity $J_n^{\mathrm{prime,joint}}(N) \succeq 0$ reduces to:**

> *Does $\mathrm{Arch}_n(N)$ dominate $-\mathrm{Main}_n(N)|_{\text{neg eigenvalues}} + \|\mathrm{Err}_n(N)\|$, uniformly in $n$ and $N$?*

This is a precise quantitative question:
1. Is $-\det\mathrm{Main}_n(N) \cdot \lambda_{\max}^{-1}(\mathrm{Main}_n(N))^{-1}$ (the magnitude of the indefinite contribution) bounded above by $\lambda_{\min}(\mathrm{Arch}_n(N))$?
2. Is the Siegel–Walfisz residual $\|\mathrm{Err}_n(N)\|$ subdominant to the arch margin?

The empirical answer at $N = 30, 210$ for $n \le 14$ is YES (with margin LDL diagonal $\ge 0.84$ at $N = 210$). The structural answer is open.

---

## §6. What T28 accomplishes (and does not)

### §6.1 Closed structural finding

**T28 §4 (Cauchy-Schwarz computation):** The coset-averaged main term of the prime-joint Stieltjes Hankel at primorial $N$ is structurally NOT PSD. The Cauchy-Schwarz ratio is **explicit and dimensional**: $r_k \rho_k > 1$ for all $k \ge 2$, with closed-form values $r_k = \sqrt{(k-1)(k+2)/(k(k+1))}$ and $\rho_k = (2k+5)(2k+4)/((2k+3)(2k+2))$.

**This is a clean negative result.** The "obvious" Vector B attack (coset averaging + Stieltjes structure of the main term) does NOT close the Stieltjes positivity. The empirical positivity must come from **arch domination** of the indefinite main + residual.

### §6.2 Open structural question

**The unconditional Stieltjes positivity reduces to arch domination of the indefinite main term + Siegel–Walfisz residual.** This is a precise quantitative question, structurally isolated for the first time. The previous attempts (T8.4 Lemma 6.4, principal-coset variant) tried to show the prime side ALONE is PSD; T28 shows this is structurally impossible and isolates the actual closing mechanism: arch-domination.

### §6.3 Forward doors

1. **T28.1 — Arch-domination at fixed $n, N$.** Quantitative comparison of $\lambda_{\min}(\mathrm{Arch}_n(N))$ vs $\sup_v |v^T \mathrm{Main}_n(N) v|/\|v\|^2$ at the empirically tested levels. Does the arch margin scale at the right rate?

2. **T28.2 — Cauchy-Schwarz tightening via $\langle h_k, \chi_c \rangle$ off-diagonal structure.** The Vector B decomposition averaged the $\langle h_k, \chi_c\rangle$ across cosets to extract the trivial coefficient $\varphi(N) R_k$. This collapses information. A more careful decomposition (e.g., conjugate-pair symmetry, or grouping by real-vs-complex characters) might give a different main term that IS PSD. Open.

3. **T28.3 — Bypass via explicit-formula sign cancellation.** The explicit formula gives $\sum_n \Lambda(n)/\sqrt{n} \cdot f(\log n) = \text{archimedean} + \sum_\rho \hat f(\rho)$ for appropriate test $f$. The sign of $\sum_\rho \hat f(\rho)$ under RH is the on-line-zero positivity; without RH, off-line zeros contribute sign. T28's main term IS, modulo constants, the prime side of the explicit formula. The arch term IS the archimedean side. Their combination IS the zero side. So $J_n^{\mathrm{prime,joint}}(N) \succeq 0 \Longleftrightarrow$ zero side has positive Hankel cumulants $\Longleftrightarrow$ GRH at primorial $N$. **This is exactly the (GBP) circular obstruction at the simplicial level.**

### §6.4 Honest residual

T28 does NOT close the Stieltjes positivity unconditionally. It identifies the explicit obstruction: the coset-averaged main term is NOT PSD (Cauchy-Schwarz factor $r_k \rho_k > 1$ structurally), and the empirical positivity comes from arch domination, which is what GRH at primorial $N$ requires.

**The (GBP) obstruction transfers to T28 at the simplicial level:** the unconditional prime-side Stieltjes positivity at primorial $N$ is equivalent to GRH at primorial $N$, just as (GBP) is equivalent to RH at the Archimedean level.

---

## §7. Summary

- **T28 §3 (coset averaging):** unconditional structural decomposition $J^{\mathrm{prime,joint}}_n(N) = \mathrm{Main} + \mathrm{Err} + \mathrm{Arch}$.
- **T28 §4 (Cauchy-Schwarz):** $\mathrm{Main}_n(N)$ is structurally NOT PSD, with explicit ratio $r_k \rho_k = \sqrt{(k-1)(k+2)/(k(k+1))} \cdot (2k+5)(2k+4)/((2k+3)(2k+2)) > 1$ for $k \ge 2$.
- **T28 §5 (residual):** $\mathrm{Err}_n(N)$ controlled by Siegel–Walfisz; $\mathrm{Arch}_n(N) \succeq 0$ by ArchStruct.
- **T28 §6 (obstruction):** unconditional closure requires arch domination, which is GRH at primorial $N$ — the simplicial-level (GBP) obstruction.

**Vector B does not close the kernel positivity unconditionally. It precisely isolates the closing mechanism (arch domination) and reproduces the (GBP) obstruction at the simplicial level.**

---

## §8. Files

- This paper: `T28-VectorB-CosetAveraging-StieltjesPositivity-Draft1.md`.
- Audited: `T8.4-StieltjesPositivityPrimeMultiplicativeApex-Draft1.md` §§5–7, `T8.4-Lemma-6p4-Falsification-Note.md`.
- Supporting: `T9.4-GaussSumDecompositionConductorBlocks-Draft1.md` (Cor 5.1), `T9-HelmertFourierTransferMatrix-Draft1.md` (Thm 2.1, character orthogonality), `ArchStruct` (Thm 1, Cor 2(ii)).
- Pending probe: empirical verification of $r_k \rho_k > 1$ at higher $k$, and of arch-domination margin scaling with $N$.

---

## §9. References

- Murillo Montero, L. (2026). T8.4 — Stieltjes Positivity of the Prime-Side Multiplicative Apex at Primorial Scale.
- Murillo Montero, L. (2026). T8.4 Lemma 6.4 Falsification Note (May 25).
- Murillo Montero, L. (2026). T9 — Helmert-Fourier Transfer Matrix.
- Murillo Montero, L. (2026). T9.4 — Gauss Sum Decomposition into Conductor Blocks.
- Murillo Montero, L. (2026). ArchStruct — Archimedean Structure Theorems.
- Murillo Montero, L. (2026). Paper III — Closure Draft 2 (§9.3 Main Theorem 9.4 fourfold equivalence RH ⟺ (GBP)).

---

*T28 attempts Vector B (coset-averaged kernel re-factorization) and finds: (i) coset averaging gives a clean structural decomposition $\mathrm{Main} + \mathrm{Err} + \mathrm{Arch}$; (ii) the main term is structurally NOT PSD with explicit Cauchy-Schwarz factor $r_k \rho_k > 1$ for all $k \ge 2$; (iii) the unconditional closure requires arch-domination, which is GRH at primorial $N$. The Vector B path therefore reproduces the (GBP) obstruction at the simplicial level — not a closure, but a clean isolation of where the closing condition is.*
