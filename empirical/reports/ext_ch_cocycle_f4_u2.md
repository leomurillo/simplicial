# Ext_CH Cocycle Reducer

- ring: F_4[u]/(u^2)
- Gamma size: 24
- raw atom count: 1569
- raw carry pair count: 369
- atom orbit count: 71
- pair orbit count: 20
- atom orbit missing total: 0
- pair orbit missing total: 0
- raw coefficient distribution: {'-1': 1569}

## Raw Path Distribution

- u->u->u: 9
- u->u->u^2: 36
- u^2->u->u: 36
- u^2->u->u^2: 912
- u^2->u^2->u^2: 576

## Canonical Pair-Orbit Representative Table

| orbit | size | atoms | path | representative | coeffs |
|---:|---:|---:|---|---|---|
| 1 | 3 | 3 | u->u->u | `(w+1)u <- (w+1)u (u->u->u)` | `{'-1': 3}` |
| 2 | 6 | 6 | u->u->u | `(w+1)u <- u (u->u->u)` | `{'-1': 6}` |
| 3 | 24 | 24 | u->u->u^2 | `1 <- (w+1)u (u->u->u^2)` | `{'-1': 24}` |
| 4 | 12 | 12 | u->u->u^2 | `1 <- u (u->u->u^2)` | `{'-1': 12}` |
| 5 | 24 | 24 | u^2->u->u | `(w+1)u <- 1 (u^2->u->u)` | `{'-1': 24}` |
| 6 | 12 | 12 | u^2->u->u | `(w+1)u <- w+1 (u^2->u->u)` | `{'-1': 12}` |
| 7 | 12 | 108 | u^2->u->u^2 | `1 <- 1 (u^2->u->u^2)` | `{'-1': 108}` |
| 8 | 24 | 216 | u^2->u->u^2 | `1 <- 1+(w+1)u (u^2->u->u^2)` | `{'-1': 216}` |
| 9 | 12 | 108 | u^2->u->u^2 | `1 <- 1+u (u^2->u->u^2)` | `{'-1': 108}` |
| 10 | 24 | 120 | u^2->u->u^2 | `1 <- w (u^2->u->u^2)` | `{'-1': 120}` |
| 11 | 24 | 120 | u^2->u->u^2 | `1 <- w+(w+1)u (u^2->u->u^2)` | `{'-1': 120}` |
| 12 | 24 | 120 | u^2->u->u^2 | `1 <- w+1+(w+1)u (u^2->u->u^2)` | `{'-1': 120}` |
| 13 | 24 | 120 | u^2->u->u^2 | `1 <- w+1+u (u^2->u->u^2)` | `{'-1': 120}` |
| 14 | 12 | 48 | u^2->u^2->u^2 | `1 <- 1 (u^2->u^2->u^2)` | `{'-1': 48}` |
| 15 | 24 | 96 | u^2->u^2->u^2 | `1 <- 1+(w+1)u (u^2->u^2->u^2)` | `{'-1': 96}` |
| 16 | 12 | 48 | u^2->u^2->u^2 | `1 <- 1+u (u^2->u^2->u^2)` | `{'-1': 48}` |
| 17 | 24 | 96 | u^2->u^2->u^2 | `1 <- w (u^2->u^2->u^2)` | `{'-1': 96}` |
| 18 | 24 | 96 | u^2->u^2->u^2 | `1 <- w+(w+1)u (u^2->u^2->u^2)` | `{'-1': 96}` |
| 19 | 24 | 96 | u^2->u^2->u^2 | `1 <- w+1+(w+1)u (u^2->u^2->u^2)` | `{'-1': 96}` |
| 20 | 24 | 96 | u^2->u^2->u^2 | `1 <- w+1+u (u^2->u^2->u^2)` | `{'-1': 96}` |

## Coboundary Reduction

- mode: full_block
- C1 generators: 3204
- C2 dimension: 76320
- coboundary rank: 3204
- raw support: 1569
- residual support: 1569
- raw is coboundary: False

## Interpretation

The canonical pair-orbit table is the normalized Ext_CH representative
for the current section of the filtered adjacency algebra.  The
coboundary engine is explicit and finite; a selected gauge model can be
used to test which section changes preserve or trivialize the carry.
