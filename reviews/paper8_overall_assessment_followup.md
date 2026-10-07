# Paper 8 Overall Assessment Follow-Up

**Scope:** `8.parity_dual_simplices.md`

**Source:** User-supplied overall assessment, May 2026.

---

## Assessment Capture

The review is broadly positive.  It identifies Theorem 6.2, the convex-hull decomposition

```text
conv(X_N) ~= (Delta_{m-1} direct-sum Delta_{m-1}) x I,
```

as the current highlight.  It also approves the stabilizer theorem and the even/odd dichotomy.

The remaining critique is mostly about positioning and forward momentum:

1. The term "Janus" is too internal to the companion quadray-rotor story for a general mathematical paper.
2. The frame-theory thread should not end at "not an ETF"; the compound is still a structured unit-norm tight frame.
3. The most important future direction is the full cyclotomic reflection group, beyond the single `Phi_2` block.

The user clarified that "Janus" is rooted in Andy's quadray rotor work and can be evicted from this paper in favor of the best intrinsic naming.

---

## Implemented Changes

### Naming

The paper now uses intrinsic language:

- title changed to `Parity-Dual Simplices and Spectral Compounds`;
- abstract no longer says "stella-octangula/Janus phenomenon";
- keywords now use `parity reflection` and `spectral compounds`;
- the local Janus paragraph was replaced by a short historical note;
- the conclusion no longer uses a "sharpened Janus picture" block.

The formal language of the paper is now:

```text
parity-dual simplex
parity reflection
parity-dual compound
spectral compound
```

### Frame Theory

Section 3 now clarifies that `V_N union W_N` is not a single ETF for `N>=6`, but after unit normalization it is a unit-norm tight frame with frame bound `2N/(N-1)`.

### Full Cyclotomic Reflection Group

Added an open-problem section:

```text
Open Problems: Full Cyclotomic Reflection Compounds
```

It defines block-sign involutions

```text
rho_d = I - 2P_d
```

for every cyclotomic summand `H_N^[d]`, observes that the block-sign group is

```text
B_N ~= (C_2)^(tau(N)-1),
```

and states three open problems:

1. classify the orbit compound under `B_N`;
2. refine block signs to Fourier-plane flips and Galois plane permutations;
3. compare the refined complexified action with finite unitary reflection groups, without prematurely identifying it with a Shephard-Todd group.

### References

Added:

- Shephard and Todd, "Finite Unitary Reflection Groups" (1954);
- Lehrer and Taylor, *Unitary Reflection Groups* (2009).

---

## Remaining Optional Polish

1. Consider renaming `X_N` to `\mathcal X_N` in a LaTeX pass to reduce notation overlap with Coxeter-type labels.
2. Add one paragraph in the introduction explaining why "spectral compound" is the paper's umbrella term.
3. Add a small table comparing:
   - parity-dual compound;
   - full block-sign spectral compound;
   - Fourier-plane refined compound.

