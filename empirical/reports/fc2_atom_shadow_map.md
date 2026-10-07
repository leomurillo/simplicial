# FC2 Coefficient-Level Atom Shadow Map

This report maps full filtered residual representatives to the visible
input-side H4 Fisher-shadow support.  It is an incidence classifier:
`visible_h4_incident` means the atom-boundary H4 orbit is in the
already certified H4 image of the `K_CH` commutator shadow.  It does
not make `K_CH` a standalone `Ext_CH` detector.

Because the current row atlas has `full_block_residual_equal_raw=true`,
the raw carry atoms are used here as coefficient-level representatives
of the full filtered residual.

## Summary

| row | full residual atoms | support residual | K_CH orbits | visible H4 orbits | atom-boundary visible | atom-boundary invisible | timing |
|---|---:|---:|---:|---:|---:|---:|---:|
| `f4-u2` | 1569 | 0 | 592 | 7 | 72 | 1497 | 0.075 |
| `f2-u5` | 19140 | 0 | 6656 | 43 | 5424 | 13716 | 4.26 |
| `f8-u2` | 158081 | 0 | 17944 | 30 | 784 | 157297 | 110.011 |
| `f16-field` | 225 | 0 | 0 | 0 | 0 | 225 | 0.049 |
| `f2-u4-control` | 1540 | 0 | 1148 | 17 | 368 | 1172 | 0.231 |

## f4-u2

- ring: `F_4[u]/(u^2)`
- full residual atoms: `1569`
- full residual equals raw cochain: `True`
- support projection residual: `0`
- K_CH commutator orbits: `592`
- input-side H4 orbits hit by K_CH: `7`
- atom-boundary visible/invisible: `72 / 1497`
- non-H4 or nonclosed atom boundaries: `0 / 0`

Path visibility:

| carry path | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `u->u->u` | 9 | 0 | 9 | `0/9` |
| `u->u->u^2` | 36 | 36 | 0 | `36/36` |
| `u^2->u->u` | 36 | 36 | 0 | `36/36` |
| `u^2->u->u^2` | 912 | 0 | 912 | `0/912` |
| `u^2->u^2->u^2` | 576 | 0 | 576 | `0/576` |

Atom-boundary H4 family visibility:

| H4 family | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `TTTT` | 9 | 0 | 9 | `0/9` |
| `TTWW` | 72 | 72 | 0 | `72/72` |
| `WWWW` | 1488 | 0 | 1488 | `0/1488` |

Visible H4 orbit atom counts:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 1 | TTWW | 48 | 56 | 1344 | `((w+1)u, (w+1)u, 1, 1)` |
| 3 | TTWW | 24 | 32 | 672 | `((w+1)u, (w+1)u, w+1, w+1)` |

Largest H4-invisible atom-boundary orbits under this channel:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 17 | WWWW | 576 | 0 | 0 | `(1, 1+(w+1)u, w+1, w+1+(w+1)u)` |
| 16 | WWWW | 288 | 0 | 0 | `(1, 1+(w+1)u, w, w+(w+1)u)` |
| 13 | WWWW | 192 | 0 | 0 | `(1, 1, w+(w+1)u, w+(w+1)u)` |
| 10 | WWWW | 96 | 0 | 0 | `(1, 1, 1+(w+1)u, 1+(w+1)u)` |
| 12 | WWWW | 96 | 0 | 0 | `(1, 1, w, w)` |
| 14 | WWWW | 96 | 0 | 0 | `(1, 1, w+1+(w+1)u, w+1+(w+1)u)` |
| 15 | WWWW | 72 | 0 | 0 | `(1, 1+(w+1)u, 1+u, 1+wu)` |
| 11 | WWWW | 48 | 0 | 0 | `(1, 1, 1+u, 1+u)` |
| 9 | WWWW | 24 | 0 | 0 | `(1, 1, 1, 1)` |
| 2 | TTTT | 6 | 0 | 0 | `((w+1)u, (w+1)u, u, u)` |
| 0 | TTTT | 3 | 0 | 0 | `((w+1)u, (w+1)u, (w+1)u, (w+1)u)` |

## f2-u5

