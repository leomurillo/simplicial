"""Numerical probe for the folded xi determinant/PF target.

This is evidence only. It computes early coefficients of

    B(x) = Xi(i*sqrt(x)) / Xi(0)

via even derivatives of Xi(z)=xi(1/2+i z), then checks small Toeplitz
minors and the folded cumulants.
"""

from __future__ import annotations

import itertools
import math

import mpmath as mp


mp.mp.dps = 80


def xi_s(s: mp.mpc) -> mp.mpc:
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi(z: mp.mpc) -> mp.mpc:
    return xi_s(mp.mpf("0.5") + 1j * z)


def B_folded(x: mp.mpc) -> mp.mpc:
    """Folded xi B(x)=Xi(i sqrt(x))/Xi(0).

    Xi is even, so the value is independent of the square-root branch.
    """
    xi0 = Xi(0)
    return Xi(1j * mp.sqrt(x)) / xi0


def folded_coefficients(order: int, radius: mp.mpf = mp.mpf("1.0"), samples: int = 256) -> list[mp.mpf]:
    """Return b[0..order] for B(x)=Xi(i sqrt(x))/Xi(0).

    Uses Cauchy's coefficient formula on a small circle and a DFT.
    This is much faster and numerically more stable than high-order
    automatic differentiation of the completed xi function.
    """
    coeffs = [mp.mpc(0) for _ in range(order + 1)]
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        point = radius * mp.e ** (1j * theta)
        value = B_folded(point)
        for n in range(order + 1):
            coeffs[n] += value * mp.e ** (-1j * n * theta) / (radius ** n)
    return [mp.re(c / samples) for c in coeffs]


def toeplitz_entry(b: list[mp.mpf], i: int, j: int) -> mp.mpf:
    k = j - i
    if k < 0 or k >= len(b):
        return mp.mpf("0")
    return b[k]


def det_matrix(mat: list[list[mp.mpf]]) -> mp.mpf:
    n = len(mat)
    total = mp.mpf("0")
    for perm in itertools.permutations(range(n)):
        inv = 0
        prod = mp.mpf("1")
        for i, j in enumerate(perm):
            prod *= mat[i][j]
            for k in range(i):
                if perm[k] > j:
                    inv += 1
        total += (-prod if inv % 2 else prod)
    return total


def min_toeplitz_minor(b: list[mp.mpf], matrix_size: int, minor_size: int):
    rows = range(matrix_size)
    cols = range(matrix_size)
    min_det = None
    min_pair = None
    negative_count = 0
    tolerance = mp.mpf("1e-50")
    checked = 0
    for row_idx in itertools.combinations(rows, minor_size):
        for col_idx in itertools.combinations(cols, minor_size):
            mat = [[toeplitz_entry(b, i, j) for j in col_idx] for i in row_idx]
            val = det_matrix(mat)
            checked += 1
            if val < -tolerance:
                negative_count += 1
            if min_det is None or val < min_det:
                min_det = val
                min_pair = (row_idx, col_idx)
    return checked, negative_count, min_det, min_pair


def formal_log_cumulants(b: list[mp.mpf], order: int) -> list[mp.mpf]:
    """Compute ell_m from log(B)=sum (-1)^(m+1) ell_m x^m/m."""
    # Formal series arithmetic up to order.
    f = [mp.mpf("0")] * (order + 1)
    for i in range(min(len(b), order + 1)):
        f[i] = b[i]
    u = f[:]
    u[0] -= 1
    log_coeff = [mp.mpf("0")] * (order + 1)
    power = [mp.mpf("0")] * (order + 1)
    power[0] = 1
    for k in range(1, order + 1):
        # power *= u
        new_power = [mp.mpf("0")] * (order + 1)
        for i in range(order + 1):
            if power[i] == 0:
                continue
            for j in range(1, order + 1 - i):
                if u[j] != 0:
                    new_power[i + j] += power[i] * u[j]
        power = new_power
        sign = 1 if k % 2 == 1 else -1
        for i in range(1, order + 1):
            log_coeff[i] += sign * power[i] / k
    ells = []
    for m in range(1, order + 1):
        ell = ((-1) ** (m + 1)) * m * log_coeff[m]
        ells.append(ell)
    return ells


def main() -> None:
    coeff_order = 12
    b = folded_coefficients(coeff_order)
    print("Folded coefficients b_n for B(x)=Xi(i sqrt(x))/Xi(0):")
    for i, val in enumerate(b):
        print(f"b[{i}] = {mp.nstr(val, 30)}")

    print("\nSmall Toeplitz total-positivity probe:")
    for minor_size in range(1, 5):
        checked, negative_count, min_det, min_pair = min_toeplitz_minor(
            b, matrix_size=8, minor_size=minor_size
        )
        print(
            f"size {minor_size}: checked={checked}, "
            f"negative_count={negative_count}, "
            f"min_det={mp.nstr(min_det, 20)}, at rows/cols={min_pair}"
        )

    ells = formal_log_cumulants(b, 8)
    print("\nFolded divisor cumulants ell_m from formal log:")
    for i, val in enumerate(ells, start=1):
        print(f"ell[{i}] = {mp.nstr(val, 30)}")

    print("\nHankel probe for r_k=ell_(k+1):")
    r = ells
    for size in range(1, 4):
        mat = [[r[i + j] for j in range(size)] for i in range(size)]
        val = det_matrix(mat)
        print(f"Hankel size {size}: det={mp.nstr(val, 20)}")


if __name__ == "__main__":
    main()
