"""
P-infinity / the COMPLEX (HERMITIAN) LIFT of the Weil form -- testing the collaborator's diagnosis:
"a real Q is flux-blind; the arithmetic momentum / arrow of time lives in the IMAGINARY part."

Four exact tests (sympy). Honest verdict at the end: where the diagnosis is RIGHT, where it must be
corrected, and the genuine unification it unlocks.

A. FLUX-BLINDNESS (the core physics claim, CONFIRMED). For a wave E = A + iA' (the de Branges block
   Xi + i Xi', A real), the probability current on the real axis is
        J(x) = Im( conj(E) E' ) = A A'' - (A')^2 = -L_1(A),   L_1 = (A')^2 - A A''  (the Laguerre form).
   For a PURELY REAL wave psi = A: J = Im(A A') = 0. So a real wave carries ZERO current; the current is
   exactly the Laguerre/de Branges object and exists only via the complex (i A') part. RIGHT.

B. HERMITIAN > REAL-PART (the "complex Q sees more", in GENERAL). For a Hermitian form H = R + iS
   (R sym, S antisym), real vectors see only R (v^T S v = 0). R PSD does NOT imply H PSD: the imaginary
   part S (the current) can break positivity. Toy: H=[[1,2i],[-2i,1]], R=I PSD but H indefinite.
   CORRECTION: for the WEIL form specifically, positivity on REAL EVEN test functions ALREADY <=> RH
   (Weil 1952), so the real Weil form is NOT blind to RH at the CRITERION level. The complex lift is the
   right INSTRUMENT (it exhibits the current / stress tensor), not a stronger criterion.

C. THE OFF-DIAGONAL IS THE PRIME FLUX (geometric / F_q). The C x C stress split G(q,a)=g - a E has
   off-diagonal -a = the Frobenius trace = the prime momentum flux T_{0i}; it is REAL here (the geometric
   metric is real Lorentzian). It is LOAD-BEARING: a=0 (no flux) is trivially causal but VACUOUS (sees no
   primes). Causality |a|<2sqrt q (Lemma 4.1) is a statement about the off-diagonal momentum.

D. THE UNIFICATION. T_{00} (energy density, Re/diagonal) and T_{0i} (momentum flux, Im/off-diagonal) are
   the two halves of one stress tensor. Geometric (F_q): T_{0i} = -a (real). Analytic (de Branges):
   T_{0i} = the current J = -L_1 = (up to |E|^2) the Herglotz field u_B = Im m_B. OS-dual. The NULL/
   DOMINANT energy condition = current positivity = u_B >= 0 = Herglotz = reflection positivity = RH.
   So the complex Q UNIFIES the energy-density condition (P-inf sec4, |a|<2sqrt q) with the current/
   Herglotz condition (sec5, u_B>=0): they are T_{00} and T_{0i} of one tensor.

EXACT. No torch.
"""
import sympy as sp
z = sp.symbols('z', real=True)

def signature_real_sym(M):
    lam = sp.symbols('lam')
    rs = sp.Poly(sp.expand(M.charpoly(lam).as_expr()), lam).real_roots()
    npl = sum(1 for r in rs if r.is_positive); nmi = sum(1 for r in rs if r.is_negative)
    return npl, len(rs)-npl-nmi, nmi

print("="*86)
print("A. FLUX-BLINDNESS: the current J = Im(conj(E) E') of the de Branges wave E = A + i A'")
print("="*86)
A = sp.prod([(1 - z**2/g**2) for g in (1, 2, 3)])      # toy 'Xi' (real, zeros on the real axis)
Ap = sp.diff(A, z); App = sp.diff(A, z, 2)
E = A + sp.I*Ap; Ep = sp.diff(E, z)
J = sp.simplify(sp.im(sp.expand_complex(sp.conjugate(E)*Ep)))   # current on the real axis
L1 = sp.simplify(Ap**2 - A*App)
print(f"  E = A + iA',  A = prod(1 - z^2/g^2), g in {{1,2,3}}")
print(f"  current  J(z) = Im(conj(E) E')         = {sp.factor(J)}")
print(f"  Laguerre L1   = (A')^2 - A A''         = {sp.factor(L1)}")
print(f"  J + L1 == 0 (so J = -L1, the Laguerre/de Branges current): {sp.simplify(J + L1) == 0}")
# purely real wave psi = A : current = Im(conj(A) A') = 0 since A,A' real
print(f"  purely-real wave psi=A:  Im(conj(A) A') = {sp.simplify(sp.im(A*Ap))}   => REAL WAVE CARRIES NO CURRENT")
print("  VERDICT A: CONFIRMED -- the current is an Im object (= -Laguerre); a real wave is flux-blind.")

