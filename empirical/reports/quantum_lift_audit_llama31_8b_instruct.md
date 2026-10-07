# Quantum-Lift Audit: Z/6Z Modular Addition

## Status

- model: `meta-llama/Llama-3.1-8B-Instruct`
- prompts: 216
- layers: 28, 29, 30, 31
- baseline six-bin accuracy: 0.3241
- mode: final residual readout/lift audit

This report tests an operational version of the Paper 15 lift.  The
diagonal of the empirical density matrix is the six-answer softmax
distribution; the off-diagonal entries come from residual covariance
projected onto the six answer-readout directions, with the largest
PSD-safe coherence scale allowed by the requested gamma.

## Family Summary

| layer | family | mean squash ratio | median | density diag/pre ratio |
|---:|---|---:|---:|---:|
| 28 | cartan | 12.8696 | 9.65339 | 0.157838 |
| 28 | nonabelian_su2 | 3.02738 | 2.27874 | 0.15229 |
| 28 | nonabelian_su3 | 4.20851 | 3.14085 | 0.0737775 |
| 29 | cartan | 11.6825 | 8.76261 | 0.142148 |
| 29 | nonabelian_su2 | 2.71538 | 2.04367 | 0.158086 |
| 29 | nonabelian_su3 | 4.14724 | 3.01923 | 0.0781713 |
| 30 | cartan | 1.74195 | 1.30638 | 0.150705 |
| 30 | nonabelian_su2 | 0.470564 | 0.355033 | 0.0935508 |
| 30 | nonabelian_su3 | 0.758972 | 0.586507 | 0.113204 |
| 31 | cartan | 0.11607 | 0.123742 | 0.141997 |
| 31 | nonabelian_su2 | 0.0916107 | 0.0897394 | 0.109103 |
| 31 | nonabelian_su3 | 0.0924897 | 0.0914725 | 0.113379 |

Interpretation: lower squash ratio means more hidden-space motion is lost
after LayerNorm + unembedding + Softmax.  The decisive comparison is
`nonabelian_*` versus `cartan` at matched theta on the same layer.

## Density Coherence

| layer | gamma used | offdiag/diag Frobenius | min eigenvalue | purity |
|---:|---:|---:|---:|---:|
| 28 | 0.35 | 0.209736 | 9.640e-02 | 0.182642 |
| 29 | 0.35 | 0.215957 | 9.506e-02 | 0.183105 |
| 30 | 0.35 | 0.199129 | 9.686e-02 | 0.181883 |
| 31 | 0.35 | 0.196017 | 9.665e-02 | 0.181668 |

## Generator Details

