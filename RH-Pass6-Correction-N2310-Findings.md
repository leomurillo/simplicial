# Pass-6 Correction: The N = 2310 Probe Reveals a Structural Issue

**Leonardo Murillo Montero + Codex**

*Working note - May 24, 2026*

## Headline

The N-scan from $N = 30 \to 210 \to 2310$ does **NOT** show the conjectured convergence of Born atoms to $\gamma_k^{-2}$. Instead:

\[
\text{Overshoot trajectory: } 1.47 \to 0.61 \to 0.054
\]

The atoms continue to shrink past 1 toward 0, even at high $T$. The conjectured asymptotic regime where $\lambda_{\max}^{(N,T)} \to \gamma_1^{-2}$ is **not realized in the simple joint limit**.

This contradicts Conjecture 6.2 from Pass-6 Draft 1 as initially stated, and forces a structural re-examination.

## The data at N = 2310

T-scan results:

| $T$ | $n_{pp}$ | $n_{\text{nonzero}}$ | trace | $c$ | $\lambda_{\max}$ | overshoot | worst $|\log_{10}|$ |
|---|---|---|---|---|---|---|---|
| 7 | 184 | 184 | 13.4 | 0.0359 | $1.35 \times 10^{-4}$ | 0.027 | 16.26 |
| 9 | 1,036 | 464 | 17.4 | 0.0314 | $2.12 \times 10^{-4}$ | 0.042 | 14.70 |
| 11 | 6,099 | 480 | 19.6 | 0.0296 | $1.95 \times 10^{-4}$ | 0.039 | 14.55 |
| 13 | 37,260 | 480 | 24.8 | 0.0263 | $2.46 \times 10^{-4}$ | 0.049 | 13.73 |
| 15 | 235,164 | 480 | 27.4 | 0.0251 | $2.70 \times 10^{-4}$ | 0.054 | 13.10 |

The atom magnitude *barely changes* as $T$ grows from 9 to 15 (saturates around $2 \times 10^{-4}$), suggesting prime-power-density is not the limiting factor.

## Diagnosis

### Why N=30, 210 looked like they were converging

In retrospect, the apparent convergence at small $N$ was **partly an artifact of calibration**. We forced $\sum_\psi \lambda_\psi = \ell_1$ by definition. With few atoms (7 at $N=30$, 47 at $N=210$), the largest atom ends up at $\sim \ell_1 / O(\text{characters})$, which happens to be in the same ballpark as $\gamma_1^{-2}$ for small character count.

The "crossover through 1" between $N=30$ and $N=210$ wasn't a convergence signal — it was just **trace conservation under increasing character count**.

### What the multiplicative apex actually encodes

The Dirichlet character coefficients $\widehat y_\psi$ encode partial sums of
\[
\sum_{n \le e^T} \chi(n) \Lambda(n) / \sqrt{n}
\]
which are related to $L'/L(\chi, 1/2)$-type evaluations, NOT to the Riemann zeros $\gamma_k$ directly.

Each Dirichlet character $\chi$ has its own L-function $L(\chi, s)$ with its own zero set $\{\gamma_k^\chi\}$. The sum $\sum_\psi |\widehat y_\psi|^2$ traces out information about the **joint spectrum of all Dirichlet L-functions mod $N$**, not just $\zeta$.

Reality check against known LMFDB data:
- $\zeta$: first zero at $\gamma_1 = 14.13$
- $L(\chi_3)$: first zero at $\gamma \approx 8.04$
- $L(\chi_4)$: first zero at $\gamma \approx 6.02$
- $L(\chi_5)$: various, all distinct from 14.13

If the multiplicative apex Born squares were tracking $(\gamma_1^\chi)^{-2}$ for each character $\chi$, we'd see a *spread* of atom values matching the spread of first L-function zeros. Empirically at $N=2310$ we see atoms tightly clustered around $2 \times 10^{-4}$ — neither matching $\gamma_1^{-2}$ for Riemann nor for individual Dirichlet L-functions.

### The most likely real interpretation

$|\widehat y_\psi|^2$ at finite $T$ approximates the squared partial L-derivative
\[
\left|\sum_{n \le e^T} \chi(n) \Lambda(n) / \sqrt{n}\right|^2 / \varphi(N).
\]

For non-trivial $\chi$, this partial sum has its own asymptotic behavior governed by $L'/L(\chi, s)$ near $s = 1/2$. It does NOT directly equal the sum over zeros of $L(\chi, s)$ — those would be obtained from a *different* test function in the explicit formula.

The Pass-5 Theorem 19.1 moment identity $\sum_\psi |\widehat y_\psi|^{2(n+1)} = \ell_{n+1}$ was a **hopeful conjecture, not a derived identity**. The N=2310 probe shows it does not hold for this candidate.

## What this means for the program

### (1) Pass-6 Draft 1 needs significant revision

The framing "multiplicative Dirichlet apex converges to folded $\xi$ cumulants" was overoptimistic. The empirical N=30, 210 partial successes were artifacts of small character count under trace calibration.

### (2) Pass-5 Theorem 19.1 status

Pass-5 Theorem 19.1 remains **conditional and unwitnessed**. Both the additive Pass-4 §5.1 candidate (ruled out earlier this session) and the multiplicative Dirichlet candidate (ruled out now) fail to satisfy the moment identity.

### (3) The Born-Helmert direct route as a whole

The simplest candidates derived from primorial prime sums do not give Born squares whose moments are $\ell_{n+1}$. Three possibilities remain:

