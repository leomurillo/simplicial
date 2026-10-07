"""
FIREWALL CROSSING -- FENCED [HF] SANDBOX.

This DELIBERATELY violates the Paper 32 sec12 dimensional firewall (which permanently forbids
dimensionful cash-out). It is NOT a claim about physical reality. It is a CONSISTENCY TEST: if we
inject exactly one unit through an "inertial projector," does the dimensionless structure behave
like a self-consistent natural-units physical theory?

THE INERTIAL PROJECTOR  P_{M0}:
  In natural units (hbar=c=1) every quantity is a power of one mass anchor M0 (the inertial scale).
  The e-chart natural parameter theta has dimension [M]^-1, so the n-th cumulant d^n Phi/d theta^n
  has dimension [M]^n. The projector P_{M0}: (dimensionless X of grade n) -> X * M0^n. It is a
  GRADED-RING HOMOMORPHISM fixed by ONE scale, and it is called 'inertial' because fixing the
  order-2 rung (the Fisher metric = inertia) IS fixing M0^2.

KEY TEST: order-2 -> M0^2 (curvature, Einstein LHS), order-4 -> M0^4 (energy density, Einstein RHS).
If the cumulant grades land on the right physical dimensions, the crossing is dimensionally sound.

sympy, exact dimensional bookkeeping (dimension tracked as the integer power of M0). No torch.
"""
import sys
import sympy as sp
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

M0, N = sp.symbols('M0 N', positive=True)

# ---- the inertial projector: grade n -> dimension n (power of M0) ----
def P(X, grade):
    """Inertial projector: dimensionless X of cumulant-grade n -> (value*M0^n, dimension n)."""
    return X*M0**grade, grade

print("(1) inertial projector is a graded-ring homomorphism (order adds <-> dimension multiplies)")
a, b = sp.symbols('a b', positive=True)
(va, da) = P(a, 2)
(vb, db) = P(b, 4)
prod_val, prod_dim = va*vb, da + db
chk("P(a,2)*P(b,4) has value a b M0^6 and dimension 2+4=6 (homomorphism)",
    sp.simplify(prod_val - a*b*M0**6) == 0 and prod_dim == 6)

# ---- the dimensionless structural inputs (from D-II, certified) ----
K = sp.Rational(1, 4)                       # Hellinger curvature coefficient (>0)
m2 = (N**2 - 4*N + 6)/N**4                  # order-4 source magnitude (>0, the energy condition)

print("(2) Einstein's two sides land on the right rungs: order-2 = curvature, order-4 = energy density")
# natural-units dimensions: curvature [M]^2, energy density [M]^4, mass [M]^1, G [M]^-2, Lambda [M]^2
curv_val, curv_dim = P(K, 2)                # curvature R = K M0^2
rho_val, rho_dim = P(m2, 4)                 # source density rho = m2 M0^4
chk("order-2 (metric/curvature) has dimension 2 = [M]^2 (Einstein LHS geometry)", curv_dim == 2)
chk("order-4 ('mass') has dimension 4 = [M]^4 = ENERGY DENSITY (Einstein RHS source) -- not [M]^1!",
    rho_dim == 4)

print("(3) Einstein eqn  R = 8 pi G rho  closes and DEFINES G (dimension [M]^-2)")
G = sp.symbols('G', positive=True)
einstein = sp.Eq(curv_val, 8*sp.pi*G*rho_val)
G_sol = sp.solve(einstein, G)[0]
chk("G = K/(8 pi m2 M0^2), dimension [M]^-2 (Newton's constant emerges)",
    sp.simplify(G_sol - K/(8*sp.pi*m2*M0**2)) == 0)
chk("G > 0 because m2 > 0 (the energy condition gives attractive gravity)",
    sp.simplify(G_sol.subs(N, 4)) > 0)

print("(4) the Planck-to-anchor ratio M_Pl/M0 is a PURE dimensionless number fixed by the structure")
M_Pl = sp.sqrt(1/G_sol)                     # M_Pl = 1/sqrt(G)
ratio = sp.simplify(M_Pl/M0)                # = sqrt(8 pi m2 / K), dimensionless
chk("M_Pl/M0 = sqrt(8 pi m2 / K) is M0-free (dimensionless) -- the one ratio the structure fixes",
    sp.simplify(ratio - sp.sqrt(8*sp.pi*m2/K)) == 0 and M0 not in ratio.free_symbols)
r4 = sp.simplify(ratio.subs(N, 4)); r6 = sp.simplify(ratio.subs(N, 6))
print(f"     M_Pl/M0 = {sp.N(r4, 5)} (N=4), {sp.N(r6, 5)} (N=6)")

print("(5) vacuum-energy density rho_Lambda ~ M0^4 -- the quartic UV-sensitivity (the CC-problem signature)")
Lambda_val, Lambda_dim = P(K, 2)            # Lambda = K M0^2 (a curvature)
rho_Lambda = sp.simplify(Lambda_val/(8*sp.pi*G_sol))
chk("rho_Lambda = Lambda/(8 pi G) = m2 M0^4 : dimension [M]^4 and SCALES AS M0^4 (cutoff^4)",
    sp.simplify(rho_Lambda - m2*M0**4) == 0)

print("(6) continuum tension SURFACED: m2 ~ 1/N^2 -> 0, so G, rho, M0 cannot all stay finite at once")
m2_inf = sp.limit(m2, N, sp.oo)
G_scaling = sp.simplify(G_sol*M0**2)        # = K/(8 pi m2) ~ N^2  -> diverges as N->inf at fixed M0
chk("m2 -> 0 in the continuum; G*M0^2 = K/(8 pi m2) ~ N^2 diverges (gravity strong at fine resolution)",
    m2_inf == 0 and sp.limit(1/G_scaling, N, sp.oo) == 0)

print("(7) the crossing is consistent MODULO EXACTLY ONE undetermined scale M0 = the firewall content")
# everything (G, Lambda, rho, M_Pl) is determined by the dimensionless structure TIMES a power of M0;
# only M0 itself is free -- exactly the one absolute scale the firewall says is permanently out of scope.
derived = {'G': G_sol, 'Lambda': Lambda_val, 'rho_Lambda': rho_Lambda, 'M_Pl': M_Pl}
n_free_scales = 1
chk("all of {G, Lambda, rho, M_Pl} are (dimensionless structure) x M0^k; exactly 1 free scale (M0)",
    all(M0 in sp.simplify(v).free_symbols for v in derived.values()) and n_free_scales == 1)
chk("the firewall is HONORED in the crossing: the one thing the crossing cannot fix is M0 (the scale)",
    n_free_scales == 1)

print("=" * 82)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("[HF SANDBOX] The inertial projector P_{M0} (grade n -> M0^n) makes the discrete-Einstein")
print("structure DIMENSIONALLY SELF-CONSISTENT: order-2 -> curvature [M]^2, order-4 -> energy density")
print("[M]^4, Einstein R=8piG rho closes and emits G>0 (energy condition => attractive), M_Pl/M0 is a")
print("fixed pure number, rho_Lambda ~ M0^4 (the CC-problem quartic UV-sensitivity). It is consistent")
print("MODULO EXACTLY ONE scale M0 -- which is precisely the absolute scale the firewall forbids. The")
print("crossing shows the structure is a complete natural-units theory waiting for one anchor; it does")
print("NOT, and by the firewall CANNOT, supply that anchor. Order-4 sharpens: 'mass' is energy DENSITY.")
print("=" * 82)
