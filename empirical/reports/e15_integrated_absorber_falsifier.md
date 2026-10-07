# E15 Integrated Absorber Falsifier

- timestamp: `2026-06-04T00:00:25.000779+00:00`
- seed: `20260603`
- trials per domain: `650`
- admitted/bait share: `0.6` / `0.3`
- alpha: `0.05`
- ridge: `0.002`
- finding: **CONTINUOUS_ABSORBER_FITS_INTENSITY_BUT_GATES_CONTROL_ADMISSION**

## Claim Tested

E15 tests whether a single pooled continuous policy can absorb the
governed-admission story. The continuous absorber sees all domains,
train-side control fields, squares, and pairwise interactions. The
gate bank sees only domain-calibrated held-out persistence.

The probe scores graded operation intensity separately from admission
into a durable operation.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous intensity RMSE | 0.049 |
| gate intensity RMSE | 0.140 |
| governed intensity RMSE | 0.047 |
| hybrid intensity RMSE | 0.047 |
| continuous admission RMSE | 0.446 |
| gate admission RMSE | 0.132 |
| governed admission RMSE | 0.136 |
| hybrid admission RMSE | 0.043 |
| continuous false admission | 0.708 |
| gate false admission | 0.048 |
| governed false admission | 0.048 |
| continuous detection | 0.931 |
| gate detection | 1.000 |
| governed detection | 1.000 |
| continuous bait false | 0.925 |
| gate bait false | 0.062 |

## Model Summary

| model | intensity RMSE | intensity R2 | admission RMSE | admission acc | detect | nonadmit FA | bait FA | other FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.162 | -0.000 | 0.473 | 0.611 | 1.000 | 1.000 | 1.000 | 1.000 |
| continuous_absorber | 0.049 | 0.906 | 0.446 | 0.683 | 0.931 | 0.708 | 0.925 | 0.003 |
| gate_bank | 0.140 | 0.246 | 0.132 | 0.982 | 1.000 | 0.048 | 0.062 | 0.000 |
| governed_absorber | 0.047 | 0.916 | 0.136 | 0.982 | 1.000 | 0.048 | 0.062 | 0.000 |
| hybrid_full | 0.047 | 0.916 | 0.043 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 |

## Calibrated Gates

| domain | gate |
| --- | --- |
| current | 0.406 |
| structure | 0.378 |
| ambiguity | 0.384 |
| externalize | 0.409 |
| refusal | 0.413 |

## Domain Admission Summary

| domain | cont detect | cont FA | cont bait FA | gate detect | gate FA | gate bait FA | governed FA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| current | 0.869 | 0.619 | 0.827 | 1.000 | 0.054 | 0.073 | 0.054 |
| structure | 0.940 | 0.733 | 0.925 | 1.000 | 0.032 | 0.040 | 0.032 |
| ambiguity | 0.954 | 0.775 | 0.971 | 1.000 | 0.069 | 0.086 | 0.069 |
| externalize | 0.932 | 0.708 | 0.917 | 1.000 | 0.049 | 0.063 | 0.049 |
| refusal | 0.963 | 0.697 | 0.983 | 1.000 | 0.033 | 0.046 | 0.033 |

## Source Means

