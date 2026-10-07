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

- label: `(n mod 2^4, n mod 3^1)`
- combined modulus: `48`
- occupied labels on this orbit: `32` of `48`
- projected transition edges used: `43`

Top projected transitions:

- `2:1110|3:1 -> 2:0111|3:2`: `6`
- `2:0111|3:2 -> 2:0110|3:1`: `6`
- `2:0010|3:1 -> 2:1001|3:2`: `5`
- `2:1001|3:2 -> 2:1100|3:1`: `5`
- `2:1100|3:1 -> 2:1110|3:2`: `4`
- `2:1110|3:1 -> 2:1111|3:2`: `4`
- `2:1111|3:2 -> 2:1110|3:1`: `4`
- `2:0110|3:1 -> 2:1011|3:2`: `4`
- `2:1011|3:2 -> 2:0010|3:1`: `4`
- `2:0100|3:1 -> 2:0010|3:2`: `4`
- `2:1110|3:2 -> 2:1111|3:1`: `3`
- `2:1111|3:1 -> 2:1110|3:1`: `3`
- `2:0100|3:1 -> 2:1010|3:2`: `3`
- `2:1000|3:1 -> 2:1100|3:2`: `3`
- `2:1100|3:2 -> 2:1110|3:1`: `3`
- `2:0110|3:1 -> 2:0011|3:2`: `3`

Transition matrix on occupied labels:

