# Collatz Append-One Surplus Note

## Setup

For a contracting anchor word `w`, append a block `1^k` and assume the child `w1^k` is also contracting.  Use the append-one block notation:

```text
y      = y_w = U_w(r_w),
q      = q_w,
A      = 3^m,
alpha  = (y+1)/2,
D_k    = 2^(S+k)-3^(m+k),
b      == -alpha * A^-1 mod 2^k,   0 <= b < 2^k.
```

The exact block recurrence is

```text
q_{w,1^k} = q + (D_k b - (3^k - 2^k) alpha) / 2^k.
```

## Surplus Decomposition

Define the scaled surplus

```text
Sigma(w,k) = 2^k q_{w,1^k}.
```

Then

```text
Sigma(w,k)
= 2^k q + D_k b - (3^k - 2^k) alpha.
```

This is just the append-one positivity inequality with all denominators cleared.  The three terms have different jobs:

```text
anchor support:      2^k q
forced lift support: D_k b
one-block demand:    (3^k - 2^k) alpha
```

So append-one positivity is exactly

```text
anchor support + forced lift support >= one-block demand.
```

## Support Split

There are two local proof channels:

```text
Anchor-supported:
2^k q >= (3^k - 2^k) alpha.
```

In this channel the prior margin alone proves `q_{w,1^k} >= 0`; the forced lift residue `b` is not needed.

```text
Lift-supported:
2^k q < (3^k - 2^k) alpha.
```

Here the proof must use the congruence-forced residue

```text
b == -alpha * (3^m)^-1 mod 2^k
```

to show

```text
D_k b >= (3^k - 2^k) alpha - 2^k q.
```

The zero-lift subcase `b=0` can only be anchor-supported if positivity holds, because it contributes no `D_k b` term.

## Empirical Check

The surplus miner

```powershell
python empirical/collatz_append_one_surplus_miner.py --max-length 12 --max-total-depth 25 --max-carry 8
```

checked:

```text
words scanned:          15710500
contracting words:      15641778
append-one blocks:       6501342
decomposition failures:        0
negative q words:              0
```

In that window, only `175` append-one blocks were lift-supported; the other `6501167` were already anchor-supported.

The smallest lift-supported near-failures were:

```text
(2^2 1):       Sigma=4,  k=1, b=1
(2^3 1^2):     Sigma=8,  k=2, b=1
(3 2 1^3):     Sigma=8,  k=3, b=1
(4 1^4):       Sigma=32, k=4, b=5
```

These examples suggest that the next useful lemma should focus on the rare lift-supported channel, especially the forced small-`b` cases.  This note does not prove append-one positivity; it isolates the exact surplus split that a proof would need to close.
