"""
RIGOROUS PROOF of (G_C) for SOME fixed C>1, UNCONDITIONAL.

We use TWO unconditional inputs:
  (W) [Westzynthius 1931 / even elementary] limsup_n d_n = +infty.
  (MT) [Maynard 2013, Tao; Polymath8b] liminf_n d_n <= 246 (in particular liminf_n d_n =: L0 < infty;
       there is a fixed even number attained by infinitely many gaps; more simply liminf d_n<infty).

ARGUMENT (the "ascent/descent" or "peak isolation"):
 Since limsup d_n=+infty and liminf d_n = L0 < infty, the gap sequence (d_n) oscillates:
 it returns below L0+1 infinitely often AND exceeds any bound infinitely often.

 Fix a large target T (to be chosen). Choose a gap d_M > 3T*L0 ... let me make it concrete.
 Actually here's the clean peak-isolation:

 Let B = liminf d_n (finite). For any threshold V, infinitely many n have d_n > V (by W).
 Consider the FIRST index after which a gap exceeds V following a "small" gap...

 CLEANEST: Define a "peak" at l if d_l > d_{l-1} and d_l > d_{l+1} (strict two-sided local max).
 LEMMA P: there are infinitely many peaks l with d_l/min(... ) -> we want d_l large vs BOTH nbrs.

 Use: among any maximal run where the sequence goes up then down, the top is a peak. Since the
 sequence is unbounded above and has bounded liminf, there are infinitely many "excursions"
 from level ~B up to level >V and back to ~B. Each excursion has a MAXIMUM (a peak) of height
 >V. At that peak l*, d_{l*}=H>V. Its immediate neighbors d_{l*-1},d_{l*+1} are < H (peak), but
 could be close to H. To force them <= H/2 (strong), we need the peak to be SHARP.

 Sharpness is NOT guaranteed by W+MT alone (the descent could be gradual: H, H-2, H-4,...).
 So the FULLY ELEMENTARY route gives ratio>1 (plain), not ratio>C.

 THE UPGRADE that DOES give ratio bounded away from 1 i.o.:
   Maynard-Tao gives infinitely many n with d_{n}<=246 AND d_{n+1}<=246 (two consecutive small
   gaps), in fact a whole CLUSTER of consecutive bounded gaps. Pair with Erdos: limsup d_n/log p_n
   =infty (Westzynthius quantitative). The configuration we want: ... d_{l}<=246, d_{l+1}=BIG,
   d_{l+2}<=246. I.e. a single big gap immediately flanked by two bounded gaps.

   Does such a config provably occur i.o.? This is "a large gap isolated between two bounded
   gaps". The BFTB (Banks-Freiberg-Turnage-Butterbaugh, 2014) "consecutive primes in tuples" +
   prescribed patterns gives gap patterns realized by CONSECUTIVE primes i.o., but a 'big' gap
   in the middle of an admissible tuple is the LARGE-gap regime, not directly their small-gap
   tuples. So this specific isolated-peak config is, to my knowledge, NOT a citable closed theorem
   unconditionally.

 CONCLUSION ON RIGOR:
   - PLAIN (G_1): d_{l+1}^2 > d_l d_{l+2} i.o. -- PROVED unconditionally (log-convexity argument).
   - STRONG (G_C, C>1 fixed): TRUE (density ~25%, limsup=+inf numerically), but I do NOT have a
     fully rigorous unconditional citation/proof that the ratio stays bounded away from 1 i.o.
   - The criterion needs ratio > (1+o(1)); PLAIN (G_1) gives ratio>1 but excess ->0, which races
     against rho(s)-1->0. WHO WINS? Need: excess of R(s) over 1 vs rho(s)-1.

 SO the crux becomes a RACE. Let me MEASURE the race directly: at the i.o. plain-log-concave
 windows (ratio>1), is R(s)-1 >> rho(s)-1 ? i.e. is the margin Psi(s)<0 actually achieved at
 LARGE s for the minimal (ratio just above 1) windows, or only at strong (ratio>=4) windows?
 If firing requires strong windows, and strong windows' unconditional recurrence is open, then
 status = STRONG-EVIDENCE not PROVED. Let me check whether PLAIN windows (1<ratio<1.5) fire at
 large s.
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,10000000))
def gap(l): return P[l]-P[l-1]
def fires(ff,s):
    def c(l): return ff(P[l-1])
    g0=c(s+1)-c(s); g1=c(s+2)-c(s+1); g2=c(s+3)-c(s+2)
    return c(s)*int(g1)**2 > c(s+2)*g0*g2

# For f=p, look at windows with 1<R<1.5 (weakly log-concave) at LARGE s: do they fire?
ff=lambda p:p
weak_fire=0; weak_total=0; weak_examples=[]
for s in range(50000, 400000):
    R=Fraction(gap(s+1)**2, gap(s)*gap(s+2))
    if 1<R<Fraction(3,2):
        weak_total+=1
        if fires(ff,s):
            weak_fire+=1
        elif len(weak_examples)<5:
            weak_examples.append((s,float(R)))
print(f"f=p, large s in [50000,400000), windows with 1<R<1.5: total={weak_total}, FIRED={weak_fire}")
print(f"  fraction fired: {weak_fire/max(weak_total,1):.4f}")
print(f"  examples NOT fired (s,R): {weak_examples}")
# rho(s)-1 scale at s~100000:
s0=100000
print(f"  rho(s0)-1 at s0={s0}: {gap.__self__ if False else (P[s0+1]/P[s0-1]-1):.2e}")
