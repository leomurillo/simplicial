# FC2 Visible Fisher-Jet Kernel

This report starts the visible Fisher-jet kernel phase of FC2
classification.  The filtered source theorem is not being re-proved:
`[kappa_R]` is the source class, while `K_CH` and H4 are tested
Fisher-jet shadows of that class.

The raw-support projection is kept separate from `K_CH`.  A support
residual of `0` means erasure in that quotient, not filtered closure.

## Extraction Limits

- max exact conductor-mixed mode pairs: `100`
- max exact candidate tangent products: `50000`
- sampled mode pairs per gated packet pair: `0`
- forced exact rows: `['f2-u5', 'f8-u2']`

## Row Summary

| row | ring | packets | mixed mode pairs | candidate products | status | K_CH entries | K_CH orbits | H4 lift | residual accounting |
|---|---|---|---:|---:|---|---:|---:|---|---|
| f4-u2 | F_4[u]/(u^2) | {'u': 3, 'u^2': 12} | 36 | 7560 | exact | 14112 | 592 | 592/592 H2; mixed 7/7; pure 0/11 | full 1569; support 0; atom map unresolved |
| f2-u5 | F_2[u]/(u^5) | {'u': 1, 'u^2': 2, 'u^3': 4, 'u^4': 8, 'u^5': 16} | 310 | 288300 | exact | 558000 | 6656 | 6656/6656 H2; mixed 43/43; pure 0/29 | full 19140; support 0; atom map unresolved |
| f8-u2 | F_8[u]/(u^2) | {'u': 7, 'u^2': 56} | 392 | 1531152 | exact | 3013696 | 17944 | 17944/17944 H2; mixed 30/30; pure 0/56 | full 158081; support 0; atom map unresolved |
| f16-field | F_16 | {'field': 15} | 0 | 0 | empty | 0 | 0 | empty mixed channel | full 225; support 0; atom map unresolved |
| f2-u4-control | F_2[u]/(u^4) | {'u': 1, 'u^2': 2, 'u^3': 4, 'u^4': 8} | 70 | 14700 | exact | 27440 | 1148 | 1148/1148 H2; mixed 17/17; pure 0/15 | full 1540; support 0; atom map unresolved |

## Execution Notes

- `f2-u5`: 2026-05-14 pre-streaming forced exact run timed out after 900 seconds.  After the streaming orbit canonicalizer was added, `--force-exact f2-u5` completed exactly; the combined report records the current timing.
- `f8-u2`: 2026-05-14 pre-sparse forced exact runs timed out after 900 seconds.  After the sparse commutator formula and support-set orbiting path were added, `--force-exact f8-u2` completed exactly; the combined report records the current timing.

## Exact Shadows

### f4-u2

- commutator entries: `14112`
- commutator orbits: `592`
- orbit sizes: `{'12': 8, '24': 584}`
- coefficients: `{'-1': 7056, '1': 7056}`
- lifted input-side H2 orbits: `592 / 592`
- H4 mixed/pure hit: `7 / 7` mixed, `0 / 11` pure
- H2 to H4 multiplicity: `{'1': 592}`
- timings: `{'witness_generation': 0.005, 'commutator_orbits': 0.051, 'h4_orbits': 0.066}`

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 3 | TTWW | 72 | 32 | 672 | `((w+1)u, (w+1)u, w+1, w+1)` |
| 1 | TTWW | 144 | 56 | 1344 | `((w+1)u, (w+1)u, 1, 1)` |
| 4 | TTWW | 144 | 56 | 1344 | `((w+1)u, 1, 1+u, wu)` |
| 5 | TTWW | 288 | 112 | 2688 | `((w+1)u, 1, 1+wu, u)` |
| 6 | TWWW | 288 | 84 | 2016 | `((w+1)u, 1, w, w+1+(w+1)u)` |
| 8 | TWWW | 288 | 84 | 2016 | `((w+1)u, 1, w+1+u, w+wu)` |
| 7 | TWWW | 576 | 168 | 4032 | `((w+1)u, 1, w+(w+1)u, w+1)` |

Packet-pair breakdown:

| packet pair | mode pairs | entries | orbits | H4 hit | family hits |
|---|---:|---:|---:|---:|---|
| u->u^2 | 36 | 14112 | 592 | 7 | `{'TTWW': 4, 'TWWW': 3}` |

### f2-u5

