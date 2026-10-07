# Bigram-confound control — weekdays, Mistral-7B-v0.3-c4-10M

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
| 1 | transposed | 0.820 | 9/13 (0.692) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 3 | transposed | 0.690 | 10/21 (0.476) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 5 | transposed | 0.739 | 10/21 (0.476) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 10 | transposed | 0.816 | 10/20 (0.500) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |

## Per-window statistics — full

| window | offdiag r same (raw) | offdiag r trans (raw) | offdiag r same (cond) | offdiag r trans (cond) | asymm r same | asymm r trans | sign same | sign trans |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | -0.131 | 0.776 | -0.078 | 0.821 | -0.820 | 0.820 | 4/13 | 9/13 |
| 3 | -0.194 | 0.585 | -0.201 | 0.671 | -0.690 | 0.690 | 11/21 | 10/21 |
| 5 | -0.161 | 0.661 | -0.166 | 0.748 | -0.739 | 0.739 | 11/21 | 10/21 |
| 10 | -0.124 | 0.721 | -0.117 | 0.800 | -0.816 | 0.816 | 10/20 | 10/20 |

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
| monday | 0.6649 | 0.0428 | 0.0062 | 0.0050 | 0.0084 | 0.0188 | 0.2538 |
| tuesday | 0.1536 | 0.7742 | 0.0250 | 0.0095 | 0.0058 | 0.0092 | 0.0226 |
| wednesday | 0.0142 | 0.2425 | 0.6915 | 0.0308 | 0.0066 | 0.0037 | 0.0106 |
| thursday | 0.0017 | 0.0057 | 0.0824 | 0.8690 | 0.0311 | 0.0036 | 0.0066 |
| friday | 0.0017 | 0.0011 | 0.0040 | 0.1909 | 0.7818 | 0.0140 | 0.0064 |
| saturday | 0.0053 | 0.0026 | 0.0014 | 0.0075 | 0.2738 | 0.6870 | 0.0224 |
| sunday | 0.0474 | 0.0062 | 0.0030 | 0.0052 | 0.0204 | 0.2841 | 0.6338 |

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
