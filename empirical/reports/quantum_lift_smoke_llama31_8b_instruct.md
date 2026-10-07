# Quantum-Lift Audit: Z/6Z Modular Addition

## Status

- model: `meta-llama/Llama-3.1-8B-Instruct`
- prompts: 36
- layers: 31
- baseline six-bin accuracy: 0.3056
- mode: final residual readout/lift audit

This report tests an operational version of the Paper 15 lift.  The
diagonal of the empirical density matrix is the six-answer softmax
distribution; the off-diagonal entries come from residual covariance
projected onto the six answer-readout directions, with the largest
PSD-safe coherence scale allowed by the requested gamma.

## Family Summary

| layer | family | mean squash ratio | median | density diag/pre ratio |
|---:|---|---:|---:|---:|
| 31 | cartan | 0.114384 | 0.114384 | 0.189499 |
| 31 | nonabelian_su2 | 0.0717837 | 0.0717837 | 0.111056 |
| 31 | nonabelian_su3 | 0.0718122 | 0.07789 | 0.165994 |

Interpretation: lower squash ratio means more hidden-space motion is lost
after LayerNorm + unembedding + Softmax.  The decisive comparison is
`nonabelian_*` versus `cartan` at matched theta on the same layer.

## Density Coherence

| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |
|---:|---:|---:|---:|---:|
| 31 | 0.35 | 0.204812 | 9.475e-02 | 0.179962 |

## Generator Details

| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| 31 | cartan | cartan_fourier_k1 | 0.05 | 0.0986939 | 0.0121811 | 0.121625 | [0.0976333, 0.146756] | 0.00518033 | 0.00119094 |
| 31 | cartan | cartan_fourier_k2 | 0.05 | 0.102557 | 0.0106427 | 0.107143 | [0.0745611, 0.141493] | 0.00502693 | 0.000749522 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.378028 | 0.023145 | 0.0717837 | [0.0572, 0.0884363] | 0.0134798 | 0.00149702 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.268712 | 0.0202655 | 0.0855412 | [0.0617941, 0.114998] | 0.0109095 | 0.00117028 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.281994 | 0.0129109 | 0.0520053 | [0.0368112, 0.0719454] | 0.0074483 | 0.00184543 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.28968 | 0.0187172 | 0.07789 | [0.0581609, 0.101349] | 0.010839 | 0.0015494 |

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