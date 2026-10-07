# Prime-Power Stabilizer Verifier

**Script:** `empirical/verify_prime_power_stabilizers.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** exact pair-color and generator checks passed

For odd prime powers `N=p^r`, the coordinate-pair colors recover the full p-adic congruence tree.  For powers of two `N=2^r`, `r>=3`, the top two binary layers fuse into four-point fibers; the colors recover congruences only through modulo `2^(r-2)`, and each fiber carries a full `S_4` action.

| N | p | r | pair-color levels | checked generators | predicted coordinate stabilizer order | group description |
|---:|---:|---:|---:|---:|---:|---|
| 8 | 2 | 3 | 2 | 7 | 1152 | binary congruence tree with S_4 fibers at level 1 |
| 9 | 3 | 2 | 2 | 8 | 1296 | Aut of depth-2 p-adic congruence tree; iterated S_3 wreath product |
| 16 | 2 | 4 | 3 | 15 | 2654208 | binary congruence tree with S_4 fibers at level 2 |
| 25 | 5 | 2 | 2 | 24 | 2985984000000 | Aut of depth-2 p-adic congruence tree; iterated S_5 wreath product |
| 27 | 3 | 3 | 3 | 26 | 13060694016 | Aut of depth-3 p-adic congruence tree; iterated S_3 wreath product |
| 32 | 2 | 5 | 4 | 31 | 14089640214528 | binary congruence tree with S_4 fibers at level 3 |

## Consequences

1. The `N=8` and `N=9` stabilizer rows in the polytope census are the first two prime-power cases of a general p-adic pattern.
2. Odd prime powers have the full rooted p-ary tree automorphism group, equivalently an iterated wreath product with `r` copies of `S_p`.
3. Powers of two are slightly exceptional: the half-turn kernel fuses the last two binary levels, leaving full `S_4` fibers over the residue classes modulo `2^(r-2)`.
4. Mixed composites such as `N=12` are not explained by the prime-power theorem; their stabilizers remain part of the squarefree/mixed-divisor problem.
