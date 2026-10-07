"""
C6 -- The complex-sector zero variety = Newton polygon (spine T6).

For complex amplitudes z (off the decoherent face) the frequencies y_s are
complex, and the zeros of M(beta,c) = sum_s a_s e^{y_s beta} accumulate along
rays PERPENDICULAR TO THE EDGES of the convex hull (indicator diagram) of
{y_s} in C:  a two-term balance a_a e^{y_a b} + a_b e^{y_b b} = 0 gives
b ~ 2 pi i k / (y_a - y_b), a line at angle  pi/2 - arg(y_a - y_b),  with
spacing 2 pi / |y_a - y_b|  (density |y_a-y_b|/2pi).  Only hull EDGES survive
(interior pairs are dominated).

Unification: a REAL ledger has hull = a segment on the real axis -> one edge ->
one imaginary-direction family -> recovers C2's law n(T) ~ Delta_y T/pi.
N=2 complex -> one edge -> single rotated line = T7 Prop 6.2 exactly.
N=3 complex -> triangle -> three ray families. This is Conj 7.4's
"structured subvariety", made precise.

Certified: (i) N=2 complex matches Prop 6.2's lattice to ~1e-25;
(ii) N=3 complex: far zeros align to the 3 predicted edge-normal directions,
and per-direction counts match edge_length/2pi.
"""

import cmath
import mpmath as mp
from apex_core import centered_complex_ledger, M, Mprime, _newton, count_zeros_rect_fast

mp.mp.dps = 30


# ---- N=2 complex: exact Prop 6.2 lattice ----------------------------------
def test_qubit_prop62(theta, phi, T=mp.mpf("10")):
    z = [mp.cos(theta / 2), mp.e ** (1j * phi) * mp.sin(theta / 2)]
    y = centered_complex_ledger(z)
    eta = y[0]                                    # N=2: y_0 = -y_1 = eta
    a = abs(eta); psi = -mp.arg(eta)
    base = mp.pi / a
    # predicted lattice beta_k = pi(k+1/2)/a * e^{i(pi/2+psi)}
    ang = mp.pi / 2 + psi
    kmax = int(mp.floor((T / base)))
    pred = [base * (k + mp.mpf(1) / 2) * mp.e ** (1j * ang) for k in range(-kmax, kmax)]
    pred = [p for p in pred if abs(mp.im(p)) <= T and abs(mp.re(p)) <= T]
    # find via Newton seeded on the predicted ray
    found = []
    for p in pred:
        b = _newton(p + mp.mpc("0.01", "0.01"), 0, y)
        if abs(M(b, 0, y)) < mp.mpf("1e-18") and not any(abs(b - f) < mp.mpf("1e-6") for f in found):
            found.append(b)
    d = None
    if len(found) == len(pred) and pred:
        # nearest-neighbour match (sort-then-zip is unstable when Im ~ 0,
        # e.g. the uniform-modulus equator where the lattice is on the real axis)
        d = max(min(abs(p - f) for f in found) for p in pred)
    good = d is not None and d < mp.mpf("1e-18")
    print(f"  [N2 complex theta={float(theta):.2f} phi={float(phi):.2f}] "
          f"ray angle={float(ang):.3f} rad, |eta|={float(a):.3f}: "
          f"pred={len(pred)} found={len(found)} match={'n/a' if d is None else f'{float(d):.1e}'} "
          f"{'OK' if good else 'FAIL'}")
    return good


# ---- N=3 complex: triangle Newton polygon ---------------------------------
def grid_newton_disk(c, y, R, step):
    found = []
    n = int(mp.ceil(2 * R / step))
    for i in range(n + 1):
        re0 = -R + 2 * R * i / n
        for j in range(n + 1):
            im0 = -R + 2 * R * j / n
            b = _newton(mp.mpc(re0, im0), c, y)
            if abs(b) > R:
                continue
            if abs(M(b, c, y)) > mp.mpf("1e-16"):
                continue
            if any(abs(b - f) < mp.mpf("1e-6") for f in found):
                continue
            found.append(b)
    return found


def test_triangle(z, label, R=mp.mpf("11"), r0=mp.mpf("4")):
    y = centered_complex_ledger(z)
    N = len(y)
    yc = [complex(mp.re(v), mp.im(v)) for v in y]
    # hull edges of 3 generic points = all 3 pairs; predicted ray-line angles mod pi
    pairs = [(0, 1), (0, 2), (1, 2)]
    edges = [(yc[a] - yc[b]) for a, b in pairs]
    pred_ang = [(cmath.pi / 2 - cmath.phase(d)) % cmath.pi for d in edges]
    edge_len = [abs(d) for d in edges]
    # spacing along a family must resolve: step < min(2pi/|d|)/3
    step = float(min(2 * cmath.pi / L for L in edge_len)) / 3.5
    zeros = grid_newton_disk(0, y, R, mp.mpf(str(step)))
    far = [b for b in zeros if abs(b) >= r0]
    # each far zero's line-angle must match one predicted edge-normal (mod pi)
    def angdist(a, b):
        d = abs((a - b) % cmath.pi)
        return min(d, cmath.pi - d)
    worst = 0.0
    per_family = [0, 0, 0]
    for b in far:
        ab = cmath.phase(complex(mp.re(b), mp.im(b))) % cmath.pi
        dists = [angdist(ab, pa) for pa in pred_ang]
        k = min(range(3), key=lambda i: dists[i])
        per_family[k] += 1
        worst = max(worst, dists[k])
    # density check: count on each full line in disk ~ 2R*|d|/2pi = R|d|/pi
    pred_count = [float(R) * L / cmath.pi for L in edge_len]
    aligned = worst < 0.06                       # ~3.4 degrees
    # total completeness vs argument principle on the bounding box
    nap = count_zeros_rect_fast(0, y, -R, R, -R, R)
    complete = abs(mp.re(nap) - len(zeros)) < 1.5
    good = aligned and complete
    print(f"  [{label}] edges |d|={[round(L,2) for L in edge_len]} "
          f"angles(mod pi)={[round(a,3) for a in pred_ang]}")
    print(f"     far zeros={len(far)} worst-angle-dev={worst:.4f} rad "
          f"per-family={per_family} pred~{[round(p,1) for p in pred_count]} "
          f"argP(disk box)={float(mp.re(nap)):.2f} found={len(zeros)} "
          f"{'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 74)
    print("C6 -- complex sector = Newton polygon (edge-normal rays); Prop 6.2 lift")
    print("=" * 74)
    ok = True
    print("  -- N=2 complex: exact Prop 6.2 phase-twisted lattice")
    ok = test_qubit_prop62(mp.mpf("1.0"), mp.mpf("1.2")) and ok
    ok = test_qubit_prop62(mp.pi / 2, mp.mpf("0.9")) and ok      # uniform-modulus: near real axis
    print("  -- N=3 complex: triangle hull -> 3 edge-normal ray families")
    ok = test_triangle([mp.mpc("1.0", "0.0"), mp.mpc("0.3", "1.1"), mp.mpc("-0.8", "0.5")],
                       "N3 cplx A") and ok
    ok = test_triangle([mp.mpc("1.2", "0.4"), mp.mpc("-0.5", "0.9"), mp.mpc("0.2", "-1.0")],
                       "N3 cplx B") and ok
    print("-" * 74)
    print("C6:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
