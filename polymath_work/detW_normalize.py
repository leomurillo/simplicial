"""
Normalize det W_N to find clean inequality.

KEY IDEA: The Hankel matrix H = (b_{i+j}). b_n = prod_{k=1}^n c_k.
W_{ij} = b_{i+j}/b_i = prod_{l=i+1}^{i+j} c_l.

Alternative: factor differently. Consider the SUBSTITUTION that turns
the AP case into the moment case cleanly.

Standard fact: a sequence (b_n) is a Hamburger moment sequence iff ALL Hankel
determinants D_N >= 0 (and a Stieltjes condition for shifted). Actually for
Hamburger: positive semidefinite Hankel => moment (by Hamburger's theorem,
need D_N >= 0 for the genuine moment; strictly the condition is the Hankel
forms are PSD).

We want to show SOME D_N < 0.

LOG-CONVEXITY ANGLE:
D_1 = b0*b2 - b1^2 = b1^2 ( (b0 b2)/b1^2 - 1 ) ... with b0=1:
   D_1 = b2 - b1^2.  In ratios: b1=c1, b2=c1 c2. D_1 = c1 c2 - c1^2 = c1(c2-c1).
   >0 iff c2>c1.  For monic f and primes, c2=f(3)>f(2)=c1 (increasing). So D_1>0 always.
   (This is just log-convexity of b: b_{n-1} b_{n+1} >= b_n^2 iff c_{n+1}>=c_n.)

So D_1>=0 is automatic for increasing c (which holds for monic incr f on primes).
The OBSTRUCTION is at D_2 (3x3) and beyond.

Let me get the cleanest form of det W_2.
det W_2 = -c1 c2^2 + 2 c1 c2 c3 - c1 c3 c4 - c2 c3^2 + c2 c3 c4
"""
from sympy import symbols, simplify, factor, expand, together, cancel, Rational

c1,c2,c3,c4,c5,c6,c7,c8 = symbols('c1 c2 c3 c4 c5 c6 c7 c8', positive=True)

d2 = -c1*c2**2 + 2*c1*c2*c3 - c1*c3*c4 - c2*c3**2 + c2*c3*c4

# Try grouping as a "discrete convexity" expression.
# Hypothesis: d2 = c3*[ (c2-c1)(c4 - c2) - (c2-c1)(...) ]? Let's solve.
# Rearrange: d2 = c2 c3 c4 - c1 c3 c4 - c1 c2^2 + 2 c1 c2 c3 - c2 c3^2
#              = c3 c4 (c2 - c1) - c2^2 c1 + 2 c1 c2 c3 - c2 c3^2
# Group last three: -(c1 c2^2 - 2 c1 c2 c3 + c2 c3^2) = -c2(c1 c2 - 2 c1 c3 + c3^2)?
#    c1 c2 - 2 c1 c3 + c3^2 -- not a clean square.
# Try: -c2( c1 c2 - 2 c1 c3 + c3^2 ). Expand: -c1 c2^2 + 2 c1 c2 c3 - c2 c3^2. YES matches.
test = c3*c4*(c2-c1) - c2*(c1*c2 - 2*c1*c3 + c3**2)
print("regroup check d2:", expand(test - d2))  # should be 0

# So d2 = c3 c4 (c2-c1) - c2 (c1 c2 - 2 c1 c3 + c3^2)
# Note c1 c2 - 2 c1 c3 + c3^2 ... hmm. Let me instead complete differently:
#   c1 c2 - 2 c1 c3 + c3^2 = c1(c2 - c3) - c3(c1 - c3) = c1(c2-c3) + c3(c3-c1)
# Alternatively divide everything by c1 c2 c3 (all positive) to make a ratio inequality.
# Define u = c2/c1, v = c3/c2, w = c4/c3 (consecutive ratios of the c's).
u,v,w = symbols('u v w', positive=True)
# c1 = c1, c2 = c1 u, c3 = c1 u v, c4 = c1 u v w
sub = {c2: c1*u, c3: c1*u*v, c4: c1*u*v*w}
d2s = expand(d2.subs(sub))
print("d2 in c1,u,v,w:", d2s)
d2s_fac = factor(d2s)
print("d2 factored:", d2s_fac)
# divide by c1^? to get pure ratio expression
print("d2 / c1^3 :", simplify(d2s/c1**3))
