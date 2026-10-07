# Probe: Archimedean vs Prime Hankel Sequences in the Apex Cumulants

**Leonardo Murillo Montero + Codex**

*Draft 1 — May 25, 2026 — numerical follow-up to Pass-5 §17 audit*

## One-line verdict

**The §17.2 split $F = F_{\mathrm{arch}} + F_{\mathrm{prime}}$ does not support a Bombieri–Lagarias-style attack.** The two cumulant sequences $\mu_k^{\mathrm{arch}}$ and $\mu_k^{\mathrm{prime}}$ are *antagonistic*: they have opposite sign at every $k$, grow as $\pm 2 \cdot 4^k$ each, and cancel to leave the tiny true cumulant $\mu_k \sim \gamma_1^{-2k}$. Cancellation tightness grows exponentially with $k$ (ratio $\sim 10^{-90}$ at $k=30$).

## What we measured

Computed Taylor coefficients of $A(s) = 1/s + 1/(s-1) - (\log\pi)/2 + \psi(s/2)/2$ and $P(s) = \zeta'/\zeta(s)$ at $s = 1/2$ at mpmath dps=250, then extracted

$$\mu_k^{\mathrm{arch}} = (-1)^k \frac{A^{(2k+1)}(1/2)}{2(2k+1)!}, \qquad \mu_k^{\mathrm{prime}} = (-1)^k \frac{P^{(2k+1)}(1/2)}{2(2k+1)!}$$

