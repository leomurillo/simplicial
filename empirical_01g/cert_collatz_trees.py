"""Paper 01g, Section 12.6 (the binary tree and the Collatz tree) -- certificate.

2026-10-17. Criteria declared before first execution, after exploratory probes in the
same session. Family T_a(x) = x/2 (x even), (a x + 1)/2 (x odd), a odd; a = 3 is Collatz.

B1  The binary tree is the inverse tree of T_1: for 2 <= n <= 2^20 the T_1-parent of n
    is unique (n/2 or (n+1)/2), every n reaches 1, and the depth of n is exactly
    ceil(log2 n), so level k is {2^(k-1)+1, ..., 2^k}.
B2  Two perfect transversals: for k in {8, 12, 16} the 2^k Collatz preimages of 1 at
    depth k in Z_2 (one per parity word, x_w = (1 - B_w)/A_w) lie in 2^k distinct
    classes mod 2^k, each follows its word and maps to 1; the number of positive
    integral ones is within a factor [1.2, 1.8] of (4/3)^k.
B3  Parity charge: Q(n) = sum_i eps_i(n) 2^i, read as a 2-adic rational, has
    denominator exactly 3 for every 1 <= n <= 20000; Q(-1) = -1, Q(0) = 0, the
    denominator of Q(-5) is 7 and that of Q(-17) divides 2^11 - 1 = 2047.
B4  Coverage equation g_a(t) = 2^(-t)(1 + a^(t-1)) = 1: t = 1 is a root for every a;
    for a = 3 the roots are exactly t = 1 and t = 2 (2^t - 3^(t-1) = 1 at t = 1, 2,
    and g_3 is strictly convex, so there are no others); g_a'(1) = (1/2) ln(a/4);
    for a = 4 the root t = 1 is double; the second roots for a = 5, 7 are
    0.6509 +- 1e-4 and 0.3735 +- 1e-4; a = 1 has no root other than 1.
B5  Empirical coverage: for a in {5, 7} the number of n <= X reaching 1 under T_a
    (X = 10^3..10^6) grows with fitted exponent strictly below 1, smaller for a = 7
    than for a = 5; for a = 3 every n <= 10^6 reaches 1.
"""
from pathlib import Path
import json, math, sys, time
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []; t0 = time.perf_counter()
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail}); print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)

