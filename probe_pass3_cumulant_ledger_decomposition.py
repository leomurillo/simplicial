"""Decompose folded xi cumulants into native ledger pieces.

This probe is diagnostic, not a proof. It splits the local folded log

    S(x) = log(Xi(i sqrt(x)) / Xi(0))

using s = 1/2 + y, x = y^2, into:

    rational endpoint factor: log(1 - 4x)
    Archimedean gamma factor: centered log Gamma_R
    centered zeta residual: whatever remains locally

The point is to expose the cancellation ledger behind Pile III. The raw
Euler/prime action and the Archimedean/rational action are not separately
positive determinant ledgers; the trace-gauge object is the centered sum.
"""

from __future__ import annotations

import importlib.util
from math import factorial
from pathlib import Path

import mpmath as mp


mp.mp.dps = 100

PROBE_PATH = Path(__file__).with_name("probe_pass3_folded_xi_trace_model.py")
spec = importlib.util.spec_from_file_location("folded_probe", PROBE_PATH)
folded_probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folded_probe)
mp.mp.dps = 100
folded_probe.mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    order = 10
    b = folded_probe.folded_coefficients(order + 2, radius=mp.mpf("1.0"), samples=1536)
    ell_total = folded_probe.formal_log_cumulants(b, order)

    print("m  ell_total              ell_rat                ell_arc                ell_zeta_residual")
    for m in range(1, order + 1):
        # S_rat(x)=log(1-4x), and S=sum (-1)^(m+1) ell_m x^m / m.
        ell_rat = ((-1) ** m) * mp.mpf(4) ** m

        # S_arc(x)=1/2[f(1/2+y)+f(1/2-y)-2f(1/2)] with
        # f(s)=log Gamma_R(s). For 2m >= 2,
        # [y^(2m)] S_arc = (1/2)^(2m) psi^(2m-1)(1/4)/(2m)!.
        c_arc = (mp.mpf("0.5") ** (2 * m)) * mp.polygamma(2 * m - 1, mp.mpf("0.25")) / factorial(2 * m)
        ell_arc = ((-1) ** (m + 1)) * m * c_arc

        ell_zeta = ell_total[m - 1] - ell_rat - ell_arc

        print(
            f"{m:2d} {fmt(ell_total[m-1], 20):>23} "
            f"{fmt(ell_rat, 20):>23} "
            f"{fmt(ell_arc, 20):>23} "
            f"{fmt(ell_zeta, 20):>23}"
        )


if __name__ == "__main__":
    main()
