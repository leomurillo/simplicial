# Paper 46 (proposed) C5 Geometric Realization on D(ℂ³⁰) — Bures-Hessian Sub-Bundle Audit

**Date:** 2026-05-20
**Audit script:** [`empirical/paper46_bures_hessian_sub_bundle_audit_z30.py`](../paper46_bures_hessian_sub_bundle_audit_z30.py)
**Deterministic transcript:** [`empirical/paper46_bures_hessian_sub_bundle_audit_z30_run_output.txt`](../paper46_bures_hessian_sub_bundle_audit_z30_run_output.txt)
**Tier:** **[P]** for the hybrid signature pattern on `D(ℂ³⁰)` at the centroid `ρ_* = I_30/30`: V-Lorentzian `(1, 6)` on a 7-dimensional V-supported tangent sub-bundle (exact along V-rays), M-Euclidean `(22, 0)` on a 22-dimensional M-supported tangent sub-bundle (from the 4th-order quartic form `(m²_simplex)²`), HS-orthogonal at machine precision (max singular value of overlap `5.82 × 10⁻¹⁶`), flat on the remaining 870 directions. Deterministic float audit on `D(ℂ³⁰)`'s 899-dimensional tangent space; no fitted parameters; no tolerances in any decision.
**Wall time:** **3.95 seconds** on CPU. No GPU. Pure linear algebra: a 899 × 899 symmetric eigendecomposition + projector overlaps.
**Anchors:** Paper 32 §13.2B audit triad on `D(ℂ⁶)` (reproduced as the dim-6 special case); audit δ all-orders Pontryagin proof (the structural foundation); audit α/η/θ row-generalization at the arithmetic-substrate tier (the V/M decomposition extends across primorial rows, this audit confirms it at the geometric tier).

---

## 1. Audit scope and pre-claim

Settles Paper 46 (proposed) C5 *geometric realization on `D(ℂ^N)` for `N > 6`* at the first row beyond the minimal mixed CRT row: does the **Hartle–Hawking signature pattern** of Paper 32 §13.2B (V-Lorentzian on V-supported sub-bundle + M-Euclidean on M-supported sub-bundle, HS-orthogonal, jointly realized) extend to the Bures lift `D(ℂ³⁰)` of the next primorial row `ℤ/30`?

Pre-claim (Paper 46 (proposed) §1.2 + v2insert-01 §2.3 C5, [A] at v0.1):
- **K-branch:** The hybrid signature pattern extends — Lorentzian sub-bundle on V's `(p_i - 1)`-block for each prime `p_i | N`, Euclidean correction on M's cross-prime block — confirming the correspondence is structural, not row-specific.
- **L-branch:** The signature pattern does not extend; `ℤ/6` is the minimal and unique CRT row carrying the Hartle–Hawking signature.
- **Joint-on-disjoint:** Partial extension with row-specific structural corrections.

---

## 2. Setup and operator construction

### 2.1 Conductor lattice on `ℤ/30`

Integer-arithmetic partition of `(ℤ/30)^∧ \ {0}` (audit δ machinery):

```
V_idx (single-prime conductor, dim_V = 7):  [6, 10, 12, 15, 18, 20, 24]
M_idx (composite-divisor,    dim_M = 22):  [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 16, 17,
                                            19, 21, 22, 23, 25, 26, 27, 28, 29]
```

`V` corresponds to single-prime conductor packets `H_2 = {15}, H_3 = {10, 20}, H_5 = {6, 12, 18, 24}` (dim `1 + 2 + 4 = 7`). `M` corresponds to cross-prime carry packets `H_6, H_{10}, H_{15}, H_{30}` (dim `2 + 4 + 8 + 8 = 22`).

Pontryagin check: `‖P_V · P_M‖_F = 1.225 × 10⁻¹⁴` (at machine floor; algebraic value 0 exactly by character orthogonality on disjoint index sets).

