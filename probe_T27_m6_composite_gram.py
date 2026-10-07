"""
probe_T27_m6_composite_gram.py
================================

Composite-rung diagnostic at m=6 vs the prime rungs m=2, m=3 at N=30.

Hypothesis: composite m=6 (prime factors 2 and 3) might show RICHER
eigenstructure than the cyclic prime cases m=2, m=3 due to prime-factor
interference in the Galois content of K_N^(6) = compositum(K_N^(2), K_N^(3)).

Galois degrees at N=30:
  [K_30^(2):Q] = 2^10 = 1024
  [K_30^(3):Q] = 2 * 3^10 = 118098
  [K_30^(6):Q] = 2 * 6^10 = 120932352

m=6 has 1000x richer field than m=3 — does this richness manifest in G^(6)?

Output:
  - Side-by-side eigenvalue spectra m=2, 3, 6.
  - Cross-rung eigenvector overlaps (does m=6 eigenbasis align with m=2 or m=3?).
  - Bimodal/multimodal structure tests on G^(6) spectrum.
  - Dirichlet character alignment.
  - Approximation as scalar*I deviation.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import time
import numpy as np
from mpmath import mp, mpf, mpc, exp, pi
mp.dps = 50


# =========================================================================
# Setup
# =========================================================================

N = 30
n = N - 1

print("=" * 78)
print(f" Composite-Rung Probe: m=6 vs m=2, m=3 at N={N}")
print("=" * 78)
print(f" Dimension: {n} x {n}")
print()

omega = exp(mpc(0, 1) * 2 * pi / mpf(N))


# =========================================================================
# Compute Helmert-Fourier coefficients
# =========================================================================

print("Computing Helmert-Fourier coefficients C_{kc}...")
t0 = time.time()
C_mp = [[mpc(0, 0) for _ in range(n)] for _ in range(n)]
for k_idx in range(n):
    k = k_idx + 1
    for c_idx in range(n):
        c = c_idx + 1
        omc = omega ** mpf(c)
        s_sum = mpc(0, 0)
        w = mpc(1, 0)
        for _ in range(k):
            w = w * omc
            s_sum += w
        last = w * omc
        C_mp[k_idx][c_idx] = s_sum - mpf(k) * last
print(f"  done in {time.time() - t0:.1f}s")

C = np.array([[complex(C_mp[i][j]) for j in range(n)] for i in range(n)])


# =========================================================================
# Helmert radicals at m = 2, 3, 6
# =========================================================================

def R_k_m(k, N, m):
    """R_k^(m) = 1/(N * (k + k^m))^(1/m).

    Derived from ||h_k||_m^m = k + k^m (the L^m norm of h_k = (1,...,1,-k,0,...))
    and ||chi_c||_m^m = N (since |chi_c(s)| = 1 for all s, sum of N ones)."""
    val = mpf(N) * (mpf(k) + mpf(k) ** m)
    return mpf(1) / val ** (mpf(1) / m)


R2 = np.array([float(R_k_m(k+1, N, 2)) for k in range(n)])
R3 = np.array([float(R_k_m(k+1, N, 3)) for k in range(n)])
R6 = np.array([float(R_k_m(k+1, N, 6)) for k in range(n)])

print(f"\nHelmert radicals R_k^(m) at sampled k:")
print(f"  {'k':>3}  {'R^(2)':>14}  {'R^(3)':>14}  {'R^(6)':>14}")
for k_idx in [0, 1, 4, 9, 14, 19, 28]:
    print(f"  {k_idx+1:>3}  {R2[k_idx]:>14.8f}  {R3[k_idx]:>14.8f}  {R6[k_idx]:>14.8f}")


# =========================================================================
# Build U^(m) and G^(m) = U^(m)* U^(m)
# =========================================================================

def build_G(R_array, C):
    U = R_array[:, np.newaxis] * C
    G = U.conj().T @ U
    return (G + G.conj().T) / 2  # Hermitize numerically


G2 = build_G(R2, C)
G3 = build_G(R3, C)
G6 = build_G(R6, C)

# Sanity check
err = np.linalg.norm(G2 - np.eye(n))
print(f"\nSanity check ||G^(2) - I||_F = {err:.4e} (expect ~0)")


# =========================================================================
# Eigenstructures
# =========================================================================

eigs2, vecs2 = np.linalg.eigh(G2)
eigs3, vecs3 = np.linalg.eigh(G3)
eigs6, vecs6 = np.linalg.eigh(G6)

eigs2 = eigs2.real
eigs3 = eigs3.real
eigs6 = eigs6.real

print("\n" + "-" * 78)
print(" Side-by-side eigenvalue spectra (sorted ascending)")
print("-" * 78)
print(f"  {'idx':>3}  {'lambda^(2)':>14}  {'lambda^(3)':>14}  {'lambda^(6)':>14}")
for i in range(n):
    print(f"  {i:>3}  {eigs2[i]:>14.8f}  {eigs3[i]:>14.8f}  {eigs6[i]:>14.8f}")

print(f"\n  Summary statistics:")
print(f"  {'rung':>6}  {'min':>14}  {'max':>14}  {'mean':>14}  {'std':>10}  {'cond':>10}")
for label, eigs in [("m=2", eigs2), ("m=3", eigs3), ("m=6", eigs6)]:
    print(f"  {label:>6}  {min(eigs):>14.6f}  {max(eigs):>14.6f}  "
          f"{np.mean(eigs):>14.6f}  {np.std(eigs):>10.6f}  "
          f"{max(eigs)/min(eigs):>10.4f}")


# =========================================================================
# Deviation from scalar identity
# =========================================================================

print("\n" + "-" * 78)
print(" Approximation as scalar * I")
print("-" * 78)
print(f"  {'rung':>6}  {'scalar':>14}  {'||G - cI||_F':>16}  {'rel deviation':>16}")
for label, G in [("m=2", G2), ("m=3", G3), ("m=6", G6)]:
    c = np.trace(G).real / n
    dev = np.linalg.norm(G - c * np.eye(n))
    rel = dev / np.linalg.norm(G)
    print(f"  {label:>6}  {c:>14.6f}  {dev:>16.6f}  {rel:>16.6f}")


# =========================================================================
# Eigenvalue spread analysis
# =========================================================================

print("\n" + "-" * 78)
print(" Spread analysis: max/min ratio and IQR")
print("-" * 78)
for label, eigs in [("m=2", eigs2), ("m=3", eigs3), ("m=6", eigs6)]:
    sorted_e = sorted(eigs)
    iqr = sorted_e[3*len(sorted_e)//4] - sorted_e[len(sorted_e)//4]
    print(f"  {label}: max/min = {max(eigs)/min(eigs):.4f}, "
          f"max-min = {max(eigs)-min(eigs):.4f}, IQR = {iqr:.4f}")


# =========================================================================
# Bimodal/multimodal structure detection
# =========================================================================

print("\n" + "-" * 78)
print(" Multimodal structure in G^(6) spectrum")
print("-" * 78)

sorted_eigs6 = sorted(eigs6)
gaps6 = np.array([sorted_eigs6[i+1] - sorted_eigs6[i] for i in range(len(sorted_eigs6)-1)])
mean_gap = np.mean(gaps6)
max_gap_idx = np.argmax(gaps6)
max_gap = gaps6[max_gap_idx]

print(f"  Mean consecutive gap: {mean_gap:.6f}")
print(f"  Max gap: {max_gap:.6f} (between idx {max_gap_idx} and {max_gap_idx+1})")
print(f"  Max/mean gap ratio: {max_gap/mean_gap:.2f}x")
print(f"  Eigenvalue at gap boundary: {sorted_eigs6[max_gap_idx]:.4f}, "
      f"{sorted_eigs6[max_gap_idx+1]:.4f}")

# Look for gaps > 2x mean (potential cluster boundaries)
big_gaps = [(i, g) for i, g in enumerate(gaps6) if g > 2 * mean_gap]
if big_gaps:
    print(f"  Gaps exceeding 2x mean: {len(big_gaps)}")
    for i, g in big_gaps:
        print(f"    Index {i}: gap = {g:.6f} ({g/mean_gap:.2f}x mean)")
else:
    print("  No gaps exceeding 2x mean — smooth spectrum, no clusters")


# =========================================================================
# Cross-rung eigenvector overlaps
# =========================================================================

print("\n" + "-" * 78)
print(" Cross-rung eigenvector overlaps")
print("-" * 78)

# How well do G^(3) eigenvectors diagonalize G^(6)? (sanity for m_1 | m_2 hypothesis)
print("\n  G^(3) eigenvectors diagonalize G^(6)?")
diag6_in_3 = np.diag(vecs3.conj().T @ G6 @ vecs3).real
off6_in_3 = G6 - np.diag(diag6_in_3)  # NOT QUITE - this is wrong basis
# Actually compute G^(6) in v^(3) basis:
G6_in_basis_3 = vecs3.conj().T @ G6 @ vecs3
off_diag_norm = np.linalg.norm(G6_in_basis_3 - np.diag(np.diag(G6_in_basis_3)))
diag_norm = np.linalg.norm(np.diag(G6_in_basis_3))
print(f"  ||off-diag of G^(6) in v^(3) basis|| / ||diag|| = "
      f"{off_diag_norm/diag_norm:.4e}")
print(f"  (if small: G^(3) and G^(6) are nearly simultaneously diagonalized)")

# How about G^(2) (= I, all bases work) vs G^(6)?
print(f"\n  G^(6) diagonal entries in std additive-character basis:")
diag6 = np.diag(G6).real
print(f"    range: [{min(diag6):.4f}, {max(diag6):.4f}]")
print(f"    std: {np.std(diag6):.4f}")
G6_minus_diag = G6 - np.diag(diag6)
print(f"    ||off-diag of G^(6) in std basis|| = {np.linalg.norm(G6_minus_diag):.4f}")
print(f"    ||G^(6)||_F = {np.linalg.norm(G6):.4f}")
print(f"    relative off-diag = {np.linalg.norm(G6_minus_diag)/np.linalg.norm(G6):.4e}")


# =========================================================================
# Dirichlet character alignment
# =========================================================================

print("\n" + "-" * 78)
print(" Dirichlet character alignment with G^(6) eigenvectors")
print("-" * 78)

units_mod_30 = [1, 7, 11, 13, 17, 19, 23, 29]


def discrete_log_Z30(u):
    """Return (a, b) such that u = 7^a * 11^b mod 30."""
    for a in range(4):
        for b in range(2):
            if (pow(7, a, 30) * pow(11, b, 30)) % 30 == u:
                return (a, b)
    raise ValueError(u)


unit_coords = {u: discrete_log_Z30(u) for u in units_mod_30}

characters = []
for alpha in range(4):
    for beta in range(2):
        char_vals = {u: np.exp(1j * 2 * np.pi * (alpha * unit_coords[u][0] / 4 +
                                                  beta * unit_coords[u][1] / 2))
                     for u in units_mod_30}
        characters.append((alpha, beta, char_vals))


def char_vec(char_vals):
    v = np.zeros(n, dtype=complex)
    for c in range(1, N):
        if c in char_vals:
            v[c - 1] = char_vals[c]
    return v / np.linalg.norm(v)


dirichlet_vecs = [(a, b, char_vec(vals)) for (a, b, vals) in characters]

print(f"  {'(alpha,beta)':>14}  {'G^(3) best':>22}  {'G^(6) best':>22}")
for (a, b, cv) in dirichlet_vecs:
    ovlp3 = [abs(np.vdot(vecs3[:, i], cv))**2 for i in range(n)]
    ovlp6 = [abs(np.vdot(vecs6[:, i], cv))**2 for i in range(n)]
    b3 = np.argmax(ovlp3)
    b6 = np.argmax(ovlp6)
    print(f"       ({a},{b})  v_{b3:>2} @ {ovlp3[b3]:>6.3f} (lam={eigs3[b3]:.3f})  "
          f"v_{b6:>2} @ {ovlp6[b6]:>6.3f} (lam={eigs6[b6]:.3f})")


# =========================================================================
# Decomposition by prime divisors (the key composite-rung test)
# =========================================================================

print("\n" + "-" * 78)
print(" KEY TEST: Does G^(6) decompose by prime factors 2,3?")
print("-" * 78)

# Hypothesis: G^(6) ~ alpha * G^(2)-component + beta * G^(3)-component + cross
# Test: project G^(6) onto rank-1 directions defined by G^(2)=I and G^(3) eigenstructure.

# Test: is G^(6) a linear combination of G^(2)=I and G^(3)?
# Find best (a, b) such that G^(6) ~ a*I + b*G^(3)
# Least squares on flattened matrices
G2_flat = np.eye(n).flatten()
G3_flat = G3.flatten()
G6_flat = G6.flatten()

# Solve G6 = a*I + b*G3 + residual
M = np.column_stack([G2_flat.real, G3_flat.real])
b_vec = G6_flat.real
sol, residuals, rank, sv = np.linalg.lstsq(M, b_vec, rcond=None)
a_fit, b_fit = sol
predicted = a_fit * np.eye(n) + b_fit * G3
residual_matrix = G6 - predicted

print(f"  Best fit G^(6) = a*I + b*G^(3):")
print(f"    a = {a_fit:.6f}")
print(f"    b = {b_fit:.6f}")
print(f"    ||residual||_F = {np.linalg.norm(residual_matrix):.6f}")
print(f"    ||G^(6)||_F = {np.linalg.norm(G6):.6f}")
print(f"    relative residual = {np.linalg.norm(residual_matrix)/np.linalg.norm(G6):.4e}")

if np.linalg.norm(residual_matrix) / np.linalg.norm(G6) < 0.01:
    print(f"    ==> G^(6) is essentially a linear combination of G^(2) and G^(3).")
    print(f"        Composite rung adds NO new structure beyond the prime rungs.")
else:
    print(f"    ==> G^(6) has independent content beyond G^(2), G^(3).")
    print(f"        Composite rung CARRIES the prime-factor interference structure.")


# =========================================================================
# Summary
# =========================================================================

print("\n" + "=" * 78)
print(" Summary")
print("=" * 78)
print(f"""
At N={N}:
  - G^(2) = I (T9 unitarity, deviation = {np.linalg.norm(G2-np.eye(n)):.2e}).
  - G^(3): scalar-like, eigenvalues [{min(eigs3):.3f}, {max(eigs3):.3f}], cond={max(eigs3)/min(eigs3):.3f}.
  - G^(6): eigenvalues [{min(eigs6):.3f}, {max(eigs6):.3f}], cond={max(eigs6)/min(eigs6):.3f}.

The KEY QUESTION: does G^(6) add structure beyond G^(2) + G^(3)?

Answer (from least-squares decomposition above):
  relative residual = {np.linalg.norm(residual_matrix)/np.linalg.norm(G6):.4e}

If << 0.01: composite rung is trivial; the gauge ladder doesn't accumulate new content.
If >> 0.01: composite rung carries genuine prime-factor interference; ladder works.

Implications for the [A3'] ladder aggregation hypothesis:
  - Trivial composite = ladder collapses to prime-rung family, aggregation gives nothing new.
  - Non-trivial composite = ladder has cross-rung interaction, aggregation might close [A3'].
""")
