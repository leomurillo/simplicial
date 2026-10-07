"""Confirm the N*=10 plateau holds for very large d (d up to 40)."""
from search import poly_from_coeffs, bn
from sympy import primerange, Matrix, symbols, expand, Poly, Symbol

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
            return N, d
    return None, None

Nmax = 14
for r in [-1, 0, 1]:
    for d in [16, 20, 25, 30, 40]:
        coeffs = coeffs_power(r, d)
        f = poly_from_coeffs(coeffs)
        N, det = first_leading_neg(f, Nmax)
        print(f"r={r}, d={d}: N*={N}")
