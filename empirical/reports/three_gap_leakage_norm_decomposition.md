# Three-Gap Leakage Norm Decomposition

This report resolves the post-convolution leakage-norm question at the
finite linear-algebra level.  A leakage Gram form is three-gap safe
exactly when its off-diagonal part in the output-character basis
vanishes.  Otherwise it splits canonically into a diagonal safe part
plus a priced non-diagonal correction.

## By Compression / Leakage Model

| mode | rows | safe | max offdiag op | max relative offdiag | max correction rank | max compressed dim |
|---|---:|---:|---:|---:|---:|---:|
| conductor_sum | 5 | 0/5 | 47 | 0.9791667 | 196 | 11 |
| conductor_weight_diagonal | 5 | 5/5 | 0 | 0 | 0 | 196 |
| mobius_total | 5 | 0/5 | 195 | 0.994898 | 196 | 1 |
| mobius_weight_diagonal | 5 | 5/5 | 0 | 0 | 0 | 196 |
| zeta_identity | 5 | 5/5 | 0 | 0 | 0 | 196 |
| crt_face_restriction | 18 | 18/18 | 0 | 0 | 0 | 196 |

## First Unsafe Examples

| row | mode | labels | compressed dim | offdiag op | relative offdiag | correction rank |
|---:|---|---:|---:|---:|---:|---:|
| 6 | conductor_sum | 2 | 1 | 1 | 0.5 | 2 |
| 6 | mobius_total | 2 | 1 | 1 | 0.5 | 2 |
| 10 | conductor_sum | 4 | 1 | 3 | 0.75 | 4 |
| 10 | mobius_total | 4 | 1 | 3 | 0.75 | 4 |
| 15 | conductor_sum | 8 | 1 | 7 | 0.875 | 8 |
| 15 | mobius_total | 8 | 1 | 7 | 0.875 | 8 |
| 30 | conductor_sum | 22 | 4 | 7 | 0.875 | 22 |
| 30 | mobius_total | 22 | 1 | 21 | 0.9545455 | 22 |
| 210 | conductor_sum | 196 | 11 | 47 | 0.9791667 | 196 |
| 210 | mobius_total | 196 | 1 | 195 | 0.994898 | 196 |

## Reading

Identity, diagonal Mobius weights, diagonal conductor-depth weights, and
CRT face restrictions are zeta-diagonal.  They preserve the three-gap
grammar after the convolutional current layer.  Conductor-sum and
Mobius-total compressions are unsafe because their Gram matrices contain
cross-terms between distinct output characters.

Thus the leakage norm/current compression is solved as a dichotomy:
prove the Paper 22 leakage form is translation-equivariant, hence
zeta-diagonal, or split it into its canonical diagonal Reynolds part
plus the explicit off-diagonal correction priced by the operator norm
recorded here.
