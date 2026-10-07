# H4 R4 Covariant Full Mixed-Lift Coefficient Table

This report evaluates the paired-slot `R^(4)` recipe on every lifted
mixed support record coming from the 592 arity-2 commutator orbits.  The
arity-2 computation is used only to locate the support records; the
coefficient values are recomputed by the standalone paired-slot verifier.

## Global Summary

- records scanned: 592
- inherited coefficient distribution: {-1: 296, 1: 296}
- unrestricted Leibniz value distribution: {-2: 44, 1: 504, 2: 44}
- paired-slot `R^(4)` value distribution: {-1: 44, 1: 504, 2: 44}
- H4 mixed orbit groups: 7

## Seven Mixed Orbit Groups

| family | H4 orbit | H4 orbit size | records | inherited coeffs | unrestricted Leibniz | paired-slot R^(4) |
|---|---:|---:|---:|---:|---:|---:|
| TTWW | 2 | 72 | 32 | {-1: 16, 1: 16} | {-2: 16, 2: 16} | {-1: 16, 2: 16} |
| TTWW | 3 | 144 | 56 | {-1: 28, 1: 28} | {-2: 28, 2: 28} | {-1: 28, 2: 28} |
| TTWW | 5 | 144 | 56 | {-1: 28, 1: 28} | {1: 56} | {1: 56} |
| TTWW | 4 | 288 | 112 | {-1: 56, 1: 56} | {1: 112} | {1: 112} |
| TWWW | 7 | 288 | 84 | {-1: 42, 1: 42} | {1: 84} | {1: 84} |
| TWWW | 8 | 288 | 84 | {-1: 42, 1: 42} | {1: 84} | {1: 84} |
| TWWW | 6 | 576 | 168 | {-1: 84, 1: 84} | {1: 168} | {1: 168} |

## Interpretation

The full mixed-lift coefficient table supports the same distinction as the
two-cell verifier: input-side inheritance locates the support, while the
paired-slot projection computes the signed coefficient.  The paired-slot
rule removes the crossing contribution wherever it is active; it does not
use the inherited commutator coefficient as a target value.

## Method Guardrail

This report imports no arity-4 Mobius witness or follow-up code.  It uses
only the Section 9.1 operator pieces (`M`, `B^tau`, `B^omega`, `C`) and
the arity-2 commutator support to choose which mixed records to evaluate.
