# Audits ξ + χ_10 + χ_12 — Settlement (Batch 2: Small-N Empirical Extensions)

**Date:** 2026-05-20
**Audit scripts:**
- [`empirical/audit_xi_capacity_z510510_extension.py`](../audit_xi_capacity_z510510_extension.py)
- [`empirical/audit_chi_bures_hessian_z10_z12.py`](../audit_chi_bures_hessian_z10_z12.py)

**Deterministic transcripts:**
- [`empirical/audit_xi_capacity_z510510_extension_run_output.txt`](../audit_xi_capacity_z510510_extension_run_output.txt)
- [`empirical/audit_chi_bures_hessian_z10_z12_run_output.txt`](../audit_chi_bures_hessian_z10_z12_run_output.txt)

**Tier:** **[P]** for all `Capacity_V` integer values and Bures-Hessian / quartic-form signatures on the audited rows (integer arithmetic in every membership decision; deterministic linear algebra in every Hessian eigendecomposition); **[A]** for the K-branch classification of the PNT-heuristic extrapolation (audit ξ ratio 1.538 within factor-of-2 K-branch threshold; the mild upward drift of the multiplicative constant K is a recorded sub-finding); **[P]** for the joint-on-disjoint outcome of the V/W/M trichotomy on `ℤ/12` at the tangent-sub-bundle tier (W-Eucl ⊥ M-Eucl max overlap 0.447, NOT machine floor); **[P]** for the K-branch outcome of the V/M binary on `ℤ/10` and `ℤ/12` at the tangent tier (all sub-bundle orthogonalities at machine floor).
**Wall time (all three audits combined):** **< 2 seconds** on CPU. Pure linear algebra; integer arithmetic in capacity counts; deterministic eigendecompositions.

---

## Audit ξ — Capacity_V at ℤ/510510 (the 7th primorial row)

**Settles:** Paper 48 (proposed) C3/C4 sharper than audit ι's five-row anchor; tests the PNT-heuristic shape prediction `Capacity_V(P_n) ~ K · n² · ln(n) / N²`.

### Headline result

| Row | `n` | `dim_V` | `T_total` | `pure_V` | `Capacity_V` | log₁₀ |
|---|---:|---:|---:|---:|---:|---:|
| ℤ/6 | 2 | 3 | 6 | 2 | 3.333e-1 | −0.48 |
| ℤ/30 | 3 | 7 | 150 | 6 | 4.000e-2 | −1.40 |
| ℤ/210 | 4 | 13 | 7 350 | 14 | 1.905e-3 | −2.72 |
| ℤ/2310 | 5 | 23 | 889 350 | 34 | 3.823e-5 | −4.42 |
| ℤ/30030 | 6 | 35 | 150 300 150 | 62 | 4.125e-7 | −6.38 |
| **ℤ/510510** | **7** | **51** | **43 436 743 350** | **110** | **2.532e-9** | **−8.60** |

`Capacity_V(ℤ/510510) = 110 / 43,436,743,350 = 2.532 × 10⁻⁹` (exact rational).

### Three-outcome adjudication (PNT-heuristic shape test)

Audit ι (v2insert-10) PNT-heuristic prediction:
```
Capacity_V(P_n) ≈ K · n² · ln(n) / N²,   K_mean ≈ 4.5 over 5 rows.
```
At `n = 7, N = 510510`:
```
PNT prediction = 4.5 · 49 · ln(7) / 510510² ≈ 1.646 × 10⁻⁹
```

**Observed / Predicted ratio:** `2.532e-9 / 1.646e-9 = 1.538`

**K-branch realized** (ratio within factor of 2). The audit-ι joint-on-disjoint settlement extrapolates cleanly to the 7th primorial row.

### Sub-finding: multiplicative constant has mild upward drift

Re-fitting `K = Capacity_V · N² / (n² · ln(n))` across the six rows:

| Row | K observed |
|---|---:|
| ℤ/6 | 4.328 |
| ℤ/30 | 3.641 |
| ℤ/210 | 3.787 |
| ℤ/2310 | 5.070 |
| ℤ/30030 | 5.767 |
| ℤ/510510 | 6.922 |

Mean K = 4.92; range [3.64, 6.92]; spread **1.901×** (audit-ι 5-row spread was 1.584×).