| source | n | intensity | admit | gate score | drive | flow | uncert | eig | resource | risk | rule | tool | candidate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ambiguity:ambiguity_world | 388 | 0.912 | 1.000 | 0.864 | 0.780 | 0.111 | 0.731 | 0.883 | 0.109 | 0.111 | 0.111 | 0.109 | 0.894 |
| ambiguity:eig_bait_world | 209 | 0.872 | 0.000 | 0.288 | 0.776 | 0.111 | 0.729 | 0.882 | 0.112 | 0.115 | 0.108 | 0.111 | 0.900 |
| ambiguity:no_sample_world | 53 | 0.123 | 0.000 | 0.158 | 0.117 | 0.106 | 0.183 | 0.123 | 0.116 | 0.104 | 0.115 | 0.108 | 0.142 |
| current:current_bait_world | 179 | 0.854 | 0.000 | 0.298 | 0.894 | 0.875 | 0.109 | 0.105 | 0.111 | 0.106 | 0.110 | 0.115 | 0.110 |
| current:current_world | 411 | 0.898 | 1.000 | 0.872 | 0.888 | 0.888 | 0.109 | 0.114 | 0.113 | 0.115 | 0.113 | 0.112 | 0.112 |
| current:idle_world | 60 | 0.144 | 0.000 | 0.128 | 0.104 | 0.118 | 0.109 | 0.115 | 0.108 | 0.104 | 0.113 | 0.118 | 0.097 |
| externalize:compress_world | 62 | 0.520 | 0.000 | 0.219 | 0.609 | 0.105 | 0.099 | 0.110 | 0.680 | 0.122 | 0.110 | 0.230 | 0.108 |
| externalize:tool_bait_world | 205 | 0.859 | 0.000 | 0.298 | 0.813 | 0.110 | 0.114 | 0.114 | 0.889 | 0.099 | 0.119 | 0.903 | 0.109 |
| externalize:tool_world | 383 | 0.895 | 1.000 | 0.859 | 0.818 | 0.108 | 0.105 | 0.109 | 0.897 | 0.112 | 0.111 | 0.885 | 0.108 |
| refusal:forbidden_world | 406 | 0.874 | 1.000 | 0.871 | 0.823 | 0.111 | 0.115 | 0.115 | 0.111 | 0.386 | 0.899 | 0.109 | 0.114 |
| refusal:risk_world | 71 | 0.776 | 0.000 | 0.246 | 0.773 | 0.095 | 0.109 | 0.108 | 0.104 | 0.888 | 0.141 | 0.098 | 0.112 |
| refusal:rule_bait_world | 173 | 0.834 | 0.000 | 0.300 | 0.814 | 0.121 | 0.114 | 0.108 | 0.116 | 0.381 | 0.902 | 0.117 | 0.115 |
| structure:noise_world | 52 | 0.734 | 0.000 | 0.190 | 0.583 | 0.110 | 0.839 | 0.113 | 0.118 | 0.102 | 0.110 | 0.093 | 0.106 |
| structure:structure_world | 399 | 0.954 | 1.000 | 0.860 | 0.826 | 0.109 | 0.887 | 0.110 | 0.109 | 0.109 | 0.108 | 0.112 | 0.114 |
| structure:uncertainty_bait_world | 199 | 0.916 | 0.000 | 0.279 | 0.816 | 0.113 | 0.883 | 0.109 | 0.112 | 0.107 | 0.104 | 0.108 | 0.109 |

## Phase Sweep

| admit share | bait share | intensity winner | admission winner | cont intensity | gate intensity | governed intensity | cont FA | gate FA | gate detect | cont bait FA | gate bait FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.300 | continuous_absorber | gate_bank | 0.047 | 0.220 | 0.052 | 0.000 | 0.000 | nan | 0.000 | 0.000 |
| 0.250 | 0.300 | hybrid_full | hybrid_full | 0.049 | 0.213 | 0.049 | 0.149 | 0.058 | 1.000 | 0.370 | 0.134 |
| 0.450 | 0.300 | hybrid_full | hybrid_full | 0.049 | 0.183 | 0.047 | 0.434 | 0.055 | 1.000 | 0.796 | 0.099 |
| 0.600 | 0.300 | governed_absorber | hybrid_full | 0.050 | 0.142 | 0.048 | 0.696 | 0.062 | 1.000 | 0.901 | 0.079 |
| 0.800 | 0.100 | governed_absorber | hybrid_full | 0.048 | 0.123 | 0.047 | 0.471 | 0.044 | 1.000 | 1.000 | 0.089 |
| 1.000 | 0.000 | continuous_absorber | scalar | 0.044 | 0.057 | 0.044 | nan | nan | 1.000 | nan | nan |

## Interpretation

The pooled absorber wins the graded intensity problem against the
gate-only model, which is exactly where continuous control fields
should win. But it still admits bait/null cases too often. The
calibrated gate bank recovers admission across domains while
controlling false admission, and the governed absorber combines
both advantages.

## Anti-Tautology Checks

- scalar surprise is matched across all domains;
- the continuous absorber pools all five domains and receives expanded nonlinear features;
- admitted and bait cases share train-side continuous fields within each domain;
- only held-out persistence separates durable admission from local bait;
- gates are calibrated on non-admitted calibration cases, not on the test labels;
- the result is synthetic architectural evidence, not biological validation.
