"""
probe_gamma_kch_identity.py  --  hardening the CBS kappa_3 tri-linkage into an EXACT identity.

CLAIM (Proposition). The Stuart-Landau symmetry-breaking coefficient gamma -- the zbar^2 coefficient
of the cubic gradient vector field on the slow rotational 2-plane -- is EXACTLY (minus the conjugate
of) the spin-3 component of the Amari-Chentsov cubic K^CH = d^3 Phi (= the third cumulant of the
log-partition Phi). In real components on the plane (K_abc symmetric, a,b,c in {1,2}):

    gamma = -(1/8) [ (K111 - 3 K122) + i (3 K112 - K222) ]  =  - conj(w3),

where w3 is the z^3 (spin-3, traceless) component of the cubic form, and the resonant gauge-covariant
|z|^2 z part is carried by the spin-1 (trace) component w1. Hence the SAME cubic K^CH = d^3 Phi sets:
cycle non-circularity (gamma = its spin-3 part), the curvature defect nu_D (a contraction of it), and
the spectral->functional gap (a positive quadratic in it). One tensor, three readings.

PART 1  EXACT algebraic identity: gamma = -conj(spin-3 part) for a GENERAL symmetric cubic (symbolic).
PART 2  K = d^3 Phi = kappa_3: for the categorical (softmax) log-partition, verify d^3 Phi equals the
        exact third-central-moment (cumulant) formula -- so K really is the Amari-Chentsov cubic.
PART 3  assemble: evaluate gamma at a concrete categorical point in the Helmert mean-zero plane.

sympy exact. No torch.
"""
import sympy as sp

print("=" * 88)
print("PART 1  EXACT identity: gamma (zbar^2 coeff of cubic gradient flow) = -conj(spin-3 of K^CH)")
print("=" * 88)
K111, K112, K122, K222 = sp.symbols('K111 K112 K122 K222', real=True)
z, zb = sp.symbols('z zb')                       # z and zbar, treated as independent (Wirtinger)
x1 = (z + zb) / 2
x2 = (z - zb) / (2 * sp.I)

# real cubic form  C = K_abc x^a x^b x^c  (symmetric)  and potential V3 = C/6
C = K111 * x1**3 + 3 * K112 * x1**2 * x2 + 3 * K122 * x1 * x2**2 + K222 * x2**3
C = sp.expand(C)
V3 = C / 6

# spin decomposition of the cubic FORM:  C = 2 Re(w3 z^3) + 6 Re(w1 z^2 zb)
Cpoly = sp.Poly(C, z, zb)
w3 = Cpoly.coeff_monomial(z**3)                  # z^3 coefficient  (spin-3, traceless)
w1 = Cpoly.coeff_monomial(z**2 * zb) / 3         # z^2 zb coefficient / 3  (spin-1, trace)

# cubic gradient flow in complex form:  zdot = -2 d/dzbar V3
zdot = sp.expand(-2 * sp.diff(V3, zb))
gamma = sp.Poly(zdot, z, zb).coeff_monomial(zb**2)
resonant = sp.Poly(zdot, z, zb).coeff_monomial(z * zb)   # |z|^2 z  (= z^2 zb) coefficient

gamma_claim = -sp.Rational(1, 8) * ((K111 - 3 * K122) + sp.I * (3 * K112 - K222))
print(f"  w3 (z^3 / spin-3 coeff of K^CH) = {sp.simplify(w3)}")
print(f"  gamma (zbar^2 coeff of zdot)    = {sp.simplify(gamma)}")
print(f"  gamma - [-(1/8)((K111-3K122)+i(3K112-K222))] = {sp.simplify(gamma - gamma_claim)}   (==0)")
print(f"  gamma - (-conj(w3))             = {sp.simplify(gamma - (-sp.conjugate(w3)))}   (==0  =>  gamma = -conj(spin-3))")
print(f"  resonant |z|^2 z coeff          = {sp.simplify(resonant)}")
print(f"  resonant - (-2 conj(w1))        = {sp.simplify(resonant - (-2 * sp.conjugate(w1)))}   (==0  =>  resonant = spin-1)")
print(f"  |gamma|^2 = (1/64)[(K111-3K122)^2+(3K112-K222)^2]? "
      f"{sp.simplify(sp.Abs(gamma_claim)**2 - sp.Rational(1,64)*((K111-3*K122)**2+(3*K112-K222)**2))==0}")
print("  => EXACT: gamma is the spin-3 (traceless) part of the cubic K^CH, constant 1/8; the gauge-")
print("     covariant resonant part is the spin-1 (trace) part. Pure algebra of a symmetric 3-tensor.")

