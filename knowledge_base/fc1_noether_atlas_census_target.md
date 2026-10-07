# FC1 Noether Atlas Census Target

Created: 2026-05-15

This note records the next proof target after the FC1 finite-jet theorem
pieces.  It is a census target, not a completed theorem.  Its purpose is to
close the remaining FC1 dependency before the FC3 information-investment
unification theorem is upgraded.

## Target Row

The first row should be `F_4[u]/(u^2)`.

Reason: it is the smallest mixed local row with all current ingredients
available at exact finite level:

- gamma size: `24`;
- packet-energy coordinates: `2`;
- H3 orbits: `5`;
- H4 orbits: `18`;
- `K_CH` commutator orbits: `592`;
- carry-pair orbits: `20`;
- seed coordinates: `637`;
- full/support residual split: `1569/0`;
- atom-boundary H4 incidence: `72` visible and `1497` invisible.

## Statement To Prove

Fix the row `R = F_4[u]/(u^2)`, finite adjacency/Fisher-jet order `k`,
polynomial jet order `r`, and an explicitly declared finite support or
coefficient skeleton inside the seed coordinate set emitted by
`empirical/fc1_noether_atlas_seed.py`.

Then the exact decomposable finite-sufficient Hamiltonian tuples in that
skeleton have a finite Noether atlas:

1. finitely many normalizer orbits of tuple supports/coefficient patterns;
2. a stabilizer subgroup for every orbit representative;
3. a determinant character for every stabilized Hamiltonian tuple;
4. closure-defect labels `D_m^S` through order `k`;
5. local filtered residual labels sourced by the FC2 section class `[kappa]`,
   with support-visible, H4-visible, H3-contraction-visible, and full filtered
   costs kept as distinct fields.

This does not classify arbitrary smooth invariant functions or all
Fisher-volume-preserving currents.  It classifies the declared finite
Noether atlas at fixed row/order/skeleton data.

## Dependencies Already Available

- FC1-A: centroid finite-sufficient normalizer-equivariant quadratic jets are
  packet energies plus packetwise orthogonal refinements.
- FC1-B1: finite-sufficient Hamiltonian differentials pull back through
  `Phi_{R,k}` and exact decomposable currents live in the exterior power of
  the finite differential module.
- FC1-C: off-centroid closure through order `k` is equivalent to vanishing
  finite defects `D_m^S`; the first failure is quotient-character adjacency
  carry.
- FC2-B: `[kappa]` is the filtered source; `K_CH`, H4, and higher jets are
  Fisher-shadow projections modulo kernel.
- Current seed report: `empirical/reports/fc1_noether_atlas_seed.md`.
- Current FC2 reports:
  `empirical/reports/fc2_row_classification.md`,
  `empirical/reports/fc2_visible_fisher_kernel.md`,
  `empirical/reports/fc2_atom_shadow_map.md`, and
  `empirical/reports/fc2_h4_contraction_shadow.md`.

## Missing Lemmas And Computations

1. Define the first census skeleton.  Recommended first pass:
   `row=f4-u2`, `k=1`, `r=1`, support skeleton over packet energies, H3/H4
   family orbits, `K_CH` commutator orbit representatives, carry-pair orbits,
   and atom-boundary H4 incidence buckets.
2. Implement canonical normalizer action on the seed coordinate list.
3. Enumerate tuple support orbits under the normalizer action.
4. For each orbit representative, compute the stabilizer and determinant
   character on the span of the chosen Hamiltonian tuple.
5. Attach `D_m^S` closure-defect labels and `[kappa]` residual labels without
   collapsing support closure, Fisher-shadow visibility, and full filtered
   closure.
6. Emit JSON and Markdown certificates with independent count checks:
   orbit-stabilizer sums, determinant-character consistency, and row-level
   residual-accounting conservation.

## Falsifiers And Boundary Conditions

- A tuple orbit requires a coordinate outside packet energies, quotient
  layers, quotient-character adjacency data, or `[kappa]`-labeled carry.
- Orbit-stabilizer counts fail to match the declared finite normalizer action.
- A determinant character cannot be computed consistently on a stabilizer.
- A closure defect appears before any quotient-character adjacency carry term.
- A report column treats support residual `0` as full filtered closure.
- A cost column treats `K_CH` as a standalone `Ext_CH` detector.

## Patch Plan

1. Add `empirical/fc1_noether_atlas_census.py`.
2. Reuse the existing seed JSON as input instead of rebuilding FC2 data.
3. Start with `f4-u2` only; keep larger rows gated until the census format is
   stable.
