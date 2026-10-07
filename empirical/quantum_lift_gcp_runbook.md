# Quantum-Lift Audit GCP Runbook

This runbook executes the mod-6 transformer audit implemented in
`empirical/quantum_lift_audit.py`.

## What The Experiment Measures

Task: exhaustive synthetic addition in `Z/6Z`.

Model targets:

- `meta-llama/Llama-3.1-8B`
- `mistralai/Mistral-7B-v0.3`

Layer targets: decoder layers `28,29,30,31`, captured at the last prompt token.

Primary measurement:

- build six-bin next-token answer distributions over digits `0..5`;
- project final residual activations into the six answer-readout directions;
- construct an empirical density matrix with softmax diagonal and covariance
  off-diagonal terms;
- apply matched-amplitude Cartan and CRT-local off-diagonal rotations;
- report the post-measurement squash ratio:

```text
post Hellinger distance after LayerNorm + lm_head + Softmax
----------------------------------------------------------
pre intervention chord distance in the six-residue readout subspace
```

Lower ratio means more hidden-space motion is lost at the classical output
simplex.

## Current GCP Hardware Choice

Recommended first pass: one `g2-standard-8` VM.

Reason: Google Cloud's current Compute Engine GPU docs list G2 machines as
NVIDIA L4 instances, with `g2-standard-8` providing 1 L4 GPU and 24 GB GPU
memory. The same docs list A2 `a2-highgpu-1g` as 1 A100 40 GB. G2/L4 is the
right cost/performance default for this inference audit; A100 is the faster
fallback if L4 capacity is unavailable or if exact suffix reinjection is added.

Official docs checked on 2026-05-14:

- GPU machine types: https://docs.cloud.google.com/compute/docs/gpus
- Deep Learning VM images: https://cloud.google.com/deep-learning-vm/docs/images
- GPU pricing overview: https://cloud.google.com/compute/gpus-pricing

## Runtime Estimate

The fast final-lens audit forwards each prompt once, then evaluates rotations
through final LayerNorm and `lm_head`.

| Run | Prompts | Hardware | Expected wall time after deps/model cache |
|---|---:|---|---:|
| Smoke | 36 to 72 | CPU or tiny GPU | 2 to 10 min |
| One model, fast audit | 216 | 1x L4 24 GB | 20 to 45 min |
| Both models, fast audit | 432 total | 1x L4 24 GB | 45 to 90 min |
| One model, fast audit | 216 | 1x A100 40 GB | 8 to 20 min |
| Both models, fast audit | 432 total | 1x A100 40 GB | 20 to 45 min |

Add 15 to 45 minutes on the first run for VM setup and model downloads,
depending on disk/network/cache state.

The `--exact-suffix` follow-up is much heavier because it reruns downstream
transformer layers per intervention. Budget roughly 2 to 5 hours per model on
L4, or 40 to 100 minutes per model on A100, before tuning.

## VM Setup

Use a Deep Learning VM GPU image so CUDA, PyTorch, and NVIDIA drivers are not a
side quest. If the newer PyTorch/CUDA image family is available in the project,
this concrete command is the preferred launch path:

```bash
gcloud compute instances create causalab-vm \
  --project=causalab-llama \
  --zone=us-east4-c \
  --machine-type=g2-standard-8 \
  --image-family=pytorch-2-9-cu129-ubuntu-2204-nvidia-580 \
  --image-project=deeplearning-platform-release \
  --boot-disk-size=200GB \
  --accelerator=type=nvidia-l4,count=1 \
  --maintenance-policy=TERMINATE \
  --metadata=install-nvidia-driver=True
```

If GCP rejects the accelerator flag on `g2-standard-8`, remove
`--accelerator=type=nvidia-l4,count=1`; G2 machine types already have fixed L4
GPUs attached. Official public docs checked on 2026-05-14 list
`pytorch-2-7-cu128-ubuntu-2204-nvidia-570` as the current documented PyTorch GPU
image family, so use it as the conservative fallback if the `2-9/cu129/580`
family is not visible in the project.

Example variables:

```bash
export PROJECT_ID="your-project"
export ZONE="us-central1-a"
export INSTANCE="qlift-l4"
export IMAGE_FAMILY="pytorch-2-7-cu128-ubuntu-2204-nvidia-570"
```

Example creation command:

```bash
gcloud compute instances create "$INSTANCE" \
  --project="$PROJECT_ID" \
  --zone="$ZONE" \
  --machine-type="g2-standard-8" \
  --image-family="$IMAGE_FAMILY" \
  --image-project="deeplearning-platform-release" \
  --boot-disk-size="200GB" \
  --maintenance-policy="TERMINATE"
```