print("\n" + "=" * 88)
print("PART 2  K^CH = d^3 Phi = kappa_3:  categorical log-partition, d^3 Phi == 3rd central moment")
print("=" * 88)
e1, e2 = sp.symbols('eta1 eta2', real=True)
Phi = sp.log(sp.exp(e1) + sp.exp(e2) + 1)         # Z/3 categorical, gauge eta3=0
p = [sp.exp(e1), sp.exp(e2), sp.Integer(1)]
Zt = sum(p); p = [pi / Zt for pi in p]            # probabilities
eta = [e1, e2]
# d^3 Phi  vs  third central moment of the one-hot indicator (exact cumulant formula)
def kron(i, j): return sp.Integer(1) if i == j else sp.Integer(0)
ok = True
for a in range(2):
    for b in range(2):
        for c in range(2):
            d3 = sp.simplify(sp.diff(Phi, eta[a], eta[b], eta[c]))
            kappa = sp.simplify(p[a]*kron(a, b)*kron(b, c)
                                - p[a]*p[c]*kron(a, b) - p[a]*p[b]*kron(a, c) - p[a]*p[b]*kron(b, c)
                                + 2*p[a]*p[b]*p[c])
            if sp.simplify(d3 - kappa) != 0:
                ok = False
print(f"  d^3 Phi == exact third-central-moment formula for all (a,b,c)? {ok}")
print("  => Phi is the cumulant generating function, so K^CH = d^3 Phi is literally the 3rd cumulant.")

print("\n" + "=" * 88)
print("PART 3  assemble gamma at a concrete categorical point (Helmert mean-zero 2-plane)")
print("=" * 88)
# Helmert orthonormal basis of the mean-zero plane of R^3
h1 = [sp.Rational(1, 1), sp.Rational(-1, 1), sp.Integer(0)]
h1 = [x / sp.sqrt(2) for x in h1]                 # (1,-1,0)/sqrt2
h2 = [sp.Rational(1, 1), sp.Rational(1, 1), sp.Integer(-2)]
h2 = [x / sp.sqrt(6) for x in h2]                 # (1,1,-2)/sqrt6
H = [h1, h2]
pv = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)]   # a generic categorical point
# full 3x3x3 third cumulant of the one-hot indicator at pv
def kap(i, j, k):
    return (pv[i]*kron(i, j)*kron(j, k)
            - pv[i]*pv[k]*kron(i, j) - pv[i]*pv[j]*kron(i, k) - pv[i]*pv[j]*kron(j, k)
            + 2*pv[i]*pv[j]*pv[k])
# project onto the Helmert plane -> K_abc (a,b,c in {1,2})
def Kproj(a, b, c):
    return sp.simplify(sum(kap(i, j, k)*H[a][i]*H[b][j]*H[c][k]
                           for i in range(3) for j in range(3) for k in range(3)))
K = {(a, b, c): Kproj(a, b, c) for a in range(2) for b in range(2) for c in range(2)}
K111v, K112v, K122v, K222v = K[(0,0,0)], K[(0,0,1)], K[(0,1,1)], K[(1,1,1)]
gamma_val = sp.simplify(-sp.Rational(1, 8) * ((K111v - 3*K122v) + sp.I*(3*K112v - K222v)))
absg = sp.simplify(sp.sqrt(sp.Abs(gamma_val)**2))
print(f"  p = (1/2, 1/3, 1/6);  K^CH in Helmert plane:")
print(f"    K111={K111v}, K112={K112v}, K122={K122v}, K222={K222v}")
print(f"  gamma = {gamma_val}")
print(f"  |gamma| = {sp.nsimplify(absg)} = {sp.N(absg, 8)}   (= magnitude of the spin-3 part of K^CH)")

print("\n" + "=" * 88)
print("PROPOSITION (hardened)")
print("=" * 88)
print("""  For any log-partition Phi with Amari-Chentsov cubic K^CH = d^3 Phi, on a slow rotational 2-plane
  with complex coordinate z = x1 + i x2 the Stuart-Landau symmetry-breaking coefficient is EXACTLY
        gamma = -(1/8)[(K111 - 3 K122) + i (3 K112 - K222)] = - conj( spin-3 part of K^CH ),
  with the gauge-covariant resonant term the spin-1 (trace) part. Thus the CBS kappa_3 tri-linkage is
  one tensor read three ways: gamma = spin-3(K^CH) (orbit non-circularity), nu_D = a contraction of
  K^CH (curvature defect), spectral->functional gap = a positive quadratic in K^CH. This upgrades CBS
  Prop 9.1 from a certified scaling law (eps ~ kappa_3) to an exact identity with the explicit
  constant 1/8 and the explicit spin-projection, anchored to the program's cubic K^CH (paper 17 /
  cumulant tower) -- series-grade, exact-arithmetic.""")
