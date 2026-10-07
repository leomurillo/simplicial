#!/usr/bin/env python
"""
Benchmark #2 (Gamma/Mosco equi-coercivity of the Weil form) + the entropy-monotone
alternative.  numpy only (no torch).

PART 1 — Is the finite Weil quadratic form, as a Lambda-indexed family Q_Lambda, EQUI-COERCIVE?
  Weil's criterion: RH  <=>  Q(phi) = sum_{nontrivial rho} hat g(rho) >= 0 for every phi
  of positive type (g = phi * phi~), where on RH  Q(phi) = sum_gamma |phihat(gamma)|^2.
  Take phi supported in [-Lambda, Lambda]  (band-limited family PW_Lambda); cutoff = Lambda.
  Equi-coercivity (the hypothesis a Gamma/Mosco "positivity passes to the limit" theorem needs)
  means: inf_{||phi||_2 = 1} Q_Lambda(phi) >= c > 0, UNIFORMLY in Lambda.
  Decisive test: track the coercivity constant lambda_min(Lambda).
    - stays >= c > 0   => equi-coercive => soft Gamma/Mosco route gives the limit theorem.
    - -> 0             => NOT equi-coercive => soft route blocked; the leak direction is the
                          near-null mode, and we read off WHERE the margin escapes.

  Rigorous sub-result (needs no eigensolve): the DC mode phi_const = 1/sqrt(2 Lambda) on
  [-Lambda,Lambda], ||phi||_2 = 1, gives  phihat(gamma) = sqrt(2/Lambda) sin(gamma Lambda)/gamma,
  so  Q(phi_const) = 2 * sum_{gamma>0} (2/Lambda) sin^2(gamma Lambda)/gamma^2 <= (4/Lambda) * sum 1/gamma^2 -> 0.
  Hence inf Q_Lambda <= O(1/Lambda) -> 0 : equi-coercivity FAILS, with the escaping direction the
  lowest-frequency (DC / central zero-free-gap) mode.

PART 2 — The entropy-monotone alternative that does NOT need coercivity.
  Relative entropy of cutoff compressions is monotone in the cutoff (data-processing inequality)
  and >= 0 in the limit (Klein's inequality) -- automatically.  Demonstrated classically
  (KL under coarse-graining).  The program's task is to realize the Weil defect AS such a
  relative entropy of scale-compressions (extends N14: archimedean Weil = relative entropy).
"""
import numpy as np

# first 50 nontrivial zeta zeros (positive imaginary parts), standard values
GAMMA = np.array([
 14.134725142,21.022039639,25.010857580,30.424876126,32.935061588,
 37.586178159,40.918719012,43.327073281,48.005150881,49.773832478,
 52.970321478,56.446247697,59.347044003,60.831778525,65.112544048,
 67.079810529,69.546401711,72.067157674,75.704690699,77.144840069,
 79.337375020,82.910380854,84.735492981,87.425274613,88.809111208,
 92.491899271,94.651344041,95.870634228,98.831194218,101.317851006,
 103.725538040,105.446623052,107.168611184,111.029535543,111.874659177,
 114.320220915,116.226680321,118.790782866,121.370125002,122.946829294,
 124.256818554,127.516683880,129.578704200,131.087688531,133.497737203,
 134.756509753,138.116042055,139.736208952,141.123707404,143.111845808])

print("="*72)
print("PART 1 — equi-coercivity of the Weil form family Q_Lambda")
print("="*72)
print("central zero-free gap: no nontrivial zero with |gamma| <",
      f"{GAMMA[0]:.4f}  (the leak window)\n")

S2 = np.sum(1.0/GAMMA**2)             # sum 1/gamma^2 over the 50 positive zeros (tail tiny, ~1/gamma^2)
print(f"sum 1/gamma^2 (first 50 positive zeros) = {S2:.6f}   (converges; tail negligible)\n")

print("(a) DC-mode Rayleigh quotient  Q(phi_const)/||phi_const||^2  vs cutoff Lambda")
print("    [a rigorous UPPER BOUND on the coercivity constant lambda_min(Lambda)]")
print(f"    {'Lambda':>8} {'Q(DC)':>14} {'Q*Lambda':>12}")
for Lam in [1,2,4,8,16,32,64,128]:
    Q = 2.0*np.sum((2.0/Lam)*np.sin(GAMMA*Lam)**2/GAMMA**2)   # factor 2 for +/- gamma
    print(f"    {Lam:>8} {Q:>14.6e} {Q*Lam:>12.5f}")
