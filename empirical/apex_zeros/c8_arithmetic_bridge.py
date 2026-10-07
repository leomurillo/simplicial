"""
C8 -- The arithmetic bridge (the thesis probe).

Units-indicator ledger on Z/N (T7 7.6's named arithmetic ledger): x_s = e if
gcd(s,N)=1 else 1. It is 2-LEVEL, so via Ramanujan sums
    S_units(c) = sum_{gcd(s,N)=1} zeta^{-cs} = c_N(c)   (Ramanujan sum),
    S_nonunits(c) = -c_N(c)  for c != 0,   = N-phi(N) for c = 0,
the generator collapses to a TWO-TERM exponential sum
    M(beta,c) = (1/N)[ A_c e^{beta u} + B_c e^{beta v} ],  u-v = 1,
whose single line of zeros sits at  Re beta = log|B_c/A_c| / (u-v).

Two readings, both certified here:
  (1) c != 0: A_c = c_N(c), B_c = -c_N(c)  -> EQUAL modulus -> Re beta = 0
      (unitarity again forces the trivial line);
  (2) c = 0:  A_0 = phi(N), B_0 = N-phi(N) -> UNEQUAL modulus
      -> Re beta = log((N-phi(N))/phi(N)) != 0, an ARITHMETIC off-line position
      that GROWS along primorials (more primes -> phi/N smaller).

THE BRIDGE: arithmetic moves the LINE POSITION (via unequal coefficient moduli
-- here phi vs N-phi, the simplest arithmetic weights; the sqrt(q) Frobenius/
Gauss weights of the function-field lift are the deep version that yields Weil's
1/2). But the zero DENSITY stays Delta_y/pi -- CONSTANT, linear in T, NO log
factor. zeta's n(T) ~ (T/2pi)log T has the log; the finite apex cannot produce
it (it is exponential type). The missing log = the archimedean place. This is
the precise, honest localization of why the classical target is hard, and ties
to T15 / P0 / the N-series Archimedean operator.
"""

import math
import mpmath as mp
from apex_core import centered_log_ledger, M, find_zeros_rect, count_zeros_rect_fast

mp.mp.dps = 30


def units_ledger(N):
    return [mp.e if math.gcd(s, N) == 1 else mp.mpf(1) for s in range(N)]


def phi(N):
    return sum(1 for s in range(N) if math.gcd(s, N) == 1)


def test_line(N, T=mp.mpf("12.0")):
    x = units_ledger(N)
    y = centered_log_ledger(x)
    ph = phi(N)
    Restar = mp.log(mp.mpf(N - ph) / ph)          # predicted c=0 line (u-v = 1)
    box = (mp.mpf("-0.5"), mp.mpf("2.0"), -T, T)
    # c = 0 : off-line at Re*
    z0 = find_zeros_rect(0, y, *box)
    re0 = max((abs(mp.re(b) - Restar) for b in z0), default=mp.mpf(99))
    im0_odd = max((abs(mp.im(b) / mp.pi - mp.nint(mp.im(b) / mp.pi)) for b in z0), default=mp.mpf(0))
    # Im should be ODD multiples of pi (A0,B0 same sign -> -B/A negative)
    im0_parity = all(int(mp.nint(mp.im(b) / mp.pi)) % 2 == 1 for b in z0)
    # c = 1 : on-line at Re = 0 (equal-modulus Ramanujan)
    z1 = find_zeros_rect(1, y, *box)
    re1 = max((abs(mp.re(b)) for b in z1), default=mp.mpf(99))
    good = (re0 < mp.mpf("1e-15") and im0_odd < mp.mpf("1e-12") and im0_parity
            and re1 < mp.mpf("1e-12"))
    print(f"  [N={N:4d}] phi={ph:4d}  Re*(c=0)=log((N-phi)/phi)={float(Restar):.4f}  "
          f"c0: max|Re-Re*|={float(re0):.1e} odd-pi={im0_parity} | "
          f"c1: max|Re|={float(re1):.1e}  {'OK' if good else 'FAIL'}")
    return good, float(Restar)


def test_density_no_log(N):
    """Density is Delta_y/pi (linear); explicitly NOT T log T (the archimedean gap)."""
    x = units_ledger(N)
    y = centered_log_ledger(x)
    Dy = max(mp.re(v) for v in y) - min(mp.re(v) for v in y)   # = 1 for this ledger
    pred = float(Dy / mp.pi)
    box_re = (mp.mpf("-0.5"), mp.mpf("2.0"))
    Ts = [20.0, 40.0, 80.0, 160.0]
    counts = []
    for T in Ts:
        n = count_zeros_rect_fast(0, y, box_re[0], box_re[1], -mp.mpf(T), mp.mpf(T))
        counts.append(int(mp.nint(mp.re(n))))
    # linear fit residual vs a forced log model
    import numpy as np
    A_lin = np.array([[t, 1.0] for t in Ts])
    a_lin, *_ = np.linalg.lstsq(A_lin, counts, rcond=None)
    lin_res = max(abs(a_lin[0] * t + a_lin[1] - c) for t, c in zip(Ts, counts))
    # log model n = g * T log T : best g, see how badly it misfits
    g = sum(c * (t * math.log(t)) for t, c in zip(Ts, counts)) / sum((t * math.log(t)) ** 2 for t in Ts)
    log_res = max(abs(g * t * math.log(t) - c) for t, c in zip(Ts, counts))
    good = abs(a_lin[0] - pred) < 0.02 and lin_res < 2.0 and log_res > 3 * lin_res
    print(f"  [N={N:4d}] counts={counts} lin_slope={a_lin[0]:.4f} pred(Dy/pi)={pred:.4f} "
          f"lin_resid={lin_res:.2f} (TlogT misfit={log_res:.1f}) {'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 78)
    print("C8 -- arithmetic bridge: units-indicator ledger, Ramanujan-sum 2-term apex")
    print("=" * 78)
    ok = True
    print("  -- line position: c=0 off-line at log((N-phi)/phi); c!=0 on Re=0")
    restars = []
    for N in (6, 30, 210):
        g, rs = test_line(N)
        ok = g and ok
        restars.append(rs)
    growing = all(restars[i] < restars[i + 1] for i in range(len(restars) - 1))
    print(f"     Re*(c=0) along primorials 6,30,210 = {[round(r,4) for r in restars]} "
          f"-> increasing={growing} {'OK' if growing else 'FAIL'}")
    ok = growing and ok
    print("  -- density stays Delta_y/pi (CONSTANT, no log) -- the archimedean gap:")
    for N in (6, 30, 210):
        ok = test_density_no_log(N) and ok
    print("-" * 78)
    print("C8:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