4. Emit:
   - `empirical/reports/fc1_noether_atlas_census_f4_u2.json`;
   - `empirical/reports/fc1_noether_atlas_census_f4_u2.md`.
5. After the first certificate passes count checks, update
   `knowledge_base/fc1_natural_macrovariable_theorem.md` only to say that the
   first census row has been emitted.  Do not update the claim graph until the
   certificate is reviewed.

## Execution Status

The first orbit-skeleton layer has been emitted:

- `empirical/fc1_noether_atlas_census.py`;
- `empirical/reports/fc1_noether_atlas_census_f4_u2.json`;
- `empirical/reports/fc1_noether_atlas_census_f4_u2.md`.

The certificate passes its count checks.  It verifies the finite base table
for the tuple census: packet-energy buckets, H3/H4 orbit buckets, `K_CH`
commutator orbit counts, carry-pair orbits, and the full/support/H4/H3
residual visibility split.  The full 14-Hamiltonian tuple support census is
still open and should be the next execution layer.

The first small tuple-support baseline has also been emitted:

- `empirical/fc1_noether_tuple_census_f4_u2.py`;
- `empirical/reports/fc1_noether_tuple_census_f4_u2_small.json`;
- `empirical/reports/fc1_noether_tuple_census_f4_u2_small.md`.

This baseline enumerates \(C(24,14)=1,961,256\) supports in the aggregate
orbit-bucket skeleton.  Since each aggregate bucket is fixed by the normalizer,
all supports have stabilizer order `24` and trivial determinant character.
This is a determinant-character baseline, not the final nontrivial tuple
census.  The next layer is to split selected aggregate buckets into individual
normalizer-moving representatives and recompute tuple stabilizers.

The first selected moving-coordinate layer has now been emitted:

- `empirical/fc1_noether_moving_tuple_census_f4_u2.py`;
- `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_selected.json`;
- `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_selected.md`.

It splits one size-12 carry-pair orbit on the `u->u->u^2` path.  With four
fixed macro/residual buckets, the 16-coordinate skeleton has `120` supports,
`15` normalizer orbits, stabilizer orders `1`, `2`, `4`, and `24`, and
nontrivial sign determinant characters on `12` orbit types.

The next full-orbit moving-coordinate layer has also been emitted:

- `empirical/fc1_noether_moving_tuple_census_f4_u2_size24.py`;
- `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_size24.json`;
- `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_size24.md`.

It splits one full size-24 carry-pair orbit on the same `u->u->u^2` path and
keeps the four fixed macro/residual buckets.  The 28-coordinate skeleton has
`40,116,600` supports, `1,674,272` normalizer orbits, orbit sizes
`2`, `4`, `6`, `8`, `12`, and `24`, stabilizer orders `1`, `2`, `3`,
`4`, `6`, and `12`, and `1,248` sign-nontrivial determinant-character orbit
types.  The certificate passes Burnside, orbit-stabilizer, support partition,
and residual-separation checks.  The simultaneous 637-coordinate tuple atlas
is an optional stronger extension, not a blocker for bounded FC1 closure.

The bounded carry-pair one-split atlas has now been emitted:

- `empirical/fc1_noether_carry_pair_atlas_f4_u2.py`;
- `empirical/reports/fc1_noether_carry_pair_atlas_f4_u2.json`;
- `empirical/reports/fc1_noether_carry_pair_atlas_f4_u2.md`.

It assesses all `20` canonical carry-pair orbits.  Six size-12 charts are
enumerated directly, twelve size-24 charts are certified by the verified
regular size-24 profile, and the size-3/size-6 charts are marked as requiring
companion coordinates.  Across these separate one-split charts, not as a
simultaneous atlas, the report records `20,091,354` normalizer orbit types and
`15,048` sign-nontrivial determinant-character chart orbit types.  Every chart
inherits the tuple-level residual label
`full/support/H4/H3/remaining = 1569/0/72/1470/27`.

The bounded FC1 atlas delivery certificate has also been emitted:

- `empirical/fc1_noether_atlas_final_certificate_f4_u2.py`;
- `empirical/reports/fc1_noether_atlas_certificate_f4_u2.json`;
- `empirical/reports/fc1_noether_atlas_certificate_f4_u2.md`.

This certificate gathers the analytic FC1-A/B1/C theorem status and the exact
finite atlas layers for the declared `F4[u]/(u^2)` scope.  It is the bounded
atlas demonstration layer for FC1, not empirical neural evidence and not the
simultaneous `C(637,14)` atlas.
