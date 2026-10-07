"""
C7 -- Functional equation / conjugation symmetry (spine T5).

Exact identity for a real ledger:   conj( M(conj(beta), c) ) = M(beta, -c).
Consequences:
  * zero set of mode c  =  complex conjugate of zero set of mode (N-c);
  * self-conjugate modes c in {0, N/2} have REAL coefficients, so their zero
    sets are symmetric about the real axis (beta zero => conj(beta) zero).
This is the apex analog of an L-function functional equation (relating the
character c to its dual -c), and it pairs with C6's Newton-polygon symmetry.
"""

import mpmath as mp
from apex_core import centered_log_ledger, strip_bound, M, find_zeros_rect

mp.mp.dps = 30
RNG = __import__("numpy").random.default_rng(3)


def test_identity(x, label):
    y = centered_log_ledger(x)
    N = len(y)
    worst = mp.mpf(0)
    for c in range(N):
        for b in (mp.mpc("0.4", "1.3"), mp.mpc("-0.9", "2.1"), mp.mpc("0.2", "-2.7")):
            lhs = mp.conj(M(mp.conj(b), c, y))
            rhs = M(b, (-c) % N, y)
            worst = max(worst, abs(lhs - rhs))
    good = worst < mp.mpf("1e-25")
    print(f"  [{label}] N={N}: |conj M(conj b,c) - M(b,-c)|max = {float(worst):.1e} "
          f"{'OK' if good else 'FAIL'}")
    return good


def test_conjugate_pairing(x, label, T=mp.mpf("9.0")):
    y = centered_log_ledger(x)
    N = len(y)
    Rm, Rp = strip_bound(y, N); pad = mp.mpf("0.7")
    # zeros of mode c, conjugated, must be zeros of mode (-c)
    cross = mp.mpf(0)
    for c in range(N):
        for b in find_zeros_rect(c, y, -(Rm + pad), Rp + pad, -T, T):
            cross = max(cross, abs(M(mp.conj(b), (-c) % N, y)))
    # self-conjugate modes: zeros symmetric about real axis
    self_modes = [0] + ([N // 2] if N % 2 == 0 else [])
    selfsym = mp.mpf(0)
    for c in self_modes:
        for b in find_zeros_rect(c, y, -(Rm + pad), Rp + pad, -T, T):
            selfsym = max(selfsym, abs(M(mp.conj(b), c, y)))
    good = cross < mp.mpf("1e-15") and selfsym < mp.mpf("1e-15")
    print(f"  [{label}] N={N}: conj-pair cross-resid={float(cross):.1e} "
          f"self-conj({self_modes}) sym-resid={float(selfsym):.1e} "
          f"{'OK' if good else 'FAIL'}")
    return good


def main():
    print("=" * 74)
    print("C7 -- functional equation  conj M(conj b, c) = M(b, -c)")
    print("=" * 74)
    ok = True
    for x, lab in [([1, 2, 3], "N3 [1,2,3]"), ([1, 2, 3, 4], "N4 ramp"),
                   (list(1 + RNG.random(5) * 5), "N5 rand"), ([1, 2, 3, 4, 5, 6], "N6 ramp")]:
        ok = test_identity(x, lab) and ok
    print("  -- zero-set consequences:")
    for x, lab in [([1, 2, 3], "N3 [1,2,3]"), ([1, 2, 3, 4], "N4 ramp"),
                   ([1, 2, 3, 4, 5, 6], "N6 ramp")]:
        ok = test_conjugate_pairing(x, lab) and ok
    print("-" * 74)
    print("C7:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
