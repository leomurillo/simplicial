"""Paper 01g, Section 12.5 (Collatz on the rationals with odd denominators) -- certificate.

2026-10-17. Criteria declared before first execution, after exploratory probes in the
same session. T(x) = x/2 if the numerator of x is even, (3x+1)/2 otherwise, on Z_(2)
(rationals with odd denominator).

Q1  Wikipedia examples: the word (1011001) generates 151/47 and the 7-cycle
    151/47 -> 250/47 -> 125/47 -> 211/47 -> 340/47 -> 170/47 -> 85/47 -> 151/47;
    the words (1100) and (11001100) both generate 5/7.
Q2  Denominator law: for x = a/(3^k d) in lowest terms (3 not dividing d), every odd
    step divides the denominator by 3 while k > 0 and leaves it unchanged once k = 0;
    every even step leaves it unchanged (5000 random orbits, 300 steps each).
Q3  One rational cycle per primitive necklace: for 1 <= K <= 16 the number of distinct
    rational cycles of length K equals (1/K) sum_{e|K} mu(e) 2^{K/e}, and every point
    n*_w realizes its own word w.
Q4  Charge 1: among all primitive words with K <= 18, the cycles of denominator 1 are
    exactly {0}, {-1}, {1,2}, {-5,-7,-10} and the eleven-step cycle {-17,...,-136}.
Q5  Fibers: for 5000 random (d, a) with d odd, 3 not dividing d, gcd(a,d) = 1:
    d * T(a/d) = T_d(a), where T_d(a) = a/2 (a even), (3a+d)/2 (a odd).
Q6  Charges: every odd d <= 60 not divisible by 3 is the denominator of a primitive
    rational cycle of length <= 30; for d = 41 and d = 53 none has length <= 18, and
    primitive cycles of T_41 of length 20 and of T_53 of length 29 exist.
Q7  The 3-coordinate is attracted to 0: for 5000 random x in Z_(2) with v3(x) = j
    (|j| <= 6), v3(T^i x) = 0 for every i after the (max(-j,0)+1)-th odd step, over 300
    steps.
"""
from pathlib import Path
import json, math, sys, time, random
from fractions import Fraction as Fr
from sympy import mobius, divisors

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []; t0 = time.perf_counter()
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail}); print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)
def T(x): return (3 * x + 1) / 2 if x.numerator % 2 else x / 2
def nstar(w):
    a, b = Fr(1), Fr(0)
    for e in w:
        if e: a, b = a * Fr(3, 2), b * Fr(3, 2) + Fr(1, 2)
        else: a, b = a / 2, b / 2
    return b / (1 - a)
def v3(x):
    a, b, v = abs(x.numerator), x.denominator, 0
    if a == 0: return 10**9
    while a % 3 == 0: a //= 3; v += 1
    while b % 3 == 0: b //= 3; v -= 1
    return v

# Q1
x = nstar([1, 0, 1, 1, 0, 0, 1]); orb = [x]
for _ in range(7): orb.append(T(orb[-1]))
exp = [Fr(n, 47) for n in (151, 250, 125, 211, 340, 170, 85, 151)]
check("Q1 Wikipedia examples", orb == exp and nstar([1, 1, 0, 0]) == Fr(5, 7) == nstar([1, 1, 0, 0, 1, 1, 0, 0]), f"{x}; 5/7 twice")

# Q2
random.seed(20261017); ok = True; n_orbits = 0
while n_orbits < 5000:
    k = random.randint(0, 6); d = random.choice([1, 5, 7, 11, 13, 25, 35, 49, 55, 77, 91, 143, 187])
    a = random.randrange(-10**8, 10**8)
    if a == 0 or math.gcd(a, 3 ** k * d) != 1: continue
    n_orbits += 1; x = Fr(a, 3 ** k * d); kk = k
    for _ in range(300):
        y = T(x)
        if x.numerator % 2:
            ok &= y.denominator == (3 ** (kk - 1) * d if kk > 0 else d); kk = max(kk - 1, 0)
        else:
            ok &= y.denominator == x.denominator
        x = y
check("Q2 denominator law", ok, "3-part stripped one per odd step; 3-free part frozen")

