"""Sign of the contiguous 3x3 Hankel minor in terms of consecutive ratios.
Hankel minor on {m,m+1,m+2} uses b_{2m},b_{2m+1},b_{2m+2},b_{2m+3},b_{2m+4}.
Factor out positive b's: set t_k = c_{2m+k} (the four relevant ratios
c_{2m+1},c_{2m+2},c_{2m+3},c_{2m+4}). Get sign as a function of (t1,t2,t3,t4)."""
from sympy import symbols, Matrix, factor, simplify, expand, Symbol

# Let B0=b_{2m}, then b_{2m+1}=B0*t1, b_{2m+2}=B0*t1*t2, b_{2m+3}=B0*t1*t2*t3, b_{2m+4}=B0*t1*t2*t3*t4
B0,t1,t2,t3,t4 = symbols('B0 t1 t2 t3 t4', positive=True)
e=[B0, B0*t1, B0*t1*t2, B0*t1*t2*t3, B0*t1*t2*t3*t4]  # b_{2m+0..4}
M=Matrix(3,3, lambda i,j: e[i+j])
det=factor(M.det())
print("3x3 contiguous Hankel minor det =")
print("  ", det)
# strip positive prefactor B0^3 * t1^2 * t2 ... to isolate the SIGN-deciding bracket
# divide by the obvious positive monomial:
from sympy import Poly, together, cancel
# det should be B0^3 * t1^2 * t2 * (bracket). Extract bracket:
bracket=simplify(det/(B0**3*t1**2*t2))
print("sign-deciding bracket (det / (B0^3 t1^2 t2)) =")
print("  ", factor(bracket))
# Interpret: define ratios of ratios u=t3/t2, etc. The minor<0 iff bracket<0.
# Rewrite bracket in terms of g2=t2, and second-differences.
print()
# Substitute t_k = R^k (pure geometric) -> should be >=0 (geometric = point mass, moment):
R=Symbol('R',positive=True)
print("geometric test t_k=R^k:", simplify(bracket.subs({t1:R,t2:R**2,t3:R**3,t4:R**4})))
# AP-in-log? t_k = exp(a + b k): t1=E*Q, t2=E*Q^2.. with E=exp(a),Q=exp(b)? that's geometric again in index.
# Try t_k = (k)!-like: t_k from c_i AP: c_i = i  -> t_k = (2m+k). Test linear ratios:
print("linear-ratio test t_k=(s+k):")
s=Symbol('s',positive=True)
print("   ", factor(simplify(bracket.subs({t1:s+1,t2:s+2,t3:s+3,t4:s+4}))))