### 2.2 V-supported operators (generalized-Gell-Mann construction)

On the 7-dimensional V subspace identified with `ℂ⁷` via the column isometry `V_iso = char_basis(30)[:, V_idx]`:

```
H_V = diag(1, -1, 0, 0, 0, 0, 0)     (analog of λ_3 on 3×3)
P_1 = E_{0,1} + E_{1,0}                 (real symmetric off-diagonal)
P_2 = E_{1,2} + E_{2,1}
P_3 = E_{2,3} + E_{3,2}
P_4 = E_{3,4} + E_{4,3}
P_5 = E_{4,5} + E_{5,4}
P_6 = E_{5,6} + E_{6,5}
```

Six P_a operators total (`n_P = dim_V - 1 = 6`); all Hermitian traceless on the 7-dimensional V; all promoted to `ℂ³⁰` by `A_30 = V_iso · A_V · V_iso†`. The V-supported "energy" `H_30` and six V-supported "spatial momenta" `P_{a, 30}` parallel the choice in Paper 32 §13.2's `(H, P_1, P_2, P_3)` for `ℤ/6` (`n_P = 3` there because `dim_V = 3`).

### 2.3 M-supported simplex-mass proxy

```
m²_simplex(ρ) := Σ_{k ∈ M_idx} (⟨χ_k | ρ | χ_k⟩ - 1/30)²
```

Quadratic in deviations along the 22-dimensional M-diagonal of `ρ - ρ_*`; vanishes at the centroid `ρ_* = I_30/30`. Paper 20 §3 analog adapted to `ℤ/30`.

### 2.4 Dispersion-Casimir

```
I_complex(ρ) := ⟨H⟩²(ρ) + α² · (m²_simplex(ρ))² − Σ_{a=1}^{6} ⟨P_a⟩²(ρ)
```

with `α = 1`.

---

## 3. Audit triad — three checks at machine precision

### 3.1 Audit (A): Casimir along V-rays is exactly quadratic, m²_simplex ≡ 0 on V

For tangent vectors `X = V_iso · X_V · V_iso†` supported on V (i.e., `X_V ∈ Hermitian traceless 7 × 7`):

| Direction `X_V` | `t` | `I_real(ρ_* + tX)` | `I_complex(ρ_* + tX)` | `m²_simplex(ρ_* + tX)` | `I_real / t²` |
|---|---:|---:|---:|---:|---:|
| timelike (`H_V`) | 0.1 | 0.040000 | 0.040000 | 5.78e-34 | 4.000000 |
| spacelike (`P_1`) | 0.1 | −0.040000 | −0.040000 | 1.49e-33 | −4.000000 |
| mixed (`(H_V + P_1)/√2`) | 0.1 | −0.000000 | −0.000000 | 1.49e-33 | 0.000000 |

`I_real(ρ_* + tX) / t²` is constant in `t` for every V-direction tested (verified at `t = 0.001, 0.01, 0.05, 0.1`); `m²_simplex(ρ_* + tX) = 0` exactly to machine floor on V-rays (since V's character indices are disjoint from M's; the M-diagonal projection of any V-tangent direction vanishes algebraically).

**Result:** On V-rays, `I_complex = I_real` exactly; `I_real` is exactly quadratic in `t`; the Lorentzian signature established at 2nd order is the *exact* signature to all orders along V-rays.

### 3.2 Audit (B): Hessian of `I_real` on the 899-dim tangent space

The Hessian of `I_real(ρ) = ⟨H⟩²(ρ) − Σ_a ⟨P_a⟩²(ρ)` at `ρ_*` is computed on the 899-dim Hermitian-traceless basis of `T_{ρ_*} D(ℂ³⁰)` (generalized Gell-Mann basis with `tr(T_a T_b) = 2 δ_{ab}`); converted to orthonormal basis; diagonalized:

| Quantity | Value | Expected |
|---|---:|---:|
| Tangent-space dim | 899 | `30² − 1 = 899` ✓ |
| Hessian signature `(pos, neg, zero)` | **(1, 6, 892)** | (1, 6, 892) ✓ |
| Non-zero eigenvalues | `+4.0, -4.0, -4.0, -4.0, -4.0, -4.0, -4.0` | (1 positive, 6 negative) ✓ |
| V-Lorentzian sub-bundle dim | 7 | `1 + n_P = 7` ✓ |

The Hessian has signature `(1, 6, 892)` on the 899-dim tangent space. The **V-Lorentzian `(1, 6)` sub-bundle is 7-dimensional**, contained in V-supported tangent directions; the 892 zero-mode directions contain all M-supported tangent directions (and the V-traceless directions not spanned by `(H, P_a)`). The eigenvalue structure is symmetric in spacelike directions (six eigenvalues all equal to `-4.0`) because the six `P_a` choices yield isotropic spacelike contributions to the Casimir.

### 3.3 Audit (C): 4th-order quartic form `(m²_simplex)²` on M-diagonal

The leading-order content of the 4th-order quartic form `(m²_simplex(ρ_* + X))²` is captured by the *quadratic*-in-`X` form `m²_simplex(ρ_* + X)` itself (whose square is the quartic form, sharing the same kernel). The signature on the 899-dim `r`-space:

| Quantity | Value | Expected |
|---|---:|---:|
| `m²_simplex` quadratic-form signature `(pos, neg, zero)` | **(22, 0, 877)** | (22, 0, 877) ✓ |

Positive-semidefinite of rank `dim_M = 22`, supported on the 22-dim M-diagonal sub-bundle. The 4th-order quartic form `(m²_simplex)²` therefore has positive-semidefinite signature on the same 22-dim M-supported sub-bundle and vanishes elsewhere.

### 3.4 Audit (D): HS-orthogonality of V-Lorentzian and M-Euclidean sub-bundles

Eigenvectors of the Hessian with non-zero eigenvalues span the V-Lorentzian sub-bundle (7-dim); eigenvectors of the `m²_simplex` quadratic form with positive eigenvalues span the M-Euclidean sub-bundle (22-dim). The HS-overlap (singular values of `V_lorentz^† · M_pos`):

```
singular values: 5.82e-16, 3.48e-16, 1.98e-16, 1.42e-16, 1.13e-16, 9.91e-17, 7.70e-17
```

Max singular value: **`5.82 × 10⁻¹⁶`**. All seven singular values are below `EPS = 10⁻¹⁰` (machine-precision floor).

**The V-Lorentzian and M-Euclidean sub-bundles are HS-orthogonal at machine precision on `D(ℂ³⁰)`**.

---

## 4. The structural settlement

Under the three-outcome matched-pair discipline of Paper 35 §3.1 (v2insert-04 §3.1):

- **K-branch (the hybrid signature pattern extends).** **REALIZED.** All four audit predictions (V-rays exact, Hessian signature `(1, 6, 892)`, quartic signature `(22, 0, 877)`, HS-orthogonality at `5.82 × 10⁻¹⁶`) confirmed at machine precision.
- **L-branch (`ℤ/6` specific).** Not realized; the signature pattern extends cleanly to `ℤ/30`.
- **Joint-on-disjoint.** Not realized; no row-specific structural corrections were observed.

**Net:** Paper 46 (proposed) C5 *geometric realization on `D(ℂ^N)` for `N > 6`* promotes from [A] (queued Bures-Hessian sub-bundle audit) to **[P] on `D(ℂ³⁰)`**. The arithmetic substrate (V ⊥ M Hilbert-subspace decomposition, [P] on five primorial rows by audits α/η/θ + audit δ) and the geometric realization (V-Lorentzian + M-Euclidean HS-orthogonal sub-bundles, [P] on `D(ℂ⁶) + D(ℂ³⁰)`) are now jointly load-bearing.

