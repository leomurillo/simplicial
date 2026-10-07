"""Exact NON-LEADING principal minor scan for the p^d candidate.
Build the (Nmax+1)x(Nmax+1) Hankel exactly, then:
  (A) check ALL k-subsets for k=2,3,4,5 (feasible counts) -> small-minor violations
  (B) check all CONTIGUOUS windows [a..a+w] for w up to Nmax (these are the
      'shifted leading minors', Hankel of the shifted sequence) via Bareiss
  (C) check 'arithmetic-progression' index sets {a, a+s, a+2s, ...}
If everything >=0 through the whole 23x23 block, this is a COUNTEREXAMPLE."""
import sys, itertools
from sympy import primerange, Integer, Matrix
P = list(primerange(2, 100000))

def bn_pow(r, d, L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (Integer(P[i-1])+r)**d; out.append(a)
    return out

def submatrix_det(b, idx):
    n=len(idx)
    M=[[b[idx[i]+idx[j]] for j in range(n)] for i in range(n)]
    # Bareiss det
    prev=Integer(1); sign=1; M=[row[:] for row in M]
    for k in range(n):
        if M[k][k]==0:
            # pivot swap among rows below
            sw=None
            for i in range(k+1,n):
                if M[i][k]!=0: sw=i;break
            if sw is None: return Integer(0)
            M[k],M[sw]=M[sw],M[k]; sign=-sign
        pk=M[k][k]
        for i in range(k+1,n):
            Mik=M[i][k]
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*pk - Mik*M[k][j])//prev
            M[i][k]=Integer(0)
        prev=pk
    return sign*M[n-1][n-1]

def scan(r, d, Nmax):
    b = bn_pow(r, d, 2*Nmax+2)
    idx_all = list(range(Nmax+1))
    # (A) all small subsets k=2..5
    for k in [2,3,4,5]:
        cnt=0; negs=[]
        for sub in itertools.combinations(idx_all, k):
            det = submatrix_det(b, list(sub))
            cnt+=1
            if det < 0:
                negs.append((sub, det))
        print(f"  k={k}: checked {cnt} subsets, negatives={len(negs)}")
        if negs:
            print(f"    FIRST NEGATIVE {k}x{k} minor: idx={negs[0][0]}  det<0")
            return ('NONPSD', k, negs[0][0])
    # (B) contiguous windows
    for w in range(1, Nmax+1):
        for a in range(0, Nmax+1-w):
            sub=list(range(a, a+w+1))
            det=submatrix_det(b, sub)
            if det<0:
                print(f"  contiguous window [{a}..{a+w}] det<0")
                return ('NONPSD','window',(a,a+w))
    # (C) AP index sets
    for s in range(2,6):
        for a in range(0, Nmax+1):
            sub=[a+s*t for t in range(0, (Nmax-a)//s+1)]
            if len(sub)<2: continue
            det=submatrix_det(b, sub)
            if det<0:
                print(f"  AP set start={a} step={s} det<0: {sub}")
                return ('NONPSD','AP',(a,s))
    return ('PSD-so-far', None, None)

if __name__=="__main__":
    d=int(sys.argv[1]); r=int(sys.argv[2]) if len(sys.argv)>2 else 0
    Nmax=int(sys.argv[3]) if len(sys.argv)>3 else 22
    print(f"NON-LEADING scan f=(p+{r})^{d}, Nmax={Nmax}")
    verdict=scan(r,d,Nmax)
    print("VERDICT:", verdict)
