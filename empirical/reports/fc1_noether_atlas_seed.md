# FC1 Noether Atlas Seed

This report freezes the finite coordinate skeleton for the next FC1
Noether orbit/stabilizer computation.  It is not the tuple-orbit census
yet; it is the finite input table for that census.

| row | ring | gamma size | packets | H3 | H4 | K_CH orbits | carry pair orbits | seed coords | residual full/support |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| f16-field | F_16 | 60 | 1 | 2 | 7 | 0 | 5 | 15 | 225/0 |
| f2-u4-control | F_2[u]/(u^4) | 32 | 4 | 7 | 32 | 1148 | 33 | 1224 | 1540/0 |
| f2-u5 | F_2[u]/(u^5) | 128 | 5 | 12 | 72 | 6656 | 81 | 6826 | 19140/0 |
| f4-u2 | F_4[u]/(u^2) | 24 | 2 | 5 | 18 | 592 | 20 | 637 | 1569/0 |
| f8-u2 | F_8[u]/(u^2) | 168 | 2 | 8 | 86 | 17944 | 49 | 18089 | 158081/0 |

## Next Computation

For a fixed polynomial jet order `r`, enumerate Hamiltonian tuple
support patterns inside the seed coordinate set, compute normalizer
stabilizers, compute determinant characters on each stabilized tuple,
and attach the Paper 11 closure-defect and FC2 filtered residual data.

The seed coordinate count is deliberately conservative bookkeeping:
it prevents support-level closure, K_CH-visible closure, and full
filtered closure from being collapsed into one number.