- ring: `F_2[u]/(u^5)`
- full residual atoms: `19140`
- full residual equals raw cochain: `True`
- support projection residual: `0`
- K_CH commutator orbits: `6656`
- input-side H4 orbits hit by K_CH: `43`
- atom-boundary visible/invisible: `5424 / 13716`
- non-H4 or nonclosed atom boundaries: `0 / 0`

Path visibility:

| carry path | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `u^2->u->u^2` | 4 | 0 | 4 | `0/4` |
| `u^2->u->u^3` | 8 | 8 | 0 | `8/8` |
| `u^2->u->u^4` | 16 | 16 | 0 | `16/16` |
| `u^2->u->u^5` | 32 | 32 | 0 | `32/32` |
| `u^3->u->u^2` | 8 | 8 | 0 | `8/8` |
| `u^3->u->u^3` | 48 | 0 | 48 | `0/48` |
| `u^3->u->u^4` | 96 | 96 | 0 | `96/96` |
| `u^3->u->u^5` | 192 | 192 | 0 | `192/192` |
| `u^3->u^2->u^3` | 32 | 0 | 32 | `0/32` |
| `u^3->u^2->u^4` | 64 | 64 | 0 | `64/64` |
| `u^3->u^2->u^5` | 128 | 128 | 0 | `128/128` |
| `u^4->u->u^2` | 16 | 16 | 0 | `16/16` |
| `u^4->u->u^3` | 96 | 96 | 0 | `96/96` |
| `u^4->u->u^4` | 448 | 0 | 448 | `0/448` |
| `u^4->u->u^5` | 896 | 896 | 0 | `896/896` |
| `u^4->u^2->u^3` | 64 | 64 | 0 | `64/64` |
| `u^4->u^2->u^4` | 384 | 0 | 384 | `0/384` |
| `u^4->u^2->u^5` | 768 | 768 | 0 | `768/768` |
| `u^4->u^3->u^4` | 256 | 0 | 256 | `0/256` |
| `u^4->u^3->u^5` | 512 | 512 | 0 | `512/512` |
| `u^5->u->u^2` | 32 | 32 | 0 | `32/32` |
| `u^5->u->u^3` | 192 | 192 | 0 | `192/192` |
| `u^5->u->u^4` | 896 | 896 | 0 | `896/896` |
| `u^5->u->u^5` | 3840 | 0 | 3840 | `0/3840` |
| `u^5->u^2->u^3` | 128 | 128 | 0 | `128/128` |
| `u^5->u^2->u^4` | 768 | 768 | 0 | `768/768` |
| `u^5->u^2->u^5` | 3584 | 0 | 3584 | `0/3584` |
| `u^5->u^3->u^4` | 512 | 512 | 0 | `512/512` |
| `u^5->u^3->u^5` | 3072 | 0 | 3072 | `0/3072` |
| `u^5->u^4->u^5` | 2048 | 0 | 2048 | `0/2048` |

Atom-boundary H4 family visibility:

| H4 family | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `2222` | 4 | 0 | 4 | `0/4` |
| `2233` | 16 | 16 | 0 | `16/16` |
| `2244` | 32 | 32 | 0 | `32/32` |
| `2255` | 64 | 64 | 0 | `64/64` |
| `3333` | 80 | 0 | 80 | `0/80` |
| `3344` | 320 | 320 | 0 | `320/320` |
| `3355` | 640 | 640 | 0 | `640/640` |
| `4444` | 1088 | 0 | 1088 | `0/1088` |
| `4455` | 4352 | 4352 | 0 | `4352/4352` |
| `5555` | 12544 | 0 | 12544 | `0/12544` |

