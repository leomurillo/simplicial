#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_theta_capacity_scaling_primorial_ladder.py
=================================================

Audit theta:  primorial-ladder Capacity_V scaling for Paper 48 (proposed,
v2insert-03 / v2insert-08).  Extends audit eta (v2insert-08, on Z/30) to the
next three primorial rows -- Z/210 = 2*3*5*7, Z/2310 = 2*3*5*7*11, and
Z/30030 = 2*3*5*7*11*13 -- and fixes the empirical scaling law of
Capacity_V along the primorial ladder.

Anchored objects (Paper 35 sec 3.3):

  - Paper 32 sec 6.2 Lemma 6.1a (Pontryagin selection rule
    T_{klm} != 0 iff k+l+m == 0 mod N)
  - v2insert-03 sec 1.3 (Conductor Capacity Bound definition)
  - v2insert-08 (audit eta settlement on Z/6 + Z/30; the two data points
    this audit extends)

Discipline (Paper 35 sec 3):

  - Deterministic, no seeds (sec 3.4)
  - Integer arithmetic in every membership / vanishing decision
  - Closed-form total count via orbit counting on ordered closing triples;
    pure-V enumeration O(|V|^2) directly from the single-prime axes set
  - For N > 210, the |M|^2 per-class breakdown is SKIPPED (memory / time
    blowup at Z/30030 would be ~900M operations); only headline numbers
    reported.  Per-class breakdown still done for N <= 210.
  - Pontryagin orthogonality is algebraically exact by character
    orthogonality on (Z/N)^∧; the numerical projector check is only
    performed for N <= 210.  For N > 210 the orthogonality is stated as
    algebraically guaranteed (anchored to Paper 32 Lemma 6.1a).

Three-outcome pre-claim (v2insert-04 sec 3.1) for this audit:

  K-branch  : Capacity_V continues to decay monotonically along the
              primorial ladder, with a decay-factor pattern consistent
              with the Z/6 -> Z/30 8.3x decrease.
  L-branch  : Capacity_V stalls at some primorial row (decay factor ~ 1).
  joint-on- : Capacity_V increases on some primorial row, or shows
  disjoint    non-monotone behavior (e.g., spike at Z/210 then decay).

All three branches publishable.

