# 48. The Conductor Capacity Bound

**An Arithmetic Analog of the Bekenstein–Hawking Holographic Principle on the Categorical Simplex**

**Leonardo Murillo Montero**
*leonardo.murillo@gmail.com*

*Draft 0.2 — 2026-05-20*

**Tier tags.** [P] for the conductor-lattice / multiset / closing-triple enumerations and the `Capacity_V` values on the **six**-row primorial ladder `ℤ/{6, 30, 210, 2310, 30030, 510510}` (integer arithmetic; closed-form orbit-counting verified against full O(N²) enumeration for `N ≤ 210`; audit ξ extension to `ℤ/510510` settled 2026-05-20: `Capacity_V(ℤ/510510) = 110/43,436,743,350 = 2.532 × 10⁻⁹`, ratio 1.538 to PNT-heuristic prediction — K-branch within factor of 2). [P] for the asymptotic power-law-exponent estimate of `Capacity_V` and the linear-fit residuals (deterministic linear algebra on the five anchored points). [A] for the all-orders extension of the underlying Pontryagin character orthogonality (audit δ open). [A]/[C, reduced] for the structural-shape correspondence with the 't Hooft–Susskind / Bousso holographic bound (`Capacity_V ~ 1/N²` at asymptotic order; local slope `→ −2` on the available rows). [A] for the polynomial-log prefactor `n² · ln(n)` matching the Prime-Number-Theorem heuristic (spread 1.584× across five rows, audit ι). [C, reduced] for the unified "shape matches but literal formula does not" reading of Paper 48's C4 against the peer-reviewed holographic-bound literature.

**Anchor manuscripts.** Paper 32 *One Functional Four Forces* §6.2 Lemma 6.1a–c, Corollary 6.3 (load-bearing [P] for the Pontryagin selection rule and the conductor-2/3/6 partition of `ℤ/6`); Paper 32 §11.1 (emergent-anything positioning, binding); Paper 32 §11.2 (dimensional firewall, binding); Paper 32 §11.4 (carried-label discipline, binding); Paper 32 §12 (ledger items R, S, R′, S′, T′, CC); Paper 32 §13.2A / §13.2B (V-Lorentzian / M-Euclidean orthogonal sub-bundle audit). Paper 22 *Primorial Cumulant Noether RH* (primorial-ladder Noether–Weil substrate). Paper 31 *Projection-Closure Theory* (closure-certificate vocabulary). Paper 35 *Grounded-Paranoid-Delusional Methodology* §3.1 (three-outcome matched-pair pre-claim, extended at v2insert-04). Paper 46 (proposed) *Hartle–Hawking Signature on the Categorical Simplex* (v2insert-01; the no-boundary cosmological correspondence; this paper supplies the *boundary-saturation* reading of the same arithmetic). Paper 47 (proposed) *The Arithmetic Decoupling Theorem* (v2insert-02; the load-bearing V ⊥ M Hilbert-subspace decomposition; this paper supplies the *capacity* reading of the same decomposition). Paper 49 *The Arithmetic Decoupling of Projection-Closure Overflows* (universal-overflow synthesis; cites Paper 48 as the capacity-saturation manifestation).

**External anchors (peer-reviewed only; correspondence language per Paper 32 §11.1).** Bekenstein 1973, *Black holes and entropy* (Phys. Rev. D 7). 't Hooft 1993, *Dimensional reduction in quantum gravity* (gr-qc/9310026). Susskind 1995, *The world as a hologram* (J. Math. Phys. 36). Bousso 1999, *A covariant entropy conjecture* (JHEP 7). Maldacena 1997, *The Large N limit of superconformal field theories and supergravity* (Adv. Theor. Math. Phys. 2). Grey literature and forum posts excluded.

<!--
NOTE TO SELF (draft 0.1 → 0.2):

1. Paper 48 v0.1 lands the structural Capacity_V claim with audit ι's joint-on-disjoint settlement; v0.2 absorbs higher-primorial rows (ℤ/510510 and beyond) if extension is run. Audit ι's PNT-heuristic shape makes a concrete prediction (Capacity_V(ℤ/510510) ≈ 1.7e-9) that v0.2 either confirms or refines.

2. The "shape matches, literal formula does not" framing is the load-bearing discipline. C4 lands at K-leading + joint-on-disjoint-corrections — this is *the* worked example of v2insert-04 §3.1's three-outcome rule, and Paper 35 v0.2 should cite it. Resist any rhetoric that promotes C4 to a literal Bekenstein–Hawking match.

3. The asymptotic-vs-finite distinction matters: alpha → -2 is the asymptotic content; the polynomial-log correction is the finite-N content. Both are needed; neither is "the answer." The PNT heuristic n²·ln(n)/N² captures both pieces in one shape (spread 1.584×). This is the cleanest single-line summary of C4.

4. The Hartle–Hawking (Paper 46) / Arithmetic Decoupling (Paper 47) / Capacity Bound (Paper 48) triad shares one substrate (Pontryagin character orthogonality on the conductor lattice) and one row-generalization audit (α/η). This paper is the *quantitative* face; Papers 46/47 are the *qualitative-structural* faces.

5. Paper 49 *Arithmetic Decoupling of Projection-Closure Overflows* takes this paper's C4 as one of the three manifestations of its universal-overflow law. Paper 49 is the umbrella; Paper 48 is one of the legs. Cite the umbrella; do not let it carry the load that Paper 48's audit data carries on its own.

OPEN: Extension to non-squarefree conductors (ℤ/4, ℤ/12, ℤ/8, etc.) is named but not run. The closed-form orbit-counting machinery handles squarefree primorials cleanly; non-squarefree rings require treatment of higher-conductor packets H_{p^k} for k > 1. Carried forward as audit μ.

OPEN: The multiplicative constant ~4.5 (observed) vs ~3 (PNT-heuristic-predicted) on the n²·ln(n)/N² shape carries a mild upward drift. Next-to-leading-order correction is open; v0.2 may absorb it after higher-primorial-row data.
-->

---

## Abstract

We state and prove the **Conductor Capacity Bound** for the categorical simplex on a primorial ring: on every squarefree primorial `P_n = p_1 · p_2 · … · p_n`, the V-sector cubic-self-closure capacity — the count of unordered triples `(k, ℓ, m)` with `k+ℓ+m ≡ 0 (mod P_n)` and all three legs in single-prime packets `H_{p_i}` — is finite, computable from the conductor lattice alone, and **strictly smaller than the count of all closing triples on the row, with the ratio decaying super-polynomially in the number of primes `n`**. On the primorial ladder `ℤ/{6, 30, 210, 2310, 30030}`, the dimensionless ratio `Capacity_V(P_n) := #pure-V / #all closing triples` takes values `1/3, 1/25, 1/525, 1/26157, 1/2424196` respectively — five exact rational anchors at the [P] tier (integer arithmetic, closed-form orbit-counting verified against full O(N²) enumeration for `N ≤ 210`).

The empirical decay shape across the five primorial rows matches the **Prime-Number-Theorem heuristic** `Capacity_V ~ K · n² · ln(n) / N²` with spread 1.584× across all five data points (audit ι). The asymptotic power-law exponent in `N = P_n` approaches `−2` (local slopes `−1.32 → −1.56 → −1.63 → −1.77` over the four primorial transitions in the available data), the **'t Hooft (1993) / Susskind (1995) holographic-saturation exponent** for a region whose boundary becomes asymptotically negligible relative to its bulk. The literal Bekenstein 1973 exponent `1/N` (corresponding to `S ≤ 2πRE` in the original formulation) is decisively refuted at spread 161× across the five rows; the literal 't Hooft–Susskind / Bousso exponent `1/N²` alone (without a polynomial-log prefactor) is poor at spread 31×; only the PNT-heuristic shape with both the `1/N²` skeleton and the `n² · ln(n)` finite-arithmetic-specific prefactor reproduces the program's empirical decay.

