#!/usr/bin/env python3
"""Computational Helmert/Fourier apex transfers.

This is the executable version of the T9 transfer matrix:

    U_kc = <e_k, chi_c / sqrt(N)>

with the radical-cyclotomic split

    U_kc = R_k * C_kc,
    R_k = 1 / sqrt(N k (k + 1)).

The module keeps the convention from T9:

- Helmert rungs k are 1-based, k=1,...,N-1.
- non-trivial Fourier characters c are 1-based, c=1,...,N-1.
- inner products are Hermitian: <u,v> = sum conjugate(u_i) v_i.

Coordinate convention:

    y = sum_k a_k e_k = sum_c b_c normalized_chi_c
    a = U b
    b = U* a
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


Number = complex | float


@dataclass(frozen=True)
class TransferEntry:
    """One radical-cyclotomic transfer entry."""

    radical: float
    cyclotomic: complex

    @property
    def value(self) -> complex:
        return self.radical * self.cyclotomic


def omega(N: int) -> complex:
    if N < 2:
        raise ValueError("N must be at least 2")
    return cmath.exp(2j * math.pi / N)


def conductor(N: int, c: int) -> int:
    if not 0 <= c < N:
        raise ValueError("c must be in 0,...,N-1")
    return 1 if c == 0 else N // math.gcd(N, c)


def conductor_packets(N: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = defaultdict(list)
    for c in range(1, N):
        packets[conductor(N, c)].append(c)
    return dict(sorted(packets.items()))


def helmert_vector(N: int, k: int, *, unit: bool = True) -> list[float]:
    if not 1 <= k <= N - 1:
        raise ValueError("k must be in 1,...,N-1")
    vector = [0.0] * N
    for i in range(k):
        vector[i] = 1.0
    vector[k] = -float(k)
    if unit:
        scale = math.sqrt(k * (k + 1))
        vector = [value / scale for value in vector]
    return vector


def character_vector(N: int, c: int, *, normalized: bool = True) -> list[complex]:
    if not 0 <= c <= N - 1:
        raise ValueError("c must be in 0,...,N-1")
    root = omega(N)
    scale = math.sqrt(N) if normalized else 1.0
    return [root ** (c * s) / scale for s in range(N)]


def inner(left: Iterable[Number], right: Iterable[Number]) -> complex:
    return sum(complex(a).conjugate() * complex(b) for a, b in zip(left, right))


def transfer_entry(N: int, k: int, c: int, *, form: str = "polynomial") -> complex:
    """Return U_kc by one of T9's equivalent closed forms."""

    if not 1 <= k <= N - 1:
        raise ValueError("k must be in 1,...,N-1")
    if not 1 <= c <= N - 1:
        raise ValueError("c must be in 1,...,N-1")
    scale = 1.0 / math.sqrt(N * k * (k + 1))

    if form == "basis":
        return inner(helmert_vector(N, k), character_vector(N, c))  # type: ignore[arg-type]

    root = omega(N)
    z = root**c
    if form == "geometric":
        bracket = sum(z**j for j in range(k)) - k * z**k
    elif form == "polynomial":
        bracket = (1 - (k + 1) * z**k + k * z ** (k + 1)) / (1 - z)
    elif form == "trigonometric":
        theta = math.pi * c / N
        bracket = cmath.exp(1j * (k - 1) * theta) * math.sin(k * theta) / math.sin(theta)
        bracket -= k * cmath.exp(2j * k * theta)
    elif form == "exponential":
        theta = math.pi * c / N
        bracket = cmath.exp(1j * k * theta) * (
            cmath.exp(-1j * theta) * math.sin(k * theta) / math.sin(theta)
            - k * cmath.exp(1j * k * theta)
        )
    else:
        raise ValueError(f"unknown form {form!r}")
    return scale * bracket


def factorized_entry(N: int, k: int, c: int) -> TransferEntry:
    scale = 1.0 / math.sqrt(N * k * (k + 1))
    root = omega(N)
    z = root**c
    cyclotomic = sum(z**j for j in range(k)) - k * z**k
    return TransferEntry(radical=scale, cyclotomic=cyclotomic)


def transfer_matrix(N: int, *, form: str = "polynomial") -> list[list[complex]]:
    return [[transfer_entry(N, k, c, form=form) for c in range(1, N)] for k in range(1, N)]


