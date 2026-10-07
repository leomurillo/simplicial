# Arity-4 Curvature-Lift Support Audit for F4[u]/(u^2)

This is the support-level test for Theorem 9.3 of Paper 11.  The
analytic arity-4 curvature coefficient R^(4) is defined there as the
centroid-normalized, S_4-symmetrized four-linear coefficient projected
onto the antisymmetric commutator component.  This script audits its
claimed support via the canonical input-side boundary of the already
computed arity-2 commutator witnesses.

## Measured arity-4 skeleton

- total closed nontrivial 4-cells: 3165
- Gamma_R x S_4 orbits: 18
- family orbit counts: TTTT: 2, TTWW: 4, TWWW: 3, WWWW: 9

## Input-side lift

For a commutator witness
`(tau, omega, alpha, beta, input, output)`, the input-side lift uses
the two closed projections
`(tau, omega, alpha, input)` and `(tau, omega, beta, input)`.

- arity-2 commutator orbits: 592
- lifted arity-2 commutator orbits: 592
- H2 orbit to H4 orbit multiplicity: 1 H4 orbit: 592
- H4 mixed orbits hit: 7 / 7
- H4 pure orbits hit: 0 / 11
- lifted entry hits by family: TTWW: 6048, TWWW: 8064

Thus every one of the 592 commutator orbits has exactly one
input-side arity-4 orbit image, and the images are exactly the seven
mixed TTWW/TWWW orbits.  No TTTT or WWWW orbit is hit by this lift.

## Mixed-orbit image table

| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |
|---:|---|---:|---:|---:|---|
| 2 | TTWW | 72 | 32 | 672 | `(u, u, 1, 1)` |
| 3 | TTWW | 144 | 56 | 1344 | `(u, u, w, w)` |
| 5 | TTWW | 144 | 56 | 1344 | `(u, wu, w+1, w+1+(w+1)u)` |
| 4 | TTWW | 288 | 112 | 2688 | `(u, wu, 1, 1+(w+1)u)` |
| 7 | TWWW | 288 | 84 | 2016 | `(u, 1, w+wu, w+1+(w+1)u)` |
| 8 | TWWW | 288 | 84 | 2016 | `(u, 1, w+(w+1)u, w+1+wu)` |
| 6 | TWWW | 576 | 168 | 4032 | `(u, 1, w, w+1+u)` |

## Projection due diligence

| projection | lifted H2 orbits | closed hits | family hits | H2 orbit -> H4 orbit count |
|---|---:|---:|---|---|
| input alpha leg | 296/592 | 7056 | TTWW: 3024, TWWW: 4032 | 1 ids: 296 |
| input beta leg | 296/592 | 7056 | TTWW: 3024, TWWW: 4032 | 1 ids: 296 |
| input-side union | 592/592 | 14112 | TTWW: 6048, TWWW: 8064 | 1 ids: 592 |
| operator pair | 44/592 | 1008 | TTWW: 432, TWWW: 576 | 1 ids: 44 |
| output-side union | 44/592 | 1008 | TTWW: 432, TWWW: 576 | 1 ids: 44 |
| all literal four-label projections | 592/592 | 23904 | TTTT: 360, TTWW: 10368, TWWW: 11520, WWWW: 1656 | 1 ids: 504, 2 ids: 48, 3 ids: 40 |

The single input projections split the 592 into two 296-orbit halves.
Their union is exact.  The operator-pair and output-side projections
under-detect the commutator support, while allowing all literal four-label
projections is too loose because it also routes through pure TTTT and
WWWW cells.

## Status

GREEN for Theorem 9.3 at support level: under the input-side boundary
convention, the 592 lift exactly onto the seven mixed arity-4 orbits
and avoid the eleven pure orbits.

Coefficient values are supplied by `h4_R4_covariant_full_mixed_lift_table.md`.
Open beyond this support theorem: the full Ext_CH^(4) class and the operadic
composition law.
