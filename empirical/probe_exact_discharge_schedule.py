"""
CONSOLIDATION CHECK (2026-06-08) -- the EXACT V/M discharge schedule vs the asymptotic 1-C*/n.

The V/M crossover (ocho 7.1): V-sector pure_V(P_n) must dominate the max-over-a M-error P_n^{1-theta0}:
        pure_V(P_n) > P_n^{1-theta0}   <=>   theta0(n) = 1 - log(pure_V(P_n))/log(P_n).
ocho 5: V-sector capacity is the EXACT sum  pure_V(P_n) = sum_{p<=p_n} (p^2-1)/6  (S(p)=(p^2-1)/6).
The asymptotic 1 - C*/n (C* ~ 2.80, really -> 3) is only the LARGE-n form; for small n it UNDERSTATES
the requirement. This probe computes the exact schedule and the true discharge frontiers.
"""
from math import log

def primes_upto(N):
    s = [True]*(N+1); s[0]=s[1]=False
    for i in range(2,int(N**0.5)+1):
        if s[i]: s[i*i::i]=[False]*len(s[i*i::i])
    return [i for i in range(2,N+1) if s[i]]

P = primes_upto(2000)                      # plenty for n up to ~50

def stats(n):
    ps = P[:n]
    pv = sum((p*p-1)/6 for p in ps)        # pure_V(P_n), exact value as float
    logPn = sum(log(p) for p in ps)        # log P_n = sum log p
    theta0 = 1 - log(pv)/logPn
    return theta0, pv, ps[-1], logPn

print("EXACT V/M discharge schedule  theta0(n) = 1 - log(pure_V)/log(P_n),  pure_V=sum_{p<=p_n}(p^2-1)/6")
print("=" * 80)
print(f"  {'n':>2} {'p_n':>4} {'pure_V':>9} {'theta0 EXACT':>12} {'1-2.80/n':>9} {'ocho tbl':>9}")
ocho_tbl = {3:0.473, 4:0.507, 5:0.545, 7:0.642, 10:0.735, 20:0.862, 30:0.907}
for n in range(2, 11):
    th, pv, pn, _ = stats(n)
    tbl = ocho_tbl.get(n)
    print(f"  {n:>2} {pn:>4} {pv:>9.2f} {th:>12.4f} {1-2.80/n:>9.4f} {(f'{tbl:.3f}' if tbl else '-'):>9}")

print("-" * 80)
print("Discharge frontier  n_max(theta) = largest n with theta0_EXACT(n) <= theta :")
def frontier(th, exact=True):
    best=1
    for n in range(2,60):
        t = stats(n)[0] if exact else (1-2.80/n)
        if t <= th: best=n
    return best
for name, th in [("classical BV 1/2",0.5),("Pascadi 6/11",6/11),("theta=0.600",0.600),("theta=0.642",0.642)]:
    print(f"  {name:>16} (theta={th:.4f}):  EXACT n<={frontier(th)}   |   asymptotic(1-2.80/n) n<={frontier(th,False)}")

print("-" * 80)
th5=stats(5)[0]; th6=stats(6)[0]; th4=stats(4)[0]
print("VERDICT.")
print(f"  * theta0(5) EXACT = {th5:.4f} (ocho tbl 0.545 -- matches); 6/11={6/11:.5f} covers n=5 (razor-tight).")
print(f"  * theta0(6) EXACT = {th6:.4f} ~ 3/5 -- NOT 8/15=0.5333 (the asymptotic 1-2.80/6).")
print(f"  * Pascadi 6/11={6/11:.4f} < theta0(6)={th6:.4f}: n=6 is NOT discharged. Max-over-a frontier = n<=5.")
print(f"  * theta0(4) EXACT = {th4:.4f} > 1/2: classical-BV frontier = n<=3 (NOT n<=5).")
print("  * Recent claims (classical n<=5, Pascadi n<=6) used the ASYMPTOTIC 1-2.80/n -- 1-2 rows")
print("    optimistic at small n. CORRECTED: classical n<=3, Pascadi n<=5; n=6 needs 0.600, n=7 0.642.")
assert abs(th6-0.6)<0.005 and th5 < 6/11 < th6 and th4 > 0.5
print("  [asserts pass]")
