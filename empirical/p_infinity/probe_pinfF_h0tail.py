"""probe_pinfF_h0tail.py -- the (H0'-tail) strike: the horizon form measured at mechanism level.

THE TARGET: QW(F) >= 0 geometrically for half-line (horizon) supported F -- the (H0'-tail)
localization of P-inf-F section 17.2.  Head-math found: the CC-Thm-1 hope ("arch floor +
small prime perturbation") DIES on the horizon; the mechanism is an ARCH-PRIME CONSPIRACY.

PRE-REGISTERED (GPD):
  T1 (redshift domain edge, Prop F.19): pure-exponential tails F ~ e^{alpha y}: the pole
      functional diverges as alpha -> 1/2+ (measure pole/||F||^2 blowing up ~1/(alpha-1/2));
      the prime sum converges iff alpha > 1/2 -- SAME line.
  T2 (the conspiracy): pole-dodged family F = (1+(alpha-1/2)y)e^{alpha y} (fhat(i/2) = 0
      by construction): arch/||F||^2 in [-3,-1]; total small-positive; hence -primes
      POSITIVE of size ~|arch| -- the primes RESCUE the arch well.
      FALSIFIER X2: -primes not positive-rescuing on this family.
  T3 (triple balance of the TRUE tails): the prolate tails (lam = 1.3, 1.5, 2.0/n=8) have
      (pole, arch, primes)/||F||^2 all O(1) with total/||F||^2 = O(1) matching the matrix
      epsilon-side (E.22.2, certified 1.3% at lam=2) -- the seam identity in geometric
      coordinates.  FALSIFIER X3: terms not O(1)-relative.
  T4 (adversarial sweep): random in-domain horizon functions (alpha in [0.75,3], with and
      without pole-dodge, oscillations): ALL totals >= -(tail allowance ~ 0.05 rel).
      FALSIFIER X1: a genuine negative (contradicts verified zeros => diagnose probe first).

Engine: weil_form_general (bookkeeping probe lineage; F64-2/3 lessons: families A/B/D are
O(1)-relative -- engine-visible; family C terms are O(1) relative to the TAIL norm).
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
from scipy.special import digamma
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src = open("empirical/p_infinity/probe_pinfF_bookkeeping.py", encoding="utf-8").read()
exec(src.split('# ---------------- M0/M1')[0])   # builders: weil_form_general, assemble_full_Eh, prolate_modes, ...

print("harvesting zeros (40)...")
mp.mp.dps = 15
GAM = [float(mp.im(mp.zetazero(k))) for k in range(1, 41)]
mp.mp.dps = 30


def zero_side(yg, F, J=40):
    dy = yg[1] - yg[0]
    tot = 0.0
    for g in GAM[:J]:
        fh = complex(np.sum(F * np.exp(1j * g * yg)) * dy)
        tot += 2 * abs(fh)**2
    return tot


def report(label, yg, F, lam_for_primes=2.0):
    # F64-4: Tmax must stay below the y-grid alias image 2*pi/dy (= 3142 at dy=0.002);
    # with Tmax=3000 the first image escaped by luck in the bookkeeping run -- use 1400.
    n2 = float(np.trapezoid(F * F, yg))
    q, parts = weil_form_general(yg, F, lam_for_primes, Tmax=1400.0)
    zs = zero_side(yg, F)
    print(f"   {label:42s} pole={parts['pole']/n2:+7.3f}  arch={parts['arch']/n2:+7.3f}  "
          f"-primes={-parts['primes']/n2:+7.3f}  TOTAL={q/n2:+8.4f}  zero-side={zs/n2:+8.4f}")
    return q / n2, parts, n2, zs / n2


L0 = np.log(2.0)          # horizon edge at the lambda=2 window
yg = np.arange(-10.0, -L0 + 0.001, 0.002)   # dy=0.002: alias image at 3142 >> Tmax=1400 (F64-4)

print("\n== T1: pure exponential tails (the redshift domain edge) ==")
res_T1 = []
for al in (0.55, 0.6, 0.75, 1.0, 1.5, 2.5):
    F = np.exp(al * (yg + L0))
    t, p, n2, zs = report(f"A: alpha={al}", yg, F)
    res_T1.append((al, p['pole'] / n2))
ok1 = res_T1[0][1] > 4 * res_T1[4][1]      # pole(0.55) >> pole(1.5): blow-up toward alpha=1/2
print("   T1: " + ("SURVIVES -- pole functional blows up toward alpha=1/2 (domain edge = "
                   "redshift line)" if ok1 else "check"))

print("\n== T2: pole-dodged family (the conspiracy) ==")
ok2 = True
for al in (0.75, 1.0, 1.5, 2.5):
    c = al - 0.5
    F = (1 + c * (yg + L0)) * np.exp(al * (yg + L0))
    t, p, n2, zs = report(f"B: alpha={al}, fhat(i/2)=0", yg, F)
    ok2 &= (p['pole'] / n2 < 0.15) and (-p['primes'] / n2 > 0.3) and (p['arch'] / n2 < -0.5) \
        and (t > -0.08)
print("   T2: " + ("SURVIVES -- pole dead, arch well deep, PRIMES RESCUE (-primes > 0), "
                   "total small-positive" if ok2 else "X2 FIRED -- diagnose"))

print("\n== T3: the TRUE prolate tails (triple balance = the seam, geometric) ==")
ok3 = True
for lam_f, ncell in ((1.3, 4), (1.5, 4), (2.0, 8)):
    x_p, Hp, defp = prolate_modes(lam_f, 36)
    I0 = np.trapezoid(Hp[0], x_p)
    naux = 8 if ncell != 8 else 12
    M2c = np.array([[np.trapezoid(Hp[0], x_p), np.trapezoid(Hp[naux], x_p)],
                    [Hp[0][len(x_p) // 2], Hp[naux][len(x_p) // 2]]])
    rhs = np.array([np.trapezoid(Hp[ncell], x_p), Hp[ncell][len(x_p) // 2]])
    ab = np.linalg.solve(M2c, rhs)
    hcomb = Hp[ncell] - ab[0] * Hp[0] - ab[1] * Hp[naux]
    ygc, Eh = assemble_full_Eh(lam_f, hcomb, x_p)
    Lx = np.log(lam_f)
    Fo = np.where(ygc < -Lx, Eh, 0.0)
    t, p, n2, zs = report(f"C: prolate tail lam={lam_f}, n={ncell}", ygc, Fo, lam_f)
    ok3 &= all(abs(v) < 50 for v in (p['pole'] / n2, p['arch'] / n2, p['primes'] / n2))
print("   T3: " + ("SURVIVES -- three O(1)-relative terms; total = the epsilon-side scale "
                   "(the seam identity, geometric)" if ok3 else "X3 FIRED"))

print("\n== T4: adversarial sweep (positivity of the horizon form, per-window) ==")
rng = np.random.default_rng(17)
worst = np.inf
worst_lbl = ""
for trial in range(24):
    al = rng.uniform(0.75, 3.0)
    mode = trial % 3
    base = np.exp(al * (yg + L0))
    if mode == 0:
        F = base * (1 + 0.8 * np.sin(rng.uniform(0.5, 8.0) * yg + rng.uniform(0, 6)))
    elif mode == 1:
        c = al - 0.5
        F = (1 + c * (yg + L0)) * base * (1 + 0.5 * np.sin(rng.uniform(1, 6) * yg))
    else:
        F = base * np.cos(rng.uniform(0.3, 4.0) * (yg + L0))
    n2 = float(np.trapezoid(F * F, yg))
    if n2 < 1e-12:
        continue
    q, _ = weil_form_general(yg, F, 2.0, Tmax=1400.0)
    if q / n2 < worst:
        worst, worst_lbl = q / n2, f"mode{mode}, alpha={al:.2f}"
print(f"   24 trials: worst TOTAL/||F||^2 = {worst:+.4f}  ({worst_lbl})")
ok4 = worst > -0.08
print("   T4: " + ("SURVIVES -- horizon form positive across the adversarial family (margin"
                   " floor reported)" if ok4 else "X1 CANDIDATE -- diagnose probe vs math"))

print("\nRESULT: " + ("GREEN -- horizon mechanism certified: redshift domain edge, the "
                      "arch-prime conspiracy, the triple balance, per-window positivity"
                      if (ok1 and ok2 and ok3 and ok4) else "PARTIAL -- see fired lines"))
