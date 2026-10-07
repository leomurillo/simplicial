# Three-Body Ternary Residual Audit

This is a controlled Paper 28 comprobation scaffold, not a claim about real gravitation.
The null is softened pairwise Newtonian mechanics.  The planted alternative adds
a nonadditive triplet potential `V3 = -alpha*m1*m2*m3/(s12*s23*s31)`.

## Configuration

- trials: `18`
- steps: `1600`
- dt: `0.002`
- sample stride: `3`
- masses: `[1.0, 1.25, 0.85]`
- gravity: `1.0`
- softening: `0.15`
- planted alpha: `0.035`
- pairwise radial powers: `[1, 2, 3, 4, 5, 6]`

## Newtonian Null

| model | rank | coefficient | train RMSE | test RMSE | train R2 vs zero | test R2 vs zero |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0 | 0 | 0 | 0 | 0 |
| ternary_one_coefficient | 1 | 0 | 0 | 0 | 0 | 0 |
| pairwise_only_radial_basis | 18 | 0 | 0 | 0 | 0 | 0 |
| shuffled_ternary_feature | 1 | 0 | 0 | 0 | 0 | 0 |
| random_same_rank_feature | 1 | 0 | 0 | 0 | 0 | 0 |

Finite-difference residual noise on test components: `0.00575456`.

## Planted Ternary Channel

| model | rank | coefficient | train RMSE | test RMSE | train R2 vs zero | test R2 vs zero |
|---|---:|---:|---:|---:|---:|---:|
| pairwise_null | 0 | 0 | 0.141442 | 0.159581 | 0 | 0 |
| ternary_one_coefficient | 1 | 0.035 | 2.328400e-16 | 2.471165e-16 | 1 | 1 |
| pairwise_only_radial_basis | 18 | 0 | 0.0545283 | 0.0806788 | 0.851377 | 0.744403 |
| shuffled_ternary_feature | 1 | 0.00129602 | 0.141345 | 0.159517 | 0.00137115 | 0.000798188 |
| random_same_rank_feature | 1 | 0.000379396 | 0.141442 | 0.159582 | 7.131381e-06 | -5.982740e-06 |

Finite-difference residual noise on test components: `0.00647064`.

## Divergence Audit

Representative trial true alpha `0.035`, recovered alpha `0.035`.

| model | final position RMS | max position RMS | final momentum RMS | max momentum RMS |
|---|---:|---:|---:|---:|
| pairwise_null | 0.0796819 | 0.193573 | 0.201304 | 0.786712 |
| recovered_ternary | 1.841081e-15 | 1.841081e-15 | 2.680539e-15 | 4.471333e-15 |
| pairwise_only_radial_basis | 0.14239 | 0.14239 | 0.120467 | 0.362831 |

## Invariant Checks

| run | max total momentum | max angular drift | max relative energy drift |
|---|---:|---:|---:|
| truth | 7.806573e-15 | 4.218847e-15 | 0.00159978 |
| pairwise_null | 6.843850e-15 | 6.661338e-15 | 0.00145395 |
| recovered_ternary | 8.188600e-15 | 5.995204e-15 | 0.00159978 |
| pairwise_only_radial_basis | 8.917793e-15 | 3.996803e-15 | n/a |

## Reading

The null run has exact residual RMS `0` and recovers alpha `0`, so the ternary feature does not hallucinate a channel when the dynamics are pairwise.
The planted run recovers alpha `0.035` against true alpha `0.035` with test R2 `1`.
The stronger pair-only radial basis reaches test R2 `0.744403`.  It can absorb some trajectory-specific structure, but it does not match the one-coefficient planted triplet channel across held-out initial conditions.
In trajectory replay, the recovered ternary model stays near the planted trajectory, while the pure pairwise null diverges.  This is the intended Paper 28 empirical lane: a controlled residual audit that distinguishes pairwise closure from a typed ternary overflow.

## Guardrail

This does not prove physical gravity is ternary.  It proves the audit can detect a known irreducible/nonadditive triplet channel, reject it under the Newtonian null, and price the divergence caused by forcing the triplet whole into pairwise shadows.
