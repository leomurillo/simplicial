"""Probe the native Hankel/Stieltjes lock for folded xi cumulants.

Given S(x)=log(Xi(i sqrt(x))/Xi(0)) and

    S'(x)=sum_{n>=0} (-1)^n mu_n x^n,
    mu_n = ell_{n+1},

the trace-gauge Stieltjes target is

    mu_n = int_0^R t^n d sigma(t)

for a positive finite measure on [0,R]. This script computes the moment
sequence from folded coefficients and checks finite Hankel/localizing
matrices:

    H0[i,j] = mu_{i+j}
    H1[i,j] = mu_{i+j+1}
    HR[i,j] = R*mu_{i+j} - mu_{i+j+1}

Numerical evidence only; not a proof.
"""

from __future__ import annotations

import importlib.util
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


def hankel(moments: list[mp.mpf], size: int, shift: int = 0) -> mp.matrix:
    return mp.matrix([[moments[i + j + shift] for j in range(size)] for i in range(size)])


def localizing_upper(moments: list[mp.mpf], size: int, r: mp.mpf) -> mp.matrix:
    return mp.matrix(
        [[r * moments[i + j] - moments[i + j + 1] for j in range(size)] for i in range(size)]
    )


def min_eig_symmetric(mat: mp.matrix) -> mp.mpf:
    vals = mp.eigsy(mat, eigvals_only=True)
    return min(vals)


def fmt(x: mp.mpf, digits: int = 10) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    max_size = 8
    order = 2 * max_size + 6
    b = folded_probe.folded_coefficients(order + 2, radius=mp.mpf("1.0"), samples=2048)
    ell = folded_probe.formal_log_cumulants(b, order + 1)
    mu = ell  # mu_n = ell_{n+1}; ell list is 1-indexed by meaning.

    gamma1 = mp.im(mp.zetazero(1))
    r = 1 / (gamma1 * gamma1)

    print(f"R candidate gamma_1^-2 = {fmt(r, 24)}")
    print("size  min eig H0        min eig H1        min eig HR        det H0")
    for size in range(1, max_size + 1):
        h0 = hankel(mu, size, 0)
        h1 = hankel(mu, size, 1)
        hr = localizing_upper(mu, size, r)
        det_h0 = mp.det(h0)
        print(
            f"{size:2d}  {fmt(min_eig_symmetric(h0), 12):>14} "
            f"{fmt(min_eig_symmetric(h1), 12):>14} "
            f"{fmt(min_eig_symmetric(hr), 12):>14} "
            f"{fmt(det_h0, 12):>14}"
        )


if __name__ == "__main__":
    main()
