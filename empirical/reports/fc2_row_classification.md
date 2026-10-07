# FC2 Row Classification

This is the first row-level classifier after the FC2 source theorem.
It treats `[kappa_R]` as the solved filtered section class and classifies
which finite rows are nonzero, what the raw-support projection erases,
and which Fisher-jet shadows are already explicitly extracted.

## Classification Problem

- nonzero criterion: A measured row is classified nonzero when the full-block section-change reducer has residual_support > 0.
- kernel question: For a chosen Fisher/support projection J, which part of the full filtered residual is erased by ker J?
- visible support question: Record support-projection visibility for every row, and record K_CH/higher-arity shadows only where the exact Fisher-jet lift has been extracted.

The support projection below is not being identified with `K_CH`.
It is a reproducible support-level quotient.  The `K_CH`/arity-4
shadow is separately imported where it has an exact certificate.

## Row Table

| row | ring | role | raw atoms | raw pairs | pair orbits | full residual | support residual | erased by support | H3 | H4 | K_CH status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| f4-u2 | F_4[u]/(u^2) | certified mixed row | 1569 | 369 | 20 | 1569 | 0 | 1569 | 210/5 | 3165/18 | 592 comm orbits; H4 mixed 7/7 |
| f2-u5 | F_2[u]/(u^5) | certified atlas row | 19140 | 2516 | 81 | 19140 | 0 | 19140 | 930/12 | 28861/72 | not extracted in this first classifier; the row is classified at filtered and raw-support projection level |
| f8-u2 | F_8[u]/(u^2) | certified atlas row | 158081 | 7105 | 49 | 158081 | 0 | 158081 | 3906/8 | 246141/86 | not extracted in this first classifier; the row is classified at filtered and raw-support projection level |
| f16-field | F_16 | computable control | 225 | 225 | 5 | 225 | 0 | 225 | 210/2 | 3165/7 | zero conductor-mixed mode pairs; K_CH mixed-conductor shadow is empty |
| f2-u4-control | F_2[u]/(u^4) | computable control | 1540 | 404 | 33 | 1540 | 0 | 1540 | 210/7 | 3165/32 | not extracted in this first classifier; use as pure wild control |

## Support-Kernel Reading

- `f4-u2`: nonzero full filtered class erased by raw-support projection (erasure ratio `1.000`).
- `f2-u5`: nonzero full filtered class erased by raw-support projection (erasure ratio `1.000`).
- `f8-u2`: nonzero full filtered class erased by raw-support projection (erasure ratio `1.000`).
- `f16-field`: nonzero full filtered class erased by raw-support projection (erasure ratio `1.000`).
- `f2-u4-control`: nonzero full filtered class erased by raw-support projection (erasure ratio `1.000`).

## Orbit Data

| row | atom orbits | atom orbit sizes | pair orbit sizes | H3 families | H4 families |
|---|---:|---|---|---|---|
| f4-u2 | 71 | {'3': 1, '6': 1, '12': 8, '24': 61} | {'3': 1, '6': 1, '12': 6, '24': 12} | {'TTT': 1, 'TWW': 2, 'WWW': 2} | {'TTTT': 2, 'TTWW': 4, 'TWWW': 3, 'WWWW': 9} |
| f2-u5 | n/a | n/a | {'2': 2, '4': 4, '8': 20, '16': 24, '32': 21, '128': 10} | {'122': 1, '133': 1, '144': 1, '155': 1, '233': 1, '244': 2, '255': 1, '344': 1, '355': 2, '455': 1} | {'1111': 1, '1122': 1, '1133': 1, '1144': 1, '1155': 1, '1233': 1, '1244': 2, '1255': 1, '1344': 1, '1355': 2, '1455': 1, '2222': 2, '2233': 2, '2244': 3, '2255': 2, '2344': 1, '2355': 2, '2455': 2, '3333': 4, '3344': 4, '3355': 7, '3455': 2, '4444': 8, '4455': 6, '5555': 14} |
| f8-u2 | n/a | n/a | {'7': 1, '21': 2, '56': 6, '168': 40} | {'111': 1, '122': 3, '222': 4} | {'1111': 3, '1122': 10, '1222': 20, '2222': 53} |
| f16-field | 5 | {15: 1, 30: 1, 60: 3} | {15: 1, 30: 1, 60: 3} | {'FFF': 2} | {'FFFF': 7} |
| f2-u4-control | 92 | {2: 2, 4: 6, 8: 49, 32: 35} | {2: 2, 4: 4, 8: 20, 32: 7} | {'122': 1, '133': 1, '144': 1, '233': 1, '244': 2, '344': 1} | {'1111': 1, '1122': 1, '1133': 1, '1144': 1, '1233': 1, '1244': 2, '1344': 1, '2222': 2, '2233': 2, '2244': 3, '2344': 1, '3333': 4, '3344': 4, '4444': 8} |

## Fisher-Jet Shadow Status

### f4-u2

- support projection residual: `0`
- K_CH commutator orbits: `592`
- lifted arity-4 commutator orbits: `592`
- H4 mixed/pure hit: `7 / 7` mixed, `0 / 11` pure
- representative Fisher probe: `mixed_order2_support=14` for modes `(w+1)u`, `1`

### f2-u5

- support projection residual: `0`
- K_CH status: not extracted in this first classifier; the row is classified at filtered and raw-support projection level
- representative Fisher probe: `mixed_order2_support=30` for modes `u^4`, `u^3`

### f8-u2

- support projection residual: `0`
- K_CH status: not extracted in this first classifier; the row is classified at filtered and raw-support projection level
- representative Fisher probe: `mixed_order2_support=62` for modes `(1+b)*u`, `1`

### f16-field

- support projection residual: `0`
- K_CH status: zero conductor-mixed mode pairs; K_CH mixed-conductor shadow is empty
- representative Fisher probe: `mixed_order2_support=14` for modes `1`, `1`

### f2-u4-control

- support projection residual: `0`
- K_CH status: not extracted in this first classifier; use as pure wild control
- representative Fisher probe: `mixed_order2_support=14` for modes `u^3`, `u^2`

## FC1/FC3 Handoff

FC1 should now treat conductor packet sizes, carry path distributions,
normalizer pair-orbits, and H3/H4 family orbits as candidate natural
macrovariables.  The table shows why support closure alone is too coarse:
every classified nonzero row can be erased by the raw-support projection.

FC3 should score the full filtered residual separately from visible
support residuals.  The projection kernel is not a nuisance term; it
is the list of residual mass that a chosen information-investment
functional cannot see unless it pays for a richer K_CH or higher-arity
Fisher-jet channel.
