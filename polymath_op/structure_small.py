"""
Structural analysis of small Hankel determinants in terms of ratios c_l.
b_0=1, b_1=c_1, b_2=c_1 c_2, b_3=c_1 c_2 c_3, ...
sign(D_N) = sign(det W_N) where row factoring removes b_i>0.

Goal: find the EXACT sign condition for D_2<0 and D_3<0 purely in terms
of the c_l, then specialize to c_l = f(p_l) and exploit prime gaps.
"""
from sympy import symbols, Matrix, factor, expand, simplify, Integer, primerange, collect, Poly

# symbolic ratios
c1,c2,c3,c4,c5,c6,c7,c8 = symbols('c1 c2 c3 c4 c5 c6 c7 c8', positive=True)
cs = [c1,c2,c3,c4,c5,c6,c7,c8]

def b_sym(n):
    if n==0: return Integer(1)
    r = Integer(1)
    for i in range(n): r *= cs[i]
    return r

def D_sym(N):
    return Matrix(N+1, N+1, lambda i,j: b_sym(i+j)).det()

print("D_1 =", factor(D_sym(1)))
print()
D2 = D_sym(2)
print("D_2 =", factor(D2))
print()
# W_2: divide by b_0,b_1,b_2 rows -> the sign-carrying matrix
# det W_2 sign:
print("D_2/(b_0 b_1 b_2) [should be the W-determinant, a polynomial in c's]:")
W2 = simplify(D2/(b_sym(0)*b_sym(1)*b_sym(2)))
print("   =", factor(W2))
print()

D3 = D_sym(3)
print("D_3 =", factor(D3))
print()
W3 = simplify(D3/(b_sym(0)*b_sym(1)*b_sym(2)*b_sym(3)))
print("D_3/(b_0 b_1 b_2 b_3) =", factor(W3))
print()

# Now: the lambda_2 = D_0 D_2 / D_1^2 = D_2/c1^2.  sign(lambda_2)=sign(D_2).
# D_2 factor reveals the condition. Let's see D_2 explicitly expanded/factored.
print("--- lambda_2 sign = sign(D_2). Examine factor structure ---")
print("lambda_2 = D_2/(b_1^2) =", factor(D2/b_sym(1)**2))
