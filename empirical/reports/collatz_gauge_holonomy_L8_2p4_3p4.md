# Collatz Gauge Holonomy Audit

## Meaning

A branch word `W` in the inverse alphabet `D(x)=2x`, `U(x)=(x-1)/3` is not merely a support word.  If `W` has `u` uses of `U`, then the honest finite quotient arrow is

```text
R / (3^u M) -> R / M,    M = 2^a 3^b.
```

The lift digit `q mod 3^u` is the gauge coordinate.  If `W` has `d` uses of `D`, changing that digit changes the final phase by

```text
q -> phi_0(r) + 2^d q mod 3^u.
```

The offset `phi_0(r)` depends on the coarse source.  The multiplier `2^d mod 3^u` is the gauge holonomy of the support word.

## Settings

- base quotient: `M = 2^4 3^4 = 1296`
- audited branch-word length: `1..8`
- imported cycle sieve: `empirical\reports\collatz_cycle_sieve_L12_S24_K8.json`

## Verification

- audited words: `380`
- words with honest sources: `141`
- finite parity-defect words: `239`
- gauge words with sources: `133`
- gauge orbit violations: `0`
- phase-law violations: `0`
- target-width law failures: `0`
- gauge-law failures: `0`

For every audited word with honest sources, the raw same-level multivaluedness is exactly one `Z/3^u` gauge orbit.  The gauge-reduced closure deficit is zero.  Words with no honest source have already developed a finite 2-adic parity defect.

## Branch Examples

| word | d | u | legal sources | source fraction | target width | raw deficit | phase | order | identity |
|---|---:|---:|---:|---:|---|---:|---|---:|---|
| `U` | 0 | 1 | 216 | 0.166666666667 | 3:216 | 0.666666666667 | 1 mod 3 | 1 | True |
| `DU` | 1 | 1 | 432 | 0.333333333333 | 3:432 | 0.666666666667 | 2 mod 3 | 2 | False |
| `DDU` | 2 | 1 | 432 | 0.333333333333 | 3:432 | 0.666666666667 | 1 mod 3 | 1 | True |
| `UDD` | 2 | 1 | 216 | 0.166666666667 | 3:216 | 0.666666666667 | 1 mod 3 | 1 | True |
| `UU` | 0 | 2 | 0 | 0.000000000000 | - | - | 1 mod 9 | 1 | True |
| `DUU` | 1 | 2 | 0 | 0.000000000000 | - | - | 2 mod 9 | 6 | False |
| `UDU` | 1 | 2 | 72 | 0.055555555556 | 9:72 | 0.888888888889 | 2 mod 9 | 6 | False |
| `DUDU` | 2 | 2 | 144 | 0.111111111111 | 9:144 | 0.888888888889 | 4 mod 9 | 3 | False |
| `DDUDU` | 3 | 2 | 144 | 0.111111111111 | 9:144 | 0.888888888889 | 8 mod 9 | 2 | False |
| `UD` | 1 | 1 | 216 | 0.166666666667 | 3:216 | 0.666666666667 | 2 mod 3 | 2 | False |
| `UUD` | 1 | 2 | 0 | 0.000000000000 | - | - | 2 mod 9 | 6 | False |
| `UUU` | 0 | 3 | 0 | 0.000000000000 | - | - | 1 mod 27 | 1 | True |

Sample for word `UDU`, coarse source `16`, orbit base `3`:

| lift digit q | target | final phase |
|---:|---:|---:|
| 0 | 3 | 0 |
| 1 | 291 | 2 |
| 2 | 579 | 4 |
| 3 | 867 | 6 |
| 4 | 1155 | 8 |
| 5 | 147 | 1 |
| 6 | 435 | 3 |
| 7 | 723 | 5 |
| 8 | 1011 | 7 |

## Support Ledger

