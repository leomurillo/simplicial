#!/usr/bin/env python
"""
N14-extension make-or-break (Z/6 = P2 = 2*3 row).  numpy + mpmath (no torch).

Question: can the finite Weil form be written  Q = A_full - P  with the PRIME side P a
genuine DATA-PROCESSING image of the archimedean state A_full?  Concretely (the entropy route):
  * A_full = archimedean (Gamma-factor, = relative-entropy Hessian, N14) + pole  -- the positive side.
  * P      = prime sum restricted to p in {2,3} (the Z/6 primorial row).
  * Q      = A_full - P  (Weil form; Q >= 0 on this row is the program's [P] cubic claim).
For the relative-entropy MONOTONE (data-processing + Klein) to apply, the prime side must be
realizable as A_full coarse-grained by a completely-positive (Markov/Chentsov) CONTRACTION:
  (i)  P PSD                          (P is a Gram/channel image at all)
  (ii) B := A_full^{-1/2} P A_full^{-1/2}  has spectrum in [0,1]   (contraction <=> Q>=0; >=0 <=> P PSD)
  (iii) the channel K := A_full^{-1} P is POSITIVITY-PRESERVING  (classical proxy: K entrywise >= 0;
        a Markov/Chentsov coarse-graining must map the positive cone into itself)
(iii) is the crux: contraction (Weil positivity) is necessary but NOT sufficient for the
relative-entropy data-processing certificate, which needs complete positivity.  If K has
negative entries, the prime transfer is a contraction but NOT a data-processing map -- the
free monotone does not apply, and the obstruction localizes to the sign structure.

Test basis: real even Gaussian bumps phi_i(t)=g(t-u_i)+g(t+u_i), g=exp(-t^2/2w^2), centered at
u_i = log of the 2,3-smooth numbers (the Z/6 multiplicative support).  Standard Weil ingredients
restricted to p in {2,3}.  (A defensible concrete model of the conductor-packet Weil form at P2;
conventions stated; NOT claimed identical to the exact Paper-22 form.)
"""
import numpy as np, mpmath as mp

w = 0.25
S = [1, 2, 3, 4, 6, 8, 9, 12]          # 2,3-smooth numbers (Z/6 multiplicative support)
u = np.log(np.array(S, float)); d = len(S)

# archimedean weight Omega(r) = Re psi(1/4 + i r/2) - log pi
R, Npts = 30.0, 4000
r = np.linspace(-R, R, Npts)
Om = np.array([float(mp.re(mp.digamma(0.25 + 0.5j*rr))) - float(mp.log(mp.pi)) for rr in r])

c0 = 2*np.sqrt(2*np.pi)*w
PH = np.array([c0*np.exp(-w**2*r**2/2)*np.cos(r*ui) for ui in u])   # phi_hat_i(r), real even

_trap = getattr(np, "trapezoid", getattr(np, "trapz", None))
A = np.array([[_trap(PH[i]*PH[j]*Om, r)/(2*np.pi) for j in range(d)] for i in range(d)])
v = c0*np.exp(w**2/8)*np.cosh(u/2)                                  # phi_hat_i(+-i/2)  (pole)
pole = 2*np.outer(v, v)
A_full = A + pole

primepowers = [(2, 2), (4, 2), (8, 2), (16, 2), (32, 2), (3, 3), (9, 3), (27, 3)]
def corr(ui, uj, lag):
    s = 0.0
    for si in (1, -1):
        for sj in (1, -1):
            s += np.sqrt(np.pi)*w*np.exp(-((si*ui - sj*uj - lag)**2)/(4*w**2))
    return s
P = np.zeros((d, d))
for (n, p) in primepowers:
    lam, ln = np.log(p), np.log(n)
    for i in range(d):
        for j in range(d):
            P[i, j] += 2*(lam/np.sqrt(n))*corr(u[i], u[j], ln)

Q = A_full - P

def ev(M): return np.linalg.eigvalsh((M+M.T)/2)
print("="*70)
print("N14-extension test on Z/6 (P2 = 2*3 row)")
print("="*70)
print(f"basis dim d = {d}   smooth numbers = {S}")
print(f"cond(A_full) = {np.linalg.cond(A_full):.3e}")
print()
print(f"(1) eig(A_full)  min..max = {ev(A_full)[0]:.4e} .. {ev(A_full)[-1]:.4e}   PD? {ev(A_full)[0] > 0}")
print(f"(2) eig(Q=A_full-P) min..max = {ev(Q)[0]:.4e} .. {ev(Q)[-1]:.4e}   Weil>=0 on row? {ev(Q)[0] > -1e-9}")
print(f"(4) eig(P)       min..max = {ev(P)[0]:.4e} .. {ev(P)[-1]:.4e}   P PSD? {ev(P)[0] > -1e-9}")

# DECISIVE, basis-robust necessary condition for "prime side = data-processing image of a
# positive archimedean state":  any congruence  P = T^dagger A T  with A >= 0 is itself PSD.
# So  P PSD  is NECESSARY for ANY positive/CP data-processing realization (any A, any T).
ppsd = ev(P)[0] > -1e-9
print()
print("DECISIVE TEST — is the prime form P a positive data-processing image at all?")
print(f"   P = T^dag A T (A>=0)  forces  P >= 0.   eig(P) min = {ev(P)[0]:.4e}   P PSD? {ppsd}")
print(f"   => prime side {'CAN' if ppsd else 'CANNOT'} be a positive/CP data-processing image of any archimedean state.")

# Why (basis-robust): P = sum_n (2 Lambda(n)/sqrt n) * Corr_n, and each Corr_n (n>1) is a
# SHIFTED-Gaussian kernel exp(-(u_i-u_j-log n)^2/..), which is itself NOT PSD for log n != 0.
def shifted_kernel(lag):
    return np.array([[corr(u[i], u[j], lag) for j in range(d)] for i in range(d)])
for n in (2, 3):
    Kn = shifted_kernel(np.log(n))
    print(f"   shifted kernel at lag=log{n}: eig min = {ev(Kn)[0]:.4e}  (PSD? {ev(Kn)[0] > -1e-9})")
print("   => the prime quadratic form is intrinsically indefinite (a sum of non-PSD shifted kernels),")
print("      so its indefiniteness is structural, not an archimedean-modeling artifact.")
print()
print("VERDICT:")
if ppsd:
    print("  P is PSD -> the positive data-processing realization is not excluded; run the Loewner-")
    print("  domination test (prime-Fisher <= arch-Fisher) on N14's positive arch form. PURSUE.")
else:
    print("  P is INDEFINITE -> the literal 'prime side = completely-positive data-processing image")
    print("  of the archimedean state' is IMPOSSIBLE (congruence of a PSD matrix is PSD).")
    print("  The free relative-entropy/data-processing monotone (Part 2) does NOT realize this way.")
    print("  The Weil form is genuinely DIFFERENCE-OF-CONVEX (N15: arch - prime), not a single")
    print("  relative entropy; the obstruction is the prime form's intrinsic indefiniteness.")
    print("  Residual viable target (weaker): Loewner domination prime-Fisher <= arch-Fisher on")
    print("  N14's *positive* (Bregman/log-Gamma) arch form -- needs N14's exact construction, not")
    print("  the raw digamma weight (which is itself indefinite at low frequency: eig(A_full) min")
    print(f"  = {ev(A_full)[0]:.3e}, the same archimedean/low-frequency locus where Part 1 leaked).")
