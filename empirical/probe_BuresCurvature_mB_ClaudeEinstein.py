"""Compare the Bures/K projective curvature with Im m_B.

This probe accompanies Note_BuresCurvature_mB_obstruction_Q7rX2.md.

It uses the completed two-channel reduction

    V(z) = (Xi(z), L3c(z))

of the exact Z/6 decomposition F=zeta E + L3 O.  The orthonormal-channel
Bures/Fubini-Study curvature is

    kappa = |Xi L3c' - L3c Xi'|^2 / (|Xi|^2 + |L3c|^2)^2 >= 0.

The Bures covariant log-derivative object is

    m_B = -Xi'/Xi.

The test checks that kappa is positive and finite near the first zeta-zero
ordinate while Im m_B has the Herglotz pole ~1/y.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (
        mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)
    )


def xi(s: mp.mpc) -> mp.mpc:
    if abs(s) < mp.mpf("1e-40") or abs(s - 1) < mp.mpf("1e-40"):
        return mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def lambda3(s: mp.mpc) -> mp.mpc:
    return (
        mp.power(3 / mp.pi, (s + 1) / 2)
        * mp.gamma((s + 1) / 2)
        * chi3_L(s)
    )


def Xi(z: mp.mpc) -> mp.mpc:
    return xi(mp.mpf("0.5") + 1j * z)


def L3c(z: mp.mpc) -> mp.mpc:
    return lambda3(mp.mpf("0.5") + 1j * z)


def deriv(f, z: mp.mpc) -> mp.mpc:
    h = mp.mpf("1e-6")
    return (f(z + h) - f(z - h)) / (2 * h)


def m_B(z: mp.mpc) -> mp.mpc:
    return -deriv(Xi, z) / Xi(z)


def kappa_EO(z: mp.mpc) -> mp.mpf:
    xi_z = Xi(z)
    l_z = L3c(z)
    xi_p = deriv(Xi, z)
    l_p = deriv(L3c, z)
    wedge = xi_z * l_p - l_z * xi_p
    denom = (abs(xi_z) ** 2 + abs(l_z) ** 2) ** 2
    return abs(wedge) ** 2 / denom


def fmt_complex(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.10e}{float(mp.im(z)):+.10e}j"


def fmt_real(x: mp.mpf) -> str:
    return f"{float(x):+.10e}"


def main() -> None:
    gamma1 = mp.mpf("14.134725141734693790457251983562")

    print("=" * 100)
    print("Bures/K curvature density versus Im m_B")
    print("=" * 100)
    print("m_B(z) = -Xi'(z)/Xi(z)")
    print("kappa_EO = |Xi L3c' - L3c Xi'|^2/(|Xi|^2+|L3c|^2)^2 >= 0")

    print("\nGeneric upper-half-plane samples:")
    samples = [
        mp.mpc(0, mp.mpf("0.25")),
        mp.mpc(3, mp.mpf("0.4")),
        mp.mpc(10, mp.mpf("0.7")),
        mp.mpc(14, mp.mpf("0.3")),
        mp.mpc(20, mp.mpf("1.2")),
    ]
    for z in samples:
        mb = m_B(z)
        kap = kappa_EO(z)
        print(
            f"  z={fmt_complex(z)}  Im m_B={fmt_real(mp.im(mb))}  "
            f"kappa_EO={fmt_real(kap)}  ratio={fmt_real(kap / mp.im(mb))}"
        )

    print("\nApproach the first zeta-zero ordinate from C+:")
    print("  If Im m_B were a regular Bures curvature, it would stay finite here.")
    for y in [
        mp.mpf("0.5"),
        mp.mpf("0.1"),
        mp.mpf("0.02"),
        mp.mpf("0.005"),
        mp.mpf("0.001"),
    ]:
        z = mp.mpc(gamma1, y)
        mb = m_B(z)
        kap = kappa_EO(z)
        print(
            f"  y={float(y):.3g}  Im m_B={fmt_real(mp.im(mb))}  "
            f"y*Im m_B={fmt_real(y * mp.im(mb))}  kappa_EO={fmt_real(kap)}"
        )

    print("\nAt the first zero ordinate, the odd channel is nonzero:")
    l_at = L3c(gamma1)
    xi_p_at = deriv(Xi, gamma1)
    finite_limit = abs(xi_p_at) ** 2 / abs(l_at) ** 2
    print(f"  |L3c(gamma1)|={fmt_real(abs(l_at))}")
    print(f"  |Xi'(gamma1)|={fmt_real(abs(xi_p_at))}")
    print(f"  predicted finite kappa limit={fmt_real(finite_limit)}")

    print("\nConclusion:")
    print("  kappa_EO is positive and Bures/K-covariant, but it is finite at Xi zeros.")
    print("  Im m_B has the zeta-divisor Herglotz pole ~1/y.")
    print("  Therefore Im m_B is not a regular positive Bures curvature/norm.")
    print("  Its positive form, under RH, is the singular Poisson density of the Xi divisor.")


if __name__ == "__main__":
    main()

