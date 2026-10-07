"""verify_diez43.py — exact re-derivation of the [P] claims in the Diez Thm 4.3 skeleton,
before any of it is landed in the manuscripts.  Deterministic; no external audit script trusted.
  (1) transfer identity (N0 Lemma 6.8) on genuine characters mod 15
  (2) the level schedule theta_0(n), C*(n)  and the table in diez_4_3_skeleton.md sec.4
  (3) the Holder cap theta_0(n) <= 3/4  <=>  n <= 10  (sec.5)
  (4) the 6/11 razor at n=5, the capacity-fraction deflation, the C* -> 3 asymptote
"""
import math, cmath
from sympy import primerange, primorial, prime

# ---------------------------------------------------------------- (1) IDENTITY
def lambda_sieve(X):
    X=int(X); spf=list(range(X+1)); L=[0.0]*(X+1)
    for p in primerange(2,X+1):
        pe=p
        while pe<=X:
            L[pe]=math.log(p); pe*=p
    return L
def dlog(gen, m):           # discrete log base gen mod m
    d={}; g=1
    for k in range(m):
        if math.gcd(g,m)==1: d[g]=k
        g=(g*gen)%m
    return d
def identity_mod15(X=20000):
    X=int(X); L=lambda_sieve(X)
    d=15; phi=8; units=[a for a in range(d) if math.gcd(a,d)==1]
    dl3=dlog(2,3); dl5=dlog(2,5)        # (Z/3)*=<2> ord2 ; (Z/5)*=<2> ord4
    chars=[(j3,j5) for j3 in range(2) for j5 in range(4)]   # 8 chars (j3 mod2, j5 mod4)
    def chi(c,n):
        if math.gcd(n,15)!=1: return 0
        j3,j5=c
        ang=j3*dl3[n%3]/2 + j5*dl5[n%5]/4
        return cmath.exp(2j*math.pi*ang)
    # psi(X,chi)
    psi={c:sum(L[n]*chi(c,n) for n in range(2,X+1)) for c in chars}
    # psi(X;15,a) coprime classes
    psiA={a:sum(L[n] for n in range(2,X+1) if n%15==a) for a in units}
    mu=sum(psiA.values())/phi
    Delta={a:psiA[a]-mu for a in units}
    V=sum(D*D for D in Delta.values()); D3=sum(D**3 for D in Delta.values())
    lhs=phi**2*sum(v**3 for v in psiA.values())
    # character side: sum over triples chi1 chi2 chi3 = chi0 (j3 sum=0 mod2, j5 sum=0 mod4)
    rhs=0
    for c1 in chars:
        for c2 in chars:
            c3=((-(c1[0]+c2[0]))%2, (-(c1[1]+c2[1]))%4)
            rhs+=psi[c1]*psi[c2]*psi[c3]
    rhs=rhs.real
    expand=phi*mu**3 + 3*mu*V + D3
    print("(1) TRANSFER IDENTITY  mod 15, X=%d"%X)
    print("    phi^2 * sum_a psi^3           = %.10e"%lhs)
    print("    sum_{chi1chi2chi3=chi0} prod  = %.10e   reldiff=%.2e"%(rhs,abs(lhs-rhs)/abs(lhs)))
    print("    phi*mu^3 + 3 mu V + sum D^3   = %.10e   reldiff=%.2e"%(expand,abs(lhs-expand)/abs(lhs)))
    print("    toy limbs:  main=phi*mu^3=%.3e  linear=3 mu V=%.3e  cubic=sum D^3=%.3e"%(phi*mu**3,3*mu*V,D3))

# ---------------------------------------------------------------- (2,3,4) SCHEDULE
def pure_V(n):              # ocho sec.5 : 2 + (1/6) sum_{i=3}^n (p_i^2 - 1)
    ps=list(primerange(2, prime(n)+1))
    return 2 + sum((p*p-1) for p in ps[2:])/6.0   # ps[2:] = p_3, p_4, ...
def logPn(n):               # log of primorial P_n = prod_{i<=n} p_i
    return sum(math.log(p) for p in primerange(2, prime(n)+1))
def theta0(n): return 1 - math.log(pure_V(n))/logPn(n)
def Cstar(n):  return n*(1-theta0(n))

def schedule():
    print("\n(2) LEVEL SCHEDULE  theta_0(n)=1-log(pure_V)/log(P_n),  C*(n)=n(1-theta_0)")
    skel={3:(0.473,1.580),5:(0.545,2.277),6:(0.600,2.402),7:(0.642,2.503),
          10:(0.735,2.650),15:(0.818,2.733),20:(0.862,2.766),30:(0.907,2.781),50:(0.944,2.796)}
    print("     n |  pure_V        theta_0   C*     | skeleton theta_0/C*   match")
    for n in sorted(skel):
        t,c=theta0(n),Cstar(n); st,sc=skel[n]
        ok="OK" if abs(t-st)<5e-4 and abs(c-sc)<5e-4 else "MISMATCH"
        print("    %3d | %12.2f  %.4f   %.4f | %.3f / %.3f        %s"%(n,pure_V(n),t,c,st,sc,ok))
    print("    C* asymptote (n=100,300,1000): %.3f %.3f %.3f  (-> 3)"%(Cstar(100),Cstar(300),Cstar(1000)))

def holder_cap():
    print("\n(3) HOLDER CAP  theta_0(n) <= 3/4  closes Lemma 6.8 remainder; find the ceiling")
    for n in range(8,14):
        print("    n=%2d: theta_0=%.4f  %s 3/4"%(n,theta0(n),"<=" if theta0(n)<=0.75 else "> "))
    ceil=max(n for n in range(3,60) if theta0(n)<=0.75)
    print("    => Holder route ceiling: n <= %d  (claim: n<=10)"%ceil)

def razor_and_capacity():
    print("\n(4) the 6/11 razor at n=5, and the capacity-fraction deflation")
    print("    theta_0(5)=%.4f   6/11=%.4f   margin=%.1e  (6/11 > theta_0(5)? %s)"%(
        theta0(5),6/11,6/11-theta0(5),6/11>theta0(5)))
    print("    capacity 6*pure_V/P_n^2 :", end="")
    for n in [3,4,5,6,7]:
        Pn=int(primorial(n)); print(" n=%d:%.2e"%(n,6*pure_V(n)/Pn**2), end="")
    print()

if __name__=="__main__":
    identity_mod15(20000)
    schedule(); holder_cap(); razor_and_capacity()
