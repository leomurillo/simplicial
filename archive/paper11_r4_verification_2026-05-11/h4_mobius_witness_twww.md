# H4 Mobius Follow-up: TWWW Witness

This is a follow-up to `empirical/reports/h4_mobius_witness.md`.
It compares classical Pi_4 Mobius contraction with NC_4 Mobius
contraction on one additional lifted commutator cell.

The requested TWWW size-12 class is empty under the measured
input-side lift:

- TWWW size-12 records: 0
- TWWW size-24 records: 336

This report therefore uses a minimal TWWW witness, which has
arity-2 commutator orbit size 24.

## Chosen witness

```text
witness = (tau, omega, alpha, beta, input, output)
        = ((w+1)u, 1+u, w+1, (w+1)u, w+wu, (w+1)u)
commutator coefficient = 1
commutator orbit size = 24
lift = alpha-in
cell = ((w+1)u, 1+u, w+1, w+wu)
sum(cell) = 0
H4 orbit = 7, family = TWWW, orbit size = 288
tested entry = w+wu <- w+wu
```

## Result

| candidate | partitions | value at input diagonal | matches inherited coefficient? |
|---|---:|---:|---|
| Pi_4 classical Mobius | 15 | 1 | True |
| NC_4 non-crossing Mobius | 14 | 1 | True |

Full cumulant operator distributions:

- Pi_4 nonzero entries: 7, distribution {-3: 1, -1: 2, 1: 3, 3: 1}
- NC_4 nonzero entries: 7, distribution {-2: 1, -1: 2, 1: 3, 2: 1}

## Class scan

- records in class TWWW, arity-2 orbit size 24: 336
- inherited coefficient distribution: {-1: 168, 1: 168}
- Pi_4 value distribution: {1: 336}
- NC_4 value distribution: {1: 336}
- Pi_4 matches inherited coefficient: 168 / 336
- NC_4 matches inherited coefficient: 168 / 336

## Partition contribution table

| partition | crossing? | base entry | mu_Pi | Pi contribution | mu_NC | NC contribution |
|---|---|---:|---:|---:|---:|---:|
| `{tau,omega,alpha,iota}` | no | 1 | 1 | 1 | 1 | 1 |
| `{tau} | {omega,alpha,iota}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,omega} | {alpha,iota}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,omega,alpha} | {iota}` | no | 0 | -1 | 0 | -1 | 0 |
| `{tau,omega,iota} | {alpha}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,alpha} | {omega,iota}` | yes | 1 | -1 | -1 | - | - |
| `{tau,alpha,iota} | {omega}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,iota} | {omega,alpha}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau} | {omega} | {alpha,iota}` | no | 1 | 2 | 2 | 2 | 2 |
| `{tau} | {omega,alpha} | {iota}` | no | 0 | 2 | 0 | 2 | 0 |
| `{tau} | {omega,iota} | {alpha}` | no | 1 | 2 | 2 | 1 | 1 |
| `{tau,omega} | {alpha} | {iota}` | no | 0 | 2 | 0 | 2 | 0 |
| `{tau,alpha} | {omega} | {iota}` | no | 0 | 2 | 0 | 1 | 0 |
| `{tau,iota} | {omega} | {alpha}` | no | 1 | 2 | 2 | 2 | 2 |
| `{tau} | {omega} | {alpha} | {iota}` | no | 0 | -6 | 0 | -5 | 0 |
