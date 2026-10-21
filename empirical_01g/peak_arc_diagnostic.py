"""Unsampled peak-cohort diagnostics and sampling comparison."""
from collections import Counter
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    N=1_000_000
    peaks=[0]*(N+1);peaks[1]=1
    for n in range(2,N+1):
        z=n;high=n;steps=0
        while z>=n:
            z=3*z+1 if z&1 else z//2
            high=max(high,z);steps+=1
            if steps>=100000:raise RuntimeError(n)
        peaks[n]=max(high,peaks[z])
    ns=np.arange(2,N+1)
    ps=np.array(peaks[2:],dtype=np.int64)
    ys=np.log(ps)/np.log(ns)
    old=(ns<=2000)|(ns%101==0)
    cohort=ns[ps==9232]
    counts=Counter(peaks[2:])
    top=counts.most_common(12)
    # Every nontrivial global peak has an odd predecessor and must be 4 mod 12.
    assert all(p==n or p%12==4 for n,p in enumerate(peaks[2:],2))
    report=dict(limit=N,old_sampling='all n<=2000; thereafter multiples of 101 only',
                old_plot_count=int(sum(old)),full_plot_count=len(ns),
                cohort_9232=dict(count=len(cohort),min=int(cohort.min()),max=int(cohort.max()),
                                 odd_count=int(sum(cohort%2==1)),max_odd=int(cohort[cohort%2==1].max()),
                                 old_plot_count=int(sum(old & (ps==9232)))),
                common_peaks=[dict(peak=p,count=c,min_seed=next(n for n in range(2,N+1) if peaks[n]==p)) for p,c in top],
                band_counts=[dict(lo=lo,hi=hi,full=int(sum((ns>=lo)&(ns<=hi))),
                                  old=int(sum((ns>=lo)&(ns<=hi)&old))) for lo,hi in [(1000,2000),(2001,10000),(10001,100000)]])
    out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained')
    ax=axes[0,0];ax.scatter(ns[old],ys[old],s=3,alpha=.3)
    ax.set_title('Original sampling: density changes at 2,000')
    ax.axvline(2000,color='#c05030',ls='--');ax.set_xscale('log');ax.set_ylabel('log(peak) / log(n)')
    ax=axes[0,1];ax.scatter(ns,ys,s=.4,alpha=.14,rasterized=True)
    ax.set_title('All 999,999 starts: no omitted integers')
    ax.axvline(2000,color='#c05030',ls='--');ax.set_xscale('log')
    ax=axes[1,0]
    cut=ns<=12000
    ax.scatter(ns[cut],ys[cut],s=2,color='#b5bdc5',alpha=.25)
    for p,color in [(9232,'#c05030'),(250504,'#386a9b'),(190996,'#5f8037'),(1276936,'#87539a')]:
        mask=cut&(ps==p)
        ax.scatter(ns[mask],ys[mask],s=7,color=color,label=f'peak = {p:,}')
        if sum(mask):
            grid=np.geomspace(ns[mask].min(),min(p,12000),300)
            ax.plot(grid,np.log(p)/np.log(grid),color=color,lw=.8,alpha=.5)
    ax.set_xscale('log');ax.set_title('Exact shared-peak cohorts (all starts ≤ 12,000)')
    ax.set_ylabel('log(peak) / log(n)');ax.legend(fontsize=8)
    ax=axes[1,1]
    ax.scatter(ns[cut],np.log10(ps[cut]),s=2,alpha=.25,color='#527ea6')
    mask=cut&(ps==9232);ax.scatter(ns[mask],np.log10(ps[mask]),s=6,color='#c05030')
    ax.set_xscale('log');ax.set_ylabel('log10(peak)');ax.set_title('Remove division by log(n): arcs become horizontal')
    for ax in axes.flat:
        ax.set_xlabel('Starting integer n');ax.grid(alpha=.15)
    fig.savefig(out.with_suffix('.png'),dpi=150)


if __name__=='__main__':main()
