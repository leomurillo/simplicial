# Bigram-confound control — months, Llama-3.1-8B-months-c4-10M

**Corpus:** HuggingFace streaming dataset: allenai/c4 (config=en, split=train, max_docs=100000, max_tokens=10000000)
**Documents scanned:** 27548
**Whitespace tokens scanned:** 10000000
**Unigram counts:** january=1290, february=1058, march=1416, april=1489, may=12523, june=1313, july=1293, august=1052, september=1148, october=1265, november=1100, december=1031

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
| 1 | transposed | 0.258 | 15/23 (0.652) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 3 | transposed | 0.359 | 35/60 (0.583) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 5 | transposed | 0.320 | 38/65 (0.585) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |
| 10 | transposed | 0.301 | 42/65 (0.646) | INTERMEDIATE — rephrase manuscript §4.1 as 'consistent with both'. |

## Per-window statistics — full

| window | offdiag r same (raw) | offdiag r trans (raw) | offdiag r same (cond) | offdiag r trans (cond) | asymm r same | asymm r trans | sign same | sign trans |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.200 | 0.389 | 0.164 | 0.331 | -0.258 | 0.258 | 8/23 | 15/23 |
| 3 | 0.159 | 0.414 | 0.112 | 0.417 | -0.359 | 0.359 | 25/60 | 35/60 |
| 5 | 0.225 | 0.446 | 0.177 | 0.432 | -0.320 | 0.320 | 27/65 | 38/65 |
| 10 | 0.276 | 0.464 | 0.232 | 0.443 | -0.301 | 0.301 | 23/65 | 42/65 |

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
- conductor 2: 0.0867
- conductor 3: 0.1709
- conductor 4: 0.1746
- conductor 6 (mixed): 0.1899
- conductor 12: 0.3779

**Corpus h_i conductor energy fractions (window=1):**
- trivial (k=0): 0.0000
- conductor 2: 0.0877
- conductor 3: 0.1607
- conductor 4: 0.1496
- conductor 6 (mixed): 0.1821
- conductor 12: 0.4199

**Corpus h_i conductor energy fractions (window=3):**
- trivial (k=0): 0.0000
- conductor 2: 0.0868
- conductor 3: 0.1074
- conductor 4: 0.1494
- conductor 6 (mixed): 0.1935
- conductor 12: 0.4629

**Corpus h_i conductor energy fractions (window=5):**
- trivial (k=0): 0.0000
- conductor 2: 0.1017
- conductor 3: 0.1056
- conductor 4: 0.1334
- conductor 6 (mixed): 0.1640
- conductor 12: 0.4953

**Corpus h_i conductor energy fractions (window=10):**
- trivial (k=0): 0.0000
- conductor 2: 0.1267
- conductor 3: 0.1251
- conductor 4: 0.1220
- conductor 6 (mixed): 0.1366
- conductor 12: 0.4896

## Centroid matrix

| | january | february | march | april | may | june | july | august | september | october | november | december |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| january | 0.6675 | 0.0368 | 0.0624 | 0.0072 | 0.0051 | 0.0046 | 0.0262 | 0.0048 | 0.0078 | 0.0091 | 0.0194 | 0.1491 |
| february | 0.0271 | 0.9124 | 0.0168 | 0.0121 | 0.0022 | 0.0014 | 0.0036 | 0.0044 | 0.0033 | 0.0082 | 0.0027 | 0.0058 |
| march | 0.0074 | 0.0314 | 0.9190 | 0.0171 | 0.0092 | 0.0015 | 0.0018 | 0.0027 | 0.0033 | 0.0022 | 0.0023 | 0.0023 |
| april | 0.0047 | 0.0204 | 0.1127 | 0.7662 | 0.0482 | 0.0249 | 0.0046 | 0.0026 | 0.0047 | 0.0060 | 0.0019 | 0.0032 |
| may | 0.0026 | 0.0036 | 0.0307 | 0.0269 | 0.8624 | 0.0271 | 0.0378 | 0.0025 | 0.0017 | 0.0015 | 0.0019 | 0.0014 |
| june | 0.0014 | 0.0028 | 0.0045 | 0.0086 | 0.0242 | 0.9081 | 0.0173 | 0.0270 | 0.0018 | 0.0014 | 0.0009 | 0.0020 |
| july | 0.0020 | 0.0018 | 0.0035 | 0.0049 | 0.0107 | 0.0192 | 0.9159 | 0.0148 | 0.0221 | 0.0018 | 0.0014 | 0.0022 |
| august | 0.0017 | 0.0027 | 0.0019 | 0.0028 | 0.0055 | 0.0074 | 0.0167 | 0.9438 | 0.0098 | 0.0047 | 0.0013 | 0.0017 |
| september | 0.0010 | 0.0018 | 0.0032 | 0.0015 | 0.0042 | 0.0043 | 0.0051 | 0.0194 | 0.9457 | 0.0080 | 0.0039 | 0.0020 |
| october | 0.0019 | 0.0019 | 0.0025 | 0.0014 | 0.0032 | 0.0057 | 0.0067 | 0.0106 | 0.0259 | 0.9230 | 0.0089 | 0.0081 |
| november | 0.0037 | 0.0016 | 0.0020 | 0.0020 | 0.0024 | 0.0050 | 0.0048 | 0.0036 | 0.0044 | 0.0107 | 0.9514 | 0.0084 |
| december | 0.0083 | 0.0086 | 0.0020 | 0.0022 | 0.0018 | 0.0037 | 0.0027 | 0.0022 | 0.0031 | 0.0067 | 0.0475 | 0.9112 |

## Corpus co-occurrence matrix (window=3)

| | january | february | march | april | may | june | july | august | september | october | november | december |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| january | 0 | 17 | 11 | 7 | 6 | 6 | 4 | 2 | 3 | 0 | 1 | 5 |
| february | 3 | 0 | 11 | 7 | 8 | 4 | 3 | 1 | 1 | 3 | 0 | 0 |
| march | 1 | 3 | 0 | 26 | 13 | 8 | 1 | 3 | 1 | 2 | 2 | 1 |
| april | 3 | 0 | 1 | 0 | 19 | 6 | 3 | 0 | 2 | 10 | 2 | 2 |
| may | 3 | 4 | 1 | 2 | 0 | 26 | 6 | 6 | 7 | 6 | 4 | 2 |
| june | 3 | 0 | 0 | 1 | 0 | 0 | 15 | 6 | 15 | 6 | 4 | 3 |
| july | 1 | 1 | 2 | 2 | 0 | 5 | 0 | 24 | 11 | 6 | 1 | 5 |
| august | 3 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 14 | 2 | 4 | 2 |
| september | 1 | 1 | 0 | 2 | 8 | 2 | 1 | 1 | 0 | 20 | 8 | 3 |
| october | 0 | 0 | 4 | 2 | 4 | 3 | 2 | 0 | 2 | 0 | 19 | 10 |
| november | 11 | 4 | 7 | 5 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 18 |
| december | 11 | 2 | 4 | 2 | 4 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
