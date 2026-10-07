"""
Weil quadratic form, BUILD v2 -- exact archimedean kernel. Held to the correctness check:
the minimal eigenvector's first Fourier zero must be 14.13 (Connes' first zeta zero).

Fixes vs v1 (which gave 3.56, FAILED):
  (1) EXACT archimedean kernel.  Omega_inf(r)=Re psi(1/4+ir/2)-log pi has inverse transform
        K_inf(u) = -sum_{n>=0} e^{-(2n+1/2)|u|} = -e^{-|u|/2}/(1-e^{-2|u|})   (u != 0),
      a -1/(2|u|) singularity + divergent diagonal self-energy (a CONSTANT -> shifts
      eigenvalues, not eigenvectors).  v1 used a crude r-cutoff+taper: wrong kernel.
  (2) MAIN term rank-2 (general phi): h(i/2)+h(-i/2) = 2(int phi e^{x/2})(int phi e^{-x/2})
      => kernel 2 cosh((x-y)/2), NOT the rank-1 cosh(x/2)cosh(y/2) of v1.

Weil quadratic form (positivity <=> RH):
  W(phi) = 2(int phi e^{x/2})(int phi e^{-x/2})              [main / poles]
         + (1/2pi) int |phihat|^2 Omega_inf(r) dr            [archimedean]  = int int phi phi K_inf
         - 2 sum_{n<=X} (Lambda(n)/sqrt n) (phi*phi)(log n)  [primes <= X]
phi even/general on [-a,a], a=(log X)/2 (symmetric [lambda^-1,lambda], primes<=X=lambda^2).

numpy + mpmath. No torch.
"""
import numpy as np

def prime_powers(X):
    sieve=np.ones(X+1,bool); sieve[:2]=False
    for i in range(2,int(X**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    out=[]
    for p in np.where(sieve)[0]:
        pe=int(p)
        while pe<=X:
            out.append((pe,float(np.log(p)))); pe*=int(p)
    return out

def K_inf(u):
    au=np.abs(u)
    out=np.where(au<1e-12, 0.0, -np.exp(-au/2)/(1-np.exp(-2*au)+1e-300))
    return out

def build(X, N=400):
    a=0.5*np.log(X); x=np.linspace(-a,a,N); dx=x[1]-x[0]
    D=x[:,None]-x[None,:]
    M_inf = K_inf(D)*dx*dx
    np.fill_diagonal(M_inf, 0.0)                 # uniform self-energy -> drop (const shift)
    M_main = 2*np.cosh(D/2)*dx*dx                # rank-2 main, general phi
    M_pr = np.zeros((N,N))
    for (n,logp) in prime_powers(X):
        t=np.log(n); w=logp/np.sqrt(n)
        xt=x-t
        for i in range(N):
            xp=xt[i]
            if xp<x[0] or xp>x[-1]: continue
            jf=(xp-x[0])/dx; j=int(np.floor(jf)); fr=jf-j
            if 0<=j<N-1:
                M_pr[i,j]   += -2*w*dx*(1-fr)
                M_pr[i,j+1] += -2*w*dx*fr
    M=M_inf+M_main+M_pr; M=0.5*(M+M.T)
    return x,dx,M

def fourier_zeros(x,dx,eta,par,rmax=40.0):
    rr=np.linspace(1.0,rmax,4000)
    if par<0: eh=np.array([(eta*np.sin(rv*x)).sum()*dx for rv in rr])
    else:     eh=np.array([(eta*np.cos(rv*x)).sum()*dx for rv in rr])
    z=[]
    for k in range(len(rr)-1):
        if eh[k]*eh[k+1]<0:
            z.append(rr[k]-eh[k]*(rr[k+1]-rr[k])/(eh[k+1]-eh[k]))
    return z

ZETA=[14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719]
print("="*80)
print("BUILD v2 correctness check: minimal-eigenvector Fourier zeros vs zeta zeros")
print("="*80)
for X in [13, 30]:
    x,dx,M=build(X,N=420); w,V=np.linalg.eigh(M)
    eta=V[:,0]; par=float(np.dot(eta,eta[::-1])/np.dot(eta,eta))
    z=fourier_zeros(x,dx,eta,par)
    print(f"\n  X={X} (a={0.5*np.log(X):.3f}, primes<={X}, N=420)")
    print(f"    ground-state parity overlap {par:+.3f} ({'EVEN' if par>0.5 else 'ODD' if par<-0.5 else 'mixed'})")
    print(f"    eigenvalue gaps lam_k-lam_0: {', '.join(f'{v:.4f}' for v in (w[1:5]-w[0]))}")
    print(f"    Fourier zeros: {', '.join(f'{zz:.3f}' for zz in z[:7])}")
    print(f"    zeta zeros:    {', '.join(f'{zz:.3f}' for zz in ZETA)}")
    if z: print(f"    FIRST-ZERO CHECK: {z[0]:.3f} vs 14.135  -> |err|={abs(z[0]-14.134725):.3f}")
