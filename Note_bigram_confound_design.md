# Bigram-Confound Control for Centroid Asymmetric Leakage

**Status:** design note, May 2026
**Targets:** §4.1 weekday centroids; §5.1 month centroids; §11 launch pitch.
**Defends against:** the "linguistic-bigram" alternative explanation of the
asymmetric off-diagonal leakage observed in the Llama-3.1-8B and Mistral-7B-v0.3
centroid matrices — i.e. the claim that *every weekday leaks more probability
to its cyclic predecessor than to its successor* is a frequency artifact of
pretraining text, not a finite arithmetic carry phenomenon.

**Post-run addendum, May 14, 2026:** the registered `allenai/c4` English run
has been completed on a 10,000,000-token sample.  All three available centroid
files (Llama weekdays, Mistral weekdays, Llama months) land in the
pre-registered **intermediate** band.  See
`empirical/reports/bigram_corpus_control_c4_10M_summary.md` and the three
per-target C4 reports.

## 1. What the manuscript currently asserts

From [§4.1](single-discrete_fisher_skeletons_for_ai_optimization.md:680):

> Both centroid matrices are visibly **asymmetric**: every weekday leaks
> substantially more probability to its cyclic predecessor than to its
> cyclic successor on Mistral … This asymmetry breaks the dihedral symmetry
> assumed by the symmetric proxy and reproduces across both models — it is a
> real off-centroid arithmetic feature, not a single-model artifact. It is
> precisely the kind of finite carry datum that $K^{CH}$ on the empirical
> $h$ records but a linear summary in moment coordinates flattens.

The text "real off-centroid arithmetic feature" is the load-bearing claim. The
reviewer's challenge:

> "Sunday to Monday" is a highly frequent phrase (the weekend transition), and
> lists often start on Monday and end on Sunday. The model's behavior might be
> reflecting linguistic bigram frequencies or tokenizer boundaries rather than
> intrinsic $K^{CH}$ cubic curvature.

## 2. Scope: what the bigram test does and does not adjudicate

This control is narrowly targeted. It is **not** a global referendum on the
$K^{CH}$ thesis. The full claim partition:

| Claim | Bigram test relevance |
|---|---|
| Moment-Euclidean correlation drops while Hellinger/Fisher hold | **Not adjudicated.** Independent of which off-diagonal direction the leakage takes. |
| CRT conductor energy spreads across $\{2,3,4,6,12\}$ on months (§5.1) | **Not adjudicated.** A pretraining-prior explanation of *direction* does not produce conductor-6 energy. |
| $\|K^{CH}_{p_*}(h_i)\|_F$ tracks self-confidence | **Not adjudicated.** Norm is rotation-invariant; direction-confound doesn't touch it. |
| "Predecessor-bias asymmetry is a finite arithmetic carry feature" | **Directly adjudicated.** This is the claim under test. |
| Activation pullback near-isometry on $C_7$ (§7.2.1) | **Not adjudicated.** Independent measurement. |

The honest interpretation matrix:

- **Bigrams fully explain asymmetry direction:** retract the "arithmetic carry"
  framing of the asymmetric-leakage paragraph in §4.1 and §11. The $K^{CH}$
  conductor decomposition argument and the moment-vs-Hellinger correlation
  drop survive untouched.
- **Bigrams partially explain (e.g. $r \le 0.5$):** rephrase as "consistent
  with both pretraining priors and off-centroid arithmetic; the residual
  asymmetry beyond the bigram prediction is what $K^{CH}$ records."
- **Bigrams do not explain (e.g. $r \le 0.2$):** the current §4.1 framing
  stands; add the control as positive evidence.

## 3. Test design

### 3.1 Quantities to compare

Define, for each row $i$ (correct-answer class) and column $j \ne i$ (output
day):

- **Empirical leakage:** $L_{ij} = \text{centroid}[i][j]$
- **Empirical asymmetry:** $A_{ij} = L_{ij} - L_{ji}$ (skew-symmetric, $A_{ii}=0$)
- **Corpus co-occurrence:** $C^{(w)}_{ij}$ = count of "$d_j$ appears within $w$
  tokens after $d_i$" in a public corpus
- **Corpus asymmetry:** $\Delta^{(w)}_{ij} = C^{(w)}_{ij} - C^{(w)}_{ji}$

The headline statistic is the Pearson correlation between the upper-triangular
entries of $A$ and $\Delta^{(w)}$, separately for $w \in \{1, 3, 5, 10\}$.

### 3.2 Corpus choice

Llama-3.1 and Mistral-7B were trained on large web crawls dominated by
FineWeb / RedPajama / C4 style sources. The closest publicly-available proxy
is the C4 English crawl, accessible via the HuggingFace `datasets` library
(`allenai/c4`, `en` subset). A sample of $10^7$–$10^8$ tokens is sufficient to
estimate the $7 \times 7$ (or $12 \times 12$) co-occurrence matrices to a few
percent relative precision.

Secondary corpora useful as triangulation:
- **Project Gutenberg sample** (older, literary distribution — should show
  *less* "Sunday Monday weekend transition" bias if the bigram explanation is
  primarily contemporary-web in origin)
- **English Wikipedia dump** (different register; useful sanity check)

### 3.3 Tokenization

Two tokenization regimes; report both:

1. **Lowercase whitespace tokenization** of day/month names. Robust to BPE
   variants. Closest to what a human reader thinks of as a "bigram."