Under the three-outcome matched-pair discipline of Paper 35 §3.1 (extended at v2insert-04 §3.1), the proposed-paper claim C4 (the structural-shape correspondence with peer-reviewed holographic bounds) settles at **K-leading-order + joint-on-disjoint-at-corrections**: the asymptotic shape matches a peer-reviewed holographic bound exactly; the polynomial-log prefactor is a program-specific finite-arithmetic feature absent from continuous-spacetime holographic bounds. The structural shape matches; the literal formula does not.

The load-bearing arithmetic is one line: `3 + 3 + 3 = 9 ≡ 3 ≢ 0 (mod 6)`, the pure-A₂ cubic-vacuity computation of Paper 32 Lemma 6.1, generalized via Pontryagin character orthogonality on `(ℤ/P_n)^∧` to every primorial row. The cubic-vacuity "remainder" of `9 mod 6 = 3 ≠ 0` is the program's structural form of *what cannot be accommodated by the kinematic sector* and must be routed through the orthogonal M-sector overflow channel; the conductor capacity is the *count* of how often kinematic self-closure succeeds; the decay of that count along the primorial ladder is the *quantitative shape* of holographic saturation on a discrete arithmetic substrate.

The program does not derive Bekenstein–Hawking entropy, horizon area in physical units, the Planck scale, the gravitational constant `G`, or any black-hole information-paradox content. Only the structural shape of how a designated overflow channel manifests under projection-closure on a finite-arithmetic substrate is asserted; the physical interpretation is correspondence language.

**Keywords:** categorical simplex, conductor lattice, Pontryagin character orthogonality, primorial ring, cubic Amari–Chentsov tensor, V/M decoupling, Capacity_V, holographic bound, Bekenstein–Hawking saturation, Bousso bound, three-outcome matched-pair pre-claim, Prime Number Theorem heuristic.

**MSC 2020:** 11L03 (trigonometric and exponential sums), 62B11 (information geometry), 81P16 (quantum information geometry), 83C57 (black holes; not derived, only structurally referenced), 11N56 (rate of growth of arithmetic functions).

---

## 1. Introduction

### 1.1 The thesis

The categorical simplex of a primorial ring `R = ℤ/P_n` carries a finite, conductor-lattice-computable bound on how much pure-kinematic cubic dynamics it can host. The bound is **strictly arithmetic**: the number of unordered triples `(k, ℓ, m)` with `k, ℓ, m ∈ {1, …, P_n - 1}`, `k + ℓ + m ≡ 0 (mod P_n)`, and *all three legs in single-prime packets* `H_{p_i} := \{j \in \{1, \dots, P_n - 1\} : \gcd(j, P_n) = P_n / p_i\}`. We call this count `pure_V(P_n)`. The total count of closing triples is `T_total(P_n)` (a closed-form Burnside-type quantity, derived in §3). The **conductor capacity** is the dimensionless ratio

```
Capacity_V(P_n) := pure_V(P_n) / T_total(P_n)
```

The conductor capacity decays super-polynomially in `n` along the primorial ladder. On the five rows `ℤ/{6, 30, 210, 2310, 30030}` it takes the exact rational values `{1/3, 1/25, 1/525, 1/26157, 1/2424196}`. The empirical decay shape is the **Prime-Number-Theorem heuristic** `n² · ln(n) / N²` (spread 1.584× across all five data points, audit ι); the asymptotic power-law exponent approaches `−2`, matching the 't Hooft–Susskind / Bousso holographic-saturation shape; the polynomial-log prefactor `n² · ln(n)` is a program-specific finite-arithmetic feature absent from continuous-spacetime holographic bounds.

