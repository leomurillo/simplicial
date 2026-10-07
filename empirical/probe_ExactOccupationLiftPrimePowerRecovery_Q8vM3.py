"""Probe for Note_ExactOccupationLiftPrimePowerRecovery_Q8vM3.

Checks the finite algebraic identity

    D_s Pi_sa sum_{k<=K} H_s^k/k
      = sum_{p<=p_n, r<=K} log(p) p^{-rs} e_{r e_p}

in the polynomial symmetric-algebra normalization, and displays CRT aliasing
that makes single-axis extraction ill-defined after compression.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import math


PRIMES = (2, 3, 5)
K = 7


Monomial = tuple[int, ...]
Poly = dict[Monomial, Fraction]


def zero() -> Monomial:
    return (0,) * len(PRIMES)


def add_alpha(a: Monomial, b: Monomial) -> Monomial:
    return tuple(x + y for x, y in zip(a, b))


def degree(a: Monomial) -> int:
    return sum(a)


def is_single_axis(a: Monomial) -> bool:
    return sum(1 for x in a if x) == 1


def multiply(A: Poly, B: Poly) -> Poly:
    out: Poly = defaultdict(Fraction)
    for a, ca in A.items():
        for b, cb in B.items():
            out[add_alpha(a, b)] += ca * cb
    return dict(out)


def scale(A: Poly, c: Fraction) -> Poly:
    return {a: c * ca for a, ca in A.items()}


def add(A: Poly, B: Poly) -> Poly:
    out: Poly = defaultdict(Fraction)
    for a, ca in A.items():
        out[a] += ca
    for a, cb in B.items():
        out[a] += cb
    return {a: c for a, c in out.items() if c}


def H_poly() -> Poly:
    out: Poly = {}
    for i, _p in enumerate(PRIMES):
        a = [0] * len(PRIMES)
        a[i] = 1
        out[tuple(a)] = Fraction(1)
    return out


def log_series(K: int) -> Poly:
    H = H_poly()
    power = {zero(): Fraction(1)}
    total: Poly = {}
    for k in range(1, K + 1):
        power = multiply(power, H)
        total = add(total, scale(power, Fraction(1, k)))
    return total


@dataclass(frozen=True)
class DerivedCoeff:
    alpha: Monomial
    rational_coeff_before_D: Fraction
    D_log_weight: float
    expected_log_weight: float
    error: float


def derived_single_axis_coeffs(K: int) -> list[DerivedCoeff]:
    L = log_series(K)
    out: list[DerivedCoeff] = []
    for alpha, coeff in sorted(L.items(), key=lambda item: (degree(item[0]), item[0])):
        if not is_single_axis(alpha):
            continue
        idx = next(i for i, x in enumerate(alpha) if x)
        r = alpha[idx]
        logp = math.log(PRIMES[idx])
        D_weight = float(coeff) * r * logp
        out.append(
            DerivedCoeff(
                alpha=alpha,
                rational_coeff_before_D=coeff,
                D_log_weight=D_weight,
                expected_log_weight=logp,
                error=abs(D_weight - logp),
            )
        )
    return out


def crt_label(alpha: Monomial) -> Monomial:
    return tuple(a % p for a, p in zip(alpha, PRIMES))


def all_occupations_of_degree(k: int) -> list[Monomial]:
    out: list[Monomial] = []

    def rec(pos: int, remaining: int, current: list[int]) -> None:
        if pos == len(PRIMES) - 1:
            out.append(tuple(current + [remaining]))
            return
        for v in range(remaining + 1):
            rec(pos + 1, remaining - v, current + [v])

    rec(0, k, [])
    return out


def alias_report(max_degree: int) -> list[tuple[int, Monomial, list[Monomial], list[Monomial]]]:
    rows = []
    for k in range(1, max_degree + 1):
        labels: dict[Monomial, list[Monomial]] = defaultdict(list)
        for alpha in all_occupations_of_degree(k):
            labels[crt_label(alpha)].append(alpha)
        for label, alphas in sorted(labels.items()):
            singles = [a for a in alphas if is_single_axis(a)]
            mixed = [a for a in alphas if not is_single_axis(a)]
            if singles and mixed:
                rows.append((k, label, singles, mixed))
    return rows


def mixed_pollution_example() -> None:
    # Degree 5 at row (2,3,5): 5e_5 and 2e_2+3e_3 both compress to (0,0,0).
    alpha_single = (0, 0, 5)
    alpha_mixed = (2, 3, 0)
    L = log_series(5)
    coeff_single = L[alpha_single]
    coeff_mixed = L[alpha_mixed]
    D_single = float(coeff_single) * 5 * math.log(5)
    D_mixed = float(coeff_mixed) * (2 * math.log(2) + 3 * math.log(3))
    print("\nCompression-before-projection pollution example")
    print(f"single alpha={alpha_single}, label={crt_label(alpha_single)}, coeff before D={coeff_single}, D weight={D_single:.12e}")
    print(f"mixed  alpha={alpha_mixed}, label={crt_label(alpha_mixed)}, coeff before D={coeff_mixed}, D weight={D_mixed:.12e}")
    print("Upstairs Pi_sa keeps the first and kills the second; compressed labels cannot decide this.")


def main() -> None:
    print("Exact occupation-lift prime-power recovery probe")
    print(f"prime row={PRIMES}, occupation cutoff K={K}")

    coeffs = derived_single_axis_coeffs(K)
    max_error = max(c.error for c in coeffs)
    print(f"\nmax single-axis coefficient error after D_s: {max_error:.3e}")
    print("sample single-axis coefficients: alpha, coeff before D, D weight, expected log p")
    for c in coeffs[:10]:
        print(
            f"  {c.alpha}: {c.rational_coeff_before_D} -> "
            f"{c.D_log_weight:.12e} vs {c.expected_log_weight:.12e}"
        )

    print("\nFixed-degree CRT aliasing with both single-axis and mixed occupations")
    rows = alias_report(K)
    for k, label, singles, mixed in rows[:8]:
        print(f"  degree={k}, label={label}, singles={singles[:3]}, mixed={mixed[:3]}")
    print(f"total polluted labels through degree {K}: {len(rows)}")

    print("\nCross-degree occupation-depth aliasing on one axis")
    for i, p in enumerate(PRIMES):
        a = [0] * len(PRIMES)
        b = [0] * len(PRIMES)
        a[i] = 1
        b[i] = 1 + p
        print(f"  axis p={p}: {tuple(a)} and {tuple(b)} both compress to {crt_label(tuple(a))}")

    mixed_pollution_example()


if __name__ == "__main__":
    main()

