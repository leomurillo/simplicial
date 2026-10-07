# Collatz Margin Suffix Monotonicity Note

## Setup

For a carry word `w=(s_1,...,s_m)`, write

```text
U_w(n) = (3^m n + C_w) / 2^S,
D_w    = 2^S - 3^m.
```

Assume `w` is contracting, so `D_w > 0`.  Let `r_w` be the first positive representative of the exact carry cylinder and set

```text
y_w = U_w(r_w),
q_w = (r_w - y_w)/2.
```

Append one carry `s`, and assume the child word `(w,s)` is also contracting.  Let

```text
D_{w,s} = 2^(S+s) - 3^(m+1).
```

The child residue has the form

```text
r_{w,s} = r_w + t 2^(S+1) mod 2^(S+s+1),
```

where `t mod 2^s` is forced by the next carry gate

```text
y_w + 2 * 3^m * t == a_s mod 2^(s+1),
a_s = (2^s - 1) * 3^-1 mod 2^(s+1).
```

Here `t` is represented by the integer `0 <= t < 2^s`.

## Append-Delta Identity

The exact difference is

```text
q_{w,s} - q_w =
  (2D_{w,s}t + (2^s - 3)y_w - 1) / 2^(s+1).
```

Proof:

The parent image at the lifted residue is

```text
U_w(r_w + t 2^(S+1)) = y_w + 2 * 3^m * t.
```

Therefore the child image is

```text
y_{w,s} = (3y_w + 1 + 6 * 3^m * t) / 2^s.
```

Since `q=(r-y)/2`,

```text
q_{w,s} - q_w
= (t 2^(S+1) - (y_{w,s} - y_w)) / 2
= (2D_{w,s}t + (2^s - 3)y_w - 1) / 2^(s+1).
```

## Suffix Monotonicity

If `s >= 2`, then

```text
2^s - 3 >= 1.
```

Since the child is contracting, `D_{w,s} > 0`; since `r_w` is a positive exact-cylinder representative, `y_w` is a positive odd integer; and by construction `t >= 0`.  Hence

```text
2D_{w,s}t + (2^s - 3)y_w - 1 >= y_w - 1 >= 0.
```

So

```text
q_{w,s} >= q_w        for every appended carry s >= 2.
```

For `s >= 3`, the inequality is strict because `(2^s - 3)y_w - 1 >= 4`.  For `s=2`, equality can occur only when

```text
t = 0 and y_w = 1.
```

This explains the observed `q`-preserving families such as `(2)^m` and `(1,4,2,...,2)`.

## Remaining Dangerous Channel

For `s=1`, the identity becomes

```text
q_{w,1} - q_w = (2D_{w,1}t - y_w - 1) / 4,
```

with `t in {0,1}`.  Thus append-1 can decrease `q`, and it is the only suffix channel that can do so after a contracting prefix.

The descent-margin proof target is therefore reduced to:

```text
1. Control append-1 chains.
2. Control first-contraction boundary words whose prefix is not contracting.
```

The broad suffix case `s >= 2` is no longer empirical.  It is an exact inequality.

## Computational Check

The recurrence audit

```powershell
python empirical/collatz_margin_recurrence_miner.py --max-length 8 --max-total-depth 21 --max-carry 8
```

verified the residue recurrence and append-delta identity in `355243` parent-child transitions with zero failures.  In that window:

```text
appended s >= 2: no negative deltas
appended s >= 3: strictly positive deltas
appended s = 1: the only negative deltas
negative q words: 0
```

This note does not prove the full Collatz conjecture.  It proves one reduction lemma for the `q_w >= 0` descent-margin program.