**(R5) Use the trivial Dirichlet character.** The trivial character $\chi_0$ of $(\mathbb Z/N)^\times$ has $L(\chi_0, s) = \zeta(s) \prod_{p | N}(1 - p^{-s})$ — connected to $\zeta$ directly. But we excluded $\chi_0$ via centering. Reintroducing it via a different normalization might give a $\zeta$-specific candidate.

**(R6) Reweight by L-function zero density.** Instead of using flat weights $1/\sqrt{p^k}$, use weights that encode the spectral measure of each L-function. This would essentially be assuming the answer — but maybe makes the construction circular but valid.

**(R7) Heat-flow Born realization (P2 from before).** Pass-4 §4 heat-smoothed kernel gives positive Born factorization unconditionally for $t > \Lambda$. The de Bruijn-Newman boundary is unavoidable, but at least the construction works at every $t > 0$.

**(R8) Abandon Born-Helmert direct entirely.** Pursue Pass-5 Apex No-Isolator (§17.3) via prime/gamma split, or Bures Herglotz route via de Branges.

### (4) The transfer matrix work stays unconditional

The Helmert-Fourier transfer matrix closed form (T4 Conjecture 2) and its multiplicative analog are still valid mathematical results independent of the Born-Helmert moment-match question. They are tools, not assertions about RH.

## Honest accounting

What the session **did** establish:

- ✅ T4 Conjecture 2 (additive transfer matrix closed form): solved
- ✅ Pass-4 §5.1 additive primorial ledger: ruled out as Pass-5 Theorem 19.1 witness
- ✅ Multiplicative Dirichlet apex at fixed $N \in \{30, 210\}$ with $T = 7$: partial moment match
- ✅ Multiplicative apex at $N = 2310$: **revealed structural failure of the moment identity**

What the session **did NOT** establish:

- ❌ Born-Helmert moment identity at any $(N, T)$ with primorial-prime candidate
- ❌ Convergent asymptotic regime for the multiplicative apex (Conjecture 6.2)
- ❌ Closure of Pass-5 Theorem 19.1 via primorial constructions

What the session **revealed**:

- 🔍 The naive primorial primes-only ledger is NOT the right object for Pass-5 Theorem 19.1, in either additive or multiplicative form.
- 🔍 The multiplicative apex traces a sum-over-L-functions spectral object, not $\zeta$-specific cumulants.
- 🔍 The Born-Helmert direct route, as currently formulated, may require a fundamentally different candidate construction (R5–R8 above).

## Recommendation

**Pause on the Born-Helmert direct route** until a candidate ledger is identified that has a principled connection to $\zeta$-only spectrum (not the joint L-function spectrum).

**Pursue Pass-5 §17.3 Apex No-Isolator** via the prime/gamma split (R8 partial) — that route doesn't depend on a Born ledger candidate; it works directly with the cumulant ledger.

**Maintain T4 Helmert-Fourier transfer matrix machinery** as a valid result.

**Pass-6 Draft 1 should be replaced** with a more careful documentation of what the multiplicative apex actually encodes (joint Dirichlet L-function content) and why it does NOT directly give RH cumulants.

## What I should have caught earlier

The growth rate at N=2310 ($\sim 1/\varphi(N)$ at fixed $T$) is consistent with **trace conservation across more characters**, not convergence to a fixed spectrum. I should have predicted this from N=30 to N=210 (factor 6 in $\varphi$, factor $\sim 2.4$ in atom magnitude — close to $\sqrt{6}$ suggesting per-character variance going as $1/\varphi(N)$).

Pre-committing to Conjecture 6.2 (overshoot → 1) was overoptimistic without theoretical justification. The empirical match at N=30 and N=210 should have been suspected as coincidence given the small character count and unprincipled calibration.

This is a real lesson about pre-committed criteria: they protect against confirmation bias only if applied to predictions that have theoretical backing, not to hopeful pattern-matching.

## Files this session (corrected status)

- `T4-HelmertFourierTransferMatrix-WorkedExample-Draft1.md` ✓ valid
- `probe_born_helmert_*.py` (R1 probes) ✓ valid (additive ruled out)
- `probe_R1_findings.md` ✓ valid
- `probe_dirichlet_apex_N30.py` ✓ valid (data correct, interpretation revised)
- `probe_dirichlet_calibration.py` ✓ valid (calibration is empirical fact)
- `probe_dirichlet_T_scan_N30.py` ✓ valid (oscillation finding correct)
- `probe_dirichlet_N210.py` ✓ valid (data correct, interpretation revised)
- `probe_dirichlet_N2310.py` ✓ valid (this is the revealing probe)
- `probe_dirichlet_N2310_T_scan.py` ✓ valid (confirms saturation)
- `P1-MultiplicativeDirichletApex-WorkedExample-Draft1.md` ⚠ needs revision
- `RH-Pass6-MultiplicativeDirichletConvergence-Draft1.md` ⚠ needs revision

## Closing line

The Pass-5 Theorem 19.1 moment identity is **harder to witness than this session's probes suggested**. The multiplicative Dirichlet apex is the *right shape of object* but its connection to $\ell_n$ requires a $\zeta$-specific projection that we have not constructed.

Honest assessment: the session produced one unconditional theorem (transfer matrix closed form), conclusively ruled out two candidate ledgers (additive prime sum, multiplicative Dirichlet prime sum), and clarified the structural reason both fail. That is real progress, but it is **not progress toward closing Pass-5**; it is progress in understanding what the candidate cannot be.

The team should know.
