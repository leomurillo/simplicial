"""
PARANOID AUDIT of Vector A/B: is J = B - B^T really the chiral / arrow-of-time content,
or did we over-read a phase-BLIND object?

The worry: B_{ck} = |U_{kc}|^2 is built from the MODULUS of U only. Hence J = B - B^T is a
function of |U|^2 alone -- it discards arg(U). But the chiral / L(.,chi_3) content of the program
lives in PHASES. Two independent sanity checks:

  CHK1  state-independence.  J is a fixed property of U (no state). The arrow / chiral current of
        a coarse-graining must VANISH at the self-dual vacuum (equilibrium has no arrow). We compute
        the genuine state-dependent chiral current of the archimedean state in the character frame,
              C(rho) = Im( rho_chi ),   rho_chi = U diag(p) U^dagger,
        for (i) the vacuum p = uniform and (ii) a non-uniform state. If C(vacuum)=0 while ||J||>0,
        then J -- being nonzero independent of state -- CANNOT be the arrow/chiral current.

  CHK2  gauge / phase sensitivity.  Rephase the characters chi_c -> e^{i beta_c} chi_c (a legitimate
        basis phase freedom). Then |U|^2 is unchanged, so B and J are unchanged; but the genuine
        chiral current Im(rho_chi) changes. A phase-blind object cannot be the phase content.

If both fire, the Vector A/B identification "J = the chiral L(.,chi_3) channel" is an OVERREACH and
must be corrected: J is a real, true structural asymmetry of |U|^2 (odd under c->-c), but it is NOT
the RH-bearing chiral phase, and its flux-sign is NOT established to equal c_2<0 / L(1/2,chi_3).

No torch. numpy. Deterministic (fixed nonuniform state; fixed phases).
"""
import numpy as np

def apex_unitary(N):
    w = np.exp(2j * np.pi / N)
    k = np.arange(1, N).reshape(-1, 1); c = np.arange(1, N).reshape(1, -1)
    R = 1.0 / np.sqrt(N * k * (k + 1))
    return R * (1 - (k + 1) * w ** (k * c) + k * w ** ((k + 1) * c)) / (1 - w ** c)

def rho_chi(U, p):
    # U has rows=Helmert k, cols=char c.  e_k -> column? We need rho in CHARACTER basis.
    # |e_k> in char basis = column? (U)_{kc} = <chi_c, e_k>; so e_k = sum_c conj(U_{kc}) chi_c.
    # rho = sum_k p_k |e_k><e_k|  =>  (rho_chi)_{c c'} = sum_k p_k conj(U_{kc}) U_{kc'}.
    return np.einsum('k,kc,kd->cd', p, np.conj(U), U)

for (N, label) in ((7, "prime p=7"), (6, "primorial N=6")):
    U = apex_unitary(N)
    B = (np.abs(U) ** 2).T
    J = B - B.T
    nJ = np.linalg.norm(J)

    # CHK1
    p_vac = np.ones(N - 1) / (N - 1)
    p_non = np.arange(1, N, dtype=float); p_non /= p_non.sum()
    C_vac = np.linalg.norm(rho_chi(U, p_vac).imag)
    C_non = np.linalg.norm(rho_chi(U, p_non).imag)

    # CHK2  rephase characters by fixed phases
    rng_phases = np.array([np.cos(j) for j in range(1, N)])  # deterministic "random-ish" phases
    Q = np.exp(1j * rng_phases)                # per-character phase
    U2 = U * Q[np.newaxis, :]                   # rephase columns (characters)
    B2 = (np.abs(U2) ** 2).T
    J2 = B2 - B2.T
    dJ = np.linalg.norm(J2 - J)                 # should be ~0 (J phase-blind)
    C_non_2 = np.linalg.norm(rho_chi(U2, p_non).imag)
    dC = abs(C_non_2 - C_non)                   # genuine chiral current DOES change under rephasing

    print(f"\n=== {label} (N={N}) ===")
    print(f"  ||J = B - B^T||                         = {nJ:.6f}   (state-INDEPENDENT property of |U|^2)")
    print(f"  CHK1  genuine chiral current ||Im rho_chi||:")
    print(f"          vacuum (uniform p)              = {C_vac:.3e}   <- MUST be ~0 (no arrow at equilibrium)")
    print(f"          non-uniform state              = {C_non:.6f}   <- nonzero, STATE-DEPENDENT")
    print(f"        => J nonzero on the vacuum while the true arrow vanishes there: J is NOT the arrow.")
    print(f"  CHK2  rephase characters chi_c -> e^(i b_c) chi_c:")
    print(f"          change in J                     = {dJ:.3e}   <- ~0: J is phase-BLIND (uses |U|^2)")
    print(f"          change in genuine chiral current= {dC:.6f}   <- nonzero: the chiral content IS phase")

print("""
========================================================================================
VERDICT.  J = B - B^T is a TRUE structural fact (|U|^2 is transpose-asymmetric, odd under
c->-c), but it is PHASE-BLIND and STATE-INDEPENDENT, so it is NOT the chiral / arrow /
L(.,chi_3) content -- that content is a state-dependent PHASE (Berry/Bargmann) object that
vanishes on the self-dual vacuum.  The Vector A/B claim "J = the chiral channel, its flux-sign
= c_2<0 = L(1/2,chi_3)" is an OVERREACH and must be corrected in N14 sec 7.5.
========================================================================================
""")
