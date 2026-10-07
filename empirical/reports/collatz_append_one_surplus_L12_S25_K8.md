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

- max length: `12`
- max total carry depth: `25`
- carry alphabet: `1..8`
- retained examples per list: `12`

## Verification

- words scanned: `15710500`
- contracting words: `15641778`
- append-one blocks: `6501342`
- decomposition failures: `0`
- negative q words: `0`
- zero q words: `12`
- trivial zero words: `12`
- positive q words: `15641766`

## Surplus Ledger By Run Length

| k | blocks | q < 0 | b=0 | lift needed | q support enough | min Sigma | min child q | max drop | min-Sigma word |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3909061 | 0 | 1954074 | 12 | 3909049 | 2 | 1 | 88572 | `(1 3 1)` |
| 2 | 1609560 | 0 | 402021 | 20 | 1609540 | 8 | 2 | 73805 | `(2^3 1^2)` |
| 3 | 632621 | 0 | 78798 | 27 | 632594 | 8 | 1 | 46740 | `(3 2 1^3)` |
| 4 | 234717 | 0 | 14617 | 28 | 234689 | 32 | 2 | 26585 | `(4 1^4)` |
| 5 | 80980 | 0 | 2415 | 28 | 80952 | 1536 | 48 | 14348 | `(1 2^2 4 2 1^5)` |
| 6 | 25431 | 0 | 395 | 28 | 25403 | 4608 | 72 | 6650 | `(2^2 4 2 1^6)` |
| 7 | 7037 | 0 | 0 | 16 | 7021 | 60288 | 471 | -247 | `(2 1 6 1^7)` |
| 8 | 1625 | 0 | 0 | 8 | 1617 | 180736 | 706 | -611 | `(4^2 1^8)` |
| 9 | 282 | 0 | 0 | 5 | 277 | 3310592 | 6466 | -6362 | `(7 1^9)` |
| 10 | 28 | 0 | 0 | 3 | 25 | 28968960 | 28290 | -28248 | `(8 1^10)` |

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
| 8 | 1 | 4 | `(2 3 2 1^4 2^2 1)` | 27 | 23 | 0 | `0` | q_support_sufficient | 8 | 0 | 46 |
| 8 | 2 | 2 | `(2^3 1^2)` | 0 | -2 | 1 | `10` | lift_needed | -5 | 13 | 5 |
| 8 | 3 | 1 | `(3 2 1^3)` | 16 | 15 | 1 | `100` | lift_needed | -5 | 13 | 133 |
| 10 | 1 | 5 | `(1 3 1 3 1^3 2^2 1)` | 28 | 23 | 0 | `0` | q_support_sufficient | 10 | 0 | 46 |
| 10 | 1 | 5 | `(1^2 2 1 4 1)` | 10 | 5 | 0 | `0` | q_support_sufficient | 10 | 0 | 10 |

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
| 8 | 1 | 4 | `(2 3 2 1^4 2^2 1)` | 27 | 23 | 0 | `0` | q_support_sufficient | 8 | 0 | 46 |
| 10 | 1 | 5 | `(1 3 1 3 1^3 2^2 1)` | 28 | 23 | 0 | `0` | q_support_sufficient | 10 | 0 | 46 |
| 10 | 1 | 5 | `(1^2 2 1 4 1)` | 10 | 5 | 0 | `0` | q_support_sufficient | 10 | 0 | 10 |
| 10 | 1 | 5 | `(4 1^4 2^2 1 2 1)` | 31 | 26 | 0 | `0` | q_support_sufficient | 10 | 0 | 52 |
| 16 | 1 | 8 | `(2^2 1 3 1)` | 11 | 3 | 0 | `0` | q_support_sufficient | 16 | 0 | 6 |
| 22 | 1 | 11 | `(1 2 1 2 3 1 2 1)` | 28 | 17 | 0 | `0` | q_support_sufficient | 22 | 0 | 34 |

## Lift Residue Buckets

Buckets are only descriptive: `zero`, `all_ones`, and quartiles of `0 < b < 2^k-1`.  They help separate no-lift drops from cases where `D_{w,k} b` supplies the missing positivity.

