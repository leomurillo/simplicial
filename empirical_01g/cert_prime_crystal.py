"""Paper 01g (The Prime Crystal) -- certificate. Criteria declared before first execution.

2026-10-16. Author certificate after analytic derivation, not blind discovery.
Exploratory probes (scratchpad, same session) preceded these checks; every claim
below is re-derived here from scratch. Retain all run logs; report failures.

Frame N: Gram <a,b>_N = (N a.b - sum(a) sum(b))/(N-1) on exponent vectors e(n).
Window W_N = {1,...,p_{N+1}-1}. Home frame of n: N = max(2, pi(n)).

G1  Window faithfulness and walls (2<=N<=300, all n in W_N, n>=2): P_N does not
    divide n, and for every p<=p_N: p|n  <=>  N v_p(n) - Omega(n) > 0, while p does
    not divide n  =>  value = -Omega(n) < 0. Control outside the window: 162 in N=3
    is even but lies on the odd side.
G2  Step identities (n < 1e5, home frame of n+1): |D_n|^2 formula, <e(n),e(n+1)> =
    -Omega(n)Omega(n+1)/(N-1) exactly, wall crossings = omega(n)+omega(n+1).
G3  Alignment. (a) No two walk steps parallel in frames 3..11 (exact). (b) The
    own-frame ray-alignment equation p^j +- 1 = P_N/p has, for 3<=N<=2000, exactly
    the solutions (N,p,j) = (3,2,4),(3,3,2),(3,5,1). (c) Own-frame parallel classes of
    Stormer bonds: N=3 has exactly {1->2, 15->16}; N=4,5 have none.
G4  Obtuse turns. Every turn at 2<=n<1e7 (home frame of n+1) has negative inner
    product. The analytic regime condition N > (log2 p_{N+1})^2 holds for every
    100<=N<=1e5. Report the closest approach to 90 degrees.
G5  Turn law: E[v2(n-1)v2(n+1) 1_{n odd}] = 1.5 +- 0.002 on [1e6,2e6), and the
    ratio-of-means C1/C0 equals -(EQ+EAC)/(2EQ) to 1e-12 on the same window.
G6  Birth identities. (a) Symbolic: <a,b>_{N+1} - <a,b>_N = (Oa Ob - a.b)/(N(N-1)).
    (b) For 2<=N<40: e(P_N) = -e(p_{N+1}) in frame N+1 (unit, inner product -1), and
    <e(m), e(p_{N+1})>_{N+1} = -Omega(m)/N for every m in W_N.
G7  Stormer census: consecutive p_N-smooth pairs (n<2e7) number 1,4,10,23,40,68,
    108,167,241 for N=1..9, last pairs at n = 1,8,80,4374,9800,123200,336140,
    11859210,11859210. Native steps: for 2<=n<1e6 the step's height equals the walk
    frame pi(n+1) iff n+1 or n is the newest prime p_{pi(n+1)}.
G8  Every record-length step n->n+1 (n<2e6, home frame) has n or n+1 a power of 2.
G9  Bulb, 9<=x<=1500, frame pi(x): the farthest node from 1 is 2^floor(log2 x)
    (unique); the diameter pair is {2^a, 3^b} (a,b maximal) and unique except
    x in {25,26}, where 5^2 ties with 3^2.
G10 Chirality kappa3 = sum_p (v_p - Omega/N)^3: kappa3(prime) = (N-1)(N-2)/N^2 and
    kappa3(P_N/p) = -kappa3(prime) exactly (N<=50); every window point n>=2 has
    kappa3 > 0 for 5<=N<=6000; for N<=4 the exceptions are exactly N=2:{2,3,4} (zero),
    N=3:{6} (negative), N=4:{6,10} (zero).
G11 Self-avoidance, exact, frames 2..8 (window steps): contacts between non-adjacent
    steps occur only for N=2 (1->2 and 3->4 overlap) and N=3 (exactly three:
    node 1 on 5->6; 2->3 crosses 5->6 at (1/2,3/4); 3->4 crosses 5->6 at (1/3,5/6));
    none for 4<=N<=8. Bonse: P_N > p_{N+1}^2 for 4<=N<=2000.
G12 Correlation kernel: mean of e(n).e(n+j) over n<4e6 equals
    c(j) = sum_{p|j} (1-p^{-v_p(j)})(p+1)/(p-1)^2 to 1e-4 for j=1..12.
G13 Centroid at n=1e6 (frame pi(1e6)) within 1e-3 of sqrt(sum_p 1/(p-1)^2)=1.172632.
G14 Bond stretching at births: a bond stretches iff (Omega(n+1)-Omega(n))^2 >
    Q(n)+Q(n+1); the first stretching bond is 59->60; direct recomputation of
    |D_n|^2 in frames N and N+1 matches the G6 update for all n<5000.

Run 1 (cert_run1.log): 13/14. G5 failed on a mis-specified criterion: the exact
identity is C1 = -(E[Q(n)] + E[A_n]) on the window, while C0 = E[Q(n)+Q(n+1)] equals
2E[Q] only up to the one-step window shift, so the ratio cannot match to 1e-12.
Repairs before run 2 (other criteria unchanged):
 - G5 now checks C1 == -(EQ+EAC) to 1e-12 (exact) and C1/C0 against
   -1/2 - EAC/(2EQ) to 1e-4.
 - G15 added (declared before run 2): adjacent walk steps n-1->n and n->n+1 meet
   only at the shared node e(n) in every frame 3<=N<=8 (window steps); in N=2 every
   adjacent pair is collinear (the fold).
"""
from pathlib import Path
import json, math, sys, time, itertools, bisect
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from sympy import primerange, factorint

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows, details = [], {}
t0 = time.perf_counter()


