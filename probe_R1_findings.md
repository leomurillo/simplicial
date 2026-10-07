# R1 Findings: Archimedean Correction Fails

**Leonardo Murillo Montero + Codex**

*Working note - May 24, 2026*

## Verdict

\[
\boxed{
\text{R1 with naive archimedean localization: FAILED.}
\]
\]

Per pre-committed criteria:
- Success threshold: $\ge 100\times$ improvement, $p_0$ ratio $\le 10^2$
- Failure threshold: $\le 10\times$ improvement
- Ambiguous: 10–100, iterate

**Achieved: $1.02\times$ improvement at the best scaling sweep.** Far below failure threshold. Direction: archimedean correction at scale $\ne 0.1$ makes things WORSE, not better.

## What was tried

**R1 Attempt 1 — Sweep over scale and sign:**

Construction: $y(r) = y_{\mathrm{prime}}(r) + \kappa \cdot y_{\mathrm{arch}}(r)$ where $y_{\mathrm{arch}}$ is the residue-class inverse-DFT of digamma-jet character coefficients sampled at integer frequencies.

| Scale $\kappa$ | $p_0$ improvement | $p_0$ ratio to $\ell_1$ |
|---|---|---|
| baseline ($\kappa=0$) | 1.0× | $1.80 \times 10^4$ |
| $+0.01$ | 1.00× | $1.80 \times 10^4$ |
| $+0.1$ | 1.02× | $1.76 \times 10^4$ |
| $+1$ | **0.60×** (worse) | $2.98 \times 10^4$ |
| $+10$ | 0.01× (much worse) | $1.70 \times 10^6$ |
| $-1$ | 0.44× (worse) | $4.09 \times 10^4$ |

Adding the archimedean correction at "natural" magnitudes makes the ratio *increase*. The digamma jet at integer frequencies does not cancel the prime ledger's spectral structure.

**Diagnostic Attempt 2 — Single conductor packet projection:**

To check whether ANY filtering of the additive-character decomposition helps:

| Conductor $d$ | $\dim H_d$ | Packet trace | $p_0/\ell_1$ ratio |
|---|---|---|---|
| 2 | 1 | 122.0 | $7.64 \times 10^3$ |
| 3 | 2 | 58.8 | $3.68 \times 10^3$ |
| 5 | 4 | 27.7 | $1.73 \times 10^3$ |
| 6 | 2 | 52.6 | $3.29 \times 10^3$ |
| 10 | 4 | 24.6 | $1.54 \times 10^3$ |
| 15 | 8 | 12.4 | $7.77 \times 10^2$ |
| **30** | **8** | **11.8** | $\mathbf{7.41 \times 10^2}$ |

Best single packet (conductor 30): improvement 26× over baseline. Still ratio $\sim 700$ — TWO orders of magnitude off.

**Even the highest-conductor (most "fine-grained") packet of additive characters does not encode the zero distribution.**

## Diagnosis

The negative result is structural, not technical. Three observations.

**(D4) Additive characters of $\mathbb Z/N$ do not naturally separate the prime racing structure.** The dominant low-conductor modes (conductor 2 alone carries 39% of the trace, conductor 3 another 19%) reflect *parity and small modular structure of primes* — Chebyshev bias and Dirichlet density. These are real arithmetic phenomena, but they are not the spectral content of folded $\xi$.

**(D5) The naturally "right" basis for prime distribution is multiplicative Dirichlet characters of $(\mathbb Z/N)^\times$, not additive characters of $\mathbb Z/N$.** Dirichlet $L$-functions, the explicit-formula natural objects, use multiplicative characters. Their zeros encode arithmetic of residue classes in a way additive characters cannot.

**(D6) Naive scale corrections fail systematically.** The N-scaling probe ruled out $N^k$ rescaling. This probe rules out additive-character localization. Two independent corrections fail.

## Implications for the Born-Helmert direct route

The Pass-5 Theorem 19.1 candidate from Pass-4 §5.1 — the centered additive-character primorial Helmert ledger — does NOT carry the folded $\xi$ cumulant structure, with no available local correction.

This is a real obstruction to the direct route in its current formulation.

## Three pivot options

