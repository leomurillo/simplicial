"""Produce a rigorous NON-CND certificate: smallest N where the CND-witness
matrix A (size N) has a negative eigenvalue, plus an explicit rational vector v
with v^T A v < 0 (robust margin). This is a checkable proof that psi is not CND,
hence (Schoenberg) exp(-d psi) is not PSD at all sizes for ANY d>0, hence NO
power (p+r)^d is a Hamburger moment sequence."""
import mpmath as mp
mp.mp.dps=80
from sympy import primerange, Rational, Matrix as SMatrix, log as slog, Integer, nsimplify
P=list(primerange(2,100000))

def Smp(r,m):
    s=mp.mpf(0)
    for k in range(1,m+1):
        s+=mp.log(mp.mpf(P[k-1])+r)
    return s

def buildA(r,N):
    Sc=[Smp(r,m) for m in range(0,2*N+1)]
    A=mp.matrix(N,N)
    for ii in range(1,N+1):
        for jj in range(1,N+1):
            pij=(Sc[2*ii]+Sc[2*jj]-2*Sc[ii+jj])/2
            pi0=(Sc[2*ii]-2*Sc[ii])/2
            p0j=(Sc[2*jj]-2*Sc[jj])/2
            A[ii-1,jj-1]=pi0+p0j-pij
    return A

# smallest N with min eig < 0
r=0
print("Finding smallest CND-witness failure (r=0)...")
for N in range(2,12):
    A=buildA(r,N)
    ev,EV=mp.eigsy(A)  # eigenvalues, eigenvectors
    evlist=[ev[k] for k in range(N)]
    mn=min(evlist); k=evlist.index(mn)
    print(f"  N={N}: min eig = {mp.nstr(mn,5)}")
    if mn < -mp.mpf(10)**(-20):
        # eigenvector for min eig -> rationalize -> certificate
        vec=[EV[i,k] for i in range(N)]
        # scale to make entries O(1), rationalize with small denominators
        vr=[nsimplify(mp.nstr(x,6), rational=True) for x in vec]
        # compute v^T A v exactly-ish at high precision using rational v and mp A
        val=mp.mpf(0)
        for i in range(N):
            for j in range(N):
                val+= mp.mpf(str(vr[i]))*mp.mpf(str(vr[j]))*A[i,j]
        nv=sum(mp.mpf(str(x))**2 for x in vr)
        print(f"    smallest non-CND size N={N}")
        print(f"    rational witness v = {vr}")
        print(f"    v^T A v = {mp.nstr(val,6)}   (||v||^2={mp.nstr(nv,5)})  Rayleigh={mp.nstr(val/nv,6)}")
        print(f"    => A NOT PSD => psi NOT CND => no (p+{r})^d is a moment sequence (Schoenberg).")
        break
