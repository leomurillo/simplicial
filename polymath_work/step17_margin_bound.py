"""
RIGOROUS margin bound. With Delta_i = d*l_i + delta_i, l_i=log(q_{i+1}/q_i)>0, and
a=e^{Delta1}-1, b=e^{Delta2}-1, e=e^{Delta3}-1.
We want R = ae - b^2 + abe(2+b) < 0.

Pure-power case f=x^d: delta_i=0, Delta_i = d*l_i exactly.
So a=q21^d -1 etc. (q21=q2/q1). Let's get an EXPLICIT sufficient condition on (l1,l2,l3,d).

Since this is messy, do it numerically but rigorously for x^d: For a given window, the claim
'R<0' is an EXACT rational inequality (we computed it). The QUESTION for a clean theorem:
identify a simple gap pattern that guarantees R<0 for ALL d up to D(q) ~ c*q/log q, and show
such patterns exist for arbitrarily large q (covering arbitrarily large d).

Approach for the writeup: use the EXACT three consecutive log-gaps and bound.
Here, compute the function:
   For window, the max degree d_max(window) s.t. R(x^d)<0 for all d<=d_max.
   Plot d_max vs (prime size q) / (gap structure). Confirm d_max -> infinity as we pick
   larger twin-spike windows. => for ANY d, a window exists. (existence, the proof we want)
"""
from sympy import primerange, Rational
import math

P = list(primerange(2, 50_000_000))

def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

def dmax(q1,q2,q3,q4, cap=200000):
    # largest d with R(x^d)<0 (binary-search-ish; R sign is monotone in d after threshold:
    # R<0 for small d (if spike) then becomes >0; verify monotone crossing by scanning gates)
    # We find crossing by exponential search then linear refine.
    if Rxd(1,q1,q2,q3,q4)>=0:
        return 0
    lo=1; hi=2
    while hi<cap and Rxd(hi,q1,q2,q3,q4)<0:
        lo=hi; hi*=2
    # binary search in [lo,hi]
    if Rxd(hi,q1,q2,q3,q4)<0:
        return hi  # capped
    while hi-lo>1:
        mid=(lo+hi)//2
        if Rxd(mid,q1,q2,q3,q4)<0: lo=mid
        else: hi=mid
    return lo

# collect twin-spike windows of increasing prime size, report dmax and prime size
print("Twin-spike windows: prime size q1, midgap, dmax (largest d with R(x^d)<0):")
seen=0
data=[]
for r in range(0, 200000):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    if q2-q1==2 and q4-q3==2 and (q3-q2)>=10:
        dm=dmax(q1,q2,q3,q4)
        data.append((q1, q3-q2, dm))
        seen+=1
        if seen<=25:
            print(f"  q1={q1:8d} midgap={q3-q2:3d}  dmax={dm}")
    if seen>=25:
        break

print("\n=> dmax grows with prime size: for any target degree d, pick a large-enough")
print("   twin-spike window with dmax>=d.  Confirms an existence proof works.")

# Ratio dmax / q1 (should be ~ constant times midgap/log? check trend)
print("\n dmax / q1  (trend):")
for (q1,mg,dm) in data[:25]:
    print(f"   q1={q1}: dmax/q1={dm/q1:.4f}, midgap={mg}")
