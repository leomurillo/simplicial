"""Peak exponent log(P(n))/log(n), standard Collatz, finite census."""
from decimal import Decimal, localcontext
from pathlib import Path
import heapq
import json
import math


def main():
    limit = 1_000_000
    peaks = [0]*(limit+1)
    peaks[1] = 1
    top = []
    records = []
    best = 0.0
    sample = []
    selected = []
    for n in range(2, limit+1):
        z, high, steps = n, n, 0
        while z >= n:
            z = 3*z+1 if z & 1 else z//2
            high = max(high, z)
            steps += 1
            if steps >= 100000:
                raise RuntimeError(('Descent cap reached', n))
        peaks[n] = max(high, peaks[z])
        exponent = math.log(peaks[n])/math.log(n)
        item = (exponent, n, peaks[n])
        if len(top)<10:
            heapq.heappush(top,item)
        elif item>top[0]:
            heapq.heapreplace(top,item)
        if exponent>best:
            best=exponent
            records.append(dict(n=n,peak=peaks[n],exponent=exponent))
        if n in (3,7,15,27,31,703,1819,159487):
            selected.append(dict(n=n,peak=peaks[n],exponent=exponent))
        if n<=2000 or n%101==0:
            sample.append((n,exponent))
    with localcontext() as ctx:
        ctx.prec=60
        finalists=[dict(n=n,peak=p,exponent_60_digits=str(Decimal(p).ln()/Decimal(n).ln()))
                   for _,n,p in sorted(top,reverse=True)]
    out=Path(__file__).with_suffix('.json')
    result=dict(limit=limit,map='standard',peak_arithmetic='exact integers',
                ranking='double precision scan; top ten recomputed with 60-digit Decimal logarithms',
                records=records,selected=selected,top_ten=finalists)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots(figsize=(10,4.5),layout='constrained')
        ax.scatter([x for x,y in sample],[y for x,y in sample],s=4,alpha=.23,color='#527ea6')
        ax.plot([r['n'] for r in records]+[limit], [r['exponent'] for r in records]+[best],
                drawstyle='steps-post',color='#c05030',label='Running maximum (full scan)')
        ax.scatter([27],[best],color='black',zorder=5)
        ax.annotate('27: 2.770292...', (27,best),xytext=(12,-22),textcoords='offset points')
        ax.set_xscale('log'); ax.set_xlabel('Starting integer n');ax.set_ylabel('log(peak) / log(n)')
        ax.set_title('Peak as a power of the starting value\nStandard Collatz: 2 ≤ n ≤ 1,000,000; points subsampled')
        ax.grid(alpha=.15);ax.legend(loc='lower left')
        fig.savefig(out.with_suffix('.png'),dpi=160)
    except ImportError:
        pass


if __name__=='__main__':
    main()
