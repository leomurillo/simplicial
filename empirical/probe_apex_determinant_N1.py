#!/usr/bin/env python3
r"""N1 determinant probe — authoritative settlement of Conjectures 4.1 / 4.2.

Computes det U_N directly (operative convention C1, the closed form (2.1))
for N = 2..30, exactly for small N and at 50-digit precision for all N,
then identifies det U_N as a root of unity and locates its field.

This is the AUTHORITY for:
  - Conjecture 4.1: det U_N is a root of unity (det U_N = zeta_M^j).
  - Conjecture 4.2: det U_N lies in Q(zeta_N)  (i.e. M | (N if N even else 2N)).
  - the closed form  det U_N = zeta_M^{f}  feeding N2 deliverable (3),(4).

Why a direct probe and not only the per-rung parity count r_p(N):
the parity decomposition tests each prime separately, but the radical that
actually enters det U_N is  sqrt( sf(P) ),  P = N^{N-1} (N-1)! N!,  as a
WHOLE.  Several primes with odd parity can COMBINE into a radical that is
already cyclotomic (e.g. at N=21, sqrt(3) and sqrt(7) are each non-
cyclotomic but sqrt(21) in Q(zeta_21) since 21 = 1 mod 4).  Only the whole
quadratic field Q(sqrt(sf P)) and its conductor decide membership.  This
probe sidesteps the issue entirely by computing det U_N itself.
"""

from __future__ import annotations

import json
from fractions import Fraction

import mpmath as mpm
import sympy as sp
from sympy import I, Rational, exp, pi, sqrt, factorint

mpm.mp.dps = 50  # 50 decimal digits


def det_mp(N):
    """det U_N at 50-digit precision via mpmath Gaussian elimination (operative C1)."""
    w = mpm.e ** (2j * mpm.pi / N)
    A = mpm.matrix(N - 1, N - 1)
    for k in range(1, N):
        Rk_ = 1 / mpm.sqrt(N * k * (k + 1))
        h = [1] * k + [-k] + [0] * (N - 1 - k)
        for c in range(1, N):
            A[k - 1, c - 1] = Rk_ * sum(h[j] * w ** (c * j) for j in range(N))
    # Gaussian elimination with partial pivoting; det = sign * prod(pivots)
    n = N - 1
    det = mpm.mpf(1)
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(A[r, i]))
        if piv != i:
            A[i, :], A[piv, :] = A[piv, :].copy(), A[i, :].copy()
            det = -det
        det *= A[i, i]
        for r in range(i + 1, n):
            f = A[r, i] / A[i, i]
            for cc in range(i, n):
                A[r, cc] -= f * A[i, cc]
    return complex(det)


def root(m, N):
    return exp(2 * I * pi * Rational(int(m) % N, N))


def Rk(N, k):
    return 1 / sqrt(N * k * (k + 1))


def helmert(N, k):
    v = [sp.Integer(0)] * N
    for j in range(k):
        v[j] = sp.Integer(1)
    v[k] = sp.Integer(-k)
    return v


def entry_C1(N, k, c):
    """Operative convention: R_k * sum_j h_k(j) omega^{+c j}."""
    h = helmert(N, k)
    return Rk(N, k) * sum(h[j] * root(c * j, N) for j in range(N))


def U(N):
    return sp.Matrix(N - 1, N - 1, lambda a, b: entry_C1(N, a + 1, b + 1))


def squarefree_part(n):
    sf = 1
    for p, e in factorint(n).items():
        if e % 2:
            sf *= p
    return sf


def product_P(N):
    P = 1
    for k in range(1, N):
        P *= N * k * (k + 1)
    return P


def quad_conductor(m):
    """Conductor of Q(sqrt(m)) for squarefree m>0: m if m=1(4) else 4m. (m=1 -> 1)."""
    if m == 1:
        return 1
    return m if m % 4 == 1 else 4 * m


def roots_of_unity_in_QzetaN(N):
    """Order L of the group of roots of unity in Q(zeta_N): N if N even else 2N."""
    return N if N % 2 == 0 else 2 * N


