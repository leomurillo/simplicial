"""
#9 stress-test: are the cubic off-line "teeth" (c_2 < 0, chirality-anchored by L(1/2,chi_3))
UNIFORM in height gamma_0, or do they decay? Uniform => a single witness detects off-line
zeros at all heights (closure-enabling); decaying => height-local only (forecloses uniform
closure without the primorial-EH input).

The normalization-invariant relative cluster margin (diez §2):
  R(gamma_0, sigma_0) = c_2 / C_Lambda(0),
  c_2          = 24 eta''(3i gamma_0) + 72 eta''(i gamma_0)     (diez cluster delta^2 coeff)
  C_Lambda(0)  = 16 eta(3i gamma_0)  + 48 eta(i gamma_0)        (delta=0 baseline, (8,8,24,24) grouping)
with Gaussian smearing eta(z)=exp(-sigma_0^2 z^2/2), eta''(z)=sigma_0^2(sigma_0^2 z^2 -1)eta(z).
The common g~^3 cluster factor cancels in the ratio.

Clean structural fact this probe exhibits: with u := sigma_0 * gamma_0,
  eta(i b gamma_0)   = exp(b^2 u^2 / 2),    eta''(i b gamma_0) = sigma_0^2(-b^2 u^2 -1) eta(...)
so the GROWING exponentials CANCEL in R, leaving
  R(gamma_0,sigma_0) = sigma_0^2 * f(u),   f(u) = [24(-9u^2-1)e^{9u^2/2}+72(-u^2-1)e^{u^2/2}]
                                                   / [16 e^{9u^2/2} + 48 e^{u^2/2}].
f(u) -> -1.5 (u->0),  f(u) -> -13.5 u^2 (u->inf). R is MONOTONIC in sigma_0 (no interior max),
so |R_opt| = sigma_max(gamma_0)^2 * |f(sigma_max*gamma_0)|. The height-uniformity question
reduces ENTIRELY to the admissible smearing ceiling sigma_max(gamma_0):
   sigma_max ~ 1/gamma_0       => |R_opt| ~ gamma_0^{-2}      DECAY (forecloses)
   sigma_max ~ 1/log gamma_0   => |R_opt| ~ gamma_0^2/(log)^4 GROWTH (closure-enabling)
   sigma_max ~ const           => |R_opt| ~ gamma_0^2         GROWTH
This probe verifies the cancellation/structure and shows the reduction.
numpy. No torch.
"""
import numpy as np

def R(gamma0, sigma0):
    s2 = sigma0**2
    def eta(b):   return np.exp(0.5*s2*(b*gamma0)**2)            # eta(i b gamma0)
    def etapp(b): return s2*(-s2*(b*gamma0)**2 - 1)*eta(b)        # eta''(i b gamma0)
    c2   = 24*etapp(3) + 72*etapp(1)
    base = 16*eta(3)   + 48*eta(1)
    return c2/base

def f(u):
    num = 24*(-9*u**2-1)*np.exp(4.5*u**2) + 72*(-u**2-1)*np.exp(0.5*u**2)
    den = 16*np.exp(4.5*u**2) + 48*np.exp(0.5*u**2)
    return num/den

print("="*82)
print("#9: relative cluster margin R = c_2/C_Lambda(0) — structure and height-uniformity")
print("="*82)
print("\n(1) the exponentials cancel: R(gamma0,sigma0) = sigma0^2 * f(sigma0*gamma0)")
print(f"  {'gamma0':>7} {'sigma0':>7} {'u=s*g':>7} {'R direct':>12} {'sigma0^2 f(u)':>14}")
for gamma0 in [14.13, 100, 1000]:
    for sigma0 in [0.5/gamma0, 2.0/gamma0, 1.0/np.log(gamma0)]:
        u=sigma0*gamma0
        print(f"  {gamma0:>7.1f} {sigma0:>7.4f} {u:>7.3f} {R(gamma0,sigma0):>12.4e} {sigma0**2*f(u):>14.4e}")

print("\n(2) f(u): bounded ratio (-1.5 at u->0, ~ -13.5 u^2 at u->inf)")
print(f"  {'u':>6} {'f(u)':>10}")
for u in [0.1,0.5,1,2,3,5]:
    print(f"  {u:>6.1f} {f(u):>10.3f}")

print("\n(3) optimal teeth |R_opt| under three candidate admissibility ceilings sigma_max(gamma0)")
print(f"  {'gamma0':>8} {'~1/g (decay)':>14} {'~1/log g':>14} {'~const=0.1':>12}")
for gamma0 in [14.13, 50, 200, 1000, 5000]:
    r_inv  = abs(R(gamma0, 2.0/gamma0))          # sigma_max ~ 1/gamma0
    r_log  = abs(R(gamma0, 1.0/np.log(gamma0)))  # sigma_max ~ 1/log gamma0
    r_con  = abs(R(gamma0, 0.1))                 # sigma_max ~ const
    print(f"  {gamma0:>8.1f} {r_inv:>14.4e} {r_log:>14.4e} {r_con:>12.4e}")

print()
print("="*82)
print("VERDICT — #9 reduces to one scaling, not cleanly settled (unlike #34)")
print("="*82)
print("""  STRUCTURE (clean): the chirality-anchored off-line margin is R = sigma0^2 * f(sigma0*gamma0)
  with f bounded between -1.5 and -13.5u^2; R is MONOTONE increasing in sigma0 (the witness
  wants the widest admissible smearing). So the height-uniformity of the teeth is ENTIRELY
  controlled by the admissible smearing ceiling sigma_max(gamma0):
    - sigma_max ~ 1/gamma0  => teeth DECAY ~ gamma0^{-2}  (the earlier workflow finding;
      'witness infinitely fine-tuned to one height') => FORECLOSES uniform-in-height closure;
    - sigma_max ~ 1/log gamma0 or const => teeth GROW => would be closure-enabling.
  (Column (3) shows the three regimes numerically: 1/gamma0 collapses, the other two grow.)

  HONEST: unlike #34 (cleanly settled NEGATIVE by a condition-number bound), #9 does NOT cleanly
  settle here. It reduces to a single, sharply-stated open sub-question: what is the admissible
  smearing ceiling sigma_max(gamma0) for the cubic witness, set by the diez §2.5 bulk-vs-cluster
  control at VARYING height? The bulk (non-cluster zeros within sigma_0 of gamma_0, ~ sigma_0 log
  gamma_0 of them) must not swamp the cluster's negative c_2 delta^2. If that forces sigma_max ~
  1/gamma_0, #9's teeth decay and it conserves difficulty; if sigma_max ~ 1/log gamma_0 is
  admissible, the teeth grow and #9 becomes a genuinely uniform off-line detector. THIS bulk-
  control-at-height is the decidable next sub-question — a real, narrow, analytic problem in the
  diez cluster framework, not visibly RH-equivalent on its face.""")
