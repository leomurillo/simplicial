"""
joint_regime_probe.py — the measurement the bridge audit calls for.

For squarefree d | P_7, measure at scales X where d = X^alpha with alpha
ranging from the iterated regime (alpha ~ 0.17) into the joint regime
(alpha = 1/2, 0.54, 0.60, 0.64, 2/3):

  Delta(a) = psi(X; d, a) - mean over coprime classes
  V(d)     = sum_a Delta(a)^2          (the sparse-BDH object, terminus T1)
  D3(d)    = sum_a Delta(a)^3  SIGNED  (the Lemma 6.8 remainder, terminus T2)

Reported ratios:
  R2    = V / (X ln X)            BDH-strength ratio (O(1) <=> sqrt cancellation in mean square)
  Rtriv = V * phi / X^2           trivial-strength ratio
  R3    = |D3| / (X^3/phi^2)      the cubic transfer error vs per-modulus main term  <- decisive
  R3abs = sum|Delta|^3 / main     what absolute values give
  Rhold = V^{3/2} / main          what N0 Lemma 6.8's Holder bound l3<=l2 charges
"""
import numpy as np, math, time

XMAX = 30030**2  # 901,800,900
MODULI = [30, 210, 2310, 6006, 10010, 15015, 30030,
          46410, 72930, 102102, 255255, 510510]   # squarefree divisors of P_7

cps = [
    (int(2310**1.5), [2310]),
    (int(15015**1.5), [15015]),
    (int(30030**1.5), [30030]),
    (2310**2, [2310]),
    (6006**2, [6006]),
    (10010**2, [10010]),
    (15015**2, [15015]),
    (XMAX, MODULI),
]
cps.sort()

lim = int(XMAX**0.5) + 1
bs = np.ones(lim + 1, bool); bs[:2] = False
for p in range(2, int(lim**0.5) + 1):
    if bs[p]:
        bs[p*p::p] = False
BASE = np.flatnonzero(bs)
print(f"base primes to {lim}: {len(BASE)}")

acc = {d: np.zeros(d) for d in MODULI}
rows = []

def snapshot(d, X):
    v = acc[d].copy()
    for p in BASE:                       # prime powers p^e <= X, e >= 2
        p = int(p)
        if p * p > X: break
        pe, lp = p * p, math.log(p)
        while pe <= X:
            v[pe % d] += lp
            pe *= p
    a = np.arange(d)
    cop = np.gcd(a, d) == 1
    vals = v[cop]
    phi = int(cop.sum())
    D = vals - vals.mean()
    V = float((D * D).sum())
    D3 = float((D ** 3).sum())
    D3a = float((np.abs(D) ** 3).sum())
    main = X**3 / phi**2
    rows.append(dict(d=d, X=X, al=math.log(d)/math.log(X), phi=phi, V=V,
                     R2=V/(X*math.log(X)), Rtriv=V*phi/X**2,
                     R3=abs(D3)/main, R3abs=D3a/main,
                     Rhold=V**1.5/main, D3=D3))

def add_chunk(ps):
    if len(ps) == 0: return
    lg = np.log(ps.astype(np.float64))
    for d in MODULI:
        acc[d] += np.bincount(ps % d, weights=lg, minlength=d)

t0 = time.time()
SEG = 1 << 23
lo, ci = 0, 0
while lo <= XMAX:
    hi = min(lo + SEG, XMAX + 1)
    b = np.ones(hi - lo, bool)
    if lo == 0:
        b[0:2] = False
    for p in BASE:
        p = int(p)
        if p * p >= hi: break
        st = max(p * p, ((lo + p - 1) // p) * p)
        b[st - lo::p] = False
    ps = np.flatnonzero(b) + lo
    pos = 0
    while ci < len(cps) and cps[ci][0] < hi:
        cx, ds = cps[ci]
        idx = int(np.searchsorted(ps, cx, side='right'))
        add_chunk(ps[pos:idx]); pos = idx
        for d in ds:
            snapshot(d, cx)
        ci += 1
    add_chunk(ps[pos:])
    lo = hi
print(f"sieve+accumulate: {time.time()-t0:.1f}s")

rows.sort(key=lambda r: r['al'])
print(f"\n{'d':>7} {'X':>11} {'alpha':>6} {'phi':>6}  {'R2=V/XlnX':>10} "
      f"{'Rtriv':>9}  {'R3 signed':>10} {'R3 |.|':>9} {'R3 Holder':>10}  {'sgn D3':>6}")
for r in rows:
    print(f"{r['d']:>7} {r['X']:>11} {r['al']:>6.3f} {r['phi']:>6}  {r['R2']:>10.3f} "
          f"{r['Rtriv']:>9.2e}  {r['R3']:>10.2e} {r['R3abs']:>9.2e} {r['Rhold']:>10.2e}  "
          f"{'+' if r['D3']>0 else '-':>6}")

print("\ncancellation of the SIGNED third moment vs absolute (|D3| / sum|Delta|^3):")
for r in rows:
    print(f"  d={r['d']:>7} X={r['X']:>11} alpha={r['al']:.3f}:  {r['R3']/r['R3abs']:.4f}")
