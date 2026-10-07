# Bigram-confound control — weekdays, Llama-3.1-8B-c4-10M

**Corpus:** HuggingFace streaming dataset: allenai/c4 (config=en, split=train, max_docs=100000, max_tokens=10000000)
**Documents scanned:** 27548
**Whitespace tokens scanned:** 10000000
**Unigram counts:** monday=866, tuesday=721, wednesday=636, thursday=783, friday=1259, saturday=1078, sunday=1042

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
| 1 | transposed | 0.500 | 7/13 (0.538) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 3 | transposed | 0.424 | 9/21 (0.429) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 5 | transposed | 0.392 | 9/21 (0.429) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 10 | transposed | 0.438 | 9/20 (0.450) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |

## Per-window statistics — full

| window | offdiag r same (raw) | offdiag r trans (raw) | offdiag r same (cond) | offdiag r trans (cond) | asymm r same | asymm r trans | sign same | sign trans |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.129 | 0.416 | 0.154 | 0.623 | -0.500 | 0.500 | 6/13 | 7/13 |
| 3 | 0.027 | 0.211 | 0.060 | 0.451 | -0.424 | 0.424 | 12/21 | 9/21 |
| 5 | 0.083 | 0.262 | 0.108 | 0.486 | -0.392 | 0.392 | 12/21 | 9/21 |
| 10 | 0.120 | 0.334 | 0.144 | 0.515 | -0.438 | 0.438 | 11/20 | 9/20 |

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

**Corpus h_i conductor energy fractions (window=1):**
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
| monday | 0 | 11 | 11 | 8 | 50 | 15 | 2 |
| tuesday | 0 | 0 | 15 | 7 | 2 | 5 | 4 |
| wednesday | 0 | 0 | 0 | 18 | 9 | 4 | 7 |
| thursday | 1 | 0 | 0 | 0 | 13 | 8 | 7 |
| friday | 8 | 1 | 0 | 3 | 0 | 46 | 10 |
| saturday | 1 | 0 | 1 | 3 | 0 | 0 | 50 |
| sunday | 8 | 2 | 2 | 1 | 3 | 3 | 0 |
