# H4 Mobius Follow-up: TTWW Size-24 Witness

This is a follow-up to `empirical/reports/h4_mobius_witness.md`.
It compares classical Pi_4 Mobius contraction with NC_4 Mobius
contraction on one additional lifted commutator cell.

This report uses a TTWW witness from an arity-2 commutator orbit
of size 24.  It is chosen so that NC_4 matches the inherited
commutator coefficient while Pi_4 does not.

## Chosen witness

```text
witness = (tau, omega, alpha, beta, input, output)
        = (wu, 1+u, w+(w+1)u, 1+u, wu, w+(w+1)u)
commutator coefficient = -1
commutator orbit size = 24
lift = beta-in
cell = (wu, 1+u, 1+u, wu)
sum(cell) = 0
H4 orbit = 3, family = TTWW, orbit size = 144
tested entry = wu <- wu
```

## Result

| candidate | partitions | value at input diagonal | matches inherited coefficient? |
|---|---:|---:|---|
| Pi_4 classical Mobius | 15 | -2 | False |
| NC_4 non-crossing Mobius | 14 | -1 | True |

Full cumulant operator distributions:

- Pi_4 nonzero entries: 3, distribution {-2: 2, 2: 1}
- NC_4 nonzero entries: 3, distribution {-1: 2, 1: 1}

## Class scan

- records in class TTWW, arity-2 orbit size 24: 248
- inherited coefficient distribution: {-1: 124, 1: 124}
- Pi_4 value distribution: {-2: 40, 1: 168, 2: 40}
- NC_4 value distribution: {-1: 40, 1: 168, 2: 40}
- Pi_4 matches inherited coefficient: 84 / 248
- NC_4 matches inherited coefficient: 104 / 248

## Partition contribution table

| partition | crossing? | base entry | mu_Pi | Pi contribution | mu_NC | NC contribution |
|---|---|---:|---:|---:|---:|---:|
| `{tau,omega,beta,iota}` | no | 1 | 1 | 1 | 1 | 1 |
| `{tau} | {omega,beta,iota}` | no | 0 | -1 | 0 | -1 | 0 |
| `{tau,omega} | {beta,iota}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,omega,beta} | {iota}` | no | 0 | -1 | 0 | -1 | 0 |
| `{tau,omega,iota} | {beta}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,beta} | {omega,iota}` | yes | 1 | -1 | -1 | - | - |
| `{tau,beta,iota} | {omega}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau,iota} | {omega,beta}` | no | 1 | -1 | -1 | -1 | -1 |
| `{tau} | {omega} | {beta,iota}` | no | 0 | 2 | 0 | 2 | 0 |
| `{tau} | {omega,beta} | {iota}` | no | 0 | 2 | 0 | 2 | 0 |
| `{tau} | {omega,iota} | {beta}` | no | 0 | 2 | 0 | 1 | 0 |
| `{tau,omega} | {beta} | {iota}` | no | 0 | 2 | 0 | 2 | 0 |
| `{tau,beta} | {omega} | {iota}` | no | 0 | 2 | 0 | 1 | 0 |
| `{tau,iota} | {omega} | {beta}` | no | 1 | 2 | 2 | 2 | 2 |
| `{tau} | {omega} | {beta} | {iota}` | no | 0 | -6 | 0 | -5 | 0 |
