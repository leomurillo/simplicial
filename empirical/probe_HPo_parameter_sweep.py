"""Parameter sweep for KU-3 Hilbert-Polya candidate families.

The affine rescale gamma ~= a lambda + b is reported separately from structural
coefficients. A convincing candidate should not need this rescale, but the sweep
is useful as a failure diagnostic: even tuned finite structural combinations do
not reproduce the zero ordinates beyond low-dimensional interpolation.
"""

from __future__ import annotations

import numpy as np

from hpo_common import (
    K_PERM,
    RIEMANN_GAMMAS,
    apply_k,
    best_affine_fit,
    cyclic_momentum,
    g_balanced,
    hermitian_part,
    k_antisymmetric_diag,
    positive_branch,
    sorted_eigenvalues,
    sym,
)


def normalize(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    if n == 0:
        return v
    return v / n


def fit_score(matrix: np.ndarray, branch: str) -> tuple[float, dict[str, object], np.ndarray]:
    vals = sorted_eigenvalues(matrix).real
    if branch == "positive":
        seq = positive_branch(vals)
    else:
        seq = np.sort(vals)
    fit = best_affine_fit(seq, RIEMANN_GAMMAS)
    return float(fit["rms"]), fit, seq


def random_sweep(name: str, bases: list[np.ndarray], samples: int = 5000) -> None:
    rng = np.random.default_rng(20260522)
    best: dict[str, tuple[float, np.ndarray, dict[str, object], np.ndarray]] = {}
    for branch in ("full", "positive"):
        best[branch] = (float("inf"), np.zeros(len(bases)), {}, np.array([]))

    candidates = [np.eye(len(bases))[i] for i in range(len(bases))]
    candidates += [-np.eye(len(bases))[i] for i in range(len(bases))]
    candidates += [normalize(rng.normal(size=len(bases))) for _ in range(samples)]

    for coeff in candidates:
        h = sum(c * b for c, b in zip(coeff, bases))
        h = hermitian_part(h)
        for branch in ("full", "positive"):
            rms, fit, seq = fit_score(h, branch)
            if rms < best[branch][0]:
                best[branch] = (rms, coeff.copy(), fit, seq.copy())

    print("=" * 100)
    print(name)
    print("=" * 100)
    for branch in ("full", "positive"):
        rms, coeff, fit, seq = best[branch]
        print(f"branch={branch}")
        print("  coeffs: " + ", ".join(f"{x:+.6f}" for x in coeff))
        print(f"  eigenvalues used ({len(seq)}): " + ", ".join(f"{x:+.8f}" for x in seq[: int(fit['count'])]))
        print(
            f"  affine fit: gamma ~= {fit['scale']:.10g}*lambda + {fit['shift']:.10g}; "
            f"m={fit['count']}, rms={fit['rms']:.6g}, max={fit['max_abs']:.6g}"
        )


def family_b_bases() -> list[np.ndarray]:
    p = cyclic_momentum()
    g = g_balanced()
    return [
        hermitian_part(1j * (g @ p - p @ g)),
        hermitian_part(0.5 * (g + apply_k(g))),
        hermitian_part(1j * (k_antisymmetric_diag() @ p - p @ k_antisymmetric_diag())),
    ]


def k_shift_observable(g: np.ndarray) -> np.ndarray:
    return hermitian_part(sym(K_PERM, g))


def family_c_bases() -> list[np.ndarray]:
    p = cyclic_momentum()
    g = g_balanced()
    a_g = k_shift_observable(g)
    a_odd = k_shift_observable(k_antisymmetric_diag())
    rate = hermitian_part(0.5 * (apply_k(g) @ g + g @ apply_k(g)))
    return [hermitian_part(sym(p, a_g)), hermitian_part(sym(p, a_odd)), rate]


def family_d_bases() -> list[np.ndarray]:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    p = cyclic_momentum()
    g = g_balanced()
    h_b = hermitian_part(1j * (g @ p - p @ g))
    a_k = k_shift_observable(k_antisymmetric_diag()) + k_shift_observable(g)
    return [
        hermitian_part(np.kron(h_b, sz)),
        hermitian_part(np.kron(a_k, sx)),
        hermitian_part(np.kron(p, sy)),
    ]


if __name__ == "__main__":
    random_sweep("Family B structural coefficient sweep", family_b_bases())
    random_sweep("Family C structural coefficient sweep", family_c_bases())
    random_sweep("Family D structural coefficient sweep", family_d_bases())
