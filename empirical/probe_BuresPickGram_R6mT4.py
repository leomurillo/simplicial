"""Probe the Pick kernel / de Branges / boundary-divisor Gram identities.

This accompanies Note_BuresPickGram_Equivalence_R6mT4.md.

The script checks three things:

1. Algebraic identity:
   P_m(z,w) = pi K_E(z,w)/(Xi(z) conj(Xi(w))) for E=Xi+iXi'.

2. Conditional boundary Gram:
   For a truncated real-zero measure, the Pick kernel is exactly a Cauchy
   Gram matrix in L^2(sum delta_gamma).

3. Off-line model:
   An artificial FE cluster with interior atoms gives an indefinite Pick
   matrix, so it cannot be a positive Bures/Hilbert Gram kernel.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 70


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


def A(z: mp.mpc) -> mp.mpc:
    return Xi(z)


def B(z: mp.mpc) -> mp.mpc:
    return -Xip(z)


def m_B(z: mp.mpc) -> mp.mpc:
    return B(z) / A(z)


def E(z: mp.mpc) -> mp.mpc:
    return A(z) - 1j * B(z)


def E_sharp(z: mp.mpc) -> mp.mpc:
    return A(z) + 1j * B(z)


def pick_kernel(m_func, z: mp.mpc, w: mp.mpc) -> mp.mpc:
    return (m_func(z) - mp.conj(m_func(w))) / (z - mp.conj(w))


def debranges_kernel(z: mp.mpc, w: mp.mpc) -> mp.mpc:
    num = E(z) * mp.conj(E(w)) - E_sharp(z) * mp.conj(E_sharp(w))
    den = 2 * mp.pi * 1j * (mp.conj(w) - z)
    return num / den


def normalized_debranges_pick(z: mp.mpc, w: mp.mpc) -> mp.mpc:
    return mp.pi * debranges_kernel(z, w) / (A(z) * mp.conj(A(w)))


ZEROS = [
    mp.mpf("14.134725141734693790457251983562"),
    mp.mpf("21.022039638771554992628479593896"),
    mp.mpf("25.010857580145688763213790992562"),
    mp.mpf("30.424876125859513210311897530584"),
    mp.mpf("32.935061587739189690662368964075"),
    mp.mpf("37.586178158825671257217763480706"),
]


def m_trunc(z: mp.mpc) -> mp.mpc:
    total = mp.mpc(0)
    for gamma in ZEROS:
        total += 1 / (gamma - z)
        total += 1 / (-gamma - z)
    return total


def boundary_cauchy_gram(z: mp.mpc, w: mp.mpc) -> mp.mpc:
    total = mp.mpc(0)
    for gamma in ZEROS:
        for point in [gamma, -gamma]:
            total += 1 / ((point - z) * (point - mp.conj(w)))
    return total


GAMMA = ZEROS[0]
DELTA = mp.mpf("0.08")


def P_off(z: mp.mpc, gamma: mp.mpf = GAMMA, delta: mp.mpf = DELTA) -> mp.mpc:
    return ((z - gamma) ** 2 + delta**2) * ((z + gamma) ** 2 + delta**2)


def Pp_off(z: mp.mpc, gamma: mp.mpf = GAMMA, delta: mp.mpf = DELTA) -> mp.mpc:
    first = (z - gamma) ** 2 + delta**2
    second = (z + gamma) ** 2 + delta**2
    return 2 * (z - gamma) * second + 2 * (z + gamma) * first


def m_off(z: mp.mpc) -> mp.mpc:
    return -Pp_off(z) / P_off(z)


def matrix_from_kernel(kernel_func, points: list[mp.mpc]) -> np.ndarray:
    n = len(points)
    mat = np.zeros((n, n), dtype=np.complex128)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            mat[i, j] = complex(kernel_func(z, w))
    return (mat + mat.conj().T) / 2


def fmt_complex(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.10e}{float(mp.im(z)):+.10e}j"


def main() -> None:
    points = [
        mp.mpc(0, mp.mpf("0.2")),
        mp.mpc(2, mp.mpf("0.35")),
        mp.mpc(7, mp.mpf("0.45")),
        mp.mpc(12, mp.mpf("0.4")),
        mp.mpc(14, mp.mpf("0.3")),
    ]

    print("=" * 100)
    print("Bures Pick kernel as Gram kernel: identities and obstruction")
    print("=" * 100)

    print("\nAlgebraic de Branges identity:")
    max_err = mp.mpf("0")
    for z in points[:3]:
        for w in points[2:]:
            left = pick_kernel(m_B, z, w)
            right = normalized_debranges_pick(z, w)
            err = abs(left - right)
            max_err = max(max_err, err)
    print(f"  max |P_m - pi K_E/(A A*)| over sample pairs: {float(max_err):.3e}")

    print("\nActual Xi Pick matrix sampled in C+:")
    actual = matrix_from_kernel(lambda z, w: pick_kernel(m_B, z, w), points)
    actual_eigs = np.linalg.eigvalsh(actual)
    print("  eigenvalues:", " ".join(f"{x:+.6e}" for x in actual_eigs))

    print("\nTruncated boundary-divisor Gram identity with first six zero pairs:")
    trunc_pick = matrix_from_kernel(lambda z, w: pick_kernel(m_trunc, z, w), points)
    cauchy = matrix_from_kernel(boundary_cauchy_gram, points)
    gram_err = np.max(np.abs(trunc_pick - cauchy))
    cauchy_eigs = np.linalg.eigvalsh(cauchy)
    print(f"  max |truncated Pick - Cauchy Gram|: {gram_err:.3e}")
    print("  Cauchy Gram eigenvalues:", " ".join(f"{x:+.6e}" for x in cauchy_eigs))

    print("\nArtificial off-line FE cluster obstruction:")
    off_points = [
        mp.mpc(GAMMA, DELTA / 2),
        mp.mpc(GAMMA + mp.mpf("0.04"), DELTA / 2),
        mp.mpc(-GAMMA, DELTA / 2),
    ]
    off = matrix_from_kernel(lambda z, w: pick_kernel(m_off, z, w), off_points)
    off_eigs = np.linalg.eigvalsh(off)
    for z in off_points:
        print(f"  z={fmt_complex(z)}  P(z,z)={float(mp.re(pick_kernel(m_off, z, z))):+.10e}")
    print("  off-line Pick eigenvalues:", " ".join(f"{x:+.6e}" for x in off_eigs))

    print("\nConclusion:")
    print("  The Gram formula is exact under boundary support: R_z(gamma)=1/(gamma-z).")
    print("  Any positive Bures/K Gram law for the full m_B is equivalent to RH.")
    print("  Without boundary support, the natural divisor form becomes indefinite.")


if __name__ == "__main__":
    main()

