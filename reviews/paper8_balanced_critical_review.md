# Paper 8 Balanced Critical Review

**Scope:** `8.parity_dual_simplices.md`

**Source:** User-supplied balanced critical review, May 2026.

---

## Review Summary

The review is positive about the paper's core move: it demystifies the `N=4` stella-octangula phenomenon by separating Galois conjugation from parity reflection and then classifying the higher even-`N` stabilizers.  It especially values the clean linear-algebraic formulation through the `Phi_2` parity axis and the stabilizer theorem for `N>=6`.

The main critique is that the paper currently has more algebra than geometry.  It identifies symmetries and Gram profiles of

```text
X_N = V_N union W_N,
```

but does not say enough about the convex hull or the geometric family to which the higher-dimensional compounds belong.

---

## Action Items

1. **Define Janus locally.**
   The paper should not assume the reader knows the internal "Janus" vocabulary.  Add a short definition: in the `N=4` companion context, Janus is the orientation bit/choice of one of the two complementary tetrahedra in the stella octangula, equivalently the sign of the `H_4` volume form or cross-product convention.

2. **Reframe the ETF negative result.**
   The compound is not a single ETF for `N>=6`, but it is still useful:
   - it is a union of two regular simplex ETFs;
   - after unit normalization it is a unit-norm tight frame;
   - it is vertex-transitive under its full orthogonal stabilizer;
   - it has an explicitly controlled angle profile.

3. **Soften the odd-`N` dismissal.**
   Odd `N` has no `Phi_2` parity axis, so this construction is absent.  But other cyclotomic block reflections still exist and deserve a future-work sentence.

4. **Add the missing polyhedral geometry.**
   Identify the convex hull:

   ```text
   conv(X_N) = (Delta_E direct-sum Delta_O) x I
   ```

   where `Delta_E` and `Delta_O` are the two parity-class regular simplices in the even and odd zero-sum subspaces.  Equivalently, it is a prism over the free sum of two `(m-1)`-simplices for `N=2m`.  For `N=4`, this recovers the cube; for `N=6`, it is a 5-polytope with 12 vertices, a prism over the free sum of two triangles.

5. **Add empirical polytope report.**
   At the time of this review SciPy was not available in the runtime, so the safe path was to use the exact decomposition to generate f-vectors rather than relying on numerical convex-hull software.

---

## Priority

Highest priority: the convex-hull theorem.  This directly answers the review's top missing direction and gives the paper a geometric conclusion matching its Coxeter/polytope framing.

---

## Implementation Status

- Added local Janus definition to `8.parity_dual_simplices.md`.
- Added unit-norm tight-frame clarification for `V_N union W_N`.
- Added odd-`N` clarification: no `Phi_2` parity axis, but other cyclotomic block reflections remain future work.
- Added Theorem 6.2 identifying `conv(X_N)` as a prism over the free sum of two equal simplices.
- Added `empirical/census_parity_dual_polytope.py` and `empirical/reports/parity_dual_polytope.md`.
