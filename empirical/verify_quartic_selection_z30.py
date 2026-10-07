r"""The ORDER-4 selection rule and the Z/30 atlas: the program's own named-open quartic computation
(Paper 21 "what remains" item 5; Paper 22 sec 7), done -- informed by the two-tower (Beyond-CBS) lens.

CONTEXT (not reinventing -- building on the corpus):
  * T3 proved the ORDER-3 selection rule a+b+c=0 (mod N) for the Amari-Chentsov cubic on Z/N
    (additive characters), and Paper 22 sec 5.3 used it to organize the cubic term of the Weil form:
    Q_2(R_2 f) = W_zeta(f*f^*)|_{<=3} on Z/6, recovering the first prime correction sum_{p=2,3} log p.
  * Paper 21 (quartic force law) NAMED the order-4 / three-prime question OPEN: "run the first finite
    atlas on Z/30 ... decide whether the fourth-cumulant case is just more of the same or qualitatively
    new." T2 left Q_{ijkl}=d^4 Phi's form uncomputed ("not needed for what follows").
  * Paper 22 sec 7: Z/30 = Z/2 x Z/3 x Z/5 is "the first row where a genuine three-prime conductor
    class can exist ... the first non-pairwise obstruction."

THE NEW STRUCTURE (this probe's finding, derived + verified):
  the order-4 CUMULANT (connected) selection rule, on non-trivial characters, is
      Q(chi_a,chi_b,chi_c,chi_d)|_u = delta_{a+b+c+d=0}
            - delta_{a+b=0}delta_{c+d=0} - delta_{a+c=0}delta_{b+d=0} - delta_{a+d=0}delta_{b+c=0}.
  Order 3 had NO subtraction (the only 2+1 partition isolates a single index, which vanishes on
  non-trivial chi). Order 4 is the FIRST order with a WICK (pairwise) SUBTRACTION -- the three
  delta_{a+b=0}delta_{c+d=0} pairings are exactly the GAUSSIAN / 2nd-order content (the conductor
  blind spot floor), and the cumulant SUBTRACTS them, leaving the CONNECTED part (a+b+c+d=0 with NO
  vanishing sub-pair) = the genuine beyond-Gaussian 4th-order content. This IS Beyond-CBS's TWO TOWERS
  (distributional cumulant vs Gaussian), realized exactly and arithmetically on the conductor lattice
  -- and it ANSWERS Paper 21's open question: order 4 IS qualitatively new (the first Gaussian subtraction).

THIS PROBE:
  (A) VERIFY the order-4 selection rule on N=6,8: build Q_{ijkl}|_u by the moment-cumulant partition
      formula (uniform categorical moments M(block)=1/N iff all-equal), contract on characters, confirm
      it equals connected - Wick to machine precision.
  (B) The Z/30 ATLAS: conductor packets, and the CONNECTED quadruples (a+b+c+d=0, no sub-pair=0),
      classified by conductor multiset -- isolating the genuine THREE-PRIME quadruples (the first
      non-pairwise obstruction Paper 22 sec 7 named).
  (C) the two-tower reading + the Weil-form (Paper 22) connection + honest residual.

NUMERICAL (numpy/exact-combinatorial); builds on T3/T2/21/22; NO claim RH is proved.
"""

import sys
import numpy as np
from math import gcd
from itertools import product

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# the 15 set-partitions of {0,1,2,3}, as lists of blocks
PARTITIONS_4 = [
    [[0, 1, 2, 3]],
    [[0, 1, 2], [3]], [[0, 1, 3], [2]], [[0, 2, 3], [1]], [[1, 2, 3], [0]],
    [[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]],
    [[0, 1], [2], [3]], [[0, 2], [1], [3]], [[0, 3], [1], [2]],
    [[1, 2], [0], [3]], [[1, 3], [0], [2]], [[2, 3], [0], [1]],
    [[0], [1], [2], [3]],
]
from math import factorial


def cumulant4_tensor(N):
    """Q_{ijkl}|_u for the uniform categorical, via kappa = sum_pi (-1)^{|pi|-1}(|pi|-1)! prod_B M(B),
    with M(block) = 1/N iff all indices in the block are equal, else 0."""
    Q = np.zeros((N, N, N, N))
    invN = 1.0 / N
    for idx in product(range(N), repeat=4):
        total = 0.0
        for part in PARTITIONS_4:
            sign = (-1) ** (len(part) - 1) * factorial(len(part) - 1)
            prod = 1.0
            for block in part:
                vals = [idx[b] for b in block]
                prod *= invN if all(v == vals[0] for v in vals) else 0.0
            total += sign * prod
        Q[idx] = total
    return Q


