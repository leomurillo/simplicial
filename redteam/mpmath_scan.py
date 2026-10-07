"""High-precision float scan to map the moment boundary far beyond exact reach.
Use log-scaling: work with L_n = log b_n to avoid overflow, build Hankel in a
SCALED way. For PSD detection we can rescale rows/cols by positive diagonals
(D-congruence preserves PSD): H' = diag(1/sqrt(b_{2i})) H diag(1/sqrt(b_{2j})),
entries H'_{ij} = b_{i+j}/sqrt(b_{2i} b_{2j}) = exp(L_{i+j} - (L_{2i}+L_{2j})/2).
This is bounded in [0,1]-ish and PSD-equivalent. Check min eigenvalue sign.
NOTE: float is for MAPPING; any survivor gets exact confirmation."""
import mpmath as mp
mp.mp.dps = 80
from sympy import primerange
P = list(primerange(2, 100000))
logP = {}

def Ln(r, d, n):
    """L_n = log b_n = d * sum_{i=1}^n log(p_i + r)."""
    s = mp.mpf(0)
    for i in range(1, n+1):
        s += mp.log(mp.mpf(P[i-1]) + r)
    return d*s

def scaled_hankel_min_eig(r, d, N):
    # precompute L_0..L_{2N}
    L = [mp.mpf(0)]*(2*N+1)
    acc = mp.mpf(0)
    for m in range(1, 2*N+1):
        acc += mp.log(mp.mpf(P[m-1]) + r)
        L[m] = d*acc
    # scaled entry
    M = mp.matrix(N+1, N+1)
    for i in range(N+1):
        for j in range(N+1):
            M[i,j] = mp.e**(L[i+j] - (L[2*i]+L[2*j])/2)
    E = mp.eigsy(M, eigvals_only=True)
    return min(E)

# Map: for each d, find first N where min-eig < 0 (tolerance for fp noise)
def first_psd_fail(r, d, Nmax, tol=mp.mpf(10)**(-50)):
    for N in range(1, Nmax+1):
        me = scaled_hankel_min_eig(r, d, N)
        if me < -tol:
            return N, me
    return None, None

Nmax = 40
print(f"mpmath dps={mp.mp.dps}, scaled-Hankel min-eig, ceiling N={Nmax}")
for r in [0]:
    for d in [16, 32, 64, 128, 256, 512, 1024, 4096]:
        N, me = first_psd_fail(r, d, Nmax)
        if N is None:
            print(f"  r={r} d={d:5d}: NO PSD fail through N={Nmax}  <-- candidate survivor")
        else:
            print(f"  r={r} d={d:5d}: first PSD fail N={N}  (min eig ~ {mp.nstr(me,3)})")
