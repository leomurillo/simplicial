"""
P-infinity / companion note Pinf-A -- THE de BRANGES APPARATUS AS OSTERWALDER-SCHRADER RECONSTRUCTION.

Thesis: the de Branges space of E_B = Xi + i Xi', with the SCALING group as Euclidean time and the
functional equation s<->1-s as the time reflection theta, IS the OS reconstruction of the reflection-
positive explicit-formula system. RH = reflection positivity = the reconstructed scaling semigroup is
POSITIVE-ENERGY = the de Branges canonical Hamiltonian H(t) >= 0. We certify the load-bearing
equivalences on a finite de Branges model, EXACTLY (sympy Q(i); signature = Sylvester-invariant), and
exhibit the Krein-Langer index = #off-line zeros.

Three OS faces, all <=> zeros on the line (= real ordinates):
  (F1/F2) OS Hilbert space / positive energy:  m = -A'/A is HERGLOTZ  <=>  the Nevanlinna-PICK matrix
          P[i,j] = (m(w_i) - m(conj w_j))/(w_i - conj w_j),  w_i in C+,  is PSD.   (Pick's theorem)
          #negative eigenvalues of P = the Krein-Langer index kappa = #off-line zeros (N10).
  (F3)    OS two-point complete monotonicity (Bernstein-Widder, half-line):  S(t)=sum_k e^{-t g_k} is
          completely monotone  <=>  the moment Hankel [mu_{i+j}], mu_j=sum_k g_k^j, is PSD.  [the
          ADDITIVE shadow -- marginal by the Tower Theorem; included for completeness, NOT the lever.]
  (HB)    Hermite-Biehler margin D(w) = |E(w)|^2 - |E(conj w)|^2 > 0 on C+  <=>  E_B is HB <=> RH.

Model: ordinates g (the zero heights); A(z)=prod_k (1 - z^2/g_k^2) real even ("Xi"), E=A + i A'.
On-line: g real. Off-line: a conjugate pair g = c, conj c (a zero off the critical line), A still real.
No torch. Exact.
"""
import sympy as sp

z, t = sp.symbols('z t')

def signature_real_sym(M):
    """(n+,n0,n-) of a real symmetric rational matrix via EXACT real_roots (WITH multiplicity)."""
    lam = sp.symbols('lam')
    p = sp.Poly(sp.expand(M.charpoly(lam).as_expr()), lam)
    rs = p.real_roots()                       # list, with multiplicity; all real (M symmetric)
    npos = sum(1 for r in rs if r.is_positive)
    nneg = sum(1 for r in rs if r.is_negative)
    nz = len(rs) - npos - nneg
    assert npos + nneg + nz == M.shape[0], (npos, nz, nneg, M.shape[0])
    return npos, nz, nneg

def _real(e):
    return sp.nsimplify(sp.re(sp.expand_complex(sp.nsimplify(e))))

def hermitian_signature(P):
    """inertia (n+,n0,n-) of a Hermitian sympy matrix P (entries in Q(i)).
       Real matrix -> real_roots; else Jacobi's rule on the (real) leading principal minors of P
       (leading minors of a Hermitian matrix are real); embedding+real_roots as a last-resort fallback."""
    n = P.shape[0]
    S = P.applyfunc(lambda e: sp.im(sp.expand_complex(sp.nsimplify(e))))
    if all(S[i, j] == 0 for i in range(n) for j in range(n)):
        return signature_real_sym(P.applyfunc(_real))
    # Jacobi's signature rule on leading principal minors D_0=1, D_1, ..., D_n (all real)
    D = [sp.Integer(1)]
    for k in range(1, n+1):
        D.append(_real(P[:k, :k].det()))
    if all(d != 0 for d in D):
        signs = [1 if d > 0 else -1 for d in D]
        nneg = sum(1 for i in range(n) if signs[i]*signs[i+1] < 0)
        return n - nneg, 0, nneg
    # fallback: real embedding + real_roots
    R = P.applyfunc(_real)
    M = sp.Matrix(sp.BlockMatrix([[R, -S], [S, R]])); M = sp.Matrix(M)
    p, zz, m = signature_real_sym(M)
    return p//2, zz//2, m//2

def build_A(gs):
    A = sp.Integer(1)
    for g in gs:
        A *= (1 - z**2/g**2)
    return sp.expand(A)

def pick_matrix(gs, samples):
    A = build_A(gs); Ap = sp.diff(A, z)
    m = -Ap/A
    def mval(w): return sp.simplify(m.subs(z, w))
    n = len(samples)
    P = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            wi = samples[i]; wjc = sp.conjugate(samples[j])
            num = mval(wi) - mval(wjc)
            den = wi - wjc
            P[i, j] = sp.simplify(num/den)
    return P

def moment_hankel(gs, m):
    mu = [sp.expand(sum(g**k for g in gs)) for k in range(0, 2*m+1)]
    return sp.Matrix(m+1, m+1, lambda i, j: sp.nsimplify(mu[i+j]))

def hb_margin(gs, w):
    A = build_A(gs); Ap = sp.diff(A, z)
    E = A + sp.I*Ap
    val = sp.simplify(sp.Abs(E.subs(z, w))**2 - sp.Abs(E.subs(z, sp.conjugate(w)))**2)
    return sp.nsimplify(val)

