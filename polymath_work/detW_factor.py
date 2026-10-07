"""
Factor det W_2 and det W_3 and find the clean 'non-moment inequality' form.
"""
from sympy import symbols, Matrix, factor, collect, simplify, Integer, expand, Poly

cs = symbols('c1:13', positive=True)
c = {l: cs[l-1] for l in range(1, 13)}

def Wmat(N):
    def entry(i, j):
        p = Integer(1)
        for l in range(i+1, i+j+1):
            p *= c[l]
        return p
    return Matrix(N+1, N+1, entry)

# det W_2
d2 = expand(Wmat(2).det())
print("det W_2 raw:", d2)
# Try to factor out c2*c3 etc and recognize structure
# d2 = -c1 c2^2 + 2 c1 c2 c3 - c1 c3 c4 - c2 c3^2 + c2 c3 c4
# group:
c1,c2,c3,c4,c5,c6,c7,c8 = cs[:8]
# Let's see d2 as combination
f2 = factor(d2)
print("det W_2 factored:", f2)
# Express in terms of differences. Try writing d2 = -(c2-c1)*something + ...
# Hypothesis: d2 relates to c3*(c2-c1)*(...) Let's just collect.
print()
print("collect by c4:", collect(d2, c4))
print("collect by c1:", collect(d2, c1))
print()

# det W_3
d3 = expand(Wmat(3).det())
f3 = factor(d3)
print("det W_3 factored:", f3)
print()

# Key idea: normalize. Since all c_i>0, divide det W_2 by (c1*c2*c3) etc?
# Actually the cleaner object: log-convexity. Let's define ratios.
# Let's test: is there a common factor?
from sympy import gcd
print("d2 is already irreducible per factor():", f2)
