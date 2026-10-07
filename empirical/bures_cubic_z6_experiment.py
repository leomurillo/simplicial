"""
Empirical test of the Bures Cubic Imaginary Trace Criterion (BCITC) for RH.

For the residue-projected zeta distribution on Z/6 at parameter s = 1/2 + it,
compute the K-twisted cubic cumulant of test operators and report its imaginary part.

Conjecture: Im[kappa_3^K(G; s)] has structure tied to non-trivial zeros of zeta.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30  # 30 digits precision for mpmath

# ===== Residue-projected zeta distribution =====

def q_r_6(r, s_complex):
    """
    q_r^(6)(s) = (1/zeta(s)) * sum_{m equiv r mod 6, m >= 1} m^{-s}
              = (1/zeta(s)) * 6^{-s} * zeta(s, r/6)  for r=1..5
              = 6^{-s}                                for r=0
    Uses analytic continuation via Hurwitz zeta.
    """
    s = mp.mpc(s_complex.real, s_complex.imag)
    if r == 0:
        val = mp.mpc(6) ** (-s)
    else:
        val = mp.mpc(6) ** (-s) * mp.zeta(s, mp.mpc(r) / mp.mpc(6)) / mp.zeta(s)
    return complex(float(val.real), float(val.imag))

def rho_diag(s_complex):
    """Diagonal entries of rho(s)."""
    return np.array([q_r_6(r, s_complex) for r in range(6)], dtype=complex)

# ===== Canonical involution K =====
# K acts on Z/6 by r -> -r mod 6, combined with complex conjugation.
# Permutation: 0->0, 1->5, 2->4, 3->3, 4->2, 5->1.

K_perm = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0]
], dtype=complex)

def apply_K(G):
    """K G K^{-1} for anti-unitary K = K_perm . J (J = complex conjugation)."""
    return K_perm @ np.conjugate(G) @ K_perm.T

# ===== K-twisted third cumulant =====

def trace_diag_rho(M, q):
    """Tr(diag(q) @ M) = sum_i q_i * M_{ii}."""
    return np.sum(q * np.diag(M))

def kappa3_K(G, q):
    """
    K-twisted third cumulant of Hermitian operator G at diagonal rho(s).

    kappa_3^K(G) := Tr(rho G^K G G) - <G^K> <G^2> - 2 <G> <G^K G> + 2 <G^K> <G>^2
    """
    G_K = apply_K(G)

    g       = trace_diag_rho(G, q)
    g_K     = trace_diag_rho(G_K, q)
    g_sq    = trace_diag_rho(G @ G, q)
    g_K_g   = trace_diag_rho(G_K @ G, q)
    g_K_gsq = trace_diag_rho(G_K @ G @ G, q)

    return g_K_gsq - g_K * g_sq - 2 * g * g_K_g + 2 * g_K * g**2

# ===== Test operators =====

def G_diag_proj0():
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1
    return G

def G_diag_proj1():
    G = np.zeros((6, 6), dtype=complex)
    G[1, 1] = 1
    return G

def G_mixed():
    """Mixed diagonal + off-diagonal, K-non-fixed."""
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1
    G[0, 1] = 1
    G[1, 0] = 1
    return G

def G_balanced():
    """A more complex test op with multiple off-diagonals."""
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1; G[1, 1] = -1; G[2, 2] = 0.5; G[3, 3] = -0.5
    G[0, 1] = 0.3; G[1, 0] = 0.3
    G[2, 3] = 0.2; G[3, 2] = 0.2
    G[0, 2] = 0.1; G[2, 0] = 0.1
    return G

def G_K_pair():
    """Off-diagonal connecting K-pair (1,5)."""
    G = np.zeros((6, 6), dtype=complex)
    G[1, 5] = 1
    G[5, 1] = 1
    return G

def G_non_K_pair():
    """Off-diagonal NOT connecting K-pair, e.g. (1,2)."""
    G = np.zeros((6, 6), dtype=complex)
    G[1, 2] = 1
    G[2, 1] = 1
    return G

# ===== Experiment 1: Sanity check at s = 2 =====

print("=" * 90)
print("Experiment 1: Sanity check at s = 2.0 (real, > 1)")
print("Expected: kappa3_K is REAL (Hermiticity of rho).")
print("=" * 90)
s = complex(2.0, 0.0)
q = rho_diag(s)
print(f"\nq(2) = [")
for r in range(6):
    print(f"  q[{r}] = {q[r].real:.6f} + {q[r].imag:.6e}j")
print(f"]")
print(f"Sum = {sum(q).real:.6f} + {sum(q).imag:.2e}j")
print()
print(f"{'Operator':<20s} {'Re[kappa3_K]':>16s} {'Im[kappa3_K]':>16s}")
for name, G in [
    ("G_diag_proj0", G_diag_proj0()),
    ("G_diag_proj1", G_diag_proj1()),
    ("G_mixed", G_mixed()),
    ("G_balanced", G_balanced()),
    ("G_K_pair", G_K_pair()),
    ("G_non_K_pair", G_non_K_pair()),
]:
    k = kappa3_K(G, q)
    print(f"{name:<20s} {k.real:16.4e} {k.imag:16.4e}")

# ===== Experiment 2: Sweep critical line =====

print()
print("=" * 90)
print("Experiment 2: Sweep s = 1/2 + i*t along the critical line")
print("Investigating: does Im[kappa3_K] have structure near zeta-zeros?")
print("First few non-trivial zeros: t = 14.1347, 21.0220, 25.0109, 30.4249, 32.9351")
print("=" * 90)

# Include known zeros + grid + boundary points
zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862]
grid = list(np.linspace(0.5, 40, 81))
t_vals = sorted(set([round(t, 4) for t in grid + zeros]))

print()
print(f"{'t':>8s} {'|zeta|':>10s} {'Im[k(G_diag_proj0)]':>22s} {'Im[k(G_mixed)]':>22s} {'Im[k(G_balanced)]':>22s}")
print("-" * 90)

results = []
for t in t_vals:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))
    q = rho_diag(s)

    k_a = kappa3_K(G_diag_proj0(), q)
    k_m = kappa3_K(G_mixed(), q)
    k_b = kappa3_K(G_balanced(), q)

    results.append((t, abs(zeta_val), k_a.imag, k_m.imag, k_b.imag))

    marker = " <-- near zero" if any(abs(t - z) < 0.05 for z in zeros) else ""
    print(f"{t:8.4f} {abs(zeta_val):10.4e} {k_a.imag:22.6e} {k_m.imag:22.6e} {k_b.imag:22.6e}{marker}")

# ===== Experiment 3: high-resolution near a zero =====

print()
print("=" * 90)
print("Experiment 3: High-resolution near the first non-trivial zero (t = 14.1347)")
print("=" * 90)
print()
print(f"{'t':>10s} {'|zeta|':>14s} {'Re[k(G_balanced)]':>20s} {'Im[k(G_balanced)]':>20s}")
print("-" * 70)
for t in np.linspace(14.10, 14.17, 30):
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))
    q = rho_diag(s)
    k = kappa3_K(G_balanced(), q)
    marker = " <-- ZETA ZERO" if abs(t - 14.1347) < 0.001 else ""
    print(f"{t:10.5f} {abs(zeta_val):14.6e} {k.real:20.6e} {k.imag:20.6e}{marker}")

print()
print("=" * 90)
print("Summary:")
print("- Experiment 1 (s=2): Im should be ~0 by Hermiticity")
print("- Experiment 2 (critical line): scan for structure")
print("- Experiment 3 (near first zero): zoom in on potential signature")
print("=" * 90)