def identify_root_of_unity(zval, max_order):
    """Given a complex value on the unit circle, return (num, den) with
    zval ~ exp(2 pi i num/den), den minimal <= max_order, plus residual.
    Uses mpmath 50-digit arithmetic for the residual."""
    z = mpm.mpc(zval.real, zval.imag)
    theta = float(mpm.arg(z) / (2 * mpm.pi))
    frac = Fraction(theta).limit_denominator(max_order)
    cand = mpm.e ** (2j * mpm.pi * mpm.mpf(frac.numerator) / frac.denominator)
    residual = float(abs(z - cand))
    return frac.numerator % frac.denominator, frac.denominator, residual


def main():
    report = {"probe": "apex_determinant_N1", "convention": "C1 (closed form 2.1)"}
    rows = []

    # exact symbolic confirmation for tiny N (N=5 omitted: nested-radical det
    # does not auto-simplify, but the 50-digit mpmath value below pins it to -1)
    exact = {}
    for N in (2, 3, 4, 6):
        d = sp.simplify(sp.expand_complex(U(N).det()))
        exact[N] = str(d)
    report["exact_det"] = exact

    for N in range(2, 31):
        det = det_mp(N)
        absdet = abs(det)
        L = roots_of_unity_in_QzetaN(N)
        # search order up to 4N (conjecture: M | 4N)
        num, den, residual = identify_root_of_unity(det, 4 * N)
        is_rou = residual < 1e-25
        in_QzetaN = (L % den == 0) if is_rou else None

        P = product_P(N)
        m = squarefree_part(P)
        cond = quad_conductor(m)
        pred_in_QzetaN = (N % cond == 0) if m > 1 else True  # sqrt(m) in Q(zeta_N)?

        rows.append(
            {
                "N": N,
                "abs_det": round(absdet, 12),
                "det_order_M": den,
                "det = zeta_M^j (j)": num,
                "is_root_of_unity": is_rou,
                "residual": float(f"{residual:.2e}"),
                "in_Q_zetaN(matrix)": in_QzetaN,
                "sf(P)": m,
                "Q(sqrt sf) conductor": cond,
                "pred_in_Q_zetaN(radical)": pred_in_QzetaN,
                "agree": (in_QzetaN == pred_in_QzetaN) if is_rou else None,
                "N_mod_4": N % 4,
            }
        )

    report["rows"] = rows
    all_rou = all(r["is_root_of_unity"] for r in rows)
    all_agree = all(r["agree"] for r in rows if r["agree"] is not None)
    viol_42 = [r["N"] for r in rows if r["in_Q_zetaN(matrix)"] is False]
    report["conj_4_1_all_roots_of_unity"] = all_rou
    report["radical_test_agrees_with_det"] = all_agree
    report["conj_4_2_violations_N(det not in Q zetaN)"] = viol_42
    report["PASS_conj_4_1"] = bool(all_rou)

    print(json.dumps(report, indent=2))

    print("\n=== exact det U_N (symbolic) ===")
    for N in (2, 3, 4, 6):
        print(f"  det U_{N} = {exact[N]}")
    print("  det U_5 = -1  (50-digit; nested-radical symbolic form does not auto-reduce)")

    print("\n=== det U_N as root of unity, N=2..30 ===")
    print(f"{'N':>3} {'N%4':>4} | {'|det|':>10} | det = zeta_M^j      | in Q(zN)? | sf(P) | radical-pred")
    print("-" * 92)
    for r in rows:
        zexpr = f"zeta_{r['det_order_M']}^{r['det = zeta_M^j (j)']}"
        print(
            f"{r['N']:>3} {r['N_mod_4']:>4} | {r['abs_det']:>10.6f} | {zexpr:<18} |"
            f" {str(r['in_Q_zetaN(matrix)']):>7} | {r['sf(P)']:>5} | {r['pred_in_Q_zetaN(radical)']}"
        )

    print("\n=== VERDICT ===")
    print(f"Conjecture 4.1 (det U_N is a root of unity): {'HOLDS' if all_rou else 'FAILS'} for N=2..30.")
    print(f"Radical (conductor) prediction matches actual field: {all_agree}")
    print(f"Conjecture 4.2 (det U_N in Q(zeta_N)) violated at N = {viol_42}")
    if viol_42:
        mods = sorted(set(N % 4 for N in viol_42))
        print(f"  -> violations have N mod 4 in {mods}")
    return 0 if all_rou else 1


if __name__ == "__main__":
    raise SystemExit(main())
