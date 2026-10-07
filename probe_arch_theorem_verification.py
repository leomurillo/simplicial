"""
Verify the structural arch theorems at multiple N values:
- N=1 (zeta only): N_E = 0, should FAIL H positivity (mass at -4 is -2).
- N=6 = 2*3: same as N=3 (chi_3 only), N_E = 0, should FAIL.
- N=30: N_E = 3, should PASS H positivity, FAIL J (NSD).
- N=210: N_E = 23, should PASS H, FAIL J (already verified).
- N=2310: N_E = ?, should PASS H, FAIL J.

Theorem 1 prediction: mass at lambda=-4 is -2 + 2*N_E.
"""

import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, zeta, log, pi, matrix

mp.dps = 200

K_MAX = 25  # mu_0 .. mu_24, enough for Hankel up to n=12

# Per-L-function arch cumulant (closed form)
def mu_arch_per_L(k, parity):
    """Even (E): b=1/4; Odd (O): b=3/4. Per L-function contribution."""
    b = mpf(1)/4 if parity == 'E' else mpf(3)/4
    return (-1)**k * zeta(2*k+2, b) / mpf(2)**(2*k+3)

def mu_arch_zeta(k):
    """Zeta contribution including pole pieces."""
    pole = -mpf(2)**(2*k+3)
    psi_part = zeta(2*k+2, mpf(1)/4) / mpf(2)**(2*k+2)
    return (-1)**k * (pole + psi_part) / 2

# Character counts at each N (counting L-functions, not character classes)
# Format: (N_label, N_E_count, N_O_count, descriptor)
test_cases = [
    ("N=1 (zeta only)",              0,  0, "zeta only, N_E=0 → expect FAIL"),
    ("N=6 (zeta + chi_3)",           0,  1, "chi_3 odd, N_E=0 → expect FAIL"),
    ("N=5",                          1,  2, "chi_5(4) even + chi_5(2,3) odd pair, N_E=1 → marginal"),
    ("N=7",                          2,  2, "chi_7 cubic pair even + chi_7(6) odd + chi_7 sextic pair odd"),
    ("N=15",                         3,  4, "chi_5(4) + chi_15(2,8) + chi_3 + chi_5(2,3) + chi_15(14)"),
    ("N=30",                         3,  4, "Same as N=15 since 2 has no chars; primorial"),
    ("N=210",                       23, 24, "Full N=210 from probe (already verified)"),
]

def ldl(M):
    n = M.rows
    A_ = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A_[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A_[k, k]
        diags.append(d)
        if d <= 0:
            return False, k, diags
        for i in range(k+1, n):
            f = A_[i, k] / d
            for j in range(k+1, n):
                A_[i, j] -= f * A_[k, j]
    return True, n, diags

def ldl_neg(M):
    """Check if -M is PSD, i.e., M is NSD."""
    return ldl(-M)

def hankel(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j]
    return M

def hankel_shift(seq, n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = seq[i+j+1]
    return M

print("=" * 80)
print(" Structural arch theorem verification at multiple N")
print("=" * 80)
print(f" mpmath dps = {mp.dps}")
print()

for label, N_E, N_O, desc in test_cases:
    print("-" * 80)
    print(f"  {label}: {desc}")
    print(f"  N_E = {N_E}, N_O = {N_O}, total L-functions = {1 + N_E + N_O}")
    print(f"  Theorem 1 predicted mass at lambda=-4: M_1 = -2 + 2*{N_E} = {-2 + 2*N_E}")

    # Build arch cumulants for this case
    mu_arch = []
    for k in range(K_MAX):
        val = mu_arch_zeta(k)
        val += N_E * mu_arch_per_L(k, 'E')
        val += N_O * mu_arch_per_L(k, 'O')
        mu_arch.append(val)

    # Check leading behavior vs theorem prediction
    M_1 = -2 + 2*N_E
    if M_1 != 0:
        ratio_30 = float(mu_arch[20] / (M_1 * mpf(-4)**20))
        print(f"  Asymptotic check: mu_20 / (M_1 * (-4)^20) = {ratio_30:.6f} (predict ~1.000)")
    else:
        print(f"  M_1 = 0: leading term comes from higher atoms")

    # Hankel tests
    print(f"  {'n':>3}  {'H_n':>8} {'J_n':>8}    {'H_minD':>14} {'J_minD':>14}")
    for n in [0, 1, 2, 3, 5, 8, 12]:
        if 2*n+1 >= K_MAX:
            break
        H = hankel(mu_arch, n)
        J = hankel_shift(mu_arch, n)
        h_psd, _, h_d = ldl(H)
        j_nsd, _, j_d = ldl_neg(J)  # J NSD = -J PSD
        h_status = "PSD" if h_psd else "FAIL"
        j_status = "NSD" if j_nsd else "fail"
        h_md = mp.nstr(min(h_d), 4)
        j_md = mp.nstr(min(j_d), 4)
        print(f"  {n:>3}  {h_status:>8} {j_status:>8}    {h_md:>14} {j_md:>14}")
    print()

print("=" * 80)
print(" Summary")
print("=" * 80)
print()
print("  Theorem 1 predicts H PSD ⟺ N_E ≥ 1 (mass at -4 non-negative).")
print("  Cases above should show:")
print("    N=1 (N_E=0): H FAILS at n=0 already (mu_0^arch < 0).")
print("    N=6 (N_E=0): H FAILS at n=0 already.")
print("    N=5 (N_E=1): H marginal (M_1 = 0, atom at -4 absent).")
print("    N=7+ (N_E ≥ 2): H PSD.")
print("    All N: J NSD (atoms on negative axis).")