print("    => Q(DC) ~ C/Lambda -> 0 : inf Q_Lambda -> 0, so the family is NOT equi-coercive.\n")

def phihat_cos(k, Lam, g):
    """FT at frequency g of cos(k*pi*t/Lam) on [-Lam,Lam] (even); k=0 is the constant."""
    if k == 0:
        return 2.0*np.sin(g*Lam)/g
    a = g - k*np.pi/Lam
    b = g + k*np.pi/Lam
    return np.sinc(a*Lam/np.pi)*Lam + np.sinc(b*Lam/np.pi)*Lam   # sin(x)/x = Lam*sinc(xLam/pi)

print("(b) coercivity constant lambda_min over a low-frequency cosine subspace of PW_Lambda")
print("    [Rayleigh-min over a subspace >= true lambda_min; if THIS -> 0, true -> 0 too]")
print(f"    {'Lambda':>8} {'K(basis)':>9} {'lambda_min':>14} {'argmin peak k':>14}")
for Lam in [2,4,8,16]:
    K = min(int(Lam*GAMMA[-1]/np.pi), 14)        # low-freq cap (keep < #zeros)
    ks = np.arange(0, K+1)
    PH = np.array([phihat_cos(k, Lam, GAMMA) for k in ks])      # (K+1, Nzeros), real
    M = 2.0*(PH @ PH.T)                                          # form matrix (factor 2 for +/-)
    gnorm = np.array([2.0*Lam] + [Lam]*(K))                      # Gram diag (||cos||^2)
    Gm12 = 1.0/np.sqrt(gnorm)
    Mn = M*np.outer(Gm12, Gm12)                                  # G^{-1/2} M G^{-1/2}
    w, V = np.linalg.eigh(Mn)
    vmin = np.abs(V[:, 0])
    peak = int(np.argmax(vmin))
    print(f"    {Lam:>8} {K:>9} {w[0]:>14.6e} {peak:>14}")
print("    => lambda_min -> 0 and the minimizer peaks at k=0 (the lowest frequency):")
print("       the margin leaks into the DC / central-gap / archimedean-end mode.\n")

print("="*72)
print("PART 2 — relative entropy of compressions is monotone in the cutoff (for free)")
print("="*72)
print("Mechanism: data-processing inequality (KL non-increasing under coarse-graining)")
print("+ Klein's inequality (KL >= 0). No equi-coercivity required -- the exact gap Part 1 hits.\n")

rng = np.random.default_rng(0)
n = 64
p = rng.random(n)**2 + 0.05; p /= p.sum()
q = rng.random(n)**2 + 0.05; q /= q.sum()
def KL(a, b):
    m = a > 0
    return float(np.sum(a[m]*np.log(a[m]/b[m])))
def coarse(v, m):                                  # merge n bins into m by summation
    idx = (np.arange(n)*m)//n
    out = np.zeros(m)
    np.add.at(out, idx, v)
    return out
print(f"    {'#bins m (cutoff)':>16} {'D_m = KL(p_m||q_m)':>20} {'monotone?':>10}")
prev = -1.0
mono = True
for m in [1,2,4,8,16,32,64]:
    D = KL(coarse(p,m), coarse(q,m))
    ok = (D >= prev - 1e-12) and (D >= -1e-12)
    mono = mono and ok
    print(f"    {m:>16} {D:>20.6f} {('yes' if ok else 'NO'):>10}")
    prev = D
print(f"\n    D_m monotonically increases to D_inf = KL(p||q) = {KL(p,q):.6f} >= 0,")
print(f"    each D_m >= 0, monotone-in-cutoff verified: {mono}")
print("    => a positivity-preserving-limit certificate that needs NO coercivity.")
print("       Program obligation: realize the Weil functional/defect as KL(rho_Lambda||sigma_Lambda)")
print("       of scale/cutoff compressions (extends N14: archimedean Weil = relative entropy).")
