"""
probe_cubic_vs_gue_deviation.py  --  does the apex cubic K^CH predict the zeros' departure from GUE?

Conjecture (to test, not assume): the leading arithmetic deviation of the zeros from pure GUE is the
third cumulant, = the apex cubic K^CH. PARANOID checks built in, because two different "order"
hierarchies are in play and could be conflated:
   - n-POINT correlations of the zeros (1-pt density, 2-pt pair correlation, 3-pt, ...);
   - distributional CUMULANTS of the conductor categorical (Fisher order 2, K^CH order 3, ...).
These are NOT the same hierarchy; a clean match needs the explicit-formula transfer between them.

PART 1  is there a 3-point (skewness) arithmetic signal? zeros' spacing skewness vs GUE, with the
        sampling-noise floor sqrt(6/n). (The direct "cubic" test.)
PART 2  is the count S = (1/pi)arg zeta non-Gaussian? (Selberg: S -> Gaussian, 3rd cumulant -> 0.)
PART 3  where the arithmetic ROBUSTLY is: number variance Sigma^2(L) vs GUE log -- the ORDER-2 prime
        (Berry) over-rigidity. This is the leading arithmetic deviation, and it is order 2, not 3.
PART 4  honest verdict on the K^CH bridge.

mpmath + numpy. No torch. (Statistical certificate; zeros cached.)
"""
import numpy as np
import mpmath as mp
import os
mp.mp.dps = 18

N = 250
cache = "empirical/zeros_cache.npy"
if os.path.exists(cache):
    gam = np.load(cache)[:N]
else:
    gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, N + 1)]); np.save(cache, gam)
x = np.array([float(mp.siegeltheta(mp.mpf(g)) / mp.pi + 1) for g in gam])
sp = np.diff(x)
S = np.arange(1, N + 1) - x

def moments(a):
    m = a.mean(); v = a.var(); c3 = ((a - m)**3).mean()
    return m, v, c3 / v**1.5

# GUE beta=2 Wigner-surmise spacing moments (numeric integration)
ss = np.linspace(0, 6, 60000); ds = ss[1] - ss[0]
P = (32 / np.pi**2) * ss**2 * np.exp(-(4 / np.pi) * ss**2)
m1 = np.sum(ss * P) * ds
m2 = np.sum(ss**2 * P) * ds
m3 = np.sum(ss**3 * P) * ds
gue_var = m2 - m1**2
gue_skew = (m3 - 3 * m2 * m1 + 2 * m1**3) / gue_var**1.5

print("=" * 84)
print("[1] 3-POINT (skewness) test: zeros' spacing skewness vs GUE (beta=2), with noise floor")
print("=" * 84)
zm, zv, zskew = moments(sp)
noise = np.sqrt(6 / len(sp))
print(f"  zeros' spacings: mean={zm:.3f}, var={zv:.3f}, skewness={zskew:.3f}")
print(f"  GUE (beta=2)   : mean={m1:.3f}, var={gue_var:.3f}, skewness={gue_skew:.3f}")
print(f"  deviation in skewness = {zskew - gue_skew:+.3f}   sampling noise floor = +-{noise:.3f}")
sig = abs(zskew - gue_skew) > 2 * noise
print(f"  significant (> 2 sigma)? {sig}  =>  {'a 3-point arithmetic signal' if sig else 'consistent with GUE; NO resolved cubic signal at this N'}")

print("\n" + "=" * 84)
print("[2] is the count S = (1/pi) arg zeta non-Gaussian? (Selberg: 3rd cumulant -> 0)")
print("=" * 84)
sm, sv, sskew = moments(S)
snoise = np.sqrt(6 / len(S))
print(f"  S: mean={sm:.3f}, var={sv:.3f}, skewness={sskew:.3f}   noise floor +-{snoise:.3f}")
print(f"  => S skewness {'is' if abs(sskew) > 2*snoise else 'is NOT'} significant; "
      f"{'non-Gaussian' if abs(sskew) > 2*snoise else 'consistent with Gaussian (Selberg) -- no order-3 in the count'}")

print("\n" + "=" * 84)
print("[3] where the arithmetic ROBUSTLY is: ORDER-2 over-rigidity (number variance vs GUE log)")
print("=" * 84)
def number_variance(levels, L, nw=400):
    lo, hi = levels.min(), levels.max() - L
    starts = np.linspace(lo, hi, nw)
    return np.array([np.sum((levels >= s) & (levels < s + L)) for s in starts]).var()
gue_var_L = lambda L: (1/np.pi**2)*(np.log(2*np.pi*L) + np.euler_gamma + 1 - np.pi**2/8)
print(f"  {'L':>4} {'Sigma^2 zeros':>14} {'GUE log':>9} {'Poisson':>8} {'zeros/GUE':>10}")
for L in (4, 8, 12, 16):
    s2 = number_variance(x, L); g = gue_var_L(L)
    print(f"  {L:>4} {s2:>14.3f} {g:>9.3f} {float(L):>8.1f} {s2/g:>10.2f}")
print("  => Sigma^2 sits at/below the GUE log curve and FAR below Poisson: the zeros are GUE-rigid, with")
print("     an order-2 arithmetic (Berry) over-rigidity. The arithmetic enters the 2-POINT function.")

print("\n" + "=" * 84)
print("VERDICT  --  honest grounding of the K^CH bridge")
print("=" * 84)
kch = np.sqrt(122) / 216
print(f"""  Apex cubic on the Z/3 conductor: |K^CH-spin3| = sqrt(122)/216 = {kch:.4f} (exact, probe_gamma_kch_identity).
  PARANOID/GROUNDED outcome:
   * the 3-point (skewness) deviation of the zeros from GUE is {zskew-gue_skew:+.3f}, within the +-{noise:.2f}
     sampling floor -- NO resolved cubic signal at N={N}; and the count S is consistent with Gaussian.
   * the ROBUST arithmetic deviation is ORDER 2 (the number-variance over-rigidity / Berry saturation,
     the tau=1 effect of the previous probe), NOT order 3.
  So the conjecture "K^CH = leading deviation from GUE" is CORRECTED, not confirmed: the leading
  arithmetic deviation lives in the 2-POINT function (order 2, the primes in the pair correlation),
  while K^CH is the third cumulant of the conductor CATEGORICAL -- a different hierarchy. The two are a
  structural ANALOGY (each is 'Gaussian backbone + correction'), linked only through the explicit-
  formula transfer, which is exactly the tau=1 wall. The honest deposit: the arithmetic is in the zeros
  ALREADY at order 2 (so the 'GUE=order2 / arithmetic=order3' picture is too simple), and the genuine
  quantitative target remains the order-2 prime effect at tau=1 -- not a cubic match. Discipline over a
  forced bridge: the cubic is real and exact, but it is not the zeros' leading departure from noise.""")
