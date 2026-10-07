# Layerwise packet spectroscopy -- weekdays on Mistral-7B-v0.3 (audit kappa, lens arm)

**Run date:** 2026-06-12 (GCP, NVIDIA L4, transformers 4.57.6, torch 2.9.1+cu129).
**Driver:** `audit_kappa_driver_v0.2_2026_06_12`; **scorer:** `audit_kappa_lens_v0.1_2026_05_20` (`--mode layerwise`).
**Prompts:** `weekdays/baseline/train_samples.json` (49 examples; the exact Paper 26 baseline prompt set).
**V_R token ids (cyclic 0..N-1 order):** `[10030, 11955, 12231, 11751, 8853, 9281, 8497]` (single-token identity asserted against the tokenizer).
**Residual capture:** BF16 last-token, all 33 hidden_states rows; row 0 = embeddings, row k = output of decoder block k-1, row 32 = post-final-norm (feeds W_U).
**Layer-index convention:** the Goodfire/causalab artifact 'L28_last_token' corresponds to row 29 here (verified, months/Llama: cosine 0.9998 per-example vs saved raw_features; lens f_12 agrees to ~6e-5).

| row | f_7 |
|---:|---:|
| 0 | 1.000000 |
| 1 | 1.000000 |
| 2 | 1.000000 |
| 3 | 1.000000 |
| 4 | 1.000000 |
| 5 | 1.000000 |
| 6 | 1.000000 |
| 7 | 1.000000 |
| 8 | 1.000000 |
| 9 | 1.000000 |
| 10 | 1.000000 |
| 11 | 1.000000 |
| 12 | 1.000000 |
| 13 | 1.000000 |
| 14 | 1.000000 |
| 15 | 1.000000 |
| 16 | 1.000000 |
| 17 | 1.000000 |
| 18 | 1.000000 |
| 19 | 1.000000 |
| 20 | 1.000000 |
| 21 | 1.000000 |
| 22 | 1.000000 |
| 23 | 1.000000 |
| 24 | 1.000000 |
| 25 | 1.000000 |
| 26 | 1.000000 |
| 27 | 1.000000 |
| 28 | 1.000000 |
| 29 | 1.000000 |
| 30 | 1.000000 |
| 31 | 1.000000 |
| 32 | 1.000000 |

f_7 = 1.0 identically at every row: on the prime modulus Z/7 the only nontrivial packet is H_7, so the nontrivial-energy fraction is 1 by construction at every layer. No spurious off-divisor structure can appear at this metric level (Paper 36 P10 K-branch; P4 ramp is not measurable in the fraction normalization).
