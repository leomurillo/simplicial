# GCP Experiments — A1 (Compositionality Tax) & A4 (Dark Structure)

Two pre-registered tests from `../FALSIFIABLE_PREDICTIONS_REGISTRY.md`, on real transformer
activations. **GCP-only** (they import torch/transformers, which must never run on the author's
laptop). Guarded: each refuses to run unless `GCP_RUN=1`. The numpy kernel math is laptop-safe and is
self-tested (`py kernel_probe.py`, no torch).

## Files
- `kernel_probe.py` — shared: model load + activation extraction (torch), degree-m polynomial-kernel
  ridge, PCA reduction, CV R²/accuracy (numpy). `selftest_numpy()` validates the phase boundary with no torch.
- `a1_compositionality_tax.py` — A1: order-m probe faithful to order-k behavior iff m≥k (sharp phase
  boundary, τ(k)=k), + the degradation-with-dimension sweep (the practical obstruction).
- `a4_dark_structure.py` — A4: dark:visible = (R²₄−R²₂)/R²₂ of predicting next-token surprisal,
  across layers; dark structure = output-relevant content invisible to order-2.
- `_tune_regime.py` — helper that found the statistically-accessible regime (low d_sub). Documentation.

## Deploy & run (GCP)
```bash
# on a small CPU instance (e2-standard-4 is plenty; both jobs are CPU-bound, minutes each)
python -m venv venv && . venv/bin/activate
pip install -r requirements.txt
pip install torch --index-url https://download.pytorch.org/whl/cpu
export GCP_RUN=1
python kernel_probe.py                  # optional: confirm the numpy phase-boundary selftest PASSes
python a1_compositionality_tax.py       # writes results/a1_compositionality_tax.json
python a4_dark_structure.py             # writes results/a4_dark_structure.json
# retrieve the two JSONs, then delete the instance
```
Default model: `EleutherAI/pythia-410m` (ungated, interp-standard, CPU-fast). Layer indices adapt to
the model's depth automatically. Override via env: `A1_MODEL`, `A1_LAYER`, `A1_NTOK`; `A4_MODEL`,
`A4_LAYERS`, `A4_NTOK`. First run downloads the model + (optionally) wikitext-2. **Gated models**
(e.g. `meta-llama/Llama-3.2-1B`, as used in the κ-audit) also need `export HF_TOKEN=...` and accepting
the license on HF. Ungated models (Pythia, GPT-2) need no token.

## Pre-registered verdicts (set before the data)
**A1 — CONFIRM** iff at d_sub=k+1, for every k∈{2,3,4}: acc(m<k) ≤ 0.65, acc(m≥k) ≥ 0.80, a single
0→1 step with τ(k)=k. **FALSIFY** on a gradient (no sharp step) or τ(k)≠k in the accessible regime.
The degradation sweep additionally reports how the boundary washes out as d_sub grows.

**A4 — CONFIRM** iff, in the accessible regime, dark:visible(L) > 1 at early/mid layers AND decreases
toward the final layer (the output linearizes into the unembedding). **FALSIFY** if order-2 captures
the majority everywhere (dark:visible < 1 at all layers and d_sub). **PARTIAL** if dark dominates but
the depth trend is flat.

## Honesty caveats (carried into any writeup)
- A1's controlled behavior is a parity of real-activation PCA coordinates — a *genuine* order-k
  function of real activation values, tested in the regime where order-k is statistically isolable.
  The boundary's degradation with d_sub is a real second finding (high-order structure becomes
  inaccessible in high dimensions — the obstruction in practice).
- A4's `dark` is a **lower bound**: structure of order > 4, or inaccessible at the chosen d_sub
  (curse of dimensionality), is uncounted. The claim rides the *trend across d_sub and layers*, not a
  single number. If A4 comes back ambiguous, that is itself an honest result about measurability.
- Neither experiment cashes out any dimensionful quantity; both are pure ML / dimensionless.
