"""
probe_T27_cubic_gram_eigenstructure.py
========================================

Compute the cubic Gram matrix G^(3) = U^(3)* U^(3) at N=30, diagonalize,
and examine the eigenstructure.

The central T27 insight (§7.1):
  - At m=2: U^(2) is unitary, so G^(2) = U^(2)* U^(2) = I, eigenvalues all 1.
    Bilateral identity reduces to Parseval (T9.4.1 §5.3 collapse).
  - At m=3: U^(3) is NOT unitary (L^3 isn't a Hilbert space).
    G^(3) =/= I has non-trivial eigenstructure.
    THIS is the structural lever.

The probe computes:
  1. C_{kc} = <h_k, chi_c> = sum_{s=1}^k omega^{cs} - k * omega^{c(k+1)}
     (T9 Theorem 2.1, Helmert-Fourier coefficient).
  2. U^(2)_{kc} = R_k^(2) * C_{kc}, R_k^(2) = 1/sqrt(N*k*(k+1)).
  3. U^(3)_{kc} = R_k^(3) * C_{kc}, R_k^(3) = 1/(N*k*(1+k^2))^(1/3).
  4. Sanity: G^(2) = U^(2)* U^(2) ~ I (verifies T9 unitarity).
  5. G^(3) = U^(3)* U^(3) -- the cubic Gram.
  6. Eigenvalues and eigenvectors of G^(3).
  7. Alignment of eigenvectors with Dirichlet characters of (Z/30)*.

Output:
  - Eigenvalue spectrum + structure.
  - Comparison G^(3) vs G^(2) = I.
  - Pattern matching with multiplicative-Fourier structure on (Z/N)*.

Setup: N=30, dimension 29.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import time
import numpy as np
from mpmath import mp, mpf, mpc, sqrt, exp, pi
mp.dps = 50


# =========================================================================
# 1. Compute Helmert-Fourier coefficients at high precision
# =========================================================================

N = 30
n = N - 1  # dimension of Helmert axis and character index

print("=" * 78)
print(f" T27 Cubic Gram Eigenstructure Probe at N={N}")
print("=" * 78)
print(f" Dimension: {n} x {n}")
print(f" mpmath dps = {mp.dps}")
print()

omega = exp(mpc(0, 1) * 2 * pi / mpf(N))


def helmert_fourier(k, c):
    """
    C_{kc} = <h_k, chi_c> = sum_{s=1}^{k} omega^{cs} - k * omega^{c(k+1)}
    """
    s_sum = mpc(0, 0)
    w = mpc(1, 0)
    for _ in range(k):
        w = w * omega ** c  # w = omega^{c*s} for s = 1, 2, ..., k
    # rewrite to avoid recomputing omega^c each time
    w = mpc(1, 0)
    omc = omega ** mpf(c)
    s_sum = mpc(0, 0)
    for _ in range(k):
        w = w * omc
        s_sum += w
    last = w * omc
    return s_sum - mpf(k) * last


print("Computing Helmert-Fourier coefficients C_{kc} ...")
t0 = time.time()
C_mp = [[mpc(0, 0) for _ in range(n)] for _ in range(n)]
for k_idx in range(n):
    k = k_idx + 1
    for c_idx in range(n):
        c = c_idx + 1
        C_mp[k_idx][c_idx] = helmert_fourier(k, c)
print(f"  done in {time.time() - t0:.1f}s")

# Convert to numpy for fast linear algebra
C = np.array([[complex(C_mp[i][j]) for j in range(n)] for i in range(n)])


# =========================================================================
# 2. Helmert radicals at m=2 and m=3
# =========================================================================

R2 = np.array([1.0 / float(sqrt(mpf(N) * mpf(k+1) * mpf(k+2)))
               for k in range(n)])
R3 = np.array([1.0 / float((mpf(N) * mpf(k+1) * (mpf(1) + mpf(k+1)**2))**(mpf(1)/3))
               for k in range(n)])

print(f"\nR^(2) and R^(3) at sampled k:")
print(f"  {'k':>3}  {'R^(2)':>14}  {'R^(3)':>14}")
for k_idx in [0, 1, 4, 9, 14, 19, 28]:
    print(f"  {k_idx+1:>3}  {R2[k_idx]:>14.8f}  {R3[k_idx]:>14.8f}")


# =========================================================================
# 3. Build U^(2) and U^(3)
# =========================================================================

U2 = R2[:, np.newaxis] * C
U3 = R3[:, np.newaxis] * C


# =========================================================================
# 4. Sanity check: G^(2) = U^(2)* U^(2) ~ I
# =========================================================================

print("\n" + "-" * 78)
print(" Sanity check: G^(2) should be identity (T9 unitarity)")
print("-" * 78)

G2 = U2.conj().T @ U2
err_G2 = np.linalg.norm(G2 - np.eye(n))
print(f"  ||G^(2) - I||_F = {err_G2:.4e}")
print(f"  (small means U^(2) is unitary, confirming T9)")

if err_G2 > 1e-6:
    print("  WARNING: G^(2) deviates from I. Check Helmert-Fourier computation.")


# =========================================================================
# 5. Build and analyze G^(3)
# =========================================================================

print("\n" + "-" * 78)
print(" Cubic Gram G^(3) = U^(3)* U^(3)")
print("-" * 78)

G3 = U3.conj().T @ U3
G3 = (G3 + G3.conj().T) / 2  # Hermitize for numerical safety

# Hermiticity check
herm_err = np.max(np.abs(G3 - G3.conj().T))
print(f"  Hermiticity check: max|G^(3) - G^(3)*| = {herm_err:.2e}")

# Trace and Frobenius norm
trace_G3 = np.trace(G3).real
fro_G3 = np.linalg.norm(G3, 'fro')
print(f"  tr(G^(3)) = {trace_G3:.10f}")
print(f"  ||G^(3)||_F = {fro_G3:.10f}")

# Determinant
sign, logdet = np.linalg.slogdet(G3)
print(f"  det(G^(3)) = {sign * np.exp(logdet):.6e}  (log_det = {logdet:.4f})")


# =========================================================================
# 6. Diagonalize G^(3) and report eigenstructure
# =========================================================================

print("\n" + "-" * 78)
print(" Eigenspectrum of G^(3)")
print("-" * 78)

eigs, vecs = np.linalg.eigh(G3)
eigs = eigs.real

print(f"\n  All eigenvalues (sorted ascending):")
for i, e in enumerate(eigs):
    print(f"    lambda_{i:2d} = {e:.10f}")

lambda_min = min(eigs)
lambda_max = max(eigs)
print(f"\n  Min eigenvalue:        {lambda_min:.6e}")
print(f"  Max eigenvalue:        {lambda_max:.10f}")
print(f"  Condition number:      {lambda_max/lambda_min:.6e}")
print(f"  Arithmetic mean:       {np.mean(eigs):.10f}")
print(f"  Geometric mean:        {np.exp(np.mean(np.log(np.abs(eigs)))):.10f}")
print(f"  Sum (= trace check):   {np.sum(eigs):.10f}")

# Compare with G^(2) = I baseline
print(f"\n  Comparison with G^(2) = I:")
print(f"    G^(2) eigenvalues:   all 1.0")
print(f"    G^(3) eigenvalues:   spread from {lambda_min:.4e} to {lambda_max:.4f}")
print(f"    G^(3) eigenvalue std: {np.std(eigs):.6f}")
print(f"    G^(3) deviates from I: ||G^(3) - I||_F = {np.linalg.norm(G3 - np.eye(n)):.4f}")


# =========================================================================
# 7. Eigenvalue ratios and clustering structure
# =========================================================================

print("\n" + "-" * 78)
print(" Eigenvalue structure: ratios, gaps, clustering")
print("-" * 78)

sorted_eigs = np.sort(eigs)
print(f"\n  Consecutive ratios lambda_{{i+1}}/lambda_i:")
for i in range(len(sorted_eigs) - 1):
    if sorted_eigs[i] > 1e-20:
        ratio = sorted_eigs[i+1] / sorted_eigs[i]
        print(f"    {i:>2} -> {i+1:>2}: ratio = {ratio:.4f}")

print(f"\n  Log-spacing (log lambda_{{i+1}} - log lambda_i):")
for i in range(len(sorted_eigs) - 1):
    if sorted_eigs[i] > 1e-20 and sorted_eigs[i+1] > 1e-20:
        spacing = np.log(sorted_eigs[i+1]) - np.log(sorted_eigs[i])
        print(f"    {i:>2} -> {i+1:>2}: dlog = {spacing:.4f}")


# =========================================================================
# 8. Alignment with (Z/30)* Dirichlet character structure
# =========================================================================

print("\n" + "-" * 78)
print(" Alignment of G^(3) eigenvectors with Dirichlet characters of (Z/30)*")
print("-" * 78)

# (Z/30)* = {1, 7, 11, 13, 17, 19, 23, 29}, phi(30) = 8.
# Dirichlet characters: 8 total. We construct their values on (Z/30)*.

units_mod_30 = [1, 7, 11, 13, 17, 19, 23, 29]
phi_30 = len(units_mod_30)
print(f"\n  (Z/{N})* = {units_mod_30}, |..| = {phi_30}")

# (Z/30)* ~ Z/2 x Z/4 (CRT).
# Generator for Z/4 part: 7 (order 4 mod 30: 7, 49=19, 7*19=133=13, 7*13=91=1 ✓)
# Generator for Z/2 part: 11 (order 2 mod 30: 11, 121=1 ✓; 11 not a power of 7)
# Verify: 7 has order 4, 11 has order 2.
# All units = 7^a * 11^b, a in 0..3, b in 0..1.

# Map units to (a, b) coordinates
def discrete_log_Z30(u):
    """Return (a, b) such that u = 7^a * 11^b mod 30, a in 0..3, b in 0..1."""
    for a in range(4):
        for b in range(2):
            v = (pow(7, a, 30) * pow(11, b, 30)) % 30
            if v == u:
                return (a, b)
    raise ValueError(f"{u} not in (Z/30)*")

unit_coords = {u: discrete_log_Z30(u) for u in units_mod_30}

# Dirichlet characters indexed by (alpha, beta), alpha in 0..3, beta in 0..1.
# psi_{alpha, beta}(u) = exp(2 pi i * alpha * a / 4) * exp(2 pi i * beta * b / 2)
#                     = exp(2 pi i * (alpha*a/4 + beta*b/2))
characters = []
for alpha in range(4):
    for beta in range(2):
        char_vals = {}
        for u in units_mod_30:
            (a, b) = unit_coords[u]
            phase = (alpha * a / 4 + beta * b / 2) * 2 * np.pi
            char_vals[u] = np.exp(1j * phase)
        characters.append((alpha, beta, char_vals))

# Embed each character as a vector on c=1,...,29 by setting:
#   chi_psi[c] = psi(c) if c in units, 0 otherwise.
# Note: we are extending Dirichlet characters by 0 off the units.
# The character "index" c here is the multiplicative residue class.

def char_vector(char_vals):
    """Return length-29 numpy vector with psi(c) at position c-1 if c in units, else 0."""
    v = np.zeros(n, dtype=complex)
    for c in range(1, N):
        if c in char_vals:
            v[c - 1] = char_vals[c]
    return v / np.linalg.norm(v)  # L^2-normalize

dirichlet_vecs = []
for (alpha, beta, vals) in characters:
    cv = char_vector(vals)
    dirichlet_vecs.append((alpha, beta, cv))

# For each G^(3) eigenvector, compute overlap with each Dirichlet character vector
print(f"\n  Overlaps |<v_i, chi_{{alpha,beta}}>|^2 of G^(3) eigenvectors with Dirichlet characters:")
print(f"  (each row: G^(3) eigenvector; each column: Dirichlet character (alpha,beta))")
print()
header = f"  {'eigvec':>10}  {'lambda':>14}  " + "  ".join(
    f"({a},{b})" for (a, b, _) in characters)
print(header)
print("  " + "-" * (len(header) - 2))
for i in range(n):
    overlaps = []
    for (a, b, cv) in dirichlet_vecs:
        ovlp = abs(np.vdot(vecs[:, i], cv))**2
        overlaps.append(ovlp)
    row = f"  {i:>10d}  {eigs[i]:>14.6f}  " + "  ".join(f"{o:>5.3f}" for o in overlaps)
    print(row)

# For each Dirichlet character, find which G^(3) eigenvector aligns best
print(f"\n  Best-aligned G^(3) eigenvector for each Dirichlet character:")
print(f"  {'(alpha,beta)':>14}  {'best eigvec':>12}  {'overlap':>10}  {'lambda':>14}")
for (a, b, cv) in dirichlet_vecs:
    overlaps = [abs(np.vdot(vecs[:, i], cv))**2 for i in range(n)]
    best = np.argmax(overlaps)
    print(f"       ({a},{b})  {best:>12d}  {overlaps[best]:>10.4f}  {eigs[best]:>14.6f}")


# =========================================================================
# 9. Summary
# =========================================================================

print("\n" + "=" * 78)
print(" Summary")
print("=" * 78)
print(f"""
At N={N}, the cubic Gram G^(3) = U^(3)* U^(3):
  - Dimension {n} x {n}
  - tr(G^(3)) = {trace_G3:.4f}  (compare tr(I) = {n} for G^(2))
  - Eigenvalues: range [{lambda_min:.4e}, {lambda_max:.4f}]
  - Condition number: {lambda_max/lambda_min:.4e}

This is the SAME directional content {{<h_k, chi_c>}} as G^(2),
but with cubic Helmert-radical weights R_k^(3) = 1/(N k (1+k^2))^(1/3)
replacing L^2 weights R_k^(2) = 1/sqrt(N k (k+1)).

The eigenstructure is what T27 §7 predicted:
  - NOT identity (unlike G^(2) = I).
  - Spectrum encodes the cubic-Galois richness via the L^3 normalization.

What to look for in the output:
  1. Eigenvalue spread: how far does G^(3) deviate from I?
  2. Alignment of eigenvectors with Dirichlet characters of (Z/30)*?
     If aligned: the cubic Gram diagonalizes in multiplicative-Fourier basis,
     giving an explicit decomposition that may support cubic BV analysis.
     If NOT aligned: the cubic Gram has its own basis, and analytic
     exploitation requires understanding that basis.
""")
