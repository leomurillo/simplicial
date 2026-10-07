"""
Probe A2: Verify the universal K-cumulant tower identity at zeta zeros.

Empirical finding from Probe A:
   kappa_n^K(rho) * zeta(rho)^n = (-1)^n * (n-1)! * B_G(rho)^n

for n = 3, 4 verified. This conjectures the entire K-cumulant tower at every
zeta zero is governed by:

   K^K(z; rho) := sum_{n>=1} kappa_n^K z^n / n! = -log(1 + B_G(rho) z / zeta(rho))

This is the cumulant generating function of an EXPONENTIAL distribution with
rate parameter -zeta(rho)/B_G(rho). As rho approaches a zero, ze(ta)ta -> 0 so
the rate -> 0, distribution becomes a "spike at infinity" -- the divergence.

We verify for n = 2, 3, 4, 5, 6 numerically by computing each K-cumulant
directly via the partition formula.

If this universal identity holds: the entire Bures K-cumulant tower
collapses to a single 1-parameter exponential family at every zeta zero,
parameter = B_G(rho)/zeta(rho).
"""

import numpy as np
import mpmath as mp
from math import factorial

mp.mp.dps = 40  # very high precision needed since |zeta|^n is tiny


def q_r_6(r, s):
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


def compute_moments(G, q, n_max=6):
    G_K = apply_K(G)
    m = [1.0 + 0j]  # m[0] = <I> = 1
    mK = [np.sum(q * np.diag(G_K))]  # mK[0] = <G_K>
    Gk = np.eye(6, dtype=complex)
    for k in range(1, n_max + 1):
        Gk = Gk @ G  # now Gk = G^k
        m.append(np.sum(q * np.diag(Gk)))
        if k < n_max:
            mK.append(np.sum(q * np.diag(G_K @ Gk)))
    return m, mK


def all_partitions(n):
    """Generate all set partitions of [n]."""
    if n == 0:
        yield []
        return
    elif n == 1:
        yield [[0]]
        return
    for p in all_partitions(n - 1):
        # add (n-1) to any existing block
        for i in range(len(p)):
            new_p = [list(b) for b in p]
            new_p[i].append(n - 1)
            yield new_p
        # or start a new block with just (n-1)
        new_p = [list(b) for b in p]
        new_p.append([n - 1])
        yield new_p


def k_marked_partitions(n):
    """
    All set partitions of [n] where element 0 is the K-marked vertex.
    Returns list of partitions; for each, the block containing 0 contributes a K-cumulant.
    """
    return list(all_partitions(n))


def compute_K_cumulant(G, q, n, m_cache=None, mK_cache=None):
    """
    Compute kappa_n^K via direct partition expansion.
    The K-marked vertex is element 0; ordinary vertices are 1, ..., n-1.

    m_n^K = sum_{partitions pi of [n] with 0 marked} prod_{B in pi} kappa_{|B|, marked if 0 in B}

    Inverting via Mobius on lattice of partitions:
       kappa_n^K = sum_{partitions pi} (-1)^{|pi|-1} (|pi|-1)! prod_{B in pi} m_{|B|, marked}

    where m_{k, ordinary} = m_k = <G^k>, m_{k, marked} = mK[k-1] = <G_K G^{k-1}>.
    """
    if m_cache is None:
        m, mK = compute_moments(G, q, n_max=n)
    else:
        m, mK = m_cache, mK_cache

    total = 0j
    for partition in all_partitions(n):
        sign = (-1) ** (len(partition) - 1)
        coef = factorial(len(partition) - 1)
        prod = 1.0 + 0j
        for block in partition:
            block_size = len(block)
            if 0 in block:
                # K-marked block: contributes <G_K G^{k-1}> = mK[block_size - 1]
                prod *= mK[block_size - 1]
            else:
                # ordinary block: contributes <G^k> = m[block_size]
                prod *= m[block_size]
        total += sign * coef * prod
    return total


# ----- Closed-form B_G(s) -----

