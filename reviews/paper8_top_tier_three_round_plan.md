# Paper 8 Top-Tier Three-Round Plan

**Scope:** `8.parity_dual_simplices.md`

**Goal:** Move the paper from a strong parity-dual/stella-octangula resolution to a broader theory of cyclotomic spectral compounds.

---

## Round 1: Full Block-Sign Orbit Census

**Question.** What happens when the parity reflection \(\rho_2\) is replaced by the full block-sign group

```text
B_N = <rho_d : d | N, d > 1>?
```

**Deliverables.**

1. Exact rational census for small `N`.
2. Orbit-size theorem for the number of distinct simplex images.
3. Identification of the half-turn kernel for even `N`.
4. First angle-profile and vertex-count data for the full spectral compound.

**Success criterion.** Section 8 becomes more than an open problem: it contains the first structural theorem for `B_N`.

---

## Round 2: Few-Angle Tight Frame Theory

**Question.** What is the frame-theoretic value of these compounds if they are not ETFs?

**Candidate tasks.**

1. Prove tightness for parity-dual and full block-sign orbit compounds, with frame bounds.
2. Classify the number of distinct angles for small `N`, then seek a formula in terms of Ramanujan sums.
3. Compare the angle profiles to known few-angle tight frames, spherical designs, fusion frames, or association schemes.

**Success criterion.** Replace "not an ETF" with a positive frame-theoretic classification.

---

## Round 3: Polytope And Coxeter Upgrade

**Question.** What are the convex hulls and symmetry groups of the full spectral compounds?

**Candidate tasks.**

1. Compute f-vectors for full block-sign orbit compounds where possible.
2. Identify polar structures and whether they are known Coxeter/weight polytopes.
3. Relate refined Fourier-plane groups to Weyl groups, signed permutation groups, or finite unitary reflection groups.

**Success criterion.** The paper has a geometric classification program beyond the \(\Phi_2\) prism/free-sum theorem.

---

## Round 1 Status

Completed.

**Results.**

- Added `empirical/census_cyclotomic_block_signs.py`.
- Added `empirical/reports/cyclotomic_block_signs.md`.
- Promoted the first block-sign theorem into Section 8 of `8.parity_dual_simplices.md`.
- The block-sign orbit has `2^(tau(N)-1)` distinct simplices for odd `N`, and `2^(tau(N)-2)` for even `N`, because the cyclic half-turn is a nontrivial block-sign element fixing `V_N`.
- Distinct simplex images are vertex-disjoint.
- Cross-Gram entries are governed exactly by Ramanujan sums:

```text
<v_i, T_epsilon v_j> = (1/N) sum_{d|N, d>1} epsilon_d c_d(i-j).
```

**Implication.** Round 2 should focus on the Ramanujan-sum angle algebra and few-angle/projective tight-frame interpretation, not on discovering the orbit size.

---

## Updated Round 2 Plan

**Goal:** turn the full block-sign compound from a census object into a frame-theoretic theorem.

1. Prove that the full block-sign spectral compound is a unit-norm tight frame after normalization.
2. Use the Ramanujan-sum cross-Gram formula to express its projective angle set.
3. Separate ordinary coherence, which is always `1` because the compound is centrally symmetric, from non-antipodal/projective coherence.
4. Check whether the angle relations define an association scheme or fusion-frame structure for small `N`.

**Target manuscript result:** a theorem or proposition titled something like `Ramanujan Few-Angle Tight Frame`.

---

## Updated Round 3 Plan

**Goal:** classify the convex hulls and symmetry groups of the full block-sign spectral compounds.

1. Compute exact polytope data for `X_N^spec` for tractable `N`.
2. Determine whether the full block-sign convex hull has a product/free-sum/polar description analogous to the parity-dual case.
3. Analyze the stabilizer of `X_N^spec`: start with the normalizer of the cyclotomic block-sign group inside the coordinate/Galois normalizer, then compare with the full Gram/orthogonal stabilizer.
4. Only after the real block-sign case is classified, revisit Fourier-plane refinements and finite unitary reflection groups.

**Target manuscript result:** a structural theorem for at least one nontrivial full block-sign family, such as squarefree `N` or prime powers.

---

## Round 3 Status

Completed as a first theorem-plus-census pass.

**Results.**

- Added `empirical/census_cyclotomic_block_polytope.py`.
- Added `empirical/reports/cyclotomic_block_polytope.md`.
- Added a general polar description:

```text
conv(X_N^spec)^o = intersection_T T([-1,1]^N cap H_N).
```

- Proved the prime-family hull theorem: for odd prime `p`,

```text
X_p^spec = V_p union -V_p,
conv(X_p^spec)^o = [-1,1]^p cap H_p.
```

- Added the prime-family f-vector formula and stabilizer `C_2 x S_p`.
- Computed the first composite full spectral hull exactly at `N=6`, with f-vector `(24, 108, 192, 144, 38)`.
- With SciPy available, added Qhull-seeded exact rational face-lattice reconstructions for `N=8,9,10`.
- Computed exact coordinate stabilizer data for `N=6,8,9,10,12` using coordinate-pair color upper bounds.

**Implication.** The composite theory is genuinely arithmetic.  The next round should split prime powers, squarefree composites, and full orthogonal stabilizers instead of expecting one immediate product/free-sum classification.

## Round 4 Seed: Prime-Power Stabilizers

Started.

**Results.**

- Added `empirical/verify_prime_power_stabilizers.py`.
- Added `empirical/reports/prime_power_stabilizers.md`.
- Promoted a prime-power coordinate-stabilizer theorem into Section 8.
- For odd prime powers `N=p^r`, the coordinate stabilizer is the rooted p-adic congruence-tree automorphism group, an iterated wreath product with `r` copies of `S_p`.
- For powers of two `N=2^r`, `r>=3`, the top two binary levels fuse into four-point `S_4` fibers over residues modulo `2^(r-2)`.

**Implication.** The prime-power branch is no longer a census-only phenomenon.  The next natural lift is squarefree and mixed composites, with `N=6,10,12,15` as the first comparison set.

## Round 4 Seed: Mixed-Composite Stabilizers

Started.

**Results.**

- Added `empirical/verify_mixed_composite_stabilizers.py`.
- Added `empirical/reports/mixed_composite_stabilizers.md`.
- Added a mixed-composite stabilizer census subsection to Section 8.
- Verified exact upper/lower stabilizer matches for `N=6,10,12,15,18,20`.

**Implication.** The mixed branch now has a vocabulary: parity collapse (`N=6,10`), CRT product separation (`N=15,20`), divisor-scheme blow-up (`N=18`), and divisor-lattice rigidity (`N=12`).

## Round 4 Seed: N=6 Hull Structure

Completed.

**Result.** Promoted the `N=6` composite hull from exact enumeration to an analytic theorem:

```text
P_6^spec ~= (hexagon free-sum hexagon) x I.
```

**Implication.** Section 8 now has a structural bridge between the parity-only prism theorem and the full composite census.
