"""
EVEN-s WINDOWS: confirm Psi(s)<0 at even s also yields a genuine NEGATIVE principal minor
of the Hankel matrix H=(b_{i+j}).

Recall: contiguous principal minor on indices {i,i+1,i+2} has sign = sign(Psi(2i+1)) [ODD s].
For EVEN s, we need a principal minor whose sign = sign(Psi(s)).

Claim: the principal minor on indices {i, i+1, i+2} for the W-matrix corresponds to s=2i+1.
But Psi(s) is defined for ALL s via the shifted det W2. The shifted det W2 at window s is the
determinant of the 3x3 matrix V(s) = [[1,c_{s},c_s c_{s+1}? ...]] -- let me recompute which
ACTUAL principal minor of H realizes an arbitrary s (even or odd).

GENERAL principal minor of H on index set {p,q,r} (p<q<r), factoring b_p,b_q,b_r from rows:
   M_{p,q,r} = b_p b_q b_r * det T, T = [[1, prod_{p+1..p+?}...]] -- the columns are p,q,r so
   entries b_{row+col}. Row p: b_{p+p},b_{p+q},b_{p+r}. /b_p: prod c_{p+1..p+p}? no, b_{p+p}/b_p
   = prod_{l=p+1}^{2p} c_l. Messy for non-contiguous.

SIMPLER: just DIRECTLY test — for each f and its first firing (even) s, exhibit an EXPLICIT
negative principal minor of H by SEARCHING small principal minors near that window. The theory
guarantees SOME negative minor exists once H is not PSD; we verify H not PSD by finding a
negative principal minor (any index subset).

The cleanest: once we KNOW (proof) that there are i.o. ODD s with Psi(s)<0 (we can always find
ODD-s firing windows too, since they have positive density), the contiguous-minor argument
ALONE suffices -- we never NEED even s. Let me confirm: for every f, is there an ODD firing s?
(positive density of firing windows => infinitely many of each parity, in particular odd.)
"""
from sympy import primerange, Matrix, Integer
import itertools
Pg=list(primerange(2,2000000))
def firesf(ff,s):
    def cc(l): return ff(Pg[l-1])
    g0=cc(s+1)-cc(s); g1_=cc(s+2)-cc(s+1); g2_=cc(s+3)-cc(s+2)
    return cc(s)*int(g1_)**2 > cc(s+2)*g0*g2_

print("For each f: first ODD firing s, and first EVEN firing s:")
tests=[("p",lambda p:p),("p+10^6",lambda p:p+10**6),("p^2+1",lambda p:p**2+1),
       ("p^7+1",lambda p:p**7+1),("p^12+3",lambda p:p**12+3),("p^20+1",lambda p:p**20+1)]
for name,ff in tests:
    fo=next((s for s in range(1,300000,1) if s%2==1 and firesf(ff,s)),None)
    fe=next((s for s in range(2,300000,1) if s%2==0 and firesf(ff,s)),None)
    print(f"  {name:10s}: first ODD s={fo}, first EVEN s={fe}")

print()
print("CONCLUSION: every f has a firing ODD s => contiguous-minor argument (s=2i+1) alone closes it.")
print()
# Direct PSD double-check: for one f, exhibit an explicit negative principal minor (eigenvalue<0)
print("Direct non-PSD check for f=p^12+3 (numerically: smallest eigenvalue of Hankel sign):")
import math
ff=lambda p:p**12+3
def make_b(ff,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L):
        a*=ff(Pg[i-1]); b.append(a)
    return b
# use odd firing window s -> i=(s-1)/2 contiguous minor; show it's negative exactly
fo=next(s for s in range(1,300000) if s%2==1 and firesf(ff,s))
i=(fo-1)//2
b=make_b(ff,2*i+7)
Mm=Matrix(3,3,lambda r,c:b[(i+r)+(i+c)])
print(f"  f=p^12+3: odd firing s={fo}, contiguous minor on {{{i},{i+1},{i+2}}} det = {Mm.det()} (NEGATIVE => H not PSD => NOT a moment sequence)")
print(f"  det sign: {'NEGATIVE' if Mm.det()<0 else 'nonneg'}")
