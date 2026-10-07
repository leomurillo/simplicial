"""Map N*(d) carefully for r=0 (f=p^d), d=2..60, to N=22 ceiling.
Question: does N* exceed 22 for some d we can reach? Where is the growth going?"""
from search import bn
from sympy import primerange, Matrix, symbols, expand, Poly, Symbol

P = list(primerange(2, 100000))

def coeffs_power(r, d):
    p = Symbol('p')
    pol = expand((p+r)**d)
    return [int(x) for x in Poly(pol, p).all_coeffs()]

def fpow(r, d):
    # f(p) = (p+r)^d directly (faster than expanding to coeffs)
    from sympy import Integer
    def f(p):
        return (Integer(p)+r)**d
    return f

def first_leading_neg(f, Nmax):
    b = bn(f, 2*Nmax+2)
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        det = M.det()
        if det < 0:
            return N
    return None  # survived to Nmax

Nmax = 22
print(f"r=0, f=p^d, ceiling N={Nmax}")
res = {}
for d in [2,4,6,8,10,12,14,16,18,20,24,28,32,40,48,56]:
    f = fpow(0, d)
    N = first_leading_neg(f, Nmax)
    res[d] = N
    print(f"  d={d:3d}: N*={N}")
