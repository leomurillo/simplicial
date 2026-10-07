"""
P-infinity sec.4 -- THE ARITHMETIC ENERGY CONDITION (the new instrument).

Physics analogy made precise: in general relativity a light cone stays causal NOT because of a
monotone but because matter satisfies a pointwise ENERGY CONDITION (null/weak/dominant). The program
proved there is no heat-flow monotone for Lambda<=0 (only Lambda>=0; Rodgers-Tao one-sided). So the
replacement instrument is an ARITHMETIC ENERGY CONDITION: a pointwise positivity on the prime
correction ("matter") against the archimedean intersection metric ("geometry") that forces the
primitive cone spacelike WITHOUT a backward flow.

We make the IMPLICATION exact and non-circular:
   (energy condition |a| <= 2 sqrt q)  ==>  (primitive cone spacelike = causal = RH-over-F_q-finite),
and we exhibit the energy condition as a DOMINANT-ENERGY bound (prime flux <= geometric capacity),
two-faced: the C x C primitive intersection form M is NEG-definite and the Rosati form R is POS-definite,
flipping at the SAME boundary |a|=2 sqrt q. Over F_q the energy condition is a THEOREM (Hodge/Rosati
positivity on a genuine surface = the geometric energy condition); over Q it is the open arch-domination.

EXACT (sympy Z/Q; signature via charpoly+Descartes = Sylvester-invariant). No torch.
"""
import sympy as sp

def signature(Mat):
    n = Mat.shape[0]; lam = sp.symbols('lam')
    coeffs = Mat.charpoly(lam).all_coeffs()
    nz = 0
    while coeffs and coeffs[-1] == 0:
        nz += 1; coeffs = coeffs[:-1]
    def sc(seq):
        s = [c for c in seq if c != 0]
        return sum(1 for i in range(len(s)-1) if s[i]*s[i+1] < 0)
    npl = sc(coeffs); nmi = sc([c*(-1)**i for i, c in enumerate(coeffs)])
    assert npl+nmi+nz == n
    return npl, nz, nmi

def Gram_CxC(q, a, g=1):
    D2 = 2-2*g; GF2 = q*(2-2*g)
    return sp.Matrix([[0,1,1,q],[1,0,1,1],[1,1,D2,q+1-a],[q,1,q+1-a,GF2]])
def primitive_M(q, a, g=1):
    return sp.Matrix([[-2*g*q,-a],[-a,-2*g]])
def rosati_R(q, a):
    # Rosati/Weil positive form on End^0(E)=<1,F>: G_Ros=[[2,a],[a,2q]] (N7); pos-def <=> 4q-a^2>0.
    return sp.Matrix([[2,a],[a,2*q]])

print("="*88)
print("PART A - THE IMPLICATION LEMMA (exact): energy bound <=> causal primitive cone")
print("="*88)
print("  Background g := G(q, a=0) (the 'vacuum' Lorentzian metric); stress -a*E adds the prime flux a")
print("  (only the Lefschetz entry Gamma_F.Delta=q+1-a depends on a; E=e3 e4^T+e4 e3^T).")
q = 13
g0 = Gram_CxC(q, 0)
E = sp.zeros(4); E[2,3] = E[3,2] = 1
print(f"  q={q}: sig(background g)={signature(g0)} (Lorentzian).  Check G(q,a)=g - a*E:")
ok = (Gram_CxC(q, 7) == g0 - 7*E)
print(f"    G(q,a) = g - a*E  identity holds: {ok}")
print(f"  {'a':>4} {'4q-a^2':>8} {'M sig':>9} {'cone':>10} {'EC |a|<2sqrt q?':>16} {'implication':>14}")
import math
bound = 2*math.sqrt(q)
for a in range(0, 9):
    M = primitive_M(q, a); sM = signature(M); det = 4*q-a*a
    cone = "spacelike" if sM==(0,0,2) else ("null" if det==0 else "indefinite")
    ec = a < bound
    causal = (sM == (0,0,2))
    implic = "EC <=> causal" if (ec == causal or det==0) else "MISMATCH"
    print(f"  {a:>4} {det:>8} {str(sM):>9} {cone:>10} {str(ec):>16} {implic:>14}")
