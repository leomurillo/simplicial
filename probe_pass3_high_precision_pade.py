"""High-precision Pass-3 Padé/Stieltjes dishwasher.

This script strengthens `probe_pass3_pade_trace_gauge.py` by using
mpmath linear algebra and polynomial roots. It extracts the finite
Stieltjes atoms of

    S'(x) = d/dx log(Xi(i sqrt(x))/Xi(0))

from folded cumulants and compares the resolved atoms with
gamma_k^{-2}, where gamma_k are Riemann-zero ordinates.

Numerical evidence only; not a proof.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp


mp.mp.dps = 120

PROBE_PATH = Path(__file__).with_name("probe_pass3_folded_xi_trace_model.py")
spec = importlib.util.spec_from_file_location("folded_probe", PROBE_PATH)
folded_probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folded_probe)
mp.mp.dps = 120
folded_probe.mp.mp.dps = 120


def pade_stieltjes_mp(ells: list[mp.mpf], n: int):
    """Return sorted (lambda, weight, ratio) for [n-1/n] Padé of S'."""
    a = [((-1) ** k) * ells[k] for k in range(2 * n)]

    mat = mp.matrix(n)
    rhs = mp.matrix(n, 1)
    for row, k in enumerate(range(n, 2 * n)):
        rhs[row] = -a[k]
        for j in range(1, n + 1):
            mat[row, j - 1] = a[k - j]

    q_tail = mp.lu_solve(mat, rhs)
    q = [mp.mpf(1)] + [q_tail[i] for i in range(n)]

    p = []
    for k in range(n):
        p.append(mp.fsum(q[j] * a[k - j] for j in range(0, min(k, n) + 1)))

    # mp.polyroots uses descending powers.
    roots = mp.polyroots(
        list(reversed(q)),
        maxsteps=2000,
        extraprec=100,
        error=False,
        cleanup=True,
    )
    atoms = []
    for r in roots:
        lam = -1 / r
        pr = mp.fsum(p[k] * (r**k) for k in range(n))
        qprime = mp.fsum(k * q[k] * (r ** (k - 1)) for k in range(1, n + 1))
        residue = pr / qprime
        weight = lam * residue
        ratio = weight / lam
        atoms.append((lam, weight, ratio))

    atoms.sort(key=lambda t: mp.re(t[0]), reverse=True)
    return atoms


def fmt(x: mp.mpc, digits: int = 18) -> str:
    if abs(mp.im(x)) < mp.mpf("1e-70"):
        return mp.nstr(mp.re(x), digits)
    return mp.nstr(x, digits)


def main() -> None:
    max_n = 10
    coeff_order = 2 * max_n + 4
    print(f"mp.dps={mp.mp.dps}, coefficient order={coeff_order}")

    b = folded_probe.folded_coefficients(coeff_order, radius=mp.mpf("1.0"), samples=1536)
    ells = folded_probe.formal_log_cumulants(b, 2 * max_n)

    known = []
    for k in range(1, max_n + 1):
        gamma = mp.im(mp.zetazero(k))
        known.append(1 / (gamma * gamma))

    print("\nKnown folded eigenvalues gamma_k^-2:")
    for k, val in enumerate(known, start=1):
        print(f"  k={k:2d}  {fmt(val, 22)}")

    for n in (4, 6, 8, 10):
        atoms = pade_stieltjes_mp(ells, n)
        print(f"\n[N-1/N] Padé/Stieltjes atoms, N={n}")
        print("  a   lambda                         weight/lambda           nearest known rel.err")
        bad = 0
        for a_idx, (lam, weight, ratio) in enumerate(atoms, start=1):
            if abs(mp.im(lam)) > mp.mpf("1e-50") or abs(mp.im(weight)) > mp.mpf("1e-50"):
                bad += 1
            if mp.re(lam) <= 0 or mp.re(weight) <= 0:
                bad += 1
            nearest = min(known, key=lambda z: abs(mp.re(lam) - z))
            rel = abs(mp.re(lam) - nearest) / nearest
            print(
                f"  {a_idx:2d}  {fmt(lam, 24):>28}  "
                f"{fmt(ratio, 18):>22}  {mp.nstr(rel, 8)}"
            )
        print(f"  bad atoms = {bad}")


if __name__ == "__main__":
    main()
