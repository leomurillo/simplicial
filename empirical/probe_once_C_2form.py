"""
Probe ONCE-C: The 2-form omega_K = dB_G ∧ dB_GK and contour integrals.

Pursues option (C): the cluster as a curved 2-form on Z/6.

For K-antisymmetric G: B_GK = -B_G identically, so naive d B_G ∧ d B_GK = 0.

The non-trivial version (using complex-conjugate differentials):
   omega_K_real := dB_G ∧ d conj(B_GK) + conj-conj   (real 2-form on C)

In real coordinates s = sigma + i*t:
   omega_K_real = 4 |B_G'(s)|^2 d sigma ∧ dt   (for K-antisymmetric G)

Integral over cluster Lambda(rho) = rectangle of width 2*delta, height 2*gamma_0:
   I(rho) := integral_Lambda omega_K_real

Properties:
- On-line (delta=0): I = 0 (rectangle has zero width).
- Off-line (delta>0): I > 0, scales as delta * (integrated |B_G'|^2).

This 2-form INTEGRAL DISCRIMINATES on-line from off-line.

The Cauchy-style residue interpretation: via the argument principle,
   contour integral_{partial Lambda} B_G(s) * zeta'(s)/zeta(s) ds = 2pi*i * sum over zeros in Lambda of B_G(rho_v)

For on-line cluster: 2 distinct zeros, sum = 2 (B_G(rho) + B_G(bar rho)) = 4 Re B_G(rho).
For off-line cluster: 4 distinct zeros, sum = sum_v B_G(rho_v).

We compute both and report.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30

GAMMA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935062587739189,
]

G_balanced = [1.0, 1.0, 0.5, 0.0, -0.5, -1.0]

def G_K(G):
    return [G[0], G[5], G[4], G[3], G[2], G[1]]

def B_G(s, G):
    s_mp = mp.mpc(s.real, s.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += mp.mpc(G[r]) * mp.zeta(s_mp, mp.mpf(r) / mp.mpf(6))
    val *= mp.mpc(6) ** (-s_mp)
    return complex(val)

def B_G_deriv(s, G):
    """Numerical derivative of B_G in s (along real axis)."""
    h = 1e-5
    return (B_G(s + h, G) - B_G(s - h, G)) / (2 * h)

# ===== The 2-form integral over the cluster =====

def cluster_2form_integral(delta, gamma0, G=G_balanced, n_grid=20):
    """
    Integrate |B_G'(s)|^2 over the cluster rectangle Lambda(rho).
    Returns 4 * integral as the "real 2-form" value.
    """
    if delta < 1e-10:
        return 0.0

    sigma_min, sigma_max = 0.5 - delta, 0.5 + delta
    t_min, t_max = -gamma0, gamma0

    sigmas = np.linspace(sigma_min, sigma_max, n_grid)
    ts = np.linspace(t_min, t_max, 2 * n_grid)  # more in t since range is much larger

    dsigma = sigmas[1] - sigmas[0] if n_grid > 1 else 2 * delta
    dt = ts[1] - ts[0] if 2 * n_grid > 1 else 2 * gamma0 / (2 * n_grid)

    total = 0.0
    for sigma in sigmas:
        for t in ts:
            s = complex(sigma, t)
            BG_p = B_G_deriv(s, G)
            total += abs(BG_p)**2

    integral = 4 * total * dsigma * dt
    return integral

# ===== The Cauchy contour integral via argument principle =====

def cauchy_sum_BG(delta, gamma0, G=G_balanced):
    """
    By the argument principle:
       (1/(2pi*i)) oint_{partial Lambda} B_G(s) zeta'/zeta ds = sum_{zeros in Lambda} B_G(rho)

    For on-line cluster (delta=0): if there's exactly one ζ-zero at rho=1/2+i*gamma_0
    inside Lambda, sum = B_G(rho) + B_G(bar rho) = 2 Re B_G(rho).

    For off-line cluster (delta>0, hypothetical): if 4 zeros are inside (4 cluster vertices),
    sum = sum_v B_G(rho_v).

    We compute this sum directly (no contour integration needed -- we know the cluster
    vertices and B_G at each).
    """
    if delta < 1e-10:
        # On-line: cluster degenerates to {rho, bar rho}
        rho = complex(0.5, gamma0)
        return 2 * (B_G(rho, G) + B_G(rho.conjugate(), G))
        # Factor of 2 because each vertex appears twice in the degenerate cluster
    else:
        # Off-line: 4 distinct cluster vertices
        cluster = [
            complex(0.5 + delta, +gamma0),
            complex(0.5 - delta, +gamma0),
            complex(0.5 + delta, -gamma0),
            complex(0.5 - delta, -gamma0),
        ]
        return sum(B_G(rho_v, G) for rho_v in cluster)

# ===== Run =====

print("=" * 90)
print("Probe ONCE-C: 2-form omega_K and Cauchy-style invariants")
print("=" * 90)

print("\n--- 2-form integral I(rho) = 4 * integral |B_G'|^2 over Lambda(rho) ---")
print("Expected: 0 on-line, >0 off-line (discriminates delta)")
print(f"\n{'delta':>8s} {'gamma_0':>10s} {'I(rho)':>16s}")
print("-" * 40)

for gamma0 in GAMMA_ZEROS[:3]:  # first 3 zeros, computational cost
    for delta in [0.0, 0.01, 0.05, 0.1]:
        I = cluster_2form_integral(delta, gamma0, n_grid=10)
        print(f"{delta:8.3f} {gamma0:10.4f} {I:16.6e}")

print()
print("--- Cauchy argument-principle sum (sum of B_G over cluster zeros) ---")
print(f"\n{'delta':>8s} {'gamma_0':>10s} {'Re sum':>14s} {'Im sum':>14s}")
print("-" * 50)

for gamma0 in GAMMA_ZEROS:
    for delta in [0.0, 0.1, 0.2]:
        S = cauchy_sum_BG(delta, gamma0)
        print(f"{delta:8.3f} {gamma0:10.4f} {S.real:14.6e} {S.imag:14.6e}")

# ===== The structural identity to check =====

print()
print("=" * 90)
print("Structural test: is the Cauchy sum at every nontrivial zero rho")
print("FORCED to be zero by some topological constraint?")
print("=" * 90)

print("\nOn-line: cauchy_sum = 4 Re B_G(rho) (for double-counted cluster)")
print(f"\n{'rho_n':>15s} {'B_G(rho)':>30s} {'4 Re B_G(rho)':>16s}")
print("-" * 65)

for gamma0 in GAMMA_ZEROS:
    rho = complex(0.5, gamma0)
    BG = B_G(rho, G_balanced)
    print(f"{f'0.5+{gamma0:.4f}i':>15s} {f'{BG.real:+.4f}{BG.imag:+.4f}j':>30s} {4*BG.real:16.6e}")

print()
print("Question: at every nontrivial zero rho, is 4 Re B_G(rho) constrained?")
print("If yes (e.g., always zero): we have an RH-equivalent at fixed Z/6.")
print("If no (varies arbitrarily): no topological constraint, need other mechanism.")
