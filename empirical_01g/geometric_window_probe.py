"""Finite checks for the prime-crystal window geometry. Not an asymptotic proof."""
from pathlib import Path
import json
import numpy as np


def sieve_statistics(limit):
    sieve=np.ones(limit+1,dtype=bool); sieve[:2]=False
    for p in range(2,int(limit**.5)+1):
        if sieve[p]:sieve[p*p::p]=False
    primes=np.flatnonzero(sieve)
    omega=np.zeros(limit+1,dtype=np.int32)
    Q=np.zeros(limit+1,dtype=np.int32)
    for p0 in primes:
        p=int(p0); power=p; a=1
        while power<=limit:
            omega[power::power]+=1
            Q[power::power]+=2*a-1
            power*=p; a+=1
    return primes,omega,Q


def main():
    primes,omega,Q=sieve_statistics(2000100)
    rng=np.random.default_rng(20261017)
    records=[]; checks=0
    for X in (1000,10000,100000,1000000):
        L=np.log(np.log(X))
        n=np.arange(X,2*X,dtype=np.int64)
        stretch=(omega[n+1]-omega[n])**2 > Q[n]+Q[n+1]
        # Consecutive supports are disjoint; distance-two overlap uses only 2.
        v2n=np.zeros(len(n),dtype=np.int32)
        v2n2=np.zeros(len(n),dtype=np.int32)
        power=2
        while power<=2*X+2:
            v2n+=(n%power==0); v2n2+=((n+2)%power==0)
            power*=2
        overlap=v2n*v2n2
        frame=int(np.searchsorted(primes,2*X+64,side='right'))
        left=omega[n+1]-omega[n]
        right=omega[n+2]-omega[n+1]
        dot=-frame*(Q[n+1]+overlap)-left*right
        norm1=frame*(Q[n]+Q[n+1])-left**2
        norm2=frame*(Q[n+1]+Q[n+2])-right**2
        angle=np.arccos(np.clip(dot/np.sqrt(norm1.astype(float)*norm2),-1,1))
        windows=[]
        for m in (2,4,8,16,32):
            errors=[]; rayleigh=[]
            for start in rng.integers(X,2*X,size=60):
                ns=np.arange(start,start+m,dtype=np.int64)
                low=[]
                for p0 in primes[primes<=m]:
                    p=int(p0); a=np.zeros(m,dtype=np.int64); power=p
                    while power<=int(ns[-1]):
                        a+=(ns%power==0); power*=p
                    low.append(a)
                V=np.array(low,dtype=np.int64).T
                high=Q[ns]-np.sum(V*V,axis=1)
                assert np.all(high>=0)
                G=V@V.T+np.diag(high)
                # Independently reconstruct each off-diagonal from gcd support.
                for i in range(m):
                    for j in range(i):
                        common=int(np.gcd(ns[i],ns[j])); dot_exact=0
                        for p0 in primes[primes<=m]:
                            p=int(p0)
                            if common%p:continue
                            a=int(ns[i]); b=int(ns[j]); va=vb=0
                            while a%p==0:a//=p;va+=1
                            while b%p==0:b//=p;vb+=1
                            dot_exact+=va*vb
                        assert G[i,j]==dot_exact
                mass=omega[ns].astype(np.int64)
                GM=(frame*G-np.outer(mass,mass))/(frame-1)
                H=np.eye(m)-np.ones((m,m))/m
                errors.append(float(np.max(np.abs(np.linalg.eigvalsh(H@GM@H/L-H)))))
                even=(ns%2==0); e=int(even.sum()); o=m-e
                u=np.where(even,np.sqrt(o/(e*m)),-np.sqrt(e/(o*m)))
                v2=V[:,0]
                assert (u@v2)**2+1e-10>=e*o/m
                bound=(u*u)@high+e*o/m
                assert u@G@u+1e-8>=bound
                rayleigh.append(float(u@GM@u/L))
                checks+=1
            windows.append(dict(m=m,mean_centered_operator_error=float(np.mean(errors)),
                                mean_parity_rayleigh=float(np.mean(rayleigh))))
        records.append(dict(X=X,loglogX=float(L),stretch_fraction=float(np.mean(stretch)),
                            mean_turn_degrees=float(np.mean(angle)*180/np.pi),windows=windows))
    ns=np.arange(1000000,1065536,dtype=np.int64)
    columns=[]
    for p0 in primes[:8]:
        p=int(p0); a=np.zeros(len(ns),dtype=np.int64); power=p
        while power<=int(ns[-1]):
            a+=(ns%power==0); power*=p
        columns.append(a)
    V=np.array(columns,dtype=np.int64).T
    masses=V.sum(axis=0)
    covariance_numerator=len(ns)*(V.T@V)-np.outer(masses,masses)
    covariance=covariance_numerator.astype(float)/len(ns)**2
    target=np.array([int(p)/(int(p)-1)**2 for p in primes[:8]])
    covariance_check=dict(window_start=1000000,window_length=len(ns),
                          primes=[int(p) for p in primes[:8]],
                          variances=np.diag(covariance).tolist(),target_variances=target.tolist(),
                          maximum_entry_error=float(np.max(np.abs(covariance-np.diag(target)))))
    result=dict(status='Finite identity checks; asymptotic assertions require the written proofs',
                exact_decomposition_and_parity_checks=checks,records=records,
                fixed_prime_covariance_check=covariance_check)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(checks=checks,summary=[{k:r[k] for k in ('X','stretch_fraction','mean_turn_degrees')} for r in records]),indent=2))


if __name__=='__main__':main()