# B1
ok = True
for n in range(2, 2 ** 20 + 1):
    parents = [p for p in ((n // 2) if n % 2 == 0 else None, (n + 1) // 2 if n % 2 == 1 else None) if p]
    ok &= len(parents) == 1
x_depth_ok = True
depth = [0] * (2 ** 20 + 1)
for n in range(2, 2 ** 20 + 1):
    par = n // 2 if n % 2 == 0 else (n + 1) // 2
    depth[n] = depth[par] + 1 if par != n else 0
    x_depth_ok &= depth[n] == math.ceil(math.log2(n)) if n & (n - 1) else depth[n] == int(math.log2(n))
check("B1 binary tree = inverse tree of T_1", ok and x_depth_ok, "unique parents; depth = ceil(log2 n)")

# B2
def T(x): return (3 * x + 1) / 2 if x.numerator % 2 else x / 2
ok = True; det = {}
for k in (8, 12, 16):
    cls = set(); integral = 0
    for b in range(2 ** k):
        w = [(b >> i) & 1 for i in range(k)]
        A, B = Fr(1), Fr(0)
        for e in w:
            if e: A, B = A * Fr(3, 2), B * Fr(3, 2) + Fr(1, 2)
            else: A, B = A / 2, B / 2
        x = (1 - B) / A; y = x
        for e in w:
            if y.numerator % 2 != e: ok = False; break
            y = T(y)
        ok &= y == 1
        cls.add((x.numerator * pow(x.denominator, -1, 2 ** k)) % 2 ** k)
        if x.denominator == 1 and x > 0: integral += 1
    ok &= len(cls) == 2 ** k and 1.2 <= integral / (4 / 3) ** k <= 1.8
    det[k] = integral
check("B2 two perfect 2-adic transversals", ok, f"positive integral preimages by depth: {det}")

# B3
def parity_bits(n, K):
    x = n; bits = []
    for _ in range(K):
        bits.append(x % 2); x = x // 2 if x % 2 == 0 else (3 * x + 1) // 2
    return bits
def Qrat(n, K, period_hint):
    # rational value of the 2-adic integer whose digits are the parity sequence, using eventual periodicity
    bits = parity_bits(n, K + 4 * period_hint)
    for k in range(K):
        P = period_hint
        if all(bits[j] == bits[j + P] for j in range(k, K + 2 * P)):
            r = sum(b << i for i, b in enumerate(bits[:k]))
            W = sum(b << i for i, b in enumerate(bits[k:k + P]))
            return r + Fr(2 ** k * W, 1 - 2 ** P)
    return None
ok = all(Qrat(n, 700, 2).denominator == 3 for n in range(1, 20001))
q1, q0, q5, q17 = Qrat(-1, 50, 1), Qrat(0, 50, 1), Qrat(-5, 50, 3), Qrat(-17, 200, 11)
ok2 = q1 == -1 and q0 == 0 and q5.denominator == 7 and 2047 % q17.denominator == 0
check("B3 parity charge", ok and ok2, f"Q(n)=a/3 for n<=20000: {ok}; Q(-1)={q1}, Q(0)={q0}, den Q(-5)={q5.denominator}, den Q(-17)={q17.denominator}")

# B4
def g(a, t): return 2 ** (-t) * (1 + a ** (t - 1))
r3 = abs(g(3, 1) - 1) < 1e-15 and abs(g(3, 2) - 1) < 1e-15
conv = all((g(3, t - 1e-3) + g(3, t + 1e-3) - 2 * g(3, t)) > 0 for t in np.linspace(-5, 10, 301))
slopes = all(abs((g(a, 1 + 1e-7) - g(a, 1 - 1e-7)) / 2e-7 - 0.5 * math.log(a / 4)) < 1e-6 for a in (1, 3, 5, 7, 9))
dbl = abs((g(4, 1 + 1e-6) - g(4, 1 - 1e-6)) / 2e-6) < 1e-6
r5 = brentq(lambda t: g(5, t) - 1, 1e-6, 0.9999); r7 = brentq(lambda t: g(7, t) - 1, 1e-6, 0.9999)
a1_only = all(abs(g(1, t) - 1) > 1e-9 for t in np.linspace(-5, 10, 1501) if abs(t - 1) > 1e-3)
ok = r3 and conv and slopes and dbl and abs(r5 - 0.6509) < 1e-4 and abs(r7 - 0.3735) < 1e-4 and a1_only
check("B4 coverage equation roots", ok, f"a=3 roots 1,2: {r3}; convex: {conv}; slope=½ln(a/4): {slopes}; a=4 double: {dbl}; a=5: {r5:.6f}; a=7: {r7:.6f}")

# B5
def reaches1(n, a, cap=10 ** 40, steps=5000):
    x = n
    for _ in range(steps):
        if x == 1: return True
        x = x // 2 if x % 2 == 0 else (a * x + 1) // 2
        if x > cap: return False
    return False
fits = {}
for a in (5, 7):
    Xs = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    cnt = [sum(1 for n in range(1, X + 1) if reaches1(n, a)) for X in Xs]
    fits[a] = (float(np.polyfit(np.log(Xs), np.log(cnt), 1)[0]), cnt)
all3 = all(reaches1(n, 3) for n in range(1, 10 ** 6 + 1))
ok = fits[5][0] < 1 and fits[7][0] < fits[5][0] and all3
check("B5 empirical coverage of the tree of 1", ok, f"a=5 exponent {fits[5][0]:.3f} {fits[5][1]}; a=7 exponent {fits[7][0]:.3f} {fits[7][1]}; a=3 all n<=1e6 reach 1: {all3}")

el = time.perf_counter() - t0; npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s")
(HERE / "cert_collatz_trees_results.json").write_text(json.dumps({"rows": rows, "elapsed_s": el}, indent=2))
sys.exit(0 if npass == len(rows) else 1)
