# Collatz Append-One Chain Miner

## Meaning

Suffix monotonicity leaves append-1 as the only suffix channel that can decrease the descent-margin quotient.  This report mines that channel using exact integer recurrences, not floating approximations.

For one appended carry, the lift digit is determined by

```text
y_w + 2 * 3^m * t == 3 mod 4,   t in {0,1}.
```

Since `y_w` is odd, this is the simple parity split:

```text
t = 0  iff  y_w == 3 mod 4
t = 1  iff  y_w == 1 mod 4.
```

For a whole appended block `1^k`, write `A=3^m`, `alpha=(y_w+1)/2`, and let `b` be the unique integer `0 <= b < 2^k` satisfying

```text
A b == -alpha mod 2^k.
```

Equivalently, `y_w + 2 A b == -1 mod 2^(k+1)`.  The bits of `b` are the successive lift digits of the appended-one chain.

## Settings

- max length: `12`
- max total carry depth: `25`
- carry alphabet: `1..8`

## Verification

- words scanned: `15710500`
- contracting words: `15641778`
- negative q words: `0`
- zero q words: `12`
- trivial zero words: `12`
- positive q words: `15641766`
- append-one transitions: `6501342`
- append-one blocks: `6501342`
- one-step recurrence failures: `0`
- block recurrence failures: `0`

## One-Step Gate Split

| lift t | transitions | delta < 0 | delta = 0 | delta > 0 | min delta | min child q | recurrence failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3250129 | 3250129 | 0 | 0 | -88572 | 1 | 0 |
| 1 | 3251213 | 1074 | 0 | 3250139 | -6598 | 2 | 0 |

Most negative one-step deltas by lift digit:

| t | parent | child | q parent | q child | delta | y | D child |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | `(3 1 3 2 1 2 1 2 1 2 1)` | `(3 1 3 2 1 2 1 2 1 2 1^2)` | 347127 | 258555 | -88572 | 354287 | 517135 |
| 1 | `(1 7 1^7)` | `(1 7 1^8)` | 13071 | 6473 | -6598 | 39365 | 6487 |

The `t=0` branch always decreases `q` by `(y_w+1)/4`.  The `t=1` branch has

```text
q_{w,1} - q_w = (2D_{w,1} - y_w - 1) / 4,
```

so it can still decrease when `y_w` is large compared with the child denominator `D_{w,1}`.

## Block Chains

| trailing ones k | blocks | q < 0 | q = 0 | q > 0 | drop > 0 | min q | max signed drop | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3909061 | 0 | 0 | 3909061 | 1954538 | 1 | 88572 | `(1 3 1)` |
| 2 | 1609560 | 0 | 0 | 1609560 | 402519 | 2 | 73805 | `(2^3 1^2)` |
| 3 | 632621 | 0 | 0 | 632621 | 79039 | 1 | 46740 | `(3 2 1^3)` |
| 4 | 234717 | 0 | 0 | 234717 | 14687 | 2 | 26585 | `(4 1^4)` |
| 5 | 80980 | 0 | 0 | 80980 | 2436 | 48 | 14348 | `(1 2^2 4 2 1^5)` |
| 6 | 25431 | 0 | 0 | 25431 | 401 | 72 | 6650 | `(2^2 4 2 1^6)` |
| 7 | 7037 | 0 | 0 | 7037 | 0 | 471 | -247 | `(2 1 6 1^7)` |
| 8 | 1625 | 0 | 0 | 1625 | 0 | 706 | -611 | `(4^2 1^8)` |
| 9 | 282 | 0 | 0 | 282 | 0 | 6466 | -6362 | `(7 1^9)` |
| 10 | 28 | 0 | 0 | 28 | 0 | 28290 | -28248 | `(8 1^10)` |

Smallest observed q after an append-one block:

- anchor: `(1 3)`
- child: `(1 3 1)`
- run k: `1`
- anchor q: `4`
- child q: `1`
- drop from anchor: `3`
- y, alpha: `11, 6`
- block lift b: `0`
- t bits low-to-high: `0`
- h: `3`
- D block: `5`
- scaled surplus `2^k q_child`: `2`

Largest observed drop across an append-one block:

- anchor: `(1^2 2 1 2^2 1 4 3 1 3)`
- child: `(1^2 2 1 2^2 1 4 3 1 3 1)`
- run k: `1`
- anchor q: `1919964`
- child q: `1831392`
- drop from anchor: `88572`
- y, alpha: `354287, 177144`
- block lift b: `0`
- t bits low-to-high: `0`
- h: `88572`
- D block: `3662863`
- scaled surplus `2^k q_child`: `3662784`

## Exact Block Recurrence

With `D_{w,k}=2^(S+k)-3^(m+k)` and `h=(alpha+A b)/2^k`, the block image is

```text
y_{w,1^k} = 2 * 3^k * h - 1.
```

The block margin recurrence verified above is

```text
q_{w,1^k} = q_w + (D_{w,k} b - (3^k - 2^k) alpha) / 2^k.
```

Thus append-one positivity is exactly the integer inequality

```text
2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha.
```

In this finite window, every checked contracting append-one block has nonnegative `q`, and the scaled surplus `2^k q_{w,1^k}` is the exact difference between the two sides of the inequality.

This is not a proof of Collatz.  It isolates the append-one proof obligation as a closed finite-arithmetic inequality for the forced lift residue `b`.

## Reproduction

```powershell
python empirical/collatz_append_one_chain_miner.py --max-length 12 --max-total-depth 25 --max-carry 8
```
