# Empirical Verification: Parity-Dual Simplices

**Script:** `empirical/verify_parity_dual_simplices.py`
**Companion note:** `8.parity_dual_simplices.md`
**Status:** all checks passed

This report records the verifier output for the parity-dual simplex theorem.  The exact checks cover:

1. existence of the parity vector \(s=(1,-1,\ldots,1,-1)\) for even \(N\);
2. \(C_Ns=-s\), identifying \(H_N^{[2]}=\ker(C_N+I)\);
3. \(\rho_2^2=I\), \(\rho_2^T\rho_2=I\), and \(\rho_2C_N=C_N\rho_2\);
4. regular-simplex Gram identities for \(W_N=\rho_2V_N\);
5. the cross-Gram formula \(\langle v_i,w_j\rangle=\delta_{ij}-1/N-(2/N)s_is_j\);
6. the \(N=4\) specialization \(w_i=-v_{i+2}\);
7. the \(N=6\) compound \(V_6\cup W_6\), including its unordered Gram profile and coordinate-permutation symmetry group;
8. absence of a \(\Phi_2\) parity component for odd \(N\).

```text
=== Parity-dual simplex verifier ===
[ok] N=2: parity-dual simplex verified; cross-Gram values=[Fraction(-1, 2), Fraction(1, 2)]
[ok] N=4: parity-dual simplex verified; cross-Gram values=[Fraction(-3, 4), Fraction(1, 4)]
[ok] N=6: parity-dual simplex verified; cross-Gram values=[Fraction(-1, 2), Fraction(1, 6), Fraction(1, 2)]
[ok] N=8: parity-dual simplex verified; cross-Gram values=[Fraction(-3, 8), Fraction(1, 8), Fraction(5, 8)]
[ok] N=10: parity-dual simplex verified; cross-Gram values=[Fraction(-3, 10), Fraction(1, 10), Fraction(7, 10)]
[ok] N=12: parity-dual simplex verified; cross-Gram values=[Fraction(-1, 4), Fraction(1, 12), Fraction(3, 4)]
[info] N=6 compound unordered Gram profile={Fraction(-1, 2): 12, Fraction(-1, 6): 30, Fraction(1, 6): 18, Fraction(1, 2): 6}
[info] N=6 coordinate-permutation symmetries=72 = 2*(3!)^2
[info] N=6 central inversion is not a compound symmetry; rho_2 exchanges the two simplices

[ok] N=3: no Phi_2 parity component
[ok] N=5: no Phi_2 parity component
[ok] N=7: no Phi_2 parity component
[ok] N=9: no Phi_2 parity component
[ok] N=11: no Phi_2 parity component
[ok] N=13: no Phi_2 parity component

All checks passed.
```
