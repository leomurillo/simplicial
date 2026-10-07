# Weekdays K^CH Prediction

## Setup

This computation is intrinsic to the seven-class weekday behavior simplex.
Empirical Wurgaft/Llama weekday output centroids were not found locally during the May 2026 repository inspection, so this run uses a cyclic parametric centroid model:

- peak mass on target weekday: `0.760000`
- mass on each adjacent weekday: `0.090000`
- uniform floor on each of the four non-neighbor weekdays: `0.015000`

Concrete empirical replacement path: create a JSON file containing either a top-level seven-by-seven array or `{ "centroids": [...] }`, with rows and columns ordered Monday through Sunday and each row a strictly positive probability vector summing to one. Then run `python empirical/compute_weekdays_K_CH.py --centroids-json path/to/weekdays_centroids.json`.

The reported Wurgaft et al. numbers used for comparison are:

- activation-manifold vs behavior-manifold isometry, weekdays: `r = 0.99` in the text, `r = 0.9896` in Fig. 2;
- activation-linear vs behavior-manifold distance, weekdays: `r = 0.89` in the text; Fig. 2 OCR exposes a lower panel near `r = 0.7097`, so the exact visual value should be checked against the source figure;
- naturalness energy, weekdays: manifold `E_BC = 0.34 +/- 0.03`; linear `E_BC = 0.93 +/- 0.11`;
- pullback recovery, weekdays: pullback `R^2 = 0.77 +/- 0.03`; linear baseline `R^2 = 0.42 +/- 0.07`.

Notation follows the engagement instructions: `theta` is the centered moment/m-coordinate `p - p_*`, and `eta` is the centered natural/logit/e-coordinate `log p - mean(log p) 1`. Paper 2 currently uses the opposite Greek-letter convention, so any insertion should either avoid the letters or flag the convention.

## Coordinate Translation

At the uniform centroid `p_* = (1/7) 1`:

- moment coordinate: `theta = p - p_* in H`;
- natural coordinate: `eta = log p - mean(log p) 1 in H`;
- Hellinger coordinate: `x = sqrt(p) in S^6_+`;
- infinitesimally at `p_*`, `d eta = 7 d theta` and `d x = (sqrt(7)/2) d theta`;
- Fisher metric: `g_p(u,v) = sum_i u_i v_i / p_i`; at `p_*`, `g = 7 <.,.>_Euc`;
- Amari-Chentsov cubic: `T_p(u,v,w)=sum_i u_i v_i w_i / p_i^2`;
- raised cubic: `K^CH_p(u)v = u v / p - g_p(u,v) p`, tangent-projected.

The Hellinger coordinate is therefore an admissible spherical coordinate choice for the same Fisher object, not the unique intrinsic coordinate system.

Sign convention warning: Paper 11 fixes `K^CH = Gamma^(m) - Gamma^(e)`. If a prior table used the opposite e/m convention, its magnitudes remain valid but all signed `K^CH` displacement entries must be explicitly flipped.

## Parametric Centroids

Rows are ordered Monday through Sunday.

```text
[0.760000, 0.090000, 0.015000, 0.015000, 0.015000, 0.015000, 0.090000]
[0.090000, 0.760000, 0.090000, 0.015000, 0.015000, 0.015000, 0.015000]
[0.015000, 0.090000, 0.760000, 0.090000, 0.015000, 0.015000, 0.015000]
[0.015000, 0.015000, 0.090000, 0.760000, 0.090000, 0.015000, 0.015000]
[0.015000, 0.015000, 0.015000, 0.090000, 0.760000, 0.090000, 0.015000]
[0.015000, 0.015000, 0.015000, 0.015000, 0.090000, 0.760000, 0.090000]
[0.090000, 0.015000, 0.015000, 0.015000, 0.015000, 0.090000, 0.760000]
```

## K^CH at the Centroid

At `p_*`, the formulas reduce to:

```text
T_{p_*}(u,v,w) = 49 sum_i u_i v_i w_i
K^CH_{p_*}(u)v = 7 u*v - 7 <u,v>_Euc p_*
```

Centroid-normalized against the full character/multiplication algebra, this is the `c = 1` convention of Paper 11: before the augmentation-corner projection, multiplication by a character is literally multiplication by that character at `p_*`. The table below gives a concrete real-coordinate operator for the Monday displacement `theta_Monday = p_Monday - p_*`, acting on the seven centered vertex directions `e_i - p_*`.

