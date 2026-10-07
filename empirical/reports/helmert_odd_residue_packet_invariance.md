# Helmert Odd-Residue Packet Invariance

This report tests the non-top odd-residue analogue of Paper 25 Theorem
3.10 in the real cosine/sine tangent basis.

For each case, the verifier compares the real Fisher Gram of
`F_p[u]/(u^k)` at target packet `u^s` with the top-packet Gram of
`F_p[u]/(u^s)`.  It also differentiates the real off-block Fisher
coupling over all cross-packet coordinate planes and records whether
the winning plane stays inside the conductor-`<=s` prefix.

## Config

- `cases`: `[(3, 3, 2), (3, 4, 2), (3, 4, 3), (5, 3, 2)]`
- `alphas`: `[0.35, 0.75]`

## Structural Checks

| row | target | alpha | prefix dim | within diff | cross max | out descent | beyond descent | columns match | pass |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| F_3[u]/(u^3) | u^2 | 0.35 | 8 | 6.661e-16 | 2.226e-17 | 3.406e-17 | 0.000e+00 | yes | PASS |
| F_3[u]/(u^3) | u^2 | 0.75 | 8 | 6.661e-16 | 8.979e-17 | 6.331e-16 | 0.000e+00 | yes | PASS |
| F_3[u]/(u^4) | u^2 | 0.35 | 8 | 6.661e-16 | 3.652e-17 | 6.812e-17 | 1.983e-17 | yes | PASS |
| F_3[u]/(u^4) | u^2 | 0.75 | 8 | 8.882e-16 | 8.587e-17 | 5.181e-16 | 1.306e-16 | yes | PASS |
| F_3[u]/(u^4) | u^3 | 0.35 | 26 | 2.548e-16 | 1.556e-17 | 1.972e-17 | 0.000e+00 | yes | PASS |
| F_3[u]/(u^4) | u^3 | 0.75 | 26 | 2.548e-16 | 3.652e-17 | 2.098e-16 | 0.000e+00 | yes | PASS |
| F_5[u]/(u^3) | u^2 | 0.35 | 24 | 2.442e-15 | 1.916e-17 | 2.340e-17 | 0.000e+00 | yes | PASS |
| F_5[u]/(u^3) | u^2 | 0.75 | 24 | 1.332e-15 | 4.390e-17 | 3.895e-16 | 0.000e+00 | yes | PASS |

## Mu Comparison

| row | reference | alpha | embedded mu | reference mu | formula real | mu diff | formula diff | factor vs complex | best class | best packets |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| F_3[u]/(u^3) | F_3[u]/(u^2) | 0.35 | 0.09288737 | 0.09288737 | 0.09288737 | 1.388e-16 | 1.943e-16 | 2 | in | [1, 2] |
| F_3[u]/(u^3) | F_3[u]/(u^2) | 0.75 | 0.7310862 | 0.7310862 | 0.7310862 | 2.220e-16 | 2.220e-16 | 2 | in | [1, 2] |
| F_3[u]/(u^4) | F_3[u]/(u^2) | 0.35 | 0.09288737 | 0.09288737 | 0.09288737 | 4.163e-17 | 1.943e-16 | 2 | in | [1, 2] |
| F_3[u]/(u^4) | F_3[u]/(u^2) | 0.75 | 0.7310862 | 0.7310862 | 0.7310862 | 2.220e-16 | 2.220e-16 | 2 | in | [1, 2] |
| F_3[u]/(u^4) | F_3[u]/(u^3) | 0.35 | 0.03096246 | 0.03096246 | 0.03096246 | 9.714e-17 | 1.735e-17 | 2 | in | [2, 3] |
| F_3[u]/(u^4) | F_3[u]/(u^3) | 0.75 | 0.418924 | 0.418924 | 0.418924 | 2.776e-16 | 0.000e+00 | 2 | in | [1, 2] |
| F_5[u]/(u^3) | F_5[u]/(u^2) | 0.35 | 0.09996717 | 0.09996717 | 0.09996717 | 4.718e-16 | 6.939e-17 | 2 | in | [1, 2] |
| F_5[u]/(u^3) | F_5[u]/(u^2) | 0.75 | 0.8055061 | 0.8055061 | 0.8055061 | 5.551e-16 | 7.772e-16 | 2 | in | [1, 2] |

## Reading

The real cross-prefix block vanishes to numerical precision; it does not
split into a nonzero conjugate-pair block.  Realification doubles the
odd-prime price relative to the complex character envelope, but that
same factor appears in both the embedded row and the quotient row, so
it cancels in the packet-local invariance comparison.
