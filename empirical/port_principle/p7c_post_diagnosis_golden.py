"""
Port Principle — P7c: POST-DIAGNOSIS check for P7.H7b(ii) (NOT BLIND; written after the H7b verdict).

What happened. P7.H7b(ii) pre-registered "every golden local exponent ln n*/ln(1/delta) in [0.42, 0.58] for delta in
1e-3..1e-70". At delta = 1e-3, n* = 55 = F_10 and ln 55 / ln 1000 = 0.5801 > 0.58. Verdict RETAINED (H7b FAIL).
The same mis-calibration as P7.H7a/A6: a pointwise local-exponent window at finite delta cannot absorb the constant in
n* ~ C delta^(-1/2) (here C = 55 * 10^-1.5 = 1.74 gives 0.5 + ln 1.74 / ln 1000 = 0.580).

What this file tests (the theorem-level claim, written before running this file):
    K7c'a [exact]: for golden spacing, n* delta^(1/2) stays in [0.3, 3] for every delta = 10^-3 .. 10^-70 (step 0.25)
          (bounded constant: n* is exactly a Fibonacci number by Proposition 6.8(c)).
    K7c'b [exact]: the local exponent converges: |ln n*/ln(1/delta) - 1/2| <= 0.01 for every delta <= 1e-40.
    L: any failure.
LESSON (for later pre-registrations): state asymptotic claims as bounded-constant tests (n* delta^(1/r) in a band) or
as slopes over a range, never as pointwise local-exponent windows at finite delta.
"""
import sys, math
from fractions import Fraction as F
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def simplest(below_lo, above_hi):
    lp, lq, rp, rq = 0, 1, 1, 0
    while True:
        mp_, mq = lp + rp, lq + rq
        if below_lo(mp_, mq):
            k = 1
            while below_lo(lp + 2 * k * rp, lq + 2 * k * rq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if below_lo(lp + mid * rp, lq + mid * rq): lo_k = mid
                else: hi_k = mid
            lp, lq = lp + lo_k * rp, lq + lo_k * rq
        elif above_hi(mp_, mq):
            k = 1
            while above_hi(rp + 2 * k * lp, rq + 2 * k * lq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if above_hi(rp + mid * lp, rq + mid * lq): lo_k = mid
                else: hi_k = mid
            rp, rq = rp + lo_k * lp, rq + lo_k * lq
        else:
            return mp_, mq

# golden x = 1/phi as a deep convergent (same construction as P7)
p0, q0, p1, q1 = 1, 0, 0, 1
for _ in range(400):
    p0, q0, p1, q1 = p1, q1, p1 + p0, q1 + q0
x = F(p1, q1)
okA, okB, Cs, worst = True, True, [], 0.0
k = 3.0
while k <= 70.0 + 1e-9:
    dl = F(mp.nstr(mp.mpf(10) ** (-mp.mpf(k)), 40)); hi = x * (1 + dl)
    a, b, c, d = x.numerator, x.denominator, hi.numerator, hi.denominator
    kk, m = simplest(lambda P, Q: P * b <= Q * a, lambda P, Q: P * d >= Q * c)
    n = max(kk, m)
    C = n * 10 ** (-k / 2); Cs.append(C); okA &= 0.3 <= C <= 3
    if k >= 40: e = math.log(n) / (k * math.log(10)); worst = max(worst, abs(e - 0.5)); okB &= abs(e - 0.5) <= 0.01
    k += 0.25
check("H7c'.K7c'a [exact] golden: n* delta^(1/2) bounded in [0.3, 3] for delta 1e-3..1e-70", okA, f"range [{min(Cs):.3f}, {max(Cs):.3f}]")
check("H7c'.K7c'b [exact] golden local exponent within 0.01 of 1/2 for delta <= 1e-40", okB, f"max deviation {worst:.4f}")
print(f"\nP7c: {sum(res)}/{len(res)} PASS")
