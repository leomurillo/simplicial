#!/usr/bin/env python3
r"""N3 trace tower -- field trace of tr U_N over Q(zeta_N).

Corrects and replaces the N1 Sec 5 conjecture
    Tr_{L_N/Q(zeta_N)}(tr U_N) = 0  for all N
which is FALSE (first failure N=5, value -2 zeta_5).

THEOREM (proved by character orthogonality).
Let L_N = K_N . Q(zeta_N), F = Q(zeta_N), Gamma = Gal(L_N/F) (an elementary
abelian 2-group of order 2^s, s = pi(N) - t(N), acting by sign changes on the
quadratic radicals not already in F). The diagonal entry (U_N)_{kk} = R_k C_{kk}
has R_k = 1/sqrt(N k(k+1)) in K_N and C_{kk} in Z[omega] subset F. Each tau in
Gamma fixes C_{kk} and sends R_k -> eps_k(tau) R_k for a sign character eps_k.
By orthogonality sum_{tau} eps_k(tau) = 2^s [R_k in F], so

    Tr_{L_N/F}( (U_N)_{kk} ) = 2^s (U_N)_{kk}   if k in S_N,  else 0,

    Tr_{L_N/F}( tr U_N ) = 2^s * Sigma_N,   Sigma_N = sum_{k in S_N} (U_N)_{kk},

where  S_N = { k in 1..N-1 : sqrt(sf(N k(k+1))) in Q(zeta_N) }
            = { k : cond(Q(sqrt(sf(N k(k+1))))) | N }.

Consequences:
  (i)  The GENUINELY NON-CYCLOTOMIC part rho_N = sum_{k not in S_N} (U_N)_{kk}
       has vanishing field trace -- the always-true generalization of the N=4
       case (where S_4 = empty so tr U_4 IS entirely non-cyclotomic).
  (ii) Tr_{L_N/F}(tr U_N) = 0  <=>  Sigma_N = 0.  Empirically (N<=60) this holds
       <=> S_N = empty; the conjecture "always 0" fails whenever S_N is nonempty.

This script VERIFIES the theorem by an INDEPENDENT brute-force Galois sum: it
builds Gamma explicitly (sign assignments on primes <= N that fix Q(zeta_N)) and
sums tau(tr U_N) over tau in Gamma, comparing to 2^s Sigma_N at 30-digit
precision. PASS iff (a) Galois sum == 2^s Sigma_N for all N tested,
(b) Tr(rho_N) == 0 for all N, (c) the first nonzero field trace is at N=5.
"""

from __future__ import annotations

import itertools
import json

import mpmath as mpm
from sympy import factorint, primerange

mpm.mp.dps = 30


def sf(n):
    s = 1
    for p, e in factorint(n).items():
        if e % 2:
            s *= p
    return s


def cond(m):
    if m == 1:
        return 1
    return m if m % 4 == 1 else 4 * m


def in_cyclo(m, N):
    """sqrt(m) in Q(zeta_N) for squarefree m>=1."""
    return N % cond(m) == 0


def Udiag(N, k):
    """(U_N)_{kk} = R_k C_kk at 30-digit precision."""
    w = mpm.e ** (2j * mpm.pi / N)
    Rk = 1 / mpm.sqrt(N * k * (k + 1))
    C = sum(w ** (k * j) for j in range(k)) - k * w ** (k * k)
    return Rk * C


def gamma_group(N, primes):
    """All sign assignments chi in {+-1}^primes that fix Q(zeta_N):
    prod_{p in S} chi(p) = +1 for every squarefree product m=prod S with
    sqrt(m) in Q(zeta_N). Returns list of dicts p->sign."""
    # cyclotomic subspace V = subsets S with sqrt(prod S) in Q(zeta_N)
    cyc_subsets = []
    for r in range(len(primes) + 1):
        for S in itertools.combinations(primes, r):
            m = 1
            for p in S:
                m *= p
            if in_cyclo(m, N):  # m squarefree by construction
                cyc_subsets.append(set(S))
    G = []
    for signs in itertools.product([1, -1], repeat=len(primes)):
        chi = dict(zip(primes, signs))
        ok = True
        for S in cyc_subsets:
            prod = 1
            for p in S:
                prod *= chi[p]
            if prod != 1:
                ok = False
                break
        if ok:
            G.append(chi)
    return G


