"""
Probe ONCE: Discrete Gauss-Bonnet on the FE-cluster tetrahedron.

The conjecture (once.md):
   Phi_L(rho) = sum_{(v,w) in 6 edges} 2 B_G(rho_v) B_GK(rho_w)
   Phi_R(rho) = sum_{v in 4 vertices} (2pi - sum_{f containing v} theta_f(v))

At every nontrivial zero rho of zeta, we expect Phi_L = Phi_R.

For on-line rho (delta=0): cluster degenerates, Phi_L = Phi_R = 0.
For off-line rho (delta>0): cluster is a genuine tetrahedron, Phi_R = 4pi by Descartes.

The conjecture, if verified, forces all zeros on-line (continuity of Phi_L
in delta, vs jump of Phi_R from 0 to 4pi).

We test:
1. At first 5 zeros on-line: Phi_L numerical, expect approx 0.
2. At artificial off-line (gamma_0 = 14.13473, delta=0.1, 0.2): compute Phi_L
   to see if it approaches 4pi or stays small.
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

# ===== Bures-Hurwitz amplitudes =====

def B_G(s, G_diag):
    """B_G(s) = 6^{-s} sum_{r=1}^5 G_r zeta(s, r/6)."""
    s_mp = mp.mpc(s.real, s.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += mp.mpc(G_diag[r]) * mp.zeta(s_mp, mp.mpf(r) / mp.mpf(6))
    val *= mp.mpc(6) ** (-s_mp)
    return complex(val)

# K-antisymmetric G_balanced (nueve §6):
#   G_diag = [G_0, G_1, G_2, G_3, G_4, G_5] with G_0 free, G_3 = 0,
#   G_4 = -G_2, G_5 = -G_1.
G_balanced = [1.0, 1.0, 0.5, 0.0, -0.5, -1.0]

# K-conjugate: G^K_r = G_{6-r}
def G_K(G):
    return [G[0], G[5], G[4], G[3], G[2], G[1]]

# ===== Cluster geometry =====

def cluster(delta, gamma0):
    """4 cluster zeros: rho_+, rho_-, bar(rho_+), bar(rho_-)."""
    rho_p = complex(0.5 + delta, +gamma0)
    rho_m = complex(0.5 - delta, +gamma0)
    rho_p_bar = complex(0.5 + delta, -gamma0)
    rho_m_bar = complex(0.5 - delta, -gamma0)
    return [rho_p, rho_m, rho_p_bar, rho_m_bar]

# ===== Side L: Bures amplitude curvature sum =====

def Phi_L(delta, gamma0, G=G_balanced):
    """Phi_L = 2 sum over 6 cluster edges of B_G(rho_v) * B_GK(rho_w)."""
    G_K_diag = G_K(G)
    L = cluster(delta, gamma0)
    BG_vals = [B_G(rho, G) for rho in L]
    BGK_vals = [B_G(rho, G_K_diag) for rho in L]

    total = 0.0 + 0j
    for i in range(4):
        for j in range(i + 1, 4):  # 6 edges (unordered pairs)
            # Symmetrize over the two orientations of each edge
            edge_term = 0.5 * (BG_vals[i] * BGK_vals[j] + BG_vals[j] * BGK_vals[i])
            total += 2 * edge_term
    return total

# ===== Side R: discrete angular deficit (Descartes) =====

def K_modulus_discrepancy(rho, G=G_balanced):
    """h(rho) := |B_G(rho)|^2 - |B_GK(rho)|^2.
    Zero on critical line by K-antisymmetry; non-zero off-line."""
    BG = B_G(rho, G)
    BGK = B_G(rho, G_K(G))
    return abs(BG)**2 - abs(BGK)**2

def lift_to_R3(rho, G=G_balanced):
    """Embed cluster vertex rho in R^3 with Bures-tower height."""
    h = K_modulus_discrepancy(rho, G)
    return np.array([rho.real, rho.imag, h])

def angular_deficit(vertices_3d, vertex_index):
    """At vertex v, compute 2*pi - sum_{f containing v} interior_angle_f(v).
    v is connected to the other 3 vertices, forming 3 faces sharing v.
    Each face is a triangle (v, u1, u2)."""
    v = vertices_3d[vertex_index]
    others = [vertices_3d[i] for i in range(4) if i != vertex_index]

    # Three faces share v, formed by pairing the 3 "others" two at a time.
    angle_sum = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            u1 = others[i]
            u2 = others[j]
            # Interior angle at v in triangle (v, u1, u2): angle between (u1-v) and (u2-v)
            vec1 = u1 - v
            vec2 = u2 - v
            cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2) + 1e-30)
            cos_angle = np.clip(cos_angle, -1, 1)
            angle = np.arccos(cos_angle)
            angle_sum += angle

    return 2 * np.pi - angle_sum

def Phi_R(delta, gamma0, G=G_balanced):
    """Phi_R = sum over 4 cluster vertices of angular deficits (Descartes)."""
    L = cluster(delta, gamma0)
    V3 = [lift_to_R3(rho, G) for rho in L]
    total = 0.0
    for i in range(4):
        total += angular_deficit(V3, i)
    return total

# ===== Run the test =====

print("=" * 90)
print("Probe ONCE: Phi_L vs Phi_R on FE-cluster tetrahedron")
print("=" * 90)

print(f"\n{'(delta, gamma_0)':>22s} {'h(rho_+)':>15s} {'Phi_L':>20s} {'Phi_R':>15s} {'|Phi_L|':>12s}")
print("-" * 90)

# On-line: delta = 0 at first 5 zeros
print("\n--- On-line (delta = 0): expect Phi_L = Phi_R = 0 ---")
for gamma0 in GAMMA_ZEROS:
    PL = Phi_L(0.0, gamma0)
    PR = Phi_R(0.0, gamma0)
    h = K_modulus_discrepancy(complex(0.5, gamma0))
    print(f"({0:6.2f}, {gamma0:8.4f})  {h:15.6e} {PL.real:+10.4e}{PL.imag:+10.4e}j {PR:15.6f} {abs(PL):12.4e}")

# Off-line (artificial): delta > 0 at gamma_0 = first zero
print("\n--- Artificial off-line (delta > 0): does Phi_L approach 4pi = 12.566? ---")
print("                                                                            (4pi if conjecture)")
for delta in [0.0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4]:
    gamma0 = 14.134725141734693
    PL = Phi_L(delta, gamma0)
    PR = Phi_R(delta, gamma0)
    h_p = K_modulus_discrepancy(complex(0.5 + delta, gamma0))
    print(f"({delta:6.3f}, {gamma0:8.4f})  {h_p:15.6e} {PL.real:+10.4e}{PL.imag:+10.4e}j {PR:15.6f} {abs(PL):12.4e}")

# Check at a non-zero off-line point (no zero exists, but compute formally)
print("\n--- Off-line, no zero present (sanity check at random gamma) ---")
for delta in [0.0, 0.1, 0.2]:
    gamma0 = 15.0  # not a zero
    PL = Phi_L(delta, gamma0)
    PR = Phi_R(delta, gamma0)
    h_p = K_modulus_discrepancy(complex(0.5 + delta, gamma0))
    print(f"({delta:6.3f}, {gamma0:8.4f})  {h_p:15.6e} {PL.real:+10.4e}{PL.imag:+10.4e}j {PR:15.6f} {abs(PL):12.4e}")

print()
print("=" * 90)
print("Analysis:")
print("=" * 90)
print("""
If Phi_L stays small (~0) at on-line zeros: consistent with Phi_R = 0 (degenerate cluster).

For off-line (delta > 0), if Phi_R jumps to ~4pi = 12.566 (Descartes for tetrahedron),
then the conjecture says Phi_L must also equal 4pi. But Phi_L is analytically continuous
in delta. If Phi_L stays small as delta grows, the conjecture is FALSIFIED for off-line
zeros — meaning no off-line zeros can exist (since the identity must hold at every zero).

If Phi_L grows to match 4pi: the conjecture is supported, and the mechanism for RH is:
   continuity of Phi_L in delta contradicts the topological jump of Phi_R, so no off-line
   zero can exist.

Either outcome is informative. If Phi_L != Phi_R at any tested zero, the conjecture as
stated needs refinement (e.g., different height function, different metric structure).
""")
