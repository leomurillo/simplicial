# Llama 3.1 8B Weekday Centroids Blocker Report

Run timestamp: 2026-05-11T21:49:34-06:00.

## Outcome

No empirical 7x7 weekday centroid matrix was produced. The run is blocked before
logit collection: this workspace does not currently have a Llama 3.1 8B model,
an inference runtime capable of exposing next-token logits, the required Python
packages, or Hugging Face credentials for gated Llama weights.

Per the session prompt, no centroid JSON or K_CH empirical report was fabricated.
The existing parametric files remain separate:

- `empirical/reports/weekdays_K_CH_prediction.md`
- `empirical/reports/weekdays_K_CH_prediction.json`

## Local Checks

Commands/runtime availability:

- `nvidia-smi.exe` is available at `C:\windows\system32\nvidia-smi.exe`.
- `ollama` was not found.
- `llama-cli` was not found.
- `llama-server` was not found.
- `huggingface-cli` was not found.

GPU check:

```text
NVIDIA GeForce RTX 3050 4GB Laptop GPU, 4096 MiB total, 3930 MiB free, driver 581.83
```

Python package check using `C:\Users\leomu\.local\bin\python.exe`:

```text
torch: false
transformers: false
huggingface_hub: false
llama_cpp: false
sentencepiece: false
accelerate: false
bitsandbytes: false
```

Local model/search check:

- No local `*.gguf` files were found under the checked project/user cache paths.
- No local Llama `*.safetensors` or model `*.bin` weights were found under the
  checked project/user cache paths.
- No local `2605.05115v1.pdf` or file matching `*2605.05115*` was found.

Credential check:

- `C:\Users\leomu\.cache\huggingface\token` does not exist.
- `C:\Users\leomu\.huggingface\token` does not exist.
- `HF_TOKEN` is not present in the environment.
- `HUGGINGFACE_HUB_TOKEN` is not present in the environment.

## Blocker

The requested primary experiment requires next-token logits from
`meta-llama/Llama-3.1-8B` or `meta-llama/Llama-3.1-8B-Instruct`. In this
environment, collection is blocked by all of the following:

1. No local model weights or GGUF quantization are available.
2. No local inference executable is installed.
3. No Python inference stack is installed.
4. No Hugging Face token is configured for the gated official Llama 3.1 8B
   weights.
5. No hosted/cloud logprob endpoint or credentials were available in the
   workspace context.

Because the model and tokenizer cannot be loaded, the weekday answer-bin token
ids could not be verified and no next-token probability mass could be measured.

## Artifacts Not Created

The following requested empirical artifacts were intentionally not created:

- `empirical/data/weekdays_llama31_8b_centroids_7bin.json`
- `empirical/data/weekdays_llama31_8b_centroids_8bin_with_other.json`
- `empirical/reports/weekdays_llama31_8b_K_CH.md`
- `empirical/reports/weekdays_llama31_8b_K_CH.json`

## Unblocked Path

To complete the experiment, provide one of:

- a local GGUF or Hugging Face cache for Llama 3.1 8B/Instruct plus a runtime
  that exposes next-token logits;
- a configured Hugging Face token with accepted Llama 3.1 license access, plus
  permission to install the Python inference stack; or
- a hosted endpoint/API that returns next-token logprobs for the selected Llama
  3.1 8B variant.

Once model access is available, the next step is to collect the 49 prompt
distributions, normalize the seven weekday bins, save the 7-bin centroid JSON,
and run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json empirical\data\weekdays_llama31_8b_centroids_7bin.json --report empirical\reports\weekdays_llama31_8b_K_CH.md --json empirical\reports\weekdays_llama31_8b_K_CH.json
```
