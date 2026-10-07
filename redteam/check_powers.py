"""URGENT: the (p+r)^d candidates 'survived' leading-minor check to N=7.
Check them HARD: full PSD + leading minors to N=22."""
from search import poly_from_coeffs, valid_on_primes, bn, full_psd_failure, first_leading_failure
from sympy import primerange, Matrix, Integer, symbols, expand, Poly, Symbol
import itertools

P = list(primerange(2, 100000))

def coeffs_power(r, d):
    p = Symbol('p')
    pol = expand((p+r)**d)
    return [int(x) for x in Poly(pol, p).all_coeffs()]

def leading_dets(f, Nmax):
    b = bn(f, 2*Nmax+2)
    out = []
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        out.append(M.det())
    return out

cases = [("(p-1)^5", coeffs_power(-1,5)),
         ("(p-1)^6", coeffs_power(-1,6)),
         ("p^6",     coeffs_power(0,6)),
         ("(p+1)^6", coeffs_power(1,6)),
         ("(p-1)^2", coeffs_power(-1,2)),
         ("p^2",     coeffs_power(0,2)),
         ("(p+1)^2", coeffs_power(1,2)),
         ("(p-1)^3", coeffs_power(-1,3)),
         ("(p-1)^4", coeffs_power(-1,4))]

for name, coeffs in cases:
    f = poly_from_coeffs(coeffs)
    valid = valid_on_primes(coeffs)
    dets = leading_dets(f, 12)
    neg = [(N,d) for N,d in enumerate(dets) if d < 0]
    print(f"{name}: valid_on_primes={valid}")
    print(f"   leading dets D_0..D_12 signs: {['+' if d>0 else ('0' if d==0 else '-') for d in dets]}")
    if neg:
        print(f"   FIRST LEADING NEG at N={neg[0][0]}: {neg[0][1]}")
    else:
        print(f"   NO leading negative through N=12 -- run FULL PSD")
        fp = full_psd_failure(f, 8)
        print(f"   full PSD (size 8) first neg minor: {fp}")
