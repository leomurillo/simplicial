"""
T8.4 Lemma 6.4 — variant matrix forms.

The team's probe at probe_T8p4_lemma_6p4_Q_matrix.py confirms that
  Q_re[i,j] = R_{i+j+1} * Re(<h_{i+j+1}, chi_1>)
FAILS PSD at every n >= 1 (sign flip in axis sequence around k ~ 0.7*N).

This script tests the variants implied by the proof sketch in §6.4
("R_k <h_k, chi_1> = R_k^2 |C_{k,1}|^2 (sign)"):
  V1: |Q_re|[i,j] = R_{i+j+1} * |Re(<h_{i+j+1}, chi_1>)|  (abs of axis)
  V2: Q_abs[i,j] = R_{i+j+1} * |<h_{i+j+1}, chi_1>|       (modulus of axis)
  V3: Q_sq[i,j]  = (R_{i+j+1} * |<h_{i+j+1}, chi_1>|)^2  (squared modulus)
  V4: outer-product form (rank-1): v_k v_k^T with v_k = R_k <h_k,chi_1>
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from mpmath import mp, mpf, mpc, sqrt, exp, pi, matrix, re

mp.dps = 80

def R(k, N):
    return mpf(1) / sqrt(mpf(N) * mpf(k) * mpf(k + 1))

def hk_chi1(k, N):
    omega = exp(mpc(0, 1) * 2 * pi / mpf(N))
    s_sum = mpc(0, 0)
    w = mpc(1, 0)
    for _ in range(k):
        w = w * omega
        s_sum += w
    last = w * omega
    return s_sum - mpf(k) * last

def axis_value(k, N, form):
    """Compute axis_k for the chosen variant form."""
    val = hk_chi1(k, N)
    rk = R(k, N)
    if form == 'V1':  # abs of real part
        return rk * abs(re(val))
    if form == 'V2':  # modulus
        return rk * abs(val)
    if form == 'V3':  # squared modulus
        return (rk * abs(val)) ** 2
    raise ValueError(form)

def hankel_from_axis(axis, n):
    """Hankel matrix from axis sequence: M[i,j] = axis[i+j+1] (shifted index)."""
    M = matrix(n + 1, n + 1)
    for i in range(n + 1):
        for j in range(n + 1):
            M[i, j] = axis[i + j]
    return M

def ldl(M):
    n = M.rows
    A = matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = M[i, j]
    diags = []
    for k in range(n):
        d = A[k, k]
        diags.append(d)
        if d <= 0:
            return False, min(diags), k
        for i in range(k+1, n):
            f = A[i, k] / d
            for j in range(k+1, n):
                A[i, j] -= f * A[k, j]
    return True, min(diags), n

def run_test(N, n_max, form_label, form_code):
    axis = [axis_value(k, N, form_code) for k in range(1, 2 * n_max + 2)]
    print(f"  {form_label} at N={N}:")
    print(f"    axis (k=1..{min(10, 2*n_max+1)}): " +
          ", ".join(mp.nstr(axis[i], 4) for i in range(min(10, 2*n_max+1))))
    print(f"    {'n':>3}  {'PSD':>5}  {'min D':>16}")
    passed = 0
    for n in [0, 1, 2, 3, 5, 8, 10, 14]:
        if 2 * n >= len(axis): break
        M = hankel_from_axis(axis, n)
        psd, min_d, _ = ldl(M)
        s = "PSD" if psd else "FAIL"
        if psd: passed += 1
        print(f"    {n:>3}  {s:>5}  {mp.nstr(min_d, 4):>16}")
    print(f"    -> {passed} PSD rungs")
    print()

print("=" * 78)
print(" T8.4 Lemma 6.4 — variant matrix forms (PSD test)")
print("=" * 78)
print()

for N in [30, 210]:
    print(f"--- N = {N} ---")
    print()
    run_test(N, 14, "V1: R_k * |Re<h_k,chi_1>|", 'V1')
    run_test(N, 14, "V2: R_k * |<h_k,chi_1>|", 'V2')
    run_test(N, 14, "V3: (R_k * |<h_k,chi_1>|)^2", 'V3')

print("=" * 78)
print(" Diagnostic")
print("=" * 78)
print("""
Summary of axis sign structure at N=30:
  Re(R_k <h_k,chi_1>) is positive for k = 1..20, then NEGATIVE for k = 21..29.
  The sign flip at k ~ 0.7N kills Stieltjes positivity of the team's stated Q.

If any variant (V1, V2, V3) passes PSD universally at both N=30 and N=210,
the Lemma 6.4 statement should be reformulated to use that variant.

V3 (squared modulus): trivially PSD as a rank-1-like outer-product structure
since (R_k |<h_k,chi_1>|)^2 = (R_k |<h_k,chi_1>|) * (R_k |<h_k,chi_1>|).

If V1 and V2 both fail PSD: Lemma 6.4 cannot be salvaged by sign/modulus
adjustment; the proof needs structurally different machinery.
""")
