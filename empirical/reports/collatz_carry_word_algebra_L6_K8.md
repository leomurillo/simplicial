# Collatz Carry-Word Algebra

## Status

This report enumerates a finite window in the carry-word algebra of the accelerated odd Collatz map.  The finite window is a diagnostic slice of an infinite pro-2 carry tower.

- carry alphabet: `1..8`
- max word length: `6`
- words enumerated: `299592`
- positive-denominator words: `299464`
- integer cycle candidates: `6`
- exact cycles: `6`
- nontrivial exact cycles: `0`
- Haar mass represented by the truncated carry alphabet across all listed lengths: `5.9185007263`

## Algebra

For a word `w=(s1,...,sm)`,

```text
U_w(n) = (3^m n + C_w) / 2^S
S = s1 + ... + sm
C_empty = 0
C_{w,s} = 3 C_w + 2^S
```

Composition is a semigroup law:

```text
C_{uv} = 3^|v| C_u + 2^S(u) C_v
S_{uv} = S_u + S_v
```

A cycle with carry word `w` would have to satisfy

```text
n = C_w / (2^S - 3^m)
```

and also pass the exact carry simulation test.

## Length Summary

| m | words | positive denom | nonpositive denom | integer candidates | exact cycles | nontrivial exact cycles | min positive drift | min noninteger reduced denom | Haar mass |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 7 | 1 | 1 | 1 | 0 | 0.415037 | 5 | 0.9960937500 |
| 2 | 64 | 61 | 3 | 1 | 1 | 0 | 0.830075 | 5 | 0.9922027588 |
| 3 | 512 | 508 | 4 | 1 | 1 | 0 | 0.245112 | 5 | 0.9883269668 |
| 4 | 4096 | 4081 | 15 | 1 | 1 | 0 | 0.660150 | 5 | 0.9844663145 |
| 5 | 32768 | 32747 | 21 | 1 | 1 | 0 | 0.075187 | 5 | 0.9806207430 |
| 6 | 262144 | 262060 | 84 | 1 | 1 | 0 | 0.490225 | 5 | 0.9767901932 |

## Exact Cycle Candidates

The expected trivial family is the one-cycle word `(2)` and its powers, all giving `n=1`.

| word | m | S | drift | C_w | 2^S-3^m | reduced denom | candidate | exact | domain cylinder |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `(2)` | 1 | 2 | 0.415037 | 1 | 1 | 1 | 1 | True | `n = 1 mod 8` |
| `(2,2)` | 2 | 4 | 0.830075 | 7 | 7 | 1 | 1 | True | `n = 1 mod 32` |
| `(2,2,2)` | 3 | 6 | 1.245112 | 37 | 37 | 1 | 1 | True | `n = 1 mod 128` |
| `(2,2,2,2)` | 4 | 8 | 1.660150 | 175 | 175 | 1 | 1 | True | `n = 1 mod 512` |
| `(2,2,2,2,2)` | 5 | 10 | 2.075187 | 781 | 781 | 1 | 1 | True | `n = 1 mod 2048` |
| `(2,2,2,2,2,2)` | 6 | 12 | 2.490225 | 3367 | 3367 | 1 | 1 | True | `n = 1 mod 8192` |

## Nontrivial Exact Cycles

_None in this finite window._

## Near-Resonant Positive-Drift Words

These are the words with the smallest positive `S - m log2(3)` in the finite window.  Positive drift is required for a positive cycle denominator.

| word | m | S | drift | C_w | 2^S-3^m | reduced denom | candidate | exact | domain cylinder |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `(1,1,1,1,4)` | 5 | 8 | 0.075187 | 211 | 13 | 13 | - | False | `n = 95 mod 512` |
| `(1,1,1,2,3)` | 5 | 8 | 0.075187 | 227 | 13 | 13 | - | False | `n = 175 mod 512` |
| `(1,1,1,3,2)` | 5 | 8 | 0.075187 | 259 | 13 | 13 | - | False | `n = 335 mod 512` |
| `(1,1,1,4,1)` | 5 | 8 | 0.075187 | 323 | 13 | 13 | - | False | `n = 143 mod 512` |
| `(1,1,2,1,3)` | 5 | 8 | 0.075187 | 251 | 13 | 13 | - | False | `n = 295 mod 512` |
| `(1,1,2,2,2)` | 5 | 8 | 0.075187 | 283 | 13 | 13 | - | False | `n = 455 mod 512` |
| `(1,1,2,3,1)` | 5 | 8 | 0.075187 | 347 | 13 | 13 | - | False | `n = 263 mod 512` |
| `(1,1,3,1,2)` | 5 | 8 | 0.075187 | 331 | 13 | 13 | - | False | `n = 183 mod 512` |
| `(1,1,3,2,1)` | 5 | 8 | 0.075187 | 395 | 13 | 13 | - | False | `n = 503 mod 512` |
| `(1,1,4,1,1)` | 5 | 8 | 0.075187 | 491 | 13 | 13 | - | False | `n = 471 mod 512` |
| `(1,2,1,1,3)` | 5 | 8 | 0.075187 | 287 | 13 | 13 | - | False | `n = 219 mod 512` |
| `(1,2,1,2,2)` | 5 | 8 | 0.075187 | 319 | 13 | 13 | - | False | `n = 379 mod 512` |
| `(1,2,1,3,1)` | 5 | 8 | 0.075187 | 383 | 13 | 13 | - | False | `n = 187 mod 512` |
| `(1,2,2,1,2)` | 5 | 8 | 0.075187 | 367 | 13 | 13 | - | False | `n = 107 mod 512` |
| `(1,2,2,2,1)` | 5 | 8 | 0.075187 | 431 | 13 | 13 | - | False | `n = 427 mod 512` |
| `(1,2,3,1,1)` | 5 | 8 | 0.075187 | 527 | 13 | 13 | - | False | `n = 395 mod 512` |

