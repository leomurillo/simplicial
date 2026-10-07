# Collatz Arithmetic Skeleton: start 27

## Status

This is a finite arithmetic projection of one Collatz orbit.  It is meant to expose the discrete carry structure; it is not evidence of a proof by itself.

- raw stopping steps: `111`
- ended at one within budget: `True`
- end value: `1`
- max value: `9232`
- accelerated odd bursts: `41`
- initial halving depth: `0`
- max odd carry depth v2(3n+1): `5`
- mean odd carry depth: `1.707317`
- mean odd log2 gain after full odd burst: `-0.115973`

## Quotient Simplex

- label: `(n mod 2^1, n mod 3^1)`
- combined modulus: `6`
- occupied labels on this orbit: `5` of `6`
- projected transition edges used: `7`

Top projected transitions:

- `2:0|3:1 -> 2:1|3:2`: `28`
- `2:1|3:2 -> 2:0|3:1`: `28`
- `2:0|3:1 -> 2:0|3:2`: `21`
- `2:0|3:2 -> 2:1|3:1`: `13`
- `2:1|3:1 -> 2:0|3:1`: `12`
- `2:0|3:2 -> 2:0|3:1`: `8`
- `2:1|3:0 -> 2:0|3:1`: `1`

Transition matrix on occupied labels:

```text
    0:1 0:2 1:0 1:1 1:2
0:1   .  21   .   .  28
0:2   8   .   .  13   .
1:0   1   .   .   .   .
1:1  12   .   .   .   .
1:2  28   .   .   .   .

Legend: row/column labels are residue2:residue3.
Full labels: 0:1=2:0|3:1, 0:2=2:0|3:2, 1:0=2:1|3:0, 1:1=2:1|3:1, 1:2=2:1|3:2
```

## Odd Carry Depths

The odd operation is recorded as `n -> (3n+1)/2^s`, where `s=v2(3n+1)`.  This is the local 2-adic carry packet that a smooth interpolation tends to hide.

| carry depth s | count |
|---:|---:|
| 1 | 24 |
| 2 | 10 |
| 3 | 3 |
| 4 | 3 |
| 5 | 1 |

Carry depth split by `n mod 3^1`:

| residue | depth counts |
|---:|---|
| 0 | `1:1` |
| 1 | `1:6, 2:3, 3:2, 4:1` |
| 2 | `1:17, 2:7, 3:1, 4:2, 5:1` |

## Finite-Quotient Closure Deficit

A finite 2-adic quotient does not make the raw Collatz map closed: for an even residue, division by 2 needs one hidden lift bit.  The count below measures that missing lift information as a relation rather than forcing a false function.

- raw relation sources: `6`
- deterministic sources: `3`
- ambiguous sources: `3`
- closure deficit: `3`
- outdegree distribution: `{1: 3, 2: 3}`
- mean row entropy: `0.500000` bits

For the accelerated odd map, the script samples all lifts modulo `2^8` hidden lift bits over the same quotient.

- odd relation sources: `3`
- deterministic odd sources: `0`
- ambiguous odd sources: `3`
- accelerated closure deficit: `3`
- odd outdegree distribution: `{2: 3}`
- mean odd row entropy: `0.919581` bits
- max odd row entropy: `0.920878` bits

Most ambiguous accelerated sources:

- source `1`: targets `1:85, 5:171`, carry depths `1:128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1, 9:1`, entropy `0.916988`
- source `3`: targets `1:86, 5:170`, carry depths `1:128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1, 12:1`, entropy `0.920878`
- source `5`: targets `1:86, 5:170`, carry depths `1:128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1, 10:1`, entropy `0.920878`

## Interpretation

The low-dimensional mod-2/mod-3 picture is the entrance ramp, but the nontrivial object is the lift-sensitive relation.  The raw map exposes a predictable division-by-2 ambiguity, while the accelerated odd map records the variable carry depth created by `3n+1`.  That is the Collatz version of a discrete skeleton: finite categorical labels, transition operators, and explicit carry data instead of a smoothed curve.

## Reproduction

```powershell
python empirical/collatz_arithmetic_skeleton.py --start 27 --two-bits 1 --three-pow 1 --lift-bits 8
python empirical/collatz_arithmetic_skeleton.py --start 27 --two-bits 4 --three-pow 1 --range-limit 10000
```
