# Collatz Append-One Surplus Miner

## Meaning

The append-one block recurrence reduces the remaining suffix channel to the exact inequality

```text
2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha.
```

This report ranks append-one blocks by the scaled surplus

```text
Sigma(w,k) = 2^k q_{w,1^k}
```

which is exactly the difference between the two sides of the inequality.  Small `Sigma` examples are the near-failures that a proof has to explain.

## Settings

- max length: `8`
- max total carry depth: `21`
- carry alphabet: `1..8`
- retained examples per list: `12`

## Verification

- words scanned: `359083`
- contracting words: `358130`
- append-one blocks: `119545`
- decomposition failures: `0`
- negative q words: `0`
- zero q words: `8`
- trivial zero words: `8`
- positive q words: `358122`

## Surplus Ledger By Run Length

| k | blocks | q < 0 | b=0 | lift needed | q support enough | min Sigma | min child q | max drop | min-Sigma word |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 83151 | 0 | 41239 | 8 | 83143 | 2 | 1 | 1092 | `(1 3 1)` |
| 2 | 26563 | 0 | 6520 | 12 | 26551 | 8 | 2 | 905 | `(2^3 1^2)` |
| 3 | 7573 | 0 | 907 | 13 | 7560 | 8 | 1 | 570 | `(3 2 1^3)` |
| 4 | 1848 | 0 | 115 | 6 | 1842 | 32 | 2 | 260 | `(4 1^4)` |
| 5 | 359 | 0 | 0 | 3 | 356 | 3680 | 115 | -36 | `(2 4 2 1^5)` |
| 6 | 48 | 0 | 0 | 3 | 45 | 11136 | 174 | -168 | `(3 4 1^6)` |
| 7 | 3 | 0 | 0 | 1 | 2 | 137856 | 1077 | -1067 | `(6 1^7)` |

Smallest global scaled surpluses:

| Sigma | k | child q | child | anchor q | drop | b | bits | mode | q gap | lift | obstruction |
|---:|---:|---:|---|---:|---:|---:|---|---|---:|---:|---:|
| 2 | 1 | 1 | `(1 3 1)` | 4 | 3 | 0 | `0` | q_support_sufficient | 2 | 0 | 6 |
| 2 | 1 | 1 | `(2 1^2 3 1)` | 13 | 12 | 0 | `0` | q_support_sufficient | 2 | 0 | 24 |
| 4 | 1 | 2 | `(2^2 1)` | 0 | -2 | 1 | `1` | lift_needed | -1 | 5 | 1 |
| 6 | 1 | 3 | `(1^3 4 1)` | 26 | 23 | 0 | `0` | q_support_sufficient | 6 | 0 | 46 |
| 6 | 1 | 3 | `(2^2 1 2 1)` | 29 | 26 | 0 | `0` | q_support_sufficient | 6 | 0 | 52 |
| 8 | 1 | 4 | `(1 2 1 3 1)` | 34 | 30 | 0 | `0` | q_support_sufficient | 8 | 0 | 60 |
| 8 | 1 | 4 | `(2 1 3 1)` | 7 | 3 | 0 | `0` | q_support_sufficient | 8 | 0 | 6 |
| 8 | 2 | 2 | `(2^3 1^2)` | 0 | -2 | 1 | `10` | lift_needed | -5 | 13 | 5 |
| 8 | 3 | 1 | `(3 2 1^3)` | 16 | 15 | 1 | `100` | lift_needed | -5 | 13 | 133 |
| 10 | 1 | 5 | `(1^2 2 1 4 1)` | 10 | 5 | 0 | `0` | q_support_sufficient | 10 | 0 | 10 |
| 12 | 1 | 6 | `(1 3 1 2 1)` | 3 | -3 | 1 | `1` | lift_needed | -1 | 13 | 7 |
| 12 | 1 | 6 | `(1^2 2 3 1)` | 1 | -5 | 1 | `1` | lift_needed | -1 | 13 | 3 |

Smallest surpluses where lift support is needed:

