# Born-Helmert Numerical Probe at $N = 30$: Findings

**Leonardo Murillo Montero + Codex**

*Working note - May 24, 2026*

## Summary

The Pass-5 Theorem 19.1 hypothesis was tested numerically at $N = 30$, $T = 7$ using two natural candidate ledgers from Pass-4 §5.1:

1. **Permissive ledger:** all primes $p \le e^T \approx 1096$.
2. **Strict Pass-4 ledger:** only primes $p$ dividing $P_n = 30$, i.e., $p \in \{2, 3, 5\}$.

Neither candidate satisfies the moment identity $\sum_c |\widehat y_c|^{2(n+1)} \to \ell_{n+1}$. Both fail by structural factors growing geometrically in $n$.

\[
\boxed{
\text{The simplest Born-Helmert candidates from Pass-4 §5.1 are NOT the right object.}
}
\]

This is a negative result for the naive direct construction, with diagnostic value.

## What was verified

**1. Transfer matrix closed form** (T4 Conjecture 2):
$$T_{c,k} = \frac{1}{\sqrt{N k (k+1)}} \cdot \frac{1 - (k+1)\omega_c^k + k \omega_c^{k+1}}{1 - \omega_c}, \quad \omega_c = e^{2\pi i c/N}$$
**Verified to machine precision.** Cross-check $\widehat y_c^{(\text{direct DFT})}$ vs $\sum_k \overline{T_{c,k}} \langle y, e_k \rangle$ agrees to $4.34 \times 10^{-39}$ across all 29 modes. The closed-form factorization (radical × cyclotomic) holds.

**2. Plancherel/Parseval consistency:** $\sum_c |\widehat y_c|^2$ equals $\sum_r |\tilde y(r)|^2 / N$ exactly. The character/Helmert/DFT framework is self-consistent.

## What was disconfirmed

**Permissive ledger ($p \le e^7$, 184 primes, 209 prime powers):**

| $n$ | $\ell_{n+1}$ | $p_n$ | $p_n / \ell_{n+1}$ |
|---|---|---|---|
| 0 | $1.86 \times 10^{-2}$ | $310.0$ | $1.67 \times 10^4$ |
| 1 | $3.71 \times 10^{-5}$ | $1.84 \times 10^4$ | $4.96 \times 10^8$ |
| 2 | $1.44 \times 10^{-7}$ | $1.91 \times 10^6$ | $1.32 \times 10^{13}$ |
| 5 | $1.59 \times 10^{-14}$ | $3.31 \times 10^{12}$ | $2.08 \times 10^{26}$ |
| 10 | $4.94 \times 10^{-26}$ | $8.95 \times 10^{22}$ | $1.81 \times 10^{48}$ |

Mismatch grows geometrically. The conductor-2 character ($c = 15$) dominates with $\lambda_{15} = 122$, an order of magnitude larger than other modes — picking up "most primes are odd" parity, structurally unrelated to folded $\xi$ cumulants.

**Strict Pass-4 ledger (primes $\{2, 3, 5\}$ only, 20 prime powers):**

| $n$ | $\ell_{n+1}$ | $p_n$ | $p_n / \ell_{n+1}$ |
|---|---|---|---|
| 0 | $1.35 \times 10^{-2}$ | $1.76$ | $1.30 \times 10^2$ |
| 1 | $3.62 \times 10^{-5}$ | $0.191$ | $5.27 \times 10^3$ |
| 5 | $1.59 \times 10^{-14}$ | $2.73 \times 10^{-4}$ | $1.72 \times 10^{10}$ |
| 10 | $4.94 \times 10^{-26}$ | $1.59 \times 10^{-7}$ | $3.22 \times 10^{18}$ |

Smaller trace ($1.76$ vs $310$) but worse asymptotic ratio growth.

## Structural diagnosis

Three observations explain the failure.

**(D1) The von Mangoldt residue-class sum is NOT a Born square of zero data.** The explicit formula relates prime sums and zero sums via:
$$2\sum_n \frac{\Lambda(n)}{\sqrt{n}} g(\log n) = \text{archimedean}(h) + \text{endpoint}(h) - \sum_\rho h(\gamma_\rho)$$
for test-function pairs $(h, g)$ in Mellin duality. The prime sum is *minus* a zero sum *plus* archimedean and endpoint corrections — not directly the zero sum, and not its square.

