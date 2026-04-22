# QA Report — `verify_theorem_7_1_nine_multiplication.py` (Loop 2)

**Target claim:** Theorem 7.1 (9-multiplication kernel) of `simplicial_vector_calculus.md`.
**Reviewer:** Empirical Reviewer.
**Script reviewed:** `empirical/verify_theorem_7_1_nine_multiplication.py` (312 lines).
**Paper sections consulted:** §2.4 (Gram matrix), §2.5 (N=4 conventions), §3 (Definition 3.1, Remark 3.2), §5 (Rodrigues, §5.4 worked example), §6, §7 (Theorem 7.1), Appendix D.

---

## Loop 1 → Loop 2 delta

| Loop-1 finding | Severity | Status in Loop 2 |
|---|---|---|
| H1. Test 4 did not implement §5.4 / App. D | High | **Resolved.** `test_4_worked_example` now builds `K(u)` via `build_K_u`, asserts `K1=0`, `K^T=-K`, `K^3=-K`, and `u^T G u = 1`, Rodrigues-exponentiates at θ=2π/3, and compares `R @ P` against the exact App. D target `((√3−2)/2, −√3/2, (√3+2)/2, −√3/2)` at 1e-12. |
| H2. Generator bypassed Def. 3.1; no R-sanity assertions | High | **Resolved.** (a) New `build_K_u` + `generate_random_rotation_via_Ku` sampler instantiates Def. 3.1 directly with simplicial-unit-norm axis. (b) New `test_1b_identity_via_Ku` runs 10⁴ trials at 1e-12. (c) Both generators now assert `R1=1`, `R^T R=I`, `det R=1` per draw. |
| M1. Lax 1e-10 tolerance | Medium | **Resolved.** Tests 1, 1b, 4, 6 now all threshold at 1e-12. |
| M2. Inner `np.random.seed(42)` inside test_4 | Medium | **Resolved.** Removed; single top-level seed at line 292. |
| M3. Negative test not quantitative | Medium | **Resolved.** Test 5 now checks `|RP[:3] − kernel[:3]| ≈ R[:3,3]·sum(P)` at 1e-12, not just a magnitude threshold. Formula is correctly restricted to the three unabsorbed components. |
| M4. Elementwise R_tilde construction | Medium | **Resolved.** Vectorized slicing in Tests 1, 1b, 4, 5, 6. |
| L1. H3 independence not made explicit | Low | **Resolved.** Docstring now states the MatrixSymbol construction makes the 9-count a structural property independent of (u, θ). |
| L2. Dual counting methodology | Low | **Resolved.** Single strict count via `len(Add.args)` after `expand`. |
| L3. No P-normalization in reports | Low | Unchanged; harmless. |
| L4. No R-sanity asserts | Low | **Resolved** alongside H2. |
| L5. Unnecessary non-zero-sum guard | Low | **Resolved.** Guard removed. |

---

## Findings (Loop 2)

### Critical

- None.

### High

- None.

### Medium

- **M-new-1. Test 4 uses a hard `assert` for `error_full < 1e-12` (line 196) before returning a verdict.** The surrounding script uses return-based `passed` flags so that a failing test still allows the summary table to print. A raw `AssertionError` at line 196 would abort execution before H5 and H6 run. Given the error budget (~1e-15 by hand calculation), this is unlikely to trigger, but it creates a single point of abort. Recommend replacing with a `passed_full = error_full < 1e-12` branch and folding it into the final `passed = passed_full and passed_reduced`. Polish only.

### Low

- **L-new-1. K-property assertions in `test_4` use 1e-14 while identity tests use 1e-12 (lines 181–187, 196).** Defensible — the K matrix for the specific axis has entries exactly representable as ±1/2 up to ~1e-16 rounding, so 1e-14 is achievable — but inconsistency across tests can confuse readers. Consider unifying on 1e-12 or documenting why 1e-14 is safe here.

- **L-new-2. `test_2_and_3_symbolic_count` treats a non-`Add` expression as contributing 1 mul (line 153).** For a MatrixSymbol × MatrixSymbol product after `sp.expand`, each row will always be an `Add` with 3 args, so the branch `else 1` is unreachable in the current setup. Harmless defensive code, but slightly misleading to a reader.

