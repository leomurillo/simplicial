# Quantum-Lift Audit: Z/6Z Modular Addition

## Status

- model: `meta-llama/Llama-3.1-8B`
- prompts: 36
- layers: 31
- baseline six-bin accuracy: 0.1667
- mode: final residual readout/lift audit

This report tests an operational version of the Paper 15 lift.  The
diagonal of the empirical density matrix is the six-answer softmax
distribution; the off-diagonal entries come from residual covariance
projected onto the six answer-readout directions, with the largest
PSD-safe coherence scale allowed by the requested gamma.

## Family Summary

| layer | family | mean squash ratio | median | density diag/pre ratio |
|---:|---|---:|---:|---:|
| 31 | cartan | 0.0559993 | 0.0559993 | 0.0652199 |
| 31 | nonabelian_su2 | 0.112121 | 0.112121 | 0.0915807 |
| 31 | nonabelian_su3 | 0.128903 | 0.125576 | 0.0525152 |

Interpretation: lower squash ratio means more hidden-space motion is lost
after LayerNorm + unembedding + Softmax.  The decisive comparison is
`nonabelian_*` versus `cartan` at matched theta on the same layer.

## Density Coherence

| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |
|---:|---:|---:|---:|---:|
| 31 | 0.35 | 0.127279 | 5.045e-02 | 0.264729 |

## Generator Details

| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| 31 | cartan | cartan_fourier_k1 | 0.05 | 0.0196946 | 0.0018721 | 0.0854021 | [0.0335261, 0.148385] | 0.0144452 | 0.00095802 |
| 31 | cartan | cartan_fourier_k2 | 0.05 | 0.0166852 | 0.00048179 | 0.0265965 | [0.00437492, 0.0584677] | 0.0146259 | 0.000937796 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.0640208 | 0.00639231 | 0.112121 | [0.085829, 0.137015] | 0.0308521 | 0.00282546 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.0462655 | 0.00584198 | 0.11936 | [0.0862959, 0.157385] | 0.0305426 | 0.00176338 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.0476246 | 0.00625075 | 0.141773 | [0.0986116, 0.191198] | 0.0192268 | 0.00156494 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.0428937 | 0.0051261 | 0.125576 | [0.0875907, 0.165962] | 0.0209375 | 0.000385607 |

## Pre-Registered Success Read

- Cartan conservation: Cartan rows should have a stable, nonzero
  post/pre slope across theta.
- Nonabelian squash: nonabelian mean squash ratio below the Cartan mean
  at matched theta and layer, ideally below 0.5x with bootstrap intervals
  separated from the Cartan family.
- Density coherence: offdiag/diag Frobenius should be materially above
  random-label or shuffled-residual controls in a follow-up run.

Boundary: this audit can support or fail to support the transformer
analogy.  It does not by itself prove an actual SU(2) x SU(3) gauge
action inside the model.