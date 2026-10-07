"""
Symbolic form of principal minors in terms of ratios c_l = f(p_l).
b_n = prod_{l=1}^n c_l, b_0=1.
"""
from sympy import symbols, Matrix, factor, simplify, prod, Integer, expand

# Use enough symbolic ratios
NC = 14
c = symbols('c1:%d' % (NC+1), positive=True)  # c[0]=c1,...,c[NC-1]=c_NC
def b(n):
    if n == 0:
        return Integer(1)
    return prod(c[0:n])

def minor_sym(S):
    n = len(S)
    return Matrix(n, n, lambda a, d: b(S[a]+S[d])).det()

print("=== 3x3 consecutive minors {r,r+1,r+2} ===")
for r in range(0, 4):
    S = (r, r+1, r+2)
    M = factor(minor_sym(S))
    print(f"\nS={S}:")
    print("  M =", M)

print("\n=== Leading 3x3 D_2 = {0,1,2} expanded factor ===")
print(factor(minor_sym((0,1,2))))

print("\n=== Strong shifted 4x4 minors ===")
for S in [(1,2,3,4),(2,3,4,5)]:
    M = factor(minor_sym(S))
    print(f"\nS={S}:")
    print("  M =", M)
