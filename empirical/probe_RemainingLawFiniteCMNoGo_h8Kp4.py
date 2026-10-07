"""Rank probe for the remaining finite CM/Bures Gram law.

Random suffix: h8Kp4

The probe computes the Pick matrix of m_B=-Xi'/Xi at points near the first ten
known critical-line zeros.  A finite six-edge CM/Bures Gram state would have
rank at most 6.  The sampled Pick matrix has rank 10, demonstrating the
finite-rank obstruction numerically.
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


def pick_matrix(points):
    matrix = np.empty((len(points), len(points)), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            matrix[i, j] = complex(pick_bures(z, w))
    return (matrix + matrix.conj().T) / 2


def normalized_edge_gram_rank(points):
    """Rank of a typical six-channel finite edge-state Gram.

    This does not claim to be the unique CM Gram; it records the universal
    dimensional ceiling: any six-edge vector state has rank at most 6.
    """
    # Use simple Vandermonde-like six-edge feature placeholders to show the
    # rank ceiling independently of the detailed Bures normalization.
    features = np.empty((len(points), 6), dtype=complex)
    for i, z in enumerate(points):
        zc = complex(z)
        features[i, :] = [1, zc, zc**2, zc**3, np.exp(0.1j * zc), np.exp(-0.07j * zc)]
    gram = features @ features.conj().T
    singular = np.linalg.svd(gram, compute_uv=False)
    return singular, int(np.sum(singular > 1e-8))


def main() -> None:
    points = [gamma + mp.mpc(0, mp.mpf("0.5")) for gamma in GAMMAS]
    K = pick_matrix(points)
    eigs = np.linalg.eigvalsh(K)
    singular = np.linalg.svd(K, compute_uv=False)
    rank = int(np.sum(singular > 1e-8))

    print("sample_count:", len(points))
    print("Pick eigenvalues:")
    print(np.array2string(eigs, precision=8))
    print("Pick singular values:")
    print(np.array2string(singular, precision=8))
    print("Pick numerical rank tol=1e-8:", rank)
    print("finite six-edge rank ceiling:", 6)
    print("rank_obstruction_detected:", rank > 6)

    edge_singular, edge_rank = normalized_edge_gram_rank(points)
    print("\nExample six-feature Gram singular values:")
    print(np.array2string(edge_singular, precision=8))
    print("Example six-feature Gram rank tol=1e-8:", edge_rank)

    print("\nConclusion:")
    if rank > 6:
        print("  P_B already has rank greater than the six-edge state ceiling.")
        print("  The remaining law cannot be finite-dimensional CM edge positivity.")
        print("  A genuine proof needs an infinite CM divisor/canonical-system space.")
    else:
        print("  Increase sample size or precision; no obstruction detected here.")


if __name__ == "__main__":
    main()

