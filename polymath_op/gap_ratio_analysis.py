"""
Reduce the trigger Q(m)=v^2 c_m - u w c_{m+2} > 0 to prime-gap geometry.

For monic f of degree d, on the window primes q0=p_m,q1=p_{m+1},q2=p_{m+2},q3=p_{m+3}:
  c_l = f(q_l).
  u = f(q1)-f(q0),  v = f(q2)-f(q1),  w = f(q3)-f(q2).

KEY ASYMPTOTIC: as primes ->oo, c_{m+2}/c_m -> 1 (consecutive-prime ratio ->1, fixed deg).
Trigger ~  v^2 > u w * (c_{m+2}/c_m).  Since c_{m+2}/c_m -> 1, the *robust* trigger is
  v^2 > u w   with a little room.

Now v^2 > u*w is a statement about the local convexity/peakedness of l -> f(p_l).
For f increasing & convex on the window, by AM-GM-like reasoning we need the MIDDLE
forward-difference to dominate. This happens when the prime gap pattern has a LOCAL
PEAK at the middle: g1 = p_{m+2}-p_{m+1} is large while g0,g2 are small.

Let's QUANTIFY: define the discrete trigger margin
   T(m) := v^2 * c_m - u*w*c_{m+2}
and the *normalized* trigger  v^2/(u w) and (c_{m+2}/c_m), to see how much slack.
Tabulate for f(p)=p on the first universal trigger windows.
"""
from sympy import primerange, Integer, Rational, nsimplify

P=list(primerange(2,100))

def show(fname,f):
    print(f"\n=== f(p)={fname} ===")
    print(" m | window primes        | u    v    w   | v^2/(uw)   c_m+2/c_m | Q sign")
    for m in [1,2,3,4,5]:
        q=[P[m-1+k] for k in range(4)]
        c=[f(x) for x in q]
        u=c[1]-c[0]; v=c[2]-c[1]; w=c[3]-c[2]
        Q=v*v*c[0]-u*w*c[2]
        r1=Rational(v*v,u*w) if u*w!=0 else None
        r2=Rational(c[2],c[0])
        print(f" {m} | {str(tuple(q)):20s} | {u:4} {v:4} {w:4} | {str(r1):10s} {str(r2):8s} | {'POS(min<0)' if Q>0 else 'neg'}  Q={Q}")

show("p", lambda p:p)
show("p^2", lambda p:p**2)
show("p+5", lambda p:p+5)

# The point: at window primes (5,7,11,13): gaps in p are 2,4,2 -> u~,v~,w~ for f=p: u=2,v=4,w=2
# v^2/(uw)=16/4=4 >> c_{m+2}/c_m=11/5=2.2.  So 4>2.2 -> trigger. The "4-2-... gap peak".
print("\n--- The structural trigger: a prime-gap LOCAL PEAK g_mid >> g_left,g_right ---")
print("window (5,7,11,13): prime gaps (2,4,2). For f(p)=p, v^2/(uw)=16/4=4 > 11/5=2.2. TRIGGER.")
print("This pattern (small,large,small gap) recurs infinitely (e.g. 11,13,17,19; 23,29,31,...).")
