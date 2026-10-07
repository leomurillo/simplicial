"""
CLOSING THE PROOF with Pintz's unconditional theorem.

UNCONDITIONAL THEOREM (Erdos conjecture; proved by Pintz [Pin2]=arXiv:1305.6289, building on
Zhang/Maynard-Tao + Erdos-Rankin):
    limsup_n d_{n+1}/d_n = +infinity     and    liminf_n d_{n+1}/d_n = 0,        (PINTZ)
where d_n = p_{n+1}-p_n.

GOAL: produce infinitely many s with d_{s+1}^2/(d_s d_{s+2}) >= K for fixed K>1, at s->oo.
Actually we want EITHER d_{s+1}^2 >> d_s d_{s+2} (a "spike" up) — to make criterion fire.

Derivation from (PINTZ):
  limsup d_{n+1}/d_n = +infinity means: for every M, infinitely many n with d_{n+1} > M d_n.
  i.e. infinitely many n with d_{n+1}/d_n > M.   Set m=n. Then at index m: d_{m+1} > M d_m.
  This controls the LEFT ratio (d_{m+1} big vs d_m). Need also RIGHT: d_{m+1} big vs d_{m+2}.
  Equivalently d_{m+2}/d_{m+1} small, i.e. the ratio d_{m+2}/d_{m+1} < 1/M' for the NEXT index.
  By liminf d_{n+1}/d_n = 0: infinitely many n with d_{n+1}/d_n < eps. Set n=m+1: d_{m+2}/d_{m+1}<eps.
  But we need these at the SAME m. (PINTZ) as stated separately doesn't pin the same m.

  HOWEVER — limsup d_{n+1}/d_n = infinity ALONE gives, at index m, d_{m+1} > M d_m, so
     d_{s+1}^2/(d_s d_{s+2}) with s=m: = d_{m+1}^2/(d_m d_{m+2}).
  We know d_{m+1}>M d_m. Need d_{m+1} also large vs d_{m+2}. Not guaranteed by left ratio alone.

  CLEANER: use limsup d_{n+1}/d_n=infinity at index s+1: pick n=s s.t. d_{s+1}>M d_s (left big).
  For the right, note d_{s+2} could be huge. BUT consider instead applying limsup to get a spike
  and liminf to get the descent right after. The cleanest is:

  TWO-SIDED SPIKE LEMMA (derived): There are infinitely many m with
      d_{m+1} > M*d_m  AND  d_{m+1} > M*d_{m+2}.
  Is this derivable from (PINTZ)? Consider the set S_up={n: d_{n+1}>M d_n} (infinite).
  For n in S_up, look at n+1: ratio d_{n+2}/d_{n+1}. If for infinitely many n in S_up we also
  have d_{n+2} < d_{n+1}/M (i.e. d_{n+2}/d_{n+1}<1/M), then m=n works.
  Suppose NOT: then for all but finitely many n in S_up, d_{n+2} >= d_{n+1}/M.
  Hmm, that's consistent (gaps stay large). So not immediate.

  Let me use a DIFFERENT, fully rigorous route that (PINTZ)-type limsup directly gives:
  Use the ONE-SIDED spike and a SHIFTED window. The Hankel minors come in two flavors:
  contiguous minor at offset i used s=2i+1 with Psi(s)=c_{s+2}g_s g_{s+2}-c_s g_{s+1}^2 (middle
  spike up => fire). But there's ALSO the option of a minor that fires on a DOWN-spike (valley),
  by symmetry/transpose. Let me check: does a window with d_{s+1} SMALL vs neighbors (valley)
  also produce a negative minor? Test Psi sign for valley pattern.
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,3000000))
def gap(l): return P[l]-P[l-1]
def Psi(ff,s):
    def c(l): return ff(P[l-1])
    g0=c(s+1)-c(s); g1=c(s+2)-c(s+1); g2=c(s+3)-c(s+2)
    return c(s+2)*g0*g2 - c(s)*int(g1)**2   # <0 => fire
# spike up: g1 big. valley: g1 small. Check which fires.
ff=lambda p:p
print("Pattern vs Psi sign (Psi<0 = fires = non-moment witness):")
# find a clean spike-up window and a valley window at moderate s
for label,cond in [("SPIKE-UP d_{s+1}>2max(d_s,d_{s+2})", lambda s: gap(s+1)>2*max(gap(s),gap(s+2))),
                   ("VALLEY  d_{s+1}<min(d_s,d_{s+2})/2", lambda s: 2*gap(s+1)<min(gap(s),gap(s+2)))]:
    found=[]
    for s in range(100,5000):
        if cond(s):
            ps=Psi(ff,s)
            found.append((s,(gap(s),gap(s+1),gap(s+2)),int(ps<0)))
            if len(found)>=4: break
    print(f"  {label}: (s, gaps, fires?) -> {found}")
