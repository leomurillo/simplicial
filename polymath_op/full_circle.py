"""
FULL-CIRCLE verification: take a witness window (odd m => consecutive principal minor),
build the ACTUAL Hankel matrix (b_{i+j}) with b_n=prod f(p_i), extract the genuine 3x3
PRINCIPAL minor on rows/cols {i,i+1,i+2}, and confirm its determinant < 0.
This closes the chain  Q(m)>0  =>  3x3 principal minor < 0  =>  Hankel not PSD  =>
b_n NOT a Hamburger moment sequence.

We do this for a HIGH-degree f (p^12) and a large prime window, using EXACT integers.
"""
import sys
sys.set_int_max_str_digits(2000000)
from sympy import primerange, Integer, Matrix
P=list(primerange(2,300000))

def ndigits(n):
    n=int(n)
    if n==0: return 1
    return len(str(abs(n)))

def bn_full(f, upto):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,upto):
        a*=f(P[i-1]); b.append(a)
    return b

def principal_minor3(b, i):
    """3x3 principal minor on index set {i,i+1,i+2} of Hankel (b_{r+c})."""
    idx=[i,i+1,i+2]
    M=Matrix(3,3,lambda r,c: b[idx[r]+idx[c]])
    return M, M.det()

# find an odd-m witness for p^12 at a largish prime
G=[P[k+1]-P[k] for k in range(len(P)-1)]
def f(p): return p**12
# scan odd m (m=2i+1) i.e. window start index m-1; we want the consecutive minor {i,i+1,i+2}
# recall m (1-indexed window start) maps c_m=f(P[m-1]); minor index i=(m-1)//2 with m odd.
witness=None
for m in range(3, 2000, 2):  # odd m
    a,b,e=G[m-1],G[m],G[m+1]
    if b*b<=a*e: continue
    q=(P[m-1],P[m],P[m+1],P[m+2])
    A,B,C,D=f(q[0]),f(q[1]),f(q[2]),f(q[3])
    Q=(C-B)**2*A-(B-A)*(D-C)*C
    if Q>0:
        witness=m
        if P[m-1]>5000:  # take a reasonably large prime witness
            break
print("Chosen odd m =", witness, " window primes =", (P[witness-1],P[witness],P[witness+1],P[witness+2]))
i=(witness-1)//2
print("Corresponding principal-minor index set: {%d,%d,%d}"%(i,i+1,i+2))

need = max(i+1, witness)+3
b = bn_full(f, 2*(i+2)+3)
M, det = principal_minor3(b, i)
print("\n3x3 principal minor matrix (rows/cols {%d,%d,%d}) of the Hankel(b_{r+c}):"%(i,i+1,i+2))
print("  [b_%d b_%d b_%d]"%(2*i,i+(i+1),i+(i+2)))
print("  entries (digit counts):")
for r in range(3):
    print("   ", [ndigits(M[r,c]) for c in range(3)], "digit numbers")
print("  det digit count:", ndigits(det))
print("\n  det(3x3 principal minor) sign:", "NEGATIVE" if det<0 else ("zero" if det==0 else "positive"))
print("  det < 0 :", det<0)
print("\n  => the Hankel matrix (b_{i+j}) has a NEGATIVE 3x3 PRINCIPAL minor")
print("  => (b_n) is NOT positive semidefinite Hankel => NOT a Hamburger moment sequence. [for f=p^12]")

# also independently: the leading-determinant view -- confirm SOME principal minor negative
# via eigenvalue sign of the (i+3)-dim leading Hankel block? Not needed; principal minor suffices.
print("\n--- sanity: also show D_2-type leading minor sign for small f recovers known values ---")
def D(f,N):
    bb=bn_full(f,2*N+2); return Matrix(N+1,N+1,lambda r,c:bb[r+c]).det()
print("  f=p   D_3 =", D(lambda p:p,3), "(expect -787680)")
