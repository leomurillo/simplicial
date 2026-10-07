"""
D-I: the Surprise-Debt Theorem.

The CBS-P4 blind-cubic collision weight  C2(p) = sum_y 1/p_y^2  is the price of capturing the
order-3 structure a second-order (Fisher/Gram) model is blind to. This cert establishes:

 (1) THREE FACES of C2 -- one functional, three readings:
       (a) blind cubic coupling  T_p(chi_k,chi_l,chi_m) = sum 1/p_y^2   [CBS P4, 18/18, cited]
       (b) L1 mass of the third cumulant  sum_y |d^3 phi / dp_y^3| = sum 1/p_y^2   [here]
       (c) squared Fisher norm  tr(g^2) = ||Hess(phi)||_F^2 = sum 1/p_y^2        [here]
     (phi = sum p log p = negative entropy; g = Hess(phi) = diag(1/p) = Fisher metric.)

 (2) C2 is strictly SCHUR-CONVEX (manifest SOS certificate), uniquely minimized at the
     barycenter p_* with C2(p_*) = n^3, and diverging to +inf at every face.

 (3) The entropy H = -phi is strictly SCHUR-CONCAVE, uniquely maximized at p_*.

 (4) CO-EXTREMALITY (the user's "maximize short-term surprise <=> minimize long-term debt"):
     H Schur-concave and C2 Schur-convex are extremized at the SAME point p_*. Maximizing
     entropy (exploration) IS minimizing the surprise debt. Along any sharpening (majorization-
     increasing) trajectory C2 rises while H falls -- so the order-3 structure is cheapest to
     capture at maximum entropy and compounds with commitment: explore-then-exploit is forced.

 (5) Continuum: C2 ~ n^3 -> inf is a finite-grid quantity; the per-cell debt n^3/n -> the
     order-3 rung of the same finite-resolution tower whose order-4 rung is the mass (D-II).

sympy/numpy, exact; no torch.
"""
import sys
import sympy as sp
import numpy as np
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

# ---------------- (1) three faces ----------------
print("(1) C2 = sum 1/p^2 : three faces (cumulant L1 mass; squared Fisher norm)")
n = 4
p = sp.symbols(f'p1:{n+1}', positive=True)
phi = sum(pk*sp.log(pk) for pk in p)                  # negative entropy = the potential
# face (b): L1 mass of the diagonal third cumulant
T3 = [sp.simplify(sp.diff(phi, pk, 3)) for pk in p]   # d^3 phi/dp^3 = -1/p^2
C2_cum = sp.simplify(sum(sp.Abs(t) for t in T3))
chk("third cumulant T3_yyy = -1/p_y^2, so sum|T3| = sum 1/p^2",
    all(sp.simplify(T3[i] + 1/p[i]**2) == 0 for i in range(n))
    and sp.simplify(C2_cum - sum(1/pk**2 for pk in p)) == 0)
# face (c): tr(g^2), g = Hess(phi) = diag(1/p)
g = sp.diag(*[sp.diff(phi, pk, 2) for pk in p])        # = diag(1/p)
trg2 = sp.simplify((g*g).trace())
chk("g = Hess(phi) = diag(1/p); tr(g^2) = ||Hess(entropy)||_F^2 = sum 1/p^2",
    sp.simplify(g[0, 0] - 1/p[0]) == 0 and sp.simplify(trg2 - sum(1/pk**2 for pk in p)) == 0)

# ---------------- (2) Schur-convexity of C2 ----------------
print("(2) C2 strictly Schur-convex; min at barycenter = n^3; diverges at faces")
pi, pj = sp.symbols('pi pj', positive=True)
C2pair = 1/pi**2 + 1/pj**2
schur_C2 = sp.simplify((pi - pj)*(sp.diff(C2pair, pi) - sp.diff(C2pair, pj)))
# should equal 2 (pi-pj)^2 (pi^2+pi pj+pj^2)/(pi^3 pj^3) >= 0  (manifest SOS)
sos = sp.simplify(schur_C2 - 2*(pi - pj)**2*(pi**2 + pi*pj + pj**2)/(pi**3*pj**3))
chk("Schur-Ostrowski (p_i-p_j)(d_i-d_j)C2 = 2(p_i-p_j)^2(p_i^2+p_ip_j+p_j^2)/(p_i p_j)^3 >= 0 (SOS)",
    sos == 0)
