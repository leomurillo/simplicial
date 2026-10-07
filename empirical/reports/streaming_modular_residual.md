# Streaming Modular Residual Audit

- JSON artifact: `empirical\reports\streaming_modular_residual.json`
- Scope: selected conductor leaf, full-block C2 coordinates, full-block section changes inside the leaf.
- Coefficients are finite-field modular; rows are residual evidence, not rational finite-closure proofs.

| target | field | status | C2 dim | C1 processed | rank | raw support | residual support | deficit | C2 orbit vol | residual orbit support | orbit residual mass | nu_E residual | raw=coboundary | seconds |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| f2-u6 | F_1000003 | complete | 3997696 | 69632 | 69376 | 16384 | 16384 | 1.000000 | 10496 | 116 | 0.011052 | 0.004098 | False | 554.857000 |
| f8-u2 | F_1000003 | complete | 12845056 | 200704 | 200704 | 25088 | 25088 | 1.000000 | 76480 | 152 | 0.001987 | 0.001953 | False | 573.375000 |

## Reading

These rows convert quotient pressure into modular residual-orbit data when status is `complete`.  A generator-limited row is only a progress artifact and must not be read as a full residual result.