| Sigma | k | child q | child | anchor q | drop | b | bits | mode | q gap | lift | obstruction |
|---:|---:|---:|---|---:|---:|---:|---|---|---:|---:|---:|
| 4 | 1 | 2 | `(2^2 1)` | 0 | -2 | 1 | `1` | lift_needed | -1 | 5 | 1 |
| 8 | 2 | 2 | `(2^3 1^2)` | 0 | -2 | 1 | `10` | lift_needed | -5 | 13 | 5 |
| 8 | 3 | 1 | `(3 2 1^3)` | 16 | 15 | 1 | `100` | lift_needed | -5 | 13 | 133 |
| 12 | 1 | 6 | `(1 3 1 2 1)` | 3 | -3 | 1 | `1` | lift_needed | -1 | 13 | 7 |
| 12 | 1 | 6 | `(1^2 2 3 1)` | 1 | -5 | 1 | `1` | lift_needed | -1 | 13 | 3 |
| 24 | 2 | 6 | `(2 1 3 1^2)` | 7 | 1 | 2 | `01` | lift_needed | -2 | 26 | 30 |
| 32 | 4 | 2 | `(4 1^4)` | 2 | 0 | 5 | `1010` | lift_needed | -33 | 65 | 65 |
| 36 | 2 | 9 | `(1 2 3 1^2)` | 3 | -6 | 3 | `11` | lift_needed | -3 | 39 | 15 |
| 36 | 2 | 9 | `(3 1 2 1^2)` | 8 | -1 | 3 | `11` | lift_needed | -3 | 39 | 35 |
| 46 | 1 | 23 | `(2^3 1)` | 0 | -23 | 1 | `1` | lift_needed | -1 | 47 | 1 |
| 56 | 3 | 7 | `(2 3 1^3)` | 6 | -1 | 5 | `101` | lift_needed | -9 | 65 | 57 |
| 80 | 3 | 10 | `(1 4 1^3)` | 1 | -9 | 7 | `111` | lift_needed | -11 | 91 | 19 |

Smallest surpluses with zero block lift `b=0`:

| Sigma | k | child q | child | anchor q | drop | b | bits | mode | q gap | lift | obstruction |
|---:|---:|---:|---|---:|---:|---:|---|---|---:|---:|---:|
| 2 | 1 | 1 | `(1 3 1)` | 4 | 3 | 0 | `0` | q_support_sufficient | 2 | 0 | 6 |
| 2 | 1 | 1 | `(2 1^2 3 1)` | 13 | 12 | 0 | `0` | q_support_sufficient | 2 | 0 | 24 |
| 6 | 1 | 3 | `(1^3 4 1)` | 26 | 23 | 0 | `0` | q_support_sufficient | 6 | 0 | 46 |
| 6 | 1 | 3 | `(2^2 1 2 1)` | 29 | 26 | 0 | `0` | q_support_sufficient | 6 | 0 | 52 |
| 8 | 1 | 4 | `(1 2 1 3 1)` | 34 | 30 | 0 | `0` | q_support_sufficient | 8 | 0 | 60 |
| 8 | 1 | 4 | `(2 1 3 1)` | 7 | 3 | 0 | `0` | q_support_sufficient | 8 | 0 | 6 |
| 10 | 1 | 5 | `(1^2 2 1 4 1)` | 10 | 5 | 0 | `0` | q_support_sufficient | 10 | 0 | 10 |
| 16 | 1 | 8 | `(2^2 1 3 1)` | 11 | 3 | 0 | `0` | q_support_sufficient | 16 | 0 | 6 |
| 22 | 1 | 11 | `(1 2 1 2 3 1 2 1)` | 28 | 17 | 0 | `0` | q_support_sufficient | 22 | 0 | 34 |
| 22 | 1 | 11 | `(1^2 2 1 4 1 3 1)` | 14 | 3 | 0 | `0` | q_support_sufficient | 22 | 0 | 6 |
| 26 | 1 | 13 | `(2^2 1^2 3 1)` | 25 | 12 | 0 | `0` | q_support_sufficient | 26 | 0 | 24 |
| 28 | 1 | 14 | `(4 1^4 2^2 1)` | 37 | 23 | 0 | `0` | q_support_sufficient | 28 | 0 | 46 |

## Lift Residue Buckets

Buckets are only descriptive: `zero`, `all_ones`, and quartiles of `0 < b < 2^k-1`.  They help separate no-lift drops from cases where `D_{w,k} b` supplies the missing positivity.

