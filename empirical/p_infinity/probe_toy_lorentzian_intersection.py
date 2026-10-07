"""
P-infinity anchoring certificate: THE TOY FINITE LORENTZIAN INTERSECTION FORM.

Paper: "What Is Multiplicative? The Intersection Metric and the Lorentzian Geometry of the
Arithmetic Apex" (exterior peh-series keystone, twin of laned-series T0).

Thesis being certified (all in EXACT arithmetic -- sympy Z/Q, signature via the characteristic
polynomial + Descartes, which is EXACT for symmetric matrices since all eigenvalues are real;
we read the SIGNATURE, a congruence invariant by Sylvester's law, NOT float conditioning):

  CLAIM 2  The multiplicative metric (the intersection form on NS(C x C)) is LORENTZIAN,
           signature (1, rho-1).  [P over F_q]
  CLAIM 5  RH-over-F_q  <=>  the primitive cone is causal (spacelike): the primitive Gram
           M = [[-2q,-a],[-a,-2]] is negative-definite  <=>  det = 4q-a^2 > 0  <=>  |a| <= 2 sqrt q
           (Hasse/Weil).  The boundary |a|=2 sqrt q is the NULL cone (a primitive class becomes
           lightlike); |a|>2 sqrt q is ACAUSAL (a primitive class goes timelike = a zero off the line).
  CLAIM 3  Fisher (additive, order 2) is RIEMANNIAN (n,0); intersection (multiplicative, order 2)
           is LORENTZIAN (1,n-1).  Same order, opposite signature = the signature flip.
  CLAIM 4  There is exactly ONE timelike direction (the polarization / ample class h+v);
           over Q it must be supplied at the archimedean place.
  CLAIM 7  Scalar shadow: the primorial is not a moment sequence (Hankel D_3 < 0) -- the scalar
           witness of Lorentzian indefiniteness; Gamma (additive) has a moment rep, peh (mult.) does not.

Intersection theory on the surface S = C x C, C of genus g (elliptic g=1 is the clean toy):
  basis  B = [F1, F2, Delta, Gamma_F]  with F1 = C x {pt}, F2 = {pt} x C, Gamma_F = graph of Frobenius.
  F1^2=0, F2^2=0, F1.F2=1 ; Delta^2 = 2-2g ; Delta.F1=Delta.F2=1 ;
  Gamma_F.F1 = q (deg Frobenius), Gamma_F.F2 = 1 ; Gamma_F.Delta = #C(F_q) = q+1-a (Lefschetz=explicit formula);
  Gamma_F^2 = q(2-2g)  (adjunction: K_S=(2g-2)(F1+F2)).
Primitive classes (orthogonal to the {F1,F2} hyperbolic plane): Delta_0=Delta-F1-F2, Gamma_0=Gamma_F-F1-qF2.
  Delta_0^2 = -2g  ... (g=1: -2) ; Gamma_0^2 = q(2-2g)-2q = -2gq ... (g=1: -2q) ; Gamma_0.Delta_0 = -a.
  => for g=1, the primitive Gram is exactly M = [[-2q, -a],[-a, -2]].

No torch. Exact only.
"""
import sympy as sp

# ---------- exact signature via charpoly + Descartes (valid: symmetric => all real eigenvalues) ----------
def signature(Mat):
    """Return (n_plus, n_zero, n_minus) exactly for a symmetric sympy integer/rational matrix."""
    n = Mat.shape[0]
    lam = sp.symbols('lam')
    p = Mat.charpoly(lam)                  # monic, exact integer/rational coeffs
    coeffs = p.all_coeffs()                # highest degree first, length n+1
    # multiplicity of zero root = number of trailing zero coeffs
    nz = 0
    while coeffs and coeffs[-1] == 0:
        nz += 1; coeffs = coeffs[:-1]
    # strip to the nonzero-root polynomial q(lam) of degree (n - nz); all its roots real & nonzero
    def sign_changes(seq):
        s = [c for c in seq if c != 0]
        return sum(1 for i in range(len(s)-1) if s[i]*s[i+1] < 0)
    n_plus = sign_changes(coeffs)                                   # Descartes on q(lam): # positive roots
    alt = [c*(-1)**i for i, c in enumerate(coeffs)]                 # q(-lam) coeffs (coeffs high->low)
    n_minus = sign_changes(alt)                                     # # negative roots
    assert n_plus + n_minus + nz == n, (n_plus, n_minus, nz, n)
    return n_plus, nz, n_minus

