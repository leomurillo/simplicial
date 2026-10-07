# The frontier located: sup_{k,n} r_k(n) at the n=0 corner ~ 0.9999

**Script:** `empirical/verify_cumulant_corner.py`
**Context:** locates the supremum of the cancellation ratio (the analytic-frontier bound).
**Finding:** sup is the k->inf limit at n=0 (the dominant low zeros); R(0) ~ 0.9999, marginal.
**Nature:** numerical (mpmath dps 50), labelled.  NOT a proof (R(0)<1 is RH).

```text
The frontier, located: sup_{k,n} r_k(n) lives at the n=0 corner, and equals ~0.9999.

Companion to verify_cumulant_frontier.  r_k(n)=|Delta^k A_n|/|Delta^k C_n| (arithmetic cumulant /
archimedean reference); RH <=> sup_{k,n} r_k(n) < 1.  r_k(n) is MONOTONE: increasing in k, decreasing
in n (verified there).  Hence the supremum is attained in the limit k->inf at the SMALLEST shift n=0
-- the lowest Jensen polynomials, governed by the DOMINANT LOW-LYING ZEROS (the biggest peaks).

This probe maps that corner directly: r_k(n) for small n and k up to 8, the grid max, and the n=0
increment structure with an extrapolation of R(0)=lim_{k->inf} r_k(0).

FINDING (honest): R(0) ~ 0.9999 -- one hair below 1.  Whether R(0)<1 (RH) or R(0)=1 (a zero off the
line) is exactly what finite k cannot decide: the increments shrink ~geometrically but their ratio
creeps up, so the tail is marginal.  This IS RH's marginality, pinned to a single point of the
Jensen tower.  NOT a proof; the frontier made as small and sharp as it goes.

NUMERICAL (mpmath dps 50), labelled.

================  THE HIGH CORNER : r_k(n), small n, k up to 8  ================
  (r_k rises in k, falls in n; the sup is the k->inf limit at the smallest n.)
   n      r_2    r_3    r_4    r_5    r_6    r_7    r_8
   0  0.9343  0.98074  0.9919  0.99592  0.9977  0.99861  0.9991
   1  0.88087  0.95427  0.97729  0.98713  0.99207  0.99482  0.99647
   2  0.84284  0.93015  0.96171  0.97662  0.98472  0.98952  0.99254
   3  0.81325  0.90864  0.94639  0.96549  0.97644  0.98323  0.98769
   4  0.78918  0.88952  0.93184  0.95434  0.96777  0.9764  0.98223
   5  0.76899  0.87244  0.9182  0.94346  0.95902  0.96929  0.9764
   6  0.75168  0.8571  0.90547  0.93299  0.95038  0.9621  0.97038
   7  0.73657  0.84321  0.89361  0.92299  0.94193  0.95495  0.96428
   8  0.7232  0.83057  0.88255  0.91346  0.93375  0.9479  0.95819

  max over tested grid = 0.9991043  at (k,n) = (8, 0)

================  THE n=0 CORNER : does R(0)=lim_k r_k(0) stay < 1 ?  ================
  r_k(0), k=2..8 : 0.934303, 0.980739, 0.991902, 0.995921, 0.997704, 0.998606, 0.999104
  increments     : 0.04644, 0.01116, 0.004019, 0.001783, 0.0009014, 0.0004987
  incr. ratios   : 0.2404, 0.36, 0.4437, 0.5055, 0.5532
  last increment 0.0004987, last ratio 0.5532 -> geometric tail ~ 0.0006175
  => R(0) = lim_{k->inf} r_k(0) ~ 0.99972176   (one hair below 1)

  HONEST: the increment ratios CREEP UP (toward ~0.6), so the geometric extrapolation is
  itself marginal -- R(0) could be just under 1 (RH) or reach 1 (a zero off the line). Finite
  k cannot decide.  This is RH's marginality, pinned to ONE point: the n=0 head of the Jensen
  tower = the dominant low-lying zeros = the biggest peaks.  sup_{k,n} r_k(n) = R(0) ~ 0.9999.

  RH  <=>  R(0) < 1  <=>  at the lowest shift, the arithmetic moment-log-curvature
  |Delta^k log a_0| stays strictly below the archimedean reference |Delta^k C_0| as k->inf
  -- the Riemann measure's curvature at the dominant low zeros never quite catches the
  Gamma-factor's.  Cornered to a single limit, value one hair under one; not crossed.
```
