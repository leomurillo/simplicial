# FC3 Bounded Cost Ledger: F4[u]/(u^2)

This is the first exact split-cost ledger for FC3.  It imports the
bounded FC1 atlas and the B0-B4 information-investment audits without
turning support projection into full filtered closure.

## Ledger Summary

| channel | value | reading |
|---|---:|---|
| generated-subgroup descent mean J | 0.093056 | zero structural baseline on the held-out frontier |
| generated-subgroup resource | 0.372222 | mean support/resource paid by D_G(S) |
| normalizer transfer gain | 1.498377 | expected structural gain on normalizer-transfer audit |
| normalizer transfer premium | 0.167708 | resource-weighted symmetry premium |
| normalizer break-even margin | 1.330668 | positive means B3 pays on this audit distribution |
| PSL lambda_crit | 55.406250 | row break-even for shallow PSL depth |
| full filtered residual | 1569 | true [kappa]-sourced local carry mass |
| support projection residual | 0 | support-only pricing channel |
| H4-visible atoms | 72 | Fisher-shadow incidence channel |
| H3-contraction visible atoms | 1470 | weaker contraction-shadow channel |
| remaining hidden atoms | 27 | not visible to tested H4/H3 channels |
| support underpricing gap | 1569 | full minus support residual |

## Visibility Fractions

| field | fraction of full residual |
|---|---:|
| support_projection | 0.000000 |
| h4_visible | 0.045889 |
| h3_contraction_visible | 0.936902 |
| remaining_hidden | 0.017208 |
| support_underpricing_gap | 1.000000 |

## Resource Skeleton

| field | value |
|---|---:|
| seed_coordinates | 637 |
| tuple_size | 14 |
| aggregate_tuple_supports | 1961256 |
| size24_orbits | 1674272 |
| size24_sign_nontrivial | 1248 |
| carry_pair_chart_orbits_not_simultaneous | 20091354 |

## Checks

| check | observed | expected | pass |
|---|---|---|---|
| fc1_certificate_pass | `true` | `true` | True |
| residual_visibility_partition | `1569` | `1569` | True |
| support_projection_erases_full_residual | `[1569, 0]` | `[1569, 0]` | True |
| support_only_underpricing_gap_positive | `1569` | `"> 0"` | True |
| generated_subgroup_zero_structural_frontier | `{"balance": 0.0, "closure": 0.0, "fisher": 0.0, "reciprocal": 0.0}` | `"all near 0"` | True |
| normalizer_transfer_break_even | `1.3306682751172347` | `"> 0"` | True |
| psl_dagger_holds | `true` | `true` | True |

## Reading

The bounded FC3 theorem should start from the generated-subgroup baseline,
add the normalizer premium only under the transfer break-even rule, and
price local carry through the full filtered residual and its declared
visibility partition.  On this certified row, support-only pricing sees
`0` carry atoms while the full filtered ledger sees `1569`.
