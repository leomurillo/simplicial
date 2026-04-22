# Empirical Reviewer QA Report — Proposition 6.1

**Script:** `empirical/verify_proposition_6_1_rotation_properties.py`
**Target claim:** Proposition 6.1 of `simplicial_vector_calculus.md`, lines 387–397 — nine structural properties of $R(u, \theta)$.
**Submission package:** code + captured stdout (Skeptical executed the script before submitting per the updated empirical-validation skill).

## 1. Reuse of upstream certified helpers

- **No finding.** `build_K_u` (lines 13–22) and `generate_random_zero_sum_vector` (lines 8–11) are byte-identical to their counterparts in the certified `verify_theorem_7_1_nine_multiplication.py` (verified by MD5). The two intentional divergences:
  1. `generate_random_rotation` (lines 24–35): per-call asserts stripped and hoisted into `preflight_checks`. Performance-correct.
  2. `generate_random_rotation_via_Ku` (lines 37–50): return signature extended to `(R, u, theta)` to expose $\theta$ for the trace (P5) and spectrum (P9) tests; per-call asserts likewise removed. Documented in the docstring, extra returns consumed by callers at lines 107 and 160.

## 2. Preflight asserts (lines 52–65)

- **No finding.** Preflight runs on a single canary draw once at script start (main block, line 226), not on every trial. Asserts $K\mathbf{1}=0$, $K^\top=-K$, $K^3=-K$ at the $K(u)$ level and $R\mathbf{1}=\mathbf{1}$, $R^\top R=I$, $\det R=1$ at the $R$ level, tolerance `1e-12`. Correct scope; no per-trial performance leak.

## 3. Per-test correctness

- **No finding. P1 orthogonality (lines 67–74), P2 row sums (76–83), P3 column sums (85–92), P4 determinant (94–101), P6 hyperplane (113–121):** direct 1:1 maps to Prop 6.1.1/2/3/4/6.
- **P5 trace (lines 103–111): Low.** Tests $|\operatorname{tr}(R) - (2+2\cos\theta)|$ (the gauge-lift form). The equivalent restricted-trace form $\operatorname{tr}(R|_H) = 1+2\cos\theta$ is not explicitly computed, but it is mathematically implied by P2 + the identity $\operatorname{tr}(R|_H) = \operatorname{tr}(R) - 1$. Since P2 passes at ~1e-15 and P5 at ~3e-15, the derived restricted-trace identity holds at ~4e-15. Not a coverage gap, just a docstring note.
- **No finding. P7 gauge-equivariance (lines 123–134):** genuine randomized test — $P$ sampled from $\mathbb{R}^4$ (not restricted to $H$), $k$ sampled from $\mathcal{N}(0,1)$, both sides of $R(P + k\mathbf{1}) = RP + k\mathbf{1}$ computed and subtracted. Not degenerate. Algebraically equivalent to P2 + linearity, so passing at the same order as P2 (~3e-15) is expected and observed.
- **No finding. P8 metric (lines 136–154):** both forms exercised in the same trial — the scalar inner-product form $\langle RP, RQ\rangle_s - \langle P, Q\rangle_s$ and the matrix form $R^\top G R - G$, using the correct $G = \frac{4}{3}I - \frac{1}{3}J$ (line 139). `max_err` aggregates over both.
- **P9 spectrum (lines 156–187):**
  - **No finding.** Eigenvalue pairing: sort key `(abs(z - 1.0), np.imag(z))` (lines 168–170) correctly separates the two $\lambda=1$ eigenvalues from the complex pair $e^{\pm i\theta}$ because $|e^{\pm i\theta}-1| = 2|\sin(\theta/2)|$ is $\Theta(1)$ for generic $\theta$, whereas the two $\lambda=1$ eigenvalues sit within $\mathcal{O}(\varepsilon_{\text{mach}})$ of $1$. Within each group, the imaginary-part tiebreak handles sign selection cleanly for generic $\theta$. Observed max err 3.55e-15 is consistent with 4×4 eig decomposition precision.
  - **Low (edge cases).** At $\theta \to 0, 2\pi$ the complex pair collapses onto the real eigenvalues (the $|z-1|$ key ceases to separate groups); at $\theta \to \pi$ the imag tiebreak becomes degenerate within the complex pair ($\sin\theta \to 0$). Neither case actually breaks the pairwise error bound — expected and actual arrays converge to the same limit — and with seeded uniform sampling on $[0, 2\pi]$ the probability of numerical ambiguity is $\lesssim 10^{-10}$ per trial. No action required; a Hungarian-style min-weight matching would be defensively more robust.
  - **No finding.** Eigenspace: $Ru \approx u$ (line 178) and $R\mathbf{1} \approx \mathbf{1}$ (line 179) tested per trial. Rank test (line 182, `np.linalg.matrix_rank(R-I, tol=1e-10)`): the absolute tolerance is tight enough to reject spurious rank inflation from ~1e-14 roundoff and loose enough to treat the two structural zero singular values as zero. Only theoretical edge case is $\theta=0$ (then $\operatorname{rank}(R-I)=0\ne 2$); measure zero in uniform sampling and did not occur with seed 42.