## Best Divisibility Obstructions

For positive-denominator words that do not give integer candidates, the reduced denominator is `(2^S - 3^m)/gcd(C_w, 2^S - 3^m)`.  Small values are the closest algebraic misses.

| word | m | S | drift | C_w | 2^S-3^m | reduced denom | candidate | exact | domain cylinder |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `(1,1,3)` | 3 | 5 | 0.245112 | 19 | 5 | 5 | - | False | `n = 55 mod 64` |
| `(1,1,3,1,1,3)` | 6 | 10 | 0.490225 | 1121 | 295 | 5 | - | False | `n = 823 mod 2048` |
| `(1,2,2)` | 3 | 5 | 0.245112 | 23 | 5 | 5 | - | False | `n = 43 mod 64` |
| `(1,2,2,1,2,2)` | 6 | 10 | 0.490225 | 1357 | 295 | 5 | - | False | `n = 1643 mod 2048` |
| `(1,3,1)` | 3 | 5 | 0.245112 | 31 | 5 | 5 | - | False | `n = 19 mod 64` |
| `(1,3,1,1,3,1)` | 6 | 10 | 0.490225 | 1829 | 295 | 5 | - | False | `n = 1235 mod 2048` |
| `(2,1,2)` | 3 | 5 | 0.245112 | 29 | 5 | 5 | - | False | `n = 57 mod 64` |
| `(2,1,2,2,1,2)` | 6 | 10 | 0.490225 | 1711 | 295 | 5 | - | False | `n = 825 mod 2048` |
| `(2,2,1)` | 3 | 5 | 0.245112 | 37 | 5 | 5 | - | False | `n = 33 mod 64` |
| `(2,2,1,2,2,1)` | 6 | 10 | 0.490225 | 2183 | 295 | 5 | - | False | `n = 417 mod 2048` |
| `(3)` | 1 | 3 | 1.415037 | 1 | 5 | 5 | - | False | `n = 13 mod 16` |
| `(3,1,1)` | 3 | 5 | 0.245112 | 49 | 5 | 5 | - | False | `n = 61 mod 64` |
| `(3,1,1,3,1,1)` | 6 | 10 | 0.490225 | 2891 | 295 | 5 | - | False | `n = 829 mod 2048` |
| `(3,3)` | 2 | 6 | 2.830075 | 11 | 55 | 5 | - | False | `n = 77 mod 128` |
| `(3,3,3)` | 3 | 9 | 4.245112 | 97 | 485 | 5 | - | False | `n = 205 mod 1024` |
| `(3,3,3,3)` | 4 | 12 | 5.660150 | 803 | 4015 | 5 | - | False | `n = 3277 mod 8192` |

## Backwards From The Goal

To rule out nontrivial cycles, the algebraic task is: for every primitive carry word not generated by `(2)`, prove that either `2^S - 3^m` does not divide `C_w`, or the resulting integer fails the exact carry word.  The finite report performs that test only inside the enumerated window.

To rule out escape, the algebraic task is different: control the height cocycle

```text
H(w) = S(w) - |w| log2(3)
```

along infinite admissible carry words.  Escape would require prefixes whose average carry depth fails to beat `log2(3)` often enough to overcome the affine constants.

So the needed object is not a single finite matrix.  It is the filtered pro-2 carry-word groupoid: carry words, their exact domain cylinders `n = r_w mod 2^(S+1)`, the cocycle `C_w`, and the height cocycle `H(w)`.  Finite quotient adjacency matrices are representations of this algebra, not the algebra itself.

## Reproduction

```powershell
python empirical/collatz_carry_word_algebra.py --max-length 6 --max-carry 8
```
