# Projective Leakage Correction Budget

This audit turns Theorem 3.20 into the finite correction-budget ledger
needed for the Paper 22 projective-closure package.  The diagonal
part of a leakage Gram form is three-gap safe; the off-diagonal
correction is priced by its operator norm.

## Config

- `rows`: `[6, 10, 15, 30, 210]`
- `modes`: `['zeta_identity', 'mobius_weight_diagonal', 'conductor_weight_diagonal', 'conductor_sum', 'mobius_total']`
- `min_face_omega`: `2`
- `tolerance`: `1e-10`

## Scope / Model Summary

| scope:model | records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |
|---|---:|---:|---:|---:|---:|---:|---:|
| face_model:conductor_sum | 18 | 0/18 | 196 | 11 | 47 | 0.9791667 | 196 |
| face_model:conductor_weight_diagonal | 18 | 18/18 | 196 | 196 | 0 | 0 | 0 |
| face_model:mobius_total | 18 | 0/18 | 196 | 1 | 195 | 0.994898 | 196 |
| face_model:mobius_weight_diagonal | 18 | 18/18 | 196 | 196 | 0 | 0 | 0 |
| face_model:zeta_identity | 18 | 18/18 | 196 | 196 | 0 | 0 | 0 |
| full_row_model:conductor_sum | 5 | 0/5 | 196 | 11 | 47 | 0.9791667 | 196 |
| full_row_model:conductor_weight_diagonal | 5 | 5/5 | 196 | 196 | 0 | 0 | 0 |
| full_row_model:mobius_total | 5 | 0/5 | 196 | 1 | 195 | 0.994898 | 196 |
| full_row_model:mobius_weight_diagonal | 5 | 5/5 | 196 | 196 | 0 | 0 | 0 |
| full_row_model:zeta_identity | 5 | 5/5 | 196 | 196 | 0 | 0 | 0 |
| restriction_operator:crt_face_restriction | 18 | 18/18 | 196 | 196 | 0 | 0 | 0 |

## Full Row Scaling

| row:model | safe | labels | coordinates | ||E||_op | relative offdiag | rank(E) |
|---|---:|---:|---:|---:|---:|---:|
| 6:conductor_sum | 0/1 | 2 | 1 | 1 | 0.5 | 2 |
| 6:conductor_weight_diagonal | 1/1 | 2 | 2 | 0 | 0 | 0 |
| 6:mobius_total | 0/1 | 2 | 1 | 1 | 0.5 | 2 |
| 6:mobius_weight_diagonal | 1/1 | 2 | 2 | 0 | 0 | 0 |
| 6:zeta_identity | 1/1 | 2 | 2 | 0 | 0 | 0 |
| 10:conductor_sum | 0/1 | 4 | 1 | 3 | 0.75 | 4 |
| 10:conductor_weight_diagonal | 1/1 | 4 | 4 | 0 | 0 | 0 |
| 10:mobius_total | 0/1 | 4 | 1 | 3 | 0.75 | 4 |
| 10:mobius_weight_diagonal | 1/1 | 4 | 4 | 0 | 0 | 0 |
| 10:zeta_identity | 1/1 | 4 | 4 | 0 | 0 | 0 |
| 15:conductor_sum | 0/1 | 8 | 1 | 7 | 0.875 | 8 |
| 15:conductor_weight_diagonal | 1/1 | 8 | 8 | 0 | 0 | 0 |
| 15:mobius_total | 0/1 | 8 | 1 | 7 | 0.875 | 8 |
| 15:mobius_weight_diagonal | 1/1 | 8 | 8 | 0 | 0 | 0 |
| 15:zeta_identity | 1/1 | 8 | 8 | 0 | 0 | 0 |
| 30:conductor_sum | 0/1 | 22 | 4 | 7 | 0.875 | 22 |
| 30:conductor_weight_diagonal | 1/1 | 22 | 22 | 0 | 0 | 0 |
| 30:mobius_total | 0/1 | 22 | 1 | 21 | 0.9545455 | 22 |
| 30:mobius_weight_diagonal | 1/1 | 22 | 22 | 0 | 0 | 0 |
| 30:zeta_identity | 1/1 | 22 | 22 | 0 | 0 | 0 |
| 210:conductor_sum | 0/1 | 196 | 11 | 47 | 0.9791667 | 196 |
| 210:conductor_weight_diagonal | 1/1 | 196 | 196 | 0 | 0 | 0 |
| 210:mobius_total | 0/1 | 196 | 1 | 195 | 0.994898 | 196 |
| 210:mobius_weight_diagonal | 1/1 | 196 | 196 | 0 | 0 | 0 |
| 210:zeta_identity | 1/1 | 196 | 196 | 0 | 0 | 0 |

