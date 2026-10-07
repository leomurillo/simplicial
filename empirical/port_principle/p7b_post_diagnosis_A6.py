"""
Port Principle — P7b: POST-DIAGNOSIS check for P7.H7a / case A6 (NOT BLIND; written after the A6 verdict).

What happened. P7.H7a pre-registered "every local exponent ln n*/ln(1/delta) <= 0.60 for delta in 1e-2..1e-7" for a
very well approximable spectrum E' = (1, 1+xL, 2) with u' = (3/10, -7/10, 9/20) (entropy that sees the resonant
kernel K = Z(2,0,-1)). The measured maximum was 0.604 (n* = 10723 at delta = 1e-7). That verdict is RETAINED.

Diagnosis. Theorem 6.9(b) claims n* <= C delta^(-1/2) with a constant C that depends on the spectrum only through
fixed data (a section of L, a kernel vector k0, k0.u'), NOT on any Diophantine property. A local-exponent ceiling of
0.60 at delta = 1e-7 tolerates only C <= 10^0.7 ~ 5; the proof's constant for this spectrum is ~47. The pre-registered
ceiling conflated the asymptotic exponent with finite-delta local exponents.

What this file tests (the theorem's actual claim, written before running this file):
    K7b'a [exact]: the proof's constructive exchange a = s(b) + t k0 (b from the largest convergent of xL not
          exceeding H = ceil(delta^-1/2); t the least admissible integer) VIOLATES passivity exactly
          (a.E' < 0 < a.E' + delta a.u') at every delta = 10^-2 .. 10^-30 (step 0.25).
    K7b'b [exact]: its cost (sum c+) times delta^(1/2) stays <= 47.1, the constant obtained from the proof's crude
          bounds for this spectrum, at every such delta.
    K7b'c [exact]: on the P7 range (delta = 1e-2 .. 1e-7) the scanned minimum n* (from p7_run logs, hard-coded below)
          never exceeds the constructive cost.
    L: any failure.
"""
import sys, math
from fractions import Fraction as F
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 50
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def cf_value(cf):
    p0, q0, p1, q1 = 1, 0, cf[0], 1
    convs = [(cf[0], 1)]
    for a in cf[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        convs.append((p1, q1))
    return F(p1, q1), convs
cfL = [0, 2]
while True:
    _, cv = cf_value(cfL)
    if cv[-1][1] > 10 ** 220: break
    cfL.append(cv[-1][1] ** 2)
xL, convL = cf_value(cfL)                       # same xL as P7

E = [F(1), 1 + xL, F(2)]
u = [F(3, 10), F(-7, 10), F(9, 20)]
k0 = (2, 0, -1)                                 # kernel vector, k0.E = 0, k0.u = 3/20 > 0
assert sum(a * e for a, e in zip(k0, E)) == 0
ku = sum(a * x for a, x in zip(k0, u)); assert ku == F(3, 20)
def cost(a):
    c = [-sum(a)] + list(a)
    return sum(x for x in c if x > 0)

def construct(delta):
    H = int(mp.ceil(1 / mp.sqrt(mp.mpf(delta.numerator) / delta.denominator)))
    p, q = max(((p, q) for p, q in convL if 1 <= q <= H), key=lambda t: t[1])
    b1, b2 = -p, q                              # b.omega = b1 + b2 xL  (omega = (1, xL))
    if b1 + b2 * xL > 0: b1, b2 = -b1, -b2
    bw = b1 + b2 * xL
    assert bw < 0
    s = (b1 - b2, b2, 0)                        # section: s(b).E = (b1 - b2) + b2 (1 + xL) = b1 + b2 xL
    su = sum(a * x for a, x in zip(s, u))
    t = math.floor((-bw / delta - su) / ku) + 1
    a = tuple(si + t * ki for si, ki in zip(s, k0))
    aE = sum(x * e for x, e in zip(a, E)); au = sum(x * y for x, y in zip(a, u))
    return a, aE < 0 < aE + delta * au

okA, okB, worst = True, True, 0.0
consts = {}
k = 2.0
while k <= 30.0 + 1e-9:
    delta = F(mp.nstr(mp.mpf(10) ** (-mp.mpf(k)), 40))
    a, viol = construct(delta)
    okA &= viol
    C = cost(a) * math.sqrt(float(delta))
    worst = max(worst, C); okB &= C <= 47.1
    consts[round(k, 2)] = (cost(a), round(C, 3))
    k += 0.25
check("H7b'.K7b'a [exact] the constructive exchange of Theorem 6.9(b) violates passivity at every delta 1e-2..1e-30", okA)
check("H7b'.K7b'b [exact] constructive cost * delta^(1/2) <= 47.1 (the proof's constant) throughout", okB,
      f"max observed {worst:.2f}")
p7_scan = [9, 9, 9, 9, 9, 9, 9, 9, 61, 203, 455, 740, 740, 740, 740, 740, 1471, 2761, 4395, 7319, 10723]   # P7 A6, delta = 10^-2..10^-7 step 0.25
okC = all(n <= consts[round(2.0 + 0.25 * i, 2)][0] for i, n in enumerate(p7_scan))
check("H7b'.K7b'c [exact] scanned minimum n* never exceeds the constructive cost on the P7 range", okC)
for kk in [2.0, 4.75, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0]:
    print(f"   delta=1e-{kk}: constructive cost {consts[kk][0]}, cost*delta^(1/2) = {consts[kk][1]}")
print(f"\nP7b: {sum(res)}/{len(res)} PASS")