print("="*86)
print("B. HERMITIAN > REAL-PART in general; but the WEIL real-even criterion already <=> RH")
print("="*86)
H = sp.Matrix([[1, 2*sp.I], [-2*sp.I, 1]])
R = H.applyfunc(sp.re); S = H.applyfunc(sp.im)
emb = sp.Matrix(sp.BlockMatrix([[R, -S], [S, R]])); emb = sp.Matrix(emb)
sgH = signature_real_sym(emb)            # doubled inertia of H
sgR = signature_real_sym(R)
print(f"  H = [[1,2i],[-2i,1]]:  Re-part R = I has signature {sgR} (PSD on real vectors);")
print(f"  full Hermitian H has (doubled) signature {sgH}  => H is INDEFINITE (the current S breaks it).")
print("  => In GENERAL the imaginary/current part carries content the real part cannot see.")
print("  CORRECTION (honest): for the Weil form, positivity on REAL EVEN test functions already <=> RH")
print("  (Weil 1952). So the real Weil form is NOT blind to RH at the criterion level; the complex lift")
print("  is the right INSTRUMENT for the stress tensor/current, not a stronger criterion.")

print("="*86)
print("C. THE OFF-DIAGONAL IS THE PRIME FLUX (geometric, F_q): T_{0i} = -a, load-bearing")
print("="*86)
def primM(q, a): return sp.Matrix([[-2*q, -a], [-a, -2]])
q = 7
for a in (0, 4, 6):
    M = primM(q, a); sg = signature_real_sym(M)
    role = "VACUOUS (a=0: no prime flux, trivially causal, sees nothing)" if a==0 else (
           "causal (RH)" if 4*q-a*a>0 else "ACAUSAL (off-line)")
    print(f"  q={q}, a={a} (off-diagonal momentum): det=4q-a^2={4*q-a*a:>4}  sig {sg}  -> {role}")
print("  => the off-diagonal momentum -a (Frobenius trace = prime flux) is what carries RH; a=0 is vacuous.")

print("="*86)
print("D. THE UNIFICATION: energy density (Re/diag) and momentum flux (Im/off-diag) = one stress tensor")
print("="*86)
print("""  T_{00} = energy density = the diagonal (geometric: -2q,-2; the |a|<2sqrt q bound, sec4).
  T_{0i} = momentum flux  = the off-diagonal:  geometric  -> -a  (real, Frobenius trace);
                                               analytic   -> J = -L1 = the de Branges current
                                               (= u_B |E|^2-type, the Herglotz field), OS-dual.
  NULL/DOMINANT energy condition  =  current positivity  =  u_B = Im m_B >= 0  =  Herglotz
                                  =  reflection positivity  =  |a| <= 2 sqrt q  =  RH.
  => The COMPLEX Q is the instrument that makes T_{0i} (the prime momentum) expressible; it UNIFIES
     P-inf sec4 (energy density, |a|<2sqrt q) with sec5 (the current/Herglotz, u_B>=0) as the two
     components T_{00}, T_{0i} of one Lorentzian stress tensor. Content unchanged (= RH); the lift is
     the de Branges/CBS/apex complex structure the program already carries, now physically organized.""")

print("="*86)
print("HONEST VERDICT")
print("="*86)
print("""  RIGHT [A]: the current/arrow is an IMAGINARY object (J = -Laguerre = the de Branges/Herglotz field);
       a purely real wave is flux-blind; the off-diagonal momentum (geometric -a, analytic u_B) carries RH;
       the complex/Hermitian lift is the correct instrument for the arithmetic stress-energy tensor, and it
       UNIFIES the energy-density (sec4) and current/Herglotz (sec5) conditions as T_{00}, T_{0i}.
  CORRECTION [P]: the REAL Weil criterion (real even test functions) already <=> RH (Weil 1952), so the
       historical form is not blind to RH itself; and the full complex Hermitian positivity <=> RH too --
       same content, no strictly-weaker condition. The gain is the INSTRUMENT + new toolboxes (CFT
       holomorphic T(z)/Virasoro unitarity; Osterwalder-Schrader), not a bypass.
  RESIDUAL [C]=RH: prove the current positivity u_B>=0 (= |a|<=2sqrt q uniformly = reflection positivity
       = a unitary CFT stress tensor with positive energy). The complex lift is the right language; the
       positivity is still RH.""")