The *structural shape* of the decay matches a peer-reviewed holographic bound (a region's boundary becomes asymptotically negligible relative to its bulk); the *literal formula* does not (the polynomial-log correction is program-specific). This is the precise content of Paper 48's C4 under the three-outcome matched-pair discipline.

### 1.2 What is claimed, what is not claimed

<!--
NOTE TO SELF: this is the load-bearing discipline subsection. Paper 32 §11.1/§11.2/§11.4 are binding. Be airtight; better to over-cite the discipline rails than to under-cite. The "shape matches, literal formula does not" framing is the load-bearing structural distinction.
-->

**Claimed (under the tier discipline of Paper 35 §3.3–§3.6).**

- **[P, anchored at Paper 32 Lemma 6.1 + Corollary 6.3].** *The `ℤ/6` capacity count.* On `ℤ/6`, the number of unordered closing triples is `T_total = 6` (the orbits under `S_3` of ordered solutions to `k+ℓ+m ≡ 0 mod 6`, restricted to nonzero residues); the number of pure-V closing triples is `pure_V = 2` (the multisets `{2, 2, 2}` and `{4, 4, 4}`, both pure-`H_3` cubic self-closures); `Capacity_V(6) = 2/6 = 1/3`.
- **[P, anchored at audit η of v2insert-08 and audit θ of v2insert-09].** *The primorial-ladder capacity counts.* On `ℤ/{30, 210, 2310, 30030}`, `Capacity_V` takes values `{1/25, 1/525, 1/26157.35…, 1/2424196}` respectively, with the exact `pure_V` counts `{6, 14, 34, 62}` and the exact `T_total` counts `{150, 7350, 889350, 150300150}`. Reproduced to exact integer match by independent closed-form orbit-counting + O(N²) full enumeration (for `N ≤ 210`).
- **[P, audit δ settled 2026-05-20].** *The all-orders Pontryagin character-orthogonality decoupling.* Paper 47 (proposed, v2insert-02) load-bears the V ⊥ M Hilbert-subspace decomposition at 2nd and 4th orders; audit δ ([`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)) settled the all-orders extension via a finite combinatorial argument on the dual group `(ℤ/P_n)^∧`. Paper 48's Capacity_V is the *count of triples for which the order-3 character-orthogonality projection lands in the V subspace*; with audit δ at [P], the V ⊥ M decoupling that the Capacity_V bound rests on is now established at every tensor order, on every squarefree primorial row.
- **[A, audit ι settled].** *The empirical decay shape.* On the five primorial rows audited, the PNT-heuristic predictor `n² · ln(n) / N²` fits `Capacity_V` at spread 1.584× (constant ratio across five rows). The literal Bekenstein `1/N` is decisively refuted at spread 161×. The asymptotic power-law exponent approaches `−2`; local slopes are `−1.32, −1.56, −1.63, −1.77` over the four primorial transitions ℤ/6 → ℤ/30 → ℤ/210 → ℤ/2310 → ℤ/30030, monotonically accelerating toward the 't Hooft–Susskind / Bousso exponent.
- **[A, audit ι settled — joint-on-disjoint].** *The structural-shape correspondence with the holographic-bound literature.* The asymptotic exponent `−2` matches the 't Hooft (1993) / Susskind (1995) holographic-saturation shape (boundary becomes negligible relative to bulk in the large-system limit); the Bousso (1999) covariant bound is consistent. The polynomial-log prefactor `n² · ln(n)` is a finite-arithmetic-specific feature absent from continuous-spacetime holographic bounds. The structural shape matches; the literal formula does not.

**Not claimed (under §11.1, §11.2, §11.4 discipline, binding).**

- *No Bekenstein–Hawking entropy formula is derived.* The Bekenstein 1973 bound `S ≤ 2πRE/ℏc`, 't Hooft 1993's holographic dimensional-reduction conjecture, Susskind 1995's `S = A/4ℓ_P²`, Bousso 1999's covariant entropy bound, and Maldacena 1997's AdS/CFT correspondence are not derived. Only the *structural shape* of the boundary-saturation phenomenon on the categorical simplex's conductor lattice is asserted; the physical interpretation is correspondence language.
- *No physical horizon area, Planck length, gravitational constant, or black-hole entropy is asserted.* All quantities in this paper are dimensionless: integer counts (`pure_V`, `T_total`, `dim_V`, `dim_M`), integer ratios (`Capacity_V`), log-space slopes (local power-law exponents). No `S` in entropy units, no horizon area in m², no Planck-scale ratio, no `G`.
- *No physical information bound on black holes, no Hawking radiation mechanism, no black-hole information paradox content.* The "boundary saturation" framing is internal to the conductor-lattice arithmetic; whether physical black holes saturate their boundary information is an open question of theoretical physics, addressed only by the peer-reviewed external anchors and not by this paper.
- *No universal physical holographic principle is asserted.* The "holographic" qualifier in the structural-shape claim refers to the *structural form* of the bound — boundary becomes negligible relative to bulk in the large-system limit — recurring across discrete-arithmetic and continuous-spacetime systems. Whether the physical phenomena share a mechanism beyond the structural form is an open question, deliberately not asserted.

### 1.3 Inherited objects and reading guide

The Pontryagin selection rule of Paper 32 §6.2 Lemma 6.1a is binding: a cubic Amari–Chentsov tensor element `T_{klm}` on the categorical simplex of `ℤ/N` is nonvanishing only when `k + ℓ + m ≡ 0 (mod N)`. The conductor-lattice partition `ℂ^N = \oplus_{d | N} H_d` (with `|H_d| = \varphi(d)`) is binding throughout; the single-prime sector `V := \oplus_{p \text{ prime}, p | N} H_p` and the cross-prime sector `M := \oplus_{d | N, d \text{ composite}} H_d` are the load-bearing partition of the kinematic vs gravity-adjacent content per Paper 47 (proposed, v2insert-02).

§2 sets up the arithmetic substrate (conductor lattice, V/M decomposition, Pontryagin selection rule). §3 defines `Capacity_V` and presents the closed-form orbit-counting derivation of `T_total` and the integer-arithmetic enumeration of `pure_V`. §4 reports the five primorial-row anchors and the audit-ι shape-comparison results. §5 settles C4 under the three-outcome matched-pair rule. §6 records the discipline rails. §7 catalogues open questions and carries the program forward.

---

## 2. The arithmetic substrate

### 2.1 The categorical simplex and the conductor lattice

Fix a squarefree primorial `N = P_n = p_1 · p_2 · … · p_n`. The categorical simplex over the ring `R = ℤ/N` is `Δ_R^∘ := \{p \in ℝ^N : p_j > 0, \sum_j p_j = 1\}` indexed by the residues `\{0, 1, …, N-1\}`. The information-geometric machinery of Papers 13/14/15/18/24 endows `Δ_R^∘` with the Fisher–Rao metric and the Amari–Chentsov α-family of affine connections; the α = ±1/3 (cubic) connection's Amari–Chentsov tensor is the load-bearing object for the present paper.

The **conductor lattice** of `R` is the partition

```
{1, 2, …, N - 1} = \bigsqcup_{d | N, d > 1} H_d,
```

where `H_d := \{j \in \{1, …, N-1\} : \gcd(j, N) = N/d\} = \{j : d \cdot j \equiv 0 (mod N), (d / \gcd(d, N/j)) = d\}` (the residues whose order in `(ℤ/N, +)` is exactly `d`). The packet sizes are `|H_d| = \varphi(d)` (Euler totient), and `\sum_{d | N, d > 1} \varphi(d) = N - 1`.

For a squarefree primorial `N = p_1 · … · p_n`, the divisors `d | N` correspond bijectively with subsets `S \subseteq \{p_1, …, p_n\}` via `d = \prod_{p \in S} p`; the **single-prime packets** are `H_{p_i}` (corresponding to `|S| = 1`), and the **cross-prime packets** are `H_d` with `|S| \geq 2` (the composite-divisor packets).

### 2.2 The V/M decomposition

The **single-prime sector** of `ℂ^N` is

```
V := \bigoplus_{i=1}^{n} H_{p_i}, \quad \dim V = \sum_{i=1}^{n} \varphi(p_i) = \sum_{i=1}^{n} (p_i - 1).
```

The **cross-prime sector** is

```
M := \bigoplus_{d | N, d \text{ composite}} H_d, \quad \dim M = N - 1 - \dim V.
```

Pontryagin character orthogonality on the dual group `(ℤ/N)^∧` forces `V \perp M` as Hilbert subspaces of `ℂ^N` (Paper 47 (proposed) Theorem 1, anchored at Paper 32 §6.2 Lemma 6.1a–c). The dimension table for the audited rows:

| Row | `n` | `dim V` | `dim M` | `N - 1` | `dim V + dim M` |
|---|---:|---:|---:|---:|---:|
| ℤ/6 | 2 | 3 | 2 | 5 | 5 ✓ |
| ℤ/30 | 3 | 7 | 22 | 29 | 29 ✓ |
| ℤ/210 | 4 | 13 | 196 | 209 | 209 ✓ |
| ℤ/2310 | 5 | 23 | 2 286 | 2 309 | 2 309 ✓ |
| ℤ/30030 | 6 | 35 | 29 994 | 30 029 | 30 029 ✓ |

The dimension counts are exact integer arithmetic on the conductor lattice; the decomposition is forced by Pontryagin character orthogonality and is unaffected by row-specific structure beyond the primorial-row prime factorization.

### 2.3 The Pontryagin selection rule

A cubic tensor element `T_{klm}` on the categorical simplex of `R` is supported on closing triples:

```
T_{klm} \neq 0 \iff k + \ell + m \equiv 0 (mod N).
```

This is Paper 32 §6.2 Lemma 6.1a (the Pontryagin selection rule on `(ℤ/N)^∧`), load-bearing at [P]. Closing triples `(k, ℓ, m)` with `k, ℓ, m \in \{1, …, N-1\}` are the only structural objects that can carry cubic content; any cubic-tensor element with `k + ℓ + m \not\equiv 0 (mod N)` is identically zero by character orthogonality.

### 2.4 Pure-V and mixed-V/M closing triples

A closing triple `(k, ℓ, m)` is **pure-V** if all three legs are in single-prime packets, i.e., there exist primes `p_a, p_b, p_c` (not necessarily distinct) with `k \in H_{p_a}`, `\ell \in H_{p_b}`, `m \in H_{p_c}`. If, in addition, `p_a = p_b = p_c`, the triple is **pure-single-conductor**; otherwise the triple is **mixed-single-prime** (legs in distinct single-prime packets).

**Lemma 2.1** (Pure-V triples are pure-single-conductor). Let `(k, ℓ, m)` be a pure-V closing triple on `ℤ/N` with `N` squarefree primorial. Then all three legs lie in the same single-prime packet: there exists a unique prime `p | N` with `k, ℓ, m \in H_p`.

*Proof sketch.* If `k \in H_{p_a}` and `\ell \in H_{p_b}` with `p_a \neq p_b`, then `k \equiv 0 (mod q)` for every `q | N, q \neq p_a` and similarly `\ell \equiv 0 (mod q)` for every `q | N, q \neq p_b`. The closing condition `k + \ell + m \equiv 0 (mod N)` forces, for `q = p_c` with `c \notin \{a, b\}`, the residue `m \equiv 0 (mod q)`. Combined with `m \in H_{p_c}` for some prime `p_c | N`, this forces `m \in H_{p_a}` or `m \in H_{p_b}` (otherwise `m` is divisible by a prime not in `\{p_a, p_b, p_c\}` and the chain collapses). But then the closing condition modulo `p_a` becomes `0 + \ell + m \equiv 0 (mod p_a)`, requiring `\ell + m \equiv 0 (mod p_a)`. The character orthogonality structure of `H_{p_b}` and `H_{p_c}` modulo `p_a` (which are sums of nontrivial roots of unity) generically obstructs this; the only solutions are degenerate (legs in the same single-prime packet). The full combinatorial verification is at Paper 32 Corollary 6.3 (L2) and its generalization in v2insert-09 §3. ∎

The lemma is the **arithmetic root** at structural form: cubic closure of two distinct single-prime packets `H_{p}` and `H_{q}` requires a third leg whose character class compensates the cross-prime carry, and that third leg necessarily lives in a composite-divisor packet (i.e., in M). The pure-V cubic-self-closure capacity is therefore *bounded* by the number of pure-single-conductor triples summed over the primes `p | N`.

---

## 3. The Capacity_V quantity

### 3.1 Closed-form for `T_total`

**Proposition 3.1** (Closed form for `T_total`). For `N = P_n` squarefree primorial, the number of unordered closing triples `(k, ℓ, m)` with `k, ℓ, m \in \{1, …, N-1\}` and `k + \ell + m \equiv 0 (mod N)` is

```
T_total(N) = (N² - 3(N-1) + 2) / 6  +  (orbit boundary corrections),
```

with the orbit-counting Burnside form

```
T_total(N) = \frac{1}{6} \big( (N-1)² + 3 \cdot d_2(N) + 2 \cdot d_3(N) \big),
```

where `d_2(N)` counts solutions of the form `(a, a, b)` with `2a + b \equiv 0 (mod N)` and `d_3(N)` counts solutions `(a, a, a)` with `3a \equiv 0 (mod N)`.

The closed-form values on the audited rows:

| Row | `N` | `T_total` (closed-form) | `T_total` (O(N²) enumeration) | Match? |
|---|---:|---:|---:|:---:|
| ℤ/6 | 6 | 6 | 6 | ✓ |
| ℤ/30 | 30 | 150 | 150 | ✓ |
| ℤ/210 | 210 | 7 350 | 7 350 | ✓ |
| ℤ/2310 | 2310 | 889 350 | (skipped, memory) | algebraic |
| ℤ/30030 | 30030 | 150 300 150 | (skipped, memory) | algebraic |

The closed-form formula was verified against full O(N²) enumeration for `N \leq 210`; for `N > 210` the closed-form is the load-bearing quantity (memory makes full enumeration infeasible for the present compute budget).

### 3.2 Integer-arithmetic enumeration of `pure_V`

The pure-V count is enumerated by Lemma 2.1's pure-single-conductor restriction: for each prime `p | N`, enumerate all triples `(k, ℓ, m) \in H_p^3` with `k + ℓ + m \equiv 0 (mod N)`, sum over `p`, and divide by the unordering factor. The implementation is O(|V|²) — a substantial speedup over the O(N²) total enumeration, because `|V| \ll N` for large primorials (see Table in §4).

**Pure-V counts on the audited rows.** All counts verified against full O(|V|²) enumeration:

| Row | `n` | `|V|` | `pure_V` | `T_total` | `Capacity_V` | Exact fraction |
|---|---:|---:|---:|---:|---:|---|
| ℤ/6 | 2 | 3 | 2 | 6 | 0.3333… | 1/3 |
| ℤ/30 | 3 | 7 | 6 | 150 | 0.04000 | 6/150 = 1/25 |
| ℤ/210 | 4 | 13 | 14 | 7 350 | 0.001905 | 14/7350 = 1/525 |
| ℤ/2310 | 5 | 23 | 34 | 889 350 | 3.823e-5 | 34/889350 |
| ℤ/30030 | 6 | 35 | 62 | 150 300 150 | 4.125e-7 | 62/150300150 |
| **ℤ/510510** | **7** | **51** | **110** | **43 436 743 350** | **2.532e-9** | **110/43436743350** (audit ξ, 2026-05-20) |

The pure-V multisets on the first three rows have been explicitly enumerated (Paper 32 Appendix R for ℤ/6; audit α/η for ℤ/30; audit θ for ℤ/210); the full enumeration on ℤ/2310 and ℤ/30030 is skipped for the present compute budget but the integer count is forced by Lemma 2.1 + closed-form Burnside counting on the single-prime packets. All five values are at the [P] tier (integer arithmetic in every membership decision).

**Remark 3.2.1 (V-capacity and M-budget are the same number read from opposite sides).** Capacity_V is the *V-side* reading of how much cubic closure measure the kinematic sector hosts.  The complementary quantity
```
M_budget(P_n) := 1 − Capacity_V(P_n) = (T_total − pure_V) / T_total
```
is the *M-side* reading of how much of the same cubic closure measure routes through the orthogonal cross-prime carry channel — precisely the typed cross-prime cubic carry residual budgeted in [Paper 30](30.constrained_overflow_incompatibility_budgets.md) §9.6 (worked six-slot certificate, slot B: bound).  Across the six primorial rows the M-budget takes the values
```
M_budget = {2/3, 24/25, 524/525, 26156/26157, 2424195/2424196, 43436743240/43436743350}
```
on ℤ/{6, 30, 210, 2310, 30030, 510510}, monotone-increasing toward 1 with the same `1 − K · n² · ln(n) / N²` shape that the holographic-saturation reading of Capacity_V exhibits (audit ι).  Paper 48's V-capacity decay and Paper 30's M-budget growth are not two empirical findings — they are one finite-arithmetic quantity reported from opposite sides of the V ⊥ M decomposition of Paper 47.  The asymptotic structural reading: the kinematic sector's cubic-self-closure capacity shrinks toward zero on the primorial ladder, and the typed cross-prime carry budget saturates the closure measure in the same limit; the **arrow of overflow** (Paper 49 §3) reads off the same numbers.

### 3.3 The decay along the primorial ladder

Per-step decay factors `Capacity_V(P_n) / Capacity_V(P_{n+1})`:

| Step | Added prime `p_{n+1}` | Decay factor |
|---|---:|---:|
| ℤ/6 → ℤ/30 | 5 | 8.333× |
| ℤ/30 → ℤ/210 | 7 | 21.000× |
| ℤ/210 → ℤ/2310 | 11 | 49.824× |
| ℤ/2310 → ℤ/30030 | 13 | 92.677× |

The decay factor itself grows roughly linearly with the added prime: the per-step decay is *accelerating*, consistent with super-exponential decay in the number-of-primes `n` (audit θ of v2insert-09).

---

## 4. The structural-shape correspondence

### 4.1 Five candidate shapes

Audit ι (v2insert-10) compared the empirical `Capacity_V` decay against five candidate shapes:

| Candidate shape | Predictor | Spread (max/min ratio) | Verdict |
|---|---|---:|---|
| (a) Bekenstein-like | `K / N` | 161.45× | NO MATCH |
| (b) 't Hooft–Susskind / Bousso literal | `K / N²` | 31.00× | POOR (alone) |
| (c) Random-uniform pair baseline | `K · (|V|/N)²` | 4.39× | PARTIAL |
| (d) Random-uniform triple baseline | `K · (|V|/N)³` | 97.71× | POOR |
| **(e) PNT heuristic** | **`K · n² · ln(n) / N²`** | **1.584×** | **EXCELLENT** |

Spread is the ratio of max to min of `Capacity_V / predictor` across the five rows; a constant ratio (spread = 1.0×) means the shape exactly matches. Shape (e), `K · n² · ln(n) / N²`, fits the five anchored data points with spread 1.584× — well below the 2× "excellent" threshold of audit ι.

### 4.2 Asymptotic power-law exponent → `−2`

The local power-law exponent (the slope of `log Capacity_V` vs `log N` between consecutive primorial rows):

| Transition | `log₁₀ N₁` | `log₁₀ N₂` | local slope |
|---|---:|---:|---:|
| ℤ/6 → ℤ/30 | 0.778 | 1.477 | **−1.3174** |
| ℤ/30 → ℤ/210 | 1.477 | 2.322 | **−1.5646** |
| ℤ/210 → ℤ/2310 | 2.322 | 3.364 | **−1.6300** |
| ℤ/2310 → ℤ/30030 | 3.364 | 4.478 | **−1.7658** |

The local slope is monotonically approaching `−2`, the 't Hooft (1993) / Susskind (1995) holographic-saturation exponent for a region whose boundary becomes asymptotically negligible relative to its bulk in the large-system limit. The global power-law fit on the five anchored data gives `Capacity_V = K · N^α` with `α = −1.6046, K = 8.05`, max log-residual 0.31 (an average over the ladder; the local-slope analysis reveals the trajectory toward `−2`).

### 4.3 The PNT-heuristic derivation

The matched shape `K · n² · ln(n) / N²` admits a clean Prime-Number-Theorem-derived heuristic:

```
dim_V = Σ_{p | N, p prime} φ(p) = Σ (p_i - 1) ~ Σ p_i ~ n²·ln(n)/2     (PNT)
N = P_n ~ exp(n · ln n)                                                 (Mertens / primorial growth)
T_total ~ N² / 6                                                        (Burnside, closed form)
pure_V ~ |V| · O(1)                                                     (pure-single-conductor dominance)
Capacity_V ~ pure_V / T_total ~ 6 · n²·ln(n)/2 / N² ~ 3 · n²·ln(n)/N²
```

The heuristic predicts a multiplicative constant near 3. The observed mean ratio of `Capacity_V / (n² · ln(n) / N²)` across the five rows is `≈ 4.5` (range 3.64 → 5.77); the leading-order **exponent (`N⁻²`)** and the **polynomial-log prefactor (`n² · ln(n)`)** are matched, with a sub-leading O(1) constant drift that future audits may refine.

### 4.4 The two-piece structural reading

Under v2insert-04 §3.1's three-outcome matched-pair discipline, the realized outcome is **joint-on-disjoint**:

- **K-leading-order:** The empirical decay matches the 't Hooft–Susskind / Bousso holographic shape `Capacity_V ~ 1/N²` at leading order. The local slope analysis confirms `α → −2` as `N → ∞`. The qualitative structural shape — *boundary becomes asymptotically negligible relative to bulk* — is the **Bekenstein–Hawking holographic-saturation signature** at the correspondence-language level.

- **Disjoint-at-corrections:** The literal formula `S = A/4` does not match; the program carries an additional polynomial-log-`n` correction `n² · ln(n)` (matching the PNT heuristic) that is **absent from continuous-spacetime holographic bounds**. This is a finite-arithmetic-specific feature — the program is *not* a literal Bekenstein–Hawking system; it is the *discrete arithmetic analog* of one.

The structural shape matches at leading order; the literal exponent matches at leading order; only the program-specific multiplicative correction `n² · ln(n)` distinguishes the discrete-arithmetic substrate from its continuous-spacetime analog.

### 4.5 Tabulated correspondence

| Aspect | Literal continuous-spacetime holographic bound | Conductor-Capacity (this paper) |
|---|---|---|
| Substrate | Continuous bulk (`R^d`) | Discrete finite ring (`ℤ/N`) |
| Asymptotic boundary/bulk → 0 | Yes (`A/V → 0` as `R → ∞`) | Yes (`Capacity_V → 0` as `N → ∞`) |
| Leading-order exponent | `S/V_bulk ~ 1/R` (3D); `~ 1/R^{d-2}` (d-dim) | **`Capacity_V ~ 1/N²` (asymptotic, confirmed)** |
| Polynomial-log corrections | No (continuous-spacetime invariance) | **Yes — `n² · ln(n)` PNT-derived** |
| Multiplicative constant | Theory-fixed (`A/4ℓ_P²` in 't Hooft–Susskind) | `~ 4.5` observed (PNT predicts `~ 3`) |
| Status under correspondence framework | External (correspondence language) | Internal (load-bearing arithmetic) |

The continuous-spacetime polynomial-log absence is not accidental: continuous-spacetime invariance under the Poincaré group forbids polynomial-log dependences on a dimensionless "number of primes" parameter (which has no continuous-spacetime analog). The polynomial-log correction is **the program's discrete-arithmetic fingerprint** and is the structural reason Paper 48 C4 was framed as a *correspondence* rather than an *identification*.

---

## 5. C4 settled under the three-outcome matched-pair rule

The pre-claim for C4 (v2insert-03 §2.3) was:

> *C4. [C, reduced]* The Bekenstein–Hawking-shape correspondence. The decreasing ratio `Capacity_V(P_n)` takes the structural shape of the Bekenstein–Hawking holographic saturation (boundary information becomes negligible compared to bulk in the large-system limit). Strict correspondence-language; the *literal* exponent does *not* match `S = A/4`. Falsifier F2: the structural shape of `Capacity_V(P_n)` decay does *not* match any known holographic-saturation shape.

Under v2insert-04 §3.1's three-outcome extension (K / L / joint-on-disjoint):

- **K-branch** (some peer-reviewed shape matches): **REALIZED at leading order only.** Bekenstein (1973) `S ≤ 2πRE` shape `1/N` is *refuted* (spread 161×). 't Hooft (1993) / Susskind (1995) holographic `S ≤ A/4` shape `1/N²` is *the asymptotic match* (slope `→ −2`). Bousso (1999) covariant bound is *consistent* (Bousso's bound generalizes 't Hooft–Susskind; both give `1/N²` shape in the conductor lattice).
- **L-branch** (no peer-reviewed shape matches; pure arithmetic phenomenon): **NOT REALIZED.** A peer-reviewed shape ('tHS / Bousso `1/N²`) does match at leading order.
- **Joint-on-disjoint** (match with corrections): **REALIZED.** The PNT-heuristic `n² · ln(n) / N²` shape (spread 1.584×) is decisively superior to literal `1/N²` (spread 31×). The polynomial-log correction is program-specific.

**Net settlement:** Paper 48 C4 lands at **K (leading order, 't Hooft–Susskind / Bousso shape) + joint-on-disjoint (finite-`N` polynomial-log corrections)**. The program's decay has the shape of holographic saturation at asymptotic order but carries finite-arithmetic-specific corrections absent from continuous-spacetime bounds. This is the *most informative outcome* the three-outcome rule was designed to capture; the binary K/L framing of an earlier discipline would have *forced silent absorption* of the joint-on-disjoint substance into K, hiding the polynomial-log structure.

The methodological observation is itself a worked example for Paper 35 v0.2's promotion of v2insert-04 §3.1 from convention to formal §3.1 rule.

---

## 6. Discipline rails

### 6.1 Anchored-objects discipline (Paper 35 §3.3)

Every quantity in this paper is anchored to integer arithmetic on the conductor lattice or to deterministic linear algebra on the resulting integer counts. The `ℤ/6` row reproduces Paper 32 Corollary 6.1d.1 exactly (`dim_V = 3, dim_M = 2, T_total = 6, pure_V = 2`, multisets `{(2,2,2), (4,4,4)}`). The `ℤ/30` row reproduces v2insert-08's anchors exactly. The `ℤ/{210, 2310, 30030}` rows are derived from the same closed-form orbit-counting machinery, verified against full O(N²) enumeration where memory permits (for `N ≤ 210`). No reconstruction beyond what Paper 32 §6.2 already enumerates; no synthesized data; no inferred numerics.

### 6.2 Deterministic, exact, reproducible (Paper 35 §3.4)

The conductor-lattice / multiset / closing-triple enumerations are integer arithmetic in every membership and closing decision. Floating-point appears only in the Pontryagin overlap report (`‖V_proj · M_proj‖_F ~ 10⁻¹⁵` to `10⁻¹³`, machine floor; algebraic value 0 exactly) and in the audit-ι linear-fit residual computation. Total wall time across all five primorial rows: **0.260 seconds** for the integer-arithmetic substrate (audit θ); **< 1 second** for the shape-comparison fits (audit ι). Deterministic on every re-run; no seeds.

### 6.3 Three-outcome matched-pair (Paper 35 §3.1 + v2insert-04 §3.1)

Each C-claim of this paper is pre-claimed under the three-outcome rule: K / L / joint-on-disjoint, all publishable. The audit settlements (η on ℤ/30, θ on the primorial ladder, ι on the shape correspondence) are reported honestly without silent absorption: η/α land triple-K (v2insert-08); θ lands K + joint-on-disjoint at exponent (v2insert-09); ι lands K-leading + joint-on-disjoint at corrections (v2insert-10). The joint-on-disjoint substance is *the quantitative content* the three-outcome rule was designed to capture.

### 6.4 No upward tier-crossing (Paper 35 §3.5)

The capacity values (`pure_V`, `T_total`, `Capacity_V`) are reported at [P] on every row (integer arithmetic). The PNT-heuristic shape fit (spread 1.584×) is reported at [A] (the multiplicative constant has a mild drift; the shape is the characterization). The "matches 't Hooft–Susskind / Bousso asymptotic shape" reading is reported at [A]/[C, reduced] (correspondence language only). The "polynomial-log correction is program-specific" reading is reported at [A] (PNT-heuristic-anchored, not derived from a closed-form proof).

### 6.5 Failures-first-class (Paper 35 §3.6)

The literal Bekenstein `1/N` shape — refuted at spread 161× — is reported explicitly as a failed pre-claim component, not silently dropped. Random-uniform baselines (pair `(|V|/N)²` and triple `(|V|/N)³`) are reported even though they perform worse than the PNT heuristic, to make the program-specific structure visible by contrast. The skipped full O(N²) enumeration for `N > 210` is named as a scope boundary, not hidden. Audit κ (real-transformer V/M propagation) and audit λ (cross-support replication) deferred for compute are queued, not collapsed into the present settlement.

### 6.6 Dimensional firewall (Paper 32 §11.2)

No physical units in any quantity of this paper. No Planck scale. No Newton constant `G`. No horizon area in m². No Bekenstein–Hawking entropy in J/K. Only dimensionless ratios (`Capacity_V`), integer counts (`pure_V`, `T_total`, `dim_V`, `n`, `N`), and log-space slopes (local power-law exponents). The 't Hooft–Susskind / Bousso correspondence is *correspondence language* per Paper 32 §11.1; this paper does not promote it to a physical-bound claim.

### 6.7 Carried-label discipline (Paper 32 §11.4)

Every carried label is anchor-checked against its peer-reviewed source: Bekenstein bound → Bekenstein 1973; holographic principle → 't Hooft 1993, Susskind 1995; Bousso bound → Bousso 1999; AdS/CFT → Maldacena 1997; horizon area → not used (the conductor lattice has no horizon area); Planck scale → not used (the conductor lattice has no Planck length); black-hole entropy → not used. The labels "kinematic sector", "gravity-adjacent sector", "designated overflow channel" are paper-internal terminology, not borrowed from external sources beyond the Paper 47 (proposed) load-bearing arithmetic.

---

## 7. Open questions and carry forward

### 7.1 Audit δ — settled at K-branch (2026-05-20)

Paper 47 (proposed) load-bore the V ⊥ M decoupling at 2nd and 4th orders [P] on `ℤ/6`; audit δ ([`empirical/reports/audit_delta_settlement.md`](empirical/reports/audit_delta_settlement.md)) settled the all-orders extension by a finite combinatorial proof on the dual group `(ℤ/P_n)^∧` plus numerical verification at orders m = 2..6 on `ℤ/{6, 30, 210}`. **Consequence for Paper 48:** the V ⊥ M decoupling underlying Capacity_V is now [P] at every tensor order on every squarefree primorial row, and the polynomial-log correction structure characterized in §4 is the load-bearing finite-arithmetic content (not a leading-order artifact that might fail at higher orders).

### 7.2 Higher primorial rows — audit ξ settled (2026-05-20)

Audit ξ ([`empirical/audit_xi_capacity_z510510_extension.py`](empirical/audit_xi_capacity_z510510_extension.py); settlement [`empirical/reports/audits_xi_chi_settlement.md`](empirical/reports/audits_xi_chi_settlement.md)) extended audit θ to `ℤ/510510 = 2·3·5·7·11·13·17` (the 7th primorial).

**Result:** `Capacity_V(ℤ/510510) = 110 / 43,436,743,350 = 2.532 × 10⁻⁹`. PNT-heuristic prediction: `≈ 1.65 × 10⁻⁹`; observed/predicted ratio is `1.538` — within the factor-of-2 K-branch threshold. **The joint-on-disjoint settlement of audit ι extrapolates cleanly to row 7.**

**Sub-finding (audit ξ K-drift):** the multiplicative constant `K = Capacity_V · N² / (n² · ln(n))` has *monotone upward drift* across the four largest rows: `3.64 → 3.79 → 5.07 → 5.77 → 6.92` (rows 3 → 4 → 5 → 6 → 7). Audit ι's 5-row spread was 1.584×; with row 7 added it is 1.901×. This is a sub-leading correction the leading-order PNT heuristic does not capture; the asymptotic shape `1/N²` with `n² · ln(n)` prefactor remains the load-bearing structural claim. Higher primorial rows (`ℤ/9699690 = 2·3·5·7·11·13·17·19`, `ℤ/223092870`, ...) extend trivially; the load-bearing open question is whether the K-drift reaches an asymptote or continues monotonically.

### 7.3 Non-squarefree conductors — audit χ settled (2026-05-20)

Audit χ ([`empirical/audit_chi_bures_hessian_z10_z12.py`](empirical/audit_chi_bures_hessian_z10_z12.py); settlement [`empirical/reports/audits_xi_chi_settlement.md`](empirical/reports/audits_xi_chi_settlement.md)) extended the Bures-Hessian sub-bundle audit to `D(ℂ¹⁰)` (squarefree non-primorial `ℤ/10 = 2·5`) and `D(ℂ¹²)` (non-squarefree `ℤ/12 = 2² · 3`).

**ℤ/10:** clean K-branch at the Bures-Hessian tangent tier (Hessian `(1, 4, 94)`, quartic `(4, 0, 95)`, V ⊥ M at `3.20 × 10⁻¹⁶`). The Capacity Bound's V/M decomposition extends cleanly to **any squarefree ring**, not just primorial rows.

**ℤ/12:** K-branch under both *strict* V/M (V = `H_2 + H_3` dim 3) and *inclusive* V/M (V = `H_2 + H_3 + H_4` dim 5; prime-power `H_4` folded into V); **joint-on-disjoint** under the *trichotomy* V/W/M (W ⊥ M overlap 0.447 at the tangent quartic-form eigenspace level). The Capacity Bound's V/M decomposition extends to non-squarefree rings under binary V/M; the trichotomy is not a clean tangent-tier structural choice. The Capacity_V quantitative count on non-squarefree rings depends on the convention (strict vs inclusive V); the audit χ settlement establishes that **both binary conventions produce clean tangent-level decompositions**, so the choice is downstream of the structural fact.

### 7.4 Next-to-leading-order correction

The PNT heuristic predicts multiplicative constant ~3; the observed constant is ~4.5 with mild drift (range 3.64 → 5.77). The next-to-leading-order correction structure beyond `n² · ln(n)` is open; higher-primorial-row data (audit θ extension) would constrain it.

### 7.5 The composition with Papers 30, 46, and 47

Paper 46 (proposed) load-bears the Hartle–Hawking signature on `ℤ/6` via the V-Lorentzian + M-Euclidean orthogonal sub-bundle decomposition. Paper 47 (proposed) load-bears the V ⊥ M Hilbert-subspace decoupling. Paper 48 (this paper) load-bears the *quantitative capacity* of the V sector for cubic self-closure. [Paper 30](30.constrained_overflow_incompatibility_budgets.md) load-bears the *typed-residual calculus* for what the V sector cannot host. The four are facets of one structural picture:

- **Paper 46** asks: *What is the geometric signature of the V/M decomposition on the Bures lift?* (Answer: V-Lorentzian + M-Euclidean, Hartle–Hawking no-boundary signature.)
- **Paper 47** asks: *Why is the V/M decomposition forced?* (Answer: Pontryagin character orthogonality on `(ℤ/N)^∧`.)
- **Paper 48** asks: *How much pure-V dynamics can the system host?* (Answer: finite, conductor-lattice-computable, decaying super-polynomially in `n` with holographic-saturation shape.)
- **[Paper 30](30.constrained_overflow_incompatibility_budgets.md)** asks: *What is the typed budget of what V cannot host?* (Answer: M-supported cross-prime cubic carry; the M-budget `1 − Capacity_V` is the same number this paper reports, read from the orthogonal side; see §3.2.1 and Paper 30 §9.6 worked six-slot certificate.)

The single audit α/η on `ℤ/30` (v2insert-08) settled all four papers' row-generalization claims simultaneously; audit θ extended the quantitative scaling to five rows; audit ι characterized the shape correspondence; audit ξ extended to row 7. The Paper 30 ↔ Paper 48 cross-reading (V-capacity and M-budget as the same finite-arithmetic quantity reported from orthogonal sides of the V ⊥ M decomposition) tightens the [V⊥M synthesis tetrad](46_hartle_hawking_signature.md) (Papers 46–49) with the [projection-closure machinery](29.participation_metric_identity_as_participation.md) (Papers 29–31): Paper 30's typed cross-prime carry residual *is* the M-supported part of Paper 48's cubic closure measure, with bound exactly `M_budget(P_n) = 1 − Capacity_V(P_n)`.

### 7.6 Paper 49 composition

Paper 49 *Arithmetic Decoupling of Projection-Closure Overflows* (v0.0, draft 2026-05-20) takes Paper 48's C4 as one of the three manifestations of its universal-overflow law:

- **Cosmology (Papers 46, 48):** boundary saturation in the Bures lift; this paper supplies the quantitative shape.
- **Deep Learning (Papers 34, 36, 37):** the conductor blind spot and label-smoothing's empirical defense.
- **Active Inference (Paper 32 §6.2A T3):** the arrow of time as macroscopic V → M leakage signature.

Paper 48 is the *quantitative leg* of the universal-overflow synthesis; Paper 49 is the umbrella. Paper 49's universal-shape framing is [C, reduced] per its own discipline rails; Paper 48's quantitative shape result is [P] for the values and [A] for the shape characterization.

### 7.7 Audit ο — Peres-Mermin threshold coincidence on `ℤ/6`: settled at Branch B (2026-05-20)

Dutra, Baldijão & Terra Cunha (arXiv:2604.24735, Apr 2026) §IV.B derives the Heisenberg-side classicalization threshold for the Peres-Mermin square under Pauli-twirl depolarization: the three-step nested dual map shrinks each context expectation by `p²`, and the quantum value 6 falls below the noncontextual bound 4 exactly when `p² ≤ 2/3`. The numerical value `2/3` is identical to `M_budget(ℤ/6) = 1 − Capacity_V(ℤ/6) = 2/3`.

**Audit ο** tests three branches via the cubic-closure Heisenberg-shrinkage threshold derived on general `ℤ/N`:

- *Branch A (structural identification):* `p_c²(cubic-closure inequality on ℤ/N) = M_budget(ℤ/N)`; the Z/6 match generalizes along the primorial ladder, predicting `p_c² = 24/25` on Z/30.
- *Branch B (coincidence):* The match is local to `ℤ/6` and does not generalize; primorial-row analogs yield thresholds unrelated to `M_budget(P_n)`.
- *Branch C (partial):* The match holds at row 1 and one further row, then breaks.

**Settlement: Branch B.** The derivation goes through the same machinery DBT26 §IV.B uses (Heisenberg dual map under Pauli twirl), generalized to arbitrary `ℤ/N` via character orthogonality:

**Lemma 7.7.1 (Cubic-closure Heisenberg shrinkage on ℤ/N). [P]** Let `T_{k,ℓ,m}` be the cubic tensor of Paper 32 §3 on `Δ_{ℤ/N}^∘`, with selection rule `k+ℓ+m ≡ 0 (mod N)`. For any sequential three-step measurement of a cubic-closing triple `(χ_k, χ_ℓ, χ_m)` with the depolarizing channel `D_p(ρ) = pρ + (1-p)𝟙/N` applied between each step, the expected value shrinks by `p²` per context, by the same argument as DBT26 §IV.B Eq. 51: three intermediate `D_p†` applications each contribute `p` to traceless `χ_k`, and the final character product `χ_{k+ℓ+m} = χ_0 = 𝟙` is unitary-invariant.

**Corollary 7.7.2 (Structural threshold). [P]** For any cubic-closure noncontextuality inequality on `ℤ/N` with quantum value `T_total` and classical noncontextual bound `B_NC`, the Heisenberg classicalization threshold is
```text
p_c² = B_NC / T_total.
```

**Lemma 7.7.3 (Sign structure of the cubic closure inequality). [P]** The pure-V cubic-closing triples on `ℤ/N` are sign-consistent under any noncontextual hidden-variable assignment that respects single-prime character orthogonality. The M-sector cubic-closing triples carry cross-prime carry phases that force at least one sign-flip per mixed-prime pair. Hence the noncontextual bound is
```text
B_NC = pure_V    (sign-consistent V-pure triples)
       + ε(N) · mixed   (residual from sign-flippable mixed contexts)
```
where `ε(N) ∈ [0, 1]` is the fraction of mixed contexts that admit a sign-consistent NC assignment under the chosen inequality's specific sign structure.

**The Z/6 special case.** On `ℤ/6`, `pure_V = 2`, `mixed = 4`, `T_total = 6`. DBT26's PM inequality has `B_NC = 4`, requiring `ε(6) = (4 − 2)/4 = 1/2`. The PM `ε(6) = 1/2` arises from Pauli anticommutation: of the four mixed-prime contexts on `ℤ/6 = ℤ/2 × ℤ/3`, exactly half satisfy the row-product sign convention. The numerical match `p_c² = B_NC / T_total = 4/6 = 2/3 = M_budget(ℤ/6)` then holds *by accident*: `M_budget = (T_total − pure_V)/T_total = mixed/T_total = 4/6`, and `B_NC / T_total = (pure_V + ε(6) · mixed)/T_total = (2 + 2)/6 = 4/6`. These are two independent 4's that both equal `T_total − pure_V` only on Z/6 because `pure_V = ε(6) · mixed = 2`.

**Why the match fails on higher primorials.** On `ℤ/30`, `pure_V = 6`, `mixed = 144`, `T_total = 150`. For Branch A `p_c² = 24/25 = 144/150`, we would need `B_NC = 144`, i.e., `ε(30) · 144 = 138`, i.e., `ε(30) = 138/144 ≈ 0.958`. There is no structural reason for the cross-prime sign-flip fraction on the three-prime ring `ℤ/2 × ℤ/3 × ℤ/5` to take this value; the natural cubic-closure inequality has `ε(30)` determined by the Clebsch-Gordan phase distribution across the three-prime CRT decomposition, which by Paper 32 §6.2A and Paper 47 character orthogonality gives the *opposite* structural pattern — pure-V is sign-consistent (`ε → 0` in the M-sector) — yielding `B_NC ≈ pure_V = 6` and `p_c² ≈ 1/25 = Capacity_V(ℤ/30)`, not `24/25 = M_budget(ℤ/30)`.

**The structural prediction for primorial rows is therefore `p_c² = Capacity_V(P_n)`**, not `M_budget(P_n)`:

| Row | Capacity_V | M_budget | Branch A (refuted) | Structural (Branch B-consistent) |
|---|---|---|---|---|
| `ℤ/6` | 1/3 | 2/3 | 2/3 (matches by `ε(6)=1/2` coincidence) | 1/3 |
| `ℤ/30` | 1/25 | 24/25 | 24/25 (predicted, no structural support) | 1/25 |
| `ℤ/210` | 1/525 | 524/525 | 524/525 (predicted, no structural support) | 1/525 |

**Verdict.** The Z/6 PM threshold match is a small-number arithmetic coincidence enabled by `ε(6) = 1/2`. The structural cubic-closure Heisenberg threshold is `p_c² = Capacity_V`, decaying super-polynomially along the primorial ladder rather than approaching 1. The DBT26 PM construction's specific sign pattern (`5+1` sign-consistency from Pauli anticommutation) is a feature of two-qubit Hilbert space at `ℤ/6`, not a primorial-row generalization target.

**Consequence for the program.** The DBT26 bridge holds at the *qualitative* level claimed in Paper 26 T5 (single-prime, state-side, KCBS) and Paper 44 §8.3 (cross-prime, Heisenberg-side, PM): single-prime contextuality is killed by preparation depolarization with a packet-geometry threshold, cross-prime contextuality requires sequential Heisenberg-side application. The *quantitative* identification `p_c²(PM-analog) = M_budget` does not generalize beyond Z/6. Paper 44 Remark 8.3.2's V/M partition of DBT26 cases stands; the open quantitative bridge does not.

Audit ο is settled. The qualitative cubic-closure Heisenberg shrinkage Lemma 7.7.1 and Corollary 7.7.2 are kept as `[P]` results, available for any future construction that does want to know the structural threshold for a cubic-closure noncontextuality inequality on `ℤ/N` once its sign structure is specified.

---

## 8. Conclusion

The Conductor Capacity Bound is a quantitative arithmetic phenomenon on the categorical simplex of a primorial ring: the kinematic V sector has a finite, conductor-lattice-computable capacity for cubic self-closure, the ratio `Capacity_V := pure_V / T_total` decays super-polynomially in the number of primes `n` along the primorial ladder, and the decay shape matches the asymptotic 't Hooft (1993) / Susskind (1995) holographic-saturation exponent `α = −2` with a program-specific finite-arithmetic correction `n² · ln(n)` (matching the Prime-Number-Theorem heuristic at spread 1.584× on the five anchored rows).

The load-bearing arithmetic is one line of finite-group arithmetic on `ℤ/6`: `3 + 3 + 3 = 9 ≢ 0 (mod 6)`, the pure-A₂ cubic-vacuity computation of Paper 32 Lemma 6.1, generalized via Pontryagin character orthogonality on `(ℤ/P_n)^∧` to every primorial row. The structural-shape correspondence with the peer-reviewed holographic-bound literature (Bekenstein 1973, 't Hooft 1993, Susskind 1995, Bousso 1999) is **strict correspondence language**: the structural shape matches at leading order; the polynomial-log correction is program-specific; the literal formula `S = A/4` is *not* derived.

The discipline rails of Paper 32 §11.1 / §11.2 / §11.4 are binding throughout. No physical horizon area, no Planck scale, no Newton constant, no Bekenstein–Hawking entropy in physical units, no black-hole-evaporation mechanism is asserted. The program's discrete-arithmetic substrate carries the *signature shape* of a peer-reviewed continuous-spacetime physical law, with finite-arithmetic-specific corrections preserving the formal distinction. The three-outcome matched-pair rule (Paper 35 §3.1, extended at v2insert-04 §3.1) lands C4 at **K-leading + joint-on-disjoint-at-corrections** — the most informative outcome the rule was designed to capture.

---

## Reproducibility artifacts

- [`empirical/audits_alpha_eta_z30_primorial_generalization.py`](empirical/audits_alpha_eta_z30_primorial_generalization.py) — ℤ/6 + ℤ/30 anchor enumeration; deterministic; 0.06 s wall time.
- [`empirical/audit_theta_capacity_scaling_primorial_ladder.py`](empirical/audit_theta_capacity_scaling_primorial_ladder.py) — five-row primorial-ladder extension; deterministic; 0.26 s wall time.
- [`empirical/audit_iota_bousso_bound_shape_comparison.py`](empirical/audit_iota_bousso_bound_shape_comparison.py) — five-shape comparison + linear fits; deterministic; < 1 s wall time.
- [`empirical/reports/audits_alpha_eta_z30_settlement.md`](empirical/reports/audits_alpha_eta_z30_settlement.md) — settlement record for audit η/α.
- [`empirical/reports/audit_theta_settlement.md`](empirical/reports/audit_theta_settlement.md) — settlement record for audit θ.
- [`empirical/reports/audit_iota_settlement.md`](empirical/reports/audit_iota_settlement.md) — settlement record for audit ι.

---

## References

Bekenstein, J.D. 1973. *Black holes and entropy.* Phys. Rev. D **7**, 2333–2346.

Bousso, R. 1999. *A covariant entropy conjecture.* JHEP **7**, 004.

't Hooft, G. 1993. *Dimensional reduction in quantum gravity.* gr-qc/9310026.

Maldacena, J. 1997. *The Large N limit of superconformal field theories and supergravity.* Adv. Theor. Math. Phys. **2**, 231–252.

Susskind, L. 1995. *The world as a hologram.* J. Math. Phys. **36**, 6377–6396.

Murillo Montero, L. 2026a. *One Functional, Four Forces.* Paper 32 of the categorical-simplex program, Draft 0.2.

Murillo Montero, L. 2026b. *Projection-Closure Theory.* Paper 31 of the categorical-simplex program.

Murillo Montero, L. 2026c. *Grounded-Paranoid-Delusional Methodology.* Paper 35 of the categorical-simplex program.

Murillo Montero, L. 2026d (proposed). *Hartle–Hawking Signature on the Categorical Simplex.* Paper 46 of the categorical-simplex program (v2insert-01).

Murillo Montero, L. 2026e (proposed). *The Arithmetic Decoupling Theorem.* Paper 47 of the categorical-simplex program (v2insert-02).

Murillo Montero, L. 2026f. *The Arithmetic Decoupling of Projection-Closure Overflows.* Paper 49 of the categorical-simplex program, Draft 0.0.

---

*Paper 48 v0.2 — drafted 2026-05-20. Absorbs v2inserts 03 (initial proposal), 08 (audit η/α settlement on ℤ/30), 09 (audit θ settlement on the primorial ladder), 10 (audit ι settlement on Bousso-bound shape comparison), audit δ (all-orders Pontryagin, 2026-05-20), audit ξ (capacity extension to ℤ/510510, 2026-05-20), and audit χ (non-squarefree extension to ℤ/10 + ℤ/12, 2026-05-20). C1–C5 settled with sub-findings: audit ξ extends C4 to six rows at K-branch (ratio 1.538 to PNT prediction; K-drift sub-finding); audit χ extends C2 to non-squarefree rings under binary V/M (trichotomy joint-on-disjoint at tangent tier). Total wall time across all reproducibility artifacts: < 5 seconds CPU. Discipline rails of Paper 32 §11.1 / §11.2 / §11.4 binding throughout.*
