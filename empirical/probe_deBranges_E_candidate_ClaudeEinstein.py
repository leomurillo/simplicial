"""Test whether E(z) = Xi(z) - i*L3c(z) is a de Branges E-function.

A de Branges E-function satisfies |E(z)| > |E^#(z)| for all z in C+, equivalently
all zeros of E lie in the closed lower half-plane.

For real-entire Xi and L3c we have E^#(z) = Xi(z) + i*L3c(z), so

  |E|^2 - |E^#|^2 = -4 * Im(conj(Xi)(z) * L3c(z)).

The de Branges condition is therefore

  Im(conj(Xi)(z) * L3c(z)) < 0   for all z in C+.

This probe checks the sign of that quantity on a grid in C+ and looks for
sign changes.  If uniformly negative, E = Xi - i L3c is a de Branges function
and the boundary-support law for the joint divisor follows.
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


def de_branges_quantity(z: mp.mpc) -> mp.mpf:
    """Return Im(conj(Xi(z)) * L3c(z)).  Need this NEGATIVE on C+ for E to be deBranges."""
    return mp.im(mp.conj(Xi(z)) * L3c(z))


def magnitude_E_minus_Estar(z: mp.mpc) -> mp.mpf:
    """Direct computation of |E|^2 - |E#|^2 for E = Xi - i*L3c."""
    e = Xi(z) - 1j * L3c(z)
    e_sharp = Xi(z) + 1j * L3c(z)
    return abs(e) ** 2 - abs(e_sharp) ** 2


def main() -> None:
    print("=" * 100)
    print("de Branges E-function candidate: E(z) = Xi(z) - i*L3c(z)")
    print("=" * 100)
    print("De Branges condition: |E(z)|^2 - |E#(z)|^2 > 0 on C+")
    print("Equivalent: Im(conj(Xi(z)) * L3c(z)) < 0 on C+")
    print()

    # Sample points
    print("Sample points in C+:")
    samples = [
        mp.mpc(0, mp.mpf("0.1")),
        mp.mpc(0, mp.mpf("1.0")),
        mp.mpc(5, mp.mpf("0.5")),
        mp.mpc(10, mp.mpf("0.7")),
        mp.mpc(14, mp.mpf("0.3")),
        mp.mpc(20, mp.mpf("1.0")),
        mp.mpc(-5, mp.mpf("0.5")),
        mp.mpc(50, mp.mpf("2.0")),
    ]
    for z in samples:
        q = de_branges_quantity(z)
        mag = magnitude_E_minus_Estar(z)
        sign_q = "negative (good)" if q < 0 else "POSITIVE (bad)"
        sign_mag = "positive (good)" if mag > 0 else "NEGATIVE (bad)"
        print(
            f"  z={float(mp.re(z)):+8.3f}{float(mp.im(z)):+6.3f}i  "
            f"Im(conj(Xi)*L3c)={float(q):+.4e} [{sign_q}]  "
            f"|E|^2-|E#|^2={float(mag):+.4e} [{sign_mag}]"
        )

    # Grid scan
    print("\nGrid scan over (x in [-20, 20], y in [0.05, 5]):")
    bad_points = []
    min_mag = mp.inf
    min_z = None
    max_mag = -mp.inf
    max_z = None
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
            mag = magnitude_E_minus_Estar(z)
            if mag < min_mag:
                min_mag = mag
                min_z = z
            if mag > max_mag:
                max_mag = mag
                max_z = z
            if mag <= 0:
                bad_points.append((z, float(mag)))

    print(f"  Sampled {41 * 7} = 287 points")
    print(f"  Minimum |E|^2 - |E#|^2 = {float(min_mag):+.6e} at z={min_z}")
    print(f"  Maximum |E|^2 - |E#|^2 = {float(max_mag):+.6e} at z={max_z}")
    print(f"  Number of points with |E|^2 - |E#|^2 <= 0: {len(bad_points)}")
    if bad_points and len(bad_points) <= 10:
        print("  Bad points (sign-violating):")
        for z, mag in bad_points:
            print(f"    z={z}  |E|^2-|E#|^2={mag:+.4e}")
    elif len(bad_points) > 10:
        print(f"  First 5 bad points:")
        for z, mag in bad_points[:5]:
            print(f"    z={z}  |E|^2-|E#|^2={mag:+.4e}")

    # Behavior near real zeros
    print("\nNear first zeta zero ordinate (gamma1 = 14.1347...):")
    gamma1 = mp.mpf("14.134725141734693790457251983562")
    for y in [
        mp.mpf("0.5"),
        mp.mpf("0.1"),
        mp.mpf("0.02"),
        mp.mpf("0.005"),
    ]:
        z = mp.mpc(gamma1, y)
        mag = magnitude_E_minus_Estar(z)
        e_val = Xi(z) - 1j * L3c(z)
        e_sharp = Xi(z) + 1j * L3c(z)
        print(
            f"  y={float(y):.3g}  |E|^2-|E#|^2={float(mag):+.4e}  "
            f"|E|={float(abs(e_val)):.4e}  |E#|={float(abs(e_sharp)):.4e}"
        )

    print("\nTest the alternate E = Xi + i*L3c (sign flip):")
    print("  This requires Im(conj(Xi)*L3c) > 0 on C+.")
    z = mp.mpc(5, mp.mpf("0.5"))
    q = de_branges_quantity(z)
    print(f"  z={z}: Im(conj(Xi)*L3c)={float(q):+.4e}")
    print(f"  Sign opposite of E = Xi - i*L3c case, so exactly one of the two")
    print(f"  candidates is a de Branges function (or neither, if signs disagree).")

    print("\nConclusion:")
    if not bad_points:
        print("  E(z) = Xi(z) - i*L3c(z) PASSES the de Branges sign test on the grid.")
        print("  Boundary support follows for the joint divisor.")
        print("  Next: prove this analytically for all z in C+ (not just sampled).")
    else:
        print(f"  E(z) = Xi(z) - i*L3c(z) FAILS at {len(bad_points)} grid points.")
        print("  Try E = Xi + i*L3c, or a phase-rotated variant.")


if __name__ == "__main__":
    main()
