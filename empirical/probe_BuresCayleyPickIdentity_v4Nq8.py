"""Probe the Bures-Cayley Pick identity.

Random suffix: v4Nq8

The script verifies:
1. Symbolic Cayley-Menger factorization
       Delta_CM(F) = Z * A_CM
   for the exact Z/6 packet F = Z E + L O.
2. The completed numerical identity
       Delta_CM(F_c(z)) = Xi(z) * A_B(z).
3. The log-derivative identity
       -d log Delta_CM(F_c) + d log A_B = -Xi'/Xi.
4. The Cayley-Menger Hessian has a positive shape metric after scale removal.
5. The cofactor is nonzero at the first tested zeta zeros.
"""

from __future__ import annotations

import random

import mpmath as mp
import numpy as np
import sympy as sp


MP_DPS = 70
mp.mp.dps = MP_DPS

GAMMAS = [
    mp.mpf("14.1347251417346937904572519835625"),
    mp.mpf("21.0220396387715549926284795938969"),
    mp.mpf("25.0108575801456887632137909925628"),
    mp.mpf("30.4248761258595132103118975305840"),
    mp.mpf("32.9350615877391896906623689640747"),
]


def cm_poly(values):
    y = values
    return -2 * (
        y[0] ** 2 * y[3]
        - y[0] * y[1] * y[3]
        - y[0] * y[1] * y[4]
        + y[0] * y[1] * y[5]
        - y[0] * y[2] * y[3]
        + y[0] * y[2] * y[4]
        - y[0] * y[2] * y[5]
        + y[0] * y[3] ** 2
        - y[0] * y[3] * y[4]
        - y[0] * y[3] * y[5]
        + y[1] ** 2 * y[4]
        + y[1] * y[2] * y[3]
        - y[1] * y[2] * y[4]
        - y[1] * y[2] * y[5]
        - y[1] * y[3] * y[4]
        + y[1] * y[4] ** 2
        - y[1] * y[4] * y[5]
        + y[2] ** 2 * y[5]
        - y[2] * y[3] * y[5]
        - y[2] * y[4] * y[5]
        + y[2] * y[5] ** 2
        + y[3] * y[4] * y[5]
    )


def symbolic_factorization():
    Z, L, a, b = sp.symbols("Z L a b")
    E = [
        a * b,
        sp.Rational(1, 2) * (1 - a) * (1 - b),
        sp.Rational(1, 2) * a * (1 - b),
        b * (1 - a),
        sp.Rational(1, 2) * a * (1 - b),
        sp.Rational(1, 2) * (1 - a) * (1 - b),
    ]
    O = [
        0,
        sp.Rational(1, 2) * (1 + a),
        sp.Rational(1, 2) * a,
        0,
        -sp.Rational(1, 2) * a,
        -sp.Rational(1, 2) * (1 + a),
    ]
    F = [sp.expand(Z * E[i] + L * O[i]) for i in range(6)]
    delta = sp.factor(sp.expand(cm_poly(F)))
    C0 = -4 * a**2 * b - 4 * a * b + 4 * a + 3 * b
    C2 = b * (
        4 * a**2 * b**2
        - 8 * a**2 * b
        + 4 * a**2
        - 12 * a * b**2
        + 12 * a * b
        - 4 * a
        + 9 * b**2
        - 6 * b
        + 1
    )
    expected = sp.factor(-Z * a * (L**2 * C0 + Z**2 * C2) / 2)
    return sp.simplify(delta - expected) == 0, sp.factor(delta), sp.factor(expected)


def xi_s(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z):
    return xi_s(mp.mpf("0.5") + 1j * z)


def Xi_prime(z):
    s = mp.mpf("0.5") + 1j * z
    return 1j * mp.diff(xi_s, s)