**(P1) Switch to multiplicative Dirichlet characters (T0 §6.2).**

Replace the additive Fourier-Mellin apex $\mathcal M_x(\beta, c)$ with the multiplicative Dirichlet apex $\mathcal D_x(\beta, \psi)$ over $(\mathbb Z/N)^\times$. This is the natural finite analog of the Dirichlet $L$-function setting where prime distribution lives.

- **Cost:** requires extending T0 §6.2 forward-door material into actual machinery; rebuilding the transfer matrix and Born construction for the multiplicative setting.
- **Benefit:** the right basis for prime distribution; connects to Dirichlet $L$-function literature; the Born squares of the multiplicative version may genuinely encode $L$-function zeros.

**(P2) Heat-flow Born realization (Pass-4 §4, $t > \Lambda$).**

Use the heat-smoothed kernel $\Xi_t$ for $t > \Lambda$ where it has only real zeros. The Born factorization is automatic at any $t > 0$ above the de Bruijn-Newman boundary.

- **Cost:** re-introduces the boundary issue. The $t \to 0^+$ limit is RH itself.
- **Benefit:** unconditional positive Born ledger at each $t > 0$; well-defined finite-stage object; connects to Rodgers-Tao program directly.

**(P3) Bures Herglotz route (Pass-5 §17, de Branges machinery).**

Bypass the Born-Helmert direct construction entirely. Pursue $m_B = \Xi'/\Xi$ Herglotz via de Branges Hilbert space machinery.

- **Cost:** abandons the simplicial-program native route; requires substantial de Branges infrastructure.
- **Benefit:** half a century of established literature; the Lagarias-Burnol work has explicit candidates.

## Recommendation

**Commit to P1 (multiplicative Dirichlet apex)** as the natural next attack.

Rationale:
1. P1 is *still native to the simplicial program* (T0 already names the multiplicative apex as a forward door).
2. P1 directly addresses the diagnosis (D5): use the *right* basis for prime distribution.
3. The transfer-matrix machinery built today is structurally analogous to the multiplicative version — partially reusable.
4. P2 retreats to known boundary problems; P3 abandons the program's distinctive route.

The first concrete step under P1: write the multiplicative analog of the transfer matrix and re-run the moment-match probe with Dirichlet characters $\psi$ on $(\mathbb Z/30)^\times$. Conductor structure is now indexed by primitive Dirichlet characters mod $d \mid 30$, $d \in \{1, 3, 4, 5, 8, 12, ...\}$ ... wait, those don't all divide 30. Restate: primitive characters of conductor $d$ where $d \mid 30$, so $d \in \{1, 3, 5, 6, 10, 15, 30\}$ (excluding 2 since odd Dirichlet characters mod 2 only the trivial one). $(\mathbb Z/30)^\times$ has order $\varphi(30) = 8$, so there are 8 Dirichlet characters mod 30. These are the natural finite-arithmetic basis.

## What this preserves

The structural results of the work remain intact:

- **Transfer matrix closed form** at $N = 6, 30$ (T4 Conjecture 2): still resolved.
- **Pass-5 Theorem 16.2** (RH $\iff$ all-rung $H_n, J_n \succeq 0$): unaffected.
- **Pass-5 §17 prime/gamma split** and Apex No-Isolator Theorem: unaffected.
- **The Born-Helmert framework itself**: works; just needs the right ledger.

What's been ruled out: the *simplest* candidate ledger (Pass-4 §5.1 additive-character primorial sum). The framework is solid; the candidate is wrong.

## Files

- `probe_born_helmert_with_archimedean.py` — R1 attempt 1 (digamma jet)
- `probe_conductor_projection.py` — conductor-packet diagnostic
- `probe_R1_findings.md` — this report

## Next action

Implement multiplicative Dirichlet apex at $N = 30$:
1. Enumerate Dirichlet characters of $(\mathbb Z/30)^\times$ (8 characters total).
2. Compute multiplicative analog of transfer matrix.
3. Construct candidate ledger as Dirichlet sum: $y_\psi = \sum_n \chi(n) \Lambda(n)/\sqrt{n} \cdot \mathbf{1}[n \le e^T]$.
4. Born-square and check moments against $\ell_n$.

Estimated time: 1 session.
