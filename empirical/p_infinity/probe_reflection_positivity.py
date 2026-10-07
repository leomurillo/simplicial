"""
P-infinity sec.5 -- THE ARITHMETIC ENERGY CONDITION AS REFLECTION POSITIVITY (Osterwalder-Schrader).

Dictionary (Euclidean QFT -> arithmetic):
  Euclidean time         = the scaling/log variable (multiplicative R_+, the dilation flow's time)
  time reflection theta  = the functional equation s<->1-s  (= Frobenius <-> Verschiebung F<->F^vee=q/F,
                           the Rosati involution; = the metric's time-reflection isometry, P-inf sec1.3)
  two-point function     = the Weil explicit-formula / apex intersection kernel
  OS reflection pairing  = <theta f, f> = the Weil quadratic form W(f)
  RH                     = Weil positivity W(f)>=0  =  OS REFLECTION POSITIVITY of the arithmetic theory
  OS reconstruction      = the de Branges/prolate Lorentzian side (H_space = dB space of E_B=Xi+iXi',
                           Hamiltonian = W_lambda = -S^2+V >=0, spectrum = the zeros, H>=0 = zeros real = RH)

Concrete exact model (genus g=1): the TRANSFER MATRIX is Frobenius F (one scaling step); its OS
reflection form on Z[F] = <1,F,F^2,...,F^n> is the ROSATI form
        H[j,k] = Tr( F^j (F^vee)^k ) = alpha^j beta^k + beta^j alpha^k,   beta = F^vee = q/alpha,
the reflected pairing <theta F^k, F^j>. REFLECTION POSITIVITY = H is PSD. Theorem (certified exact):
        H PSD  <=>  beta = conj(alpha)  <=>  |alpha| = sqrt q  <=>  RH-over-F_q.
Over F_q this PSD is the Rosati positivity (a THEOREM, the geometric energy condition); over Q the same
OS positivity of the explicit-formula theory is the open arch-domination = RH, and constructive QFT
proves RP via a POSITIVE TRANSFER MATRIX / positive Boltzmann weight -- the new target.

EXACT (sympy Z[i]/Q; signature via charpoly+Descartes). No torch.
"""
import sympy as sp

def signature(Mat):
    n = Mat.shape[0]; lam = sp.symbols('lam')
    coeffs = sp.expand(Mat.charpoly(lam).as_expr())
    coeffs = sp.Poly(coeffs, lam).all_coeffs()
    nz = 0
    while coeffs and coeffs[-1] == 0:
        nz += 1; coeffs = coeffs[:-1]
    def sc(seq):
        s = [c for c in seq if c != 0]
        return sum(1 for i in range(len(s)-1) if s[i]*s[i+1] < 0)
    npl = sc(coeffs); nmi = sc([c*(-1)**i for i, c in enumerate(coeffs)])
    assert npl+nmi+nz == n, (npl,nz,nmi,n)
    return npl, nz, nmi

def OS_reflection_form(alpha, beta, n):
    """H[j,k] = alpha^j beta^k + beta^j alpha^k  (Rosati/OS reflection pairing on 1,F,...,F^n)."""
    return sp.Matrix(n+1, n+1, lambda j, k: sp.expand(alpha**j*beta**k + beta**j*alpha**k))

print("="*86)
print("REFLECTION POSITIVITY of the Frobenius transfer  <=>  RH-over-F_q  (genus 1, exact)")
print("="*86)
I = sp.I
cases = [
    ("on-circle  alpha=2i, beta=-2i   (q=4, |alpha|=2=sqrt4)", 2*I, -2*I, 4),
    ("on-circle  alpha=1+2i,beta=1-2i  (q=5, |alpha|=sqrt5)",  1+2*I, 1-2*I, 5),
    ("OFF-circle alpha=4, beta=1       (q=4, real, |alpha|=4)", sp.Integer(4), sp.Integer(1), 4),
    ("OFF-circle alpha=5, beta=1       (q=5, real, |alpha|=5)", sp.Integer(5), sp.Integer(1), 5),
]
n = 5
for name, al, be, q in cases:
    assert sp.simplify(al*be - q) == 0, "FE pairing alpha*beta=q must hold"
    H = OS_reflection_form(al, be, n)
    sg = signature(H)
    psd = (sg[2] == 0)
    oncirc = (sp.simplify(be - sp.conjugate(al)) == 0)
    print(f"  {name}")
    print(f"      OS reflection form H (size {n+1}) signature {sg}  ->  RP (PSD): {psd}   "
          f"|alpha|=sqrt q: {oncirc}   => {'RH' if psd else 'RH VIOLATED'}")
