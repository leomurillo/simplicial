"""N0 three-front audit: finite HB model, additive clock, and Weil marginality.

This probe is intentionally modest. It does not prove RH and it does not use
the false fixed-prime Gram-square bridge. It checks three structural facts that
the N0 draft uses:

1. Zero-side finite approximants P_M+iP_M' are Hermite-Biehler on sampled
   upper-half-plane grids. This is a sanity model for the desired finite
   de Branges exhaustion; it is circular if used as proof because it uses zeros.
2. The true derivative-polarized E_B=Xi+iXi' has positive sampled de Branges
   margin and positive sampled phase velocity.
3. The additive log geometry sees zeros as 1/y Herglotz poles, while the
   quadratic Bures/Fubini-Study curvature of L_chi3/Xi stays finite there.

It also builds a small Weil matrix to show the expected marginal behavior.
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp
import numpy as np


mp.mp.dps = 40


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "empirical" / "reports" / "n0_three_fronts.md"


def xi_s(s: complex) -> complex:
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi(z: complex) -> complex:
    return xi_s(mp.mpf("0.5") + 1j * z)


def dXi(z: complex, n: int = 1) -> complex:
    return mp.diff(Xi, z, n)


def E_true(z: complex) -> complex:
    return Xi(z) + 1j * dXi(z)


def sharp(E, z: complex) -> complex:
    return mp.conj(E(mp.conj(z)))


def hb_margin(E, z: complex) -> mp.mpf:
    a = abs(E(z)) ** 2
    b = abs(sharp(E, z)) ** 2
    return mp.re((a - b) / (a + b))


def phi_prime(x: mp.mpf) -> mp.mpf:
    x1 = dXi(x, 1)
    x2 = dXi(x, 2)
    x0 = Xi(x)
    return mp.re((x1 * x1 - x0 * x2) / (x0 * x0 + x1 * x1))


def zeta_zero(n: int) -> mp.mpf:
    return mp.im(mp.zetazero(n))


def finite_zero_poly(gammas: list[mp.mpf]):
    def P(z: complex) -> complex:
        out = mp.mpf(1)
        for g in gammas:
            out *= 1 - (z / g) ** 2
        return out

    def E(z: complex) -> complex:
        return P(z) + 1j * mp.diff(P, z)

    return E


def l_chi3(s: complex) -> complex:
    # Analytic continuation by Hurwitz zeta. The raw Dirichlet series is the
    # wrong numerical tool on the critical line.
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def L3_completed_z(z: complex) -> complex:
    s = mp.mpf("0.5") + 1j * z
    return mp.power(3 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * l_chi3(s)


def additive_u_at_zero(gamma: mp.mpf, y: mp.mpf) -> mp.mpf:
    z = gamma + 1j * y
    return mp.im(-dXi(z) / Xi(z))


def bures_curvature_at_zero(gamma: mp.mpf, eps: mp.mpf = mp.mpf("1e-5")) -> mp.mpf:
    # For M=L3/Xi, near a simple Xi zero M ~ A/(z-gamma), so FS curvature
    # |M'|^2/(1+|M|^2)^2 tends to 1/|A|^2.
    A = L3_completed_z(gamma) / dXi(gamma)
    return mp.re(1 / (abs(A) ** 2 + eps * 0))


def two_theta_prime(rvals: np.ndarray) -> np.ndarray:
    out = np.empty_like(rvals, dtype=float)
    lp = float(mp.log(mp.pi))
    for i, r in enumerate(rvals):
        out[i] = float(mp.re(mp.digamma(mp.mpf("0.25") + 1j * mp.mpf(float(r)) / 2))) - lp
    return out


def von_mangoldt_upto(nmax: int) -> list[tuple[int, float]]:
    out: list[tuple[int, float]] = []
    for n in range(2, nmax + 1):
        temp = n
        primes: set[int] = set()
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                primes.add(d)
                temp //= d
            d += 1
        if temp > 1:
            primes.add(temp)
        if len(primes) == 1:
            out.append((n, float(mp.log(next(iter(primes))))))
    return out


def basis_funcs(u: np.ndarray, L: float, m: int) -> np.ndarray:
    env = np.where(np.abs(u) <= L, (1 + np.cos(np.pi * u / L)) / 2, 0.0)
    return np.array([env * np.cos(k * np.pi * u / L) for k in range(m)])


def small_weil_matrix(L: float = 2.0, m: int = 10):
    du = 2 * L / 1400
    u = np.arange(-L, L + du / 2, du)
    g = basis_funcs(u, L, m)

    R, dr = 120.0, 0.12
    r = np.arange(-R, R + dr / 2, dr)
    ghat = (g @ np.cos(np.outer(r, u)).T) * du
    ttp = two_theta_prime(r)

    A = np.zeros((m, m))
    for j in range(m):
        wj = ghat[j] * ttp * dr / (2 * np.pi)
        for k in range(j, m):
            A[j, k] = A[k, j] = float(np.sum(wj * ghat[k]))

    Gk = (g * np.cosh(u / 2)) @ np.ones_like(u) * du
    pole = 2 * np.outer(Gk, Gk)

    nmax = int(np.floor(np.exp(2 * L)))
    vm = [(n, lam) for (n, lam) in von_mangoldt_upto(nmax) if np.log(n) <= 2 * L + 1e-9]
    P = np.zeros((m, m))
    for (n, lam) in vm:
        w = np.log(n)
        shifted = np.array([np.interp(u - w, u, g[k], left=0.0, right=0.0) for k in range(m)])
        P += 2 * lam / np.sqrt(n) * ((g @ shifted.T) * du)

    M = (A + pole - P)
    M = (M + M.T) / 2
    return M, A + pole, P


def main() -> int:
    out: list[str] = []

    def log(line: str = "") -> None:
        print(line)
        out.append(line)

    log("# N0 Three-Front Probe")
    log()
    log("This is an audit for `N0-DeBrangesExhaustionAndWeilDomination-Draft1.md`.")
    log("It is evidence for the shape of the proof targets, not a proof of RH.")
    log()

    xs = [mp.mpf(v) for v in ["0", "7", "14.1347251417", "17.5", "21.0220396388", "25.01085758"]]
    ys = [mp.mpf("0.10"), mp.mpf("0.35"), mp.mpf("0.80")]

    log("## Part A - zero-side finite Hermite-Biehler sanity model")
    log()
    for M in [4, 8, 16]:
        gammas = [zeta_zero(i) for i in range(1, M + 1)]
        E = finite_zero_poly(gammas)
        margins = [hb_margin(E, x + 1j * y) for x in xs for y in ys]
        log(f"M={M:2d}: sampled min HB margin for P_M+iP_M' = {mp.nstr(min(margins), 8)}")
    log()
    log("This uses true zeros, so it is a model of the desired finite HB exhaustion, not a proof.")
    log()

    log("## Part B - true E_B sampled margin and phase velocity")
    log()
    true_margins = [hb_margin(E_true, x + 1j * y) for x in xs for y in ys]
    log(f"sampled min HB margin for E_B=Xi+iXi' = {mp.nstr(min(true_margins), 8)}")
    log()
    log("| x | phi'(x) |")
    log("|---:|---:|")
    for x in xs:
        log(f"| {mp.nstr(x, 12)} | {mp.nstr(phi_prime(x), 10)} |")
    log()

    log("## Part C - additive divisor current vs quadratic Bures curvature")
    log()
    log("| zero | y | Im m_B(gamma+iy) | y Im m_B | FS curvature limit |")
    log("|---:|---:|---:|---:|---:|")
    for idx in [1, 2]:
        gamma = zeta_zero(idx)
        curv = bures_curvature_at_zero(gamma)
        for y in [mp.mpf("0.05"), mp.mpf("0.01")]:
            u = additive_u_at_zero(gamma, y)
            log(
                f"| gamma_{idx}={mp.nstr(gamma, 12)} | {mp.nstr(y, 4)} | "
                f"{mp.nstr(u, 10)} | {mp.nstr(y*u, 10)} | {mp.nstr(curv, 8)} |"
            )
    log()
    log("The additive log geometry has the 1/y Herglotz pole; the quadratic FS/Bures curvature is finite.")
    log()

    log("## Part D - small Weil matrix marginality")
    log()
    M, floor, prime = small_weil_matrix()
    ew = np.linalg.eigvalsh(M)
    ef = np.linalg.eigvalsh(floor)
    ep = np.linalg.eigvalsh(prime)
    log(f"lambda_min(Weil floor - prime) = {ew[0]:.6e}")
    log(f"lambda_min(archimedean floor + pole) = {ef[0]:.6e}")
    log(f"lambda_max(prime erosion block) = {ep[-1]:.6e}")
    log()
    log("The small matrix is only a coarse truncation, but it shows the intended anatomy: floor, erosion, marginality.")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\n[report -> {REPORT}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
