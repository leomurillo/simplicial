"""Lower-gate half-compensation ledger for the Pass-3 RMS proof target.

The Hausdorff/Stieltjes support certificate has a lower localizer

    J_n = (mu_{a+b+1}) = Gram_{L_0}(1,t,...,t^n),
    L_0(f) = L(t f).

This probe gives that lower gate the same T6 RMS treatment as the interior
and upper gates.  The sign orientation flips: for the lower shifted ledger
the endpoint carrier is the large positive credit, while the Archimedean and
zeta pieces consume nearly one half each.  The positive lower pivot is the
small unconsumed remainder.

Numerical evidence only; this is a proof-target locator.
"""

from __future__ import annotations

import mpmath as mp

from probe_pass3_t5_pivot_component_ledger import (
    component_moments,
    fmt,
    monic_residual,
    square_value,
)


mp.mp.dps = 90


def shifted(components: dict[str, list[mp.mpf]]) -> dict[str, list[mp.mpf]]:
    """Moments for L_0(f)=L(t f)."""
    return {name: moments[1:] for name, moments in components.items()}


def print_lower_table(ledgers: dict[str, list[mp.mpf]], max_n: int) -> None:
    print("Lower-support residual squares U_n under shifted orthogonalization")
    print("n   lower pivot         endpoint credit      arch debt           zeta debt")
    rows: list[tuple[int, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for n in range(max_n + 1):
        poly = monic_residual(ledgers["total"], n)
        endpoint = square_value(poly, ledgers["endpoint"])
        arch = square_value(poly, ledgers["arch"])
        zeta = square_value(poly, ledgers["zeta"])
        total = endpoint + arch + zeta
        rows.append((n, total, endpoint, arch, zeta))
        print(
            f"{n:1d}  {fmt(total, 16):>20} "
            f"{fmt(endpoint, 16):>20} "
            f"{fmt(-arch, 16):>20} "
            f"{fmt(-zeta, 16):>20}"
        )

    print()
    print("normalized against endpoint credit")
    print("n   surplus/credit      arch-debt/credit    zeta-debt/credit    debt total")
    for n, total, endpoint, arch, zeta in rows:
        arch_debt = -arch / endpoint
        zeta_debt = -zeta / endpoint
        print(
            f"{n:1d}  {fmt(total/endpoint, 12):>18} "
            f"{fmt(arch_debt, 12):>18} "
            f"{fmt(zeta_debt, 12):>18} "
            f"{fmt(arch_debt + zeta_debt, 12):>18}"
        )

    print()
    print("midline defects around half-consumption")
    print("n   arch debt excess    zeta debt shortfall lower surplus")
    for n, total, endpoint, arch, zeta in rows:
        arch_excess = -arch / endpoint - mp.mpf("0.5")
        zeta_shortfall = mp.mpf("0.5") - (-zeta / endpoint)
        surplus = total / endpoint
        print(
            f"{n:1d}  {fmt(arch_excess, 12):>18} "
            f"{fmt(zeta_shortfall, 12):>20} "
            f"{fmt(surplus, 12):>18}"
        )


def main() -> None:
    max_n = 6
    order = 2 * max_n + 10
    components = component_moments(order)
    lower_components = shifted(components)

    print("Pass-3 T6 lower-gate half-compensation")
    print("L_0(f)=L(t f), so the shifted moments are mu_{k+1}.")
    print()
    print_lower_table(lower_components, max_n)
    print()
    print("Interpretation")
    print("- The lower gate is not a fourth idea; it is the shifted RMS gate.")
    print("- Its sign orientation is dual to the interior and upper gates.")
    print("- The proof target is zeta debt shortfall exceeding Archimedean debt excess.")


if __name__ == "__main__":
    main()
