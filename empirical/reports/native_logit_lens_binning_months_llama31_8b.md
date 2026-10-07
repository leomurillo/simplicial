# Native Final-Logit Lens Binning Packet Score -- Llama-3.1-8B

**Run date:** 2026-05-16
**Full-vocabulary distribution:** `months\baseline\full_output_dists.safetensors`
**Samples:** `months\baseline\test_samples.json`
**Token-id source:** `months\baseline\top_logits.json`
**Examples:** 84

## Experiment

This uses the model's native final unembedding distribution.  The saved artifact stores probabilities over the full vocabulary; taking `log p(token)` gives logits up to a per-example additive constant, which vanishes after centering before conductor scoring.

For each example, the twelve month token scores are packet-scored before binning. That pre-bin packet profile is the model-facing measurement. Then the month-token probabilities are explicitly binned into the quotient classes `C_12 -> C_k`, converted back to log scores, lifted to twelve labels by `score_12[x] = score_k[x mod k]`, and packet-scored again as a projector sanity check.

## Month Token IDs

- January: token id `6186`
- February: token id `7552`
- March: token id `5587`
- April: token id `5936`
- May: token id `3297`
- June: token id `5651`
- July: token id `5887`
- August: token id `6287`
- September: token id `6250`
- October: token id `6664`
- November: token id `6841`
- December: token id `6790`

## Accuracy

- native twelve-month token accuracy: 0.988

## Before/After Binning

| quotient k | native forbidden fraction before binning | after-bin forbidden fraction | after-bin max forbidden energy | quotient acc |
|---:|---:|---:|---:|---:|
| 2 | 0.949392 | 4.975e-33 | 1.175e-29 | 0.988 |
| 3 | 0.933610 | 0.000e+00 | 0.000e+00 | 0.988 |
| 4 | 0.890310 | 4.277e-33 | 7.506e-30 | 0.988 |
| 6 | 0.716497 | 0.000e+00 | 0.000e+00 | 0.988 |
| 12 | 0.000000 | 0.000e+00 | 0.000e+00 | 0.988 |

## Packet Fractions

| condition | H_2 | H_3 | H_4 | H_6 | H_12 |
|---|---:|---:|---:|---:|---:|
| native full month logits | 0.050608 | 0.066390 | 0.059082 | 0.166506 | 0.657415 |
| after C12->C2->C12 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| after C12->C3->C12 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 |
| after C12->C4->C12 | 0.300402 | 0.000000 | 0.699598 | 0.000000 | 0.000000 |
| after C12->C6->C12 | 0.145746 | 0.225871 | 0.000000 | 0.628383 | 0.000000 |
| after C12->C12->C12 | 0.050608 | 0.066390 | 0.059082 | 0.166506 | 0.657415 |

## Reading

Before binning, the native final month-token logits contain energy in all five nontrivial conductor packets; this is the falsifiable model-facing result. After explicit quotient binning and lifting, every packet forbidden by `d not| k` is zero up to numerical floor, but that zero is forced by the bin-and-lift map. The bridge to T2 is that the full native codomain can express the observed packet profile, while a binned quotient codomain discards exactly the packets excluded by its annihilator.

This is a final-layer native logit-lens experiment, not a trained tuned lens across intermediate layers.  The remaining tuned-lens version would train layerwise affine translators to full vocabulary or month-token scores, then repeat this before/after quotient-binning packet score.
