# Audits α + η — Settlement: Primorial-Row Generalization on `ℤ/30`

**Date:** 2026-05-20
**Audit script:** [`empirical/audits_alpha_eta_z30_primorial_generalization.py`](../audits_alpha_eta_z30_primorial_generalization.py)
**Deterministic transcript:** [`empirical/audits_alpha_eta_z30_primorial_generalization_run_output.txt`](../audits_alpha_eta_z30_primorial_generalization_run_output.txt)
**Tier:** **[P]** for all integer-arithmetic conductor/multiset counts (deterministic, integer-only in every membership/vanishing decision); **[P]** for the projector idempotence, hermiticity, and `V ⊥ M` overlap (floating-point only in the reporting step; the orthogonality follows algebraically from Pontryagin character orthogonality on `(ℤ/N)^∧`); **[K-branch realized]** for each of Papers 46 C5, 47 C3, 48 C2 under the v2insert-04 §3.1 three-outcome matched-pair rule.

---

## 1. Audit scope

Single deterministic compute pass on `R = ℤ/30 = 2·3·5` (next squarefree primorial after `ℤ/6`). Settles, simultaneously and at machine precision in the deterministic arithmetic, the row-generalization claims of three proposed papers staged in v2inserts 01, 02, 03:

| Item | Origin | Pre-claim (three-outcome, v2insert-04 §3.1) |
|---|---|---|
| Paper 48 **C2** | v2insert-03 §2.3 (Conductor Capacity Bound enumeration on the primorial ladder) | K: `Capacity_V < 1/3` (monotone decrease) / L: ≈ 1/3 / joint-on-disjoint: > 1/3 |
| Paper 47 **C3** | v2insert-02 §1 (Arithmetic Decoupling Theorem extends to higher CRT rows) | K: `V ⊥ M` at machine precision / L: structural overlap / joint-on-disjoint: partial overlap at some conductor pair |
| Paper 46 **C5** | v2insert-01 §2.3 (Hartle–Hawking signature's arithmetic substrate extends) | K (partial): the V/M decomposition with the predicted character exists / L: row-specific to `ℤ/6` / joint-on-disjoint: V/M structurally inverted |

---

## 2. Anchor verification (`ℤ/6`, Paper 32 Corollary 6.1d)

The audit runs on `ℤ/6` first as anchor (Paper 35 §3.3 anchored-objects). All Paper 32 §6.2 / Corollary 6.1d numbers reproduce exactly:

| Quantity | Paper 32 reference | Observed |
|---|---|---|
| `dim_V` (= `dim H_2 + dim H_3`) | 1 + 2 = 3 | **3** ✓ |
| `dim_M` (= `dim H_6`) | 2 | **2** ✓ |
| total closing unordered multisets on `{1,…,5}`, sum ≡ 0 mod 6 | 6 (Lemma 6.1) | **6** ✓ |
| pure-V multisets (= pure-A₃ self-closure) | 2 (Cor 6.1d.1: `{2,2,2}`, `{4,4,4}`) | **2** ✓ |
| `\|V_proj · M_proj\|_F` | 0 (Pontryagin character orthogonality, Lemma 6.1a–c) | `1.14e-15` ✓ (machine floor) |

Anchor passes. Audit proceeds.

---

## 3. `ℤ/30` results

### 3.1 Conductor lattice (anchored, Paper 32 §6.1 / Pontryagin theory)

Conductor of `k`: `c(k) = 30 / gcd(k, 30)`. Packets `H_d = {k : c(k) = d}`. All `|H_d| = φ(d)` checked.

| `d` | `H_d` indices | `\|H_d\|` | `φ(d)` | Class |
|---:|---|---:|---:|---|
| 1 | `{0}` | 1 | 1 | gauge (excluded) |
| 2 | `{15}` | 1 | 1 | **single-prime (V)** |
| 3 | `{10, 20}` | 2 | 2 | **single-prime (V)** |
| 5 | `{6, 12, 18, 24}` | 4 | 4 | **single-prime (V)** |
| 6 | `{5, 25}` | 2 | 2 | **cross-prime (M)** |
| 10 | `{3, 9, 21, 27}` | 4 | 4 | **cross-prime (M)** |
| 15 | `{2, 4, 8, 14, 16, 22, 26, 28}` | 8 | 8 | **cross-prime (M)** |
| 30 | `{1, 7, 11, 13, 17, 19, 23, 29}` | 8 | 8 | **cross-prime (M)** |

`dim_V = 7`, `dim_M = 22`, `dim_dynamical = 29 = 7 + 22` ✓.

### 3.2 Closing-multiset enumeration on `{1, …, 29}` with `k + ℓ + m ≡ 0 (mod 30)`

| V/M content | Count | % of total |
|---|---:|---:|
| `VVV` (pure-V) | **6** | 4.00% |
| `MVV` | 14 | 9.33% |
| `MMV` | 66 | 44.00% |
| `MMM` (pure-M) | 64 | 42.67% |
| **Total** | **150** | 100.00% |

**The six pure-V closing multisets:**

| Multiset | Sum | Reading |
|---|---:|---|
| `(6, 6, 18)` | 30 | All three legs in `H_5` |
| `(6, 12, 12)` | 30 | All three legs in `H_5` |
| `(10, 10, 10)` | 30 | All three legs in `H_3` |
| `(12, 24, 24)` | 60 | All three legs in `H_5` |
| `(18, 18, 24)` | 60 | All three legs in `H_5` |
| `(20, 20, 20)` | 60 | All three legs in `H_3` |

Observation: all six are *pure-single-conductor* triples (either all-`H_5` or all-`H_3`). **No pure-V multiset mixes single-prime packets.** This is a structural feature of the primorial decomposition: V-cubic self-closure on each `H_p` is independent and the cross-`H_p` triples (e.g., (`H_5`, `H_5`, `H_3`)) cannot close to 0 mod `p_1·p_2·p_3` without an `H_{p_i p_j}` leg (which is M, by definition). Pure-`H_2` (which is just `{15}`) gives no closing triple because `15 + 15 + 15 = 45 ≡ 15 ≠ 0 (mod 30)` — the exact analog of Paper 32 Corollary 6.3 (L1) (pure-`A_2` cubic vacuity on `ℤ/6` via `3+3+3 = 9 ≢ 0 mod 6`). **Same arithmetic root**, generalized to the next primorial.

### 3.3 Pontryagin character orthogonality

| Quantity | Value | Interpretation |
|---|---:|---|
| `V_proj` rank | 7.000000 | matches `dim_V` ✓ |
| `M_proj` rank | 22.000000 | matches `dim_M` ✓ |
| `\|V_proj² − V_proj\|_F` | 5.31e-15 | idempotence ✓ |
| `\|V_proj^† − V_proj\|_F` | 1.94e-16 | hermiticity ✓ |
| `\|M_proj² − M_proj\|_F` | 2.33e-14 | idempotence ✓ |
| `\|M_proj^† − M_proj\|_F` | 4.13e-16 | hermiticity ✓ |
| **`\|V_proj · M_proj\|_F`** | **1.22e-14** | **`V ⊥ M` to machine precision** ✓ |

The character index sets of V (`{6, 10, 12, 15, 18, 20, 24}`) and M (the 22 indices in `H_6 ∪ H_10 ∪ H_15 ∪ H_30`) are disjoint subsets of `{0, …, 29}`. By Pontryagin character orthogonality `⟨χ_k | χ_ℓ⟩ = δ_{k,ℓ}` on `(ℤ/30)^∧`, the projectors are orthogonal as operators. The floating-point overlap `1.22e-14` is the machine-precision floor of the matrix multiplication; the algebraic content is **exactly zero**.

---

## 4. Adjudication of pre-registered branches

### 4.1 Paper 48 C2 — Conductor Capacity Bound

| Row | `Capacity_V` = pure-V / total | Notes |
|---|---:|---|
| `ℤ/6` (Paper 32 anchor) | **2/6 = 0.333333** | matches Cor 6.1d.1 |
| `ℤ/30` (this audit) | **6/150 = 0.040000** | strict decrease |

**Realized branch: K** (`Capacity_V(ℤ/30) < Capacity_V(ℤ/6)` strictly). Monotone decrease on the primorial ladder; ratio shrinks by a factor of **8.3×** in one primorial step (1/3 → 1/25). v2insert-03 §1.3 structural prediction confirmed.

### 4.2 Paper 47 C3 — Arithmetic Decoupling Theorem extends to `ℤ/30`

`\|V_proj · M_proj\|_F = 1.22e-14` (machine floor). V and M sub-Hilbert-spaces of `ℂ^30` are HS-orthogonal at machine precision; Pontryagin character orthogonality on the conductor-2/3/5/6/10/15/30 packet partition forces the orthogonality algebraically.

**Realized branch: K** (Arithmetic Decoupling Theorem extends to the next primorial row at the conductor-lattice level). v2insert-02 §1 conjecture C3 elevated from [A] to [P] on `ℤ/30`.

### 4.3 Paper 46 C5 — Hartle–Hawking signature's arithmetic substrate

The V/M decomposition exists on `ℤ/30` with the predicted character: three single-prime axes (H_2, H_3, H_5) playing the V role; four cross-prime carry packets (H_6, H_10, H_15, H_30) playing the M role; V ⊥ M by Pontryagin (§4.2).

**Realized branch: K (partial — arithmetic substrate only).** The full empirical generalization of audit κ to a `ℤ/30`-shaped categorical task on real transformers remains **deferred** (requires GPU + HuggingFace access; see [`v2insert-07.md`](../../v2insert-07.md)). At the arithmetic-substrate level — which is what v2insert-01 §2.3 C5 pre-claims — the Hartle–Hawking-style V/M decomposition is realized cleanly on `ℤ/30`.

---

## 5. Compact summary

| Row | `dim_V` | `dim_M` | total multisets | pure-V | `Capacity_V` | `\|V ⊥ M\|_F` |
|---|---:|---:|---:|---:|---:|---:|
| `ℤ/6` | 3 | 2 | 6 | 2 | **0.333333** | 1.14e-15 |
| `ℤ/30` | 7 | 22 | 150 | 6 | **0.040000** | 1.22e-14 |

---

## 6. Implications for the proposed Papers 46/47/48

- **Paper 48 (Conductor Capacity Bound).** C2 settled with K-branch on `ℤ/30`. Capacity ratio drops by 8.3× per primorial step (1/3 → 1/25); v2insert-03 §1.3's "decays rapidly with primorial growth" prediction is confirmed quantitatively. The structural *shape* of the decay (matches Bekenstein–Hawking holographic saturation in being faster than linear-in-bulk) is now verified on two data points (`ℤ/6` and `ℤ/30`); audit θ extending to `ℤ/210`, `ℤ/2310` will fix the scaling exponent.

- **Paper 47 (Arithmetic Decoupling Theorem).** C3 settled with K-branch on `ℤ/30`. Pontryagin character orthogonality on `(ℤ/30)^∧` forces V ⊥ M as Hilbert subspaces (and by inheritance, as HS-orthogonal sub-bundles of the tangent space at the centroid of `D(ℂ^30)`, by the same argument as Paper 32 §13.2B). The all-orders extension (audit δ) is a separate undertaking; the **row-generalization** dimension is now closed at K.

- **Paper 46 (Hartle–Hawking No-Boundary Lift).** C5 settled with K-branch (partial — arithmetic substrate). The V/M decomposition exists on `ℤ/30` with the predicted V = single-prime axes + M = cross-prime carry character. The full geometric realization of the Hartle–Hawking signature on `D(ℂ^30)` requires the §13.2B-style Bures-Hessian sub-bundle audit on the 899-dim tangent space of `D(ℂ^30)`; this is a separate compute and is queued.

---

## 7. Methodological notes (Paper 35 discipline)

- **Anchored objects (§3.3).** `ℤ/6` anchors reproduced to exact integer match against Paper 32 Cor 6.1d.1 (dim_V=3, dim_M=2, total=6, pure-V=2 with explicit multisets `{2,2,2}` and `{4,4,4}`). No reconstruction beyond what Paper 32 §6.2 already enumerates.

- **Deterministic, exact, reproducible (§3.4).** Pure integer arithmetic in every multiset enumeration and packet membership decision; integer GCD for conductor computation; floating-point only in the Pontryagin overlap report (`1.22e-14`, at machine floor). No seeds. No tolerances except the conventional floor convention `< 1e-10` for the Pontryagin-orthogonality claim, which itself is exact algebraically (Pontryagin character orthogonality on the dual group `(ℤ/30)^∧`).

- **Three-outcome matched-pair (v2insert-04 §3.1).** Each of Papers 46 C5 / 47 C3 / 48 C2 had K / L / joint-on-disjoint pre-claimed in v2inserts 01/02/03. All three returned **K-branch**. No silent absorption of a different outcome.

- **No upward tier-crossing (§3.5).** The conductor-lattice arithmetic counts (V/M dimensions, multiset counts, pure-V counts, capacity ratios) are reported at [P]. The Pontryagin orthogonality, while at machine-floor in the floating-point report, is at [P] *algebraically* by Pontryagin character orthogonality on a finite cyclic dual group (a standard result). The structural-correspondence claims (Hartle–Hawking signature, QG-mixing-bypass, Bekenstein–Hawking holographic shape) remain at [C, reduced] — this audit does not promote them; it only confirms the row-generalization of the *arithmetic substrate* on which those structural-correspondence claims rest.

- **Failures-first-class (§3.6).** No failures in this audit. Paper 46 C5's geometric companion (the full `D(ℂ^30)` Bures-Hessian audit) and Paper 47's all-orders extension (audit δ) remain queued; their non-execution in this run is **stated** here as a scope boundary, not hidden.

- **Dimensional firewall (Paper 32 §11.2).** Only structural dimensionless quantities reported: integer counts, ratios of integer counts, projector ranks (=dimensions), HS-norm floors. No physical units. No Planck scale. No Newton constant. No horizon area. No mass-shell asymptote magnitude. The Hartle–Hawking / QG-mixing-bypass / Bekenstein–Hawking external correspondences are *correspondence language only* (§11.1 emergent-gravity positioning); the program does not derive physical cosmology, physical QG, or physical holographic principle.

---

## 8. Carry forward (queued audits)

| Audit | Settles | Status after this run |
|---|---|---|
| α (this audit) | Paper 47 C3 row-generalization on `ℤ/30` | **SETTLED — K-branch** |
| η (this audit) | Paper 48 C2 capacity count on `ℤ/30` | **SETTLED — K-branch** |
| C5 substrate (this audit) | Paper 46 C5 row-generalization at arithmetic level | **SETTLED — K-branch (partial; geometric realization deferred)** |
| δ (Paper 47) | All-orders Pontryagin character-orthogonality proof | **PENDING** — pure mathematics, not new compute. Would promote Paper 47 C1 to [P] at all orders. |
| ε (Paper 47) | Structural-dictionary Lie-algebra QG-decoupling check | **PENDING** |
| θ (Paper 48) | `Capacity_V` scaling on `ℤ/210`, `ℤ/2310`, … | **PENDING** — extends this audit; one additional run per primorial row, each runtime < 1 second on this script's machinery. |
| ι (Paper 48) | Bousso-bound shape comparison vs `Capacity_V` decay | **PENDING** — pure mathematics, no new compute. |
| κ (Paper 47, Paper 46) | Llama / Mistral V/M propagation on `ℤ/30`-shaped task | **DEFERRED** — requires GPU + HuggingFace + a `ℤ/30` cyclic-task corpus; see v2insert-07. |
| λ (Paper 47) | Cross-support replication at `S = {6, 12}` on `ℤ/6` MLP sweep | **PENDING** — see v2insert-06 §8 / v2insert-07 carry-forward. |
| λ-`ℤ/30` (Paper 47) | Training-side MLP sweep on a `ℤ/30` task | **DEFERRED** — requires acquiring or constructing a `ℤ/30` cyclic-task corpus. |

## 9. The arithmetic-root coherence count, now extended

Paper 32 §6.2A Corollary 6.3 named four threads on `ℤ/6`. v2insert-02 added a fifth (V/M sub-bundle decoupling), v2insert-03 added a sixth (Conductor Capacity Bound), v2insert-05/06 brought Papers 36 and 37 into the same family. **This audit extends the threads to `ℤ/30`:**

| Thread | `ℤ/6` instance | `ℤ/30` instance (this audit) |
|---|---|---|
| Pure-V cubic vacuity (the `3+3+3 ≢ 0 mod 6` arithmetic root) | (L1) of Cor 6.3 | `15 + 15 + 15 = 45 ≡ 15 ≠ 0 (mod 30)` — same arithmetic shape; pure-`H_2` self-closure forbidden |
| Conductor packet partition by Pontryagin character orthogonality | Paper 32 Lemma 6.1a–c | extended cleanly to 8 conductor packets on `ℤ/30` (all `\|H_d\| = φ(d)` verified) |
| V/M arithmetic decoupling | v2insert-02 (Paper 47 C1) | **V ⊥ M to machine precision** (this audit §3.3) |
| Conductor Capacity Bound | v2insert-03 (Paper 48 C2; 2/6 = 1/3) | **6/150 = 1/25** (this audit §3.2) |

Six independent corpus results (Y′-negative, color-protection of the chirality bit, FEP-3 sector resolution, C2 conductor-misspecification certificate, V/M decoupling, Conductor Capacity Bound) on `ℤ/6` standing on the same arithmetic root *also* generalize to `ℤ/30` at the structural level. The structural prediction is row-stable across at least one primorial step.

---

*Settlement record archived. Audits α + η on `ℤ/30` settled with K-branch realization across all three pre-registered claims (Papers 46 C5, 47 C3, 48 C2). Paper 35 §3 discipline honored throughout; no tier-crossing, no silent absorption, no anchor failure. Reproducibility artifact and deterministic transcript both archived under `empirical/`.*
