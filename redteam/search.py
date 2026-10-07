"""Aggressive counterexample search. Find monic f, f(p)>0, whose b_n is a
Hamburger moment sequence (all principal minors of Hankel >=0 up to large N)."""
from sympy import primerange, Matrix, Integer, Rational
import itertools, sys

P = list(primerange(2, 100000))

def bn(fvals_or_f, L, is_f=True):
    b = [Integer(1)]
    a = Integer(1)
    if is_f:
        for i in range(1, L):
            a = a * fvals_or_f(P[i-1])
            b.append(a)
    else:
        for i in range(1, L):
            a = a * fvals_or_f[i-1]
            b.append(a)
    return b

def first_leading_failure(f, Nmax):
    """First N with leading Hankel det < 0. Fast path using only leading minors."""
    b = bn(f, 2*Nmax+2)
    for N in range(0, Nmax+1):
        M = Matrix(N+1, N+1, lambda i, j: b[i+j])
        d = M.det()
        if d < 0:
            return N, d
    return None, None

def full_psd_failure(f, size):
    """First negative principal minor (ANY subset) of (size+1)x(size+1) Hankel."""
    b = bn(f, 2*size+2)
    H = Matrix(size+1, size+1, lambda i, j: b[i+j])
    idx = list(range(size+1))
    for k in range(1, size+2):
        for sub in itertools.combinations(idx, k):
            sub = list(sub)
            d = H[sub, sub].det()
            if d < 0:
                return (tuple(sub), d)
    return None

def valid_on_primes(coeffs, npr=200):
    """Check f(p)>0 on first npr primes. coeffs high->low, monic assumed."""
    for p in P[:npr]:
        v = 0
        for c in coeffs:
            v = v*p + c
        if v <= 0:
            return False
    return True

def poly_from_coeffs(coeffs):
    def f(p):
        v = Integer(0)
        for c in coeffs:
            v = v*p + c
        return v
    return f

def scan(candidates, Nmax=8, label=""):
    """candidates: list of (name, coeffs). Report N* via leading minors."""
    results = []
    for name, coeffs in candidates:
        if not valid_on_primes(coeffs):
            continue
        f = poly_from_coeffs(coeffs)
        N, d = first_leading_failure(f, Nmax)
        if N is None:
            results.append((name, coeffs, None, None))  # survivor so far!
        else:
            results.append((name, coeffs, N, d))
    # sort: survivors first, then largest N*
    results.sort(key=lambda r: (r[2] is not None, r[2] if r[2] is not None else 1e9))
    return results