Visible H4 orbit atom counts:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 6 | 4455 | 768 | 120 | 15360 | `(1, 1, u, u)` |
| 7 | 3355 | 128 | 72 | 3840 | `(1, 1, u^2, u^2)` |
| 8 | 3355 | 64 | 48 | 1920 | `(1, 1, u^2+u^3, u^2+u^3)` |
| 9 | 3355 | 64 | 48 | 1920 | `(1, 1, u^2+u^3+u^4, u^2+u^3+u^4)` |
| 10 | 2255 | 64 | 72 | 3840 | `(1, 1, u^3, u^3)` |
| 23 | 4455 | 1024 | 240 | 30720 | `(1, 1+u^2, u, u+u^2)` |
| 27 | 4455 | 1024 | 240 | 30720 | `(1, 1+u^2+u^3, u, u+u^2+u^3)` |
| 31 | 4455 | 512 | 120 | 15360 | `(1, 1+u^3, u, u+u^3)` |
| 32 | 4455 | 512 | 120 | 15360 | `(1, 1+u^3, u+u^2, u+u^2+u^3)` |
| 33 | 3355 | 128 | 144 | 7680 | `(1, 1+u^3, u^2, u^2+u^3)` |
| 34 | 3355 | 128 | 144 | 7680 | `(1, 1+u^3, u^2+u^3+u^4, u^2+u^4)` |
| 36 | 4455 | 512 | 120 | 15360 | `(1, 1+u^4, u, u+u^4)` |
| 37 | 3355 | 64 | 72 | 3840 | `(1, 1+u^4, u^2, u^2+u^4)` |
| 38 | 3355 | 64 | 96 | 3840 | `(1, 1+u^4, u^2+u^3, u^2+u^3+u^4)` |
| 45 | 3344 | 128 | 72 | 3840 | `(u, u, u^2, u^2)` |
| 46 | 2244 | 16 | 36 | 960 | `(u, u, u^3, u^3)` |
| 47 | 2244 | 16 | 36 | 960 | `(u, u, u^3+u^4, u^3+u^4)` |
| 54 | 3344 | 64 | 72 | 3840 | `(u, u+u^3, u^2, u^2+u^3)` |
| 56 | 3344 | 64 | 72 | 3840 | `(u, u+u^3+u^4, u^2, u^2+u^3+u^4)` |
| 58 | 3344 | 64 | 72 | 3840 | `(u, u+u^4, u^2, u^2+u^4)` |
| 63 | 2233 | 16 | 48 | 960 | `(u^2, u^2, u^3, u^3)` |

Largest H4-invisible atom-boundary orbits under this channel:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 12 | 5555 | 4608 | 0 | 0 | `(1, 1+u, 1+u+u^2, 1+u^2)` |
| 1 | 5555 | 1280 | 0 | 0 | `(1, 1, 1+u, 1+u)` |
| 13 | 5555 | 1152 | 0 | 0 | `(1, 1+u, 1+u+u^3, 1+u^3)` |
| 14 | 5555 | 1152 | 0 | 0 | `(1, 1+u, 1+u+u^3+u^4, 1+u^3+u^4)` |
| 15 | 5555 | 1152 | 0 | 0 | `(1, 1+u, 1+u+u^4, 1+u^4)` |
| 21 | 5555 | 1152 | 0 | 0 | `(1, 1+u^2, 1+u^2+u^3, 1+u^3)` |
| 49 | 4444 | 384 | 0 | 0 | `(u, u+u^2, u+u^2+u^3, u+u^3)` |
| 2 | 5555 | 320 | 0 | 0 | `(1, 1, 1+u^2, 1+u^2)` |
| 3 | 5555 | 320 | 0 | 0 | `(1, 1, 1+u^2+u^3, 1+u^2+u^3)` |
| 4 | 5555 | 320 | 0 | 0 | `(1, 1, 1+u^3, 1+u^3)` |
| 22 | 5555 | 288 | 0 | 0 | `(1, 1+u^2, 1+u^2+u^4, 1+u^4)` |
| 26 | 5555 | 288 | 0 | 0 | `(1, 1+u^2+u^3, 1+u^2+u^3+u^4, 1+u^4)` |

## f8-u2

- ring: `F_8[u]/(u^2)`
- full residual atoms: `158081`
- full residual equals raw cochain: `True`
- support projection residual: `0`
- K_CH commutator orbits: `17944`
- input-side H4 orbits hit by K_CH: `30`
- atom-boundary visible/invisible: `784 / 157297`
- non-H4 or nonclosed atom boundaries: `0 / 0`

Path visibility:

