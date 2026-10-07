# Weekday $C_7$ $K^{CH}$ Diagnostic — Real Transformer Measurement

**Model:** Mistral-7B-v0.3 (layer 28, last token)
**Source:** `per_class_output_dists.safetensors` from causalab `weekdays_mistral_pipeline`
**Shape:** [7, 7]  (row i = output distribution for input weekday i)

## Centroid Matrix

| Input \ Output | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Monday | 0.6649 | 0.0428 | 0.0062 | 0.0050 | 0.0084 | 0.0188 | 0.2538 |
| Tuesday | 0.1536 | 0.7742 | 0.0250 | 0.0095 | 0.0058 | 0.0092 | 0.0226 |
| Wednesday | 0.0142 | 0.2425 | 0.6915 | 0.0308 | 0.0066 | 0.0037 | 0.0106 |
| Thursday | 0.0017 | 0.0057 | 0.0824 | 0.8690 | 0.0311 | 0.0036 | 0.0066 |
| Friday | 0.0017 | 0.0011 | 0.0040 | 0.1909 | 0.7818 | 0.0140 | 0.0064 |
| Saturday | 0.0053 | 0.0026 | 0.0014 | 0.0075 | 0.2738 | 0.6870 | 0.0224 |
| Sunday | 0.0474 | 0.0062 | 0.0030 | 0.0052 | 0.0204 | 0.2841 | 0.6338 |

## Correlation with Cyclic Hellinger Arc

Parametric proxy values (Paper 12 §4) shown for comparison.

| Metric | Real (Mistral-7B) | Parametric proxy |
|---|---|---|
| Hellinger chord vs cyclic arc | **0.916873** | 0.910010 |
| Moment Euclidean chord vs cyclic arc | **0.714715** | 0.886448 |
| Natural/logit chord vs cyclic arc | **0.955300** | 0.941295 |
| Fisher L-C distance vs cyclic arc | **0.922202** | 0.911776 |

> The moment Euclidean chord value should be compared with the
> Wurgaft et al. reported linear correlation r ≈ 0.89.
> The behavior-manifold reference is r ≈ 0.99.

## $K^{CH}$ Frobenius Norms per Centroid

| Weekday | $\|K^{CH}_{p_*}(h_i)\|_F$ |
|---|---|
| Monday | 41.9230 |
| Tuesday | 48.0863 |
| Wednesday | 43.5752 |
| Thursday | 54.5717 |
| Friday | 49.2491 |
| Saturday | 44.0816 |
| Sunday | 40.5386 |

## Interpretation

The moment chord correlation closes the open empirical item in Paper 12 §10:
the parametric proxy is replaced by an actual transformer measurement.
The residual between the moment chord correlation and the cyclic arc
correlation (r ≈ 0.99 reference) is attributed to:

1. Intrinsic behavior-side $K^{CH}$ cubic (quantified above)
2. Activation pullback distortion $J_F^\top g_y J_F$
3. Hessian terms of $F$
4. Sampling / spline parameterization error