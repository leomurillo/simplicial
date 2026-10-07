# Month Control Probe Readiness

## Verdict

The month row is not from scratch, but it is not locally data-ready.

Wurgaft et al. explicitly use cyclic language tasks, and public summaries of
the figure include months as a cyclic task.  The public Causalab README,
however, currently advertises the runnable public entry point as the weekday
pipeline and the `demos/weekdays_geometry.ipynb` notebook.  I do not see a
published month artifact in this workspace.

Therefore the correct status is:

1. the task shape is already in the Wurgaft/Causalab family;
2. the exact month artifact is still an upstream input for this repository;
3. the local second control should be prepared as an artifact adapter, not
   as a claim that month centroids have already landed here.

## Why C12 Comes Next

The prime weekday row is the clean no-Ext control:

```text
C7: one nontrivial conductor packet
```

The month row is the next empirical control because:

```text
C12 ~= C4 x C3
```

The nontrivial additive-character conductor packets are:

| conductor | dimension | p=2 part | p=3 part |
|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 |
| 3 | 2 | 1 | 3 |
| 4 | 2 | 4 | 1 |
| 6 | 2 | 2 | 3 |
| 12 | 4 | 4 | 3 |

So the p=2 component already sees conductor depths 1, 2, and 4, while the
p=3 component gives a tame companion factor.  That is exactly the intermediate
check between the prime C7 control and the genuinely local finite rows.

## Boundary

C12 should be run before reaching for a finite-field local neural claim, but
it should not be oversold as the same thing as `F4[u]/(u^2)`.

The month task tests mixed conductor splitting in a cyclic CRT label algebra.
It does not by itself test nilpotent carry, local principal units, or the
`Ext_CH` obstruction.  A positive month result would say the Wurgaft pipeline
sees a mixed conductor product.  The finite-field local row is still needed
for genuine tame/wild carry data.

## Local Work Landed

The C12 lane now has executable scaffolding:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_cyclic_centroids_from_dump.py --preset months
C:\Users\leomu\.local\bin\python.exe empirical\compute_cyclic_K_CH.py --preset months
```

Generated files:

```text
empirical/data/months_probe_manifest.json
empirical/reports/months_centroid_build.md
empirical/reports/months_cyclic_K_CH_prediction.md
empirical/reports/months_cyclic_K_CH_prediction.json
```

The parametric C12 proxy currently gives:

| comparison | r |
|---|---:|
| Hellinger chord vs cyclic Hellinger arc | 0.729101 |
| moment Euclidean chord vs cyclic Hellinger arc | 0.696128 |
| natural/logit chord vs cyclic Hellinger arc | 0.773256 |
| Fisher LC endpoint distance vs cyclic Hellinger arc | 0.732249 |

These are not transformer measurements.  They are the behavior-side target
shape for the empirical artifact.

## Upstream Artifact Need

If Causalab has the month analogue of the weekday artifact, the expected shape
is:

```text
artifacts/natural_domains_arithmetic/llama31_8b/months/baseline/per_class_output_dists.safetensors
```

That path is inferred from the weekday artifact naming pattern and must be
checked against the actual runner output.

If supplied, run:

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\build_cyclic_centroids_from_dump.py --preset months --per-class-safetensors path\to\per_class_output_dists.safetensors --report empirical\reports\months_centroid_build.md
C:\Users\leomu\.local\bin\python.exe empirical\compute_cyclic_K_CH.py --preset months --centroids-json empirical\data\months_llama31_8b_centroids_12bin.json --report empirical\reports\months_llama31_8b_K_CH.md --json empirical\reports\months_llama31_8b_K_CH.json
```

## Sources Checked

- arXiv page for Wurgaft et al., `2605.05115`, accessed May 12, 2026:
  https://arxiv.org/abs/2605.05115
- public Causalab README, accessed May 12, 2026:
  https://github.com/goodfire-ai/causalab
- public paper summary with the figure caption naming months, accessed
  May 12, 2026:
  https://chatpaper.com/paper/275889
