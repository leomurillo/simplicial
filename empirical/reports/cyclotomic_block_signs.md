# Cyclotomic Block-Sign Census

**Script:** `empirical/census_cyclotomic_block_signs.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** all checks passed

For each `N`, the block-sign group

```text
B_N = <rho_d : d | N, d > 1>
```

acts on the regular simplex `V_N`.  The census computes the distinct simplex images and the angle profile of the resulting spectral compound.

The listed frame bound is for the unit-normalized compound in the `(N-1)`-dimensional zero-sum hyperplane.  Since the compound is centrally symmetric, ordinary coherence is always `1`; the non-antipodal/projective coherence is the useful packing statistic.

| N | block divisors | B_N order | kernel | distinct simplices | vertices | frame bound | projective angle values | coherence | non-antipodal coherence | abs profile preview |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | `[3]` | 2 | 1 | 2 | 6 | 3 | 1 | 1 | 1/2 | `1/2:12; 1:3` |
| 4 | `[2, 4]` | 4 | 2 | 2 | 8 | 8/3 | 1 | 1 | 1/3 | `1/3:24; 1:4` |
| 5 | `[5]` | 2 | 1 | 2 | 10 | 5/2 | 1 | 1 | 1/4 | `1/4:40; 1:5` |
| 6 | `[2, 3, 6]` | 8 | 2 | 4 | 24 | 24/5 | 2 | 1 | 3/5 | `1/5:192; 3/5:72; 1:12` |
| 7 | `[7]` | 2 | 1 | 2 | 14 | 7/3 | 1 | 1 | 1/6 | `1/6:84; 1:7` |
| 8 | `[2, 4, 8]` | 8 | 2 | 4 | 32 | 32/7 | 3 | 1 | 5/7 | `1/7:352; 3/7:96; 5/7:32; 1:16` |
| 9 | `[3, 9]` | 4 | 1 | 4 | 36 | 9/2 | 3 | 1 | 5/8 | `1/8:504; 1/2:36; 5/8:72; 1:18` |
| 10 | `[2, 5, 10]` | 8 | 2 | 4 | 40 | 40/9 | 3 | 1 | 7/9 | `1/9:560; 1/3:160; 7/9:40; 1:20` |
| 11 | `[11]` | 2 | 1 | 2 | 22 | 11/5 | 1 | 1 | 1/10 | `1/10:220; 1:11` |
| 12 | `[2, 3, 4, 6, 12]` | 32 | 2 | 16 | 192 | 192/11 | 5 | 1 | 9/11 | `1/11:9600; 3/11:4992; 5/11:2496; 7/11:960; 9/11:192; 1:96` |
| 13 | `[13]` | 2 | 1 | 2 | 26 | 13/6 | 1 | 1 | 1/12 | `1/12:312; 1:13` |
| 14 | `[2, 7, 14]` | 8 | 2 | 4 | 56 | 56/13 | 3 | 1 | 11/13 | `1/13:1120; 3/13:336; 11/13:56; 1:28` |
| 15 | `[3, 5, 15]` | 8 | 1 | 8 | 120 | 60/7 | 8 | 1 | 5/7 | `1/14:4320; 1/7:120; 3/14:1440; 5/14:480; 3/7:120; 1/2:240; 9/14:240; 5/7:120; ... (9 values)` |
| 16 | `[2, 4, 8, 16]` | 16 | 2 | 8 | 128 | 128/15 | 7 | 1 | 13/15 | `1/15:5504; 1/5:1408; 1/3:384; 7/15:384; 3/5:128; 11/15:128; 13/15:128; 1:64` |

## Consequences

1. For odd `N`, the block-sign action has no coordinate half-turn kernel in the tested range, so the number of distinct simplices is `2^(tau(N)-1)`.
2. For even `N`, the half-turn `C_N^(N/2)` is itself a block-sign element and fixes `V_N` as a set.  The number of distinct simplices is therefore `2^(tau(N)-2)`.
3. If `M_N` is the number of distinct simplex images, then the unit-normalized compound has `N M_N` vectors and frame bound `N M_N/(N-1)`.  The script verifies the exact frame operator identity for every tested `N`.
4. Because the all-block sign flip is `-I` on `H_N`, the full spectral compound always contains antipodal partners and has ordinary coherence `1`.  The non-antipodal/projective coherence is the meaningful packing statistic.
5. The full spectral compounds are still exact few-angle objects for small `N`, but the number of angle values grows.  This motivates a Ramanujan-sum formula rather than case-by-case tables.

## Projective Packing Baseline

The compound is centrally symmetric, so the packing comparison is made after identifying antipodal pairs.  The table below uses the number of projective lines `vertices/2`.  The bound column is the Welch bound except where the second real projective Levenshtein bound applies.

| N | dimension | vertices | projective lines | projective coherence | Welch bound | Levenshtein bound | excess over bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 4 | 10 | 5 | 1/4 | 1/4 | - | 0.000000 |
| 6 | 5 | 24 | 12 | 3/5 | sqrt(7/55) | - | 0.243247 |
| 7 | 6 | 14 | 7 | 1/6 | 1/6 | - | 0.000000 |
| 8 | 7 | 32 | 16 | 5/7 | sqrt(3/35) | - | 0.421516 |
| 9 | 8 | 36 | 18 | 5/8 | sqrt(5/68) | - | 0.353837 |
| 10 | 9 | 40 | 20 | 7/9 | sqrt(11/171) | - | 0.524149 |
| 12 | 11 | 192 | 96 | 9/11 | sqrt(17/209) | sqrt(29/221) | 0.455936 |
