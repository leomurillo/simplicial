# Nonlinear Base-10 Shortcut Ablation -- Llama-3.1-8B

**Run date:** 2026-05-16
**Feature source:** `months\subspace\pca_k64\result\features\raw_features.safetensors`
**Dataset source:** `months\subspace\pca_k64\result\train_dataset.json`
**Split:** 60 train / 24 test (2 held out per result month)
**Ridge alpha:** `0.01`

## Experiment

This is a feature-level nonlinear ablation for the base-10 shortcut alternative.  Residualizers are fit on the training fold only.  The primary ablation, `decimal_sum_digits`, removes the subspace predicted by source month, offset, raw decimal sum ones/tens digits, base-10 carry, and mod-12 wrap carry.  The `raw_sum_class` ablation is an aggressive oracle upper bound because the unwrapped sum almost determines the cyclic result in this dataset.

## Ablation Summary

| ablation | result acc | raw-sum acc | ones acc | carry10 acc | wrap12 acc | k=2 acc | k=6 acc | H_12 fraction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| none | 0.958 | 0.917 | 0.958 | 1.000 | 1.000 | 1.000 | 0.958 | 0.355640 |
| linear_source_offset | 1.000 | 1.000 | 0.958 | 0.708 | 0.708 | 1.000 | 0.958 | 0.330952 |
| decimal_sum_digits | 0.458 | 0.583 | 0.167 | 0.583 | 0.667 | 0.500 | 0.625 | 0.065181 |
| raw_sum_class | 0.083 | 0.042 | 0.083 | 0.583 | 0.667 | 0.458 | 0.125 | 0.000000 |

## Full-Label Result-Probe Packet Fractions

| ablation | H_2 | H_3 | H_4 | H_6 | H_12 |
|---|---:|---:|---:|---:|---:|
| none | 0.112379 | 0.183369 | 0.154248 | 0.194364 | 0.355640 |
| linear_source_offset | 0.093864 | 0.153776 | 0.155150 | 0.266257 | 0.330952 |
| decimal_sum_digits | 0.000000 | 0.217861 | 0.488431 | 0.228527 | 0.065181 |
| raw_sum_class | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## Reading

In these runs, result accuracy and `H_12` packet mass drop sharply after `decimal_sum_digits`, so the live hidden-state result probe is strongly entangled with the tested base-10 sum/carry code. The `raw_sum_class` row should be read as a deliberately over-strong oracle check, not as the primary causal claim. This is a probe-level feature ablation, not a causal forward-pass intervention.
