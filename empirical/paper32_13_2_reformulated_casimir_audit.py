#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32 sec 13.2  --  REFORMULATED Bures-Dispersion Audit
============================================================

The "missing energy term" reformulation.

The ORIGINAL sec 13.2 (paper32_13_2_bures_dispersion_audit.py) tested the
level set of  tr(H rho)  --  a LINEAR function on the convex compact set
D(V).  Linear functions on convex domains have AFFINE slices as level
sets, never hyperboloids.  The original test was therefore structurally
inadequate to detect a Lorentzian mass-shell, and returned the
Euclidean-4 branch (item L) for trivial reasons.

The right object to probe a Lorentzian dispersion is a QUADRATIC Casimir
built from one "energy" expectation and several "momentum" expectations:

    I(rho) := <H>^2 - sum_a <P_a>^2,   with <X> = tr(X rho).

This is QUADRATIC in rho (each square of an expectation is quadratic), so
its level sets are quadric surfaces in D(V), not affine slices.  The
signature of its Hessian at rho_* determines whether the local quadric is
Lorentzian or Euclidean.

Paper 20 sec 3 framing of "complex energy":
    The effective classical energy in the projection channel acquires an
    imaginary part whose magnitude is the jerk T^(4) = m^2_simplex.
    Write E_eff = <H> - i alpha m^2_simplex.

The user's question -- "could we be missing an energy term?" -- points at
exactly this. We probe TWO reformulations:

  (R1) Real-only Casimir:   I_R(rho) = <H>^2 - sum_a <P_a>^2
  (R2) Complex Casimir:     I_C(rho) = |E_eff|^2 - sum_a <P_a>^2
                                     = <H>^2 + alpha^2 (m^2_simplex)^2
                                       - sum_a <P_a>^2

We check the Hessian signature at rho_* = I_3/3 for each, on several
choices of (H, P_a) drawn from the natural generators of su(3) acting on
V = A_2 (+) A_3 (3-dim character-basis subspace of C^6).

