"""Exploratory block transfer tests, not rigorous norm enclosures.

The norm ratios are attained test-vector ratios, not estimates claimed to be
the exact operator norm. Truncated Neumann tails are <= steps*2^(-terms)
in exact arithmetic; float64 rounding is not enclosed.
"""
import json
from pathlib import Path
import numpy as np
from syracuse_phase_energy_probe import lift_law, top

W=np.exp(2j*np.pi/3)


def transfer_batch(n,z,terms=64):
    size=3**(n-1); j=np.arange(size)
    tau=((2*j-1)//3)%(size//3)
    twist=(W**(2*j//size))[:,None]
    term=np.where((j%3==2)[:,None],twist*np.conj(z[tau]),0)
    out=np.zeros_like(term)
    for a in range(terms):
        out+=2.**(-a-1)*term
        term=twist*np.conj(term[(2*j)%size])
    return out


def main():
    mu=np.array([1.]); fields={}
    for n in range(1,10):
        mu=lift_law(mu); fields[n]=top(mu)
    rows=[]
    for start in range(3,7):
        size=3**(start-1)
        contexts=sorted(set([1,2,4,5,size-2,size-1]))
        angles=np.arange(12)*np.pi/12
        probes=[(j,float(angle)) for j in contexts for angle in angles]
        z=np.zeros((size,len(probes)),dtype=complex)
        for c,(j,angle) in enumerate(probes): z[j,c]=np.exp(1j*angle)
        actual=fields[start][:,None]/np.abs(fields[start]).sum()
        z=np.concatenate((z,actual),axis=1)
        for steps in range(1,min(4,10-start)):
            z=transfer_batch(start+steps,z)
            ratios=np.abs(z).sum(axis=0)
            best=int(np.argmax(ratios[:-1]))
            expected=np.abs(fields[start+steps]).sum()/np.abs(fields[start]).sum()
            assert abs(ratios[-1]-expected)<2e-12
            row=dict(start=start,steps=steps,end=start+steps,
                     largest_test_ratio=float(ratios[best]),
                     best_context=probes[best][0],best_phase=probes[best][1],
                     actual_syracuse_ratio=float(ratios[-1]),
                     exact_arithmetic_series_tail_bound=steps*2.**(-64))
            rows.append(row); print(json.dumps(row),flush=True)
    # Measured dyadic block energies on already-computed actual fields.
    energies=[]
    for N in (2,4):
        # kappa indices N,...,2N-1; input field is N-1.
        previous=float(np.abs(fields[N-1]).sum()); final=float(np.abs(fields[2*N-1]).sum())
        energies.append(dict(N=N,actual_block_ratio=final/previous,
                             log_contraction=float(np.log(previous/final))))
    Path(__file__).with_suffix('.json').write_text(json.dumps({
        'status':'float64 attained test ratios, no rigorous numerical operator norm claim',
        'blocks':rows,'actual_dyadic_blocks':energies},indent=2))


if __name__=='__main__': main()