| L | d | u | words | honest possible | parity defects | source fraction range | phase | identity words | law failures |
|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
| 1 | 0 | 1 | 1 | 1 | 0 | 0.166667..0.166667 | 1 mod 3 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 2 | 0 | 2 | 1 | 0 | 1 | - | 1 mod 9 | 1 | 0 |
| 2 | 1 | 1 | 2 | 2 | 0 | 0.166667..0.333333 | 2 mod 3 | 0 | 0 |
| 2 | 2 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 3 | 0 | 3 | 1 | 0 | 1 | - | 1 mod 27 | 1 | 0 |
| 3 | 1 | 2 | 3 | 1 | 2 | 0.055556..0.055556 | 2 mod 9 | 0 | 0 |
| 3 | 2 | 1 | 3 | 3 | 0 | 0.166667..0.333333 | 1 mod 3 | 3 | 0 |
| 3 | 3 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 4 | 0 | 4 | 1 | 0 | 1 | - | 1 mod 81 | 1 | 0 |
| 4 | 1 | 3 | 4 | 0 | 4 | - | 2 mod 27 | 0 | 0 |
| 4 | 2 | 2 | 6 | 3 | 3 | 0.055556..0.111111 | 4 mod 9 | 0 | 0 |
| 4 | 3 | 1 | 4 | 4 | 0 | 0.166667..0.333333 | 2 mod 3 | 0 | 0 |
| 4 | 4 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 5 | 1 | 4 | 5 | 0 | 5 | - | 2 mod 81 | 0 | 0 |
| 5 | 2 | 3 | 10 | 1 | 9 | 0.018519..0.018519 | 4 mod 27 | 0 | 0 |
| 5 | 3 | 2 | 10 | 6 | 4 | 0.055556..0.111111 | 8 mod 9 | 0 | 0 |
| 5 | 4 | 1 | 5 | 5 | 0 | 0.166667..0.333333 | 1 mod 3 | 5 | 0 |
| 5 | 5 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 6 | 2 | 4 | 15 | 0 | 15 | - | 4 mod 81 | 0 | 0 |
| 6 | 3 | 3 | 20 | 4 | 16 | 0.018519..0.037037 | 8 mod 27 | 0 | 0 |
| 6 | 4 | 2 | 15 | 10 | 5 | 0.055556..0.111111 | 7 mod 9 | 0 | 0 |
| 6 | 5 | 1 | 6 | 6 | 0 | 0.166667..0.333333 | 2 mod 3 | 0 | 0 |
| 6 | 6 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 7 | 3 | 4 | 35 | 1 | 34 | 0.006173..0.006173 | 8 mod 81 | 0 | 0 |
| 7 | 4 | 3 | 35 | 10 | 25 | 0.018519..0.037037 | 16 mod 27 | 0 | 0 |
| 7 | 5 | 2 | 21 | 15 | 6 | 0.055556..0.111111 | 5 mod 9 | 0 | 0 |
| 7 | 6 | 1 | 7 | 7 | 0 | 0.166667..0.333333 | 1 mod 3 | 7 | 0 |
| 7 | 7 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |
| 8 | 4 | 4 | 70 | 5 | 65 | 0.006173..0.012346 | 16 mod 81 | 0 | 0 |
| 8 | 5 | 3 | 56 | 20 | 36 | 0.018519..0.037037 | 5 mod 27 | 0 | 0 |
| 8 | 6 | 2 | 28 | 21 | 7 | 0.055556..0.111111 | 1 mod 9 | 28 | 0 |
| 8 | 7 | 1 | 8 | 8 | 0 | 0.166667..0.333333 | 2 mod 3 | 0 | 0 |
| 8 | 8 | 0 | 1 | 1 | 0 | 1.000000..1.000000 | - | 0 | 0 |

## Integer Cycle Calibration

The all-`Z` calibration cycles remain separate components.  The positive `1 -> 4 -> 2 -> 1` component has identity gauge holonomy; the negative components carry nontrivial phase holonomy.

| component | cycle | carries | m | S | phase | order | identity | verified |
|---|---|---|---:|---:|---|---:|---|---|
| zero | `0` | `()` | 0 | 0 | - | - | - | True |
| positive | `1, 4, 2` | `(2)` | 1 | 2 | 1 mod 3 | 1 | True | True |
| negative | `-1, -2` | `(1)` | 1 | 1 | 2 mod 3 | 2 | False | True |
| negative | `-5, -14, -7, -20, -10` | `(1,2)` | 2 | 3 | 8 mod 9 | 2 | False | True |
| negative | `-17, -50, -25, -74, -37, -110, -55, -164, -82, -41, -122, -61, -182, -91, -272, -136, -68, -34` | `(1,1,1,2,1,1,4)` | 7 | 11 | 2048 mod 2187 | 1458 | False | True |

## Forward Cycle-Sieve Comparison

- source: `empirical\reports\collatz_cycle_sieve_L12_S24_K8.json`
- exact cycle necklaces: `1`
- nontrivial exact cycle necklaces: `0`
- identity-holonomy misses in displayed comparison rows: `5`