- commutator entries: `558000`
- commutator orbits: `6656`
- orbit sizes: `{'128': 3732, '16': 248, '2': 8, '32': 2292, '4': 8, '8': 368}`
- coefficients: `{'-1': 279000, '1': 279000}`
- lifted input-side H2 orbits: `6656 / 6656`
- H4 mixed/pure hit: `43 / 43` mixed, `0 / 29` pure
- H2 to H4 multiplicity: `{'1': 6656}`
- timings: `{'witness_generation': 0.399, 'commutator_orbits': 11.833, 'h4_orbits': 4.427}`

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 70 | 1122 | 12 | 24 | 240 | `(u^3, u^3, u^4, u^4)` |
| 64 | 1133 | 24 | 32 | 480 | `(u^2, u^2, u^4, u^4)` |
| 48 | 1144 | 48 | 36 | 960 | `(u, u, u^4, u^4)` |
| 11 | 1155 | 96 | 48 | 1920 | `(1, 1, u^4, u^4)` |
| 66 | 1233 | 96 | 120 | 2400 | `(u^2, u^2+u^3, u^3+u^4, u^4)` |
| 55 | 1244 | 96 | 90 | 2400 | `(u, u+u^3, u^3+u^4, u^4)` |
| 57 | 1244 | 96 | 90 | 2400 | `(u, u+u^3+u^4, u^3, u^4)` |
| 35 | 1255 | 384 | 180 | 9600 | `(1, 1+u^3, u^3+u^4, u^4)` |
| 52 | 1344 | 384 | 180 | 9600 | `(u, u+u^2, u^2+u^4, u^4)` |
| 25 | 1355 | 384 | 180 | 9600 | `(1, 1+u^2, u^2+u^4, u^4)` |
| 29 | 1355 | 384 | 240 | 9600 | `(1, 1+u^2+u^3, u^2+u^3+u^4, u^4)` |
| 20 | 1455 | 1536 | 300 | 38400 | `(1, 1+u, u+u^4, u^4)` |
| 63 | 2233 | 48 | 48 | 960 | `(u^2, u^2, u^3, u^3)` |
| 67 | 2233 | 48 | 48 | 960 | `(u^2, u^2+u^4, u^3, u^3+u^4)` |
| 46 | 2244 | 48 | 36 | 960 | `(u, u, u^3, u^3)` |
| 47 | 2244 | 48 | 36 | 960 | `(u, u, u^3+u^4, u^3+u^4)` |
| 59 | 2244 | 96 | 72 | 1920 | `(u, u+u^4, u^3, u^3+u^4)` |
| 10 | 2255 | 192 | 72 | 3840 | `(1, 1, u^3, u^3)` |
| 39 | 2255 | 192 | 72 | 3840 | `(1, 1+u^4, u^3, u^3+u^4)` |
| 51 | 2344 | 768 | 360 | 19200 | `(u, u+u^2, u^2+u^3, u^3)` |
| 24 | 2355 | 768 | 360 | 19200 | `(1, 1+u^2, u^2+u^3, u^3)` |
| 28 | 2355 | 768 | 360 | 19200 | `(1, 1+u^2+u^3, u^2, u^3)` |
| 18 | 2455 | 1536 | 300 | 38400 | `(1, 1+u, u+u^3, u^3)` |
| 19 | 2455 | 1536 | 300 | 38400 | `(1, 1+u, u+u^3+u^4, u^3+u^4)` |
| 45 | 3344 | 192 | 72 | 3840 | `(u, u, u^2, u^2)` |
| 54 | 3344 | 192 | 72 | 3840 | `(u, u+u^3, u^2, u^2+u^3)` |
| 56 | 3344 | 192 | 72 | 3840 | `(u, u+u^3+u^4, u^2, u^2+u^3+u^4)` |
| 58 | 3344 | 192 | 72 | 3840 | `(u, u+u^4, u^2, u^2+u^4)` |
| 8 | 3355 | 96 | 48 | 1920 | `(1, 1, u^2+u^3, u^2+u^3)` |
| 9 | 3355 | 96 | 48 | 1920 | `(1, 1, u^2+u^3+u^4, u^2+u^3+u^4)` |
| 7 | 3355 | 192 | 72 | 3840 | `(1, 1, u^2, u^2)` |
| 37 | 3355 | 192 | 72 | 3840 | `(1, 1+u^4, u^2, u^2+u^4)` |
| 38 | 3355 | 192 | 96 | 3840 | `(1, 1+u^4, u^2+u^3, u^2+u^3+u^4)` |
| 33 | 3355 | 384 | 144 | 7680 | `(1, 1+u^3, u^2, u^2+u^3)` |
| 34 | 3355 | 384 | 144 | 7680 | `(1, 1+u^3, u^2+u^3+u^4, u^2+u^4)` |
| 16 | 3455 | 3072 | 600 | 76800 | `(1, 1+u, u+u^2, u^2)` |
| 17 | 3455 | 3072 | 600 | 76800 | `(1, 1+u, u+u^2+u^3, u^2+u^3)` |
| 6 | 4455 | 768 | 120 | 15360 | `(1, 1, u, u)` |
| 31 | 4455 | 768 | 120 | 15360 | `(1, 1+u^3, u, u+u^3)` |
| 32 | 4455 | 768 | 120 | 15360 | `(1, 1+u^3, u+u^2, u+u^2+u^3)` |
| 36 | 4455 | 768 | 120 | 15360 | `(1, 1+u^4, u, u+u^4)` |
| 23 | 4455 | 1536 | 240 | 30720 | `(1, 1+u^2, u, u+u^2)` |
| 27 | 4455 | 1536 | 240 | 30720 | `(1, 1+u^2+u^3, u, u+u^2+u^3)` |

