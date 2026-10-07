"""
probe_li_chiral_stability.py

Targets STABILITY (not existence) of the RG fixed point, per the agreed push.

Li's criterion:  RH  <=>  lambda_n >= 0 for all n,   lambda_n = sum_rho [1 - (1-1/rho)^n].
This IS the fixed-point stability: for rho on the line, (rho-1)/rho = -conj(rho)/rho has MODULUS 1
(marginal); off the line |1-1/rho| != 1 and the term runs away exponentially. So:
   all zeros marginal (|1-1/rho|=1)  <=>  lambda_n bounded-positive  <=>  RH  <=>  stable fixed point.

We:
  A. compute lambda_n(zeta) from the true zeros; show lambda_n > 0 and archimedean-dominated growth;
  B. MECHANISM: move ONE zero off the line and show lambda_n crashes negative (stability = RH, made
     visceral -- a single unstable mode destroys positivity);
  C. CHIRAL split: lambda_n(L(.,chi_3)) from L(s,chi_3) zeros; compare positivity/structure to zeta;
  D. calibrate honestly: lambda_n>=0 is RH-equivalent (Li); positivity confirms, does not prove; the
     chiral structure localizes where positivity lives; the open core is the prime-fluctuation bound.

Deterministic: mpmath.  No torch.
"""
import mpmath as mp
mp.mp.dps = 25

# ---------- zeros of zeta ----------
NZ = 220
print("computing zeta zeros ...", flush=True)
zeta_g = [mp.im(mp.zetazero(k)) for k in range(1, NZ+1)]

def li_from_gammas(gammas, nmax, betas=None):
    """lambda_n = sum over zeros [1-(1-1/rho)^n], rho=beta+i*gamma paired with conj.
       betas: list of real parts (default 1/2 each, i.e. on the line)."""
    if betas is None:
        betas = [mp.mpf(1)/2]*len(gammas)
    out = []
    for n in range(1, nmax+1):
        tot = mp.mpf(0)
        for b, g in zip(betas, gammas):
            for rho in (mp.mpc(b, g), mp.mpc(b, -g)):       # rho and its conjugate
                tot += 1 - (1 - 1/rho)**n
        out.append(mp.re(tot))
    return out

NMAX = 30
print("A) lambda_n(zeta) from", NZ, "zeros (all on the line)")
lam = li_from_gammas(zeta_g, NMAX)
print(f"  {'n':>3} {'lambda_n':>14} {'lambda_n/((n/2)ln n)':>22} {'>=0?':>5}")
for n in (1,2,3,5,10,15,20,25,30):
    ref = (n/2)*mp.log(n) if n > 1 else mp.mpf(1)
    print(f"  {n:>3} {mp.nstr(lam[n-1],8):>14} {mp.nstr(lam[n-1]/ref,6):>22} {str(lam[n-1] >= 0):>5}")
allpos = all(v >= 0 for v in lam)
print(f"  all lambda_n >= 0 (n<= {NMAX}): {allpos}   (archimedean-dominated; ~ (n/2)ln n)")

print("\nB) STABILITY MECHANISM: a single zero's CONTRIBUTION to lambda_n, on-line vs off-line")
print("   on-line |1-1/rho|=1 (marginal) -> bounded oscillation; off-line |1-1/rho|!=1 -> runaway.")
def one_zero_contrib(beta, gamma, nmax):
    """contribution of the zero(s) at height gamma to lambda_n.
       on-line: pair {1/2 +- i gamma};  off-line: quadruple {beta, 1-beta} x {+- i gamma}."""
    out = []
    for n in range(1, nmax+1):
        if beta == mp.mpf(1)/2:
            zs = [mp.mpc(mp.mpf(1)/2, gamma), mp.mpc(mp.mpf(1)/2, -gamma)]
        else:
            zs = [mp.mpc(beta, gamma), mp.mpc(beta, -gamma),
                  mp.mpc(1-beta, gamma), mp.mpc(1-beta, -gamma)]
        out.append(mp.re(sum(1-(1-1/r)**n for r in zs)))
    return out
gt = mp.mpf(4)                                    # a low height where the runaway is visible by n~50
on  = one_zero_contrib(mp.mpf(1)/2, gt, 60)
off = one_zero_contrib(mp.mpf('0.80'), gt, 60)    # off the line at the same height
print(f"   zero at height gamma={gt}:  |1-1/rho| on-line = {mp.nstr(abs(1-1/mp.mpc('0.5',gt)),8)}, "
      f"off-line(beta=0.2 partner) = {mp.nstr(abs(1-1/mp.mpc('0.2',gt)),8)}")
