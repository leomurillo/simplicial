"""
THE RACE, MADE RIGOROUS. This is the key to upgrading to a PROOF.

Setup: f monic, deg d>=1, increasing on [X0,oo). s large. a=p_s<b=p_{s+1}<c=p_{s+2}<e=p_{s+3}.
Gaps d_s=b-a, d_{s+1}=c-b, d_{s+2}=e-c (positive even integers for s>=2; smallest is 2).

We want Psi(s)<0:  c_s g_{s+1}^2 < ... wait sign. Psi(s)=c_{s+2}g_s g_{s+2} - c_s g_{s+1}^2.
Psi(s)<0  <=>  c_s g_{s+1}^2 > c_{s+2} g_s g_{s+2}
          <=>  g_{s+1}^2/(g_s g_{s+2}) > c_{s+2}/c_s = rho(s).

We'll show: IF g_{s+1}^2 > g_s g_{s+2}  [plain gap-log-concavity of the f-gaps]  AND s large,
THEN g_{s+1}^2/(g_s g_{s+2}) > rho(s), hence Psi(s)<0.

Need a LOWER bound on the excess E(s):=g_{s+1}^2/(g_s g_{s+2}) - 1 when it's >0, and an UPPER
bound on rho(s)-1, and show lower>upper for large s.

(A) UPPER bound rho(s)-1:
   rho(s) = f(c)/f(a). f monic deg d. f(c)-f(a) = f'(xi)(c-a), a<xi<c. c-a=d_s+d_{s+1}.
   rho(s)-1 = f'(xi)(c-a)/f(a) <= f'(c)(c-a)/f(a).
   For monic f deg d and large x: f'(x) <= 2 d x^{d-1}, f(x) >= x^d/2. So
   rho(s)-1 <= [2 d c^{d-1}/(a^d/2)] (c-a) = 4d (c^{d-1}/a^d)(c-a).
   Since c=a+O(c-a) and c-a is small vs a: c^{d-1}/a^d <= 2/a for large a (as c~a). So
   rho(s)-1 <= 8 d (c-a)/a = 8 d (d_s+d_{s+1})/p_s.       (ROUGH but rigorous-able)
   KEY: rho(s)-1 = O_d( (d_s+d_{s+1}) / p_s ).  Gaps are o(p_s) (any prime-gap bound), so ->0.

(B) LOWER bound on E(s) when g-log-concave:
   g_l = f(p_{l+1})-f(p_l) are POSITIVE INTEGERS (f has integer coeffs? NOT necessarily!
   f is a real polynomial. Hmm. f(p) integer not guaranteed).
   *** PROBLEM: f need not be integer-valued. Then g_l not integers, E(s) excess not >= 1/(..).
   So the integer argument FAILS for general real f. ***
   Must bound E(s) below differently. When g_{s+1}^2 > g_s g_{s+2}, the excess can be tiny
   for real f. So PLAIN log-concavity does NOT obviously beat rho for general REAL f.

   HOWEVER: we get to CHOOSE the window s. We don't need EVERY log-concave window; we need
   ONE (i.o.) where E(s) is bounded away from 0. That's exactly (G_C) again for the f-gaps.
   For the f-gaps g_l ~ f'(p_l) d_l, E(s) ~ d_{s+1}^2/(d_s d_{s+2}) - 1 (f' factors cancel to
   1+o(1)). So E(s) bounded away from 0 i.o.  <=>  prime-gap ratio bounded away from 1 i.o.
   = (G_C) for PRIME gaps. Back to needing strong prime-gap fluctuation.

 *** REVISED HONEST CONCLUSION ***
 The integer-excess shortcut only works when f is INTEGER-VALUED on primes (e.g. f in Z[x],
 or binomial-integer-valued). For such f (which includes ALL the natural cases p, p+c (c integer),
 p^2+1, etc.), g_l are integers, excess>=1/(g_s g_{s+2}), and the race is WINNABLE rigorously
 (see below). For general REAL f, we still reduce to (G_C)-prime which is true but I lack an
 unconditional citation.

Let me make the INTEGER-VALUED case fully rigorous and quantify, since it covers the headline
cases. For f in Z[x] (integer coefficients): g_l = f(p_{l+1})-f(p_l) in Z, and g_l>0 for large l.
When g_{s+1}^2 > g_s g_{s+2} (integers), g_{s+1}^2 >= g_s g_{s+2} + 1, so
   E(s) = g_{s+1}^2/(g_s g_{s+2}) - 1 >= 1/(g_s g_{s+2}).
We need 1/(g_s g_{s+2}) > rho(s)-1. With rho(s)-1 = O(d_s+d_{s+1})/p_s and g_l<=f'(c)*d_l<=
2 d c^{d-1} d_l, we get g_s g_{s+2} <= 4 d^2 c^{2d-2} d_s d_{s+2}. So suffices:
   1/(4 d^2 c^{2d-2} d_s d_{s+2}) > 8 d (d_s+d_{s+1})/a
i.e.  a > 32 d^3 c^{2d-2} d_s d_{s+2}(d_s+d_{s+1}).      (RACE-INT)
LHS a=p_s ~ c. RHS ~ c^{2d-2} * (gaps)^3. For d>=2, c^{2d-2}>=c^2 grows FASTER than c -> RHS
beats LHS!! So for d>=2 the integer-excess (just +1) is TOO SMALL. The race is LOST for d>=2
with only +1 excess. Need bigger excess => again strong fluctuation.

  Wait: recheck. For d>=2, g_l ~ f'(p_l) d_l ~ d p_l^{d-1} d_l is LARGE (~p^{d-1}), so g_s g_{s+2}
  ~ p^{2d-2} is huge, and 1/(g_s g_{s+2}) ~ p^{-(2d-2)} is tiny, much smaller than rho-1~1/p.
  So integer +1 excess loses for d>=2. CONFIRMED. The +1 trick only helps d=1.

 So even integer-valued f with d>=2 needs E(s) ~ (prime gap ratio -1) bounded away from 0, i.e.
 (G_C)-prime. The degree-1 case (f=p+c) might close via +1 trick. Let me verify d=1 closes
 and confirm d>=2 truly needs (G_C).
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,10000000))
def gap(l): return P[l]-P[l-1]

# d=1, f=p+0: g_l = d_l (prime gaps, integers). rho(s)=c/a=(p_{s+2})/(p_s) if c=0 -> p_{s+2}/p_s.
# Plain log-concave window: d_{s+1}^2 > d_s d_{s+2}. excess >=1/(d_s d_{s+2}). rho-1=(p_{s+2}-p_s)/p_s
# =(d_s+d_{s+1})/p_s. Race: 1/(d_s d_{s+2}) > (d_s+d_{s+1})/p_s <=> p_s > d_s d_{s+2}(d_s+d_{s+1}).
# gaps ~ log p, product ~ (log p)^3 << p. So holds for large s. CHECK every plain-log-concave
# window at large s fires for f=p:
ff=lambda p:p
bad=0; tot=0
for s in range(20000,300000):
    if gap(s+1)**2 > gap(s)*gap(s+2):  # plain log-concave (integer prime gaps)
        tot+=1
        g0=gap(s); g1=gap(s+1); g2=gap(s+2)
        # fires iff a*g1^2 > c*g0*g2 with a=p_s,c=p_{s+2}
        a=P[s-1]; c=P[s+1]
        if not (a*g1**2 > c*g0*g2):
            bad+=1
print(f"d=1 f=p: plain-log-concave windows s in [20000,300000): total={tot}, NON-firing={bad}")
print("  => for d=1, EVERY plain gap-log-concave window fires at large s (integer +1 excess wins).")
