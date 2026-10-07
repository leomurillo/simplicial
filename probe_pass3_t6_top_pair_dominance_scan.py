"""Scan the T6 top-pair dominance ratio across Pass-3 rungs.

The local induction target is

    Delta_{n,2n} > -sum_{m<2n} Delta_{n,m}.

This probe records:

    top      = Delta_{n,2n}
    lower    = sum_{m<2n} Delta_{n,m}
    total    = top + lower = h_n / S_n
    lower/top cancellation ratio = -lower/top
    total/top survival ratio = total/top

The same audit is run for the boundary-complement ladder.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 170


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def ell_endpoint(m: int) -> mp.mpf:
    return ((-1) ** m) * mp.mpf(4) ** m


def ell_archimedean(m: int) -> mp.mpf:
    c_arc = (
        (mp.mpf("0.5") ** (2 * m))
        * mp.polygamma(2 * m - 1, mp.mpf("0.25"))
        / factorial(2 * m)
    )
    return ((-1) ** (m + 1)) * m * c_arc


def component_moments(order: int) -> dict[str, list[mp.mpf]]:
    total = eta.total_ells(None, order)
    endpoint = [ell_endpoint(k + 1) for k in range(order)]
    arch = [ell_archimedean(k + 1) for k in range(order)]
    zeta = [total[k] - endpoint[k] - arch[k] for k in range(order)]
    return {"total": total, "endpoint": endpoint, "arch": arch, "zeta": zeta}


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def monic_residual(moments: list[mp.mpf], n: int) -> list[mp.mpf]:
    if n == 0:
        return [mp.mpf(1)]
    _, coeffs = pivots.schur_pivot(moments, n)
    return coeffs + [mp.mpf(1)]


def square_coefficients(poly: list[mp.mpf]) -> list[mp.mpf]:
    out = [mp.mpf(0) for _ in range(2 * len(poly) - 1)]
    for a, pa in enumerate(poly):
        for b, pb in enumerate(poly):
            out[a + b] += pa * pb
    return out


def dominance_row(moments: list[mp.mpf], ledgers: dict[str, list[mp.mpf]], n: int) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    poly = monic_residual(moments, n)
    coeffs = square_coefficients(poly)
    endpoint_packets = [coeffs[m] * ledgers["endpoint"][m] for m in range(2 * n + 1)]
    total_packets = [
        coeffs[m]
        * (ledgers["endpoint"][m] + ledgers["arch"][m] + ledgers["zeta"][m])
        for m in range(2 * n + 1)
    ]
    scale = -mp.fsum(endpoint_packets)
    normalized = [packet / scale for packet in total_packets]
    top = normalized[-1]
    lower = mp.fsum(normalized[:-1])
    total = top + lower
    return top, lower, total


def print_scan(label: str, moments: list[mp.mpf], ledgers: dict[str, list[mp.mpf]], max_n: int) -> None:
    print(label)
    print("n   top Delta          lower sum          total surplus      -lower/top        total/top")
    previous_survival: mp.mpf | None = None
    for n in range(1, max_n + 1):
        try:
            top, lower, total = dominance_row(moments, ledgers, n)
        except Exception as exc:  # noqa: BLE001 - diagnostic probe
            print(f"{n:2d}  failed: {exc}")
            continue
        cancel = -lower / top
        survive = total / top
        ratio_to_prev = "" if previous_survival is None else fmt(survive / previous_survival, 10)
        previous_survival = survive
        print(
            f"{n:2d}  {fmt(top, 12):>16} {fmt(lower, 12):>18} "
            f"{fmt(total, 12):>18} {fmt(cancel, 14):>16} {fmt(survive, 14):>16} "
            f"{ratio_to_prev:>14}"
        )
    print()


def main() -> None:
    max_n = 10
    order = 2 * max_n + 8
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    components = component_moments(order)
    boundary_components = {
        name: boundary(moments, radius) for name, moments in components.items()
    }

    print("Pass-3 T6 top-pair dominance scan")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print("last column: survival ratio divided by previous survival ratio")
    print()
    print_scan("Interior ladder", components["total"], components, max_n)
    print_scan("Boundary-complement ladder", boundary_components["total"], boundary_components, max_n)
    print("Interpretation")
    print("- The cancellation ratio approaches 1 from below when the gate is positive.")
    print("- The survival ratio is the tiny uncancelled fraction of the top pair.")
    print("- Since the survival ratio decays, a proof needs an explicit positive asymptotic.")


if __name__ == "__main__":
    main()
