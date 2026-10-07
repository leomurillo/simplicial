"""
probe_archimedean_schur.py — the archimedean Schur/innovation chain of QW_lambda.

C12 (apex_zeros) established the template in the SOLVABLE place: the function-field
Weil form is a Toeplitz matrix, its Levinson reflection coefficients k_m are the
Gohberg-Krein/Schur params, and |k_m|<=1 (a strict contraction) <=> Weil purity.
Frobenius hands that contraction over for free; Q must manufacture it = (H0').

Here we run the chain on the ACTUAL CCM semilocal Weil matrix (even sector, center-out
ordered — exactly P infinity-F section 19's ordering). For a symmetric PD matrix the
center-out Cholesky gives:
  * pivots d_m = L[m,m]^2  = the innovation / conditional variance of mode m given its
    past (section 19's d(s) for the finite matrix);
  * contraction coefficients k_m = sqrt(1 - d_m / Ev[m,m]) in [0,1) = the multiple-
    correlation of mode m with modes 0..m-1 (the Schur/reflection coefficient, section 23's
    "contraction frame"); |k_m| < 1 for all m  <=>  all pivots > 0  <=>  PSD  <=>  (H0')
    AT THIS WINDOW.

The point of the measurement (what C12 tells us to look for): in the function field the
chain SATURATES (|k|=1 exactly at rank 2g, innovation hits 0 — determinism reached). The
archimedean chain has INFINITE rank, so it must stay a STRICT contraction (|k_m|<1) at
every window while the EDGE coefficient creeps toward 1 as lambda grows (determinism
approached from inside the disk, never reached). We measure that creep — the archimedean
"approach to the boundary" — and check it stays sub-unit (per-window (H0'), Prop F.6).

mpmath, dps 40, deterministic, local. No torch.
"""

import mpmath as mp

mp.mp.dps = 40


def primes_upto(x):
    out, n = [], 2
    while n <= x:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_Ev(lam, N):
    """Even-sector CCM matrix Ev (center-out: index 0 = V_0, index k = |k|-mode)."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pj = []
    for p in primes_upto(float(mp.exp(L)) + 1e-12):
        j = 1
        while j * mp.log(p) <= L + mp.mpf("1e-30"):
            pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
            j += 1
    pts = mp.linspace(0, L, 16)
    S = {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj)
        S[k] = A - B - P
    cgamma = mp.euler
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + cgamma) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = mp.matrix(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = D[abs(n)] if n == m else (S[m] - S[n]) / (mp.pi * (n - m))
    Ev = mp.matrix(N + 1, N + 1)
    for k in range(N + 1):
        for l in range(N + 1):
            a, b = QW[N + k, N + l], QW[N + k, N - l]
            if k == 0 and l == 0:
                Ev[k, l] = a
            elif k == 0 or l == 0:
                Ev[k, l] = mp.sqrt(2) * a
            else:
                Ev[k, l] = a + b
    return Ev


def ldl_pivots(A):
    """Center-out symmetric LDL^T: returns pivots d_0..d_n (conditional variances).
    Works whether or not A is PD (negative pivot signals an indefinite leading block)."""
    n = A.rows
    M = mp.matrix(A.tolist())
    d = []
    Lmat = mp.eye(n)
    for j in range(n):
        s = M[j, j] - mp.fsum(Lmat[j, k] ** 2 * d[k] for k in range(j))
        d.append(s)
        for i in range(j + 1, n):
            if s == 0:
                Lmat[i, j] = 0
            else:
                Lmat[i, j] = (M[i, j] - mp.fsum(Lmat[i, k] * Lmat[j, k] * d[k] for k in range(j))) / s
    return d


def report(lam, N):
    Ev = build_Ev(lam, N)
    diag = [Ev[m, m] for m in range(N + 1)]
    d = ldl_pivots(Ev)                                   # innovations / conditional variances
    # contraction coefficients k_m = sqrt(1 - d_m/diag_m) in [0,1) when PD
    kk = []
    for m in range(N + 1):
        r = 1 - d[m] / diag[m] if diag[m] != 0 else mp.mpf(1)
        kk.append(mp.sqrt(r) if r >= 0 else -mp.sqrt(-r))   # imaginary->report as negative magnitude
    all_pivots_pos = all(x > 0 for x in d)
    max_k = max(abs(x) for x in kk)
    min_piv = min(d)
    # smallest eigenvalue (the ground epsilon_lambda) for context
    eps = min(mp.mpf(str(e)) for e in mp.eigsy(Ev, eigvals_only=True))
    contraction = all_pivots_pos and max_k < 1
    print(f"  lambda={float(lam):.2f}  N={N}:  PD/(H0')-this-window={all_pivots_pos}  "
          f"strict-contraction(all |k_m|<1)={max_k < 1}")
    print(f"     pivots d_m (innovations): {[mp.nstr(x,3) for x in d]}")
    print(f"     contraction k_m:          {[mp.nstr(x,3) for x in kk]}")
    print(f"     min pivot={mp.nstr(min_piv,3)}  max|k_m|={mp.nstr(max_k,6)} (edge/seam)  "
          f"eps_lambda={mp.nstr(eps,3)}")
    return contraction, float(max_k), float(min_piv)


def main():
    print("=" * 82)
    print("Archimedean Schur/innovation chain of QW_lambda (even sector, center-out)")
    print("  d_m>0 (innovations) & |k_m|<1 (contraction)  <=>  PSD  <=>  (H0') at this window")
    print("=" * 82)
    rows = []
    for lam, N in [(mp.mpf("1.3"), 10), (mp.mpf("1.5"), 10), (mp.mpf("2.0"), 12), (mp.mpf("2.2"), 12)]:
        c, mk, mp_ = report(lam, N)
        rows.append((float(lam), c, mk))
    print("-" * 82)
    print("  edge-contraction creep (max|k_m| vs lambda — approach to the disk boundary):")
    for lam, c, mk in rows:
        print(f"     lambda={lam:.2f}: max|k_m|={mk:.6f}  {'(<1, strict)' if mk < 1 else '(>=1 !!)'}")
    ok = all(c for c, in [(r[1],) for r in rows])
    print("  ALL windows strict contraction (per-window (H0'), Prop F.6):", ok)
    print("  [C12 template: function field SATURATES |k|=1 at rank 2g; archimedean must stay")
    print("   |k_m|<1 at every window with the edge creeping toward 1 as lambda grows.]")
    print("RESULT:", "GREEN" if ok else "RED")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
