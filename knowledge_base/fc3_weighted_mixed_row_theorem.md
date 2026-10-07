# FC3-C Weighted Mixed-Row Information-Investment Theorem

Created: 2026-05-15

## Status

FC3-C is the scalarized mixed-row continuation of FC3-A/B.  It adds
task-dependent weights to the split ledger and attaches that ledger to the
mixed-row A0/J_infty statement without collapsing the full filtered,
support-visible, H4-visible, H3-contraction-visible, and remaining-hidden
fields.

This is a bounded theorem statement for finite abelian rows and the current
certified local rows.  It does not claim global quotient sufficiency, arbitrary
smooth invariant classification, or a universal learned-model optimizer.

## Setup

Let

```text
R = G_ab x product_p R_p
```

be a finite behavior algebra split into finite abelian descent factors and
certified local conductor-filtered rows.  A policy `D` consists of:

1. a reciprocal support closure on each abelian factor;
2. an optional normalizer saturation;
3. a PSL flag/depth choice on each local conductor row;
4. a declared local carry observation level;
5. a resource proxy.

The unspecialized FC3 vector ledger is

```text
J_split(D) =
  projection_error
  + reciprocal_projection_error
  + additive_closure_leakage
  + generated_subgroup_descent_cost
  + normalizer_symmetry_premium
  + PSL_boundary_carry
  + local_filtered_carry
  + resource_cost.
```

For a certified local row `R_p`, the local filtered-carry field is the
five-entry vector

```text
C_loc(R_p) = (full, support, H4, H3, remaining)
```

with

```text
H4 + H3 + remaining = full.
```

The current exact FC2 row-family ledger is

```text
full/support/H4/H3/remaining = 180555/0/6648/173404/503.
```

The first bounded FC1 Noether-atlas row imports the sharper row label

```text
F4[u]/(u^2): full/support/H4/H3/remaining = 1569/0/72/1470/27.
```

## Admissible Scalar Weights

A task-dependent scalarization is admissible when all weights are nonnegative
and the local carry is charged in one of the following noncollapsing modes.

### Full-Filtered Audit Mode

Use

```text
C_loc,w(R_p) =
  lambda_full * full(R_p)
  + lambda_support * support(R_p).
```

For filtered-closure-sensitive tasks, require `lambda_full > 0`.  Since the
support residual can vanish while the full filtered residual survives, a
support-only scalarization is faithful only to support-level tasks.

### Visibility-Partition Mode

Use

```text
C_loc,w(R_p) =
  lambda_support * support(R_p)
  + lambda_H4 * H4(R_p)
  + lambda_H3 * H3(R_p)
  + lambda_hidden * remaining(R_p).
```

For filtered-closure-sensitive tasks, require positive visibility weights on
all surviving partitions:

```text
lambda_H4 > 0, lambda_H3 > 0, lambda_hidden > 0.
```

The natural risk order is

```text
0 <= lambda_H4 <= lambda_H3 <= lambda_hidden,
```

because H4-visible atoms are most instrumented, H3-contraction visible atoms
are weaker support shadows, and remaining hidden atoms require richer
coefficient or higher-arity observables.

### No Double Counting Convention

Do not add both `lambda_full * full` and
`lambda_H4 * H4 + lambda_H3 * H3 + lambda_hidden * remaining` as if they were
independent carry masses.  The partition sums to the full residual.  A separate
`lambda_full` term is allowed only when it is explicitly an external audit
penalty for proving filtered closure rather than the row's primary carry price.

## The Scalar Functional

For an admissible weight vector `w`, define

```text
J_w(D; task) =
  E_task[
    a_proj * projection_error(D)
    + a_rec * reciprocal_projection_error(D)
    + a_cl * additive_closure_leakage(D)
    + a_desc * generated_subgroup_descent_cost(D)
    + a_psl * PSL_boundary_carry(D)
    + C_loc,w(D)
  ]
  + lambda_res * Resource(D).
```

