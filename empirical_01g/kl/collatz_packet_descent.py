"""Exact-integer packet quotient and descent diagnostics. No general termination claim."""
from pathlib import Path
import json


def valuation(n,p):
    assert n>0
    v=0
    while n%p==0:
        n//=p; v+=1
    return v


def odd_step(n):
    z=3*n+1
    return z >> valuation(z,2)


def bottom(n):
    assert n>0 and n%2
    t=valuation(n+1,3)
    return ((n+1)//3**t)*2**t-1


def packet_step(n):
    assert n>0 and n%2 and (n+1)%3
    M=valuation(n+1,2)
    q=(n+1)//2**M
    X=3**M*q
    b=valuation(X-1,2)
    z=(X-1)//2**b
    t=valuation(z+1,3)
    out=((z+1)//3**t)*2**t-1
    assert out==bottom(z)
    assert (out+1)*2**b*3**t == (X-1+2**b)*2**t
    if b%2:
        assert t==0
    elif 1+valuation(b//2,3)<M:
        assert t==1+valuation(b//2,3)
    return out,dict(M=M,q=q,b=b,t=t,exit=z)


def ordinary_descent(n,limit=10000):
    x=n
    for j in range(1,limit+1):
        x=odd_step(x)
        if x<n: return j
    return None


def packet_descent(n,limit=10000):
    x=n; path=[n]; replayed_odd_steps=0; expansions=0
    for j in range(1,limit+1):
        x,row=packet_step(x)
        replayed_odd_steps+=row['M']; expansions+=int(x>path[-1])
        path.append(x)
        if x<n:
            return dict(steps=j,path=path,replayed_odd_steps=replayed_odd_steps,expansions=expansions)
    return dict(steps=None,path=path)


def main():
    checks=0
    for n in range(1,20000,2):
        t=valuation(n+1,3)
        s=valuation(n+1,2)
        q=(n+1)//(2**s*3**t)
        root=bottom(n)
        assert root==2**(s+t)*q-1
        y=root
        for _ in range(t):
            assert valuation(3*y+1,2)==1
            y=odd_step(y)
        assert y==n
        if valuation(3*n+1,2)==1:
            assert bottom(odd_step(n))==root
        checks+=1
    examined=0; longest=dict(steps=0); expansions=0; unresolved=[]
    for n in range(3,200000,2):
        if (n+1)%3==0: continue
        out,data=packet_step(n)
        y=n
        for _ in range(data['M']): y=odd_step(y)
        assert y==data['exit'] and bottom(y)==out
        result=packet_descent(n)
        examined+=1; expansions+=int(out>n)
        if result['steps'] is None: unresolved.append(n)
        elif result['steps']>longest['steps']:
            longest=dict(start=n,steps=result['steps'],path=result['path'])
    examples=[]
    for n in (3,7,27,31,703,100003):
        if (n+1)%3==0:continue
        examples.append(dict(start=n,ordinary_odd_steps_to_descent=ordinary_descent(n),
                             packet_descent=packet_descent(n)))
    assert packet_step(7)[0]==13 and packet_step(27)[0]==31
    expanding_runs=0
    for modulus in (1,2,3,5,7,16,81,100):
        for length in range(1,41):
            start=24*modulus*8**length-5
            current=start
            for j in range(length):
                nxt,data=packet_step(current)
                expected=24*modulus*9**(j+1)*8**(length-j-1)-5
                assert data['M']==2 and data['b']==1 and data['t']==0
                assert nxt==expected and nxt>current
                assert (nxt-current)%modulus==0
                assert valuation(nxt+1,2)==2
                current=nxt
            expanding_runs+=1
    output=dict(status='Exact finite verification, not a proof of universal descent',
                packet_membership_checks=checks,canonical_starts_below_200000=examined,
                expanding_first_packet_moves=expansions,unresolved=unresolved,
                exact_expanding_packet_runs=expanding_runs,
                longest_observed_descent=longest,examples=examples,
                linear_rank_obstruction=['7 -> 13: 8 -> 14 requires w7 < 2*w2',
                                         '27 -> 31: 28 -> 32 requires w7 > 3*w2'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2))
    print(json.dumps({key:value for key,value in output.items() if key not in ('examples','longest_observed_descent')}))
    print(json.dumps(dict(longest_start=longest.get('start'),longest_steps=longest['steps'],
                         examples=[dict(n=e['start'],ordinary=e['ordinary_odd_steps_to_descent'],
                                        packet=e['packet_descent']['steps']) for e in examples])))


if __name__=='__main__':main()
