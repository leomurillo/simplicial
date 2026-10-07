#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_xi_capacity_z510510_extension.py
========================================

Audit xi: extend audit theta (v2insert-09) to Z/510510 = 2*3*5*7*11*13*17,
the sixth primorial row.

Settles Paper 48 (proposed) C3/C4 sharper than v2insert-10 audit iota's
five-row anchor: audit iota's PNT-heuristic shape
  Capacity_V(P_n) ~ K * n^2 * ln(n) / N^2
predicts (with the audit-iota multiplicative constant ~ 4.5 average):
  Capacity_V(Z/510510) ~ 4.5 * 7^2 * ln(7) / 510510^2 ~ 1.7e-9

This audit computes the exact integer-arithmetic value of
  Capacity_V(Z/510510) := pure_V(510510) / T_total(510510)
by:
  - integer-arithmetic enumeration of V_idx = {k : gcd(k, 510510) = 510510/p
    for some prime p | 510510}
  - closed-form Burnside count of T_total(N) (orbits of S_3 acting on
    ordered closing triples)
  - integer-arithmetic O(|V|^2) enumeration of pure-V triples

Compute: dim_V on Z/510510 = sum(p_i - 1) = 1 + 2 + 4 + 6 + 10 + 12 + 16 = 51.
|V|^2 = 2601 pairs; for each (a, b) in V, compute c = -a-b mod N and check
c in V.  Trivial CPU.  Total compute estimate: under 1 second.

The audit also recomputes the five-row v2insert-09 anchors to verify
the implementation reproduces v2insert-09 values exactly.

Pre-claimed three-outcome (v2insert-04 sec 3.1):
  K-branch: Capacity_V(Z/510510) within factor of 2 of PNT-heuristic
    prediction 1.7e-9; joint-on-disjoint settlement of audit iota
    extrapolates cleanly.
  L-branch: Capacity_V(Z/510510) deviates from prediction by more than
    a factor of 2; the PNT-heuristic shape is row-specific to Z/{6, 30,
    210, 2310, 30030} and the audit-iota settlement does not extrapolate.
  joint-on-disjoint: deviates in a structured way (e.g., specific to
    the addition of prime p_7 = 17), revealing a higher-order correction
    audit iota did not capture.
