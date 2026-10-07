# Paper 8 Round 3: Polytope and Stabilizer Upgrade

**Scope:** `8.parity_dual_simplices.md`, Section 8.

**Status:** Round 3 landed as a cautious theorem-plus-census layer.

---

## What Was Proved

The safe all-`N` convex-hull statement is polar rather than primal:

```text
conv(X_N^spec)^o = intersection_T T([-1,1]^N cap H_N),
```

where `T` ranges over representatives of the distinct block-sign simplex images.

This follows from the identity

```text
<y, T v_i> = (T y)_i
```

for `y in H_N`, since each block-sign operator is orthogonal and self-adjoint.

For odd prime `p`, this specializes completely:

```text
X_p^spec = V_p union -V_p,
conv(X_p^spec)^o = [-1,1]^p cap H_p.
```

The coordinate stabilizer is `S_p`, and the full orthogonal stabilizer is
`C_2 x S_p`.  The hull is simplicial, with

```text
f_k = sum_{a+b=k+1, |a-b| < p-k-1} p!/(a! b! (p-a-b)!).
```

In particular, the number of facets is

```text
p * binomial(p-1, (p-1)/2).
```

---

## Empirical Composite Results

The new script `empirical/census_cyclotomic_block_polytope.py` records:

| N | result |
|---:|---|
| 6 | exact f-vector `(24, 108, 192, 144, 38)`; facets have 8 or 12 vertices |
| 8 | SciPy/Qhull-seeded f-vector `(32, 192, 496, 684, 528, 216, 38)`; facets have 16 vertices; coordinate stabilizer `S_4 wr S_2`, order `1152` |
| 9 | SciPy/Qhull-seeded f-vector `(36, 486, 2616, 6660, 8928, 6378, 2196, 252)`; facets have 12 or 16 vertices; coordinate stabilizer `S_3 wr S_3`, order `1296` |
| 10 | SciPy/Qhull-seeded f-vector `(40, 380, 2020, 6640, 13660, 17400, 13200, 5400, 902)`; facets have 16 or 20 vertices; coordinate stabilizer `S_5 wr S_2`, order `28800` |
| 12 | coordinate stabilizer `Aff(Z/12)`, order `48` |

For `N=8,9,10`, Qhull supplies facet hyperplane hints, and the script reconstructs the exposed facets with exact rational arithmetic before counting the face lattice.  These rows should remain labeled as computational census data, not as a structural theorem.

The coordinate stabilizer counts are exact for these rows because the coordinate-pair color automorphism upper bound matches an explicit lower-bound group.

---

## Cautions

The composite cases do not yet admit a uniform product/free-sum description like the parity-only prism theorem.

The safe spectral-affine subgroup

```text
(B_N x Aff(Z/NZ))/K_N
```

has order `M_N N phi(N)`, but this is not generally the full stabilizer.  Prime dimensions expand to `C_2 x S_p`, while small composite coordinate stabilizers vary by arithmetic type.

No complex reflection group, association scheme, spherical design, or fusion-frame claim was made.

---

## Updated Round 4 Direction

The highest ROI next step is a family split:

1. Prime powers: explain why `N=8,9` have imprimitive coordinate wreath products, and determine whether this persists for `p^r` with `r >= 3`.
2. Squarefree composites: compare `N=6,10` against `N=12,15`; the stabilizer behavior changes sharply when more divisor layers interact.
3. Full orthogonal stabilizers: start with `N=6`, where the vertex count is only 24 and the exact f-vector is known.

## Round 4 Prime-Power Lift

Started and promoted into the manuscript.

**New theorem.** For odd prime powers `N=p^r`, the coordinate stabilizer of the full block-sign spectral compound is the automorphism group of the rooted p-adic congruence tree, equivalently an iterated wreath product with `r` copies of `S_p`:

```text
|G_coord(X_{p^r}^spec)| = product_{a=0}^{r-1} (p!)^(p^a).
```

For powers of two, `N=2^r`, `r>=3`, the top two binary levels fuse: the stabilizer preserves congruences through modulo `2^(r-2)` and has full `S_4` action inside each four-point fiber.  Its order is

```text
(4!)^(2^(r-2)) * product_{a=0}^{r-3} 2^(2^a).
```

**Verifier.** Added `empirical/verify_prime_power_stabilizers.py` and `empirical/reports/prime_power_stabilizers.md`.  The verifier checks exact coordinate-pair color partitions and generators for `N=8,9,16,25,27,32`.

**Implication.** The composite stabilizer story now has a real first classification family.  The next unknown is no longer "why are `N=8,9` wreath products?" but "how do squarefree and mixed divisor lattices break or collapse the p-adic tree pattern?"

## Round 4 Mixed-Composite Lift

Started and promoted as a census subsection.

**New verifier.** Added `empirical/verify_mixed_composite_stabilizers.py` and `empirical/reports/mixed_composite_stabilizers.md`.  It checks exact coordinate-pair color upper bounds and generator lower bounds for `N=6,10,12,15,18,20`.

**Results.**

| N | coordinate stabilizer |
|---:|---|
| 6 | `S_3 wr S_2`, order `72` |
| 10 | `S_5 wr S_2`, order `28800` |
| 12 | `Aff(Z/12)`, order `48` |
| 15 | `S_3 x S_5`, order `720` |
| 18 | `S_3^6 semidirect Aff(Z/6)`, order `559872` |
| 20 | `Aff(Z/4) x S_5`, order `960` |

**Implication.** Mixed composites are not one theorem yet.  The new organizing phrase is **divisor-lattice rigidity**: incompatible prime-power layers can either collapse to parity fibers, separate by CRT coordinates, blow up a smaller divisor scheme, or rigidify all the way down to the affine cyclic normalizer.

## N=6 Hull Lift

Promoted.

**New theorem.** The first composite spectral hull has an analytic decomposition:

```text
P_6^spec ~= (hexagon free-sum hexagon) x I.
```

This derives the f-vector `(24, 108, 192, 144, 38)` and facet sizes `8,12` without treating `N=6` as merely an enumerated composite row.  Conceptually, `rho_3` and `rho_6` turn the even/odd parity triangles into antipodal hexagons in the two zero-sum planes, while `rho_2` supplies the independent parity prism direction.
