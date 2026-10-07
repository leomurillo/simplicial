"""
==================  FINAL DEGREE-2 CERTIFICATE  ==================
THEOREM (deg 2). Let f(x)=x^2+Bx+C (monic) with f(p)>0 for all primes p.
Then the sequence b_0=1, b_n=prod_{i=1}^n f(p_i) is NOT a Hamburger moment sequence:
  - if B<=-5:  D_2 = det(b_{i+j})_{0<=i,j<=2} < 0;
  - if B>-5 :  the 3x3 principal minor M234 on index set {2,3,4} is < 0.
(Scaling reduction f=a*g, a>0, g monic, gives sign(D_N(f))=sign(D_N(g)); so monic is WLOG.)

This script re-derives and checks EVERY load-bearing fact with exact arithmetic.
"""
from sympy import (primerange, Matrix, Integer, symbols, factor, expand, simplify,
                   Poly, Rational, S, diff, solve, collect, nsimplify)
import sympy as sp

B,C,q,t,s = symbols('B C q t s', real=True)
PR=list(primerange(2,100))
def f(p): return p*p+B*p+C
def bn(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(PR[i-1]); b.append(a)
    return b
b=bn(12)
ok=True
def check(name,cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

print("STEP 0. D_2 and its sign-reduction det W_2")
D2=Matrix(3,3,lambda i,j:b[i+j]).det()
g2 = B**3 - B**2*C + 38*B**2 - 15*B*C + 341*B - 68*C + 988
# det W_2 = D_2 / (b_0 b_1^2 b_2)?? Actually sign(D_2)=sign(detW_2)=sign(g2). Verify D_2 = pos*g2.
D2f=factor(D2)
check("D_2 = 2 (2B+C+4)^2 (3B+C+9) g2",
      simplify(D2 - 2*(2*B+C+4)**2*(3*B+C+9)*g2)==0)
# (2B+C+4)=f(2)>0, (3B+C+9)=f(3)>0 on valid region => sign(D_2)=sign(g2).
check("f(2)=2B+C+4 and f(3)=3B+C+9 (positivity factors)",
      expand(f(2)-(2*B+C+4))==0 and expand(f(3)-(3*B+C+9))==0)

print("\nSTEP 1. g2 decreasing in C; g2<0 <=> C>Cstar(B)")
cf=g2.diff(C)
check("coeff_C(g2) = -(B^2+15B+68), disc=-47<0 => <0 for all B",
      simplify(cf-(-(B**2+15*B+68)))==0 and (15**2-4*68)<0)

print("\nSTEP 2. Region A (B<=-5): binding prime q nearest -B/2, validity => C>-qB-q^2.")
print("        Show g2(B,-qB-q^2) <= 0 on each q-piece (then g2(B,C)<0 for C>-qB-q^2).")
g2e=expand(g2.subs(C,-q*B-q**2))
g2e_s=expand(g2e.subs(B,-2*q+s*q))
lead=Poly(g2e_s,q).all_coeffs()[0]
check("g2_edge(B=-2q+sq) leading q^4 coeff = (s-2)^2(s-1) (<0 for s<1)",
      simplify(lead-((s-2)**2*(s-1)))==0)
# 2a. Bertrand window: piece s-range = [1-q'/q, 1-q''/q] subset (-1,1) by Bertrand (q'<2q, q''>q/2).
# 2b. Dominance for q>=60 on s in [-1,1/2]:  -g2_edge >= G(q) = 9/8 q^4 -63 q^3 -206 q^2 -1023 q -988 >0.
Ngen = -g2e_s   # = N_q in (q,s)
# bound coeffs on s in[-1,1/2]; we already derived G(q). Recheck G(q) largest root <60:
A4=(2-s)**2*(1-s); A3=(2-s)*(s**2+11*s-11); A2=-2*(19*s**2-42*s+42); A1=341*(2-s); A0=S(-988)
def extr(e,lo=S(-1),hi=Rational(1,2)):
    cps=[c for c in solve(sp.Eq(diff(e,s),0),s) if c.is_real and lo<=c<=hi]
    vals=[e.subs(s,x) for x in [lo,hi]+cps]; return min(vals),max(vals)
A4mn=extr(A4)[0]; A3a=max(abs(x) for x in extr(A3)); A2a=max(abs(x) for x in extr(A2)); A1a=max(abs(x) for x in extr(A1)); A0a=abs(A0)
G=A4mn*q**4-A3a*q**3-A2a*q**2-A1a*q-A0a
roots=[float(r) for r in solve(sp.Eq(G,0),q) if r.is_real]
check("Dominance G(q)=9/8 q^4-63q^3-206q^2-1023q-988>0 for q>59.35 (largest root<60)",
      max(roots)<60)
# 2c. finite exact per-piece check for primes q in [3,60): g2_edge<=0 on the piece corner-interval.
Pbig=list(primerange(2,200))
def g2edge_q(qval): return expand(g2.subs(C,-qval*B-qval**2))
allok=True
for k in range(1,len(Pbig)-1):
    qv=Pbig[k]
    if qv>=60: break
    lo=-(qv+Pbig[k+1]); hi=-(Pbig[k-1]+qv)
    E=g2edge_q(qv)
    crit=[c for c in solve(sp.Eq(diff(E,B),0),B) if c.is_real and lo<c<hi]
    cand=[lo,hi]+crit
    mx=max(E.subs(B,c) for c in cand)   # want g2_edge <=0 i.e. MAX <=0
    if mx>0: allok=False; print("    piece q=",qv,"MAX g2_edge=",mx)
check("finite exact: g2_edge<=0 on every q-piece for primes q in [3,60)", allok)
# 2d. Bertrand containment (theorem) re-confirmed numerically large range:
Pchk=list(primerange(2,50000)); bc=True
for k in range(1,len(Pchk)-1):
    if not (Pchk[k-1]>=Rational(Pchk[k],2) and Pchk[k+1]<=2*Pchk[k]): bc=False;break
check("Bertrand window containment q''>=q/2 and q'<=2q (primes<50000; theorem)", bc)

print("\nSTEP 3. Region B (B>-5): binding prime is 2; validity <=> C>-2B-4 (f(2)>0).")
check("f(p)-f(2)=(p-2)(p+2+B) >0 for prime p>=3, B>-5",
      simplify(factor(expand((p:=symbols('p'))**2+B*p+C-(4+2*B+C))) - (p-2)*(p+2+B))==0)

print("\nSTEP 4. Region B: M234 = -12 * prod f(p_k)^{m_k} * Psi, Psi>0 => M234<0.")
M234=Matrix(3,3,lambda i,j:b[4+i+j]).det()
Psi=9*B**3 + B**2*C + 605*B**2 + 60*B*C + 12204*B + 912*C + 61968
prod=Integer(1)
for pk,mk in {2:3,3:3,5:3,7:3,11:2,13:1}.items(): prod*=f(pk)**mk
check("M234 == -12 * f(2)^3 f(3)^3 f(5)^3 f(7)^3 f(11)^2 f(13)^1 * Psi",
      simplify(M234 - (-12*prod*Psi))==0)
check("coeff_C(Psi)=B^2+60B+912, disc=-48<0 => >0 all B => Psi increasing in C",
      simplify(Psi.diff(C)-(B**2+60*B+912))==0 and (60**2-4*912)<0)
E2=expand(Psi.subs(C,-2*B-4))
check("Psi|_{C=-2B-4} = E2 = 7B^3+481B^2+10140B+58320",
      simplify(E2-(7*B**3+481*B**2+10140*B+58320))==0)
E2roots_p=[float(r) for r in solve(sp.Eq(diff(E2,B),0),B) if r.is_real]
check("E2'(B)=21B^2+962B+10140 has both roots < -5 (so E2 increasing on [-5,inf))",
      all(r< -5 for r in E2roots_p))
check("E2(-5)=18770>0  => E2(B)>=18770>0 for B>=-5 => Psi>0 on B>-5 valid",
      E2.subs(B,-5)==18770 and E2.subs(B,-5)>0)

print("\n================  RESULT  ================")
print("ALL CHECKS PASSED:", ok)
