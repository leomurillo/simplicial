# Collatz Append-One Lift Channel Note

## Setup

For a contracting anchor `w`, append `1^k` and assume the child is contracting.  Use the notation from the append-one block recurrence:

```text
alpha = (y_w+1)/2,
D_k   = 2^(S+k)-3^(m+k),
b     == -alpha * (3^m)^-1 mod 2^k,   0 <= b < 2^k.
```

The scaled surplus is

```text
Sigma = 2^k q_{w,1^k}
      = 2^k q_w + D_k b - (3^k - 2^k) alpha.
```

The append-one block is anchor-supported when

```text
2^k q_w >= (3^k - 2^k) alpha.
```

The remaining rare channel is the lift-supported channel:

```text
2^k q_w < (3^k - 2^k) alpha.
```

## Exact Copy-Cover Lemma

In the lift-supported channel, define the positive deficit

```text
E = (3^k - 2^k) alpha - 2^k q_w > 0.
```

Since `D_k>0`, define

```text
N = ceil(E / D_k).
```

Then

```text
q_{w,1^k} >= 0    iff    N <= b.
```

Proof:

```text
2^k q_{w,1^k} = D_k b - E.
```

Because `D_k` is positive, `D_k b >= E` is equivalent to `b >= ceil(E/D_k)`.  This is exactly `N <= b`.

This lemma is only a repackaging of the local recurrence, but it is useful: the dangerous question is no longer whether `D_k b` is large enough in the abstract.  It is whether the congruence-forced lift residue `b` supplies at least `N` copies of the positive denominator `D_k`.

## One-Copy Sublemma

If

```text
E <= D_k,
```

then `N=1`.  Since lift-supported cases have `E>0`, they cannot have `b=0`; hence `b>=1`, and the child has nonnegative `q`.

So a tempting local proof route is:

```text
Lift-supported one-copy lemma:
For every lift-supported append-one block, either E <= D_k,
or the block belongs to a small explicitly controlled exceptional family.
```

This route is useful as a diagnostic, but it is not true as a global theorem without a genuine multi-copy channel; see the counterexample update below.

## Empirical Check

The lift-channel miner

```powershell
python empirical/collatz_append_one_lift_channel_miner.py --max-length 12 --max-total-depth 25 --max-carry 8
```

checked:

```text
words scanned:          15710500
contracting words:      15641778
append-one blocks:       6501342
anchor-supported blocks: 6501167
lift-supported blocks:       175
forced-cover failures:         0
```

Required lift-copy counts in this window:

```text
N=1: 174 cases
N=3:   1 case
```

The unique observed multi-copy case is

```text
child:  (4 1^4)
anchor: (4)
k:      4
alpha:  1
q_w:    2
D_k:    13
b:      5
E:      33
N:      ceil(33/13) = 3
Sigma:  13*5 - 33 = 32
```

So the finite-window picture is extremely sharp:

```text
anchor-supported channel: 6501167 cases
one-copy lift channel:        174 cases
explicit multi-copy case:       1 case
```

This is not a proof of append-one positivity.  It reduces the rare lift-supported obligation to the copy-cover inequality `N <= b`.

## Counterexample Update

The proposed universal one-copy bound

```text
E <= D_k
```

is false.  The smallest failure is already `(4 1^4)`:

```text
q_w = 2, alpha = 1, D_k = 13, b = 5,
E = 33,
N = ceil(33/13) = 3.
```

The child is still positive because

```text
D_k b - E = 13*5 - 33 = 32.
```

A targeted counterexample search also finds larger multi-copy examples such as

```text
(8 4 1^15):
D_k = 5077565,
E   = 5654956,
N   = 2,
b   = 18204.
```

So the corrected theorem-facing target is:

```text
Copy-cover lemma:
In the lift-supported channel, prove N <= b.
```

The one-copy bound remains a useful majority sublemma, but the proof program must include a real multi-copy channel rather than treating `(4 1^4)` as the only possible exception.