2. **Native model tokenizer** (HuggingFace `AutoTokenizer` for each model).
   Closer to what the model actually saw. Token boundaries for " Monday"
   vs "Monday" matter here.

The two should agree qualitatively; disagreement is itself informative.

### 3.4 Window sizes

- $w = 1$: strict adjacency (the literal "bigram" reviewer named).
- $w = 3$: catches "Sunday, then Monday", "Sunday → Monday", "from Sunday to
  Monday".
- $w = 10$: catches sentence-level co-mention.

The predecessor-bias hypothesis should appear most strongly at $w=1$ or $w=3$.
A signal that only appears at $w=10$ is closer to topical co-mention than to a
sequential prior.

### 3.5 Controls within the test

- **Self-counts $C_{ii}$:** discarded (they swamp; we only care about
  off-diagonal asymmetry).
- **Frequency normalization:** report both raw $C_{ij}$ and the conditional
  $P(d_j \mid d_i, w) = C^{(w)}_{ij} / \sum_k C^{(w)}_{ik}$. The conditional
  controls for the marginal frequency of each day name (Sunday and Friday are
  more frequent unigrams than Tuesday, which would push naive raw counts).
- **Direction of asymmetry:** report the sign agreement rate
  $\#\{(i,j): \operatorname{sgn} A_{ij} = \operatorname{sgn} \Delta_{ij}\} /
   \binom{N}{2}$. With $N=7$ there are 21 off-diagonal pairs; this is a
  more interpretable summary than Pearson alone.

## 4. Predictions

The cubic-diagnostic theory makes no prediction about the *sign* of
predecessor-bias on the $C_7$ row. At the uniform centroid, the $C_7$
character algebra is rotationally symmetric; the observed direction of
asymmetry is a function of the empirical $h_i$, which is itself a function of
pretraining. Therefore:

- The theory is **agnostic** about the bigram-correlation result on $C_7$.
- The theory *would* be **embarrassed** by a result where the empirical
  predecessor-bias direction agrees almost perfectly with corpus bigram
  asymmetry direction (sign agreement $\ge 18/21$) *and* the Pearson
  correlation between magnitudes is $\ge 0.7$. In that regime, "real
  off-centroid arithmetic feature" overclaims.
- The theory is **strengthened** by a result where sign agreement is near
  chance ($\sim 10/21$–$13/21$) and the magnitude correlation is low.

## 5. Stretch test: months and the CRT prediction

On $C_{12}$ the theory makes a sharper subsidiary prediction. The
conductor-3 (tame) packet $\{4, 8\} \subset \mathbb{Z}/12$ and the
conductor-4 (2-primary) packet $\{3, 6, 9\}$ are predicted to decouple under
CRT at every Taylor order on displacements supported in one primary block
([§5 CRT isolation prediction](single-discrete_fisher_skeletons_for_ai_optimization.md:772)).

A corpus bigram model is not factored through any number-theoretic CRT
decomposition — it just records linguistic adjacency. So a bigram-driven
asymmetry pattern would *not* preferentially align the off-diagonal residual
with the conductor-6 mixed packet that §5.1 finds carries 19.2% of the
empirical energy.

Concretely: project both the empirical centroid displacements $h_i$ and the
corpus bigram asymmetry vectors onto the conductor packets. If the bigram
asymmetry has roughly uniform energy across conductors while the empirical
$h_i$ concentrates on conductor 6 (and 12), that is structural evidence the
network is doing something the corpus prior is not.

## 6. Per-example decomposition (follow-up)

A second, sharper test uses the `per_example_output_dists.safetensors` file
([weekdays/output_manifold/](weekdays/output_manifold)). For each prompt
producing result class $r$, the prompt mentions a specific base day $b$ and
an offset $k = (r - b) \bmod 7$. Decompose the centroid:

$$
L_{rj} = \frac{1}{|S_r|} \sum_{p \in S_r} P(\text{output}=j \mid p)
$$

into contributions stratified by $k$. The *base-stickiness* hypothesis
predicts that leakage to day $j$ is concentrated in prompts where $b = j$
(i.e. the model copied the base). The arithmetic predecessor-bias hypothesis
predicts the leakage is roughly uniform across base-day strata.

This decomposition does not require any external corpus; it can be run
directly on the existing safetensors.

## 7. Deliverables

1. `empirical/bigram_corpus_control.py` — the analysis script.
   Inputs: a corpus iterator (lines of text); the centroid safetensors.
   Outputs: a markdown report with Pearson, sign-agreement, and conductor
   projection statistics, for both weekdays and months.
2. `empirical/reports/bigram_corpus_control.md` — generated report.
3. A short addendum to §4.1 of the manuscript reporting the outcome and the
   interpretive consequences from §2 of this note.

## 8. Falsifiability checklist

Before running the corpus pass, register the following in the report header:

- Pre-registered Pearson threshold for "bigrams fully explain": $r \ge 0.7$
  with sign agreement $\ge 18/21$ on $C_7$.
- Pre-registered Pearson threshold for "bigrams do not explain": $r \le 0.2$
  with sign agreement $\le 13/21$.
- Pre-registered intermediate band: anything else; the manuscript paragraph
  will be rephrased as "consistent with both" rather than "arithmetic carry."

This pre-registration prevents post-hoc reinterpretation of the result.
