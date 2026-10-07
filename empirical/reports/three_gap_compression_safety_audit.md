# Three-Gap Compression Safety Audit

This audit tests which current-level compressions preserve the
PSL-boundary three-gap grammar.  The positive theorem-safe class is
eta-diagonal compression.  The lossy conductor modes are falsifiers:
they show what a Hayes-Mobius quotient must not do without adding a
correction term.

## Config

- `rows`: `[6, 10, 15, 30, 210]`
- `min_face_omega`: `2`
- `prefix_fractions`: `['1/3', '1/2', '2/3', '1']`
- `max_generators_per_face`: `0`
- `modes`: `['eta_diagonal', 'boundary_eta_diagonal', 'eta_conductor', 'boundary_eta_conductor', 'mobius_total', 'boundary_mobius_total']`
- `tolerance`: `1e-08`

## By Compression Mode

| mode | records | support | jump lift | jump count | zero obs | max dim | max jump classes |
|---|---:|---:|---:|---:|---:|---:|---:|
| boundary_eta_conductor | 1380 | 1368/1380 | 270/1380 | 300/1380 | 0 | 98 | 65 |
| boundary_eta_diagonal | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 1648 | 3 |
| boundary_mobius_total | 1380 | 1368/1380 | 270/1380 | 300/1380 | 0 | 50 | 65 |
| eta_conductor | 1380 | 1368/1380 | 270/1380 | 300/1380 | 0 | 11 | 65 |
| eta_diagonal | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 196 | 3 |
| mobius_total | 1380 | 1368/1380 | 270/1380 | 300/1380 | 0 | 1 | 94 |

## First Unsafe-Compression Falsifiers

| row | face | gamma | prefix | mode | dim | rotation gaps | jump classes |
|---:|---:|---:|---:|---|---:|---|---|
| 6 | 6 | 1 | 4 | eta_conductor | 1 | ['1/6', '1/2'] | ['2', '4'] |
| 6 | 6 | 1 | 4 | boundary_eta_conductor | 2 | ['1/6', '1/2'] | ['1.414214', '2.828427'] |
| 6 | 6 | 1 | 4 | mobius_total | 1 | ['1/6', '1/2'] | ['2', '4'] |
| 6 | 6 | 1 | 4 | boundary_mobius_total | 2 | ['1/6', '1/2'] | ['1.414214', '2.828427'] |
| 6 | 6 | 1 | 6 | eta_conductor | 1 | ['1/6'] | ['2', '4'] |
| 6 | 6 | 1 | 6 | boundary_eta_conductor | 2 | ['1/6'] | ['1.414214', '2.828427'] |
| 6 | 6 | 1 | 6 | mobius_total | 1 | ['1/6'] | ['2', '4'] |
| 6 | 6 | 1 | 6 | boundary_mobius_total | 2 | ['1/6'] | ['1.414214', '2.828427'] |
| 6 | 6 | 5 | 4 | eta_conductor | 1 | ['1/6', '1/2'] | ['2', '4'] |
| 6 | 6 | 5 | 4 | boundary_eta_conductor | 2 | ['1/6', '1/2'] | ['1.414214', '2.828427'] |
| 6 | 6 | 5 | 4 | mobius_total | 1 | ['1/6', '1/2'] | ['2', '4'] |
| 6 | 6 | 5 | 4 | boundary_mobius_total | 2 | ['1/6', '1/2'] | ['1.414214', '2.828427'] |

## Reading

Eta-diagonal compression preserves the three-gap jump grammar because
the compressed squared jump norm is a weighted sum of independent
character terms indexed by `eta`; each term depends only on the
adjacent rotation difference.  Conductor-only compression mixes
different character phases into the same coordinate.  Then the norm
can depend on the starting point as well as the gap, which is exactly
the failure mode recorded above.

The Paper 22 bridge is now sharper: prove the Hayes-Mobius leakage
quotient is eta-diagonal after the functorial split/flat quotient, or
is eta-diagonal plus a controlled correction whose gap-price is
accounted for separately.
