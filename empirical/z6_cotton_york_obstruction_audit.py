"""Cotton-York conformal obstruction audit for Paper 28, T*1'.

In three dimensions, the Weyl tensor vanishes identically and conformal
geometry is controlled by the Cotton tensor.  This audit computes the
scale-free invariant

    I = tr(CY^3)^2 / tr(CY^2)^3

for:

1. the mass-weighted physical shape metric G_shape in (rho,u,w), and
2. the Fisher metric restricted to the Z6 V2+V3 sector.

This numerical audit is a falsifier for proposed point matches and a range
test for the Z6 sector.  A global no-go still requires proving that the target
invariant range cannot intersect the physical shape invariant range.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_jacobi_fisher_execution_audit import shape_metric, z6_basis


EPS_SYMBOL = np.array(
    [
        [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]],
        [[0.0, 0.0, -1.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
    ]
)


def fisher_sector_metric(x: np.ndarray, eps: float) -> np.ndarray:
    basis = z6_basis()
    frame = np.stack([basis["e_rho"], basis["e_u"], basis["e_w"]], axis=1)
    p = np.full(6, 1.0 / 6.0) + eps * (frame @ x)
    if np.any(p <= 0):
        raise ValueError("point left the positive simplex")
    return eps**2 * frame.T @ np.diag(1.0 / p) @ frame


def metric_derivatives(metric_fn, x: np.ndarray, h: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    g0 = metric_fn(x)
    dg = np.zeros((3, 3, 3))
    ddg = np.zeros((3, 3, 3, 3))
    for a in range(3):
        xp = x.copy()
        xm = x.copy()
        xp[a] += h
        xm[a] -= h
        gp = metric_fn(xp)
        gm = metric_fn(xm)
        dg[a] = (gp - gm) / (2.0 * h)
        ddg[a, a] = (gp - 2.0 * g0 + gm) / (h * h)
        for b in range(a + 1, 3):
            xpp = x.copy()
            xpm = x.copy()
            xmp = x.copy()
            xmm = x.copy()
            xpp[a] += h
            xpp[b] += h
            xpm[a] += h
            xpm[b] -= h
            xmp[a] -= h
            xmp[b] += h
            xmm[a] -= h
            xmm[b] -= h
            mixed = (metric_fn(xpp) - metric_fn(xpm) - metric_fn(xmp) + metric_fn(xmm)) / (4.0 * h * h)
            ddg[a, b] = mixed
            ddg[b, a] = mixed
    return g0, dg, ddg


def christoffel(g: np.ndarray, dg: np.ndarray) -> np.ndarray:
    inv = np.linalg.inv(g)
    gamma = np.zeros((3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                gamma[i, j, k] = 0.5 * sum(
                    inv[i, l] * (dg[j, k, l] + dg[k, j, l] - dg[l, j, k])
                    for l in range(3)
                )
    return gamma


def christoffel_derivatives(g: np.ndarray, dg: np.ndarray, ddg: np.ndarray) -> np.ndarray:
    inv = np.linalg.inv(g)
    dinv = np.zeros((3, 3, 3))
    for a in range(3):
        dinv[a] = -inv @ dg[a] @ inv
    dgamma = np.zeros((3, 3, 3, 3))
    for a in range(3):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    term = 0.0
                    for l in range(3):
                        combo = dg[j, k, l] + dg[k, j, l] - dg[l, j, k]
                        dcombo = ddg[a, j, k, l] + ddg[a, k, j, l] - ddg[a, l, j, k]
                        term += dinv[a, i, l] * combo + inv[i, l] * dcombo
                    dgamma[a, i, j, k] = 0.5 * term
    return dgamma


def ricci_tensor(gamma: np.ndarray, dgamma: np.ndarray) -> np.ndarray:
    ric = np.zeros((3, 3))
    for j in range(3):
        for l in range(3):
            val = 0.0
            for i in range(3):
                val += dgamma[i, i, j, l] - dgamma[l, i, j, i]
                for m in range(3):
                    val += gamma[i, i, m] * gamma[m, j, l] - gamma[i, l, m] * gamma[m, j, i]
            ric[j, l] = val
    return 0.5 * (ric + ric.T)


def schouten_at(metric_fn, x: np.ndarray, h: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    g, dg, ddg = metric_derivatives(metric_fn, x, h)
    gam = christoffel(g, dg)
    dgam = christoffel_derivatives(g, dg, ddg)
    ric = ricci_tensor(gam, dgam)
    scalar = float(np.einsum("ij,ij->", np.linalg.inv(g), ric))
    p = ric - 0.25 * scalar * g
    return p, g, gam


def cotton_york(metric_fn, x: np.ndarray, h: float) -> dict:
    p0, g, gam = schouten_at(metric_fn, x, h)
    inv = np.linalg.inv(g)
    det = float(np.linalg.det(g))
    d_p = np.zeros((3, 3, 3))
    for a in range(3):
        xp = x.copy()
        xm = x.copy()
        xp[a] += h
        xm[a] -= h
        pp, _, _ = schouten_at(metric_fn, xp, h)
        pm, _, _ = schouten_at(metric_fn, xm, h)
        d_p[a] = (pp - pm) / (2.0 * h)
    cov_d_p = np.zeros((3, 3, 3))
    for k in range(3):
        for l in range(3):
            for j in range(3):
                cov_d_p[k, l, j] = d_p[k, l, j]
                for m in range(3):
                    cov_d_p[k, l, j] -= gam[m, k, l] * p0[m, j]
                    cov_d_p[k, l, j] -= gam[m, k, j] * p0[l, m]
    p_mixed_deriv = np.einsum("jm,klm->klj", inv, cov_d_p)
    cy_upper = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            cy_upper[i, j] = sum(EPS_SYMBOL[i, k, l] * p_mixed_deriv[k, l, j] for k in range(3) for l in range(3))
    cy_upper /= math.sqrt(max(det, 1.0e-300))
    cy_mixed = g @ cy_upper
    cy_mixed = 0.5 * (cy_mixed + np.linalg.inv(g) @ cy_mixed.T @ g)
    cy_mixed -= (np.trace(cy_mixed) / 3.0) * np.eye(3)
    j2 = float(np.trace(cy_mixed @ cy_mixed))
    j3 = float(np.trace(cy_mixed @ cy_mixed @ cy_mixed))
    invariant = None if abs(j2) < 1.0e-300 else (j3 * j3) / (j2 * j2 * j2)
    return {
        "metric": g.tolist(),
        "cotton_york_mixed": cy_mixed.tolist(),
        "J2": j2,
        "J3": j3,
        "I": invariant,
        "eigenvalues": np.linalg.eigvals(cy_mixed).real.tolist(),
        "cotton_norm": float(np.linalg.norm(cy_mixed)),
    }


def audit(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    rho0 = math.log(args.perimeter0)
    sigma = np.array([rho0, args.u, args.w])
    x = np.array([args.rho_offset, args.u, args.w])

    shape_fn = lambda sig: shape_metric(sig, masses, args.metric_step)
    fisher_fn = lambda y: fisher_sector_metric(y, args.epsilon)
    shape = cotton_york(shape_fn, sigma, args.curvature_step)
    fisher = cotton_york(fisher_fn, x, args.curvature_step)
    if shape["I"] is None or fisher["I"] is None:
        rel_delta = None
        status = "DEGENERATE"
        kills = ["Cotton-York J2 too small for invariant comparison"]
    else:
        rel_delta = abs(shape["I"] - fisher["I"]) / max(abs(shape["I"]), abs(fisher["I"]), 1.0e-300)
        status = "PASS" if rel_delta <= args.invariant_tol else "KILL"
        kills = [] if status == "PASS" else ["Cotton-York invariant mismatch"]
    return {
        "claim_tested": "local conformal-invariant compatibility of G_shape and Z6 Fisher sector",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "shape": shape,
        "fisher_sector": fisher,
        "summary": {
            "status": status,
            "relative_invariant_delta": rel_delta,
            "shape_I": shape["I"],
            "fisher_I": fisher["I"],
            "shape_cotton_norm": shape["cotton_norm"],
            "fisher_cotton_norm": fisher["cotton_norm"],
            "kills": kills,
        },
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Cotton-York Obstruction Audit",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- relative invariant delta: {s['relative_invariant_delta']}",
        f"- shape I: {s['shape_I']}",
        f"- Fisher-sector I: {s['fisher_I']}",
        f"- shape Cotton norm: {s['shape_cotton_norm']:.6e}",
        f"- Fisher Cotton norm: {s['fisher_cotton_norm']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Interpretation",
        "",
        "A KILL is a local conformal-invariant mismatch for this sampled point",
        "assignment. A full global no-go requires proving that the Fisher-sector",
        "invariant range cannot match the physical shape invariant range under",
        "any admissible point map.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--perimeter0", type=float, default=3.0)
    parser.add_argument("--rho-offset", type=float, default=0.0)
    parser.add_argument("--u", type=float, default=0.08)
    parser.add_argument("--w", type=float, default=-0.05)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--metric-step", type=float, default=1.0e-5)
    parser.add_argument("--curvature-step", type=float, default=3.0e-4)
    parser.add_argument("--invariant-tol", type=float, default=1.0e-2)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_obstruction_audit.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_obstruction_audit.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
