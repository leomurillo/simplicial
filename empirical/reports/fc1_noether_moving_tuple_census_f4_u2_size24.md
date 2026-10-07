# FC1 Noether Moving Tuple Census: F4[u]/(u^2) Size-24 Orbit

This is the next non-aggregate tuple census after the selected size-12
split.  It splits one full size-24 carry-pair orbit into individual
normalizer-moving coordinates and computes exact aggregate support
orbits, stabilizers, and determinant signs.

## Candidate Ranking

| rank | candidate | reading |
| --- | --- | --- |
| 1 | split one full size-24 carry-pair orbit | maximal FC1 dependency leverage among ready tasks: exact moving-coordinate tuple stabilizers/determinant characters without treating K_CH as an Ext detector or claiming FC3 |
| 2 | split selected K_CH commutator representatives | useful next FC1 layer, but higher overclaim risk because K_CH must remain only a Fisher-jet shadow of [kappa] |
| 3 | draft bounded FC3 information-investment theorem | central but premature until the FC1 tuple atlas has more non-aggregate stabilizer/determinant data |

## Scope

- row: `f4-u2`
- ring: `F_4[u]/(u^2)`
- status: `full size-24 carry-pair moving-coordinate tuple census`
- certificate pass: `True`
- tuple size: `14`
- coordinates: `28`
- selected carry-pair path: `u->u->u^2`
- selected carry-pair source index: `2`
- this is not the full 637-coordinate tuple census.
- support residual `0` is not treated as full filtered closure.
- `K_CH` remains only a Fisher-shadow channel of `[kappa]`.

## Tuple Census

| field | value |
| --- | --- |
| support count | 40116600 |
| normalizer orbit count | 1674272 |
| orbit size distribution | 2:18, 4:24, 6:126, 8:36, 12:5184, 24:1668884 |
| stabilizer order distribution | 1:1668884, 2:5184, 3:36, 4:126, 6:24, 12:18 |
| determinant character distribution | sign-nontrivial:1248, trivial:1673024 |

## By Fixed Coordinates

| fixed | moving | support count | tuple orbits | stabilizers | determinants |
| --- | --- | --- | --- | --- | --- |
| 0 | 14 | 1961256 | 82016 | 1:81422, 2:594 | sign-nontrivial:594, trivial:81422 |
| 1 | 13 | 9984576 | 416024 | 1:416024 | trivial:416024 |
| 2 | 12 | 16224936 | 678192 | 1:673992, 2:3996, 3:36, 4:126, 6:24, 12:18 | sign-nontrivial:60, trivial:678132 |
| 3 | 11 | 9984576 | 416024 | 1:416024 | trivial:416024 |
| 4 | 10 | 1961256 | 82016 | 1:81422, 2:594 | sign-nontrivial:594, trivial:81422 |

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
| coordinate count | 28 | 28 | True |
| selected moving orbit size | 24 | 24 | True |
| tuple support count | 40116600 | 40116600 | True |
| support partition by fixed-coordinate count | 40116600 | 40116600 | True |
| moving orbit Burnside check | {"10": 82016, "11": 104006, "12": 113032, "13": 104006, "14": 82016} | {"10": 82016, "11": 104006, "12": 113032, "13": 104006, "14": 82016} | True |
| full tuple Burnside check | 1674272 | 1674272 | True |
| orbit-stabilizer total | 40116600 | 40116600 | True |
| orbit-stabilizer divisibility | true | true | True |
| nontrivial determinant character appears | true | true | True |
| support/full residual inherited separately | [1569, 0] | [1569, 0] | True |

## Sample Orbit Types

| fixed | moving | stabilizer | det | fixed ids | moving sample |
| --- | --- | --- | --- | --- | --- |
| 0 | 14 | 1 | trivial | (none) | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 0 | 14 | 2 | sign-nontrivial | (none) | M:4, M:5, M:6, M:8, M:9, M:10, M:11, M:12, M:13, M:14 |
| 1 | 13 | 1 | trivial | PE:u | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 2 | 12 | 1 | trivial | PE:u, PE:u^2 | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 2 | 12 | 2 | trivial | PE:u, PE:u^2 | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 2 | 12 | 3 | trivial | PE:u, PE:u^2 | M:1, M:3, M:4, M:5, M:8, M:9, M:10, M:12, M:13, M:14 |
| 2 | 12 | 4 | sign-nontrivial | PE:u, PE:u^2 | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:11 |
| 2 | 12 | 6 | trivial | PE:u, PE:u^2 | M:2, M:3, M:4, M:5, M:8, M:9, M:10, M:11, M:12, M:13 |
| 2 | 12 | 12 | trivial | PE:u, PE:u^2 | M:0, M:1, M:4, M:5, M:8, M:9, M:12, M:13, M:14, M:15 |
| 3 | 11 | 1 | trivial | PE:u, PE:u^2, VIS:h4_visible | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 4 | 10 | 1 | trivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:9 |
| 4 | 10 | 2 | sign-nontrivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | M:0, M:1, M:2, M:3, M:4, M:5, M:6, M:7, M:8, M:13 |

## Reading

This layer gives the first full-orbit moving-coordinate tuple census.
It supplies exact non-aggregate stabilizer and determinant-character
metadata for a size-24 carry-pair orbit while preserving the FC1/FC2
hygiene boundaries.  It is still a declared finite skeleton, not a
classification of arbitrary smooth invariants or all decomposable
current coefficient patterns.

- `base_census`: `empirical/reports/fc1_noether_atlas_census_f4_u2.json`
- `ext_cocycle`: `empirical/reports/ext_ch_cocycle_f4_u2.json`
