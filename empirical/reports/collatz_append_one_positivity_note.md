# Collatz Append-One Positivity Note

## Setup

For a contracting carry word `w=(s_1,...,s_m)`, write

```text
U_w(n) = (3^m n + C_w) / 2^S,
D_w    = 2^S - 3^m.
```

Let `r_w` be the first positive representative of the exact carry cylinder, and set

```text
y_w = U_w(r_w),
q_w = (r_w - y_w)/2.
```

The suffix-monotonicity lemma handles every appended carry `s >= 2`, so the remaining suffix channel is append-one.

## One-Step Gate

For an appended carry `1`, the child residue has the form

```text
r_{w,1} = r_w + t 2^(S+1) mod 2^(S+2),
```

where `t in {0,1}` is forced by

```text
y_w + 2 * 3^m * t == 3 mod 4.
```

Since `y_w` is odd and `3^m` is odd, this is exactly

```text
t = 0  iff  y_w == 3 mod 4,
t = 1  iff  y_w == 1 mod 4.
```

The append-delta identity specializes to

```text
q_{w,1} - q_w = (2D_{w,1}t - y_w - 1) / 4,
D_{w,1}=2^(S+1)-3^(m+1).
```

Thus:

```text
t=0:  q_{w,1} - q_w = -(y_w+1)/4.
t=1:  q_{w,1} - q_w = (2D_{w,1}-y_w-1)/4.
```

So `t=0` is always a strict drop, while `t=1` can still drop if `y_w` is large relative to `D_{w,1}`.

## Step Evolution Along A One-Chain

For a chain of appended ones, put

```text
A_j = 3^(m+j),
D_j = 2^(S+j) - 3^(m+j),
y_j = y_{w,1^j},
q_j = q_{w,1^j}.
```

The next lift digit is

```text
t_j = 0  iff  y_j == 3 mod 4,
t_j = 1  iff  y_j == 1 mod 4.
```

The exact step recurrences are

```text
A_{j+1} = 3A_j,
D_{j+1} = 2D_j - A_j,
y_{j+1} = (3y_j + 1 + 6A_j t_j) / 2,
q_{j+1} = q_j + (2D_{j+1}t_j - y_j - 1) / 4.
```

The child remains in the contracting regime precisely when `D_{j+1}>0`.

## Block Gate For `1^k`

Now append a whole block `1^k`.  Write

```text
A     = 3^m,
alpha = (y_w + 1)/2.
```

The lifted parent image before the all-one block is

```text
z = y_w + 2A b,
```

where `0 <= b < 2^k` records the successive lift digits:

```text
b = t_0 + 2t_1 + ... + 2^(k-1)t_(k-1).
```

The exact all-one cylinder is the residue `-1 mod 2^(k+1)`, because the map

```text
T_1(n) = (3n+1)/2
```

fixes `-1` in the `2`-adic sense.  Therefore `b` is uniquely determined by

```text
y_w + 2A b == -1 mod 2^(k+1),
```

or equivalently

```text
A b == -alpha mod 2^k.
```

This gives a closed formula for the append-one block lift:

```text
b == -alpha * A^-1 mod 2^k,       0 <= b < 2^k.
```

## Block Image

Let

```text
h = (alpha + A b) / 2^k.
```

This is an integer by the defining congruence for `b`.  Since

```text
z = y_w + 2A b = 2^(k+1)h - 1,
```

and

```text
T_1^k(n) = (3^k n + 3^k - 2^k) / 2^k,
```

the child image is

```text
y_{w,1^k} = T_1^k(z) = 2 * 3^k * h - 1.
```

## Block Margin Recurrence

The child residue is

```text
r_{w,1^k} = r_w + b 2^(S+1) mod 2^(S+k+1).
```

Using `q=(r-y)/2`,

```text
q_{w,1^k} - q_w
= (b 2^(S+1) - (y_{w,1^k}-y_w)) / 2.
```

Substituting the image formula and `alpha=(y_w+1)/2` gives

```text
q_{w,1^k}
= q_w + (D_{w,k} b - (3^k - 2^k) alpha) / 2^k,
```

where

```text
D_{w,k}=2^(S+k)-3^(m+k).
```

This is the append-one block analogue of the single-step delta identity.

## Exact Remaining Inequality

For a contracting child `w1^k`, append-one positivity is therefore equivalent to

```text
2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha,
```

with

```text
b == -alpha * (3^m)^-1 mod 2^k,
0 <= b < 2^k,
alpha = (y_w+1)/2.
```

The scaled surplus is exactly

```text
2^k q_{w,1^k}
= 2^k q_w + D_{w,k} b - (3^k - 2^k) alpha.
```

So the append-one channel has been reduced to a finite arithmetic inequality for the forced residue `b`.  This note proves the local recurrences; it does not prove that the inequality is always nonnegative.

## Computational Check

The append-one miner

```powershell
python empirical/collatz_append_one_chain_miner.py --max-length 12 --max-total-depth 25 --max-carry 8
```

checked:

```text
words scanned:              15710500
contracting words:          15641778
append-one transitions:      6501342
append-one blocks:           6501342
one-step recurrence failures:      0
block recurrence failures:         0
negative q in this window:         0
```

The run also confirms that `t=1` is not automatically monotone: it had `1074` negative one-step deltas in this window.  The block inequality above is therefore the sharper next proof obligation.