def L3(s):
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def L3_completed(z):
    s = mp.mpf("0.5") + 1j * z
    return mp.power(3 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * L3(s)


def local_ab(z):
    s = mp.mpf("0.5") + 1j * z
    return mp.power(2, -s), mp.power(3, -s)


def C0_num(a, b):
    return -4 * a**2 * b - 4 * a * b + 4 * a + 3 * b


def C2_num(a, b):
    return b * (
        4 * a**2 * b**2
        - 8 * a**2 * b
        + 4 * a**2
        - 12 * a * b**2
        + 12 * a * b
        - 4 * a
        + 9 * b**2
        - 6 * b
        + 1
    )


def completed_packet(z):
    a, b = local_ab(z)
    X = Xi(z)
    L = L3_completed(z)
    E = [
        a * b,
        mp.mpf("0.5") * (1 - a) * (1 - b),
        mp.mpf("0.5") * a * (1 - b),
        b * (1 - a),
        mp.mpf("0.5") * a * (1 - b),
        mp.mpf("0.5") * (1 - a) * (1 - b),
    ]
    O = [
        0,
        mp.mpf("0.5") * (1 + a),
        mp.mpf("0.5") * a,
        0,
        -mp.mpf("0.5") * a,
        -mp.mpf("0.5") * (1 + a),
    ]
    return [X * E[i] + L * O[i] for i in range(6)]


def cm_completed(z):
    return cm_poly(completed_packet(z))


def cofactor_completed(z):
    a, b = local_ab(z)
    X = Xi(z)
    L = L3_completed(z)
    return -a * (L**2 * C0_num(a, b) + X**2 * C2_num(a, b)) / 2


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def dlog(func, z):
    return mp.diff(func, z) / func(z)


def m_cm_transfer(z):
    return -dlog(cm_completed, z) + dlog(cofactor_completed, z)


def hessian_at_regular():
    y = sp.symbols("y0:6")
    delta = cm_poly(y)
    H = sp.Matrix([[sp.diff(delta, yi, yj) for yj in y] for yi in y])
    reg = {yi: sp.Rational(8, 3) for yi in y}
    Hreg = sp.Matrix(H.subs(reg))
    return np.array(Hreg.tolist(), dtype=float)


def project_scale(v):
    return v - np.mean(v)


def main():
    ok, delta, expected = symbolic_factorization()
    print("symbolic_factorization_ok:", ok)
    print("factorized_delta:")
    print(delta)

    samples = [
        mp.mpc("0.7", "0.2"),
        mp.mpc("3.0", "0.4"),
        mp.mpc("10.0", "0.7"),
        mp.mpc("14.0", "0.3"),
        mp.mpc("-4.0", "0.5"),
    ]
    print("\ncompleted factor and log-derivative checks:")
    for z in samples:
        lhs = cm_completed(z)
        rhs = Xi(z) * cofactor_completed(z)
        rel = abs(lhs - rhs) / max(mp.mpf("1e-80"), abs(rhs))
        merr = abs(m_cm_transfer(z) - m_bures(z))
        print(
            "z=", z,
            "factor_rel_err=", mp.nstr(rel, 4),
            "m_err=", mp.nstr(merr, 4),
        )

    print("\ncofactor at first tested spectral zeros:")
    for gamma in GAMMAS:
        z = gamma
        A = cofactor_completed(z)
        c0 = C0_num(*local_ab(z))
        print(
            "gamma=", mp.nstr(gamma, 14),
            "|A_B|=", mp.nstr(abs(A), 8),
            "|C0|=", mp.nstr(abs(c0), 8),
            "|L3c|=", mp.nstr(abs(L3_completed(z)), 8),
        )

    print("\nnear gamma_1 divisor scaling:")
    gamma = GAMMAS[0]
    for y in [mp.mpf("0.1"), mp.mpf("0.02"), mp.mpf("0.005"), mp.mpf("0.001")]:
        z = gamma + 1j * y
        print(
            "y=", y,
            "|CM|/y=", mp.nstr(abs(cm_completed(z)) / y, 8),
            "Pdiag=", mp.nstr(mp.im(m_bures(z)) / y, 8),
        )

    H = hessian_at_regular()
    evals = np.linalg.eigvalsh(H)
    print("\nCM Hessian eigenvalues at regular edge vector:")
    print(np.array2string(evals, precision=8))
    print("Negative Hessian is positive on random scale-fixed directions:")
    rng = random.Random(260515910)
    mins = []
    for _ in range(20):
        v = np.array([rng.uniform(-1, 1) for _ in range(6)], dtype=float)
        u = project_scale(v)
        mins.append(float(-u @ H @ u))
    print("min_random_shape_metric:", min(mins))


if __name__ == "__main__":
    main()

