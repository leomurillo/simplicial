"""Independent phase-energy and twisted-transfer probes; float64 exploration.

No asymptotic certification. Existing Syracuse checker is not imported or changed.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

W = np.exp(2j*np.pi/3)


def lift_law(previous):
    m = 3*len(previous); period = 2*(m//3)
    orbit = np.empty(period,dtype=np.int64); orbit[0] = 1
    for j in range(1,period): orbit[j] = 2*orbit[j-1] % m
    forcing = np.zeros(m); forcing[1+3*np.arange(m//3)] = previous
    f = forcing[orbit]
    # Exact geometric-resolvent formula evaluated in float64. Neglected
    # terms underflow naturally; this implementation is not exact arithmetic.
    aa = np.arange(1,period+1)
    out = np.empty(period)
    out[-1] = np.sum(np.exp2(-aa.astype(float))*f[(period-1+aa)%period])/(1-2.**(-period))
    for j in range(period-2,-1,-1): out[j] = (f[j+1]+out[j+1])/2
    mu = np.zeros(m); mu[orbit] = out
    return mu


def top(mu):
    tri = mu.reshape(3,-1)
    return tri[0]+W*tri[1]+W**2*tri[2]


def transfer(n,z,iterations=160):
    k = 3**(n-1); j = np.arange(k)
    tau = ((2*j-1)//3) % (k//3)
    twist = W**(2*j//k)
    term = np.where(j%3==2,twist*np.conj(z[tau]),0)
    out = np.zeros(k,dtype=complex)
    for a in range(iterations):
        out += 2.**(-a-1)*term
        term = twist*np.conj(term[(2*j)%k])
    return out


def exact_recursion(max_n=5):
    """Coefficients in Q(omega), represented as u+v*omega, omega^2=-1-omega."""
    def conjugate(p): return (p[0]-p[1],-p[1])
    def twist(p,c): return p if c==0 else (-p[1],p[0]-p[1])
    previous=[F(1)]; previous_z=None; checks=0
    for n in range(1,max_n+1):
        m=3**n; period=2*3**(n-1); orbit=[1]
        for _ in range(1,period): orbit.append(2*orbit[-1]%m)
        forcing=[F(0)]*m
        for j,value in enumerate(previous): forcing[1+3*j]=value
        f=[forcing[r] for r in orbit]; g=[F(0)]*period
        g[-1]=sum((f[(period-1+a)%period]/2**a for a in range(1,period+1)),F(0))/(1-F(1,2**period))
        for j in range(period-2,-1,-1): g[j]=(f[j+1]+g[j+1])/2
        mu=[F(0)]*m
        for r,value in zip(orbit,g): mu[r]=value
        assert sum(mu)==1
        k=m//3; z=[(mu[j]-mu[j+2*k],mu[j+k]-mu[j+2*k]) for j in range(k)]
        if previous_z is not None:
            for j in range(k):
                a=conjugate(z[2*j%k]); b=(F(0),F(0))
                if j%3==2: b=conjugate(previous_z[((2*j-1)//3)%(k//3)])
                rhs=twist(((a[0]+b[0])/2,(a[1]+b[1])/2),int(2*j>=k))
                assert z[j]==rhs
                checks+=1
        previous=mu; previous_z=z
    return dict(max_n=max_n,contexts_checked=checks,exact_field='Q(omega)',all_pass=True)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--max-n',type=int,default=12)
    args = parser.parse_args(); mu=np.array([1.]); oldz=None; rows=[]
    for n in range(1,args.max_n+1):
        mu=lift_law(mu); z=top(mu); s=float(np.abs(z).sum())
        if oldz is not None:
            k=len(z); j=np.arange(k); odd=j%3==2
            tau=((2*j-1)//3)%(k//3)
            a=z[(2*j[odd])%k]; b=oldz[tau[odd]]
            aa,bb=np.abs(a),np.abs(b)
            total=aa+bb; w=np.divide(aa*bb,total,out=np.zeros_like(aa),where=total>0)
            product=aa*bb
            cosine=np.divide(np.real(a*np.conj(b)),product,out=np.ones_like(aa),where=product>0)
            cosine=np.clip(cosine,-1,1)
            energy=float(np.sum(w*(1-cosine)))
            # Stable triangle-deficit expression.
            deficit=float(np.sum(np.divide(2*product*(1-cosine),total+np.abs(a+b),out=np.zeros_like(aa),where=total>0)))
            previous=float(np.abs(oldz).sum()); kappa=(previous-s)/previous
            overlap=float(w.sum()/previous)
            amplitude_ratio=float(aa.sum()/previous)
            fidelity_squared=float(np.sum(np.sqrt(product))**2/(aa.sum()*bb.sum()))
            p=aa/aa.sum(); q=bb/bb.sum(); qlive=q>0
            reverse_kl=float(np.sum(q[qlive]*np.log(q[qlive]/p[qlive]))) if np.all(p[qlive]>0) else None
            overlap_lower=amplitude_ratio/(1+amplitude_ratio)*fidelity_squared
            assert overlap+1e-13 >= overlap_lower
            tri=mu.reshape(3,-1); loss=float(np.sum(tri.sum(0)-3*tri.min(0)))
            row=dict(n=n,S=s,kappa=kappa,n_kappa=n*kappa,
                     normalized_energy=energy/previous,overlap=overlap,
                     amplitude_ratio=amplitude_ratio,fidelity_squared=fidelity_squared,
                     relative_entropy_q_to_p=reverse_kl,
                     overlap_fidelity_lower_bound=overlap_lower,
                     weighted_mean_one_minus_cosine=energy/w.sum(),
                     rms_chord=float(np.sqrt(2*energy/w.sum())),
                     n_times_weighted_angle_energy=n*energy/w.sum(),
                     triangle_identity_error=abs(deficit-(previous-s)),
                     loss_over_S=loss/s,
                     recursion_error=float(np.max(np.abs(z-(W**(2*j//k))*(np.conj(z[(2*j)%k])+np.where(odd,np.conj(oldz[tau]),0))/2))))
            assert energy <= deficit+1e-13 and deficit <= 2*energy+1e-13
            assert 1-1e-12 <= loss/s <= 2+1e-12
            assert row['triangle_identity_error'] < 1e-12
            rows.append(row); print(json.dumps(row),flush=True)
        oldz=z
    tests=[]
    for n in range(2,7):
        dim=3**(n-2); z=np.zeros(dim,dtype=complex); z[0 if n==2 else 1]=np.exp(.37j)
        out=transfer(n,z)
        L=2*3**(n-2); q=2.**(-L)
        predicted=(1-q)/np.sqrt(1+q+q*q)
        observed=float(np.abs(out).sum())
        assert abs(predicted-observed)<2e-14
        tests.append(dict(n=n,period=L,contraction_predicted=predicted,contraction_observed=observed))
    exact=exact_recursion()
    print(json.dumps({'exact_recursion':exact}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'phase and norm data are floating-point exploration; separate exact rational recursion check included','levels':rows,'single_context_operator_norm':tests,'exact_recursion':exact},indent=2))


if __name__=='__main__': main()
