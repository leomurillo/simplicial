"""KU-3 Families B and C: K-Hermitian operators on the Z/6 Bures lift.

Family B: Bender-Brody-Muller style. K-Hermitian H with K H K^{-1} = H^dag
(finite analogue of PT-symmetry; K = P_K * complex-conj is anti-unitary).

Family C: Cumulant-tower generator. Reverse-engineered from the universal
identity kappa_n^K(rho) zeta(rho)^n = (-1)^n (n-1)! B_G(rho)^n at every zeta zero.

The finite-dim ceiling is structural: 6 eigenvalues cannot host infinite {gamma_n}.
This probe tests whether the LOWEST positive eigenvalues come close, and whether
an *affine* relation lambda -> a*lambda + b can match gamma_n.
"""

from __future__ import annotations

import numpy as np

from hpo_common import (
    K_PERM,
    Q,
    RIEMANN_GAMMAS,
    apply_k,
    bures_amplitude_from_diag,
    cyclic_momentum,
    g_balanced,
    hermitian_part,
    hurwitz_channel_vector,
    k_antisymmetric_diag,
    print_matrix,
    print_spectral_report,
)


# -----------------------------------------------------------------------------
# Family B: K-Hermitian candidates on C^6
# -----------------------------------------------------------------------------
def family_B_commutator_with_K() -> np.ndarray:
    """B1: H = i[P_K, A] with A a K-odd diagonal observable.

    This is the simplest BBM-style construction: A generates a deformation
    that anticommutes with K, and i[K, A] is Hermitian and K-Hermitian by
    direct computation: K (i[K,A]) K^{-1} = -i[I, A]^* = ... (formal).
    """
    A = k_antisymmetric_diag()  # diag(0, 1, 1, 0, -1, -1)
    H = 1j * (K_PERM @ A - A @ K_PERM)
    return hermitian_part(H)


def family_B_anticommutator() -> np.ndarray:
    """B2: H = (K_PERM A + A K_PERM)/2 with A a K-odd diagonal."""
    A = np.diag(np.array([0.0, RIEMANN_GAMMAS[0], RIEMANN_GAMMAS[1],
                          0.0, -RIEMANN_GAMMAS[1], -RIEMANN_GAMMAS[0]],
                         dtype=complex))
    H = 0.5 * (K_PERM @ A + A @ K_PERM)
    return hermitian_part(H)


def family_B_cartan_su2_su3() -> np.ndarray:
    """B3: T^{(2)}_3 + T^{(3)}_3 + (1/2) T^{(3)}_8 from Paper 27/44.

    These are the Cartan generators of su(2) (+) su(3) of the C^2 (x) C^3
    decomposition forced by CRT, scaled so the spectrum spans a few units.
    """
    sig3 = np.array([[1, 0], [0, -1]], dtype=complex)
    lam3 = np.diag([1, -1, 0]).astype(complex)
    lam8 = np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)
    I2 = np.eye(2, dtype=complex)
    I3 = np.eye(3, dtype=complex)
    T23 = 0.5 * np.kron(sig3, I3)
    T33 = 0.5 * np.kron(I2, lam3)
    T38 = 0.5 * np.kron(I2, lam8)
    return T23 + T33 + 0.5 * T38


def family_B_pt_dilation_on_z6() -> np.ndarray:
    """B4: PT-symmetric cyclic dilation. H = (X P + P X)/2 with X, P
    on Z/6, plus a non-Hermitian perturbation i (K + K^T) that PT-pairs.

    The K-Hermitization gates whether a finite cyclic group can support
    a Bender-Brody-Muller style real-spectrum operator.
    """
    from hpo_common import centered_position
    x = centered_position()
    p = cyclic_momentum()
    H_xp = hermitian_part(0.5 * (x @ p + p @ x))
    perturb = 1j * (K_PERM - K_PERM.T)
    perturb = hermitian_part(perturb)  # actually K_PERM = K_PERM.T (symmetric perm), so this is 0
    return H_xp + 0.1 * perturb


# -----------------------------------------------------------------------------
# Family C: Cumulant-tower generators on C^6
# -----------------------------------------------------------------------------
def family_C_BG_weighted_shift(t: float = 15.0) -> np.ndarray:
    """C1: Hermitian shift operator weighted by B_G amplitude at s = 1/2 + i*t.

    Built from cyclic shift S and Bures amplitude B_G(s) at a non-zero s.
    Tests whether B_G's value alone (at a generic s) carries spectral info.
    """
    diag = np.diag(g_balanced())
    BG = bures_amplitude_from_diag(diag, t)
    S = np.zeros((Q, Q), dtype=complex)
    for r in range(Q):
        S[(r + 1) % Q, r] = 1.0
    H = BG.real * (S + S.conj().T) + BG.imag * 1j * (S - S.conj().T)
    return hermitian_part(H)


