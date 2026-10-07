# C4 10M Bigram-Confound Control Summary

**Corpus:** `allenai/c4`, English config, train split, HuggingFace streaming  
**Sample:** 27,548 documents, 10,000,000 whitespace tokens  
**Run date:** 2026-05-14  
**Centroid files:**
- `weekdays/baseline/per_class_output_dists.safetensors` (Llama-3.1-8B weekdays)
- `per_class_output_dists.safetensors` (Mistral-7B-v0.3 weekdays)
- `months/baseline/per_class_output_dists.safetensors` (Llama-3.1-8B months)

## Verdict

The pre-registered bigram control lands in the **intermediate** band.
Corpus bigrams partially align with the model asymmetry under the transposed
indexing convention, but they do not satisfy the registered "fully explain"
criterion because sign agreement stays far below \(18/21\) on weekdays.

This closes the asymmetry question as follows:

- The predecessor-direction leakage should **not** be described as independent
  evidence of an arithmetic carry signature.
- It should be described as **consistent with both** a learned pretraining
  sequence prior and a residual off-centroid cyclic signal.
- The main empirical support for the cubic diagnostic remains the
  moment-vs-Hellinger/Fisher metric gap, the \(C_{12}\) conductor-energy split,
  and the activation-pullback audit.

## Headline Results

| target | window | alignment | asymm Pearson \(r\) | sign agreement | pre-registered verdict |
|---|---:|---|---:|---:|---|
| Llama weekdays | 1 | transposed | 0.500 | 7/13 (0.538) | intermediate |
| Llama weekdays | 3 | transposed | 0.424 | 9/21 (0.429) | intermediate |
| Llama weekdays | 5 | transposed | 0.392 | 9/21 (0.429) | intermediate |
| Llama weekdays | 10 | transposed | 0.438 | 9/20 (0.450) | intermediate |
| Mistral weekdays | 1 | transposed | 0.820 | 9/13 (0.692) | intermediate |
| Mistral weekdays | 3 | transposed | 0.690 | 10/21 (0.476) | intermediate |
| Mistral weekdays | 5 | transposed | 0.739 | 10/21 (0.476) | intermediate |
| Mistral weekdays | 10 | transposed | 0.816 | 10/20 (0.500) | intermediate |
| Llama months | 1 | transposed | 0.258 | 15/23 (0.652) | intermediate |
| Llama months | 3 | transposed | 0.359 | 35/60 (0.583) | intermediate |
| Llama months | 5 | transposed | 0.320 | 38/65 (0.585) | intermediate |
| Llama months | 10 | transposed | 0.301 | 42/65 (0.646) | intermediate |

## Notes

The registered weekday thresholds were:

- **Fully explain:** \(r \ge 0.70\) and sign agreement \(\ge 18/21\).
- **Do not explain:** \(r \le 0.20\) and sign agreement \(\le 13/21\).
- **Intermediate:** anything else.

Mistral reaches the magnitude threshold at windows 1, 5, and 10, but never the
sign-agreement threshold. Llama never reaches the magnitude threshold. Thus the
corpus explains part of the direction/magnitude pattern but not most of the
weekday asymmetry under the pre-registered joint criterion.

The month conductor-energy comparison is not a falsification threshold, but it
is a useful sanity check. The C4 month corpus also places substantial energy in
conductor 12 and nontrivial energy in conductor 6. That means conductor-energy
fractions alone should not be used as a linguistic-confound dismissal; the
stronger month result remains the metric gap plus the CRT interpretation of the
empirical displacement geometry.
