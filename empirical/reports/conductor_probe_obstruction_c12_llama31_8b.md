# Conductor Probe-Obstruction Prereg Check -- Llama-3.1-8B

**Run date:** 2026-05-16
**Source:** `months\baseline\per_class_output_dists.safetensors`
**Label algebra:** `C_12`
**Quotients:** `[2, 3, 4, 6, 12]`
**Controls:** 500 shuffled-label draws; 500 same-rank random subspaces.

For `k = N`, the quotient is full rank on the zero-sum tangent space, so every orthogonal control also retains all packets. Control breakage is assessed on the proper quotients `k < N`.

## Preregistered Prediction

A quotient-respecting rank-k readout retains exactly the conductor packets `H_d` with `d | k` and annihilates the packets with `d not| k`.  The measured quantity is packet-pure survival `||P_k h_d||^2 / ||h_d||^2` aggregated over the empirical class-centroid displacements.

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 | 0 | 0 |
| 3 | 0 | 1 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 | 0 | 0 |
| 6 | 1 | 1 | 0 | 1 | 0 |
| 12 | 1 | 1 | 1 | 1 | 1 |

## Aligned Quotient Readout

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 3 | 0.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 |
| 4 | 1.000000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 |
| 6 | 1.000000 | 1.000000 | 0.000000 | 1.000000 | 0.000000 |
| 12 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |

Error against the preregistered table:

- max absolute error: 2.220e-16
- mean absolute error: 1.332e-17

## Positive Control

The full conductor-aware readout retains every nontrivial packet.

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 12 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |

## Shuffled-Label Control

A common random permutation of output labels is applied before the same quotient projection and then undone before scoring true conductor packets. Mean packet-pure survival across shuffled-label draws:

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 2 | 0.083 | 0.097 | 0.094 | 0.084 | 0.092 |
| 3 | 0.184 | 0.179 | 0.179 | 0.186 | 0.182 |
| 4 | 0.256 | 0.275 | 0.276 | 0.271 | 0.275 |
| 6 | 0.458 | 0.455 | 0.450 | 0.449 | 0.458 |
| 12 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

Error distribution against the divisor step table:

- mean max absolute error: 0.945
- median max absolute error: 0.938
- 5%-95% max absolute error: [0.889, 1.000]
- mean absolute error: 0.307

## Same-Rank Random-Subspace Control

For each quotient k, the control uses a random real subspace of dimension `k-1` inside the zero-sum tangent hyperplane. Mean packet-pure survival:

| quotient k | H_2 | H_3 | H_4 | H_6 | H_12 |
|---:|---:|---:|---:|---:|---:|
| 2 | 0.094 | 0.089 | 0.091 | 0.095 | 0.089 |
| 3 | 0.184 | 0.176 | 0.179 | 0.182 | 0.185 |
| 4 | 0.269 | 0.274 | 0.273 | 0.277 | 0.271 |
| 6 | 0.467 | 0.451 | 0.456 | 0.448 | 0.455 |
| 12 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

Error distribution against the divisor step table:

- mean max absolute error: 0.947
- median max absolute error: 0.963
- 5%-95% max absolute error: [0.835, 0.999]
- mean absolute error: 0.306

## Verdict

The aligned quotient-respecting readout realizes the exact `{0,1}` divisor step function predicted by the conductor obstruction theorem on the saved C12 month centroids.  The shuffled-label and same-rank random-subspace controls do not preserve the step function: survival is fractional and no longer follows the `d | k` packet rule.

This does not claim that unconstrained supervised probes fail.  It tests the falsifiable theorem in the quotient/rank-restricted readout class and records the two controls a referee would expect before the result is used as interpretability bridge evidence.
