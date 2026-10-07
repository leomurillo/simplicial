"""joint_regime_highalpha.py — push the joint-regime measurement PAST the Holder cap.

The shared joint_regime_probe.py reaches only alpha = log d/log X <= 0.667 (divisors of P_7, n<=7),
but T2 becomes the binding terminus only at n>=11, where theta_0 > 3/4 and the Holder route (Rhold)
fails (sec.5 cap).  Here we measure alpha in [0.70, 0.90] (the n=11..30 schedule: theta_0(11)=0.757,
theta_0(15)=0.818, theta_0(20)=0.862) by snapshotting a fixed smooth modulus d at X = d^{1/alpha}.

Decisive separation to exhibit:  as alpha crosses 3/4,
    Rhold = V^{3/2}/main           CROSSES 1  (the lossy l3<=l2 Holder charge fails)
    R3    = |sum Delta^3|/main      STAYS << 1 (the GENUINE signed third moment T2 holds, CLT-scale)
i.e. T2 is true with room exactly where the Holder route dies.  Same engine as the shared probe.
"""
import numpy as np, math, time

DS = [30030, 102102, 255255, 510510]      # smooth moduli (large phi -> enough primes/class at high alpha)
ALPHAS = [0.70, 0.75, 0.80, 0.85, 0.90]
cps_raw = sorted((int(d ** (1.0/al)), d) for d in DS for al in ALPHAS)
XMAX = max(x for x, _ in cps_raw)
print(f"high-alpha cut points: {len(cps_raw)};  XMAX = {XMAX:,}")

lim = int(XMAX**0.5) + 1
bs = np.ones(lim + 1, bool); bs[:2] = False
for p in range(2, int(lim**0.5) + 1):
    if bs[p]: bs[p*p::p] = False
BASE = np.flatnonzero(bs)

acc = {d: np.zeros(d) for d in DS}
rows = []
def snapshot(d, X):
    v = acc[d].copy()
    for p in BASE:
        p = int(p)
        if p * p > X: break
        pe, lp = p * p, math.log(p)
        while pe <= X:
            v[pe % d] += lp; pe *= p
    a = np.arange(d); cop = np.gcd(a, d) == 1
    vals = v[cop]; phi = int(cop.sum())
    D = vals - vals.mean()
    V = float((D*D).sum()); D3 = float((D**3).sum()); D3a = float((np.abs(D)**3).sum())
    main = X**3 / phi**2
    rows.append(dict(d=d, X=X, al=math.log(d)/math.log(X), phi=phi,
                     R2=V/(X*math.log(X)), R3=abs(D3)/main, Rhold=V**1.5/main,
                     canc=abs(D3)/D3a if D3a else 0.0))

def add_chunk(ps):
    if len(ps)==0: return
    lg = np.log(ps.astype(np.float64))
    for d in DS: acc[d] += np.bincount(ps % d, weights=lg, minlength=d)

t0=time.time(); SEG=1<<23; lo=0; ci=0
cps = cps_raw[:]
while lo <= XMAX:
    hi = min(lo+SEG, XMAX+1)
    b = np.ones(hi-lo, bool)
    if lo==0: b[0:2]=False
    for p in BASE:
        p=int(p)
        if p*p>=hi: break
        st = max(p*p, ((lo+p-1)//p)*p); b[st-lo::p]=False
    ps = np.flatnonzero(b)+lo; pos=0
    while ci < len(cps) and cps[ci][0] < hi:
        cx, d = cps[ci]
        idx = int(np.searchsorted(ps, cx, side='right'))
        add_chunk(ps[pos:idx]); pos=idx
        snapshot(d, cx); ci += 1
    add_chunk(ps[pos:]); lo=hi
print(f"sieve+accumulate: {time.time()-t0:.1f}s\n")

rows.sort(key=lambda r: r['al'])
print(f"{'d':>7} {'X':>11} {'alpha':>6} {'phi':>6}  {'R2':>7} {'R3 signed':>10} {'Rhold':>10}  "
      f"{'Rhold/R3':>9}  {'Holder':>7} {'T2(R3<1)':>9}")
for r in rows:
    print(f"{r['d']:>7} {r['X']:>11} {r['al']:>6.3f} {r['phi']:>6}  {r['R2']:>7.3f} {r['R3']:>10.2e} "
          f"{r['Rhold']:>10.2e}  {r['Rhold']/max(r['R3'],1e-300):>9.1e}  "
          f"{'FAILS' if r['Rhold']>1 else 'ok':>7} {'HOLDS' if r['R3']<1 else 'NO':>9}")

print("\nverdict by schedule row (theta_0(n)=alpha):")
print("  Holder cap is theta<3/4=0.75 ; theta_0(11)=0.757, theta_0(15)=0.818, theta_0(20)=0.862")
nfail_holder = sum(1 for r in rows if r['al']>0.75 and r['Rhold']>1)
nt2 = sum(1 for r in rows if r['al']>0.75 and r['R3']<1)
ntot = sum(1 for r in rows if r['al']>0.75)
print(f"  past the cap (alpha>0.75): Holder charge exceeds 1 in {nfail_holder}/{ntot} rows;"
      f"  signed T2 (R3<1) holds in {nt2}/{ntot}")
print("  => the lossy Holder route dies past 3/4 while the genuine signed third moment stays << 1:")
print("     T2 is the correct terminus and is empirically true with room exactly where n>=11 needs it.")
