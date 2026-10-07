# Months $C_{12}$ $K^{CH}$ Diagnostic — Llama-3.1-8B

**Model:** Llama-3.1-8B (layer 28, last token)
**Source:** `C:/Projects/simplicial/months/baseline/per_class_output_dists.safetensors`
**Shape:** [12, 12]
**Output algebra:** $C_{12} \cong C_4 \times C_3$ (CRT)

## Centroid Matrix

| Input \ Output | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Jan | 0.667 | 0.037 | 0.062 | 0.007 | 0.005 | 0.005 | 0.026 | 0.005 | 0.008 | 0.009 | 0.019 | 0.149 |
| Feb | 0.027 | 0.912 | 0.017 | 0.012 | 0.002 | 0.001 | 0.004 | 0.004 | 0.003 | 0.008 | 0.003 | 0.006 |
| Mar | 0.007 | 0.031 | 0.919 | 0.017 | 0.009 | 0.002 | 0.002 | 0.003 | 0.003 | 0.002 | 0.002 | 0.002 |
| Apr | 0.005 | 0.020 | 0.113 | 0.766 | 0.048 | 0.025 | 0.005 | 0.003 | 0.005 | 0.006 | 0.002 | 0.003 |
| May | 0.003 | 0.004 | 0.031 | 0.027 | 0.862 | 0.027 | 0.038 | 0.002 | 0.002 | 0.002 | 0.002 | 0.001 |
| Jun | 0.001 | 0.003 | 0.004 | 0.009 | 0.024 | 0.908 | 0.017 | 0.027 | 0.002 | 0.001 | 0.001 | 0.002 |
| Jul | 0.002 | 0.002 | 0.003 | 0.005 | 0.011 | 0.019 | 0.916 | 0.015 | 0.022 | 0.002 | 0.001 | 0.002 |
| Aug | 0.002 | 0.003 | 0.002 | 0.003 | 0.006 | 0.007 | 0.017 | 0.944 | 0.010 | 0.005 | 0.001 | 0.002 |
| Sep | 0.001 | 0.002 | 0.003 | 0.002 | 0.004 | 0.004 | 0.005 | 0.019 | 0.946 | 0.008 | 0.004 | 0.002 |
| Oct | 0.002 | 0.002 | 0.003 | 0.001 | 0.003 | 0.006 | 0.007 | 0.011 | 0.026 | 0.923 | 0.009 | 0.008 |
| Nov | 0.004 | 0.002 | 0.002 | 0.002 | 0.002 | 0.005 | 0.005 | 0.004 | 0.004 | 0.011 | 0.951 | 0.008 |
| Dec | 0.008 | 0.009 | 0.002 | 0.002 | 0.002 | 0.004 | 0.003 | 0.002 | 0.003 | 0.007 | 0.048 | 0.911 |

## Correlations with Cyclic Hellinger Arc

| Metric | Real (Llama-3.1-8B) | Symmetric proxy |
|---|---|---|
| Hellinger chord vs cyclic arc | **0.708696** | (n/a) |
| Moment Euclidean chord vs cyclic arc | **0.210147** | 0.696128 |
| Natural/logit chord vs cyclic arc | **0.870898** | (n/a) |
| Fisher Levi-Civita distance vs cyclic arc | **0.713899** | (n/a) |

## $K^{CH}$ Frobenius Norms per Centroid

| Month | $\|K^{CH}_{p_*}(h_i)\|_F$ |
|---|---|
| Jan | 127.3399 |
| Feb | 176.4116 |
| Mar | 177.8389 |
| Apr | 146.8466 |
| May | 165.9821 |
| Jun | 175.5404 |
| Jul | 177.1487 |
| Aug | 183.0476 |
| Sep | 183.4545 |
| Oct | 178.6652 |
| Nov | 184.6506 |
| Dec | 176.3000 |

## CRT Conductor Energy Decomposition

Each empirical displacement $h_i = p_i - p_*$ is decomposed into
conductor packets of $C_{12}$ via the unitary DFT.  Conductor 12 is
the highest-frequency (single-element-resolution) packet; conductor 2
is the global up/down split.

| Month | cond 2 | cond 3 | cond 4 | cond 6 | cond 12 |
|---|---|---|---|---|---|
| Jan | 0.071 | 0.144 | 0.145 | 0.227 | 0.413 |
| Feb | 0.088 | 0.173 | 0.180 | 0.189 | 0.370 |
| Mar | 0.086 | 0.173 | 0.178 | 0.191 | 0.372 |
| Apr | 0.067 | 0.146 | 0.168 | 0.217 | 0.402 |
| May | 0.096 | 0.163 | 0.159 | 0.181 | 0.401 |
| Jun | 0.091 | 0.172 | 0.172 | 0.184 | 0.382 |
| Jul | 0.091 | 0.173 | 0.173 | 0.183 | 0.380 |
| Aug | 0.088 | 0.178 | 0.180 | 0.185 | 0.369 |
| Sep | 0.088 | 0.179 | 0.181 | 0.186 | 0.367 |
| Oct | 0.088 | 0.175 | 0.180 | 0.184 | 0.373 |
| Nov | 0.089 | 0.179 | 0.182 | 0.185 | 0.366 |
| Dec | 0.084 | 0.172 | 0.179 | 0.193 | 0.372 |

**Aggregate per-conductor energy fractions** (averaged over the 12 inputs):

| conductor | aggregate fraction |
|---|---|
| 2 | 0.0856 |
| 3 | 0.1689 |
| 4 | 0.1730 |
| 6 | 0.1921 |
| 12 | 0.3804 |

## Interpretation

Unlike $C_7$, the $C_{12}$ tangent space has **multiple conductors**
(2, 3, 4, 6, 12).  The aggregate energy fractions above tell us how
the empirical $h_i$ distribute across them.  A pure dihedral
(rotation-symmetric) signal would put all weight into conductor 12.
Deviations indicate CRT-arithmetic structure that the symmetric proxy
cannot capture: conductor-2 weight = global ordering, conductor-3
weight = quarterly structure (3-month seasons), conductor-4 weight =
trimester structure, etc.

This is the first transformer measurement of the CRT conductor
ladder predicted by Paper 12 §5 for the months task.