print(f"""  LEMMA [P]: for the Lorentzian background, (energy condition |a| < 2sqrt q = {bound:.3f})
  <=> (primitive Gram M negative-definite) <=> (primitive cone spacelike = causal). The prime flux a
  is the 'matter'; 2sqrt q is the 'speed-of-light' geometric capacity. This is the exact, non-circular
  half: energy condition ==> causality ==> RH-over-F_q-finite. (n-dim generalization in sec.3: the
  energy bound is the spectral-radius-<1 condition on g^{{-1}}T restricted to the spacelike sheet.)""")

print("="*88)
print("PART B - THE ENERGY CONDITION IS TWO-FACED (intersection neg-def AND Rosati pos-def, same flip)")
print("="*88)
print(f"  {'q':>4} {'a':>4} {'det=4q-a^2':>11} {'M (C x C) neg-def?':>18} {'R (Rosati) pos-def?':>19} {'EC':>5}")
for (q, a) in [(7,4),(7,5),(7,6),(9,5),(9,6),(9,7),(25,9),(25,10),(25,11)]:
    M = primitive_M(q,a); R = rosati_R(q,a)
    mneg = signature(M)==(0,0,2); rpos = signature(R)==(2,0,0); det = 4*q-a*a
    ec = "OK" if det>0 else ("bd" if det==0 else "VIOL")
    print(f"  {q:>4} {a:>4} {det:>11} {str(mneg):>18} {str(rpos):>19} {ec:>5}")
print("""  Both faces flip at exactly |a|=2sqrt q (det=4q-a^2=0): the C x C primitive intersection form M
  goes neg-def -> indefinite, the Rosati/Weil endomorphism form R goes pos-def -> indefinite. They are
  the two signs of ONE dominant energy condition |a|<=2sqrt q = arch-domination. Over F_q this is the
  Hodge/Rosati positivity on a genuine surface (the GEOMETRIC energy condition, a THEOREM). [P/F_q]""")

print("="*88)
print("PART C - THE OPERATOR d'ALEMBERTIAN (W_lambda = -S^2 + V; the source energy condition)")
print("="*88)
print("""  Connes-Consani-Moscovici W_lambda = -S^2 + 2 pi lambda^2 (4N+1) - 1/4 (arXiv:2310.18423):
    -S^2   : S = self-adjoint dilation generator (scaling-TIME momentum) => -S^2 is the d'ALEMBERTIAN
             of scaling-time (the 1-D wave operator box_t). Its symbol is Lorentzian (one time sign).
    +V     : V = 2 pi lambda^2 (4N+1) >= 0, a CONFINING potential (cures the xp continuous-spectrum
             disease; harmonic in the polynomial grading N).
  Reading: the polarization 'W_lambda >= 0' (which, if ASSERTED, is RH-equivalent) is the statement
  that the wave operator box_t + V has no negative modes given the arithmetic SOURCE (the prime/von
  Mangoldt term). In a wave equation box phi = J, positivity of the energy follows from an ENERGY
  CONDITION on the source J (reflection positivity / unitarity), not from a monotone. THE NEW TARGET:
  derive W_lambda >= 0 from an arithmetic NULL ENERGY CONDITION on the prime source -- the arithmetic
  analog of reflection positivity / the Rosati positivity (a THEOREM over F_q). [C] = RH.""")

print("="*88)
print("SUMMARY")
print("="*88)
print("""  [P] IMPLICATION LEMMA (Part A): energy condition |a|<=2sqrt q <=> causal primitive cone. Exact,
      non-circular -- the arithmetic Raychaudhuri/focusing step.
  [P/F_q] the energy condition is two-faced and is, over F_q, the Hodge/Rosati positivity = a THEOREM
      (the geometric energy condition holds automatically on a genuine surface) (Part B).
  [A] the operator d'Alembertian: W_lambda = box_t (scaling-time wave op) + confining V; the polarization
      is a SOURCE energy condition, not a monotone (Part C).
  [C] = RH: prove the arithmetic energy condition over Q (the prime source satisfies the null/dominant
      energy bound |a|<=2sqrt q at every scale = arch-domination), via reflection-positivity/unitarity
      of the underlying scaling field theory -- a new toolbox, distinct from the dead heat-flow monotones.""")
