# N0 Three-Front Probe

This is an audit for `N0-DeBrangesExhaustionAndWeilDomination-Draft1.md`.
It is evidence for the shape of the proof targets, not a proof of RH.

## Part A - zero-side finite Hermite-Biehler sanity model

M= 4: sampled min HB margin for P_M+iP_M' = 0.0039786374
M= 8: sampled min HB margin for P_M+iP_M' = 0.0050824925
M=16: sampled min HB margin for P_M+iP_M' = 0.0060905032

This uses true zeros, so it is a model of the desired finite HB exhaustion, not a proof.

## Part B - true E_B sampled margin and phase velocity

sampled min HB margin for E_B=Xi+iXi' = 0.0092416512

| x | phi'(x) |
|---:|---:|
| 0.0 | 0.04620998623 |
| 7.0 | 0.05519792982 |
| 14.1347251417 | 1.0 |
| 17.5 | 0.1693822848 |
| 21.0220396388 | 1.0 |
| 25.01085758 | 0.9999999998 |

## Part C - additive divisor current vs quadratic Bures curvature

| zero | y | Im m_B(gamma+iy) | y Im m_B | FS curvature limit |
|---:|---:|---:|---:|---:|
| gamma_1=14.1347251417 | 0.05 | 20.00338407 | 1.000169203 | 64.198255 |
| gamma_1=14.1347251417 | 0.01 | 100.0006768 | 1.000006768 | 64.198255 |
| gamma_2=21.0220396388 | 0.05 | 20.0069436 | 1.00034718 | 1848.5822 |
| gamma_2=21.0220396388 | 0.01 | 100.0013888 | 1.000013888 | 1848.5822 |

The additive log geometry has the 1/y Herglotz pole; the quadratic FS/Bures curvature is finite.

## Part D - small Weil matrix marginality

lambda_min(Weil floor - prime) = -1.016232e-05
lambda_min(archimedean floor + pole) = -1.059285e+00
lambda_max(prime erosion block) = 5.038332e+00

The small matrix is only a coarse truncation, but it shows the intended anatomy: floor, erosion, marginality.
