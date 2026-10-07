# Non-Reversible Resolvent Audit

- Claim tested: non-reversible generator escape hatch for Green-kernel recovery
- Grid dimensions: `(9, 9, 9)`
- State count: 729

| model | q4 | unit q4 | symbol A | current rel flux | 1/r R2 | slope | shell CV mean |
|---|---:|---:|---:|---:|---:|---:|---:|
| local_reversible | 1.666667e-01 | 4.115226e-03 | 0.000000e+00 | 0.000000e+00 | 9.841589e-01 | 8.647825e-03 | 3.714930e-02 |
| local_drift | 1.666667e-01 | 4.115226e-03 | 0.000000e+00 | 5.000000e-02 | 9.611556e-01 | 8.551411e-03 | 9.800539e-01 |
| complete | 1.254943e+00 | 1.034294e-01 | 2.694141e-15 | 0.000000e+00 | -1.529883e+01 | 5.192033e-20 | 1.531876e-17 |
| complete_plus_drift | 1.184409e+00 | 1.005406e-01 | 2.615776e-15 | 1.875000e-01 | 4.721327e-01 | 3.678937e-03 | 2.257331e-01 |

## Interpretation

Local drift-diffusion may retain a local 1/r-like singular profile,
but only when the jump carre-du-champ is already local. Mean-field
complete jumps keep a bad locality diagnostic and do not acquire a
1/r resolvent profile from adding a current. This finite test keeps
the no-go stated as reversible unless a broader non-reversible,
nonlocal construction is explicitly supplied.
