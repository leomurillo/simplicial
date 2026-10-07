# Audit β Settlement — Lie-Algebra-of-Wick-Rotation Structural Dictionary

**Audit anchor:** [Paper 46](46_hartle_hawking_signature.md) §4.2 (the Hartle–Hawking ↔ §13.2B correspondence table); §8.1 (audit β specification — *for each row of the §4.2 table, identify the precise Lie-algebra-of-Wick-rotation statement on both sides*).

**Status:** **SETTLED — joint-on-disjoint** under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule (file deleted on absorption; rule binding via [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.1 extension). Four of five rows audit at the **Lie-algebra level [P]-spirit**; one row (imaginary time ↔ imaginary energy) audits at the **structural-abstraction level [P]-spirit**, with the dimensional gap recorded honestly. The C2 claim of Paper 46 §4.2 is promoted from [A] structural dictionary to **[P]-spirit at the Lie-algebra tier** with a single explicit sub-finding at row 3.

**Method:** finite Lie-algebra check; no compute. Pure-mathematics audit per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §3.4 (deterministic, exact, reproducible) and §3.5 (no upward tier-crossing — correspondence remains [C, reduced] in scope; the *Lie-algebra structure* of each row is what is promoted, not the cosmological claim).

**Prepared:** 2026-05-20 · Author: Leonardo Murillo Montero (team Leo)

---

## 0. The pre-claimed three-outcome branches

Per [v2insert-04](v2insert-04.md) §3.1, the audit pre-claims three branches:

- **K-branch.** Clean Lie-algebra match on every row of §4.2. The Wick rotation of Hartle–Hawking 1983 and the V/M sub-bundle structure of Paper 32 §13.2B are statements about the same Lie-algebra structure on different realizations. C2 promotes to [P]-spirit uniformly.

- **L-branch.** No Lie-algebra match anywhere. The §4.2 dictionary is verbal correspondence with no underlying Lie-algebra identification. C2 falls; the correspondence reverts to "suggestive only."

- **Joint-on-disjoint.** Lie-algebra match on some rows, weaker structural-abstraction match on others, with the difference recorded explicitly per row. C2 promotes per row; the table is annotated with row-specific tier.

**Realized branch: joint-on-disjoint.** Rows 1, 2, 4, 5 admit a clean Lie-algebra match. Row 3 (imaginary time ↔ imaginary energy) admits a structural-abstraction match with an explicit dimensional gap that is itself informative.

---

## 1. Background: the Lie algebra of the Wick rotation

The Wick rotation in physics is the substitution $t \mapsto -i\tau$ that takes the Lorentzian metric $\eta = \mathrm{diag}(-1, +1, +1, +1)$ to the Euclidean metric $\delta = \mathrm{diag}(+1, +1, +1, +1)$. At the Lie-algebra level, the substitution acts on the Lorentz algebra $\mathfrak{so}(1, 3)$ as follows.

The Lorentz algebra has generators $\{J_i, K_i\}_{i = 1, 2, 3}$, with $J_i$ generating spatial rotations (compact) and $K_i$ generating boosts (non-compact), and commutation relations

$$
[J_i, J_j] = i\, \varepsilon_{ijk}\, J_k, \quad [K_i, K_j] = -i\, \varepsilon_{ijk}\, J_k, \quad [J_i, K_j] = i\, \varepsilon_{ijk}\, K_k.
$$

The complexification $\mathfrak{so}(1, 3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C}$ contains *two* real forms: $\mathfrak{so}(1, 3)$ (with non-compact boosts $K_i$) and $\mathfrak{so}(4)$ (with all six generators compact). The **Lie-algebra realization of Wick rotation** is the substitution $K_i \mapsto i K_i$ that maps the boost generators of $\mathfrak{so}(1, 3)$ to (compact) rotation-like generators of $\mathfrak{so}(4)$ within the common complexification.

The **dimensional content** of Wick rotation: the four spacetime dimensions of Lorentzian signature $(1, 3)$ analytically continue to four Euclidean dimensions of signature $(4, 0)$. *The transverse dimensions of the analytic continuation — the "imaginary-time directions" — number 1 (the time axis being Wick-rotated)*. In Hartle–Hawking 1983, the Euclidean section is a compact 4-sphere $S^4$; the Lorentzian observer-frame is locally $\mathbb R^{1, 3}$.

This is the Lie-algebra/Lie-group structure each row of Paper 46 §4.2 must be checked against.

---

## 2. Row-by-row audit

### Row 1: Compact Euclidean 4-sphere globally ↔ compact Bures manifold globally

**Hartle–Hawking side.** The Euclidean 4-sphere $S^4$ is a homogeneous space $S^4 = \mathrm{SO}(5) / \mathrm{SO}(4)$, with both $\mathrm{SO}(5)$ (the rotation group) and $\mathrm{SO}(4)$ (the stabilizer at any point) compact Lie groups. The Lie algebra $\mathfrak{so}(5)$ acts transitively on $S^4$ and preserves the round metric. **The compactness of $\mathrm{SO}(5)$ is exactly what guarantees the no-boundary property** — $S^4$ has no asymptotic direction because no element of $\mathrm{SO}(5)$ escapes to infinity.

**Program side.** The Bures manifold $\mathcal{D}^\circ(\mathbb{C}^6)$ is a homogeneous space under the action of $\mathrm{U}(6)$ (or $\mathrm{SU}(6) / \mathbb Z_6$ after central quotient), with $\mathrm{U}(6)$ compact ([Paper 18](18.bures_completion_of_cubic_information_geometric_mechanics.md) §3, [P]). The Bures-Helstrom metric is positive-definite and $\mathrm{U}(6)$-invariant. **The compactness of $\mathrm{U}(6)$ is exactly what guarantees the no-asymptote property** — no element of $\mathrm{U}(6)$ takes a density matrix to infinity in the trace norm; in particular, the manifold has no boundary.

**Lie-algebra match. [P]-spirit.** Both manifolds are homogeneous spaces of compact Lie groups acting transitively and preserving a positive-definite Riemannian metric:

$$
S^4 = \mathrm{SO}(5)/\mathrm{SO}(4) \quad \longleftrightarrow \quad \mathcal{D}^\circ(\mathbb{C}^6) \simeq \mathrm{U}(6)/(\mathrm{U}(1) \times \cdots)
$$

The structural identity is: **positive-definite invariant Riemannian metric + transitive compact Lie group action ⇒ no-boundary Riemannian manifold**. This is a standard result in homogeneous-space geometry (cf. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Ch. IV) and applies verbatim to both sides.

---

### Row 2: Lorentzian observer frame locally ↔ V-Lorentzian sub-bundle on $\mathcal D^\circ(\mathbb C^6)$

**Hartle–Hawking side.** At each point of the *Lorentzian* section (obtained from the Euclidean path integral by Wick rotation), the tangent space is $\mathbb R^{1, 3}$ with metric signature $(-, +, +, +)$. The infinitesimal symmetries preserving this metric form the Lorentz Lie algebra $\mathfrak{so}(1, 3)$, dim 6. The "local observer frame" is the choice of an oriented orthonormal basis at the point; the change-of-frame group is $\mathrm{SO}^+(1, 3)$.

**Program side.** At $\rho_* = I_6/6 \in \mathcal{D}^\circ(\mathbb{C}^6)$, the §13.2B audit ([Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [P]) establishes that the Hessian of the dispersion Casimir

$$
I_{\mathrm{complex}}(\rho) = \langle H \rangle^2(\rho) + \alpha^2 \cdot \bigl(m^2_{\mathrm{simplex}}(\rho)\bigr)^2 - \sum_{a = 1}^3 \langle P_a \rangle^2(\rho)
$$

restricted to the V-Lorentzian sub-bundle has signature $(1, 3)$ on a 4-dimensional sub-bundle (one $\langle H \rangle^2$ direction + three $\langle P_a \rangle^2$ directions). The infinitesimal transformations preserving the *indefinite* quadratic form on this 4-dim block form $\mathfrak{so}(1, 3)$ ([P], by elementary linear algebra: any non-degenerate quadratic form on $\mathbb R^4$ of signature $(1, 3)$ has automorphism group $\mathrm{O}(1, 3)$).

**Lie-algebra match. [P]-spirit, immediate.** Both sides carry the same Lie algebra $\mathfrak{so}(1, 3)$ acting on a 4-dimensional vector space with indefinite signature $(1, 3)$:

$$
T_x M_{\mathrm{HH-Lorentzian}} \simeq \mathbb R^{1, 3} \quad \longleftrightarrow \quad V\text{-block of } T_{\rho_*} \mathcal{D}^\circ(\mathbb{C}^6) \simeq \mathbb R^{1, 3}.
$$

The structural identity is **indefinite quadratic form of signature $(1, 3)$ on a 4-dim vector space $\Leftrightarrow$ action of $\mathfrak{so}(1, 3)$ as the algebra of form-preserving infinitesimal transformations**. Both sides realize this identity on a 4-dim tangent block.

---

### Row 3: Imaginary time as smoothing direction ↔ imaginary energy on M

**This is the row at which the audit returns joint-on-disjoint.**

**Hartle–Hawking side.** The Wick rotation parameter is the imaginary-time direction $\tau = -it$. At the Lie-algebra level, the substitution $K_i \mapsto i K_i$ acts as an automorphism of the *complexified* Lie algebra $\mathfrak{so}(1, 3)_{\mathbb C} \cong \mathfrak{so}(4)_{\mathbb C}$, taking the *non-compact* real form $\mathfrak{so}(1, 3)$ (boosts $K_i$ non-compact) to the *compact* real form $\mathfrak{so}(4)$ (the $i K_i$ generators now compact, rotation-like). The number of "imaginary-time directions" is *one*: a single time axis is Wick-rotated, while the three spatial directions remain real.

**Program side.** The M-Euclidean sub-bundle on $\mathcal{D}^\circ(\mathbb{C}^6)$ has dimension $\dim_{\mathrm M} = 2$ (the conductor-6 packet has two characters $\chi_1, \chi_5$). The 4th-order quartic form $(m^2_{\mathrm{simplex}})^2$ on this 2-dim block has positive-definite signature $(2, 0)$ ([Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [P]). The Lie algebra of $(2, 0)$-preserving infinitesimal transformations on $\mathbb R^2$ is $\mathfrak{so}(2)$, of dimension 1.

**Dimensional comparison.** Hartle–Hawking's "imaginary-time direction" is 1-dimensional; the program's M-Euclidean sub-bundle on $\mathbb Z/6\mathbb Z$ is 2-dimensional. The Lie algebras on each side are $\mathfrak{so}(2)$ (HH after Wick rotation: 1 rotation generator) and $\mathfrak{so}(2)$ (program: 1 rotation generator on the 2-dim Euclidean plane). The Lie-algebra-of-Wick-rotation $\mathfrak{so}(2)$ matches on both sides, but the *dimensions of the vector spaces it acts on* differ.

**Interpretation.** The dimension excess on the program side is exactly the conductor structure: HH treats time as a single direction, while the program's "imaginary-time analog" carries the dimension of the conductor-6 carry packet, which is 2 on $\mathbb Z/6\mathbb Z$. This is informative, not a defect of the dictionary: it says **the program's analog of Wick rotation is parameterized not by a single $\tau$ but by a $\dim_{\mathrm M}$-dimensional generalized imaginary-time direction whose dimension is set by the conductor carry**. On the primorial ladder, the dimension grows as $\dim_{\mathrm M}(\mathbb Z/N\mathbb Z)$, recorded at five rows in Paper 46 §5.1.

**Lie-algebra match. [P]-spirit at the algebraic level (both $\mathfrak{so}(2)$), [A] at the dimensional level (HH = 1, program = $\dim_{\mathrm M}$).** The structural identity at the Lie-algebra-only level holds; the *generalized* statement on the program side is *richer* than the literal Hartle–Hawking statement by exactly the conductor-carry dimension. This is the audit's load-bearing joint-on-disjoint sub-finding.

---

### Row 4: No initial singularity ↔ no global asymptote

**Hartle–Hawking side.** The no-boundary universe has no Big Bang singularity *because the Euclidean section closes smoothly at $\tau = 0$* — there is no "initial time" because time is part of a compact Euclidean manifold without boundary. At the Lie-algebra level, this is a property of $\mathrm{SO}(5)$ acting on $S^4$: every $\mathrm{SO}(5)$-orbit is finite (since $\mathrm{SO}(5)$ is compact); there is no "asymptotic direction" along which observables diverge.

**Program side.** $\mathcal{D}^\circ(\mathbb{C}^6)$ is compact: the trace norm is bounded by 1 ($\|\rho\|_1 = 1$ for any $\rho \in \mathcal{D}^\circ$), and the Bures-distance metric on $\mathcal{D}^\circ$ is bounded ($d_{\mathrm B}(\rho_0, \rho_1) \leq \pi/2$ for any pair). At the Lie-algebra level, this is a property of $\mathrm{U}(6)$ acting on $\mathcal{D}^\circ(\mathbb{C}^6)$: every $\mathrm{U}(6)$-orbit is finite (since $\mathrm{U}(6)$ is compact); there is no asymptotic direction. **No manifold-level Lorentzian Lie-group action exists**: any infinite-dimensional non-compact Lie-group action would force unbounded orbits, contradicting compactness.

**Lie-algebra match. [P]-spirit.** Both sides realize the structural identity **compact Lie group action ⇒ no manifold-level Lorentzian Lie-group action ⇒ no asymptote/singularity**:

$$
\mathrm{SO}(5) \text{ compact} \ \longleftrightarrow\ \mathrm{U}(6) \text{ compact} \quad\Rightarrow\quad \text{no global Lorentzian direction.}
$$

The Lorentzian content on both sides exists *only* at the local-tangent level (Row 2), not at the global-manifold level.

---

### Row 5: Hawking radiation as imaginary-energy decay width ↔ leakage rate

**Hartle–Hawking side.** Hawking 1974's mechanism: a quantum field on a black-hole spacetime acquires a thermal spectrum whose temperature $T_{\mathrm H} = \hbar / (8 \pi G M k_{\mathrm B})$ is the imaginary part of the field's energy spectrum (the decay width of asymptotic modes). At the Lie-algebra level, this is the imaginary part of the time-translation generator $H_{\mathrm{ext}}$ acting on the asymptotic Fock space — a 1-dim sub-algebra $\mathfrak{u}(1) \subset \mathfrak{so}(1, 3)$ generated by $\partial_t$.

**Program side.** [Paper 20 §3](20.the_jerk_as_simplex_mass_term.md) ([P]) identifies the *imaginary energy* $m^2_{\mathrm{simplex}} = \nabla^{(e)} T$ as the leakage rate of the projection-closure channel — the rate at which information leaves the classical diagonal of $\mathcal{D}^\circ$ into the off-diagonal coherence directions ([Paper 31](31.projection_closure_theory.md) closure-certificate vocabulary). At the Lie-algebra level, this is the imaginary part of an operator-valued generator acting on the M-Euclidean sub-bundle — a 1-dim sub-algebra $\mathfrak{u}(1) \subset \mathfrak{u}(6)$ generated by the M-supported phase rotation.

**Lie-algebra match. [P]-spirit.** Both sides realize the structural identity **imaginary part of a Lie-algebra generator ⇒ exponential decay rate of the corresponding flow**:

$$
\text{Im}(H_{\mathrm{ext}}) = \text{Hawking temperature}\ \longleftrightarrow\ \text{Im}(\text{M-supported generator}) = m^2_{\mathrm{simplex}}\ /\ \text{leakage rate.}
$$

Both are $\mathfrak{u}(1)$ sub-algebras of the relevant ambient Lie algebra; on both sides the imaginary part is what selects the "decay" interpretation of the corresponding semigroup flow. The structural identification is **complete decay = exponential of an imaginary $\mathfrak{u}(1)$ generator**, holding on both sides.

---

## 3. Summary table (audit β tier promotion per row)

| Row | HH side | Program side | Lie-algebra match | Tier promotion |
|---:|---|---|---|:---:|
| 1 | Compact $S^4 = \mathrm{SO}(5)/\mathrm{SO}(4)$ | Compact $\mathcal{D}^\circ(\mathbb C^6) \simeq \mathrm{U}(6)/(\cdots)$ | Same homogeneous-space structure of compact Lie groups acting transitively | **[P]-spirit** |
| 2 | $\mathfrak{so}(1, 3)$ on local 4-dim tangent | $\mathfrak{so}(1, 3)$ on V-Lorentzian 4-dim sub-bundle | Same Lie algebra on 4-dim signature-$(1, 3)$ vector space | **[P]-spirit** |
| 3 | $\mathfrak{so}(2)$ Wick-rotation locus, dim 1 | $\mathfrak{so}(2)$ on M-Euclidean sub-bundle, dim $\dim_{\mathrm M}$ | Same Lie algebra; **dim mismatch ($1$ vs $\dim_{\mathrm M}$): program is *richer*** | **[P]-spirit (algebra) + [A] (dimension)** — **joint-on-disjoint sub-finding** |
| 4 | $\mathrm{SO}(5)$ compact ⇒ no global Lorentzian | $\mathrm{U}(6)$ compact ⇒ no global Lorentzian | Same compactness argument | **[P]-spirit** |
| 5 | Im$(H_{\mathrm{ext}})$ = Hawking temperature | Im(M-generator) = $m^2_{\mathrm{simplex}}$ leakage rate | Same $\mathfrak{u}(1)$ decay-flow structure | **[P]-spirit** |

**Aggregate: 4 rows at [P]-spirit (Lie-algebra match clean); 1 row at [P]-spirit at the algebra tier + [A] at the dimensional tier (joint-on-disjoint sub-finding).** C2 of Paper 46 §4.2 is promoted from [A] structural dictionary to **[P]-spirit at the Lie-algebra tier with an explicit dimensional generalization at row 3**.

---

## 4. The joint-on-disjoint sub-finding at row 3 — structural significance

The dimensional mismatch at row 3 (HH's 1-dim imaginary-time direction vs program's $\dim_{\mathrm M}$-dim M-Euclidean sub-bundle) is *not a defect* of the dictionary. It is the audit's central informative content:

> **The program's analog of Wick rotation is multi-parameter; its parameter space has dimension $\dim_{\mathrm M}(\mathbb Z/N\mathbb Z)$, equal to the conductor-carry dimension on the row.**

| Row | $\dim_{\mathrm M}$ | Wick-rotation dim |
|---|---:|---:|
| $\mathbb Z/6\mathbb Z$ | 2 | 2 |
| $\mathbb Z/30\mathbb Z$ | 22 | 22 |
| $\mathbb Z/210\mathbb Z$ | 196 | 196 |
| $\mathbb Z/2310\mathbb Z$ | 2 286 | 2 286 |

Hartle–Hawking 1983's 1-dimensional imaginary time is the $\dim_{\mathrm M} = 1$ degenerate case (not realized on any nontrivial CRT row — the minimal mixed row $\mathbb Z/6\mathbb Z$ already has $\dim_{\mathrm M} = 2$). **The categorical-simplex realization is a strict generalization of Hartle–Hawking's mechanism, with the generalization parameter equal to the conductor-carry dimension.**

This connects to the [Conductor Capacity Bound of Paper 48](48_conductor_capacity_bound.md) and its super-exponential decay of $\mathrm{Capacity}_V$ on the primorial ladder: the dimension of the "Wick-rotation parameter space" $\dim_{\mathrm M}$ grows super-exponentially in the number of primes, while the V-Lorentzian dimension grows only polynomially. The categorical-simplex realization of Wick rotation is asymptotically *all imaginary-time*: as the primorial grows, almost every direction of the tangent space at the centroid becomes a Wick-rotation locus.

This is correspondence-language, not derivation: the program does *not* claim that physical spacetime has a high-dimensional generalized imaginary-time direction. It claims that *the projection-closure form* of the Hartle–Hawking mechanism on the categorical simplex generalizes Hartle–Hawking's 1-dim imaginary time to a $\dim_{\mathrm M}$-dim one, with the dimension set by the row.

---

## 5. Discipline check ([Paper 35](35_grounded_paranoid_delusional_methodology.md) §3 honored)

- **Anchored objects (§3.3).** Every Hartle–Hawking object cited (compact Euclidean 4-sphere, Lorentzian observer frame, imaginary time, no-boundary, Hawking radiation) anchored against its peer-reviewed source (Hartle–Hawking 1983; Hawking 1974; Gibbons–Hawking 1977). Every program object (V/M sub-bundle decomposition, dispersion Casimir, $m^2_{\mathrm{simplex}}$, Bures manifold, $\mathrm U(6)$ action) anchored against [Paper 32 §13.2B](32_one_functional_four_forces_v0.2%20(2).md), [Paper 18](18.bures_completion_of_cubic_information_geometric_mechanics.md), [Paper 20 §3](20.the_jerk_as_simplex_mass_term.md), [Paper 31](31.projection_closure_theory.md), at [P] tier.
- **Deterministic, exact, reproducible (§3.4).** Pure Lie-algebra check; no compute. All Lie-algebra identifications follow standard arguments in homogeneous-space geometry (cf. Helgason 1978; Knapp 1996, *Lie Groups Beyond an Introduction*).
- **No upward tier-crossing (§3.5).** The Lie-algebra-level identifications are promoted to [P]-spirit (the structural correspondence at the Lie-algebra tier is established); the *cosmological correspondence* (the Hartle–Hawking physical claim about the universe) remains [C, reduced] per [Paper 32 §11.1](32_one_functional_four_forces_v0.2%20(2).md) emergent-gravity-positioning discipline. **Audit β does not promote the cosmological claim**; it promotes the Lie-algebra-level structural identification, with the dimensional generalization at row 3 recorded as [A].
- **Three-outcome matched-pair (§3.1 + [v2insert-04](v2insert-04.md) §3.1).** K/L/joint-on-disjoint pre-claimed in §0; realized branch is **joint-on-disjoint**, with the joint-on-disjoint locus identified as row 3 (dimensional gap between HH's 1-dim imaginary time and program's $\dim_{\mathrm M}$-dim M-Euclidean sub-bundle).
- **Failures-first-class (§3.6).** The dimensional gap at row 3 is recorded explicitly, not absorbed into the K-branch or relabeled as an L-branch refutation. The audit's load-bearing sub-finding is precisely the structural feature that the binary K/L pre-claim would have hidden.
- **Dimensional firewall ([Paper 32 §11.2](32_one_functional_four_forces_v0.2%20(2).md)).** No physical constants. No Planck length, no $G$, no $\hbar$, no Bekenstein–Hawking temperature in physical units. All quantities are dimensionless Lie-algebra structural identities and integer dimension counts.
- **Carried-label discipline ([Paper 32 §11.4](32_one_functional_four_forces_v0.2%20(2).md)).** The labels *Wick rotation*, *No-Boundary Proposal*, *Hawking radiation*, *Lorentz algebra*, *imaginary time*, *Euclidean 4-sphere* are anchored to peer-reviewed sources before each use. The label *Lie algebra of Wick rotation* is internal program language for the Lie-algebra-level structural identification audit β performs; it is distinct from the peer-reviewed *Wick rotation* itself and is used consistently in that sense throughout this settlement.

---

## 6. Implications for Paper 46

The settlement implies the following manuscript-edit absorption:

1. **§4.2 — augment the dictionary table with a fifth column for Lie-algebra audit status.** Rows 1, 2, 4, 5 mark [P]-spirit; row 3 marks [P]-spirit (algebra) + [A] (dimensional generalization).

2. **§4 — add a new §4.4 (audit β settlement) summarizing the row-by-row tier promotion and the joint-on-disjoint sub-finding.** Reference this settlement file for the full Lie-algebra derivation.

3. **§5 — extend the dimensional table of §5.1 to include the *Wick-rotation parameter dimension* column equal to $\dim_{\mathrm M}$ per row.** Records the row-3 generalization as quantitative across the primorial ladder.

4. **§8.1 — replace the audit-β-open carry-forward with audit β settled.** Cite this settlement file.

5. **Reproducibility artifacts — add this settlement record.** Non-computational audits are absorbed into the artifact list at the same tier as computational ones.

---

## 7. Discipline closing note

This settlement is the program's first *pure-mathematics* row-generalization audit settled by structural identification rather than deterministic float computation. The pattern (Lie-algebra structural dictionary as a tier-promotion mechanism) is itself a methodological observation worth recording, but per [Paper 35](35_grounded_paranoid_delusional_methodology.md) §7 (no self-promotional claims), the methodological reading is left implicit: the worked record of audit β is on file; its general significance is not asserted here.

The grounded-paranoid-delusional grammar, once more: delusion proposed that the Hartle–Hawking dictionary on $\mathcal{D}^\circ(\mathbb C^6)$ admits a Lie-algebra-level identification on every row; paranoia bounded this with a binary-to-three-outcome matched-pair pre-claim; grounded executed the row-by-row Lie-algebra check and recorded **K (clean Lie-algebra match) on four rows + joint-on-disjoint (algebra match plus dimensional generalization) on one row**. The dimensional generalization is the audit's load-bearing positive finding, *not* a refutation — Hartle–Hawking's 1-dim imaginary time is the $\dim_{\mathrm M} = 1$ degenerate limit of a $\dim_{\mathrm M}$-parametric structure visible on every nontrivial mixed CRT row.

---

*End audit β settlement. Status: settled, joint-on-disjoint. Paper 46 C2 promoted from [A] structural dictionary to [P]-spirit at the Lie-algebra tier on rows 1, 2, 4, 5; [P]-spirit (algebra) + [A] (dimension) at row 3. Manuscript-edit absorption proposed for Paper 46 §4.2, §4.4, §5.1, §8.1, and reproducibility artifacts. No new audits opened. Total work: pure-mathematics Lie-algebra check; no compute consumed.*
