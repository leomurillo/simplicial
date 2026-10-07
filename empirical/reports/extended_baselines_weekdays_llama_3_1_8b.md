# Extended metric baselines — weekdays, Llama-3.1-8B

**Centroid shape:** 7 x 7

Each metric is computed pairwise across the N centroids; the
Pearson correlation is taken against the cyclic Hellinger arc
reference (the canonical behavior-manifold-aware geodesic).

The 'proxy' column uses the symmetric cyclic-confidence
centroid family of Paper 12 §4 at beta=2.5; it is the parametric
calibration reference, not an empirical measurement.

Δ = real − proxy. Classification:
- |Δ| < 0.03: **holds**
- 0.03 ≤ |Δ| < 0.15: **drops mildly**
- |Δ| ≥ 0.15: **drops sharply**

| Metric | Category | Fisher-equiv | Cyclic-aware | Proxy r | Real r | 95% CI | Δ | Class |
|---|---|---|---|---:|---:|---|---:|---|
| Moment Euclidean | linear-L2 | no | no | 0.8831 | **0.6145** | [0.333, 0.824] | -0.269 | drops sharply |
| Total variation | linear-L1 | no | no | 1.0000 | **0.8937** | [0.822, 0.967] | -0.106 | drops mildly |
| Hellinger chord | quad-Fisher | yes | no | 0.9233 | **0.8998** | [0.831, 0.949] | -0.023 | holds |
| Jensen-Shannon distance | quad-Fisher | yes | no | 0.9379 | **0.8954** | [0.826, 0.948] | -0.042 | drops mildly |
| Symmetric KL | quad-Fisher | yes | no | 0.9997 | **0.9006** | [0.817, 0.956] | -0.099 | drops mildly |
| Bhattacharyya | quad-Fisher | yes | no | 0.9873 | **0.9251** | [0.854, 0.972] | -0.062 | drops mildly |
| Fisher Levi-Civita | quad-Fisher | yes | no | 0.9283 | **0.9032** | [0.829, 0.954] | -0.025 | holds |
| Natural/logit chord | quad-natural | no | no | 0.9819 | **0.9443** | [0.896, 0.977] | -0.038 | drops mildly |
| Wasserstein-1 cyclic | OT-cyclic | no | yes | 0.9997 | **0.9921** | [0.985, 0.997] | -0.008 | holds |

## Drop-pattern summary

- Moment Euclidean Δ = -0.2685 (drops sharply)
- Total variation Δ = -0.1063 (drops mildly)
- Max |Δ| across Fisher-equivalent metrics = 0.0991
- Hellinger chord Δ = -0.0235
- Wasserstein-1 cyclic Δ = -0.0076

**Reading (see Note_metric_baselines_design.md §3):**
- *Mixed or mild pattern.* Inspect the table; report row-by-row.

## Centroid matrix

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | 0.6356 | 0.0558 | 0.0089 | 0.0089 | 0.0064 | 0.0136 | 0.2709 |
| 1 | 0.1155 | 0.7487 | 0.0734 | 0.0151 | 0.0086 | 0.0152 | 0.0234 |
| 2 | 0.0178 | 0.1100 | 0.7374 | 0.0624 | 0.0264 | 0.0199 | 0.0261 |
| 3 | 0.0154 | 0.0121 | 0.0685 | 0.7732 | 0.0965 | 0.0146 | 0.0196 |
| 4 | 0.0079 | 0.0093 | 0.0050 | 0.0704 | 0.8328 | 0.0499 | 0.0247 |
| 5 | 0.0103 | 0.0052 | 0.0051 | 0.0044 | 0.1440 | 0.7477 | 0.0833 |
| 6 | 0.0283 | 0.0088 | 0.0034 | 0.0079 | 0.0043 | 0.0506 | 0.8967 |

## K^CH Frobenius norms per row

- row 0: 40.2866
- row 1: 45.8379
- row 2: 44.8546
- row 3: 47.5071
- row 4: 51.8104
- row 5: 46.1796
- row 6: 56.5011
