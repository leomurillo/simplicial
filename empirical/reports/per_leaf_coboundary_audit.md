# Per-Leaf Full-Block Coboundary Audit

## Status

- JSON artifact: `C:\Projects\simplicial\empirical\reports\per_leaf_coboundary_audit.json`
- C2 scope: full block restricted to source/middle/target inside the conductor leaf
- C1 generators: full-block section changes with source/target inside the conductor leaf
- normalized residual columns use the support-atlas active orbit count and active atom mass when available, falling back to raw support for atom mass
- `nu_lambda^E` uses coefficient L1 mass over Q, or nonzero support mass over a finite field, divided by the leaf full-block C2 dimension
- C2 orbit quotient columns use normalizer orbits on the leaf full-block C2 coordinates
- H4->H3 cokernel is a support-level orbit cokernel, not the full current quotient `H_hyp`

This is the first filtered residual audit on the minimizing local leaves. Skipped rows need a larger dimension limit or a modular run.

| ring | leaf | field | C2 dim | C1 gens | raw support | residual support | residual deficit | res/atom | nu_E residual | C2 orbit vol | residual orbit support | orbit residual mass | H3 orbits | H4 orbits | H4->H3 cokernel | residual dim | status | seconds |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| F_4[u]/(u^2) | `u^2` | Q | 36864 | 2304 | 576 | 576 | 1.000000 | 1.000000 | 0.015625 | 1552 | 26 | 0.016753 | 2 | 9 | 0 | 34560 | residual | 4.341000 |
| F_2[u]/(u^2) | `u+u^2` | Q | 61 | 17 | 4 | 4 | 1.000000 | 1.000000 | 0.065574 | 31 | 2 | 0.064516 | 1 | 4 | 0 | 45 | residual | 0.006000 |
| F_2[u]/(u^3) | `u^2+u^3` | Q | 976 | 136 | 32 | 32 | 1.000000 | 1.000000 | 0.032787 | 136 | 6 | 0.044118 | 1 | 8 | 0 | 844 | residual | 0.095000 |
| F_2[u]/(u^4) | `u^3+u^4` | Q | 15616 | 1088 | 256 | 256 | 1.000000 | 1.000000 | 0.016393 | 612 | 20 | 0.032680 | 1 | 16 | 0 | 14544 | residual | 1.915000 |
| F_2[u]/(u^5) | `u^4+u^5` | Q | 249856 | 8704 | 2048 | 2048 | 1.000000 | 1.000000 | 0.008197 | 2544 | 48 | 0.018868 | 1 | 28 | 0 | 241216 | residual | 75.119000 |
| F_8[u]/(u^2) | `u^2` | n/a | 12845056 | 200704 | 25088 | n/a | n/a | n/a | n/a | 76480 | n/a | n/a | 4 | 53 | 0 | n/a | skipped | 74.437000 |
