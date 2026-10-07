"""
Show N_q(B) >= 0 on the INTERIOR of each q-piece (between envelope corners),
for the generic prime q. Combined with N>=0 at corners, gives N>=0 on the whole ray B<=-5,
hence Cmin>=Cstar, hence detW2 < 0 on the ENTIRE valid region with B<=-5.

N_q(B) = (-qB - q^2)(B^2+15B+68) - (B^3+38B^2+341B+988)
       = -q B^3 - q^2 B^2 - 15 q B^2 - 15 q^2 B - 68 q B - 68 q^2 - B^3 - 38 B^2 - 341 B - 988
Let's get it symbolic in q and B, then analyze on the piece.
The q-piece B-interval is ( -(q+nextprime), -(prevprime+q) ). To make a q-UNIFORM argument,
note this interval is a SUBSET of B in [ -2q - G, -2q + G ] where G = max prime gap near q.
But cleaner: at the binding piece, the *defining* property is that q is the closest prime to
the vertex v=-B/2, i.e. |v-q| <= |v-q'| and |v-q| <= |v-q''| for neighbors. Equivalently
  -(q+q') <= B <= -(q''+q)   (the corners).
We'll just prove: for ALL real B in [-(q+q'), -(q''+q)], N_q(B) >= 0, by showing N_q is
positive there. Strategy that is q-uniform: substitute B = -2q + t and bound.
"""
from sympy import symbols, expand, factor, simplify, collect, Poly, Rational, sqrt
import sympy as sp

B, q, t = symbols('B q t', real=True)
Nq = expand((-q*B - q**2)*(B**2+15*B+68) - (B**3+38*B**2+341*B+988))
print("N_q(B) =", Nq)
print()
# Substitute B = -2q + t  (t = B+2q, the deviation of B from -2q; vertex v=-B/2 = q - t/2)
Nsub = expand(Nq.subs(B, -2*q + t))
Nsub = collect(Nsub, t)
print("N_q(-2q + t) =", Nsub)
print()
# Group by powers of t
poly_t = Poly(Nsub, t)
print("As polynomial in t (coeffs are polynomials in q):")
for deg, coeff in zip(range(poly_t.degree(), -1, -1), poly_t.all_coeffs()):
    print(f"   t^{deg}: {factor(coeff)}")