Packet-pair breakdown:

| packet pair | mode pairs | entries | orbits | H4 hit | family hits |
|---|---:|---:|---:|---:|---|
| u->u^2 | 2 | 3600 | 120 | 5 | `{'1122': 1, '1233': 1, '1244': 2, '1255': 1}` |
| u->u^3 | 4 | 7200 | 200 | 5 | `{'1133': 1, '1233': 1, '1344': 1, '1355': 2}` |
| u->u^4 | 8 | 14400 | 240 | 5 | `{'1144': 1, '1244': 2, '1344': 1, '1455': 1}` |
| u->u^5 | 16 | 28800 | 408 | 5 | `{'1155': 1, '1255': 1, '1355': 2, '1455': 1}` |
| u^2->u^3 | 8 | 14400 | 360 | 6 | `{'1233': 1, '2233': 2, '2344': 1, '2355': 2}` |
| u^2->u^4 | 16 | 28800 | 480 | 8 | `{'1244': 2, '2244': 3, '2344': 1, '2455': 2}` |
| u^2->u^5 | 32 | 57600 | 744 | 7 | `{'1255': 1, '2255': 2, '2355': 2, '2455': 2}` |
| u^3->u^4 | 32 | 57600 | 744 | 8 | `{'1344': 1, '2344': 1, '3344': 4, '3455': 2}` |
| u^3->u^5 | 64 | 115200 | 1560 | 13 | `{'1355': 2, '2355': 2, '3355': 7, '3455': 2}` |
| u^4->u^5 | 128 | 230400 | 1800 | 11 | `{'1455': 1, '2455': 2, '3455': 2, '4455': 6}` |

### f8-u2

