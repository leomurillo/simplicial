# FC1 Noether Atlas Census: F4[u]/(u^2)

This is the first executable FC1 Noether-atlas census certificate.
It certifies the finite orbit skeleton for the smallest mixed local row.
It is not the full 14-Hamiltonian tuple-orbit census yet.

## Scope

- row: `f4-u2`
- ring: `F_4[u]/(u^2)`
- status: `first orbit-skeleton census certificate; full tuple enumeration deferred`
- certificate pass: `True`
- support residual `0` is kept separate from full filtered closure.
- `K_CH` is used only as a Fisher-shadow channel of `[kappa]`.

## Seed Coordinates

| block | count |
| --- | --- |
| packet energies | 2 |
| H3 orbit buckets | 5 |
| H4 orbit buckets | 18 |
| K_CH commutator orbits | 592 |
| carry-pair orbits | 20 |
| seed total | 637 |

## Count Checks

| check | observed | expected | pass |
| --- | --- | --- | --- |
| gamma size agrees across seed/local/ext | [24, 24, 24] | [24, 24, 24] | True |
| seed coordinate count | 637 | 637 | True |
| H3 orbit-size sum | 210 | 210 | True |
| H4 orbit-size sum | 3165 | 3165 | True |
| K_CH commutator orbit-size sum | 14112 | 14112 | True |
| carry-pair orbit-size sum | 369 | 369 | True |
| raw atom orbit-size sum | 1569 | 1569 | True |
| support/full residual kept separate | [1569, 0] | [1569, 0] | True |
| residual visibility partition | 1569 | 1569 | True |
| K_CH is not an Ext_CH detector | true | true | True |
| H3 contraction still leaves hidden residue | true | true | True |

## Orbit-Stabilizer Summary

| block | group | orbits | size distribution | stabilizer distribution |
| --- | --- | --- | --- | --- |
| H3 | Gamma_R x S3 | 5 | 6:1, 24:1, 36:1, 72:2 | 2:2, 4:1, 6:1, 24:1 |
| H4 | Gamma_R x S4 | 18 | 3:1, 12:1, 18:1, 36:1, 72:5, 144:3, 288:4, 576:2 | 1:2, 2:4, 4:3, 8:5, 16:1, 32:1, 48:1, 192:1 |
| K_CH commutator | Gamma_R | 592 | 12:8, 24:584 | 1:584, 2:8 |
| carry pairs | Gamma_R | 20 | 3:1, 6:1, 12:6, 24:12 | 1:12, 2:6, 4:1, 8:1 |
| raw atoms | Gamma_R | 71 | 3:1, 6:1, 12:8, 24:61 | 1:61, 2:8, 4:1, 8:1 |

## Residual Visibility Ledger

| field | value |
| --- | --- |
| full filtered residual atoms | 1569 |
| support projection residual | 0 |
| H4-visible atoms | 72 |
| H4-invisible atoms | 1497 |
| H3-contraction visible from H4-invisible | 1470 |
| remaining invisible atoms | 27 |

## Determinant Characters

At this orbit-bucket layer, each single coordinate bucket has trivial
one-dimensional determinant character on its stabilizer.  The tuple
determinant characters are deliberately not claimed here: they require
the next layer, where finite Hamiltonian tuple supports/coefficient
patterns are chosen and stabilized.

## Next Tuple Layer

Use this certificate as the finite base table for the first real tuple
enumeration.  The recommended first tuple skeleton is small: packet
energies, carry-pair buckets, the H4-visible incidence bucket, and
the remaining-invisible bucket.  Once that determinant-character
machinery passes, expand to all K_CH commutator orbit coordinates.

## Sources

- `seed`: `empirical/reports/fc1_noether_atlas_seed.json`
- `local_adjacency`: `empirical/reports/local_adjacency_constructor_f4_u2.json`
- `ext_cocycle`: `empirical/reports/ext_ch_cocycle_f4_u2.json`
- `ext_orbits`: `empirical/reports/f4_u2_ext_orbits.json`
- `atom_shadow`: `empirical/reports/fc2_atom_shadow_map.json`
- `h4_contraction_shadow`: `empirical/reports/fc2_h4_contraction_shadow.json`