def mat_vec(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def adjoint_mat_vec(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    cols = len(matrix[0]) if matrix else 0
    return [sum(matrix[i][j].conjugate() * vector[i] for i in range(len(matrix))) for j in range(cols)]


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


def helmert_coordinates(values: list[float]) -> list[complex]:
    N = len(values)
    y = centered(values)
    return [inner(helmert_vector(N, k), y) for k in range(1, N)]  # type: ignore[arg-type]


def fourier_coordinates(values: list[float]) -> list[complex]:
    N = len(values)
    y = centered(values)
    return [inner(character_vector(N, c), y) for c in range(1, N)]  # type: ignore[arg-type]


def helmert_to_fourier(helmert_coords: list[complex], N: int) -> list[complex]:
    U = transfer_matrix(N)
    return adjoint_mat_vec(U, helmert_coords)


def fourier_to_helmert(fourier_coords: list[complex], N: int) -> list[complex]:
    U = transfer_matrix(N)
    return mat_vec(U, fourier_coords)


def conductor_energy(fourier_coords: list[complex], N: int) -> dict[int, float]:
    energy: dict[int, float] = defaultdict(float)
    for c, value in enumerate(fourier_coords, start=1):
        energy[conductor(N, c)] += abs(value) ** 2
    return dict(sorted(energy.items()))


def apex_generator(values: list[float], beta: float, c: int, *, epsilon: float = 1e-12) -> complex:
    """Compute M_x(beta,c) = mean exp(beta*y_s) conjugate(chi_c(s))."""

    N = len(values)
    if not 0 <= c < N:
        raise ValueError("c must be in 0,...,N-1")
    if any(value + epsilon <= 0 for value in values):
        raise ValueError("values must be positive after epsilon shift")
    logs = [math.log(value + epsilon) for value in values]
    y = centered(logs)
    root = omega(N)
    return sum(math.exp(beta * y[s]) * (root ** (-c * s)) for s in range(N)) / N


def apex_surface(values: list[float], beta: float, *, epsilon: float = 1e-12) -> list[complex]:
    return [apex_generator(values, beta, c, epsilon=epsilon) for c in range(len(values))]


def max_form_error(N: int) -> float:
    forms = ("basis", "geometric", "polynomial", "trigonometric", "exponential")
    worst = 0.0
    for k in range(1, N):
        for c in range(1, N):
            reference = transfer_entry(N, k, c, form="basis")
            for form in forms[1:]:
                worst = max(worst, abs(reference - transfer_entry(N, k, c, form=form)))
    return worst


def unitarity_error(N: int) -> float:
    U = transfer_matrix(N)
    worst = 0.0
    for i in range(N - 1):
        for j in range(N - 1):
            row_inner = sum(U[i][c] * U[j][c].conjugate() for c in range(N - 1))
            col_inner = sum(U[k][i].conjugate() * U[k][j] for k in range(N - 1))
            target = 1.0 if i == j else 0.0
            worst = max(worst, abs(row_inner - target), abs(col_inner - target))
    return worst


def demo(N: int) -> dict[str, object]:
    values = [2.0 + math.sin(2 * math.pi * s / N) + 0.35 * math.cos(6 * math.pi * s / N) for s in range(N)]
    h_coords = helmert_coordinates(values)
    f_coords_direct = fourier_coordinates(values)
    f_coords_via_u = helmert_to_fourier(h_coords, N)
    h_coords_roundtrip = fourier_to_helmert(f_coords_via_u, N)
    return {
        "N": N,
        "max_form_error": max_form_error(N),
        "unitarity_error": unitarity_error(N),
        "helmert_to_fourier_error": max(abs(a - b) for a, b in zip(f_coords_direct, f_coords_via_u)),
        "roundtrip_helmert_error": max(abs(a - b) for a, b in zip(h_coords, h_coords_roundtrip)),
        "conductor_packets": conductor_packets(N),
        "conductor_energy": conductor_energy(f_coords_via_u, N),
        "apex_beta_1_abs_by_c": [abs(value) for value in apex_surface(values, 1.0)],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", type=int, default=8, help="run a numerical demo at this N")
    args = parser.parse_args()
    print(json.dumps(demo(args.demo), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
