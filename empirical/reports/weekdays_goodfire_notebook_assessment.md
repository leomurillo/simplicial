# Goodfire Weekdays Notebook Assessment

## Finding

The Goodfire notebook is directly relevant, but the notebook file alone does
not contain the exact tensor needed for the weekday control.

It records a successful `meta-llama/Llama-3.1-8B` baseline run on the 49-case
weekday task and names the key artifact:

```text
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/baseline/per_class_output_dists.safetensors
```

The notebook log says this artifact has shape `torch.Size([7, 7])`.  That is
the missing weekday behavior-centroid matrix up to row normalization over the
seven weekday bins.

## What The Notebook Gives

- exact model id: `meta-llama/Llama-3.1-8B`;
- task setup: exhaustive 49-case weekday arithmetic;
- prompt examples such as `Q: What day is one days after Monday?\nA:`;
- base accuracy: `45/49 = 91.8%`;
- probability accuracy: `56.88482540450535%`;
- artifact names for `full_output_dists.safetensors`, `top_logits.json`, and
  `per_class_output_dists.safetensors`.
- PCA variance spectrum for the activation subspace:
  `16.8%, 14.8%, 12.8%, 7.4%, 6.3%, 5.3%, ...`, with the top 32 PCs totaling
  `98.0%`;
- evidence that the subspace step computed seven activation centroids from the
  49 samples, grouped by `result`.

The centroid log line is activation-side evidence, not output-side evidence.
In Causalab, `compute_centroids(features, param_tensors)` groups the projected
activation features by unique parameter combinations.  The subspace PCA script
saves the numerical activation artifacts as:

```text
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/subspace/pca_k32/result/rotation.safetensors
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/subspace/pca_k32/result/features/training_features.safetensors
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/subspace/pca_k32/result/features/raw_features.safetensors
artifacts/natural_domains_arithmetic/llama31_8b/weekdays/subspace/pca_k32/result/train_dataset.json
```

## What It Does Not Give

The committed notebook embeds rendered plots and logs, but not the raw
`per_class_output_dists.safetensors` bytes.  The confusion heatmap image is not
annotated with exact numbers, so extracting values from the image would be a
lossy approximation rather than the empirical centroid matrix.

The same applies to the activation centroids.  The notebook tells us they were
computed and plotted, but it does not embed the actual seven centroid
coordinates, the 49 projected features, or the raw residual-stream features.
Those artifacts appear to live in the original runner's local
`/mnt/home/can.rager/causalab/artifacts/...` directory, not in the GitHub repo.

## Ready Path If Artifact Is Supplied

If we obtain `per_class_output_dists.safetensors`, run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_weekday_centroids_from_dump.py --per-class-safetensors path\to\per_class_output_dists.safetensors --report empirical\reports\weekdays_centroid_build.md
```

Then run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json empirical\data\weekdays_llama31_8b_centroids_7bin.json --report empirical\reports\weekdays_llama31_8b_K_CH.md --json empirical\reports\weekdays_llama31_8b_K_CH.json
```

## Verdict

Yes, this points to exactly what the weekday control would need.  No, the
notebook URL alone does not ship the needed data.  And no, the absence of those
artifacts does not block the filtered arithmetic program.

For the Paper 9/10 intrinsic behavior-side benchmark, the next ask is narrow:
get `per_class_output_dists.safetensors`.

For the residual-1% activation-side probe, the PCA line is close evidence but
not enough.  We also need the subspace artifacts, especially
`features/training_features.safetensors` plus `train_dataset.json`, or a rerun
of Goodfire's subspace step in an environment with Llama 3.1 8B access.

If those artifacts never arrive, close this empirical lane and continue with
the exact finite quotient census.
