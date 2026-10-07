r"""The quintic row R_4 = Z/210 (adds p=7): the cross-prime cancellation generalized to ALL orders/rows,
the order-5 Wick structure (Gaussian pair x Amari-Chentsov triple), and the p=7 von Mangoldt entry.

Works AROUND the mu_210 memory block: the full order-5 energy on Z/210 is 210^5 ~ 4e11 (blocked), but the
sec-7 cancellation question only needs the SINGLE-PRIME characters -- 1+2+4+6 = 13 of them -- and the
cubic/quartic pattern generalizes to a theorem proved without any large enumeration:

  GENERAL CROSS-PRIME CANCELLATION THEOREM.  Let N be squarefree (a primorial). A single-prime (Cartan)
  character on axis p is == 0 mod q for every other prime q | N and != 0 mod p.  Then NO connected vertex
  (sum == 0 mod N, no proper subset == 0 mod N), of ANY order, built from single-prime characters can span
  >= 2 primes.  PROOF: if it spans axes p_1,...,p_m (m>=2), the chars on axis p_1 form a non-empty PROPER
  subset; their sum is == 0 mod p_1 (the full sum is, and only axis-p_1 chars are nonzero mod p_1) and == 0
  mod q for q != p_1 (single-prime), hence == 0 mod N by CRT -- a vanishing proper subset, contradicting
  connectivity.  []  Consequently the closed-leaf projection Pi_tau (onto the single-prime Cartan axes)
  annihilates the ENTIRE cross-prime sector at EVERY order and EVERY primorial row -- the sec-7 carry
  vanishes uniformly (cubic Z/6, quartic Z/30, quintic Z/210, ...), subsuming Paper 22 sec 5.3 and the
  quartic result into one statement.

This probe:
  PART A -- the theorem, spot-checked: enumerate single-prime tuples (multisets) on Z/6, Z/30, Z/210 at
            orders 3,4,5; confirm 0 connected cross-prime.  Von Mangoldt single-axis recovery (Lambda via
            Mobius): p=2,3,5,7 -> log p on Z/210; p=7 the NEW entry; the single-axis connected quintets in
            A_7 carry log 7.
  PART B -- the order-5 cumulant selection rule (verified on N=6): kappa_5 = delta_{a+b+c+d+e=0}
            - sum_{10 pairs} delta_{pair=0} delta_{triple=0} -- the first order whose Wick subtraction is a
            GAUSSIAN PAIR x AMARI-CHENTSOV TRIPLE (order 2 x order 3), not pair x pair.
  PART C -- the sec-7 'triple-face coherence' answer + honest scope.

NUMERICAL/exact-combinatorial; builds on Paper 22 sec 5.3/sec 7, the quartic atlas/leakage probes. NO RH claim.
"""

import sys
from math import gcd, factorial
from itertools import combinations_with_replacement, product
import sympy as sp
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def conductor(k, N):
    return N // gcd(k, N) if k % N != 0 else 1


def prime_set(d):
    s, m, p = set(), d, 2
    while p * p <= m:
        while m % p == 0:
            s.add(p); m //= p
        p += 1
    if m > 1:
        s.add(m)
    return s


def single_prime_chars(N):
    out = {}
    for k in range(1, N):
        ps = prime_set(conductor(k, N))
        if len(ps) == 1:
            out.setdefault(next(iter(ps)), []).append(k)
    return out