- commutator entries: `3013696`
- commutator orbits: `17944`
- orbit sizes: `{'168': 17936, '56': 8}`
- coefficients: `{'-1': 1506848, '1': 1506848}`
- lifted input-side H2 orbits: `17944 / 17944`
- H4 mixed/pure hit: `30 / 30` mixed, `0 / 56` pure
- H2 to H4 multiplicity: `{'1': 17944}`
- timings: `{'witness_generation': 2.813, 'commutator_orbits': 45.971, 'h4_orbits': 123.489}`

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 3 | 1122 | 336 | 88 | 13888 | `((1+b)*u, (1+b)*u, 1+b, 1+b)` |
| 2 | 1122 | 1008 | 248 | 41664 | `((1+b)*u, (1+b)*u, 1, 1)` |
| 4 | 1122 | 1008 | 248 | 41664 | `((1+b)*u, (1+b)*u, 1+b^2, 1+b^2)` |
| 6 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, 1, 1+b^2*u)` |
| 7 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, 1+b, 1+b+b^2*u)` |
| 8 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, 1+b+b^2, 1+b+b^2+b^2*u)` |
| 9 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, 1+b^2, 1+b^2+b^2*u)` |
| 10 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, b, b+b^2*u)` |
| 11 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, b+b^2, b+b^2+b^2*u)` |
| 12 | 1122 | 2016 | 496 | 83328 | `((1+b)*u, (1+b+b^2)*u, b^2, b^2+b^2*u)` |
| 22 | 1222 | 1344 | 248 | 41664 | `((1+b)*u, 1, 1+b+b^2+b^2*u, b+b^2+(1+b+b^2)*u)` |
| 23 | 1222 | 1344 | 248 | 41664 | `((1+b)*u, 1, 1+b+b^2+u, b+b^2+b*u)` |
| 13 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b, b+(1+b)*u)` |
| 14 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+(1+b)*u, b)` |
| 15 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+(1+b+b^2)*u, b+b^2*u)` |
| 16 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+(1+b^2)*u, b+(b+b^2)*u)` |
| 17 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+(b+b^2)*u, b+(1+b^2)*u)` |
| 18 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+b*u, b+u)` |
| 19 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+b^2, b+b^2+(1+b)*u)` |
| 20 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+b^2*u, b+(1+b+b^2)*u)` |
| 21 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+b^2+(1+b+b^2)*u, b+b^2+b^2*u)` |
| 24 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b+u, b+b*u)` |
| 25 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2, b^2+(1+b)*u)` |
| 26 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+(1+b)*u, b^2)` |
| 27 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+(1+b+b^2)*u, b^2+b^2*u)` |
| 28 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+(1+b^2)*u, b^2+(b+b^2)*u)` |
| 29 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+(b+b^2)*u, b^2+(1+b^2)*u)` |
| 30 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+b*u, b^2+u)` |
| 31 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+b^2*u, b^2+(1+b+b^2)*u)` |
| 32 | 1222 | 4032 | 744 | 124992 | `((1+b)*u, 1, 1+b^2+u, b^2+b*u)` |

Packet-pair breakdown:

| packet pair | mode pairs | entries | orbits | H4 hit | family hits |
|---|---:|---:|---:|---:|---|
| u->u^2 | 392 | 3013696 | 17944 | 30 | `{'1122': 10, '1222': 20}` |

### f2-u4-control

- commutator entries: `27440`
- commutator orbits: `1148`
- orbit sizes: `{'2': 8, '32': 764, '4': 8, '8': 368}`
- coefficients: `{'-1': 13720, '1': 13720}`
- lifted input-side H2 orbits: `1148 / 1148`
- H4 mixed/pure hit: `17 / 17` mixed, `0 / 15` pure
- H2 to H4 multiplicity: `{'1': 1148}`
- timings: `{'witness_generation': 0.016, 'commutator_orbits': 0.147, 'h4_orbits': 0.27}`

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 30 | 1122 | 12 | 20 | 112 | `(u^2, u^2, u^3, u^3)` |
| 24 | 1133 | 24 | 20 | 224 | `(u, u, u^3, u^3)` |
| 8 | 1144 | 48 | 32 | 448 | `(1, 1, u^3, u^3)` |
| 26 | 1233 | 96 | 80 | 1120 | `(u, u+u^2, u^2+u^3, u^3)` |
| 15 | 1244 | 96 | 80 | 1120 | `(1, 1+u^2, u^2+u^3, u^3)` |
| 17 | 1244 | 96 | 80 | 1120 | `(1, 1+u^2+u^3, u^2, u^3)` |
| 12 | 1344 | 384 | 140 | 4480 | `(1, 1+u, u+u^3, u^3)` |
| 23 | 2233 | 48 | 32 | 448 | `(u, u, u^2, u^2)` |
| 27 | 2233 | 48 | 32 | 448 | `(u, u+u^3, u^2, u^2+u^3)` |
| 6 | 2244 | 48 | 32 | 448 | `(1, 1, u^2, u^2)` |
| 7 | 2244 | 48 | 32 | 448 | `(1, 1, u^2+u^3, u^2+u^3)` |
| 19 | 2244 | 96 | 64 | 896 | `(1, 1+u^3, u^2, u^2+u^3)` |
| 11 | 2344 | 768 | 280 | 8960 | `(1, 1+u, u+u^2, u^2)` |
| 5 | 3344 | 192 | 56 | 1792 | `(1, 1, u, u)` |
| 14 | 3344 | 192 | 56 | 1792 | `(1, 1+u^2, u, u+u^2)` |
| 16 | 3344 | 192 | 56 | 1792 | `(1, 1+u^2+u^3, u, u+u^2+u^3)` |
| 18 | 3344 | 192 | 56 | 1792 | `(1, 1+u^3, u, u+u^3)` |

Packet-pair breakdown:

| packet pair | mode pairs | entries | orbits | H4 hit | family hits |
|---|---:|---:|---:|---:|---|
| u->u^2 | 2 | 784 | 68 | 4 | `{'1122': 1, '1233': 1, '1244': 2}` |
| u->u^3 | 4 | 1568 | 80 | 3 | `{'1133': 1, '1233': 1, '1344': 1}` |
| u->u^4 | 8 | 3136 | 152 | 4 | `{'1144': 1, '1244': 2, '1344': 1}` |
| u^2->u^3 | 8 | 3136 | 152 | 4 | `{'1233': 1, '2233': 2, '2344': 1}` |
| u^2->u^4 | 16 | 6272 | 304 | 6 | `{'1244': 2, '2244': 3, '2344': 1}` |
| u^3->u^4 | 32 | 12544 | 392 | 6 | `{'1344': 1, '2344': 1, '3344': 4}` |

## Gated Profiles

No rows were gated under this run.

## Atom-Level Accounting

This report deliberately does not count `K_CH` as an `Ext_CH` atom
detector.  The exact rows prove that a row has a visible Fisher-jet
shadow and identify its commutator/H4 support.  They do not yet assign
individual full filtered residual atoms to visible or invisible K_CH
buckets.  That coefficient-level atom map is the next refinement.

## FC1/FC3 Handoff

For FC1, the new natural invariants are mixed mode-pair counts,
commutator orbit sizes, input-side H4 image families, and gated
candidate-product profiles.  For FC3, the split is now explicit:
full filtered residual cost, raw-support-erased cost, and the cost of
paying for a richer visible Fisher channel are separate quantities.