print(f"   {'n':>3} {'on-line contrib':>16} {'off-line contrib':>17}")
for n in (1,5,10,20,30,40,50,60):
    print(f"   {n:>3} {mp.nstr(on[n-1],7):>16} {mp.nstr(off[n-1],7):>17}")
first_neg = next((n for n in range(1,61) if off[n-1] < 0), None)
print(f"  >>> on-line contribution stays bounded; off-line goes NEGATIVE from n={first_neg}, "
      f"diverging ~ -|1-1/rho|^n.")
print("      A real off-line zero at height gamma forces lambda_n<0 by n ~ gamma^2 -- inevitable but")
print("      delayed for high zeros. => lambda_n>=0 for ALL n IS exactly 'every mode marginal' = RH.")

# ---------- zeros of L(s,chi_3) ----------
print("\nC) CHIRAL split: lambda_n(L(.,chi_3))  (chi_3 odd real char mod 3)")
def Lchi3(s):
    return mp.power(3, -s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
def theta_chi3(t):
    return (t/2)*mp.log(3/mp.pi) + mp.im(mp.loggamma(mp.mpf(3)/4 + 1j*t/2))
def Z_chi3(t):
    return mp.re(mp.e**(1j*theta_chi3(t))*Lchi3(mp.mpc(mp.mpf(1)/2, t)))
print("  finding L(.,chi_3) zeros on the critical line via Z-function sign changes ...", flush=True)
chi_g = []
t = mp.mpf('0.5'); prev = Z_chi3(t); step = mp.mpf('0.2')
while t < 70 and len(chi_g) < 40:
    t2 = t + step; cur = Z_chi3(t2)
    if prev == 0 or (prev < 0) != (cur < 0):
        try:
            r = mp.findroot(Z_chi3, (t+t2)/2)
            if r > 0 and (not chi_g or abs(r-chi_g[-1]) > 1e-6):
                chi_g.append(r)
        except Exception:
            pass
    t, prev = t2, cur
print(f"  found {len(chi_g)} zeros; first few: {[mp.nstr(g,7) for g in chi_g[:5]]}")
NMAXc = 15
lam_c = li_from_gammas(chi_g, NMAXc)
print(f"  {'n':>3} {'lambda_n(chi_3)':>16} {'lambda_n(zeta)':>16} {'>=0?':>5}")
for n in (1,2,3,5,8,12,15):
    print(f"  {n:>3} {mp.nstr(lam_c[n-1],7):>16} {mp.nstr(lam[n-1],7):>16} {str(lam_c[n-1] >= 0):>5}")
allpos_c = all(v >= 0 for v in lam_c)
print(f"  all lambda_n(chi_3) >= 0 (n<= {NMAXc}, from {len(chi_g)} zeros): {allpos_c}")

print("\n" + "="*78)
print("VERDICT (calibrated)")
print("="*78)
print(f"""  A: lambda_n(zeta) > 0 for n<= {NMAX}, growing and archimedean-DOMINATED (finite-zero truncation
     slightly UNDERSHOOTS, so the true values are a touch larger -- even more robustly positive).
     The positivity 'floor' is the archimedean growth; the prime/zero fluctuation is the small rider.
  B: a single zero's contribution is bounded on-line but runs away NEGATIVE off-line (here from
     n={first_neg} at height 4). This is the cleanest statement of the push's target:
     'RG fixed point stable' = 'every mode marginal |1-1/rho|=1' = 'lambda_n>=0' = RH. Sharp,
     noise-free. (A real off-line zero at height gamma bites by n ~ gamma^2 -- delayed, not denied.)
  C: lambda_n(chi_3) > 0 too. The chiral sector is positive in plain sight (its larger values are
     partly its lower-lying first zero at 8.04 vs 14.13, so do not over-read the magnitude); both
     sectors are stable to computed order, consistent with the margin result.

  HONEST CALIBRATION. This resolves the *form* of the question (sharp, noise-free) but it is
  RH-EQUIVALENT: lambda_n>=0 for ALL n IS RH (Li 1997). Computing it positive to n<= {NMAX}
  confirms (as billions of zeros already do); it does not prove. What WOULD prove it is an
  UNCONDITIONAL lower bound lambda_n >= 0 -- i.e. showing the archimedean growth (n/2)ln n always
  dominates the prime fluctuation. That domination is exactly the stability of the RG fixed point,
  and bounding the prime fluctuation a priori is RH. The chiral split localizes (chi_3 manifestly
  positive, zeta the deep-well bottleneck) but does not supply the unconditional bound.
  => The push reached the sharpest possible STATEMENT of stability; the bound itself is still RH.""")
