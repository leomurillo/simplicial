# FC1 Noether Atlas Certificate: F4[u]/(u^2)

This is the bounded FC1 Noether-atlas delivery certificate for the
first mixed local row.  The analytic theorem is recorded in the FC1
knowledge-base notes; this artifact is the exact finite demonstration
layer for the declared atlas scope.

## Analytic Status

| piece | status |
| --- | --- |
| FC1-A | proved at centroid finite-sufficient quadratic jet scope |
| FC1-B1 | proved for fixed finite-jet exact decomposable currents |
| FC1-C | proved for fixed finite-jet off-centroid closure defects |
| certificate role | exact finite demonstration/computer-assisted certificate, not empirical neural evidence |

## Delivered Scope

- row: `f4-u2`
- ring: `F_4[u]/(u^2)`
- status: `bounded FC1 Noether-atlas certificate delivered`
- certificate pass: `True`
- tuple size: `14`
- seed coordinates: `637`
- this is a bounded finite atlas certificate, not the simultaneous `C(637,14)` atlas.

## Layer Summary

| layer | value |
| --- | --- |
| base seed coordinates | 637 |
| base K_CH commutator orbits | 592 |
| base carry-pair orbits | 20 |
| aggregate tuple supports | 1961256 |
| aggregate determinants | trivial baseline |
| selected size-12 orbits | 15 |
| selected size-12 sign-nontrivial | 12 |
| size-24 supports | 40116600 |
| size-24 orbits | 1674272 |
| size-24 sign-nontrivial | 1248 |
| carry-pair charts | {"enumerated": 6, "enumerated_by_regular_size24_profile": 12, "requires_companion_coordinates": 2} |
| carry-pair chart orbits, not simultaneous | 20091354 |

## Tuple-Level Residual Label

| field | value |
| --- | --- |
| source | FC2 filtered section class [kappa] |
| support projection residual | 0 |
| full filtered residual | 1569 |
| H4-visible atoms | 72 |
| H3-contraction visible from H4-invisible | 1470 |
| remaining invisible atoms | 27 |

## Count Checks

| check | observed | expected | pass |
| --- | --- | --- | --- |
| component certificates pass | {"aggregate_tuple": true, "base": true, "carry_pair_atlas": true, "selected_size12": true, "size24": true} | {"aggregate_tuple": true, "base": true, "carry_pair_atlas": true, "selected_size12": true, "size24": true} | True |
| seed coordinate count | 637 | 637 | True |
| aggregate tuple support count | 1961256 | 1961256 | True |
| selected size-12 moving chart orbits | 15 | 15 | True |
| size-24 moving chart support/orbits | [40116600, 1674272] | [40116600, 1674272] | True |
| carry-pair atlas assessed/capable/companion | [20, 18, 2] | [20, 18, 2] | True |
| support/full residual kept separate | [1569, 0] | [1569, 0] | True |
| residual visibility partition | 1569 | 1569 | True |

## Non-Claims

- simultaneous C(637,14) tuple enumeration
- all K_CH commutator coordinates split
- arbitrary smooth invariant functions
- all Fisher-volume-preserving currents
- global sufficiency beyond the declared finite skeleton

## Sources

- `base_census`: `empirical/reports/fc1_noether_atlas_census_f4_u2.json`
- `aggregate_tuple`: `empirical/reports/fc1_noether_tuple_census_f4_u2_small.json`
- `selected_size12`: `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_selected.json`
- `size24`: `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_size24.json`
- `carry_pair_atlas`: `empirical/reports/fc1_noether_carry_pair_atlas_f4_u2.json`
- `fc1_theorem_note`: `knowledge_base/fc1_natural_macrovariable_theorem.md`
- `fc1_census_target`: `knowledge_base/fc1_noether_atlas_census_target.md`
