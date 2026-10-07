# Paper 11 R4 Verification Leader Note

**Date:** May 11, 2026
**Posture:** no Heaven escalation.

## Result

The two-cell covariant verifier has passed.

```text
Cell 1: (tau, omega, beta, iota) = (u, 1, 1, u), entry u <- u
unrestricted Leibniz = -48 / 4! = -2
paired-slot R^(4)   = -24 / 4! = -1

Cell 2: (tau, omega, beta, iota) = (wu, w, wu, w), entry w <- w
paired-slot R^(4)   = 48 / 4! = 2
```

The TTWW arity-2 orbit-size-24 lift-class sweep scanned 248 records and found

```text
unrestricted Leibniz distribution: {-2: 40, 1: 168, 2: 40}
paired-slot R^(4) distribution:   {-1: 40, 1: 168, 2: 40}
```

## Interpretation

The input-side arity-2 commutator lift is the support selector.  It should not
be promoted to the signed coefficient formula.

The signed arity-4 coefficient comes from the unrestricted Leibniz expansion
followed by the paired-slot Bianchi projection.  Equivalently on four slots,
this is the \(NC_4\) contraction.  The non-crossing rule is therefore a result
of the projection, not an imported cumulant tautology.

## Action

Rewrite Paper 11 around this distinction:

1. support is inherited from the input-side lift;
2. coefficients are computed by the paired-slot \(NC_4\) contraction;
3. the full coefficient table and operadic law remain open;
4. no Heaven report is needed unless a later full-orbit coefficient table
   exposes a new ambiguity.

## Artifacts

- `empirical/compute_R4_covariant_at_cell.py`
- `empirical/reports/h4_R4_covariant_target_cell.md`
- `empirical/reports/h4_R4_covariant_plus2_cell.md`
- `empirical/reports/h4_R4_covariant_ttww_size24_sweep.md`
