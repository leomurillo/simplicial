# Months \(C_{12}\) Conductor Null Comparison -- Llama-3.1-8B

**Model:** Llama-3.1-8B  
**Source:** `months/baseline/per_class_output_dists.safetensors`  
**Run date:** 2026-05-15  
**Task:** compare the aggregate \(C_{12}\) conductor-energy split against
the per-character-uniform null and a common output-label permutation null.

## Verdict

The raw aggregate conductor split is close to the per-character-uniform null
induced by packet dimensions \((1,2,2,2,4)\), with a small systematic tilt away
from conductors \(2,3,4\) and toward conductors \(6,12\).  This means the raw
aggregate table should not be described by itself as proof of CRT-specific
routing.  It is better read as:

1. a stable all-nontrivial-character energy pattern,
2. with a modest high-conductor bias,
3. whose CRT-specific interpretation requires class-level anisotropy,
   label-permutation controls, unstructured 12-class controls, and replication.

## Per-Character-Uniform Null

For \(C_{12}\), the nontrivial character counts by conductor are:

| conductor | character indices | count | per-character null |
|---:|---|---:|---:|
| 2 | \(6\) | 1 | 0.090909 |
| 3 | \(4,8\) | 2 | 0.181818 |
| 4 | \(3,9\) | 2 | 0.181818 |
| 6 | \(2,10\) | 2 | 0.181818 |
| 12 | \(1,5,7,11\) | 4 | 0.363636 |

The observed aggregate split is:

| conductor | observed | null | observed - null | row-bootstrap 95% CI for diff |
|---:|---:|---:|---:|---:|
| 2 | 0.085581 | 0.090909 | -0.005328 | [-0.010239, -0.001294] |
| 3 | 0.168923 | 0.181818 | -0.012895 | [-0.019928, -0.007121] |
| 4 | 0.172981 | 0.181818 | -0.008837 | [-0.015466, -0.003566] |
| 6 | 0.192102 | 0.181818 | +0.010284 | [+0.003500, +0.019019] |
| 12 | 0.380412 | 0.363636 | +0.016776 | [+0.008825, +0.026005] |

Bootstrap details: 200,000 resamples of the 12 input-class rows, with
replacement.  This bootstrap treats the 12 class centroids as the population
being summarized; it is not a replacement for prompt-level uncertainty or an
unstructured-task null.

Aggregate distances from the per-character null:

- \(L^1\) distance: 0.054119.
- \(L^2\) distance: 0.025689.

## Common Output-Label Permutation Null

As a stronger sanity check, a common random permutation of the 12 output labels
was applied to all rows before recomputing the conductor fractions.  This
preserves the per-class probability spectra while breaking the alignment
between month labels and the \(C_{12}\) character basis.

Permutation count: 50,000.

| conductor | observed | permutation 2.5% | permutation median | permutation 97.5% | observed percentile |
|---:|---:|---:|---:|---:|---:|
| 2 | 0.085581 | 0.083270 | 0.090696 | 0.100703 | 0.1450 |
| 3 | 0.168923 | 0.171835 | 0.180950 | 0.195741 | 0.0004 |
| 4 | 0.172981 | 0.170261 | 0.181536 | 0.194769 | 0.0856 |
| 6 | 0.192102 | 0.170539 | 0.181594 | 0.194793 | 0.9378 |
| 12 | 0.380412 | 0.346914 | 0.363910 | 0.378574 | 0.9870 |

For the aggregate \(L^2\) distance from the per-character null:

- observed: 0.025689;
- permutation 95% interval: [0.005739, 0.024820];
- observed percentile: 0.9803.

This suggests that the high-conductor tilt is not a generic consequence of
arbitrary output-label ordering.  It still does not by itself prove
CRT-specific routing, because the correct negative controls are prompt-level
bootstrap, unstructured 12-class tasks, and replication on a second model
family.

## Class-Level Conductor 6 Anisotropy

Conductor 6 is the mixed \(C_4\times C_3\) packet.  Its class-level fractions
relative to the per-character null \(2/11=0.181818\) are:

| month | cond 6 fraction | diff from null |
|---|---:|---:|
| Jan | 0.227 | +0.045 |
| Feb | 0.189 | +0.008 |
| Mar | 0.191 | +0.009 |
| Apr | 0.217 | +0.035 |
| May | 0.181 | -0.000 |
| Jun | 0.184 | +0.002 |
| Jul | 0.183 | +0.001 |
| Aug | 0.185 | +0.003 |
| Sep | 0.186 | +0.004 |
| Oct | 0.184 | +0.003 |
| Nov | 0.185 | +0.003 |
| Dec | 0.193 | +0.011 |

Summary:

- mean: 0.192102;
- standard deviation across classes: 0.014556;
- min/max: 0.181367 / 0.227137;
- range: 0.045770.

The mixed packet is not uniformly elevated across classes.  The largest
class-level contributions are January and April.  A future class-anisotropy
test should therefore look beyond the aggregate mean and test whether these
months remain high under prompt resampling, label permutations, and a second
model family.

## Reading for the Paper

Use the following phrasing:

> The \(C_{12}\) aggregate conductor split is close to the
> per-character-uniform null but shows a stable high-conductor tilt, especially
> in conductors \(6\) and \(12\).  This supports a cautious composite-control
> reading, not a standalone proof of CRT-specific routing.

Avoid:

> The aggregate conductor split proves that the transformer learns CRT routing.

