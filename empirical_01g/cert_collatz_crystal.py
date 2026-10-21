"""Paper 01g, Section 12 (Collatz as a {2,3} phenomenon of the crystal) -- certificate.

2026-10-17. Criteria declared before first execution, after exploratory probes in the
same session. Author certificate, not blind. Shortcut map T(n) = n/2 (n even),
(3n+1)/2 (n odd), extended to Z[1/3] by the parity of the numerator.

C1  Frame-confined cycles: using all consecutive p_N-smooth pairs below 1.2e7
    (complete by Lehmer for p_N <= 23), the Collatz cycles whose odd elements and
    images are p_N-smooth are exactly {1}, {-1} for N = 2,3 and {1}, {-1}, {-5,-7}
    for 4 <= N <= 9 (odd elements listed). The 11-cycle's largest prime is 61.
C2  Z[1/3]: (a) T(2x) = x and T((2x-1)/3) = x, with (2x-1)/3 odd, for 20000 random
    x in Z[1/3]; (b) x = a/3^k (3 not dividing a) becomes an integer after exactly k
    odd steps (20000 random, k <= 12); (c) backward: if v3(x) = -k < 0 then
    v3((2x-1)/3) = -k-1 and v3(2x) = -k (all checked cases).
C3  Branching: for integers 1 <= m <= 1e6, the odd preimage (2m-1)/3 is an integer
    iff m = 2 mod 3; no m = 0 mod 3 has an integral odd preimage at any level 2^j m,
    j <= 30; the inverse-tree level ratio at depth 40 is within 0.005 of 4/3.
C4  Pathwise three-place balance: for 2000 random pairs x != y sharing their first K
    parity bits (K = 30), with m odd steps: v2(T^K x - T^K y) = v2(x-y) - K,
    v3(T^K x - T^K y) = v3(x-y) + m, and T^K x - T^K y = (3^m/2^K)(x-y) exactly.
C5  Unimodular cycles: |2^K - 3^m| = 1 for 1<=K<=400, 0<=m<=260 exactly at
    (K,m) = (1,0),(1,1),(2,1),(3,2); their parity words give exactly the integer
    cycles {0}, {-1}, {1,2}, {-5,-7,-10}; the pairs {2^K,3^m} are exactly the
    consecutive {2,3}-smooth pairs (1,2),(2,3),(3,4),(8,9).
C6  Affine branches: for every primitive word w with K<=14, the rational periodic
    point n*_w = S_w/(2^K-3^m) has sign(n*_w) = sign(2^K-3^m); for the alternating
    words (10)^j, j<=20, n*_w = 1.
C7  Comma lock: the first (K,m) with 0 < K ln2 - m ln3 < m/(3A), scanning upper
    convergents and intermediate fractions of log2 3, is (301994, 190537) for
    A = 1.765e10 and (114208327604, 72057431991) for A = 2^68.
C8  Entropy lock: 1 - H(log_3 2) (binary entropy, bits) lies in [0.0499, 0.0502].
"""
from pathlib import Path
import json, math, sys, time, random
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
from sympy import primerange, factorint

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []; t0 = time.perf_counter()
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail}); print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)
PR = list(primerange(2, 100))
def T(x):
    x = Fr(x)
    return (3 * x + 1) / 2 if x.numerator % 2 else x / 2
def odd_part(x):
    while x % 2 == 0: x //= 2
    return x
def v3(x):
    x = Fr(x); v = 0; a, b = x.numerator, x.denominator
    while a % 3 == 0: a //= 3; v += 1
    while b % 3 == 0: b //= 3; v -= 1
    return v

