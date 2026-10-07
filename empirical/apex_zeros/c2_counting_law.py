"""
C2 -- Counting law (spine T3).

Claim: n_c(T) := #{zeros with |Im beta| <= T} = (Delta_y / pi) * T + O(1),
       with slope INDEPENDENT of the character c (Delta_y = max y - min y).
This is the apex analog of Riemann--von Mangoldt -- but with CONSTANT density
(linear n(T)), versus zeta's log-growing density. The contrast localizes the
archimedean place (see C8 / the bridge conjecture).

Counts via the argument principle only (no root polishing) -> fast, large T.
"""

import numpy as np
import mpmath as mp
from apex_core import centered_log_ledger, spread, strip_bound, count_zeros_rect_fast

RNG = np.random.default_rng(1)
TS = [mp.mpf(t) for t in ("40.13", "80.13", "160.13", "320.13")]


def min_gap(y):
    rs = sorted(float(mp.re(v)) for v in y)
    return min(b - a for a, b in zip(rs, rs[1:]))


def count_at(c, y, T):
    Rm, Rp = strip_bound(y, len(y))
    pad = mp.mpf("0.6")
    n = count_zeros_rect_fast(c, y, -(Rm + pad), Rp + pad, -T, T)
    ni = int(mp.nint(mp.re(n)))
    clean = abs(mp.re(n) - ni) < 0.05 and abs(mp.im(n)) < 0.05
    return ni, clean


def slope_report(x, label, all_c=False):
    y = centered_log_ledger(x)
    N = len(y)
    Dy = spread(y)
    pred = float(Dy / mp.pi)               # predicted slope
    Tf = [float(T) for T in TS]
    cs = range(N) if all_c else [0]
    ok = True
    for c in cs:
        counts, clean_all = [], True
        for T in TS:
            ni, clean = count_at(c, y, T)
            counts.append(ni)
            clean_all = clean_all and clean
        # regression slope (intercept absorbs the O(1)); and bounded residuals
        slope, intercept = np.polyfit(Tf, counts, 1)
        resid = [counts[i] - pred * Tf[i] for i in range(len(Tf))]   # n(T) - (Dy/pi)T
        ratio = slope / pred
        bounded = max(abs(r) for r in resid) < 3.0          # O(1), not growing
        nongrow = abs(resid[-1]) <= abs(resid[0]) + 2.0
        good = clean_all and abs(ratio - 1) < 0.015 and bounded and nongrow
        ok = ok and good
        cc = f"c={c}" if all_c else "c=0"
        print(f"  [{label}] N={N} Dy={float(Dy):.4f} {cc}: counts={counts} "
              f"fit_slope={slope:.4f} pred={pred:.4f} ratio={ratio:.4f} "
              f"resid=[{', '.join(f'{r:+.2f}' for r in resid)}] {'OK' if good else 'FAIL'}")
    return ok


def rand_ledger(N, min_g=0.25):
    while True:
        x = list(1 + RNG.random(N) * 6)
        if min_gap(centered_log_ledger(x)) >= min_g:
            return x


def main():
    print("=" * 74)
    print("C2 -- Counting law  n(T) ~ (Delta_y/pi) T   (slope c-independent)")
    print("=" * 74)
    ok = True
    # geometric ledger: zeros exactly on Re=0, density still Delta_y/pi
    ok = slope_report([2 ** s for s in range(5)], "N5 geom (on-line)") and ok
    ok = slope_report([1, 2, 3, 4], "N4 ramp") and ok
    ok = slope_report(rand_ledger(5), "N5 rand") and ok
    ok = slope_report([1, 2, 3, 4, 5, 6], "N6 ramp") and ok
    print("  -- c-independence of the slope (one ledger, all characters):")
    ok = slope_report([1, 2, 3, 4, 5], "N5 ramp", all_c=True) and ok
    print("-" * 74)
    print("C2:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
