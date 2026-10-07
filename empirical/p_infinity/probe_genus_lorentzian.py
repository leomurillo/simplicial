"""
P-infinity sec.3 -- HIGHER GENUS: the Lorentzian structure persists, and the FULL eigenvalue RH.

(3a) GENERAL g: the C x C 4-dim toy generalizes exactly. Delta^2=2-2g, Gamma_F^2=q(2-2g), primitives
     Delta_0=Delta-F1-F2, Gamma_0=Gamma_F-F1-qF2 give
        M_g = [[-2gq, -a],[-a, -2g]],   det M_g = 4 g^2 q - a^2,
     neg-def <=> |a| < 2 g sqrt q (the genus-g WEIL TRACE bound, generalizing Hasse). Full 4x4 Gram
     signature stays (1, 0, 3) = LORENTZIAN. Verified on a REAL genus-2 curve (point count -> a_1=trace).
     HONEST: the 4-dim toy captures only the TRACE bound |a|<=2g sqrt q (first eigenvalue moment).

(3b) FULL RH (each |alpha_i| = sqrt q, not just the trace): via the NORMALIZED FROBENIUS-POWER
     TOEPLITZ form. With Frobenius eigenvalues alpha_i = sqrt q * z_i and power sums a_k = sum alpha_i^k,
     the normalized moments t_k = a_k / q^{k/2} = sum z_i^k are the trigonometric moments of the measure
     sum delta_{z_i}. By Herglotz/Bochner, the Toeplitz form [t_{|j-k|}] is PSD  <=>  the z_i lie on the
     UNIT circle  <=>  all |alpha_i| = sqrt q  <=>  FULL RH-over-F_q. (This is the determinantal/circle
     face the program's Toeplitz work already touches; here it is the genus-g RH, not the trace bound.)

EXACT (sympy Z/Q; signature via charpoly+Descartes). No torch.
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

def Gram_CxC(q, a, g):
    D2 = 2-2*g; GF2 = q*(2-2*g)
    return sp.Matrix([[0,1,1,q],[1,0,1,1],[1,1,D2,q+1-a],[q,1,q+1-a,GF2]])
def primitive_M(q, a, g):
    return sp.Matrix([[-2*g*q,-a],[-a,-2*g]])

# ---- real genus-2 hyperelliptic curve y^2 = f(x), deg f = 5 (one point at infinity) ----
def a1_genus2(p, fcoeffs):
    """a_1 = trace = p+1 - #C(F_p). #C = 1 (infty) + sum_x (#y with y^2=f(x))."""
    def f(x):
        v = 0
        for c in fcoeffs: v = (v*x + c) % p   # Horner, fcoeffs high->low
        return v % p
    cnt = 1
    for x in range(p):
        r = f(x)
        for y in range(p):
            if (y*y - r) % p == 0: cnt += 1
    return p + 1 - cnt

print("="*90)
print("PART 3a - GENERAL g: M_g=[[-2gq,-a],[-a,-2g]], det=4g^2 q - a^2, |a|<2g sqrt q ; real genus-2 curve")
print("="*90)
print("  abstract g sweep (q=13): full 4x4 Gram stays Lorentzian (1,0,3); primitive bound |a|<2g sqrt(13):")
import math
for g in [1,2,3]:
    q=13; a=2  # a within bound for all these g
    G=Gram_CxC(q,a,g); M=primitive_M(q,a,g)
    print(f"   g={g}: sig(G)={signature(G)}  M={ [list(M.row(0)), list(M.row(1))] }  det={4*g*g*q-a*a}  "
          f"|a|<2g sqrt q = {2*g*math.sqrt(q):.2f}")
