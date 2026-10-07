"""
Find the GEOMETRIC meaning of Q2 < 0.

Q2 = v^2(u-1) w - u v^2 + 2 v - 1.
u=c2/c1, v=c3/c2, w=c4/c3.

Let me re-express det W_2 < 0 directly in terms of c1,c2,c3,c4 in a way
that exposes a "second-difference" / "discrete convexity" structure.

det W_2 = c3 c4 (c2-c1) - c2(c1 c2 - 2 c1 c3 + c3^2).

Let me try the substitution to differences. Define the c-sequence and its
first differences d_l = c_{l+1} - c_l. For monic incr f, d_l>0.
"""
from sympy import symbols, simplify, factor, expand, collect, Rational, together

c1,c2,c3,c4 = symbols('c1 c2 c3 c4', positive=True)
d2 = -c1*c2**2 + 2*c1*c2*c3 - c1*c3*c4 - c2*c3**2 + c2*c3*c4

# Approach 1: write in terms of c1, and gaps g1=c2-c1, g2=c3-c2, g3=c4-c3.
g1,g2,g3 = symbols('g1 g2 g3')
sub = {c2: c1+g1, c3: c1+g1+g2, c4: c1+g1+g2+g3}
d2g = expand(d2.subs(sub))
print("det W_2 in (c1,g1,g2,g3):")
print(collect(d2g, c1))
print()
print("factor:", factor(d2g))
print()

# Approach 2: The truly clean object. det W_2 = det of
# [[1,c1,c1c2],[1,c2,c2c3],[1,c3,c3c4]].
# Subtract rows: R2-R1, R3-R2.
# This is like a divided-difference / Wronskian structure.
# Let's instead think of it as: the sequence m_k where in W, row i = (1, c_{i+1}-shifted...).
# Actually, KEY: consider the generating ratio. Define x_i = c_i (the ratio b_i/b_{i-1}).
# The Hankel PSD condition for moments. Let me directly compute the 2x2 leading + the
# crucial fact via the THREE-TERM structure.

# Approach 3: Hankel matrix H_2 itself (not W). H = [[b0,b1,b2],[b1,b2,b3],[b2,b3,b4]].
# b0=1, b1=c1, b2=c1c2, b3=c1c2c3, b4=c1c2c3c4.
from sympy import Matrix
b0,b1,b2,b3,b4 = 1, c1, c1*c2, c1*c2*c3, c1*c2*c3*c4
H2 = Matrix([[b0,b1,b2],[b1,b2,b3],[b2,b3,b4]])
print("D_2 (Hankel) =", factor(H2.det()))
print("  expand:", expand(H2.det()))
