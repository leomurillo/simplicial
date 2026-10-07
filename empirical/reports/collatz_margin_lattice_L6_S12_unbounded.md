# Collatz Margin Lattice Miner

## Stress Check From Old Notes

The old notes are cycle-side notes: they reduce periodic obstructions to the path-sum divisibility condition and warn that small-modulus/canonical-coset structure is mostly a mirage.  This report therefore does not canonicalize carry words and does not look for a small-prime obstruction.  It mines the exact domain inequality for every linear carry word in the window.

The cycle-side zero condition remains hard globally.  What is new here is the descent-side lattice: once a contracting word is not exactly zero-margin, the margin cannot be close to zero.

## Lattice Lemma

For a contracting word, set `D = 2^S - 3^m`, `M = 2^(S+1)`, and choose the exact domain residue `r` with

```text
3^m r + C_w == 2^S mod 2^(S+1).
```

Then

```text
margin(w) = rD - C_w
q_w       = margin(w) / 2^(S+1)  is an integer.
```

So a nonzero margin has an automatic gap of at least one full domain modulus.  The remaining proof-facing sign question is whether nontrivial contracting words ever have `q_w <= 0`.

## Settings

- max length: `6`
- max total carry depth: `12`
- max carry per step: `unbounded`
- expanding words skipped: `128`

## Totals

- contracting words: `2381`
- primitive contracting words: `2342`
- positive q: `2375`
- zero q: `6`
- trivial zero q: `6`
- nontrivial zero q: `0`
- negative q: `0`
- primitive zero q: `1`
- primitive negative q: `0`

## Length Envelope

| m | contracting | positive q | zero q | negative q | min q | min gap | gcd positive q | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 11 | 10 | 1 | 0 | 2 | 5 | 2 | `(4)` |
| 2 | 63 | 62 | 1 | 0 | 1 | 3 | 1 | `(1 4)` |
| 3 | 216 | 215 | 1 | 0 | 1 | 3 | 1 | `(1 3 1)` |
| 4 | 480 | 479 | 1 | 0 | 1 | 3 | 1 | `(1^2 2 3)` |
| 5 | 771 | 770 | 1 | 0 | 1 | 3 | 1 | `(2 1^2 3 1)` |
| 6 | 840 | 839 | 1 | 0 | 5 | 25 | 1 | `(1^2 2 1 4 1)` |

## Pair Envelope Hotspots

| m,S | contracting | positive q | zero q | negative q | min q | min gap | gcd q | min-q word |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 5,11 | 210 | 210 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^3)` |
| 4,9 | 56 | 56 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^2)` |
| 5,8 | 35 | 35 | 0 | 0 | 1 | 40 | 1 | `(2 1^2 3 1)` |
| 4,7 | 20 | 20 | 0 | 0 | 1 | 6 | 1 | `(1^2 2 3)` |
| 3,7 | 15 | 15 | 0 | 0 | 1 | 3 | 1 | `(1 4 2)` |
| 3,5 | 6 | 6 | 0 | 0 | 1 | 13 | 1 | `(1 3 1)` |
| 2,5 | 4 | 4 | 0 | 0 | 1 | 3 | 1 | `(1 4)` |
| 5,12 | 330 | 330 | 0 | 0 | 2 | 5 | 1 | `(4 2^4)` |
| 4,10 | 84 | 84 | 0 | 0 | 2 | 5 | 1 | `(4 2^3)` |
| 5,9 | 70 | 70 | 0 | 0 | 2 | 8 | 1 | `(2 1^2 2 3)` |
| 3,8 | 21 | 21 | 0 | 0 | 2 | 5 | 1 | `(4 2^2)` |
| 2,6 | 5 | 5 | 0 | 0 | 2 | 5 | 1 | `(4 2)` |
| 1,4 | 1 | 1 | 0 | 0 | 2 | 5 | 2 | `(4)` |
| 3,6 | 10 | 9 | 1 | 0 | 3 | 11 | 1 | `(1 2 3)` |
| 2,4 | 3 | 2 | 1 | 0 | 4 | 19 | 2 | `(1 3)` |
| 1,3 | 1 | 1 | 0 | 0 | 4 | 13 | 4 | `(3)` |
| 6,10 | 126 | 126 | 0 | 0 | 5 | 35 | 1 | `(1^2 2 1 4 1)` |
| 4,8 | 35 | 34 | 1 | 0 | 5 | 15 | 1 | `(1^3 5)` |
| 4,11 | 120 | 120 | 0 | 0 | 6 | 13 | 1 | `(3 4 2^2)` |
| 3,9 | 28 | 28 | 0 | 0 | 6 | 13 | 1 | `(3 4 2)` |
| 2,7 | 6 | 6 | 0 | 0 | 6 | 13 | 1 | `(3 4)` |
| 5,10 | 126 | 125 | 1 | 0 | 7 | 19 | 1 | `(1 3 1 2 3)` |
| 6,12 | 462 | 461 | 1 | 0 | 10 | 25 | 1 | `(2 1 3 1 2 3)` |
| 6,11 | 252 | 252 | 0 | 0 | 10 | 32 | 1 | `(2^2 1 3 1 2)` |

