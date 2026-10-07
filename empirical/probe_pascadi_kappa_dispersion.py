"""
N1b -- pin the dispersion efficiency kappa in theta_0 = 1/2 + kappa*eta (Pascadi handoff, Paper 43 8).

Per-modulus completed-Pascadi bound (Section 8.1-8.3 of the rewrite):
    |Delta_d| << sqrt(X) * d^{-eta_eff}                       (balanced d | P_n)
    => sum_{d<=Q} |Delta_d| << sqrt(X) Q^{1-eta_eff} << X  <=>  theta < 1 / (2(1-eta_eff)).
So kappa is set by eta_eff, the EFFECTIVE per-modulus saving exponent.

THE HINGE (paranoid check).  Pascadi Ex 1.3 gives d^{-1/12} ONLY if d has a divisor d' ~ sqrt(d) with
d/d' squarefree.  For d | P_n the divisor lattice has multiplicative gaps up to the largest prime
p_n = X^beta, so the best balanced divisor is d' in [sqrt(d)/p_n, sqrt(d)], and the saving degrades:
    saving = (f/min(d,d'^2))^{1/6} with d' ~ sqrt(d)/p_n, f=d'  =>  p_n^{1/6} d^{-1/12}
           = X^{beta/6} d^{-1/12} = d^{-eta_eff},   eta_eff = 1/12 - beta/(6 theta).
So eta_eff (hence kappa, hence the level) depends on beta = log p_n / log X.

This script computes, EXACTLY, the achievable level theta_ach(beta) and the n=6 threshold beta_max.
Verdict: n=6 (needs theta >= theta_0(6)=8/15) is secured IFF the binding moduli have largest prime
p_n <= X^{theta/8}; under Paper 43's looser p_n <= X^{theta/5}, the worst case FAILS n=6.
"""
import sympy as sp

C_star = sp.Rational(14, 5)         # 2.80
eta0 = sp.Rational(1, 12)           # base Pascadi saving (beta=0, fully balanced)
theta6 = 1 - C_star / 6             # = 8/15, the n=6 required level
half = sp.Rational(1, 2)

def eta_eff(beta, theta):
    return eta0 - beta / (6 * theta)

def theta_ach(eta):
    return 1 / (2 * (1 - eta))      # from theta(1-eta_eff)=1/2

print("N1b -- pin kappa: achievable primorial-BV level vs largest-prime exponent beta")
print(f"  base saving eta0 = 1/12 = {float(eta0):.4f};  n=6 needs theta_0(6) = 8/15 = {float(theta6):.4f}")
print("=" * 80)

# favorable regime: beta -> 0 (p_n = X^{o(1)}, minimal-n coupling)
eta_fav = eta_eff(0, theta6)
th_fav = theta_ach(eta_fav)
kappa_fav = (th_fav - half) / eta0
print(f"  beta=0 (ideal):  eta_eff=1/12,  theta_ach = 1/(2*11/12) = 6/11 = {float(th_fav):.4f}"
      f"   kappa = {sp.nsimplify(kappa_fav)} = {float(kappa_fav):.3f}")
print(f"                   -> 6/11={float(sp.Rational(6,11)):.4f} >= 8/15={float(theta6):.4f}  =>  n=6 SECURED (kappa 0.545 >= 0.40)")
print("-" * 80)

# threshold: largest beta for which theta_ach(beta) >= theta6
beta = sp.Symbol('beta', positive=True)
sol = sp.solve(sp.Eq(theta_ach(eta_eff(beta, theta6)), theta6), beta)
beta_max = [s for s in sol if s > 0][0]
print(f"  n=6 threshold:  theta_ach(beta) = 8/15  at  beta = {sp.nsimplify(beta_max)} = {float(beta_max):.4f}")
print(f"                  = theta_0(6)/8 = {float(theta6/8):.4f}  (i.e. p_n <= X^{{theta/8}})")
print("-" * 80)

print(f"  {'beta = log p_n/log X':>22} | {'eta_eff':>9} | {'theta_ach':>10} | n=6?")
print("  " + "-" * 64)
for beta_val in [sp.Integer(0), theta6/16, theta6/8, sp.Rational(1,15), theta6/5, sp.Rational(1,10)]:
    ee = eta_eff(beta_val, theta6)
    ta = theta_ach(ee)
    ok = "YES" if ta >= theta6 else "NO"
    label = f"{float(beta_val):.4f}"
    note = ""
    if beta_val == theta6/8:
        note = " (threshold)"
    if beta_val == theta6/5:
        note = " (Paper43 r0=5 constraint p_n<=X^{theta/5})"
    print(f"  {label:>22} | {float(ee):>9.4f} | {float(ta):>10.4f} | {ok}{note}")

print("=" * 80)
print("VERDICT (N1b).  kappa is NOT a single constant -- it is regime-dependent via beta=log p_n/log X:")
print("  - favorable (beta=0, minimal-n, p_n=X^{o(1)}):  kappa = 6/11 = 0.545 >= 0.40  =>  n=6 secured.")
print("  - n=6 holds IFF binding moduli have p_n <= X^{theta/8} ~ X^{0.067}.")
print("  - Paper 43's looser p_n <= X^{theta/5}: worst case theta_ach=0.526 < 0.533  =>  n=6 can FAIL.")
print("So n=6 is secured CONDITIONAL on the bridge's n-X coupling giving p_n <= X^{theta/8} (a smooth-")
print("enough-moduli condition, the bridge's business -- ocho 7 -- not Pascadi's).  Plus: Type-III")
print("admissibility at theta~0.53 must be checked separately.  n=7 (theta_0=0.60 > 6/11) out regardless.")
