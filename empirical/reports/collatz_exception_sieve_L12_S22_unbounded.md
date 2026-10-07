# Collatz Contracting Exception Sieve

## Status

This report enumerates bounded carry words and classifies the exact finite nondecrease exceptions in each contracting domain cylinder.

- max length: `12`
- max total carry depth: `22`
- max carry per step: `unbounded`
- max exception representatives certified per word: `128`
- max tail steps per representative: `10000`

## Decision Rule

For `2^S > 3^m`, the whole cylinder is decreasing after the word when

```text
r_w (2^S - 3^m) - C_w > 0.
```

If the margin is nonpositive, the sieve lists the finite representatives and tries to certify each one by hitting the `1` cycle or descending below its starting value.

## Totals

| category | all words | primitive words |
|---|---:|---:|
| expanding | 68722 | 68570 |
| contracting-all-decrease | 3027780 | 3026352 |
| trivial-cycle-exception | 11 | 1 |
| trivial-basin-exception | 0 | 0 |
| descent-certified-exception | 0 | 0 |
| unknown-exception | 0 | 0 |

- total words: `3096513`
- primitive words: `3094923`
- finite exception representatives: `11`
- unknown exception representatives: `0`
- primitive unknown exception representatives: `0`

## Pair Hotspots

| m,S | words | all-decrease | finite-exception reps | unknown reps | primitive unknown reps |
|---|---:|---:|---:|---:|---:|
| 11,22 | 352716 | 352715 | 1 | 0 | 0 |
| 10,20 | 92378 | 92377 | 1 | 0 | 0 |
| 9,18 | 24310 | 24309 | 1 | 0 | 0 |
| 8,16 | 6435 | 6434 | 1 | 0 | 0 |
| 7,14 | 1716 | 1715 | 1 | 0 | 0 |
| 6,12 | 462 | 461 | 1 | 0 | 0 |
| 5,10 | 126 | 125 | 1 | 0 | 0 |
| 4,8 | 35 | 34 | 1 | 0 | 0 |
| 3,6 | 10 | 9 | 1 | 0 | 0 |
| 2,4 | 3 | 2 | 1 | 0 | 0 |
| 1,2 | 1 | 0 | 1 | 0 | 0 |
| 12,22 | 352716 | 352716 | 0 | 0 | 0 |
| 10,22 | 293930 | 293930 | 0 | 0 | 0 |
| 9,22 | 203490 | 203490 | 0 | 0 | 0 |
| 11,21 | 184756 | 184756 | 0 | 0 | 0 |
| 10,21 | 167960 | 167960 | 0 | 0 | 0 |
| 12,21 | 167960 | 167960 | 0 | 0 | 0 |
| 9,21 | 125970 | 125970 | 0 | 0 | 0 |
| 8,22 | 116280 | 116280 | 0 | 0 | 0 |
| 11,20 | 92378 | 92378 | 0 | 0 | 0 |

