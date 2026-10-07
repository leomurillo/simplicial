# Collatz Curvature Linearization: 2^5 x 3^1

## Status

This report samples the accelerated odd Collatz map on a finite quotient simplex, fits an affine-convolution linear skeleton, and measures the residual as carry-depth curvature.

- modulus: `96`
- odd residue states: `48`
- hidden lifts per state: `1024`
- total samples: `49152`
- fitted affine image size: `48` of `48` odd states
- true-kernel outdegree distribution: `{2: 24, 4: 12, 8: 6, 16: 3, 32: 3}`
- mean true row entropy: `1.932397` bits
- max true row entropy: `4.918695` bits

## Linear Skeleton Fit

The null model is the source-blind target marginal.  The seed model uses the visible affine numerator `3n+1`.  The fitted model searches source-sensitive affine bases `A*n+B (mod Q)` and learns one translation-invariant residual packet over affine deltas.  The carry-sliced model repeats that affine fit separately inside each carry packet.

| model | A | B | mean Fisher energy | mean Fisher norm | max Fisher norm | mean Hellinger | mean L1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| source-blind null | 0 | 0 | 14.375034 | 3.524140 | 4.654847 | 0.754863 | 1.626040 |
| seed affine 3n+1 | 3 | 1 | 14.375034 | 3.524140 | 4.654847 | 0.754863 | 1.626040 |
| best affine-convolution | 13 | 0 | 15.041660 | 3.645995 | 4.795933 | 0.821316 | 1.750424 |
| same-base carry-conditioned affine | 13 | 0 | 15.041607 | 3.645963 | 4.795832 | 0.821303 | 1.750244 |
| carry-sliced affine | - | - | 14.875025 | 3.507841 | 4.795832 | 0.753424 | 1.625841 |
| exact carry-lift oracle | - | - | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

Same-base carry conditioning changes the fitted mean Fisher residual energy by `0.00%` relative to the best global affine-convolution model.
Carry-sliced affine linearization changes it by `1.11%`.
The exact carry-lift oracle keeps the hidden lift coordinate required by division by `2^s`, so its residual is zero by construction; the audit below records the coordinate cost.

Top deltas in the best global affine residual packet:

- delta `0`: `0.020874`
- delta `18`: `0.020874`
- delta `16`: `0.020854`
- delta `20`: `0.020854`
- delta `22`: `0.020854`
- delta `26`: `0.020854`
- delta `38`: `0.020854`
- delta `44`: `0.020854`
- delta `52`: `0.020854`
- delta `58`: `0.020854`
- delta `60`: `0.020854`
- delta `76`: `0.020854`

## Carry Packets

Each row below holds one carry channel `s = v2(3n+1)`.  The two residual columns compare the global affine model with a carry-conditioned affine model using the same fitted `A,B`.

