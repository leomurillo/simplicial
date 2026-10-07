# vec2vec residual order-spectroscopy — the Conductor Blind Spot, measured in the wild

**Probe:** `empirical/probe_vec2vec_residual_conductor.py` (numpy gate, validated)
**Extractor (GCP):** `empirical/_gcp_dump_arrays.py` → `dump_arrays.py` on `rh-jensen-vm`
**Date:** 2026-06-17 · **Status:** GREEN, **CBS-POSITIVE**

## What was run

Real **vec2vec** (Jha, Zhang, Shmatikov & Morris, arXiv:2505.12540), the paper's
flagship cross-architecture pair, using **their released v1.0.0 checkpoint**
`gte_gtr` (source `gte`, BERT-based → target `gtr`, T5-based; `style=res_mlp`,
`d_adapter=1024`, VSP loss weight 1.0, trained on 1M NQ points). On GCP
(`c3-standard-22`, CPU) we embedded **N=20,000** streamed NQ passages
(`jxm/nq_corpus_dpr`, `max_seq_length=64`) with both encoders and applied the
trained translator `F: gte→gtr` (`translate_embeddings`), dumping paired
`U=gte(x)`, `V=gtr(x)`, `VHAT=F(gte(x))` (each 20000×768). `load_state_dict`:
**0 missing / 0 unexpected** keys. Paired translation cosine **0.753** (in the
range their tables report for this pair).

The diagnostic reads the residual by **cumulant order** (the C2/C3 cumulant-tower
bridge, the rigorous continuous analogue of the discrete Z/n Conductor Blind
Spot — embeddings carry no ring on their axes).

## Result

**Isotropic (random-direction) spectroscopy is near-vacuous** — and that is itself
the first finding: random 1-D shadows of normalized embeddings are Gaussianized
by concentration of measure (target raw |κ₃|≈6.4e-7; standardized skew ≈0.014 ≈
the N=20k sampling floor 0.017). The higher-order structure is **anisotropic** —
it lives in a low-dimensional structured subspace, not in generic directions.

**Structured (top-k target-PC) spectroscopy** — where variance and any semantic
non-Gaussianity concentrate — is decisive. Reproduction error of vec2vec by order:

| k (PCs) | var (O2) | skew (O3) | kurt (O4) | tgt skew/floor | tgt kurt/floor |
|--------:|---------:|----------:|----------:|---------------:|---------------:|
| 8   | 0.047 | 0.364 | 0.160 | 8.3× | 11.3× |
| 16  | 0.038 | 0.329 | 0.260 | 10.4× | 11.5× |
| 32  | 0.034 | 0.418 | 0.362 | 8.0× | 8.5× |
| 64  | 0.032 | 0.513 | 0.499 | 6.0× | 6.1× |
| 128 | 0.039 | 0.676 | 0.614 | 4.5× | 4.5× |
| 256 | 0.080 | 1.082 | 0.438 | 3.4× | 4.8× |

The target's non-Gaussianity is **real at every k** (3.4–11.5× the sampling
floor). Across k=8…256, vec2vec reproduces **order-2 to 3–8%** but **order-3 to
33–108%** — an **8–14× gap at every scale**. Stable, not a knob artifact.

**Identity baseline (the clincher).** Raw `gte` vs `gtr` with no translation
(top-64 PCs): var 0.912, skew 1.196, kurt 1.166 — ~100%+ wrong at every order
(the spaces are genuinely incomparable; vec2vec's job is real). vec2vec closes
the gap **asymmetrically**:

| order | identity (no translation) | vec2vec | improvement |
|------|--------------------------:|--------:|------------:|
| O2 (variance) | 0.912 | 0.032 | **30×** |
| O3 (skew)     | 1.196 | 0.513 | 2.3× |
| O4 (kurt)     | 1.166 | 0.499 | 2.3× |

The method pours essentially all its capacity into matching second order (30×)
and barely moves third/fourth (2.3×). That asymmetry *is* the Conductor Blind
Spot: an order-2 training signal (VSP = preserve the Gram / inner-product
distribution; cosine) is structurally blind to the order-≥3 content — even when,
as here, that content demonstrably exists.

## Verdict

**CBS-POSITIVE, in the structured subspace.** This converts vec2vec's
self-described "lower bound" hedge into a **named order-2 floor**: the residual
(cosine 0.75, not 1.0) is not mere optimization slack — it is the order-≥3
structure that an order-2 objective cannot transport. A deployed,
security-relevant system is a clean in-the-wild instance of the second-order
blind spot (FaithfulnessObstruction §8; OpenProblemsSurvey C1/C2;
[[reference_vec2vec_2505_12540]]).

**Honest nuance / scope.**
- The higher-order structure is **anisotropic** (invisible to random slicing,
  6× the floor along PCs). This is itself consistent with the LeJEPA/order-2
  picture: most *isotropic* content is order-2; the *discriminative* higher-order
  content is concentrated and is exactly what is lost.
- One encoder pair (`gte→gtr`), one corpus (NQ), in-distribution text (the
  conservative choice: best-case order-2 fidelity, so the order-3 deficit is
  structural, not a train/test-gap artifact), `max_seq_length=64`. Generalizing
  across pairs/corpora is the obvious next sweep.
- The bridge to the discrete Conductor Blind Spot is via C2/C3 (cumulant tower),
  not the literal Z/n packet predicate.

## Validation

The diagnostic's synthetic matched-pair gate (`python
probe_vec2vec_residual_conductor.py`, no args) PASSES: an order-2-faithful
Gaussianizing translator K (g₃=0.020, ladder D3/D2=203) vs a structureless
control L (g₃=1.001, flat) — confirming the readout is order-selective, not
noise-sensitive, before it was trusted on real data.
