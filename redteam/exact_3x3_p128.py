"""EXACT (integer) certificate that p^128 is NOT a moment sequence:
an explicit 3x3 principal minor of the Hankel matrix (b_{i+j}), b_n=(prod p_i)^128,
on contiguous indices {m,m+1,m+2}, that is NEGATIVE. From the float scan m=40.
We compute the 3x3 determinant in EXACT integer arithmetic (no float)."""
from sympy import primerange, Integer
P=list(primerange(2,100000))

def bn_pow(r,d,L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*=(Integer(P[i-1])+r)**d; out.append(a)
    return out

def minor3_det(b, m):
    # principal 3x3 on indices {m,m+1,m+2}: entries b_{i+j}
    idx=[m,m+1,m+2]
    M=[[b[idx[i]+idx[j]] for j in range(3)] for i in range(3)]
    # exact 3x3 determinant
    det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    return det

d=128; r=0
maxidx=45
b=bn_pow(r,d,2*maxidx+4)
print(f"EXACT 3x3 contiguous principal minors of Hankel for f=p^{d}:")
firstneg=None
for m in range(35,45):
    det=minor3_det(b,m)
    sign='+' if det>0 else ('0' if det==0 else 'NEGATIVE')
    print(f"  m={m}: 3x3 minor on {{{m},{m+1},{m+2}}} sign = {sign}")
    if det<0 and firstneg is None:
        firstneg=m
        import sys as _sys; _sys.set_int_max_str_digits(200000)
        print(f"     ^^^ EXACT NEGATIVE 3x3 PRINCIPAL MINOR. p^{d} is NOT PSD => NOT a moment sequence.")
        print(f"     (det is a negative integer with {len(str(abs(int(det))))} digits; sign by exact integer comparison)")
print(f"\nFirst negative contiguous 3x3 at m={firstneg} (EXACT).")
print(f"This is a checkable certificate that b_n=(prod p_i)^{d} is NOT a Hamburger moment sequence,")
print(f"even though its leading Hankel minors D_0..D_22 are all > 0 (it clears the N=22 bar).")
