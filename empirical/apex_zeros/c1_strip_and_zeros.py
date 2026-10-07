"""
C1 -- Strip confinement + zero completeness.

Claims certified (T1, T2 of the spine):
  * M(.,c) has only finitely many zeros in any bounded box, all genuine
    (|M| ~ 0), and the count matches the argument principle (completeness).
  * Every zero lies in the provable vertical strip
        -log(N-1)/(y_(2)-y_(1)) <= Re beta <= log(N-1)/(y_(N)-y_(N-1)).

Runs over N = 3, 4, 6, structured and random real ledgers, characters c.
"""

import numpy as np
import mpmath as mp

from apex_core import (centered_log_ledger, spread, strip_bound,
                       M, count_zeros_rect_fast, find_zeros_rect)

RNG = np.random.default_rng(0)
T = mp.mpf("12.37")          # box half-height (off-lattice to avoid contour hits)
PAD = mp.mpf("0.75")         # real padding beyond the strip bound
RESID_TOL = mp.mpf(10) ** (-15)
STRIP_TOL = mp.mpf("1e-9")


def test_ledger(x, label):
    y = centered_log_ledger(x)
    N = len(y)
    Rm, Rp = strip_bound(y, N)
    re_lo, re_hi = -(Rm + PAD), (Rp + PAD)
    ok = True
    lines = []
    for c in range(N):
        n_ap = count_zeros_rect_fast(c, y, re_lo, re_hi, -T, T)
        n_int = int(mp.nint(mp.re(n_ap)))
        clean = abs(mp.re(n_ap) - n_int) < mp.mpf("0.02") and abs(mp.im(n_ap)) < mp.mpf("0.02")
        zeros = find_zeros_rect(c, y, re_lo, re_hi, -T, T)
        max_resid = max((abs(M(b, c, y)) for b in zeros), default=mp.mpf(0))
        max_absre = max((abs(mp.re(b)) for b in zeros), default=mp.mpf(0))
        in_strip = all(-(Rm + STRIP_TOL) <= mp.re(b) <= (Rp + STRIP_TOL) for b in zeros)
        complete = (len(zeros) == n_int)
        good = clean and complete and (max_resid < RESID_TOL) and in_strip
        ok = ok and good
        lines.append(
            f"    c={c}: argP={float(mp.re(n_ap)):+.4f} (n={n_int}) found={len(zeros)} "
            f"resid={float(max_resid):.1e} max|Re|={float(max_absre):.4f} "
            f"strip<=({float(Rm):.4f},{float(Rp):.4f}) {'OK' if good else 'FAIL'}"
        )
    print(f"  [{label}] N={N} Delta_y={float(spread(y)):.4f}")
    for ln in lines:
        print(ln)
    return ok


def main():
    print("=" * 74)
    print("C1 -- Strip confinement + zero completeness (argument principle)")
    print("=" * 74)
    ledgers = [
        ([1, 2, 3], "N3 ramp"),
        ([1, 3, 9], "N3 geom"),
        (list(1 + RNG.random(3) * 5), "N3 rand"),
        ([1, 2, 3, 4], "N4 ramp"),
        (list(1 + RNG.random(4) * 5), "N4 rand"),
        ([1, 2, 3, 4, 5, 6], "N6 ramp"),
        (list(1 + RNG.random(6) * 5), "N6 rand"),
    ]
    ok = True
    for x, label in ledgers:
        ok = test_ledger(x, label) and ok
    print("-" * 74)
    print("C1:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
