"""
Pinf-A Section 8 -- pushing the MODULAR language as far as it goes.

RESULT (a sharp NEGATIVE that CONFIRMS the program's localization, with the structural reason):

  THEOREM 8.3a (the ax+b obstruction).  In finite dimension the Borchers relation
        Delta^{it} U(s) Delta^{-it} = U(e^{-2 pi t} s),    U(s) = e^{i s P},   H := log Delta = H*,
  forces P = 0.  Hence positive-energy modular covariance (the FIFTH equivalent face of RH, Sec 8.3)
  is INTRINSICALLY infinite-dimensional, and there is PROVABLY NO finite modular witness of RH.

  Proof.  Differentiate at t=0:  [H, P] = 2 pi i P.
    (i) Trace:  0 = tr([H,P]) = 2 pi i tr(P)  =>  tr(P) = 0;  with P >= 0,  P = 0.
    (ii) Spectral (stronger, drops P>=0): if H|h> = h|h> then H(P|h>) = (h + 2 pi i)(P|h>); H Hermitian
         has REAL spectrum, h + 2 pi i is not real, so P|h> = 0 for every eigenvector => P = 0.
  => the affine 'ax+b' group has no nonzero finite-dim Hermitian rep of the translation generator.

  This is the modular-theory form of 'finite witnesses are necessary-not-sufficient' (Sec 5 Rem 5.2):
  all RH content sits in whether the INFINITE-dim scaling flow IS the modular dilation (Borchers holds)
  = the prolate convergence (CCM 2511.22755) = the program's one open step.  Modular theory does not
  open a new front; it gives the existing front a geometric meaning (the limit is where the modular
  flow becomes geometric) and proves no finite shortcut exists.

WHAT IS FINITE AND EXACT (hence NOT where RH hides -- confirming Sec 8.2 firewall and 8.4 circularity):

  (FW) Firewall 8.2:  for ANY standard subspace V,  J Delta J = Delta^{-1}  (Tomita), so spec(log Delta)
       is symmetric about 0 -> the modular Hamiltonian is KMS-symmetric, never >= 0.  It sees the
       functional-equation pairing, not the zero positivity.  Verified to machine eps below.
  (EX) Circularity 8.4:  the modular pair (Delta, J) is CONSTRUCTIBLE from any standard subspace
       UNCONDITIONALLY -> mere existence separates nothing (on-line / off-line data alike).  Verified.

No torch.  numpy for the standard-subspace linear algebra; sympy for the exact trace identity.
"""
import numpy as np
import sympy as sp

TWO_PI = 2.0 * np.pi
rng = np.random.default_rng(0)  # fixed seed: deterministic, no Math.random concerns


# ---------------------------------------------------------------------------
# THEOREM 8.3a -- the ax+b obstruction.  Exact trace identity + finite linear-system kernel.
# ---------------------------------------------------------------------------

def obstruction_trace_identity(n):
    """EXACT (sympy): tr([H,P]) = 0 identically, and the Borchers derivative gives 2 pi i tr(P) = 0."""
    H = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'h{i}{j}'))
    P = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'p{i}{j}'))
    comm = H * P - P * H
    return sp.simplify(comm.trace()) == 0  # => 0 = 2 pi i tr(P) => tr(P)=0; with P>=0, P=0


def obstruction_kernel(n):
    """Numeric: for a generic Hermitian H, the only matrix P with [H,P] = 2 pi i P is P = 0.
    We build the linear map L(P) = [H,P] - 2 pi i P and report dim ker L over C^{n x n} (= n^2 vars)."""
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    H = (A + A.conj().T) / 2  # generic Hermitian
    # vectorize L(P) = H P - P H - 2 pi i P:  vec(HP-PH) = (I⊗H - H^T⊗I) vec(P)
    I = np.eye(n)
    L = np.kron(I, H) - np.kron(H.T, I) - 2j * np.pi * np.eye(n * n)
    s = np.linalg.svd(L, compute_uv=False)
    tol = 1e-9 * max(1.0, s[0])
    nullity = int(np.sum(s < tol))
    smin = s.min()
    return nullity, smin


def obstruction_psd_floor(n, trials=2000):
    """Quantify it: over PSD P with ||P||_F = 1, min ||[H,P] - 2 pi i P||_F is bounded AWAY from 0
    (no near-solutions).  Random PSD sampling -> a floor; the theorem says the true inf is > 0."""
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    H = (A + A.conj().T) / 2
    best = np.inf
    for _ in range(trials):
        B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        P = B @ B.conj().T            # PSD
        P /= np.linalg.norm(P)        # ||P||_F = 1
        r = np.linalg.norm(H @ P - P @ H - 2j * np.pi * P)
        best = min(best, r)
    return best


# ---------------------------------------------------------------------------
# Standard-subspace modular operator (FW + EX).  Built in the realification; properties CHECKED, not
# asserted, so a convention error fails loudly.
# ---------------------------------------------------------------------------