| carry path | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `u->u->u` | 49 | 0 | 49 | `0/49` |
| `u->u->u^2` | 392 | 392 | 0 | `392/392` |
| `u^2->u->u` | 392 | 392 | 0 | `392/392` |
| `u^2->u->u^2` | 132160 | 0 | 132160 | `0/132160` |
| `u^2->u^2->u^2` | 25088 | 0 | 25088 | `0/25088` |

Atom-boundary H4 family visibility:

| H4 family | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `1111` | 49 | 0 | 49 | `0/49` |
| `1122` | 784 | 784 | 0 | `784/784` |
| `2222` | 157248 | 0 | 157248 | `0/157248` |

Visible H4 orbit atom counts:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 2 | 1122 | 336 | 248 | 41664 | `((1+b)*u, (1+b)*u, 1, 1)` |
| 3 | 1122 | 112 | 88 | 13888 | `((1+b)*u, (1+b)*u, 1+b, 1+b)` |
| 4 | 1122 | 336 | 248 | 41664 | `((1+b)*u, (1+b)*u, 1+b^2, 1+b^2)` |

Largest H4-invisible atom-boundary orbits under this channel:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 46 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b, 1+b+(1+b)*u)` |
| 48 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b+(1+b+b^2)*u, 1+b+b^2*u)` |
| 49 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b+b^2, 1+b+b^2+(1+b)*u)` |
| 50 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b+b^2+(1+b+b^2)*u, 1+b+b^2+b^2*u)` |
| 51 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b^2, 1+b^2+(1+b)*u)` |
| 52 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, 1+b^2+(1+b^2)*u, 1+b^2+(b+b^2)*u)` |
| 53 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, b, b+(1+b)*u)` |
| 54 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, b+(1+b+b^2)*u, b+b^2*u)` |
| 55 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, b^2, b^2+(1+b)*u)` |
| 56 | 2222 | 4032 | 0 | 0 | `(1, 1+(1+b)*u, b^2+(1+b^2)*u, b^2+(b+b^2)*u)` |
| 57 | 2222 | 4032 | 0 | 0 | `(1, 1+(b+b^2)*u, 1+b, 1+b+(b+b^2)*u)` |
| 59 | 2222 | 4032 | 0 | 0 | `(1, 1+(b+b^2)*u, 1+b+(1+b)*u, 1+b+(1+b^2)*u)` |

## f16-field

- ring: `F_16`
- full residual atoms: `225`
- full residual equals raw cochain: `True`
- support projection residual: `0`
- K_CH commutator orbits: `0`
- input-side H4 orbits hit by K_CH: `0`
- atom-boundary visible/invisible: `0 / 225`
- non-H4 or nonclosed atom boundaries: `0 / 0`

Path visibility:

| carry path | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `field->field->field` | 225 | 0 | 225 | `0/225` |

Atom-boundary H4 family visibility:

| H4 family | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `FFFF` | 225 | 0 | 225 | `0/225` |

Visible H4 orbit atom counts:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|

Largest H4-invisible atom-boundary orbits under this channel:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 1 | FFFF | 120 | 0 | 0 | `(1, 1, 1+a, 1+a)` |
| 3 | FFFF | 60 | 0 | 0 | `(1, 1, 1+a+a^2+a^3, 1+a+a^2+a^3)` |
| 2 | FFFF | 30 | 0 | 0 | `(1, 1, 1+a+a^2, 1+a+a^2)` |
| 0 | FFFF | 15 | 0 | 0 | `(1, 1, 1, 1)` |

## f2-u4-control

- ring: `F_2[u]/(u^4)`
- full residual atoms: `1540`
- full residual equals raw cochain: `True`
- support projection residual: `0`
- K_CH commutator orbits: `1148`
- input-side H4 orbits hit by K_CH: `17`
- atom-boundary visible/invisible: `368 / 1172`
- non-H4 or nonclosed atom boundaries: `0 / 0`

Path visibility:

| carry path | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `u^2->u->u^2` | 4 | 0 | 4 | `0/4` |
| `u^2->u->u^3` | 8 | 8 | 0 | `8/8` |
| `u^2->u->u^4` | 16 | 16 | 0 | `16/16` |
| `u^3->u->u^2` | 8 | 8 | 0 | `8/8` |
| `u^3->u->u^3` | 48 | 0 | 48 | `0/48` |
| `u^3->u->u^4` | 96 | 96 | 0 | `96/96` |
| `u^3->u^2->u^3` | 32 | 0 | 32 | `0/32` |
| `u^3->u^2->u^4` | 64 | 64 | 0 | `64/64` |
| `u^4->u->u^2` | 16 | 16 | 0 | `16/16` |
| `u^4->u->u^3` | 96 | 96 | 0 | `96/96` |
| `u^4->u->u^4` | 448 | 0 | 448 | `0/448` |
| `u^4->u^2->u^3` | 64 | 64 | 0 | `64/64` |
| `u^4->u^2->u^4` | 384 | 0 | 384 | `0/384` |
| `u^4->u^3->u^4` | 256 | 0 | 256 | `0/256` |

Atom-boundary H4 family visibility:

| H4 family | total atoms | visible H4 incident | H4 invisible | visible fraction |
|---|---:|---:|---:|---:|
| `2222` | 4 | 0 | 4 | `0/4` |
| `2233` | 16 | 16 | 0 | `16/16` |
| `2244` | 32 | 32 | 0 | `32/32` |
| `3333` | 80 | 0 | 80 | `0/80` |
| `3344` | 320 | 320 | 0 | `320/320` |
| `4444` | 1088 | 0 | 1088 | `0/1088` |

Visible H4 orbit atom counts:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 5 | 3344 | 128 | 56 | 1792 | `(1, 1, u, u)` |
| 6 | 2244 | 16 | 32 | 448 | `(1, 1, u^2, u^2)` |
| 7 | 2244 | 16 | 32 | 448 | `(1, 1, u^2+u^3, u^2+u^3)` |
| 14 | 3344 | 64 | 56 | 1792 | `(1, 1+u^2, u, u+u^2)` |
| 16 | 3344 | 64 | 56 | 1792 | `(1, 1+u^2+u^3, u, u+u^2+u^3)` |
| 18 | 3344 | 64 | 56 | 1792 | `(1, 1+u^3, u, u+u^3)` |
| 23 | 2233 | 16 | 32 | 448 | `(u, u, u^2, u^2)` |

Largest H4-invisible atom-boundary orbits under this channel:

| H4 orbit | family | atoms | K_CH H2 orbits | K_CH entry hits | representative |
|---:|---|---:|---:|---:|---|
| 9 | 4444 | 384 | 0 | 0 | `(1, 1+u, 1+u+u^2, 1+u^2)` |
| 1 | 4444 | 224 | 0 | 0 | `(1, 1, 1+u, 1+u)` |
| 10 | 4444 | 192 | 0 | 0 | `(1, 1+u, 1+u+u^3, 1+u^3)` |
| 13 | 4444 | 96 | 0 | 0 | `(1, 1+u^2, 1+u^2+u^3, 1+u^3)` |
| 2 | 4444 | 56 | 0 | 0 | `(1, 1, 1+u^2, 1+u^2)` |
| 3 | 4444 | 56 | 0 | 0 | `(1, 1, 1+u^2+u^3, 1+u^2+u^3)` |
| 4 | 4444 | 56 | 0 | 0 | `(1, 1, 1+u^3, 1+u^3)` |
| 21 | 3333 | 32 | 0 | 0 | `(u, u, u+u^2, u+u^2)` |
| 0 | 4444 | 24 | 0 | 0 | `(1, 1, 1, 1)` |
| 25 | 3333 | 24 | 0 | 0 | `(u, u+u^2, u+u^2+u^3, u+u^3)` |
| 22 | 3333 | 16 | 0 | 0 | `(u, u, u+u^3, u+u^3)` |
| 20 | 3333 | 8 | 0 | 0 | `(u, u, u, u)` |

## FC1/FC3 Implications

For FC1, the natural row macrovariables now include atom-boundary H4
family incidence, visible H4 orbit atom mass, and the split between
support-erased atoms incident to the Fisher-shadow image and atoms
invisible to the tested Fisher-jet channel.

For FC3, the cost split is explicit: full filtered residual mass can be
support-erased while still having a nonzero visible H4-shadow incidence
component.  The remaining H4-invisible atoms are the next target for
richer Fisher-jet or coefficient-shadow observables.
