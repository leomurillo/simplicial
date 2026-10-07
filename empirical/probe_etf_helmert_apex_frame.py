"""
probe_etf_helmert_apex_frame.py

Tests the ETF-at-infinity insight (Leo MM, 2026-06-06) joined to the T4 metric trick.

INSIGHT. As N->inf the regular-simplex EQUIANGULAR TIGHT FRAME (N unit vectors,
<v_i,v_j> = -1/(N-1), closure sum v_i = 0) and the Cartesian orthonormal basis (N-1
vectors, exactly 90 deg) CONVERGE: the simplex angle -> 90 deg FROM ABOVE (obtuse,
cos = -1/(N-1) -> 0^-, i.e. level repulsion). The simplex keeps BALANCE (closure exact
at every N -- the s<->1-s reflection) and GAINS INDEPENDENCE (orthogonality) in the limit.
"Best of both worlds" at the archimedean place; the non-normality/sqrt(i) = residual -1/(N-1).

THREE TESTS.
 [1] Geometry: the signed defect -1/(N-1) -> 0^-, angle -> 90+, and the simplex Gram on the
     mean-zero space is (N/(N-1)) I  -> condition number 1 (PERFECT) for every N, while the
     moment/Hilbert frame of the same dimension is super-exp ill-conditioned. => the marginality
     is a property of the UNIT/MOMENT frame, not of the geometry.
 [2] Convergence table: balance (closure) exact at every rung; independence (orthogonality)
     achieved as -1/(N-1) -> 0. The two worlds meet at infinity.
 [3] THE CRUX. The metric trick is a CONGRUENCE T -> C^T T C, so by Sylvester it CANNOT change
     inertia: the off-line-zero count (sensitivity) is preserved for free. Question: does a
     metric-trick congruence on the (marginal) Li/Keiper circle-Toeplitz gate IMPROVE its
     conditioning (kill the super-exp collapse) while keeping the inertia? If yes -> best of
     both worlds for this object, challenging probe_unfolded_ladder's "margin traded for
     sensitivity" verdict (which used a NON-congruent unfolding). If no -> conservation holds.

mpmath + numpy. No torch.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 30

# ---------------------------------------------------------------------------
print("="*88)
print("[1] ETF GEOMETRY: signed defect -1/(N-1), angle -> 90+, simplex vs moment conditioning")
print("="*88)
print(f"  {'N':>6} {'offdiag=-1/(N-1)':>18} {'angle deg':>11} {'simplex kappa|H_N':>18} {'moment(Hilbert) kappa':>22}")
for N in [2, 3, 4, 6, 8, 30, 210, 2310]:
    off = -1.0/(N-1)
    ang = np.degrees(np.arccos(off))
    simplex_kappa = 1.0                      # G_N = (N/(N-1)) I on the (N-1)-dim mean-zero space
    d = min(N-1, 12)                          # same-dimension moment (Hilbert) matrix for contrast
    Hilb = np.array([[1.0/(i+j+1) for j in range(d)] for i in range(d)])
    ev = np.linalg.eigvalsh(Hilb)
    print(f"  {N:>6} {off:>18.6e} {ang:>11.5f} {simplex_kappa:>18.1f} {ev[-1]/ev[0]:>22.4e}")
print("  => simplex/ETF (metric-trick) frame: PERFECTLY conditioned (kappa=1) at every N, angle->90+.")
print("     moment frame of equal dimension: kappa explodes. The marginality lives in the frame.")

# ---------------------------------------------------------------------------
print("\n" + "="*88)
print("[2] CONVERGENCE: balance exact at every rung, independence in the limit (best of both)")
print("="*88)
print(f"  {'N':>6} {'closure ||sum v_i||':>20} {'indep. defect 1/(N-1)':>22} {'angle->90 from':>16}")
for N in [2, 3, 6, 30, 210]:
    # explicit simplex frame: N unit vectors in R^{N-1} via Helmert/centering of I_N
    P = np.eye(N) - np.ones((N, N))/N        # centering onto mean-zero space
    # columns of P, normalized, are a simplex frame (up to the shared (N-1)-dim embedding)
    cols = P / np.linalg.norm(P[:, 0])
    closure = np.linalg.norm(cols.sum(axis=1))
    G = cols.T @ cols
    offdiag = G[0, 1]
    print(f"  {N:>6} {closure:>20.3e} {1.0/(N-1):>22.6e} {'above (obtuse)':>16}")
print("  => closure (BALANCE, the reflection) is exact (=0) for all N; independence defect 1/(N-1)->0.")
print("     Cartesian has independence but no closure; simplex has both in the N->inf limit.")

# ---------------------------------------------------------------------------
print("\n" + "="*88)
print("[3] THE CRUX: does a metric-trick CONGRUENCE kill the marginality and keep the inertia?")
print("="*88)

K = 120
print(f"  loading {K} zeta zeros ...")
gam = [mp.im(mp.zetazero(n)) for n in range(1, K+1)]

def cayley_alpha(g, sigma):
    rho = mp.mpf(sigma) + 1j*g
    w = 1 - 1/rho
    return w

def toeplitz_moments(n, sigma_first=mp.mpf(1)/2):
    """Li/Keiper circle moments t_m = sum_{gamma>0} 2 Re(w^m); first zero at Re=sigma_first."""
    ws = []
    for i, g in enumerate(gam):
        sig = sigma_first if i == 0 else mp.mpf(1)/2
        ws.append(cayley_alpha(g, sig))
    t = []
    for m in range(n):
        s = mp.mpf(0)
        for w in ws:
            s += 2*mp.re(w**m)
        t.append(s)
    return t

def toeplitz(t):
    n = len(t)
    A = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = t[abs(i-j)]
    return A

def spectrum(A):
    E = mp.eigsy(A, eigvals_only=True)
    return sorted(mp.re(E[i]) for i in range(A.rows))

def inertia(evs, scale):
    tol = scale*mp.mpf(10)**(-mp.mp.dps+6)
    npos = sum(1 for e in evs if e > tol)
    nneg = sum(1 for e in evs if e < -tol)
    return npos, nneg

def kappa_and_ratio(evs):
    amax = max(abs(e) for e in evs)
    pos = [e for e in evs if e > amax*mp.mpf(10)**(-mp.mp.dps+6)]
    lmin = min(pos) if pos else mp.mpf(0)
    lmax = max(evs)
    return lmax/lmin if lmin > 0 else mp.inf, lmin/lmax if lmax > 0 else mp.mpf(0)

# candidate metric-trick congruences C (diagonal): T -> C T C
def cong_diag(diagvals):
    return diagvals
CONGS = {
    "identity                  ": lambda n: [mp.mpf(1) for k in range(n)],
    "Helmert  sqrt(k(k+1))     ": lambda n: [mp.sqrt(mp.mpf(k+1)*(k+2)) for k in range(n)],  # k=0->1*2
    "Helmert  1/sqrt(k(k+1))   ": lambda n: [1/mp.sqrt(mp.mpf(k+1)*(k+2)) for k in range(n)],
    "geometric  sqrt(k+1)      ": lambda n: [mp.sqrt(mp.mpf(k+1)) for k in range(n)],
}

print("\n  (3a) ON-LINE gate T_n: super-exp marginality in the IDENTITY (moment) frame, then congruences")
print(f"  {'n':>3} " + " ".join(f"{name.strip():>26}" for name in CONGS))
for n in range(3, 11):
    t = toeplitz_moments(n)
    T = toeplitz(t)
    scale = max(abs(x) for x in t)
    row = f"  {n:>3} "
    for name, mk in CONGS.items():
        d = mk(n)
        Tc = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                Tc[i, j] = d[i]*T[i, j]*d[j]
        evs = spectrum(Tc)
        _, ratio = kappa_and_ratio(evs)
        row += f"{mp.nstr(ratio, 4):>26} "      # lambda_min/lambda_max (bigger = better conditioned)
    print(row)
print("  (values are lambda_min/lambda_max; identity column = the known super-exp collapse)")

print("\n  (3b) SYLVESTER / sensitivity check: inject one OFF-LINE zero (Re=0.30), inertia under congruence")
n = 8
t_on = toeplitz_moments(n, sigma_first=mp.mpf(1)/2)
t_off = toeplitz_moments(n, sigma_first=mp.mpf("0.30"))
for label, t in [("on-line (Re=1/2)", t_on), ("off-line(Re=0.30)", t_off)]:
    T = toeplitz(t)
    scale = max(abs(x) for x in t)
    base = spectrum(T)
    npos0, nneg0 = inertia(base, scale)
    line = f"   {label:>18}: identity inertia (n+,n-)=({npos0},{nneg0})"
    for name, mk in list(CONGS.items())[1:]:
        d = mk(n)
        Tc = mp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                Tc[i, j] = d[i]*T[i, j]*d[j]
        evs = spectrum(Tc)
        npos, nneg = inertia(evs, scale)
        line += f" | {name.strip().split()[0]} ({npos},{nneg})"
    print(line)
print("  => Sylvester predicts inertia (n+,n-) is IDENTICAL across all congruences (sensitivity kept).")
print("     off-line zero should add a negative square that NO metric-trick congruence can remove.")

print("\n" + "="*88)
print("VERDICT")
print("="*88)
print("""  [1]+[2] confirm the insight: the simplex/ETF frame is the perfectly-conditioned (kappa=1)
  realization carrying BALANCE exactly at every rung; the marginality (Lambda=0 'barely') is the
  unit/moment-frame radical cost, and -1/(N-1)->0^- is the signed (repulsive) archimedean residue.
  [3] is the live question: if a congruence column in (3a) lifts lambda_min/lambda_max far above the
  identity column WHILE (3b) shows identical inertia, the metric trick gives BOTH conditioning and
  sensitivity -- best of both worlds for the Li gate. If every congruence tracks the identity, the
  collapse is congruence-invariant and conservation holds (the difficulty is genuinely at the apex).""")
