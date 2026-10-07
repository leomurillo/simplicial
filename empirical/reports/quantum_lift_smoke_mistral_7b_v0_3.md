# Quantum-Lift Audit: Z/6Z Modular Addition

## Status

- model: `mistralai/Mistral-7B-v0.3`
- prompts: 36
- layers: 31
- baseline six-bin accuracy: 0.3333
- mode: final residual readout/lift audit

This report tests an operational version of the Paper 15 lift.  The
diagonal of the empirical density matrix is the six-answer softmax
distribution; the off-diagonal entries come from residual covariance
projected onto the six answer-readout directions, with the largest
PSD-safe coherence scale allowed by the requested gamma.

## Family Summary

| layer | family | mean squash ratio | median | density diag/pre ratio |
|---:|---|---:|---:|---:|
| 31 | cartan | 0.0888632 | 0.0888632 | 0.142161 |
| 31 | nonabelian_su2 | 0.12362 | 0.12362 | 0.322389 |
| 31 | nonabelian_su3 | 0.153318 | 0.154255 | 0.312939 |

Interpretation: lower squash ratio means more hidden-space motion is lost
after LayerNorm + unembedding + Softmax.  The decisive comparison is
`nonabelian_*` versus `cartan` at matched theta on the same layer.

## Density Coherence

| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |
|---:|---:|---:|---:|---:|
| 31 | 0.35 | 0.410768 | 7.678e-02 | 0.214719 |

## Generator Details

| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| 31 | cartan | cartan_fourier_k1 | 0.05 | 0.0226497 | 0.00316323 | 0.11688 | [0.062809, 0.168911] | 0.00760008 | 0.000918012 |
| 31 | cartan | cartan_fourier_k2 | 0.05 | 0.0233408 | 0.00201247 | 0.0608458 | [0.0278747, 0.0987204] | 0.00751005 | 0.00122813 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.124486 | 0.0106717 | 0.12362 | [0.0961739, 0.153896] | 0.0201189 | 0.00648613 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.0645105 | 0.00863239 | 0.137132 | [0.0941649, 0.189408] | 0.0158609 | 0.00379501 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.058761 | 0.00877201 | 0.154255 | [0.118886, 0.185677] | 0.0144422 | 0.00481108 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.0649219 | 0.00939575 | 0.168568 | [0.129067, 0.208264] | 0.0168269 | 0.00616575 |

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