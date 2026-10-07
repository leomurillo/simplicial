# Collatz Margin Recurrence Miner

## Meaning

This audit moves the `q_w >= 0` problem from census to recurrence.  For a contracting parent carry word `w` and appended carry `s`, the child exact-cylinder lift is

```text
r_{w,s} = r_w + t 2^(S+1) mod 2^(S+s+1).
```

The lift digit `t mod 2^s` is forced by the next carry gate:

```text
U_w(r_w) + 2 * 3^m * t == a_s mod 2^(s+1),
a_s = (2^s - 1) * 3^-1 mod 2^(s+1).
```

The script verifies this exact recurrence and records the sign of `q_{w,s} - q_w`.

The same recurrence gives the exact append-delta identity

```text
q_{w,s} - q_w = (2D_{w,s}t + (2^s - 3)y_w - 1) / 2^(s+1),
```

where `D_{w,s}=2^(S+s)-3^(m+1)` and `y_w=U_w(r_w)`.

## Settings

- max length: `8`
- max total carry depth: `21`
- carry alphabet: `1..8`

## Verification

- words scanned: `359083`
- contracting words: `358130`
- recurrence transitions: `355243`
- recurrence failures: `0`
- delta formula failures: `0`
- negative q words: `0`
- zero q words: `8`
- trivial zero words: `8`
- positive q words: `358122`

## Append Delta Ledger

| appended s | transitions | delta < 0 | delta = 0 | delta > 0 | min delta | min child q | recurrence failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 119545 | 59424 | 0 | 60121 | -1092 | 1 | 0 |
| 2 | 84403 | 0 | 241 | 84162 | 0 | 0 | 0 |
| 3 | 57886 | 0 | 0 | 57886 | 4 | 6 | 0 |
| 4 | 38544 | 0 | 0 | 38544 | 2 | 3 | 0 |
| 5 | 24858 | 0 | 0 | 24858 | 24 | 28 | 0 |
| 6 | 15477 | 0 | 0 | 15477 | 71 | 178 | 0 |
| 7 | 9257 | 0 | 0 | 9257 | 229 | 272 | 0 |
| 8 | 5273 | 0 | 0 | 5273 | 42 | 56 | 0 |

Observed candidate reduction:

- monotone appended carries: `[2, 3, 4, 5, 6, 7, 8]`
- strict positive appended carries: `[3, 4, 5, 6, 7, 8]`
- dangerous appended carries: `[1]`

In this window, appending `s >= 2` never decreases `q`; appending `1` is the only observed decreasing move.

Most negative append deltas:

| parent | s | child | q parent | q child | delta | lift t | gate y mod |
|---|---:|---|---:|---:|---:|---:|---:|
| `(3 2 1 2 1 2 1)` | 1 | `(3 2 1 2 1 2 1^2)` | 1903 | 811 | -1092 | 0 | 3 |

Sample q-preserving append-2 moves:

| parent | s | child | q parent | q child | delta | lift t | gate y mod |
|---|---:|---|---:|---:|---:|---:|---:|
| `(2)` | 2 | `(2^2)` | 0 | 0 | 0 | 0 | 1 |
| `(4)` | 2 | `(4 2)` | 2 | 2 | 0 | 0 | 1 |
| `(6)` | 2 | `(6 2)` | 10 | 10 | 0 | 0 | 1 |
| `(8)` | 2 | `(8 2)` | 42 | 42 | 0 | 0 | 1 |
| `(2^2)` | 2 | `(2^3)` | 0 | 0 | 0 | 0 | 1 |
| `(1 4)` | 2 | `(1 4 2)` | 1 | 1 | 0 | 0 | 1 |
| `(4 2)` | 2 | `(4 2^2)` | 2 | 2 | 0 | 0 | 1 |
| `(3 4)` | 2 | `(3 4 2)` | 6 | 6 | 0 | 0 | 1 |

## Contraction Boundary

| final s | contracting children | parent contracting | parent noncontracting | min boundary q |
|---:|---:|---:|---:|---:|
| 1 | 119545 | 119545 | 0 | - |
| 2 | 84625 | 84403 | 222 | 2 |
| 3 | 58272 | 57886 | 386 | 1 |
| 4 | 38986 | 38544 | 442 | 1 |
| 5 | 25314 | 24858 | 456 | 5 |
| 6 | 15935 | 15477 | 458 | 25 |
| 7 | 9715 | 9257 | 458 | 233 |
| 8 | 5731 | 5273 | 458 | 37 |

Boundary examples where the child is contracting but its prefix is not:

| child | final s | m | S | q | height |
|---|---:|---:|---:|---:|---:|
| `(1 2^2)` | 2 | 3 | 5 | 3 | 0.245112 |
| `(2 1 2)` | 2 | 3 | 5 | 4 | 0.245112 |
| `(1 3)` | 3 | 2 | 4 | 4 | 0.830075 |
| `(1^2 3)` | 3 | 3 | 5 | 4 | 0.245112 |
| `(1 4)` | 4 | 2 | 5 | 1 | 1.830075 |
| `(1^2 4)` | 4 | 3 | 6 | 25 | 1.245112 |
| `(1 5)` | 5 | 2 | 6 | 15 | 2.830075 |
| `(1^2 5)` | 5 | 3 | 7 | 9 | 2.245112 |
| `(1 6)` | 6 | 2 | 7 | 46 | 3.830075 |
| `(1^2 6)` | 6 | 3 | 8 | 182 | 3.245112 |
| `(1 7)` | 7 | 2 | 8 | 233 | 4.830075 |
| `(1^2 7)` | 7 | 3 | 9 | 314 | 4.245112 |
| `(1 8)` | 8 | 2 | 9 | 363 | 5.830075 |
| `(1^2 8)` | 8 | 3 | 10 | 572 | 5.245112 |

## Next Lemma Candidate

The recurrence miner suggests a proof strategy sharper than raw positivity:

```text
Suffix monotonicity lemma:
If w and (w,s) are contracting and s >= 2, then q_{w,s} >= q_w.
```

If this lemma is proved, then any minimal negative-margin counterexample cannot end in a carry `s >= 2` with contracting prefix.  It must either end in carry `1`, or be a first-contraction boundary word whose prefix has `2^S - 3^m <= 0`.

So the descent-margin theorem splits into two smaller targets:

```text
1. Prove suffix monotonicity for s >= 2.
2. Control append-1 and first-contraction boundary words.
```

This is still not a proof of Collatz, but it turns the `q_w >= 0` question into a finite-looking recurrence problem with one visibly dangerous channel.

## Reproduction

```powershell
python empirical/collatz_margin_recurrence_miner.py --max-length 8 --max-total-depth 21 --max-carry 8
```
