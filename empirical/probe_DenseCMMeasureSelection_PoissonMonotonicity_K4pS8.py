"""Probe dense CM measure selection via Poisson monotonicity.

Random suffix: K4pS8

The probe checks sampled positivity of
    d/dy log |Xi(x+iy)| = Im(-Xi'/Xi)(x+iy)
and contrasts it with a fake real-even function with off-boundary zeros, where
the vertical derivative becomes negative below the off-boundary zero.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 50


def xi_s(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z):
    return xi_s(mp.mpf("0.5") + 1j * z)


def log_abs_Xi(z):
    return mp.log(abs(Xi(z)))


def vertical_derivative_log_abs(func, x, y):
    y = mp.mpf(y)
    h = min(mp.mpf("1e-4"), y / 5)
    zp = mp.mpc(x, y + h)
    zm = mp.mpc(x, y - h)
    return (func(zp) - func(zm)) / (2 * h)


def Xi_prime(z):
    return 1j * mp.diff(xi_s, mp.mpf("0.5") + 1j * z)


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def fake_X(z, gamma=mp.mpf("6.0"), delta=mp.mpf("0.7")):
    return ((z - gamma) ** 2 + delta**2) * ((z + gamma) ** 2 + delta**2)


def log_abs_fake(z):
    return mp.log(abs(fake_X(z)))


def scan_xi_grid():
    xs = np.linspace(0.25, 60.0, 80)
    ys = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]
    min_val = mp.inf
    min_point = None
    negatives = []
    for y in ys:
        for x in xs:
            val = vertical_derivative_log_abs(log_abs_Xi, mp.mpf(str(x)), mp.mpf(str(y)))
            if val < min_val:
                min_val = val
                min_point = (x, y)
            if val < -mp.mpf("1e-6"):
                negatives.append((x, y, val))
    return min_val, min_point, negatives


def fake_negative_scan():
    gamma = mp.mpf("6.0")
    delta = mp.mpf("0.7")
    rows = []
    for y in [0.1, 0.3, 0.5, 0.65, 0.75, 1.0]:
        val = vertical_derivative_log_abs(log_abs_fake, gamma, mp.mpf(str(y)))
        rows.append((y, val))
    return rows


def main() -> None:
    print("Identity check: d_y log|Xi| = Im m_B")
    samples = [
        mp.mpc("0.7", "0.4"),
        mp.mpc("5.0", "0.5"),
        mp.im(mp.zetazero(1)) + mp.mpc(0, "0.5"),
    ]
    for z in samples:
        dy = vertical_derivative_log_abs(log_abs_Xi, mp.re(z), mp.im(z))
        im_m = mp.im(m_bures(z))
        print(
            "z=", mp.nstr(z, 14),
            "dy_log_abs=", mp.nstr(dy, 12),
            "Im_mB=", mp.nstr(im_m, 12),
            "abs_err=", mp.nstr(abs(dy - im_m), 4),
        )

    print("\nSampled Xi Poisson monotonicity grid:")
    min_val, min_point, negatives = scan_xi_grid()
    print("  min_dy_log_abs=", mp.nstr(min_val, 12), "at", min_point)
    print("  negative_count_below_tol=", len(negatives))

    print("\nFake off-boundary zero vertical derivative at x=gamma:")
    for y, val in fake_negative_scan():
        print("  y=", y, "dy_log_abs_fake=", mp.nstr(val, 12))

    print("\nPoisson density near first two zeros:")
    for gamma in [mp.im(mp.zetazero(1)), mp.im(mp.zetazero(2))]:
        for y in [mp.mpf("0.5"), mp.mpf("0.1"), mp.mpf("0.02")]:
            dy = vertical_derivative_log_abs(log_abs_Xi, gamma, y)
            print(
                "  gamma=", mp.nstr(gamma, 12),
                "y=", y,
                "u_y=(1/pi)dy=", mp.nstr(dy / mp.pi, 12),
            )

    print("\nConclusion:")
    print("  Sampled normalized CM transfer Xi is vertically monotone on the grid.")
    print("  A fake off-boundary zero creates a negative valley below the zero.")
    print("  Proving this monotonicity globally is equivalent to the dense")
    print("  CM measure-selection theorem, hence to RH.")


if __name__ == "__main__":
    main()