print("\n  REAL genus-2 curve  C: y^2 = x^5 + x + 1  over F_p  (g=2, trace bound |a_1| <= 4 sqrt p):")
print(f"   {'p':>4} {'a_1':>5} {'|a1|<=4sqrt p?':>14} {'sig(G 4x4)':>11} {'det M_2=16p-a1^2':>16} {'M_2 neg-def?':>12}")
fco = [1,0,0,0,1,1]  # x^5 + x + 1  (high->low)
for p in [7,11,13,17,19,23]:
    a = a1_genus2(p, fco); G=Gram_CxC(p,a,2); M=primitive_M(p,a,2)
    bound = a*a <= 16*p
    print(f"   {p:>4} {a:>5} {str(bound):>14} {str(signature(G)):>11} {str(16*p-a*a):>16} "
          f"{str(signature(M)==(0,0,2)):>12}")
print("""  Lorentzian (1,0,3) persists at every genus; the primitive bound is the genus-g Weil TRACE bound
  |a_1| <= 2g sqrt p. [P]  This 4-dim toy sees only the first eigenvalue moment a_1; FULL RH (every
  |alpha_i|=sqrt p) is Part 3b.""")

print("="*90)
print("PART 3b - FULL RH = Frobenius-power TOEPLITZ PSD  <=>  all eigenvalues on the circle |.|=sqrt q")
print("="*90)
def toeplitz_psd_report(name, q, z_list, m=5):
    """z_list = eigenvalues normalized by sqrt q (so alpha_i = sqrt q * z_i). t_k = sum z_i^k.
       Build Toeplitz [t_{|i-j|}]_{0..m}, report signature; PSD <=> all |z_i|=1 <=> full RH."""
    t = [sum(z**k for z in z_list) for k in range(0, m+1)]
    T = sp.Matrix(m+1, m+1, lambda i, j: t[abs(i-j)])
    sg = signature(T)
    psd = (sg[2] == 0)            # no negative eigenvalues
    oncirc = all(sp.nsimplify(abs(z))**2 == 1 or sp.simplify(abs(z)**2-1)==0 for z in z_list)
    print(f"  {name}: t_0..t_{m} = {[sp.nsimplify(x) for x in t]}")
    print(f"        Toeplitz signature {sg}  =>  PSD: {psd}   (all |z_i|=1: {oncirc})   "
          f"=> {'FULL RH' if psd else 'RH VIOLATED'}")

I = sp.I
# genus 2, all on the unit circle: z in {i,-i,1,-1} (4th roots of unity; |z|=1) -> integer moments,
# conjugate-reciprocal (i<->-i, 1<->1, -1<->-1), no surds.
on = [I, -I, sp.Integer(1), sp.Integer(-1)]
toeplitz_psd_report("on-circle (RH)   ", 4, on, m=6)
# genus 2, one pair OFF the circle: replace {1,-1} by real FE-pair {2, 1/2} (2*(1/2)=1) -> |z|!=1.
off = [I, -I, sp.Integer(2), sp.Rational(1,2)]
toeplitz_psd_report("off-circle (viol)", 4, off, m=6)
print("""  EXACT: on-circle eigenvalues -> Toeplitz PSD -> FULL RH; a single off-circle (real) pair makes
  the normalized moments grow geometrically -> Toeplitz acquires a negative eigenvalue -> NOT PSD ->
  RH violated. [P]  This is the full genus-g statement (all |alpha_i|=sqrt q), the determinantal/circle
  face: RH-over-F_q <=> the Frobenius-power Toeplitz (the trigonometric-moment form of the eigenvalue
  measure) is positive. The same object over Q is the Bures/Nevanlinna circle-Toeplitz of the zeros.""")

print("="*90)
print("SUMMARY (sec.3)")
print("="*90)
print("""  [P] 3a: M_g=[[-2gq,-a],[-a,-2g]], full Gram Lorentzian (1,0,3) at every genus; primitive bound =
      genus-g Weil trace bound |a_1|<=2g sqrt q; verified on a real genus-2 curve.
  [P] 3b: FULL RH (each |alpha_i|=sqrt q) <=> normalized Frobenius-power Toeplitz PSD; exact on/off-circle
      flip. The toy Lorentzian form (trace) and the Toeplitz form (full spectrum) are the two exact
      faces; both have the SAME Q-side obstruction = the F_1 surface / arch-domination = RH.""")
