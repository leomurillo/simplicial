# Mixed-Composite Stabilizer Verifier

**Script:** `empirical/verify_mixed_composite_stabilizers.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** exact pair-color upper bounds match checked vertex-set witnesses

The mixed composites do not share one stabilizer pattern.  The coordinate-pair colors remember different quotient schemes depending on how the divisor lattice combines prime-power layers.

| N | pair-color classes | checked witnesses | coordinate stabilizer order | group description |
|---:|---:|---:|---:|---|
| 6 | 2 | 5 | 72 | S_3 wr S_2; parity-fiber collapse |
| 10 | 2 | 9 | 28800 | S_5 wr S_2; parity-fiber collapse |
| 12 | 5 | 4 | 48 | Aff(Z/12); divisor-lattice rigidity |
| 15 | 3 | 6 | 720 | S_3 x S_5 on CRT coordinates |
| 18 | 4 | 14 | 559872 | S_3^6 semidirect Aff(Z/6); three-fold blow-up of Z/6 |
| 20 | 5 | 6 | 960 | Aff(Z/4) x S_5 on CRT coordinates |
| 24 | 7 | 768 | 768 | order-768 automorphism group of the full gcd-distance scheme |

## Consequences

1. The even semiprimes `N=6,10` collapse to the parity-fiber wreath products `S_3 wr S_2` and `S_5 wr S_2`.
2. The odd squarefree case `N=15` separates cleanly by CRT coordinates and has stabilizer `S_3 x S_5`.
3. The mixed prime-power case `N=18` is a blow-up of the divisor scheme on `Z/6`, with internal `S_3` fibers over each residue class modulo `6`.
4. The case `N=20` keeps an affine `Z/4` factor but allows a full `S_5` action on the coprime CRT coordinate.
5. The case `N=12` is the first rigid collapse in this range: its coordinate stabilizer is only `Aff(Z/12)`.
6. The case `N=24` has seven pair-color classes, one for each nonzero gcd class, and all 768 pair-color automorphisms preserve the spectral vertex set.
