# Collatz Curvature Linearization: 2^4 x 3^1

## Status

This report samples the accelerated odd Collatz map on a finite quotient simplex, fits an affine-convolution linear skeleton, and measures the residual as carry-depth curvature.

- modulus: `48`
- odd residue states: `24`
- hidden lifts per state: `1024`
- total samples: `24576`
- fitted affine image size: `12` of `24` odd states
- true-kernel outdegree distribution: `{2: 12, 4: 6, 8: 3, 16: 3}`
- mean true row entropy: `1.864740` bits
- max true row entropy: `3.917923` bits

## Linear Skeleton Fit

The null model is the source-blind target marginal.  The seed model uses the visible affine numerator `3n+1`.  The fitted model searches source-sensitive affine bases `A*n+B (mod Q)` and learns one translation-invariant residual packet over affine deltas.  The carry-sliced model repeats that affine fit separately inside each carry packet.

| model | A | B | mean Fisher energy | mean Fisher norm | max Fisher norm | mean Hellinger | mean L1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| source-blind null | 0 | 0 | 6.416840 | 2.353908 | 3.109270 | 0.660413 | 1.416748 |
| seed affine 3n+1 | 3 | 1 | 6.416840 | 2.353908 | 3.109270 | 0.660413 | 1.416748 |
| best affine-convolution | 2 | 0 | 7.083425 | 2.496224 | 3.316772 | 0.750522 | 1.583798 |
| same-base carry-conditioned affine | 2 | 0 | 7.083299 | 2.496147 | 3.316625 | 0.750500 | 1.583605 |
| carry-sliced affine | - | - | 6.750007 | 2.218264 | 3.316625 | 0.614296 | 1.333917 |
| exact carry-lift oracle | - | - | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

Same-base carry conditioning changes the fitted mean Fisher residual energy by `0.00%` relative to the best global affine-convolution model.
Carry-sliced affine linearization changes it by `4.71%`.
The exact carry-lift oracle keeps the hidden lift coordinate required by division by `2^s`, so its residual is zero by construction; the audit below records the coordinate cost.

Top deltas in the best global affine residual packet:

- delta `5`: `0.041707`
- delta `7`: `0.041707`
- delta `13`: `0.041707`
- delta `23`: `0.041707`
- delta `35`: `0.041707`
- delta `39`: `0.041707`
- delta `45`: `0.041707`
- delta `1`: `0.041667`
- delta `9`: `0.041667`
- delta `11`: `0.041667`
- delta `15`: `0.041667`
- delta `17`: `0.041667`

## Carry Packets

Each row below holds one carry channel `s = v2(3n+1)`.  The two residual columns compare the global affine model with a carry-conditioned affine model using the same fitted `A,B`.

