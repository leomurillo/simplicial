# E17 Temporal PenDigits Admission Probe

- timestamp: `2026-06-04T00:52:25.735240+00:00`
- dataset: `UCI Pen-Based Recognition of Handwritten Digits`
- dataset URL: `https://archive.ics.uci.edu/dataset/81/pen+based+recognition+of+handwritten+digits`
- train/calibration/test: `5620` / `1874` / `3498`
- early/gate/audit points: `2` / `[4, 5, 6]` / `[7, 8]`
- audit threshold: `1.0`
- alpha: `0.05`
- finding: **TEMPORAL_PERSISTENCE_GOVERNS_ADMISSION**

## Claim Tested

E17 tests whether E16's negative static-image result changes when
the external proxy has temporal structure. Early trajectory points
supply local continuous evidence, middle points supply a label-free
persistence gate, and late points define durable admission.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous intensity RMSE | 0.016 |
| gate intensity RMSE | 0.017 |
| governed intensity RMSE | 0.017 |
| hybrid intensity RMSE | 0.017 |
| continuous admission RMSE | 0.397 |
| gate admission RMSE | 0.312 |
| governed admission RMSE | 0.292 |
| hybrid admission RMSE | 0.212 |
| continuous false admission | 0.265 |
| gate false admission | 0.055 |
| governed false admission | 0.096 |
| continuous detection | 0.794 |
| gate detection | 0.768 |
| continuous bait false | 0.484 |
| gate bait false | 0.135 |
| gate threshold | 0.017 |
| bait threshold | 0.023 |

## Split Summary

| split | n | early acc | durable rate | mean intensity | mean gate | gate same | audit true |
| --- | --- | --- | --- | --- | --- | --- | --- |
| train | 5620 | 0.477 | 0.454 | 0.124 | 0.010 | 0.569 | 0.871 |
| calibration | 1874 | 0.475 | 0.446 | 0.124 | 0.010 | 0.565 | 0.870 |
| test | 3498 | 0.457 | 0.418 | 0.123 | 0.010 | 0.547 | 0.810 |

## Model Summary

| model | intensity RMSE | intensity R2 | admission RMSE | admission acc | detect | nonadmit FA | bait FA | bait n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.015 | 0.261 | 0.464 | 0.657 | 0.585 | 0.292 | 0.859 | 672 |
| continuous_early | 0.016 | 0.192 | 0.397 | 0.760 | 0.794 | 0.265 | 0.484 | 672 |
| temporal_gate | 0.017 | 0.123 | 0.312 | 0.871 | 0.768 | 0.055 | 0.135 | 672 |
| governed_temporal | 0.017 | 0.104 | 0.292 | 0.885 | 0.858 | 0.096 | 0.119 | 672 |
| hybrid_full | 0.017 | 0.058 | 0.212 | 0.937 | 0.957 | 0.077 | 0.112 | 672 |

## Digit Summary

| digit | n | early acc | durable rate | bait rate | intensity | gate score | audit true | cont FA | gate FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 363 | 0.738 | 0.725 | 0.058 | 0.129 | 0.017 | 0.822 | 0.190 | 0.080 |
| 1 | 364 | 0.571 | 0.429 | 0.269 | 0.130 | 0.013 | 0.467 | 0.466 | 0.144 |
| 2 | 364 | 0.646 | 0.629 | 0.104 | 0.121 | 0.012 | 0.953 | 0.141 | 0.074 |
| 3 | 336 | 0.122 | 0.122 | 0.244 | 0.119 | 0.005 | 0.948 | 0.305 | 0.037 |
| 4 | 364 | 0.376 | 0.371 | 0.099 | 0.117 | 0.008 | 0.929 | 0.266 | 0.031 |
| 5 | 335 | 0.003 | 0.003 | 0.621 | 0.124 | 0.002 | 0.649 | 0.269 | 0.003 |
| 6 | 336 | 0.917 | 0.896 | 0.045 | 0.125 | 0.017 | 0.970 | 0.629 | 0.114 |
| 7 | 364 | 0.802 | 0.736 | 0.137 | 0.129 | 0.015 | 0.791 | 0.354 | 0.219 |
| 8 | 336 | 0.003 | 0.003 | 0.208 | 0.119 | 0.003 | 0.804 | 0.137 | 0.027 |
| 9 | 336 | 0.318 | 0.196 | 0.161 | 0.119 | 0.005 | 0.771 | 0.226 | 0.044 |

## Prefix Sweep

| early | gate | audit | early acc | durable rate | intensity winner | admission winner | cont FA | gate FA | cont detect | gate detect | cont bait FA | gate bait FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4,5,6 | 7,8 | 0.457 | 0.418 | scalar | hybrid_full | 0.265 | 0.055 | 0.794 | 0.768 | 0.484 | 0.135 |
| 3 | 4,5,6 | 7,8 | 0.577 | 0.522 | scalar | hybrid_full | 0.200 | 0.133 | 0.913 | 0.639 | 0.344 | 0.218 |
| 4 | 5,6 | 7,8 | 0.671 | 0.622 | scalar | hybrid_full | 0.177 | 0.276 | 0.962 | 0.738 | 0.281 | 0.326 |
| 5 | 6 | 7,8 | 0.737 | 0.693 | scalar | hybrid_full | 0.199 | 0.820 | 0.973 | 0.958 | 0.354 | 0.829 |

## Interpretation

Temporal persistence survives the external proxy: early continuous
stroke evidence fits graded intensity, but middle-stroke stability
controls false admission into durable recognition.

## Anti-Tautology Checks

- the dataset is external pen-trajectory digit data, not a synthetic B-series generator;
- early evidence uses only the first trajectory points;
- the persistence gate is label-free and uses middle trajectory points;
- durable admission is evaluated on later trajectory points and true labels;
- calibration thresholds are estimated on calibration examples and scored on the held-out test file;
- the prefix sweep tests whether the result depends on how much early evidence is available.
