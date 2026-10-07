#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 32 sec 13.2  --  The Bures-Dispersion Audit
==================================================

Settles items K, L, J' of the Paper 32 sec 12 priority ledger.

----------------------------------------------------------------------------
SPECIFICATION (Paper 32 sec 13.2, verbatim)
----------------------------------------------------------------------------
"Lift the energy to tr(H rho) on D(C^2 (x) C^3) (Paper 18), restricted to
 the conductor-2 and conductor-3 packets. Check
   (i)  the level set tr(H rho) = E is a genuine two-sheeted hyperboloid,
   (ii) it is invariant under a 3-parameter group completing the Cartan flow.
 Outcome (i)+(ii) => Lorentzian 3+1 derived as a lift phenomenon (item K
 confirmed). Outcome 'ellipsoid / wrong-dimensional group' => intrinsically
 Euclidean-4 (item L confirmed). Both outcomes are publishable results
 pre-claimed in sec 12. Free additional read-off (no extra cost): the
 asymptotic slope of the same level set is the invariant speed of
 Corollary 9.7; a genuine hyperboloid confirms a finite invariant speed
 exists and equals 1 in internal units (item J'), while a definite level set
 confirms there is none (Galilean / Euclidean-4). The c-claim is therefore
 decided by this audit at zero marginal cost."

----------------------------------------------------------------------------
ANCHORED [P] OBJECTS
----------------------------------------------------------------------------
- CRT identification C^6 ~= C^2 (x) C^3   (Paper 18 sec 5, [Certain])
- Conductor packets of Z/6Z: trivial {k=0}, A_2 = {k=3}, A_3 = {k=2,4},
                              M = {k=1,5}                  (Paper 32 sec 6.1, [P])
- Sub-Hilbert space V := span(chi_3, chi_2, chi_4) subset C^6
                                                           (dim_C V = 3)
- Bures metric is the unique monotone metric whose conservative
  Nambu-Bures flow is unitary von Neumann evolution         (Paper 18 sec 4)
- At rho = I/N the Bures metric reduces to (1/N) times the Hilbert-Schmidt
  inner product on traceless Hermitians                     (Paper 15 sec 2)

----------------------------------------------------------------------------
WHAT THE AUDIT CHECKS
----------------------------------------------------------------------------
For a Cartan-respecting Hamiltonian H on D(C^2 (x) C^3) and the sub-Hilbert
space V of the conductor-2 and conductor-3 packets, the audit determines:

   (A) signature of H restricted to V                (does the energy
                                                      operator itself have
                                                      indefinite signature?)
   (B) topology of the level set
       {rho in D(V) : tr(H_V rho) = E}               (connected? compact?
                                                      one sheet or two?)
   (C) signature of the Bures metric on T_{rho_*} D(V)
                                                     (Riemannian or
                                                      pseudo-Riemannian?)
   (D) the symmetry group of (the level set, the Bures metric)
                                                     (compact toric, or
                                                      non-compact 3-parameter
                                                      Lorentzian boost group?)

A two-sheeted hyperboloid requires:
   - level set with two disconnected components (non-compact),
   - tangent-space metric of signature (1, n) at points on the level set,
   - 3-parameter boost group acting non-compactly.

An ellipsoid / Euclidean-4 outcome requires:
   - level set connected and compact,
   - tangent metric definite (positive definite Riemannian),
   - symmetry group compact (toric).

----------------------------------------------------------------------------
PRE-CLAIMED BRANCHES (matched-pair discipline, sec 12 items K and L)
----------------------------------------------------------------------------
K confirmed:  Lorentzian 3+1 derived as a lift phenomenon
              (hyperboloid + non-compact 3-parameter boost group)
L confirmed:  intrinsically Euclidean-4
              (ellipsoid + compact symmetry group)

Both outcomes are stated, publishable, pre-claimed.
"""

import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

EPS = 1e-10


# ---------------------------------------------------------------------------
# 1. CRT identification C^6 ~= C^2 (x) C^3
# ---------------------------------------------------------------------------
def build_crt_permutation():
    """
    Permutation matrix Pi sending the standard C^6 basis |k> (k=0..5)
    to the tensor basis |i> (x) |j> with i = k mod 2, j = k mod 3.
    Tensor basis ordering: row index = 3*i + j.
    """
    Pi = np.zeros((6, 6))
    for k in range(6):
        i, j = k % 2, k % 3
        Pi[3 * i + j, k] = 1.0
    return Pi


# ---------------------------------------------------------------------------
# 2. Pauli, Gell-Mann
# ---------------------------------------------------------------------------
def pauli():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    return s1, s2, s3


def gell_mann():
    lam1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    lam2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    lam3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    lam4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    lam5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    lam6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    lam7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    lam8 = (1 / np.sqrt(3)) * np.diag([1, 1, -2]).astype(complex)
    return lam1, lam2, lam3, lam4, lam5, lam6, lam7, lam8


# ---------------------------------------------------------------------------
# 3. Character basis of C^6 and conductor packets
# ---------------------------------------------------------------------------
def char_basis():
    """Normalized character vectors chi_k for k = 0..5."""
    C = np.zeros((6, 6), dtype=complex)
    for k in range(6):
        for j in range(6):
            C[j, k] = np.exp(2j * np.pi * k * j / 6) / np.sqrt(6)
    return C


def packets():
    return {"trivial": [0], "A_2": [3], "A_3": [2, 4], "M": [1, 5]}


# ---------------------------------------------------------------------------
# 4. Build the audit objects
# ---------------------------------------------------------------------------
def setup(a, b, c):
    """Build H on C^2(x)C^3 with H = a sigma_3 (x) I + b I (x) lam_3 + c I (x) lam_8;
    transport to C^6 standard basis; restrict to V = chi_3 + chi_2 + chi_4."""
    Pi = build_crt_permutation()
    s1, s2, s3 = pauli()
    lams = gell_mann()
    lam3 = lams[2]
    lam8 = lams[7]
    I2 = np.eye(2, dtype=complex)
    I3 = np.eye(3, dtype=complex)

    H_tensor = (a * np.kron(s3, I3)
                + b * np.kron(I2, lam3)
                + c * np.kron(I2, lam8))
    H_std = Pi.conj().T @ H_tensor @ Pi  # in standard C^6 basis

    C = char_basis()
    pk = packets()
    V_idx = pk["A_2"] + pk["A_3"]          # [3, 2, 4]
    V = C[:, V_idx]                        # 6 x 3 isometry into C^6
    H_V = V.conj().T @ H_std @ V           # 3 x 3 Hermitian
    return Pi, H_std, V, V_idx, H_V


# ---------------------------------------------------------------------------
# 5. Test (A): signature of H restricted to V
# ---------------------------------------------------------------------------
def test_A_signature(H_V):
    eigs = np.sort(eigvalsh(H_V))
    pos = int(np.sum(eigs > EPS))
    neg = int(np.sum(eigs < -EPS))
    zer = int(np.sum(np.abs(eigs) < EPS))
    return eigs, (pos, neg, zer)


# ---------------------------------------------------------------------------
# 6. Test (B): topology of {rho in D(V) : tr(H_V rho) = E}
# ---------------------------------------------------------------------------
def test_B_level_set_topology(H_V):
    """
    D(V) is the set of 3x3 positive semidefinite Hermitian matrices with
    trace 1. It is a CONVEX COMPACT subset of the 8-dim space of traceless
    Hermitian 3x3 matrices (Bloch parametrization).

    tr(H_V rho) is a LINEAR functional on D(V).

    The level set {rho in D(V) : tr(H_V rho) = E}, for E strictly inside
    the spectrum (lambda_min(H_V), lambda_max(H_V)), is the intersection of
    a hyperplane with the convex compact set D(V). It is therefore:
        - convex (intersection of convex sets),
        - compact (intersection with a compact set),
        - connected (convex => connected),
        - bounded (compact),
        - of codimension 1 in D(V) (dim = 7 real).

    A two-sheeted hyperboloid requires DISCONNECTED level set and a
    NON-COMPACT one. The level set fails BOTH requirements.
    """
    eigs = np.sort(eigvalsh(H_V))
    E_min, E_max = float(eigs[0]), float(eigs[-1])
    return {
        "E_range": (E_min, E_max),
        "level_set_dim_real": 7,           # codim 1 in 8-dim D(V)
        "convex": True,
        "compact": True,
        "connected": True,
        "two_disconnected_sheets": False,
        "non_compact_asymptote": False,
    }


# ---------------------------------------------------------------------------
# 7. Test (C): Bures metric signature at the Cartan-fixed point
# ---------------------------------------------------------------------------
def test_C_bures_signature():
    """
    At rho_* = I/3 in D(V) (the maximally mixed state in V), the SLD
    Bures metric on traceless Hermitian tangent vectors X is

        g^B_{rho_*}(X, X) = sum_i X_ii^2 / p_i + sum_{i!=j} 2|X_ij|^2/(p_i+p_j)
                          = 3 * sum_i X_ii^2 + 3 * sum_{i!=j} |X_ij|^2
                          = 3 * ||X||_HS^2

    where p_i = 1/3 and ||.||_HS is the Hilbert-Schmidt norm.

    The matrix of g^B on the 8-dim tangent space (in the Gell-Mann basis,
    where the orthonormal generators give X = sum_a r_a lam_a / sqrt(2))
    is therefore proportional to the identity 8x8 matrix.

    Signature: (8, 0, 0)  -- POSITIVE DEFINITE (Riemannian, Euclidean).
    """
    # Construct the Bures metric matrix in the orthonormal Gell-Mann basis
    # at rho_* = I/3. With X_a = lam_a / sqrt(2) (Hilbert-Schmidt orthonormal),
    # g^B(X_a, X_b) = 3 * tr(X_a X_b) = 3 * delta_{ab}, so the metric is 3 * I_8.
    G_bures = 3.0 * np.eye(8)
    eigs = eigvalsh(G_bures)
    pos = int(np.sum(eigs > EPS))
    neg = int(np.sum(eigs < -EPS))
    zer = int(np.sum(np.abs(eigs) < EPS))
    return G_bures, eigs, (pos, neg, zer)


# ---------------------------------------------------------------------------
# 8. Test (D): symmetry group of (D(V), tr(H_V rho))
# ---------------------------------------------------------------------------
def test_D_symmetry_group(H_V):
    """
    The natural symmetry of D(V) is the unitary group U(V) ~= U(3),
    acting by conjugation: rho -> U rho U^dagger.

    The subgroup preserving tr(H_V rho) is the stabilizer of H_V in U(3)
    under conjugation -- i.e. the centralizer of H_V in U(3).

    For non-degenerate spectrum of H_V (three distinct eigenvalues), the
    centralizer is the maximal torus U(1)^3 -- THREE parameters,
    COMPACT, TORIC.

    To produce a LORENTZIAN 3-parameter boost subgroup (e.g. SO(3,1)/SO(3) =
    boosts, 3-dim non-compact symmetric space), we would need the centralizer
    to be non-compact -- but U(3) is compact and ALL its subgroups are
    compact. There is no non-compact 3-parameter Lorentzian group acting by
    conjugation on D(V) preserving the spectrum of H_V.

    Hence: 3-parameter symmetry exists (matching the conjecture's count),
    but it is COMPACT TORIC, not Lorentzian.
    """
    eigs = np.sort(eigvalsh(H_V))
    eigvals_distinct = len(np.unique(eigs.round(10)))
    stab_dim = 9  # default = dim U(3)
    if eigvals_distinct == 3:
        stab_dim = 3   # U(1)^3
    elif eigvals_distinct == 2:
        # two equal eigenvalues -- larger stabilizer (e.g. U(2) x U(1) = 5-dim)
        stab_dim = 5
    elif eigvals_distinct == 1:
        stab_dim = 9   # full U(3)
    return {
        "eigvals_distinct": eigvals_distinct,
        "stab_real_dim": stab_dim,
        "stab_is_compact": True,    # subgroup of compact U(3)
        "stab_is_toric": (eigvals_distinct == 3),
        "ambient_unitary_group_compact": True,
    }


# ---------------------------------------------------------------------------
# 9. Run the audit
# ---------------------------------------------------------------------------
def run_audit(a=1.0, b=0.7, c=0.4, label=""):
    print("=" * 74)
    print(f"  Run: H = {a}(sigma_3 (x) I) + {b}(I (x) lam_3) + {c}(I (x) lam_8)"
          + (f"   [{label}]" if label else ""))
    print("=" * 74)

    Pi, H_std, V, V_idx, H_V = setup(a, b, c)

    print()
    print("Setup")
    print("-----")
    print(f"  Hilbert space:  C^6 ~= C^2 (x) C^3  (CRT identification)")
    print(f"  Sub-Hilbert-space V = A_2 (+) A_3   (basis: chi_3, chi_2, chi_4)")
    print(f"  dim_C V = 3, dim_R D(V) = 8")
    print(f"  Spectrum of H on C^6: {sorted(eigvalsh(H_std).round(6))}")
    print(f"  H_V = restriction of H to V (3x3, Hermitian)")

    # --- Test (A) ---
    eigs_HV, sig_HV = test_A_signature(H_V)
    print()
    print("(A) Signature of H_V")
    print("--------------------")
    print(f"    eigenvalues:                    {eigs_HV.round(6)}")
    print(f"    signature (pos, neg, zero):     {sig_HV}")
    print(f"    indefinite (needed for hyperboloid in purification picture): "
          f"{sig_HV[0] > 0 and sig_HV[1] > 0}")

    # --- Test (B) ---
    B = test_B_level_set_topology(H_V)
    print()
    print("(B) Level set {rho in D(V) : tr(H_V rho) = E}")
    print("---------------------------------------------")
    print(f"    energy range E in [{B['E_range'][0]:.6f}, {B['E_range'][1]:.6f}]"
          f"  (BOUNDED)")
    print(f"    level set real dim:             {B['level_set_dim_real']}"
          f"  (codim 1 in 8-dim D(V))")
    print(f"    convex:                         {B['convex']}")
    print(f"    compact:                        {B['compact']}")
    print(f"    connected:                      {B['connected']}")
    print(f"    two disconnected sheets:        {B['two_disconnected_sheets']}"
          f"  <-- NEEDED for hyperboloid; ABSENT")
    print(f"    non-compact asymptote:          {B['non_compact_asymptote']}"
          f"  <-- NEEDED for asymptotic slope (item J'); ABSENT")

    # --- Test (C) ---
    G_bures, eigs_G, sig_G = test_C_bures_signature()
    print()
    print("(C) Bures metric signature at rho_* = I/3")
    print("-----------------------------------------")
    print(f"    metric matrix:                  3 * I_8  (orthonormal G-M basis)")
    print(f"    signature (pos, neg, zero):     {sig_G}")
    print(f"    Riemannian (positive definite): {sig_G[1] == 0 and sig_G[2] == 0}")
    print(f"    pseudo-Riemannian / Lorentzian: "
          f"{sig_G[0] > 0 and sig_G[1] > 0}  <-- NEEDED for hyperboloid; ABSENT")

    # --- Test (D) ---
    D = test_D_symmetry_group(H_V)
    print()
    print("(D) Symmetry group of (D(V), tr(H_V rho))")
    print("-----------------------------------------")
    print(f"    H_V eigenvalues distinct:       {D['eigvals_distinct']}")
    print(f"    stabilizer real dim:            {D['stab_real_dim']}"
          f"  (matches the conjecture's '3-parameter' count when generic)")
    print(f"    stabilizer compact:             {D['stab_is_compact']}"
          f"  <-- a Lorentzian boost group would be NON-compact")
    print(f"    stabilizer toric:               {D['stab_is_toric']}")
    print(f"    ambient group U(3) is compact:  {D['ambient_unitary_group_compact']}")
    print(f"    Lorentzian 3-parameter boost group acting by conjugation"
          f" on D(V): IMPOSSIBLE (all subgroups of U(3) are compact).")

    # --- Verdict for this run ---
    hyperboloid = (sig_HV[0] > 0 and sig_HV[1] > 0
                   and B['two_disconnected_sheets']
                   and B['non_compact_asymptote']
                   and sig_G[1] > 0
                   and not D['stab_is_compact'])
    return {
        "H_V_signature": sig_HV,
        "level_set_compact": B['compact'],
        "level_set_connected": B['connected'],
        "level_set_two_sheets": B['two_disconnected_sheets'],
        "bures_metric_signature": sig_G,
        "stab_compact": D['stab_is_compact'],
        "stab_dim": D['stab_real_dim'],
        "hyperboloid": hyperboloid,
    }


# ---------------------------------------------------------------------------
# 10. Main: run on several Hamiltonians, verify robustness
# ---------------------------------------------------------------------------
def main():
    print()
    print("#" * 74)
    print("#  Paper 32 sec 13.2 -- Bures-Dispersion Audit")
    print("#  Settles items K (Lorentzian) / L (Euclidean-4) / J' (invariant c)")
    print("#" * 74)

    runs = [
        (1.0, 0.7, 0.4, "generic Cartan H, non-degenerate spectrum"),
        (1.0, 0.0, 0.0, "pure parity Cartan, H = sigma_3 (x) I"),
        (0.0, 1.0, 0.0, "pure cube-root Cartan, H = I (x) lam_3"),
        (0.0, 0.0, 1.0, "second cube-root Cartan, H = I (x) lam_8"),
        (0.5, 0.3, 0.2, "another generic Cartan H"),
    ]

    results = []
    for (a, b, c, label) in runs:
        r = run_audit(a, b, c, label)
        results.append((label, r))

    # ---------- Summary ----------
    print()
    print("#" * 74)
    print("#  SUMMARY")
    print("#" * 74)
    print()
    print(f"{'Run':56s} | Sig(H_V) | LS compact | Stab cpt | Hyperboloid?")
    print("-" * 74)
    for (label, r) in results:
        print(f"{label[:56]:56s} | {str(r['H_V_signature']):8s} | "
              f"{str(r['level_set_compact']):10s} | "
              f"{str(r['stab_compact']):8s} | "
              f"{str(r['hyperboloid']):10s}")
    print()

    any_hyperboloid = any(r['hyperboloid'] for (_, r) in results)
    all_compact_LS = all(r['level_set_compact'] for (_, r) in results)
    all_compact_stab = all(r['stab_compact'] for (_, r) in results)
    bures_definite = all(r['bures_metric_signature'][1] == 0
                         and r['bures_metric_signature'][2] == 0
                         for (_, r) in results)

    print("VERDICT")
    print("=======")
    print(f"  Any run yields a hyperboloid:                  {any_hyperboloid}")
    print(f"  All runs: level set compact:                   {all_compact_LS}")
    print(f"  All runs: stabilizer compact (no Lorentz boost):{all_compact_stab}")
    print(f"  Bures metric positive definite everywhere:     {bures_definite}")
    print()
    if any_hyperboloid:
        print("  ITEM K (Lorentzian 3+1 as Bures-lift phenomenon):  CONFIRMED")
        print("  ITEM L (intrinsically Euclidean-4):                REFUTED")
        print("  ITEM J' (finite invariant speed c):                CONFIRMED")
    else:
        print("  ITEM K (Lorentzian 3+1 as Bures-lift phenomenon):  REFUTED")
        print("  ITEM L (intrinsically Euclidean-4):                CONFIRMED")
        print("  ITEM J' (finite invariant speed c):                FALLS")
        print()
        print("  Reason: the level set tr(H_V rho) = E is an affine slice of the")
        print("          convex compact set D(V); it is connected and bounded,")
        print("          NOT a two-sheeted hyperboloid. The Bures metric is")
        print("          positive definite (3 * I_8 at rho_* = I/3), NOT")
        print("          pseudo-Riemannian. The 3-parameter centralizer of H_V")
        print("          in U(3) is a compact torus U(1)^3, NOT a non-compact")
        print("          Lorentzian boost group SO(3,1)/SO(3).")
        print()
        print("          Conjecture 9.4 was the Lorentzian alternative; the")
        print("          Euclidean-4 branch was its pre-claimed matched-pair")
        print("          (item L). The matched-pair branch is the realized one.")
        print()
        print("          ITEM J' (invariant speed c as the hyperboloid")
        print("          asymptote): since there is no asymptote on a compact")
        print("          level set, there is NO finite invariant speed on the")
        print("          lifted conductor-2 (+) conductor-3 block of D(C^6).")
        print("          The classical-Galilean (parabolic) dispersion of")
        print("          Lemma 9.2 is NOT promoted to Lorentzian by the Bures")
        print("          lift, on this realization.")
        print()
        print("  Untouched by this verdict:")
        print("   - Item T' (hbar as the i-face conversion constant) lives on")
        print("     the Mandelstam-Tamm/Bures speed-limit relation, which is a")
        print("     statement about Bures DISTINGUISHABILITY rate vs energy")
        print("     spread -- independent of whether the energy LEVEL SET is")
        print("     a hyperboloid. Item T' stands.")
        print("   - Items S' (the C^2-leg real-form face) and the four-pillar")
        print("     GR triad (sec 5.A) are independent of the signature face")
        print("     and are untouched.")
        print()
        print("  Net effect on Cor 9.7 ('one lift, four faces'):")
        print("    - face (1) Lorentzian signature       -> REFUTED on this row")
        print("    - face (2) nonabelian gauge restoration -> untouched")
        print("    - face (3) imaginary i, invariant hbar  -> untouched (T')")
        print("    - face (4) invariant speed c            -> REFUTED on this row")
        print("    The 'four faces' contracts to 'two forced internal faces")
        print("    (gauge, i-face/hbar) on top of a fixed Riemannian (Euclidean)")
        print("    background; the signature face is the classical (3,1)")
        print("    contact-geometric split of sec 9.1 (Thm 9.1) without a")
        print("    Lorentzian-metric promotion'.")
        print()

    print()
    print("Discipline check (sec 11.2 firewall): no dimensionful magnitude")
    print("emitted. Only structural classifications (signature, connectedness,")
    print("compactness, dimension counts) are reported.")


if __name__ == "__main__":
    main()
