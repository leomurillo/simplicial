# Structural Theorems for the Joint Primorial Archimedean Cumulants

**Leonardo Murillo Montero + Codex**

*Draft 1 — May 25, 2026 — formalization of the structural duality from the N=210 joint probe*

## Abstract

Let $N$ be a positive integer and let $\hat{X}_N$ denote the set of primitive Dirichlet characters of conductor dividing $N$. The joint completed L-function $\Xi_N(z) = \prod_{\chi \in \hat{X}_N} \Lambda(\chi, 1/2 + iz)$ (with the trivial-character factor taken to be $\xi$, so that $\Xi_N$ is entire) gives rise to joint cumulants $\mu_k^{\mathrm{joint}}(N) := \ell_{k+1}^{\mathrm{joint}}(N)$. The archimedean part of the joint log-derivative $\Xi'_N/\Xi_N$ produces a sub-sequence $\mu_k^{\mathrm{arch,joint}}(N)$ that admits a closed-form Hurwitz-zeta expression.

**We prove**:

1. **Theorem 1 (Joint arch atomic structure):** For $N$ with at least one non-trivial primitive even Dirichlet character of conductor dividing $N$ (the smallest such $N$ is 5; in particular all primorials $N \ge 30$), the joint arch cumulant sequence $\mu_k^{\mathrm{arch,joint}}(N)$ is the moment sequence of an *explicit positive atomic measure* $\sigma_N^{\mathrm{arch}}$ supported on the negative real axis.

2. **Corollary 2 (Hankel signatures):** Under the hypothesis of Theorem 1, the joint arch Hankel matrices satisfy $H_n^{\mathrm{arch,joint}}(N) \succeq 0$ and $J_n^{\mathrm{arch,joint}}(N) \preceq 0$ for every $n \ge 0$.

3. **Theorem 3 (Apex split):** Apex Lemma$_{HJ}$ at primorial $N$ is equivalent to two analytical inequalities relating the explicit closed-form arch piece to the prime-side cumulants. The H slot's "easy half" and J slot's "easy half" are *automatic from the structural arch theorems*; the remaining analytical content concentrates entirely on the prime side.

Theorems 1 and Corollary 2 are *unconditional* (no GRH assumption). Theorem 3 reformulates Apex Lemma$_{HJ}$ as a specific analytical bound the prime side must satisfy, with the arch side fully calibrated.

## 1. Setup

### 1.1 Completed L-functions and parities

For each primitive Dirichlet character $\chi$ of conductor $f_\chi$ and parity $a_\chi := (1 - \chi(-1))/2 \in \{0, 1\}$:

- $a_\chi = 0$ ⟺ $\chi(-1) = +1$: **even character**.
- $a_\chi = 1$ ⟺ $\chi(-1) = -1$: **odd character**.

The completed L-function is
$$\Lambda(\chi, s) := \left(\frac{f_\chi}{\pi}\right)^{(s+a_\chi)/2} \Gamma\!\left(\frac{s+a_\chi}{2}\right) L(\chi, s).$$

