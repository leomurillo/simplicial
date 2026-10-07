"""
C4 -- The character index c is a phase/offset, not a zero-mover.

(i) Cyclic-shift covariance (exact, all ledgers): relabelling x_s -> x_{s+1}
    on Z/N gives  M_shift(beta,c) = zeta^c * M(beta,c),  zeta = e^{2 pi i/N}.
    Hence the zero set of every mode c is INVARIANT under cyclic relabelling,
    and the ratio M_shift/M is the constant zeta^c (independent of beta).

(ii) Geometric exact offset (from C3): mode c deletes residue class c from the
     common lattice {2 pi i m/(aN)} -- so c only shifts WHICH lattice points are
     excluded (the a_1+...+a_n = c selection rule), leaving spacing/density fixed.

Together with C2 (density c-independent) this pins c to the imaginary-offset role.
"""

import mpmath as mp
from apex_core import centered_log_ledger, strip_bound, M, find_zeros_rect

mp.mp.dps = 30
RNG = __import__("numpy").random.default_rng(7)


def cyclic_shift(x):
    return x[1:] + x[:1]


def test_covariance(x, label, T=mp.mpf("9.2")):
    N = len(x)
    y = centered_log_ledger(x)
    ys = centered_log_ledger(cyclic_shift(x))
    zeta = mp.e ** (2j * mp.pi / N)
    ok = True
    # (a) constant-phase ratio M_shift/M = zeta^c at random sample points
    max_ratio_err = mp.mpf(0)
    for c in range(N):
        for bsamp in (mp.mpc("0.3", "1.1"), mp.mpc("-0.7", "2.4"), mp.mpc("0.1", "-3.3")):
            r = M(bsamp, c, ys) / M(bsamp, c, y)
            max_ratio_err = max(max_ratio_err, abs(r - zeta ** c))
    # (b) every zero of mode c for x is a zero of mode c for the shifted ledger
    #     (corollary of the constant-phase covariance; checked by direct eval,
    #      which avoids re-find/pairing fragility near the box boundary)
    Rm, Rp = strip_bound(y, N); pad = mp.mpf("0.7")
    max_cross_resid = mp.mpf(0)
    for c in range(N):
        for b in find_zeros_rect(c, y, -(Rm + pad), Rp + pad, -T, T):
            max_cross_resid = max(max_cross_resid, abs(M(b, c, ys)))
    good = (max_ratio_err < mp.mpf("1e-25")) and (max_cross_resid < mp.mpf("1e-15")) and ok
    print(f"  [{label}] N={N}: |M_shift/M - zeta^c|max={float(max_ratio_err):.1e} "
          f"cross-resid={float(max_cross_resid):.1e} {'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 74)
    print("C4 -- c is a phase/offset: cyclic-shift covariance (zeros invariant)")
    print("=" * 74)
    ok = True
    ok = test_covariance([1, 2, 3], "N3 [1,2,3]") and ok
    ok = test_covariance([1, 3, 9], "N3 geom") and ok
    ok = test_covariance([1, 2, 3, 4, 5], "N5 ramp") and ok
    ok = test_covariance(list(1 + RNG.random(6) * 5), "N6 rand") and ok
    print("-" * 74)
    print("C4:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
