"""
RIGOROUS domination: show Q = v^2 c_m - u w c_{m+2} > 0 at the actual prime window,
given b^2 > a e, for x large enough -- with EXPLICIT, uniform-enough control.

Setup: f monic degree d>=1. Window q0=x, q1=x+a, q2=x+a+b, q3=x+a+b+e, all primes,
2 <= a,b,e <= (gaps). We have exact:
  u=f(q1)-f(q0), v=f(q2)-f(q1), w=f(q3)-f(q2), c_m=f(q0), c_{m+2}=f(q2).

We want a clean sufficient inequality. Strategy: use the MEAN VALUE THEOREM with
monotone f' on [x, x+a+b+e] (f' eventually increasing & positive). Write:
  u = f(x+a)-f(x)         = a * f'(xi_u),  xi_u in (x, x+a)
  v = f(x+a+b)-f(x+a)     = b * f'(xi_v),  xi_v in (x+a, x+a+b)
  w = f(x+a+b+e)-f(x+a+b) = e * f'(xi_w),  xi_w in (x+a+b, x+a+b+e)
with xi_u < xi_v < xi_w.  Since f' is increasing (for x>=X1, as f'->+oo monotonic for monic),
  f'(xi_u) <= f'(xi_v) <= f'(xi_w).
Also c_m=f(x), c_{m+2}=f(x+a+b) >= f(x)=c_m, and c_{m+2}/c_m -> 1.

Then:
  v^2 c_m = b^2 f'(xi_v)^2 f(x)
  u w c_{m+2} = a e f'(xi_u) f'(xi_w) f(x+a+b)
So Q = v^2 c_m - u w c_{m+2}
     = b^2 f'(xi_v)^2 f(x) - a e f'(xi_u) f'(xi_w) f(x+a+b).
For Q>0 it SUFFICES:
  b^2 f'(xi_v)^2 f(x)  >  a e f'(xi_u) f'(xi_w) f(x+a+b).
Using f'(xi_u)<=f'(xi_v)<=f'(xi_w):  the worst case is f'(xi_u)=f'(xi_v) small ratio.
This is delicate because f'(xi_w)>=f'(xi_v). Hmm the ordering goes the WRONG way for a clean bound
(we'd want f'(xi_w)<=f'(xi_v)). So MVT-with-monotone-f' alone isn't enough; we need the
QUANTITATIVE closeness f'(xi_w)/f'(xi_v) -> 1.

Better: Taylor with explicit remainder. f'(xi)=f'(x)(1+O((a+b+e)/x)). Make this precise:
For monic f of degree d, on [x, x+W] with W=a+b+e, and x large,
  f'(t) = f'(x) (1 + r(t)), with |r(t)| <= K_f * (W/x)  for t in [x,x+W], x>=X2.
Then f'(xi_v)^2 / (f'(xi_u) f'(xi_w)) = (1+O(W/x)). Similarly f(x+a+b)/f(x)=1+O(W/x).
So Q>0 reduces to b^2 (1 - O(W/x)) > a e (1 + O(W/x)), i.e.
  b^2 - a e  >  O(W/x) (b^2 + a e).
Since b^2-ae >= 1 (integers, b^2>ae => b^2-ae>=1) ... actually b^2,ae integers so b^2>=ae+1.
And b<=W. So SUFFICIENT:  1 <= b^2-ae  and  C_f*(W/x)*(b^2+ae) < 1.
Since b^2+ae <= 2W^2 and we need C_f W^3 / x < 1 roughly. So if W = o(x^{1/3}) we win.

THE GAP W between the small-gap shoulders: by Maynard-Zhang the shoulders recur with
g<=246, and the excursion peak b is a prime gap, which is O(log^2 x) under nothing...
Actually unconditionally gaps are O(x^{0.525}) (BHP) and the excursion width W is at most
the distance between two consecutive g<=246 indices. We need W=o(x^{1/3}).

==> CLEANEST: don't fix the excursion. Use a SINGLE explicit recurring pattern whose
existence at large x is unconditional and has BOUNDED W. The bounded-gap theorem gives
infinitely many n with p_{n+1}-p_n <= 246. We need a LOCAL-MAX with bounded width.

Let me just NUMERICALLY validate the reduction Q>0 <= [b^2-ae > C_f (W/x)(b^2+ae)] and
measure the constant, to confirm the analytic claim is sound; the airtight unconditional
closure is argued separately (bounded clusters).
"""
from sympy import primerange, Integer, Rational
P=list(primerange(2,500000))
G=[P[i+1]-P[i] for i in range(len(P)-1)]

def Qval(window,f):
    q0,q1,q2,q3=window
    A,B,C,D=f(q0),f(q1),f(q2),f(q3)
    return (C-B)**2*A-(B-A)*(D-C)*C

# Collect last-argmax trigger windows
THR=8
small=[i for i in range(len(G)) if G[i]<=THR]
wins=[]
for k in range(len(small)-1):
    s,t=small[k],small[k+1]
    if t<=s+1: continue
    seg=list(range(s,t+1)); bmax=max(G[j] for j in seg)
    if bmax<=THR: continue
    pk=max(j for j in seg if G[j]==bmax)
    if 0<pk<len(G)-1:
        wins.append(pk)

# For each polynomial, check Q>0 on ALL sufficiently-far trigger windows and find first failure
import sys
def check(fname,f,dmax_prime=400000):
    fails=[]; oks=0
    for pk in wins:
        q=(P[pk-1],P[pk],P[pk+1],P[pk+2])
        if q[3]>dmax_prime: break
        if any(f(x)<=0 for x in q):  # admissibility on window
            continue
        Q=Qval(q,f)
        if Q>0: oks+=1
        else: fails.append((P[pk-1],(G[pk-1],G[pk],G[pk+1]),Q))
    return oks,fails

for fname,f,deg in [
    ("p",lambda p:p,1),
    ("p^2",lambda p:p**2,2),
    ("p^5",lambda p:p**5,5),
    ("p^8",lambda p:p**8,8),
    ("p^12",lambda p:p**12,12),
    ("p^20",lambda p:Integer(p)**20,20),
    ("p+10^6",lambda p:p+1000000,1),
    ("p^3-100p^2+1",lambda p:p**3-100*p**2+1,3),
]:
    oks,fails=check(fname,f)
    # find the LARGEST-prime failure (small-prime failures are expected/irrelevant)
    last_fail_prime = fails[-1][0] if fails else None
    print(f"f={fname:16s}: trigger-windows passing Q>0: {oks:5d}; failures: {len(fails):4d}; "
          f"largest failing prime: {last_fail_prime}")
    if fails and len(fails)<=6:
        for p0,g,Q in fails:
            print(f"        FAIL at window start prime {p0}, gaps {g}, Q={Q}")
print("\n(If failures are confined to SMALL primes and vanish beyond some X0(f), the asymptotic claim holds.)")
