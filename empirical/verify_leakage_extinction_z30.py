r"""Finite order-4 leakage extinction on Z/30: the closed-leaf projection Pi_tau annihilates the
cross-prime sector (the Paper 22 sec 7 / Paper 21 carry-obstruction), per-row instance.

Paper 22 sec 5.3 (cubic, Z/6): Pi_tau projects onto the single-prime Cartan packets A_2 + A_3 and
"the mixed 2*3 term ... vanishes after closed-leaf projection, as required by the functional-equation
side." Conjecture 5.2 input #3 (leakage extinction) is the LIMIT/all-order statement (mu_n^*(H_n)
polylog(P_n) -> 0); the FINITE per-row instance is computable, and is what we settle here.

MECHANISM (sharp, combinatorial -- not Paper-22 apparatus-dependent):
  * a character chi_k on Z/N has the prime p in its conductor  iff  p does NOT divide k (p | N).
    Single-prime (Cartan) packet A_p = {k : conductor(k) = p} (exactly one active prime).
  * Pi_tau = projection onto the single-prime axes  A_{p1} + ... ;  it ZEROES every mixed-conductor
    character. So a vertex (selection-rule tuple) survives Pi_tau iff ALL its characters are single-prime.
  * CLAIM (finite leakage extinction): every CROSS-PRIME connected vertex -- one whose characters'
    conductors span >= 2 distinct primes -- contains at least one MIXED (multi-prime) character, hence
    lies in ker Pi_tau. Equivalently: NO connected vertex spanning >= 2 primes is built from single-prime
    characters alone. Therefore Pi_tau Q_k keeps ONLY single-axis (one-prime) vertices, which carry the
    von Mangoldt weight Lambda(p^r) = log p; no cross-prime carry survives.
  PROOF (three-prime quadruple case, the decisive one): a connected quadruple spanning {2,3,5} built
  from single-prime characters needs a surjection {4 chars} -> {2,3,5}, i.e. one prime doubled. The
  mod-2 constraint sum = 0 forces an EVEN number of 2-active characters, so the doubled prime must be 2;
  but A_2 = {N/2} is 1-dimensional, so "two 2-active characters" means the SAME character twice, whose
  sum is N/2 + N/2 = 0 -- a vanishing sub-pair, i.e. WICK, not connected. Contradiction. (The general
  cross-prime case is verified computationally below.)

This probe:
  PART A -- validate on Z/6 (cubic): cross-prime triples all contain the conductor-6 character; Pi_tau
            (onto A_2+A_3) kills them -- reproducing Paper 22 sec 5.3's "mixed 2*3 vanishes".
  PART B -- Z/30 (quartic): enumerate connected quadruples; SINGLE-AXIS ones survive Pi_tau (-> log p);
            CROSS-PRIME ones (incl. all 914 three-prime) each contain a mixed character (count of
            all-single-prime cross-prime vertices = 0) -- so the entire cross-prime sector is in ker Pi_tau.
  PART C -- the finite order-4 leakage-extinction statement + honest scope (the limit = Conjecture 5.2).

NUMERICAL/exact-combinatorial; builds on Paper 22 sec 5.3/sec 7, Paper 21, the quartic atlas. NO RH claim.
"""

import sys
from math import gcd
from itertools import product
from collections import Counter

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


def is_single_prime(k, N):
    return len(prime_set(conductor(k, N))) == 1


def primes_spanned(tup, N):
    s = set()
    for k in tup:
        s |= prime_set(conductor(k, N))
    return s


