"""
Does a ONE-SIDED spike (d_{s+1} >> d_s, but d_{s+2} unconstrained) ever suffice to fire?
Criterion fires iff R(s)=g_{s+1}^2/(g_s g_{s+2}) > rho(s)~1.
R(s) ~ d_{s+1}^2/(d_s d_{s+2}). If d_{s+1} >> d_s but d_{s+2} ~ d_{s+1} (gap stays high),
then R ~ d_{s+1}^2/(d_s d_{s+1}) = d_{s+1}/d_s >> 1 -> FIRES (since d_{s+1}/d_s>M>1>rho).
If d_{s+2} >> d_{s+1} (gap keeps growing), R ~ d_{s+1}^2/(d_s d_{s+2}) could be <1.

So one-sided LEFT spike (d_{s+1}>M d_s) fires PROVIDED d_{s+2} is not too much bigger than d_{s+1}.
Precisely fires if d_{s+1}^2 > rho(s) d_s d_{s+2}, i.e. d_{s+2} < d_{s+1}^2/(rho d_s) ~ d_{s+1}*(d_{s+1}/d_s).
Since d_{s+1}/d_s>M, this allows d_{s+2} up to ~ M d_{s+1}. So fires UNLESS d_{s+2}>~M d_{s+1}
(another big jump up).

KEY: At index s where d_{s+1}/d_s = local LIMSUP record (d_{s+1} largest ratio jump), the NEXT
ratio d_{s+2}/d_{s+1} -- if d_{s+2}>M d_{s+1} then s+1 is an even bigger spike; can't keep
growing forever (gaps bounded by ~log^2 p << any geometric). So eventually the spike TOPS OUT
and at the top d_{s+2}<=d_{s+1}. At THAT s, R~d_{s+1}/d_s side... let me just verify empirically:
take the s achieving max d_{n+1}/d_n in a range; does criterion fire there?
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,5000000))
def gap(l): return P[l]-P[l-1]
def fires(ff,s):
    def c(l): return ff(P[l-1])
    g0=c(s+1)-c(s); g1=c(s+2)-c(s+1); g2=c(s+3)-c(s+2)
    return c(s)*int(g1)**2 > c(s+2)*g0*g2

# In each dyadic range, find s maximizing d_{s+1}/d_s (limsup witness), check fire for several f.
import math
LP=len(P)
print("num primes:", LP)
cap=LP-1000
ranges=[(a,min(b,cap)) for (a,b) in [(1000,10000),(10000,100000),(100000,cap)]]
for ffname,ff in [("p",lambda p:p),("p^2+1",lambda p:p**2+1),("p^6+1",lambda p:p**6+1)]:
    print(f"--- f={ffname} ---")
    for a,b in ranges:
        best=None; bestr=0
        for s in range(a,b):
            r=gap(s+1)/gap(s)
            if r>bestr: bestr=r; best=s
        s=best
        print(f"  range[{a},{b}): max d_{{s+1}}/d_s={bestr:.1f} at s={s}, gaps=({gap(s)},{gap(s+1)},{gap(s+2)}), "
              f"d_{{s+2}}/d_{{s+1}}={gap(s+2)/gap(s+1):.2f}, FIRES={fires(ff,s)}")
