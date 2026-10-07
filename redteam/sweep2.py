"""Sweep 2: try to make f(p_i) close to a moment-friendly sequence.
Key idea: AP ratios c_i = a+b*i give moment seqs (Gamma/Pochhammer).
Geometric ratios c_i = r give moment seqs (b_n = r^n, a point mass).
So we WANT f(p_i) ~ AP or ~ const or ~ smooth. Primes are irregular;
can a polynomial 'undo' the irregularity over the relevant window?"""
from search import full_psd_failure, poly_from_coeffs, valid_on_primes, first_leading_failure
from sympy import primerange, Integer, Rational, nsimplify
import itertools

P = list(primerange(2, 100000))

# Strategy A: high-degree leading term dominates -> ratios c_i ~ (p_i)^d which is
#   super-irregular. Strategy B: try f with a large additive constant to flatten?
#   Prompt says large additive const makes N* SMALLER. So go the OTHER way:
#   make f(p) GROW so the ratio sequence is dominated by leading term?
#   That doesn't help either. Let's just brute many shapes and track N*.

Nmax = 7
cands = []

# Products of two quadratics / linear*cubic etc, monic
# (p + r1)(p + r2): degree 2, already covered. Try (p^2+a)(p^2+b) style:
for a in range(-3, 10):
    for b in range(a, 10):
        # (p^2+a)(p^2+b) = p^4 + (a+b)p^2 + ab
        cands.append((f"(p^2+{a})(p^2+{b})", [1, 0, a+b, 0, a*b]))

# (p+r)^d : f(p_i) = (p_i+r)^d, ratio = ((p_i+r)/(p_{i-1}... no, ratio c_i=(p_i+r)^d
for r in range(-1, 8):
    for d in range(2, 7):
        coeffs = [Integer(0)]*(d+1)
        # expand (p+r)^d
        from sympy import symbols, expand, Poly, Symbol
        p = Symbol('p')
        pol = expand((p+r)**d)
        c = Poly(pol, p).all_coeffs()
        cands.append((f"(p+{r})^{d}", [int(x) for x in c]))

# scale-free: f(p) = p^2 + a p + b with a,b chosen so f(2),f(3),f(5)... near AP
for a in range(-3, 5):
    for b in range(-3, 12):
        cands.append((f"q2 {a},{b}", [1, a, b]))

print(f"candidates: {len(cands)}")
results = []
for name, coeffs in cands:
    if not valid_on_primes(coeffs):
        continue
    f = poly_from_coeffs(coeffs)
    N, d = first_leading_failure(f, Nmax)
    results.append((name, coeffs, N, d))

surv = [r for r in results if r[2] is None]
print("survivors:", len(surv))
for s in surv[:30]:
    print("  SURVIVOR:", s[0], s[1])

from collections import Counter
dist = Counter(r[2] for r in results if r[2] is not None)
print("N* dist:", dict(sorted(dist.items())))
results.sort(key=lambda r: (r[2] is not None, r[2] if r[2] is not None else 1e9))
print("max N* examples:")
for r in results[:12]:
    print(f"  N*={r[2]} {r[0]} coeffs={r[1]}")