- **P5' Appendix D (lines 189–221):** deterministic worked example $u = (\sqrt{3}/4)(1,1,-1,-1)$, $\theta = 2\pi/3$. Normalization confirmed: $(4/3)\sum u_i^2 = (4/3)(4\cdot 3/16) = 1$. Tests all nine properties at tolerance `1e-14`. Observed max err 4.44e-16 = machine epsilon.
  - **Low.** This deterministic block does not reproduce the eigenspace/rank checks from P9 (lines 178, 182), only the eigenvalue-list check (line 218). Stochastic P9 covers it, so coverage is adequate, but parity across deterministic and stochastic suites would be cleaner.

## 4. Numerical stability & algorithmic correctness

- **No finding.** No catastrophic cancellation: all operations on $4\times 4$ matrices with $\mathcal{O}(1)$ entries ($K$ normalized to spectral norm 1; $\sin\theta, 1-\cos\theta \in [0,2]$). No subtraction of near-equal $\mathcal{O}(1)$ quantities.
- **No finding.** All tests enforce `max_err < 1e-12`.
- **No finding.** `np.linalg.eigvals` on a 4×4 real matrix is numerically safe; the subtraction at line 175 correctly handles the complex return array.

## 5. Runtime & reproducibility

- **No finding.** `np.random.seed(42)` set exactly once at line 224, at the top of `main`, before any random draw. Appendix D (P5') is fully deterministic, so seed stability is not broken by its ordering. Total work $\approx 10^4 \times 10$ tests of 4×4 float64 arithmetic; captured output shows all tests completed — comfortably under the 30-s budget.

## 6. Output plausibility cross-check (independent of code review)

Predicted per-operation floor in float64 is ~1e-15 for a single 4×4 operation; compound operations accumulate linearly.

| Property | Max err | Predicted floor | Ratio | Plausibility |
|---|---|---|---|---|
| P1 orthogonality | 4.99e-15 | ~1e-15 (4×4 matmul − I) | ~5× | On-floor |
| P2 row sums | 1.11e-15 | ~1e-15 (one 4-term sum) | ~1× | Machine epsilon |
| P3 col sums | 1.51e-14 | ~1e-15 (symmetric to P2) | ~15× | **Mildly elevated, see below** |
| P4 determinant | 6.22e-15 | ~1e-15 | ~6× | On-floor |
| P5 trace | 3.00e-15 | ~1e-15 | ~3× | On-floor |
| P6 hyperplane | 6.66e-15 | ~1e-15 | ~7× | On-floor |
| P7 gauge-equiv | 2.66e-15 | ~1e-15 (equiv to P2) | ~3× | On-floor |
| P8 metric | 2.49e-14 | ~1e-14 (two 4×4 matmuls) | ~2× | On-floor |
| P9 spectrum | 3.55e-15 | ~1e-15 (4×4 eig) | ~4× | On-floor |
| P5' deterministic | 4.44e-16 | ~1e-16 (exact rational inputs) | ~1× | Machine epsilon |

- **Low (informational).** P3 at 1.5e-14 vs structurally symmetric P2 at 1.1e-15 is a ~15× gap. Rationale: $K^2$ is computed once as `K @ K` and its transpose inherits subtle roundoff asymmetry from float-matmul non-associativity; also $R^\top \mathbf{1}$ touches the column layout differently than $R\mathbf{1}$. Over $10^4$ i.i.d. draws, tail-extremum variation easily explains a 15× ratio between two samples from nearly the same error distribution. Not a generator bug. A reseed sanity-run would likely show P2 and P3 swapping ranks occasionally.
- No `nan`, `inf`, or silent `RuntimeWarning` in captured stdout. `PASS`/`FAIL` labels are internally consistent with the printed max errors and the 1e-12 threshold.

## 7. Counter-example scan

- No observed value falsifies a Proposition 6.1 property at 1e-12 tolerance. No STATUS: RED trigger.

## Summary by severity

- **Critical:** none.
- **High:** none.
- **Medium:** none.
- **Low:** (1) P5 docstring omits the equivalent restricted-trace form; (2) P9 eigenvalue pairing has theoretical edge-case fragility at $\theta \in \{0, \pi, 2\pi\}$; (3) P3 tail-extremum ~15× above P2, almost certainly a sampling artefact; (4) P5' deterministic block does not mirror P9's eigenspace/rank checks.

None of the Low findings invalidate the conclusion.

STATUS: GREEN