| layer | family | generator | theta | pre chord | post Hellinger | squash ratio | 95% CI | density Bures | density post H |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
| 28 | cartan | cartan_fourier_k1 | 0.02 | 0.0177182 | 0.229492 | 25.2292 | [20.3032, 32.4258] | 0.00184453 | 0.00038197 |
| 28 | cartan | cartan_fourier_k1 | 0.05 | 0.0442881 | 0.230633 | 10.1176 | [8.15174, 13.0053] | 0.00461087 | 0.000978451 |
| 28 | cartan | cartan_fourier_k1 | 0.1 | 0.0885367 | 0.233637 | 5.09874 | [4.11845, 6.55412] | 0.00921848 | 0.00203851 |
| 28 | cartan | cartan_fourier_k2 | 0.02 | 0.0178751 | 0.228896 | 22.9848 | [19.6719, 26.7181] | 0.00216805 | 0.000214877 |
| 28 | cartan | cartan_fourier_k2 | 0.05 | 0.0446953 | 0.228538 | 9.18916 | [7.85733, 10.6869] | 0.00541944 | 0.00054841 |
| 28 | cartan | cartan_fourier_k2 | 0.1 | 0.0894005 | 0.228472 | 4.59839 | [3.93198, 5.33882] | 0.010834 | 0.00115171 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.0748844 | 0.22997 | 5.6386 | [4.80006, 6.51085] | 0.00576672 | 0.00093229 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.187131 | 0.232344 | 2.27874 | [1.94177, 2.63206] | 0.0144124 | 0.00220878 |
| 28 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.373778 | 0.237948 | 1.1648 | [0.995061, 1.34592] | 0.0287932 | 0.00408713 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0484623 | 0.229137 | 8.40881 | [7.27966, 9.59982] | 0.00460797 | 3.60631e-05 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.121047 | 0.229577 | 3.38063 | [2.91784, 3.85831] | 0.0115166 | 0.000247513 |
| 28 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.241648 | 0.232143 | 1.71409 | [1.47523, 1.95329] | 0.0230099 | 0.00118694 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0505675 | 0.229847 | 7.81384 | [6.73311, 8.96305] | 0.00324118 | 0.000491456 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.126483 | 0.231405 | 3.14085 | [2.69801, 3.60368] | 0.00810075 | 0.00128414 |
| 28 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.253071 | 0.235194 | 1.59163 | [1.36449, 1.82933] | 0.0161858 | 0.00275882 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0530192 | 0.228664 | 7.40856 | [6.48941, 8.50364] | 0.00449443 | 0.000202626 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.132591 | 0.227576 | 2.94779 | [2.57906, 3.38615] | 0.0112329 | 0.000363928 |
| 28 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.265218 | 0.227634 | 1.47037 | [1.28166, 1.69269] | 0.0224427 | 0.000561439 |
| 29 | cartan | cartan_fourier_k1 | 0.02 | 0.0184713 | 0.240134 | 22.7123 | [19.3668, 26.9471] | 0.00191724 | 0.000367305 |
| 29 | cartan | cartan_fourier_k1 | 0.05 | 0.0461721 | 0.241176 | 9.1106 | [7.76949, 10.799] | 0.00479256 | 0.000946935 |
| 29 | cartan | cartan_fourier_k1 | 0.1 | 0.0923082 | 0.243924 | 4.58658 | [3.91768, 5.42761] | 0.00958132 | 0.00199229 |
| 29 | cartan | cartan_fourier_k2 | 0.02 | 0.0185882 | 0.239722 | 21.0586 | [18.1683, 24.2283] | 0.00211907 | 0.000177676 |
| 29 | cartan | cartan_fourier_k2 | 0.05 | 0.0464774 | 0.239505 | 8.41463 | [7.26391, 9.68608] | 0.00529702 | 0.000447091 |
| 29 | cartan | cartan_fourier_k2 | 0.1 | 0.0929617 | 0.239774 | 4.21251 | [3.63575, 4.84999] | 0.0105893 | 0.000926993 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.0807187 | 0.240134 | 5.05813 | [4.38665, 5.71743] | 0.00587806 | 0.000987482 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.201676 | 0.241705 | 2.04367 | [1.77124, 2.31372] | 0.0146907 | 0.00233948 |
| 29 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.402718 | 0.246162 | 1.04435 | [0.904932, 1.18206] | 0.0293495 | 0.00431479 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0511598 | 0.23967 | 8.43404 | [7.33811, 9.66217] | 0.00472401 | 0.000219657 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.127806 | 0.239824 | 3.38192 | [2.95123, 3.8772] | 0.0118067 | 0.000453547 |
| 29 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.255212 | 0.241991 | 1.70683 | [1.49007, 1.95444] | 0.0235894 | 0.000999432 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0520961 | 0.239817 | 7.50765 | [6.57038, 8.48681] | 0.0032637 | 0.000468505 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.130289 | 0.241274 | 3.01923 | [2.64132, 3.41432] | 0.00815708 | 0.0012151 |
| 29 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.260637 | 0.243972 | 1.52644 | [1.33354, 1.7249] | 0.0162986 | 0.00258737 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0551583 | 0.239403 | 7.35555 | [6.42741, 8.47356] | 0.00454228 | 0.000241705 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.137961 | 0.238747 | 2.9307 | [2.55737, 3.38247] | 0.0113525 | 0.00046534 |
| 29 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.276029 | 0.239132 | 1.46284 | [1.27486, 1.69127] | 0.0226818 | 0.000698557 |
| 30 | cartan | cartan_fourier_k1 | 0.02 | 0.0292906 | 0.0665427 | 3.50181 | [3.01853, 4.15076] | 0.00193618 | 0.000439715 |
| 30 | cartan | cartan_fourier_k1 | 0.05 | 0.0732146 | 0.0668841 | 1.40344 | [1.21185, 1.6583] | 0.00483994 | 0.00112583 |
| 30 | cartan | cartan_fourier_k1 | 0.1 | 0.146364 | 0.0694319 | 0.714816 | [0.620202, 0.840198] | 0.00967619 | 0.00234243 |
| 30 | cartan | cartan_fourier_k2 | 0.02 | 0.0302688 | 0.0669096 | 3.00071 | [2.6601, 3.38834] | 0.00216537 | 0.000151129 |
| 30 | cartan | cartan_fourier_k2 | 0.05 | 0.0756795 | 0.0675417 | 1.20932 | [1.0767, 1.36391] | 0.0054128 | 0.000363383 |
| 30 | cartan | cartan_fourier_k2 | 0.1 | 0.151358 | 0.0700704 | 0.621624 | [0.55168, 0.699369] | 0.0108211 | 0.000708787 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.115798 | 0.0669956 | 0.860803 | [0.758886, 0.97983] | 0.00564739 | 0.000540247 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.289373 | 0.0691766 | 0.355033 | [0.314081, 0.402348] | 0.0141141 | 0.00130124 |
| 30 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.57801 | 0.0771702 | 0.195855 | [0.174203, 0.220254] | 0.028197 | 0.00261652 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0801976 | 0.0680788 | 1.41938 | [1.21274, 1.62772] | 0.00460403 | 0.000176535 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.200403 | 0.0715315 | 0.586507 | [0.503296, 0.673799] | 0.0115068 | 0.00041797 |
| 30 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.400376 | 0.0793597 | 0.313408 | [0.272391, 0.359091] | 0.0229901 | 0.00117285 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0816745 | 0.0668643 | 1.29033 | [1.11525, 1.47844] | 0.00315255 | 0.000658113 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.204258 | 0.0686468 | 0.527558 | [0.459081, 0.60428] | 0.00787929 | 0.00169167 |
| 30 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.408615 | 0.072794 | 0.278013 | [0.242896, 0.314251] | 0.0157436 | 0.00354085 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0873363 | 0.0671718 | 1.49347 | [1.22043, 1.80623] | 0.00449087 | 0.000437584 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.218501 | 0.0688132 | 0.605642 | [0.493284, 0.728149] | 0.0112239 | 0.000939266 |
| 30 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.437374 | 0.0745191 | 0.316449 | [0.259695, 0.378506] | 0.0224247 | 0.00142781 |
| 31 | cartan | cartan_fourier_k1 | 0.02 | 0.0343196 | 0.00343957 | 0.0976333 | [0.0757522, 0.118188] | 0.00197649 | 0.000413736 |
| 31 | cartan | cartan_fourier_k1 | 0.05 | 0.0857869 | 0.0112268 | 0.133826 | [0.119761, 0.148085] | 0.00494071 | 0.0010576 |
| 31 | cartan | cartan_fourier_k1 | 0.1 | 0.171504 | 0.0228806 | 0.146014 | [0.134856, 0.160677] | 0.00987772 | 0.00219685 |
| 31 | cartan | cartan_fourier_k2 | 0.02 | 0.0345809 | 0.00258847 | 0.0714622 | [0.0547087, 0.0908722] | 0.00214192 | 0.000146217 |
| 31 | cartan | cartan_fourier_k2 | 0.05 | 0.0864612 | 0.00936474 | 0.12051 | [0.104804, 0.139015] | 0.0053542 | 0.000363337 |
| 31 | cartan | cartan_fourier_k2 | 0.1 | 0.172922 | 0.0192144 | 0.126973 | [0.11486, 0.139703] | 0.0107042 | 0.000750015 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.02 | 0.133903 | 0.00999829 | 0.0990262 | [0.0854247, 0.114895] | 0.0056576 | 0.000631875 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.05 | 0.334624 | 0.022685 | 0.0897394 | [0.0798823, 0.100647] | 0.0141396 | 0.0015287 |
| 31 | nonabelian_su2 | su2_sigma_y_shadow | 0.1 | 0.668419 | 0.0440777 | 0.0860664 | [0.077668, 0.0963143] | 0.0282478 | 0.00303691 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.02 | 0.0944224 | 0.00890203 | 0.114986 | [0.100692, 0.135128] | 0.00461272 | 0.00016408 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.05 | 0.235868 | 0.0180898 | 0.0983909 | [0.0877384, 0.111842] | 0.0115285 | 0.000447563 |
| 31 | nonabelian_su3 | su3_lambda_01_shadow | 0.1 | 0.470943 | 0.0345179 | 0.0870488 | [0.0773635, 0.0993746] | 0.0230334 | 0.00134962 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.02 | 0.0952969 | 0.00760118 | 0.105648 | [0.0893607, 0.125951] | 0.00316175 | 0.000656258 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.05 | 0.23826 | 0.0144744 | 0.0779646 | [0.0675082, 0.0915524] | 0.00790223 | 0.001664 |
| 31 | nonabelian_su3 | su3_lambda_02_shadow | 0.1 | 0.47641 | 0.0267465 | 0.0708408 | [0.0631481, 0.081156] | 0.0157891 | 0.00341402 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.02 | 0.0991852 | 0.00852173 | 0.107596 | [0.0924374, 0.124249] | 0.00441077 | 0.000438788 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.05 | 0.248194 | 0.0177751 | 0.0914725 | [0.0821686, 0.103071] | 0.0110238 | 0.00094978 |
| 31 | nonabelian_su3 | su3_lambda_12_shadow | 0.1 | 0.496963 | 0.0326738 | 0.0784594 | [0.0709902, 0.0872291] | 0.0220248 | 0.00148507 |

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