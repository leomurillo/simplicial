#!/usr/bin/env python3
r"""Lemma B certificate: det Htilde_N = (-1)^{N-1} N!  in closed form.

Htilde_N is the N x N integer Helmert matrix:
  row 0    = (1, 1, ..., 1)                          [all ones]
  row k>=1 = ( 1,...,1 [k ones], -k, 0,...,0 )       [ = h_k ]

The closed-form proof expands det along the LAST column (column N-1),
which has exactly two nonzero entries:
  (0,    N-1) = 1
  (N-1,  N-1) = -(N-1)
and reduces to the exact recursion  det Htilde_N = -N det Htilde_{N-1},
solved by  det Htilde_N = (-1)^{N-1} N!.

This script certifies every structural claim used in that derivation,
EXACTLY (sympy integer determinants), for N = 1..14:

  (S1) column N-1 of Htilde_N has nonzeros only at rows {0, N-1},
       with values {1, -(N-1)}.
  (S2) minor M_{N-1,N-1} = det Htilde_{N-1}.
  (S3) minor M_{0,N-1}  = (-1)^{N-2} det Htilde_{N-1}
       (the deleted block B is the cyclic row-shift of Htilde_{N-1}).
  (S4) cofactor identity:
       det Htilde_N = (+1)(-1)^{0+(N-1)} M_{0,N-1}
                      + (-(N-1))(-1)^{2(N-1)} M_{N-1,N-1}
                    = -N det Htilde_{N-1}.
  (S5) closed form: det Htilde_N = (-1)^{N-1} N!.
"""

from __future__ import annotations

import json
from math import factorial

import sympy as sp


def Htilde(N):
    rows = [[sp.Integer(1)] * N]
    for k in range(1, N):
        rows.append([sp.Integer(1)] * k + [sp.Integer(-k)] + [sp.Integer(0)] * (N - 1 - k))
    return sp.Matrix(rows)


def minor(M, r, c):
    return M.minor_submatrix(r, c).det()


def main():
    report = {"lemma": "det Htilde_N = (-1)^{N-1} N!"}
    rows = []
    ok_all = True
    for N in range(1, 15):
        H = Htilde(N)
        detH = H.det()

        # (S5) closed form
        s5 = detH == (-1) ** (N - 1) * factorial(N)

        if N == 1:
            rows.append({"N": 1, "detH": int(detH), "closed_form": int((-1) ** 0 * 1),
                         "S1": True, "S2": True, "S3": True, "S4": True, "S5": bool(s5)})
            ok_all &= bool(s5)
            continue

        # (S1) last column structure
        col = [H[r, N - 1] for r in range(N)]
        nz = [(r, int(col[r])) for r in range(N) if col[r] != 0]
        s1 = nz == [(0, 1), (N - 1, -(N - 1))]

        # minors
        Hprev = Htilde(N - 1)
        detHprev = Hprev.det()
        M_last = minor(H, N - 1, N - 1)
        M_first = minor(H, 0, N - 1)

        # (S2)
        s2 = M_last == detHprev
        # (S3)
        s3 = M_first == (-1) ** (N - 2) * detHprev
        # (S4) full cofactor expansion along column N-1 equals -N det Htilde_{N-1}
        cof = (sp.Integer(1) * (-1) ** (0 + (N - 1)) * M_first
               + sp.Integer(-(N - 1)) * (-1) ** (2 * (N - 1)) * M_last)
        s4 = (cof == detH) and (cof == -N * detHprev)

        ok = s1 and s2 and s3 and s4 and s5
        ok_all &= ok
        rows.append({"N": N, "detH": int(detH), "closed_form": int((-1) ** (N - 1) * factorial(N)),
                     "S1": bool(s1), "S2": bool(s2), "S3": bool(s3), "S4": bool(s4), "S5": bool(s5)})

    report["rows"] = rows
    report["PASS"] = bool(ok_all)
    print(json.dumps(report, indent=2))
    print("\n=== LEMMA B CERTIFICATE ===")
    print(f"{'N':>3} | {'det Htilde_N':>14} | {'(-1)^(N-1) N!':>14} | S1 S2 S3 S4 S5")
    print("-" * 64)
    for r in rows:
        flags = " ".join("Y" if r[s] else "N" for s in ("S1", "S2", "S3", "S4", "S5"))
        print(f"{r['N']:>3} | {r['detH']:>14} | {r['closed_form']:>14} |  {flags}")
    print(f"\nRecursion det Htilde_N = -N det Htilde_(N-1) and closed form "
          f"(-1)^(N-1) N! certified N=1..14:  PASS = {ok_all}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
