# Mixed Rigidity Frontier

**Script:** `empirical/verify_mixed_rigidity_frontier.py`
**Status:** pair-color upper bounds match checked CRT generator lower bounds

This report tests the first `4p` and `4pq` rows suggested by the `N=12` rigidity pattern.  The evidence is coordinate-layer evidence only; no face-lattice or full orthogonal-stabilizer classification is claimed.

| N | factor form | scaled vertices | pair-color classes | gcd classes | coordinate stabilizer order | affine order | affine-rigid? | description |
|---:|---|---:|---:|---|---:|---:|---|---|
| 12 | 4*3 | 192 | 5 | `1,2,3,4,6` | 48 | 48 | yes | Aff(Z/4) x S_3 |
| 20 | 4*5 | 320 | 5 | `1,2,4,5,10` | 960 | 160 | no | Aff(Z/4) x S_5 |
| 28 | 4*7 | 448 | 5 | `1,2,4,7,14` | 40320 | 336 | no | Aff(Z/4) x S_7 |
| 60 | 4*3*5 | 61440 | 11 | `1,2,3,4,5,6,10,12,15,20,30` | 5760 | 960 | no | Aff(Z/4) x S_3 x S_5 |

## Interpretation

1. `N=12=4*3` is affine-rigid because the odd factor contributes `S_3`, and `S_3 = Aff(Z/3)`.
2. `N=20=4*5` and `N=28=4*7` are not affine-rigid.  The `4` side remains affine, but the odd prime side contributes the full symmetric group.
3. `N=60=4*3*5` is not affine-rigid.  The first `4pq` row has coordinate stabilizer `Aff(Z/4) x S_3 x S_5`, not `Aff(Z/60)`.
4. The refined conjecture should not be stated as `4p` or `4pq` rigidity.  The correct next target is to characterize when odd CRT factors contribute only their affine subgroup and when they enlarge to full symmetric factors.
