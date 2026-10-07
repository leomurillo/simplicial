"""
Probe A: Quartic Bures K-cumulant on Z/6.

Building on the cubic detector
   kappa_3^K(G; s) ~ C_G(s) / zeta(s)^3   at zeta zeros
   where C_G(s) = 2 B_{G^K}(s) B_G(s)^2,
   B_G(s) = 6^{-s} sum_{r=1}^5 zeta(s, r/6) G_{rr}

we now compute the quartic K-cumulant
   kappa_4^K(G; s) ~ D_G(s) / zeta(s)^4   at zeta zeros

and ask:
  Q1: What is the closed form D_G(s)?
  Q2: Does D_G(s) have a DIFFERENT zero set from C_G(s) in the critical strip?
      (If yes -> quartic is a NEW discriminator; if no -> same Bures-blind locus.)
  Q3: Does the leading divergence give |kappa_4^K|*|zeta|^4 = c |B_G|^4 with
      a clean Pascal/binomial coefficient c?

K-marked partition formula on {K, 1, 2, 3}:
   m_4^K = kappa_4^K + 3 kappa_3^K kappa_1 + 3 kappa_2^K kappa_2 + kappa_1^K kappa_3
           + 3 kappa_2^K kappa_1^2 + 3 kappa_1^K kappa_2 kappa_1 + kappa_1^K kappa_1^3

Inverted:
   kappa_4^K = m_4^K - 3 kappa_3^K kappa_1 - 3 kappa_2^K kappa_2 - kappa_1^K kappa_3
               - 3 kappa_2^K kappa_1^2 - 3 kappa_1^K kappa_2 kappa_1 - kappa_1^K kappa_1^3
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30


def q_r_6(r, s):
    """The Z/6 distribution: q_0 = 6^{-s}, q_r = 6^{-s} zeta(s, r/6) / zeta(s) for r>=1."""
    s_mp = mp.mpc(s.real, s.imag)
    if r == 0:
        val = mp.mpc(6) ** (-s_mp)
    else:
        val = mp.mpc(6) ** (-s_mp) * mp.zeta(s_mp, mp.mpc(r) / mp.mpc(6)) / mp.zeta(s_mp)
    return complex(float(val.real), float(val.imag))


def rho_diag(s):
    return np.array([q_r_6(r, s) for r in range(6)], dtype=complex)


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


def moments(G, q, n_max=4):
    """Raw moments m_k = <G^k> and K-moments m_k^K = <G_K G^{k-1}>."""
    G_K = apply_K(G)
    ms = []  # m_k = <G^k>
    msK = []  # m_k^K = <G_K G^{k-1}>
    Gk = np.eye(6, dtype=complex)
    for k in range(n_max + 1):
        if k == 0:
            ms.append(1.0 + 0j)  # <I> = 1 (no, sum q_r = ?)
            # Actually <I> = sum q_r = 6^{-s} (1 + sum zeta(s,r/6)/zeta(s))
            # By Kluyver: sum_{r=1}^Q zeta(s, r/Q) = Q^s zeta(s), so:
            #   sum_{r=1}^{Q-1} zeta(s, r/Q) = Q^s zeta(s) - zeta(s, 1) = Q^s zeta(s) - zeta(s)
            #   = (Q^s - 1) zeta(s)
            # So <I> = 6^{-s} + 6^{-s} (6^s - 1) = 6^{-s} + 1 - 6^{-s} = 1. Good.
            # We use <I> = 1.
            ms.append(np.sum(q))
            msK.append(np.sum(q * np.diag(G_K)))
        else:
            ms.append(np.sum(q * np.diag(Gk @ G)))
            msK.append(np.sum(q * np.diag(G_K @ Gk @ G if k > 1 else G_K @ G)))
            # Note: msK[k] index corresponds to <G_K G^k> for k>=1, prepended by <G_K> at k=0.
        if k >= 1:
            Gk = Gk @ G
    # Reindex: ms[0]=<I>=1, ms[1]=<G>, ms[2]=<G^2>, ..., ms[n_max] = <G^n_max>
    # msK[0]=<G_K>, msK[1]=<G_K G>, ..., msK[n_max-1]=<G_K G^{n_max-1}>
    # Wait we have an off-by-one. Let me redo cleanly.
    return None  # discard, do it cleanly below


def compute_moments(G, q, n_max=4):
    """
    Returns:
      m[k] = <G^k>     for k = 0, 1, ..., n_max  (m[0] = 1)
      mK[k] = <G_K G^k> for k = 0, 1, ..., n_max-1
    """
    G_K = apply_K(G)
    m = [1.0 + 0j]
    mK = [np.sum(q * np.diag(G_K))]  # <G_K>
    Gk = np.eye(6, dtype=complex)
    for k in range(1, n_max + 1):
        Gk_new = Gk @ G  # G^k
        m.append(np.sum(q * np.diag(Gk_new)))
        if k < n_max:
            mK.append(np.sum(q * np.diag(G_K @ Gk_new)))
        Gk = Gk_new
    return m, mK


def cumulants_K(m, mK):
    """
    Compute kappa_k and kappa_k^K up to k = 4 (using m[0..4], mK[0..3]).
    Formulas:
      k1 = m1
      k2 = m2 - m1^2
      k3 = m3 - 3 m1 m2 + 2 m1^3
      k4 = m4 - 4 m1 m3 - 3 m2^2 + 12 m1^2 m2 - 6 m1^4
      k1^K = mK0
      k2^K = mK1 - mK0 m1
      k3^K = mK2 - mK0 m2 - 2 mK1 m1 + 2 mK0 m1^2
      k4^K = mK3 - 3 k3^K k1 - 3 k2^K k2 - k1^K k3 - 3 k2^K k1^2 - 3 k1^K k2 k1 - k1^K k1^3
            (equivalently: m4^K - {non-trivial partition sums})
    """
    m1, m2, m3, m4 = m[1], m[2], m[3], m[4]
    mK0, mK1, mK2, mK3 = mK[0], mK[1], mK[2], mK[3]

    k1 = m1
    k2 = m2 - m1 ** 2
    k3 = m3 - 3 * m1 * m2 + 2 * m1 ** 3
    k4 = m4 - 4 * m1 * m3 - 3 * m2 ** 2 + 12 * m1 ** 2 * m2 - 6 * m1 ** 4

    k1K = mK0
    k2K = mK1 - mK0 * m1
    k3K = mK2 - mK0 * m2 - 2 * mK1 * m1 + 2 * mK0 * m1 ** 2
    # Use the partition formula: kappa_4^K = m_4^K - 3 k3K k1 - 3 k2K k2 - k1K k3
    #                                          - 3 k2K k1^2 - 3 k1K k2 k1 - k1K k1^3
    k4K = (mK3 - 3 * k3K * k1 - 3 * k2K * k2 - k1K * k3
           - 3 * k2K * k1 ** 2 - 3 * k1K * k2 * k1 - k1K * k1 ** 3)

    return k1, k2, k3, k4, k1K, k2K, k3K, k4K


# ----- Closed-form B_G(s) for verification -----

def B_G(g_diag, s):
    s_mp = mp.mpc(s.real, s.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += mp.zeta(s_mp, mp.mpf(r) / 6) * mp.mpc(g_diag[r])
    val *= mp.mpc(6) ** (-s_mp)
    return complex(val)


def C_G_analytic(g_diag, s):
    """Cubic detector: 2 B_GK B_G^2."""
    g_K_diag = [g_diag[0], g_diag[5], g_diag[4], g_diag[3], g_diag[2], g_diag[1]]
    BG = B_G(g_diag, s)
    BGK = B_G(g_K_diag, s)
    return 2 * BGK * BG ** 2


# ----- Test setup -----

def G_balanced():
    """G_balanced: K-mixed test operator."""
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1; G[1, 1] = -1; G[2, 2] = 0.5; G[3, 3] = -0.5
    G[0, 1] = 0.3; G[1, 0] = 0.3
    G[2, 3] = 0.2; G[3, 2] = 0.2
    G[0, 2] = 0.1; G[2, 0] = 0.1
    return G


G = G_balanced()
g_diag = [G[i, i].real for i in range(6)]
print(f"G_balanced diag: {g_diag}")
print(f"G_K_balanced diag: {[g_diag[0], g_diag[5], g_diag[4], g_diag[3], g_diag[2], g_diag[1]]}")

print("\n" + "=" * 100)
print("Probe A: Quartic K-cumulant scaling at zeta zeros")
print("=" * 100)
print(f"\n{'t':>10s} {'|zeta|':>13s} {'|kappa_3^K|':>14s} {'|k3K|*|z|^3':>14s} {'|kappa_4^K|':>14s} {'|k4K|*|z|^4':>14s} {'2|B_G|^3':>14s} {'?|B_G|^4':>14s}")
print("-" * 110)

# Test at known zeta zeros
zeros_t = [14.13473, 21.02204, 25.01086, 30.42488, 32.93506, 37.58618]

results = []
for t in zeros_t:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))
    abs_z = abs(zeta_val)

    q = rho_diag(s)
    m, mK = compute_moments(G, q, n_max=4)
    k1, k2, k3, k4, k1K, k2K, k3K, k4K = cumulants_K(m, mK)

    BG = B_G(g_diag, s)
    abs_BG = abs(BG)

    k3K_div = abs(k3K) * abs_z ** 3
    k4K_div = abs(k4K) * abs_z ** 4

    print(f"{t:10.5f} {abs_z:13.4e} {abs(k3K):14.4e} {k3K_div:14.4e} {abs(k4K):14.4e} {k4K_div:14.4e} "
          f"{2 * abs_BG ** 3:14.4e} {abs_BG ** 4:14.4e}")
    results.append((t, abs_z, k3K, k4K, BG))

# ----- Analyze leading constant ratio -----
print("\n" + "=" * 100)
print("Leading-constant ratios at zeta zeros")
print("=" * 100)

print(f"\n{'t':>10s} {'k4K*z^4 / |B_G|^4':>22s} {'arg(k4K)/B_G^4':>22s}")
print("-" * 60)
for t, abs_z, k3K, k4K, BG in results:
    coeff = (k4K * abs_z ** 4) / (BG ** 4)
    if abs(BG) > 1e-15:
        print(f"{t:10.5f} {abs(coeff):22.6e}  arg = {np.angle(coeff):8.4f}")

# Look for a clean closed-form constant
print("\nCompare ratio  (k4K * zeta^4) / B_G^4  at zeros:")
ratios_complex = [(t, (k4K * complex(mp.zeta(mp.mpc(0.5, t))) ** 4) / (BG ** 4))
                  for t, _, _, k4K, BG in results]
for t, r in ratios_complex:
    print(f"  t = {t:.5f}: ratio = {r.real:+.6f} {r.imag:+.6f}j")

# ----- D_G(s) closed-form hypothesis: P_4(s) = c * B_GK^? * B_G^? at zeros -----
print("\n" + "=" * 100)
print("Hypothesis: kappa_4^K(rho) * zeta(rho)^4 = c * f(B_G, B_GK) at zeta zeros")
print("Test candidate forms:")
print("=" * 100)

for t, abs_z, k3K, k4K, BG in results:
    s = complex(0.5, t)
    g_K_diag = [g_diag[0], g_diag[5], g_diag[4], g_diag[3], g_diag[2], g_diag[1]]
    BGK = B_G(g_K_diag, s)
    Z = complex(mp.zeta(mp.mpc(s.real, s.imag)))
    target = k4K * Z ** 4

    cand_A = BG ** 4  # 4*B_G^4
    cand_B = BG ** 3 * BGK
    cand_C = BG ** 2 * BGK ** 2
    cand_D = BG * BGK ** 3
    cand_E = BGK ** 4
    cand_F = (BG ** 2 * BGK + BG * BGK ** 2)  # mixed
    cand_G = BG ** 4 + BGK ** 4  # sym 4th

    print(f"\nt = {t:.5f}: target k4K*z^4 = {target.real:+.4e} {target.imag:+.4e}j")
    for name, c in [('B_G^4', cand_A), ('B_G^3 B_GK', cand_B), ('B_G^2 B_GK^2', cand_C),
                    ('B_G B_GK^3', cand_D), ('B_GK^4', cand_E),
                    ('B_G^2 B_GK + B_G B_GK^2', cand_F), ('B_G^4 + B_GK^4', cand_G)]:
        if abs(c) > 1e-15:
            r = target / c
            print(f"  target / ({name}) = {r.real:+.4f} {r.imag:+.4f}j")
