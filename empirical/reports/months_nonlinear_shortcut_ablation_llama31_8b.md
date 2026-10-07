# Nonlinear Base-10 Shortcut Ablation -- Llama-3.1-8B

**Run date:** 2026-05-16
**Feature source:** `months\subspace\pca_k64\result\features\training_features.safetensors`
**Dataset source:** `months\subspace\pca_k64\result\train_dataset.json`
**Split:** 60 train / 24 test (2 held out per result month)
**Ridge alpha:** `0.01`

## Experiment

This is a feature-level nonlinear ablation for the base-10 shortcut alternative.  Residualizers are fit on the training fold only.  The primary ablation, `decimal_sum_digits`, removes the subspace predicted by source month, offset, raw decimal sum ones/tens digits, base-10 carry, and mod-12 wrap carry.  The `raw_sum_class` ablation is an aggressive oracle upper bound because the unwrapped sum almost determines the cyclic result in this dataset.

## Ablation Summary

| ablation | result acc | raw-sum acc | ones acc | carry10 acc | wrap12 acc | k=2 acc | k=6 acc | H_12 fraction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| none | 0.667 | 0.625 | 0.583 | 0.750 | 0.875 | 0.917 | 0.792 | 0.168594 |
| linear_source_offset | 0.750 | 0.708 | 0.833 | 0.667 | 0.583 | 0.958 | 0.875 | 0.232286 |
| decimal_sum_digits | 0.417 | 0.333 | 0.167 | 0.583 | 0.667 | 0.500 | 0.542 | 0.090505 |
| raw_sum_class | 0.167 | 0.083 | 0.042 | 0.583 | 0.667 | 0.542 | 0.125 | 0.000000 |

## Full-Label Result-Probe Packet Fractions

| ablation | H_2 | H_3 | H_4 | H_6 | H_12 |
|---|---:|---:|---:|---:|---:|
| none | 0.119861 | 0.223716 | 0.327817 | 0.160012 | 0.168594 |
| linear_source_offset | 0.073030 | 0.254667 | 0.233168 | 0.206848 | 0.232286 |
| decimal_sum_digits | 0.000000 | 0.330205 | 0.439345 | 0.139945 | 0.090505 |
| raw_sum_class | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## Reading

In these runs, result accuracy and `H_12` packet mass drop sharply after `decimal_sum_digits`, so the live hidden-state result probe is strongly entangled with the tested base-10 sum/carry code. The `raw_sum_class` row should be read as a deliberately over-strong oracle check, not as the primary causal claim. This is a probe-level feature ablation, not a causal forward-pass intervention.
