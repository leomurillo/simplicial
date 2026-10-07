"""Finite spoofing probe for CM measure selection.

Random suffix: T9fB6

Fits positive even atomic measures to finite samples of the Bures Pick kernel.
The point is not to identify the true measure, but to demonstrate that finite
Pick constraints can be closely reproduced by wrong positive measures.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np
from scipy.optimize import lsq_linear


mp.mp.dps = 60

GAMMA1 = mp.mpf("14.1347251417346937904572519835625")
GAMMA2 = mp.mpf("21.0220396387715549926284795938969")
GAMMAS10 = np.array(
    [
        14.134725141734693,
        21.022039638771555,
        25.01085758014569,
        30.424876125859513,
        32.93506158773919,
        37.58617815882567,
        40.91871901214749,
        43.327073280915,
        48.00515088116716,
        49.7738324776723,
    ],
    dtype=float,
)


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
    return 1j * mp.diff(xi_s, mp.mpf("0.5") + 1j * z)


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def pick_bures(z, w):
    return (m_bures(z) - mp.conj(m_bures(w))) / (z - mp.conj(w))


def build_linear_system(points, atoms, target):
    rows = []
    rhs = []
    cpoints = [complex(z) for z in points]
    for i, z in enumerate(cpoints):
        for j, w in enumerate(cpoints):
            if j < i:
                continue
            vals = 1 / ((atoms - z) * (atoms - np.conj(w)))
            rows.append(vals.real)
            rhs.append(target[i, j].real)
            if i != j or abs(target[i, j].imag) > 1e-14:
                rows.append(vals.imag)
                rhs.append(target[i, j].imag)
    return np.vstack(rows), np.array(rhs)


def fit_measure(name, atoms, points, target):
    A, y = build_linear_system(points, atoms, target)
    result = lsq_linear(
        A,
        y,
        bounds=(0, np.inf),
        tol=1e-12,
        lsmr_tol="auto",
        max_iter=20000,
    )
    pred = A @ result.x
    rel = np.linalg.norm(pred - y) / np.linalg.norm(y)
    nonzero = int(np.sum(result.x > 1e-7))
    return {
        "name": name,
        "rel": rel,
        "nonzero": nonzero,
        "max_weight": float(result.x.max()),
        "cost": float(result.cost),
    }


def symmetric_atoms(kind):
    if kind == "true10":
        pos = GAMMAS10
    elif kind == "uniform_grid":
        pos = np.linspace(1.0, 80.0, 160)
    elif kind == "quadratic_grid":
        k = np.arange(1, 181, dtype=float)
        pos = 0.25 + 85.0 * (k / (len(k) + 1)) ** 2
    elif kind == "shifted_grid":
        pos = np.linspace(0.6, 90.0, 180) + 0.137
    else:
        raise ValueError(kind)
    return np.concatenate([-pos[::-1], pos])


def main() -> None:
    points = [
        mp.mpc("0.7", "0.4"),
        mp.mpc("5.0", "0.5"),
        GAMMA1 + mp.mpc(0, "0.5"),
        GAMMA2 + mp.mpc(0, "0.5"),
    ]

    target = np.empty((len(points), len(points)), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            target[i, j] = complex(pick_bures(z, w))
    target = (target + target.conj().T) / 2

    print("Target Pick matrix eigenvalues:")
    print(np.array2string(np.linalg.eigvalsh(target), precision=8))

    print("\nPositive even atomic measure fits:")
    for kind in ["true10", "uniform_grid", "quadratic_grid", "shifted_grid"]:
        atoms = symmetric_atoms(kind)
        stats = fit_measure(kind, atoms, points, target)
        print(
            f"{stats['name']:>14}",
            "rel=", f"{stats['rel']:.6e}",
            "nonzero=", stats["nonzero"],
            "max_weight=", f"{stats['max_weight']:.6e}",
        )

    print("\nConclusion:")
    print("  Different positive even atom dictionaries fit the same finite")
    print("  Pick data to small residual. Finite tests restrict but do not")
    print("  select the Hilbert-Polya divisor measure.")
    print("  The selection law must be a dense Cauchy/Pick/Weil identity.")


if __name__ == "__main__":
    main()

