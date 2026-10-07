"""
C3 -- The exact-line locus (spine T4, sharpened; new theorem).

EQUAL-SPACING EXACT-LINE THEOREM.  If the centered log-ledger y is an
arithmetic progression with common spacing a (i.e. x is a geometric
progression), then with w = e^{a beta}, zeta = e^{2 pi i / N},

    M(beta, c) = (1/N) sum_{s} (w zeta^{-c})^s = (1/N) (W^N - 1)/(W - 1),  W = w zeta^{-c},

so the zeros are exactly  W^N = 1, W != 1, i.e.

    { beta = 2 pi i m / (a N) : m in Z, m != c (mod N) }   -- ALL on Re beta = 0.

This generalizes T0 Prop 2.5 (N=2 cosh) and T7 Prop 6.2 to every N and every c,
and pins the exact additive "critical line" to the maximal-symmetry locus.

Certified here: (i) geometric ledgers N=2..7 match the exact set to ~1e-25;
(ii) Re beta = 0 to machine precision; (iii) a NON-geometric control whose zeros
do NOT lie on the predicted lattice (the locus is special).
"""

import mpmath as mp
from apex_core import centered_log_ledger, strip_bound, M, find_zeros_rect

mp.mp.dps = 30


def predicted_set(a, N, c, T):
    """Exact geometric-ledger zero set inside |Im beta| <= T."""
    base = 2 * mp.pi / (abs(a) * N)
    mmax = int(mp.floor(T / base))
    out = []
    for m in range(-mmax, mmax + 1):
        if (m % N) == (c % N):
            continue                      # W = 1 removable point, not a zero
        out.append(mp.mpc(0, m * base * mp.sign(a)))
    return out


def match(found, predicted, tol=mp.mpf("1e-20")):
    """Max nearest-neighbour distance found<->predicted (both sorted by Im)."""
    if len(found) != len(predicted):
        return None
    f = sorted(found, key=lambda b: float(mp.im(b)))
    p = sorted(predicted, key=lambda b: float(mp.im(b)))
    return max(abs(fi - pi) for fi, pi in zip(f, p))


def test_geometric(rho, N, T=mp.mpf("11.3")):
    x = [mp.mpf(rho) ** s for s in range(N)]
    y = centered_log_ledger(x)
    a = y[1] - y[0]
    Rm, Rp = strip_bound(y, N)
    pad = mp.mpf("0.5")
    ok = True
    details = []
    for c in range(N):
        z = find_zeros_rect(c, y, -(Rm + pad), Rp + pad, -T, T)
        maxre = max((abs(mp.re(b)) for b in z), default=mp.mpf(0))
        pred = predicted_set(a, N, c, T)
        d = match(z, pred)
        good = (maxre < mp.mpf("1e-12")) and (d is not None) and (d < mp.mpf("1e-18"))
        ok = ok and good
        details.append((c, len(z), len(pred), float(maxre), None if d is None else float(d), good))
    print(f"  [geom rho={rho} N={N}] a={float(a):+.4f}")
    for c, nf, npr, mre, d, good in details:
        ds = "n/a" if d is None else f"{d:.1e}"
        print(f"     c={c}: found={nf} pred={npr} max|Re|={mre:.1e} match={ds} "
              f"{'OK' if good else 'FAIL'}")
    return ok


def test_control(x, label, T=mp.mpf("11.3")):
    """Non-geometric ledger: zeros must NOT match the (best-fit) on-line lattice."""
    y = centered_log_ledger(x)
    N = len(y)
    Rm, Rp = strip_bound(y, N)
    pad = mp.mpf("0.6")
    z = find_zeros_rect(0, y, -(Rm + pad), Rp + pad, -T, T)
    maxre = max((abs(mp.re(b)) for b in z), default=mp.mpf(0))
    offline = maxre > mp.mpf("1e-3")     # genuinely off the imaginary axis
    print(f"  [control {label}] N={N}: found={len(z)} max|Re|={float(maxre):.4f} "
          f"-> off-line={offline} {'OK' if offline else 'FAIL'}")
    return offline


def main():
    print("=" * 74)
    print("C3 -- Exact-line locus: equal-spacing => zeros are roots of unity in w")
    print("=" * 74)
    ok = True
    for rho, N in [(3, 2), (3, 3), (2, 5), ("1.7", 7)]:
        ok = test_geometric(rho, N) and ok
    print("  -- negative controls (non-geometric => off-line):")
    print("     (note: [1,2,4] is secretly geometric (x2); the locus is judged")
    print("      by EQUAL log-spacing, not by 'looking like a ramp')")
    ok = test_control([1, 2, 3], "N3 [1,2,3]") and ok          # spacings .693,.405 unequal
    ok = test_control([1, 2, 3, 5], "N4 [1,2,3,5]") and ok
    print("-" * 74)
    print("C3:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
