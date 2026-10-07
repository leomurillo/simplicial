# N=12 Multi-Block Fourier Refinement

**Script:** `empirical/analyze_phi12_multiblock_refinement.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** all checks passed

The nonzero Fourier labels split into cyclotomic blocks as follows.

| block | labels | refinement factor | factor order | reflections |
|---|---|---|---:|---:|
| Phi_2 | `{6}` | `C2` | 2 | 1 |
| Phi_3 | `(4, 8)` | `G(3,3,2)` | 6 | 3 |
| Phi_4 | `(3, 9)` | `G(4,4,2)` | 8 | 4 |
| Phi_6 | `(2, 10)` | `G(6,6,2)` | 12 | 6 |
| Phi_12 | `(1, 11)` | `G(12,12,2)` | 24 | 12 |
| Phi_12 | `(5, 7)` | `G(12,12,2)` | 24 | 12 |

| group | order | reflections | reflection subgroup | reflection generated? |
|---|---:|---:|---:|---|
| arithmetic normalizer <C12, Gal> | 48 | 0 | 1 | no |
| blockwise reflection product | 663552 | 38 | 663552 | yes |
| product plus Phi_12 pair exchange | 1327104 | 38 | 663552 | no |

## Consequences

1. The arithmetic normalizer `<C12, Gal>` has order `48` and contains no complex reflections on the eleven-dimensional complexified zero-sum space.
2. The reflection-generated Fourier-plane refinement is the independent product `C2 x G(3,3,2) x G(4,4,2) x G(6,6,2) x G(12,12,2)^2`, of order `663552`.
3. The product has `38` codimension-one reflections: one from the Phi_2 line and `3+4+6+12+12` from the five conjugate-pair factors.
4. The only extra Galois normalizer action not already contained in the product exchanges the two Phi_12 pair factors, doubling the order to `1327104`.
5. That Phi_12 pair exchange has codimension at least two on the exchanged four-dimensional subspace, so it adds no reflections.  The normalizer extension is not reflection-generated.
6. Thus the N=12 Fourier-plane refinement decomposes as the product predicted by the cyclotomic monomial normalizer hypothesis, with a within-Phi_12 normalizer extension.  The coordinate-level divisor rigidity at N=12 does not force cross-block coupling in this reflection-refinement model.