---

## 5. Implications

### 5.1 Paper 46 (proposed) — C5 geometric realization extends to `D(ℂ³⁰)`

Paper 46 v0.1 reported the **arithmetic substrate** at [P] across five primorial rows and the **geometric realization** at [P] only on `D(ℂ⁶)`. After audit μ_30 (this audit), the geometric realization is also [P] on `D(ℂ³⁰)`. The universal-Wick-rotation reading (C3) gains its first row-generalization at the geometric tier: the conductor-6 carry packet `M` is *not* `ℤ/6`-specific; on `ℤ/30`, the cross-prime carry packets `M = H_6 ⊕ H_{10} ⊕ H_{15} ⊕ H_{30}` jointly play the same role at the Bures-Hessian tangent-sub-bundle level.

### 5.2 Paper 47 (proposed) — Theorem 3.1 (D2)–(D3) verified geometrically on `D(ℂ³⁰)`

Paper 47 Theorem 3.1's all-orders V/M decoupling (audit δ, [P] at all orders by Pontryagin character orthogonality) lifts cleanly to the **tangent-sub-bundle decomposition** of `D(ℂ³⁰)` at the centroid. Specifically:

- (D2): V-supported observables produce Hessian contributions supported on V-tangent directions. Verified: the V-supported `H, P_a` yield Hessian signature `(1, 6, 892)` with the non-zero eigenvalues confined to a 7-dimensional V-tangent sub-bundle.
- (D3): M-supported observables produce 4th-order quartic-form contributions supported on M-tangent directions. Verified: the M-supported `m²_simplex` yields a positive-semidefinite quadratic form of rank 22, confined to the 22-dim M-diagonal sub-bundle.
- (D4): The V-Lorentzian and M-Euclidean sub-bundles are HS-orthogonal. Verified at `5.82 × 10⁻¹⁶`.

### 5.3 Paper 48 (proposed) — capacity bound's structural foundation

The Capacity_V quantitative bound of Paper 48 (`pure_V / T_total` decay along the primorial ladder) rests on the V ⊥ M Hilbert-subspace decomposition and the cubic-self-closure pure-V triples count. The geometric realization on `D(ℂ³⁰)` does not change Paper 48's quantitative conclusions (those rely on integer arithmetic on the conductor lattice, not on the geometric tangent-sub-bundle structure), but it strengthens the **structural foundation**: the same V/M decomposition that bounds Capacity_V quantitatively also realizes the Hartle–Hawking geometric signature on the next primorial row.

---

## 6. Discipline check (Paper 35 §3 honored throughout)

- **Anchored objects (§3.3).** The conductor-lattice partition of `(ℤ/30)^∧` is integer arithmetic on the divisors of 30. The character basis is the DFT of `ℤ/30`. The V-supported `(H, P_a)` operators are constructed by promoting generalized-Gell-Mann generators on `ℂ⁷` via the column isometry. The Bures-Hessian basis on `T_{ρ_*} D(ℂ³⁰)` is the 899-element generalized-Gell-Mann basis with `tr(T_a T_b) = 2 δ_{ab}`. No reconstruction beyond what Paper 32 §6.2 + Paper 18 already specify; no synthesized data.
- **Deterministic, exact, reproducible (§3.4).** Pure linear algebra; numpy / LAPACK on a workstation; no seeds; no tolerances in any decision except the machine-precision floor `EPS = 10⁻¹⁰` (the floor itself is the floating-point limit). Total wall time **3.95 seconds**; deterministic on every re-run.
- **Three-outcome matched-pair (§3.1 + v2insert-04 §3.1).** K / L / joint-on-disjoint pre-claimed for Paper 46 C5. Realized as **K-branch** at the geometric tier on `D(ℂ³⁰)`.
- **No upward tier-crossing (§3.5).** The geometric realization on `D(ℂ³⁰)` is at [P] (deterministic float audit at machine floor). The universal-Wick-rotation reading (C3) is promoted from [C, reduced] (one-row-only) to [P]/[C, reduced] (two-row-confirmed, with C3 itself still [C, reduced] until the audit extends to `D(ℂ²¹⁰)` and beyond). The Hartle–Hawking structural-dictionary correspondence (C2) remains at [A] pending audit β (Lie-algebra-of-Wick-rotation check).
- **Failures-first-class (§3.6).** No failures. All four audit predictions confirmed at machine precision. The geometric realization on `D(ℂ²¹⁰)` (next primorial row) is queued; the `D(ℂ²³¹⁰)` and `D(ℂ³⁰⁰³⁰)` audits are larger compute (`2309²` and `30029²` Hessians, respectively) and deferred pending workstation memory budget.
- **Dimensional firewall (Paper 32 §11.2).** No physical units. No Planck length. No Newton constant `G`. No Bekenstein–Hawking temperature in K. Only dimensionless quantities: integer character indices, complex projector matrix elements, eigenvalues and singular values of dimensionless quadratic forms. The Hartle–Hawking correspondence is *correspondence language* per Paper 32 §11.1; this audit does not promote it.

