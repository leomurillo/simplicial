"""Independent exact certificate checker; standard library only."""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json


def counts(n,k):
    binary=format(n,'b')
    text='^'*(k-1)+binary+'$'*(k-1)
    return Counter(text[i:i+k] for i in range(len(text)-k+1))


def main():
    records=json.loads(Path(__file__).with_name('binary_pattern_rank_probe.json').read_text())
    checked=0
    for record in records:
        k=record['window']
        aggregate=defaultdict(Fraction)
        total=Fraction(0)
        for row in record['exact_certificate']:
            n=row['start']; end=row['end']
            assert n>0 and n%2
            word={'A':(1,),'B':(2,1,1)}[row['block']]
            x=n
            for a in word:
                t=3*x+1
                assert t%2**a==0 and (t//2**a)%2==1
                x=t//2**a
            assert x==end
            weight=Fraction(row['numerator'],row['denominator'])
            assert weight>0
            total+=weight
            before=counts(n,k); after=counts(end,k)
            for key in before.keys()|after.keys():
                aggregate[key]+=weight*(before[key]-after[key])
            checked+=1
        assert total>0
        for key,value in aggregate.items():
            if '^' in key or '$' in key:
                assert value==0, (k,key,value)
            else:
                assert value<=0, (k,key,value)
    result=dict(status='All exact certificates passed',windows=[r['window'] for r in records],
                weighted_transition_checks=checked,
                scope='No strictly decreasing additive binary-window rank with nonnegative interior weights and arbitrary boundary weights, for each listed window.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
