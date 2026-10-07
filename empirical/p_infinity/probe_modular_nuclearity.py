"""
P-infinity / companion note Pinf-A, Section 8 -- THE MODULAR LANGUAGE (Tomita-Takesaki) AND WHY IT
DOES NOT BUY POSITIVITY.   *** STUB / SPEC -- NOT YET A CLOSED CERTIFICATE ***

Section 8 recasts RH a FOURTH way (after OS reflection positivity Sec.3, canonical-Hamiltonian
H(t)>=0 Sec.3.3, and SUSY H={Q,Q*} Sec.7): in the modular theory of the standard subspace of the
half-scaling-time of H(E_B). The thesis of Sec.8 -- which THIS probe is scoped to make falsifiable on
the finite Sec.5 model -- is NEGATIVE and structural:

  (8.2 FIREWALL)  The modular Hamiltonian K = -log Delta is KMS-symmetric (J K J = -K), hence
                  unbounded BOTH ways; it is NOT the OS Hamiltonian H_OS >= 0.  Positive energy
                  cannot be read off Delta.   PREDICTION: spec(K) is symmetric about 0 in BOTH the
                  on-line and off-line models (it sees the functional-equation pairing, not RH).

  (8.3 ARROW)     Borchers/Bisognano-Wichmann/Wiesbrock: positivity ==> geometric modular covariance
                  Delta^{it} U(s) Delta^{-it} = U(e^{-2 pi t} s),  NOT the reverse.  The Borchers
                  relation is the FIFTH equivalent face of RH.
                  *** CORRECTION (Prop 8.3a, certified in probe_modular_borchers_obstruction.py): the
                  Borchers residual does NOT vanish on finite ON-LINE models -- it CANNOT, because
                  [log Delta, P] = 2 pi i P has no nonzero finite-dim Hermitian solution (the ax+b
                  group has no finite unitary rep; obstruction quantized at 2 pi).  So there is NO
                  finite Borchers discriminant of RH at all; the earlier 'R==0 on-line' prediction was
                  FALSE.  The fifth face is intrinsically infinite-dimensional.  See that probe. ***

  (8.4 CIRCULARITY)  Tomita-Takesaki is FREE: every standard subspace yields (Delta, J)
                  unconditionally (Rieffel-van Daele).  By the Faltings-Hriljac guillotine a free
                  structure cannot decide RH.  PREDICTION: (Delta, J) are constructible identically
                  for on-line AND off-line models -- their mere EXISTENCE separates nothing; only the
                  Borchers covariance (8.3) does.

  (8.6 FRONT-END)  The one non-tautological handle: modular nuclearity / split (Buchholz-Wichmann).
                  OPEN QUESTION this probe is meant to pressure: is the finite nuclearity norm
                  ||U(s) e^{-beta K}||_1 bounded by phase-space/heat-kernel data WITHOUT assuming
                  H_OS >= 0 ?  If finiteness silently needs positivity, 8.6 collapses into 8.4.

Model (identical to probe_os_reconstruction.py, so kappa lines up):
  ordinates g_k;  A(z) = prod_k (1 - z^2/g_k^2)  ("Xi", real even);  E = A + i A';  m = -A'/A.
  on-line  : g real            -> RH-consistent (kappa = 0).
  off-line : a conjugate pair   -> off-line zeros (kappa = #such pairs).

No torch. Exact arithmetic where computed (sympy). The modular operator of the finite standard
subspace, the Borchers test, and the nuclearity norm are SCOPED BELOW with their exact formulas and
left as TODO -- this file is the Section 8 spec, deliberately not a green certificate.
"""
import sympy as sp

z = sp.symbols('z')

# ---------------------------------------------------------------------------
# Computable now (exact): the finite de Branges model and its Krein-Langer index,
# reused verbatim from probe_os_reconstruction.py so the two certificates share kappa.
# ---------------------------------------------------------------------------

# Krein-Langer index machinery: imported verbatim from the CERTIFIED companion
# probe_os_reconstruction.py so the two probes share the SAME kappa (sample-dependent lower bound).

def _real(e):
    return sp.nsimplify(sp.re(sp.expand_complex(sp.nsimplify(e))))


def signature_real_sym(M):
    lam = sp.symbols('lam')
    rs = sp.Poly(sp.expand(M.charpoly(lam).as_expr()), lam).real_roots()
    npos = sum(1 for r in rs if r.is_positive)
    nneg = sum(1 for r in rs if r.is_negative)
    return npos, len(rs) - npos - nneg, nneg


def hermitian_signature(P):
    """inertia (n+,n0,n-) of a Hermitian sympy matrix; Jacobi minors, real-embedding fallback."""
    n = P.shape[0]
    S = P.applyfunc(lambda e: sp.im(sp.expand_complex(sp.nsimplify(e))))
    if all(S[i, j] == 0 for i in range(n) for j in range(n)):
        return signature_real_sym(P.applyfunc(_real))
    D = [sp.Integer(1)] + [_real(P[:k, :k].det()) for k in range(1, n + 1)]
    if all(d != 0 for d in D):
        signs = [1 if d > 0 else -1 for d in D]
        nneg = sum(1 for i in range(n) if signs[i] * signs[i + 1] < 0)
        return n - nneg, 0, nneg
    R = P.applyfunc(_real)
    M = sp.Matrix(sp.BlockMatrix([[R, -S], [S, R]]))
    p, zz, m = signature_real_sym(sp.Matrix(M))
    return p // 2, zz // 2, m // 2


# four C+ points avoiding all model zeros (Im in {0,+-1,+-1/2}); identical to the certified probe
SAMPLES = [sp.Rational(1, 3) + 2 * sp.I / 3, sp.Rational(5, 4) + 2 * sp.I / 3,
           sp.Rational(11, 5) + 2 * sp.I / 3, sp.Rational(1, 3) + 7 * sp.I / 4]