## Smallest Positive q

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 1.000000 | positive-margin | 4 | 7 | 0.660150 | 1 | 6 | 0.000000 | 2.807355 | True | `(1^2 2 3)` |
| 1.000000 | positive-margin | 3 | 5 | 0.245112 | 1 | 13 | 2.584963 | 4.247928 | True | `(1 3 1)` |
| 1.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 1.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 6.108524 | 6.768184 | True | `(3 2 1^3)` |
| 1.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |
| 1.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 1.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 5.044394 | 6.189825 | True | `(2 1^2 3 1)` |

## Smallest Gap To Cap

Here `gap = first admissible n - floor(C_w / D)`.  Positive margins force `gap >= ceil(2^(S+1)/D)`, so even the nearest descent cases clear the cap by multiple integers.

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 3.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |
| 3.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 3.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 3.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 5.000000 | positive-margin | 1 | 4 | 2.415037 | 2 | 5 | -inf | 2.321928 | True | `(4)` |
| 5.000000 | positive-margin | 3 | 8 | 3.245112 | 2 | 5 | -inf | 2.321928 | True | `(4 2^2)` |
| 5.000000 | positive-margin | 2 | 6 | 2.830075 | 2 | 5 | -inf | 2.321928 | True | `(4 2)` |
| 5.000000 | positive-margin | 4 | 10 | 3.660150 | 2 | 5 | -inf | 2.321928 | True | `(4 2^3)` |

## q = 1 Witnesses

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 5.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 5.000000 | positive-margin | 3 | 5 | 0.245112 | 1 | 13 | 2.584963 | 4.247928 | True | `(1 3 1)` |
| 7.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 7.000000 | positive-margin | 4 | 7 | 0.660150 | 1 | 6 | 0.000000 | 2.807355 | True | `(1^2 2 3)` |
| 8.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 5.044394 | 6.189825 | True | `(2 1^2 3 1)` |
| 8.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 6.108524 | 6.768184 | True | `(3 2 1^3)` |
| 9.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 11.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |

## Nontrivial Zero q

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Negative q

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Largest Contracting Caps

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 6.426265 | positive-margin | 5 | 8 | 0.075187 | 2 | 79 | 6.426265 | 7.366322 | True | `(4 1^4)` |
| 6.108524 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 6.108524 | 6.768184 | True | `(3 2 1^3)` |
| 5.930737 | positive-margin | 5 | 8 | 0.075187 | 7 | 276 | 5.930737 | 8.396605 | True | `(2 3 1^3)` |
| 5.857981 | positive-margin | 5 | 8 | 0.075187 | 9 | 355 | 5.857981 | 8.689998 | True | `(3 1 2 1^2)` |
| 5.832890 | positive-margin | 5 | 8 | 0.075187 | 10 | 394 | 5.832890 | 8.816984 | True | `(1 4 1^3)` |
| 5.672425 | positive-margin | 5 | 8 | 0.075187 | 10 | 394 | 5.672425 | 8.797662 | True | `(3 1^2 2 1)` |
| 5.643856 | positive-margin | 5 | 8 | 0.075187 | 2 | 79 | 5.643856 | 7.011227 | True | `(2^3 1^2)` |
| 5.523562 | positive-margin | 5 | 8 | 0.075187 | 2 | 79 | 5.523562 | 6.965784 | True | `(3 1^3 2)` |

## Interpretation

The computation separates the descent problem into a clean trichotomy.  `q_w = 0` is the cycle obstruction.  `q_w < 0` would be a finite nondecrease packet.  `q_w > 0` means the entire exact cylinder decreases after the word.

In this window, the only zero margins are the trivial `(2)^m` words and there are no negative margins.  Combined with the old notes, this says the next real theorem candidate is not a small modular obstruction.  It is a sign theorem for the domain-lattice quotient `q_w`, with the cycle-zero case explicitly separated.

## Reproduction

```powershell
python empirical/collatz_margin_lattice_miner.py --max-length 6 --max-total-depth 12 --top-limit 8
```
