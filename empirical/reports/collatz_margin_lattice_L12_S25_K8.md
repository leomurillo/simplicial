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

- max length: `12`
- max total carry depth: `25`
- max carry per step: `8`
- expanding words skipped: `68722`

## Totals

- contracting words: `15641778`
- primitive contracting words: `15639283`
- positive q: `15641766`
- zero q: `12`
- trivial zero q: `12`
- nontrivial zero q: `0`
- negative q: `0`
- primitive zero q: `1`
- primitive negative q: `0`

## Length Envelope

| m | contracting | positive q | zero q | negative q | min q | min gap | gcd positive q | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 7 | 6 | 1 | 0 | 2 | 5 | 2 | `(4)` |
| 2 | 61 | 60 | 1 | 0 | 1 | 3 | 1 | `(1 4)` |
| 3 | 508 | 507 | 1 | 0 | 1 | 3 | 1 | `(1 3 1)` |
| 4 | 3871 | 3870 | 1 | 0 | 1 | 3 | 1 | `(1^2 2 3)` |
| 5 | 23429 | 23428 | 1 | 0 | 1 | 3 | 1 | `(2 1^2 3 1)` |
| 6 | 104020 | 104019 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^4)` |
| 7 | 344990 | 344989 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^5)` |
| 8 | 886852 | 886851 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^6)` |
| 9 | 1822219 | 1822218 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^7)` |
| 10 | 3071277 | 3071276 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^8)` |
| 11 | 4308888 | 4308887 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^9)` |
| 12 | 5075656 | 5075655 | 1 | 0 | 1 | 3 | 1 | `(1 4 2^10)` |

## Pair Envelope Hotspots

| m,S | contracting | positive q | zero q | negative q | min q | min gap | gcd q | min-q word |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 12,25 | 2443728 | 2443728 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^10)` |
| 11,23 | 635635 | 635635 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^9)` |
| 10,21 | 165760 | 165760 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^8)` |
| 9,19 | 43353 | 43353 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^7)` |
| 8,17 | 11376 | 11376 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^6)` |
| 7,15 | 2996 | 2996 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^5)` |
| 6,13 | 792 | 792 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^4)` |
| 5,11 | 210 | 210 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^3)` |
| 4,9 | 56 | 56 | 0 | 0 | 1 | 3 | 1 | `(1 4 2^2)` |
| 5,8 | 35 | 35 | 0 | 0 | 1 | 40 | 1 | `(2 1^2 3 1)` |
| 4,7 | 20 | 20 | 0 | 0 | 1 | 6 | 1 | `(1^2 2 3)` |
| 3,7 | 15 | 15 | 0 | 0 | 1 | 3 | 1 | `(1 4 2)` |
| 3,5 | 6 | 6 | 0 | 0 | 1 | 13 | 1 | `(1 3 1)` |
| 2,5 | 4 | 4 | 0 | 0 | 1 | 3 | 1 | `(1 4)` |
| 11,24 | 1111033 | 1111033 | 0 | 0 | 2 | 5 | 1 | `(4 2^10)` |
| 10,22 | 286780 | 286780 | 0 | 0 | 2 | 5 | 1 | `(4 2^9)` |
| 9,20 | 74097 | 74097 | 0 | 0 | 2 | 5 | 1 | `(4 2^8)` |
| 8,18 | 19160 | 19160 | 0 | 0 | 2 | 5 | 1 | `(4 2^7)` |
| 7,16 | 4956 | 4956 | 0 | 0 | 2 | 5 | 1 | `(4 2^6)` |
| 6,14 | 1281 | 1281 | 0 | 0 | 2 | 5 | 1 | `(4 2^5)` |
| 5,12 | 330 | 330 | 0 | 0 | 2 | 5 | 1 | `(4 2^4)` |
| 4,10 | 84 | 84 | 0 | 0 | 2 | 5 | 1 | `(4 2^3)` |
| 5,9 | 70 | 70 | 0 | 0 | 2 | 8 | 1 | `(2 1^2 2 3)` |
| 3,8 | 21 | 21 | 0 | 0 | 2 | 5 | 1 | `(4 2^2)` |

