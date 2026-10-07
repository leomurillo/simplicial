# Quantum-Lift Audit: Z/6Z Modular Addition

## Status

- model: `mistralai/Mistral-7B-v0.3`
- prompts: 216
- layers: 28, 29, 30, 31
- baseline six-bin accuracy: 0.5093
- mode: final residual readout/lift audit

This report tests an operational version of the Paper 15 lift.  The
diagonal of the empirical density matrix is the six-answer softmax
distribution; the off-diagonal entries come from residual covariance
projected onto the six answer-readout directions, with the largest
PSD-safe coherence scale allowed by the requested gamma.

## Family Summary

| layer | family | mean squash ratio | median | density diag/pre ratio |
|---:|---|---:|---:|---:|
| 28 | cartan | 16.8513 | 12.9081 | 0.169932 |
| 28 | nonabelian_su2 | 2.71631 | 2.03979 | 0.199844 |
| 28 | nonabelian_su3 | 4.16932 | 3.09439 | 0.142169 |
| 29 | cartan | 9.12134 | 6.83647 | 0.159722 |
| 29 | nonabelian_su2 | 2.16221 | 1.62487 | 0.183405 |
| 29 | nonabelian_su3 | 3.45966 | 2.51106 | 0.138982 |
| 30 | cartan | 4.97956 | 3.73693 | 0.18206 |
| 30 | nonabelian_su2 | 1.22093 | 0.918573 | 0.234186 |
| 30 | nonabelian_su3 | 2.01082 | 1.49538 | 0.154413 |
| 31 | cartan | 0.0901778 | 0.0972506 | 0.209932 |
| 31 | nonabelian_su2 | 0.102508 | 0.0945913 | 0.241893 |
| 31 | nonabelian_su3 | 0.12165 | 0.124078 | 0.202582 |

Interpretation: lower squash ratio means more hidden-space motion is lost
after LayerNorm + unembedding + Softmax.  The decisive comparison is
`nonabelian_*` versus `cartan` at matched theta on the same layer.

## Density Coherence

| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |
|---:|---:|---:|---:|---:|
| 28 | 0.35 | 0.205449 | 9.198e-02 | 0.184104 |
| 29 | 0.35 | 0.21139 | 9.215e-02 | 0.184541 |
| 30 | 0.35 | 0.245898 | 9.229e-02 | 0.187329 |
| 31 | 0.35 | 0.23978 | 9.594e-02 | 0.186804 |

## Generator Details

| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| 28 | cartan | cartan_fourier_k1 | 0.02 | 0.0265346 | 0.281642 | 42.9177 | [16.2659, 95.4706] | 0.00224103 | 0.000419996 |
| 28 | cartan | cartan_fourier_k1 | 0.05 | 0.0663264 | 0.281065 | 17.2113 | [6.49356, 38.3321] | 0.00560168 | 0.00100671 |
| 28 | cartan | cartan_fourier_k1 | 0.1 | 0.132596 | 0.280366 | 8.60498 | [3.24353, 19.1754] | 0.0111971 | 0.00186922 |
| 28 | cartan | cartan_fourier_k2 | 0.02 | 0.0252451 | 0.281743 | 20.2369 | [17.83, 22.9245] | 0.00198625 | 0.00031052 |
| 28 | cartan | cartan_fourier_k2 | 0.05 | 0.063111 | 0.281408 | 8.08911 | [7.1224, 9.16592] | 0.00496506 | 0.000797417 |
| 28 | cartan | cartan_fourier_k2 | 0.1 | 0.126194 | 0.281432 | 4.04793 | [3.56706, 4.58684] | 0.00992606 | 0.00167336 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.0905608 | 0.282178 | 5.08283 | [4.57015, 5.58013] | 0.00577102 | 0.00111865 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.226322 | 0.282794 | 2.03979 | [1.83019, 2.23354] | 0.0144232 | 0.00285941 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.452138 | 0.283919 | 1.0263 | [0.922606, 1.1247] | 0.0288151 | 0.00597746 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0561363 | 0.282061 | 7.65845 | [6.96251, 8.32454] | 0.00448657 | 0.00056168 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.140353 | 0.282873 | 3.07078 | [2.78872, 3.33936] | 0.0112133 | 0.00160401 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.280662 | 0.283303 | 1.53437 | [1.39349, 1.66864] | 0.0224039 | 0.00386526 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0577799 | 0.281845 | 8.05701 | [7.32641, 8.9983] | 0.00317464 | 0.000486804 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.144519 | 0.281848 | 3.21943 | [2.92859, 3.59522] | 0.0079345 | 0.00120101 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.289171 | 0.282337 | 1.61194 | [1.46629, 1.79492] | 0.015854 | 0.00236466 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0615041 | 0.281749 | 7.7262 | [6.91364, 8.51659] | 0.00508062 | 0.000548474 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.153745 | 0.281831 | 3.09439 | [2.77246, 3.41199] | 0.0126979 | 0.00158154 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.307348 | 0.282738 | 1.55134 | [1.39103, 1.71015] | 0.0253698 | 0.00386618 |
| 29 | cartan | cartan_fourier_k1 | 0.02 | 0.0292565 | 0.254658 | 16.1489 | [13.6985, 19.8361] | 0.0021598 | 0.000332593 |
| 29 | cartan | cartan_fourier_k1 | 0.05 | 0.0731344 | 0.254586 | 6.45424 | [5.4641, 7.93873] | 0.00539867 | 0.000792088 |
| 29 | cartan | cartan_fourier_k1 | 0.1 | 0.14622 | 0.254546 | 3.22901 | [2.73581, 3.96949] | 0.0107915 | 0.00145576 |
| 29 | cartan | cartan_fourier_k2 | 0.02 | 0.0289198 | 0.254676 | 18.0699 | [15.2891, 21.8233] | 0.00203461 | 0.000344833 |
| 29 | cartan | cartan_fourier_k2 | 0.05 | 0.0722922 | 0.25416 | 7.2187 | [6.1088, 8.72299] | 0.00508588 | 0.000880589 |
| 29 | cartan | cartan_fourier_k2 | 0.1 | 0.144535 | 0.254032 | 3.60731 | [3.05031, 4.3625] | 0.0101671 | 0.00183105 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.103755 | 0.254996 | 4.04646 | [3.6323, 4.4724] | 0.00585965 | 0.00102683 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.259334 | 0.255617 | 1.62487 | [1.45777, 1.8029] | 0.0146447 | 0.00265723 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.518208 | 0.256098 | 0.8153 | [0.732652, 0.905095] | 0.029258 | 0.00566235 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0646859 | 0.255139 | 6.27486 | [5.65001, 6.96084] | 0.00460535 | 0.000504145 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.161754 | 0.255486 | 2.51106 | [2.26751, 2.78922] | 0.0115101 | 0.00146046 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.323537 | 0.256161 | 1.25767 | [1.13389, 1.39439] | 0.0229973 | 0.00358018 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0634014 | 0.254952 | 6.95028 | [6.27138, 7.71887] | 0.00330291 | 0.000546346 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.158574 | 0.255344 | 2.78 | [2.51171, 3.08783] | 0.00825507 | 0.00138353 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.31729 | 0.256378 | 1.39157 | [1.2614, 1.54759] | 0.0164944 | 0.00283635 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0705161 | 0.25446 | 6.23917 | [5.5671, 6.94097] | 0.00509976 | 0.000493143 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.176228 | 0.253873 | 2.48768 | [2.21899, 2.77159] | 0.0127458 | 0.00145488 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.352139 | 0.253646 | 1.24468 | [1.11258, 1.38748] | 0.0254658 | 0.00364147 |
| 30 | cartan | cartan_fourier_k1 | 0.02 | 0.0241899 | 0.146555 | 8.89141 | [7.73056, 10.4753] | 0.0021566 | 0.000467935 |
| 30 | cartan | cartan_fourier_k1 | 0.05 | 0.0604648 | 0.146395 | 3.56266 | [3.09027, 4.1827] | 0.0053907 | 0.0011274 |
| 30 | cartan | cartan_fourier_k1 | 0.1 | 0.120874 | 0.146358 | 1.78275 | [1.54675, 2.09225] | 0.0107756 | 0.00211206 |
| 30 | cartan | cartan_fourier_k2 | 0.02 | 0.0232894 | 0.146449 | 9.77372 | [8.75901, 10.9171] | 0.00209516 | 0.000315802 |
| 30 | cartan | cartan_fourier_k2 | 0.05 | 0.0582184 | 0.146369 | 3.9112 | [3.50756, 4.37331] | 0.0052372 | 0.000813965 |
| 30 | cartan | cartan_fourier_k2 | 0.1 | 0.116399 | 0.146578 | 1.95565 | [1.75489, 2.18803] | 0.0104693 | 0.00171795 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.0910571 | 0.146714 | 2.28176 | [2.09875, 2.46215] | 0.00614693 | 0.00140596 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.227589 | 0.147084 | 0.918573 | [0.844362, 0.99266] | 0.0153628 | 0.00357762 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.454753 | 0.147596 | 0.462452 | [0.423739, 0.499765] | 0.0306933 | 0.00739574 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0538752 | 0.146354 | 3.73223 | [3.47124, 4.01583] | 0.00475752 | 0.00055505 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.134708 | 0.146802 | 1.49538 | [1.38716, 1.60565] | 0.0118906 | 0.00154485 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.2694 | 0.147361 | 0.752343 | [0.698617, 0.806622] | 0.0237579 | 0.00364403 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0529943 | 0.146636 | 3.91706 | [3.54473, 4.31325] | 0.0033337 | 0.000384452 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.132528 | 0.146703 | 1.56067 | [1.41009, 1.71936] | 0.00833223 | 0.00100559 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.265123 | 0.14726 | 0.780937 | [0.705276, 0.859388] | 0.0166499 | 0.00217022 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0583288 | 0.146453 | 3.6538 | [3.31445, 3.98544] | 0.00537539 | 0.00102173 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.145761 | 0.147131 | 1.46716 | [1.33809, 1.60264] | 0.0134347 | 0.00274844 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.291227 | 0.148431 | 0.73776 | [0.677999, 0.803372] | 0.0268422 | 0.0061398 |
| 31 | cartan | cartan_fourier_k1 | 0.02 | 0.0221756 | 0.00182655 | 0.0664695 | [0.0442022, 0.0936469] | 0.00237718 | 0.0006216 |
| 31 | cartan | cartan_fourier_k1 | 0.05 | 0.0554276 | 0.0067371 | 0.111844 | [0.0971322, 0.129924] | 0.00594201 | 0.00151059 |
| 31 | cartan | cartan_fourier_k1 | 0.1 | 0.110797 | 0.013776 | 0.128587 | [0.116958, 0.140782] | 0.0118773 | 0.002874 |
| 31 | cartan | cartan_fourier_k2 | 0.02 | 0.0205956 | 0.00132878 | 0.0396658 | [0.0279809, 0.0534379] | 0.00209214 | 0.000334608 |
| 31 | cartan | cartan_fourier_k2 | 0.05 | 0.0514868 | 0.00488317 | 0.0875501 | [0.0697765, 0.107864] | 0.00522964 | 0.00086704 |
| 31 | cartan | cartan_fourier_k2 | 0.1 | 0.102949 | 0.0104401 | 0.106951 | [0.0935503, 0.11924] | 0.0104543 | 0.00184183 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.0830656 | 0.00778848 | 0.131788 | [0.115309, 0.148091] | 0.00589614 | 0.00140025 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.207578 | 0.0134358 | 0.0945913 | [0.0861153, 0.103469] | 0.0147359 | 0.00354729 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.414667 | 0.0236412 | 0.081143 | [0.0745646, 0.087411] | 0.02944 | 0.0072855 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0485168 | 0.00555253 | 0.130752 | [0.114016, 0.151012] | 0.00461305 | 0.000773027 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.121332 | 0.0112995 | 0.121749 | [0.110376, 0.133672] | 0.0115294 | 0.00207986 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.242735 | 0.01979 | 0.105891 | [0.0981535, 0.113565] | 0.0230362 | 0.00467426 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0491396 | 0.00579764 | 0.133241 | [0.116442, 0.153381] | 0.00326003 | 0.000451413 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.122882 | 0.0109722 | 0.126555 | [0.114347, 0.139622] | 0.00814808 | 0.00118033 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.245805 | 0.0186402 | 0.105927 | [0.0985373, 0.11359] | 0.0162819 | 0.00253812 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0530617 | 0.00672791 | 0.142832 | [0.123736, 0.164352] | 0.00539643 | 0.00141036 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.132589 | 0.0125809 | 0.124078 | [0.111513, 0.136753] | 0.0134872 | 0.00370615 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.264892 | 0.0225493 | 0.103822 | [0.0964308, 0.110952] | 0.0269468 | 0.00800336 |

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