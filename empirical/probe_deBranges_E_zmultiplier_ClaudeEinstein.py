"""Test E(z) = Xi(z) - i*z*L3c(z) as a de Branges E-function.

The naive E = Xi - i*L3c fails because both factors are even in z, giving
parity-anti-symmetric sign of |E|^2 - |E^#|^2.  The factor z is odd, so

    E(z)    = Xi(z) - i*z*L3c(z)
    E^#(z)  = conj(E(conj(z))) = Xi(z) + i*z*L3c(z)

On the real line: E^#(x) = conj(E(x)), so |E(x)| = |E^#(x)| (de Branges
boundary equality).

For z in C+, we need |E|^2 > |E^#|^2.  Compute and check.
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


def E_zmult(z: mp.mpc) -> mp.mpc:
    return Xi(z) - 1j * z * L3c(z)


def E_zmult_sharp(z: mp.mpc) -> mp.mpc:
    # E^#(z) := conj(E(conj(z))) -- since Xi, L3c are real-entire (even), this is
    # Xi(z) + i*z*L3c(z)
    return Xi(z) + 1j * z * L3c(z)


def magnitude_diff(z: mp.mpc) -> mp.mpf:
    return abs(E_zmult(z)) ** 2 - abs(E_zmult_sharp(z)) ** 2


def main() -> None:
    print("=" * 100)
    print("de Branges candidate (z-multiplier): E(z) = Xi(z) - i*z*L3c(z)")
    print("=" * 100)
    print("Need |E(z)|^2 - |E^#(z)|^2 > 0 on C+; equal on R.")
    print()

    # Real-line check
    print("Real-line check (de Branges boundary equality):")
    for x in [
        mp.mpf("-5"),
        mp.mpf("-1"),
        mp.mpf("0"),
        mp.mpf("1"),
        mp.mpf("5"),
        mp.mpf("14.1347"),
    ]:
        z = mp.mpc(x, 0)
        mag = magnitude_diff(z)
        print(f"  x={float(x):+8.4f}: |E|^2 - |E^#|^2 = {float(mag):+.4e}")

    # Sample points in C+
    print("\nSample points in C+:")
    samples = [
        mp.mpc(0, mp.mpf("0.1")),
        mp.mpc(0, mp.mpf("1.0")),
        mp.mpc(5, mp.mpf("0.5")),
        mp.mpc(-5, mp.mpf("0.5")),
        mp.mpc(10, mp.mpf("0.7")),
        mp.mpc(14, mp.mpf("0.3")),
        mp.mpc(20, mp.mpf("1.0")),
        mp.mpc(-20, mp.mpf("0.05")),
        mp.mpc(50, mp.mpf("2.0")),
    ]
    for z in samples:
        mag = magnitude_diff(z)
        sign = "positive (good)" if mag > 0 else "NEGATIVE (bad)"
        print(
            f"  z={float(mp.re(z)):+8.3f}{float(mp.im(z)):+6.3f}i  "
            f"|E|^2-|E^#|^2={float(mag):+.4e} [{sign}]"
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
            mag = magnitude_diff(z)
            if mag < min_mag:
                min_mag = mag
                min_z = z
            if mag > max_mag:
                max_mag = mag
                max_z = z
            if mag <= 0:
                bad_points.append((z, float(mag)))

    print(f"  Sampled 287 points")
    print(f"  Minimum |E|^2 - |E#|^2 = {float(min_mag):+.6e} at z={min_z}")
    print(f"  Maximum |E|^2 - |E#|^2 = {float(max_mag):+.6e} at z={max_z}")
    print(f"  Number of points with |E|^2 - |E#|^2 <= 0: {len(bad_points)}")
    if 0 < len(bad_points) <= 10:
        print("  Bad points:")
        for z, mag in bad_points:
            print(f"    z={z}  |E|^2-|E#|^2={mag:+.4e}")
    elif len(bad_points) > 10:
        print(f"  First 5 bad points:")
        for z, mag in bad_points[:5]:
            print(f"    z={z}  |E|^2-|E#|^2={mag:+.4e}")

    print("\nConclusion:")
    if not bad_points:
        print("  E(z) = Xi(z) - i*z*L3c(z) PASSES sign test on grid.")
        print("  Candidate is a de Branges E-function on the sampled region.")
    else:
        print(f"  E(z) = Xi(z) - i*z*L3c(z) FAILS at {len(bad_points)} points.")
        print("  Try E = Xi(z) + i*z*L3c(z) or different multiplier.")


if __name__ == "__main__":
    main()
