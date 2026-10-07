"""
C11 -- the p-adic Newton polygon: companion to C6, the second place of Weil's 1/2.

C6 was the ARCHIMEDEAN Newton polygon: zeros of the apex live on rays normal to
the edges of the convex hull of the frequencies {y_s} in C -- the indicator
diagram, the place at infinity, where the critical line lives. Here we read the
SAME eigenvalues at the place p: the p-adic Newton polygon of the L-polynomial
P(T) = sum c_k T^k in Z[T] is the lower convex hull of (k, v_p(c_k)); its slopes
are the p-adic valuations of the Frobenius eigenvalues alpha_i.

The two places, one number 1/2:
  * Archimedean: |alpha_i| = sqrt q for EVERY i (Weil) -> Re s = 1/2.
  * p-adic: the slopes need NOT be 1/2 -- but they lie in [0,1], the polygon runs
    from (0,0) to (2g,g), so the AVERAGE slope is g/2g = 1/2, the slope of the
    Hodge diagonal. Newton lies on/above Hodge (Mazur).
      - ORDINARY (p = 1 mod N here): slopes {0^g, 1^g} = Hodge polygon exactly;
        half the eigenvalues are p-adic units, half are p/unit; average 1/2.
      - SUPERSINGULAR (cubic at p = 2 mod 3, a_p=0): P = 1 + p T^2, the Newton
        polygon is the straight diagonal, every slope = 1/2 -- the p-adic slopes
        LITERALLY equal the Archimedean weight. This is the crystalline shadow of
        the same 1/2.

So C6 (place infinity) and C11 (place p) are the two Newton polygons of one set of
eigenvalues, both pinned by 1/2: |alpha|=q^{1/2} at infinity, average slope 1/2 at p.
"""

import math
import numpy as np
from ff_core import make_chars, fermat_count_Fp
from c10_higher_genus import Lpoly as quartic_Lpoly


def vp(n, p):
    if n == 0:
        return math.inf
    v = 0
    n = abs(int(round(n)))
    while n % p == 0:
        n //= p; v += 1
    return v


def newton_slopes(coeffs, p):
    """Slopes of the lower convex hull of (k, v_p(c_k)), expanded by horizontal run."""
    pts = [(k, vp(c, p)) for k, c in enumerate(coeffs) if vp(c, p) != math.inf]
    pts.sort()
    # lower convex hull (monotone chain)
    hull = []
    for pt in pts:
        while len(hull) >= 2:
            (x0, y0), (x1, y1) = hull[-2], hull[-1]
            # pop if last point is not below the line (x0,y0)-(pt)
            if (y1 - y0) * (pt[0] - x0) >= (pt[1] - y0) * (x1 - x0):
                hull.pop()
            else:
                break
        hull.append(pt)
    slopes = []
    for (x0, y0), (x1, y1) in zip(hull, hull[1:]):
        s = (y1 - y0) / (x1 - x0)
        slopes += [s] * (x1 - x0)
    return slopes, hull


def hodge_polygon_slopes(g):
    return [0.0] * g + [1.0] * g


def check(coeffs, p, g, label, arch_alpha=None):
    slopes, hull = newton_slopes(coeffs, p)
    slopes_sorted = sorted(slopes)
    in01 = all(-1e-12 <= s <= 1 + 1e-12 for s in slopes)
    endpoints = hull[0] == (0, 0) and hull[-1] == (2 * g, g)
    avg = sum(slopes) / len(slopes)
    avg_half = abs(avg - 0.5) < 1e-12
    # Newton on/above Hodge: at each integer x, Newton_y >= Hodge_y
    def poly_y(sl):
        ys = [0.0]
        for s in sl:
            ys.append(ys[-1] + s)
        return ys
    ny, hy = poly_y(slopes_sorted), poly_y(hodge_polygon_slopes(g))
    # Mazur: the Newton polygon lies ON or ABOVE the Hodge polygon (same endpoints)
    above = all(ny[x] >= hy[x] - 1e-12 for x in range(2 * g + 1))
    ordinary = all(abs(s) < 1e-9 or abs(s - 1) < 1e-9 for s in slopes)
    ss = all(abs(s - 0.5) < 1e-9 for s in slopes)
    kind = "ordinary" if ordinary else ("supersingular" if ss else "mixed")
    arch = ""
    if arch_alpha is not None:
        weil = all(abs(abs(a) - math.sqrt(p)) < 1e-3 for a in arch_alpha)
        arch = f" | archimedean |alpha|=sqrt p:{weil} (Re s=1/2)"
    good = in01 and endpoints and avg_half and above
    print(f"  [{label}] slopes={[round(s,3) for s in slopes_sorted]} avg={avg:.3f} "
          f"({kind}); Newton>=Hodge:{above} endpoints{hull[0]}->{hull[-1]}{arch} "
          f"{'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 78)
    print("C11 -- p-adic Newton polygon: average slope 1/2 = the archimedean Weil weight")
    print("=" * 78)
    ok = True
    print("  ORDINARY (p = 1 mod N): Newton polygon = Hodge polygon, slopes {0^g,1^g}")
    # cubic g=1, p = 1 mod 3
    for p in (7, 13, 31, 61):
        a = p + 1 - fermat_count_Fp(p, 3)
        P = [1, -a, p]
        ok = check(P, p, 1, f"cubic g=1 p={p} (a_p={a})", arch_alpha=np.roots([1.0, -a, p])) and ok
    # quartic g=3, p = 1 mod 4
    for p in (13, 17, 29):
        P, _ = quartic_Lpoly(p)
        ok = check(P, p, 3, f"quartic g=3 p={p}", arch_alpha=np.roots([float(x) for x in P])) and ok
    print("  SUPERSINGULAR (cubic at p = 2 mod 3, a_p=0): every slope = 1/2 (crystalline 1/2)")
    for p in (5, 11, 17, 23):
        a = p + 1 - fermat_count_Fp(p, 3)
        P = [1, -a, p]
        ok = check(P, p, 1, f"cubic g=1 p={p} (a_p={a})", arch_alpha=np.roots([1.0, -a, p])) and ok
    print("-" * 78)
    print("C11:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