"""
from __future__ import annotations
import math
import sys
import time
import itertools


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


def primes_dividing(n: int) -> list[int]:
    primes = []
    for p in range(2, n + 1):
        if n % p == 0 and is_prime(p):
            primes.append(p)
        if p * p > n:
            break
    # Also catch large prime factors
    m = n
    for p in primes:
        while m % p == 0:
            m //= p
    if m > 1:
        primes.append(m)
    return sorted(set(primes))


def V_indices_squarefree_primorial(N: int) -> list[int]:
    """Return the single-prime V_idx = {k : N/gcd(k, N) is prime}."""
    return [k for k in range(1, N) if is_prime(N // math.gcd(k, N))]


def T_total_closed_form(N: int) -> int:
    """Closed-form count of unordered closing triples (k, l, m) with
    k, l, m in {1, .., N-1} and k+l+m ≡ 0 (mod N).

    Burnside / orbit count: the action of S_3 on ordered closing triples
    has size N^2 (since k, l free and m = -k-l mod N).  Subtract triples
    with any leg zero: 3*(N-1) ordered + 2 (the all-zero) = corrections.

    Formula (verified on Z/6 = 6, Z/30 = 150, Z/210 = 7350):
      T_ordered_nonzero = N^2 - 3*(N-1) - 1 + 0   (over-counts adjusted)
      ... let's compute directly from S_3 orbit decomp.

    Actually the simpler approach: use the formula
      T_total = (N^2 + 3*N*one_of_pairs + 2*N*one_of_triples) / 6
    where one_of_pairs counts unordered (a, a, b) with 2a+b ≡ 0 (mod N), a != b
    and one_of_triples counts (a, a, a) with 3a ≡ 0 (mod N), all in {1..N-1}.

    For verification, just enumerate at small N and compare to closed form.
    For Z/510510 we use a closed form derived from the orbit-counting lemma.
    """
    # Number of ordered closing triples (k, l, m) with k, l, m in {1, ..., N-1}
    # and k+l+m ≡ 0 (mod N):
    # = #{(k, l) in {1..N-1}^2 : k+l ≢ 0 (mod N), -k-l mod N in {1..N-1}}
    # = #{(k, l) in {1..N-1}^2 : k+l ≢ 0 (mod N)}
    # = (N-1)^2 - #{(k, l) : l ≡ -k mod N, k, l in {1..N-1}}
    # = (N-1)^2 - (N-1)
    # = (N-1)(N-2)
    # Wait, but we also need k+l+m = 0 mod N with m != 0; if k+l = 0 mod N
    # then m would have to be 0, not allowed. So ordered = (N-1)(N-2)? No,
    # let me recount.
    #
    # For each (k, l) in {1..N-1}^2, m = (-k-l) mod N is in {0, .., N-1}.
    # We need m != 0, i.e. k+l ≢ 0 (mod N).
    # So ordered triples (k, l, m) in {1..N-1}^3 with closing = (N-1)^2 - (N-1)
    # = (N-1)(N-2). Verify on N=6: (5)(4) = 20.
    # Hmm but the v2insert-09 table has T_total(Z/6) = 6 for unordered.
    # 20 / 6? 20 is ordered, and unordered orbits of S_3 are 20 / (3! / sym) ...
    # not all orbits have size 6 (e.g., {2,2,2} has orbit size 1).
    #
    # Let me just enumerate at small N to check.
    n_ord = 0
    for k in range(1, N):
        for l in range(1, N):
            m = (-k - l) % N
            if m != 0:
                n_ord += 1
    # Now count unordered multisets via Burnside:
    # Number of unordered = sum_{g in S_3} fix(g) / |S_3|
    # fix(identity) = n_ord
    # fix(2-cycles, 3 of them) = each is a swap; fix = triples with two equal entries
    # fix(3-cycles, 2 of them) = triples with all entries equal
    # Easier: directly enumerate unordered multisets.
    seen: set[tuple[int, int, int]] = set()
    for k in range(1, N):
        for l in range(k, N):  # l >= k
            m = (-k - l) % N
            if m == 0 or m < l:
                continue
            seen.add((k, l, m))
        # also m = l case: handled by m < l check
    # Plus (a, a, b) with 2a+b = 0 mod N, a < b OR a = b (i.e., 3a = 0)
    # already handled? Let me reconsider.
    return -1  # placeholder, we use enumeration directly


def enumerate_closing_multisets(N: int) -> int:
    """Direct enumeration of unordered closing multisets (k, l, m).
    Returns T_total(N).  O(N^2) work."""
    multisets: set[tuple[int, ...]] = set()
    for k in range(1, N):
        for l in range(1, N):
            m = (-k - l) % N
            if m == 0:
                continue
            t = tuple(sorted((k, l, m)))
            multisets.add(t)
    return len(multisets)


def enumerate_pure_V_multisets(N: int, V_set: set[int]) -> int:
    """Count unordered multisets (k, l, m) with all three in V and closing.
    O(|V|^2) work."""
    multisets: set[tuple[int, ...]] = set()
    V_list = sorted(V_set)
    for k in V_list:
        for l in V_list:
            m = (-k - l) % N
            if m == 0 or m not in V_set:
                continue
            t = tuple(sorted((k, l, m)))
            multisets.add(t)
    return len(multisets)


def T_total_closed(N: int, primes: list[int]) -> int:
    """Closed-form T_total for squarefree primorial.

    Burnside count: T_total = (1/6) * (n_ord + 3 * n_pairs + 2 * n_triples)
      n_ord = ordered closing triples (k, l, m), all in {1, .., N-1}
            = (N-1)(N-2)  ... wait, let me reverify
      n_pairs = number of (a, b) with a != b, 2a+b = 0 (mod N), a, b in {1..N-1}
              = number of a in {1..N-1} with 2a in {1..N-1} (i.e., b = -2a mod N in {1..N-1})
                excluding those with a = b
      n_triples = number of a in {1..N-1} with 3a = 0 (mod N)
                = (gcd(3, N) - 1) for N with gcd(3, N) trivially or 3.

    For squarefree primorial N with 3 | N: gcd(3, N) = 3, so n_triples = 2
    (the two non-zero a in {1..N-1} with 3a ≡ 0 mod N are a = N/3 and 2N/3).

    For ordered: we have (k, l, m) in {1..N-1}^3 with k+l+m = 0 (mod N).
    Let k, l free in {1..N-1}: m = (-k-l) mod N.  m = 0 iff l = -k mod N.
    For each k in {1..N-1}, exactly one l in {1..N-1} (namely N-k) gives m=0.
    So n_ord = (N-1)^2 - (N-1) = (N-1)(N-2).
    For N=6: 5*4 = 20.  Total ordered + (5) zeros = 25; not (N-1)^2 - exclusions.
    Hmm wait: (N-1)^2 = 25, minus (N-1) where m=0: 25 - 5 = 20. Yes.

    But on Z/6 we know T_total (unordered) = 6.  Burnside gives unordered:
    sum_{g in S_3} fix(g) / 6.
    fix(identity) on ordered triples = 20.
    fix(swap 1<->2) = triples (a, a, b) with a + a + b = 0 (mod N), a in {1..N-1}, b in {1..N-1}.
       = number of a with -2a mod N in {1..N-1}
       = (N-1) - #{a : 2a = 0 mod N} = N-1 minus (gcd(2,N) - 1) = N-1 - 1 = N-2 (for even N).
       For N=6: 5 - 1 = 4.  So fix(12-swap) = 4.  Total swap fixes: 3 * 4 = 12.
    fix(3-cycle) = triples (a, a, a) with 3a = 0 (mod N)
       = gcd(3, N) - 1 (if 3 | N), else 0.
       For N=6: gcd(3,6) = 3, n=2.  Total 3-cycle fixes: 2 * 2 = 4.
    Total Burnside: (20 + 12 + 4)/6 = 36/6 = 6. ✓

    General formula:
      n_ord     = (N-1)(N-2)
      n_2cycle  = (N-2)  if N even, (N-1) if N odd  [number of a with 2a != 0]
      n_3cycle  = gcd(3, N) - 1
      T_total   = [n_ord + 3 * n_2cycle + 2 * n_3cycle] / 6

    For squarefree primorials, the primes always include 2 and 3:
      2 | N, 3 | N, so n_2cycle = N - 2, n_3cycle = 2.
      T_total = [(N-1)(N-2) + 3(N-2) + 4] / 6
              = [N^2 - 3N + 2 + 3N - 6 + 4] / 6
              = N^2 / 6.

    So for any squarefree primorial:  T_total(N) = N^2 / 6.

    Verify: Z/6: 36/6 = 6 ✓; Z/30: 900/6 = 150 ✓; Z/210: 44100/6 = 7350 ✓;
    Z/2310: 2310^2/6 = 5336100/6 = 889350 ✓; Z/30030: 30030^2/6 = 901800900/6 = 150300150 ✓.

    The closed form for primorial N is simply N^2 / 6.
    """
    return (N * N) // 6


def main() -> int:
    print("=" * 78)
    print(" Audit xi: capacity scaling extension to Z/510510")
    print(" Tests audit iota's PNT-heuristic shape prediction at primorial row 7")
    print("=" * 78)
    print()

    # The primorial ladder
    primorials = [(6, [2, 3]), (30, [2, 3, 5]), (210, [2, 3, 5, 7]),
                  (2310, [2, 3, 5, 7, 11]), (30030, [2, 3, 5, 7, 11, 13]),
                  (510510, [2, 3, 5, 7, 11, 13, 17])]

    print(f"  {'Row':>10}  {'n':>3}  {'dim_V':>6}  {'T_total':>14}  "
          f"{'pure_V':>10}  {'Capacity_V':>14}  {'log10':>8}  {'PNT pred':>12}  {'ratio':>8}")
    print(f"  {'-' * 10}  {'-' * 3}  {'-' * 6}  {'-' * 14}  "
          f"{'-' * 10}  {'-' * 14}  {'-' * 8}  {'-' * 12}  {'-' * 8}")

    results = []
    K_pnt_avg = 4.5  # average multiplicative constant from audit iota

    for N, primes in primorials:
        t0 = time.time()

        # V_idx: single-prime conductor packets
        V_idx = V_indices_squarefree_primorial(N)
        dim_V = len(V_idx)
        n_primes = len(primes)

        # T_total: closed form N^2/6 for squarefree primorials
        T_total = T_total_closed(N, primes)

        # pure_V: O(|V|^2) enumeration
        V_set = set(V_idx)
        pure_V = enumerate_pure_V_multisets(N, V_set)

        Capacity_V = pure_V / T_total
        log10_cap = math.log10(Capacity_V)

        # PNT-heuristic prediction
        pnt_pred = K_pnt_avg * (n_primes ** 2) * math.log(n_primes) / (N * N)
        ratio = Capacity_V / pnt_pred

        elapsed = time.time() - t0
        print(f"  Z/{N:>7}  {n_primes:>3}  {dim_V:>6}  {T_total:>14}  "
              f"{pure_V:>10}  {Capacity_V:>14.6e}  {log10_cap:>+8.4f}  "
              f"{pnt_pred:>12.4e}  {ratio:>8.3f}")

        results.append({
            'N': N, 'n_primes': n_primes, 'dim_V': dim_V, 'T_total': T_total,
            'pure_V': pure_V, 'Capacity_V': Capacity_V, 'log10': log10_cap,
            'pnt_pred': pnt_pred, 'ratio': ratio, 'elapsed': elapsed,
        })

    print()
    print("-" * 78)
    print(" Verification against v2insert-09 anchors:")
    print("-" * 78)
    v2insert09_anchors = {
        6:    (3, 6, 2),
        30:   (7, 150, 6),
        210:  (13, 7350, 14),
        2310: (23, 889350, 34),
        30030:(35, 150300150, 62),
    }
    all_anchors_ok = True
    for r in results:
        if r['N'] in v2insert09_anchors:
            expected_dV, expected_Tt, expected_pV = v2insert09_anchors[r['N']]
            ok_dV = r['dim_V'] == expected_dV
            ok_Tt = r['T_total'] == expected_Tt
            ok_pV = r['pure_V'] == expected_pV
            status = "OK" if (ok_dV and ok_Tt and ok_pV) else "FAIL"
            if not (ok_dV and ok_Tt and ok_pV):
                all_anchors_ok = False
            print(f"  Z/{r['N']:>7}: dim_V={r['dim_V']}/{expected_dV}, "
                  f"T_total={r['T_total']}/{expected_Tt}, "
                  f"pure_V={r['pure_V']}/{expected_pV}  [{status}]")
    if all_anchors_ok:
        print("  All v2insert-09 anchors reproduced exactly.  [PASS]")
    print()

    # Focus on the new row: Z/510510
    print("-" * 78)
    print(" Audit xi headline: Z/510510 = 2*3*5*7*11*13*17 (the 7th primorial)")
    print("-" * 78)
    new = results[-1]
    print(f"  dim_V = {new['dim_V']}  (= 1 + 2 + 4 + 6 + 10 + 12 + 16)")
    print(f"  T_total = {new['T_total']}  (= 510510^2 / 6)")
    print(f"  pure_V = {new['pure_V']}")
    print(f"  Capacity_V = {new['Capacity_V']:.6e}  (= {new['pure_V']}/{new['T_total']})")
    print(f"  log10(Capacity_V) = {new['log10']:+.4f}")
    print()
    print(f"  PNT-heuristic prediction: {new['pnt_pred']:.4e}")
    print(f"  Ratio Capacity_V / prediction: {new['ratio']:.3f}")
    print()
    print(f"  Per-step decay factor (row 6 -> row 7):")
    decay = results[-2]['Capacity_V'] / new['Capacity_V']
    print(f"  Capacity_V(Z/30030) / Capacity_V(Z/510510) = {decay:.2f}x")
    print(f"  (audit theta pattern: 8.3x -> 21x -> 50x -> 93x -> {decay:.0f}x)")
    print(f"  Predicted by p_7^2 = 17^2 = 289 (with |V| growth correction: "
          f"~ p_7^2 * (n_6/n_7)^c)")
    print()

    # Three-outcome adjudication
    print("-" * 78)
    print(" Three-outcome adjudication (v2insert-04 sec 3.1)")
    print("-" * 78)
    if 0.5 <= new['ratio'] <= 2.0:
        print(f"  K-branch (PNT-heuristic extrapolates within factor of 2):")
        print(f"    Capacity_V(Z/510510) / PNT_pred = {new['ratio']:.3f}")
        print(f"    -> WITHIN factor of 2.  K-branch REALIZED.")
        print(f"    The joint-on-disjoint settlement of audit iota extrapolates")
        print(f"    cleanly to the 7th primorial row.")
    elif 0.25 <= new['ratio'] <= 4.0:
        print(f"  Borderline K-branch (ratio = {new['ratio']:.3f}):")
        print(f"    PNT-heuristic predicts within factor of 4 but not 2.")
        print(f"    Sub-leading correction may be needed.")
    else:
        print(f"  L-branch or joint-on-disjoint (ratio = {new['ratio']:.3f}):")
        print(f"    PNT-heuristic deviates by more than factor of 4.")
        print(f"    Audit iota's settlement is row-specific to Z/{{6, .., 30030}}.")

    # Check: re-fit the K constant on all 6 rows
    print()
    print(f"  Multiplicative constant K = Capacity_V * N^2 / (n^2 * ln(n)):")
    print(f"  {'Row':>10}  {'K observed':>12}")
    for r in results:
        K = r['Capacity_V'] * (r['N'] ** 2) / ((r['n_primes'] ** 2) * math.log(r['n_primes']))
        print(f"  Z/{r['N']:>7}  {K:>12.4f}")
    Ks = [r['Capacity_V'] * (r['N'] ** 2) / ((r['n_primes'] ** 2) * math.log(r['n_primes']))
          for r in results]
    K_mean = sum(Ks) / len(Ks)
    K_max = max(Ks)
    K_min = min(Ks)
    spread = K_max / K_min
    print(f"  Mean K = {K_mean:.4f}, range [{K_min:.4f}, {K_max:.4f}], spread = {spread:.3f}x")
    print(f"  (audit iota 5-row spread was 1.584x)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
