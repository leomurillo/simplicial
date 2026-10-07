"""
Break-the-wall attempt: the FINITE intersection form and its Hodge positivity, built
explicitly, to locate exactly where "the arrow is pure" (|alpha|=sqrt q) becomes an
UNCONDITIONAL theorem -- and whether the primorial truncation supplies it.

The finite intersection / Hodge form, done right, is the ROSATI FORM: the
positive-definite trace pairing <phi,psi> = Tr(phi . psi^Rosati) on the endomorphisms
of the Jacobian.  Its positive-definiteness IS the abelian-variety Hodge index
(Castelnuovo-Severi), and it FORCES the Frobenius eigenvalues onto |alpha|=sqrt q.
We test the foothold across three tiers:

  TIER 0  the conductor lattice Z/N itself (the primorial apex's own base ring):
          the "Frobenius" is multiplication by a unit; its eigenvalues are Dirichlet
          characters, |chi|=1 -- GENUS 0, RH trivial, NO content (matches T8 sec 5.3:
          the finite truncation carries no normalization forcing zeros onto a line).

  TIER 1  the genus>=1 curve over F_q (Fermat cubic, CM by Z[omega]): the Frobenius is
          alpha in Z[omega] with NORM = q; the Rosati form is the norm form
          a^2-ab+b^2 (Gram [[1,-1/2],[-1/2,1]], eigenvalues 1/2, 3/2 > 0 -- POSITIVE
          DEFINITE), so N(alpha)=q forces |alpha|=sqrt q UNCONDITIONALLY.  This is the
          finite Castelnuovo, with content, computed.

  TIER 2  the archimedean zeta: the analogous Rosati form would live on End of the
          (non-existent) F_1 self-product surface.  No abelian variety, no positive
          pairing -- the positivity is RH itself.

Conclusion the probe will force: the unconditional finite Hodge positivity exists and
is the Rosati form, but ONLY at genus>=1 over F_q (Tier 1).  The primorial base ring
(Tier 0) is genus 0 (no content); zeta (Tier 2) is the missing-surface case.  So the
foothold is the proven function-field template, not a primorial shortcut -- the wall is
the archimedean Rosati form (the F_1 surface), named to the object.

Deterministic: pure python + cmath.  No torch.
"""

import cmath

w = cmath.exp(2j * cmath.pi / 3)           # primitive cube root of unity

# The Rosati / norm form on Z[omega] in the basis {1, omega}:  <x,y> = Re(x conj y)
G = [[1.0, -0.5], [-0.5, 1.0]]             # Gram matrix
# eigenvalues of G: (trace +/- sqrt(trace^2-4det))/2, trace=2, det=3/4
tr, det = G[0][0] + G[1][1], G[0][0] * G[1][1] - G[0][1] * G[1][0]
ev_lo = (tr - (tr * tr - 4 * det) ** 0.5) / 2
ev_hi = (tr + (tr * tr - 4 * det) ** 0.5) / 2

print("=" * 84)
print("THE ROSATI / HODGE FORM on Z[omega]  (basis {1, omega})")
print("=" * 84)
print(f"  Gram G = [[1, -1/2], [-1/2, 1]],  eigenvalues = {ev_lo:.4f}, {ev_hi:.4f}  "
      f"(both > 0 => POSITIVE DEFINITE)")
print("  => N(a+b*omega) = a^2 - a b + b^2 = v^T G v > 0 for (a,b) != 0.")
print("  This positive-definiteness is the abelian-variety Hodge index (Rosati).")
print("  ANY alpha with N(alpha)=q therefore has |alpha| = sqrt q -- UNCONDITIONALLY.")

def norm(a, b):
    return a * a - a * b + b * b

def find_frob(q):
    """alpha = a + b*omega in Z[omega] with N(alpha)=q (q = 1 mod 3 splits)."""
    R = int(q**0.5) + 2
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            if norm(a, b) == q:
                return a, b
    return None