## Smallest Positive q

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 1.000000 | positive-margin | 4 | 7 | 0.660150 | 1 | 6 | 0.000000 | 2.807355 | True | `(1^2 2 3)` |
| 1.000000 | positive-margin | 6 | 13 | 3.490225 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^4)` |
| 1.000000 | positive-margin | 3 | 5 | 0.245112 | 1 | 13 | 2.584963 | 4.247928 | True | `(1 3 1)` |
| 1.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 1.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 5.044394 | 6.189825 | True | `(2 1^2 3 1)` |
| 1.000000 | positive-margin | 7 | 15 | 3.905262 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^5)` |
| 1.000000 | positive-margin | 11 | 23 | 5.565412 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^9)` |
| 1.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 6.108524 | 6.768184 | True | `(3 2 1^3)` |
| 1.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 1.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |
| 1.000000 | positive-margin | 10 | 21 | 5.150375 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^8)` |
| 1.000000 | positive-margin | 9 | 19 | 4.735337 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^7)` |
| 1.000000 | positive-margin | 8 | 17 | 4.320300 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^6)` |
| 1.000000 | positive-margin | 12 | 25 | 5.980450 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^10)` |
| 2.000000 | positive-margin | 5 | 8 | 0.075187 | 2 | 79 | 5.523562 | 6.965784 | True | `(3 1^3 2)` |

## Smallest Gap To Cap

Here `gap = first admissible n - floor(C_w / D)`.  Positive margins force `gap >= ceil(2^(S+1)/D)`, so even the nearest descent cases clear the cap by multiple integers.

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 3.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 3.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 3.000000 | positive-margin | 9 | 19 | 4.735337 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^7)` |
| 3.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 3.000000 | positive-margin | 11 | 23 | 5.565412 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^9)` |
| 3.000000 | positive-margin | 10 | 21 | 5.150375 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^8)` |
| 3.000000 | positive-margin | 7 | 15 | 3.905262 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^5)` |
| 3.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |
| 3.000000 | positive-margin | 6 | 13 | 3.490225 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^4)` |
| 3.000000 | positive-margin | 8 | 17 | 4.320300 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^6)` |
| 3.000000 | positive-margin | 12 | 25 | 5.980450 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^10)` |
| 5.000000 | positive-margin | 4 | 10 | 3.660150 | 2 | 5 | -inf | 2.321928 | True | `(4 2^3)` |
| 5.000000 | positive-margin | 6 | 14 | 4.490225 | 2 | 5 | -inf | 2.321928 | True | `(4 2^5)` |
| 5.000000 | positive-margin | 5 | 12 | 4.075187 | 2 | 5 | -inf | 2.321928 | True | `(4 2^4)` |
| 5.000000 | positive-margin | 7 | 16 | 4.905262 | 2 | 5 | -inf | 2.321928 | True | `(4 2^6)` |
| 5.000000 | positive-margin | 8 | 18 | 5.320300 | 2 | 5 | -inf | 2.321928 | True | `(4 2^7)` |

## q = 1 Witnesses

| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 5.000000 | positive-margin | 3 | 5 | 0.245112 | 1 | 13 | 2.584963 | 4.247928 | True | `(1 3 1)` |
| 5.000000 | positive-margin | 2 | 5 | 1.830075 | 1 | 3 | -inf | 1.584963 | True | `(1 4)` |
| 7.000000 | positive-margin | 3 | 7 | 2.245112 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2)` |
| 7.000000 | positive-margin | 4 | 7 | 0.660150 | 1 | 6 | 0.000000 | 2.807355 | True | `(1^2 2 3)` |
| 8.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 5.044394 | 6.189825 | True | `(2 1^2 3 1)` |
| 8.000000 | positive-margin | 5 | 8 | 0.075187 | 1 | 40 | 6.108524 | 6.768184 | True | `(3 2 1^3)` |
| 9.000000 | positive-margin | 4 | 9 | 2.660150 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^2)` |
| 11.000000 | positive-margin | 5 | 11 | 3.075187 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^3)` |
| 13.000000 | positive-margin | 6 | 13 | 3.490225 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^4)` |
| 15.000000 | positive-margin | 7 | 15 | 3.905262 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^5)` |
| 17.000000 | positive-margin | 8 | 17 | 4.320300 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^6)` |
| 19.000000 | positive-margin | 9 | 19 | 4.735337 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^7)` |
| 21.000000 | positive-margin | 10 | 21 | 5.150375 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^8)` |
| 23.000000 | positive-margin | 11 | 23 | 5.565412 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^9)` |
| 25.000000 | positive-margin | 12 | 25 | 5.980450 | 1 | 3 | -inf | 1.584963 | True | `(1 4 2^10)` |

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
| 8.573647 | positive-margin | 10 | 16 | 0.150375 | 6466 | 130648 | 8.573647 | 16.999527 | True | `(7 1^9)` |
| 8.303781 | positive-margin | 10 | 16 | 0.150375 | 5028 | 101593 | 8.303781 | 16.636922 | True | `(6 2 1^8)` |
| 8.149747 | positive-margin | 10 | 16 | 0.150375 | 4309 | 87065 | 8.149747 | 16.414504 | True | `(5 3 1^8)` |
| 8.092757 | positive-margin | 10 | 16 | 0.150375 | 1907 | 38532 | 8.092757 | 15.243955 | True | `(6 1 2 1^7)` |
| 8.066089 | positive-margin | 10 | 16 | 0.150375 | 706 | 14265 | 8.066089 | 13.827045 | True | `(4^2 1^8)` |
| 8.016808 | positive-margin | 10 | 16 | 0.150375 | 2148 | 43402 | 8.016808 | 15.414058 | True | `(3 5 1^8)` |
| 7.994353 | positive-margin | 10 | 16 | 0.150375 | 2869 | 57970 | 7.994353 | 15.829351 | True | `(2 6 1^8)` |
| 7.982994 | positive-margin | 10 | 16 | 0.150375 | 6473 | 130790 | 7.982994 | 16.999681 | True | `(1 7 1^8)` |
| 7.930737 | positive-margin | 10 | 16 | 0.150375 | 4151 | 83873 | 7.930737 | 16.360110 | True | `(6 1^2 2 1^6)` |
| 7.912889 | positive-margin | 10 | 16 | 0.150375 | 1188 | 24004 | 7.912889 | 14.565400 | True | `(5 2^2 1^7)` |
| 7.813781 | positive-margin | 10 | 16 | 0.150375 | 5647 | 114100 | 7.813781 | 16.802781 | True | `(6 1^3 2 1^5)` |
| 7.807355 | positive-margin | 10 | 16 | 0.150375 | 4072 | 82277 | 7.807355 | 16.332124 | True | `(4 3 2 1^7)` |
| 7.774787 | positive-margin | 10 | 16 | 0.150375 | 2871 | 58010 | 7.774787 | 15.829450 | True | `(5 1 3 1^7)` |
| 7.754888 | positive-margin | 10 | 16 | 0.150375 | 5514 | 111413 | 7.754888 | 16.768352 | True | `(3 4 2 1^7)` |
| 7.727920 | positive-margin | 10 | 16 | 0.150375 | 3432 | 69345 | 7.727920 | 16.085908 | True | `(5 2 1 2 1^6)` |
| 7.727920 | positive-margin | 10 | 16 | 0.150375 | 4482 | 90561 | 7.727920 | 16.469976 | True | `(6 1^4 2 1^4)` |

## Interpretation

The computation separates the descent problem into a clean trichotomy.  `q_w = 0` is the cycle obstruction.  `q_w < 0` would be a finite nondecrease packet.  `q_w > 0` means the entire exact cylinder decreases after the word.

In this window, the only zero margins are the trivial `(2)^m` words and there are no negative margins.  Combined with the old notes, this says the next real theorem candidate is not a small modular obstruction.  It is a sign theorem for the domain-lattice quotient `q_w`, with the cycle-zero case explicitly separated.

## Reproduction

```powershell
python empirical/collatz_margin_lattice_miner.py --max-length 12 --max-total-depth 25 --max-carry 8 --top-limit 16
```
