"""Sign-aware gate scan for the Pass-3 ordinary-tail completion.

The first gate interval probe used symmetric moment errors:

    mu_m -> mu_m +/- eps_m.

But the omitted ordinary tail has a known sign pattern. Each missing
occupation atom contributes

    delta mu_m = (-1)^(m+1) * positive_m.

So the actual completion lives in a one-sided box:

    odd  m: mu_m <= completed_mu_m <= mu_m + eps_m,
    even m: mu_m - eps_m <= completed_mu_m <= mu_m.

This probe evaluates gate determinants over the corners of that one-sided
box. Corner scanning is an exploratory determinant-aware diagnostic, not a
formal global polynomial bound; it is sharper than the symmetric Leibniz
radius and reveals whether the sign information is already enough to move
the gates into the positive chamber.
"""

from __future__ import annotations

from itertools import product

import mpmath as mp

import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def one_sided_ranges(mu: list[mp.mpf], eps: list[mp.mpf]) -> list[tuple[mp.mpf, mp.mpf]]:
    ranges: list[tuple[mp.mpf, mp.mpf]] = []
    for m, (center, radius) in enumerate(zip(mu, eps), start=1):
        if m % 2 == 1:
            ranges.append((center, center + radius))
        else:
            ranges.append((center - radius, center))
    return ranges


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def corner_scan(
    kind: str, i: int, ranges: list[tuple[mp.mpf, mp.mpf]], support: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    needed = 2 * i + 1 if kind == "D" else 2 * i + 2
    lo = mp.inf
    hi = -mp.inf
    for bits in product([0, 1], repeat=needed):
        mu = [ranges[j][bits[j]] for j in range(needed)]
        val = gate_value(kind, i, mu, support)
        lo = min(lo, val)
        hi = max(hi, val)
    return lo, hi


def verdict(lo: mp.mpf, hi: mp.mpf) -> str:
    if lo > 0:
        return "positive"
    if hi < 0:
        return "negative"
    return "crosses"


def main() -> None:
    order = 8
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    a_theta = mp.mpf("1.01")
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = mp.mpf(primes[-1])
    eps = gates.ordinary_tail_error_radii(order, x, r_cut, a_theta)
    ranges = one_sided_ranges(mu, eps)

    print("Pass-3 sign-aware gate corner scan")
    print(
        f"prime_count={prime_count}, X={primes[-1]}, r_cut={r_cut}, "
        f"mobius_cutoff={mobius_cutoff}, A_theta={a_theta}"
    )
    print("Omitted ordinary tail sign: delta_m has sign (-1)^(m+1).")
    print()

    print("One-sided moment ranges")
    print("m   low                 high                contains true eta moment?")
    import probe_pass3_eta_total_hankel_gates as eta

    true_mu = eta.total_ells(None, order)
    for m in range(1, order + 1):
        lo, hi = ranges[m - 1]
        contains = lo <= true_mu[m - 1] <= hi
        print(
            f"{m:1d}  {fmt(lo, 14):>18} {fmt(hi, 14):>18} {str(contains):>10}"
        )
    print()

    print("Corner scan over one-sided ordinary-tail box")
    print("gate  corner low          corner high         verdict")
    for kind in ["D", "G"]:
        for i in range(4):
            lo, hi = corner_scan(kind, i, ranges, support)
            print(f"{kind}{i:<3} {fmt(lo, 12):>18} {fmt(hi, 12):>18} {verdict(lo, hi):>10}")
    print()

    print("Interpretation")
    print("- One-sided signs narrow the admissible completion region.")
    print("- If a gate still crosses zero here, sign alone is insufficient.")
    print("- The next step would need lower theta bounds or exact r=3 evaluation, not just upper radii.")


if __name__ == "__main__":
    main()
