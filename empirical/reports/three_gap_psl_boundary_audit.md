# Three-Gap PSL-Boundary Audit

This is the second Paper 25 three-gap diagnostic.  It replaces the
raw integer carry from `three_gap_carry_audit.py` with a non-split
PSL cover-boundary character observable.  The result is a finite
character-vector rigidity check, not a proof of the full conductor/CRT
carry law.

## Config

- `rows`: `[6, 10, 15, 30, 210]`
- `min_face_omega`: `2`
- `prefix_fractions`: `['1/3', '1/2', '2/3', '1']`
- `max_generators_per_face`: `0`
- `tolerance`: `1e-08`
- `observable`: `non-split PSL cover-boundary edge Fourier coefficients, centered modulo flat constants`

## Aggregate

| check | pass | total | rate | max primitive classes | failures |
|---|---:|---:|---:|---:|---:|
| rotation shadow | 1380 | 1380 | 100.00% | 3 | 0 |
| PSL support gaps | 1380 | 1380 | 100.00% | 3 | 0 |
| PSL jump classes lift from rotation gaps | 1380 | 1380 | 100.00% | 3 | 0 |
| PSL jump class count <= rotation count | 1380 | 1380 | 100.00% | 3 | 0 |
| PSL jump additive three-gap law | 1002 | 1380 | 72.61% | 3 | 378 |

The first four rows are the intended finite rigidity checks.  The
last row is intentionally stronger: it asks the nonlinear jump norms
themselves to satisfy the additive largest=sum law.  That stronger
amplitude statement is not expected from the classical theorem.

## By Row

| row | records | support | jump lift | jump count | additive jumps | max entries |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 8 | 8/8 | 8/8 | 8/8 | 8/8 | 4 |
| 10 | 24 | 24/24 | 24/24 | 24/24 | 22/24 | 24 |
| 15 | 48 | 48/48 | 48/48 | 48/48 | 42/48 | 64 |
| 30 | 128 | 128/128 | 128/128 | 128/128 | 106/128 | 268 |
| 210 | 1172 | 1172/1172 | 1172/1172 | 1172/1172 | 824/1172 | 15136 |

## By Face

| row:face | records | support | jump lift | jump count | additive jumps | max jump classes | max entries |
|---|---:|---:|---:|---:|---:|---:|---:|
| 6:6 | 8 | 8/8 | 8/8 | 8/8 | 8/8 | 2 | 4 |
| 10:10 | 24 | 24/24 | 24/24 | 24/24 | 22/24 | 3 | 24 |
| 15:15 | 48 | 48/48 | 48/48 | 48/48 | 42/48 | 3 | 64 |
| 30:6 | 8 | 8/8 | 8/8 | 8/8 | 8/8 | 2 | 4 |
| 30:10 | 24 | 24/24 | 24/24 | 24/24 | 22/24 | 3 | 24 |
| 30:15 | 48 | 48/48 | 48/48 | 48/48 | 42/48 | 3 | 64 |
| 30:30 | 48 | 48/48 | 48/48 | 48/48 | 34/48 | 3 | 268 |
| 210:6 | 8 | 8/8 | 8/8 | 8/8 | 8/8 | 2 | 4 |
| 210:10 | 24 | 24/24 | 24/24 | 24/24 | 22/24 | 3 | 24 |
| 210:14 | 36 | 36/36 | 36/36 | 36/36 | 34/36 | 3 | 60 |
| 210:15 | 48 | 48/48 | 48/48 | 48/48 | 42/48 | 3 | 64 |
| 210:21 | 72 | 72/72 | 72/72 | 72/72 | 66/72 | 3 | 144 |
| 210:30 | 48 | 48/48 | 48/48 | 48/48 | 34/48 | 3 | 268 |
| 210:35 | 144 | 144/144 | 144/144 | 144/144 | 120/144 | 3 | 384 |
| 210:42 | 72 | 72/72 | 72/72 | 72/72 | 48/72 | 3 | 616 |
| 210:70 | 144 | 144/144 | 144/144 | 144/144 | 90/144 | 3 | 1956 |
| 210:105 | 288 | 288/288 | 288/288 | 288/288 | 194/288 | 3 | 4528 |
| 210:210 | 288 | 288/288 | 288/288 | 288/288 | 166/288 | 3 | 15136 |

## First Rigidity Failures

No failures for support gaps, jump lift, or jump class-count checks.

## Reading

The raw integer carry audit failed because integer carry is not the
filtered conductor observable.  This PSL-boundary audit keeps the
character-translation structure.  After deleting split prime-axis
entries and centering flat constants, support gaps and jump classes
are controlled by the same primitive rotation-gap classes on every
tested cyclic face.

This supports a precise next theorem: finite character-vector PSL
carry phases have a three-gap support grammar and a jump-class grammar
lifted from the rotation gaps.  It still does not prove that the
current-level Hayes-Mobius leakage quotient is exactly this vector
observable, nor that projective CRT products preserve the grammar.