def model(gs):
    """A(z)=prod(1 - z^2/g^2) ('Xi'), E=A+iA', m=-A'/A. gs may contain conjugate pairs (off-line)."""
    A = sp.expand(sp.prod([1 - z**2 / g**2 for g in gs]))
    Ap = sp.diff(A, z)
    return {'A': A, 'Ap': Ap, 'E': A + sp.I * Ap, 'm': -Ap / A, 'gs': gs}


def pick_negative_index(m, pts):
    """Krein-Langer index (sample-dependent lower bound): #neg eigenvalues of the Nevanlinna-Pick
    matrix P[i,j] = (m(w_i) - m(conj w_j))/(w_i - conj w_j) on pts in C+."""
    n = len(pts)
    P = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            wi, wjc = pts[i], sp.conjugate(pts[j])
            P[i, j] = sp.simplify((m.subs(z, wi) - m.subs(z, wjc)) / (wi - wjc))
    return hermitian_signature(P)[2]


# ---------------------------------------------------------------------------
# SCOPED / TODO -- the Section 8 content proper.  Formulas given; left unimplemented on purpose.
# ---------------------------------------------------------------------------

def standard_subspace_modular(model_dict):
    """TODO (8.1/8.4).  Build the closed real subspace V of H(E_B) = the half-scaling-time data,
    theta-reflected (theta = the functional equation s<->1-s).  Then the Tomita operator
        S_V (xi + i eta) = xi - i eta,   xi, eta in V,
    polar-decomposes as S_V = J Delta^{1/2}.  On the finite model H(E) is finite-dimensional
    (reproducing kernel K(w,z) = [B(z)A*(w)-A(z)B*(w)] / (pi (z - wbar)) with B=A'); realify and
    use the Rieffel-van Daele angle-operator formula for (Delta, J) of a standard real subspace.
    Return (Delta, J) as exact matrices.

    PREDICTION (8.4): constructs identically for on-line and off-line -> EXISTENCE separates nothing.
    """
    raise NotImplementedError("8.1/8.4: finite standard-subspace modular operator -- spec only")


def modular_hamiltonian_spectrum(Delta):
    """TODO (8.2 FIREWALL).  K = -log Delta.  Assert spec(K) is SYMMETRIC about 0 (J K J = -K) in
    BOTH models -> K is not H_OS>=0.  This is the certificate that the modular Hamiltonian sees the
    FE pairing, never the zero positivity."""
    raise NotImplementedError("8.2: modular Hamiltonian symmetry -- spec only")


def borchers_residual(*_):
    """SUPERSEDED by Prop 8.3a (probe_modular_borchers_obstruction.py).  There is NO finite Borchers
    residual discriminant: [log Delta, P] = 2 pi i P forces P = 0 in finite dimension, so the relation
    cannot even approximately hold on a finite model (least singular value of the constraint = 2 pi).
    The Borchers face is intrinsically infinite-dimensional; do not look for it here."""
    raise NotImplementedError("8.3: superseded by the ax+b obstruction -- see the obstruction probe")


def modular_nuclearity_norm(Delta, U, beta, s):
    """TODO (8.6 FRONT-END, the only non-tautological handle).  Trace (nuclear) norm
        Theta(beta,s) = || U(s) e^{-beta K} ||_1     (Buchholz-Wichmann).
    OPEN: is Theta finite from phase-space/heat-kernel data WITHOUT assuming H_OS>=0?
    If finiteness requires positivity, 8.6 collapses into the 8.4 circularity.  This function is
    the experimental front-end where that question becomes a number."""
    raise NotImplementedError("8.6: modular nuclearity norm -- the open analytic front-end")


if __name__ == "__main__":
    print(__doc__.strip().splitlines()[0])
    print("=" * 78)
    print("Section 8 STUB: computable now = the finite model + Krein-Langer index kappa.")
    print("The modular operator / Borchers residual / nuclearity norm are scoped TODO (see funcs).")
    print("-" * 78)

    # the same three models / sample points as probe_os_reconstruction.py Sec.5 (kappa lines up)
    cases = {
        "on-line  g={1,2,3}":       [sp.Integer(1), sp.Integer(2), sp.Integer(3)],
        "off-line g={1,2+/-i}":     [sp.Integer(1), 2 + sp.I, 2 - sp.I],
        "off-line g={3+/-i/2,1,2}": [3 + sp.I / 2, 3 - sp.I / 2, sp.Integer(1), sp.Integer(2)],
    }
    for name, gs in cases.items():
        kappa = pick_negative_index(model(gs)['m'], SAMPLES)
        verdict = "RH-consistent" if kappa == 0 else f"off-line DETECTED (kappa>={kappa})"
        print(f"  {name:26s}  Krein-Langer neg-index kappa>={kappa}  [{verdict}]")
    print("  (NB Sec.5 honest point: the 4-pt Pick UNDER-detects g={3+/-i/2,1,2} -- the Hankel face")
    print("   catches it; kappa here is a sample-dependent LOWER bound, exactly as in Sec.5.)")
    print("  *** No finite Borchers/modular discriminant exists (Prop 8.3a) -- see")
    print("      probe_modular_borchers_obstruction.py.  kappa above is the Pick/Hankel witness, NOT")
    print("      a modular one.  The only modular handle is the infinite-dim nuclearity front-end. ***")
    print("-" * 78)
    print("OPEN (8.6): is ||U(s) e^{-beta K}||_1 finite WITHOUT assuming H_OS>=0 ?  -> the lever.")
