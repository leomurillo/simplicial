# The analytic frontier: sup_{k,n} r_k(n) < 1 via tilted-moment cumulants

**Script:** `empirical/verify_cumulant_frontier.py`
**Context:** attempts the bound P0 sec8.2 / Conjecture 8.4 reduces RH to.
**Result:** provable fixed-k decay r_k(n)~C_k/log n -> 0; the crux is the growth of C_k/(k-2)!.
**Nature:** numerical (mpmath dps 70), labelled, pre-registered.  NOT a proof (uniform-in-k = RH).

```text
The analytic frontier: attempt sup_{k,n} r_k(n) < 1 via the tilted-moment cumulants.

From P0 sec8.2 / verify_cancellation_place_decomposition: with b_n=a_n n!/(2n)!, L_n=log b_n=C_n+A_n,
C_n=log(n!/(2n)!) (archimedean), A_n=log a_n (arithmetic), the cancellation is
    r_k(n) = |Delta^k A_n| / |Delta^k C_n| < 1   (archimedean Gamma-curvature beats arithmetic).
RH lives in sup_{k,n} r_k(n) < 1 (uniform-in-degree domination).

CGF / CUMULANT FRAMEWORK (the right language).  a_n = int_0^inf u^{2n} Phi du = int_0^inf s^n dnu(s)
(s=u^2, dnu=Phi du >= 0).  So a(t)=int s^t dnu is the MGF of the log-pushforward measure mu (in
x=log s), and A_n = log a_n = K(n) is its CUMULANT GENERATING FUNCTION.  By the finite-difference
mean value theorem, Delta^k A_n = K^{(k)}(theta) = kappa_k(mu_theta), the k-th CUMULANT of the
exponentially tilted measure d mu_t ~ s^t dnu, theta in (n, n+k).  In particular
  * kappa_2(mu_t) = Var >= 0  (re-proves log-convexity Delta^2 A >= 0),
  * the higher kappa_k carry the arithmetic (the zeros, via the Taylor coeffs of log Xi).

The archimedean side is explicit: Delta^k C_n ~ (-1)^{k+1} (k-2)! / n^{k-1}.  Hence
    r_k(n) ~ |kappa_k(mu_n)| n^{k-1} / (k-2)!.
A saddle analysis of a(t) (saddle u_t with u_t e^{2u_t} ~ t/pi) predicts the slowly-varying form
    kappa_k(n) ~ c_k / (n^{k-1} log n),   so   r_k(n) ~ (c_k/(k-2)!) / log n.

PREDICTIONS TO TEST (pre-registered):
  T1. kappa_2(n) * n * log n -> a constant (variance decays a full log faster than |Delta^2 C|~1/n).
  T2. For each fixed k, r_k(n) -> 0 as n -> inf (so any finite set of degrees is eventually safe;
      a rate-equipped strengthening of 'N(d) exists').  Specifically r_k(n) log n -> C_k.
  T3. THE CRUX: the growth of C_k = lim_n r_k(n) log n, equivalently C_k/(k-2)!.  If C_k/(k-2)! is
      BOUNDED, the archimedean reference dominates uniformly for large n; if it grows, the head
      (k large vs n) is where RH's content sits.  We extract C_k and watch C_k/(k-2)!.

NUMERICAL (mpmath dps 70), labelled.  NOT a proof: it makes the reduction explicit and tests the
provable (fixed-k) direction; the uniform-in-k growth of c_k is the arithmetic = RH.  Refutation kept.

Computing 88 Phi-moments (dps=70) ...
  done.

================  T1 : variance scaling  kappa_2(n) = Delta^2 A_n ~ c/(n log n)  ==========
   n        kappa_2(n)        kappa_2 * n          kappa_2 * n * ln n   (-> constant?)
    4   0.158366   0.633463   0.878166
    8   0.0804389   0.643511   1.33814
   16   0.0383577   0.613723   1.7016
   32   0.0176418   0.564539   1.95654
   48   0.0111008   0.532837   2.06272
   64   0.00797425   0.510352   2.12249
   80   0.00616533   0.493227   2.16133
  |Delta^2 C_n| ~ 1/n, so r_2(n) = kappa_2/|Delta^2 C| ~ (kappa_2 * n) ~ const/log n -> 0.

================  T2 : r_k(n) < 1, and r_k(n) -> 0 for each fixed k (r_k log n -> C_k)  =====
   n      r_2(n)    r_3(n)    r_4(n)    r_5(n)    r_6(n)
    4   0.78918   0.88952   0.93184   0.95434   0.96777
    8   0.7232   0.83057   0.88255   0.91346   0.93375
   16   0.65189   0.75803   0.81502   0.85207   0.87837
   32   0.58214   0.68048   0.73702   0.77609   0.80543
   48   0.54392   0.63597   0.6903   0.7288   0.75837
   64   0.51832   0.60553   0.65774   0.69524   0.72442
   80   0.49939   0.58278   0.63313   0.6696   0.69821

  g_k(n) := r_k(n) * ln n   (-> C_k if r_k ~ C_k/log n):
   n      g_2(n)    g_3(n)    g_4(n)    g_5(n)    g_6(n)
    4   1.094   1.2331   1.2918   1.323   1.3416
    8   1.5039   1.7271   1.8352   1.8995   1.9417
   16   1.8074   2.1017   2.2597   2.3624   2.4353
   32   2.0175   2.3584   2.5543   2.6897   2.7914
   48   2.1056   2.462   2.6723   2.8213   2.9358
   64   2.1556   2.5183   2.7355   2.8914   3.0128
   80   2.1883   2.5537   2.7744   2.9342   3.0596

================  T3 (THE CRUX) : C_k = lim_n r_k(n) ln n,  and  C_k / (k-2)!  ============
  Richardson-ish estimate C_k ~ g_k(n_max) (+ drift); watch whether C_k/(k-2)! is BOUNDED.
   k      g_k(48)    g_k(64)    g_k(80)    C_k(est)   (k-2)!     C_k/(k-2)!
   2   2.1056   2.1556   2.1883   2.7979   1.0   2.7979
   3   2.462   2.5183   2.5537   3.2134   1.0   3.2134
   4   2.6723   2.7355   2.7744   3.4993   2.0   1.7496
   5   2.8213   2.8914   2.9342   3.7313   6.0   0.62189
   6   2.9358   3.0128   3.0596   3.932   24.0   0.16383

  Reading: r_k(n)<1 throughout and r_k(n)->0 for each fixed k (T2) -- the provable direction,
  a rate-equipped 'every finite set of degrees is eventually safe'.  THE CRUX is the last
  column: if C_k/(k-2)! stays bounded, the archimedean reference dominates uniformly for large
  n; if it grows, the head (k large vs n) carries RH.  c_k is the arithmetic (the zeros, via
  the Taylor coefficients of log Xi); bounding its growth by (k-2)! is the open content.

================  WHAT THIS IS (honest)  ================
PROVABLE (modulo making the saddle rigorous): kappa_2>=0 (Cauchy-Schwarz); kappa_2~c/(n log n)
so r_2~C_2/log n->0; and for each FIXED k, r_k(n)~C_k/log n -> 0 (T1, T2).  This RE-DERIVES,
with an explicit 1/log n rate, that each Jensen degree is eventually hyperbolic.
IRREDUCIBLE = RH: the UNIFORM-in-k bound needs c_k <= (k-2)!(1-eps).  The archimedean/Gaussian
part of c_k (leading saddle of Phi) is <= (k-2)! by construction; the ARITHMETIC correction is
set by the zeros (kappa_k carries sum_rho (rho-1/2)^{-k}-type data).  sup_{k,n} r_k(n)<1 <=>
the arithmetic cumulant growth never exceeds the archimedean reference -- which is RH itself,
not a reduction to anything easier.  The frontier is exactly: bound the tilted-Riemann-measure
higher cumulants by the Gamma-reference rate, uniformly in order.
```