# ---------------- C1
L = 12_000_002
gpf = np.ones(L + 1, np.int64)
for p in primerange(2, L + 1): gpf[p::p] = p
res = {}
for N in range(2, 10):
    m = np.arange(1, L); pairs = m[np.maximum(gpf[m], gpf[m + 1]) <= PR[N - 1]]
    edges = {}
    for A in pairs.tolist():
        B = A + 1
        if A % 3 == 0 and (A // 3) % 2 == 1: edges[A // 3] = odd_part(B)
        if B % 3 == 0 and (B // 3) % 2 == 1: edges[-(B // 3)] = -odd_part(A)
    cyc = set()
    for s in edges:
        seen = []; x = s
        while x in edges and x not in seen: seen.append(x); x = edges[x]
        if x in seen: cyc.add(tuple(sorted(seen[seen.index(x):])))
    res[N] = sorted(cyc)
exp = {N: ([(-1,), (1,)] if N < 4 else [(-7, -5), (-1,), (1,)]) for N in range(2, 10)}
p61 = max(max(factorint(abs(x))) for x in [-17, -25, -37, -55, -41, -61, -91, -82, -136, -68, -34])
check("C1 frame-confined cycles", res == exp and p61 == 61, f"{res}; 11-cycle largest prime {p61}")

# ---------------- C2
random.seed(20261017); ok_a = ok_b = ok_c = True
for _ in range(20000):
    k = random.randint(0, 8); a = random.randrange(-10**6, 10**6)
    x = Fr(a, 3 ** k)
    up = (2 * x - 1) / 3
    ok_a &= T(2 * x) == x and T(up) == x and up.numerator % 2 == 1
    kk = random.randint(1, 12); aa = random.randrange(1, 10**9)
    while aa % 3 == 0: aa = random.randrange(1, 10**9)
    y = Fr(aa, 3 ** kk); odd = 0
    while y.denominator != 1:
        if y.numerator % 2: odd += 1
        y = T(y)
    ok_b &= odd == kk
    z = Fr(aa, 3 ** kk)
    ok_c &= v3((2 * z - 1) / 3) == -kk - 1 and v3(2 * z) == -kk
check("C2 Z[1/3] two-to-one, forward drain, backward leak", ok_a and ok_b and ok_c, f"two-to-one {ok_a}; drain {ok_b}; leak {ok_c}")

# ---------------- C3
ok1 = all(((2 * m - 1) % 3 == 0) == (m % 3 == 2) for m in range(1, 10**6 + 1))
ok2 = all(((2 * (m * 2 ** j) - 1) % 3 != 0) for m in range(3, 3 * 10**4, 3) for j in range(31))
lvl = [1]; cnt = [1]
for d in range(40):
    nxt = []
    for x in lvl:
        nxt.append(2 * x)
        if x % 3 == 2 and x > 2: nxt.append((2 * x - 1) // 3)
    lvl = nxt; cnt.append(len(lvl))
ratio = cnt[40] / cnt[39]
check("C3 branching rule and 4/3 growth", ok1 and ok2 and abs(ratio - 4 / 3) < 0.005, f"rule {ok1}; dead stalks {ok2}; ratio {ratio:.4f}")

# ---------------- C4
def v2(n):
    n = abs(n); v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v
def v3i(n):
    n = abs(n); v = 0
    while n % 3 == 0: n //= 3; v += 1
    return v
ok = True; K = 30
for _ in range(2000):
    x = random.randrange(1, 10**12); y = x + (2 ** K) * random.randrange(1, 10**6) * (1 if random.random() < .5 else 3)
    a, b, mo = x, y, 0
    for _ in range(K):
        if a % 2: a, b, mo = (3 * a + 1) // 2, (3 * b + 1) // 2, mo + 1
        else: a, b = a // 2, b // 2
    ok &= v2(b - a) == v2(y - x) - K and v3i(b - a) == v3i(y - x) + mo and Fr(b - a) == Fr(3 ** mo, 2 ** K) * (y - x)
check("C4 three-place balance along shared parity words", ok, "v2 drops by K, v3 rises by m, exact ratio 3^m/2^K")

# ---------------- C5
uni = [(Kk, mm) for Kk in range(1, 401) for mm in range(0, 261) if abs(2 ** Kk - 3 ** mm) == 1]
def word_cycles(Kk, mm):
    out = set()
    for wbits in range(2 ** Kk):
        w = [(wbits >> i) & 1 for i in range(Kk)]
        if sum(w) != mm: continue
        # periodic point: x = A_w(x) with A_w composed along w
        a_, b_ = Fr(1), Fr(0)  # x -> a_ x + b_
        for e in w:
            if e: a_, b_ = a_ * Fr(3, 2), b_ * Fr(3, 2) + Fr(1, 2)
            else: a_, b_ = a_ / 2, b_ / 2
        x = b_ / (1 - a_)
        if x.denominator != 1: continue
        # check it follows w
        y = x; good = True
        for e in w:
            if (y.numerator % 2) != e: good = False; break
            y = T(y)
        if good:
            orb = []; y = x
            for _ in range(Kk): orb.append(int(y)); y = T(y)
            out.add(tuple(sorted(set(orb))))
    return out
cyc = set()
for Kk, mm in uni: cyc |= word_cycles(Kk, mm)
pairs23 = sorted({tuple(sorted((2 ** Kk, 3 ** mm))) for Kk, mm in uni})
ok = uni == [(1, 0), (1, 1), (2, 1), (3, 2)] and cyc == {(0,), (-1,), (1, 2), (-10, -7, -5)} and pairs23 == [(1, 2), (2, 3), (3, 4), (8, 9)]
check("C5 unimodular cycles = line-frame Stormer pairs", ok, f"(K,m) {uni}; cycles {sorted(cyc)}; pairs {pairs23}")

# ---------------- C6
def nstar(w):
    a_, b_ = Fr(1), Fr(0)
    for e in w:
        if e: a_, b_ = a_ * Fr(3, 2), b_ * Fr(3, 2) + Fr(1, 2)
        else: a_, b_ = a_ / 2, b_ / 2
    return b_ / (1 - a_)
ok = True
for Kk in range(1, 15):
    for wbits in range(2 ** Kk):
        w = [(wbits >> i) & 1 for i in range(Kk)]; mm = sum(w); D = 2 ** Kk - 3 ** mm
        if D == 0: continue
        ns = nstar(w)
        if ns != 0: ok &= (ns > 0) == (D > 0)
alt = all(nstar([1, 0] * j) == 1 for j in range(1, 21))
check("C6 affine branches: sign law and alternating fixed point 1", ok and alt, f"sign law {ok}; (10)^j -> 1: {alt}")

# ---------------- C7
mp.mp.dps = 60
th = mp.log(3) / mp.log(2)
a = []; x = th
for _ in range(45):
    ai = int(mp.floor(x)); a.append(ai); x = 1 / (x - ai)
conv = [(a[0], 1)]; p0, q0, p1, q1 = 1, 0, a[0], 1
for ai in a[1:]:
    p0, q0, p1, q1 = p1, q1, ai * p1 + p0, ai * q1 + q0; conv.append((p1, q1))
cands = set(c for c in conv if c[0] > c[1] * th)
for i in range(2, len(conv)):
    (pa, qa), (pb, qb) = conv[i - 2], conv[i - 1]
    for t in range(1, a[i] + 1):
        Kk, mm = pa + t * pb, qa + t * qb
        if Kk > mm * th: cands.add((Kk, mm))
cands = sorted(cands, key=lambda z: z[1])
def first(Abound):
    for Kk, mm in cands:
        d = Kk * mp.log(2) - mm * mp.log(3)
        if 0 < d < mm / (3 * Abound): return (Kk, mm)
f1, f2 = first(mp.mpf("1.765e10")), first(mp.mpf(2) ** 68)
check("C7 comma lock", f1 == (301994, 190537) and f2 == (114208327604, 72057431991), f"A=1.765e10 -> {f1}; A=2^68 -> {f2}")

# ---------------- C8
f = math.log(2) / math.log(3)
Hb = -(f * math.log2(f) + (1 - f) * math.log2(1 - f))
check("C8 entropy lock", 0.0499 <= 1 - Hb <= 0.0502, f"1 - H(log_3 2) = {1-Hb:.5f} bits/step")

el = time.perf_counter() - t0; npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s")
(HERE / "cert_collatz_crystal_results.json").write_text(json.dumps({"rows": rows, "elapsed_s": el}, indent=2))
sys.exit(0 if npass == len(rows) else 1)
