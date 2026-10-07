"""Probe CM Poisson Monotonicity and the direct finite-geometry no-go.

This script illustrates the theorem in
Note_CMPoissonMonotonicity_DirectNoGo_W8rN5.md:

1. K-real, even fake transfers with off-boundary zeros obey the same formal
   divisor symmetries but violate Poisson monotonicity.
2. The same fake transfers violate Pick positivity and Hermite-Biehler
   positivity.
3. The completed zeta Xi is sampled only as a sanity check, not as proof.
"""

import cmath
import math

import mpmath as mp
import numpy as np

mp.mp.dps = 50


def fake_X(z, gamma=14.134725141734693, beta=0.6):
    return ((z - gamma) ** 2 + beta**2) * ((z + gamma) ** 2 + beta**2)


def fake_log_derivative(z, gamma=14.134725141734693, beta=0.6):
    """Return X'(z)/X(z) for the fake even off-boundary transfer."""

    return (
        2 * (z - gamma) / ((z - gamma) ** 2 + beta**2)
        + 2 * (z + gamma) / ((z + gamma) ** 2 + beta**2)
    )


def fake_m(z, gamma=14.134725141734693, beta=0.6):
    return -fake_log_derivative(z, gamma=gamma, beta=beta)


def pick_matrix(mfun, points):
    n = len(points)
    out = np.zeros((n, n), dtype=np.complex128)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            out[i, j] = (mfun(z) - np.conjugate(mfun(w))) / (z - np.conjugate(w))
    return out


def hb_gap_for_real_entire(log_derivative, value, z):
    """Return |E|^2-|E#|^2 for E=X+iX', using X and X'/X."""

    x_val = value(z)
    q = log_derivative(z)
    e_val = x_val * (1 + 1j * q)
    e_sharp = x_val * (1 - 1j * q)
    return abs(e_val) ** 2 - abs(e_sharp) ** 2


def xi(z):
    s = mp.mpf("0.5") + 1j * z
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_m(z):
    z_mp = mp.mpc(z.real, z.imag)
    return -mp.diff(xi, z_mp) / xi(z_mp)


def main():
    gamma = 14.134725141734693
    beta = 0.6
    ys = [0.1, 0.3, 0.55, 0.59]

    print("Fake K-real even transfer X_{gamma,beta}")
    print(f"gamma={gamma:.12f}, beta={beta:.3f}")
    print("y, d_y log|X(gamma+i y)| = Im(-X'/X)")
    for y in ys:
        z = gamma + 1j * y
        print(f"{y:6.3f}  {fake_m(z, gamma, beta).imag: .12e}")

    hb_z = gamma + 0.59j
    hb_gap = hb_gap_for_real_entire(
        lambda zz: fake_log_derivative(zz, gamma, beta),
        lambda zz: fake_X(zz, gamma, beta),
        hb_z,
    )
    print()
    print("Hermite-Biehler gap |E|^2-|E#|^2 at fake point")
    print(f"z={hb_z}, gap={hb_gap:.12e}")

    points = [
        gamma + 0.50j,
        gamma + 0.56j,
        gamma + 0.59j,
        gamma + 0.40j,
    ]
    pmat = pick_matrix(lambda zz: fake_m(zz, gamma, beta), points)
    eigs = np.linalg.eigvalsh((pmat + pmat.conj().T) / 2)
    print()
    print("Fake Pick matrix eigenvalues")
    print(np.array2string(eigs, precision=8, suppress_small=False))

    print()
    print("Sample Xi monotonicity sanity check (not a proof)")
    xi_points = [
        14.134725141734693 + 0.20j,
        21.022039638771554 + 0.20j,
        25.010857580145688 + 0.30j,
    ]
    for z in xi_points:
        val = xi_m(z)
        print(f"z={z.real:.6f}+{z.imag:.2f}i  Im m_B={float(mp.im(val)):.12e}")


if __name__ == "__main__":
    main()