| s | samples | sources hit | sliced A,B | image | global energy | same-base energy | sliced energy | sliced reduction | top sliced deltas |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 12288 | 12 | 1,0 | 12 | 132.000007 | 132.000000 | 132.000000 | 0.00% | `0:0.0417, 2:0.0417, 4:0.0417, 6:0.0417, 8:0.0417, 10:0.0417, 12:0.0417, 14:0.0417` |
| 2 | 6144 | 6 | 1,0 | 6 | 30.000003 | 30.000000 | 30.000000 | 0.00% | `0:0.0417, 2:0.0417, 4:0.0417, 6:0.0417, 8:0.0417, 10:0.0417, 12:0.0417, 14:0.0417` |
| 3 | 3072 | 3 | 0,0 | 1 | 6.000002 | 6.000000 | 0.000000 | 100.00% | `5:0.1250, 11:0.1250, 17:0.1250, 23:0.1250, 29:0.1250, 35:0.1250, 41:0.1250, 47:0.1250` |
| 4 | 1536 | 3 | 0,0 | 1 | 1.500000 | 1.500000 | 0.000000 | 100.00% | `1:0.1250, 7:0.1250, 13:0.1250, 19:0.1250, 25:0.1250, 31:0.1250, 37:0.1250, 43:0.1250` |
| 5 | 768 | 3 | 0,0 | 1 | 0.375000 | 0.375000 | 0.000000 | 100.00% | `5:0.1250, 11:0.1250, 17:0.1250, 23:0.1250, 29:0.1250, 35:0.1250, 41:0.1250, 47:0.1250` |
| 6 | 384 | 3 | 0,0 | 1 | 0.093750 | 0.093750 | 0.000000 | 100.00% | `1:0.1250, 7:0.1250, 13:0.1250, 19:0.1250, 25:0.1250, 31:0.1250, 37:0.1250, 43:0.1250` |
| 7 | 192 | 3 | 0,0 | 1 | 0.023438 | 0.023438 | 0.000000 | 100.00% | `5:0.1250, 11:0.1250, 17:0.1250, 23:0.1250, 29:0.1250, 35:0.1250, 41:0.1250, 47:0.1250` |
| 8 | 96 | 3 | 0,0 | 1 | 0.005859 | 0.005859 | 0.000000 | 100.00% | `1:0.1250, 7:0.1250, 13:0.1250, 19:0.1250, 25:0.1250, 31:0.1250, 37:0.1250, 43:0.1250` |
| 9 | 48 | 3 | 0,0 | 1 | 0.001465 | 0.001465 | 0.000000 | 100.00% | `5:0.1250, 11:0.1250, 17:0.1250, 23:0.1250, 29:0.1250, 35:0.1250, 41:0.1250, 47:0.1250` |
| 10 | 24 | 3 | 0,0 | 1 | 0.000366 | 0.000366 | 0.000000 | 100.00% | `1:0.1250, 7:0.1250, 13:0.1250, 19:0.1250, 25:0.1250, 31:0.1250, 37:0.1250, 43:0.1250` |
| 11 | 12 | 3 | 0,0 | 1 | 0.000229 | 0.000183 | 0.000122 | 46.66% | `5:0.1667, 11:0.1667, 17:0.1667, 23:0.1667, 29:0.0833, 35:0.0833, 41:0.0833, 47:0.0833` |
| 12 | 6 | 3 | 0,0 | 1 | 0.000126 | 0.000092 | 0.000092 | 27.26% | `1:0.1667, 7:0.1667, 13:0.1667, 19:0.1667, 25:0.1667, 31:0.1667` |
| 13 | 3 | 3 | 0,0 | 1 | 0.000066 | 0.000046 | 0.000046 | 30.43% | `5:0.3333, 11:0.3333, 17:0.3333` |
| 14 | 2 | 2 | 0,0 | 1 | 0.000044 | 0.000023 | 0.000023 | 47.82% | `1:0.5000, 7:0.5000` |
| 16 | 1 | 1 | 0,0 | 1 | 0.000022 | 0.000000 | 0.000000 | 100.00% | `1:1.0000` |

Global carry-depth distribution:

- `s=1`: `12288`
- `s=2`: `6144`
- `s=3`: `3072`
- `s=4`: `1536`
- `s=5`: `768`
- `s=6`: `384`
- `s=7`: `192`
- `s=8`: `96`
- `s=9`: `48`
- `s=10`: `24`
- `s=11`: `12`
- `s=12`: `6`
- `s=13`: `3`
- `s=14`: `2`
- `s=16`: `1`

## Exact Carry-Lift Formula

For `n = x + kQ` and `s = v2(3n+1)`, the exact lifted linearization is

```text
target = ((3 * (x + kQ) + 1) / 2^s) mod Q
```

At fixed `x` and `s`, the target is determined by the hidden residue `k mod 2^s`.  The table shows source-only ambiguity before retaining that coordinate, and deterministic lift cells after retaining it.

