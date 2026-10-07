"""
PROVE (logic check + unconditional inputs) that strict-local-max gaps occur at
arbitrarily large primes.

We rely on TWO unconditional facts about the gap sequence g_n = p_{n+1}-p_n:
 (U1) limsup_n g_n = +infinity   (prime gaps are unbounded; classical, e.g. via n!+2,...,n!+n,
      or Westzynthius 1931). UNCONDITIONAL.
 (U2) liminf_n g_n < +infinity   (in fact <=246 by Maynard/Zhang; even the classical
      Erdos 1940 liminf g_n/log n <1 suffices, OR simply: g_n=2 or small infinitely often
      is NOT needed -- we only need g_n does NOT ->infinity, i.e. liminf finite).
      Actually liminf g_n is trivially finite: g_n>=2 for n>=2 and the average gap ~log p_n,
      but we need g_n bounded along a subsequence. Maynard-Zhang gives liminf<=246. UNCONDITIONAL.

LOGIC: Suppose for contradiction only finitely many strict local maxima. Then there is N0
beyond which g_n has NO strict local max, i.e. for all n>N0: NOT(g_{n-1}<g_n>g_{n+1}).
A real sequence with no strict local maximum beyond N0 ... we must show this forces
either eventual monotonic-up (=> limsup reached only at infinity but then no contradiction?)
Let's reason carefully and TEST the logic on synthetic sequences.

Cleaner LOGIC (the one we'll use):
  Since limsup g_n=oo, pick any threshold. Since liminf g_n=L<oo finite, infinitely many
  n have g_n<=L. Consider the running structure: there are infinitely many "ascents"
  (g_n large) and infinitely many "descents back to <=L). Between a value <=L and a
  subsequent value >L and back, the MAXIMUM gap in that excursion is a strict local max
  (a highest point strictly above both shoulders that are <= it, and at least one neighbor
  strictly below since it came up from <=L and returns). Formalize via: take an excursion
  where the peak value exceeds L; the FIRST index achieving the peak maximum on the excursion
  is a strict local max.

We TEST: generate the real gap sequence, and ALSO confirm that between any two indices with
small gaps there's a strict local max, and these go to infinity. Already confirmed numerically
(local maxima up to P~200000). Here we just sanity-check the EXTRACTION argument is valid:
for each 'excursion' between consecutive small-gap (<=4) indices that contains a gap>4,
verify a strict local max exists inside.
"""
from sympy import primerange
P=list(primerange(2,500000))
G=[P[i+1]-P[i] for i in range(len(P)-1)]

L=6  # use a concrete finite bound that liminf certainly beats infinitely often (g_n<=2,4,6 recur)
small=[i for i in range(len(G)) if G[i]<=4]   # indices with small gap (<=4) -- infinite (heuristically; here just need recurrence)
print(f"#indices with gap<=4 among {len(G)} gaps: {len(small)} (recur throughout range up to P={P[small[-1]]})")

# For each consecutive pair of small-gap indices (s,t) with an interior gap exceeding both
# endpoints, verify a STRICT local max lies strictly inside.
bad=0; checked=0; maxprime_with_locmax=0
for k in range(len(small)-1):
    s,t=small[k],small[k+1]
    if t<=s+1: continue
    interior=range(s+1,t)  # indices strictly between
    if not interior: continue
    # peak on [s..t]
    seg=list(range(s,t+1))
    peakval=max(G[j] for j in seg)
    if peakval<=max(G[s],G[t]):  # excursion doesn't rise above shoulders
        continue
    checked+=1
    # first index achieving peakval
    pk=next(j for j in seg if G[j]==peakval)
    # is it a strict local max?
    isloc = (0<pk<len(G)-1) and G[pk]>G[pk-1] and G[pk]>G[pk+1]
    if not isloc:
        # the peak might be flat (plateau). Then look for any strict local max inside seg.
        found=any((0<j<len(G)-1) and G[j]>G[j-1] and G[j]>G[j+1] for j in range(s+1,t))
        if not found: bad+=1
        else: maxprime_with_locmax=max(maxprime_with_locmax,P[pk])
    else:
        maxprime_with_locmax=max(maxprime_with_locmax,P[pk])

print(f"excursions checked: {checked}; excursions with NO interior strict local max: {bad}")
print(f"=> every qualifying excursion contains a strict local-max gap (bad=0 expected).")
print(f"strict-local-max gaps verified up to prime ~{maxprime_with_locmax}")
