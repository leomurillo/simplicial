# Arity-4 Audit for F4[u]/(u^2)

This checks the third epistle's arity-4 preregistration before the
curvature-lift computation is attempted.

## Count Convention

- all nontrivial closed ordered 4-tuples: 3165
- all-distinct nontrivial closed ordered 4-tuples: 2520
- proposed count in epistle: 2730

The stated hyper-adjacency convention only excludes the trivial label, so
the operative count is 3165.  The number 2730 is the count of ordered
distinct choices for the first three legs before imposing that the fourth
leg is nonzero; after imposing closure and nontriviality, the distinct
count is 2520.

## Conductor Stratification

Ordered words:

- TTTT: 21
- TTWW: 108
- TWTW: 108
- TWWT: 108
- TWWW: 288
- WTTW: 108
- WTWT: 108
- WTWW: 288
- WWTT: 108
- WWTW: 288
- WWWT: 288
- WWWW: 1344

Unordered families:

- TTTT: 21
- TTWW: 648
- TWWW: 1152
- WWWW: 1344

In particular, TTWW and TWWW families are nonzero.  The proposed parity
claim that these vanish is false under the stated closure rule.

## Orbit Counts

- Gamma_R-only orbits: 140 with sizes {3: 1, 6: 3, 12: 10, 24: 126}
- Gamma_R x C_4 orbits: 47 with sizes {3: 1, 6: 1, 12: 3, 24: 6, 48: 10, 96: 26}
- Gamma_R x S_4 orbits: 18 with sizes {3: 1, 12: 1, 18: 1, 36: 1, 72: 5, 144: 3, 288: 4, 576: 2}

By family under Gamma_R x C_4:

- TTTT: 3 orbits, sizes [3, 6, 12]
- TTWW: 9 orbits, sizes [24, 48, 48, 48, 96, 96, 96, 96, 96]
- TWWW: 12 orbits, sizes [96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96]
- WWWW: 23 orbits, sizes [12, 12, 24, 24, 24, 24, 24, 48, 48, 48, 48, 48, 48, 48, 96, 96, 96, 96, 96, 96, 96, 96, 96]

By family under Gamma_R x S_4:

- TTTT: 2 orbits, sizes [3, 18]
- TTWW: 4 orbits, sizes [72, 144, 144, 288]
- TWWW: 3 orbits, sizes [288, 288, 576]
- WWWW: 9 orbits, sizes [12, 36, 72, 72, 72, 72, 144, 288, 576]

The cyclic and full symmetric quotients differ at arity 4: this is the
first place where quotienting too aggressively can erase structure.
The revised fourth-epistle family prediction is still not correct:
measured S_4 family orbit counts are TTTT=2, TTWW=4, TWWW=3, WWWW=9,
not TTTT=1, TTWW=3, TWWW=5, WWWW=9.

## Controls

- pure tame F_4: 21 closed arity-4 cells, normalizer actions 6, orbit sizes [3, 18]
- pure wild F_2[u]/(u^2): 21 closed arity-4 cells, unit actions 2, orbit sizes [1, 2, 6, 12], conductor words {'TTTT': 1, 'TTWW': 2, 'TWTW': 2, 'TWWT': 2, 'WTTW': 2, 'WTWT': 2, 'WWTT': 2, 'WWWW': 8}

Unlike arity 3, the pure controls do not collapse to one orbit at arity 4.
The fourth epistle corrected these pure-control counts, but the stronger
claim that C_4-to-S_4 collapse occurs only on curvature-carrying lifts is
false at the orbit-skeleton level: TTTT and WWWW families also collapse.

## Status

RED for both the original and revised arity-4 preregistrations as written.
The selector may still be right, but the measurable orbit-family
predictions need correction before the curvature-lift test can be trusted.
This RED status applies only to the earlier preregistered arity-4 predictions.
The measured skeleton used by Paper 11 is the corrected \(3165\)-cell,
\(18\)-orbit S4 atlas above.
