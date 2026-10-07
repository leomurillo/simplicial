"""
Degree 3: analyze Psi3 (M234 = -12 * prod f(p_k)^m * Psi3). sign(M234)=-sign(Psi3) on valid.
Psi3 linear in E:  Psi3 = (coeffE) E + (rest).
coeffE = 912 B^2 + 60 B C + 1342 C + 474285 ... let me extract exactly.
Goal: replicate deg-2: on the region where prime 2 binds, reduce by E to a (B,C) problem,
evaluate at binding edge and see if Psi3>0 (=> M234<0).
Binding-prime-2 condition for cubic: f(p)-f(2)=(p-2)[p^2+2p+4 + B(p+2) + C] > 0 for prime p>=3
 <=> bracket Q_p(B,C) := p^2+2p+4 + B(p+2) + C > 0 for all primes p>=3.
The MOST binding is the smallest bracket; for p=3: 19 + 5B + C; p=5: 39+7B+C; ... bracket increases
with p if (slope in p)>0. So p=3 is the binding neighbor (smallest bracket) when B,C moderate.
Region where 2 binds: Q_3=5B+C+19>0 AND f(2)>0 ... actually need ALL Q_p>0; Q_3 smallest typically.
"""
import os
os.makedirs(r"C:\Projects\simplicial\polymath_certs", exist_ok=True)
from sympy import symbols, factor, expand, Poly, simplify, solve, S, primerange
import sympy as sp
B,C,E,p=symbols('B C E p', real=True)
Psi3 = (61968*B**3 + 12204*B**2*C + 912*B**2*E + 3003756*B**2 + 605*B*C**2 + 60*B*C*E
        + 468726*B*C + 41340*B*E + 42324361*B + 9*C**3 + C**2*E + 12087*C**2 + 1342*C*E
        + 4481955*C + 474285*E + 128230389)
coeffE = Psi3.diff(E)
restE = expand(Psi3 - coeffE*E)
print("Psi3 coeff of E:", factor(coeffE))
print("Psi3 (E=0) part:", factor(restE))

# binding-prime-2 region: need Q_p = p^2+2p+4 + B(p+2)+C >0 for all primes p>=3.
print("\nbracket Q_p = p^2+2p+4 + B(p+2) + C:")
for pk in [3,5,7,11,13]:
    print(f"  Q_{pk} =", expand(pk**2+2*pk+4 + B*(pk+2)+C))
# Q_p as function of p (continuous): increasing in p when d/dp>0: 2p+2 + B >0 i.e. p > -(B+2)/2.
# For B>-? the smallest prime p=3 gives smallest Q if 3 > -(B+2)/2 i.e. B > -8. So for B>-8, Q_3 is min.
print("\nFor B>-8, smallest bracket is Q_3=5B+C+19. So 2 binds (vs all p>=3) iff Q_3>0 AND f(2)>0.")
print("But also need Q_5,Q_7,...>0; since Q_p increasing in p for p>=3 when B>-8, Q_3>0 => all >0.")

# Now: in the binding-2 region, validity <=> f(2)>0 <=> E > -(4B+2C+8). Psi3 linear in E with
# coeff (912B^2+60BC+1342C+474285)?? wait coeffE includes C^2 term? recheck:
print("\ncoeffE expanded:", expand(coeffE))
# evaluate Psi3 at the binding edge E = -(4B+2C+8) (f(2)=0+):
Psi3_edge = expand(Psi3.subs(E, -(4*B+2*C+8)))
print("\nPsi3 at E=-(4B+2C+8) [f(2)=0 edge]:")
print("  =", factor(Psi3_edge))
with open(r"C:\Projects\simplicial\polymath_certs\deg3_Psi3_edge.txt","w") as fh:
    fh.write("coeffE: "+str(factor(coeffE))+"\n")
    fh.write("Psi3_edge: "+str(factor(Psi3_edge))+"\n")
