"""
Symbolic D_2(B,C), D_3(B,C) for monic quadratic f(p)=p^2 + B*p + C.
Also det W_2, det W_3 (the sign-equivalent reduced determinants).
"""
from sympy import primerange, Matrix, Integer, symbols, factor, simplify, expand, Poly
import sympy as sp

P = list(primerange(2, 1000))
B, C = symbols('B C', real=True)

def f(p):
    return p*p + B*p + C   # monic quadratic, symbolic

def bn(L):
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1])
        b.append(a)
    return b

def Ddet(N):
    b = bn(2*N+2)
    M = Matrix(N+1, N+1, lambda i, j: b[i+j])
    return M.det()

# det W_N : factor b_i out of row i. W_N[i][j] = prod_{l=i+1}^{i+j} c_l, c_l=f(p_l) (1-indexed primes).
# c_l = f(P[l-1]).
def c(l):
    return f(P[l-1])

def Wdet(N):
    def entry(i, j):
        # prod_{l=i+1}^{i+j} c_l ; empty product (j=0) = 1
        prod = Integer(1)
        for l in range(i+1, i+j+1):
            prod *= c(l)
        return prod
    M = Matrix(N+1, N+1, entry)
    return M.det()

print("=== D_1 ===")
D1 = factor(Ddet(1))
print("D_1 =", D1)

print("\n=== det W_1 ===")
print("W_1 =", factor(Wdet(1)))

print("\n=== D_2 (full Hankel det) factored ===")
D2 = factor(Ddet(2))
print("D_2 =", D2)

print("\n=== det W_2 factored ===")
W2 = factor(Wdet(2))
print("det W_2 =", W2)
print("   expand:", expand(Wdet(2)))
