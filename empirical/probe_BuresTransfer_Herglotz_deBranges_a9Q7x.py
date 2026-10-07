"""Numerical witnesses for the completed Bures transfer ratio.

This script accompanies Note_BuresTransfer_Herglotz_deBranges_a9Q7x.md.
It does not prove the theorem by itself; it prints the concrete diagnostics
that mirror the proof:

1. The K-normalized ratio M(z)=Lambda_3(1/2+iz)/xi(1/2+iz) is real at
   interior points z=iy of the spectral upper half-plane.
2. Im M changes sign in the upper half-plane.
3. The Hermite-Biehler inequality for E=Xi-iLambda_3 has both signs and,
   more basically, equality on the interior imaginary axis.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def xi(s: mp.mpc) -> mp.mpc:
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lambda3(s: mp.mpc) -> mp.mpc:
    return mp.power(3 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * chi3_L(s)


def Xi(z: mp.mpc) -> mp.mpc:
    return xi(mp.mpf("0.5") + 1j * z)


def L3c(z: mp.mpc) -> mp.mpc:
    return lambda3(mp.mpf("0.5") + 1j * z)


def M(z: mp.mpc) -> mp.mpc:
    return L3c(z) / Xi(z)


def E(z: mp.mpc) -> mp.mpc:
    return Xi(z) - 1j * L3c(z)


def E_sharp(z: mp.mpc) -> mp.mpc:
    # For real entire Xi,L3c, E# = Xi + i L3c.
    return Xi(z) + 1j * L3c(z)


def fmt(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.10e}{float(mp.im(z)):+.10e}j"


print("=" * 100)
print("Completed Bures transfer ratio M(z)=Lambda_3(1/2+iz)/xi(1/2+iz)")
print("=" * 100)

print("\nInterior imaginary-axis points z=iy (upper half-plane for y>0):")
for y in [mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.75"), mp.mpf("1.2")]:
    z = 1j * y
    value = M(z)
    print(f"  z={fmt(z)}  M(z)={fmt(value)}  Im M={float(mp.im(value)):+.3e}")

print("\nSign check for Im M in the upper half-plane:")
for z in [
    mp.mpc(1, mp.mpf("0.1")),
    mp.mpc(5, mp.mpf("0.5")),
    mp.mpc(10, mp.mpf("0.5")),
    mp.mpc(-3, mp.mpf("0.7")),
]:
    value = M(z)
    print(f"  z={fmt(z)}  M(z)={fmt(value)}  Im M={float(mp.im(value)):+.10e}")

print("\nHermite-Biehler delta for E=Xi-iLambda_3:")
print("delta(z)=|E(z)|^2-|E#(z)|^2; HB would require one strict sign in C+.")
for z in [
    1j * mp.mpf("0.25"),
    mp.mpc(1, mp.mpf("0.1")),
    mp.mpc(5, mp.mpf("0.5")),
    mp.mpc(10, mp.mpf("0.5")),
]:
    delta = abs(E(z)) ** 2 - abs(E_sharp(z)) ** 2
    print(f"  z={fmt(z)}  delta={float(delta):+.10e}")

print("\nConclusion:")
print("  The completed ratio is K-real inside C+ on z=iy, so it is not Herglotz.")
print("  The associated E has |E|=|E#| at interior C+ points, so it is not Hermite-Biehler.")
