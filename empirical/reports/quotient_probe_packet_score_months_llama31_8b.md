# Quotient-Tied Linear Probe Packet Score -- Llama-3.1-8B

**Run date:** 2026-05-16
**Feature source:** `months\subspace\pca_k64\result\features\training_features.safetensors`
**Dataset source:** `months\subspace\pca_k64\result\train_dataset.json`
**Split:** 60 train / 24 test (2 held out per month)
**Ridge alpha:** `0.01`

## Experiment

For each quotient `k | 12`, an affine ridge probe is trained from the saved layer-28 PCA-64 month features to the coarse label `month mod k`. The `k` probe logits are lifted back to twelve labels by pullback `score_12[x] = score_k[x mod k]`, then the held-out lifted logits are decomposed into cyclic conductor packets.

This is an actual trained quotient probe/lens instantiation of T2/T3, but the lifted forbidden-packet zeros are analytic consequences of the pullback `q^*`, not independent model evidence. The empirical content is the held-out accuracy retained while the probe is forced to use a packet-blind coarse codomain.

## Probe Accuracy And Analytic Forbidden-Energy Check

| quotient k | train acc | test acc | analytic forbidden fraction | analytic max forbidden energy | allowed packets | forbidden packets |
|---:|---:|---:|---:|---:|---|---|
| 2 | 1.000 | 0.917 | 5.576e-33 | 1.385e-30 | H_2 | H_3, H_4, H_6, H_12 |
| 3 | 1.000 | 0.583 | 0.000e+00 | 0.000e+00 | H_3 | H_2, H_4, H_6, H_12 |
| 4 | 1.000 | 0.583 | 3.553e-33 | 5.350e-31 | H_2, H_4 | H_3, H_6, H_12 |
| 6 | 1.000 | 0.792 | 0.000e+00 | 0.000e+00 | H_2, H_3, H_6 | H_4, H_12 |
| 12 | 1.000 | 0.667 | 0.000e+00 | 0.000e+00 | H_2, H_3, H_4, H_6, H_12 | none |

## Held-Out Lifted-Logit Packet Fractions

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 3 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 |
| 4 | 0.267739 | 0.000000 | 0.732261 | 0.000000 | 0.000000 |
| 6 | 0.238014 | 0.444243 | 0.000000 | 0.317743 | 0.000000 |
| 12 | 0.119861 | 0.223716 | 0.327817 | 0.160012 | 0.168594 |

## Reading

The numerical-zero forbidden energy is a sanity check that the lifted scores really lie in the quotient subspace. It should not be counted as evidence about the model: once the script sets `score_12[x] = score_k[x mod k]`, T1 already forces those entries to zero.

The evidence is instead in the accuracies. A coarse quotient probe can retain real held-out behavior while being algebraically blind to high conductor packets. The full `k = 12` probe is the escape hatch: because its target is the full label algebra, the conductor obstruction does not remove any packet.

## Insights

1. Accuracy and packet visibility decouple.  A quotient probe can be accurate on its coarse target while still being exactly blind to packets outside the quotient algebra.
2. Bias and ridge tuning do not matter for the obstruction.  They change the function inside `L^2(C_k)`, but the pullback remains inside the quotient subspace.
3. A poor full-label probe would not refute T2.  The theorem says the full codomain permits all packets, not that a particular training run must learn all of them.
4. The stronger native final-logit version is supplied by `native_logit_lens_binning_packet_score.py`.  The remaining stronger variant is a true tuned lens across intermediate layers, packet-scored before and after quotient binning.
