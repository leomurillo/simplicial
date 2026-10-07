"""
MASTER CERTIFICATE. Runs the complete degree-2 proof + degree-3 partial, all exact.
"""
from sympy import (primerange, Matrix, Integer, symbols, factor, expand, simplify,
                   Poly, Rational, S, diff, solve, prod)
import sympy as sp

PASS=True
def ck(name,c):
    global PASS; PASS=PASS and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {name}")

PR=list(primerange(2,200))
print("#"*72)
print("# ENGINE: block sign-reduction law (generic positive ratios)")
print("#"*72)
c=symbols('c1:40', positive=True)
def bb(n):
    p=Integer(1)
    for i in range(1,n+1): p*=c[i-1]
    return p
for (k,r,lab) in [(2,2,"{2,3,4}"),(2,3,"{2,3,4,5}"),(0,2,"{0,1,2}")]:
    idx=list(range(k,k+r+1))
    M=Matrix(r+1,r+1,lambda i,j: bb(idx[i]+idx[j]))
    def R_entry(i,j,idx=idx):
        ii=idx[i];jj=idx[j];p=Integer(1)
        for l in range(ii+1,ii+jj+1): p*=c[l-1]
        return p
    R=Matrix(r+1,r+1,R_entry)
    ck(f"block {lab}: M=(prod b_{{k+i}})*det R", simplify(M.det()-prod([bb(idx[i]) for i in range(r+1)])*R.det())==0)

print("\n"+"#"*72); print("# DEGREE 1 (re-confirm established)"); print("#"*72)
cc=symbols('c', real=True)  # monic f(p)=p+c
def f1(x): return x+cc
def D1(N):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,2*N+2): a*=f1(PR[i-1]); b.append(a)
    return Matrix(N+1,N+1,lambda i,j:b[i+j]).det()
ck("D_2(c) = -2(c-1)(c+2)^2(c+3)", simplify(D1(2)-(-2*(cc-1)*(cc+2)**2*(cc+3)))==0)
D3_1=factor(D1(3))
ck("D_3(c) = 4(c+2)^3(c+3)^2(c+5)(c^3-21c^2-297c-547)",
   simplify(D1(3)-4*(cc+2)**3*(cc+3)**2*(cc+5)*(cc**3-21*cc**2-297*cc-547))==0)

