"""Re-verify the degree-1 factored polynomials symbolically."""
from sympy import symbols, primerange, Matrix, factor, expand, Integer

c = symbols('c')
P = list(primerange(2, 100))

def bn_sym(fc, L):
    b = [Integer(1)]
    a = Integer(1)
    for i in range(1, L):
        a = expand(a * fc.subs('p', P[i-1]))
        b.append(a)
    return b

# monic f(p) = p + c
from sympy import Symbol
p = Symbol('p')
fc = p + c

def D_sym(N):
    b = bn_sym(fc, 2*N+2)
    M = Matrix(N+1, N+1, lambda i, j: b[i+j])
    return factor(M.det())

print("D_1 =", D_sym(1))
print("D_2 =", D_sym(2))
print("D_3 =", D_sym(3))