print("""
  THEOREM [P]: the OS reflection form H[j,k]=Tr(F^j (F^vee)^k) is positive semi-definite
  <=> beta=conj(alpha) <=> |alpha|=sqrt q <=> RH-over-F_q. PSD = REFLECTION POSITIVITY of the Frobenius
  transfer matrix; on the circle H = v v* + conj(v v*) (sum of a rank-1 PSD and its conjugate, PSD);
  off the circle H = u 1^T + 1 u^T-type rank-2 INDEFINITE (signature (1,1) on the {alpha,beta} plane).""")

print("="*86)
print("THE OS RECONSTRUCTION (structural): RP  =>  the Lorentzian/unitary de Branges side")
print("="*86)
print("""  Osterwalder-Schrader: REFLECTION POSITIVITY of a Euclidean theory  =>  a Hilbert space (GNS over
  the RP pairing), a self-adjoint Hamiltonian H>=0 generating the Euclidean-time contraction semigroup
  e^{-tH}, and Lorentzian (unitary, positive-energy) correlations by analytic continuation. In the
  arithmetic theory the reconstructed object IS the program's Lorentzian side:
     RP pairing <theta f,f>=W(f)  --GNS-->  de Branges space of E_B = Xi + i Xi'
     Euclidean-time generator      =  the prolate/scaling operator W_lambda = -S^2 + V  (sec.4)
     spectrum(H)                   =  the nontrivial zeros
     H >= 0 (positive energy)      =  zeros real  =  RH
     m_B = -Xi'/Xi Herglotz        =  OS positivity in spectral (Nevanlinna) form
  So the program's Euclidean side (Weil form / explicit formula / Connes scaling site) and its
  Lorentzian side (de Branges / prolate / zeros) are the two ends of ONE OS reconstruction, and
  reflection positivity is the exact bridge = the arithmetic energy condition.""")

print("="*86)
print("WHAT RP IMPORTS (honest)")
print("="*86)
print("""  As a relabeling, 'RH = reflection positivity' is Weil positivity (= RH, no gain). Its VALUE is the
  constructive-QFT TOOLBOX for PROVING RP, none of which is a monotone:
    (i)  POSITIVE TRANSFER MATRIX / positive Boltzmann weight in a lattice approximation -> RP by the
         Markov/transfer argument. Arithmetic transfer = the scaling step; over F_q = Frobenius F, whose
         RP is the Rosati positivity (THEOREM, certified above). Over Q = the scaling-site Boltzmann
         weight (the prime/conductor measure); its positivity is the open arch-domination = RH.
    (ii) GAUSSIAN DOMINATION / chessboard estimates;  (iii) correlation inequalities (Griffiths/FKG).
  TARGET [C]=RH: realize the arithmetic explicit-formula theory as the continuum limit of a lattice
  theory with a POSITIVE transfer matrix / Boltzmann weight (the scaling site as a reflection-positive
  statistical system). This converts 'prove the marginal Weil positivity' into 'exhibit a positive
  arithmetic transfer matrix' -- a pointwise positivity constructive QFT has tools for, distinct from
  the exhausted heat-flow monotones. Over F_q the transfer (Frobenius) is positive for free; over Q the
  positivity must be manufactured at the archimedean place (the OS reflection axis).""")
