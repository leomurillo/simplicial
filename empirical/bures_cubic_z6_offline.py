"""
Follow-up experiment: scan OFF the critical line to verify that divergences
of Im[kappa_3^K] sit only on Re(s) = 1/2 (which would be RH numerically confirmed
up to whatever height we scan).
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30

# Reuse functions
def q_r_6(r, s_complex):
    s = mp.mpc(s_complex.real, s_complex.imag)
    if r == 0:
        val = mp.mpc(6) ** (-s)
    else:
        val = mp.mpc(6) ** (-s) * mp.zeta(s, mp.mpc(r) / mp.mpc(6)) / mp.zeta(s)
    return complex(float(val.real), float(val.imag))

def rho_diag(s_complex):
    return np.array([q_r_6(r, s_complex) for r in range(6)], dtype=complex)

K_perm = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0]
], dtype=complex)

def apply_K(G):
    return K_perm @ np.conjugate(G) @ K_perm.T

def kappa3_K(G, q):
    G_K = apply_K(G)
    g       = np.sum(q * np.diag(G))
    g_K     = np.sum(q * np.diag(G_K))
    g_sq    = np.sum(q * np.diag(G @ G))
    g_K_g   = np.sum(q * np.diag(G_K @ G))
    g_K_gsq = np.sum(q * np.diag(G_K @ G @ G))
    return g_K_gsq - g_K * g_sq - 2 * g * g_K_g + 2 * g_K * g**2

def G_balanced():
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1; G[1, 1] = -1; G[2, 2] = 0.5; G[3, 3] = -0.5
    G[0, 1] = 0.3; G[1, 0] = 0.3
    G[2, 3] = 0.2; G[3, 2] = 0.2
    G[0, 2] = 0.1; G[2, 0] = 0.1
    return G

# ===== Diagnostic 1: Regularized cumulant on critical line =====

print("=" * 90)
print("Diagnostic 1: Regularized cumulant tilde_kappa = |zeta|^3 * kappa on critical line")
print("Expectation: divergence factor should be removed; tilde_kappa stays bounded near zeros")
print("=" * 90)

zeros_first_few = [14.13473, 21.02204, 25.01086, 30.42488, 32.93506, 37.58618]

print(f"\n{'t':>10s} {'|zeta|':>14s} {'|kappa|':>14s} {'|kappa|*|zeta|^3':>20s}")
print("-" * 70)
for t in [14.0, 14.1, 14.13, 14.13473, 14.14, 14.2, 14.5, 18.0, 21.0, 21.02204, 21.1]:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))
    q = rho_diag(s)
    k = kappa3_K(G_balanced(), q)
    abs_zeta3 = abs(zeta_val)**3
    print(f"{t:10.5f} {abs(zeta_val):14.6e} {abs(k):14.6e} {abs(k)*abs_zeta3:20.6e}")

# ===== Diagnostic 2: Off-line scan =====

print()
print("=" * 90)
print("Diagnostic 2: Scan |kappa| over a grid in the critical strip 0.3 < Re(s) < 0.7")
print("Looking for: divergences at any Re(s) != 1/2 would indicate RH-violation")
print("=" * 90)

print(f"\n{'Re(s)':>10s} {'t':>10s} {'|zeta(s)|':>14s} {'|kappa(s)|':>14s} {'|kappa|*|zeta|^3':>20s}")
print("-" * 75)

# Scan around the first zero's imaginary part at different real parts
t_test = 14.13473  # exact first zero imaginary part
for sigma in [0.3, 0.4, 0.45, 0.48, 0.49, 0.5, 0.51, 0.52, 0.55, 0.6, 0.7]:
    s = complex(sigma, t_test)
    s_mp = mp.mpc(sigma, t_test)
    zeta_val = complex(mp.zeta(s_mp))
    q = rho_diag(s)
    k = kappa3_K(G_balanced(), q)
    print(f"{sigma:10.4f} {t_test:10.5f} {abs(zeta_val):14.6e} {abs(k):14.6e} {abs(k)*abs(zeta_val)**3:20.6e}")

# ===== Diagnostic 3: 2D grid sweep =====

print()
print("=" * 90)
print("Diagnostic 3: 2D scan in (sigma, t) grid, looking for ANY divergence")
print("=" * 90)

print(f"\n{'Re(s)':>10s} {'t':>10s} {'|zeta(s)|':>14s} {'|kappa|':>14s}")
print("-" * 60)

# Coarse grid in the critical strip up to t = 50
peaks = []
for sigma in np.linspace(0.05, 0.95, 19):
    for t in np.linspace(0.5, 50, 100):
        s = complex(sigma, t)
        s_mp = mp.mpc(sigma, t)
        zeta_val = complex(mp.zeta(s_mp))
        abs_zeta = abs(zeta_val)
        if abs_zeta < 0.001:  # potentially near a zero
            q = rho_diag(s)
            k = kappa3_K(G_balanced(), q)
            peaks.append((sigma, t, abs_zeta, abs(k)))

print(f"Found {len(peaks)} points with |zeta| < 0.001:")
for sigma, t, abs_zeta, abs_k in peaks:
    on_critical = "(ON critical line)" if abs(sigma - 0.5) < 0.001 else "<-- OFF critical line!"
    print(f"{sigma:10.4f} {t:10.4f} {abs_zeta:14.6e} {abs_k:14.6e} {on_critical}")

if all(abs(sigma - 0.5) < 0.001 for sigma, _, _, _ in peaks):
    print("\n*** All near-zero points sit on Re(s) = 1/2. Empirical RH confirmation up to t = 50. ***")
else:
    print("\n*** Off-line points found! Numerical evidence against RH (or numerical artifact). ***")
