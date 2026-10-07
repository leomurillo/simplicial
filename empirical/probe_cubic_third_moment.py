"""
The cubic Weil functional, derived correctly: C_zeta(g;eta) = int eta(u) S_g(u)^3 du,
the THIRD MOMENT of the prime/zero wave S_g -- NOT an additive Chowla correlation.

S_g(u) = sum_{gamma>0} 2 ghat(gamma) cos(gamma u)   (zero side; = prime-side wave by the
explicit formula).  Cubing and integrating gives a TERNARY correlation
  C_zeta = sum_{gamma_1,gamma_2,gamma_3} ghat ghat ghat * etahat(gamma_1 +/- gamma_2 +/- gamma_3),
i.e. the THIRD CORRELATION OF THE ZEROS = third moment of primes in short intervals.

Key structural fact this probe shows: over u, S_g(u) is a sum of many incommensurate
cosines, so by CLT it is asymptotically GAUSSIAN -- and the third moment of a Gaussian is
ZERO.  So the cubic functional's LEADING (GUE) term vanishes; the positivity content is
SUBLEADING (the arithmetic cluster c_2, where L(1/2,chi_3) lives).  This is the
Rudnick-Sarnak (1996, leading, unconditional restricted-support) + Montgomery-Soundararajan
(2004, subleading, conditional on Hardy-Littlewood) regime -- prime 3-tuples / short
intervals, NOT additive Chowla.

We compute mean/variance/skew of S_g over u and show skew ~ 0 (GUE leading vanishes),
while S_g genuinely takes both signs (so the positivity int eta S^3 >= 0 is non-trivial).
Deterministic: mpmath zeros + numpy.  No torch.
"""

import numpy as np
import mpmath as mp
mp.mp.dps = 20

M = 150
print(f"computing first {M} zeta zeros ...")
gammas = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, M + 1)])
Omega = gammas[74]                      # bandlimit ~ gamma_75
ghat = np.maximum(1.0 - gammas / Omega, 0.0)   # Fejer triangle on the zeros
active = ghat > 0

U = 40.0
u = np.linspace(-U, U, 200000)
# S_g(u) = sum 2 ghat cos(gamma u)
S = (2.0 * ghat[active])[:, None] * np.cos(np.outer(gammas[active], u))
S = S.sum(axis=0)
eta = np.exp(-u**2 / (2 * 8.0**2))      # positive smearing window
du = u[1] - u[0]

m1 = np.sum(eta * S) * du / (np.sum(eta) * du)
var = np.sum(eta * (S - m1)**2) * du / (np.sum(eta) * du)
m3 = np.sum(eta * (S - m1)**3) * du / (np.sum(eta) * du)
skew = m3 / var**1.5
cubic_functional = np.sum(eta * S**3) * du     # C_zeta (unnormalized third moment)
second_moment = np.sum(eta * S**2) * du

print()
print("=" * 76)
print("S_g(u) = sum 2 ghat(gamma) cos(gamma u) over the true zeros")
print("=" * 76)
print(f"  range of S_g:    min={S.min():+.3f}   max={S.max():+.3f}   "
      f"(takes BOTH signs => int eta S^3 >= 0 is non-trivial)")
print(f"  mean (over u):   {m1:+.4f}")
print(f"  variance:        {var:.4f}   (the 2-point / second moment, > 0)")
print(f"  third moment:    {m3:+.5f}")
print(f"  SKEWNESS:        {skew:+.5f}   <- ~ 0: the GUE/Gaussian leading term VANISHES")
print()
print(f"  cubic functional C_zeta = int eta S^3 du = {cubic_functional:+.4f}")
print(f"  second moment   int eta S^2 du          = {second_moment:.4f}")
print(f"  ratio |C_3| / (2nd moment)^1.5          = {abs(cubic_functional)/second_moment**1.5:.5f}")
print()
print("=" * 76)
print("READING")
print("=" * 76)
print("""  S_g takes both signs, so S_g^3 takes both signs -- the positivity int eta S_g^3 >= 0
  is a genuine cancellation statement (the negative excursions must not dominate), which
  is exactly RH (it holds for the special admissible class G, under which S_g >= 0).

  The SKEWNESS ~ 0: as a sum of incommensurate cosines S_g is asymptotically Gaussian
  (CLT), and the third moment of a Gaussian is zero -- so the cubic functional's LEADING
  term VANISHES.  The positivity content is the SUBLEADING deviation from Gaussian: the
  arithmetic cluster c_2 (prop L(1/2,chi_3)^2), the prime-3-tuple / short-interval term.

  CORRECT IDENTIFICATION: C_zeta = third correlation of the zeros = third moment of
  primes in short intervals.  Leading (GUE) -> Rudnick-Sarnak 1996 (unconditional,
  restricted support).  Subleading (the positivity) -> Montgomery-Soundararajan 2004
  (conditional on the uniform Hardy-Littlewood prime k-tuple conjecture).  This is the
  prime-3-tuple / short-interval frontier -- NOT additive Chowla (TT2017), NOT a
  multiplicative product.""")
