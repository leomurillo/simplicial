# Activation Pullback Audit -- Llama-3.1-8B, `months`

**Model:** Llama-3.1-8B (layer 28, last token)
**Samples:** 84 prompts grouped into 12 result classes
**Hidden dim:** 4096
**Source:** `C:/Projects/simplicial/months/subspace/pca_k64/result/features/raw_features.safetensors`

## Variance Decomposition in Activation Space

Partition the total \(L^2\) variance of the saved activations across
the result-class label.  Between-class variance is the part captured
by the centroid representation \(A_c\); within-class variance is the
irreducible noise visible to the K^CH centroid analysis.

| component | fraction of total |
|---|---|
| between-class | **0.5862** |
| within-class  | 0.4138 |

## Pairwise Activation vs. Behavior Distances

There are \(66\) inter-class pairs.  For each pair we compute
the ambient activation-space distance and the output-space
Hellinger distance.

| comparison | Pearson \(r\) |
|---|---|
| activation distance vs Hellinger chord | **0.821285** |
| activation distance vs cyclic Hellinger arc | **0.651696** |

## Effective Pullback Lipschitz

Linear regression of behavior distance on activation distance gives
the effective Lipschitz constant \(L_F\) for the activation->output
map at this scale.

| regression | slope |
|---|---|
| Hellinger chord ~ \(L_F\) · activation distance | 2.537689e-02 |
| cyclic arc ~ \(L\) · activation distance | 4.454577e-01 |

## Local Pullback Metric Variation

Per-pair pullback metric \(G_F^{ij} = (d_H(p_i,p_j) / \|A_i - A_j\|)^2\)
summarises how the Fisher-Hellinger metric pulls back to activation
space at the class-centroid scale.

| statistic | value |
|---|---|
| mean | 4.5371e-03 |
| std  | 1.0574e-03 |
| coefficient of variation | **0.2331** |

A coefficient of variation near zero indicates that the map \(F\)
behaves as a (rescaled) local isometry on this centroid set: the
*activation-pullback distortion residual* of Paper 12 §7.2 is small,
and the linear-vs-manifold gap measured in §4–§5 is attributable
primarily to the intrinsic behavior-side cubic.
A large coefficient of variation means the activation embedding
stretches and compresses pairs at different rates -- the activation
pullback carries part of the gap and the K^CH cubic carries the rest.