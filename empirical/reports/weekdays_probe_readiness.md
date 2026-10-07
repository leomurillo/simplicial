# Weekday Control Probe Readiness

## Verdict

The residual-1% weekday probe is upstream-blocked in this workspace, but the
Paper 9/10/11 program is not blocked.

The weekday lane is a prime \(C_7\) control and a translation device for the
deep-learning surround.  The mathematical computation is runnable once a real
seven-by-seven weekday centroid matrix exists.  The existing
`compute_weekdays_K_CH.py` script consumes that matrix and produces the
Fisher/Hellinger/K_CH diagnostics.  The newly added
`build_weekday_centroids_from_dump.py` script supplies the handoff:
it records the 49 prompt cases and aggregates a model probability/logprob dump
or Goodfire's `per_class_output_dists.safetensors` artifact into the exact
centroid JSON expected by the K_CH script.

## Current Machine Check

- GPU present: NVIDIA GeForce RTX 3050 4GB Laptop GPU, 4096 MiB total, 3930 MiB free, driver 581.83.
- No local `ollama`, `llama-cli`, `llama-server`, or `huggingface-cli` command was found.
- Python packages absent: `torch`, `transformers`, `huggingface_hub`, `llama_cpp`, `sentencepiece`, `accelerate`, `bitsandbytes`.
- Hugging Face token files were not found at `C:\Users\leomu\.cache\huggingface\token` or `C:\Users\leomu\.huggingface\token`.
- No empirical centroid JSON exists at `empirical\data\weekdays_llama31_8b_centroids_7bin.json`.

## Prepared Handoff

The prompt manifest exists:

```text
empirical\data\weekdays_probe_manifest.json
```

It contains all 49 ordered `(start_day, offset)` cases, rows and columns ordered
Monday through Sunday, with the correct weekday recorded for each case.

Given a probability dump, run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_weekday_centroids_from_dump.py --write-manifest empirical\data\weekdays_probe_manifest.json --dump-json <model_probability_dump.json> --report empirical\reports\weekdays_centroid_build.md
```

Then run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json empirical\data\weekdays_llama31_8b_centroids_7bin.json --report empirical\reports\weekdays_llama31_8b_K_CH.md --json empirical\reports\weekdays_llama31_8b_K_CH.json
```

## Exact Upstream Need For This Control

Supply one of:

1. a local Llama 3.1 8B/Instruct runtime that exposes next-token logits or
   probabilities for the manifest prompts;
2. a hosted/cloud endpoint with next-token logprobs for the selected model; or
3. Wurgaft et al.'s published or shareable weekday behavior centroids.

The dump may contain `weekday_probs`, `weekday_logprobs`, `token_probs`, or
`token_logprobs`.  If token-level output is supplied, the builder bins exact
next-token strings such as `Monday` and ` Monday` unless a tokenizer-verified
`token_bins` object is included in the dump.

The Goodfire `weekdays_geometry.ipynb` notebook identifies a particularly
narrow artifact target:

```text
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/baseline/per_class_output_dists.safetensors
```

That notebook reports this tensor as `torch.Size([7, 7])`.  If supplied, use
`--per-class-safetensors` instead of `--dump-json`.

## Boundary

Do not call the local parametric weekday report an empirical measurement.  Until
one of the upstream inputs above exists, the project can state the prime `C7`
control algebra and the K_CH prediction, but it cannot measure the real
transformer residual.

This does not stop the active program.  The filtered arithmetic signal has
already appeared in the exact finite row `F_4[u]/(u^2)`, where the associated
graded loses mixed tame/wild extension data that the quotient-character
adjacency algebra retains.