## CRT Face Scaling

| omega(face):model | records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2:conductor_sum | 12 | 0/12 | 24 | 1 | 23 | 0.9583333 | 24 |
| 2:conductor_weight_diagonal | 12 | 12/12 | 24 | 24 | 0 | 0 | 0 |
| 2:mobius_total | 12 | 0/12 | 24 | 1 | 23 | 0.9583333 | 24 |
| 2:mobius_weight_diagonal | 12 | 12/12 | 24 | 24 | 0 | 0 | 0 |
| 2:zeta_identity | 12 | 12/12 | 24 | 24 | 0 | 0 | 0 |
| 3:conductor_sum | 5 | 0/5 | 92 | 4 | 47 | 0.9791667 | 92 |
| 3:conductor_weight_diagonal | 5 | 5/5 | 92 | 92 | 0 | 0 | 0 |
| 3:mobius_total | 5 | 0/5 | 92 | 1 | 91 | 0.9891304 | 92 |
| 3:mobius_weight_diagonal | 5 | 5/5 | 92 | 92 | 0 | 0 | 0 |
| 3:zeta_identity | 5 | 5/5 | 92 | 92 | 0 | 0 | 0 |
| 4:conductor_sum | 1 | 0/1 | 196 | 11 | 47 | 0.9791667 | 196 |
| 4:conductor_weight_diagonal | 1 | 1/1 | 196 | 196 | 0 | 0 | 0 |
| 4:mobius_total | 1 | 0/1 | 196 | 1 | 195 | 0.994898 | 196 |
| 4:mobius_weight_diagonal | 1 | 1/1 | 196 | 196 | 0 | 0 | 0 |
| 4:zeta_identity | 1 | 1/1 | 196 | 196 | 0 | 0 | 0 |

## Restriction Operators

| records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 18/18 | 196 | 196 | 0 | 0 | 0 |

## First Unsafe Examples

| row | face | scope | mode | labels | coordinates | ||E||_op | relative offdiag | rank(E) |
|---:|---:|---|---|---:|---:|---:|---:|---:|
| 6 |  | full_row_model | conductor_sum | 2 | 1 | 1 | 0.5 | 2 |
| 6 |  | full_row_model | mobius_total | 2 | 1 | 1 | 0.5 | 2 |
| 6 | 6 | face_model | conductor_sum | 2 | 1 | 1 | 0.5 | 2 |
| 6 | 6 | face_model | mobius_total | 2 | 1 | 1 | 0.5 | 2 |
| 10 |  | full_row_model | conductor_sum | 4 | 1 | 3 | 0.75 | 4 |
| 10 |  | full_row_model | mobius_total | 4 | 1 | 3 | 0.75 | 4 |
| 10 | 10 | face_model | conductor_sum | 4 | 1 | 3 | 0.75 | 4 |
| 10 | 10 | face_model | mobius_total | 4 | 1 | 3 | 0.75 | 4 |
| 15 |  | full_row_model | conductor_sum | 8 | 1 | 7 | 0.875 | 8 |
| 15 |  | full_row_model | mobius_total | 8 | 1 | 7 | 0.875 | 8 |
| 15 | 15 | face_model | conductor_sum | 8 | 1 | 7 | 0.875 | 8 |
| 15 | 15 | face_model | mobius_total | 8 | 1 | 7 | 0.875 | 8 |
| 30 |  | full_row_model | conductor_sum | 22 | 4 | 7 | 0.875 | 22 |
| 30 |  | full_row_model | mobius_total | 22 | 1 | 21 | 0.9545455 | 22 |
| 30 | 6 | face_model | conductor_sum | 2 | 1 | 1 | 0.5 | 2 |
| 30 | 6 | face_model | mobius_total | 2 | 1 | 1 | 0.5 | 2 |

## Reading

The diagonal identity, Mobius-weight, and conductor-depth norms have
`E=0` on every row and CRT face tested.  The normalized CRT face
restriction operators are also diagonal-safe.  The conductor-sum and
Mobius-total models are deliberately unsafe phase-mixing comparisons:
their correction rank and relative off-diagonal mass grow with the
available non-split character labels.

For Paper 22, this says the projective closure theorem can use the
three-gap grammar only after the actual leakage form is proved
zeta-diagonal on the split/flat quotient, or after the correction
budget is shown to vanish along the tower.