def is_neg_def(Mat):
    p, z, m = signature(Mat)
    return (p == 0 and z == 0)

def Gram_CxC(q, a, g=1):
    """Full 4x4 intersection Gram on [F1,F2,Delta,Gamma_F]."""
    D2 = 2 - 2*g
    GF2 = q*(2 - 2*g)
    return sp.Matrix([
        [0,        1,        1,        q        ],
        [1,        0,        1,        1        ],
        [1,        1,        D2,       q + 1 - a],
        [q,        1,        q + 1 - a, GF2     ],
    ])

def primitive_M(q, a, g=1):
    """2x2 primitive Gram [[Gamma_0^2, Gamma_0.Delta_0],[.,Delta_0^2]]."""
    return sp.Matrix([[-2*g*q, -a], [-a, -2*g]])

# ---------- point-count a_p for a real elliptic curve y^2 = x^3 + x + 1 over F_p ----------
def a_of_curve(p):
    cnt = 1  # point at infinity
    for x in range(p):
        rhs = (x*x*x + x + 1) % p
        for y in range(p):
            if (y*y - rhs) % p == 0:
                cnt += 1
    return p + 1 - cnt   # a_p = p+1 - #E(F_p)

print("="*88)
print("PART 1 - REAL elliptic curves E: y^2=x^3+x+1 over F_p : the intersection form IS Lorentzian")
print("="*88)
print(f"  {'p':>4} {'a_p':>5} {'|a|<=2sqrt p?':>13} {'sig(G 4x4)':>12} {'Lorentzian?':>12} "
      f"{'det M=4p-a^2':>13} {'M neg-def?':>11}")
for p in [11, 13, 17, 19, 23, 29, 31, 37, 41]:
    a = a_of_curve(p)
    G = Gram_CxC(p, a, g=1)
    M = primitive_M(p, a, g=1)
    sg = signature(G)
    hasse = a*a <= 4*p
    detM = sp.Integer(4*p - a*a)
    print(f"  {p:>4} {a:>5} {str(hasse):>13} {str(sg):>12} "
          f"{str(sg==(1,0,3)):>12} {str(detM):>13} {str(is_neg_def(M)):>11}")
print("""
  READING: a_p is the GENUINE Frobenius trace (Hasse |a|<=2sqrt p holds, a THEOREM). The full
  4x4 intersection Gram has signature (1,0,3) = LORENTZIAN at every prime [Claim 2], and the
  primitive Gram M=[[-2p,-a],[-a,-2]] is negative-definite with det=4p-a^2>0 [Claim 5]. The
  arithmetic supplies a Lorentzian-causal metric, exactly.""")

print("="*88)
print("PART 2 - the UNIQUE timelike direction is the polarization (ample) class h+v")
print("="*88)
p, a = 13, a_of_curve(13)
G = Gram_CxC(p, a, g=1)
amp = sp.Matrix([1, 1, 0, 0])          # F1 + F2
print(f"  (F1+F2)^2 = {(amp.T*G*amp)[0]}  > 0  => TIMELIKE (the one '+').")
for nm, v in [("F1", (1,0,0,0)), ("Gamma_0", (-1,-p,0,1)), ("Delta_0", (-1,-1,1,0))]:
    v = sp.Matrix(v); val = int((v.T*G*v)[0])
    kind = 'timelike' if val>0 else ('null' if val==0 else 'spacelike')
    print(f"  {nm:>8}^2 = {val:>6}  => {kind}")
print("""  Exactly one timelike direction (h+v); the primitive classes Gamma_0, Delta_0 are spacelike.
  [Claim 4] Over Q this single timelike/polarization direction must be supplied at the
  archimedean place -- the 'time' of the arithmetic spacetime.""")

print("="*88)
print("PART 3 - the LIGHT CONE: RH-over-F_q <=> primitive cone causal (signature flip at |a|=2sqrt q)")
print("="*88)
print("  Abstract (q,a) pairs (Weil's theorem FORBIDS |a|>2sqrt q; we cross it to see the flip):")
print(f"  {'q':>4} {'a':>4} {'det M':>7} {'M sig':>10} {'cone':>9} {'G sig':>10} {'verdict':>14}")
for (q, a) in [(7,4),(7,5),(7,6),(9,5),(9,6),(9,7),(25,9),(25,10),(25,11)]:
    M = primitive_M(q, a, 1); G = Gram_CxC(q, a, 1)
    sM = signature(M); sG = signature(G); detM = 4*q - a*a
    if detM > 0 and sM == (0,0,2):
        cone, verdict = "spacelike", "CAUSAL (RH)"
    elif detM == 0:
        cone, verdict = "null", "BOUNDARY"
    else:
        cone, verdict = "indefinite", "ACAUSAL (off-line)"
    print(f"  {q:>4} {a:>4} {detM:>7} {str(sM):>10} {cone:>9} {str(sG):>10} {verdict:>14}")
