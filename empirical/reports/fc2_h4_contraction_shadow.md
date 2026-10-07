# FC2 H4-Invisible Atom Contraction Shadow

This experiment starts from the exact input-side H4 Fisher-shadow image
and contracts it to H3.  It then asks which atom-boundary H4 cells that
were invisible at H4 become visible after the same H4-to-H3 support
projection.

This is a projection-shadow diagnostic only.  It does not claim support
closure, and it does not make `K_CH` an `Ext_CH` detector.

## Summary

| row | raw atoms | H4-visible | H4-invisible | H3-contraction visible from H4-invisible | remaining invisible | visible H3 orbits | timing |
|---|---:|---:|---:|---:|---:|---:|---:|
| `f4-u2` | 1569 | 72 | 1497 | 1470 | 27 | 5 | 0.117 |
| `f2-u5` | 19140 | 5424 | 13716 | 13618 | 98 | 12 | 5.986 |
| `f8-u2` | 158081 | 784 | 157297 | 157178 | 119 | 8 | 124.891 |
| `f16-field` | 225 | 0 | 225 | 0 | 225 | 0 | 0.083 |
| `f2-u4-control` | 1540 | 368 | 1172 | 1138 | 34 | 7 | 0.389 |

## f4-u2

- ring: `F_4[u]/(u^2)`
- H4-visible atoms: `72`
- H4-invisible atoms entering this refinement: `1497`
- H3-contraction visible atoms: `1470`
- remaining invisible atoms: `27`
- visible H3 orbits generated from K_CH H4 image: `5`

H4-invisible family refinement:

| H4 family | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `TTTT` | 9 | 6 | 3 | `6/9` |
| `WWWW` | 1488 | 1464 | 24 | `1464/1488` |

H4-invisible path refinement:

| carry path | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `u->u->u` | 9 | 6 | 3 | `6/9` |
| `u^2->u->u^2` | 912 | 900 | 12 | `900/912` |
| `u^2->u^2->u^2` | 576 | 564 | 12 | `564/576` |

## f2-u5

- ring: `F_2[u]/(u^5)`
- H4-visible atoms: `5424`
- H4-invisible atoms entering this refinement: `13716`
- H3-contraction visible atoms: `13618`
- remaining invisible atoms: `98`
- visible H3 orbits generated from K_CH H4 image: `12`

H4-invisible family refinement:

| H4 family | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `2222` | 4 | 2 | 2 | `2/4` |
| `3333` | 80 | 72 | 8 | `72/80` |
| `4444` | 1088 | 1064 | 24 | `1064/1088` |
| `5555` | 12544 | 12480 | 64 | `12480/12544` |

H4-invisible path refinement:

| carry path | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `u^2->u->u^2` | 4 | 2 | 2 | `2/4` |
| `u^3->u->u^3` | 48 | 44 | 4 | `44/48` |
| `u^3->u^2->u^3` | 32 | 28 | 4 | `28/32` |
| `u^4->u->u^4` | 448 | 440 | 8 | `440/448` |
| `u^4->u^2->u^4` | 384 | 376 | 8 | `376/384` |
| `u^4->u^3->u^4` | 256 | 248 | 8 | `248/256` |
| `u^5->u->u^5` | 3840 | 3824 | 16 | `3824/3840` |
| `u^5->u^2->u^5` | 3584 | 3568 | 16 | `3568/3584` |
| `u^5->u^3->u^5` | 3072 | 3056 | 16 | `3056/3072` |
| `u^5->u^4->u^5` | 2048 | 2032 | 16 | `2032/2048` |

## f8-u2

- ring: `F_8[u]/(u^2)`
- H4-visible atoms: `784`
- H4-invisible atoms entering this refinement: `157297`
- H3-contraction visible atoms: `157178`
- remaining invisible atoms: `119`
- visible H3 orbits generated from K_CH H4 image: `8`

H4-invisible family refinement:

| H4 family | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `1111` | 49 | 42 | 7 | `42/49` |
| `2222` | 157248 | 157136 | 112 | `157136/157248` |

H4-invisible path refinement:

| carry path | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `u->u->u` | 49 | 42 | 7 | `42/49` |
| `u^2->u->u^2` | 132160 | 132104 | 56 | `132104/132160` |
| `u^2->u^2->u^2` | 25088 | 25032 | 56 | `25032/25088` |

## f16-field

- ring: `F_16`
- H4-visible atoms: `0`
- H4-invisible atoms entering this refinement: `225`
- H3-contraction visible atoms: `0`
- remaining invisible atoms: `225`
- visible H3 orbits generated from K_CH H4 image: `0`

H4-invisible family refinement:

| H4 family | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `FFFF` | 225 | 0 | 225 | `0/225` |

H4-invisible path refinement:

| carry path | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `field->field->field` | 225 | 0 | 225 | `0/225` |

## f2-u4-control

- ring: `F_2[u]/(u^4)`
- H4-visible atoms: `368`
- H4-invisible atoms entering this refinement: `1172`
- H3-contraction visible atoms: `1138`
- remaining invisible atoms: `34`
- visible H3 orbits generated from K_CH H4 image: `7`

H4-invisible family refinement:

| H4 family | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `2222` | 4 | 2 | 2 | `2/4` |
| `3333` | 80 | 72 | 8 | `72/80` |
| `4444` | 1088 | 1064 | 24 | `1064/1088` |

H4-invisible path refinement:

| carry path | H4-invisible atoms | H3-contraction visible | remaining invisible | fraction |
|---|---:|---:|---:|---:|
| `u^2->u->u^2` | 4 | 2 | 2 | `2/4` |
| `u^3->u->u^3` | 48 | 44 | 4 | `44/48` |
| `u^3->u^2->u^3` | 32 | 28 | 4 | `28/32` |
| `u^4->u->u^4` | 448 | 440 | 8 | `440/448` |
| `u^4->u^2->u^4` | 384 | 376 | 8 | `376/384` |
| `u^4->u^3->u^4` | 256 | 248 | 8 | `248/256` |
