# H4 R4 Covariant Verification - Target Cell

This report computes the two-cell `R^(4)` verifier directly from the
Section 9.1 operator ingredients.  The script imports `M`, `B^tau`,
`B^omega`, and `C` through `elementary_expansion`; it does not import
the existing arity-4 witness or follow-up code.

## Cell

```text
cell  = (u, 1, 1, u)
entry = u <- u
tau displacement   = u
omega displacement = 1
sum(cell) = 0
H4 orbit = 2, family = TTWW, size = 72
source = original sealed target
witness = (u, 1, u, 1, u, u)
lift = beta-in, cell = (u, 1, 1, u)
```

## Stage 1 - Taylor Pieces

| slot | label | cond | M nz | B_tau nz | B_omega nz | C nz | M entry | B_tau entry | B_omega entry | C entry |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tau | u | u | 14 | 15 | 14 | 14 | 0 | -2 | 0 | 0 |
| omega | 1 | u^2 | 14 | 14 | 15 | 14 | 0 | 0 | -1 | 0 |
| beta | 1 | u^2 | 14 | 14 | 15 | 14 | 0 | 0 | -1 | 0 |
| iota | u | u | 14 | 15 | 14 | 14 | 0 | -2 | 0 | 0 |

The direct mixed path check is recorded separately from the contraction
calculation:

```text
[s r] K(x1)K(x2)K(x3)K(x4) entry = 0
[s r] K(x1+x2+x3+x4) entry        = 0
direct product-minus-composed entry = 0
```

## Stage 2 - Unrestricted Leibniz Contraction

All 15 product-rule contractions are generated.  No non-crossing filter is
applied at this stage.

| contraction | block labels | base entry | Leibniz coeff | raw contribution |
|---|---|---:|---:|---:|
| `{tau,omega,beta,iota}` | `0` | 1 | 1 | 24 |
| `{tau,omega,beta} | {iota}` | `u | u` | 0 | -1 | 0 |
| `{tau,omega,iota} | {beta}` | `1 | 1` | 1 | -1 | -24 |
| `{tau,omega} | {beta,iota}` | `1+u | 1+u` | 1 | -1 | -24 |
| `{tau,omega} | {beta} | {iota}` | `1+u | 1 | u` | 0 | 2 | 0 |
| `{tau,beta,iota} | {omega}` | `1 | 1` | 1 | -1 | -24 |
| `{tau,beta} | {omega,iota}` | `1+u | 1+u` | 1 | -1 | -24 |
| `{tau,beta} | {omega} | {iota}` | `1+u | 1 | u` | 0 | 2 | 0 |
| `{tau,iota} | {omega,beta}` | `0 | 0` | 1 | -1 | -24 |
| `{tau} | {omega,beta,iota}` | `u | u` | 0 | -1 | 0 |
| `{tau} | {omega,beta} | {iota}` | `u | 0 | u` | 0 | 2 | 0 |
| `{tau,iota} | {omega} | {beta}` | `0 | 1 | 1` | 1 | 2 | 48 |
| `{tau} | {omega,iota} | {beta}` | `u | 1+u | 1` | 0 | 2 | 0 |
| `{tau} | {omega} | {beta,iota}` | `u | 1 | 1+u` | 0 | 2 | 0 |
| `{tau} | {omega} | {beta} | {iota}` | `u | 1 | 1 | u` | 0 | -6 | 0 |

```text
raw unrestricted Leibniz entry = -48
after 1/4! normalization       = -2
```

## Stage 3 - Paired-Slot Projection

The six-term paired-slot alternation cancels the middle pair-of-pairs
`(tau,beta;omega,iota)` and propagates that cancellation through its
Leibniz refinements.  The table shows the correction applied after the
unrestricted expansion has already been formed.

| contraction | Leibniz coeff | Bianchi correction | projected coeff | raw projected contribution |
|---|---:|---:|---:|---:|
| `{tau,omega,beta,iota}` | 1 | 0 | 1 | 24 |
| `{tau,omega,beta} | {iota}` | -1 | 0 | -1 | 0 |
| `{tau,omega,iota} | {beta}` | -1 | 0 | -1 | -24 |
| `{tau,omega} | {beta,iota}` | -1 | 0 | -1 | -24 |
| `{tau,omega} | {beta} | {iota}` | 2 | 0 | 2 | 0 |
| `{tau,beta,iota} | {omega}` | -1 | 0 | -1 | -24 |
| `{tau,beta} | {omega,iota}` | -1 | 1 | 0 | 0 |
| `{tau,beta} | {omega} | {iota}` | 2 | -1 | 1 | 0 |
| `{tau,iota} | {omega,beta}` | -1 | 0 | -1 | -24 |
| `{tau} | {omega,beta,iota}` | -1 | 0 | -1 | 0 |
| `{tau} | {omega,beta} | {iota}` | 2 | 0 | 2 | 0 |
| `{tau,iota} | {omega} | {beta}` | 2 | 0 | 2 | 48 |
| `{tau} | {omega,iota} | {beta}` | 2 | -1 | 1 | 0 |
| `{tau} | {omega} | {beta,iota}` | 2 | 0 | 2 | 0 |
| `{tau} | {omega} | {beta} | {iota}` | -6 | 1 | -5 | 0 |

```text
raw projected entry = -24
```

## Stage 4 - Normalization

```text
R^(4) entry = -24 / 24 = -1
```

## Outcome

Cell 1 returns `-1`: Heaven's recipe is verified at the sealed target cell.
