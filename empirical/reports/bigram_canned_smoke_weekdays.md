# Bigram-confound control — weekdays, Llama-3.1-8B-canned-tiny

**Corpus:** plaintext file: empirical\_tiny_canned_corpus.txt
**Documents scanned:** 25
**Unigram counts:** monday=18, tuesday=6, wednesday=5, thursday=6, friday=9, saturday=9, sunday=15

**Pre-registered thresholds:**
- Fully explain:  asymm Pearson r >= 0.70 AND sign agreement >= 0.857
- Do not explain: asymm Pearson r <= 0.20 AND sign agreement <= 0.619
- Intermediate: anything else.

## Per-window statistics — headline (max-|r| alignment)

Two alignments are considered for each window:
- **same:** centroid M[i,j] vs corpus M[i,j]
- **transposed:** centroid M[i,j] vs corpus M[j,i]

The headline row reports whichever alignment has larger |asymm r|.
If the reviewer's hypothesis 'pretraining "Sun Mon" bigram explains
Mon→Sun centroid leakage' holds, the transposed alignment will
show high correlation; if same-direction bigrams drive the bias,
the same alignment will. Either is bad for the manuscript claim.

| window | alignment | asymm r | sign agree | verdict |
|---:|---|---:|---:|---|
| 3 | transposed | 0.564 | 6/9 (0.667) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 5 | transposed | 0.787 | 6/9 (0.667) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 10 | transposed | 0.787 | 6/9 (0.667) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |

## Per-window statistics — full

| window | offdiag r same (raw) | offdiag r trans (raw) | offdiag r same (cond) | offdiag r trans (cond) | asymm r same | asymm r trans | sign same | sign trans |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0.237 | 0.618 | 0.242 | 0.688 | -0.564 | 0.564 | 3/9 | 6/9 |
| 5 | 0.164 | 0.805 | 0.242 | 0.710 | -0.787 | 0.787 | 3/9 | 6/9 |
| 10 | 0.205 | 0.816 | 0.289 | 0.726 | -0.787 | 0.787 | 3/9 | 6/9 |

## Conductor-packet energy decomposition (per-row displacements)

Each row i of the centroid (resp. row-normalized corpus matrix)
is a probability distribution p_i on Z/N. The displacement from
uniform h_i = p_i - p_* lives in the zero-sum hyperplane and
decomposes under the additive-character basis. Energy is summed
across rows and across characters within each conductor packet,
then normalized to sum to 1.

This is the §5.1 conductor energy decomposition applied
symmetrically to both the centroid and the corpus co-occurrence.
If the bigram corpus carries the same conductor signature as the
centroid, the two decompositions should agree.

**Centroid h_i conductor energy fractions:**
- trivial (k=0): 0.0000
- conductor 7 (nontrivial): 1.0000

**Corpus h_i conductor energy fractions (window=3):**
- trivial (k=0): 0.0000
- conductor 7 (nontrivial): 1.0000

**Corpus h_i conductor energy fractions (window=5):**
- trivial (k=0): 0.0000
- conductor 7 (nontrivial): 1.0000

**Corpus h_i conductor energy fractions (window=10):**
- trivial (k=0): 0.0000
- conductor 7 (nontrivial): 1.0000

## Centroid matrix

| | monday | tuesday | wednesday | thursday | friday | saturday | sunday |
|---|---|---|---|---|---|---|---|
| monday | 0.6356 | 0.0558 | 0.0089 | 0.0089 | 0.0064 | 0.0136 | 0.2709 |
| tuesday | 0.1155 | 0.7487 | 0.0734 | 0.0151 | 0.0086 | 0.0152 | 0.0234 |
| wednesday | 0.0178 | 0.1100 | 0.7374 | 0.0624 | 0.0264 | 0.0199 | 0.0261 |
| thursday | 0.0154 | 0.0121 | 0.0685 | 0.7732 | 0.0965 | 0.0146 | 0.0196 |
| friday | 0.0079 | 0.0093 | 0.0050 | 0.0704 | 0.8328 | 0.0499 | 0.0247 |
| saturday | 0.0103 | 0.0052 | 0.0051 | 0.0044 | 0.1440 | 0.7477 | 0.0833 |
| sunday | 0.0283 | 0.0088 | 0.0034 | 0.0079 | 0.0043 | 0.0506 | 0.8967 |

## Corpus co-occurrence matrix (window=3)

| | monday | tuesday | wednesday | thursday | friday | saturday | sunday |
|---|---|---|---|---|---|---|---|
| monday | 0 | 4 | 0 | 0 | 3 | 0 | 0 |
| tuesday | 1 | 0 | 3 | 1 | 0 | 0 | 0 |
| wednesday | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| thursday | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| friday | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| saturday | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| sunday | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
