# Collatz Contracting Exception Sieve

## Status

This report enumerates bounded carry words and classifies the exact finite nondecrease exceptions in each contracting domain cylinder.

- max length: `6`
- max total carry depth: `12`
- max carry per step: `unbounded`
- max exception representatives certified per word: `128`
- max tail steps per representative: `2000`

## Decision Rule

For `2^S > 3^m`, the whole cylinder is decreasing after the word when

```text
r_w (2^S - 3^m) - C_w > 0.
```

If the margin is nonpositive, the sieve lists the finite representatives and tries to certify each one by hitting the `1` cycle or descending below its starting value.

## Totals

| category | all words | primitive words |
|---|---:|---:|
| expanding | 128 | 116 |
| contracting-all-decrease | 2375 | 2341 |
| trivial-cycle-exception | 6 | 1 |
| trivial-basin-exception | 0 | 0 |
| descent-certified-exception | 0 | 0 |
| unknown-exception | 0 | 0 |

- total words: `2509`
- primitive words: `2458`
- finite exception representatives: `6`
- unknown exception representatives: `0`
- primitive unknown exception representatives: `0`

## Pair Hotspots

| m,S | words | all-decrease | finite-exception reps | unknown reps | primitive unknown reps |
|---|---:|---:|---:|---:|---:|
| 6,12 | 462 | 461 | 1 | 0 | 0 |
| 5,10 | 126 | 125 | 1 | 0 | 0 |
| 4,8 | 35 | 34 | 1 | 0 | 0 |
| 3,6 | 10 | 9 | 1 | 0 | 0 |
| 2,4 | 3 | 2 | 1 | 0 | 0 |
| 1,2 | 1 | 0 | 1 | 0 | 0 |
| 5,12 | 330 | 330 | 0 | 0 | 0 |
| 6,11 | 252 | 252 | 0 | 0 | 0 |
| 5,11 | 210 | 210 | 0 | 0 | 0 |
| 4,12 | 165 | 165 | 0 | 0 | 0 |
| 6,10 | 126 | 126 | 0 | 0 | 0 |
| 4,11 | 120 | 120 | 0 | 0 | 0 |
| 4,10 | 84 | 84 | 0 | 0 | 0 |
| 5,9 | 70 | 70 | 0 | 0 | 0 |
| 4,9 | 56 | 56 | 0 | 0 | 0 |
| 6,9 | 56 | 0 | 0 | 0 | 0 |
| 3,12 | 55 | 55 | 0 | 0 | 0 |
| 3,11 | 45 | 45 | 0 | 0 | 0 |
| 3,10 | 36 | 36 | 0 | 0 | 0 |
| 5,8 | 35 | 35 | 0 | 0 | 0 |

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

## Closest All-Decrease Margins

Small score means the first admissible representative barely clears the nondecrease cap.

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 6.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.584963 | 4.247928 | `(1 3 1)` |
| 6.000000 | contracting-all-decrease | 1 | 3 | 1.415037 | True | 0 | None | -inf | 3.700440 | `(3)` |
| 6.000000 | contracting-all-decrease | 2 | 5 | 1.830075 | True | 0 | None | -inf | 1.584963 | `(1 4)` |
| 6.000000 | contracting-all-decrease | 1 | 4 | 2.415037 | True | 0 | None | -inf | 2.321928 | `(4)` |
| 7.000000 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.807355 | 5.044394 | `(2^2 1)` |
| 7.000000 | contracting-all-decrease | 2 | 4 | 0.830075 | True | 0 | None | -inf | 4.247928 | `(1 3)` |
| 7.584963 | contracting-all-decrease | 2 | 4 | 0.830075 | True | 0 | None | 0.000000 | 4.857981 | `(3 1)` |
| 7.584963 | contracting-all-decrease | 3 | 5 | 0.245112 | True | 0 | None | 2.000000 | 5.426265 | `(1 2^2)` |

## Largest Contracting Caps

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 6.426265 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 6.426265 | 7.366322 | `(4 1^4)` |
| 6.108524 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 6.108524 | 6.768184 | `(3 2 1^3)` |
| 5.930737 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.930737 | 8.396605 | `(2 3 1^3)` |
| 5.857981 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.857981 | 8.689998 | `(3 1 2 1^2)` |
| 5.832890 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.832890 | 8.816984 | `(1 4 1^3)` |
| 5.672425 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.672425 | 8.797662 | `(3 1^2 2 1)` |
| 5.643856 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.643856 | 7.011227 | `(2^3 1^2)` |
| 5.523562 | contracting-all-decrease | 5 | 8 | 0.075187 | True | 0 | None | 5.523562 | 6.965784 | `(3 1^3 2)` |

## Largest Certified Tail Values

| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |
|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|
| 0.000000 | trivial-cycle-exception | 1 | 2 | 0.415037 | True | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2)` |
| 0.000000 | trivial-cycle-exception | 2 | 4 | 0.830075 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^2)` |
| 0.000000 | trivial-cycle-exception | 3 | 6 | 1.245112 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^3)` |
| 0.000000 | trivial-cycle-exception | 4 | 8 | 1.660150 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^4)` |
| 0.000000 | trivial-cycle-exception | 5 | 10 | 2.075187 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^5)` |
| 0.000000 | trivial-cycle-exception | 6 | 12 | 2.490225 | False | 1 | trivial-cycle | 0.000000 | 0.000000 | `(2^6)` |

## Interpretation

This is the proof-shaped blindspot audit.  The average contraction and the intercept tail are no longer separate summaries: every contracting word is forced through its exact residue cylinder, and every surviving exception representative is either certified by descent, certified into the trivial basin, or left in the unknown bucket.

An empty primitive-unknown bucket in a bounded window does not prove Collatz.  It does, however, identify the algebra that a proof must control: the integer margin `r_w(2^S-3^m)-C_w` plus a descent certificate for the finite representatives when that margin is nonpositive.

## Reproduction

```powershell
python empirical/collatz_exception_sieve.py --max-length 6 --max-total-depth 12 --max-exception-reps 128 --max-tail-steps 2000
```