| s | samples | sources hit | sliced A,B | image | global energy | same-base energy | sliced energy | sliced reduction | top sliced deltas |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 24576 | 24 | 1,0 | 24 | 552.000017 | 552.000000 | 552.000000 | 0.00% | `0:0.0208, 2:0.0208, 4:0.0208, 6:0.0208, 8:0.0208, 10:0.0208, 12:0.0208, 14:0.0208` |
| 2 | 12288 | 12 | 1,0 | 12 | 132.000009 | 132.000000 | 132.000000 | 0.00% | `0:0.0208, 2:0.0208, 4:0.0208, 6:0.0208, 8:0.0208, 10:0.0208, 12:0.0208, 14:0.0208` |
| 3 | 6144 | 6 | 1,0 | 6 | 30.000004 | 30.000000 | 30.000000 | 0.00% | `0:0.0208, 2:0.0208, 4:0.0208, 6:0.0208, 8:0.0208, 10:0.0208, 12:0.0208, 14:0.0208` |
| 4 | 3072 | 3 | 0,0 | 1 | 6.000002 | 6.000000 | 0.000000 | 100.00% | `1:0.0625, 7:0.0625, 13:0.0625, 19:0.0625, 25:0.0625, 31:0.0625, 37:0.0625, 43:0.0625` |
| 5 | 1536 | 3 | 0,0 | 1 | 1.500001 | 1.500000 | 0.000000 | 100.00% | `5:0.0625, 11:0.0625, 17:0.0625, 23:0.0625, 29:0.0625, 35:0.0625, 41:0.0625, 47:0.0625` |
| 6 | 768 | 3 | 0,0 | 1 | 0.375000 | 0.375000 | 0.000000 | 100.00% | `1:0.0625, 7:0.0625, 13:0.0625, 19:0.0625, 25:0.0625, 31:0.0625, 37:0.0625, 43:0.0625` |
| 7 | 384 | 3 | 0,0 | 1 | 0.093750 | 0.093750 | 0.000000 | 100.00% | `5:0.0625, 11:0.0625, 17:0.0625, 23:0.0625, 29:0.0625, 35:0.0625, 41:0.0625, 47:0.0625` |
| 8 | 192 | 3 | 0,0 | 1 | 0.023438 | 0.023437 | 0.000000 | 100.00% | `1:0.0625, 7:0.0625, 13:0.0625, 19:0.0625, 25:0.0625, 31:0.0625, 37:0.0625, 43:0.0625` |
| 9 | 96 | 3 | 0,0 | 1 | 0.005859 | 0.005859 | 0.000000 | 100.00% | `5:0.0625, 11:0.0625, 17:0.0625, 23:0.0625, 29:0.0625, 35:0.0625, 41:0.0625, 47:0.0625` |
| 10 | 48 | 3 | 0,0 | 1 | 0.001465 | 0.001465 | 0.000000 | 100.00% | `1:0.0625, 7:0.0625, 13:0.0625, 19:0.0625, 25:0.0625, 31:0.0625, 37:0.0625, 43:0.0625` |
| 11 | 24 | 3 | 0,0 | 1 | 0.000915 | 0.000732 | 0.000488 | 46.65% | `5:0.0833, 11:0.0833, 17:0.0833, 23:0.0833, 29:0.0833, 35:0.0833, 41:0.0833, 47:0.0833` |
| 12 | 12 | 3 | 0,0 | 1 | 0.000503 | 0.000366 | 0.000366 | 27.26% | `1:0.0833, 7:0.0833, 13:0.0833, 19:0.0833, 25:0.0833, 31:0.0833, 37:0.0833, 43:0.0833` |
| 13 | 6 | 3 | 0,0 | 1 | 0.000263 | 0.000183 | 0.000183 | 30.43% | `5:0.1667, 11:0.1667, 17:0.1667, 23:0.1667, 29:0.1667, 35:0.1667` |
| 14 | 3 | 3 | 0,0 | 1 | 0.000134 | 0.000092 | 0.000092 | 31.91% | `1:0.3333, 7:0.3333, 13:0.3333` |
| 15 | 1 | 1 | 0,0 | 1 | 0.000045 | 0.000000 | 0.000000 | 100.00% | `5:1.0000` |
| 16 | 1 | 1 | 0,0 | 1 | 0.000045 | 0.000000 | 0.000000 | 100.00% | `1:1.0000` |
| 18 | 1 | 1 | 0,0 | 1 | 0.000045 | 0.000000 | 0.000000 | 100.00% | `1:1.0000` |

Global carry-depth distribution:

- `s=1`: `24576`
- `s=2`: `12288`
- `s=3`: `6144`
- `s=4`: `3072`
- `s=5`: `1536`
- `s=6`: `768`
- `s=7`: `384`
- `s=8`: `192`
- `s=9`: `96`
- `s=10`: `48`
- `s=11`: `24`
- `s=12`: `12`
- `s=13`: `6`
- `s=14`: `3`
- `s=15`: `1`
- `s=16`: `1`
- `s=18`: `1`

## Exact Carry-Lift Formula

For `n = x + kQ` and `s = v2(3n+1)`, the exact lifted linearization is

```text
target = ((3 * (x + kQ) + 1) / 2^s) mod Q
```

At fixed `x` and `s`, the target is determined by the hidden residue `k mod 2^s`.  The table shows source-only ambiguity before retaining that coordinate, and deterministic lift cells after retaining it.

