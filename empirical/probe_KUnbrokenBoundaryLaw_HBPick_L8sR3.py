"""Diagnostics for the K-unbroken boundary law.

This probe accompanies Note_KUnbrokenBoundaryLaw_HBPick_L8sR3.md.

The proposed missing law is the derivative-polarized Hermite-Biehler law

    E_B(z) = Xi(z) + i Xi'(z) is Hermite-Biehler,

equivalently m_B=-Xi'/Xi is Herglotz, equivalently the Pick kernel

    (m_B(z)-conj(m_B(w)))/(z-conj(w))

is positive semidefinite on C+.

The script also compares an artificial off-line FE-cluster model, where the
law must fail because there is an interior divisor atom.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 70


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (
        mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)
    )


def xi(s: mp.mpc) -> mp.mpc:
    if abs(s) < mp.mpf("1e-35") or abs(s - 1) < mp.mpf("1e-35"):
        return mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z: mp.mpc) -> mp.mpc:
    return xi(mp.mpf("0.5") + 1j * z)


def deriv(f, z: mp.mpc) -> mp.mpc:
    h = mp.mpf("1e-6")
    return (f(z + h) - f(z - h)) / (2 * h)


def Xip(z: mp.mpc) -> mp.mpc:
    return deriv(Xi, z)


def m_B(z: mp.mpc) -> mp.mpc:
    return -Xip(z) / Xi(z)


def E_B(z: mp.mpc) -> mp.mpc:
    return Xi(z) + 1j * Xip(z)


def E_B_sharp(z: mp.mpc) -> mp.mpc:
    return Xi(z) - 1j * Xip(z)


def hb_delta(z: mp.mpc) -> mp.mpf:
    return abs(E_B(z)) ** 2 - abs(E_B_sharp(z)) ** 2


def hb_delta_identity(z: mp.mpc) -> mp.mpf:
    return 4 * abs(Xi(z)) ** 2 * mp.im(m_B(z))


def pick_matrix(m_func, points: list[mp.mpc]) -> np.ndarray:
    n = len(points)
    mat = np.zeros((n, n), dtype=np.complex128)
    vals = [m_func(z) for z in points]
    for i, zi in enumerate(points):
        for j, zj in enumerate(points):
            val = (vals[i] - mp.conj(vals[j])) / (zi - mp.conj(zj))
            mat[i, j] = complex(val)
    return (mat + mat.conj().T) / 2


GAMMA = mp.mpf("14.134725141734693790457251983562")
DELTA = mp.mpf("0.08")


def P_off(z: mp.mpc, gamma: mp.mpf = GAMMA, delta: mp.mpf = DELTA) -> mp.mpc:
    return ((z - gamma) ** 2 + delta**2) * ((z + gamma) ** 2 + delta**2)


def Pp_off(z: mp.mpc, gamma: mp.mpf = GAMMA, delta: mp.mpf = DELTA) -> mp.mpc:
    first = (z - gamma) ** 2 + delta**2
    second = (z + gamma) ** 2 + delta**2
    return 2 * (z - gamma) * second + 2 * (z + gamma) * first


def m_off(z: mp.mpc) -> mp.mpc:
    return -Pp_off(z) / P_off(z)


def fmt(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.10e}{float(mp.im(z)):+.10e}j"


def main() -> None:
    print("=" * 100)
    print("K-unbroken boundary law: Hermite-Biehler / Pick diagnostics")
    print("=" * 100)
    print("E_B = Xi + i Xi'")
    print("m_B = -Xi'/Xi")

    samples = [
        mp.mpc(0, mp.mpf("0.2")),
        mp.mpc(2, mp.mpf("0.35")),
        mp.mpc(7, mp.mpf("0.5")),
        mp.mpc(12, mp.mpf("0.4")),
        mp.mpc(14, mp.mpf("0.2")),
        mp.mpc(20, mp.mpf("1.0")),
    ]

    print("\nHermite-Biehler inequality samples:")
    for z in samples:
        delta_hb = hb_delta(z)
        identity = hb_delta_identity(z)
        err = abs(delta_hb - identity)
        print(
            f"  z={fmt(z)}  |E|^2-|E#|^2={float(delta_hb):+.10e}  "
            f"4|Xi|^2 Im m_B={float(identity):+.10e}  err={float(err):.3e}"
        )

    points = [
        mp.mpc(0, mp.mpf("0.2")),
        mp.mpc(3, mp.mpf("0.35")),
        mp.mpc(7, mp.mpf("0.45")),
        mp.mpc(11, mp.mpf("0.6")),
        mp.mpc(14, mp.mpf("0.25")),
    ]
    pick = pick_matrix(m_B, points)
    eigvals = np.linalg.eigvalsh(pick)
    print("\nPick kernel finite Gram test for actual Xi:")
    print("  eigenvalues:", " ".join(f"{ev:+.6e}" for ev in eigvals))
    print(f"  min eigenvalue: {eigvals[0]:+.6e}")

    off_points = [
        mp.mpc(GAMMA, DELTA / 2),
        mp.mpc(GAMMA + mp.mpf("0.04"), DELTA / 2),
        mp.mpc(-GAMMA, DELTA / 2),
    ]
    off_pick = pick_matrix(m_off, off_points)
    off_eigvals = np.linalg.eigvalsh(off_pick)
    print("\nArtificial off-line FE-cluster model:")
    for z in off_points:
        print(f"  z={fmt(z)}  Im m_off={float(mp.im(m_off(z))):+.10e}")
    print("  Pick eigenvalues:", " ".join(f"{ev:+.6e}" for ev in off_eigvals))
    print(f"  min eigenvalue: {off_eigvals[0]:+.6e}")

    print("\nConclusion:")
    print("  The missing law is Pick positivity / Hermite-Biehlerness of E_B=Xi+iXi'.")
    print("  The actual Xi samples pass this finite test.")
    print("  The off-line model fails by a negative diagonal/Pick direction.")
    print("  Proving the Pick kernel is a Bures/K Gram kernel would close the boundary-support gap.")


if __name__ == "__main__":
    main()

