"""
FINALIZE the rigorous chain. Identify the MINIMAL unconditional input.

THEOREM (to prove): For every monic f, deg>=1, f(p)>0 on all primes, the sequence
   b_n = prod_{i<=n} f(p_i) is NOT a Hamburger moment sequence.

PROOF ARCHITECTURE:
 (1) [PROVED, exact] sign(D_N)=sign(det W_N); contiguous 3x3 Hankel minor at offset i has
     sign = sign(Psi(s)), s=2i+1, where
        Psi(s) = c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2,   c_l=f(p_l), g_l=c_{l+1}-c_l.
     A negative principal minor => NOT moment. So it SUFFICES to find ONE odd s with Psi(s)<0,
     i.e.  c_s g_{s+1}^2 > c_{s+2} g_s g_{s+2}.          (*)
     [We may even use any s if we allow the general principal minor on indices {a,a+1,a+2}
      with a=s? Let's confirm: minor on {i,i+1,i+2} gave s=2i+1 ODD. To realize an arbitrary
      odd s we set i=(s-1)/2. We only need SOME s, and the firing windows include odd s, so OK.
      Actually safer: we need the witness window to be at an ODD s. Check firing at odd s below.]

 (2) [Calculus, uniform] For s large, with a=p_s,...,e=p_{s+3}, gaps bounded (any sub-linear
     prime gap bound, e.g. classical d_l = o(p_l)):
        rho(s)=f(p_{s+2})/f(p_s) = 1 + O_f( (p_{s+2}-p_s)/p_s ) -> 1,
        and the f'-correction bracket -> 1, so
        Psi(s)<0  <==  d_{s+1}^2/(d_s d_{s+2}) > (1+o(1)).      (suffic., for s large)

 (3) [Unconditional ANT input -- THE crux] There exist infinitely many ODD s with
        d_{s+1}^2 > 4 d_s d_{s+2}          (strong gap-local-max).      (G)
     Then d_{s+1}^2/(d_s d_{s+2})>4>(1+o(1)), so (*) holds for those s large => DONE.

 Establish (G) UNCONDITIONALLY:
   Suppose only finitely many l have d_{l+1}^2>4 d_l d_{l+2}. Then for all l>=L:
       d_{l+1}^2 <= 4 d_l d_{l+2}.                                  (H)
   Hmm, factor 4 weakens the log-convex argument. Let me use the PLAIN version (no factor 4):
   we actually only need d_{s+1}^2 > (1+eps_s) d_s d_{s+2} with eps_s->0. So the real needed (G'):
       limsup_l  d_{l+1}^2/(d_l d_{l+2})  > 1     [strictly], occurring at arbitrarily large l.
   Equivalently NOT eventually log-convex. Suppose eventually log-convex:
       d_{l+1}^2 <= d_l d_{l+2}  for all l>=L  =>  r_l:=d_{l+1}/d_l nondecreasing (l>=L).
   r_l nondecreasing => limit R0 in (0,oo].
     If R0>1: d_l >= c R0'^l geometric (R0'>1) for large l => d_l grows exponentially in l.
        But d_l <= p_{l+1} <= (by Bertrand iterated) ... more simply: sum_{k<=l} d_k = p_{l+1}-2
        <= p_{l+1} = O(l log l). A sequence with d_l >= c R0'^l has sum >= c R0'^l -> exceeds
        O(l log l). CONTRADICTION.
     If R0<=1: r_l<=R0<=1 eventually? No: r_l nondecreasing with limit R0<=1 => r_l<=R0<=1 for
        all l>=L => d_{l+1}<=d_l for l>=L => d_l nonincreasing => bounded. But limsup d_l=+oo
        (prime gaps unbounded: e.g. l!+2,...,l!+l composite gives gaps>=l; ELEMENTARY, no PNT).
        CONTRADICTION.
   Hence NOT eventually log-convex: d_{l+1}^2>d_l d_{l+2} for infinitely many l. But this gives
   ratio>1 possibly ->1. For the UNIFORM eps_s we need ratio bounded away from 1 i.o.
   UPGRADE: At an l where d_{l+1}^2>d_l d_{l+2} with all even integers >=2, the ratio is a
   fraction of even integers exceeding 1; its EXCESS over 1 is >= 1/(d_l d_{l+2}) which ->0.
   So plain version doesn't give a uniform gap. NEED the stronger statement that the ratio
   exceeds a FIXED constant >1 infinitely often. THIS is the genuine analytic input.

   => Reduce to: limsup_l d_{l+1}/sqrt(d_l d_{l+2}) > 1 strictly, AND realized i.o. with a fixed
      margin. Numerically limsup looks like +oo. The cleanest SUFFICIENT unconditional theorem:
         (E-R) limsup_l d_{l+1}/d_l = +oo  AND  liminf_l d_{l+1}/d_l = 0  (Erdos-type),
      combined to get a local max with big ratio. Let me see if a SINGLE clean known theorem
      gives strong-local-max i.o.

Let me TEST the discrimination crisply at ODD s (needed for (1)), and confirm strong-local-max
at odd s recurs.
"""
from sympy import primerange
P=list(primerange(2,5000000))
def gap(l): return P[l]-P[l-1]
# odd-s strong-local-max with factor 4
sm=300000
odd_strong=[l for l in range(1,sm) if (l%2==1) and gap(l+1)**2>4*gap(l)*gap(l+2)]
print(f"ODD s with d_{{s+1}}^2>4 d_s d_{{s+2}} in [1,{sm}]: count={len(odd_strong)}, max={max(odd_strong)}")
print(f"  examples (s, p_s, d_s,d_s+1,d_s+2): {[(s,P[s-1],gap(s),gap(s+1),gap(s+2)) for s in odd_strong[:5]]}")
print(f"  large-s example: {[(s,P[s-1],gap(s),gap(s+1),gap(s+2)) for s in odd_strong[-3:]]}")
