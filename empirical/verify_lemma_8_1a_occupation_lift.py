r"""Exact-arithmetic audit of Lemma 8.1a (occupation lift from squarefree axes)
of `22.primorial_cumulant_noether_rh.md`.

Grounded-paranoid-delusional gate: the settlement meaning below was fixed BEFORE this
script was run (see PRE-REGISTRATION). The transcript, not any prose, is the record.

Lemma 8.1a was "still to be written out" in the source; this audit writes out its testable
content and decides its true shape.

============================================================================
PRE-REGISTRATION  (Audit of Lemma 8.1a; matched-pair, meaning fixed pre-run)
============================================================================
The von Mangoldt target sum is indexed by the OCCUPATION lattice N^{p<=p_n}: the prime
power p^r is the occupation k = r*e_p, at position r*log p, with weight Lambda(p^r)=log p.
The finite recovery datum and its additive convolutions are indexed by the SQUAREFREE
additive dual \hat R_n = prod F_p (conductors are radicals). Lemma 8.1a asserts that the
single-axis prime-power ladder with weight log p is "remaining algebraic bookkeeping"
over the squarefree axes.

K (positive, the paper's framing): the single-axis prime-power ladder {p^r : r>=1} with
    constant von Mangoldt weight log p is a function of the squarefree additive datum on
    R_n, recoverable by finite conductor-convolution bookkeeping.

L (negative, the split): occupation depth r is NOT a function of the additive characters
    of R_n. Additive convolution on axis F_p wraps mod p, and the radical map
    N^P -> {squarefree divisors}, k -> rad(prod p^{k_p}), forgets all depths (infinite
    fibers). So the prime-power ladder {p^r} cannot be recovered from the squarefree
    additive data; the occupation lift to N^P is strictly additional structure (the
    Thm 5.2.1 "double cutoff" hypothesis), NOT squarefree bookkeeping.

JOINT-ON-DISJOINT: K on the squarefree skeleton + mixed-axis separation (the radical /
    which-axes-lit content IS recoverable, finite algebra, consistent with the R=30
    triple-mixing certificate), and L on the occupation depth (the p^r ladder is not).
    This draws the firewall exactly at "squarefree axis skeleton (finite, on \hat R_n)
    vs prime-power occupation lift (external, on N^P)" -- the line the source's own
    Claim-Hygiene paragraph and Thm 5.2.1 double-cutoff hypothesis already point at.
============================================================================

All arithmetic is exact (integers, multiset Counters, modular sums); no floating point
enters any conductor, equality, support, or counting decision.
"""

from __future__ import annotations

from collections import Counter
from math import gcd, comb
from pathlib import Path


# ---- additive-character conductors on Z/m (m squarefree) ---------------------------

def conductor(eta, m):
    """Conductor of the additive character e_eta on Z/m = m/gcd(eta,m) = radical of lit axes."""
    return m // gcd(eta % m, m)


def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def radical(n):
    r = 1
    for p in factorize(n):
        r *= p
    return r


def conv(a, b, m):
    """Additive convolution of two multisets (Counters) of labels on Z/m."""
    out = Counter()
    for x, cx in a.items():
        for y, cy in b.items():
            out[(x + y) % m] += cx * cy
    return out


# ---- Part (a): squarefree skeleton + mixed-axis separation  (expected K) ------------

def part_a(m, log):
    primes = sorted(factorize(m))
    n = len(primes)
    axis = {p: [e for e in range(m) if conductor(e, m) == p] for p in primes}
    h = Counter()
    for p in primes:
        for e in axis[p]:
            h[e] += 1                                   # indicator of the union of single-axis packets

    log("  single-axis packets: " + ", ".join("cond %d -> %d labels" % (p, len(axis[p])) for p in primes))

    # convolution powers h^{*k}, k = 1..n; conductors appearing at each order
    conductors_by_order = {}
    cur = Counter(h)
    for k in range(1, n + 1):
        conds = sorted({conductor(e, m) for e, c in cur.items() if c})
        conductors_by_order[k] = conds
        log("  order k=%d : conductors present = %s%s"
            % (k, conds, "   <- full conductor %d" % m if m in conds else ""))
        if k < n:
            cur = conv(cur, h, m)

    # checks
    all_squarefree = all(radical(d) == d for k in conductors_by_order for d in conductors_by_order[k])
    full_first_at_n = (m not in conductors_by_order.get(n - 1, [])) and (m in conductors_by_order[n])
    # single-axis closure: convolving labels of one axis stays on that axis or trivial
    single_axis_closed = True
    for p in primes:
        hp = Counter({e: 1 for e in axis[p]})
        hp2 = conv(hp, hp, m)
        if any(conductor(e, m) not in (1, p) for e, c in hp2.items() if c):
            single_axis_closed = False
    log("  [a1] every conductor present is squarefree (radical of lit axes) : %s"
        % ("PASS" if all_squarefree else "FAIL"))
    log("  [a2] full conductor %d first appears at order n=%d (not before)   : %s"
        % (m, n, "PASS" if full_first_at_n else "FAIL"))
    log("  [a3] single-axis convolution stays single-axis (cond in {1,p})    : %s"
        % ("PASS" if single_axis_closed else "FAIL"))
    return all_squarefree and full_first_at_n and single_axis_closed


# ---- Part (b): occupation depth is not recoverable from additive data  (expected L) --