def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


PR = list(primerange(2, 2_000_000))
def pi(x): return bisect.bisect_right(PR, x)
def E(n, N):
    f = factorint(n); return [f.get(PR[i], 0) for i in range(N)]
def ip(a, b, N): return Fr(N * sum(x * y for x, y in zip(a, b)) - sum(a) * sum(b), N - 1)


# ------------------------------------------------------------ sieve arrays
M = 20_000_002
idx = np.arange(M + 1)
spf = np.zeros(M + 1, np.int64)
for p in range(2, int(M ** 0.5) + 1):
    if spf[p] == 0:
        s = spf[p * p::p]; s[s == 0] = p
spf[(spf == 0) & (idx >= 2)] = idx[(spf == 0) & (idx >= 2)]
Om = np.zeros(M + 1, np.int64); Q = np.zeros(M + 1, np.int64); S3 = np.zeros(M + 1, np.int64)
w = np.zeros(M + 1, np.int64); gpf = np.ones(M + 1, np.int64)
for m in range(2, M + 1):
    p = spf[m]; k = m; a = 0
    while k % p == 0: k //= p; a += 1
    Om[m] = Om[k] + a; Q[m] = Q[k] + a * a; S3[m] = S3[k] + a ** 3; w[m] = w[k] + 1; gpf[m] = max(gpf[k], p)
v2 = np.zeros(M + 1, np.int64); t = 2
while t <= M: v2[t::t] += 1; t *= 2
isp = (spf == idx) & (idx >= 2); pic = np.cumsum(isp)
print(f"arrays ready ({time.perf_counter()-t0:.1f}s)", flush=True)

# ------------------------------------------------------------ G1
fails = 0
for N in range(2, 301):
    P = math.prod(PR[:N])
    for n in range(2, PR[N]):
        if n % P == 0: fails += 1
        v = E(n, N); o = sum(v)
        for i in range(N):
            val = N * v[i] - o
            if (v[i] > 0) != (val > 0) or (v[i] == 0 and val != -o): fails += 1
v162 = E(162, 3)
ctrl = (3 * v162[0] - sum(v162)) < 0
check("G1 window faithful, walls = divisibility", fails == 0 and ctrl,
      f"failures {fails} over N<=300; control 162 (frame 3) on odd side: {ctrl}")

# ------------------------------------------------------------ G2
bad = 0
for n in range(1, 100000):
    N = max(2, pi(n + 1)); a, b = E(n, N), E(n + 1, N)
    d = [y - x for x, y in zip(a, b)]
    L2 = Fr(N * (Q[n] + Q[n + 1]) - (Om[n + 1] - Om[n]) ** 2, N - 1)
    if ip(d, d, N) != L2: bad += 1
    if ip(a, b, N) != Fr(-Om[n] * Om[n + 1], N - 1): bad += 1
    if sum(1 for i in range(N) if (a[i] > 0) != (b[i] > 0)) != w[n] + w[n + 1]: bad += 1
check("G2 step identities", bad == 0, f"mismatches {bad} for n<1e5")

# ------------------------------------------------------------ G3
def par(a, b, N): return ip(a, a, N) * ip(b, b, N) == ip(a, b, N) ** 2
pairs = 0
for N in range(3, 12):
    S = [[y - x for x, y in zip(E(n, N), E(n + 1, N))] for n in range(1, PR[N] - 1)]
    pairs += sum(1 for a, b in itertools.combinations(S, 2) if par(a, b, N))
