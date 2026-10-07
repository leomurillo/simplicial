# Paper 8 Round 2: Few-Angle Tight Frame Pass

**Scope:** `8.parity_dual_simplices.md`, Section 8.

**Goal:** Promote the full cyclotomic block-sign compound from an orbit census to a positive frame-theoretic object.

## Converged Claim

Let

```text
B_N = <rho_d : d | N, d > 1>
```

and let `M_N` be the number of distinct simplex images in the `B_N`-orbit of `V_N`.
From Round 1,

```text
M_N = 2^(tau(N)-1)  for odd N,
M_N = 2^(tau(N)-2)  for even N.
```

After unit normalization, the full spectral compound `X_N^spec` is a unit-norm tight frame of `N M_N` vectors in `H_N`, with frame bound

```text
A_N = N M_N / (N - 1).
```

The projective non-antipodal angle set is controlled by the Ramanujan formula

```text
abs((1/(N-1)) * sum_{d|N, d>1} epsilon_d c_d(k)),
```

with duplicate simplex images quotiented by the kernel `K_N = B_N cap Stab(V_N)` and the absolute value `1` removed.

## Important Caution

The compound is centrally symmetric because the all-block sign flip is `-I_H`.  Therefore its ordinary coherence is always `1`.  The useful statistic is the non-antipodal/projective coherence.

## Deferred Claims

No association-scheme, spherical-design, or fusion-frame structure is claimed in this pass.  Those patterns may exist for special families of `N`, but they need a separate proof and should remain a Round 3 or optional extension.

## Census Update

`empirical/census_cyclotomic_block_signs.py` now reports:

- distinct simplex count,
- vertex count,
- exact frame bound,
- number of projective angle values,
- ordinary coherence,
- non-antipodal/projective coherence.

It also verifies the exact frame-operator identity

```text
sum_{x in Xhat} x x^T = (N M_N / (N - 1)) P_H
```

for each tested `N`.
