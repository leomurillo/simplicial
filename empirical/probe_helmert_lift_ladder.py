"""
probe_helmert_lift_ladder.py  --  the upward lift on (2,3,5), BOTH ways.

ONE STEP:  R^N  <->  H_{N+1}   (N Cartesian numbers  =  sum-zero (N+1)-vector), an exact bijection.

PART 1  HELMERT (sequential / ordered / real):  v = sum_k x_k h_k,  h_k=(1,...,1,-k,0,...,0).
        Climb 3 -> 8, watch the leading-zero CASCADE push the content to the tail; descend back exactly.
PART 2  FOURIER (symmetric / cyclic / complex):  v = sum_c x_c chi_c,  chi_c(s)=exp(2pi i c s/(N+1)).
        The 'other way' on the same (2,3,5): no cascade, the mass sits in the DC slot, shape in
        conjugate pairs. Same target H_{N+1}, exact round-trip.

Pure python (fractions) for Helmert; numpy for Fourier. No torch.
"""
from fractions import Fraction as F
import numpy as np

# ============================== PART 1 : HELMERT (exact, integer) ==============================
def helmert(N, M):  return [[1]*k + [-k] + [0]*(M-k-1) for k in range(1, N+1)]
def lift(x):        N=len(x); M=N+1; H=helmert(N,M); return [sum(x[k]*H[k][i] for k in range(N)) for i in range(M)], H
def project(v,H):   return [F(sum(h[i]*v[i] for i in range(len(v))), (j+1)*(j+2)) for j,h in enumerate(H)]
def show(v):        return "[" + ", ".join(str(int(t)) if F(t).denominator==1 else str(t) for t in v) + "]"
def lead0(v):       return next((i for i,t in enumerate(v) if t!=0), len(v))

print("="*92)
print("PART 1  --  HELMERT lift on (2,3,5):  3 -> 8   (sequential, real; watch the cascade)")
print("="*92)
cur=[F(2),F(3),F(5)]; Hs=[]
for _ in range(5):                                   # 3->4,4->5,5->6,6->7,7->8
    v,H=lift(cur); ok=(project(v,H)==cur); N=len(cur)
    print(f"  R^{N} {show(cur):<40} -> H_{N+1} {show(v):<42} sum={int(sum(v))}  lead0={lead0(v)}  rt={ok}")
    Hs.append(H); cur=v
down=cur
for H in reversed(Hs): down=project(down,H)
print(f"\n  full descent 8->3 recovers the start exactly: {down==[F(2),F(3),F(5)]}   {show(down)}")
print(f"  => the content (2,3,5) has walked out to the LAST 4 slots of the 8-vector; leading zeros = rung-4.")

# ============================== PART 2 : FOURIER (symmetric, complex) ==========================
def cx(z):
    a=round(z.real,6); b=round(z.imag,6)
    ai,bi=int(round(a)),int(round(b))
    if abs(a-ai)<1e-6: a=ai
    if abs(b-bi)<1e-6: b=bi
    if b==0: return f"{a}"
    if a==0: return f"{b}i"
    return f"{a}{'+' if b>=0 else '-'}{abs(b)}i"
def cshow(v): return "[" + ", ".join(cx(z) for z in v) + "]"
def f_lift(x):
    N=len(x); M=N+1; s=np.arange(M)
    chi=np.array([np.exp(2j*np.pi*c*s/M) for c in range(1,M)])   # c=1..N
    return x@chi, M
def f_proj(v,M):
    s=np.arange(M)
    return np.array([(v*np.exp(-2j*np.pi*c*s/M)).sum()/M for c in range(1,M)])

print("\n"+"="*92)
print("PART 2  --  FOURIER lift on (2,3,5):  R^3 -> H_4   (symmetric, cyclic, complex; the 'other way')")
print("="*92)
x=np.array([2.,3.,5.])
v,M=f_lift(x); back=f_proj(v,M)
print(f"  R^3 [2, 3, 5]")
print(f"   -> H_4 (Z/4 characters, omega=i):  {cshow(v)}     sum = {cx(v.sum())}")
print(f"   round-trip back = {cshow(back)}   exact match: {np.allclose(back,x)}")
print(f"   DC slot (s=0) = {cx(v[0])} = the mass 2+3+5;  s=1,s=3 are a conjugate pair (the shape); s=2 real.")
# one iteration to show DC->0 but NO growing cascade
v2,M2=f_lift(v)
print(f"\n  iterate once (R^4 -> H_5, Z/5):  DC slot = {cx(v2[0])}  (=sum of a sum-zero vector -> 0),")
print(f"   but the other 4 slots stay nonzero/spread: {cshow(v2[1:])}")
print(f"   => Fourier has at most a single DC-zero, NEVER the Helmert leading-zero cascade.")

print("\n"+"="*92)
print("THE TWO WAYS, side by side (same (2,3,5), same target H_{N+1}, both exact bijections)")
print("="*92)
print("""   HELMERT (sequential)        FOURIER (cyclic)
   - real, integer-friendly     - complex (conjugate-symmetric for real input)
   - slot ORDER matters         - all slots equal (cyclic-symmetric)
   - mass -> coord 0; then a     - mass -> DC slot (s=0); shape -> conjugate
     CASCADE of leading zeros      pairs; sum-zero only kills the DC, no cascade
   - content migrates to TAIL    - content stays spread over the cyclic slots
   Both meet coord-0 = the sum (the 'mass') = 10. They are the two orthonormal frames of H_{N+1};
   the change of basis BETWEEN them is exactly the apex unitary U_N (Helmert <-> Fourier).""")
