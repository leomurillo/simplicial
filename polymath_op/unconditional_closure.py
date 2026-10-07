"""
Pin down the UNCONDITIONAL closure of the width issue.

We need: for each fixed d, infinitely many 4-prime windows with b^2>ae AND domination (**).
Domination (**) for pattern with width W and ratio s:=b^2/(ae)>1 needs
   x > W/(s^{1/(3d)}-1).
Worst case s just above 1 needs x huge; but we can DEMAND s>=2 (b^2>=2ae) to keep threshold mild:
then need x> W/(2^{1/(3d)}-1) ~ W*3d/ln2 ~ 4.33 d W. So if we find trigger windows with
b^2>=2ae and BOUNDED W at arbitrarily large x, domination holds for x> ~4.33 d W (finite).

CLEANEST UNCONDITIONAL INPUT (Banks-Freiberg-Maynard / Maynard 2016, 'Dense clusters of primes'):
For any m, there are infinitely many intervals [x, x+C_m] (C_m a constant dep. on m) containing
exactly m+1 primes with PRESCRIBED gap pattern realizable among admissible tuples... More simply:
the bounded gap theorem in the strong form gives infinitely many n with
   p_{n+1}-p_n <= 246  AND we can also bound a few consecutive gaps.
But controlling THREE consecutive gaps (to force a local max of bounded width) at large x is
exactly a 'pattern of gaps' statement. Maynard's method DOES give:
   For any admissible 4-tuple (h1<h2<h3<h4), there are infinitely many n with
   {n+h1,...,n+h4} all prime AND these being CONSECUTIVE primes is NOT guaranteed.
Consecutiveness is the obstruction (that's the quadruplet conjecture).

==> HONEST STATUS: a fully rigorous UNCONDITIONAL proof of bounded-width trigger windows
at arbitrarily large primes appears to require either (i) consecutive-prime constellations
(open), or (ii) a softer argument. Let's find the SOFTER argument that needs only:
   limsup g_n = oo  and  liminf g_n < oo   (both unconditional)
and yields trigger windows with x/W -> oo.

SOFT ARGUMENT ATTEMPT:
We do NOT need bounded W. We need x > W/(s^{1/3d}-1). For FIXED d, s^{1/3d}-1 is a fixed positive
number c_d as long as s>=2. So we need x > W/c_d, i.e. W < c_d * x. Since at prime x the local
gaps are W <= 3*max gap near x, and max gap near x is unconditionally O(x^{0.525}) (BHP) << c_d x,
this is satisfied for ALL large x AUTOMATICALLY -- PROVIDED the window has s=b^2/ae>=2.
So the ONLY thing to secure unconditionally: infinitely many windows at large x with b^2>=2ae.
Does b^2>=2ae happen infinitely often at large x unconditionally? b=local max gap.
A strict local max gives b>max(a,e) but maybe only b^2>ae, not >=2ae. Need a STRONG local max:
b^2>=2ae. Test: do strong local maxima (b^2>=2ae) occur at arbitrarily large x? (numeric)
And is there an unconditional reason? b unbounded with a,e its neighbors: if b is a NEW MAXIMAL
gap (record), neighbors are <= previous records << b, so b^2 >> ae. Maximal (record) gaps are
infinite & unbounded (unconditional) and their neighbors are strictly smaller => b>a,b>e, and
typically b^2>>ae. CHECK record gaps give b^2>=2ae.
"""
from sympy import primerange
P=list(primerange(2,2000000)); NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]

# RECORD (maximal) gaps: g_n > g_k for all k<n. Their neighbors are < g_n (strictly, since record).
records=[]
cur=0
for i in range(1,len(G)-1):
    if G[i]>cur:
        cur=G[i]
        records.append(i)
print("Record-gap windows (b=record gap, a,e neighbors). Check b^2 vs ae and vs 2ae:")
print(" idx    x=P[i]     a   b   e   | b^2     ae    2ae  | b^2>ae b^2>=2ae")
ok_strong=0; ok_weak=0
for i in records:
    a,b,e=G[i-1],G[i],G[i+1]
    w=b*b>a*e; s=b*b>=2*a*e
    ok_weak+= w; ok_strong+= s
    if i==records[-1] or len(records)<=40 or i in records[:30]:
        print(f" {i:6d} {P[i]:9d}  {a:3d} {b:3d} {e:3d} | {b*b:5d} {a*e:5d} {2*a*e:5d} | {str(w):5s}  {str(s)}")
print(f"\nrecord-gap windows: {len(records)}; with b^2>ae: {ok_weak}; with b^2>=2ae: {ok_strong}")
print("largest prime with a record-gap window:", P[records[-1]])
print("NOTE: record gaps are unbounded & infinite (unconditional). Their neighbors are strictly")
print("smaller (by definition of record). So b>a and b>e ALWAYS for record gaps => b^2>ae always.")
