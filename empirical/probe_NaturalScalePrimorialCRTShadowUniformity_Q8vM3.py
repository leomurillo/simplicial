"""Probe for Note_NaturalScalePrimorialCRTShadowUniformity_Q8vM3.

The theorem is a BDH/large-sieve mean-square statement.  This probe computes
the full-modulus compressed CRT shadow for small primorials:

    E_P(W; X) = phi(P)^(-1) sum_{a mod P}^* W(a)
                (psi(X; P, a) - X / phi(P)).

It compares the normalized weighted shadow with the worst residue discrepancy.
The point is qualitative: smooth compressed shadows are much smaller than
worst-residue demands, matching the theorem's L2 target.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i in range(limit + 1) if sieve[i]]


def primorials(count: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    acc = 1
    for p in primes_upto(100):
        acc *= p
        out.append((p, acc))
        if len(out) == count:
            break
    return out


def phi_squarefree(P: int) -> int:
    result = P
    x = P
    p = 2
    while p * p <= x:
        if x % p == 0:
            result = result // p * (p - 1)
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result = result // x * (x - 1)
    return result


def von_mangoldt_table(limit: int) -> list[float]:
    lam = [0.0] * (limit + 1)
    for p in primes_upto(limit):
        logp = math.log(p)
        power = p
        while power <= limit:
            lam[power] = logp
            power *= p
    return lam


def residue_psi(P: int, X: int) -> list[float]:
    lam = von_mangoldt_table(X)
    psi = [0.0] * P
    for m in range(1, X + 1):
        if lam[m]:
            psi[m % P] += lam[m]
    return psi


def gaussian_crt_window(a: int, P: int, centers: tuple[float, float] = (0.23, 0.67), sigma: float = 0.045) -> float:
    x = a / P
    total = 0.0
    for c in centers:
        d = min(abs(x - c), 1.0 - abs(x - c))
        total += math.exp(-(d * d) / (2 * sigma * sigma))
    return total


@dataclass
class ShadowStats:
    P: int
    X: int
    phi: int
    weighted_error_over_x: float
    rms_error_over_x: float
    worst_error_over_x: float
    window_l2_avg: float


def compute_shadow(P: int, alpha: float) -> ShadowStats:
    X = max(20, int(P**alpha))
    phi = phi_squarefree(P)
    psi = residue_psi(P, X)
    expected = X / phi

    weighted = 0.0
    w2 = 0.0
    err2 = 0.0
    worst = 0.0
    for a in range(P):
        if math.gcd(a, P) != 1:
            continue
        w = gaussian_crt_window(a, P)
        delta = psi[a] - expected
        weighted += w * delta
        w2 += w * w
        err2 += delta * delta
        worst = max(worst, abs(delta))

    compressed_error = abs(weighted / phi)
    return ShadowStats(
        P=P,
        X=X,
        phi=phi,
        weighted_error_over_x=compressed_error / X,
        rms_error_over_x=math.sqrt(err2 / phi) / X,
        worst_error_over_x=worst / X,
        window_l2_avg=math.sqrt(w2 / phi),
    )


def main() -> None:
    print("Natural-scale primorial CRT shadow uniformity probe")
    print("Full-modulus smooth compressed shadow, W = two Gaussian arcs on (Z/PZ)^*.")
    print()
    print(
        "p_n     P_n       alpha       X        phi(P)   "
        "|E_W|/X        RMS/X        worst/X      ||W||_2avg"
    )
    for p, P in primorials(7):
        if P < 30:
            continue
        for alpha in (1.05, 1.20):
            stats = compute_shadow(P, alpha)
            print(
                f"{p:3d} {P:9d} {alpha:7.2f} {stats.X:9d} {stats.phi:9d} "
                f"{stats.weighted_error_over_x:12.4e} "
                f"{stats.rms_error_over_x:12.4e} "
                f"{stats.worst_error_over_x:12.4e} "
                f"{stats.window_l2_avg:12.4e}"
            )


if __name__ == "__main__":
    main()

