"""Three-gate half-compensation dashboard.

This combines the interior H gate, lower J gate, and upper K gate into one
notation check:

    winning defect - challenging defect = normalized Schur pivot.

For H and K the endpoint carrier is negative debt, so the winning defect is
Archimedean overpayment.  For J the endpoint carrier is positive credit, so
the winning defect is zeta underconsumption.

Numerical evidence only; this verifies that the three-gate theorem target is
being written with the correct orientations.
"""

from __future__ import annotations

import mpmath as mp

from probe_pass3_t5_pivot_component_ledger import (
    boundary,
    component_moments,
    fmt,
    monic_residual,
    square_value,
)


mp.mp.dps = 90


def shifted(components: dict[str, list[mp.mpf]]) -> dict[str, list[mp.mpf]]:
    return {name: moments[1:] for name, moments in components.items()}


def pieces(poly: list[mp.mpf], ledgers: dict[str, list[mp.mpf]]) -> dict[str, mp.mpf]:
    return {
        "endpoint": square_value(poly, ledgers["endpoint"]),
        "arch": square_value(poly, ledgers["arch"]),
        "zeta": square_value(poly, ledgers["zeta"]),
    }


def debt_gate_row(
    gate: str,
    ledgers: dict[str, list[mp.mpf]],
    n: int,
) -> tuple[str, int, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    poly = monic_residual(ledgers["total"], n)
    row = pieces(poly, ledgers)
    pivot = row["endpoint"] + row["arch"] + row["zeta"]
    scale = -row["endpoint"]
    winner = row["arch"] / scale - mp.mpf("0.5")
    challenger = mp.mpf("0.5") - row["zeta"] / scale
    return gate, n, pivot / scale, winner, challenger, winner - challenger


def credit_gate_row(
    gate: str,
    ledgers: dict[str, list[mp.mpf]],
    n: int,
) -> tuple[str, int, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    poly = monic_residual(ledgers["total"], n)
    row = pieces(poly, ledgers)
    pivot = row["endpoint"] + row["arch"] + row["zeta"]
    scale = row["endpoint"]
    winner = mp.mpf("0.5") - (-row["zeta"] / scale)
    challenger = -row["arch"] / scale - mp.mpf("0.5")
    return gate, n, pivot / scale, winner, challenger, winner - challenger


def main() -> None:
    max_n = 5
    order = 2 * max_n + 12
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)

    components = component_moments(order)
    lower_components = shifted(components)
    upper_components = {
        name: boundary(moments, radius) for name, moments in components.items()
    }

    print("Pass-3 T6 three-gate half-compensation dashboard")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print("gate n normalized pivot    winning defect      challenging defect  margin check")
    for n in range(max_n + 1):
        rows = [
            debt_gate_row("H", components, n),
            credit_gate_row("J", lower_components, n),
            debt_gate_row("K", upper_components, n),
        ]
        for gate, rung, surplus, winner, challenger, margin in rows:
            print(
                f"{gate:>4} {rung:1d} "
                f"{fmt(surplus, 12):>18} "
                f"{fmt(winner, 12):>18} "
                f"{fmt(challenger, 12):>20} "
                f"{fmt(margin, 12):>16}"
            )
        print()

    print("Interpretation")
    print("- H/K: winning defect = Archimedean overpayment of endpoint debt.")
    print("- J: winning defect = zeta underconsumption of endpoint credit.")
    print("- The margin column equals the normalized pivot in each gate.")


if __name__ == "__main__":
    main()
