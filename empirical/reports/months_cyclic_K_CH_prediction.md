# Months C12 K^CH Probe

## Status

- label count: `12`
- centroid source: `parametric`
- peak mass on target label: `0.760000`
- mass on adjacent labels: `0.090000` each
- uniform floor on other labels: `0.006667`

This report is intrinsic to the output simplex.  It measures the behavior-side Fisher cubic available before any activation pullback, Hessian, or steering-path residual is estimated.

## Label Order

`January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`

## Character Conductors

| conductor | dimension | character indices |
|---:|---:|---|
| 2 | 1 | `6` |
| 3 | 2 | `4, 8` |
| 4 | 2 | `3, 9` |
| 6 | 2 | `2, 10` |
| 12 | 4 | `1, 5, 7, 11` |

## CRT Packet Table

| conductor | dimension | p=2 part | p=3 part |
|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 |
| 3 | 2 | 1 | 3 |
| 4 | 2 | 4 | 1 |
| 6 | 2 | 2 | 3 |
| 12 | 4 | 4 | 3 |

For C12, the CRT view is C4 x C3.  The p=2 part takes values 1, 2, and 4 across the nontrivial tangent packets, so the month row is an intermediate mixed-conductor control: less local than F4[u]/(u^2), but already richer than prime C7.

## Centroids

Rows and columns use the label order above.

```text
[0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000]
[0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000, 0.006667]
[0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000, 0.090000]
[0.090000, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.006667, 0.090000, 0.760000]
```

## K^CH at the Uniform Centroid

At p_* = (1/n) 1,

```text
T_{p_*}(u,v,w) = n^2 sum_i u_i v_i w_i
K^CH_{p_*}(u)v = n u*v - n <u,v>_Euc p_*
```

In the nontrivial character basis, the first-label displacement acts by cyclic convolution.  The matrix below omits the constant character row and column.

```text
[0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i]
[0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i]
[0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i]
[0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i]
[0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i]
[0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i]
[0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i]
[0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i, 0.7533+0.0000i]
[0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i, 0.8367+0.0000i]
[0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i, 0.8977+0.0000i]
[0.8367+0.0000i, 0.7533+0.0000i, 0.6700+0.0000i, 0.6090+0.0000i, 0.5867+0.0000i, 0.6090+0.0000i, 0.6700+0.0000i, 0.7533+0.0000i, 0.8367+0.0000i, 0.8977+0.0000i, 0.0000+0.0000i]
```

## Pair Probes

### January -> February

- cyclic separation: `1`
- theta displacement: `[-0.670000, 0.670000, 0.083333, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, -0.083333]`
- eta endpoint difference: `[-2.133509, 2.133509, 2.602690, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, -2.602690]`
- Fisher norm ||h||_F: `3.307607`
- cubic scalar T(h,h,h): `0.000000`
- unit-direction cubic T(hat h,hat h,hat h): `0.000000`
- ||K^CH(h)h||_F: `24.018742`
- second-order endpoint deviation norm coefficient: `6.004686`
- exact max m-flat vs Fisher LC path, Hellinger units: `0.023691`
- exact max e-flat vs Fisher LC path, Hellinger units: `0.029382`
- path lengths (m, e, LC), Hellinger units: `(0.634568, 0.636375, 0.632976)`

### January -> March

- cyclic separation: `2`
- theta displacement: `[-0.753333, 0.000000, 0.753333, 0.083333, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, -0.083333]`
- eta endpoint difference: `[-4.736198, 0.000000, 4.736198, 2.602690, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, -2.602690]`
- Fisher norm ||h||_F: `3.713076`
- cubic scalar T(h,h,h): `0.000000`
- unit-direction cubic T(hat h,hat h,hat h): `0.000000`
- ||K^CH(h)h||_F: `30.383501`
- second-order endpoint deviation norm coefficient: `7.595875`
- exact max m-flat vs Fisher LC path, Hellinger units: `0.080398`
- exact max e-flat vs Fisher LC path, Hellinger units: `0.184738`
- path lengths (m, e, LC), Hellinger units: `(0.887907, 0.960048, 0.874402)`

### January -> July

- cyclic separation: `6`
- theta displacement: `[-0.753333, -0.083333, 0.000000, 0.000000, 0.000000, 0.083333, 0.753333, 0.083333, 0.000000, 0.000000, 0.000000, -0.083333]`
- eta endpoint difference: `[-4.736198, -2.602690, 0.000000, 0.000000, 0.000000, 2.602690, 4.736198, 2.602690, 0.000000, 0.000000, 0.000000, -2.602690]`
- Fisher norm ||h||_F: `3.735452`
- cubic scalar T(h,h,h): `0.000000`
- unit-direction cubic T(hat h,hat h,hat h): `0.000000`
- ||K^CH(h)h||_F: `30.310070`
- second-order endpoint deviation norm coefficient: `7.577518`
- exact max m-flat vs Fisher LC path, Hellinger units: `0.073607`
- exact max e-flat vs Fisher LC path, Hellinger units: `0.152090`
- path lengths (m, e, LC), Hellinger units: `(0.917763, 0.969557, 0.909797)`

## Intrinsic Linear-vs-Manifold Prediction

- Hellinger chord vs cyclic Hellinger arc: `r = 0.729101`
- moment Euclidean chord vs cyclic Hellinger arc: `r = 0.696128`
- natural/logit chord vs cyclic Hellinger arc: `r = 0.773256`
- Fisher LC endpoint distance vs cyclic Hellinger arc: `r = 0.732249`

## Interpretation

C12 should be run before claiming a local finite-field row in the neural setting.  It is already present in Wurgaft-style month geometry, has CRT structure C4 x C3, and tests whether the activation/behavior pipeline sees a mixed conductor split before the genuinely local Ext_CH rows are invoked.

## Reproduction

```powershell
python empirical/compute_cyclic_K_CH.py --preset months
python empirical/compute_cyclic_K_CH.py --labels-json path/to/labels.json --centroids-json path/to/centroids.json
```

Path comparisons used `400` intervals.