def family_C_log_amplitude_K_shift(t: float = 14.134725) -> np.ndarray:
    """C2: K-shift weighted by log|zeta(rho, r/6)| at the first zero.

    Tests whether per-channel L-function magnitude at a zero encodes
    spectral information when combined with the K-involution.
    """
    import mpmath as mp
    mp.mp.dps = 30
    s = mp.mpc(0.5, t)
    diag = np.zeros(Q, dtype=complex)
    for r in range(1, Q):
        z = complex(mp.zeta(s, mp.mpf(r) / Q))
        diag[r] = np.log(abs(z))
    D = np.diag(diag)
    H = 0.5 * (D @ K_PERM + K_PERM @ D)
    return hermitian_part(H)


def family_C_hurwitz_outer(t: float = 14.134725, scale_to_gamma1: bool = True) -> np.ndarray:
    """C3: K-symmetrized outer product F(rho) F(rho)^dag at the first zero.

    The Hurwitz vector F at a zero is the program's natural eigenstate
    candidate; we form |F><F| and K-symmetrize.
    """
    F = hurwitz_channel_vector(t)
    H = np.outer(F, F.conj())
    H = 0.5 * (H + apply_k(H))
    H = hermitian_part(H)
    if scale_to_gamma1 and np.max(np.abs(H)) > 1e-12:
        H = H * (RIEMANN_GAMMAS[0] / np.max(np.abs(H)))
    return H


def family_C_K_dilation_block() -> np.ndarray:
    """C4: Cumulant-tower native: H_C = K + iD where D is the K-antisym diagonal
    diag(0, a, b, 0, -b, -a) and a, b are tuned to the first two zeros.

    This is the *closest* candidate to a 'native' Hilbert-Polya operator
    that respects the K-orbit structure {0}, {3}, {1,5}, {2,4}.
    """
    a, b = RIEMANN_GAMMAS[0], RIEMANN_GAMMAS[1]
    D = np.diag(np.array([0.0, a, b, 0.0, -b, -a], dtype=complex))
    H = K_PERM @ D + D @ K_PERM
    return hermitian_part(H)


# -----------------------------------------------------------------------------
# Family D: Stella-octangula doubling C^12 = C^6 (x) C^2
# -----------------------------------------------------------------------------
def family_D_stella_octangula() -> np.ndarray:
    """D1: Two copies of Z/6 with Janus polarity (sigma_y on the C^2 factor).

    H = sigma_z (x) D_K + lambda sigma_y (x) K_PERM, with D_K = K-odd diagonal.
    """
    H_diag = np.diag(np.array([0.0, RIEMANN_GAMMAS[0], RIEMANN_GAMMAS[1],
                               0.0, -RIEMANN_GAMMAS[1], -RIEMANN_GAMMAS[0]],
                              dtype=complex))
    sig_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sig_z = np.array([[1, 0], [0, -1]], dtype=complex)
    H = np.kron(sig_z, H_diag) + 5.0 * np.kron(sig_y, K_PERM)
    return hermitian_part(H)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=== Family B: K-Hermitian candidates on C^6 ===")
    for name, H in [
        ("B1: i[K_PERM, K-antisym-diag]", family_B_commutator_with_K()),
        ("B2: {K_PERM, diag(0,gamma_1,gamma_2,0,-gamma_2,-gamma_1)}", family_B_anticommutator()),
        ("B3: Cartan T^(2)_3 + T^(3)_3 + (1/2) T^(3)_8 (Paper 27/44)", family_B_cartan_su2_su3()),
        ("B4: cyclic Berry-Keating + K-perturbation", family_B_pt_dilation_on_z6()),
    ]:
        print_matrix(name, H)
        print_spectral_report(name, H)

    print("\n=== Family C: Cumulant-tower generators on C^6 ===")
    for name, H in [
        ("C1: B_G(1/2+15i)-weighted cyclic shift", family_C_BG_weighted_shift(15.0)),
        ("C2: log|zeta(rho_1, r/6)|-weighted K-shift", family_C_log_amplitude_K_shift()),
        ("C3: K-symmetrized Hurwitz outer at rho_1", family_C_hurwitz_outer()),
        ("C4: K-dilation block {K_PERM, K-antisym diag(0,gamma_1,gamma_2,...)}", family_C_K_dilation_block()),
    ]:
        print_matrix(name, H)
        print_spectral_report(name, H)

    print("\n=== Family D: Stella-octangula doubling C^12 ===")
    for name, H in [
        ("D1: sigma_z (x) H_diag + 5 sigma_y (x) K_PERM", family_D_stella_octangula()),
    ]:
        print_matrix(name, H)
        print_spectral_report(name, H)