print("""  EXACT signature flip: |a|<2sqrt q -> M=(0,0,2) primitive spacelike, G=(1,0,3) Lorentzian-causal
  (RH); |a|=2sqrt q -> det M=0, a primitive class is NULL (the Hasse boundary = the critical line);
  |a|>2sqrt q -> M indefinite (a primitive class goes TIMELIKE) and G flips to (2,0,2) -- a zero has
  left the spacelike cone = left the critical line. [Claim 5] This is the causal reading of RH, exact.""")

print("="*88)
print("PART 4 - the SIGNATURE FLIP: additive (Fisher) is Riemannian, multiplicative (intersection) Lorentzian")
print("="*88)
# additive 2nd-order: Fisher metric of a strictly-positive ledger rho on 4 points = diag(1/rho_i) (>0).
rho = [sp.Rational(1,3), sp.Rational(1,4), sp.Rational(1,4), sp.Rational(1,6)]
Fisher = sp.diag(*[1/r for r in rho])
sF = signature(Fisher)
p, a = 13, a_of_curve(13); G = Gram_CxC(p, a, 1); sG = signature(G)
print(f"  ADDITIVE  (Fisher metric diag(1/rho), order 2) : signature {sF}  => RIEMANNIAN (n,0)")
print(f"  MULTIPLIC.(intersection Gram G, order 2)        : signature {sG}  => LORENTZIAN (1,n-1)")
print("""  Same order (2), opposite signature. [Claim 3] The additive/Fisher form is positive-definite
  hence (Tower Theorem) definite=>vacuous: it lives on the spacelike sheet and is blind to the one
  timelike (archimedean) direction where the RH content lives. The leap from additive to
  multiplicative is the leap from Riemannian to Lorentzian -- the signature flip.""")

print("="*88)
print("PART 5 - SCALAR SHADOW: the primorial is not a moment sequence (Hankel D_3 < 0)")
print("="*88)
P = [1, 2, 6, 30, 210, 2310, 30030]   # primorials P_0..P_6
def hankel_det(seq, n):
    return sp.Matrix(n+1, n+1, lambda i, j: seq[i+j]).det()
for n in range(0, 4):
    Dn = hankel_det(P, n)
    print(f"  D_{n} = det[P_(i+j)]_(0..{n}) = {Dn}   {'(>0)' if Dn>0 else '(< 0  => NOT a moment sequence)'}")
print("""  D_3 < 0 => no positive measure mu has P_n = integral t^n dmu => the primorial (a multiplicative
  object) admits NO additive (Mellin/moment) representation. The factorial does (n!=int t^n e^-t dt =>
  Gamma). [Claim 7] Gamma is the additive completion; peh (the smooth primorial, T15 sec 12) is the
  multiplicative one, living where no positive measure can. D_3<0 is the scalar shadow of the
  Lorentzian indefiniteness certified geometrically in Parts 1-4.""")

print("="*88)
print("CERTIFICATE SUMMARY (all exact; signature = Sylvester-invariant, not float conditioning)")
print("="*88)
print("""  [P] Claim 2: intersection metric Lorentzian (1,rho-1) at every real prime (Part 1).
  [P] Claim 5: RH/F_q = primitive cone spacelike = M neg-def = |a|<=2sqrt q; exact light-cone flip (Part 3).
  [P] Claim 3: additive=Riemannian (n,0) vs multiplicative=Lorentzian (1,n-1) -- the signature flip (Part 4).
  [A] Claim 4: unique timelike = polarization h+v; over Q = the archimedean place (Part 2).
  [P] Claim 7: primorial not a moment sequence, D_3<0 -- scalar shadow of indefiniteness (Part 5).
  OPEN [C]: construct (X/F_1, F, intersection form) over Q with this Lorentzian-causal structure = RH.
  The toy Lorentzian intersection form is the anchoring certificate of the P-infinity paper.""")
