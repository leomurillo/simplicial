"""
Deep structural analysis of the D_2 sign polynomial:
  Q2 := c1*c2^2 - 2*c1*c2*c3 + c1*c3*c4 + c2*c3^2 - c2*c3*c4
  D_2 < 0  <=>  Q2 > 0.
Rewrite Q2 in terms of gaps / try to expose a "convexity"-type structure.
"""
from sympy import symbols, factor, expand, simplify, collect, together, Integer, Rational

c1,c2,c3,c4 = symbols('c1 c2 c3 c4', positive=True)

Q2 = c1*c2**2 - 2*c1*c2*c3 + c1*c3*c4 + c2*c3**2 - c2*c3*c4

print("Q2 =", Q2)
print("Q2 factored:", factor(Q2))
print()

# group by c1 and the rest
print("collect on c1:", collect(expand(Q2), c1))
print("collect on c4:", collect(expand(Q2), c4))
print()

# Try writing as combination. Note coefficient of c1: c2^2-2 c2 c3 + c3 c4 = c2(c2-c3) - c3(c2-c4)
# coefficient of c4 (the c4 terms): c1 c3 - c2 c3 = c3(c1-c2)
# So Q2 = c1(c2^2 - 2 c2 c3) + c2 c3^2 + c4*c3*(c1-c2)
#       = c1 c2 (c2 - 2c3) + c2 c3^2 + c3 c4 (c1 - c2)

# Let me try the substitution c_i are *increasing* (true for f(p)=p+const, p^2 increasing).
# Define gaps. Actually let me look for the cleanest form.

# Hypothesis: Q2 relates to a 2x2 determinant / discrete second difference.
# Consider the "ratio of ratios": rho_i = c_{i+1}/c_i.
# Divide Q2 by c1 c3?
print("Q2/(c2*c3):", expand(Q2/(c2*c3)))
print("Q2/(c1*c2):", expand(Q2/(c1*c2)))
print()

# A cleaner approach: D_2 = det of 3x3 Hankel [[1,c1,c1c2],[c1,c1c2,c1c2c3],[c1c2,c1c2c3,c1c2c3c4]]
# Let me re-derive and look at it as quadratic form structure.

# Try: is Q2 = c3*(c1-c2)*(c4 - something) + (c2-c3)*(...) ?
# Q2 = c1 c2(c2-2c3)+c2 c3^2 + c3 c4(c1-c2)
expr = c1*c2*(c2-2*c3) + c2*c3**2 + c3*c4*(c1-c2)
print("check rewrite 1:", simplify(Q2-expr))

# = c1 c2^2 -2 c1 c2 c3 + c2 c3^2 + c3 c4 c1 - c3 c4 c2
# group (c1 c2^2 - 2 c1 c2 c3 + c1 c3^2)  - c1 c3^2 + c2 c3^2 + c3 c4(c1-c2)
# = c1(c2-c3)^2 - c3^2(c1-c2) + c3 c4 (c1-c2)
# = c1(c2-c3)^2 + c3(c1-c2)(c4 - c3)
expr2 = c1*(c2-c3)**2 + c3*(c1-c2)*(c4-c3)
print("check rewrite 2 (KEY):", simplify(Q2-expr2))
print()
print(">>> Q2 = c1*(c2-c3)^2 + c3*(c1-c2)*(c4-c3)")
print(">>> D_2 < 0  <=>  c1*(c2-c3)^2 + c3*(c1-c2)*(c4-c3) > 0")