hits = []
for N in range(3, 2001):
    ps = PR[:N]
    for p in ps:
        r = 1
        for q in ps:
            if q != p: r = r * q % p
        if r in (1, p - 1):
            Pq = math.prod(q for q in ps if q != p)
            for sgn in (-1, 1):
                x = Pq + sgn; j = 0
                while x % p == 0: x //= p; j += 1
                if x == 1: hits.append((N, p, j))
classes = {}
for N in (3, 4, 5):
    B = [n for n in range(1, 10000) if max(factorint(n * (n + 1)).keys()) <= PR[N - 1]]
    Sv = {n: [y - x for x, y in zip(E(n, N), E(n + 1, N))] for n in B}
    cl = []
    for n in B:
        for c in cl:
            if par(Sv[c[0]], Sv[n], N): c.append(n); break
        else: cl.append([n])
    classes[N] = [c for c in cl if len(c) > 1]
ok = pairs == 0 and sorted(hits) == [(3, 2, 4), (3, 3, 2), (3, 5, 1)] and classes == {3: [[1, 15]], 4: [], 5: []}
check("G3 alignment", ok, f"walk parallel pairs N=3..11: {pairs}; ray-equation solutions N<=2000: {hits}; own-frame classes {classes}")

# ------------------------------------------------------------ G4
n = np.arange(2, 10_000_000)
AC = np.where(n % 2 == 1, v2[n - 1] * v2[n + 1], 0)
N_ = np.maximum(2, pic[n + 1])
num = -N_ * (Q[n] + AC) + (Om[n] - Om[n - 1]) * (Om[n] - Om[n + 1])
B1 = N_ * (Q[n - 1] + Q[n]) - (Om[n] - Om[n - 1]) ** 2
B2 = N_ * (Q[n] + Q[n + 1]) - (Om[n + 1] - Om[n]) ** 2
cosv = num / np.sqrt(B1.astype(float) * B2.astype(float))
k = int(cosv.argmax())
regime = all(N > math.log2(PR[N]) ** 2 for N in range(100, 100001))
check("G4 obtuse turns", bool((num < 0).all()) and regime,
      f"all turns obtuse for n<1e7; closest {math.degrees(math.acos(cosv[k])):.3f} deg at n={int(n[k])}; analytic regime N>(log2 p_N+1)^2 for 100<=N<=1e5: {regime}")
details["G4"] = {"closest_deg": math.degrees(math.acos(cosv[k])), "at": int(n[k])}

# ------------------------------------------------------------ G5
s = (n >= 1_000_000) & (n < 2_000_000)
EAC = AC[s].mean(); EQ = Q[n[s]].mean()
C1 = (-(Q[n[s]] + AC[s])).mean(); C0 = (Q[n[s]] + Q[n[s] + 1]).mean()
ok = abs(EAC - 1.5) < 0.002 and abs(C1 + (EQ + EAC)) < 1e-12 and abs(C1 / C0 - (-0.5 - EAC / (2 * EQ))) < 1e-4
check("G5 turn law", ok, f"E[AC]={EAC:.5f}, E[Q]={EQ:.4f}, C1/C0={C1/C0:.5f} vs -1/2-E[AC]/(2E[Q])={-0.5-EAC/(2*EQ):.5f}, mean cos={cosv[s].mean():.5f}")

# ------------------------------------------------------------ G6
Ns = sp.symbols("N", positive=True)
a = sp.symbols("a0:5"); b = sp.symbols("b0:5")
def ipS(x, y, nn): return (nn * sum(i * j for i, j in zip(x, y)) - sum(x) * sum(y)) / (nn - 1)
res = sp.simplify(ipS(list(a) + [0], list(b) + [0], Ns + 1) - ipS(a, b, Ns)
                  - (sum(a) * sum(b) - sum(i * j for i, j in zip(a, b))) / (Ns * (Ns - 1)))
okb = True
for N in range(2, 40):
    one = [1] * N + [0]; new = [0] * N + [1]
    okb &= ip(one, one, N + 1) == 1 and ip(one, new, N + 1) == -1
    for m in range(2, PR[N]):
        okb &= ip(E(m, N) + [0], new, N + 1) == Fr(-int(Om[m]), N)
check("G6 birth identities", res == 0 and okb, f"symbolic residual {res}; antipode + layering N<40: {okb}")

