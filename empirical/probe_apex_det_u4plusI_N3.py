#!/usr/bin/env python3
r"""N3 -- attempt det(U_N^4 + I) != 0 via the (HF)^4 structure.

GOAL. No-crossing <=> det(U_N^4 + I) != 0. Try to prove this algebraically from
M = HF (F symmetric, F^2 = reversal), as the N2 determinant det U_N = i^{-C(N-1,2)}
was proved via det U_N = det H . det F.

WHAT THE (HF)-STRUCTURE + N2 GIVE (genuine, proved):
  (a) det(U^4 + I) is REAL.  Because U^4 + I = U^2 (U^2 + U^{-2}), with
      det(U^2) = (det U)^2 = (i^{-C(N-1,2)})^2 = (-1)^{C(N-1,2)}  (N2 theorem),
      and U^2 + U^{-2} = U^2 + (U^*)^2 Hermitian (real determinant). Hence
          det(U^4 + I) = (-1)^{C(N-1,2)} . det(U^2 + U^{-2}).
  (b) det(U^4 + I) = 2^{N-1} prod_j cos(4 pi delta_j), where delta_j in [-1/8,1/8]
      is the signed distance of eigenvalue lambda_j to its nearest fourth root.
      (lambda_j^4 + 1 = 2 cos(4 pi delta_j) e^{4 pi i delta_j}; the phases combine
      to +-1 by reality, and to + by the N2 sign.) Hence
          0 <= det(U^4 + I) <= 2^{N-1},  with equality to 0 IFF some delta_j = 1/8.

VERDICT (honest, negative). The (HF)^4 structure does NOT yield an algebraic proof
of non-vanishing. det(U^4 + I) = 2^{N-1} prod_j cos(4 pi delta_j), and its strict
positivity is EXACTLY the no-crossing (no eigenvalue at a gap) -- a spectral fact,
equivalent to the leading-straggler bound. There is no shortcut because U^2+U^{-2}
is a SUM, not a product: the factorization det U = det H . det F that made the bare
determinant clean does not apply to det(U^4+I) = det(U^2) det(U^2+U^{-2}). The
hard core (delta_max < 1/8) is unchanged. What the structure buys is reality,
positivity, the Hermitian reduction, and the explicit value 2^{N-1} prod cos --
not the proof.

This script certifies identities (a),(b) exactly (machine-eps) for N=2..17.
"""

from __future__ import annotations

import json
from math import comb

import numpy as np


def U_block(N):
    w = np.exp(2j * np.pi / np.float64(N))
    j = np.arange(N)
    F = w ** np.outer(j, j) / np.sqrt(N)
    H = np.zeros((N, N))
    H[0, :] = 1 / np.sqrt(N)
    for k in range(1, N):
        H[k, :k] = 1.0
        H[k, k] = -k
        H[k] /= np.sqrt(k * (k + 1))
    return (H @ F.T)[1:, 1:]


def main():
    report = {"probe": "apex_det_u4plusI_N3"}
    rows = []
    ok = True
    for N in range(2, 18):
        U = U_block(N)
        n = N - 1
        I = np.eye(n)
        U2 = U @ U
        Ui2 = np.linalg.inv(U2)
        d4 = complex(np.linalg.det(np.linalg.matrix_power(U, 4) + I))
        dH = complex(np.linalg.det(U2 + Ui2))
        sgn = (-1) ** comb(N - 1, 2)

        ev = np.linalg.eigvals(U)
        roots = [1, 1j, -1, -1j]
        prodcos = 1.0
        for e in ev:
            c = int(np.argmin([abs(e - r) for r in roots]))
            dd = abs(np.angle(e / roots[c])) / (2 * np.pi)
            prodcos *= np.cos(4 * np.pi * dd)
        form = 2 ** n * prodcos

        real_ok = abs(d4.imag) < 1e-7
        ida = abs(d4.real - sgn * dH.real) < 1e-6        # (a)
        idb = abs(d4.real - form) < 1e-6                 # (b)
        pos = d4.real > 0
        ok &= real_ok and ida and idb and pos
        rows.append({"N": N, "det(U^4+I)": round(d4.real, 4), "imag": float(f"{abs(d4.imag):.1e}"),
                     "(-1)^C det(U^2+U^-2)": round(sgn * dH.real, 4),
                     "2^(N-1) prod cos": round(form, 4),
                     "prod cos": round(prodcos, 4),
                     "real&(a)&(b)&pos": bool(real_ok and ida and idb and pos)})

    report["rows"] = rows
    report["identities_hold_all_N"] = bool(ok)
    report["det_is_real_positive"] = bool(ok)
    report["algebraic_shortcut_found"] = False
    report["conclusion"] = ("det(U^4+I)=2^{N-1} prod cos(4 pi delta_j); strict "
                            "positivity = no-crossing (spectral). No algebraic "
                            "obstruction from (HF)^4 (det of a SUM, not a product).")
    report["PASS"] = bool(ok)

    print(json.dumps(report, indent=2))
    print("\n=== det(U^4+I) STRUCTURE CERTIFICATE ===")
    print(f"{'N':>3} | {'det(U^4+I)':>12} | {'(-1)^C det(U2+U-2)':>18} | {'2^(N-1)prodcos':>14} | prodcos")
    print("-" * 74)
    for r in rows:
        print(f"{r['N']:>3} | {r['det(U^4+I)']:>12.4f} | {r['(-1)^C det(U^2+U^-2)']:>18.4f} |"
              f" {r['2^(N-1) prod cos']:>14.4f} | {r['prod cos']:.4f}")
    print(f"\n(a) det(U^4+I) = (-1)^C(N-1,2) det(U^2+U^-2)  and  (b) = 2^(N-1) prod cos(4pi d_j): {ok}")
    print("Honest verdict: NO algebraic shortcut. det(U^4+I) = 2^{N-1} prod cos(4pi d_j);")
    print("strict positivity IS the no-crossing (spectral). (HF)^4 gives reality + the")
    print("Hermitian reduction, not the proof -- it's a det of a SUM, so det H . det F fails.")
    print(f"PASS = {report['PASS']}")
    return 0 if report["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
