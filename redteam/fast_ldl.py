"""Fast leading-PSD verdict via exact LDL (sign of pivots) instead of N separate dets.
A symmetric matrix is PSD iff in LDL^T all diagonal pivots d_i >= 0 (when no
breakdown). Pivots d_i = D_i / D_{i-1}, so sign(pivot_i) = sign(D_i)·sign(D_{i-1}).
Cheaper: one O(n^3) elimination gives all leading-minor info.

We compute pivots by exact Gaussian elimination on the rationals (Hankel is integer)."""
from sympy import primerange, Integer, Rational, Matrix
P = list(primerange(2, 100000))

def bn_pow(r, d, L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (Integer(P[i-1])+r)**d; out.append(a)
    return out

def leading_psd_first_fail(b, Nmax):
    """Return first N (size) at which leading principal minor < 0, using exact
    symmetric elimination. Works directly with the Hankel entries b_{i+j}.
    Returns (N, 'neg') or (N,'breakdown zero pivot') or None if PSD through Nmax."""
    n = Nmax+1
    # build matrix as list of lists (Fraction-exact via sympy Rational)
    A = [[Integer(b[i+j]) for j in range(n)] for i in range(n)]
    # symmetric LDL via outer-product elimination, tracking pivot signs
    for k in range(n):
        piv = A[k][k]
        if piv == 0:
            return (k, 'zero pivot (singular leading block)')
        if piv < 0:
            return (k, 'negative pivot -> D_%d<0' % k)
        for i in range(k+1, n):
            f = Rational(A[i][k], piv)
            for j in range(k, n):
                A[i][j] = A[i][j] - f*A[k][j]
    return None

# Map N*(d) FAST to higher ceiling
Nmax = 30
print(f"Fast LDL leading-PSD, ceiling N={Nmax}")
for r in [0, -1, 1]:
    print(f" r={r}:")
    for d in [2,8,16,32,64,128,256]:
        b = bn_pow(r, d, 2*Nmax+2)
        res = leading_psd_first_fail(b, Nmax)
        if res is None:
            print(f"   d={d:4d}: PSD-leading SURVIVES to N={Nmax} !!!")
        else:
            print(f"   d={d:4d}: first leading fail N={res[0]} ({res[1]})")
