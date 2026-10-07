# Finite Row Proof-Extraction Certificates

These certificates compress the heavy finite-row reports into the
counts and hashes needed for theorem-facing proof extraction.

## Rows

| row | ring | packets | H3 cells/orbits | H4 cells/orbits | raw atoms | raw pairs | full residual | support residual |
|---|---|---|---:|---:|---:|---:|---:|---:|
| f4-u2 | F_4[u]/(u^2) | u:3, u^2:12 | 210/5 | 3165/18 | 1569 | 369 | 1569 | n/a |
| f2-u5 | F_2[u]/(u^5) | u:1, u^2:2, u^3:4, u^4:8, u^5:16 | 930/12 | 28861/72 | 19140 | 2516 | 19140 | 0 |
| f8-u2 | F_8[u]/(u^2) | u:7, u^2:56 | 3906/8 | 246141/86 | 158081 | 7105 | 158081 | 0 |

## Source Hashes

### f4-u2

- `empirical\reports\local_adjacency_constructor_f4_u2.json`
  - sha256: `a8df9feb2ed2eeb4cfa5566732c04ddbbe7f3b017655bd48e4ceff0bb2f7c4e3`
  - bytes: `72140`
- `empirical\reports\ext_ch_cocycle_f4_u2.json`
  - sha256: `bfaae575f1be6626309cfc02b39ae0bd39c14760511ec5f94ee653e4d59087e2`
  - bytes: `33507`

### f2-u5

- `empirical\reports\next_local_row_f2_u5.json`
  - sha256: `0e43c00f4aba542302979dc1c9f03ff7761929644db64aa3f04dee52c0a3ae03`
  - bytes: `46240`

### f8-u2

- `empirical\reports\next_local_row_f8_u2.json`
  - sha256: `3174d98891395c5b6bb2aa62fbe05859b42bbe6bf76befd8af96feb6ea555607`
  - bytes: `35670`

## Reading

The full residual column is the filtered-adjacency obstruction.  The
support residual column is deliberately separate: rows with support
residual `0` and full residual nonzero are the finite counterexamples
to support-level closure implying filtered closure.