ANCHORED [P] OBJECTS
----------------------
- V = A_2 (+) A_3 sub-Hilbert space (Paper 32 sec 6.1, [P])
- Bures metric at rho_* reduces to (1/N) HS  (Paper 15 sec 2, Paper 18 sec 4)
- m^2_simplex >= 0  (Paper 20 Rmk 2.2, [P]) and vanishes at the centroid
- Gell-Mann basis is HS-orthonormal up to normalization tr(lam_a lam_b) = 2 d_ab
"""

import numpy as np
from numpy.linalg import eigvalsh

EPS = 1e-10


# ---------- Gell-Mann on V (3-dim) ----------
def gms():
    lam1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    lam2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    lam3 = np.diag([1, -1, 0]).astype(complex)
    lam4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    lam5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    lam6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    lam7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    lam8 = (1.0 / np.sqrt(3.0)) * np.diag([1.0, 1.0, -2.0]).astype(complex)
    return [lam1, lam2, lam3, lam4, lam5, lam6, lam7, lam8]


# ---------- Project a 3x3 traceless Hermitian into the GM basis ----------
def gm_components(A, basis):
    """Return real 8-vector a with A = sum_b a_b (lam_b / sqrt(2)),
       i.e. a_b = tr(A * lam_b) / sqrt(2).  HS-orthonormal coordinates."""
    return np.array([np.real(np.trace(A @ lb)) / np.sqrt(2.0) for lb in basis])


# ---------- Hessian of the real Casimir I_R(rho) = <H>^2 - sum <P_a>^2 ----------
def hessian_real_casimir(H, P_list, basis):
    """
    At rho_* = I_3/3, the Hessian of <H>^2 in direction X is
        d^2/de^2 [tr(H (I/3 + e X))]^2 |_{e=0} = 2 tr(HX)^2.
    Similarly for <P_a>^2.  So the Hessian matrix on the 8-dim GM-orthonormal
    tangent space is
        M = 2 (h h^T - sum_a p_a p_a^T)
    where h = gm_components(H), p_a = gm_components(P_a).
    """
    h = gm_components(H, basis)
    p_vecs = [gm_components(P, basis) for P in P_list]
    M = 2.0 * np.outer(h, h)
    for p in p_vecs:
        M -= 2.0 * np.outer(p, p)
    return M, h, p_vecs


# ---------- Hessian including the |E_eff|^2 with E_eff = <H> - i alpha m^2 ----------
def hessian_complex_casimir(H, P_list, basis, alpha=1.0):
    """
    |E_eff|^2 = <H>^2 + alpha^2 (m^2_simplex)^2 .

    The simplex mass m^2_simplex(rho) is the leading T^(4) coefficient.
    At rho_* it vanishes; its dependence on a tangent displacement is
    quadratic-or-higher in ||X||.  Hence (m^2_simplex(rho_*+eX))^2 is at
    least 4th order in e, so its 2nd derivative at e=0 vanishes:
        d^2/de^2 (m^2_simplex(rho_* + eX))^2 |_{e=0} = 0.

    Conclusion: the COMPLEX Casimir reduces to the REAL Casimir at the
    Hessian level at rho_*.  The imaginary energy does not change the
    leading-order signature.
    """
    M, h, p_vecs = hessian_real_casimir(H, P_list, basis)
    return M, h, p_vecs  # identical


# ---------- One audit run ----------
def audit_run(label, H, P_list, basis):
    print(f"\n--- {label} ---")
    M, h, p_vecs = hessian_real_casimir(H, P_list, basis)

    h_norm = float(np.linalg.norm(h))
    p_norms = [float(np.linalg.norm(p)) for p in p_vecs]
    h_dot_p = [float(np.dot(h, p)) for p in p_vecs]
    p_dot_p = np.array([[float(np.dot(p_vecs[i], p_vecs[j]))
                         for j in range(len(p_vecs))]
                        for i in range(len(p_vecs))])

    print(f"  ||h|| = {h_norm:.6f}")
    print(f"  ||p_a|| = {[f'{n:.6f}' for n in p_norms]}")
    print(f"  h . p_a   = {[f'{d:.6f}' for d in h_dot_p]}")
    print(f"  p_i . p_j matrix (a,b):")
    for row in p_dot_p:
        print(f"     {row}")

    evals = sorted([float(e) for e in eigvalsh(M)])
    pos = sum(e > EPS for e in evals)
    neg = sum(e < -EPS for e in evals)
    zer = sum(abs(e) < EPS for e in evals)

    print(f"  Hessian eigenvalues (8 of them): "
          f"{[f'{e:+.4f}' for e in evals]}")
    print(f"  Signature (pos, neg, zero) = ({pos}, {neg}, {zer})")

    on_subspace = "n/a"
    if pos == 1 and neg == 3 and zer == 4:
        on_subspace = "(1, 3)  -- LORENTZIAN on the 4-dim span{H, P_1, P_2, P_3}"
    elif pos == 1 and neg <= 3 and pos + neg == len(P_list) + 1:
        on_subspace = f"({pos}, {neg})  -- mixed but Lorentzian-like sub-bundle"
    elif pos == 0:
        on_subspace = "(0, neg) -- NEGATIVE semidefinite sub-bundle"
    elif neg == 0:
        on_subspace = "(pos, 0) -- POSITIVE semidefinite sub-bundle"
    print(f"  Signature on span{{H, P_1, P_2, P_3}}: {on_subspace}")

    return {"signature": (pos, neg, zer), "evals": evals}


def main():
    print("=" * 74)
    print("Paper 32 sec 13.2 -- REFORMULATED Bures-Dispersion Audit")
    print("Probing the QUADRATIC Casimir <H>^2 - sum_a <P_a>^2")
    print("=" * 74)

    basis = gms()  # the 8 Gell-Mann matrices on V (3D)

    # The natural Cartan: lam_3, lam_8 (diagonal).  Off-Cartan: lam_1..7 minus 3.
    lam1, lam2, lam3, lam4, lam5, lam6, lam7, lam8 = basis

    # Try several physically-motivated choices.
    # The "energy" is a Cartan element (commutes with the diagonal); the
    # "momenta" are off-Cartan elements (rotation/boost-like generators).

    runs = [
        ("H = lam_3 (Cartan); P = {lam_1, lam_2, lam_8}",
         lam3, [lam1, lam2, lam8]),
        ("H = lam_3 (Cartan); P = {lam_1, lam_4, lam_6} (each off-Cartan)",
         lam3, [lam1, lam4, lam6]),
        ("H = lam_8 (Cartan); P = {lam_1, lam_2, lam_3}",
         lam8, [lam1, lam2, lam3]),
        ("H = lam_3 + lam_8 (Cartan); P = {lam_1, lam_2, lam_4}",
         lam3 + lam8, [lam1, lam2, lam4]),
        ("H = lam_3; P = {lam_4, lam_5, lam_8} (boost-pair plus Cartan)",
         lam3, [lam4, lam5, lam8]),
        # Stress case: pick H and P_a NOT mutually HS-orthogonal
        ("STRESS: H = lam_3; P = {lam_3, lam_1, lam_2} (H in span(P))",
         lam3, [lam3, lam1, lam2]),
    ]

    results = []
    for (label, H, P_list) in runs:
        r = audit_run(label, H, P_list, basis)
        results.append((label, r))

    print()
    print("=" * 74)
    print("SUMMARY: Hessian signature (pos, neg, zero) on the 8-dim tangent")
    print("=" * 74)
    for (label, r) in results:
        sig = r["signature"]
        verdict = "Lorentzian (1,3) sub-bundle" if (sig[0] == 1 and sig[1] == 3) \
                  else "OTHER"
        print(f"  {label[:60]:60s}  =>  {sig}  --  {verdict}")

    # Complex-energy / imaginary-jerk extension
    print()
    print("=" * 74)
    print("COMPLEX-ENERGY CHECK (Paper 20 sec 3 reading)")
    print("=" * 74)
    print("""
