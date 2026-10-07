"""
Native Simplicial Investigation, Script 02:
Compute the apex generator M_x(beta, c) at N=6 for each character c,
and locate its complex zeros in beta.

The apex generator (T0 Def 3.1):
    M_x(beta, c) = (1/N) sum_{s=0}^{N-1} exp(beta * y_s) * conj(chi_c(s))
                 = (1/6) sum_{s=0}^{5} exp(beta * y_s) * exp(-2 pi i c s / 6)

For fixed c and fixed (real) y, this is an entire function of complex beta,
a finite linear combination of 6 exponentials exp(beta * y_s).

Zeros of M_x(., c) in complex beta are the Lee-Yang points of mode c.

The natural ANSATZ for a "distinguished line" in beta could be:
  - the real line (no purely real zeros if M positive; but complex/imaginary zeros)
  - the imaginary axis (Re beta = 0)
  - a vertical line Re beta = const (analog of critical line)
  - a horizontal band

We use mpmath's mp.findroot with a grid of seeds in a rectangle around 0.
Because the function is exponential-polynomial it has infinitely many zeros
extending to infinity in particular directions; we focus on |beta| <= R for
some R (R = 5, 10, 20 chosen).
"""

import mpmath as mp
from native_simplicial_01_ledger import primorial_ledger, center

mp.mp.dps = 40


def apex(beta, c, y, N=6):
    """Structured apex generator M_x(beta, c)."""
    beta = mp.mpc(beta)
    s_val = mp.mpc(0)
    for s in range(N):
        chi_bar = mp.exp(-2j * mp.pi * c * s / N)
        s_val += mp.exp(beta * y[s]) * chi_bar
    return s_val / N


def find_zeros_in_rectangle(c, y, x_range, y_range, grid_x=40, grid_y=40,
                             tol=1e-25, dedup_tol=1e-6, N=6):
    """
    Find zeros of M_x(., c) in the rectangle [x_min, x_max] x [y_min, y_max]
    of the complex beta-plane, by seeded Newton iteration from a grid.
    Returns a deduplicated list of zeros.
    """
    x_min, x_max = x_range
    y_min, y_max = y_range
    zeros = []

    def f(beta):
        return apex(beta, c, y, N=N)

    for i in range(grid_x):
        for j in range(grid_y):
            x0 = x_min + (x_max - x_min) * i / (grid_x - 1)
            y0 = y_min + (y_max - y_min) * j / (grid_y - 1)
            seed = mp.mpc(x0, y0)
            try:
                z = mp.findroot(f, seed, solver='muller', tol=tol, maxsteps=80)
            except Exception:
                continue
            # check in box, check unique
            if not (x_min - 0.5 <= float(z.real) <= x_max + 0.5):
                continue
            if not (y_min - 0.5 <= float(z.imag) <= y_max + 0.5):
                continue
            # validate
            if abs(f(z)) > 1e-15:
                continue
            is_new = True
            for w in zeros:
                if abs(z - w) < dedup_tol:
                    is_new = False
                    break
            if is_new:
                zeros.append(z)
    return sorted(zeros, key=lambda z: (float(z.real), float(z.imag)))


def main():
    cutoff = 1000
    print("=" * 75)
    print(f"Apex generator zeros at N=6, primorial prime-power ledger, cutoff={cutoff}")
    print("=" * 75)

    y_raw = primorial_ledger(cutoff, variant="prime_power")
    y = center(y_raw)
    print("centered ledger y:")
    for s in range(6):
        print(f"   y[{s}] = {mp.nstr(y[s], 20)}")
    print()

    # First: c=0 case (this is e^{K_y(beta)} which has NO zeros, M = exp(...)) -
    # but actually M_x(beta, 0) = (1/N) sum e^{beta y_s} = Z_y(beta), the partition
    # function, which is positive for real beta but may have complex zeros.
    # Let's check.
    print("Mode c=0 (unstructured apex Z_y = (1/6) sum exp(beta y_s)):")
    print("  This is the partition function, with Lee-Yang zeros in complex beta.")
    print("  M_x(beta, 0) = e^{K_y(beta)} only as composition; the function itself")
    print("  HAS zeros (the Lee-Yang singularities of K_y).")
    print()

    from math import gcd as _gcd
    for c in range(6):
        cond = 1 if c == 0 else 6 // _gcd(c, 6)
        print(f"--- Character mode c = {c} (conductor {cond}) ---")
        zeros = find_zeros_in_rectangle(
            c, y, x_range=(-3, 3), y_range=(-3, 3),
            grid_x=24, grid_y=24, N=6
        )
        print(f"  found {len(zeros)} zeros in [-3,3] x [-3,3]:")
        for z in zeros:
            print(f"    beta = {mp.nstr(z.real, 12):>20} + {mp.nstr(z.imag, 12):>20} i"
                  f"  |M(beta,c)| = {mp.nstr(abs(apex(z, c, y)), 4)}")
        print()


if __name__ == "__main__":
    main()
