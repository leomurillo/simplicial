"""DECISIVE theoretical test: is the kernel psi CND?
psi(i,j) = (1/2)(S_{2i}+S_{2j}-2 S_{i+j}),  S_m = sum_{k<=m} log(p_k + r).
b_n=(prod (p_k+r))^d  =>  scaled Hankel = exp(-d*psi) (PSD-equivalent).
Schoenberg: exp(-t psi) PSD for ALL t>0  <=>  psi is conditionally neg. def. (CND),
i.e. the matrix  G(i,j) = -[psi(i,j) - psi(i,0) - psi(0,j) + psi(0,0)]  is PSD
(equivalently A(i,j)= psi(i,0)+psi(0,j)-psi(i,j) is PSD for i,j>=1; psi(0,0)=0).

If psi is NOT CND  ->  for every d, exp(-d psi) eventually has a negative eigenvalue
  => NO power p^d is a moment sequence (theorem TRUE for whole power family).
If psi IS CND      ->  exp(-d psi) is PSD for all sizes for every d
  => p^d IS a moment sequence for every d (COUNTEREXAMPLE)."""
import mpmath as mp
mp.mp.dps=60
from sympy import primerange
P=list(primerange(2,100000))

def S(r, m):
    s=mp.mpf(0)
    for k in range(1,m+1):
        s+=mp.log(mp.mpf(P[k-1])+r)
    return s

def psi(r, i, j, Scache):
    return (Scache[2*i]+Scache[2*j]-2*Scache[i+j])/2

def is_cnd(r, N):
    """Build A(i,j)=psi(i,0)+psi(0,j)-psi(i,j) for i,j in 1..N, check PSD (min eig>=0).
    psi(i,0)=(S_{2i}+S_0-2 S_i)/2=(S_{2i}-2S_i)/2 since S_0=0. psi(0,0)=0."""
    Scache=[S(r,m) for m in range(0,2*N+1)]
    A=mp.matrix(N,N)
    for ii in range(1,N+1):
        for jj in range(1,N+1):
            pij=psi(r,ii,jj,Scache)
            pi0=(Scache[2*ii]-2*Scache[ii])/2
            p0j=(Scache[2*jj]-2*Scache[jj])/2
            A[ii-1,jj-1]=pi0+p0j-pij
    ev=mp.eigsy(A,eigvals_only=True)
    return min(ev), max(ev)

for r in [0,-1,1]:
    for N in [6,10,14,18,22]:
        mn,mx=is_cnd(r,N)
        verdict = "CND-ok-sofar" if mn >= -mp.mpf(10)**(-30) else "NOT CND (min eig<0)"
        print(f"r={r} N={N}: A min eig={mp.nstr(mn,4)} max={mp.nstr(mx,4)}  -> {verdict}", flush=True)
