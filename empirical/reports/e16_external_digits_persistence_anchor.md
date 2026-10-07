# E16 External Digits Persistence Anchor

- timestamp: `2026-06-04T00:35:03.051598+00:00`
- dataset: `UCI Optical Recognition of Handwritten Digits`
- dataset URL: `https://archive.ics.uci.edu/dataset/80/optical%2Brecognition%2Bof%2Bhandwritten%2Bdigits`
- train/calibration/test: `2867` / `956` / `1797`
- audit threshold: `0.5`
- alpha: `0.05`
- finding: **EXTERNAL_CONTINUOUS_EVIDENCE_ABSORBS_PERSISTENCE**

## Claim Tested

E16 tests the B-series field/gate split on a real perceptual proxy:
the UCI handwritten digit recognition dataset. Original-image
evidence supplies the continuous field. Perturbation persistence
supplies the admission gate. The admission target is evaluated on a
different audit perturbation set, so the gate evidence is not the same
quantity as the test label.

## Main Decision Quantities

| quantity | value |
| --- | --- |
| continuous intensity RMSE | 0.019 |
| gate intensity RMSE | 0.029 |
| governed intensity RMSE | 0.020 |
| hybrid intensity RMSE | 0.021 |
| continuous admission RMSE | 0.298 |
| gate admission RMSE | 0.325 |
| governed admission RMSE | 0.295 |
| hybrid admission RMSE | 0.286 |
| continuous false admission | 0.093 |
| gate false admission | 0.090 |
| governed false admission | 0.087 |
| continuous detection | 0.765 |
| gate detection | 0.690 |
| continuous bait false | 0.065 |
| gate bait false | 0.081 |
| gate threshold | 0.022 |
| bait threshold | 0.054 |

## Split Summary

| split | n | orig acc | durable rate | mean intensity | mean gate | gate same | audit true |
| --- | --- | --- | --- | --- | --- | --- | --- |
| train | 2867 | 0.940 | 0.302 | 0.178 | 0.015 | 0.562 | 0.417 |
| calibration | 956 | 0.939 | 0.302 | 0.176 | 0.015 | 0.559 | 0.412 |
| test | 1797 | 0.918 | 0.267 | 0.173 | 0.014 | 0.552 | 0.399 |

## Model Summary

| model | intensity RMSE | intensity R2 | admission RMSE | admission acc | detect | nonadmit FA | bait FA | bait n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar | 0.017 | 0.762 | 0.431 | 0.733 | 0.000 | 0.000 | 0.000 | 382 |
| continuous_evidence | 0.019 | 0.699 | 0.298 | 0.869 | 0.765 | 0.093 | 0.065 | 382 |
| persistence_gate | 0.029 | 0.257 | 0.325 | 0.851 | 0.690 | 0.090 | 0.081 | 382 |
| governed_evidence | 0.020 | 0.666 | 0.295 | 0.880 | 0.790 | 0.087 | 0.076 | 382 |
| hybrid_full | 0.021 | 0.613 | 0.286 | 0.883 | 0.794 | 0.084 | 0.068 | 382 |

## Digit Summary

| digit | n | orig acc | durable rate | bait rate | intensity | gate score | audit true | cont FA | gate FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 178 | 0.983 | 0.000 | 0.556 | 0.192 | 0.012 | 0.294 | 0.000 | 0.000 |
| 1 | 182 | 0.868 | 0.714 | 0.000 | 0.162 | 0.020 | 0.608 | 0.346 | 0.538 |
| 2 | 177 | 0.949 | 0.316 | 0.254 | 0.179 | 0.019 | 0.433 | 0.240 | 0.207 |
| 3 | 183 | 0.907 | 0.317 | 0.120 | 0.166 | 0.008 | 0.404 | 0.160 | 0.040 |
| 4 | 181 | 0.950 | 0.006 | 0.425 | 0.186 | 0.014 | 0.324 | 0.006 | 0.011 |
| 5 | 182 | 0.984 | 0.038 | 0.522 | 0.190 | 0.012 | 0.302 | 0.000 | 0.006 |
| 6 | 181 | 0.967 | 0.823 | 0.000 | 0.182 | 0.021 | 0.625 | 0.531 | 0.875 |
| 7 | 179 | 0.933 | 0.330 | 0.168 | 0.175 | 0.017 | 0.435 | 0.267 | 0.083 |
| 8 | 174 | 0.759 | 0.092 | 0.075 | 0.152 | 0.008 | 0.256 | 0.025 | 0.108 |
| 9 | 180 | 0.878 | 0.022 | 0.006 | 0.148 | 0.009 | 0.299 | 0.011 | 0.017 |

## Audit-Threshold Sweep

| audit th | durable rate | intensity winner | admission winner | cont intensity | gate intensity | cont FA | gate FA | cont detect | gate detect | cont bait FA | gate bait FA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 0.267 | scalar | hybrid_full | 0.019 | 0.029 | 0.093 | 0.090 | 0.765 | 0.690 | 0.065 | 0.081 |
| 0.580 | 0.134 | scalar | governed_evidence | 0.018 | 0.030 | 0.031 | 0.054 | 0.671 | 0.608 | 0.029 | 0.034 |
| 0.720 | 0.028 | scalar | governed_evidence | 0.018 | 0.031 | 0.002 | 0.000 | 0.080 | 0.000 | 0.000 | 0.000 |
| 0.860 | 0.004 | scalar | hybrid_full | 0.019 | 0.031 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.000 | 0.004 | scalar | hybrid_full | 0.018 | 0.031 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Interpretation

Original-image continuous evidence absorbs the persistence gate on
this task. This is a negative anchor for the broad gate claim:
simple static recognition may not require a distinct admission
gate when local evidence already predicts perturbation durability.

## Anti-Tautology Checks

- the dataset is external real handwritten digit data, not a synthetic B-series generator;
- the OCR classifier is trained from scratch using NumPy only;
- continuous evidence uses the original image only;
- gate evidence uses label-free persistence under one perturbation set;
- durable admission is evaluated with true labels under a different audit perturbation set;
- calibration thresholds are estimated on calibration examples and scored on the held-out test set;
- this is still not brain data; it is a real perceptual proxy and protocol rehearsal.
