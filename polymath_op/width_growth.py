"""
Settle the domination-existence rigor: among trigger windows (b^2>ae), how small can the
width W=a+b+e be at large primes? We need infinitely many trigger windows with W small enough
that (**) b^2>ae(1+W/x)^{3d} holds at the window's own x, for each fixed d.

(**) holds  <=>  x > W / ((b^2/ae)^{1/(3d)} - 1).
For the tightest trigger (2,4,2): b^2/ae=4, so need x > W/(4^{1/(3d)}-1).
  4^{1/(3d)}-1 ~ ln4/(3d) for large d. So need x > W*3d/ln4 ~ 2.16 d W.
So for pattern (2,4,2), domination holds once x > ~2.16 d * 8 = ~17 d.  TINY threshold.
=> If pattern (2,4,2) [primes x,x+2,x+6,x+8] occurs at some prime x>17d, DONE for degree d.
   But (2,4,2)-quadruples at arbitrarily large x is the prime-quadruplet conjecture (OPEN!).

So we must NOT rely on a fixed bounded pattern. Instead: show infinitely many trigger windows
with W = o(x^{1/(3d)})-ish, i.e. W grows slower than any power. Average gap ~ log x, and
trigger windows are a POSITIVE FRACTION (we saw ~36000 in last decade). Their widths:
measure max W among trigger windows in the last decade vs x. If W=O(log^2 x) (Cramer-ish) or
even O(x^{0.2}), then x>W*const*d holds for all large x. Let's MEASURE.
"""
from sympy import primerange, Integer
import math
P=list(primerange(2,2000000)); NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]

# trigger windows: b^2>ae. Record (x, W). Look at distribution of W and the RATIO x/W.
# For the proof we want: infinitely many trigger windows with x/W -> infinity (so (**) eventually holds).
# Equivalently min over trigger windows in [X,2X] of (x/W) -> infinity? No -- we want SUP of x/W large,
# i.e. SOME trigger window with x/W huge. Since smallest W (=8 for (2,4,2)-like, but also (2,6,4) W=12 etc)
# trigger windows have BOUNDED W while x->oo IF small-W triggers recur. Check recurrence of small-W triggers.
from collections import defaultdict
buckets=defaultdict(int)   # W -> count of trigger windows
maxx_for_W=defaultdict(int)
for i in range(NP-3):
    a,b,e=G[i],G[i+1],G[i+2]
    if b*b>a*e:
        W=a+b+e
        buckets[W]+=1
        maxx_for_W[W]=max(maxx_for_W[W],P[i])
print("Trigger-window width W : count : largest prime x carrying such a trigger window")
for W in sorted(buckets)[:20]:
    print(f"  W={W:4d} : count={buckets[W]:6d} : largest x={maxx_for_W[W]}")

# The decisive quantity for the proof: for each fixed small W0, do trigger windows of width<=W0
# occur at arbitrarily large x? Report largest x with W<=12, <=16, <=20, <=30.
for W0 in [8,10,12,14,16,18,20,24,30,40]:
    mx=max((maxx_for_W[W] for W in buckets if W<=W0), default=0)
    cnt=sum(buckets[W] for W in buckets if W<=W0)
    # count in last decade
    print(f"  trigger windows with W<= {W0:3d}: total {cnt:7d}, largest prime x = {mx}")
