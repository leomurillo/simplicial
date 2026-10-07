"""Structural probe: D_2 in terms of ratios c_1,c_2,c_3,c_4.
b_0=1, b_1=c1, b_2=c1c2, b_3=c1c2c3, b_4=c1c2c3c4.
D_1 = b0 b2 - b1^2 = c1c2 - c1^2 = c1(c2-c1).
For PSD need c2>=c1 (ratios non-decreasing) -- log-convexity.
D_2 = det[[b0,b1,b2],[b1,b2,b3],[b2,b3,b4]].
Let's get the factored form in c_i and see what 'irregular primes' must violate."""
from sympy import symbols, Matrix, factor, simplify, expand

c1,c2,c3,c4,c5,c6 = symbols('c1 c2 c3 c4 c5 c6', positive=True)
b = [1, c1, c1*c2, c1*c2*c3, c1*c2*c3*c4, c1*c2*c3*c4*c5, c1*c2*c3*c4*c5*c6]

def Dk(N):
    M = Matrix(N+1, N+1, lambda i,j: b[i+j])
    return factor(M.det())

print("D_1 =", Dk(1))
print("D_2 =", Dk(2))
print("D_2/(c1^? )... factor:")
d2 = Dk(2)
print("   ", d2)
# The 'det W' reduction: factor out b_i from rows. det W_2 should be a poly in c's.
# Show D_2 as product of positive prefactor times a 'shape' term.
