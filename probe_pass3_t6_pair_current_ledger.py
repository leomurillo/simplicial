"""Quadratic pair-current ledger for the Pass-3 RMS pivots.

T6 says a square closure is a pair-current: coefficients mix by a+b=c.
For the Pass-3 residual pivots, the relevant square is

    P_n(t)^2 = sum_{a,b} p_a p_b t^{a+b}.

This probe groups the residual square by the pair degree m=a+b and charges
each packet to the endpoint, Archimedean, and zeta ledger pieces. It then
expresses the half-compensation proof target packetwise.

This is the polynomial analogue of the T6 conductor-mixing audit. It is not
yet a proof; it identifies the local dominance packets that a proof must
control.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 90


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
    return {
        "total": total,
        "endpoint": endpoint,
        "arch": arch,
        "zeta": zeta,
    }


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


def packet_rows(poly: list[mp.mpf], ledgers: dict[str, list[mp.mpf]]) -> list[dict[str, mp.mpf]]:
    coeffs = square_coefficients(poly)
    rows: list[dict[str, mp.mpf]] = []
    for m, coeff in enumerate(coeffs):
        rows.append(
            {
                "m": mp.mpf(m),
                "coeff": coeff,
                "endpoint": coeff * ledgers["endpoint"][m],
                "arch": coeff * ledgers["arch"][m],
                "zeta": coeff * ledgers["zeta"][m],
            }
        )
        rows[-1]["total"] = rows[-1]["endpoint"] + rows[-1]["arch"] + rows[-1]["zeta"]
    return rows


def summarize(
    label: str,
    moments: list[mp.mpf],
    ledgers: dict[str, list[mp.mpf]],
    n: int,
    compact: list[tuple[str, int, mp.mpf, mp.mpf, mp.mpf]],
) -> None:
    poly = monic_residual(moments, n)
    rows = packet_rows(poly, ledgers)
    endpoint = mp.fsum(row["endpoint"] for row in rows)
    arch = mp.fsum(row["arch"] for row in rows)
    zeta = mp.fsum(row["zeta"] for row in rows)
    total = endpoint + arch + zeta
    scale = -endpoint

    print(label)
    print(f"n={n}")
    print("residual polynomial coefficients, low to high:")
    print("  " + ", ".join(fmt(c, 10) for c in poly))
    print(
        f"pivot={fmt(total, 16)}  debt={fmt(scale, 16)}  "
        f"surplus/debt={fmt(total/scale, 14)}"
    )
    print("m  sq_coeff            endpoint/S          arch-excess packet  zeta-shortfall packet  surplus packet")
    for row in rows:
        m = int(row["m"])
        half_endpoint = row["endpoint"] / 2
        arch_excess = (row["arch"] + half_endpoint) / scale
        zeta_shortfall = -(row["zeta"] + half_endpoint) / scale
        surplus = row["total"] / scale
        print(
            f"{m:1d}  {fmt(row['coeff'], 12):>16} "
            f"{fmt(row['endpoint']/scale, 12):>18} "
            f"{fmt(arch_excess, 12):>20} "
            f"{fmt(zeta_shortfall, 12):>22} "
            f"{fmt(surplus, 12):>18}"
        )
    print(
        "sum"
        f"{'':>16} "
        f"{fmt(endpoint/scale, 12):>18} "
        f"{fmt((arch + endpoint/2)/scale, 12):>20} "
        f"{fmt(-(zeta + endpoint/2)/scale, 12):>22} "
        f"{fmt(total/scale, 12):>18}"
    )
    top = rows[-1]
    top_surplus = top["total"] / scale
    lower_surplus = total / scale - top_surplus
    compact.append((label, n, total / scale, top_surplus, lower_surplus))
    print()


def main() -> None:
    max_n = 4
    order = 2 * max_n + 6
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    components = component_moments(order)
    boundary_components = {
        name: boundary(moments, radius) for name, moments in components.items()
    }

    print("Pass-3 T6 quadratic pair-current ledger")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    compact: list[tuple[str, int, mp.mpf, mp.mpf, mp.mpf]] = []
    for n in range(1, max_n + 1):
        summarize(
            "Interior pair-current packets P_n^2",
            components["total"],
            components,
            n,
            compact,
        )
        summarize(
            "Boundary-complement pair-current packets Q_n^2",
            boundary_components["total"],
            boundary_components,
            n,
            compact,
        )

    print("Compact surplus summary")
    print("label        n   total surplus        top packet          lower correction")
    for label, n, total, top, lower in compact:
        short = "interior" if label.startswith("Interior") else "boundary"
        print(
            f"{short:<11} {n:1d} "
            f"{fmt(total, 12):>18} {fmt(top, 12):>18} {fmt(lower, 12):>22}"
        )
    print()

    print("Interpretation")
    print("- The column arch-excess packet sums to a_n.")
    print("- The column zeta-shortfall packet sums to b_n.")
    print("- The proof target is packetwise control of arch-excess minus zeta-shortfall.")


if __name__ == "__main__":
    main()
