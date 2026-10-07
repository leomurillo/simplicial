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

- max length: `8`
- max total carry depth: `21`
- carry alphabet: `1..8`

## Verification

- words scanned: `359083`
- contracting words: `358130`
- negative q words: `0`
- zero q words: `8`
- trivial zero words: `8`
- positive q words: `358122`
- append-one transitions: `119545`
- append-one blocks: `119545`
- one-step recurrence failures: `0`
- block recurrence failures: `0`

## One-Step Gate Split

| lift t | transitions | delta < 0 | delta = 0 | delta > 0 | min delta | min child q | recurrence failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 59357 | 59357 | 0 | 0 | -1092 | 1 | 0 |
| 1 | 60188 | 67 | 0 | 60121 | -278 | 2 | 0 |

Most negative one-step deltas by lift digit:

| t | parent | child | q parent | q child | delta | y | D child |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | `(3 2 1 2 1 2 1)` | `(3 2 1 2 1 2 1^2)` | 1903 | 811 | -1092 | 4367 | 1631 |
| 1 | `(2 5 1^5)` | `(2 5 1^6)` | 1902 | 1624 | -278 | 4373 | 1631 |

The `t=0` branch always decreases `q` by `(y_w+1)/4`.  The `t=1` branch has

```text
q_{w,1} - q_w = (2D_{w,1} - y_w - 1) / 4,
```

so it can still decrease when `y_w` is large compared with the child denominator `D_{w,1}`.

## Block Chains

| trailing ones k | blocks | q < 0 | q = 0 | q > 0 | drop > 0 | min q | max signed drop | min-q word |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 83151 | 0 | 0 | 83151 | 41270 | 1 | 1092 | `(1 3 1)` |
| 2 | 26563 | 0 | 0 | 26563 | 6545 | 2 | 905 | `(2^3 1^2)` |
| 3 | 7573 | 0 | 0 | 7573 | 917 | 1 | 570 | `(3 2 1^3)` |
| 4 | 1848 | 0 | 0 | 1848 | 117 | 2 | 260 | `(4 1^4)` |
| 5 | 359 | 0 | 0 | 359 | 0 | 115 | -36 | `(2 4 2 1^5)` |
| 6 | 48 | 0 | 0 | 48 | 0 | 174 | -168 | `(3 4 1^6)` |
| 7 | 3 | 0 | 0 | 3 | 0 | 1077 | -1067 | `(6 1^7)` |

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

- anchor: `(2 1^4 7 3)`
- child: `(2 1^4 7 3 1)`
- run k: `1`
- anchor q: `63245`
- child q: `62153`
- drop from anchor: `1092`
- y, alpha: `4367, 2184`
- block lift b: `0`
- t bits low-to-high: `0`
- h: `1092`
- D block: `124511`
- scaled surplus `2^k q_child`: `124306`

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
python empirical/collatz_append_one_chain_miner.py --max-length 8 --max-total-depth 21 --max-carry 8
```
