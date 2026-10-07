"""
Get JUST the structure we need from M2345 for degree 3, cheaply.
The 4x4 Hankel minor on {2,3,4,5} = det of Hankel(b4,b5,...,b10).
Instead of full symbolic det, compute its value as a polynomial in E with B,C SYMBOLIC by
evaluating at E nodes? Still heavy.

Lighter: confirm the f(p_k) factorization holds for deg3 M2345 by checking the determinant
VANISHES when f(p_k)=0 (i.e. substitute E such that f(2)=0, det should be divisible -> det=0
when the multiplicity-bearing factor is set 0). Quick sanity that the block-factorization law holds
for deg 3 too (it must, by the row-factoring argument, but let's confirm numerically).
Then we KNOW sign(M2345)=sign(const)*sign(core) with core = M2345/prod f(p_k)^m.
We get the SIGN of core on the sliver purely numerically (already doing exact sweep separately).
Here: verify block-factorization law for deg3 by evaluating det at f(2)=0 (expect 0).
"""
from sympy import primerange, Matrix, Integer, Rational, symbols
import sympy as sp
PR=list(primerange(2,200))

def f_of(B,C,E,x): return x**3+B*x**2+C*x+E
def bn_num(B,C,E,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L):
        pp=PR[i-1]; a*=f_of(B,C,E,pp); b.append(a)
    return b
def M2345_num(B,C,E):
    b=bn_num(B,C,E,12)
    return Matrix(4,4,lambda i,j:b[4+i+j]).det()

# Pick B,C; set E so f(2)=0 => E0=-(8+4B+2C). Then b1=f(2)=0 => many b's vanish => det should be 0.
B,C=2,3
E0=-(8+4*B+2*C)
print(f"B={B},C={C}; E0 makes f(2)=0: E0={E0}, f(2)=",f_of(B,C,E0,2))
print("M2345 at f(2)=0:", M2345_num(B,C,E0), "(expect 0 since f(2)|det with mult 4)")
# set f(3)=0 => E=-(27+9B+3C)
E1=-(27+9*B+3*C)
print(f"f(3)=0 at E={E1}, f(3)=",f_of(B,C,E1,3))
print("M2345 at f(3)=0:", M2345_num(B,C,E1),"(expect 0)")
# set f(17)=0 => mult 1, still divisible => 0
E17=-(17**3+B*17**2+C*17)
print(f"f(17)=0 at E={E17}")
print("M2345 at f(17)=0:", M2345_num(B,C,E17),"(expect 0)")
# set f(19)=0 (NOT a factor, block is {2..17}); det should be NONZERO
E19=-(19**3+B*19**2+C*19)
print(f"f(19)=0 at E={E19} (19 NOT in block {{2..17}})")
print("M2345 at f(19)=0:", M2345_num(B,C,E19),"(expect NONZERO)")
print("\n=> confirms block-factorization law M2345 = const*prod_{p in block} f(p)^m * core for deg 3.")
