"""Persistence under refinement (Paper 53 §4.7): is an off-line zero of the finite port a feature or an artifact?

With the Hagedorn tail carried along, the functional equation gives exactly
    S_X(s) = chi(s) A_X(1-s) / A_X(s) = exp(R_X(s) - R_X(1-s)),   R_X = log(target) - (L_X + E_X),
so an off-line zero of the port is either the shadow of an off-line zero of the target (log(target) is singular
there, and the shadow converges as X grows) or a fluctuation of the mirror tail R_X(1-s) (it wanders with X).
Test: locate the port's off-line zeros in a window at successive resolutions and measure how far each moves.
"""
import numpy as np
from p53_third_law_curve import make, XGRID


def strip_zeros(F, s_lo, s_hi, t_lo, t_hi, dsig=0.01, dt=0.02):
    sg = np.arange(s_lo, s_hi + dsig / 2, dsig)
    tg = np.arange(t_lo, t_hi + dt / 2, dt)
    S = sg[:, None] + 1j * tg[None, :]
    L = np.log(np.abs(F(S)) + 1e-300)
    core = L[1:-1, 1:-1]
    nb = np.stack([L[1 + a:L.shape[0] - 1 + a, 1 + b:L.shape[1] - 1 + b]
                   for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)])
    found = []
    for z in S[1:-1, 1:-1][core < nb.min(axis=0)]:
        step = 1.0
        for _ in range(60):
            f = F(np.array([z]))[0]
            d = (F(np.array([z + 1e-6]))[0] - F(np.array([z - 1e-6]))[0]) / 2e-6
            if d == 0:
                break
            step = f / d
            z = z - step
            if abs(step) < 1e-13:
                break
        if abs(step) < 1e-10 and s_lo < z.real < s_hi and t_lo <= z.imag <= t_hi \
                and all(abs(z - w) > 1e-6 for w in found):
            found.append(z)
    return np.array(found)


def track(name, t0, t1, xs, target=None):
    prev = None
    print(f"\n{name} window [{t0},{t1}]" + (f", target off-line zero {target}" if target is not None else ""))
    for X in xs:
        F, arch = make(name, X)
        z = strip_zeros(F, 0.502, 0.999, t0, t1)
        moved = "" if prev is None or len(prev) == 0 or len(z) == 0 else \
            f" | median move from previous X: {np.median([np.min(np.abs(prev - w)) for w in z]):.3f}"
        near = "" if target is None or len(z) == 0 else \
            f" | nearest to target: {z[np.argmin(np.abs(z - target))]:.6f} (dist {np.min(np.abs(z - target)):.2e})"
        print(f"  X={X:5d}: {len(z):3d} off-line{moved}{near}")
        prev = z


if __name__ == "__main__":
    xs = [x for x in XGRID if x >= 13]
    track("DH", 80.0, 100.0, xs, target=0.808517 + 85.699348j)
    track("DH", 160.0, 180.0, xs, target=0.724258 + 176.702461j)
    track("zeta_c", 20.0, 40.0, xs)
    track("zeta_c", 100.0, 120.0, xs)
    track("zeta_c", 400.0, 420.0, xs)