## Unknown Exceptions

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Primitive Unknown Exceptions

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Largest Exception Counts

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 1.000000 | trivial-cycle-exception | 1 | 2 | 0.415037 | True | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2)` |
| 1.000000 | trivial-cycle-exception | 2 | 4 | 0.830075 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^2)` |
| 1.000000 | trivial-cycle-exception | 3 | 6 | 1.245112 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^3)` |
| 1.000000 | trivial-cycle-exception | 4 | 8 | 1.660150 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^4)` |
| 1.000000 | trivial-cycle-exception | 5 | 10 | 2.075187 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^5)` |
| 1.000000 | trivial-cycle-exception | 6 | 12 | 2.490225 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^6)` |
| 1.000000 | trivial-cycle-exception | 7 | 14 | 2.905262 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^7)` |
| 1.000000 | trivial-cycle-exception | 8 | 16 | 3.320300 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^8)` |
| 1.000000 | trivial-cycle-exception | 9 | 18 | 3.735337 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^9)` |
| 1.000000 | trivial-cycle-exception | 10 | 20 | 4.150375 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^10)` |
| 1.000000 | trivial-cycle-exception | 11 | 22 | 4.565412 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^11)` |

## Closest All-Decrease Margins

Small score means the first admissible representative barely clears the nondecrease cap.

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 6.000000 | contracting-all-decrease | 1 | 4 | 2.415037 | True | 0 | None | -inf | 2.321928 | `(4)` |
| 6.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.584963 | 4.247928 | `(1 3 1)` |
| 6.000000 | contracting-all-decrease | 2 | 5 | 1.830075 | True | 0 | None | -inf | 1.584963 | `(1 4)` |
| 6.000000 | contracting-all-decrease | 1 | 3 | 1.415037 | True | 0 | None | -inf | 3.700440 | `(3)` |
| 7.000000 | contracting-all-decrease | 2 | 4 | 0.830075 | True | 0 | None | -inf | 4.247928 | `(1 3)` |
| 7.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.807355 | 5.044394 | `(2^2 1)` |
| 7.584963 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.000000 | 5.426265 | `(1 2^2)` |
| 7.584963 | contracting-all-decrease | 2 | 4 | 0.830075 | True | 0 | None | 0.000000 | 4.857981 | `(3 1)` |
| 8.000000 | contracting-all-decrease | 2 | 6 | 2.830075 | True | 0 | None | -inf | 2.321928 | `(4 2)` |
| 8.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 1.584963 | 5.781360 | `(1^2 3)` |
| 8.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.321928 | 5.832890 | `(2 1 2)` |
| 8.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 3.169925 | 5.930737 | `(3 1^2)` |

## Largest Contracting Caps

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 8.573647 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.573647 | 16.999527 | `(7 1^9)` |
| 8.303781 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.303781 | 16.636922 | `(6 2 1^8)` |
| 8.149747 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.149747 | 16.414504 | `(5 3 1^8)` |
| 8.092757 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.092757 | 15.243955 | `(6 1 2 1^7)` |
| 8.066089 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.066089 | 13.827045 | `(4^2 1^8)` |
| 8.016808 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 8.016808 | 15.414058 | `(3 5 1^8)` |
| 7.994353 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.994353 | 15.829351 | `(2 6 1^8)` |
| 7.982994 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.982994 | 16.999681 | `(1 7 1^8)` |
| 7.930737 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.930737 | 16.360110 | `(6 1^2 2 1^6)` |
| 7.912889 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.912889 | 14.565400 | `(5 2^2 1^7)` |
| 7.813781 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.813781 | 16.802781 | `(6 1^3 2 1^5)` |
| 7.807355 | contracting-all-decrease | 10 | 16 | 0.150375 | True | 0 | None | 7.807355 | 16.332124 | `(4 3 2 1^7)` |

## Largest Certified Tail Values

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 0.000000 | trivial-cycle-exception | 1 | 2 | 0.415037 | True | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2)` |
| 0.000000 | trivial-cycle-exception | 2 | 4 | 0.830075 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^2)` |
| 0.000000 | trivial-cycle-exception | 3 | 6 | 1.245112 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^3)` |
| 0.000000 | trivial-cycle-exception | 4 | 8 | 1.660150 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^4)` |
| 0.000000 | trivial-cycle-exception | 5 | 10 | 2.075187 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^5)` |
| 0.000000 | trivial-cycle-exception | 6 | 12 | 2.490225 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^6)` |
| 0.000000 | trivial-cycle-exception | 7 | 14 | 2.905262 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^7)` |
| 0.000000 | trivial-cycle-exception | 8 | 16 | 3.320300 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^8)` |
| 0.000000 | trivial-cycle-exception | 9 | 18 | 3.735337 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^9)` |
| 0.000000 | trivial-cycle-exception | 10 | 20 | 4.150375 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^10)` |
| 0.000000 | trivial-cycle-exception | 11 | 22 | 4.565412 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^11)` |

## Interpretation

This is the proof-shaped blindspot audit.  The average contraction and the intercept tail are no longer separate summaries: every contracting word is forced through its exact residue cylinder, and every surviving exception representative is either certified by descent, certified into the trivial basin, or left in the unknown bucket.

An empty primitive-unknown bucket in a bounded window does not prove Collatz.  It does, however, identify the algebra that a proof must control: the integer margin `r_w(2^S-3^m)-C_w` plus a descent certificate for the finite representatives when that margin is nonpositive.

## Reproduction

```powershell
python empirical/collatz_exception_sieve.py --max-length 12 --max-total-depth 22 --max-exception-reps 128 --max-tail-steps 10000
```
