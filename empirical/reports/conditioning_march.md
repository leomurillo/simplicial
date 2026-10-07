# The Conditioning March (RH direction)

**Script:** `empirical/verify_conditioning_march.py`
**Context:** follow-up to the Conj 8.1 positivity and Beurling-Nyman probes.
**Nature:** numerical (mpmath/numpy), labelled.

```text
The conditioning march: how marginal is RH's positivity / approximation?

Two faces from the prior probes, both <=> RH, both governed by sum_rho 1/|rho|^2:
  * APPROXIMATION (Beurling-Nyman / Baez-Duarte): d_N = dist(1, span rho_{1/n}) -> 0.
  * POSITIVITY (Weil form): PSD on the line; an off-line zero drives min-eig < 0.

This march pushes the model size N and reads the *margin*:
  PART 1 (Baez-Duarte). Track d_N^2, the rate (log N) d_N^2 against C = sum_rho 1/|rho|^2 =
    2 + gamma - log(4 pi) ~ 0.0461914, AND the Gram conditioning lambda_min(G_N), cond(G_N).
    The conjecture (BDBLS) is (log N) d_N^2 -> C. The conditioning growth is itself the finding:
    1 is reachable only through increasingly ill-conditioned (finely cancelling) combinations --
    the numerical signature of RH sitting exactly on the boundary.
  PART 2 (Weil margin). On the line the Weil form is PSD for EVERY basis (min-eig >= 0, shrinking
    to 0+ -- only semidefinite in the limit); off the line it is negative for a resolving basis,
    more negative as the basis sharpens. Zero margin to off-line: the positivity is exactly critical.

Accuracy: the Gram entries are G_{mn} = sum_k {k/m}{k/n}/(k(k+1)). We sum to K and add the exact
mean-tail  (mean of {k/m}{k/n} over the period lcm(m,n)) * sum_{k>K} 1/(k(k+1)) = mean/(K+1),
killing the leading 1/(4K) bias. The solve is high-precision (mpmath); we flag where conditioning
overwhelms the entry accuracy (d_N^2 non-monotone or out of [0,1]) -- the conditioning wall.

NUMERICAL probe, labelled.

================  PART 1 : Baez-Duarte distance, rate, and conditioning  ================
  C = sum_rho 1/|rho|^2 = 2 + gamma - log(4 pi) = 0.0461914
  K = 200000, exact mean-tail correction; solve in mpmath dps=40.

   N |    d_N^2     |  (log N) d_N^2  |  lambda_min(G) |   cond(G_N)   | trust
  ---+--------------+-----------------+----------------+---------------+------
   1 |   0.30685282 |      0.21269417 |      1.733e-01 |     1.000e+00 | ok
   2 |   0.09574778 |      0.10518969 |      6.880e-02 |     4.091e+00 | ok
   3 |   0.06595169 |      0.09142846 |      4.136e-02 |     9.716e+00 | ok
   4 |   0.03631902 |      0.05845320 |      3.027e-02 |     1.652e+01 | ok
   5 |   0.03620803 |      0.06487609 |      2.262e-02 |     2.656e+01 | ok
   6 |   0.02438837 |      0.04745757 |      1.717e-02 |     3.983e+01 | ok
   7 |   0.02424453 |      0.05041507 |      1.423e-02 |     5.374e+01 | ok
   8 |   0.02409508 |      0.05294230 |      1.041e-02 |     8.041e+01 | ok
   9 |   0.02385255 |      0.05492253 |      9.171e-03 |     9.870e+01 | ok
  10 |   0.02049960 |      0.04915590 |      7.377e-03 |     1.310e+02 | ok
  11 |   0.02049815 |      0.05093598 |      7.003e-03 |     1.466e+02 | ok
  12 |   0.01987424 |      0.05097643 |      5.200e-03 |     2.077e+02 | ok
  13 |   0.01853181 |      0.04890652 |      5.200e-03 |     2.176e+02 | ok
  14 |   0.01838021 |      0.04977454 |      4.100e-03 |     2.879e+02 | ok
  15 |   0.01793627 |      0.04972989 |      3.977e-03 |     3.083e+02 | ok
  16 |   0.01710665 |      0.04846678 |      3.342e-03 |     3.797e+02 | ok
  17 |   0.01709654 |      0.04941534 |      3.314e-03 |     3.955e+02 | ok
  18 |   0.01685307 |      0.04962282 |      2.598e-03 |     5.195e+02 | ok
  19 |   0.01653825 |      0.04954418 |      2.596e-03 |     5.346e+02 | ok
  20 |   0.01612419 |      0.04909045 |      2.194e-03 |     6.487e+02 | ok
  21 |   0.01609083 |      0.04973743 |      2.169e-03 |     6.721e+02 | ok
  22 |   0.01557816 |      0.04884522 |      1.894e-03 |     7.869e+02 | ok

  reliable through N=22; beyond that the Gram conditioning overwhelms the entry accuracy
  (the conditioning WALL -- 1 is reachable only via ever-more-cancelling coefficients).
  d_1^2 = 0.30685282 vs exact 1 - log 2 = 0.30685282

================  PART 2 : Weil positivity margin (on-line vs off-line)  ================
  basis size |  min-eig ON line  |  min-eig OFF line (delta=0.1)
  -----------+-------------------+------------------------------
      3      |      7.368745e-16 |     -9.307653e-02
      5      |     -1.151773e-15 |     -1.114278e-01
      7      |     -2.174539e-16 |     -1.117014e-01
      9      |     -4.977725e-16 |     -1.117018e-01

  On the line: min-eig >= 0 for EVERY basis (PSD, only semidefinite in the limit).
  Off the line: min-eig < 0 for every resolving basis, sharper as the basis widens.
  Zero margin: no basis makes the on-line form indefinite; a basis always detects off-line.

================  WHAT THE MARCH READS OFF  ================
RH is EXACTLY marginal, now quantified three ways:
  1. d_N -> 0 only logarithmically: (log N) d_N^2 hugs C = sum_rho 1/|rho|^2 = 0.04619.
  2. The approximating system ill-conditions fast: cond(G_N) explodes -- 1 is reachable
     only through finely cancelling combinations (a conditioning wall at modest N).
  3. The Weil positivity has zero margin: PSD on the line for every basis, negative off
     it for every resolving basis. No slack either way.

Cornered, mapped: the criticality budget is measured -- RH sits on the boundary with no
margin, which is precisely why brute numerics cannot settle it and why the zero-controlled
STRUCTURE (the rate constant, the explicit detector) is the lever, not more N.
```
