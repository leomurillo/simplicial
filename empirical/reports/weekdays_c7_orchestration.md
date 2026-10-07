# Weekdays C7 Orchestration

## Status

- outcome: `blocked`
- source: `blocked`
- timestamp: `2026-05-12T17:28:17`

## Blockers

- No real C7 data source was found in the workspace.
- Expected Goodfire artifact, if present: artifacts/natural_domains_arithmetic/llama31_8b/weekdays/baseline/per_class_output_dists.safetensors
- Provide --centroids-json, --dump-json, --per-class-safetensors, or --hf-model with a runnable local Hugging Face model.

## Artifact Targets

- manifest: `empirical\data\weekdays_probe_manifest.json`
- probability dump: `empirical\data\weekdays_llama31_8b_probability_dump.json`
- seven-bin centroids: `empirical\data\weekdays_llama31_8b_centroids_7bin.json`
- eight-bin centroids: `empirical\data\weekdays_llama31_8b_centroids_8bin_with_other.json`
- K_CH report: `empirical\reports\weekdays_llama31_8b_K_CH.md`
- K_CH JSON: `empirical\reports\weekdays_llama31_8b_K_CH.json`

## Boundary

This orchestration treats a run as empirical only when a real dump, real centroids, a real safetensors artifact, or a successfully scored local model is supplied. Otherwise it stops at this report and does not overwrite empirical K_CH outputs.