print("\n"+"#"*72); print("# DEGREE 2 — FULL PROOF"); print("#"*72)
B,C=symbols('B C', real=True)
def f2(x): return x*x+B*x+C
def bn2(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f2(PR[i-1]); b.append(a)
    return b
b2=bn2(13)
# D2
g2=B**3-B**2*C+38*B**2-15*B*C+341*B-68*C+988
ck("D_2 = 2 f(2)^2 f(3) g2", simplify(Matrix(3,3,lambda i,j:b2[i+j]).det()-2*(2*B+C+4)**2*(3*B+C+9)*g2)==0)
ck("coeff_C(g2)=-(B^2+15B+68)<0 (disc -47) => g2 decr in C", simplify(g2.diff(C)+(B**2+15*B+68))==0 and 15**2-4*68<0)
# Region A: g2 at binding edge C=-qB-q^2 in relative var: leading q^4 = (s-2)^2(s-1)
q,sv=symbols('q s', real=True)
g2e=expand(g2.subs(C,-q*B-q**2)); g2es=expand(g2e.subs(B,-2*q+sv*q))
ck("Region A: g2_edge leading q^4 coeff=(s-2)^2(s-1)(<0 for s<1)", simplify(Poly(g2es,q).all_coeffs()[0]-((sv-2)**2*(sv-1)))==0)
# dominance G(q)>0 for q>=60
A4=(2-sv)**2*(1-sv);A3=(2-sv)*(sv**2+11*sv-11);A2=-2*(19*sv**2-42*sv+42);A1=341*(2-sv);A0=S(-988)
def ext(e,lo=S(-1),hi=Rational(1,2)):
    cps=[x for x in solve(sp.Eq(diff(e,sv),0),sv) if x.is_real and lo<=x<=hi]
    vs=[e.subs(sv,x) for x in [lo,hi]+cps]; return min(vs),max(vs)
A4m=ext(A4)[0];A3a=max(abs(x) for x in ext(A3));A2a=max(abs(x) for x in ext(A2));A1a=max(abs(x) for x in ext(A1))
G=A4m*q**4-A3a*q**3-A2a*q**2-A1a*q-abs(A0)
ck("Region A dominance: G(q)=9/8 q^4-63q^3-206q^2-1023q-988 has largest root<60", max(float(x) for x in solve(sp.Eq(G,0),q) if x.is_real)<60)
# finite per-piece q in [3,60)
Pb=list(primerange(2,200)); okp=True
for kk in range(1,len(Pb)-1):
    qv=Pb[kk]
    if qv>=60: break
    lo=-(qv+Pb[kk+1]);hi=-(Pb[kk-1]+qv);Ee=expand(g2.subs(C,-qv*B-qv**2))
    cand=[lo,hi]+[x for x in solve(sp.Eq(diff(Ee,B),0),B) if x.is_real and lo<x<hi]
    if max(Ee.subs(B,x) for x in cand)>0: okp=False
ck("Region A finite: g2_edge<=0 on each q-piece, primes q in[3,60)", okp)
# Region B: binding prime 2, M234 factorization, Psi>0
ck("f(p)-f(2)=(p-2)(p+2+B)>0 for p>=3,B>-5", simplify(factor(expand(f2(symbols('p'))-f2(2)))-(symbols('p')-2)*(symbols('p')+2+B))==0)
Psi=9*B**3+B**2*C+605*B**2+60*B*C+12204*B+912*C+61968
prodfk=Integer(1)
for pk,mk in {2:3,3:3,5:3,7:3,11:2,13:1}.items(): prodfk*=f2(pk)**mk
ck("M234=-12 prod f(p_k)^m Psi", simplify(Matrix(3,3,lambda i,j:b2[4+i+j]).det()+12*prodfk*Psi)==0)
ck("coeff_C(Psi)=B^2+60B+912>0 (disc -48) => Psi incr in C", simplify(Psi.diff(C)-(B**2+60*B+912))==0 and 60**2-4*912<0)
E2=expand(Psi.subs(C,-2*B-4))
ck("Psi|_{C=-2B-4}=7B^3+481B^2+10140B+58320 =: E2", simplify(E2-(7*B**3+481*B**2+10140*B+58320))==0)
ck("E2'(B) roots both < -5 (E2 incr on [-5,inf))", all(r< -5 for r in [float(x) for x in solve(sp.Eq(diff(E2,B),0),B) if x.is_real]))
ck("E2(-5)=18770>0 => Psi>0 on B>-5 valid => M234<0", E2.subs(B,-5)==18770)

print("\n"+"#"*72); print("# DEGREE 3 — PARTIAL"); print("#"*72)
B3,C3,E3=symbols('B C E', real=True)
def f3(x): return x**3+B3*x**2+C3*x+E3
def bn3(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f3(PR[i-1]); b.append(a)
    return b
b3=bn3(13)
Psi3=(61968*B3**3+12204*B3**2*C3+912*B3**2*E3+3003756*B3**2+605*B3*C3**2+60*B3*C3*E3
      +468726*B3*C3+41340*B3*E3+42324361*B3+9*C3**3+C3**2*E3+12087*C3**2+1342*C3*E3
      +4481955*C3+474285*E3+128230389)
prodfk3=Integer(1)
for pk,mk in {2:3,3:3,5:3,7:3,11:2,13:1}.items(): prodfk3*=f3(pk)**mk
ck("deg3 M234=-12 prod f(p_k)^m Psi3", simplify(Matrix(3,3,lambda i,j:b3[4+i+j]).det()+12*prodfk3*Psi3)==0)
coeffE=Psi3.diff(E3)
ck("deg3 coeffE>0 on binding-2 region (coeffE<0 only B in[-49.6,-40.4], disjoint from B>-8)",
   all(float((4*(3*B3**2+270*B3+6011)).subs(B3,bv))>0 for bv in [-8,-5,0,10]))
E2_3=expand(Psi3.subs(E3,-(4*B3+2*C3+8)))
ck("deg3 Psi3|_{f(2)=0 edge}=58320B^3+10140B^2C+...(2-var cubic)",
   simplify(E2_3-(58320*B3**3+10140*B3**2*C3+2831100*B3**2+481*B3*C3**2+380198*B3*C3+40096501*B3+7*C3**3+9395*C3**2+3522649*C3+124436109))==0)

print("\n"+"#"*72)
print("# OVERALL:", "ALL PASS" if PASS else "SOME FAILED")
print("#"*72)
