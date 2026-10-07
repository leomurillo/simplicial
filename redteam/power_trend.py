"""Does N*((p+r)^d) grow with d? Map the trend for r in {-1,0,1,2} and d=2..14.
This is the most promising counterexample direction."""
from search import poly_from_coeffs, valid_on_primes, bn
from sympy import primerange, Matrix, Integer, symbols, expand, Poly, Symbol

P = list(primerange(2, 100000))

def coeffs_power(r, d):
    p = Symbol('p')
    pol = expand((p+r)**d)
    return [int(x) for x in Poly(pol, p).all_coeffs()]

def first_leading_neg(f, Nmax):
    b = bn(f, 2*Nmax+2)
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        d = M.det()
        if d < 0:
            return N
    return None

Nmax = 20
for r in [-1, 0, 1, 2, 3]:
    row = []
    for d in range(2, 15):
        coeffs = coeffs_power(r, d)
        f = poly_from_coeffs(coeffs)
        N = first_leading_neg(f, Nmax)
        row.append(N if N is not None else f">{Nmax}")
    print(f"r={r:2d}: N* for d=2..14: {row}")
