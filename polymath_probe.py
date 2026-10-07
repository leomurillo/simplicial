"""
Probe the region where BOTH D_2>=0 and D_3>=0 (Phi<=0 on the band). Find what minor IS negative.
Use EXACT arithmetic at sample rational points. Check leading D_2..D_6 and ALL principal minors.
"""
from sympy import primerange, Matrix, Integer, Rational, symbols
import sympy as sp
import itertools

P = list(primerange(2, 2000))

def bn_num(Bv, Cv, L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (P[i-1]**2 + Bv*P[i-1] + Cv)
        b.append(a)
    return b

def hankel(Bv,Cv,N):
    b=bn_num(Bv,Cv,2*N+2)
    return Matrix(N+1,N+1,lambda i,j: b[i+j])

def leadingdets(Bv,Cv,Nmax):
    b=bn_num(Bv,Cv,2*Nmax+2)
    out=[]
    for N in range(0,Nmax+1):
        out.append(Matrix(N+1,N+1,lambda i,j:b[i+j]).det())
    return out

def all_principal_minors_neg(Bv,Cv,Nmax):
    # Hankel of size (Nmax+1); check all principal minors (subsets of {0..Nmax})
    b=bn_num(Bv,Cv,2*Nmax+2)
    H=Matrix(Nmax+1,Nmax+1,lambda i,j:b[i+j])
    negs=[]
    idx=list(range(Nmax+1))
    for r in range(1,Nmax+2):
        for sub in itertools.combinations(idx,r):
            sub=list(sub)
            M=H[sub,sub]
            d=M.det()
            if d<0:
                negs.append((tuple(sub),d))
    return negs

# Test points (rationals near the problem area). f(p)=p^2+Bp+C, valid (f(2)>0 etc).
tests = [
    (Rational(24,5), Rational(-135,10)),   # ~ (4.8, -13.5) the worst-Phi point
    (5, -13),
    (5, -10),
    (4, -10),
    (3, -8),
    (10, -25),     # B>-5 large
    (2, -8),
    (1, -6),
    (0, -4),       # near c-like
    (Rational(1,1), Rational(-6,1)),
]
for Bv,Cv in tests:
    # validity
    ok=all(P[i]**2+Bv*P[i]+Cv>0 for i in range(50))
    ld=leadingdets(Bv,Cv,6)
    signs=['+' if d>0 else ('-' if d<0 else '0') for d in ld]
    # first negative leading minor index
    firstneg=next((N for N,d in enumerate(ld) if d<0), None)
    print(f"B={Bv}, C={Cv}  valid={ok}")
    print(f"   leading D_0..D_6 signs: {signs}")
    if firstneg is not None:
        print(f"   -> first NEGATIVE leading minor at N={firstneg}: D_{firstneg}={ld[firstneg]}")
    else:
        # search non-leading principal minors up to size 6
        negs=all_principal_minors_neg(Bv,Cv,6)
        print(f"   -> NO negative leading minor up to D_6. Negative PRINCIPAL minors: {negs[:5]}")
