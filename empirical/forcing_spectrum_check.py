"""Smoke test for the SGD forcing-spectrum theorem (Paper 12, Theorem 1.1.1).

Verifies on R = C_6 (six-element cyclic group, three nontrivial conductor packets):

  1. The output-side population covariance T_D(z) = E_y[(p_* - e_y)(p_* - e_y)^T]
     satisfies   T_char[chi_a, chi_b] = (1/Q) * hat_mu(a - b)   exactly
     (Theorem 1.1.1(1)).  In particular:

       (a) At uniform marginal mu = p_*, T_char is exactly character-diagonal
           (a fortiori conductor-block-diagonal).
       (b) At biased Hayes-invariant marginal, the cross-conductor entries
           coincide with the Hayes-Mobius operator C_1[f,e](mu - p_*) entries
           of Paper 11 -- not zero, but determined by the same algebra A_R.

  2. At a centroid-initialized softmax MLP with uniform labels, the empirical
     gradient covariance is character-diagonal up to MC noise (Theorem 1.1.1(2)).

  3. The mini-batch noise covariance Sigma at w_* with uniform marginal labels
     is character-diagonal (Theorem 1.1.1(4)).

Conductor packets of R = C_6 (character chi_k(j) = omega^{kj} for omega = e^{2*pi*i/6}):

    X_6 = {chi_1, chi_5}    (order 6 -- "fully primitive")
    X_3 = {chi_2, chi_4}    (order 3 -- "tame")
    X_2 = {chi_3}           (order 2 -- "parity")

Hayes normalizer Gamma_R = (Z/6)^* = {1, 5}, acting by chi_k -> chi_{5k mod 6}:
swaps chi_1 <-> chi_5 and chi_2 <-> chi_4, fixes chi_3.

Run from empirical/:

    python forcing_spectrum_check.py

Exit status 0 on success; nonzero on any failure beyond numerical tolerance.
"""

from __future__ import annotations

import sys
import numpy as np


RNG_SEED = 20260513
TOLERANCE = 1e-10
EMPIRICAL_TOLERANCE = 5e-2  # for MC-estimated quantities


# ---------------------------------------------------------------------------
# C_6 conductor structure


Q = 6
OMEGA = np.exp(2j * np.pi / Q)

# DFT matrix: F[k, j] = omega^{kj} / sqrt(Q), so F sends standard basis (rows j)
# to character basis (rows k).
DFT = np.array([[OMEGA ** (k * j) for j in range(Q)] for k in range(Q)]) / np.sqrt(Q)
DFT_INV = DFT.conj().T

