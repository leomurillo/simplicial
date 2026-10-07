"""
Weil quadratic form v3 -- parity-separated. v2 already reproduced the zeta zeros
(14.13,21.02,25.00,30.42,32.96 to 3 digits) but the minimal eigenvector was a near-degenerate
EVEN+ODD mix (spurious low zeros 3.68,6.09; gap ~1e-4; mixed parity). The form commutes with
parity P (x->-x) = functional equation s<->1-s, so diagonalize the EVEN and ODD blocks
separately. This isolates the clean even ground state (Connes' eta) and tests S6.6(a):
is the global ground state EVEN, and is it SIMPLE (gap within its sector + below the other
sector)?

Exact archimedean kernel K_inf(u)=-e^{-|u|/2}/(1-e^{-2|u|}); rank-2 main 2cosh((x-y)/2);
primes<=X. numpy+mpmath. No torch.
"""
import numpy as np

def prime_powers(X):
    sieve=np.ones(X+1,bool); sieve[:2]=False
    for i in range(2,int(X**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    out=[]
    for p in np.where(sieve)[0]:
        pe=int(p)
        while pe<=X: out.append((pe,float(np.log(p)))); pe*=int(p)
    return out

def K_inf(u):
    au=np.abs(u); return np.where(au<1e-12,0.0,-np.exp(-au/2)/(1-np.exp(-2*au)+1e-300))

def build(X, N=420):
    a=0.5*np.log(X); x=(np.arange(N)-(N-1)/2)* (2*a/(N-1)); dx=x[1]-x[0]
    D=x[:,None]-x[None,:]
    M=K_inf(D)*dx*dx; np.fill_diagonal(M,0.0)
    M+=2*np.cosh(D/2)*dx*dx
    for (n,logp) in prime_powers(X):
        t=np.log(n); w=logp/np.sqrt(n); xt=x-t
        for i in range(N):
            xp=xt[i]
            if xp<x[0] or xp>x[-1]: continue
            jf=(xp-x[0])/dx; j=int(np.floor(jf)); fr=jf-j
            if 0<=j<N-1: M[i,j]+=-2*w*dx*(1-fr); M[i,j+1]+=-2*w*dx*fr
    M=0.5*(M+M.T)
    return x,dx,M

def parity_blocks(M,N):
    # symmetric grid: pair (k, N-1-k). even = e_k+e_{N-1-k}, odd = e_k-e_{N-1-k}
    ne=N//2
    Be=np.zeros((N,ne)); Bo=np.zeros((N,ne))
    for k in range(ne):
        Be[k,k]=1/np.sqrt(2); Be[N-1-k,k]=1/np.sqrt(2)
        Bo[k,k]=1/np.sqrt(2); Bo[N-1-k,k]=-1/np.sqrt(2)
    return Be,Bo

def fz(x,dx,B,vec,even=True,rmax=45):
    eta=B@vec
    rr=np.linspace(1.0,rmax,5000)
    if even: eh=np.array([(eta*np.cos(rv*x)).sum()*dx for rv in rr])
    else:    eh=np.array([(eta*np.sin(rv*x)).sum()*dx for rv in rr])
    z=[]
    for k in range(len(rr)-1):
        if eh[k]*eh[k+1]<0: z.append(rr[k]-eh[k]*(rr[k+1]-rr[k])/(eh[k+1]-eh[k]))
    return z

ZETA=[14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073]
print("="*82)
print("Weil form v3 (parity-separated): is the ground state EVEN and SIMPLE? (Connes S6.6a)")
print("="*82)
for X in [13,30,60]:
    N=420; x,dx,M=build(X,N=N); Be,Bo=parity_blocks(M,N)
    Me=Be.T@M@Be; Mo=Bo.T@M@Bo
    we,Ve=np.linalg.eigh(Me); wo,Vo=np.linalg.eigh(Mo)
    # shift both sectors by the global min for comparison
    g0=min(we[0],wo[0])
    ze=fz(x,dx,Be,Ve[:,0],even=True); zo=fz(x,dx,Bo,Vo[:,0],even=False)
    ground_even = we[0]<wo[0]
    print(f"\n  X={X} (a={0.5*np.log(X):.3f}, primes<={X})")
    print(f"    EVEN  ground {we[0]-g0:+.5f}, gap to 2nd even = {we[1]-we[0]:.5f}")
    print(f"    ODD   ground {wo[0]-g0:+.5f}, gap to 2nd odd  = {wo[1]-wo[0]:.5f}")
    print(f"    GLOBAL GROUND STATE: {'EVEN' if ground_even else 'ODD'}  "
          f"(even-odd ground split = {wo[0]-we[0]:+.5f})")
    print(f"    even-ground Fourier zeros: {', '.join(f'{z:.3f}' for z in ze[:8])}")
    print(f"    zeta zeros:                {', '.join(f'{z:.3f}' for z in ZETA)}")
    if ze:
        # match count
        m=sum(1 for k,zz in enumerate(ZETA) if any(abs(zz-z)<0.2 for z in ze))
        print(f"    first even-zero {ze[0]:.3f} vs 14.135 -> |err|={abs(ze[0]-14.134725):.3f};"
              f"  zeta zeros matched (<0.2): {m}/{len(ZETA)}")
print("""
  READ: if the even ground sits below the odd ground (EVEN global ground), with a clean
  gap to the 2nd even state (SIMPLE within sector), and the even-ground Fourier zeros are
  the zeta zeros with NO spurious low zeros -> Connes S6.6(a) (simple+even) holds for the
  finite Weil form, verified. The even-odd split and the within-sector gap are the two
  numbers the program's order-3 chirality (c_2<0, L(1/2,chi_3)!=0) must keep strictly
  positive in the limit.""")
