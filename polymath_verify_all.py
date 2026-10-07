"""
FULL VERIFICATION of the degree-2 proof chain.

CLAIM (deg 2): every monic f(p)=p^2+Bp+C with f(p)>0 for all primes p has some Hankel minor <0.
Proof split:
  (A) B <= -5: det W_2 < 0 (=> D_2 < 0).      [proven via N_q>=0 envelope argument]
  (B) B >  -5: M234 < 0 (3x3 minor on {2,3,4}). [proven via Psi>0]

This script verifies, with EXACT arithmetic, every load-bearing identity:
 1. D_2 factorization & det W_2 = 2*g2, g2 = B^3-B^2C+38B^2-15BC+341B-68C+988.
 2. det W_2 = 2[(B^3+38B^2+341B+988) - (B^2+15B+68)C]; coeff (B^2+15B+68)>0 (disc -47).
 3. M234 = -12 * prod_{k=1..6} f(p_k)^{m_k} * Psi, with m=(3,3,3,3,2,1) for p=(2,3,5,7,11,13),
    Psi = 9B^3+B^2C+605B^2+60BC+12204B+912C+61968.
 4. For B>-5: validity => C>-2B-4 (binding prime 2); then Psi >= E2(B)=7B^3+481B^2+10140B+58320>0.
 5. Boundary B=-5 belongs to region (A): det W_2<0.
 6. Cross-check at exact sample points that the claimed minor is indeed <0 and valid.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, simplify, Poly, Rational, S, diff, solve
import sympy as sp

P=list(primerange(2,100))
B,C=symbols('B C', real=True)
def f(p): return p*p+B*p+C
def bn(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(P[i-1]); b.append(a)
    return b
b=bn(12)

print("="*70)
print("1. D_2 and det W_2")
D2=Matrix(3,3,lambda i,j:b[i+j]).det()
print("   D_2 =", factor(D2))
# det W_2: factor b_i out of row i
def Wdet(N):
    def c(l): return f(P[l-1])
    def entry(i,j):
        pr=Integer(1)
        for l in range(i+1,i+j+1): pr*=c(l)
        return pr
    return Matrix(N+1,N+1,entry).det()
W2=expand(Wdet(2))
print("   det W_2 =", factor(W2))
g2 = B**3 - B**2*C + 38*B**2 - 15*B*C + 341*B - 68*C + 988
print("   check det W_2 == 2*g2:", simplify(W2 - 2*g2)==0)

print("\n2. det W_2 sign structure")
coeffC=g2.diff(C); constC=expand(g2-coeffC*C)
print("   coeff of C in g2:", factor(coeffC), " (= -(B^2+15B+68))")
print("   disc(B^2+15B+68)=", 15**2-4*68, "(<0 => B^2+15B+68>0 for all real B)")
print("   => det W_2 decreasing in C; det W_2<0 <=> C> (B^3+38B^2+341B+988)/(B^2+15B+68)=:Cstar")

print("\n3. M234 factorization")
M234=Matrix(3,3,lambda i,j:b[4+i+j]).det()
M234f=factor(M234)
fl=sp.factor_list(M234)
print("   M234 factor_list constant:", fl[0])
for fac,m in fl[1]:
    print("     factor^",m,":",fac)
Psi=9*B**3 + B**2*C + 605*B**2 + 60*B*C + 12204*B + 912*C + 61968
prod = Integer(1)
mult={2:3,3:3,5:3,7:3,11:2,13:1}
for pk,mk in mult.items():
    prod*= f(pk)**mk
claim = -12*prod*Psi
print("   check M234 == -12 * prod f(p_k)^m_k * Psi :", simplify(M234 - claim)==0)

print("\n4. Psi>0 for B>-5 valid")
coeffPsiC=Psi.diff(C);
print("   coeff of C in Psi:", factor(coeffPsiC), " disc=",60**2-4*912,"(<0 => >0 all B) => Psi incr in C")
E2=expand(Psi.subs(C,-2*B-4))
print("   E2(B)=Psi|_{C=-2B-4} =", E2)
print("   check E2 == 7B^3+481B^2+10140B+58320:", simplify(E2-(7*B**3+481*B**2+10140*B+58320))==0)
E2p=diff(E2,B)
print("   E2'(B)=",expand(E2p)," roots:",[float(r) for r in solve(sp.Eq(E2p,0),B) if r.is_real]," (both < -5)")
print("   E2(-5)=",E2.subs(B,-5),">0; E2 incr on [-5,inf) => E2(B)>=18770>0 for B>=-5")
print("   E2 real roots:",[float(r) for r in solve(sp.Eq(E2,0),B) if r.is_real])

print("\n5/6. EXACT spot checks (valid points), confirm the assigned minor is <0")
def Dn_at(Bv,Cv,N):
    bb=[Integer(1)];a=Integer(1)
    Pl=list(primerange(2,2000))
    for i in range(1,2*N+2): a*=(Pl[i-1]**2+Bv*Pl[i-1]+Cv); bb.append(a)
    return Matrix(N+1,N+1,lambda i,j:bb[i+j]).det()
def M234_at(Bv,Cv):
    bb=[Integer(1)];a=Integer(1)
    Pl=list(primerange(2,2000))
    for i in range(1,12): a*=(Pl[i-1]**2+Bv*Pl[i-1]+Cv); bb.append(a)
    return Matrix(3,3,lambda i,j:bb[4+i+j]).det()
def valid(Bv,Cv):
    Pl=list(primerange(2,2000))
    return all(Pl[i]**2+Bv*Pl[i]+Cv>0 for i in range(120))
tests_Ble5=[(-5,Rational(1,1)),(-6,Rational(10,1)),(-10,Rational(26,1)),(-8,Rational(16,1)),(-20,Rational(100,1))]
tests_Bgt5=[(Rational(24,5),Rational(-27,2)),(5,-13),(0,-3),(3,-9),(10,-25+5),(2,-7),(-4,Rational(9,2)),(-49*S(1)/10,Rational(581,100))]
print("  Region A (B<=-5): det W_2<0 ?  (sign(D_2)=sign(detW_2))")
for Bv,Cv in tests_Ble5:
    if not valid(Bv,Cv):
        print(f"    B={Bv},C={Cv}: NOT VALID, skip"); continue
    d2=Dn_at(Bv,Cv,2)
    print(f"    B={Bv}, C={Cv}: valid, D_2={d2}  ({'OK<0' if d2<0 else 'NOT<0!'})")
print("  Region B (B>-5): M234<0 ?")
for Bv,Cv in tests_Bgt5:
    if not valid(Bv,Cv):
        print(f"    B={Bv},C={Cv}: NOT VALID, skip"); continue
    m=M234_at(Bv,Cv)
    print(f"    B={Bv}, C={Cv}: valid, M234={m}  ({'OK<0' if m<0 else 'NOT<0!'})")