For the trivial character ($f = 1$, even), we use Riemann's completed function
$$\xi(s) := \tfrac{1}{2}\, s(s-1)\, \pi^{-s/2}\, \Gamma(s/2)\, \zeta(s),$$
which differs from $\Lambda(\chi_0, s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ by the polar factor $s(s-1)/2$. The factor $\xi$ is entire; $\Lambda(\chi_0)$ has poles at $s = 0, 1$. We use $\xi$ in the joint product to keep $\Xi_N$ entire.

### 1.2 Joint completed function and folded variable

Set $\hat{X}_N^{\times} := \hat{X}_N \setminus \{\chi_0\}$. The joint product is
$$\Xi_N(z) := \xi(1/2 + iz) \prod_{\chi \in \hat{X}_N^{\times}} \Lambda(\chi, 1/2 + iz).$$

This is entire of order $1$ (product of finitely many entire functions of order $1$). It satisfies the functional equation $\Xi_N(z) = \overline{\Xi_N(\bar z)} = \pm \Xi_N(-z)$ (depending on the joint root number, but the modulus is invariant).

The folded form:
$$B_N(x) := \frac{\Xi_N(i\sqrt{x})}{\Xi_N(0)}, \qquad F_N(x) := \frac{B'_N(x)}{B_N(x)}.$$

With $t = \sqrt{x}$, $s = 1/2 + t$:
$$F_N(x) = \frac{1}{2t}\, G_N(s), \quad \text{where} \quad G_N(s) := \frac{\xi'(s)}{\xi(s)} + \sum_{\chi \in \hat{X}_N^{\times}} \frac{\Lambda'(\chi, s)}{\Lambda(\chi, s)}.$$

By the functional equations $\xi(s) = \xi(1-s)$ and $\Lambda(\chi, s) = W(\chi)\Lambda(\bar\chi, 1-s)$, the joint sum $G_N(1/2 + t)$ is an odd function of $t$. Hence $F_N(x)$ is a single-valued analytic function of $x$ in a neighborhood of $0$, with Taylor expansion
$$F_N(x) = \sum_{k \ge 0} (-1)^k\, \mu_k^{\mathrm{joint}}(N)\, x^k, \qquad \mu_k^{\mathrm{joint}}(N) = \ell_{k+1}^{\mathrm{joint}}(N).$$

### 1.3 Archimedean/prime split

Standard derivative formulas give:
$$\frac{\xi'(s)}{\xi(s)} = \frac{1}{s} + \frac{1}{s-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{s}{2}\right) + \frac{\zeta'(s)}{\zeta(s)},$$
$$\frac{\Lambda'(\chi, s)}{\Lambda(\chi, s)} = \frac{1}{2}\log\frac{f_\chi}{\pi} + \frac{1}{2}\psi\!\left(\frac{s+a_\chi}{2}\right) + \frac{L'(\chi, s)}{L(\chi, s)}.$$

Define the joint archimedean and joint prime functions:
$$A_N(s) := \frac{1}{s} + \frac{1}{s-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{s}{2}\right) + \sum_{\chi \in \hat{X}_N^{\times}} \left[\frac{1}{2}\log\frac{f_\chi}{\pi} + \frac{1}{2}\psi\!\left(\frac{s+a_\chi}{2}\right)\right],$$
$$P_N(s) := \frac{\zeta'(s)}{\zeta(s)} + \sum_{\chi \in \hat{X}_N^{\times}} \frac{L'(\chi, s)}{L(\chi, s)}.$$

Then $G_N(s) = A_N(s) + P_N(s)$, and accordingly:
$$F_N(x) = F_N^{\mathrm{arch}}(x) + F_N^{\mathrm{prime}}(x)$$
$$\mu_k^{\mathrm{joint}}(N) = \mu_k^{\mathrm{arch,joint}}(N) + \mu_k^{\mathrm{prime,joint}}(N)$$
where
$$\mu_k^{\mathrm{arch,joint}}(N) := (-1)^k \frac{1}{(2k+1)! \cdot 2} \cdot \frac{d^{2k+1}}{dt^{2k+1}}\Big|_{t=0} A_N(1/2 + t).$$

The constants $-\log\pi/2$ and $(1/2)\log(f_\chi/\pi)$ vanish in higher derivatives.

## 2. Per-character atomic representation

### Lemma A (Non-zeta arch atomic decomposition)

For any primitive Dirichlet character $\chi \in \hat{X}_N^{\times}$ of conductor $f_\chi$ and parity $a_\chi$:
$$\boxed{\mu_k^{\mathrm{arch}, \chi} = \int_{-\infty}^{0} s^k \, d\sigma_\chi(s)}$$
where $\sigma_\chi$ is the **positive atomic measure** on $(-\infty, 0)$ given by
$$d\sigma_\chi(s) := \sum_{n \ge 0} c_{n,\chi}\, \delta_{\lambda_{n,\chi}}(s), \quad c_{n,\chi} := \frac{2}{(4n + 1 + 2a_\chi)^2}, \quad \lambda_{n,\chi} := -\frac{4}{(4n + 1 + 2a_\chi)^2}.$$

For even $\chi$ ($a = 0$): atoms at $\lambda \in \{-4, -4/25, -4/81, -4/169, \ldots\}$, with masses $\{2, 2/25, 2/81, \ldots\}$.

For odd $\chi$ ($a = 1$): atoms at $\lambda \in \{-4/9, -4/49, -4/121, \ldots\}$, with masses $\{2/9, 2/49, 2/121, \ldots\}$.

**Proof.** The constant term $(1/2)\log(f_\chi/\pi)$ in $A_\chi(s)$ contributes only to $s = 1/2$ and not to higher derivatives. The remaining piece is $(1/2)\psi((s + a_\chi)/2)$.

Setting $s = 1/2 + t$:
$$\frac{1}{2}\psi\!\left(\frac{1/2 + t + a_\chi}{2}\right) = \frac{1}{2}\psi(b_\chi + t/2), \quad b_\chi := \frac{1/2 + a_\chi}{2} = \begin{cases} 1/4 & \text{even} \\ 3/4 & \text{odd} \end{cases}$$

Taylor expansion: $\psi(b_\chi + t/2) = \psi(b_\chi) + \sum_{n \ge 1} \psi^{(n)}(b_\chi) (t/2)^n / n!$. Using the polygamma identity $\psi^{(n)}(s) = (-1)^{n+1} n! \zeta(n+1, s)$ for $n \ge 1$ (with $\zeta(s, a)$ the Hurwitz zeta), we get
$$\psi(b_\chi + t/2) - \psi(b_\chi) = \sum_{n \ge 1} \frac{(-1)^{n+1} \zeta(n+1, b_\chi)}{2^n} t^n.$$

Thus the coefficient of $t^{2k+1}$ in $(1/2) \psi(b_\chi + t/2)$ is
$$a_{2k+1}^\chi = \frac{1}{2} \cdot \frac{\zeta(2k+2, b_\chi)}{2^{2k+1}} = \frac{\zeta(2k+2, b_\chi)}{2^{2k+2}}.$$
(using $(-1)^{2k+2} = 1$).

Therefore
$$\mu_k^{\mathrm{arch}, \chi} = (-1)^k \frac{a_{2k+1}^\chi}{2} = (-1)^k \frac{\zeta(2k+2, b_\chi)}{2^{2k+3}}.$$

Expanding the Hurwitz zeta:
$$\zeta(2k+2, b_\chi) = \sum_{n \ge 0} \frac{1}{(n + b_\chi)^{2k+2}}.$$

Substituting:
$$\mu_k^{\mathrm{arch}, \chi} = (-1)^k \sum_{n \ge 0} \frac{1}{2^{2k+3} (n + b_\chi)^{2k+2}}.$$

Set $r_n := 2(n + b_\chi) > 0$. Then $2^{2k+2}(n + b_\chi)^{2k+2} = r_n^{2k+2}$, so $2^{2k+3}(n+b_\chi)^{2k+2} = 2 r_n^{2k+2}$. Hence
$$\mu_k^{\mathrm{arch}, \chi} = \sum_{n \ge 0} \frac{(-1)^k}{2 r_n^{2k+2}} = \sum_{n \ge 0} \frac{1}{2 r_n^2} \cdot \left(-\frac{1}{r_n^2}\right)^k.$$

Setting $\lambda_n := -1/r_n^2 \in (-1/r_0^2, 0) \subset (-\infty, 0)$ and $c_n := 1/(2 r_n^2) = |\lambda_n|/2 > 0$:
$$\mu_k^{\mathrm{arch}, \chi} = \sum_{n \ge 0} c_n \lambda_n^k = \int s^k \, d\sigma_\chi(s).$$

For $b_\chi = 1/4$: $r_n = 2n + 1/2 = (4n+1)/2$, so $r_n^2 = (4n+1)^2/4$, $\lambda_n = -4/(4n+1)^2$, $c_n = 2/(4n+1)^2$. ✓

For $b_\chi = 3/4$: $r_n = (4n+3)/2$, $\lambda_n = -4/(4n+3)^2$, $c_n = 2/(4n+3)^2$. ✓ $\square$

### Lemma B (Zeta arch atomic decomposition)

For the zeta factor (conductor $f = 1$, even, with poles):
$$\mu_k^{\mathrm{arch}, \zeta} = \int_{-\infty}^0 s^k\, d\sigma_\zeta(s)$$
where $\sigma_\zeta$ is the signed atomic measure
$$d\sigma_\zeta(s) := d\sigma_{1/4}(s) - 4\, \delta_{-4}(s),$$
with $d\sigma_{1/4} := d\sigma_\chi$ for a hypothetical even character with $b_\chi = 1/4$ (i.e., atoms at $-4/(4n+1)^2$ with masses $2/(4n+1)^2$).

The signed measure $\sigma_\zeta$ has all positive masses except at $\lambda_0 = -4$, where the net mass is $2 - 4 = -2$ (negative).

**Proof.** $A_\zeta(s) = 1/s + 1/(s-1) - (\log\pi)/2 + (1/2)\psi(s/2)$. The polygamma piece is the same as for an even character with $a_\chi = 0$, contributing $d\sigma_{1/4}$.

The pole pieces: at $s = 1/2 + t$:
$$\frac{1}{s} = \frac{1}{1/2 + t} = \frac{2}{1 + 2t} = \sum_{n \ge 0} (-2)^n \cdot 2 t^n = \sum_{n \ge 0} (-1)^n\, 2^{n+1}\, t^n,$$
$$\frac{1}{s-1} = \frac{1}{t - 1/2} = -\frac{2}{1 - 2t} = -\sum_{n \ge 0} 2^{n+1}\, t^n.$$

Sum: $\sum_n [(-1)^n - 1] 2^{n+1} t^n = -\sum_{n\text{ odd}} 2^{n+2}\, t^n$.

For $n = 2k+1$: coefficient is $-2^{2k+3}$. So:
$$\mu_k^{\mathrm{arch}, \zeta, \text{pole}} = (-1)^k \cdot \frac{-2^{2k+3}}{2} = -(-1)^k \cdot 2^{2k+2} = -4 \cdot (-4)^k.$$

This is the moment sequence of the signed atomic measure $-4 \delta_{-4}$ (atom at $\lambda = -4$ with mass $-4$). $\square$

## 3. Theorem 1 — Joint arch is positive atomic on the negative real axis

### Theorem 1

Let $N \ge 1$ and define
$$N_E := \#\{\chi \in \hat{X}_N^{\times} : \chi \text{ is even}\}, \qquad N_O := \#\{\chi \in \hat{X}_N^{\times} : \chi \text{ is odd}\},$$
counting each primitive character once (so a non-self-dual pair contributes 2 to either $N_E$ or $N_O$).

If $N_E \ge 1$, then there exists a positive atomic measure $\sigma_N^{\mathrm{arch}}$ supported on the negative real axis $(-\infty, 0)$ such that
$$\mu_k^{\mathrm{arch,joint}}(N) = \int_{-\infty}^0 s^k\, d\sigma_N^{\mathrm{arch}}(s) \quad \text{for all } k \ge 0.$$

The measure is given explicitly by
$$d\sigma_N^{\mathrm{arch}}(s) = \sum_{n \ge 0} M_{4n+1}\, \delta_{-4/(4n+1)^2}(s) + \sum_{n \ge 0} M_{4n+3}\, \delta_{-4/(4n+3)^2}(s)$$
with atomic masses
$$M_1 = -2 + 2 N_E, \quad M_{4n+1} = \frac{2(1 + N_E)}{(4n+1)^2} \;\; (n \ge 1), \quad M_{4n+3} = \frac{2 N_O}{(4n+3)^2} \;\; (n \ge 0).$$

All masses are non-negative; the mass at $\lambda = -4$ (corresponding to $k=1$, $n=0$) is non-negative iff $N_E \ge 1$.

### Proof

By Lemmas A and B, the joint arch cumulant is a finite linear combination of moment sequences of atomic measures with rational atom locations $-4/(2m+1)^2$ for odd $2m+1 \ge 1$.

We collect contributions at each atom location:

**At $\lambda = -4$ (corresponding to $r_0 = 1/2$, $m = 0$):**
- Zeta-pole: mass $-4$.
- Zeta-$\psi$ (Lemma B): mass $\alpha_0^{1/4}/2 = 2/1 = 2$ (the $n=0$ term of $\zeta(\cdot, 1/4)$).
- Each non-zeta **even** L-function (Lemma A with $b = 1/4$): mass $2/1 = 2$ (per L-function).
- Each non-zeta **odd** L-function: mass $0$ at $\lambda = -4$ (atoms at $\lambda = -4/(4n+3)^2$ instead).

Total mass at $\lambda = -4$:
$$M_1 = -4 + 2 + 2 N_E = -2 + 2 N_E.$$

**At $\lambda = -4/(4n+1)^2$ for $n \ge 1$:**
- Zeta-pole: contributes nothing (only at $\lambda = -4$).
- Zeta-$\psi$: mass $2/(4n+1)^2$.
- Each non-zeta even L-function: mass $2/(4n+1)^2$.

Total: $M_{4n+1} = 2(1 + N_E)/(4n+1)^2 > 0$.

**At $\lambda = -4/(4m+3)^2$ for $m \ge 0$:**
- Only non-zeta odd L-functions contribute.

Total: $M_{4m+3} = 2 N_O/(4m+3)^2 \ge 0$, with strict inequality when $N_O \ge 1$.

Summing all contributions:
$$\mu_k^{\mathrm{arch, joint}}(N) = \sum_{m \ge 0} M_{2m+1} \cdot \left(-\frac{4}{(2m+1)^2}\right)^k = \int s^k \, d\sigma_N^{\mathrm{arch}}(s).$$

The measure $\sigma_N^{\mathrm{arch}}$ is a positive (in the sense $\ge 0$) atomic measure on $(-\infty, 0)$ iff all masses $M_{2m+1} \ge 0$. The only potentially negative mass is $M_1 = -2 + 2N_E$, which is non-negative iff $N_E \ge 1$. $\square$

## 4. Corollary 2 — Hankel positivity/negativity signatures

### Corollary 2

Under the hypothesis of Theorem 1 ($N$ such that $N_E \ge 1$):

(i) **H-positivity.** $H_n^{\mathrm{arch, joint}}(N) := (\mu_{i+j}^{\mathrm{arch, joint}}(N))_{0 \le i,j \le n} \succeq 0$ for all $n \ge 0$.

(ii) **J-negativity.** $J_n^{\mathrm{arch, joint}}(N) := (\mu_{i+j+1}^{\mathrm{arch, joint}}(N))_{0 \le i,j \le n} \preceq 0$ for all $n \ge 0$.

### Proof

(i) For any $v = (v_0, \ldots, v_n) \in \mathbb{R}^{n+1}$ with polynomial $q(s) := \sum_{i=0}^n v_i s^i$:
$$v^T H_n^{\mathrm{arch, joint}} v = \sum_{i,j} v_i v_j \mu_{i+j}^{\mathrm{arch, joint}} = \int \left(\sum_i v_i s^i\right)\!\left(\sum_j v_j s^j\right) d\sigma_N^{\mathrm{arch}}(s) = \int q(s)^2 \, d\sigma_N^{\mathrm{arch}}(s) \ge 0,$$
because $\sigma_N^{\mathrm{arch}} \ge 0$ as a measure and $q(s)^2 \ge 0$ as an integrand.

(ii) Similarly,
$$v^T J_n^{\mathrm{arch, joint}} v = \int s\, q(s)^2 \, d\sigma_N^{\mathrm{arch}}(s).$$
Since $\sigma_N^{\mathrm{arch}}$ is supported on $(-\infty, 0)$, $s < 0$ throughout the support, so $s\, q(s)^2 \le 0$ on $\mathrm{supp}(\sigma_N^{\mathrm{arch}})$. Hence the integral is $\le 0$, giving $J_n^{\mathrm{arch, joint}}(N) \preceq 0$. $\square$

## 5. Theorem 3 — Apex Lemma$_{HJ}$ split

### Theorem 3

Let $N$ be primorial with $N_E \ge 1$ (in particular all primorials $N \ge 30$). Define the prime cumulants
$$\mu_k^{\mathrm{prime, joint}}(N) := \mu_k^{\mathrm{joint}}(N) - \mu_k^{\mathrm{arch, joint}}(N),$$
the prime Hankel and shifted Hankel
$$H_n^{\mathrm{prime, joint}}(N), \quad J_n^{\mathrm{prime, joint}}(N).$$

Then **Apex Lemma$_{HJ}$ at $N$** (i.e., $H_n^{\mathrm{joint}}(N), J_n^{\mathrm{joint}}(N) \succeq 0$ for all $n$) is equivalent to the conjunction of:

**(Apex-H)** For every $n \ge 0$:
$$H_n^{\mathrm{prime, joint}}(N) + H_n^{\mathrm{arch, joint}}(N) \succeq 0.$$
By Corollary 2(i), $H_n^{\mathrm{arch, joint}}(N) \succeq 0$. So Apex-H is equivalent to the prime piece not subtracting more from the arch piece's positive cone than the latter can absorb. In particular, $v^T H_n^{\mathrm{prime, joint}}(N) v \ge -v^T H_n^{\mathrm{arch, joint}}(N) v$ for every $v$.

**(Apex-J)** For every $n \ge 0$:
$$J_n^{\mathrm{prime, joint}}(N) + J_n^{\mathrm{arch, joint}}(N) \succeq 0.$$
By Corollary 2(ii), $J_n^{\mathrm{arch, joint}}(N) \preceq 0$. So Apex-J is equivalent to the prime piece's positivity dominating the arch piece's negativity: $v^T J_n^{\mathrm{prime, joint}}(N) v \ge -v^T J_n^{\mathrm{arch, joint}}(N) v = |v^T J_n^{\mathrm{arch, joint}}(N) v|$ for every $v$.

### Proof

Direct: $H_n^{\mathrm{joint}} = H_n^{\mathrm{arch}} + H_n^{\mathrm{prime}}$ (entrywise), and likewise for $J$. Apex Lemma$_{HJ}$ asks $H^{\mathrm{joint}}, J^{\mathrm{joint}} \succeq 0$. $\square$

### Remark

Theorem 3 is content-free as a logical equivalence, but it provides:

- **A concrete analytical target.** Apex-H asks for an explicit upper bound on the prime piece's *negativity* in terms of the arch piece's *positivity*, both of which have explicit formulas: arch from Theorem 1 (closed-form Hurwitz-zeta), prime from $\zeta'/\zeta + \sum L'(\chi)/L(\chi)$ (Dirichlet series of $\Lambda(n)$).
- **A natural decomposition for proof strategy.** The two slots of Apex Lemma$_{HJ}$ are decoupled by sign: one needs to control prime's H-negative contribution (against arch H-positivity) and prime's J-positive contribution (against arch J-negativity). These are independent inequalities; one can attack them separately.
- **A failure mode for sub-primorial $N$.** When $N_E = 0$ (e.g., $N \in \{1, 2, 3, 6\}$), Theorem 1's hypothesis fails, $\sigma_N^{\mathrm{arch}}$ has a negative atom at $\lambda = -4$, and Corollary 2(i) is false. The structural duality is **specific to primorial $N \ge 30$** (the first primorial with sufficient even non-trivial characters).

## 6. Numerical verification

### 6.1 Cross-$N$ verification of Theorem 1 and Corollary 2

Computed at mpmath dps=200 (`probe_arch_theorem_verification.py`). For each $N$, $N_E$ and $N_O$ count L-functions (so a non-self-dual pair contributes 2). $M_1 = -2 + 2 N_E$ is Theorem 1's predicted mass at $\lambda = -4$. Asymptotic ratio $\mu_{20}^{\mathrm{arch}}/(M_1 \cdot (-4)^{20})$ should equal 1 when $M_1 \ne 0$.

| $N$ | $N_E$ | $N_O$ | $M_1 = -2+2N_E$ | $H_n^{\mathrm{arch}}$ | $J_n^{\mathrm{arch}}$ | Asymp. ratio |
|---|---|---|---|---|---|---|
| 1 (zeta only) | 0 | 0 | $-2$ | **FAIL** at every $n$ | **FAIL NSD** | $1.000000$ (negative leading atom) |
| 6 (zeta + $\chi_3$) | 0 | 1 | $-2$ | **FAIL** at every $n$ | **FAIL NSD** | $1.000000$ |
| 5 | 1 | 2 | $0$ | **PSD** | **NSD** | (atom at $-4$ absent; leading shifts) |
| 7 | 2 | 2 | $2$ | **PSD** | **NSD** | $1.000000$ |
| 15 | 3 | 4 | $4$ | **PSD** | **NSD** | $1.000000$ |
| 30 | 3 | 4 | $4$ | **PSD** | **NSD** | $1.000000$ |
| 210 | 23 | 24 | $44$ | **PSD** | **NSD** | $1.000000$ |

**Observations matching Theorem 1 + Corollary 2:**

1. **$N \in \{1, 6\}$ ($N_E = 0$, $M_1 = -2 < 0$):** Negative atom present, $H^{\mathrm{arch}}$ FAILS PSD at $n = 0$ (since $\mu_0^{\mathrm{arch}} < 0$). $J^{\mathrm{arch}}$ also fails NSD (indefinite, because the negative-mass atom at $-4$ contributes $c\lambda = (-2)(-4) = +8 > 0$ to $J$). Single-zeta antagonism, as expected.

2. **$N = 5$ ($N_E = 1$, $M_1 = 0$):** The atom at $-4$ is absent. The leading nonzero atoms are at $-4/9$ (odd contribution, mass $\propto N_O$) and $-4/25$ (even, mass $\propto 1 + N_E$). $H^{\mathrm{arch}}$ PSD, $J^{\mathrm{arch}}$ NSD as predicted. Asymptotic ratio undefined (leading atom shifts).

3. **$N \ge 7$ with $N_E \ge 2$:** All atoms have strictly positive mass, $H^{\mathrm{arch}}$ PSD, $J^{\mathrm{arch}}$ NSD. Asymptotic ratio is exactly 1.0 to 6+ digits, confirming Theorem 1's atom-at-$-4$ identification.

4. **$N = 30$ vs $N = 15$:** Identical because conductor 2 has no nontrivial primitive characters, so $\hat{X}_{30}^{\times} = \hat{X}_{15}^{\times}$. ✓

The structural theorem holds **exactly as stated** across all tested $N$. The duality dissolves at $N \le 6$ and emerges starting from $N = 5$ (marginal) and $N = 7+$ (strict).

### 6.2 Verification at $N = 210$ (detailed)

From the joint primorial probe (`probe_arch_prime_N210_joint.py`) at $N = 210$:

- $N_E = 23$ (1 zeta-equivalent + 3 non-zeta even self-dual + 20 non-zeta even from 10 pairs).
  - Wait, this counts L-functions. $N_E$ as defined counts primitive even characters: 3 self-dual + 10 pairs × 2 = 23. ✓ Same.
- $N_O = 24$ (4 self-dual + 20 from 10 pairs).
- Verify: $1 + N_E + N_O = 1 + 23 + 24 = 48 = \varphi(210)$. ✓

**Theorem 1 predictions:**
- Mass at $\lambda = -4$: $M_1 = -2 + 2 \cdot 23 = 44$.
- Asymptotic $\mu_k^{\mathrm{arch, joint}}(210) \sim 44 \cdot (-4)^k$ as $k \to \infty$ (dominant atom).

**Numerical check from probe:**

| $k$ | Predicted $44 \cdot (-4)^k$ | Measured $\mu_k^{\mathrm{arch, joint}}(210)$ |
|---|---|---|
| 0 | $44$ | $55.22$ |
| 1 | $-176$ | $-178.82$ |
| 2 | $704$ | $705.11$ |
| 10 | $4.61 \times 10^7$ | $4.61 \times 10^7$ |
| 20 | $4.84 \times 10^{13}$ | $4.84 \times 10^{13}$ |
| 30 | $5.07 \times 10^{19}$ | $5.07 \times 10^{19}$ |

The agreement at $k \ge 10$ is exact to 4+ significant digits — the sub-leading atoms ($M_{4n+1}$ for $n \ge 1$, $M_{4n+3}$ for $n \ge 0$) contribute relatively $\le (1/9)^k \to 0$. At $k = 0, 1, 2$ the corrections are explicit:
$$\mu_0^{\mathrm{arch, joint}}(210) = 44 + \sum_{n \ge 1} \frac{2(1+23)}{(4n+1)^2} + \sum_{n \ge 0} \frac{2 \cdot 24}{(4n+3)^2} = 44 + 24 \cdot (\zeta(2,1/4)/8 - 2) + 48 \cdot \zeta(2,3/4)/16 \approx 55.22.$$

(Details: $\zeta(2, 1/4) \approx 17.20$, so $\zeta(2, 1/4)/8 - 2 = 2.15 - 2 = 0.15$; $\zeta(2, 3/4) \approx 2.541$, so $\zeta(2,3/4)/16 \approx 0.159$; combining: $44 + 24 \cdot 0.15 + 48 \cdot 0.159 = 44 + 3.6 + 7.62 = 55.22$. ✓)

**Hankel signatures:**
- $H_n^{\mathrm{arch, joint}}(210)$ tested PSD at $n \in \{0, 1, \ldots, 14\}$. ✓ (Corollary 2(i))
- $J_n^{\mathrm{arch, joint}}(210)$ tested negative semi-definite at $n \in \{0, 1, \ldots, 13\}$. ✓ (Corollary 2(ii))

## 7. Open conjectures

The reduction in Theorem 3 makes Apex Lemma$_{HJ}$ at primorial $N$ depend on bounds on the prime side. Two natural conjectures, each equivalent to half of Apex Lemma$_{HJ}$:

### Conjecture 7.1 (Apex-H at primorial $N$)

For every primorial $N \ge 30$ and every $n \ge 0$:
$$v^T H_n^{\mathrm{prime, joint}}(N) v \ge -v^T H_n^{\mathrm{arch, joint}}(N) v \quad \forall v \in \mathbb{R}^{n+1}.$$

Equivalently: the prime Hankel's most-negative eigenvalue magnitude is bounded by the arch Hankel's smallest eigenvalue.

### Conjecture 7.2 (Apex-J at primorial $N$)

For every primorial $N \ge 30$ and every $n \ge 0$:
$$v^T J_n^{\mathrm{prime, joint}}(N) v \ge -v^T J_n^{\mathrm{arch, joint}}(N) v = |v^T J_n^{\mathrm{arch, joint}}(N) v| \quad \forall v \in \mathbb{R}^{n+1}.$$

These conjectures are *empirically verified* through $n = 14$ (H) and $n = 13$ (J) at $N = 210$ (and presumably could be checked at $N = 30$ similarly).

### Conjecture 7.3 (Stieltjes-J of the prime piece, empirical-only)

Empirically $J_n^{\mathrm{prime, joint}}(N) \succeq 0$ at every tested $n$ at $N = 210$. This is *stronger* than what Apex-J requires (which only asks $J^{\mathrm{prime}} \succeq -J^{\mathrm{arch}}$, where $-J^{\mathrm{arch}} \succeq 0$). Conjecture: $J_n^{\mathrm{prime, joint}}(N) \succeq 0$ for all primorial $N \ge 30$ and all $n \ge 0$.

If Conjecture 7.3 holds, it suggests the prime side has an *independent* Stieltjes-positive structure on a half-line — a deeper analytical fact.

## 8. Path forward

**Established (this draft):**
- Joint arch atomic structure (Theorem 1).
- Arch Hankel signatures $H \succeq 0$, $J \preceq 0$ (Corollary 2).
- Apex Lemma$_{HJ}$ split (Theorem 3).
- Numerical verification at $N = 210$ matches to 4+ digits.

**Next analytical targets:**

1. **Quantitative arch lower bound.** Derive an explicit lower bound on $v^T H_n^{\mathrm{arch, joint}}(N) v$ in terms of $\|v\|$, $n$, and $N$. Closed-form Hurwitz-zeta makes this tractable; the dominant atom at $\lambda = -4$ gives leading contribution $M_1 (\sum v_i (-4)^i)^2$, with sub-leading from other atoms.

2. **Explicit-formula attack on prime side.** The joint prime cumulant is
$$\mu_k^{\mathrm{prime, joint}}(N) = \mu_k^{\mathrm{prime}, \zeta} + \sum_{\chi \in \hat{X}_N^\times} \mu_k^{\mathrm{prime}, \chi}.$$
Each per-character prime cumulant can be expanded via the explicit formula or via the Dirichlet series of $\Lambda(n)\chi(n)/n^s$. At primorial scale, character orthogonality reorganizes the sum into prime-power contributions with weights amenable to Bombieri-Lagarias-style or Bettin-Chandee-style bounds.

3. **Conjecture 7.3 from L-function structure.** If $J^{\mathrm{prime, joint}}_n \succeq 0$ can be proven from $L'(\chi)/L(\chi)$ Dirichlet-series structure independent of RH, it gives a clean analytical pathway: Apex-J follows from a Stieltjes-positive prime piece + Corollary 2(ii). Apex-H is then the remaining hard direction.

The simplicial program's distinctive contribution: the joint primorial structure breaks the single-zeta antagonism (probed in `Arch-Prime-Cancellation-Probe-Draft1.md`) into the duality formalized here. This is the first concrete analytical attack target since the structural reduction was completed at $N = 30, 210$.

## References

- **Pass-5**, *Lock A No-Loss and the Born Heat Flow*: §16 (Apex Lemma$_{HJ}$ equivalence), §17 (prime/gamma split).
- **PassFive-Section17-Audit-Draft1.md**: identifies §17.3 as a target, not a theorem.
- **Arch-Prime-Cancellation-Probe-Draft1.md**: single-zeta antagonism documentation.
- **Arch-Prime-N210-Duality-Draft1.md**: joint primorial duality probe.
- **probe_arch_prime_N210_joint.py**: numerical probe at $N = 210$.
- **GRH30-Apex-Verification-Note-Draft1.md**: Apex Lemma$_{HJ}$ at $N = 30, 210$ verified computationally.

## Files

- This note: `Arch-Structural-Theorems-Draft1.md`.

---

*The structural duality is no longer a numerical curiosity. It is a theorem.*
