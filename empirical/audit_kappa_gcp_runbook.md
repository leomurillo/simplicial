# Runbook: closing the deferred LLM validation block (audit κ and successors) on GCP

Created 2026-06-12 (OpenProblemsSurvey Sharp-2 follow-up). Precedents: the E11 recipe
(transient instance → scp → venv → run → retrieve JSON → delete; see
`ConductorBlindSpot/empirical/apex_recovery/reports/e11_trained_two_encoder.json`
`_environment` note) and `e6_grokking_gcp_runbook.md`. Standing rule: torch/transformers
NEVER run locally (feedback_torch_gcp_only); scripts are written and staged locally,
executed on GCP, JSON/reports retrieved, instance deleted.

## What this closes

The recorded deferral in
`empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md` §1: the full
layerwise sweep of Paper 36 (audit κ proper, pre-registered P1–P7) was deferred for
environment only — `transformers` not installed, HF checkpoints not downloaded,
CPU-only laptop, only layer-28 PCA-64 months residuals saved. The driver scripts are
written and versioned (`audit_kappa_driver_v0.1_2026_05_20`,
`audit_kappa_lens_v0.1_2026_05_20`). This is provisioning work, not science work.

## Prerequisites (user actions — cannot be done by the agent)

1. **HF gated access**: accept the license / request access for
   `meta-llama/Llama-3.1-8B` (and optionally `mistralai/Mistral-7B-v0.3`) on the
   HuggingFace account; create a read token (`HF_TOKEN`).
2. **GCP project + billing**: the 32-vCPU quota was freed when `rh-jensen-vm` was
   deleted (2026-06-10; snapshot `rh-jensen-vm-backup` preserved — that snapshot is
   the RH box, NOT needed here). GPU quota (1× L4) may need a one-time quota request
   in the chosen region.

## VM recipe

- **Recommended**: `g2-standard-8` (1× NVIDIA L4, 24 GB VRAM) — Llama-3.1-8B in
  bf16/fp16 fits (~16 GB); spot/preemptible is fine (runs are short and resumable).
- **Fallback (no GPU quota)**: high-mem CPU (e.g. `c3-standard-22`); 8B forward passes
  on CPU are slow but the prompt sets are tiny (84 months + 49 weekdays examples), so
  even CPU completes in hours.
- Image: Deep Learning VM (PyTorch, CUDA) or plain Debian 12 + `pip install torch
  transformers safetensors accelerate huggingface_hub` in a venv.
- Stage: `gcloud compute scp` the drivers + task data:
  - `empirical/layerwise_packet_spectroscopy.py` (Paper 36 §8 driver)
  - `empirical/native_logit_lens_packet_score_layerwise.py` (lens arm)
  - the task/prompt assets the drivers reference under `months/` and `weekdays/`
    (`baseline/`, prompt lists; consult each script's input manifest at top of file)
  - for later phases: Paper 39/40/45 drivers as they are finalized.
- `export HF_TOKEN=...` then `huggingface-cli download meta-llama/Llama-3.1-8B`.

## Run order (decisive-first; each phase is independently retrievable)

1. **Audit κ proper** — full layerwise sweep, Llama-3.1-8B, months + weekdays:
   settles pre-registered P1–P7 of Paper 36 (layerwise packet crystallization,
   V/M differential saturation). Outputs: per-layer packet fractions JSON + report.
   This is THE Sharp-2 bridge test: does the conductor-packet picture hold layer-by-
   layer on a frontier model beyond the final-layer anchors already measured.
2. **Cross-model arm** — same driver on Mistral-7B-v0.3 (Paper 36 cross-model
   predictions; cheap once the box is up).
3. **Paper 39 Γ-law protocol** — attention-sink phase under input reversal (forward
   passes only; highest-novelty/highest-risk item, pre-registered).
4. **Paper 40 σ-audit taxonomy extension** — beyond the measured months anchor
   (σ = 0.458) to the seven pre-registered task classes.
5. **Paper 45 CCSAE training** — the only multi-hour GPU phase (SAE training on the
   captured activations; divisor tables months C₁₂ / weekdays C₇ / digits C₁₀).

After each phase: `gcloud compute scp` the JSON/report back into
`empirical/reports/`, update the settlement record (the deferral note in the κ report
is replaced by outcomes, per Paper 35 §3.6 — outcomes recorded whichever way they
fall), and DELETE the instance (E11 pattern).

## Cost envelope

L4 spot ≈ $0.7–1.0/hr. Phases 1–4 are forward-pass-only over ~10² prompts: a day of
wall clock, single-digit dollars. Phase 5 (CCSAE) is the only multi-hour GPU job;
budget separately once dictionary sizes are fixed.

## Explicitly out of scope here

- E11 (IBS trained two-encoder): already DONE and PASSED on GCP 2026-06-02.
- The RH workstation items (μ_210+ memory audit): different machine profile
  (high-RAM CPU), different runbook; snapshot `rh-jensen-vm-backup` restores that box.
