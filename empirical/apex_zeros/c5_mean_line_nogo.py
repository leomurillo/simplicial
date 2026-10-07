"""
C5 -- Approximate critical line / the no-go (spine T4).

For a GENERIC (non-geometric) real ledger the zeros do not lie on a line, but
because all coefficients have equal modulus 1/N (characters are unitary), the
Newton diagram of {(y_s, log|a_s|)} is horizontal, so every zero family
accumulates on Re beta = 0:

   * mean of Re(beta) over |Im beta| <= T  ->  0   (approximate critical line),
   * RMS spread of Re(beta) stays > 0 and BOUNDED  (genuinely off-line),
   * spread = 0 exactly only on the equal-spacing (geometric) locus (C3).

This is the honest statement that the ADDITIVE apex has no arithmetic critical
line: the Re=0 accumulation is forced by unitarity, not by arithmetic, and is
only approximate off the symmetry locus. (Breaking equal-modulus -- e.g. sqrt(q)
Frobenius/Gauss weights in the function-field lift -- is what creates a genuine
nontrivial line; see the bridge / C8.)
"""

import mpmath as mp
from apex_core import centered_log_ledger, strip_bound, find_zeros_rect

mp.mp.dps = 30


def re_stats(x, c, T):
    y = centered_log_ledger(x)
    N = len(y)
    Rm, Rp = strip_bound(y, N)
    pad = mp.mpf("0.7")
    z = find_zeros_rect(c, y, -(Rm + pad), Rp + pad, -T, T)
    res = [mp.re(b) for b in z]
    n = len(res)
    if n == 0:
        return 0, mp.mpf(0), mp.mpf(0)
    mean = sum(res) / n
    rms = mp.sqrt(sum((r - mean) ** 2 for r in res) / n)
    return n, mean, rms


def test_generic(x, label):
    n20, m20, s20 = re_stats(x, 0, mp.mpf("20.1"))
    n80, m80, s80 = re_stats(x, 0, mp.mpf("80.1"))
    off_line = s80 > mp.mpf("0.03")                        # genuinely off the axis
    mean_small = abs(m80) < mp.mpf("0.03")                 # approximate line
    mean_decays = abs(m80) <= abs(m20) + mp.mpf("0.005")   # mean -> 0 as T grows
    spread_bounded = s80 <= s20 * mp.mpf("1.6")            # spread does not grow
    good = off_line and mean_small and mean_decays and spread_bounded
    print(f"  [{label}] T=20: mean_Re={float(m20):+.4f} rms_Re={float(s20):.4f} (n={n20}) | "
          f"T=80: mean_Re={float(m80):+.4f} rms_Re={float(s80):.4f} (n={n80}) "
          f"{'OK' if good else 'FAIL'}")
    return good


def test_geometric(x, label):
    _, m80, s80 = re_stats(x, 0, mp.mpf("80.1"))
    good = s80 < mp.mpf("1e-12")
    print(f"  [{label}] (symmetry locus) rms_Re={float(s80):.1e} mean_Re={float(m80):.1e} "
          f"{'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 74)
    print("C5 -- approximate critical line: mean Re->0, spread>0 (no-go for exact line)")
    print("=" * 74)
    ok = True
    ok = test_generic([1, 2, 3], "N3 [1,2,3]") and ok
    ok = test_generic([1, 2, 3, 4], "N4 ramp") and ok
    ok = test_generic([1, 4, 9, 16, 25], "N5 squares") and ok
    ok = test_generic([2, 3, 5, 7, 11, 13], "N6 primes") and ok
    print("  -- symmetry locus (geometric): spread is exactly zero")
    ok = test_geometric([1, 3, 9, 27, 81], "N5 geom") and ok
    print("-" * 74)
    print("C5:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
