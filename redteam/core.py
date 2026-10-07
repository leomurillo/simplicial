"""Core exact-arithmetic machinery for the Hamburger-moment red-team."""
from sympy import primerange, Matrix, Integer, Rational, symbols, factor, simplify
import itertools

# Primes 2,3,5,7,...
P = list(primerange(2, 100000))   # plenty

def bn(f, L):
    """b_0..b_{L-1}: b_0=1, b_n = prod_{i=1}^n f(p_i)."""
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a = a * f(P[i-1])
        b.append(a)
    return b

def hankel(f, N):
    """Hankel matrix (b_{i+j})_{0<=i,j<=N}, size (N+1)x(N+1)."""
    b = bn(f, 2*N+2)
    return Matrix(N+1, N+1, lambda i, j: b[i+j])

def D(f, N):
    """Leading Hankel determinant D_N."""
    return hankel(f, N).det()

def first_leading_failure(f, Nmax):
    """First N where leading Hankel det D_N < 0, else None."""
    b = bn(f, 2*Nmax+2)
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        d = M.det()
        if d < 0:
            return N, d
    return None, None

def all_principal_minors_psd(f, size):
    """Check ALL principal minors of the (size+1)x(size+1) Hankel matrix >=0.
    Returns (ok, witness) where witness is (index_subset, det) of first negative.
    This is the FULL PSD test (necessary AND sufficient for the finite block)."""
    b = bn(f, 2*size+2)
    H = Matrix(size+1, size+1, lambda i, j: b[i+j])
    idx = list(range(size+1))
    for k in range(1, size+2):
        for sub in itertools.combinations(idx, k):
            sub = list(sub)
            sm = H[sub, sub]
            d = sm.det()
            if d < 0:
                return False, (tuple(sub), d)
    return True, None

if __name__ == "__main__":
    # Re-verify load-bearing facts
    print("D(p, 3) =", D(lambda p: p, 3), " (expect -787680)")
    print("D(p, 1) =", D(lambda p: p, 1))
    print("D(p, 2) =", D(lambda p: p, 2))
