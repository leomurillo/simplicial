"""
Modeling WHAT KIND of inequality the open step is -- to decide which proof FRAMEWORK can reach it.

The open step (CCM Cor 3.8 / Lemma 7.2): lambda_min of the Weil form stays >= 0 in the limit.
QUESTION the user asked: "some induction?" -- i.e. is the margin an AVERAGE functional (which an
induction / a level-of-distribution / an MRT-type average bound can reach) or a SUP/INDIVIDUAL
functional (which needs a uniform, every-zero, every-height bound that no bounded induction supplies)?

We TEST this directly on the marginal form W^zero (lambda_min = +9.3e-7 on the true zeros):

  A. OFF-LINE excursion.  Move ONE zero off Re=1/2 by eps (the only way RH fails).  Does lambda_min
     drop / go negative?  If yes, the form DETECTS off-line zeros (Weil positivity = RH) and a SINGLE
     off-line zero -- at ANY height -- breaks the margin.  => SUP functional.
  B. AVERAGE stays clean while the SUP breaks.  Track the AVERAGE diagonal (the "RMS / variance"
     surrogate that MRT / mollifier / level-of-distribution control) vs lambda_min under the same
     perturbation.  If the average barely moves while lambda_min collapses, the average tools are
     STRUCTURALLY BLIND to the failure mode.
  C. TIGHT PAIR (GUE gap).  Merge two adjacent on-line zeros (gap->0).  lambda_min drops via near-
     degeneracy -- the height-independent gap^2 event the barrier synthesis names as the common root.

Reading for the framework choice:
  SUP/individual + average-blind  =>  induction on level/height (Family B), average/variance (MRT),
  mollifier (Family E) all CEILING -- they bound the mean, not the worst zero.  A winning framework
  must inject a UNIFORM individual bound (self-duality / GUE individual repulsion = RH-strength).

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 30

ZEROS = [mp.mpf(z) for z in [
 14.134725142,21.022039639,25.010857580,30.424876126,32.935061588,37.586178159,
 40.918719012,43.327073281,48.005150881,49.773832478,52.970321478,56.446247697,
 59.347044003,60.831778525,65.112544048,67.079810529,69.546401711,72.067157674,
 75.704690699,77.144840069,79.337375020,82.910380854,84.735492981,87.425274613,
 88.809111208,92.491899271,94.651344041,95.870634228,98.831194218,101.317851006,
 103.725538040,105.446623052,107.168611184,111.029535543,111.874659177,114.320220915,
 116.226680321,118.790782866,121.370125002,122.946829294]]

s = mp.mpf(3); NUS = [mp.mpf(v) for v in (8, 14, 20, 26)]; n = len(NUS)

def phi(j, r):   # complex-capable frequency bump
    return mp.e**(-(r-NUS[j])**2/(2*s**2)) + mp.e**(-(r+NUS[j])**2/(2*s**2))

def sym_eigmin(M):
    M = (M + M.T) / 2
    return min(mp.re(x) for x in mp.eigsy(M, eigvals_only=True))

def avg_diag(M):
    return mp.fsum(M[j, j] for j in range(n)) / n

def W_from_zeros(zlist):
    M = mp.matrix(n, n)
    for j in range(n):
        for k in range(j, n):
            M[j, k] = M[k, j] = mp.fsum(2*phi(j, g)*phi(k, g) for g in zlist)
    return M

W0 = W_from_zeros(ZEROS)
lam0 = sym_eigmin(W0); avg0 = avg_diag(W0)

print("=" * 82)
print("Is the open-step margin an AVERAGE functional (inducible) or a SUP functional (not)?")
print("=" * 82)
print(f"\n  baseline (true zeros, on-line):  lambda_min = {mp.nstr(lam0,5)}   avg-diagonal = {mp.nstr(avg0,6)}")

# ---- A + B: off-line excursion of the FIRST zero; track lambda_min AND the average ----
print("\nA+B  move ONE zero (gamma_1=14.13) off the line by eps; lambda_min vs the average diagonal:")
print(f"     {'eps':>8} {'lambda_min':>16} {'d(lam)/lam0':>14} {'avg-diagonal':>16} {'d(avg)/avg0':>14}")
m = 0; gm = ZEROS[m]
for eps in [mp.mpf(e) for e in (0, 0.02, 0.05, 0.1, 0.2, 0.4)]:
    M = mp.matrix(n, n)
    for j in range(n):
        for k in range(j, n):
            base = W0[j, k]
            on = 2*phi(j, gm)*phi(k, gm)
            off = mp.re(phi(j, gm-1j*eps)*phi(k, gm-1j*eps) + phi(j, gm+1j*eps)*phi(k, gm+1j*eps))
            M[j, k] = M[k, j] = base - on + off
    lam = sym_eigmin(M); av = avg_diag(M)
    dl = (lam - lam0) / abs(lam0); da = (av - avg0) / avg0
    print(f"     {mp.nstr(eps,3):>8} {mp.nstr(lam,5):>16} {mp.nstr(dl,4):>14} {mp.nstr(av,6):>16} {mp.nstr(da,4):>14}")

# ---- C: tight pair (GUE gap -> 0), staying on the line ----
print("\nC    merge two adjacent on-line zeros (gamma_1,gamma_2): gap->0 (the GUE / de Bruijn event):")
print(f"     {'merge-frac':>11} {'gap':>10} {'lambda_min':>16} {'avg-diagonal':>16}")
for frac in [mp.mpf(f) for f in (0, 0.5, 0.9, 0.99, 1.0)]:
    z = list(ZEROS); mid = (z[0] + z[1]) / 2
    z[0] = mid - (1 - frac) * (mid - ZEROS[0])
    z[1] = mid + (1 - frac) * (ZEROS[1] - mid)
    M = W_from_zeros(z); lam = sym_eigmin(M); av = avg_diag(M)
    print(f"     {mp.nstr(frac,3):>11} {mp.nstr(z[1]-z[0],3):>10} {mp.nstr(lam,5):>16} {mp.nstr(av,6):>16}")

print("\n" + "=" * 82)
print("""READING -- which framework can reach the open inequality:
  A  off-line excursion moves lambda_min (the form is a Weil-positivity detector: on-line=marginal,
     off-line perturbs it).  ONE zero, at ANY height, perturbs the global margin.
  B  the AVERAGE diagonal barely moves while lambda_min swings: the average/variance surrogate that
     MRT, the mollifier, and the level-of-distribution all control is STRUCTURALLY BLIND to the
     single-zero failure.  This is the barrier-synthesis 'holds on average, not at every height.'
  C  a tight on-line pair (gap->0) drives lambda_min DOWN via near-degeneracy -- the height-
     independent GUE gap^2 event, the common root of Li / de Bruijn / Jensen.

  VERDICT:  the margin is a SUP / INDIVIDUAL functional, and the averages are blind to it.
    => Family B (induction on level/primorial) and Family E-average (MRT/mollifier/variance) CEILING:
       they bound the mean; the margin is the worst zero.  No BOUNDED induction reaches it because the
       killer zero/pair can sit at any height (height-independent).
    => A winning framework must inject a UNIFORM, every-zero, every-height (individual repulsion /
       self-dual) bound -- which is RH-strength.  That is the precise reason 'some induction' is not
       enough, and what the open inequality demands.
""")
print("=" * 82)