| section | necklace | m | S | phase | order | identity | reduced denom | mod residue | exact |
|---|---|---:|---:|---|---:|---|---:|---:|---|
| exact_records | `(2)` | 1 | 2 | 1 mod 3 | 1 | True | - | - | True |
| closest_divisibility | `(3)` | 1 | 3 | 2 mod 3 | 2 | False | 5 | 1 | False |
| closest_divisibility | `(1,1,3)` | 3 | 5 | 5 mod 27 | 18 | False | 5 | 1 | False |
| closest_divisibility | `(1,2,2)` | 3 | 5 | 5 mod 27 | 18 | False | 5 | 1 | False |
| closest_divisibility | `(1,3)` | 2 | 4 | 7 mod 9 | 3 | False | 7 | 2 | False |
| closest_divisibility | `(1,5)` | 2 | 6 | 1 mod 9 | 1 | True | 11 | 5 | False |
| closest_divisibility | `(1,1,2,2,1,1,3,3)` | 8 | 14 | 3262 mod 6561 | 2187 | False | 11 | 893 | False |
| closest_divisibility | `(4)` | 1 | 4 | 1 mod 3 | 1 | True | 13 | 1 | False |
| closest_divisibility | `(1,1,1,1,4)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 2 | False |
| closest_modular | `(3)` | 1 | 3 | 2 mod 3 | 2 | False | 5 | 1 | False |
| closest_modular | `(4)` | 1 | 4 | 1 mod 3 | 1 | True | 13 | 1 | False |
| closest_modular | `(5)` | 1 | 5 | 2 mod 3 | 2 | False | 29 | 1 | False |
| closest_modular | `(6)` | 1 | 6 | 1 mod 3 | 1 | True | 61 | 1 | False |
| closest_modular | `(7)` | 1 | 7 | 2 mod 3 | 2 | False | 125 | 1 | False |
| closest_modular | `(8)` | 1 | 8 | 1 mod 3 | 1 | True | 253 | 1 | False |
| closest_modular | `(1,1,3)` | 3 | 5 | 5 mod 27 | 18 | False | 5 | 1 | False |
| closest_modular | `(1,2,2)` | 3 | 5 | 5 mod 27 | 18 | False | 5 | 1 | False |
| near_resonant | `(1,1,1,1,4)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 2 | False |
| near_resonant | `(1,1,1,2,3)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 3 | False |
| near_resonant | `(1,1,1,3,2)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 1 | False |
| near_resonant | `(1,1,2,1,3)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 2 | False |
| near_resonant | `(1,1,2,2,2)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 1 | False |
| near_resonant | `(1,1,3,1,2)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 1 | False |
| near_resonant | `(1,2,1,2,2)` | 5 | 8 | 13 mod 243 | 81 | False | 13 | 2 | False |
| near_resonant | `(1,1,1,1,1,1,1,1,1,7)` | 10 | 16 | 6487 mod 59049 | 19683 | False | 6487 | 358 | False |

Holonomy identity is not the same as the cycle equation: displayed misses such as `(4)`, `(6)`, `(8)`, or `(1,5)` can have identity phase but still fail divisibility.  The cycle obstruction is still the exact affine fixed-point equation; holonomy is the filtered bookkeeping that prevents us from mistaking same-level multivaluedness for dynamics.

## Theorem Candidate After The Audit

The clean local statement is now:

```text
For M = 2^a 3^b and every inverse branch word W with u <= b,
the honest finite quotient relation is either empty because a
U parity gate fails, or it is a principal Z/(3^u) gauge orbit
over each legal coarse source.  Its holonomy multiplier is
2^d mod 3^u, where d is the number of D branches in W.
```

The global Collatz-facing target therefore splits cleanly:

```text
Local closure: handled by the mixed 2/3 filtered path algebra.
Cycle obstructions: the primitive carry-necklace divisibility problem.
Escape/descent: the q_w >= 0 margin problem on contracting carry words.
```

So the mission does not end in a proof claim.  It ends in a sharper skeleton: same-level U closure deficits are gauge artifacts; impossible inverse support words are finite parity defects; remaining positive periodic obstructions reduce to the carry-cycle equation and the descent-margin lemma.

## Reproduction

```powershell
python empirical/collatz_gauge_holonomy.py --max-word-length 8 --two-bits 4 --three-depth 4 --cycle-sieve-json empirical\reports\collatz_cycle_sieve_L12_S24_K8.json
```