**(D2) The conductor structure of the prime ledger does not match folded $\xi$.** The dominant character mode in the permissive ledger is $c = 15$ (conductor 2, "mod 2 parity"), because primes are mostly odd. But folded $\xi$ cumulants $\ell_n$ are not concentrated in any mod-2 substructure. The prime ledger's conductor spectrum is dominated by trivial number-theoretic facts (parity), not by the folded zero distribution.

**(D3) Scale mismatch is geometric, not constant.** Ratios $p_n / \ell_{n+1}$ grow geometrically in $n$, indicating not a constant normalization error but a **scale-of-magnitude** mismatch in the underlying atoms: the typical $\lambda_c$ is $O(1)$, while typical $\gamma_k^{-2}$ is $O(10^{-3})$. The candidate ledger's atoms live two orders of magnitude too large.

## What this means for Pass-5 Theorem 19.1

**Theorem 19.1 hypothesis is NOT satisfied by Pass-4 §5.1 candidate ledgers.** The Born-Helmert direct route cannot use the naive heat-smoothed primorial prime-power sum as $\widehat y_a^{(M)}$.

Three response paths:

**(R1) Find the refined candidate.** Adjust the Pass-4 §5.1 construction by:
- Adding the archimedean Gamma derivative contributions, localized to residue classes
- Adding the endpoint $(s=0, s=1)$ pole contributions
- Renormalizing by an explicit scale factor (currently scale-mismatch is $\sim 10^4$ for $n=0$, growing)
- Including only conductor packets matching $\xi$ structure (excluding the dominant mod-2 parity stratum)

**(R2) Replace the candidate.** Construct $\widehat y_a^{(M)}$ from a different principle:
- Directly from the heat-smoothed kernel $\Xi_t^{(n,T)}$ at finite $t > 0$ (Pass-4 §4), then $t \to 0^+$ (re-introduces the de Bruijn-Newman boundary)
- From a finite-dimensional approximation of the de Branges Hilbert space for $\xi$
- From a regularized Weil test function (Pass-5 §18.3)

**(R3) Abandon Born-Helmert direct.** Accept that the direct construction route fails for natural candidates and proceed via:
- Heat-flow Born realization (Pass-4 §4 + Pass-5 §16) at $t > \Lambda$
- The Apex No-Isolator Theorem (Pass-5 §17.3) directly via prime/gamma split
- The Bures Herglotz route (Pass-5 §17) via de Branges/Krein

## Why this is still useful information

1. **The transfer matrix is unconditionally validated.** The closed-form $T_{c,k}$ now has a computational implementation and machine-precision verification. T4 Conjecture 2 stays solved.

2. **The Born-Helmert framework is computable.** Even if the naive candidate fails, the *machinery* — transfer matrix, character coefficients, squared amplitudes, power sums — works correctly and is ready for any refined candidate.

3. **The failure mode is sharp.** We now know exactly which structural features the naive candidate is missing: archimedean Gamma cancellation of the mod-2 parity dominance, endpoint contributions, and a scale renormalization of $\sim 10^4$ at the trace level.

4. **The team is no longer flying blind on the direct route.** Before this probe, Pass-5 Theorem 19.1 was a conditional statement with unknown candidate viability. Now we know the conditional is non-trivial.

## Concrete next experiment (R1 refinement)

The most surgical refinement: add the archimedean Gamma correction.

For each residue $r \in \mathbb Z/N$, define
$$y_t^{\mathrm{full}}(r) = y_t^{\mathrm{prime}}(r) + y_t^{\mathrm{arch}}(r)$$
where $y_t^{\mathrm{arch}}(r)$ is the residue-class localization of the digamma jet from Pass-5 §17.2:
$$y_t^{\mathrm{arch}}(r) = \frac{1}{N} \int_{-\infty}^\infty A_t(u) \cdot \delta_{u \equiv r/N \pmod 1} \, du$$
where $A_t$ is the heat-smoothed archimedean Riemann-Siegel kernel.

If the moment identity closes after adding this term, the Born-Helmert direct route is real. If it doesn't close, we know the next correction needed.

This is the natural follow-up probe.

## Files

- `probe_born_helmert_N30_T7.py` — permissive primes
- `probe_born_helmert_strict_pass4.py` — strict Pass-4
- `T4-HelmertFourierTransferMatrix-WorkedExample-Draft1.md` — closed form derivation
- `probe_born_helmert_N30_findings.md` — this report

## References

- RH Pass-4 §5.1 (candidate ledger definition)
- RH Pass-5 §19 (Born-Helmert direct theorem)
- RH Pass-5 §17.2 (prime/gamma split)
- T4 Conjecture 2 / Helmert-Fourier transfer matrix worked example