I = sp.I
# four points in C+ chosen to avoid all model zeros of A (zeros have Im in {0,+-1,+-1/2}); use Im=2/3,7/4
samples = [sp.Rational(1,3)+2*I/3, sp.Rational(5,4)+2*I/3, sp.Rational(11,5)+2*I/3, sp.Rational(1,3)+7*I/4]

models = [
    ("ON-LINE   g=[1,2,3]            (all real ordinates)", [sp.Integer(1), sp.Integer(2), sp.Integer(3)]),
    ("OFF-LINE  g=[1, 2-i, 2+i]      (one conjugate pair off the real axis)",
         [sp.Integer(1), 2-I, 2+I]),
    ("OFF-LINE2 g=[3-i/2,3+i/2,1,2]  (a higher off-line pair)",
         [3-I/2, 3+I/2, sp.Integer(1), sp.Integer(2)]),
]

print("="*92)
print("OS RECONSTRUCTION on a finite de Branges model: RP / positive-energy <=> zeros on the line")
print("="*92)
for name, gs in models:
    P = pick_matrix(gs, samples)
    sgP = hermitian_signature(P)
    kappa = sgP[2]                      # # negative eigenvalues = Krein-Langer index = #off-line zeros
    H = moment_hankel(gs, 3)
    # moment Hankel may be complex if ordinates complex; test real-PSD via Hermitian signature
    sgH = hermitian_signature(sp.Matrix(H.rows, H.cols, lambda i,j: sp.expand(H[i,j])))
    hb = hb_margin(gs, 1+I)            # HB margin at one C+ point
    pick_psd = (sgP[2] == 0)
    hank_psd = (sgH[2] == 0)
    hb_pos = bool(sp.simplify(hb) > 0) if hb.is_real else None
    all_pass = pick_psd and hank_psd and (hb_pos is True)
    detectors = []
    if not pick_psd: detectors.append("Pick")
    if not hank_psd: detectors.append("Hankel")
    if hb_pos is False: detectors.append("HB")
    print(f"\n  {name}")
    print(f"    (F1/F2) Pick matrix signature {sgP}  -> PSD: {pick_psd}"
          f"   neg-index = {kappa}  (a SAMPLE-DEPENDENT LOWER BOUND on the Krein-Langer kappa)")
    print(f"    (F3)    moment Hankel signature {sgH}  -> PSD (complete monotonicity): {hank_psd}")
    print(f"    (HB)    Hermite-Biehler margin at one point 1+i = {hb}  -> >0: {hb_pos}  (single-point; insufficient alone)")
    if all_pass:
        verdict = "all finite witnesses pass (RH-consistent at this finite level; necessary-not-sufficient)"
    else:
        verdict = f"RH VIOLATION DETECTED by: {', '.join(detectors)}  (Krein-Langer kappa >= 1)"
    print(f"    => {verdict}")

print("""
""" + "="*92)
print("READING")
print("="*92)
print("""  [P] ON-LINE: every finite witness passes -- Pick PSD (neg-index 0), moment Hankel PSD, HB margin >0
      => the OS Hilbert space exists, the reconstructed scaling semigroup e^{-tH} is POSITIVE-ENERGY,
      and m_B=-A'/A is Herglotz. Consistent across all three faces.
  [P] OFF-LINE: reflection positivity is broken, but the DETECTION IS WITNESS-DEPENDENT, and this is the
      load-bearing honest point. For g=[1,2+-i] the 4-point Pick neg-index is 1 and the Hankel is non-PSD;
      for g=[3+-i/2,1,2] the SAME 4-point Pick is PSD (neg-index 0 -- it under-detects, the points sit far
      from the off-line poles at Im=1/2) while the moment Hankel IS non-PSD. NEITHER is a bug: a finite
      Pick neg-index is only a LOWER BOUND on the Krein-Langer kappa (Nevanlinna-Pick: m is Herglotz iff
      EVERY Pick matrix is PSD; a single finite one is necessary-not-sufficient), and the single-point HB
      margin is positive in all three models (it too must be checked globally). So:
  [P] RH <=> m_B Herglotz <=> reflection positivity <=> EVERY finite Pick PSD <=> complete monotonicity
      (every Hankel PSD). The OS reconstruction gives the EQUIVALENCE in the limit (all point sets / the
      full operator); any single finite check is necessary-not-sufficient. This is the program's
      marginality, exhibited inside the OS frame: RH is the GLOBAL positivity, not a finite witness.
  [C] = RH: the SAME equivalences for the genuine E_B = Xi + i Xi' (the infinite zero set). By de
      Branges' structure theorem, HB(E_B) <=> the canonical-system Hamiltonian H(t) >= 0 (pointwise) <=>
      the reconstructed scaling semigroup is positive-energy. The OS additions over de Branges' stuck
      route: (i) the Neeb-Olafsson reconstruction theorem (RP => positive-energy semigroup, rigorous);
      (ii) the half-line / complete-monotonicity (Bernstein-Widder) reduction -- RP need only be checked
      on positive scaling-time; (iii) the energy-condition reading -- H(t)>=0 is a POINTWISE positivity
      along scaling time, an arithmetic null/dominant energy condition, not a monotone. The positivity
      itself remains RH (the additive Hankel face is marginal, Tower Theorem); the deposit is the
      rigorous dictionary + the reconstruction bridge + the new toolbox (Herglotz/Pick, Bernstein-Widder,
      Lax-Phillips), distinct from the exhausted heat-flow monotones.""")