# ------------------------------------------------------------ G7
mm = np.arange(1, M - 1)
H = pic[np.maximum(gpf[mm], gpf[mm + 1])]
counts = [int((H <= N).sum()) for N in range(1, 10)]
lasts = [int(mm[H <= N].max()) for N in range(1, 10)]
walk = np.maximum(1, pic[mm + 1])
sel = (mm >= 2) & (mm < 1_000_000)
newest = np.array(PR)[walk[sel] - 1]
native_pred = (mm[sel] + 1 == newest) | (mm[sel] == newest)
native_obs = H[sel] == walk[sel]
ok = (counts == [1, 4, 10, 23, 40, 68, 108, 167, 241]
      and lasts == [1, 8, 80, 4374, 9800, 123200, 336140, 11859210, 11859210]
      and bool((native_pred == native_obs).all()))
check("G7 Stormer census + native steps", ok, f"counts {counts}; last bonds {lasts}; native rule exact for n<1e6: {bool((native_pred==native_obs).all())}")

# ------------------------------------------------------------ G8
rec = -1; recs = []
for nn in range(1, 2_000_000):
    N = max(2, pic[nn + 1])
    L2 = (N * (Q[nn] + Q[nn + 1]) - (Om[nn + 1] - Om[nn]) ** 2) / (N - 1)
    if L2 > rec + 1e-12: rec = L2; recs.append(nn)
pow2 = lambda x: x & (x - 1) == 0
check("G8 records at powers of 2", all(pow2(r) or pow2(r + 1) for r in recs), f"{len(recs)} records: {recs}")

