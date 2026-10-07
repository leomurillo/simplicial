"""
probe_CxC_intersection_blueprint.py  --  OPEN RESEARCH: the C x C / scaling-site positivity, made
concrete as the geometric blueprint the number-field construction must replicate.

Over F_q the Weil positivity that forces |alpha|=sqrt q is read on the SURFACE S = C x C via the Hodge
index theorem (the intersection form is negative-definite on the primitive part of NS(S)). We compute
the blueprint exactly for an elliptic curve and exhibit the negative-definite primitive Gram whose
definiteness IS RH(F_q) -- the geometric ORIGIN of the Rosati Gram of N7 Rem 6.3.

Setup (genus 1; basis of NS(S) we use: h={pt}xC, v=Cx{pt}, Delta diagonal, Gamma_F Frobenius graph):
  h.h=0, v.v=0, h.v=1;  Delta.Delta = 2-2g = 0,  Delta.h=Delta.v=1;
  Gamma_F.h = 1,  Gamma_F.v = deg F = q,  Gamma_F.Delta = #C(F_q) = q+1-a,  Gamma_F.Gamma_F = q(2-2g)=0.
Decompose into hyperbolic <h,v> + primitive (orthogonal to h,v):
  Delta   = h + v + Delta_0,   Delta_0^2 = Delta.Delta - 2(h.v) = -2;
  Gamma_F = q h + v + Gamma_0,  Gamma_0^2 = Gamma_F.Gamma_F - 2q(h.v) = -2q;
  Gamma_0.Delta_0 = Gamma_F.Delta - (q+1) = -a.
The PRIMITIVE intersection Gram on {Gamma_0, Delta_0} is
        M = [[ -2q, -a ], [ -a, -2 ]].
Hodge index: M is NEGATIVE-DEFINITE  <=>  det M = 4q - a^2 > 0  <=>  |a| < 2 sqrt q  <=>  |alpha|=sqrt q
= RH over F_q. Weil's theorem = this negative-definiteness (a property of an actual surface). This is the
same content as the Rosati Gram [[2,a],[a,2q]] PSD (N7 Rem 6.3) -- here in its surface-geometry origin.

THE NUMBER-FIELD OBLIGATION (open = RH): construct, over Q, the analogue of S = C x C (the Connes
scaling-site square) with a primitive intersection form that is negative-definite, FED by the apex's
complete local data: Gamma_F <-> the Hasse-Davenport / (-1)^n Frobenius lift; Delta <-> the archimedean
edge operator + trivial part; M <-> the apex Weil-Pick Gram. The negative-definiteness is RH; over F_q
it is the geometry, over Q it must be supplied (candidate: cubic chirality c_2<0 = Connes' missing
eigenvalue). This probe exhibits the blueprint exactly; it does NOT construct the number-field surface.

sympy + numpy. No torch.
"""
import numpy as np
import math

def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
def ap_elliptic(p, A, B):
    return -sum(legendre(x**3 + A*x + B, p) for x in range(p))

A, B = 1, 1
print("=" * 92)
print("(1) the C x C primitive intersection Gram M=[[-2q,-a],[-a,-2]] is NEG-DEFINITE <=> RH over F_q")
print("=" * 92)
print(f"  E: y^2=x^3+{A}x+{B}; S=ExE; primitive parts Gamma_0 (Frobenius graph), Delta_0 (diagonal)")
print(f"  {'p':>4} {'a':>4} {'Gamma0^2':>9} {'Delta0^2':>9} {'Gamma0.Delta0':>14} {'det M=4q-a^2':>13} {'neg-def(M)?':>12} {'=RH?':>6}")
for p in (11, 13, 17, 19, 23, 29):
    a = ap_elliptic(p, A, B)
    M = np.array([[-2.0*p, -a], [-a, -2.0]])
    det = 4*p - a*a
    eig = np.linalg.eigvalsh(M)
    negdef = bool(np.all(eig < 0))
    rh = abs(a) <= 2*math.sqrt(p)
    print(f"  {p:>4} {a:>4} {-2*p:>9} {-2:>9} {-a:>14} {det:>13} {str(negdef):>12} {str(rh):>6}")
