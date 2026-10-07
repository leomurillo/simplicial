# Parity-Dual Even-N Census

**Script:** `empirical/census_parity_dual_simplices.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** all checks passed

This census covers the compound `V_N union W_N` for even `N=4,6,8,10,12`, where `W_N=rho_2(V_N)`.  All Gram profiles are exact rational counts.  Coherence is computed after unit-normalizing the vectors.  The Welch bound is included as a packing baseline for `2N` unit vectors in dimension `N-1`.

The coordinate stabilizer is the subgroup of ambient coordinate permutations preserving the compound.  For `N=4` this is the full tetrahedral coordinate action `S_4`.  For `N=2m>=6`, Theorem 6.1 of the companion note proves the parity-class wreath product `(S_m x S_m) semidirect C_2`, of order `2(m!)^2`, preserving or swapping the even/odd coordinate classes.  The full Gram automorphism group, equivalently the ambient orthogonal stabilizer, additionally includes the simplex-swap induced by `rho_2`; for `N=4` this is the full cube/stella-octangula order `48`.

| N | dim | raw off-diagonal Gram profile | normalized absolute profile | coherence | Welch | coordinate stabilizer | full Gram/orthogonal stabilizer | central inversion |
|---:|---:|---|---|---:|---:|---:|---:|---|
| 4 | 3 | `-3/4:4; -1/4:12; 1/4:12` | `1/3:24; 1:4` | 1 (1.000000) | 0.487950 | 24 | 48 | yes |
| 6 | 5 | `-1/2:12; -1/6:30; 1/6:18; 1/2:6` | `1/5:48; 3/5:18` | 3/5 (0.600000) | 0.356753 | 72 | 144 | no |
| 8 | 7 | `-3/8:24; -1/8:56; 1/8:32; 5/8:8` | `1/7:88; 3/7:24; 5/7:8` | 5/7 (0.714286) | 0.292770 | 1152 | 2304 | no |
| 10 | 9 | `-3/10:40; -1/10:90; 1/10:50; 7/10:10` | `1/9:140; 1/3:40; 7/9:10` | 7/9 (0.777778) | 0.253629 | 28800 | 57600 | no |
| 12 | 11 | `-1/4:60; -1/12:132; 1/12:72; 3/4:12` | `1/11:204; 3/11:60; 9/11:12` | 9/11 (0.818182) | 0.226679 | 1036800 | 2073600 | no |

## Brute Coordinate Checks

The coordinate stabilizer orders for `N=4,6,8` were verified by exhaustive enumeration of all ambient coordinate permutations.  The `N=10,12` entries use the closed-form parity-class stabilizer count, because brute force over `10!` and `12!` permutations is unnecessary for this census.

| N | brute coordinate stabilizer | formula |
|---:|---:|---:|
| 4 | 24 | 24 |
| 6 | 72 | 72 |
| 8 | 1152 | 1152 |

## Consequences

1. The `N=4` case is exceptional: `W_4=-V_4` up to relabeling, central inversion preserves the compound, and the full Gram/orthogonal stabilizer has order `48`.
2. For `N>=6`, central inversion does not preserve the compound.  The coordinate stabilizer is exactly the parity-class wreath product proved in Theorem 6.1.
3. The full compound is not a single ETF in these tested cases.  Each component simplex is an ETF, but the union has multiple normalized absolute inner products and does not meet the Welch bound.
4. The largest cross-angle grows with `N`: the coherence is `(N-3)/(N-1)` for `N>=8`, while the Welch baseline decreases.  This suggests the parity-dual compound is better studied as a structured two-simplex compound than as a Grassmannian packing candidate.
