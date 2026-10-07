"""Closed-form EXACT 2x2 non-CND certificate for f=p^d (r=0).
psi(i,j)=(S_{2i}+S_{2j}-2S_{i+j})/2,  S_m=log(p1)+...+log(p_m), p1=2,p2=3,p3=5,p4=7.
A(i,j)=psi(i,0)+psi(0,j)-psi(i,j), i,j in {1,2}.  psi(0,*)=psi(*,0): psi(i,0)=(S_{2i}-2S_i)/2.

Det A < 0  <=>  A not PSD (since trace>0)  <=>  psi not CND  <=>  no p^d is moment.
Compute det A in closed form in terms of L2=log2,L3=log3,L5=log5,L7=log7."""
from sympy import symbols, log, Rational, simplify, nsimplify, Matrix, expand, factor, N as Neval

L2,L3,L5,L7 = log(2),log(3),log(5),log(7)
S=[Rational(0), L2, L2+L3, L2+L3+L5, L2+L3+L5+L7]  # S_0..S_4

def psi(i,j):
    return (S[2*i]+S[2*j]-2*S[i+j])/2

A=Matrix(2,2, lambda a,b: ( (S[2*(a+1)]-2*S[a+1])/2 + (S[2*(b+1)]-2*S[b+1])/2 - psi(a+1,b+1) ))
A=A.applyfunc(simplify)
print("A (exact) =")
print("  A11 =", A[0,0], " = S2-2S1 = log3 - log2  =", simplify(A[0,0]))
print("  A12 =", simplify(A[0,1]))
print("  A22 =", simplify(A[1,1]))
detA=simplify(A.det())
print("det A (exact) =", detA)
print("det A (numeric) =", Neval(detA, 30))
trA=simplify(A.trace())
print("tr A =", trA, " numeric:", Neval(trA,20))
mn=Neval((trA - (trA**2-4*detA)**Rational(1,2))/2, 30)
print("min eigenvalue (exact formula, numeric) =", mn)
# Sign of det A is the whole story:
print()
print("det A < 0  =>  A indefinite  =>  psi NOT conditionally negative definite.")
print("By Schoenberg, exp(-d*psi) is NOT PSD for all sizes, for ANY d>0.")
print("Hence b_n=(prod p_i)^d is NOT a Hamburger moment sequence for any d>=1.")