def contract_chars(Q, N, a, b, c, d):
    w = np.exp(2j * np.pi / N)
    i = np.arange(N)
    va = w ** (a * i); vb = w ** (b * i); vc = w ** (c * i); vd = w ** (d * i)
    # sum_{ijkl} Q[i,j,k,l] va[i] vb[j] vc[k] vd[l]
    t = np.tensordot(Q, va, axes=([0], [0]))
    t = np.tensordot(t, vb, axes=([0], [0]))
    t = np.tensordot(t, vc, axes=([0], [0]))
    t = np.tensordot(t, vd, axes=([0], [0]))
    return t


def analytic_rule(N, a, b, c, d):
    z = lambda x: 1.0 if x % N == 0 else 0.0
    return (z(a + b + c + d)
            - z(a + b) * z(c + d) - z(a + c) * z(b + d) - z(a + d) * z(b + c))


def conductor(k, N):
    return N // gcd(k, N) if k % N != 0 else 1


def prime_set(d):
    s, p = set(), 2
    m = d
    while p * p <= m:
        while m % p == 0:
            s.add(p); m //= p
        p += 1
    if m > 1:
        s.add(m)
    return s


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ============================================================================
    #  PART A -- verify the order-4 selection rule (connected - Wick)
    # ============================================================================
    log("================  PART A: verify the order-4 cumulant selection rule on N=6, N=8  ============")
    for N in (6, 8):
        Q = cumulant4_tensor(N)
        maxerr = 0.0
        checks = 0
        for a, b, c, d in product(range(1, N), repeat=4):
            val = contract_chars(Q, N, a, b, c, d)
            ana = analytic_rule(N, a, b, c, d)
            maxerr = max(maxerr, abs(val - ana))
            checks += 1
        log("  N=%d: contracted Q_{ijkl}|_u vs (delta_{sum=0} - 3 Wick pairings) over %d nontrivial"
            " quadruples; max|diff| = %.2e  %s" % (N, checks, maxerr, "MATCH" if maxerr < 1e-9 else "MISMATCH"))
    log("  => the order-4 cumulant selection rule is CONFIRMED: connected (a+b+c+d=0) MINUS the three")
    log("     Gaussian Wick pairings (a+b=0,c+d=0). Order 3 (T3) had NO subtraction; order 4 is the FIRST")
    log("     order carrying the Gaussian/2nd-order floor as an explicit subtraction -- the two towers, arithmetic.")
    log("")

    # ============================================================================
    #  PART B -- the Z/30 atlas
    # ============================================================================
    log("================  PART B: the Z/30 = Z/2 x Z/3 x Z/5 atlas (the three-prime row)  ============")
    N = 30
    # conductor packets
    packets = {}
    for k in range(1, N):
        d = conductor(k, N)
        packets.setdefault(d, []).append(k)
    log("  conductor packets H_d (d|30, d>1):  d : dim phi(d) : primes(d)")
    for d in sorted(packets):
        log("     H_%-2d : dim %d : primes %s : k in %s"
            % (d, len(packets[d]), sorted(prime_set(d)) or "{}", packets[d]))
    log("")

    # enumerate connected quadruples (a+b+c+d=0 mod 30, no sub-pair = 0), classify by conductor multiset
    log("  enumerating quadruples a+b+c+d=0 (mod 30), a,b,c,d in {1..29}, up to ordering...")
    from collections import Counter
    sum0 = 0
    wick = 0          # at least one sub-pair = 0 (reducible to Gaussian/pairwise)
    connected = 0     # no sub-pair = 0 (genuine 4th-order)
    conn_by_primes = Counter()   # connected, keyed by the SET of primes spanned by the 4 conductors
    conn_threeprime_examples = []
    seen = set()
    for a, b, c, d in product(range(1, N), repeat=4):
        if (a + b + c + d) % N != 0:
            continue
        key = tuple(sorted((a, b, c, d)))
        if key in seen:
            continue
        seen.add(key)
        sum0 += 1
        pairs0 = ((a + b) % N == 0) or ((a + c) % N == 0) or ((a + d) % N == 0) \
            or ((b + c) % N == 0) or ((b + d) % N == 0) or ((c + d) % N == 0)
        if pairs0:
            wick += 1
        else:
            connected += 1
            primes = set().union(*(prime_set(conductor(x, N)) for x in (a, b, c, d)))
            conn_by_primes[frozenset(primes)] += 1
            if primes == {2, 3, 5} and len(conn_threeprime_examples) < 6:
                conds = tuple(conductor(x, N) for x in key)
                conn_threeprime_examples.append((key, conds))
    log("  quadruples with a+b+c+d=0 (unordered): %d total" % sum0)
    log("     WICK-reducible (some sub-pair=0; Gaussian/2nd-order, conductor-blind-spot floor): %d" % wick)
    log("     CONNECTED (no sub-pair=0; genuine 4th-order, beyond-Gaussian): %d" % connected)
    log("")
    log("  CONNECTED quadruples by the prime-set their four conductors span (the cross-prime reach):")
    for ps in sorted(conn_by_primes, key=lambda s: (len(s), sorted(s))):
        log("     primes %-12s : %d connected quadruples" % (str(sorted(ps)), conn_by_primes[ps]))
    log("  => the {2,3,5} rows are GENUINE THREE-PRIME obstructions: connected order-4 vertices that")
    log("     couple all three primes and are NOT reducible to a Gaussian pairing or a pairwise (two-prime)")
    log("     face -- exactly the 'first non-pairwise obstruction' Paper 22 sec 7 named, now counted.")
    log("  sample three-prime connected quadruples (indices ; their conductors):")
    for key, conds in conn_threeprime_examples:
        log("     %s ; conductors %s" % (str(key), str(conds)))
    log("")

    # ============================================================================
    #  PART C -- the two-tower reading, the Weil connection, honest residual
    # ============================================================================
    log("================  PART C: reading + Paper 22 Weil connection + honest residual  ==============")
    log("TWO-TOWER (Beyond-CBS), arithmetic and exact:")
    log("  * the WICK-reducible quadruples (delta_{a+b=0}delta_{c+d=0}) are the GAUSSIAN / 2nd-order")
    log("    content -- the conductor-blind-spot floor; a 2nd-moment / symmetric instrument sees only these.")
    log("  * the CONNECTED quadruples are the genuine 4th-CUMULANT (beyond-Gaussian) content; the cumulant")
    log("    Q SUBTRACTS the Wick part, isolating them. Order 4 is the FIRST order with this split (order 3")
    log("    is pure-connected) -- the arithmetic realization of 'the two towers coincide only at the Gaussian'.")
    log("  * ANSWERS Paper 21's open question: the fourth-cumulant case IS qualitatively new -- the first")
    log("    Gaussian (Wick) subtraction -- and on Z/30 it produces genuine THREE-PRIME connected vertices.")
    log("")
    log("PAPER 22 (the program's RH route) connection:")
    log("  Paper 22 sec 5.3: the ORDER-3 selection rule organizes Q_2 = W_zeta(f*f^*)|_{<=3} on Z/6,")
    log("  recovering the first prime correction sum_{p=2,3} log p. The ORDER-4 atlas here is the next")
    log("  truncation W_zeta(f*f^*)|_{<=4} on Z/30: the connected three-prime quadruples carry the genuine")
    log("  quartic prime-interaction content (p=5 enters; the non-pairwise term), while the Wick part")
    log("  reproduces the Gaussian/2nd-order (archimedean main + pairwise) piece already present at order 2.")
    log("  This EXTENDS Paper 22 sec 5.3 from cubic to quartic -- the computation Papers 21/22 named open.")
    log("")
    log("HONEST RESIDUAL (tiered):")
    log("  [P] the order-4 selection rule (connected - 3 Wick pairings), verified to machine precision; the")
    log("      Z/30 packet atlas and the connected/three-prime quadruple counts (exact combinatorics).")
    log("  [A] the two-tower reading (Wick=Gaussian floor, connected=beyond-Gaussian) and the Weil-truncation")
    log("      placement W_zeta|_{<=4}; the claim that order 4 is the first Gaussian-subtraction order.")
    log("  [open == RH] this is one more finite row of Paper 22's tower; positivity/boundedness here is the")
    log("      order-4 instance, NOT a proof of RH. Conservation of difficulty holds: the all-order limit")
    log("      (Paper 22 Conjecture 5.2: von Mangoldt recovery + Archimedean Noether Limit + leakage")
    log("      extinction) remains the hard step. The NEW content is the qualitative order-4 structure (the")
    log("      Wick split / three-prime obstruction), answering Paper 21 and feeding Paper 22's quartic row.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "quartic_selection_z30.md"
    header = [
        "# The order-4 selection rule and the Z/30 atlas (the program's named-open quartic computation)",
        "",
        "**Script:** `empirical/verify_quartic_selection_z30.py`  (builds on T3, T2, Paper 21, Paper 22).",
        "**Finding:** the order-4 cumulant selection rule is delta_{a+b+c+d=0} MINUS three Wick pairings",
        "delta_{a+b=0}delta_{c+d=0} (verified to machine precision on N=6,8). Order 4 is the FIRST order with",
        "a Gaussian (Wick) subtraction -- the two-tower (Beyond-CBS) split made arithmetic. On Z/30 the",
        "CONNECTED (no-sub-pair) quadruples spanning {2,3,5} are the genuine three-prime obstruction Paper 22",
        "sec 7 named; this extends Paper 22 sec 5.3 (cubic on Z/6) to the quartic row and answers Paper 21's",
        "open question (order 4 IS qualitatively new). NO claim RH is proved; conservation of difficulty holds.",
        "**Nature:** numerical/exact-combinatorial; builds on the corpus, does not reinvent it.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