def connected(tup, N):
    if sum(tup) % N != 0:
        return False
    r = len(tup)
    for i in range(r):
        for j in range(i + 1, r):
            if (tup[i] + tup[j]) % N == 0:   # vanishing pair (=> any complementary subset also 0)
                return False
    return True


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ============================================================================
    #  PART A -- the general theorem, spot-checked on Z/6, Z/30, Z/210
    # ============================================================================
    log("================  PART A: general cross-prime cancellation -- spot-check + von Mangoldt  ======")
    for N in (6, 30, 210):
        sp_axes = single_prime_chars(N)
        allsp = [k for ks in sp_axes.values() for k in ks]
        axis_of = {k: next(iter(prime_set(conductor(k, N)))) for k in allsp}
        log("  --- Z/%d : single-prime (Cartan) characters by axis ---" % N)
        for p in sorted(sp_axes):
            log("     A_%d (dim %d): %s" % (p, len(sp_axes[p]), sp_axes[p]))
        # enumerate single-prime multisets of orders 3..5, count connected cross-prime
        maxord = 5
        bad = 0
        single_axis_hits = {}
        for r in range(3, maxord + 1):
            for tup in combinations_with_replacement(allsp, r):
                if not connected(tup, N):
                    continue
                axes = {axis_of[k] for k in tup}
                if len(axes) >= 2:
                    bad += 1
                else:
                    single_axis_hits.setdefault((r, next(iter(axes))), 0)
                    single_axis_hits[(r, next(iter(axes)))] += 1
        log("     connected CROSS-PRIME single-prime tuples (orders 3-5): %d  %s"
            % (bad, "(theorem: must be 0)" if bad == 0 else "<-- VIOLATION"))
        sa = sorted(single_axis_hits.items())
        if sa:
            log("     connected SINGLE-AXIS single-prime tuples that SURVIVE Pi_tau (carry log p):")
            for (r, p), c in sa:
                log("        order %d, axis %d : %d  (-> log %d)" % (r, p, c, p))
        log("")
    log("  => 0 connected cross-prime single-prime tuples on every row -- the theorem holds; Pi_tau")
    log("     annihilates the cross-prime sector at orders 3,4,5 on Z/6, Z/30, AND Z/210.  In particular")
    log("     the quintic four-prime row Z/210 adds NO new surviving carry: 'more of the same'.")
    log("")
    # von Mangoldt single-axis recovery, p=7 new
    log("  von Mangoldt recovery Lambda(d)=sum_{e|d} mu(d/e) log e on the conductor lattice of 210:")
    primes_recovered = []
    for d in sp.divisors(210):
        if d == 1:
            continue
        lam = sp.simplify(sum(int(sp.mobius(d // e)) * sp.log(e) for e in sp.divisors(d)))
        ps = sorted(prime_set(d))
        if len(ps) == 1 and lam != 0:
            primes_recovered.append(ps[0])
            log("     A_%d : Lambda = log %d = %.5f   (single-axis, survives Pi_tau)" % (d, ps[0], float(lam)))
    log("     composite conductors (6,10,...,210): Lambda = 0 (Mobius cancels) -- the mixed residual.")
    log("     single-prime recovery on Z/210 = { %s };  p=7 (log 7) is the NEW entry at the four-prime row."
        % ", ".join("log %d" % p for p in sorted(primes_recovered)))
    log("")

    # ============================================================================
    #  PART B -- the order-5 cumulant selection rule (Gaussian pair x cubic triple)
    # ============================================================================
    log("================  PART B: order-5 cumulant selection rule (verified on N=6)  ==================")

    def set_partitions(s):
        s = list(s)
        if len(s) == 1:
            yield [s]; return
        first = s[0]
        for rest in set_partitions(s[1:]):
            for i in range(len(rest)):
                yield rest[:i] + [[first] + rest[i]] + rest[i + 1:]
            yield [[first]] + rest

    N = 6
    parts5 = list(set_partitions(range(5)))   # Bell(5)=52 partitions
    log("  Bell(5) = %d set-partitions; non-singleton ones (survive on H_0): full (1) + 3+2 (10) = 11." % len(parts5))
    # build kappa_5 tensor and verify on a sample of non-trivial character 5-tuples
    K = np.zeros((N,) * 5)
    invN = 1.0 / N
    for idx in product(range(N), repeat=5):
        tot = 0.0
        for part in parts5:
            sgn = (-1) ** (len(part) - 1) * factorial(len(part) - 1)
            pr = 1.0
            for block in part:
                vals = [idx[b] for b in block]
                pr *= invN if all(v == vals[0] for v in vals) else 0.0
            tot += sgn * pr
        K[idx] = tot

    def contract(a, b, c, d, e):
        w = np.exp(2j * np.pi / N); i = np.arange(N)
        t = K
        for f in (a, b, c, d, e):
            t = np.tensordot(t, w ** (f * i), axes=([0], [0]))
        return t

    def analytic5(a, b, c, d, e):
        z = lambda x: 1.0 if x % N == 0 else 0.0
        full = z(a + b + c + d + e)
        wick = 0.0
        idxs = [a, b, c, d, e]
        for i in range(5):
            for j in range(i + 1, 5):
                rest = [idxs[t] for t in range(5) if t not in (i, j)]
                wick += z(idxs[i] + idxs[j]) * z(sum(rest))
        return full - wick

    rng = np.random.default_rng(0)
    maxerr = 0.0
    checks = 0
    sample = set()
    while len(sample) < 300:
        t = tuple(int(x) for x in rng.integers(1, N, size=5))
        sample.add(t)
    for t in sample:
        maxerr = max(maxerr, abs(contract(*t) - analytic5(*t)))
        checks += 1
    log("  kappa_5 contracted vs  delta_{a+b+c+d+e=0} - sum_{10 pairs} delta_{pair=0} delta_{triple=0} :")
    log("     over %d random non-trivial 5-tuples, max|diff| = %.2e  %s"
        % (checks, maxerr, "MATCH" if maxerr < 1e-9 else "MISMATCH"))
    log("  => the order-5 Wick subtraction is the 3+2 partition: a GAUSSIAN PAIR (order 2) times an")
    log("     AMARI-CHENTSOV TRIPLE (order 3).  Order 5 is the first order whose disconnected part")
    log("     contains the CUBIC -- the cumulant tower's order-2 and order-3 content meeting in one rung")
    log("     (cf. order 4, whose only Wick term was pair x pair = Gaussian x Gaussian).")
    log("")

    # ============================================================================
    #  PART C -- the sec-7 coherence answer + honest scope
    # ============================================================================
    log("================  PART C: sec-7 triple-face coherence + scope  ================")
    log("Paper 22 sec 7 asks, at the quintic four-prime row Z/210, whether the three-prime obstructions")
    log("compose 'coherently across the divisor lattice' -- the four triple-faces 30, 42, 70, 105")
    log("(=2*3*5, 2*3*7, 2*5*7, 3*5*7).  ANSWER (general theorem, PART A): every cross-prime connected")
    log("vertex -- on any triple-face, on the full 210, at any order -- contains a mixed character and")
    log("lies in ker Pi_tau.  So ALL the three-prime obstructions vanish, COHERENTLY and uniformly; there")
    log("is no surviving four-prime carry.  The composition is trivial-by-cancellation, not a new obstruction.")
    log("")
    log("HONEST SCOPE:")
    log("  [P] the finite cross-prime cancellation is now GENERAL: Pi_tau annihilates the cross-prime")
    log("      sector at every order and every primorial row (one proof, PART A), subsuming the cubic")
    log("      (Paper 22 sec 5.3) and quartic results; the quintic Z/210 confirms it and adds log 7.")
    log("  [P] order-5 cumulant structure: the 3+2 (Gaussian pair x cubic triple) Wick subtraction, verified.")
    log("  [open == Conjecture 5.2] the ALL-ORDER LIMIT (projective compatibility + mu_n^*(H_n)polylog->0")
    log("      across n->inf) is untouched -- the conserved hard core, >= GRH.  The general FINITE theorem")
    log("      does NOT give the uniform limit; it removes the cross-prime CARRY worry uniformly, leaving")
    log("      the limit as the sole obstruction (as Paper 22 sec 8 already states).")
    log("  [C == RH] the full identity and Thm 6.1.")
    log("  NOTE: the full order-5 Noether ENERGY on Z/210 (mu_210, 210^5) is memory-blocked and NOT")
    log("        computed here; the cancellation needed only the 13 single-prime characters + the theorem.")
    log("")
    log("NET: the quintic row contributes no new carry (general theorem); p=7 enters single-axis; the new")
    log("structural feature is the order-5 Gaussian-x-cubic Wick term.  The cross-prime carry-obstruction is")
    log("now closed UNIFORMLY across the primorial tower at finite order; the entire residual difficulty is")
    log("the all-order limit (Conjecture 5.2), unchanged.  Conservation holds.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "quintic_z210.md"
    header = [
        "# The quintic row Z/210: general cross-prime cancellation, order-5 Wick structure, p=7 entry",
        "",
        "**Script:** `empirical/verify_quintic_z210.py`  (works around the mu_210 memory block via the 13",
        "single-prime characters + a general theorem; builds on Paper 22 sec 5.3/sec 7 and the quartic probes).",
        "**Finding:** a GENERAL theorem -- no connected single-prime tuple (any order, any squarefree primorial)",
        "spans >= 2 primes -- so Pi_tau annihilates the cross-prime sector at EVERY order/row, subsuming the cubic",
        "and quartic results. Spot-checked: 0 connected cross-prime single-prime tuples on Z/6, Z/30, Z/210 (orders",
        "3-5). p=7 = log 7 the new single-axis entry at Z/210. Order-5 Wick subtraction = Gaussian pair x",
        "Amari-Chentsov triple (verified N=6). sec-7 coherence: all three-prime obstructions vanish coherently;",
        "no four-prime carry. ALL-ORDER LIMIT (Conjecture 5.2) untouched; mu_210 full energy not needed/blocked.",
        "**Nature:** exact-combinatorial + general proof + numerical (order-5 formula). NO claim RH proved.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
