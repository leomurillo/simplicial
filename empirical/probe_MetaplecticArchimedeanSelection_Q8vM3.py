"""Probe for Note_MetaplecticArchimedeanSelection_Q8vM3.

This script demonstrates two things:

1. The even/odd oscillator Mellin integrals numerically match the gamma
   factors.
2. The gamma reflection phase is unitary for many different even positive
   measures, so the phase does not select the spectral measure.
"""

from __future__ import annotations

import cmath
import math
from typing import Callable

try:
    import mpmath as mp
except ImportError as exc:  # pragma: no cover
    raise SystemExit("This probe requires mpmath, which is available in the project env.") from exc


mp.mp.dps = 40


def gamma_R(s: complex) -> complex:
    z = mp.mpc(s)
    return complex(mp.power(mp.pi, -z / 2) * mp.gamma(z / 2))


def gamma_phase(t: float) -> complex:
    return gamma_R(0.5 + 1j * t) / gamma_R(0.5 - 1j * t)


def sample_grid(width: float = 12.0, n: int = 20001) -> list[float]:
    step = 2 * width / (n - 1)
    return [-width + i * step for i in range(n)]


def trapz(values: list[float], xs: list[float]) -> float:
    total = 0.0
    for i in range(len(xs) - 1):
        total += 0.5 * (values[i] + values[i + 1]) * (xs[i + 1] - xs[i])
    return total


def test_function(t: float) -> complex:
    return (1.0 + 0.3j) * cmath.exp(-0.18 * (t - 1.7) ** 2) + (
        -0.4 + 0.8j
    ) * cmath.exp(-0.11 * (t + 2.1) ** 2)


def norm_under_measure(weight: Callable[[float], float], transformed: bool) -> float:
    xs = sample_grid()
    vals = []
    for t in xs:
        if transformed:
            value = gamma_phase(t) * test_function(-t)
        else:
            value = test_function(t)
        vals.append(abs(value) ** 2 * weight(t))
    return trapz(vals, xs)


def gaussian_weight(t: float) -> float:
    return math.exp(-0.15 * t * t)


def cauchy_weight(t: float) -> float:
    return 1.0 / (1.0 + t * t)


def compact_weight(t: float) -> float:
    return max(0.0, 1.0 - abs(t) / 10.0)


def atomic_norm(transformed: bool) -> float:
    atoms = [(0.7, 0.8), (2.5, 1.1), (5.0, 0.35)]
    total = 0.0
    for lam, mass in atoms:
        for t in (lam, -lam):
            value = gamma_phase(t) * test_function(-t) if transformed else test_function(t)
            total += mass * abs(value) ** 2
    return total


def oscillator_mellin_check() -> None:
    print("Oscillator Mellin character check")
    for s in [0.5 + 3.0j, 1.2 + 0.7j, 2.0 + 4.5j]:
        z = mp.mpc(s)
        even_integral = 2 * mp.quad(
            lambda x: mp.e ** (-mp.pi * x * x) * x ** (z - 1), [0, mp.inf]
        )
        odd_integral = 2 * mp.quad(
            lambda x: mp.e ** (-mp.pi * x * x) * x ** z, [0, mp.inf]
        )
        even_gamma = mp.power(mp.pi, -z / 2) * mp.gamma(z / 2)
        odd_gamma = mp.power(mp.pi, -(z + 1) / 2) * mp.gamma((z + 1) / 2)
        print(
            f"s={s}: |even-gamma|={float(abs(even_integral-even_gamma)):.3e}, "
            f"|odd-gamma|={float(abs(odd_integral-odd_gamma)):.3e}"
        )


def phase_measure_freedom_check() -> None:
    print("\nGamma phase unitarity across incompatible even measures")
    measures = [
        ("Gaussian continuous", gaussian_weight),
        ("Cauchy continuous", cauchy_weight),
        ("Compact tent continuous", compact_weight),
    ]
    for name, weight in measures:
        before = norm_under_measure(weight, transformed=False)
        after = norm_under_measure(weight, transformed=True)
        print(f"{name:24s}: before={before:.12e} after={after:.12e} diff={abs(before-after):.3e}")
    before = atomic_norm(transformed=False)
    after = atomic_norm(transformed=True)
    print(f"{'Symmetric atomic':24s}: before={before:.12e} after={after:.12e} diff={abs(before-after):.3e}")

    print("\nSame phase, visibly different measures")
    for t in [0.0, 1.0, 3.0, 6.0]:
        phase = gamma_phase(t)
        print(f"t={t:3.1f}: |gamma_phase|={abs(phase):.12f}, arg={cmath.phase(phase): .6f}")


def main() -> None:
    oscillator_mellin_check()
    phase_measure_freedom_check()


if __name__ == "__main__":
    main()