def B_G(g_diag, s):
    s_mp = mp.mpc(s.real, s.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += mp.zeta(s_mp, mp.mpf(r) / 6) * mp.mpc(g_diag[r])
    val *= mp.mpc(6) ** (-s_mp)
    return complex(val)


# ----- Test setup -----

def G_balanced():
    G = np.zeros((6, 6), dtype=complex)
    G[0, 0] = 1; G[1, 1] = -1; G[2, 2] = 0.5; G[3, 3] = -0.5
    G[0, 1] = 0.3; G[1, 0] = 0.3
    G[2, 3] = 0.2; G[3, 2] = 0.2
    G[0, 2] = 0.1; G[2, 0] = 0.1
    return G


G = G_balanced()
g_diag = [G[i, i].real for i in range(6)]

print("=" * 100)
print("Probe A2: Universal K-cumulant tower at zeta zeros")
print(f"Conjecture: kappa_n^K(rho) * zeta(rho)^n = (-1)^n (n-1)! B_G(rho)^n")
print("=" * 100)

zeros_t = [14.13473, 21.02204, 25.01086, 30.42488, 32.93506]

for t in zeros_t:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    zeta_val = complex(mp.zeta(s_mp))
    abs_z = abs(zeta_val)

    q = rho_diag(s)
    m, mK = compute_moments(G, q, n_max=6)

    BG = B_G(g_diag, s)

    print(f"\nt = {t:.5f}, |zeta(rho)| = {abs_z:.4e}, B_G(rho) = {BG.real:+.4e} {BG.imag:+.4e}j")
    print(f"  {'n':>3s} {'|kappa_n^K|':>16s} {'kappa_n^K * zeta^n':>26s} {'(-1)^n (n-1)! B_G^n':>26s} {'ratio':>14s}")
    print(f"  {'-' * 3} {'-' * 16} {'-' * 26} {'-' * 26} {'-' * 14}")

    for n in range(2, 7):
        kn_K = compute_K_cumulant(G, q, n, m, mK)
        z_n = zeta_val ** n
        product = kn_K * z_n
        predicted = (-1) ** n * factorial(n - 1) * BG ** n
        ratio = product / predicted if abs(predicted) > 1e-20 else float('nan')
        print(f"  {n:>3d} {abs(kn_K):16.4e} {f'{product.real:+.3e}{product.imag:+.3e}j':>26s} "
              f"{f'{predicted.real:+.3e}{predicted.imag:+.3e}j':>26s} {ratio.real:+.6f}{ratio.imag:+.6f}j")

print()
print("=" * 100)
print("Test off-zero (s = 0.5 + 18i): is the identity restricted to zeros?")
print("=" * 100)

s = complex(0.5, 18.0)
s_mp = mp.mpc(0.5, 18.0)
zeta_val = complex(mp.zeta(s_mp))
abs_z = abs(zeta_val)

q = rho_diag(s)
m, mK = compute_moments(G, q, n_max=6)
BG = B_G(g_diag, s)

print(f"\nt = 18.0, |zeta(s)| = {abs_z:.4e} (NOT near a zero), B_G(s) = {BG.real:+.4e} {BG.imag:+.4e}j")
print(f"  {'n':>3s} {'|kappa_n^K|':>16s} {'kappa_n^K * zeta^n':>26s} {'(-1)^n (n-1)! B_G^n':>26s} {'ratio':>14s}")

for n in range(2, 7):
    kn_K = compute_K_cumulant(G, q, n, m, mK)
    z_n = zeta_val ** n
    product = kn_K * z_n
    predicted = (-1) ** n * factorial(n - 1) * BG ** n
    ratio = product / predicted if abs(predicted) > 1e-20 else float('nan')
    print(f"  {n:>3d} {abs(kn_K):16.4e} {f'{product.real:+.3e}{product.imag:+.3e}j':>26s} "
          f"{f'{predicted.real:+.3e}{predicted.imag:+.3e}j':>26s} {ratio.real:+.6f}{ratio.imag:+.6f}j")

print("""
Expectation:
- At zeta zeros: ratio = +1 + 0j (universal identity holds)
- Off zeros: ratio NOT +1 (identity is special to zeros only)
""")
