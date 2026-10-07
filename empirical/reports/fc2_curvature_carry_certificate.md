# FC2 Curvature-Carry Certificate

- ring: `F_4[u]/(u^2)`
- cohomological object: filtered quotient-character adjacency extension class [kappa] in the section-change/Hochschild 2-cohomology model
- not the object: the signed all-pair boundary on closed nontrivial hypercells; that boundary fails d^2=0 over Z

## Binary Filtered Carry

- raw atoms: `1569`
- raw carry pairs: `369`
- atom orbits: `71`
- pair orbits: `20`
- full-block coboundary rank: `3204` / `3204`
- C2 dimension: `76320`
- residual support: `1569`
- raw is coboundary: `False`
- non-coboundary over Q certified: `True`

## Arity-4 Fisher Curvature Shadow

- closed nontrivial 4-cells: `3165`
- Gamma_R x S4 orbits: `18`
- arity-2 commutator orbits: `592`
- lifted commutator orbits: `592`
- mixed H4 orbits hit: `7 / 7`
- pure H4 orbits hit: `0 / 11`
- entry hits by family: `{'TTWW': 6048, 'TWWW': 8064}`

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 2 | TTWW | 72 | 32 | 672 | `(u, u, 1, 1)` |
| 3 | TTWW | 144 | 56 | 1344 | `(u, u, w, w)` |
| 5 | TTWW | 144 | 56 | 1344 | `(u, wu, w+1, w+1+(w+1)u)` |
| 4 | TTWW | 288 | 112 | 2688 | `(u, wu, 1, 1+(w+1)u)` |
| 7 | TWWW | 288 | 84 | 2016 | `(u, 1, w+wu, w+1+(w+1)u)` |
| 8 | TWWW | 288 | 84 | 2016 | `(u, 1, w+(w+1)u, w+1+wu)` |
| 6 | TWWW | 576 | 168 | 4032 | `(u, 1, w, w+1+u)` |

## Why This Is Not Hypercell Cohomology

The closed nontrivial all-pair boundary fails `d^2=0` over `Z` on a
tiny control row:

- witness ring: `(Z/2)^2`
- witness cell: `[1, 2, 1, 2]`
- `d_3 d_4(cell)` over `Z`: `{'(3, 3)': 4, '(2, 2)': -2, '(1, 1)': 2}`
- `d^2 = 0` over `Z`: `False`
- witness vanishes mod 2: `True`

So FC2 is solved by using the filtered adjacency extension class as
the cohomological source.  The hyper-adjacency tower remains the
Fisher-jet support shadow of that source.

## Status

Solved for the first mixed local row: the binary Ext_CH class is the cohomological source, K_CH is its cubic Fisher shadow, and the arity-4 curvature support is its input-side Fisher-jet lift.
