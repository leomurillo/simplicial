# Hidden-State Shortcut Audit -- Llama-3.1-8B

**Run date:** 2026-05-16
**Feature source:** `months\subspace\pca_k64\result\features\raw_features.safetensors`
**Dataset source:** `months\subspace\pca_k64\result\train_dataset.json`
**Split:** 60 train / 24 test (2 held out per result month)
**Ridge alpha:** `0.01`

## Experiment

This audit uses per-example layer-28 hidden features rather than saved class centroids.  It is designed to test the base-10/input-side shortcut warning directly.  The `full hidden features` condition trains ordinary affine probes.  The `after source+offset residualization` condition first removes the linear subspace predicted by source month and offset number, fitting that residualizer only on the training fold.

No quotient lift is used for the full-label result probe, so its packet fractions are not forced by T1.  Quotient-probe accuracies are also ordinary held-out accuracies, not projector identities.

## Input-Side Target Decodability

| representation | target | classes | chance | train acc | test acc |
|---|---|---:|---:|---:|---:|
| full hidden features | result_month | 12 | 0.083 | 1.000 | 0.958 |
| full hidden features | source_month | 12 | 0.083 | 1.000 | 1.000 |
| full hidden features | offset_number | 7 | 0.143 | 1.000 | 1.000 |
| full hidden features | unwrapped_source_plus_offset | 18 | 0.056 | 1.000 | 0.917 |
| after source+offset residualization | result_month | 12 | 0.083 | 1.000 | 1.000 |
| after source+offset residualization | source_month | 12 | 0.083 | 0.117 | 0.000 |
| after source+offset residualization | offset_number | 7 | 0.143 | 0.200 | 0.042 |
| after source+offset residualization | unwrapped_source_plus_offset | 18 | 0.056 | 1.000 | 1.000 |

## Result Quotient Probe Test Accuracy

| representation | k=2 | k=3 | k=4 | k=6 | k=12 |
|---|---:|---:|---:|---:|---:|
| full hidden features | 1.000 | 0.833 | 0.958 | 0.958 | 0.958 |
| after source+offset residualization | 1.000 | 0.875 | 0.958 | 0.958 | 1.000 |

## Full-Label Result-Probe Packet Fractions

| representation | full-label test acc | H_2 | H_3 | H_4 | H_6 | H_12 |
|---|---:|---:|---:|---:|---:|---:|
| full hidden features | 0.958 | 0.112379 | 0.183369 | 0.154248 | 0.194364 | 0.355640 |
| after source+offset residualization | 1.000 | 0.093864 | 0.153776 | 0.155150 | 0.266257 | 0.330952 |

## Reading

If result-month accuracy survives source+offset residualization, the hidden state contains a linearly accessible result code beyond a linear readout of the obvious input-side variables. In these runs it survives and improves, so the linear input-shortcut alternative is falsified. This does not rule out a nonlinear base-10 sum/carry mechanism, which requires the separate nonlinear ablation. The packet fractions in the full-label probe are likewise empirical: unlike the quotient lift, an unconstrained twelve-class probe is allowed to place energy in any conductor packet.