| s | samples | sources hit | source edges | mean source outdegree | max source outdegree | lift bits | full cycle sampled | lift cells | deterministic cells | max cell outdegree | formula failures |
|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 1 | 24576 | 24 | 48 | 2.000000 | 2 | 1 | True | 48 | 48 | 1 | 0 |
| 2 | 12288 | 12 | 48 | 4.000000 | 4 | 2 | True | 48 | 48 | 1 | 0 |
| 3 | 6144 | 6 | 48 | 8.000000 | 8 | 3 | True | 48 | 48 | 1 | 0 |
| 4 | 3072 | 3 | 48 | 16.000000 | 16 | 4 | True | 48 | 48 | 1 | 0 |
| 5 | 1536 | 3 | 48 | 16.000000 | 16 | 5 | True | 48 | 48 | 1 | 0 |
| 6 | 768 | 3 | 48 | 16.000000 | 16 | 6 | True | 48 | 48 | 1 | 0 |
| 7 | 384 | 3 | 48 | 16.000000 | 16 | 7 | True | 48 | 48 | 1 | 0 |
| 8 | 192 | 3 | 48 | 16.000000 | 16 | 8 | True | 48 | 48 | 1 | 0 |
| 9 | 96 | 3 | 48 | 16.000000 | 16 | 9 | True | 48 | 48 | 1 | 0 |
| 10 | 48 | 3 | 48 | 16.000000 | 16 | 10 | True | 48 | 48 | 1 | 0 |
| 11 | 24 | 3 | 24 | 8.000000 | 8 | 11 | False | 24 | 24 | 1 | 0 |
| 12 | 12 | 3 | 12 | 4.000000 | 4 | 12 | False | 12 | 12 | 1 | 0 |
| 13 | 6 | 3 | 6 | 2.000000 | 2 | 13 | False | 6 | 6 | 1 | 0 |
| 14 | 3 | 3 | 3 | 1.000000 | 1 | 14 | False | 3 | 3 | 1 | 0 |
| 15 | 1 | 1 | 1 | 1.000000 | 1 | 15 | False | 1 | 1 | 1 | 0 |
| 16 | 1 | 1 | 1 | 1.000000 | 1 | 16 | False | 1 | 1 | 1 | 0 |
| 18 | 1 | 1 | 1 | 1.000000 | 1 | 18 | False | 1 | 1 | 1 | 0 |

## Largest Signed Residual Edges

Positive residual means the true sampled kernel puts more mass on the edge than the fitted global affine skeleton predicts; negative means the skeleton predicts mass that the sampled kernel does not use at that source.

| source | target | true | model | residual | true carry mix |
|---|---|---:|---:|---:|---|
| `3 [2:00011, 3:0]` | `53 [2:10101, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `11 [2:01011, 3:2]` | `17 [2:10001, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `15 [2:01111, 3:0]` | `71 [2:00111, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `23 [2:10111, 3:2]` | `83 [2:10011, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `27 [2:11011, 3:0]` | `41 [2:01001, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `31 [2:11111, 3:1]` | `47 [2:01111, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `35 [2:00011, 3:2]` | `5 [2:00101, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `39 [2:00111, 3:0]` | `59 [2:11011, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `47 [2:01111, 3:2]` | `71 [2:00111, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `55 [2:10111, 3:1]` | `35 [2:00011, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `59 [2:11011, 3:2]` | `89 [2:11001, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `67 [2:00011, 3:1]` | `53 [2:10101, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `75 [2:01011, 3:0]` | `65 [2:00001, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `83 [2:10011, 3:2]` | `77 [2:01101, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `91 [2:11011, 3:1]` | `41 [2:01001, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |
| `95 [2:11111, 3:2]` | `95 [2:11111, 3:2]` | 0.500000 | 0.020813 | 0.479187 | `1:1.000` |

## Interpretation

The affine skeleton gives a quotient-linear explanation of the sampled odd map only after we choose what information it is allowed to see.  A source-blind marginal is a strong null model at this coarse quotient; the meaningful test is whether resolving carry packets lets low-complexity affine pieces outperform that null.  If the carry-sliced row lowers Fisher energy, the nonlinear part is being carried by discrete 2-adic depth rather than by featureless noise.  If it does not, this quotient is still too coarse or the affine family is too weak.

The exact carry-lift audit is the reverse-engineering payload: source-only quotient rows are many-valued, but after adjoining `k mod 2^s` every sampled lift cell is deterministic and the divided affine formula has no failures.  That identifies the missing coordinate rather than merely measuring residual size.

In the manuscript vocabulary, this is the Collatz analogue of isolating a mixed tame/wild obstruction: the visible affine numerator is the tame-looking part, and the variable 2-adic carry is the wild depth packet that survives linearization.

## Reproduction

```powershell
python empirical/collatz_curvature_linearization.py --two-bits 5 --three-pow 1 --lift-bits 10
```
