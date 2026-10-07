# H4 Mobius Witness Probe

This is a one-cell test for the arity-4 lower-contraction formula in
Paper 11.  It compares classical partition Mobius inversion on Pi_4
with non-crossing Mobius inversion on NC_4.

## Chosen size-12 commutator witness

```text
witness = (tau, omega, alpha, beta, input, output)
        = (u, 1, u, 1, u, u)
commutator coefficient = -1
commutator orbit size = 12
```

The closed input-side beta lift is

```text
cell = (tau, omega, beta, input)
     = (u, 1, 1, u)
sum(cell) = 0
H4 orbit = 2, family = TTWW, orbit size = 72
tested matrix entry = input <- input = u <- u
```

The inherited arity-2 commutator coefficient is used as the provisional
single-cell target because the current codebase has no independent
coefficient-level implementation of R^(4).

## Result

| candidate | partitions | value at input diagonal | matches inherited coefficient? |
|---|---:|---:|---|
| Pi_4 classical Mobius | 15 | -2 | False |
| NC_4 non-crossing Mobius | 14 | -1 | True |

On this witness, NC_4 matches the inherited commutator coefficient and
Pi_4 overshoots by the single crossing partition.

The full cumulant operators are sparse:

- Pi_4 nonzero entries: 3, coefficient distribution {-2: 2, 2: 1}
- NC_4 nonzero entries: 3, coefficient distribution {-1: 2, 1: 1}

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

The crossing partition

```text
{tau,beta} | {omega,iota}
```

has base entry 1 and classical contribution -1.  It is absent from
NC_4.  Removing exactly this contribution changes the value from -2
to -1.

## Interpretation

For this size-12 witness, the non-crossing Mobius contraction is the
candidate compatible with the inherited arity-2 curvature coefficient.
This is not yet a proof of Theorem 9.3's coefficient formula, but it is
strong evidence that Option A-prime should be written with NC_4 lower
contractions rather than all of Pi_4.