The K-constant has **monotone upward drift across the four largest rows** (`3.64 → 3.79 → 5.07 → 5.77 → 6.92`). This is a sub-leading correction the leading-order PNT heuristic does not capture; the asymptotic-shape claim `Capacity_V ~ K · n² · ln(n) / N²` remains correct, but the multiplicative constant is itself slowly varying with `n` (consistent with higher-order terms in the PNT expansion of `dim_V` and `T_total`).

### Decay-factor pattern

Per-step decay (`Capacity_V(P_n) / Capacity_V(P_{n+1})`):

| Step | Added prime | Decay factor |
|---|---:|---:|
| 6 → 30 | 5 | 8.33× |
| 30 → 210 | 7 | 21.0× |
| 210 → 2310 | 11 | 49.8× |
| 2310 → 30030 | 13 | 92.7× |
| **30030 → 510510** | **17** | **163×** |

The accelerating-decay pattern continues. Decay factor ~ `p_{n+1}²` (with growth correction from `|V|`): 17² = 289 vs observed 163 (factor ~ 1.77 reduction from |V| growth — consistent with audit θ's analysis).

---

## Audit χ_10 — Bures-Hessian on D(ℂ¹⁰), ℤ/10 = 2·5

**Settles:** Paper 46/47/48 extension to the **first squarefree non-primorial row**.

| Conductor | `V_idx (dim 5)` | `M_idx (dim 4)` | `‖P_V · P_M‖_F` |
|---|---|---|---:|
| `ℤ/10 = 2·5` | `{2, 4, 5, 6, 8}` | `{1, 3, 7, 9}` | `1.86e-15` |

99-dim tangent space `T_{ρ_*} D(ℂ¹⁰)`. Audit predictions and results:

| Predicate | Predicted | Observed | Status |
|---|---|---|:---:|
| Hessian I_real signature | `(1, 4, 94)` | `(1, 4, 94)` | ✓ |
| `m²_simplex` quartic signature | `(4, 0, 95)` | `(4, 0, 95)` | ✓ |
| V-Lorentzian (dim 5) ⊥ M-Euclidean (dim 4) | `~10⁻¹⁶` | `3.20e-16` | ✓ |

**K-branch realized** on `D(ℂ¹⁰)`. The Hartle–Hawking V-Lorentzian + M-Euclidean signature pattern extends from primorials to squarefree non-primorials cleanly. Paper 36's digits task algebra `ℤ/10` carries the V/M decomposition at [P] at the Bures-Hessian tangent-sub-bundle tier.

---

## Audit χ_12 — Bures-Hessian on D(ℂ¹²), ℤ/12 = 2² · 3 (non-squarefree)

**Settles:** Paper 47/48 non-squarefree extension; tests v2insert-05 P9 joint-on-disjoint prediction for the prime-power packet `H_4`.

### Conductor lattice of ℤ/12

| Packet | Indices | Dim | Conductor structure |
|---|---|---:|---|
| `H_2` | `{6}` | 1 | single-prime (2) |
| `H_3` | `{4, 8}` | 2 | single-prime (3) |
| `H_4` | `{3, 9}` | 2 | prime-power (2²) |
| `H_6` | `{2, 10}` | 2 | cross-prime (2·3) |
| `H_12` | `{1, 5, 7, 11}` | 4 | cross-prime (2²·3) |

### Three candidate decompositions

| Decomposition | V_idx (dim) | M_idx (dim) | Extra |
|---|---|---|---|
| (a) Strict V/M | `H_2 + H_3` (3) | `H_4 + H_6 + H_12` (8) | — |
| (b) Inclusive V/M | `H_2 + H_3 + H_4` (5) | `H_6 + H_12` (6) | — |
| (c) Trichotomy V/W/M | `H_2 + H_3` (3) | `H_6 + H_12` (6) | `W = H_4` (2) |

### Audit results on the 143-dim tangent space

| Decomposition | Hessian sig | `m²_M` quartic sig | V ⊥ M (max sv) | V ⊥ W | W ⊥ M |
|---|---|---|---:|---:|---:|
| (a) Strict V/M | `(1, 2, 140)` ✓ | `(8, 0, 135)` ✓ | `3.70e-16` | — | — |
| (b) Inclusive V/M | `(1, 4, 138)` ✓ | `(6, 0, 137)` ✓ | `2.83e-16` | — | — |
| (c) Trichotomy V/W/M | `(1, 2, 140)` ✓ | `(6, 0, 137)` ✓ | `3.50e-16` | `1.05e-16` | **`4.47e-01`** |

All Hessian and quartic signatures match expectations exactly. **All V-Lorentzian ⊥ M-Euclidean orthogonalities at machine floor.** But the W-Euclidean ⊥ M-Euclidean overlap in the trichotomy is **0.447** — NOT machine floor.

### Adjudication — the key finding

**At the Hilbert-subspace level on `ℂ¹²`** (Pontryagin character orthogonality on `(ℤ/12)^∧`):
- V, W, M are **pairwise HS-orthogonal as subspaces of `ℂ¹²`** (all `‖P_X · P_Y‖_F` at machine floor).
- The binary V/M (strict or inclusive) and the trichotomy V/W/M produce equally clean Hilbert-subspace decompositions.

**At the tangent-sub-bundle level on `T_{ρ_*} D(ℂ¹²)`**:
- The V-Lorentzian sub-bundle (eigenspace of Hessian of V-supported `I_real`) is HS-orthogonal to **both** the W-Euclidean quad eigenspace and the M-Euclidean quad eigenspace at machine precision.
- **The W-Euclidean and M-Euclidean tangent sub-bundles SHARE tangent directions** (max overlap singular value `4.47e-01`, far above machine floor).

### Structural reason for the W ⊥ M tangent overlap

Off-diagonal-in-standard-basis tangent vectors `T_{ij} = E_{ij} + E_{ji}` have **character-basis-diagonal entries spread across multiple `k` indices**:
```
diag_char(T_{ij})_k = (2/N) · cos(2π(j-i)k/N)
```
which is non-zero for *most* `k`. So a single tangent direction can have simultaneous non-trivial diag_char content at both W-indices `{3, 9}` AND M-indices `{1, 2, 5, 7, 10, 11}`. The W-quad and M-quad forms — both built from character-basis-diagonal entries at their respective index sets — have **overlapping eigenspaces** in `T_{ρ_*} D(ℂ¹²)`.

### The settlement (v2insert-05 P9 joint-on-disjoint at tangent tier)

Under v2insert-04 §3.1's three-outcome rule applied to the v2insert-05 P9 pre-claim ("prime-power H_4 needs its own status"):

- **K-branch** (V/M binary with H_4 in V): realized cleanly at machine floor. Inclusive decomposition produces (1, 4, 138) Hessian + (6, 0, 137) quartic + V ⊥ M at 2.83e-16.
- **K-branch** (V/M binary with H_4 in M): also realized cleanly at machine floor. Strict decomposition produces (1, 2, 140) Hessian + (8, 0, 135) quartic + V ⊥ M at 3.70e-16.
- **Joint-on-disjoint** (V/W/M trichotomy): **REALIZED at the tangent-sub-bundle tier**. The trichotomy is clean at the Hilbert-subspace level (V ⊥ W ⊥ M as subspaces of `ℂ¹²`) but the **4th-order quartic forms `(m²_W)²` and `(m²_M)²` have overlapping eigenspaces** in the tangent geometry. The prime-power H_4 cannot be cleanly separated from the cross-prime carry M at the Bures-Hessian sub-bundle tier.

### Implication for the AI manifestation (Papers 36, 37)

The months task on `ℤ/12` (Paper 36 P3 + Paper 37 sweep) uses the *inclusive V/M* convention (V = H_2 + H_3 + H_4) per v2insert-05 §1. Audit χ_12 validates this choice at the Bures-Hessian tangent-sub-bundle tier:

- The **inclusive V/M** decomposition is the **natural binary partition** on non-squarefree rings; the prime-power H_4 should be folded into V at the Bures-Hessian tier.
- The **strict V/M** is also valid (single-prime conductor only) but produces a smaller V-Lorentzian sub-bundle (dim 3 vs 5).
- The **trichotomy V/W/M** is **NOT a clean tangent-level structural choice** because of the W ⊥ M tangent overlap. Use binary V/M for empirical work on `ℤ/12`.

When audit κ un-defers (GPU + HuggingFace), the residual-stream V/M binning on the months task should use the **inclusive V/M** convention; the prime-power H_4 packet on `ℤ/12` is part of the V (kinematic) sector at the tangent-geometry level.

---

## Combined verdict — Batch 2

| Audit | Predicted | Realized | Branch |
|---|---|---|---|
| ξ (Capacity_V on ℤ/510510) | PNT shape `K · n²·ln(n)/N²` within factor 2 | Ratio 1.538 (within 2) | **K-branch** with mild K-drift sub-finding |
| χ_10 (D(ℂ¹⁰)) | V-Lorentzian (1, 4) + M-Euclidean (4, 0), V ⊥ M | All confirmed at machine floor | **K-branch** |
| χ_12 binary (D(ℂ¹²)) | V-Lorentzian + M-Euclidean, V ⊥ M | All confirmed at machine floor | **K-branch** (both strict and inclusive) |
| χ_12 trichotomy | V ⊥ W ⊥ M at every tier | V ⊥ W, V ⊥ M at machine floor; **W ⊥ M overlap = 0.447** | **Joint-on-disjoint** at tangent tier |

---

## Implications for the proposed papers

### Paper 46 (Hartle–Hawking signature)

- **C5 geometric realization extends beyond primorials** to squarefree non-primorial ℤ/10 (χ_10) and to non-squarefree ℤ/12 (χ_12 binary). At [P] on three additional rows.

### Paper 47 (Arithmetic Decoupling Theorem)

- **C3 row-generalization extends to non-squarefree rings** at the Hilbert-subspace level (V ⊥ M by Pontryagin character orthogonality at machine floor on every conductor packet decomposition). At [P] on ℤ/10 and ℤ/12.
- **The V/M binary is the natural tangent-tier structural choice** on non-squarefree rings; trichotomy is joint-on-disjoint at the tangent tier.

### Paper 48 (Conductor Capacity Bound)

- **C3 / C4 PNT-heuristic shape extrapolates to row 7** (`Capacity_V(ℤ/510510) = 2.532e-9`, ratio 1.538 to PNT prediction).
- The mild upward K-drift (3.64 → 6.92 across six rows) is a recorded sub-finding; the asymptotic 1/N² + n²·ln(n) shape remains the load-bearing structural claim.
- Audit ι's joint-on-disjoint settlement is robust across six rows.

### Paper 36 / Paper 37 (AI manifestation, when audit κ un-defers)

- **The inclusive V/M decomposition is the natural choice for the months task on ℤ/12.** Prime-power H_4 ∈ V at the Bures-Hessian tangent tier.
- The trichotomy V/W/M is NOT a clean tangent-level structural choice (W ⊥ M tangent overlap 0.447); avoid it in audit κ's V/M binning.

---

## Discipline check (Paper 35 §3 honored throughout)

- **Anchored objects (§3.3).** All conductor-packet enumerations are integer arithmetic on divisors. Character basis is the DFT of `ℤ/N`. The five-row v2insert-09 anchors are reproduced to exact integer match within audit ξ.
- **Deterministic, exact, reproducible (§3.4).** Total wall time across three audits < 2 seconds. Deterministic; no seeds.
- **Three-outcome matched-pair (§3.1 + v2insert-04 §3.1).** All three audits explicitly stage K / L / joint-on-disjoint. Audit ξ realized K (mild K-drift sub-finding); audits χ_10 / χ_12 binary realized K; audit χ_12 trichotomy realized joint-on-disjoint at the tangent tier.
- **No upward tier-crossing (§3.5).** Capacity values, signatures, and overlap norms reported at [P]. The PNT-heuristic shape characterization remains [A].
- **Failures-first-class (§3.6).** The mild upward K-drift in audit ξ and the W ⊥ M tangent overlap in χ_12 trichotomy are reported as recorded sub-findings, not absorbed silently into K.
- **Dimensional firewall (Paper 32 §11.2).** No physical units. Only dimensionless integer counts, ratios, eigenvalues, and singular values.

---

*Settlement record archived. Audits ξ + χ_10 + χ_12 — Batch 2 small-N empirical extensions — settled. Audit ξ confirms PNT-heuristic shape extrapolates to ℤ/510510 at K-branch with ratio 1.538 (mild K-drift sub-finding 3.64 → 6.92 across six rows). Audit χ_10 extends V/M decomposition to first squarefree non-primorial row at [P] (D(ℂ¹⁰)). Audit χ_12 settles non-squarefree ℤ/12: binary V/M K-branch at machine floor for both strict and inclusive partitions; trichotomy V/W/M joint-on-disjoint at tangent tier (W ⊥ M overlap 0.447). Inclusive V/M is the natural tangent-tier convention; the AI manifestation on ℤ/12 should use it when audit κ un-defers. Total wall time < 2 seconds. Reproducibility artifacts: [`empirical/audit_xi_capacity_z510510_extension.py`](../audit_xi_capacity_z510510_extension.py), [`empirical/audit_chi_bures_hessian_z10_z12.py`](../audit_chi_bures_hessian_z10_z12.py).*
