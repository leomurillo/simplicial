# Weekday $C_7$ $K^{CH}$ Diagnostic — Llama-3.1-8B

**Model:** Llama-3.1-8B (layer 28, last token)
**Source:** `C:/Projects/simplicial/weekdays/baseline/per_class_output_dists.safetensors`
**Shape:** [7, 7]  (row i = output distribution for input weekday i)

## Centroid Matrix

| Input \ Output | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Monday | 0.6356 | 0.0558 | 0.0089 | 0.0089 | 0.0064 | 0.0136 | 0.2709 |
| Tuesday | 0.1155 | 0.7487 | 0.0734 | 0.0151 | 0.0086 | 0.0152 | 0.0234 |
| Wednesday | 0.0178 | 0.1100 | 0.7374 | 0.0624 | 0.0264 | 0.0199 | 0.0261 |
| Thursday | 0.0154 | 0.0121 | 0.0685 | 0.7732 | 0.0965 | 0.0146 | 0.0196 |
| Friday | 0.0079 | 0.0093 | 0.0050 | 0.0704 | 0.8328 | 0.0499 | 0.0247 |
| Saturday | 0.0103 | 0.0052 | 0.0051 | 0.0044 | 0.1440 | 0.7477 | 0.0833 |
| Sunday | 0.0283 | 0.0088 | 0.0034 | 0.0079 | 0.0043 | 0.0506 | 0.8967 |

## Correlation with Cyclic Hellinger Arc

Parametric proxy values (Paper 12 §4) shown for comparison.

| Metric | Real (Llama-3.1-8B) | Parametric proxy |
|---|---|---|
| Hellinger chord vs cyclic arc | **0.899815** | 0.910010 |
| Moment Euclidean chord vs cyclic arc | **0.614547** | 0.886448 |
| Natural/logit chord vs cyclic arc | **0.944337** | 0.941295 |
| Fisher L-C distance vs cyclic arc | **0.903176** | 0.911776 |

> The moment Euclidean chord value should be compared with the
> Wurgaft et al. reported linear correlation r ≈ 0.89.
> The behavior-manifold reference is r ≈ 0.99.

## $K^{CH}$ Frobenius Norms per Centroid

| Weekday | $\|K^{CH}_{p_*}(h_i)\|_F$ |
|---|---|
| Monday | 40.2866 |
| Tuesday | 45.8379 |
| Wednesday | 44.8546 |
| Thursday | 47.5071 |
| Friday | 51.8104 |
| Saturday | 46.1796 |
| Sunday | 56.5011 |

## Interpretation

The moment chord correlation closes the open empirical item in Paper 12 §10:
the parametric proxy is replaced by an actual transformer measurement.
The residual between the moment chord correlation and the cyclic arc
correlation (r ≈ 0.99 reference) is attributed to:

1. Intrinsic behavior-side $K^{CH}$ cubic (quantified above)
2. Activation pullback distortion $J_F^\top g_y J_F$
3. Hessian terms of $F$
4. Sampling / spline parameterization error