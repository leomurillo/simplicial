# Extended metric baselines — weekdays, Mistral-7B-v0.3

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
| Moment Euclidean | linear-L2 | no | no | 0.8831 | **0.7147** | [0.485, 0.865] | -0.168 | drops sharply |
| Total variation | linear-L1 | no | no | 1.0000 | **0.8634** | [0.783, 0.928] | -0.137 | drops mildly |
| Hellinger chord | quad-Fisher | yes | no | 0.9233 | **0.9169** | [0.869, 0.957] | -0.006 | holds |
| Jensen-Shannon distance | quad-Fisher | yes | no | 0.9379 | **0.8976** | [0.834, 0.947] | -0.040 | drops mildly |
| Symmetric KL | quad-Fisher | yes | no | 0.9997 | **0.9433** | [0.903, 0.974] | -0.056 | drops mildly |
| Bhattacharyya | quad-Fisher | yes | no | 0.9873 | **0.9608** | [0.927, 0.985] | -0.027 | holds |
| Fisher Levi-Civita | quad-Fisher | yes | no | 0.9283 | **0.9222** | [0.874, 0.960] | -0.006 | holds |
| Natural/logit chord | quad-natural | no | no | 0.9819 | **0.9553** | [0.920, 0.982] | -0.027 | holds |
| Wasserstein-1 cyclic | OT-cyclic | no | yes | 0.9997 | **0.9861** | [0.975, 0.994] | -0.014 | holds |

## Drop-pattern summary

- Moment Euclidean Δ = -0.1684 (drops sharply)
- Total variation Δ = -0.1366 (drops mildly)
- Max |Δ| across Fisher-equivalent metrics = 0.0564
- Hellinger chord Δ = -0.0064
- Wasserstein-1 cyclic Δ = -0.0136

**Reading (see Note_metric_baselines_design.md §3):**
- *Mixed or mild pattern.* Inspect the table; report row-by-row.

## Centroid matrix

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 | 0.6649 | 0.0428 | 0.0062 | 0.0050 | 0.0084 | 0.0188 | 0.2538 |
| 1 | 0.1536 | 0.7742 | 0.0250 | 0.0095 | 0.0058 | 0.0092 | 0.0226 |
| 2 | 0.0142 | 0.2425 | 0.6915 | 0.0308 | 0.0066 | 0.0037 | 0.0106 |
| 3 | 0.0017 | 0.0057 | 0.0824 | 0.8690 | 0.0311 | 0.0036 | 0.0066 |
| 4 | 0.0017 | 0.0011 | 0.0040 | 0.1909 | 0.7818 | 0.0140 | 0.0064 |
| 5 | 0.0053 | 0.0026 | 0.0014 | 0.0075 | 0.2738 | 0.6870 | 0.0224 |
| 6 | 0.0474 | 0.0062 | 0.0030 | 0.0052 | 0.0204 | 0.2841 | 0.6338 |

## K^CH Frobenius norms per row

- row 0: 41.9230
- row 1: 48.0863
- row 2: 43.5752
- row 3: 54.5717
- row 4: 49.2491
- row 5: 44.0816
- row 6: 40.5386
