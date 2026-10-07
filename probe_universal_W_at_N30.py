"""
probe_universal_W_at_N30.py
============================

The probe of the universal unitary W := sqrt(D^(2)) * C — equivalently, T9's U^(2)
— the Helmert-Fourier transfer matrix that simultaneously diagonalizes the
entire gauge corridor's Gram operators {G^(m) : m in Z}.

By the m=6 probe's theoretical clean-up:
  G^(m) = W* E^(m) W, where E^(m) = D^(m)/D^(2) is diagonal,
  W is unitary, and W is INDEPENDENT of m.

So the gauge-corridor variation is entirely in the diagonal E^(m).
The L-function content (if any in the simplicial framework at primorial N)
lives in W.

Probe targets:
  1. W eigenvalues on the unit circle.
  2. W eigenvector decomposition.
  3. Alignment with Dirichlet characters of (Z/30)*.
  4. Conductor-orbit structure under the Galois action c -> a*c, a in (Z/N)*.
  5. Trace identities tr(W), tr(W^k).
  6. Action on prime-arithmetic vector: W @ vec(Lambda).
  7. Spectrum of W^* M W for M = (entries (c, c') = 1/((c-c') if c-c' != 0 else 0))
     or other natural operators tied to L-functions.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import time
import numpy as np
from mpmath import mp, mpf, mpc, sqrt, exp, pi
mp.dps = 50


# =========================================================================
# Setup
# =========================================================================

N = 30
n = N - 1

print("=" * 78)
print(f" Universal W Probe at N={N}")
print("=" * 78)
print(f" Dimension: {n} x {n}")
print()

omega = exp(mpc(0, 1) * 2 * pi / mpf(N))


# =========================================================================
# 1. Build W = sqrt(D^(2)) C
# =========================================================================

print("Computing Helmert-Fourier coefficients C_{kc}...")
t0 = time.time()
C_mp = [[mpc(0, 0) for _ in range(n)] for _ in range(n)]
for k_idx in range(n):
    k = k_idx + 1
    for c_idx in range(n):
        c = c_idx + 1
        omc = omega ** mpf(c)
        s_sum = mpc(0, 0)
        w = mpc(1, 0)
        for _ in range(k):
            w = w * omc
            s_sum += w
        last = w * omc
        C_mp[k_idx][c_idx] = s_sum - mpf(k) * last
print(f"  done in {time.time() - t0:.1f}s")

C = np.array([[complex(C_mp[i][j]) for j in range(n)] for i in range(n)])

R2 = np.array([1.0 / float(sqrt(mpf(N) * mpf(k+1) * mpf(k+2))) for k in range(n)])

# W = diag(R2) * C  (this is T9's U^(2))
W = R2[:, np.newaxis] * C

# Verify unitarity
err_unit = np.linalg.norm(W.conj().T @ W - np.eye(n))
print(f"\nUnitarity check ||W*W - I||_F = {err_unit:.4e}")


# =========================================================================
# 2. Eigenvalues of W on unit circle
# =========================================================================

print("\n" + "-" * 78)
print(" W eigenspectrum on the unit circle")
print("-" * 78)

W_eigs, W_vecs = np.linalg.eig(W)

# All eigenvalues should have |lambda| = 1 (unitary)
moduli = np.abs(W_eigs)
print(f"  |eigenvalue| range: [{min(moduli):.10f}, {max(moduli):.10f}]")
print(f"  (should all be 1.0 for unitary W)")

# Sort by angle
angles = np.angle(W_eigs)
angles_sorted = np.sort(angles)
print(f"\n  Eigenvalue angles (in units of pi):")
for i, theta in enumerate(angles_sorted):
    pi_frac = theta / np.pi
    print(f"    arg(lambda_{i:2d}) = {pi_frac:+.6f} pi")


# =========================================================================
# 3. Search for natural eigenvalue structure
# =========================================================================

print("\n" + "-" * 78)
print(" Search for natural eigenvalue structure")
print("-" * 78)

# Check if eigenvalues are roots of unity (z^k = 1 for some k)
print(f"\n  Check: are W eigenvalues N-th roots of unity?")
test_N_roots = np.array([np.exp(2j*np.pi*k/N) for k in range(N)])
matches = []
for ev in W_eigs:
    closest = min(test_N_roots, key=lambda z: abs(z - ev))
    err = abs(closest - ev)
    matches.append(err)
print(f"    Max distance from nearest N={N}-th root: {max(matches):.4e}")

# Try 2N, 4N roots
for trial_N in [2*N, 4*N, N**2, 2*N**2]:
    roots = np.array([np.exp(2j*np.pi*k/trial_N) for k in range(trial_N)])
    errs = [min(abs(roots - ev)) for ev in W_eigs]
    max_err = max(errs)
    print(f"    Max distance from nearest {trial_N}-th root: {max_err:.4e}")

# Test: sum of all eigenvalues = trace(W)
trace_W = np.trace(W)
print(f"\n  tr(W) = {trace_W.real:+.6f} + {trace_W.imag:+.6f}i")
print(f"  sum(eigs) = {sum(W_eigs).real:+.6f} + {sum(W_eigs).imag:+.6f}i")

# Test W^N = ?
W_pow = W.copy()
for k_pow in [2, 3, 4, 6, N]:
    W_p = np.linalg.matrix_power(W, k_pow)
    # Check if proportional to I
    diag_avg = np.trace(W_p) / n
    deviation = np.linalg.norm(W_p - diag_avg * np.eye(n))
    print(f"  W^{k_pow}: ||W^{k_pow} - (tr/n)I||_F = {deviation:.4e}, tr/n = {diag_avg:+.4f}+{diag_avg.imag:+.4f}i")


# =========================================================================
# 4. Galois action: c -> a*c for a in (Z/N)*
# =========================================================================

print("\n" + "-" * 78)
print(" Galois action: conductor orbit decomposition")
print("-" * 78)

# Conductor of chi_c (additive char with index c in Z/N): N/gcd(c, N)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

conductor_of_c = {c: N // gcd(c, N) for c in range(1, N)}
print(f"\n  Conductor of chi_c for c=1..{N-1}:")
print(f"    {dict(sorted(conductor_of_c.items()))}")

# Conductor orbits (Galois action of (Z/N)* permutes characters with same conductor)
from collections import defaultdict
orbits = defaultdict(list)
for c in range(1, N):
    orbits[conductor_of_c[c]].append(c)
print(f"\n  Conductor orbits (size phi(d) at conductor d):")
for d in sorted(orbits.keys()):
    print(f"    conductor d={d:>3}: size phi({d})={len(orbits[d])}, c in {orbits[d]}")


# =========================================================================
# 5. W's action on conductor-orbit subspaces
# =========================================================================

print("\n" + "-" * 78)
print(" Does W preserve conductor-orbit subspaces?")
print("-" * 78)

# For each conductor d, build the orthogonal projection onto the subspace
# spanned by the additive characters chi_c with c in orbit_d.
# Compute commutator [W, P_d]; if ~ 0, W preserves this subspace.

print(f"  {'conductor d':>14}  {'orbit size':>11}  {'||[W, P_d]||_F':>18}")
for d in sorted(orbits.keys()):
    cs = orbits[d]
    # P_d projects onto e_c for c in cs (standard basis vectors)
    P_d = np.zeros((n, n))
    for c in cs:
        P_d[c-1, c-1] = 1.0
    commutator = W @ P_d - P_d @ W
    err = np.linalg.norm(commutator)
    print(f"    d={d:>3} ({'split' if d==30 else '   '})  {len(cs):>11}  {err:>18.4e}")


# =========================================================================
# 6. Dirichlet character alignment with W eigenvectors
# =========================================================================

print("\n" + "-" * 78)
print(" Dirichlet character alignment with W eigenvectors")
print("-" * 78)

units_mod_30 = [1, 7, 11, 13, 17, 19, 23, 29]


def discrete_log_Z30(u):
    for a in range(4):
        for b in range(2):
            if (pow(7, a, 30) * pow(11, b, 30)) % 30 == u:
                return (a, b)
    raise ValueError(u)


unit_coords = {u: discrete_log_Z30(u) for u in units_mod_30}

# 8 Dirichlet characters of (Z/30)*
characters = []
for alpha in range(4):
    for beta in range(2):
        char_vals = {u: np.exp(1j * 2 * np.pi * (alpha * unit_coords[u][0] / 4 +
                                                  beta * unit_coords[u][1] / 2))
                     for u in units_mod_30}
        characters.append((alpha, beta, char_vals))


def char_vec_on_chars(char_vals):
    """Embed Dirichlet character psi: (Z/30)* -> C as a vector indexed by additive characters
    chi_c for c=1..N-1. Set psi(c) at position c-1 if c in units, 0 otherwise."""
    v = np.zeros(n, dtype=complex)
    for c in range(1, N):
        if c in char_vals:
            v[c - 1] = char_vals[c]
    return v / np.linalg.norm(v)


dirichlet_vecs = [(a, b, char_vec_on_chars(vals)) for (a, b, vals) in characters]

# Test: does W act on Dirichlet vector dv as scaling?
print(f"\n  Action of W on Dirichlet vectors: W*dv / dv (if eigenvector, this is constant)")
print(f"  {'(alpha,beta)':>14}  {'||W*dv||':>10}  {'overlap with eigvec':>22}  {'best eigval':>22}")
for (a, b, dv) in dirichlet_vecs:
    Wdv = W @ dv
    Wdv_norm = np.linalg.norm(Wdv)
    # overlap with W's eigenvectors
    proj = np.abs(W_vecs.conj().T @ dv) ** 2
    best = np.argmax(proj)
    eigval_best = W_eigs[best]
    arg = np.angle(eigval_best) / np.pi
    print(f"       ({a},{b})  {Wdv_norm:>10.6f}  v_{best:>2} @ overlap={proj[best]:>6.4f}  "
          f"  arg/pi = {arg:>+8.4f}")


# =========================================================================
# 7. W on prime-arithmetic vector
# =========================================================================

print("\n" + "-" * 78)
print(" Action of W on prime-arithmetic vector vec(Lambda)")
print("-" * 78)

# Build the von Mangoldt vector at c = 1..N-1
# Lambda(n) = log p if n = p^k, else 0
from math import log


def is_prime_power(n):
    if n < 2:
        return None
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            x = n
            while x % p == 0:
                x //= p
            if x == 1:
                return p
            return None
    return n  # n itself is prime


def vonMangoldt(n):
    p = is_prime_power(n)
    return log(p) if p else 0.0


Lambda_vec = np.array([vonMangoldt(c) for c in range(1, N)])
print(f"\n  Lambda(c) for c=1..{N-1}:")
print(f"    {Lambda_vec.round(4).tolist()}")

W_Lambda = W @ Lambda_vec
print(f"\n  ||vec(Lambda)|| = {np.linalg.norm(Lambda_vec):.6f}")
print(f"  ||W * vec(Lambda)|| = {np.linalg.norm(W_Lambda):.6f} (should equal above since W unitary)")

# Decompose W*Lambda in the W eigenbasis
W_Lambda_in_W_basis = W_vecs.conj().T @ Lambda_vec
print(f"\n  |coefficients of vec(Lambda) in W eigenbasis|, sorted descending:")
coeffs = np.abs(W_Lambda_in_W_basis) ** 2
order = np.argsort(coeffs)[::-1]
for i, idx in enumerate(order[:10]):
    eigval = W_eigs[idx]
    arg = np.angle(eigval) / np.pi
    print(f"    coef_{i} = {coeffs[idx]:.6f}  (eigvec_{idx}, eigval @ arg/pi = {arg:+.4f})")


# =========================================================================
# 8. Trace identities
# =========================================================================

print("\n" + "-" * 78)
print(" Trace identities")
print("-" * 78)

for k_pow in [1, 2, 3, 4, 5, 6, 10, 15, 29, 30]:
    if k_pow == 1:
        T = trace_W
    else:
        T = np.trace(np.linalg.matrix_power(W, k_pow))
    print(f"  tr(W^{k_pow:>2}) = {T.real:+12.6f} + {T.imag:+12.6f}i, |.|={abs(T):.4f}")


# =========================================================================
# 9. Spectral content tied to L-function zeros?
# =========================================================================

print("\n" + "-" * 78)
print(" L-function zero connection?")
print("-" * 78)

# Hypothesis: W's eigenvalue angles theta_j = arg(lambda_j) might cluster
# near values related to zeros of L-functions mod 30.
#
# At N=30, the first zeros of L(chi_3, s) are at gamma ~ 8.04, 11.25, ...
# and zeta zeros at 14.13, 21.02, 25.01, ...
#
# If the W spectrum encoded L-function zeros, we'd see clustering.
# Probe this by sorting angles and looking for clustering / gaps.

angles_pi = sorted([np.angle(ev) / np.pi for ev in W_eigs])
print(f"\n  Eigenvalue arguments (units of pi), sorted:")
for i in range(0, n, 5):
    chunk = angles_pi[i:i+5]
    print(f"    [{i:>2}-{min(i+4, n-1):>2}]: " + "  ".join(f"{x:+.4f}" for x in chunk))

gaps = [angles_pi[i+1] - angles_pi[i] for i in range(len(angles_pi)-1)]
print(f"\n  Mean angle gap: {np.mean(gaps):.6f} pi")
print(f"  Max angle gap: {max(gaps):.6f} pi (uniform spacing would give {2/n:.6f} pi)")
print(f"  Min angle gap: {min(gaps):.6f} pi")
print(f"  Spacing irregularity (std/mean): {np.std(gaps)/np.mean(gaps):.4f}")


# =========================================================================
# Summary
# =========================================================================

print("\n" + "=" * 78)
print(" Summary")
print("=" * 78)
print(f"""
At N={N}:
  - W is unitary (||W*W - I|| = {err_unit:.2e}).
  - Eigenvalues on unit circle, |moduli| in [{min(moduli):.4e}, {max(moduli):.4f}].
  - tr(W) = {trace_W.real:+.4f} + {trace_W.imag:+.4f}i.

Key questions probed:
  1. Are W eigenvalues N-th roots of unity? (look at root-distance output above)
  2. Does W respect conductor-orbit subspaces? (commutator norms above)
  3. Do Dirichlet characters of (Z/30)* align with W eigenvectors?
  4. Does W * vec(Lambda) decompose cleanly?
  5. Is there an L-function spectrum hidden in W's angles?

Look at the structured output above for the verdict.
""")
