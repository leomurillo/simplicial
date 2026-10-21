"""Numerical diagnostics for an explicit translated Weil-form test.

No RH inference from finite data. No interval certification is claimed.
The prime computation uses a sieve and math.fsum; selected sums are independently
recomputed using 50-digit mpmath arithmetic. Output paths are beside this script.
"""
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np


def prime_powers(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p:limit + 1:p] = b"\x00" * (((limit - p * p) // p) + 1)
    data = []
    for p in range(2, limit + 1):
        if sieve[p]:
            n = p
            while n <= limit:
                data.append((n, p))
                n *= p
    return sorted(data)


def g(v):
    u = abs(v)
    return (4 * mp.exp(-u) - mp.exp(u)) / 2 if u <= mp.log(2) else mp.mpf(0)


def G(s):
    if s == 1 or s == -1:
        return mp.mpf(3) * mp.log(2) / 2
    return (5 - 4 * mp.cosh(mp.log(2) * s)) / (1 - s * s)


def arch_correction(X):
    x = mp.mpf(X)
    a = mp.log(2)
    return x ** (-mp.mpf(5) / 2) * mp.quad(
        lambda v: g(v) * mp.exp(mp.mpf(5) * v / 2)
        / (1 - mp.exp(2 * v) / (x * x)), [-a, 0, a]
    )


def main():
    mp.mp.dps = 50
    a = mp.log(2)
    A = 4 * (5 - 3 * mp.sqrt(2)) / 3
    q0 = 2 * A - mp.mpf('1.5') * (
        mp.euler + mp.log(4 * mp.pi) + mp.log(mp.tanh(a / 2))
    ) - mp.quad(lambda v: (mp.exp(v / 2) * g(v) - mp.mpf('1.5'))
                / mp.sinh(v) if v else -mp.mpf('1.75'), [0, a])
    transform_checks = []
    for s in [mp.mpf('.5'), mp.mpc('.375', 14), mp.mpc(0, 21)]:
        direct = mp.quad(lambda v: g(v) * mp.exp(-s * v), [-a, 0, a])
        transform_checks.append(float(abs(direct - G(s))))
    data = prime_powers(2_000_000)
    ns = np.array([n for n, _ in data], dtype=np.float64)
    lps = np.array([math.log(p) for _, p in data], dtype=np.float64)
    samples = [3, 10, 100, 1000, 10000, 100000, 1000000]
    records = []
    for X in samples:
        mask = (ns >= X / 2) & (ns <= 2 * X)
        n = ns[mask]
        r = n / X
        weight = np.where(r <= 1, 2 * r - 1 / (2 * r), 2 / r - r / 2)
        P = math.fsum((lps[mask] * weight / np.sqrt(n)).tolist())
        E = P - float(A) * math.sqrt(X)
        D = arch_correction(X)
        entry = {"X": X, "P": P, "P_minus_A_sqrtX": E,
                 "D": float(D), "K_logX": -E - float(D)}
        if X in (3, 100, 10000):
            xx = mp.mpf(X)
            Pmp = mp.fsum(mp.log(p) / mp.sqrt(n) * g(mp.log(mp.mpf(n) / xx))
                         for n, p in data if X / 2 <= n <= 2 * X)
            entry["mp50_error_in_P"] = float(abs(Pmp - P))
            entry["mp50_error_in_residual"] = float(abs((Pmp - A * mp.sqrt(xx)) - E))
        records.append(entry)
    result = {"status": "Numerical diagnostics only; not an RH proof or interval certificate",
              "A": mp.nstr(A, 40), "Q_f_from_arithmetic": mp.nstr(q0, 40),
              "norm_f_squared": 1.5,
              "Mellin_transform_absolute_errors": transform_checks,
              "samples": records}
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
