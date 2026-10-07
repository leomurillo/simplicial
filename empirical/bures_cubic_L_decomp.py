"""
L-function decomposition of B_G(s) and C_G(s).

The Hurwitz zetas at r/6 decompose over Dirichlet characters mod 6 (which are
just the trivial chi_0 and the unique non-trivial primitive chi_6), with
intermediate factorization through chi_3 (the Legendre symbol mod 3).

After working out the decomposition:

  B_G(s)    = Z(s) - (1/2) L(s, chi_6) + (2^{-s}/4) L(s, chi_3)
  B_{G^K}(s) = Z(s) + (1/2) L(s, chi_6) - (2^{-s}/4) L(s, chi_3)

where the shared zeta part is
  Z(s) = zeta(s) * [ -1/2 + (2^{-s}/4)(3 - 3^{-s}) ]

For G_balanced specifically. The C_G product:
  C_G(s) = 2 * B_{G^K} * B_G^2 = 2 * (B_G * B_{G^K}) * B_G
         = 2 * [Z^2 - (1/2 L_6 - (2^{-s}/4) L_3)^2] * [Z - (1/2) L_6 + (2^{-s}/4) L_3]

We verify this decomposition numerically against the direct Hurwitz formula.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 20  # 20 digits is plenty for verification

def hurwitz(s_c, a):
    s = mp.mpc(s_c.real, s_c.imag)
    return mp.zeta(s, mp.mpf(a) if not isinstance(a, mp.mpc) else a)

def L_chi_3(s_c):
    """L(s, chi_3) via Hurwitz: L(s, chi_3) = 3^{-s} [zeta(s, 1/3) - zeta(s, 2/3)]."""
    s = mp.mpc(s_c.real, s_c.imag)
    val = mp.mpc(3)**(-s) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
    return complex(float(val.real), float(val.imag))

def L_chi_6(s_c):
    """L(s, chi_6) via Hurwitz: L(s, chi_6) = 6^{-s} [zeta(s, 1/6) - zeta(s, 5/6)]."""
    s = mp.mpc(s_c.real, s_c.imag)
    val = mp.mpc(6)**(-s) * (mp.zeta(s, mp.mpf(1)/6) - mp.zeta(s, mp.mpf(5)/6))
    return complex(float(val.real), float(val.imag))

def zeta_value(s_c):
    return complex(mp.zeta(mp.mpc(s_c.real, s_c.imag)))

# ===== B_G via direct Hurwitz formula =====

def B_G_direct(g_diag, s_c):
    """Direct: 6^{-s} sum_{r=1}^5 zeta(s, r/6) g_r."""
    s = mp.mpc(s_c.real, s_c.imag)
    val = mp.mpc(0)
    for r in range(1, 6):
        val += hurwitz(s_c, r/mp.mpf(6)) * mp.mpc(g_diag[r])
    val *= mp.mpc(6) ** (-s)
    return complex(float(val.real), float(val.imag))

# ===== B_G via L-function decomposition (for G_balanced specifically) =====

def Z_part(s_c):
    """Z(s) = zeta(s) * [-1/2 + (2^{-s}/4)(3 - 3^{-s})]."""
    s = mp.mpc(s_c.real, s_c.imag)
    a = mp.mpc(2) ** (-s)  # 2^{-s}
    b = mp.mpc(3) ** (-s)  # 3^{-s}
    bracket = -mp.mpf(1)/2 + (a/4) * (3 - b)
    val = mp.zeta(s) * bracket
    return complex(float(val.real), float(val.imag))

def B_G_decomp(s_c):
    """For G_balanced: B_G(s) = Z(s) - (1/2) L_6 + (2^{-s}/4) L_3."""
    Z = Z_part(s_c)
    L3 = L_chi_3(s_c)
    L6 = L_chi_6(s_c)
    a = complex(mp.mpc(2)**(-mp.mpc(s_c.real, s_c.imag)))
    return Z - 0.5 * L6 + (a/4) * L3

def B_GK_decomp(s_c):
    """For G_K_balanced: B_GK(s) = Z(s) + (1/2) L_6 - (2^{-s}/4) L_3."""
    Z = Z_part(s_c)
    L3 = L_chi_3(s_c)
    L6 = L_chi_6(s_c)
    a = complex(mp.mpc(2)**(-mp.mpc(s_c.real, s_c.imag)))
    return Z + 0.5 * L6 - (a/4) * L3

# ===== Verification =====

g_balanced = [1, -1, 0.5, -0.5, 0, 0]
g_balanced_K = [1, 0, 0, -0.5, 0.5, -1]

print("=" * 100)
print("Verification: B_G(s) via direct Hurwitz sum vs L-function decomposition")
print("=" * 100)
print(f"\n{'t':>10s} {'B_G direct':>26s} {'B_G decomp':>26s} {'agreement?':>14s}")
print("-" * 100)
for t in [14.13473, 21.02204, 25.0109, 30.4249, 18.0, 32.9351]:
    s = complex(0.5, t)
    B_direct = B_G_direct(g_balanced, s)
    B_decomp = B_G_decomp(s)
    agree = abs(B_direct - B_decomp) < 1e-6
    print(f"{t:10.4f} {f'{B_direct.real:+.4e}{B_direct.imag:+.4e}j':>26s} {f'{B_decomp.real:+.4e}{B_decomp.imag:+.4e}j':>26s} {'YES' if agree else 'NO':>14s}")

print()
print("=" * 100)
print("Verification: B_GK direct vs decomposition")
print("=" * 100)
print(f"\n{'t':>10s} {'B_GK direct':>26s} {'B_GK decomp':>26s} {'agreement?':>14s}")
print("-" * 100)
for t in [14.13473, 21.02204, 25.0109, 30.4249, 18.0]:
    s = complex(0.5, t)
    BGK_direct = B_G_direct(g_balanced_K, s)
    BGK_decomp = B_GK_decomp(s)
    agree = abs(BGK_direct - BGK_decomp) < 1e-6
    print(f"{t:10.4f} {f'{BGK_direct.real:+.4e}{BGK_direct.imag:+.4e}j':>26s} {f'{BGK_decomp.real:+.4e}{BGK_decomp.imag:+.4e}j':>26s} {'YES' if agree else 'NO':>14s}")

# ===== Find zeros of B_G(s) in the critical strip =====

print()
print("=" * 100)
print("Searching for zeros of B_G(s) in the critical strip 0.1 < Re(s) < 0.9")
print("(Zeros of B_G OFF the critical line could mask off-line zeta zeros)")
print("=" * 100)
print()

# Scan |B_G(s)|, look for small values
print(f"{'sigma':>10s} {'t':>10s} {'|B_G|':>14s}")
print("-" * 40)

zeros_BG = []
for sigma in np.linspace(0.1, 0.9, 17):
    for t in np.linspace(0.5, 30, 60):
        s = complex(sigma, t)
        bg = B_G_decomp(s)
        if abs(bg) < 0.02:  # potentially near a zero
            zeros_BG.append((sigma, t, abs(bg)))

zeros_BG.sort(key=lambda x: x[2])
print(f"Found {len(zeros_BG)} candidates with |B_G| < 0.02:")
for sigma, t, abs_bg in zeros_BG[:20]:
    on_cl = "(ON critical line)" if abs(sigma - 0.5) < 0.001 else f"(off line, sigma={sigma:.3f})"
    print(f"{sigma:10.4f} {t:10.4f} {abs_bg:14.6e} {on_cl}")

# ===== The decisive test: scan to find true zeros =====

print()
print("=" * 100)
print("Decisive test: refine candidate zero locations of B_G")
print("=" * 100)
print()

# Iterate to find a precise zero of B_G(s)
if len(zeros_BG) > 0:
    sigma0, t0, _ = zeros_BG[0]
    print(f"Refining candidate at (sigma, t) = ({sigma0:.4f}, {t0:.4f})...")

    # Newton-like search
    for step in range(10):
        s = complex(sigma0, t0)
        bg = B_G_decomp(s)
        # Numerical gradient
        eps = 1e-5
        bg_ds = (B_G_decomp(complex(sigma0 + eps, t0)) - bg) / eps
        bg_dt = (B_G_decomp(complex(sigma0, t0 + eps)) - bg) / eps
        # Move down |B_G|^2 gradient
        grad_real = 2 * (bg.real * bg_ds.real + bg.imag * bg_ds.imag)
        grad_imag = 2 * (bg.real * bg_dt.real + bg.imag * bg_dt.imag)
        sigma0 -= 0.01 * grad_real
        t0 -= 0.01 * grad_imag
        print(f"  step {step}: s = {sigma0:.6f} + {t0:.6f}i, |B_G| = {abs(bg):.6e}")

print()
print("=" * 100)
print("Summary of structural finding")
print("=" * 100)
print("""
B_G(s) for G_balanced has the closed-form L-function decomposition:

   B_G(s) = Z(s) - (1/2) L(s, chi_6) + (2^{-s}/4) L(s, chi_3)

where Z(s) = zeta(s) * [-1/2 + (2^{-s}/4)(3 - 3^{-s})].

This is a SPECIFIC linear combination of three L-functions:
   - Riemann zeta zeta(s)
   - L(s, chi_3): non-trivial Dirichlet character mod 3
   - L(s, chi_6): non-trivial Dirichlet character mod 6

Zeros of B_G(s) in the critical strip occur at points where this linear
combination vanishes. Under GRH (for all three L-functions involved),
the zeros of each L-function sit on Re(s) = 1/2. Zeros of the linear
combination can be at OTHER points where the components cancel.

The decisive question for the Bures cubic detector:
   Does B_G(s) (and hence C_G(s) = 2 B_GK B_G^2) have OFF-LINE zeros
   in the critical strip?

If YES: such off-line zeros could mask hypothetical off-line zeros of zeta.
If NO: the detector is universal, every zeta-zero corresponds to a divergence.

Empirical scan above gives evidence.
""")