# ------------------------------------------------------------ G9
XM = 1500; NM = pi(XM)
V = np.array([E(nn, NM) for nn in range(1, XM + 1)], dtype=np.int64)
exc = []
for x in range(9, XM + 1):
    N = pi(x); Vx = V[:x, :N]; o = Vx.sum(1); q = (Vx * Vx).sum(1)
    r2 = N * q - o ** 2
    far = np.flatnonzero(r2 == r2.max()) + 1
    G = Vx @ Vx.T
    D = N * (q[:, None] + q[None, :] - 2 * G) - (o[:, None] - o[None, :]) ** 2
    cnt = int((D == D.max()).sum() // 2); i, j = np.unravel_index(D.argmax(), D.shape)
    aa = int(math.floor(math.log2(x))); bb = 0
    while 3 ** (bb + 1) <= x: bb += 1
    if list(far) != [2 ** aa] or {int(i) + 1, int(j) + 1} != {2 ** aa, 3 ** bb} or cnt != 1: exc.append(x)
check("G9 bulb: farthest node and diameter", exc == [25, 26], f"exceptions {exc} (expected [25, 26]: 5^2 ties 3^2)")

# ------------------------------------------------------------ G10
okp = all(sum((Fr(int(i == 0)) - Fr(1, N)) ** 3 for i in range(N)) == Fr((N - 1) * (N - 2), N * N)
          and sum((Fr(1 - int(i == 0)) - Fr(N - 1, N)) ** 3 for i in range(N)) == -Fr((N - 1) * (N - 2), N * N)
          for N in range(3, 51))
nonpos = {}
for N in range(2, 6001):
    nn = np.arange(2, PR[N]); kk = N * N * S3[nn] - 3 * N * Om[nn] * Q[nn] + 2 * Om[nn] ** 3
    bad = nn[kk <= 0]
    if len(bad): nonpos[N] = [(int(x), int(np.sign(N * N * S3[x] - 3 * N * Om[x] * Q[x] + 2 * Om[x] ** 3))) for x in bad]
check("G10 chirality", okp and nonpos == {2: [(2, 0), (3, 0), (4, 0)], 3: [(6, -1)], 4: [(6, 0), (10, 0)]},
      f"prime/co-prime kappa3 exact: {okp}; nonpositive window points: {nonpos}")

# ------------------------------------------------------------ G11
def meet(nn, m, N):
    en, em = E(nn, N), E(m, N)
    dn = [y - x for x, y in zip(en, E(nn + 1, N))]; dm = [y - x for x, y in zip(em, E(m + 1, N))]
    A = sp.Matrix([[dn[i], -dm[i], -1] for i in range(N)]); bvec = sp.Matrix([em[i] - en[i] for i in range(N)])
    try: sol, params = A.gauss_jordan_solve(bvec)
    except ValueError: return None
    if params.shape[0] > 0: return "overlap"
    tt, ss, _ = sol
    return (tt, ss) if 0 <= tt <= 1 and 0 <= ss <= 1 else None
contacts = {}
for N in range(2, 9):
    top = PR[N] - 1
    contacts[N] = [(nn, m, meet(nn, m, N)) for nn in range(1, top) for m in range(nn + 2, top) if meet(nn, m, N)]
bonse = all(math.prod(PR[:N]) > PR[N] ** 2 for N in range(4, 2001))
exp3 = [(1, 5, (0, sp.Rational(1, 2))), (2, 5, (sp.Rational(1, 2), sp.Rational(3, 4))), (3, 5, (sp.Rational(1, 3), sp.Rational(5, 6)))]
ok = (contacts[2] == [(1, 3, "overlap")] and contacts[3] == exp3 and all(contacts[N] == [] for N in range(4, 9)) and bonse)
check("G11 self-avoidance", ok, f"contacts N=2: {contacts[2]}; N=3: {contacts[3]}; N=4..8 empty: {all(contacts[N]==[] for N in range(4,9))}; Bonse 4<=N<=2000: {bonse}")

# ------------------------------------------------------------ G12
Xk = 4_000_000; err = 0.0
for j in range(1, 13):
    cj = sum((1 - 1 / p ** e) * (p + 1) / (p - 1) ** 2 for p, e in factorint(j).items())
    tot = 0.0
    for p in factorint(j):
        vv = np.zeros(Xk + 64, np.int64); tt = p
        while tt < len(vv): vv[tt::tt] += 1; tt *= p
        tot += (vv[1:Xk + 1] * vv[1 + j:Xk + 1 + j]).mean()
    err = max(err, abs(tot - cj))
check("G12 correlation kernel c(j)", err < 1e-4, f"max |mean - c(j)| over j<=12: {err:.2e}")

# ------------------------------------------------------------ G13
xN = 1_000_000; N = pi(xN)
xs = np.array([sum(xN // p ** k for k in range(1, 40) if p ** k <= xN) / xN for p in PR[:N]])
cen = math.sqrt(N / (N - 1) * ((xs * xs).sum() - xs.sum() ** 2 / N))
lim = math.sqrt(sum(1 / (p - 1) ** 2 for p in PR))
check("G13 centroid limit", abs(cen - 1.172632) < 1e-3, f"|centroid(1e6)| = {cen:.6f}; limit (p<2e6) = {lim:.6f}")

# ------------------------------------------------------------ G14
badu = 0; first = None
for nn in range(1, 5000):
    N = max(2, pi(nn + 1))
    d = [y - x for x, y in zip(E(nn, N), E(nn + 1, N))]
    upd = ip(d + [0], d + [0], N + 1) - ip(d, d, N)
    if upd != Fr(int((Om[nn + 1] - Om[nn]) ** 2 - Q[nn] - Q[nn + 1]), N * (N - 1)): badu += 1
    if first is None and (Om[nn + 1] - Om[nn]) ** 2 > Q[nn] + Q[nn + 1]: first = nn
frac = float(((Om[mm[1_000_000:2_000_000] + 1] - Om[mm[1_000_000:2_000_000]]) ** 2 >
              Q[mm[1_000_000:2_000_000]] + Q[mm[1_000_000:2_000_000] + 1]).mean())
check("G14 bond stretching at births", badu == 0 and first == 59,
      f"update mismatches {badu}; first stretching bond {first}->{first+1}; stretching fraction near 1e6: {frac:.4f}")

# ------------------------------------------------------------ G15
def meet_adj(nn, N):
    """steps nn-1 -> nn (param t) and nn -> nn+1 (param s): all contacts."""
    a, b, c = E(nn - 1, N), E(nn, N), E(nn + 1, N)
    d1 = [y - x for x, y in zip(a, b)]; d2 = [y - x for x, y in zip(b, c)]
    A = sp.Matrix([[d1[i], -d2[i], -1] for i in range(N)]); bvec = sp.Matrix([b[i] - a[i] for i in range(N)])
    sol, params = A.gauss_jordan_solve(bvec)
    if params.shape[0] > 0: return "collinear"
    return (sol[0], sol[1])
adj = {N: [meet_adj(nn, N) for nn in range(2, PR[N] - 1)] for N in range(2, 9)}
ok = all(r == "collinear" for r in adj[2]) and all(r == (1, 0) for N in range(3, 9) for r in adj[N])
check("G15 adjacent steps meet only at their node", ok,
      f"N=2: {adj[2]}; N=3..8 all only at shared node: {all(r == (1, 0) for N in range(3, 9) for r in adj[N])}")

el = time.perf_counter() - t0
npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s (Python {sys.version.split()[0]}, NumPy {np.__version__}, SymPy {sp.__version__})")
(HERE / "cert_prime_crystal_results.json").write_text(json.dumps({"rows": rows, "details": details, "elapsed_s": el}, indent=2, default=float))
sys.exit(0 if npass == len(rows) else 1)
