"""
The band region needing D_3:  R = { B > -5,  Cmin(B) < C <= Cstar(B), valid }.
On the q=2 piece (B>-5), binding prime is 2, so Cmin(B) = -2B-4 (= -(f(2)-C)... i.e. f(2)>0).
Actually Cmin(B) = -2B-4 means f(2)=4+2B+C>0 i.e. C > -2B-4. For B>-5, is the binding prime
always 2? Envelope said q=2 binds for B in (-5, +oo). YES. So on B>-5: valid <=> C > -2B-4
(f(2)>0 is the binding constraint; need to CONFIRM f(p)>0 for all other p is implied).
=> band R = { B > -5,  -2B-4 < C <= Cstar(B) }.

det W_3 = -4 Φ(B,C). Want Φ>0 on R (=> D_3<0). Check numerically on a dense grid.
Also CONFIRM on B>-5, C>-2B-4 really is the full valid region (binding prime =2).
"""
from sympy import symbols, primerange, S
import sympy as sp
import numpy as np

P = list(primerange(2,200))
B,C = symbols('B C', real=True)

Phi = (547*B**6 + 297*B**5*C + 32888*B**5 + 21*B**4*C**2 + 17727*B**4*C + 749230*B**4
       - B**3*C**3 + 1302*B**3*C**2 + 385779*B**3*C + 8211596*B**3 - 29*B**2*C**3
       + 24885*B**2*C**2 + 3860625*B**2*C + 45675199*B**2 - 340*B*C**3 + 177108*B*C**2
       + 18423204*B*C + 118856828*B - 2256*C**3 + 445968*C**2 + 34380432*C + 99623856)
Phi_f = sp.lambdify((B,C), Phi, 'numpy')
Cstar_f = sp.lambdify(B, (B**3+38*B**2+341*B+988)/(B**2+15*B+68), 'numpy')

def valid(Bv,Cv):
    for q in P:
        if q*q+Bv*q+Cv <= 0: return False
    return True
def binding_is_2(Bv,Cv):
    # is f(2) the min over primes? check f(2)<=f(p) for all p
    f2 = 4+2*Bv+Cv
    for q in P:
        if q*q+Bv*q+Cv < f2 - 1e-9:
            return False
    return True

print("Scan band R: B>-5, -2B-4 < C <= Cstar(B). Report min Phi and any Phi<=0.")
minPhi = None; worst=None
viol_valid=[]  # points in (B>-5, C>-2B-4) that are NOT valid (would break 'binding=2')
bad_binding=[]
cnt=0
for Bv in np.linspace(-4.99, 200, 400):
    cs = Cstar_f(Bv)
    Clo = -2*Bv-4
    if cs <= Clo:   # band empty
        continue
    for Cv in np.linspace(Clo+1e-6, cs, 120):
        cnt+=1
        ph = Phi_f(Bv,Cv)
        if minPhi is None or ph<minPhi:
            minPhi=ph; worst=(Bv,Cv,ph)
        if ph<=0:
            viol_valid.append((Bv,Cv,ph))
        # spot-check validity / binding on a coarser subset
    # check validity & binding at band endpoints for this B
    for Cv in [Clo+1e-6, (Clo+cs)/2, cs]:
        if not valid(Bv,Cv): viol_valid.append(('INVALID',Bv,Cv))
        if not binding_is_2(Bv,Cv): bad_binding.append((Bv,Cv))

print(f"Scanned {cnt} band points.")
print("min Phi on band:", minPhi, " at (B,C,Phi)=", worst)
print("Phi<=0 occurrences:", [v for v in viol_valid if not (isinstance(v[0],str))][:10])
print("points where binding prime != 2 (B>-5):", bad_binding[:10], "(empty => binding is always p=2)")
