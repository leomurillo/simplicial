# Pre-Heaven Audit

This is the due-diligence packet before escalating the arity-3 result.

## 1. Cyclic vs symmetric arity-3 quotient

- Gamma_R-only orbits: 11 with sizes [6, 12, 12, 12, 24, 24, 24, 24, 24, 24, 24]
- Gamma_R x C_3 orbits: 5 with sizes [6, 24, 36, 72, 72]
- Gamma_R x S_3 orbits: 5 with sizes [6, 24, 36, 72, 72]

On this row, quotienting by C_3 already gives the same five orbits as
quotienting by S_3.  Thus the arity-3 S_3 table did not erase a cyclic
distinction.  This should not be assumed at arity 4.

## 2. Arity-3 contraction profiles

| family | ordered size | representative | pair signatures after deleting one leg |
|---|---:|---|---|
| TTT | 6 | `((w+1)u, u, wu)` | 18 x `[T; T]` |
| TWW | 36 | `((w+1)u, w+1, w+1+(w+1)u)` | 72 x `[T(nu=1); W(rho=1,nu=0)]`<br>36 x `[W(rho=1,nu=0); W(rho=1,nu=1)]` |
| TWW | 72 | `((w+1)u, 1, 1+(w+1)u)` | 144 x `[T(nu=w); W(rho=1,nu=0)]`<br>72 x `[W(rho=1,nu=0); W(rho=1,nu=w)]` |
| WWW | 24 | `(1, w, w+1)` | 72 x `[W(rho=1,nu=0); W(rho=w,nu=0)]` |
| WWW | 72 | `(1, w+(w+1)u, w+1+(w+1)u)` | 72 x `[W(rho=1,nu=0); W(rho=w,nu=1)]`<br>144 x `[W(rho=1,nu=0); W(rho=w,nu=w)]` |

Every contraction lands in the same rho/nu pair-signature language used
at arity 2.  The new arity-3 information is the three-leg closure law,
not a new local coordinate.

## 3. Curvature selector audit

- full arity-2 defect orbits: 4438
- commutator-supported orbits: 592
- swap-symmetric orbits: 14
- swap-asymmetric orbits: 4424
- swap-asymmetric but Ext-only orbits: 3832
- commutator orbits inside swap-symmetric stratum: 0

Swap-asymmetry is necessary for curvature but not sufficient.  The coarse
candidate invariants still underfit:

- coarse buckets: 62
- largest coarse bucket: 1466 orbits
- coefficient-pure buckets: 27 / 62
- curvature-support-pure buckets: 38 / 62

Escalation should ask for the intrinsic Hayes-Carlitz condition selecting
the 592 curvature orbits, not merely for confirmation that they exist.

## 4. Control rows

- pure tame F_4: 6 closed arity-3 cells, normalizer actions 6, orbit sizes [6]
- pure wild F_2[u]/(u^2): 6 closed arity-3 cells, unit actions 2, orbit sizes [6], conductor words {'TWW': 2, 'WTW': 2, 'WWT': 2}

Both control rows collapse to one arity-3 orbit.  The five-orbit split in
F_4[u]/(u^2) is therefore genuinely mixed: it needs both nontrivial
residue-field multiplicative structure and a nilpotent tail.

## Escalation draft

We verified the arity-3 atlas and audited the obvious failure modes.
Cyclic quotienting does not refine the five S_3 orbits at arity 3; all
contractions land in the arity-2 rho/nu pair-signature language; pure
tame and pure wild controls each collapse to one orbit.  The unresolved
point is the arity-2 curvature selector: only 592 of 4424 swap-asymmetric
full-defect orbits carry commutator curvature.  What intrinsic
Hayes-Carlitz condition selects exactly those 592, and what arity-4
test should be pre-registered so cyclic/modular structure is not erased?
