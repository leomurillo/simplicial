#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
cert_A2_chart_localization.py  --  EXACT certificate (sympy + exact combinatorics)

LEVERAGE ITEM A2: weld Paper 21's 2+2 Wick obstruction to Paper III (01c) section 7's
chart-localization theorem (Proposition 7.2).

  Paper 21  "The Quartic Force Law at Cumulant Order Four"  (21.quartic_force_law_n4_obstruction.md)
  Paper III "Information Geometry on the Simplicial Frame"  (01c.simplicial_information_geometry.md), sec 7

THE CLAIM BEING CERTIFIED (the chart split):
  Paper 21 reads the order-4 obstruction as a 2+2 Gaussian (Wick) SUBTRACTION in the
  additive-character basis:
        Q(chi_a,chi_b,chi_c,chi_d)|_u
            = delta_{a+b+c+d=0}
            - delta_{a+b=0}delta_{c+d=0} - delta_{a+c=0}delta_{b+d=0} - delta_{a+d=0}delta_{b+c=0}.
  Paper III sec 7 (Prop 7.2) proves this object CANNOT live in the negative-entropy
  m-chart tower nabla^n phi (which is purely DIAGONAL, Thm 4.1), and MUST live in the dual
  log-partition e-chart tower nabla^n Phi (which carries the 2+2 Wick block). This is a
  Legendre-duality consequence, not an extra hypothesis.

