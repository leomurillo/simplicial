"""
N=210 v6 high-precision rerun at mpmath dps=600.

The v6 run at dps=300 hit a precision floor at n=60: gamma_min=0.141 gave
dynamic range ~10^200 in the Hankel entries, exceeding dps=300's effective
precision floor of ~10^{-100}. At dps=600 the effective floor is ~10^{-300},
plenty of margin for n=60.

Pre-sets mp.dps=600 BEFORE importing zero_data_N210, so all mpf objects are
constructed from the 25-30 digit source strings at dps=600.
"""

import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, matrix
mp.dps = 600

# Import zero data (mpf objects auto-quantize to the current mp.dps)
from zero_data_N210 import self_dual_all as sd, non_self_dual_all as nsd

print(f"Loaded {len(sd)} self-dual + {len(nsd)} non-self-dual pairs = "
      f"{len(sd) + 2*len(nsd)} L-functions at dps={mp.dps}.")

M_MAX = 130

def jc(m):
    total = mpf(0)
    for zs in sd.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    for zs in nsd.values():
        total += 2 * sum(z ** (-2 * m) for z in zs)
    return total

print()
print("=" * 78)
print(f" v6 high-precision verification at mpmath dps={mp.dps}")
print("=" * 78)
print()

t0 = time.time()
ell = [None] + [jc(m) for m in range(1, M_MAX + 1)]
print(f"Cumulants in {time.time()-t0:.1f}s")
print(f"  ell_1   = {mp.nstr(ell[1], 8)}")
print(f"  ell_60  = {mp.nstr(ell[60], 6)}")
print(f"  ell_120 = {mp.nstr(ell[120], 6)}")

def ldl(M):
    n = M.rows
    A = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A[k, k]; diags.append(d)
        if d <= 0:
            return False, min(diags), k
        for i in range(k+1, n):
            f = A[i, k] / d
            for j in range(k+1, n):
                A[i, j] -= f * A[k, j]
    return True, min(diags), n

def H(n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = ell[i+j+1]
    return M

def J(n):
    M = matrix(n+1, n+1)
    for i in range(n+1):
        for j in range(n+1):
            M[i, j] = ell[i+j+2]
    return M

print()
print(f"  {'n':>3} {'H_n':>8} {'min D(H)':>22} {'J_n':>8} {'min D(J)':>22}")
print("  " + "-" * 68)

n_to_test = [40, 45, 50, 55, 58, 60, 62, 64]
t0 = time.time()
passed = 0
for n in n_to_test:
    h_psd, h_min, _ = ldl(H(n))
    j_psd, j_min, _ = ldl(J(n))
    print(f"  {n:>3} {'PSD' if h_psd else 'FAIL':>8} {mp.nstr(h_min, 5):>22} "
          f"{'PSD' if j_psd else 'FAIL':>8} {mp.nstr(j_min, 5):>22}")
    if h_psd and j_psd:
        passed += 1

print()
print(f"Verified: {passed}/{len(n_to_test)} sampled high rungs PSD at dps={mp.dps}")
print(f"Wall time: {time.time()-t0:.1f}s")