| s | samples | sources hit | source edges | mean source outdegree | max source outdegree | lift bits | full cycle sampled | lift cells | deterministic cells | max cell outdegree | formula failures |
|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 1 | 12288 | 12 | 24 | 2.000000 | 2 | 1 | True | 24 | 24 | 1 | 0 |
| 2 | 6144 | 6 | 24 | 4.000000 | 4 | 2 | True | 24 | 24 | 1 | 0 |
| 3 | 3072 | 3 | 24 | 8.000000 | 8 | 3 | True | 24 | 24 | 1 | 0 |
| 4 | 1536 | 3 | 24 | 8.000000 | 8 | 4 | True | 24 | 24 | 1 | 0 |
| 5 | 768 | 3 | 24 | 8.000000 | 8 | 5 | True | 24 | 24 | 1 | 0 |
| 6 | 384 | 3 | 24 | 8.000000 | 8 | 6 | True | 24 | 24 | 1 | 0 |
| 7 | 192 | 3 | 24 | 8.000000 | 8 | 7 | True | 24 | 24 | 1 | 0 |
| 8 | 96 | 3 | 24 | 8.000000 | 8 | 8 | True | 24 | 24 | 1 | 0 |
| 9 | 48 | 3 | 24 | 8.000000 | 8 | 9 | True | 24 | 24 | 1 | 0 |
| 10 | 24 | 3 | 24 | 8.000000 | 8 | 10 | True | 24 | 24 | 1 | 0 |
| 11 | 12 | 3 | 12 | 4.000000 | 4 | 11 | False | 12 | 12 | 1 | 0 |
| 12 | 6 | 3 | 6 | 2.000000 | 2 | 12 | False | 6 | 6 | 1 | 0 |
| 13 | 3 | 3 | 3 | 1.000000 | 1 | 13 | False | 3 | 3 | 1 | 0 |
| 14 | 2 | 2 | 2 | 1.000000 | 1 | 14 | False | 2 | 2 | 1 | 0 |
| 16 | 1 | 1 | 1 | 1.000000 | 1 | 16 | False | 1 | 1 | 1 | 0 |

## Largest Signed Residual Edges

Positive residual means the true sampled kernel puts more mass on the edge than the fitted global affine skeleton predicts; negative means the skeleton predicts mass that the sampled kernel does not use at that source.

| source | target | true | model | residual | true carry mix |
|---|---|---:|---:|---:|---|
| `3 [2:0011, 3:0]` | `5 [2:0101, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `7 [2:0111, 3:1]` | `35 [2:0011, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `11 [2:1011, 3:2]` | `41 [2:1001, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `15 [2:1111, 3:0]` | `23 [2:0111, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `23 [2:0111, 3:2]` | `35 [2:0011, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `39 [2:0111, 3:0]` | `11 [2:1011, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `43 [2:1011, 3:1]` | `41 [2:1001, 3:2]` | 0.500000 | 0.041626 | 0.458374 | `1:1.000` |
| `11 [2:1011, 3:2]` | `17 [2:0001, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `15 [2:1111, 3:0]` | `47 [2:1111, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `19 [2:0011, 3:1]` | `5 [2:0101, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `27 [2:1011, 3:0]` | `17 [2:0001, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `31 [2:1111, 3:1]` | `23 [2:0111, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `31 [2:1111, 3:1]` | `47 [2:1111, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `35 [2:0011, 3:2]` | `5 [2:0101, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `43 [2:1011, 3:1]` | `17 [2:0001, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |
| `47 [2:1111, 3:2]` | `23 [2:0111, 3:2]` | 0.500000 | 0.041667 | 0.458333 | `1:1.000` |

## Interpretation

The affine skeleton gives a quotient-linear explanation of the sampled odd map only after we choose what information it is allowed to see.  A source-blind marginal is a strong null model at this coarse quotient; the meaningful test is whether resolving carry packets lets low-complexity affine pieces outperform that null.  If the carry-sliced row lowers Fisher energy, the nonlinear part is being carried by discrete 2-adic depth rather than by featureless noise.  If it does not, this quotient is still too coarse or the affine family is too weak.

The exact carry-lift audit is the reverse-engineering payload: source-only quotient rows are many-valued, but after adjoining `k mod 2^s` every sampled lift cell is deterministic and the divided affine formula has no failures.  That identifies the missing coordinate rather than merely measuring residual size.

In the manuscript vocabulary, this is the Collatz analogue of isolating a mixed tame/wild obstruction: the visible affine numerator is the tame-looking part, and the variable 2-adic carry is the wild depth packet that survives linearization.

## Reproduction

```powershell
python empirical/collatz_curvature_linearization.py --two-bits 4 --three-pow 1 --lift-bits 10
```
