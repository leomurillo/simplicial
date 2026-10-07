# Parity-Dual Stabilizer Notes

**Scope:** `8.parity_dual_simplices.md`

**Purpose:** Consolidate the Round 1 and Round 2 stabilizer work into a single review note.

---

## Symmetry Layers

For the parity-dual compound

```text
X_N = V_N union W_N,
```

there are three symmetry layers that should not be conflated.

| Layer | Meaning | Result |
|---|---|---|
| Coordinate stabilizer | Ambient coordinate permutations in `S_N` preserving `X_N` | For `N=2m>=6`, `S_m wr S_2`, order `2(m!)^2`. |
| Gram/orthogonal stabilizer | Vertex permutations preserving all pairwise inner products; equivalently orthogonal maps of `H_N` preserving `X_N` | For `N=2m>=6`, `C_2 x (S_m wr S_2)`, order `4(m!)^2`. |
| Central inversion | Whether `-I_{H_N}` preserves `X_N` | Yes for `N=4`; no for `N>=6`. |

---

## Round 1: Coordinate And Gram Stabilizers

The first stabilizer pass separated coordinate symmetries from abstract Gram automorphisms.

For `N=2m>=6`, the four off-diagonal inner-product types are distinct:

```text
same simplex, different indices:      -1/N
matched cross pair v_i--w_i:          (N-3)/N
same-parity cross, nonmatched:        -3/N
opposite-parity cross:                 1/N
```

The matched cross value identifies the pairs `{v_i,w_i}`.  The same-simplex value forces any inside-pair flip to be global rather than independent by pair.  The remaining index permutation must preserve the parity equivalence relation or swap the two parity classes.

Therefore:

```text
G_coord(X_N) ~= (S_m x S_m) semidirect C_2 ~= S_m wr S_2
|G_coord(X_N)| = 2(m!)^2

Aut_Gram(X_N) ~= C_2 x ((S_m x S_m) semidirect C_2)
|Aut_Gram(X_N)| = 4(m!)^2
```

The extra `C_2` in the Gram group is the global simplex swap `v_i <-> w_i`, induced by `rho_2`.

Manuscript result:

- Theorem 6.1: Parity-Class Stabilizer.
- Corollary 6.4: Compound Gram Profile.

---

## Round 2: Orthogonal Stabilizer, Coxeter Language, And `N=4`

### Ambient Orthogonal Stabilizer

For `N=2m>=6`, the natural action map

```text
O(X_N) -> Aut_Gram(X_N)
```

is an isomorphism.

Reason:

- Injectivity: `X_N` spans `H_N`, since `V_N` already spans `H_N`.
- Surjectivity: any Gram-preserving permutation of the spanning set extends to a well-defined orthogonal map.  If a linear relation maps to something nonzero, its squared norm would still be zero because the Gram matrix is preserved.

This is folded into Theorem 6.1.

### Type-A Coxeter / Young Subgroup Language

Inside

```text
W(A_{N-1}) ~= S_N,
```

with `N=2m`, the even/odd split gives a Young subgroup

```text
S_E x S_O ~= S_m x S_m.
```

After reordering coordinates, this is a standard parabolic subgroup of type

```text
A_{m-1} x A_{m-1}.
```

The full coordinate stabilizer is the setwise stabilizer of the unordered bipartition `{E,O}`, hence the normalizer of this equal-block Young subgroup:

```text
N_{S_N}(S_E x S_O) ~= S_m wr S_2 ~= (S_m x S_m) semidirect C_2.
```

It is also the centralizer in `S_N` of the rank-one parity projector `P_2=ss^T/N`, equivalently of the Householder reflection `rho_2=I-2P_2`.

Important caution: this is not the centralizer of a fixed-point-free involution in `S_{2m}`, whose order is `2^m m!`.

### The `N=4` Boundary Case

The `N=4` case deserves its own theorem because it is not the first instance of the higher-`N` wreath pattern.  It is the exceptional stella-octangula/cube case:

```text
X_4 = V_4 union W_4 = V_4 union (-V_4).
```

After unit normalization, `X_4` is the vertex set of a cube in `H_4 ~= R^3`.  Equivalently, it is the compound of two complementary tetrahedra known as the stella octangula.  Its polar polytope is the three-dimensional cross-polytope.

Manuscript result:

- Theorem 4.1: The Stella-Octangula Boundary Case.

---

## Citation Decision

The paper now cites Bjorner and Brenti's *Combinatorics of Coxeter Groups* for the type-A Coxeter, parabolic/Young subgroup, and wreath-product normalizer language.  This is enough for the structural vocabulary without burdening the paper with additional representation-theory references.

---

## Remaining Optional Polish

1. If the manuscript becomes journal-facing, add a short sentence connecting the equal-block Young normalizer to the stabilizer of a composition `(m,m)` in the type-A Coxeter complex.
2. If the symmetry table grows too long in the main text, move it to an appendix and leave only Theorem 6.1 plus the `N=4` theorem in the body.
3. Consider adding a small figure for `N=4` showing the cube/stella-octangula/cross-polytope polarity.

