"""
probe_rosati_gram_positivity.py  --  the intersection positivity, in its cleanest instance, mapped to Q.

Opportunity: construct the Hodge-index / C x C positivity over Q from the apex's (now complete) local
Frobenius data. The positivity over Q IS RH, so this is NOT a proof; it builds the exact TEMPLATE and
localizes the missing object -- and it closes back to the session's opening problem ("prove the Hermitian
Gram carries no negative squares").

THE CLEANEST INSTANCE (elliptic curve / Rosati). For E/F_q the geometric Frobenius F acts on H^1 (Tate
module) with F F^vee = q (F^vee = dual isogeny = the Rosati conjugate). On End^0(E) = Q(alpha) (imaginary
quadratic under RH) the ROSATI FORM <phi,psi> = Tr(phi * psi^vee) is, by Weil's theorem (the polarization
/ intersection positivity on the abelian variety), POSITIVE-DEFINITE. The Gram matrix of {1, F} is
        G = [[<1,1>, <1,F>],[<F,1>, <F,F>]] = [[2, a],[a, 2q]],   a = tr F = a_p.
Weil's positivity FORCES G to be PSD, i.e. det G = 4q - a^2 >= 0, i.e. |a| <= 2 sqrt q, i.e. |alpha|=sqrt q
-- the Riemann Hypothesis over F_q. So: RH(F_q) = "the Rosati Gram has no negative squares", and the
positivity that supplies it is Weil's geometric (Hodge-index) theorem.

THIS IS THE PROGRAM'S OPENING PROBLEM. The session began with "prove the Hermitian Gram carries no
negative squares off the real axis." Over F_q that Gram is exactly G=[[2,a],[a,2q]], PSD by Rosati/Weil.
Over Q the analogue is the (infinite) Weil-Pick Gram of the apex; its PSD-ness is RH.

THE MAP TO Q (honest):
  - apex edge operator (A-I)Phi (N4/N5)   <->  F (the substitute Frobenius; local data complete, opp. ii)
  - functional equation xi(s)=xi(1-s)     <->  the Rosati duality F <-> F^vee, F F^vee = q
  - the Weil / Pick / Bures-Poisson form   <->  the Rosati form Tr(phi psi^vee)
  - RH = the Gram PSD = the form positive   <->  Weil's positivity (geometric over F_q; OPEN over Q)
The apex supplies F and the Gram STRUCTURE; the missing piece is the POSITIVITY of the form -- which over
F_q is a THEOREM (geometry) and over Q is the open RH (= arch-domination = Connes' Weil positivity =
the cubic-chirality / missing-eigenvalue candidate, c_2<0, L(1/2,chi3)>0).

sympy + numpy. No torch.
"""
import numpy as np
import sympy as sp
import math

def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
def ap_elliptic(p, A, B):
    return -sum(legendre(x**3 + A*x + B, p) for x in range(p))

print("=" * 92)
print("(1) THE TEMPLATE: the Rosati Gram G=[[2,a],[a,2q]] is PSD  <=>  RH over F_q; Weil's positivity forces it")
print("=" * 92)
A, B = 1, 1
print(f"  E: y^2 = x^3 + {A}x + {B};  F = Frobenius on H^1, a = tr F = a_p, F F^vee = q")
print(f"  {'p':>4} {'a_p':>5} {'Rosati Gram [[2,a],[a,2q]]':>28} {'det=4q-a^2':>11} {'eigs>=0 (PSD)?':>15} {'=RH?':>6}")
for p in (11, 13, 17, 19, 23, 29):
    a = ap_elliptic(p, A, B)
    G = np.array([[2.0, a], [a, 2.0*p]])
    det = 4*p - a*a
    eigs = np.linalg.eigvalsh(G)
    psd = bool(np.all(eigs >= -1e-9))
    rh = abs(a) <= 2*math.sqrt(p)
    print(f"  {p:>4} {a:>5} {'[[2,'+str(a)+'],['+str(a)+','+str(2*p)+']]':>28} {det:>11} {str(psd):>15} {str(rh):>6}")