Normalizer saturation is priced by replacing the generated-subgroup support
`D_G(S)=<S>\{0}` with `D_G^Gamma(S)=<Gamma.S>\{0}` and adding the resource
premium

```text
lambda_res * (Resource(D_G^Gamma(S)) - Resource(D_G(S))).
```

It is selected exactly when expected structural transfer gain exceeds this
resource-weighted premium.

## Theorem

**FC3-C. Weighted mixed-row information-investment theorem.**  Fix a finite
behavior algebra `R` with the row scope above, an admissible task weight vector
`w`, and a resource proxy monotone in declared support, symmetry completion,
and PSL/local observation depth.  Then:

1. On finite abelian rows, the unique minimum-resource zero-structural-cost
   support for generic reciprocal coefficients is

   ```text
   D_G(S) = <S> \ {0}.
   ```

   This is the FC3 zero-carry baseline.  Normalizer saturation is not free
   closure; it is an optional symmetry investment.

2. Among policies whose deployment distribution ranges over a declared
   normalizer orbit, the normalizer-saturated policy is selected if and only if

   ```text
   expected transfer gain
   >
   lambda_res * symmetry premium.
   ```

3. On a certified local row, support projection is not a filtered carry price.
   If `full > 0` and `support = 0`, then every scalarization with zero weight
   on the full residual or on all parts of its visibility partition is
   support-faithful at most; it is not filtered-faithful.

4. On the current exact FC2 local rows, the mixed local contribution is the
   rowwise sum of the separated ledgers.  In particular the aggregate

   ```text
   180555/0/6648/173404/503
   ```

   proves that support-only pricing underprices every current local row with
   nonzero full filtered residual.

5. In the mixed-row A0/J_infty statement, CRT separates the local carry
   operators into rowwise contributions.  Cross-prime effects enter through
   task displacement, rank/resource coupling, and declared deployment
   expectations, not through a new cross-prime filtered extension class at this
   scope.

6. A PSL depth choice is justified rowwise by the Paper 12 carry-vs-depth
   threshold: full declared PSL depth beats a shallower flag whenever

   ```text
   lambda_PSL < lambda_PSL_crit(R_p)
   ```

   for the binding row in the declared product.  The current verified atlas
   keeps the binding row on the residue-degree-1 wild-depth sequence.

Therefore the bounded information-investment price decomposes as:

```text
minimal generated-subgroup descent
+ justified normalizer premium
+ certified PSL depth/boundary carry
+ filtered-faithful local carry scalarization
+ resource cost.
```

## Proof Spine

Items 1 and 2 are B1/B2/B3/B4: generated-subgroup descent is the minimal
support closure, while normalizer saturation is selected only by a
resource-weighted transfer inequality.

Item 3 is FC2 plus the FC1 handoff: `[kappa]` is the filtered source; `K_CH`,
H4, and H3 are Fisher-shadow or projection channels modulo kernel.  They do
not replace the full filtered class by themselves.

Item 4 is FC3-B: the current exact row-family ledger has support residual zero
and positive full filtered residual.

Item 5 is the CRT factorization of the quotient-character adjacency algebra
used in Paper 12 Theorem 9.2.1.  The scalar weights can couple rows through
task expectation and resource accounting, but the filtered local carry ledger
remains rowwise.

Item 6 is the Paper 12 PSL carry-vs-depth theorem and certificate.  It remains
compatible with FC3-C because PSL boundary carry and local filtered carry are
kept as separate cost fields.

## Boundary Lines

FC3-C does not claim:

- support residual `0` is full filtered closure;
- `K_CH` is an `Ext_CH` detector by itself;
- quotient sufficiency outside the declared finite skeleton;
- arbitrary smooth invariant functions or all Fisher-volume-preserving
  currents are classified;
- learned-model transfer follows from the finite row ledger alone;
- Bures, transformer, FEP, primorial, or RH material belongs in the core FC3
  proof spine.

