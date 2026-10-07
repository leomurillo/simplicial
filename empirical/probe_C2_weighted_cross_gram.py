"""
Probe C2: Weighted cross-Gram on Z/Q with non-uniform divisor weights.

Generalization of Probe C: the Paper 9 cross-Gram
   M_{eps,eta}(a, b) = Q^{-1} sum_{d | Q, d != 1} eps_d eta_d C_d(a - b)

becomes structurally interesting when eps_d, eta_d carry arithmetic data.
Cases we examine:

1. UNIFORM: eps_d = 1 (Probe C; projection, all eigs = 1 or 0)
2. MOBIUS: eps_d = mu(d) (Mobius-weighted; connects to 1/zeta)
3. SQUAREFREE INDICATOR: eps_d = |mu(d)| (squarefree only)
4. CHARACTER chi_3 LIFTED: eps_d = chi_3(d) where chi_3 = Legendre mod 3,
   extended by 0 on 3|d
5. CHARACTER chi_6 LIFTED: similar for chi_6
6. VON MANGOLDT-LIKE: eps_d = sqrt(d) * mu(d) (link to explicit formula)
7. PRIMORIAL-LADDER: eps_d = +1 if d is a primorial divisor of Q, else 0

We compute eigenvalues of M_{eps,eps} (real-symmetric) and look for
correspondences with the first 10 zeta-zero imaginary parts:
   {14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77}

The matrix is translation-invariant (depends only on a-b), so diagonalized
by Fourier basis on Z/Q. Eigenvalues are indexed by k in Z/Q.
"""

import numpy as np
from math import gcd

# ----- Number-theoretic helpers -----

def mobius(n):
    if n == 1:
        return 1
    p = 2
    result = 1
    nn = n
    while p * p <= nn:
        if nn % p == 0:
            nn //= p
            if nn % p == 0:
                return 0
            result = -result
        p += 1
    if nn > 1:
        result = -result
    return result


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def euler_phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def ramanujan_sum(d, h):
    if d == 1:
        return 1.0
    h_mod = h % d
    g = gcd(d, h_mod) if h_mod != 0 else d
    n = d // g
    mu_n = mobius(n)
    if mu_n == 0:
        return 0.0
    return mu_n * euler_phi(d) / euler_phi(n)


def chi_3(d):
    """Legendre symbol mod 3, extended by 0 on 3|d."""
    if d % 3 == 0:
        return 0
    return 1 if d % 3 == 1 else -1


def chi_6(d):
    """Non-trivial character mod 6: chi_6(d) = chi_3(d) * chi_2(d) where chi_2 is trivial."""
    if gcd(d, 6) > 1:
        return 0
    # d coprime to 6, d in {1, 5}: chi_6(1) = 1, chi_6(5) = -1
    return 1 if d % 6 == 1 else -1


# ----- Weight assignments -----

WEIGHTS = {
    'uniform': lambda d: 1.0,
    'mobius': lambda d: float(mobius(d)),
    'squarefree': lambda d: 1.0 if mobius(d) != 0 else 0.0,
    'chi_3': lambda d: float(chi_3(d)),
    'chi_6': lambda d: float(chi_6(d)),
    'von_mangoldt': lambda d: np.sqrt(d) * mobius(d),
    'log_d': lambda d: np.log(d) if d > 1 else 0.0,
    'phi_d': lambda d: float(euler_phi(d)),
    'inv_phi_d': lambda d: 1.0 / euler_phi(d) if euler_phi(d) > 0 else 0.0,
}


def cross_gram_weighted(Q, weight_fn, exclude_d_1=True):
    M = np.zeros((Q, Q))
    divs = [d for d in divisors(Q) if (not exclude_d_1 or d != 1)]
    weights = {d: weight_fn(d) for d in divs}
    for a in range(Q):
        for b in range(Q):
            h = (a - b) % Q
            val = sum(weights[d] ** 2 * ramanujan_sum(d, h) for d in divs)
            M[a, b] = val
    return M / Q


def analyze_weighted(Q, weight_name, weight_fn):
    M = cross_gram_weighted(Q, weight_fn)
    eigvals = np.sort(np.linalg.eigvalsh(M))[::-1]
    nonzero = eigvals[np.abs(eigvals) > 1e-10]
    return eigvals, nonzero


# ----- Run scan -----

zeta_zeros = [14.134725, 21.022040, 25.010858, 30.424876,
              32.935062, 37.586178, 40.918719, 43.327073,
              48.005151, 49.773832]

print("=" * 100)
print("Probe C2: Weighted Ramanujan cross-Gram spectra")
print("=" * 100)

for Q in [6, 30, 210]:
    print(f"\n{'=' * 80}\nQ = {Q}, divisors = {divisors(Q)}\n{'=' * 80}")
    print(f"{'weight':>20s}  {'spectrum (top 10 nonzero eigenvalues)':<70s}")
    print("-" * 100)
    for name, fn in WEIGHTS.items():
        eigvals, nonzero = analyze_weighted(Q, name, fn)
        spectrum = ", ".join(f"{e:+.4f}" for e in nonzero[:10])
        n_distinct = len(np.unique(np.round(nonzero, 8)))
        print(f"{name:>20s}  {spectrum:<70s}  [{len(nonzero)} nonzero, {n_distinct} distinct]")

# ----- Look at distinct eigenvalues for "structural" weights -----
print("\n" + "=" * 100)
print("Detail: distinct eigenvalues by weight at Q = 30 and 210")
print("Goal: any rational/algebraic eigenvalue connecting to zeta_zero structure?")
print("=" * 100)

for Q in [30, 210]:
    print(f"\nQ = {Q}:")
    for name in ['mobius', 'chi_3', 'chi_6', 'von_mangoldt', 'log_d']:
        fn = WEIGHTS[name]
        eigvals, nonzero = analyze_weighted(Q, name, fn)
        unique_eigs = np.unique(np.round(eigvals, 8))
        unique_eigs_sorted = sorted([u for u in unique_eigs if abs(u) > 1e-8], reverse=True)
        mults = [int(np.sum(np.abs(eigvals - u) < 1e-7)) for u in unique_eigs_sorted]
        # Check for any near-zero negative eigenvalues (non-PSD case)
        neg = [e for e in unique_eigs if e < -1e-8]
        print(f"  {name:>15s}: {len(unique_eigs_sorted)} distinct nonzero eigs, multiplicities: "
              f"{list(zip([f'{u:+.4f}' for u in unique_eigs_sorted[:10]], mults[:10]))}")
        if neg:
            print(f"    (Has negative eigenvalues: {[f'{n:+.4e}' for n in neg]})")

# ----- Test for Hilbert-Pólya connection: is there a "spectral operator" whose
# eigenvalues match zeta zero gaps? -----
print("\n" + "=" * 100)
print("Test: do any eigenvalue gaps match zeta-zero gaps?")
print("=" * 100)

zero_gaps = [zeta_zeros[i+1] - zeta_zeros[i] for i in range(len(zeta_zeros) - 1)]
print(f"\nZeta-zero gaps (first 9): {[f'{g:.4f}' for g in zero_gaps]}")

for Q in [30, 210]:
    for name in ['von_mangoldt', 'log_d']:
        fn = WEIGHTS[name]
        eigvals, nonzero = analyze_weighted(Q, name, fn)
        eigvals_sorted = sorted(eigvals, reverse=True)
        eig_gaps = [eigvals_sorted[i] - eigvals_sorted[i+1] for i in range(min(9, len(eigvals_sorted) - 1))]
        print(f"\n  Q={Q}, {name}: eigenvalue gaps = {[f'{g:.4f}' for g in eig_gaps]}")