# ---------------------------------------------------------------------------
print()
print("=" * 84)
print("TIER 1 -- genus 1 (Fermat cubic over F_q):  Rosati positivity FORCES |alpha|=sqrt q")
print("=" * 84)
print(f"  {'q':>4} {'(a,b)':>10} {'N=a^2-ab+b^2':>14} {'q':>5} {'|alpha|':>10} {'sqrt q':>10} {'tr=2a-b':>8}")
for q in [7, 13, 19, 31, 37, 43, 61, 67]:
    ab = find_frob(q)
    if ab is None:
        continue
    a, b = ab
    alpha = a + b * w
    print(f"  {q:>4} {str(ab):>10} {norm(a,b):>14} {q:>5} {abs(alpha):>10.5f} {q**0.5:>10.5f} {2*a-b:>8}")
print("  >>> N(alpha) = q EXACTLY and |alpha| = sqrt q EXACTLY: the eigenvalue sits on the")
print("      critical circle BECAUSE the Rosati form is positive definite. No RH assumed.")
print("      (tr = 2a-b matches the curve's a_q up to the 6 units of Z[omega]; probe (1)")
print("       already certified a_q = -2 Re J via the point count.)")

# ---------------------------------------------------------------------------
print()
print("=" * 84)
print("TIER 0 -- the conductor lattice Z/N itself (the primorial apex base ring)")
print("=" * 84)
print("  The 'Frobenius' on functions on (Z/N)^x is multiplication by a unit a; its")
print("  eigenvalues are the Dirichlet characters chi(a), all on the UNIT circle |chi|=1.")
for N in [6, 30, 210]:
    # units mod N
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    # eigenvalues of mult-by-a are chi(a) for characters chi; |chi(a)|=1 always.
    print(f"  N={N:>4}: phi(N)={len(units):>3} units; mult-by-unit eigenvalues are characters, "
          f"|chi|=1 (genus 0 -- RH trivial, no content)")
print("  >>> The primorial base ring is GENUS 0: the critical-circle statement is free and")
print("      empty (characters are unimodular by definition).  Matches T8 sec 5.3 -- the")
print("      finite Dirichlet polynomial carries no normalization forcing zeros onto a line.")
print("      The content is NOT in the base ring; it is in genus>=1 curves OVER it (Tier 1).")

# ---------------------------------------------------------------------------
print()
print("=" * 84)
print("TIER 2 -- the archimedean zeta:  the Rosati form is the MISSING object")
print("=" * 84)
print("""  Over Q the analogous positive pairing would live on End of the self-product
  surface Spec(Z) x_{F_1} Spec(Z) -- which does not exist as a scheme.  There is no
  abelian variety, no Rosati involution, no positive-definite norm form to force the
  zeros onto Re(s)=1/2.  The archimedean 'Rosati positivity' IS the Weil positivity at
  infinity = RH.  This is precisely the N_infty / V_arith operator of P0 sec 8.3 whose
  self-adjointness is the open step.""")

print()
print("=" * 84)
print("VERDICT (calibrated after the math)")
print("=" * 84)
print("""  The finite intersection/Hodge form, built explicitly, is the ROSATI form, and its
  positive-definiteness is UNCONDITIONAL and FORCES |alpha|=sqrt q -- but only at
  genus >= 1 over F_q (Tier 1), where the Jacobian / abelian variety exists.

   - Tier 0 (primorial base ring Z/N): genus 0, characters unimodular -- the foothold
     I proposed (a primorial-truncation Castelnuovo) is EMPTY.  The truncation is the
     wrong object; T8 sec 5.3 already said its zeros lie on no line.
   - Tier 1 (curve over F_q): the foothold is REAL and computed -- the proven template.
   - Tier 2 (zeta over Q): the Rosati form is the missing F_1 surface = RH.

  So the wall is named to the object: the archimedean Rosati / Hodge positivity on the
  F_1 self-product surface.  The function-field genus>=1 case is the proven twin; the
  primorial truncation is genus 0 and does NOT shortcut it.  The honest break-point is
  therefore NOT a finite primorial Castelnuovo (it is empty), but either (i) construct
  the F_1 surface (Connes-Consani), or (ii) the cubic route -- the unconditional
  content that survives at order three (cluster c_2<0 + test class non-empty),
  reducing to the primorial-BV rate [A3'].  The quadratic finite Hodge form does not
  carry it; the genus-0 truncation proves why.""")
