# Collatz Append-One One-Copy Bound Disproof

## Claim Tested

In the lift-supported append-one channel, define

```text
E = (3^k - 2^k) alpha - 2^k q_w > 0,
D_k = 2^(S+k)-3^(m+k),
N = ceil(E/D_k).
```

The proposed one-copy bound was

```text
E <= D_k.
```

If true, it would force `N=1`, and since every lift-supported case has `b>0`, append-one positivity would follow immediately from one copy of `D_k`.

## Disproof

The bound is false.  Take the anchor word

```text
w = (4)
```

and append `1^4`.  The exact anchor data are

```text
q_w = 2,
y_w = 1,
alpha = (y_w+1)/2 = 1.
```

For `k=4`,

```text
D_k = 2^(4+4)-3^(1+4) = 256 - 243 = 13,
3^k - 2^k = 81 - 16 = 65.
```

Therefore

```text
E = 65*1 - 16*2 = 33.
```

So

```text
E = 33 > 13 = D_k.
```

The one-copy bound fails.

However, the forced lift residue is

```text
b == -alpha * (3^1)^-1 mod 16
  == -1 * 11 mod 16
  == 5 mod 16.
```

Thus

```text
N = ceil(33/13) = 3 <= 5 = b,
```

and the actual surplus is positive:

```text
2^4 q_{(4,1,1,1,1)}
= D_k b - E
= 13*5 - 33
= 32.
```

So this is not a counterexample to append-one positivity.  It is a counterexample to the one-copy shortcut.

## Larger Failures

The counterexample miner

```powershell
python empirical/collatz_append_one_lift_counterexample_miner.py --max-anchor-length 4 --max-anchor-total-depth 16 --max-carry 10 --max-run 30
```

found:

```text
anchors scanned:          2360
contracting anchors:      2337
children checked:        28193
lift-supported children:   345
one-copy failures:           6
forced-cover failures:       0
```

The earliest failures are:

```text
(4 1^4):       N=3, b=5
(10 2 1^15):   N=2, b=29127
(2 10 1^15):   N=2, b=18204
(4 8 1^15):    N=2, b=29127
(7 5 1^15):    N=2, b=21845
(8 4 1^15):    N=2, b=18204
```

## Corrected Target

The exact lift-supported obligation is not the one-copy bound.  It is:

```text
Copy-cover lemma:
N <= b,
where N = ceil(E/D_k)
and b == -alpha * (3^m)^-1 mod 2^k.
```

A proof may still split off the majority `N=1` channel, but it must also control genuine multi-copy cases.  The forced residue `b` is very large in the longer failures, which suggests the multi-copy channel may be easier than the small `(4 1^4)` exception once it is stated correctly.