```text
[3.085714, -0.564286, -0.489286, -0.489286, -0.489286, -0.489286, -0.564286]
[-0.564286, -0.264286, 0.180714, 0.180714, 0.180714, 0.180714, 0.105714]
[-0.489286, 0.180714, -0.639286, 0.255714, 0.255714, 0.255714, 0.180714]
[-0.489286, 0.180714, 0.255714, -0.639286, 0.255714, 0.255714, 0.180714]
[-0.489286, 0.180714, 0.255714, 0.255714, -0.639286, 0.255714, 0.180714]
[-0.489286, 0.180714, 0.255714, 0.255714, 0.255714, -0.639286, 0.180714]
[-0.564286, 0.105714, 0.180714, 0.180714, 0.180714, 0.180714, -0.264286]
```

### Character-Basis Form

Because `7` is prime, the nontrivial C7 Fisher tangent space is a single six-dimensional conductor packet. Let `phi_k(x)=7^(-1/2) exp(2 pi i kx/7)` and let `hat h_r=<phi_r,h>` be the unitary additive-character coefficients. For `h in H` and `ell != 0`,

```text
K^CH_{p_*}(h) phi_ell = sqrt(7) sum_{k=1}^6 hat h_{k-ell} phi_k
```

Thus the off-centroid Taylor support is pure convolution in the dual group `Z/7Z`; in the prime weekday case there is no further conductor splitting to hide it.

For the Monday displacement `theta_Monday`, the unitary Fourier coefficients `hat h_r`, `r=0,...,6`, are:

```text
[0.000000+0.000000i, 0.316932+0.000000i, 0.268968+0.000000i, 0.230503+0.000000i, 0.230503+0.000000i, 0.268968+0.000000i, 0.316932+0.000000i]
```

The nontrivial character-basis matrix of `v |-> K^CH_{p_*}(theta_Monday)v`, with rows and columns ordered `1,...,6`, is:

```text
[0.000000+0.000000i, 0.838523+0.000000i, 0.711622+0.000000i, 0.609855+0.000000i, 0.609855+0.000000i, 0.711622+0.000000i]
[0.838523+0.000000i, 0.000000+0.000000i, 0.838523+0.000000i, 0.711622+0.000000i, 0.609855+0.000000i, 0.609855+0.000000i]
[0.711622+0.000000i, 0.838523+0.000000i, 0.000000+0.000000i, 0.838523+0.000000i, 0.711622+0.000000i, 0.609855+0.000000i]
[0.609855+0.000000i, 0.711622+0.000000i, 0.838523+0.000000i, 0.000000+0.000000i, 0.838523+0.000000i, 0.711622+0.000000i]
[0.609855+0.000000i, 0.609855+0.000000i, 0.711622+0.000000i, 0.838523+0.000000i, 0.000000+0.000000i, 0.838523+0.000000i]
[0.711622+0.000000i, 0.609855+0.000000i, 0.609855+0.000000i, 0.711622+0.000000i, 0.838523+0.000000i, 0.000000+0.000000i]
```

## Displacement Probes

### Adjacent Monday -> Tuesday

- cyclic separation: `1`
- `theta` displacement: `[-0.670000, 0.670000, 0.075000, 0.000000, 0.000000, 0.000000, -0.075000]`
- `eta` endpoint difference: `[-2.133509, 2.133509, 1.791759, 0.000000, 0.000000, 0.000000, -1.791759]`
- Hellinger tangent at `p_*`: `[-0.886327, 0.886327, 0.099216, 0.000000, 0.000000, 0.000000, -0.099216]`
- Fisher norm `||h||_F`: `2.522568`
- cubic scalar `T(h,h,h)`: `0.000000`
- unit-direction cubic `T(hat h,hat h,hat h)`: `0.000000`
- raised cubic `K^CH(h)h`: `[2.233250, 2.233250, -0.869675, -0.909050, -0.909050, -0.909050, -0.869675]`
- `||K^CH(h)h||_F`: `9.887678`
- second-order endpoint deviation norm coefficient: `2.471919`
- second-order midpoint deviation norm coefficient: `0.617980`
- exact max same-parameter m-flat vs Fisher LC path, Hellinger units: `0.021088`
- exact max same-parameter e-flat vs Fisher LC path, Hellinger units: `0.025024`
- exact path lengths `(m, e, LC)` in Hellinger units: `(0.619367, 0.620585, 0.618206)`

The m-flat sign is `-1/4 K^CH(h,h)` and the e-flat sign is `+1/4 K^CH(h,h)` for same-initial-velocity endpoint displacement; norms are equal.

### Non-adjacent Monday -> Wednesday

