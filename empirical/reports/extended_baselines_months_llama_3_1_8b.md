# Extended metric baselines — months, Llama-3.1-8B

**Centroid shape:** 12 x 12

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
| Moment Euclidean | linear-L2 | no | no | 0.6899 | **0.2101** | [-0.043, 0.415] | -0.480 | drops sharply |
| Total variation | linear-L1 | no | no | 0.8454 | **0.6429** | [0.555, 0.734] | -0.202 | drops sharply |
| Hellinger chord | quad-Fisher | yes | no | 0.7414 | **0.7087** | [0.608, 0.788] | -0.033 | drops mildly |
| Jensen-Shannon distance | quad-Fisher | yes | no | 0.7557 | **0.6659** | [0.574, 0.754] | -0.090 | drops mildly |
| Symmetric KL | quad-Fisher | yes | no | 0.9016 | **0.7520** | [0.645, 0.834] | -0.150 | drops mildly |
| Bhattacharyya | quad-Fisher | yes | no | 0.9729 | **0.7420** | [0.618, 0.832] | -0.231 | drops sharply |
| Fisher Levi-Civita | quad-Fisher | yes | no | 0.7477 | **0.7139** | [0.621, 0.797] | -0.034 | drops mildly |
| Natural/logit chord | quad-natural | no | no | 0.9601 | **0.8709** | [0.823, 0.911] | -0.089 | drops mildly |
| Wasserstein-1 cyclic | OT-cyclic | no | yes | 0.9993 | **0.9931** | [0.991, 0.995] | -0.006 | holds |

## Drop-pattern summary

- Moment Euclidean Δ = -0.4798 (drops sharply)
- Total variation Δ = -0.2025 (drops sharply)
- Max |Δ| across Fisher-equivalent metrics = 0.2309
- Hellinger chord Δ = -0.0327
- Wasserstein-1 cyclic Δ = -0.0063

**Reading (see Note_metric_baselines_design.md §3):**
- *Some Fisher-equivalent metric drops by ≥0.15.* Heterogeneous
  Fisher-equivalent metric behavior at the chord level is unusual;
  identify which metric drops and test whether the per-pair residual
  correlates with the K^CH(h_i) Frobenius norm.

## Centroid matrix

| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0.6675 | 0.0368 | 0.0624 | 0.0072 | 0.0051 | 0.0046 | 0.0262 | 0.0048 | 0.0078 | 0.0091 | 0.0194 | 0.1491 |
| 1 | 0.0271 | 0.9124 | 0.0168 | 0.0121 | 0.0022 | 0.0014 | 0.0036 | 0.0044 | 0.0033 | 0.0082 | 0.0027 | 0.0058 |
| 2 | 0.0074 | 0.0314 | 0.9190 | 0.0171 | 0.0092 | 0.0015 | 0.0018 | 0.0027 | 0.0033 | 0.0022 | 0.0023 | 0.0023 |
| 3 | 0.0047 | 0.0204 | 0.1127 | 0.7662 | 0.0482 | 0.0249 | 0.0046 | 0.0026 | 0.0047 | 0.0060 | 0.0019 | 0.0032 |
| 4 | 0.0026 | 0.0036 | 0.0307 | 0.0269 | 0.8624 | 0.0271 | 0.0378 | 0.0025 | 0.0017 | 0.0015 | 0.0019 | 0.0014 |
| 5 | 0.0014 | 0.0028 | 0.0045 | 0.0086 | 0.0242 | 0.9081 | 0.0173 | 0.0270 | 0.0018 | 0.0014 | 0.0009 | 0.0020 |
| 6 | 0.0020 | 0.0018 | 0.0035 | 0.0049 | 0.0107 | 0.0192 | 0.9159 | 0.0148 | 0.0221 | 0.0018 | 0.0014 | 0.0022 |
| 7 | 0.0017 | 0.0027 | 0.0019 | 0.0028 | 0.0055 | 0.0074 | 0.0167 | 0.9438 | 0.0098 | 0.0047 | 0.0013 | 0.0017 |
| 8 | 0.0010 | 0.0018 | 0.0032 | 0.0015 | 0.0042 | 0.0043 | 0.0051 | 0.0194 | 0.9457 | 0.0080 | 0.0039 | 0.0020 |
| 9 | 0.0019 | 0.0019 | 0.0025 | 0.0014 | 0.0032 | 0.0057 | 0.0067 | 0.0106 | 0.0259 | 0.9230 | 0.0089 | 0.0081 |
| 10 | 0.0037 | 0.0016 | 0.0020 | 0.0020 | 0.0024 | 0.0050 | 0.0048 | 0.0036 | 0.0044 | 0.0107 | 0.9514 | 0.0084 |
| 11 | 0.0083 | 0.0086 | 0.0020 | 0.0022 | 0.0018 | 0.0037 | 0.0027 | 0.0022 | 0.0031 | 0.0067 | 0.0475 | 0.9112 |

## K^CH Frobenius norms per row

- row 0: 127.3399
- row 1: 176.4116
- row 2: 177.8389
- row 3: 146.8466
- row 4: 165.9821
- row 5: 175.5404
- row 6: 177.1487
- row 7: 183.0476
- row 8: 183.4545
- row 9: 178.6652
- row 10: 184.6506
- row 11: 176.3000