def part_b(log):
    ok_collapse = True

    # W1: depth is not a function of the additive label -- same character from different depths.
    log("  [W1] additive label r*a mod p is periodic in occupation depth r (period p):")
    for p in (2, 3, 5):
        a = 1
        row = [(r, (r * a) % p) for r in range(1, 2 * p + 1)]
        # exhibit r1 != r2 with identical label
        seen = {}
        witness = None
        for r, lab in row:
            if lab != 0 and lab in seen and witness is None:
                witness = (seen[lab], r, lab)
            seen.setdefault(lab, r)
        log("        p=%d, a=1:  (r -> r*a mod p) = %s" % (p, [lab for _, lab in row]))
        if witness:
            r1, r2, lab = witness
            log("              depths r=%d and r=%d both give label %d -> identical character, conductor %d"
                % (r1, r2, lab, p))
        else:
            ok_collapse = False
            log("              FAIL: expected a depth collision mod %d" % p)

    # W2: the radical map forgets depth -- a whole prime-power tower maps to one conductor.
    log("  [W2] radical map N^P -> squarefree conductor forgets occupation depth:")
    for p in (2, 3, 5):
        tower = [p ** r for r in range(1, 9)]
        conds = {radical(x) for x in tower}
        log("        tower {p^r : r=1..8} = %s  ->  radical/conductor set = %s" % (tower, sorted(conds)))
        if conds != {p}:
            ok_collapse = False
            log("              FAIL: tower did not collapse to the single conductor %d" % p)
    log("        => Lambda(p^r)=log p sits at distinct positions r*log p but ONE conductor; "
        "the conductor cannot separate the ladder.")

    # C1: counting -- occupation lattice is infinite-to-one over the finite conductor lattice.
    log("  [C1] occupation profiles over a fixed conductor grow without bound (R_30, n=3 axes):")
    n = 3
    log("        #nontrivial squarefree conductors of P_n = 2^n - 1 = %d   (fixed)" % (2 ** n - 1))
    log("        full-support occupation profiles of total depth K  (-> the single conductor 30):")
    grows = []
    for K in range(n, n + 7):
        # compositions of K into n positive parts = C(K-1, n-1); each maps to conductor 30
        count = comb(K - 1, n - 1)
        grows.append(count)
        log("            K=%d : %d profiles  (e.g. partitions of K into 3 positive prime-occupations)" % (K, count))
    monotone_unbounded = all(grows[i] < grows[i + 1] for i in range(len(grows) - 1)) and grows[-1] > (2 ** n - 1)
    log("  [b-verdict] occupation depth not recoverable from additive R_n data : %s"
        % ("CONFIRMED (L)" if (ok_collapse and monotone_unbounded) else "NOT CONFIRMED"))
    return ok_collapse and monotone_unbounded


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(__doc__)

    log("================  PART (a): squarefree skeleton + mixed-axis separation  ================")
    a_ok = True
    for m in (6, 30):
        log("")
        log("---- R = Z/%d ----" % m)
        a_ok = part_a(m, log) and a_ok

    log("")
    log("================  PART (b): occupation-depth recoverability  ================")
    b_split = part_b(log)

    log("")
    log("================  REALIZED BRANCH  ================")
    if a_ok and b_split:
        log("K on the squarefree skeleton: conductors are radicals of lit axes; the full")
        log("conductor first appears at convolution order n = #primes; single-axis convolution")
        log("stays single-axis. The which-axes-lit (radical) content IS finite-algebraic.")
        log("")
        log("L on the occupation depth: additive convolution on F_p wraps mod p (W1), the radical")
        log("map collapses each prime-power tower to one conductor (W2), and the occupation lattice")
        log("is infinite-to-one over the finite squarefree-conductor lattice (C1). The {p^r} ladder")
        log("with weight log p is NOT a function of the squarefree additive data on R_n.")
        log("")
        log(">>> JOINT-ON-DISJOINT: Lemma 8.1a splits. The squarefree skeleton + mixed separation")
        log(">>> is [P] finite algebra; the occupation lift to N^P (prime powers, weight log p) is")
        log(">>> NOT squarefree bookkeeping but strictly-additional structure -- the Thm 5.2.1")
        log(">>> double-cutoff hypothesis. This refines the source's 'remaining algebraic")
        log(">>> bookkeeping' framing and localizes the occupation lift as an external obligation.")
    else:
        log(">>> A pre-registered expectation did not hold; see rows above.")

    report = Path(__file__).resolve().parent / "reports" / "lemma_8_1a_occupation_lift.md"
    header = [
        "# Lemma 8.1a Occupation-Lift Audit",
        "",
        "**Script:** `empirical/verify_lemma_8_1a_occupation_lift.py`",
        "**Source:** `22.primorial_cumulant_noether_rh.md` (Lemma 8.1a, occupation lift)",
        "**Status:** %s" % ("joint-on-disjoint realized — squarefree skeleton [P]; occupation lift is external, not bookkeeping"
                            if (a_ok and b_split) else "see transcript"),
        "",
        "Deterministic, exact (integers / `Counter` multisets); no floating point enters any",
        "conductor, support, equality, or counting decision. Re-running reproduces this",
        "transcript identically. The transcript below is the record.",
        "",
        "```text",
    ]
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(header + lines + ["```", ""]), encoding="utf-8")
    print("\n[report written to %s]" % report)
    return 0 if (a_ok and b_split) else 1


if __name__ == "__main__":
    raise SystemExit(main())
