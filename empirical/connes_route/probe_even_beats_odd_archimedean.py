"""
Even-beats-odd for the finite Weil form, decomposed -- the structural half of Connes step (a).
Standard convention RH <=> Q >= 0; pole term = |fhat(i/2)|^2+|fhat(-i/2)|^2 = sum of squares =
POSITIVE in BOTH sectors: even +2(int f cosh u/2)^2, odd +2(int f sinh u/2)^2 (for odd real f,
fhat(+-i/2)=+- int f sinh). Separate even (cos) and odd (sin) Dirichlet sectors on [-a,a]; report
the lowest eigenvalue of each at three assembly levels.

MECHANISM (the program-native point): Omega_inf(r)=Re psi(1/4+ir/2)-log pi is DEEPEST at r=0;
even fns have fhat(0)=int f != 0 and bind there, odd fns have fhat(0)=0 (vanish quadratically) and
are BLIND to the deepest well -> even binds lower. = CBS symmetric(S)/arrow(A) split; even=S binds,
odd=arrow A (apex non-normality / sqrt i) blind. = apex=prolate Slepian ordering chi_0>chi_1.

mpmath, no torch.  usage: py probe_even_beats_odd_archimedean.py [dps=35] [N=20] [X=13]
"""
import mpmath as mp, sys
DPS=int(sys.argv[1]) if len(sys.argv)>1 else 35
NE =int(sys.argv[2]) if len(sys.argv)>2 else 20
X  =int(sys.argv[3]) if len(sys.argv)>3 else 13
GLP=20
mp.mp.dps=DPS
a=mp.log(X)/2
we=[(2*j+1)*mp.pi/(2*a) for j in range(NE)]
wo=[(k+1)*mp.pi/a       for k in range(NE)]
def prime_powers(X):
    s=[True]*(X+1); out=[]
    for i in range(2,X+1):
        if s[i]:
            for m in range(i*i,X+1,i): s[m]=False
    for p in [p for p in range(2,X+1) if s[p]]:
        pe=p
        while pe<=X: out.append((pe,mp.log(p))); pe*=p
    return out
PP=prime_powers(X)
def gauss_legendre(n):
    nd=[];wt=[]
    for i in range(1,n+1):
        x=mp.cos(mp.pi*(i-mp.mpf('0.25'))/(n+mp.mpf('0.5')))
        for _ in range(80):
            p0,p1=mp.mpf(1),x
            for k in range(2,n+1): p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
            dp=n*(x*p1-p0)/(x*x-1); dx=p1/dp; x-=dx
            if abs(dx)<mp.mpf(10)**(-DPS-3): break
        p0,p1=mp.mpf(1),x
        for k in range(2,n+1): p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
        dp=n*(x*p1-p0)/(x*x-1); nd.append(x); wt.append(2/((1-x*x)*dp*dp))
    return nd,wt
gn,gw=gauss_legendre(GLP)
def Omega(r): return mp.re(mp.digamma(mp.mpf('0.25')+0.5j*r))-mp.log(mp.pi)
def ehat_e(j,r):
    wj=we[j]; d=wj*wj-r*r
    if abs(d)<mp.mpf(10)**(-DPS+5): return ((-1)**j)*(2*wj/mp.sqrt(a))*(a*((-1)**j)/(2*wj))
    return ((-1)**j)*(2*wj/mp.sqrt(a))*mp.cos(r*a)/d
def ehat_o(k,r):
    wk=wo[k]; d=wk*wk-r*r
    if abs(d)<mp.mpf(10)**(-DPS+5): return ((-1)**(k+1))*(2*wk/mp.sqrt(a))*(a*((-1)**(k+1))/(2*wk))
    return ((-1)**(k+1))*(2*wk/mp.sqrt(a))*mp.sin(r*a)/d
half=mp.pi/(2*a)/2; Rmax=max(we[-1],wo[-1])*2+80; npan=int(mp.nint(Rmax/half))+1
rs=[];ws=[]
for ip in range(npan):
    lo=ip*half; mid=lo+half/2; hw=half/2
    for t,wt in zip(gn,gw): rs.append(mid+hw*t); ws.append(wt*hw)
P=len(rs); Om=[Omega(r) for r in rs]; wom=[ws[m]*Om[m] for m in range(P)]
def basis_e(j,u): return mp.cos(we[j]*u)/mp.sqrt(a)
def basis_o(k,u): return mp.sin(wo[k]*u)/mp.sqrt(a)
def build(sector, primes, pole):
    n=NE; hat=ehat_e if sector=='even' else ehat_o
    EH=[[hat(j,r) for r in rs] for j in range(n)]
    A=mp.zeros(n,n)
    for j in range(n):
        for k in range(j,n):
            s=mp.mpf(0)
            for m in range(P): s+=wom[m]*EH[j][m]*EH[k][m]
            A[j,k]=s/mp.pi
    if primes:
        bas=basis_e if sector=='even' else basis_o
        def C(j,k,t):
            lo=max(-a,t-a); hi=min(a,t+a)
            if hi<=lo: return mp.mpf(0)
            return mp.quad(lambda x: bas(j,x)*bas(k,x-t),[lo,hi])
        for j in range(n):
            for k in range(j,n):
                v=A[j,k]
                for (nn,lp) in PP: v+=-2*(lp/mp.sqrt(nn))*C(j,k,mp.log(nn))
                A[j,k]=v
    if pole:   # POSITIVE in both sectors (sum of squares |fhat(i/2)|^2+|fhat(-i/2)|^2)
        bas=basis_e if sector=='even' else basis_o
        g=mp.cosh if sector=='even' else mp.sinh
        c=[mp.quad(lambda u: bas(j,u)*g(u/2),[-a,0,a]) for j in range(n)]
        for j in range(n):
            for k in range(j,n): A[j,k]=A[j,k]+2*c[j]*c[k]
    for j in range(n):
        for k in range(j+1,n): A[k,j]=A[j,k]
    return A
print(f"# even-beats-odd (standard conv, +pole both sectors): X={X} a={mp.nstr(a,7)} NE={NE} dps={DPS}")
print(f"# Omega_inf(0)={mp.nstr(Omega(mp.mpf('1e-9')),8)} deepest; crosses 0 near r=6.3")
for (primes,pole,tag) in [(False,False,'PURE ARCH'),(False,True,'ARCH+POLE'),(True,True,'FULL WEIL')]:
    Ee,_=mp.eigsy(build('even',primes,pole)); Eo,_=mp.eigsy(build('odd',primes,pole))
    d=Eo[0]-Ee[0]
    print(f"  {tag:10s} even_min={mp.nstr(Ee[0],8):>12}  odd_min={mp.nstr(Eo[0],8):>12}  "
          f"Delta={mp.nstr(d,6):>10}  {'EVEN binds lower' if d>0 else 'odd lower'}")