print("  => det G = 4q - a^2 >= 0  <=>  |a|<=2 sqrt q  <=>  |alpha|=sqrt q  <=>  RH over F_q. Weil's theorem")
print("     (the polarization / Hodge-index positivity of End^0(E)) makes the Rosati form positive-definite,")
print("     hence G PSD: 'the Gram carries no negative squares' -- a THEOREM here, supplied by the geometry.")

print("\n" + "=" * 92)
print("(2) this IS the session's opening problem; over Q it is the (infinite) Weil-Pick Gram of the apex")
print("=" * 92)
print("""  The program opened with: 'prove the Hermitian Gram carries no negative squares off the real axis'
  (= the Pick matrix P of m=-Xi'/Xi is PSD = RH). Over F_q that Gram is exactly G=[[2,a],[a,2q]], and it
  is PSD by the Rosati/Weil positivity. So the opening problem is, structurally, the number-field
  instance of the function-field Hodge-index positivity: the apex's Weil-Pick / Bures-Poisson Gram must
  carry no negative squares -- the same statement, in infinite dimension, without the geometry to force it.""")

print("\n" + "=" * 92)
print("(3) THE MAP, and the one missing object (honest)")
print("=" * 92)
print(f"  {'function-field (F_q), THEOREM':>40}   {'number-field (Q), via the apex':>34}")
rows = [
 ("Frobenius F on H^1", "apex edge operator (A-I)Phi  [N4/N5]"),
 ("F F^vee = q (Poincare duality)", "functional eq. xi(s)=xi(1-s)"),
 ("local Frobenius eigenvalues |alpha|=sqrt q", "Gauss/Jacobi sums |.|=sqrt q  [opp. ii]"),
 ("Frobenius lift alpha->alpha^n", "Hasse-Davenport = (-1)^n transfer [N5/ii]"),
 ("Rosati form Tr(phi psi^vee)", "Weil / Pick / Bures-Poisson form"),
 ("ROSATI POSITIVITY (geometry)  *PROVEN*", "Gram PSD = arch-domination  *OPEN = RH*"),
]
for L, R in rows:
    print(f"  {L:>40} <-> {R:>34}")
print("""  The apex now supplies EVERY local piece (operator, |.|=sqrt q skeleton, Hasse-Davenport lift) and the
  Gram STRUCTURE. The SINGLE missing object is the POSITIVITY of the Weil-Pick form -- the analogue of
  Weil's geometric (Hodge-index) theorem. Over F_q it is proven from the polarization of the abelian
  variety; over Q there is no variety, so it is the open RH. Its program-internal candidate is the cubic
  chirality c_2 < 0 (L(1/2,chi3)=0.4808>0), = Connes' missing simple+even lowest eigenvalue (sec 6.6a).""")

print("\n" + "=" * 92)
print("VERDICT  --  the positivity, templated and localized (honest; NOT a proof)")
print("=" * 92)
print("""  ACHIEVED: the intersection positivity is now exhibited in its cleanest instance -- the Rosati Gram
  G=[[2,a],[a,2q]], PSD <=> RH over F_q, made PSD by Weil's geometric positivity -- and mapped to Q,
  where it is exactly the program's opening problem ('the Hermitian Gram carries no negative squares').
  The apex supplies F, the local sqrt q eigenvalue skeleton, the Hasse-Davenport lift, and the Gram
  structure; the SINGLE remaining object is the POSITIVITY of the (infinite) Weil-Pick Gram.
  HONEST STATUS: that positivity IS RH. Over F_q it is a theorem because there is a variety with a
  polarization (Hodge index / Rosati); over Q there is no variety, and supplying the positivity by other
  means -- Connes' scaling-site / C x C analogue, with the cubic-chirality c_2<0 as the candidate missing
  eigenvalue -- is the open Riemann Hypothesis. NO proof. What is delivered: the target is now a SINGLE,
  geometric, fully-templated object (a positive form making one explicit Gram PSD), with every local
  ingredient in hand and the function-field theorem as the exact blueprint. The arc closes where it
  opened, now with the missing piece named, localized, and shown to be the Weil/Hodge positivity itself.""")