print("  => det M = 4q - a^2 > 0 (with trace<0) <=> M negative-definite <=> |a|<2sqrt q <=> |alpha|=sqrt q")
print("     = RH over F_q. The Hodge index theorem on the SURFACE S=CxC supplies the negative-definiteness")
print("     (a theorem, from the geometry). This is the geometric ORIGIN of the Rosati Gram (N7 Rem 6.3).")

print("\n" + "=" * 92)
print("(2) the intersection-number blueprint (exact, the data the number-field surface must reproduce)")
print("=" * 92)
p = 13; a = ap_elliptic(p, A, B)
rows = [
 ("h.h, v.v, h.v", "0, 0, 1   (hyperbolic plane)"),
 ("Delta.Delta = 2-2g", "0   (genus 1)"),
 ("Delta.h, Delta.v", "1, 1"),
 ("Gamma_F.h (1st proj deg)", "1"),
 ("Gamma_F.v (Frobenius deg)", f"{p}  (= q)"),
 ("Gamma_F.Delta = #C(F_q)", f"{p+1-a}  (= q+1-a, the Lefschetz fixed points)"),
 ("Gamma_F.Gamma_F = q(2-2g)", "0"),
]
print(f"  for p={p} (a={a}):")
for L, R in rows:
    print(f"    {L:>28} = {R}")
print("  => the explicit formula = Lefschetz = Gamma_F.Delta; arch-domination (q^n >> sum alpha^n) is the")
print("     Hodge-index inequality (Gamma_0.Delta_0)^2 <= Gamma_0^2 Delta_0^2, i.e. a^2 <= 4q.")

print("\n" + "=" * 92)
print("(3) THE NUMBER-FIELD OBLIGATION (open = RH): the apex feeds the analogue; the positivity is RH")
print("=" * 92)
print(f"  {'C x C over F_q (THEOREM)':>34}   {'scaling-site square over Q (via apex)':>40}")
for L, R in [
 ("surface S = C x C", "Connes scaling-site square [CC20]"),
 ("Frobenius graph Gamma_F", "Hasse-Davenport / (-1)^n lift [N5, opp ii]"),
 ("diagonal Delta", "archimedean edge operator + trivial part [N4/N5]"),
 ("Lefschetz Gamma_F.Delta", "the apex Weil form Q(g) [N5 sec6]"),
 ("primitive Gram M (neg-def)", "the apex Weil-Pick Gram (PSD)"),
 ("HODGE INDEX (geometry) *PROVEN*", "Gram definite = RH  *OPEN*"),
]:
    print(f"  {L:>34} <-> {R:>40}")
print("""  The apex supplies every LOCAL piece and the Gram STRUCTURE (this paper). The missing object is the
  DEFINITENESS of the primitive form -- over F_q a theorem (the surface and its Hodge index exist), over
  Q the open RH (no surface; must be constructed). Candidate mechanism: the cubic chirality c_2<0
  (L(1/2,chi3)=0.4808>0) as Connes' missing simple+even lowest eigenvalue -- the chiral channel supplying
  the one direction the metric channel's positivity needs.""")

print("\n" + "=" * 92)
print("VERDICT  --  the C x C positivity, blueprinted exactly; the construction over Q is open (= RH)")
print("=" * 92)
print("""  DELIVERED (the blueprint, exact [P]): over F_q the Weil positivity is the negative-definiteness of
  the primitive C x C intersection Gram M=[[-2q,-a],[-a,-2]] (det 4q-a^2>0 <=> RH), the surface-geometry
  origin of the Rosati Gram (N7 Rem 6.3). The intersection numbers (h,v,Delta,Gamma_F) are exhibited
  exactly; the explicit formula is the Lefschetz intersection; arch-domination is the Hodge-index
  inequality.
  THE OPEN RESEARCH (= RH): construct the number-field analogue -- the Connes scaling-site square with a
  negative-definite primitive intersection form -- FED by the apex's now-complete local data (the
  Hasse-Davenport Frobenius lift as Gamma_F, the archimedean edge operator as Delta, the Weil-Pick Gram
  as M). Over F_q the definiteness is the Hodge index (a theorem about an actual surface); over Q there
  is no surface, and supplying the definiteness -- with the cubic chirality c_2<0 as the candidate
  missing eigenvalue -- is the Riemann Hypothesis. The blueprint is exact and the local data complete;
  the surface and its positivity over Q are the genuine open construction. NO proof.""")