Sanity: $A(1/2) + P(1/2) = O(10^{-251})$ (matches the symmetry $\xi'/\xi(1/2) = 0$). $\mu_0^{\mathrm{arch}} + \mu_0^{\mathrm{prime}} = 0.023105$ matches the classical value $\sum_{\gamma > 0} 1/\gamma^2 \approx 0.0231$.

### Cumulant table

| $k$ | $\mu_k^{\mathrm{arch}}$ | $\mu_k^{\mathrm{prime}}$ | $\mu_k$ (sum) |
|---|---|---|---|
| 0 | $-1.85033$ | $+1.87344$ | $0.023105$ |
| 1 | $+7.98551$ | $-7.98547$ | $3.72 \times 10^{-5}$ |
| 2 | $-31.9979$ | $+31.9979$ | $1.44 \times 10^{-7}$ |
| 3 | $+128.0$ | $-128.0$ | $6.63 \times 10^{-10}$ |
| 5 | $+2048.0$ | $-2048.0$ | $1.59 \times 10^{-14}$ |
| 10 | $-2.10 \times 10^{6}$ | $+2.10 \times 10^{6}$ | $4.94 \times 10^{-26}$ |
| 20 | $-2.20 \times 10^{12}$ | $+2.20 \times 10^{12}$ | $4.87 \times 10^{-49}$ |
| 30 | $-2.31 \times 10^{18}$ | $+2.31 \times 10^{18}$ | $4.81 \times 10^{-72}$ |

### Sign pattern

```
mu_k^arch  : -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
mu_k^prime : +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
mu_k       : +++++++++++++++++++++++++++++++
```

$\mathrm{sign}(\mu_k^{\mathrm{arch}}) = (-1)^{k+1}$. $\mathrm{sign}(\mu_k^{\mathrm{prime}}) = (-1)^k$. Always opposite. The total is uniformly positive (as it must be under RH).

### Cancellation tightness

$\eta_k := |\mu_k| / \max(|\mu_k^{\mathrm{arch}}|, |\mu_k^{\mathrm{prime}}|)$ — the relative precision needed in any analytical bound to certify $\mu_k > 0$ from the arch and prime pieces separately:

| $k$ | $\eta_k$ |
|---|---|
| 0 | $1.2 \times 10^{-2}$ |
| 1 | $4.7 \times 10^{-6}$ |
| 2 | $4.5 \times 10^{-9}$ |
| 5 | $7.8 \times 10^{-18}$ |
| 10 | $2.4 \times 10^{-32}$ |
| 20 | $2.2 \times 10^{-61}$ |
| 30 | $2.1 \times 10^{-90}$ |

$\eta_k \sim (\gamma_1^{-2}/4)^k$ with $\gamma_1 \approx 14.13$ — exponential decay at rate $\log(\gamma_1^{-2}/4) \approx -6.7$ per rung.

### Hankel positivity test

| $n$ | $H_n^{\mathrm{arch}}$ | $H_n^{\mathrm{prime}}$ | $H_n^{\mathrm{total}}$ | min $D(H_n^{\mathrm{total}})$ |
|---|---|---|---|---|
| 0 | **FAIL** | PSD | PSD | $0.0231$ |
| 1 | **FAIL** | **FAIL** | PSD | $8.4 \times 10^{-8}$ |
| 5 | **FAIL** | **FAIL** | PSD | $4.1 \times 10^{-33}$ |
| 10 | **FAIL** | **FAIL** | PSD | $8.9 \times 10^{-69}$ |
| 15 | **FAIL** | **FAIL** | PSD | $6.2 \times 10^{-107}$ |

**$H_n^{\mathrm{arch}}$ fails PSD at every $n \ge 0$** (because $\mu_0^{\mathrm{arch}} < 0$ already kills the rank-1 minor). **$H_n^{\mathrm{prime}}$ fails at every $n \ge 1$** (because $\mu_0^{\mathrm{prime}} \mu_2^{\mathrm{prime}} - (\mu_1^{\mathrm{prime}})^2 < 0$). The total is uniformly PSD.

## Why this happens — structural reason

The leading-order behavior of $\mu_k^{\mathrm{arch}}$ is determined by the $1/s + 1/(s-1)$ poles of $A$ at $s = 0$ and $s = 1$ plus the asymptotic of $\psi(s/2)$ at $s = 1/2$. Direct computation:

- Pole contribution: $a_{2k+1}^{\text{pole}} = -2^{2k+3}$, giving $\mu_k^{\text{pole}} = -(-1)^k \cdot 4^{k+1}$.
- $\psi$ contribution at large $k$: $a_{2k+1}^{\psi} = \zeta(2k+2, 1/4)/2^{2k+2} \approx 4^{2k+2}/2^{2k+2} = 4^{k+1}$, giving $\mu_k^{\psi} \approx (-1)^k \cdot 2 \cdot 4^k$.

Combining: $\mu_k^{\mathrm{arch}} \approx -(-1)^k \cdot 4^{k+1} + (-1)^k \cdot 2 \cdot 4^k = -(-1)^k \cdot 2 \cdot 4^k$ for $k$ large.

The pole and $\psi$ contributions partially cancel within $A$, but the residual scale is still $\pm 2 \cdot 4^k$ with alternating sign $(-1)^{k+1}$. Since $\zeta(2k+2, 1/4)$ is uniformly positive and the $(-1)^k$ from the conversion $\mu_k = (-1)^k a_{2k+1}/2$ always alternates, **the archimedean sequence cannot be made positive Hankel by any rearrangement of the gamma + pole terms**.

The prime side mirrors arch with opposite sign because $\xi'/\xi(1/2) = 0$ forces $A(1/2) + P(1/2) = 0$ and by analogous derivative identities at every odd order, the leading antagonism propagates to every $k$.

## What this rules out

A clean class of attacks on §17.3 ("True No-Isolator Theorem") is now off the table:

1. **"Archimedean dominates positively, prime is a perturbation."** False at $k = 0$: $\mu_0^{\mathrm{arch}} < 0$.
2. **"Archimedean Hankel is PSD, prime adds a small psd correction."** False at every $n \ge 0$: $H_n^{\mathrm{arch}}$ is indefinite.
3. **"Pointwise inequality $\mathfrak{D}_{p^2}[F_{\mathrm{arch}}] \ge c \cdot \mathfrak{D}_{p^2}[F_{\mathrm{prime}}]$" for some $c > 0$.** False: the two are nearly equal in magnitude and opposite sign at every order — any pointwise inequality with constant $c > 0$ is contradicted by the cancellation.

The analogous Bombieri–Lagarias attack on Li's coefficients suffers a similar antagonism, but in the Li case the integrated bound has different structure (logarithmic integral; cumulative sums) and at least gives positivity at small $n$. The Hankel-positivity setup here is more rigid — the antagonism appears at $k = 0$ already.

## What this allows / suggests

The cancellation $\mu_k^{\mathrm{arch}} + \mu_k^{\mathrm{prime}} \to \mu_k$ is not random: it is the **exact arithmetic content** of $\xi'/\xi(1/2) = 0$ propagated to every odd derivative. So an analytical proof of $\mu_k > 0$ must:

**(α)** Recognize the cancellation as structural, not adversarial. Some identity must convert "arch + prime is a small positive number" into "arch + prime is *manifestly* the sum-over-zeros $\sum_\gamma 1/\gamma^{2(k+1)}$" — at which point positivity is automatic if all zeros are real.

This is essentially the **explicit formula**: $\sum_\rho 1/(\rho - 1/2)^{2m} = (\text{arch boundary term}) + (\text{prime sum})$. The Apex setting is the truncated, polynomial-tested version.

**(β)** Find a *different* decomposition where the antagonism is broken. Candidates:

- **Multi-prime / joint primorial.** At $N = 210$ the joint product has 48 L-functions. Each $L(\chi)$ has its own archimedean and prime parts, but the *cross-character* combinations at primorial scale generate non-trivial cancellation patterns. Specifically: $\sum_\chi L'_\chi/L_\chi$ at $s = 1/2$ may admit a structurally different split.
- **Real-Helmert decomposition (simplicial-native).** The radical clock $K_N = \mathbb{Q}(\sqrt{p} : p \le N)$ gives a different basis on the primorial multiplicative group. Could organize the prime side $\sum_n \Lambda(n)/n^s$ along Helmert axes, with each axis giving its own apex contribution. Antagonism may localize to one axis rather than infect the whole.
- **Operator-theoretic.** Construct the positive operator $L_\Xi$ in §16.3 directly without going through Hadamard atomization. The trace structure may produce positivity without the arch–prime split appearing at all.

**(γ)** Bound the cancellation directly. If the antagonism is exponential ($\eta_k \sim (\gamma_1^{-2}/4)^k$) and structural, there may be an analytical identity expressing the residual cancelled quantity as a manifestly positive object — without going through the antagonistic split.

## Consequences for the program

- **A1 (Pass-5 §17 audit + this probe) settled.** The §17 reformulation is sharp; the naive arch-domination attack is structurally barred. To attack §17.3, we must use **(α)**, **(β)**, or **(γ)** above.
- **A2 (extend N=6 closed-form theorem to general primorial)** becomes more valuable: it's a candidate route via **(β)** (multi-prime joint cumulants at primorial $N$).
- **A3 (Pass-8 Cesàro at all rungs)** is the natural route to **(α)** — the Cesàro identity is essentially the explicit formula in finite-jet form.
- **B1 (joint Li-type analytical proof)** remains the dream, but this probe shows it cannot reduce to Bombieri-Lagarias-style estimates without a new structural insight.

## Recommended next step

**Repeat this probe at the joint primorial scale $N = 210$.** Decompose $\Xi_{210}'(z)/\Xi_{210}(z)$ into character-by-character archimedean and prime parts. Check whether:

- Cross-character cancellation breaks the arch–prime antagonism in any sector.
- Some character's individual arch+prime is closer to PSD than ζ's was.
- The Helmert-orbital decomposition gives a positive cone for at least some sectors.

This is a 1–2 day computational task, and a clean positive result (a sector where Hankel is positive on one piece alone) would identify the simplicial program's distinctive lever for closing the gap.

## Files

- `probe_arch_prime_hankel.py` — numerical probe at mpmath dps=250, K through 30.
- `PassFive-Section17-Audit-Draft1.md` — companion audit of Pass-5 §17.

---

*This probe was designed to test whether Pass-5 §17's clean reformulation hides an accessible analytical proof. It does not. The split is exact but adversarial. The simplicial program's distinctive levers (joint primorial, Helmert decomposition) remain the most promising candidates for analytical progress.*
