# Constraint 3 Cubic Noether Verification

## Status

- JSON artifact: `C:\Projects\simplicial\empirical\reports\constraint3_cubic_noether_verification.json`
- theorem source: Paper 17, Definition 2.1 and Theorems 2.2-2.3
- retired FFT proxy: not used
- vector field: volume-dual Nambu-Fisher field on a linear regular leaf
- charge density: scale-normalized `T_p(h, X_C, X_C)` along the trajectory
- closure residual: Fisher fraction of `K^CH_p(X_C, X_C)` outside the squarefree two-prime support
- seeds per row: `50`
- amplitude / initial Fisher speed: `0.04` / `0.02`
- horizon / RK4 steps: `1.0` / `240`
- numerical floor used for SNR: `1.0e-14`

This is the first trajectory-level audit for Constraint 3.  It does not
use `sum(IFFT(FFT(J)^3))`; it follows an actual Nambu-Fisher trajectory
and contracts the Amari-Chentsov cubic with the trajectory vector field.

## Row Summary

| row | support | outside | mean abs normalized charge | mean leakage | median leakage | max leakage | SNR vs Z/6 floor | assessment |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 6 | `[2, 3, 6]` | `[]` | 0.457667 | 3.130e-32 | 2.995e-32 | 2.248e-31 | n/a | known-closed baseline at numerical floor |
| 12 | `[2, 3, 6]` | `[4, 12]` | 0.518829 | 9.500e-32 | 4.569e-32 | 1.973e-30 | 9.500e-18 | no cubic-force leakage above baseline |
| 18 | `[2, 3, 6]` | `[9, 18]` | 0.556986 | 5.221e-32 | 5.131e-32 | 4.486e-31 | 5.221e-18 | no cubic-force leakage above baseline |

## Interpretation

The `Z/6Z` row is the known-closed Paper 17 baseline.  Its outside
support is empty because the squarefree two-prime support is the full
nontrivial conductor support.  Its leakage therefore measures numerical
floor only.

For `Z/12Z` and `Z/18Z`, the same squarefree support `{2, 3, 6}` is
embedded in a row with prime-power depth.  Leakage measures whether the
genuine cubic force exits that squarefree support into the depth packets.
This is a real cubic response diagnostic; it is not a random-phase mean.

## Per-Row Seed Ranges

| row | min leakage | median leakage | max leakage | min probability | max sum error |
|---:|---:|---:|---:|---:|---:|
| 6 | 1.862e-32 | 2.995e-32 | 5.147e-32 | 0.146588 | 4.441e-16 |
| 12 | 2.276e-32 | 4.569e-32 | 1.251e-30 | 0.072959 | 4.441e-16 |
| 18 | 2.461e-32 | 5.131e-32 | 7.632e-32 | 0.048385 | 2.220e-16 |

## Reproduction

```powershell
python empirical/constraint3_cubic_noether_verification.py
```
