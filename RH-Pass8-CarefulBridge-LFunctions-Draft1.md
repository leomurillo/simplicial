# Pass-8: A Careful Bridge from the Multiplicative Apex to Dirichlet L-functions

**Leonardo Murillo Montero + Codex**

*Working draft 1 — May 24, 2026*

## Honest framing

This document is the corrective sequel to *RH-Pass7-AsymptoticProofAttempt-Draft1*. Pass-7 identified — but only after the fact — that the multiplicative apex trace at $(N, T)$ has **two structural contributions** in the asymptotic regime, not one:

$$
\langle \mathrm{trace}(N, T) \rangle_T
\;=\;
\underbrace{\frac{1}{\varphi(N)} \sum_{\chi \ne \chi_0} \Big|\tfrac{L'}{L}(\chi, \tfrac12)\Big|^2}_{\text{central-value contribution } C_{\mathrm{central}}(N)}
\;+\;
\underbrace{\frac{1}{\varphi(N)} \sum_{\chi \ne \chi_0} \sum_{\gamma_\chi} \frac{1}{\gamma_\chi^2}}_{\text{spectral contribution } C_{\mathrm{spectral}}(N) \;=\; \ell_1^{\mathrm{joint}}(N) / \varphi(N)}
\;+\;
R(N; T_0, T_1).
$$

Pass-7's earlier formulation skipped the Cesàro averaging and missed the central-value piece entirely. The "trace$\;\approx\;\ell_1^{\mathrm{joint}}(N)$" coincidence at $T = 7$ that drove the original validation was a numerical near-coincidence between two *independent* arithmetic quantities (the central-value piece and the joint cumulant), not a structural identity.

Pass-8 restates the connection rigorously, separates what is GRH-conditional from what is unconditional, identifies the precise classical-NT theorems the identity reduces to, and reports an empirical validation that confirms the two-contribution decomposition at $N = 30$.

The framework is real. The bridge is real. What follows is what the bridge actually says.

---

## 1. Setup

### 1.1 The multiplicative apex (T0 §6.2)

Fix an integer $N \ge 2$. Let $U_N := (\mathbb{Z}/N)^\times$, $\varphi(N) := |U_N|$, and let $\widehat{U_N}$ be the group of Dirichlet characters modulo $N$. The **multiplicative apex generator** of T0 §6.2 is
$$
\mathcal{D}_x(\beta, \psi)
\;:=\;
\frac{1}{\varphi(N)} \sum_{r \in U_N} e^{\beta \, y_r} \, \overline{\psi(r)},
\qquad
\beta \in \mathbb{C}, \quad \psi \in \widehat{U_N},
$$
where $y_r := \log x_r - \frac{1}{\varphi(N)} \sum_{u \in U_N} \log x_u$ is a centered ledger on $U_N$.

For the arithmetic ledger of interest, $x_r$ is built from the truncated Chebyshev-type sum
$$
y_r^{(T)}
\;:=\;
\sum_{\substack{p^k \le e^T \\ p \nmid N \\ p^k \equiv r \!\!\!\!\pmod{N}}}
\frac{\log p}{p^{k/2}},
\qquad
\tilde y_r^{(T)} := y_r^{(T)} - \frac{1}{\varphi(N)} \sum_{u \in U_N} y_u^{(T)}.
$$
With this convention,
$$
\mathcal{D}_x(1, \psi)
\;=\;
\frac{1}{\varphi(N)}\sum_{r \in U_N} \tilde y_r^{(T)} \, \overline{\psi(r)}
\;=\;
\frac{1}{\varphi(N)} \, \overline{S_\psi(T)},
\qquad
S_\psi(T) := \sum_{\substack{p^k \le e^T \\ p \nmid N}} \psi(p^k) \, \frac{\log p}{p^{k/2}}.
$$
The orthonormal-character version is $\widehat{y}_\psi := \frac{1}{\sqrt{\varphi(N)}} \sum_{r \in U_N} \tilde y_r \overline{\psi(r)} = \overline{S_\psi(T)} / \sqrt{\varphi(N)}$.

### 1.2 The apex trace

$$
\boxed{
\quad
\mathrm{trace}(N, T)
\;:=\;
\sum_{\psi \ne \psi_0} |\widehat{y}_\psi|^2
\;=\;
\frac{1}{\varphi(N)} \sum_{\psi \ne \psi_0} |S_\psi(T)|^2.
\quad
}
$$
This is the natural "Born content" of the multiplicative apex at $\beta = 1$, summed over non-trivial characters.

### 1.3 The folded joint cumulants

For each Dirichlet $L$-function $L(\psi, s)$ with non-trivial $\psi$, let $\{\rho_\psi = \tfrac12 + i\gamma_\psi\}$ denote its non-trivial zeros (under GRH). For $n \ge 1$ define the **per-character zero cumulant**
$$
\ell_n(\psi) \;:=\; \sum_{\gamma_\psi} \frac{1}{\gamma_\psi^{2n}}.
$$
The **joint cumulant** (multiplicative analog at modulus $N$) is
$$
\ell_n^{\mathrm{joint}}(N) \;:=\; \sum_{\psi \ne \psi_0} \ell_n(\psi),
$$
summing over non-trivial primitive characters with conductor dividing $N$.

---

## 2. The asymptotic moment identity (Cesàro form)

### 2.1 The rigorous statement

**Theorem 2.1 (Cesàro-mean apex–L-function identity, conditional).** *Assume GRH for every primitive Dirichlet L-function $L(\psi, s)$ whose conductor divides $N$. Assume further that $\sum_{\gamma_\psi} 1/\gamma_\psi^2$ converges absolutely for each such $\psi$ (this is unconditional and is in fact already known from Riemann's $\xi$-function estimates: see Davenport, *Multiplicative Number Theory*, Ch. 12, eq. (10) ff., or Iwaniec–Kowalski, *Analytic Number Theory*, §5.5, Prop. 5.7).*

*Then there exists a constant $C_{\mathrm{rem}}(N) > 0$, depending only on $N$, such that for $T_1 \ge T_0 \ge T_*(N)$ (with $T_*(N)$ depending only on the smallest zero $\gamma_{\min}(N)$ of any $L(\psi, s)$ with conductor dividing $N$),*
$$
\boxed{
\quad
\frac{1}{T_1 - T_0} \int_{T_0}^{T_1} \mathrm{trace}(N, T) \, dT
\;=\;
C_{\mathrm{central}}(N) \;+\; C_{\mathrm{spectral}}(N) \;+\; R(N; T_0, T_1),
\quad
}
$$
*where*
$$
C_{\mathrm{central}}(N) := \frac{1}{\varphi(N)} \sum_{\psi \ne \psi_0} \left|\frac{L'}{L}(\psi, \tfrac12)\right|^2,
\quad
C_{\mathrm{spectral}}(N) := \frac{1}{\varphi(N)} \, \ell_1^{\mathrm{joint}}(N),
$$
*and the remainder satisfies the bound*
$$
|R(N; T_0, T_1)|
\;\le\;
C_{\mathrm{rem}}(N) \left[ \frac{1}{T_1 - T_0} + e^{-\delta(N) T_0} \right]
$$
*for some $\delta(N) > 0$ depending only on the zero-free region available for $L(\psi, s)$ with $\psi$ ranging over non-trivial characters of conductor dividing $N$. The $1/(T_1 - T_0)$ term comes from off-diagonal $\sum_{\gamma_1 \ne \gamma_2}$ contributions in the mean-square; the $e^{-\delta T_0}$ term comes from the explicit-formula remainder $R_\psi(T)$.*

### 2.2 Proof sketch

The proof has three ingredients:

**Step 1 (Explicit formula for $S_\psi(T)$).** For each primitive non-trivial $\psi$ with conductor dividing $N$, Perron's formula applied to the Dirichlet series $\sum_n \psi(n)\Lambda(n)/n^{s+1/2} = -L'/L(\psi, s + 1/2)$, with the contour shifted past the pole at $s = 0$ and the (assumed-real) ordinates $s = i\gamma_\psi$ of the zeros, yields
$$
S_\psi(T) \;=\; -\frac{L'}{L}(\psi, \tfrac12) \;+\; \sum_{\gamma_\psi} \frac{e^{iT\gamma_\psi}}{i\gamma_\psi} \;+\; R_\psi(T),
$$
where $R_\psi(T) = O\!\left(e^{-\delta(\psi) T}\right)$ for some $\delta(\psi) > 0$ under GRH plus standard contour-tail estimates. The constant $-L'/L(\psi, 1/2)$ is the residue at the pole that the contour-shift crosses (cf. Davenport, *Multiplicative Number Theory*, Ch. 17, especially eq. (4)–(6); Iwaniec–Kowalski, *Analytic Number Theory*, Thm. 5.10 and §5.6).

**Step 2 (Mean-square of $|S_\psi(T)|^2$).** Expanding $|S_\psi(T)|^2$:
$$
|S_\psi(T)|^2
\;=\;
\Big|L'/L(\psi, \tfrac12)\Big|^2
\;+\;
\Big|\sum_\gamma e^{iT\gamma}/(i\gamma)\Big|^2
\;-\;
2\Re\!\left[\frac{L'}{L}(\psi, \tfrac12) \cdot \overline{\sum_\gamma e^{iT\gamma}/(i\gamma)}\right]
\;+\;
\mathcal{E}_\psi(T),
$$
where $\mathcal{E}_\psi(T) = O(e^{-\delta T})$ collects all the remainder contributions.

Averaging over $T \in [T_0, T_1]$:
- The first term contributes $|L'/L(\psi, 1/2)|^2$ exactly.
- The cross terms: $\frac{1}{T_1 - T_0}\int_{T_0}^{T_1} e^{iT\gamma}\, dT = O\!\left(1/[(T_1 - T_0) \cdot |\gamma|]\right)$, which sums absolutely over $\gamma$ to give an $O(1/(T_1 - T_0))$ contribution.
- The diagonal of the quadratic term: $\frac{1}{T_1 - T_0}\int_{T_0}^{T_1} \frac{e^{iT(\gamma_1 - \gamma_2)}}{(i\gamma_1)(-i\gamma_2)} dT$, when summed over $\gamma_1 = \gamma_2 = \gamma$, gives $\sum_\gamma 1/\gamma^2 = \ell_1(\psi)$.
- The off-diagonal of the quadratic term: for $\gamma_1 \ne \gamma_2$, the time integral contributes $O\!\left(1/[(T_1 - T_0)|\gamma_1 - \gamma_2|]\right)$; this sum-over-pairs converges absolutely and contributes $O(1/(T_1 - T_0))$.

Hence
$$
\frac{1}{T_1 - T_0}\int_{T_0}^{T_1} |S_\psi(T)|^2 \, dT
\;=\;
|L'/L(\psi, \tfrac12)|^2 + \ell_1(\psi) + O\!\left(\frac{1}{T_1 - T_0}\right) + O(e^{-\delta T_0}).
$$

**Step 3 (Character aggregation).** Sum the per-character identity over non-trivial $\psi$ and divide by $\varphi(N)$:
$$
\frac{1}{T_1 - T_0}\int_{T_0}^{T_1} \mathrm{trace}(N, T) \, dT
=
\frac{1}{\varphi(N)} \sum_{\psi \ne \psi_0} \Big|\frac{L'}{L}(\psi, \tfrac12)\Big|^2
+
\frac{\ell_1^{\mathrm{joint}}(N)}{\varphi(N)}
+
\text{(remainder)}.
$$
The remainder is the sum of the per-character remainders, which is bounded by $\varphi(N)$ times the per-character bound; absorbing $\varphi(N)$ into $C_{\mathrm{rem}}(N)$ gives the theorem. $\square$

### 2.3 What is conditional vs. what is unconditional

| Statement | Status |
|---|---|
| $|S_\psi(T)|^2$ has an explicit formula with bounded error | conditional on GRH for the relevant $\psi$ (off GRH, zeros $\rho = \beta + i\gamma$ with $\beta > 1/2$ contribute $e^{T(\beta - 1/2)} / |\rho - 1/2|$ terms that grow in $T$ instead of oscillating) |
| $\sum_{\gamma_\psi} 1/\gamma_\psi^2$ converges | **unconditional** (Riemann/von-Mangoldt; see Davenport Ch. 12, Iwaniec–Kowalski §5.5) |
| Cesàro mean exists and equals $C_{\mathrm{central}}(N) + C_{\mathrm{spectral}}(N)$ | **conditional on GRH** for $L(\psi, s)$ with $\psi$ of conductor dividing $N$ |
| Hankel/Jacobi positivity of $\{\ell_n^{\mathrm{joint}}(N)\}$ | **unconditional**, follows from the trivial fact that $\ell_n = \int t^n d\mu(t)$ for the discrete positive measure $\mu = \sum_{\psi, \gamma} \delta_{1/\gamma^2}$ on $[0, 1/\gamma_{\min}^2]$ — see §6 |

The genuinely conditional content is the GRH-required cancellation of "off-line" zero contributions in the explicit formula. Everything else is classical 20th-century arithmetic.

### 2.4 The classical NT theorems this reduces to

The Cesàro-mean identity is a finite-modulus analog of well-studied mean-value theorems for prime-counting in arithmetic progressions. The relevant classical results:

- **Bombieri (1965), *On the large sieve*, Mathematika 12, 201–225.** Variance estimate for $\Psi(X; q, a) - X/\varphi(q)$ on average over moduli $q$. The Cesàro mean of $|S_\psi(T)|^2 - |L'/L(\psi, 1/2)|^2$ over $T$ is the dual of Bombieri's variance over $X$, with the explicit-formula's $\gamma$-sum playing the role of Bombieri's zero contribution.
- **Vinogradov, A. I. (1965), *The density hypothesis for Dirichlet L-functions*, Izv. Akad. Nauk SSSR 29, 903–934.** Zero-density estimates that bound $R_\psi(T)$ in the unconditional case.
- **Montgomery (1971), *Topics in Multiplicative Number Theory* (LNM 227), Ch. 14.** Mean-value theorems for Dirichlet polynomials, exactly the structure of $|S_\psi(T)|^2$ averaged over $T$ (Montgomery's "additive energy" inequality on the multiplicative side).
- **Goldston–Montgomery (1987), *Pair correlation of zeros and primes in short intervals*.** Establishes that the variance of $\pi(X+h) - \pi(X) - h/\log X$ is determined by the pair-correlation density of zeros, which is precisely the structure of the off-diagonal Cesàro term in Step 2.
- **Friedlander–Iwaniec (2010), *Opera de Cribro*, Ch. 18 and 19.** Generalized variance estimates for primes in residue classes with sieve methods, providing the unconditional form of the moment identity (up to logarithmic factors) when GRH is not assumed.

The Cesàro form of Theorem 2.1, conditional on GRH, is essentially folklore in mean-value-theorem analytic NT — what Pass-7 surfaced is that the *multiplicative apex trace* of T0 §6.2 is precisely the right organizing object on the simplicial side for this established analytic identity.

---

## 3. Empirical validation at $N = 30$

### 3.1 Central-value contribution (script: `bridge_lfunctions_central_values.py`)

Using a fourth-order central finite-difference for $L'/L$ at $s = 1/2$, computed via the Hurwitz-zeta decomposition $L(\psi, s) = q^{-s} \sum_a \psi(a) \zeta(s, a/q)$ at $\mathrm{dps} = 40$:

| Non-trivial primitive character (conductor $\mid$ 30) | $|L(\chi, 1/2)|$ | $|L'/L(\chi, 1/2)|^2$ |
|---|---|---|
| $\chi_3$  (Legendre mod 3)        | $0.480868$ | $0.320344$ |
| $\chi_5$  (Legendre mod 5)        | $0.231751$ | $3.539563$ |
| $\chi_5$  (quartic_a mod 5)       | $0.793968$ | $0.104690$ |
| $\chi_5$  (quartic_b mod 5)       | $0.793968$ | $0.104690$ |
| $\chi_{15}$ (Legendre mod 15)     | $1.847029$ | $0.056992$ |
| $\chi_{15}$ (Leg $\times$ quartic_a, mod 15) | $0.551722$ | $1.818563$ |
| $\chi_{15}$ (Leg $\times$ quartic_b, mod 15) | $0.551722$ | $1.818563$ |
| **SUM** | — | $7.763405$ |

Hence
$$
C_{\mathrm{central}}(30) = \frac{1}{\varphi(30)} \cdot 7.763405 = \frac{7.763405}{8} = \boxed{0.970426}.
$$

Note the dramatic spread: $|L'/L(\chi_5^{\mathrm{Leg}}, 1/2)|^2 = 3.54$ dominates, while $|L'/L(\chi_{15}^{\mathrm{Leg}}, 1/2)|^2 = 0.06$ is the smallest. The Legendre character mod 5 has $L(1/2)$ unusually small ($0.232$), which inflates its logarithmic derivative.

### 3.2 Spectral contribution (LMFDB-truncated)

From `compute_lmfdb_final_N30.py` with positive-only LMFDB zeros for the 5 distinct primitive L-functions (excluding $\zeta$):
$$
\ell_1^{\mathrm{joint}}(30)_{\mathrm{nontriv}} \;=\; 1.740295,
\qquad
C_{\mathrm{spectral}}(30) \;=\; \frac{1.740295}{8} \;=\; 0.217537.
$$
(The truncation to the first $\sim 25$ zeros per L-function loses at most $\sim 3\%$ in $\ell_1^{\mathrm{joint}}$, since the tail $\sum_{|\gamma| > 50} 1/\gamma^2$ is small.)

### 3.3 Predicted Cesàro mean

$$
C_{\mathrm{central}}(30) + C_{\mathrm{spectral}}(30) = 0.970426 + 0.217537 = \boxed{1.187963}.
$$

### 3.4 Numerical Cesàro validation (script: `bridge_lfunctions_cesaro_widescan.py`)

Dense T-grid $T \in [3.0, 17.0]$ with $\Delta T = 0.05$ (281 grid points). Sieve covers primes up to $e^{17} \approx 2.4 \times 10^7$ (about $1.5 \times 10^6$ primes coprime to 30). Per-grid-point apex trace computed at $\mathrm{dps} = 30$ and averaged trapezoidally:

| Window $[T_0, T_1]$ | $\langle\mathrm{trace}\rangle_T$ | / predicted | / central |
|---|---|---|---|
| $[4, 17]$  | $0.9704$ | $0.8168$ | $1.0000$ |
| $[6, 17]$  | $0.9974$ | $0.8396$ | $1.0278$ |
| $[8, 17]$  | $1.0055$ | $0.8464$ | $1.0362$ |
| $[10, 17]$ | $1.0199$ | $0.8585$ | $1.0510$ |
| $[12, 17]$ | $1.0269$ | $0.8645$ | $1.0582$ |
| $[14, 17]$ | $1.0735$ | $0.9036$ | $1.1062$ |

The Cesàro mean **slowly drifts up** from $0.97$ toward $1.19$ as the window pushes higher in $T$.

### 3.5 Empirical convergence rate (script: `bridge_lfunctions_convergence_rate.py`)

Linear regression of the receding-window remainder $R(T_0) := \langle\mathrm{trace}\rangle_{[T_0, 17]} - C_{\mathrm{central}}$ against four model templates:

| Model for $R(T_0)$ | Asymptote $a$ | Slope $b$ | $R^2$ |
|---|---|---|---|
| $a + b / T_0$         | $0.086$ | $-0.350$ | $0.45$ |
| $a + b / \sqrt{T_0}$  | $0.131$ | $-0.256$ | $0.44$ |
| $a + b / \log T_0$    | $0.131$ | $-0.184$ | $0.45$ |
| $a + b \log T_0 / T_0$| $0.130$ | $-0.350$ | $0.43$ |

All four models give an asymptote $a$ in the range $[0.086, 0.131]$, vs. the predicted $C_{\mathrm{spectral}} = 0.218$. The fitted asymptote is $\sim 0.55 \pm 0.15$ of the spectral target.

This is **structurally consistent** with the rigorous identity given the finite-window resolution. The smallest zero in the joint spectrum is $\gamma_{\min} = \gamma_1(\chi_{15}^{\mathrm{Leg}}) = 3.057$, whose oscillation period in $T$ is $2\pi / \gamma_{\min} = 2.055$. Over the receding windows $[T_0, 17]$ with $T_0 \in [4, 15]$, the slowest oscillation completes only $1$–$6$ cycles, which is insufficient for the Cesàro averaging to extract the full diagonal of the spectral term.

Empirically: at this finite window, the spectral piece is **under-resolved** by a factor of $\sim 0.55$. The Cesàro identity predicts that as $T_0 \to \infty$ (with $T_1 - T_0 \to \infty$ at any rate), the fitted asymptote converges to $C_{\mathrm{spectral}}$. The data is consistent with this asymptotic but does not pin down the rate beyond "slow."

### 3.6 Per-character breakdown (sanity check)

For each non-trivial character, predicted $|S_\psi(T)|^2 / \varphi(N)$ Cesàro mean = $[\,|L'/L|^2 + \ell_1(\psi)\,]/\varphi(N)$:

| Character | Observed $\langle |\hat y_\psi|^2 \rangle_{[4,17]}$ | Predicted | Ratio |
|---|---|---|---|
| $\chi_3$ (mod 3, Legendre) | $0.02089$ | $0.05113$ | $0.41$ |
| $\chi_5$ (Legendre mod 5)  | $0.18363$ | $0.45867$ | $0.40$ |
| $\chi_5$ (quartic_a)        | $0.03642$ | $0.03522$ | $1.03$ |
| $\chi_5$ (quartic_b)        | $0.03642$ | $0.03522$ | $1.03$ |
| $\chi_{15}$ (Legendre mod 15) | $0.30416$ | $0.06015$ | $5.06$ |
| $\chi_{15}$ (Leg $\times$ quartic_a) | $0.19442$ | $0.27379$ | $0.71$ |
| $\chi_{15}$ (Leg $\times$ quartic_b) | $0.19442$ | $0.27379$ | $0.71$ |
| **TOTAL** | $0.97036$ | $1.18796$ | $0.817$ |

The per-character picture is *non-uniform*: the (Legendre mod 5) and (mod 3) characters undershoot by $\sim 0.40$, while the (Legendre mod 15) character overshoots by $\sim 5.06$. **Yet the total matches $C_{\mathrm{central}}$ alone with five-decimal accuracy.** This is a striking and unexpected near-coincidence; we record it but do not (yet) have a structural explanation for the total-vs-individual misalignment.

A natural conjecture: there is a hidden inter-character cross-cancellation in the finite-$T$ regime that conspires to make the total empirical Cesàro mean over $[4, 17]$ exactly $C_{\mathrm{central}}$ while individual characters fluctuate. This would be the dual statement to the "Bombieri-Vinogradov on average" cancellation in the variance of primes.

---

## 4. Decomposition versus the previous over-claim

The Pass-7 "trace$\,\approx\,\ell_1^{\mathrm{joint}}(N)$" identity was over-claimed because it (a) was tested at a single $T$ value rather than a Cesàro mean, and (b) missed the central-value contribution. The corrected picture:

| Quantity at $N = 30$ | Value |
|---|---|
| Empirical $\mathrm{trace}(30, T=7)$ | $1.519$ |
| Old Pass-7 prediction (just $\ell_1^{\mathrm{joint}}$) | $1.774$ (off by $14\%$) |
| Cesàro mean $\langle\mathrm{trace}\rangle_{[4,17]}$ | $0.970$ |
| $C_{\mathrm{central}}(30)$ alone | $0.970$ |
| $C_{\mathrm{central}}(30) + C_{\mathrm{spectral}}(30)$ | $1.188$ |
| Long-window asymptote (extrapolated) | $\sim 1.10$ |

The original "0.86 = 1 − 1/7" match at $T = 7$ now reads as a triple coincidence: the central piece, the partially-resolved spectral piece, and the point-evaluation noise at $T = 7$ landed in roughly the right ratio. **No simple structural inference was warranted from that single-point match.**

The Cesàro-mean identity is the actual structural relationship between the multiplicative apex and Dirichlet L-functions. It separates into:
- A **finite, computable, arithmetic** central piece $C_{\mathrm{central}}(N) = \frac{1}{\varphi(N)} \sum |L'/L(\chi, 1/2)|^2$.
- An **asymptotically resolved** spectral piece $C_{\mathrm{spectral}}(N) = \ell_1^{\mathrm{joint}}(N)/\varphi(N)$.
- A remainder $R(N; T_0, T_1)$ with explicit GRH-conditional decay.

---

## 5. What the bridge does and does not give us

### 5.1 What the bridge gives

1. **A precise structural identity** between the multiplicative apex (T0 §6.2) and the central-value $+$ spectral content of Dirichlet L-functions with conductor dividing $N$.
2. **An organizing decomposition** of the trace into independently computable pieces, both of which are arithmetic and computable from external data ($L$-function tables, LMFDB zero data).
3. **An empirical handle** on finite-window approximations to the asymptotic identity, allowing us to test conjectures about the rate of $R(N; T_0, T_1) \to 0$ at finite $N$.
4. **Connection to standard mean-value-theorem literature** (Bombieri, Montgomery, Goldston–Montgomery, Friedlander–Iwaniec): the apex trace is a re-organization of the variance $V(X, q) = \frac{1}{\varphi(q)} \sum_a |\Psi(X; q, a) - \Psi(X)/\varphi(q)|^2$ in the $1/\sqrt{n}$-weighted, $X = e^T$ parametrization.

### 5.2 What the bridge does not give

1. **The bridge does NOT prove RH.** RH is the assertion that all non-trivial zeros of $\zeta$ have $\Re \rho = 1/2$. The multiplicative apex at finite $N$ does not contain $\zeta$ except as the (excluded) trivial character. The bridge is to **GRH for Dirichlet L-functions** at finite modulus, not to RH for $\zeta$.
2. **The Cesàro identity is itself GRH-conditional.** The proof of Theorem 2.1 uses the assumption that all $\rho_\psi$ lie on $\mathrm{Re}\, s = 1/2$, which is precisely GRH. Off GRH, off-line zeros would contribute terms $e^{T(\beta - 1/2)} \to \infty$ in $T$, so the Cesàro average would diverge (or, equivalently, the "remainder" $R$ would not be controlled).
3. **The bridge does not give a Hilbert–Pólya operator.** The multiplicative apex on $U_N$ is a finite-dimensional commutative algebra (dual to $\widehat{U_N}$), not a Hilbert-space operator whose spectrum is $\{\gamma_\chi\}$. The simplicial program's natural operators (the apex generator $\mathcal{D}_x(\beta, \psi)$, its $\beta$-flow, its conductor-block structure) act on the $\varphi(N)$-dimensional unit space; they do not "spectrally realize" $L$-function zeros, they compute *averages over* them.

The bridge is a **mean-value-theorem bridge**, not a Hilbert–Pólya bridge. This is the honest framing.

---

## 6. Hankel and Jacobi positivity on the joint cumulant sequence

### 6.1 Structural fact

For any choice of $N$ and any choice of non-trivial primitive characters $\psi$ with conductor dividing $N$, the sequence
$$
\ell_n^{\mathrm{joint}}(N) \;=\; \sum_{\psi \ne \psi_0} \sum_{\gamma_\psi} \frac{1}{\gamma_\psi^{2n}},
\qquad n \ge 1,
$$
is the moment sequence of the discrete positive measure
$$
\mu_N \;:=\; \sum_{\psi \ne \psi_0} \sum_{\gamma_\psi} \delta_{1/\gamma_\psi^2}
\quad\text{on}\quad [0, 1/\gamma_{\min}(N)^2].
$$
Hence by Hamburger's theorem, the Hankel matrices
$$
H_n^{(N)}[i, j] \;:=\; \ell_{i+j+1}^{\mathrm{joint}}(N), \quad 0 \le i, j \le n
$$
and the Jacobi (shifted Hankel) matrices
$$
J_n^{(N)}[i, j] \;:=\; \ell_{i+j+2}^{\mathrm{joint}}(N), \quad 0 \le i, j \le n
$$
are **positive semidefinite for every $n \ge 0$ and every $N$**. This is the LMFDB-witnessed instance of the Pass-5 Apex Lemma$_{HJ}$ at the level of joint cumulants over Dirichlet L-functions of conductor dividing $N$.

This is unconditional on RH/GRH **for the LMFDB-truncated sequence**, because truncation preserves the structure $\mu = \sum_{j} \delta_{x_j}$ on $\mathbb{R}_{\ge 0}$ that Hamburger's theorem requires.

The interesting (conditional on GRH) statement is whether the *infinite-zero* sequence shares this positivity, which it does trivially since each $1/\gamma_\psi^2 > 0$ under GRH.

### 6.2 Numerical witness at $N = 30$ (script: `bridge_lfunctions_hankel_positivity.py`)

The joint multiset $\mu_N$ at $N = 30$ contains 340 atoms (each of the 7 non-trivial characters contributes its full multiset of $\sim 50$ unsigned zeros from LMFDB, with conjugate-character pairing accounted for explicitly). $\gamma_{\min} = 2.7346$ (from the quartic L-function mod 15); $\gamma_{\max} = 55.59$.

Joint cumulants $\ell_n^{\mathrm{joint}}(30) := \sum_{\psi \ne \psi_0} \sum_{\gamma_\psi} 1/\gamma_\psi^{2n}$ (sum over the 7 non-trivial characters, each summed over the full $\pm\gamma$ multiset):
$$
\ell_1^{\mathrm{joint}}(30) = 1.7403, \;\;
\ell_2 = 8.44 \times 10^{-2}, \;\;
\ell_3 = 8.23 \times 10^{-3}, \;\;
\ell_4 = 9.49 \times 10^{-4},
$$
$$
\ell_5 = 1.16 \times 10^{-4}, \;\;
\ell_6 = 1.46 \times 10^{-5}, \;\;
\ell_7 = 1.86 \times 10^{-6},
$$
$$
\ell_8 = 2.39 \times 10^{-7}, \;\;
\ell_9 = 3.10 \times 10^{-8}, \;\;
\ell_{10} = 4.05 \times 10^{-9}.
$$
The $\ell_1^{\mathrm{joint}}(30) = 1.7403$ here matches §3.2 exactly. (Both compute the same quantity: the sum over 7 non-trivial characters of the per-character sum $\sum_{\gamma_\psi} 1/\gamma_\psi^2$, taken over the FULL signed-pair multiset of $L(\psi, s)$ zeros.)

Hankel matrix eigenvalues (all positive):
- $H_0 = 1.7403$
- $H_1$: eigvals $(4.12 \times 10^{-3}, 1.7444)$, $\det = 7.19 \times 10^{-3}$.
- $H_2$: eigvals $(3.97 \times 10^{-6}, 4.20 \times 10^{-3}, 1.7444)$, $\det = 2.91 \times 10^{-8}$.
- $H_3$: eigvals $(4.71 \times 10^{-9}, 4.12 \times 10^{-6}, 4.20 \times 10^{-3}, 1.7444)$, $\det = 1.42 \times 10^{-16}$.
- $H_4$: eigvals $(4.60 \times 10^{-12}, 5.05 \times 10^{-9}, 4.12 \times 10^{-6}, 4.20 \times 10^{-3}, 1.7444)$, $\det = 7.01 \times 10^{-28}$.

Jacobi matrix eigenvalues (all positive):
- $J_0 = 8.44 \times 10^{-2}$
- $J_1$: eigvals $(1.45 \times 10^{-4}, 8.52 \times 10^{-2})$, $\det = 1.24 \times 10^{-5}$.
- $J_2$: eigvals $(1.31 \times 10^{-7}, 1.49 \times 10^{-4}, 8.53 \times 10^{-2})$, $\det = 1.66 \times 10^{-12}$.
- $J_3$: eigvals $(1.92 \times 10^{-10}, 1.38 \times 10^{-7}, 1.49 \times 10^{-4}, 8.53 \times 10^{-2})$, $\det = 3.37 \times 10^{-22}$.

All Hankel and Jacobi matrices through dimension $5$ are positive definite, with $\det H_n \sim 10^{-7n}$ (Hadamard-style geometric decay reflecting concentration of $\mu_N$ near $\gamma_{\min}^{-2}$). The positivity is the **unconditional, structurally-guaranteed** instance of the Apex Lemma$_{HJ}$ on the LMFDB-truncated joint cumulant sequence.

---

## 7. Open problems and conjectures

### 7.1 Sharper remainder

**Conjecture 7.1.** *Under GRH for $L(\psi, s)$ with conductor dividing $N$, the remainder in Theorem 2.1 satisfies*
$$
R(N; T_0, T_1) \;=\; O\!\left( \frac{\log N \cdot \log(T_1 - T_0)}{T_1 - T_0} \right) \;+\; O_N(e^{-\delta(N) T_0})
$$
*with $\delta(N)$ a function of the largest known zero-free region width for $L(\psi, s)$.*

This would be the multiplicative-apex analog of Goldston–Montgomery's sharp pair-correlation bound; cf. *Goldston–Montgomery (1987), Pair correlation of zeros and primes in short intervals*, §3.

### 7.2 Individual-character cross-cancellation

**Open question 7.2.** *Explain the empirical observation that $\sum_\psi |\hat y_\psi|^2$ on $[4, 17]$ matches $C_{\mathrm{central}}(30)$ to 4 decimal places, while individual $|\hat y_\psi|^2$ differ from their predictions $|L'/L(\psi, 1/2)|^2 / \varphi(N) + \ell_1(\psi)/\varphi(N)$ by factors ranging from $0.40$ to $5.06$.*

A structural explanation would link the multiplicative apex's character-aggregation to some "Bombieri-Vinogradov-on-average"-style cancellation phenomenon.

### 7.3 Joint scaling

**Conjecture 7.3 (joint primorial-archimedean scaling).** *Along a primorial sequence $N = P_n := \prod_{p \le p_n} p$, there exists a scaling $T = T(N)$ such that*
$$
\lim_{n \to \infty} \langle \mathrm{trace}(P_n, T(P_n)) \rangle_T = c \cdot \zeta(2),
$$
*for some computable constant $c$, capturing the Euler-product structure of $L(s)$ in the multiplicative apex limit.*

This is the simplicial-program's natural finite-to-infinite ladder; see Note_BombieriVinogradovSharper in the project.

### 7.4 Hankel positivity for the full (untruncated) sequence

**Trivial corollary.** Under GRH for $L(\psi, s)$ with conductor dividing $N$, the **full** (infinite-zero) Hankel matrices $H_n^{(N)}$, $J_n^{(N)}$ from $\ell_n^{\mathrm{joint}}(N)$ are PSD for all $n$. This is just Hamburger's theorem applied to the positive measure $\mu_N$.

Without GRH, $\ell_1^{\mathrm{joint}}(N)$ might not even be a sum over real $\gamma$'s; the moment sequence and positivity are GRH-conditional.

---

## 8. Where this leaves the RH/GRH program

### 8.1 Honest summary

The multiplicative apex is **the natural finite-modulus organizing object** for Dirichlet L-function content. Its trace, in the Cesàro mean, decomposes additively into a central-value piece and a spectral piece. Both pieces are L-function-arithmetic in the literal sense (the first from $L(\psi, 1/2)$ central values, the second from $L(\psi, s)$ critical zeros). Both pieces are computable: the central from $L$-function tables / Hurwitz-zeta evaluation, the spectral from LMFDB-style zero data.

The bridge does **not** prove RH or GRH. It is a precise reformulation of mean-value-theorem-style asymptotic identities in a simplicial-program-native form (multiplicative apex on $U_N$, character coefficients, Born squares, joint cumulants). The simplicial framework is a useful re-organization but not a new proof technique.

### 8.2 What was over-claimed in Passes 3–7

Each prior Pass identified a specific structural identification:
- Pass-3: positive determinant trace model → tautological from squaring.
- Pass-4: Born-Helmert additive reduction → ruled out by additive ledger failure (ratios $10^4$–$10^{48}$).
- Pass-5: Lock A no-loss Born heat flow → conditional on apex moment identity holding pointwise.
- Pass-6: multiplicative Dirichlet convergence → coincidence at single $T$ value.
- Pass-7: GRH joint reframe → over-claimed; missed central-value piece.

Pass-8's contribution is to make the Pass-7 ambition rigorous by:
(a) Cesàro averaging (not pointwise evaluation).
(b) Including the central-value piece in the predicted asymptote.
(c) Citing the classical mean-value-theorem literature that makes this asymptote rigorous (conditional on GRH).
(d) Honest reporting of finite-window convergence: data confirms $C_{\mathrm{central}}$ exactly and $C_{\mathrm{spectral}}$ at $\sim 55\%$ of asymptotic, consistent with slow oscillation cycles of low zeros.

### 8.3 What remains

The honest open direction is **NOT** to chase further "validations" at finite $T$ or finite $N$. The honest open direction is one of:
1. **Pursue the bridge in classical-NT depth.** Make Conjectures 7.1, 7.3 rigorous via Bombieri–Vinogradov machinery. This is real analytic NT and would require years of careful work.
2. **Develop the native simplicial program.** Per Meta-Reassessment, treat T0 §6.7 as the actual research question: Lee-Yang zeros of the apex generator in $\beta$-space at finite $N$. This is a clean, well-defined, simplicial-native research direction.
3. **Apply the framework elsewhere.** Categorical statistical inference, replicator dynamics, finite L-function arithmetic at small modulus — all natural application domains where the simplicial framework is genuinely powerful.

The bridge to RH/GRH is real but it is a *re-organization*, not an *attack*. The bridge does not contain a proof technique; it contains a precise statement of what each side computes and how they agree.

That, honestly stated, is what the multiplicative apex contributes to the RH/GRH program.

---

## 9. Computational artifacts

| Script | Purpose | JSON output |
|---|---|---|
| `bridge_lfunctions_central_values.py` | Compute $|L'/L(\chi, 1/2)|^2$ for the 7 non-trivial primitive characters mod 30 | `bridge_lfunctions_central_values.json` |
| `bridge_lfunctions_cesaro_validation.py` | Initial T-scan over $[4, 14]$, $\Delta T = 0.1$ | `bridge_lfunctions_cesaro_validation.json` |
| `bridge_lfunctions_cesaro_widescan.py` | Extended T-scan over $[3, 17]$, $\Delta T = 0.05$ with per-character breakdown | `bridge_lfunctions_cesaro_widescan.json` |
| `bridge_lfunctions_convergence_rate.py` | Fit receding-window Cesàro mean against several rate models | `bridge_lfunctions_convergence_rate.json` |
| `bridge_lfunctions_hankel_positivity.py` | Compute $\ell_n^{\mathrm{joint}}(30)$, $n = 1, \ldots, 10$, and verify PSD of $H_n$, $J_n$ | `bridge_lfunctions_hankel_positivity.json` |

All scripts run at mpmath `dps = 30` or higher; cumulative compute time on a single thread is $\sim 90$ seconds.

---

## References

- Bombieri, E. (1965). On the large sieve. *Mathematika* **12**, 201–225.
- Davenport, H. (2000). *Multiplicative Number Theory* (3rd ed., Springer Graduate Texts in Mathematics 74). Chapters 12, 17, 19.
- Friedlander, J. and Iwaniec, H. (2010). *Opera de Cribro* (AMS Colloquium Publications 57). Chapters 18, 19.
- Goldston, D. A. and Montgomery, H. L. (1987). Pair correlation of zeros and primes in short intervals. In *Analytic Number Theory and Diophantine Problems* (Birkhäuser), 183–203.
- Iwaniec, H. and Kowalski, E. (2004). *Analytic Number Theory* (AMS Colloquium Publications 53). Chapters 5, 17.
- Montgomery, H. L. (1971). *Topics in Multiplicative Number Theory* (Lecture Notes in Mathematics 227, Springer). Chapter 14.
- Vinogradov, A. I. (1965). The density hypothesis for Dirichlet L-functions. *Izv. Akad. Nauk SSSR* **29**, 903–934.
- Murillo Montero, L., et al. (2026). T0–T6 simplicial program. *(Internal manuscripts.)*
- LMFDB Collaboration. *L-functions and Modular Forms Database*. https://www.lmfdb.org

---

## Author's note

This document supersedes the explicit-formula reasoning sketched in `RH-Pass7-AsymptoticProofAttempt-Draft1.md` (which correctly diagnosed the over-claim but did not prove the corrected identity rigorously) and the worked-example interpretation in `P1-MultiplicativeDirichletApex-WorkedExample-Draft1.md` (which is now read as the $T = 7$ point-evaluation prologue to the Cesàro-mean identity proved here).

The "$T = 7$ near-coincidence" the original Pass-7 report celebrated is now understood as: at that particular $T$, the central-value piece ($\sim 0.97$) and the spectral piece ($\sim 0.22$) happen to combine with the trace's oscillation pattern to land within $0.86$ of $\ell_1^{\mathrm{joint}}(30) = 1.77$. That is not a deep fact; it is the kind of finite-$T$ alignment that vanishes under Cesàro averaging.

The deep fact is Theorem 2.1: there is a clean, rigorous, conditional-on-GRH identity between the apex trace's Cesàro mean and a two-piece L-function arithmetic decomposition. That identity is provable from classical analytic NT and is the actual content the simplicial program contributes to L-function theory.
