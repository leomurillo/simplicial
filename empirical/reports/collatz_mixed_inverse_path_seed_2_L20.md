# Collatz Mixed 2/3 Inverse Path Algebra

## Meaning

This is the flipped object.  Binary support paths are cheap because both formal branches are defined in `Z[1/3]`.  Honest integer inverse paths require two filters at every `U` branch:

```text
3-adic: x = 1 mod 3 so (x - 1)/3 is an integer.
2-adic: x = 4 mod 6 so that integer is odd.
```

Thus the algebra is mixed: `D` is a 2-adic even-preimage lift, while `U` is a 3-adic filtered division with a 2-adic parity gate.

## Path Ledger

- seed: `2`
- max length: `20`
- final support words: `1048576`
- final integer words: `355`
- final honest inverse words: `179`
- final honest density: `0.000170707703`

| L | support words | integer words | honest words | integer density | honest density | distinct honest endpoints |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 0.500000000000 | 0.500000000000 | 1 |
| 2 | 4 | 2 | 2 | 0.500000000000 | 0.500000000000 | 2 |
| 3 | 8 | 3 | 2 | 0.375000000000 | 0.250000000000 | 2 |
| 4 | 16 | 4 | 3 | 0.250000000000 | 0.187500000000 | 3 |
| 5 | 32 | 5 | 4 | 0.156250000000 | 0.125000000000 | 4 |
| 8 | 256 | 12 | 10 | 0.046875000000 | 0.039062500000 | 10 |
| 10 | 1024 | 22 | 15 | 0.021484375000 | 0.014648437500 | 15 |
| 12 | 4096 | 39 | 26 | 0.009521484375 | 0.006347656250 | 26 |
| 14 | 16384 | 66 | 44 | 0.004028320312 | 0.002685546875 | 44 |
| 16 | 65536 | 115 | 69 | 0.001754760742 | 0.001052856445 | 69 |
| 18 | 262144 | 200 | 113 | 0.000762939453 | 0.000431060791 | 113 |
| 20 | 1048576 | 355 | 179 | 0.000338554382 | 0.000170707703 | 179 |

## U-Branch Gate Ledger

The `U` branch is where the mixed closure lives.  `U 3-adic pass` counts integer parents with `x = 1 mod 3`; `U honest pass` is the stricter `x = 4 mod 6`; `U parity fail` is the integer-but-not-Collatz branch.

| L | U from integer | U 3-adic pass | U parity fail | U honest pass | U from noninteger |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 1 | 1 |
| 3 | 2 | 1 | 1 | 0 | 2 |
| 4 | 3 | 1 | 0 | 1 | 5 |
| 5 | 4 | 1 | 0 | 1 | 12 |
| 8 | 9 | 3 | 0 | 3 | 119 |
| 10 | 17 | 5 | 0 | 5 | 495 |
| 12 | 28 | 11 | 3 | 8 | 2020 |
| 14 | 50 | 16 | 2 | 14 | 8142 |
| 16 | 87 | 28 | 6 | 22 | 32681 |
| 18 | 153 | 47 | 8 | 39 | 130919 |
| 20 | 267 | 88 | 20 | 68 | 524021 |

## Finite Quotient Adjacency

At `M = 2^a 3^b`, `D` is same-level and single-valued.  `U` is not: a source residue modulo `M` has three lifts modulo `3M`, and those lifts can land in three different target residues modulo `M`.  The filtered closed arrow is `R/(3M) -> R/M`.

| 2^a | 3^b | M | U sources | U full lift arrows | U target width | closure deficit | U targets |
|---:|---:|---:|---:|---:|---|---:|---:|
| 1 | 1 | 6 | 1 | 3 | 3:1 | 0.666667 | 3 |
| 2 | 1 | 12 | 2 | 6 | 3:2 | 0.666667 | 6 |
| 3 | 2 | 72 | 12 | 36 | 3:12 | 0.666667 | 36 |
| 4 | 3 | 432 | 72 | 216 | 3:72 | 0.666667 | 216 |
| 5 | 3 | 864 | 144 | 432 | 3:144 | 0.666667 | 432 |

## Gauge Sections

A gauge is a section choice for the filtered `U` source lift.  For a legal coarse source `r mod M`, the three lifts `r`, `r+M`, and `r+2M` give targets separated by `M/3`.  Choosing one lift turns `U` into a deterministic representative; changing the section adds the constant `Z/3` phase.

| M | gauge group | target shift | gauge orbits | gauge-reduced targets | gauge-reduced deficit |
|---:|---|---:|---:|---:|---:|
| 6 | Z/3 | 2 | 1 | 1 | 0.000000 |
| 12 | Z/3 | 4 | 2 | 2 | 0.000000 |
| 72 | Z/3 | 24 | 12 | 12 | 0.000000 |
| 432 | Z/3 | 144 | 72 | 72 | 0.000000 |
| 864 | Z/3 | 288 | 144 | 144 | 0.000000 |

Sample section targets for the largest quotient audit:

| source mod 864 | gauge 0 | gauge 1 | gauge 2 | orbit mod 288 |
|---:|---:|---:|---:|---:|
| 4 | 1 | 289 | 577 | 1 |
| 10 | 3 | 291 | 579 | 3 |
| 16 | 5 | 293 | 581 | 5 |
| 22 | 7 | 295 | 583 | 7 |
| 28 | 9 | 297 | 585 | 9 |
| 34 | 11 | 299 | 587 | 11 |
| 40 | 13 | 301 | 589 | 13 |
| 46 | 15 | 303 | 591 | 15 |
| 52 | 17 | 305 | 593 | 17 |
| 58 | 19 | 307 | 595 | 19 |
| 64 | 21 | 309 | 597 | 21 |
| 70 | 23 | 311 | 599 | 23 |

## Integer Cycles In All Z

These are the calibration components for the global integer dynamics.

| cycle | length | verified |
|---|---:|---|
| `0` | 1 | True |
| `1, 4, 2` | 3 | True |
| `-1, -2` | 2 | True |
| `-5, -14, -7, -20, -10` | 5 | True |
| `-17, -50, -25, -74, -37, -110, -55, -164, -82, -41, -122, -61, -182, -91, -272, -136, -68, -34` | 18 | True |

## Interpretation

This is the paper-style closure deficit in Collatz clothing.  If we keep only binary support, every word exists.  If we keep `Z[1/3]`, most words acquire a 3-denominator defect.  If we keep integers, many remaining words are still parity-wrong.  If we keep honest inverse-Collatz paths, the tree is governed by a filtered quotient algebra where `U` consumes one extra 3-adic digit and checks one 2-adic parity bit.

The next theorem candidate becomes:

```text
In the mixed inverse path algebra, every infinite honest integer path
is contained in the inverse basin of one of the five integer cycles;
all other binary support paths acquire a finite 3-adic denominator
defect or a 2-adic parity defect.
```

This is stronger and cleaner than a purely 2-adic no-descent statement: it makes the missing prime part of the state space.

## Reproduction

```powershell
python empirical/collatz_mixed_inverse_path_algebra.py --seed 2 --max-length 20 --quotient-pairs 1:1 2:1 3:2 4:3 5:3
```
