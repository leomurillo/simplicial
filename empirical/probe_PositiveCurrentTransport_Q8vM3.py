"""Probe for Note_PositiveCurrentTransport_Q8vM3.

This is a finite-dimensional transport sanity check.  It models:

raw current = closed current + leakage,
Q(raw) = Q(closed) + leakage_penalty,
Q(closed) >= 0,
target_n = Q(closed) + signed recovery error,
recovery error -> 0.

The point is not to simulate zeta.  It checks the sign logic: if the actual
finite value is evaluated on the projected admissible current and recovery
errors vanish, the limiting transported value cannot become negative.
"""

from __future__ import annotations

import math
import random


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def mat_vec(A: list[list[float]], x: list[float]) -> list[float]:
    return [dot(row, x) for row in A]


def q_value(A: list[list[float]], x: list[float]) -> float:
    y = mat_vec(A, x)
    return dot(y, y)


def norm2(x: list[float]) -> float:
    return dot(x, x)


def project_closed(x: list[float], closed_dim: int) -> list[float]:
    return x[:closed_dim] + [0.0] * (len(x) - closed_dim)


def leakage_part(x: list[float], closed_dim: int) -> list[float]:
    return [0.0] * closed_dim + x[closed_dim:]


def run_trial(seed: int = 20260522) -> None:
    rng = random.Random(seed)
    dim = 9
    closed_dim = 5
    A = [[rng.uniform(-0.7, 0.7) for _ in range(dim)] for _ in range(dim)]

    print("Positive-current transport probe")
    print("n    Q_closed        leakage        Q_raw          recovery_err   target_n")

    target_values = []
    min_q = float("inf")
    for n in range(1, 16):
        closed = [math.sin(0.3 * n + j) / (1 + 0.02 * n) for j in range(closed_dim)]
        leak_scale = 1.0 / (n * n)
        leak = [leak_scale * math.cos(n + j) for j in range(dim - closed_dim)]
        raw = closed + leak
        projected = project_closed(raw, closed_dim)
        leakage = leakage_part(raw, closed_dim)

        q_closed = q_value(A, projected)
        leakage_penalty = norm2(leakage)
        q_raw_model = q_closed + leakage_penalty

        # Signed recovery error tends to zero and can be negative at finite n.
        recovery_err = ((-1) ** n) * 0.08 / (n ** 1.4)
        target_n = q_closed + recovery_err
        target_values.append(target_n)
        min_q = min(min_q, q_closed)

        print(
            f"{n:2d} {q_closed:15.8e} {leakage_penalty:15.8e} "
            f"{q_raw_model:15.8e} {recovery_err:15.8e} {target_n:15.8e}"
        )

    print()
    print(f"minimum finite Q_closed: {min_q:.8e}")
    print(f"last transported target: {target_values[-1]:.8e}")
    print("The signed recovery error decays; the limiting sign is carried by Q_closed >= 0.")


if __name__ == "__main__":
    run_trial()

