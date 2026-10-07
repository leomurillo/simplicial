"""Shared utilities for KU-3 Hilbert-Polya probes on the Z/6 Bures lift."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import mpmath as mp


Q = 6

RIEMANN_GAMMAS = np.array(
    [
        14.134725141734693790457251983562,
        21.022039638771554992628479593896,
        25.010857580145688763213790992562,
        30.424876125859513210311897530584,
        32.935061587739189690662368964075,
        37.586178158825671257217763480705,
        40.918719012147495187398126914633,
        43.327073280914999519496122165406,
        48.005150881167159727942472749427,
        49.773832477672302181916784678563,
        52.970321477714460644147296608880,
        56.446247697063394804367759476706,
        59.347044002602353079653648674992,
        60.831778524609809844259901824524,
        65.112544048081606660875054253183,
        67.079810529494173714478828896522,
        69.546401711173979252926857526554,
        72.067157674481907582522107969826,
        75.704690699083933168326916762030,
        77.144840068874805372682664856304,
    ],
    dtype=float,
)


def k_permutation(n: int = Q) -> np.ndarray:
    """Permutation matrix for r -> -r mod n."""
    mat = np.zeros((n, n), dtype=complex)
    for r in range(n):
        mat[(-r) % n, r] = 1.0
    return mat


K_PERM = k_permutation()


def apply_k(matrix: np.ndarray) -> np.ndarray:
    return K_PERM @ np.conjugate(matrix) @ K_PERM.T


def unitary_dft(n: int = Q) -> np.ndarray:
    j, k = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    return np.exp(2j * np.pi * j * k / n) / np.sqrt(n)


def cyclic_momentum(n: int = Q) -> np.ndarray:
    """Hermitian finite cyclic momentum with centered Fourier labels."""
    labels = np.fft.fftfreq(n, d=1.0 / n)
    dft = unitary_dft(n)
    return dft @ np.diag(labels) @ dft.conj().T


def centered_position(n: int = Q) -> np.ndarray:
    x = np.arange(n, dtype=float) - (n - 1) / 2.0
    x = x / np.sqrt(np.mean(x * x))
    return np.diag(x.astype(complex))


def g_balanced() -> np.ndarray:
    """The canonical G_balanced used in nueve/probe_A2."""
    g = np.zeros((Q, Q), dtype=complex)
    g[0, 0] = 1.0
    g[1, 1] = -1.0
    g[2, 2] = 0.5
    g[3, 3] = -0.5
    g[0, 1] = g[1, 0] = 0.3
    g[2, 3] = g[3, 2] = 0.2
    g[0, 2] = g[2, 0] = 0.1
    return g


def k_antisymmetric_diag() -> np.ndarray:
    """Diagonal K-odd test observable from probe_D_hurwitz_FE_chain."""
    return np.diag(np.array([0.0, 1.0, 1.0, 0.0, -1.0, -1.0], dtype=complex))


def hermitian_part(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (matrix + matrix.conj().T)


def sym(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return 0.5 * (a @ b + b @ a)


def matrix_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix))


def hermiticity_defect(matrix: np.ndarray) -> float:
    return matrix_norm(matrix - matrix.conj().T)


def k_hermitian_defect(matrix: np.ndarray) -> float:
    return matrix_norm(apply_k(matrix) - matrix.conj().T)


def sorted_eigenvalues(matrix: np.ndarray) -> np.ndarray:
    if hermiticity_defect(matrix) < 1.0e-8:
        return np.linalg.eigvalsh(hermitian_part(matrix))
    vals = np.linalg.eigvals(matrix)
    vals = vals[np.argsort(vals.real)]
    return vals


def best_affine_fit(values: np.ndarray, target: np.ndarray) -> dict[str, object]:
    values = np.asarray(values, dtype=float)
    target = np.asarray(target, dtype=float)
    m = min(len(values), len(target))
    if m == 0:
        return {"count": 0, "scale": np.nan, "shift": np.nan, "rms": np.nan, "max_abs": np.nan}
    x = values[:m]
    y = target[:m]
    a_matrix = np.column_stack([x, np.ones(m)])
    scale, shift = np.linalg.lstsq(a_matrix, y, rcond=None)[0]
    fitted = scale * x + shift
    residual = fitted - y
    return {
        "count": m,
        "scale": float(scale),
        "shift": float(shift),
        "rms": float(np.sqrt(np.mean(residual * residual))),
        "max_abs": float(np.max(np.abs(residual))),
        "fitted": fitted,
        "residual": residual,
    }


def positive_branch(values: Iterable[float], tolerance: float = 1.0e-9) -> np.ndarray:
    values = np.sort(np.asarray(list(values), dtype=float))
    pos = values[values > tolerance]
    return pos


def rvm_count(t: float) -> float:
    if t <= 2 * np.pi:
        return 0.0
    return (t / (2 * np.pi)) * np.log(t / (2 * np.pi)) - t / (2 * np.pi)


def print_matrix(name: str, matrix: np.ndarray, precision: int = 4) -> None:
    print(f"\n{name} matrix in |0>,...,|{matrix.shape[0] - 1}> basis:")
    with np.printoptions(precision=precision, suppress=True):
        print(matrix)


def print_spectral_report(name: str, matrix: np.ndarray, target: np.ndarray = RIEMANN_GAMMAS) -> None:
    print("=" * 100)
    print(name)
    print("=" * 100)
    print(f"dimension: {matrix.shape[0]}")
    print(f"Hermiticity defect ||H-H^*||: {hermiticity_defect(matrix):.6e}")
    if matrix.shape == (Q, Q):
        print(f"K-Hermitian defect ||KHK^-1-H^*||: {k_hermitian_defect(matrix):.6e}")
    vals = sorted_eigenvalues(matrix)
    if np.iscomplexobj(vals):
        print("raw eigenvalues:")
        for z in vals:
            print(f"  {z.real:+.10f} {z.imag:+.10f}j")
        real_vals = vals.real
    else:
        real_vals = vals
        print("raw eigenvalues:")
        print("  " + ", ".join(f"{x:+.10f}" for x in real_vals))

    all_fit = best_affine_fit(np.sort(real_vals), target)
    print(
        "best affine fit on sorted full spectrum "
        f"(m={all_fit['count']}): gamma ~= {all_fit['scale']:.10g}*lambda + {all_fit['shift']:.10g}; "
        f"rms={all_fit['rms']:.6g}, max={all_fit['max_abs']:.6g}"
    )

    pos = positive_branch(real_vals)
    if len(pos):
        pos_fit = best_affine_fit(pos, target)
        print(
            "best affine fit on positive branch "
            f"(m={pos_fit['count']}): gamma ~= {pos_fit['scale']:.10g}*lambda + {pos_fit['shift']:.10g}; "
            f"rms={pos_fit['rms']:.6g}, max={pos_fit['max_abs']:.6g}"
        )
    else:
        print("positive branch: empty")

    t = target[min(len(target), max(1, matrix.shape[0])) - 1]
    print(
        f"finite counting check at T={t:.3f}: candidate N(T)<={matrix.shape[0]}, "
        f"Riemann-von Mangoldt smooth N(T)~{rvm_count(t):.3f}"
    )


def hurwitz_channel_vector(t: float, dps: int = 50) -> np.ndarray:
    """Six Hurwitz channels f_r(t)=6^-s zeta(s,r/6), with f_0=6^-s."""
    mp.mp.dps = dps
    s = mp.mpc(0.5, t)
    out = [mp.power(Q, -s)]
    for r in range(1, Q):
        out.append(mp.power(Q, -s) * mp.zeta(s, mp.mpf(r) / Q))
    return np.array([complex(z) for z in out], dtype=complex)


def bures_amplitude_from_diag(diag: np.ndarray, t: float, dps: int = 50) -> complex:
    mp.mp.dps = dps
    s = mp.mpc(0.5, t)
    total = mp.mpc(0)
    for r in range(1, Q):
        total += mp.zeta(s, mp.mpf(r) / Q) * complex(diag[r])
    total *= mp.power(Q, -s)
    return complex(total)


@dataclass
class ProjectedOps:
    d_dt: np.ndarray
    p_t: np.ndarray
    x_t: np.ndarray
    b_mult: np.ndarray
    sample_t: np.ndarray
    derivative_residual: float
    multiplication_residual: float
    bures_residual: float


def projected_critical_line_ops(
    sample_t: np.ndarray | None = None,
    dps: int = 50,
    h: float = 1.0e-5,
) -> ProjectedOps:
    """Least-squares finite-channel projection of d/dt, t, and B_G(t).

    The samples intentionally avoid using zeros. This tests whether the Z/6
    Hurwitz channel span is closed enough under the requested operations.
    """
    if sample_t is None:
        sample_t = np.linspace(7.0, 62.0, 56)
    f_cols = []
    df_cols = []
    tf_cols = []
    bf_cols = []
    diag = np.diag(g_balanced())
    for t in sample_t:
        f = hurwitz_channel_vector(float(t), dps=dps)
        fp = hurwitz_channel_vector(float(t + h), dps=dps)
        fm = hurwitz_channel_vector(float(t - h), dps=dps)
        df = (fp - fm) / (2.0 * h)
        b = bures_amplitude_from_diag(diag, float(t), dps=dps)
        f_cols.append(f)
        df_cols.append(df)
        tf_cols.append(float(t) * f)
        bf_cols.append(b * f)

    f_mat = np.column_stack(f_cols)
    df_mat = np.column_stack(df_cols)
    tf_mat = np.column_stack(tf_cols)
    bf_mat = np.column_stack(bf_cols)

    # Solve A F ~= Y as A = Y pinv(F).
    pinv_f = np.linalg.pinv(f_mat, rcond=1.0e-10)
    d_dt = df_mat @ pinv_f
    x_t = tf_mat @ pinv_f
    b_mult = bf_mat @ pinv_f

    derivative_residual = matrix_norm(d_dt @ f_mat - df_mat) / max(matrix_norm(df_mat), 1.0e-300)
    multiplication_residual = matrix_norm(x_t @ f_mat - tf_mat) / max(matrix_norm(tf_mat), 1.0e-300)
    bures_residual = matrix_norm(b_mult @ f_mat - bf_mat) / max(matrix_norm(bf_mat), 1.0e-300)

    return ProjectedOps(
        d_dt=d_dt,
        p_t=hermitian_part(-1j * d_dt),
        x_t=hermitian_part(x_t),
        b_mult=b_mult,
        sample_t=sample_t,
        derivative_residual=float(derivative_residual),
        multiplication_residual=float(multiplication_residual),
        bures_residual=float(bures_residual),
    )


def print_projection_residuals(ops: ProjectedOps) -> None:
    print("projection window: t in [{:.3f}, {:.3f}], {} samples".format(
        float(np.min(ops.sample_t)), float(np.max(ops.sample_t)), len(ops.sample_t)
    ))
    print(f"relative d/dt projection residual: {ops.derivative_residual:.6e}")
    print(f"relative t multiplication projection residual: {ops.multiplication_residual:.6e}")
    print(f"relative B_G multiplication projection residual: {ops.bures_residual:.6e}")
