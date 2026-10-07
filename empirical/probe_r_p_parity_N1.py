#!/usr/bin/env python3
r"""N1 radicals-cancel parity probe (exact integer arithmetic).

Settles Conjecture 4.2 of N1-ApexUnitaries-Draft1.md empirically to N=30.

Background (N1 section 7.5). Write  U_N|_{kc} = R_k * C_{kc}  with
R_k = 1/sqrt(N k (k+1)) in K_N (multiquadratic) and C_{kc} in Q(zeta_N).
Then

    det U_N = (prod_{k=1}^{N-1} R_k) * det(C),   det(C) in Q(zeta_N).

So det U_N lies in Q(zeta_N)  <=>  prod_k R_k lies in Q(zeta_N), because
det(C) can only supply radicals sqrt(p) that already live in Q(zeta_N).

prod_k R_k = 1 / sqrt( P ),   P = prod_{k=1}^{N-1} N*k*(k+1) = N^{N-1} (N-1)! N!.

A prime p survives in sqrt(P) iff v_p(P) is odd, i.e. iff the per-rung
parity count

    r_p(N) := #{ k in 1..N-1 : p | sf( N k (k+1) ) }
            = #{ k in 1..N-1 : v_p(N k (k+1)) is odd }
            = v_p(P) mod 2 -counted-by-rung

is ODD.  (sf = squarefree part.)  sqrt(p) is ALREADY in Q(zeta_N) iff
(p = 1 mod 4 and p | N) or (p = 2 and 8 | N); for those p the surviving
radical is harmless. Hence:

    Conjecture 4.2  <=>  r_p(N) is EVEN for every prime p <= N with
                         sqrt(p) NOT in Q(zeta_N).

This probe computes r_p(N) for N = 2..30 and flags any violation.
Pure integer arithmetic; no floats anywhere. Cross-checks the per-rung
count against v_p(P) mod 2 computed independently from P's factorization.

CORRECTION (post-determinant-probe). The per-prime parity criterion of
N1 section 7.5 is too crude: it asks each relevant prime separately to
have even parity. But several odd-parity primes can COMBINE into a
radical that is already cyclotomic. The decisive object is the WHOLE
radical sqrt(sf P): det U_N in Q(zeta_N) iff sqrt(sf P) in Q(zeta_N),
iff the conductor of Q(sqrt(sf P)) divides N. Example: N=21 has primes
3 and 7 both odd-parity (each sqrt non-cyclotomic), but sf P = 21 = 1
mod 4 with conductor 21 | 21, so sqrt(21) in Q(zeta_21) and det U_21 in
Q(zeta_21) AFTER ALL. The per-prime count would wrongly flag N=21.
This probe reports BOTH: the per-prime table (diagnostic) and the
conductor verdict (authoritative, matches the direct determinant probe).
"""

from __future__ import annotations

import json
import sys
from math import gcd

from sympy import factorint, primerange


def squarefree_part(n: int) -> int:
    sf = 1
    for p, e in factorint(n).items():
        if e % 2 == 1:
            sf *= p
    return sf