- **L-new-3. Per-call sanity asserts in both generators are executed 10⁵ + 10⁴ times.** Cost is negligible (≈O(10) flops per assert on a 4-vector), but a one-time assertion on a canary draw would be the usual idiom. Style only.

---

## Independent verifications performed this cycle

1. **Entrywise equality `build_K_u` ↔ Definition 3.1.** Compared the Python array against the paper's matrix (§3.2, lines 219–224) entry by entry with substitution `(ul, un, um, up) ↔ (u_l, u_n, u_m, u_p)`. All 16 entries match; skew-symmetry and vanishing row/column sums hold by construction.

2. **Appendix D worked-example target.** Hand-computed `K(u)` for `u = (√3/4)(1,1,−1,−1)` (entries of `K` are ±1/2 in a block-antidiagonal pattern), formed `K²` (block-diagonal ±1/2), applied Rodrigues at `θ=2π/3`, multiplied against `P = (1/2, −3/2, −1/2, 3/2)`. Result matches `((√3−2)/2, −√3/2, (√3+2)/2, −√3/2)` exactly. The 1e-12 assertion will pass with headroom (expected drift ≈1e-15).

3. **M3 disagreement formula.** Derived analytically: for `i ∈ {0,1,2}`, `(RP)_i − kernel_i = R_{i,3}·Σ_k P_k`. The script compares only the first three components against this formula, correctly avoiding the different (and naive-hint-incompatible) component-3 residual. Verified.

4. **Simplicial-unit normalization in `generate_random_rotation_via_Ku`.** After `u = u / sqrt((4/3)·Σ u_i²)`, the post-scale axis satisfies `Σ u_i² = 3/4` and hence `u^T G u = 1` with `G = (4/3)I − (1/3)J`. Zero-sum preserved by scaling. Matches Definition 3.1's preconditions.

5. **9-mul strict count.** `sp.MatrixSymbol` entries are independent placeholders; after `sp.expand`, each row of the 3×3·3×1 product is an `Add` of three distinct monomials `R_tilde[i,j]*P[j,0]` with no like-term collapse available. 3·3 = 9 exactly, stable under repeated runs.

---

## Fidelity to the paper — summary

| Paper object | Script implementation | Verdict |
|---|---|---|
| `K(u)` via Def. 3.1 (cyclic differences, 1/√3) | `build_K_u` (lines 38–47) | Matches entry-wise |
| Zero-sum unit axis (`u^T G u = 1`) | Explicit normalization + assertion (line 187) | Correct |
| Rodrigues `R = I + sin θ·K + (1−cos θ)·K²` | Lines 30, 59, 190 | Correct |
| Simplicial rotation properties | Asserted in both generators + Test 4 | Correct and now defensively checked |
| `tilde R_{ij} = R_{ij} − R_{ip}` for fixed p=4 | Vectorized slicing at lines 82, 114, 199 | Correct |
| Absorbed-index invariance for arbitrary p | Lines 262–280 | Correct |
| Symbolic 9-mul count | Lines 146–160 via MatrixSymbol + expand + Add.args | Correct |
| §5.4 / App. D worked example (`u=(√3/4)(1,1,−1,−1)`, θ=2π/3, P=(1/2,−3/2,−1/2,3/2), P′=((√3−2)/2,−√3/2,(√3+2)/2,−√3/2)) | `test_4_worked_example` now implements all of it at 1e-12 | Correct; target value independently re-derived |

---

## Expected runtime

Test 1: 10⁵ trials × (4×4 skew gen + projector sandwich + 2-norm + Rodrigues + 3×3 apply). Rough estimate: 60–120 s on CPU.
Test 1b: 10⁴ trials × (zero-sum proj + norm + Def.3.1 build + Rodrigues + 3×3 apply). ~6–15 s.
Tests 2, 3, 4, 5: subsecond.
Test 6: 10⁴ trials × 4 absorbed-index variants. ~15–30 s.
Total: well under 5 min on a modern laptop; no performance blocker.

STATUS: GREEN
