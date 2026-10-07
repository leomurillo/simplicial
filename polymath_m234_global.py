"""
HYPOTHESIS: M234 < 0 on the ENTIRE valid region (all B, monic quadratic).
M234 = -12 * [prod f(p_k)>0] * Psi,  so M234<0 <=> Psi>0.
Psi = (B^2+60B+912) C + (9B^3+605B^2+12204B+61968), increasing in C (coeff>0 always).
On valid region, C > Cmin(B) = max_p (-(p^2+Bp)). On the binding piece (prime q),
Cmin = -q*B - q^2. So Psi > Psi|_{C=-qB-q^2} = (B^2+60B+912)(-qB-q^2)+(9B^3+...).
Define E_q(B) = Psi at C=-qB-q^2. M234<0 on whole valid region  <=  E_q(B) >= 0 on each
q-piece's B-interval (then Psi>E_q>=0 for the strict-interior valid C).
Test: compute E_q(B) for binding prime q on each piece; check >=0 on the piece B-interval.
Also: direct numeric scan over the whole valid region for any Psi<=0.
"""
from sympy import symbols, primerange, factor, expand, S, Rational, lambdify, solve
import sympy as sp
import numpy as np

B=symbols('B', real=True)
C=symbols('C', real=True)
P=list(primerange(2,5000))
Psi = 9*B**3 + B**2*C + 605*B**2 + 60*B*C + 12204*B + 912*C + 61968

# (1) Whole-region numeric scan for Psi<=0 within valid region.
Psif=lambdify((B,C),Psi,'numpy')
def Cmin(Bv): return max(-(q*q+Bv*q) for q in P[:300])
bad=[]; mn=None; total=0
for Bv in np.linspace(-200,200,800):
    cmn=Cmin(Bv)
    for Cv in np.linspace(cmn+1e-6, cmn+5000, 200):
        total+=1
        v=Psif(Bv,Cv)
        if mn is None or v<mn: mn=v; mnat=(Bv,Cv)
        if v<=0: bad.append((round(Bv,2),round(Cv,2),v))
print(f"Whole-region scan ({total} valid pts, B in [-200,200]): Psi<=0 occurrences: {len(bad)}")
print(f"  min Psi = {mn:.3f} at {mnat}")
print("  sample Psi<=0:", bad[:8])

# (2) Per-piece exact: E_q(B) = Psi at C = -qB - q^2, check >=0 on corner-interval of q.
def Eq(q):
    return expand(Psi.subs(C, -q*B - q**2))
print("\nPer-piece: E_q(B)=Psi|_{C=-qB-q^2}; want >=0 on [-(q+q'), -(q''+q)].")
worst=None; fails=[]
for k in range(0, 800):
    q=P[k]
    if k==0:
        lo=-(P[0]+P[1]); hi=sp.oo   # B in (-5, +oo)
    else:
        lo=-(q+P[k+1]); hi=-(P[k-1]+q)
    E=Eq(q); Ep=sp.diff(E,B)
    crit=[r for r in solve(sp.Eq(Ep,0),B) if r.is_real]
    cand=[lo]+([hi] if hi!=sp.oo else [])
    cand+=[c for c in crit if (lo<c) and (hi==sp.oo or c<hi)]
    # for the unbounded piece (q=2), also check behavior as B->+oo: leading coeff of E in B
    if hi==sp.oo:
        lead=sp.Poly(E,B).all_coeffs()[0]
        # E ~ lead*B^3; if lead>0 -> +inf, fine
    vals=[E.subs(B,c) for c in cand]
    mn2=min(vals) if vals else S(0)
    # for unbounded, also ensure E>0 for large B: check sign of leading coeff
    if hi==sp.oo:
        leadcoeff=sp.Poly(E,B).LC()
        bigok = leadcoeff>0
    else:
        bigok=True
    if worst is None or float(mn2)<float(worst[0]):
        worst=(mn2,q,[(str(c),float(E.subs(B,c))) for c in cand])
    if mn2<0 or not bigok:
        fails.append((q,lo,hi,float(mn2),bigok))
print("  fails (E_q<0 somewhere on piece OR bad large-B):", fails[:10], " count", len(fails))
print("  worst min E_q over pieces:", float(worst[0]), "at q=", worst[1])
print("  E_2(B) =", factor(Eq(2)))
print("  leading coeff E_2:", sp.Poly(Eq(2),B).LC(), "(>0 => E_2->+inf as B->+inf)")
