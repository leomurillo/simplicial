# FC1 Noether Tuple Census: F4[u]/(u^2) Small Skeleton

This is the first tuple-support baseline after the orbit-skeleton
certificate.  The coordinates are aggregate normalizer orbit-buckets,
so every coordinate is fixed by `Gamma_R`; every tuple support has full
stabilizer and trivial determinant character.

## Scope

- row: `f4-u2`
- ring: `F_4[u]/(u^2)`
- status: `small aggregate tuple-support baseline; nontrivial 637-coordinate tuple census deferred`
- certificate pass: `True`
- Hamiltonian tuple size: `14`
- this is not the full 637-coordinate tuple census.

## Coordinate Skeleton

| kind | count |
| --- | --- |
| carry_pair_orbit | 20 |
| packet_energy | 2 |
| residual_visibility_bucket | 2 |

## Tuple Census

| field | value |
| --- | --- |
| coordinate count | 24 |
| tuple support total | 1961256 |
| normalizer orbit count | 1961256 |
| orbit size distribution | 1:1961256 |
| stabilizer order distribution | 24:1961256 |
| determinant character distribution | trivial:1961256 |

## Visibility Coverage

| coverage | count |
| --- | --- |
| both_h4_visible_and_remaining_hidden | 646646 |
| h4_visible_only | 497420 |
| no_visibility_bucket | 319770 |
| remaining_hidden_only | 497420 |

## Category Counts

| support category | count |
| --- | --- |
| (('carry_pair_orbit', 10), ('packet_energy', 2), ('residual_visibility_bucket', 2)) | 184756 |
| (('carry_pair_orbit', 11), ('packet_energy', 1), ('residual_visibility_bucket', 2)) | 335920 |
| (('carry_pair_orbit', 11), ('packet_energy', 2), ('residual_visibility_bucket', 1)) | 335920 |
| (('carry_pair_orbit', 12), ('packet_energy', 0), ('residual_visibility_bucket', 2)) | 125970 |
| (('carry_pair_orbit', 12), ('packet_energy', 1), ('residual_visibility_bucket', 1)) | 503880 |
| (('carry_pair_orbit', 12), ('packet_energy', 2), ('residual_visibility_bucket', 0)) | 125970 |
| (('carry_pair_orbit', 13), ('packet_energy', 0), ('residual_visibility_bucket', 1)) | 155040 |
| (('carry_pair_orbit', 13), ('packet_energy', 1), ('residual_visibility_bucket', 0)) | 155040 |
| (('carry_pair_orbit', 14), ('packet_energy', 0), ('residual_visibility_bucket', 0)) | 38760 |

## Residual Ledger Inherited From Base Certificate

| field | value |
| --- | --- |
| full filtered residual | 1569 |
| support projection residual | 0 |
| H4-visible atoms | 72 |
| H3-contraction visible from H4-invisible | 1470 |
| remaining invisible atoms | 27 |

## Count Checks

| check | observed | expected | pass |
| --- | --- | --- | --- |
| coordinate count | 24 | 24 | True |
| tuple support count | 1961256 | 1961256 | True |
| category formula agrees with enumeration | 9 entries | 9 entries | True |
| coverage partition | 1961256 | 1961256 | True |
| normalizer orbits equal supports on aggregate skeleton | 1961256 | 1961256 | True |
| stabilizer order is full Gamma_R | 24 | 24 | True |
| determinant character baseline | "trivial" | "trivial" | True |
| support/full residual still distinguished | [1569, 0] | [1569, 0] | True |
| hidden residual bucket retained | true | true | True |

## Reading

This baseline proves that the tuple-census machinery can enumerate
`C(24,14)` finite supports, assign full stabilizer `Gamma_R`, and
emit the determinant-character ledger without collapsing the residual
visibility fields.  It is intentionally too aggregated to produce
nontrivial determinant characters.

The next layer should replace selected aggregate buckets by individual
normalizer-moving representatives, then recompute stabilizers and
determinants.

Source: `empirical/reports/fc1_noether_atlas_census_f4_u2.json`