---

## 7. Carry forward

| Audit | Status after audit μ_30 | Next step |
|---|---|---|
| **μ_30 (this audit)** | **SETTLED — K-branch on `D(ℂ³⁰)`** | — |
| μ_210 (geometric realization on `D(ℂ²¹⁰)`) | PENDING | Same machinery, `209² = 43681`-dim tangent space (`43681 × 43681` Hessian — `~ 7 GB` storage at float64, requires workstation memory budget) |
| μ_2310 (geometric on `D(ℂ²³¹⁰)`) | PENDING — large compute | `~ 5.3M`-dim tangent space; algebraic by audit δ |
| Audit β (Lie-algebra-of-Wick-rotation structural dictionary) | PENDING — finite Lie-algebra check | Promotes Paper 46 C2 from [A] to [P]-spirit |
| Audit γ (classical-limit identification) | PENDING | Take `m²_simplex → 0` in V-Lorentzian Casimir, verify Galilean parabolic dispersion |
| Audit κ (real-transformer V/M propagation, v2insert-05) | **DEFERRED** — needs GPU + HuggingFace | Paper 36 sweep; v2insert-07 §3 deferral active |

**Recommended next concrete move:** Either (a) audit β / γ on `D(ℂ⁶)` (pure mathematics, no compute), or (b) extending audit μ to `D(ℂ²¹⁰)` (CPU-tractable but `~ 7 GB` Hessian memory).

---

*Settlement record archived. Audit μ_30 — Bures-Hessian sub-bundle audit on `D(ℂ³⁰)` — settled at K-branch: Hessian signature `(1, 6, 892)` confirms V-Lorentzian `(1, 6)` sub-bundle of dim 7 on V-supported tangent directions; 4th-order quartic form `(m²_simplex)²` signature `(22, 0, 877)` confirms M-Euclidean positive-semidefinite sub-bundle of dim 22 on M-supported tangent directions; HS-orthogonality at `5.82 × 10⁻¹⁶` (machine precision). Paper 46 (proposed) C5 geometric realization promotes from [A] queued to [P] on the first two primorial rows (`D(ℂ⁶)` + `D(ℂ³⁰)`). The Hartle–Hawking signature pattern is row-stable at the geometric tier on the next primorial row. Total wall time: 3.95 seconds. Reproducibility artifact: [`empirical/paper46_bures_hessian_sub_bundle_audit_z30.py`](../paper46_bures_hessian_sub_bundle_audit_z30.py); transcript: [`empirical/paper46_bures_hessian_sub_bundle_audit_z30_run_output.txt`](../paper46_bures_hessian_sub_bundle_audit_z30_run_output.txt).*
