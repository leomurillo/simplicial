"""Numerical probe for the Poisson-window bridge.

The point is not to prove RH numerically.  It illustrates the local theorem:
if vertical Poisson monotonicity fails at a point, a positive narrow window
detects the failure.
"""

import math

import mpmath as mp
import numpy as np

mp.mp.dps = 50


def fake_m(z, gamma=14.134725141734693, beta=0.6):
    """m=-X'/X for X=((z-gamma)^2+beta^2)((z+gamma)^2+beta^2)."""

    return -(
        2 * (z - gamma) / ((z - gamma) ** 2 + beta**2)
        + 2 * (z + gamma) / ((z + gamma) ** 2 + beta**2)
    )


def boundary_m(z, gamma=14.134725141734693):
    """m=-X'/X for a real-boundary pair X=(z-gamma)(z+gamma)."""

    return -(1 / (z - gamma) + 1 / (z + gamma))


def gaussian_window(x, x0, sigma):
    return math.exp(-0.5 * ((x - x0) / sigma) ** 2)


def window_functional(mfun, x0, y, sigma, half_width=6.0, n=5001):
    xs = np.linspace(x0 - half_width * sigma, x0 + half_width * sigma, n)
    vals = []
    weights = []
    for x in xs:
        w = gaussian_window(float(x), x0, sigma)
        vals.append(w * mfun(complex(float(x), y)).imag)
        weights.append(w)
    integral = np.trapezoid(vals, xs)
    mass = np.trapezoid(weights, xs)
    return integral, integral / mass


def xi(z):
    s = mp.mpf("0.5") + 1j * z
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_m(z):
    z_mp = mp.mpc(z.real, z.imag)
    return -mp.diff(xi, z_mp) / xi(z_mp)


def xi_window(x0, y, sigma, half_width=4.0, n=101):
    xs = np.linspace(x0 - half_width * sigma, x0 + half_width * sigma, n)
    vals = []
    weights = []
    for x in xs:
        w = gaussian_window(float(x), x0, sigma)
        vals.append(w * float(mp.im(xi_m(complex(float(x), y)))))
        weights.append(w)
    integral = np.trapezoid(vals, xs)
    mass = np.trapezoid(weights, xs)
    return integral, integral / mass


def main():
    gamma = 14.134725141734693
    beta = 0.6

    print("Poisson-window detection probe")
    print(f"gamma={gamma:.12f}, beta={beta:.3f}")

    cases = [
        ("fake-offline", lambda z: fake_m(z, gamma=gamma, beta=beta), gamma, 0.58, 0.02),
        ("fake-offline wider", lambda z: fake_m(z, gamma=gamma, beta=beta), gamma, 0.55, 0.08),
        ("real-boundary", lambda z: boundary_m(z, gamma=gamma), gamma, 0.20, 0.08),
        ("real-boundary off-center", lambda z: boundary_m(z, gamma=gamma), gamma + 0.30, 0.20, 0.12),
    ]

    print()
    print("model, x0, y, sigma, window integral, normalized average")
    for name, mfun, x0, y, sigma in cases:
        integ, avg = window_functional(mfun, x0, y, sigma)
        print(f"{name:20s} {x0:10.6f} {y:6.3f} {sigma:7.3f} {integ: .12e} {avg: .12e}")

    print()
    print("Xi sanity windows near first two zeros (not a proof)")
    for x0, y, sigma in [(gamma, 0.20, 0.05), (21.022039638771554, 0.20, 0.05)]:
        integ, avg = xi_window(x0, y, sigma)
        print(f"Xi x0={x0:.6f} y={y:.2f} sigma={sigma:.3f}: {integ:.12e}, avg={avg:.12e}")


if __name__ == "__main__":
    main()
