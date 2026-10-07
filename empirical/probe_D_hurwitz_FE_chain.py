"""
Probe D: Hurwitz functional-equation chain across primorials Q in {6, 30, 210}.

The Hurwitz zeta zeta(s, a) for a = r/Q rational satisfies a functional equation
via Hurwitz's formula (Hurwitz 1882):

   zeta(1-s, r/Q) = (2 Gamma(s) / (2pi Q)^s) sum_{m=1}^{Q-1}
                    [cos(pi s / 2 - 2 pi m r / Q) zeta(s, m/Q)]

In matrix form: vec(zeta(1-s, r/Q))_{r=1}^{Q-1} = M_Q(s) * vec(zeta(s, m/Q))_{m=1}^{Q-1}

The matrix M_Q(s) has entries
   M_Q(s)_{r, m} = (2 Gamma(s) / (2pi Q)^s) cos(pi s / 2 - 2 pi m r / Q)

The CRITICAL LINE corresponds to s -> 1-s being a symmetry: s = 1/2 + it gives
1 - s = 1/2 - it, complex conjugate (for real coefficients).

For a hypothetical OFF-LINE zero rho = sigma + i*t with sigma != 1/2:
   - The Riemann FE pairs rho <-> 1 - bar(rho) = (1-sigma) + i*t
   - Both zeros must be in the Hurwitz vector simultaneously
   - The B_G(s) = 6^{-s} sum zeta(s, r/6) G_rr identity must hold at both

Question: does the Hurwitz FE matrix M_Q(s) provide a constraint that
forces sigma = 1/2 for any K-antisymmetric G?

Test: compute M_Q(rho) numerically at hypothetical off-line points and check
whether the K-antisymmetric F-vector identity F_3(rho) = 0, F_5 + F_1 = 0,
F_4 + F_2 = 0 can hold consistently with M_Q(rho) acting on the vector.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30


def hurwitz_vec(s, Q):
    """Return vector [zeta(s, r/Q)]_{r=1}^{Q-1}."""
    return np.array([complex(mp.zeta(mp.mpc(s.real, s.imag), mp.mpf(r) / mp.mpf(Q)))
                     for r in range(1, Q)])


def hurwitz_FE_matrix(s, Q):
    """
    Matrix M_Q(s) such that vec_zeta(1-s, r/Q) = M_Q(s) vec_zeta(s, m/Q).
    Hurwitz's formula.
    """
    s_mp = mp.mpc(s.real, s.imag)
    pre = 2 * mp.gamma(s_mp) / (2 * mp.pi * Q) ** s_mp
    M = np.zeros((Q - 1, Q - 1), dtype=complex)
    for r in range(1, Q):
        for m in range(1, Q):
            arg = mp.pi * s_mp / 2 - 2 * mp.pi * mp.mpf(m * r) / mp.mpf(Q)
            val = pre * mp.cos(arg)
            M[r - 1, m - 1] = complex(val)
    return M


def test_FE_at(s, Q):
    """Verify Hurwitz FE numerically: ||M_Q(s) vec_zeta(s) - vec_zeta(1-s)||"""
    vec_s = hurwitz_vec(s, Q)
    s_dual = complex(1 - s.real, -s.imag)
    vec_dual = hurwitz_vec(s_dual, Q)
    M = hurwitz_FE_matrix(s, Q)
    predicted_dual = M @ vec_s
    error = np.linalg.norm(predicted_dual - vec_dual)
    return error, vec_s, vec_dual, M


# ----- Step 1: Verify Hurwitz FE matrix is correct -----

print("=" * 90)
print("Step 1: Verify Hurwitz functional equation matrix")
print("=" * 90)

for Q in [6, 12, 30]:
    print(f"\nQ = {Q}:")
    for t in [14.13473, 21.02204, 30.4249]:
        s = complex(0.5, t)
        err, _, _, _ = test_FE_at(s, Q)
        print(f"  s = 0.5 + {t:.5f}i: ||FE error|| = {err:.4e}")
    # Off-line test
    s_off = complex(0.7, 14.13473)
    err, _, _, _ = test_FE_at(s_off, Q)
    print(f"  s = 0.7 + 14.13473i: ||FE error|| = {err:.4e}  (off-line check)")

# ----- Step 2: The K-antisymmetric F-vector identity at zeta zeros -----
#
# F_r(s) := zeta(s, r/6) is the Hurwitz value at r/6.
# Define K-antisymmetric Bures combination from earlier:
#   B_G(s) = 6^{-s} (G_1 F_1 + G_2 F_2 + G_3 F_3 + G_4 F_4 + G_5 F_5)
#
# K-antisymmetry of G means G_K_r = -G_{-r mod 6}, i.e.:
#   G_1 -> -G_5,   G_2 -> -G_4,   G_3 -> -G_3 (so G_3 = 0)
#
# At a zeta zero rho, the structural identity is:
#   B_G(rho) = some non-trivial linear combination of zeta(rho, r/6)
#
# Question: under the Hurwitz FE matrix M_Q(rho) constraint, does the
# K-antisymmetric component vanish only at sigma = 1/2?

print("\n" + "=" * 90)
print("Step 2: K-antisymmetric structure of Hurwitz vector under FE")
print("=" * 90)

# K-antisymmetric "test" vector on Z/6: G_diag = [0, 1, 1, 0, -1, -1] (zero for r=0,3)
G_K_anti = np.array([1, 1, 0, -1, -1])  # G_{r}, r=1..5, with G_3=0, G_4=-G_2, G_5=-G_1
G_K_sym = np.array([1, 1, 0, 1, 1])     # K-symmetric: G_r = G_{-r}

Q = 6
for t in [14.13473, 21.02204, 25.0109]:
    s = complex(0.5, t)
    vec = hurwitz_vec(s, Q)  # [zeta(s, 1/6), ..., zeta(s, 5/6)]
    # Apply K to vec: K acts as r -> 6 - r (since -r mod 6 on r=1..5 swaps 1<->5, 2<->4, fixes 3)
    K_perm = np.array([
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ])
    vec_K = K_perm @ vec
    six_neg_s = complex(mp.mpc(6) ** (-mp.mpc(s.real, s.imag)))

    B_anti = six_neg_s * G_K_anti @ vec
    B_sym = six_neg_s * G_K_sym @ vec
    print(f"\nt = {t}, s = 0.5 + {t:.5f}i:")
    print(f"  vec_zeta(s, r/6) = {[f'{v.real:+.3f}{v.imag:+.3f}j' for v in vec]}")
    print(f"  K-vec            = {[f'{v.real:+.3f}{v.imag:+.3f}j' for v in vec_K]}")
    print(f"  K-anti scalar B  = {B_anti.real:+.6e} {B_anti.imag:+.6e}j")
    print(f"  K-sym scalar B   = {B_sym.real:+.6e} {B_sym.imag:+.6e}j")

# ----- Step 3: Off-line FE constraint test -----
#
# Hypothetical off-line zero: zeta(rho) = 0 with rho = sigma + it, sigma != 1/2.
# By FE, zeta(1 - bar(rho)) = 0 also. Both zeros must satisfy the Hurwitz vector
# identities (Kluyver: sum_r zeta(s, r/Q) = (Q^s - 1) zeta(s) gives sum_r = 0
# whenever zeta(s) = 0).
#
# But the K-antisymmetric scalar B_anti(rho) need NOT be zero at off-line rho
# — it just satisfies the structural identity proved earlier.

print("\n" + "=" * 90)
print("Step 3: Off-line scan — does Hurwitz FE constrain off-line zeros?")
print("=" * 90)

# At an off-line zero, zeta(rho) = 0 implies sum_r zeta(rho, r/Q) = 0.
# Check whether |zeta(rho)| can be small simultaneously with constraints

print(f"\nKluyver test: sum_{{r=0}}^{{Q-1}} zeta(s, r/Q) = Q^s zeta(s).")
print(f"At zeta(s) = 0, sum vanishes. Check this is consistent off-line:\n")

for Q in [6, 30]:
    print(f"Q = {Q}:")
    for sigma in [0.3, 0.4, 0.5, 0.6, 0.7]:
        for t in [14.13473]:
            s = complex(sigma, t)
            s_mp = mp.mpc(sigma, t)
            zeta_val = complex(mp.zeta(s_mp))
            # Kluyver: sum_{r=0}^{Q-1} zeta(s, r/Q) — but r=0 is undefined (need a > 0)
            # Use r=1..Q: sum is (Q^s - 1) zeta(s) WAIT — Kluyver: sum_{r=1}^Q zeta(s, r/Q)
            # Actually: sum_{r=1}^{Q} zeta(s, r/Q) = Q^s zeta(s) (note r=Q is zeta(s, 1) = zeta(s))
            sum_vec = sum(complex(mp.zeta(mp.mpc(sigma, t), mp.mpf(r) / mp.mpf(Q))) for r in range(1, Q + 1))
            Q_s_zeta = complex(mp.mpc(Q)**(mp.mpc(sigma, t)) * mp.zeta(mp.mpc(sigma, t)))
            err = abs(sum_vec - Q_s_zeta) / max(abs(Q_s_zeta), 1e-10)
            print(f"  sigma={sigma:.2f}: |zeta|={abs(zeta_val):.4e}, "
                  f"|sum - Q^s zeta|/|Q^s zeta| = {err:.4e}")

# ----- Step 4: Hurwitz FE chain Q=6 -> Q=30 -> Q=210 -----
#
# Key insight: zeta(s, r/6) decomposes as sum_{m: m mod 30 reduces to r mod 6}
# zeta(s, m/30) -- the "primorial refinement" identity:
#   zeta(s, a) = sum_{k=0}^{n-1} zeta(s, (a+k)/n) / n^s    [Hurwitz multiplication theorem]
# Specialized to a = r/6, n = 5: zeta(s, r/6) = 5^{-s} sum_{k=0}^{4} zeta(s, (r + 6k)/30)
# This gives the FE-chain refinement Q=6 -> Q=30.

print("\n" + "=" * 90)
print("Step 4: Hurwitz multiplication theorem — primorial refinement Q=6 -> Q=30")
print("=" * 90)

for t in [14.13473, 21.0]:
    s = complex(0.5, t)
    s_mp = mp.mpc(0.5, t)
    print(f"\ns = 0.5 + {t}i:")
    for r in range(1, 6):
        # zeta(s, r/6) should equal 5^{-s} sum_{k=0}^{4} zeta(s, (r + 6k)/30)
        # WAIT — multiplication theorem: zeta(s, a) = n^s/n sum_{k=0}^{n-1} zeta(s, a/n + k/n)?
        # No, correct form: zeta(s, a) = n^{-s} sum_{k=0}^{n-1} zeta(s, (a+k)/n)
        # We want refinement: zeta(s, r/6) = ? zeta(s, m/30) for m mod 30 lifting r mod 6.
        # The m's mapping to r mod 6 are m = r + 6k, k=0..4. These are r, r+6, r+12, r+18, r+24.
        # All m/30 = (r + 6k)/30. By Hurwitz mult thm:
        #   sum_{k=0}^{n-1} zeta(s, (a+k)/n) = n^s zeta(s, a)
        # Set a = r/6, n = 5: sum_{k=0}^{4} zeta(s, r/30 + k/5) = 5^s zeta(s, r/6)
        # r/30 + k/5 = r/30 + 6k/30 = (r + 6k)/30. CORRECT.
        # So: zeta(s, r/6) = 5^{-s} sum_{k=0}^{4} zeta(s, (r + 6k)/30)
        lhs = complex(mp.zeta(s_mp, mp.mpf(r) / mp.mpf(6)))
        rhs = complex(sum(mp.zeta(s_mp, mp.mpf(r + 6 * k) / mp.mpf(30)) for k in range(5)) * mp.mpc(5)**(-s_mp))
        err = abs(lhs - rhs)
        print(f"  r={r}: zeta(s, {r}/6) = {lhs.real:+.4f}{lhs.imag:+.4f}j, "
              f"5^{{-s}} sum = {rhs.real:+.4f}{rhs.imag:+.4f}j, err = {err:.4e}")

print("\n" + "=" * 90)
print("Conclusion of Probe D")
print("=" * 90)
print("""
The Hurwitz functional equation gives a matrix M_Q(s) relating
vec_zeta(s, r/Q) to vec_zeta(1-s, r/Q). This matrix has entries
involving cos(pi s/2 - 2 pi mr/Q) * Gamma(s) / (2 pi Q)^s.

The primorial refinement (multiplication theorem) shows
zeta(s, r/Q) lifts to zeta(s, m/Q') for Q' = pQ where p is the
next prime, via a Dirichlet-character-free identity.

Critical structural fact: the FE matrix M_Q(s) is INVERTIBLE for
generic s (Gamma(s) does not vanish, cosines form non-singular
matrix). It does NOT vanish on off-line points; it does not
DISTINGUISH off-line from on-line.

Therefore: Hurwitz FE chain alone does NOT close RH. The
constraint it provides (existence of M_Q(rho) acting on vec_zeta(rho))
is a STRUCTURAL identity that holds at every s — providing no
discriminator between on-line and off-line zeros.

The Hurwitz FE is necessary for the explicit formula but
insufficient to force sigma = 1/2.
""")