| k | bucket | count | min Sigma | min-Sigma word |
|---:|---|---:|---:|---|
| 1 | `all_ones` | 41912 | 4 | `(2^2 1)` |
| 1 | `zero` | 41239 | 2 | `(1 3 1)` |
| 2 | `all_ones` | 6737 | 16 | `(3 1^2)` |
| 2 | `lower_middle` | 6782 | 8 | `(2^3 1^2)` |
| 2 | `upper_middle` | 6524 | 24 | `(2 1 3 1^2)` |
| 2 | `zero` | 6520 | 44 | `(2^3 1^2 3 1^2)` |
| 3 | `all_ones` | 1048 | 80 | `(1 4 1^3)` |
| 3 | `high_quarter` | 894 | 1816 | `(1 3^2 1^3)` |
| 3 | `low_quarter` | 946 | 8 | `(3 2 1^3)` |
| 3 | `lower_middle` | 1836 | 680 | `(2 1 4 1^3)` |
| 3 | `upper_middle` | 1942 | 56 | `(2 3 1^3)` |
| 3 | `zero` | 907 | 136 | `(1 4 1^2 3 1^3)` |
| 4 | `all_ones` | 131 | 4224 | `(5 1^4)` |
| 4 | `high_quarter` | 343 | 3616 | `(2 4 1^4)` |
| 4 | `low_quarter` | 325 | 2208 | `(5 2 1^4)` |
| 4 | `lower_middle` | 509 | 32 | `(4 1^4)` |
| 4 | `upper_middle` | 425 | 3088 | `(3^2 1^4)` |
| 4 | `zero` | 115 | 256 | `(2^2 3 2 1^4)` |
| 5 | `all_ones` | 24 | 9280 | `(5 1^5)` |
| 5 | `high_quarter` | 75 | 44224 | `(5 1 2 1^5)` |
| 5 | `low_quarter` | 82 | 3680 | `(2 4 2 1^5)` |
| 5 | `lower_middle` | 73 | 17248 | `(1 2 5 1^5)` |
| 5 | `upper_middle` | 105 | 26880 | `(1 5 2 1^5)` |
| 6 | `all_ones` | 9 | 103936 | `(2 5 1^6)` |
| 6 | `high_quarter` | 10 | 80640 | `(5 2 1^6)` |
| 6 | `low_quarter` | 8 | 11136 | `(3 4 1^6)` |
| 6 | `lower_middle` | 15 | 34304 | `(4 3 1^6)` |
| 6 | `upper_middle` | 6 | 418112 | `(5 3 1^6)` |
| 7 | `all_ones` | 1 | 1254656 | `(7 1^7)` |
| 7 | `upper_middle` | 2 | 137856 | `(6 1^7)` |

## Common Lift-Bit Patterns

The bit strings are low-to-high, so the first character is the first appended-one lift digit.

| k | most common lift-bit patterns |
|---:|---|
| 1 | `1` (41912), `0` (41239) |
| 2 | `10` (6782), `11` (6737), `01` (6524), `00` (6520) |
| 3 | `111` (1048), `101` (1022), `100` (946), `010` (933), `001` (920), `000` (907) |
| 4 | `1110` (170), `0010` (134), `1111` (131), `1011` (130), `1010` (125), `1000` (125) |
| 5 | `11100` (26), `10001` (26), `00111` (25), `11111` (24), `10101` (22), `01000` (22) |
| 6 | `100011` (10), `111111` (9), `101010` (8), `111000` (8), `001110` (7), `010101` (6) |
| 7 | `1010101` (2), `1111111` (1) |

## Proof-Facing Read

The support decomposition is

```text
Sigma = 2^k q_w + D_{w,k} b - (3^k - 2^k) alpha.
```

If `2^k q_w >= (3^k - 2^k) alpha`, positivity is already supplied by the anchor margin.  Otherwise the proof must use the forced lift residue `b`; those are the `lift_needed` rows.  The `b=0` rows are the opposite extreme: no lift support is available, so their positivity must come entirely from prior margin.

This is still not a proof of Collatz.  It isolates the append-one channel into exact near-failure families for the next local lemma.

## Reproduction

```powershell
python empirical/collatz_append_one_surplus_miner.py --max-length 8 --max-total-depth 21 --max-carry 8
```
