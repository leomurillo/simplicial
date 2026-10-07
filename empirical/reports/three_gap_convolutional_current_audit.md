# Three-Gap Convolutional Current Audit

This audit tests the all-order convolutional coefficient layer used by
Hayes-Mobius-style currents.  The theorem-safe statement is that
k-fold cyclic convolution of fixed character-phase data remains
diagonal by the output character label `zeta`.

## Config

- `rows`: `[6, 10, 15, 30, 210]`
- `min_face_omega`: `2`
- `prefix_fractions`: `['1/3', '1/2', '2/3', '1']`
- `max_generators_per_face`: `0`
- `seed_modes`: `['plain_count', 'mobius', 'oriented_boundary']`
- `orders`: `[1, 2, 3, 4]`
- `tolerance`: `1e-08`

## Aggregate

| check | pass | total | rate | max classes |
|---|---:|---:|---:|---:|
| support gaps | 16560 | 16560 | 100.00% | 3 |
| jump lift | 16560 | 16560 | 100.00% | 3 |
| jump count <= rotation count | 16560 | 16560 | 100.00% | 3 |

- zero current records after split quotient: `6048`
- max output character count: `196`

## By Seed And Order

| seed/order | records | support | jump lift | jump count | zero current | max outputs |
|---|---:|---:|---:|---:|---:|---:|
| mobius:k1 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 196 |
| mobius:k2 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 132 | 196 |
| mobius:k3 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 196 |
| mobius:k4 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 132 | 196 |
| oriented_boundary:k1 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 1380 | 0 |
| oriented_boundary:k2 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 1380 | 0 |
| oriented_boundary:k3 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 1380 | 0 |
| oriented_boundary:k4 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 1380 | 0 |
| plain_count:k1 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 196 |
| plain_count:k2 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 132 | 196 |
| plain_count:k3 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 0 | 196 |
| plain_count:k4 | 1380 | 1380/1380 | 1380/1380 | 1380/1380 | 132 | 196 |

## First Failures

No support, jump-lift, or jump-count failures in this run.

## Reading

For fixed boundary/Hayes-Mobius seed weights, convolution itself does
not mix starting phases.  The output coefficient at label `zeta` is
again a fixed coefficient times `chi_zeta(x_j)`.  Thus all tested
orders inherit the same three-gap support and jump-class grammar.

The remaining Paper 22 bridge is therefore not the convolutional
coefficient layer.  It is the leakage norm or compression applied
after this layer: it must be zeta-diagonal after split/flat quotienting
or have an explicit non-diagonal correction that is priced separately.
