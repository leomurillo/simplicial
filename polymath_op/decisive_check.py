"""
DECISIVE: for each monic f of degree d, scan ALL consecutive-prime 4-windows up to a large
bound and verify that BEYOND a finite X0(f), there are still trigger windows where Q>0 holds.
Equivalently: count windows with the WEAK trigger (b^2>ae) AND domination, far out.

Crucially we use the EXACT integer Q (no float), so this is rigorous evidence.
We report, for each f:
  - the largest prime up to which we scanned,
  - how many windows in the LAST DECADE [X/2, X] have Q>0 (must be many -> persists to infinity),
  - the single largest-prime window with Q>0 (the 'witness' principal minor).
"""
from sympy import primerange, Integer
P=list(primerange(2,2000000))   # ~148933 primes
NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]
print(f"primes available: {NP}, up to {P[-1]}")

def Qint(i,f):
    # window starts at index i (0-based): primes P[i..i+3]
    q0,q1,q2,q3=P[i],P[i+1],P[i+2],P[i+3]
    A,B,C,D=f(q0),f(q1),f(q2),f(q3)
    return (C-B)**2*A-(B-A)*(D-C)*C

def report(fname,f,deg,Xscan=1999000):
    # iterate windows with b^2>ae quickly (gap test first), then exact Q for those
    last_witness=None
    cnt_lastdecade=0
    halfX=Xscan//2
    total_trig=0
    for i in range(NP-3):
        if P[i]>Xscan: break
        a,b,e=G[i],G[i+1],G[i+2]
        if b*b<=a*e: continue       # weak trigger necessary (asymptotically); skip non-triggers
        # admissibility
        if f(P[i])<=0: continue
        Q=Qint(i,f)
        if Q>0:
            total_trig+=1
            last_witness=(i,P[i],(a,b,e))
            if P[i]>=halfX: cnt_lastdecade+=1
    iw=last_witness
    print(f"f={fname:14s} deg {deg}: #windows Q>0 (trigger&dominate)={total_trig:6d}; "
          f"in [{halfX},{Xscan}]: {cnt_lastdecade:5d}; "
          f"largest witness prime: {iw[1] if iw else None} gaps {iw[2] if iw else None}")
    return iw

for fname,f,deg in [
    ("p",        lambda p:p, 1),
    ("p+10^6",   lambda p:p+1000000, 1),
    ("p^2",      lambda p:p**2, 2),
    ("p^3",      lambda p:p**3, 3),
    ("p^5",      lambda p:p**5, 5),
    ("p^8",      lambda p:p**8, 8),
    ("p^12",     lambda p:p**12, 12),
    ("p^20",     lambda p:p**20, 20),
    ("p^30",     lambda p:p**30, 30),
]:
    report(fname,f,deg)
