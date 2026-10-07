"""
Probe C: Cross-Gram Ramanujan matrix on primorials Q in {6, 30, 210}.

From Paper 9 (Conductor Block Spectral Compounds):
   <T_eps v_a, T_eta v_b> = Q^{-1} sum_{d | Q, d != 1} eps_d eta_d C_d(a-b)

where C_d(h) is the Ramanujan sum:
   C_d(h) = sum_{k coprime to d, 1<=k<=d} exp(2 pi i k h / d)
          = mu(d/gcd(d,h)) * phi(d) / phi(d/gcd(d,h))   (Holder formula)

We build the matrix M_Q(a, b) := sum_{d | Q, d != 1} C_d(a - b)
(taking eps_d = eta_d = 1 for the orientation-symmetric "uniform" case),
which is the indicator-conductor-block compound Gram on Z/Q.

Goal: examine eigenvalue spectrum at Q = 6, 30, 210; look for structure
connecting to Riemann zeta-zero distribution {14.13, 21.02, 25.01, 30.42, ...}.
"""

import numpy as np
import mpmath as mp
from math import gcd

mp.mp.dps = 30


def ramanujan_sum(d, h):
    """C_d(h) = sum_{k=1, gcd(k,d)=1}^{d} exp(2 pi i k h / d)."""
    if d == 1:
        return 1.0
    g = gcd(d, h) if h != 0 else d
    n = d // g
    phi_n = sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)
    if phi_n == 0:
        return 0.0
    mu = mobius(n)
    phi_d = sum(1 for k in range(1, d + 1) if gcd(k, d) == 1)
    return mu * phi_d / phi_n


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
    divs = []
    for d in range(1, n + 1):
        if n % d == 0:
            divs.append(d)
    return divs


def cross_gram_matrix(Q, exclude_d_1=True):
    """
    M_Q(a, b) = sum_{d | Q, d != 1} C_d(a - b)   if exclude_d_1
              = sum_{d | Q} C_d(a - b) = Q if a == b else 0   otherwise.

    Note: full sum (including d=1) recovers Kluyver's identity:
        sum_{d | Q} C_d(h) = Q if Q | h else 0  (for h in Z/Q, this is Q*[h==0])
    """
    M = np.zeros((Q, Q), dtype=complex)
    divs = [d for d in divisors(Q) if (not exclude_d_1 or d != 1)]
    for a in range(Q):
        for b in range(Q):
            h = (a - b) % Q
            val = sum(ramanujan_sum(d, h) for d in divs)
            M[a, b] = val
    return M / Q  # normalize by Q^{-1} from Paper 9 formula


def analyze(Q):
    print(f"\n{'=' * 80}")
    print(f"Q = {Q}, divisors = {divisors(Q)}")
    print(f"{'=' * 80}")
    M = cross_gram_matrix(Q, exclude_d_1=True)
    eigvals = np.linalg.eigvalsh(M.real)  # M is real symmetric by construction
    eigvals_sorted = np.sort(eigvals)[::-1]
    print(f"Eigenvalues (sorted desc):")
    for i, e in enumerate(eigvals_sorted):
        print(f"  lambda_{i} = {e:+.10f}")
    print(f"Sum  = {eigvals.sum():+.10f}")
    print(f"Prod = {np.prod(eigvals):+.10e}")
    print(f"Trace M = {np.trace(M).real:+.10f}")
    print(f"||M||_F = {np.linalg.norm(M, 'fro'):.10f}")
    print(f"Rank (numerical) = {np.linalg.matrix_rank(M, tol=1e-10)}")

    # Multiplicity structure
    unique, counts = np.unique(np.round(eigvals_sorted, 10), return_counts=True)
    print(f"\nMultiplicity structure:")
    for u, c in sorted(zip(unique, counts), key=lambda x: -x[0]):
        print(f"  lambda = {u:+.10f}  multiplicity {c}")

    # Decomposition per divisor
    print(f"\nPer-divisor contribution (first row, h = b - a in Z/Q):")
    for d in divisors(Q):
        if d == 1:
            continue
        row = [ramanujan_sum(d, h) / Q for h in range(min(Q, 12))]
        print(f"  d = {d:3d}: C_d(.)/Q = {[f'{r:+.5f}' for r in row]}")

    return M, eigvals_sorted


for Q in [6, 30, 210]:
    analyze(Q)

print("\n" + "=" * 80)
print("Now compare: spacings of |eigvals| at Q = 30, 210 vs first ζ-zero spacings")
print("(zeta zeros: 14.13, 21.02, 25.01, 30.42, 32.94, 37.59, ...)")
print("=" * 80)

zeta_zeros = [14.134725, 21.022040, 25.010858, 30.424876,
              32.935062, 37.586178, 40.918719, 43.327073,
              48.005151, 49.773832]

for Q in [30, 210]:
    M, eigs = analyze.__wrapped__(Q) if hasattr(analyze, '__wrapped__') else (None, None)
    # Re-run to get eigs
    M = cross_gram_matrix(Q, exclude_d_1=True)
    eigs = np.sort(np.linalg.eigvalsh(M.real))[::-1]
    eigs_nz = eigs[np.abs(eigs) > 1e-10]
    spacings = -np.diff(eigs_nz)
    print(f"\nQ = {Q}: first 10 eigenvalue spacings (nonzero eigs only):")
    for i, sp in enumerate(spacings[:10]):
        print(f"  Delta_{i} = {sp:.6f}")
    print(f"\n  zeta zero spacings (first 9): {[f'{zeta_zeros[i+1]-zeta_zeros[i]:.4f}' for i in range(9)]}")