def main():
    report = {"probe": "apex_trace_fieldtrace_N3", "dps": 30}
    rows = []
    all_formula_ok = True
    all_rho_zero = True
    first_nonzero = None

    for N in range(2, 31):
        primes = list(primerange(2, N + 1))
        diag = {k: Udiag(N, k) for k in range(1, N)}
        m = {k: sf(N * k * (k + 1)) for k in range(1, N)}
        S = [k for k in range(1, N) if in_cyclo(m[k], N)]
        Sigma = sum((diag[k] for k in S), mpm.mpc(0))
        rho = sum((diag[k] for k in range(1, N) if k not in S), mpm.mpc(0))

        G = gamma_group(N, primes)
        s_exp = len(primes) - (len(S) and 0)  # placeholder; real s = log2|G|
        s_exp = round(mpm.log(len(G), 2))

        # brute-force Galois sum of tr U_N and of rho_N
        def galois_sum(weights):
            tot = mpm.mpc(0)
            for chi in G:
                acc = mpm.mpc(0)
                for k, val in weights.items():
                    sgn = 1
                    for p in factorint(m[k]):
                        sgn *= chi[p]
                    acc += sgn * val
                tot += acc
            return tot

        tr_fieldtrace = galois_sum(diag)              # Tr_{L/F}(tr U_N)
        rho_fieldtrace = galois_sum({k: diag[k] for k in range(1, N) if k not in S})

        formula = (2 ** s_exp) * Sigma
        ok_formula = abs(tr_fieldtrace - formula) < mpm.mpf(10) ** (-20)
        ok_rho = abs(rho_fieldtrace) < mpm.mpf(10) ** (-20)
        all_formula_ok &= ok_formula
        all_rho_zero &= ok_rho

        nonzero = abs(tr_fieldtrace) > mpm.mpf(10) ** (-20)
        if nonzero and first_nonzero is None:
            first_nonzero = N

        rows.append({
            "N": N, "primes": len(primes), "s=log2|Gamma|": s_exp,
            "S_N": S, "|S_N|": len(S),
            "field_trace_abs": float(abs(tr_fieldtrace)),
            "matches 2^s*Sigma": bool(ok_formula),
            "Tr(rho)=0": bool(ok_rho),
            "vanishes": not nonzero,
        })

    report["rows"] = rows
    first_nontrivial = next((r["N"] for r in rows if r["N"] >= 3 and not r["vanishes"]), None)
    report["formula_holds_all_N"] = bool(all_formula_ok)
    report["rho_fieldtrace_zero_all_N"] = bool(all_rho_zero)
    report["first_N_with_nonzero_fieldtrace"] = first_nonzero  # N=2 (degenerate U_2=[1])
    report["first_nontrivial_N_with_nonzero_fieldtrace"] = first_nontrivial  # N=5
    report["conjecture_Tr_eq_0_is_false"] = first_nonzero is not None
    report["PASS"] = bool(all_formula_ok and all_rho_zero and first_nontrivial == 5)

    print(json.dumps(report, indent=2))

    print("\n=== TRACE FIELD-TRACE THEOREM CERTIFICATE ===")
    print(f"{'N':>3} {'|S_N|':>5} {'s':>3} | {'|Tr_{L/F}(tr U_N)|':>18} | {'=2^s*Sigma?':>11} | {'Tr(rho)=0?':>10} | vanishes")
    print("-" * 80)
    for r in rows:
        print(f"{r['N']:>3} {r['|S_N|']:>5} {r['s=log2|Gamma|']:>3} | {r['field_trace_abs']:>18.6f} |"
              f" {str(r['matches 2^s*Sigma']):>11} | {str(r['Tr(rho)=0']):>10} | {r['vanishes']}")
    print(f"\nField-trace formula  Tr = 2^s * Sigma_N  holds for all N=2..30: {all_formula_ok}")
    print(f"Non-cyclotomic part rho_N has vanishing field trace (always):    {all_rho_zero}")
    print(f"Conjecture 'Tr = 0 for all N' is FALSE; first nonzero at N = {first_nonzero}")
    print(f"PASS = {report['PASS']}")
    return 0 if report["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
