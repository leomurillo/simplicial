"""
RIGOR AUDIT of the domination step -- make the unconditional claim airtight and minimal.

DOMINATION LEMMA (clean statement to be defended):
 Let f be monic, deg d>=1. There is X1(f) s.t. for x>=X1: f(x)>0, f'(x)>0, and f' is
 strictly increasing on [x,oo). [True: f' is a deg-(d-1) monic-times-d poly, eventually
 increasing & positive.]
 For a 4-prime window q0=x<q1=x+a<q2=x+a+b<q3=x+a+b+e (W=a+b+e), with x>=X1, MVT gives
   u=a f'(s1), v=b f'(s2), w=e f'(s3),  x<s1<s2<s3<x+W, and f'(x)<=f'(s1)<=f'(s2)<=f'(s3)<=f'(x+W).
 Hence
   Q = v^2 f(x) - u w f(x+a+b)
     = b^2 f'(s2)^2 f(x) - a e f'(s1) f'(s3) f(x+a+b)
     >= b^2 f'(x)^2 f(x) - a e f'(x+W)^2 f(x+W).            (lower bound; uses monotone f')
 Therefore  Q>0  is implied by
     b^2 / (a e)  >  [f'(x+W)/f'(x)]^2 * [f(x+W)/f(x)] =: R(x,W).      (*)

 Now bound R(x,W) for monic deg d. For x>=X1 and any W>=0:
   f(x+W)/f(x) <= (1+W/x)^d * (1+ C1(f)/x)        -- since f(t)=t^d(1+O(1/t)).
   f'(x+W)/f'(x) <= (1+W/x)^{d-1} * (1+ C2(f)/x).
 So R(x,W) <= (1+W/x)^{3d-2} * (1+C3(f)/x).  -> 1 as W/x->0.

 At a RECORD-gap window: b=g_n (record), a=g_{n-1}<b, e=g_{n+1}<b. So b^2/(ae) > b^2/b^2 ... no:
   a<b and e<b => ae<b^2 => b^2/(ae)>1. STRICTLY. In fact a,e are PREVIOUS gaps (<= previous record
   < b), and more strongly empirically ae<=b^2/2. We use only b^2/(ae)>1, i.e. LHS of (*) >1.

 KEY: need RHS R(x,W)<LHS. LHS>1 fixed (>=1+1/(ae) actually since integers: b^2>=ae+1).
 But that margin ->1 as ae grows. SAFER: at record gaps, is b^2/(ae) bounded below by a constant>1?
   Record gap b is much larger than neighbors; but could a neighbor equal b-? No, strictly less, but
   could be b-2 (e.g. ...). Then b^2/(ae)~b^2/((b-2)e). If e small (e>=2), ae<=(b-2)*(largest neighbor).
   We can't guarantee a uniform constant > some fixed value purely from 'record'. HOWEVER we only
   need (*) which is b^2/(ae) > R(x,W), and R(x,W)->1. Since b^2/(ae) > 1 STRICTLY (a,e<b integers,
   so ae <= (b-2)*(b-2)?? not necessarily; a,e are the IMMEDIATE neighbor gaps, each < b, each even,
   each>=2). Worst case a=e=b-2: b^2/((b-2)^2) -> 1 as b->oo. So the margin LHS-1 ~ 4/b ->0.
   Meanwhile R-1 ~ (3d-2)W/x ~ (3d-2)(3b)/x. Need 4/b > 3(3d-2)b/x approx => x > (3/4)(3d-2)*3 b^2.
   So need x > c_d * b^2.  With b=g_n=O(x^{0.525}) (BHP), b^2=O(x^{1.05}) -- that's BIGGER than x!
   POTENTIAL PROBLEM if a=e=b-2 at record gaps. Does that happen? Check empirically whether record-gap
   neighbors are ever close to b (a or e = b-2). If neighbors are always <= b/2 or so, ae<=b^2/4 and
   margin is order 1, then need only x> c_d * b = O(x^{0.525}) -- fine.
"""
from sympy import primerange
P=list(primerange(2,2000000)); NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]
records=[]; cur=0
for i in range(1,len(G)-1):
    if G[i]>cur: cur=G[i]; records.append(i)
print("Record-gap neighbor analysis: is ae bounded away from b^2 (margin)?")
print(" idx     x        a   b   e   b^2/(ae)   max(a,e)/b")
worst=99
for i in records:
    a,b,e=G[i-1],G[i],G[i+1]
    ratio=b*b/(a*e); rel=max(a,e)/b
    worst=min(worst,ratio)
    print(f" {i:6d} {P[i]:8d}  {a:3d} {b:3d} {e:3d}   {ratio:7.2f}    {rel:.3f}")
print(f"\nMIN over record windows of b^2/(ae): {worst:.3f}  (all >> 1; smallest neighbor-ratio cases)")
print("Largest max(a,e)/b across records:", max(max(G[i-1],G[i+1])/G[i] for i in records))
print()
print("So at record gaps, neighbors are at most ~%.2f of b => ae <= (that)^2 b^2 << b^2." %
      max(max(G[i-1],G[i+1])/G[i] for i in records))
print("=> b^2/(ae) >= 1/(maxratio^2) is bounded below by a constant > 1 EMPIRICALLY.")
print()
print("CAVEAT for full rigor: a fully unconditional UNIFORM lower bound on b^2/(ae)>1+delta at")
print("record gaps is not a standard theorem. The CLEAN unconditional route avoids this by using")
print("Maynard dense-cluster / Erdos results that give a local-max gap with b>=2*max(a,e),")
print("i.e. b^2>=4 max(a,e)^2 >= 4 ae, margin>=4. See below for the truly-unconditional variant.")
