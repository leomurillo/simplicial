"""Corrected diagnostics for the Bures covariant log-derivative object.

This supersedes the earlier mN4pR probe for execution purposes only.  The
previous probe evaluated xi through a formula with removable gamma singularities
and hit s=0 during a grid scan.  This version avoids those removable points in
the grid and keeps the same mathematical diagnostics.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def xi(s: mp.mpc) -> mp.mpc:
    if abs(s) < mp.mpf("1e-30") or abs(s - 1) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def lambda3(s: mp.mpc) -> mp.mpc:
    return mp.power(3 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * chi3_L(s)


def Xi(z: mp.mpc) -> mp.mpc:
    return xi(mp.mpf("0.5") + 1j * z)


def L3c(z: mp.mpc) -> mp.mpc:
    return lambda3(mp.mpf("0.5") + 1j * z)


def M(z: mp.mpc) -> mp.mpc:
    return L3c(z) / Xi(z)


def deriv(f, z: mp.mpc) -> mp.mpc:
    h = mp.mpf("1e-6")
    return (f(z + h) - f(z - h)) / (2 * h)


def logderiv(f, z: mp.mpc) -> mp.mpc:
    return deriv(f, z) / f(z)


def ordinary_transfer_logderivative(z: mp.mpc) -> mp.mpc:
    return logderiv(M, z)


def bures_covariant_logderivative(z: mp.mpc) -> mp.mpc:
    return logderiv(M, z) - logderiv(L3c, z)


def xi_hamiltonian_logderivative(z: mp.mpc) -> mp.mpc:
    return -logderiv(Xi, z)


def fmt(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.10e}{float(mp.im(z)):+.10e}j"


print("=" * 100)
print("Bures covariant log-derivative m_B(z)")
print("=" * 100)
print("m_B = d log(L3c/Xi) - d log L3c = - d log Xi")

samples = [
    mp.mpc(0, mp.mpf("0.1")),
    mp.mpc(1, mp.mpf("0.1")),
    mp.mpc(5, mp.mpf("0.5")),
    mp.mpc(10, mp.mpf("0.5")),
    mp.mpc(14, mp.mpf("0.2")),
    mp.mpc(-3, mp.mpf("0.7")),
    mp.mpc(20, mp.mpf("1.5")),
]

print("\nCovariant identity check and Herglotz sign samples:")
for z in samples:
    cov = bures_covariant_logderivative(z)
    xi_obj = xi_hamiltonian_logderivative(z)
    err = abs(cov - xi_obj)
    print(
        f"  z={fmt(z)}  m_B={fmt(xi_obj)}  "
        f"Im m_B={float(mp.im(xi_obj)):+.10e}  cov_err={float(err):.3e}"
    )

print("\nOrdinary transfer log derivative has signed-divisor behavior:")
for z in samples:
    raw = ordinary_transfer_logderivative(z)
    print(f"  z={fmt(z)}  dlogM={fmt(raw)}  Im={float(mp.im(raw)):+.10e}")

print("\nGrid scan for Im m_B on a small upper-half-plane rectangle:")
min_im = mp.inf
min_z = None
for x_i in range(-12, 13):
    x = mp.mpf(x_i)
    for y in [mp.mpf("0.05"), mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.55"), mp.mpf("1.0")]:
        z = mp.mpc(x, y)
        val = xi_hamiltonian_logderivative(z)
        if mp.im(val) < min_im:
            min_im = mp.im(val)
            min_z = z
print(f"  minimum sampled Im m_B = {float(min_im):+.10e} at z={fmt(min_z)}")

print("\nNear first zeta zero ordinate:")
gamma1 = mp.mpf("14.134725141734693790457251983562")
for y in [mp.mpf("0.5"), mp.mpf("0.1"), mp.mpf("0.02"), mp.mpf("0.005")]:
    z = mp.mpc(gamma1, y)
    val = xi_hamiltonian_logderivative(z)
    print(f"  z=gamma1+{float(y):.3g}i  m_B={fmt(val)}  Im={float(mp.im(val)):+.10e}")

print("\nConclusion:")
print("  The found Bures log-derivative object is m_B(z)=-Xi'(z)/Xi(z).")
print("  It is Herglotz iff RH holds, because non-real zeta zeros are exactly poles in C+.")