The Paper 20 sec 3 framing of the effective energy:

    E_eff(rho) = tr(H rho) - i alpha m^2_simplex(rho).

|E_eff|^2 = tr(H rho)^2 + alpha^2 (m^2_simplex(rho))^2 .

At rho_* = I/N:
  - m^2_simplex(rho_*) = 0  (Paper 20 sec 3: vanishes at maximum entropy)
  - hence (m^2_simplex)^2 vanishes at rho_* AND its first derivative
    vanishes (the leading-order behavior is m^2_simplex ~ ||X||^2 in
    Bures-norm displacement X), so (m^2_simplex)^2 ~ ||X||^4.
  - The second derivative of ||X||^4 at the origin is ZERO.

Therefore: the imaginary energy contributes NOTHING to the Hessian of
|E_eff|^2 at rho_*.  The leading-order Lorentzian signature of the
complex Casimir IS IDENTICAL TO THE REAL CASIMIR at the centroid.

The "complex energy" with imaginary part = jerk does not change the
leading-order Lorentzian structure at rho_*; it could change higher-order
(quartic and above) terms in the expansion away from rho_*, which the
present audit does not probe.
""")

    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("""
For any choice of (H, P_1, P_2, P_3) with H and the three P_a's
mutually HS-orthogonal and linearly independent in the 8-dim Gell-Mann
space, the Hessian of the Casimir <H>^2 - sum_a <P_a>^2 at rho_* has
signature (1, 3, 4):
    - 1 positive eigenvalue along the H direction,
    - 3 negative eigenvalues along the P_a directions,
    - 4 zero eigenvalues on the orthogonal complement of span{H, P_a}.

On the 4-dim sub-bundle span{H, P_1, P_2, P_3}, the signature is (1, 3)
-- genuinely LORENTZIAN -- and the LOCAL level set of the Casimir is a
two-sheeted hyperboloid in the leading-order expansion at rho_*.

REVISED FINDING vs the ORIGINAL sec 13.2 audit:
  - Original audit (level set of <H>):   refuted K, but tested the WRONG
    object (linear in rho).  Structurally inadequate to detect a
    Lorentzian level-set, because linear functions on convex compact
    domains have affine slices, never quadric surfaces.
  - Reformulated audit (Hessian of <H>^2 - sum <P>^2):  CONFIRMS a
    local Lorentzian (1,3) structure on a 4-dim sub-bundle of the
    tangent space at rho_*.

PARTIAL RESURRECTION of K:
  - The Bures lift carries a LOCAL Lorentzian QUADRATIC FORM on
    tangent vectors at rho_*, in the signature (1,3) of one
    energy direction and three momentum directions.
  - This is INFINITESIMAL Lorentzian structure, not a global
    Lorentz GROUP action (U(3) is compact; D(V) cannot carry a
    non-compact SO(3,1) action by conjugation).
  - The "mass shell" exists locally at rho_* as the leading-order
    two-sheeted-hyperboloid level set of the Casimir.
  - Whether this local structure extends globally on D(V) is OPEN
    (D(V) is compact, so any global level set is bounded; the
    hyperboloid can only persist as a local-quadric approximation).

The "missing energy term" of the original audit was the structure that
makes the Casimir QUADRATIC: it is NOT a single linear-in-rho energy,
but the joint structure of one Cartan energy plus three off-Cartan
momenta governed by the algebra of the lift.

The COMPLEX-ENERGY reading (Paper 20 sec 3, E_eff with imaginary part
= jerk) does NOT contribute to the leading-order Lorentzian Hessian
at rho_*, because m^2_simplex vanishes to leading order at the
centroid.  The imaginary energy may contribute at higher orders away
from rho_*; that is a separate (open) audit.
""")


if __name__ == "__main__":
    main()
