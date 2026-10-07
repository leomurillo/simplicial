# H4 R4 Covariant Sweep - TTWW Orbit-Size-24 Lift Class

This is a broader sanity sweep after the two-cell verification.  It
reconstructs the TTWW arity-2 commutator orbit-size-24 lift class from
the arity-2 operator computation, then evaluates every lifted cell with
`compute_R4_covariant_at_cell.py`'s independent paired-slot recipe.
The inherited arity-2 coefficient is reported only as class metadata;
it is not used to compute any `R^(4)` value.

## Summary

- records scanned: 248
- inherited coefficient distribution: {-1: 124, 1: 124}
- unrestricted Leibniz value distribution: {-2: 40, 1: 168, 2: 40}
- paired-slot `R^(4)` value distribution: {-1: 40, 1: 168, 2: 40}
- `R^(4)=+2` records: 40
- H4 orbit-size distribution: 72: 24, 144: 112, 288: 112

The `+2` discriminator is therefore not isolated: the independent
paired-slot verifier finds the same 40-record `+2` stratum expected from
the earlier class scan, without importing the cumulant scripts.

## First ten `+2` records

| arity-2 orbit | lift | cell | entry | stage 2 | R^(4) | inherited coeff |
|---:|---|---|---|---:|---:|---:|
| 2 | beta-in | `(u, 1, u, 1)` | `1 <- 1` | 2 | 2 | -1 |
| 4 | alpha-in | `(u, w, u, w)` | `w <- w` | 2 | 2 | 1 |
| 15 | beta-in | `(u, w, u, w)` | `w <- w` | 2 | 2 | -1 |
| 25 | beta-in | `(u, w, u, w)` | `w <- w` | 2 | 2 | -1 |
| 40 | beta-in | `(u, 1, u, 1)` | `1 <- 1` | 2 | 2 | -1 |
| 75 | alpha-in | `(u, w, u, w)` | `w <- w` | 2 | 2 | 1 |
| 93 | alpha-in | `(u, 1, u, 1)` | `1 <- 1` | 2 | 2 | 1 |
| 114 | alpha-in | `(u, w, u, w)` | `w <- w` | 2 | 2 | 1 |
| 115 | beta-in | `(u, 1, u, 1)` | `1 <- 1` | 2 | 2 | -1 |
| 117 | alpha-in | `(u, 1, u, 1)` | `1 <- 1` | 2 | 2 | 1 |

## Method Guardrail

This sweep imports no `compute_h4_mobius_witness.py` or
`compute_h4_mobius_followups.py` symbols.  The only imported numerical
operators are the Section 9.1 `M`, `B^tau`, `B^omega`, and `C` pieces
already used by the verifier.
