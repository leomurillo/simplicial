# H4 Independent \(R^{(4)}\) Witness Status

**Status:** not completed.  
**Reason:** the current codebase does not yet implement the covariant
definition of \(R^{(4)}\) independently of the input-side lift / \(NC_4\)
cumulant probe.

## Target Cell

Use the original TTWW size-12 witness:

```text
witness = (tau, omega, alpha, beta, input, output)
        = (u, 1, u, 1, u, u)
commutator coefficient = -1
closed beta lift = (tau, omega, beta, input) = (u, 1, 1, u)
tested entry = u <- u
```

The existing Mobius probe gives:

```text
Pi_4 classical Mobius = -2
NC_4 non-crossing Mobius = -1
inherited arity-2 commutator target = -1
```

## What Would Count as Independent

An independent \(R^{(4)}\) computation should start from the analytic
definition in Paper 11 Section 9.3:

```text
R^(4) = S_4-symmetrized fourth covariant coefficient of K^CH
        at p_*, projected to the antisymmetric commutator component.
```

It should not use the input-side lift or the inherited arity-2 commutator
coefficient as the target.

## Missing Implementation Piece

To compute this independently, we still need an operational formula for:

1. the fourth covariant derivative of \(K^{CH}\) at \(p_*\);
2. the lower-order contraction subtraction in \(\Delta^{(4)}\);
3. the paired-slot antisymmetric commutator projection;
4. the normalization relating the symmetrized covariant coefficient to the
   matrix entry \(u\leftarrow u\).

Until those are written explicitly, an "independent \(R^{(4)}\)" computation
would simply repackage the \(NC_4\) cumulant probe and would not be an
independent check.

## Current Conclusion

Task 3 from the lead response remains open.  The right next move is to write
`Draft_0.3.1_Delta4_NC4_cumulant.md` into a precise formula for
\(\Delta^{(4)}\), then implement this independent covariant calculation
against the same TTWW size-12 cell.