```text
      0:1  0:2  1:1  1:2  2:1  2:2  3:2  4:1  4:2  5:1  5:2  6:1  6:2  7:1  7:2  8:1  8:2  9:1  9:2 10:1 10:2 11:0 11:1 11:2 12:1 12:2 13:1 13:2 14:1 14:2 15:1 15:2
 0:1    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 0:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 1:1    .    .    .    .    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 1:2    .    .    .    .    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 2:1    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    5    .    .    .    .    .    .    .    .    .    .    .    .    .
 2:2    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 3:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .
 4:1    .    .    .    .    .    4    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .
 4:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .
 5:1    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 5:2    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 6:1    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    4    .    .    .    .    .    .    .    .
 6:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    2    .    .    .    .    .    .    .    .    .
 7:1    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 7:2    .    .    .    .    .    .    .    .    .    .    .    6    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 8:1    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .    .    .    .
 8:2    .    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
 9:1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .
 9:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    5    .    .    .    .    .    .    .
10:1    .    .    .    .    .    .    .    .    .    .    3    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .
10:2    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    2    .    .    .    .    .
11:0    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
11:1    .    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
11:2    .    .    .    .    4    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
12:1    .    .    .    .    .    .    .    .    .    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    4    .    .
12:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .
13:1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
13:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .
14:1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    6    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    4
14:2    .    .    .    .    .    .    .    .    .    .    .    .    .    1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .
15:1    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    3    .    .    .
15:2    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    .    4    .    .    .

Legend: row/column labels are residue2:residue3.
Full labels: 0:1=2:0000|3:1, 0:2=2:0000|3:2, 1:1=2:0001|3:1, 1:2=2:0001|3:2, 2:1=2:0010|3:1, 2:2=2:0010|3:2, 3:2=2:0011|3:2, 4:1=2:0100|3:1, 4:2=2:0100|3:2, 5:1=2:0101|3:1, 5:2=2:0101|3:2, 6:1=2:0110|3:1, 6:2=2:0110|3:2, 7:1=2:0111|3:1, 7:2=2:0111|3:2, 8:1=2:1000|3:1, 8:2=2:1000|3:2, 9:1=2:1001|3:1, 9:2=2:1001|3:2, 10:1=2:1010|3:1, 10:2=2:1010|3:2, 11:0=2:1011|3:0, 11:1=2:1011|3:1, 11:2=2:1011|3:2, 12:1=2:1100|3:1, 12:2=2:1100|3:2, 13:1=2:1101|3:1, 13:2=2:1101|3:2, 14:1=2:1110|3:1, 14:2=2:1110|3:2, 15:1=2:1111|3:1, 15:2=2:1111|3:2
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

- raw relation sources: `48`
- deterministic sources: `24`
- ambiguous sources: `24`
- closure deficit: `24`
- outdegree distribution: `{1: 24, 2: 24}`
- mean row entropy: `0.500000` bits

For the accelerated odd map, the script samples all lifts modulo `2^8` hidden lift bits over the same quotient.

- odd relation sources: `24`
- deterministic odd sources: `0`
- ambiguous odd sources: `24`
- accelerated closure deficit: `96`
- odd outdegree distribution: `{2: 12, 4: 6, 8: 3, 16: 3}`
- mean odd row entropy: `1.864530` bits
- max odd row entropy: `3.916241` bits

Most ambiguous accelerated sources:

- source `5`: targets `1:22, 5:11, 7:22, 11:11, 13:21, 17:11, 19:22, 23:10, 25:21, 29:11, 31:21, 35:10, 37:21, 41:10, 43:21, 47:11`, carry depths `4:128, 5:64, 6:32, 7:16, 8:8, 9:4, 10:2, 11:1, 12:1`, entropy `3.916241`
- source `21`: targets `1:22, 5:11, 7:21, 11:11, 13:22, 17:11, 19:21, 23:11, 25:21, 29:10, 31:22, 35:11, 37:21, 41:10, 43:21, 47:10`, carry depths `4:128, 5:64, 6:32, 7:16, 8:8, 9:4, 10:2, 11:1, 12:1`, entropy `3.916241`
- source `37`: targets `1:22, 5:11, 7:22, 11:11, 13:21, 17:11, 19:21, 23:11, 25:22, 29:10, 31:21, 35:10, 37:21, 41:11, 43:21, 47:10`, carry depths `4:128, 5:64, 6:32, 7:16, 8:8, 9:4, 10:2, 11:1, 14:1`, entropy `3.916241`
- source `13`: targets `5:32, 11:32, 17:32, 23:32, 29:32, 35:32, 41:32, 47:32`, carry depths `3:256`, entropy `3.000000`
- source `29`: targets `5:32, 11:32, 17:32, 23:32, 29:32, 35:32, 41:32, 47:32`, carry depths `3:256`, entropy `3.000000`
- source `45`: targets `5:32, 11:32, 17:32, 23:32, 29:32, 35:32, 41:32, 47:32`, carry depths `3:256`, entropy `3.000000`
- source `1`: targets `1:64, 13:64, 25:64, 37:64`, carry depths `2:256`, entropy `2.000000`
- source `9`: targets `7:64, 19:64, 31:64, 43:64`, carry depths `2:256`, entropy `2.000000`

## Range Sweep

- starts swept: `1..10000`
- ended at one within budget: `10000`
- not ended within budget: `0`
- total raw steps: `849666`
- max value seen: `27114424`
- mean stopping time among ended starts: `84.966600`
- max stopping time among ended starts: `261`
- carry distribution: `{1: 141827, 2: 65428, 3: 34775, 4: 27600, 5: 8082, 6: 2310, 7: 1023, 8: 456, 9: 104, 10: 388, 11: 12, 12: 13, 14: 2, 15: 2}`

## Interpretation

The low-dimensional mod-2/mod-3 picture is the entrance ramp, but the nontrivial object is the lift-sensitive relation.  The raw map exposes a predictable division-by-2 ambiguity, while the accelerated odd map records the variable carry depth created by `3n+1`.  That is the Collatz version of a discrete skeleton: finite categorical labels, transition operators, and explicit carry data instead of a smoothed curve.

## Reproduction

```powershell
python empirical/collatz_arithmetic_skeleton.py --start 27 --two-bits 4 --three-pow 1 --lift-bits 8
python empirical/collatz_arithmetic_skeleton.py --start 27 --two-bits 4 --three-pow 1 --range-limit 10000
```
