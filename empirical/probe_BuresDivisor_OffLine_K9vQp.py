"""Local model for the off-line-zero Bures divisor-current contradiction.

This script accompanies Note_BuresDivisor_OffLineContradiction_K9vQp.md.

It does not assume real off-line zeta zeros exist.  It models the forced
functional-equation cluster in the spectral z-plane:

    gamma +/- i delta, -gamma +/- i delta.

For the local model

    P_delta(z)=((z-gamma)^2+delta^2)((z+gamma)^2+delta^2),
    m_delta(z)=-P_delta'(z)/P_delta(z),

the Bures divisor current is

    D_delta = -(1/pi) dbar m_delta = sum_{P_delta(a)=0} delta_a.

A Cauchy test around an upper-half-plane atom returns mass 1.  A boundary
support law would return mass 0 for every disk compactly inside C+, so this is
the precise contradiction.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 50


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


def P_on(z: mp.mpc, gamma: mp.mpf = GAMMA) -> mp.mpc:
    return z**2 - gamma**2


def Pp_on(z: mp.mpc, gamma: mp.mpf = GAMMA) -> mp.mpc:
    return 2 * z


def m_on(z: mp.mpc) -> mp.mpc:
    return -Pp_on(z) / P_on(z)


def cauchy_divisor_mass(m_func, center: mp.mpc, radius: mp.mpf) -> mp.mpc:
    def integrand(t: mp.mpf) -> mp.mpc:
        z = center + radius * mp.e ** (1j * t)
        dz = 1j * radius * mp.e ** (1j * t)
        return m_func(z) * dz

    integral = mp.quad(integrand, [0, 2 * mp.pi])
    return -integral / (2 * mp.pi * 1j)


def fmt(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.12e}{float(mp.im(z)):+.12e}j"


def main() -> None:
    upper_atom = mp.mpc(GAMMA, DELTA)
    lower_atom = mp.mpc(GAMMA, -DELTA)
    upper_atom_neg = mp.mpc(-GAMMA, DELTA)
    lower_atom_neg = mp.mpc(-GAMMA, -DELTA)
    radius = DELTA / 3
    empty_center = mp.mpc(0, DELTA)

    print("=" * 100)
    print("Off-line FE cluster as Bures divisor current")
    print("=" * 100)
    print(f"gamma={GAMMA}")
    print(f"delta={DELTA}")
    print("\nSpectral cluster atoms:")
    for atom in [upper_atom, lower_atom, upper_atom_neg, lower_atom_neg]:
        half = "C+" if mp.im(atom) > 0 else "C-"
        print(f"  {fmt(atom)}  {half}")

    print("\nCauchy divisor-current tests:")
    mass_upper = cauchy_divisor_mass(m_off, upper_atom, radius)
    mass_lower = cauchy_divisor_mass(m_off, lower_atom, radius)
    mass_empty = cauchy_divisor_mass(m_off, empty_center, radius)
    mass_on_empty = cauchy_divisor_mass(m_on, empty_center, radius)
    print(f"  off-line disk around gamma+i delta: mass={fmt(mass_upper)}")
    print(f"  off-line disk around gamma-i delta: mass={fmt(mass_lower)}")
    print(f"  off-line empty disk inside C+:     mass={fmt(mass_empty)}")
    print(f"  on-line model disk inside C+:      mass={fmt(mass_on_empty)}")

    print("\nBoundary-support contradiction:")
    print("  Boundary-support law says every compact disk inside C+ has mass 0.")
    print("  Off-line FE cluster gives mass 1 in a disk around gamma+i delta.")
    print("  Therefore boundary support excludes off-line zeros.")

    print("\nK-covariance check:")
    print("  The pair gamma+i delta and gamma-i delta is K-symmetric.")
    print("  So K-covariance alone allows the pair; boundary support is the missing law.")


if __name__ == "__main__":
    main()