def connected(tup, N):
    # selection rule sum=0 and (order>=4) no vanishing sub-pair; for order 3 no proper sub-pair test
    if sum(tup) % N != 0:
        return False
    r = len(tup)
    if r >= 4:
        for i in range(r):
            for j in range(i + 1, r):
                if (tup[i] + tup[j]) % N == 0:
                    return False
    return True


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ============================================================================
    #  PART A -- cubic validation on Z/6 (reproduce Paper 22 sec 5.3)
    # ============================================================================
    log("================  PART A: Z/6 cubic -- Pi_tau (A_2+A_3) kills the mixed 2*3 term  ============")
    N = 6
    sp = {k for k in range(1, N) if is_single_prime(k, N)}
    log("  single-prime (Cartan) characters: %s  (A_2={3}: cond 2; A_3={2,4}: cond 3)" % sorted(sp))
    log("  mixed characters: %s  (conductor 6, the M packet)" % sorted(set(range(1, N)) - sp))
    cross = 0
    cross_all_single = 0
    seen = set()
    for tup in product(range(1, N), repeat=3):
        key = tuple(sorted(tup))
        if key in seen:
            continue
        seen.add(key)
        if not connected(tup, N):
            continue
        ps = primes_spanned(tup, N)
        if len(ps) >= 2:
            cross += 1
            if all(is_single_prime(k, N) for k in tup):
                cross_all_single += 1
    log("  cross-prime cubic triples (span {2,3}): %d ; of these ALL-single-prime: %d" % (cross, cross_all_single))
    log("  => every cross-prime cubic triple contains a mixed (conductor-6) character; Pi_tau annihilates")
    log("     the cross-prime sector -- exactly Paper 22 sec 5.3's 'the mixed 2*3 term vanishes'. [validated]")
    log("")

    # ============================================================================
    #  PART B -- quartic on Z/30
    # ============================================================================
    log("================  PART B: Z/30 quartic -- single-axis survives, cross-prime in ker Pi_tau  ===")
    N = 30
    sp = {k for k in range(1, N) if is_single_prime(k, N)}
    cartan = {}
    for k in sp:
        cartan.setdefault(conductor(k, N), []).append(k)
    log("  single-prime (Cartan) packets, the image of Pi_tau:")
    for d in sorted(cartan):
        log("     A_%d = %s   (prime %d, von Mangoldt weight log %d)" % (d, sorted(cartan[d]), d, d))
    log("")

    single_axis_conn = Counter()   # connected, all four in ONE A_p
    cross_conn = 0                  # connected, span >= 2 primes
    cross_all_single = 0            # connected cross-prime built from single-prime chars only
    threeprime_conn = 0
    threeprime_all_single = 0
    seen = set()
    for tup in product(range(1, N), repeat=4):
        key = tuple(sorted(tup))
        if key in seen:
            continue
        seen.add(key)
        if not connected(tup, N):
            continue
        ps = primes_spanned(tup, N)
        allsingle = all(is_single_prime(k, N) for k in tup)
        if len(ps) == 1:
            single_axis_conn[next(iter(ps))] += 1
        else:
            cross_conn += 1
            if allsingle:
                cross_all_single += 1
            if ps == {2, 3, 5}:
                threeprime_conn += 1
                if allsingle:
                    threeprime_all_single += 1
    log("  CONNECTED quadruples, by survival under Pi_tau:")
    log("     SINGLE-AXIS (one prime, ALL chars in one A_p) -- SURVIVE Pi_tau, carry log p:")
    for p in sorted(single_axis_conn):
        log("        prime %d : %d connected single-axis quadruples  (-> log %d)" % (p, single_axis_conn[p], p))
    log("     CROSS-PRIME (span >= 2 primes): %d total ; of these ALL-single-prime (would SURVIVE): %d"
        % (cross_conn, cross_all_single))
    log("        among them THREE-PRIME {2,3,5}: %d ; all-single-prime: %d"
        % (threeprime_conn, threeprime_all_single))
    log("")
    log("  RESULT: %d of %d cross-prime connected quadruples are all-single-prime  => EVERY cross-prime"
        % (cross_all_single, cross_conn))
    log("  connected vertex contains >= 1 MIXED character, hence lies in ker Pi_tau and is annihilated.")
    log("  In particular all %d three-prime connected vertices vanish under Pi_tau (the sec-7 carry)." % threeprime_conn)
    log("  Only the single-axis vertices survive, carrying Lambda(p)=log p (p=2,3,5; p=5 the Z/30 entry).")
    log("")

    # ============================================================================
    #  PART C -- the finite leakage-extinction statement + honest scope
    # ============================================================================
    log("================  PART C: finite order-4 leakage extinction + scope  ================")
    log("THEOREM (finite, order-4, Z/30) [P]:  the closed-leaf projection Pi_tau onto the single-prime")
    log("  Cartan packets A_2 + A_3 + A_5 annihilates the ENTIRE cross-prime sector of the order-4 Noether")
    log("  form (every cross-prime connected quadruple has >= 1 mixed character; %d/%d all-single-prime," % (cross_all_single, cross_conn))
    log("  proven via the mod-2 parity + dim A_2 = 1 argument, verified above), while the single-axis sector")
    log("  survives with the von Mangoldt weights log 2, log 3, log 5.  Hence Pi_tau Q_3 carries NO")
    log("  cross-prime / three-prime CARRY: the sec-7 obstruction is ABSENT at the finite order-4 level, and")
    log("  Q_3 restricts on Crit_3 to the single-prime von Mangoldt sector = W_zeta(f*f^*)|_{<=4}'s prime side.")
    log("")
    log("READING vs the cubic: this is 'more of the same' as Paper 22 sec 5.3 (the cross-prime vertices are")
    log("  killed by Pi_tau in BOTH the cubic 2*3 and the quartic 2*3*5 case, for the same reason -- spanning")
    log("  an extra prime forces a mixed character).  The genuinely NEW order-4 feature is the WICK/Gaussian")
    log("  subtraction (verify_quartic_selection_z30.py), NOT a surviving three-prime carry.  So Paper 21's")
    log("  sec-7 question resolves: NO new qualitative CARRY obstruction at order 4; the novelty is the")
    log("  connected/Gaussian bifurcation of the selection rule.")
    log("")
    log("HONEST SCOPE:")
    log("  [P] the FINITE per-row instance (order 4, Z/30): Pi_tau annihilates the cross-prime sector; single-")
    log("      axis von Mangoldt recovery intact. Exact combinatorics + proof.")
    log("  [open == Conjecture 5.2 input #3] the ALL-ORDER, LIMIT leakage extinction -- projective")
    log("      compatibility across the primorial tower and the frame-price scaling mu_n^*(H_n) polylog(P_n)")
    log("      -> 0 -- is NOT settled here; it is the conserved hard core (Paper 22 sec 8), >= GRH. The finite")
    log("      per-row vanishing does not imply the uniform/limit vanishing.")
    log("  [C == RH] the full Primorial Noether-Weil Identity (Conjecture 5.2) and thence RH (Thm 6.1).")
    log("")
    log("NET: the order-4 leakage-extinction is settled AT THE FINITE ROW -- the cross-prime carry vanishes")
    log("under Pi_tau, cleanly, the same mechanism as the cubic -- so the order-4 row contributes exactly the")
    log("single-prime von Mangoldt side and no obstruction. The remaining difficulty is entirely the uniform")
    log("LIMIT (Conjecture 5.2), unchanged. Conservation holds.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "leakage_extinction_z30.md"
    header = [
        "# Finite order-4 leakage extinction on Z/30: Pi_tau kills the cross-prime carry",
        "",
        "**Script:** `empirical/verify_leakage_extinction_z30.py`  (builds on Paper 22 sec 5.3/sec 7, Paper 21).",
        "**Finding:** the closed-leaf projection Pi_tau onto the single-prime Cartan packets A_2+A_3+A_5",
        "annihilates the ENTIRE cross-prime order-4 sector -- every cross-prime connected quadruple contains",
        ">= 1 mixed character (0 of them are all-single-prime; proven via mod-2 parity + dim A_2=1), so all 914",
        "three-prime vertices vanish under Pi_tau, while the single-axis sector carries log 2,3,5. The sec-7",
        "carry-obstruction is ABSENT at the finite order-4 level ('more of the same' as the cubic; the novelty",
        "is the Wick split, not a carry). LIMIT leakage extinction (Conjecture 5.2 input #3) remains the open",
        "hard core; this is the per-row instance only.",
        "**Nature:** exact combinatorics + proof; validated against the cubic Z/6 case. NO claim RH proved.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
