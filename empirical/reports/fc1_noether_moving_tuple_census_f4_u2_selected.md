# FC1 Noether Moving Tuple Census: F4[u]/(u^2) Selected Orbit

This is the first non-aggregate tuple census.  It splits one
normalizer-moving carry-pair orbit into individual coordinates and
computes support orbits, stabilizers, and determinant signs exactly.

## Scope

- row: `f4-u2`
- ring: `F_4[u]/(u^2)`
- status: `selected moving-coordinate tuple census; one size-12 carry-pair orbit split`
- certificate pass: `True`
- tuple size: `14`
- coordinates: `16`
- selected carry-pair path: `u->u->u^2`
- selected carry-pair source index: `3`
- this is not the full 637-coordinate tuple census.

## Tuple Census

| field | value |
| --- | --- |
| support count | 120 |
| normalizer orbit count | 15 |
| orbit size distribution | 1:6, 6:1, 12:7, 24:1 |
| stabilizer order distribution | 1:1, 2:7, 4:1, 24:6 |
| determinant character distribution | sign-nontrivial:12, trivial:3 |

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
| coordinate count | 16 | 16 | True |
| selected moving orbit size | 12 | 12 | True |
| tuple support count | 120 | 120 | True |
| orbit-stabilizer total | 120 | 120 | True |
| orbit-stabilizer divisibility | true | true | True |
| nontrivial moving-coordinate orbits exist | true | true | True |
| nontrivial determinant character appears | true | true | True |
| support/full residual inherited separately | [1569, 0] | [1569, 0] | True |

## Orbit Representatives

| orbit | size | stabilizer | det | fixed ids | moving count |
| --- | --- | --- | --- | --- | --- |
| 0 | 6 | 4 | sign-nontrivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 10 |
| 1 | 12 | 2 | sign-nontrivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 10 |
| 2 | 12 | 2 | trivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 10 |
| 3 | 24 | 1 | trivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 10 |
| 4 | 12 | 2 | trivial | PE:u, PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 10 |
| 5 | 12 | 2 | sign-nontrivial | PE:u, PE:u^2, VIS:h4_visible | 11 |
| 6 | 12 | 2 | sign-nontrivial | PE:u, PE:u^2, VIS:remaining_invisible | 11 |
| 7 | 12 | 2 | sign-nontrivial | PE:u, VIS:h4_visible, VIS:remaining_invisible | 11 |
| 8 | 12 | 2 | sign-nontrivial | PE:u^2, VIS:h4_visible, VIS:remaining_invisible | 11 |
| 9 | 1 | 24 | sign-nontrivial | PE:u, PE:u^2 | 12 |
| 10 | 1 | 24 | sign-nontrivial | PE:u, VIS:h4_visible | 12 |
| 11 | 1 | 24 | sign-nontrivial | PE:u^2, VIS:h4_visible | 12 |
| 12 | 1 | 24 | sign-nontrivial | PE:u, VIS:remaining_invisible | 12 |
| 13 | 1 | 24 | sign-nontrivial | PE:u^2, VIS:remaining_invisible | 12 |
| 14 | 1 | 24 | sign-nontrivial | VIS:h4_visible, VIS:remaining_invisible | 12 |

## Reading

This is the first layer where determinant characters are not forced
to be trivial by aggregate buckets.  The selected moving orbit already
produces nontrivial sign characters on some tuple stabilizers.

The next layer should split either a full size-24 carry-pair orbit or
selected `K_CH` commutator representatives, while keeping the same
support/full/H4/H3 residual distinctions.

- `base_census`: `empirical/reports/fc1_noether_atlas_census_f4_u2.json`
- `ext_cocycle`: `empirical/reports/ext_ch_cocycle_f4_u2.json`
