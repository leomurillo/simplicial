# Helmert Odd-Residue Top-Packet Formula

This report tests the odd-prime analogue of Paper 25 Theorem 3.12 in the
real tangent basis.  For odd `p`, additive characters come in conjugate
pairs, so the real cosine/sine coordinate-plane price is twice the
complex-character branch envelope:

\[
\mu^{\mathrm{real}}_{p,k}(\alpha)
=
2\max\{\mu^{\mathrm{top},+}_{p,k}(\alpha),\mu^{\mathrm{nt}}_{p,k}(\alpha)\}.
\]

The branch formulas inside the maximum are the same as Theorem 3.12 with
`F=p`.

## Config

- `alphas`: `[0.35, 0.75]`
- `epsilon`: `1e-06`

## Finite-Difference Verification

| p | k | alpha | numeric mu | formula mu | rel err | numeric packet pair | formula branch |
|---:|---:|---:|---:|---:|---:|---|---|
| 3 | 2 | 0.35 | 0.09288758 | 0.09288737 | 2.249e-06 | [1, 2] | top |
| 3 | 2 | 0.75 | 0.7310883 | 0.7310862 | 2.819e-06 | [1, 2] | top |
| 3 | 3 | 0.35 | 0.03096251 | 0.03096246 | 1.742e-06 | [2, 3] | top |
| 3 | 3 | 0.75 | 0.4189244 | 0.418924 | 1.000e-06 | [1, 2] | non-top |
| 5 | 2 | 0.35 | 0.09996722 | 0.09996717 | 4.218e-07 | [1, 2] | top |
| 5 | 2 | 0.75 | 0.8055057 | 0.8055061 | 5.145e-07 | [1, 2] | top |
| 7 | 2 | 0.35 | 0.07452994 | 0.07452994 | 1.001e-08 | [1, 2] | top |
| 7 | 2 | 0.75 | 0.5536104 | 0.5536113 | 1.549e-06 | [1, 2] | top |

## Formula Table

| p | k | alpha | real envelope | real top | real non-top | branch | alpha threshold |
|---:|---:|---:|---:|---:|---:|---|---:|
| 3 | 2 | 0.35 | 0.09288737 | 0.09288737 | 0 | top | -- |
| 3 | 2 | 0.75 | 0.7310862 | 0.7310862 | 0 | top | -- |
| 3 | 3 | 0.35 | 0.03096246 | 0.03096246 | 0.007818628 | top | 0.6164024 |
| 3 | 3 | 0.75 | 0.418924 | 0.2436954 | 0.418924 | non-top | 0.6164024 |
| 3 | 4 | 0.35 | 0.01032082 | 0.01032082 | 0.003474946 | top | 0.5515188 |
| 3 | 4 | 0.75 | 0.1861884 | 0.0812318 | 0.1861884 | non-top | 0.5515188 |
| 5 | 2 | 0.35 | 0.09996717 | 0.09996717 | 0 | top | -- |
| 5 | 2 | 0.75 | 0.8055061 | 0.8055061 | 0 | top | -- |
| 5 | 3 | 0.35 | 0.01999343 | 0.01999343 | 0.008278891 | top | 0.5301169 |
| 5 | 3 | 0.75 | 0.3446373 | 0.1611012 | 0.3446373 | non-top | 0.5301169 |
| 5 | 4 | 0.35 | 0.003998687 | 0.003998687 | 0.001986934 | top | 0.4869736 |
| 5 | 4 | 0.75 | 0.08271295 | 0.03222024 | 0.08271295 | non-top | 0.4869736 |
| 7 | 2 | 0.35 | 0.07452994 | 0.07452994 | 0 | top | -- |
| 7 | 2 | 0.75 | 0.5536113 | 0.5536113 | 0 | top | -- |
| 7 | 3 | 0.35 | 0.01064713 | 0.01064713 | 0.00660303 | top | 0.4409359 |
| 7 | 3 | 0.75 | 0.2419311 | 0.07908732 | 0.2419311 | non-top | 0.4409359 |
| 7 | 4 | 0.35 | 0.001521019 | 0.001521019 | 0.001078046 | top | 0.4134511 |
| 7 | 4 | 0.75 | 0.03949895 | 0.01129819 | 0.03949895 | non-top | 0.4134511 |
| 11 | 2 | 0.35 | 0.0419548 | 0.0419548 | 0 | top | -- |
| 11 | 2 | 0.75 | 0.2825656 | 0.2825656 | 0 | top | -- |
| 11 | 3 | 0.35 | 0.004006647 | 0.003814072 | 0.004006647 | non-top | 0.3416272 |
| 11 | 3 | 0.75 | 0.1290346 | 0.02568778 | 0.1290346 | non-top | 0.3416272 |
| 11 | 4 | 0.35 | 0.0003973534 | 0.0003467339 | 0.0003973534 | non-top | 0.3273153 |
| 11 | 4 | 0.75 | 0.01279682 | 0.002335253 | 0.01279682 | non-top | 0.3273153 |
| 13 | 2 | 0.35 | 0.0327868 | 0.0327868 | 0 | top | -- |
| 13 | 2 | 0.75 | 0.2142996 | 0.2142996 | 0 | top | -- |
| 13 | 3 | 0.35 | 0.003199444 | 0.002522061 | 0.003199444 | non-top | 0.3112417 |
| 13 | 3 | 0.75 | 0.09928156 | 0.01648459 | 0.09928156 | non-top | 0.3112417 |
| 13 | 4 | 0.35 | 0.0002650427 | 0.0001940047 | 0.0002650427 | non-top | 0.300057 |
| 13 | 4 | 0.75 | 0.008224508 | 0.001268045 | 0.008224508 | non-top | 0.300057 |

## Reading

The odd-prime top-packet law is not a new branch formula; it is a
realification of the same finite-field character-sum envelope.  The
new arithmetic feature is the factor of two: characteristic-two
characters are already real, while odd-prime characters split into
cosine/sine conjugate-pair coordinates in the real tangent space.
