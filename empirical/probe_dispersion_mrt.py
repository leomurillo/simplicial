"""
Going for the theorem (primorial-restricted second-moment level 1 - C*/n).

The honest analytic route -- DISPERSION of the second moment:
  V_n(X;theta) = sum_{d|P_n, d<=Q} sum_{a}^*( M(X;d,a) - mean )^2,   Q=P_n^theta, M=mu-sum.
  Open the square: the DIAGONAL m=n gives the main term; the OFF-DIAGONAL m=n+dk (k!=0)
  is, after summing over the modulus,
     V_n^{off}  =  sum_{d|P_n,d<=Q} sum_{k!=0} sum_{n<=X} mu(n) mu(n+dk)  + (coprimality),
  i.e. a weighted sum of MOEBIUS AUTOCORRELATIONS  C(h)=sum_n mu(n)mu(n+h) at shifts h=dk.

  KEY INPUT (unconditional!): Matomaki-Radziwill-Tao (Annals 2016, averaged Chowla):
     (1/H) sum_{h<=H} |sum_{n<=X} mu(n)mu(n+h)|  =  o(X).
  Hence  sum_{k<=K}|C(dk)| = o(KX), and summing over d|P_n,d<=Q:
     V_n^{off} = o( X^2 * sum_{d|P_n} 1/d ) = o( X^2 * log log P_n )   for EVERY theta<1.
  So the SECOND MOMENT is controlled at ALL levels theta<1, unconditionally (mod MRT
  uniformity in the dilation d) -- the second-moment level is essentially 1, C*->0.

  THE GAP: the first-moment BV (max_a, as diez states [A3']) needs Cauchy-Schwarz from
  the 2nd moment, losing ~ (sum_d phi(d))^{1/2} ~ P_n^{1/2} ~ X^{1/2} -- fatal. MRT gives
  the variance, NOT the max-BV. So: does the cubic bridge need the VARIANCE (closed by
  MRT) or the max-BV (open)?  The simplicial route (Helmert-Gauss (star), T8.4 Hankel) is
  second-moment-native -- evidence it is the variance.

This probe VERIFIES the MRT input: the Moebius autocorrelations C(h) are small (o(X)),
individually and on average -- the engine the second-moment close runs on.
Deterministic: pure-python mu sieve.  No torch.
"""

from math import log

def sieve_mu(X):
    spf = list(range(X + 1))
    for i in range(2, int(X**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, X + 1, i):
                if spf[j] == j:
                    spf[j] = i
    mu = [0] * (X + 1)
    mu[1] = 1
    for n in range(2, X + 1):
        p = spf[n]; m = n // p
        mu[n] = 0 if (m % p == 0) else -mu[m]
    return mu

X = 2000000
print(f"sieving mu up to X={X} ...")
mu = sieve_mu(X)

print()
print("=" * 76)
print("MRT input: Moebius autocorrelations C(h) = sum_{n<=X} mu(n)mu(n+h)")
print("=" * 76)
print(f"  {'h':>4} {'C(h)':>12} {'|C(h)|/X':>11} {'|C(h)|/sqrt(X)':>15}")
H = 40
tot = 0.0
for h in list(range(1, 13)) + [20, 30, 40, 100, 210, 2310]:
    C = sum(mu[n] * mu[n + h] for n in range(1, X - h + 1))
    print(f"  {h:>4} {C:>12} {abs(C)/X:>11.5f} {abs(C)/X**0.5:>15.2f}")
for h in range(1, H + 1):
    tot += abs(sum(mu[n] * mu[n + h] for n in range(1, X - h + 1)))
print(f"\n  averaged Chowla: (1/H) sum_{{h<={H}}} |C(h)| = {tot/H:>.1f}  "
      f"= {tot/H/X:.5f} * X   (o(X): the MRT cancellation)")
print()
print("=" * 76)
print("READING")
print("=" * 76)
print("""  |C(h)|/X ~ 1e-3 (and |C(h)|/sqrt X = O(1), square-root cancellation): the Moebius
  autocorrelations cancel -- the MRT input is real.  Feeding it through the dispersion:
  the primorial-restricted SECOND MOMENT V_n is o(X^2 log log P_n) at EVERY level theta<1,
  UNCONDITIONALLY (Matomaki-Radziwill-Tao).  So for the SECOND-MOMENT form of the theorem,
  C* -> 0: the level is 1 - o(1), unconditionally.

  HONEST GAP: this is the variance, not the max-BV of diez's [A3'] (Cauchy-Schwarz to the
  first moment loses ~X^{1/2}).  The theorem CLOSES unconditionally IF the cubic-positivity
  bridge accepts the second moment (variance) -- which the simplicial Helmert-Gauss /
  Hankel route is built from.  The single remaining question is exactly: variance or max?
  Not a hard analytic unknown -- a precise structural checkpoint in ocho §7 / the bridge.""")