for nn in (4, 6, 30):
    val = nn*(sp.Rational(1, nn))**(-2)                # n * n^2
    chk(f"C2(p_*) = n^3 at n={nn}: {int(val)} == {nn**3}", val == nn**3)
chk("C2 -> +inf as a coordinate -> 0 (face divergence: the debt diverges at commitment)",
    sp.limit(1/p[0]**2, p[0], 0, '+') == sp.oo)

# ---------------- (3) entropy Schur-concave ----------------
print("(3) entropy H = -phi strictly Schur-concave; max at barycenter")
Hpair = -(pi*sp.log(pi) + pj*sp.log(pj))
schur_H = sp.simplify((pi - pj)*(sp.diff(Hpair, pi) - sp.diff(Hpair, pj)))
# = -(pi-pj)(log pi - log pj) <= 0
chk("Schur-Ostrowski (p_i-p_j)(d_i-d_j)H = -(p_i-p_j)(log p_i - log p_j) <= 0 (Schur-concave)",
    sp.simplify(schur_H + (pi - pj)*(sp.log(pi) - sp.log(pj))) == 0)

# ---------------- (4) co-extremality + pay-early monotonicity ----------------
print("(4) co-extremality at p_*; explore-then-exploit forced (C2 up, H down on sharpening)")
# both gradients parallel to 1 at the barycenter (=> both stationary on the simplex there)
gradC2_star = [sp.diff(sum(1/pk**2 for pk in p), pk).subs({pk: sp.Rational(1, n) for pk in p}) for pk in p]
gradH_star = [sp.diff(-phi, pk).subs({pk: sp.Rational(1, n) for pk in p}) for pk in p]
chk("at p_*: grad C2 and grad H are both constant vectors (parallel to 1) => co-stationary",
    len(set(gradC2_star)) == 1 and len(set(gradH_star)) == 1)
# along a sharpening ray p(t) = (1-t) p_* + t e_1, n=6: C2 strictly up, H strictly down
m = 6
unif = np.full(m, 1.0/m); e1 = np.zeros(m); e1[0] = 1.0
ts = np.linspace(0, 0.9, 19)
C2t = np.array([np.sum(1.0/((1-t)*unif + t*e1)**2) for t in ts])
Ht = np.array([-np.sum(((1-t)*unif + t*e1)*np.log((1-t)*unif + t*e1)) for t in ts])
chk("along sharpening ray: C2(t) strictly increasing (debt compounds with certainty)",
    np.all(np.diff(C2t) > 0) and abs(C2t[0] - m**3) < 1e-9)
chk("along sharpening ray: H(t) strictly decreasing (short-term surprise spent)",
    np.all(np.diff(Ht) < 0) and abs(Ht[0] - np.log(m)) < 1e-9)
# pay-early: capturing structure at the start (t=0) costs the global minimum of C2 along the path
chk("pay-early optimum: argmin_t C2(p(t)) = 0 (cheapest capture is at max entropy / explore)",
    int(np.argmin(C2t)) == 0)

# ---------------- (5) the order tower: C2 is the order-3 rung; mass (D-II) is order-4 ----------------
print("(5) cumulant-debt tower: |T^(k)_y..y| = (k-2)!/p_y^(k-1); C2=order-3 rung, mass=order-4")
k = sp.symbols('k', integer=True, positive=True)
# verify the diagonal cumulant magnitudes for k=2,3,4 on phi = sum p log p
mags = {kk: sp.simplify(sp.Abs(sp.diff(p[0]*sp.log(p[0]), p[0], kk))) for kk in (2, 3, 4)}
chk("diagonal cumulant magnitudes 1/p (order2, Fisher), 1/p^2 (order3, C2), 2/p^3 (order4, mass)",
    sp.simplify(mags[2] - 1/p[0]) == 0 and sp.simplify(mags[3] - 1/p[0]**2) == 0
    and sp.simplify(mags[4] - 2/p[0]**3) == 0)

print("=" * 80)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("SURPRISE-DEBT THEOREM: C2(p)=sum 1/p^2 = blind cubic coupling (P4) = L1 third-cumulant mass")
print("= tr(g^2)=||Hess(entropy)||_F^2. Strictly Schur-convex, min n^3 at p_*; entropy Schur-concave,")
print("max at p_*. => maximizing short-term surprise (entropy/explore) IS minimizing the surprise")
print("debt; on any sharpening path C2 rises and H falls, so order-3 capture is cheapest at maximum")
print("entropy and compounds with commitment -- explore-then-exploit is forced by Schur-convexity.")
print("=" * 80)
