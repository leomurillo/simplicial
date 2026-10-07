# New-session prompt: empirical weekday control

This is a control/translation lane, not a blocker for the Paper 9/10/11
program.  The exact finite quotient work continues without this data.  If the
actual empirical weekday behavior-centroid matrix for Llama 3.1 8B becomes
available, run it through the local K_CH pipeline.

Work in `C:\Projects\simplicial`. The existing script is `empirical\compute_weekdays_K_CH.py`; it accepts:

Primary one-command conductor:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\orchestrate_weekdays_c7.py
```

It auto-detects the standard local centroid JSON, probability dump, or Goodfire
`per_class_output_dists.safetensors` artifact if present.  It can also route an
explicit source:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\orchestrate_weekdays_c7.py --per-class-safetensors <path\to\per_class_output_dists.safetensors>
C:\Users\leomu\.local\bin\python.exe empirical\orchestrate_weekdays_c7.py --dump-json <model_probability_dump.json>
C:\Users\leomu\.local\bin\python.exe empirical\orchestrate_weekdays_c7.py --centroids-json <weekdays_7x7_centroids.json>
C:\Users\leomu\.local\bin\python.exe empirical\orchestrate_weekdays_c7.py --source hf --hf-model meta-llama/Llama-3.1-8B --hf-device-map auto --hf-dtype bfloat16
```

The HF route uses `empirical\collect_weekday_prob_dump_hf.py` to collect real
next-token probabilities, then feeds the dump through the same centroid builder
and K_CH scorer.  If no real source is present, the conductor writes
`empirical\reports\weekdays_c7_orchestration.md` and refuses to create empirical
centroid/K_CH artifacts.

The low-level scorer remains:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json <path> --report <path> --json <path>
```

There is also a handoff script for the model-output side:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_weekday_centroids_from_dump.py --write-manifest empirical\data\weekdays_probe_manifest.json --dump-json <model_probability_dump.json> --report empirical\reports\weekdays_centroid_build.md
```

If using Goodfire/causalab's saved weekday baseline artifact instead of a JSON
dump, run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_weekday_centroids_from_dump.py --per-class-safetensors <path\to\per_class_output_dists.safetensors> --report empirical\reports\weekdays_centroid_build.md
```

The manifest-only command has already produced `empirical\data\weekdays_probe_manifest.json`.
The dump script does not run a model or fabricate data; it aggregates supplied
`weekday_probs`, `weekday_logprobs`, `token_probs`, `token_logprobs`, or a
seven-by-seven `per_class_output_dists.safetensors` tensor into the exact
seven-bin centroid JSON consumed by `compute_weekdays_K_CH.py`.

Goal: produce a real 7x7 weekday centroid probability matrix, not a parametric placeholder, then run the K_CH analysis.  If the data or runtime is unavailable, record the missing input precisely and return to the finite quotient program.

Local machine facts from the previous session:

- GPU: NVIDIA GeForce RTX 3050 4GB Laptop GPU, 4096 MiB VRAM.
- C: drive free space: about 719 GB.
- No local `ollama`, `llama-cli`, `llama-server`, or `huggingface-cli` was found.
- RAM could not be read from WMI because access was denied.

Do not fabricate empirical data. If model access, licensing, package install, HF token, RAM, or inference runtime prevents collection, write a precise missing-input report and stop this control lane there.

Primary experiment:

1. Use `meta-llama/Llama-3.1-8B` or `meta-llama/Llama-3.1-8B-Instruct`, preferring the same variant Wurgaft et al. used if the PDF/appendix identifies it. Record exact model id, revision if available, precision/quantization, inference runtime, and date.
2. Build the 49 weekday prompts for all ordered pairs `(start_day, offset)` with seven starts and offsets 1..7, or match the Wurgaft weekday prompt template if it is available in `2605.05115v1.pdf`.
3. For each prompt, obtain the next-token logits/probabilities. We need probabilities assigned to the seven weekday answer bins:
   `Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday`.
4. For each weekday bin, sum over the tokenizer variants that represent that answer as the next token. At minimum test leading-space and no-leading-space forms, for example `" Monday"` and `"Monday"`, and include case variants only if the prompt makes them plausible. Verify the token ids instead of assuming all names are single tokens.
5. Aggregate the 49 distributions by correct answer day to produce seven behavior centroids. The resulting matrix should have rows ordered Monday..Sunday and columns ordered Monday..Sunday. Each row must be strictly positive and sum to 1 over the seven weekday bins. If there is significant probability outside the seven names, save an auxiliary 8-bin version with `other`, but feed the normalized 7-bin conditional matrix into the existing K_CH script.
6. Save:
   - `empirical\data\weekdays_llama31_8b_centroids_7bin.json`
   - `empirical\data\weekdays_llama31_8b_centroids_8bin_with_other.json` if applicable
   - `empirical\reports\weekdays_llama31_8b_K_CH.md`
   - `empirical\reports\weekdays_llama31_8b_K_CH.json`
7. Run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json empirical\data\weekdays_llama31_8b_centroids_7bin.json --report empirical\reports\weekdays_llama31_8b_K_CH.md --json empirical\reports\weekdays_llama31_8b_K_CH.json
```

What to report:

- The 7x7 centroid matrix.
- Row-sum and positivity checks.
- Token ids used for each weekday bin.
- Total out-of-weekday probability before renormalization.
- The resulting K_CH/Fisher/Hellinger diagnostics from the report JSON.
- Whether the measured intrinsic behavior geometry narrows or explains the Wurgaft 0.99-vs-0.89 gap.

Hardware strategy:

- Full BF16 Llama 3.1 8B is not realistic on the 4GB GPU. It is roughly a 16 GB weights download before runtime overhead.
- A 4-bit GGUF Llama 3.1 8B is realistic in storage terms, roughly 5 GB, but may need CPU/RAM offload and will be slower. That is acceptable for 49 prompts if logits can be extracted reliably.
- If local execution is too painful, use a hosted or cloud runtime that exposes next-token logits/logprobs, or ask Wurgaft's team for their published-run behavior centroids. Make clear whether the output is exact BF16 replication or a quantized local proxy.

Second-phase comparisons, after Llama 3.1 8B:

1. Run the same weekday K_CH pipeline on Gemma 4 E2B or E4B. E2B is the best local sanity model; E4B is stronger but heavier.
2. Run Qwen3-4B as a text-only, Apache-licensed comparison if Gemma tooling is inconvenient.
3. Add a composite cyclic task, especially months (`C12`), because it tests the conductor-block decomposition instead of only the prime `C7` single nontrivial block.
4. Preserve the same centroid JSON schema for every model/task pair so Paper 9/10/11 comparisons can use the same pipeline.