# Q3 / Q4
def prim_necklaces(K):
    seen = set(); out = []
    for b in range(2 ** K):
        w = tuple((b >> i) & 1 for i in range(K)); rots = [w[i:] + w[:i] for i in range(K)]; r = min(rots)
        if r in seen: continue
        seen.add(r)
        if len(set(rots)) == K: out.append(r)
    return out
ok3 = True; int_cycles = set(); total = 0
for K in range(1, 19):
    nk = prim_necklaces(K)
    if K <= 16:
        ok3 &= len(nk) == sum(mobius(e) * 2 ** (K // e) for e in divisors(K)) // K
    for w in nk:
        if 2 ** K == 3 ** sum(w): continue
        xs = nstar(list(w)); y = xs; total += 1
        if K <= 16:
            for e in w:
                if y.numerator % 2 != e: ok3 = False; break
                y = T(y)
            ok3 &= y == xs
        if xs.denominator == 1:
            o = [xs]
            for _ in range(K - 1): o.append(T(o[-1]))
            int_cycles.add(tuple(sorted(int(v) for v in o)))
check("Q3 one rational cycle per primitive necklace", ok3, f"K<=16 counts and realizations; {total} cycles with K<=18")
expect = {(0,), (-1,), (1, 2), (-10, -7, -5), (-136, -91, -82, -68, -61, -55, -41, -37, -34, -25, -17)}
check("Q4 charge-1 cycles", int_cycles == expect, f"{sorted(int_cycles)}")

# Q5
ok = True; cnt = 0
while cnt < 5000:
    d = random.randrange(1, 10**4, 2)
    if d % 3 == 0: continue
    a = random.randrange(-10**9, 10**9)
    if math.gcd(a, d) != 1: continue
    cnt += 1
    Td = a // 2 if a % 2 == 0 else (3 * a + d) // 2
    ok &= d * T(Fr(a, d)) == Td
check("Q5 fibers are cousin worlds", ok, "d*T(a/d) = T_d(a)")

# Q6
charges = {}
for K in range(1, 19):
    for w in prim_necklaces(K):
        if 2 ** K == 3 ** sum(w): continue
        dd = nstar(list(w)).denominator; charges.setdefault(dd, K)
def prim_cycle_len(d, N=60000, steps=3000):
    best = None
    for n0 in range(1, N):
        xx = n0; seen = {}
        for i in range(steps):
            if xx in seen:
                cyc = []; yy = xx
                while True:
                    cyc.append(yy); yy = yy // 2 if yy % 2 == 0 else (3 * yy + d) // 2
                    if yy == xx: break
                g = 0
                for c in cyc: g = math.gcd(g, c)
                if g == 1: best = len(cyc) if best is None else min(best, len(cyc))
                break
            seen[xx] = i; xx = xx // 2 if xx % 2 == 0 else (3 * xx + d) // 2
    return best
missing = [d for d in range(1, 61, 2) if d % 3 and d not in charges]
l41, l53 = prim_cycle_len(41), prim_cycle_len(53)
ok = missing == [41, 53] and l41 == 20 and l53 == 29
check("Q6 every small charge carries a cycle", ok, f"absent for K<=18: {missing}; primitive cycle lengths found: 41 -> {l41}, 53 -> {l53}")

# Q7
ok = True; cnt = 0
while cnt < 5000:
    j = random.randint(-6, 6); d = random.choice([1, 5, 7, 11, 13, 35])
    u = random.randrange(1, 10**7) * random.choice([-1, 1])
    if u % 3 == 0 or math.gcd(u, d) != 1: continue
    x = Fr(u * 3 ** max(j, 0), 3 ** max(-j, 0) * d)
    if x.denominator % 2 == 0: continue
    cnt += 1; need = max(-j, 0) + 1; odd = 0
    for _ in range(300):
        if x.numerator % 2: odd += 1
        x = T(x)
        if odd >= need and x != 0: ok &= v3(x) == 0
check("Q7 the 3-coordinate is attracted to 0", ok, "v3 = 0 after max(-j,0)+1 odd steps")

el = time.perf_counter() - t0; npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s")
(HERE / "cert_collatz_rationals_results.json").write_text(json.dumps({"rows": rows, "elapsed_s": el}, indent=2))
sys.exit(0 if npass == len(rows) else 1)