| k | bucket | count | min Sigma | min-Sigma word |
|---:|---|---:|---:|---|
| 1 | `all_ones` | 1954987 | 4 | `(2^2 1)` |
| 1 | `zero` | 1954074 | 2 | `(1 3 1)` |
| 2 | `all_ones` | 402325 | 16 | `(3 1^2)` |
| 2 | `lower_middle` | 402999 | 8 | `(2^3 1^2)` |
| 2 | `upper_middle` | 402215 | 24 | `(2 1 3 1^2)` |
| 2 | `zero` | 402021 | 40 | `(1 2^2 1^2 2^2 3 1^2)` |
| 3 | `all_ones` | 79387 | 80 | `(1 4 1^3)` |
| 3 | `high_quarter` | 78738 | 1816 | `(1 3^2 1^3)` |
| 3 | `low_quarter` | 79271 | 8 | `(3 2 1^3)` |
| 3 | `lower_middle` | 158049 | 680 | `(2 1 4 1^3)` |
| 3 | `upper_middle` | 158378 | 56 | `(2 3 1^3)` |
| 3 | `zero` | 78798 | 120 | `(2^2 1^2 2^2 3 1^3)` |
| 4 | `all_ones` | 14732 | 4224 | `(5 1^4)` |
| 4 | `high_quarter` | 44033 | 3616 | `(2 4 1^4)` |
| 4 | `low_quarter` | 43974 | 2208 | `(5 2 1^4)` |
| 4 | `lower_middle` | 58826 | 32 | `(4 1^4)` |
| 4 | `upper_middle` | 58535 | 3088 | `(3^2 1^4)` |
| 4 | `zero` | 14617 | 80 | `(1 2^3 3 2 1^4)` |
| 5 | `all_ones` | 2621 | 9280 | `(5 1^5)` |
| 5 | `high_quarter` | 17652 | 44224 | `(5 1 2 1^5)` |
| 5 | `low_quarter` | 17781 | 3680 | `(2 4 2 1^5)` |
| 5 | `lower_middle` | 20203 | 17248 | `(1 2 5 1^5)` |
| 5 | `upper_middle` | 20308 | 26880 | `(1 5 2 1^5)` |
| 5 | `zero` | 2415 | 1536 | `(1 2^2 4 2 1^5)` |
| 6 | `all_ones` | 437 | 103936 | `(2 5 1^6)` |
| 6 | `high_quarter` | 5985 | 80640 | `(5 2 1^6)` |
| 6 | `low_quarter` | 5937 | 11136 | `(3 4 1^6)` |
| 6 | `lower_middle` | 6397 | 34304 | `(4 3 1^6)` |
| 6 | `upper_middle` | 6280 | 219648 | `(5 2 1 2 1^6)` |
| 6 | `zero` | 395 | 4608 | `(2^2 4 2 1^6)` |
| 7 | `all_ones` | 98 | 1254656 | `(7 1^7)` |
| 7 | `high_quarter` | 1696 | 644480 | `(1 5 3 1^7)` |
| 7 | `low_quarter` | 1726 | 60288 | `(2 1 6 1^7)` |
| 7 | `lower_middle` | 1699 | 244096 | `(6 1 2 1^7)` |
| 7 | `upper_middle` | 1818 | 137856 | `(6 1^7)` |
| 8 | `all_ones` | 40 | 1657088 | `(1 7 1^8)` |
| 8 | `high_quarter` | 391 | 1287168 | `(6 2 1^8)` |
| 8 | `low_quarter` | 379 | 180736 | `(4^2 1^8)` |
| 8 | `lower_middle` | 434 | 549888 | `(3 5 1^8)` |
| 8 | `upper_middle` | 381 | 1103104 | `(5 3 1^8)` |
| 9 | `all_ones` | 20 | 3310592 | `(7 1^9)` |
| 9 | `high_quarter` | 62 | 38667776 | `(5 4 1^9)` |
| 9 | `low_quarter` | 60 | 9652736 | `(7 2 1^9)` |
| 9 | `lower_middle` | 59 | 14491648 | `(2 7 1^9)` |
| 9 | `upper_middle` | 81 | 24162304 | `(3 6 1^9)` |
| 10 | `all_ones` | 5 | 529487872 | `(3 7 1^10)` |
| 10 | `high_quarter` | 4 | 411807744 | `(6 4 1^10)` |
| 10 | `low_quarter` | 6 | 58779648 | `(4 6 1^10)` |
| 10 | `lower_middle` | 9 | 28968960 | `(8 1^10)` |
| 10 | `upper_middle` | 4 | 352965632 | `(7 3 1^10)` |

## Common Lift-Bit Patterns

The bit strings are low-to-high, so the first character is the first appended-one lift digit.

| k | most common lift-bit patterns |
|---:|---|
| 1 | `1` (1954987), `0` (1954074) |
| 2 | `10` (402999), `11` (402325), `01` (402215), `00` (402021) |
| 3 | `111` (79387), `101` (79378), `100` (79271), `110` (79038), `010` (79011), `001` (79000) |
| 4 | `1110` (14876), `1010` (14790), `1001` (14773), `1011` (14768), `1111` (14732), `0011` (14705) |
| 5 | `10100` (2622), `11111` (2621), `11101` (2615), `00001` (2610), `10111` (2592), `00110` (2579) |
| 6 | `111000` (502), `101101` (483), `111010` (481), `010110` (464), `100001` (460), `010011` (453) |
| 7 | `0000001` (121), `0100110` (121), `1000011` (118), `1001111` (117), `1110000` (116), `0011000` (115) |
| 8 | `11101001` (47), `10110111` (46), `11011110` (46), `10100100` (46), `01000010` (44), `10010000` (43) |
| 9 | `111000111` (21), `111111111` (20), `100011100` (20), `001110001` (18), `101010101` (17), `010101010` (17) |
| 10 | `1000111000` (6), `1110001110` (5), `1111111111` (5), `1010101010` (4), `0011100011` (4), `0101010101` (4) |

## Proof-Facing Read

The support decomposition is

```text
Sigma = 2^k q_w + D_{w,k} b - (3^k - 2^k) alpha.
```

If `2^k q_w >= (3^k - 2^k) alpha`, positivity is already supplied by the anchor margin.  Otherwise the proof must use the forced lift residue `b`; those are the `lift_needed` rows.  The `b=0` rows are the opposite extreme: no lift support is available, so their positivity must come entirely from prior margin.

This is still not a proof of Collatz.  It isolates the append-one channel into exact near-failure families for the next local lemma.

## Reproduction

```powershell
python empirical/collatz_append_one_surplus_miner.py --max-length 12 --max-total-depth 25 --max-carry 8
```
