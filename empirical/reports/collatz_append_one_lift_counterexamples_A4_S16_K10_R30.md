# Collatz Append-One One-Copy Counterexamples

## Meaning

This report tests the proposed one-copy bound in the lift-supported append-one channel:

```text
E <= D_k.
```

The bound is useful because it implies `N=ceil(E/D_k)=1`; since lift-supported cases have `b>0`, one copy of `D_k` would cover the deficit.  The search below shows that this shortcut is false in general.

The true local condition remains

```text
N <= b.
```

## Settings

- max anchor length: `4`
- max anchor total depth: `16`
- carry alphabet: `1..10`
- max appended-one run: `30`

## Verification

- anchors scanned: `2360`
- contracting anchors: `2337`
- children checked: `28193`
- lift-supported children: `345`
- one-copy failures: `6`
- forced-cover failures: `0`
- max required copies: `3`

Earliest one-copy failures:

| child | anchor | k | b | N | spare | E | D_k | Sigma | alpha | q anchor |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(4 1^4)` | `(4)` | 4 | 5 | 3 | 2 | 33 | 13 | 32 | 1 | 2 |
| `(10 2 1^15)` | `(10 2)` | 15 | 29127 | 2 | 29125 | 8745579 | 5077565 | 147885490176 | 1 | 170 |
| `(2 10 1^15)` | `(2 10)` | 15 | 18204 | 2 | 18202 | 5196204 | 5077565 | 92426797056 | 4 | 1589 |
| `(4 8 1^15)` | `(4 8)` | 15 | 29127 | 2 | 29125 | 6910571 | 5077565 | 147887325184 | 1 | 226 |
| `(7 5 1^15)` | `(7 5)` | 15 | 21845 | 2 | 21843 | 5986113 | 5077565 | 110913421312 | 3 | 1128 |
| `(8 4 1^15)` | `(8 4)` | 15 | 18204 | 2 | 18202 | 5654956 | 5077565 | 92426338304 | 4 | 1575 |

## Explicit Disproof

The smallest failure is already

```text
anchor w = (4), appended block 1^4.
```

For this block:

```text
q_w = 2, alpha = 1, D_k = 13, b = 5,
E = (3^4 - 2^4)alpha - 2^4 q_w = 65 - 32 = 33.
```

So `E=33 > 13=D_k`, and the one-copy bound fails.  The child still has positive surplus because

```text
D_k b - E = 13*5 - 33 = 32.
```

The right target is therefore not the universal one-copy bound.  It is the copy-cover inequality `N <= b`, possibly with a one-copy sublemma for the majority channel and a separate multi-copy channel.

## Reproduction

```powershell
python empirical/collatz_append_one_lift_counterexample_miner.py --max-anchor-length 4 --max-anchor-total-depth 16 --max-carry 10 --max-run 30
```
