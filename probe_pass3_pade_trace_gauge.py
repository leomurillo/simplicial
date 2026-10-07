"""Pass-3 Pade/Stieltjes trace-gauge microscope.

For

    B(x) = Xi(i sqrt(x)) / Xi(0)
    S(x) = log B(x)
    S'(x) = sum_{k>=0} (-1)^k ell_{k+1} x^k

RH predicts that

    S'(x) = sum_a lambda_a / (1 + lambda_a x)

with lambda_a = gamma_a^{-2} and determinant multiplicity one.

The [N-1/N] Pade approximant of S' is the finite Stieltjes quadrature
microscope:

    S'_N(x) = sum_a w_a / (1 + lambda_a x).

It should have lambda_a >= 0 and w_a > 0 if the Stieltjes structure is
visible. The Pass-3 trace gauge asks for the stronger determinant-class
condition w_a/lambda_a -> integer multiplicity, ideally 1 for simple
eigenvalues in the exact finite determinant case.

This is a numerical probe, not a proof.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np


PROBE_PATH = Path(__file__).with_name("probe_pass3_folded_xi_trace_model.py")
spec = importlib.util.spec_from_file_location("folded_probe", PROBE_PATH)
folded_probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folded_probe)


def pade_stieltjes_from_ells(ells: list[float], n: int):
    """Return denominator, numerator, lambdas, weights for [n-1/n]."""
    # a_k are coefficients of S'(x).
    a = np.array([((-1) ** k) * ells[k] for k in range(2 * n)], dtype=np.float64)

    # Solve a_k + q1 a_{k-1}+...+qn a_{k-n}=0 for k=n..2n-1.
    mat = np.zeros((n, n), dtype=np.float64)
    rhs = np.zeros(n, dtype=np.float64)
    for row, k in enumerate(range(n, 2 * n)):
        rhs[row] = -a[k]
        for j in range(1, n + 1):
            mat[row, j - 1] = a[k - j]
    q_tail = np.linalg.solve(mat, rhs)
    q = np.concatenate(([1.0], q_tail))

    # Numerator p_k = sum_{j=0..min(k,n)} q_j a_{k-j}, k=0..n-1.
    p = np.zeros(n, dtype=np.float64)
    for k in range(n):
        p[k] = sum(q[j] * a[k - j] for j in range(0, min(k, n) + 1))

    # Roots of Q(x)=q[0]+q[1]x+...+q[n]x^n.
    roots = np.roots(q[::-1])
    lambdas = []
    weights = []
    for r in roots:
        lam = -1.0 / r
        # residue of P/Q at r is P(r)/Q'(r).
        pr = sum(p[k] * (r ** k) for k in range(n))
        qprime = sum(k * q[k] * (r ** (k - 1)) for k in range(1, n + 1))
        residue = pr / qprime
        # w/(1+lambda x) has residue w/lambda at x=-1/lambda.
        w = lam * residue
        lambdas.append(lam)
        weights.append(w)

    # Sort by descending lambda magnitude, which corresponds to low zeros.
    pairs = sorted(zip(lambdas, weights), key=lambda z: z[0].real, reverse=True)
    return q, p, pairs


def main() -> None:
    coeff_order = 36
    b = folded_probe.folded_coefficients(coeff_order, radius=1.0, samples=512)
    ells_mp = folded_probe.formal_log_cumulants(b, 20)
    ells = [float(x) for x in ells_mp]

    print("Pade/Stieltjes trace-gauge microscope for S'(x)=d log B / dx")
    print("ell[1..8]:")
    for i, val in enumerate(ells[:8], start=1):
        print(f"  ell[{i}] = {val:.16e}")

    for n in range(1, 7):
        _q, _p, pairs = pade_stieltjes_from_ells(ells, n)
        print(f"\n[N-1/N] Pade with N={n}")
        print("  lambda              weight              weight/lambda")
        bad = 0
        for lam, w in pairs:
            if abs(lam.imag) > 1e-7 or abs(w.imag) > 1e-7 or lam.real <= 0 or w.real <= 0:
                bad += 1
            ratio = w / lam
            print(f"  {lam.real: .12e}  {w.real: .12e}  {ratio.real: .12e}")
        print(f"  nonpositive/complex atoms: {bad}")

    print("\nKnown first zeta-zero folded eigenvalues gamma_k^{-2}:")
    for k in range(1, 7):
        gamma = float(folded_probe.mp.im(folded_probe.mp.zetazero(k)))
        print(f"  k={k}: gamma={gamma:.12f}, gamma^-2={1/(gamma*gamma):.12e}")


if __name__ == "__main__":
    main()
