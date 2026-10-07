# Tower Quotient Saturation Scan

- JSON artifact: `C:\Projects\simplicial\empirical\reports\tower_quotient_saturation.json`
- Tower leaf: top-two suffix packet `{u^(e-1), u^e}` in `F_2[u]/(u^e)`.
- Exact rows are loaded from `per_leaf_coboundary_audit`; extension rows are raw quotient-pressure rows and do not claim residual reduction.
- Modular rows are loaded from `streaming_modular_residual`; they give finite-field residual data, not rational closure proofs.
- Saturation target: show normalized residual orbit mass tends to zero and the full higher-current quotient vanishes in the inverse limit.
- This report is not a finite full-closure certificate.

## Tower Indicators

- C2-volume residual mass halves on exact rows: `True`
- Orbit residual mass strictly decreases on exact rows: `True`
- C2-volume residual mass halves on all reduced rows: `True`
- Orbit residual mass strictly decreases on all reduced rows: `True`
- Available C2-volume pressure halves including raw extension rows: `True`
- Available orbit pressure mass strictly decreases including raw extension rows: `True`
- Relative full-block deficit remains 1 on exact rows: `True`
- Support H4->H3 orbit cokernel is zero where available: `True`

| e | leaf | row kind | field | reduced residual | C2 dim | raw support | residual support | deficit | nu_E raw | nu_E residual | C2 orbit vol | raw orbit support | raw orbit mass | residual orbit support | residual orbit mass | H3 orbits | H4 orbits | H4->H3 cokernel | seconds |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | `u+u^2` | exact_reduced | Q | True | 61 | 4 | 4 | 1.000000 | 0.065574 | 0.065574 | 31 | 2 | 0.064516 | 2 | 0.064516 | 1 | 4 | 0 | 0.006000 |
| 3 | `u^2+u^3` | exact_reduced | Q | True | 976 | 32 | 32 | 1.000000 | 0.032787 | 0.032787 | 136 | 6 | 0.044118 | 6 | 0.044118 | 1 | 8 | 0 | 0.095000 |
| 4 | `u^3+u^4` | exact_reduced | Q | True | 15616 | 256 | 256 | 1.000000 | 0.016393 | 0.016393 | 612 | 20 | 0.032680 | 20 | 0.032680 | 1 | 16 | 0 | 1.915000 |
| 5 | `u^4+u^5` | exact_reduced | Q | True | 249856 | 2048 | 2048 | 1.000000 | 0.008197 | 0.008197 | 2544 | 48 | 0.018868 | 48 | 0.018868 | 1 | 28 | 0 | 75.119000 |
| 6 | `u^5+u^6` | modular_reduced | F_1000003 | True | 3997696 | 16384 | 16384 | 1.000000 | 0.004098 | 0.004098 | 10496 | 116 | 0.011052 | 116 | 0.011052 | n/a | n/a | n/a | 554.857000 |

## Reading

The exact rational rows through the original reduction frontier do not close finitely: the relative full-block residual deficit stays `1.0`.  The streaming modular row at the next suffix depth also has residual deficit `1.0`, but now its quotient-pressure datum is an actual modular residual-orbit datum.  The C2-volume mass halves along the reduced suffix tower, and the orbit-quotient residual mass is strictly decreasing on the same reduced rows.  The support-level H4-to-H3 orbit cokernel is already zero where the support quotient is computed.

The tower theorem target is therefore sharper: prove that the inverse-system transition maps turn this decreasing quotient mass into zero limiting higher-current quotient, or exhibit a stable residual class that survives despite the finite support-orbit saturation.