Output: stdout transcript; intended to be captured to file
`audit_theta_capacity_scaling_primorial_ladder_run_output.txt` via tee.
"""

from __future__ import annotations
from math import gcd
from itertools import combinations_with_replacement
from collections import Counter
import sys
import time

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy required.")
    sys.exit(1)


# ----------------------------------------------------------------------------
# Conductor lattice machinery (duplicated from audits_alpha_eta_z30 for
# reproducibility-discipline -- each audit script is self-contained)
# ----------------------------------------------------------------------------
def conductor(k: int, N: int) -> int:
    if k == 0:
        return 1
    return N // gcd(k, N)


def euler_phi(d: int) -> int:
    if d == 1:
        return 1
    result = d
    p = 2
    temp = d
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def prime_factors(d: int) -> set[int]:
    facs = set()
    temp = d
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            facs.add(p)
            temp //= p
        p += 1
    if temp > 1:
        facs.add(temp)
    return facs


def is_single_prime(d: int) -> bool:
    return d != 1 and len(prime_factors(d)) == 1


def build_packets(N: int) -> dict[int, list[int]]:
    pk: dict[int, list[int]] = {}
    for k in range(N):
        d = conductor(k, N)
        pk.setdefault(d, []).append(k)
    return pk


def vm_partition(N: int, packets: dict[int, list[int]]):
    V_idx, M_idx, triv_idx = [], [], []
    for d, ks in packets.items():
        if d == 1:
            triv_idx.extend(ks)
        elif is_single_prime(d):
            V_idx.extend(ks)
        else:
            M_idx.extend(ks)
    return sorted(V_idx), sorted(M_idx), sorted(triv_idx)


# ----------------------------------------------------------------------------
# Closed-form total count of unordered closing multisets in {1,...,N-1}^3
# ----------------------------------------------------------------------------
def closing_multiset_counts(N: int) -> tuple[int, int, int, int]:
    """Returns (T_total, T_all_equal, T_two_equal, T_distinct).

    Derivation (orbit counting):
      # ordered triples (a,b,c) in {0,...,N-1}^3 with a+b+c == 0 mod N:
          for each (a,b), c is determined => N^2.
      # ordered with at least one 0: 3N - 2 (inclusion-exclusion).
      # ordered with all nonzero: N^2 - 3N + 2 = (N-1)(N-2).

      Each unordered multiset corresponds to:
        - 6 ordered triples if all distinct
        - 3 ordered triples if exactly two equal
        - 1 ordered triple if all equal

      T_all_equal = # of a in {1,...,N-1} with 3a == 0 mod N
                  = phi-like: solutions of 3a == 0 are a = N*j/gcd(3,N)
                    for j = 0,1,...,gcd(3,N)-1.  Excluding a=0 gives
                    gcd(3,N) - 1 valid values.
        For 3|N: gcd(3,N) = 3, so T_all_equal = 2.
        Otherwise: T_all_equal = 0.

      T_two_equal: # of unordered {a,a,c} with a != c, a,c in {1,...,N-1},
                   2a + c == 0 mod N.
        For each a in {1,...,N-1}, c = (-2a) mod N is determined.
        c = 0 iff 2a == 0 mod N iff a = N/2 (only if N even).
        c = a iff 3a == 0 mod N (the all-equal case).
        So # valid a's = (N-1) - (1 if N even else 0) - (gcd(3,N) - 1).

      6*T_distinct + 3*T_two_equal + T_all_equal = (N-1)(N-2)
      T_distinct = ((N-1)(N-2) - 3*T_two_equal - T_all_equal) / 6
      T_total = T_distinct + T_two_equal + T_all_equal."""
    g3 = gcd(3, N)
    T_all = g3 - 1  # excludes a=0; valid only if 3|N giving 2 values

    N_even = 1 if N % 2 == 0 else 0
    T_two = (N - 1) - N_even - (g3 - 1)

    ordered_nonzero = (N - 1) * (N - 2)
    T_distinct_x6 = ordered_nonzero - 3 * T_two - T_all
    assert T_distinct_x6 % 6 == 0, (
        f"orbit-counting modulo failure on N={N}: {T_distinct_x6} not divisible by 6"
    )
    T_distinct = T_distinct_x6 // 6
    T_total = T_distinct + T_two + T_all
    return T_total, T_all, T_two, T_distinct


# ----------------------------------------------------------------------------
# Pure-V multiset enumeration (efficient: only enumerates within V)
# ----------------------------------------------------------------------------
def pure_V_count(N: int, V_idx: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    V_set = set(V_idx)
    V_sorted = sorted(V_idx)
    n = len(V_sorted)
    count = 0
    multisets: list[tuple[int, int, int]] = []
    for i in range(n):
        a = V_sorted[i]
        for j in range(i, n):
            b = V_sorted[j]
            c = (-(a + b)) % N
            if c == 0:
                continue
            if c < b:
                continue
            if c in V_set:
                count += 1
                multisets.append((a, b, c))
    return count, multisets


# ----------------------------------------------------------------------------
# Pontryagin numerical check (only for N <= 210)
# ----------------------------------------------------------------------------
def pontryagin_check(N: int, V_idx: list[int], M_idx: list[int]):
    char = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            char[j, k] = np.exp(2j * np.pi * k * j / N) / np.sqrt(N)
    V_proj = np.zeros((N, N), dtype=complex)
    for k in V_idx:
        v = char[:, k]
        V_proj += np.outer(v, v.conj())
    M_proj = np.zeros((N, N), dtype=complex)
    for k in M_idx:
        v = char[:, k]
        M_proj += np.outer(v, v.conj())
    overlap = V_proj @ M_proj
    return float(np.linalg.norm(overlap))


# ----------------------------------------------------------------------------
# Pure-M and cross counts (only for N <= 210, full O(N^2) enumeration)
# ----------------------------------------------------------------------------
def full_class_breakdown(N: int, V_idx: list[int], M_idx: list[int]):
    V_set = set(V_idx)
    M_set = set(M_idx)
    classes: Counter = Counter()
    total = 0
    for a in range(1, N):
        for b in range(a, N):
            c = (-(a + b)) % N
            if c == 0:
                continue
            if c < b:
                continue
            total += 1
            cats = []
            for x in (a, b, c):
                if x in V_set:
                    cats.append("V")
                elif x in M_set:
                    cats.append("M")
                else:
                    cats.append("?")
            cats.sort()
            classes["".join(cats)] += 1
    return total, classes


# ----------------------------------------------------------------------------
# Audit row
# ----------------------------------------------------------------------------
def audit_row(N: int) -> dict:
    print("-" * 78)
    label = f"Z/{N}"
    primes = sorted(prime_factors(N))
    prime_str = "*".join(str(p) for p in primes) if primes else "1"
    print(f" Auditing R = {label}Z   (= {prime_str})")
    print("-" * 78)

    pk = build_packets(N)
    V_idx, M_idx, triv_idx = vm_partition(N, pk)
    dim_V = len(V_idx)
    dim_M = len(M_idx)
    dim_dyn = N - 1
    assert dim_V + dim_M == dim_dyn, f"V+M != dim_dyn on N={N}"

    print(f"  dim_V = {dim_V}  (single-prime conductor packets, sum of phi(p))")
    print(f"  dim_M = {dim_M}  (cross-prime carry packets, total - V)")
    print(f"  dim_dynamical = {dim_dyn}  (V + M check: {dim_V} + {dim_M} = {dim_dyn})")
    print(f"  V/M dimensional ratio: {dim_V}/{dim_M} = "
          f"{dim_V/dim_M:.6f}")

    # Closed-form total count
    t0 = time.perf_counter()
    T_total, T_all, T_two, T_distinct = closing_multiset_counts(N)
    t_total_time = time.perf_counter() - t0
    print(f"  Total closing unordered multisets {{a<=b<=c}} from {{1,...,{N-1}}}")
    print(f"    with a+b+c == 0 (mod {N}):  total = {T_total}")
    print(f"      all-equal:    {T_all}")
    print(f"      two-equal:    {T_two}")
    print(f"      all-distinct: {T_distinct}")
    print(f"    [closed-form orbit count, {t_total_time*1000:.3f} ms]")

    # Pure-V enumeration
    t0 = time.perf_counter()
    pure_V, pure_V_triples = pure_V_count(N, V_idx)
    t_pureV_time = time.perf_counter() - t0
    print(f"  Pure-V closing multisets: {pure_V}/{T_total}  "
          f"=  Capacity_V = {pure_V/T_total:.8f}")
    print(f"    [O(|V|^2) = O({dim_V}^2) = {dim_V*dim_V} enumeration, "
          f"{t_pureV_time*1000:.3f} ms]")
    if pure_V <= 16:
        print(f"  Pure-V multisets (explicit):")
        for t in pure_V_triples:
            print(f"    {t}  (sum = {sum(t)})")
    else:
        print(f"  Pure-V multisets: too many to list ({pure_V}); skipped explicit print")

    # Full class breakdown only for N <= 210
    if N <= 210:
        t0 = time.perf_counter()
        total_check, classes = full_class_breakdown(N, V_idx, M_idx)
        t_full_time = time.perf_counter() - t0
        assert total_check == T_total, (
            f"closed-form total ({T_total}) != full enum total ({total_check}) on N={N}"
        )
        print(f"  Full class breakdown (cross-checks closed form):")
        for cls in sorted(classes.keys()):
            cnt = classes[cls]
            pct = 100.0 * cnt / T_total
            print(f"    {cls:>5}: {cnt:>10}  ({pct:>5.2f}%)")
        print(f"    [O(N^2) = O({N}^2) = {N*N} enumeration, "
              f"{t_full_time*1000:.3f} ms]")
        pure_M = classes.get("MMM", 0)
    else:
        print(f"  Full class breakdown SKIPPED (N > 210; O(N^2) too slow / memory).")
        pure_M = None

    # Pontryagin check only for N <= 210
    if N <= 210:
        t0 = time.perf_counter()
        overlap = pontryagin_check(N, V_idx, M_idx)
        t_pq_time = time.perf_counter() - t0
        print(f"  Pontryagin character orthogonality numerical check:")
        print(f"    ||V_proj * M_proj||_F = {overlap:.6e}  "
              f"(machine floor; algebraic value: 0)")
        print(f"    [{N}x{N} projectors, {t_pq_time*1000:.3f} ms]")
    else:
        print(f"  Pontryagin check (numerical) SKIPPED (N > 210; "
              f"{N}x{N} complex matrix exceeds budget).")
        print(f"    Algebraic value: 0 exactly, by Pontryagin character orthogonality")
        print(f"    on (Z/{N})^* with disjoint V/M index sets (Paper 32 Lemma 6.1a).")
        overlap = None

    print()

    return {
        "N": N,
        "primes": primes,
        "dim_V": dim_V,
        "dim_M": dim_M,
        "T_total": T_total,
        "T_all_equal": T_all,
        "T_two_equal": T_two,
        "T_distinct": T_distinct,
        "pure_V": pure_V,
        "capacity_V": pure_V / T_total if T_total else 0.0,
        "pontryagin_overlap": overlap,
        "pure_M": pure_M,
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(" audit theta -- Capacity_V scaling on the primorial ladder")
    print(" Z/6, Z/30, Z/210, Z/2310, Z/30030  (squarefree primorials P_n)")
    print(" Settles Paper 48 (proposed, v2insert-03) quantitative shape.")
    print(" Anchored: Paper 32 Lemma 6.1a; v2insert-08 (Z/6 + Z/30 anchors).")
    print("=" * 78)
    print()

    rows = [6, 30, 210, 2310, 30030]
    results = {}
    t_start = time.perf_counter()
    for N in rows:
        r = audit_row(N)
        results[N] = r
    t_total = time.perf_counter() - t_start
    print(f"  Total audit wall time across {len(rows)} rows: {t_total:.3f} seconds")
    print()

    # Anchor verification against v2insert-08
    print("=" * 78)
    print(" ANCHOR VERIFICATION (v2insert-08 results on Z/6 and Z/30)")
    print("=" * 78)
    print()
    expected = {
        6: {"dim_V": 3, "dim_M": 2, "T_total": 6, "pure_V": 2,
            "capacity_V": 2/6},
        30: {"dim_V": 7, "dim_M": 22, "T_total": 150, "pure_V": 6,
             "capacity_V": 6/150},
    }
    all_ok = True
    for N, exp in expected.items():
        r = results[N]
        for key, expected_val in exp.items():
            observed = r[key]
            if isinstance(expected_val, float):
                ok = abs(observed - expected_val) < 1e-9
            else:
                ok = observed == expected_val
            status = "OK" if ok else "MISMATCH"
            if not ok:
                all_ok = False
            print(f"  Z/{N}  {key:>12}: expected {expected_val}, observed "
                  f"{observed}  [{status}]")
    if all_ok:
        print(f"  All v2insert-08 anchors reproduced exactly.")
    else:
        print(f"  ANCHOR MISMATCH -- audit cannot proceed without reconciliation.")
        return 1
    print()

    # Scaling table
    print("=" * 78)
    print(" SCALING TABLE: Capacity_V along the primorial ladder")
    print("=" * 78)
    print()
    header = (
        "  primorial   |    n_primes |  dim_V  | dim_M  | "
        "T_total      | pure_V  | Capacity_V   | log10(Cap_V) | "
        "decay vs prev"
    )
    print(header)
    print("  " + "-" * (len(header) - 2))
    prev_cap = None
    for N in rows:
        r = results[N]
        prime_str = "*".join(str(p) for p in r["primes"])
        n_primes = len(r["primes"])
        cap = r["capacity_V"]
        log_cap = (np.log10(cap) if cap > 0 else float("-inf"))
        decay = f"{prev_cap/cap:.3f}x" if prev_cap and cap > 0 else "  -- "
        primorial_str = f"Z/{N}=" + prime_str
        print(f"  {primorial_str:>13} | {n_primes:>11} | {r['dim_V']:>6} | "
              f"{r['dim_M']:>6} | {r['T_total']:>11} | "
              f"{r['pure_V']:>6} | {cap:>10.8f}  |   {log_cap:>8.4f}   |  {decay:>9}")
        prev_cap = cap
    print()

    # Scaling analysis
    print("=" * 78)
    print(" SCALING ANALYSIS")
    print("=" * 78)
    print()

    # Fit log10(Capacity_V) vs n (= number of primes)
    n_vals = np.array([len(results[N]["primes"]) for N in rows])
    cap_vals = np.array([results[N]["capacity_V"] for N in rows])
    log_cap_vals = np.log10(cap_vals)

    print(f"  n (# primes):     {n_vals.tolist()}")
    print(f"  log10(Capacity_V): {[f'{x:.4f}' for x in log_cap_vals]}")
    print()

    # Linear fit: log10(Cap_V) = a * n + b  (i.e., Cap_V = 10^b * 10^(a*n))
    A = np.vstack([n_vals, np.ones_like(n_vals)]).T.astype(float)
    coef, *_ = np.linalg.lstsq(A, log_cap_vals, rcond=None)
    a, b = float(coef[0]), float(coef[1])
    print(f"  Best-fit linear: log10(Capacity_V) = {a:.4f} * n + {b:.4f}")
    print(f"  Equivalently: Capacity_V ~ {10**b:.4e} * 10^({a:.4f}*n)")
    print(f"  Per-prime decay factor: 10^({a:.4f}) = {10**a:.4f} per added prime")
    print(f"  Equivalently: Capacity_V shrinks by 1/{1/10**a:.2f} per primorial step")
    print()

    # Residuals
    fitted = a * n_vals + b
    residuals = log_cap_vals - fitted
    print(f"  Residuals (observed - fitted): {[f'{r:+.4f}' for r in residuals]}")
    print(f"  Max abs residual: {np.max(np.abs(residuals)):.4f}")
    if np.max(np.abs(residuals)) < 0.1:
        print(f"    -- Excellent linear fit in log space (residuals < 0.1 log10).")
    elif np.max(np.abs(residuals)) < 0.3:
        print(f"    -- Good linear fit in log space (residuals < 0.3 log10).")
    else:
        print(f"    -- Residuals exceed 0.3 log10; nonlinear behavior present.")
    print()

    # Decay factor table
    print("  Decay factor per primorial step (Capacity_V[n] / Capacity_V[n+1]):")
    for i in range(len(rows) - 1):
        N1, N2 = rows[i], rows[i+1]
        c1, c2 = results[N1]["capacity_V"], results[N2]["capacity_V"]
        if c2 > 0:
            factor = c1 / c2
            print(f"    {N1:>6} -> {N2:>6} (added prime {results[N2]['primes'][-1]}): "
                  f"decay factor = {factor:.3f}x")
        else:
            print(f"    {N1:>6} -> {N2:>6}: Capacity_V[{N2}] = 0; "
                  f"saturation reached")
    print()

    # Three-outcome adjudication
    print("=" * 78)
    print(" ADJUDICATION (audit theta, v2insert-04 sec 3.1 three-outcome rule)")
    print("=" * 78)
    print()
    monotone_decay = all(
        results[rows[i]]["capacity_V"] > results[rows[i+1]]["capacity_V"]
        for i in range(len(rows) - 1)
        if results[rows[i+1]]["capacity_V"] > 0
    )
    if monotone_decay:
        print("  REALIZED BRANCH: K  --  Capacity_V decays MONOTONICALLY along the")
        print("                          primorial ladder Z/6 -> Z/30 -> Z/210 ->")
        print("                          Z/2310 -> Z/30030.  Empirical scaling law")
        print("                          fits log10(Capacity_V) = a*n + b with")
        print(f"                          a = {a:.4f}, b = {b:.4f}.")
        print(f"                          Per-prime decay factor: 1/{1/10**a:.2f}.")
        print("                          v2insert-03 sec 1.3 / Paper 48 C2's")
        print("                          'decays rapidly with primorial growth'")
        print("                          confirmed quantitatively at five data points.")
    else:
        print("  REALIZED BRANCH: L or joint-on-disjoint  --  monotone decay broken")
        print("                          on at least one primorial step.")
    print()
    print(f"  Pontryagin orthogonality (Paper 47 C3 row-generalization):")
    for N in rows:
        r = results[N]
        if r["pontryagin_overlap"] is not None:
            print(f"    Z/{N}: ||V*M||_F = {r['pontryagin_overlap']:.6e}  (numerical)")
        else:
            print(f"    Z/{N}: V*M = 0  (algebraic, by Pontryagin character orthogonality)")
    print()
    print(f"  For all five primorial rows, V and M character index sets are disjoint")
    print(f"  by construction; Pontryagin orthogonality holds algebraically on every")
    print(f"  row (Paper 32 Lemma 6.1a generalized).  Paper 47 C3 row-generalization")
    print(f"  is now confirmed on five primorial rows.")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