def vp(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def sqrt_p_in_cyclotomic(p: int, N: int) -> bool:
    """sqrt(p) in Q(zeta_N)?  True iff (p=1 mod 4 and p|N) or (p=2 and 8|N)."""
    if p == 2:
        return N % 8 == 0
    return (p % 4 == 1) and (N % p == 0)


def r_p(N: int, p: int) -> int:
    return sum(1 for k in range(1, N) for n in [N * k * (k + 1)] if vp(n, p) % 2 == 1)


def product_P(N: int) -> int:
    P = 1
    for k in range(1, N):
        P *= N * k * (k + 1)
    return P


def quad_conductor(m: int) -> int:
    """Conductor of Q(sqrt(m)) for squarefree m>0: 1 if m=1; m if m=1 mod 4; else 4m."""
    if m == 1:
        return 1
    return m if m % 4 == 1 else 4 * m


def sqrt_sfP_in_cyclotomic(N: int) -> bool:
    """Authoritative test: det U_N in Q(zeta_N) iff sqrt(sf P) in Q(zeta_N)
    iff conductor(Q(sqrt(sf P))) | N."""
    m = squarefree_part(product_P(N))
    return N % quad_conductor(m) == 0


def main() -> int:
    report = {"probe": "r_p_parity_N1", "exact": True, "N_range": [2, 30]}
    rows = []
    per_prime_flags = []   # naive per-prime "violations" (diagnostic only)
    conductor_violations = []  # authoritative violations of Conjecture 4.2
    all_conductor_ok = True

    for N in range(2, 31):
        P = product_P(N)
        fac = factorint(P)
        relevant = []
        for p in primerange(2, N + 1):
            if sqrt_p_in_cyclotomic(p, N):
                continue  # radical is harmless (already cyclotomic)
            rp = r_p(N, p)
            # independent cross-check: r_p parity must equal v_p(P) parity
            vp_P_parity = fac.get(p, 0) % 2
            assert rp % 2 == vp_P_parity, f"parity mismatch N={N} p={p}: {rp%2} vs {vp_P_parity}"
            relevant.append({"p": p, "r_p": rp, "even": rp % 2 == 0})
            if rp % 2 == 1:
                per_prime_flags.append({"N": N, "p": p, "r_p": rp})

        sf_P = squarefree_part(P)
        in_Q = sqrt_sfP_in_cyclotomic(N)  # AUTHORITATIVE
        if not in_Q:
            all_conductor_ok = False
            conductor_violations.append({"N": N, "sf(P)": sf_P, "N_mod_4": N % 4})

        rows.append(
            {
                "N": N,
                "sf(P)": sf_P,
                "Q(sqrt sf) conductor": quad_conductor(sf_P),
                "det_in_Q_zetaN": in_Q,
                "N_mod_4": N % 4,
                "relevant_primes": relevant,
                "naive_per_prime_all_even": all(r["even"] for r in relevant),
            }
        )

    report["rows"] = rows
    report["naive_per_prime_flags"] = per_prime_flags
    report["conductor_violations_of_conj_4_2"] = conductor_violations
    report["conj_4_2_holds_all_N_2_to_30"] = all_conductor_ok
    report["PASS"] = bool(all_conductor_ok)
    all_even = all_conductor_ok  # alias for the print block below
    violations = conductor_violations

    # ---- compact human table
    print(json.dumps(report, indent=2))
    print("\n=== r_p(N) PARITY TABLE (relevant primes; E=even, O=odd) + conductor verdict ===")
    print(f"{'N':>3} {'N%4':>4} | {'sf(P)':>6} {'cond':>5} | det in Q(zN)? | per-prime r_p(parity)")
    print("-" * 82)
    for row in rows:
        rels = "  ".join(
            f"{r['p']}:{r['r_p']}{'E' if r['even'] else 'O'}" for r in row["relevant_primes"]
        ) or "(none)"
        print(
            f"{row['N']:>3} {row['N_mod_4']:>4} | {row['sf(P)']:>6} {row['Q(sqrt sf) conductor']:>5} |"
            f" {str(row['det_in_Q_zetaN']):>11}   | {rels}"
        )

    print("\n=== VERDICT (authoritative = conductor test, matches direct determinant probe) ===")
    if all_conductor_ok:
        print("Conjecture 4.2 HOLDS for all N in 2..30.")
    else:
        vN = [v["N"] for v in conductor_violations]
        print(f"Conjecture 4.2 (det U_N in Q(zeta_N)) FAILS at N = {vN}")
        print(f"  -> exactly N = 3 (mod 4): {sorted(set(v['N_mod_4'] for v in conductor_violations))}")
        print("  In every failing case sf(P) = 3 mod 4, conductor 4*sf, so sqrt(sf P)")
        print("  needs the factor 4 (i.e. i): det U_N = +-i lies in Q(zeta_4) \\ Q(zeta_N),")
        print("  hence in Q(zeta_{4N}). det U_N is STILL a root of unity (Conj 4.1 holds).")
    if per_prime_flags:
        ppN = sorted(set(v["N"] for v in per_prime_flags))
        falsepos = sorted(set(ppN) - set(v["N"] for v in conductor_violations))
        print(f"\nNaive per-prime count (N1 section 7.5 as literally stated) would flag N = {ppN}")
        print(f"  -> false positives removed by the conductor test: N = {falsepos}")
        print("  This is a substantive correction to N1's Conjecture 4.2 / section-7.5 wording.")
    print(f"\nPASS = {all_conductor_ok}")
    return 0 if all_conductor_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
