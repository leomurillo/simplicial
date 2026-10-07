"""
Analytical derivation of C_G(s), the scaling constant in
    |kappa_3^K(G; s)| ~ |C_G(s)| / |zeta(s)|^3 near a zeta-zero.

The cumulant decomposes as:
    kappa_3^K(G; s) = P_0(s) + P_1(s)/zeta + P_2(s)/zeta^2 + P_3(s)/zeta^3

The leading divergence at zeta-zeros is P_3(s) / zeta(s)^3, where
    P_3(s) = 2 * B_{G^K}(s) * B_G(s)^2

with
    B_G(s) := 6^{-s} sum_{r=1}^5 zeta(s, r/6) * G_{rr}

(zeta(s, a) being the Hurwitz zeta function).

This expresses C_G(s) = P_3(s) as an explicit linear combination of Hurwitz zetas.
We verify by direct comparison with the empirical |kappa| * |zeta|^3 measurement.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 40  # high precision

# ===== Closed-form C_G(s) =====

def B_G(g_diag, s_complex):
    """
    B_G(s) = 6^{-s} * sum_{r=1}^5 zeta(s, r/6) * g_r
    where g_diag = [g_0, g_1, g_2, g_3, g_4, g_5] is the diagonal of G.
    """
    s = mp.mpc(s_complex.real, s_complex.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += mp.zeta(s, mp.mpf(r) / 6) * mp.mpc(g_diag[r])
    val *= mp.mpc(6) ** (-s)
    return complex(float(val.real), float(val.imag))

def C_G_analytic(g_diag, s_complex):
    """
    C_G(s) = 2 * B_{G^K}(s) * B_G(s)^2

    where G^K diagonal is g_diag permuted by r -> -r mod 6:
    K: 0->0, 1->5, 2->4, 3->3, 4->2, 5->1
    """
    g_K_diag = [g_diag[0], g_diag[5], g_diag[4], g_diag[3], g_diag[2], g_diag[1]]

    BG = B_G(g_diag, s_complex)
    BGK = B_G(g_K_diag, s_complex)

    return 2 * BGK * BG**2

# ===== Verification: compare to empirical |kappa| * |zeta|^3 =====

# Re-import the experimental setup
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

def kappa3_K_empirical(G, q):
    G_K = apply_K(G)
    g       = np.sum(q * np.diag(G))
    g_K     = np.sum(q * np.diag(G_K))
    g_sq    = np.sum(q * np.diag(G @ G))
    g_K_g   = np.sum(q * np.diag(G_K @ G))
    g_K_gsq = np.sum(q * np.diag(G_K @ G @ G))
    return g_K_gsq - g_K * g_sq - 2 * g * g_K_g + 2 * g_K * g**2

# ===== Test: G_balanced =====

def G_balanced():
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1; G[1, 1] = -1; G[2, 2] = 0.5; G[3, 3] = -0.5
    G[0, 1] = 0.3; G[1, 0] = 0.3
    G[2, 3] = 0.2; G[3, 2] = 0.2
    G[0, 2] = 0.1; G[2, 0] = 0.1
    return G

G = G_balanced()
g_diag = [G[i, i].real for i in range(6)]
print(f"G_balanced diagonal: {g_diag}")
print(f"G_K_balanced diagonal: {[g_diag[0], g_diag[5], g_diag[4], g_diag[3], g_diag[2], g_diag[1]]}")
print()

# ===== Compare at several test points =====

print("=" * 100)
print("Verification: comparing closed-form C_G(s) to empirical |kappa| * |zeta|^3")
print("Expected: |C_G_analytic| approximates |kappa| * |zeta|^3 near zeta zeros.")
print("=" * 100)
print()
print(f"{'t':>12s} {'|zeta|':>14s} {'|kappa_empirical|':>18s} {'|kappa|*|zeta|^3':>20s} {'|C_G_analytic|':>18s} {'ratio':>10s}")
print("-" * 100)

# Points around first zero and a few generic points
test_points = [
    14.00, 14.10, 14.130, 14.13473, 14.140, 14.20, 14.50,
    18.0,
    21.00, 21.022, 21.02204, 21.030,
    25.00, 25.0109, 25.020,
    30.4249,
]

for t in test_points:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))

    # Empirical
    q = rho_diag(s)
    k_emp = kappa3_K_empirical(G, q)
    abs_k_zeta3 = abs(k_emp) * abs(zeta_val)**3

    # Analytical
    c_analytic = C_G_analytic(g_diag, s)
    abs_c = abs(c_analytic)

    ratio = abs_k_zeta3 / abs_c if abs_c > 1e-20 else float('inf')

    marker = " <-- ZETA ZERO" if any(abs(t - z) < 0.01 for z in [14.13473, 21.02204, 25.0109, 30.4249]) else ""
    print(f"{t:12.5f} {abs(zeta_val):14.6e} {abs(k_emp):18.6e} {abs_k_zeta3:20.6e} {abs_c:18.6e} {ratio:10.6f}{marker}")

# ===== Analyze C_G structure: does it have zeros in the critical strip? =====

print()
print("=" * 100)
print("Analysis: Does C_G(s) have zeros that could mask zeta-zeros?")
print("Scanning |C_G(s)| over critical strip near known zeta zeros")
print("=" * 100)
print()

# Look at |C_G(s)| on a vertical line near sigma = 0.5
for sigma in [0.3, 0.4, 0.49, 0.5, 0.51, 0.6, 0.7]:
    s = complex(sigma, 14.13473)
    c = C_G_analytic(g_diag, s)
    print(f"  sigma={sigma:.3f}, t=14.13473: |C_G| = {abs(c):.6e}, arg(C_G) = {np.angle(c):.6f} rad")

print()
print("Scanning |C_G(s)| in 2D, looking for zeros of C_G itself")
print(f"{'sigma':>10s} {'t':>10s} {'|C_G|':>14s}")
print("-" * 40)
min_c = float('inf')
min_s = None
for sigma in np.linspace(0.1, 0.9, 17):
    for t in np.linspace(0.5, 40, 80):
        s = complex(sigma, t)
        c = C_G_analytic(g_diag, s)
        if abs(c) < min_c:
            min_c = abs(c)
            min_s = (sigma, t)

print(f"Minimum |C_G| in scan: {min_c:.6e} at (sigma, t) = {min_s}")
print()
if min_c > 1e-6:
    print(f"*** C_G_analytic does NOT vanish in critical strip up to t=40. ***")
    print(f"    Bures cubic detector is non-degenerate for this G across the scan.")
else:
    print(f"*** C_G might vanish at (sigma, t) = {min_s} — needs investigation. ***")
