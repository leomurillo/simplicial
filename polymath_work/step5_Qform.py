"""
The 3x3 consecutive minor M_{r,r+1,r+2} = -(monomial)*Q_r where Q_r depends on
c_{2r+1}, c_{2r+2}, c_{2r+3}, c_{2r+4}.
Actually from output: for r=0, Q_0 uses c1,c2,c3,c4.  For r=1, Q_1 uses c3,c4,c5,c6.
So the consecutive 3x3 minor at base r uses c_{2r+1..2r+4}: a sliding window of 4 ratios,
step 2.   Let w,x,y,z = c_{2r+1},c_{2r+2},c_{2r+3},c_{2r+4}.
Claim: minor < 0  <=>  Q(w,x,y,z) > 0  where
   Q = w*x^2 - 2*w*x*y + w*y*z + x*y^2 - x*y*z
Let's CONFIRM the window/step and the universal shape, and re-derive Q in clean variables.
"""
from sympy import symbols, Matrix, factor, simplify, prod, Integer, expand, collect

NC = 16
c = symbols('c1:%d' % (NC+1), positive=True)
def b(n):
    if n == 0: return Integer(1)
    return prod(c[0:n])
def minor_sym(S):
    n = len(S)
    return Matrix(n, n, lambda a, d: b(S[a]+S[d])).det()

# clean variables for the window
w,x,y,z = symbols('w x y z', positive=True)
Q = w*x**2 - 2*w*x*y + w*y*z + x*y**2 - x*y*z

print("Universal Q (window of 4 ratios, step 2):")
print("  Q =", Q)
print("  Q factored =", factor(Q))
# regroup
print("  regrouped: x*(w*x - 2*w*y + y^2) + y*z*(w - x)")
chk = x*(w*x - 2*w*y + y**2) + y*z*(w - x)
print("  regroup matches:", expand(Q - chk) == 0)

# Verify for r=0,1,2,3: minor_{r,r+1,r+2} == -mono * Q(c_{2r+1},c_{2r+2},c_{2r+3},c_{2r+4})
print("\nVerify window/step for consecutive triples:")
for r in range(0,5):
    S=(r,r+1,r+2)
    M = minor_sym(S)
    sub = {w:c[2*r], x:c[2*r+1], y:c[2*r+2], z:c[2*r+3]}  # c_{2r+1}=c[2r] (0-indexed)
    Qsub = Q.subs(sub)
    # the monomial prefactor = -M / Q? compute ratio
    ratio = simplify(M / (-Qsub))
    print(f"  r={r}: M / (-Q_window) = {factor(ratio)}  (should be a positive monomial in c's)")

# So minor<0  <=>  Q>0. Express Q in terms of f at primes:
# w=f(p_{2r+1}), x=f(p_{2r+2}), y=f(p_{2r+3}), z=f(p_{2r+4}).
# For LEADING D_2 (r=0): w=f(2),x=f(3),y=f(5),z=f(7).
print("\nLEADING D_2: minor sign = -Q(f(2),f(3),f(5),f(7)); D_2<0 <=> Q>0")
print("  Q = f(3)*[f(2)f(3) - 2 f(2)f(5) + f(5)^2] + f(5)f(7)*[f(2)-f(3)]")
