# Empirical Verification: Galois Simplex Units

**Script:** `empirical/verify_galois_simplex_units.py`  
**Companion note:** `7.galois_simplex_units.md`  
**Status:** all checks passed

This report records the verifier output for the Galois/simplex and cyclotomic-unit identities.  The exact checks cover:

1. normalizer/Galois conjugation: \(\sigma_a C_N\sigma_a^{-1}=C_N^a\);
2. Gram normalization: \(G_{\mathrm{simp}}=(1/p)G_{\mathrm{trace}}\);
3. determinant normalization: \(\det G_{\mathrm{simp}}=1/p\), \(\det G_{\mathrm{trace}}=p^{p-2}\);
4. arc-sum norm agreement for prime cyclotomic units;
5. real palindromic arc-star norm checks;
6. \(p=5\) and \(p=7\) geometric orbit checks.

The regulator values are numerical exploratory output for the log-arc-star parallelotope picture.

```text
=== Galois/simplex verifier ===
[ok] N=3: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=4: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=5: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=6: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=7: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=8: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=9: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=11: sigma_a C sigma_a^-1 = C^a for all units a
[ok] N=13: sigma_a C sigma_a^-1 = C^a for all units a

[ok] p=3: G_simp=(1/p)G_trace, det(G_simp)=1/3, det(G_trace)=3^1
[ok] p=3: all arc-sum norms match trace normalization

[ok] p=5: G_simp=(1/p)G_trace, det(G_simp)=1/5, det(G_trace)=5^3
[ok] p=5: all arc-sum norms match trace normalization
[ok] p=5: palindromic arc-stars have real norm +/-1
[info] p=5: regulator candidate |det(log embeddings)| = 0.48121182506
        0.481211825

[ok] p=7: G_simp=(1/p)G_trace, det(G_simp)=1/7, det(G_trace)=7^5
[ok] p=7: all arc-sum norms match trace normalization
[ok] p=7: palindromic arc-stars have real norm +/-1
[info] p=7: regulator candidate |det(log embeddings)| = 0.525454682123
        0.809586916   0.588862606
       -0.588862606   0.220724310

[ok] p=11: G_simp=(1/p)G_trace, det(G_simp)=1/11, det(G_trace)=11^9
[ok] p=11: all arc-sum norms match trace normalization
[ok] p=11: palindromic arc-stars have real norm +/-1
[info] p=11: regulator candidate |det(log embeddings)| = 1.63569412559

[ok] p=13: G_simp=(1/p)G_trace, det(G_simp)=1/13, det(G_trace)=13^11
[ok] p=13: all arc-sum norms match trace normalization
[ok] p=13: palindromic arc-stars have real norm +/-1
[info] p=13: regulator candidate |det(log embeddings)| = 3.77450098008

[ok] p=5: u_2 is edge sum; real unit phi is 3-star
[ok] p=7: eta_5 equals negative opposite pair modulo gauge
[info] p=7 eta_3 Galois orbit (skip, vertex set):
       1 -> (0, 1, 6)
       2 -> (0, 2, 5)
       3 -> (0, 3, 4)
[info] p=7 eta_5 negative-pair orbit (skip, vertex pair):
       1 -> (1, 6)
       2 -> (2, 5)
       3 -> (3, 4)

All checks passed.
```

