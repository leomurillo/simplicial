"""Test E_B(z) = Xi(z) + i*Xi'(z) as the derivative-polarized de Branges associate.

Per the Notes (Z3hP9, R6mT4, L8sR3), the correct de Branges E-function for the
Riemann xi function is NOT the cross-channel E = Xi - i*L3c (which fails by
parity, per Addendum D.9) but the derivative-polarized

    E_B(z) := Xi(z) + i*Xi'(z).

The identity

    |E_B|^2 - |E_B^#|^2 = 4 |Xi|^2 * Im(m_B(z)) = 4 |Xi|^2 * Im(-Xi'/Xi)

is unconditional.  The Hermite-Biehler condition |E_B| > |E_B^#| on C+ is
equivalent to Im(m_B) > 0 on C+ which is equivalent to RH.  So a successful
empirical sign test does NOT prove RH (RH is numerically verified to enormous
height) but it confirms the algebraic identity and the candidate's structure.

This probe verifies:
  1. The unconditional identity |E_B|^2 - |E_B^#|^2 = 4|Xi|^2 Im m_B.
  2. The Hermite-Biehler sign on a grid in C+.
  3. The behavior near a known zero gamma_1.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 50


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (
        mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)
    )


def xi(s: mp.mpc) -> mp.mpc:
    if abs(s) < mp.mpf("1e-30") or abs(s - 1) < mp.mpf("1e-30"):
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


def Xi_prime(z: mp.mpc) -> mp.mpc:
    return deriv(Xi, z)


def E_B(z: mp.mpc) -> mp.mpc:
    return Xi(z) + 1j * Xi_prime(z)


def E_B_sharp(z: mp.mpc) -> mp.mpc:
    return Xi(z) - 1j * Xi_prime(z)


def m_B(z: mp.mpc) -> mp.mpc:
    return -Xi_prime(z) / Xi(z)


def magnitude_diff(z: mp.mpc) -> mp.mpf:
    return abs(E_B(z)) ** 2 - abs(E_B_sharp(z)) ** 2


def identity_check(z: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
    """Return (LHS, RHS) of |E_B|^2 - |E_B^#|^2 = 4 |Xi|^2 Im m_B."""
    lhs = magnitude_diff(z)
    rhs = 4 * abs(Xi(z)) ** 2 * mp.im(m_B(z))
    return lhs, rhs


def main() -> None:
    print("=" * 100)
    print("Derivative-polarized de Branges associate: E_B(z) = Xi(z) + i*Xi'(z)")
    print("=" * 100)
    print("Hermite-Biehler condition: |E_B|^2 - |E_B^#|^2 > 0 on C+")
    print("Algebraic identity (unconditional):")
    print("   |E_B|^2 - |E_B^#|^2 = 4 |Xi(z)|^2 * Im m_B(z)")
    print()

    # 1. Identity check
    print("Unconditional identity check (LHS = RHS):")
    samples = [
        mp.mpc(0, mp.mpf("0.5")),
        mp.mpc(3, mp.mpf("0.7")),
        mp.mpc(10, mp.mpf("0.5")),
        mp.mpc(14, mp.mpf("0.3")),
        mp.mpc(-5, mp.mpf("0.4")),
        mp.mpc(20, mp.mpf("1.0")),
    ]
    for z in samples:
        lhs, rhs = identity_check(z)
        err = abs(lhs - rhs)
        print(
            f"  z={float(mp.re(z)):+8.3f}{float(mp.im(z)):+6.3f}i  "
            f"LHS={float(lhs):+.6e}  RHS={float(rhs):+.6e}  err={float(err):.3e}"
        )

    # 2. Grid sign scan
    print("\nGrid sign scan (x in [-20, 20], y in [0.05, 5]):")
    bad_points = []
    min_mag = mp.inf
    max_mag = -mp.inf
    for x_i in range(-20, 21):
        x = mp.mpf(x_i)
        for y_i in [
            mp.mpf("0.05"),
            mp.mpf("0.1"),
            mp.mpf("0.25"),
            mp.mpf("0.5"),
            mp.mpf("1.0"),
            mp.mpf("2.0"),
            mp.mpf("5.0"),
        ]:
            z = mp.mpc(x, y_i)
            mag = magnitude_diff(z)
            if mag < min_mag:
                min_mag = mag
            if mag > max_mag:
                max_mag = mag
            if mag <= 0:
                bad_points.append((z, float(mag)))
    print(f"  Sampled 287 points")
    print(f"  Minimum |E_B|^2 - |E_B^#|^2 = {float(min_mag):+.6e}")
    print(f"  Maximum |E_B|^2 - |E_B^#|^2 = {float(max_mag):+.6e}")
    print(f"  Number of points with |E_B|^2 - |E_B^#|^2 <= 0: {len(bad_points)}")
    if bad_points:
        for z, mag in bad_points[:5]:
            print(f"    z={z}  |E_B|^2-|E_B^#|^2={mag:+.4e}")

    # 3. Behavior near gamma_1
    print("\nNear first zeta zero ordinate (gamma1 = 14.1347...):")
    gamma1 = mp.mpf("14.134725141734693790457251983562")
    for y in [
        mp.mpf("0.5"),
        mp.mpf("0.1"),
        mp.mpf("0.02"),
        mp.mpf("0.005"),
        mp.mpf("0.001"),
    ]:
        z = mp.mpc(gamma1, y)
        mag = magnitude_diff(z)
        xi_z = Xi(z)
        im_mb = mp.im(m_B(z))
        prediction = 4 * abs(xi_z) ** 2 * im_mb
        print(
            f"  y={float(y):.3g}  |E_B|^2-|E_B^#|^2={float(mag):+.4e}  "
            f"4|Xi|^2*Im m_B={float(prediction):+.4e}"
        )

    # 4. Real-axis check (de Branges boundary equality)
    print("\nReal-axis check (boundary equality |E_B(x)| = |E_B^#(x)|):")
    for x in [
        mp.mpf("-5"),
        mp.mpf("0"),
        mp.mpf("5"),
        mp.mpf("14.1347"),
    ]:
        z = mp.mpc(x, 0)
        mag = magnitude_diff(z)
        print(f"  x={float(x):+8.4f}: |E_B|^2 - |E_B^#|^2 = {float(mag):+.4e}")

    print("\nConclusion:")
    if not bad_points:
        print("  E_B(z) = Xi(z) + i*Xi'(z) PASSES Hermite-Biehler sign test on grid.")
        print("  Identity |E_B|^2 - |E_B^#|^2 = 4|Xi|^2 Im m_B holds unconditionally.")
        print("  Numerical confirmation of RH on the sampled grid.")
        print("  NOT a proof: RH is independently known up to enormous height.")
    else:
        print(f"  Sign test FAILS at {len(bad_points)} points — would refute RH if real.")
        print("  Investigate sign-violating points.")


if __name__ == "__main__":
    main()