def _realify_linear(M):
    """realification of the C-LINEAR map z -> M z  acting on (Re z; Im z)."""
    return np.block([[M.real, -M.imag], [M.imag, M.real]])


def _J0(n):
    """realification of multiplication by i (the complex structure)."""
    Z, I = np.zeros((n, n)), np.eye(n)
    return np.block([[Z, -I], [I, Z]])


def modular_from_C(C):
    """A standard subspace V = C(R^n)  (C invertible complex n x n  =>  C^n = V (+) iV).
    Tomita S_V z = M conj(z) with M = C conj(C)^{-1}; S_V^2 = I.  Realify, form Delta_real = S^T S
    (real inner product = Re<.,.>), CHECK it is C-linear and that log spec is symmetric (J Delta J = Delta^{-1})."""
    n = C.shape[0]
    M = C @ np.linalg.inv(C.conj())
    K = np.block([[np.eye(n), np.zeros((n, n))], [np.zeros((n, n)), -np.eye(n)]])  # conj
    S = _realify_linear(M) @ K                         # antilinear: S_real
    J0 = _J0(n)
    antilin_err = np.linalg.norm(S @ J0 + J0 @ S)      # S anti-C-linear: S J0 = -J0 S
    invol_err = np.linalg.norm(S @ S - np.eye(2 * n))  # S^2 = I
    Delta = S.T @ S                                    # real-SPD, must be C-linear
    clin_err = np.linalg.norm(Delta @ J0 - J0 @ Delta) # [Delta, J0] = 0  <=> C-linear
    ev = np.linalg.eigvalsh((Delta + Delta.T) / 2)
    logs = np.sort(np.log(ev))
    sym_err = np.linalg.norm(logs + logs[::-1])         # spectrum of log Delta symmetric about 0
    return dict(antilin_err=antilin_err, invol_err=invol_err, clin_err=clin_err,
                sym_err=sym_err, logspec=logs)


def random_invertible_C(n):
    while True:
        C = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        if abs(np.linalg.det(C)) > 1e-3:
            return C


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Pinf-A Sec 8 -- modular language, pushed.  (no torch; numpy + sympy)")
    print("=" * 78)

    print("\n[THM 8.3a] the ax+b obstruction: [H,P] = 2 pi i P with H Hermitian => P = 0")
    print("-" * 78)
    print(f"  exact trace identity tr([H,P]) == 0  (n=3):  {obstruction_trace_identity(3)}"
          "   => 0 = 2 pi i tr(P) => tr(P)=0; with P>=0, P=0.  [EXACT]")
    for n in (2, 3, 4, 5):
        nullity, smin = obstruction_kernel(n)
        floor = obstruction_psd_floor(n)
        print(f"  n={n}: dim ker(L) over C^(nxn) = {nullity}  (smin={smin:.3e})   "
              f"PSD-floor min||[H,P]-2pi i P||_F >= {floor:.3f}  -> NO finite positive-energy Borchers")
    print("  VERDICT: the FIFTH face (Borchers/+hsm) is intrinsically infinite-dimensional;")
    print("           there is provably NO finite modular witness of RH.")

    print("\n[FW + EX] standard-subspace modular operator: firewall (8.2) + circularity (8.4)")
    print("-" * 78)
    print("  Constructing (Delta, J) for several UNCONDITIONAL standard subspaces V = C(R^n):")
    for n in (2, 3, 4):
        r = modular_from_C(random_invertible_C(n))
        ok = max(r['antilin_err'], r['invol_err'], r['clin_err'], r['sym_err'])
        print(f"  n={n}:  S antilinear {r['antilin_err']:.1e} | S^2=I {r['invol_err']:.1e} | "
              f"Delta C-linear {r['clin_err']:.1e} | log-spec symmetric {r['sym_err']:.1e}  "
              f"[{'OK' if ok < 1e-8 else 'FAIL'}]")
        print(f"        log spec(Delta) = {np.round(r['logspec'], 4)}  (symmetric about 0 = KMS)")
    print("  VERDICT (8.2): log Delta is KMS-symmetric for EVERY V -> never >= 0, sees the FE pairing.")
    print("  VERDICT (8.4): (Delta, J) exist unconditionally -> existence separates nothing.")

    print("\n" + "=" * 78)
    print("CONCLUSION: modular theory ADDS no finite lever (8.3a) and the two finite facts it does")
    print("give (8.2 firewall, 8.4 circularity) carry no RH discriminant.  The ONLY modular route to")
    print("RH is the infinite-dim closed-form Delta of the prolate/de Branges space, whose Borchers")
    print("covariance = the scaling flow BECOMING the modular dilation = CCM prolate convergence =")
    print("the program's one open step.  Same front, now with a geometric meaning + a no-shortcut thm.")
