"""DEEP investigation of high-degree power candidates that survived to N=14.
Push leading minors to N=22 AND check full PSD. These are the prime suspects."""
from search import poly_from_coeffs, bn, full_psd_failure
from sympy import primerange, Matrix, symbols, expand, Poly, Symbol

P = list(primerange(2, 100000))

def coeffs_power(r, d):
    p = Symbol('p')
    pol = expand((p+r)**d)
    return [int(x) for x in Poly(pol, p).all_coeffs()]

def leading_signs(f, Nmax):
    b = bn(f, 2*Nmax+2)
    signs = []
    firstneg = None
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        d = M.det()
        signs.append('+' if d>0 else ('0' if d==0 else '-'))
        if d < 0 and firstneg is None:
            firstneg = N
    return signs, firstneg

for (r,d) in [(-1,16),(0,20),(1,20),(-1,20),(0,30),(-1,40)]:
    coeffs = coeffs_power(r,d)
    f = poly_from_coeffs(coeffs)
    signs, fn = leading_signs(f, 22)
    print(f"(p+{r})^{d}: leading D_0..D_22 signs:")
    print("   ", ''.join(signs))
    print(f"   first leading neg N = {fn}")