If that zone lacks L4 quota/capacity, switch zone or use A100:

```bash
gcloud compute instances create "qlift-a100" \
  --project="$PROJECT_ID" \
  --zone="$ZONE" \
  --machine-type="a2-highgpu-1g" \
  --image-family="$IMAGE_FAMILY" \
  --image-project="deeplearning-platform-release" \
  --boot-disk-size="250GB" \
  --maintenance-policy="TERMINATE"
```

After SSH:

```bash
nvidia-smi
python -m pip install -U "transformers>=4.45" accelerate safetensors scipy
huggingface-cli login
```

Llama access may require accepting the model license and using a Hugging Face
token with access to `meta-llama/Llama-3.1-8B`.

## Code Transfer

From this workspace, copy or push the repository to the VM. Minimal paths are:

```text
empirical/quantum_lift_audit.py
empirical/data/mod6_addition_probe_manifest.json
```

The manifest can also be regenerated on the VM:

```bash
python empirical/quantum_lift_audit.py --write-manifest --templates 6
```

## Commands

Fast Llama pass:

```bash
python empirical/quantum_lift_audit.py \
  --model meta-llama/Llama-3.1-8B \
  --layers 28,29,30,31 \
  --theta 0.02,0.05,0.1 \
  --dtype bfloat16 \
  --device cuda \
  --progress \
  --report empirical/reports/quantum_lift_audit_llama31_8b.md
```

Fast Mistral pass:

```bash
python empirical/quantum_lift_audit.py \
  --model mistralai/Mistral-7B-v0.3 \
  --layers 28,29,30,31 \
  --theta 0.02,0.05,0.1 \
  --dtype bfloat16 \
  --device cuda \
  --progress \
  --report empirical/reports/quantum_lift_audit_mistral_7b_v0_3.md
```

If a 24 GB L4 is tight, use 4-bit loading:

```bash
python -m pip install -U bitsandbytes
python empirical/quantum_lift_audit.py \
  --model meta-llama/Llama-3.1-8B \
  --layers 28,29,30,31 \
  --theta 0.02,0.05,0.1 \
  --dtype bfloat16 \
  --device-map auto \
  --load-in-4bit \
  --progress \
  --report empirical/reports/quantum_lift_audit_llama31_8b_4bit.md
```

## Smoke Test Before Spending The Full Run

Use fewer prompts:

```bash
python empirical/quantum_lift_audit.py \
  --model meta-llama/Llama-3.1-8B \
  --limit 36 \
  --layers 31 \
  --theta 0.05 \
  --dtype bfloat16 \
  --device cuda \
  --progress \
  --report empirical/reports/quantum_lift_smoke.md
```

Expected smoke-test output:

- JSON artifact in `empirical/quantum_lift/`;
- Markdown report in `empirical/reports/`;
- nonzero baseline six-bin probabilities for every digit;
- no rank-deficiency error from the six answer readout directions.

## Exact Suffix Follow-Up

Run this only after the fast audit produces a sensible report. Start with one
layer and one angle:

```bash
python empirical/quantum_lift_audit.py \
  --model meta-llama/Llama-3.1-8B \
  --limit 72 \
  --layers 30 \
  --theta 0.05 \
  --dtype bfloat16 \
  --device cuda \
  --exact-suffix \
  --progress \
  --report empirical/reports/quantum_lift_exact_suffix_smoke.md
```

Then scale to all prompts/layers only if the smoke result is stable.

## Decision Rule

Primary support pattern:

- Cartan family has stable, nonzero post/pre ratio across theta.
- `nonabelian_su2` and `nonabelian_su3` have lower mean squash ratios than
  `cartan` on the same layer and theta.
- A strong positive result is nonabelian/cartan ratio below `0.5` with
  bootstrap intervals that do not overlap much.
- Density coherence is meaningful only if `offdiag/diag Frobenius` survives a
  follow-up shuffled-label or random-generator control.

Null result:

- nonabelian and Cartan squash ratios are indistinguishable;
- off-diagonal density energy collapses to the PSD floor;
- the model is not competent on mod-6 addition, making the task unsuitable.

## Follow-Up Controls

Run these if the first pass is promising:

- shuffled result labels before density construction;
- random skew generators in the same six-dimensional readout subspace;
- prompts with subtraction and multiplication mod 6;
- exact suffix reinjection for layers 28-30;
- repeat with instruction/chat templates versus plain prompts.
