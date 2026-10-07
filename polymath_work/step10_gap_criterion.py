"""
Verify the gap criterion. For window primes q1<q2<q3<q4 (consecutive),
define exact ratios u=f(q2)/f(q1), v=f(q3)/f(q2), s=f(q4)/f(q3),
a=u-1,b=v-1,e=s-1.  EXACT R = a*e - b**2 + 2*a*b*e + a*b**2*e.
Q>0 <=> R<0.

Asymptotic leading term: ae - b^2 ~ d^2 * [ g1*g3/(q1 q3) - g2^2/q2^2 ], gk gaps.
Equivalent leading criterion:  g2^2 / q2^2 > g1 g3 /(q1 q3),  i.e.
   (g2/q2)^2 > (g1/q1)(g3/q3)  approx  -> 'gap convexity spike'.

TEST 1: Does sign(R) == sign(ae - b^2) for the actual prime windows (leading term dominates)?
TEST 2: For f(x)=x (d=1): compute R exactly on each window, and compare to the pure-gap
        quantity G = g1*g3*q2^2 - g2^2*q1*q3  (sign should match R<0 <=> minor<0).
TEST 3: find smallest r where 'gap spike' G>0 holds (q2 gap is locally large).
"""
from sympy import primerange, Integer, Rational

P = list(primerange(2, 2_000_000))

def Rexact(f, r):
    q1,q2,q3,q4 = P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1; b=v-1; e=s-1
    return a*e - b**2 + 2*a*b*e + a*b**2*e, (a*e-b**2), (q1,q2,q3,q4)

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f

# For f(x)=x: gap quantity
def gapG(r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    g1=q2-q1; g2=q3-q2; g3=q4-q3
    # leading criterion R<0 <=> ae-b^2<0 <=> d^2[g1 g3/(q1 q3) - g2^2/q2^2]<0
    # <=> g1 g3 q2^2 < g2^2 q1 q3 . Define G = g2^2 q1 q3 - g1 g3 q2^2 ; R<0(leading) <=> G>0
    return g2*g2*q1*q3 - g1*g3*q2*q2

fid = poly([Integer(1),Integer(0)])  # f(x)=x
print("=== f(x)=x : exact R sign vs leading ae-b^2 sign vs gap G sign (first 40 r) ===")
mismatch=0
firstRneg=None; firstGpos=None
for r in range(0,40):
    Rfull, Rlead, qs = Rexact(fid,r)
    G = gapG(r)
    sR = (Rfull<0); sL=(Rlead<0); sG=(G>0)
    if firstRneg is None and sR: firstRneg=r
    if firstGpos is None and sG: firstGpos=r
    if not (sR==sL==sG):
        mismatch+=1
        if mismatch<=15:
            print(f"  r={r} q={qs} Rfull<0={sR} Rlead<0={sL} G>0={sG}  Rfull={Rfull} G={G}")
print(f"first r with exact R<0 (minor neg): {firstRneg}")
print(f"first r with gap G>0: {firstGpos}")
print(f"sign mismatches among R<0 / leading / G in 0..39: {mismatch}")

# Confirm minor sign directly for f=x at firstRneg
from sympy import Matrix
def bn(f,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(P[i-1]); b.append(a)
    return b
def minor(f,S):
    b=bn(f,2*max(S)+2); n=len(S)
    return Matrix(n,n,lambda i,j:b[S[i]+S[j]]).det()
if firstRneg is not None:
    r=firstRneg
    print(f"\nDirect minor M_{{{r},{r+1},{r+2}}}(f=x) =", minor(fid,(r,r+1,r+2)))

# Show the gap structure around firstGpos
if firstGpos is not None:
    r=firstGpos
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    print(f"\nGap spike at r={firstGpos}: primes {q1},{q2},{q3},{q4} gaps {q2-q1},{q3-q2},{q4-q3}")
