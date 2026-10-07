"""
det W structure derivation.
sign(D_N) = sign(det W_N), W_{ij} = prod_{l=i+1}^{i+j} c_l, c_l = f(p_l), 0<=i,j<=N.
Indices i,j from 0..N. Empty product (j=0) = 1.
"""
from sympy import symbols, Matrix, simplify, factor, prod, Integer, expand

def Wmat(N, c):
    # c is a dict-like or function: c[l] for l>=1
    def entry(i, j):
        p = Integer(1)
        for l in range(i+1, i+j+1):
            p *= c[l]
        return p
    return Matrix(N+1, N+1, entry)

# Symbolic c_1..c_8
cs = symbols('c1:13', positive=True)
c = {l: cs[l-1] for l in range(1, 13)}

for N in range(1, 5):
    W = Wmat(N, c)
    d = factor(W.det())
    print(f"=== det W_{N} ===")
    print("matrix rows:")
    for r in range(N+1):
        print("  ", [W[r,k] for k in range(N+1)])
    print("det W_%d =" % N, d)
    print()