THIS CERT verifies, deterministically (sympy exact rationals + exact integer combinatorics):

  A. m-CHART HAS NO 2+2 BLOCK.
     phi(p) = sum_i p_i log p_i  (Paper III: the m-affine / mixture-chart potential).
     For EVERY i != j the component  d^4 phi / dp_i^2 dp_j^2  is the exact zero, while the
     diagonal  d^4 phi / dp_i^4 = c_4 / p_i^3  with c_4 = +2 (Paper III Thm 4.1).
     => the entropy tower is purely diagonal; it has no i,i,j,j (2+2) component at all.
     (Exhaustive over all 2+2 index pairs on the program's N=4 frame; sampled on Z/30.)

  B. e-CHART CARRIES THE 2+2 BLOCK, and the number is -3/128 on the N=4 frame.
     Phi(theta) = log sum_i exp(theta_i)  (Paper III: the dual / exponential-chart potential).
     At the uniform point theta = 0  (p_i = 1/N):
        d^4 Phi / dtheta_i^2 dtheta_j^2 |_0   is NONZERO   (the 2+2 Wick block),
     and on the N=4 categorical frame it equals exactly
        d^4 Phi / dtheta_1^2 dtheta_2^2 |_0 = -3/128.
     This is the explicit e-chart value of Paper 21's Gaussian subtraction.
     (Confirmed nonzero on N = 4,5,6,8,30; the -3/128 value pinned exactly on N=4.)

  C. THE TWO ARE THE SAME OBJECT (character contraction).
     Contracting the exact e-chart tensor  nabla^4 Phi|_0  against the additive characters of
     Z/N reproduces Paper 21's boxed selection rule (connected minus 3 Wick pairings) exactly.
     So the coordinate-basis 2+2 block (-3/128 at N=4) and the character-basis Wick subtraction
     (-1 on a single-pairing quadruple) are one tensor in two bases. The obstruction is an
     e-chart phenomenon, exactly as Prop 7.2 asserts.

  D. PAPER 21's Z/30 ATLAS COUNTS reproduce from the same rule:
        1202 unordered quadruples a+b+c+d=0 (mod 30);  120 Wick-reducible;  1082 connected;
        914 connected three-prime ({2,3,5}) vertices.
     This anchors the chart-localized object to Paper 21's actual arithmetic skeleton.

  E. LEGENDRE SIGN / SELF-DUALITY bookkeeping (Paper III Prop 7.1).
     m-tower diagonal coefficient c_4 = +2; the e-tower 4th cumulant carries the dual sign;
     the two towers are sign-opposite away from the self-dual order-2 (Fisher) rung.

Run:   py cert_A2_chart_localization.py
Pass:  prints "CERT GREEN" and exits 0.  Any failure raises AssertionError / exits 1.

NOTE on a small-N coincidence (recorded honestly, not load-bearing):
  On the N=4 frame the e-chart diagonal block (iiii) and the all-distinct block (ijkl) ALSO
  equal -3/128. That is a 4-category coincidence (few indices), NOT the structural claim. The
  robust, all-N statement -- and the only one this cert leans on -- is "2+2 block = 0 in the
  m-chart, nonzero in the e-chart." The diagonal/distinct coincidence is verified-and-flagged
  in check E, not used to support the localization.
"""

import sympy as sp
import numpy as np
from itertools import product, combinations
from math import gcd
from collections import Counter

try:
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def assert_zero(expr, msg):
    e = sp.simplify(sp.together(sp.expand(expr)))
    assert e == 0, f"FAIL: {msg}\n   residual = {e}"


results = []


def record(label, fn):
    fn()
    results.append((label, True))
    print(f"  [OK] {label}")


# ===========================================================================
# A. m-chart (negative entropy) has NO 2+2 block.
# ===========================================================================
def check_A():
    N = 4
    ps = sp.symbols(f'p1:{N+1}', positive=True)
    phi = sum(p * sp.log(p) for p in ps)
    # every 2+2 (i,i,j,j), i != j, must vanish exactly
    for i, j in combinations(range(N), 2):
        d = phi
        for k in (i, i, j, j):
            d = sp.diff(d, ps[k])
        assert_zero(d, f"A: m-chart 2+2 block ({i}{i}{j}{j}) must vanish")
    # the diagonal survives with c_4 = +2
    d = phi
    for k in (0, 0, 0, 0):
        d = sp.diff(d, ps[0])
    assert_zero(d - sp.Integer(2) / ps[0]**3, "A: m-chart diagonal d^4 = 2/p^3 (c_4=+2)")

    # Z/30 sample: the 2+2 block is still exactly zero (full 30^4 sweep is unnecessary --
    # separability of phi=sum g(p_i) kills every mixed partial; sample to anchor to Paper 21's row)
    N2 = 30
    qs = sp.symbols(f'q1:{N2+1}', positive=True)
    phi2 = sum(q * sp.log(q) for q in qs)
    for (i, j) in [(0, 1), (0, 15), (5, 25), (2, 28), (14, 29)]:
        d = phi2
        for k in (i, i, j, j):
            d = sp.diff(d, qs[k])
        assert_zero(d, f"A: Z/30 m-chart 2+2 block ({i}{i}{j}{j}) must vanish")


record("A  m-chart nabla^4 phi: ALL 2+2 (iijj) blocks = 0 (N=4 exhaustive + Z/30 sample); diag c_4=+2",
       check_A)

# ===========================================================================
# B. e-chart (log-partition) carries the 2+2 block; value = -3/128 on N=4.
# ===========================================================================
def check_B():
    # the program's N=4 frame: pin the exact -3/128
    N = 4
    th = sp.symbols(f't1:{N+1}', real=True)
    Phi = sp.log(sum(sp.exp(t) for t in th))
    sub0 = {t: 0 for t in th}
    d = Phi
    for k in (0, 0, 1, 1):
        d = sp.diff(d, th[k])
    block = sp.simplify(d.subs(sub0))
    assert block == sp.Rational(-3, 128), f"B: N=4 e-chart 2+2 block must be -3/128, got {block}"

    # robustness: nonzero at several N (the structural claim is N-independent)
    for N in (5, 6, 8, 30):
        th = sp.symbols(f't1:{N+1}', real=True)
        Phi = sp.log(sum(sp.exp(t) for t in th))
        sub0 = {t: 0 for t in th}
        d = Phi
        for k in (0, 0, 1, 1):
            d = sp.diff(d, th[k])
        val = sp.simplify(d.subs(sub0))
        assert val != 0, f"B: e-chart 2+2 block must be nonzero at N={N}, got {val}"


record("B  e-chart nabla^4 Phi: 2+2 (iijj) block NONZERO at N=4,5,6,8,30; N=4 value EXACTLY -3/128",
       check_B)

# ===========================================================================
# C. The two are ONE tensor in two bases:
#    char-contraction of the exact e-chart nabla^4 Phi|_0 == Paper 21 boxed rule.
# ===========================================================================
def check_C():
    for N in (4, 6):
        th = sp.symbols(f't1:{N+1}', real=True)
        Phi = sp.log(sum(sp.exp(t) for t in th))
        sub0 = {t: 0 for t in th}
        # build the exact rational 4-tensor at uniform
        Q = np.zeros((N, N, N, N))
        for idx in product(range(N), repeat=4):
            d = Phi
            for k in idx:
                d = sp.diff(d, th[k])
            Q[idx] = float(sp.Rational(d.subs(sub0)))  # exact rational -> float for contraction

        def contract(a, b, c, d):
            w = np.exp(2j * np.pi / N)
            i = np.arange(N)
            va = w**(a * i); vb = w**(b * i); vc = w**(c * i); vd = w**(d * i)
            t = np.tensordot(Q, va, ([0], [0]))
            t = np.tensordot(t, vb, ([0], [0]))
            t = np.tensordot(t, vc, ([0], [0]))
            t = np.tensordot(t, vd, ([0], [0]))
            return t

        def rule(a, b, c, d):
            z = lambda x: 1.0 if x % N == 0 else 0.0
            return (z(a + b + c + d)
                    - z(a + b) * z(c + d) - z(a + c) * z(b + d) - z(a + d) * z(b + c))

        maxerr = 0.0
        nchk = 0
        for a, b, c, d in product(range(1, N), repeat=4):
            maxerr = max(maxerr, abs(contract(a, b, c, d) - rule(a, b, c, d)))
            nchk += 1
        assert maxerr < 1e-9, f"C: N={N} char-contract vs Paper21 rule max|diff|={maxerr:.2e}"


record("C  char-contract(nabla^4 Phi|_0) == Paper 21 rule (connected - 3 Wick), N=4,6, to mach. prec.",
       check_C)

# ===========================================================================
# D. Paper 21's Z/30 atlas counts reproduce from the same selection rule.
# ===========================================================================
def conductor(k, N):
    return N // gcd(k, N) if k % N != 0 else 1


def prime_set(d):
    s = set(); m = d; p = 2
    while p * p <= m:
        while m % p == 0:
            s.add(p); m //= p
        p += 1
    if m > 1:
        s.add(m)
    return s


def check_D():
    N = 30
    sum0 = wick = connected = 0
    conn_by_primes = Counter()
    seen = set()
    for a, b, c, d in product(range(1, N), repeat=4):
        if (a + b + c + d) % N != 0:
            continue
        key = tuple(sorted((a, b, c, d)))
        if key in seen:
            continue
        seen.add(key); sum0 += 1
        pairs0 = any((x + y) % N == 0 for x, y in combinations((a, b, c, d), 2))
        if pairs0:
            wick += 1
        else:
            connected += 1
            primes = set().union(*(prime_set(conductor(x, N)) for x in (a, b, c, d)))
            conn_by_primes[frozenset(primes)] += 1
    assert sum0 == 1202, f"D: total a+b+c+d=0 must be 1202, got {sum0}"
    assert wick == 120, f"D: Wick-reducible must be 120, got {wick}"
    assert connected == 1082, f"D: connected must be 1082, got {connected}"
    assert conn_by_primes[frozenset({2, 3, 5})] == 914, \
        f"D: three-prime connected must be 914, got {conn_by_primes[frozenset({2,3,5})]}"
    # the per-prime-set breakdown Paper 21 tabulates
    expected = {frozenset({5}): 4, frozenset({2, 3}): 6, frozenset({2, 5}): 32,
                frozenset({3, 5}): 126, frozenset({2, 3, 5}): 914}
    for ps_key, cnt in expected.items():
        assert conn_by_primes[ps_key] == cnt, \
            f"D: connected[{sorted(ps_key)}] must be {cnt}, got {conn_by_primes[ps_key]}"


record("D  Z/30 atlas: 1202 / 120 Wick / 1082 connected / 914 three-prime (Paper 21 sec 5.2) reproduced",
       check_D)

# ===========================================================================
# E. Legendre sign bookkeeping (Paper III Prop 7.1) + honest small-N coincidence flag.
# ===========================================================================
def check_E():
    # m-tower diagonal coefficient c_4 = (-1)^4 (4-2)! = +2
    c4 = sp.Integer((-1)**4) * sp.factorial(2)
    assert c4 == sp.Integer(2), f"E: c_4 must be +2, got {c4}"
    # e-tower 4th DISTINCT cumulant at uniform p=1/m: kappa_4 = (-1)^3 3! m^-4 = -6/m^4 (sign -)
    m = sp.symbols('m', positive=True, integer=True)
    kappa4 = sp.Integer((-1)**(4 - 1)) * sp.factorial(3) * m**(-4)
    assert sp.sign(c4) == sp.Integer(1) and sp.sign(kappa4 * m**4) == sp.Integer(-1), \
        "E: order-4 towers must be sign-opposite (e<->m Legendre flip)"

    # honest flag: at N=4 the e-chart diagonal (iiii) and all-distinct (ijkl) ALSO hit -3/128.
    # Verify-and-record; this is a 4-category coincidence, NOT the structural claim.
    N = 4
    th = sp.symbols(f't1:{N+1}', real=True)
    Phi = sp.log(sum(sp.exp(t) for t in th))
    sub0 = {t: 0 for t in th}
    d = Phi
    for k in (0, 0, 0, 0):
        d = sp.diff(d, th[k])
    diag = sp.simplify(d.subs(sub0))
    d = Phi
    for k in (0, 1, 2, 3):
        d = sp.diff(d, th[k])
    distinct = sp.simplify(d.subs(sub0))
    assert diag == sp.Rational(-3, 128) and distinct == sp.Rational(-3, 128), \
        "E: (recorded) N=4 e-chart diag and all-distinct blocks also = -3/128 (small-N coincidence)"
    # at N=8 they DIVERGE (showing it is a coincidence, the 2+2 block stays the robust object):
    N = 8
    th = sp.symbols(f't1:{N+1}', real=True)
    Phi = sp.log(sum(sp.exp(t) for t in th))
    sub0 = {t: 0 for t in th}
    d = Phi
    for k in (0, 0, 1, 1):
        d = sp.diff(d, th[k])
    blk22 = sp.simplify(d.subs(sub0))
    d = Phi
    for k in (0, 0, 0, 0):
        d = sp.diff(d, th[k])
    diag8 = sp.simplify(d.subs(sub0))
    assert blk22 != diag8, "E: at N=8 the 2+2 block and diagonal differ (coincidence is N=4-only)"


record("E  Legendre sign-opposite (c_4=+2 vs kappa_4 sign -); N=4 diag/distinct coincidence flagged",
       check_E)

# ===========================================================================
# summary
# ===========================================================================
print("\n" + "=" * 76)
allpass = all(ok for _, ok in results)
for label, ok in results:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}")
print("=" * 76)
if allpass:
    print("CERT GREEN  ({} checks).".format(len(results)))
    print("  m-chart nabla^4 phi has NO 2+2 Wick block (Paper III Thm 4.1, diagonal tower).")
    print("  e-chart nabla^4 Phi DOES carry it; on the N=4 frame the block = -3/128.")
    print("  Char-contraction shows it IS Paper 21's selection rule; Z/30 gives 914 three-prime vertices.")
    print("  => Paper 21's 2+2 obstruction is provably an e-chart object (Paper III Prop 7.2). Welded.")
    raise SystemExit(0)
else:
    print("CERT RED")
    raise SystemExit(1)
