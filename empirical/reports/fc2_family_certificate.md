# FC2 Family Certificate

- theorem scope: All finite local conductor-filtered quotient-character adjacency rows satisfying the section-extension hypotheses; visible support is computed after quotienting by the Fisher-jet kernel.
- formal source: filtered section class [kappa] in the section-change complex
- formal shadows: `K_CH cubic Fisher commutator shadow`, `higher arity hyper-adjacency/Fisher-jet support shadows`
- all certified rows have full nonzero residual: `True`
- support projection can hide full carry: `True`

## First Mixed Row Shadow

- ring: `F_4[u]/(u^2)`
- commutator orbits lifted: `592 / 592`
- mixed H4 orbits hit: `7 / 7`
- pure H4 orbits hit: `0 / 11`

## Certified Local Rows

| row | ring | packets | H3 | H4 | raw atoms | raw pairs | pair orbits | full residual | support residual |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| f4-u2 | F_4[u]/(u^2) | u:3, u^2:12 | 210/5 | 3165/18 | 1569 | 369 | 20 | 1569 | n/a |
| f2-u5 | F_2[u]/(u^5) | u:1, u^2:2, u^3:4, u^4:8, u^5:16 | 930/12 | 28861/72 | 19140 | 2516 | 81 | 19140 | 0 |
| f8-u2 | F_8[u]/(u^2) | u:7, u^2:56 | 3906/8 | 246141/86 | 158081 | 7105 | 49 | 158081 | 0 |

## Reading

The family theorem is formal: the source of curvature-carry is the
filtered section class `[kappa]`, and visible curvature/carry supports
are its Fisher-jet images.  The table certifies nonzero full filtered
carry on the current finite local atlas.  Rows with support residual
`0` show why support closure alone is not the theorem.
