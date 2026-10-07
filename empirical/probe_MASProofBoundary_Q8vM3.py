"""Probe for Note_MASProofBoundary_Q8vM3.

The script checks the three operational pieces of the MAS boundary theorem:

1. gamma reflection is unitary on a non-metaplectic atomic packet;
2. the atomic support obstructs Weyl translation covariance;
3. once the Weyl multiplier and positive oscillator polarization are inserted,
   the even/odd Mellin characters match the gamma factors.
"""

from __future__ import annotations

import cmath
import math

import mpmath as mp


mp.mp.dps = 40


def gamma_R(s: complex) -> complex:
    z = mp.mpc(s)
    return complex(mp.power(mp.pi, -z / 2) * mp.gamma(z / 2))


def gamma_phase(t: float) -> complex:
    return gamma_R(0.5 + 1j * t) / gamma_R(0.5 - 1j * t)


def atomic_measure(cutoff: int = 8) -> list[tuple[float, float]]:
    atoms = [(0.0, 1.0)]
    for k in range(1, cutoff + 1):
        mass = 2.0 ** (-k)
        atoms.append((float(k), mass))
        atoms.append((float(-k), mass))
    norm = sum(m for _, m in atoms)
    return [(t, m / norm) for t, m in atoms]


def sample_function(t: float) -> complex:
    return (1 + 0.2j) * cmath.exp(-0.05 * (t - 1.0) ** 2) + (
        -0.3 + 0.7j
    ) * cmath.exp(-0.08 * (t + 2.0) ** 2)


def atomic_norm(atoms: list[tuple[float, float]], transformed: bool) -> float:
    total = 0.0
    for t, mass in atoms:
        value = gamma_phase(t) * sample_function(-t) if transformed else sample_function(t)
        total += mass * abs(value) ** 2
    return total


def gamma_atomic_countermodel() -> None:
    atoms = atomic_measure()
    before = atomic_norm(atoms, transformed=False)
    after = atomic_norm(atoms, transformed=True)
    print("Atomic gamma-reflection packet")
    print(f"weighted norm before  : {before:.12e}")
    print(f"weighted norm after   : {after:.12e}")
    print(f"difference            : {abs(before - after):.3e}")


def translation_covariance_obstruction() -> None:
    support = {t for t, _ in atomic_measure()}
    shifted = {t + 0.5 for t in support}
    intersection = support.intersection(shifted)
    print("\nTranslation covariance obstruction")
    print(f"support size          : {len(support)}")
    print(f"shifted overlap       : {len(intersection)}")
    print("rank preservation fails for the spectral projection E_T(S) -> E_T(S+1/2).")


def weyl_multiplier_demo() -> None:
    a = (0.7, -1.2)
    b = (2.0, 0.4)
    c = (-0.3, 0.9)

    def omega(x: tuple[float, float], y: tuple[float, float]) -> float:
        return x[0] * y[1] - x[1] * y[0]

    left_phase = cmath.exp(1j * math.pi * omega(a, b)) * cmath.exp(
        1j * math.pi * omega((a[0] + b[0], a[1] + b[1]), c)
    )
    right_phase = cmath.exp(1j * math.pi * omega(b, c)) * cmath.exp(
        1j * math.pi * omega(a, (b[0] + c[0], b[1] + c[1]))
    )
    associator = left_phase / right_phase
    cocycle_identity_error = abs(associator - 1)
    print("\nWeyl multiplier cocycle check")
    print(f"2-cocycle identity error: {cocycle_identity_error:.3e}")
    print("This antisymmetric phase is the datum missing from Bures/Petz metric data.")


def oscillator_mellin() -> None:
    print("\nOscillator gamma character under MAS")
    for s in [0.5 + 1.7j, 1.1 + 0.2j, 2.0 + 3.0j]:
        z = mp.mpc(s)
        even_integral = 2 * mp.quad(
            lambda x: mp.e ** (-mp.pi * x * x) * x ** (z - 1), [0, mp.inf]
        )
        odd_integral = 2 * mp.quad(
            lambda x: x * mp.e ** (-mp.pi * x * x) * x ** (z - 1), [0, mp.inf]
        )
        even_gamma = mp.power(mp.pi, -z / 2) * mp.gamma(z / 2)
        odd_gamma = mp.power(mp.pi, -(z + 1) / 2) * mp.gamma((z + 1) / 2)
        print(
            f"s={s}: even={float(abs(even_integral-even_gamma)):.3e}, "
            f"odd={float(abs(odd_integral-odd_gamma)):.3e}"
        )


def main() -> None:
    gamma_atomic_countermodel()
    translation_covariance_obstruction()
    weyl_multiplier_demo()
    oscillator_mellin()


if __name__ == "__main__":
    main()

