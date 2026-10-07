# Tree Spectral Boundary Probe

- timestamp: `2026-05-28T04:29:50.013708+00:00`
- seed: `260523821`
- alpha: `0.05`
- closure cost: `0.02`

## Claim Tested

A Nava-Wyart style tree co-occurrence kernel induces Haar hierarchy packets. After retaining only coarse packets, scalar surprise should not tell structural omitted packets from matched noise, while held-out T17 boundary gain should identify and admit the missing fine split.

## Setup

- binary leaf tree: depth `6`, leaves `64`
- kernel: `K_ij = exp(-0.65 * tree_distance(i,j))`
- retained hierarchy levels: `< 2` (3 retained split packets)
- candidate dictionary: omitted Haar split packets from the remaining levels
- structural episodes use one omitted packet as the target; noise episodes have matched retained-sector variance

## Results

| target level | support leaves | evidence | scalar AUC | raw corr AUC | T17 gain AUC | raw kernel true | raw corr true | T17 true | conformal TPR | conformal FPR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 16 | 32 | 0.469 | 0.869 | 0.989 | 0.259 | 0.761 | 0.974 | 0.978 | 0.041 |
| 2 | 16 | 64 | 0.483 | 0.989 | 1.000 | 0.244 | 0.984 | 1.000 | 1.000 | 0.046 |
| 2 | 16 | 128 | 0.486 | 1.000 | 1.000 | 0.255 | 1.000 | 1.000 | 1.000 | 0.042 |
| 2 | 16 | 256 | 0.494 | 1.000 | 1.000 | 0.240 | 1.000 | 1.000 | 1.000 | 0.030 |
| 3 | 8 | 32 | 0.472 | 0.794 | 0.983 | 0.000 | 0.586 | 0.979 | 0.979 | 0.048 |
| 3 | 8 | 64 | 0.478 | 0.972 | 1.000 | 0.000 | 0.930 | 1.000 | 1.000 | 0.082 |
| 3 | 8 | 128 | 0.485 | 1.000 | 1.000 | 0.000 | 0.999 | 1.000 | 1.000 | 0.050 |
| 3 | 8 | 256 | 0.498 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 0.056 |
| 4 | 4 | 32 | 0.445 | 0.782 | 0.898 | 0.000 | 0.457 | 0.875 | 0.877 | 0.044 |
| 4 | 4 | 64 | 0.476 | 0.926 | 0.982 | 0.000 | 0.820 | 0.978 | 0.978 | 0.037 |
| 4 | 4 | 128 | 0.478 | 0.991 | 1.000 | 0.000 | 0.973 | 1.000 | 1.000 | 0.038 |
| 4 | 4 | 256 | 0.477 | 1.000 | 1.000 | 0.000 | 0.999 | 1.000 | 1.000 | 0.054 |

## Mean Scores

| target level | evidence | structural scalar | noise scalar | structural gain | noise gain | null gain threshold |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 32 | 1.286 | 1.272 | 1.090 | 0.041 | 0.112 |
| 2 | 64 | 1.201 | 1.196 | 1.067 | 0.024 | 0.048 |
| 2 | 128 | 1.149 | 1.156 | 1.022 | 0.019 | 0.036 |
| 2 | 256 | 1.136 | 1.140 | 1.011 | 0.015 | 0.029 |
| 3 | 32 | 1.283 | 1.271 | 1.110 | 0.041 | 0.114 |
| 3 | 64 | 1.195 | 1.195 | 1.062 | 0.024 | 0.045 |
| 3 | 128 | 1.159 | 1.160 | 1.031 | 0.018 | 0.034 |
| 3 | 256 | 1.146 | 1.144 | 1.021 | 0.016 | 0.028 |
| 4 | 32 | 1.268 | 1.285 | 1.002 | 0.040 | 0.107 |
| 4 | 64 | 1.196 | 1.199 | 1.041 | 0.023 | 0.050 |
| 4 | 128 | 1.161 | 1.158 | 1.033 | 0.018 | 0.036 |
| 4 | 256 | 1.141 | 1.143 | 1.016 | 0.016 | 0.028 |

## Interpretation

This is a pass when scalar AUC stays near 0.5, raw kernel priority does not identify the episode-specific omitted packet, and held-out T17 gain approaches high AUC with conformal false admission near alpha.

The result is exactly the T16/T17 reading of the arXiv paper: hierarchical geometry can emerge from co-occurrence spectra, but useful updating requires packet-resolved held-out closure gain rather than raw surprise or global spectral priority.