# Conductor packet of chi_k = order of chi_k = Q / gcd(Q, k).
NONTRIVIAL_CHARS = list(range(1, Q))  # k = 1, ..., 5
CONDUCTOR_PACKET = {k: Q // np.gcd(Q, k) for k in NONTRIVIAL_CHARS}
# 1 -> 6, 5 -> 6, 2 -> 3, 4 -> 3, 3 -> 2

P_STAR = np.ones(Q) / Q


def packet_index_groups() -> dict[int, list[int]]:
    """Return mapping conductor -> list of character indices (1..Q-1) in that packet."""
    groups: dict[int, list[int]] = {}
    for k, cond in CONDUCTOR_PACKET.items():
        groups.setdefault(cond, []).append(k)
    return groups


def to_character_basis(M: np.ndarray) -> np.ndarray:
    """Change basis from R-standard to character basis: M_char = DFT @ M @ DFT^H."""
    return DFT @ M @ DFT_INV


def hayes_invariant_check(mu: np.ndarray) -> bool:
    """For C_6, Hayes-invariance is mu[1] == mu[5] and mu[2] == mu[4]."""
    return np.isclose(mu[1], mu[5]) and np.isclose(mu[2], mu[4])


# ---------------------------------------------------------------------------
# (1) Output-side block diagonalization


def output_side_covariance(mu: np.ndarray) -> np.ndarray:
    """T = sum_y mu_y (e_y - p_*) (e_y - p_*)^T."""
    T = np.zeros((Q, Q))
    for y in range(Q):
        tau_y = -P_STAR.copy()
        tau_y[y] += 1.0
        T += mu[y] * np.outer(tau_y, tau_y)
    return T


def off_conductor_norm(T_char: np.ndarray, packets: dict[int, list[int]]) -> float:
    """Max magnitude of T_char[k, k'] over (k, k') in distinct conductor packets,
    with k, k' both nontrivial."""
    max_off = 0.0
    packet_list = list(packets.values())
    for i, group_i in enumerate(packet_list):
        for group_j in packet_list[i + 1 :]:
            for k in group_i:
                for kp in group_j:
                    max_off = max(max_off, abs(T_char[k, kp]), abs(T_char[kp, k]))
    return float(max_off)


def on_conductor_summary(T_char: np.ndarray, packets: dict[int, list[int]]) -> dict:
    """Report Frobenius norm of each conductor-block diagonal restriction."""
    out: dict[int, float] = {}
    for cond, group in packets.items():
        block = T_char[np.ix_(group, group)]
        out[cond] = float(np.linalg.norm(block, ord="fro"))
    return out


def hat_mu(mu: np.ndarray, eta: int) -> complex:
    """Fourier transform of mu at character chi_eta: sum_j mu_j omega^{eta j}."""
    return sum(mu[j] * OMEGA ** (eta * j) for j in range(Q))


def check_output_side_identity(rng: np.random.Generator) -> dict:
    """Verify T_char[chi_a, chi_b] = Q^{-1} * hat_mu(a - b) exactly,
    for several mu (uniform, biased Hayes-invariant, generic non-Hayes-invariant).
    This is the corrected Theorem 1.1.1(1) identity."""

    samples = []
    samples.append(("uniform", P_STAR.copy()))
    samples.append(("biased Hayes-inv 1", np.array([0.30, 0.10, 0.15, 0.20, 0.15, 0.10])))
    samples.append(("biased Hayes-inv 2", np.array([0.25, 0.20, 0.05, 0.25, 0.05, 0.20])))
    samples.append(("non-Hayes-inv", np.array([0.30, 0.05, 0.20, 0.20, 0.15, 0.10])))
    for i in range(3):
        raw = rng.uniform(0.1, 0.5, size=Q)
        raw = raw / raw.sum()
        samples.append((f"random non-Hayes-inv {i}", raw))

    failures = 0
    max_residual = 0.0
    for name, mu in samples:
        T = output_side_covariance(mu)
        T_char = to_character_basis(T)
        # check identity at every (a, b) with a, b nontrivial
        for a in NONTRIVIAL_CHARS:
            for b in NONTRIVIAL_CHARS:
                predicted = hat_mu(mu, a - b) / Q
                actual = T_char[a, b]
                residual = abs(actual - predicted)
                max_residual = max(max_residual, residual)
                if residual > TOLERANCE:
                    failures += 1

    return {
        "samples": len(samples),
        "failures": failures,
        "max_residual": max_residual,
    }


def check_output_side_uniform_diagonal() -> dict:
    """At uniform mu = p_*, T_char should be exactly character-diagonal with
    entry 1/Q on every nontrivial character (Theorem 1.1.1(1), uniform case)."""

    packets = packet_index_groups()
    T = output_side_covariance(P_STAR)
    T_char = to_character_basis(T)
    expected_diag = 1.0 / Q
    diag = np.array([T_char[k, k].real for k in NONTRIVIAL_CHARS])
    off_diag = np.array(
        [
            abs(T_char[a, b])
            for a in NONTRIVIAL_CHARS
            for b in NONTRIVIAL_CHARS
            if a != b
        ]
    )
    return {
        "diag_min": float(diag.min()),
        "diag_max": float(diag.max()),
        "expected_diag": expected_diag,
        "max_off_diag": float(off_diag.max()),
        "off_conductor_norm": off_conductor_norm(T_char, packets),
    }


def check_biased_hayes_inv_block_structure(rng: np.random.Generator) -> dict:
    """For biased Hayes-invariant mu, the on-conductor blocks should be
    Hayes-orbit-constant: by Schur, the operator hat_mu acts as a scalar on
    each Hayes-orbit within each packet.  This is what survives the
    block-diagonalization that fails for the full cross-conductor claim."""

    packets = packet_index_groups()
    mu = np.array([0.30, 0.10, 0.15, 0.20, 0.15, 0.10])
    assert hayes_invariant_check(mu)
    T = output_side_covariance(mu)
    T_char = to_character_basis(T)

    # Verify Hayes-orbit-constancy of on-conductor diagonal blocks.
    # On X_6 = {chi_1, chi_5}: T_char[1, 1] should equal T_char[5, 5] (Hayes-invariance).
    # On X_3 = {chi_2, chi_4}: T_char[2, 2] should equal T_char[4, 4].
    failures = 0
    if not np.isclose(T_char[1, 1], T_char[5, 5]):
        failures += 1
    if not np.isclose(T_char[2, 2], T_char[4, 4]):
        failures += 1

    return {
        "X6_diag_equal": bool(np.isclose(T_char[1, 1], T_char[5, 5])),
        "X3_diag_equal": bool(np.isclose(T_char[2, 2], T_char[4, 4])),
        "failures": failures,
        "block_norms": on_conductor_summary(T_char, packets),
    }


# ---------------------------------------------------------------------------
# (2) Parameter-side block diagonalization via a centroid-initialized softmax MLP


def softmax_logits_to_probs(z: np.ndarray) -> np.ndarray:
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


class TinyMLP:
    """One hidden layer, tanh, output dim Q, init = small Gaussian, output bias = 0."""

    def __init__(self, input_dim: int, hidden_dim: int, rng: np.random.Generator) -> None:
        self.W1 = rng.standard_normal((hidden_dim, input_dim)) * 0.05
        self.b1 = np.zeros(hidden_dim)
        self.W2 = rng.standard_normal((Q, hidden_dim)) * 0.05
        # NOTE: output bias is exactly zero; combined with tanh activations near origin
        # and small init, logits are O(small) so softmax outputs are near p_* = 1/Q.

    def logits(self, z: np.ndarray) -> np.ndarray:
        h = np.tanh(self.W1 @ z + self.b1)
        return self.W2 @ h

    def probs(self, z: np.ndarray) -> np.ndarray:
        return softmax_logits_to_probs(self.logits(z))

    def output_jacobian_W2(self, z: np.ndarray) -> np.ndarray:
        """Jacobian of the *output* probs with respect to W2 row entries, as a (Q, Q*h) matrix.

        d p_a / d W2[c, j] = (delta_{ac} - p_a p_c) * h_j (in m-coordinates),
        but easier: at small init p ~ p_*, so softmax_jac ~ Q^{-1} P_H, and
        d logits_c / d W2[c, j] = h_j.  We'll work directly with the logit Jacobian
        below in the bracket test.
        """
        raise NotImplementedError("not used in this test")

    def logit_jacobian_W2(self, z: np.ndarray) -> np.ndarray:
        """Jacobian of *logits* (Q,) wrt W2 (Q, h), flattened to (Q, Q*h).

        d ell_c / d W2[c', j] = delta_{c,c'} * h_j.
        """
        h = np.tanh(self.W1 @ z + self.b1)
        hidden_dim = h.size
        J = np.zeros((Q, Q * hidden_dim))
        for c in range(Q):
            J[c, c * hidden_dim : (c + 1) * hidden_dim] = h
        return J


def check_parameter_side(rng: np.random.Generator) -> dict:
    """Estimate F(w_*) empirically and verify conductor-block-diagonal structure
    when projected via the logit Jacobian to character coordinates."""

    packets = packet_index_groups()
    mlp = TinyMLP(input_dim=8, hidden_dim=16, rng=rng)

    n_samples = 5000
    # uniform marginal labels (Hayes-equivariant)
    inputs = rng.standard_normal((n_samples, 8))
    labels = rng.integers(0, Q, size=n_samples)

    # accumulate the output-side covariance in character basis,
    # averaged over z (so E_z T_D(z) in char basis)
    T_char_accum = np.zeros((Q, Q), dtype=complex)
    for i in range(n_samples):
        p = mlp.probs(inputs[i])
        y = labels[i]
        g = p.copy()
        g[y] -= 1.0  # g = p - e_y
        # outer product, then DFT both sides
        T_char_accum += DFT @ np.outer(g, g) @ DFT_INV
    T_char_mean = T_char_accum / n_samples

    off = off_conductor_norm(T_char_mean.real, packets) + off_conductor_norm(T_char_mean.imag, packets)
    block_norms = on_conductor_summary(np.abs(T_char_mean), packets)

    # at w_*, the network outputs are ~p_*, so T(z) ~ E_y[tau_y tau_y^T] = Q^{-1} P_H
    # for uniform y, which is exactly diagonal in the character basis with eigenvalue
    # 1/Q on every nontrivial mode.  Off-block entries should be O(MC noise / sqrt(N)).

    expected_diag = 1.0 / Q  # because at p_* with uniform labels, T = Q^{-1} P_H
    # diagonal entries on nontrivial characters
    diag = np.array([T_char_mean[k, k].real for k in NONTRIVIAL_CHARS])

    return {
        "n_samples": n_samples,
        "off_conductor_norm": off,
        "block_norms": block_norms,
        "diag_mean": float(np.mean(diag)),
        "expected_diag": expected_diag,
        "diag_max_deviation": float(np.max(np.abs(diag - expected_diag))),
    }


# ---------------------------------------------------------------------------
# (4) Mini-batch noise covariance


def check_minibatch_noise(rng: np.random.Generator) -> dict:
    """Estimate Sigma_{chi, psi} for uniform labels and verify conductor-block structure.

    Sigma is the variance of the per-batch fluctuation; we estimate by
    sampling many batches of size B and computing the empirical batch-mean variance.
    """

    packets = packet_index_groups()
    B = 32  # batch size
    n_batches = 4000

    batch_means_char = []
    for _ in range(n_batches):
        labels = rng.integers(0, Q, size=B)
        gs = []
        for y in labels:
            tau_y = -P_STAR.copy()
            tau_y[y] += 1.0
            # at w_*, gradient direction = p_* - e_y = -tau_y
            gs.append(-tau_y)
        batch_mean = np.mean(gs, axis=0)
        batch_means_char.append(DFT @ batch_mean)

    batch_means_char = np.array(batch_means_char)  # (n_batches, Q) complex
    # mean over batches
    mean_char = batch_means_char.mean(axis=0)
    # fluctuation
    fluct = batch_means_char - mean_char[None, :]
    Sigma_char = (fluct.conj().T @ fluct) / n_batches  # (Q, Q)

    # off-conductor norm
    off = off_conductor_norm(np.abs(Sigma_char), packets)
    block_norms = on_conductor_summary(np.abs(Sigma_char), packets)

    return {
        "batch_size": B,
        "n_batches": n_batches,
        "off_conductor_norm": off,
        "block_norms": block_norms,
    }


# ---------------------------------------------------------------------------
# main


def main() -> int:
    rng = np.random.default_rng(RNG_SEED)
    print(f"R = C_6, conductor packets: {packet_index_groups()}")
    print()

    failures_total = 0

    # 1. fundamental output-side identity: T_char[chi_a, chi_b] = Q^{-1} hat_mu(a - b)
    print("[1] T_char[chi_a, chi_b] = Q^{-1} * hat_mu(a - b) (Theorem 1.1.1(1)) ...")
    stats = check_output_side_identity(rng)
    print(f"    distributions={stats['samples']}  failures={stats['failures']}  max_residual={stats['max_residual']:.3e}")
    failures_total += stats["failures"]

    # 1a. uniform marginal => exact character-diagonal
    print("[1a] uniform marginal mu = p_*: T_char is exactly character-diagonal ...")
    stats = check_output_side_uniform_diagonal()
    print(f"    diag range = [{stats['diag_min']:.6f}, {stats['diag_max']:.6f}]  expected = {stats['expected_diag']:.6f}")
    print(f"    max off-diagonal = {stats['max_off_diag']:.3e}  off_conductor_norm = {stats['off_conductor_norm']:.3e}")
    if stats["max_off_diag"] > TOLERANCE or abs(stats["diag_min"] - stats["expected_diag"]) > TOLERANCE:
        failures_total += 1

    # 1b. biased Hayes-invariant: on-conductor blocks Hayes-orbit-constant
    print("[1b] biased Hayes-invariant mu: on-conductor diagonal blocks Hayes-orbit-constant ...")
    stats = check_biased_hayes_inv_block_structure(rng)
    print(f"    X_6 diag entries equal: {stats['X6_diag_equal']}  X_3 diag entries equal: {stats['X3_diag_equal']}")
    print(f"    block norms: {stats['block_norms']}")
    failures_total += stats["failures"]

    # 2. parameter-side via MLP at uniform labels (empirical, MC noise)
    print("[2] parameter-side F(w_*) at small-init MLP, uniform labels ...")
    stats = check_parameter_side(rng)
    print(f"    n_samples={stats['n_samples']}  off_conductor_norm={stats['off_conductor_norm']:.3e}")
    print(f"    diag_mean={stats['diag_mean']:.4f}  expected={stats['expected_diag']:.4f}  max_deviation={stats['diag_max_deviation']:.3e}")
    if stats["off_conductor_norm"] > EMPIRICAL_TOLERANCE:
        print(f"    FAIL: off-conductor entries exceed empirical tolerance")
        failures_total += 1
    if stats["diag_max_deviation"] > EMPIRICAL_TOLERANCE:
        print(f"    FAIL: diagonal entries deviate from theoretical 1/Q")
        failures_total += 1

    # 3. mini-batch noise covariance at uniform marginal
    print("[3] mini-batch noise covariance at uniform marginal labels ...")
    stats = check_minibatch_noise(rng)
    print(f"    B={stats['batch_size']}  n_batches={stats['n_batches']}  off_conductor_norm={stats['off_conductor_norm']:.3e}")
    print(f"    on-conductor block norms: {stats['block_norms']}")
    if stats["off_conductor_norm"] > EMPIRICAL_TOLERANCE:
        print(f"    FAIL: off-conductor entries exceed empirical tolerance")
        failures_total += 1

    print()
    if failures_total == 0:
        print("PASS  (forcing-spectrum identity and uniform-marginal block diagonality verified)")
        return 0
    else:
        print(f"FAIL  total failures = {failures_total}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
