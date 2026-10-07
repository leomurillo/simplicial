"""Corrected bounded-feature rank display for the finite CM no-go.

Random suffix: P3mV7

This companion avoids ill-conditioned polynomial/exponential placeholder
features.  It keeps the same P_B rank test and compares it to a bounded
six-feature Gram whose numerical rank displays the exact finite ceiling.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 80

GAMMAS = [
    mp.mpf("14.1347251417346937904572519835625"),
    mp.mpf("21.0220396387715549926284795938969"),
    mp.mpf("25.0108575801456887632137909925628"),
    mp.mpf("30.4248761258595132103118975305840"),
    mp.mpf("32.9350615877391896906623689640747"),
    mp.mpf("37.5861781588256712572177634807053"),
    mp.mpf("40.9187190121474951873981269146334"),
    mp.mpf("43.3270732809149995194961221654068"),
    mp.mpf("48.0051508811671597279424727494277"),
    mp.mpf("49.7738324776723021819167846785638"),
]


def xi_s(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z):
    return xi_s(mp.mpf("0.5") + 1j * z)


def Xi_prime(z):
    return 1j * mp.diff(xi_s, mp.mpf("0.5") + 1j * z)


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def pick_bures(z, w):
    return (m_bures(z) - mp.conj(m_bures(w))) / (z - mp.conj(w))


def numerical_rank(values, *, relative=1e-10):
    values = np.asarray(values, dtype=float)
    return int(np.sum(values > relative * values[0]))


def bounded_six_feature_gram(points):
    centers = np.array([-3, -1, 0, 2, 5, 8], dtype=float)
    features = np.empty((len(points), len(centers)), dtype=complex)
    for i, z in enumerate(points):
        zc = complex(z)
        features[i, :] = [1 / (zc + 20 + c) for c in centers]
    gram = features @ features.conj().T
    return (gram + gram.conj().T) / 2


def main() -> None:
    points = [gamma + mp.mpc(0, mp.mpf("0.5")) for gamma in GAMMAS]

    pick = np.empty((len(points), len(points)), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            pick[i, j] = complex(pick_bures(z, w))
    pick = (pick + pick.conj().T) / 2

    pick_s = np.linalg.svd(pick, compute_uv=False)
    pick_e = np.linalg.eigvalsh(pick)
    print("P_B eigenvalues:")
    print(np.array2string(pick_e, precision=8))
    print("P_B numerical rank relative=1e-10:", numerical_rank(pick_s))

    six = bounded_six_feature_gram(points)
    six_s = np.linalg.svd(six, compute_uv=False)
    print("\nBounded six-feature Gram singular values:")
    print(np.array2string(six_s, precision=12))
    print("Bounded six-feature numerical rank relative=1e-10:", numerical_rank(six_s))

    print("\nRank comparison:")
    print("  P_B rank:", numerical_rank(pick_s))
    print("  finite six-edge ceiling:", 6)
    print("  bounded six-feature rank:", numerical_rank(six_s))
    print("  obstruction:", numerical_rank(pick_s) > 6)


if __name__ == "__main__":
    main()