- cyclic separation: `2`
- `theta` displacement: `[-0.745000, 0.000000, 0.745000, 0.075000, 0.000000, 0.000000, -0.075000]`
- `eta` endpoint difference: `[-3.925268, 0.000000, 3.925268, 1.791759, 0.000000, 0.000000, -1.791759]`
- Hellinger tangent at `p_*`: `[-0.985542, 0.000000, 0.985542, 0.099216, 0.000000, 0.000000, -0.099216]`
- Fisher norm `||h||_F`: `2.801625`
- cubic scalar `T(h,h,h)`: `0.000000`
- unit-direction cubic `T(hat h,hat h,hat h)`: `0.000000`
- raised cubic `K^CH(h)h`: `[2.763875, -1.121300, 2.763875, -1.081925, -1.121300, -1.121300, -1.081925]`
- `||K^CH(h)h||_F`: `12.236728`
- second-order endpoint deviation norm coefficient: `3.059182`
- second-order midpoint deviation norm coefficient: `0.764796`
- exact max same-parameter m-flat vs Fisher LC path, Hellinger units: `0.066410`
- exact max same-parameter e-flat vs Fisher LC path, Hellinger units: `0.131502`
- exact path lengths `(m, e, LC)` in Hellinger units: `(0.825285, 0.863443, 0.814304)`

The m-flat sign is `-1/4 K^CH(h,h)` and the e-flat sign is `+1/4 K^CH(h,h)` for same-initial-velocity endpoint displacement; norms are equal.

## Intrinsic Linear-vs-Manifold Prediction

Using the seven cyclic centroids only, the correlation between flat output-simplex distances and cyclic behavior-manifold arc distances is:

- Hellinger chord vs cyclic Hellinger arc: `r = 0.910010`
- moment Euclidean chord vs cyclic Hellinger arc: `r = 0.886448`
- natural/logit chord vs cyclic Hellinger arc: `r = 0.941295`
- Fisher LC endpoint distance vs cyclic Hellinger arc: `r = 0.911776`

## Gap Accounting

Using the text-level Wurgaft weekday reference `r_manifold = 0.9896` and `r_linear = 0.89`:

- published text gap: `0.099600`
- intrinsic behavior-side linear gap: `0.103152`
- residual versus text linear baseline: `-0.003552`
- fraction of text gap accounted for by intrinsic behavior geometry: `1.035662`

This is the important outcome: the symmetric seven-centroid output model reproduces the text-level weekday linear correlation almost exactly in moment coordinates (`0.886` here versus Wurgaft et al.'s `0.89`) while keeping a clear gap to the manifold isometry (`0.99`). The cubic predicts nonzero local path curvature through `K^CH(h)h`, the explicit cubic curvature operator separating linear flat paths from Fisher/Hellinger manifold paths, but cyclic symmetry makes the pairwise distance matrix remain largely monotone in cyclic separation. Therefore the output-side cubic can explain the modest weekday text gap, but not a substantially lower figure-panel value such as `0.71` without empirical centroids, activation-side distortion, spline-parameterization effects, or some combination of those residuals.

## Comparison to Wurgaft et al.

The intrinsic behavior-side computation agrees with Wurgaft et al. on the positive claim: the behavior manifold has the right geometry, and Hellinger/Fisher coordinates make the cyclic structure explicit. It also lands on the reported weekday text correlation for linear paths. What it cannot decide, without their empirical activation and output centroids, is how much of any stronger linear-path failure comes from `M_y` itself versus the activation-side map.

The next named object should be the activation-side residual of the pullback: the part of `J_F^T g_y J_F` and its cubic correction that is not captured by the intrinsic `M_y` Fisher cubic. The script now has an explicit replacement path for empirical centroids via `--centroids-json`; until those centroids are supplied, the report remains a parametric proxy rather than a measurement on Llama outputs.

## Caveats

- The weekday centroids are parametric, not extracted from Llama 3.1 8B.
- Wurgaft et al. add an `other` bin in the paper's output distributions; this computation uses the seven weekday concept tokens only, as requested.
- Their measured correlations compare activation-space distances to behavior-manifold distances. This script computes an intrinsic behavior-space proxy.
- The second-order `K^CH` signs use the Paper 11 convention `K^CH = Gamma^(m) - Gamma^(e)`. Reversing the e/m convention flips signs but not norms.
- Numerical path comparisons use `400` intervals; increasing this only changes the last decimals.

## Reproduction

```powershell
python empirical/compute_weekdays_K_CH.py
python empirical/compute_weekdays_K_CH.py --centroids-json path/to/weekdays_centroids.json
```

The script also emits `empirical/reports/weekdays_K_CH_prediction.json` with the raw values.
